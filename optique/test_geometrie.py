"""Vérifications de lois physiques, de cas limites et du contrat public des TP."""
import json
import math
import unittest

import numpy as np

from catalogue_geometrie import LABS, LAB_BY_ID
from modeles_geometrie import (
    C, DEG, calculate, translation, lens, thin_image, fresnel_unpolarized, fresnel_amplitudes,
    bessel_positions, bessel_uncertainty, afocal_matrix, microscope_setup,
    fiber_parameters, folded_fiber_y, mirage_analytic, mirage_integrate,
    mirage_ground_intersection, cauchy_index, rainbow_deviation, rainbow_stationary,
    rainbow_path, refract_vector, reflect_vector, prism_deviation, prism_path,
    mirror_surface, mirror_axis_intercept, fermat_crossing, fermat_path,
    fermat_derivative,
)


def defaults(lab):
    return {control["key"]: control["value"] for control in LAB_BY_ID[lab]["controls"]}


def number(result, begins):
    return next(item["value"] for item in result["metrics"] if item["label"].startswith(begins))


class SnellTests(unittest.TestCase):
    def test_normal_incidence_has_four_percent_reflection(self):
        R,T,_=fresnel_unpolarized(1,1.5,0)
        self.assertAlmostEqual(R,.04,places=14)
        self.assertAlmostEqual(T,.96,places=14)

    def test_energy_conservation_including_total_reflection(self):
        for n1,n2 in [(1,1.5),(1.5,1),(1.7,1.9)]:
            for angle in np.linspace(0,80,41):
                R,T,_=fresnel_unpolarized(n1,n2,angle*DEG)
                self.assertAlmostEqual(R+T,1,places=14)
                self.assertGreaterEqual(R,0)
                self.assertLessEqual(R,1+1e-14)

    def test_equal_indices_do_not_reflect(self):
        for angle in [0,30,70]:
            R,T,_=fresnel_unpolarized(1.5,1.5,angle*DEG)
            self.assertAlmostEqual(R,0,places=13)
            self.assertAlmostEqual(T,1,places=13)

    def test_critical_angle_has_zero_normal_transmission(self):
        R,T,_=fresnel_unpolarized(1.5,1,math.asin(1/1.5))
        self.assertAlmostEqual(R,1,places=12)
        self.assertAlmostEqual(T,0,places=12)

    def test_total_reflection_has_imaginary_normal_wave_number(self):
        R,T,ct=fresnel_unpolarized(1.5,1,60*DEG)
        self.assertGreater(ct.imag,0)
        self.assertAlmostEqual(R,1,places=13)
        self.assertAlmostEqual(T,0,places=13)

    def test_scene_obeys_snell_and_reflection(self):
        result=calculate("snell",{"angle":37})
        incoming=np.array(result["scene"]["paths"][0]["points"])
        reflected=np.array(result["scene"]["paths"][1]["points"])
        transmitted=np.array(result["scene"]["paths"][2]["points"])
        ui=incoming[-1]-incoming[0]
        ur=reflected[-1]-reflected[0]
        ut=transmitted[-1]-transmitted[0]
        self.assertAlmostEqual(ui[1]/np.linalg.norm(ui),ur[1]/np.linalg.norm(ur),places=14)
        self.assertAlmostEqual(ui[1]/np.linalg.norm(ui),1.5*ut[1]/np.linalg.norm(ut),places=14)

    def test_brewster_annuls_only_tm_reflection(self):
        rs,rp,_=fresnel_amplitudes(1,1.5,math.atan(1.5))
        self.assertLess(abs(rp),1e-13)
        self.assertGreater(abs(rs),.1)


