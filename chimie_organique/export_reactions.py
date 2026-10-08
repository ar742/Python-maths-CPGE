"""Exporter l'atlas et les compléments organiques (bibliothèque standard seule)."""

from pathlib import Path
from collections import Counter

from reactions_recueil import REACTIONS
from cours_recueil import LESSONS, EXERCISES, LAB_GUIDES
from export_cours import prose


def bullets(items):
    return "\n".join("- " + safe(item) for item in items)


def safe(text):
    return str(text).replace("[", r"\[").replace("]", r"\]")


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name("REACTIONS_DU_RECUEIL.md")
    pages = Counter(item["page"] for item in REACTIONS)
    parts = [
        "# Chimie organique — atlas des réactions du recueil",
        f"**{len(REACTIONS)} fiches de transformations et de règles**, centrées sur les pages imprimées **524 à 528**, puis **531 à 534**. Cet atlas est l’entrée de lecture pour les types de réactions, leurs produits, leurs règles et leurs mécanismes. Les textes et schémas du programme sont originaux ; les pages du document source ne sont pas redistribuées.",
        "[Parcours guidés de réactions](PARCOURS_REACTIONS.md) · [Présentation et lancement](README.md) · [Cours initial et outils complémentaires](COURS.md)",
        "Une fiche se lit dans l’ordre **substrat → conditions → produits → liaisons modifiées → sélectivité → caractérisation du produit → étapes → question corrigée**. « Caractériser » désigne ici reconnaître la fonction, la connectivité, les charges et la stéréochimie issues d’une transformation. IR, RMN, CCM et autres outils restent des compléments pour vérifier des propositions de produits.",
        "Les familles désignent l’échelle annoncée : **AB** transfert acido-basique ; **AE** addition électrophile ; **AN** addition nucléophile ; **addition–élimination** substitution acyle ; **OR** oxydoréduction ; **E1/E2** éliminations ; **SN1/SN2** substitutions nucléophiles ; **SEA** substitution électrophile aromatique. Une transformation globale peut réunir plusieurs actes, par exemple AE, AN et AB pour l’hydratation acide. Le code AE seul n’est donc jamais employé ici pour masquer une addition–élimination acyle.",
        "Les règles sont accompagnées de leur domaine : Markovnikov par un chemin ionique approprié, anti-Markovnikov par un autre mécanisme, Zaïtsev seulement après avoir vérifié les voies accessibles, orientation aromatique distincte de l’activation. Aucune propriété d’une espèce pure ni borne de stœchiométrie n’est transformée en proportion expérimentale ou rendement universel.",
        "## Repères de pages",
        "| Page imprimée | Fiches de l’atlas | Centre du travail |\n| --- | ---: | --- |\n" + "\n".join(
            f"| {page} | {pages[page]} | " + next(item["rubric"] for item in REACTIONS if item["page"] == page) + " |"
            for page in sorted(pages)),
    ]
    current = None
    for index, item in enumerate(sorted(REACTIONS, key=lambda item: item["page"]), 1):
        if item["page"] != current:
            current = item["page"]
            parts.append(f"## Page {current} — {item['rubric']}")
        parts.extend([
            f"### Fiche {index} — {item['title']}",
            f"**Famille :** {item['family']} · **Niveau :** {item['level']} · **Identifiant :** `{item['id']}`",
            "**Substrat.** " + safe(item["substrate"]),
            "**Réactifs et conditions.** " + safe(item["reagents"]),
            "**Produit / bilan.** " + safe(item["product"]),
            "**Liaisons et fonctions modifiées**\n\n" + bullets(item["changes"]),
            "**Règles et sélectivité**\n\n" + bullets(item["selectivity"]),
            "**Caractérisation du produit**\n\n" + bullets(item["characterization"]),
            "**Étapes à reconstruire**\n\n" + "\n".join(f"{n}. {safe(step)}" for n, step in enumerate(item["mechanism"], 1)),
            "**Expérience.** Dans l’application, la fiche ouvre le laboratoire `" + item["lab"] + "` et son scénario. Paramètres : `" + ", ".join(f"{key}={value}" for key, value in item["params"].items()) + "`.",
        ])
        if item["model_note"]:
            parts.append("**Domaine du modèle.** " + safe(item["model_note"]))
        parts.extend(["**Question.** " + safe(item["question"]), "**Réponse.** " + safe(item["answer"])])
    parts.extend([
        "## Douze approfondissements de cours",
        "Ces douze leçons complètent le cours initial ; leurs numéros ici sont locaux à ce document. L’application les rassemble avec les leçons existantes pour une navigation commune.",
    ])
    for index, item in enumerate(LESSONS, 1):
        parts.extend([f"### Leçon complémentaire {index} — {item['title']}",
                      f"*{item['level']}* · laboratoire `{item['lab']}`.",
                      prose(item["html"])])
    parts.append("## Douze introductions d’expériences")
    for lab, item in LAB_GUIDES.items():
        parts.extend([
            f"### Laboratoire `{lab}`", item["purpose"],
            "**Objets et unités**\n\n" + bullets(item["objects"]),
            "**Hypothèses**\n\n" + bullets(item["assumptions"]),
            "**Techniques**\n\n" + bullets(item["techniques"]),
            "**Prédire → expérimenter → justifier**\n\n" + "\n".join(f"{i}. {safe(step)}" for i, step in enumerate(item["first_steps"], 1)),
            "**Niveaux**\n\n" + bullets(["Sup : " + item["levels"]["sup"], "Spé : " + item["levels"]["spe"], "Au-delà : " + item["levels"]["beyond"]]),
            "Leçons complémentaires : " + ", ".join(map(str, item["lesson_numbers"])) + ".",
            "**Résultat attendu.** " + item["expected"],
        ])
    parts.append("## Vingt-quatre problèmes corrigés de réactions")
    for index, item in enumerate(EXERCISES, 1):
        parts.extend([f"### Problème complémentaire {index} — {item['title']}",
                      f"*{item['level']}* · laboratoire `{item['lab']}`.",
                      prose(item["question"]), prose(item["answer"])])
    parts.append("## Sources et statut pédagogique")
    parts.append("La lecture suit les pages ciblées du recueil fourni. Les programmes officiels, les références de définitions IUPAC et les sources institutionnelles de méthodes sont détaillés dans [COURS.md](COURS.md). PCSI puis PC/PC* constituent le parcours principal ; les réactions de banque accompagnée et les prolongements ne sont pas déclarés exigibles uniformément dans toutes les filières. Dans les niveaux au-delà, les thèmes sont proposés comme ouverture et ne sont pas promis par les calculs du laboratoire.")
    path.write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
    return path


if __name__ == "__main__":
    print(export())
