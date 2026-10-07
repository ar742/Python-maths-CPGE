"""Vérifier les données pédagogiques réellement délivrées et leurs exports."""
import json
import threading
import unittest
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from chimie_organique import make_server

class ServeurTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0);cls.port=cls.server.server_port;cls.base=f'http://127.0.0.1:{cls.port}'
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join(3)
    def get(self,path,headers=None):
        with urlopen(Request(self.base+path,headers=headers or {}),timeout=8) as response:
            return response.status,response.read(),dict(response.headers)
    def post(self,data,headers=None):
        payload=json.dumps(data).encode('utf-8')
        with urlopen(Request(self.base+'/api/calculate',data=payload,headers=dict({'Content-Type':'application/json'},**(headers or {}))),timeout=8) as response:
            return response.status,json.load(response),dict(response.headers)
    def bootstrap(self): return json.loads(self.get('/api/bootstrap')[1])
    def test_cours_exercices_et_guides_reellement_disponibles(self):
        data=self.bootstrap();self.assertEqual(data['application'],'chimie_organique')
        ids={lab['id'] for lab in data['labs']}
        self.assertTrue({'rmn','sn2','dielsalder','retrosynthese','polymeres'}<=ids)
        self.assertEqual(ids,set(data['lab_guides']))
        for lesson in data['lessons']: self.assertIn(lesson['lab'],ids)
        for exercise in data['exercises']: self.assertIn(exercise['lab'],ids)
    def test_actifs_locaux_et_politique_de_contenu(self):
        for path in ['/','/app.js','/visuals.js','/style.css','/favicon.svg']:
            status,body,headers=self.get(path);self.assertEqual(status,200);self.assertTrue(body)
            self.assertIn("default-src 'self'",headers['Content-Security-Policy'])
        self.assertIn('Liaisons & Synthèses',self.get('/')[1].decode('utf-8'))
    def test_fichiers_internes_non_servis(self):
        for path in ['/cours.py','/modeles_analyse.py','/../AGENTS.md','/.git/config','/README.md']:
            with self.subTest(path=path),self.assertRaises(HTTPError) as raised: self.get(path)
            self.assertEqual(raised.exception.code,404)
    def test_calcul_authentifie_puis_export_identique(self):
        data=self.bootstrap();headers={'X-CPGE-Token':data['token'],'Origin':self.base}
        status,result,_=self.post({'lab':'extraction'},headers)
        self.assertEqual(status,200);self.assertEqual(result['lab'],'extraction')
        exported=json.loads(self.get('/api/export/'+result['export_id'])[1]);self.assertEqual(exported,result)
        self.assertTrue(result['assumptions'])
    def test_refus_token_ou_origine_non_autorises(self):
        token=self.bootstrap()['token']
        for headers in [{},{'X-CPGE-Token':'invalide'},{'X-CPGE-Token':token,'Origin':'https://example.com'}]:
            with self.subTest(headers=headers),self.assertRaises(HTTPError) as raised: self.post({'lab':'rmn'},headers)
            self.assertEqual(raised.exception.code,403)
    def test_validation_des_parametres_renvoyee_au_navigateur(self):
        token=self.bootstrap()['token']
        with self.assertRaises(HTTPError) as raised:
            self.post({'lab':'rmn','params':{'absent':1}},{'X-CPGE-Token':token,'Origin':self.base})
        self.assertEqual(raised.exception.code,400)
    def test_figures_referencees_presentes_et_servies(self):
        import xml.etree.ElementTree as ET
        data=self.bootstrap()
        self.assertEqual({lab['id'] for lab in data['labs']},{id_ for figure in data['figures'] for id_ in figure['labs']})
        for figure in data['figures']:
            status,body,_=self.get('/illustrations/'+figure['file']);self.assertEqual(status,200)
            self.assertEqual(ET.fromstring(body).tag,'{http://www.w3.org/2000/svg}svg')

if __name__=='__main__': unittest.main()
