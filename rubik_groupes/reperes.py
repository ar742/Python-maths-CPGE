"""Guides des quatre activités interactives du cube."""


def guide(purpose, objects, hypotheses, techniques, steps, sup, spe, beyond, expected):
    return dict(purpose=purpose, objects=objects.split(' | '),
                hypotheses=hypotheses.split(' | '), techniques=techniques.split(' | '),
                first_steps=steps, levels=dict(sup=sup, spe=spe, beyond=beyond), expected=expected)


LAB_GUIDES = {
    'analyse': guide(
        'Associer une suite de tours de faces à une permutation. Lire ses cycles et trouver combien de répétitions ramènent le cube au départ.',
        'U,D,R,L,F,B nomment les faces haut, bas, droite, gauche, devant et derrière. R\' est le tour inverse de R ; R2 est un demi-tour. | Un mot est une suite de mouvements ; g est la transformation obtenue. Ici RU signifie R puis U, soit U∘R avec la convention des fonctions. | Un cycle décrit les déplacements de pièces ou de facettes. L’ordre de g est le plus petit entier positif k tel que g répété k fois soit l’identité e.',
        'On étudie un cube 3×3 à centres fixes, sans suivre l’orientation de logos. | L’ordre sur les pièces tient compte de leur orientation ; regarder leurs seules positions peut sous-estimer cet ordre.',
        'Bijections, composition et inverse | Décomposition en cycles, ppcm et ordre d’un élément',
        ['Analyser R et retrouver son ordre 4.', 'Analyser RU : comparer cycles des pièces et cycles des facettes.', 'Jouer un mot, puis son inverse : vérifier le retour au départ.'],
        'Permutations et calcul de l’inverse d’une composée.',
        'Sous-groupe engendré, ordre et groupe cyclique : programme MP.',
        'Représentation fidèle du groupe du cube sur ses facettes.',
        'Des mots différents peuvent avoir le même effet ; les éléments du groupe sont ces effets.'),
    'compare': guide(
        'Montrer que deux transformations ne commutent pas toujours. Construire un commutateur et déplacer son action par conjugaison.',
        'A et B sont les deux mots saisis, et aussi leurs transformations. AB signifie exécuter A puis B. | [A,B]=ABA⁻¹B⁻¹ est le commutateur dans cette convention. S est une manœuvre de préparation ; SAS⁻¹ est une conjugaison : S prépare les pièces, A agit, S⁻¹ annule la préparation. | e est la transformation qui ne déplace aucune facette ; il n’y a pas de grandeur physique ni d’unité dans cette expérience.',
        'La caméra change le point de vue, jamais le nom des faces. | Les produits se lisent chronologiquement de gauche à droite dans tout l’atelier.',
        'Comparer deux composées sur un même objet | Inverse, commutateur et conjugaison',
        ['Comparer A=R et B=U : regarder où AB et BA diffèrent.', 'Comparer deux faces opposées : chercher pourquoi leurs tours commutent.', 'Jouer le commutateur, puis une conjugaison : repérer les pièces affectées.'],
        'Composition de bijections et exemple de groupe non commutatif.',
        'Calcul dans un groupe et sous-groupes engendrés.',
        'Commutateurs et conjugaisons comme outils pour construire des algorithmes localisés.',
        'Un commutateur mesure un défaut de commutation ; une conjugaison transporte une action.'),
    'resolution': guide(
        'Passer d’une configuration à un mot qui la résout. Distinguer inversion d’un mélange connu et recherche d’un chemin sans historique.',
        'L’historique est la suite des mouvements exécutés depuis le cube résolu. Son inverse les annule dans l’ordre opposé. | Le graphe de Cayley a les configurations pour sommets et les mouvements autorisés pour arêtes. Une profondeur compte les mouvements, avec le demi-tour compté comme un seul. | La recherche bidirectionnelle part du mélange et du cube résolu ; le solveur complet, s’il est installé, utilise une autre méthode.',
        'L’inverse de l’historique exige un historique connu. | La recherche bornée explore jusqu’à la profondeur annoncée ; un échec dans cette limite n’est pas une impossibilité de résoudre. | Les longueurs de solution ne sont comparables qu’avec une même convention de mouvements.',
        'Inverser une composée | Parcours d’un graphe et comparaison d’algorithmes',
        ['Créer un petit mélange puis jouer l’inverse de son historique.', 'Demander la recherche bidirectionnelle sur un mélange court.', 'Comparer les mots trouvés et leur longueur : ne pas confondre solution et solution minimale.'],
        'Inverse, suites d’opérations et raisonnement algorithmique.',
        'Partie génératrice et ordre ; liens avec les graphes étudiés en informatique.',
        'Graphe de Cayley et méthode de résolution par phases.',
        'Connaître le mélange fournit immédiatement une solution ; résoudre sans historique demande une recherche.'),
    'invariants': guide(
        'Tester si une configuration décrite par ses couleurs peut provenir de tours de faces. Comprendre comment des invariants excluent certains assemblages.',
        'Les 54 lettres décrivent les facettes dans l’ordre URFDLB annoncé par l’interface. Les centres fixent le repère des couleurs. | σc et σe sont les permutations des huit coins et des douze arêtes. Un coin porte une orientation modulo 3 ; une arête, modulo 2. | La signature d’une permutation vaut +1 ou −1 selon sa parité. Les sommes d’orientations et les signatures sont des invariants à vérifier.',
        'Chaque couleur apparaît neuf fois et les centres sont ceux du repère. | Un simple comptage des couleurs ne suffit pas : orientation et parité doivent aussi convenir. | Les tests concernent le cube standard à centres fixes.',
        'Congruences modulo 2 et 3 | Signature d’une permutation et invariance sous les générateurs',
        ['Tester le cube résolu puis un mélange autorisé.', 'Choisir une seule arête retournée : identifier l’invariant violé.', 'Tester un seul coin tourné puis un échange impossible : distinguer orientation et parité.'],
        'Permutations, signature et calcul modulo un entier.',
        'Montrer une invariance sur les générateurs puis sur leurs produits.',
        'Caractérisation des configurations atteignables et structure du groupe du cube.',
        'Un invariant nécessaire se démontre sur chaque tour de face ; la suffisance demande un résultat supplémentaire.')
}
