# Topologie & Ensembles · Exercices corrigés

60 exercices originaux. Chercher la solution avant de lire la correction et réinvestir le laboratoire associé.

## 1. Choisir un rayon sûr dans ℝ⁴

**Sup → Spé · TP : boules_normes**

**Énoncé.** Pour x=(1,−2,2,−1), calculer ses normes 1, 2 et ∞. Donner une boule euclidienne contenue dans la boule ouverte infinie de rayon 3, et une boule infinie contenue dans cette même boule euclidienne.

### Correction guidée

**Corrigé.** On obtient 6, √10 et 2. Comme ‖z‖∞≤‖z‖₂, B₂(0,3)⊂B∞(0,3). Comme ‖z‖₂≤2‖z‖∞ dans ℝ⁴, B∞(0,3/2)⊂B₂(0,3). Ces inclusions expliquent pourquoi un ouvert pour une norme reste ouvert pour l’autre, sans supposer l’égalité des boules.

## 2. Un rayon intérieur calculé, non deviné

**Sup → Spé · TP : boules_normes**

**Énoncé.** Dans la boule ouverte de norme 1, de centre a=(1,−1) et rayon 2, prendre x=(1,4;−0,5). Déterminer une boule centrée en x contenue dans la boule initiale. Le même raisonnement fonctionne-t-il pour un point de la sphère ?

### Correction guidée

**Corrigé.** ‖x−a‖₁=0,4+0,5=0,9 ; la marge est 1,1. Ainsi B₁(x,1,1) est contenue dans B₁(a,2), avec des inégalités strictes. Sur la sphère la marge vaut zéro, donc ce calcul ne fournit aucun rayon positif ; de fait tout voisinage d’un point de cette sphère contient des points hors de la boule.

## 3. Un anneau et deux frontières

**Sup → Spé · TP : interieur_frontiere**

**Énoncé.** Dans ℝ², A={x : 1/2≤‖x‖₂≤1}. Déterminer A°, Ā et Fr(A), puis classer A. Pourquoi le cercle intérieur ne disparaît-il pas de la frontière ?

### Correction guidée

**Corrigé.** A°={1/2<‖x‖₂<1}, Ā=A et Fr(A) est la réunion des cercles de rayons 1/2 et 1. A est fermé et borné, donc compact en dimension finie, mais n’est pas ouvert. Une boule autour d’un point du cercle intérieur contient à la fois des points de rayon inférieur à 1/2 et supérieur à 1/2 : elle rencontre les deux côtés.

## 4. Une frontière peut avoir un intérieur

**Sup → Spé · TP : interieur_frontiere**

**Énoncé.** Déterminer intérieur, adhérence et frontière de ℚ dans ℝ. Déduire si la frontière d’un ensemble possède toujours un intérieur vide.

### Correction guidée

**Corrigé.** Chaque intervalle contient un rationnel et un irrationnel. Ainsi ℚ°=∅, ℚ̄=ℝ et Fr(ℚ)=ℝ, dont l’intérieur est ℝ. La frontière d’un ensemble quelconque n’a donc pas toujours un intérieur vide. Pour un fermé F, en revanche Fr(F)=F∖F° a un intérieur vide : une boule incluse dans cette frontière serait incluse dans F et donc dans F°.

## 5. Un ensemble de matrices qui se ferme en ajoutant une limite

**Sup → Spé · TP : adherence_suite**

**Énoncé.** Dans M₄(ℝ) de norme de Frobenius, poser Dₙ=diag(1,1,1,1/n). Déterminer l’adhérence de {Dₙ:n≥1}, son caractère compact et sa distance à l’ensemble des matrices singulières.

### Correction guidée

**Corrigé.** Dₙ→D∞=diag(1,1,1,0). Comme pour {1/n}, l’adhérence est {Dₙ}∪{D∞}. L’ensemble initial n’est pas fermé et n’est donc pas compact ; son adhérence est fermée bornée dans ℝ¹⁶, donc compacte. Chaque Dₙ est à distance 1/n des matrices singulières, car sa plus petite valeur singulière vaut 1/n ; l’infimum sur tout l’ensemble est zéro, non atteint par un Dₙ.

## 6. Accumulation ou isolement ?

**Sup → Spé · TP : adherence_suite**

**Énoncé.** Pour C={0}∪{1/n:n≥1}, caractériser ses points d’accumulation. Montrer qu’une suite parcourant une infinité de points distincts de C ne peut avoir une limite différente de 0.

### Correction guidée

**Corrigé.** 0 est un point d’accumulation car chaque boule autour de zéro contient des 1/n non nuls. Chaque 1/k possède un voisinage évitant les autres valeurs, obtenu avec la moitié du plus petit écart aux voisins. Une suite de points distincts convergeant vers un point isolé serait finalement égale à ce point, contradiction ; l’unique limite possible est donc zéro.

## 7. Un intervalle semi-ouvert bien classé

**Sup → Spé · TP : topologie_relative**

