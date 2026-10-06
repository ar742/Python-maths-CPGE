"""Invariants et expériences indépendantes : Markov et Laplaciens."""
from itertools import combinations
import json
import unittest
import numpy as np
import sympy as sp
import applications as a


def tree_sum_by_enumeration(n,edges):
    total=sp.S.Zero
    for selected in combinations(edges,n-1):
        parent=list(range(n))
        def root(i):
            while parent[i]!=i:i=parent[i]
            return i
        weight=sp.S.One
        for i,j,w in selected:
            x,y=root(i),root(j)
            if x==y:break
            parent[x]=y;weight*=w
        else:
            if len({root(i) for i in range(n)})==1:total+=weight
    return total


class MarkovTests(unittest.TestCase):
    def test_column_protocol_and_probabilities(self):
        for bridge,bias,eta in [(0,0,0),(sp.Rational(1,4),sp.Rational(3,5),sp.Rational(1,20)),(2,-sp.Rational(4,5),sp.Rational(3,10))]:
            M,_=a.markov_matrix(bridge,bias,eta)
            self.assertTrue(all(v>=0 for v in M))
            self.assertEqual([sum(M[:,j]) for j in range(6)],[1]*6)
            p=M*sp.eye(6)[:,0]
            self.assertEqual(p,M[:,0])
            self.assertEqual(sum(p),1)

    def test_reversible_irregular_graph_stationary_degree_formula(self):
        b=sp.Rational(1,4)
        M,W=a.markov_matrix(b,0,0)
        degrees=sp.Matrix([sum(W[i,:]) for i in range(6)])
        pi=degrees/sum(degrees)
        self.assertEqual(pi,sp.Matrix([sp.Rational(4,25),sp.Rational(4,25),sp.Rational(9,50),sp.Rational(9,50),sp.Rational(4,25),sp.Rational(4,25)]))
        self.assertEqual(M*pi,pi)
        self.assertNotEqual(M,M.T)
        F=M*sp.diag(*pi)
        self.assertEqual(F,F.T)
        result=a.markov(dict(bias=0,teleport=0))
        self.assertTrue(result["theory"]["reversible"])

    def test_stationarity_does_not_imply_reversibility(self):
        result=a.markov({})
        self.assertTrue(result["theory"]["exact_stationarity"])
        self.assertFalse(result["theory"]["reversible"])
        M,_=a.markov_matrix()
        clockwise=M[1,0]*M[2,1]*M[0,2]
        reverse=M[2,0]*M[1,2]*M[0,1]
        self.assertNotEqual(clockwise,reverse)

    def test_closed_classes_limit_depends_on_initial_mass(self):
        result=a.markov(dict(bridge=0,teleport=0,initial="gauche",steps=20))
        self.assertEqual(result["theory"]["stationary_dimension"],2)
        self.assertEqual(result["theory"]["spectral_gap"],0)
        self.assertEqual(result["theory"]["limiting_law"],["1/3"]*3+["0"]*3)
        self.assertEqual(result["theory"]["stationary"],["1/6"]*6)
        self.assertLess(result["theory"]["total_variation"],1e-14)

    def test_teleport_reconnects_the_two_closed_classes(self):
        result=a.markov(dict(bridge=0,teleport=.1,steps=100))
        self.assertEqual(result["theory"]["stationary_dimension"],1)
        self.assertEqual(result["theory"]["stationary"],["1/6"]*6)
        self.assertLess(result["theory"]["total_variation"],2e-5)

    def test_initial_stationary_is_fixed(self):
        result=a.markov(dict(initial="stationnaire",steps=100))
        self.assertLess(result["theory"]["total_variation"],2e-14)

    def test_iteration_against_independent_exact_power(self):
        M,_=a.markov_matrix()
        expected=np.array(M**8*sp.eye(6)[:,0],dtype=float).ravel()
        result=a.markov(dict(steps=8))
        np.testing.assert_allclose(result["theory"]["final_law"],expected,atol=1e-14,rtol=0)
        self.assertAlmostEqual(sum(result["theory"]["final_law"]),1)
        tv=np.array(result["charts"][2]["series"][0]["y"])
        self.assertTrue(np.all(np.diff(tv)<=1e-14))

    def test_manual_probability_and_invalid_probability(self):
        result=a.markov(dict(initial="manuel",p0="1/2;0;0;1/2;0;0"))
        self.assertEqual(result["theory"]["initial"],["1/2","0","0","1/2","0","0"])
        for vector in ["1;1;0;0;0;0","-1;2;0;0;0;0","1;0;0", "sin(0);1;0;0;0;0"]:
            with self.subTest(vector=vector),self.assertRaises(ValueError):a.markov(dict(initial="manuel",p0=vector))


