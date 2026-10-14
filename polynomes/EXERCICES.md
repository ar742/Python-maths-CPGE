# Polynômes & Géométrie — 108 exercices corrigés

## 01. Le coefficient au pôle simple

Sup · Laboratoire `rationnelle_recueil`

Pour la fraction de l’exercice 4, multiplier F par X+1 puis évaluer en −1. Déterminer le coefficient du terme simple.

**Correction guidée**

Le coefficient vaut P(−1)/(−3)³. P(−1)=−54, donc il vaut 2. Les termes réguliers multipliés par X+1 s’annulent au point −1.

## 02. Faire disparaître les puissances fortes

Sup · Laboratoire `rationnelle_recueil`

Soit F=1+2/(X+1)+1/(X−2)+C/(X−2)²+D/(X−2)³. Quels choix donnent un pôle simple en 2 ?

**Correction guidée**

Il faut D=0 puis C=0. Le coefficient de 1/(X−2) reste 1, non nul : l’ordre est exactement un. Si ce coefficient était aussi nul, le pôle disparaîtrait.

## 03. De la décomposition à une primitive

Sup / spé · Laboratoire `rationnelle_recueil`

Donner une primitive de la fraction du recueil sur chacun des intervalles séparés par −1 et 2.

**Correction guidée**

Une primitive est x+2 ln|x+1|+ln|x−2|−2/(x−2)−3/[2(x−2)²]. La constante d’intégration peut être différente sur chaque intervalle. La dérivation retrouve chaque élément simple.

## 04. Un pôle triple calculé en une ligne

Sup · Laboratoire `poles_multiples`

Décomposer (X⁴+2X²+X+1)/X³.

**Correction guidée**

La division des monômes donne X+2/X+1/X²+1/X³. Les coefficients polaires sont g″(0)/2=2, g′(0)=1 et g(0)=1 ; la partie entière est X.

## 05. Un ordre qui baisse

Sup · Laboratoire `poles_multiples`

Avec g=X⁴−X²+X+1, déterminer l’ordre de g/(X+1)^4 en −1.

**Correction guidée**

g(−1)=0 mais g′(−1)=4(−1)³−2(−1)+1=−1, non nul. Le numérateur possède un zéro simple ; le pôle réduit est donc d’ordre trois.

## 06. Construire une partie polaire imposée

Spé — synthèse · Laboratoire `poles_multiples`

Pour m=3, chercher un numérateur polynomial g donnant les coefficients 2, −1, 3 devant (X−a)⁻¹, (X−a)⁻², (X−a)⁻³.

**Correction guidée**

Il faut g(a)=3, g′(a)=−1 et g″(a)=4. Ainsi g=3−(X−a)+2(X−a)²+(X−a)³q(X), où q est un polynôme arbitraire. La fraction vaut q+2/(X−a)−1/(X−a)²+3/(X−a)³.

## 07. Décomposer 1/(X²+1)

Sup · Laboratoire `reel_complexe`

Déterminer les coefficients des termes en 1/(X−i) et 1/(X+i).

**Correction guidée**

Au pôle i, le coefficient est 1/(2i)=−i/2. Au pôle −i, il vaut i/2. Ainsi 1/(X²+1)=−i/[2(X−i)]+i/[2(X+i)].

## 08. Regrouper deux fractions conjuguées

Sup · Laboratoire `reel_complexe`

Regrouper (1+i)/(X−i)+(1−i)/(X+i) en une fraction réelle.

**Correction guidée**

Le numérateur est (1+i)(X+i)+(1−i)(X−i)=2X−2. La somme vaut donc (2X−2)/(X²+1).

## 09. Une primitive réelle à retrouver

Sup / spé · Laboratoire `reel_complexe`

Intégrer (2x+1)/(x²+1) sur ℝ.

**Correction guidée**

Le terme 2x/(x²+1) donne ln(x²+1). Le terme 1/(x²+1) donne arctan x. Une primitive réelle est ln(x²+1)+arctan x. La décomposition complexe explique le couple de pôles ; elle n’oblige pas à choisir des logarithmes complexes.

## 10. Un trou avec une limite non nulle

Sup · Laboratoire `annulations`

Déterminer la limite en 2 de (x³−8)/(x−2), et préciser le domaine initial.

**Correction guidée**

x³−8=(x−2)(x²+2x+4). La formule réduite vaut x²+2x+4 et tend vers 12. Le domaine initial est ℝ privé de 2 ; on peut prolonger la fonction en attribuant la valeur 12.

## 11. Une collision change le diagnostic

Sup · Laboratoire `annulations`

Avec k=m=2, comparer F=(X−a)^k/[(X−a)^m(X−b)] lorsque a≠b puis lorsque a=b.

**Correction guidée**

Si a≠b, la formule réduite est 1/(X−b) : trou en a, pôle simple en b. Si a=b, elle devient 1/(X−a) : le point unique est un pôle. L’annulation des facteurs n’efface pas le facteur supplémentaire X−b.

## 12. Toutes les limites possibles

Spé — synthèse · Laboratoire `annulations`

Supposer a=b. Classer le point a selon les valeurs de k−m−1.

**Correction guidée**

Si k−m−1<0, il reste un pôle d’ordre m+1−k. Si k−m−1=0, la formule réduite est constante 1 et la limite vaut 1. Si k−m−1>0, la limite vaut 0. Dans les deux derniers cas, le point est toujours exclu de l’expression initiale.

## 13. Un reste de division obtenu par trois valeurs

Sup — TP p.166 · Laboratoire `interpolation`

Déterminer le reste de X⁴ par (X−1)(X−2)(X−3), à partir de ses valeurs aux trois racines.

**Correction guidée**

Le reste R=αX²+βX+γ vérifie R(1)=1, R(2)=16, R(3)=81. La résolution donne α=25, β=−60, γ=36. Vérifier : X⁴=(X+6)(X³−6X²+11X−6)+25X²−60X+36.

## 14. Pourquoi la différence s’annule

Sup · Laboratoire `interpolation`

Deux polynômes de degré au plus quatre coïncident en cinq points distincts. Montrer qu’ils sont égaux.

**Correction guidée**

Leur différence a degré au plus quatre et possède cinq racines distinctes. Un polynôme non nul ne peut pas avoir plus de racines que son degré. La différence est donc nulle.

## 15. Une fonction invisible aux nœuds

Spé — contre-exemple · Laboratoire `interpolation`

À des nœuds x₀,…,x_n, les données sont toutes nulles. Construire une fonction non nulle qui a pourtant ces valeurs.

**Correction guidée**

Prendre f(x)=∏_{i=0}^n(x−x_i). Son interpolateur de degré au plus n est le polynôme nul, alors que f n’est pas identiquement nulle. Le contrôle aux nœuds ne suffit pas à contrôler l’erreur entre eux.

## 16. Vérifier une orthogonalité de Legendre

Sup · Laboratoire `orthogonaux`

