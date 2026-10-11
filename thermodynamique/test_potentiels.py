"""Bilans indépendants et contrôles de stabilité des modèles P22."""
import itertools
import json
import math
import unittest
import numpy as np
from commun import clean, integrate
from catalogue_potentiels import LABS
from contenu_potentiels import LESSONS, EXERCISES, GUIDES
from modeles_potentiels import (
    COMPUTE, R, TM, C_ICE, C_WATER, LATENT,
    helmholtz_potential, helmholtz_gradient, helmholtz_equilibrium,
    gibbs_mixture, gibbs_equilibrium, calorimetry_state,
    vdw_pressure, vdw_enthalpy, vdw_joule_thomson,
    cycle_data, compressor_work, body_exergy
)


def defaults(id_):
    lab = next(item for item in LABS if item['id'] == id_)
    return {c['key']: c['value'] for c in lab['controls']}


def calculate(id_, **changes):
    p = defaults(id_)
    p.update(changes)
    return COMPUTE[id_](p)


def metrics(out):
    return {m['label']: m['value'] for m in out['metrics']}


class WorkPaths(unittest.TestCase):
    def test_isothermal_work_and_first_principle(self):
        m = metrics(calculate('travail_chemins', T1=300, ratio=2, k=1))
        self.assertAlmostEqual(m['Travail reçu : polytrope'], -R * 300 * math.log(2), delta=1e-10)
        self.assertAlmostEqual(m['ΔU commune aux trois chemins'], 0, delta=1e-10)
        self.assertAlmostEqual(m['Chaleur reçue : polytrope'], R * 300 * math.log(2), delta=1e-10)

    def test_adiabatic_case_cools_and_entropy_is_constant(self):
        m = metrics(calculate('travail_chemins', k=1.4, ratio=2))
        self.assertLess(m['Température finale commune T₂'], 300)
        self.assertAlmostEqual(m['Chaleur reçue : polytrope'], 0, delta=1e-10)
        self.assertAlmostEqual(m['ΔS commune aux trois chemins'], 0, delta=2e-13)

    def test_alternative_paths_share_energy_and_have_different_work(self):
        out = calculate('travail_chemins', ratio=2, k=1.4)
        rows = out['table']['rows']
        for row in rows:
            self.assertAlmostEqual(row[1] + row[2], row[3], delta=1e-10)
        self.assertNotAlmostEqual(rows[1][1], rows[2][1])
        self.assertEqual(rows[0][3], rows[1][3])

    def test_polytrope_work_matches_independent_area(self):
        out = calculate('travail_chemins', k=1.3, ratio=.5)
        curve = out['charts'][0]['series'][0]
        area = -integrate(curve['y'] * 1e5, curve['x'] / 1000)
        expected = metrics(out)['Travail reçu : polytrope']
        self.assertAlmostEqual(area / expected, 1, delta=2e-6)
        self.assertGreater(expected, 0)

    def test_degenerate_path_has_zero_transfers(self):
        m = metrics(calculate('travail_chemins', ratio=1, k=1.8))
        for name in ['Travail reçu : polytrope', 'ΔU commune aux trois chemins', 'Chaleur reçue : polytrope', 'ΔS commune aux trois chemins']:
            self.assertAlmostEqual(m[name], 0, delta=1e-12)

    def test_generalised_work_equals_stored_energy_change_and_oriented_area(self):
        for device in ['surface', 'wire', 'capacitor', 'coil']:
            out = calculate('travaux_generalises', device=device, initial=.2, final=2)
            m = metrics(out)
            effort = out['charts'][0]['series'][0]
            # Undo only the display scale; the effort is already in SI units.
            display = {'surface': 1e4, 'wire': 100, 'capacitor': 1e6, 'coil': 1000}[device]
            area = integrate(effort['y'], effort['x'] / display)
            self.assertAlmostEqual(area, m['Travail reçu W'], delta=1e-12)
            self.assertAlmostEqual(m['Variation de l’énergie stockée'], m['Travail reçu W'])

    def test_reversing_generalised_coordinate_reverses_work(self):
        for device in ['surface', 'wire', 'capacitor', 'coil']:
            forward = metrics(calculate('travaux_generalises', device=device, initial=.2, final=2))['Travail reçu W']
            backward = metrics(calculate('travaux_generalises', device=device, initial=2, final=.2))['Travail reçu W']
            self.assertAlmostEqual(backward, -forward, delta=1e-12)

    def test_coil_energy_matches_LI_squared(self):
        m = metrics(calculate('travaux_generalises', device='coil', final=2, scale=1))
        I = m['Intensité I finale']
        self.assertAlmostEqual(m['Énergie stockée finale'], .5 * .04 * I ** 2, delta=1e-14)


