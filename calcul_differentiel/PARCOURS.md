# Un parcours de travail : conjecturer, calculer, démontrer

Le volet comprend **8 laboratoires, 14 leçons et 18 exercices**. Pour chaque séance,
écrire la conjecture avant de lire la correction. Les extensions Lie et gaussienne
sont accessibles avec des rappels, mais dépassent certaines filières CPGE.

## Séance 1 · Sup : linéariser et distinguer les notions · 45 min

Ouvrir **Différentielle & Taylor**, fonction lisse. Changer la direction ; comparer
fonction, tangente et parabole de Taylor. Exporter les restes puis estimer leur pente
en coordonnées logarithmiques. Lire les leçons 1 et 5.

Ouvrir **Chemin courbe**. Expliquer pourquoi une direction fixe ne voit pas le chemin
y=x³. Faire les exercices 1 et 7. Livrable : définition de la différentielle,
preuve de son unicité et contre-exemple « dérivées directionnelles ⇒ différentiabilité ».

## Séance 2 · Spé : les deux TP de coordonnées et d’intégrales · 60 min

Ouvrir **Jacobiennes**, comparer les trois systèmes. En sphérique, identifier les
colonnes, calculer le signe du déterminant et ouvrir le pôle singulier. Séparer
singularité de la carte et différentiabilité de F. Leçons 2 à 4 ; exercices 2 et 3.

Ouvrir **Intégrale elliptique** et **TP du recueil**. Retrouver les coefficients 81
et −4, puis le facteur 6r. Prédire l’effet d’un changement de demi-axe sur chaque
terme de l’intégrale. Vérifier numériquement puis rédiger la preuve exacte.
Exercices 4 et 5. Complément : lancer `tp_symbolique.py` après avoir calculé J à la main.

## Séance 3 · Spé : le TP matriciel · 45 min

Ouvrir **Matrices**, puis **À l’identité** et **Matrice singulière**. Pourquoi le
déterminant garde-t-il une différentielle, contrairement à l’inverse ? Choisir une
matrice presque singulière et observer les restes. Leçon 6 ; exercices 8 et 9.

Livrable : démontrer les deux différentielles et expliquer leur domaine de validité.
Pour n quelconque, relier cofacteurs, adjointe classique et trace.

## Séance 4 · Spé : Hessienne, Rayleigh et algorithmes · 60 min

Ouvrir les trois points critiques de l’**exercice 1**. Refaire les déterminants de
H ; expliquer le cas dégénéré par une coupe qui change de signe. Exercice 6.

Ouvrir **Rayleigh & Newton**. Faire varier l’orientation et l’écart spectral.
Comparer un pas stable, le seuil αλmax=2 et un pas trop grand. Expliquer Newton
en un pas sur cette quadratique. Ouvrir **Rayleigh**, puis approcher la direction
minimale. Leçons 7 et 8 ; exercices 10 à 12.

Livrable : distinguer Hessienne semi-définie, définie positive et stricte convexité ;
démontrer la condition de convergence et l’erreur quadratique du quotient.

## Séance 5 · Extension : la différentielle explique Lie · 60 min

Ouvrir **Algèbres de Lie**. Comparer GL, SL et SO en dimension 3. Vérifier trace,
déterminant et défaut d’orthogonalité dans les valeurs détaillées. Passer à SO(2) :
le crochet disparaît. Revenir à SO(3) et étudier le quotient du commutateur par s².
Leçons 9 et 10 ; exercices 13 et 14.

Livrable : calculer les espaces tangents par dérivation des contraintes, puis
établir les réciproques grâce à exp(tX). Développer le commutateur à l’ordre 2.
Faire le lien avec les commutateurs du volet Rubik, en distinguant les deux cadres.

## Séance 6 · Extension : l’intégrale gaussienne étendue · 60 min

