# Un deuxième parcours en 60 minutes

Lancer `Lancer_Optimisation.cmd` depuis la racine, ou suivre [le lancement manuel](LISEZ_MOI.md).
Toutes les expériences se trouvent dans les onglets de la même application.

## 0–15 min · Le TP de cosinus

1. Garder l'intervalle [0,π/2], le degré 1 et le poids 0. Retrouver les coefficients du TP.
2. Comparer **I** et la **distance L²** : quelle relation les relie ?
3. Comparer les droites verte et dorée. Refaire la preuve par les trois erreurs alternées de la droite uniforme.
4. Passer au degré 3, puis 6. Observer l'erreur et le conditionnement en monômes.
5. Augmenter le poids κ : l'erreur près de la droite de l'intervalle compte davantage.

Leçons 2–4 ; exercices 1–4.

## 15–25 min · Matrices et dimension impaire

1. Faire varier θ. Retrouver le minimum et le maximum de la distance à S₃.
2. En dimension 3, expliquer pourquoi l'ensemble antisymétrique de déterminant 1 est vide.
3. Passer à n=4 : retrouver la borne √n avec les deux blocs J.
4. Déformer avec η : le déterminant reste 1, tandis que la norme augmente.
5. Activer le mode complexe, remettre η=0 et varier φ : distinguer transpose et adjoint.

Leçons 5–6 ; exercices 5–8.

## 25–35 min · Ellipsoïde et boîte maximale

1. Choisir « Ellipsoïde 3,2,1 ». Justifier les huit sommets et le volume maximal.
2. Déplacer le point avec longitude et latitude ; comparer sa valeur au maximum.
3. Choisir |x|²|y||z| : prédire les fractions optimales avant de lire le résultat.

Leçon 7 ; exercices 9–10.

## 35–45 min · Un point face à une surface

1. Faire tourner l'ellipsoïde ; observer que les deux extrema changent.
2. Choisir « Au centre ». Pourquoi les multiplicateurs deviennent-ils singuliers ?
3. Comparer la distance minimale à la surface et celle au solide.
4. Vérifier le cas de la sphère : distances |‖p−c‖−r| et ‖p−c‖+r sur la surface.

Leçon 8 ; exercice 11.

## 45–60 min · Deux ellipsoïdes et SVM

1. Garder les centres et axes distincts. Lire les bornes L,U et leur écart.
2. Faire tourner E₂ : pourquoi le segment minimal ne suit-il pas en général la droite des centres ?
3. Choisir les deux sphères et vérifier la distance avec la formule connue.
4. Approcher E₂, puis choisir les solides qui se recouvrent : interpréter le minimum annoncé.
5. Pour le cas séparé, retrouver le plan médian et sa marge. Relier ce problème au SVM de la fiche.
6. Exporter un résultat JSON pour conserver les paramètres et les contrôles.

Leçons 9–10 ; exercices 12–14. Les formules de support constituent l'ouverture de spé.

<!-- REPERES_EXPERIENCES -->

## Guides des expériences