class FreeEnergyMinima(unittest.TestCase):
    def test_no_spring_equilibrium_equalises_pressures(self):
        for nL in [.2, .4, .8]:
            y = helmholtz_equilibrium(300, nL, 0, .6)
            self.assertAlmostEqual(y, nL, delta=2e-15)
            m = metrics(calculate('potentiel_helmholtz', fraction=nL, stiffness=0))
            self.assertAlmostEqual(m['Pression gauche à l’équilibre'], m['Pression droite à l’équilibre'], delta=1e-12)

    def test_helmholtz_stationary_point_is_global_minimum(self):
        p = defaults('potentiel_helmholtz')
        p.update(stiffness=80000, fraction=.2, rest=.8)
        y = helmholtz_equilibrium(p['T'], p['fraction'], p['stiffness'], p['rest'])
        minimum = float(helmholtz_potential(y, p['T'], p['fraction'], p['stiffness'], p['rest']))
        candidates = helmholtz_potential(np.linspace(.001, .999, 10001), p['T'], p['fraction'], p['stiffness'], p['rest'])
        self.assertGreaterEqual(np.min(candidates) + 1e-9, minimum)

    def test_helmholtz_force_equals_derivative_and_pressure_balance(self):
        T, fraction, k, rest, y = 300, .4, 30000, .6, .7
        eps = 1e-6
        central = (helmholtz_potential(y + eps, T, fraction, k, rest) - helmholtz_potential(y - eps, T, fraction, k, rest)) / (2 * eps)
        self.assertAlmostEqual(float(central), helmholtz_gradient(y, T, fraction, k, rest), delta=2e-6)
        out = metrics(calculate('potentiel_helmholtz', T=T, fraction=fraction, stiffness=k, rest=rest))
        self.assertAlmostEqual(out['Résidu du bilan des forces à l’équilibre'], 0, delta=2e-10)

    def test_helmholtz_potential_decreases_along_relaxation(self):
        for yi in [.1, .9]:
            out = calculate('potentiel_helmholtz', initial=yi)
            energy = out['charts'][2]['series'][0]['y']
            self.assertTrue(np.all(np.diff(energy) <= 1e-9))
            self.assertGreaterEqual(np.min(energy), -1e-9)

    def test_gibbs_equal_standard_potentials_give_equal_mixture(self):
        self.assertAlmostEqual(gibbs_equilibrium(300, 0, 0), .5)
        self.assertAlmostEqual(gibbs_mixture(.5, 300, 0, 0), -R * 300 * math.log(2), delta=1e-10)

    def test_gibbs_derivative_and_mass_action_agree(self):
        T, dH, dS = 300, -6, -10
        x = gibbs_equilibrium(T, dH, dS)
        K = math.exp(-(dH * 1000 - T * dS) / (R * T))
        self.assertAlmostEqual(x / (1 - x), K, delta=1e-12)
        self.assertAlmostEqual(dH * 1000 - T * dS + R * T * math.log(x / (1 - x)), 0, delta=1e-10)

    def test_gibbs_temperature_switch_is_at_H_over_S(self):
        self.assertAlmostEqual(gibbs_equilibrium(600, -6, -10), .5)
        self.assertGreater(gibbs_equilibrium(300, -6, -10), .5)
        self.assertLess(gibbs_equilibrium(700, -6, -10), .5)

    def test_gibbs_minimum_is_lower_than_endpoint_compositions(self):
        for T, dH, dS in [(240, 12, -20), (700, -12, 20), (300, 0, 0)]:
            x = gibbs_equilibrium(T, dH, dS)
            self.assertLess(float(gibbs_mixture(x, T, dH, dS)), min(float(gibbs_mixture(0, T, dH, dS)), float(gibbs_mixture(1, T, dH, dS))))


