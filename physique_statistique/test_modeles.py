"""Contrôles scientifiques indépendants : comptages, moments et intégrales.

Exécution : python -m unittest discover -s physique_statistique -p 'test_*.py'.
NumPy suffit ; les assertions de limite distinguent leurs approximations.
"""
import itertools
import json
import math
import unittest
import numpy as np
import modeles as p

trapezoid = np.trapezoid if hasattr(np,"trapezoid") else np.trapz


def integrate(function,low,high,order=240):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    xx=(low+high)/2+(high-low)*nodes/2
    return float(weights@function(xx)*(high-low)/2)


class Contract(unittest.TestCase):
    def test_defaults_and_modes_are_strict_json(self):
        cases=[dict(lab=lab) for lab in p.LABS]+[
            dict(lab="canonique",mode="trois"),
            dict(lab="occupations",mode="comparaison"),
            dict(lab="occupations",mode="bose",temperature=1e-7,log_density=20),
            dict(lab="occupations",mode="bose",temperature=5e-7,log_density=20),
            *[dict(lab="maxwell",mode=mode) for mode in ["pression","effusion","paroi"]],
            dict(lab="ising",mode="carre")]
        self.assertEqual(len(p.LABS),8)
        for case in cases:
            with self.subTest(case=case):
                result=p.calculate(case)
                json.dumps(result,allow_nan=False)
                self.assertEqual(result["lab"],case["lab"])
                self.assertTrue(result["metrics"])
                self.assertTrue(result["notes"])
                for chart in result["charts"]:
                    for line in chart["series"]:
                        self.assertEqual(len(line["x"]),len(line["y"]))

    def test_reject_nonobject_unknown_lab_and_mode(self):
        cases=[None,[],3,"canonique",dict(lab=[]),dict(lab="inconnu"),
               dict(lab="canonique",mode="quatre"),dict(lab="maxwell",mode=[]),
               dict(lab="occupations",mode="spin")]
        for case in cases:
            with self.subTest(case=case),self.assertRaises(ValueError):p.calculate(case)

    def test_reject_nonfinite_boolean_fractional_and_domains(self):
        cases=[dict(lab="canonique",temperature=value) for value in [math.nan,math.inf,True,0]]+[
            dict(lab="canonique",particles=3.5),dict(lab="canonique",fraction=1.1),
            dict(lab="canonique",mode="trois",degeneracy=0),
            dict(lab="maxwell",molar_mass=0),dict(lab="maxwell",mode="effusion",hole_mm2=0),
            dict(lab="occupations",mode="bose",mass_atom_u=0),
            dict(lab="occupations",mode="comparaison",mu_ratio=0),
            dict(lab="oscillateur",confinement=True)]
        for case in cases:
            with self.subTest(case=case),self.assertRaises(ValueError):p.calculate(case)

    def test_extreme_allowed_values_stay_finite(self):
        cases=[dict(lab="canonique",particles=100000,fraction=0,temperature=1,epsilon_mev=250),
               dict(lab="canonique",particles=1,fraction=1,temperature=3000,epsilon_mev=.1),
               dict(lab="gaz",temperature=3000,side_nm=20,mass_ratio=5,cutoff=4),
               dict(lab="oscillateur",temperature=.5,frequency_thz=50,confinement=6),
               dict(lab="spins",temperature=.1,field=-10,magnetic_moment=3),
               dict(lab="planck",temperature=100,wavelength_um=.05),
               dict(lab="occupations",temperature=1e-8,log_density=30),
               dict(lab="occupations",temperature=3000,log_density=15),
               dict(lab="occupations",mode="bose",temperature=1e-8,log_density=30,mass_atom_u=1),
               dict(lab="occupations",mode="bose",temperature=3000,log_density=15,mass_atom_u=250),
               dict(lab="maxwell",mode="paroi",fraction_initial=0,time_ratio=0,volume_litre=.001,volume2_litre=100,temperature=1,temperature2=3000)]
        for case in cases:
            with self.subTest(case=case):json.dumps(p.calculate(case),allow_nan=False)


