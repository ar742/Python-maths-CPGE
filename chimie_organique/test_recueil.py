"""Contrôles indépendants de structures, bilans atomiques et choix de mécanisme."""
import itertools
import json
import math
import re
import unittest
from collections import Counter
import numpy as np
from catalogue_recueil import LABS
from commun import clean
import modeles_recueil as models

DEFAULTS={lab['id']:{c['key']:c['value'] for c in lab['controls']} for lab in LABS}


def calc(id_,**changes):
    return models.calculate(id_,{**DEFAULTS[id_],**changes})


def atoms_in_formula(formula):
    # Recalcul dans les tests : aucun indicateur de conservation fourni par
    # le modèle n'est utilisé pour valider les espèces de ses équations.
    result=Counter()
    for element,number in re.findall(r'([A-Z][a-z]?)(\d*)',formula):
        result[element]+=int(number or '1')
    return result


SUBS=str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789')


def label_formula(label):
    label=label.translate(SUBS)
    if label=='NEt3':return 'C6H15N'
    if label=='HNEt3':return 'C6H16N'
    if label=='C(CH3)3':return 'C4H9'
    return label.replace('Et','C2H5').replace('Ph','C6H5').replace('tBu','C4H9')


def graph_inventory(graph):
    counts=Counter()
    for a in graph['atoms']:
        counts.update(atoms_in_formula(label_formula(a['label'])))
    return counts,sum(a.get('charge',0) for a in graph['atoms'])