**Énoncé.** Pour X=[0,1] et A=[0,1/2[, calculer les intérieurs, adhérences et frontières dans ℝ puis dans X. A est-il compact ?

### Correction guidée

**Corrigé.** Dans ℝ, intérieur ]0,1/2[, adhérence [0,1/2] et frontière {0,1/2}. Dans X, intérieur [0,1/2[, même adhérence [0,1/2] et frontière {1/2}. A n’est pas compact : la suite 1/2−1/(n+3) converge vers 1/2, hors de A. L’ouverture relative ne décide pas à elle seule de la compacité.

## 8. Fermé relatif ne suffit pas

**Sup → Spé · TP : topologie_relative**

**Énoncé.** Dans X=]0,1[, considérer F=]0,1/2]. Montrer que F est fermé dans X mais pas compact. Quel rôle joue le caractère non fermé de X dans ℝ ?

### Correction guidée

**Corrigé.** F=X∩]−∞,1/2], donc est fermé dans X. Pourtant 1/(n+2)∈F tend vers zéro dans ℝ, hors de F ; aucune sous-suite n’a une autre limite. F n’est pas compact et n’est pas fermé dans ℝ. Un fermé d’un compact est compact ; ici X n’est pas compact, donc ce théorème ne s’applique pas.

## 9. La réunion infinie qui perd sa limite

**Sup → Spé · TP : operations_ouverts**

**Énoncé.** Déterminer ⋃n≥1[1/n,1] et son adhérence. Donner une suite qui prouve que cette réunion n’est pas fermée et distinguer l’union de son adhérence.

### Correction guidée

**Corrigé.** Chaque réel x∈]0,1] appartient à [1/n,1] pour n≥1/x ; zéro n’appartient à aucun terme. La réunion est donc ]0,1], son adhérence [0,1]. La suite 1/n est dans la réunion et converge vers zéro, absent de celle-ci. L’adhérence ajoute la limite, tandis que l’union demande l’appartenance à au moins un terme.

## 10. Intersections finies de denses ouverts

**Sup → Spé · TP : operations_ouverts**

**Énoncé.** Dans ℝ, montrer que l’intersection d’un nombre fini d’ouverts denses est dense. Pourquoi cette preuve ne permet-elle pas de conclure pour les ouverts denses ℝ∖{qₙ}, où (qₙ) énumère ℚ, avec une simple récurrence finie ?

### Correction guidée

**Corrigé.** L’exercice 8 et une récurrence donnent l’assertion finie, puisque l’intersection obtenue reste ouverte. L’intersection infinie vaut ℝ∖ℚ, dense mais non ouverte. Chaque étape finie possède un rayon intérieur ; aucun rayon commun positif ne découle de la récurrence. La densité de cette intersection infinie peut être prouvée ici directement par les irrationnels, ou par le théorème de Baire sur ℝ complet, théorème supplémentaire.

## 11. Une union de disques : deux points également proches

**Sup → Spé · TP : distance_ensemble**

**Énoncé.** D₋ et D₊ sont les disques fermés de rayon 1/2 centrés en (−2,0) et (2,0). Calculer d((0,1),D₋∪D₊) et les deux projections.

### Correction guidée

**Corrigé.** Les deux centres sont à distance √5. La distance cherchée vaut √5−1/2. Les projections sont p₋=(−2,0)+(1/(2√5))(2,1) et p₊=(2,0)+(1/(2√5))(−2,1). Elles sont distinctes et réalisent le même minimum. La fonction distance ne choisit pas entre ces deux points.

## 12. La distance à un ouvert dense

**Sup → Spé · TP : distance_ensemble**

**Énoncé.** Soit A=ℝ∖ℤ. Calculer d(x,A) pour tout x∈ℝ et comparer avec d(x,ℤ). Peut-on reconstituer A à partir de la seule fonction d(·,A) ?

### Correction guidée

**Corrigé.** A est dense, donc d(x,A)=0 pour tout x. La distance à ℤ vaut min(|x−⌊x⌋|,|x−⌈x⌉|) et n’est nulle que sur ℤ. La fonction distance à A caractérise Ā, pas A lui-même : A et ℝ ont la même fonction distance, identiquement nulle.

## 13. Un convexe défini par quatre contraintes

**Sup → Spé · TP : convexite**

**Énoncé.** Montrer que C={(x,y): x≥0, y≥0, x+y≤3, 2x+y≤4} est convexe et compact. Déterminer ses sommets et donner un point intérieur.

### Correction guidée

**Corrigé.** Chaque contrainte définit un demi-plan fermé convexe ; l’intersection est donc fermée et convexe. Elle est bornée par 0≤x≤2 et 0≤y≤3, donc compacte. Les sommets sont (0,0), (2,0), (1,2), (0,3). Le point (1/2,1/2) satisfait strictement toutes les contraintes, donc possède un voisinage contenu dans C.

## 14. Une union qui n’est pas automatiquement convexe

**Sup → Spé · TP : convexite**

**Énoncé.** Donner deux convexes compacts de ℝ² dont la réunion est non convexe. Déterminer une condition suffisante simple pour que leur réunion soit convexe.

### Correction guidée

**Corrigé.** Deux disques de rayon 1/2 centrés en (−2,0) et (2,0) sont convexes compacts, mais le milieu de leurs centres manque leur réunion. Une condition suffisante est l’inclusion de l’un dans l’autre : la réunion est alors le plus grand. L’intersection non vide seule ne suffit pas ; deux disques qui se chevauchent faiblement peuvent encore laisser manquer un segment entre leurs bords extérieurs.

## 15. Un barycentre dans un quadrilatère

**Sup → Spé · TP : enveloppe_convexe**

**Énoncé.** Pour A=(0,0), B=(3,0), C=(3,2), D=(0,2), calculer le barycentre de poids (1/10,2/10,3/10,4/10). Exprimer le résultat avec seulement trois des sommets.

### Correction guidée

