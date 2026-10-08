"""Conservation et géométries des expériences des pages 531–534."""
import collections
import itertools
import json
import math
import unittest
import numpy as np
from catalogue_exos_recueil import LABS
from modeles_exos_recueil import calculate, aromatic_structure


DEFAULTS = {lab['id']: {c['key']: c['value'] for c in lab['controls']} for lab in LABS}


def calc(lab_id, **changes):
    return calculate(lab_id, {**DEFAULTS[lab_id], **changes})


def inventory(graph):
    counts = collections.Counter(a['element'] for a in graph['atoms'])
    counts['H'] += sum(a.get('implicit_h', 0) for a in graph['atoms'])
    return {k: v for k, v in counts.items() if v}


def charge(graph):
    return sum(a.get('charge', 0) for a in graph['atoms'])


def valences(graph):
    counts = collections.Counter()
    for b in graph['bonds']:
        counts[b['a']] += b['order']
        counts[b['b']] += b['order']
    return {a['id']: counts[a['id']] + a.get('implicit_h', 0) for a in graph['atoms']}


def geometric_ez(graph):
    """Comparer les côtés du C=C portant les substituants prioritaires."""
    db = next(b for b in graph['bonds'] if b['order'] == 2)
    atoms = {a['id']: np.array([a['x'], a['y']]) for a in graph['atoms']}
    priorities = graph['priority_groups']
    a, b = db['a'], db['b']
    axis = atoms[b] - atoms[a]
    def side(center):
        v = atoms[priorities[center]] - atoms[center]
        return axis[0] * v[1] - axis[1] * v[0]
    return 'Z' if side(a) * side(b) > 0 else 'E'


