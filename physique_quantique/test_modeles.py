"""Vérifications indépendantes des modèles et de leur contrat JSON.

Quadratures, système de raccordement, diagonalisation et matrices explicites
complètent les invariants physiques ; aucune dépendance à SciPy n'est requise.
"""
import json
import math
import unittest
import numpy as np
import modeles as q

trapezoid = np.trapezoid if hasattr(np,"trapezoid") else np.trapz


def integrate_interval(function,a,b,order=220):
    nodes,w=np.polynomial.legendre.leggauss(order)
    x=(a+b)/2+(b-a)/2*nodes
    return np.sum(function(x)*w)*(b-a)/2


def independent_barrier(E,V,a):
    """Quatre amplitudes obtenues sans la matrice de propagation du moteur."""
    k=math.sqrt(2*E);z=np.sqrt(complex(2*(E-V)))
    forward=np.exp(1j*z*a);back=np.exp(-1j*z*a);out=np.exp(1j*k*a)
    M=np.array([[1,-1,-1,0],[-1j*k,-1j*z,1j*z,0],
                [0,forward,back,-out],[0,1j*z*forward,-1j*z*back,-1j*k*out]],dtype=complex)
    return np.linalg.solve(M,np.array([-1,-1j*k,0,0]))


class InputValidation(unittest.TestCase):
    def test_reject_nan_and_infinity(self):
        for v in [math.nan,math.inf,-math.inf]:
            with self.subTest(v=v),self.assertRaises(ValueError):q.calculate(dict(lab="boite",L_nm=v))

    def test_reject_boolean_as_number(self):
        with self.assertRaises(ValueError):q.calculate(dict(lab="boite",nx=True))

    def test_reject_fractional_quantum_number(self):
        with self.assertRaises(ValueError):q.calculate(dict(lab="oscillateur",n=2.5))

    def test_reject_negative_wall_quantum_number(self):
        with self.assertRaises(ValueError):q.calculate(dict(lab="boite",nx=0))

    def test_reject_unknown_lab_and_choices(self):
        for data in [dict(lab="inconnu"),dict(lab=[]),dict(lab="intrication",state="pur"),dict(lab="bloch",gate="CNOT")]:
            with self.subTest(data=data),self.assertRaises(ValueError):q.calculate(data)

    def test_reject_nonobject(self):
        for data in [None,[],"boite",3]:
            with self.subTest(data=data),self.assertRaises(ValueError):q.calculate(data)

    def test_all_defaults_are_strict_json(self):
        for lab in q.LABS:
            with self.subTest(lab=lab):
                result=q.calculate(dict(lab=lab))
                json.dumps(result,allow_nan=False)
                self.assertEqual(result["lab"],lab)
                self.assertTrue(result["metrics"])
                self.assertTrue(result["notes"])
                for c in result["charts"]:
                    for s in c["series"]:self.assertEqual(len(s["x"]),len(s["y"]))

    def test_extreme_parameters_remain_finite(self):
        cases=[dict(lab="boite",boundary="periodique",nx=-4,ny=4,nz=0,mix=.5,time=8,L_nm=.2),
               dict(lab="heisenberg",sigma=.2,chirp=-3,time=6,p0=-3),
               dict(lab="diffusion",energy=.1,height=4,width=4),
               dict(lab="diffusion",energy=4,height=4,width=4),
               dict(lab="oscillateur",mode="coherent",alpha=3,time=12),
               dict(lab="intrication",visibility=0),dict(lab="josephson",voltage_uV=0),
               dict(lab="rabi",omega=.1,detuning=-4,time=15),
               dict(lab="bloch",purity=0,gate="Ry",angle=360),dict(lab="circuits",mode="grover",iterations=4)]
        for data in cases:
            with self.subTest(data=data):json.dumps(q.calculate(data),allow_nan=False)


