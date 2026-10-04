"""Vérifications indépendantes : dénombrement, moments, spectres et HTTP local."""
from fractions import Fraction
import itertools
import json
import math
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import numpy as np
from mathematiques import (execute, binomial, hypergeometric, polarization_moments,
                          order_cdf, arcsine_cdf, semicircle_cdf, path_matrix,
                          wigner_matrix, wilson)
from probabilites_cpge import make_server
from cours import EXERCISES


class DiscreteTests(unittest.TestCase):
    def test_binomial_enumeration(self):
        counts = np.zeros(7)
        for bits in itertools.product([0, 1], repeat=6):
            counts[sum(bits)] += 1/64
        np.testing.assert_allclose(binomial(6, .5), counts, atol=1e-15)

    def test_binomial_degenerate_and_large(self):
        self.assertEqual(binomial(9, 0)[0], 1)
        self.assertEqual(binomial(9, 1)[9], 1)
        for p in [.0001, .3, .9999]:
            v = binomial(1000, p)
            self.assertAlmostEqual(v.sum(), 1)
            self.assertAlmostEqual(np.dot(np.arange(1001), v), 1000*p, places=8)

    def test_hypergeometric_enumeration(self):
        counts = np.zeros(4)
        for sample in itertools.combinations(range(7), 3):
            counts[sum(i<3 for i in sample)] += 1/math.comb(7, 3)
        np.testing.assert_allclose(hypergeometric(3, 4, 3), counts)

    def test_urn_moments_and_covariance(self):
        r = execute(dict(lab='urne', red=7, blue=12, draws=9))
        pmf = np.array(r['theory']['pmf'])
        k = np.arange(10)
        self.assertAlmostEqual(float(k@pmf), r['theory']['mean'])
        self.assertAlmostEqual(float((k*k)@pmf-(k@pmf)**2), r['theory']['variance'])
        cov = 7*6/(19*18)-(7/19)**2
        self.assertAlmostEqual(cov, r['theory']['covariance'])

    def test_entire_urn_deterministic(self):
        r = execute(dict(lab='urne', red=4, blue=5, draws=9))
        self.assertEqual(r['theory']['variance'], 0)
        self.assertEqual(r['theory']['pmf'][4], 1)

    def test_convolution_same_parameter(self):
        np.testing.assert_allclose(np.convolve(binomial(7, .3), binomial(4, .3)),
                                   binomial(11, .3), atol=2e-15)

    def test_random_walk_return_and_parity(self):
        p = binomial(20, .5)
        self.assertAlmostEqual(p[10], math.comb(20, 10)/2**20)
        self.assertAlmostEqual(p[12], .12013435363769531)
        self.assertTrue(all((2*k-21)%2 for k in range(22)))

    def test_exact_tail_and_chebyshev(self):
        r = execute(dict(lab='fluctuations', n=20, p=.5, epsilon=.1))['theory']
        exact = sum(math.comb(20, k) for k in range(21) if abs(k-10)>=2)/2**20
        self.assertAlmostEqual(r['tail'], exact)
        self.assertLessEqual(r['tail'], r['chebyshev']+1e-14)

    def test_bernoulli_edges_no_normal_division(self):
        for p in [0, 1]:
            r = execute(dict(lab='fluctuations', n=1, p=p))
            self.assertEqual(r['theory']['tail'], 0)
            self.assertEqual(r['theory']['chebyshev'], 0)
            json.dumps(r, allow_nan=False)

    def test_wilson_edges_and_symmetry(self):
        left, right = wilson(0, 100), wilson(100, 100)
        self.assertAlmostEqual(left[0], 0)
        self.assertAlmostEqual(right[1], 1)
        self.assertAlmostEqual(left[1], 1-right[0])
        self.assertLess(left[1], .04)


