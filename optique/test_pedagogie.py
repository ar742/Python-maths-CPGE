"""Navigation pédagogique, formules lisibles et export intégral (stdlib seule)."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlparse

from catalogue import LABS
from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES
from export_cours import export, prose


ROOT = Path(__file__).resolve().parent


class EditorialHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"p", "b", "div", "br", "a"}:
            self.errors.append("Balise inconnue : " + tag)
        if tag == "a":
            self.links.append(dict(attrs).get("href", ""))
        if tag != "br":
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            self.errors.append("Fermeture incohérente : " + tag)


class PedagogieTests(unittest.TestCase):
    def test_every_lab_has_course_guide_and_two_corrected_exercises(self):
        ids = {lab["id"] for lab in LABS}
        self.assertEqual(len(LABS), 24)
        self.assertEqual(len(ids), 24)
        self.assertEqual(set(LAB_GUIDES), ids)
        self.assertEqual({item["lab"] for item in LESSONS}, ids)
        self.assertEqual(Counter(item["lab"] for item in EXERCISES), Counter({id_: 2 for id_ in ids}))

    def test_course_is_complete_numbered_and_has_reasoning(self):
        self.assertEqual(len(LESSONS), 36)
        self.assertEqual([int(x["title"].split(".", 1)[0]) for x in LESSONS], list(range(1, 37)))
        for item in LESSONS:
            with self.subTest(lesson=item["title"]):
                self.assertTrue(item["level"])
                self.assertGreaterEqual(item["html"].count("<p>"), 4)
                self.assertIn("class='formula'", item["html"])

    def test_corrected_exercises_are_substantive_and_sequential(self):
        self.assertEqual(len(EXERCISES), 48)
        self.assertEqual([int(x["title"].split(".", 1)[0]) for x in EXERCISES], list(range(1, 49)))
        for item in EXERCISES:
            with self.subTest(exercise=item["title"]):
                self.assertIn("Énoncé.", item["question"])
                self.assertIn("Corrigé.", item["answer"])
                self.assertGreater(len(prose(item["answer"])), 300)
                self.assertIn("=", prose(item["answer"]))

    def test_html_is_closed_and_does_not_absorb_formula_inequalities(self):
        fragments = [x["html"] for x in LESSONS] + SOURCES
        fragments += [x[k] for x in EXERCISES for k in ("question", "answer")]
        for fragment in fragments:
            parser = EditorialHTML()
            parser.feed(fragment)
            parser.close()
            self.assertEqual(parser.errors, [])
            self.assertEqual(parser.stack, [])
        self.assertIn("p<0", prose(LESSONS[2]["html"]))
        self.assertIn("V<2,405", prose(LESSONS[11]["html"]))
        self.assertIn("0<g₁g₂<1", prose(LESSONS[32]["html"]))

    def test_guides_include_hypotheses_units_levels_and_three_actions(self):
        for lab, guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertGreater(len(guide["purpose"]), 100)
                self.assertGreaterEqual(len(guide["objects"]), 2)
                self.assertGreaterEqual(len(guide["assumptions"]), 2)
                self.assertEqual(len(guide["first_steps"]), 3)
                self.assertEqual(len(guide["techniques"]), 3)
                self.assertEqual(set(guide["levels"]), {"sup", "spe", "beyond"})
                self.assertTrue(all(guide["levels"].values()))
                self.assertTrue(guide["expected"])
                refs = guide["lesson_numbers"]
                self.assertEqual(len(refs), len(set(refs)))
                self.assertTrue(all(1 <= ref <= len(LESSONS) for ref in refs))
                self.assertIn(lab, [LESSONS[i-1]["lab"] for i in refs])

    def test_ten_missions_cover_the_whole_workshop(self):
        text = (ROOT / "PARCOURS.md").read_text(encoding="utf-8")
        missions = re.findall(r"^## Mission (\d+) —", text, re.MULTILINE)
        self.assertEqual(list(map(int, missions)), list(range(1, 11)))
        self.assertEqual(set(re.findall(r"`([a-z]+)`", text)), {lab["id"] for lab in LABS})
        for section in re.split(r"^## Mission \d+ —", text, flags=re.MULTILINE)[1:]:
            for title in ("**Prévoir.**", "**Expérimenter.**", "**Justifier.**", "**Livrable :**"):
                self.assertIn(title, section)

    def test_sources_are_public_primary_institutions(self):
        parser = EditorialHTML()
        parser.feed("".join(SOURCES))
        self.assertGreaterEqual(len(parser.links), 12)
        primary = {"www.education.gouv.fr", "www.ocw.mit.edu", "ocw.mit.edu", "science.nasa.gov", "www.nei.nih.gov", "www.physics.usyd.edu.au", "farside.ph.utexas.edu"}
        for url in parser.links:
            self.assertEqual(urlparse(url).scheme, "https")
            self.assertIn(urlparse(url).hostname, primary)
        public = "".join(frag for item in LESSONS for frag in (item["html"],)) + "".join(SOURCES)
        self.assertNotIn("C:\\Users", public)
        self.assertNotIn("MemoCPGEScientifAR2027-optique.pdf", public)

    def test_export_preserves_every_guide_answer_and_link(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            path = export(Path(directory) / "cours.md")
            data = path.read_bytes()
            self.assertNotIn(b"\r", data)
            text = data.decode("utf-8")
            for item in LESSONS:
                self.assertIn("## " + item["title"], text)
                self.assertIn(prose(item["html"]), text)
            for item in EXERCISES:
                self.assertIn("### " + item["title"], text)
                self.assertIn(prose(item["answer"]), text)
            for lab, guide in LAB_GUIDES.items():
                self.assertIn("### Laboratoire `" + lab + "`", text)
                self.assertIn(guide["objects"][0], text)
                self.assertIn(guide["assumptions"][0], text)
            parser = EditorialHTML()
            parser.feed("".join(SOURCES))
            for url in parser.links:
                self.assertIn("](" + url + ")", text)
            self.assertNotIn("<p>", text)
            self.assertNotIn("<div", text)

    def test_generated_course_is_current(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            current = export(Path(directory) / "cours.md")
            self.assertEqual(current.read_bytes(), (ROOT / "COURS.md").read_bytes())

    def test_only_four_verified_formula_errata_are_listed(self):
        text = (ROOT / "ERRATA.md").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"^## (\d+)\.", text, re.MULTILINE), ["1", "2", "3", "4"])
        for page in ("337", "344", "348", "350"):
            self.assertIn("Recueil p. " + page, text)
        self.assertNotIn("C:\\Users", text)


if __name__ == "__main__":
    unittest.main()
