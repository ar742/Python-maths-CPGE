"""Bilans indépendants : Maxwell, flux, raccords, réponses passives et limites."""
from itertools import product
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


def value(result,label):
    return next(item["value"] for item in result["metrics"] if item["label"]==label)


class VacuumTests(unittest.TestCase):
    def test_progressive_cross_products_and_energy(self):
        z=np.linspace(0,1,101)
        E,B,S,mean,uE,uB=m.vacuum_fields(z,.17,130,.6)
        np.testing.assert_allclose(B,np.cross(np.array([0.,0.,1.]),E)/m.C,rtol=1e-14)
        np.testing.assert_allclose(S,m.C*(uE+uB),rtol=1e-14)
        np.testing.assert_allclose(uE,uB,rtol=1e-14)
        self.assertTrue(np.all(S>=0))
        self.assertAlmostEqual(mean[0],130**2*(1+.6**2)/(2*m.Z0))

    def test_period_average_progressive_and_stationary(self):
        times=np.arange(2048)/2048;z=np.array([.13,.27,.36])
        for standing in (False,True):
            for ell in (0,.35,1):
                values=[m.vacuum_fields(z,t,80,ell,standing) for t in times]
                measured=np.mean([row[2] for row in values],axis=0)
                expected=values[0][3]
                np.testing.assert_allclose(measured,expected,atol=1e-12)
                energy=np.mean([row[4]+row[5] for row in values],axis=0)
                target=(1 if standing else .5)*m.EPS0*80**2*(1+ell**2)
                np.testing.assert_allclose(energy,target,rtol=1e-13)

    def test_Maxwell_Faraday_and_local_energy_by_derivatives(self):
        z=np.array([.13,.21,.42]);t=.19;dt=1e-6
        for standing in (False,True):
            minus=m.vacuum_fields(z,t-dt,100,.4,standing);plus=m.vacuum_fields(z,t+dt,100,.4,standing)
            left=m.vacuum_fields(z-dt,t,100,.4,standing);right=m.vacuum_fields(z+dt,t,100,.4,standing)
            dE=(right[0]-left[0])/(2*dt);dB=(plus[1]-minus[1])/(2*dt)
            curl=np.column_stack([-dE[:,1],dE[:,0],np.zeros(len(z))])
            np.testing.assert_allclose(curl,-m.C*dB,rtol=2e-9,atol=1e-7)
            du=((plus[4]+plus[5])-(minus[4]+minus[5]))/(2*dt)
            dS=(right[2]-left[2])/(2*dt)
            np.testing.assert_allclose(m.C*du+dS,0,atol=2e-7)

    def test_stationary_circular_flux_is_instantaneously_zero(self):
        for phase in (.1,.2,.35):
            _,_,S,_,_,_=m.vacuum_fields(np.linspace(0,2,100),phase,200,1,True)
            np.testing.assert_allclose(S,0,atol=4*np.finfo(float).eps*200**2/m.Z0)