Ouvrir **Gaussienne étendue**, puis **Exemple calculable**. Vérifier le résultat à
la main. Faire varier B₁ et B₂ : prédire le centre et la tangente à log I. Tourner
les axes ; augmenter la dimension puis la précision des axes suivants.

Lire les leçons 11 et 12. Faire les exercices 15 et 16. Livrable : compléter le
carré, diagonaliser, calculer la jacobienne et justifier les dérivées sous l’intégrale.
Interpréter les dérivées comme moments et covariance, en lien avec le volet probabilités.
Séparer la borne de troncature de l’erreur de quadrature observée.

## Séance 7 · Spé : les hypothèses d’intégration · 45 min

Dans **Green & Fubini**, retrouver l’orientation positive et la circulation −13/60.
Calculer par la frontière puis par le domaine ; inverser le sens. Exercice 17.

Ouvrir **Coupure symétrique**, puis **Coupures inégales**. Faire tendre les coupures
avec des vitesses différentes. Leçons 13 et 14 ; exercice 18. Livrable : expliquer
la divergence de l’intégrale absolue et le statut des deux intégrales itérées.

## Pour un oral

Choisir une figure, formuler précisément le résultat, annoncer ses hypothèses puis
donner une preuve de cinq minutes. Expliquer ce que le calcul numérique confirme
et ce qu’il ne peut pas prouver. Les corrections du recueil sont un bon exercice
de contrôle : vérifier une dérivée, un signe et une classification avant de conclure.

<!-- REPERES_EXPERIENCES -->

## Guides des expériences