Avec L₀=1 et L₂=(3X²−1)/2, calculer ∫_{−1}^1 L₀L₂.

**Correction guidée**

L’intégrale vaut [x³−x]_{−1}^1/2=0. La constante et le polynôme de degré deux sont orthogonaux pour le poids uniforme.

## 17. Les deux conventions d’Hermite

Sup / spé · Laboratoire `orthogonaux`

Déterminer H₂ et Ĥ₂, sachant H₁=X dans la convention probabiliste et Ĥ₁=2X dans la convention physique.

**Correction guidée**

Les récurrences donnent H₂=X²−1 et Ĥ₂=4X²−2. La relation Ĥ₂(X)=2H₂(√2X) est vérifiée. Une comparaison exige de préciser le poids gaussien et le changement d’échelle.

## 18. Deux nœuds, quatre moments

Au-delà — application guidée · Laboratoire `orthogonaux`

Pour Legendre n=2, les nœuds sont ±1/√3 et les deux poids valent 1. Vérifier la formule pour 1,x,x²,x³ puis tester x⁴.

**Correction guidée**

Les sommes valent 2,0,2/3,0 : ce sont les quatre intégrales exactes. Pour x⁴, la quadrature donne 2/9 alors que l’intégrale vaut 2/5. Le degré trois est garanti ; le degré quatre ne l’est pas.

## 19. Un reste sans division longue

Sup · Laboratoire `euclide_bezout`

Calculer le reste de X⁴ modulo (X−1)(X−2)(X−3) en utilisant les trois racines du diviseur.

**Correction guidée**

Écrire R=αX²+βX+γ. Les valeurs 1,16,81 donnent α=25, β=−60, γ=36. Le quotient est X+6; la multiplication vérifie l’identité.

## 20. Composition et congruence

Sup · Laboratoire `euclide_bezout`

Dans ℚ[X], poser P=X²+2X−1 et B=P−X. Montrer B|P(P(X))−X, puis calculer le reste de A=X⁴+5X³+5X²−X−2 modulo B.

**Correction guidée**

Modulo B, P(X)≡X, donc P(P(X))≡P(X)≡X. Le développement donne P(P(X))−X=X⁴+4X³+4X²−X−2. A en diffère de X³+X². Avec X²≡1−X, on a X³+X²≡X. Le reste est X.

## 21. Reconnaître le rôle du coefficient dominant

Sup · Laboratoire `euclide_bezout`

A=2(X²+1)(X³−2X+1), B=3(X²+1)(X²+X+2). Leurs facteurs cubique et quadratique sont premiers entre eux. Donner PGCD(A,B) et expliquer pourquoi 6(X²+1) n’est pas le PGCD retenu.

**Correction guidée**

Dans ℚ[X], les constantes non nulles sont inversibles. Le facteur commun maximal est X²+1; le PGCD est choisi unitaire. 6(X²+1) est un autre générateur du même idéal, mais son coefficient dominant vaut 6.

## 22. Gauss par Bézout

Sup · Laboratoire `gauss_eisenstein`

Dans K[X], supposer A|BC et AU+BV=1. Prouver A|C sans invoquer une factorisation de B.

**Correction guidée**

Multiplier l’identité par C : C=AUC+BVC. A divise AUC; il divise BVC puisque A|BC. Il divise donc leur somme C.

## 23. Un Eisenstein caché

Au-delà accompagné · Laboratoire `gauss_eisenstein`

P=(X−1)⁵+3(X−1)+3. Prouver P irréductible sur ℚ.

**Correction guidée**

P(X+1)=X⁵+3X+3. Pour p=3, le coefficient dominant n’est pas divisible par 3, tous les autres le sont, et 9 ne divise pas le terme constant 3. Eisenstein s’applique. Une factorisation de P donnerait une factorisation de P(X+1), donc P est irréductible.

## 24. L’absence de racines n’est pas un certificat

Sup · Laboratoire `gauss_eisenstein`

Le polynôme X⁴+4 a-t-il une racine rationnelle ? Est-il irréductible sur ℚ ?

**Correction guidée**

Pour tout réel x, x⁴+4>0, donc aucune racine rationnelle. Pourtant X⁴+4=(X²−2X+2)(X²+2X+2). L’absence de racines suffit pour les degrés 2 et 3, mais pas pour le degré 4.

## 25. Un inverse sans factoriser

Sup / prolongement · Laboratoire `inverse_quotient`

Dans ℚ[X]/(X³−2), calculer l’inverse de la classe de X.

**Correction guidée**

X×(X²/2)=X³/2≡1. L’inverse est la classe de X²/2; l’identité exacte est X(X²/2)−(X³−2)/2=1.

## 26. Un diviseur de zéro non nul

Spé / prolongement · Laboratoire `inverse_quotient`

M=(X²+1)(X²+X+1). Dans ℚ[X]/(M), montrer que la classe de X²+1 est non nulle et non inversible.

**Correction guidée**

Son degré 2 est inférieur à deg M=4, donc sa classe est non nulle. Son produit par la classe non nulle de X²+X+1 est nul. Un élément inversible ne peut annuler un élément non nul.

## 27. Quatre coefficients, seize éléments

Au-delà accompagné · Laboratoire `inverse_quotient`

M=X⁴+X+1 est irréductible sur F₂. Combien d’éléments possède F₂[X]/(M) ? Combien sont inversibles ?

**Correction guidée**

Chaque représentant a quatre coefficients indépendants, valant 0 ou 1 : 2⁴=16 éléments. L’irréductibilité fait du quotient un corps; ses 15 éléments non nuls sont tous inversibles.

## 28. Retrouver l’interpolation

Sup · Laboratoire `restes_chinois`

Déterminer le représentant de degré inférieur à 2 vérifiant S≡2 modulo X−1 et S≡5 modulo X−3.

**Correction guidée**

Écrire S=αX+β. Les équations α+β=2 et 3α+β=5 donnent α=3/2, β=1/2. Les solutions sont (3X+1)/2+(X−1)(X−3)Q.

## 29. Tester l’obstruction au bon endroit

Spé / prolongement · Laboratoire `restes_chinois`

On impose S≡X modulo (X−1)(X+1) et S≡X+1 modulo (X−1)(X+2). Existe-t-il une solution ?

**Correction guidée**

Le PGCD des modules est X−1. Au point X=1, les restes valent 1 et 2. Leur différence 1 n’est pas divisible par X−1 : aucune solution.

## 30. Vérifier un idempotent

Spé / prolongement · Laboratoire `restes_chinois`

Dans ℚ[X]/((X−1)(X+1)), poser E₁=(X+1)/2 et E₂=(1−X)/2. Vérifier les identités de projecteurs.

**Correction guidée**

E₁+E₂=1. E₁²−E₁=(X²−1)/4, E₂²−E₂=(X²−1)/4 et E₁E₂=(1−X²)/4 sont nuls modulo X²−1. E₁ sélectionne la valeur en 1; E₂ celle en −1.

