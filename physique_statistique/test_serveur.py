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


    def test_progression_covers_every_lab_with_distinct_levels(self):
        from parcours_progressif import PROGRESSION, LAB_LINKS
        from reperes import LAB_GUIDES
        links={link['id']:link for link in LAB_LINKS}
        self.assertEqual(len(links),len(LAB_LINKS))
        self.assertEqual(set(links),set(LAB_GUIDES))
        covered=set();sessions=set();statuses=set()
        for stage in PROGRESSION['stages']:
            for session in stage['sessions']:
                self.assertNotIn(session['id'],sessions);sessions.add(session['id'])
                statuses.add(session['status'])
                self.assertTrue(session['labs'])
                for field in ['objective','task','success','limits']:
                    self.assertGreater(len(session[field]),25)
                for lab in session['labs']:
                    self.assertIn(lab,links);covered.add(lab)
                    self.assertEqual(links[lab]['href'],'/?tp='+lab)
        self.assertEqual(covered,set(links))
        self.assertEqual(statuses,{'socle','approfondissement','prolongement'})
        json.dumps(PROGRESSION,allow_nan=False)
        with self.request('/api/bootstrap') as response:
            data=json.load(response)
        self.assertEqual(data['progression'],PROGRESSION)
        self.assertEqual(data['progression_links'],LAB_LINKS)

    def test_progression_routes_assets_and_direct_entries(self):
        from parcours_progressif import LAB_LINKS
        for path in ['/parcours','/parcours.html','/parcours.js','/parcours.css','/?tp=unknown&seance=unknown']+[l['href'] for l in LAB_LINKS]:
            with self.request(path) as response:
                self.assertEqual(response.status,200)
                self.assertGreater(len(response.read()),100)
                self.assertIn("script-src 'self'",response.headers['Content-Security-Policy'])
        for path in ['/parcours_progressif.py','/export_progression.py']:
            with self.assertRaises(HTTPError) as caught:
                self.request(path)
            self.assertEqual(caught.exception.code,404)
            caught.exception.close()

    def test_progression_document_and_generator_stay_consistent(self):
        from pathlib import Path
        from parcours_progressif import PROGRESSION
        root=Path(__file__).resolve().parent
        document=(root/'PARCOURS_PROGRESSIF.md').read_text(encoding='utf8')
        for stage in PROGRESSION['stages']:
            for session in stage['sessions']:
                self.assertIn(session['title'],document)
                self.assertIn(session['limits'],document)
        self.assertIn('export_progression()', (root/'export_cours.py').read_text(encoding='utf8'))
        self.assertIn("'/parcours#'", (root/'app.js').read_text(encoding='utf8'))
        self.assertIn('Parcours sup / spé',(root/'index.html').read_text(encoding='utf8'))

    def test_bootstrap(self):
        with self.request("/api/bootstrap") as r:data=json.load(r)
        self.assertEqual(data["application"],"physique-statistique")
        self.assertEqual(len(data["lessons"]),16);self.assertEqual(len(data["exercises"]),24)
        guides=data['lab_guides']
        self.assertEqual(set(guides), {lesson['lab'] for lesson in data['lessons']})
        for guide in guides.values():
            self.assertTrue(guide['objects']);self.assertTrue(guide['assumptions'])
            self.assertEqual(len(guide['first_steps']),3)
            self.assertEqual(set(guide['levels']),{'sup','spe','beyond'})

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
