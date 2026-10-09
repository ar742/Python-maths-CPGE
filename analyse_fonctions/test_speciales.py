"""Contrôles indépendants : identités, équations et extrêmes des paramètres."""
import json
import itertools
import math
import unittest
import numpy as np
from commun import clean, integrate
from catalogue_speciales import LABS
from contenu_speciales import LESSONS, EXERCISES, GUIDES
from modeles_speciales import (
    COMPUTE, beta_quadrature, beta_value, gamma_quadrature, zeta_value,
    planck_quadrature, power_integral, fractional_quadrature,
    pulse_integral, bell_partial, faa_value, hermite, hermite_function, gauss_integral
)


def defaults(id_):
    item = next(lab for lab in LABS if lab['id'] == id_)
    return {c['key']: c['value'] for c in item['controls']}


def calculate(id_, **changes):
    p = defaults(id_)
    p.update(changes)
    return COMPUTE[id_](p)


def metrics(out):
    return {m['label']: m['value'] for m in out['metrics']}


class GammaBeta(unittest.TestCase):
    def test_gamma_integer_integral_independent_of_gamma_library(self):
        for n in [1, 2, 5, 8]:
            T = 12
            tail = math.factorial(n - 1) * math.exp(-T) * sum(T ** k / math.factorial(k) for k in range(n))
            expected = math.factorial(n - 1) - tail
            self.assertAlmostEqual(gamma_quadrature(n, T), expected, delta=1e-10 * max(1, expected))

    def test_gamma_half_matches_gaussian_integral(self):
        self.assertAlmostEqual(gamma_quadrature(.5, 45), math.sqrt(math.pi), delta=2e-11)

    def test_gamma_positive_domain_near_zero(self):
        for x in [.35, .7, 1.05, 2.3, 5.25]:
            self.assertAlmostEqual(gamma_quadrature(x, 45) / math.gamma(x), 1, delta=2e-10)

    def test_gamma_truncation_monotone(self):
        values = [gamma_quadrature(5, T) for T in [1, 4, 8, 16]]
        self.assertTrue(all(a < b for a, b in zip(values, values[1:])))
        self.assertLess(values[-1], math.factorial(4))

    def test_beta_uniform_normalisation(self):
        self.assertAlmostEqual(beta_quadrature(1, 1), 1, delta=2e-14)

    def test_beta_both_endpoint_singularities(self):
        self.assertAlmostEqual(beta_quadrature(.5, .5), math.pi, delta=1e-10)
        self.assertAlmostEqual(beta_quadrature(.35, .35) / beta_value(.35, .35), 1, delta=2e-10)

    def test_beta_integer_formula_independent(self):
        for a, b in [(2, 5), (4, 4), (7, 2)]:
            expected = math.factorial(a - 1) * math.factorial(b - 1) / math.factorial(a + b - 1)
            self.assertAlmostEqual(beta_quadrature(a, b), expected, delta=1e-13)

    def test_beta_symmetry_includes_reflection_of_density(self):
        one = calculate('beta_geometrie', a=2, b=5)
        two = calculate('beta_geometrie', a=5, b=2)
        np.testing.assert_allclose(one['charts'][0]['series'][0]['y'][::-1], two['charts'][0]['series'][0]['y'], atol=3e-14)
        self.assertAlmostEqual(beta_value(2, 5), beta_value(5, 2))

    def test_beta_moments_from_direct_polynomial_integrals(self):
        a, b = 2, 5
        x = np.linspace(0, 1, 20001)
        density = x ** (a - 1) * (1 - x) ** (b - 1) / beta_value(a, b)
        mean = integrate(x * density, x)
        variance = integrate((x - mean) ** 2 * density, x)
        m = metrics(calculate('beta_geometrie', a=a, b=b))
        self.assertAlmostEqual(m['Moyenne de la densité'], mean, delta=1e-8)
        self.assertAlmostEqual(m['Variance de la densité'], variance, delta=1e-8)