## 31. Une inversion concrète

Au-delà accompagné · Laboratoire `mobius_diviseurs`

Utiliser φ(n)=Σ_{d|n}μ(d)n/d pour calculer φ(30).

**Correction guidée**

Les diviseurs sont 1,2,3,5,6,10,15,30. Les contributions sont 30,−15,−10,−6,5,3,2,−1. La somme vaut 8, en accord avec 30(1−1/2)(1−1/3)(1−1/5).

## 32. La constante 1 n’est pas χ

Au-delà accompagné · Laboratoire `mobius_diviseurs`

Noter 1 la fonction constante égale à 1. Calculer (1∗1)(12), puis expliquer pourquoi χ est l’unité de convolution.

**Correction guidée**

(1∗1)(12) compte les diviseurs 1,2,3,4,6,12 : résultat 6. Pour (f∗χ)(n), seul d=n contribue puisque χ(n/d) est nul sauf si n/d=1; on retrouve f(n).

## 33. Un carré supprime une contribution

Sup / prolongement · Laboratoire `mobius_diviseurs`

Calculer μ(72), μ(30) et μ(1), puis la somme Σ_{d|72}μ(d).

**Correction guidée**

72=2³3² a des facteurs carrés, donc μ(72)=0. 30=2×3×5 donne μ(30)=−1, et μ(1)=1. Seuls 1,2,3,6 donnent des termes non nuls dans la somme : 1−1−1+1=0.

## 34. Le premier quadratique irréductible

Au-delà accompagné · Laboratoire `irreductibles_fp`

Énumérer les quatre polynômes unitaires de degré 2 sur F₂ et déterminer les irréductibles.

**Correction guidée**

X², X²+1=(X+1)² et X²+X=X(X+1) sont réductibles. X²+X+1 ne s’annule ni en 0 ni en 1, donc il est irréductible. I₂(2)=(4−2)/2=1.

## 35. Un degré premier

Au-delà accompagné · Laboratoire `irreductibles_fp`

Calculer I₃(3), puis expliquer pourquoi le dénominateur 3 intervient.

**Correction guidée**

Les diviseurs de 3 sont 1 et 3. I₃(3)=(3³−3)/3=8. Après avoir retiré les trois racines du corps de base, chaque irréductible cubique apporte trois racines distinctes dans l’extension.

## 36. Isoler un degré composé

Au-delà accompagné · Laboratoire `irreductibles_fp`

Calculer 6I₂(6) directement, puis I₂(6). Quelle identité générale utilisera-t-on pour les autres degrés ?

**Correction guidée**

Les diviseurs 1,2,3,6 donnent 64−8−4+2=54, donc I₂(6)=9. L’identité générale est la somme Σ_{d|n}μ(d)p^(n/d), dont les exposants n/d varient avec chaque diviseur.

## 37. Huit racines, quatre facteurs

Au-delà accompagné · Laboratoire `frobenius_fp`

Vérifier sur F₂ : X⁸−X=X(X+1)(X³+X+1)(X³+X²+1). Pourquoi les cubiques sont-ils irréductibles ?

**Correction guidée**

Une multiplication modulo 2 donne X⁸+X, égal à X⁸−X dans F₂. Chaque cubique vaut 1 en 0 et en 1 : aucun facteur linéaire, donc irréductibilité en degré 3. Les degrés totalisent 1+1+3+3=8.

## 38. Pas de quadratiques dans X⁸−X

Au-delà accompagné · Laboratoire `frobenius_fp`

Pourquoi X²+X+1, irréductible sur F₂, ne divise-t-il pas X⁸−X ? Dans quel polynôme de Frobenius de plus petit degré apparaît-il ?

**Correction guidée**

Son degré 2 ne divise pas 3. Il ne figure donc pas dans X^(2³)−X. Il apparaît dans X^(2²)−X=X⁴−X, puisque 2 divise 2.

## 39. Une extension a plusieurs coordonnées

Au-delà accompagné · Laboratoire `frobenius_fp`

α est une racine de X⁴+X+1, irréductible sur F₂. Décrire les éléments de F₂[α] et la réduction de α⁴.

**Correction guidée**

Les éléments s’écrivent de façon unique a₀+a₁α+a₂α²+a₃α³ avec aᵢ∈{0,1}; il y en a 16. La relation α⁴+α+1=0 donne α⁴=α+1 en caractéristique 2.

## 40. Distinguer six racines et deux primitives

Sup · Laboratoire `cyclotomie`

Donner les racines primitives d’ordre 6 et leur polynôme.

**Correction guidée**

Les entiers k premiers avec 6 sont 1 et 5. Les deux racines sont exp(±iπ/3); leur somme vaut 1 et leur produit vaut 1. Φ₆=X²−X+1.

## 41. Un ordre premier

Sup / prolongement · Laboratoire `cyclotomie`

Pour p premier, exprimer Φₚ(X) et Φₚ(1).

**Correction guidée**

Toutes les racines p-ièmes sauf 1 sont primitives. Φₚ=(Xᵖ−1)/(X−1)=1+X+⋯+X^(p−1), donc Φₚ(1)=p.

## 42. Un quotient qui redevient entier

Au-delà accompagné · Laboratoire `cyclotomie`

Utiliser les diviseurs de 12 pour obtenir Φ₁₂. Pourquoi le terme X−1 n’intervient-il pas dans le produit de Möbius ?

**Correction guidée**

Les exposants μ(12/d) sont nuls pour d=1,3. Les autres donnent Φ₁₂=(X¹²−1)(X²−1)/[(X⁶−1)(X⁴−1)]=X⁴−X²+1. μ(12)=0 car 12 contient le carré 2².

## 43. Construire B₂

Sup · Laboratoire `bernoulli_faulhaber`

Avec B₁=X−1/2, déterminer B₂ en utilisant B₂′=2B₁ et ∫₀¹B₂=0.

**Correction guidée**

Une primitive est X²−X+c. Son intégrale est 1/3−1/2+c; elle s’annule pour c=1/6. Donc B₂=X²−X+1/6.

## 44. Sommer sans récurrence forte

Sup / prolongement · Laboratoire `bernoulli_faulhaber`

B₃=X³−3X²/2+X/2. Retrouver Σ_{k=0}^N k².

**Correction guidée**

B₃(X+1)−B₃(X)=3X². Le télescopage donne B₃(N+1)/3, puisque B₃(0)=0. Après développement : N(N+1)(2N+1)/6.

## 45. Contrôler une génératrice au voisinage de zéro

Spé / prolongement · Laboratoire `bernoulli_faulhaber`

La fonction G(z)=z/(exp(z)−1), prolongée en z=0, engendre les nombres bₘ=Bₘ(0). Calculer ses trois premiers termes et les comparer à B₁,B₂.

**Correction guidée**

