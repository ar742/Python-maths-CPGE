"""Contrats de navigation, lisibilité, sources et export (stdlib seule).

La validation scientifique des modèles est indépendante, dans test_conversion.py et test_ondes.py.
Ces tests empêchent notamment un corrigé manquant, un guide sans cours, une
commande supprimée ou une inégalité absorbée comme balise HTML.
"""

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
IDS = set("dipoles gauss biotsavart helmholtz drude hall induction hautparleur hysteresis synchrone asynchrone peau maxwell interfaces guide antenne plasma dielectrique aimantation meissner faraday kerr rayonnement dynamo".split())


class ConstantHTML(HTMLParser):
    """Les constantes éditoriales utilisent seulement des balises autorisées."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = []
        self.errors = []
        self.text = []

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

    def handle_data(self, text):
        self.text.append(text)


class PedagogieTests(unittest.TestCase):
    def test_catalogue_has_exactly_24_unique_ids(self):
        self.assertEqual(len(LABS), 24)
        self.assertEqual({lab["id"] for lab in LABS}, IDS)

    def test_lessons_are_ordered_and_cover_every_experiment(self):
        self.assertEqual(len(LESSONS), 36)
        self.assertEqual([int(x["title"].split(".", 1)[0]) for x in LESSONS], list(range(1, 37)))
        self.assertEqual({x["lab"] for x in LESSONS}, IDS)
        for item in LESSONS:
            with self.subTest(lesson=item["title"]):
                self.assertTrue(item["level"])
                self.assertGreaterEqual(item["html"].count("<p>"), 4)
                self.assertIn("class='formula'", item["html"])

    def test_all_48_exercises_have_full_answers(self):
        self.assertEqual(len(EXERCISES), 48)
        self.assertEqual([int(x["title"].split(".", 1)[0]) for x in EXERCISES], list(range(1, 49)))
        self.assertEqual(Counter(x["lab"] for x in EXERCISES), Counter({id_: 2 for id_ in IDS}))
        for item in EXERCISES:
            with self.subTest(exercise=item["title"]):
                self.assertIn("Énoncé.", item["question"])
                self.assertIn("Corrigé.", item["answer"])
                # Rejeter une réponse vide ou un simple placeholder ; le test
                # scientifique est la relecture et le contrôle des modèles.
                self.assertGreater(len(prose(item["answer"])), 200)
                self.assertIn("=", prose(item["answer"]))

    def test_html_preserves_inequalities_and_has_no_open_tags(self):
        fragments = [x["html"] for x in LESSONS]
        fragments += [x[k] for x in EXERCISES for k in ("question", "answer")]
        fragments += SOURCES
        for fragment in fragments:
            parser = ConstantHTML()
            parser.feed(fragment)
            parser.close()
            self.assertEqual(parser.errors, [])
            self.assertEqual(parser.stack, [])
        self.assertIn("a<b", prose(LESSONS[5]["html"]))
        self.assertIn("ω<ωp", prose(LESSONS[25]["html"]))

    def test_guides_have_units_hypotheses_and_three_actions(self):
        self.assertEqual(set(LAB_GUIDES), IDS)
        for lab, guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertGreater(len(guide["purpose"]), 80)
                self.assertGreaterEqual(len(guide["objects"]), 2)
                self.assertGreaterEqual(len(guide["assumptions"]), 2)
                self.assertEqual(len(guide["first_steps"]), 3)
                self.assertEqual(len(guide["techniques"]), 3)
                self.assertEqual(set(guide["levels"]), {"sup", "spe", "beyond"})
                self.assertTrue(all(guide["levels"].values()))
                self.assertTrue(guide["expected"])

    def test_guide_lesson_links_are_valid_and_relevant(self):
        for lab, guide in LAB_GUIDES.items():
            with self.subTest(lab=lab):
                self.assertEqual(len(guide["lesson_numbers"]), len(set(guide["lesson_numbers"])))
                self.assertTrue(all(1 <= i <= 36 for i in guide["lesson_numbers"]))
                self.assertIn(lab, [LESSONS[i-1]["lab"] for i in guide["lesson_numbers"]])

    def test_commands_required_by_guides_are_real(self):
        requirements = {
            "dipoles": {"q", "a", "angle", "distance"}, "gauss": {"mode", "Q", "R", "length", "ratio"},
            "biotsavart": {"mode", "I", "R", "length"}, "helmholtz": {"R", "spacing", "I", "turns"},
            "drude": {"tau", "frequency", "carrier"}, "hall": {"carrier", "B", "width", "thickness"},
            "induction": {"mode", "B", "R", "L", "mass", "height"}, "hautparleur": {"coupling", "frequency", "mass", "stiffness"},
            "hysteresis": {"Bs", "amplitude", "frequency", "N1", "N2"}, "synchrone": {"phase", "load", "J"},
            "asynchrone": {"slip", "R2", "poles"}, "peau": {"mode", "logf", "time"},
            "maxwell": {"mode", "ellipticity", "phase"}, "interfaces": {"polarization", "angle", "wavelength"},
            "guide": {"frequency", "width", "phase", "length"}, "antenne": {"aperture", "steering"},
            "plasma": {"ratio", "collision", "density"}, "dielectrique": {"ratio", "damping", "field"},
            "aimantation": {"model", "temperature", "radius", "demag"}, "meissner": {"history", "halfwidth", "penetration"},
            "faraday": {"passes", "field", "analyzer", "verdet", "length"}, "kerr": {"intensity", "n2", "distance"},
            "rayonnement": {"model", "frequency", "resonance", "dipole"}, "dynamo": {"alpha", "velocity", "helicity", "length"},
        }
        for lab in LABS:
            self.assertLessEqual(requirements[lab["id"]], {c["key"] for c in lab["controls"]})

    def test_ten_missions_cover_the_24_ids(self):
        text = (ROOT / "PARCOURS.md").read_text(encoding="utf-8")
        missions = re.findall(r"^## Mission (\d+) —", text, re.MULTILINE)
        self.assertEqual(list(map(int, missions)), list(range(1, 11)))
        ids = set(re.findall(r"`([a-z]+)`", text))
        self.assertEqual(ids, IDS)
        for section in re.split(r"^## Mission \d+ —", text, flags=re.MULTILINE)[1:]:
            self.assertIn("**Prévoir.**", section)
            self.assertIn("**Expérimenter.**", section)
            self.assertIn("**Justifier.**", section)
            self.assertIn("**Livrable :**", section)

    def test_sources_are_public_primary_links(self):
        parser = ConstantHTML()
        parser.feed("".join(SOURCES))
        self.assertGreaterEqual(len(parser.links), 12)
        allowed = {"www.education.gouv.fr", "ocw.mit.edu", "www.ocw.mit.edu", "live.ocw.mit.edu", "doi.org", "physics.nist.gov", "www.usgs.gov", "geomag.bgs.ac.uk"}
        for url in parser.links:
            self.assertEqual(urlparse(url).scheme, "https")
            self.assertIn(urlparse(url).hostname, allowed)
        editorial = "".join(x["html"] for x in LESSONS) + "".join(SOURCES)
        self.assertNotIn("C:\\Users", editorial)
        self.assertNotIn("MemoCPGEScientifAR2027-em.pdf", editorial)

    def test_export_keeps_every_answer_guide_and_source(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            path = export(Path(directory) / "cours.md")
            self.assertIsInstance(path, Path)
            data = path.read_bytes()
            self.assertNotIn(b"\r", data)
            text = data.decode("utf-8")
            for item in LESSONS:
                self.assertIn("## " + item["title"], text)
            for item in EXERCISES:
                self.assertIn("### " + item["title"], text)
                self.assertIn(prose(item["answer"]), text)
            for lab, guide in LAB_GUIDES.items():
                self.assertIn("### Laboratoire `" + lab + "`", text)
                self.assertIn(guide["objects"][0], text)
                self.assertIn(guide["assumptions"][0], text)
            parser = ConstantHTML()
            parser.feed("".join(SOURCES))
            for url in parser.links:
                self.assertIn("](" + url + ")", text)
            self.assertNotIn("<p>", text)
            self.assertNotIn("<div", text)
            self.assertNotIn("Mécanique des fluides — cours", text)


if __name__ == "__main__":
    unittest.main()
