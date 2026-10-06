"""Lois physiques, limites et protocole numérique des laboratoires de fluides."""
import json
import math
import unittest

import numpy as np

from catalogue import LABS
from modeles import (G, MU0, TAU, acoustic_coefficients, blasius_solution,
                     calculate, darcy_factor, diffusion_profile, dispersion,
                     hartmann_profile, orbit_axes, rankine, taylor_green)


def result(lab, **p):
    return calculate({"lab": lab, "params": p})


def metrics(r):
    return {m["label"]: m["value"] for m in r["metrics"]}


def has_value(r, prefix):
    return next(m["value"] for m in r["metrics"] if m["label"].startswith(prefix))


class ProtocolTests(unittest.TestCase):
    def test_eighteen_unique_labs(self):
        self.assertEqual(len(LABS), 18)
        self.assertEqual(len({x["id"] for x in LABS}), 18)

    def test_all_presets_serializable(self):
        for lab in LABS:
            for preset in lab["presets"]:
                with self.subTest(lab=lab["id"], preset=preset["label"]):
                    r = result(lab["id"], **preset["values"])
                    json.dumps(r, allow_nan=False)
                    self.assertTrue(r["steps"] and r["assumptions"] and r["charts"])
                    for graph in r["charts"]:
                        for curve in graph["series"]:
                            self.assertEqual(len(curve["x"]), len(curve["y"]))

    def test_defaults_fit_native_slider(self):
        for lab in LABS:
            for c in lab["controls"]:
                if c["type"] == "range":
                    n = (c["value"]-c["min"])/c["step"]
                    self.assertAlmostEqual(n, round(n), places=7, msg=f"{lab['id']} {c['key']}")

    def test_every_individual_control_extreme_finite(self):
        for lab in LABS:
            for c in lab["controls"]:
                values = [o["value"] for o in c["options"]] if c["type"] == "select" else [c["min"], c["max"]]
                for value in values:
                    with self.subTest(lab=lab["id"], parameter=c["key"], value=value):
                        json.dumps(result(lab["id"], **{c["key"]: value}), allow_nan=False)

    def test_all_numeric_extremes_together_finite(self):
        for lab in LABS:
            for side in ("min", "max"):
                p = {c["key"]: c[side] for c in lab["controls"] if c["type"] == "range"}
                with self.subTest(lab=lab["id"], side=side):
                    json.dumps(result(lab["id"], **p), allow_nan=False)

    def test_field_dimensions(self):
        for lab in LABS:
            f = result(lab["id"]).get("field")
            if f:
                for key in ("u", "v", "scalar"):
                    self.assertEqual(np.shape(f[key]), (len(f["y"]), len(f["x"])))

    def test_nonfinite_and_boolean_rejected(self):
        for bad in (float("nan"), float("inf"), -float("inf"), True, "0.5", None, 10**400):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                result("cinematique", a=bad)

    def test_outside_bounds_and_unknown_rejected(self):
        for p in ({"a": 1.01}, {"a": -1.01}, {"viscosity": 1}, {"geometry": "other"}):
            with self.assertRaises(ValueError):
                result("cinematique", **p)
        with self.assertRaises(ValueError):
            calculate({"lab": "inconnu"})

    def test_integer_mode_required(self):
        with self.assertRaises(ValueError):
            result("conduit", m=1.5)
        with self.assertRaises(ValueError):
            result("conduit", n=-1)


