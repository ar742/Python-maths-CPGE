"""Contrôles indépendants : unités, bilans, limites et arrêt des modèles."""
import json
import math
import unittest
import numpy as np
from commun import clean, integrate
from catalogue_effets import LABS
from contenu_effets import LESSONS, EXERCISES, GUIDES
from modeles_effets import (COMPUTE,SIGMA,RWATER,leslie_power,seebeck_voltage,seebeck_inverse,
    peltier_flows,acoustic_branches,piezo_energy,piezo_response,saturation_log_ratio,condensation_margin)


def calculate(id_,**changes):
    lab=next(item for item in LABS if item['id']==id_)
    params={control['key']:control['value'] for control in lab['controls']}; params.update(changes)
    return COMPUTE[id_](params)


def values(out):
    return {item['label']:item['value'] for item in out['metrics']}


class Radiation(unittest.TestCase):
    def test_net_power_and_surface_ratio(self):
        rad,conv=leslie_power(373,293,.01,.95,8)
        self.assertAlmostEqual(float(rad),.95*SIGMA*.01*(373**4-293**4),places=12)
        self.assertAlmostEqual(float(conv),6.4,places=12)
        self.assertAlmostEqual(float(rad)/float(leslie_power(373,293,.01,.04,8)[0]),.95/.04,places=12)

    def test_equilibrium_and_incoming_heat(self):
        self.assertEqual(leslie_power(293,293,.01,.95,8),(0,0))
        radiation,convection=leslie_power(280,300,.01,.95,8)
        self.assertLess(radiation,0); self.assertLess(convection,0)
        out=calculate('cube_leslie',T=300,Tamb=320)
        cooling=out['charts'][2]['series'][0]['y']
        self.assertTrue(np.all(np.diff(cooling)>=-1e-12))
        self.assertTrue(np.all(cooling<=320))

    def test_cooling_obeys_integrated_first_principle(self):
        out=calculate('cube_leslie',T=400,Tamb=293,side=.1,h=8,capacity=900)
        curve=out['charts'][2]['series'][0]; t=np.asarray(curve['x']); temp=np.asarray(curve['y'])
        lost=SIGMA*.01*(.95+.90+.35+.04+.95+.95)*(temp**4-293**4)+6*8*.01*(temp-293)
        stored=900*(400-temp[-1]); escaped=float(integrate(lost,t))
        self.assertAlmostEqual(escaped/stored,1,delta=2e-6)
        self.assertTrue(np.all(np.diff(temp)<=1e-12)); self.assertTrue(np.all(temp>=293))


class Thermocouple(unittest.TestCase):
    def test_nonlinear_calibration_against_hand_calculation(self):
        measured=seebeck_voltage(473.15,293.15,40e-6,.02e-6)
        self.assertAlmostEqual(float(measured),.007596,places=14)
        t=np.linspace(293.15,473.15,101)
        independent=float(integrate(40e-6+.02e-6*(t-273.15),t))
        self.assertAlmostEqual(float(measured),independent,places=14)

    def test_inverse_and_zero_voltage(self):
        for slope in [-.03e-6,0,.03e-6]:
            for hot,cold in [(250,330),(423.15,293.15),(650,250)]:
                voltage=seebeck_voltage(hot,cold,30e-6,slope)
                self.assertAlmostEqual(float(seebeck_inverse(voltage,cold,30e-6,slope)),hot,places=10)
            self.assertAlmostEqual(float(seebeck_inverse(0,300,30e-6,slope)),300,places=12)

    def test_reference_error_for_constant_coefficient(self):
        out=values(calculate('seebeck',Th=423.15,Tc=293.15,S0=40,slope=0,cold_error=5))
        self.assertAlmostEqual(out['Tension à circuit ouvert'],5.2,places=12)
        self.assertAlmostEqual(out['Erreur de température correspondante'],5,places=12)
        self.assertAlmostEqual(out['Température si Tf est supposée à 273,15 K'],403.15,places=10)

    def test_monotone_branch_for_all_calibration_extremes(self):
        for S0 in [30e-6,60e-6]:
            for slope in [-.03e-6,.03e-6]:
                self.assertTrue(np.all(S0+slope*(np.linspace(240,710,301)-273.15)>0))


