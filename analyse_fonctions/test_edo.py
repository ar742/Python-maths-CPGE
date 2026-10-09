"""Références indépendantes, ordres, bilans et cas singuliers des dix labos EDO."""
import math
import unittest
import numpy as np
from catalogue_edo import LABS
from contenu_edo import LESSONS, EXERCISES, GUIDES
from modeles_edo import (COMPUTE,rk4,euler_solution,integrating_solution,
    homogeneous_oscillator,oscillator_exact,variation_solution,euler_particular,
    reservoir_matrix)
from commun import clean

def params(id_):
    return {c['key']:c['value'] for lab in LABS if lab['id']==id_ for c in lab['controls']}

def measured(id_,**values):
    p=params(id_); p.update(values); return COMPUTE[id_](p)

def metric_value(r,label):
    return next(m['value'] for m in r['metrics'] if m['label']==label)

class NumeriqueTests(unittest.TestCase):
    def test_euler_ordre_un(self):
        errors=[]
        for n in (80,160,320):
            t,y=euler_solution(0,4,n); exact=np.exp(np.sin(t))-1
            errors.append(np.max(abs(y-exact)))
        self.assertTrue(1.85<errors[-2]/errors[-1]<2.15)

    def test_rk4_ordre_quatre(self):
        errors=[]
        for n in (40,80,160):
            t,y=rk4(lambda x,z:math.cos(x)*(z+1),0,4,n)
            errors.append(np.max(abs(y-(np.exp(np.sin(t))-1))))
        self.assertTrue(14<errors[-2]/errors[-1]<18)

    def test_rk4_systeme_rotation(self):
        t,z=rk4(lambda t,z:np.array([-z[1],z[0]]),np.array([1.,0.]),2*math.pi,400)
        np.testing.assert_allclose(z[-1],[1,0],atol=4e-9)

    def test_equilibre_tp_conserve(self):
        t,y=rk4(lambda x,z:math.cos(x)*(z+1),-1,12,80)
        np.testing.assert_allclose(y,-1,atol=1e-14)

    def test_facteur_constant_reference(self):
        t=np.linspace(0,6,301); a=1.2; w=2; F=.8; y0=.7
        expected=y0*np.exp(-a*t)+F*(a*np.cos(w*t)+w*np.sin(w*t)-a*np.exp(-a*t))/(a*a+w*w)
        np.testing.assert_allclose(integrating_solution(t,a,0,F,w,y0),expected,atol=2e-13)

    def test_facteur_sans_coefficient(self):
        t=np.linspace(0,6,301)
        np.testing.assert_allclose(integrating_solution(t,0,0,2,1.3,.5),.5+2*np.sin(1.3*t)/1.3,atol=2e-13)

    def test_difference_de_solutions(self):
        t=np.linspace(0,6,301)
        one=integrating_solution(t,.8,.6,1.5,2,.2)
        two=integrating_solution(t,.8,.6,1.5,2,1.2)
        np.testing.assert_allclose(two-one,np.exp(-.8*t-.3*t*t),atol=2e-14)

class QualitatifTests(unittest.TestCase):
    def test_attente_vrai_raccordement(self):
        tau=1.3; t=np.array([tau-.1,tau,tau+.1])
        y=np.maximum(t-tau,0)**2
        derivative=2*np.maximum(t-tau,0)
        np.testing.assert_allclose(derivative,2*np.sqrt(y),atol=1e-14)
        self.assertEqual(y[1],0)

    def test_lipschitz_quotient_non_borne(self):
        self.assertGreater(2/math.sqrt(1e-8),100*(2/math.sqrt(1e-3)))

    def test_explosion_intervalle_et_valeur(self):
        r=measured('explosion_logistique',a=2,y0=.5,fraction=.8)
        self.assertAlmostEqual(metric_value(r,'Temps d’explosion t*'),1)
        self.assertAlmostEqual(metric_value(r,'Croissance quadratique y(T)'),2.5)
        self.assertLess(metric_value(r,'Erreur relative maximale RK4'),1e-8)

    def test_logistique_de_decroissance_au_dessus(self):
        r=measured('explosion_logistique',y0=2,K=.8)
        z=np.asarray(r['charts'][0]['series'][1]['y'])
        self.assertTrue(np.all(np.diff(z)<0)); self.assertTrue(np.all(z>.8))

    def test_homogene_et_raccordement_global(self):
        for c in (.1,.5,2):
            x=np.linspace(-4,4,401); y=c*x*x-1/(4*c)
            np.testing.assert_allclose(x*(2*c*x)-y,np.hypot(x,y),atol=2e-13)

    def test_riccati_explosion_horizon(self):
        r=measured('riccati',z0=1.5,T=4)
        pole=metric_value(r,'Explosion Riccati à droite')
        self.assertAlmostEqual(pole,math.atanh(2/3))
        self.assertLess(metric_value(r,'Durée effectivement calculée pour Riccati'),pole)

    def test_riccati_deux_equilibres(self):
        for z0 in (-1.,1.):
            r=measured('riccati',z0=z0)
            np.testing.assert_allclose(r['charts'][1]['series'][0]['y'],z0,atol=2e-13)