**Corrigé.** Le point vaut (3×5/10,2×7/10)=(1,5;1,4). Il s’exprime avec B,C,D de poids 0,3, 0,2 et 0,5 : x=3(0,3+0,2)=1,5 et y=2(0,2+0,5)=1,4. Les poids sont non négatifs et leur somme vaut 1. Plusieurs représentations barycentriques sont possibles dans un polygone.

## 16. Pourquoi un poids négatif est dangereux

**Sup → Spé · TP : enveloppe_convexe**

**Énoncé.** Pour a=(0,0), b=(1,0), c=(0,1), déterminer conv{a,b,c}. Le point 2b−c est-il dans cette enveloppe malgré une somme de coefficients égale à 1 ?

### Correction guidée

**Corrigé.** L’enveloppe est le triangle x≥0, y≥0, x+y≤1. Le point 2b−c=(2,−1) est hors du triangle, car son ordonnée est négative. Les coefficients (0,2,−1) ont bien une somme égale à 1 mais ne sont pas tous non négatifs : ils définissent une combinaison affine, pas convexe.

## 17. Projeter sur un rectangle

**Spé · TP : projection_convexe**

**Énoncé.** Pour C=[−1,1]×[−2,2] et x=(3,−4), calculer la projection, la distance et vérifier la condition angulaire pour tout z∈C.

### Correction guidée

**Corrigé.** La projection vaut p=(1,−2), obtenue en ramenant séparément chaque coordonnée dans son intervalle. La distance vaut √8. Pour z=(z₁,z₂), ⟨x−p,z−p⟩=2(z₁−1)−2(z₂+2)≤0 car z₁≤1 et z₂≥−2. Cette inégalité prouve directement la minimalité et l’unicité.

## 18. Un triangle : vérifier seulement trois sommets

**Spé · TP : projection_convexe**

**Énoncé.** Soit C=conv{(0,0),(3,0),(0,3)} et x=(2,2). Proposer p, puis vérifier la condition sur les sommets avant de conclure.

### Correction guidée

**Corrigé.** La projection orthogonale sur x₁+x₂=3 donne p=(1,5;1,5), qui appartient à l’arête. x−p=(0,5;0,5). Les produits scalaires avec les trois sommets moins p valent −1,5, 0 et 0. Toute combinaison convexe conserve leur signe, donc la caractérisation prouve p=P_C(x). La distance vaut √0,5.

## 19. Deux segments hors de zéro

**Sup → Spé · TP : connexite_chemins**

**Énoncé.** Relier a=(2,0) à b=(−3,0) dans ℝ²∖{0} par un chemin formé de deux segments. Donner une paramétrisation continue explicite et vérifier qu’elle ne rencontre pas zéro.

### Correction guidée

**Corrigé.** Choisir c=(0,1). Pour t∈[0,1/2], γ(t)=(1−2t)a+2tc ; pour t∈[1/2,1], γ(t)=(2−2t)c+(2t−1)b. Les deux formules valent c au raccord. Sur le premier segment, l’ordonnée est positive sauf à a ; sur le second, elle est positive sauf à b. Les extrémités sont non nulles, donc zéro n’est jamais atteint.

## 20. Un réel continu sur un anneau prend toutes les valeurs intermédiaires

**Sup → Spé · TP : connexite_chemins**

**Énoncé.** Sur A={1≤x²+y²≤4}, prendre f(x,y)=x. Déterminer f(A) puis justifier que f ne peut sauter une valeur entre −2 et 2, même si A n’est pas convexe.

### Correction guidée

**Corrigé.** Tout point de A vérifie |x|≤2. Chaque c∈[−2,2] est l’abscisse d’un point du cercle extérieur : (c,√(4−c²))∈A. Donc f(A)=[−2,2]. Plus généralement A est connexe par arcs et f continue ; le TVI appliqué à f∘γ sur un chemin relie deux valeurs et garantit toutes les valeurs intermédiaires. La convexité n’est pas nécessaire.

## 21. Trois limites cachées dans quatre classes d’indices

**Sup → Spé · TP : bolzano_weierstrass**

**Énoncé.** Pour xₙ=((−1)ⁿ,cos(nπ/2)) dans ℝ², déterminer les valeurs prises, les limites d’adhérence et une extraction vers chacune.

### Correction guidée

**Corrigé.** Selon n modulo 4, les valeurs sont (1,1), (−1,0), (1,−1), (−1,0). Les trois limites d’adhérence distinctes sont donc (1,1), (−1,0), (1,−1), et non quatre malgré quatre classes d’indices. Les extractions n=4k, n=4k+1 et n=4k+2 sont constantes. La suite entière ne converge pas.

## 22. Une limite en dehors de l’ensemble initial

**Sup → Spé · TP : bolzano_weierstrass**

