"""Exporter cours, guides et corrigés : python export_cours.py (stdlib seule)."""

from pathlib import Path
import html
import re

from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


def prose(value):
    value = re.sub(r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",
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
        "# Optique — lumière, images et expériences",
        "36 leçons, 24 laboratoires et 48 exercices corrigés. Dix missions transversales se trouvent dans [PARCOURS.md](PARCOURS.md).",
        "Les ateliers réinvestissent les TP et les problèmes de l’extrait Optique du recueil : lentilles, Bessel, lunette, microscope, prisme/goniomètre, Michelson et polarisation ; fibres, mirages, arc-en-ciel, Young, doublet, diffraction, apodisation, réseau, Fabry–Perot et génération non linéaire. Les figures et textes de l’application sont originaux.",
        "Les mentions Sup, Spé et Au-delà indiquent des outils et une progression, avec un statut dépendant de la filière. La conjugaison de Gauss et la mesure sur banc fournissent les entrées Sup. Diffraction, interférences, Michelson et polarisation ne sont pas à attribuer indistinctement à tous les programmes. Jones/Poincaré, ABCD de résonateur, filtrage 4f complet, gain saturé et conversion χ² sont des prolongements accompagnés ; les liens officiels de programmes sont regroupés en fin de document.",
        "Conventions : axe de lentille orienté vers la propagation, p<0 pour un objet réel ; λ₀ est dans le vide, la longueur d’onde de milieu vaut λ₀/n ; sinc u=sin(u)/u et sinc 0=1. Les tableaux Jones utilisent Re[Ẽ exp(−iωt)] et S₃=2Im(Ex*Ey). Les matrices de rayons réduits utilisent (y,nθ) ; le paramètre gaussien q associé à (y,θ) est réduit en q/n pour ces mêmes matrices. Les variables, unités et domaines sont repris au début de chaque expérience.",
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
    return path


if __name__ == "__main__":
    print(export())
