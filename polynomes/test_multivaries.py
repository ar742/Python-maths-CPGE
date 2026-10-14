"""Certificats indépendants des laboratoires multivariés."""
import json
import math
import unittest
import numpy as np
import sympy as sp
from catalogue_multivaries import LABS
from contenu_multivaries import GUIDES,LESSONS,EXERCISES
from commun import clean
from modeles_multivaries import (COMPUTE,convex_hull,circle_parabola_roots,distinct_complex,
    elimination_polynomials,groebner_data,symmetric_values,quadratic_data,
    motzkin_value,motzkin_minimum,lagrange_data)

class ExactModels(unittest.TestCase):
    def test_exponent_geometry(self):
        self.assertEqual(set(convex_hull([(0,0),(4,0),(0,4),(2,3),(1,1)])),{(0,0),(4,0),(2,3),(0,4)})
        data=COMPUTE['monomes_newton'](dict(m=4,n=4,q=3,a=1,c=1))
        vals={m['label']:m['value'] for m in data['metrics']}
        self.assertEqual(vals['Degré total'],5)
        self.assertEqual(vals['Aire du polygone de Newton'],10)
        data=COMPUTE['monomes_newton'](dict(m=4,n=4,q=3,a=0,c=1))
        vals={m['label']:m['value'] for m in data['metrics']}
        self.assertEqual(vals['Degré total'],4)
        self.assertEqual(vals['Aire du polygone de Newton'],8)

    def test_circle_parabola_vieta_and_equations(self):
        for r,h in [(1,1.125),(.5,.5),(1,1.25),(1,-2),(.75,2.5)]:
            roots,D=circle_parabola_roots(r,h)
            self.assertEqual(len(roots),4)
            coefficients=np.poly(roots)
            np.testing.assert_allclose(coefficients,[1,0,1-2*h,0,h*h-r*r],atol=1e-12)
            for z in roots:
                y=z*z-h
                self.assertLess(abs(z*z+y*y-r*r),1e-11)

    def test_intersection_multiplicities(self):
        roots,D=circle_parabola_roots(.5,.5)
        self.assertEqual(distinct_complex(roots),[[0j,4]])
        roots,D=circle_parabola_roots(1,1.25)
        pairs=distinct_complex(roots)
        self.assertEqual(sorted(k for z,k in pairs),[2,2])
        roots,D=circle_parabola_roots(1,1.125)
        self.assertEqual(len(distinct_complex(roots)),4)
        self.assertTrue(all(abs(z.imag)<1e-10 for z in roots))

    def test_resultant_determinant_and_back_substitution(self):
        x,y=sp.symbols('x y')
        for a,b in [(0,1),(2,-1),(sp.Rational(1,2),sp.Rational(1,4)),(1,0)]:
            F,G,R=elimination_polynomials(a,b)
            A=sp.Poly(F,y).coeff_monomial(y); B=F.subs(y,0)
            C=sp.Poly(G,y).coeff_monomial(y); D=G.subs(y,0)
            self.assertEqual(sp.expand(R-sp.det(sp.Matrix([[A,B],[C,D]]))),0)
            self.assertEqual(F.subs(x,a),-1)
            self.assertEqual(R.subs(x,a),0)
            if b:
                solution={x:a+1/b,y:b}
                self.assertAlmostEqual(float(F.subs(solution)),0,places=12)
                self.assertAlmostEqual(float(G.subs(solution)),0,places=12)
            else:
                self.assertEqual(sp.expand(G-F),1)

    def test_groebner_membership_and_s_certificates(self):
        x,y=sp.symbols('x y')
        for c in (-3,0,3):
            for order in ('lex','grevlex'):
                F,G,basis,certs=groebner_data(c,order)
                self.assertEqual(basis.reduce(F)[1],0)
                self.assertEqual(basis.reduce(G)[1],0)
                self.assertTrue(all(r==0 for i,j,s,r in certs))
                if order=='lex':
                    self.assertEqual(set(poly.monoms(order=order)[0] for poly in basis.polys),{(1,0),(0,3)})
                else:
                    self.assertEqual(set(poly.monoms(order=order)[0] for poly in basis.polys),{(2,0),(1,1),(0,2)})
                self.assertEqual(sp.expand(sp.resultant(F,G,x)-(y**3-c*y-1)),0)

    def test_symmetric_identities_exact(self):
        u,v,w=sp.symbols('u v w')
        # Independent symbolic discriminant from the product polynomial.
        T=sp.symbols('T'); poly=(T-u)*(T-v)*(T-w)
        self.assertEqual(sp.factor(sp.discriminant(poly,T)),(u-v)**2*(u-w)**2*(v-w)**2)
        for roots in [(-1,1,2),(1,1,-2),(.25,-.5,1.75),(3,3,3)]:
            ss,powers,D=symmetric_values(*roots)
            exact_roots=[sp.Rational(str(z)) for z in roots]
            for k in range(1,7):
                self.assertEqual(sp.expand(powers[k]-sum(z**k for z in exact_roots)),0)
            e1,e2,e3=ss
            disc=e1**2*e2**2-4*e2**3-4*e1**3*e3-27*e3**2+18*e1*e2*e3
            self.assertEqual(sp.expand(D-disc),0)

    def test_singularity_candidates(self):
        x,y,t=sp.symbols('x y t'); F=y*y-x**3-t*x*x
        self.assertEqual(F.subs({x:-2*t/3,y:0}),-4*t**3/27)
        self.assertEqual(sp.hessian(F,(x,y)).subs({x:0,y:0}),sp.diag(-2*t,2))
        s=sp.symbols('s')
        self.assertEqual(F.subs({x:s*s,y:s**3,t:0}),0)

    def test_projective_chart_transition(self):
        u,v,c=sp.symbols('u v c'); x,y=sp.symbols('x y')
        for F,chart in [(y-x*x-c,v-u*u-c*v*v),(x*y-c,u-c*v*v)]:
            transformed=sp.factor(v*v*F.subs({x:u/v,y:1/v}))
            self.assertEqual(sp.expand(transformed-chart),0)
            self.assertEqual(chart.subs({u:0,v:0}),0)

    def test_sylvester_against_eigenvalues(self):
        for a,b,c in [(0,2,0),(.5,2,.5),(1,0,0),(1.5,2,.5),(.75,.25,1)]:
            A,vals,vectors,minors,signs=quadratic_data(a,b,c)
            self.assertAlmostEqual(np.linalg.det(A),minors[2],places=12)
            np.testing.assert_allclose(A@vectors,vectors*vals,atol=1e-12)
            self.assertEqual(all(d>1e-10 for d in minors),all(vals>1e-10))
            self.assertEqual(sum(signs),3)

    def test_motzkin_bound_and_equality(self):
        rng=np.random.default_rng(417)
        x=rng.uniform(-3,3,1000); y=rng.uniform(-3,3,1000)
        for lam in (0,.5,2,3,4):
            lower=motzkin_minimum(lam)
            self.assertTrue(np.all(motzkin_value(x,y,lam)>=lower-1e-12))
            s=math.sqrt(lam/3)
            self.assertAlmostEqual(motzkin_value(s,s,lam),lower,places=12)
            self.assertAlmostEqual(motzkin_value(-s,s,lam),lower,places=12)
        # The global lower bound follows from this algebraic identity,
        # not from the preceding random check.
        xx,yy,lam,t=sp.symbols('x y lam t',real=True)
        diff=xx**4*yy**2+xx**2*yy**4-2*sp.Abs(xx*yy)**3
        self.assertEqual(sp.simplify(diff-xx**2*yy**2*(sp.Abs(xx)-sp.Abs(yy))**2),0)
        cubic=2*t**3-lam*t*t+1
        self.assertEqual(sp.expand(cubic-(1-lam**3/27)-(lam-3*t)**2*(lam+6*t)/27),0)

    def test_lagrange_gradients_extrema_and_bifurcation(self):
        for a,r,count in [(0,1,8),(1,1,8),(2,1,4),(4,1,4),(-2,1,4),(4,2,8),(-8,.5,4)]:
            rows,fmin,fmax=lagrange_data(a,r)
            self.assertEqual(len(rows),count)
            for z in rows:
                x,y,mu=z['x'],z['y'],z['multiplier']
                self.assertAlmostEqual(x*x+y*y,r*r,places=12)
                self.assertAlmostEqual(4*x**3+a*y,2*mu*x,places=10)
                self.assertAlmostEqual(4*y**3+a*x,2*mu*y,places=10)
            self.assertAlmostEqual(min(z['value'] for z in rows),fmin,places=11)
            self.assertAlmostEqual(max(z['value'] for z in rows),fmax,places=11)
            theta=np.linspace(0,2*math.pi,4001)
            x=r*np.cos(theta); y=r*np.sin(theta); values=x**4+y**4+a*x*y
            self.assertGreaterEqual(np.min(values),fmin-1e-10)
            self.assertLessEqual(np.max(values),fmax+1e-10)

