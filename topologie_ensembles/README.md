# Topologie & Ensembles · CPGE sup / spé

**Atelier 13 · septième volet de mathématiques.**

![Du voisinage aux ensembles limites](apercu.png)

**30 laboratoires interactifs, 60 leçons, 60 exercices corrigés et 30 figures scientifiques originales**, fondés sur la fiche **M1**, pages **12 à 25** du recueil de A. R. Les laboratoires explicitent le but, les objets, les variables, les hypothèses et les techniques du cours avant la manipulation. Les repères **Sup / Spé / au-delà** précisent la progression selon la filière.

## Démarrer

Sous Windows, double-cliquer sur **Lancer_Topologie.cmd**, à la racine du dépôt ou dans ce dossier. Python **3.10 ou plus récent** est nécessaire ; le lanceur prépare un environnement et installe NumPy si besoin.

Sous Linux ou macOS, depuis ce dossier :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python topologie_ensembles.py
```

Le navigateur s’ouvre sur **http://127.0.0.1:8777**. Garder le serveur ouvert pendant les manipulations ; `Ctrl+C` le ferme. Un autre port se choisit avec `--port 8782`. Le laboratoire fonctionne hors ligne après installation des dépendances. GitHub présente le programme et les cours ; l’application Python fonctionne localement.

## Les définitions deviennent des expériences

| Question | Objets manipulés et critère démontré |
|---|---|
| Qu’est-ce qu’un voisinage ? | Boules des normes 1, 2, ∞ et p ; marge exacte `r−‖x‖`, bord strict ou inclus. |
| Un point absent peut-il être adhérent ? | `{1/n}`, avec ou sans sa limite 0 ; distance exacte à l’ensemble infini. |
| Ouvert, fermé, intérieur et frontière ? | Disque, anneau et disque épointé ; propriété relative dans `[0,1]`. |
| Quelles opérations préservent les ouverts ? | Intersections finies et infinies ; réunion de fermés perdant une limite. |
| Convexe, connexe, connexe par arcs ? | Segments vérifiés analytiquement, plan épointé, anneau, disques et ovales de Cassini. |
| La compacité est-elle visible ? | Sous-suites, recouvrements, extrema, produit de compacts et image continue. |
| Dénombrable signifie-t-il discret ? | Énumération des rationnels, densité de ℚ et de son complémentaire. |
| Un compact peut-il être indénombrable sans intervalle ? | Construction de Cantor, injection ternaire, argument diagonal. |
| Connexe suffit-il pour tracer un chemin ? | Sinus du topologue : compact connexe, mais non connexe par arcs. |
| Quand la dimension change-t-elle la réponse ? | `xⁿ` et non-équivalence de normes ; modes `eⁱⁿˣ/√(2π)` dans une boule non compacte. |
| Comment la topologie agit-elle sur l’algèbre ? | Matrices denses 4×4 à 8×8, norme d’opérateur, GL₄, O₄ et SL₄. |
| À quoi sert la complétude ? | Suites de Cauchy rationnelles convergeant hors de ℚ ; contractions et borne de Banach. |

## Le fil du recueil

- **Pages 15–16 et 19–21 :** normes, boules, voisinages, adhérence, densité, intérieur, frontière, ouverts et fermés ; compacité, complétude, convexité, connexité et continuité.
- **TP page 17 :** extraction de records stricts d’une suite uniforme dans `[0,3]`, indices originaux croissants, simulations reproductibles et loi exacte de la distance à la cible. La simulation est distinguée de la preuve de convergence presque sûre.
- **Page 22 :** progression de synthèse « identifier l’espace, choisir la norme, utiliser la dimension, raisonner par suites, extraire, conclure ».
- **Exercice 6 :** produit de compacts et image continue, avec somme de Minkowski d’une ellipse et d’un segment.
- **Exercice 7 :** chemins dans le plan épointé ; retrait d’un point pour distinguer ℝ et ℝ² à homéomorphisme près.
- **Exercice 8 :** l’ouverture dans l’intersection de deux parties denses ; contre-exemple ℚ et ℝ∖ℚ.
- **Exercice 9 :** boule unité de fonctions non compacte, séparation exacte √2 entre les modes normalisés.

[Douze missions guidées](PARCOURS.md) · [Correspondance détaillée avec la fiche](MATRICE_RECUEIL.md) · [Cours et démonstrations](COURS.md) · [Exercices corrigés](EXERCICES.md).

## Lire correctement les résultats

Un ensemble est défini dans un **espace ambiant**. Être ouvert dans `[0,1]` n’est pas la même propriété qu’être ouvert dans ℝ. Les bords pointillés représentent des points exclus ; un cercle vide signale un point limite absent.

Les critères décisifs sont analytiques : distance à `{1/n}` entier, norme d’une boule, appartenance d’un segment, projection sur un polytope, signe du déterminant, nombre de composantes de Cassini. Les tracés polygonaux et les nuages finis servent à les illustrer. Une étape de Cantor contient encore des intervalles ; elle n’est pas le compact limite.

**Fermé et borné implique compact dans ℝⁿ et ℂⁿ.** Cette équivalence n’est pas appliquée à un espace de fonctions ou à ℚ muni de la distance usuelle. Les contre-exemples et leurs hypothèses sont rédigés dans le cours.

Les résultats se téléchargent en **JSON** avec paramètres, métriques, données graphiques et hypothèses. Les [figures SVG](illustrations/README.md) sont autonomes et réutilisables. L’[errata autorisé](ERRATA.md) se limite aux erreurs de formules vérifiées dans cet extrait.

## Vérifier et réutiliser

```bash
python -X utf8 -m unittest -v test_geometrie test_analyse test_ensembles test_entree test_pedagogie test_serveur
```

Les tests confrontent les résultats à des distances et intégrales indépendantes, des caractérisations variationnelles, des recouvrements stricts et des formules matricielles. GitHub vérifie Windows et Ubuntu avec Python 3.10 et 3.12.

Pour régénérer les figures :

```bash
python -m pip install -r requirements-illustrations.txt
python topologie_ensembles.py --export-illustrations
```

Les fichiers `catalogue_*.py` définissent les expériences, `modeles_*.py` leurs calculs, `cours.py` les leçons et exercices et `reperes.py` leurs introductions. `exporter_cours.py` régénère les deux recueils Markdown. Le PDF source n’est pas distribué dans le dépôt.
