"""Identités indépendantes : ODE, intégrales, Parseval et convergence."""
import json
import math
import unittest
import numpy as np
from catalogue_transformees import LABS
from commun import integrate
from modeles_transformees import (calculate, rc_response, rc_transfer, rlc_response,
                                 porte_convolution, fourier_coefficients,
                                 periodic_wave, fourier_sum)


class TestContratsTransformees(unittest.TestCase):
    def defaults(self, laboratory):
        return {c['key']: c['value'] for c in laboratory['controls']}

    def check_result(self, out):
        json.dumps(out, allow_nan=False)
        self.assertGreaterEqual(len(out['steps']), 4)
        self.assertGreaterEqual(len(out['charts']), 2)
        for c in out['charts']:
            for s in c['series']:
                self.assertEqual(len(s['x']), len(s['y']))
                self.assertLessEqual(len(s['x']), 650)
                self.assertTrue(np.all(np.isfinite(s['x'])))
                self.assertTrue(np.all(np.isfinite(s['y'])))

    def test_ten_distinct_laboratories(self):
        self.assertEqual(len(LABS), 10)
        self.assertEqual(len({l['id'] for l in LABS}), 10)

    def test_defaults_and_presets(self):
        for laboratory in LABS:
            for values in [self.defaults(laboratory)] + [self.defaults(laboratory) | item['values'] for item in laboratory['presets']]:
                with self.subTest(id=laboratory['id'], values=values):
                    self.check_result(calculate(laboratory['id'], values))

    def test_parameter_extremes(self):
        for laboratory in LABS:
            for end in ('min', 'max'):
                p = self.defaults(laboratory)
                for c in laboratory['controls']:
                    if c['type'] == 'range': p[c['key']] = c[end]
                with self.subTest(id=laboratory['id'], end=end):
                    self.check_result(calculate(laboratory['id'], p))

    def test_select_choices(self):
        for laboratory in LABS:
            for c in laboratory['controls']:
                if c['type'] == 'select':
                    for item in c['options']:
                        with self.subTest(id=laboratory['id'], choice=item['value']):
                            p = self.defaults(laboratory); p[c['key']] = item['value']
                            self.check_result(calculate(laboratory['id'], p))


