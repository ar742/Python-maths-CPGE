"""Contrôles indépendants des lois de mécanique P1, sans dépendance externe."""
import json
import math
import unittest
import numpy as np
from commun import clean
from catalogue_p1 import LABS
from modeles_p1 import COMPUTE, ellipse


def defaults(id_):
    item = next(lab for lab in LABS if lab['id'] == id_)
    return {c['key']: c['value'] for c in item['controls']}


def calculate(id_, **changes):
    params = defaults(id_)
    params.update(changes)
    return COMPUTE[id_](params)


def metrics(output):
    return {m['label']: m['value'] for m in output['metrics']}


class OrbitalLaws(unittest.TestCase):
    def test_ellipse_satisfies_newton_with_differentiated_positions(self):
        t, x, y, vx, vy, r, _ = ellipse(1.7, .35, 1.2, samples=4001)
        dt = t[1] - t[0]
        ax = (x[2:] - 2 * x[1:-1] + x[:-2]) / dt ** 2
        ay = (y[2:] - 2 * y[1:-1] + y[:-2]) / dt ** 2
        expected_x = -1.2 * x[1:-1] / r[1:-1] ** 3
        expected_y = -1.2 * y[1:-1] / r[1:-1] ** 3
        np.testing.assert_allclose(ax, expected_x, atol=1e-5, rtol=1e-4)
        np.testing.assert_allclose(ay, expected_y, atol=1e-5, rtol=1e-4)

    def test_equal_time_areas_using_polygon_cross_products(self):
        t, x, y, *_ = ellipse(2, .75, 1, samples=6001)
        triangles = .5 * (x[:-1] * y[1:] - y[:-1] * x[1:])
        sectors = triangles.reshape(12, 500).sum(axis=1)
        self.assertLess(np.ptp(sectors) / np.mean(sectors), .001)

    def test_kepler_scalings_and_eccentricity_independence(self):
        first = metrics(calculate('orbite_kepler', a=1, e=.1, mass=1))
        second = metrics(calculate('orbite_kepler', a=4, e=.8, mass=1))
        self.assertAlmostEqual(second['Période orbitale T'] / first['Période orbitale T'], 8)
        self.assertAlmostEqual(second['Énergie par unité de masse ε'] / first['Énergie par unité de masse ε'], .25)
        third = metrics(calculate('orbite_kepler', a=1, e=.8, mass=4))
        self.assertAlmostEqual(third['Période orbitale T'], .5)

    def test_two_stars_have_a_fixed_barycentre(self):
        out = calculate('deux_corps', q=.35, e=.8)
        m = metrics(out)
        first, second = out['scene']['bodies'][:2]
        np.testing.assert_allclose(m['Masse de la première étoile m₁'] * first['x'] + m['Masse de la deuxième étoile m₂'] * second['x'], 0, atol=1e-13)
        np.testing.assert_allclose(m['Masse de la première étoile m₁'] * first['y'] + m['Masse de la deuxième étoile m₂'] * second['y'], 0, atol=1e-13)
        self.assertAlmostEqual(m['Demi-grand axe a₁ autour de G'] / m['Demi-grand axe a₂ autour de G'], .35)

    def test_two_body_kinetic_decomposition(self):
        out = calculate('deux_corps', q=.2, e=.7)
        curves = out['charts'][1]['series']
        np.testing.assert_allclose(curves[0]['y'] + curves[1]['y'], curves[2]['y'], rtol=2e-14)
        first = metrics(out)
        second = metrics(calculate('deux_corps', q=.8, e=.7))
        self.assertAlmostEqual(first['Période commune'], second['Période commune'])

    def test_subcircular_launch_starts_at_apocentre(self):
        out = calculate('potentiel_effectif', eta=.5)
        curve = out['scene']['paths'][0]
        r = np.hypot(curve['x'], curve['y'])
        self.assertAlmostEqual(r[0], 1)
        self.assertAlmostEqual(np.max(r), 1)
        self.assertAlmostEqual(np.min(r), 1 / 7)

    def test_escape_threshold_and_circular_orbit(self):
        circle = calculate('potentiel_effectif', eta=1)
        np.testing.assert_allclose(np.hypot(circle['scene']['paths'][0]['x'], circle['scene']['paths'][0]['y']), 1, atol=1e-13)
        parabolic = metrics(calculate('potentiel_effectif', eta=math.sqrt(2)))
        self.assertAlmostEqual(parabolic['Énergie spécifique ε'], 0)
        self.assertEqual(parabolic['Type de trajectoire'], 'Parabole')
        self.assertGreater(metrics(calculate('potentiel_effectif', eta=1.6))['Énergie spécifique ε'], 0)

    def test_hohmann_same_radius_has_zero_cost(self):
        m = metrics(calculate('transfert_hohmann', r1=2, r2=2))
        self.assertAlmostEqual(m['Coût total |Δv₁|+|Δv₂|'], 0)
        self.assertAlmostEqual(m['Excentricité de transfert'], 0)

    def test_hohmann_reversed_transfer_has_same_cost_and_time(self):
        outward = metrics(calculate('transfert_hohmann', r1=1, r2=6))
        inward_out = calculate('transfert_hohmann', r1=6, r2=1)
        inward = metrics(inward_out)
        self.assertAlmostEqual(outward['Coût total |Δv₁|+|Δv₂|'], inward['Coût total |Δv₁|+|Δv₂|'])
        self.assertAlmostEqual(outward['Durée du transfert'], inward['Durée du transfert'])
        self.assertLess(inward['Première impulsion Δv₁ (signée)'], 0)
        transfer = inward_out['scene']['paths'][-1]
        self.assertAlmostEqual(math.hypot(transfer['x'][0], transfer['y'][0]), 6)
        self.assertAlmostEqual(math.hypot(transfer['x'][-1], transfer['y'][-1]), 1)

    def test_mars_transfer_has_expected_time_scale(self):
        out = metrics(calculate('transfert_hohmann', central='sun', r1=1, r2=1.524))
        self.assertAlmostEqual(out['Durée du transfert'] / 24, 259, delta=2)

    def test_scattering_energy_and_monotonic_deflection(self):
        far = metrics(calculate('diffusion_gravitationnelle', b=4, vinf=1))
        near = metrics(calculate('diffusion_gravitationnelle', b=1, vinf=1))
        self.assertGreater(near['Angle de déviation δ'], far['Angle de déviation δ'])
        self.assertLess(near['Distance minimale au centre rp'], far['Distance minimale au centre rp'])
        self.assertLess(near['Erreur maximale sur ε=v²/2−1/r'], 1e-12)
        faster = metrics(calculate('diffusion_gravitationnelle', b=1, vinf=2))
        self.assertLess(faster['Angle de déviation δ'], near['Angle de déviation δ'])

    def test_assistance_requires_a_moving_astre_in_second_frame(self):
        rest = metrics(calculate('diffusion_gravitationnelle', planet_v=0))
        self.assertAlmostEqual(rest['Gain d’énergie cinétique spécifique à l’infini'], 0)
        gain = metrics(calculate('diffusion_gravitationnelle', encounter='gain'))
        loss = metrics(calculate('diffusion_gravitationnelle', encounter='loss'))
        self.assertGreater(gain['Gain d’énergie cinétique spécifique à l’infini'], 0)
        self.assertAlmostEqual(gain['Gain d’énergie cinétique spécifique à l’infini'], -loss['Gain d’énergie cinétique spécifique à l’infini'])


