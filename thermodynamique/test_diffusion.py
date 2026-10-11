"""Références indépendantes, bilans physiques et contrats de P23."""
from __future__ import annotations
import json
import math
from pathlib import Path
import sys
import unittest
import warnings

import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from catalogue_diffusion import LABS
from contenu_diffusion import EXERCISES,GUIDES,LESSONS
from commun import clean,integrate
import modeles_diffusion as m


LAB_BY_ID={lab['id']:lab for lab in LABS}

def parameters(id_,**changes):
    out={control['key']:control['value'] for control in LAB_BY_ID[id_]['controls']}
    out.update(changes)
    return out

def metric_value(result,index):
    return result['metrics'][index]['value']


class CatalogueTests(unittest.TestCase):
    def test_coverage_and_content(self):
        self.assertEqual(len(LABS),14)
        self.assertEqual(set(LAB_BY_ID),set(m.COMPUTE))
        self.assertEqual(len(LESSONS),28)
        self.assertEqual(len(EXERCISES),42)
        self.assertEqual(set(GUIDES),set(m.COMPUTE))
        for id_ in m.COMPUTE:
            self.assertEqual(sum(x['lab']==id_ for x in LESSONS),2)
            self.assertEqual(sum(x['lab']==id_ for x in EXERCISES),3)
            g=GUIDES[id_]
            self.assertEqual(len(g['first_steps']),3)
            self.assertEqual(set(g['levels']),{'sup','spe','beyond'})
            for name in ('purpose','objects','hypotheses','techniques','expected'):
                self.assertTrue(g[name],(id_,name))

    def test_presets_within_controls(self):
        for lab in LABS:
            controls={c['key']:c for c in lab['controls']}
            self.assertGreaterEqual(len(lab['presets']),3)
            for preset in lab['presets']:
                for key,value in preset['values'].items():
                    with self.subTest(lab=lab['id'],preset=preset['label'],key=key):
                        self.assertIn(key,controls)
                        control=controls[key]
                        if control['type']=='select':
                            self.assertIn(value,[o['value'] for o in control['options']])
                        else:
                            self.assertGreaterEqual(value,control['min'])
                            self.assertLessEqual(value,control['max'])

    def test_defaults_and_presets_export_finite_json(self):
        with warnings.catch_warnings():
            warnings.simplefilter('error',RuntimeWarning)
            for lab in LABS:
                candidates=[('défaut',parameters(lab['id']))]
                candidates.extend((preset['label'],parameters(lab['id'],**preset['values'])) for preset in lab['presets'])
                for name,p in candidates:
                    with self.subTest(lab=lab['id'],preset=name):
                        output=m.COMPUTE[lab['id']](p)
                        json.dumps(clean(output),allow_nan=False)
                        self.assertGreaterEqual(len(output['metrics']),4)
                        self.assertGreaterEqual(len(output['charts']),2)
                        self.assertTrue(output['scene']['description'])
                        self.assertTrue(output['scene']['xLabel'])
                        self.assertTrue(output['scene']['yLabel'])
                        if output['scene']['kind']=='heatmap':
                            self.assertTrue(output['scene']['zLabel'])
                        self.assertGreaterEqual(len(output['steps']),3)
                        self.assertTrue(output['assumptions'])

    def test_each_control_bound_and_choice_exports_finitely(self):
        with warnings.catch_warnings():
            warnings.simplefilter('error',RuntimeWarning)
            for lab in LABS:
                for control in lab['controls']:
                    values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                    for value in values:
                        with self.subTest(lab=lab['id'],key=control['key'],value=value):
                            out=m.COMPUTE[lab['id']](parameters(lab['id'],**{control['key']:value}))
                            json.dumps(clean(out),allow_nan=False)