class NitroLewisAndReduction(unittest.TestCase):
    def test_nitro_formula_and_neutrality(self):
        for contributor in ['oxygen_a', 'oxygen_b']:
            r = calc('nitrobenzene', contributor=contributor)
            for g in r['scene']['frames']:
                self.assertEqual(inventory(g), dict(C=6, H=5, N=1, O=2))
                self.assertEqual(charge(g), 0)

    def test_nitrogen_octet_and_oxygen_charges(self):
        r = calc('nitrobenzene')
        for g in r['scene']['frames']:
            v = valences(g)
            n = next(a for a in g['atoms'] if a['element'] == 'N')
            self.assertEqual(v[n['id']], 4)
            self.assertEqual(n['charge'], 1)
            self.assertEqual(n['lone_pairs'], 0)
            oxygens = [a for a in g['atoms'] if a['element'] == 'O']
            self.assertEqual(sorted(a['charge'] for a in oxygens), [-1, 0])
            for a in oxygens:
                self.assertEqual(2 * v[a['id']] + 2 * a['lone_pairs'], 8)

    def test_contributors_keep_all_nuclei(self):
        frames = calc('nitrobenzene')['scene']['frames']
        self.assertEqual([(a['id'], a['element'], a['x'], a['y']) for a in frames[0]['atoms']],
                         [(a['id'], a['element'], a['x'], a['y']) for a in frames[1]['atoms']])
        self.assertNotEqual([b['order'] for b in frames[0]['bonds']],
                            [b['order'] for b in frames[1]['bonds']])

    def test_lewis_arrows_are_doublets(self):
        for g in calc('nitrobenzene')['scene']['frames']:
            self.assertEqual([a['electrons'] for a in g['arrows']], [2, 2])

    def test_reduction_species_atom_inventory(self):
        expected = [dict(C=6, H=5, N=1, O=2), dict(C=6, H=5, N=1, O=1),
                    dict(C=6, H=7, N=1, O=1), dict(C=6, H=7, N=1)]
        frames = calc('nitrobenzene', mode='reduction')['scene']['frames']
        self.assertEqual([inventory(g) for g in frames], expected)
        self.assertEqual([charge(g) for g in frames], [0, 0, 0, 0])

    def test_reduction_species_valences(self):
        for g in calc('nitrobenzene', mode='reduction')['scene']['frames']:
            v = valences(g)
            for a in g['atoms']:
                expected = {'C': 4, 'H': 1, 'N': 4 if a.get('charge') == 1 else 3,
                            'O': 1 if a.get('charge') == -1 else 2}[a['element']]
                self.assertEqual(v[a['id']], expected, (g['name'], a))

    def test_each_half_reaction_conserves_atoms_and_charge(self):
        # Inventaires indépendants des graphes et des chaînes de formule.
        species = {
            'PhNO2': (dict(C=6, H=5, N=1, O=2), 0),
            'PhNO': (dict(C=6, H=5, N=1, O=1), 0),
            'PhNHOH': (dict(C=6, H=7, N=1, O=1), 0),
            'PhNH2': (dict(C=6, H=7, N=1), 0),
            'H2O': (dict(H=2, O=1), 0), 'H+': (dict(H=1), 1), 'e-': ({}, -1),
        }
        def total(side):
            atoms = collections.Counter()
            q = 0
            for name, n in side.items():
                counts, charge_ = species[name]
                atoms.update({element: n * amount for element, amount in counts.items()})
                q += n * charge_
            return atoms, q
        for step in calc('nitrobenzene', mode='reduction')['balances']:
            self.assertEqual(total(step['reactants']), total(step['products']))

    def test_reduction_total_six_electrons_two_waters(self):
        r = calc('nitrobenzene', mode='reduction', stage=3)
        self.assertEqual(r['electron_equivalents'], 6)
        self.assertEqual(r['proton_equivalents'], 6)
        self.assertEqual(r['water_equivalents'], 2)
        self.assertEqual(r['oxidation_number'], -3)

    def test_each_redox_change_is_two(self):
        r = [calc('nitrobenzene', mode='reduction', stage=i) for i in range(4)]
        self.assertEqual([x['oxidation_number'] for x in r], [3, 1, -1, -3])
        self.assertEqual([x['water_equivalents'] for x in r], [0, 1, 1, 2])

    def test_strategy_target_formula_and_positions(self):
        r = calc('nitrobenzene', mode='strategy', stage=3)
        target = r['target']
        self.assertEqual(inventory(target), dict(C=8, H=5, N=1, O=3, Br=1, Cl=1))
        self.assertEqual(target['substituents'], {'0': 'COCH3', '2': 'NO2', '3': 'Br', '4': 'Cl'})
        self.assertEqual(r['target_positions'], {'COCH3': 1, 'Cl': 3, 'Br': 4, 'NO2': 5})
        self.assertEqual(charge(target), 0)

    def test_strategy_bromobenzene_sequence_keeps_graph_atoms_valid(self):
        r = calc('nitrobenzene', mode='strategy', route='bromobenzene', stage=3)
        self.assertTrue(r['allowed'])
        for g in r['scene']['frames']:
            v = valences(g)
            for a in g['atoms']:
                expected = {'C': 4, 'N': 4, 'O': 1 if a.get('charge') == -1 else 2,
                            'Br': 1, 'Cl': 1}[a['element']]
                self.assertEqual(v[a['id']], expected, (g['name'], a))

    def test_friedel_crafts_after_nitro_stays_blocked(self):
        for stage in range(4):
            r = calc('nitrobenzene', mode='strategy', route='nitro_first', stage=stage)
            self.assertFalse(r['allowed'])
            for g in r['scene']['frames']:
                self.assertEqual(inventory(g), dict(C=6, H=5, N=1, O=2))
            self.assertNotIn('yield', r)


