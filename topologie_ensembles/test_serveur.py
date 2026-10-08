"""Serveur réel sur un port éphémère : contenu, validation et export JSON."""
import contextlib
import io
import json
from http.client import HTTPConnection
from pathlib import Path
import threading
import unittest
from unittest.mock import Mock, patch
import xml.etree.ElementTree as ET
import topologie_ensembles as application


class ServeurTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = application.make_server(0)
        cls.port = cls.server.server_port
        cls.base = f'http://127.0.0.1:{cls.port}'
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(3)

    def request(self, method, path, body=None, headers=None):
        connection = HTTPConnection('127.0.0.1', self.port, timeout=8)
        try:
            connection.request(method, path, body=body, headers=headers or {})
            response = connection.getresponse()
            return response.status, response.read(), dict(response.getheaders())
        finally:
            connection.close()

    def bootstrap(self):
        status, body, _ = self.request('GET', '/api/bootstrap')
        self.assertEqual(status, 200)
        return json.loads(body)

    def post(self, data, headers=None, path='/api/calculate'):
        return self.request('POST', path, json.dumps(data).encode('utf8'),
                            {'Content-Type': 'application/json', **(headers or {})})

    def authorized(self):
        return {'X-CPGE-Token': self.bootstrap()['token'], 'Origin': self.base}

    def test_pedagogical_content_and_links_to_experiences(self):
        data = self.bootstrap()
        self.assertEqual(data['application'], 'topologie_ensembles')
        ids = {lab['id'] for lab in data['labs']}
        self.assertEqual(len(ids), 30)
        self.assertEqual(ids, set(data['lab_guides']))
        self.assertEqual(ids, {lesson['lab'] for lesson in data['lessons']})
        self.assertEqual(ids, {exercise['lab'] for exercise in data['exercises']})
        self.assertGreaterEqual(len(data['lessons']), len(ids))
        self.assertGreaterEqual(len(data['exercises']), 2 * len(ids))
        self.assertTrue(data['sources'])
        for lesson in data['lessons']:
            self.assertTrue(lesson['title'])
            self.assertTrue(lesson['html'])
        for exercise in data['exercises']:
            self.assertTrue(exercise['question'])
            self.assertTrue(exercise['answer'])

    def test_guides_explain_objects_levels_and_course_links(self):
        data = self.bootstrap()
        for lab_id, guide in data['lab_guides'].items():
            with self.subTest(lab=lab_id):
                for key in ['purpose', 'expected', 'objects', 'assumptions', 'techniques']:
                    self.assertTrue(guide[key], key)
                self.assertGreaterEqual(len(guide['first_steps']), 3)
                for level in ['sup', 'spe', 'beyond']:
                    self.assertTrue(guide['levels'][level])
                self.assertTrue(guide['lesson_numbers'])
                linked_labs = set()
                for number in guide['lesson_numbers']:
                    self.assertIsInstance(number, int)
                    self.assertGreaterEqual(number, 1)
                    self.assertLessEqual(number, len(data['lessons']))
                    linked_labs.add(data['lessons'][number - 1]['lab'])
                self.assertIn(lab_id, linked_labs)

    def test_static_assets_and_response_headers(self):
        types = {'/': 'text/html', '/index.html': 'text/html', '/style.css': 'text/css',
                 '/app.js': 'text/javascript', '/visuals.js': 'text/javascript', '/favicon.svg': 'image/svg+xml'}
        for path, mime in types.items():
            with self.subTest(path=path):
                status, body, headers = self.request('GET', path)
                self.assertEqual(status, 200)
                self.assertTrue(body)
                self.assertTrue(headers['Content-Type'].startswith(mime))
                self.assertEqual(int(headers['Content-Length']), len(body))
                self.assertEqual(headers['Cache-Control'], 'no-store')
                self.assertEqual(headers['X-Content-Type-Options'], 'nosniff')
                self.assertIn("default-src 'self'", headers['Content-Security-Policy'])
                self.assertIn("object-src 'none'", headers['Content-Security-Policy'])
                self.assertIn("frame-ancestors 'none'", headers['Content-Security-Policy'])
        self.assertIn('Topologie', self.request('GET', '/')[1].decode('utf8'))

    def test_figures_are_well_formed_and_cover_labs(self):
        data = self.bootstrap()
        self.assertEqual({l['id'] for l in data['labs']}, {lab for figure in data['figures'] for lab in figure['labs']})
        names = [f['file'] for f in data['figures']]
        self.assertEqual(len(names), len(set(names)))
        for figure in data['figures']:
            self.assertEqual(figure['file'], Path(figure['file']).name)
            self.assertTrue(figure['file'].endswith('.svg'))
            status, body, headers = self.request('GET', '/illustrations/' + figure['file'])
            self.assertEqual(status, 200)
            self.assertEqual(headers['Content-Type'], 'image/svg+xml')
            self.assertEqual(ET.fromstring(body).tag, '{http://www.w3.org/2000/svg}svg')

    def test_internal_files_are_not_exposed(self):
        for path in ['/cours.py', '/modeles.py', '/README.md', '/.git/config', '/../AGENTS.md',
                     '/%2e%2e/AGENTS.md', '/illustrations/../cours.py', '/illustrations/catalogue.json',
                     '/illustrations/README.md', '/illustrations/inconnu.svg']:
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', path)[0], 404)

    def test_query_string_on_bootstrap_does_not_change_result(self):
        status, body, _ = self.request('GET', '/api/bootstrap?lecture=1')
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body), self.bootstrap())

    def test_successful_calculation_and_identical_download(self):
        status, body, _ = self.post({'lab': 'boules_normes'}, self.authorized())
        self.assertEqual(status, 200)
        result = json.loads(body)
        self.assertEqual(result['lab'], 'boules_normes')
        self.assertTrue(result['assumptions'])
        status, body, headers = self.request('GET', '/api/export/' + result['export_id'])
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body), result)
        self.assertIn('attachment;', headers['Content-Disposition'])
        self.assertIn('topologie_ensembles-boules_normes.json', headers['Content-Disposition'])

    def test_only_last_four_calculations_can_be_downloaded(self):
        authorization = self.authorized()
        results = []
        for radius in [.3, .4, .5, .6, .7]:
            status, body, _ = self.post({'lab': 'boules_normes', 'params': {'radius': radius}}, authorization)
            self.assertEqual(status, 200)
            results.append(json.loads(body))
        self.assertEqual(self.request('GET', '/api/export/' + results[0]['export_id'])[0], 404)
        for result in results[1:]:
            status, body, _ = self.request('GET', '/api/export/' + result['export_id'])
            self.assertEqual(status, 200)
            self.assertEqual(json.loads(body), result)

    def test_unknown_export_is_reported_as_expired(self):
        status, body, _ = self.request('GET', '/api/export/inconnu')
        self.assertEqual(status, 404)
        self.assertIn('expiré', json.loads(body)['error'])

    def test_missing_or_wrong_token_rejected(self):
        for authorization in [{}, {'X-CPGE-Token': 'invalide'}]:
            with self.subTest(authorization=authorization):
                self.assertEqual(self.post({'lab': 'boules_normes'}, authorization)[0], 403)

    def test_origin_restriction_and_localhost_allowed(self):
        headers = self.authorized()
        status, _, _ = self.post({'lab': 'boules_normes'}, {**headers, 'Origin': 'https://example.org'})
        self.assertEqual(status, 403)
        status, _, _ = self.post({'lab': 'boules_normes'}, {**headers, 'Origin': f'http://localhost:{self.port}'})
        self.assertEqual(status, 200)
        headers.pop('Origin')
        self.assertEqual(self.post({'lab': 'boules_normes'}, headers)[0], 200)

    def test_host_restriction_on_get_and_post(self):
        bad_host = {'Host': f'example.org:{self.port}'}
        self.assertEqual(self.request('GET', '/api/bootstrap', headers=bad_host)[0], 403)
        self.assertEqual(self.post({'lab': 'boules_normes'}, {**self.authorized(), **bad_host})[0], 403)
        self.assertEqual(self.request('GET', '/api/bootstrap', headers={'Host': f'localhost:{self.port}'})[0], 200)

    def test_post_destination_must_match_exact_endpoint(self):
        for path in ['/api/bootstrap', '/inconnu', '/api/calculate?query=1']:
            with self.subTest(path=path):
                self.assertEqual(self.post({'lab': 'boules_normes'}, self.authorized(), path)[0], 403)

    def test_bad_json_and_nonfinite_constants_rejected(self):
        headers = {**self.authorized(), 'Content-Type': 'application/json'}
        for payload in [b'{', b'[]', b'null', b'\xff', b'{"lab":"boules_normes","radius":NaN}',
                        b'{"lab":"boules_normes","radius":Infinity}', b'{"lab":"boules_normes","radius":-Infinity}',
                        b'{"lab":"boules_normes","radius":1e400}']:
            with self.subTest(payload=payload):
                status, body, _ = self.request('POST', '/api/calculate', payload, headers)
                self.assertEqual(status, 400)
                self.assertTrue(json.loads(body)['error'])

    def test_bad_params_produce_explanatory_http_400(self):
        for data in [{'lab': 'absent'}, {'lab': 'boules_normes', 'params': []},
                     {'lab': 'boules_normes', 'radius': True}, {'lab': 'boules_normes', 'radius': 0},
                     {'lab': 'boules_normes', 'params': {'absent': 1}}, {'lab': 'adherence_suite', 'N': 2.5}]:
            with self.subTest(data=data):
                status, body, _ = self.post(data, self.authorized())
                self.assertEqual(status, 400)
                self.assertTrue(json.loads(body)['error'])

    def test_content_type_is_required_and_charset_allowed(self):
        headers = self.authorized()
        self.assertEqual(self.post({'lab': 'boules_normes'}, {**headers, 'Content-Type': 'text/plain'})[0], 400)
        self.assertEqual(self.post({'lab': 'boules_normes'}, {**headers, 'Content-Type': 'application/json; charset=utf-8'})[0], 200)

    def test_invalid_or_oversized_content_length_rejected(self):
        headers = {**self.authorized(), 'Content-Type': 'application/json'}
        for length in ['0', '-1', '20001', 'absent']:
            with self.subTest(length=length):
                status, _, _ = self.request('POST', '/api/calculate', b'{}', {**headers, 'Content-Length': length})
                self.assertEqual(status, 400)

    def test_port_cannot_be_claimed_by_a_second_server(self):
        with self.assertRaises(OSError):
            application.make_server(self.port)


