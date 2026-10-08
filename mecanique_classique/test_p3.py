"""Vérifications physiques P3 : limites, contacts et invariants indépendants."""
import math
import unittest
import numpy as np
from commun import clean
from catalogue_p3 import LABS
from modeles_p3 import COMPUTE, inertia, coulomb_motion, G
from contenu_p3 import LESSONS, EXERCISES, GUIDES

def parameters(name, **values):
    p={c['key']:c['value'] for lab in LABS if lab['id']==name for c in lab['controls']}; p.update(values); return p

def measures(name, **values):
    result=COMPUTE[name](parameters(name,**values)); return {m['label']:m['value'] for m in result['metrics']},result

class TestContratP3(unittest.TestCase):
    def test_huit_experiences_deux_cours_trois_problemes(self):
        self.assertEqual(len(LABS),8)
        for lab in LABS:
            key=lab['id']; self.assertIn(key,COMPUTE); self.assertIn(key,GUIDES)
            self.assertEqual(sum(x['lab']==key for x in LESSONS),2)
            self.assertEqual(sum(x['lab']==key for x in EXERCISES),3)
            self.assertGreaterEqual(len(lab['presets']),3)
            self.assertEqual(len(GUIDES[key]['first_steps']),3)

    def test_tous_les_prereglages_sont_exportables(self):
        for lab in LABS:
            for preset in [dict(label='Défaut',values={})]+lab['presets']:
                with self.subTest(lab=lab['id'],preset=preset['label']):
                    r=clean(COMPUTE[lab['id']](parameters(lab['id'],**preset['values'])))
                    self.assertTrue(r['charts']); self.assertTrue(r['steps']); self.assertTrue(r['assumptions']); self.assertIn('kind',r['scene'])

class TestInertieKonig(unittest.TestCase):
    def test_masses_sur_un_cercle(self):
        a=2.; m=3.; points=np.array([[a,0,0],[-a,0,0],[0,a,0],[0,-a,0]])
        np.testing.assert_allclose(inertia(points,np.full(4,m)),np.diag([2*m*a*a,2*m*a*a,4*m*a*a]))

    def test_translation_parallele_axe_ne_change_pas_inertie(self):
        a,_=measures('inertie_huygens',dx=.8,dy=0,theta=90,phi=0)
        self.assertAlmostEqual(a['Inertie de l’axe passant par O'],a['Inertie de l’axe passant par G'],places=12)

    def test_huygens_ne_diminue_jamais_inertie(self):
        a,_=measures('inertie_huygens',dx=.8,dy=-.4,theta=60,phi=130)
        self.assertGreaterEqual(a['Inertie de l’axe passant par O'],a['Inertie de l’axe passant par G'])
        self.assertLess(a['Écart entre calcul direct et Huygens'],1e-12)

    def test_konig_translation_seule(self):
        a,_=measures('konig',omega=0,mass=4,vx=3,vy=4)
        self.assertAlmostEqual(a['Énergie calculée par les six vitesses'],50.)
        self.assertAlmostEqual(a['Énergie de rotation'],0.)

    def test_konig_mouvement_mixte(self):
        a,_=measures('konig',omega=-5,mass=4,vx=-2,vy=3,gx=1,gy=-2)
        self.assertLess(a['Écart du premier théorème de König'],1e-12)
        self.assertLess(a['Écart du second théorème de König'],1e-12)

