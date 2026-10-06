"""Vérifications indépendantes des représentations et de la géométrie de phase.

Les références des tests viennent des dérivées de monômes, du produit vectoriel,
des équations de Hamilton et des formules analytiques d'un oscillateur libre.
"""
import collections
import itertools
import json
import math
import unittest
import numpy as np
import sympy as sp
try:
    from . import structures as s
    from . import modeles as m
except ImportError:
    import structures as s
    import modeles as m


def exact_matrix(entries):
    return sp.Matrix([[sp.Rational(v) for v in row] for row in entries])


def columns_vec(A):
    return sp.Matrix([A[i,j] for j in range(A.cols) for i in range(A.rows)])


def blocks(result):
    return {item['label']:exact_matrix(item['entries']) for item in result['matrices']}


class Jacobi(unittest.TestCase):
    def test_produit_vectoriel_et_triangle_non_trivial(self):
        x=sp.Matrix([1,2,-1]);y=sp.Matrix([-1,1,2]);z=sp.Matrix([2,-1,1])
        self.assertEqual(s.bracket(s.hat(x),s.hat(y)),s.hat(x.cross(y)))
        expected=[sp.Matrix([3,-2,-1]),sp.Matrix([-1,3,-2]),sp.Matrix([-2,-1,3])]
        actual=s.jacobi_parts(s.hat(x),s.hat(y),s.hat(z))
        self.assertEqual(actual,[s.hat(v) for v in expected])
        self.assertEqual(sum(expected,sp.zeros(3,1)),sp.zeros(3,1))
        self.assertTrue(all(v.dot(v)==14 for v in expected))

    def test_expansion_douze_mots_sans_supposer_jacobi(self):
        X=sp.Matrix([[2,1,0],[1,-1,3],[0,2,1]])
        Y=sp.Matrix([[0,1,2],[3,1,0],[1,-1,1]])
        Z=sp.Matrix([[1,2,1],[0,-1,3],[2,0,1]])
        scene=s.jacobi_scene(X,Y,Z);lookup={'X':X,'Y':Y,'Z':Z}
        coefficients=collections.Counter();contributions=[sp.zeros(3) for _ in range(3)]
        for term in scene['expansion']:
            coefficients[term['word']]+=term['sign']
            value=sp.eye(3)
            for letter in term['word']:value=value*lookup[letter]
            contributions[term['contribution']]+=term['sign']*value
        self.assertEqual(len(scene['expansion']),12)
        self.assertEqual(set(coefficients),{'XYZ','XZY','YXZ','YZX','ZXY','ZYX'})
        self.assertTrue(all(value==0 for value in coefficients.values()))
        self.assertEqual(contributions,[exact_matrix(c['matrix']) for c in scene['contributions']])
        self.assertEqual(sum(contributions,sp.zeros(3)),sp.zeros(3))
        self.assertTrue(all(M!=sp.zeros(3) for M in contributions))

    def test_adjoint_vectorisation_et_representation(self):
        A=sp.Matrix([[1,2],[3,-1]]);B=sp.Matrix([[2,0],[1,-2]])
        T=sp.Matrix([[2,3],[5,7]])
        self.assertEqual(s.adjoint_matrix(A)*columns_vec(T),columns_vec(A*T-T*A))
        self.assertEqual(s.bracket(s.adjoint_matrix(A),s.adjoint_matrix(B)),s.adjoint_matrix(A*B-B*A))
        self.assertEqual(s.adjoint_matrix(sp.eye(2)),sp.zeros(4))
        self.assertEqual(s.adjoint_matrix(A).nullspace().__len__(),2)

    def test_generateurs_denses_sp4_et_trois_contributions(self):
        J=s.symplectic_form(2);matrices=s.classical_generators('sp')
        self.assertTrue(all(all(entry!=0 for entry in M) for M in matrices))
        for A in matrices:
            self.assertEqual(A.T*J+J*A,sp.zeros(4))
            K=-J*A
            self.assertEqual(K.T,K)
            self.assertTrue(all(K[:i,:i].det()>0 for i in range(1,5)))
        for family in ('so','sl','sp'):
            parts=s.jacobi_parts(*s.classical_generators(family))
            self.assertTrue(all(M!=sp.zeros(M.rows) for M in parts))
            self.assertEqual(sum(parts,sp.zeros(parts[0].rows)),sp.zeros(parts[0].rows))


