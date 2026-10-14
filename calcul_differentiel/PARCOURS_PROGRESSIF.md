# Calcul différentiel & Transformations : un parcours sup / spé

Partir d’une approximation à une variable, puis construire la différentielle comme application linéaire. Relier ensuite jacobiennes, matrices, extrema et contraintes avant de choisir les prolongements.

Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les approfondissements et les branches au-delà du programme se choisissent ensuite, indépendamment.

Repères MPSI / MP : dérivées partielles en sup ; différentielle, règle de la chaîne, gradients, Hessienne, Taylor–Young d’ordre 2 et optimisation sous contrainte en MP. Les groupes de Lie, les intégrales multiples, Green–Riemann et Fubini sont des prolongements. Le parcours distingue ces théories des calculs d’intégration et de matrice qui leur servent de point d’entrée.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : dérivation, développements limités, primitives, trigonométrie et matrices.
- Fin de sup : fonctions de deux variables et dérivées partielles.
- Spé : espaces euclidiens, théorème spectral, topologie en dimension finie et calcul différentiel.

## Pour chaque séance

1. Lire les objets, les notations et les hypothèses du TP.
2. Prévoir un résultat sur papier, puis ouvrir l’expérience.
3. Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.
4. Conclure par une courte preuve et distinguer résultat exact, approximation et observation.

## Sup : deux séances pour préparer la différentielle

Les expériences sont abordées par des courbes et des calculs accessibles à une variable.

### 1. Dériver le long d’une droite

**Techniques incontournables** · Sup · dérivées et approximation affine

Comprendre une dérivée directionnelle à partir d’une fonction d’une variable.

**À faire :** Noter a le point de base, u une direction unitaire et t le déplacement. Pour la fonction lisse du TP, étudier φ(t)=f(a+tu) : calculer φ′(0), comparer la tangente puis réduire l’intervalle h.

**Acquis attendu :** Distinguer la pente dans une direction, les dérivées partielles et l’erreur d’approximation.

**Limites et compléments :** À ce palier, rester sur la courbe φ. La notion complète de différentielle et la classification par Hessienne arrivent en spé.

**TP associés :** La fonction, sa tangente et sa courbure

### 2. Des coordonnées transforment des vecteurs

**Techniques incontournables** · Sup · trigonométrie et dérivées partielles

Identifier les directions radiale, angulaire et verticale.

**À faire :** Partir des coordonnées polaires x=ρcosθ,y=ρsinθ, puis cylindriques en ajoutant z. Noter ρ le rayon et θ l’angle en radians dans les dérivées ; calculer les deux colonnes des dérivées partielles et leur déterminant.

**Acquis attendu :** Retrouver le facteur ρ et expliquer la perte d’une direction lorsque ρ=0 ; ne pas confondre les degrés des curseurs avec les radians du calcul.

**Limites et compléments :** Le calcul de la matrice est accessible en sup ; son interprétation comme matrice d’une différentielle sera formalisée en spé.

**TP associés :** Une jacobienne transforme les directions

## Spé : quatre séances incontournables

La linéarité, les hypothèses et la preuve d’extremum précèdent l’observation des graphiques.

### 3. Une application linéaire tangente

**Techniques incontournables** · Spé · différentielle et règle de la chaîne

Passer d’un calcul de dérivées à une approximation valable pour tous les petits déplacements.

**À faire :** Noter F la transformation de coordonnées et J sa jacobienne au point de base. Comparer F(a+v)−F(a) à Jv lorsque le déplacement v diminue ; en sphérique, expliquer la singularité au pôle. Vérifier la dérivée d’une composée.

**Acquis attendu :** Écrire F(a+v)=F(a)+Jv+o(‖v‖) et distinguer dérivées directionnelles et différentiabilité dans le mode pathologique.

**Limites et compléments :** Une image qui se rapproche soutient le calcul du reste ; elle ne démontre pas à elle seule la différentiabilité.

**TP associés :** Une jacobienne transforme les directions ; La fonction, sa tangente et sa courbure

### 4. Différencier le déterminant et l’inverse

**Techniques incontournables** · Spé · applications matricielles

Utiliser multilinéarité et dérivation d’un produit matriciel.

**À faire :** Noter A la matrice de base et H la direction fixée du TP. Partir de A=I, identité, puis dériver det(A+tH) à t=0. Pour l’inverse, dériver (A+tH)(A+tH)⁻¹=I et garder l’ordre des facteurs.

**Acquis attendu :** Retrouver Ddet(I)[H]=Tr H et Dinv(A)[H]=−A⁻¹HA⁻¹ ; expliquer pourquoi la seconde formule exige l’inversibilité.

**Limites et compléments :** Les formules se démontrent comme exercices. Le conditionnement et les seuils numériques sont des diagnostics, pas de nouvelles hypothèses algébriques.

**TP associés :** Différencier le déterminant et l’inverse

### 5. Point critique, Hessienne et conclusion

**Techniques incontournables** · Spé · Taylor–Young et théorème spectral

Distinguer conditions nécessaires, conditions suffisantes et cas dégénéré.

**À faire :** Noter ∇f le gradient et Hf la matrice hessienne. Dans le TP Taylor, comparer un minimum, une selle et un point dégénéré ; examiner plusieurs coupes. Pour la quadratique positive du TP optimisation, calculer son gradient puis compléter le carré.

**Acquis attendu :** Justifier un minimum strict par une Hessienne définie positive ; expliquer pourquoi une Hessienne seulement positive ne conclut pas toujours.

