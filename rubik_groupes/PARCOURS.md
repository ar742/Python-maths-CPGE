# Parcours : prévoir, expérimenter, démontrer

<!-- REPERES_EXPERIENCES -->

## Guides des expériences

Les repères distinguent les outils de sup, ceux de spé et les prolongements. Ils s’appuient sur les programmes de mathématiques [MPSI](https://prepas.org/ups.php?document=69) et [MP](https://prepas.org/ups.php?document=85).

### Lire une transformation

Associer une suite de tours de faces à une permutation. Lire ses cycles et trouver combien de répétitions ramènent le cube au départ.

**Objets et notations**

- U,D,R,L,F,B nomment les faces haut, bas, droite, gauche, devant et derrière. R' est le tour inverse de R ; R2 est un demi-tour.

- Un mot est une suite de mouvements ; g est la transformation obtenue. Ici RU signifie R puis U, soit U∘R avec la convention des fonctions.

- Un cycle décrit les déplacements de pièces ou de facettes. L’ordre de g est le plus petit entier positif k tel que g répété k fois soit l’identité e.

**Hypothèses**

- On étudie un cube 3×3 à centres fixes, sans suivre l’orientation de logos.

- L’ordre sur les pièces tient compte de leur orientation ; regarder leurs seules positions peut sous-estimer cet ordre.

**Techniques à mobiliser**

- Bijections, composition et inverse

- Décomposition en cycles, ppcm et ordre d’un élément

**Trois premières manipulations**

1. Analyser R et retrouver son ordre 4.

2. Analyser RU : comparer cycles des pièces et cycles des facettes.

3. Jouer un mot, puis son inverse : vérifier le retour au départ.

**Repères CPGE**

**Sup :** Permutations et calcul de l’inverse d’une composée.

**Spé :** Sous-groupe engendré, ordre et groupe cyclique : programme MP.

**Au-delà :** Représentation fidèle du groupe du cube sur ses facettes.

**À retenir :** Des mots différents peuvent avoir le même effet ; les éléments du groupe sont ces effets.

### Comparer et construire

Montrer que deux transformations ne commutent pas toujours. Construire un commutateur et déplacer son action par conjugaison.

**Objets et notations**

- A et B sont les deux mots saisis, et aussi leurs transformations. AB signifie exécuter A puis B.

- [A,B]=ABA⁻¹B⁻¹ est le commutateur dans cette convention. S est une manœuvre de préparation ; SAS⁻¹ est une conjugaison : S prépare les pièces, A agit, S⁻¹ annule la préparation.

- e est la transformation qui ne déplace aucune facette ; il n’y a pas de grandeur physique ni d’unité dans cette expérience.

**Hypothèses**

- La caméra change le point de vue, jamais le nom des faces.

- Les produits se lisent chronologiquement de gauche à droite dans tout l’atelier.

**Techniques à mobiliser**

- Comparer deux composées sur un même objet

- Inverse, commutateur et conjugaison

**Trois premières manipulations**

1. Comparer A=R et B=U : regarder où AB et BA diffèrent.

2. Comparer deux faces opposées : chercher pourquoi leurs tours commutent.

3. Jouer le commutateur, puis une conjugaison : repérer les pièces affectées.

**Repères CPGE**

**Sup :** Composition de bijections et exemple de groupe non commutatif.

**Spé :** Calcul dans un groupe et sous-groupes engendrés.

**Au-delà :** Commutateurs et conjugaisons comme outils pour construire des algorithmes localisés.

**À retenir :** Un commutateur mesure un défaut de commutation ; une conjugaison transporte une action.

### Du mélange au mot solution

Passer d’une configuration à un mot qui la résout. Distinguer inversion d’un mélange connu et recherche d’un chemin sans historique.

**Objets et notations**

- L’historique est la suite des mouvements exécutés depuis le cube résolu. Son inverse les annule dans l’ordre opposé.

- Le graphe de Cayley a les configurations pour sommets et les mouvements autorisés pour arêtes. Une profondeur compte les mouvements, avec le demi-tour compté comme un seul.

- La recherche bidirectionnelle part du mélange et du cube résolu ; le solveur complet, s’il est installé, utilise une autre méthode.

**Hypothèses**

- L’inverse de l’historique exige un historique connu.

- La recherche bornée explore jusqu’à la profondeur annoncée ; un échec dans cette limite n’est pas une impossibilité de résoudre.

- Les longueurs de solution ne sont comparables qu’avec une même convention de mouvements.

**Techniques à mobiliser**

- Inverser une composée

- Parcours d’un graphe et comparaison d’algorithmes

**Trois premières manipulations**

1. Créer un petit mélange puis jouer l’inverse de son historique.

2. Demander la recherche bidirectionnelle sur un mélange court.

3. Comparer les mots trouvés et leur longueur : ne pas confondre solution et solution minimale.

**Repères CPGE**

**Sup :** Inverse, suites d’opérations et raisonnement algorithmique.

**Spé :** Partie génératrice et ordre ; liens avec les graphes étudiés en informatique.

**Au-delà :** Graphe de Cayley et méthode de résolution par phases.

**À retenir :** Connaître le mélange fournit immédiatement une solution ; résoudre sans historique demande une recherche.

### Tester une configuration

Tester si une configuration décrite par ses couleurs peut provenir de tours de faces. Comprendre comment des invariants excluent certains assemblages.

**Objets et notations**

- Les 54 lettres décrivent les facettes dans l’ordre URFDLB annoncé par l’interface. Les centres fixent le repère des couleurs.

- σc et σe sont les permutations des huit coins et des douze arêtes. Un coin porte une orientation modulo 3 ; une arête, modulo 2.

- La signature d’une permutation vaut +1 ou −1 selon sa parité. Les sommes d’orientations et les signatures sont des invariants à vérifier.

**Hypothèses**

- Chaque couleur apparaît neuf fois et les centres sont ceux du repère.

- Un simple comptage des couleurs ne suffit pas : orientation et parité doivent aussi convenir.

- Les tests concernent le cube standard à centres fixes.

**Techniques à mobiliser**

- Congruences modulo 2 et 3

- Signature d’une permutation et invariance sous les générateurs

**Trois premières manipulations**

1. Tester le cube résolu puis un mélange autorisé.

2. Choisir une seule arête retournée : identifier l’invariant violé.

3. Tester un seul coin tourné puis un échange impossible : distinguer orientation et parité.

**Repères CPGE**

**Sup :** Permutations, signature et calcul modulo un entier.

**Spé :** Montrer une invariance sur les générateurs puis sur leurs produits.

**Au-delà :** Caractérisation des configurations atteignables et structure du groupe du cube.

**À retenir :** Un invariant nécessaire se démontre sur chaque tour de face ; la suffisance demande un résultat supplémentaire.