exp(z)−1=z+z²/2+z³/6+⋯. L’inversion donne G(z)=1−z/2+z²/12+O(z³). Le coefficient de zᵐ est bₘ/m! : b₀=1, b₁=−1/2, b₂=1/6.

## 46. Les carrés deviennent exacts

Sup / prolongement · Laboratoire `euler_maclaurin`

Appliquer Euler–Maclaurin à f(x)=x² sur [0,N], avec une correction et b₂=1/6, pour retrouver Σ_{j=0}^N j².

**Correction guidée**

L’intégrale vaut N³/3, les demi-extrémités N²/2, et la correction b₂[f′(N)−f′(0)]/2!=N/6. Leur somme est N(N+1)(2N+1)/6. La dérivée seconde est constante : le reste intègre B₂ sur des intervalles entiers et vaut 0.

## 47. Une borne pour la somme harmonique

Spé / prolongement · Laboratoire `euler_maclaurin`

Pour f(x)=1/x et N≥2, écrire l’approximation avec k=1 et majorer son reste.

**Correction guidée**

S≈ln N+(1+1/N)/2+(1−1/N²)/12. f″=2/x³, donc |R₁|≤(1/12)∫₁ᴺ2/x³ dx=(1−1/N²)/12. La borne garantit l’écart, même si elle peut être bien supérieure à l’erreur observée.

## 48. Savoir quand s’arrêter

Spé / prolongement · Laboratoire `euler_maclaurin`

Pour un polynôme f de degré 7 et une somme sur des bornes entières, combien de corrections suffisent à garantir un reste nul ? Justifier par la formule du reste.

**Correction guidée**

Quatre corrections suffisent : 2k=8>7, donc f^(8)=0. Le reste R₄ est nul. Cela fournit un arrêt garanti, indépendamment de la forme des coefficients du polynôme.

## 49. Le premier cas non trivial

Sup · Laboratoire `cayley_tangentes`

Développer P₂(Z)=(Z+1)⁴−(Z−1)⁴ puis le factoriser dans ℂ[Z].

**Correction guidée**

P₂=8Z³+8Z=8Z(Z−i)(Z+i). Les trois racines sont 0, i et −i. Le quatrième candidat de la transformation, w=−1, n’a pas d’image finie.

## 50. Une somme sans calcul trigonométrique

Sup · Laboratoire `cayley_tangentes`

Pour n=5, calculer Σₖ₌₀,ₖ≠₅⁹ tan(kπ/10), puis le produit des huit termes non nuls.

**Correction guidée**

La somme vaut 0, par Viète ou par appariement des indices k et 10−k. Le produit vaut (−1)⁴=1. On doit omettre k=5 dans les deux expressions et k=0 dans le produit.

## 51. Le degré explique le candidat perdu

Spé · Laboratoire `cayley_tangentes`

Pourquoi une équation faisant intervenir une puissance 2n ne donne-t-elle que 2n−1 solutions finies ici ?

**Correction guidée**

Après suppression du dénominateur, (Z+1)²ⁿ−(Z−1)²ⁿ=0 : les termes Z²ⁿ s’annulent. Le coefficient suivant est 4n≠0, donc le degré est 2n−1. Le candidat w=−1 est précisément celui perdu lors de l’inversion z=(w−1)/(w+1).

## 52. Un facteur indispensable

Sup · Laboratoire `geometrique_affine`

Pour P₃(Z)=Σⱼ₌₀³((Z+1)/2)ʲ, donner P₃(1), son coefficient dominant et le produit de ses racines.

**Correction guidée**

P₃(1)=4. Le coefficient dominant est 1/8. Le produit vaut (−1)³×8×P₃(0)=−8×15/8=−15. La factorisation sans 1/8 ne serait pas celle de P₃.

## 53. Des coefficients vraiment complexes

Sup · Laboratoire `geometrique_affine`

Pour n=2, c=i et r=1, développer P₂(Z)=1+(Z−i)+(Z−i)² et situer ses racines.

**Correction guidée**

P₂(Z)=Z²+(1−2i)Z−i. Ses coefficients ne sont pas réels. Les racines sont i+e^(2iπ/3) et i+e^(4iπ/3), sur le cercle de centre i et de rayon 1.

## 54. Simplicité des racines

Spé · Laboratoire `geometrique_affine`

Justifier que Pₙ(Z)=Σⱼ₌₀ⁿ((Z−c)/r)ʲ possède exactement n racines simples lorsque r>0.

**Correction guidée**

Dans la variable T=(Z−c)/r, (1−T)Pₙ=1−T^(n+1). Les n+1 racines de T^(n+1)−1 sont distinctes car sa dérivée (n+1)Tⁿ ne s’annule sur aucune d’elles. T=1 est supprimé; l’affinité Z=c+rT, de pente non nulle, conserve les n autres racines et leurs multiplicités.

## 55. Une borne facilement calculable

Sup · Laboratoire `racines_coefficients`

Pour P(Z)=Z⁵+(2+i)Z²−3i, prouver que toutes les racines vérifient |α|≤1+max(√5,3)=4.

**Correction guidée**

Poser A=max des modules des coefficients non dominants=3. Pour r>1+A=4, Σₖ₌₀⁴|aₖ|rᵏ≤A(r⁵−1)/(r−1)<r⁵. Une racine de module r serait incompatible avec l’inégalité triangulaire. Donc |α|≤4. Cette borne simple peut être moins fine que ρ.

## 56. Vérifier une monotonie

Spé · Laboratoire `racines_coefficients`

Pour P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i), écrire h(r)=Q(r)/r⁶ et justifier son unique zéro positif.

**Correction guidée**

h(r)=1−|a|/r²−√2/r⁴−|b|/r⁵−√0,89/r⁶. Sa dérivée est strictement positive, même si a=b=0. Ses limites sont −∞ en 0 et 1 à l’infini. Le théorème des valeurs intermédiaires et la stricte monotonie donnent un unique zéro.

## 57. Une confusion de quantificateurs

Spé · Laboratoire `racines_coefficients`

La borne (2^(1/n)−1)ρ≤max|αₖ| implique-t-elle que toutes les racines sont hors du petit disque ?

**Correction guidée**

Non : elle affirme qu’au moins une racine a un module supérieur ou égal à ce rayon. Les autres peuvent être dans le petit disque, voire à l’origine pour un autre polynôme. La borne supérieure |αₖ|≤ρ, elle, concerne chaque racine.

## 58. Deux racines sans les calculer

Au-delà accompagné · Laboratoire `rouche_disque`

Pour P(Z)=Z⁵+(−4+i)Z²+0,5+0,3i, certifier le nombre de racines dans |z|<1. Le théorème de Rouché est fourni.

**Correction guidée**

Choisir f=(−4+i)Z². Sur |z|=1, |f|=√17 et |P−f|≤1+√0,34. Comme √17>1+√0,34, P possède autant de racines que f : exactement deux, comptées avec multiplicité.

## 59. Agrandir le disque

Au-delà accompagné · Laboratoire `rouche_disque`

