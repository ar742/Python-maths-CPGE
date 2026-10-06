"""Tests physiques indépendants des champs et de la conversion électromagnétique."""
import json
import math
import unittest

import numpy as np

from catalogue_conversion import LABS
from modeles_conversion import (EPS0, MU0, E_CHARGE, K_E, TAU, G, calculate,
    electric_pair, electric_dipole, sphere_field, loop_axis, loop_field,
    mutual_inductance, solenoid_axis, solenoid_field, rail_state,
    frame_entry, speaker_response, relay_hysteresis, induction_machine)


def value(r, prefix):
    return next(m["value"] for m in r["metrics"] if m["label"].startswith(prefix))


def integral(y, x):
    return np.trapezoid(y, x) if hasattr(np, "trapezoid") else np.trapz(y, x)


class ProtocolTests(unittest.TestCase):
    def test_twelve_unique_laboratories(self):
        self.assertEqual(len(LABS), 12)
        self.assertEqual(len({l["id"] for l in LABS}), 12)

    def test_defaults_and_presets_finite(self):
        for lab in LABS:
            for p in [{}]+[item["values"] for item in lab["presets"]]:
                with self.subTest(lab=lab["id"], p=p):
                    r = calculate(lab["id"], p)
                    json.dumps(r, allow_nan=False)
                    self.assertTrue(r["steps"] and r["assumptions"])
                    for c in r["charts"]:
                        for curve in c["series"]:
                            self.assertEqual(len(curve["x"]), len(curve["y"]))

    def test_native_sliders_preserve_defaults(self):
        for lab in LABS:
            for control in lab["controls"]:
                if control["type"] == "range":
                    n = (control["value"]-control["min"])/control["step"]
                    self.assertAlmostEqual(n, round(n), places=7, msg=f"{lab['id']} {control['key']}")

    def test_individual_extremes_finite(self):
        for lab in LABS:
            for c in lab["controls"]:
                bounds = [o["value"] for o in c["options"]] if c["type"] == "select" else [c["min"], c["max"]]
                for bound in bounds:
                    with self.subTest(lab=lab["id"], key=c["key"], value=bound):
                        json.dumps(calculate(lab["id"], {c["key"]: bound}), allow_nan=False)

    def test_combined_extremes_in_each_mode_finite(self):
        for lab in LABS:
            modes = next(([o["value"] for o in c["options"]] for c in lab["controls"] if c["key"] == "mode"), [None])
            for mode in modes:
                for side in ("min", "max"):
                    p = {c["key"]: c[side] for c in lab["controls"] if c["type"] == "range"}
                    if mode:
                        p["mode"] = mode
                    with self.subTest(lab=lab["id"], mode=mode, side=side):
                        json.dumps(calculate(lab["id"], p), allow_nan=False)

    def test_field_dimensions_and_physical_units(self):
        for lab in LABS:
            f = calculate(lab["id"]).get("field")
            if f:
                self.assertIn(f["vector_label"], ("E", "B"))
                for key in ("u", "v", "scalar"):
                    self.assertEqual(np.shape(f[key]), (len(f["y"]), len(f["x"])))