class LancementTests(unittest.TestCase):
    def test_invalid_port_fails_before_opening_any_browser(self):
        for port in ['-1', '65536']:
            with self.subTest(port=port), patch('sys.argv', ['programme', '--port', port, '--no-browser']), \
                 patch.object(application, 'make_server') as make, patch.object(application.webbrowser, 'open') as browser, \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
                application.main()
            self.assertEqual(raised.exception.code, 2)
            make.assert_not_called()
            browser.assert_not_called()

    def test_relaunch_recognizes_own_application_and_closes_probe(self):
        connection = Mock()
        connection.getresponse.return_value.read.return_value = b'{"application":"topologie_ensembles"}'
        output = io.StringIO()
        with patch('sys.argv', ['programme', '--port', '12345', '--no-browser']), \
             patch.object(application, 'make_server', side_effect=OSError('occupé')), \
             patch.object(application, 'HTTPConnection', return_value=connection), \
             patch.object(application.webbrowser, 'open') as browser, contextlib.redirect_stdout(output):
            application.main()
        self.assertIn('fonctionne déjà', output.getvalue())
        self.assertIn('127.0.0.1:12345', output.getvalue())
        connection.close.assert_called_once()
        browser.assert_not_called()

    def test_relaunch_does_not_confuse_another_application(self):
        connection = Mock()
        connection.getresponse.return_value.read.return_value = b'{"application":"autre_atelier"}'
        with patch('sys.argv', ['programme', '--port', '12345', '--no-browser']), \
             patch.object(application, 'make_server', side_effect=OSError('occupé')), \
             patch.object(application, 'HTTPConnection', return_value=connection), \
             patch.object(application.webbrowser, 'open') as browser, contextlib.redirect_stderr(io.StringIO()), \
             self.assertRaises(SystemExit) as raised:
            application.main()
        self.assertEqual(raised.exception.code, 1)
        connection.close.assert_called_once()
        browser.assert_not_called()


if __name__ == '__main__':
    unittest.main()