class LensTests(unittest.TestCase):
    def test_real_inverted_image(self):
        self.assertAlmostEqual(thin_image(200,80),400/3,places=12)
        result=calculate("lentille",{})
        self.assertLess(number(result,"Grandissement"),0)

    def test_virtual_magnified_image(self):
        self.assertAlmostEqual(thin_image(50,80),-400/3,places=12)
        self.assertGreater(number(calculate("lentille",{"distance":50}),"Grandissement"),1)

    def test_divergent_lens_virtual_reduced_image(self):
        q=thin_image(200,-80)
        self.assertLess(q,0)
        self.assertLess(-q/200,1)

    def test_object_in_focal_plane_has_parallel_emergent_rays(self):
        result=calculate("lentille",{"distance":80,"focal":80})
        self.assertIsNone(thin_image(80,80))
        slopes=[]
        for item in result["scene"]["paths"]:
            a,b=np.array(item["points"][-2:])
            slopes.append((b[1]-a[1])/(b[0]-a[0]))
        np.testing.assert_allclose(slopes,slopes[0],atol=1e-14)

    def test_all_emergent_rays_meet_the_conjugate_image(self):
        for params in [{},{"distance":50},{"type":"divergente"}]:
            result=calculate("lentille",params)
            q=number(result,"p′")
            gamma=number(result,"Grandissement")
            for item in result["scene"]["paths"]:
                if item["dashed"]:
                    continue
                a,b=np.array(item["points"][-2:])
                slope=(b[1]-a[1])/(b[0]-a[0])
                self.assertAlmostEqual(a[1]+q*slope,gamma*15,places=10)

    def test_gaussian_optical_matrices_are_unimodular(self):
        for f in [-80,30,125]:
            self.assertAlmostEqual(np.linalg.det(lens(f)),1)
            self.assertAlmostEqual(np.linalg.det(translation(150)@lens(f)),1)

    def test_translation_and_lens_have_reverse_maps(self):
        np.testing.assert_allclose(translation(-137)@translation(137),np.eye(2),atol=1e-14)
        np.testing.assert_allclose(lens(-80)@lens(80),np.eye(2),atol=1e-14)


class BesselTests(unittest.TestCase):
    def test_both_positions_focus_on_same_screen(self):
        s1,s2,d=bessel_positions(800,120)
        for s in [s1,s2]:
            self.assertAlmostEqual(1/s+1/(800-s),1/120,places=14)
        self.assertAlmostEqual(s2-s1,d,delta=1e-10)

    def test_silbermann_is_double_root(self):
        self.assertEqual(bessel_positions(480,120),(240,240,0))

    def test_distance_below_four_focal_has_no_solution(self):
        self.assertIsNone(bessel_positions(400,120))

    def test_reciprocal_magnifications(self):
        s1,s2,_=bessel_positions(800,120)
        self.assertAlmostEqual((-(800-s1)/s1)*(-(800-s2)/s2),1,places=13)

    def test_focal_recovered_across_suitable_bench_lengths(self):
        for D in [480,600,800,1500]:
            gap=bessel_positions(D,120)[2]
            self.assertAlmostEqual((D*D-gap*gap)/(4*D),120,places=11)

    def test_uncertainty_matches_local_numerical_sensitivity(self):
        D,d=800,bessel_positions(800,120)[2]
        def f(distance,gap):
            return (distance*distance-gap*gap)/(4*distance)
        eps=1e-3
        dD=(f(D+eps,d)-f(D-eps,d))/(2*eps)
        dd=(f(D,d+eps)-f(D,d-eps))/(2*eps)
        self.assertAlmostEqual(bessel_uncertainty(D,d,1.2,.8),math.hypot(dD*1.2,dd*.8),places=9)


class InstrumentsTests(unittest.TestCase):
    def test_kepler_lunette_is_afocal_at_sum_of_focals(self):
        matrix=afocal_matrix(1000,25,1025)
        self.assertAlmostEqual(matrix[1,0],0,places=14)
        self.assertAlmostEqual(matrix[1,1],-40,places=13)

    def test_lunette_defocus_has_expected_vergence(self):
        matrix=afocal_matrix(1000,25,1030)
        self.assertAlmostEqual(matrix[1,0],5/(1000*25),places=14)

    def test_lunette_matrix_preserves_optical_phase_area(self):
        for d in [1005,1025,1045]:
            self.assertAlmostEqual(np.linalg.det(afocal_matrix(1000,25,d)),1,places=11)

    def test_objective_diameter_improves_resolution_independently_of_eyepiece(self):
        first=calculate("telescope",{"diameter":100,"eyepiece":25})
        second=calculate("telescope",{"diameter":200,"eyepiece":10})
        self.assertAlmostEqual(number(first,"Rayleigh"),2*number(second,"Rayleigh"),places=12)

    def test_lunette_afocal_scene_really_has_parallel_output(self):
        result=calculate("telescope",{})
        self.assertLess(number(result,"Écart angulaire"),1e-13)

    def test_lunette_exit_pupil_is_image_of_objective(self):
        result=calculate("telescope",{})
        self.assertAlmostEqual(number(result,"Diamètre de la pupille"),2.5,places=13)
        q=number(result,"Pupille de sortie après")
        self.assertAlmostEqual(1/1025+1/q,1/25,places=13)

    def test_microscope_nominal_object_conjugacy(self):
        d,v,s=microscope_setup(8,25,160)
        self.assertAlmostEqual(thin_image(s,8),v,places=10)
        self.assertAlmostEqual(v/s,20,places=12)
        self.assertEqual(d,193)

    def test_microscope_nominal_output_is_parallel(self):
        result=calculate("microscope",{})
        self.assertLess(number(result,"Écart angulaire"),1e-12)
        self.assertAlmostEqual(number(result,"Grossissement"),-200,places=12)

    def test_microscope_object_defocus_requires_accommodation(self):
        result=calculate("microscope",{"defocus":20})
        self.assertGreater(number(result,"Écart angulaire"),1e-4)

    def test_microscope_resolution_is_inverse_numerical_aperture(self):
        r1=number(calculate("microscope",{"NA":.1}),"Rayleigh")
        r2=number(calculate("microscope",{"NA":.2}),"Rayleigh")
        self.assertAlmostEqual(r1,2*r2,places=12)


