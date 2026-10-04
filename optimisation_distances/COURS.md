# Optimisation & Distances — cours et exercices

Deuxième volet de **Python-maths-CPGE**, adapté des fiches de A. R. (TP p. 158, exercice 4 et exercice 6 p. 162), et du fichier `distMatrices.txt` fourni.

Les figures et les expériences interactives se lancent avec Python. Ce document donne les démonstrations et corrections à lire séparément.

## 1. Choisir l'objet et la distance

**Sup**

<p>La distance entre deux ensembles non vides est <b>d(A,B) = inf {‖a−b‖ : a∈A, b∈B}</b>.
    Elle peut être nulle sans intersection si les ensembles ne sont pas fermés. Pour deux compacts,
    le minimum est atteint ; s'ils sont disjoints, il est strictement positif.</p>
    <p>On peut minimiser la distance ou son carré : les minimiseurs sont identiques, car la fonction
    carré est croissante sur ℝ₊. Les valeurs optimales diffèrent : dans le TP,
    <b>I<sub>min</sub> = d(cos, Vect(1,t))²</b>. Ne pas confondre une intégrale d'erreur quadratique
    avec une distance, ni le minimum avec le maximum.</p>
    <p>Une surface ellipsoïdale vérifie une égalité ; le solide qu'elle borde vérifie une inégalité.
    Un point intérieur a distance nulle au solide, mais généralement positive à la surface.
    Deux solides emboîtés ont distance nulle ; leurs surfaces peuvent être disjointes.</p>

## 2. Le cosinus : projection orthogonale

**Sup / Spé**

<p>Dans C([0,L],ℝ), poser ⟨f,g⟩ = ∫₀ᴸ f(t)g(t)dt. Pour F = Vect(1,t), la meilleure
    approximation b+at est le projeté orthogonal de cos. Le résidu est orthogonal à 1 et à t :</p>
    <div class="formula">L b + L²a/2 = sin L<br>L²b/2 + L³a/3 = L sin L + cos L − 1.</div>
    <p>On obtient a = 12[L sin L/2 + cos L − 1]/L³ et b = sin L/L − aL/2.
    Pour L = π/2 : a ≈ −0,66444, b ≈ 1,15847, I<sub>min</sub> ≈ 0,006189,
    d ≈ 0,07867. L'identité de Pythagore donne I(a,b) = I<sub>min</sub> + ‖(a−a₀)t+(b−b₀)‖²,
    donc l'unicité et le minimum global.</p>
    <p>La base orthonormée u₀ = 1/√L, u₁ = √(12/L³)(t−L/2) retrouve le TP.
    Pour les polynômes de degré m, les polynômes de Legendre normalisés sont plus stables que
    les monômes. Le calcul utilise une factorisation QR du tableau d'évaluation pondéré.</p>

## 3. Hessienne, poids et descente

**Spé**

<p>On enrichit le TP avec I = ∫₀ᴸ (cos t−p(t))²w(t)dt et w(t)=1+κt/L, κ&gt;−1.
    La matrice de Gram des monômes est G<sub>ij</sub> = L<sup>i+j+1</sup>[1/(i+j+1)+κ/(i+j+2)].
    Elle est définie positive : cᵀGc = ∫p²w &gt; 0 pour p non nul.</p>
    <p>Dans l'ordre des paramètres (a,b), sans poids, la Hessienne vaut
    H = [[2L³/3,L²],[L²,2L]]. Son déterminant L⁴/3 est positif et H₁₁&gt;0.
    Le minimum est global car la fonction est strictement convexe et coercive ; elle n'a pas de maximum.</p>
    <p>Pour θ<sub>k+1</sub> = θ<sub>k</sub>−α∇I(θ<sub>k</sub>), l'erreur est multipliée par I₂−αH.
    La convergence est assurée si 0&lt;α&lt;2/λ<sub>max</sub>(H). Le graphique montre cette descente.
    Augmenter le degré ne peut augmenter l'erreur minimale L², à poids et intervalle fixés.</p>
    <p>La quadrature de Gauss à 96 points et les nombres flottants produisent des approximations
    numériques. Les expressions affines du cours sont exactes. Un petit résidu d'orthogonalité
    contrôle le calcul ; il ne remplace pas l'analyse du conditionnement.</p>

## 4. L² ou uniforme : deux meilleures droites

**Spé · approfondissement**

