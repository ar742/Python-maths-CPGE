"""Vérifications physiques : échelles, limites, unitarité et invariants."""
import json
import math
import unittest
import numpy as np

try:
    from . import modeles_ondes as m
    from .catalogue_ondes import LABS
except ImportError:
    import modeles_ondes as m
    from catalogue_ondes import LABS


def metric(result, prefix):
    return next(x["value"] for x in result["metrics"] if x["label"].startswith(prefix))


class YoungTests(unittest.TestCase):
    def test_zero_and_fourfold_peak(self):
        self.assertAlmostEqual(float(m.young_intensity(0, 600e-9, .5e-3, .04e-3, 2)), 4)

    def test_half_interfringe_destructive(self):
        lam, a, D = 600e-9, .5e-3, 2
        self.assertAlmostEqual(float(m.young_intensity(lam*D/(2*a), lam, a, .04e-3, D)), 0, places=13)

    def test_phase_average_equals_incoherent(self):
        x = np.linspace(-.01, .01, 173)
        r0 = m.young_intensity(x, 633e-9, .7e-3, .06e-3, 2.5, .3)
        rpi = m.young_intensity(x, 633e-9, .7e-3, .06e-3, 2.5, .3, np.pi)
        incoherent = m.young_intensity(x, 633e-9, .7e-3, .06e-3, 2.5, .3, visibility=0)
        np.testing.assert_allclose((r0+rpi)/2, incoherent, atol=2e-15)

    def test_double_distance_doubles_interfringe(self):
        first, second = m.calculate("young", {"distance": 1}), m.calculate("young", {"distance": 2})
        self.assertAlmostEqual(metric(second, "Interfrange")/metric(first, "Interfrange"), 2)

    def test_single_equals_ratio_zero(self):
        first, second = m.calculate("young", {"mode": "single"}), m.calculate("young", {"ratio": 0})
        np.testing.assert_allclose(first["scene"]["intensity"], second["scene"]["intensity"])

    def test_envelope_has_total_width_twice_halfwidth(self):
        result = m.calculate("young")
        self.assertAlmostEqual(metric(result, "Largeur"), 2*600e-9*2/.04e-3*1e3)


class GratingTests(unittest.TestCase):
    def test_orders_have_exact_maximum(self):
        np.testing.assert_allclose(m.grating_factor(np.arange(-5, 6), 1000), 1, atol=0)

    def test_first_zero_of_order(self):
        self.assertLess(float(m.grating_factor(3+1/500, 500)), 1e-24)

    def test_factor_periodic_for_integer_count(self):
        q = np.linspace(-.49, .49, 231)
        np.testing.assert_allclose(m.grating_factor(q, 127), m.grating_factor(q+3, 127), atol=5e-14)

    def test_missing_envelope_order(self):
        intensity = m.grating_intensity(math.asin(2*600e-9/2e-6), 600e-9, 2e-6, 500, .5)
        self.assertLess(float(intensity), 1e-28)

    def test_order_can_be_absent(self):
        result = m.calculate("reseau", {"pitch": 1, "incidence": 30, "order": 3})
        self.assertFalse(result["scene"]["order_present"])

    def test_resolving_power_scales_with_number(self):
        self.assertEqual(metric(m.calculate("reseau", {"count": 500, "order": 2}), "Pouvoir"), 1000)

    def test_fractional_slit_count_rejected(self):
        with self.assertRaises(ValueError): m.calculate("reseau", {"count": 50.5})