class NetworkTests(unittest.TestCase):
    def test_laplacian_by_neighbor_formula_not_incidence(self):
        for n in [6,8]:
            L,B,W,edges=a.clique_bridge(n,sp.Rational(2,5))
            independent=sp.zeros(n)
            for i,j,w in edges:
                independent[i,i]+=w;independent[j,j]+=w
                independent[i,j]-=w;independent[j,i]-=w
            self.assertEqual(L,independent)
            self.assertEqual(L,L.T)
            self.assertEqual(L*sp.ones(n,1),sp.zeros(n,1))
            self.assertEqual(L,B*W*B.T)

    def test_orientation_does_not_change_L(self):
        L,B,W,_=a.clique_bridge()
        changed=B.copy()
        for j in range(0,B.cols,2):changed[:,j]=-changed[:,j]
        self.assertEqual(L,changed*W*changed.T)

    def test_kernel_dimension_and_constant_vectors(self):
        for n in [6,8]:
            half=n//2
            L,*_=a.clique_bridge(n,0)
            self.assertEqual(n-L.rank(),2)
            for v in [sp.Matrix([1]*half+[0]*half),sp.Matrix([0]*half+[1]*half)]:
                self.assertEqual(L*v,sp.zeros(n,1))
            connected,*_=a.clique_bridge(n,sp.Rational(1,10))
            self.assertEqual(n-connected.rank(),1)

    def test_weighted_Kirchhoff_by_tree_enumeration(self):
        for n in [6,8]:
            b=sp.Rational(2,5)
            L,_,_,edges=a.clique_bridge(n,b)
            expected=tree_sum_by_enumeration(n,edges)
            self.assertEqual(L[:-1,:-1].det(),expected)
            self.assertEqual(expected,b*(n//2)**(n-4))
            for deleted in [0,n//2,n-1]:
                minor=L.copy();minor.row_del(deleted);minor.col_del(deleted)
                self.assertEqual(minor.det(),expected)

    def test_Dirichlet_energy_and_nonnegativity(self):
        L,_,_,edges=a.clique_bridge(8,sp.Rational(3,10))
        x=sp.Matrix([1,-2,0,sp.Rational(1,3),4,1,-1,2])
        energy=(x.T*L*x)[0]
        expected=sum(w*(x[i]-x[j])**2 for i,j,w in edges)
        self.assertEqual(energy,expected)
        self.assertGreater(energy,0)

    def test_Fiedler_closed_formula_against_independent_eigh(self):
        for n in [6,8]:
            for b in [0,.000001,.2,1,2]:
                result=a.reseaux(dict(size=n,bridge=b))
                L,*_=a.clique_bridge(n,sp.Rational(str(b)))
                eigen=np.linalg.eigvalsh(np.array(L,dtype=float))
                self.assertAlmostEqual(result["theory"]["lambda2"],eigen[1],places=12)
                self.assertLess(result["theory"]["fiedler_residual"],1e-12)
                self.assertLessEqual(result["theory"]["lambda2"],4*b/n+1e-12)

    def test_heat_diffusion_conserves_mass_and_dissipates_energy(self):
        for bridge in [0,.2,2]:
            result=a.reseaux(dict(bridge=bridge,time=8,signal="impulsion"))
            self.assertAlmostEqual(result["theory"]["mass_final"],1,places=12)
            energy=np.array(result["charts"][2]["series"][0]["y"])
            self.assertTrue(np.all(np.diff(energy)<=1e-12))
            self.assertTrue(np.all(np.array(result["theory"]["signal_final"])>=-1e-13))
        disconnected=a.reseaux(dict(bridge=0,signal="contraste",time=8))
        np.testing.assert_allclose(disconnected["theory"]["signal_final"],[1]*4+[-1]*4,atol=1e-12)

    def test_manual_signal_has_eight_rational_coordinates(self):
        result=a.reseaux(dict(signal="manuel",values="1/2;0;0;0;0;0;0;-1/2"))
        self.assertEqual(result["theory"]["mass_initial"],"0")
        self.assertEqual(len(result["theory"]["signal_initial"]),8)


class ContractTests(unittest.TestCase):
    def test_scenes_pedagogy_and_strict_JSON(self):
        for data in [dict(lab="markov"),dict(lab="markov",bridge=0,teleport=0),dict(lab="reseaux"),dict(lab="reseaux",size="6",bridge=0)]:
            result=a.calculate_lab(data)
            json.dumps(result,allow_nan=False)
            self.assertTrue(result["scenes"])
            self.assertTrue(result["pedagogy"]["reading"])
            self.assertTrue(result["pedagogy"]["proof"])
            for scene in result["scenes"]:
                ids={node["id"] for node in scene["nodes"]}
                self.assertEqual(len(ids),len(scene["nodes"]))
                self.assertTrue(all(edge["source"] in ids and edge["target"] in ids for edge in scene["edges"]))
                for frame in scene.get("frames",[]):self.assertEqual(len(frame["values"]),len(ids))

    def test_validation(self):
        for data in [dict(lab="missing"),dict(lab="markov",steps=0),dict(lab="markov",bias=1),dict(lab="reseaux",size=7),dict(lab="reseaux",bridge=-1),dict(lab="reseaux",time=9)]:
            with self.subTest(data=data),self.assertRaises(ValueError):a.calculate_lab(data)


if __name__=="__main__":unittest.main()