class ConductionTests(unittest.TestCase):
    def test_bar_power_units(self):
        out=m.fourier_barre(parameters('fourier_barre'))
        self.assertAlmostEqual(metric_value(out,0),3.125)
        self.assertAlmostEqual(metric_value(out,1),9600)
        self.assertAlmostEqual(metric_value(out,2),19.2)
        profile=out['charts'][0]['series'][0]
        np.testing.assert_allclose(profile['y'],80-120*profile['x'],rtol=0,atol=3e-14)

    def test_bar_zero_difference_and_reversal(self):
        zero=m.fourier_barre(parameters('fourier_barre',T1=20,T2=20))
        self.assertAlmostEqual(metric_value(zero,2),0)
        self.assertGreater(metric_value(zero,0),0)
        backward=m.fourier_barre(parameters('fourier_barre',T1=0,T2=40))
        self.assertLess(metric_value(backward,2),0)
        self.assertGreater(metric_value(backward,3),0)

    def test_wall_series_and_interfaces(self):
        p=parameters('paroi_composite')
        R,P,T=m.wall_solution(p)
        reference=(1/p['hi']+p['e1']/p['k1']+p['e2']/p['k2']+1/p['ho'])/p['area']
        self.assertAlmostEqual(sum(R),reference)
        self.assertAlmostEqual(P,(p['Ti']-p['To'])/reference)
        np.testing.assert_allclose(T[:-1]-T[1:],P*R,rtol=2e-14,atol=1e-14)
        self.assertAlmostEqual(T[0],p['Ti'])
        self.assertAlmostEqual(T[-1],p['To'])

    def test_wall_reversed_transfer_and_insulation(self):
        p=parameters('paroi_composite',Ti=10,To=15)
        _,power,temp=m.wall_solution(p)
        self.assertLess(power,0)
        self.assertTrue(np.all(np.diff(temp)>0))
        p2=dict(p,e2=.4)
        self.assertLess(abs(m.wall_solution(p2)[1]),abs(power))

    def test_radial_critical_radii_are_loss_maxima(self):
        for geometry,factor in [('cylinder',1),('sphere',2)]:
            ri,k,h=.01,.1,4
            critical=factor*k/h
            radii=critical*np.array([.98,1,1.02])
            powers=60/m.radial_resistance(ri,radii,k,h,1,geometry)
            self.assertGreater(powers[1],powers[0])
            self.assertGreater(powers[1],powers[2])
            dh=critical*1e-5
            derivative=(m.radial_resistance(ri,critical+dh,k,h,1,geometry)-m.radial_resistance(ri,critical-dh,k,h,1,geometry))/(2*dh)
            self.assertLess(abs(derivative),1e-5)

    def test_radial_beyond_critical_is_monotone(self):
        for geometry in ['cylinder','sphere']:
            radii=np.linspace(.1,.5,100)
            resistance=m.radial_resistance(.1,radii,.1,10,1,geometry)
            self.assertTrue(np.all(np.diff(resistance)>0))

    def test_radial_zero_shell_is_convection(self):
        radius,length,k,h=.07,1.3,.2,15
        self.assertAlmostEqual(float(m.radial_resistance(radius,radius,k,h,length,'cylinder')),1/(h*2*math.pi*radius*length))
        self.assertAlmostEqual(float(m.radial_resistance(radius,radius,k,h,length,'sphere')),1/(h*4*math.pi*radius**2))

    def test_igloo_hemisphere_resistance_and_target(self):
        p=parameters('igloo')
        out=m.igloo(p)
        ri,ro=p['radius'],p['radius']+p['thickness']
        R=(1/ri-1/ro)/(2*math.pi*p['conductivity'])
        self.assertAlmostEqual(metric_value(out,1),R)
        power=p['people']*p['power']
        self.assertAlmostEqual(metric_value(out,2),p['To']+power*R)
        e=metric_value(out,4)
        self.assertIsInstance(e,float)
        achieved=p['To']+power*(1/ri-1/(ri+e))/(2*math.pi*p['conductivity'])
        self.assertAlmostEqual(achieved,p['target'])

    def test_igloo_impossible_and_melting_are_explicit(self):
        impossible=m.igloo(parameters('igloo',conductivity=2))
        self.assertIn('impossible',metric_value(impossible,4))
        melting=m.igloo(parameters('igloo',people=3))
        self.assertGreater(metric_value(melting,2),0)
        self.assertIn('fonte',metric_value(melting,3))
        self.assertTrue(any('pas un équilibre stationnaire réel' in x for x in melting['assumptions']))