class DiffractionTests(unittest.TestCase):
    def test_apodization_normalized_at_origin(self):
        self.assertAlmostEqual(float(m.apodized_amplitude(0)), 1)

    def test_apodization_regular_at_formal_poles(self):
        self.assertAlmostEqual(float(m.apodized_amplitude(.5)), np.pi/4)
        self.assertAlmostEqual(float(m.apodized_amplitude(-.5)), np.pi/4)

    def test_apodization_first_zero(self):
        self.assertAlmostEqual(float(m.apodized_amplitude(1.5)), 0, places=14)

    def test_apodization_widens_central_lobe(self):
        uniform = m.calculate("diffraction", {"aperture": "rectangle"})
        apodized = m.calculate("diffraction", {"aperture": "apodized"})
        self.assertAlmostEqual(metric(apodized, "Largeur")/metric(uniform, "Largeur"), 1.5)

    def test_width_inverse_to_aperture(self):
        first = m.calculate("diffraction", {"width": .2})
        second = m.calculate("diffraction", {"width": .4})
        self.assertAlmostEqual(metric(first, "Largeur")/metric(second, "Largeur"), 2)


class PolarizationTests(unittest.TestCase):
    def test_retarder_is_unitary(self):
        field = np.array([.3+.4j, math.sqrt(.75)])
        for axis in (.1, .7, 2):
            for delay in (0, np.pi/2, np.pi, 3.4):
                out = m.jones_retarder(field, axis, delay)
                self.assertAlmostEqual(float(np.vdot(out, out).real), 1, places=14)

    def test_quarterwave_at_45_makes_circular(self):
        result = m.calculate("polarisation", {"input": "linear", "input_angle": 45, "axis": 0, "retardance": 90})
        s = np.array(result["scene"]["stokes"])
        np.testing.assert_allclose(s, [0, 0, 1], atol=3e-16)

    def test_circular_analysis_independent_angle(self):
        result = m.calculate("polarisation", {"input": "circular", "retardance": 0})
        np.testing.assert_allclose(result["charts"][0]["series"][0]["y"], .5, atol=5e-16)

    def test_malus_extinction(self):
        result = m.calculate("polarisation", {"input": "linear", "input_angle": 0, "retardance": 0, "analyzer": 90})
        self.assertLess(metric(result, "Transmission"), 1e-30)

    def test_pure_stokes_on_unit_sphere(self):
        result = m.calculate("polarisation", {"input": "elliptical", "input_angle": -31, "axis": 27, "retardance": 173})
        self.assertAlmostEqual(np.linalg.norm(result["scene"]["stokes"]), 1, places=14)

    def test_halfwave_reflects_linear_orientation(self):
        field = np.array([math.cos(.3), math.sin(.3)], complex)
        out = m.jones_retarder(field, 0, np.pi)
        np.testing.assert_allclose(out, [math.cos(.3), -math.sin(.3)], atol=2e-16)


class MichelsonTests(unittest.TestCase):
    def test_opd_on_axis_has_factor_two(self):
        self.assertEqual(float(m.michelson_opd(0, 0, .001, .2, 0, "rings")), .002)

    def test_equal_inclination_opd_decreases_radially(self):
        center = m.michelson_opd(0, 0, .001, .2, 0, "rings")
        outside = m.michelson_opd(.02, 0, .001, .2, 0, "rings")
        self.assertLess(outside, center)

    def test_contact_uniform_image(self):
        result = m.calculate("michelson", {"gap": 0, "mode": "rings"})
        np.testing.assert_allclose(result["scene"]["intensity"], 2)

    def test_wedge_interfringe_inverse_tilt(self):
        r1 = m.calculate("michelson", {"tilt": .1})
        r2 = m.calculate("michelson", {"tilt": .2})
        self.assertAlmostEqual(metric(r1, "Interfrange")/metric(r2, "Interfrange"), 2)

    def test_extreme_patterns_are_spatially_resolved(self):
        for mode in ("rings", "wedge"):
            result = m.calculate("michelson", {"mode": mode, "gap": 1000, "field": 6, "tilt": 2, "wavelength": 400})
            x = np.array(result["scene"]["x"])*1e-3
            y = np.array(result["scene"]["y"])*1e-3
            X, Y = np.meshgrid(x, y)
            opd = m.michelson_opd(X, Y, .001, .2, .002, mode)
            self.assertLessEqual(np.max(abs(np.diff(opd, axis=1)))/400e-9, .251)