**Énoncé.** Une suite prend ses valeurs dans A=]0,1[ et est bornée. Bolzano–Weierstrass assure-t-il une limite extraite dans A ? Donner un contre-exemple et la condition supplémentaire qui réparerait la conclusion.

### Correction guidée

**Corrigé.** La suite xₙ=1/(n+2) converge vers zéro, hors de A ; toutes ses sous-suites ont la même limite. BW ne promet qu’une limite dans ℝ. Si A est fermé et borné dans ℝᵈ, toute limite extraite appartient à A : A est compact. La fermeture complète précisément l’hypothèse manquante.

## 23. Atteindre 1 à 0,01 près avec 99 % de confiance

**Sup → Spé · TP : extraction_aleatoire**

**Énoncé.** Pour a=1, ε=0,01 et des essais indépendants uniformes sur [0,3], donner un budget suffisant pour une probabilité de succès au moins 0,99. Ce résultat exclut-il tout échec ?

### Correction guidée

**Corrigé.** Il faut m≥ln(0,01)/ln(1−0,02/3)≈688,47, donc 689 essais suffisent. La probabilité d’échec reste positive mais ≤0,01. Un échec dans la simulation ne réfute pas la formule ; il est une réalisation possible. Répéter le test avec des graines différentes ne transforme pas une confiance statistique en preuve déterministe.

## 24. La cible située au bord

**Sup → Spé · TP : extraction_aleatoire**

**Énoncé.** Reprendre a=0 et 0<ε<3. Calculer la probabilité de succès d’un essai et le budget pour ε=0,01, confiance 99 %. Pourquoi le facteur 2 disparaît-il ?

### Correction guidée

**Corrigé.** Le voisinage intersecté avec [0,3] est [0,ε[, de longueur ε : la probabilité vaut ε/3. Le budget est ceil[ln(0,01)/ln(1−0,01/3)]=1380. Au bord, une seule moitié du voisinage contient des valeurs possibles. La formule intérieure 2ε/3 ne s’applique donc pas.

## 25. Une borne rationnelle du défaut de Newton

**Sup → Spé · TP : cauchy_rationnels**

**Énoncé.** En partant de u₀=2, montrer que eₙ=uₙ−√2 satisfait eₙ₊₁≤eₙ²/2. Déduire une convergence plus rapide qu’une simple décroissance géométrique une fois eₙ≤1/2.

### Correction guidée

**Corrigé.** Comme uₙ≥√2>1, l’identité donne eₙ₊₁=eₙ²/(2uₙ)≤eₙ²/2. Si eₙ≤1/2, alors eₙ₊₁≤eₙ/4, mais le facteur eₙ/2 devient lui-même de plus en plus petit. C’est une convergence quadratique. Cette rapidité ne rend pas √2 rationnel : chaque approximation reste rationnelle sans que sa limite le soit.

## 26. Fermé dans ℚ et pourtant incomplet

**Sup → Spé · TP : cauchy_rationnels**

**Énoncé.** A=ℚ∩[1,2], muni de la distance usuelle. Montrer qu’il est fermé et borné dans ℚ mais incomplet et non compact.

### Correction guidée

**Corrigé.** A est l’intersection avec ℚ d’un fermé de ℝ, donc fermé relativement à ℚ ; il est borné. La suite rationnelle de Newton partant de 2 reste dans A et est de Cauchy, mais sa seule limite réelle est √2, hors de ℚ. A est incomplet. Un compact métrique étant complet, il n’est pas compact. La caractérisation fermé borné des compacts exige ℝᵈ ou ℂᵈ, et ne s’étend pas à ℚ.

## 27. Un recouvrement sans extraction finie

**Sup → Spé · TP : compacts_recouvrements**

**Énoncé.** Vérifier que Uₙ=]1/n,1[, n≥2, recouvrent ]0,1[. Montrer qu’aucun sous-recouvrement fini n’existe. Comment adapter un recouvrement pour rendre visible le rôle de zéro dans [0,1] ?

### Correction guidée

**Corrigé.** Pour x>0, choisir n>1/x : x∈Uₙ. Une union finie est contenue dans ]1/N,1[ où N est le plus grand indice choisi, et manque 1/(2N). Ces mêmes Uₙ ne recouvrent pas [0,1], car zéro et un sont absents. Tout véritable recouvrement ouvert de [0,1] doit aussi contenir des ouverts autour de ces extrémités ; leur marge permet la compacité.

## 28. Une marge positive dans une boule ouverte

**Sup → Spé · TP : compacts_recouvrements**

**Énoncé.** K est un compact non vide d’un espace normé, inclus dans Bₒ(0,1). Prouver qu’il existe r<1 avec K⊂B𝒇(0,r). Pourquoi un ensemble simplement borné ne suffit-il pas ?

### Correction guidée

**Corrigé.** La norme est continue et atteint un maximum r sur K. Puisque chaque point de K a une norme strictement inférieure à 1, le maximum atteint vérifie r<1. L’ensemble {1−1/n:n≥2}⊂ℝ est borné et inclus dans ]−1,1[, mais son supremum vaut 1, non atteint ; aucune marge r<1 ne le contient. C’est l’atteinte du maximum, non la seule bornitude, qui produit la marge.

## 29. Un minimum quartique non convexe

**Sup → Spé · TP : valeurs_extremes**

**Énoncé.** Pour f(x,y)=(x²−1)²+y² sur ℝ², prouver l’existence d’un minimum global et déterminer les minimisants. L’existence impose-t-elle l’unicité ?

### Correction guidée

**Corrigé.** f est polynomiale et continue. En posant u=x², (u−1)²−u=(u−3/2)²−5/4≥−5/4, donc f(x,y)≥x²+y²−5/4 : elle est coercive. Comme chaque terme est non négatif, le minimum vaut zéro, atteint exactement en (−1,0) et (1,0). L’existence ne donne donc aucune unicité ; une stricte convexité appropriée serait une hypothèse supplémentaire.

## 30. La continuité ne peut être omise

**Sup → Spé · TP : valeurs_extremes**

**Énoncé.** Sur [0,1], définir f(0)=1 et f(x)=x pour x>0. Déterminer infimum et supremum, puis préciser lesquels sont atteints et pourquoi le théorème des extrema ne s’applique pas.

### Correction guidée

**Corrigé.** L’infimum vaut zéro sans être atteint, puisque toutes les valeurs sont strictement positives et f(1/n)=1/n→0. Le supremum vaut 1, atteint en 0 et 1. Le domaine est compact non vide, mais f est discontinue en zéro : sa limite à droite vaut zéro alors que f(0)=1. La conclusion complète du théorème manque donc.

## 31. Une oscillation qui détruit l’uniformité

**Sup → Spé · TP : heine_continuite**

**Énoncé.** Sur ]0,1], f(x)=sin(1/x). Construire deux suites de points de distance tendant vers zéro et dont les images restent à distance 2.

### Correction guidée

**Corrigé.** Prendre xₙ=1/(π/2+2πn) et yₙ=1/(3π/2+2πn). Elles sont positives, tendent vers zéro et leur différence tend vers zéro ; f(xₙ)=1 et f(yₙ)=−1. La continuité uniforme échoue, bien que f soit continue en chaque point du domaine. Le point zéro est hors du domaine et ne peut fournir une extraction dans un compact.

## 32. Un rayon explicite pour la racine

**Sup → Spé · TP : heine_continuite**

**Énoncé.** Sur [0,4], garantir une variation de √x inférieure à 0,02 avec un rayon uniforme. Peut-on utiliser une dérivée globalement bornée ?

### Correction guidée

**Corrigé.** La borne Hölder donne δ=(0,02)²=0,0004 : |x−y|<δ implique |√x−√y|<0,02. La dérivée 1/(2√x) est non bornée près de zéro et n’existe pas finiment en zéro, donc une borne de dérivée uniforme ne convient pas. Heine garantit l’existence d’un rayon, et l’inégalité fournit sa valeur concrète.

## 33. Somme d’un cercle et d’un segment

**Spé · TP : image_compacte**

**Énoncé.** A est le cercle unité de ℝ², B=[−2,2]×{0}. Prouver que A+B est compact sans supposer qu’il soit convexe. Trouver ses abscisses maximale et minimale.

### Correction guidée

**Corrigé.** A et B sont fermés bornés donc compacts, et l’addition est continue : A+B est compact par l’exercice 6. Pour a∈A et b∈B, l’abscisse appartient à [−3,3]. Les bornes sont atteintes en a=(±1,0), b=(±2,0), de signes identiques. La preuve de compacité n’utilise pas la convexité ; le cercle lui-même n’est pas convexe.

## 34. Des fermés disjoints à distance nulle

**Spé · TP : image_compacte**

**Énoncé.** Justifier soigneusement que A={(x,0)} et B={(x,eˣ)} sont fermés dans ℝ², puis calculer dist(A,B). Quel point de la preuve compacte manque ici ?

### Correction guidée

**Corrigé.** A est l’image réciproque de {0} par (x,y)↦y ; B celle de {0} par (x,y)↦y−eˣ. Ils sont fermés par continuité. Ils sont disjoints puisque eˣ>0, mais les couples (−n,0),(−n,e⁻ⁿ) ont une distance e⁻ⁿ→0 ; l’infimum vaut zéro. La suite minimisante part à l’infini et n’a aucune extraction convergente dans A×B ; le minimum n’est pas atteint.

## 35. Une norme d’opérateur obtenue sans tester mille directions

**Spé · TP : applications_lineaires**

**Énoncé.** Pour Q orthogonale 4×4 et A=Q diag(4,2,1,1/2) Qᵀ, calculer ‖A‖op et ‖A⁻¹‖op en norme euclidienne. Donner une direction qui atteint chacun des gains.

### Correction guidée

**Corrigé.** Les transformations orthogonales conservent la norme, donc ‖A‖op=4 et ‖A⁻¹‖op=2. Les directions Qe₁ et Qe₄ réalisent respectivement ces gains. Le conditionnement euclidien vaut 8. Ce calcul repose sur la structure spectrale symétrique positive ; pour une matrice générale, utiliser les valeurs singulières, pas uniquement le module des valeurs propres.

## 36. Évaluation contre dérivation

**Spé · TP : applications_lineaires**

**Énoncé.** Sur les polynômes munis de ‖·‖∞ sur [0,1], comparer v(P)=P(1) et u(P)=P′(1). Pourquoi la linéarité commune ne donne-t-elle pas la même propriété de continuité ?

### Correction guidée

**Corrigé.** On a |v(P)|≤‖P‖∞ et la constante 1 est atteinte par P=1, donc v est continue de norme 1. Pour u, les Pₙ=xⁿ/n tendent uniformément vers zéro mais Pₙ′(1)=1 ; u est non continue. La borne uniforme sur la boule unité est le critère pertinent, et non la seule linéarité.

## 37. Une suite de pics normalisés

**Spé → au-delà · TP : normes_dimension_infinie**

**Énoncé.** Pour fₙ(x)=√(2n+1)xⁿ, calculer les normes 1, 2 et ∞. Conclure sur la convergence dans chacune et sur l’équivalence des normes.

### Correction guidée

**Corrigé.** ‖fₙ‖₂=1, ‖fₙ‖₁=√(2n+1)/(n+1)→0 et ‖fₙ‖∞=√(2n+1)→∞. La suite converge vers zéro en norme 1, ne converge pas vers zéro en norme 2 et est non bornée en norme uniforme. Une convergence dans des normes équivalentes serait simultanée ; ces comportements prouvent leur non-équivalence sur cet espace infini.

## 38. Une marche approchée par des fonctions continues

**Spé → au-delà · TP : normes_dimension_infinie**

**Énoncé.** Définir fₙ=0 sur [0,1/2−1/n], affine jusqu’à la valeur 1 en 1/2+1/n, puis constante 1, pour n≥3. Montrer qu’elle approche la marche g=𝟙_{x>1/2} en norme 1, mais pas uniformément.

### Correction guidée

**Corrigé.** L’erreur est nulle hors d’une bande de largeur 2/n et vaut au plus 1, donc ‖fₙ−g‖₁≤2/n ; un calcul des deux triangles donne exactement 1/(2n). La norme uniforme de l’erreur vaut 1/2, indépendamment de n, et g est discontinue. Une limite uniforme de fonctions continues serait continue, ce qui exclut également cette convergence uniforme.

## 39. Retrouver les constantes avant normalisation

**Spé · TP : boule_non_compacte**

**Énoncé.** Pour uₙ(t)=e^(int), calculer ‖uₙ‖₂ et ‖uₚ−u_q‖₂ pour p≠q. En déduire les résultats normalisés sans perdre le facteur √(2π).

### Correction guidée

**Corrigé.** ‖uₙ‖₂²=∫₀²π1dt=2π. La distance carrée vaut ∫(2−2cos((p−q)t))dt=4π, donc la distance vaut 2√π. Diviser chaque mode par √(2π) donne norme 1 et distance (2√π)/√(2π)=√2. Ce calcul prouve la non-compacité de la boule unité via la suite normalisée.

## 40. Combien de petites boules pour tous les modes ?

**Spé · TP : boule_non_compacte**

**Énoncé.** Peut-on couvrir tous les eₙ par un nombre fini de boules ouvertes de rayon 0,6 dans la norme 2 ? Comparer avec un dessin de seulement vingt modes.

### Correction guidée

**Corrigé.** Deux modes dans une même boule auraient une distance <1,2 par l’inégalité triangulaire, impossible puisque √2≈1,414. Chaque boule contient donc au plus un mode ; une infinité de boules est nécessaire. Vingt modes dessinés se couvrent par vingt boules, ce qui ne fournit aucune couverture de l’ensemble infini et ne prouve aucune compacité.

## 41. Les décimaux ne sont pas tous les réels

**Sup · TP : denombrer_rationnels**

**Énoncé.** Montrer que l’ensemble D={p10⁻ⁿ : p∈ℤ,n∈ℕ} des décimaux est dénombrable et dense dans ℝ. Donner un rationnel qui n’est pas décimal.

### Correction guidée

**Corrigé.** D est l’image de ℤ×ℕ, donc au plus dénombrable, et contient ℤ donc est infini dénombrable. Pour x∈ℝ, qₙ=⌊10ⁿx⌋10⁻ⁿ vérifie 0≤x−qₙ<10⁻ⁿ, donc qₙ→x. Le rationnel 1/3 n’est pas décimal : si 1/3=p/10ⁿ, alors 10ⁿ=3p, impossible puisque 3 ne divise pas une puissance de 10.

## 42. Une liste des couples

**Sup · TP : denombrer_rationnels**

**Énoncé.** Écrire les dix premiers couples de ℕ² en parcourant les diagonales n+m=0,1,2,… avec n croissant. Pourquoi aucun couple n’est-il oublié ?

### Correction guidée

**Corrigé.** La liste commence (0,0), (0,1), (1,0), (0,2), (1,1), (2,0), (0,3), (1,2), (2,1), (3,0). Le couple (n,m) apparaît sur la diagonale finie d’indice n+m et y possède une position unique. La construction porte sur toutes les diagonales, même si l’interface n’en affiche qu’un nombre fini.

## 43. Une diagonale explicite dans un tableau

**Sup → Spé · TP : diagonale_cantor**

**Énoncé.** Les quatre premières lignes commencent par 0101, 1100, 0011, 1010. Construire les quatre premiers chiffres de l’antidiagonale et préciser ce qui serait nécessaire pour conclure sur une liste infinie.

### Correction guidée

**Corrigé.** Les chiffres diagonaux sont 0,1,1,0 ; l’antidiagonale commence par 1,0,0,1. Ce préfixe distingue le nouveau mot de chacune des quatre lignes au chiffre correspondant. Pour une liste infinie, il faut définir dₙ pour chaque n et utiliser la contradiction à un rang quelconque k ; quatre chiffres seuls ne suffisent pas.

## 44. Pourquoi des chiffres ternaires 0 et 2 ?

**Sup → Spé · TP : diagonale_cantor**

**Énoncé.** Deux suites binaires diffèrent pour la première fois au rang k, numéroté à partir de zéro. Minorer l’écart de leurs encodages ternaires. Peut-il être nul à cause de deux écritures d’un même réel ?

### Correction guidée

**Corrigé.** La contribution du premier chiffre vaut 2/3ᵏ⁺¹. La queue est majorée par Σn>k2/3ⁿ⁺¹=1/3ᵏ⁺¹. L’écart total est donc au moins 1/3ᵏ⁺¹>0. L’encodage est injectif. L’ambiguïté générale des écritures ternaires met en jeu un chiffre 1 dans l’écriture concurrente ; elle n’identifie pas deux suites distinctes utilisant uniquement 0 et 2.

## 45. Étapes finies et ensemble limite

**Sup → Spé · TP : ensemble_cantor**

**Énoncé.** Au rang n=5, combien d’intervalles subsistent, quelle est leur longueur et leur longueur totale ? Pourquoi ces valeurs ne donnent-elles pas le cardinal de C ?

### Correction guidée

**Corrigé.** Il subsiste 2⁵=32 intervalles de longueur 3⁻⁵=1/243, et leur longueur totale vaut 32/243≈0,131687. Chaque intervalle contient déjà une infinité non dénombrable de points ; le nombre d’intervalles ne compte donc pas les points. La non-dénombrabilité de C limite repose sur l’encodage des suites infinies, tandis que la longueur totale tend vers zéro.

## 46. Un point qui appartient encore à toutes les étapes

**Sup → Spé · TP : ensemble_cantor**

**Énoncé.** Vérifier que 1/4 appartient à C en utilisant son écriture ternaire. Trouver des points distincts de C qui convergent vers lui.

### Correction guidée

**Corrigé.** 1/4=Σk≥1 2/3²ᵏ=2/9·1/(1−1/9), donc son écriture ternaire est 0,020202… et utilise seulement 0 et 2. Modifier un seul chiffre à un rang de plus en plus grand donne des points distincts de C, à distance 2/3ⁿ du point initial. Ils convergent vers 1/4 et démontrent son caractère non isolé.

## 47. Une fonction déterminée par ses valeurs rationnelles

**Sup → Spé · TP : rationnels_irrationnels**

**Énoncé.** f:ℝ→ℝ est continue et vérifie f(q)=q² pour tout q rationnel. Déterminer f(x) pour tout réel. Que se passe-t-il si la continuité est retirée ?

### Correction guidée

**Corrigé.** La fonction g(x)=x² est continue ; f et g sont égales sur ℚ dense, donc f=g sur ℝ. Sans continuité, on peut définir f(x)=x² pour les rationnels et x²+1 pour les irrationnels ; l’égalité rationnelle ne détermine plus les autres valeurs.

## 48. L’intersection de deux denses peut être vide

**Sup → Spé · TP : rationnels_irrationnels**

**Énoncé.** Prendre A=ℚ et B=ℝ∖ℚ. Donner leurs intérieurs, adhérences et intersection. Comparer avec l’hypothèse de l’exercice 8 du recueil.

### Correction guidée

**Corrigé.** A°=B°=∅ et Ā=B̄=ℝ, mais A∩B=∅. Ni A ni B n’est ouvert dans ℝ. L’exercice 8 exige qu’un des deux denses soit ouvert pour que chaque premier point trouvé conserve un petit voisinage dans lequel on peut appliquer la seconde densité.

## 49. Tous les points de la verticale sont adhérents

**Spé → au-delà · TP : sinus_topologue**

**Énoncé.** Construire une suite de points de G tendant vers (0,1/2), puis une autre vers (0,−1). Pourquoi un simple préfixe du graphe ne suffit-il pas ?

### Correction guidée

**Corrigé.** Pour 1/2, prendre xₙ=1/(π/6+2πn), donnant sin(1/xₙ)=1/2. Pour −1, prendre xₙ=1/(3π/2+2πn). Les deux abscisses tendent vers zéro. Un graphe limité à x≥δ>0 reste à une distance positive de la verticale et ne contient pas ces abscisses tardives : l’adhérence du graphe infini dépasse celle du préfixe dessiné.

## 50. Classifier le graphe sans sa verticale

**Spé → au-delà · TP : sinus_topologue**

**Énoncé.** G seul est-il fermé, compact, connexe et connexe par arcs ? Comparer avec S et expliquer quelle propriété est conservée par l’adhérence.

### Correction guidée

**Corrigé.** G est connexe par arcs : relier deux abscisses positives dans ]0,1] puis composer avec le graphe. Il est borné mais non fermé, puisque (0,0) par exemple est une limite absente ; il n’est donc pas compact. S est fermé borné compact et connexe, mais non connexe par arcs. L’adhérence conserve la connexité, pas la connexité par arcs.