class CanonicalAndCounting(unittest.TestCase):
    def test_two_level_partition_by_full_microstate_enumeration(self):
        N,x=8,.7
        energies=np.array([sum(bits) for bits in itertools.product([0,1],repeat=N)],dtype=float)
        weights=np.exp(-x*energies)
        probabilities=weights/weights.sum()
        state=p.two_level_statistics(x)
        mean=float(probabilities@energies)
        variance=float(probabilities@((energies-mean)**2))
        self.assertAlmostEqual(math.log(weights.sum()),N*state["log_partition"],13)
        self.assertAlmostEqual(mean,N*state["energy_ratio"],13)
        self.assertAlmostEqual(x*x*variance,N*state["heat_capacity"],13)
        self.assertAlmostEqual(-float(probabilities@np.log(probabilities)),N*state["entropy"],12)

    def test_microcanonical_count_and_stirling_borders(self):
        N=9
        counts={k:0 for k in range(N+1)}
        for bits in itertools.product([0,1],repeat=N):counts[sum(bits)]+=1
        for k,count in counts.items():
            state=p.microcanonical_two_level(N,k)
            self.assertAlmostEqual(state["entropy"],math.log(count),13)
            if k in [0,N]:
                self.assertEqual(state["entropy"],0)
                self.assertIsNone(state["stirling_refined"])
                self.assertIsNone(state["beta_epsilon_stirling"])
        self.assertGreater(p.microcanonical_two_level(N,2)["beta_epsilon_stirling"],0)
        self.assertLess(p.microcanonical_two_level(N,7)["beta_epsilon_stirling"],0)

    def test_stirling_improves_only_interior_and_capacity_factor(self):
        state=p.microcanonical_two_level(10000,3000)
        self.assertLess(abs(state["stirling_refined"]-state["entropy"]),.0001)
        self.assertGreater(abs(state["stirling_leading"]-state["entropy"]),4)
        x=2.
        self.assertAlmostEqual(p.two_level_statistics(x)["heat_capacity"],x*x/(4*math.cosh(x/2)**2),14)

    def test_three_levels_enumerate_degenerate_microstates(self):
        x,g=.63,4
        energies=np.array([0]+[1]*g+[2],dtype=float)
        weights=np.exp(-x*energies);prob=weights/weights.sum()
        state=p.canonical_levels(x,g)
        self.assertAlmostEqual(float(prob@energies),state["energy_ratio"],14)
        self.assertAlmostEqual(-float(prob@np.log(prob)),state["entropy"],14)
        self.assertAlmostEqual(state["probabilities"][1],float(prob[1:-1].sum()),14)

    def test_thermodynamic_derivatives_at_fixed_spectrum(self):
        for function in [p.two_level_statistics,lambda x:p.canonical_levels(x,5),p.oscillator_statistics]:
            for x in [.1,.8,3.]:
                h=1e-5*x;state=function(x)
                plus,minus=function(x+h),function(x-h)
                energy=-(plus["log_partition"]-minus["log_partition"])/(2*h)
                capacity=-x*x*(plus["energy_ratio"]-minus["energy_ratio"])/(2*h)
                self.assertAlmostEqual(energy,state["energy_ratio"],8)
                self.assertAlmostEqual(capacity,state["heat_capacity"],8)
                self.assertAlmostEqual(state["entropy"],state["log_partition"]+x*state["energy_ratio"],12)


