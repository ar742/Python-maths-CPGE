"""Identités, contre-exemple et majorations : contrôles indépendants des seules courbes."""
import json
import math
import unittest
import numpy as np
from commun import clean, integrate
from catalogue_theoremes import LABS
from modeles_theoremes import (COMPUTE, identified, frullani_kernel, concentration_envelope,
    exponential_moment_tail, gamma_log_moment, gamma_moment_tail_bound, digamma_trigamma)


def calculate(id_,**changes):
    item=next(item for item in LABS if item['id']==id_)
    p={control['key']:control['value'] for control in item['controls']}; p.update(changes)
    return COMPUTE[id_](p)


def metrics(output):
    return {m['label']:float(m['value']) for m in output['metrics']}


class FunctionalEquations(unittest.TestCase):
    def test_exact_additive_and_multiplicative_residuals(self):
        for a in [-2,-.3,0,1.7]:
            for id_,changes in [('cauchy_additive',dict(a=a,b=0)),('cauchy_multiplicative',dict(equation='log',a=a,b=0)),('cauchy_multiplicative',dict(equation='power',a=a,b=0))]:
                with self.subTest(id=id_,a=a,mode=changes.get('equation')):
                    output=calculate(id_,**changes); residue=np.asarray(output['scene']['z'])
                    self.assertLess(float(np.max(abs(residue))),2e-10)

    def test_additive_perturbation_detected_by_pi_over_two(self):
        output=calculate('cauchy_additive',a=1,b=.2)
        self.assertGreater(metrics(output)['Défaut maximal sur les couples testés'],.25)
        x=math.pi/2; f=lambda x:x+.2*math.sin(x)
        self.assertAlmostEqual(f(2*x)-2*f(x),-.4,places=13)

    def test_logarithmic_residual_has_predicted_sign(self):
        output=calculate('cauchy_multiplicative',equation='log',a=.7,b=.3)
        scene=output['scene']; u=np.asarray(scene['x']); v=np.asarray(scene['y']); U,V=np.meshgrid(u,v)
        np.testing.assert_allclose(scene['z'],.6*U*V,atol=3e-15,rtol=3e-14)

    def test_dalembert_exact_families_and_zero(self):
        for family in ['cos','cosh','zero']:
            with self.subTest(family=family):
                output=calculate('dalembert',family=family,k=1.2,b=0)
                self.assertLess(np.max(abs(np.asarray(output['scene']['z']))),2e-12)
                self.assertEqual(metrics(output)['f(0)'],0 if family=='zero' else 1)

    def test_dalembert_perturbation_keeps_parity_but_fails(self):
        output=calculate('dalembert',family='cos',k=1,b=.1)
        self.assertEqual(metrics(output)['f(0)'],1)
        self.assertGreater(metrics(output)['Défaut maximal de l’équation fonctionnelle'],.1)

    def test_identification_satisfies_equation_independently(self):
        x=np.array([-11,-3,-1,-.01,.001,.2,1,4,9])
        np.testing.assert_allclose(identified(x)+identified(-x)/x,x,rtol=2e-14,atol=2e-14)
        self.assertAlmostEqual(float(identified(1)),1)
        self.assertAlmostEqual(float(identified(-1)),0)

    def test_even_odd_decomposition_and_limit(self):
        x=np.linspace(.001,5,301)
        np.testing.assert_allclose((identified(x)+identified(-x))/2,x*x/(1+x*x),rtol=3e-14,atol=3e-14)
        np.testing.assert_allclose((identified(x)-identified(-x))/2,x**3/(1+x*x),rtol=3e-14,atol=3e-14)
        self.assertLess(float(identified(1e-8)),2e-16)

    def test_identification_perturbed_residual_near_zero(self):
        x=1e-7; b=.2; f=lambda t:identified(t)+b*math.sin(t)
        self.assertAlmostEqual(float(f(x)+f(-x)/x-x),-b,places=6)