class PeltierBalance(unittest.TestCase):
    def test_independent_integer_balance(self):
        Qc,Qh,P=peltier_flows(280,300,4,.05,2,1)
        self.assertEqual(float(Qc),20); self.assertEqual(float(Qh),56); self.assertEqual(float(P),36)
        out=values(calculate('peltier',Tc=280,delta=20,I=4,alpha=.05,R=2,K=1))
        self.assertAlmostEqual(out['Coefficient de performance Qc/P'],5/9,places=12)

    def test_energy_entropy_and_carnot_bound(self):
        rng=np.random.default_rng(71)
        for _ in range(100):
            Tc=float(rng.uniform(260,310)); delta=float(rng.uniform(1,60)); Th=Tc+delta
            I=float(rng.uniform(0,10)); alpha=float(rng.uniform(.01,.08)); R=float(rng.uniform(.5,4)); K=float(rng.uniform(.1,2))
            Qc,Qh,P=peltier_flows(Tc,Th,I,alpha,R,K)
            self.assertAlmostEqual(float(Qh-Qc),float(P),delta=2e-12)
            sigma=Qh/Th-Qc/Tc
            expected=R*I*I/2*(1/Th+1/Tc)+K*delta*(1/Tc-1/Th)
            self.assertAlmostEqual(float(sigma),float(expected),delta=2e-14)
            self.assertGreaterEqual(sigma,-2e-14)
            if Qc>0: self.assertLessEqual(Qc/P,Tc/delta+1e-12)

    def test_unavailable_cop_is_explicit(self):
        zero=values(calculate('peltier',I=0))
        excessive=values(calculate('peltier',I=10,alpha=.03,R=2))
        self.assertLess(zero['Chaleur extraite Qc'],0)
        self.assertIn('Non défini',zero['Coefficient de performance Qc/P'])
        self.assertLess(excessive['Chaleur extraite Qc'],0)
        self.assertEqual(excessive['Coefficient de performance Qc/P'],'Pas de refroidissement')

    def test_optimum_and_equilibrium(self):
        I=7; optimum=float(peltier_flows(280,300,I,.05,2,1)[0])
        self.assertAlmostEqual(optimum,29,places=12)
        self.assertGreater(optimum,float(peltier_flows(280,300,I+.5,.05,2,1)[0]))
        self.assertGreater(optimum,float(peltier_flows(280,300,I-.5,.05,2,1)[0]))
        out=values(calculate('peltier',Tc=280,delta=20,I=4,alpha=.05,R=2,K=1,load=10))
        cold=out['Température d’équilibre pour la charge choisie']
        self.assertAlmostEqual(cold,326/1.2,places=10)
        self.assertAlmostEqual(float(peltier_flows(cold,300,4,.05,2,1)[0]),10,places=10)


class CoupledAcoustic(unittest.TestCase):
    def test_both_branches_satisfy_original_coupled_equations(self):
        P,T,rho,gamma=100000,293,1.2,1.4
        for lam in [1e-6,.026,50,100]:
            for omega in [2*math.pi*20,2*math.pi*6000,2*math.pi*20000]:
                ka,kt,ratio,c,rhocp=acoustic_branches(omega,lam,P,T,rho,gamma)
                for k in [complex(ka),complex(kt)]:
                    s=gamma*omega**2/c**2
                    # Normaliser par τ pour la branche thermique évite de diviser
                    # par iωρcₚ+λk², presque nul dans la limite λ→0.
                    if abs(k)>10*omega/c:
                        tau=1; pressure=s*P/T/(s-k*k)
                    else:
                        pressure=1; tau=1j*omega/(1j*omega*rhocp+lam*k*k)
                    equations=[
                        [s*pressure,-k*k*pressure,-s*P/T*tau],
                        [1j*omega*rhocp*tau,lam*k*k*tau,-1j*omega*pressure]]
                    for terms in equations:
                        self.assertLess(abs(sum(terms))/sum(abs(v) for v in terms),3e-13)
                    self.assertLessEqual(k.imag,0)
                self.assertAlmostEqual(abs(complex(ratio)-1j*omega/(1j*omega*rhocp+lam*complex(ka)**2)),0,places=13)

    def test_adiabatic_and_isothermal_limits(self):
        omega=2*math.pi*20000; P,T,rho,gamma=100000,293,1.2,1.4
        k,thermal,ratio,c,_=acoustic_branches(omega,0,P,T,rho,gamma)
        self.assertIsNone(thermal)
        self.assertAlmostEqual(complex(k).real,omega/c,places=12)
        self.assertEqual(complex(k).imag,0)
        self.assertAlmostEqual(complex(ratio).real,(gamma-1)*T/(gamma*P),places=15)
        k,_,_,_,_=acoustic_branches(omega,1e6,P,T,rho,gamma)
        self.assertAlmostEqual(omega/complex(k).real,c/math.sqrt(gamma),delta=1e-4)

    def test_low_conduction_attenuation_approximation(self):
        omega=2*math.pi*6000; lam=1e-6; gamma=1.4
        k,_,ratio,c,rhocp=acoustic_branches(omega,lam,100000,293,1.2,gamma)
        first_order=lam*(gamma-1)*omega**2/(2*rhocp*c**3)
        self.assertAlmostEqual(-complex(k).imag/first_order,1,delta=2e-7)
        self.assertGreater(complex(ratio).imag,0)  # Avance pour exp(iωt).

    def test_physical_branch_and_dispersion_residual(self):
        frequencies=np.geomspace(20,20000,81)
        for gamma in [1.1,1.4,1.8]:
            for lam in [0,1e-10,.026,100]:
                k,_,_,c,_=acoustic_branches(2*np.pi*frequencies,lam,100000,293,1.2,gamma)
                self.assertTrue(np.all(k.real>0)); self.assertTrue(np.all(k.imag<=0))
                speed=2*np.pi*frequencies/k.real
                self.assertTrue(np.all(speed<=c*(1+1e-12)))
                self.assertTrue(np.all(speed>=c/math.sqrt(gamma)*(1-1e-12)))
        out=values(calculate('thermoacoustique',conductivity=50,frequency=12000))
        self.assertLess(out['Résidu relatif de dispersion'],1e-13)