class BoxOscillatorSpins(unittest.TestCase):
    def test_cube_factorization_against_full_3d_sum(self):
        x,cut=.3,7
        energies=np.array([a*a+b*b+c*c for a,b,c in itertools.product(range(1,cut+1),repeat=3)],dtype=float)
        weights=np.exp(-x*energies);prob=weights/weights.sum()
        mean=float(prob@energies)
        state=p.cube_statistics(x,cut)
        self.assertAlmostEqual(math.log(weights.sum()),state["log_partition"],13)
        self.assertAlmostEqual(mean,state["energy_ratio"],12)
        self.assertAlmostEqual(x*x*float(prob@((energies-mean)**2)),state["heat_capacity"],12)

    def test_cube_ground_state_and_classical_limit_with_converged_cutoff(self):
        cold=p.cube_statistics(30,20)
        self.assertAlmostEqual(cold["energy_ratio"],3,14)
        self.assertLess(cold["heat_capacity"],1e-30)
        x=1e-5
        hot=p.cube_statistics(x,5000)
        self.assertAlmostEqual(x*hot["energy_ratio"],1.5,delta=.003)
        self.assertAlmostEqual(hot["heat_capacity"],1.5,delta=.002)

    def test_oscillator_infinite_sum_by_long_geometric_window(self):
        x=.017;n=np.arange(4000)
        weights=np.exp(-x*(n+.5));prob=weights/weights.sum()
        state=p.oscillator_statistics(x)
        self.assertAlmostEqual(math.log(weights.sum()),state["log_partition"],12)
        self.assertAlmostEqual(float(prob@(n+.5)),state["energy_ratio"],11)
        self.assertAlmostEqual(-float(prob@np.log(prob)),state["entropy"],12)
        cold=p.oscillator_statistics(1000)
        self.assertEqual(cold["energy_ratio"],.5)
        self.assertEqual(cold["heat_capacity"],0)
        self.assertAlmostEqual(p.oscillator_statistics(1e-5)["heat_capacity"],1,10)

    def test_classical_three_translation_terms_are_distinct_from_full_1d_ho(self):
        result=p.calculate(dict(lab="oscillateur",confinement=1))
        self.assertEqual(result["theory"]["classical_quadratic_terms"],4)
        self.assertAlmostEqual(result["theory"]["classical_energy_joule"]/(p.KB*300),2)

    def test_spin_ensemble_and_susceptibility_derivative(self):
        for x in [-3.,-.4,0.,.4,3.]:
            weights=np.exp(np.array([x,-x]));prob=weights/weights.sum()
            state=p.spin_statistics(x)
            self.assertAlmostEqual(float(prob@np.array([1.,-1.])),state["polarization"],14)
            self.assertAlmostEqual(-float(prob@np.log(prob)),state["entropy"],13)
            h=1e-5
            derivative=(p.spin_statistics(x+h)["polarization"]-p.spin_statistics(x-h)["polarization"])/(2*h)
            self.assertAlmostEqual(derivative,state["susceptibility_ratio"],9)
        self.assertEqual(p.spin_statistics(0)["entropy"],math.log(2))


class QuantumGases(unittest.TestCase):
    def test_single_state_distributions_and_dilute_limit(self):
        mu=-.8;x=.6
        occupation=p.occupation(x,mu,"BE")
        n=np.arange(200);z=math.exp(mu-x);prob=(1-z)*z**n
        self.assertAlmostEqual(float(prob@n),occupation,13)
        self.assertAlmostEqual(float(prob@((n-occupation)**2)),occupation*(1+occupation),13)
        fermion=p.occupation(x,mu,"FD")
        self.assertAlmostEqual(fermion,math.exp(mu-x)/(1+math.exp(mu-x)),14)
        for statistics in ["BE","FD"]:
            self.assertAlmostEqual(p.occupation(10,-8,statistics)/p.occupation(10,-8,"MB"),1,7)
        self.assertEqual(p.occupation(10000,0,"FD"),0)
        self.assertEqual(p.occupation(-10000,0,"FD"),1)
        with self.assertRaises(ValueError):p.occupation(0,0,"BE")

    def test_fermi_sphere_count_and_spin_degeneracy(self):
        n=1e28;tf=p.fermi_temperature(n)
        kf=math.sqrt(2*p.M_E*p.KB*tf)/p.HBAR
        self.assertAlmostEqual(2*kf**3/(6*math.pi**2)/n,1,14)
        self.assertAlmostEqual(p.fermi_temperature(n,degeneracy=1)/tf,2**(2/3),14)

    def test_fermi_integrals_against_dense_momentum_quadrature(self):
        theta=.35;state=p.fermi_gas_state(theta)
        q=np.linspace(0,6,240001)
        f=1/(1+np.exp((q*q-state["mu_ef"])/theta))
        self.assertAlmostEqual(float(trapezoid(3*q*q*f,q)),1,10)
        self.assertAlmostEqual(float(trapezoid(3*q**4*f,q)),state["energy_ef"],10)
        self.assertLess(abs(state["number_residual"]),1e-12)

    def test_fermi_sommerfeld_and_classical_limits(self):
        theta=.015;state=p.fermi_gas_state(theta)
        self.assertAlmostEqual(state["mu_ef"],1-math.pi**2*theta**2/12,delta=8e-8)
        self.assertAlmostEqual(state["energy_ef"],.6+math.pi**2*theta**2/4,delta=2e-7)
        cold=p.fermi_gas_state(1e-9)
        self.assertAlmostEqual(cold["energy_ef"],.6,11)
        hot=p.fermi_gas_state(1000)
        self.assertAlmostEqual(hot["energy_ef"]/1000,1.5,delta=1e-5)

    def test_bose_integral_against_convergent_fugacity_series(self):
        for mu in [-5.,-.7,-.05]:
            k=np.arange(1,10001,dtype=float)
            independent=float(np.sum(np.exp(mu*k)/k**1.5))
            self.assertAlmostEqual(p.bose_number_function(mu),independent,12)
        self.assertEqual(p.bose_number_function(0),p.ZETA_3_2)

    def test_bose_critical_density_and_condensate_conservation(self):
        n,mass=1e20,87*p.M_U
        tc=p.bose_temperature(n,mass)
        wavelength=p.thermal_wavelength(tc,mass)
        self.assertAlmostEqual(n*wavelength**3,p.ZETA_3_2,13)
        self.assertAlmostEqual(tc,3.979148732593922e-7,delta=1e-18)
        for theta in [.01,.5,.999,1.,1.001,1.5,20.]:
            state=p.bose_gas_state(theta)
            self.assertAlmostEqual(state["thermal_fraction"]+state["condensate_fraction"],1,14)
            if theta<=1:
                self.assertEqual(state["mu_ratio"],0)
                self.assertAlmostEqual(state["condensate_fraction"],1-theta**1.5,14)
            else:
                self.assertLess(state["mu_ratio"],0)
                self.assertLess(abs(state["number_residual"]),1e-10)
                self.assertAlmostEqual(p.bose_number_function(state["mu_ratio"])*theta**1.5/p.ZETA_3_2,1,10)

    def test_bose_boundary_layer_arbitrarily_close_to_criticality(self):
        # g3/2(e^η)=ζ(3/2)−2√π√(−η)+O(η) ; indépendant de la quadrature.
        eta=-1e-15
        leading=p.ZETA_3_2-2*math.sqrt(math.pi*(-eta))
        self.assertAlmostEqual(p.bose_number_function(eta),leading,delta=3e-14)
        theta=1+1e-9;state=p.bose_gas_state(theta)
        deficit=p.ZETA_3_2*(1-theta**(-1.5))
        expected_mu=-(deficit/(2*math.sqrt(math.pi)))**2
        self.assertAlmostEqual(state["mu_ratio"]/expected_mu,1,delta=1e-6)
        self.assertLess(abs(state["number_residual"]),1e-12)


