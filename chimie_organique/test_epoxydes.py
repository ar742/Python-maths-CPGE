"""Inventaires, charges et stéréospécificité de la banque époxydes."""
import collections
import itertools
import json
import unittest
import numpy as np
from catalogue_epoxydes import LABS
from modeles_epoxydes import calculate, epoxide, alkene


DEFAULTS = {c['key']: c['value'] for c in LABS[0]['controls']}


def calc(**changes):
    return calculate('epoxydes', {**DEFAULTS, **changes})


def inventory(graph):
    counts = collections.Counter(a['element'] for a in graph['atoms'])
    counts['H'] += sum(a.get('implicit_h', 0) for a in graph['atoms'])
    return {k: v for k, v in counts.items() if v}


def charge(graph):
    return sum(a.get('charge', 0) for a in graph['atoms'])


def neighbor_valence(graph):
    counts = collections.Counter()
    for b in graph['bonds']:
        counts[b['a']] += b['order']
        counts[b['b']] += b['order']
    return {a['id']: counts[a['id']] + a.get('implicit_h', 0) for a in graph['atoms']}


def geometry_configuration(g, center, oxygen):
    # Les substituants ont mêmes priorités dans cette série : O, branche
    # de l'autre carbone, Me, H. Vérifier directement la perspective.
    atoms = {a['id']: a for a in g['atoms']}
    other = 'c2' if center == 'c1' else 'c1'
    groups = [oxygen, other, 'm' + center[1], 'h' + center[1]]
    c = atoms[center]
    vectors = []
    for group in groups:
        a = atoms[group]
        b = next(b for b in g['bonds'] if {b['a'], b['b']} == {center, group})
        z = {'wedge': 1, 'dash': -1}.get(b.get('style'), 0)
        vectors.append(np.array([a['x']-c['x'], a['y']-c['y'], z]))
    p1, p2, p3, p4 = vectors
    sign = np.linalg.det(np.array([p1-p4, p2-p4, p3-p4]))
    return 'R' if sign < 0 else 'S'


class EpoxideFormation(unittest.TestCase):
    def test_each_peracid_reaction_keeps_inventory(self):
        for substrate in ['ethylene', 'propene', 'butene_E', 'butene_Z']:
            r = calc(substrate=substrate)
            first, final = r['scene']['frames']
            self.assertEqual(inventory(first), inventory(final))
            self.assertEqual(charge(first), 0)
            self.assertEqual(charge(final), 0)

    def test_peracid_transfers_exactly_one_oxygen(self):
        for substrate in ['ethylene', 'propene', 'butene_E', 'butene_Z']:
            r = calc(substrate=substrate)
            initial = inventory(alkene(substrate))
            expected = {**initial, 'O': 1}
            self.assertEqual(inventory(r['product']), expected)

    def test_peracid_coproduct_is_acetic_acid(self):
        r = calc(substrate='propene')
        g = r['scene']['frames'][1]
        atoms = [a for a in g['atoms'] if a['id'].startswith('g1_')]
        counts = collections.Counter(a['element'] for a in atoms)
        counts['H'] += sum(a.get('implicit_h', 0) for a in atoms)
        self.assertEqual(counts, collections.Counter(C=2, H=4, O=2))

    def test_E_alkene_gives_trans_epoxide(self):
        r = calc(substrate='butene_E')
        g = r['product']
        styles = [next(b['style'] for b in g['bonds'] if {b['a'], b['b']} == {f'c{i}', f'm{i}'}) for i in [1, 2]]
        self.assertEqual(set(styles), {'wedge', 'dash'})
        self.assertEqual(g['configuration_relation'], 'trans')
        self.assertEqual([geometry_configuration(g, f'c{i}', 'ox') for i in [1, 2]], ['R', 'R'])

    def test_Z_alkene_gives_cis_meso_epoxide(self):
        r = calc(substrate='butene_Z')
        g = r['product']
        styles = [next(b['style'] for b in g['bonds'] if {b['a'], b['b']} == {f'c{i}', f'm{i}'}) for i in [1, 2]]
        self.assertEqual(styles, ['wedge', 'wedge'])
        self.assertEqual([geometry_configuration(g, f'c{i}', 'ox') for i in [1, 2]], ['R', 'S'])
        self.assertEqual(len(r['products']), 1)
        self.assertIn('méso', r['stereo_summary'])

    def test_propene_and_E_butene_have_mirror_products(self):
        for substrate in ['propene', 'butene_E']:
            r = calc(substrate=substrate)
            self.assertEqual(len(r['products']), 2)
            a, b = r['products']
            self.assertEqual(inventory(a), inventory(b))
            for center, config in a['configurations'].items():
                self.assertNotEqual(config, b['configurations'][center])

    def test_silver_ethylene_inventory(self):
        r = calc(mode='silver', substrate='ethylene')
        self.assertTrue(r['allowed'])
        self.assertEqual([inventory(g) for g in r['scene']['frames']], [dict(C=4,H=8,O=2)]*2)
        self.assertIn('2 C2H4', r['equation'])

    def test_silver_other_alkenes_are_not_predicted(self):
        for substrate in ['propene', 'butene_E', 'butene_Z']:
            r = calc(mode='silver', substrate=substrate, stage=3)
            self.assertFalse(r['allowed'])
            self.assertNotIn('product', r)
            self.assertEqual(len(r['scene']['frames']), 1)
            self.assertEqual(inventory(r['scene']['frames'][0]), inventory(alkene(substrate)))

    def test_no_fake_carbocation_in_peracid_bilan(self):
        r = calc(substrate='butene_E')
        self.assertEqual(len(r['scene']['frames']), 2)
        self.assertEqual([charge(g) for g in r['scene']['frames']], [0, 0])