class EyeTests(unittest.TestCase):
    def test_quarter_meter_object_requires_four_diopters(self):
        result=calculate("oeil",{"distance":.25,"accommodation":4})
        self.assertLess(abs(number(result,"Correction supplémentaire")),1e-12)
        self.assertLess(number(result,"Diamètre du flou"),1e-10)

    def test_myopic_focus_lies_before_retina(self):
        result=calculate("oeil",{"distance":10,"error":3})
        self.assertLess(number(result,"Position du foyer"),17)

    def test_divergent_correction_restores_myopic_focus(self):
        result=calculate("oeil",{"distance":10,"error":3,"correction":-3,"accommodation":.1})
        self.assertAlmostEqual(number(result,"Position du foyer"),17,places=12)

    def test_hyperopic_focus_lies_behind_retina(self):
        result=calculate("oeil",{"distance":10,"error":-3})
        self.assertGreater(number(result,"Position du foyer"),17)

    def test_geometric_blur_scales_with_pupil_diameter(self):
        a=number(calculate("oeil",{"pupil":2,"error":2}),"Diamètre du flou")
        b=number(calculate("oeil",{"pupil":4,"error":2}),"Diamètre du flou")
        self.assertAlmostEqual(b,2*a,places=11)

    def test_airy_diameter_scales_inversely_with_pupil_diameter(self):
        a=number(calculate("oeil",{"pupil":2}),"Diamètre jusqu'au")
        b=number(calculate("oeil",{"pupil":4}),"Diamètre jusqu'au")
        self.assertAlmostEqual(a,2*b,places=12)


class FiberTests(unittest.TestCase):
    def test_acceptance_combines_both_snell_interfaces(self):
        p=fiber_parameters(1.48,1.46,25e-6,850e-9,1000)
        alpha=math.asin(p["NA"])
        theta=math.asin(math.sin(alpha)/1.48)
        self.assertAlmostEqual(math.cos(theta),1.46/1.48,places=14)

    def test_geometric_delay_extremes(self):
        p=fiber_parameters(1.48,1.46,25e-6,850e-9,1000)
        self.assertAlmostEqual(p["delay_max"],p["delay_min"]/math.cos(p["internal_max"]),places=15)

    def test_delay_scales_with_length(self):
        first=fiber_parameters(1.48,1.46,25e-6,850e-9,1000)
        second=fiber_parameters(1.48,1.46,25e-6,850e-9,2000)
        self.assertAlmostEqual(second["delay_max"]-second["delay_min"],2*(first["delay_max"]-first["delay_min"]),places=15)

    def test_cladding_not_below_core_has_no_guiding(self):
        p=fiber_parameters(1.44,1.55,25e-6,850e-9,1000)
        self.assertFalse(p["guiding"])
        self.assertEqual(p["NA"],0)
        json.dumps(calculate("fibre",{"core":1.44,"cladding":1.55}),allow_nan=False)

    def test_folded_path_has_exact_reflection_vertices(self):
        a=25
        angle=.1
        xs=np.array([0,a/math.tan(angle),3*a/math.tan(angle),5*a/math.tan(angle)])
        np.testing.assert_allclose(folded_fiber_y(xs,a,angle),[0,a,-a,a],atol=1e-11)

    def test_normalized_frequency_scales_with_radius_and_inverse_wavelength(self):
        first=fiber_parameters(1.48,1.46,10e-6,850e-9,1000)
        second=fiber_parameters(1.48,1.46,20e-6,1700e-9,1000)
        self.assertAlmostEqual(first["V"],second["V"],places=13)

    def test_selected_launch_outside_acceptance_is_not_marked_guided(self):
        self.assertFalse(calculate("fibre",{"angle":25})["scene"]["guided"])
        self.assertTrue(calculate("fibre",{"angle":8})["scene"]["guided"])