class ConservationTests(unittest.TestCase):
    def assertBalanced(self,equation):
        totals=[];charges=[]
        for side in ['reactants','products']:
            counts=Counter();charge=0
            for s in equation[side]:
                for element,n in atoms_in_formula(s['formula']).items():
                    counts[element]+=s['coefficient']*n
                charge+=s['coefficient']*s['charge']
            totals.append(counts);charges.append(charge)
        self.assertEqual(totals[0],totals[1]);self.assertEqual(charges[0],charges[1])

    def test_equations_all_selected_reactions(self):
        for lab in LABS:
            base=DEFAULTS[lab['id']]
            choices=[]
            for c in lab['controls']:
                choices.append([(c['key'],o['value']) for o in c['options']] if c['type']=='select' else [(c['key'],c['value'])])
            for values in itertools.product(*choices):
                with self.subTest(lab=lab['id'],params=dict(values)):
                    r=calc(lab['id'],**dict(values))
                    for key in ['reaction','insertion_reaction','quench_reaction']:
                        if key in r:self.assertBalanced(r[key])

    def test_e1_atomic_inventory_in_each_frame(self):
        for substrate in ['secondary','tertiary','primary']:
            for f in calc('e1',substrate=substrate)['scene']['frames']:
                with self.subTest(substrate=substrate,frame=f['name']):
                    counts,charge=graph_inventory(f)
                    self.assertEqual(counts,Counter(C=5,H=15,O=2));self.assertEqual(charge,1)

    def test_e1_source_halogen_and_beta_hydrogen_inventory_in_each_frame(self):
        for f in calc('e1',substrate='source')['scene']['frames']:
            self.assertEqual(graph_inventory(f),(Counter(C=5,H=13,Cl=1,O=1),0))

    def test_enolate_atomic_inventory_in_each_frame(self):
        for donor,rx,site in itertools.product(['acetone','malonate'],['methyl','ethyl','tertbutyl'],['C','O']):
            frames=calc('enolatealkyl',donor=donor,electrophile=rx,site=site)['scene']['frames']
            initial=graph_inventory(frames[0])
            for f in frames:
                with self.subTest(donor=donor,rx=rx,site=site,frame=f['name']):
                    self.assertEqual(graph_inventory(f),initial)
                    self.assertEqual(graph_inventory(f)[1],-1)

    def test_ammonium_atomic_inventory_in_each_frame(self):
        for amine,rx in itertools.product(['trimethyl','triethyl'],['methyl','benzyl']):
            frames=calc('aminealkyl',amine=amine,electrophile=rx)['scene']['frames']
            initial=graph_inventory(frames[0])
            for f in frames:self.assertEqual(graph_inventory(f),initial)
            self.assertEqual(initial[1],0)

    def test_anhydride_atomic_inventory_in_each_frame(self):
        for acyl,v,trap in itertools.product(['acetyl','benzoyl'],['formation','chloridealcohol','hydrolysis','alcoholysis','amidation'],['secondamine','external']):
            frames=calc('anhydride',acyl=acyl,variant=v,acidtrap=trap)['scene']['frames']
            initial=graph_inventory(frames[0])
            for f in frames:
                with self.subTest(acyl=acyl,variant=v,trap=trap,frame=f['name']):
                    self.assertEqual(graph_inventory(f),initial)

    def test_hydrolysis_atomic_inventory_in_each_frame(self):
        for derivative,medium in itertools.product(['chloride','ester','amide'],['acid','base']):
            frames=calc('hydrolyseacyle',derivative=derivative,medium=medium)['scene']['frames']
            initial=graph_inventory(frames[0])
            for f in frames:
                with self.subTest(derivative=derivative,medium=medium,frame=f['name']):
                    self.assertEqual(graph_inventory(f),initial)

    def test_photoaddition_hydrogens_retained(self):
        f=calc('photochlore',mode='addition',chlorine=3)['scene']['frames'][-1]
        self.assertEqual(graph_inventory(f),(Counter(C=6,H=6,Cl=6),0))
        self.assertEqual(sum(b['order']==2 for b in f['bonds']),0)

    def test_sea_hydrogen_goes_to_hcl(self):
        f=calc('photochlore',mode='sea',chlorine=1)['scene']['frames'][-1]
        self.assertEqual(graph_inventory(f),(Counter(C=6,H=6,Cl=2),0))
        self.assertEqual(sum(b['order']==2 for b in f['bonds']),3)
        self.assertTrue(any(b['a']=='h' and b['b']=='clh' for b in f['bonds']))

    def test_grignard_mixture_conserves_atoms_at_all_limits(self):
        for group,halide,mg,water,progress in itertools.product(['ethyl','phenyl'],['Br','Cl'],[0,.4,1,2],[0,.3,1,2],[0,.4,1]):
            r=calc('grignardprep',group=group,halide=halide,magnesium=mg,water=water,progress=progress)
            initial=Counter();final=Counter()
            for row in r['inventory']:
                self.assertGreaterEqual(row['final'],-1e-12)
                for element,n in atoms_in_formula(row['formula']).items():
                    initial[element]+=row['initial']*n;final[element]+=row['final']*n
            with self.subTest(group=group,halide=halide,mg=mg,water=water,p=progress):
                self.assertEqual(initial.keys(),final.keys())
                for element in initial:self.assertAlmostEqual(initial[element],final[element])


