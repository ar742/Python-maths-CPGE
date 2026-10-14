# Algèbre & Réductions : un parcours progressif sup / spé

Commencer par les systèmes et les changements de base. En spé, utiliser le spectre et les polynômes d’une matrice pour expliquer sa dynamique. Les structures de Lie et les grandes classifications viennent ensuite, au choix.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Si deux TP sont associés, le second sert de comparaison ou de travail personnel. Les branches facultatives peuvent occuper plusieurs séances.

Repères MPSI et MP. « Incontournable » désigne les techniques de la séance, pas tous les résultats du TP. La classification de Jordan, la décomposition de Dunford, la forme de Frobenius, les algèbres de Lie et le pfaffien sont des prolongements, même si leurs premiers calculs utilisent des outils de CPGE.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : systèmes linéaires, matrices, applications linéaires, image, noyau, rang et déterminant.
- Sup : bases, sommes directes, produit scalaire, projection orthogonale et division polynomiale.
- Spé : valeurs propres, diagonalisation, polynômes annulateurs et théorème spectral; polynôme minimal et décomposition des noyaux en MP.

## Pour chaque séance

1. Lire le but, les objets et les hypothèses avant de modifier un réglage.
2. Prévoir un résultat sur papier, puis comparer à la figure ou au certificat calculé.
3. Faire varier un seul paramètre et justifier ce qui change.
4. Conclure par une preuve courte : résultat, hypothèses et portée de l’expérience.

## Sup : quatre séances de calcul et de géométrie

Distinguer une transformation des vecteurs, un changement de base et une opération sur les équations.

### 1. Composer, inverser et lire un déterminant

**Techniques incontournables** · Sup · calcul matriciel

Comprendre l’ordre d’une composition et relier déterminant, volume et perte de dimension.

**À faire :** Choisir deux transformations du cube. Comparer leurs deux ordres, suivre un sommet et prévoir le signe du déterminant. Tester ensuite une transformation singulière.

**Acquis attendu :** Écrire le produit dans le bon ordre; distinguer matrice inversible et matrice de rang insuffisant.

**Limites et compléments :** L’action d’un groupe sert d’interprétation. Aucune théorie des groupes de Lie n’est nécessaire.

**TP associés :** Agir dans l’espace : volume, orientation, composition

### 2. Résoudre et certifier un système

**Techniques incontournables** · Sup · pivot, noyau et image

Décrire toutes les solutions, ou prouver qu’il n’en existe aucune.

**À faire :** Comparer un système compatible à un système incompatible. Refaire les premières opérations de Gauss et lire les colonnes pivots. Vérifier une solution puis les vecteurs du noyau.

**Acquis attendu :** Écrire l’ensemble des solutions comme une solution particulière plus le noyau; contrôler le théorème du rang.

**Limites et compléments :** Le calcul exact est prioritaire. Conditionnement et erreurs d’arrondi sont des compléments numériques.

**TP associés :** Gauss : rang, noyau et systèmes

### 3. Décomposer sans confondre les projections

**Techniques incontournables** · Sup · sommes directes et espaces euclidiens

Caractériser un projecteur par son image et son noyau; reconnaître quand il est orthogonal.

**À faire :** Choisir le mode projection oblique. Décomposer le vecteur, vérifier que projeter deux fois donne le même résultat, puis comparer la direction de projection à une perpendiculaire.

**Acquis attendu :** Justifier la somme directe et l’identité de projecteur; ne pas attribuer à une projection oblique une propriété de distance minimale.

**Limites et compléments :** La construction de projecteurs par Bézout sera reprise en spé. Les projecteurs primaires restent facultatifs.

**TP associés :** Décomposer un espace avec des projecteurs

### 4. Inverser dans le bon ensemble

**Techniques incontournables** · Sup · déterminant et inverse

Maîtriser l’inversibilité sur un corps avant d’explorer les coefficients entiers ou modulaires.

**À faire :** Commencer dans les rationnels avec une matrice non singulière. Vérifier le produit avec son inverse. Puis comparer aux entiers : expliquer pourquoi un inverse rationnel peut sortir de l’ensemble autorisé.

**Acquis attendu :** Employer det non nul sur un corps; identifier précisément l’obstacle quand les coefficients de l’inverse ne sont plus autorisés.

**Limites et compléments :** Le théorème sur GLₙ d’un anneau commutatif est fourni en approfondissement; il ne remplace pas le critère étudié sur un corps.

**TP associés :** Le déterminant doit être une unité

## Spé : trois séances pour choisir un invariant

Les calculs deviennent des preuves de réduction et des méthodes pour éviter les multiplications inutiles.

### 5. Valeurs propres et diagonalisation

**Techniques incontournables** · Spé · réduction

Décider une diagonalisation en examinant les espaces propres, pas seulement la liste des valeurs propres.

**À faire :** Comparer deux familles proposées. Calculer un noyau associé à une valeur propre et compter les dimensions des espaces propres. Expliquer un échec de diagonalisation.

**Acquis attendu :** Construire une base de vecteurs propres quand elle existe; distinguer multiplicité d’une racine et dimension de l’espace propre.

**Limites et compléments :** S’arrêter au critère de diagonalisation et aux noyaux. Les chaînes et la classification de Jordan sont réservées aux prolongements.

**TP associés :** Spectre, Jordan et choix du corps

### 6. Réduire une grande puissance

**Techniques incontournables** · Spé MP · polynômes annulateurs

Calculer une puissance matricielle par division euclidienne et Cayley–Hamilton.

**À faire :** Choisir la matrice dense et une puissance élevée. Utiliser le polynôme caractéristique fourni pour réduire la puissance, puis vérifier l’égalité matricielle. Comparer une réduction par le polynôme minimal quand il est disponible.

