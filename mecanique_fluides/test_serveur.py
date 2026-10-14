"""Contrats HTTP, protection du serveur local et instantané exporté."""
import json
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from mecanique_fluides import make_server


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
        h={"Content-Type":"application/json","X-Fluides-Token":self.server.api_token}
        h.update(headers or {})
        return urlopen(Request(self.base+path,data=payload,headers=h),timeout=10)

    def error(self,path,payload=None,headers=None):
        with self.assertRaises(HTTPError) as cm:self.request(path,payload,headers)
        try:return cm.exception.code
        finally:cm.exception.close()


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
        with self.request('/api/bootstrap') as r:data=json.load(r)
        self.assertEqual(data['application'],'fluides-ondes')
        self.assertEqual(len(data['labs']),18)
        self.assertEqual(set(data['lab_guides']),{l['id'] for l in data['labs']})
        for guide in data['lab_guides'].values():
            self.assertTrue(guide['objects']);self.assertTrue(guide['assumptions'])
        self.assertGreaterEqual(len(data['lessons']),28)
        self.assertGreaterEqual(len(data['exercises']),40)

    def test_assets_and_figures(self):
        for path in ['/','/app.js','/style.css','/favicon.svg']:
            with self.request(path) as r:
                self.assertEqual(r.status,200);self.assertTrue(r.read())
                self.assertIn("default-src 'self'",r.headers['Content-Security-Policy'])
        with self.request('/api/bootstrap') as r:figures=json.load(r)['figures']
        for f in figures:
            with self.request('/illustrations/'+f['file']) as r:
                self.assertIn('image/svg+xml',r.headers['Content-Type']);self.assertIn(b'<svg',r.read())

    def test_calculate_and_export(self):
        with self.request('/api',b'{"lab":"houle"}') as r:data=json.load(r)
        self.assertEqual(data['lab'],'houle')
        self.assertGreater(data['scene']['omega'],0)
        with self.request('/api/export/'+data['export_id']) as r:
            self.assertEqual(json.load(r),data)
            self.assertIn('attachment',r.headers['Content-Disposition'])

    def test_export_expiration(self):
        with self.request('/api',b'{"lab":"couette"}') as r:old=json.load(r)['export_id']
        for lab in ['houle','vortex','poiseuille','acoustique']:
            with self.request('/api',json.dumps({'lab':lab}).encode()) as r:json.load(r)
        self.assertEqual(self.error('/api/export/'+old),404)

    def test_origin_host_token(self):
        for h in [{'Origin':'https://example.org'},{'Host':'example.org'},{'X-Fluides-Token':''}]:
            self.assertEqual(self.error('/api',b'{}',h),403)
        self.assertEqual(self.error('/',headers={'Host':'example.org'}),403)

    def test_validation(self):
        for payload in [b'{',b'[]',b'{"nu":NaN}',b'{"lab":"absent"}',b'{"lab":"houle","h":-1}']:
            self.assertEqual(self.error('/api',payload),400)
        self.assertEqual(self.error('/api',b'{}',{'Content-Type':'text/plain'}),400)

    def test_source_files_private(self):
        for path in ['/cours.py','/modeles.py','/../README.md','/illustrations/../cours.py','/illustrations/README.md']:
            self.assertEqual(self.error(path),404)


if __name__=='__main__':unittest.main()