class PolarizationTests(unittest.TestCase):
    def test_small_tree_exact_rational_moments(self):
        states = [(Fraction(2, 5), Fraction(1))]
        lam = Fraction(1, 3)
        for _ in range(5):
            states = [(y, p*q) for x, p in states for y, q in
                      [((1-lam)*x, 1-x), ((1-lam)*x+lam, x)]]
        reference = [float(sum(p*x**k for x,p in states)) for k in range(5)]
        np.testing.assert_allclose(polarization_moments(.4, 1/3, 5)[-1], reference, atol=1e-15)

    def test_second_moment_closed_form(self):
        for c, lam, n in [(.12,.02,500),(.8,.7,100),(.35,.25,0)]:
            m = polarization_moments(c, lam, n)
            defect = c*(1-c)*(1-lam*lam)**n
            self.assertAlmostEqual(m[-1,1], c)
            self.assertAlmostEqual(m[-1,2], c-defect, places=12)

    def test_higher_moment_bound(self):
        c, lam, n = .35, .25, 70
        m = polarization_moments(c, lam, n)
        D = c*(1-c)*(1-lam*lam)**n
        for k in [2,3,4]:
            self.assertGreaterEqual(c-m[-1,k], -1e-14)
            self.assertLessEqual(c-m[-1,k], (k-1)*D+1e-14)

    def test_zero_steps(self):
        r = execute(dict(lab='polarisation', steps=0))
        self.assertTrue(all(x==.35 for x in r['terminal']))
        self.assertAlmostEqual(r['theory']['variance'], 0)

    def test_paths_bounded_and_seed_reproducible(self):
        d = dict(lab='polarisation',steps=70,reps=500,seed=34)
        a, b = execute(d), execute(d)
        self.assertEqual(a,b)
        paths=np.array(a['paths'])
        self.assertGreaterEqual(paths.min(),0)
        self.assertLessEqual(paths.max(),1)


class ContinuousTests(unittest.TestCase):
    def test_order_cdf_explicit_extremes(self):
        u=np.linspace(0,1,21)
        np.testing.assert_allclose(order_cdf(7,7,u),u**7,atol=2e-15)
        np.testing.assert_allclose(order_cdf(7,1,u),1-(1-u)**7,atol=2e-15)

    def test_maximum_variance_formula(self):
        r=execute(dict(lab='extremes',n=37,theta=3,mode='max'))['theory']
        self.assertAlmostEqual(r['mean'],3*37/38)
        self.assertAlmostEqual(r['variance'],9*(37/39-(37/38)**2))

    def test_uniform_single_order(self):
        for mode in ['max','min','ordre']:
            r=execute(dict(lab='extremes',n=1,k=1,theta=2,mode=mode))['theory']
            self.assertAlmostEqual(r['mean'],1)
            self.assertAlmostEqual(r['variance'],1/3)

    def test_scaled_gap_moments_and_limit(self):
        r=execute(dict(lab='extremes',n=100,mode='ecart'))['theory']
        self.assertAlmostEqual(r['mean'],100/101)
        self.assertAlmostEqual(r['variance'],100**3/(101**2*102))
        self.assertAlmostEqual((1-2/1000)**1000,math.exp(-2),delta=.001)

    def test_beta_sampling_matches_moments(self):
        r=execute(dict(lab='extremes',n=10,k=4,mode='ordre',reps=10000,seed=72))
        self.assertAlmostEqual(r['metrics'][2]['value'],4/11,delta=.01)

    def test_cdfs_normalized_and_monotone(self):
        x=np.linspace(-3,3,301)
        for func in [arcsine_cdf,semicircle_cdf]:
            F=func(x)
            self.assertEqual(F[0],0)
            self.assertEqual(F[-1],1)
            self.assertTrue(np.all(np.diff(F)>=-1e-15))
            np.testing.assert_allclose(F+func(-x),1,atol=2e-15)


class SpectralTests(unittest.TestCase):
    def test_path_eigenvalues_against_diagonalization(self):
        for n in [2,3,11,50]:
            expected=np.sort(2*np.cos(np.arange(1,n+1)*np.pi/(n+1)))
            np.testing.assert_allclose(np.linalg.eigvalsh(path_matrix(n)),expected,atol=3e-15)

    def test_all_sine_eigenvectors(self):
        n=15
        j=np.arange(1,n+1)
        vectors=np.sqrt(2/(n+1))*np.sin(np.outer(j,j)*np.pi/(n+1))
        np.testing.assert_allclose(vectors.T@vectors,np.eye(n),atol=3e-15)
        np.testing.assert_allclose(path_matrix(n)@vectors,
                                   vectors*(2*np.cos(j*np.pi/(n+1))),atol=3e-15)

    def test_arcsine_trace_and_integrated_bins(self):
        r=execute(dict(lab='arcsinus',n=60,power=2))
        self.assertAlmostEqual(r['metrics'][1]['value'],2*59/60)
        self.assertAlmostEqual(sum(r['theory']['bin_masses']),1)
        self.assertLess(r['theory']['residual'],1e-13)

    def test_wigner_symmetry_and_sign_second_moment(self):
        a=wigner_matrix(30,'signes',np.random.default_rng(2))
        np.testing.assert_array_equal(a,a.T)
        self.assertAlmostEqual(np.trace(a@a)/30,1)

    def test_wigner_moments_against_matrix_powers(self):
        a=wigner_matrix(20,'gauss',np.random.default_rng(74))
        s=np.linalg.eigvalsh(a)
        for k in range(1,7):
            self.assertAlmostEqual(np.mean(s**k),np.trace(np.linalg.matrix_power(a,k))/20,places=11)

    def test_wigner_model_reference_moments(self):
        r=execute(dict(lab='wigner',n=30,matrices=1,law='signes'))
        self.assertAlmostEqual(r['metrics'][0]['value'],1)
        self.assertEqual([row[2] for row in r['table']['rows']],[0,1,0,2,0,5,0,14])
        self.assertTrue(all(row[3] is None for row in r['table']['rows']))

    def test_reference_density_moments_by_quadrature(self):
        t=np.linspace(0,np.pi,20001)
        x=2*np.cos(t)
        integrate=getattr(np,'trapezoid',np.trapz if hasattr(np,'trapz') else None)
        for k,arc,sc in [(2,2,1),(4,6,2),(6,20,5)]:
            self.assertAlmostEqual(integrate(x**k,t)/np.pi,arc,places=10)
            self.assertAlmostEqual(integrate(x**k*2*np.sin(t)**2,t)/np.pi,sc,places=10)