**Acquis attendu :** Expliquer pourquoi le reste polynomial donne la même matrice et pourquoi changer de base conserve le polynôme caractéristique.

**Limites et compléments :** Les identités générales entre traces et coefficients et l’algorithme de Faddeev–LeVerrier sont des compléments fournis.

**TP associés :** De la trace aux puissances d’une matrice

### 7. Lire le signe d’une forme quadratique

**Techniques incontournables** · Spé · matrices symétriques et théorème spectral

Relier les valeurs propres d’une matrice symétrique au signe de sa forme quadratique.

**À faire :** Comparer les cas positif, indéfini et dégénéré. Suivre les lignes de niveau et vérifier les signes sur des vecteurs. Écrire le changement orthonormé qui explique la figure.

**Acquis attendu :** Distinguer congruence pour une forme et similitude pour un endomorphisme; expliquer un vecteur non nul de valeur quadratique nulle.

**Limites et compléments :** La loi d’inertie générale est un prolongement. Le socle est le théorème spectral et l’usage des valeurs propres pour la positivité.

**TP associés :** Changer de base pour une forme quadratique

## Deux approfondissements avec les outils de CPGE

Les objets nouveaux sont définis dans le TP; les preuves utilisent rang, noyau, positivité et réduction.

### A1. Une dynamique engendrée par un vecteur

**Approfondissement CPGE** · Sup / spé · application guidée

Construire une famille par applications successives et reconnaître le sous-espace qu’elle engendre.

**À faire :** Comparer un vecteur propre à un vecteur témoin cyclique. Contrôler le rang de la famille obtenue et la récurrence affichée. En MP, reprendre les projecteurs construits par Bézout.

**Acquis attendu :** Relier une dépendance linéaire à une récurrence; justifier la décomposition des noyaux par des polynômes premiers entre eux.

**Limites et compléments :** Le nom Krylov, le critère général de cyclicité et le calcul du commutant ne sont pas des exigences supplémentaires.

**TP associés :** Un vecteur peut engendrer toute la dynamique ; Décomposer un espace avec des projecteurs

### A2. Matrices, probabilités et diffusion

**Approfondissement CPGE** · Spé · applications de la réduction

Interpréter noyau, positivité et modes lents dans deux modèles concrets.

**À faire :** Couper le pont du réseau puis le rétablir. Comparer les noyaux du Laplacien et l’évolution du signal. Dans la chaîne de Markov, vérifier conservation de la somme et loi stationnaire.

**Acquis attendu :** Établir le bilan conservé et relier les changements de noyau ou d’espace propre à la séparation des groupes.

**Limites et compléments :** Les théorèmes généraux de Markov, Fiedler, Kirchhoff et de vitesse de mélange sont des prolongements; une expérience finie ne les démontre pas.

**TP associés :** Le pont d'un réseau se lit dans son Laplacien ; Six états : circuler, mélanger, converger

## Trois branches au-delà du programme

Choisir une branche après le socle. Vérifier les certificats du TP avant de chercher une théorie générale.

### P1. Jordan, Dunford et Frobenius

**Au-delà du programme** · Au-delà · classification et calcul matriciel

Comprendre ce que le seul polynôme caractéristique ne distingue pas.

**À faire :** Comparer les accroissements des noyaux, puis vérifier la décomposition proposée par Dunford et la commutation de ses deux parties. Comparer enfin deux formes de Frobenius de même polynôme caractéristique.

**Acquis attendu :** Expliquer le rôle de chaque invariant et vérifier les changements de base ou polynômes fournis.

**Limites et compléments :** Les théorèmes généraux de ces trois classifications ne sont pas exigibles en MPSI / MP.

**TP associés :** Spectre, Jordan et choix du corps ; Séparer la partie semi-simple et la nilpotente ; Les facteurs invariants organisent la matrice

### P2. Du commutateur aux représentations de Lie

**Au-delà du programme** · Au-delà · structures et actions

Passer d’un défaut de commutation à une action d’opérateurs sur des polynômes.

**À faire :** Développer les trois termes de Jacobi, puis vérifier les relations sur une base de monômes. Comparer deux petites rotations et leur commutateur. Revenir aux anneaux pour le rôle des éléments inversibles.

**Acquis attendu :** Séparer une identité accessible par développement de la définition et de la théorie d’une algèbre de Lie.

**Limites et compléments :** L’exponentielle matricielle est un outil du programme MP. Les représentations irréductibles et le passage global de l’algèbre au groupe sont des prolongements accompagnés.

**TP associés :** Du groupe à son algèbre de Lie ; Jacobi : trois contributions qui se compensent ; sl2 agit sur les polynômes homogènes ; Le déterminant doit être une unité

### P3. Pfaffien et mécanique symplectique

**Au-delà du programme** · Au-delà · formes alternées et invariants

Distinguer conservation du volume et conservation de la forme symplectique.

**À faire :** Contrôler le carré du pfaffien sur une matrice antisymétrique de taille paire. Comparer ensuite une transformation symplectique à celle de déterminant 1 proposée comme contre-exemple.

**Acquis attendu :** Expliquer pourquoi un déterminant égal à 1 ne suffit pas; interpréter séparément énergie, volume et forme conservée.

**Limites et compléments :** Pfaffien, produit extérieur et intégrateurs hamiltoniens sont hors programme; leurs définitions et certificats restent fournis.

**TP associés :** Un déterminant est le carré d’un pfaffien ; Conserver la forme symplectique, pas seulement le volume

## Repères de programme

- [Programme de mathématiques MPSI / MP2I](https://prepas.org/ups.php?document=69)
- [Programme de mathématiques MP](https://prepas.org/ups.php?document=85)