class ContinuityTheorem(unittest.TestCase):
    def test_gaussian_fourier_value_and_certified_error(self):
        for a in [0,2,-4,6]:
            for L in [2,4,6]:
                with self.subTest(a=a,L=L):
                    m=metrics(calculate('continuite_gauss',a=a,L=L))
                    self.assertAlmostEqual(m['Valeur sur ℝ'],math.sqrt(math.pi)*math.exp(-a*a/4),places=13)
                    self.assertLessEqual(m['Erreur absolue constatée'],m['Borne totale : queues + trapèzes']+2e-14)

    def test_gaussian_global_envelope_really_dominates(self):
        out=calculate('continuite_gauss',a=5.7,L=6)
        curves=out['scene']['curves']; f=np.asarray(curves[0]['y']); envelope=np.asarray(curves[1]['y'])
        self.assertTrue(np.all(abs(f)<=envelope+2e-16))

    def test_concentration_has_nonzero_mass_and_pointwise_limit(self):
        t=.2; widths=[.1,.01,.001]
        heights=[math.exp(-t/a)/a for a in widths]
        self.assertLess(heights[-1],1e-70)
        for a in widths:
            m=metrics(calculate('continuite_defaut',a=a))
            self.assertEqual(m['F(a) pour a>0'],1)
            self.assertEqual(m['F(0)'],0)
            self.assertEqual(m['Différence ∫|fₐ−f₀|'],1)

    def test_fixed_relative_window_captures_fixed_mass(self):
        for a in [.01,.05,.3]:
            m=metrics(calculate('continuite_defaut',a=a,epsilon=a))
            self.assertAlmostEqual(m['Masse dans [0,ε]'],1-math.exp(-1),places=14)

    def test_family_envelope_is_attained_and_is_not_integrable(self):
        t=np.array([.001,.01,.4,1,2,5])
        optimal=np.minimum(t,1); attained=np.exp(-t/optimal)/optimal
        np.testing.assert_allclose(concentration_envelope(t),attained,rtol=2e-14)
        # Chaque décennie proche de 0 ajoute la même aire à l'enveloppe 1/(et).
        u=np.linspace(-10,-1,10001); transformed=np.exp(u)*concentration_envelope(np.exp(u))
        self.assertAlmostEqual(float(integrate(transformed,u)),9/math.e,places=10)

    def test_concentration_local_envelope_controls_neighbourhood(self):
        a=.13; t=np.linspace(.001,5,801); envelope=2/a*np.exp(-t/(2*a))
        for alpha in np.linspace(a/2,2*a,13):
            self.assertTrue(np.all(np.exp(-t/alpha)/alpha<=envelope*(1+1e-14)))