## 51. Déterminant positif ne veut pas dire égal à un

**Spé · TP : gl_composantes**

**Énoncé.** Pour A=diag(2,1,1,3), préciser l’appartenance à GL₄⁺(ℝ), SL₄(ℝ) et O(4). Construire un chemin dans GL₄⁺ vers I.

### Correction guidée

**Corrigé.** det A=6>0, donc A∈GL₄⁺, mais A∉SL₄ car 6≠1. Elle n’est pas orthogonale car AᵀA=diag(4,1,1,9)≠I. Le chemin diag(2−t,1,1,3−2t), t∈[0,1], reste à coefficients diagonaux positifs et aboutit à I. Le déterminant varie tout en restant strictement positif.

## 52. Une matrice singulière approchée par les deux signes

**Spé · TP : gl_composantes**

**Énoncé.** Pour A₀=diag(0,1,2,3), construire deux suites inversibles de déterminants de signes opposés convergeant vers A₀. Déduire que la frontière de GL contient A₀.

### Correction guidée

**Corrigé.** Aₙ⁺=diag(1/n,1,2,3) et Aₙ⁻=diag(−1/n,1,2,3) ont des déterminants ±6/n et convergent en norme de Frobenius vers A₀. Le point A₀ n’appartient pas à GL mais est dans son adhérence ; comme GL est ouvert, A₀ est sur sa frontière. Plus généralement la frontière de GL est l’ensemble det=0, par ouverture et densité.

