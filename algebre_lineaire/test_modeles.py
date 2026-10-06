"""Certificats indépendants : arithmétique, géométrie et algèbre exacte.

Exécution : python -m unittest discover -s algebre_lineaire -p 'test_[mr]*.py'.
Les tests ne se contentent pas de lire les indicateurs booléens du moteur.
"""
import itertools
import json
import math
import unittest
import numpy as np
import sympy as sp
try:
    from . import calculs_exacts as ce
    from . import modeles as m
except ImportError:
    import calculs_exacts as ce
    import modeles as m


def permutation_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


class ParseurRationnel(unittest.TestCase):
    def test_litteraux_exacts(self):
        A=ce.parse_matrix("-2/3, .25; +4, -0.125")
        self.assertEqual(A,sp.Matrix([[sp.Rational(-2,3),sp.Rational(1,4)],[4,sp.Rational(-1,8)]]))
        self.assertEqual(ce.parse_matrix('[[1,"2/3"],[0,0.25]]'),sp.Matrix([[1,sp.Rational(2,3)],[0,sp.Rational(1,4)]]))

    def test_expressions_interdites(self):
        for value in ("sqrt(2)","2**10","1+2","pi","nan","1/0","1e3","__import__('os').getcwd()","x",True,None,float('inf')):
            with self.subTest(value=value),self.assertRaises(ValueError):ce.parse_scalar(value)

    def test_limites_dimensions_et_taille(self):
        for value in ("", "1 2;3", "1 "*100, [[1]*5]*5, "1"*5000):
            with self.subTest(value=value),self.assertRaises(ValueError):ce.parse_matrix(value)
        for value in ("10001","1/1000001","0.0000001","9999999",10**200):
            with self.subTest(value=value),self.assertRaises(ValueError):ce.parse_scalar(value)
        self.assertEqual(ce.parse_matrix([[1]*6]*6,max_size=6).shape,(6,6))
        with self.assertRaises(ValueError):ce.parse_matrix("1 2 3",square=True)

    def test_vecteur_formats_et_longueur(self):
        expected=sp.Matrix([1,sp.Rational(-2,3),sp.Rational(1,5)])
        for value in ("1;-2/3;.2",[1,"-2/3",.2],[[1],["-2/3"],[.2]]):self.assertEqual(ce.parse_vector(value,3),expected)
        with self.assertRaises(ValueError):ce.parse_vector("1;2",3)

    def test_parametres_invalides(self):
        for value in (True,float('nan'),float('inf'),10**500,"1"):
            with self.subTest(value=value),self.assertRaises(ValueError):ce.number({"a":value},"a",1,-3,3)
        with self.assertRaises(ValueError):ce.number({"a":1.5},"a",1,0,3,True)
        with self.assertRaises(ValueError):m.calculate([])
        with self.assertRaises(ValueError):m.calculate({"lab":"inconnu"})

    def test_polynome_horner(self):
        A=sp.Matrix([[1,2],[3,4]]);p=sp.Poly(ce.X**3-sp.Rational(2,3)*ce.X+5,ce.X)
        self.assertEqual(ce.polynomial_evaluate(A,p),A**3-sp.Rational(2,3)*A+5*sp.eye(2))
        with self.assertRaises(ValueError):ce.polynomial_evaluate(A,"X+1")

    def test_smith_structure_connue(self):
        X=ce.X
        cases=[(sp.diag(1,1,2),[X-1,(X-1)*(X-2)]),
               (sp.Matrix([[1,1,0],[0,1,0],[0,0,2]]),[(X-1)**2*(X-2)]),
               (sp.zeros(3),[X,X,X]),
               (sp.Matrix([[0,-1],[1,0]]),[X**2+1])]
        for A,expected in cases:
            factors=ce.invariant_factors(A)
            self.assertEqual(factors,[sp.Poly(p,X,domain=sp.QQ) for p in expected])
            self.assertEqual(sp.expand(sp.prod(p.as_expr() for p in factors)),A.charpoly(X).as_expr())