class EffectsTests(unittest.TestCase):
    def test_chlorine_induction_and_mesomeric_signs_differ(self):
        r=calc('effets',group='chloro',system='mesomeric')
        self.assertEqual(r['inductive'],'−I');self.assertEqual(r['mesomeric'],'+M');self.assertEqual(r['orientation'],'ortho/para')

    def test_donor_contributor_moves_negative_charge_ortho_para(self):
        for group in ['methoxy','chloro']:
            fs=calc('effets',group=group,system='mesomeric')['scene']['frames']
            self.assertEqual(next(a for a in fs[1]['atoms'] if a['id']=='r1')['charge'],-1)
            self.assertEqual(next(a for a in fs[2]['atoms'] if a['id']=='r3')['charge'],-1)
            for f in fs:self.assertEqual(sum(a['charge'] for a in f['atoms']),0)

    def test_nitro_preserves_octet_with_two_negative_oxygens(self):
        r=calc('effets',group='nitro',system='mesomeric')
        self.assertEqual(r['orientation'],'méta')
        for f in r['scene']['frames'][1:]:
            self.assertEqual(sum(b['order'] for b in f['bonds'] if 'n' in (b['a'],b['b'])),4)
            self.assertEqual([a['charge'] for a in f['atoms'] if a['element']=='O'],[-1,-1])
            self.assertEqual(sum(a['charge'] for a in f['atoms']),0)

    def test_mesomeric_contributors_preserve_nuclei(self):
        for group in ['alkyl','methoxy','chloro','nitro']:
            frames=calc('effets',group=group,system='mesomeric')['scene']['frames']
            first=graph_inventory(frames[0])
            for f in frames:self.assertEqual(graph_inventory(f),first)

    def test_markovnikov_conditions_change_function_and_position(self):
        acid=calc('effets',system='markovnikov',conditions='ordinary')
        borane=calc('effets',system='markovnikov',conditions='alternative')
        self.assertEqual(acid['product_name'],'2-bromobutane');self.assertTrue(acid['carbocation'])
        self.assertEqual(borane['product_name'],'butan-1-ol');self.assertFalse(borane['carbocation'])
        final=borane['scene']['frames'][-1]
        self.assertTrue(any({b['a'],b['b']}=={'c0','b'} for b in final['bonds']))

    def test_markovnikov_addition_conserves_hbr_and_charge_in_each_image(self):
        for f in calc('effets',system='markovnikov',conditions='ordinary')['scene']['frames']:
            self.assertEqual(graph_inventory(f),(Counter(C=4,H=9,Br=1),0))

    def test_zaitsev_alternative_changes_leaving_group_and_mechanism(self):
        acid=calc('effets',system='zaitsev',conditions='ordinary')
        base=calc('effets',system='zaitsev',conditions='alternative')
        self.assertEqual(acid['mechanism'],'E1');self.assertEqual(base['mechanism'],'E2')
        self.assertTrue(any(a['element']=='Br' for a in base['scene']['frames'][0]['atoms']))
        self.assertTrue(any(b['order']==2 and b['a']=='0' and b['b']=='1' for b in base['scene']['frames'][-1]['bonds']))


class E1Tests(unittest.TestCase):
    def test_first_order_half_life(self):
        r=calc('e1',k_ion=.02,time=math.log(2)/.02)
        self.assertAlmostEqual(r['remaining'][-1],.5)

    def test_both_branches_plus_alcohol_equal_one(self):
        for z in [0,30,80,100]:
            r=calc('e1',branch_z=z)
            np.testing.assert_allclose(r['remaining']+r['product_z']+r['product_h'],1)

    def test_branch_ratio_is_selected_data(self):
        r=calc('e1',branch_z=75)
        self.assertAlmostEqual(r['product_z'][-1]/r['product_h'][-1],3)

    def test_primary_does_not_invent_carbocation(self):
        r=calc('e1',substrate='primary',k_ion=.2)
        self.assertFalse(r['allowed']);np.testing.assert_allclose(r['remaining'],1)
        self.assertEqual(len(r['scene']['frames']),1)

    def test_rate_change_affects_extent_not_selected_branch_ratio(self):
        low=calc('e1',k_ion=.005);high=calc('e1',k_ion=.1)
        self.assertGreater(high['total_alkene'][-1],low['total_alkene'][-1])
        self.assertAlmostEqual(low['product_z'][-1]/low['total_alkene'][-1],.8)

    def test_water_departure_is_separate_from_beta_deprotonation(self):
        fs=calc('e1',substrate='secondary')['scene']['frames']
        self.assertTrue(any({b['a'],b['b']}=={'c1','o'} for b in fs[1]['bonds']))
        self.assertFalse(any({b['a'],b['b']}=={'c1','o'} for b in fs[2]['bonds']))
        self.assertFalse(any(b['order']==2 for b in fs[2]['bonds']))
        self.assertTrue(any(b['order']==2 for b in fs[3]['bonds']))

    def test_transferred_proton_is_bound_to_only_one_oxygen_in_each_frame(self):
        fs=calc('e1',substrate='secondary')['scene']['frames']
        for i,f in enumerate(fs):
            attached=[b for b in f['bonds'] if 'ha' in (b['a'],b['b'])]
            self.assertEqual(len(attached),1)
            self.assertIn('w' if i==0 else 'o',(attached[0]['a'],attached[0]['b']))

    def test_source_e1_is_direct_secondary_cation_without_hidden_migration(self):
        r=calc('e1',substrate='source')
        fs=r['scene']['frames']
        self.assertEqual(next(a for a in fs[1]['atoms'] if a['id']=='c1')['charge'],1)
        self.assertEqual(next(a for a in fs[1]['atoms'] if a['id']=='c2')['charge'],0)
        self.assertIn('3-méthylbut-1-ène',r['charts'][0]['series'][2]['label'])
        self.assertFalse(any({b['a'],b['b']}=={'c1','cl'} for b in fs[1]['bonds']))