class ReciprocalPiezo(unittest.TestCase):
    def test_energy_derivatives_and_cross_derivatives(self):
        k,C,theta=3.,2.,.7; x,q=.2,-.3; h=1e-5
        dqx=(piezo_energy(x+h,q+h,k,C,theta)-piezo_energy(x+h,q-h,k,C,theta)
             -piezo_energy(x-h,q+h,k,C,theta)+piezo_energy(x-h,q-h,k,C,theta))/(4*h*h)
        self.assertAlmostEqual(float(dqx),-theta/C,delta=1e-7)
        V=(q-theta*x)/C; force=k*x-theta*V
        dUdx=(piezo_energy(x+h,q,k,C,theta)-piezo_energy(x-h,q,k,C,theta))/(2*h)
        dUdq=(piezo_energy(x,q+h,k,C,theta)-piezo_energy(x,q-h,k,C,theta))/(2*h)
        self.assertAlmostEqual(float(dUdx),force,places=10)
        self.assertAlmostEqual(float(dUdq),V,places=10)
        self.assertGreater(piezo_energy(x,q,k,C,theta),0)
        self.assertAlmostEqual((k+theta**2/C)/C-(-theta/C)**2,k/C,places=12)

    def test_lossless_antiresonance_and_coupling_shift(self):
        m,k,C,theta=2e-4,1e6,1e-9,.01
        wr=math.sqrt(k/m); wa=math.sqrt((k+theta**2/C)/m)
        _,_,Y=piezo_response(wa,m,k,C,theta,0)
        self.assertLess(abs(complex(Y))/(wa*C),2e-14)
        self.assertAlmostEqual((wa/wr)**2-1,.1,places=13)
        out=values(calculate('piezo_resonateur'))
        self.assertAlmostEqual(out['Résonance : repère sans pertes fᵣ'],wr/(2*math.pi)/1000,places=12)

    def test_passivity_and_power_identity(self):
        m,k,C,theta,r,V=2e-4,1e6,1e-9,.01,.3,2
        for omega in [1000,math.sqrt(k/m),90000]:
            X,_,Y=map(complex,piezo_response(omega,m,k,C,theta,r,V))
            expected=theta**2*r*omega**2/((k-m*omega**2)**2+(r*omega)**2)
            self.assertAlmostEqual(Y.real/expected,1,places=12)
            self.assertGreater(Y.real,0)
            self.assertAlmostEqual((V*V*Y.real)/(r*omega**2*abs(X)**2),1,places=12)

    def test_zero_coupling_leaves_a_capacitor(self):
        omega=12345; X,Q,Y=piezo_response(omega,2e-4,1e6,1e-9,0,.3,2)
        self.assertEqual(complex(X),0)
        self.assertAlmostEqual(complex(Q).real,2e-9,places=18)
        self.assertEqual(complex(Y),1j*omega*1e-9)