class Anneaux(unittest.TestCase):
    def test_det_non_nul_non_unite(self):
        for ring,expected in (("Q",True),("Z",False),("mod",False)):
            result=m.calculate(dict(lab="anneaux",ring=ring,matrix="2 0;0 1",modulus=6))
            self.assertEqual(result['theory']['unit'],expected)

    def test_modulaire_pivot_non_unite(self):
        A=sp.Matrix([[2,1],[3,2]]) # det=1 ; premier pivot 2 non-unité modulo 6.
        inverse=m.modular_inverse(A,6)
        self.assertIsNotNone(inverse)
        self.assertEqual((A*inverse).applyfunc(lambda x:x%6),sp.eye(2))
        self.assertEqual((inverse*A).applyfunc(lambda x:x%6),sp.eye(2))

    def test_inverse_modulaire_differents_modules(self):
        matrices=[sp.Matrix([[1,2],[3,5]]),sp.Matrix([[3,2],[4,3]]),sp.diag(2,1),sp.zeros(2)]
        for modulus,A in itertools.product(range(2,13),matrices):
            inverse=m.modular_inverse(A,modulus)
            self.assertEqual(inverse is not None,math.gcd(int(A.det()),modulus)==1)
            if inverse is not None:self.assertEqual((A*inverse).applyfunc(lambda x:x%modulus),sp.eye(2))

    def test_unimodulaire(self):
        result=m.calculate(dict(lab="anneaux",ring="Z",matrix="1 2;3 5"))
        inv=ce.parse_matrix(result['theory']['inverse'])
        self.assertTrue(all(v.q==1 for v in inv));self.assertEqual(sp.Matrix([[1,2],[3,5]])*inv,sp.eye(2))
        for ring in ("Z","mod"):
            with self.assertRaises(ValueError):m.calculate(dict(lab="anneaux",ring=ring,matrix="1/2 0;0 1"))

    def test_cardinaux_par_comptage_direct(self):
        for modulus in range(2,9):
            count=sum(math.gcd(a*d-b*c,modulus)==1 for a,b,c,d in itertools.product(range(modulus),repeat=4))
            self.assertEqual(m.gl2_mod_cardinality(modulus),count)
            if sp.isprime(modulus):self.assertEqual(m.gl_cardinality(2,modulus),count)
        self.assertEqual(m.gl_cardinality(3,2),168)
        with self.assertRaises(ValueError):m.gl_cardinality(2,4)


class GeometrieEtLie(unittest.TestCase):
    def test_aire_orientation_et_ordre(self):
        for sx,sy in ((2,1),(-2,1),(0,1)):
            result=m.calculate(dict(lab="geometrie",sx=sx,sy=sy,shear=1,lower=1))
            blocks={x['label']:ce.parse_matrix(x['entries']) for x in result['matrices']}
            A=blocks['A'];B=blocks['B'];self.assertEqual(A.det(),sx*sy)
            self.assertEqual(blocks['AB'],A*B);self.assertEqual(blocks['BA'],B*A)
            # Aire orientée par la formule du lacet sur les sommets transformés.
            vertices=[A*sp.Matrix(v) for v in ((0,0),(1,0),(1,1),(0,1))]
            area=sum(vertices[i][0]*vertices[(i+1)%4][1]-vertices[(i+1)%4][0]*vertices[i][1] for i in range(4))/2
            self.assertEqual(area,A.det())

    def test_jacobi_bilinearite_et_trace(self):
        A=sp.Matrix([[2,1,3],[1,0,-1],[4,2,1]]);B=sp.Matrix([[0,1,2],[3,1,0],[2,-1,1]]);C=sp.diag(1,2,3)
        bracket=m.commutator
        self.assertEqual(bracket(A,bracket(B,C))+bracket(B,bracket(C,A))+bracket(C,bracket(A,B)),sp.zeros(3))
        self.assertEqual(bracket(2*A+C,B),2*bracket(A,B)+bracket(C,B))
        self.assertEqual(sp.trace(bracket(A,B)),0)

    def test_fermeture_et_conditions_classiques(self):
        for family in ("gl","sl","so","sp"):
            A,B,C=m.lie_generators(family)
            for M in (A,B,C,m.commutator(A,B)):
                self.assertTrue(m.lie_membership(M,family))
            self.assertEqual(m.commutator(A,m.commutator(B,C))+m.commutator(B,m.commutator(C,A))+m.commutator(C,m.commutator(A,B)),sp.zeros(A.rows))
        J=m.symplectic_J();self.assertEqual(J.T,-J);self.assertEqual(J**2,-sp.eye(4))

    def test_exponentielle_numerique_contre_formules_exactes(self):
        N=sp.Matrix([[0,1,0],[0,0,1],[0,0,0]])
        for t in (-2,-.4,0,.5,2):
            np.testing.assert_allclose(ce.numeric_exp(t*N),np.array(sp.eye(3)+t*N+t*t*N**2/2,dtype=float),atol=1e-13)
        angle=.7;R=sp.Matrix([[0,-angle],[angle,0]])
        np.testing.assert_allclose(ce.numeric_exp(R),[[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]],atol=1e-14)
        np.testing.assert_allclose(ce.numeric_exp(sp.diag(-2,3)),np.diag([math.exp(-2),math.exp(3)]),rtol=3e-14)

    def test_exponentielles_conservent_formes(self):
        for family in ("sl","so","sp"):
            A,_,_=m.lie_generators(family)
            E=ce.numeric_exp(2*A);I=np.eye(A.rows)
            if family=="sl":self.assertAlmostEqual(np.linalg.det(E),1,places=12)
            elif family=="so":np.testing.assert_allclose(E.T@E,I,atol=1e-13)
            else:
                J=np.array(m.symplectic_J(),dtype=float);np.testing.assert_allclose(E.T@J@E,J,atol=1e-13)

    def test_signe_commutateur_groupe_degre2(self):
        A,B,_=m.lie_generators("sl");h=sp.Symbol('h')
        group=(sp.eye(2)+h*A)*(sp.eye(2)+h*B)*(sp.eye(2)-h*A)*(sp.eye(2)-h*B)
        term=group.applyfunc(lambda v:sp.expand(v).coeff(h,2))
        self.assertEqual(term,m.commutator(A,B))

    def test_limite_tangente_non_nilpotente(self):
        A,_,_=m.lie_generators('gl');Af=np.array(A,dtype=float);I=np.eye(2)
        errors=[np.linalg.norm((ce.numeric_exp(h*A)-I)/h-Af) for h in (.01,.005)]
        self.assertGreater(errors[0]/errors[1],1.99);self.assertLess(errors[0]/errors[1],2.02)