class DipoleGeometry(unittest.TestCase):
    def test_recueil_orthometa_para_reference(self):
        for isomer, factor in [('ortho', math.sqrt(3)), ('meta', 1), ('para', 0)]:
            r = calc('dipolesnitro', isomer=isomer, mu0=4.03)
            self.assertAlmostEqual(r['magnitude'], factor * 4.03, places=12)

    def test_orthogonal_component_sum(self):
        for isomer in ['ortho', 'meta', 'para']:
            r = calc('dipolesnitro', isomer=isomer, rotation=35)
            np.testing.assert_allclose(np.sum(r['moments'], axis=0), r['resultant'], atol=1e-14)
            self.assertAlmostEqual(math.hypot(*r['resultant']), r['magnitude'], places=12)

    def test_rotation_preserves_norm(self):
        for isomer, rotation in itertools.product(['ortho', 'meta', 'para'], range(0, 361, 15)):
            a = calc('dipolesnitro', isomer=isomer, rotation=0)
            b = calc('dipolesnitro', isomer=isomer, rotation=rotation)
            self.assertAlmostEqual(a['magnitude'], b['magnitude'], places=12)

    def test_zero_moment_has_no_nan(self):
        for isomer in ['ortho', 'meta', 'para']:
            r = calc('dipolesnitro', isomer=isomer, mu0=0)
            self.assertEqual(r['magnitude'], 0)
            json.dumps(r, allow_nan=False)

    def test_same_group_moment_norm(self):
        r = calc('dipolesnitro', mu0=4.03, rotation=235)
        for v in r['moments']:
            self.assertAlmostEqual(math.hypot(*v), 4.03, places=12)

    def test_group_vectors_remain_aligned_with_the_rotated_molecule(self):
        for isomer, rotation in itertools.product(['ortho', 'meta', 'para'], [0, 35, 90, 235]):
            r = calc('dipolesnitro', isomer=isomer, rotation=rotation)
            atoms = {a['id']: np.array([a['x'], a['y']]) for a in r['scene']['molecule']['atoms']}
            site = {'ortho': 1, 'meta': 2, 'para': 3}[isomer]
            for v, ring_site in zip(r['moments'], [0, site]):
                radial = atoms[f'n{ring_site}'] - atoms[str(ring_site)]
                # Le moment physique de groupe choisi est dirigé vers
                # le cycle : antiparallèle au vecteur cycle→NO₂.
                self.assertAlmostEqual(np.dot(v, radial) / (np.linalg.norm(v) * np.linalg.norm(radial)), -1, places=12)

    def test_dinitro_formula_is_all_isomers(self):
        for isomer in ['ortho', 'meta', 'para']:
            g = calc('dipolesnitro', isomer=isomer)['scene']['molecule']
            self.assertEqual(inventory(g), dict(C=6, H=4, N=2, O=4))
            self.assertEqual(charge(g), 0)

    def test_proportions_are_not_inferred(self):
        for isomer in ['ortho', 'meta', 'para']:
            r = calc('dipolesnitro', isomer=isomer)
            self.assertFalse(any(key in r for key in ['shares', 'proportions', 'yield']))