class Zeta(unittest.TestCase):
    def test_euler_maclaurin_basel_and_even_values(self):
        self.assertAlmostEqual(zeta_value(2), math.pi ** 2 / 6, delta=2e-14)
        self.assertAlmostEqual(zeta_value(4), math.pi ** 4 / 90, delta=2e-14)
        self.assertAlmostEqual(zeta_value(6), math.pi ** 6 / 945, delta=2e-14)

    def test_zeta_apery_constant_independent_reference(self):
        self.assertAlmostEqual(zeta_value(3), 1.2020569031595943, delta=2e-14)

    def test_integral_bounds_contain_zeta_at_all_slider_edges(self):
        for s in [1.1, 1.5, 2, 6]:
            for N in [20, 100, 4000]:
                out = metrics(calculate('zeta_series', s=s, N=N))
                remainder = out['ζ(s), référence Euler–Maclaurin'] - out['Somme des N premiers termes']
                self.assertLessEqual(out['Borne inférieure du reste'] - 2e-13, remainder)
                self.assertGreaterEqual(out['Borne supérieure du reste'] + 2e-13, remainder)

    def test_corrected_interval_shrinks_on_doubling(self):
        one = metrics(calculate('zeta_series', s=1.5, N=200))
        two = metrics(calculate('zeta_series', s=1.5, N=400))
        self.assertLess(two['Largeur de l’encadrement de ζ(s)'], one['Largeur de l’encadrement de ζ(s)'])

    def test_zeta_is_decreasing(self):
        values = [zeta_value(s) for s in [1.1, 1.2, 2, 3, 6]]
        self.assertTrue(all(a > b for a, b in zip(values, values[1:])))

    def test_planck_integral_at_even_value(self):
        self.assertAlmostEqual(planck_quadrature(4, 45), math.pi ** 4 / 15, delta=2e-11)
        self.assertAlmostEqual(planck_quadrature(2, 45), math.pi ** 2 / 6, delta=2e-11)

    def test_planck_integral_singular_origin_is_handled(self):
        for s in [1.15, 1.2, 1.5, 3.3, 6]:
            ratio = planck_quadrature(s, 45) / (math.gamma(s) * zeta_value(s))
            self.assertAlmostEqual(ratio, 1, delta=2e-9)

    def test_planck_truncation_increases(self):
        self.assertLess(planck_quadrature(6, 5), planck_quadrature(6, 10))
        self.assertLess(planck_quadrature(6, 10), planck_quadrature(6, 20))


class FractionalCalculus(unittest.TestCase):
    def test_ordinary_primitive_is_order_one(self):
        t = np.linspace(0, 3, 101)
        for q in [0, .5, 1, 4]:
            np.testing.assert_allclose(power_integral(t, q, 1), t ** (q + 1) / (q + 1), atol=1e-13, rtol=3e-14)

    def test_two_half_integrals_of_constant(self):
        value = fractional_quadrature(lambda u: 2 * np.sqrt(u) / math.sqrt(math.pi), 2, .5, n=512)
        self.assertAlmostEqual(value, 2, delta=3e-8)

    def test_composition_by_independent_quadrature(self):
        for q, alpha, beta in [(1, .5, .5), (2, .4, .7), (3, 1.4, .6)]:
            sequential = fractional_quadrature(lambda u: power_integral(u, q, beta), 1.7, alpha, n=512)
            direct = float(power_integral(1.7, q, alpha + beta))
            self.assertAlmostEqual(sequential, direct, delta=2e-8 * max(1, direct))

    def test_pulse_order_one_is_area_under_rectangular_signal(self):
        t = np.linspace(0, 4, 121)
        np.testing.assert_allclose(pulse_integral(t, 1, 1.3), np.minimum(t, 1.3), atol=1e-14)

    def test_pulse_keeps_memory_after_switch_off(self):
        out = calculate('integrale_fractionnaire', profile='pulse', a=1, alpha=.5)
        signal, response = out['charts'][0]['series'][:2]
        self.assertEqual(signal['y'][-1], 0)
        self.assertGreater(response['y'][-1], 0)
        self.assertAlmostEqual(response['y'][-1], 2 * (2 - math.sqrt(3)) / math.sqrt(math.pi))

    def test_pulse_tail_equivalent(self):
        t = 1e5
        actual = float(pulse_integral(t, .5, 1))
        self.assertAlmostEqual(actual * math.sqrt(math.pi * t), 1, delta=3e-6)

    def test_caputo_constant_vanishes_but_rl_does_not(self):
        out = calculate('derivees_fractionnaires', q=0, c=2, alpha=.5)
        rl, caputo = out['charts'][0]['series']
        self.assertTrue(np.all(rl['y'] > 0))
        np.testing.assert_array_equal(caputo['y'], np.zeros_like(caputo['y']))
        self.assertAlmostEqual(metrics(out)['Riemann–Liouville à t=1'], 3 / math.sqrt(math.pi))

    def test_rl_caputo_agree_when_initial_value_is_zero(self):
        out = calculate('derivees_fractionnaires', q=3, c=0, alpha=.7)
        rl, caputo = out['charts'][0]['series']
        np.testing.assert_allclose(rl['y'], caputo['y'], atol=2e-14)

    def test_history_functions_share_value_and_ordinary_slope(self):
        out = calculate('derivees_fractionnaires', memory=2)
        first, second = out['charts'][1]['series']
        self.assertEqual(first['y'][-1], second['y'][-1])
        # The endpoint derivative is checked analytically, independently of the grids.
        self.assertEqual(1 + 2 * (1 - 4 + 3), 1)
        self.assertNotAlmostEqual(out['charts'][2]['series'][0]['y'][-1], out['charts'][2]['series'][1]['y'][-1])

    def test_history_difference_has_exact_half_derivative_value(self):
        out = metrics(calculate('derivees_fractionnaires', alpha=.5, memory=1))
        self.assertAlmostEqual(out['Écart de Caputo entre les deux histoires à t=1'], -2 / (15 * math.sqrt(math.pi)), delta=2e-14)