class CoherenceTests(unittest.TestCase):
    def test_gaussian_fwhm_convention(self):
        linewidth = 20e9
        halfwidth = 2*np.log(2)/np.pi*m.C/linewidth
        self.assertAlmostEqual(float(m.gaussian_coherence(halfwidth, linewidth)), .5)

    def test_doublet_first_zero(self):
        difference = 500e9
        self.assertAlmostEqual(float(m.doublet_coherence(m.C/(2*difference), difference)), 0, places=14)

    def test_doublet_visibility_reappears(self):
        difference = 500e9
        self.assertAlmostEqual(abs(float(m.doublet_coherence(m.C/difference, difference))), 1)

    def test_independent_sources_have_no_fringe(self):
        result = m.calculate("coherence", {"spectrum": "independent"})
        np.testing.assert_allclose(result["scene"]["intensity"], 1)

    def test_point_source_has_spatial_coherence_one(self):
        result = m.calculate("coherence", {"source_width": 0})
        self.assertEqual(metric(result, "Facteur"), 1)

    def test_larger_spectral_width_reduces_coherence(self):
        self.assertGreater(float(m.gaussian_coherence(.003, 20e9)), float(m.gaussian_coherence(.003, 50e9)))


class FabryPerotTests(unittest.TestCase):
    def test_resonance_transmits_one(self):
        np.testing.assert_allclose(m.airy_transmission([-2, -1, 0, 1, 2], .99), 1, atol=1e-15)

    def test_zero_reflectivity_has_flat_transmission(self):
        np.testing.assert_allclose(m.airy_transmission(np.linspace(-2, 2, 51), 0), 1)

    def test_fsr_inverse_length(self):
        one, two = m.calculate("fabryperot", {"length": 1}), m.calculate("fabryperot", {"length": 2})
        self.assertAlmostEqual(metric(one, "Intervalle")/metric(two, "Intervalle"), 2)

    def test_exact_fwhm_is_half_height(self):
        R = .85
        result = m.calculate("fabryperot", {"reflectivity": R})
        fractional_width = metric(result, "Largeur")/metric(result, "Intervalle")
        self.assertAlmostEqual(float(m.airy_transmission(fractional_width/2, R)), .5)

    def test_low_reflectivity_has_no_half_height(self):
        result = m.calculate("fabryperot", {"reflectivity": .1})
        self.assertIsInstance(metric(result, "Largeur"), str)


class FourierTests(unittest.TestCase):
    def test_unitary_parseval(self):
        _, _, obj, transform, _, _ = m.fourier_field("cells", "identity", 20, 10)
        self.assertAlmostEqual(np.sum(abs(obj)**2), np.sum(abs(transform)**2), places=9)

    def test_identity_reconstructs_complex_phase(self):
        _, _, obj, _, _, out = m.fourier_field("phase", "identity", 20, 10)
        np.testing.assert_allclose(out, obj, atol=8e-16)

    def test_passive_mask_cannot_add_power(self):
        for filtering in ("lowpass", "highpass", "vertical", "horizontal"):
            _, _, obj, _, mask, out = m.fourier_field("cells", filtering, 12, 10)
            self.assertLessEqual(np.sum(abs(out)**2), np.sum(abs(obj)**2)*(1+1e-14))
            self.assertTrue(np.all((mask >= 0)&(mask <= 1)))

    def test_phase_object_uniform_input_intensity(self):
        _, _, obj, _, _, out = m.fourier_field("phase", "highpass", 8, 10)
        np.testing.assert_allclose(abs(obj)**2, 1, atol=4e-16)
        self.assertGreater(np.ptp(abs(out)**2), .01)

    def test_cutoff_beyond_nyquist_restores_image(self):
        # Le coin de la grille 2D atteint √2 νNyquist : coupure 80 > √2×50.
        _, _, obj, _, _, out = m.fourier_field("grid", "lowpass", 80, 10)
        np.testing.assert_allclose(out, obj, atol=1e-15)