class FoundationTests(unittest.TestCase):
    def test_solid_rotation_preserves_radius(self):
        curve = result("cinematique", a=0, U=0, omega=.8)["charts"][0]["series"][0]
        radius = np.hypot(curve["x"], curve["y"])
        np.testing.assert_allclose(radius, radius[0], rtol=1e-13)

    def test_extensional_flow_preserves_xy(self):
        curve = result("cinematique", a=.6, U=0, omega=0)["charts"][0]["series"][2]
        invariant = np.array(curve["x"])*curve["y"]
        np.testing.assert_allclose(invariant, invariant[0], rtol=1e-13)

    def test_streamfunction_constant_on_trajectory(self):
        a, w, U = .35, .55, .3
        curve = result("cinematique", a=a, omega=w, U=U)["charts"][0]["series"][2]
        x, y = np.array(curve["x"]), np.array(curve["y"])
        psi = U*y+a*x*y-w*(x*x+y*y)/2
        np.testing.assert_allclose(psi, psi[0], atol=2e-16)

    def test_critical_matrix_case_no_division_by_zero(self):
        r = result("cinematique", a=.5, omega=.5, U=0)
        curve = r["charts"][0]["series"][0]
        self.assertAlmostEqual(curve["x"][-1], 2*curve["x"][0])
        self.assertAlmostEqual(curve["y"][-1], curve["x"][0])

    def test_newtonian_rigid_rotation_no_stress(self):
        r = result("newtonien", a=0, shear=0, omega=8)
        self.assertEqual(has_value(r, "Dissipation"), 0)
        self.assertEqual(has_value(r, "Contrainte τxy"), 0)

    def test_newtonian_dissipation_invariant_to_rotation(self):
        for w in (-10, 0, 10):
            self.assertAlmostEqual(has_value(result("newtonien", eta=100, a=2, shear=3, omega=w), "Dissipation"), .1*(16+9))

    def test_dynamic_and_kinematic_viscosities(self):
        self.assertAlmostEqual(has_value(result("newtonien", eta=100, rho=1000), "Viscosité cinématique"), 1e-4)

    def test_hydrostatic_pressure_increment(self):
        self.assertAlmostEqual(has_value(result("hydrostatique", height=100, rho=1000), "Surpression"), 981000)

    def test_gas_density_and_pressure_same_scale(self):
        r = result("hydrostatique", mode="gas", height=5000)
        pressure, density = r["charts"][0]["series"][0], r["charts"][1]["series"][0]
        np.testing.assert_allclose(np.array(pressure["y"])*1000/np.array(density["y"]), 287.05*288)