class CatalogueCoverage(unittest.TestCase):
    def test_all_presets_finite_and_fields_rectangular(self):
        for lab in LABS:
            base={c['key']:c['value'] for c in lab['controls']}
            cases=[base]+[{**base,**p['values']} for p in lab['presets']]
            for control in lab['controls']:
                if control['type']=='range':
                    cases.extend([{**base,control['key']:control['min']},{**base,control['key']:control['max']}])
                else:
                    cases.extend([{**base,control['key']:option['value']} for option in control['options']])
            for params in cases:
                with self.subTest(lab=lab['id'],params=params):
                    data=clean(COMPUTE[lab['id']](params))
                    json.dumps(data,allow_nan=False)
                    scene=data['scene']
                    if scene['kind']=='field':
                        self.assertEqual(len(scene['z']),len(scene['y']))
                        self.assertTrue(all(len(row)==len(scene['x']) for row in scene['z']))
                    self.assertTrue(data['steps'])
                    self.assertTrue(data['assumptions'])

    def test_pedagogical_coverage(self):
        ids={lab['id'] for lab in LABS}
        self.assertEqual(set(GUIDES),ids)
        self.assertEqual(len(LESSONS),20)
        self.assertEqual(len(EXERCISES),30)
        for id_ in ids:
            self.assertEqual(sum(l['lab']==id_ for l in LESSONS),2)
            self.assertEqual(sum(e['lab']==id_ for e in EXERCISES),3)
            self.assertEqual(len(GUIDES[id_]['first_steps']),3)

if __name__=='__main__': unittest.main()