class Gauss(unittest.TestCase):
    def test_certificats_et_pivots_nuls(self):
        matrices=[sp.Matrix([[0,1,2],[0,0,3],[0,0,0]]),sp.Matrix([[0,2],[1,3]]),
                  sp.zeros(3,4),sp.Matrix([[1,2,3,4],[2,4,6,8]])]
        for A in matrices:
            R,pivots,E,steps=ce.rref_steps(A)
            self.assertEqual(E*A,R);self.assertNotEqual(E.det(),0)
            self.assertEqual((R,pivots),A.rref())
            self.assertTrue(all(isinstance(entry,str) for item in steps for row in item['matrix'] for entry in row))

    def test_solution_noyau_image_rectangulaire(self):
        A=sp.Matrix([[1,2,3,4],[2,4,6,8]]);b=sp.Matrix([3,6])
        result=m.calculate(dict(lab='gauss',matrix=ce.serialize_matrix(A),vector=[3,6]));theory=result['theory']
        x=sp.Matrix([ce.parse_scalar(v) for v in theory['solution']]);self.assertEqual(A*x,b)
        self.assertEqual(theory['rank']+theory['nullity'],A.cols)
        kernel=sp.Matrix.hstack(*[sp.Matrix([ce.parse_scalar(v) for v in column]) for column in theory['kernel']])
        self.assertEqual(A*kernel,sp.zeros(2,3));self.assertEqual(kernel.rank(),3)
        image=next(block for block in result['matrices'] if block['label']=="Base de l'image")
        self.assertEqual(ce.parse_matrix(image['entries']),A[:,[0]])

    def test_incompatibilite(self):
        result=m.calculate(dict(lab='gauss',matrix='1 2;2 4',vector='1;3'))
        self.assertFalse(result['theory']['compatible']);self.assertIsNone(result['theory']['solution'])
        R=ce.parse_matrix(result['matrices'][2]['entries']);self.assertEqual(R[-1,:],sp.Matrix([[0,0,1]]))

    def test_gauss_ne_preserve_pas_spectre(self):
        A=sp.Matrix([[1,2],[0,3]]);R,_,_,_=ce.rref_steps(A)
        self.assertEqual(R,sp.eye(2));self.assertNotEqual(A.charpoly().as_expr(),R.charpoly().as_expr())


