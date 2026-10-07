"""Contrôles scientifiques : bilans, symétries et domaines des modèles."""
import json
import math
import unittest
import numpy as np
from catalogue_analyse import LABS
from commun import clean
from modeles_analyse import calculate, equilibrium_extent, carothers, butane_energy


DEFAULTS={l['id']:{c['key']:c['value'] for c in l['controls']} for l in LABS}
def run(id_,**changes):
    p=dict(DEFAULTS[id_]);p.update(changes);return calculate(id_,p)


class FormuleTests(unittest.TestCase):
    def test_benzene_four_insaturations(self):
        self.assertEqual(run('formule',C=6,H=6,O=0)['ihd'],4)
    def test_oxygen_does_not_change_ihd(self):
        self.assertEqual(run('formule',O=0)['ihd'],run('formule',O=5)['ihd'])
    def test_chlorine_ratio(self):
        r=run('formule',C=6,H=5,O=0,Cl=1)['isotopes'];self.assertAlmostEqual(r[0]['intensity']/r[1]['intensity'],.7576/.2424,12)
        self.assertAlmostEqual(r[1]['position']-r[0]['position'],1.99704992,7)
    def test_two_bromine_binomial(self):
        r=run('formule',C=2,H=4,O=0,Br=2)['isotopes'];self.assertAlmostEqual(sum(p['intensity'] for p in r),1)
        self.assertAlmostEqual(r[1]['intensity'],2*.5069*.4931,12)
    def test_invalid_valence_no_nan(self):
        r=run('formule',C=2,H=10,O=0);self.assertFalse(r['admissible']);json.dumps(clean(r),allow_nan=False)


class StereoTests(unittest.TestCase):
    def test_reference_clockwise_rank4_away(self):
        self.assertEqual(run('stereo',angle=0)['configuration'],'R')
    def test_rotation_preserves_hand(self):
        original=run('stereo',angle=0)
        for angle in (20,90,180,271):
            r=run('stereo',angle=angle);self.assertEqual(r['configuration'],original['configuration']);self.assertAlmostEqual(r['determinant'],original['determinant'],12)
    def test_mirror_changes_hand(self):
        a=run('stereo');b=run('stereo',mirror='mirror');self.assertEqual(b['configuration'],'S');self.assertAlmostEqual(a['determinant'],-b['determinant'])
    def test_racemate_rotation(self):
        r=run('stereo',fraction=.5);self.assertEqual(r['ee'],0);self.assertEqual(r['observed_rotation'],0)
    def test_rotation_not_sign_of_R(self):
        r=run('stereo',fraction=1,alpha=-20,length=2,concentration=.1);self.assertEqual(r['configuration'],'R');self.assertAlmostEqual(r['observed_rotation'],-4)


class ConformerTests(unittest.TestCase):
    def test_four_energy_levels(self):
        np.testing.assert_allclose(butane_energy(np.array([0,60,120,180])),[21,3.8,16,0],atol=1e-12)
    def test_boltzmann_degeneracy(self):
        p=run('conformeres',temperature=298)['populations'];self.assertAlmostEqual(p[1]/p[0],2*math.exp(-3800/(8.31446261815324*298)),12)
    def test_heating_populates_gauche(self):
        self.assertGreater(run('conformeres',temperature=500)['populations'][1],run('conformeres',temperature=200)['populations'][1])
    def test_chair_population(self):
        p=run('conformeres',system='cyclohexane',delta=7.5)['populations'];self.assertGreater(p[0],.95);self.assertAlmostEqual(sum(p),1)
    def test_chair_preserves_up_substituent(self):
        for m in run('conformeres',system='cyclohexane')['scene']['molecules']:
            byid={a['id']:a for a in m['atoms']};self.assertGreater(byid['m']['xyz'][2]-byid['0']['xyz'][2],0)
    def test_chair_tetrahedral_angles(self):
        for m in run('conformeres',system='cyclohexane')['scene']['molecules']:
            a={q['id']:np.array(q['xyz']) for q in m['atoms']};vectors=[a[q]-a['0'] for q in ('1','5','m')]
            for i,j in ((0,1),(0,2),(1,2)):
                self.assertAlmostEqual(float(vectors[i]@vectors[j]/np.linalg.norm(vectors[i])/np.linalg.norm(vectors[j])),-1/3,12)


