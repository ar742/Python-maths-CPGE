"""Contrôles mathématiques indépendants des fractions et quadratures."""
import math
import unittest
import numpy as np
import sympy as sp
from modeles_classiques import X,ordre,barycentric,orthogonal_data,moment,rationnelle_recueil,poles_multiples,annulations

class ClassiquesTests(unittest.TestCase):
    def test_source_partial_fraction_matches_original_polynomials(self):
        P=X**4-2*X**3-7*X**2+29*X-21
        Q=X**4-5*X**3+6*X**2+4*X-8
        F=1+2/(X+1)+1/(X-2)+2/(X-2)**2+3/(X-2)**3
        self.assertEqual(sp.cancel(P/Q-F),0)
        self.assertEqual(ordre(P/Q,-1),1)
        self.assertEqual(ordre(P/Q,2),3)

    def test_removed_poles_do_not_create_false_graph_breaks(self):
        r=rationnelle_recueil(dict(A=0,B=0,C=0,D=0,shift=0))
        y=r['charts'][0]['series'][0]['y']
        self.assertTrue(all(value==1 for value in y))

    def test_taylor_coefficients_and_order_loss_at_a_root(self):
        p=poles_multiples(dict(a=0,m=3,c=2))
        self.assertEqual([row[1] for row in p['table']['rows']],['2','1','1','X'])
        g=X**4-X**2+X+1
        self.assertEqual(g.subs(X,-1),0)
        self.assertEqual(sp.diff(g,X).subs(X,-1),-1)
        self.assertEqual(ordre(g/(X+1)**4,-1),3)

    def test_colliding_exclusions_add_denominator_multiplicities(self):
        r=annulations(dict(a=1,b=1,k=3,m=2))
        self.assertEqual(r['metrics'][0]['value'],'1')
        self.assertEqual(r['metrics'][1]['value'],1)
        self.assertEqual(r['metrics'][2]['value'],1)
        self.assertEqual(r['table']['rows'][0][3],'1')
        r=annulations(dict(a=1,b=1,k=2,m=2))
        self.assertEqual(r['table']['rows'][0][2],'1')

    def test_barycentric_interpolation_reproduces_polynomials(self):
        f=lambda x:x**4-3*x**3+2*x-5
        xx=np.linspace(-1,1,137)
        for n in (5,10,18):
            for nodes in (np.linspace(-1,1,n+1),np.cos((2*np.arange(n+1)+1)*np.pi/(2*(n+1)))):
                np.testing.assert_allclose(barycentric(nodes,f(nodes),xx),f(xx),rtol=0,atol=2e-10)
                np.testing.assert_allclose(barycentric(nodes,f(nodes),nodes),f(nodes),rtol=0,atol=1e-13)

    def test_legendre_rodrigues_and_orthogonality(self):
        n=5
        P=orthogonal_data('legendre',n)[0]
        rod=sp.diff((X**2-1)**n,X,n)/(2**n*sp.factorial(n))
        self.assertEqual(sp.expand(P-rod),0)
        for k in range(n): self.assertEqual(sp.integrate(P*X**k,(X,-1,1)),0)
        self.assertEqual(sp.integrate(P**2,(X,-1,1)),sp.Rational(2,2*n+1))

    def test_gauss_quadratures_have_the_advertised_moments(self):
        for family in ('legendre','chebyshev','hermite'):
            for n in (2,6,10):
                P,nodes,weights,_,_=orthogonal_data(family,n)
                self.assertTrue(np.all(weights>0))
                for k in range(2*n):
                    estimate=math.fsum(float(w*x**k) for x,w in zip(nodes,weights))
                    exact=moment(family,k)
                    self.assertAlmostEqual(estimate/(abs(exact) or 1),exact/(abs(exact) or 1),delta=2e-13)
                estimate=math.fsum(float(w*float(P.subs(X,float(x)))**2) for x,w in zip(nodes,weights))
                self.assertLess(estimate,1e-9)

    def test_two_hermite_conventions_are_not_confused(self):
        self.assertEqual(orthogonal_data('hermite',2)[0],X**2-1)
        _,nodes,weights,_,_=orthogonal_data('hermite',6)
        self.assertAlmostEqual(math.fsum(weights),math.sqrt(2*math.pi),delta=1e-14)
        self.assertEqual(moment('hermite',4),3*math.sqrt(2*math.pi))

if __name__=='__main__': unittest.main()