class MirageTests(unittest.TestCase):
    def test_parabola_has_the_second_derivative_required_by_ray_equation(self):
        a,z,theta=20000,2,-.5*DEG
        eps=.1
        second=float((mirage_analytic(300+eps,a,z,theta)-2*mirage_analytic(300,a,z,theta)+mirage_analytic(300-eps,a,z,theta))/eps**2)
        self.assertAlmostEqual(second,1/(2*(a+z)*math.cos(theta)**2),places=11)

    def test_rk4_matches_independent_analytic_solution(self):
        xs,states,_=mirage_integrate(20000,2,-.5*DEG,1000)
        np.testing.assert_allclose(states[:,0],mirage_analytic(xs,20000,2,-.5*DEG),atol=1e-10,rtol=1e-12)

    def test_conserved_eikonal_horizontal_momentum(self):
        xs,states,_=mirage_integrate(1000,20,2*DEG,3000)
        momentum=np.sqrt(1+states[:,0]/1000)/np.sqrt(1+states[:,1]**2)
        np.testing.assert_allclose(momentum,momentum[0],atol=1e-9,rtol=1e-9)

    def test_index_scale_does_not_change_geometric_trajectory(self):
        a=calculate("mirage",{"n0":1.0001})
        b=calculate("mirage",{"n0":1.01})
        np.testing.assert_allclose(a["scene"]["paths"][0]["points"],b["scene"]["paths"][0]["points"],atol=0,rtol=0)

    def test_ray_stops_at_first_ground_contact(self):
        xs,states,ground=mirage_integrate(100000,2,-DEG,1000)
        self.assertIsNotNone(ground)
        self.assertAlmostEqual(xs[-1],ground,places=10)
        self.assertAlmostEqual(states[-1,0],0,places=10)
        self.assertGreaterEqual(states[:,0].min(),-1e-10)

    def test_ground_solution_uses_first_not_second_root(self):
        ground=mirage_ground_intersection(100000,2,-DEG)
        self.assertLess(ground,150)
        self.assertAlmostEqual(float(mirage_analytic(ground,100000,2,-DEG)),0,places=11)

    def test_horizontal_ray_has_zero_initial_slope(self):
        xs,states,_=mirage_integrate(20000,2,0,1000)
        self.assertEqual(states[0,1],0)
        self.assertGreater(states[-1,0],2)

    def test_apparent_tangent_matches_local_ray_direction(self):
        result=calculate("mirage",{})
        dashed=result["scene"]["paths"][-1]
        self.assertTrue(dashed["dashed"])
        arrival,apparent=np.array(dashed["points"])
        a,z0,theta=20000,2,-.5*DEG
        expected_slope=math.tan(theta)+arrival[0]/(2*(a+z0)*math.cos(theta)**2)
        self.assertAlmostEqual((arrival[1]-apparent[1])/arrival[0],expected_slope,places=12)
        self.assertLess(apparent[1],0)