class OscillateurTests(unittest.TestCase):
    def test_donnees_initiales_tous_regimes(self):
        for zeta in (0,.1,1,1.5):
            y,v=oscillator_exact(np.array([0.]),1.2,zeta,1.2,1,.4,-.2)
            self.assertAlmostEqual(float(y[0]),.4,places=12)
            self.assertAlmostEqual(float(v[0]),-.2,places=12)

    def test_critique_reference(self):
        t=np.linspace(0,5,301); y,v=homogeneous_oscillator(t,1,1,1,0)
        np.testing.assert_allclose(y,(1+t)*np.exp(-t),atol=1e-14)
        np.testing.assert_allclose(v,-t*np.exp(-t),atol=1e-14)

    def test_resonance_exacte_non_amortie(self):
        t=np.linspace(0,12,301); y,v=oscillator_exact(t,2,0,2,3)
        np.testing.assert_allclose(y,.75*t*np.sin(2*t),atol=2e-14)
        np.testing.assert_allclose(v,.75*(np.sin(2*t)+2*t*np.cos(2*t)),atol=2e-14)

    def test_reference_rk4_independante(self):
        for zeta in (.1,1,1.4):
            t,z=rk4(lambda t,z:np.array([z[1],.8*math.cos(1.3*t)-2*zeta*z[1]-z[0]]),np.array([.3,-.2]),5,1600)
            y,v=oscillator_exact(t,1,zeta,1.3,.8,.3,-.2)
            np.testing.assert_allclose(z[:,0],y,atol=2e-9)
            np.testing.assert_allclose(z[:,1],v,atol=2e-9)

    def test_energie_libre_conservee(self):
        t=np.linspace(0,10,301); y,v=oscillator_exact(t,1.3,0,1.2,0,.3,-.2)
        energy=(v*v+1.3**2*y*y)/2
        np.testing.assert_allclose(energy,energy[0],atol=2e-14)

    def test_bilan_energetique_amorti_force(self):
        r=measured('oscillateur_resonance')
        self.assertLess(metric_value(r,'Résidu du bilan énergétique'),.002)

    def test_pas_de_fausse_amplitude_stationnaire(self):
        r=measured('oscillateur_resonance',zeta=0,ratio=1)
        self.assertEqual(metric_value(r,'Amplitude stationnaire'),'pas de valeur finie')

    def test_forcage_nul_meme_pulsation_sans_fausse_resonance(self):
        r=measured('oscillateur_resonance',zeta=0,ratio=1,F=0,y0=.7,v0=.2)
        self.assertEqual(metric_value(r,'Amplitude de la particulière forcée'),0)
        curve=r['charts'][0]['series'][0]; t=np.asarray(curve['x'])
        np.testing.assert_allclose(curve['y'],.7*np.cos(t)+.2*np.sin(t),atol=2e-14)

    def test_sans_amortissement_particuliere_ne_vaut_pas_regime_etabli(self):
        r=measured('oscillateur_resonance',zeta=0,ratio=1.5,F=1)
        self.assertAlmostEqual(metric_value(r,'Amplitude de la particulière harmonique'),.8)
        self.assertNotIn('Amplitude stationnaire',[m['label'] for m in r['metrics']])