Pour le même polynôme, certifier le nombre de racines dans |z|<2.

**Correction guidée**

Choisir f=Z⁵ : |f|=32. Les autres termes sont majorés par 4√17+√0,34<32. Rouché donne cinq racines. Le grand disque contient donc toutes les racines du polynôme de degré 5.

## 60. Une égalité qui ne suffit pas

Au-delà accompagné · Laboratoire `rouche_disque`

La condition de comparaison avec f=Z⁵ échoue. Peut-on en déduire que P possède moins de cinq racines dans le disque ?

**Correction guidée**

Non. Le majorant utilisé est une condition suffisante, pas nécessaire. Son échec ne fournit aucun comptage. Il faut une autre décomposition, une inégalité plus fine ou une méthode différente; le calcul approché constitue une observation, pas ce certificat.

## 61. Un barycentre forcé

Au-delà accompagné · Laboratoire `gauss_lucas`

On fournit P′/P=Σ1/(Z−αₖ). Pour une racine β de P′ telle que P(β)≠0, établir sa représentation comme barycentre à poids positifs.

**Correction guidée**

Conjuguer l’égalité nulle : Σ(β−αₖ)/|β−αₖ|²=0. Mettre β en facteur puis diviser par Σ1/|β−αₖ|²>0. Les coefficients obtenus sont strictement positifs et de somme 1; β appartient à l’enveloppe convexe.

## 62. Un centre de gravité partagé

Spé · Laboratoire `gauss_lucas`

P est unitaire de degré n≥2, de coefficient c₁ devant Z^(n−1). Comparer la moyenne des racines de P et celle des racines de P′.

**Correction guidée**

Viète donne Σαₖ=−c₁. P′ a coefficient dominant n et coefficient suivant (n−1)c₁, donc Σβⱼ=−(n−1)c₁/n. Après division par les nombres respectifs de racines n et n−1, les deux moyennes valent −c₁/n.

## 63. La racine commune

Sup · Laboratoire `gauss_lucas`

Si α est racine de multiplicité m≥2 de P, quelle est sa multiplicité dans P′ ? Pourquoi ne pose-t-elle pas de difficulté pour Gauss–Lucas ?

**Correction guidée**

Écrire P=(Z−α)^mQ avec Q(α)≠0. P′=(Z−α)^(m−1)[mQ+(Z−α)Q′], dont le crochet vaut mQ(α)≠0. La multiplicité est m−1. La racine α est déjà dans l’ensemble des racines de P, donc dans son enveloppe convexe.

## 64. Un calcul avec des coefficients non réels

Sup · Laboratoire `reciproque_conjugue`

Calculer le réciproque conjugué de P(Z)=(1+i)Z³+2Z²+(1−2i)Z+3i.

**Correction guidée**

P*(Z)=−3iZ³+(1+2i)Z²+2Z+(1−i). Il faut inverser l’ordre des coefficients et conjuguer chacun d’eux; un simple renversement donnerait un autre polynôme.

## 65. Même direction, autre module

Sup · Laboratoire `reciproque_conjugue`

Une racine vaut α=1+i. Calculer son image réciproque conjuguée, puis comparer modules et arguments.

**Correction guidée**

1/conj(α)=1/(1−i)=(1+i)/2. Le module passe de √2 à 1/√2 et l’argument reste π/4. Le réciproque sans conjugaison, (1−i)/2, aurait l’argument opposé.

## 66. Le zéro et le second retournement

Spé · Laboratoire `reciproque_conjugue`

P(Z)=Z(Z−(1+i))(Z−2) est de degré 3. Quel est le degré effectif de P* ? Que donne son réciproque conjugué pris en degré effectif ?

**Correction guidée**

P a une racine nulle simple et ses deux autres racines sont non nulles. P* a donc degré 2. En retournant ensuite ses trois coefficients de degré 2, on obtient P/Z=(Z−(1+i))(Z−2), et non P. En gardant dès le départ quatre coefficients de degré ambiant 3, le double retournement retrouve P.

## 67. Quatrième somme exacte

Spé · Laboratoire `viete_newton`

Pour P(Z)=Z⁶+(1+i)Z⁴+(1+i)Z²+(−1+0,5i)Z+0,5−0,8i, calculer s₄=Σαⱼ⁴ sans déterminer les racines.

**Correction guidée**

s₁=s₃=0 et s₂=−2(1+i). Newton au rang 4 donne s₄+(1+i)s₂+4(1+i)=0. Ainsi s₄=2(1+i)²−4(1+i)=4i−4−4i=−4.

## 68. Une somme et un produit

Sup · Laboratoire `viete_newton`

Pour le polynôme général du laboratoire, déterminer la somme et le produit des six racines, comptées avec multiplicité.

**Correction guidée**

Le coefficient de Z⁵ est nul, donc la somme vaut 0. Le degré 6 est pair et le polynôme unitaire : le produit vaut son terme constant, 0,5−0,8i. Aucune symétrie de conjugaison n’est nécessaire.

## 69. Cinquième et septième sommes

Spé · Laboratoire `viete_newton`

Dans la famille P=Z⁶+aZ⁴+(1+i)Z²+bZ+0,5−0,8i, calculer s₅ puis s₇.

**Correction guidée**

Comme s₁=s₃=0, l’identité au rang 5 donne s₅=−5b. Au rang 7, la récurrence donne s₇=−a s₅−(1+i)s₃−b s₂−c₆s₁=5ab+2ab=7ab. Les rangs 5 et 7 n’utilisent pas exactement la même forme de l’identité.

## 70. Un point qui ne démarre pas

Sup / prolongement · Laboratoire `newton_bassins`

Pour P(Z)=(Z−c)⁴−1, avec c=0,3+0,4i, expliquer pourquoi Newton ne peut pas démarrer en z₀=c.

**Correction guidée**

P(c)=−1 alors que P′(c)=4(c−c)³=0. Le quotient P(c)/P′(c) n’est pas défini. Le centre ne doit donc recevoir la couleur d’aucune racine; il est classé séparément.

## 71. Un résidu et une erreur

Spé · Laboratoire `newton_bassins`

Près d’une racine simple α, pourquoi |P(z)| petit ne donne-t-il une estimation de |z−α| qu’en tenant compte de P′(α) ?

**Correction guidée**

P(z)=P′(α)(z−α)+O((z−α)²). Au premier ordre, |z−α|≈|P(z)|/|P′(α)|. Une petite dérivée amplifie l’erreur de position correspondant à un même résidu; l’estimation exige d’être déjà dans un voisinage convenable de la racine.

## 72. La racine multiple ralentit Newton

Spé · Laboratoire `newton_bassins`

Pour P(Z)=(Z−α)^m et m≥2, écrire exactement la récurrence de Newton et le facteur de réduction de l’erreur.

**Correction guidée**

