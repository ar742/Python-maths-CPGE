"""Vérifications physiques et mathématiques des quatorze expériences."""
import math
import unittest
import numpy as np
from catalogue_commande import LABS
from contenu_commande import LESSONS, EXERCISES, GUIDES
from modeles_commande import COMPUTE, homogeneous, adc_codes, discrete_responses, rk4, matrix_exponential
from commun import clean


DEFAULTS={lab['id']:{c['key']:c['value'] for c in lab['controls']} for lab in LABS}


def run(name,**changes):
    return COMPUTE[name](dict(DEFAULTS[name],**changes))


def values(out,graph=0,curve=0):
    return np.asarray(out['charts'][graph]['series'][curve]['y'])


def metrics(out):
    return {m['label']:m['value'] for m in out['metrics']}


class TestCommande(unittest.TestCase):
    def test_catalogue_and_pedagogical_coverage(self):
        self.assertEqual(len(LABS),14)
        self.assertEqual(set(DEFAULTS),set(COMPUTE))
        self.assertEqual(set(DEFAULTS),set(GUIDES))
        for lab in LABS:
            ident=lab['id']
            self.assertEqual(sum(x['lab']==ident for x in LESSONS),2)
            self.assertEqual(sum(x['lab']==ident for x in EXERCISES),3)
            self.assertTrue(all(isinstance(GUIDES[ident][key],list) and GUIDES[ident][key] for key in ('objects','hypotheses','techniques','first_steps')))
            for pre in lab['presets']:
                self.assertLessEqual(set(pre['values']),set(DEFAULTS[ident]))
                for c in lab['controls']:
                    v=pre['values'].get(c['key'],c['value'])
                    if c['type']=='select': self.assertIn(v,[o['value'] for o in c['options']])
                    else:
                        self.assertGreaterEqual(v,c['min']); self.assertLessEqual(v,c['max'])
        self.assertEqual(len(LESSONS),28); self.assertEqual(len(EXERCISES),42)

    def test_export_for_presets_and_control_boundaries(self):
        for lab in LABS:
            ident=lab['id']; base=DEFAULTS[ident]
            cases=[base]+[dict(base,**pr['values']) for pr in lab['presets']]
            for control in lab['controls']:
                extremes=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                cases += [dict(base,**{control['key']:v}) for v in extremes]
            for end in ('min','max'):
                cases.append({c['key']:(c[end] if c['type']=='range' else c['value']) for c in lab['controls']})
            for p in cases:
                with self.subTest(lab=ident,p=p):
                    out=clean(COMPUTE[ident](p))
                    self.assertTrue(out['scene']['description'])
                    for graph in out['charts']:
                        for curve in graph['series']:
                            self.assertEqual(len(curve['x']),len(curve['y']))

    def test_initial_state_superposition_and_equilibrium(self):
        out=run('laplace_initiales',initial=3,gain=2,input=1)
        total,forced,free=(values(out,0,k) for k in range(3))
        np.testing.assert_allclose(total,forced+free,rtol=1e-14)
        self.assertEqual(total[0],3)
        self.assertAlmostEqual(total[-1],2+math.exp(-6),places=12)
        zero=run('laplace_initiales',initial=2,gain=2,input=1)
        np.testing.assert_allclose(values(zero),2,atol=1e-12)

    def test_second_order_critical_limit_and_overshoot(self):
        t=np.linspace(0,3,100)
        exact=np.exp(-2*t)*(1+2*t)
        np.testing.assert_allclose(homogeneous(t,1,0,2,1),exact,atol=1e-14)
        for z in (1-1e-6,1+1e-6):
            np.testing.assert_allclose(homogeneous(t,1,0,2,z),exact,atol=2e-6)
        out=run('bode_second_ordre',zeta=0.5)
        self.assertAlmostEqual(metrics(out)['Dépassement théorique'],100*math.exp(-math.pi/math.sqrt(3)),places=12)
        self.assertAlmostEqual(values(out,2)[0],0,places=12)
        critical=run('bode_second_ordre',zeta=1)
        self.assertTrue(np.all(np.diff(values(critical,2))>=-1e-12))

    def test_feedback_without_sensor_is_identity(self):
        out=run('retroaction_sensibilite',beta=0,variation=0.2)
        self.assertEqual(metrics(out)['Sensibilité relative'],1)
        self.assertAlmostEqual(metrics(out)['Variation relative réelle de G'],20,places=12)
        closed=run('retroaction_sensibilite',mu=20,beta=0.1,variation=0.2)
        self.assertAlmostEqual(metrics(closed)['Variation relative réelle de G'],100/17,places=12)

    def test_motor_x_exact_tp_and_zero_feedback(self):
        out=run('moteur_x')
        m=metrics(out)
        self.assertEqual(m['Vitesse finale en boucle ouverte'],20)
        self.assertAlmostEqual(m['Vitesse finale en boucle fermée'],20/3,places=12)
        self.assertAlmostEqual(m['Constante de temps fermée τ′'],1/3,places=12)
        plain=run('moteur_x',beta=0)
        np.testing.assert_allclose(values(plain,0,0),values(plain,0,1),atol=1e-13)
        self.assertAlmostEqual(values(out,0,0)[0],0,places=12)
        self.assertAlmostEqual(values(out,0,1)[0],0,places=12)

    def test_mcc_permanent_energy_balance(self):
        out=run('moteur_mcc',load=0.03)
        m=metrics(out); w=m['Vitesse permanente']; i=m['Courant permanent']
        self.assertAlmostEqual(w,38,places=12); self.assertAlmostEqual(i,4.1,places=12)
        # Puissance électrique = pertes Joule + frottement + puissance de charge.
        self.assertAlmostEqual(12*i,2*i*i+0.01*w*w+0.03*w,places=12)
        wvalues=values(out,0); ivalues=values(out,1)
        self.assertAlmostEqual(wvalues[0],0,places=10); self.assertAlmostEqual(ivalues[0],0,places=10)
        self.assertLess(abs(wvalues[-1]-w),0.15)

    def test_mcc_fast_current_is_resolved_when_rotor_is_slow(self):
        out=run('moteur_mcc',R=8,L=5,J=30,friction=1,k=0.02,load=0)
        curve=out['charts'][4]['series'][0]
        times=np.asarray(curve['x'])*1e-3; current=np.asarray(curve['y'])
        electrical_time=0.005/8
        self.assertLessEqual(times[1]-times[0],electrical_time/50+1e-15)
        self.assertGreaterEqual(times[-1],8*electrical_time-1e-15)
        index=int(np.argmin(abs(times-electrical_time)))
        # Le rotor massif reste presque immobile pendant ce transitoire RL.
        expected=12/8*(1-math.exp(-1))
        self.assertAlmostEqual(current[index],expected,delta=2e-6)
        self.assertAlmostEqual(current[0],0,places=12)
        self.assertLess(current[1],0.05)

    def test_pi_accessible_and_saturated_integral(self):
        out=run('correcteur_pi',target=1,limit=5,tau=0.5,Ti=0.5)
        self.assertLess(abs(metrics(out)['Erreur à la fin']),0.015)
        ordinary=run('correcteur_pi',target=3,limit=0.5,aw='off')
        corrected=run('correcteur_pi',target=3,limit=0.5,aw='on')
        self.assertEqual(metrics(ordinary)['Première consigne accessible'],'non')
        self.assertLess(metrics(corrected)['Action intégrale à la fin'],metrics(ordinary)['Action intégrale à la fin'])
        self.assertLessEqual(np.max(abs(values(ordinary,1,0))),0.5+1e-12)
        off=run('correcteur_pi',kp=0)
        np.testing.assert_allclose(values(off,0,1),0,atol=1e-12)

    def test_rk4_resolves_electrical_scale(self):
        t=np.linspace(0,1,51)
        state=rk4(lambda tm,s:np.array([-50*s[0]+50]),t,[0],0.002)
        np.testing.assert_allclose(state[:,0],1-np.exp(-50*t),atol=4e-7)

    def test_margins_equal_time_constants_critical_gain_eight(self):
        for gain,stable in ((4,'oui'),(12,'non')):
            out=run('stabilite_marges',K=gain,tau1=0.2,tau2=0.2,tau3=0.2)
            m=metrics(out)
            self.assertEqual(m['Boucle fermée stable'],stable)
            self.assertAlmostEqual(m['Marge de gain'],20*math.log10(8/gain),places=9)
        limit=run('stabilite_marges',K=8,tau1=0.2,tau2=0.2,tau3=0.2)
        self.assertAlmostEqual(metrics(limit)['Marge de phase'],0,places=8)
        self.assertAlmostEqual(metrics(limit)['Marge de gain'],0,places=8)
        low=run('stabilite_marges',K=0.5)
        self.assertIsInstance(metrics(low)['Marge de phase'],str)

    def test_closed_loop_double_pole_retains_initial_state_and_jordan_term(self):
        gain=1.5019344587351198
        out=run('stabilite_marges',K=gain,tau1=1,tau2=0.1,tau3=0.05)
        y=values(out,2); t=np.asarray(out['charts'][2]['series'][0]['x'])
        self.assertEqual(y[0],0)
        # D(p)=p³+31p²+230p+200(1+K)=(p−r)²(p−s).
        # La décomposition analytique possède un terme t exp(rt), absent d'une
        # simple somme de résidus calculés comme si les pôles étaient distincts.
        r=(-62+math.sqrt(1084))/6; s=-31-2*r; numerator=200*gain
        constant=gain/(1+gain)
        double=numerator/(r*(r-s))
        single=-numerator*(2*r-s)/(r*r*(r-s)**2)
        other=numerator/(s*(s-r)**2)
        expected=constant+(single+double*t)*np.exp(r*t)+other*np.exp(s*t)
        np.testing.assert_allclose(y,expected,atol=3e-13,rtol=2e-12)
        for nearby in (gain-1e-8,gain+1e-8):
            np.testing.assert_allclose(values(run('stabilite_marges',K=nearby,tau1=1,tau2=0.1,tau3=0.05),2),y,atol=3e-9)
        jordan=np.array([[-2,1],[0,-2]],float)
        np.testing.assert_allclose(matrix_exponential(jordan),math.exp(-2)*np.array([[1,1],[0,1]]),atol=2e-15)

    def test_seismic_diagram_force_is_derivative_of_relative_motion(self):
        out=run('isolation_sismique',omega_r=8,alpha=0.01,eta=25)
        self.assertAlmostEqual(metrics(out)['Amortissement ajouté ζ'],1,places=12)
        graph=out['charts'][1]; w=np.asarray(graph['series'][1]['x']); gain=values(out,1,1)
        # Le schéma impose x=I[x₀−αηp(x−x₀)] ; vérifier son module sans utiliser son polynôme réduit.
        s=1j*w; I=64/(s*s+64)
        expected=I*(1+0.25*s)/(1+0.25*s*I)
        np.testing.assert_allclose(gain,20*np.log10(abs(expected)),atol=1e-11)
        self.assertAlmostEqual(values(out,0,2)[0],0,places=10)
        self.assertGreater(gain[-1],values(out,1,0)[-1])

    def test_adc_codes_bounds_error_and_saturation(self):
        samples=np.linspace(-1.8,1.8,5001)
        code,value,q=adc_codes(samples,8,2)
        self.assertTrue(np.all((code>=0)&(code<256)))
        self.assertLessEqual(float(np.max(abs(value-samples))),q/2+1e-12)
        code,value,_=adc_codes([-10,10],8,2)
        np.testing.assert_array_equal(code,[0,255])
        self.assertGreater(value[0],-2); self.assertLess(value[1],2)
        out=run('echantillonnage_adc',frequency=800,sample_rate=1000)
        self.assertEqual(metrics(out)['Fréquence repliée'],200)
        exact=np.asarray(out['scene']['curves'][0]['y']); ts=np.asarray(out['scene']['x'])
        folded=1.5*np.sin(-2*np.pi*200*ts+math.pi/6)
        np.testing.assert_allclose(exact,folded,atol=2e-12)

    def test_fir_annuls_expected_noise_and_memory_is_finite(self):
        out=run('filtre_rif',N=10,noise=0.3)
        h=values(out,1)
        self.assertEqual(np.count_nonzero(h),10)
        self.assertAlmostEqual(float(np.sum(h)),1,places=12)
        self.assertLess(metrics(out)['Gain sur le bruit'],1e-12)
        self.assertAlmostEqual(metrics(out)['Retard de groupe'],0.0045,places=12)

    def test_iir_impulse_step_and_negative_pole(self):
        out=run('filtre_rii_z',a=0.8,N=200)
        h,step=values(out,0,0),values(out,0,1)
        np.testing.assert_allclose(np.cumsum(h),step,atol=2e-15)
        self.assertAlmostEqual(float(np.sum(h)),1,places=12)
        neg=run('filtre_rii_z',a=-0.8)
        self.assertGreater(values(neg)[0],0); self.assertLess(values(neg)[1],0)
        self.assertAlmostEqual(metrics(neg)['Somme de |hₖ|, sur tout k'],9,places=12)
        zero=run('filtre_rii_z',a=0)
        self.assertEqual(zero['scene']['apparatus']['poles'],[])

    def test_discrete_tp_distinguishes_initial_state_from_impulse(self):
        _,source,_,_=discrete_responses(0.001,50e-6,'source',5)
        _,impulse,bilinear,zoh=discrete_responses(0.001,50e-6,'impulse',5)
        self.assertEqual(source[0],1); self.assertAlmostEqual(source[1],1,places=14)
        self.assertAlmostEqual(source[2],20/21,places=14)
        self.assertEqual(impulse[0],0); self.assertAlmostEqual(impulse[1],1/21,places=14)
        self.assertAlmostEqual(bilinear[1],1/41,places=14)
        self.assertAlmostEqual(zoh[1],1-math.exp(-0.05),places=14)
        # Pour une impulsion à état nul, la somme des réponses vaut le gain continu unité.
        _,impulse,bilinear,zoh=discrete_responses(0.001,50e-6,'impulse',1000)
        for y in (impulse,bilinear,zoh): self.assertAlmostEqual(float(np.sum(y)),1,places=10)
        _,step,_,exact=discrete_responses(0.001,50e-6,'step',50)
        np.testing.assert_allclose(exact,1-np.exp(-np.arange(51)*0.05),atol=1e-14)

    def test_pole_radius_and_conjugacy(self):
        out=run('polezero_z',radius=0.5,angle=60,zero_angle=36,N=200)
        app=out['scene']['apparatus']; poles=app['poles']; zeros=app['zeros']
        for z in poles: self.assertAlmostEqual(math.hypot(z['re'],z['im']),0.5,places=12)
        for z in zeros: self.assertAlmostEqual(math.hypot(z['re'],z['im']),1,places=12)
        self.assertAlmostEqual(poles[0]['im'],-poles[1]['im'],places=12)
        self.assertLess(abs(values(out)[-1]),1e-45)
        self.assertAlmostEqual(metrics(out)['Fréquence relative des pôles'],1/6,places=12)

    def test_am_spectral_power_and_overmodulation(self):
        out=run('modulation_am',U=2,m=0.6,message=100,ratio=20)
        np.testing.assert_allclose(out['charts'][1]['series'][0]['x'],[1900,2000,2100])
        np.testing.assert_allclose(values(out,1),[0.6,2,0.6])
        power=sum(v*v/2 for v in values(out,1))
        self.assertAlmostEqual(power,metrics(out)['Puissance moyenne pour R=1 Ω'],places=12)
        # L'intervalle couvre un nombre entier de périodes de toutes les raies.
        am=values(out,0); self.assertAlmostEqual(float(np.mean(am[:-1]**2)),power,places=10)
        over=run('modulation_am',m=1.3)
        self.assertLess(float(np.min(values(over,0,1))),0)
        self.assertGreaterEqual(float(np.min(values(over,0,2))),0)
        tm=np.asarray(over['charts'][2]['series'][1]['x'])*1e-3
        np.testing.assert_allclose(values(over,2,1),2*1.3*np.cos(2*np.pi*100*tm),atol=3e-14)


if __name__=='__main__': unittest.main()