class IRTests(unittest.TestCase):
    def test_beer_lambert_absorbance(self):
        a=run('ir',concentration=.5);b=run('ir',concentration=1);np.testing.assert_allclose(b['absorbance'],2*a['absorbance'],atol=1e-13)
    def test_transmission_product(self):
        a=run('ir',concentration=.5);b=run('ir',concentration=1);np.testing.assert_allclose(b['transmittance']/100,(a['transmittance']/100)**2,atol=1e-12)
    def test_no_negative_transmission(self):
        for name in ('ethanol','ethanoate','acetone','acide','anisole','benzaldehyde','acetophenone'):
            r=run('ir',molecule=name,concentration=2,path=2);self.assertTrue(np.all((r['transmittance']>0)&(r['transmittance']<=100)))
    def test_conjugation_carbonyl_shift(self):
        unconj=[p['position'] for p in run('ir',molecule='acetone')['bands'] if 'C=O' in p['label']][0]
        conj=[p['position'] for p in run('ir',molecule='acetophenone')['bands'] if 'C=O' in p['label']][0];self.assertLess(conj,unconj)


class NMRTests(unittest.TestCase):
    def test_ester_integrations(self):
        r=run('rmn',molecule='ethanoate');self.assertEqual([s['integral'] for s in r['signals']],[3,3,2]);self.assertAlmostEqual(r['integral'][-1],8,10)
    def test_coupling_hz_unchanged(self):
        for frequency in (60,400,600):
            sig=run('rmn',frequency=frequency)['signals'][0];self.assertAlmostEqual((sig['positions'][1]-sig['positions'][0])*frequency,7.2,10)
    def test_quartet_pascal_weights(self):
        sig=run('rmn')['signals'][2];np.testing.assert_allclose(sig['weights'],np.array([1,3,3,1])/8)
    def test_area_independent_of_linewidth(self):
        a=run('rmn',linewidth=.5);b=run('rmn',linewidth=6);self.assertAlmostEqual(a['integral'][-1],b['integral'][-1],10);self.assertGreater(max(a['intensity']),max(b['intensity']))
    def test_nucleus_symmetry(self):
        r=run('rmn',molecule='acetone',nucleus='C');self.assertEqual(len(r['signals']),2);self.assertEqual(r['total_integral'],3)
    def test_hydroxyl_exchange_no_assumed_n_plus_one(self):
        sig=run('rmn',molecule='ethanol')['signals'][-1];self.assertEqual(sig['J'],0);self.assertEqual(sig['integral'],1)
    def test_weak_field_domain_reduces_ratio(self):
        a=run('rmn',molecule='ethanol',frequency=60,shift_scale=.2);b=run('rmn',molecule='ethanol',frequency=600,shift_scale=.2);self.assertAlmostEqual(b['ratio']/a['ratio'],10)
    def test_high_delta_not_truncated(self):
        r=run('rmn',molecule='acide',shift_scale=1.5);self.assertGreater(r['ppm'][-1],16.8);self.assertAlmostEqual(r['integral'][-1],4,10)


class CCMTests(unittest.TestCase):
    def test_fraction_between_zero_one(self):
        for f in (0,.5,1):self.assertTrue(all(0<value<1 for value in run('ccm',eluent=f)['rf'].values()))
    def test_polar_eluent_migrates_further(self):
        a=run('ccm',eluent=0)['rf'];b=run('ccm',eluent=1)['rf'];self.assertTrue(all(b[k]>a[k] for k in a))
    def test_no_reactant_at_full_conversion(self):
        spots=run('ccm',conversion=1)['spots'];self.assertFalse(any(s['lane']==2 and s['label']=='R' for s in spots));self.assertTrue(any(s['label']=='I' for s in spots))
    def test_longer_front_increases_separation(self):
        self.assertAlmostEqual(run('ccm',front=10)['resolution']/run('ccm',front=5)['resolution'],2)


class ExtractionTests(unittest.TestCase):
    def test_acid_half_neutral_at_pKa(self):
        self.assertAlmostEqual(run('extraction',solute='acid',pH=4.2)['neutral'],.5)
    def test_base_half_neutral_at_pKa(self):
        self.assertAlmostEqual(run('extraction',solute='base',pH=4.6)['neutral'],.5)
    def test_multiple_extractions_improve_fixed_volume(self):
        self.assertGreater(run('extraction',stages=3)['extracted'],run('extraction',stages=1)['extracted'])
    def test_every_stage_mass_balance(self):
        for stage in run('extraction',stages=8)['stages']:self.assertAlmostEqual(stage['aqueous']+stage['organic_collected'],1,12)
    def test_ph_changes_opposite_for_acid_base(self):
        self.assertGreater(run('extraction',solute='acid',pH=2)['extracted'],run('extraction',solute='acid',pH=10)['extracted']);self.assertLess(run('extraction',solute='base',pH=2)['extracted'],run('extraction',solute='base',pH=10)['extracted'])
    def test_layer_position_does_not_change_equilibrium(self):
        self.assertEqual(run('extraction',position='top')['extracted'],run('extraction',position='bottom')['extracted'])