class TestBarres(unittest.TestCase):
    def test_vitesse_horizontale_et_scaling(self):
        a,_=measures('barre_bascule',L=.8,theta2=90)
        self.assertAlmostEqual(a['Vitesse angulaire finale']**2,3*G/(2*.8),places=11)
        b,_=measures('barre_bascule',L=1.6,theta2=90)
        self.assertAlmostEqual(b['Durée entre les deux angles']/a['Durée entre les deux angles'],math.sqrt(2),places=12)

    def test_duree_par_quadrature_independante(self):
        a,_=measures('barre_bascule',theta1=10,theta2=130)
        angle=np.linspace(np.radians(10),np.radians(130),100001)
        integrate=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
        quadrature=integrate(1/np.sqrt(3*G/(2*.8)*(1-np.cos(angle))),angle)
        self.assertAlmostEqual(a['Durée entre les deux angles'],quadrature,places=8)

    def test_energie_barre_pivot(self):
        a,_=measures('barre_bascule',theta1=.2,theta2=170)
        self.assertLess(a['Variation numérique de E_c+E_p'],1e-11)

    def test_barre_plan_reste_dans_plan(self):
        a,r=measures('barre_rotule',phi_dot=0,theta_dot=.5)
        self.assertLess(np.max(np.abs(r['scene']['axis'][:,1])),1e-14)
        self.assertLess(a['Écart maximal de l’énergie'],2e-7)
        self.assertLess(a['Écart maximal de cette composante'],1e-12)

    def test_rotation_conique_exacte(self):
        L=.7; theta=120; rate=math.sqrt(-3*G/(4*L*math.cos(math.radians(theta))))
        a,r=measures('barre_rotule',L=L,theta=theta,theta_dot=0,phi_dot=rate)
        self.assertLess(np.ptp(r['scene']['axis'][:,2]),1e-8)
        self.assertLess(a['Écart maximal de l’énergie'],1e-7)
        self.assertLess(a['Écart maximal de cette composante'],1e-7)