**Limites et compléments :** Hessienne et Taylor–Young d’ordre 2 sont au programme MP. La théorie abstraite de la différentielle seconde et les algorithmes de Newton restent hors du socle.

**TP associés :** La fonction, sa tangente et sa courbure ; Du gradient aux valeurs propres

### 6. Un extremum sous une contrainte

**Techniques incontournables** · Spé · quotient de Rayleigh

Relier optimisation sur la sphère et valeurs propres d’une matrice symétrique.

**À faire :** Choisir le mode Rayleigh et noter A la matrice symétrique, u un vecteur unitaire, R(u)=uᵀAu. Vérifier la régularité de la contrainte uᵀu=1 ; retrouver la condition Au=λu et comparer les valeurs aux axes propres.

**Acquis attendu :** Justifier l’existence sur la sphère compacte et les extrema égaux aux valeurs propres extrêmes.

**Limites et compléments :** Le calcul sous une contrainte régulière est au programme MP. Les méthodes d’itération pour trouver des vecteurs propres sont facultatives.

**TP associés :** Du gradient aux valeurs propres

## Approfondissements : deux ponts vers les applications

Les résultats nécessaires sont donnés ; priorité aux contrôles de calcul.

### 7. Du spectre au choix d’un pas

**Approfondissement CPGE** · Spé · suites géométriques et algorithme

Analyser une itération à partir de ses composantes propres.

**À faire :** Noter α le pas de descente, λmax la plus grande valeur propre et x* le minimum de la quadratique. Écrire la récurrence de l’erreur ; comparer αλmax<2 puis αλmax>2. Comparer avec Newton sur cette quadratique.

**Acquis attendu :** Déduire la condition 0<α<2/λmax et expliquer pourquoi Newton atteint ici le minimum en un pas, à l’arrondi près.

**Limites et compléments :** L’étude de suites géométriques et la diagonalisation sont le socle. Les méthodes de descente et de Newton sont des applications numériques accompagnées.

**TP associés :** Du gradient aux valeurs propres

### 8. Une contrainte de groupe donne une contrainte linéaire

**Approfondissement CPGE** · Spé · dériver une identité matricielle

Exercer la dérivation d’un produit et du déterminant avant d’introduire une théorie de Lie.

**À faire :** Noter M(t) une courbe matricielle avec M(0)=I et X=M′(0). Dériver M(t)ᵀM(t)=I puis det M(t)=1 ; retrouver Xᵀ=−X dans le premier cas et Tr X=0 dans le second.

**Acquis attendu :** Expliquer le passage d’une équation non linéaire sur M à une équation linéaire sur sa vitesse X.

**Limites et compléments :** La dérivation utilise les outils MP. Les groupes et algèbres de Lie, leurs représentations et leur classification ne sont pas au programme.

**TP associés :** Le tangent engendre une transformation

## Au-delà : trois branches à choisir

Les intégrales multiples et la théorie de Lie sont annoncées comme nouvelles, avec leurs définitions.

### A. Aires transformées, Green et Fubini

**Au-delà du programme** · Au-delà · intégrales multiples

Comprendre les facteurs de mesure et les hypothèses de permutation des intégrales.

**À faire :** Sur le quart d’ellipse, retrouver |det J|=abr, où a,b sont les demi-axes et r le rayon réduit. Dans Green, inverser l’orientation du contour. Dans Fubini, comparer des coupures symétriques et dissymétriques près de l’origine singulière.

**Acquis attendu :** Expliquer séparément facteur d’aire, signe d’orientation et défaut d’intégrabilité absolue.

**Limites et compléments :** Le changement de variables multiple, Green–Riemann et Fubini sont des prolongements hors du programme MPSI / MP ; primitives et limites restent les outils de calcul.

**TP associés :** L’intégrale change avec la mesure ; Intégrer : orientation et hypothèses

### B. Une gaussienne en plusieurs dimensions

**Au-delà du programme** · Au-delà · intégrales et probabilités multivariées

Compléter le carré et interpréter une matrice symétrique positive.

**À faire :** Noter A la matrice définie positive, B le terme linéaire et μ=A⁻¹B le centre. Retrouver la complétion du carré dans exp(−xᵀAx/2+Bᵀx), puis comparer les ellipses pour plusieurs valeurs de B.

**Acquis attendu :** Séparer le déplacement du centre, réglé par B, et l’étalement, réglé par A⁻¹ ; comparer quadrature et masse omise.

**Limites et compléments :** La diagonalisation et la complétion du carré réutilisent le programme. Intégrales multiples, covariance multivariée et dérivation de ces intégrales sont des prolongements fournis.

**TP associés :** Une intégrale révèle moyenne et covariance

### C. Exponentielle et crochet de Lie

**Au-delà du programme** · Au-delà · groupes et algèbres de Lie

Relier des matrices tangentes à des transformations finies et à leur défaut de commutation.

**À faire :** Noter X,Y les matrices tangentes et [X,Y]=XY−YX leur crochet. Comparer SO(2) et SO(3), puis observer exp(tX) et le quotient du commutateur par le carré d’un petit pas.

**Acquis attendu :** Relier antisymétrie à conservation des longueurs et trace nulle à conservation du déterminant ; distinguer identité exacte et développement limité.

**Limites et compléments :** L’exponentielle matricielle fait partie des outils MP. La structure de Lie et l’interprétation du crochet sont des prolongements ; les très petits pas sont sensibles à l’arrondi.

**TP associés :** Le tangent engendre une transformation

## Repères de programme

- [Programme officiel de mathématiques MPSI](https://prepas.org/ups.php?document=69)
- [Programme officiel de mathématiques MP](https://prepas.org/ups.php?document=85)
