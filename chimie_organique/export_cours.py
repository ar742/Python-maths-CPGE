"""Exporter cours, guides et corrigés : python export_cours.py (stdlib seule)."""

from pathlib import Path
import html
import re

from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


def prose(value):
    links = []

    def keep_link(match):
        label = html.unescape(re.sub(r"<[^>]*>", "", match.group(2)))
        label = label.replace("[", r"\[").replace("]", r"\]")
        url = html.unescape(match.group(1))
        links.append("[" + label + "](" + url + ")")
        return "\x00LINK" + str(len(links)-1) + "\x00"

    value = re.sub(r"<a\s+href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>",
                   keep_link,
                   value, flags=re.DOTALL)
    value = re.sub(r"<br\s*/?>", "  \n", value)
    value = re.sub(r"<(?:p|div)[^>]*>", "", value)
    value = re.sub(r"</(?:p|div)>", "\n\n", value)
    value = value.replace("<b>", "**").replace("</b>", "**")
    value = html.unescape(re.sub(r"<[^>]*>", "", value)).strip()
    # Une concentration [RX](t) est une formule, pas un lien Markdown vers « t ».
    value = value.replace("[", r"\[").replace("]", r"\]")
    for index, link in enumerate(links):
        value = value.replace("\x00LINK" + str(index) + "\x00", link)
    return value


def bullets(items):
    return "\n".join("- " + item for item in items)


def numbers(items):
    return "\n".join(str(i) + ". " + item for i, item in enumerate(items, 1))


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name("COURS.md")
    parts = [
        "# Liaisons & Synthèses — chimie organique CPGE",
        "42 leçons, 30 laboratoires et 60 exercices corrigés. Douze missions transversales se trouvent dans [PARCOURS.md](PARCOURS.md). Le repérage programme/recueil est dans [MATRICE_PROGRAMME.md](MATRICE_PROGRAMME.md).",
        "L’atelier réinvestit l’extrait du recueil : outils électroniques, types de réactions, exemples et suites d’exemples, organomagnésiens, hydrogénation, hydroboration, acylation, énolates, aldol/crotonisation, Michael, Wittig, époxydes, orbitales et Diels–Alder. Les problèmes d’alcènes/alcynes et d’aromatiques deviennent des raisonnements sur conditions, produits, mécanismes et ordre de synthèse. Textes, dessins, simulations et corrigés sont originaux ; les pages du recueil ne sont pas redistribuées.",
        "La progression vise principalement PCSI puis PC/PC*. Le tronc commun PCSI précède les approfondissements de l’option PC ; les chapitres organiques ne sont pas identiques dans toutes les autres filières. Les mentions Sup, PC et Au-delà indiquent le statut de l’outil, non une promesse que toutes les réactions de la réactiothèque sont exigibles sans données. Les transformations supplémentaires du recueil et les extensions numériques sont accompagnées d’une banque, de paramètres ou de règles fournies. Les programmes officiels de 2021 consultés et les sources primaires sont liés en fin de document.",
        "Conventions : flèche pleine pour un doublet, demi-flèche pour un électron ; charges formelles en unités e et charges partielles δ distinctes. Les pKa d’une comparaison d’équilibre appartiennent au même solvant et aux mêmes conditions. Concentrations en mol·L⁻¹, quantités fréquemment en mmol, temps en s, énergies molaires en kJ·mol⁻¹ sauf orbitales en eV ; R=8,314 J·mol⁻¹·K⁻¹. RMN : δ en ppm, J en Hz et fréquence en MHz ; IR : nombre d’onde en cm⁻¹ et T=10⁻ᴬ. Chaque laboratoire expose ses hypothèses et distingue données mesurées, banques de réactions et modèles pédagogiques.",
    ]
    for item in LESSONS:
        parts.extend(["## " + item["title"], "*" + item["level"] + "* — laboratoire `" + item["lab"] + "`.", prose(item["html"])])
    parts.append("## Les 30 introductions de laboratoire")
    for lab, item in LAB_GUIDES.items():
        parts.extend([
            "### Laboratoire `" + lab + "`", item["purpose"],
            "![Illustration scientifique du laboratoire " + lab + "](illustrations/" + lab + ".svg)",
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
    parts.append("## Les 60 exercices corrigés")
    for item in EXERCISES:
        parts.extend(["### " + item["title"], "*" + item["level"] + "* — laboratoire `" + item["lab"] + "`.", prose(item["question"]), prose(item["answer"])])
    parts.extend(["## Sources primaires et programmes", bullets([prose(source) for source in SOURCES])])
    path.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    return path


if __name__ == "__main__":
    print(export())
