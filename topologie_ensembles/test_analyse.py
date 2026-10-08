"""Vérifications des preuves quantitatives, non des seuls graphes."""
import json
import math
import unittest
from fractions import Fraction
import numpy as np
from commun import clean, integrate
from catalogue_analyse import LABS
import modeles_analyse as m


def defaults(lab):
    return {control['key']:control['value'] for control in lab['controls']}


def metrics(result):
    return {item['label']:item['value'] for item in result['metrics']}


class ExtractionTests(unittest.TestCase):
    def test_explicit_subsequences_strict_indices(self):
        data=m.bolzano_weierstrass(dict(N=300,epsilon=.01))
        pair,odd=data['scene']['subsequences']
        for subseq in [pair,odd]:
            self.assertTrue(np.all(np.diff(subseq['indices'])>0))
            self.assertLess(abs(subseq['values'][-1]-subseq['limit']),.004)

    def test_bounded_sequence_and_separated_limits(self):
        ns=np.arange(1001); values=(-1.)**ns+1/(ns+1)
        self.assertTrue(np.all(values>-1)); self.assertEqual(values.max(),2)
        self.assertGreater(values[-1]-values[-2],1.99)

    def test_exact_strict_epsilon_rank(self):
        for eps in [.002,.01,.05,.1,.2]:
            values=metrics(m.bolzano_weierstrass(dict(N=20,epsilon=eps)))
            ke=values['Rang k suffisant, sous-suite paire']; ko=values['Rang k suffisant, sous-suite impaire']
            self.assertLess(1/(2*ke+1),eps)
            self.assertLess(1/(2*ko+2),eps)

    def test_records_do_not_repeat_indices_or_equal_distances(self):
        xs=np.array([2.,0.,1.8,1.8,1.2,.8,1.1,1.1,1.01])
        indices=m.record_indices(xs)
        self.assertTrue(np.all(np.diff(indices)>0))
        self.assertTrue(np.all(np.diff(abs(xs[indices]-1))<0))
        self.assertNotIn(3,indices); self.assertNotIn(7,indices)

    def test_records_equal_brute_force_minima(self):
        xs=np.random.default_rng(44).uniform(0,3,500)
        expected=[]; best=math.inf
        for j,value in enumerate(xs):
            distance=abs(value-1)
            if distance<best:expected.append(j); best=distance
        np.testing.assert_array_equal(m.record_indices(xs),expected)

    def test_survival_exact_piecewise_single_draw(self):
        d=np.array([-1,0,.5,1,1.5,2,3])
        np.testing.assert_allclose(m.nearest_survival(d,1),[1,1,2/3,1/3,1/6,0,0])

    def test_survival_product_independence(self):
        for n in [1,3,100]:
            for d in [.005,.3,1,1.4]:
                # Mesure de la partie de [0,3] restant hors du voisinage.
                inside=max(0,min(3,1+d)-max(0,1-d))
                self.assertAlmostEqual(float(m.nearest_survival(d,n)),(1-inside/3)**n,places=13)

    def test_expectation_integrates_survival(self):
        d=np.linspace(0,2,40001)
        for n in [1,4,100]:
            numerical=float(integrate(m.nearest_survival(d,n),d))
            self.assertAlmostEqual(numerical,m.nearest_expectation(n),delta=2e-8)

    def test_theory_agrees_with_independent_trials(self):
        minima=m.nearest_trials(200,6000,772)
        d=.01; probability=float(m.nearest_survival(d,200))
        self.assertAlmostEqual(np.mean(minima>d),probability,delta=.025)
        self.assertAlmostEqual(minima.mean(),m.nearest_expectation(200),delta=.0005)

    def test_seed_reproduces_complete_extraction(self):
        params=dict(N=300,seed=17,trials=50,d=.01)
        a=clean(m.extraction_aleatoire(params)); b=clean(m.extraction_aleatoire(params))
        self.assertEqual(a,b)

    def test_rare_positive_probability_is_not_displayed_as_impossible(self):
        data=m.extraction_aleatoire(dict(N=20000,seed=7,trials=50,d=1))
        self.assertIsInstance(metrics(data)['Probabilité exacte D_N>d'],str)
        self.assertAlmostEqual(data['scene']['log10_survival'],20000*math.log10(1/3),places=9)


