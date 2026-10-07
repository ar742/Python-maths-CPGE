"""Contrôles de conservation, limites, cinétiques et cas de synthèse."""
import json
import math
import unittest
import numpy as np
from catalogue_reactivite import LABS
from commun import R, clean
import modeles_reactivite as models

DEFAULTS={lab['id']:{c['key']:c['value'] for c in lab['controls']} for lab in LABS}
def calc(id_,**changes): return models.calculate(id_,{**DEFAULTS[id_],**changes})

class KineticsAndEquilibria(unittest.TestCase):
    def test_acid_unit_constant(self): self.assertAlmostEqual(models.acid_extent(0,1),.5,places=12)
    def test_acid_k100(self): self.assertAlmostEqual(models.acid_extent(2,1),10/11,places=12)
    def test_acid_weak(self): self.assertAlmostEqual(models.acid_extent(-4,1),1/101,places=12)
    def test_acid_base_limiting(self): self.assertAlmostEqual(models.acid_extent(40,.3),.3,places=12)
    def test_acid_acid_limiting(self): self.assertAlmostEqual(models.acid_extent(40,2),1,places=12)
    def test_acid_monotone(self): self.assertTrue(all(a<b for a,b in zip([models.acid_extent(d,1) for d in [-4,-2,0,2]],[models.acid_extent(d,1) for d in [-2,0,2,4]])))
    def test_acid_unequal_equilibrium(self):
        x=models.acid_extent(1.3,.7);self.assertAlmostEqual(x*x/((1-x)*(.7-x)),10**1.3,places=10)
    def test_acid_both_mass_balances(self):
        r=calc('acidebase',base_ratio=.7,concentration=.2);a,b,aa,bh=r['concentrations'];self.assertAlmostEqual(a+aa,.2);self.assertAlmostEqual(b+bh,.14)
    def test_acid_charge_balance(self): r=calc('acidebase');self.assertEqual(r['concentrations'][2],r['concentrations'][3])
    def test_second_order_equal_analytic(self):
        a,b,x=models.second_order(.2,.2,.5,np.array([0,10]));self.assertAlmostEqual(a[-1],.1);np.testing.assert_allclose(a,b)
    def test_second_order_unequal_mass(self):
        a,b,x=models.second_order(.2,.6,.3,np.linspace(0,80,80));np.testing.assert_allclose(a+x,.2);np.testing.assert_allclose(b+x,.6)
    def test_second_order_reverse_mass(self):
        a,b,x=models.second_order(.6,.2,.3,np.linspace(0,80,80));np.testing.assert_allclose(a+x,.6);np.testing.assert_allclose(b+x,.2)
    def test_second_order_exchange_symmetry(self):
        a,b,x=models.second_order(.2,.6,.3,np.arange(10));aa,bb,xx=models.second_order(.6,.2,.3,np.arange(10));np.testing.assert_allclose(a,bb);np.testing.assert_allclose(b,aa);np.testing.assert_allclose(x,xx)
    def test_second_order_limit(self):
        a,b,x=models.second_order(.2,.6,.3,np.array([1e5]));self.assertAlmostEqual(x[-1],.2);self.assertAlmostEqual(b[-1],.4)
    def test_second_order_zero_rate(self):
        a,b,x=models.second_order(.2,.6,0,np.array([0,100]));np.testing.assert_allclose(x,0);np.testing.assert_allclose(a,.2)
    def test_second_order_initial_derivative(self):
        a,b,x=models.second_order(.2,.6,.3,np.array([0,1e-5]));self.assertAlmostEqual((x[1]-x[0])/1e-5,.036,places=6)
    def test_sn2_tertiary_blocked(self): r=calc('sn2',substrate='tertiary');self.assertFalse(r['allowed']);np.testing.assert_allclose(r['product'],0)
    def test_sn2_vinyl_blocked(self): r=calc('sn2',substrate='vinyl');self.assertFalse(r['allowed']);np.testing.assert_allclose(r['product'],0)
    def test_sn2_initial_rate(self): self.assertAlmostEqual(calc('sn2',k=.2,a0=.3,b0=.4)['initial_rate'],.024)
    def test_consecutive_conservation(self):
        a,i,b=models.consecutive(.02,.1,np.linspace(0,500,100));np.testing.assert_allclose(a+i+b,1);self.assertTrue(np.all(i>=0))
    def test_consecutive_equal_rates(self):
        a,i,b=models.consecutive(.1,.1,np.array([10.]));self.assertAlmostEqual(i[0],1/math.e);self.assertAlmostEqual(a[0],1/math.e)
    def test_consecutive_initial_condition(self):
        a,i,b=models.consecutive(.02,.1,np.array([0.]));self.assertEqual(a[0],1);self.assertEqual(i[0],0);self.assertEqual(b[0],0)
    def test_consecutive_intermediate_maximum(self):
        k1=.02;k2=.1;tm=math.log(k2/k1)/(k2-k1);_,i,_=models.consecutive(k1,k2,np.array([tm-1,tm,tm+1]));self.assertGreater(i[1],i[0]);self.assertGreater(i[1],i[2])
    def test_sn1_primary_blocked(self): self.assertFalse(calc('sn1',substrate='primary')['allowed'])
    def test_sn1_benzyl_allowed(self): self.assertTrue(calc('sn1',substrate='benzyl')['allowed'])
    def test_sn1_ideal_faces(self): r=calc('sn1',bias=0);self.assertEqual(r['back_fraction'],.5);self.assertEqual(r['front_fraction'],.5)
    def test_sn1_ion_pair_bias(self): r=calc('sn1',bias=20);self.assertAlmostEqual(r['back_fraction'],.7);self.assertAlmostEqual(r['front_fraction'],.3)
    def test_competition_one_ionization(self):
        r=calc('competition',substrate='tertiary',nu=0,base=0,k_ion=.1,capture=80);self.assertAlmostEqual(sum(r['rates']),.1)
    def test_competition_conservation(self):
        r=calc('competition');np.testing.assert_allclose(r['remaining']+r['products'].sum(axis=0),1)
    def test_competition_methyl_no_elimination(self):
        r=calc('competition',substrate='methyl',base=2);self.assertEqual(r['rates'][2],0);self.assertEqual(r['rates'][3],0)
    def test_competition_tertiary_no_sn2(self): self.assertEqual(calc('competition',substrate='tertiary')['rates'][0],0)
    def test_competition_zero(self):
        r=calc('competition',nu=0,base=0,k_ion=0);np.testing.assert_allclose(r['shares'],0);np.testing.assert_allclose(r['remaining'],1)
    def test_eyring_reference(self):
        # 60 kJ/mol, entropy zero : known formula recomputed from constants.
        expected=1.380649e-23*300/6.62607015e-34*math.exp(-60000/(R*300));self.assertAlmostEqual(models.eyring(60,0,300)/expected,1,places=12)
    def test_eyring_entropy_tenfold(self):
        ratio=models.eyring(60,R*math.log(10),300)/models.eyring(60,0,300);self.assertAlmostEqual(ratio,10,places=10)
    def test_kinetic_equal_barriers(self): r=calc('cinetique',ha=65,hb=65,sa=-40,sb=-40);np.testing.assert_allclose(r['kinetic_shares'],.5)
    def test_thermodynamic_equal_levels(self): r=calc('cinetique',ga=-12,gb=-12);np.testing.assert_allclose(r['thermodynamic_shares'],.5)
    def test_kinetic_vs_thermo_distinct(self): r=calc('cinetique');self.assertGreater(r['kinetic_shares'][0],.5);self.assertLess(r['thermodynamic_shares'][0],.5)
    def test_kinetic_mass_conservation(self):
        r=calc('cinetique');np.testing.assert_allclose(r['reactant']+r['products'].sum(axis=0),1)
    def test_barrier_shift_invariance(self):
        np.testing.assert_allclose(models.fractions_from_barriers([60,65],300),models.fractions_from_barriers([80,85],300))
    def test_multiplicity_not_missing(self): np.testing.assert_allclose(models.fractions_from_barriers([80,80,80],300,[2,2,1]),[.4,.4,.2])