class FieldTests(unittest.TestCase):
    def test_pair_axial_coulomb_superposition(self):
        a, q, radius = .2, 1e-8, 1.
        ex, ey, _ = electric_pair(np.array([radius]), np.array([0.]), q, a)
        reference = K_E*q*((radius-a/2)**-2-(radius+a/2)**-2)
        self.assertAlmostEqual(ex[0], reference, places=12)
        self.assertEqual(ey[0], 0)

    def test_dipole_rotation_covariance(self):
        x, y, q, a = .5, .8, 2e-8, .2
        ex, ey, V = electric_pair(np.array([x]), np.array([y]), q, a)
        fx, fy, W = electric_pair(np.array([-y]), np.array([x]), q, a, math.pi/2)
        np.testing.assert_allclose([fx, fy], [-ey, ex], rtol=1e-14)
        np.testing.assert_allclose(V, W, rtol=1e-14)

    def test_pair_potential_odd_and_midpoint_zero(self):
        _, _, V = electric_pair(np.array([0., .4, -.4]), np.array([0., .3, -.3]), 1e-8, .2)
        self.assertEqual(V[0], 0)
        self.assertAlmostEqual(V[1], -V[2])

    def test_dipolar_error_decreases_quadratically(self):
        r1 = value(calculate("dipoles", {"distance": 10}), "Erreur relative sur l’axe")
        r2 = value(calculate("dipoles", {"distance": 20}), "Erreur relative sur l’axe")
        self.assertAlmostEqual(r1/r2, 4, delta=.005)

    def test_dipole_is_negative_gradient_of_potential(self):
        x, y, px, py, step = .6, .4, 2e-9, 1e-9, 1e-6
        ex, ey, _ = electric_dipole(x, y, px, py)
        gx = -(electric_dipole(x+step, y, px, py)[2]-electric_dipole(x-step, y, px, py)[2])/(2*step)
        gy = -(electric_dipole(x, y+step, px, py)[2]-electric_dipole(x, y-step, px, py)[2])/(2*step)
        np.testing.assert_allclose([ex, ey], [gx, gy], rtol=2e-10)

    def test_gauss_enclosed_charge_inside_outside(self):
        Q, R = 2e-8, .2
        r = np.array([R/2, R, R*2])
        electric, _ = sphere_field(r, Q, R)
        flux = 4*math.pi*r*r*electric
        np.testing.assert_allclose(EPS0*flux, [Q/8, Q, Q], rtol=1e-14)

    def test_sphere_potential_gradient_and_continuity(self):
        Q, R, step = 2e-8, .2, 1e-6
        for r in (.1, .3):
            E, _ = sphere_field(np.array([r]), Q, R)
            _, plus = sphere_field(np.array([r+step]), Q, R)
            _, minus = sphere_field(np.array([r-step]), Q, R)
            self.assertAlmostEqual(float(E[0]/(-(plus-minus)/(2*step))[0]), 1, places=8)
        E, V = sphere_field(np.array([R-step, R, R+step]), Q, R)
        self.assertLess(max(V)-min(V), .01)
        self.assertLess(max(E)-min(E), .1)

    def test_sphere_energy_from_field_integral(self):
        Q, R = 2e-8, .2
        r = np.linspace(0, R, 10001)
        E, _ = sphere_field(r, Q, R)
        interior = integral(.5*EPS0*E*E*4*math.pi*r*r, r)
        exterior = K_E*Q*Q/(2*R)
        self.assertAlmostEqual((interior+exterior)/(3*K_E*Q*Q/(5*R)), 1, places=8)

    def test_coaxial_energy_and_voltage_integral(self):
        r = calculate("gauss", {"mode": "coax"})
        curve = r["charts"][0]["series"][0]
        radii, electric = np.array(curve["x"])*.01, np.array(curve["y"])
        self.assertAlmostEqual(integral(electric, radii), 100, delta=.001)
        energy = integral(.5*EPS0*electric**2*TAU*radii, radii)
        self.assertAlmostEqual(energy/value(r, "Énergie"), 1, places=5)

    def test_loop_quadrature_matches_exact_axis(self):
        z = np.linspace(-.5, .5, 51)
        bx, bz = loop_field(np.zeros_like(z), z, .1, 2)
        np.testing.assert_allclose(bz, loop_axis(z, .1, 2), rtol=1e-14)
        np.testing.assert_allclose(bx, 0, atol=1e-20)

    def test_loop_far_field_has_magnetic_dipole_scaling(self):
        R, I, z = .1, 2, 20.
        exact = loop_axis(z, R, I)
        dipolar = MU0*(I*math.pi*R*R)/(TAU*z**3)
        self.assertAlmostEqual(exact/dipolar, 1, delta=4e-5)

    def test_isolated_loop_is_independent_of_solenoid_length(self):
        short = calculate("biotsavart", {"mode": "loop", "R": .1, "length": .1})
        long = calculate("biotsavart", {"mode": "loop", "R": .1, "length": 10})
        self.assertEqual(short["field"], long["field"])
        self.assertEqual(short["charts"], long["charts"])
        self.assertEqual(short["metrics"], long["metrics"])

    def test_biot_savart_reverses_with_current(self):
        for mode in ("wire", "loop", "solenoid"):
            positive = calculate("biotsavart", {"mode": mode, "I": 2})["field"]
            negative = calculate("biotsavart", {"mode": mode, "I": -2})["field"]
            np.testing.assert_allclose(positive["u"], -np.array(negative["u"]), atol=1e-18)
            np.testing.assert_allclose(positive["v"], -np.array(negative["v"]), atol=1e-18)

    def test_oersted_right_hand_rule(self):
        f = calculate("biotsavart", {"mode": "wire", "I": 2})["field"]
        row, col = len(f["y"])//2, len(f["x"])//2+5
        self.assertGreater(f["v"][row][col], 0)
        self.assertAlmostEqual(f["u"][row][col], 0)

    def test_mutuality_and_flux_independent_integral(self):
        r1, r2, distance = .1, .03, .2
        mutual = mutual_inductance(r1, r2, distance)
        self.assertAlmostEqual(mutual_inductance(r2, r1, distance), mutual, places=20)
        nodes, weights = np.polynomial.legendre.leggauss(64)
        radii = (nodes+1)*r2/2
        _, bz = loop_field(radii, np.full_like(radii, distance), r1, 1)
        flux = np.dot(weights, bz*TAU*radii)*r2/2
        self.assertAlmostEqual(flux/mutual, 1, places=12)

    def test_finite_solenoid_axis_numerical_field(self):
        for R, length in ((.1, 1), (.02, 2), (.5, .1)):
            z = np.linspace(-length, length, 51)
            bx, bz = solenoid_field(np.zeros_like(z), z, R, length, 2, 100)
            np.testing.assert_allclose(bz, solenoid_axis(z, R, length, 2, 100), rtol=1e-13)
            np.testing.assert_allclose(bx, 0, atol=1e-18)

    def test_solenoid_magnetic_divergence_outside_winding(self):
        x, z, step = .04, .17, 1e-6
        bx, bz = solenoid_field(np.array([x]), np.array([z]), .1, .4, 2, 100)
        px = solenoid_field(np.array([x+step]), np.array([z]), .1, .4, 2, 100)[0]
        mx = solenoid_field(np.array([x-step]), np.array([z]), .1, .4, 2, 100)[0]
        pz = solenoid_field(np.array([x]), np.array([z+step]), .1, .4, 2, 100)[1]
        mz = solenoid_field(np.array([x]), np.array([z-step]), .1, .4, 2, 100)[1]
        divergence = (px-mx)/(2*step)+bx/x+(pz-mz)/(2*step)
        self.assertAlmostEqual(float(divergence[0]), 0, places=11)

    def test_helmholtz_center_and_zero_curvature(self):
        r = calculate("helmholtz", {"spacing": 1, "R": .15, "turns": 100, "I": 1})
        self.assertAlmostEqual(value(r, "Champ au centre"), (4/5)**1.5*MU0*100/.15)
        self.assertEqual(value(r, "Courbure"), 0)

    def test_helmholtz_fourth_order_flatness(self):
        R, d = .15, .15
        def B(z):
            return loop_axis(z, R, 1, 100, -d/2)+loop_axis(z, R, 1, 100, d/2)
        first, second = abs(B(.02*R)/B(0)-1), abs(B(.04*R)/B(0)-1)
        self.assertAlmostEqual(second/first, 16, delta=.06)