class Calorimetry(unittest.TestCase):
    def test_two_capacities_equilibrate_to_weighted_mean(self):
        Tf, _, _, _, _ = calorimetry_state('solids', 330, 270, 1000 / C_WATER, 500 / C_ICE, 100)
        self.assertAlmostEqual(Tf, 311.25, delta=1e-12)

    def test_phase_energy_balance_in_all_three_regimes(self):
        cases = [(330, 263.15, .5, .1, 100), (300, 263.15, .3, .3, 0), (290, 240, .1, .8, 0)]
        regimes = set()
        for warm, cold, m1, m2, Ccal in cases:
            Tf, liquid, _, regime, initial = calorimetry_state('ice', warm, cold, m1, m2, Ccal)
            regimes.add(regime)
            ice = m1 + m2 - liquid
            final = ice * C_ICE * (Tf - TM) + liquid * (LATENT + C_WATER * (Tf - TM)) + Ccal * (Tf - TM)
            self.assertAlmostEqual(final, initial, delta=1e-8)
        self.assertEqual(len(regimes), 3)

    def test_partial_melting_mass_follows_latent_heat(self):
        Tf, liquid, _, _, _ = calorimetry_state('ice', TM + 20, TM, 1, .5, 0)
        self.assertAlmostEqual(Tf, TM)
        self.assertAlmostEqual(liquid - 1, C_WATER * 20 / LATENT, delta=1e-12)

    def test_cold_ice_can_freeze_initially_warm_water(self):
        Tf, liquid, entropy, _, _ = calorimetry_state('ice', 290, 240, .1, .8, 0)
        self.assertEqual(liquid, 0)
        self.assertLess(Tf, TM)
        self.assertGreater(Tf, 240)
        self.assertGreater(entropy, 0)

    def test_entropy_creation_positive_with_or_without_phase_change(self):
        for mode in ['solids', 'ice']:
            for m2 in np.linspace(.02, .8, 61):
                entropy = calorimetry_state(mode, 320, 250, .5, m2, 100)[2]
                self.assertGreaterEqual(entropy, -1e-10)

    def test_calorimeter_initial_energy_is_counted(self):
        without = calorimetry_state('ice', 330, 263.15, .5, .1, 0)[0]
        with_cal = calorimetry_state('ice', 330, 263.15, .5, .1, 500)[0]
        self.assertGreater(with_cal, without)


class JouleProcesses(unittest.TestCase):
    def test_free_ideal_gas_has_same_temperature_and_positive_entropy(self):
        m = metrics(calculate('detentes_joule', experiment='free_ideal', ratio=2))
        self.assertAlmostEqual(m['Variation Tf−Ti'], 0, delta=1e-12)
        self.assertAlmostEqual(m['Entropie créée par mole'], R * math.log(2), delta=1e-12)

    def test_vdw_free_expansion_conserves_u_and_cools(self):
        out = calculate('detentes_joule', experiment='free_vdw', a=.3, vi=2, ratio=3)
        m = metrics(out)
        self.assertAlmostEqual(m['Variation d’énergie interne molaire Δu'], 0, delta=1e-10)
        self.assertAlmostEqual(m['Variation Tf−Ti'], .3 / (2.5 * R) * (1 / .006 - 1 / .002), delta=1e-10)
        self.assertGreater(m['Entropie créée par mole'], 0)

    def test_vdw_throttle_conserves_h_at_every_point(self):
        out = calculate('detentes_joule', experiment='throttle_vdw', ratio=4)
        h_change = out['charts'][1]['series'][1]['y']
        np.testing.assert_allclose(h_change, 0, atol=2e-11)
        self.assertGreater(metrics(out)['Entropie créée par mole'], 0)

    def test_joule_thomson_matches_independent_slope_of_isenthalp(self):
        Ti, vi, a, b, cv = 300, .005, .14, 40e-6, 2.5 * R
        hi = float(vdw_enthalpy(Ti, vi, a, b, cv))
        v = np.array([vi * (1 - 1e-5), vi * (1 + 1e-5)])
        T = (hi + 2 * a / v) / (cv + R * v / (v - b))
        P = vdw_pressure(T, v, a, b)
        slope = (T[1] - T[0]) / (P[1] - P[0])
        expected = vdw_joule_thomson(Ti, vi, a, b, cv)[0]
        self.assertAlmostEqual(slope, expected, delta=3e-12)

    def test_inversion_temperature_annuls_coefficient(self):
        vi, a, b, cv = .005, .14, 40e-6, 2.5 * R
        Tinversion = 2 * a * (1 - b / vi) ** 2 / (R * b)
        mu, _, _, _ = vdw_joule_thomson(Tinversion, vi, a, b, cv)
        self.assertAlmostEqual(mu, 0, delta=2e-19)

    def test_two_throttles_really_have_opposite_temperature_changes(self):
        cool = metrics(calculate('detentes_joule', experiment='throttle_vdw', T=300, a=.14, b=40))
        warm = metrics(calculate('detentes_joule', experiment='throttle_vdw', T=500, a=.02, b=50))
        self.assertLess(cool['Variation Tf−Ti'], 0)
        self.assertGreater(cool['µJT initial, pour un étranglement'], 0)
        self.assertGreater(warm['Variation Tf−Ti'], 0)
        self.assertLess(warm['µJT initial, pour un étranglement'], 0)

    def test_vdw_corners_stay_stable_and_have_positive_pressures(self):
        for Ti, vi, a, b, cvR in itertools.product([180, 650], [.002, .02], [.02, .3], [20e-6, 50e-6], [1.5, 4]):
            hi = float(vdw_enthalpy(Ti, vi, a, b, cvR * R))
            v = np.linspace(vi, 4 * vi, 31)
            T = (hi + 2 * a / v) / (cvR * R + R * v / (v - b))
            self.assertTrue(np.all(vdw_pressure(T, v, a, b) > 0))
            self.assertTrue(np.all(R * T / (v - b) ** 2 - 2 * a / v ** 3 > 0))