class CauchyAndCompactTests(unittest.TestCase):
    def test_heron_exact_recurrence_and_positive_residual(self):
        values=m.heron_fractions(8)
        for u,v in zip(values,values[1:]):
            self.assertIsInstance(u,Fraction); self.assertEqual(v,u/2+1/u)
            self.assertLess(v,u); self.assertGreater(v*v,2)

    def test_heron_tail_bound_exactly_dominates_differences(self):
        values=m.heron_fractions(8); bounds=m.heron_bounds(values)
        for i,u in enumerate(values):
            for v in values[i:]:self.assertLessEqual(u-v,bounds[i])

    def test_heron_residual_recurrence_without_float_cancellation(self):
        values=m.heron_fractions(8)
        for u,v in zip(values,values[1:]):
            self.assertEqual(v*v-2,(u*u-2)**2/(4*u*u))
        self.assertGreater(m.heron_bounds(values)[-1],0)
        self.assertLess(float(m.heron_bounds(values)[-1]),1e-150)

    def test_compact_cover_has_strict_threshold(self):
        for size in [2,5,10,30]:
            threshold=1/(2*size)
            self.assertFalse(m.compact_cover(size,threshold)[0])
            self.assertFalse(m.compact_cover(size,threshold*.99)[0])
            self.assertTrue(m.compact_cover(size,threshold*1.01)[0])

    def test_boundary_midpoints_excluded_in_figure(self):
        data=m.compacts_recouvrements(dict(m=10,r=.05,N=20))
        self.assertEqual(metrics(data)['[0,1] couvert par les ouverts'],'Non')
        self.assertTrue(np.all(data['charts'][0]['series'][1]['y']==0))

    def test_noncompact_cover_has_explicit_missing_point(self):
        for N in [2,10,100,100000]:
            upper=1-1/N; outside=1-1/(2*N)
            self.assertGreaterEqual(outside,0); self.assertLess(outside,1)
            self.assertGreater(outside,upper)

    def test_lebesgue_margin_fits_nearest_ball(self):
        size=7; radius=.12; covered,margin,_=m.compact_cover(size,radius)
        self.assertTrue(covered)
        rng=np.random.default_rng(5)
        for _ in range(100):
            x=rng.uniform(0,1); center=round(size*x)/size
            self.assertLess(abs(x-center)+margin,radius+1e-14)


