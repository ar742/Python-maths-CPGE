"""Exporter les leçons, les missions et les corrigés : python export_cours.py.

Le document est autonome et conserve les liens des sources primaires.
"""

from pathlib import Path
import html
import re
from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


def prose(value):
    """Convertir les blocs HTML constants du cours en Markdown lisible."""
    value = re.sub(
        r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",
        lambda match: "[" + re.sub(r"<[^>]*>", "", match.group(2)) + "](" + match.group(1) + ")",
        value,
        flags=re.DOTALL,
    )
    value = re.sub(r"<br\s*/?>", "  \n", value)
    value = re.sub(r"<(?:p|div)[^>]*>", "", value)
    value = re.sub(r"</(?:p|div)>", "\n\n", value)
    value = re.sub(r"<h3[^>]*>", "\n### ", value)
    value = value.replace("</h3>", "\n\n")
    value = value.replace("<b>", "**").replace("</b>", "**")
    return html.unescape(re.sub(r"<[^>]*>", "", value)).strip()


def numbered(items):
    return "\n".join(str(index) + ". " + text for index, text in enumerate(items, 1))


def bulleted(items):
    return "\n".join("- " + text for text in items)


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name("COURS.md")
    parts = [
        "# Mécanique des fluides — cours, laboratoires et exercices corrigés",
        "Vingt-huit leçons, dix-huit laboratoires et quarante exercices. Les variables, unités, hypothèses et conventions sont déclarées avant les calculs. Les missions proposent de prédire, expérimenter et justifier.",
        "Les repères Sup et Spé indiquent les outils mobilisés ; les sujets obligatoires dépendent de la filière. Les équations d'Euler et de Navier–Stokes, notamment exclues du programme PSI cité, et certaines approches exclues du programme PC cité sont étudiées comme extensions accompagnées. Se reporter aux textes officiels référencés et au parcours pour choisir les séances.",
    ]
    for item in LESSONS:
        parts.extend([
            "## " + item["title"],
            "*" + item["level"] + "*",
            "Laboratoire : `" + item["lab"] + "`.",
            prose(item["html"]),
        ])
    parts.append("## Les dix-huit missions de laboratoire")
    for lab, guide in LAB_GUIDES.items():
        parts.extend([
            "### " + lab,
            guide["purpose"],
            "\n**Objets et unités.**\n",
            "\n".join("- "+item for item in guide["objects"]),
            "\n**Hypothèses.**\n",
            "\n".join("- "+item for item in guide["assumptions"]),
            "Leçons de référence : " + ", ".join(map(str, guide["lesson_numbers"])) + ".",
            "**Techniques à mobiliser**",
            bulleted(guide["techniques"]),
            "**Prédire → expérimenter → justifier**",
            numbered(guide["first_steps"]),
            "**Entrées et approfondissements**",
            bulleted([
                "Sup : " + guide["levels"]["sup"],
                "Spé : " + guide["levels"]["spe"],
                "Approfondissement : " + guide["levels"]["beyond"],
            ]),
            "**Résultat attendu.** " + guide["expected"],
        ])
    parts.append("## Les quarante exercices corrigés")
    for item in EXERCISES:
        parts.extend([
            "### " + item["title"],
            "*" + item["level"] + "* — laboratoire `" + item["lab"] + "`.",
            prose(item["question"]),
            prose(item["answer"]),
        ])
    parts.extend(["## Sources et conventions", bulleted([prose(source) for source in SOURCES])])
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
    from export_progression import export as export_progression
    export_progression()
    print(export())