<p>Sur 0&lt;L≤π/2, cos est strictement concave. La sécante s(t)=1+at, a=(cos L−1)/L,
    est sous le graphe. Le plus grand écart M est atteint en t* = arcsin(−a).
    La meilleure approximation affine uniforme est <b>ℓ∞(t)=1+at+M/2</b>.</p>
    <p>Son erreur cos−ℓ∞ vaut −M/2, +M/2, −M/2 aux trois points 0,t*,L.
    Si une autre droite avait une erreur strictement inférieure, sa différence avec ℓ∞
    serait négative aux deux extrémités et positive en t*. Une fonction affine ne peut avoir
    ce signe : la convexité de ses valeurs fournit la contradiction. Cette alternance prouve l'optimalité.</p>
    <p>La droite L² minimise une énergie intégrale ; la droite uniforme minimise le pire écart.
    Elles diffèrent. Pour un polynôme de degré ≥2, l'interface encadre seulement la norme uniforme
    de sa projection L² : maximum échantillonné ≤ norme ≤ maximum échantillonné + KΔt/2,
    où K = 1+Σ k|cₖ|L<sup>k−1</sup>. Elle ne calcule pas un polynôme minimax de degré élevé.</p>

## 5. Exercice 4 : projection des matrices

**Sup / Spé**

<p>Pour le produit scalaire de Frobenius ⟨M,N⟩ = tr(MᵀN),
    M = S+A avec S=(M+Mᵀ)/2 et A=(M−Mᵀ)/2.
    Les sous-espaces symétrique et antisymétrique sont orthogonaux : les termes (i,j) et (j,i)
    s'annulent dans Σ S<sub>ij</sub>A<sub>ij</sub>. Ainsi d(M,Sₙ)=‖A‖<sub>F</sub>, le plus proche étant S.</p>
    <p>Pour la rotation de l'exercice 4, S=diag(1,cos θ,cos θ),
    donc <b>d(Rθ,S₃)=√2 |sin θ|</b>. Le minimum est 0 pour θ∈πℤ,
    le maximum √2 pour θ∈π/2+πℤ.</p>
    <p>Si V est un sous-espace réel dont chaque élément est diagonalisable sur ℝ,
    V∩Aₙ={0} : une matrice antisymétrique a un spectre imaginaire pur, alors qu'un élément de V
    a un spectre réel ; s'il appartient aux deux, il est diagonalisable avec toutes ses valeurs propres nulles.
    La projection V→Sₙ est donc injective. Ainsi dim V≤n(n+1)/2 ; Sₙ atteint cette borne.
    Cela ne signifie pas que toutes les matrices de V sont simultanément diagonalisables.</p>

## 6. Antisymétriques de déterminant 1

**Spé · réel ou complexe**

<p>Poser E={A : Aᵀ=−A, det A=1}. En dimension impaire,
    det A = det(−A) = (−1)ⁿdet A impose det A=0. <b>En dimension 3, E est vide.</b>
    Il n'y a pas de distance réelle finie ; dans ℝ∪{+∞}, inf ∅=+∞.</p>
    <p>En dimension paire n=2p, sur ℝ ou ℂ, utiliser ⟨M,N⟩=tr(M* N), M*=M̄ᵀ.
    La décomposition par TRANSPOSITION reste orthogonale : Sᵀ=S et Aᵀ=−A, sans exiger S*=S.
    Par Pythagore d(E,Sₙ)=inf<sub>A∈E</sub>‖A‖<sub>F</sub>.</p>
    <p>Les valeurs propres λᵢ&gt;0 de A*A vérifient ∏λᵢ=|det A|²=1.
    L'inégalité arithmético-géométrique donne ‖A‖²=Σλᵢ≥n.
    La matrice diag(J,…,J), J=[[0,1],[−1,0]], a déterminant 1 et norme √n.
    <b>d(E,Sₙ)=√n</b>, atteinte exactement pour les A∈E tels que A*A=I.</p>
    <p>E est fermé et non compact. Pour n≥4, remplacer deux blocs par eᵗJ et e⁻ᵗJ :
    le déterminant reste 1, la norme devient arbitrairement grande. Pour n=2, E={J,−J}.
    Une contrainte de déterminant seule n'assurerait pas une distance positive : Iₙ est symétrique et det Iₙ=1.</p>

## 7. Exercice 6 : ellipsoïde et boîte maximale

**Sup / Spé**