class ShearAndBoundaryTests(unittest.TestCase):
    def test_couette_wall_conditions(self):
        r = result("couette", U0=.3, U1=-.2, G=700)
        u = r["scene"]["velocity"]
        self.assertAlmostEqual(u[0], .3)
        self.assertAlmostEqual(u[-1], -.2)

    def test_couette_power_balance_with_reverse_pressure(self):
        for gp in (-1500, 0, 1500):
            r = result("couette", U0=.6, U1=-.3, G=gp)
            self.assertAlmostEqual(has_value(r, "Résidu du bilan"), 0, places=12)
            self.assertGreater(has_value(r, "Dissipation"), 0)

    def test_couette_zero_flux_still_moving(self):
        r = result("couette", h=10, eta=100, U0=.1, U1=0, G=-600)
        self.assertAlmostEqual(has_value(r, "Débit"), 0, places=15)
        self.assertGreater(max(r["scene"]["velocity"]), 0)
        self.assertLess(min(r["scene"]["velocity"]), 0)

    def test_poiseuille_radius_fourth_power(self):
        q1 = has_value(result("poiseuille", R=1), "Débit")
        q2 = has_value(result("poiseuille", R=2), "Débit")
        self.assertAlmostEqual(q2/q1, 16)

    def test_poiseuille_flux_radial_integration(self):
        r = result("poiseuille")
        radii, speed = np.array(r["scene"]["coordinate"]), np.array(r["scene"]["velocity"])
        integral = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
        q = TAU*integral(radii*speed, radii)
        self.assertAlmostEqual(q/has_value(r, "Débit"), 1, places=4)
        self.assertAlmostEqual(has_value(r, "Vitesse axiale")/has_value(r, "Vitesse moyenne"), 2)

    def test_poiseuille_viscous_power(self):
        r = result("poiseuille", R=2, eta=20, dp=3000)
        rad, eta, length, dp = .002, .02, 1, 3000
        viscous = math.pi*dp**2*rad**4/(8*eta*length)
        self.assertAlmostEqual(has_value(r, "Puissance dissipée"), viscous)

    def test_halfspace_diffusion_similarity(self):
        y = np.linspace(0, .02, 101)
        np.testing.assert_allclose(diffusion_profile(y, .5, 1e-5, .3), diffusion_profile(2*y, .5, 1e-5, 1.2), atol=1e-15)

    def test_halfspace_diffusion_equation(self):
        y = np.array([.001, .002, .003])
        nu, t, dy, dt = 1e-5, .2, 1e-6, 1e-5
        ut = (diffusion_profile(y, 1, nu, t+dt)-diffusion_profile(y, 1, nu, t-dt))/(2*dt)
        uyy = (diffusion_profile(y+dy, 1, nu, t)-2*diffusion_profile(y, 1, nu, t)+diffusion_profile(y-dy, 1, nu, t))/dy**2
        np.testing.assert_allclose(ut, nu*uyy, rtol=2e-6)

    def test_finite_diffusion_boundary_and_final_state(self):
        y = np.linspace(0, .01, 101)
        for t in (.001, .2, 100):
            u = diffusion_profile(y, .5, 1e-5, t, .01)
            self.assertAlmostEqual(u[0], .5)
            self.assertAlmostEqual(u[-1], 0)
            self.assertGreaterEqual(min(u), -1e-14)
        np.testing.assert_allclose(diffusion_profile(y, .5, 1e-5, 100, .01), .5*(1-y/.01), atol=1e-13)

    def test_finite_diffusion_interior_equation(self):
        y = np.array([.002, .004, .006])
        nu, t, h, dy, dt = 1e-5, .6, .01, 1e-6, 1e-5
        ut = (diffusion_profile(y, 1, nu, t+dt, h)-diffusion_profile(y, 1, nu, t-dt, h))/(2*dt)
        uyy = (diffusion_profile(y+dy, 1, nu, t, h)-2*diffusion_profile(y, 1, nu, t, h)+diffusion_profile(y-dy, 1, nu, t, h))/dy**2
        np.testing.assert_allclose(ut, nu*uyy, rtol=3e-6)

    def test_diffusion_images_and_fourier_match(self):
        y = np.linspace(0, .01, 101)
        left = diffusion_profile(y, 1, 1e-5, .299999, .01)
        right = diffusion_profile(y, 1, 1e-5, .300001, .01)
        np.testing.assert_allclose(left, right, atol=2e-6)

    def test_blasius_shooting_reference_and_boundary(self):
        xi, f = blasius_solution()
        self.assertAlmostEqual(f[0, 2], .3320573362, places=8)
        self.assertAlmostEqual(f[-1, 1], 1, places=9)
        self.assertEqual(f[0, 0], 0)
        self.assertEqual(f[0, 1], 0)
        self.assertTrue(np.all(np.diff(f[:, 1]) >= -1e-14))

    def test_blasius_displacement_and_momentum(self):
        r = result("blasius", U=5, nu=15, x=.3)
        scale = math.sqrt(15e-6*.3/5)*1000
        self.assertAlmostEqual(has_value(r, "Épaisseur de déplacement")/scale, 1.720787, places=4)
        self.assertAlmostEqual(has_value(r, "Épaisseur de quantité")/scale, .6641147, places=4)

    def test_blasius_thickness_square_root_x(self):
        r1, r2 = result("blasius", x=.25), result("blasius", x=1)
        self.assertAlmostEqual(has_value(r2, "Épaisseur à 99")/has_value(r1, "Épaisseur à 99"), 2)
        self.assertAlmostEqual(has_value(r1, "Coefficient de frottement")/has_value(r2, "Coefficient de frottement"), 2)