class EnolateAndAmineTests(unittest.TestCase):
    def test_c_and_o_alkylation_are_different_connectivities(self):
        c=calc('enolatealkyl',site='C')['scene']['frames'][-1]
        o=calc('enolatealkyl',site='O')['scene']['frames'][-1]
        self.assertTrue(any({b['a'],b['b']}=={'alpha','e'} for b in c['bonds']))
        self.assertTrue(any({b['a'],b['b']}=={'o','e'} for b in o['bonds']))
        self.assertTrue(any({b['a'],b['b']}=={'alpha','acyl'} and b['order']==2 for b in o['bonds']))

    def test_acetone_methylation_gives_butanone_formula(self):
        r=calc('enolatealkyl',donor='acetone',electrophile='methyl',site='C')
        self.assertEqual(r['product_name'],'butan-2-one');self.assertEqual(r['product_formula'],'C4H8O')

    def test_tertiary_electrophile_is_not_sn2(self):
        r=calc('enolatealkyl',electrophile='tertbutyl',equivalents=2)
        self.assertFalse(r['allowed']);self.assertEqual(r['extent'],0)
        self.assertEqual(len(r['scene']['frames']),2)

    def test_enolate_rx_limiting(self):
        self.assertAlmostEqual(calc('enolatealkyl',equivalents=.4)['extent'],.4)
        self.assertEqual(calc('enolatealkyl',equivalents=2)['extent'],1)

    def test_quaternary_n_has_four_actual_bonds_and_counterion(self):
        f=calc('aminealkyl')['scene']['frames'][-1]
        self.assertEqual(sum('n' in (b['a'],b['b']) for b in f['bonds']),4)
        self.assertEqual(next(a for a in f['atoms'] if a['id']=='n')['charge'],1)
        self.assertEqual(next(a for a in f['atoms'] if a['id']=='br')['charge'],-1)
        self.assertFalse(any('br' in (b['a'],b['b']) for b in f['bonds']))

    def test_ammonium_equivalents_saturate_at_one(self):
        self.assertAlmostEqual(calc('aminealkyl',equivalents=.3)['extent'],.3)
        self.assertEqual(calc('aminealkyl',equivalents=3)['extent'],1)

    def test_tetramethylammonium_formula(self):
        self.assertEqual(calc('aminealkyl',amine='trimethyl',electrophile='methyl')['product_formula'],'C4H12N')


