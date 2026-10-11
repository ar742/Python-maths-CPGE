"""Vérifications physiques : signes, états, seuils et domaines des modèles."""
import math
import unittest
import numpy as np
from catalogue_analogique import LABS
from modeles_analogique import (COMPUTE,ali_response,cascade_transfer,derivative_transfer,
                               schmitt_states,astable_parameters,state_parameters,
                               state_transfer,transistor_dc)

DEFAULTS={lab['id']:{control['key']:control['value'] for control in lab['controls']} for lab in LABS}


def params(lab,**changes):
    return dict(DEFAULTS[lab],**changes)


def metric_value(result,label):
    return next(metric['value'] for metric in result['metrics'] if metric['label']==label)


class AnalogiquePhysicsTests(unittest.TestCase):
    def test_ali_product_gain_bandwidth_is_transition_frequency(self):
        for gain in (1,10,50):
            data=COMPUTE['ali_gain_bande'](params('ali_gain_bande',gain=gain,a0=1000,ft=750))
            product=metric_value(data,'Gain statique bouclé')*metric_value(data,'Bande à −3 dB')
            self.assertAlmostEqual(product,750000)

    def test_ali_linear_step_has_its_own_state_and_correct_time_constant(self):
        a0=1000; gain=10; ft=1000; dc=a0/(1+a0/gain)
        rate=2*np.pi*ft/a0*(1+a0/gain)
        times=np.linspace(0,5/rate,201)
        actual=ali_response(times,np.ones_like(times),gain,a0,ft,1e9,100)
        expected=dc*(1-np.exp(-rate*times))
        np.testing.assert_allclose(actual,expected,rtol=1e-12,atol=1e-12)
        self.assertEqual(actual[0],0)

    def test_ali_slew_and_resistive_current_limits_act_during_evolution(self):
        data=COMPUTE['ali_gain_bande'](params('ali_gain_bande',gain=50,e=5,f=50,sr=0.01,rl=100,imax=10))
        scene=data['scene']; t=np.array(scene['x'])*1e-3; y=np.array(scene['curves'][1]['y'])
        self.assertLessEqual(float(np.max(abs(y))),1.0)
        self.assertLessEqual(float(np.max(abs(np.diff(y)/np.diff(t)))),10000*(1+1e-12))
        self.assertTrue(np.any(abs(y)>0))

    def test_ali_offset_is_amplified_without_an_input(self):
        times=np.linspace(0,0.02,500); u=np.zeros_like(times)
        y=ali_response(times,u,10,1e5,1e6,1e6,12,offset=0.002)
        self.assertAlmostEqual(y[-1],0.002*1e5/(1+1e5/10),places=8)

    def test_cascade_transfer_matches_independent_nodal_solution(self):
        for frequency in (10,1000,100000):
            r1,r2,c1,c2=10000,4700,22e-9,47e-9; s=2j*np.pi*frequency
            matrix=np.array([[1/r1+1/r2+s*c1,-1/r2],[-1/r2,1/r2+s*c2]])
            independent=np.linalg.solve(matrix,np.array([1/r1,0]))[1]
            self.assertAlmostEqual(abs(independent-cascade_transfer(s,r1,r2,c1,c2)),0,places=12)

    def test_equal_rc_cells_reveal_loading_at_their_corner(self):
        s=1j/(10000*10e-9)
        direct=cascade_transfer(s,10000,10000,10e-9,10e-9)
        buffered=cascade_transfer(s,10000,10000,10e-9,10e-9,True)
        self.assertAlmostEqual(direct.real,0); self.assertAlmostEqual(direct.imag,-1/3)
        self.assertAlmostEqual(buffered.real,0); self.assertAlmostEqual(buffered.imag,-1/2)

    def test_sommateur_weights_are_resistance_ratios(self):
        data=COMPUTE['sommateur_inverseur'](params('sommateur_inverseur',r1=10,r2=20,rf=20,e1=1,e2=0))
        x=data['charts'][0]['series']; source=np.array(x[0]['y']); ideal=np.array(x[2]['y'])
        np.testing.assert_allclose(ideal,-2*source)

    def test_improved_derivative_has_inverse_sign_and_high_frequency_rolloff(self):
        r,c,rf,cf=1e4,1e-8,1e5,1e-9
        low=derivative_transfer(1j,r,c,rf,cf)
        self.assertLess(low.imag,0)
        self.assertAlmostEqual(low.imag/(-rf*c),1,places=6)
        high1=derivative_transfer(1j*1e8,r,c,rf,cf)
        high2=derivative_transfer(1j*1e9,r,c,rf,cf)
        self.assertAlmostEqual(abs(high1)/abs(high2),10,places=6)

    def test_integrator_initial_condition_is_preserved(self):
        data=COMPUTE['integrateur_derivateur'](params('integrateur_derivateur',mode='integrateur',e=1,f=1000,r=10,c=10))
        x=np.array(data['scene']['x'])*1e-3; y=np.array(data['scene']['curves'][1]['y'])
        self.assertEqual(y[0],0)
        target=(np.cos(2*np.pi*1000*x)-1)/(2*np.pi*1000*100e-6)
        np.testing.assert_allclose(y,target)
        self.assertLessEqual(float(np.max(y)),1e-12)

    def test_schmitt_switches_at_different_thresholds(self):
        u=np.array([-5,0,3,4,0,-3,-4,0],dtype=float)
        np.testing.assert_array_equal(schmitt_states(u,1/3,12),[12,12,12,-12,-12,-12,12,12])

    def test_schmitt_remembers_both_possible_states_between_thresholds(self):
        u=np.array([-1,0,1,0],dtype=float)
        np.testing.assert_array_equal(schmitt_states(u,1/3,12,1),np.full(4,12))
        np.testing.assert_array_equal(schmitt_states(u,1/3,12,-1),np.full(4,-12))

    def test_astable_symmetric_period_is_two_rc_log_two(self):
        tau,beta,low,high,plus,minus=astable_parameters(params('astable',ve=0))
        self.assertAlmostEqual(beta,1/3); self.assertAlmostEqual(low,-4); self.assertAlmostEqual(high,4)
        self.assertAlmostEqual(plus,minus)
        self.assertAlmostEqual(plus+minus,2*tau*math.log(2))

    def test_astable_offset_changes_duty_and_boundary_stops_it(self):
        tau,beta,low,high,plus,minus=astable_parameters(params('astable',ve=5))
        self.assertAlmostEqual(low,-2/3); self.assertAlmostEqual(high,22/3)
        self.assertAlmostEqual(plus/tau,math.log(19/7)); self.assertAlmostEqual(minus/tau,math.log(29/17))
        self.assertGreater(plus,minus)
        self.assertIsNone(astable_parameters(params('astable',ve=12))[-1])

    def test_wien_critical_gain_closes_a_real_unit_loop(self):
        p=params('wien',r1=20,r2=10,c1=10,c2=20,margin=1)
        data=COMPUTE['wien'](p); f0=metric_value(data,'Fréquence sélectionnée'); critical=metric_value(data,'Gain critique')
        r1,r2,c1,c2=20000,10000,10e-9,20e-9; s=2j*np.pi*f0
        zp=1/(1/r2+s*c2); zs=r1+1/(s*c1); feedback=zp/(zs+zp)
        self.assertAlmostEqual(critical,5)
        self.assertAlmostEqual((critical*feedback).real,1)
        self.assertAlmostEqual((critical*feedback).imag,0)

    def test_wien_envelope_distinguishes_decay_threshold_and_growth(self):
        seed=0.02
        for margin,relation in ((0.95,'less'),(1,'equal'),(1.02,'greater')):
            data=COMPUTE['wien'](params('wien',margin=margin,seed=seed))
            final=metric_value(data,'Amplitude finale du modèle')
            if relation=='less': self.assertLess(final,seed)
            elif relation=='equal': self.assertAlmostEqual(final,seed)
            else: self.assertGreater(final,seed); self.assertLessEqual(final,12)

    def test_precision_rectifier_outputs_a_difference_not_the_internal_ali(self):
        data=COMPUTE['redresseur_precision'](params('redresseur_precision',e=0.2,vd=0.6))
        first=data['charts'][0]['series']; intern=data['charts'][1]['series']
        ideal=np.array(first[1]['y']); bridge=np.array(first[2]['y']); precision=np.array(first[3]['y'])
        np.testing.assert_array_equal(bridge,np.zeros_like(bridge))
        np.testing.assert_allclose(precision,ideal)
        np.testing.assert_allclose(np.array(intern[1]['y'])-np.array(intern[0]['y']),ideal)
        self.assertGreater(np.max(abs(intern[2]['y'])),np.max(precision))

    def test_precision_rectifier_needs_voltage_headroom(self):
        data=COMPUTE['redresseur_precision'](params('redresseur_precision',e=5,vd=0.6,vsat=3))
        y=np.array(data['charts'][0]['series'][3]['y'])
        self.assertAlmostEqual(float(np.max(y)),2.4)

    def test_three_ali_transfer_satisfies_the_original_three_equations(self):
        p=params('filtre_etat',r1=7,r2=47,r3=22,r4=10,r5=33,r6=15,c=22)
        r,c,h0,w0,q,low,high=state_parameters(p); r1,r2,r3,r4,r5,r6=r
        for omega in (w0/10,w0,w0*10):
            # Inconnues : v_s1, v_s2, v_s ; entrée complexe unité.
            matrix=np.array([[r5/r4,0,1],[0,1j*omega*r6*c,1],[1+1j*omega*r2*c,r2/r3,0]])
            independent=np.linalg.solve(matrix,np.array([0,0,-r2/r1]))
            actual=state_transfer(omega,h0,w0,q)
            self.assertAlmostEqual(abs(actual-independent[2]),0,places=11)

    def test_three_ali_band_edges_are_half_power_and_have_exact_width(self):
        r,c,h0,w0,q,low,high=state_parameters(params('filtre_etat'))
        for edge in (low,high): self.assertAlmostEqual(abs(state_transfer(edge,h0,w0,q)),h0/math.sqrt(2))
        self.assertAlmostEqual(high-low,1/(r[1]*c))
        self.assertAlmostEqual(low*high,w0*w0)

    def test_square_input_uses_exact_odd_coefficients(self):
        data=COMPUTE['filtre_etat'](params('filtre_etat',signal='creneau',e=1,harmonics=5))
        spectrum=data['charts'][2]['series']; frequencies=np.array(spectrum[0]['x']); coeff=np.array(spectrum[0]['y'])
        ns=np.arange(1,10,2)
        np.testing.assert_array_equal(frequencies,DEFAULTS['filtre_etat']['f']*ns)
        np.testing.assert_allclose(coeff,4/(np.pi*ns))
        self.assertEqual(data['charts'][2]['style'],'bars')

    def test_transistor_active_bias_satisfies_kcl_and_emitter_relation(self):
        p=params('transistor_polarisation'); vth,rth,ib,ic,ve,vc,regime=transistor_dc(p)
        self.assertEqual(regime,'actif')
        self.assertAlmostEqual(ic,p['beta']*ib)
        self.assertAlmostEqual((vth-ve-0.7)/rth,ib)
        self.assertAlmostEqual(ve/(p['re']*1000),ic+ib)
        self.assertAlmostEqual((p['vcc']-vc)/(p['rc']*1000),ic)

    def test_transistor_saturated_bias_uses_fixed_junctions_and_not_beta(self):
        p=params('transistor_polarisation',rb1=47,rb2=10,re=0.1,rc=10)
        vth,rth,ib,ic,ve,vc,regime=transistor_dc(p)
        self.assertEqual(regime,'saturé')
        self.assertAlmostEqual(vc-ve,0.2)
        self.assertAlmostEqual(ve/(p['re']*1000),ic+ib)
        self.assertLess(ic,p['beta']*ib)
        data=COMPUTE['transistor_polarisation'](p)
        self.assertEqual(metric_value(data,'Gain petit signal à f'),0)

    def test_transistor_blocked_bias_has_no_collector_current(self):
        p=params('transistor_polarisation',vcc=5,rb1=5,rb2=100)
        vth,rth,ib,ic,ve,vc,regime=transistor_dc(p)
        self.assertEqual(regime,'bloqué'); self.assertEqual(ic,0); self.assertEqual(ib,0)
        self.assertEqual(vc,5)


if __name__=='__main__':
    unittest.main()