## 53. Une matrice à quatre directions

**Spé · TP : orthogonal_compact**

**Énoncé.** Pour Q=diag(Rθ,Rφ), où Rα est la rotation plane d’angle α, calculer determinant, norme de Frobenius et norme d’opérateur. Montrer qu’une conjugaison orthogonale dense conserve ces valeurs.

### Correction guidée

**Corrigé.** Chaque bloc a un déterminant 1 ; det Q=1. Q est orthogonale, donc ‖Q‖F=√4=2 et ‖Q‖op=1. Pour une matrice orthogonale S, SQSᵀ reste orthogonale, de même déterminant et de mêmes valeurs singulières ; ses normes restent 2 et 1. Le choix de base change les coefficients mais pas la géométrie intrinsèque.

## 54. Un volume conservé peut s’accompagner d’une fuite à l’infini

**Spé · TP : orthogonal_compact**

**Énoncé.** Pour A_t=diag(eᵗ,e⁻ᵗ,1,1), calculer le déterminant, la plus grande valeur singulière et le conditionnement pour t≥0. Que devient la compacité d’un ensemble contenant tous ces A_t ?

### Correction guidée

**Corrigé.** Le déterminant vaut 1, σmax=eᵗ et σmin=e⁻ᵗ ; le conditionnement euclidien vaut e²ᵗ. Les normes sont non bornées quand t→∞, donc aucun compact de M₄(ℝ) ne contient toute la famille. La conservation du volume ne borne ni les longueurs ni la sensibilité de l’inversion.

