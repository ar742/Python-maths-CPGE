"""Références indépendantes pour les exemples infinis et les familles matricielles."""
import math
import unittest
import numpy as np
from fractions import Fraction
from modeles_ensembles import rational_enumeration,cantor_intervals,cassini_paths,Q4,R4,calculate
from catalogue_ensembles import LABS
from commun import clean
import json

def run(name,**overrides):
    lab=next(l for l in LABS if l['id']==name)
    p={c['key']:c['value'] for c in lab['controls']};p.update(overrides)
    return calculate(name,p)

class CardinalitesTests(unittest.TestCase):
    def test_enumeration_unique(self):
        values=rational_enumeration(18)
        self.assertEqual(len(values),len(set(values)))
        self.assertIn(Fraction(0),values)
        self.assertIn(Fraction(-7,11),values)
        self.assertIn(Fraction(7,11),values)
    def test_height_prefix_is_complete(self):
        values=set(rational_enumeration(12))
        expected={Fraction(p,q) for q in range(1,13) for p in range(-12,13) if abs(p)+q<=12}
        self.assertEqual(values,expected)
    def test_prefix_preserves_enumeration(self):
        a,b=rational_enumeration(7),rational_enumeration(8)
        self.assertEqual(a,b[:len(a)])
    def test_best_distance_is_nonincreasing(self):
        for target in [.713,-1.419]:
            chart=run('denombrer_rationnels',target=target)['charts'][1]['series'][0]
            self.assertTrue(np.all(np.diff(chart['y'])<=0))
    def test_diagonal_differs_in_each_row(self):
        for seed in [0,5,99]:
            sc=run('diagonale_cantor',N=14,seed=seed)['scene']
            for i in range(14):self.assertNotEqual(sc['matrix'][i,i],sc['anti'][i])
    def test_diagonal_ternary_cylinder_contains_continuations(self):
        sc=run('diagonale_cantor')['scene'];anti=sc['anti'];N=len(anti)
        left=sum(int(v)*2/Fraction(3**(i+1)) for i,v in enumerate(anti))
        right=left+Fraction(1,3**N)
        for bit in [0,1]:
            extra=sum(bit*2/Fraction(3**j) for j in range(N+1,N+50))
            self.assertLessEqual(left,left+extra);self.assertLessEqual(left+extra,right)
    def test_cantor_lengths_and_nesting(self):
        levels=cantor_intervals(8)
        for k,intervals in enumerate(levels):
            self.assertEqual(len(intervals),2**k)
            self.assertAlmostEqual(sum(b-a for a,b in intervals),(2/3)**k,places=13)
            for a,b in intervals:
                self.assertAlmostEqual(b-a,3**(-k),places=13)
                if k:self.assertTrue(any(c-1e-14<=a<=b<=d+1e-14 for c,d in levels[k-1]))
    def test_cantor_endpoints_are_retained(self):
        for k in [0,1,3,8]:
            intervals=cantor_intervals(k)[-1]
            self.assertEqual(intervals[0][0],0);self.assertEqual(intervals[-1][1],1)
    def test_rational_floor_including_negative(self):
        for target in [-1.414,.731,0]:
            r=run('rationnels_irrationnels',target=target,N=10)
            q=r['charts'][0]['series'][0]['y'];irr=r['charts'][0]['series'][1]['y']
            for n,v,w in zip(range(1,11),q,irr):
                self.assertGreaterEqual(target-v,-2e-16)
                self.assertLess(target-v,10**(-n)+2e-16)
                self.assertAlmostEqual(w-v,math.sqrt(2)*10**(-n),places=15)
    def test_rational_and_irrational_error_bounds(self):
        r=run('rationnels_irrationnels',target=-.731,N=12)
        chart=r['charts'][0];q=chart['series'][0]['y'];irr=chart['series'][1]['y']
        self.assertLessEqual(abs(q[-1]+.731),10**(-12)+2e-16)
        self.assertLessEqual(abs(irr[-1]+.731),math.sqrt(2)*10**(-12)+2e-16)