class ContinuityAndGeometryTests(unittest.TestCase):
    def test_ellipse_support_satisfies_constraint_and_objective(self):
        for a,b,angle in [(3,.7,.2),(1,4,1.4),(2,2,3)]:
            h,v=m.ellipse_support(a,b,angle)
            self.assertAlmostEqual((v[0]/a)**2+(v[1]/b)**2,1,places=13)
            self.assertAlmostEqual(v@np.array([math.cos(angle),math.sin(angle)]),h,places=13)

    def test_ellipse_support_dominates_independent_dense_search(self):
        angles=np.linspace(0,2*math.pi,30001)
        pts=np.column_stack((3*np.cos(angles),.8*np.sin(angles)))
        for direction in [.31,1.35,2.76]:
            v=np.array([math.cos(direction),math.sin(direction)])
            h,_=m.ellipse_support(3,.8,direction)
            self.assertAlmostEqual((pts@v).max(),h,delta=5e-8)

    def test_open_ellipse_sequence_is_strictly_inside(self):
        h,vertex=m.ellipse_support(3,.8,.7)
        for N in [2,20,200]:
            inside=(1-1/N)*vertex
            self.assertLess((inside[0]/3)**2+(inside[1]/.8)**2,1)
            self.assertLess((1-1/N)*h,h)

    def test_open_ellipse_boundary_and_extrema_are_excluded_visually(self):
        data=m.valeurs_extremes(dict(a=3,b=1,theta=40,domain='open',N=20))
        self.assertFalse(data['scene']['paths'][0]['boundaryClosed'])
        self.assertEqual(len(data['scene']['points']),1)
        self.assertEqual(len(data['scene']['discs']),2)
        self.assertTrue(all(d['closed'] is False and d['fill'] is False for d in data['scene']['discs']))

    def test_chirp_witnesses_have_exact_phase_gap(self):
        data=m.heine_continuite(dict(family='chirp',R=4,n=50000)); vals=metrics(data)
        xn=data['scene']['witness_x']; yn=data['scene']['witness_y']
        self.assertAlmostEqual(yn*yn-xn*xn,math.pi/2,delta=1e-9)
        self.assertEqual(vals['Écart exact des images'],1)
        self.assertLess(data['scene']['witness_gap'],.002)

    def test_compact_chirp_lipschitz_bound(self):
        rng=np.random.default_rng(4); x=rng.uniform(-4,4,500); y=rng.uniform(-4,4,500)
        self.assertTrue(np.all(abs(np.sin(x*x)-np.sin(y*y))<=8*abs(x-y)+1e-13))

    def test_sqrt_holder_estimate(self):
        rng=np.random.default_rng(2); x=rng.uniform(0,1,1000); y=rng.uniform(0,1,1000)
        self.assertTrue(np.all(abs(np.sqrt(x)-np.sqrt(y))<=np.sqrt(abs(x-y))+1e-15))

    def test_sqrt_lipschitz_quotients_diverge(self):
        for n in [10,100,10000]:
            data=m.heine_continuite(dict(family='sqrt',R=4,n=n))
            self.assertEqual(metrics(data)['Quotient de Lipschitz sur la paire'],n)
            self.assertAlmostEqual(data['scene']['witness_values'][1]/data['scene']['witness_gap'],n)

    def test_minkowski_support_is_sum_of_two_independent_maxima(self):
        a,b,s,theta,phi=2.5,.7,1.5,.8,1.6
        h,vertex=m.minkowski_support(a,b,s,theta,phi)
        t=np.linspace(0,2*math.pi,20001); ellipse=np.column_stack((a*np.cos(t),b*np.sin(t)))
        u=np.array([math.cos(phi),math.sin(phi)]); v=np.array([math.cos(theta),math.sin(theta)])
        numerical=(ellipse@u).max()+max((-s*v)@u,(s*v)@u)
        self.assertAlmostEqual(h,numerical,delta=1e-7)
        self.assertAlmostEqual(vertex@u,h,places=13)

    def test_minkowski_area_for_circle_is_stadium_area(self):
        data=m.image_compacte(dict(a=2,b=2,length=3,theta=35,direction=100))
        self.assertAlmostEqual(metrics(data)['Aire exacte de A+B'],4*math.pi+24,places=12)

    def test_minkowski_boundary_points_respect_all_support_inequalities(self):
        p=dict(a=2.5,b=.7,length=1.5,theta=55,direction=110)
        data=m.image_compacte(p); boundary=data['scene']['paths'][0]['points']
        for angle in np.linspace(0,2*math.pi,30):
            h,_=m.minkowski_support(2.5,.7,1.5,math.radians(55),angle)
            vals=boundary@np.array([math.cos(angle),math.sin(angle)])
            self.assertLessEqual(vals.max(),h+1e-12)


