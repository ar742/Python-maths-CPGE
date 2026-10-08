"""Références analytiques et contrôles indépendants des huit laboratoires P2."""
import json
import math
import unittest
import numpy as np
from commun import clean, integrate
from catalogue_p2 import LABS
from contenu_p2 import LESSONS, EXERCISES, GUIDES
from modeles_p2 import (COMPUTE, G, U, EARTH_RATE, co2_modes, pendulum_period,
    verlet, measured_period, spring_potential, spring_force, quartic_period,
    threshold_spring_period, foucault_solution, duffing_harmonic_roots,
    duffing_trajectory, fundamental)

def defaults(item):
    return {control['key']:control['value'] for control in item['controls']}

def metrics(output):
    return {m['label']:m['value'] for m in output['metrics']}

class CatalogueP2Tests(unittest.TestCase):
    def test_eight_unique_labs_with_presets(self):
        self.assertEqual(len(LABS),8)
        self.assertEqual({x['id'] for x in LABS},set(COMPUTE))
        for item in LABS:
            self.assertGreaterEqual(len(item['presets']),3)
            for chosen in item['presets']:
                self.assertLessEqual(set(chosen['values']),set(defaults(item)))

    def test_content_links_and_depth(self):
        self.assertEqual(len(LESSONS),16)
        self.assertEqual(len(EXERCISES),24)
        self.assertEqual(set(GUIDES),set(COMPUTE))
        for item in LABS:
            labid=item['id']
            self.assertEqual(sum(x['lab']==labid for x in LESSONS),2)
            self.assertEqual(sum(x['lab']==labid for x in EXERCISES),3)
            self.assertEqual(len(GUIDES[labid]['first_steps']),3)
            self.assertEqual(set(GUIDES[labid]['levels']),{'sup','spe','beyond'})

    def test_all_default_and_preset_results_are_json_finite(self):
        for item in LABS:
            base=defaults(item)
            for name, p in [('Défaut',base)]+[(s['label'],base|s['values']) for s in item['presets']]:
                with self.subTest(lab=item['id'],preset=name):
                    output=clean(COMPUTE[item['id']](p))
                    json.dumps(output,allow_nan=False)
                    self.assertGreaterEqual(len(output['charts']),3)
                    self.assertGreaterEqual(len(output['steps']),4)
                    for figure in output['charts']:
                        for curve in figure['series']:
                            self.assertEqual(len(curve['x']),len(curve['y']))

class ChainTests(unittest.TestCase):
    def test_dispersion_against_independent_stiffness_matrix(self):
        n=14;m=1.3;k=37
        stiffness=2*k*np.eye(n)-k*np.roll(np.eye(n),1,axis=0)-k*np.roll(np.eye(n),-1,axis=0)
        exact=np.linalg.eigvalsh(stiffness/m)
        theory=4*k/m*np.sin(np.pi*np.arange(n)/n)**2
        np.testing.assert_allclose(np.sort(exact),np.sort(theory),atol=1e-12)

    def test_alternating_mode_has_maximum_frequency(self):
        item=LABS[0];p=defaults(item)|{'N':12,'q':6,'m':2,'k':50}
        data=metrics(COMPUTE[item['id']](p))
        self.assertAlmostEqual(data['Pulsation du mode choisi'],2*math.sqrt(50/2))

    def test_rigid_translation_does_not_oscillate(self):
        item=LABS[0];p=defaults(item)|{'q':0,'excitation':'standing'}
        output=COMPUTE[item['id']](p)
        for curve in output['charts'][0]['series']:
            np.testing.assert_allclose(curve['y'],p['A'],atol=1e-14)

    def test_local_preparation_and_conserved_energy(self):
        p=defaults(LABS[0])|{'excitation':'local'}
        output=COMPUTE['chaine_atomique'](p)
        first=np.asarray(output['charts'][1]['series'][0]['y'])
        np.testing.assert_allclose(first,np.r_[p['A'],np.zeros(p['N']-1)],atol=1e-14)
        energy=output['charts'][3]['series'][0]['y']
        np.testing.assert_allclose(energy,p['k']*p['A']**2,rtol=1e-13)

    def test_wave_equation_limit(self):
        n=24;q=1;k=40;m=1
        exact=2*math.sqrt(k/m)*math.sin(math.pi*q/n)
        reduced=2*math.pi*q/n
        relative=1-exact/(math.sqrt(k/m)*reduced)
        self.assertLess(abs(relative-reduced**2/24),2e-5)

