"""Références indépendantes, erreurs du recueil, limites et contrat du serveur."""
import json
import math
import threading
import unittest
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import numpy as np
from mathematiques import (coordinates,coordinate_jacobian,central_jacobian,
    ellipse_integral,ellipse_quadrature,smooth,smooth_derivatives,cubic,
    cubic_derivatives,pathology,determinant_derivative,inverse_derivative,
    rayleigh_value_gradient,matrix_exp,lie_project,bracket,gaussian,
    gaussian_mass_quadrature,fubini_rectangle,green_boundary,calculate,LABS)
from cours import LESSONS,EXERCISES
from calcul_differentiel import make_server


class CoordinatesTests(unittest.TestCase):
    def test_polar_and_cylindrical_orientation(self):
        self.assertAlmostEqual(np.linalg.det(coordinate_jacobian([2,.4],"polaire")),2)
        self.assertAlmostEqual(np.linalg.det(coordinate_jacobian([2,.4,-1],"cylindrique")),2)

    def test_spherical_order_and_metric(self):
        q=[2,.4,1.2];J=coordinate_jacobian(q,"spherique")
        self.assertAlmostEqual(np.linalg.det(J),-4*math.sin(1.2))
        np.testing.assert_allclose(J.T@J,np.diag([1,4*math.sin(1.2)**2,4]),atol=1e-14)

    def test_coordinate_derivatives_by_centered_differences(self):
        for mode,q in [("polaire",[1.7,.4]),("cylindrique",[1.7,.4,2]),("spherique",[1.7,.4,.9])]:
            np.testing.assert_allclose(coordinate_jacobian(q,mode),central_jacobian(lambda x:coordinates(x,mode),q),atol=1e-9)

    def test_singular_charts_still_have_finite_outputs(self):
        for params in [dict(r=0),dict(phi=0),dict(phi=180)]:
            result=calculate(dict(lab="jacobiennes",**params))
            self.assertFalse(result["theory"]["regular"])
            self.assertAlmostEqual(result["theory"]["determinant"],0,places=12)
            json.dumps(result,allow_nan=False)


class IntegralTests(unittest.TestCase):
    def test_corrected_tp_exact_value(self):
        self.assertAlmostEqual(ellipse_integral(3,2),324/5-3*math.pi/2,places=13)

    def test_independent_cartesian_integration(self):
        # Integrate analytically in y, then Gauss in x. Different coordinates.
        nodes,w=np.polynomial.legendre.leggauss(512)
        for a,b,alpha,beta in [(3,2,3,1),(.7,2.1,1.3,4)]:
            x=a*(nodes+1)/2;ymax=b*np.sqrt(1-(x/a)**2)
            numerical=float(np.sum(w*(alpha*x**3*ymax-beta*ymax**3/3))*a/2)
            self.assertAlmostEqual(numerical,ellipse_integral(a,b,alpha,beta),delta=2e-6)

    def test_transformed_quadrature_and_zero_integrand(self):
        self.assertAlmostEqual(ellipse_quadrature(3,2,3,1,16),ellipse_integral(3,2),places=11)
        self.assertEqual(ellipse_quadrature(2,1,0,0,4),0)
        self.assertNotAlmostEqual(ellipse_quadrature(3,2,3,1,16,False),ellipse_integral(3,2))