class DiffusionTests(unittest.TestCase):
    def test_ftcs_stability_and_discrete_maximum_principle(self):
        x,t,grid,exact,r,steps=m.ftcs_modes(70,.3,.49,60,'two')
        self.assertLessEqual(r,.49+1e-14)
        self.assertAlmostEqual(t[-1],.3)
        self.assertGreater(steps,1)
        self.assertLessEqual(float(np.max(grid)),float(np.max(grid[0]))+1e-12)
        self.assertGreaterEqual(float(np.min(grid)),-1e-12)
        np.testing.assert_allclose(grid[:,[0,-1]],0,atol=1e-14)

    def test_ftcs_independent_discrete_eigenmode(self):
        n,time,requested=40,.08,.4
        x,t,grid,exact,r,steps=m.ftcs_modes(n,time,requested,1,'one')
        eigenfactor=1-4*r*math.sin(math.pi/(2*n))**2
        reference=eigenfactor**steps*np.sin(math.pi*x)
        np.testing.assert_allclose(grid[-1],reference,rtol=5e-13,atol=5e-15)

    def test_ftcs_second_order_spatial_refinement(self):
        errors=[]
        for n in [20,40,80]:
            x,t,grid,exact,r,steps=m.ftcs_modes(n,.08,.4,1,'two')
            errors.append(float(np.max(abs(grid[-1]-exact[-1]))))
        self.assertGreater(errors[0]/errors[1],3.5)
        self.assertGreater(errors[1]/errors[2],3.5)

    def test_fourier_high_mode_relaxes_nine_times_faster(self):
        x,t,grid,exact,r,steps=m.ftcs_modes(40,.03,.4,1,'two')
        basis1=np.sin(math.pi*x);basis3=np.sin(3*math.pi*x)
        amplitude1=integrate(exact[-1]*basis1,x)/integrate(basis1*basis1,x)
        amplitude3=integrate(exact[-1]*basis3,x)/integrate(basis3*basis3,x)
        self.assertAlmostEqual(-math.log(amplitude3/.4)/(-math.log(amplitude1)),9,places=12)

    def test_semispace_energy_space_and_time(self):
        p=parameters('demi_espace')
        out=m.demi_espace(p)
        D,C,t=p['D']*1e-6,p['capacity']*1e6,p['minutes']*60
        reference=2*C*(p['Ts']-p['T0'])*math.sqrt(D*t/math.pi)
        self.assertAlmostEqual(metric_value(out,3),reference,places=8)
        self.assertLess(abs(metric_value(out,4)/reference-1),1e-5)
        u=np.linspace(0,math.sqrt(t),2001)
        # t=u² élimine la singularité du flux dans l'intégrale temporelle.
        transformed=np.full_like(u,2*D*C*(p['Ts']-p['T0'])/math.sqrt(math.pi*D))
        self.assertAlmostEqual(float(integrate(transformed,u))/reference,1,places=12)

    def test_semispace_scaling_and_cooling_sign(self):
        one=m.demi_espace(parameters('demi_espace',minutes=30))
        four=m.demi_espace(parameters('demi_espace',minutes=120))
        self.assertAlmostEqual(metric_value(four,1)/metric_value(one,1),2)
        self.assertAlmostEqual(metric_value(four,2)/metric_value(one,2),.5)
        self.assertAlmostEqual(metric_value(four,3)/metric_value(one,3),2)
        cool=m.demi_espace(parameters('demi_espace',T0=30,Ts=0))
        self.assertLess(metric_value(cool,2),0)
        self.assertLess(metric_value(cool,3),0)

    def test_erfc_surface_deep_and_pde(self):
        D,t,x=1e-6,1000,.02
        f=lambda xx,tt: math.erfc(xx/(2*math.sqrt(D*tt)))
        self.assertAlmostEqual(f(0,t),1)
        self.assertLess(f(8*math.sqrt(D*t),t),2e-8)
        ht,hx=.01,1e-5
        time_derivative=(f(x,t+ht)-f(x,t-ht))/(2*ht)
        laplacian=(f(x+hx,t)-2*f(x,t)+f(x-hx,t))/hx**2
        self.assertLess(abs(D*laplacian/time_derivative-1),1e-5)

    def test_thermal_wave_penetration_and_phase(self):
        w,delta=m.thermal_wave_parameters(1e-6,86400)
        wa,annual=m.thermal_wave_parameters(1e-6,365.25*86400)
        self.assertAlmostEqual(annual/delta,math.sqrt(365.25))
        p=parameters('onde_thermique',depth=delta)
        out=m.onde_thermique(p)
        self.assertAlmostEqual(metric_value(out,3),1/math.e)
        self.assertAlmostEqual(metric_value(out,2)*3600,1/w)

    def test_thermal_wave_satisfies_heat_equation(self):
        D,period=1e-6,86400
        w,delta=m.thermal_wave_parameters(D,period)
        f=lambda z,t: math.exp(-z/delta)*math.cos(w*t-z/delta)
        z,t=.2,period*.17; hz=delta*1e-4;ht=period*1e-5
        time_derivative=(f(z,t+ht)-f(z,t-ht))/(2*ht)
        laplacian=(f(z+hz,t)-2*f(z,t)+f(z-hz,t))/hz**2
        self.assertLess(abs(D*laplacian/time_derivative-1),1e-6)

    def test_slab_eigenvalue_equation(self):
        for Bi in [.0001,.2,250]:
            roots=m.slab_eigenvalues(Bi,5)
            np.testing.assert_allclose(roots*np.tan(roots),Bi,rtol=5e-10,atol=5e-10)
            self.assertTrue(np.all(np.diff(roots)>0))

    def test_slab_initial_symmetry_and_mean(self):
        x=np.linspace(-1,1,1001)
        times=np.array([0,.2,.8])
        mean,center,surface,profile=m.slab_temperature(2,times,x)
        np.testing.assert_allclose(profile[0],1,atol=1e-14)
        np.testing.assert_allclose(profile,profile[:,::-1],atol=1e-14)
        np.testing.assert_allclose(integrate(profile,x)/2,mean,atol=5e-7,rtol=0)
        self.assertTrue(np.all(center[1:]>mean[1:]))
        self.assertTrue(np.all(mean[1:]>surface[1:]))

    def test_biot_small_lumped_and_large_gradient(self):
        times=np.linspace(0,2,201)
        mean,center,surface=m.slab_temperature(.002,times)
        self.assertLess(float(np.max(abs(mean-np.exp(-.002*times)))),5e-6)
        mean,center,surface=m.slab_temperature(10,np.array([.2]))
        self.assertGreater(float(center[0]-surface[0]),.3)

    def test_gaussian_heat_energy_and_variance(self):
        D,t,width,Q,Cs=2e-6,120,.01,20,4000
        variance=width**2+2*D*t
        x=np.linspace(-7*math.sqrt(variance),7*math.sqrt(variance),801)
        X,Y=np.meshgrid(x,x)
        theta=m.gaussian_heat(X,Y,D,t,width,Q,Cs)
        energy=Cs*float(integrate(integrate(theta,x),x))
        moment=Cs*float(integrate(integrate(theta*(X**2+Y**2),x),x))/Q
        self.assertAlmostEqual(energy/Q,1,places=10)
        self.assertAlmostEqual(moment/(2*variance),1,places=9)

    def test_gaussian_peak_declines_inverse_variance(self):
        a=m.gaussian_heat(np.array([0]),np.array([0]),2e-6,120,.01,20,4000)[0]
        b=m.gaussian_heat(np.array([0]),np.array([0]),2e-6,480,.01,20,4000)[0]
        self.assertAlmostEqual(a/b,(.01**2+2*2e-6*480)/(.01**2+2*2e-6*120))


