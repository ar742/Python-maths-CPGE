"""Contrôles indépendants des identités exactes et des cas limites complexes."""
import json
import math
from pathlib import Path
import sys
import unittest
import numpy as np
import sympy as sp

sys.path.insert(0,str(Path(__file__).resolve().parent))
from commun import clean
from catalogue_complexes import LABS
from contenu_complexes import LESSONS, EXERCISES, GUIDES
from modeles_complexes import COMPUTE, cauchy_radius, newton_sums, recurrence_coefficients, recurrence_value, characteristic_value

def defaults(id_):
    item=next(item for item in LABS if item['id']==id_)
    return {c['key']:c['value'] for c in item['controls']}

def calculate(id_,**values):
    p=defaults(id_); p.update(values); return clean(COMPUTE[id_](p))

class ComplexesTests(unittest.TestCase):
    def test_complete_family_and_strict_json(self):
        self.assertEqual(len(LABS),10)
        self.assertEqual(len(LESSONS),20)
        self.assertEqual(len(EXERCISES),30)
        self.assertEqual(set(GUIDES),set(COMPUTE))
        for item in LABS:
            with self.subTest(lab=item['id']):
                base=defaults(item['id'])
                for p in [base]+[dict(base,**s['values']) for s in item['presets']]:
                    output=clean(COMPUTE[item['id']](p)); json.dumps(output,allow_nan=False)
                    self.assertTrue(output['scene']['description'])

    def test_cayley_exact_roots_and_leading_coefficient(self):
        for n in [2,3,7,12]:
            out=calculate('cayley_tangentes',n=n)
            self.assertEqual(out['metrics'][0]['value'],2*n-1)
            self.assertEqual(out['metrics'][1]['value'],4*n)
            polynomial=sp.Poly((sp.Symbol('X')+1)**(2*n)-(sp.Symbol('X')-1)**(2*n))
            # Scaled residual avoids mistaking a large polynomial value at large |α| for a relative error.
            for pt in out['scene']['points']:
                if pt['group']!=0: continue
                z=complex(pt['x'],pt['y']); residual=abs((z+1)**(2*n)-(z-1)**(2*n))
                scale=max(1,abs(z+1)**(2*n)+abs(z-1)**(2*n))
                self.assertLess(residual/scale,4e-14)
            self.assertEqual(int(polynomial.LC()),4*n)
            nonzero=[pt['y'] for pt in out['scene']['points'] if pt['group']==0 and abs(pt['y'])>1e-10]
            self.assertAlmostEqual(np.prod(nonzero),(-1)**(n-1),places=9)

    def test_geometric_source_prefactor_and_product(self):
        out=calculate('geometrique_affine',n=3,cx=-1,cy=0,r=2)
        self.assertEqual(out['metrics'][1]['value'],1/8)
        self.assertEqual(out['metrics'][2]['value'],4)
        roots=[complex(pt['x'],pt['y']) for pt in out['scene']['points'] if pt['group']==0]
        self.assertAlmostEqual(np.prod(roots).real,-15,places=10)
        for z in roots:
            self.assertLess(abs(sum(((z+1)/2)**j for j in range(4))),1e-12)

    def test_geometric_nonreal_coefficients(self):
        out=calculate('geometrique_affine',n=2,cx=0,cy=1,r=1)
        for pt in out['scene']['points']:
            if pt['group']!=0: continue
            z=complex(pt['x'],pt['y'])
            self.assertLess(abs(z*z+(1-2j)*z-1j),1e-12)

    def test_cauchy_enclosure_and_known_unit_circle(self):
        self.assertAlmostEqual(cauchy_radius([1,0,0,0,-1j]),1,places=13)
        rng=np.random.default_rng(129)
        for _ in range(15):
            c=np.r_[1,rng.uniform(-3,3,6)+1j*rng.uniform(-3,3,6)]
            roots=np.roots(c); rho=cauchy_radius(c); maximum=max(abs(roots))
            self.assertLessEqual(maximum,rho*(1+1e-12))
            self.assertGreaterEqual(maximum,(2**(1/6)-1)*rho*(1-1e-12))
            q=rho**6-sum(abs(c[-1-j])*rho**j for j in range(6))
            self.assertLess(abs(q)/rho**6,1e-12)

    def test_rouche_certificates_and_no_forced_conclusion(self):
        self.assertEqual(calculate('rouche_disque',r=1)['metrics'][0]['value'],'2 racines')
        self.assertEqual(calculate('rouche_disque',r=2)['metrics'][0]['value'],'5 racines')
        self.assertEqual(calculate('rouche_disque',r=1.6)['metrics'][0]['value'],'Le critère ne conclut pas')
        out=calculate('rouche_disque',ar=0,ai=0,br=1,bi=0,r=1)
        self.assertEqual(out['metrics'][0]['value'],'Le critère ne conclut pas')
        self.assertEqual(out['metrics'][3]['value'],5)  # Z⁵+1 has all five zeros on the circle.

    def test_gauss_lucas_containment_and_centroids(self):
        for x,y in [(.3,-1.8),(3,-3),(-2,-1),(0,0)]:
            out=calculate('gauss_lucas',x=x,y=y)
            pts=out['scene']['points']; roots=np.array([complex(a['x'],a['y']) for a in pts if a['group']==0]); derivative=np.array([complex(a['x'],a['y']) for a in pts if a['group']==1]); hull=out['scene']['polygons'][0]
            verts=np.array([complex(x,y) for x,y in zip(hull['x'],hull['y'])])
            for z in derivative:
                for a,b in zip(verts,np.roll(verts,-1)):
                    self.assertGreaterEqual(((b-a).conjugate()*(z-a)).imag,-1e-8)
            self.assertLess(abs(np.mean(roots)-np.mean(derivative)),1e-12)

    def test_reciprocal_conjugate_fixed_circle_and_zero(self):
        out=calculate('reciproque_conjugue',rho=1,theta=70)
        p=out['scene']['points']; original=next(a for a in p if a['label']=='α1'); image=next(a for a in p if a['label']=='α*1')
        self.assertAlmostEqual(original['x'],image['x'],places=13); self.assertAlmostEqual(original['y'],image['y'],places=13)
        out=calculate('reciproque_conjugue',rho=0,theta=0)
        self.assertEqual(out['metrics'][1]['value'],4)
        self.assertEqual(out['metrics'][2]['value'],4)
        self.assertFalse(any('α*1'==a['label'] for a in out['scene']['points']))

    def test_newton_identities_against_exact_hand_values(self):
        c=[1,0,1+1j,0,1+1j,-1+.5j,.5-.8j]; sums=newton_sums(c,7)
        expected=[0,-2-2j,0,-4,5-2.5j,1+12.8j,7*(1+1j)*(-1+.5j)]
        np.testing.assert_allclose(sums,expected,rtol=1e-13,atol=1e-13)
        # Independent root-of-unity example: sums vanish except at multiples of 5.
        np.testing.assert_allclose(newton_sums([1,0,0,0,0,-1j],10),[0,0,0,0,5j,0,0,0,0,-5],atol=1e-14)

    def test_newton_nonclassified_is_explicit(self):
        out=calculate('newton_bassins',family='carre',x0=.3,y0=.4,grid=60,iterations=12)
        self.assertEqual(out['metrics'][2]['value'],'Dérivée nulle ou excursion')
        self.assertTrue(out['scene']['categorical']); self.assertEqual(out['scene']['labels'][-1],'Non classé')
        classes=np.array(out['scene']['z']); self.assertTrue(np.all((classes>=0)&(classes<=4)))
        self.assertGreater(np.sum(classes==4),0)
        self.assertEqual(sum(row[1] for row in out['table']['rows']),60**2)

    def test_coalescence_square_root_law(self):
        out=calculate('conditionnement_racines',delta=0,exponent=-8,theta=90)
        self.assertAlmostEqual(out['metrics'][0]['value'],1e-4,places=12)
        self.assertEqual(out['metrics'][1]['value'],'Non définie : racine double')
        original=[a for a in out['scene']['points'] if a['group']==0]; changed=[a for a in out['scene']['points'] if a['group']==1]
        center=complex(original[0]['x'],original[0]['y'])
        for pt in changed:
            d=complex(pt['x'],pt['y'])-center; self.assertLess(abs(d*d-1e-8j),1e-16)

    def test_recurrence_source_initialisation_and_double_root(self):
        np.testing.assert_array_equal(recurrence_coefficients(2),[-2,0,-1])
        np.testing.assert_array_equal(recurrence_coefficients(3),[2,0,-1,0])
        for n in [0,1,2,8,18]:
            self.assertEqual(recurrence_value(n,2),(1-5*n)*(-1)**n)
            self.assertEqual(recurrence_value(n,-2),1-5*n)
            self.assertEqual(characteristic_value(n,2)[0],recurrence_value(n,2))
        self.assertEqual(recurrence_value(8,2),-39)

    def test_recurrence_complex_rotation_and_closed_formula(self):
        lam=np.exp(1j*np.pi/4)
        for n in [2,5,12]:
            c=recurrence_coefficients(n,lam); source=recurrence_coefficients(n)
            for z in [.3+.8j,-1.4+.2j,2.5-1j]:
                expected=np.polyval(source,lam*z)
                self.assertLess(abs(np.polyval(c,z)-expected)/max(1,abs(expected)),1e-12)
                self.assertLess(abs(characteristic_value(n,lam*z)[0]-expected)/max(1,abs(expected)),1e-11)

if __name__=='__main__': unittest.main()