class DifferentialTests(unittest.TestCase):
    def test_gradient_and_hessian_independent_fd(self):
        x=np.array([.3,-.4])
        for f,df in [(smooth,smooth_derivatives),(cubic,cubic_derivatives)]:
            g,H=df(x)
            np.testing.assert_allclose(central_jacobian(lambda v:np.array([f(v)]),x)[0],g,atol=1e-9)
            np.testing.assert_allclose(central_jacobian(lambda v:df(v)[0],x),H,atol=1e-8)

    def test_cubic_corrected_saddles(self):
        for x,det in [(np.array([-2.,-2.]),-72),(np.array([2/3,-2/3]),-24)]:
            g,H=cubic_derivatives(x)
            np.testing.assert_allclose(g,0,atol=1e-14)
            self.assertAlmostEqual(np.linalg.det(H),det)
            self.assertEqual(calculate(dict(lab="taylor",mode="cubique",x=x[0],y=x[1]))["theory"]["classification"],"Selle")

    def test_degenerate_origin_is_not_an_extremum(self):
        np.testing.assert_array_equal(cubic_derivatives([0,0])[1],np.diag([-6,0]))
        self.assertLess(cubic([0,-.1]),0);self.assertGreater(cubic([0,.1]),0)

    def test_directional_derivatives_do_not_imply_continuity(self):
        for u in [np.array([1.,0]),np.array([0.,1]),np.array([2.,-3]),np.array([1.,1])]:
            self.assertLess(abs(pathology(1e-7*u)/1e-7),1e-5)
        for t in [.1,.01,.001]:self.assertAlmostEqual(pathology([t,t**3]),.5)

    def test_cubic_taylor_remainder_exact(self):
        x=np.array([.4,-.2]);u=np.array([.7,.9]);g,H=cubic_derivatives(x)
        third=cubic(u)+3*u[0]**2 # homogeneous degree-three part
        for t in [.1,-.2]:
            remainder=cubic(x+t*u)-cubic(x)-t*g@u-.5*t*t*(u@H@u)
            self.assertAlmostEqual(remainder,t**3*third,places=13)


class MatrixTests(unittest.TestCase):
    def test_inverse_derivative_noncommuting_case(self):
        A=np.array([[2.,1],[0,3]]);H=np.array([[.2,1],[-.5,.7]])
        eps=1e-5;fd=(np.linalg.inv(A+eps*H)-np.linalg.inv(A-eps*H))/(2*eps)
        np.testing.assert_allclose(inverse_derivative(A,H),fd,atol=1e-10)
        self.assertGreater(np.linalg.norm(inverse_derivative(A,H)+np.linalg.matrix_power(np.linalg.inv(A),2)@H),.01)

    def test_determinant_derivative_singular_dimensions(self):
        for n in [2,3,4]:
            A=np.diag([1.]*(n-1)+[0.]);H=np.eye(n)*.7
            self.assertAlmostEqual(determinant_derivative(A,H),.7)

    def test_determinant_jacobi_identity(self):
        A=np.array([[2.,.2,.1],[0,3,.4],[.1,-.2,1]]);H=np.arange(9).reshape(3,3)/10
        self.assertAlmostEqual(determinant_derivative(A,H),np.linalg.det(A)*np.trace(np.linalg.solve(A,H)),places=12)
        eps=1e-5
        self.assertAlmostEqual(determinant_derivative(A,H),(np.linalg.det(A+eps*H)-np.linalg.det(A-eps*H))/(2*eps),delta=1e-8)

    def test_determinant_2d_exact_remainder(self):
        A=np.array([[1.,.4],[-.5,2]]);H=np.array([[.3,1],[-.7,.2]])
        for t in [.2,-.4]:
            self.assertAlmostEqual(np.linalg.det(A+t*H)-np.linalg.det(A)-t*determinant_derivative(A,H),t*t*np.linalg.det(H),places=13)

    def test_singular_matrix_lab(self):
        result=calculate(dict(lab="matrices",a=1,b=0,c=0,d=0))
        self.assertIsNone(result["theory"]["inverse_derivative"])
        self.assertAlmostEqual(result["theory"]["det_derivative"],.2)