class TestLaplace(unittest.TestCase):
    def test_rc_ramp_is_solution_of_ode_and_initial_condition(self):
        tau, a, b, y0 = 1.3, .7, -.4, 1.2
        t = np.linspace(.1, 8., 200)
        derivative = (rc_response(t + 1e-5, tau, 'ramp', a=a, b=b, y0=y0)
                      - rc_response(t - 1e-5, tau, 'ramp', a=a, b=b, y0=y0)) / 2e-5
        np.testing.assert_allclose(tau * derivative + rc_response(t, tau, 'ramp', a=a, b=b, y0=y0), a * t + b, atol=2e-10)
        self.assertAlmostEqual(float(rc_response(0., tau, 'ramp', a=a, b=b, y0=y0)), y0, places=14)

    def test_rc_step_is_solution_of_ode(self):
        tau, A, y0 = .7, 1.8, -.3
        t = np.linspace(.1, 5., 200); h = 1e-5
        y = rc_response(t, tau, 'step', amplitude=A, y0=y0)
        yp = (rc_response(t+h, tau, 'step', amplitude=A, y0=y0)-rc_response(t-h, tau, 'step', amplitude=A, y0=y0))/(2*h)
        np.testing.assert_allclose(tau * yp + y, A, atol=2e-10)

    def test_rc_impulse_jump_and_area(self):
        tau, A = .4, 1.7
        self.assertAlmostEqual(float(rc_response(0., tau, 'impulse', amplitude=A, y0=.6)), A / tau + .6)
        t = np.linspace(0., 20. * tau, 50001)
        self.assertAlmostEqual(float(integrate(rc_response(t, tau, 'impulse', amplitude=A), t)), A, delta=3e-8)

    def test_rc_transfer_cutoff_and_phase(self):
        tau = 1.3; cutoff = 1. / (2. * math.pi * tau); H = complex(rc_transfer(cutoff, tau))
        self.assertAlmostEqual(abs(H), 1. / math.sqrt(2.))
        self.assertAlmostEqual(math.atan2(H.imag, H.real), -math.pi / 4.)

    def test_rc_laplace_against_quadrature_for_ramp(self):
        tau, a, b, y0, p = .8, .7, .4, .6, 1.1
        t = np.linspace(0., 50., 200001)
        Y = float(integrate(rc_response(t, tau, 'ramp', a=a, b=b, y0=y0)*np.exp(-p*t), t))
        expected = (a / p ** 2 + b / p + tau * y0) / (1. + tau * p)
        self.assertAlmostEqual(Y, expected, delta=1e-8)

    def test_rlc_step_is_integral_of_impulse_all_regimes(self):
        w = 3.7
        for zeta in [.1, .7, 1., 1.3, 2.]:
            with self.subTest(zeta=zeta):
                t = np.linspace(.01, 8., 500); h = 2e-6
                derivative = (rlc_response(t+h, w, zeta, 'step')-rlc_response(t-h, w, zeta, 'step'))/(2*h)
                np.testing.assert_allclose(derivative, rlc_response(t, w, zeta, 'impulse'), atol=2e-10)

    def test_rlc_homogeneous_ode_and_initial_data(self):
        w, h = 4., 2e-4
        for zeta in [.2, 1., 1.8]:
            with self.subTest(zeta=zeta):
                t = np.linspace(.05, 4., 100)
                ym2, ym, y, yp, yp2 = [rlc_response(t+shift, w, zeta, 'impulse') for shift in [-2*h,-h,0.,h,2*h]]
                second = (-yp2+16*yp-30*y+16*ym-ym2)/(12*h**2)
                first = (-yp2+8*yp-8*ym+ym2)/(12*h)
                np.testing.assert_allclose(second + 2*zeta*w*first + w*w*y, 0., atol=2e-7)
                self.assertAlmostEqual(float(rlc_response(0., w, zeta, 'impulse')), 0., places=12)
                values = [float(rlc_response(shift, w, zeta, 'impulse')) for shift in [-2*h,-h,h,2*h]]
                first0 = (-values[3]+8*values[2]-8*values[1]+values[0])/(12*h)
                self.assertAlmostEqual(first0, w*w, delta=1e-8)

    def test_rlc_critical_limit(self):
        t = np.linspace(0., 3., 400)
        for mode in ['step', 'impulse']:
            critical = rlc_response(t, 3., 1., mode)
            for zeta in [1.-1e-7, 1.+1e-7]:
                np.testing.assert_allclose(rlc_response(t, 3., zeta, mode), critical, atol=3e-7)

    def test_rlc_under_damped_exact_overshoot(self):
        w, zeta = 6., .35; t_peak = math.pi/(w*math.sqrt(1-zeta*zeta))
        y_peak = float(rlc_response(t_peak, w, zeta, 'step'))
        self.assertAlmostEqual(y_peak-1., math.exp(-math.pi*zeta/math.sqrt(1-zeta*zeta)), places=14)

    def test_dirichlet_abel_value_and_derivative(self):
        for p in [.1, .6, 2.]:
            with self.subTest(p=p):
                t = np.linspace(0., 200., 100001)
                numerical = float(integrate(np.sinc(t/math.pi)*np.exp(-p*t), t))
                exact = math.atan(1./p)
                self.assertAlmostEqual(numerical, exact, delta=7e-7)
                h = 1e-5
                derivative = (math.atan(1./(p+h))-math.atan(1./(p-h)))/(2*h)
                self.assertAlmostEqual(derivative, -1./(1+p*p), places=8)

    def test_dirichlet_tail_bound_covers_truncation(self):
        for p,L in [(.02,20.),(.04,80.),(.2,40.)]:
            with self.subTest(p=p,L=L):
                t = np.linspace(0., L, 100001)
                num = float(integrate(np.sinc(t/math.pi)*np.exp(-p*t), t))
                self.assertLessEqual(abs(math.atan(1./p)-num),2*math.exp(-p*L)/L+1e-8)


