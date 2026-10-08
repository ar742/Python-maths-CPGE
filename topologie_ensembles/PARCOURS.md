# Douze missions de topologie pour les CPGE scientifiques

Ces missions complètent les **30 introductions de TP**, les **60 leçons** et les
**60 exercices corrigés** de l'interface. Avant de déplacer un curseur, annoncer
l'espace, la distance ou la norme, l'ensemble étudié, puis la conclusion à
établir. Écrire une prédiction, confronter l'expérience et terminer par une
preuve. Un préfixe fini ne prouve jamais un énoncé sur toutes les valeurs d'une
suite, tous les points d'un ensemble ou tous les rayons d'un voisinage.

Les durées sont indicatives. Les activités **Sup** constituent l'entrée
progressive ; **Spé** développe les techniques du cours ; **au-delà** est un
prolongement identifié, sans prétendre que tout soit exigible dans chaque filière.
Les corrigés détaillés sont dans [EXERCICES.md](EXERCICES.md) et le cours dans
[COURS.md](COURS.md).

## 1. Donner un rayon à la définition d'ouvert — 35 à 50 min

**Labos :** `boules_normes`, `interieur_frontiere`. **Leçons et exercices 1–4.**

**But.** Comprendre la différence entre une boule ouverte et une boule fermée,
puis fabriquer une boule témoin autour d'un point intérieur.

1. Pour le point (0,7 ; 0,7) et le rayon 1, prévoir l'appartenance aux boules des
   normes 1, 2 et ∞. Comparer les calculs, pas seulement leurs formes.
2. Tester un point de la sphère en mode ouvert et fermé. Pour un point strictement
   intérieur, prendre δ = r − ‖x‖ et rédiger l'inclusion B(x,δ) ⊂ B(0,r).
3. Passer au disque épointé et classer zéro : absent, adhérent, non intérieur et
   sur la frontière. Déterminer ensuite les deux frontières de l'anneau.

**À rendre.** Un tableau A, A°, Ā, Fr(A) pour quatre domaines et une preuve par
inégalité triangulaire. **Sup :** coordonnées et inégalités. **Spé :**
quantificateurs et équivalence des normes. **Au-delà :** géométrie des normes.

## 2. Une limite absente, un espace ambiant indispensable — 35 à 50 min

**Labos :** `adherence_suite`, `topologie_relative`. **Leçons et exercices 5–8.**

**But.** Éviter de confondre point adhérent, point appartenant et point intérieur
relativement à un domaine.

1. Étudier A = {1/n : n ≥ 1}. Pour chaque ε>0, produire un n avec 1/n<ε.
2. Ajouter zéro et justifier le passage à un compact. N ne désigne que le nombre
   de points dessinés : augmenter N ne modifie pas la définition infinie de A.
