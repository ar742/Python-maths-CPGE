"""Cohérence de l'atlas organique : navigation, chimie et documents livrés."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest

from reactions_recueil import REACTIONS, REACTION_BY_ID
from cours_recueil import LESSONS, EXERCISES, LAB_GUIDES
from export_reactions import export, safe
from export_cours import prose


ROOT = Path(__file__).resolve().parent


class Fragment(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"p", "b", "div", "br"}:
            self.errors.append(tag)
        if tag != "br":
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            self.errors.append(tag)


class AtlasReactionsTests(unittest.TestCase):
    def test_targeted_pages_and_mechanisms_are_all_navigable(self):
        self.assertEqual(len(REACTIONS), len(REACTION_BY_ID))
        self.assertEqual({r["page"] for r in REACTIONS}, {524, 525, 526, 527, 528, 531, 532, 533, 534})
        self.assertTrue({"AB", "AE", "AN", "AE-addition-élimination", "E1", "E2", "SN1", "SN2", "SEA", "OR"}.issubset({r["family"] for r in REACTIONS}))
        for item in REACTIONS:
            with self.subTest(reaction=item["id"]):
                self.assertTrue(item["lab"], "Chaque vraie transformation a une expérience disponible")
                self.assertTrue(item["params"])
                for field in ("changes", "selectivity", "characterization", "mechanism"):
                    self.assertTrue(item[field])
                self.assertGreater(len(item["question"]), 25)
                self.assertGreater(len(item["answer"]), 80)

    def test_every_additional_lab_has_course_experiments_and_two_problems(self):
        ids = {item["lab"] for item in LESSONS}
        self.assertEqual(set(LAB_GUIDES), ids)
        self.assertEqual(Counter(item["lab"] for item in EXERCISES), Counter({key: 2 for key in ids}))
        for key, item in LAB_GUIDES.items():
            self.assertEqual(len(item["first_steps"]), 3)
            self.assertEqual(set(item["levels"]), {"sup", "spe", "beyond"})
            self.assertTrue(item["objects"] and item["assumptions"])
            self.assertIn(key, {LESSONS[i - 1]["lab"] for i in item["lesson_numbers"]})

    def test_source_stereochemistry_is_explicit_and_does_not_claim_a_ratio(self):
        e = REACTION_BY_ID["e2_source_e"]
        z = REACTION_BY_ID["e2_source_z"]
        self.assertEqual(e["params"]["configuration"], "SS")
        self.assertEqual(z["params"]["configuration"], "SR")
        self.assertIn("(E)", e["product"])
        self.assertIn("(Z)", z["product"])
        self.assertEqual(e["params"]["beta"], z["params"]["beta"])
        self.assertIn("régioisomères", " ".join(e["selectivity"]))
        self.assertIn("Et", e["characterization"][0])

    def test_vector_and_reduction_examples_preserve_their_scientific_domains(self):
        reduction = REACTION_BY_ID["nitro_reduction"]
        self.assertIn("6 H⁺ + 6 e⁻", " ".join(reduction["selectivity"]))
        self.assertIn("2 H₂O", " ".join(reduction["selectivity"]))
        dipole = REACTION_BY_ID["nitro_dipoles"]
        self.assertIn("√3 μ₀", dipole["product"])
        self.assertIn("60°", dipole["selectivity"][0])
        self.assertIn("120°", dipole["selectivity"][0])
        self.assertIn("180°", dipole["selectivity"][0])
        self.assertIn("loi de mélange", dipole["answer"])

    def test_hcl_and_oxygen_industrial_cards_open_the_exact_reagent(self):
        hcl = REACTION_BY_ID["alcyne_hcl"]
        self.assertEqual(hcl["params"]["reagent"], "hcl2")
        self.assertIn("dichloropropane", hcl["product"])
        silver = REACTION_BY_ID["epoxy_industriel"]
        self.assertEqual(silver["lab"], "epoxydes")
        self.assertEqual(silver["params"]["substrate"], "ethylene")
        self.assertEqual(silver["params"]["mode"], "silver")
        self.assertIn("2 C₂H₄ + O₂", silver["characterization"][0])

    def test_lessons_and_answers_keep_chemistry_readable_in_html(self):
        fragments = [item["html"] for item in LESSONS]
        fragments += [item[key] for item in EXERCISES for key in ("question", "answer")]
        for fragment in fragments:
            parser = Fragment()
            parser.feed(fragment)
            parser.close()
            self.assertEqual(parser.errors, [])
            self.assertEqual(parser.stack, [])
        for item in LESSONS:
            self.assertGreaterEqual(item["html"].count("<p>"), 4)
            self.assertIn("class='formula'", item["html"])
            self.assertGreater(len(prose(item["html"])), 1000)
        for item in EXERCISES:
            self.assertGreater(len(prose(item["question"])), 100)
            self.assertGreater(len(prose(item["answer"])), 500)

    def test_export_has_every_product_every_answer_and_no_stale_snapshot(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            path = export(Path(directory) / "atlas.md")
            data = path.read_bytes()
            self.assertNotIn(b"\r", data)
            text = data.decode("utf-8")
            for item in REACTIONS:
                self.assertIn(item["id"], text)
                self.assertIn(safe(item["product"]), text, item["id"])
                self.assertIn(safe(item["question"]), text, item["id"])
            for item in EXERCISES:
                self.assertIn(prose(item["answer"]), text)
            self.assertEqual(data, (ROOT / "REACTIONS_DU_RECUEIL.md").read_bytes())

    def test_all_paths_have_a_chemical_deliverable(self):
        text = (ROOT / "PARCOURS_REACTIONS.md").read_text(encoding="utf-8")
        self.assertEqual(text.count("## Parcours "), 8)
        self.assertEqual(text.count("**Livrable :**"), 8)
        for key in LAB_GUIDES:
            self.assertIn("`" + key + "`", text)


if __name__ == "__main__":
    unittest.main()
