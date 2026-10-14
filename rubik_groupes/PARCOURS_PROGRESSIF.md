# Rubik & Groupes : un parcours sup / spé

Partir de gestes dont on peut vérifier l’effet, puis passer aux permutations, aux sous-groupes et aux invariants. La résolution sert de terrain d’expérimentation, sans devenir un objectif de vitesse.

Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les approfondissements et les branches au-delà du programme se choisissent ensuite, indépendamment.

Repères MPSI / MP : le socle est la composition, les permutations, la signature et, en MP, les groupes cycliques et sous-groupes engendrés. Le groupe particulier du cube est un exemple fourni. Commutateurs, actions, graphe de Cayley et résolution par phases restent des compléments. Ouvrir une séance ne joue aucun mouvement et conserve le cube sauvegardé.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : applications, bijections, composition et inverse ; calculs de divisibilité et ppcm.
- Fin de sup : permutations, cycles et signature.
- Spé : groupes, sous-groupes engendrés, ordre d’un élément et groupe cyclique.

## Pour chaque séance

1. Lire les objets, les notations et les hypothèses du TP.
2. Prévoir un résultat sur papier, puis ouvrir l’expérience.
3. Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.
4. Conclure par une courte preuve et distinguer résultat exact, approximation et observation.

## Sup : trois séances pour lire et composer

Écrire les calculs avant de jouer les mouvements. La convention est chronologique : RU signifie R puis U.

### 1. Distinguer un mot de son effet

**Techniques incontournables** · Sup · applications et groupe

Vérifier stabilité, associativité, neutre et inverse sur un exemple concret.

**À faire :** Noter R le quart de tour de la face droite et e l’identité. Analyser R, RR, R2 et RRRR ; comparer leurs effets et expliquer pourquoi des mots différents peuvent représenter la même transformation.

**Acquis attendu :** Retrouver R²=R2 et R⁴=e, puis relier l’associativité à la composition des applications.

**Limites et compléments :** Le nombre total de configurations est fourni ; sa démonstration ne fait pas partie de cette première séance.

**TP associés :** Un cube, un groupe ; Lire une transformation

### 2. Annuler une suite de mouvements

**Techniques incontournables** · Sup · inverse d’une composée

Calculer un inverse en changeant l’ordre des facteurs.

**À faire :** Pour le mot R U F2, où U tourne la face du haut et F la face avant, écrire l’inverse sur papier. Analyser ensuite le mot suivi de cet inverse ; jouer la vérification seulement après le calcul.

**Acquis attendu :** Obtenir F2 U' R' et justifier l’identité par associativité, sans supposer la commutation des tours.

**Limites et compléments :** Réduire des facteurs voisins raccourcit parfois un mot ; cela ne prouve pas que le résultat a une longueur minimale.

**TP associés :** Mots et inverses ; Lire une transformation

### 3. Décomposer en cycles et tester la commutation

**Techniques incontournables** · Fin de sup · groupe symétrique

Lire une permutation et comparer deux composées sur les mêmes objets.

**À faire :** Comparer A=R et B=U, puis A=R et B=L, où L est le tour de la face gauche. Décrire un cycle affiché et calculer la signature à partir des longueurs des cycles disjoints.

**Acquis attendu :** Identifier au moins une facette qui distingue RU de UR ; expliquer la commutation de faces opposées par leurs supports disjoints.

**Limites et compléments :** Les cycles des positions des pièces omettent leur orientation. Le calcul de l’ordre complet se fait sur les facettes.

**TP associés :** Cycles et ordre ; L’ordre des gestes ; Lire une transformation ; Comparer et construire

## Spé : trois séances pour construire des preuves

Passer du calcul d’un exemple à une propriété du sous-groupe engendré.

### 4. Ordre et sous-groupe cyclique

**Techniques incontournables** · Spé · ordre et génération

Relier les cycles d’une permutation à l’ordre de l’élément et à ses puissances.

**À faire :** Noter g l’effet du mot RU. À partir des cycles des facettes, calculer leur ppcm ; retrouver l’ordre 105 et déterminer combien d’éléments contient le sous-groupe engendré par g.

**Acquis attendu :** Justifier gᵏ=e si et seulement si 105 divise k, sans jouer 105 répétitions.

**Limites et compléments :** Le groupe cyclique engendré par un élément est au programme MP ; sa présence dans le cube est l’exemple du TP.

**TP associés :** Cycles et ordre ; Lire une transformation

### 5. Prouver une invariance sur les générateurs

**Techniques incontournables** · Spé · signature et congruences

Démontrer une condition nécessaire sur les transformations accessibles.