class Pfaffien(unittest.TestCase):
    def test_formule_4_et_definition_permutations(self):
        A=sp.Matrix([[0,2,3,5],[-2,0,7,11],[-3,-7,0,13],[-5,-11,-13,0]])
        direct=A[0,1]*A[2,3]-A[0,2]*A[1,3]+A[0,3]*A[1,2]
        permutation_sum=sum(permutation_sign(p)*A[p[0],p[1]]*A[p[2],p[3]] for p in itertools.permutations(range(4)))/8
        self.assertEqual(m.pfaffian(A),direct);self.assertEqual(m.pfaffian(A),permutation_sum)

    def test_determinant_carre_dim4_6_8(self):
        for n,a,b in itertools.product((4,6,8),(-1,0,2),(0,1)):
            A=m.pfaffian_family(n,a,b);pf=m.pfaffian(A)
            self.assertEqual(A.det(),pf**2)
            self.assertEqual(len(m.pfaffian_terms(A)),math.prod(range(1,n,2)))

    def test_congruence_y_compris_singuliere(self):
        A=m.pfaffian_family(6,2,3)
        for scale in (-2,0,1):
            P=sp.eye(6);P[0,0]=scale;P[0,2]=2;P[3,1]=-1
            self.assertEqual(m.pfaffian(P.T*A*P),P.det()*m.pfaffian(A))
        P=sp.eye(6);P.col_swap(0,1)
        self.assertEqual(m.pfaffian(P.T*A*P),-m.pfaffian(A))

    def test_impair_et_rejet_non_antisymetrique(self):
        A=m.pfaffian_family(6,1,2)[:5,:5];self.assertEqual(A.det(),0)
        with self.assertRaises(ValueError):m.pfaffian(sp.eye(2))


class Projecteurs(unittest.TestCase):
    def test_certificats_bezout_primaires(self):
        A=sp.Matrix([[1,2,1],[0,1,1],[0,0,3]])
        minimal,items=m.primary_projectors(A);self.assertEqual(minimal,sp.Poly((ce.X-1)**2*(ce.X-3),ce.X,domain=sp.QQ))
        self.assertEqual(sum((item['P'] for item in items),sp.zeros(3)),sp.eye(3))
        for i,item in enumerate(items):
            P=item['P'];f=item['f']
            self.assertEqual(item['u']*f+item['v']*item['g'],sp.Poly(1,ce.X,domain=sp.QQ))
            self.assertEqual(P*P,P);self.assertEqual(A*P,P*A)
            self.assertEqual(ce.polynomial_evaluate(A,f)*P,sp.zeros(3))
            self.assertEqual(P.rank(),len(ce.polynomial_evaluate(A,f).nullspace()))
            for j,other in enumerate(items):
                if i!=j:self.assertEqual(P*other['P'],sp.zeros(3))

    def test_collision_et_couplage_nul(self):
        for coupling,expected_degree in ((1,2),(0,1)):
            result=m.calculate(dict(lab='projecteurs',lambda1=2,lambda2=2,coupling=coupling))
            self.assertEqual(len(result['theory']['projectors']),1)
            self.assertEqual(ce.parse_matrix(result['theory']['projectors'][0]),sp.eye(3))
            expected=sp.Poly((ce.X-2)**expected_degree,ce.X,domain=sp.QQ)
            A=ce.parse_matrix(result['matrices'][0]['entries']);self.assertEqual(m.primary_projectors(A)[0],expected)

    def test_facteur_irreductible_sur_Q(self):
        A=sp.diag(sp.Matrix([[0,-1],[1,0]]),sp.Matrix([[2]]))
        minimal,items=m.primary_projectors(A)
        self.assertEqual(minimal,sp.Poly((ce.X**2+1)*(ce.X-2),ce.X,domain=sp.QQ));self.assertEqual(len(items),2)
        self.assertEqual(sorted(item['P'].rank() for item in items),[1,2])

    def test_oblique_image_noyau_et_norme(self):
        for shear in (-2,0,3):
            result=m.calculate(dict(lab='projecteurs',mode='oblique',shear=shear,x=1,y=2))
            P=ce.parse_matrix(result['matrices'][0]['entries']);self.assertEqual(P**2,P)
            self.assertEqual(P*sp.Matrix([shear,1]),sp.zeros(2,1));self.assertEqual(P*sp.Matrix([1,0]),sp.Matrix([1,0]))
            self.assertEqual(P.T==P,shear==0)
            self.assertAlmostEqual(np.linalg.norm(np.array(P,dtype=float),2),math.sqrt(1+shear**2),places=12)