## 55. Combien d’itérations pour cos ?

**Spé → au-delà · TP : point_fixe**

**Énoncé.** Pour x₀=0 et xₙ₊₁=cos xₙ, donner une borne suffisante sur n pour une erreur <10⁻⁵, en utilisant q=sin1. Pourquoi cette borne peut-elle être pessimiste ?

### Correction guidée

**Corrigé.** d(x₁,x₀)=1, donc l’erreur est ≤qⁿ/(1−q). Il suffit de choisir n avec qⁿ<10⁻⁵(1−q), soit n>ln(10⁻⁵(1−q))/ln(q), environ 77,4 ; n=78 convient. Le taux q majore la dérivée sur tout [0,1], alors que près du fixe la valeur |sin x*|≈0,674 est plus petite ; l’erreur observée peut décroître plus vite.

## 56. Un fixe répulsif et un cycle

**Spé → au-delà · TP : point_fixe**

**Énoncé.** Pour T(x)=−1,1x+2, déterminer le point fixe et décrire l’itération depuis x₀=0. Reprendre avec T(x)=−x+2.

### Correction guidée

**Corrigé.** Le premier fixe est 2/2,1=20/21 ; l’erreur vaut (−1,1)ⁿ(−20/21), alterne et augmente en module. Le fixe existe mais est répulsif. Pour T(x)=−x+2, le fixe vaut 1 et depuis zéro l’itération alterne 0,2,0,2,… ; elle ne converge pas. Le seuil strict |a|<1 est donc indispensable à la conclusion générale de convergence.