<p>Sur x²/a²+y²/b²+z²/c²=1, a,b,c&gt;0, poser u=x²/a², v=y²/b², w=z²/c².
    Alors u+v+w=1 et |xyz|=abc√(uvw). Par AM-GM, uvw≤1/27.</p>
    <div class="formula">max |xyz| = abc/(3√3)<br>(x,y,z)=(±a/√3, ±b/√3, ±c/√3).</div>
    <p>Il y a huit maximiseurs ; le minimum vaut 0 sur les intersections avec les plans de coordonnées.
    L'ellipsoïde est compact et la fonction continue, donc ces extrema existent. La sphère du PDF
    est le cas a=b=c=1.</p>
    <p>Application : une boîte centrée, parallèle aux axes, de demi-côtés |x|,|y|,|z| est inscrite
    si x²/a²+y²/b²+z²/c²≤1. Son volume maximal est 8abc/(3√3).
    Cette affirmation concerne les boîtes orientées selon les axes de l'ellipsoïde.</p>
    <p>Avec des exposants αᵢ&gt;0, le maximum de ∏|xᵢ|<sup>αᵢ</sup> est
    ∏ aᵢ<sup>αᵢ</sup>(αᵢ/Σαⱼ)<sup>αᵢ/2</sup>.
    Dans l'orthant positif, maximiser Σαᵢlog xᵢ sous la contrainte donne
    xᵢ²/aᵢ²=αᵢ/Σαⱼ. Les points où une coordonnée s'annule donnent 0, donc ne maximisent pas.</p>

## 8. Distance d'un point : Lagrange et cas singuliers

**Spé**

<p>Une surface générale s'écrit x=c+Bu, ‖u‖=1, B=R diag(aᵢ), R orthogonale.
    Pour un point p, poser D=diag(aᵢ²) et q=Bᵀ(c−p).
    Le carré de la distance est f(u)=‖c−p‖²+2qᵀu+uᵀDu.</p>
    <p>Pour le minimum, (D+μI)u=−q et D+μI≥0.
    Hors singularité, Σ qᵢ²/(aᵢ²+μ)²=1, avec μ&gt;−min aᵢ².
    Pour le maximum, (λI−D)u=q et λI−D≥0 ;
    Σ qᵢ²/(λ−aᵢ²)²=1, λ&gt;max aᵢ². Ces fonctions décroissent sur leur domaine : une dichotomie suffit.</p>
    <p>Attention : si q s'annule dans l'espace propre extrême, le multiplicateur peut se situer
    exactement au pôle. On résout les autres coordonnées puis complète la norme par une coordonnée libre.
    Le centre p=c illustre ce cas : distances min et max égales au plus petit et au plus grand demi-axe.
    L'application traite ces cas et affiche un représentant quand plusieurs points conviennent.</p>
    <p>Une condition de Lagrange seule ne prouve pas un extremum global. Ici, pour tout v unitaire,
    f(v)−f(u)=(v−u)ᵀ(D+μI)(v−u)≥0 au minimum.
    La formule analogue avec λI−D prouve le maximum.
    Les résidus de contrainte, de stationnarité et la borne spectrale sont affichés.</p>

## 9. Deux ellipsoïdes : contrôler le minimum

**Spé · approfondissement**

<p>Considérer les solides convexes Eᵢ={cᵢ+Bᵢu : ‖u‖≤1}, Qᵢ=BᵢBᵢᵀ.
    Pour un vecteur unitaire n, la fonction support vaut hᵢ(n)=n·cᵢ+√(nᵀQᵢn).
    Par Cauchy-Schwarz, pour x∈E₁ et y∈E₂ :</p>
    <div class="formula">‖y−x‖ ≥ n·(y−x) ≥ g(n)<br>g(n)=n·(c₂−c₁)−√(nᵀQ₁n)−√(nᵀQ₂n).</div>
    <p>Une paire de points admissibles fournit une borne supérieure U=‖y−x‖ ;
    max(0,g(n)) fournit une borne inférieure L. L'écart U−L contrôle l'erreur sur la distance.
    Les projections alternées x←P<sub>E₁</sub>(y), y←P<sub>E₂</sub>(x) diminuent U.
    La direction y−x sert à chercher une bonne borne inférieure. L'arrêt n'est déclaré convergé
    que lorsque l'écart relatif à l'échelle géométrique est petit.</p>
    <p>Pour des solides disjoints, au minimum n=(y−x)/d,
    x=c₁+Q₁n/√(nᵀQ₁n) et y=c₂−Q₂n/√(nᵀQ₂n).
    Ainsi d=max<sub>‖n‖=1</sub>g(n)&gt;0. Les deux points sont sur les surfaces : les distances coïncident.
    Le segment minimal n'est généralement pas porté par la droite des centres.</p>
    <p>Les valeurs affichées sont en virgule flottante : le contrôle primal-dual est numérique,
    sans arrondis dirigés ni certification par intervalles. Une distance très petite est annoncée
    comme compatible avec zéro à la précision du calcul. La formule concerne les solides ;
    elle ne résout pas la distance entre surfaces emboîtées.</p>