class CompositionsHermite(unittest.TestCase):
    def test_bell_third_and_fourth_orders_known_formulas(self):
        B3 = bell_partial([2.0, 3.0, 5.0], 3)
        self.assertAlmostEqual(float(B3[1]), 5)
        self.assertAlmostEqual(float(B3[2]), 3 * 2 * 3)
        self.assertAlmostEqual(float(B3[3]), 2 ** 3)
        B4 = bell_partial([2.0, 3.0, 5.0, 7.0], 4)
        self.assertAlmostEqual(float(B4[2]), 4 * 2 * 5 + 3 * 3 ** 2)

    def test_faa_inverse_matches_independent_leibniz_recurrence(self):
        x, a, b = .37, .3, .6
        g, gp, gpp = 1 + a * x + b * x * x, a + 2 * b * x, 2 * b
        h = [1 / g]
        for n in range(1, 9):
            value = n * gp * h[n - 1]
            if n >= 2:
                value += math.comb(n, 2) * gpp * h[n - 2]
            h.append(-value / g)
            self.assertAlmostEqual(float(faa_value(x, a, b, n, 'inverse')), h[n], delta=2e-11 * max(1, abs(h[n])))

    def test_faa_exp_quadratic_at_origin_matches_taylor_series(self):
        for n in range(1, 9):
            expected = 0 if n % 2 else math.e * math.factorial(n) * .5 ** (n // 2) / math.factorial(n // 2)
            self.assertAlmostEqual(float(faa_value(0, 0, .5, n, 'exp')), expected, delta=1e-10)

    def test_faa_table_coefficients_at_order_four(self):
        table = calculate('faa_di_bruno', n=4)['table']
        self.assertEqual([row[3] for row in table['rows']], [1, 6, 3])

    def test_hermite_matches_explicit_rodrigues_polynomial(self):
        x = np.linspace(-2, 2, 33)
        for n in range(13):
            explicit = sum(math.factorial(n) * (-1) ** j * (2 * x) ** (n - 2 * j) / (math.factorial(j) * math.factorial(n - 2 * j)) for j in range(n // 2 + 1))
            np.testing.assert_allclose(hermite(n, x), explicit, rtol=2e-12, atol=2e-7)

    def test_hermite_derivative_and_ode_by_polynomial_coefficients(self):
        from numpy.polynomial import Polynomial
        for n in [2, 5, 8]:
            coef = np.zeros(n + 1)
            for j in range(n // 2 + 1):
                coef[n - 2 * j] = math.factorial(n) * (-1) ** j * 2 ** (n - 2 * j) / (math.factorial(j) * math.factorial(n - 2 * j))
            H = Polynomial(coef)
            residual = H.deriv(2) - Polynomial([0, 2]) * H.deriv() + 2 * n * H
            np.testing.assert_allclose(residual.coef, 0, atol=1e-10)

    def test_hermite_parity_and_origin(self):
        x = np.linspace(.1, 2, 25)
        for n in range(13):
            np.testing.assert_allclose(hermite(n, -x), (-1) ** n * hermite(n, x), atol=2e-9)
            expected = 0 if n % 2 else (-1) ** (n // 2) * math.factorial(n) / math.factorial(n // 2)
            self.assertAlmostEqual(float(hermite(n, 0)), expected)

    def test_normalised_hermite_orthogonality_same_and_opposite_parity(self):
        for n, m in [(0, 0), (4, 4), (12, 12), (4, 5), (6, 8)]:
            value = gauss_integral(lambda x: hermite_function(n, x) * hermite_function(m, x), -11, 11, 384)
            self.assertAlmostEqual(value, 1 if n == m else 0, delta=3e-12)

    def test_hermite_roots_are_real_and_annul_polynomial(self):
        out = calculate('hermite_gauss', n=12)
        roots = np.array([row[1] for row in out['table']['rows']])
        self.assertEqual(len(roots), 12)
        self.assertTrue(np.all(np.diff(roots) > 0))
        # Relative scale matters for a polynomial with a large leading coefficient.
        self.assertLess(np.max(np.abs(hermite(12, roots))) / math.factorial(12), 2e-10)


class Contracts(unittest.TestCase):
    def test_simultaneous_control_corners_are_finite(self):
        for lab in LABS:
            keys = [c['key'] for c in lab['controls']]
            edges = [[c['min'], c['max']] if c['type'] == 'range' else [option['value'] for option in c['options']] for c in lab['controls']]
            for values in itertools.product(*edges):
                with self.subTest(lab=lab['id'], values=values):
                    json.dumps(clean(COMPUTE[lab['id']](dict(zip(keys, values)))), allow_nan=False)

    def test_every_preset_and_single_slider_extreme_is_finite_json(self):
        for lab in LABS:
            base = defaults(lab['id'])
            choices = [base, *[{**base, **pre['values']} for pre in lab['presets']]]
            for control in lab['controls']:
                if control['type'] == 'range':
                    choices.extend([{**base, control['key']: edge} for edge in [control['min'], control['max']]])
            for params in choices:
                with self.subTest(lab=lab['id'], params=params):
                    out = COMPUTE[lab['id']](params)
                    json.dumps(clean(out), allow_nan=False)
                    self.assertGreaterEqual(len(out['metrics']), 4)
                    self.assertGreaterEqual(len(out['charts']), 2)
                    self.assertGreaterEqual(len(out['steps']), 3)
                    self.assertEqual(out['scene']['kind'], 'curves')

    def test_content_and_guides_cover_each_lab(self):
        for lab in LABS:
            id_ = lab['id']
            self.assertEqual(sum(l['lab'] == id_ for l in LESSONS), 2)
            self.assertEqual(sum(e['lab'] == id_ for e in EXERCISES), 3)
            self.assertEqual(set(GUIDES[id_]['levels']), {'sup', 'spe', 'beyond'})
            self.assertEqual(len(GUIDES[id_]['first_steps']), 3)
            self.assertTrue(all(len(e['answer']) > 180 for e in EXERCISES if e['lab'] == id_))

    def test_all_chart_series_align_and_have_named_units(self):
        for lab in LABS:
            for chart_ in calculate(lab['id'])['charts']:
                self.assertTrue(chart_['x_label'])
                self.assertTrue(chart_['y_label'])
                for curve in chart_['series']:
                    self.assertEqual(len(curve['x']), len(curve['y']))


if __name__ == '__main__':
    unittest.main()