class KineticTheory(unittest.TestCase):
    def setUp(self):
        self.temperature=310.;self.mass=.028/p.N_A;self.density=2.4e25
        self.state=p.maxwell_statistics(self.temperature,self.mass,self.density)

    def test_maxwell_normalization_and_three_speed_moments(self):
        sigma=self.state["sigma"]
        pdf=lambda v:p.maxwell_speed_density(v,self.temperature,self.mass)
        self.assertAlmostEqual(integrate(pdf,0,10*sigma),1,12)
        self.assertAlmostEqual(integrate(lambda v:v*pdf(v),0,10*sigma)/self.state["mean_speed"],1,12)
        self.assertAlmostEqual(integrate(lambda v:v*v*pdf(v),0,10*sigma)/self.state["rms_speed"]**2,1,12)
        h=.001*sigma;mode=self.state["most_probable"]
        self.assertGreater(pdf(mode),pdf(mode-h));self.assertGreater(pdf(mode),pdf(mode+h))

    def test_pressure_and_flux_from_incoming_gaussian_halfspace(self):
        sigma=self.state["sigma"]
        gaussian=lambda v:np.exp(-v*v/(2*sigma*sigma))/(math.sqrt(2*math.pi)*sigma)
        pressure=2*self.density*self.mass*integrate(lambda v:v*v*gaussian(v),0,10*sigma)
        flux=self.density*integrate(lambda v:v*gaussian(v),0,10*sigma)
        self.assertAlmostEqual(pressure/self.state["pressure"],1,12)
        self.assertAlmostEqual(flux/self.state["incident_flux"],1,12)

    def test_effusive_selection_and_energy(self):
        sigma=self.state["sigma"]
        pdf=lambda v:p.maxwell_speed_density(v,self.temperature,self.mass,True)
        self.assertAlmostEqual(integrate(pdf,0,10*sigma),1,12)
        energy=integrate(lambda v:.5*self.mass*v*v*pdf(v),0,10*sigma)
        self.assertAlmostEqual(energy/(p.KB*self.temperature),2,12)
        result=p.calculate(dict(lab="maxwell",mode="effusion",time_ratio=2))
        state=result["theory"]
        self.assertAlmostEqual(state["rate_per_second"]*state["tau_seconds"],1,14)
        self.assertAlmostEqual(state["remaining_fraction"],math.exp(-2),14)

    def test_porous_exchange_ode_and_stationary_pressure_ratio(self):
        a1,a2,initial=.7,1.4,.1
        t,h=.3,1e-5
        first,second=p.porous_fractions(t,a1,a2,initial)
        plus=p.porous_fractions(t+h,a1,a2,initial)[0]
        minus=p.porous_fractions(t-h,a1,a2,initial)[0]
        self.assertAlmostEqual(float((plus-minus)/(2*h)),float(-a1*first+a2*second),9)
        self.assertAlmostEqual(float(first+second),1,14)
        result=p.calculate(dict(lab="maxwell",mode="paroi",temperature=200,temperature2=800,volume_litre=2,volume2_litre=3,time_ratio=8,fraction_initial=.25))
        theory=result["theory"];eq=theory["equilibrium_fraction1"]
        ratio=(eq*200/theory["volume_m3"])/((1-eq)*800/theory["volume2_m3"])
        self.assertAlmostEqual(ratio,math.sqrt(200/800),14)
        transient=p.calculate(dict(lab="maxwell",mode="paroi",time_ratio=0,fraction_initial=.5))["theory"]
        self.assertNotAlmostEqual(transient["pressure1_pa"]/math.sqrt(300),transient["pressure2_pa"]/math.sqrt(600))


