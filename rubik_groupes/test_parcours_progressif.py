"""Contrôles de navigation et de cohérence du parcours autonome."""
import importlib
import json
from pathlib import Path
import threading
import unittest
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse
from urllib.request import urlopen

from parcours_progressif import PROGRESSION, LAB_LINKS
from reperes import LAB_GUIDES
from cours import LESSONS

ROOT = Path(__file__).resolve().parent
APPLICATION = importlib.import_module(ROOT.name)


class ParcoursProgressifTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = APPLICATION.make_server(0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=3)
        cls.server.server_close()

    def read(self, path):
        with urlopen(self.url + path, timeout=5) as response:
            return response.headers['Content-Type'], response.read().decode('utf8')

    def test_seances_et_tp_reels(self):
        valid = set(LAB_GUIDES)
        if ROOT.name == 'rubik_groupes':
            valid.update(lesson['id'] for lesson in LESSONS)
        ids = [link['id'] for link in LAB_LINKS]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(set(ids) <= valid)
        sessions = [session for stage in PROGRESSION['stages'] for session in stage['sessions']]
        self.assertEqual(len(sessions), len({s['id'] for s in sessions}))
        for session in sessions:
            self.assertTrue(set(session['labs']) <= set(ids))
            self.assertTrue(session['labs'])
            self.assertIn(session['status'], {'socle', 'approfondissement', 'prolongement'})
            for field in ['objective', 'task', 'success', 'limits']:
                self.assertGreater(len(session[field]), 30)
        self.assertGreaterEqual(sum(s['status'] == 'socle' for s in sessions), 5)
        self.assertGreaterEqual(sum(s['status'] == 'prolongement' for s in sessions), 2)
        json.dumps(PROGRESSION, ensure_ascii=False, allow_nan=False)

    def test_liens_locaux_et_retour(self):
        for link in LAB_LINKS:
            parsed = urlparse(link['href'])
            self.assertEqual(parsed.path, '/')
            self.assertFalse(parsed.netloc)
            self.assertEqual(parse_qs(parsed.query), {'tp': [link['id']]})
        self.assertIn('seance=', (ROOT/'parcours.js').read_text(encoding='utf8'))
        source = (ROOT/'app.js').read_text(encoding='utf8')
        self.assertIn("get('tp')", source)
        self.assertIn("'/parcours#'", source)

    def test_document_issu_des_memes_donnees(self):
        document = (ROOT/'PARCOURS_PROGRESSIF.md').read_text(encoding='utf8')
        for stage in PROGRESSION['stages']:
            self.assertIn(stage['title'], document)
            for session in stage['sessions']:
                self.assertIn(session['title'], document)
                self.assertIn(session['limits'], document)
        self.assertIn('export_progression()', (ROOT/'export_cours.py').read_text(encoding='utf8'))

    def test_bootstrap_charge_le_parcours(self):
        mime, content = self.read('/api/bootstrap')
        self.assertIn('application/json', mime)
        data = json.loads(content)
        self.assertEqual(data['progression'], PROGRESSION)
        self.assertEqual(data['progression_links'], LAB_LINKS)

    def test_routes_et_types_des_assets(self):
        for path, expected in [('/parcours','text/html'),('/parcours.html','text/html'),
                               ('/parcours.css','text/css'),('/parcours.js','text/javascript')]:
            mime, content = self.read(path)
            self.assertIn(expected, mime)
            self.assertTrue(content.strip())
        self.assertIn('Parcours sup / spé', self.read('/')[1])

    def test_fichiers_sources_prives_ne_sont_pas_exposes(self):
        for path in ['/parcours_progressif.py', '/export_progression.py', '/parcours/../../cours.py']:
            with self.assertRaises(HTTPError) as caught:
                self.read(path)
            self.assertEqual(caught.exception.code, 404)


if __name__ == '__main__':
    unittest.main()