class LaserTests(unittest.TestCase):
    def test_roundtrip_is_symplectic(self):
        matrix = m.cavity_matrix(.2, 2, 3)
        self.assertAlmostEqual(np.linalg.det(matrix), 1, places=14)

    def test_trace_stability_identity(self):
        L, k1, k2 = .27, 1.7, 3.2
        self.assertAlmostEqual(np.trace(m.cavity_matrix(L, k1, k2))/2, 2*(1-L*k1)*(1-L*k2)-1)

    def test_q_is_fixed_point(self):
        q = m.cavity_mode(.2, 2, 2, 633e-9)
        A, B, C_, D = m.cavity_matrix(.2, 2, 2).ravel()
        self.assertGreater(q.imag, 0)
        self.assertAlmostEqual(abs(q-(A*q+B)/(C_*q+D)), 0, places=14)

    def test_stable_does_not_imply_lasing(self):
        result = m.calculate("laser", {"gain": .05})
        self.assertTrue(result["scene"]["stable"])
        self.assertEqual(metric(result, "Puissance intracavité"), 0)

    def test_unstable_mode_not_extrapolated(self):
        result = m.calculate("laser", {"curvature1": 2, "curvature2": -5})
        self.assertFalse(result["scene"]["stable"])
        self.assertEqual(metric(result, "Puissance intracavité"), 0)

    def test_saturated_gain_equals_threshold(self):
        result = m.calculate("laser")
        power = metric(result, "Puissance intracavité")
        threshold = metric(result, "Gain seuil")
        self.assertAlmostEqual(result["params"]["gain"]/(1+power/result["params"]["saturation"]), threshold)


class GaussianTests(unittest.TestCase):
    def test_width_at_rayleigh(self):
        w0, lam = 50e-6, 633e-9
        zr = np.pi*w0*w0/lam
        self.assertAlmostEqual(float(m.gaussian_width(zr, w0, lam))/w0, math.sqrt(2))

    def test_power_conserved_in_two_transverse_dimensions(self):
        w0, lam, power = 50e-6, 633e-9, .002
        for z in (0, .012, -.02):
            w = float(m.gaussian_width(z, w0, lam))
            r = np.linspace(0, 5*w, 20001)
            integral_rule = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
            integrated = integral_rule(2*np.pi*r*m.gaussian_intensity(r, z, w0, lam, power), r)
            self.assertAlmostEqual(integrated/power, 1, places=7)

    def test_radius_definition_is_one_over_e_squared(self):
        w0, lam, power = 50e-6, 633e-9, .002
        self.assertAlmostEqual(float(m.gaussian_intensity(w0, 0, w0, lam, power)/m.gaussian_intensity(0, 0, w0, lam, power)), math.exp(-2))

    def test_gouy_zero_at_waist(self):
        result = m.calculate("gaussien", {"position": 0})
        self.assertEqual(metric(result, "Phase"), 0)
        self.assertEqual(metric(result, "Rayon de courbure"), "Front plan")

    def test_index_increases_rayleigh_length(self):
        one, two = m.calculate("gaussien", {"index": 1}), m.calculate("gaussien", {"index": 2})
        self.assertAlmostEqual(metric(two, "Longueur")/metric(one, "Longueur"), 2)