Pour z≠α, P/P′=(z−α)/m. Ainsi zₖ₊₁−α=(1−1/m)(zₖ−α). Le facteur est (m−1)/m : la convergence est linéaire, contrairement au cas d’une racine simple générique.

## 73. Vérifier l’hypothèse avant d’approximer

Spé · Laboratoire `conditionnement_racines`

δ=0,2 et ε=10⁻⁶. Estimer le déplacement des racines mobiles et vérifier la condition du premier ordre.

**Correction guidée**

ε/δ²=10⁻⁶/0,04=2,5×10⁻⁵≪1. Le déplacement a pour module ε/(2δ)=2,5×10⁻⁶. La correction suivante est d’ordre ε²/δ³; le développement est adapté à cette échelle.

## 74. Double racine et perturbation imaginaire

Sup / Spé · Laboratoire `conditionnement_racines`

Pour δ=0 et η=i×10⁻⁸, écrire les deux racines mobiles autour de c=0,2+0,3i.

**Correction guidée**

√η=10⁻⁴e^(iπ/4)=10⁻⁴(1+i)/√2. Les racines sont c±10⁻⁴(1+i)/√2, chacune à distance 10⁻⁴ du centre. Le choix de l’autre racine carrée échange simplement les deux racines.

## 75. Ce que le polynôme perturbé change

Spé · Laboratoire `conditionnement_racines`

Comparer Pδ,η=[(Z−c)²−δ²−η]Q à Pδ. Les trois racines de Q sont-elles déplacées ?

**Correction guidée**

Pδ,η−Pδ=−ηQ. Les trois racines de Q restent exactement racines du polynôme perturbé. Seule la paire du facteur quadratique se déplace. Cela permet une étude contrôlée, mais ce n’est pas la même expérience qu’ajouter une constante au polynôme de degré 5.

## 76. L’initialisation compte

Sup · Laboratoire `recurrence_complexe`

Avec λ=1, calculer P₂ et P₃, à partir de P₀=1, P₁=2Z et Pₖ₊₂=−ZPₖ₊₁−Pₖ.

**Correction guidée**

P₂=−Z(2Z)−1=−2Z²−1. P₃=−Z(−2Z²−1)−2Z=2Z³−Z. Leurs degrés sont 2 et 3; ils ne sont pas les Tchebychev de première ou de deuxième espèce avec leur initialisation habituelle.

## 77. Une racine caractéristique double

Sup / Spé · Laboratoire `recurrence_complexe`

Avec λ=1 et z=2, calculer P₈(2) sans développer P₈.

**Correction guidée**

t=2, donc r²+2r+1=(r+1)². La forme est (A+Bn)(−1)ⁿ. P₀=1 impose A=1 et P₁(2)=4 impose −(1+B)=4, soit B=−5. P₈(2)=(1−40)(−1)⁸=−39.

## 78. Transporter les racines

Spé · Laboratoire `recurrence_complexe`

Montrer Pₙ,λ(Z)=Pₙ,₁(λZ), puis en déduire les racines de P₂,λ pour λ=e^(iπ/4).

**Correction guidée**

Les deux familles ont les mêmes valeurs initiales après substitution Z↦λZ et satisfont la même récurrence : l’égalité suit par récurrence. P₂,λ=−2λ²Z²−1=−2iZ²−1. Les racines de P₂,₁ sont ±i/√2; celles de P₂,λ sont donc ±e^(iπ/4)/√2.

## 79. Ne pas additionner les degrés partiels

Sup · Laboratoire `monomes_newton`

Pour P(x,y)=2x⁵y²−3x²y⁶+y⁷+4, déterminer le support, les degrés partiels et le degré total. Que devient le degré après y=0 ?

**Correction guidée**

Support : {(5,2),(2,6),(0,7),(0,0)}. Les degrés en x et y valent 5 et 7. Les degrés des termes sont 7,8,7,0, donc deg P=8. La spécialisation P(x,0)=4 a degré 0 ; elle ne conserve pas le degré en x.

## 80. Le produit additionne les degrés totaux

Sup / Spé · Laboratoire `monomes_newton`

Dans ℝ[x,y], montrer que deg(PQ)=deg P+deg Q pour deux polynômes non nuls. Pourquoi le même argument ne justifie-t-il pas deg(P+Q)=max(deg P,deg Q) sans condition ?

**Correction guidée**

Écrire P=P_d+termes de degré inférieur et Q=Q_e+termes de degré inférieur, où P_d,Q_e sont leurs parties homogènes dominantes. La partie de degré d+e de PQ vaut P_dQ_e≠0, car ℝ[x,y] est intègre. Pour la somme, les parties dominantes peuvent se compenser : (x²+y²)+(−x²−y²+x)=x.

## 81. Une enveloppe convexe qui change

Au-delà · accompagné · Laboratoire `monomes_newton`

Pour P=x⁴+y⁴+ax²y³+1, calculer l’aire du polygone de Newton lorsque a=0 puis lorsque a≠0. Le signe de a intervient-il ?

**Correction guidée**

Si a=0, le support extrême est (0,0),(4,0),(0,4), triangle d’aire 8. Si a≠0, le point (2,3) est extérieur au triangle : le quadrilatère (0,0),(4,0),(2,3),(0,4) a aire (12+8)/2=10. Le signe de a ne change pas le support ; seul son caractère nul ou non nul intervient.

## 82. Trois points, quatre multiplicités

Sup · Laboratoire `intersection_bezout`

Déterminer les intersections réelles de x²+y²=1 et y=x²−1.

**Correction guidée**

Q=x⁴−x²=x²(x²−1). Les abscisses sont 0 (multiplicité 2),1 et −1 (multiplicité 1). Les points distincts sont (0,−1),(1,0),(−1,0). Leur multiplicité totale vaut 4. Le cercle et la parabole sont tangents en (0,−1).

## 83. Deux points, deux tangences

Spé · Laboratoire `intersection_bezout`

Prendre r=1 et h=5/4. Déterminer les intersections et vérifier la tangence par les dérivées des équations.

**Correction guidée**

Q=x⁴−(3/2)x²+9/16=(x²−3/4)². Les points sont (±√3/2,−1/2), chacun de multiplicité 2. Sur le cercle, 2x+2y y′=0 donne y′=−x/y=2x ; sur la parabole, y′=2x. Les pentes coïncident.

## 84. Le réel ne montre pas tout

Sup / Au-delà · Laboratoire `intersection_bezout`

Prendre r=1 et h=−2. Montrer qu’il n’y a aucun point réel commun, puis conserver les quatre solutions algébriques.

**Correction guidée**

Pour x réel, y=x²+2≥2 tandis que le cercle impose |y|≤1 : aucune solution réelle. Q=x⁴+5x²+3. Ses valeurs de t=x² sont (−5±√13)/2, toutes deux négatives. Chacune donne deux racines imaginaires non nulles en x ; y=t+2. Les quatre points complexes sont distincts.

## 85. Un système avec un candidat rejeté

Spé · Laboratoire `resultant_elimination`

