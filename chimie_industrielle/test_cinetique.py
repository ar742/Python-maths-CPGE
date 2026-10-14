"""Contrôles indépendants de bilans, limites et équilibres cinétiques."""
import math
import unittest
import numpy as np
from commun import integrate
from modeles_cinetique import (coverage,conversions,successive,chain_rates,
    arrhenius_k,effectiveness,grain_profile,heat_equilibria,heat_terms,
    emballement_thermique,horloge_iode,R)

class CinetiqueTests(unittest.TestCase):
    def test_horloge_separates_measured_threshold_and_assumed_half_reaction(self):
        for volume in (8,10,14):
            output=horloge_iode({'vmax':volume})
            threshold=next(m for m in output['metrics'] if m['label']=='Seuil de 5 mL du recueil')
            self.assertEqual(threshold['value'],315)
            self.assertEqual(output['charts'][0]['series'][0]['y'].tolist(),[1,2,3,4,5,6])
        self.assertIn('ordre 1',[m['value'] for m in horloge_iode({'vmax':10})['metrics']])

    def test_arrhenius_reference_and_temperature_ratio(self):
        self.assertAlmostEqual(float(arrhenius_k(500,80)),.01)
        ratio=float(arrhenius_k(550,80)/arrhenius_k(450,80))
        self.assertAlmostEqual(math.log(ratio),80000/R*(1/450-1/550))

    def test_reactor_ordering_and_limit_many_tanks(self):
        times=np.linspace(0,180,121)
        tank,piston,series=conversions(.01,times,8)
        self.assertTrue(np.all(tank<=series+1e-12))
        self.assertTrue(np.all(series<=piston+1e-12))
        self.assertAlmostEqual(conversions(.01,1,1)[0],conversions(.01,1,1)[2])
        self.assertAlmostEqual(conversions(.01,1,1000000)[1],conversions(.01,1,1000000)[2],places=6)

    def test_successive_conservation_equal_rates_and_optimum(self):
        for first,second in ((.1,.04),(.1,.1),(.01,.5),(.1,.10000000001)):
            times=np.linspace(0,300,601);a,b,c=successive(first,second,times)
            np.testing.assert_allclose(a+b+c,1,atol=2e-15)
            self.assertTrue(np.all(np.minimum(a,np.minimum(b,c))>=-1e-14))
            optimal=1/first if abs(first-second)<1e-12 else math.log(second/first)/(second-first)
            aa,bb,_=successive(first,second,optimal)
            self.assertAlmostEqual(float(first*aa),float(second*bb),places=9)
        np.testing.assert_allclose(successive(.1,.1,np.array([0,10,20]))[1],np.array([0,1,2])*np.exp(-np.array([0,1,2])))

    def test_surface_fractions_and_competition(self):
        pressures=np.linspace(0,10,101)
        free,a,b=coverage(pressures,3,2,4)
        np.testing.assert_allclose(free+a+b,1,atol=1e-15)
        self.assertTrue(np.all(a<=coverage(pressures,0,2,4)[1]))

    def test_ethanal_atom_balances_and_effective_order(self):
        for c in (.001,.1,1):
            total,h2,methane=chain_rates(c,1e-6,100,1e6)
            ethane=h2;co=total
            self.assertAlmostEqual(2*total,co+methane+2*ethane)
            self.assertAlmostEqual(4*total,2*h2+4*methane+6*ethane)
            apparent=(2*h2+1.5*methane)/total
            self.assertLessEqual(1,apparent);self.assertLessEqual(apparent,1.5)

    def test_simple_thermal_root_exactly_on_mesh_is_not_lost(self):
        h=.14833982792436007
        roots=heat_equilibria(300,.5,60,h)
        self.assertEqual(len(roots),2)
        self.assertAlmostEqual(roots[0][0],305)
        self.assertLess(roots[0][1],0);self.assertGreater(roots[1][1],0)
        for temperature,_ in roots:
            produced,removed=heat_terms(temperature,300,.5,60,h)
            self.assertAlmostEqual(float(produced),float(removed),places=10)

    def test_thermal_trajectory_reaches_stable_root_and_stops_in_domain(self):
        params=dict(ambient=300,qref=.5,ea=30,h=1,initial=300)
        output=emballement_thermique(params)
        trajectory=output['charts'][0]['series'][0]
        stable=heat_equilibria(300,.5,30,1)[0][0]
        self.assertAlmostEqual(trajectory['y'][-1],stable,places=6)
        params.update(qref=2,ea=100,h=.05,initial=350)
        trajectory=emballement_thermique(params)['charts'][0]['series'][0]
        self.assertTrue(all(250<=value<=390 for value in trajectory['y']))
        self.assertLess(trajectory['x'][-1],1800)

    def test_thiele_volume_integral_and_center_limit(self):
        radial=np.linspace(0,1,20001)
        for phi in (.001,.1,1,10,150):
            profile=grain_profile(radial,phi)
            reference=3*integrate(profile*radial**2,radial)
            self.assertAlmostEqual(float(effectiveness(phi)),reference,delta=1e-6)
            self.assertAlmostEqual(float(profile[0]),phi/math.sinh(phi))
            self.assertAlmostEqual(float(profile[-1]),1)
            self.assertTrue(np.all(profile>=0));self.assertTrue(np.all(profile<=1+1e-12))

if __name__=='__main__':unittest.main()