class LeibnizTheorem(unittest.TestCase):
    def test_frullani_value_asymmetry_and_diagonal(self):
        for a,b in [(1,2),(2,1),(.25,.5),(4,4)]:
            m=metrics(calculate('leibniz_frullani',a=a,b=b,L=32))
            self.assertLessEqual(abs(m['F(a,b) calculé jusqu’à L']-math.log(b/a)),m['Borne absolue de la queue de F']+3e-13)
        self.assertAlmostEqual(metrics(calculate('leibniz_frullani',a=1,b=2,L=32))['F(a,b) calculé jusqu’à L'],-metrics(calculate('leibniz_frullani',a=2,b=1,L=32))['F(a,b) calculé jusqu’à L'],places=13)

    def test_compensated_kernel_is_stable_at_zero(self):
        t=np.array([0,1e-17,1e-12,1e-8])
        for a,b in [(1,2),(2,1),(4,4)]:
            v=frullani_kernel(a,b,t)
            self.assertTrue(np.all(np.isfinite(v)))
            np.testing.assert_allclose(v[:3],b-a,atol=3e-12,rtol=3e-12)

    def test_frullani_parametric_derivative_with_finite_difference(self):
        a,b=1.3,2.2; h=1e-4
        plus=metrics(calculate('leibniz_frullani',a=a+h,b=b,L=32))['F(a,b) calculé jusqu’à L']
        minus=metrics(calculate('leibniz_frullani',a=a-h,b=b,L=32))['F(a,b) calculé jusqu’à L']
        self.assertAlmostEqual((plus-minus)/(2*h),-1/a,places=7)

    def test_frullani_envelope_for_derivative(self):
        a=.25; t=np.linspace(0,32,601); m=a/2
        for alpha in [a/2,a,1.5*a]:
            self.assertTrue(np.all(np.exp(-alpha*t)<=np.exp(-m*t)*(1+1e-15)))

    def test_arctangent_values_and_both_tail_bounds(self):
        for a in [.2,.8,3]:
            for L in [6,24,48]:
                with self.subTest(a=a,L=L):
                    m=metrics(calculate('leibniz_arctan',a=a,L=L))
                    self.assertLessEqual(abs(m['F(a) calculé jusqu’à L']-math.atan(1/a)),m['Borne absolue de la queue de F']+2e-12)
                    self.assertLessEqual(abs(m['F′(a) calculé jusqu’à L']+1/(1+a*a)),m['Borne de la queue de F′']+2e-12)

    def test_arctangent_equation_differential(self):
        h=1e-4; a=1.2
        plus=metrics(calculate('leibniz_arctan',a=a+h,L=48))['F(a) calculé jusqu’à L']
        minus=metrics(calculate('leibniz_arctan',a=a-h,L=48))['F(a) calculé jusqu’à L']
        self.assertAlmostEqual((plus-minus)/(2*h),-1/(1+a*a),places=7)


