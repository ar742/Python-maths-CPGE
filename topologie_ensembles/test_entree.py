"""Vérifier les expériences proposées et la validation de l’entrée publique."""
import copy
import json
import math
import unittest
from catalogue import LABS, LAB_BY_ID
from modeles import calculate


class EntreeTests(unittest.TestCase):
    @staticmethod
    def defaults(lab):
        return {control['key']: control['value'] for control in lab['controls']}

    def check_result(self, result, lab_id):
        json.dumps(result, ensure_ascii=False, allow_nan=False)
        self.assertEqual(result['lab'], lab_id)
        self.assertEqual(set(result['params']), {c['key'] for c in LAB_BY_ID[lab_id]['controls']})
        for key in ('metrics', 'steps', 'assumptions', 'charts'):
            self.assertTrue(result[key], key)
        self.assertTrue(result['scene']['kind'])
        self.assertTrue(result['scene']['title'])
        self.assertTrue(result['scene']['description'])
        for chart in result['charts']:
            self.assertTrue(chart['title'])
            self.assertTrue(chart['x_label'])
            self.assertTrue(chart['y_label'])
            for curve in chart['series']:
                self.assertEqual(len(curve['x']), len(curve['y']))
                self.assertLessEqual(len(curve['x']), 650)
                self.assertTrue(all(math.isfinite(v) for v in curve['x']))
                self.assertTrue(all(math.isfinite(v) for v in curve['y']))

    def test_catalogue_unique_and_accessible(self):
        self.assertEqual(len(LABS), 30)
        self.assertEqual(len(LABS), len(LAB_BY_ID))
        self.assertEqual({l['id'] for l in LABS}, set(LAB_BY_ID))
        for lab in LABS:
            self.assertTrue(lab['intro'])
            self.assertTrue(lab['presets'])
            self.assertEqual(len(lab['controls']), len({c['key'] for c in lab['controls']}))
            for preset in lab['presets']:
                self.assertTrue(set(preset['values']) <= {c['key'] for c in lab['controls']})

    def test_default_for_every_laboratory(self):
        for lab in LABS:
            with self.subTest(lab=lab['id']):
                self.check_result(calculate({'lab': lab['id']}), lab['id'])

    def test_every_preset_is_exportable(self):
        for lab in LABS:
            for preset in lab['presets']:
                with self.subTest(lab=lab['id'], preset=preset['label']):
                    self.check_result(calculate({'lab': lab['id'], 'params': preset['values']}), lab['id'])

    def test_each_control_endpoint_and_choice(self):
        for lab in LABS:
            for c in lab['controls']:
                values = [o['value'] for o in c['options']] if c['type'] == 'select' else [c['min'], c['max']]
                for value in values:
                    with self.subTest(lab=lab['id'], control=c['key'], value=value):
                        self.check_result(calculate({'lab': lab['id'], 'params': {c['key']: value}}), lab['id'])

    def test_all_numeric_endpoints_together(self):
        for lab in LABS:
            for end in ('min', 'max'):
                params = {c['key']: c[end] for c in lab['controls'] if c['type'] == 'range'}
                with self.subTest(lab=lab['id'], end=end):
                    self.check_result(calculate({'lab': lab['id'], 'params': params}), lab['id'])

    def test_flat_and_nested_parameters_are_equivalent(self):
        for lab in LABS:
            params = self.defaults(lab)
            with self.subTest(lab=lab['id']):
                self.assertEqual(calculate({'lab': lab['id'], 'params': params}), calculate(dict(lab=lab['id'], **params)))

    def test_parameters_are_not_mutated(self):
        catalogue_before = copy.deepcopy(LABS)
        for lab in LABS:
            data = {'lab': lab['id'], 'params': self.defaults(lab)}
            before = copy.deepcopy(data)
            calculate(data)
            self.assertEqual(data, before)
        self.assertEqual(LABS, catalogue_before)

    def test_invalid_envelopes_and_laboratory_names(self):
        for data in [None, [], 1, True, 'boules_normes', {}, {'lab': None}, {'lab': []}, {'lab': True}, {'lab': 'absent'}]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                calculate(data)

    def test_params_requires_an_object(self):
        for value in [None, [], 1, True, 'tau=1']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate({'lab': 'boules_normes', 'params': value})

    def test_unknown_keys_are_not_silently_ignored(self):
        for lab in LABS:
            for data in [{'lab': lab['id'], 'params': {'absent': 1}}, {'lab': lab['id'], 'absent': 1}]:
                with self.subTest(data=data), self.assertRaises(ValueError):
                    calculate(data)

    def test_nonfinite_boolean_complex_string_and_huge_numbers_rejected(self):
        for lab in LABS:
            c = next((c for c in lab['controls'] if c['type'] == 'range'), None)
            if c is None: continue
            for value in [True, False, None, float('nan'), float('inf'), -float('inf'), '2', 1 + 0j, 1 << 4096, []]:
                with self.subTest(lab=lab['id'], value=value), self.assertRaises(ValueError):
                    calculate({'lab': lab['id'], 'params': {c['key']: value}})

    def test_outside_bounds_rejected_for_each_control(self):
        for lab in LABS:
            for c in lab['controls']:
                if c['type'] != 'range': continue
                for value in [c['min'] - 1, c['max'] + 1]:
                    with self.subTest(lab=lab['id'], control=c['key'], value=value), self.assertRaises(ValueError):
                        calculate({'lab': lab['id'], 'params': {c['key']: value}})

    def test_fractional_values_rejected_for_integer_controls(self):
        for lab in LABS:
            for c in lab['controls']:
                if not c.get('integer'): continue
                with self.subTest(lab=lab['id'], control=c['key']), self.assertRaises(ValueError):
                    calculate({'lab': lab['id'], 'params': {c['key']: c['min'] + .5}})

    def test_integer_valued_floats_remain_valid(self):
        for lab in LABS:
            c = next((c for c in lab['controls'] if c.get('integer')), None)
            if c is not None:
                with self.subTest(lab=lab['id']):
                    self.check_result(calculate({'lab': lab['id'], 'params': {c['key']: float(c['min'])}}), lab['id'])

    def test_invalid_selectors_rejected(self):
        for lab in LABS:
            for c in lab['controls']:
                if c['type'] != 'select': continue
                for value in ['choix_absent', 0, True, None, []]:
                    with self.subTest(lab=lab['id'], control=c['key'], value=value), self.assertRaises(ValueError):
                        calculate({'lab': lab['id'], 'params': {c['key']: value}})


if __name__ == '__main__':
    unittest.main()