class TestContacts(unittest.TestCase):
    def test_cylindre_seuil_contact_adherent(self):
        for fs in [.01,.2,1.,3.]:
            a,r=measures('cylindre_bord',fs=fs)
            self.assertLess(a['Premier angle de glissement'],a['Angle N=0 si l’adhérence était maintenue'])
            self.assertGreater(a['Réaction normale au seuil'],0)
            self.assertAlmostEqual(a['Réaction tangentielle au seuil'],fs*a['Réaction normale au seuil'],places=10)
            self.assertAlmostEqual(np.degrees(r['scene']['theta'][-1]),a['Premier angle de glissement'])
            self.assertAlmostEqual(r['charts'][0]['xMarker'],a['Premier angle de glissement'])
            self.assertEqual(r['charts'][0]['xMarkerLabel'],'Premier glissement')

    def test_cylindre_frottement_nul(self):
        a,r=measures('cylindre_bord',fs=0)
        self.assertEqual(a['Premier angle de glissement'],0)
        self.assertEqual(float(r['scene']['theta'][-1]),0)

    def test_statique_non_sature(self):
        a,_=measures('coulomb_horizontal',force=8,mass=4,fs=.4)
        self.assertEqual(a['Régime'],'Adhérence'); self.assertAlmostEqual(a['Frottement à t=0⁺'],-8)
        self.assertEqual(a['Accélération à t=0⁺'],0); self.assertEqual(a['Chaleur dissipée à la fin'],0)

    def test_dynamique_force_negative(self):
        a,r=measures('coulomb_horizontal',force=-60)
        self.assertLess(a['Accélération à t=0⁺'],0); self.assertGreater(a['Frottement à t=0⁺'],0); self.assertGreater(a['Chaleur dissipée à la fin'],0)
        curves=r['charts'][-1]['series']; np.testing.assert_allclose(curves[0]['y'],curves[1]['y']+curves[2]['y'],atol=1e-10)

    def test_freinage_puis_adherence(self):
        a,r=measures('coulomb_horizontal',initial='moving',v0=3,mass=2,fs=.5,ratio=.6,force=-8,duration=2)
        stop=2*3/(8+.3*2*G); position=3*stop/2
        self.assertEqual(a['Régime'],'Glissement puis adhérence')
        self.assertAlmostEqual(a['Temps d’arrêt'],stop,places=12)
        self.assertAlmostEqual(float(r['scene']['x'][-1]),position,places=12)
        self.assertEqual(float(r['scene']['v'][-1]),0)
        self.assertAlmostEqual(float(r['scene']['friction'][-1]),8.)
        self.assertLess(a['Écart du bilan W_F=ΔE_c+Q'],1e-11)

    def test_inversion_continuite_position_et_vitesse(self):
        motion=coulomb_motion(2,.5,.3,-12,3,2)
        stop=6/(12+.3*2*G); position=3*stop/2
        index=int(np.argmin(np.abs(motion['time']-stop)))
        self.assertAlmostEqual(motion['time'][index],stop,places=14)
        self.assertAlmostEqual(motion['x'][index],position,places=12)
        self.assertEqual(motion['v'][index],0)
        self.assertGreater(motion['v'][index-1],0)
        self.assertLess(motion['v'][index+1],0)
        self.assertAlmostEqual(motion['friction'][0],-.3*2*G)
        self.assertAlmostEqual(motion['friction'][-1],.3*2*G)

    def test_distance_parcourue_differe_du_deplacement_apres_inversion(self):
        a,r=measures('coulomb_horizontal',initial='moving',v0=3,mass=2,fs=.5,ratio=.6,force=-12,duration=2)
        stop=6/(12+.3*2*G); position=3*stop/2; x_final=float(r['scene']['x'][-1])
        self.assertLess(x_final,0)
        expected_heat=.3*2*G*(position+abs(x_final-position))
        self.assertAlmostEqual(a['Chaleur dissipée à la fin'],expected_heat,places=10)
        self.assertGreater(a['Chaleur dissipée à la fin'],.3*2*G*abs(x_final))
        self.assertLess(a['Écart du bilan W_F=ΔE_c+Q'],1e-10)

    def test_caisse_lancee_frotte_meme_sous_force_inferieure_seuil(self):
        motion=coulomb_motion(2,.5,.3,2,3,3)
        self.assertLess(motion['friction'][0],0)
        self.assertEqual(motion['regime'],'Glissement puis adhérence')
        self.assertEqual(motion['friction'][-1],-2.)
        self.assertEqual(motion['v'][-1],0.)

    def test_arret_exactement_au_seuil_statique(self):
        a,r=measures('coulomb_horizontal',initial='moving',v0=1,mass=2,fs=.5,ratio=.6,force=-.5*2*G,duration=2)
        self.assertEqual(a['Régime'],'Glissement puis adhérence')
        self.assertEqual(float(r['scene']['v'][-1]),0.)

    def test_sans_frottement_dynamique_bilan_apres_arret(self):
        a,r=measures('coulomb_horizontal',initial='moving',v0=3,mass=2,fs=.5,ratio=0,force=-8,duration=2)
        self.assertEqual(a['Régime'],'Glissement puis adhérence')
        self.assertEqual(a['Chaleur dissipée à la fin'],0.)
        self.assertLess(a['Écart du bilan W_F=ΔE_c+Q'],1e-12)

    def test_roulement_ideal_et_energie(self):
        for body,k in [('cylinder',.5),('sphere',.4),('ring',1)]:
            a,_=measures('plan_incline',body=body,alpha=20,fs=1)
            self.assertEqual(a['Régime'],'Roulement sans glissement')
            self.assertAlmostEqual(a['Accélération du centre de masse'],G*math.sin(math.radians(20))/(1+k))
            self.assertLess(abs(a['Vitesse de glissement finale']),1e-12)
            self.assertEqual(a['Énergie dissipée'],0)
            self.assertLess(a['Écart du bilan énergétique'],1e-11)

    def test_glissement_solide_et_dissipation(self):
        a,_=measures('plan_incline',body='ring',alpha=50,fs=.12,ratio=.7)
        self.assertEqual(a['Régime'],'Roulement avec glissement'); self.assertGreater(a['Vitesse de glissement finale'],0)
        self.assertGreater(a['Énergie dissipée'],0); self.assertLess(a['Écart du bilan énergétique'],1e-10)

    def test_caisse_immobile_sur_plan(self):
        a,_=measures('plan_incline',body='block',alpha=15,fs=.4)
        self.assertEqual(a['Accélération du centre de masse'],0)

class TestToupie(unittest.TestCase):
    def test_norme_axe_et_invariants(self):
        a,r=measures('gyroscope',spin=12,duration=3)
        np.testing.assert_allclose(np.linalg.norm(r['scene']['axis'],axis=1),1,atol=1e-13)
        self.assertLess(a['Écart maximal de l’énergie'],1e-5)
        self.assertLess(a['Écart maximal de L_z'],1e-6)

    def test_precession_scaling_vitesse(self):
        a,_=measures('gyroscope',spin=20,duration=1)
        b,_=measures('gyroscope',spin=40,duration=1)
        self.assertAlmostEqual(a['Précession lente approchée'],2*b['Précession lente approchée'])

    def test_nutation_lacher_sans_precession(self):
        a,_=measures('gyroscope',spin=12,launch='rest',duration=3)
        self.assertGreater(a['Écart entre inclinaisons extrêmes'],.1)

if __name__=='__main__': unittest.main()