class InterfaceTests(unittest.TestCase):
    def test_flux_conservation_many_angles(self):
        for n1,n2 in ((1,1.5),(1.5,1),(.7,3),(3,.7),(2,2)):
            for pol in ("TE","TM"):
                _,_,R,T,_,_=m.fresnel(n1,n2,np.linspace(0,89,301),pol)
                np.testing.assert_allclose(R+T,1,atol=1e-14)
                self.assertTrue(np.all(R>=0));self.assertTrue(np.all(T>=0))

    def test_vector_Maxwell_flux_and_all_boundary_components(self):
        y=np.array([0.,1.,0.])
        for angle in (0,30,math.degrees(math.asin(2/3)),60,88):
            for pol in ("TE","TM"):
                n1,n2=1.5,1.;r,t,R,T,ct,st=m.fresnel(n1,n2,angle,pol)
                si=math.sin(math.radians(angle));ci=math.cos(math.radians(angle))
                ki=np.array([si,0,ci],complex);kr=np.array([si,0,-ci],complex);kt=np.array([st,0,ct],complex)
                Ei=y if pol=="TE" else np.cross(y,ki)
                Er=r*y if pol=="TE" else r*np.cross(y,kr)
                Et=t*y if pol=="TE" else t*np.cross(y,kt)
                Bi=n1/m.C*np.cross(ki,Ei);Br=n1/m.C*np.cross(kr,Er);Bt=n2/m.C*np.cross(kt,Et)
                np.testing.assert_allclose((Ei+Er)[:2],Et[:2],atol=1e-14)
                np.testing.assert_allclose((Bi+Br)[:2],Bt[:2],atol=1e-22)
                self.assertAlmostEqual((n1*n1*(Ei+Er)[2]).real,(n2*n2*Et[2]).real,places=13)
                Si=.5/m.MU0*np.cross(Ei,Bi.conjugate()).real[2]
                Sr=.5/m.MU0*np.cross(Er,Br.conjugate()).real[2]
                St=.5/m.MU0*np.cross(Et,Bt.conjugate()).real[2]
                self.assertAlmostEqual(-Sr/Si,float(R),places=13)
                self.assertAlmostEqual(St/Si,float(T),places=13)

    def test_Brewster_and_TIR_limits(self):
        angle=math.degrees(math.atan(1.5));r,_,R,_,_,_=m.fresnel(1,1.5,angle,"TM")
        self.assertLess(abs(r),2e-16);self.assertLess(float(R),1e-30)
        for pol in ("TE","TM"):
            r,_,R,T,ct,_=m.fresnel(1.5,1,60,pol)
            self.assertAlmostEqual(float(R),1,places=14);self.assertEqual(float(T),0)
            self.assertGreater(ct.imag,0);self.assertAlmostEqual(abs(r),1)
        equal=m.calculate("interfaces",dict(n1=1.5,n2=1.5))
        self.assertIsInstance(value(equal,"Angle de Brewster TM"),str)


class GuideAndApertureTests(unittest.TestCase):
    def test_TE10_boundary_and_transverse_dispersion(self):
        r=m.calculate("guide",dict(width=30,frequency=8))
        E=np.array(r["scene"]["Ey"])
        np.testing.assert_allclose(E[:,[0,-1]],0,atol=5e-13)
        beta,kc,k0=m.guide_beta(.03,8e9)
        self.assertAlmostEqual((beta*beta+kc*kc).real,k0*k0,places=9)
        vg=value(r,"Vitesse de groupe");vp=value(r,"Vitesse de phase")
        self.assertAlmostEqual(vg*vp/m.C**2,1,places=14)
        self.assertLess(vg,m.C);self.assertGreater(vp,m.C)

    def test_power_integrates_independent_Poynting(self):
        a=.03;f=8e9;E0=80;beta,kc,_=m.guide_beta(a,f);omega=2*np.pi*f
        x=np.linspace(0,a,10001);Ey=E0*np.sin(kc*x);Bx=-beta/omega*Ey
        integral=np.trapezoid(-.5/m.MU0*np.real(Ey*np.conjugate(Bx)),x)
        r=m.calculate("guide",dict(width=30,frequency=8,amplitude=80))
        self.assertAlmostEqual(integral/value(r,"Puissance moyenne par hauteur"),1,places=13)

    def test_guide_cutoff_and_evanescent_flux(self):
        r=m.calculate("guide",dict(width=30,frequency=3))
        self.assertEqual(value(r,"Re β"),0);self.assertGreater(value(r,"Im β"),0)
        self.assertEqual(value(r,"Puissance moyenne par hauteur"),0)
        beta,_,_=m.guide_beta(.03,m.C/.06);self.assertEqual(beta,0)
        r=m.calculate("guide",dict(width=30,frequency=m.C/.06/1e9))
        self.assertEqual(value(r,"Régime"),"Coupure");self.assertIsInstance(value(r,"Vitesse de groupe"),str)

    def test_aperture_sinc_is_integral_of_phase(self):
        x=np.linspace(-2,2,20001);angles=np.array([-40.,-15,0,20,45])
        numerical=[abs(np.trapezoid(np.exp(2j*np.pi*x*(math.sin(math.radians(a))-math.sin(math.radians(20)))),x)/4)**2 for a in angles]
        np.testing.assert_allclose(m.aperture_pattern(angles,4,20),numerical,atol=2e-9)

    def test_no_fictitious_zero_for_small_aperture(self):
        small=m.calculate("antenne",dict(aperture=.5,steering=0))
        self.assertEqual(small["scene"]["zeros"],[])
        narrow=m.calculate("antenne",dict(aperture=4,steering=0))
        np.testing.assert_allclose(narrow["scene"]["zeros"],[-math.degrees(math.asin(.25)),math.degrees(math.asin(.25))])
        np.testing.assert_allclose(m.aperture_pattern(narrow["scene"]["zeros"],4),0,atol=1e-30)


