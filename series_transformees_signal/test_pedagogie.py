"""Vérifier les liens entre atlas, cours, exercices et guides publiés.

Ces contrôles portent sur la cohérence de la navigation et la sûreté du HTML
servi. Les identités scientifiques et erreurs numériques sont vérifiées dans
les suites de tests des modèles, sans dupliquer ces calculs ici.
"""
from collections import Counter
from html.parser import HTMLParser
import json
import unittest
from urllib.parse import urlsplit

from catalogue import LABS
from cours import LESSONS, EXERCISES, SOURCES, F, P
from reperes import LAB_GUIDES


class SafeEducationalHTML(HTMLParser):
    """Les textes pédagogiques ne doivent pas créer de contenu actif."""
    allowed_tags = {'p','b','div','br','a'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed_tags:
            raise AssertionError(f'Balise active ou inconnue : {tag}')
        attributes = dict(attrs)
        if any(key.startswith('on') for key in attributes):
            raise AssertionError('Gestionnaire JavaScript dans le texte pédagogique')
        if tag == 'a':
            parsed = urlsplit(attributes.get('href',''))
            if parsed.scheme != 'https' or not parsed.netloc:
                raise AssertionError('Lien de source non HTTPS')
        elif tag == 'div':
            if attributes != {'class':'formula'}:
                raise AssertionError('Attributs inattendus pour une formule')
        elif attributes:
            raise AssertionError(f'Attributs inattendus : {tag}')
        if tag != 'br':
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise AssertionError(f'HTML non équilibré : {tag}')

    def assert_finished(self):
        self.close()
        if self.stack:
            raise AssertionError('Balise pédagogique non fermée')


class PedagogicalIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.lab_ids = {lab['id'] for lab in LABS}

    def test_every_laboratory_has_a_guide_and_linked_content(self):
        self.assertEqual(set(LAB_GUIDES),self.lab_ids)
        self.assertEqual({item['lab'] for item in LESSONS},self.lab_ids)
        self.assertEqual({item['lab'] for item in EXERCISES},self.lab_ids)

    def test_each_lab_has_a_main_lesson_and_a_targeted_proof(self):
        self.assertEqual(Counter(item['lab'] for item in LESSONS),
                         Counter({lab:2 for lab in self.lab_ids}))
        for lab in self.lab_ids:
            pair=[item for item in LESSONS if item['lab']==lab]
            self.assertIn('Démonstration.',pair[0]['html'])
            self.assertIn('Justification.',pair[1]['html'])
            self.assertNotEqual(pair[0]['title'],pair[1]['title'])

    def test_each_lab_has_two_corrected_problems(self):
        self.assertEqual(Counter(item['lab'] for item in EXERCISES),
                         Counter({lab:2 for lab in self.lab_ids}))
        for item in EXERCISES:
            self.assertIn('Énoncé.',item['question'])
            self.assertIn('Corrigé.',item['answer'])
            self.assertNotEqual(item['question'],item['answer'])

    def test_one_based_lesson_links_resolve_to_the_same_lab(self):
        reached=set()
        for lab,guide in LAB_GUIDES.items():
            for number in guide['lesson_numbers']:
                self.assertIsInstance(number,int)
                self.assertGreaterEqual(number,1)
                self.assertLessEqual(number,len(LESSONS))
                self.assertEqual(LESSONS[number-1]['lab'],lab)
                reached.add(number)
        self.assertEqual(reached,set(range(1,len(LESSONS)+1)))

    def test_guided_steps_and_levels_exist_before_every_experiment(self):
        for lab,guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertEqual(set(guide['levels']),{'sup','spe','beyond'})
                self.assertEqual(len(guide['first_steps']),3)
                for field in ('objects','assumptions','techniques','first_steps'):
                    self.assertTrue(all(isinstance(value,str) and value.strip()
                                        for value in guide[field]))
                self.assertTrue(guide['purpose'].strip())
                self.assertTrue(guide['expected'].strip())

    def test_educational_html_is_balanced_and_has_no_active_tags(self):
        fragments=[item['html'] for item in LESSONS]
        fragments += [item[field] for item in EXERCISES
                      for field in ('question','answer')]
        fragments += SOURCES
        for fragment in fragments:
            parser=SafeEducationalHTML()
            parser.feed(fragment)
            parser.assert_finished()

    def test_formulas_escape_strict_inequalities_and_markup(self):
        formula=F('F > 2B ; x < 1\n<script>actif</script>')
        self.assertIn('F &gt; 2B',formula)
        self.assertIn('x &lt; 1',formula)
        self.assertIn('<br>',formula)
        self.assertNotIn('<script>',formula)
        parser=SafeEducationalHTML()
        parser.feed(formula)
        parser.assert_finished()

    def test_paragraph_helper_escapes_labels_and_content(self):
        paragraph=P('<label>','x<1 & y>0')
        self.assertIn('&lt;label&gt;',paragraph)
        self.assertIn('x&lt;1 &amp; y&gt;0',paragraph)
        self.assertNotIn('<label>',paragraph)

    def test_pedagogical_bundle_is_strict_json_for_the_server(self):
        bundle=dict(lessons=LESSONS,exercises=EXERCISES,sources=SOURCES,
                    guides=LAB_GUIDES)
        encoded=json.dumps(bundle,ensure_ascii=False,allow_nan=False)
        restored=json.loads(encoded)
        self.assertEqual(restored,bundle)

    def test_titles_have_unique_visible_numbering(self):
        for collection in (LESSONS,EXERCISES):
            titles=[item['title'] for item in collection]
            self.assertEqual(len(set(titles)),len(titles))
            for number,title in enumerate(titles,1):
                self.assertTrue(title.startswith(f'{number}. '))

    def test_sources_identify_requested_pages_and_real_primary_sites(self):
        source=' '.join(SOURCES)
        for page in ('99','103','105','107','108'):
            self.assertIn(page,source)
        self.assertIn('https://dlmf.nist.gov/1.8',source)
        self.assertIn('https://dlmf.nist.gov/1.14',source)
        self.assertIn('https://ocw.mit.edu/courses/',source)


if __name__=='__main__':
    unittest.main()
