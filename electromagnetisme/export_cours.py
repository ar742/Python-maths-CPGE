"""Exporter le cours et les corrigés : python export_cours.py (stdlib seule)."""

from pathlib import Path
import html
import re

from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


def prose(value):
    """Garder les liens, les formules et les séparations de paragraphes."""
    value = re.sub(
        r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",
        lambda m: "[" + re.sub(r"<[^>]*>", "", m.group(2)) + "](" + m.group(1) + ")",
        value, flags=re.DOTALL)
    value = re.sub(r"<br\s*/?>", "  \n", value)
    value = re.sub(r"<(?:p|div)[^>]*>", "", value)
    value = re.sub(r"</(?:p|div)>", "\n\n", value)
    value = value.replace("<b>", "**").replace("</b>", "**")
    return html.unescape(re.sub(r"<[^>]*>", "", value)).strip()


def bullets(items):
    return "\n".join("- " + item for item in items)


def numbers(items):
    return "\n".join(str(i) + ". " + item for i, item in enumerate(items, 1))


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name("COURS.md")
    parts = [
        "# Électromagnétisme — cours, expériences et exercices corrigés",
        "36 leçons, 24 laboratoires et 48 exercices intégralement corrigés. Les dix missions transversales sont dans [PARCOURS.md](PARCOURS.md).",
        "Convention commune : les champs réels sont Re[Ã exp(−iωt)], les ondes vers +z exp(ikz−iωt), les amplitudes harmoniques sont crête sauf mention efficace. Pour une branche passive dans un demi-espace +z, Im(k)≥0. μ₀≈4π×10⁻⁷ H·m⁻¹ est une approximation numérique.",
        "Sup et Spé désignent les outils mobilisés, avec un statut dépendant de la filière. Rails de Laplace, induction et bilans offrent des entrées de première année ; le champ électromoteur général n’est pas exigible en MPSI. Le programme PSI traite explicitement matériaux magnétiques, transformateur et machine synchrone. Circuit équivalent asynchrone, London, Faraday tensoriel, Kerr localisé et dynamo α² sont ici des prolongements accompagnés, sans assimilation à un programme commun obligatoire.",
    ]
    for item in LESSONS:
        parts.extend(["## " + item["title"], "*" + item["level"] + "* — laboratoire `" + item["lab"] + "`.", prose(item["html"])])
    parts.append("## Les 24 introductions de laboratoire")
    for lab, item in LAB_GUIDES.items():
        parts.extend([
            "### Laboratoire `" + lab + "`", item["purpose"],
            "**Objets et unités**", bullets(item["objects"]),
            "**Hypothèses de l’expérience**", bullets(item["assumptions"]),
            "**Techniques à mobiliser**", bullets(item["techniques"]),
            "**Prédire → expérimenter → justifier**", numbers(item["first_steps"]),
            "**Niveaux et approfondissements**", bullets([
                "Sup : " + item["levels"]["sup"], "Spé : " + item["levels"]["spe"],
                "Au-delà : " + item["levels"]["beyond"]]),
            "Leçons de référence : " + ", ".join(map(str, item["lesson_numbers"])) + ".",
            "**Résultat attendu.** " + item["expected"],
        ])
    parts.append("## Les 48 exercices corrigés")
    for item in EXERCISES:
        parts.extend(["### " + item["title"], "*" + item["level"] + "* — laboratoire `" + item["lab"] + "`.", prose(item["question"]), prose(item["answer"])])
    parts.extend(["## Sources primaires et programmes", bullets([prose(source) for source in SOURCES])])
    path.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    if path.resolve().parent == Path(__file__).resolve().parent:
        parcours = Path(__file__).with_name('PARCOURS.md')
        marker = '<!-- reperes-laboratoires -->'
        original = parcours.read_text(encoding='utf-8').split(marker, 1)[0].rstrip()
        overview = [marker, '## Repères pour choisir une expérience', '', 'Le cours exporté reprend les variables et hypothèses de chaque guide. Les indications de filière ci-dessous distinguent les techniques du programme et les prolongements.', '']
        for lab, guide in LAB_GUIDES.items():
            overview.extend(['### '+lab, '', guide['purpose'], '', '**Spé et filières.** '+guide['levels']['spe'], '', '**Prolongements.** '+guide['levels']['beyond'], ''])
        parcours.write_text(original+'\n\n'+'\n'.join(overview), encoding='utf-8', newline='\n')
    return path


if __name__ == "__main__":
    print(export())