class EsterTests(unittest.TestCase):
    def test_equimolar_K_four_conversion(self):
        self.assertAlmostEqual(run('esterification')['equilibrium_extent'],2/3,12)
    def test_reactant_excess_shifts_equilibrium(self):
        self.assertGreater(run('esterification',second=5)['equilibrium_extent'],run('esterification',second=1)['equilibrium_extent'])
    def test_water_addition_shifts_equilibrium(self):
        self.assertLess(run('esterification',water=2)['equilibrium_extent'],run('esterification',water=0)['equilibrium_extent'])
    def test_forward_reverse_same_state(self):
        x=equilibrium_extent(1,1,0,0,4);back=equilibrium_extent(x,x,1-x,1-x,.25);self.assertAlmostEqual(back,0,12)
    def test_saponification_limited_by_hydroxide(self):
        r=run('esterification',mode='saponification',first=2,second=.4);self.assertAlmostEqual(r['extent'],.4);self.assertEqual(r['labels'][2],'Carboxylate')
    def test_equilibrium_quotient(self):
        r=run('esterification',water=.8,second=2,K=7);a,b,c,d=r['amounts'];self.assertAlmostEqual(c*d/(a*b),7,10)


class AcylTests(unittest.TestCase):
    def test_two_amine_equivalents(self):
        r=run('acylation',amine=2,base=0);self.assertEqual(r['amide'],1);self.assertEqual(r['freeamine'],0)
    def test_external_base_saves_amine(self):
        r=run('acylation',amine=1,base=1);self.assertEqual(r['amide'],1);self.assertEqual(r['freebase'],0)
    def test_one_amine_insufficient_with_full_trapping(self):
        r=run('acylation',amine=1,base=0);self.assertEqual(r['amide'],.5);self.assertEqual(r['acid_trapped'],.5)
    def test_unactivated_acid_no_amide(self):
        self.assertEqual(run('acylation',activation='acid')['amide'],0)
    def test_tetrahedral_carbon_not_pentavalent(self):
        g=run('acylation')['scene']['frames'][1];self.assertEqual(sum(b['order'] for b in g['bonds'] if 'c' in (b['a'],b['b'])),4)
    def test_counterions_preserve_total_charge(self):
        for frame in run('acylation')['scene']['frames']:
            self.assertEqual(sum(a['charge'] for a in frame['atoms']),0)


