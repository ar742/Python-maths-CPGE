"""Contrôles des bilans électroniques, de matière et de transfert."""
import math
import unittest
import numpy as np
from commun import clean,integrate
from catalogue_redox import LABS
from modeles_redox import (R,F,TREF,CALCULATORS,nernst_pile,electrolyse_h2,
    fuel_voltage,battery_ocv,corrosion_mixed,deposition_data,
    copper_conditional,silver_titration)

class RedoxTests(unittest.TestCase):
    def test_nernst_two_electron_slope_and_charge(self):
        p=dict(logcu=-2,logzn=-2,temperature=298,amount=.1)
        first=nernst_pile(p); second=nernst_pile({**p,'logcu':-4})
        e1=first['metrics'][0]['value']; e2=second['metrics'][0]['value']
        self.assertAlmostEqual(e2-e1,-R*298*math.log(100)/(2*F),delta=1.1e-5)
        self.assertAlmostEqual(first['metrics'][2]['value'],2*F*.1,delta=.00051)

    def test_electrolysis_charge_and_energy_balance(self):
        p=dict(current=100,hours=1,voltage=1.8,faraday=.95)
        data=electrolyse_h2(p); metrics={m['label']:m['value'] for m in data['metrics']}
        n=.95*100*3600/(2*F)
        self.assertAlmostEqual(metrics['H₂ produit'],n*.002016,delta=.000006)
        energy=100*3600*1.8/3.6e6
        self.assertAlmostEqual(metrics['Électricité consommée'],energy,places=5)
        self.assertAlmostEqual(metrics['Chaleur nette à évacuer'],energy-n*285830/3.6e6,delta=.000006)
        # At ideal thermoneutral voltage, heat exchange is zero.
        thermoneutral=electrolyse_h2({**p,'voltage':285830/(2*F),'faraday':1})
        self.assertEqual(thermoneutral['metrics'][3]['value'],0.)
        low=electrolyse_h2({**p,'voltage':1.3,'faraday':1})
        self.assertLess(low['metrics'][3]['value'],0)

    def test_fuel_cell_losses_have_correct_sign_and_units(self):
        j=np.linspace(0,1.9,101)
        v,activation,ohm,transport=fuel_voltage(j,.2,.02,2)
        self.assertAlmostEqual(float(v[0]),237130/(2*F),places=14)
        self.assertTrue(np.all(np.diff(v)<0))
        self.assertTrue(np.all(activation>=0)); self.assertTrue(np.all(transport>=0))
        np.testing.assert_allclose(ohm,.2*j,rtol=0,atol=1e-15)
        np.testing.assert_allclose(v+activation+ohm+transport,237130/(2*F),rtol=0,atol=2e-15)

    def test_battery_symmetry_monotonicity_and_energy_integral(self):
        s=np.linspace(.05,.95,181); u=battery_ocv(s)
        self.assertTrue(np.all(np.diff(u)>0))
        np.testing.assert_allclose(battery_ocv(s)+battery_ocv(1-s),6.8,rtol=0,atol=2e-15)
        # The symmetric open-circuit curve integrates to its central voltage.
        self.assertAlmostEqual(float(integrate(u,s)),3.4*.9,places=13)
        for r in (.01,.05,.15): self.assertTrue(np.all(u-20*r>0))

    def test_mixed_potential_conserves_current_and_zinc_protects(self):
        for limit in (.01,.2,1):
            for logfe in (-6,-5,-2):
                e0,j0,_,_=corrosion_mixed(limit,0,logfe)
                for area in (.25,1,5):
                    e,fe,zn,oxy=corrosion_mixed(limit,area,logfe)
                    self.assertAlmostEqual(fe+area*zn+oxy,0,delta=1e-13)
                    self.assertLess(e,e0)
                    self.assertLess(fe,j0)
                    self.assertGreater(zn,0)

    def test_deposition_uses_converted_fick_and_faraday_units(self):
        lim,I,n,mass,thickness=deposition_data(1,30,100,.1,100)
        self.assertAlmostEqual(lim,2*F*7e-10*100/1e-4*.01,places=12)
        self.assertEqual(I,1)
        self.assertAlmostEqual(n,1800/(2*F),places=14)
        self.assertAlmostEqual(mass,n*63.546,places=14)
        self.assertAlmostEqual(thickness*1e-4*100*8.96,mass,places=13)
        weak=deposition_data(20,30,500,.02,200)
        self.assertEqual(weak[1],weak[0]); self.assertLess(weak[1],20)
        agitated=deposition_data(20,30,500,.02,20)
        self.assertAlmostEqual(agitated[0]/weak[0],10,places=13)

    def test_complexation_potential_matches_free_species_nernst(self):
        for lig in (-5,-2,0):
            e1,e2,l1,l2=map(float,copper_conditional(lig,10.8,11.8))
            c=1e-3
            free1=c/(1+10**10.8*10**(2*lig)); free2=c/(1+10**11.8*10**(4*lig))
            self.assertAlmostEqual(e1+R*TREF/F*math.log(c),.521+R*TREF/F*math.log(free1),places=13)
            self.assertAlmostEqual(e2+R*TREF/(2*F)*math.log(c),.340+R*TREF/(2*F)*math.log(free2),places=13)
        e1,e2,_,_=map(float,copper_conditional(0,10.8,11.8))
        self.assertLess(e1,e2) # Cu(I) under the chord, positive dismutation energy.

    def test_titration_preserves_both_totals_and_finite_equivalence(self):
        ratios=np.r_[0,np.geomspace(1e-10,.99,75),1,np.linspace(1.001,2,75)]
        for c in (.02,.1,.2):
            for pks in (8,12,14):
                ag,br,s,prec=silver_titration(ratios,c,pks)
                self.assertTrue(np.all(ag>=0)); self.assertTrue(np.all(br>=0)); self.assertTrue(np.all(s>=0))
                np.testing.assert_allclose(ag+s,c*ratios/(1+ratios),rtol=0,atol=2e-16)
                np.testing.assert_allclose(br+s,c/(1+ratios),rtol=0,atol=2e-16)
                np.testing.assert_allclose((ag*br)[prec],10**(-pks),rtol=2e-12,atol=0)
                a,b,single,has=silver_titration(1,c,pks)
                self.assertTrue(has)
                self.assertAlmostEqual(float(a),10**(-pks/2),delta=1e-18)
                self.assertAlmostEqual(float(b),float(a),delta=1e-18)
        ag,br,s,has=silver_titration(0,.1,12)
        self.assertEqual(float(ag),0); self.assertFalse(has); self.assertEqual(float(s),0)

    def test_defaults_presets_and_extreme_combinations_are_finite(self):
        for lab in LABS:
            base={c['key']:c['value'] for c in lab['controls']}
            variants=[base]+[{**base,**p['values']} for p in lab['presets']]
            for control in lab['controls']:
                values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                variants.extend({**base,control['key']:v} for v in values)
            for endpoint in ('min','max'):
                variants.append({c['key']:c.get(endpoint,c['value']) for c in lab['controls']})
            for params in variants:
                with self.subTest(lab=lab['id'],params=params): clean(CALCULATORS[lab['id']](params))

if __name__=='__main__': unittest.main()