class ContractTests(unittest.TestCase):
    def test_all_labs_finite_json(self):
        for lab in ['urne','fluctuations','polarisation','extremes','arcsinus','wigner']:
            r=execute(dict(lab=lab,reps=100,n=12))
            json.dumps(r,allow_nan=False)
            self.assertGreaterEqual(len(r['charts']),2)

    def test_all_exercises_valid(self):
        for exercise in EXERCISES:
            execute(dict(lab=exercise['lab'],reps=100,**exercise['params']))

    def test_invalid_parameters(self):
        for d in [dict(seed=-1),dict(reps=10001),dict(c=float('nan')),dict(c=True),
                  dict(steps=1.2),dict(lab='inconnu'),dict(lab='urne',draws=21),
                  dict(lab='extremes',n=3,k=4),dict(lab='arcsinus',n=4,mode=5),
                  dict(lab='wigner',n=181),dict(lab='wigner',law='cauchy')]:
            with self.assertRaises(ValueError):
                execute(d)


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0)
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.url=f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self,path='/',payload=None,headers=None):
        h={'Content-Type':'application/json','X-Probabilites-Token':self.server.api_token}
        h.update(headers or {})
        return urlopen(Request(self.url+path,data=payload,headers=h),timeout=10)

    def test_bootstrap(self):
        with self.request('/api/bootstrap') as r:
            data=json.load(r)
        self.assertEqual(data['application'],'probabilites-cpge')
        self.assertEqual(len(data['lessons']),12)
        self.assertEqual(len(data['exercises']),16)

    def test_static_assets(self):
        for path in ['/','/app.js','/style.css','/favicon.svg']:
            with self.request(path) as r:
                self.assertGreater(len(r.read()),100)
                self.assertIn("script-src 'self'",r.headers['Content-Security-Policy'])

    def test_valid_api(self):
        with self.request('/api',b'{"lab":"extremes","n":1,"k":1}') as r:
            self.assertEqual(json.load(r)['theory']['mean'],.5)

    def test_missing_token(self):
        with self.assertRaises(HTTPError) as cm:
            self.request('/api',b'{}',{'X-Probabilites-Token':''})
        self.assertEqual(cm.exception.code,403)

    def test_download_is_snapshot_with_attachment(self):
        with self.request('/api',b'{"lab":"extremes","n":1,"k":1}') as r:
            data=json.load(r)
        with self.request('/api/export/'+data['export_id']) as r:
            self.assertIn('attachment;',r.headers['Content-Disposition'])
            self.assertEqual(json.load(r),data)
        with self.assertRaises(HTTPError) as cm:
            self.request('/api/export/inconnu')
        self.assertEqual(cm.exception.code,404)

    def test_foreign_origin_and_host(self):
        for headers in [{'Origin':'https://example.org'},{'Host':'example.org'}]:
            with self.assertRaises(HTTPError) as cm:
                self.request('/api',b'{}',headers)
            self.assertEqual(cm.exception.code,403)

    def test_bad_json_and_nan(self):
        for payload in [b'{',b'[]',b'{"c":NaN}',b'{"steps":10000000}']:
            with self.assertRaises(HTTPError) as cm:
                self.request('/api',payload)
            self.assertEqual(cm.exception.code,400)

    def test_private_files_not_served(self):
        for path in ['/cours.py','/COURS.md','/../README.md']:
            with self.assertRaises(HTTPError) as cm:
                self.request(path)
            self.assertEqual(cm.exception.code,404)


if __name__=='__main__':
    unittest.main()