class Quadratiques(unittest.TestCase):
    def test_quatre_familles_inerties(self):
        expected={'definie':[2,0,0],'indefinie':[1,1,0],'degenerate':[1,0,1],'isotrope':[1,1,0]}
        for case,shear in itertools.product(expected,(-2,0,1,3)):
            result=m.calculate(dict(lab='quadratiques',case=case,shear=shear))
            S=ce.parse_matrix(result['matrices'][0]['entries']);B=ce.parse_matrix(result['matrices'][1]['entries']);D=ce.parse_matrix(result['matrices'][2]['entries'])
            self.assertEqual(B.T*S*B,D);self.assertNotEqual(B.det(),0);self.assertTrue(D.is_diagonal())
            self.assertEqual(result['theory']['inertia'],expected[case])
            eig=np.linalg.eigvalsh(np.array(S,dtype=float))
            self.assertEqual([sum(eig>1e-9),sum(eig< -1e-9),sum(abs(eig)<=1e-9)],expected[case])

    def test_pivots_isotropes_et_bloc_nul(self):
        for S in (sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,0,0],[0,0,2],[0,2,0]]),sp.zeros(4)):
            B,D,steps=m.quadratic_congruence(S)
            self.assertNotEqual(B.det(),0);self.assertEqual(B.T*S*B,D);self.assertTrue(D.is_diagonal())

    def test_congruence_generale_rationnelle(self):
        P=sp.Matrix([[1,1,2],[0,1,-1],[0,0,1]]);base=sp.diag(-2,0,3);S=P.T*base*P
        B,D,_=m.quadratic_congruence(S)
        self.assertEqual(B.T*S*B,D);self.assertNotEqual(B.det(),0)
        diagonal=[D[i,i] for i in range(3)]
        self.assertEqual([sum(bool(v>0) for v in diagonal),sum(bool(v<0) for v in diagonal),sum(v==0 for v in diagonal)],[1,1,1])

    def test_valeur_vecteur_et_distinction_similitude(self):
        result=m.calculate(dict(lab='quadratiques',case='definie',shear=1,x=2,y=-1))
        S=ce.parse_matrix(result['matrices'][0]['entries']);B=ce.parse_matrix(result['matrices'][1]['entries']);D=ce.parse_matrix(result['matrices'][2]['entries']);similar=ce.parse_matrix(result['matrices'][3]['entries'])
        self.assertEqual((sp.Matrix([2,-1]).T*S*sp.Matrix([2,-1]))[0],3)
        self.assertEqual(similar.charpoly().as_expr(),S.charpoly().as_expr());self.assertNotEqual(D.charpoly().as_expr(),S.charpoly().as_expr())
        self.assertEqual(similar,B.inv()*S*B)

    def test_figures_de_niveau_conservent_q(self):
        for case in ('definie','indefinie','degenerate','isotrope'):
            result=m.calculate(dict(lab='quadratiques',case=case,shear=3))
            S=np.array(ce.parse_matrix(result['matrices'][0]['entries']),dtype=float)
            for curve in result['charts'][1]['series'][:-2]:
                points=np.array([curve['x'],curve['y']])
                values=np.einsum('ij,ij->j',points,S@points)
                np.testing.assert_allclose(values,1,atol=5e-13)


class ContratJSON(unittest.TestCase):
    def validate(self,result):
        json.dumps(result,allow_nan=False,ensure_ascii=False)
        for key in ('lab','parameters','metrics','charts','table','notes','theory','matrices','steps'):self.assertIn(key,result)
        for c in result['charts']:
            for s in c['series']:
                self.assertEqual(len(s['x']),len(s['y']))
                self.assertTrue(all(math.isfinite(v) for v in s['x']+s['y']))
                if c['logx']:self.assertTrue(all(v>0 for v in s['x']))
                if c['logy']:self.assertTrue(all(v>0 for v in s['y']))
            if 'grid' in c:
                grid=c['grid'];self.assertEqual(len(grid['z']),len(grid['y']))
                self.assertTrue(all(len(row)==len(grid['x']) for row in grid['z']))
                self.assertTrue(np.isfinite(np.array(grid['z'])).all())
        for b in result['matrices']:self.assertTrue(all(isinstance(v,str) for row in b['entries'] for v in row))

    def test_douze_labs_par_defaut(self):
        self.assertEqual(len(m.LABS),12)
        for lab in m.LABS:
            with self.subTest(lab=lab):self.validate(m.calculate({'lab':lab}))

    def test_cas_limites_et_controles(self):
        cases=[dict(lab='anneaux',ring='mod',matrix='0 0;0 0',modulus=30),
               dict(lab='lie',family='sp',a=0,b=0,time=-2,h=.02),
               dict(lab='lie',family='so',a=-2,b=2,time=2,h=.5),
               dict(lab='gauss',matrix='0 0;0 0',vector='0;0'),
               dict(lab='pfaffien',size='8',a=-3,b=3,scale=0),
               dict(lab='projecteurs',lambda1=-3,lambda2=-3,coupling=0),
               dict(lab='projecteurs',mode='oblique',shear=3),dict(lab='quadratiques',case='isotrope',shear=0)]
        for params in cases:
            with self.subTest(params=params):self.validate(m.calculate(params))
        for size in ('5','8.0',True,5):
            with self.assertRaises(ValueError):m.calculate(dict(lab='pfaffien',size=size))


if __name__=='__main__':unittest.main()