class Radiation(unittest.TestCase):
    def test_planck_wavelength_frequency_jacobian_and_micron_conversion(self):
        wavelength,temp=.7e-6,4300.
        frequency=p.C_LIGHT/wavelength
        bnu=2*p.H*frequency**3/p.C_LIGHT**2/math.expm1(p.H*frequency/(p.KB*temp))
        self.assertAlmostEqual(p.planck_radiance(wavelength,temp)/(bnu*p.C_LIGHT/wavelength**2),1,13)
        result=p.calculate(dict(lab="planck",temperature=temp,wavelength_um=.7))
        self.assertAlmostEqual(result["metrics"][2]["value"]/p.planck_radiance(wavelength,temp),1e-6,18)

    def test_stefan_law_by_independent_log_wavelength_integration(self):
        temp=3400.
        peak=p.WIEN_B/temp
        logs=np.linspace(math.log(peak*1e-4),math.log(peak*1e4),40001)
        wavelength=np.exp(logs)
        integral=float(trapezoid(p.planck_radiance(wavelength,temp)*wavelength,logs))*math.pi
        self.assertAlmostEqual(integral/(p.SIGMA*temp**4),1,delta=1e-10)
        self.assertAlmostEqual(p.SIGMA/5.670374419e-8,1,delta=1e-10)

    def test_wien_root_is_a_maximum(self):
        temp=5000.;peak=p.WIEN_B/temp
        center=p.planck_radiance(peak,temp)
        self.assertGreater(center,p.planck_radiance(peak*.99,temp))
        self.assertGreater(center,p.planck_radiance(peak*1.01,temp))
        self.assertAlmostEqual(p.WIEN_B,2.897771955e-3,delta=1e-12)

    def test_visible_band_by_direct_si_integral(self):
        temp=2500.
        integral=math.pi*integrate(lambda wavelength:2*p.H*p.C_LIGHT**2/wavelength**5/np.expm1(p.H*p.C_LIGHT/(wavelength*p.KB*temp)),.39e-6,.78e-6)
        fraction=integral/(p.SIGMA*temp**4)
        self.assertAlmostEqual(fraction,p.visible_fraction(temp),13)
        self.assertAlmostEqual(fraction,.05895775753237519,13)
        self.assertAlmostEqual(p.visible_fraction(temp,.39e-6,.76e-6),.0518702518,delta=1e-10)
        for temp in [100.,1000.,5800.,10000.]:
            self.assertGreaterEqual(p.visible_fraction(temp),0)
            self.assertLessEqual(p.visible_fraction(temp),1)


if __name__=="__main__":unittest.main()