class AcylTests(unittest.TestCase):
    def test_anhydride_bridge_is_an_actual_oxygen_link(self):
        f=calc('anhydride',variant='formation')['scene']['frames'][-1]
        self.assertTrue(any({b['a'],b['b']}=={'ac','bz'} for b in f['bonds']))
        self.assertTrue(any({b['a'],b['b']}=={'bc','bz'} for b in f['bonds']))
        self.assertFalse(any({b['a'],b['b']}=={'ac','az'} for b in f['bonds']))

    def test_tetrahedral_carbon_has_four_single_bonds(self):
        for variant in ['formation','chloridealcohol','hydrolysis','alcoholysis','amidation']:
            f=calc('anhydride',variant=variant)['scene']['frames'][1]
            incident=[b for b in f['bonds'] if 'ac' in (b['a'],b['b'])]
            self.assertEqual(len(incident),4)
            self.assertTrue(all(b['order']==1 for b in incident))

    def test_second_amine_changes_neutralized_bilan(self):
        second=calc('anhydride',variant='amidation',equivalents=1,acidtrap='secondamine')
        external=calc('anhydride',variant='amidation',equivalents=1,acidtrap='external')
        self.assertEqual(second['required_nucleophile'],2);self.assertEqual(second['extent'],.5)
        self.assertEqual(external['required_nucleophile'],1);self.assertEqual(external['extent'],1)
        self.assertIn('C6H16N',[s['formula'] for s in external['reaction']['products']])

    def test_anhydride_hydrolysis_produces_two_acids(self):
        r=calc('anhydride',variant='hydrolysis',acyl='benzoyl')
        self.assertEqual(r['reaction']['products'][0]['coefficient'],2)
        self.assertEqual(r['reaction']['products'][0]['formula'],'C7H6O2')

    def test_chloride_alcoholysis_is_distinct_from_anhydride(self):
        c=calc('anhydride',variant='chloridealcohol',acyl='benzoyl')
        a=calc('anhydride',variant='alcoholysis',acyl='benzoyl')
        self.assertIn('HCl',[s['formula'] for s in c['reaction']['products']])
        self.assertIn('C7H6O2',[s['formula'] for s in a['reaction']['products']])
        self.assertEqual(c['reaction']['products'][0]['formula'],'C9H10O2')

    def test_hydrolysis_base_is_carboxylate_acid_is_carboxylic_acid(self):
        for derivative in ['chloride','ester','amide']:
            base=calc('hydrolyseacyle',derivative=derivative,medium='base')
            acid=calc('hydrolyseacyle',derivative=derivative,medium='acid')
            self.assertEqual(base['reaction']['products'][0]['formula'],'C2H3O2')
            self.assertEqual(base['reaction']['products'][0]['charge'],-1)
            self.assertEqual(acid['reaction']['products'][0]['formula'],'C2H4O2')
            self.assertEqual(acid['reaction']['products'][0]['charge'],0)

    def test_chloride_neutralized_hydrolysis_consumes_two_hydroxides(self):
        r=calc('hydrolyseacyle',derivative='chloride',medium='base',equivalents=1)
        self.assertEqual(r['required_nucleophile'],2);self.assertEqual(r['extent_limit'],.5)

    def test_acid_amide_traps_one_proton_as_ammonium(self):
        r=calc('hydrolyseacyle',derivative='amide',medium='acid')
        self.assertIn(('H',1),[(s['formula'],s['charge']) for s in r['reaction']['reactants']])
        self.assertIn(('H4N',1),[(s['formula'],s['charge']) for s in r['reaction']['products']])

    def test_amide_reactivity_is_not_chloride(self):
        amide=calc('hydrolyseacyle',derivative='amide')
        chloride=calc('hydrolyseacyle',derivative='chloride')
        self.assertNotEqual(amide['reactivity'],chloride['reactivity'])
        self.assertIn('chauffage',amide['reactivity'])