class E2Conformations(unittest.TestCase):
    def test_all_four_recueil_configurations(self):
        expected = {'SS': 'E', 'RR': 'E', 'SR': 'Z', 'RS': 'Z'}
        for configuration, ez in expected.items():
            r = calc('e2stereo', configuration=configuration, dihedral=180)
            self.assertTrue(r['anti'])
            self.assertEqual(r['product_configuration'], ez)
            self.assertEqual(geometric_ez(r['product']), ez)

    def test_newman_cip_matches_requested_configuration_at_all_angles(self):
        for configuration, phi in itertools.product(['SS', 'RR', 'SR', 'RS'], range(0, 361, 30)):
            r = calc('e2stereo', configuration=configuration, dihedral=phi)
            for vectors, priority, expected in [
                (r['front_vectors'], ['Br', 'C4', 'Et', 'Me'], configuration[0]),
                (r['back_vectors'], ['C3', 'Et', 'Me', 'H'], configuration[1]),
            ]:
                v = [np.array(vectors[key]) for key in priority]
                # Produit mixte : signe négatif = 1→2→3 horaire,
                # lorsque le quatrième substituant est tourné vers l'arrière.
                triple = np.dot(v[0] - v[3], np.cross(v[1] - v[3], v[2] - v[3]))
                self.assertEqual('R' if triple < 0 else 'S', expected)

    def test_nonanti_conformation_does_not_draw_formed_product(self):
        for phi in [0, 60, 120, 240, 300, 360]:
            r = calc('e2stereo', dihedral=phi)
            self.assertFalse(r['anti'])
            self.assertIsNone(r['product'])
            self.assertIsNone(r['scene']['product'])

    def test_anti_br_and_h_have_opposite_radial_directions(self):
        r = calc('e2stereo', dihedral=180)
        front = np.array(r['front_vectors']['Br'])[:2]
        back = np.array(r['back_vectors']['H'])[:2]
        self.assertAlmostEqual(np.dot(front, back), -1, places=12)

    def test_substrate_inventory(self):
        r = calc('e2stereo')
        self.assertEqual(inventory(r['scene']['molecule']), dict(C=8, H=17, Br=1))

    def test_all_regiochemical_products_conserve_carbons(self):
        for configuration, beta in itertools.product(['SS', 'RR', 'SR', 'RS'], ['c4', 'c2', 'methyl']):
            r = calc('e2stereo', configuration=configuration, beta=beta)
            for g in r['possible_products']:
                self.assertEqual(inventory(g), dict(C=8, H=16))
                self.assertTrue(all(v == 4 for v in valences(g).values()))

    def test_c2_has_two_geometries_and_exact_drawings(self):
        r = calc('e2stereo', beta='c2')
        self.assertEqual([geometric_ez(g) for g in r['possible_products']], ['E', 'Z'])
        self.assertEqual(r['scene']['kind'], 'molecules')

    def test_terminal_ch2_has_no_ez_label(self):
        r = calc('e2stereo', beta='methyl')
        self.assertEqual(len(r['possible_products']), 1)
        g = r['possible_products'][0]
        self.assertNotIn('configuration', g)
        self.assertEqual(g['atoms'][0]['label'], 'CH₂')

    def test_other_axes_do_not_use_c3_c4_dihedral_as_gate(self):
        for beta in ['c2', 'methyl']:
            a = calc('e2stereo', beta=beta, dihedral=0)
            b = calc('e2stereo', beta=beta, dihedral=180)
            self.assertEqual(a['possible_products'], b['possible_products'])

    def test_no_invented_product_proportions(self):
        for beta in ['c4', 'c2', 'methyl']:
            r = calc('e2stereo', beta=beta)
            self.assertNotIn('shares', r)
            self.assertNotIn('yield', r)


class PublicContract(unittest.TestCase):
    def test_defaults_presets_and_controls_are_finite_json(self):
        for lab in LABS:
            cases = [DEFAULTS[lab['id']]]
            cases.extend({**DEFAULTS[lab['id']], **p['values']} for p in lab['presets'])
            for control in lab['controls']:
                values = [option['value'] for option in control['options']] if control['type'] == 'select' else [control['min'], control['max']]
                cases.extend({**DEFAULTS[lab['id']], control['key']: value} for value in values)
            for params in cases:
                with self.subTest(lab=lab['id'], params=params):
                    r = calculate(lab['id'], params)
                    json.dumps(r, ensure_ascii=False, allow_nan=False)
                    self.assertTrue(r['steps'])
                    self.assertTrue(r['assumptions'])
                    self.assertIn(r['scene']['kind'], ['mechanism', 'dipoles', 'newman', 'molecules'])

    def test_graph_ids_and_every_bond_endpoint(self):
        for lab_id in DEFAULTS:
            r = calc(lab_id)
            scene = r['scene']
            graphs = scene.get('frames', []) + scene.get('molecules', [])
            if scene.get('molecule'):
                graphs.append(scene['molecule'])
            if scene.get('product'):
                graphs.append(scene['product'])
            for g in graphs:
                ids = [a['id'] for a in g['atoms']]
                self.assertEqual(len(ids), len(set(ids)))
                for b in g['bonds']:
                    self.assertIn(b['a'], ids)
                    self.assertIn(b['b'], ids)


if __name__ == '__main__':
    unittest.main()