3. Dans X=[0,1], comparer [0,1/2[ dans X et dans ℝ ; construire les deux sortes de
   boules autour de zéro et calculer les frontières correspondantes.

**À rendre.** La preuve séquentielle de Ā=A∪{0}, puis deux classifications
mentionnant explicitement l'espace ambiant. **Sup :** suites et intervalles.
**Spé :** fermeture séquentielle. **Au-delà :** sous-espaces topologiques.

## 3. Finies ou infinies : où les opérations changent — 35 à 55 min

**Labos :** `operations_ouverts`, `rationnels_irrationnels`.
**Leçons et exercices 9–10, 47–48.** **Lien au recueil : exercice 8 p.23/25.**

**But.** Repérer les hypothèses exactes dans les règles de stabilité des ouverts,
des fermés et des parties denses.

1. Calculer les intersections finies et infinies de ]−1/n,1/n[.
2. Faire de même pour les réunions de [1/n,1] ; donner une limite absente.
3. Prouver que l'intersection de deux denses est dense lorsque l'un est ouvert.
   Utiliser une boule, puis une boule plus petite incluse dans le premier dense.
4. Comparer ℚ et son complémentaire : denses disjoints, aucun ouvert.

**À rendre.** Les quatre règles ouvertes/fermées, deux contre-exemples et la
preuve complète de l'exercice 8. **Sup :** unions et intersections. **Spé :**
dense ouvert. **Au-delà :** théorème de Baire, en complément distinct.

## 4. Distances, convexité et projection — 55 à 80 min

**Labos :** `distance_ensemble`, `convexite`, `projection_convexe`.
**Leçons et exercices 11–14, 17–18.**

**But.** Séparer distance minimale, existence d'un minimisant et unicité de la
projection ; comprendre le rôle du convexe et de la norme euclidienne.

1. Sur la médiatrice de deux disques disjoints, calculer les deux projections.
2. Prouver que d(·,A) est 1-lipschitzienne même si les projections sont multiples.
3. Réfuter la convexité d'un anneau par deux points et leur milieu. La réussite
   d'un segment ne valide pas la définition pour tous les couples.
4. Projeter sur un triangle ; vérifier ⟨x−p,v−p⟩≤0 sur chacun de ses sommets.
   Étendre aux barycentres et développer ‖x−z‖².

**À rendre.** Un témoin de non-convexité et un certificat universel de projection.
**Sup :** segments et produits scalaires. **Spé :** unicité, caractérisation et
stabilité de la projection. **Au-delà :** contraintes d'optimisation.

## 5. L'enveloppe convexe comme image d'un compact — 40 à 60 min

**Labos :** `enveloppe_convexe`, `image_compacte`.
**Leçons et exercices 15–16, 33–34.** **Lien : exercice 6 p.23/25.**

**But.** Relier barycentres, calcul du bord, produit compact et application
continue.

1. Distinguer les N points d'un nuage et ses sommets extrêmes. Déplacer les poids
   et justifier que leur barycentre reste dans l'enveloppe.
2. Prouver la compacité de cette enveloppe comme image du simplexe des poids.
3. Ajouter une ellipse pleine à un segment orienté. Écrire le produit des
   domaines et l'application qui le transforme en somme.
4. Calculer l'appui dans la direction φ, puis choisir φ perpendiculaire au segment.

**À rendre.** Une preuve de produit compact avec deux extractions successives et
une formule d'appui. **Sup :** barycentres. **Spé :** exercice 6. **Au-delà :**
Carathéodory et fonctions d'appui.

## 6. Extraire une suite : déterministe, puis aléatoire — 50 à 75 min

**Labos :** `bolzano_weierstrass`, `extraction_aleatoire`.
**Leçons et exercices 21–24.** **Lien : TP p.17.**

**But.** Comprendre l'extraction sans imposer la convergence de la suite entière,
puis distinguer garantie analytique et résultat probabiliste.

1. Pour uₙ=(−1)ⁿ+1/(n+1), extraire pairs et impairs et majorer leurs erreurs.
2. Dans le TP aléatoire, vérifier les indices strictement croissants des records
   de rapprochement de la cible 1.
3. Calculer P(D_N>d)=(1−2d/3)^N pour 0<d≤1 ; choisir un budget pour une confiance
   donnée avant la simulation.
4. Expliquer pourquoi BW seul n'impose pas une cible arbitraire, tandis que le
   modèle indépendant uniforme donne presque sûrement une extraction vers 1.

**À rendre.** Deux extractions déterministes et une interprétation probabiliste
précise du TP. **Sup :** suites, simulations. **Spé :** BW, loi du meilleur
rapprochement. **Au-delà :** presque-sûreté et Borel–Cantelli.

## 7. Cauchy, complet, compact : trois mots à distinguer — 50 à 70 min

**Labos :** `cauchy_rationnels`, `compacts_recouvrements`.
**Leçons et exercices 25–28.**

**But.** Identifier le manque de limite dans ℚ et le manque de sous-recouvrement
fini pour un domaine non compact.

1. Calculer les fractions de Héron et l'identité d'erreur quadratique.
2. Prouver par parité que √2∉ℚ, puis conclure : Cauchy dans ℚ, limite dans ℝ.
3. Avec des centres j/m, trouver le seuil strict r>1/(2m) pour couvrir [0,1].
4. Pour Uₙ=]−1,1−1/n[, montrer que [0,1[ est recouvert à l'infini, mais qu'un
   voisinage de son bord manquant échappe à toute sous-famille finie.

**À rendre.** Deux preuves, l'une de non-complétude, l'autre de non-compacité.
**Sup :** limites et irrationnels. **Spé :** complétude et Heine–Borel.
**Au-delà :** complétion, précompacité et nombre de Lebesgue.

## 8. Continuité : extrema et un rayon uniforme — 50 à 75 min

**Labos :** `valeurs_extremes`, `heine_continuite`.
**Leçons et exercices 29–32.**

**But.** Localiser le rôle exact de la compacité dans le théorème des extrema et
dans Heine, puis calculer des bornes utiles.

1. Maximiser ℓθ sur l'ellipse fermée par Cauchy–Schwarz, avec le point d'égalité.
2. Ouvrir le domaine et construire une suite maximisante : le supremum est conservé,
   son atteinte est perdue.
3. Pour sin(x²), établir une borne 2R sur [−R,R], puis utiliser les paires
   √(2πn), √(2πn+π/2) pour réfuter l'uniformité sur ℝ.
4. Pour √x, trouver un rayon δ=ε² : uniforme mais non lipschitzienne à zéro.

**À rendre.** Une preuve avec trois hypothèses d'extrema et deux quantificateurs
de continuité comparés. **Sup :** dérivées et extrema. **Spé :** Heine.
**Au-delà :** coercivité et équicontinuité.

## 9. Une vraie dimension infinie — 55 à 80 min

**Labos :** `applications_lineaires`, `normes_dimension_infinie`,
`boule_non_compacte`. **Leçons et exercices 35–40.**
**Lien : exercice 9 p.23/25.**

**But.** Retrouver en dimension finie les bornes d'opérateur, puis construire des
contre-exemples lorsque la dimension n'est plus fixée.

1. Choisir une matrice dense 5×5 ou 8×8. Calculer ses trois normes d'opérateur et
   distinguer norme exacte et gains de directions tests.
2. Pour x^N, calculer les normes 1, 2 et ∞ par primitives et maximum.
3. Déduire l'impossibilité de constantes d'équivalence sur C([0,1]).
4. Pour vₙ=e^(int)/√(2π), calculer le Gram puis la distance √2 entre tous les
   modes distincts. Exclure toute extraction de Cauchy.

**À rendre.** Deux usages différents de la dimension infinie : normes non
équivalentes et boule fermée bornée non compacte. **Sup :** fonctions et
intégrales accompagnées. **Spé :** normes et exercice 9. **Au-delà :** Riesz, L².

## 10. Dénombrable, dense et pourtant très différent du continu — 55 à 80 min

**Labos :** `denombrer_rationnels`, `diagonale_cantor`, `ensemble_cantor`,
`rationnels_irrationnels`. **Leçons et exercices 41–48.**

**But.** Distinguer nombre de points, voisinages et longueur, avec des preuves
constructives.

1. Énumérer les fractions réduites par hauteur |p|+q ; prouver couverture et unicité.
2. Construire l'antidiagonale d'une liste de suites binaires, puis écrire le
   raisonnement pour tous les rangs.
3. Encoder les bits avec les chiffres ternaires 0 et 2 et minorer l'écart entre
   deux encodages au premier chiffre différent.
4. Classer le compact de Cantor : compact, parfait, non dénombrable, sans intervalle.
5. Comparer la densité de ℚ et de son complémentaire, indépendamment de leurs cardinaux.

**À rendre.** Trois preuves séparées de cardinalité, de densité et d'intérieur
vide. **Sup :** ensemble de nombres et suites. **Spé :** Cantor. **Au-delà :**
mesure et dimension fractale.

## 11. Connexité : chemins, limites et seuil critique — 55 à 85 min

**Labos :** `connexite_chemins`, `sinus_topologue`, `chemins_niveaux`.
**Leçons et exercices 19–20, 49–50, 57–58.** **Lien : exercice 7 p.23/25.**

**But.** Construire des chemins lorsqu'ils existent, utiliser une séparation pour
les interdire, puis découvrir qu'un connexe peut n'avoir aucun chemin entre deux
de ses points.

1. Contourner zéro dans ℝ², puis comparer la droite épointée.
2. Pour le sinus du topologue, prouver la connexité par adhérence et l'absence
   de chemin vers la verticale par oscillations forcées.
3. Dans Cassini, calculer F(0,y) : pour b<1, il sépare les lobes.
4. Au seuil b=1, comparer F≤1 et F<1 ; zéro fait ou défait le pont.

**À rendre.** Une chaîne d'implications et des exemples qui réfutent leurs
réciproques. **Sup :** chemins simples. **Spé :** TVI et connexité.
**Au-delà :** connexité locale et topologie des niveaux.

## 12. Structures, point fixe et homéomorphismes — 65 à 95 min

**Labos :** `gl_composantes`, `orthogonal_compact`, `point_fixe`,
`homeomorphisme`. **Leçons et exercices 51–56, 59–60.**

**But.** Mobiliser la topologie sur des matrices 4×4 et sur des applications,
avec des hypothèses toujours explicites.

1. Faire varier det A=6t : le signe sépare GL₄(ℝ). Passer au chemin complexe
   e^(iθ), qui contourne zéro. Distinguer det>0 et det=1.
2. Prouver qu'O₄ est fermé et de norme de Frobenius 2. Comparer SL₄, fermé mais
   non borné grâce à diag(e^T,e^−T,1,1).
3. Pour cos sur [0,1], vérifier domaine stable, complétude et taux sin1<1,
   puis calculer une borne d'erreur. Comparer l'affine lorsque |q|≥1.
4. Tester l'inverse de l'enroulement du cercle à la couture. Pour une injection
   continue d'un compact, retrouver la preuve de continuité de l'inverse.

**À rendre.** Une fiche de quatre théorèmes, chacun avec ses hypothèses, sa
conclusion et un contre-exemple lorsque l'une manque. **Sup :** entrée guidée.
**Spé :** GL, applications continues et compacts. **Au-delà :** groupes de Lie,
théorème de Banach et espaces quotients.