class PassiveMatterTests(unittest.TestCase):
    def test_Drude_causality_and_conductivity(self):
        for r in (.1,.5,1,1.5,3):
            for nu in (0,.05,1):
                epsilon=m.drude_epsilon(r,nu);n=m.passive_sqrt(epsilon)
                self.assertGreaterEqual(epsilon.imag,0);self.assertGreaterEqual(float(n.imag),0)
                np.testing.assert_allclose(n*n,epsilon,atol=3e-14)
                sigma=1/(nu-1j*r)
                self.assertAlmostEqual(epsilon.real,(1+1j*sigma/r).real)
                self.assertAlmostEqual(epsilon.imag,(1+1j*sigma/r).imag)

    def test_lossless_plasma_cutoff_and_group_velocity_relation(self):
        np.testing.assert_allclose(m.passive_sqrt(m.drude_epsilon(2,0)),math.sqrt(.75))
        n=m.passive_sqrt(m.drude_epsilon(.5,0));self.assertEqual(float(n.real),0)
        self.assertAlmostEqual(float(n.imag),math.sqrt(3))
        r=m.calculate("plasma",dict(ratio=.5,collision=0))
        self.assertEqual(value(r,"Flux à z=0"),0)
        cutoff=m.calculate("plasma",dict(ratio=1,collision=0));self.assertEqual(value(cutoff,"Re n"),0)

    def test_plasma_spatial_sampling_resolves_phase_and_attenuation(self):
        for ratio,collision in ((3,0),(.1,0),(.75,.4),(3,1)):
            r=m.calculate("plasma",dict(ratio=ratio,collision=collision,density=100,length=30))
            s=r["scene"];z=np.array(s["z_m"]);dx=np.max(np.diff(z))
            self.assertEqual(z[0],0);self.assertEqual(z[-1],.3)
            self.assertLessEqual(dx*s["k_real"],2*np.pi/16*(1+1e-12))
            self.assertLessEqual(dx*s["k_imag"],1/12*(1+1e-12))
            self.assertLessEqual(len(z),6800)

    def test_plasma_Poynting_gradient_equals_Joule(self):
        r=m.calculate("plasma",dict(ratio=.75,collision=.4,density=2,amplitude=40,length=1))
        k=r["scene"]["k_imag"];S=np.array(r["scene"]["poynting"]);q=np.array(r["scene"]["joule"])
        np.testing.assert_allclose(2*k*S,q,rtol=1e-13)
        self.assertTrue(np.all(q>0));self.assertTrue(np.all(np.diff(S)<0))
        z=np.linspace(0,r["scene"]["z_m"][-1],10001)
        omega_plasma=math.sqrt(2e18*m.E_CHARGE**2/(m.EPS0*m.ME))
        omega=.75*omega_plasma;nu=.4*omega_plasma
        conductivity=2e18*m.E_CHARGE**2/(m.ME*(nu-1j*omega))
        independent_q=.5*conductivity.real*40**2*np.exp(-2*k*z)
        self.assertLess(abs(np.trapezoid(independent_q,z)-(S[0]-S[-1]))/S[0],1e-8)

    def test_Lorentz_passivity_static_high_frequency_and_resonance(self):
        r=np.linspace(.01,3,1000);eps=m.lorentz_epsilon(r,2,.08,1.5)
        self.assertTrue(np.all(eps.imag>0));self.assertTrue(np.all(m.passive_sqrt(eps).imag>0))
        self.assertEqual(m.lorentz_epsilon(0,2,.08,1.5),3.5)
        self.assertAlmostEqual(m.lorentz_epsilon(1e8,2,.08,1.5).real,1.5,places=14)
        self.assertAlmostEqual(m.lorentz_epsilon(1,2,.08,1.5).imag,25)

    def test_sphere_all_electrostatic_boundary_conditions(self):
        eps=3.5;E0=100;a=.004;Ein,P,dipole=m.dielectric_sphere(eps,E0,a)
        for theta in np.linspace(0,np.pi,15):
            n=np.array([math.sin(theta),0,math.cos(theta)]);outside=np.array([0.,0.,E0])+dipole/(4*np.pi*m.EPS0*a**3)*(3*n[2]*n-np.array([0.,0.,1.]))
            inside=np.array([0.,0.,Ein]);t=np.array([math.cos(theta),0,-math.sin(theta)])
            self.assertAlmostEqual(float(t@(outside-inside)),0,places=12)
            self.assertAlmostEqual(float(n@outside),float(eps*n@inside),places=12)
            self.assertAlmostEqual(m.EPS0*float(n@(outside-inside)),P*n[2],places=18)
        theta=np.linspace(0,np.pi,10001)
        self.assertLess(abs(np.trapezoid(P*np.cos(theta)*2*np.pi*a*a*np.sin(theta),theta)),1e-25)


