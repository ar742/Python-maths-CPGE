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
        for payload in [None,[],{},dict(lab='unknown'),dict(lab=3),dict(lab='young',inconnu=1),dict(lab='young',params=[]),dict(lab='young',wavelength=True),dict(lab='young',wavelength=float('nan')),dict(lab='young',wavelength=float('inf')),dict(lab='young',wavelength=-1),dict(lab='young',mode='imaginaire')]:
            with self.subTest(payload=payload):
                with self.assertRaises((ValueError,TypeError)):calculate(payload)

    def test_nested_parameters_and_repeatability(self):
        a=calculate(dict(lab='young',params=dict(wavelength=550,mode='independent')))
        b=calculate(dict(lab='young',wavelength=550,mode='independent'))
        self.assertEqual(a,b)
        self.assertEqual(a,calculate(dict(lab='young',wavelength=550,mode='independent')))

    def test_phase_average_removes_only_the_cross_term(self):
        coherent=calculate(dict(lab='young'))
        independent=calculate(dict(lab='young',mode='independent'))
        opposite=calculate(dict(lab='young',phase=180))
        c=coherent['scene']['intensity']
        o=opposite['scene']['intensity']
        i=independent['scene']['intensity']
        self.assertEqual(len(c),len(i))
        for a,b,mean in zip(c,o,i):
            self.assertAlmostEqual((a+b)/2,mean,places=12)


if __name__=='__main__':unittest.main()
