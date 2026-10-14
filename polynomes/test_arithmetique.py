"""Contrôles scientifiques des identités, obstructions et limites proposées."""
from itertools import product
import json
import math
import unittest
import sympy as sp
from commun import clean
from catalogue_arithmetique import LABS
from modeles_arithmetique import COMPUTE, X, poly, bernoulli_poly, bernoulli_number, irreducible_count, enumerated_irreducibles, frobenius_factors

def parameters(id_):
    lab=next(l for l in LABS if l['id']==id_)
    return {c['key']:c['value'] for c in lab['controls']}
def calculation(id_,**values):
    p=parameters(id_);p.update(values);return COMPUTE[id_](p)
def metric_value(result,label): return next(m['value'] for m in result['metrics'] if m['label']==label)
def parse(text): return sp.sympify(text,locals={'X':X})
def table_pairs(result): return {row[0]:row[1] for row in result['table']['rows']}

class ArithmetiqueTests(unittest.TestCase):
    def test_euclidean_ledgers_are_exact_in_all_three_families(self):
        for cas,t,c in product(['tp','composition','commun'],[-2,0,2],[1,4]):
            r=calculation('euclide_bezout',cas=cas,translation=t,scale=c)
            for a,b,q,remainder in r['table']['rows']:
                A,B,Q,R=map(parse,[a,b,q,remainder]);self.assertEqual(sp.expand(A-B*Q-R),0)
                self.assertTrue(R==0 or sp.degree(R,X)<sp.degree(B,X))
            self.assertEqual(metric_value(r,'Certificat AU+BV=D'),'exact')
    def test_source_tp_remainder_and_composition_remainder(self):
        r=calculation('euclide_bezout',cas='tp');self.assertEqual(parse(metric_value(r,'Premier reste')),25*X**2-60*X+36)
        r=calculation('euclide_bezout',cas='composition');self.assertEqual(parse(metric_value(r,'Premier reste')),X)
    def test_gauss_distinguishes_irreducibility_from_absence_of_roots(self):
        r=calculation('gauss_eisenstein',cas='sans_racine',content=4)
        self.assertEqual(metric_value(r,'Irréductible sur ℚ'),'non');self.assertEqual(metric_value(r,'Contenu c(AB)'),'12')
        self.assertEqual(sp.expand((X**2-2*X+2)*(X**2+2*X+2)),X**4+4)
        for p,n,t in product([2,3,5],[3,8],[-2,2]):
            r=calculation('gauss_eisenstein',cas='eisenstein',p=str(p),n=n,translation=t)
            self.assertEqual(metric_value(r,'Irréductible sur ℚ'),'oui')
    def test_modular_inverse_coordinates_multiply_to_one(self):
        for field,modulus,a,b in product(['Q','2','3','5'],['generic','split'],[-2,0,3],[-2,1,3]):
            r=calculation('inverse_quotient',field=field,modulus=modulus,a=a,b=b)
            A=poly(X**2+a*X+b,field);M=poly(X**4+X+1 if modulus=='generic' else (X**2+1)*(X**2+X+1),field)
            coordinates=r['charts'][0]['series'][1]['y']
            # The graphic coordinates can be rounded rationals. Obtain the exact class from its Bézout certificate.
            U,V,D=sp.gcdex(A,M)
            if metric_value(r,'Classe de A')=='inversible': self.assertEqual((A*U).rem(M),poly(1,field))
            else:
                witness=M.exquo(D);self.assertFalse(witness.is_zero);self.assertTrue((A*witness).rem(M).is_zero)
            self.assertEqual(len(coordinates),4)
    def test_chinese_solution_and_projectors_are_exact(self):
        for a,b in product([-3,0,3],[-3,0,3]):
            r=calculation('restes_chinois',cas='coprime',a=a,b=b);objects=table_pairs(r)
            M1,M2,R1,R2,S,L,E1,E2=[poly(parse(objects[key])) for key in ['M₁','M₂','R₁','R₂','S','L=PPCM','E₁','E₂']]
            self.assertTrue((S-R1).rem(M1).is_zero);self.assertTrue((S-R2).rem(M2).is_zero)
            self.assertTrue((E1*E1-E1).rem(L).is_zero);self.assertTrue((E2*E2-E2).rem(L).is_zero)
            self.assertTrue((E1*E2).rem(L).is_zero);self.assertEqual(E1+E2,poly(1))
    def test_chinese_common_factor_obstruction(self):
        r=calculation('restes_chinois',cas='compatible');o=table_pairs(r)
        self.assertTrue((poly(parse(o['S']))-poly(parse(o['R₁']))).rem(poly(parse(o['M₁']))).is_zero)
        r=calculation('restes_chinois',cas='incompatible');self.assertEqual(metric_value(r,'Compatibilité'),'non')
        self.assertNotIn('S',table_pairs(r))
    def test_mobius_recovers_three_families_and_euler_phi(self):
        for kind,k,n in product(['phi','power','unit'],[0,3],[1,12,30,72,120]):
            r=calculation('mobius_diviseurs',fonction=kind,k=k,n=n)
            self.assertEqual(metric_value(r,'g(n) calculé directement'),metric_value(r,'g(n) retrouvé par Möbius'))
            self.assertEqual(metric_value(r,'(μ∗1)(n)'),int(n==1))
        self.assertEqual(metric_value(calculation('mobius_diviseurs',n=30,fonction='phi'),'g(n) retrouvé par Möbius'),8)
    def test_small_irreducibles_by_independent_trial_division(self):
        # For degrees 2 and 3 a polynomial is irreducible iff it has no root in the field.
        for p,n in product([2,3,5],[2,3]):
            count=0
            for coeff in product(range(p),repeat=n):
                if all((a**n+sum(coeff[k]*a**k for k in range(n)))%p for a in range(p)): count+=1
            self.assertEqual(irreducible_count(p,n),count)
            self.assertEqual(len(enumerated_irreducibles(p,n)),count)
        self.assertEqual(irreducible_count(2,6),9)
    def test_frobenius_factorization_complete_and_square_free(self):
        for p,n in product([2,3],range(1,5)):
            P,factors=frobenius_factors(p,n);productpoly=poly(1,str(p));counts={}
            for Q,m in factors:
                self.assertEqual(m,1);self.assertEqual(n%Q.degree(),0);productpoly*=Q
                counts[Q.degree()]=counts.get(Q.degree(),0)+1
            self.assertEqual(productpoly,P);self.assertEqual(P.gcd(P.diff()),poly(1,str(p)))
            self.assertEqual(sum(d*c for d,c in counts.items()),p**n)
            for d in sp.divisors(n): self.assertEqual(counts[d],irreducible_count(p,d))
    def test_cyclotomic_roots_and_degree_match_euler_phi(self):
        for n in [2,6,12,15,30]:
            r=calculation('cyclotomie',n=n);P=parse(metric_value(r,'Polynôme Φₙ'))
            roots=[z for z in r['scene']['points'] if z['group']==1]
            self.assertEqual(len(roots),sp.degree(P,X));self.assertEqual(len(roots),sp.totient(n))
            for z in roots: self.assertLess(abs(complex(P.subs(X,z['x']+1j*z['y']).evalf())),1e-10)
            self.assertEqual(metric_value(r,'Produit ∏ Φ_d=Xⁿ−1'),'exact')
    def test_bernoulli_normalization_and_difference_are_consistent(self):
        self.assertEqual(bernoulli_number(1),-sp.Rational(1,2))
        for n in range(1,11):
            B=bernoulli_poly(n)
            self.assertEqual(B.diff(),bernoulli_poly(n-1).mul_ground(n))
            self.assertEqual(sp.integrate(B.as_expr(),(X,0,1)),0)
            self.assertEqual(sp.expand(B.as_expr().subs(X,X+1)-B.as_expr()),n*X**(n-1))
    def test_faulhaber_sums_are_exact_for_large_power(self):
        for p,N in product([1,3,4,9],[1,10,30]):
            r=calculation('bernoulli_faulhaber',power=p,N=N)
            self.assertEqual(int(metric_value(r,'Formule polynomiale')),sum(j**p for j in range(N+1)))
        r=calculation('bernoulli_faulhaber',power=3,N=20)
        self.assertEqual(metric_value(r,'Somme directe Σ kᵖ'),(20*21//2)**2)
    def test_euler_maclaurin_bounds_and_exact_polynomial_cases(self):
        for kind,N,k,d in product(['inverse','exponential','polynomial'],[2,12,30],range(5),[2,6,9]):
            r=calculation('euler_maclaurin',fonction=kind,N=N,order=k,degree=d)
            error=metric_value(r,'Erreur absolue');bound=metric_value(r,'Borne garantie du reste')
            tolerance=2e-12*max(1,abs(metric_value(r,'Somme de j=1 à N')))
            self.assertLessEqual(error,bound+tolerance)
            if kind=='polynomial' and k>0 and 2*k>=d:
                self.assertLessEqual(error,tolerance);self.assertEqual(bound,0)
    def test_all_presets_export_strict_finite_json(self):
        for lab in LABS:
            for preset in [dict(values={}),*lab['presets']]:
                p=parameters(lab['id']);p.update(preset['values']);r=COMPUTE[lab['id']](p)
                json.dumps(clean(r),allow_nan=False)
                self.assertTrue(r['steps']);self.assertTrue(r['assumptions']);self.assertTrue(r['table']['rows'])

if __name__=='__main__': unittest.main()