class StrategyTests(unittest.TestCase):
    def test_protection_good_route(self):
        r=run('protection',route='valid',**{'yield':.8});self.assertTrue(r['viable']);self.assertAlmostEqual(r['global_yield'],.512)
    def test_early_deprotection_wrong(self):
        self.assertFalse(run('protection',route='premature')['viable'])
    def test_proton_incompatibility(self):
        self.assertFalse(run('protection',route='grignard')['viable']);self.assertTrue(run('protection',route='protected_grignard')['viable'])
    def test_chalcone_donor_alpha_h(self):
        r=run('aldol');self.assertFalse(r['blocked']);self.assertEqual(r['donor_alpha_h'],3);self.assertTrue(r['selective'])
    def test_benzaldehyde_not_enolizable(self):
        r=run('aldol',donor='benzaldehyde');self.assertTrue(r['blocked']);self.assertEqual(r['donor_alpha_h'],0)
    def test_crossed_enolizable_needs_control(self):
        self.assertFalse(run('aldol',donor='acetone',acceptor='acetaldehyde',mode='aldol')['selective']);self.assertTrue(run('aldol',donor='acetone',acceptor='acetaldehyde',mode='directed')['selective'])
    def test_michael_restores_carbonyl(self):
        r=run('michaelwittig',reaction='michael',reagent='enolate');self.assertEqual(r['mode'],'1,4');self.assertIn('Carbonyle conservé',r['frames'][-1]['name'])
    def test_wittig_no_universal_ratio(self):
        r=run('michaelwittig',reaction='wittig',reagent='stabilized');self.assertIn('E favorisé',r['mode']);self.assertNotIn('E_fraction',r)
    def test_incompatible_selector_pair_flagged(self):
        self.assertFalse(run('michaelwittig',reaction='wittig',reagent='cuprate')['valid'])
    def test_aldol_charge_on_oxygen(self):
        frame=run('aldol')['frames'][2];negative=[a for a in frame['atoms'] if a['charge']==-1]
        self.assertEqual(len(negative),1);self.assertEqual(negative[0]['element'],'O')
    def test_michael_enolate_oxygen_and_moved_pi(self):
        frame=run('michaelwittig',reaction='michael',reagent='enolate')['frames'][2]
        self.assertEqual(next(a['charge'] for a in frame['atoms'] if a['id']=='o'),-1)
        self.assertEqual(next(b['order'] for b in frame['bonds'] if b['a']=='c' and b['b']=='a'),2)
    def test_wittig_ylure_and_oxide_actual_phosphorus(self):
        frames=run('michaelwittig',reaction='wittig',reagent='stabilized')['frames'];p=next(a for a in frames[1]['atoms'] if a['element']=='P');self.assertEqual(p['charge'],1)
        final=frames[-1];phosphorus=next(a for a in final['atoms'] if a['element']=='P');oxygen=next(a for a in final['atoms'] if a['element']=='O')
        self.assertTrue(any(b['order']==2 and {b['a'],b['b']}=={phosphorus['id'],oxygen['id']} for b in final['bonds']))
    def test_protection_active_structure_matches_stage(self):
        for stage in range(4):
            r=run('protection',stage=stage)
            self.assertEqual(r['scene']['molecule'],r['molecules'][stage]);self.assertEqual(r['scene']['nodes'][stage]['molecule'],r['molecules'][stage])


class DielsTests(unittest.TestCase):
    def test_s_trans_acyclic_requires_conversion(self):
        self.assertFalse(run('dielsalder',diene='butadiene',conformation='trans')['accessible'])
    def test_locked_diene_available(self):
        self.assertTrue(run('dielsalder',diene='cyclopentadiene',conformation='trans')['accessible'])
    def test_endo_model_can_reverse(self):
        self.assertGreater(run('dielsalder',barrier_difference=3)['endo'],.5);self.assertLess(run('dielsalder',barrier_difference=-3)['endo'],.5)
    def test_kinetic_equilibrium_are_independent(self):
        self.assertGreater(run('dielsalder',regime='kinetic',barrier_difference=3,energy_difference=3)['endo'],.5);self.assertLess(run('dielsalder',regime='equilibrium',barrier_difference=3,energy_difference=3)['endo'],.5)
    def test_dienophile_relation_preserved(self):
        cis=run('dielsalder',dienophile='maleate')['product'];trans=run('dielsalder',dienophile='fumarate')['product']
        self.assertEqual(next(b['style'] for b in cis['bonds'] if b['b']=='s5'),'wedge');self.assertEqual(next(b['style'] for b in trans['bonds'] if b['b']=='s5'),'dash')
    def test_bicyclic_graph_bridge_positions(self):
        prod=run('dielsalder')['product'];self.assertEqual({b['a'] for b in prod['bonds'] if b['b']=='bridge'},{'0','3'})
    def test_s_trans_drawing_has_ends_on_opposite_sides(self):
        graph=run('dielsalder',diene='butadiene',conformation='trans')['scene']['molecules'][0]
        a={atom['id']:atom for atom in graph['atoms']};self.assertLess((a['1']['x']-a['2']['x'])*(a['4']['x']-a['3']['x']),0)
    def test_cyclopentadiene_hydrogens(self):
        graph=run('dielsalder')['scene']['molecules'][0];self.assertEqual(sum(a['label']=='CH' for a in graph['atoms']),4);self.assertEqual(sum(a['label']=='CH₂' for a in graph['atoms']),1)
    def test_dienophile_geometry(self):
        for name,expected in [('maleate',1),('fumarate',-1)]:
            graph=run('dielsalder',dienophile=name)['scene']['molecules'][1];a={q['id']:q for q in graph['atoms']}
            self.assertEqual(math.copysign(1,a['sl']['y']*a['sr']['y']),expected)
    def test_no_all_endo_exo_ratio_for_trans_or_acyclic(self):
        self.assertIsNone(run('dielsalder',dienophile='fumarate')['endo']);self.assertIsNone(run('dielsalder',diene='butadiene')['endo'])


