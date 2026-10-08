"""Confronter les entrées du recueil aux vrais modèles et bilans proposés."""
import json
import unittest
from catalogue import LAB_BY_ID
from modeles import calculate
from pedagogie import LESSONS,EXERCISES,LAB_GUIDES
from reactions_recueil import REACTIONS

class AtlasTests(unittest.TestCase):
    def test_chaque_fiche_ouvre_un_cas_calculable_et_exportable(self):
        for item in REACTIONS:
            with self.subTest(reaction=item['id']):
                result=calculate({'lab':item['lab'],'params':item['params']})
                json.dumps(result,allow_nan=False)
                self.assertTrue(result['scene'])
                self.assertTrue(result['steps'])
                self.assertTrue(result['assumptions'])
    def test_recensement_des_pages_et_transformations_centrales(self):
        self.assertEqual({r['page'] for r in REACTIONS},{524,525,526,527,528,531,532,533,534})
        ids={r['lab'] for r in REACTIONS}
        self.assertTrue({'enolatealkyl','aminealkyl','photochlore','anhydride','hydrolyseacyle','grignardprep','e2stereo','nitrobenzene','dipolesnitro'}<=ids)
        self.assertTrue(any(r['params'].get('reagent')=='hcl2' for r in REACTIONS))
        self.assertTrue(any(r['params'].get('reaction')=='sulfonation' for r in REACTIONS))
        self.assertEqual(len({r['id'] for r in REACTIONS}),len(REACTIONS))
    def test_tous_les_nouveaux_tp_ont_des_objets_des_hypotheses_et_un_cours(self):
        self.assertEqual(set(LAB_GUIDES),set(LAB_BY_ID))
        for lab,guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertTrue(guide['purpose']);self.assertTrue(guide['objects'])
                self.assertTrue(guide['assumptions']);self.assertTrue(guide['expected'])
                self.assertEqual(len(guide['first_steps']),3)
                self.assertEqual(set(guide['levels']),{'sup','spe','beyond'})
                self.assertTrue(all(1<=i<=len(LESSONS) for i in guide['lesson_numbers']))
                self.assertIn(lab,[LESSONS[i-1]['lab'] for i in guide['lesson_numbers']])
                self.assertGreaterEqual(sum(e['lab']==lab for e in EXERCISES),2)
    def test_addition_hcl_propyne_geminale_et_intermediaire(self):
        one=calculate({'lab':'alcyne','params':{'substrate':'propyne','reagent':'hcl1'}})
        two=calculate({'lab':'alcyne','params':{'substrate':'propyne','reagent':'hcl2','stage':2}})
        self.assertEqual(one['product_name'],'2-chloroprop-1-ène')
        self.assertEqual(two['product_name'],'2,2-dichloropropane')
        self.assertEqual(two['equivalents'],2)
        self.assertNotIn('Br',str(two['scene']))
        self.assertIn('CCl₂',str(two['scene']))
    def test_sea_chloration_sulfonation_conserve_les_electrons_du_cycle(self):
        for reaction,element,group in [('chlorination','Cl','Cl'),('sulfonation','S','SO₃H')]:
            result=calculate({'lab':'aromatique','params':{'reaction':reaction,'substituent':'h','stage':2}})
            start,sigma,end=result['scene']['frames']
            e=next(a for a in start['atoms'] if a['id']=='e')
            self.assertEqual(e['element'],element)
            self.assertEqual(e['label'],group)
            self.assertEqual(sum(a['charge'] for a in sigma['atoms']),1)
            self.assertEqual(sum(a['charge'] for a in end['atoms']),0)
            ring_bonds=[b for b in end['bonds'] if b['a'].isdigit() and b['b'].isdigit()]
            self.assertEqual(sum(b['order']==2 for b in ring_bonds),3)

if __name__=='__main__':unittest.main()
