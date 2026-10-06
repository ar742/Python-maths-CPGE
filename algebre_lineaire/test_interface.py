"""Contrats entre les contrôles visibles, les expériences et leurs explications."""
from pathlib import Path
import json
import math
import unittest
from modeles import calculate

source=Path(__file__).with_name('app.js').read_text(encoding='utf-8')
start=source.index('const labs=')+len('const labs=')
CONFIG=json.loads(source[start:source.index(';\n',start)])

def default(config):
    return {c[0]:c[3] if isinstance(c[2],list) or c[2]=='text' else c[5]
            for c in config['controls']}

class InterfaceTests(unittest.TestCase):
    def test_visible_defaults_and_exports_are_reproducible(self):
        for lab,cfg in CONFIG.items():
            with self.subTest(lab=lab):
                r=calculate(dict(lab=lab,**default(cfg)))
                self.assertEqual(r['lab'],lab)
                self.assertEqual(calculate(dict(lab=lab,**r['parameters'])),r)
                p=r.get('pedagogy',{})
                self.assertTrue(p.get('mission'),'Une question explicite est requise.')
                self.assertTrue(p.get('objects'),'Les objets doivent être définis.')
                self.assertTrue(p.get('reading'),'La lecture de la figure doit être guidée.')
                self.assertTrue(p.get('proof'),'Une construction doit être justifiée.')

    def test_every_visible_preset_can_be_calculated(self):
        for lab,cfg in CONFIG.items():
            for name,params in cfg['presets']:
                with self.subTest(lab=lab,preset=name):
                    calculate(dict(lab=lab,**(default(cfg)|params)))

    def test_every_visible_select_choice_can_be_calculated(self):
        for lab,cfg in CONFIG.items():
            for control in cfg['controls']:
                if not isinstance(control[2],list):continue
                for value,label in control[2]:
                    with self.subTest(lab=lab,control=control[0],choice=label):
                        calculate(dict(lab=lab,**(default(cfg)|{control[0]:value})))

    def test_corrected_exercise_opens_a_valid_experience(self):
        from cours import EXERCISES
        for ex in EXERCISES:
            with self.subTest(exercise=ex['title']):
                cfg=CONFIG[ex['lab']]
                calculate(dict(lab=ex['lab'],**(default(cfg)|ex.get('params',{}))))

    def test_visual_data_matches_the_objects(self):
        for lab in ('geometrie','jacobi','representations','symplectique','markov','reseaux','pfaffien'):
            r=calculate(dict(lab=lab,**default(CONFIG[lab])))
            self.assertTrue(r.get('scenes'),lab)
            for s in r['scenes']:
                with self.subTest(lab=lab,figure=s['title']):
                    self.assertTrue(s.get('description'))
                    if s['kind'] in ('graph','network','weights'):
                        nodes=s['nodes'];ids={n.get('id',i) for i,n in enumerate(nodes)}
                        for e in s.get('edges',[]):
                            self.assertIn(e.get('from',e.get('source')),ids)
                            self.assertIn(e.get('to',e.get('target')),ids)
                        for frame in s.get('frames',[]):
                            self.assertEqual(len(frame['values']),len(nodes))
                            self.assertTrue(all(math.isfinite(float(v)) for v in frame['values']))
                    if s['kind']=='matching':
                        for m in s['matchings']:
                            indices=[i for pair in m['pairs'] for i in pair]
                            self.assertEqual(sorted(indices),list(range(len(s['nodes']))))

if __name__=='__main__':unittest.main()
