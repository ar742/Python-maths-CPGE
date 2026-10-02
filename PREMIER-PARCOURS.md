# Premier parcours — Rubik & Groupes

Un parcours d'environ 45 minutes pour relier les opérations sur le cube aux
premières notions de théorie des groupes. L'application se lance avec
`Lancer_Rubik.cmd` sous Windows, ou `python rubik_groupes.py` depuis le dossier
`rubik_groupes`.

## 1. Définir le groupe

Dans **Cours & cube**, commencer par les générateurs et les inverses.
Jouer `R`, puis quatre fois `R` au total : le cube revient à l'identité.
Vérifier aussi que `R R'` ne change rien. Un mouvement correspond à une
permutation des facettes ; composer les mouvements donne une loi de groupe.

## 2. Observer la non-commutativité

Dans **Laboratoire**, comparer `R U` et `U R`. Les états diffèrent.
Lire les cycles et rapprocher l'observation de la composition des permutations.
Dans cette application, les mots se lisent toujours de gauche à droite.

## 3. Calculer un ordre

Analyser `R U`. Son ordre est **105**. Le calcul utilise le PPCM des longueurs
des cycles des facettes, et tient ainsi compte des orientations des pièces.
Comparer avec l'ordre **4** d'un quart de tour d'une face.

## 4. Construire une opération ciblée

Ouvrir la leçon sur les **commutateurs**. L'expérience
`R U R' D R U' R' D'`, soit `[R U R', D]`, agit sur **trois coins** et conserve
toutes les arêtes. Observer aussi l'orientation des coins : la permutation des
positions ne décrit pas, à elle seule, tout l'état du cube.

Passer à la **conjugaison** pour voir comment la zone d'action se déplace.
Le support change de place, mais l'ordre de l'opération est conservé.

## 5. Distinguer état légal et état impossible

Dans **Résolution**, utiliser les exemples de configurations impossibles.
Relier chaque refus à l'une des trois contraintes : somme des orientations des
coins modulo 3, somme des orientations des arêtes modulo 2, parités égales.
Ces contraintes expliquent le cardinal
**43 252 003 274 489 856 000** du groupe du cube standard à centres fixes.

## 6. Résoudre et comprendre la méthode

Créer un mélange de **quatre mouvements**, oublier son historique, puis lancer
la **recherche courte**. Jouer la solution geste par geste.
Le programme explore le graphe des configurations par couches ; une solution
trouvée est minimale en métrique HTM. Une recherche infructueuse à une borne
donnée ne prouve pas l'impossibilité du cube.

Pour prolonger : étudier le sous-groupe engendré par `U, D, R2, L2, F2, B2`
dans la leçon sur les deux phases, puis traiter les exercices corrigés.
L'installation du solveur général reste facultative.