Les repères distinguent les outils de sup, ceux de spé et les prolongements. Ils s’appuient sur les programmes de mathématiques [MPSI](https://prepas.org/ups.php?document=69) et [MP](https://prepas.org/ups.php?document=85).

### Approcher cosinus

Chercher une droite, puis un polynôme qui approche cos sur [0,L]. Comparer une erreur intégrée et le plus grand écart : ces deux critères ne choisissent pas la même droite.

**Objets et notations**

- t est la variable en radians ; L>0 fixe l’intervalle [0,L]

- p est le polynôme d’approximation ; pour la droite d’essai p(t)=at+b, a est la pente et b l’ordonnée à l’origine

- κ règle le poids w(t)=1+κt/L ; le degré limite les puissances de t

- I=∫₀ᴸ(cos t−p(t))²w(t)dt est le carré de la distance pondérée. Les valeurs sont sans unité physique

**Hypothèses**

- κ>−1 assure un poids positif ; 0<L≤π/2 pour la construction uniforme

- La droite dorée minimise le plus grand écart non pondéré ; la descente agit sur les paramètres d’une droite

**Techniques à mobiliser**

- Projection orthogonale sur un espace de dimension finie

- Intégration par parties et matrice de Gram

- Étudier une quadratique strictement convexe

**Trois premières manipulations**

1. Prendre degré 1, κ=0 et L=π/2 : retrouver les deux équations d’orthogonalité.

2. Comparer droite verte et droite dorée : identifier le critère minimisé.

3. Passer au degré 3 puis modifier κ : expliquer ce qui change dans le problème.

**Repères CPGE**

**Sup :** intégration, produit scalaire et projection orthogonale.

**Spé :** espaces préhilbertiens, orthogonalité et Hessienne.

**Au-delà :** approximation uniforme, descente de gradient et conditionnement numérique.

**À retenir :** Une valeur optimale, son point minimisant et la norme choisie sont trois informations à distinguer.

### Projeter une matrice

Décomposer une matrice en parties symétrique et antisymétrique. Utiliser cette projection pour calculer une distance, puis étudier la contrainte det A=1 selon la dimension.

**Objets et notations**

- n est la dimension de l’ensemble matriciel ; la rotation affichée est toujours une matrice réelle 3×3 d’angle θ

- Sₙ={M:Mᵀ=M} et Aₙ={M:Mᵀ=−M} utilisent la transposition

- La norme de Frobenius est ‖M‖F=√Σ|Mᵢⱼ|² ; M* est l’adjoint complexe

- η déforme deux blocs en dimension paire n≥4 ; φ est une phase en degrés utilisée seulement dans le mode complexe

**Hypothèses**

- Sur ℂ, symétrique signifie Mᵀ=M ; hermitienne signifie M*=M

- En dimension impaire, une matrice antisymétrique a déterminant nul : l’ensemble det=1 est vide

**Techniques à mobiliser**

- Décomposer M=(M+Mᵀ)/2+(M−Mᵀ)/2

- Calculer un déterminant et une norme

- Comparer les valeurs propres positives de M*M

**Trois premières manipulations**

1. Faire varier θ : retrouver la distance √2|sinθ| de la rotation à S₃.

2. Choisir n=3 : démontrer pourquoi det A=1 est impossible.

3. Passer à n=4 puis modifier η : comparer ‖A‖F à la borne √n.

**Repères CPGE**

**Sup :** transposée, déterminant, projection et dimension.

**Spé :** théorème spectral et formes positives.

**Au-delà :** distance sous contrainte de déterminant et comparaison transpose/adjoint sur ℂ.

**À retenir :** La projection orthogonale fixe la distance ; l’existence de l’ensemble contraint doit être vérifiée d’abord.

### Ellipsoïde et boîte maximale

Maximiser un produit de coordonnées sur un ellipsoïde. En déduire la boîte centrée de plus grand volume lorsque les trois exposants valent 1.

**Objets et notations**

- a,b,c>0 sont les demi-axes ; la surface vérifie x²/a²+y²/b²+z²/c²=1

- Les trois exposants positifs règlent |x|ᵖ|y|ᑫ|z|ʳ

- Longitude et latitude, en degrés dans les réglages, placent un point sur la surface

- Les demi-côtés de la boîte sont |x|,|y|,|z| ; son volume est 8|xyz|. Les longueurs sont dans une unité arbitraire cohérente

**Hypothèses**

- Ellipsoïde centré, axes alignés et exposants strictement positifs

- Les huit choix de signes donnent les mêmes valeurs ; la boîte dorée correspond seulement aux exposants 1,1,1

**Techniques à mobiliser**

- Ramener la contrainte à u+v+w=1

- Maximiser un logarithme

- Utiliser une inégalité entre moyenne arithmétique et produit

**Trois premières manipulations**

1. Choisir la sphère : prévoir les huit sommets optimaux.

2. Prendre les demi-axes 3,2,1 : retrouver le volume 8abc/(3√3).

3. Doubler l’exposant de |x| : prévoir la nouvelle répartition des carrés réduits.

**Repères CPGE**

**Sup :** Inégalités et changement de variables.

**Spé :** Gradients et existence des extrema d’une fonction continue sur un compact.

**Au-delà :** multiplicateurs de Lagrange et produits pondérés.

**À retenir :** Les coordonnées réduites permettent de séparer la géométrie de l’ellipsoïde et les exposants du produit.

### Distance d’un point

Trouver les points de la surface les plus proches et les plus éloignés d’un point p. Vérifier la différence entre distance à la surface et distance au solide.

**Objets et notations**

- p est le point choisi ; le centre fixe vaut (0,4;−0,2;0,1)

- a,b,c des curseurs « demi-axes » sont trois longueurs ; la lettre c du dessin désigne le centre, tandis que le curseur c désigne le troisième demi-axe

- R est la rotation réglée par trois angles en degrés ; un point de surface s’écrit centre+R diag(demi-axes)u, avec ‖u‖=1

- Les longueurs et distances partagent une unité arbitraire ; le niveau ellipsoïdal indique si p est dans le solide

**Hypothèses**

- Demi-axes strictement positifs ; on optimise sur toute la surface compacte

- Des extrema multiples sont possibles : le dessin choisit alors un représentant

**Techniques à mobiliser**

- Changer de repère orthonormé

- Minimiser un carré de norme

- Vérifier une contrainte et une condition de stationnarité

**Trois premières manipulations**

1. Prendre la sphère : comparer au calcul sur la droite centre–p.

2. Placer p au centre : prévoir le petit et le grand demi-axe.

3. Revenir à trois axes différents et tourner la surface : suivre les deux points extrémaux.

**Repères CPGE**

**Sup :** Distances euclidiennes et matrices de rotation.

**Spé :** Théorème spectral, formes quadratiques et compacité.

**Au-delà :** multiplicateurs, équation séculaire et cas singuliers.

**À retenir :** Un point intérieur a distance nulle au solide, mais une distance généralement positive à sa surface.

### Distance entre deux ellipsoïdes

Calculer la distance entre deux solides ellipsoïdaux orientés différemment. Encadrer ce minimum avec deux points admissibles et une direction de séparation.

**Objets et notations**

- E₁,E₂ sont les solides, définis par un centre, trois demi-axes et une rotation chacun

- x∈E₁ et y∈E₂ donnent U=‖y−x‖, une borne supérieure

- n est un vecteur unitaire ; les projections extrêmes sur n donnent une borne inférieure L≥0

- U−L mesure l’écart de l’encadrement. Les coordonnées et distances sont dans une même unité arbitraire ; les angles sont réglés en degrés

**Hypothèses**

- Les solides sont compacts et convexes ; leurs demi-axes sont positifs

- S’ils se recouvrent, leur distance est nulle ; la distance entre surfaces emboîtées est un autre problème

- Les bornes sont évaluées en virgule flottante

**Techniques à mobiliser**

- Appliquer Cauchy–Schwarz

- Calculer une fonction support

- Comparer une borne inférieure et une valeur admissible

**Trois premières manipulations**

1. Choisir deux sphères : vérifier max(0,D−r₁−r₂), avec D la distance des centres.

2. Prendre des orientations différentes : voir pourquoi le segment minimal ne suit pas nécessairement les centres.

3. Faire se recouvrir les solides : expliquer la distance nulle et l’absence de plan séparateur strict.

**Repères CPGE**

**Sup :** inégalité triangulaire, Cauchy–Schwarz et projection.

**Spé :** continuité sur un compact et formes quadratiques.

**Au-delà :** projections sur convexes, dualité et séparation à marge maximale (SVM).

**À retenir :** Un faible écart U−L contrôle la précision du minimum ; la seule stabilisation des itérations ne suffit pas.