class RulesAndTools(unittest.TestCase):
    def test_elimination_anti(self): r=calc('elimination',dihedral=180);self.assertTrue(r['anti']);self.assertEqual(r['reactive_fraction'],1)
    def test_elimination_nonanti(self): r=calc('elimination',dihedral=60);self.assertFalse(r['anti']);np.testing.assert_allclose(r['product_shares'],0)
    def test_elimination_syn_not_called_anti(self): self.assertFalse(calc('elimination',dihedral=0)['anti'])
    def test_chair_boltzmann(self): r=calc('elimination',system='cyclohexane',temperature=300,chair_gap=8);self.assertAlmostEqual(r['chair_population'],1/(1+math.exp(8000/(R*300))))
    def test_chair_beta_h_missing(self): r=calc('elimination',system='cyclohexane');np.testing.assert_allclose(r['product_shares'],[0,1])
    def test_chair_population_warming(self): self.assertGreater(calc('elimination',system='cyclohexane',temperature=400)['chair_population'],calc('elimination',system='cyclohexane',temperature=250)['chair_population'])
    def test_alkene_hydroboration_primary(self): self.assertEqual(calc('alcene',substrate='propene',reagent='borane')['product_name'],'Propan-1-ol')
    def test_alkene_hydration_secondary(self): self.assertEqual(calc('alcene',substrate='propene',reagent='water')['product_name'],'Propan-2-ol')
    def test_alkene_rearrangement(self): r=calc('alcene',substrate='rearrange',reagent='hbr');self.assertTrue(r['rearrangement']);self.assertEqual(r['product_name'],'2-bromo-2-méthylbutane')
    def test_alkene_bromination_E_meso(self): self.assertIn('meso',calc('alcene',substrate='butene_E',reagent='bromine')['product_name'])
    def test_alkene_bromination_Z_racemic(self): self.assertIn('Racémique',calc('alcene',substrate='butene_Z',reagent='bromine')['product_name'])
    def test_alkene_syn_diol_Z_meso(self): self.assertIn('meso',calc('alcene',substrate='butene_Z',reagent='diol')['product_name'])
    def test_alkene_ozone_two_fragments(self): r=calc('alcene',substrate='propene',reagent='ozone',stage=2);self.assertEqual(len(r['scene']['molecules']),3);self.assertIn('Méthanal',r['product_name'])
    def test_lindlar_Z(self): self.assertEqual(calc('alcyne',substrate='butyne',reagent='lindlar')['product_name'],'(Z)-but-2-ène')
    def test_dissolved_metal_E(self): self.assertEqual(calc('alcyne',substrate='butyne',reagent='dissolving')['product_name'],'(E)-but-2-ène')
    def test_alkyne_complete_two_h2(self): self.assertEqual(calc('alcyne',reagent='hydrogen')['equivalents'],2)
    def test_terminal_hydration_ketone(self): self.assertEqual(calc('alcyne',substrate='propyne',reagent='mercury')['product_name'],'Propanone')
    def test_terminal_hydroboration_aldehyde(self): self.assertEqual(calc('alcyne',substrate='propyne',reagent='borane')['product_name'],'Propanal')
    def test_hbr_twice_geminal(self): self.assertEqual(calc('alcyne',substrate='propyne',reagent='hbr2')['product_name'],'2,2-dibromopropane')
    def test_radical_statistics_no_selectivity(self): r=calc('radical',selectivity=1);self.assertAlmostEqual(r['tertiary_fraction'],.1)
    def test_radical_statistics_bromination(self): r=calc('radical',selectivity=1600);self.assertAlmostEqual(r['tertiary_fraction'],1600/1609)
    def test_radical_stationary_balance(self): r=calc('radical',initiation=.001,termination=1e7);self.assertAlmostEqual(2e7*r['radical_concentration']**2,.001)
    def test_radical_square_root_source(self): a=calc('radical',initiation=.001)['radical_concentration'];b=calc('radical',initiation=.004)['radical_concentration'];self.assertAlmostEqual(b/a,2)
    def test_peroxide_hbr(self): r=calc('radical',mode='peroxide',halogen='hbr');self.assertTrue(r['chain_supported']);self.assertTrue(all(x<0 for x in r['propagation_enthalpies']))
    def test_peroxide_hcl_not(self): r=calc('radical',mode='peroxide',halogen='hcl');self.assertFalse(r['chain_supported']);self.assertGreater(r['propagation_enthalpies'][1],0)
    def test_peroxide_hi_not(self): r=calc('radical',mode='peroxide',halogen='hi');self.assertFalse(r['chain_supported']);self.assertGreater(r['propagation_enthalpies'][0],0)
    def test_grignard_protons_first(self): r=calc('grignard',substrate='protic',equivalents=1,water=0);self.assertEqual(r['available_equivalents'],0);self.assertEqual(r['destroyed_equivalents'],1)
    def test_grignard_water_first(self): r=calc('grignard',substrate='ketone',equivalents=1,water=1);self.assertEqual(r['stoichiometric_upper_bound'],0)
    def test_grignard_ester_needs_two(self): r=calc('grignard',substrate='ester',equivalents=2);self.assertEqual(r['required_equivalents'],2);self.assertTrue(r['full_stoichiometry'])
    def test_grignard_ester_one_not_ketone(self): r=calc('grignard',substrate='ester',equivalents=1);self.assertFalse(r['full_stoichiometry']);self.assertIn('Mélange',r['product_name']);self.assertEqual(r['stoichiometric_upper_bound'],.5)
    def test_grignard_methanal_primary(self): self.assertIn('primaire',calc('grignard',substrate='methanal')['product_name'])
    def test_grignard_ketone_tertiary(self): self.assertIn('tertiaire',calc('grignard',substrate='ketone')['product_name'])
    def test_grignard_co2_acid(self): self.assertIn('Acide',calc('grignard',substrate='co2')['product_name'])
    def test_carbonyle_stage_clamped(self): r=calc('carbonyle',reaction='aldol',stage=4);self.assertEqual(r['stage'],2);self.assertEqual(r['scene']['index'],2)
    def test_ester_remove_water(self): self.assertGreater(calc('carbonyle',reaction='ester',water=.05)['equilibrium_fraction'],calc('carbonyle',reaction='ester',water=2)['equilibrium_fraction'])
    def test_acetal_equilibrium_known(self): self.assertAlmostEqual(calc('carbonyle',reaction='acetal',equilibrium=4,water=1)['equilibrium_fraction'],.8)
    def test_nabh4_spares_ester(self): self.assertFalse(calc('oxydoreduction',substrate='ester',reagent='nabh4')['reacts'])
    def test_lialh4_reduces_ester_four_e(self): r=calc('oxydoreduction',substrate='ester',reagent='lialh4');self.assertTrue(r['reacts']);self.assertEqual(r['electrons_per_center'],4)
    def test_alcohol_primary_to_ald_two_e(self): r=calc('oxydoreduction',substrate='alcohol1',reagent='pcc');self.assertEqual(r['product_name'],'Éthanal');self.assertEqual(r['electrons_per_center'],2)
    def test_alcohol_primary_to_acid_four_e(self): r=calc('oxydoreduction',substrate='alcohol1',reagent='aqueous');self.assertEqual(r['product_name'],'Acide éthanoïque');self.assertEqual(r['electrons_per_center'],4)
    def test_alcohol_tertiary_no_h(self): self.assertFalse(calc('oxydoreduction',substrate='alcohol3',reagent='aqueous')['reacts'])
    def test_nitro_to_aniline_six_e(self): r=calc('oxydoreduction',substrate='nitro',reagent='metal');self.assertEqual(r['product_name'],'Aniline');self.assertEqual(r['electrons_per_center'],6)
    def test_halogen_deactivating_ortho_para(self): r=calc('aromatique',substituent='chloro');self.assertEqual(r['orientation'],'ortho / para');self.assertEqual(r['activation'],'désactivant')
    def test_nitro_meta(self): self.assertEqual(calc('aromatique',substituent='nitro')['orientation'],'méta')
    def test_fc_nitro_blocked(self): r=calc('aromatique',substituent='nitro',reaction='acylation');self.assertFalse(r['allowed']);np.testing.assert_allclose(r['shares'],0)
    def test_aromatic_site_multiplicity(self): np.testing.assert_allclose(calc('aromatique',substituent='h',go=80,gm=80,gp=80)['shares'],[.4,.4,.2])
    def test_electrons_acid_inventory(self): self.assertEqual(calc('electrons',reaction='acid')['electron_inventory'],42)
    def test_electrons_sn2_inventory(self): self.assertEqual(calc('electrons',reaction='sn2')['electron_inventory'],54)
    def test_electrons_homolysis_inventory(self): self.assertEqual(calc('electrons',reaction='homolysis')['electron_inventory'],70)
    def test_electrons_resonance_inventory(self): self.assertEqual(calc('electrons',reaction='resonance')['electron_inventory'],32)
    def test_electrons_resonance_no_energy_barrier(self): self.assertEqual(len(calc('electrons',reaction='resonance')['charts']),1)
    def test_homolysis_endothermic_no_hump(self):
        curve=calc('electrons',reaction='homolysis')['charts'][1]['series'][0];self.assertGreater(curve['y'][-1],190);self.assertTrue(np.all(np.diff(curve['y'])>=0))
    def test_homolysis_not_arbitrary_barrier(self):
        a=calc('electrons',reaction='homolysis',barrier=10);b=calc('electrons',reaction='homolysis',barrier=100);np.testing.assert_allclose(a['charts'][1]['series'][0]['y'],b['charts'][1]['series'][0]['y'])
    def test_homolysis_morse_zero_at_equilibrium(self): self.assertEqual(calc('electrons',reaction='homolysis')['charts'][1]['series'][0]['y'][0],0)
    def test_alcyne_bilan_stage_clamped(self): r=calc('alcyne',reagent='lindlar',stage=2);self.assertEqual(r['stage'],1);self.assertEqual(len(r['scene']['frames']),2)