class RetroPolymerTests(unittest.TestCase):
    def test_yields_multiply(self):
        r=run('retrosynthese',target='aromatic',route='short',**{'yield':.8});self.assertEqual(r['operations'],2);self.assertAlmostEqual(r['global_yield'],.64)
    def test_mass_amount_conversion(self):
        r=run('retrosynthese',target='aspirin',scale=10,**{'yield':.8});self.assertAlmostEqual(r['mass'],.008*180.16)
    def test_no_friedel_crafts_on_nitrobenzene_route(self):
        self.assertFalse(run('retrosynthese',target='aromatic',route='wrong')['viable'])
    def test_atom_economy_distinct_from_yield(self):
        a=run('retrosynthese',target='aspirin',**{'yield':.6});b=run('retrosynthese',target='aspirin',**{'yield':.9});self.assertEqual(a['atom_economy'],b['atom_economy']);self.assertLess(a['atom_economy'],1)
    def test_carothers_balanced(self):
        self.assertAlmostEqual(run('polymeres',conversion=.95,ratio=1)['DP'],20)
    def test_carothers_stoich_upper_limit(self):
        self.assertAlmostEqual(carothers(1,.9),19);self.assertLess(run('polymeres',conversion=.999,ratio=.9)['DP'],19)
    def test_bond_count_molecules_decrease(self):
        r=run('polymeres',conversion=.8,ratio=.9);self.assertAlmostEqual(r['initial']-r['bonds'],r['chains']);self.assertAlmostEqual(r['initial']/r['chains'],r['DP'])
    def test_chain_count_controls_DP(self):
        a=run('polymeres',mode='chain',chains=.2);b=run('polymeres',mode='chain',chains=.4);self.assertAlmostEqual(a['DP'],2*b['DP'])
    def test_polyethylene_atom_economy(self):
        self.assertEqual(run('polymeres',mode='chain')['atom_economy'],1);self.assertLess(run('polymeres',mode='step')['atom_economy'],1)
    def test_chain_count_incompatible_flag(self):
        self.assertFalse(run('polymeres',mode='chain',monomers=1,conversion=.1,chains=2)['valid'])
    def test_target_graph_molecular_formula(self):
        # Independent valence count: atomized targets must have their known formulas.
        expected={'aspirin':{'C':9,'H':8,'O':4},'paracetamol':{'C':8,'H':9,'N':1,'O':2},'chalcone':{'C':15,'H':12,'O':1},'alcohol':{'C':8,'H':10,'O':1},'aromatic':{'C':8,'H':7,'N':1,'O':3}}
        for target,formula in expected.items():
            graph=run('retrosynthese',target=target)['scene']['molecule'];counts={};valences={a['id']:0 for a in graph['atoms']}
            for b in graph['bonds']:valences[b['a']]+=b['order'];valences[b['b']]+=b['order']
            hydrogens=0
            for a in graph['atoms']:
                counts[a['element']]=counts.get(a['element'],0)+1
                valence={'C':4,'O':1 if a['charge']==-1 else 2,'N':4 if a['charge']==1 else 3}[a['element']]
                self.assertLessEqual(valences[a['id']],valence)
                hydrogens+=valence-valences[a['id']]
            counts['H']=hydrogens
            self.assertEqual(counts,formula,target)
    def test_para_and_meta_target_substitution(self):
        para=run('retrosynthese',target='paracetamol')['scene']['molecule'];meta=run('retrosynthese',target='aromatic')['scene']['molecule']
        self.assertTrue(any(b['a']=='3' and b['b']=='oh' for b in para['bonds']))
        self.assertTrue(any(b['a']=='2' and b['b']=='n' for b in meta['bonds']))


class PublicDomainTests(unittest.TestCase):
    def test_all_presets_finite(self):
        for l in LABS:
            for pre in l['presets']:
                with self.subTest(lab=l['id'],preset=pre['label']):
                    params=dict(DEFAULTS[l['id']]);params.update(pre['values']);json.dumps(clean(calculate(l['id'],params)),allow_nan=False)
    def test_each_control_endpoint_finite(self):
        for l in LABS:
            for control in l['controls']:
                values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                for value in values:
                    with self.subTest(lab=l['id'],control=control['key'],value=value):
                        params=dict(DEFAULTS[l['id']]);params[control['key']]=value;json.dumps(clean(calculate(l['id'],params)),allow_nan=False)


if __name__=='__main__': unittest.main()