class CondensationOnset(unittest.TestCase):
    def test_integrated_saturation_and_clapeyron_derivative(self):
        Tstar,L,B=293.15,2.44e6,2370; A=L+B*Tstar
        self.assertEqual(float(saturation_log_ratio(Tstar,Tstar,A,B)),0)
        for T in [280,293.15,310]:
            h=.001
            derivative=(saturation_log_ratio(T+h,Tstar,A,B)-saturation_log_ratio(T-h,Tstar,A,B))/(2*h)
            self.assertAlmostEqual(float(derivative),(A-B*T)/(RWATER*T*T),delta=2e-11)

    def test_mass_and_molar_units_give_identical_saturation(self):
        M=.018; A,B,T,Tstar=3.134765e6,2370,288.15,293.15
        mass=saturation_log_ratio(T,Tstar,A,B,RWATER)
        molar=saturation_log_ratio(T,Tstar,A*M,B*M,RWATER*M)
        self.assertAlmostEqual(float(mass),float(molar),places=14)

    def test_initial_criterion_equivalent_to_temperature_threshold(self):
        for T in [250,320,380]:
            for latent in [.2e6,1e6,2.8e6]:
                for gamma in [1.1,1.33,1.67]:
                    B=2370; A=latent+B*T
                    threshold=A*(gamma-1)/(RWATER*gamma+B*(gamma-1))
                    self.assertEqual(condensation_margin(T,latent,gamma)>0,T<threshold)

    def test_condensation_stops_gas_law_at_initial_state(self):
        out=calculate('brouillard'); gas=out['charts'][0]['series'][1]
        self.assertEqual(list(gas['x']),[293.15]); self.assertEqual(list(gas['y']),[1])
        self.assertTrue(out['scene']['apparatus']['gas_law_stopped'])
        self.assertAlmostEqual(values(out)['Dernière température de vapeur seule tracée'],293.15)

    def test_no_condensation_retains_the_whole_single_phase_interval(self):
        out=calculate('brouillard',Tstar=320,latent_MJ=.2,B=1500,gamma=1.33,drop=10)
        gas=out['charts'][0]['series'][1]
        self.assertAlmostEqual(float(gas['x'][0]),310)
        self.assertFalse(out['scene']['apparatus']['condensation'])
        T=np.asarray(gas['x']); A=.2e6+1500*320
        self.assertTrue(np.all(np.asarray(gas['y'])<=np.exp(saturation_log_ratio(T,320,A,1500))*(1+1e-12)))

    def test_delayed_onset_is_found_before_the_requested_end(self):
        out=calculate('brouillard',Tstar=320,latent_MJ=.58,B=1500,gamma=1.33,drop=15)
        onset=out['scene']['apparatus']['onset_K']
        self.assertIsNotNone(onset); self.assertGreater(onset,305); self.assertLess(onset,320)
        A=.58e6+1500*320
        self.assertAlmostEqual((onset/320)**(1.33/.33),math.exp(float(saturation_log_ratio(onset,320,A,1500))),places=11)
        self.assertAlmostEqual(float(out['charts'][0]['series'][1]['x'][0]),onset)


class Contracts(unittest.TestCase):
    def test_contents_and_all_default_presets_bounds_and_mixed_parameters(self):
        self.assertEqual((len(LABS),len(LESSONS),len(EXERCISES),len(GUIDES)),(6,12,18,6))
        rng=np.random.default_rng(42)
        for lab in LABS:
            base={c['key']:c['value'] for c in lab['controls']}
            self.assertGreaterEqual(len(lab['presets']),3)
            self.assertEqual(sum(item['lab']==lab['id'] for item in LESSONS),2)
            self.assertEqual(sum(item['lab']==lab['id'] for item in EXERCISES),3)
            self.assertEqual(len(GUIDES[lab['id']]['first_steps']),3)
            for c in lab['controls']:
                steps=(c['value']-c['min'])/c['step']
                self.assertAlmostEqual(steps,round(steps),delta=1e-7,msg=f"Pas incompatible : {lab['id']} {c['key']}")
            cases=[base]+[dict(base,**s['values']) for s in lab['presets']]
            for c in lab['controls']:
                cases += [dict(base,**{c['key']:v}) for v in [c['min'],c['max']]]
            cases += [{c['key']:float(rng.uniform(c['min'],c['max'])) for c in lab['controls']} for _ in range(20)]
            for params in cases:
                with self.subTest(lab=lab['id'],params=params):
                    out=COMPUTE[lab['id']](params); json.dumps(clean(out),allow_nan=False)
                    self.assertGreaterEqual(len(out['charts']),2)
                    self.assertTrue(out['scene']['title']); self.assertTrue(out['scene']['description'])
                    self.assertIn(out['scene']['apparatus']['type'],['radiation','electric','acoustic','piezo','fog'])
                    self.assertGreaterEqual(len(out['steps']),4)


if __name__=='__main__':
    unittest.main()
