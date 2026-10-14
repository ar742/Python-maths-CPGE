"""Contrôles indépendants des bilans et des équilibres thermochimiques."""
import math
import unittest
import numpy as np
from commun import clean
from catalogue_thermo import LABS
from modeles_thermo import (R,H_NO_REF,adiabatic_temperature,thermo_k,
    ammonia_equilibrium,methanol_equilibrium,zinc_gibbs,flash_ideal,
    alloy_compositions,alloy_state,CALCULATORS,hess_combustion)

class ThermochimieTests(unittest.TestCase):
    def test_hess_counts_water_and_co2_per_fuel(self):
        for name,M,nC,nH in [('methane',16.043,1,2),('hydrogen',2.016,0,1),('methanol',32.042,1,2)]:
            data=hess_combustion(dict(fuel=name,condensation=1,recovery=1))
            metrics={m['label']:m['value'] for m in data['metrics']}
            self.assertAlmostEqual(metrics['CO₂ direct'],nC*44.01/M,delta=.00051)
            self.assertAlmostEqual(metrics['PCS']-metrics['PCI'],nH*44.004/M,delta=.0011)
            self.assertEqual(metrics['Chaleur récupérée'],metrics['PCS'])

    def test_calorimetric_reference_and_inert_energy_balance(self):
        self.assertAlmostEqual(float(adiabatic_temperature(298,0,.93)),400,places=10)
        for ti in (278,298,498):
            for ni in (0,3,12):
                for f in (0,.5,.95):
                    for xi in (0,.2,1):
                        temperature=float(adiabatic_temperature(ti,ni,f,xi))
                        h=H_NO_REF-7.5*(ti-298)
                        remaining_sensible=(43.5-7.5*xi+29*ni)*(temperature-ti)
                        self.assertAlmostEqual(remaining_sensible+(1-f)*xi*h,0,delta=1e-9)
        self.assertLess(float(adiabatic_temperature(298,12,0)),float(adiabatic_temperature(298,0,0)))

    def test_kirchhoff_vant_hoff_derivative(self):
        T=725.; dt=.001
        derivative=(float(thermo_k(T+dt,-92220,-198.1,-45))-float(thermo_k(T-dt,-92220,-198.1,-45)))/(2*dt)
        H=-92220-45*(T-298.15)
        self.assertAlmostEqual(derivative,H/(R*T*T),delta=2e-11)

    def test_ammonia_equilibrium_has_correct_atoms_and_quotient(self):
        for T,P,inert in [(450,250,0),(900,1,4),(700,100,0),(450,1,4),(900,250,4)]:
            x=float(ammonia_equilibrium(T,P,inert)); nn=np.array([1-x,3*(1-x),2*x])
            self.assertTrue(0<x<1)
            self.assertAlmostEqual(2*nn[0]+nn[2],2,places=13)
            self.assertAlmostEqual(2*nn[1]+3*nn[2],6,places=13)
            a=nn*P/(sum(nn)+inert)
            lnQ=2*math.log(a[2])-math.log(a[0])-3*math.log(a[1])
            self.assertAlmostEqual(lnQ,float(thermo_k(T,-92220,-198.1,-45)),delta=2e-10)
        self.assertGreater(float(ammonia_equilibrium(700,200)),float(ammonia_equilibrium(700,20)))
        self.assertLess(float(ammonia_equilibrium(850,100)),float(ammonia_equilibrium(500,100)))
        self.assertLess(float(ammonia_equilibrium(700,100,4)),float(ammonia_equilibrium(700,100,0)))

    def test_methanol_equilibrium_with_limiting_hydrogen(self):
        for T,P,h in [(450,100,2),(650,5,6),(500,50,3),(450,5,6),(650,100,2)]:
            x=float(methanol_equilibrium(T,P,h)); nn=np.array([1-x,h-3*x,x,x])
            self.assertTrue(0<x<min(1,h/3)); self.assertTrue(np.all(nn>0))
            # Independent atom sums for C, H and O.
            self.assertAlmostEqual(nn[0]+nn[2],1,places=13)
            self.assertAlmostEqual(2*nn[1]+4*nn[2]+2*nn[3],2*h,places=13)
            self.assertAlmostEqual(2*nn[0]+nn[2]+nn[3],2,places=13)
            a=nn*P/sum(nn)
            lnQ=math.log(a[2])+math.log(a[3])-math.log(a[0])-3*math.log(a[1])
            self.assertAlmostEqual(lnQ,float(thermo_k(T,-49500,-177,-28)),delta=2e-11)
        # Carbon balance of the recycle: product + purge = fresh feed.
        for x in (.01,.25,.9):
            for r in (0,.8,.95):
                feed=1/(1-r*(1-x))
                self.assertAlmostEqual(x*feed+(1-r)*(1-x)*feed,1,places=13)

    def test_ellingham_is_continuous_with_correct_phase_slopes(self):
        for t in (693,1180):
            self.assertAlmostEqual(float(zinc_gibbs(t-1e-6)),float(zinc_gibbs(t+1e-6)),delta=1e-6)
        for t,sz in [(500,.0416),(900,.0416+6.7/693),(1400,.0416+6.7/693+114.8/1180)]:
            slope=float(zinc_gibbs(t+1)-zinc_gibbs(t))
            self.assertAlmostEqual(slope,.205+2*sz-2*.0436,places=12)
        # Independent reaction C+ZnO -> CO+Zn at 1400K.
        t=1400.; direct_h=-110.5+121.5-(-350.5)
        direct_s=.1976+(.0416+6.7/693+114.8/1180)-.0057-.0436
        co_line=-221-t*(2*.1976-2*.0057-.205)
        self.assertAlmostEqual((co_line-float(zinc_gibbs(t)))/2,direct_h-t*direct_s,places=11)

    def test_ideal_flash_conserves_both_components(self):
        cases=0
        for alpha in (1.2,3,6):
            for z in np.linspace(.05,.95,19):
                for pressure in (.3,.7,1,1.7,2):
                    xl,yv,beta,phase=flash_ideal(float(z),pressure,alpha)
                    self.assertTrue(0<=beta<=1)
                    actual=(1-beta)*(xl if xl is not None else 0)+beta*(yv if yv is not None else 0)
                    self.assertAlmostEqual(actual,z,places=12)
                    if phase=='liquide + vapeur':
                        cases+=1
                        self.assertAlmostEqual(yv*pressure,.5*alpha*xl,places=12)
                        self.assertAlmostEqual((1-yv)*pressure,.5*(1-xl),places=12)
                        self.assertTrue(xl<z<yv)
        self.assertGreater(cases,20)

    def test_alloy_chemical_potentials_and_lever(self):
        for t in (1360,1400,1500,1600,1726):
            xl,xs=map(float,alloy_compositions(t))
            self.assertTrue(0<xl<xs<1)
            # µL−µS=ΔGfusion+RT ln(xL/xS)=0 for each constituent.
            residual_b=17480*(1-t/1728)+R*t*math.log(xl/xs)
            residual_a=13050*(1-t/1358)+R*t*math.log((1-xl)/(1-xs))
            self.assertAlmostEqual(residual_b,0,delta=1e-9)
            self.assertAlmostEqual(residual_a,0,delta=1e-9)
            z=(xl+xs)/2; _,_,fs,phase=alloy_state(t,z)
            self.assertEqual(phase,'liquide + solide'); self.assertAlmostEqual(fs,.5,places=12)
        for t in (1300,1358,1400,1500,1728,1800):
            for z in (.05,.5,.95):
                xl,xs,fs,_=alloy_state(t,z)
                self.assertAlmostEqual((1-fs)*(xl or 0)+fs*(xs or 0),z,places=12)

    def test_all_defaults_presets_and_boundaries_are_finite(self):
        for lab in LABS:
            base={c['key']:c['value'] for c in lab['controls']}
            variants=[base]+[{**base,**p['values']} for p in lab['presets']]
            for control in lab['controls']:
                values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                variants.extend({**base,control['key']:value} for value in values)
            for params in variants:
                with self.subTest(lab=lab['id'],params=params): clean(CALCULATORS[lab['id']](params))

if __name__=='__main__': unittest.main()