class VariationEtSingularitesTests(unittest.TestCase):
    def test_variation_donnees_initiales(self):
        y,v,yp,yh=variation_solution(np.array([0.]),1,.4,-.2)
        self.assertAlmostEqual(float(y[0]),.4,places=13)
        self.assertAlmostEqual(float(v[0]),-.2,places=13)
        self.assertAlmostEqual(float(yp[0]),0,places=13)

    def test_variation_homogene_mode_exact(self):
        t=np.linspace(0,3,301); y,v,yp,yh=variation_solution(t,0,1,3)
        np.testing.assert_allclose(y,np.exp(3*t),rtol=1e-14)
        np.testing.assert_allclose(v,3*np.exp(3*t),rtol=1e-14)

    def test_variation_rk4_independant(self):
        t,z=rk4(lambda x,z:np.array([z[1],5*z[1]-6*z[0]+math.exp(x)/math.cosh(x)**2]),np.array([0.,0.]),2,1600)
        y,v,yp,yh=variation_solution(t,1,0,0)
        np.testing.assert_allclose(z[:,0],y,rtol=2e-9,atol=2e-9)
        np.testing.assert_allclose(z[:,1],v,rtol=2e-9,atol=2e-9)

    def test_euler_cauchy_residu_independant(self):
        x=np.concatenate((np.linspace(-3,-1.1,80),np.linspace(-.9,.9,101),np.linspace(1.1,3,80)))
        y,v,a=euler_particular(x)
        np.testing.assert_allclose(x*x*a+x*v-y,x*x/(1-x*x),atol=5e-12)

    def test_euler_cauchy_prolongement_analytique(self):
        y,v,a=euler_particular(np.array([0.,1e-7]))
        self.assertAlmostEqual(float(y[0]),0,places=14)
        self.assertAlmostEqual(float(v[0]),0,places=14)
        self.assertAlmostEqual(float(a[0]),2/3,places=14)
        self.assertAlmostEqual(float(y[1]/1e-14),1/3,places=12)

    def test_euler_cauchy_serie_reference(self):
        x=np.linspace(-.7,.7,301); expected=sum(x**(2*n)/(4*n*n-1) for n in range(1,80))
        np.testing.assert_allclose(euler_particular(x)[0],expected,atol=4e-14)

class SystemesEtBordsTests(unittest.TestCase):
    def test_matrice_echanges_conservative(self):
        A=reservoir_matrix(1,.3,2)
        np.testing.assert_allclose(A,A.T,atol=1e-14)
        np.testing.assert_allclose(A.sum(axis=0),0,atol=1e-14)
        self.assertLessEqual(float(np.linalg.eigvalsh(A)[-1]),1e-13)

    def test_reference_trois_echanges_identiques(self):
        r=measured('lineaire_systeme',k12=1,k23=1,k13=1,decay=0)
        t=np.asarray(r['charts'][0]['series'][0]['x']); Y1=r['charts'][0]['series'][0]['y']
        np.testing.assert_allclose(Y1,1/3+2*np.exp(-3*t)/3,atol=2e-14)

    def test_perte_uniforme_total_et_positivite(self):
        r=measured('lineaire_systeme',k12=.1,k23=2,k13=.1,decay=.5,T=10)
        self.assertLess(metric_value(r,'Résidu du bilan total'),5e-14)
        self.assertGreaterEqual(metric_value(r,'Plus petite quantité calculée'),-5e-14)

    def test_green_non_resonant_solution(self):
        r=measured('green_bords',lam=2,a=1,b=.5)
        y=r['charts'][0]['series'][0]['y']; x=np.asarray(r['charts'][0]['series'][0]['x'])
        np.testing.assert_allclose(y,np.sin(x)-.25*np.sin(2*x),atol=1e-14)
        self.assertEqual(metric_value(r,'Statut du problème aux deux bords'),'solution unique')

    def test_green_resonance_incompatible(self):
        r=measured('green_bords',lam=1,a=1,b=0)
        self.assertEqual(metric_value(r,'Statut du problème aux deux bords'),'aucune solution')
        self.assertAlmostEqual(metric_value(r,'Projection du second membre sur le mode résonant'),math.pi/2)
        self.assertAlmostEqual(metric_value(r,'Résidu maximal du tracé'),1)

    def test_green_resonance_compatible_libre(self):
        one=measured('green_bords',lam=1,a=0,b=1,free=.2)
        two=measured('green_bords',lam=1,a=0,b=1,free=.7)
        x=np.asarray(one['charts'][0]['series'][0]['x'])
        np.testing.assert_allclose(np.asarray(two['charts'][0]['series'][0]['y'])-one['charts'][0]['series'][0]['y'],.5*np.sin(x),atol=1e-14)
        self.assertEqual(metric_value(one,'Statut du problème aux deux bords'),'infinité de solutions')

class PedagogieEDOTests(unittest.TestCase):
    def test_couverture_et_guides(self):
        self.assertEqual(len(LABS),10); self.assertEqual(len(LESSONS),20); self.assertEqual(len(EXERCISES),30)
        for lab in LABS:
            id_=lab['id']; self.assertEqual(sum(l['lab']==id_ for l in LESSONS),2)
            self.assertEqual(sum(e['lab']==id_ for e in EXERCISES),3)
            self.assertEqual(len(GUIDES[id_]['first_steps']),3)
            self.assertEqual(set(GUIDES[id_]['levels']),{'sup','spe','beyond'})

    def test_resultats_par_defaut_finiment_exportables(self):
        for lab in LABS:
            r=clean(COMPUTE[lab['id']](params(lab['id'])))
            self.assertGreaterEqual(len(r['charts']),2); self.assertGreaterEqual(len(r['metrics']),4)
            self.assertTrue(r['scene']['description']); self.assertGreaterEqual(len(r['assumptions']),2)

if __name__=='__main__': unittest.main()