class OptimisationTests(unittest.TestCase):
    def test_rayleigh_bounds_and_stationary_vectors(self):
        A=np.array([[3.,1],[1,3]])
        for x in [np.array([1.,1]),np.array([1.,-1])]:
            val,g=rayleigh_value_gradient(A,x)
            np.testing.assert_allclose(g,0,atol=1e-15);self.assertIn(val,[2,4])
        for t in np.linspace(0,6,30):
            val,_=rayleigh_value_gradient(A,np.array([math.cos(t),math.sin(t)]))
            self.assertGreaterEqual(val,2-1e-14);self.assertLessEqual(val,4+1e-14)

    def test_rayleigh_nonsymmetric_uses_symmetric_part(self):
        A=np.array([[2.,4],[-1,3]]);x=np.array([.4,.7]);v,g=rayleigh_value_gradient(A,x)
        np.testing.assert_allclose(g,central_jacobian(lambda y:np.array([rayleigh_value_gradient(A,y)[0]]),x)[0],atol=1e-8)
        self.assertAlmostEqual(v,rayleigh_value_gradient((A+A.T)/2,x)[0])
        with self.assertRaises(ValueError):rayleigh_value_gradient(A,np.zeros(2))

    def test_rayleigh_second_order_exact(self):
        A=np.diag([1.,4])
        for t in [.1,.001]:
            v,_=rayleigh_value_gradient(A,np.array([math.cos(t),math.sin(t)]))
            self.assertAlmostEqual(v-1,3*math.sin(t)**2,places=14)

    def test_gradient_descent_matches_spectral_solution(self):
        r=calculate(dict(lab="optimisation",rotation=0,lambda1=1,lambda2=4,x=-1.5,y=2,steps=20,factor=.8))["theory"]
        star=np.array([1.,-.125]);e0=np.array([-1.5,2])-star
        for k,x in enumerate(r["path"]):
            np.testing.assert_allclose(x,star+np.array([.8**k,.2**k])*e0,atol=2e-15)

    def test_newton_and_excessive_step(self):
        stable=calculate(dict(lab="optimisation"))["theory"]
        np.testing.assert_allclose(stable["newton"],stable["minimum"],atol=1e-14)
        unstable=calculate(dict(lab="optimisation",factor=2.5,steps=30))["theory"]
        self.assertGreater(unstable["costs"][-1],unstable["costs"][0]*1000)


class LieTests(unittest.TestCase):
    def test_exponential_diagonal_and_nilpotent(self):
        np.testing.assert_allclose(matrix_exp(np.diag([.4,-2,3])),np.diag(np.exp([.4,-2,3])),atol=1e-13)
        N=np.array([[0.,2,0],[0,0,3],[0,0,0]])
        np.testing.assert_allclose(matrix_exp(N),np.eye(3)+N+N@N/2,atol=1e-14)

    def test_rotation_against_rodrigues(self):
        X=np.array([[0.,-.7,.4],[.7,0,-1],[-.4,1,0]]);omega=math.sqrt(-np.trace(X@X)/2)
        for t in [-2,.3,1.5]:
            ref=np.eye(3)+math.sin(t*omega)/omega*X+(1-math.cos(t*omega))/omega**2*(X@X)
            np.testing.assert_allclose(matrix_exp(t*X),ref,atol=8e-15)

    def test_group_constraints_and_liouville(self):
        raw=np.array([[.4,1,.2],[-.5,.6,.7],[.3,.1,-.2]])
        for group in ["GL","SL","SO"]:
            X=lie_project(raw,group);E=matrix_exp(1.7*X)
            self.assertAlmostEqual(np.linalg.det(E),math.exp(1.7*np.trace(X)),places=12)
            if group=="SL":self.assertAlmostEqual(np.linalg.det(E),1)
            if group=="SO":np.testing.assert_allclose(E.T@E,np.eye(3),atol=4e-15)

    def test_commutator_leading_term(self):
        X=np.array([[0.,1,0],[-1,0,0],[0,0,0]]);Y=np.array([[0.,0,0],[0,0,1],[0,-1,0]])
        s=.001;C=matrix_exp(s*X)@matrix_exp(s*Y)@matrix_exp(-s*X)@matrix_exp(-s*Y)
        np.testing.assert_allclose((C-np.eye(3))/s**2,bracket(X,Y),atol=.001)

    def test_bracket_closure_and_jacobi(self):
        X=lie_project(np.arange(9).reshape(3,3),"SO");Y=lie_project(np.eye(3,k=1),"SO");Z=lie_project(np.eye(3,k=-2),"SO")
        C=bracket(X,Y);np.testing.assert_allclose(C+C.T,0,atol=1e-15)
        self.assertEqual(np.trace(C),0)
        np.testing.assert_allclose(bracket(X,bracket(Y,Z))+bracket(Y,bracket(Z,X))+bracket(Z,bracket(X,Y)),0,atol=1e-14)

    def test_so2_is_abelian(self):
        r=calculate(dict(lab="lie",n=2,group="SO"))["theory"]
        np.testing.assert_allclose(r["bracket"],0,atol=0)


