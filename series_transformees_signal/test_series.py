"""Régressions analytiques des dix laboratoires de séries de fonctions."""
import json
import math
import unittest
import numpy as np
from catalogue_series import LABS
from commun import clean
from modeles_series import (calculate,boundary_norm,stable_tp99,
    arcsin_coefficients,binomial_coefficients,coefficient_log_ratio,
    poisson_scaled_sum,elliptic_ratio,sinh_integrand,dominated_integral,
    dominated_limit,dominated_kernel)


def values(lab):return {control['key']:control['value'] for control in lab['controls']}


class BoundaryLayerTests(unittest.TestCase):
    def test_exact_maximum_independent_of_the_plot(self):
        for n in [1,7,113,1000]:
            self.assertEqual(boundary_norm(n),.5)
            self.assertAlmostEqual(n*(1/n)/(1+(n*(1/n))**2),.5)

    def test_compact_norm_switches_at_the_stationary_point(self):
        self.assertEqual(boundary_norm(10,.05),.5)
        self.assertAlmostEqual(boundary_norm(10,.2),.4)
        self.assertLess(boundary_norm(1000,.2),.0051)

    def test_peak_remains_in_rendered_points(self):
        output=calculate('couche_limite',dict(n=1000,delta=.1))
        curve=output['charts'][0]['series'][-1]
        peak=int(np.argmax(curve['y']))
        self.assertAlmostEqual(curve['x'][peak],.001)
        self.assertAlmostEqual(curve['y'][peak],.5)


class ConcentrationTests(unittest.TestCase):
    def test_area_by_independent_antiderivative(self):
        for n in [1,10,300]:
            output=calculate('concentration',dict(n=n,x0=.3))
            area=output['metrics'][0]['value']
            self.assertAlmostEqual(area,1-(n+1)*math.exp(-n))

    def test_pointwise_limit_and_mass_limit_are_distinct(self):
        output=calculate('concentration',dict(n=300,x0=.3))
        self.assertGreater(output['metrics'][0]['value'],.99999)
        self.assertLess(output['metrics'][3]['value'],1e-30)

    def test_dilation_preserves_integrated_mass(self):
        # Gauss integrates the dilated density, rather than a narrow peak.
        points,weights=np.polynomial.legendre.leggauss(160)
        u=10*(points+1)
        area=10*np.dot(weights,u*np.exp(-u))
        self.assertAlmostEqual(area,1-21*math.exp(-20),places=12)


class OriginalTPTests(unittest.TestCase):
    def test_fourth_order_coefficient_at_very_small_arguments(self):
        xs=np.array([1e-8,1e-5,1e-3])
        scaled=stable_tp99(xs)/xs**4
        np.testing.assert_allclose(scaled,-np.ones(3)/3,rtol=2e-6)

    def test_stable_expression_agrees_away_from_cancellation(self):
        xs=np.array([-.3,1.,3.,6.])
        np.testing.assert_allclose(stable_tp99(xs),np.cos(xs)-1/np.sqrt(1+xs**2),rtol=1e-13)

    def test_uniform_majorant_is_valid_beyond_small_arguments(self):
        xs=np.linspace(-10,10,5001)
        self.assertTrue(np.all(np.abs(stable_tp99(xs)) <= 5*xs**4/12+1e-15))

    def test_sum_is_not_globally_its_fourth_order_coefficient(self):
        x=2.
        computed=sum(float(stable_tp99(np.array([x/n]))[0]) for n in range(1,1001))
        fourth=-math.pi**4*x**4/270
        self.assertGreater(abs(computed-fourth),1.)

    def test_tail_bound_against_an_independent_longer_sum(self):
        x=1.7;N=50
        finite_tail=sum(float(stable_tp99(np.array([x/n]))[0]) for n in range(N+1,4001))
        self.assertLess(abs(finite_tail),5*x**4/(36*N**3))


