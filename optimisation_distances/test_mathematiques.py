"""Références analytiques, invariances et contrôles globaux indépendants."""
import http.client
import json
import math
import threading
import unittest
import numpy as np

import mathematiques as m
from optimisation_distances import make_server


class ApproximationTests(unittest.TestCase):
    def test_tp_analytique_et_integrale_independante(self):
        L = math.pi/2
        d = m.approximation({})
        a, b = m.affine_exact(L)
        np.testing.assert_allclose(d['coefficients'], [b, a], atol=2e-14)
        # Simpson composite, distinct de la quadrature de Gauss du moteur.
        t = np.linspace(0, L, 10001)
        y = (np.cos(t)-a*t-b)**2
        I = L/30000*(y[0]+y[-1]+4*sum(y[1:-1:2])+2*sum(y[2:-1:2]))
        self.assertAlmostEqual(d['I'], I, places=13)
        self.assertAlmostEqual(d['distance']**2, I, places=13)

    def test_orthogonalite_ponderee_et_emboitement(self):
        for k in [-.8, 0, 4]:
            errors = []
            for degree in range(7):
                d = m.approximation({'poids': k, 'degre': degree})
                self.assertLess(max(abs(x) for x in d['orthogonalite']), 3e-14)
                errors.append(d['I'])
            self.assertTrue(all(a>=b for a,b in zip(errors,errors[1:])))

    def test_minimax_alternance(self):
        for L in [.3, 1, math.pi/2]:
            d = m.affine_uniforme(L)
            residual = [math.cos(t)-d['a']*t-d['b'] for t in [0,d['contact'],L]]
            np.testing.assert_allclose(residual, [-d['erreur'],d['erreur'],-d['erreur']], atol=2e-15)
            a,b = m.affine_exact(L)
            self.assertGreater(m.norme_uniforme_affine(a,b,L),d['erreur'])

    def test_conditionnement_et_descente(self):
        d=m.approximation({'degre':6})
        self.assertGreater(d['condition_gram'],1e6)
        self.assertLess(d['condition_design'],1.01)
        h=d['descente']
        self.assertTrue(all(a[2]>=b[2]-1e-14 for a,b in zip(h,h[1:])))
        self.assertLess(np.linalg.norm(np.array(h[-1][:2])-d['affine_optimum']),.001)

    def test_encadrement_sup_polynome(self):
        d=m.approximation({'degre':3,'poids':2})
        t=np.linspace(0,d['L'],30001)
        sup=np.max(abs(np.cos(t)-np.polynomial.polynomial.polyval(t,d['coefficients'])))
        self.assertLessEqual(d['sup']-1e-13,sup)
        self.assertLessEqual(sup,d['sup_upper'])


class MatricesTests(unittest.TestCase):
    def test_projection_complexe_pythagore(self):
        rng=np.random.default_rng(42)
        M=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5))
        S,A=m.decomposition(M)
        self.assertLess(abs(np.vdot(S,A)),1e-13)
        T=rng.normal(size=(5,5))+1j*rng.normal(size=(5,5));T=(T+T.T)/2
        self.assertAlmostEqual(np.linalg.norm(M-T)**2,np.linalg.norm(A)**2+np.linalg.norm(S-T)**2,places=11)
        self.assertGreater(np.linalg.norm(S-S.conj().T),1)

    def test_rotation_extrema(self):
        for theta,value in [(0,0),(90,math.sqrt(2)),(180,0),(-30,1/math.sqrt(2))]:
            self.assertAlmostEqual(m.matrices({'theta':theta})['distance_rotation'],value)

    def test_dimensions_impaires_vides(self):
        for n in [3,5,7,9]:
            d=m.matrices({'n':n})
            self.assertTrue(d['vide']);self.assertIsNone(d['distance_ensemble'])
            json.dumps(d,allow_nan=False)

    def test_determinant_borne_et_egalite_complexe(self):
        for n in [2,4,6,10]:
            for eta in [0,1.2]:
                d=m.matrices({'n':n,'complexe':True,'phase':65,'eta':eta})
                np.testing.assert_allclose(d['determinant'],[1,0],atol=2e-14)
                self.assertGreaterEqual(d['norme']+1e-13,math.sqrt(n))
                if eta==0 or n==2:self.assertTrue(d['egalite'])

    def test_non_compacite(self):
        norms=[m.matrices({'n':4,'eta':v})['norme'] for v in [0,1,2]]
        self.assertTrue(norms[0]<norms[1]<norms[2])