class EpoxideOpening(unittest.TestCase):
    def test_all_opening_states_conserve_atoms_and_charge(self):
        for substrate, mode, nu in itertools.product(['ethylene', 'propene', 'butene_E', 'butene_Z'], ['basic', 'acid'], ['water', 'methoxide']):
            r = calc(substrate=substrate, mode=mode, nucleophile=nu)
            frames = r['scene']['frames']
            expected = inventory(frames[0])
            expected_q = -1 if mode == 'basic' else 1
            for g in frames:
                self.assertEqual(inventory(g), expected, (substrate, mode, nu, g['name']))
                self.assertEqual(charge(g), expected_q, (substrate, mode, nu, g['name']))

    def test_all_states_have_valid_valence_and_oxygen_octet(self):
        for substrate, mode, nu in itertools.product(['ethylene', 'propene', 'butene_E', 'butene_Z'], ['basic', 'acid'], ['water', 'methoxide']):
            r = calc(substrate=substrate, mode=mode, nucleophile=nu)
            for g in r['scene']['frames']:
                v = neighbor_valence(g)
                for a in g['atoms']:
                    if a['element'] == 'C':
                        self.assertEqual(v[a['id']], 4, (g['name'], a))
                    elif a['element'] == 'H':
                        self.assertEqual(v[a['id']], 0 if a['charge'] == 1 else 1, (g['name'], a))
                    elif a['element'] == 'O':
                        expected = 3 if a['charge'] == 1 else 1 if a['charge'] == -1 else 2
                        self.assertEqual(v[a['id']], expected, (g['name'], a))
                        self.assertEqual(2*v[a['id']] + 2*a['lone_pairs'], 8)

    def test_propene_base_attacks_less_substituted_carbon(self):
        for nu in ['water', 'methoxide']:
            r = calc(mode='basic', substrate='propene', nucleophile=nu)
            self.assertEqual(r['attack_carbon'], 'c1')
            self.assertTrue(any({b['a'], b['b']} == {'c1','nu'} for b in r['product']['bonds']))
            self.assertTrue(any({b['a'], b['b']} == {'c2','ox'} for b in r['product']['bonds']))

    def test_propene_acid_attacks_more_substituted_carbon(self):
        for nu in ['water', 'methoxide']:
            r = calc(mode='acid', substrate='propene', nucleophile=nu)
            self.assertEqual(r['attack_carbon'], 'c2')
            self.assertTrue(any({b['a'], b['b']} == {'c2','nu'} for b in r['product']['bonds']))
            self.assertTrue(any({b['a'], b['b']} == {'c1','ox'} for b in r['product']['bonds']))

    def test_acid_protonation_is_explicit_and_oxygen_positive(self):
        r = calc(mode='acid', substrate='propene')
        g = r['scene']['frames'][1]
        ox = next(a for a in g['atoms'] if a['id'] == 'ox')
        self.assertEqual(ox['charge'], 1)
        self.assertTrue(any({b['a'],b['b']} == {'ox','acid_h'} for b in g['bonds']))

    def test_acid_nucleophile_becomes_oxonium_then_neutral(self):
        r = calc(mode='acid', substrate='propene')
        charges = [next(a['charge'] for a in g['atoms'] if a['id']=='nu') for g in r['scene']['frames']]
        self.assertEqual(charges, [0,0,1,0])

    def test_base_epoxide_oxygen_becomes_alkoxide_then_neutral(self):
        r = calc(mode='basic', substrate='propene')
        charges = [next(a['charge'] for a in g['atoms'] if a['id']=='ox') for g in r['scene']['frames']]
        self.assertEqual(charges, [0,-1,0])

    def test_attacked_stereocenter_inverts_other_is_retained(self):
        for substrate, mode, nu in itertools.product(['propene','butene_E','butene_Z'], ['basic','acid'], ['water','methoxide']):
            r = calc(substrate=substrate, mode=mode, nucleophile=nu)
            target = r['attack_carbon']
            for center, before in r['initial_configurations'].items():
                after = geometry_configuration(r['product'], center, 'nu' if center == target else 'ox')
                self.assertEqual(after, ('S' if before=='R' else 'R') if center==target else before)

    def test_product_formulas(self):
        sizes = {'ethylene':(2,4),'propene':(3,6),'butene_E':(4,8),'butene_Z':(4,8)}
        for substrate, mode, nu in itertools.product(sizes, ['basic','acid'], ['water','methoxide']):
            c,h = sizes[substrate]
            methoxy = nu=='methoxide'
            expected = dict(C=c+int(methoxy),H=h+2+2*int(methoxy),O=2)
            r = calc(substrate=substrate, mode=mode, nucleophile=nu)
            self.assertEqual(inventory(r['product']), expected)
            self.assertEqual(charge(r['product']), 0)

    def test_methoxy_regioisomers_are_different(self):
        base = calc(substrate='propene', mode='basic', nucleophile='methoxide')['product']
        acid = calc(substrate='propene', mode='acid', nucleophile='methoxide')['product']
        self.assertEqual(base['name'], '1-méthoxypropan-2-ol')
        self.assertEqual(acid['name'], '2-méthoxypropan-1-ol')
        self.assertNotEqual(base['bonds'], acid['bonds'])

    def test_E_epoxide_water_gives_meso_diol(self):
        r = calc(substrate='butene_E', mode='basic', nucleophile='water')
        self.assertIn('méso', r['stereo_summary'])
        self.assertEqual(r['final_configurations'], {'c1':'S','c2':'R'})

    def test_Z_epoxide_water_gives_racemic_diol(self):
        r = calc(substrate='butene_Z', mode='basic', nucleophile='water')
        self.assertIn('racémique', r['stereo_summary'])
        self.assertEqual(r['final_configurations'], {'c1':'S','c2':'S'})


