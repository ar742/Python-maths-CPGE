"""Vérifier la navigation, l’intégrité HTML et la livraison du cours complet."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlparse

from catalogue import BASE_LABS as LABS
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
    def test_every_lab_has_a_course_a_guide_and_two_different_problems(self):
        ids = {lab["id"] for lab in LABS}
        self.assertEqual(len(ids), 30)
        self.assertEqual(len(LABS), 30)
        self.assertEqual(set(LAB_GUIDES), ids)
        self.assertEqual({item["lab"] for item in LESSONS}, ids)
        self.assertEqual(Counter(item["lab"] for item in EXERCISES),
                         Counter({lab: 2 for lab in ids}))
        for lab in ids:
            problems = [item for item in EXERCISES if item["lab"] == lab]
            self.assertNotEqual(problems[0]["question"], problems[1]["question"])

    def test_course_is_complete_numbered_and_explains_its_formulas(self):
        self.assertEqual(len(LESSONS), 42)
        self.assertEqual([int(item["title"].split(".", 1)[0]) for item in LESSONS],
                         list(range(1, 43)))
        for item in LESSONS:
            with self.subTest(lesson=item["title"]):
                self.assertTrue(item["level"])
                self.assertGreaterEqual(item["html"].count("<p>"), 4)
                self.assertIn("class='formula'", item["html"])
                self.assertGreater(len(prose(item["html"])), 1000)

    def test_sixty_answers_and_questions_survive_export(self):
        self.assertEqual(len(EXERCISES), 60)
        self.assertEqual([int(item["title"].split(".", 1)[0]) for item in EXERCISES],
                         list(range(1, 61)))
        for item in EXERCISES:
            with self.subTest(problem=item["title"]):
                self.assertIn("Énoncé.", item["question"])
                self.assertIn("Corrigé.", item["answer"])
                self.assertGreater(len(prose(item["question"])), 100)
                self.assertGreater(len(prose(item["answer"])), 500)

    def test_html_is_closed_and_does_not_swallow_inequalities(self):
        fragments = [item["html"] for item in LESSONS] + SOURCES
        fragments += [item[key] for item in EXERCISES for key in ("question", "answer")]
        for fragment in fragments:
            parser = EditorialHTML()
            parser.feed(fragment)
            parser.close()
            self.assertEqual(parser.errors, [])
            self.assertEqual(parser.stack, [])
        self.assertIn("β<0", prose(LESSONS[37]["html"]))
        self.assertIn("r≤1", prose(LESSONS[41]["html"]))
        self.assertIn("|S|<1", prose(LESSONS[36]["html"]))

    def test_guides_define_objects_limits_three_actions_and_course_links(self):
        for lab, item in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertGreater(len(item["purpose"]), 100)
                self.assertGreaterEqual(len(item["objects"]), 2)
                self.assertGreaterEqual(len(item["assumptions"]), 2)
                self.assertEqual(len(item["techniques"]), 3)
                self.assertEqual(len(item["first_steps"]), 3)
                self.assertEqual(set(item["levels"]), {"sup", "spe", "beyond"})
                self.assertTrue(all(item["levels"].values()))
                self.assertTrue(item["expected"])
                refs = item["lesson_numbers"]
                self.assertEqual(len(refs), len(set(refs)))
                self.assertTrue(all(1 <= ref <= len(LESSONS) for ref in refs))
                self.assertIn(lab, [LESSONS[ref-1]["lab"] for ref in refs])

    def test_twelve_missions_cover_all_laboratories_with_deliverables(self):
        text = (ROOT / "PARCOURS.md").read_text(encoding="utf-8")
        missions = re.findall(r"^## Mission (\d+) —", text, re.MULTILINE)
        self.assertEqual(list(map(int, missions)), list(range(1, 13)))
        self.assertEqual(set(re.findall(r"`([a-z0-9]+)`", text)),
                         {lab["id"] for lab in LABS})
        for section in re.split(r"^## Mission \d+ —", text, flags=re.MULTILINE)[1:]:
            for title in ("**Prévoir.**", "**Expérimenter.**", "**Justifier.**", "**Livrable :**"):
                self.assertIn(title, section)

    def test_program_map_covers_all_labs_and_distinguishes_filiere_and_extension(self):
        text = (ROOT / "MATRICE_PROGRAMME.md").read_text(encoding="utf-8")
        from catalogue import LABS as ALL_LABS
        ids = {lab["id"] for lab in ALL_LABS}
        rows = set(re.findall(r"^\| `([a-z0-9]+)` \|", text, re.MULTILINE))
        self.assertEqual(rows, ids)
        self.assertIn("PCSI", text)
        self.assertIn("option PC", text)
        self.assertIn("prolongements numériques", text)
        self.assertIn("réactiothèque accompagnée", text)

    def test_sources_are_public_primary_institutions_and_no_private_pdf_is_linked(self):
        parser = EditorialHTML()
        parser.feed("".join(SOURCES))
        self.assertGreaterEqual(len(parser.links), 15)
        primary = {"www.education.gouv.fr", "cache.media.education.gouv.fr",
                   "goldbook.iupac.org", "old.goldbook.iupac.org", "iupac.org",
                   "ocw.mit.edu", "webbook.nist.gov", "physics.nist.gov",
                   "pubchem.ncbi.nlm.nih.gov"}
        for url in parser.links:
            self.assertEqual(urlparse(url).scheme, "https")
            self.assertIn(urlparse(url).hostname, primary)
        public = "".join(item["html"] for item in LESSONS) + "".join(SOURCES)
        self.assertNotIn("C:\\Users", public)
        self.assertNotIn("MemoCPGEScientifAR2027-chimieOrga.pdf", public)

    def test_export_preserves_every_lesson_guide_answer_and_link(self):
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
                self.assertIn(prose(item["question"]), text)
                self.assertIn(prose(item["answer"]), text)
            for lab, item in LAB_GUIDES.items():
                self.assertIn("### Laboratoire `" + lab + "`", text)
                self.assertIn(item["objects"][0], text)
                self.assertIn(item["assumptions"][0], text)
                self.assertIn("](illustrations/" + lab + ".svg)", text)
            parser = EditorialHTML()
            parser.feed("".join(SOURCES))
            for url in parser.links:
                self.assertIn("](" + url + ")", text)
            self.assertNotIn("<p>", text)
            self.assertNotIn("<div", text)

    def test_concentration_notation_is_not_a_markdown_link(self):
        self.assertEqual(prose("<p>[RX](t)=[RX]₀ exp(−kt)</p>"),
                         r"\[RX\](t)=\[RX\]₀ exp(−kt)")
        self.assertEqual(prose("<p>v=[S](k₁+k₂[Nu])</p>"),
                         r"v=\[S\](k₁+k₂\[Nu\])")
        self.assertEqual(prose("<a href='https://iupac.org/'>Source</a>"),
                         "[Source](https://iupac.org/)")

    def test_delivered_base_markdown_is_current(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            generated = export(Path(directory) / "cours.md")
            self.assertEqual(generated.read_bytes(), (ROOT / "COURS.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