## 10. Séparation et marge maximale (SVM)

**Spé · ouverture**

<p>Si g(n)&gt;0, le plan n·x=m, où m=[h₁(n)+min<sub>E₂</sub>(n·x)]/2,
    sépare les deux solides. Chaque solide se situe à une distance au moins g(n)/2 de ce plan.
    Au minimum géométrique, cette marge vaut d(E₁,E₂)/2 et est maximale.</p>
    <p>Pour des étiquettes −1 sur E₁ et +1 sur E₂, poser w=2n/g(n), b=−2m/g(n).
    Les contraintes y(w·x+b)≥1 sont satisfaites. Maximiser la marge 1/‖w‖ équivaut
    à minimiser ½‖w‖² : c'est le problème de séparation à marge dure du SVM figurant dans votre extrait.</p>
    <p>Cette expérience utilise des contraintes sur des solides entiers, alors qu'un SVM classique
    est formulé sur un ensemble fini de points. Les fonctions support permettent ici de vérifier
    toutes les contraintes sans échantillonner la surface. Si les solides se recouvrent, aucun
    plan ne les sépare strictement : les paramètres SVM de marge dure ne sont pas définis.</p>

## Exercices corrigés

### 1. TP — retrouver la droite L²

Écrire les deux équations d'orthogonalité sur [0,π/2] et trouver a,b.

<details><summary>Correction</summary>

Intégrer cos et t cos par parties : Lb+L²a/2=sin L ; L²b/2+L³a/3=L sin L+cos L−1. Le déterminant L⁴/12 est positif. On obtient a≈−0,66444, b≈1,15847. Imin≈0,006189 est le carré de la distance, dont la valeur est ≈0,07867.

</details>

### 2. Pythagore et absence de maximum

Prouver que le point critique du TP est le minimum global unique. Existe-t-il un maximum ?

<details><summary>Correction</summary>

Le résidu cos−p est orthogonal à toute fonction affine. Donc ‖cos−ℓ‖²=‖cos−p‖²+‖p−ℓ‖². Le second terme est nul seulement pour ℓ=p. Quand le terme constant tend vers l'infini, l'intégrale tend vers l'infini : aucun maximum.

</details>

### 3. Projection de degré 2

Pourquoi l'erreur minimale ne peut-elle augmenter en passant du degré 1 au degré 2 ? Est-elle ici strictement plus petite ?

<details><summary>Correction</summary>

Les espaces sont emboîtés, donc on minimise sur un ensemble plus grand. L'égalité aurait lieu si le résidu affine était orthogonal au polynôme de Legendre de degré 2. Sur [0,π/2], son produit scalaire avec cos est non nul (le calcul de l'intégrale ou la concavité stricte le montre), donc l'erreur diminue strictement. Le laboratoire permet de mesurer cette différence.

</details>

### 4. Deux normes, deux optima

Démontrer l'optimalité de la droite uniforme à trois contacts, puis comparer son erreur L² à celle du TP.

<details><summary>Correction</summary>

La sécante est sous cos ; relever cette sécante de la moitié de l'écart maximal équilibre les erreurs −E,+E,−E. Une amélioration stricte imposerait à une fonction affine un signe négatif aux extrémités et positif à l'intérieur, impossible. La droite uniforme a une erreur L² supérieure à celle de la projection orthogonale, mais une norme uniforme plus petite.

</details>

### 5. Exercice 4 — espace diagonalisable

Trouver la dimension maximale d'un sous-espace de Mₙ(ℝ) dont chaque élément est diagonalisable sur ℝ.

<details><summary>Correction</summary>

Son intersection avec les antisymétriques est {0}, par confrontation des spectres réel et imaginaire pur puis diagonalisabilité. La projection symétrique est injective : dim V≤dim Sₙ=n(n+1)/2. Le sous-espace Sₙ atteint la borne, par le théorème spectral.

</details>

### 6. Rotation la plus éloignée

Calculer la distance de Rθ à S₃ et ses extrema sur θ∈ℝ.

<details><summary>Correction</summary>

La partie antisymétrique a deux coefficients opposés de valeur sin θ. Sa norme vaut √2|sin θ|. Minimum 0 pour θ∈πℤ ; maximum √2 pour θ∈π/2+πℤ. Le projeté le plus proche est diag(1,cos θ,cos θ).

</details>

### 7. Le piège de la dimension 3

Une matrice antisymétrique 3×3 peut-elle avoir déterminant 1 ? Que devient la question en dimension 4 ?

<details><summary>Correction</summary>

