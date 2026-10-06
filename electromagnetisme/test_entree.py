"""Contrat des commandes, reproductibilité et finitude aux bords des domaines."""
import json
import math
import unittest
from catalogue import LABS
from modeles import calculate


class EntryTests(unittest.TestCase):
    def test_every_lab_and_preset(self):
        self.assertEqual(len(LABS),24)
        self.assertEqual(len({lab['id'] for lab in LABS}),24)
        for lab in LABS:
            for preset in [dict(label='Défaut',values={})]+lab['presets']:
                with self.subTest(lab=lab['id'],preset=preset['label']):
                    r=calculate(dict(lab=lab['id'],**preset['values']))
                    self.assertEqual(r['lab'],lab['id'])
                    self.assertTrue(r['metrics'])
                    self.assertTrue(r['steps'])
                    self.assertTrue(r['assumptions'])
                    json.dumps(r,allow_nan=False)
                    self.assertTrue(r.get('field') or r.get('scene'))
                    for chart in r['charts']:
                        self.assertTrue(chart['x_label'])
                        self.assertTrue(chart['y_label'])
                        for s in chart['series']:
                            self.assertEqual(len(s['x']),len(s['y']))

    def test_numeric_boundaries(self):
        for lab in LABS:
            for c in lab['controls']:
                for v in ([o['value'] for o in c['options']] if c.get('options') else [c['min'],c['max']]):
                    with self.subTest(lab=lab['id'],control=c['key'],value=v):
                        json.dumps(calculate(dict(lab=lab['id'],**{c['key']:v})),allow_nan=False)

    def test_unknown_or_malformed_commands(self):
        for payload in [None,[],{},dict(lab='unknown'),dict(lab=3),dict(lab='maxwell',inconnu=1),dict(lab='maxwell',params=[]),dict(lab='maxwell',amplitude=True),dict(lab='maxwell',amplitude=float('nan')),dict(lab='maxwell',amplitude=float('inf')),dict(lab='maxwell',amplitude=-1),dict(lab='maxwell',mode='imaginaire')]:
            with self.subTest(payload=payload):
                with self.assertRaises((ValueError,TypeError)):calculate(payload)

    def test_nested_parameters_and_repeatability(self):
        a=calculate(dict(lab='hall',params=dict(B=-.5,carrier='hole')))
        b=calculate(dict(lab='hall',B=-.5,carrier='hole'))
        self.assertEqual(a,b)
        self.assertEqual(a,calculate(dict(lab='hall',B=-.5,carrier='hole')))

    def test_vector_field_grid(self):
        for lab in ['dipoles','biotsavart','helmholtz']:
            f=calculate(dict(lab=lab))['field']
            self.assertTrue(all(b>a for a,b in zip(f['x'],f['x'][1:])))
            self.assertTrue(all(b>a for a,b in zip(f['y'],f['y'][1:])))
            for key in ['u','v','scalar']:
                self.assertEqual(len(f[key]),len(f['y']))
                self.assertTrue(all(len(row)==len(f['x']) for row in f[key]))
                self.assertTrue(all(math.isfinite(v) for row in f[key] for v in row))


if __name__=='__main__':unittest.main()