class PowerSeriesTests(unittest.TestCase):
    def test_geometric_remainder_and_differentiated_remainder(self):
        output=calculate('geometrie',dict(N=8,r=.9))
        x=.9
        exact=1/(1-x);partial=sum(x**k for k in range(9))
        self.assertAlmostEqual(exact-partial,output['metrics'][1]['value'])
        derivative=sum(k*x**(k-1) for k in range(1,9))
        self.assertAlmostEqual(1/(1-x)**2-derivative,output['metrics'][2]['value'])

    def test_arcsin_coefficients_have_the_closed_form(self):
        cs=arcsin_coefficients(25)
        expected=[4**k*math.factorial(k)**2/math.factorial(2*k+1) for k in range(25)]
        np.testing.assert_allclose(cs,expected,rtol=3e-15)

    def test_arcsin_polynomial_satisfies_the_expected_ode_defect(self):
        N=12;x=np.array([-.8,.1,.7]);cs=arcsin_coefficients(N)
        polynomial=sum(cs[k]*x**(2*k+1) for k in range(N))
        derivative=sum((2*k+1)*cs[k]*x**(2*k) for k in range(N))
        np.testing.assert_allclose((1-x*x)*derivative-x*polynomial-1,-2*N*cs[-1]*x**(2*N),atol=2e-15)

    def test_arcsin_tail_bound(self):
        output=calculate('arcsin_ex4',dict(N=15,r=.92))
        self.assertLess(output['metrics'][3]['value'],output['metrics'][2]['value'])

    def test_binomial_central_coefficients(self):
        cs=binomial_coefficients(.5,40)
        expected=[math.comb(2*n,n)/4**n for n in range(40)]
        np.testing.assert_allclose(cs,expected,rtol=2e-15)

    def test_binomial_negative_and_positive_half_integers(self):
        for p in range(-3,4):
            alpha=p+.5;u=.3
            cs=binomial_coefficients(alpha,90)
            self.assertAlmostEqual(np.polynomial.polynomial.polyval(u,cs),(1-u)**(-alpha),places=12)

    def test_binomial_bounds_at_difficult_boundary_parameters(self):
        for p in range(-3,4):
            for N in [8,30,100]:
                output=calculate('binomiale_ex10',dict(p=str(p),N=N,r=.95))
                self.assertLessEqual(output['metrics'][3]['value'],output['metrics'][2]['value']+1e-12)


class EntireAsymptoticTests(unittest.TestCase):
    def test_coefficient_computation_matches_definition(self):
        ns=np.array([2,3,10,20,100,700])
        logs=coefficient_log_ratio(ns)
        reference=ns.astype(float)**3*np.log1p(2/ns.astype(float)**2)-2*ns
        np.testing.assert_allclose(logs,reference,atol=2e-12)

    def test_coefficient_asymptotic(self):
        ns=np.array([1000.,10000.,100000.])
        np.testing.assert_allclose(ns*coefficient_log_ratio(ns),-2*np.ones(3),rtol=2e-6)

    def test_scaled_sum_against_positive_direct_sum(self):
        x=.7;expected=0.
        for n in range(2,100):
            expected+=math.exp(n**3*math.log1p(2/n**2)-math.lgamma(n+1)+n*math.log(x)-math.exp(2)*x)
        self.assertAlmostEqual(poisson_scaled_sum(x),expected,places=14)

    def test_growth_equivalent_and_truncation_before_the_peak(self):
        self.assertGreater(poisson_scaled_sum(60),.995)
        self.assertLess(poisson_scaled_sum(30,100),1e-15)
        self.assertLess(poisson_scaled_sum(60),1.)

    def test_logarithmic_normalization_survives_the_largest_input(self):
        output=calculate('asymptotique_ex5',dict(x=60,N=700))
        self.assertTrue(math.isfinite(output['metrics'][3]['value']))
        self.assertGreater(output['metrics'][3]['value'],440)


class EllipticPendulumTests(unittest.TestCase):
    def test_zero_amplitude_returns_the_small_oscillation_period(self):
        self.assertAlmostEqual(elliptic_ratio(0),1,places=14)

    def test_known_complete_elliptic_integral(self):
        # K(1/sqrt(2))=Γ(1/4)^2/(4sqrt(π)). Our I=2K.
        expected=math.gamma(.25)**2/(2*math.pi**1.5)
        self.assertAlmostEqual(elliptic_ratio(1/math.sqrt(2)),expected,places=12)

    def test_positive_series_increases_to_the_integral(self):
        exact=elliptic_ratio(.8)
        partials=[elliptic_ratio(.8,N) for N in [1,3,10,40]]
        self.assertTrue(all(a<b for a,b in zip(partials,partials[1:])))
        self.assertLess(partials[-1],exact+1e-13)
        self.assertAlmostEqual(partials[-1],exact,places=9)

    def test_walllis_series_first_coefficients(self):
        k=.2
        self.assertAlmostEqual(elliptic_ratio(k,3),1+k*k/4+9*k**4/64)

    def test_elliptic_remainder_bound(self):
        for degrees in [10,90,160]:
            for N in [1,10,60]:
                output=calculate('elliptique_pendule',dict(angle=degrees,N=N,length=1))
                ratio=output['metrics'][1]['value']
                bound=output['metrics'][5]['value']
                error=output['metrics'][3]['value']*ratio
                self.assertLessEqual(error,bound+2e-14)

    def test_length_scaling_and_nonlinear_trajectory(self):
        a=calculate('elliptique_pendule',dict(angle=120,N=25,length=1))
        b=calculate('elliptique_pendule',dict(angle=120,N=25,length=4))
        self.assertAlmostEqual(b['metrics'][2]['value'],2*a['metrics'][2]['value'])
        theta=a['scene']['theta'];amplitude=math.radians(120)
        self.assertAlmostEqual(theta[150],-amplitude,places=5)
        self.assertAlmostEqual(theta[300],amplitude,places=5)