En dimension impaire det A=−det A, donc det A=0. L'ensemble demandé est vide. En dimension 4, diag(J,J) convient ; sa norme vaut 2. Les valeurs propres positives de A*A ont produit 1, donc leur somme vaut au moins 4. La distance à S₄ est exactement 2.

</details>

### 8. Complexe : transpose et adjoint

Pour z=eⁱᵠ, étudier A=diag(zJ,z⁻¹J). Est-elle antisymétrique, unitaire, hermitienne ?

<details><summary>Correction</summary>

Aᵀ=−A, det A=z²z⁻²=1. Comme |z|=1, A*A=I₄, donc ‖A‖=2 et elle minimise la distance. Elle n'est généralement pas hermitienne : la première condition concerne la transposition, la deuxième l'adjoint. Cette distinction est essentielle au calcul de projection.

</details>

### 9. Exercice 6 — boîte sur un ellipsoïde

Trouver la boîte centrée, parallèle aux axes, de volume maximal dans un ellipsoïde de demi-axes 3,2,1.

<details><summary>Correction</summary>

Poser u=x²/9,v=y²/4,w=z². À l'optimum u+v+w=1 et uvw≤1/27. Les demi-côtés sont √3,2/√3,1/√3 ; le volume maximal vaut 16/√3≈9,2376. Les huit sommets sont les huit maximiseurs de |xyz|.

</details>

### 10. Produit pondéré

Maximiser |x|²|y||z| sur x²/a²+y²/b²+z²/c²=1.

<details><summary>Correction</summary>

Les fractions optimales sont (1/2,1/4,1/4). Le maximum est a²bc/8, atteint aux huit points (±a/√2,±b/2,±c/2). La dérivation de 2log|x|+log|y|+log|z| donne ce résultat ; les points de coordonnées nulles ont valeur 0.

</details>

### 11. Centre, surface et solide

Pour p=c et demi-axes 3,2,1, trouver les distances minimale et maximale à la surface, puis au solide.

<details><summary>Correction</summary>

Sur la surface, le carré de la distance est 9u₁²+4u₂²+u₃², avec Σuᵢ²=1. Le minimum 1 est atteint sur le petit axe ; le maximum 3 sur le grand axe. Pour le solide, la distance minimale est 0 car c appartient au solide ; la maximale reste 3. Ces cas ont un multiplicateur singulier.

</details>

### 12. Deux sphères : référence indépendante

Deux boules de rayons r₁,r₂ ont leurs centres à distance D. Calculer leur distance et la marge maximale si elles sont disjointes.

<details><summary>Correction</summary>

L'inégalité triangulaire donne ‖x−y‖≥D−r₁−r₂ ; la droite des centres atteint cette borne si D>r₁+r₂. La distance des solides est max(0,D−r₁−r₂). La marge du plan médian des points de contact est la moitié de cette distance. Les surfaces emboîtées demandent un autre calcul.

</details>

### 13. Bornes sans deviner la direction

Pourquoi un couple admissible fournit-il une borne supérieure, et une direction unitaire une borne inférieure ?

<details><summary>Correction</summary>

Le minimum ne dépasse aucune valeur obtenue sur une paire admissible. Pour toute paire, Cauchy-Schwarz puis les fonctions support donnent ‖y−x‖≥n·(y−x)≥g(n). Ainsi max(0,g(n))≤d≤‖y−x‖. Un écart petit prouve une bonne approximation globale, même si les projections alternées ont convergé lentement.

</details>

### 14. SVM géométrique

À partir d'une séparation g(n)>0, construire w,b vérifiant les contraintes de marge dure sur les deux ellipsoïdes.

<details><summary>Correction</summary>

Prendre m au milieu des deux niveaux de support, w=2n/g(n), b=−2m/g(n). Sur E₁, w·x+b≤−1 ; sur E₂, w·x+b≥1. La marge géométrique vaut g(n)/2. Elle est maximale lorsque g(n)=d, ce que contrôle l'écart primal-dual.

</details>

## Références

- **Sources du parcours** : Extrait du recueil de fiches de A. R. : TP p. 158, SVM p. 159, exercices 4 et 6 p. 162 ; fichier distMatrices.txt fourni. Adaptations, démonstrations et figures nouvelles.
- [Distance point–ellipsoïde — David Eberly](https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf) : Équations scalaires, traitement des coordonnées nulles et des cas singuliers.
- [Convex Optimization — Boyd & Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/) : Convexité, dualité, séparation et optimisation de marge.
- [NumPy : QR et quadrature de Gauss](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html) : Documentation officielle des outils numériques employés ; quadrature via numpy.polynomial.legendre.leggauss.