Les repères distinguent les outils de sup, ceux de spé et les prolongements. Ils s’appuient sur les programmes de mathématiques [MPSI](https://prepas.org/ups.php?document=69) et [MP](https://prepas.org/ups.php?document=85).

### Coordonnées et jacobiennes

Comprendre comment un petit déplacement des coordonnées devient un déplacement du point. Comparer la transformation réelle à son approximation par la jacobienne.

**Objets et notations**

- ρ est la distance à l’origine ; θ est l’azimut ; φ est la colatitude, mesurée depuis l’axe vertical. En cylindrique, z est l’altitude.

- Les angles des curseurs sont en degrés ; les formules et les dérivées angulaires utilisent les radians. Les longueurs sont en unités arbitraires.

- F envoie les coordonnées sur le point ; J est sa matrice jacobienne. Le paramètre h règle la taille de la petite face dessinée.

**Hypothèses**

- Une carte sphérique régulière exige ρ>0 et 0<φ<π.

- Une projection plane représente la figure en trois dimensions ; elle ne conserve pas toutes les distances.

**Techniques à mobiliser**

- Dérivées partielles et matrice d’une application linéaire

- Déterminant, orientation et approximation affine

**Trois premières manipulations**

1. Choisir « Carte régulière » et identifier les directions radiale et angulaires.

2. Diminuer h : la face transformée se rapproche de celle obtenue avec J.

3. Choisir le pôle : expliquer pourquoi modifier θ ne déplace plus le point.

**Repères CPGE**

**Sup :** Trigonométrie, déterminant et transformation des vecteurs de base.

**Spé :** Différentielle, jacobienne et règle de la chaîne : programme MP.

**Au-delà :** Cartes de coordonnées, inversion locale et changement de variables dans une intégrale multiple.

**À retenir :** Un déterminant nul peut signaler une singularité des coordonnées, alors que F reste régulière.

### Une intégrale sur un quart d’ellipse

Calculer une intégrale sur un quart d’ellipse en revenant à un quart de disque. Observer le rôle du facteur qui transforme les aires.

**Objets et notations**

- a et b sont les demi-axes positifs de l’ellipse. x et y sont les coordonnées ; les longueurs sont en unités arbitraires.

- α et β sont les coefficients de l’intégrande αx³−βy². r est le rayon du disque unité et θ son angle, en radians.

- Ω est le quart d’ellipse ; J est la jacobienne de x=ar cosθ, y=br sinθ. Le nombre de nœuds règle la quadrature numérique.

**Hypothèses**

- On intègre sur x≥0, y≥0 et x²/a²+y²/b²≤1.

- La substitution utilise 0≤r≤1 et 0≤θ≤π/2 ; le facteur d’aire est |det J|=ab r.

**Techniques à mobiliser**

- Substitution et calcul de primitives

- Déterminant d’une jacobienne et séparation des variables

**Trois premières manipulations**

1. Choisir le TP et repérer les demi-axes sur la figure.

2. Comparer le résultat exact au résultat obtenu sans le facteur ab r.

3. Augmenter les nœuds : distinguer erreur de quadrature et oubli du changement de mesure.

**Repères CPGE**

**Sup :** Primitives, trigonométrie et intégration sur un intervalle.

**Spé :** Calcul de jacobiennes ; réinvestissement des techniques d’intégration.

**Au-delà :** Le théorème de changement de variables pour les intégrales multiples dépasse le programme MPSI/MP.

**À retenir :** Changer les coordonnées transforme aussi les éléments d’aire : remplacer seulement x et y ne suffit pas.

### Différentielle et Taylor

Comparer une fonction à ses approximations du premier et du deuxième ordre. Apprendre ce qu’une coupe et une Hessienne permettent de conclure sur un extremum.

**Objets et notations**

- Le point de base a possède les coordonnées x et y des curseurs. u est la direction unitaire choisie par l’angle ; t mesure le déplacement sur la droite a+tu.

- h règle l’étendue de cette coupe. Les coordonnées et valeurs sont sans unité physique imposée.

- ∇f est le gradient ; Hf est la Hessienne, matrice des dérivées secondes. Les restes sont les écarts entre f et les approximations.

**Hypothèses**

- Les modes lisse et cubique satisfont les hypothèses de Taylor.

- Dans le mode des dérivées directionnelles, le point est fixé à l’origine ; un chemin courbe complète l’étude des droites.

**Techniques à mobiliser**

- Taylor, petits o et grands O

- Points critiques, théorème spectral et signe d’une forme quadratique

**Trois premières manipulations**

1. Sur la fonction lisse, comparer les trois courbes puis réduire h.

2. Choisir une selle et changer la direction de coupe : chercher des variations de signes opposés.

3. À l’origine dégénérée, puis dans le mode des dérivées directionnelles, chercher pourquoi les tests précédents ne suffisent plus.

**Repères CPGE**

**Sup :** Taylor à une variable et étude locale d’une fonction.

**Spé :** Gradient, Hessienne et conditions d’extremum : programme MP.

**Au-delà :** Les dérivées dans toutes les directions ne suffisent pas à établir la différentiabilité.

**À retenir :** Un test concluant exige ses hypothèses ; une Hessienne dégénérée demande une étude complémentaire.

### Déterminant et inverse

Approcher det(A+tH) et l’inverse de A+tH au voisinage de t=0. Comprendre pourquoi l’ordre des facteurs et l’inversibilité comptent.

**Objets et notations**

- A est la matrice réelle 2×2 réglée par ses quatre coefficients. H=[[0,3 ; 1], [−0,7 ; 0,2]] est la direction fixée.

- t est un paramètre réel sans unité ; I est la matrice identité. Ddet(A)[H] et Dinv(A)[H] sont les dérivées dans la direction H.

- Tr est la trace ; GLₙ(ℝ) est l’ensemble des matrices inversibles. Le conditionnement mesure la sensibilité de l’inverse.

**Hypothèses**

- Le déterminant est différentiable sur toutes les matrices.

- L’inverse ne se différencie que si A est inversible ; le logiciel annonce son seuil numérique.

**Techniques à mobiliser**

- Multilinéarité du déterminant et cofacteurs

- Différentiation d’un produit matriciel

**Trois premières manipulations**

1. Partir de l’identité et retrouver Ddet(I)[H]=Tr H.

2. Prendre une matrice presque singulière : observer la zone où l’approximation reste utile.

3. Choisir la matrice singulière : conserver l’étude du déterminant et expliquer l’absence de celle de l’inverse.

**Repères CPGE**

**Sup :** Calcul matriciel, déterminants et inverse.

**Spé :** Différentielle d’une application entre espaces de matrices.

**Au-delà :** Lien entre trace et espace tangent du groupe des matrices de déterminant 1.

**À retenir :** La formule de l’inverse contient −A⁻¹HA⁻¹ ; déplacer H demande une commutation.

### Rayleigh, descente et Newton

Relier les valeurs propres à la forme des courbes de niveau et à la convergence d’une descente. Comparer cette méthode à Newton, puis étudier le quotient de Rayleigh.

**Objets et notations**

- A est une matrice réelle symétrique définie positive ; λ₁ et λ₂ sont ses valeurs propres. La rotation oriente ses axes propres.

- En descente, x=(x,y) est le point courant et B le vecteur donné dans le tableau. α est le pas ; le curseur règle αλmax. x* est le minimum.

- En mode Rayleigh, u est une direction unitaire et R(u)=uᵀAu/(uᵀu). Les angles des réglages sont en degrés, ceux des développements en radians.

**Hypothèses**

- Les deux valeurs propres sont strictement positives.

- La descente converge pour tout départ si 0<α<2/λmax.

- Newton atteint exactement le minimum d’une quadratique en un pas, à l’arrondi près.

**Techniques à mobiliser**

- Gradient et résolution de Ax=B

- Diagonalisation orthogonale et étude d’une suite géométrique

**Trois premières manipulations**

1. Comparer descente et Newton avec le préréglage stable.

2. Augmenter le facteur du pas au-delà de 2 : relier l’évolution à une direction propre.

3. Passer à Rayleigh et approcher un axe propre : mesurer l’erreur du quotient.

**Repères CPGE**

**Sup :** Systèmes linéaires, produit scalaire et suites géométriques.

**Spé :** Théorème spectral, formes quadratiques et optimisation au second ordre.

**Au-delà :** Méthodes numériques de descente et de Newton ; précision du quotient de Rayleigh.

**À retenir :** Le plus grand axe spectral impose le pas ; une erreur de direction peut donner une erreur quadratique du quotient.

### Groupes et algèbres de Lie

Retrouver les contraintes sur une vitesse de transformation matricielle, puis observer comment son exponentielle agit sur un cercle.

**Objets et notations**

- n vaut 2 ou 3 ; I est l’identité. GLₙ, SLₙ et SOₙ désignent respectivement les matrices inversibles, de déterminant 1 et les rotations.

- X et Y sont les matrices tangentes construites avec les paramètres a,b,c ; leurs valeurs figurent dans le tableau. t et s sont des paramètres sans unité physique.

- exp(tX) est l’exponentielle matricielle. [X,Y]=XY−YX est le crochet ; la norme de Frobenius est la racine de la somme des carrés des coefficients.

**Hypothèses**

- SO impose Xᵀ=−X ; SL impose Tr X=0 ; GL ne restreint pas X.

- La figure en dimension 3 est une projection plane.

- Les quotients aux très petits pas sont sensibles à l’arrondi.

**Techniques à mobiliser**

- Différentiation d’une identité matricielle

- Développement limité de l’exponentielle et non-commutation

**Trois premières manipulations**

1. Choisir SO(3) et relier l’antisymétrie de X à la conservation des longueurs.

2. Passer à SL et comparer trace nulle et déterminant de exp(tX).

3. Comparer SO(2) et SO(3) : suivre l’erreur du commutateur divisé par s².

**Repères CPGE**

**Sup :** Matrices, trace, déterminant et rotations du plan.

**Spé :** Différentiation et isométries euclidiennes fournissent les outils de calcul.

**Au-delà :** La théorie des groupes et algèbres de Lie est un prolongement ; elle n’est pas un chapitre exigible MPSI/MP.

**À retenir :** Une contrainte non linéaire sur le groupe donne une contrainte linéaire sur son espace tangent.

### Gaussienne étendue

Calculer une intégrale gaussienne décentrée en complétant le carré. Lire son centre et son étalement dans les dérivées de son logarithme.

**Objets et notations**

- n est la dimension ; x∈ℝⁿ est la variable d’intégration. A est une matrice symétrique définie positive, réglée par ses valeurs propres et une rotation.

- B est le vecteur du terme linéaire ; B₁ et B₂ sont ses deux premières coordonnées. γ règle les autres valeurs propres de A.

- I(A,B) intègre exp(−xᵀAx/2+Bᵀx). μ=A⁻¹B est le centre ; Σ=A⁻¹ est la covariance après normalisation. Les variables sont sans unité physique imposée.

**Hypothèses**

- La positivité définie de A assure la convergence de l’intégrale.

- La quadrature porte sur les deux premières coordonnées ; les autres intégrales sont exactes.

- La troncature à six écarts types et la quadrature produisent deux erreurs distinctes.

**Techniques à mobiliser**

- Compléter le carré et diagonaliser une matrice symétrique

- Dérivation sous l’intégrale avec justification

**Trois premières manipulations**

1. Partir de la gaussienne centrée et comparer les étalements des deux axes.

2. Modifier B₁ et B₂ : comparer déplacement du centre et forme des ellipses.

3. Augmenter les nœuds de quadrature et comparer l’erreur à la borne de masse omise.

**Repères CPGE**

**Sup :** Compléter le carré et intégrer une gaussienne à une variable.

**Spé :** Théorème spectral et intégrales à paramètre.

**Au-delà :** Intégrales multiples et lois à densité multivariées sont ici des prolongements hors programme MPSI/MP.

**À retenir :** B déplace le centre ; A détermine l’étalement. Les ellipses sont des niveaux de densité.

### Green et Fubini

Comparer une intégrale sur un contour à une intégrale sur son intérieur. Puis étudier un exemple où changer l’ordre d’intégration change le résultat.

**Objets et notations**

- x et y sont les coordonnées du plan. En mode Green, Ω est le domaine entre y=x² et y=x, avec 0≤x≤1. Les composantes du champ sont P=y(y+x) et Q=0 ; le contour positif est parcouru dans le sens antihoraire.

- En mode Fubini, f(x,y)=(x²−y²)/(x²+y²)² sur le carré unité hors de l’origine. εx et εy sont les coupures positives : on intègre sur [εx,1]×[εy,1].

- Les réglages log₁₀ εx et log₁₀ εy donnent les puissances de 10 correspondantes. I est l’intégrale sur ce rectangle tronqué ; les coordonnées sont sans unité physique.

**Hypothèses**

- Green demande un champ suffisamment régulier et une orientation cohérente.

- L’exemple singulier n’est pas absolument intégrable au voisinage de l’origine.

- Les valeurs sur les rectangles tronqués ne définissent pas à elles seules une intégrale sur le carré entier.

**Techniques à mobiliser**

- Paramétrer et intégrer sur chaque morceau d’un contour

- Primitives, limites et vérification des hypothèses

**Trois premières manipulations**

1. Comparer les deux calculs en mode Green puis inverser l’orientation.

2. Choisir des coupures symétriques : expliquer l’annulation par échange de x et y.

3. Rendre les coupures inégales et les réduire : comparer les limites obtenues.

**Repères CPGE**

**Sup :** Primitives, intégration par morceaux et limites.

**Spé :** Intégrabilité et passage à la limite : les hypothèses précèdent les manipulations.

**Au-delà :** Green et Fubini pour les intégrales multiples prolongent les techniques du programme MPSI/MP.

**À retenir :** Une orientation change un signe ; un défaut d’intégrabilité peut empêcher d’échanger les intégrales.