class ForcesAndEnergyTests(unittest.TestCase):
    def test_darcy_laminar_returns_poiseuille(self):
        f, regime = darcy_factor(1000, .01)
        self.assertAlmostEqual(f, .064)
        self.assertEqual(regime, "laminaire")

    def test_colebrook_residual(self):
        for re, eps in ((10000, 0), (100000, .001), (1e6, .01)):
            factor, _ = darcy_factor(re, eps)
            residual = 1/math.sqrt(factor)+2*math.log10(eps/3.7+2.51/(re*math.sqrt(factor)))
            self.assertAlmostEqual(residual, 0, places=10)

    def test_venturi_bernoulli_sign(self):
        r = result("bernoulli", Q=2, D1=5, D2=2, L=0, K=0, dz=0, pump=0)
        u1, u2 = has_value(r, "Vitesse à"), has_value(r, "Vitesse dans")
        self.assertAlmostEqual(has_value(r, "Écart de pression"), 1000*(u1*u1-u2*u2)/2)
        self.assertLess(has_value(r, "Écart de pression"), 0)

    def test_pump_efficiency_converts_electric_power(self):
        r = result("bernoulli", Q=1, pump=100, efficiency=.5, L=0, dz=0, K=0, D1=3, D2=3)
        self.assertAlmostEqual(has_value(r, "Écart de pression"), .5*100/.001)

    def test_sphere_correlation_stokes_limit(self):
        r = result("sphere", R=.005, U=.001, eta=2000)
        self.assertAlmostEqual(has_value(r, "Traînée Schiller")/has_value(r, "Traînée Stokes"), 1, delta=1e-4)

    def test_sphere_terminal_force_balance(self):
        r = result("sphere", R=.5, eta=1)
        vt, re = has_value(r, "Vitesse terminale"), has_value(r, "Reynolds terminal")
        force = 6*math.pi*.001*.0005*vt*(1+.15*re**.687)
        self.assertAlmostEqual(force/has_value(r, "Poids corrigé"), 1, places=12)

    def test_sphere_does_not_extrapolate_drag_crisis(self):
        r = result("sphere", R=5, U=1, eta=1)
        self.assertGreater(has_value(r, "Reynolds imposé"), 1000)
        self.assertIsInstance(has_value(r, "Traînée Schiller"), str)

    def test_neutrally_buoyant_sphere_no_fall(self):
        r = result("sphere", rho=1000, rho_s=1000)
        self.assertAlmostEqual(has_value(r, "Vitesse terminale"), 0, places=12)
        self.assertEqual(max(abs(v) for v in r["charts"][1]["series"][0]["y"]), 0)

    def test_rankine_velocity_pressure_continuous(self):
        eps = 1e-8
        v, p = rankine(np.array([2-eps, 2, 2+eps]), 2, 3, 1.2)
        np.testing.assert_allclose(v, 6, rtol=1e-8)
        np.testing.assert_allclose(p, -21.6, rtol=3e-8)

    def test_rankine_euler_radial_balance(self):
        r = np.array([.3, .8, 2., 3.])
        dr = 1e-6
        v, _ = rankine(r, 1, 2, 1000)
        _, pp = rankine(r+dr, 1, 2, 1000)
        _, pm = rankine(r-dr, 1, 2, 1000)
        np.testing.assert_allclose((pp-pm)/(2*dr), 1000*v*v/r, rtol=1e-9)

    def test_magnus_integrated_force_and_sign(self):
        for circulation in (-5, 0, 5):
            r = result("magnus", Gamma=circulation, U=5, rho=1.2)
            self.assertAlmostEqual(has_value(r, "Force Fx"), 0, places=12)
            self.assertAlmostEqual(has_value(r, "Force Fy"), -1.2*5*circulation, places=11)

    def test_magnus_obstacle_mask_finite_and_stationary(self):
        f = result("magnus")["field"]
        X, Y = np.meshgrid(f["x"], f["y"])
        inside = X*X+Y*Y <= .2**2
        for key in ("u", "v", "scalar"):
            self.assertTrue(np.isfinite(f[key]).all())
            self.assertTrue(np.all(np.array(f[key])[inside] == 0))