class MolecularTests(unittest.TestCase):
    def test_analytic_frequencies(self):
        mo=16*U;mc=12*U;k=1000
        _,_,omega,_=co2_modes(mo,mc,k)
        self.assertEqual(omega[0],0)
        self.assertAlmostEqual(omega[1]/math.sqrt(k/mo),1,places=13)
        self.assertAlmostEqual(omega[2]/math.sqrt(k/mo+2*k/mc),1,places=13)

    def test_weighted_orthogonality(self):
        masses,_,_,modes=co2_modes(18*U,13*U,800)
        np.testing.assert_allclose(modes.T@(masses[:,None]*modes),np.eye(3),atol=1e-13)

    def test_center_of_mass_is_fixed_for_vibrations(self):
        masses,_,_,modes=co2_modes(16*U,13*U,1000)
        self.assertLess(np.max(np.abs(masses@modes[:,1:])),1e-27)

    def test_isotope_only_changes_carbon_mode(self):
        _,_,o12,_=co2_modes(16*U,12*U,1000)
        _,_,o13,_=co2_modes(16*U,13*U,1000)
        self.assertAlmostEqual(o12[1]/o13[1],1,places=13)
        self.assertLess(o13[2],o12[2])

    def test_translation_has_zero_elastic_energy(self):
        masses,k,_,_=co2_modes(16*U,12*U,1000)
        x=np.array([1.,1.,1.])*3e-12
        self.assertEqual(float(x@k@x),0)

class FoucaultTests(unittest.TestCase):
    def test_initial_position_and_velocity(self):
        epsilon=1e-4
        z,_,_,_=foucault_solution(np.array([-epsilon,0,epsilon]),67,50,.5)
        self.assertAlmostEqual(z[1].real,.5)
        self.assertAlmostEqual(z[1].imag,0)
        self.assertLess(abs((z[2]-z[0])/(2*epsilon)),1e-12)

    def test_equator_is_plain_harmonic_motion(self):
        t=np.linspace(0,100,321)
        z,rotation,omega,_=foucault_solution(t,30,0,.5)
        self.assertEqual(rotation,0)
        np.testing.assert_allclose(z.real,.5*np.cos(omega*t),atol=1e-14)
        np.testing.assert_allclose(z.imag,0,atol=1e-14)

    def test_southern_solution_is_conjugate(self):
        t=np.linspace(0,500,333)
        north,*_=foucault_solution(t,67,50,.5)
        south,*_=foucault_solution(t,67,-50,.5)
        np.testing.assert_allclose(south,np.conjugate(north),atol=1e-14)

    def test_differential_equation_with_finite_differences(self):
        step=.001;t=np.arange(0,4+step,step)
        z,rotation,omega,_=foucault_solution(t,15,60,.8)
        derivative=(z[2:]-z[:-2])/(2*step)
        second=(z[2:]-2*z[1:-1]+z[:-2])/step**2
        residual=second+2j*rotation*derivative+omega**2*z[1:-1]
        self.assertLess(np.max(abs(residual)),1e-7)

    def test_pole_precession_uses_sidereal_day(self):
        self.assertAlmostEqual(2*math.pi/EARTH_RATE,86164.0905,places=8)

class PendulumTests(unittest.TestCase):
    def test_zero_amplitude_period_is_linear_limit(self):
        self.assertAlmostEqual(pendulum_period(0,1.7),2*math.pi*math.sqrt(1.7/G),places=13)

    def test_period_matches_known_elliptic_value_at_ninety_degrees(self):
        # K(1/sqrt(2)) = 1.8540746773013719, valeur tabulée indépendante.
        expected=4*math.sqrt(1/G)*1.8540746773013719
        self.assertAlmostEqual(pendulum_period(math.pi/2),expected,places=12)

    def test_small_angle_correction(self):
        angle=.07;t0=2*math.pi/math.sqrt(G)
        expansion=1+angle**2/16+11*angle**4/3072
        self.assertLess(abs(pendulum_period(angle)/t0-expansion),1e-10)

    def test_period_increases_with_amplitude(self):
        periods=[pendulum_period(a) for a in [.1,.5,1,2,2.95]]
        self.assertTrue(all(a<b for a,b in zip(periods,periods[1:])))

    def test_verlet_period_from_crossings_matches_integral(self):
        angle=1;period=pendulum_period(angle)
        t,x,_=verlet(lambda u:-G*math.sin(u),angle,3*period,3600)
        self.assertLess(abs(measured_period(t,x)/period-1),4e-6)

    def test_verlet_energy_improves_with_halved_step(self):
        def error(steps):
            t,x,v=verlet(lambda u:-G*math.sin(u),.8,5,steps)
            energy=.5*v*v+G*(1-np.cos(x))
            return float(np.max(abs(energy-energy[0])))
        self.assertLess(error(1600),.27*error(800))

    def test_third_harmonic_coefficient_at_small_angle(self):
        p=defaults(LABS[4])|{'angle':10}
        data=metrics(COMPUTE['pendule_anharmonique'](p))
        measured=data['Rapport mesuré troisième / première harmonique']
        expected=math.radians(10)**2/192
        self.assertLess(abs(measured/expected-1),.04)