class HigherDerivativeTheorem(unittest.TestCase):
    def test_gamma_zero_moment_against_standard_gamma(self):
        for a in [.6,1,2,2.3,5]:
            U=8*math.log(10); T=50; val=gamma_log_moment(a,0,U,T)
            bound=gamma_moment_tail_bound(a,0,U,T)
            self.assertLessEqual(abs(val-math.gamma(a)),bound+1e-11)

    def test_gamma_log_moments_by_independent_psi_and_variance(self):
        for a in [.6,1,2.5,5]:
            U=30; T=60; moments=[gamma_log_moment(a,k,U,T) for k in range(3)]
            psi,var=digamma_trigamma(a)
            self.assertAlmostEqual(moments[1]/moments[0],psi,places=5)
            self.assertAlmostEqual(moments[2]/moments[0]-(moments[1]/moments[0])**2,var,places=4)

    def test_gamma_first_derivative_with_standard_library_difference(self):
        a=2.3; h=1e-4; expected=(math.gamma(a+h)-math.gamma(a-h))/(2*h)
        value=gamma_log_moment(a,1,25,50)
        self.assertAlmostEqual(value,expected,places=7)

    def test_gamma_derivative_recurrence(self):
        a=1.3; U=28; T=60
        g0=gamma_log_moment(a,0,U,T); g1=gamma_log_moment(a,1,U,T); g2=gamma_log_moment(a,2,U,T)
        self.assertAlmostEqual(gamma_log_moment(a+1,1,U,T),g0+a*g1,places=9)
        self.assertAlmostEqual(gamma_log_moment(a+1,2,U,T),2*g1+a*g2,places=8)

    def test_gamma_higher_moment_queues_against_wider_integral(self):
        for a,n,U,T in [(.6,5,3*math.log(10),12),(2.5,3,6*math.log(10),26),(5,5,8*math.log(10),30)]:
            value=gamma_log_moment(a,n,U,T); wider=gamma_log_moment(a,n,70,100,768)
            self.assertLessEqual(abs(value-wider),gamma_moment_tail_bound(a,n,U,T)+1e-7)

    def test_gamma_common_envelope_for_all_orders_and_local_parameters(self):
        a=1.7; n=5; output=calculate('derivees_gamma',a=a,n=n,q=6,T=30)
        scene=output['scene']; u=np.asarray(scene['x']); envelope=np.asarray(scene['curves'][1]['y'])
        for alpha in [a/2,a,a+1]:
            for k in range(n+1):
                integrand=np.exp(alpha*u-np.exp(u))*abs(u)**k
                self.assertTrue(np.all(integrand<=envelope*(1+2e-14)))

    def test_trigamma_is_positive_and_satisfies_shift(self):
        for a in [.6,1,3.2,5]:
            psi,var=digamma_trigamma(a); next_psi,next_var=digamma_trigamma(a+1)
            self.assertGreater(var,0)
            self.assertAlmostEqual(next_psi-psi,1/a,places=12)
            self.assertAlmostEqual(var-next_var,1/a**2,places=12)

    def test_laplace_factorial_value_and_captured_mass(self):
        for a,n,L in [(1,4,24),(.25,8,12),(.25,8,48),(3,1,4)]:
            m=metrics(calculate('derivees_laplace',a=a,n=n,L=L))
            total=math.factorial(n)/a**(n+1)
            self.assertAlmostEqual(m['F⁽ⁿ⁾(a) exact']/total,(-1)**n)
            self.assertAlmostEqual((abs(m['F⁽ⁿ⁾(a) calculé jusqu’à L'])+m['Masse absolue après L'])/total,1,places=11)
            self.assertGreaterEqual(m['Fraction de masse capturée'],0)
            self.assertLessEqual(m['Fraction de masse capturée'],1+2e-13)

    def test_laplace_exact_tail_for_first_moment(self):
        for L in [.2,4,24]:
            self.assertAlmostEqual(exponential_moment_tail(1,1,L),math.exp(-L)*(1+L),places=13)

    def test_laplace_tail_recurrence(self):
        for a,n,L in [(.3,3,4),(2,7,5)]:
            left=exponential_moment_tail(a,n,L)
            right=math.exp(-a*L)*L**n/a+n/a*exponential_moment_tail(a,n-1,L)
            self.assertAlmostEqual(left/right,1,places=13)

    def test_laplace_common_envelope_for_all_orders(self):
        a=.25; n=8; output=calculate('derivees_laplace',a=a,n=n,L=48)
        scene=output['scene']; t=np.asarray(scene['x']); envelope=np.asarray(scene['curves'][1]['y'])
        for alpha in [a/2,a,3*a/2]:
            for k in range(n+1):
                self.assertTrue(np.all(t**k*np.exp(-alpha*t)<=envelope*(1+2e-14)))

    def test_laplace_maximum_location_analytically(self):
        a,n=.4,7; maximum=n/a; f=lambda t:t**n*math.exp(-a*t)
        self.assertGreater(f(maximum),f(maximum-.5))
        self.assertGreater(f(maximum),f(maximum+.5))


class OutputContracts(unittest.TestCase):
    def test_all_default_presets_and_control_bounds_are_finite(self):
        for item in LABS:
            defaults={c['key']:c['value'] for c in item['controls']}
            cases=[defaults]+[dict(defaults,**pr['values']) for pr in item['presets']]
            for control in item['controls']:
                values=[control['min'],control['max']] if control['type']=='range' else [o['value'] for o in control['options']]
                cases += [dict(defaults,**{control['key']:value}) for value in values]
            for params in cases:
                with self.subTest(id=item['id'],params=params):
                    output=COMPUTE[item['id']](params)
                    json.dumps(clean(output),allow_nan=False)
                    self.assertGreaterEqual(len(output['charts']),2)
                    self.assertTrue(output['scene']['title'])
                    self.assertTrue(output['scene']['description'])
                    self.assertGreaterEqual(len(output['steps']),4)


if __name__=='__main__':
    unittest.main()