class RainbowTests(unittest.TestCase):
    def test_water_primary_is_about_forty_two_degrees(self):
        i,D,radius=rainbow_stationary(4/3,1)
        self.assertTrue(41<radius/DEG<43)

    def test_water_secondary_is_about_fifty_one_degrees(self):
        i,D,radius=rainbow_stationary(4/3,2)
        self.assertTrue(50<radius/DEG<53)

    def test_stationary_incidence_annuls_independent_finite_difference(self):
        for m in [1,2]:
            i,_,_=rainbow_stationary(4/3,m)
            eps=1e-6
            derivative=(rainbow_deviation(i+eps,4/3,m)-rainbow_deviation(i-eps,4/3,m))/(2*eps)
            self.assertLess(abs(derivative),1e-8)

    def test_primary_red_has_larger_angular_radius_than_violet(self):
        red=rainbow_stationary(float(cauchy_index(700,1.322,.003)),1)[2]
        violet=rainbow_stationary(float(cauchy_index(420,1.322,.003)),1)[2]
        self.assertGreater(red,violet)

    def test_secondary_color_order_is_reversed(self):
        red=rainbow_stationary(float(cauchy_index(700,1.322,.003)),2)[2]
        violet=rainbow_stationary(float(cauchy_index(420,1.322,.003)),2)[2]
        self.assertLess(red,violet)

    def test_vector_trace_scattering_matches_unfolded_deviation(self):
        for m in [1,2]:
            for i in [40,60,75]:
                vertices,direction=rainbow_path(i*DEG,4/3,m)
                D=float(rainbow_deviation(i*DEG,4/3,m))
                self.assertAlmostEqual(direction[0],math.cos(D),places=12)
                self.assertAlmostEqual(np.linalg.norm(direction),1,places=12)

    def test_internal_reflection_points_stay_on_sphere(self):
        vertices,_=rainbow_path(60*DEG,4/3,2)
        np.testing.assert_allclose(np.linalg.norm(vertices[1:-1],axis=1),1,atol=1e-13)

    def test_refraction_vector_preserves_snell_tangent_component(self):
        direction=np.array([math.cos(40*DEG),math.sin(40*DEG)])
        transmitted=refract_vector(direction,[1,0],1,1.5)
        self.assertAlmostEqual(transmitted[1]*1.5,direction[1],places=13)


class PrismTests(unittest.TestCase):
    def test_symmetric_path_is_stationary(self):
        n,A=1.5,60*DEG
        i=math.asin(n*math.sin(A/2))
        eps=1e-6
        f0=float(prism_deviation(i,n,A)[0])
        fplus=float(prism_deviation(i+eps,n,A)[0])
        fminus=float(prism_deviation(i-eps,n,A)[0])
        self.assertLess(abs((fplus-fminus)/(2*eps)),1e-8)
        self.assertGreater(fplus+fminus-2*f0,0)

    def test_minimum_recovers_index(self):
        result=calculate("prisme",{})
        self.assertAlmostEqual(number(result,"Indice à"),number(result,"Indice déduit"),places=13)

    def test_violet_deviation_exceeds_red(self):
        red=number(calculate("prisme",{"wavelength":700}),"Déviation minimale")
        violet=number(calculate("prisme",{"wavelength":420}),"Déviation minimale")
        self.assertGreater(violet,red)

    def test_low_first_face_incidence_can_total_reflect_at_second_face(self):
        result=calculate("prisme",{"angle":10})
        self.assertIn("Réflexion totale",number(result,"Émergence"))

    def test_inaccessible_minimum_is_explicit_and_json_finite(self):
        result=calculate("prisme",{"apex":75,"cauchy_a":1.7,"cauchy_b":.015,"wavelength":400})
        self.assertEqual(number(result,"Incidence du"),"Aucun minimum transmissif")
        json.dumps(result,allow_nan=False)

    def test_vector_path_matches_second_face_angular_deviation(self):
        n,A,i=1.5,60*DEG,50*DEG
        vertices,polygon,exited,face=prism_path(i,n,A)
        self.assertTrue(exited)
        self.assertEqual(face,1)
        out=vertices[-1]-vertices[-2]
        out=out/np.linalg.norm(out)
        actual=i-math.atan2(out[1],out[0])
        predicted=float(prism_deviation(i,n,A)[0])
        self.assertAlmostEqual(actual,predicted,places=12)