class Representations(unittest.TestCase):
    def test_derivation_independante_des_monomes(self):
        x,y=sp.symbols('x y')
        for degree in range(2,7):
            monomials=[x**(degree-k)*y**k for k in range(degree+1)]
            matrices=[]
            for operator in (lambda p:x*sp.diff(p,y),lambda p:y*sp.diff(p,x),lambda p:x*sp.diff(p,x)-y*sp.diff(p,y)):
                matrices.append(sp.Matrix.hstack(*[sp.Matrix([sp.Poly(operator(p),x,y).coeff_monomial(q) for q in monomials]) for p in monomials]))
            E,F,H=s.sl2_polynomial_representation(degree)
            self.assertEqual([E,F,H],matrices)
            self.assertEqual(H*E-E*H,2*E);self.assertEqual(H*F-F*H,-2*F)
            self.assertEqual(E*F-F*E,H)

    def test_nilpotence_et_noyaux_distincts(self):
        for degree in range(2,7):
            E,F,H=s.sl2_polynomial_representation(degree);n=degree+1
            self.assertEqual(E**n,sp.zeros(n));self.assertNotEqual(E**degree,sp.zeros(n))
            self.assertEqual(F**n,sp.zeros(n));self.assertNotEqual(F**degree,sp.zeros(n))
            self.assertEqual(len(E.nullspace()),1)
            rho=sp.Matrix.hstack(*[columns_vec(M) for M in (E,F,H)])
            self.assertEqual(rho.rank(),3)

    def test_action_de_groupe_et_centre(self):
        g=sp.Matrix([[2,1],[1,1]]);h=sp.Matrix([[1,sp.Rational(2,3)],[0,1]])
        for degree in range(2,7):
            self.assertEqual(s.homogeneous_action(g*h,degree),s.homogeneous_action(g,degree)*s.homogeneous_action(h,degree))
            self.assertEqual(s.homogeneous_action(-sp.eye(2),degree),(-1)**degree*sp.eye(degree+1))
            self.assertEqual(s.homogeneous_action(sp.eye(2),degree),sp.eye(degree+1))

    def test_exponentielles_nilpotentes_et_substitution(self):
        t=sp.Rational(2,3)
        for degree in range(2,7):
            E,F,_=s.sl2_polynomial_representation(degree);n=degree+1
            for operator,g in ((E,sp.Matrix([[1,t],[0,1]])),(F,sp.Matrix([[1,0],[t,1]]))):
                exponential=sum((t**k*operator**k/sp.factorial(k) for k in range(n)),sp.zeros(n))
                self.assertEqual(exponential,s.homogeneous_action(g,degree))

    def test_metrique_adaptee_et_rotation(self):
        for degree in range(2,7):
            E,F,_=s.sl2_polynomial_representation(degree)
            G=sp.diag(*[sp.Rational(1,math.comb(degree,k)) for k in range(degree+1)])
            T=E-F
            self.assertEqual(T.T*G+G*T,sp.zeros(degree+1))
            self.assertNotEqual(T.T+T,sp.zeros(degree+1))
            result=m.calculate(dict(lab='representations',degree=degree,time=.7))
            M=np.array(blocks(result)['ρ(exp tX)'],dtype=float);Gf=np.array(G,dtype=float)
            np.testing.assert_allclose(M.T@Gf@M,Gf,atol=1e-13)

    def test_diagramme_poids_fleches(self):
        result=m.calculate(dict(lab='representations',degree=6,generator='E',time=.5))
        scene=next(item for item in result['scenes'] if item['kind']=='weights')
        nodes={node['id']:node for node in scene['nodes']}
        self.assertEqual([node['weight'] for node in scene['nodes']],[6,4,2,0,-2,-4,-6])
        self.assertEqual(len(scene['edges']),12)
        E,F,_=s.sl2_polynomial_representation(6)
        for edge in scene['edges']:
            origin=int(edge['from']);target=int(edge['to']);operator={'E':E,'F':F}[edge['operator']]
            self.assertEqual(edge['coefficient'],operator[target,origin])
            self.assertEqual(nodes[edge['to']]['weight']-nodes[edge['from']]['weight'],2 if edge['operator']=='E' else -2)

    def test_reproduction_et_entrees_bornees(self):
        for degree,generator in itertools.product((2,6),('rotation','E','F','H')):
            result=m.calculate(dict(lab='representations',degree=degree,generator=generator,time=1,coefficients=['1/3']*(degree+1)))
            exported=json.loads(json.dumps(result,allow_nan=False))
            self.assertEqual(m.calculate(dict(lab=result['lab'],**exported['parameters'])),result)
        for bad in ('x**2',[1,2],['sin(1)']*7):
            with self.assertRaises(ValueError):m.calculate(dict(lab='representations',degree=6,coefficients=bad))
        for degree in (True,1,7,10**500):
            with self.assertRaises(ValueError):m.calculate(dict(lab='representations',degree=degree))


