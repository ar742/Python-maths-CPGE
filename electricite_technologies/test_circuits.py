"""Vérifications physiques des circuits et convertisseurs, sans accès réseau."""
import math
import unittest
import numpy as np
from catalogue_circuits import LABS
from contenu_circuits import GUIDES, LESSONS, EXERCISES
from modeles_circuits import (COMPUTE, bridge_values, line_values, rlc_step,
    impedance_values, doubler_states, diode_rc_states, inverter_data,
    chopper_states, puissance_values)
from commun import clean, integrate

def parameters(id_,**overrides):
    item=next(item for item in LABS if item['id']==id_)
    p={c['key']:c['value'] for c in item['controls']}; p.update(overrides)
    return p

def value(data,label):
    return next(m['value'] for m in data['metrics'] if m['label']==label)

class CircuitsPhysics(unittest.TestCase):
    def test_catalogue_and_contents(self):
        self.assertEqual(len(LABS),12)
        for item in LABS:
            id_=item['id']; self.assertIn(id_,COMPUTE); self.assertIn(id_,GUIDES)
            self.assertEqual(sum(l['lab']==id_ for l in LESSONS),2)
            self.assertEqual(sum(e['lab']==id_ for e in EXERCISES),3)
            self.assertEqual(len(GUIDES[id_]['first_steps']),3)
            self.assertEqual(set(GUIDES[id_]['levels']),{'sup','spe','beyond'})

    def test_presets_and_extreme_controls_remain_finite(self):
        for item in LABS:
            default=parameters(item['id'])
            cases=[default]+[dict(default,**preset['values']) for preset in item['presets']]
            for control in item['controls']:
                options=[control['min'],control['max']] if control['type']=='range' else [o['value'] for o in control['options']]
                cases.extend(dict(default,**{control['key']:option}) for option in options)
            for p in cases:
                with self.subTest(lab=item['id'],parameters=p): clean(COMPUTE[item['id']](p))

    def test_bridge_zero_uses_drawn_connections(self):
        *_,open_u,loaded_u,rth=bridge_values(5,2000,1000,6000,3000,9000)
        self.assertAlmostEqual(open_u,0); self.assertAlmostEqual(loaded_u,0)
        self.assertAlmostEqual(rth,2000/3+2000)
        _,_,uopen,u,_=bridge_values(5,1000,1000,1000,1100,1000)
        self.assertLess(u,0); self.assertLess(abs(u),abs(uopen))

    def test_line_energy_loss_matches_distributed_dissipation(self):
        p=parameters('ligne_transmission',load=200,R=100,G=5,length=40)
        x,v,i,power,_,_,_=line_values(p)
        loss_density=.5*(p['R']*.001*abs(i)**2+p['G']*1e-6*abs(v)**2)
        self.assertAlmostEqual(power[0]-power[-1],integrate(loss_density,x),delta=2e-6)
        self.assertTrue(np.all(np.diff(power)<=1e-12))

    def test_rlc_equation_initial_conditions_and_energy(self):
        E=5; L=.02; C=10e-6
        for R in (20,2*math.sqrt(L/C),300):
            t=np.linspace(0,.04,20001); u,i=rlc_step(E,R,L,C,t)
            self.assertAlmostEqual(u[0],0); self.assertAlmostEqual(i[0],0)
            energy=.5*C*u*u+.5*L*i*i; work=E*C*u
            heat=integrate(R*i*i,t)
            self.assertAlmostEqual(work[-1],energy[-1]+heat,delta=1e-9)
            self.assertTrue(np.all(np.diff(work-energy)>=-1e-10))

    def test_impedance_is_corrected_for_scope_loading(self):
        for kind in ('R','RL','RC','RLC'):
            p=parameters('mesure_impedance',kind=kind,R=10000,rin=10,cin=200,f=100000)
            true,parallel,_,_,_,_,estimate,corrected=impedance_values(p)
            self.assertLess(abs(estimate-parallel),1e-8)
            self.assertLess(abs(corrected-true),1e-6)
        p1=parameters('mesure_impedance',band=10); p2=dict(p1,band=1000)
        self.assertAlmostEqual(abs(impedance_values(p1)[6]-impedance_values(p2)[6]),0,places=8)

    def test_graetz_ideal_mean_rms_and_threshold(self):
        p=parameters('pont_graetz',peak=12,R=100,drop=0)
        data=COMPUTE['pont_graetz'](p)
        self.assertAlmostEqual(value(data,'Tension moyenne du pont'),24/math.pi,delta=5e-5)
        self.assertAlmostEqual(value(data,'Tension efficace du pont'),12/math.sqrt(2),places=10)
        self.assertAlmostEqual(value(data,'Puissance dans la charge'),.72,places=10)
        data=COMPUTE['pont_graetz'](dict(p,peak=1,drop=.7))
        self.assertEqual(value(data,'Tension efficace du pont'),0)

    def test_doubler_obeys_two_charge_balances(self):
        p=parameters('doubleur_tension',C1=50,C2=300,load=1000)
        t,v1,v2,i1,i2=doubler_states(p,points=1024,periods=6); dt=t[1]-t[0]
        load=(v1[1:]+v2[1:])/p['load']
        self.assertTrue(np.all(i1>=0)); self.assertTrue(np.all(i2>=0))
        self.assertLess(np.max(abs(p['C1']*1e-6*np.diff(v1)/dt-i1[1:]+load)),1e-9)
        self.assertLess(np.max(abs(p['C2']*1e-6*np.diff(v2)/dt-i2[1:]+load)),1e-9)
        self.assertTrue(np.all(v1+v2<=2*p['peak']+1e-8))

    def test_diode_rc_nonnegative_current_and_blocked_decay(self):
        p=parameters('diode_rc',R=1000,C=100)
        t,u,v,i=diode_rc_states(p,points=2048,periods=4); dt=t[1]-t[0]
        self.assertTrue(np.all(v>=0)); self.assertTrue(np.all(i>=0)); self.assertLessEqual(np.max(v),p['peak'])
        selected=(u[1:]<0)&(u[:-1]<0)
        expected=v[:-1]*math.exp(-dt/(p['R']*p['C']*1e-6))
        self.assertLess(np.max(abs(v[1:][selected]-expected[selected])),1e-9)

    def test_transformer_ratio_and_resistive_power_balance(self):
        p=parameters('triphase_transformateur',Rseq=.001,P0=0,primary='D',secondary='Y',turns=.5)
        data=COMPUTE['triphase_transformateur'](p)
        self.assertAlmostEqual(value(data,'Tension secondaire composée à vide'),400*.5*math.sqrt(3),places=9)
        # À charge extrême, un modèle résistif donne une chute finie sans écrêtage.
        extreme=dict(p,U1=100,turns=.01,S=100,fraction=1.2,Rseq=.2,pf=1)
        data=COMPUTE['triphase_transformateur'](extreme)
        I=value(data,'Courant de ligne secondaire'); U=value(data,'Tension composée sous charge')
        self.assertAlmostEqual(3*extreme['Rseq']*I*I,value(data,'Pertes cuivre'),places=9)
        self.assertAlmostEqual(math.sqrt(3)*U*I,value(data,'Puissance utile')*1000,places=9)
        self.assertLess(U,value(data,'Tension secondaire composée à vide'))

    def test_inverter_parseval_and_truncated_thd(self):
        expected=math.sqrt(math.pi**2/8-1)
        for shift in (0,.25):
            _,_,amp,rms,fund,total,partial=inverter_data(175,shift,51)
            self.assertAlmostEqual(total,expected,places=10)
            self.assertLess(partial,total)
            self.assertTrue(np.all(amp[1::2]==0))
            self.assertAlmostEqual(rms*rms,fund*fund*(1+total*total),places=9)
        _,_,_,rms,_,_,_=inverter_data(175,.25,21)
        self.assertAlmostEqual(rms,175/math.sqrt(2),places=10)

    def test_chopper_ccm_mean_and_power(self):
        p=parameters('hacheur_mcc'); t,i,u,src,diode,imin,imax,regime=chopper_states(p,points=12000)
        self.assertEqual(regime,'conduction continue'); self.assertGreater(imin,0)
        T=1/(p['f']*1000); selected=t>=2*T; x=t[selected]; y=i[selected]
        mean=integrate(y,x)/T
        self.assertAlmostEqual(mean,(p['duty']*p['E']-p['emf'])/p['R'],delta=.001)
        received=integrate(p['E']*src[selected],x)/T
        consumed=integrate(p['R']*y*y+p['emf']*y,x)/T
        self.assertAlmostEqual(received,consumed,delta=.03)
        self.assertTrue(np.allclose(src+diode,i))

    def test_chopper_dcm_and_no_reverse_current(self):
        p=parameters('hacheur_mcc',L=.1,f=.5,duty=.5)
        t,i,u,src,diode,imin,imax,regime=chopper_states(p)
        self.assertEqual(regime,'conduction discontinue'); self.assertEqual(imin,0)
        self.assertTrue(np.all(i>=0)); self.assertTrue(np.any(i==0)); self.assertGreater(imax,0)
        self.assertTrue(np.allclose(src+diode,i))
        t,i,*_=chopper_states(dict(p,emf=60)); self.assertTrue(np.all(i==0))

    def test_compensation_preserves_active_power_and_minimizes_current(self):
        p=parameters('puissances_compensation',C=0); _,_,before,S,Copt=puissance_values(p)
        _,_,best,compensated,_=puissance_values(dict(p,C=Copt))
        _,_,over,overpower,_=puissance_values(dict(p,C=2*Copt))
        self.assertAlmostEqual(S.real,compensated.real,places=10)
        self.assertAlmostEqual(compensated.imag,0,places=10)
        self.assertLess(abs(best),abs(before)); self.assertGreater(abs(over),abs(best))
        self.assertAlmostEqual(overpower.real,S.real,places=10)

if __name__=='__main__': unittest.main()