class ImproperIntegralTests(unittest.TestCase):
    def test_endpoint_extension(self):
        self.assertEqual(sinh_integrand(np.array([0.]))[0],1.)
        self.assertAlmostEqual(sinh_integrand(np.array([1e-8]))[0],1,places=14)

    def test_improper_integral_by_independent_gauss_quadrature(self):
        points,weights=np.polynomial.legendre.leggauss(180)
        t=20*(points+1)
        integral=20*np.dot(weights,sinh_integrand(t))
        self.assertAlmostEqual(integral,math.pi**2/4,places=11)

    def test_remainder_enclosure_for_positive_modes(self):
        for N in [1,4,50,400]:
            output=calculate('integrale_sh_ex11',dict(N=N,T=8))
            exact=output['metrics'][2]['value'];lower=output['scene']['tail_lower'];upper=output['scene']['tail_upper']
            self.assertLess(lower,exact)
            self.assertLess(exact,upper)

    def test_area_is_not_the_finite_display_window(self):
        a=calculate('integrale_sh_ex11',dict(N=10,T=2))
        b=calculate('integrale_sh_ex11',dict(N=10,T=15))
        self.assertEqual(a['metrics'][1]['value'],b['metrics'][1]['value'])
        self.assertGreater(a['metrics'][4]['value'],b['metrics'][4]['value'])


class DominatedConvergenceTests(unittest.TestCase):
    def test_n_one_endpoint_is_defined(self):
        np.testing.assert_array_equal(dominated_kernel(np.array([0.,1.]),1),[1.,0.])

    def test_affine_integral_at_n_one(self):
        self.assertAlmostEqual(dominated_integral(1,'linear',3).real,2/3,places=13)

    def test_piecewise_signal_at_n_one(self):
        # ∫₀^.4(1−t)dt −.75∫_.4¹(1−t)dt = .32−.135.
        self.assertAlmostEqual(dominated_integral(1,'jump',3).real,.185,places=13)

    def test_limit_formula_against_independent_quadrature(self):
        for family in ['linear','jump','complex','oscillatory']:
            for omega in [1,8,30]:
                self.assertLess(abs(dominated_integral(None,family,omega)-dominated_limit(family,omega)),1e-13)

    def test_domination_and_quantitative_kernel_bound(self):
        t=np.linspace(0,1,5001)
        for n in [1,2,7,600]:
            kernel=dominated_kernel(t,n)
            self.assertTrue(np.all(kernel>=0));self.assertTrue(np.all(kernel<=1))
            self.assertTrue(np.all(np.exp(-t)-kernel>=-1e-15))
            if n>1:self.assertLess(np.max(np.exp(-t)-kernel),1/(2*(n-1)))

    def test_complex_integral_has_a_nonzero_imaginary_part(self):
        value=dominated_integral(30,'complex',8)
        self.assertGreater(abs(value.imag),.05)
        self.assertLess(abs(value-dominated_limit('complex',8)),.01)


class ExperienceContractTests(unittest.TestCase):
    def test_every_default_and_preset_is_finite_and_exportable(self):
        for lab in LABS:
            with self.subTest(lab=lab['id']):
                for p in [values(lab),*[{**values(lab),**preset['values']} for preset in lab['presets']]]:
                    output=clean(calculate(lab['id'],p))
                    json.dumps(output,ensure_ascii=False,allow_nan=False)
                    self.assertGreaterEqual(len(output['steps']),4)
                    for chart_ in output['charts']:
                        for curve in chart_['series']:
                            self.assertEqual(len(curve['x']),len(curve['y']))
                            self.assertLessEqual(len(curve['x']),650)


if __name__=='__main__':unittest.main()