class ConstantsAndCube(unittest.TestCase):
    def test_exact_si_relations(self):
        self.assertEqual(q.H,6.62607015e-34)
        self.assertEqual(q.E_CHARGE,1.602176634e-19)
        self.assertEqual(q.C,299792458)
        self.assertAlmostEqual(q.HBAR*2*math.pi/q.H,1,places=15)
        self.assertAlmostEqual(q.PHI0*2*q.E_CHARGE/q.H,1,places=15)

    def test_first_wall_levels_and_degeneracies(self):
        self.assertEqual([(v["level"],v["degeneracy"]) for v in q.box_levels("parois",5)],[(3,1),(6,3),(9,3),(11,3),(12,1)])

    def test_first_periodic_shells_include_zero(self):
        self.assertEqual([(v["level"],v["degeneracy"]) for v in q.box_levels("periodique",5)],[(0,1),(1,6),(2,12),(3,8),(4,6)])

    def test_wall_modes_normalized_and_orthogonal(self):
        for n,m in [(1,1),(2,2),(6,6),(1,2),(3,7)]:
            value=integrate_interval(lambda x:q.box_mode(n,x)*q.box_mode(m,x),0,1)
            self.assertAlmostEqual(float(value),int(n==m),places=12)

    def test_periodic_modes_normalized_and_orthogonal(self):
        for n,m in [(-4,-4),(0,0),(4,4),(-3,2),(0,1)]:
            value=integrate_interval(lambda x:np.conj(q.box_mode(n,x,"periodique"))*q.box_mode(m,x,"periodique"),0,1)
            self.assertAlmostEqual(abs(value-int(n==m)),0,places=12)

    def test_l_scaling_and_ground_energy(self):
        g=q.calculate(dict(lab="boite",L_nm=1))["theory"]
        h=q.calculate(dict(lab="boite",L_nm=2))["theory"]
        self.assertAlmostEqual(g["energy_scale_eV"]/h["energy_scale_eV"],4,places=13)
        expected=3*q.H*q.H/(8*q.ME*1e-18*q.E_CHARGE)
        self.assertAlmostEqual(g["mean_energy"]*g["energy_scale_eV"],expected,places=13)

    def test_superposition_marginal_normalized(self):
        for boundary in ["parois","periodique"]:
            r=q.calculate(dict(lab="boite",boundary=boundary,nx=2,ny=2,nz=2,mix=.37,phase=45,time=.8))
            s=r["charts"][0]["series"][0]
            self.assertAlmostEqual(float(trapezoid(s["y"],s["x"])),1,places=12)
            grid=r["charts"][1]["grid"]
            mass=trapezoid(trapezoid(grid["z"],grid["x"],axis=1),grid["y"])
            self.assertAlmostEqual(float(mass),1,places=12)

    def test_nz_even_does_not_destroy_marginal(self):
        r=q.calculate(dict(lab="boite",nz=2))
        self.assertGreater(np.max(r["charts"][1]["grid"]["z"]),3)

    def test_beat_phase_changes_density_not_energy(self):
        a=q.calculate(dict(lab="boite",mix=.5,time=0))
        b=q.calculate(dict(lab="boite",mix=.5,time=math.pi/3))
        ya=np.array(a["charts"][0]["series"][0]["y"])
        yb=np.array(b["charts"][0]["series"][0]["y"])
        self.assertGreater(np.max(abs(ya-yb)),2)
        self.assertEqual(a["theory"]["mean_energy"],b["theory"]["mean_energy"])

    def test_periodic_zero_mode_is_uniform(self):
        r=q.calculate(dict(lab="boite",boundary="periodique",nx=0,ny=0,nz=0))
        np.testing.assert_allclose(r["charts"][0]["series"][0]["y"],1,atol=1e-14)
        self.assertEqual(r["theory"]["mean_energy"],0)