**À faire :** Noter σc la permutation des coins et σe celle des arêtes. Vérifier sur un quart de tour que leurs signatures sont égales, puis expliquer pourquoi cette égalité se conserve par produit et inverse. Examiner les exemples impossibles sans les importer comme état courant.

**Acquis attendu :** Exclure l’échange de deux coins seuls ; distinguer comptage des couleurs, signature et sommes d’orientations.

**Limites et compléments :** Les orientations du cube sont des données expliquées. La suffisance de l’ensemble des conditions d’accessibilité est un théorème particulier fourni, hors socle.

**TP associés :** Tester une configuration : invariants

### 6. De la génération à une solution vérifiée

**Techniques incontournables** · Spé · mots, génération et inverse

Distinguer existence d’un mot inverse, construction d’une solution et optimalité.

**À faire :** Créer volontairement un mélange court après avoir noté l’état de départ. Comparer l’inverse de l’historique à une recherche bornée et vérifier les solutions. Un échec de recherche à profondeur fixée doit être interprété avec sa limite.

**Acquis attendu :** Expliquer pourquoi un historique connu suffit pour construire une solution, tandis qu’un cube importé demande une recherche.

**Limites et compléments :** Le socle est le raisonnement algébrique sur les mots. La recherche bidirectionnelle est un complément algorithmique, sans obligation de connaître un solveur complet.

**TP associés :** Mots et inverses ; Résolution

## Approfondissements : deux constructions guidées

Les définitions nouvelles sont fournies ; les calculs réinvestissent inverse et composition.

### 7. Localiser un défaut de commutation

**Approfondissement CPGE** · Sup / Spé · calcul dans un groupe

Utiliser le commutateur [A,B]=ABA⁻¹B⁻¹ et suivre les pièces affectées.

**À faire :** Comparer les commutateurs obtenus avec les faces R,U puis R,L. Prévoir lequel vaut e, puis analyser les cycles et orientations de l’autre.

**Acquis attendu :** Démontrer [A,B]=e si et seulement si AB=BA dans la convention de l’atelier.

**Limites et compléments :** Le calcul est accessible avec les axiomes ; les sous-groupes dérivés et la théorie des commutateurs ne sont pas demandés.

**TP associés :** Les commutateurs ; Comparer et construire

### 8. Transporter une manœuvre

**Approfondissement CPGE** · Spé · conjugaison guidée

Conserver le type des cycles en changeant les pièces sur lesquelles une manœuvre agit.

**À faire :** Noter A une manœuvre analysée et S un mot de préparation. Comparer A et SAS⁻¹ ; établir par récurrence l’identité (SAS⁻¹)ᵏ=SAᵏS⁻¹.

**Acquis attendu :** En déduire l’égalité des ordres et expliquer le déplacement des supports observés.

**Limites et compléments :** La conjugaison est ici un exercice algébrique fourni ; aucune classification des classes de conjugaison n’est exigée.

**TP associés :** Préparer et conjuguer ; Comparer et construire

## Au-delà : structure et algorithmes de résolution

Choisir ces deux branches après les séances prioritaires ; les théories propres au cube sont facultatives.

### A. Actions, stabilisateurs et comptage

**Au-delà du programme** · Au-delà · groupe agissant sur un ensemble

Comprendre une résolution progressive à partir des objets déjà fixés.

**À faire :** Lire la définition du stabilisateur d’une pièce, puis d’un ensemble de pièces. Relier les contraintes de permutations et d’orientations au comptage des états possibles.

**Acquis attendu :** Distinguer groupe de transformations, ensemble sur lequel il agit et sous-groupe qui fixe un objet.

**Limites et compléments :** Actions, formule orbite-stabilisateur et structure complète du groupe du cube ne sont pas présentées comme des obligations MPSI / MP.

**TP associés :** Actions et stabilisateurs ; Tester une configuration : invariants

### B. Graphes de Cayley et résolution par phases

**Au-delà du programme** · Au-delà · algorithmique et sous-groupes

Comparer la recherche d’un plus court chemin et une stratégie par sous-groupes.

**À faire :** Lire la convention HTM : chaque quart de tour, tour inverse ou demi-tour compte un mouvement. Comparer recherche courte et méthode en deux phases ; expliquer pourquoi une solution vérifiée peut ne pas être optimale.

**Acquis attendu :** Relier sommets, mouvements autorisés, profondeur et sous-groupe intermédiaire.

**Limites et compléments :** La méthode de Kociemba nécessite un module optionnel. Son algorithme, les tables de recherche et les bornes globales de distance sont des prolongements.

**TP associés :** Chercher une solution ; Vers une résolution générale ; Résolution

## Repères de programme

- [Programme officiel de mathématiques MPSI](https://prepas.org/ups.php?document=69)
- [Programme officiel de mathématiques MP](https://prepas.org/ups.php?document=85)