class ProduitTests(unittest.TestCase):
    def test_sphere_et_volume(self):
        d=m.produit({'axes':[1,1,1]})
        self.assertAlmostEqual(d['maximum'],1/(3*math.sqrt(3)))
        self.assertAlmostEqual(d['volume_boite'],8*d['maximum'])

    def test_huit_maximiseurs_pondere(self):
        d=m.produit({'axes':[3,2,1],'puissances':[2,1,1]})
        self.assertEqual(len(d['maximiseurs']),8)
        self.assertAlmostEqual(d['maximum'],9*2/8)
        for p in d['maximiseurs']:
            self.assertAlmostEqual(sum((np.array(p)/d['axes'])**2),1)
            self.assertAlmostEqual(p[0]**2*abs(p[1]*p[2]),d['maximum'])

    def test_borne_globale_echantillon(self):
        d=m.produit({'axes':[3,2,1],'puissances':[.4,2,1.6]})
        rng=np.random.default_rng(5);u=rng.normal(size=(5000,3));u/=np.linalg.norm(u,axis=1)[:,None]
        values=np.prod(abs(u*np.array(d['axes']))**np.array(d['puissances']),axis=1)
        self.assertLessEqual(max(values),d['maximum'])


class PointTests(unittest.TestCase):
    def test_sphere_interieur_exterieur_centre(self):
        for p in [[4,0,0],[.5,0,0],[0,0,0]]:
            d=m.point_ellipsoide({'axes':[2,2,2],'point':p})
            self.assertAlmostEqual(d['minimum']['distance'],abs(np.linalg.norm(p)-2))
            self.assertAlmostEqual(d['maximum']['distance'],np.linalg.norm(p)+2)
            self.assertAlmostEqual(d['distance_solide'],max(0,np.linalg.norm(p)-2))

    def test_cas_singuliers_et_axes_repetes(self):
        for axes in [[3,2,1],[3,3,1],[3,1,1]]:
            d=m.point_ellipsoide({'axes':axes,'point':[0,0,0]})
            self.assertEqual(d['minimum']['distance'],min(axes))
            self.assertEqual(d['maximum']['distance'],max(axes))
            self.assertTrue(d['minimum']['cas_singulier'])
            self.assertTrue(d['maximum']['cas_singulier'])

    def test_composantes_nulles_et_pole_non_solution(self):
        for p in [[.1,0,0],[10,0,0],[0,4,0],[0,0,8]]:
            for maximum in [False,True]:
                e=m.extremum_surface(p,[0,0,0],[3,2,1],np.eye(3),maximum)
                self.assertLess(e['contrainte'],1e-12)
                self.assertLess(e['stationnarite'],1e-11)
                self.assertGreaterEqual(e['borne_spectrale'],0)

    def test_invariance_rigide(self):
        p=np.array([4.,2,1]);a=np.array([3.,2,1]);R=m.rotation([15,40,70]);c=np.array([2.,-1,3])
        for maximum in [False,True]:
            e=m.extremum_surface(p,[0,0,0],a,np.eye(3),maximum)
            f=m.extremum_surface(R@p+c,c,a,R,maximum)
            self.assertAlmostEqual(e['distance'],f['distance'],places=12)
            np.testing.assert_allclose(R@e['point']+c,f['point'],atol=1e-12)

    def test_preuve_globale_sur_points_independants(self):
        rng=np.random.default_rng(72);u=rng.normal(size=(3000,3));u/=np.linalg.norm(u,axis=1)[:,None]
        for _ in range(12):
            a=rng.uniform(.2,3,3);c=rng.uniform(-2,2,3);p=rng.uniform(-4,4,3);R=m.rotation(rng.uniform(-90,90,3))
            distances=np.linalg.norm((u*a)@R.T+c-p,axis=1)
            lo=m.extremum_surface(p,c,a,R);hi=m.extremum_surface(p,c,a,R,True)
            self.assertLessEqual(lo['distance'],min(distances)+1e-12)
            self.assertGreaterEqual(hi['distance'],max(distances)-1e-12)
            for e in [lo,hi]:
                self.assertLess(e['contrainte'],1e-12);self.assertLess(e['stationnarite'],1e-10)