class TestFourierContinu(unittest.TestCase):
    def test_porte_transform_from_complex_integral(self):
        L, center = 1.7, -.6
        t = np.linspace(center-L/2,center+L/2,60001)
        for frequency in [0., .2, 1./L, 1.6]:
            with self.subTest(frequency=frequency):
                num = complex(integrate(np.exp(-2j*math.pi*frequency*t),t))
                expected = L*np.sinc(L*frequency)*np.exp(-2j*math.pi*frequency*center)
                self.assertAlmostEqual(abs(num-expected),0.,delta=3e-9)

    def test_porte_translation_changes_phase_not_modulus(self):
        f = np.linspace(-3.,3.,601); L = .7
        a = L*np.sinc(L*f); b = a*np.exp(-2j*math.pi*f*1.3)
        np.testing.assert_allclose(abs(a),abs(b),atol=2e-16)

    def test_gaussian_transform_direct_integral(self):
        sigma, A = .7, 1.4; t = np.linspace(-8*sigma,8*sigma,40001)
        for frequency in [0., .3, 1.]:
            with self.subTest(frequency=frequency):
                num = complex(integrate(A*np.exp(-t*t/(2*sigma*sigma))*np.exp(-2j*math.pi*frequency*t),t))
                expected = A*sigma*math.sqrt(2*math.pi)*math.exp(-2*math.pi**2*sigma**2*frequency**2)
                self.assertAlmostEqual(abs(num-expected),0.,delta=1e-13)

    def test_gaussian_parseval_and_energy_variances(self):
        for sigma in [.1,.6,2.]:
            with self.subTest(sigma=sigma):
                t = np.linspace(-8*sigma,8*sigma,50001)
                frequency = np.linspace(-8/(2*math.pi*sigma),8/(2*math.pi*sigma),50001)
                f2 = np.exp(-t*t/sigma**2)
                F2 = 2*math.pi*sigma**2*np.exp(-4*math.pi**2*sigma**2*frequency**2)
                E1, E2 = float(integrate(f2,t)),float(integrate(F2,frequency))
                self.assertAlmostEqual(E1,E2,places=13)
                vt = float(integrate(t*t*f2,t))/E1; vf = float(integrate(frequency**2*F2,frequency))/E2
                self.assertAlmostEqual(vt,sigma**2/2,places=13)
                self.assertAlmostEqual(vf,1/(8*math.pi**2*sigma**2),places=11)
                self.assertAlmostEqual(math.sqrt(vt*vf),1/(4*math.pi),places=13)

    def test_convolution_matches_overlap_quadrature(self):
        L1,L2,d = 1.1,1.8,.4; u = np.linspace(-L1/2,L1/2,60001)
        for t in [-2.,-.3,.4,1.,2.]:
            with self.subTest(t=t):
                numerical = float(integrate((np.abs(t-u-d)<=L2/2).astype(float),u))
                self.assertAlmostEqual(numerical,float(porte_convolution(t,L1,L2,d)),delta=3e-5)

    def test_convolution_support_height_and_area(self):
        for L1,L2 in [(1.,1.),(.6,2.),(3.,.2)]:
            with self.subTest(widths=(L1,L2)):
                d=.5; t = np.linspace(d-(L1+L2)/2,d+(L1+L2)/2,50001)
                y = porte_convolution(t,L1,L2,d)
                self.assertAlmostEqual(float(max(y)),min(L1,L2),places=12)
                self.assertAlmostEqual(float(integrate(y,t)),L1*L2,delta=1e-8)
                self.assertEqual(float(porte_convolution(d+(L1+L2),L1,L2,d)),0.)

    def test_convolution_fourier_product(self):
        L1,L2,d=1.3,.7,-.4; t=np.linspace(d-(L1+L2)/2,d+(L1+L2)/2,60001)
        for f in [0.,.2,1.1]:
            with self.subTest(f=f):
                numerical=complex(integrate(porte_convolution(t,L1,L2,d)*np.exp(-2j*math.pi*f*t),t))
                expected=L1*L2*np.sinc(L1*f)*np.sinc(L2*f)*np.exp(-2j*math.pi*f*d)
                self.assertAlmostEqual(abs(numerical-expected),0.,delta=2e-9)