class GaussianTests(unittest.TestCase):
    def test_diagonal_extended_gaussian(self):
        g=gaussian(np.diag([2.,3]),np.array([2.,-3]))
        self.assertAlmostEqual(g["integral"],2*math.pi/math.sqrt(6)*math.exp(2.5),places=12)
        np.testing.assert_allclose(g["mean"],[1,-1]);np.testing.assert_allclose(g["covariance"],np.diag([.5,1/3]))

    def test_orthogonal_invariance(self):
        Q=np.array([[.6,-.8],[.8,.6]]);A=np.diag([.7,2.]);B=np.array([.4,-.8])
        self.assertAlmostEqual(gaussian(A,B)["integral"],gaussian(Q@A@Q.T,Q@B)["integral"],places=12)

    def test_derivatives_in_B_and_A(self):
        A=np.array([[2.,.4],[.4,1.2]]);B=np.array([.8,-.3]);H=np.array([[.3,.2],[.2,-.1]]);g=gaussian(A,B);eps=1e-5
        fd=central_jacobian(lambda v:np.array([gaussian(A,v)["log_integral"]]),B)[0]
        np.testing.assert_allclose(fd,g["gradient_B"],atol=1e-10)
        fdH=central_jacobian(lambda v:gaussian(A,v)["gradient_B"],B)
        np.testing.assert_allclose(fdH,g["hessian_B"],atol=1e-10)
        fdA=(gaussian(A+eps*H,B)["log_integral"]-gaussian(A-eps*H,B)["log_integral"])/(2*eps)
        self.assertAlmostEqual(fdA,float(np.sum(g["gradient_A"]*H)),delta=1e-10)

    def test_moments_by_independent_normalized_quadrature(self):
        A=np.array([[1.5,.3],[.3,.8]]);B=np.array([.6,-.2]);g=gaussian(A,B)
        nodes,w=np.polynomial.legendre.leggauss(96);x=nodes*9;y=nodes*9
        X,Y=np.meshgrid(x,y,indexing="ij");p=np.stack([X,Y],axis=-1)
        exponent=-.5*np.einsum("...i,ij,...j->...",p,A,p)+p@B
        weights=np.exp(exponent-g["log_integral"])*w[:,None]*w[None,:]*81
        self.assertAlmostEqual(float(weights.sum()),1,delta=1e-11)
        mean=np.einsum("ij,ijk->k",weights,p)
        second=np.einsum("ij,ijk,ijl->kl",weights,p,p)
        np.testing.assert_allclose(mean,g["mean"],atol=1e-10)
        np.testing.assert_allclose(second,g["covariance"]+np.outer(mean,mean),atol=1e-9)

    def test_positive_determinant_is_not_enough(self):
        for A in [np.diag([-1.,-1]),np.diag([1.,0]),np.array([[1.,1],[0,1]])]:
            with self.assertRaises(ValueError):gaussian(A,np.zeros(2))

    def test_truncation_bound_is_separate_from_quadrature(self):
        mass=gaussian_mass_quadrature(np.diag([.7,2.]),np.array([1.,-.5]),64)
        exact_mass=math.erf(6/math.sqrt(2))**2
        self.assertAlmostEqual(mass,exact_mass,places=13)
        self.assertLessEqual(1-exact_mass,2*math.erfc(6/math.sqrt(2)))


class GreenFubiniTests(unittest.TestCase):
    def test_green_boundary_and_independent_area_integral(self):
        self.assertAlmostEqual(green_boundary(),-13/60,places=14)
        x,w=np.polynomial.legendre.leggauss(16);x=(x+1)/2
        area_integral=float(-np.sum((x*x-x**4+x*(x-x*x))*w)/2)
        self.assertAlmostEqual(area_integral,-13/60,places=14)
        self.assertAlmostEqual(calculate(dict(lab="green_fubini",orientation=-1))["theory"]["exact"],13/60)

    def test_symmetric_fubini_cutoff(self):
        for q in [1,.1,.001,1e-6]:self.assertAlmostEqual(fubini_rectangle(q,q),0,places=14)

    def test_asymmetric_cutoff_limits(self):
        q=1e-8
        self.assertAlmostEqual(fubini_rectangle(math.sqrt(q),q),math.pi/4,delta=3e-4)
        self.assertAlmostEqual(fubini_rectangle(q*q,q),-math.pi/4,delta=3e-8)

    def test_rectangle_against_direct_quadrature(self):
        ex,ey=.2,.1;nodes,w=np.polynomial.legendre.leggauss(96)
        x=ex+(nodes+1)*(1-ex)/2;y=ey+(nodes+1)*(1-ey)/2
        X,Y=np.meshgrid(x,y,indexing="ij")
        integral=float(np.sum((X*X-Y*Y)/(X*X+Y*Y)**2*w[:,None]*w[None,:])*(1-ex)*(1-ey)/4)
        self.assertAlmostEqual(integral,fubini_rectangle(ex,ey),places=12)


