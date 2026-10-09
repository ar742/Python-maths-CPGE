"""Le contrat public des 28 expériences : validation, scénarios et données de tracé."""
import copy
import json
import math
import unittest

from catalogue import LABS, LAB_BY_ID
from modeles import COMPUTE, calculate, parameters


class EntreeTests(unittest.TestCase):
    def assert_coordinates(self, values):
        self.assertIsInstance(values, list)
        self.assertTrue(values, 'Une série de coordonnées ne doit pas être vide.')
        for value in values:
            self.assertIsInstance(value, (int, float))
            self.assertNotIsInstance(value, bool)
            self.assertTrue(math.isfinite(value))

    def assert_result(self, output, lab_id):
        # La sérialisation stricte est celle dont dépend l'interface du navigateur.
        json.dumps(output, ensure_ascii=False, allow_nan=False)
        self.assertEqual(output['lab'], lab_id)
        self.assertEqual(set(output['params']), {c['key'] for c in LAB_BY_ID[lab_id]['controls']})
        for field in ('metrics', 'charts', 'steps', 'assumptions'):
            self.assertTrue(output[field], field)
        for metric in output['metrics']:
            self.assertTrue(metric['label'].strip())
            self.assertIn('unit', metric)
            self.assertIsInstance(metric['value'], (str, int, float))
        for chart in output['charts']:
            for field in ('title', 'x_label', 'y_label'):
                self.assertTrue(chart[field].strip())
            self.assertTrue(chart['series'])
            for curve in chart['series']:
                self.assertTrue(curve['label'].strip())
                self.assert_coordinates(curve['x'])
                self.assert_coordinates(curve['y'])
                self.assertEqual(len(curve['x']), len(curve['y']), 'Le navigateur doit associer chaque x à un y.')
        scene = output['scene']
        for field in ('kind', 'title', 'description'):
            self.assertTrue(scene[field].strip())
        if 'bounds' in scene:
            self.assertEqual(len(scene['bounds']), 4)
            xmin, xmax, ymin, ymax = scene['bounds']
            self.assertLess(xmin, xmax)
            self.assertLess(ymin, ymax)
        for path in scene.get('paths', []):
            self.assert_coordinates(path['x'])
            self.assert_coordinates(path['y'])
            self.assertEqual(len(path['x']), len(path['y']))
        if scene['kind'] == 'curves':
            self.assert_coordinates(scene['x'])
            for curve in scene['curves']:
                self.assert_coordinates(curve['y'])
                self.assertEqual(len(scene['x']), len(curve['y']))
        if scene['kind'] == 'heatmap':
            self.assert_coordinates(scene['x'])
            self.assert_coordinates(scene['y'])
            self.assertEqual(len(scene['z']), len(scene['y']))
            for row in scene['z']:
                self.assert_coordinates(row)
                self.assertEqual(len(row), len(scene['x']))
        for arrow in scene.get('arrows', []):
            self.assertTrue(all(math.isfinite(arrow[key]) for key in ('x','y','dx','dy')))

    def test_catalogue_and_calculators_cover_the_same_28_experiments(self):
        self.assertEqual(len(LABS), 28)
        self.assertEqual(len(LAB_BY_ID), 28)
        self.assertEqual({lab['id'] for lab in LABS}, set(COMPUTE))
        for lab in LABS:
            with self.subTest(lab=lab['id']):
                self.assertTrue(lab['intro'].strip())
                self.assertTrue(lab['title'].strip())
                self.assertGreaterEqual(len(lab['presets']), 3)
                keys = {c['key'] for c in lab['controls']}
                self.assertEqual(len(keys), len(lab['controls']))
                for control in lab['controls']:
                    if control['type'] == 'select':
                        options = [o['value'] for o in control['options']]
                        self.assertEqual(len(options), len(set(options)))
                        self.assertIn(control['value'], options)
                    else:
                        self.assertLess(control['min'], control['max'])
                        self.assertGreater(control['step'], 0)
                        self.assertLessEqual(control['min'], control['value'])
                        self.assertLessEqual(control['value'], control['max'])
                for preset in lab['presets']:
                    self.assertTrue(preset['label'].strip())
                    self.assertTrue(set(preset['values']) <= keys)
                    id_, values = parameters({'lab': lab['id'], 'params': preset['values']})
                    self.assertEqual(id_, lab['id'])
                    self.assertEqual(set(values), keys)

    def test_defaults_and_presets_have_exportable_graphs_and_scenes(self):
        for lab in LABS:
            requests = [{'lab': lab['id']}] + [{'lab': lab['id'], 'params': p['values']} for p in lab['presets']]
            for request in requests:
                with self.subTest(lab=lab['id'], params=request.get('params')):
                    self.assert_result(calculate(request), lab['id'])

    def test_each_endpoint_and_selector_option_is_computable(self):
        for lab in LABS:
            for control in lab['controls']:
                values = [o['value'] for o in control['options']] if control['type'] == 'select' else [control['min'], control['max']]
                for value in values:
                    with self.subTest(lab=lab['id'], control=control['key'], value=value):
                        self.assert_result(calculate({'lab': lab['id'], 'params': {control['key']: value}}), lab['id'])

    def test_flat_and_nested_requests_have_identical_results(self):
        for lab in LABS:
            params = {c['key']: c['value'] for c in lab['controls']}
            with self.subTest(lab=lab['id']):
                self.assertEqual(calculate({'lab': lab['id'], 'params': params}), calculate(dict(lab=lab['id'], **params)))

    def test_calculation_does_not_modify_requests_or_catalogue(self):
        catalogue_before = copy.deepcopy(LABS)
        for lab in LABS:
            request = {'lab': lab['id'], 'params': copy.deepcopy(lab['presets'][0]['values'])}
            before = copy.deepcopy(request)
            calculate(request)
            self.assertEqual(request, before)
        self.assertEqual(LABS, catalogue_before)

    def test_invalid_envelopes_and_lab_identifiers_are_rejected(self):
        for value in [None, [], 7, True, 'euler_rk4', {}, {'lab': None}, {'lab': []}, {'lab': True}, {'lab': 1}, {'lab': 'absent'}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate(value)

    def test_parameters_require_an_object(self):
        for value in [None, [], True, 1, 'a=1']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate({'lab': 'euler_rk4', 'params': value})

    def test_unknown_control_keys_are_rejected(self):
        for lab in LABS:
            for request in [{'lab': lab['id'], 'params': {'control_absent': 1}}, {'lab': lab['id'], 'control_absent': 1}]:
                with self.subTest(lab=lab['id']), self.assertRaises(ValueError):
                    calculate(request)

    def test_nonfinite_numbers_booleans_and_invalid_types_are_rejected(self):
        invalid = [True, False, None, float('nan'), float('inf'), -float('inf'), 1 << 4096, '1', complex(1, 0), [], {}]
        for lab in LABS:
            control = next(c for c in lab['controls'] if c['type'] == 'range')
            for value in invalid:
                with self.subTest(lab=lab['id'], type=type(value).__name__), self.assertRaises(ValueError):
                    calculate({'lab': lab['id'], 'params': {control['key']: value}})

    def test_values_outside_each_physical_domain_are_rejected(self):
        for lab in LABS:
            for control in lab['controls']:
                if control['type'] != 'range':
                    continue
                for value in [control['min'] - 1, control['max'] + 1]:
                    with self.subTest(lab=lab['id'], control=control['key']), self.assertRaises(ValueError):
                        calculate({'lab': lab['id'], 'params': {control['key']: value}})

    def test_integer_controls_reject_fractional_values_but_accept_integral_floats(self):
        for lab in LABS:
            for control in lab['controls']:
                if not control.get('integer'):
                    continue
                with self.subTest(lab=lab['id'], control=control['key']):
                    with self.assertRaises(ValueError):
                        parameters({'lab': lab['id'], 'params': {control['key']: control['min'] + .5}})
                    _, params = parameters({'lab': lab['id'], 'params': {control['key']: float(control['min'])}})
                    self.assertEqual(params[control['key']], control['min'])
                    self.assertIsInstance(params[control['key']], int)

    def test_selector_values_must_be_valid_strings(self):
        for lab in LABS:
            for control in lab['controls']:
                if control['type'] != 'select':
                    continue
                for value in ['option_absente', 0, True, None, []]:
                    with self.subTest(lab=lab['id'], control=control['key']), self.assertRaises(ValueError):
                        calculate({'lab': lab['id'], 'params': {control['key']: value}})


if __name__ == '__main__':
    unittest.main()