class ParticleTests(unittest.TestCase):
    def test_binomial_normalization_and_moments(self):
        for n,p in [(20,.5),(100,.1),(300,.9)]:
            k,law=m.binomial_distribution(n,p)
            mean=float(k@law);variance=float(((k-mean)**2)@law)
            self.assertAlmostEqual(float(np.sum(law)),1)
            self.assertAlmostEqual(mean,n*p,places=10)
            self.assertAlmostEqual(variance,n*p*(1-p),places=10)

    def test_walk_parity_and_diffusion_coefficient(self):
        p=parameters('marche_aleatoire',N=20,step=2,dt=4)
        out=m.marche_aleatoire(p)
        self.assertAlmostEqual(metric_value(out,0),(.000002)**2/(2*.004),places=20)
        self.assertAlmostEqual(metric_value(out,1),0)
        positions=out['charts'][0]['series'][0]['x']/p['step']
        np.testing.assert_allclose(np.mod(positions,2),0,atol=1e-12)
        self.assertEqual(len(positions),p['N']+1)

    def test_biased_walk_centered_variance(self):
        p=parameters('marche_aleatoire',p=.7)
        out=m.marche_aleatoire(p)
        self.assertAlmostEqual(metric_value(out,2),p['N']*(2*p['p']-1)*p['step'])
        self.assertAlmostEqual(metric_value(out,3),4*p['N']*p['p']*(1-p['p'])*p['step']**2)
        self.assertGreater(metric_value(out,1),0)

    def test_stokes_einstein_and_equipartition_units(self):
        radius,eta,rho,T=.5e-6,.001,1050,300
        D,tau,mass,drag=m.langevin_parameters(radius,eta,rho,T)
        self.assertAlmostEqual(D*drag,m.KB*T,places=33)
        self.assertAlmostEqual(tau*drag,mass,places=30)
        self.assertAlmostEqual((D/tau)*mass,m.KB*T,places=32)
        other=m.langevin_parameters(radius,2*eta,rho,T)
        self.assertAlmostEqual(other[0]/D,.5)
        self.assertAlmostEqual(other[1]/tau,.5)

    def test_langevin_ballistic_and_diffusive_limits(self):
        D,tau=4e-13,3e-8
        short=tau*1e-6
        self.assertAlmostEqual(float(m.langevin_msd(short,D,tau))/(D/tau*short**2),1,places=6)
        long=tau*1e6
        self.assertAlmostEqual(float(m.langevin_msd(long,D,tau))/(2*D*long),1,places=5)
        values=m.langevin_msd(np.array([0,tau,100*tau]),D,tau)
        self.assertAlmostEqual(float(values[0]),0,places=30)
        self.assertTrue(np.all(np.diff(values)>0))
        self.assertAlmostEqual(float(values[1]),2*D*tau/math.e,places=30)

    def test_exact_langevin_ensemble_short_and_long_variances(self):
        D,tau=4e-13,3e-8
        for ratio in [.1,50]:
            t,ensemble=m.langevin_ensemble(D,tau,ratio*tau,count=4096,steps=100)
            reference=float(m.langevin_msd(t[-1],D,tau))
            per_axis=np.mean(ensemble[-1]**2,axis=0)
            np.testing.assert_allclose(per_axis,reference,rtol=.06,atol=0)
            self.assertEqual(ensemble.shape,(101,4096,2))

    def test_neutron_source_normalization_and_absorption(self):
        p=parameters('absorption_neutrons')
        out=m.absorption_neutrons(p)
        Q=p['source']*1e6;D=p['D']*1e-4;tau=p['lifetime'];L=math.sqrt(D*tau)
        self.assertAlmostEqual(metric_value(out,0),L)
        self.assertAlmostEqual(metric_value(out,1),Q*tau)
        radius=metric_value(out,2)
        self.assertAlmostEqual((1+radius/L)*math.exp(-radius/L),.1,places=14)
        streams=out['charts'][1]['series']
        np.testing.assert_allclose(streams[0]['y']+streams[1]['y'],Q,rtol=2e-16)
        self.assertAlmostEqual((1+1e-6)*math.exp(-1e-6),1,places=11)

    def test_neutron_inventory_integral_and_pde(self):
        Q,D,tau=2e7,.01,.3;L=math.sqrt(D*tau)
        r=np.linspace(0,25*L,50001)
        integrand=Q/D*r*np.exp(-r/L)
        number=float(integrate(integrand,r))
        self.assertLess(abs(number/(Q*tau)-1),3e-8)
        f=lambda rr: Q*math.exp(-rr/L)/(4*math.pi*D*rr)
        radius=L;h=radius*1e-4
        first=(f(radius+h)-f(radius-h))/(2*h)
        second=(f(radius+h)-2*f(radius)+f(radius-h))/h**2
        self.assertLess(abs(D*(second+2*first/radius)/(f(radius)/tau)-1),2e-7)


