"""Contrats HTTP, protection du serveur local et instantané exporté."""
import json
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from electromagnetisme import make_server


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.base=f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join(3)

    def request(self,path,payload=None,headers=None):
        h={"Content-Type":"application/json","X-EM-Token":self.server.api_token}
        h.update(headers or {})
        return urlopen(Request(self.base+path,data=payload,headers=h),timeout=10)

    def error(self,path,payload=None,headers=None):
        with self.assertRaises(HTTPError) as cm:self.request(path,payload,headers)
        try:return cm.exception.code
        finally:cm.exception.close()

    def test_bootstrap(self):
        with self.request('/api/bootstrap') as r:data=json.load(r)
        self.assertEqual(data['application'],'electromagnetisme')
        self.assertEqual(len(data['labs']),24)
        self.assertEqual(set(data['lab_guides']),{l['id'] for l in data['labs']})
        self.assertGreaterEqual(len(data['lessons']),36)
        self.assertGreaterEqual(len(data['exercises']),48)

    def test_assets_and_figures(self):
        for path in ['/','/app.js','/visuals.js','/style.css','/favicon.svg']:
            with self.request(path) as r:
                self.assertEqual(r.status,200);self.assertTrue(r.read())
                self.assertIn("default-src 'self'",r.headers['Content-Security-Policy'])
        with self.request('/api/bootstrap') as r:figures=json.load(r)['figures']
        for f in figures:
            with self.request('/illustrations/'+f['file']) as r:
                self.assertIn('image/svg+xml',r.headers['Content-Type']);self.assertIn(b'<svg',r.read())

    def test_calculate_and_export(self):
        with self.request('/api',b'{"lab":"hautparleur"}') as r:data=json.load(r)
        self.assertEqual(data['lab'],'hautparleur')
        self.assertGreater(data['scene']['omega'],0)
        with self.request('/api/export/'+data['export_id']) as r:
            self.assertEqual(json.load(r),data)
            self.assertIn('attachment',r.headers['Content-Disposition'])

    def test_export_expiration(self):
        with self.request('/api',b'{"lab":"dipoles"}') as r:old=json.load(r)['export_id']
        for lab in ['maxwell','drude','hall','hautparleur']:
            with self.request('/api',json.dumps({'lab':lab}).encode()) as r:json.load(r)
        self.assertEqual(self.error('/api/export/'+old),404)

    def test_origin_host_token(self):
        for h in [{'Origin':'https://example.org'},{'Host':'example.org'},{'X-EM-Token':''}]:
            self.assertEqual(self.error('/api',b'{}',h),403)
        self.assertEqual(self.error('/',headers={'Host':'example.org'}),403)

    def test_validation(self):
        for payload in [b'{',b'[]',b'{"lab":"maxwell","amplitude":NaN}',b'{"lab":"absent"}',b'{"lab":"maxwell","amplitude":-1}']:
            self.assertEqual(self.error('/api',payload),400)
        self.assertEqual(self.error('/api',b'{}',{'Content-Type':'text/plain'}),400)

    def test_source_files_private(self):
        for path in ['/cours.py','/modeles.py','/../README.md','/illustrations/../cours.py','/illustrations/README.md']:
            self.assertEqual(self.error(path),404)


if __name__=='__main__':unittest.main()