class MachinesCycles(unittest.TestCase):
    def test_carnot_engine_reaches_bound_and_closes_both_principles(self):
        m = metrics(calculate('carnot_ditherme', mode='engine', cold=300, hot=600, quality=1, energy=10))
        self.assertAlmostEqual(m['Rendement moteur'], .5)
        self.assertAlmostEqual(m['Travail reçu W par cycle'], -5)
        self.assertAlmostEqual(m['Chaleur reçue depuis la source froide Qf'], -5)
        self.assertAlmostEqual(m['Entropie créée par cycle'], 0, delta=1e-12)

    def test_irreversible_machine_closes_entropy_balance(self):
        for mode in ['engine', 'fridge', 'heatpump']:
            m = metrics(calculate('carnot_ditherme', mode=mode, quality=.6))
            balance = m['Chaleur reçue depuis la source chaude Qc'] * 1000 / 600 + m['Chaleur reçue depuis la source froide Qf'] * 1000 / 300 + m['Entropie créée par cycle']
            self.assertAlmostEqual(balance, 0, delta=1e-11)
            self.assertAlmostEqual(m['Bilan W+Qc+Qf'], 0, delta=1e-10)
            self.assertGreater(m['Entropie créée par cycle'], 0)

    def test_fridge_and_heat_pump_cops_differ_by_one(self):
        one = metrics(calculate('carnot_ditherme', mode='fridge'))
        two = metrics(calculate('carnot_ditherme', mode='heatpump'))
        self.assertAlmostEqual(two['COP pompe à chaleur'] - one['COP frigorifique'], 1)
        self.assertEqual(one['Travail reçu W par cycle'], two['Travail reçu W par cycle'])

    def test_cycle_branch_first_principle_and_net_work(self):
        for cycle in ['otto', 'diesel', 'brayton', 'stirling']:
            d = cycle_data(cycle, 8, 1.6, 1.4, 300, .7)
            self.assertAlmostEqual(math.fsum(d['work']), d['W'], delta=1e-9)
            self.assertAlmostEqual(math.fsum(d['heat']), -d['W'], delta=1e-9)
            for j in range(4):
                dU = d['cv'] * (d['states'][(j + 1) % 4][0] - d['states'][j][0])
                self.assertAlmostEqual(d['work'][j] + d['heat'][j], dU, delta=1e-10)

    def test_cycle_area_matches_net_work_independently(self):
        for cycle in ['otto', 'diesel', 'brayton', 'stirling']:
            d = cycle_data(cycle, 8, 1.6, 1.4, 300, .6, samples=2401)
            area = -integrate(d['P'], d['V'])
            self.assertAlmostEqual(area / d['W'], 1, delta=2e-6)

    def test_otto_and_diesel_efficiency_formulas(self):
        r, z, gamma = 8, 1.6, 1.4
        otto = cycle_data('otto', r, z, gamma, 300)['efficiency']
        diesel = cycle_data('diesel', r, z, gamma, 300)['efficiency']
        self.assertAlmostEqual(otto, 1 - r ** (1 - gamma), delta=1e-14)
        self.assertAlmostEqual(diesel, 1 - r ** (1 - gamma) * (z ** gamma - 1) / (gamma * (z - 1)), delta=1e-14)

    def test_brayton_closed_and_open_net_work_agree(self):
        d = cycle_data('brayton', 8, 1.6, 1.4, 300)
        T1, T2, T3, T4 = [s[0] for s in d['states']]
        open_work = d['cp'] * ((T2 - T1) + (T4 - T3))
        self.assertAlmostEqual(open_work, d['W'], delta=1e-9)

    def test_stirling_regenerator_changes_external_heat_but_not_cycle_area(self):
        bad = cycle_data('stirling', 8, 1.6, 1.4, 300, 0)
        good = cycle_data('stirling', 8, 1.6, 1.4, 300, 1)
        np.testing.assert_array_equal(bad['P'], good['P'])
        self.assertAlmostEqual(bad['W'], good['W'], delta=1e-10)
        self.assertGreater(bad['Qhot'], good['Qhot'])
        self.assertAlmostEqual(good['efficiency'], 1 - 1 / 1.6, delta=1e-14)

    def test_cycle_efficiencies_stay_below_extreme_temperature_carnot_bound(self):
        for cycle, gamma, r, z, regen in itertools.product(['otto', 'diesel', 'brayton', 'stirling'], [1.25, 1.67], [2, 18], [1.15, 1.8], [0, 1]):
            d = cycle_data(cycle, r, z, gamma, 300, regen, samples=9)
            carnot = 1 - 300 / np.max(d['T'])
            self.assertGreater(d['efficiency'], 0)
            self.assertLessEqual(d['efficiency'], carnot + 1e-13)