class ConductorTests(unittest.TestCase):
    def test_drude_real_imag_at_relaxation_frequency(self):
        f = 1/(TAU*25e-15)/1e12
        r = calculate("drude", {"tau": 25, "frequency": f})
        sigma0 = value(r, "Conductivité continue")
        self.assertAlmostEqual(value(r, "Partie réelle")/sigma0, .5)
        self.assertAlmostEqual(value(r, "Partie imaginaire")/sigma0, .5)

    def test_drude_charge_sign_changes_drift_not_conductivity(self):
        electron, hole = calculate("drude", {"carrier": "electron"}), calculate("drude", {"carrier": "hole"})
        self.assertEqual(value(electron, "Conductivité continue"), value(hole, "Conductivité continue"))
        np.testing.assert_allclose(electron["charts"][1]["series"][0]["y"], -np.array(hole["charts"][1]["series"][0]["y"]))

    def test_drude_transient_energy_balance(self):
        curves = calculate("drude")["charts"][2]["series"]
        np.testing.assert_allclose(curves[0]["y"], np.array(curves[1]["y"])+curves[2]["y"], rtol=2e-14)
        self.assertGreater(max(curves[2]["y"]), 0)

    def test_drude_harmonic_heat_equals_kinetic_relaxation(self):
        r = calculate("drude", {"frequency": 100})
        self.assertAlmostEqual(value(r, "Chaleur moyenne")/value(r, "Énergie cinétique moyenne"), 2/(25e-15), delta=1)

    def test_hall_sign_and_lorentz_compensation(self):
        electron, hole = calculate("hall"), calculate("hall", {"carrier": "hole"})
        self.assertLess(value(electron, "UH="), 0)
        self.assertAlmostEqual(value(electron, "UH="), -value(hole, "UH="))
        self.assertAlmostEqual(value(electron, "Force électrique")+value(electron, "Force magnétique"), 0)

    def test_hall_both_reversals_and_thickness(self):
        r = calculate("hall")
        self.assertAlmostEqual(value(calculate("hall", {"I": -.2}), "UH="), -value(r, "UH="))
        self.assertAlmostEqual(value(calculate("hall", {"B": -.5}), "UH="), -value(r, "UH="))
        self.assertAlmostEqual(value(calculate("hall", {"thickness": .4}), "UH="), value(r, "UH=")/2)

    def test_hall_independent_of_width_at_fixed_current(self):
        self.assertAlmostEqual(value(calculate("hall", {"width": 5}), "UH="), value(calculate("hall", {"width": 10}), "UH="))

    def test_reversible_medium_has_no_hysteresis_loss(self):
        r = calculate("hysteresis", {"Bs": 0})
        self.assertEqual(value(r, "Énergie perdue"), 0)
        self.assertAlmostEqual(value(r, "Aire mesurée"), 0, places=13)

    def test_major_relay_loop_exact_loss(self):
        r = calculate("hysteresis", {"Hc": 1000, "Bs": 1, "amplitude": 2})
        self.assertAlmostEqual(value(r, "Énergie perdue"), 4000)
        self.assertAlmostEqual(value(r, "Aire mesurée")/4000, 1, delta=.01)
        scene = r["scene"]
        self.assertEqual(scene["B"][0], scene["B"][-1])

    def test_relay_memory_at_identical_field(self):
        threshold = np.array([100.])
        H = np.array([-200., 0., 200., 0., -200.])
        B = relay_hysteresis(H, threshold, 1)
        self.assertLess(B[1], 0)
        self.assertGreater(B[3], 0)

    def test_hysteresis_reconstruction_and_frequency(self):
        r1, r2 = calculate("hysteresis", {"frequency": 50}), calculate("hysteresis", {"frequency": 100})
        self.assertLess(value(r1, "Erreur de reconstruction"), 1e-14)
        self.assertEqual(value(r1, "Énergie perdue"), value(r2, "Énergie perdue"))
        self.assertAlmostEqual(value(r2, "Puissance volumique")/value(r1, "Puissance volumique"), 2)

    def test_minor_loop_requires_switching_threshold(self):
        r = calculate("hysteresis", {"amplitude": .1})
        self.assertEqual(value(r, "Énergie perdue"), 0)
        r = calculate("hysteresis", {"amplitude": .8})
        self.assertGreater(value(r, "Énergie perdue"), 0)
        self.assertLess(value(r, "Énergie perdue"), 4000)

    def test_skin_depth_frequency_square_root(self):
        d1, d2 = value(calculate("peau", {"logf": 3}), "Épaisseur"), value(calculate("peau", {"logf": 5}), "Épaisseur")
        self.assertAlmostEqual(d1/d2, 10)

    def test_skin_complex_field_satisfies_diffusion(self):
        mu, sigma, omega, step, x = MU0, 58e6, TAU*1000, 1e-6, .001
        D = 1/(mu*sigma)
        delta = math.sqrt(2*D/omega)
        def B(depth):
            return .01*np.exp((-1+1j)*depth/delta)
        lap = (B(x+step)-2*B(x)+B(x-step))/step**2
        self.assertAlmostEqual(abs((-1j*omega*B(x)-D*lap)/(omega*B(x))), 0, delta=1e-7)

    def test_skin_surface_flux_equals_integrated_joule(self):
        mu, sigma, omega, B0 = MU0, 58e6, TAU*1000, .01
        delta = math.sqrt(2/(mu*sigma*omega))
        x = np.linspace(0, 12*delta, 10001)
        bhat = B0*np.exp((-1+1j)*x/delta)
        j = (-1+1j)*bhat/(mu*delta)
        heat = integral(abs(j)**2/(2*sigma), x)
        flux = -.5*np.real((j[0]/sigma)*np.conj(bhat[0]/mu))
        self.assertAlmostEqual(heat/flux, 1, places=6)
        self.assertGreater(flux, 0)

    def test_magnetic_step_energy_partition(self):
        r = calculate("peau", {"mode": "step"})
        received, heat, growth = value(r, "Puissance reçue"), value(r, "Puissance Joule"), value(r, "Croissance")
        self.assertAlmostEqual(received, heat+growth)
        self.assertAlmostEqual(heat/received, 1/math.sqrt(2))
        # L'énergie intégrée varie comme √t : sa dérivée est U/(2t).
        self.assertAlmostEqual(value(r, "Énergie magnétique par aire")/(2*.001), growth)

    def test_magnetic_step_penetration_grows_sqrt_time(self):
        r1, r2 = calculate("peau", {"mode": "step", "time": 1}), calculate("peau", {"mode": "step", "time": 4})
        self.assertAlmostEqual(value(r2, "Longueur")/value(r1, "Longueur"), 2)