Résoudre (x−2)y−1=0 et (x−2)(y+1)=0 par résultant, en vérifiant chaque abscisse.

**Correction guidée**

Ici a=2,b=−1. Le résultant vaut (x−2)[1+(x−2)]=(x−2)(x−1). Pour x=2, F=−1 : rejet. Pour x=1, F=−y−1 donne y=−1, qui vérifie G=0. L’unique solution est (1,−1).

## 86. Détecter une contradiction sans calcul lourd

Sup · Laboratoire `resultant_elimination`

Montrer que xy=1 et xy=0 n’ont pas de solution, tout en calculant leur résultant par rapport à y.

**Correction guidée**

La contradiction 1=0 suffit. Pour F=xy−1 et G=xy, le déterminant des coefficients en y vaut x×0−(−1)×x=x. Son zéro x=0 est parasite puisque F(0,y)=−1. Un résultant non constant ne prouve donc pas à lui seul l’existence d’un point affine commun.

## 87. Quand la vérification devient suffisante

Spé · Laboratoire `resultant_elimination`

Pour F=A(x)y+B(x), G=C(x)y+D(x), supposer A(x₀)≠0 et R(x₀)=0. Prouver qu’un unique y₀ satisfait les deux équations.

**Correction guidée**

F impose y₀=−B(x₀)/A(x₀). Alors G(x₀,y₀)=[A(x₀)D(x₀)−B(x₀)C(x₀)]/A(x₀)=R(x₀)/A(x₀)=0. L’unicité vient de A(x₀)≠0. La chute de degré qui créait le candidat parasite est ainsi exclue par une hypothèse précise.

## 88. Certifier l’égalité des idéaux

Spé / Au-delà · Laboratoire `groebner_ordre`

Avec F=xy−1, G=y²−x−c, g₁=x−y²+c et g₂=y³−cy−1, donner les quatre identités qui prouvent (F,G)=(g₁,g₂).

**Correction guidée**

g₁=−G et g₂=yG+F donnent (g₁,g₂)⊂(F,G). Inversement, G=−g₁ et F=g₂+yg₁ donnent (F,G)⊂(g₁,g₂). Il faut les deux inclusions : produire de nouveaux polynômes dans l’idéal ne prouve pas seul qu’ils l’engendrent.

## 89. Un calcul matriciel dans le quotient

Au-delà · algèbre linéaire · Laboratoire `groebner_ordre`

Prendre c=0. Dans la base (1,y,y²) du quotient, écrire la matrice de la multiplication par y et son polynôme caractéristique.

**Correction guidée**

La relation est y³=1. Les images sont y, y², 1, donc la matrice, par colonnes, est [[0,0,1],[1,0,0],[0,1,0]]. Son polynôme caractéristique est T³−1. Les trois solutions complexes en y sont les racines cubiques de l’unité ; x=y².

## 90. Un S-polynôme contrôlable à la main

Au-delà · technique · Laboratoire `groebner_ordre`

Avec H=x²+cx−y et F=xy−1, calculer S=yH−xF. Montrer qu’il se réduit à zéro par H,F,G où G=y²−x−c.

**Correction guidée**

S=cxy−y²+x=c(xy−1)−(y²−x−c)=cF−G. Son reste est donc nul en retirant cF puis −G. Cette identité est un certificat explicite, indépendant d’une inspection du dessin.

## 91. Calculer une somme sans résoudre une cubique

Spé · Laboratoire `symetriques`

Soient α,β,γ les racines complexes de T³−3T²+2T−1. Calculer α²+β²+γ² puis α⁴+β⁴+γ⁴.

**Correction guidée**

e₁=3,e₂=2,e₃=1. p₁=3, p₂=9−4=5, p₃=3×5−2×3+3=12. Ensuite p₄=3×12−2×5+1×3=29. Aucune résolution explicite de la cubique n’est nécessaire.

## 92. Une expression symétrique qui n’est pas une puissance

Sup / Spé · Laboratoire `symetriques`

Exprimer (u−v)²+(v−w)²+(w−u)² en e₁=u+v+w et e₂=uv+uw+vw.

**Correction guidée**

La somme vaut 2(u²+v²+w²)−2(uv+uw+vw)=2p₂−2e₂=2e₁²−6e₂. Pour u,v,w réels, elle est non négative ; on retrouve e₁²≥3e₂, avec égalité si et seulement si u=v=w.

## 93. Des traces sans diagonalisation

Spé · algèbre linéaire · Laboratoire `symetriques`

Une matrice A de taille 3 a polynôme caractéristique T³−3T²+2T−1. Calculer tr(A²) et tr(A⁴), même si A n’est pas diagonalisable.

**Correction guidée**

Sur ℂ, A est triangulisable : la diagonale de Aᵏ contient αᵏ,βᵏ,γᵏ, avec multiplicité. Ainsi tr(Aᵏ)=pₖ, sans hypothèse de diagonalisation. Newton donne tr(A²)=5 et tr(A⁴)=29. Les mêmes valeurs se retrouvent en utilisant Cayley–Hamilton et les premières traces.

## 94. Écarter un faux point singulier

Spé · Laboratoire `singularites`

Pour F=y²−x³−2x², résoudre ∇F=0 puis déterminer les points singuliers de F=0.

**Correction guidée**

∂F/∂y=2y impose y=0 ; ∂F/∂x=−x(3x+4) impose x=0 ou x=−4/3. Au second candidat F=−32/27≠0. Seule l’origine est singulière sur la courbe. Les tangentes y=±√2 x sont distinctes.

## 95. Une pointe paramétrée sans racine carrée

Sup / Spé · Laboratoire `singularites`

Pour y²=x³, donner un paramétrage polynomial couvrant toute la courbe réelle et expliquer le comportement de sa vitesse à l’origine.

**Correction guidée**

x=s²,y=s³, s∈ℝ, vérifie l’équation et couvre la courbe réelle : pour x>0, s=y/x. La vitesse vaut (2s,3s²), donc s=0 donne le vecteur nul. Le quotient y/x=s tend vers 0, ce qui montre la tangente y=0, mais le paramétrage n’est pas régulier à l’origine.

## 96. Un point isolé démontré par une boule

Spé · Laboratoire `singularites`

Pour t=−1, montrer que la boule ouverte de rayon 1/2 centrée à l’origine ne contient aucun autre point de y²=x²(x−1).

**Correction guidée**

Dans cette boule, |x|<1/2. Si x≠0, x−1<0 et x²(x−1)<0, impossible pour y²≥0. Si x=0, l’équation donne y=0. La seule intersection avec la boule est donc l’origine. Cela établit l’isolement au sens topologique.

## 97. Une conique et ses points à l’infini

Sup / Au-delà · Laboratoire `homogenisation`

Homogénéiser x²+2xy+3y²−1=0. Chercher ses points à l’infini réels puis complexes.

**Correction guidée**