class PublicContract(unittest.TestCase):
    def test_all_control_combinations_are_finite_json(self):
        for substrate, mode, nu, stage in itertools.product(['ethylene','propene','butene_E','butene_Z'], ['peracid','silver','basic','acid'], ['water','methoxide'], range(4)):
            r = calc(substrate=substrate,mode=mode,nucleophile=nu,stage=stage)
            json.dumps(r, ensure_ascii=False, allow_nan=False)
            self.assertTrue(r['steps'])
            self.assertTrue(r['assumptions'])
            self.assertNotIn('yield', r)
            self.assertNotIn('shares', r)

    def test_graph_endpoints_are_all_valid(self):
        for mode in ['peracid','silver','basic','acid']:
            r = calc(mode=mode,substrate='ethylene')
            for g in r['scene']['frames']:
                ids = [a['id'] for a in g['atoms']]
                self.assertEqual(len(ids), len(set(ids)))
                for b in g['bonds']:
                    self.assertIn(b['a'], ids)
                    self.assertIn(b['b'], ids)

    def test_peracid_graphs_have_ordinary_valence(self):
        for substrate in ['ethylene','propene','butene_E','butene_Z']:
            for g in calc(substrate=substrate)['scene']['frames']:
                v = neighbor_valence(g)
                for a in g['atoms']:
                    self.assertEqual(v[a['id']], {'C':4,'H':1,'O':2}[a['element']])


if __name__ == '__main__':
    unittest.main()