class WaveTests(unittest.TestCase):
    def test_shallow_water_nondispersive_limit(self):
        k, h = .01, .1
        omega, group = dispersion(k, h, 0, 1000)
        reference = math.sqrt(G*h)
        self.assertAlmostEqual(omega/k/reference, 1, places=6)
        self.assertAlmostEqual(group/reference, 1, places=6)

    def test_deep_gravity_group_half_phase(self):
        omega, group = dispersion(2, 10, 0, 1000)
        self.assertAlmostEqual(group/(omega/2), .5, places=12)

    def test_capillary_group_three_halves_phase(self):
        k = 1e6
        omega, group = dispersion(k, 1, .072, 1000)
        self.assertAlmostEqual(group/(omega/k), 1.5, places=6)

    def test_group_is_dispersion_derivative(self):
        for k in (.1, 10, 1000):
            dk = k*1e-5
            omega, group = dispersion(k, .2, .072, 1000)
            numerical = (dispersion(k+dk, .2, .072, 1000)[0]-dispersion(k-dk, .2, .072, 1000)[0])/(2*dk)
            self.assertAlmostEqual(group/numerical, 1, places=8)

    def test_orbit_bottom_and_deep_stability(self):
        for k, h in ((1, 1), (2000, 10)):
            horizontal, vertical = orbit_axes(k, h, -h, .01)
            self.assertEqual(vertical, 0)
            self.assertTrue(math.isfinite(horizontal))
        hor, vert = orbit_axes(2, 10, 0, .01)
        self.assertAlmostEqual(hor/vert, 1, places=12)

    def test_acoustic_energy_conservation_all_impedances(self):
        for z1, z2 in ((408, 1500000), (1500000, 408), (500, 500)):
            co = acoustic_coefficients(z1, z2)
            self.assertAlmostEqual(co["R"]+co["T"], 1, places=14)
            self.assertAlmostEqual(co["tp"]**2*z1/z2, co["T"])

    def test_acoustic_pressure_velocity_continuity(self):
        for z1, z2 in ((408, 1500000), (1500000, 408)):
            co = acoustic_coefficients(z1, z2)
            self.assertAlmostEqual(1+co["rp"], co["tp"])
            self.assertAlmostEqual((1-co["rp"])/z1, co["tp"]/z2)
            self.assertEqual(co["rv"], -co["rp"])

    def test_equal_media_no_reflection(self):
        r = result("acoustique", rho2=1.2, c2=340)
        self.assertEqual(has_value(r, "Réflexion de pression"), 0)
        self.assertEqual(has_value(r, "Fraction énergétique transmise"), 1)

    def test_duct_plane_mode_no_cutoff(self):
        r = result("conduit", m=0, n=0)
        self.assertEqual(has_value(r, "Fréquence de coupure"), 0)
        self.assertAlmostEqual(has_value(r, "Vitesse de phase"), 340)
        self.assertAlmostEqual(has_value(r, "Vitesse de groupe"), 340)

    def test_duct_phase_group_product(self):
        r = result("conduit", m=1, n=1, frequency=2000)
        self.assertAlmostEqual(has_value(r, "Vitesse de phase")*has_value(r, "Vitesse de groupe"), 340**2)
        self.assertGreater(has_value(r, "Vitesse de phase"), 340)
        self.assertLess(has_value(r, "Vitesse de groupe"), 340)

    def test_duct_evanescent_decay(self):
        r = result("conduit", m=1, n=0, frequency=300)
        self.assertTrue(r["scene"]["evanescent"])
        curve = r["charts"][1]["series"][0]
        self.assertTrue(np.all(np.diff(curve["y"]) < 0))
        self.assertEqual(has_value(r, "Vitesse de groupe"), "Pas de propagation")

    def test_diffraction_no_zero_for_pdf_data(self):
        r = result("diffraction", a=1, frequency=25000, c=340)
        self.assertIsInstance(has_value(r, "Premier zéro"), str)
        self.assertIsInstance(has_value(r, "Approximation"), str)

    def test_diffraction_exact_zero_and_symmetry(self):
        r = result("diffraction", a=4, frequency=25000, c=340)
        self.assertAlmostEqual(has_value(r, "Premier zéro"), math.degrees(math.asin(.0136/.04)))
        intensity = r["charts"][0]["series"][0]["y"]
        np.testing.assert_allclose(intensity, intensity[::-1], atol=2e-15)
        self.assertEqual(intensity[len(intensity)//2], 1)


class BridgeTests(unittest.TestCase):
    def test_thermo_adiabatic_vs_isothermal(self):
        r = result("thermo", gamma=1.4)
        self.assertAlmostEqual(has_value(r, "Célérité isentropique")/has_value(r, "Célérité isotherme"), math.sqrt(1.4))
        self.assertAlmostEqual(has_value(r, "Compressibilité isotherme")/has_value(r, "Compressibilité isentropique"), 1.4)

    def test_ideal_gas_sound_independent_of_pressure(self):
        r1, r2 = result("thermo", p=50), result("thermo", p=200)
        self.assertEqual(has_value(r1, "Célérité isentropique"), has_value(r2, "Célérité isentropique"))
        self.assertAlmostEqual(has_value(r2, "Masse volumique")/has_value(r1, "Masse volumique"), 4)

    def test_thermal_diffusion_sqrt_frequency(self):
        r1, r2 = result("thermo", frequency=100), result("thermo", frequency=400)
        self.assertAlmostEqual(has_value(r1, "Longueur thermique")/has_value(r2, "Longueur thermique"), 2)

    def test_hartmann_zero_field_poiseuille_limit(self):
        y = np.linspace(-.002, .002, 101)
        u, du, ha = hartmann_profile(y, .002, 1000, .01, 1e6, 0)
        self.assertEqual(ha, 0)
        np.testing.assert_allclose(u, 1000*(.002**2-y*y)/(.02), atol=1e-15)
        np.testing.assert_allclose(du, -1000*y/.01)

    def test_hartmann_ode_and_walls(self):
        h, eta, sigma, B, gp, dy = .002, .01, 1e6, .2, 1000, 1e-7
        y = np.array([-.001, 0., .001])
        u, _, _ = hartmann_profile(y, h, gp, eta, sigma, B)
        up = hartmann_profile(y+dy, h, gp, eta, sigma, B)[0]
        um = hartmann_profile(y-dy, h, gp, eta, sigma, B)[0]
        residual = eta*(up-2*u+um)/dy**2-sigma*B*B*u+gp
        np.testing.assert_allclose(residual, 0, atol=.00003)
        walls = hartmann_profile(np.array([-h, h]), h, gp, eta, sigma, B)[0]
        np.testing.assert_allclose(walls, 0, atol=1e-15)

    def test_hartmann_energy_balance(self):
        for B in (0, .001, .2, 2):
            r = result("mhd", mode="hartmann", B=B)
            power = has_value(r, "Puissance de pression")
            self.assertAlmostEqual((has_value(r, "Dissipation visqueuse")+has_value(r, "Dissipation Joule"))/power, 1, places=8)

    def test_hartmann_lorentz_brakes_at_fixed_gradient(self):
        speeds = [has_value(result("mhd", B=B), "Vitesse moyenne") for B in (0, .1, .2, 1)]
        self.assertTrue(all(a > b for a, b in zip(speeds, speeds[1:])))

    def test_alfven_equipartition(self):
        r = result("mhd", mode="alfven", B=.2, rho=1000)
        self.assertAlmostEqual(has_value(r, "Vitesse d’Alfvén"), .2/math.sqrt(MU0*1000))
        self.assertAlmostEqual(has_value(r, "Énergie cinétique moyenne"), has_value(r, "Énergie magnétique moyenne"), places=12)

    def test_alfven_zero_field_no_propagation(self):
        r = result("mhd", mode="alfven", B=0)
        self.assertEqual(r["scene"]["omega"], 0)
        self.assertEqual(has_value(r, "Énergie cinétique"), 0)

    def test_taylor_green_divergence_and_navier_stokes(self):
        x, y, t, U, k, nu, rho, step = .2, .31, .7, 1.3, 2.4, .02, 1000, 1e-5
        u, v, _, _ = taylor_green(x, y, t, U, k, nu, rho)
        xp, xm = taylor_green(x+step, y, t, U, k, nu, rho), taylor_green(x-step, y, t, U, k, nu, rho)
        yp, ym = taylor_green(x, y+step, t, U, k, nu, rho), taylor_green(x, y-step, t, U, k, nu, rho)
        tp, tm = taylor_green(x, y, t+step, U, k, nu, rho), taylor_green(x, y, t-step, U, k, nu, rho)
        derivatives_x = (np.array(xp[:2])-xm[:2])/(2*step)
        derivatives_y = (np.array(yp[:2])-ym[:2])/(2*step)
        self.assertAlmostEqual(derivatives_x[0]+derivatives_y[1], 0, places=9)
        time_deriv = (np.array(tp[:2])-tm[:2])/(2*step)
        lap = (np.array(xp[:2])+xm[:2]+yp[:2]+ym[:2]-4*np.array([u, v]))/step**2
        gradp = np.array([xp[2]-xm[2], yp[2]-ym[2]])/(2*step)
        residual = time_deriv+u*derivatives_x+v*derivatives_y+gradp/rho-nu*lap
        np.testing.assert_allclose(residual, 0, atol=1e-7)

    def test_taylor_green_energy_decay_rate(self):
        r = result("navier", nu=.02, time=3)
        energy, diss = has_value(r, "Énergie cinétique"), has_value(r, "Dissipation moyenne")
        self.assertAlmostEqual(diss/energy, 4*.02*(TAU/2)**2)

    def test_euler_energy_conservation(self):
        r = result("navier", nu=0)
        energies = r["charts"][0]["series"][0]["y"]
        self.assertEqual(min(energies), max(energies))
        self.assertEqual(has_value(r, "Dissipation"), 0)


if __name__ == "__main__":
    unittest.main()
