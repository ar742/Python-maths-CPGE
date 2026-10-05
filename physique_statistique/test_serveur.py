import json
import unittest
import threading
from urllib.request import Request, OpenerDirector, HTTPHandler, HTTPDefaultErrorHandler, HTTPErrorProcessor
from urllib.error import HTTPError
from physique_statistique import make_server

# Ces tests ne contactent que HTTP sur la boucle locale : aucun contexte TLS.
local_http = OpenerDirector()
for handler in [HTTPHandler(), HTTPDefaultErrorHandler(), HTTPErrorProcessor()]:
    local_http.add_handler(handler)
urlopen = local_http.open


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.url=f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join(timeout=2)

    def request(self,path="/",payload=None,headers=None):
        h={"Content-Type":"application/json","X-Statistique-Token":self.server.api_token};h.update(headers or {})
        return urlopen(Request(self.url+path,data=payload,headers=h),timeout=10)

    def test_bootstrap(self):
        with self.request("/api/bootstrap") as r:data=json.load(r)
        self.assertEqual(data["application"],"physique-statistique")
        self.assertEqual(len(data["lessons"]),16);self.assertEqual(len(data["exercises"]),24)

    def test_static_assets(self):
        for path in ["/","/app.js","/style.css","/favicon.svg"]:
            with self.request(path) as r:
                self.assertGreater(len(r.read()),100);self.assertIn("script-src 'self'",r.headers["Content-Security-Policy"])

    def test_valid_api(self):
        with self.request("/api",b'{"lab":"canonique"}') as r:data=json.load(r)
        self.assertEqual(data["lab"],"canonique")

    def test_token_host_origin(self):
        for h in [{"X-Statistique-Token":""},{"Host":"example.org"},{"Origin":"https://example.org"}]:
            with self.assertRaises(HTTPError) as cm:self.request("/api",b"{}",h)
            self.assertEqual(cm.exception.code,403)

    def test_bad_json(self):
        for payload in [b"{",b"[]",b'{"r":NaN}',b'{"temperature":0}']:
            with self.assertRaises(HTTPError) as cm:self.request("/api",payload)
            self.assertEqual(cm.exception.code,400)

    def test_snapshot_download_and_expiry(self):
        with self.request("/api",b'{"lab":"canonique"}') as r:data=json.load(r)
        with self.request("/api/export/"+data["export_id"]) as r:
            self.assertIn("attachment;",r.headers["Content-Disposition"]);self.assertEqual(json.load(r),data)
        for _ in range(4):
            with self.request("/api",b'{"lab":"canonique"}') as r:json.load(r)
        with self.assertRaises(HTTPError) as cm:self.request("/api/export/"+data["export_id"])
        self.assertEqual(cm.exception.code,404)

    def test_private_files_not_served(self):
        for path in ["/cours.py","/../README.md","/COURS.md"]:
            with self.assertRaises(HTTPError) as cm:self.request(path)
            self.assertEqual(cm.exception.code,404)


if __name__=="__main__":unittest.main()