class LightAndGrignardTests(unittest.TestCase):
    def test_photoaddition_requires_three_chlorines(self):
        self.assertAlmostEqual(calc('photochlore',chlorine=1)['extent'],1/3)
        self.assertEqual(calc('photochlore',chlorine=3)['extent'],1)

    def test_photoaddition_off_has_zero_extent(self):
        r=calc('photochlore',light='off',chlorine=4)
        self.assertFalse(r['active']);self.assertEqual(r['extent'],0)
        self.assertEqual(sum(b['order']==2 for b in r['scene']['frames'][-1]['bonds']),3)

    def test_sea_reacts_without_photons_in_its_defined_catalytic_mode(self):
        r=calc('photochlore',mode='sea',light='off',chlorine=1)
        self.assertTrue(r['active']);self.assertEqual(r['extent'],1);self.assertTrue(r['aromatic_product'])

    def test_no_lindane_stereoisomer_is_assigned(self):
        f=calc('photochlore')['scene']['frames'][-1]
        self.assertFalse(any(b.get('style') in ('wedge','dash') for b in f['bonds']))
        self.assertIn('non distingués',f['name'])

    def test_grignard_water_consumes_before_synthetic_use(self):
        r=calc('grignardprep',magnesium=1,water=.6,progress=1)
        self.assertEqual(r['formed'],1);self.assertEqual(r['destroyed'],.6);self.assertAlmostEqual(r['available'],.4)

    def test_grignard_magnesium_limits_formation(self):
        r=calc('grignardprep',magnesium=.3,water=0,progress=1)
        self.assertEqual(r['formed'],.3);self.assertEqual(r['available'],.3);self.assertAlmostEqual(r['remaining_rx'],.7)

    def test_grignard_excess_water_does_not_make_negative_reagent(self):
        r=calc('grignardprep',water=2)
        self.assertEqual(r['available'],0);self.assertEqual(r['destroyed'],1);self.assertEqual(r['remaining_water'],1)

    def test_grignard_progress_is_extent_not_fictitious_time(self):
        r=calc('grignardprep',magnesium=.5,progress=.4,water=.1)
        self.assertAlmostEqual(r['formed'],.2);self.assertAlmostEqual(r['available'],.1)

    def test_grignard_zero_insertion_has_no_rmgx_in_final_picture(self):
        r=calc('grignardprep',progress=0)
        final=r['scene']['frames'][-1]
        self.assertFalse(any({b['a'],b['b']}=={'r0','mg'} for b in final['bonds']))
        self.assertEqual(r['available'],0)

    def test_grignard_dry_picture_has_no_water_or_proton_transfer_arrow(self):
        f=calc('grignardprep',water=0)['scene']['frames'][1]
        self.assertFalse(any(a['id']=='water' for a in f['atoms']));self.assertFalse(f['arrows'])

    def test_grignard_contamination_arrow_starts_from_carbon_magnesium_bond(self):
        f=calc('grignardprep',water=.3,group='ethyl')['scene']['frames'][1]
        start=f['arrows'][0]['start'];end=f['arrows'][0]['end']
        self.assertAlmostEqual(start[0],.55);self.assertAlmostEqual(end[0],.4)
        self.assertEqual(end[1],-1.6)


class PublicDataTests(unittest.TestCase):
    def test_defaults_presets_boundaries_and_each_choice_are_finite(self):
        for lab in LABS:
            cases=[DEFAULTS[lab['id']]]+[dict(DEFAULTS[lab['id']],**p['values']) for p in lab['presets']]
            for control in lab['controls']:
                values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                cases += [dict(DEFAULTS[lab['id']],**{control['key']:v}) for v in values]
            for p in cases:
                with self.subTest(lab=lab['id'],params=p):
                    r=clean(models.calculate(lab['id'],p));json.dumps(r,allow_nan=False)
                    self.assertTrue(r['metrics']);self.assertTrue(r['steps']);self.assertTrue(r['assumptions'])
                    for chart in r['charts']:
                        for curve in chart['series']:self.assertEqual(len(curve['x']),len(curve['y']))

    def test_all_graph_edges_and_arrows_are_defined(self):
        for lab in LABS:
            for changes in [dict()]+[p['values'] for p in lab['presets']]:
                r=calc(lab['id'],**changes)
                for f in r['scene'].get('frames',[]):
                    ids=[a['id'] for a in f['atoms']]
                    self.assertEqual(len(ids),len(set(ids)))
                    for b in f['bonds']:
                        self.assertIn(b['a'],ids);self.assertIn(b['b'],ids)
                        self.assertNotEqual(b['a'],b['b']);self.assertIn(b['order'],[1,2,3])
                    for curve in f.get('arrows',[]):
                        for key in ['start','end','control']:self.assertEqual(len(curve[key]),2)
                        self.assertEqual(curve['electrons'],2)


if __name__=='__main__':unittest.main()
