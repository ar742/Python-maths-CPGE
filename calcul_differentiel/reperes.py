"""Repères pour commencer chaque expérience, sans changer ses calculs."""


def guide(purpose, objects, hypotheses, techniques, steps, sup, spe, beyond, expected):
    return dict(purpose=purpose, objects=objects.split(' | '),
                hypotheses=hypotheses.split(' | '), techniques=techniques.split(' | '),
                first_steps=steps, levels=dict(sup=sup, spe=spe, beyond=beyond), expected=expected)


LAB_GUIDES = {
    'jacobiennes': guide(
        'Comprendre comment un petit déplacement des coordonnées devient un déplacement du point. Comparer la transformation réelle à son approximation par la jacobienne.',
        'ρ est la distance à l’origine ; θ est l’azimut ; φ est la colatitude, mesurée depuis l’axe vertical. En cylindrique, z est l’altitude. | Les angles des curseurs sont en degrés ; les formules et les dérivées angulaires utilisent les radians. Les longueurs sont en unités arbitraires. | F envoie les coordonnées sur le point ; J est sa matrice jacobienne. Le paramètre h règle la taille de la petite face dessinée.',
        'Une carte sphérique régulière exige ρ>0 et 0<φ<π. | Une projection plane représente la figure en trois dimensions ; elle ne conserve pas toutes les distances.',
        'Dérivées partielles et matrice d’une application linéaire | Déterminant, orientation et approximation affine',
        ['Choisir « Carte régulière » et identifier les directions radiale et angulaires.', 'Diminuer h : la face transformée se rapproche de celle obtenue avec J.', 'Choisir le pôle : expliquer pourquoi modifier θ ne déplace plus le point.'],
        'Trigonométrie, déterminant et transformation des vecteurs de base.',
        'Différentielle, jacobienne et règle de la chaîne : programme MP.',
        'Cartes de coordonnées, inversion locale et changement de variables dans une intégrale multiple.',
        'Un déterminant nul peut signaler une singularité des coordonnées, alors que F reste régulière.'),
    'elliptique': guide(
        'Calculer une intégrale sur un quart d’ellipse en revenant à un quart de disque. Observer le rôle du facteur qui transforme les aires.',
        'a et b sont les demi-axes positifs de l’ellipse. x et y sont les coordonnées ; les longueurs sont en unités arbitraires. | α et β sont les coefficients de l’intégrande αx³−βy². r est le rayon du disque unité et θ son angle, en radians. | Ω est le quart d’ellipse ; J est la jacobienne de x=ar cosθ, y=br sinθ. Le nombre de nœuds règle la quadrature numérique.',
        'On intègre sur x≥0, y≥0 et x²/a²+y²/b²≤1. | La substitution utilise 0≤r≤1 et 0≤θ≤π/2 ; le facteur d’aire est |det J|=ab r.',
        'Substitution et calcul de primitives | Déterminant d’une jacobienne et séparation des variables',
        ['Choisir le TP et repérer les demi-axes sur la figure.', 'Comparer le résultat exact au résultat obtenu sans le facteur ab r.', 'Augmenter les nœuds : distinguer erreur de quadrature et oubli du changement de mesure.'],
        'Primitives, trigonométrie et intégration sur un intervalle.',
        'Calcul de jacobiennes ; réinvestissement des techniques d’intégration.',
        'Le théorème de changement de variables pour les intégrales multiples dépasse le programme MPSI/MP.',
        'Changer les coordonnées transforme aussi les éléments d’aire : remplacer seulement x et y ne suffit pas.'),
    'taylor': guide(
        'Comparer une fonction à ses approximations du premier et du deuxième ordre. Apprendre ce qu’une coupe et une Hessienne permettent de conclure sur un extremum.',
        'Le point de base a possède les coordonnées x et y des curseurs. u est la direction unitaire choisie par l’angle ; t mesure le déplacement sur la droite a+tu. | h règle l’étendue de cette coupe. Les coordonnées et valeurs sont sans unité physique imposée. | ∇f est le gradient ; Hf est la Hessienne, matrice des dérivées secondes. Les restes sont les écarts entre f et les approximations.',
        'Les modes lisse et cubique satisfont les hypothèses de Taylor. | Dans le mode des dérivées directionnelles, le point est fixé à l’origine ; un chemin courbe complète l’étude des droites.',
        'Taylor, petits o et grands O | Points critiques, théorème spectral et signe d’une forme quadratique',
        ['Sur la fonction lisse, comparer les trois courbes puis réduire h.', 'Choisir une selle et changer la direction de coupe : chercher des variations de signes opposés.', 'À l’origine dégénérée, puis dans le mode des dérivées directionnelles, chercher pourquoi les tests précédents ne suffisent plus.'],
        'Taylor à une variable et étude locale d’une fonction.',
        'Gradient, Hessienne et conditions d’extremum : programme MP.',
        'Les dérivées dans toutes les directions ne suffisent pas à établir la différentiabilité.',
        'Un test concluant exige ses hypothèses ; une Hessienne dégénérée demande une étude complémentaire.'),
    'matrices': guide(
        'Approcher det(A+tH) et l’inverse de A+tH au voisinage de t=0. Comprendre pourquoi l’ordre des facteurs et l’inversibilité comptent.',
        'A est la matrice réelle 2×2 réglée par ses quatre coefficients. H=[[0,3 ; 1], [−0,7 ; 0,2]] est la direction fixée. | t est un paramètre réel sans unité ; I est la matrice identité. Ddet(A)[H] et Dinv(A)[H] sont les dérivées dans la direction H. | Tr est la trace ; GLₙ(ℝ) est l’ensemble des matrices inversibles. Le conditionnement mesure la sensibilité de l’inverse.',
        'Le déterminant est différentiable sur toutes les matrices. | L’inverse ne se différencie que si A est inversible ; le logiciel annonce son seuil numérique.',
        'Multilinéarité du déterminant et cofacteurs | Différentiation d’un produit matriciel',
        ['Partir de l’identité et retrouver Ddet(I)[H]=Tr H.', 'Prendre une matrice presque singulière : observer la zone où l’approximation reste utile.', 'Choisir la matrice singulière : conserver l’étude du déterminant et expliquer l’absence de celle de l’inverse.'],
        'Calcul matriciel, déterminants et inverse.',
        'Différentielle d’une application entre espaces de matrices.',
        'Lien entre trace et espace tangent du groupe des matrices de déterminant 1.',
        'La formule de l’inverse contient −A⁻¹HA⁻¹ ; déplacer H demande une commutation.'),
    'optimisation': guide(
        'Relier les valeurs propres à la forme des courbes de niveau et à la convergence d’une descente. Comparer cette méthode à Newton, puis étudier le quotient de Rayleigh.',
        'A est une matrice réelle symétrique définie positive ; λ₁ et λ₂ sont ses valeurs propres. La rotation oriente ses axes propres. | En descente, x=(x,y) est le point courant et B le vecteur donné dans le tableau. α est le pas ; le curseur règle αλmax. x* est le minimum. | En mode Rayleigh, u est une direction unitaire et R(u)=uᵀAu/(uᵀu). Les angles des réglages sont en degrés, ceux des développements en radians.',
        'Les deux valeurs propres sont strictement positives. | La descente converge pour tout départ si 0<α<2/λmax. | Newton atteint exactement le minimum d’une quadratique en un pas, à l’arrondi près.',
        'Gradient et résolution de Ax=B | Diagonalisation orthogonale et étude d’une suite géométrique',
        ['Comparer descente et Newton avec le préréglage stable.', 'Augmenter le facteur du pas au-delà de 2 : relier l’évolution à une direction propre.', 'Passer à Rayleigh et approcher un axe propre : mesurer l’erreur du quotient.'],
        'Systèmes linéaires, produit scalaire et suites géométriques.',
        'Théorème spectral, formes quadratiques et optimisation au second ordre.',
        'Méthodes numériques de descente et de Newton ; précision du quotient de Rayleigh.',
        'Le plus grand axe spectral impose le pas ; une erreur de direction peut donner une erreur quadratique du quotient.'),
    'lie': guide(
        'Retrouver les contraintes sur une vitesse de transformation matricielle, puis observer comment son exponentielle agit sur un cercle.',
        'n vaut 2 ou 3 ; I est l’identité. GLₙ, SLₙ et SOₙ désignent respectivement les matrices inversibles, de déterminant 1 et les rotations. | X et Y sont les matrices tangentes construites avec les paramètres a,b,c ; leurs valeurs figurent dans le tableau. t et s sont des paramètres sans unité physique. | exp(tX) est l’exponentielle matricielle. [X,Y]=XY−YX est le crochet ; la norme de Frobenius est la racine de la somme des carrés des coefficients.',
        'SO impose Xᵀ=−X ; SL impose Tr X=0 ; GL ne restreint pas X. | La figure en dimension 3 est une projection plane. | Les quotients aux très petits pas sont sensibles à l’arrondi.',
        'Différentiation d’une identité matricielle | Développement limité de l’exponentielle et non-commutation',
        ['Choisir SO(3) et relier l’antisymétrie de X à la conservation des longueurs.', 'Passer à SL et comparer trace nulle et déterminant de exp(tX).', 'Comparer SO(2) et SO(3) : suivre l’erreur du commutateur divisé par s².'],
        'Matrices, trace, déterminant et rotations du plan.',
        'Différentiation et isométries euclidiennes fournissent les outils de calcul.',
        'La théorie des groupes et algèbres de Lie est un prolongement ; elle n’est pas un chapitre exigible MPSI/MP.',
        'Une contrainte non linéaire sur le groupe donne une contrainte linéaire sur son espace tangent.'),
    'gaussienne': guide(
        'Calculer une intégrale gaussienne décentrée en complétant le carré. Lire son centre et son étalement dans les dérivées de son logarithme.',
        'n est la dimension ; x∈ℝⁿ est la variable d’intégration. A est une matrice symétrique définie positive, réglée par ses valeurs propres et une rotation. | B est le vecteur du terme linéaire ; B₁ et B₂ sont ses deux premières coordonnées. γ règle les autres valeurs propres de A. | I(A,B) intègre exp(−xᵀAx/2+Bᵀx). μ=A⁻¹B est le centre ; Σ=A⁻¹ est la covariance après normalisation. Les variables sont sans unité physique imposée.',
        'La positivité définie de A assure la convergence de l’intégrale. | La quadrature porte sur les deux premières coordonnées ; les autres intégrales sont exactes. | La troncature à six écarts types et la quadrature produisent deux erreurs distinctes.',
        'Compléter le carré et diagonaliser une matrice symétrique | Dérivation sous l’intégrale avec justification',
        ['Partir de la gaussienne centrée et comparer les étalements des deux axes.', 'Modifier B₁ et B₂ : comparer déplacement du centre et forme des ellipses.', 'Augmenter les nœuds de quadrature et comparer l’erreur à la borne de masse omise.'],
        'Compléter le carré et intégrer une gaussienne à une variable.',
        'Théorème spectral et intégrales à paramètre.',
        'Intégrales multiples et lois à densité multivariées sont ici des prolongements hors programme MPSI/MP.',
        'B déplace le centre ; A détermine l’étalement. Les ellipses sont des niveaux de densité.'),
    'green_fubini': guide(
        'Comparer une intégrale sur un contour à une intégrale sur son intérieur. Puis étudier un exemple où changer l’ordre d’intégration change le résultat.',
        'x et y sont les coordonnées du plan. En mode Green, Ω est le domaine entre y=x² et y=x, avec 0≤x≤1. Les composantes du champ sont P=y(y+x) et Q=0 ; le contour positif est parcouru dans le sens antihoraire. | En mode Fubini, f(x,y)=(x²−y²)/(x²+y²)² sur le carré unité hors de l’origine. εx et εy sont les coupures positives : on intègre sur [εx,1]×[εy,1]. | Les réglages log₁₀ εx et log₁₀ εy donnent les puissances de 10 correspondantes. I est l’intégrale sur ce rectangle tronqué ; les coordonnées sont sans unité physique.',
        'Green demande un champ suffisamment régulier et une orientation cohérente. | L’exemple singulier n’est pas absolument intégrable au voisinage de l’origine. | Les valeurs sur les rectangles tronqués ne définissent pas à elles seules une intégrale sur le carré entier.',
        'Paramétrer et intégrer sur chaque morceau d’un contour | Primitives, limites et vérification des hypothèses',
        ['Comparer les deux calculs en mode Green puis inverser l’orientation.', 'Choisir des coupures symétriques : expliquer l’annulation par échange de x et y.', 'Rendre les coupures inégales et les réduire : comparer les limites obtenues.'],
        'Primitives, intégration par morceaux et limites.',
        'Intégrabilité et passage à la limite : les hypothèses précèdent les manipulations.',
        'Green et Fubini pour les intégrales multiples prolongent les techniques du programme MPSI/MP.',
        'Une orientation change un signe ; un défaut d’intégrabilité peut empêcher d’échanger les intégrales.')
}
