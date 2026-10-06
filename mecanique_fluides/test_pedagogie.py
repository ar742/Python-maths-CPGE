"""Contrats de navigation et galerie scientifique ; aucune dépendance graphique.

Les lois et leurs limites sont contrôlées dans test_modeles.py. Ici, les tests
garantissent que le cours, les missions et les légendes conduisent à de vrais TP,
et que les illustrations publiées restent des documents vectoriels autonomes.
"""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

from catalogue import LABS
import cours


ROOT = Path(__file__).resolve().parent
GALLERY = ROOT / "illustrations"
LAB_IDS = {item["id"] for item in LABS}
SVG = "{http://www.w3.org/2000/svg}"
DC = "{http://purl.org/dc/elements/1.1/}"
PRIMARY_DOMAINS = {"www.education.gouv.fr", "cache.media.education.gouv.fr",
                   "ocw.mit.edu", "live.ocw.mit.edu", "www.claymath.org",
                   "magnetohydrodynamics.physics.wisc.edu", "cpp.openfoam.org"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.targets.extend(value for key, value in attrs if key == "href")


def markdown_targets(text):
    return re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text)


class GalleryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.figures = json.loads((GALLERY / "catalogue.json").read_text(encoding="utf-8"))

    def test_metadata_routes_cover_all_labs(self):
        self.assertGreaterEqual(len(self.figures), 12)
        covered = set()
        files = set()
        for figure in self.figures:
            with self.subTest(figure=figure):
                self.assertTrue({"file", "title", "caption", "labs"} <= figure.keys())
                filename = figure["file"]
                self.assertEqual(Path(filename).name, filename)
                self.assertEqual(Path(filename).suffix, ".svg")
                self.assertNotIn(filename, files)
                self.assertTrue(figure["title"].strip())
                self.assertTrue(figure["caption"].strip())
                self.assertTrue(figure["labs"])
                self.assertTrue(set(figure["labs"]) <= LAB_IDS)
                files.add(filename)
                covered.update(figure["labs"])
        self.assertEqual(covered, LAB_IDS)
        self.assertEqual(files, {path.name for path in GALLERY.glob("*.svg")})

    def test_svg_metadata_matches_navigation_caption(self):
        for figure in self.figures:
            with self.subTest(file=figure["file"]):
                svg = ET.parse(GALLERY / figure["file"]).getroot()
                self.assertEqual(svg.tag, SVG + "svg")
                self.assertEqual(svg.findtext(SVG + "title"), figure["title"])
                description = svg.find(".//" + DC + "description")
                self.assertIsNotNone(description)
                self.assertEqual(description.text, figure["caption"] +
                                 " Laboratoires : " + ", ".join(figure["labs"]))

    def test_svg_is_vector_selectable_and_self_contained(self):
        for figure in self.figures:
            with self.subTest(file=figure["file"]):
                svg = ET.parse(GALLERY / figure["file"]).getroot()
                view = [float(value) for value in svg.attrib["viewBox"].split()]
                self.assertEqual(len(view), 4)
                self.assertGreater(view[2], 0)
                self.assertGreater(view[3], 0)
                self.assertFalse(svg.findall(".//" + SVG + "image"))
                self.assertFalse(svg.findall(".//" + SVG + "script"))
                # Axes, courbes et légendes doivent subsister hors du site.
                self.assertGreaterEqual(len(svg.findall(".//" + SVG + "path")), 10)
                texts = ["".join(element.itertext()).strip()
                         for element in svg.findall(".//" + SVG + "text")]
                self.assertGreaterEqual(sum(bool(value) for value in texts), 8)
                ids = {element.attrib["id"] for element in svg.iter() if "id" in element.attrib}
                for element in svg.iter():
                    for key, value in element.attrib.items():
                        if key.endswith("href"):
                            self.assertTrue(value.startswith("#"), msg=value)
                            self.assertIn(value[1:], ids)
                        for identifier in re.findall(r"url\(#([^)]*)\)", value):
                            self.assertIn(identifier, ids)

    def test_figures_have_distinct_vector_content(self):
        digests = {hashlib.sha256((GALLERY / figure["file"]).read_bytes()).digest()
                   for figure in self.figures}
        self.assertEqual(len(digests), len(self.figures))

    def test_gallery_document_references_every_export(self):
        text = (GALLERY / "README.md").read_text(encoding="utf-8")
        references = set(markdown_targets(text))
        self.assertEqual(references, {figure["file"] for figure in self.figures})


class PedagogicalNavigationTests(unittest.TestCase):
    def test_course_and_exercise_buttons_have_actual_destinations(self):
        groups = [("cours", cours.LESSONS), ("exercices", cours.EXERCISES)]
        for name, group in groups:
            seen_titles = set()
            covered = set()
            for item in group:
                with self.subTest(group=name, title=item["title"]):
                    self.assertIn(item["lab"], LAB_IDS)
                    self.assertNotIn(item["title"], seen_titles)
                    seen_titles.add(item["title"])
                    covered.add(item["lab"])
            self.assertEqual(covered, LAB_IDS, msg=f"TP sans entrée depuis {name}")

    def test_embedded_course_links_point_to_primary_sources(self):
        links = Links()
        for item in cours.LESSONS:
            links.feed(item["html"])
        for item in cours.EXERCISES:
            links.feed(item["question"])
            links.feed(item["answer"])
        for source in cours.SOURCES:
            links.feed(source)
        self.assertTrue(links.targets)
        for target in links.targets:
            with self.subTest(target=target):
                parsed = urlsplit(target)
                self.assertEqual(parsed.scheme, "https")
                self.assertIn(parsed.hostname, PRIMARY_DOMAINS)

    def test_eight_missions_cover_actual_labs(self):
        text = (ROOT / "PARCOURS.md").read_text(encoding="utf-8")
        missions = re.split(r"(?m)^## Mission [1-8] — ", text)[1:]
        self.assertEqual(len(missions), 8)
        covered = set()
        for mission in missions:
            route = re.search(r"\*\*Laboratoires? :\*\* ([^\n]*)", mission)
            self.assertIsNotNone(route)
            ids = re.findall(r"`([a-z_]+)`", route.group(1))
            self.assertTrue(ids)
            self.assertTrue(set(ids) <= LAB_IDS)
            covered.update(ids)
        self.assertEqual(covered, LAB_IDS)

    def test_documentation_links_resolve_locally_or_to_primary_sources(self):
        for filename in ("PARCOURS.md", "ERRATA.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            targets = markdown_targets(text)
            self.assertTrue(targets)
            for target in targets:
                with self.subTest(document=filename, target=target):
                    parsed = urlsplit(target)
                    if parsed.scheme:
                        self.assertEqual(parsed.scheme, "https")
                        self.assertIn(parsed.hostname, PRIMARY_DOMAINS)
                    else:
                        self.assertTrue((ROOT / parsed.path).is_file())

    def test_public_gallery_contains_no_private_pdf_copy(self):
        self.assertFalse(list(GALLERY.glob("*.pdf")))
        self.assertFalse(list(GALLERY.glob("*.png")))
        self.assertFalse(list(GALLERY.glob("*.jpg")))


if __name__ == "__main__":
    unittest.main()