class ConversionTests(unittest.TestCase):
    def test_rail_passive_energy_derivative(self):
        m, R, L, coupling, step = .1, 1., .01, .1, 1e-5
        t = np.array([.03, .1, .5])
        v, i, _ = rail_state(t, m, R, L, coupling, 1)
        vp, ip, _ = rail_state(t+step, m, R, L, coupling, 1)
        vm, im, _ = rail_state(t-step, m, R, L, coupling, 1)
        rate = (.5*m*(vp*vp-vm*vm)+.5*L*(ip*ip-im*im))/(2*step)
        np.testing.assert_allclose(rate, -R*i*i, rtol=2e-7)

    def test_rail_zero_field_keeps_uniform_velocity(self):
        r = calculate("induction", {"B": 0, "mode": "rail"})
        np.testing.assert_allclose(r["scene"]["velocity"], 1)
        np.testing.assert_allclose(r["scene"]["current"], 0)
        np.testing.assert_allclose(r["scene"]["position"], r["scene"]["time"])

    def test_rail_arbitrarily_weak_nonzero_field_has_ballistic_limit(self):
        t = np.array([.1, 1., 2.])
        for coupling in (1e-6, 1e-10, 1e-30):
            v, i, x = rail_state(t, .1, 1., .01, coupling, 1.)
            np.testing.assert_allclose(v, 1., atol=3e-11, rtol=0)
            np.testing.assert_allclose(x, t, atol=5e-11, rtol=0)
            self.assertTrue(np.all(i <= 0))

    def test_rail_position_derivative_is_velocity_in_every_damping_regime(self):
        t, step = np.array([.001, .03, .1, .4]), 1e-7
        m, L, coupling = .01, .1, .5
        critical = 2*coupling*math.sqrt(L/m)
        for R in (.1, critical*(1-1e-10), critical, critical*(1+1e-10), 10.):
            v = rail_state(t, m, R, L, coupling, 1)[0]
            xp = rail_state(t+step, m, R, L, coupling, 1)[2]
            xm = rail_state(t-step, m, R, L, coupling, 1)[2]
            np.testing.assert_allclose((xp-xm)/(2*step), v, atol=2e-9, rtol=0)

    def test_rail_initial_lenz_current_negative(self):
        _, i, _ = rail_state(np.array([0., .001, .01]), .1, 1, .01, .1, 1)
        self.assertEqual(i[0], 0)
        self.assertLess(i[1], 0)
        self.assertLess(i[2], 0)

    def test_rail_underdamping_returns_magnetic_energy(self):
        v, i, _ = rail_state(np.linspace(0, 2, 1001), .01, .1, .1, .5, 1)
        self.assertLess(min(v), 0)
        total = .5*.01*v*v+.5*.1*i*i
        self.assertTrue(np.all(np.diff(total) <= 1e-12))

    def test_rail_critical_damping_remains_finite(self):
        m, L, coupling = .01, .1, .5
        R = 2*coupling*math.sqrt(L/m)
        t = np.linspace(0, 1, 51)
        v, i, x = rail_state(t, m, R, L, coupling, 1)
        lam = R/(2*L)
        np.testing.assert_allclose(v, np.exp(-lam*t)*(1+lam*t), rtol=1e-13)
        exact_x = -2*np.expm1(-lam*t)/lam-t*np.exp(-lam*t)
        np.testing.assert_allclose(x, exact_x, rtol=1e-13, atol=1e-15)

    def test_frame_entry_force_balance(self):
        tau, v0, t, step = .1, .2, .3, 1e-6
        _, v = frame_entry(t, v0, tau)
        _, vp = frame_entry(t+step, v0, tau)
        _, vm = frame_entry(t-step, v0, tau)
        self.assertAlmostEqual(float((vp-vm)/(2*step)), G-v/tau, places=8)

    def test_frame_complete_immersion_no_terminal_drag(self):
        r = calculate("induction", {"mode": "frame", "v0": 0, "duration": 2})
        scene = r["scene"]
        t, v, i = np.array(scene["time"]), np.array(scene["velocity"]), np.array(scene["current"])
        after = t > scene["exit_time"]+.001
        self.assertTrue(after.any())
        np.testing.assert_allclose(i[after], 0)
        np.testing.assert_allclose(np.diff(v[after])/np.diff(t[after]), G, rtol=1e-9)
        flux = np.array(r["charts"][1]["series"][0]["y"])
        self.assertTrue(np.all(flux[after] == flux[-1]))

    def test_frame_power_gravity_equals_heat_and_kinetic(self):
        curves = calculate("induction", {"mode": "frame"})["charts"][2]["series"]
        np.testing.assert_allclose(curves[0]["y"], np.array(curves[1]["y"])+curves[2]["y"], rtol=1e-13, atol=1e-14)

    def test_speaker_reciprocal_mean_power_balance(self):
        for f in (10, 50, 500, 2000):
            r = calculate("hautparleur", {"frequency": f})
            self.assertAlmostEqual(value(r, "Résidu du bilan"), 0, places=12)
            self.assertGreater(value(r, "Puissance mécanique"), 0)

    def test_speaker_motional_impedance_circle(self):
        f = np.geomspace(1, 10000, 201)
        _, z, _, _, _ = speaker_response(f, 6, .0005, .015, 1500, 1, 5, 2)
        np.testing.assert_allclose(abs(z-12.5), 12.5, rtol=1e-14)

    def test_speaker_zero_coupling_has_no_motion(self):
        z, zmot, i, v, x = speaker_response(50, 6, .0005, .015, 1500, 1, 0, 2)
        self.assertEqual(v, 0)
        self.assertEqual(x, 0)
        self.assertEqual(zmot, 0)
        self.assertAlmostEqual(abs(z-(6-1j*TAU*50*.0005)), 0)

    def test_speaker_at_mechanical_resonance_motional_resistance(self):
        f0 = math.sqrt(1500/.015)/TAU
        _, z, _, _, _ = speaker_response(f0, 6, .0005, .015, 1500, 1, 5, 2)
        self.assertAlmostEqual(z.real, 25)
        self.assertAlmostEqual(z.imag, 0, places=12)

    def test_synchronous_two_equilibria_and_pullout(self):
        r = calculate("synchrone", {"load": .5})
        self.assertAlmostEqual(value(r, "Phase stable"), 30)
        self.assertAlmostEqual(value(r, "Phase instable"), 150)
        r = calculate("synchrone", {"load": 1.2})
        self.assertIsInstance(value(r, "Phase stable"), str)

    def test_synchronous_threshold_is_critical_not_stable(self):
        r = calculate("synchrone", {"load": 1})
        self.assertIn("critique", value(r, "Phase stable"))
        self.assertIn("critique", value(r, "Phase instable"))
        self.assertEqual(value(r, "Fréquence des petites"), 0)

    def test_synchronous_small_oscillation_inertia(self):
        r1, r2 = calculate("synchrone", {"J": .1}), calculate("synchrone", {"J": .4})
        self.assertAlmostEqual(value(r1, "Fréquence des petites")/value(r2, "Fréquence des petites"), 2)

    def test_synchronous_potential_gradient(self):
        r = calculate("synchrone", {"load": .5})
        delta = np.radians(r["charts"][1]["series"][0]["x"])
        U = np.array(r["charts"][1]["series"][0]["y"])
        derivative = np.gradient(U, delta)
        expected = np.sin(delta)-.5
        np.testing.assert_allclose(derivative[2:-2], expected[2:-2], atol=6e-5)

    def test_asynchronous_zero_slip_no_rotor_current(self):
        r = calculate("asynchrone", {"slip": 0})
        self.assertEqual(value(r, "Courant rotorique"), 0)
        self.assertEqual(value(r, "Couple électromagnétique"), 0)
        self.assertEqual(value(r, "Pertes Joule au rotor"), 0)

    def test_asynchronous_signed_energy_partition(self):
        for slip in (-.2, .05, 1, 1.2):
            r = calculate("asynchrone", {"slip": slip})
            gap, rotor, mech = value(r, "Puissance d’entrefer"), value(r, "Pertes Joule au rotor"), value(r, "Puissance mécanique")
            self.assertAlmostEqual(rotor, slip*gap, places=8)
            self.assertAlmostEqual(mech, (1-slip)*gap, places=8)
            self.assertGreaterEqual(rotor, 0)
            self.assertAlmostEqual(value(r, "Résidu"), 0, places=8)

    def test_asynchronous_torque_times_rotor_speed(self):
        for slip in (-.1, .1, 1.1):
            r = calculate("asynchrone", {"slip": slip})
            power = value(r, "Couple électromagnétique")*r["scene"]["omega_rotor"]
            self.assertAlmostEqual(power, value(r, "Puissance mécanique"), places=8)

    def test_asynchronous_motoring_and_generating_torque(self):
        self.assertGreater(value(calculate("asynchrone", {"slip": .05}), "Couple"), 0)
        self.assertLess(value(calculate("asynchrone", {"slip": -.05}), "Couple"), 0)

    def test_asynchronous_speed_depends_on_pole_pairs(self):
        r1, r2 = calculate("asynchrone", {"poles": 1}), calculate("asynchrone", {"poles": 2})
        self.assertAlmostEqual(value(r1, "Vitesse synchrone")/value(r2, "Vitesse synchrone"), 2)


if __name__ == "__main__":
    unittest.main()