class OperatorAndInfiniteTests(unittest.TestCase):
    def test_dense_matrix_has_prescribed_extreme_eigenvalues(self):
        A=m.dense_matrix(8,80,42)
        vals=np.linalg.eigvalsh(A.T@A)
        self.assertAlmostEqual(math.sqrt(vals[-1]),80,places=10)
        self.assertAlmostEqual(math.sqrt(vals[0]),1,places=10)
        self.assertGreater(np.count_nonzero(abs(A)>1e-10),60)

    def test_operator_norm_one_attained_by_a_basis_vector(self):
        A=m.dense_matrix(6,12,32); norm1=abs(A).sum(axis=0).max()
        achieved=max(np.linalg.norm(A@np.eye(6)[:,j],ord=1) for j in range(6))
        self.assertAlmostEqual(norm1,achieved,places=13)

    def test_operator_norm_infinity_attained_by_sign_vector(self):
        A=m.dense_matrix(7,5,18); row=int(np.argmax(abs(A).sum(axis=1)))
        x=np.sign(A[row]); norminf=abs(A).sum(axis=1).max()
        self.assertAlmostEqual(np.linalg.norm(A@x,ord=np.inf),norminf,places=12)

    def test_svd_optimizer_uses_full_dimension(self):
        data=m.applications_lineaires(dict(dimension=8,condition=50,seed=9))
        x=data['scene']['right_optimizer']; Ax=data['scene']['image_optimizer']
        self.assertEqual(len(x),8); self.assertAlmostEqual(np.linalg.norm(x),1,places=13)
        self.assertAlmostEqual(np.linalg.norm(Ax),50,places=11)

    def test_isometry_at_condition_one(self):
        A=m.dense_matrix(6,1,7)
        np.testing.assert_allclose(A.T@A,np.eye(6),atol=1e-14)

    def test_function_integral_norms_by_independent_gauss_quadrature(self):
        t,w=np.polynomial.legendre.leggauss(90); x=(t+1)/2
        for n in [1,5,40,80]:
            data=m.normes_dimension_infinie(dict(N=n)); vals=metrics(data)
            self.assertAlmostEqual(np.dot(w,x**n)/2,vals['Norme 1 : erreur absolue moyenne'],delta=1e-14)
            self.assertAlmostEqual(math.sqrt(np.dot(w,x**(2*n))/2),vals['Norme 2 : erreur moyenne quadratique'],delta=1e-13)

    def test_norm_ratios_have_no_common_constant(self):
        a=metrics(m.normes_dimension_infinie(dict(N=10)))
        b=metrics(m.normes_dimension_infinie(dict(N=1000)))
        self.assertGreater(b['Rapport ‖f_N‖∞ / ‖f_N‖₁'],90*a['Rapport ‖f_N‖∞ / ‖f_N‖₁'])
        self.assertEqual(b['Norme ∞ : plus grande erreur'],1)

    def test_gram_formula_by_independent_periodic_quadrature(self):
        M=24; x=np.arange(2048)*2*math.pi/2048
        basis=np.exp(1j*np.arange(M)[:,None]*x)/math.sqrt(2*math.pi)
        gram=(2*math.pi/len(x))*(basis.conj()@basis.T)
        np.testing.assert_allclose(gram,np.eye(M),atol=1e-13)

    def test_modes_separated_even_at_large_indices(self):
        x=np.arange(4096)*2*math.pi/4096
        for n,j in [(1,2),(10,40),(0,100)]:
            difference=(np.exp(1j*n*x)-np.exp(1j*j*x))/math.sqrt(2*math.pi)
            norm=math.sqrt(2*math.pi*np.mean(abs(difference)**2))
            self.assertAlmostEqual(norm,math.sqrt(2),places=13)


class ContractTests(unittest.TestCase):
    def test_ten_unique_models_match_catalogue(self):
        self.assertEqual(len(LABS),10)
        self.assertEqual(set(m.MODELS),{lab['id'] for lab in LABS})

    def test_defaults_presets_and_extremes_are_finite_json(self):
        for lab in LABS:
            base=defaults(lab)
            cases=[base]+[{**base,**preset['values']} for preset in lab['presets']]
            for edge in ['min','max']:
                cases.append({control['key']:control.get(edge,control['value']) for control in lab['controls']})
            for p in cases:
                with self.subTest(lab=lab['id'],parameters=p):
                    data=clean(m.calculate(lab['id'],p))
                    json.dumps(data,allow_nan=False)
                    self.assertTrue(data['metrics']); self.assertTrue(data['charts'])
                    self.assertGreaterEqual(len(data['steps']),4)
                    for plot in data['charts']:
                        for curve in plot['series']:
                            self.assertEqual(len(curve['x']),len(curve['y']))
                            self.assertLessEqual(len(curve['x']),650)


if __name__=='__main__':unittest.main()