class TestSeriesHarmoniques(unittest.TestCase):
    def test_coefficients_against_defining_integral(self):
        # Midpoints avoid sampling the convention at isolated discontinuities.
        theta=-math.pi+(np.arange(200000)+.5)*(2*math.pi/200000)
        for wave in ['square','triangle','sawtooth']:
            values=periodic_wave(theta,wave); n,a,b,dc,_=fourier_coefficients(wave,7)
            self.assertAlmostEqual(float(np.mean(values)),dc,places=10)
            for k,ak,bk in zip(n,a,b):
                self.assertAlmostEqual(float(2*np.mean(values*np.cos(k*theta))),ak,delta=1e-9)
                self.assertAlmostEqual(float(2*np.mean(values*np.sin(k*theta))),bk,delta=1e-9)

    def test_direct_mean_square_of_normalized_signals(self):
        theta=-math.pi+(np.arange(200000)+.5)*(2*math.pi/200000)
        for wave,expected in [('square',1.),('triangle',1/3),('sawtooth',1/3)]:
            self.assertAlmostEqual(float(np.mean(periodic_wave(theta,wave)**2)),expected,delta=1e-10)

    def test_fejer_equals_cesaro_average(self):
        theta=np.linspace(-math.pi,math.pi,41); N=13
        for wave in ['square','triangle','sawtooth']:
            dc=fourier_coefficients(wave,N)[3]
            cesaro=(dc+sum(fourier_sum(theta,wave,k) for k in range(1,N+1)))/(N+1)
            np.testing.assert_allclose(fourier_sum(theta,wave,N,fejer=True),cesaro,atol=3e-15)

    def test_fejer_stays_in_range(self):
        theta=np.linspace(-math.pi,math.pi,2001)
        for wave,lo,hi in [('square',-1.,1.),('triangle',0.,1.),('sawtooth',-1.,1.)]:
            for N in [1,10,55]:
                with self.subTest(wave=wave,N=N):
                    y=fourier_sum(theta,wave,N,fejer=True)
                    self.assertGreaterEqual(float(min(y)),lo-1e-14)
                    self.assertLessEqual(float(max(y)),hi+1e-14)

    def test_parseval_projection_residual_matches_time_integral(self):
        theta=-math.pi+(np.arange(160000)+.5)*(2*math.pi/160000); N=12
        for wave in ['square','triangle','sawtooth']:
            n,a,b,dc,energy=fourier_coefficients(wave,N)
            exact=energy-dc*dc-.5*float(np.sum(a*a+b*b))
            numerical=float(np.mean((periodic_wave(theta,wave)-fourier_sum(theta,wave,N))**2))
            self.assertAlmostEqual(numerical,exact,delta=2e-9)

    def test_fejer_error_requires_coefficient_penalty(self):
        theta=-math.pi+(np.arange(160000)+.5)*(2*math.pi/160000); N=12
        for wave in ['square','triangle','sawtooth']:
            n,a,b,dc,energy=fourier_coefficients(wave,N); power=.5*(a*a+b*b)
            exact=energy-dc*dc-float(np.sum(power))+float(np.sum((n/(N+1))**2*power))
            numerical=float(np.mean((periodic_wave(theta,wave)-fourier_sum(theta,wave,N,fejer=True))**2))
            self.assertAlmostEqual(numerical,exact,delta=2e-9)

    def test_gibbs_exact_first_peak_converges_to_constant(self):
        N=1999; theta=math.pi/(N+1)
        peak=float(fourier_sum(np.array([theta]),'square',N)[0]); ratio=(peak-1)/2
        self.assertAlmostEqual(ratio,.089489872236,delta=5e-8)

    def test_jump_midpoint_values(self):
        for N in [1,20,120]:
            self.assertAlmostEqual(float(fourier_sum(np.array([0.]),'square',N)[0]),0.,places=13)
            self.assertAlmostEqual(float(fourier_sum(np.array([math.pi]),'sawtooth',N)[0]),0.,places=13)

    def test_triangle_uniform_tail_at_zero(self):
        for N in [1,12,119]:
            theta=np.linspace(-math.pi,math.pi,1201)
            err=np.abs(periodic_wave(theta,'triangle')-fourier_sum(theta,'triangle',N))
            at_zero=float(fourier_sum(np.array([0.]),'triangle',N)[0])
            self.assertAlmostEqual(float(np.max(err)),at_zero,places=12)
            self.assertLessEqual(at_zero,4/(math.pi**2*N))

    def test_poisson_kernel_series_mass_and_remainder(self):
        theta=np.linspace(-math.pi,math.pi,60001)
        for r,N in [(.2,10),(.75,20),(.97,70)]:
            with self.subTest(r=r,N=N):
                exact=(1-r*r)/(1-2*r*np.cos(theta)+r*r)
                self.assertAlmostEqual(float(integrate(exact,theta)),2*math.pi,delta=1e-11)
                n=np.arange(1,N+1); partial=1+(2*r**n)@np.cos(n[:,None]*theta[None,:])
                bound=2*r**(N+1)/(1-r)
                self.assertAlmostEqual(float(max(abs(exact-partial))),bound,delta=8e-12)

    def test_poisson_lissage_exact_matches_harmonic_sum(self):
        theta=np.linspace(-math.pi,math.pi,501)
        for r in [0.,.5,.9]:
            exact=2/math.pi*np.arctan2(2*r*np.sin(theta),np.full_like(theta,1-r*r))
            approximate=fourier_sum(theta,'square',350,abel=r)
            np.testing.assert_allclose(approximate,exact,atol=3e-15)

    def test_classical_sums_from_parseval(self):
        n=np.arange(1,100001,dtype=float); odd=n[np.remainder(n,2)==1]
        self.assertAlmostEqual(float(np.sum(1/n**2)),math.pi**2/6,delta=1.1e-5)
        self.assertAlmostEqual(float(np.sum(1/n**4)),math.pi**4/90,delta=1e-14)
        self.assertAlmostEqual(float(np.sum(1/odd**4)),math.pi**4/96,delta=1e-14)


if __name__ == '__main__':
    unittest.main()