class Uncertainty(unittest.TestCase):
    def test_gaussian_normalized_after_propagation(self):
        for sigma,chirp,time,p0 in [(.6,0,0,0),(.8,1.2,2,1),(1.5,-2,1.8,-1)]:
            g=q.gaussian_moments(sigma,chirp,time,p0);mu=g["mean_x"];w=math.sqrt(g["variance_x"])
            norm=integrate_interval(lambda x:abs(q.gaussian_wavefunction(x,sigma,chirp,time,p0))**2,mu-10*w,mu+10*w)
            self.assertAlmostEqual(float(norm),1,places=12)

    def test_wavefunction_moments_by_spatial_quadrature(self):
        sigma,chirp,time,p0=.8,1.2,2,1
        g=q.gaussian_moments(sigma,chirp,time,p0);mu=g["mean_x"];w=math.sqrt(g["variance_x"])
        mean=integrate_interval(lambda x:x*abs(q.gaussian_wavefunction(x,sigma,chirp,time,p0))**2,mu-10*w,mu+10*w)
        var=integrate_interval(lambda x:(x-mu)**2*abs(q.gaussian_wavefunction(x,sigma,chirp,time,p0))**2,mu-10*w,mu+10*w)
        self.assertAlmostEqual(float(mean),g["mean_x"],places=11)
        self.assertAlmostEqual(float(var),g["variance_x"],places=11)

    def test_impulsion_moments_from_fourier_transform(self):
        sigma,chirp,time,p0=.75,-.6,1.2,.9
        N=32768;dx=.004;x=(np.arange(N)-N//2)*dx
        psi=q.gaussian_wavefunction(x,sigma,chirp,time,p0)
        fft=np.fft.fftshift(np.fft.fft(np.fft.ifftshift(psi)))*dx/math.sqrt(2*math.pi)
        p=np.fft.fftshift(np.fft.fftfreq(N,dx))*2*math.pi;dp=p[1]-p[0]
        density=abs(fft)**2
        self.assertAlmostEqual(float(np.sum(density)*dp),1,places=11)
        self.assertAlmostEqual(float(np.sum(p*density)*dp),p0,places=11)
        self.assertAlmostEqual(float(np.sum((p-p0)**2*density)*dp),q.gaussian_moments(sigma,chirp,time,p0)["variance_p"],places=11)

    def test_free_schrodinger_equation(self):
        x=np.linspace(-3,3,80);h=1e-4;t=.7
        f=lambda xs,ts:q.gaussian_wavefunction(xs,.9,.3,ts,1)
        lhs=1j*(f(x,t+h)-f(x,t-h))/(2*h)
        rhs=-(f(x+h,t)-2*f(x,t)+f(x-h,t))/(2*h*h)
        self.assertLess(np.max(abs(lhs-rhs)),4e-8)

    def test_covariance_determinant_and_contraction(self):
        for chi in [-3,-.5,0,2.2]:
            for t in [0,.5,3,6]:
                g=q.gaussian_moments(.8,chi,t)
                self.assertGreaterEqual(g["uncertainty"],.5-1e-13)
                self.assertAlmostEqual(g["covariance_determinant"],.25,places=10)
        self.assertLess(q.gaussian_moments(1,-1,1)["variance_x"],1)

    def test_fente_first_zero_and_divergent_variance(self):
        r=q.calculate(dict(lab="heisenberg",mode="fente",width=1,wavelength_nm=500))["theory"]
        self.assertAlmostEqual(r["first_zero_angle_degrees"],30,places=12)
        self.assertFalse(r["momentum_variance_finite"])
        # La variance tronquée de la transformée rectangulaire croît avec R.
        a=1
        values=[]
        for R in [20*math.pi,40*math.pi]:
            values.append(integrate_interval(lambda p:p*p*a/(2*math.pi)*np.sinc(a*p/(2*math.pi))**2,-R,R,600))
        self.assertAlmostEqual(float(values[1]/values[0]),2,places=9)

    def test_subwavelength_fente_has_no_propagating_first_zero(self):
        r=q.calculate(dict(lab="heisenberg",mode="fente",width=.2,wavelength_nm=780))["theory"]
        self.assertIsNone(r["first_zero_angle_degrees"])

    def test_energy_bound_and_atomic_scale(self):
        r=q.calculate(dict(lab="heisenberg",mode="estimations",omega=2))["theory"]
        self.assertAlmostEqual(r["oscillator_optimal_sigma"],.5,places=14)
        self.assertAlmostEqual(r["oscillator_bound"],1,places=14)
        self.assertAlmostEqual(q.BOHR_RADIUS*1e12,52.91772105,places=6)
        self.assertAlmostEqual(r["hydrogen_estimate_eV"],-13.60569312,places=6)


class Scattering(unittest.TestCase):
    def test_step_above_threshold_flux_factor(self):
        s=q.scattering(2,1,mode="marche")
        expected_R=((math.sqrt(2)-1)/(math.sqrt(2)+1))**2
        self.assertAlmostEqual(s["R"],expected_R,places=14)
        self.assertAlmostEqual(s["T"],1-expected_R,places=14)
        self.assertGreater(abs(abs(s["t"])**2-s["T"]),.1)

    def test_subthreshold_step_has_evanescence_without_flux(self):
        s=q.scattering(1,2,mode="marche")
        self.assertAlmostEqual(s["R"],1,places=14)
        self.assertEqual(s["T"],0)
        psi,dp=q.scattering_wave([1,2],s,mode="marche")
        self.assertGreater(abs(psi[0]),abs(psi[1]))
        np.testing.assert_allclose(np.imag(np.conj(psi)*dp),0,atol=1e-14)

    def test_threshold_step_has_R_one(self):
        s=q.scattering(1,1,mode="marche")
        self.assertAlmostEqual(s["R"],1,places=14)
        self.assertEqual(s["T"],0)
        self.assertLess(max(q.scattering_residuals(s,1,"marche")),1e-14)

    def test_barrier_amplitudes_against_independent_four_equations(self):
        for E,V,a in [(.7,2,1),(3,2,1.2),(1,2,2.5),(.1,4,4)]:
            with self.subTest(E=E,V=V,a=a):
                independent=independent_barrier(E,V,a);s=q.scattering(E,V,a)
                self.assertLess(abs(independent[0]-s["r"]),2e-11)
                self.assertLess(abs(independent[3]-s["t"]),2e-11)

    def test_tunnelling_closed_formula(self):
        E,V,a=.6,2,1.4;kappa=math.sqrt(2*(V-E))
        expected=1/(1+V*V*math.sinh(kappa*a)**2/(4*E*(V-E)))
        self.assertAlmostEqual(q.scattering(E,V,a)["T"],expected,places=14)

    def test_threshold_barrier_limit(self):
        E=V=1.3;a=1.7
        expected=1/(1+E*a*a/2)
        for energy in [E,E-1e-8,E+1e-8]:
            self.assertAlmostEqual(q.scattering(energy,V,a)["T"],expected,places=7)

    def test_above_barrier_resonance(self):
        V=1;a=1.2;E=V+(math.pi/a)**2/2
        s=q.scattering(E,V,a)
        self.assertAlmostEqual(s["T"],1,places=13)
        self.assertLess(s["R"],1e-26)

    def test_zero_barrier_is_free_propagation(self):
        E=1.7;a=2.3;s=q.scattering(E,0,a)
        x=np.linspace(-3,5,150);psi,dp=q.scattering_wave(x,s,a)
        np.testing.assert_allclose(psi,np.exp(1j*math.sqrt(2*E)*x),atol=4e-15)
        self.assertLess(s["R"],1e-28)

    def test_flux_conserved_and_interfaces_continuous(self):
        for E,V,a in [(1,2,1),(3,2,2),(2,2,2),(.1,4,4)]:
            s=q.scattering(E,V,a);x=np.linspace(-3,a+3,400);psi,dp=q.scattering_wave(x,s,a)
            current=np.imag(np.conj(psi)*dp)
            np.testing.assert_allclose(current,s["k"]*s["T"],atol=5e-11)
            self.assertLess(max(q.scattering_residuals(s,a,"barriere")),1e-9)
            self.assertAlmostEqual(s["R"]+s["T"],1,places=9)


class Oscillator(unittest.TestCase):
    def test_hermite_norm_and_orthogonality(self):
        for n,m in [(0,0),(1,1),(10,10),(0,2),(3,5)]:
            value=integrate_interval(lambda x:q.hermite_wavefunction(n,x)*q.hermite_wavefunction(m,x),-12,12,320)
            self.assertAlmostEqual(float(value),int(n==m),places=12)

    def test_hermite_first_two_closed_forms(self):
        x=np.linspace(-3,3,70);ground=np.exp(-x*x/2)/math.pi**.25
        np.testing.assert_allclose(q.hermite_wavefunction(1,x),math.sqrt(2)*x*ground,atol=1e-14)
        np.testing.assert_allclose(q.hermite_wavefunction(2,x),(2*x*x-1)/math.sqrt(2)*ground,atol=1e-14)

    def test_stationary_schrodinger_equation(self):
        x=np.linspace(-4,4,80);h=1e-4
        for n in [0,1,4,10]:
            f=q.hermite_wavefunction(n,x)
            second=(q.hermite_wavefunction(n,x+h)-2*f+q.hermite_wavefunction(n,x-h))/(h*h)
            self.assertLess(np.max(abs(-second/2+x*x*f/2-(n+.5)*f)),4e-7)

    def test_eigenstate_second_moment(self):
        for n in [0,3,10]:
            variance=integrate_interval(lambda x:x*x*q.hermite_wavefunction(n,x)**2,-12,12,320)
            self.assertAlmostEqual(float(variance),n+.5,places=11)

    def test_coherent_ehrenfest_and_energy(self):
        alpha,phase=1.3,.4;h=1e-5;t=.7
        g=q.coherent_moments(alpha,phase,t)
        plus=q.coherent_moments(alpha,phase,t+h);minus=q.coherent_moments(alpha,phase,t-h)
        self.assertAlmostEqual((plus["mean_x"]-minus["mean_x"])/(2*h),g["mean_p"],places=9)
        self.assertAlmostEqual((plus["mean_p"]-minus["mean_p"])/(2*h),-g["mean_x"],places=9)
        self.assertAlmostEqual((g["mean_x"]**2+g["mean_p"]**2+1)/2,g["energy"],places=14)

    def test_stationary_density_independent_of_time(self):
        a=q.calculate(dict(lab="oscillateur",n=5,time=0))
        b=q.calculate(dict(lab="oscillateur",n=5,time=3.8))
        np.testing.assert_allclose(a["charts"][0]["series"][0]["y"],b["charts"][0]["series"][0]["y"],atol=1e-14)


class Entanglement(unittest.TestCase):
    def test_polarization_bell_joint_probabilities(self):
        rho=q.pair_density(1);a,b=.3,.8
        expected=np.array([math.cos(a-b)**2,math.sin(a-b)**2,math.sin(a-b)**2,math.cos(a-b)**2])/2
        np.testing.assert_allclose(q.pair_probabilities(rho,a,b),expected,atol=4e-16)

    def test_density_positive_and_trace_one(self):
        for state in ["werner","classique"]:
            for visibility in [0,.3,.7,1]:
                rho=q.pair_density(visibility,state)
                self.assertAlmostEqual(float(np.trace(rho).real),1,places=14)
                self.assertGreaterEqual(np.linalg.eigvalsh(rho)[0],-1e-14)

    def test_non_signalling_for_every_remote_angle(self):
        for state in ["werner","classique"]:
            for b in np.linspace(-math.pi,math.pi,13):
                probabilities=q.pair_probabilities(q.pair_density(.83,state),.6,b)
                self.assertAlmostEqual(float(probabilities.sum()),1,places=14)
                self.assertAlmostEqual(float(probabilities[:2].sum()),.5,places=14)
                self.assertAlmostEqual(float(probabilities[[0,2]].sum()),.5,places=14)

    def test_default_chsh_is_tsirelson_value(self):
        r=q.calculate(dict(lab="intrication"))["theory"]
        self.assertAlmostEqual(r["CHSH"],2*math.sqrt(2),places=13)

    def test_separability_and_chsh_thresholds_are_distinct(self):
        r=q.calculate(dict(lab="intrication",visibility=.5))["theory"]
        self.assertTrue(r["entangled"])
        self.assertLess(r["CHSH"],2)
        self.assertLess(min(r["partial_transpose_eigenvalues"]),0)
        self.assertFalse(q.calculate(dict(lab="intrication",visibility=1/3))["theory"]["entangled"])

    def test_partial_transpose_spectrum(self):
        for visibility in [0,.4,1]:
            eigen=np.linalg.eigvalsh(q.partial_transpose_b(q.pair_density(visibility)))
            expected=sorted([(1-3*visibility)/4]+[(1+visibility)/4]*3)
            np.testing.assert_allclose(eigen,expected,atol=3e-16)

    def test_classical_correlations_are_separable(self):
        rho=q.pair_density(.7,"classique");a,b=.3,.9
        self.assertAlmostEqual(q.pair_correlation(rho,a,b),.7*math.cos(2*a)*math.cos(2*b),places=14)
        self.assertGreaterEqual(np.linalg.eigvalsh(q.partial_transpose_b(rho))[0],0)
        self.assertFalse(q.calculate(dict(lab="intrication",state="classique"))["theory"]["entangled"])


class Josephson(unittest.TestCase):
    def test_ac_frequency_known_microvolt_scale(self):
        r=q.calculate(dict(lab="josephson",mode="jonction",voltage_uV=1))["theory"]
        self.assertAlmostEqual(r["josephson_frequency_Hz"]/1e6,483.5978484,places=7)

    def test_dc_zero_voltage_current_is_constant(self):
        r=q.calculate(dict(lab="josephson",mode="jonction",voltage_uV=0,phase=90,I1=7))
        np.testing.assert_allclose(r["charts"][0]["series"][0]["y"],7,atol=1e-14)
        self.assertEqual(r["theory"]["josephson_frequency_Hz"],0)

    def test_squid_equal_junctions_factor_two(self):
        self.assertAlmostEqual(float(q.squid_critical(10,10,0)),20,places=13)
        self.assertLess(float(q.squid_critical(10,10,.5)),2e-14)
        self.assertAlmostEqual(float(q.squid_critical(10,10,.25)),10*math.sqrt(2),places=13)

    def test_squid_asymmetric_minimum_and_period(self):
        phis=np.linspace(-1,1,77)
        np.testing.assert_allclose(q.squid_critical(10,7,phis),q.squid_critical(10,7,phis+1),atol=1e-13)
        self.assertAlmostEqual(float(q.squid_critical(10,7,.5)),3,places=14)

    def test_squid_critical_against_phase_maximum(self):
        phase=np.linspace(-math.pi,math.pi,100001);flux=.38
        currents=8*np.sin(phase+math.pi*flux)+11*np.sin(phase-math.pi*flux)
        self.assertAlmostEqual(float(np.max(currents)),float(q.squid_critical(8,11,flux)),places=7)

    def test_junction_and_squid_have_distinct_outputs(self):
        a=q.calculate(dict(lab="josephson",mode="jonction"));b=q.calculate(dict(lab="josephson",mode="squid"))
        self.assertNotEqual(a["metrics"][0]["label"],b["metrics"][0]["label"])
        self.assertNotEqual(a["charts"][0]["title"],b["charts"][0]["title"])


class RabiAndBloch(unittest.TestCase):
    def test_pauli_algebra(self):
        np.testing.assert_allclose(q.SX@q.SY-q.SY@q.SX,2j*q.SZ,atol=1e-14)
        for p in q.PAULI:np.testing.assert_allclose(p@p,np.eye(2),atol=1e-14)

    def test_rabi_unitary_against_diagonalization(self):
        for omega,delta,time in [(1,0,math.pi),(.4,2,.8),(0,0,4),(0,2,3)]:
            eig,V=np.linalg.eigh((delta*q.SZ+omega*q.SX)/2)
            expected=(V*np.exp(-1j*eig*time))@V.conj().T
            U=q.rabi_unitary(omega,delta,time)
            np.testing.assert_allclose(U,expected,atol=1e-14)
            np.testing.assert_allclose(U.conj().T@U,np.eye(2),atol=1e-14)

    def test_pi_and_pi_half_pulses(self):
        for time,prob in [(math.pi,1),(math.pi/2,.5),(2*math.pi,0)]:
            self.assertAlmostEqual(float(q.rabi_probability(1,0,time)),prob,places=14)

    def test_detuning_limits_transition(self):
        omega,delta=1,3;time=math.pi/math.sqrt(10)
        self.assertAlmostEqual(float(q.rabi_probability(omega,delta,time)),.1,places=14)
        psi=q.rabi_unitary(omega,delta,time)@np.array([1,0])
        self.assertAlmostEqual(float(abs(psi[1])**2),.1,places=14)

    def test_bloch_rabi_sign_and_norm(self):
        r=q.calculate(dict(lab="rabi",omega=1,detuning=0,time=math.pi/2))["theory"]
        np.testing.assert_allclose(r["bloch"],[0,-1,0],atol=3e-16)

    def test_rmn_circular_field_scaling(self):
        a=q.calculate(dict(lab="rabi",B0=1,B1_uT=10))["theory"]
        b=q.calculate(dict(lab="rabi",B0=2,B1_uT=20))["theory"]
        self.assertAlmostEqual(a["RMN_larmor_Hz"]/1e6,42.577478461,places=8)
        self.assertAlmostEqual(b["RMN_larmor_Hz"] /a["RMN_larmor_Hz"],2,places=14)
        self.assertAlmostEqual(b["RMN_pi_s"]/a["RMN_pi_s"],.5,places=14)

    def test_bloch_density_eigenvalues_and_purity(self):
        vector=np.array([.3,-.4,.2]);rho=q.bloch_density(vector);r=np.linalg.norm(vector)
        np.testing.assert_allclose(np.linalg.eigvalsh(rho),[(1-r)/2,(1+r)/2],atol=1e-14)
        self.assertAlmostEqual(float(np.trace(rho@rho).real),(1+r*r)/2,places=14)
        np.testing.assert_allclose(q.bloch_vector(rho),vector,atol=1e-14)

    def test_hadamard_and_x_actions(self):
        r=q.calculate(dict(lab="bloch",theta=0,gate="H"))["theory"]
        np.testing.assert_allclose(r["final"],[1,0,0],atol=3e-16)
        r=q.calculate(dict(lab="bloch",theta=0,gate="X"))["theory"]
        np.testing.assert_allclose(r["final"],[0,0,-1],atol=1e-14)

    def test_bloch_mixed_center_stays_center(self):
        for gate in ["H","X","Rx","Ry","Rz"]:
            r=q.calculate(dict(lab="bloch",purity=0,gate=gate))["theory"]
            np.testing.assert_allclose(r["final"],[0,0,0],atol=1e-14)
            self.assertAlmostEqual(r["purity"],.5,places=14)
            self.assertAlmostEqual(r["probability_plus"],.5,places=14)

    def test_rotation_gate_conserves_length_and_measurement_bound(self):
        for gate in ["Rx","Ry","Rz"]:
            r=q.calculate(dict(lab="bloch",theta=70,phi=-35,purity=.6,gate=gate,angle=137,axis_theta=51,axis_phi=45))["theory"]
            self.assertAlmostEqual(np.linalg.norm(r["final"]),.6,places=14)
            self.assertGreaterEqual(r["probability_plus"],0)
            self.assertLessEqual(r["probability_plus"],1)

    def test_three_dimensional_scene_uses_valid_vectors(self):
        for data,index in [(dict(lab="rabi"),1),(dict(lab="bloch",gate="Ry"),0)]:
            scene=q.calculate(data)["charts"][index]["sceneBloch"]
            for v in scene["vectors"]:
                self.assertEqual(len(v["point"]),3)
                self.assertLessEqual(np.linalg.norm(v["point"]),1+1e-14)


class QuantumCircuits(unittest.TestCase):
    def test_bell_preparation_exact_amplitudes(self):
        states=q.bell_circuit_states()
        np.testing.assert_allclose(states[0],[1,0,0,0],atol=1e-14)
        np.testing.assert_allclose(states[1],[1/math.sqrt(2),0,1/math.sqrt(2),0],atol=1e-14)
        np.testing.assert_allclose(states[2],[1/math.sqrt(2),0,0,1/math.sqrt(2)],atol=1e-14)

    def test_bell_local_mixed_global_pure(self):
        final=q.bell_circuit_states()[-1];rho=np.outer(final,final.conj())
        np.testing.assert_allclose(q.partial_trace_b(rho),np.eye(2)/2,atol=1e-14)
        self.assertAlmostEqual(float(np.trace(rho@rho).real),1,places=14)
        r=q.calculate(dict(lab="circuits",mode="bell"))["theory"]
        self.assertAlmostEqual(r["local_purity"],.5,places=14)

    def test_one_grover_iteration_finds_any_marked_state(self):
        for target in range(4):
            states=q.grover_states(target,1)
            expected=np.zeros(4);expected[target]=1
            np.testing.assert_allclose(abs(states[-1])**2,expected,atol=1e-14)

    def test_repeated_grover_obeys_analytic_rotation(self):
        for target in range(4):
            for count in range(5):
                states=q.grover_states(target,count)
                expected=math.sin((2*count+1)*math.pi/6)**2
                self.assertAlmostEqual(float(abs(states[-1][target])**2),expected,places=13)
                for s in states:self.assertAlmostEqual(float(np.vdot(s,s).real),1,places=14)

    def test_extra_iterations_can_reduce_success(self):
        one=q.calculate(dict(lab="circuits",mode="grover",marked=2,iterations=1))["theory"]
        two=q.calculate(dict(lab="circuits",mode="grover",marked=2,iterations=2))["theory"]
        self.assertGreater(one["probabilities"][2],two["probabilities"][2])
        self.assertAlmostEqual(two["probabilities"][2],.25,places=14)


if __name__=="__main__":unittest.main()