class ElectrolyteAndEntropyTests(unittest.TestCase):
    def test_ambipolar_harmonic_mean_and_equal_diffusion(self):
        Dp,Dm=1.3e-9,2e-9
        self.assertAlmostEqual(m.ambipolar(Dp,Dm),2/(1/Dp+1/Dm),places=24)
        self.assertGreater(m.ambipolar(Dp,Dm),min(Dp,Dm))
        self.assertLess(m.ambipolar(Dp,Dm),max(Dp,Dm))
        out=m.diffusion_electrolyte(parameters('diffusion_electrolyte',Dp=2,Dm=2))
        self.assertAlmostEqual(metric_value(out,0),2e-9,places=23)
        self.assertAlmostEqual(metric_value(out,1),0,places=15)
        self.assertAlmostEqual(metric_value(out,2),0,places=15)

    def test_electrolyte_equal_fluxes_and_zero_current(self):
        out=m.diffusion_electrolyte(parameters('diffusion_electrolyte'))
        curves=out['charts'][2]['series']
        scale=float(np.max(abs(curves[2]['y'])))
        np.testing.assert_allclose(curves[0]['y'],curves[2]['y'],atol=scale*5e-16,rtol=5e-16)
        np.testing.assert_allclose(curves[1]['y'],curves[2]['y'],atol=scale*5e-16,rtol=5e-16)
        self.assertLess(metric_value(out,3),1e-14)

    def test_potential_convention_and_endpoint_difference(self):
        p=parameters('diffusion_electrolyte')
        out=m.diffusion_electrolyte(p)
        potential=out['charts'][1]['series'][0];field=out['charts'][3]['series'][0]
        V=potential['y']/1000;x=potential['x']/1000
        numerical=-np.gradient(V,x)
        mask=abs(field['y'])>.02*np.max(abs(field['y']))
        np.testing.assert_allclose(numerical[mask],field['y'][mask],rtol=.003,atol=0)
        reference=m.KB*p['temperature']/m.E_CHARGE*(p['Dm']-p['Dp'])/(p['Dp']+p['Dm'])*math.log(p['right']/p['left'])*1000
        self.assertAlmostEqual(metric_value(out,1),reference,places=12)
        reversed_=m.diffusion_electrolyte(dict(p,left=p['right'],right=p['left']))
        self.assertAlmostEqual(metric_value(reversed_,1),-reference,places=12)

    def test_uniform_electrolyte_has_no_flux_or_field(self):
        out=m.diffusion_electrolyte(parameters('diffusion_electrolyte',left=20,right=20))
        for series in out['charts'][2]['series']:
            np.testing.assert_allclose(series['y'],0,atol=1e-20)
        self.assertAlmostEqual(metric_value(out,1),0)
        self.assertAlmostEqual(metric_value(out,2),0)

    def test_insulated_chain_energy_and_spectrum(self):
        A=m.insulated_chain_matrix(9,5,1000)
        np.testing.assert_allclose(A.sum(axis=0),0,atol=1e-16)
        np.testing.assert_allclose(A,A.T,atol=0)
        values=np.linalg.eigvalsh(A)
        self.assertLessEqual(float(values[-1]),1e-16)
        self.assertAlmostEqual(values[-2],-2*5/1000*(1-math.cos(math.pi/9)),places=16)

    def test_entropy_increases_energy_conserved_kelvin(self):
        out=m.entropie_diffusion(parameters('entropie_diffusion',N=9,hot=100,cold=0))
        self.assertLess(metric_value(out,2),1e-13)
        self.assertGreater(metric_value(out,3),0)
        self.assertLessEqual(metric_value(out,3),metric_value(out,4)+1e-9)
        entropy=out['charts'][1]['series'][0]['y']
        production=out['charts'][2]['series'][0]['y']
        self.assertTrue(np.all(np.diff(entropy)>=-1e-9))
        self.assertTrue(np.all(production>=0))
        self.assertAlmostEqual(metric_value(out,0),4*100/9,places=12)

    def test_two_cell_energy_and_entropy_rate_independently(self):
        C,G=1000,5;initial=np.array([353.15,293.15]);mean=float(np.mean(initial))
        A=m.insulated_chain_matrix(2,G,C);values,Q=np.linalg.eigh(A)
        time=73.
        temperature=Q@(np.exp(values*time)*(Q.T@initial))
        analytic=mean+(initial-mean)*math.exp(-2*G*time/C)
        np.testing.assert_allclose(temperature,analytic,rtol=2e-15)
        rate=C*np.sum((A@temperature)/temperature)
        production=G*(temperature[0]-temperature[1])**2/(temperature[0]*temperature[1])
        self.assertAlmostEqual(rate,production,places=14)
        maximum=C*math.log(mean**2/np.prod(initial))
        self.assertAlmostEqual(maximum,8.66,delta=.01)

    def test_uniform_chain_has_no_production_or_gain(self):
        out=m.entropie_diffusion(parameters('entropie_diffusion',hot=20,cold=20))
        for index in (3,4,5):
            self.assertAlmostEqual(metric_value(out,index),0,places=14)
        np.testing.assert_allclose(out['charts'][1]['series'][0]['y'],0,atol=1e-14)
        np.testing.assert_allclose(out['charts'][2]['series'][0]['y'],0,atol=1e-14)


if __name__=='__main__':
    unittest.main()