class Symplectique(unittest.TestCase):
    def test_forme_hamilton_et_positivite_aux_bords(self):
        for modes,coupling in itertools.product((2,3),(sp.Rational(-3,5),0,sp.Rational(3,5))):
            J,K,A=s.coupled_hamiltonian(modes,[sp.Rational(1,2),3,sp.Rational(1,2)],coupling)
            self.assertEqual(J.T,-J);self.assertEqual(J*J,-sp.eye(2*modes))
            self.assertEqual(A[:modes,modes:],sp.eye(modes))
            self.assertEqual(A[modes:,:modes],-K[:modes,:modes])
            self.assertTrue(all(K[:i,:i].det()>0 for i in range(1,2*modes+1)))
            self.assertEqual(A.T*J+J*A,sp.zeros(2*modes))
            self.assertEqual(A.T*K+K*A,sp.zeros(2*modes))

    def test_cayley_preserve_deux_formes_exactes(self):
        for modes,h in itertools.product((2,3),(sp.Rational(1,5),sp.Rational(1,2))):
            J,K,A=s.coupled_hamiltonian(modes,[1,sp.Rational(3,2),2],sp.Rational(2,5))
            C=s.cayley_step(A,h);I=sp.eye(2*modes)
            self.assertEqual((I-h*A/2)*C,I+h*A/2)
            self.assertEqual(C.T*J*C,J);self.assertEqual(C.T*K*C,K)
            self.assertEqual(C.det(),1)

    def test_defaut_euler_exact_et_energie(self):
        J,K,A=s.coupled_hamiltonian(2,[1,2,3],sp.Rational(1,3));h=sp.Rational(1,4)
        Euler=sp.eye(4)+h*A
        self.assertEqual(Euler.T*J*Euler-J,h*h*A.T*J*A)
        self.assertNotEqual(Euler.T*J*Euler,J)
        drift=Euler.T*K*Euler-K
        self.assertEqual(drift,h*h*A.T*K*A)
        self.assertTrue(all(drift[:i,:i].det()>0 for i in range(1,5)))

    def test_determinant_un_ne_suffit_pas_et_cisaillement(self):
        for modes in (2,3):
            result=m.calculate(dict(lab='symplectique',modes=str(modes),transform='volume',shear=1,steps=20))
            matrices=blocks(result);M=matrices['M choisi'];J=matrices['J : forme symplectique']
            self.assertEqual(M.det(),1);self.assertNotEqual(M.T*J*M,J)
            canonical=m.calculate(dict(lab='symplectique',modes=str(modes),transform='cisaillement',shear=1,steps=20))
            S=blocks(canonical)['M choisi']
            self.assertEqual(S.T*J*S,J);self.assertEqual(S.det(),1)
            self.assertTrue(all(S[i,modes+j]!=0 for i,j in itertools.product(range(modes),repeat=2)))

    def test_pfaffien_j_convention_et_loi(self):
        for modes in (2,3):
            J=s.symplectic_form(modes)
            # En dimension 4 J13=J24=1 : Pf=0−1+0=−1.
            self.assertEqual(m.pfaffian(J),(-1)**(modes*(modes-1)//2))
            _,_,A=s.coupled_hamiltonian(modes,[1,2,3],sp.Rational(1,3))
            C=s.cayley_step(A,sp.Rational(1,5))
            self.assertEqual(m.pfaffian(C.T*J*C),C.det()*m.pfaffian(J))

    def test_frequences_et_rotation_cayley(self):
        omega=sp.Rational(3,2);kappa=sp.Rational(2,5);X=sp.Symbol('X')
        _,K,_=s.coupled_hamiltonian(2,[omega,omega],kappa)
        self.assertEqual(K[:2,:2].charpoly(X).as_expr(),sp.expand((X-omega**2*(1-kappa))*(X-omega**2*(1+kappa))))
        A=sp.Matrix([[0,1],[-omega**2,0]]);h=sp.Rational(1,5)
        C=np.array(s.cayley_step(A,h),dtype=float);angle=2*math.atan(float(h*omega)/2)
        expected=np.array([[math.cos(angle),math.sin(angle)/float(omega)],[-float(omega)*math.sin(angle),math.cos(angle)]])
        np.testing.assert_allclose(C,expected,atol=1e-15)

    def test_simulation_controle_analytique_non_couple(self):
        result=m.calculate(dict(lab='symplectique',omega1=1,omega2=1,coupling=0,step=.1,steps=20))
        chart=result['charts'][0];cayley=np.array(chart['series'][0]['y']);euler=np.array(chart['series'][1]['y'])
        initial=.5*(1+.5**2)
        np.testing.assert_allclose(cayley,initial,rtol=1e-13)
        np.testing.assert_allclose(euler,initial*1.01**np.arange(21),rtol=1e-13)
        scene=result['scenes'][0];self.assertEqual(scene['kind'],'oscillators')
        self.assertEqual(scene['modes'],2)
        angle=2*math.atan(.1/2)
        for frame in scene['frames']:
            k=round(frame['time']/.1)
            np.testing.assert_allclose(frame['values'],[math.cos(k*angle),.5*math.cos(k*angle)],atol=1e-13)
            np.testing.assert_allclose(frame['momenta'],[-math.sin(k*angle),-.5*math.sin(k*angle)],atol=1e-13)

    def test_pire_bord_numerique_fini_et_export(self):
        params=dict(lab='symplectique',modes='3',omega1=3,omega2=3,omega3=3,coupling=.6,step=.5,steps=400)
        result=m.calculate(params);json.dumps(result,allow_nan=False)
        for series in result['charts'][0]['series']:
            self.assertTrue(all(math.isfinite(value) and value>0 for value in series['y']))
        self.assertEqual(m.calculate(dict(result['parameters'],lab='symplectique')),result)
        self.assertLess(max(result['charts'][0]['series'][1]['y']),1e300)
        for bad in (True,'4',4,'2.0'):
            with self.assertRaises(ValueError):m.calculate(dict(lab='symplectique',modes=bad))


if __name__=='__main__':unittest.main()