class ConnexiteTests(unittest.TestCase):
    def test_adherent_sequence_has_correct_ordinate(self):
        for y in [-1,-.7,0,.4,1]:
            r=run('sinus_topologue',height=y);xn=r['charts'][1]['series'][0]['y']
            np.testing.assert_allclose(np.sin(1/xn),np.full(len(xn),y),atol=6e-14)
            self.assertTrue(np.all(np.diff(xn)<0))
    def test_sinus_curve_is_not_artificially_joined_to_segment(self):
        sc=run('sinus_topologue')['scene']
        self.assertEqual(len(sc['paths']),2)
        self.assertTrue(np.all(sc['paths'][0]['points'][:,0]>0))
        self.assertTrue(np.all(sc['paths'][1]['points'][:,0]==0))
    def test_cassini_boundaries_satisfy_equation(self):
        for b in [.35,.8,1,1.01,1.8]:
            for path in cassini_paths(b):
                pts=path['points'];x,y=pts[:,0],pts[:,1]
                val=((x-1)**2+y*y)*((x+1)**2+y*y)
                np.testing.assert_allclose(val,np.full(len(x),b**4),atol=2e-13)
    def test_cassini_component_change_depends_on_strictness(self):
        for b,closed,expected in [(.8,'yes',2),(.8,'no',2),(1,'yes',1),(1,'no',2),(1.2,'no',1)]:
            metrics={m['label']:m['value'] for m in run('chemins_niveaux',b=b,closed=closed)['metrics']}
            self.assertEqual(metrics['Composantes connexes'],expected)
    def test_cassini_origin_membership(self):
        for b,closed in [(1,'no'),(1,'yes'),(1.4,'no')]:
            metrics={m['label']:m['value'] for m in run('chemins_niveaux',b=b,closed=closed)['metrics']}
            self.assertEqual(metrics['L’origine appartient au sous-niveau'],b>1 or b==1 and closed=='yes')
    def test_cassini_large_sublevel_star_segments(self):
        for b in [1.1,1.8]:
            pts=cassini_paths(b)[0]['points']
            for factor in np.linspace(0,1,21):
                x,y=(factor*pts).T;val=((x-1)**2+y*y)*((x+1)**2+y*y)
                self.assertTrue(np.all(val<=b**4+2e-13))
    def test_circle_images_approach_but_inverse_does_not(self):
        r=run('homeomorphisme',n=180)
        self.assertLess(r['charts'][0]['series'][0]['y'][-1],.006)
        self.assertGreater(r['charts'][1]['series'][0]['y'][-1],6)
    def test_compact_embedding_inverse_is_first_coordinate(self):
        r=run('homeomorphisme',family='curve',t=-.35);chart=r['charts'][0]
        t=chart['series'][0]['x']
        np.testing.assert_allclose(chart['series'][0]['y'],t)
        np.testing.assert_allclose(chart['series'][1]['y'],t*t)
        np.testing.assert_allclose(chart['series'][2]['y'],t**3)

class MatricesEtContractionsTests(unittest.TestCase):
    def test_rotations_are_proper_orthogonal(self):
        for A in [Q4,R4]:
            np.testing.assert_allclose(A.T@A,np.eye(4),atol=7e-16)
            self.assertAlmostEqual(np.linalg.det(A),1,places=14)
    def test_real_dense_determinant_and_singular_distance(self):
        for t in [-2,-.3,0,.6,2]:
            sc=run('gl_composantes',t=t)['scene'];A=sc['matrix']
            self.assertAlmostEqual(np.linalg.det(A),6*t,places=13)
            self.assertAlmostEqual(np.linalg.svd(A,compute_uv=False)[-1],min(abs(t),1),places=13)
            self.assertGreater(np.count_nonzero(abs(A)>1e-5),12)
    def test_complex_bridge_avoids_zero(self):
        for angle in [0,45,120,180,360]:
            sc=run('gl_composantes',field='complex',angle=angle)['scene'];A=sc['matrix']+1j*sc['imaginary']
            self.assertAlmostEqual(abs(np.linalg.det(A)),6,places=13)
    def test_orthogonal_all_angles_and_signs(self):
        for angle in [0,25,180,360]:
            for orientation in ['positive','negative']:
                sc=run('orthogonal_compact',angle=angle,orientation=orientation)['scene'];O=sc['matrix']
                np.testing.assert_allclose(O.T@O,np.eye(4),atol=2e-15)
                self.assertAlmostEqual(np.linalg.det(O),1 if orientation=='positive' else -1,places=13)
                self.assertAlmostEqual(np.linalg.norm(O),2,places=13)
    def test_special_linear_family_unbounded_norm_formula(self):
        for T in [0,2,6]:
            A=run('orthogonal_compact',T=T)['scene']['secondary_matrix']
            self.assertAlmostEqual(np.linalg.det(A),1,places=9)
            self.assertAlmostEqual(np.linalg.norm(A),math.sqrt(math.exp(2*T)+math.exp(-2*T)+2),places=12)
    def test_cos_iterates_stay_in_complete_invariant_segment(self):
        seq=run('point_fixe',N=60)['charts'][1]['series'][0]['y']
        self.assertTrue(all(0<=x<=1 for x in seq))
        self.assertLess(abs(seq[-1]-.7390851332151607),1e-10)
    def test_cos_posteriori_bound_contains_true_error(self):
        for N in [2,5,15,45]:
            r=run('point_fixe',N=N);metrics={m['label']:m['value'] for m in r['metrics']}
            self.assertLessEqual(metrics['Écart au point fixe de référence'],metrics['Borne a posteriori']+2e-16)
    def test_affine_iteration_against_closed_formula(self):
        for q in [-1.1,-.7,.5,.95,1.05]:
            r=run('point_fixe',family='affine',q=q,N=30,x0=.2);seq=r['charts'][1]['series'][0]['y'];star=.7/(1-q)
            np.testing.assert_allclose(seq,star+q**np.arange(31)*(.2-star),rtol=2e-13,atol=3e-13)
    def test_noncontractive_has_no_banach_error_bound(self):
        for q in [-1.1,-1,1,1.05]:
            r=run('point_fixe',family='affine',q=q,N=30)
            self.assertNotIn('Borne a posteriori',[m['label'] for m in r['metrics']])
    def test_every_preset_has_finite_json(self):
        for lab in LABS:
            for preset in lab['presets']:
                with self.subTest(lab=lab['id'],preset=preset['label']):
                    p={c['key']:c['value'] for c in lab['controls']};p.update(preset['values'])
                    json.dumps(clean(calculate(lab['id'],p)),allow_nan=False)

if __name__=='__main__':unittest.main()