class TransverseSpringTests(unittest.TestCase):
    def test_force_is_negative_potential_derivative(self):
        h=1e-6;x=.43;length=.8;rest=1;k=40
        difference=(spring_potential(x+h,length,rest,k)-spring_potential(x-h,length,rest,k))/(2*h)
        self.assertAlmostEqual(spring_force(x,length,rest,k),-difference,places=7)

    def test_all_equilibria_have_zero_force(self):
        length=.7;rest=1;k=40;position=math.sqrt(rest**2-length**2)
        for x in [0,position,-position]:
            self.assertAlmostEqual(spring_force(x,length,rest,k),0,places=12)

    def test_center_changes_stability(self):
        displacement=1e-4
        self.assertLess(spring_force(displacement,1.3,1,40),0)
        self.assertGreater(spring_force(displacement,.7,1,40),0)

    def test_threshold_has_quartic_leading_term(self):
        x=.001;rest=1;k=40
        potential=spring_potential(x,rest,rest,k)
        self.assertLess(abs(potential/(k*x**4/(4*rest**2))-1),1e-6)

    def test_confined_energy_does_not_cross_center(self):
        length=.7;rest=1;k=40;mass=1
        x0=math.sqrt(rest**2-length**2)+.05
        self.assertLess(spring_potential(x0,length,rest,k),spring_potential(0,length,rest,k))
        t,x,v=verlet(lambda x:spring_force(x,length,rest,k)/mass,x0,10,5000)
        self.assertGreater(np.min(x),0)

class QuarticTests(unittest.TestCase):
    def test_exact_amplitude_scaling(self):
        self.assertAlmostEqual(quartic_period(.4,1,40),quartic_period(.2,1,40)/2,places=13)

    def test_constant_matches_independent_beta_function_value(self):
        # I = sqrt(pi) Gamma(1/4)/(4 Gamma(3/4)), via math.gamma.
        integral=math.sqrt(math.pi)*math.gamma(.25)/(4*math.gamma(.75))
        self.assertAlmostEqual(quartic_period(.2,1,40),4*math.sqrt(2/40)*integral/.2,places=12)

    def test_quartic_trajectory_period(self):
        beta=40;amplitude=.2;mass=1;period=quartic_period(amplitude,mass,beta)
        t,x,v=verlet(lambda x:-beta*x**3/mass,amplitude,3*period,3600)
        self.assertLess(abs(measured_period(t,x)/period-1),1e-5)

    def test_exact_springs_converge_to_quartic_period(self):
        mass=1;stiffness=40;rest=1;amplitude=.001
        exact=threshold_spring_period(amplitude,mass,stiffness,rest)
        local=quartic_period(amplitude,mass,stiffness/rest**2)
        self.assertLess(abs(exact/local-1),1e-6)

    def test_spring_period_is_greater_than_quartic_at_finite_amplitude(self):
        exact=threshold_spring_period(.7,1,40,1)
        local=quartic_period(.7,1,40)
        self.assertGreater(exact,local)

class DuffingTests(unittest.TestCase):
    def test_harmonic_balance_reduces_to_linear_response(self):
        ratio=1.2;damping=.08;forcing=.2
        amplitudes=duffing_harmonic_roots(ratio,0,damping,forcing)
        expected=forcing/math.sqrt((1-ratio**2)**2+(2*damping*ratio)**2)
        self.assertEqual(len(amplitudes),1)
        self.assertAlmostEqual(amplitudes[0],expected,places=14)

    def test_roots_satisfy_independently_written_equation(self):
        ratio=1.3;beta=1;damping=.04;forcing=.2
        roots=duffing_harmonic_roots(ratio,beta,damping,forcing)
        self.assertEqual(len(roots),3)
        for amplitude in roots:
            left=amplitude**2*((1-ratio**2+.75*beta*amplitude**2)**2+(2*damping*ratio)**2)
            self.assertAlmostEqual(left,forcing**2,places=12)

    def test_linear_time_solution_reaches_reference_amplitude(self):
        damping=.1;forcing=.1;ratio=.9
        t,x,v=duffing_trajectory(0,damping,forcing,ratio,0,80)
        expected=forcing/math.sqrt((1-ratio**2)**2+(2*damping*ratio)**2)
        self.assertLess(abs(fundamental(t[-1601:],x[-1601:],ratio)/expected-1),2e-6)

    def test_unforced_damped_energy_decreases(self):
        t,x,v=duffing_trajectory(.7,.08,0,1,.8,30)
        energy=.5*v*v+.5*x*x+.7*x**4/4
        self.assertLess(np.max(np.diff(energy)),1e-10)
        self.assertLess(energy[-1],energy[0]*1e-10)

    def test_integrated_work_balance(self):
        t,x,v=duffing_trajectory(1,.06,.2,1.2,0,40)
        energy=.5*v*v+.5*x*x+x**4/4
        work=integrate(.2*np.cos(1.2*t)*v-2*.06*v*v,t)
        self.assertLess(abs(energy[-1]-energy[0]-work),3e-5)

if __name__=='__main__':
    unittest.main()