class MagnetismTests(unittest.TestCase):
    def test_Langevin_limits_oddness_and_nontrivial_distribution(self):
        self.assertEqual(float(m.langevin(0)),0)
        self.assertAlmostEqual(float(m.langevin(1e-8))/1e-8,1/3,places=14)
        self.assertAlmostEqual(float(m.langevin(100)),.99,places=14)
        x=np.array([1e-5,.2,1,5]);np.testing.assert_allclose(m.langevin(-x),-m.langevin(x),atol=1e-15)
        u=np.linspace(-1,1,100001)
        for x in (.3,1,4):
            numerical=np.trapezoid(u*np.exp(x*u),u)/np.trapezoid(np.exp(x*u),u)
            self.assertAlmostEqual(numerical,float(m.langevin(x)),places=8)

    def test_diamagnetism_negative_and_temperature_independent(self):
        values=[m.calculate("aimantation",dict(model="dia",temperature=T,field=2)) for T in (1,100,500)]
        susceptibilities=[value(r,"χ intrinsèque à faible champ") for r in values]
        self.assertEqual(susceptibilities[0],susceptibilities[1]);self.assertEqual(susceptibilities[1],susceptibilities[2])
        self.assertLess(susceptibilities[0],0);self.assertLess(value(values[0],"Aimantation M"),0)

    def test_demagnetization_self_consistency_and_apparent_slope(self):
        for model in ("classique","quantique","dia"):
            r=m.calculate("aimantation",dict(model=model,temperature=10,field=.8,demag=.4))
            Hin=value(r,"Champ interne H");M=value(r,"Aimantation M");Hext=value(r,"Champ extérieur H")
            self.assertLess(abs(Hin+.4*M-Hext),2e-9)
            little=m.calculate("aimantation",dict(model=model,temperature=10,field=1e-7,demag=.4))
            slope=value(little,"Aimantation M")/value(little,"Champ extérieur H")
            self.assertAlmostEqual(slope/value(little,"χ apparente χ/(1+Nχ)"),1,places=10)

    def test_quantum_saturation_and_Curie_factor_three(self):
        params=dict(temperature=100,field=0,demag=0)
        a=m.calculate("aimantation",dict(params,model="classique"));b=m.calculate("aimantation",dict(params,model="quantique"))
        self.assertAlmostEqual(value(b,"χ intrinsèque à faible champ")/value(a,"χ intrinsèque à faible champ"),3)
        M=m.magnetization_law(1e10,1,1e27,m.MU_B,"quantique",1e-10)
        self.assertAlmostEqual(float(M)/(1e27*m.MU_B),1,places=14)

    def test_London_boundaries_current_signs_and_integral(self):
        a=200e-9;lam=50e-9;B0=.02;x=np.linspace(-a,a,10001)
        B,j=m.london_profile(x,a,lam,B0)
        np.testing.assert_allclose(B[[0,-1]],B0,rtol=1e-14)
        np.testing.assert_allclose(B,B[::-1],atol=1e-17);np.testing.assert_allclose(j,-j[::-1],atol=.001)
        self.assertGreater(j[0],0);self.assertLess(j[-1],0)
        self.assertAlmostEqual(B[len(x)//2]/B0,1/math.cosh(a/lam),places=14)
        integral=np.trapezoid(j[len(x)//2:],x[len(x)//2:]);expected=-(B0-B[len(x)//2])/m.MU0
        self.assertLess(abs(integral/expected-1),1e-7)
        dx=1e-12;center=.7*a;Bp,jp=m.london_profile(center+dx,a,lam,B0);Bm,jm=m.london_profile(center-dx,a,lam,B0)
        self.assertAlmostEqual(float((jp-jm)/(2*dx))/(-float(m.london_profile(center,a,lam,B0)[0])/(m.MU0*lam**2)),1,places=9)

    def test_London_thick_limit_and_initial_memory(self):
        B,j=m.london_profile(np.array([-1.,0,1.]),1.,.001,1.)
        np.testing.assert_allclose(B,[1,0,1]);self.assertTrue(np.all(np.isfinite(j)))
        a=m.calculate("meissner",dict(history="refroidi_champ",field=20));b=m.calculate("meissner",dict(history="champ_apres",field=20))
        self.assertEqual(a["scene"]["B_mT"],b["scene"]["B_mT"])
        self.assertEqual(a["scene"]["B_perfect_mT"],20);self.assertEqual(b["scene"]["B_perfect_mT"],0)


class PolarizationKerrRadiationTests(unittest.TestCase):
    def test_circular_phases_equal_Jones_rotation(self):
        eplus=np.array([1,1j])/np.sqrt(2);eminus=eplus.conjugate()
        for theta in (-2,-.4,0,.7,3):
            circular=(np.exp(-1j*theta)*eplus+np.exp(1j*theta)*eminus)/np.sqrt(2)
            np.testing.assert_allclose(circular,m.jones_rotation(theta)@np.array([1.,0]),atol=4e-16)
            R=m.jones_rotation(theta)
            np.testing.assert_allclose(R.T@R,np.eye(2),atol=3e-16)
            np.testing.assert_allclose(R@R,m.jones_rotation(2*theta),atol=3e-16)

    def test_faraday_sign_return_and_Malus(self):
        a=m.calculate("faraday",dict(passes="simple",field=.5));b=m.calculate("faraday",dict(passes="double",field=.5));c=m.calculate("faraday",dict(passes="double",field=-.5))
        self.assertAlmostEqual(value(b,"Rotation totale"),2*value(a,"Rotation totale"))
        self.assertAlmostEqual(value(c,"Rotation totale"),-value(b,"Rotation totale"))
        self.assertAlmostEqual(value(a,"Transmission de l'analyseur"),math.sin(1.)**2)
        delta=value(a,"n− − n+ déduit de Verdet");wavelength=a["params"]["wavelength"]*1e-9;L=a["params"]["length"]*.01
        self.assertAlmostEqual(math.pi*delta*L/wavelength,a["scene"]["theta_single"])

    def test_sech_solves_physical_ODE_and_width_scaling(self):
        wavelength=1e-6;n0=1.5;n2=3e-20;I0=1e14
        width,k,E0,A,beta=m.kerr_soliton_parameters(wavelength,n0,n2,I0);k0=2*np.pi/wavelength
        self.assertAlmostEqual(width*math.sqrt(A),1)
        self.assertAlmostEqual(E0**2/(2*A/(beta*k0*k0)),1)
        x=np.linspace(-4,4,101);E=E0/np.cosh(x);Esecond=E*(1-2/np.cosh(x)**2)/width**2
        residual=(Esecond-(A*E-beta*k0*k0*E**3))/(A*E0)
        np.testing.assert_allclose(residual,0,atol=2e-15)
        other=m.kerr_soliton_parameters(wavelength,n0,n2,4*I0)[0]
        self.assertAlmostEqual(other/width,.5)

    def test_kerr_reference_power_and_index(self):
        a=m.calculate("kerr",dict(distance=0));b=m.calculate("kerr",dict(distance=3))
        x=np.linspace(-30,30,20001)
        Isech=1/np.cosh(x)**2
        ratio=value(a,"Indice effectif k/k₀")/a["params"]["n0"]
        for Z in (0,1,3):
            spread=math.sqrt(1+Z*Z);gauss=2*ratio/np.sqrt(np.pi)/spread*np.exp(-x*x/spread**2)
            self.assertAlmostEqual(np.trapezoid(gauss,x),ratio*np.trapezoid(Isech,x),places=13)
        self.assertAlmostEqual(max(a["scene"]["linear_intensity"]),2*ratio/math.sqrt(math.pi),places=14)
        self.assertEqual(a["scene"]["intensity"],b["scene"]["intensity"])
        self.assertLess(max(b["scene"]["linear_intensity"]),max(a["scene"]["linear_intensity"]))
        self.assertGreater(max(a["scene"]["index"]),a["params"]["n0"])

    def test_dipole_integral_and_omega_fourth(self):
        omega=2*np.pi*1e14;p0=1e-29;theta=np.linspace(0,np.pi,20001)
        differential=p0*p0*omega**4*np.sin(theta)**2/(32*np.pi**2*m.EPS0*m.C**3)
        numerical=np.trapezoid(differential*2*np.pi*np.sin(theta),theta)
        self.assertAlmostEqual(numerical/m.dipole_power(p0,omega),1,places=13)
        self.assertEqual(m.dipole_power(p0,2*omega)/m.dipole_power(p0,omega),16)

    def test_bound_radiation_power_crosssection_and_limits(self):
        r=m.calculate("rayonnement",dict(model="lie",frequency=500,resonance=500,damping=.05))
        self.assertAlmostEqual(value(r,"Puissance rayonnée moyenne")/value(r,"I incident × σ"),1,places=13)
        self.assertAlmostEqual(m.bound_cross_section(1e-5,.05)/m.SIGMA_THOMSON/(1e-5)**4,1,places=9)
        self.assertAlmostEqual(m.bound_cross_section(1e6,.05)/m.SIGMA_THOMSON,1,places=11)
        self.assertAlmostEqual(m.bound_cross_section(1,.05)/m.SIGMA_THOMSON,400,places=12)


class DynamoTests(unittest.TestCase):
    def test_helical_field_curl_and_divergence(self):
        k=.13;z=np.linspace(0,2*np.pi/k,40001);dz=z[1]-z[0]
        for s in (-1,1):
            Bx=np.cos(k*z);By=-s*np.sin(k*z)
            curl=np.column_stack([-np.gradient(By,dz),np.gradient(Bx,dz),np.zeros_like(z)])
            field=np.column_stack([Bx,By,np.zeros_like(z)])
            np.testing.assert_allclose(curl[1:-1],s*k*field[1:-1],rtol=1e-8,atol=1e-12)

    def test_growth_versus_diffusion_and_energy_budget(self):
        alpha=.0001;eta=1;L=1e6
        g,k=m.dynamo_growth(alpha,eta,L,1)
        self.assertGreater(g,0);self.assertLess(m.dynamo_growth(alpha,eta,L,-1)[0],0)
        self.assertLess(m.dynamo_growth(0,eta,L,1)[0],0)
        r=m.calculate("dynamo")
        rates=value(r,"Production relative d'énergie")-value(r,"Dissipation relative d'énergie")
        self.assertAlmostEqual(rates,2*value(r,"Taux de croissance du mode"),places=20)
        B=3e-3;dt=10.;energy=lambda t:B*B*math.exp(2*g*t)/(2*m.MU0)
        self.assertAlmostEqual((energy(dt)-energy(-dt))/(2*dt)/energy(0)/(2*g),1,places=8)

    def test_large_Rm_does_not_impose_growth(self):
        r=m.calculate("dynamo",dict(alpha=0,velocity=10,length=3500))
        self.assertGreater(value(r,"Rm=UL/ηm"),10000)
        self.assertLess(value(r,"Taux de croissance du mode"),0)

    def test_logarithmic_growth_stays_exact_at_extreme_decay(self):
        r=m.calculate("dynamo",dict(alpha=-1,diffusivity=10,length=1,years=100))
        log=value(r,"log₁₀(|B|/B₀)");g=value(r,"Taux de croissance du mode")
        self.assertAlmostEqual(log,g*100*m.YEAR/math.log(10))
        self.assertLess(log,-10000);self.assertIsInstance(value(r,"Amplitude du mode"),str)
        json.dumps(r,allow_nan=False)


class ContractTests(unittest.TestCase):
    def test_every_preset_has_finite_reproducible_results(self):
        self.assertEqual(len(LABS),12)
        for item in LABS:
            self.assertGreaterEqual(len(item["presets"]),3)
            for preset in item["presets"]:
                with self.subTest(lab=item["id"],preset=preset["label"]):
                    r=m.calculate(item["id"],preset["values"])
                    self.assertEqual(m.calculate(item["id"],r["params"]),r)
                    json.dumps(r,allow_nan=False)
                    self.assertTrue(r["steps"]);self.assertTrue(r["assumptions"]);self.assertTrue(r["scene"]["description"])
                    for chart in r["charts"]:
                        for s in chart["series"]:
                            self.assertEqual(len(s["x"]),len(s["y"]))
                            self.assertTrue(np.all(np.isfinite(s["x"])));self.assertTrue(np.all(np.isfinite(s["y"])))

    def test_all_bounded_corners_and_selections_are_finite(self):
        for item in LABS:
            ranges=[c for c in item["controls"] if c["type"]=="range"]
            selections=[c for c in item["controls"] if c["type"]=="select"]
            corners=list(product(*[(c["min"],c["max"]) for c in ranges]))
            choices=list(product(*[[o["value"] for o in c["options"]] for c in selections])) or [()]
            for corner in corners:
                for selection in choices:
                    parameters={c["key"]:v for c,v in zip(ranges,corner)}
                    parameters.update({c["key"]:v for c,v in zip(selections,selection)})
                    with self.subTest(lab=item["id"],params=parameters):json.dumps(m.calculate(item["id"],parameters),allow_nan=False)

    def test_validation_unknowns_bools_and_nonfinite(self):
        with self.assertRaises(ValueError):m.calculate("inconnu")
        for data in ({"mode":"inconnu"},{"amplitude":False},{"amplitude":math.nan},{"amplitude":math.inf},{"amplitude":10**500},{"amplitude":1001},{"foo":1}):
            with self.subTest(data=data),self.assertRaises(ValueError):m.calculate("maxwell",data)


if __name__=="__main__":unittest.main()