class OrbitalModels(unittest.TestCase):
    def test_lcao_overlap_normalization(self): r=calc('orbitales',system='lcao',overlap=.6);c=r['coefficients'];np.testing.assert_allclose(c.T@np.array([[1,.6],[.6,1]])@c,np.eye(2),atol=1e-14)
    def test_lcao_orthogonal_limit(self): r=calc('orbitales',system='lcao',overlap=0,beta=2);np.testing.assert_allclose(r['energies'],[-2,2]);np.testing.assert_allclose(abs(r['coefficients']),1/math.sqrt(2))
    def test_huckel_butadiene_known_roots(self):
        r=calc('orbitales',system='butadiene',beta=1,torsion=0);expected=np.sort([-2*math.cos(j*math.pi/5) for j in range(1,5)]);np.testing.assert_allclose(r['energies'],expected,atol=1e-14)
    def test_huckel_benzene_known_roots(self): np.testing.assert_allclose(calc('orbitales',system='benzene',beta=1)['energies'],[-2,-1,-1,1,1,2],atol=1e-14)
    def test_huckel_eigenvectors(self): r=calc('orbitales',system='benzene');np.testing.assert_allclose(r['matrix']@r['coefficients'],r['coefficients']*r['energies'],atol=1e-13)
    def test_huckel_orthonormal(self): r=calc('orbitales',system='butadiene');np.testing.assert_allclose(r['coefficients'].T@r['coefficients'],np.eye(4),atol=1e-14)
    def test_huckel_benzene_electron_sum(self): r=calc('orbitales',system='benzene');self.assertAlmostEqual(sum(r['occupations']),6);self.assertAlmostEqual(sum(r['populations']),6)
    def test_huckel_benzene_uniform_populations(self): np.testing.assert_allclose(calc('orbitales',system='benzene')['populations'],1,atol=1e-14)
    def test_four_pi_open_shell_not_benzene(self): r=calc('orbitales',system='cyclobutadiene',beta=1);np.testing.assert_allclose(r['occupations'],[2,1,1,0]);self.assertAlmostEqual(r['gap'],0,places=12)
    def test_four_pi_uniform_populations(self): np.testing.assert_allclose(calc('orbitales',system='cyclobutadiene')['populations'],1,atol=1e-14)
    def test_butadiene_twisted_splits_dimers(self): np.testing.assert_allclose(calc('orbitales',system='butadiene',beta=1,torsion=90)['energies'],[-1,-1,1,1],atol=1e-14)
    def test_butadiene_cis_trans_same_spectrum(self): np.testing.assert_allclose(calc('orbitales',system='butadiene',torsion=0)['energies'],calc('orbitales',system='butadiene',torsion=180)['energies'],atol=1e-14)
    def test_diels_cis_allowed(self): self.assertTrue(calc('orbitales',system='diels',torsion=0)['diels_geometry_allowed'])
    def test_diels_trans_requires_rotation(self): self.assertFalse(calc('orbitales',system='diels',torsion=180)['diels_geometry_allowed'])
    def test_orbital_index_clamped(self): self.assertEqual(calc('orbitales',system='lcao',orbital=6)['selected'],1)