L’équation est X²+2XY+3Y²−Z²=0. À Z=0, X²+2XY+3Y²=(X+Y)²+2Y² : aucun point projectif réel. Sur ℂ, Y≠0 et X/Y=−1±i√2. Les deux points complexes à l’infini sont [−1+i√2:1:0] et [−1−i√2:1:0].

## 98. Retrouver la transition entre cartes

Spé / Au-delà · Laboratoire `homogenisation`

Un point affine de la parabole y=x²+c a y≠0. Exprimer ses coordonnées u,v dans la carte Y≠0 et vérifier v−u²−cv²=0.

**Correction guidée**

Le point s’écrit [x:y:1], donc u=x/y et v=1/y. Alors v−u²−cv²=(y−x²−c)/y²=0. Inversement, si v≠0, x=u/v et y=1/v. Le point (u,v)=(0,0) ne peut pas revenir dans la carte affine, car la transition diviserait par v=0.

## 99. Une droite et une parabole

Spé / Au-delà · Laboratoire `homogenisation`

Montrer que la droite y=mx+b n’a aucun point commun à l’infini avec y=x²+c, puis expliquer pourquoi leur nombre complexe d’intersections avec multiplicité vaut deux.

**Correction guidée**

La droite homogène est Y−mX−bZ=0 ; la parabole à l’infini possède seulement [0:1:0], qui ne satisfait pas la droite. En affine, x²−mx+(c−b)=0 est une équation monique de degré 2, donc deux racines complexes avec multiplicité. Le cas de discriminant nul est une tangence.

## 100. Une preuve exacte de positivité

Spé · Laboratoire `formes_quadratiques`

Prendre a=1/2,b=2,c=1/2. Prouver que Q est définie positive et donner une décomposition en carrés.

**Correction guidée**

Δ₂=3/4 et Δ₃=2×3/4−1/4=5/4>0. La complétion donne Q=(x+y/2)²+(3/4)(y+2z/3)²+(5/3)z². Tous les coefficients sont positifs ; Q ne s’annule qu’en (0,0,0).

## 101. Une direction négative suffit

Sup / Spé · Laboratoire `formes_quadratiques`

Prendre a=3/2,b=2,c=1/2. Sans calculer les valeurs propres, montrer que Q est indéfinie.

**Correction guidée**

Q(1,0,0)=1>0. Avec z=0 et x=−y=1, Q=1+1+2×(3/2)×(−1)=−1<0. Deux vecteurs donnant des signes opposés suffisent à prouver l’indéfinition. Le déterminant seul ne fournirait pas cette conclusion dans tous les cas.

## 102. Déterminer le noyau sur un bord

Spé · Laboratoire `formes_quadratiques`

Pour a=1,b=c=0, classer Q et déterminer son lieu d’annulation. Une tranche z=0 suffit-elle à voir tout ce lieu ?

**Correction guidée**

Q=(x+y)², donc semi-définie positive. Son lieu d’annulation est le plan x+y=0, avec z arbitraire. A a valeurs propres 2,0,0 et un noyau de dimension 2. La tranche z=0 ne montre que la droite x+y=0 ; elle masque la seconde direction nulle.

## 103. Une preuve en trois termes

Sup · Laboratoire `positivite_motzkin`

Prouver x⁴y²+x²y⁴+1≥3x²y² pour tous x,y réels et déterminer les cas d’égalité.

**Correction guidée**

Appliquer l’inégalité arithmético-géométrique aux trois termes non négatifs A=x⁴y²,B=x²y⁴,C=1. Leur produit vaut x⁶y⁶, donc (ABC)¹ᐟ³=x²y². L’égalité exige A=B=C=1, d’où |x|=|y|=1. Les quatre couples (±1,±1) réalisent l’égalité.

## 104. Un minimum exact, pas seulement un contre-exemple

Spé · Laboratoire `positivite_motzkin`

Pour λ=4, calculer le minimum global de Mλ et tous les points où il est atteint. Comparer avec la valeur en (1,1).

**Correction guidée**

Le minimum est 1−4³/27=−37/27, réalisé en x,y=±√(4/3)=±2/√3. La valeur M₄(1,1)=−1 démontre déjà la non-positivité, mais n’est pas le minimum. L’égalité |x|=|y| dans la réduction et t=4/3 donnent exactement les quatre points minimisants.

## 105. Pourquoi l’analogie avec les quadratiques échoue

Spé / Au-delà · Laboratoire `positivite_motzkin`

Une forme quadratique réelle non négative est une somme de carrés de formes linéaires. Expliquer pourquoi ce fait ne se généralise pas à tous les polynômes de deux variables.

**Correction guidée**

Le théorème spectral diagonalise une matrice symétrique : Q=∑λᵢuᵢ², et λᵢ≥0 fournit des carrés (√λᵢuᵢ)². Le polynôme de Motzkin M₃ est de degré 6, non négatif par l’inégalité arithmético-géométrique, mais la comparaison des coefficients interdit M₃=∑qᵢ². La matrice d’une forme quadratique n’encode donc pas directement tous les degrés supérieurs.

## 106. Huit candidats et deux bornes

Sup / Spé · Laboratoire `lagrange_contrainte`

Optimiser x⁴+y⁴+xy sur x²+y²=1 et compter les points stationnaires.

**Correction guidée**

a=r=1. Les candidats satisfont cos(2θ)=0 ou sin(2θ)=1/2 : les deux familles fournissent huit points distincts. Avec s∈[−1,1], f=1−s²/2+s/2. Le minimum vaut 0, atteint lorsque s=−1, soit x=−y=±1/√2. Le maximum vaut 9/8, atteint lorsque s=1/2, soit xy=1/4 avec x²+y²=1 : quatre points.

## 107. Une seconde dérivée nulle mais un maximum

Spé / Au-delà · Laboratoire `lagrange_contrainte`

Pour a=2,r=1, examiner f sur le cercle au voisinage de θ=π/4. La dérivée seconde s’annule : peut-on conclure ?

**Correction guidée**

Avec s=sin(2θ), f=1−s²/2+s=3/2−(s−1)²/2. À θ=π/4+h, s=cos(2h)=1−2h²+O(h⁴), donc f=3/2−2h⁴+O(h⁶). C’est un maximum strict local, malgré la dérivée seconde nulle. L’écriture exacte fournit aussi le maximum global 3/2.

## 108. Changer le rayon change le seuil

Spé · Laboratoire `lagrange_contrainte`

Optimiser x⁴+y⁴+4xy sur x²+y²=4. Déterminer le nombre de points stationnaires et les valeurs extrêmes.

**Correction guidée**

r=2,a=4 : le seuil est 2r²=8 et |a|<8, donc huit stationnaires. Le minimum vaut r⁴/2−|a|r²/2=8−8=0 ; le maximum vaut r⁴+a²/8=16+2=18. Les maxima vérifient sin(2θ)=a/(2r²)=1/2, soit xy=1. Les minima vérifient x=−y=±√2.
