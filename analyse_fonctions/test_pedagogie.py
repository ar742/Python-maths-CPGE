"""Relier chaque expérience à ses objectifs, cours et exercices, sans texte de secours."""
from collections import Counter
from html.parser import HTMLParser
import json
import unittest
from urllib.parse import urlsplit

from catalogue import LABS
from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


class EducationalHTML(HTMLParser):
    """Les fragments pédagogiques peuvent contenir des formules et des liens, pas du code actif."""
    allowed_tags = {'p', 'b', 'strong', 'em', 'i', 'br', 'a', 'div', 'h3', 'h4', 'ul', 'ol', 'li', 'sub', 'sup', 'code', 'details', 'summary'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed_tags:
            raise AssertionError(f'Balise non pédagogique : {tag}')
        attributes = dict(attrs)
        if any(name.lower().startswith('on') for name in attributes):
            raise AssertionError('Gestionnaire de script dans un texte')
        if tag == 'a':
            parsed = urlsplit(attributes.get('href', ''))
            if parsed.scheme != 'https' or not parsed.netloc:
                raise AssertionError('Lien externe sans source HTTPS')
            if set(attributes) - {'href', 'target', 'rel'}:
                raise AssertionError('Attribut actif ou inattendu dans un lien')
            if attributes.get('target') == '_blank' and 'noopener' not in attributes.get('rel', '').split():
                raise AssertionError('Lien de nouvel onglet sans noopener')
        elif tag == 'div':
            if attributes != {'class': 'formula'}:
                raise AssertionError('La classe formula est attendue pour les formules')
        elif attributes:
            raise AssertionError(f'Attributs inattendus pour {tag}')
        if tag != 'br':
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise AssertionError(f'Fermeture HTML non équilibrée : {tag}')

    def assert_finished(self):
        self.close()
        if self.stack:
            raise AssertionError(f'Balise non fermée : {self.stack[-1]}')


class PedagogicalIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.lab_ids = {lab['id'] for lab in LABS}

    def test_every_lab_has_two_lessons_three_corrected_exercises_and_one_guide(self):
        self.assertEqual(len(LESSONS), 56)
        self.assertEqual(len(EXERCISES), 84)
        self.assertEqual(len(LAB_GUIDES), 28)
        self.assertEqual(set(LAB_GUIDES), self.lab_ids)
        self.assertEqual(Counter(item['lab'] for item in LESSONS), Counter({lab: 2 for lab in self.lab_ids}))
        self.assertEqual(Counter(item['lab'] for item in EXERCISES), Counter({lab: 3 for lab in self.lab_ids}))

    def test_guide_lesson_numbers_link_to_exactly_its_two_lessons(self):
        reached = set()
        for lab, guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                expected = [i + 1 for i, lesson in enumerate(LESSONS) if lesson['lab'] == lab]
                self.assertEqual(guide['lesson_numbers'], expected)
                self.assertEqual(len(expected), 2)
                for number in guide['lesson_numbers']:
                    self.assertIsInstance(number, int)
                    self.assertEqual(LESSONS[number - 1]['lab'], lab)
                    reached.add(number)
        self.assertEqual(reached, set(range(1, 57)))

    def test_every_guide_explains_objects_hypotheses_and_first_manipulations(self):
        for lab, guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                for field in ('purpose', 'expected'):
                    self.assertIsInstance(guide[field], str)
                    self.assertTrue(guide[field].strip())
                for field in ('objects', 'hypotheses', 'techniques', 'first_steps'):
                    self.assertIsInstance(guide[field], list)
                    self.assertTrue(guide[field])
                    self.assertTrue(all(isinstance(value, str) and value.strip() for value in guide[field]))
                self.assertEqual(len(guide['first_steps']), 3)
                self.assertEqual(set(guide['levels']), {'sup', 'spe', 'beyond'})
                self.assertTrue(all(isinstance(value, str) and value.strip() for value in guide['levels'].values()))

    def test_content_is_distinct_and_has_no_placeholder_fallback(self):
        placeholders = ('lorem ipsum', 'à compléter', 'contenu de secours', 'cours à venir', 'corrigé à venir', 'todo:')
        for collection in (LESSONS, EXERCISES):
            self.assertEqual(len({item['title'] for item in collection}), len(collection))
            for item in collection:
                with self.subTest(lab=item['lab'], title=item['title']):
                    self.assertTrue(item['title'].strip())
                    self.assertTrue(item['level'].strip())
                    fragments = [item['html']] if 'html' in item else [item['question'], item['answer']]
                    for text in fragments:
                        self.assertTrue(text.strip())
                        self.assertFalse(any(marker in text.lower() for marker in placeholders))
                    if 'question' in item:
                        self.assertNotEqual(item['question'], item['answer'])
        # Un assemblage accidentel de contenus génériques donnerait des fragments identiques.
        self.assertEqual(len({item['html'] for item in LESSONS}), len(LESSONS))
        self.assertEqual(len({item['answer'] for item in EXERCISES}), len(EXERCISES))

    def test_educational_html_is_balanced_and_does_not_execute_scripts(self):
        fragments = [item['html'] for item in LESSONS]
        fragments.extend(item[field] for item in EXERCISES for field in ('question', 'answer'))
        fragments.extend(SOURCES)
        for index, fragment in enumerate(fragments):
            with self.subTest(fragment=index):
                parser = EducationalHTML()
                parser.feed(fragment)
                parser.assert_finished()

    def test_html_checker_detects_unsafe_or_broken_fragments(self):
        for fragment in ['<script>document.write(1)</script>', '<p onclick="doSomething()">texte</p>', '<a href="javascript:alert(1)">lien</a>', '<p>texte</div>', '<p>texte']:
            with self.subTest(fragment=fragment), self.assertRaises(AssertionError):
                parser = EducationalHTML()
                parser.feed(fragment)
                parser.assert_finished()

    def test_pedagogical_bundle_survives_strict_json_round_trip(self):
        bundle = dict(lessons=LESSONS, exercises=EXERCISES, sources=SOURCES, guides=LAB_GUIDES)
        self.assertEqual(json.loads(json.dumps(bundle, ensure_ascii=False, allow_nan=False)), bundle)

    def test_source_priorities_identify_the_three_requested_parts(self):
        text = ' '.join(SOURCES)
        for reference in ('63', '68', '72', 'équations différentielles', 'domination'):
            self.assertIn(reference, text)


if __name__ == '__main__':
    unittest.main()