## 57. Le seuil critique, strict ou large ?

**Spé · TP : chemins_niveaux**

**Énoncé.** Pour a=b=1, montrer que {F₁≤1} est connexe par arcs et que {F₁<1} possède deux composantes. Le point zéro appartient-il à chacun des deux ensembles ?

### Correction guidée

**Corrigé.** En polaires, F₁≤1 équivaut à r²(r²−2cos2θ)≤0. Pour une direction où cos2θ≥0, les rayons 0≤r≤√(2cos2θ) sont admis ; chaque point se relie à zéro par son segment radial. Zéro appartient au sous-niveau large car F₁(0)=1. Le sous-niveau strict l’exclut et n’a aucun point sur x=0 ; ses deux lobes ouverts, chacun connexe par arcs, sont séparés.

## 58. Bornitude d’un sous-niveau quartique

**Spé · TP : chemins_niveaux**

**Énoncé.** Utiliser les distances aux foyers pour obtenir une borne radiale simple sur C_{a,b}. Pour a=1,b=2, donner un rayon de boule fermée contenant cet ensemble.

### Correction guidée

**Corrigé.** Pour r=√(x²+y²)≥a, chaque distance à un foyer est ≥r−a. Ainsi F_a≥(r−a)⁴. Si F_a≤b⁴, alors r−a≤b, donc r≤a+b. Les points de r<a satisfont aussi cette borne. C_{1,2} est contenu dans la boule fermée de rayon 3 ; une borne plus fine est possible, mais celle-ci suffit à la compacité avec la fermeture.

## 59. Une courbe gauche conserve la topologie du segment

**Spé · TP : homeomorphisme**

**Énoncé.** Pour g:[−1,1]→ℝ³, g(t)=(t,t²,t³), prouver l’injectivité, la compacité de l’image et la continuité de l’inverse. Déterminer si l’image est connexe par arcs et convexe.

### Correction guidée

**Corrigé.** La première coordonnée égale t, donc g est injective et son inverse sur l’image est la projection (x,y,z)↦x, continue. L’image d’un compact est compacte et celle d’un intervalle est connexe par arcs. Elle n’est pas convexe : le milieu de g(−1)=(-1,1,-1) et g(1)=(1,1,1) est (0,1,0), absent car g(0)=(0,0,0).

## 60. Une bijection entre deux infinis n’est pas une ressemblance topologique

**Spé · TP : homeomorphisme**

**Énoncé.** Expliquer pourquoi une bijection ensembliste entre ℝ et ℝ² ne peut être un homéomorphisme. Quel invariant simple détecte la différence après retrait d’un point ?

### Correction guidée

**Corrigé.** Le cardinal des deux ensembles est le même, mais un homéomorphisme préserverait la connexité de leurs complémentaires de points correspondants. ℝ∖{a} possède deux composantes, tandis que ℝ²∖{p} reste connexe par arcs. Cette contradiction, démontrée dans l’exercice 7, montre que la topologie contient une information supplémentaire par rapport au cardinal.