class StructuralChecks(unittest.TestCase):
    def test_catalogue_unique_complete(self): self.assertEqual(len(LABS),15);self.assertEqual(len({l['id'] for l in LABS}),15);self.assertEqual(set(DEFAULTS),set(models.CALCULATORS))
    def test_every_preset_finite(self):
        for lab in LABS:
            for preset in lab['presets']:
                with self.subTest(lab=lab['id'],preset=preset['label']): json.dumps(clean(calc(lab['id'],**preset['values'])),allow_nan=False)
    def test_every_control_extreme_finite(self):
        for lab in LABS:
            for c in lab['controls']:
                values=[v['value'] for v in c['options']] if c['type']=='select' else [c['min'],c['max']]
                for value in values:
                    with self.subTest(lab=lab['id'],key=c['key'],value=value): json.dumps(clean(calc(lab['id'],**{c['key']:value})),allow_nan=False)
    def test_all_graphs_have_existing_bond_ends(self):
        for lab in LABS:
            for preset in lab['presets']:
                r=calc(lab['id'],**preset['values']);s=r['scene'];graphs=s.get('frames',s.get('molecules',[]))
                for g in graphs:
                    with self.subTest(lab=lab['id'],graph=g['name']):
                        ids=[a['id'] for a in g['atoms']];self.assertEqual(len(ids),len(set(ids)))
                        for b in g['bonds']: self.assertIn(b['a'],ids);self.assertIn(b['b'],ids);self.assertIn(b['order'],[1,2,3])
                        for arrow in g['arrows']: self.assertIn(arrow['electrons'],[1,2]);self.assertEqual(len(arrow['start']),2);self.assertEqual(len(arrow['end']),2)
    def test_chart_lengths_and_order(self):
        for lab in LABS:
            r=calc(lab['id'])
            for chart in r['charts']:
                for curve in chart['series']:
                    self.assertEqual(len(curve['x']),len(curve['y']));self.assertTrue(np.all(np.diff(curve['x'])>=0))
    def test_sn2_electrons_charges(self):
        for stage in [0,2]: self.assertEqual(sum(a['charge'] for a in models.geom_sn2(stage)['atoms']),-1)
    def test_sn2_transition_partial_bonds_are_not_stereowedges(self):
        graph=models.geom_sn2(1)
        partial=[b for b in graph['bonds'] if b['b'] in ('nu','br')]
        self.assertEqual(len(partial),2);self.assertTrue(all(b['style']=='dashed' for b in partial))
    def test_sn1_charges_all_stages(self):
        for stage in range(4): self.assertEqual(sum(a['charge'] for a in models.sn1_graph(stage,'tertiary')['atoms']),0)
    def test_sn1_migration_charges_all_stages(self):
        for stage in range(5): self.assertEqual(sum(a['charge'] for a in models.sn1_graph(stage,'rearrange')['atoms']),0)
    def test_sn1_hydride_migration_changes_attachment(self):
        a=models.sn1_graph(1,'rearrange');b=models.sn1_graph(2,'rearrange')
        self.assertIn({'a':'h','b':'c3','order':1},a['bonds']);self.assertIn({'a':'h','b':'c2','order':1},b['bonds'])
    def test_grignard_graph_counterions(self):
        for sub in ['ketone','methanal','co2','epoxide']:
            r=calc('grignard',substrate=sub)
            for graph in r['scene']['frames'][:2]: self.assertEqual(sum(a['charge'] for a in graph['atoms']),0)
    def test_grignard_no_attack_after_quench(self):
        r=calc('grignard',substrate='protic',equivalents=1);self.assertEqual(r['scene']['frames'][0]['arrows'],[])
    def test_radical_arrows_one_electron(self):
        r=calc('radical',mode='peroxide',halogen='hbr')
        for g in r['scene']['frames']:
            for a in g['arrows']: self.assertEqual(a['electrons'],1)
    def test_michael_three_doublet_arrows(self):
        r=calc('carbonyle',reaction='michael',stage=0);self.assertEqual(len(r['scene']['frames'][0]['arrows']),3)
    def test_ester_protonated_carbonyl(self): r=calc('carbonyle',reaction='ester');self.assertEqual(sum(a['charge'] for a in r['scene']['frames'][0]['atoms']),1)

if __name__=='__main__': unittest.main()