class CompressionExergy(unittest.TestCase):
    def test_equal_pressure_ratios_are_work_minimum(self):
        for stages in [2, 3, 6]:
            optimum = compressor_work(300, 16, stages, 1 / stages, .8)
            for fraction in np.linspace(.02, .98, 101):
                self.assertGreaterEqual(compressor_work(300, 16, stages, fraction, .8) + 1e-8, optimum)

    def test_intermediate_pressures_form_geometric_sequence_at_minimum(self):
        out = calculate('compresseur_etages', ratio=16, stages=4, fraction=.25)
        ratios = [row[2] / row[1] for row in out['table']['rows']]
        np.testing.assert_allclose(ratios, [2, 2, 2, 2], atol=2e-14)

    def test_compressor_global_open_energy_balance(self):
        m = metrics(calculate('compresseur_etages', ratio=30, stages=6, efficiency=.65, fraction=.8))
        self.assertAlmostEqual(m['Travail d’arbre reçu'] + m['Chaleur reçue dans les refroidisseurs'], m['Variation d’enthalpie entrée–sortie'], delta=1e-10)
        self.assertGreater(m['Entropie créée, refroidisseurs au thermostat T₁'], 0)

    def test_more_optimal_stages_reduce_work_and_isothermal_is_lower_bound(self):
        values = [compressor_work(300, 16, N, 1 / N, 1) for N in [2, 3, 6, 20]]
        self.assertTrue(all(a > b for a, b in zip(values, values[1:])))
        self.assertGreater(values[-1], 287 * 300 * math.log(16))

    def test_hot_body_maximum_matches_integrated_carnot_efficiency(self):
        Ti, T0, C = 600, 300, 1000
        T = np.linspace(T0, Ti, 100001)
        integral = integrate(C * (1 - T0 / T), T)
        self.assertAlmostEqual(integral, float(body_exergy(Ti, T0, C)), delta=1e-5)

    def test_cold_body_exergy_is_positive(self):
        m = metrics(calculate('exergie_corps', initial=180, ambient=300, quality=1))
        self.assertGreater(m['Travail maximal disponible'], 0)
        self.assertGreater(m['Variation d’énergie interne du corps'], 0)
        self.assertGreater(m['Chaleur reçue de l’environnement par corps + machine'], m['Variation d’énergie interne du corps'])

    def test_exergy_first_and_second_principle_close(self):
        for Ti, phi in itertools.product([180, 600, 1000], [0, .4, 1]):
            m = metrics(calculate('exergie_corps', initial=Ti, quality=phi))
            self.assertAlmostEqual(m['Travail reçu par corps + machine'] + m['Chaleur reçue de l’environnement par corps + machine'], m['Variation d’énergie interne du corps'], delta=1e-10)
            entropy_balance = m['Variation d’entropie du corps'] - 1000 * m['Chaleur reçue de l’environnement par corps + machine'] / 300
            self.assertAlmostEqual(entropy_balance, m['Entropie créée'], delta=2e-10)

    def test_work_plus_destroyed_exergy_equals_initial_exergy(self):
        m = metrics(calculate('exergie_corps', quality=.4))
        self.assertAlmostEqual(m['Travail fourni au milieu extérieur'] + m['Exergie détruite T₀Scréée'], m['Travail maximal disponible'], delta=1e-10)

    def test_equal_temperature_has_zero_exergy(self):
        m = metrics(calculate('exergie_corps', initial=300, ambient=300))
        for label in ['Travail maximal disponible', 'Variation d’énergie interne du corps', 'Variation d’entropie du corps', 'Entropie créée']:
            self.assertAlmostEqual(m[label], 0, delta=1e-12)

    def test_near_equilibrium_exergy_is_quadratic(self):
        for delta in [-.01, .01]:
            actual = float(body_exergy(300 + delta, 300, 1000))
            expected = 1000 * delta ** 2 / (2 * 300)
            self.assertAlmostEqual(actual / expected, 1, delta=3e-5)