class BalancesAndFrames(unittest.TestCase):
    def test_tidal_field_decays_faster_than_attraction(self):
        close = metrics(calculate('marees', distance=4))
        far = metrics(calculate('marees', distance=8))
        self.assertAlmostEqual(close['Accélération du centre vers l’astre'] / far['Accélération du centre vers l’astre'], 4)
        self.assertAlmostEqual(close['Coefficient d’étirement radial 2GM/D³'] / far['Coefficient d’étirement radial 2GM/D³'], 8)
        self.assertLess(far['Erreur relative linéaire sur la face proche'], close['Erreur relative linéaire sur la face proche'])
        self.assertAlmostEqual(close['Somme des trois coefficients principaux'], 0)

    def test_rocket_mass_scale_does_not_change_velocity(self):
        first = calculate('fusee', m0=10)
        second = calculate('fusee', m0=20)
        np.testing.assert_allclose(first['charts'][1]['series'][1]['y'], second['charts'][1]['series'][1]['y'])
        self.assertAlmostEqual(metrics(second)['Poussée constante uq'] / metrics(first)['Poussée constante uq'], 2)

    def test_rocket_gravity_loss_and_shorter_burn(self):
        no_gravity = metrics(calculate('fusee', g=0, burn=60))
        ordinary = metrics(calculate('fusee', g=9.8, burn=60))
        shorter = metrics(calculate('fusee', g=9.8, burn=30))
        self.assertAlmostEqual(no_gravity['Vitesse finale'] - ordinary['Vitesse finale'], 9.8 * 60)
        self.assertAlmostEqual(shorter['Vitesse finale'] - ordinary['Vitesse finale'], 9.8 * 30)

    def test_rocket_position_differentiates_to_velocity(self):
        out = calculate('fusee', g=5)
        t = out['charts'][3]['series'][0]['x']
        position = out['charts'][3]['series'][0]['y'] * 1000
        velocity = out['charts'][1]['series'][1]['y']
        derivative = (position[2:] - position[:-2]) / (t[2:] - t[:-2])
        np.testing.assert_allclose(derivative, velocity[1:-1], atol=.15, rtol=1e-4)

    def test_rotating_coordinates_preserve_distance(self):
        out = calculate('coriolis', omega=.7, vx=1.2, x0=.8, y0=1.4)
        particle = out['scene']['bodies'][0]
        t = out['scene']['times']
        np.testing.assert_allclose(np.hypot(particle['x'], particle['y']), np.hypot(.8 + 1.2 * t, 1.4), rtol=1e-13)
        self.assertLess(metrics(out)['Erreur sur la somme des accélérations d’inertie'], 1e-12)

    def test_rotating_jacobi_invariant(self):
        omega = .7
        out = calculate('coriolis', omega=omega)
        body = out['scene']['bodies'][0]
        vx, vy = [curve['y'] for curve in out['charts'][0]['series'][:2]]
        invariant = .5 * (vx * vx + vy * vy) - .5 * omega ** 2 * (body['x'] ** 2 + body['y'] ** 2)
        self.assertLess(np.ptp(invariant), 1e-12)

    def test_all_presets_and_control_endpoints_are_finite(self):
        for lab in LABS:
            base = defaults(lab['id'])
            params = [base] + [dict(base, **preset['values']) for preset in lab['presets']]
            for control in lab['controls']:
                if control['type'] == 'range':
                    params.extend([dict(base, **{control['key']: control['min']}), dict(base, **{control['key']: control['max']})])
                else:
                    params.extend(dict(base, **{control['key']: option['value']}) for option in control['options'])
            for param in params:
                with self.subTest(lab=lab['id'], params=param):
                    output = COMPUTE[lab['id']](param)
                    json.dumps(clean(output), allow_nan=False)


if __name__ == '__main__':
    unittest.main()