class ContractTests(unittest.TestCase):
    def test_all_labs_and_exercises_finite_json(self):
        for lab in LABS:json.dumps(calculate(dict(lab=lab)),allow_nan=False)
        for e in EXERCISES:json.dumps(calculate(dict(lab=e["lab"],**e["params"])),allow_nan=False)

    def test_extreme_parameters_remain_finite(self):
        for d in [dict(lab="lie",group="GL",a=2,b=2,c=-2,t=2),dict(lab="gaussienne",n=8,lambda1=.2,lambda2=.2,gamma=.2,b1=3,b2=3),dict(lab="optimisation",lambda1=.2,lambda2=10,factor=2.5,steps=50),dict(lab="elliptique",alpha=0,beta=0),dict(lab="optimisation",mode="rayleigh",lambda1=1,lambda2=1)]:
            json.dumps(calculate(d),allow_nan=False)

    def test_invalid_parameters(self):
        for d in [dict(r=float("nan")),dict(r=True),dict(lab="inconnu"),dict(phi=181),dict(lab="lie",n=2.5),dict(lab="gaussienne",lambda1=0),dict(lab="green_fubini",orientation=0),dict(lab="elliptique",order=100000)]:
            with self.assertRaises(ValueError):calculate(d)


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=make_server(0);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.url=f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown();cls.server.server_close();cls.thread.join(timeout=2)

    def request(self,path="/",payload=None,headers=None):
        h={"Content-Type":"application/json","X-Differentiel-Token":self.server.api_token};h.update(headers or {})
        return urlopen(Request(self.url+path,data=payload,headers=h),timeout=10)

    def test_bootstrap(self):
        with self.request("/api/bootstrap") as r:data=json.load(r)
        self.assertEqual(data["application"],"calcul-differentiel")
        self.assertEqual(len(data["lessons"]),14);self.assertEqual(len(data["exercises"]),18)

    def test_static_assets(self):
        for path in ["/","/app.js","/style.css","/favicon.svg"]:
            with self.request(path) as r:
                self.assertGreater(len(r.read()),100);self.assertIn("script-src 'self'",r.headers["Content-Security-Policy"])

    def test_valid_api(self):
        with self.request("/api",b'{"lab":"elliptique"}') as r:data=json.load(r)
        self.assertAlmostEqual(data["theory"]["exact"],324/5-3*math.pi/2)

    def test_token_host_origin(self):
        for h in [{"X-Differentiel-Token":""},{"Host":"example.org"},{"Origin":"https://example.org"}]:
            with self.assertRaises(HTTPError) as cm:self.request("/api",b"{}",h)
            self.assertEqual(cm.exception.code,403)

    def test_bad_json(self):
        for payload in [b"{",b"[]",b'{"r":NaN}',b'{"r":9}']:
            with self.assertRaises(HTTPError) as cm:self.request("/api",payload)
            self.assertEqual(cm.exception.code,400)

    def test_snapshot_download_and_expiry(self):
        with self.request("/api",b'{"lab":"gaussienne"}') as r:data=json.load(r)
        with self.request("/api/export/"+data["export_id"]) as r:
            self.assertIn("attachment;",r.headers["Content-Disposition"]);self.assertEqual(json.load(r),data)
        for _ in range(4):
            with self.request("/api",b'{"lab":"elliptique"}') as r:json.load(r)
        with self.assertRaises(HTTPError) as cm:self.request("/api/export/"+data["export_id"])
        self.assertEqual(cm.exception.code,404)

    def test_private_files_not_served(self):
        for path in ["/cours.py","/../README.md","/COURS.md"]:
            with self.assertRaises(HTTPError) as cm:self.request(path)
            self.assertEqual(cm.exception.code,404)


if __name__=="__main__":unittest.main()