class Contracts(unittest.TestCase):
    def test_all_presets_choices_and_single_bounds_have_finite_json(self):
        for lab in LABS:
            base = defaults(lab['id'])
            variants = [base] + [{**base, **pre['values']} for pre in lab['presets']]
            for c in lab['controls']:
                options = [c['min'], c['max']] if c['type'] == 'range' else [o['value'] for o in c['options']]
                variants.extend([{**base, c['key']: value} for value in options])
            for p in variants:
                with self.subTest(lab=lab['id'], params=p):
                    out = COMPUTE[lab['id']](p)
                    json.dumps(clean(out), allow_nan=False)
                    self.assertGreaterEqual(len(out['charts']), 2)
                    self.assertGreaterEqual(len(out['metrics']), 4)

    def test_simultaneous_extreme_corners_are_finite_and_physical(self):
        for lab in LABS:
            keys = [c['key'] for c in lab['controls']]
            edges = [[c['min'], c['max']] if c['type'] == 'range' else [o['value'] for o in c['options']] for c in lab['controls']]
            for values in itertools.product(*edges):
                with self.subTest(lab=lab['id'], values=values):
                    out = COMPUTE[lab['id']](dict(zip(keys, values)))
                    json.dumps(clean(out), allow_nan=False)
                    for m in out['metrics']:
                        if 'Entropie créée' in m['label'] or 'Entropie totale créée' in m['label']:
                            self.assertGreaterEqual(m['value'], -2e-10)

    def test_course_exercises_guides_and_presets_cover_every_lab(self):
        for lab in LABS:
            id_ = lab['id']
            self.assertEqual(sum(l['lab'] == id_ for l in LESSONS), 2)
            self.assertEqual(sum(e['lab'] == id_ for e in EXERCISES), 3)
            self.assertEqual(set(GUIDES[id_]['levels']), {'sup', 'spe', 'beyond'})
            self.assertEqual(len(GUIDES[id_]['first_steps']), 3)
            self.assertGreaterEqual(len(lab['presets']), 3)
            self.assertTrue(all(len(l['html']) > 750 for l in LESSONS if l['lab'] == id_))

    def test_chart_series_align_and_have_axis_labels(self):
        for lab in LABS:
            for c in calculate(lab['id'])['charts']:
                self.assertTrue(c['x_label'])
                self.assertTrue(c['y_label'])
                for curve in c['series']:
                    self.assertEqual(len(curve['x']), len(curve['y']))


if __name__ == '__main__':
    unittest.main()