class AberrationTests(unittest.TestCase):
    def test_paraboloid_focuses_every_axial_ray_exactly(self):
        heights=np.linspace(-180,180,41)
        xs,directions=mirror_surface(heights,400,"parabole")
        travel=(-200-xs)/directions[:,0]
        np.testing.assert_allclose(heights+travel*directions[:,1],0,atol=1e-12)

    def test_sphere_paraxial_limit_is_minus_radius_over_two(self):
        focus=float(mirror_axis_intercept([.0001],400,"sphere")[0])
        self.assertAlmostEqual(focus,-200,places=9)

    def test_leading_spherical_aberration_scales_as_aperture_squared(self):
        r=400
        first=float(mirror_axis_intercept([.01*r],r,"sphere")[0])+r/2
        second=float(mirror_axis_intercept([.02*r],r,"sphere")[0])+r/2
        self.assertAlmostEqual(second/first,4,delta=.001)

    def test_reflection_preserves_norm_and_reverses_normal_component(self):
        direction=np.array([.8,.6])
        normal=np.array([1.,2.]);normal/=np.linalg.norm(normal)
        reflected=reflect_vector(direction,normal)
        self.assertAlmostEqual(np.linalg.norm(reflected),1,places=13)
        self.assertAlmostEqual(reflected@normal,-direction@normal,places=13)

    def test_sphere_has_nonzero_spot_and_paraboloid_zero_spot(self):
        sphere=calculate("aberrations",{"surface":"sphere"})
        parabola=calculate("aberrations",{"surface":"parabole"})
        self.assertGreater(number(sphere,"Rayon RMS sur"),1)
        self.assertLess(number(parabola,"Rayon RMS sur"),1e-10)

    def test_best_rms_screen_is_between_paraxial_and_marginal_foci(self):
        result=calculate("aberrations",{})
        self.assertGreater(number(result,"Écran optimal"),number(result,"Foyer paraxial"))
        self.assertLess(number(result,"Écran optimal"),number(result,"Intersection axiale"))
        self.assertLess(number(result,"Rayon RMS minimal"),number(result,"Rayon RMS sur"))


class FermatTests(unittest.TestCase):
    def test_equal_indices_give_straight_line_crossing(self):
        self.assertAlmostEqual(fermat_crossing(1.5,1.5,20,8,5),20*8/13,places=12)

    def test_unequal_indices_obey_snell(self):
        result=calculate("fermat",{})
        self.assertLess(abs(number(result,"n₁sin")),1e-13)

    def test_stationary_optical_path_is_strictly_convex(self):
        result=calculate("fermat",{})
        self.assertGreater(number(result,"L″"),0)

    def test_shortest_geometric_path_is_slower_for_unequal_indices(self):
        args=(1,1.5,20,8,5)
        optimum=fermat_crossing(*args)
        straight=20*8/13
        self.assertLess(float(fermat_path(optimum,*args)),float(fermat_path(straight,*args)))
        geometric=lambda x:math.hypot(x,8)+math.hypot(20-x,5)
        self.assertGreater(geometric(optimum),geometric(straight))

    def test_optimum_is_less_than_every_sampled_alternative(self):
        args=(1.8,1,30,2,20)
        x=fermat_crossing(*args)
        minimum=float(fermat_path(x,*args))
        samples=fermat_path(np.linspace(-10,40,1001),*args)
        self.assertLessEqual(minimum,float(samples.min())+1e-12)

    def test_scaling_both_indices_does_not_change_trajectory(self):
        self.assertAlmostEqual(fermat_crossing(1,1.5,20,8,5),fermat_crossing(2,3,20,8,5),places=12)


class CatalogueContractTests(unittest.TestCase):
    def test_twelve_unique_labs_with_units_and_presets(self):
        self.assertEqual(len(LABS),12)
        self.assertEqual(len(LAB_BY_ID),12)
        for lab in LABS:
            self.assertTrue(lab["intro"])
            self.assertGreaterEqual(len(lab["presets"]),3)
            for control in lab["controls"]:
                self.assertIn("unit",control)
                self.assertIn("label",control)

    def test_defaults_and_all_presets_have_finite_json_scenes(self):
        for lab in LABS:
            for parameters in [{}]+[preset["values"] for preset in lab["presets"]]:
                with self.subTest(lab=lab["id"],parameters=parameters):
                    result=calculate(lab["id"],parameters)
                    json.dumps(result,ensure_ascii=False,allow_nan=False)
                    self.assertEqual(result["scene"]["kind"],"rays")
                    self.assertEqual(len(result["scene"]["bounds"]),4)
                    self.assertTrue(result["scene"]["paths"])
                    self.assertGreaterEqual(len(result["steps"]),4)
                    self.assertGreaterEqual(len(result["assumptions"]),3)

    def test_every_control_extreme_is_finite(self):
        for lab in LABS:
            for control in lab["controls"]:
                values=[control["min"],control["max"]] if control["type"]=="range" else [item["value"] for item in control["options"]]
                for value in values:
                    with self.subTest(lab=lab["id"],control=control["key"],value=value):
                        result=calculate(lab["id"],{control["key"]:value})
                        json.dumps(result,allow_nan=False)


if __name__=="__main__":
    unittest.main()