class PaireTests(unittest.TestCase):
    def setUp(self):
        self.e1={'centre':[-2.4,-.6,0],'axes':[1.8,1,.7],'angles':[10,20,25]}
        self.e2={'centre':[2.4,.8,.5],'axes':[1.4,.9,.6],'angles':[-20,35,-35]}

    def test_spheres_reference(self):
        for distance in [4,2.5,1.5]:
            d=m.distance_ellipsoides({'axes':[1,1,1]},{'centre':[distance,0,0],'axes':[1.5,1.5,1.5]})
            exact=max(0,distance-2.5)
            self.assertLessEqual(d['inferieure'],exact+1e-12)
            self.assertGreaterEqual(d['superieure'],exact-1e-12)
            self.assertAlmostEqual(d['superieure'],exact,places=7)

    def test_orientes_bornes_et_faisabilite(self):
        d=m.distance_ellipsoides(self.e1,self.e2)
        self.assertTrue(d['converge']);self.assertTrue(d['separes'])
        self.assertLess(d['ecart'],1e-7)
        self.assertTrue(all(v<=1+1e-12 for v in d['faisabilite']))
        self.assertAlmostEqual(np.linalg.norm(np.array(d['p2'])-d['p1']),d['superieure'])
        h=d['historique'];self.assertTrue(all(a[2]>=b[2]-1e-12 for a,b in zip(h,h[1:])))
        centres=np.array(self.e2['centre'])-self.e1['centre'];n=d['normal']
        self.assertGreater(np.linalg.norm(np.cross(centres,n)),.1)

    def test_symetrie(self):
        a=m.distance_ellipsoides(self.e1,self.e2);b=m.distance_ellipsoides(self.e2,self.e1)
        self.assertAlmostEqual(a['superieure'],b['superieure'],places=7)

    def test_invariance_translation(self):
        d=m.distance_ellipsoides(self.e1,self.e2)
        translation=[1,2,3]
        a={**self.e1,'centre':(np.array(self.e1['centre'])+translation).tolist()}
        b={**self.e2,'centre':(np.array(self.e2['centre'])+translation).tolist()}
        f=m.distance_ellipsoides(a,b)
        self.assertAlmostEqual(d['superieure'],f['superieure'],places=12)

    def test_recouvrement_et_emboitement_solides(self):
        for c in [[0,0,0],[1,0,0]]:
            d=m.distance_ellipsoides({'axes':[3,3,3]},{'centre':c,'axes':[.5,.5,.5]})
            self.assertEqual(d['superieure'],0);self.assertFalse(d['separes'])

    def test_arret_premature_garde_bornes(self):
        d=m.distance_ellipsoides(self.e1,self.e2,iterations=1,tolerance=1e-14)
        reference=m.distance_ellipsoides(self.e1,self.e2,tolerance=1e-12)
        self.assertFalse(d['converge'])
        self.assertLessEqual(d['inferieure'],reference['superieure'])
        self.assertGreaterEqual(d['superieure'],reference['superieure'])

    def test_svm_contraintes_sans_echantillonnage(self):
        d=m.distance_ellipsoides(self.e1,self.e2)
        w=np.array(d['w_svm']);b=d['b_svm']
        c1,a1,r1,B1=m.ellipsoide(self.e1);c2,a2,r2,B2=m.ellipsoide(self.e2)
        self.assertLessEqual(w@c1+np.linalg.norm(B1.T@w)+b,-1+1e-12)
        self.assertGreaterEqual(w@c2-np.linalg.norm(B2.T@w)+b,1-1e-12)
        self.assertAlmostEqual(1/np.linalg.norm(w),d['marge'])


class ServeurTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.port=cls.server.server_port

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join()

    def request(self,path='/',payload=None,headers=None,method=None):
        conn=http.client.HTTPConnection('127.0.0.1',self.port,timeout=15)
        h={'Content-Type':'application/json','X-Optimisation-Token':self.server.api_token}
        h.update(headers or {})
        conn.request(method or ('POST' if payload is not None else 'GET'),path,body=payload,headers=h)
        r=conn.getresponse();status=r.status;body=r.read();conn.close();return status,body

    def test_ressources_et_cours(self):
        for path in ['/','/app.js','/style.css','/favicon.svg','/api/bootstrap']:
            self.assertEqual(self.request(path)[0],200)
        self.assertEqual(self.request('/mathematiques.py')[0],404)
        d=json.loads(self.request('/api/bootstrap')[1]);self.assertEqual(len(d['exercises']),14)

    def test_cinq_experiences_json_fini(self):
        for data in [{'action':'approximation'},{'action':'matrices'},{'action':'produit'},
                     {'action':'point'},{'action':'paire','e1':{'axes':[1,1,1]},'e2':{'centre':[4,0,0],'axes':[1,1,1]}}]:
            status,body=self.request('/api',json.dumps(data))
            self.assertEqual(status,200,body);json.loads(body)

    def test_session_origine_et_hote(self):
        for headers in [{'X-Optimisation-Token':'faux'},{'Origin':'https://example.org'},{'Host':'evil.example'}]:
            self.assertEqual(self.request('/api','{"action":"point"}',headers)[0],403)

    def test_entrees_invalides(self):
        for payload in ['[]','{"action":"point","point":[NaN,0,0]}',
                        '{"action":"point","axes":[1,0,2]}', '{"action":"matrices","n":3.5}',
                        '{"action":"approximation","L":1e400}', '{"action":"point","point":[true,0,0]}',
                        '{"action":"paire","e1":[],"e2":{}}']:
            self.assertEqual(self.request('/api',payload)[0],400,payload)


if __name__=='__main__':
    unittest.main()
