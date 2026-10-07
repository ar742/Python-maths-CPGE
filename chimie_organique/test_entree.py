"""Contrat d'expérience : données finies et choix accessibles depuis l'interface."""
import copy
import json
import math
import unittest
from catalogue import LABS,LAB_BY_ID
from modeles import calculate

class EntreeTests(unittest.TestCase):
    def test_tous_les_cas_proposes_donnent_un_resultat_exportable(self):
        for lab in LABS:
            base={control['key']:control['value'] for control in lab['controls']}
            cases=[base]+[dict(base,**preset['values']) for preset in lab['presets']]
            for params in cases:
                with self.subTest(lab=lab['id'],params=params):
                    result=calculate({'lab':lab['id'],'params':params})
                    json.dumps(result,allow_nan=False)
                    self.assertTrue(result['metrics']);self.assertTrue(result['steps']);self.assertTrue(result['assumptions'])
                    self.assertIn('kind',result['scene'])
                    for chart in result['charts']:
                        for curve in chart['series']:
                            self.assertEqual(len(curve['x']),len(curve['y']))

    def test_bornes_et_choix_individuels_de_l_interface(self):
        for lab in LABS:
            base={control['key']:control['value'] for control in lab['controls']}
            for control in lab['controls']:
                values=[o['value'] for o in control['options']] if control['type']=='select' else [control['min'],control['max']]
                for value in values:
                    with self.subTest(lab=lab['id'],param=control['key'],value=value):
                        result=calculate({'lab':lab['id'],'params':dict(base,**{control['key']:value})})
                        json.dumps(result,allow_nan=False)

    def test_parametres_plats_et_imbriques_equivalents(self):
        lab=LABS[0];base={c['key']:c['value'] for c in lab['controls']}
        self.assertEqual(calculate({'lab':lab['id'],'params':base}),calculate(dict(lab=lab['id'],**base)))

    def test_refus_nombre_non_fini_boolean_inconnu(self):
        lab=next(lab for lab in LABS if any(c['type']!='select' for c in lab['controls']))
        control=next(c for c in lab['controls'] if c['type']!='select')
        for value in [True,float('nan'),float('inf'),-float('inf'),'2',control['max']+1]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                calculate({'lab':lab['id'],'params':{control['key']:value}})
        for data in [[],{'lab':'absent'},{'lab':lab['id'],'params':[]},{'lab':lab['id'],'parametre_inconnu':1}]:
            with self.subTest(data=data),self.assertRaises(ValueError): calculate(data)

    def test_les_formules_brutes_exigent_des_nombres_d_atomes_entiers(self):
        with self.assertRaises(ValueError): calculate({'lab':'formule','C':2.5})

    def test_integrite_des_graphes_et_fleches(self):
        def visit(value):
            if isinstance(value,dict):
                if 'atoms' in value and 'bonds' in value:
                    ids=[str(atom['id']) for atom in value['atoms']]
                    self.assertEqual(len(ids),len(set(ids)))
                    for bond in value['bonds']:
                        self.assertIn(str(bond['a']),ids);self.assertIn(str(bond['b']),ids)
                        self.assertNotEqual(str(bond['a']),str(bond['b']))
                        self.assertIn(bond['order'],(1,1.5,2,3))
                    for arrow in value.get('arrows',[]):
                        self.assertIn(arrow.get('electrons',2),(1,2))
                        for key in ['start','end']:
                            self.assertEqual(len(arrow[key]),2)
                for child in value.values(): visit(child)
            elif isinstance(value,list):
                for child in value: visit(child)
        for lab in LABS:
            for preset in [None]+lab['presets']:
                with self.subTest(lab=lab['id'],preset=preset and preset['label']):
                    result=calculate({'lab':lab['id'],'params':preset['values'] if preset else {}})
                    visit(result['scene'])

if __name__=='__main__': unittest.main()