class AiryTests(unittest.TestCase):
    def test_origin_is_regular(self):
        for obstruction in (0, .2, .5):
            self.assertEqual(float(m.airy_amplitude(0, obstruction)), 1)

    def test_bessel_first_zero(self):
        self.assertLess(abs(float(m.bessel_j1(m.AIRY_ZERO))), 1e-14)

    def test_j1_known_value_and_oddness(self):
        self.assertAlmostEqual(float(m.bessel_j1(1)), .4400505857449335, places=14)
        self.assertAlmostEqual(float(m.bessel_j1(-2)), -float(m.bessel_j1(2)), places=14)

    def test_annular_first_minimum_changes(self):
        zero = m.first_airy_zero(.4)
        self.assertLess(zero, m.AIRY_ZERO)
        self.assertLess(abs(float(m.airy_amplitude(zero, .4))), 1e-13)

    def test_diameter_doubles_resolution(self):
        one, two = m.calculate("airy", {"diameter": 100}), m.calculate("airy", {"diameter": 200})
        self.assertAlmostEqual(metric(one, "Repère")/metric(two, "Repère"), 2)

    def test_two_coincident_sources_double_intensity(self):
        one = m.calculate("airy", {"separation": 0, "ratio": 1})
        # Le centre de la grille impaire est exactement sur l'axe.
        image = np.array(one["scene"]["intensity"])
        self.assertAlmostEqual(float(image[image.shape[0]//2, image.shape[1]//2]), 2)


class NonlinearTests(unittest.TestCase):
    def test_phase_matched_exact_solution(self):
        z, u, v = m.coupled_shg(.003, 800, 0)
        np.testing.assert_allclose(abs(u)**2, 1/np.cosh(800*z)**2, atol=2e-12)
        np.testing.assert_allclose(abs(v)**2, np.tanh(800*z)**2, atol=2e-12)

    def test_coupled_energy_conserved_with_mismatch(self):
        z, u, v = m.coupled_shg(.006, 700, 2100)
        self.assertLess(np.max(abs(abs(u)**2+abs(v)**2-1)), 5e-10)

    def test_mismatch_sign_does_not_change_intensities(self):
        _, up, vp = m.coupled_shg(.003, 300, 1000)
        _, um, vm = m.coupled_shg(.003, 300, -1000)
        np.testing.assert_allclose(abs(up)**2, abs(um)**2, atol=2e-15)
        np.testing.assert_allclose(abs(vp)**2, abs(vm)**2, atol=2e-15)

    def test_weak_conversion_matches_undepleted(self):
        z, _, v = m.coupled_shg(.001, 1, 2000)
        prediction = z**2*np.sinc(2000*z/(2*np.pi))**2
        np.testing.assert_allclose(abs(v)**2, prediction, rtol=1e-6, atol=1e-13)

    def test_photon_flux_has_factor_two(self):
        result = m.calculate("nonlineaire")
        self.assertAlmostEqual(metric(result, "Flux photonique"), metric(result, "Conversion à")/2)

    def test_saturation_does_not_exceed_one(self):
        result = m.calculate("nonlineaire", {"intensity": 2, "coefficient": 20, "length": 10, "mismatch": 0})
        self.assertLessEqual(metric(result, "Conversion à"), 1+1e-10)

    def test_small_prediction_not_clipped_when_invalid(self):
        result = m.calculate("nonlineaire", {"model": "small", "intensity": 2, "coefficient": 20, "length": 10, "mismatch": 0})
        self.assertGreater(metric(result, "Conversion à"), 1)


class ExportAndDomainTests(unittest.TestCase):
    def test_all_defaults_and_presets_are_finite_json(self):
        for lab in LABS:
            for params in [{}]+[preset["values"] for preset in lab["presets"]]:
                with self.subTest(lab=lab["id"], params=params):
                    result = m.calculate(lab["id"], params)
                    json.dumps(result, allow_nan=False)
                    self.assertTrue(result["steps"])
                    self.assertTrue(result["assumptions"])

    def test_joint_numeric_bounds_are_finite(self):
        for lab in LABS:
            for bound in ("min", "max"):
                params = {control["key"]: control[bound] for control in lab["controls"] if control["type"] == "range"}
                with self.subTest(lab=lab["id"], bound=bound):
                    json.dumps(m.calculate(lab["id"], params), allow_nan=False)

    def test_invalid_numeric_values_rejected(self):
        for invalid in (True, "600", None, float("nan"), float("inf"), 10**1000, 10):
            with self.subTest(invalid=type(invalid).__name__):
                with self.assertRaises(ValueError): m.calculate("young", {"wavelength": invalid})

    def test_unknown_key_and_invalid_select_rejected(self):
        with self.assertRaises(ValueError): m.calculate("young", {"unknown": 1})
        with self.assertRaises(ValueError): m.calculate("young", {"mode": "bad"})


if __name__ == "__main__":
    unittest.main()
