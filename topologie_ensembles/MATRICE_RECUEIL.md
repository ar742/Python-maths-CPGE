# Correspondance avec le recueil fourni

Source : fiche M1 **Topologie et ensembles**, pages imprimées **12 à 25** du PDF
fourni par l'utilisateur. Les numéros ci-dessous sont les numéros imprimés, et
non les indices de pages du fichier. Le PDF reste local ; aucun scan, tableau
ou dessin du recueil n'est redistribué. Les cours, exemples, illustrations et
exercices de l'atelier sont rédigés et construits pour cette application.

| Élément du recueil | Laboratoires et prolongements | Technique formatrice |
|---|---|---|
| p.12 : ensembles de nombres, fini, infini, cardinal | `denombrer_rationnels`, `diagonale_cantor`, `ensemble_cantor`, `rationnels_irrationnels` | Énumération par hauteur, injections, contradiction diagonale, distinction cardinal/densité/longueur |
| p.14 : continuité, continuité uniforme, espaces métriques | `heine_continuite`, `distance_ensemble`, `homeomorphisme` | Ordre des quantificateurs, paires de suites témoins, bornes Lipschitz et Hölder |
| p.15 : normes, équivalence, boules, sphères, voisinages | `boules_normes`, `applications_lineaires`, `normes_dimension_infinie` | Rayons témoins, Cauchy–Schwarz, bornes d'opérateur sur matrices denses de dimension 4 à 8 |
| p.15 : adhérence, intérieur, densité, frontière | `interieur_frontiere`, `adherence_suite`, `rationnels_irrationnels` | Définitions par voisinages, fermeture séquentielle, points isolés et points d'accumulation |
| p.15–16 : complétude et exemple rationnel de Héron | `cauchy_rationnels`, `point_fixe` | Fractions exactes, identité d'erreur quadratique, irrationalité par parité, suites de Cauchy |
| p.16 : ouverts, fermés, compacts, convexes, connexes | `topologie_relative`, `operations_ouverts`, `convexite`, `connexite_chemins`, `compacts_recouvrements` | Espace ambiant explicite, contraintes finies/infinies, preuves de segment, séparation et extraction |
| p.16 : GL, SL, groupes orthogonaux/unitaires | `gl_composantes`, `orthogonal_compact` | Déterminant continu, changement de signe impossible sur ℝ, détour complexe, fermeture et bornitude séparées |
| **TP p.17 : suite extraite de valeurs aléatoires de [0,3] vers 1** | **`extraction_aleatoire`**, préparé par `bolzano_weierstrass` | Records sans répétition d'indices, loi exacte du meilleur rapprochement, confiance finie et preuve presque sûre distinguées |
| p.18 : dimension infinie, applications linéaires non continues et compléments Hilbert | `applications_lineaires`, `normes_dimension_infinie`, `boule_non_compacte` | Linéarité sans borne uniforme, familles de degrés non bornés, orthogonalité et défaut de compacité ; les quotients algébriques restent dans le volet d'algèbre |
| p.19 : identités d'ensembles et axiomes de distance | `interieur_frontiere`, `operations_ouverts`, `distance_ensemble` | Complémentation, stabilité des ouverts/fermés, inégalité triangulaire et distance à un ensemble |
| p.20 : dimension finie, normes équivalentes | `boules_normes`, `applications_lineaires`, `normes_dimension_infinie` | Constantes uniformes sur la sphère compacte ; contre-exemple explicite en dimension infinie |
| p.20 : compacts, Borel–Lebesgue/Heine–Borel, valeurs extrêmes, BW | `bolzano_weierstrass`, `compacts_recouvrements`, `valeurs_extremes`, `image_compacte` | Extraire puis garder la limite dans le domaine ; distinguer maximum et supremum |
| p.20 : densité séquentielle | `adherence_suite`, `rationnels_irrationnels` | Construction d'approximants dans chaque voisinage |
| p.21 : convexes et complétude | `convexite`, `projection_convexe`, `cauchy_rationnels` | Produit scalaire, projection exacte, fermeture d'une partie complète |
| p.21 : connexité, chemins, ensembles de matrices diagonalisables | `connexite_chemins`, `gl_composantes` et leçon sur les ensembles étoilés | Chemin par zéro pour les diagonalisables ; signe du déterminant pour les inversibles |
| p.21 : continuité, Heine, TVI, inverse d'une injection compacte | `heine_continuite`, `chemins_niveaux`, `homeomorphisme` | Images réciproques, paires témoins, TVI sur un chemin, images compactes de fermés |
| p.21 : applications linéaires continues, norme d'opérateur | `applications_lineaires` | Continuité en zéro, majoration sur toute la boule, SVD et normes subordonnées |
| **p.22 : infographie récapitulative essentielle** | **Les 30 labos, les 60 leçons et les 12 missions** | Reprendre ses réflexes : annoncer l'espace, choisir la norme, vérifier la dimension, raisonner par suites, conclure avec hypothèses |
| **Exercice 6 p.23, corrigé p.25 : produit et image de deux compacts** | **`image_compacte`**, `enveloppe_convexe`, `valeurs_extremes` | Deux extractions successives avec indices composés, puis continuité ; somme ellipse + segment et fonction d'appui |
| **Exercice 7 p.23, corrigé p.25 : plan épointé et non-homéomorphisme ℝ/ℝ²** | **`connexite_chemins`**, `homeomorphisme` | Deux segments hors de zéro ; comparaison des composantes après retrait d'un point |
| **Exercice 8 p.23, corrigé p.25 : intersection de denses dont un ouvert** | **`operations_ouverts`**, `rationnels_irrationnels` | Deux usages emboîtés de la densité ; contre-exemple ℚ et son complémentaire |
| **Exercice 9 p.23, corrigé p.25 : boule de fonctions non compacte** | **`boule_non_compacte`**, `normes_dimension_infinie` | Modes normalisés, Gram exact, distance √2 et absence de sous-suite de Cauchy |

## Compléments originaux identifiés

- La **projection sur un convexe**, l'enveloppe convexe et les fonctions d'appui
  donnent des exemples constructifs aux définitions et relient la topologie à
  l'optimisation. Les certificats sont analytiques, pas obtenus par le seul maillage.
- **Cantor** et les approximants rationnels/irrationnels donnent des preuves
  distinctes pour fini/dénombrable/non dénombrable, densité et intérieur vide.
- Le **sinus du topologue** montre que connexe n'implique pas connexe par arcs ;
  une coupure graphique finie est explicitement distinguée de l'adhérence infinie.
- Les **niveaux de Cassini** montrent un seuil exact de changement des composantes,
  avec une différence essentielle entre l'inégalité stricte et large au seuil.
- Le **point fixe de Banach** relie complétude, existence, unicité et estimation
  d'erreur ; il est annoncé comme prolongement selon la filière et le niveau.

Les passages d'algèbre générale de p.12–14 et les exercices 1–5 de p.23–25
constituent le contexte de la fiche. Ils sont déjà traités dans les ateliers de
groupes et d'algèbre linéaire du dépôt ; ce volet privilégie la topologie demandée.
L'[errata](ERRATA.md) est limité à une famille de **formules de p.16**, vérifiée
dans son contexte ; aucune remarque éditoriale ou pédagogique n'y figure.
