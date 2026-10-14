# Polynômes & Géométrie — 72 leçons

Recueil de A. R., fiche M17, pages 165–172, et exercices des pages 31 et 39. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.

## 01. Quotient polynomial et parties polaires

Sup — fractions rationnelles · Laboratoire `rationnelle_recueil`

Une fraction rationnelle F=P/Q est un quotient de polynômes, Q non nul. Réduire F consiste à supprimer leur PGCD. La division P=EQ+R, avec deg R<deg Q, sépare le polynôme E, appelé partie entière, de R/Q.

Dans l’exercice 4, P=X⁴−2X³−7X²+29X−21 et Q=X⁴−5X³+6X²+4X−8=(X+1)(X−2)³. Les coefficients dominants sont égaux : la partie entière vaut 1.

F=1+2/(X+1)+1/(X−2)+2/(X−2)²+3/(X−2)³.

Multiplier cette égalité par Q permet une vérification polynomialement exacte, même si le graphique ne montre qu’un nombre fini de valeurs.

## 02. Identifier les coefficients sans système global

Sup — méthode locale · Laboratoire `rationnelle_recueil`

Soit a un pôle simple. On appelle c le coefficient de 1/(X−a). Après multiplication de F par X−a, les autres termes restent réguliers et le terme c est isolé par évaluation en a.

Pour un pôle triple en b, poser g=(X−b)³F. Les trois coefficients devant (X−b)⁻³, (X−b)⁻² et (X−b)⁻¹ sont respectivement g(b), g′(b) et g″(b)/2. Les termes réguliers multipliés par (X−b)³ n’interviennent pas dans ces évaluations.

Si le premier coefficient est nul, le pôle n’est plus triple. L’ordre effectif se lit après réduction.

## 03. Taylor devient une décomposition en puissances

Sup — Taylor exact · Laboratoire `poles_multiples`

Soit g un polynôme de degré d et a un nombre. En posant h=X−a, on écrit exactement g(X)=Σ_{j=0}^d g^(j)(a)h^j/j!. Il n’y a pas de reste d’approximation.

Diviser par h^m donne des puissances h^(j−m). Les indices j<m produisent la partie polaire ; les indices j≥m produisent la partie entière.

A_k=g^(m−k)(a)/(m−k)!, pour 1≤k≤m.

## 04. L’ordre du pôle résiste-t-il à la réduction ?

Sup — zéros et pôles · Laboratoire `poles_multiples`

Soit r la multiplicité du zéro de g en a : g=(X−a)^r u et u(a)≠0. Si r<m, la fraction a un pôle d’ordre m−r. Si r≥m, elle est régulière après simplification.

Le dénominateur initial interdit toujours a à l’expression de départ. La formule réduite peut toutefois fournir un prolongement continu. Cette distinction relie factorisation et limites.

## 05. Le coefficient d’un pôle non réel

Sup — factorisation complexe · Laboratoire `reel_complexe`

Avec a,b,u,v réels et b>0, les racines du quadratique (X−a)²+b² sont α=a+ib et β=a−ib. Le coefficient c_α du pôle α est obtenu en multipliant par X−α.

c_α=(uα+v)/(α−β) ; c_β=conj(c_α).

On peut aussi écrire le dénominateur Q et calculer c_α=P(α)/Q′(α) pour une fraction P/Q à pôle simple α. Cette règle vient de Q=(X−α)q et Q′(α)=q(α).

## 06. Pourquoi la somme reste réelle

Sup — conjugaison · Laboratoire `reel_complexe`

Pour une valeur réelle x, les nombres c_α/(x−α) et conj(c_α)/(x−conj(α)) sont conjugués. Leur somme vaut deux fois la partie réelle du premier.

Sur le plan complexe du TP, les points sont les pôles. La courbe réelle représente les valeurs de la fraction sur ℝ : ce sont deux objets distincts, à relier par la factorisation.

c_α/(X−α)+conj(c_α)/(X−conj(α))=(uX+v)/[(X−a)²+b²].

## 07. Réduire un quotient et conserver son domaine

Sup — fonctions et polynômes · Laboratoire `annulations`

Deux écritures P/Q et A/B représentent la même fraction rationnelle si PB=AQ. Comme fonctions numériques, elles coïncident là où leurs deux dénominateurs sont non nuls.

Par exemple (X²−1)/(X−1)=X+1 dans ℝ(X). L’expression de gauche reste interdite en x=1 ; la fonction x↦x+1 fournit son prolongement continu. Le trou a pour ordonnée 2.

## 08. Lorsque les points interdits se confondent

Sup — multiplicités · Laboratoire `annulations`

Dans le TP, les facteurs X²+1 se simplifient et n’ont pas de zéro réel. Si a≠b, l’ordre en a dépend de m−k, tandis que b reste un pôle simple.

Si a=b, le dénominateur contient (X−a)^(m+1). La fraction réduite devient (X−a)^(k−m−1). Le seuil entre trou et pôle se déplace donc d’une unité. L’identité des points doit être vérifiée avant de lire les multiplicités.

## 09. Lagrange : existence et unicité

Sup — interpolation · Laboratoire `interpolation`

Soient n+1 nœuds distincts x₀,…,x_n et des valeurs y₀,…,y_n. Le polynôme L_i(X)=∏_{j≠i}(X−x_j)/(x_i−x_j) vaut 1 au nœud i et 0 aux autres.

P(X)=Σ_{i=0}^n y_i L_i(X), deg P≤n.

Si deux polynômes de degré au plus n satisfont les mêmes contraintes, leur différence possède n+1 racines distinctes. Elle est donc nulle. Cette preuve évite de calculer un déterminant.

## 10. Changer les nœuds plutôt que monter le degré

Spé — prolongement numérique · Laboratoire `interpolation`

Le poids barycentrique w_i est 1/∏_{j≠i}(x_i−x_j). Pour x différent des nœuds, l’interpolateur s’évalue par [Σ w_i y_i/(x−x_i)]/[Σ w_i/(x−x_i)]. Aux nœuds, on reprend directement la valeur y_i.

Cette écriture évite le développement dans les monômes. Elle ne supprime pas le phénomène de Runge : celui-ci concerne le choix des nœuds et l’approximation. Les nœuds de Tchebychev, cos((2i+1)π/[2(n+1)]), se resserrent aux extrémités et améliorent ce cas.

## 11. Trois produits scalaires, trois bases

Sup / spé — espaces préhilbertiens · Laboratoire `orthogonaux`

Pour deux polynômes A,B, on définit ⟨A,B⟩=∫A(x)B(x)w(x)dx. Les poids du TP sont positifs et les moments nécessaires existent. La famille de degré croissant obtenue par orthogonalisation est une base de chaque espace de polynômes de degré borné.

Legendre est normalisé par L_n(1)=1. Tchebychev vérifie T_n(cos θ)=cos(nθ). Hermite probabiliste vérifie H₀=1, H₁=X et H_{n+1}=XH_n−nH_{n−1}. Les trois normalisations sont précisées : elles ne sont pas interchangeables.

‖L_n‖²=2/(2n+1) ; ‖T_n‖²=π/2 pour n≥1 ; ‖H_n‖²=√(2π)n!.

## 12. Pourquoi n nœuds intègrent jusqu’au degré 2n−1

Au-delà — quadrature de Gauss · Laboratoire `orthogonaux`

Soit P_n le polynôme orthogonal de degré n et x_i ses racines simples. Les poids W_i sont choisis pour intégrer exactement les polynômes de degré au plus n−1.

Pour un polynôme R de degré au plus 2n−1, diviser R=P_nQ+S avec deg Q≤n−1 et deg S≤n−1. L’intégrale de P_nQ est nulle par orthogonalité ; ses valeurs aux nœuds sont nulles aussi. La formule est donc exacte pour R.

Pour R=P_n², la quadrature donne zéro mais l’intégrale est strictement positive. Le degré 2n−1 est ainsi le meilleur degré garanti pour ces n nœuds.

## 13. Pourquoi la division termine

Sup · Laboratoire `euclide_bezout`

A et B sont deux polynômes sur un corps K, avec B≠0. La division écrit A=BQ+R avec R=0 ou deg R<deg B. Un diviseur commun de A et B divise aussi R=A−BQ; réciproquement, un diviseur de B et R divise A.

Ainsi PGCD(A,B)=PGCD(B,R). Les degrés des restes non nuls diminuent strictement : l’algorithme termine. Le dernier reste peut avoir un coefficient dominant différent de 1; on le divise par ce coefficient pour obtenir **le PGCD unitaire**.

## 14. Deux certificats pour un même reste

Sup / spé · Laboratoire `euclide_bezout`

U et V sont les polynômes obtenus en remontant les divisions : AU+BV=D, où D est le PGCD unitaire. Cette identité prouve que tout diviseur commun divise D. Pour vérifier complètement le résultat, on contrôle aussi D|A et D|B.

Dans le TP, A=X⁴ et B=(X−1)(X−2)(X−3). Le reste R a degré au plus 2 et vérifie R(1)=1, R(2)=16, R(3)=81. On trouve R=25X²−60X+36 et Q=X+6. L’interpolation et la division conduisent au même certificat : X⁴=(X+6)B+R.

## 15. Deux énoncés portant le nom de Gauss

Sup / prolongement · Laboratoire `gauss_eisenstein`

A, B et C sont des polynômes sur un corps K. Le **théorème de Gauss de divisibilité** dit : si PGCD(A,B)=1 et A|BC, alors A|C. Bézout fournit AU+BV=1; multiplier par C permet de conclure.

Pour un polynôme entier non nul P, son contenu c(P) est le PGCD positif de ses coefficients. Le **lemme de Gauss sur le contenu** donne c(PQ)=c(P)c(Q). Un produit de polynômes primitifs est donc primitif. Il relie les factorisations de ℤ[X] et de ℚ[X]. Ces deux énoncés ne portent pas sur les mêmes objets.

## 16. Ce qui constitue une preuve d’irréductibilité

Au-delà accompagné · Laboratoire `gauss_eisenstein`

P=aₙXⁿ+⋯+a₀ est un polynôme entier primitif. Pour un nombre premier p, Eisenstein exige p∤aₙ, p|aₖ pour k<n et p²∤a₀. Ces conditions impliquent l’irréductibilité sur ℚ. Elles peuvent devenir visibles après la substitution X→X+t, qui conserve la possibilité d’une factorisation.

La réduction modulo p fournit un autre certificat si elle conserve le degré et devient irréductible sur Fₚ. Pour X⁴+X+1 sur F₂, aucun facteur linéaire n’existe; le seul quadratique unitaire irréductible X²+X+1 ne le divise pas. À l’inverse, X⁴+4 est sans racine réelle mais se factorise en deux quadratiques.

## 17. La relation M(X)=0 réduit les calculs

Spé / prolongement · Laboratoire `inverse_quotient`

K est un corps et M un polynôme unitaire de degré m≥1. Dans K[X]/(M), deux polynômes représentent la même classe si leur différence est divisible par M. La division euclidienne donne un représentant unique de degré inférieur à m.

Les classes de 1,X,…,Xᵐ⁻¹ forment une base : le quotient est une K-algèbre de dimension m. Multiplier par la classe de A est un endomorphisme; les restes de AXʲ donnent les colonnes de sa matrice. On conserve ici cette dimension même si M est réductible.

## 18. L’inverse et le diviseur de zéro viennent du même PGCD

Au-delà accompagné · Laboratoire `inverse_quotient`

A est un polynôme et D=PGCD(A,M). Si D=1, Bézout donne AU+MV=1 : la classe de U est l’inverse de celle de A. Réciproquement, un inverse modulo M donne une telle identité, donc D=1.

Si D a un degré positif, écrire A=DA₁ et M=DM₁. Alors AM₁=A₁M≡0 modulo M, tandis que la classe de M₁ est non nulle car son degré est inférieur à celui de M. Cela donne un témoin concret de non-inversibilité. Le quotient est un corps exactement lorsque M est irréductible.

## 19. Deux congruences, deux projecteurs

Spé / prolongement · Laboratoire `restes_chinois`

M₁ et M₂ sont premiers entre eux dans K[X]. Bézout donne U₁M₁+U₂M₂=1. Poser E₁=U₂M₂ et E₂=U₁M₁, puis travailler modulo L=M₁M₂.

E₁ vaut 1 modulo M₁ et 0 modulo M₂; E₂ fait l’inverse. La solution S≡R₁E₁+R₂E₂ possède les restes voulus. Elle est unique modulo L : une différence entre deux solutions est divisible par les deux modules, donc par leur produit. E₁+E₂=1, Eᵢ²≡Eᵢ et E₁E₂≡0 expriment le rôle de projecteurs.

## 20. Un facteur commun ne rend pas tout impossible

Au-delà accompagné · Laboratoire `restes_chinois`

D=PGCD(M₁,M₂). Si S possède les deux restes R₁,R₂, alors D divise R₂−R₁. Cette condition est aussi suffisante. Écrire S=R₁+M₁W et diviser la deuxième congruence par D.

On résout (M₁/D)W≡(R₂−R₁)/D modulo M₂/D; les nouveaux modules sont premiers entre eux. L’unicité est modulo L=PPCM(M₁,M₂). Dans le labo, le facteur X−1 impose la même valeur des deux restes en X=1 : une différence de 1 à cet endroit interdit la solution.

## 21. Pourquoi μ annule les carrés

Au-delà accompagné · Laboratoire `mobius_diviseurs`

n≥1 possède r facteurs premiers distincts. Les diviseurs d de n pour lesquels μ(d)≠0 correspondent aux choix de sous-ensembles de ces r nombres premiers. Un sous-ensemble de taille j contribue (−1)ʲ.

Ainsi Σ_{d|n}μ(d)=(1−1)ʳ. La somme vaut 0 pour n>1 et vaut 1 pour n=1. Pour la convolution (f∗g)(n)=Σ_{d|n}f(d)g(n/d), cela s’écrit μ∗1=χ, où χ(1)=1 et χ(n)=0 sinon. La constante 1 est ici une fonction, pas l’unité de la convolution.

## 22. Inverser en réorganisant une somme finie

Spé / au-delà accompagné · Laboratoire `mobius_diviseurs`

Supposer f(n)=Σ_{d|n}g(d). Alors Σ_{d|n}μ(d)f(n/d)=Σ_{de|n}μ(d)g(e). Pour chaque e|n, le coefficient de g(e) est Σ_{d|n/e}μ(d), égal à 1 si e=n et à 0 sinon. Il reste donc g(n).

Pour φ, on classe les entiers a∈{1,…,n} selon PGCD(a,n). Ce regroupement donne Σ_{d|n}φ(d)=n. L’inversion fournit φ(n)=Σ_{d|n}μ(d)n/d=n∏_{p|n}(1−1/p). Le produit est justifié ici par les sous-ensembles de facteurs premiers.

## 23. D’abord compter tous les facteurs de Frobenius

Au-delà accompagné · Laboratoire `irreductibles_fp`

p est premier et n≥1. Le polynôme X^(pⁿ)−X a dérivée −1 sur Fₚ, donc ses facteurs irréductibles sont tous simples. Ses facteurs sont exactement les polynômes unitaires irréductibles dont le degré d divise n.

Noter Iₚ(d) leur nombre. En comparant les degrés, pⁿ=Σ_{d|n}dIₚ(d). Cette identité porte sur des polynômes et leurs degrés; elle ne signifie pas qu’il existe pⁿ résidus différents modulo p.

## 24. Une formule entière qui se contrôle

Au-delà accompagné · Laboratoire `irreductibles_fp`

Appliquer l’inversion de Möbius à f(n)=pⁿ et g(n)=nIₚ(n). On obtient **Iₚ(n)=(1/n)Σ_{d|n}μ(d)p^(n/d)**. Le résultat est un entier car il dénombre des objets.

Pour p=2,n=6 : 6I₂(6)=2⁶−2³−2²+2=54, donc I₂(6)=9. Le labo énumère ici les 64 polynômes unitaires et teste leur irréductibilité. En degré 2, être réductible équivaut à avoir une racine dans le corps; en degré supérieur, ce test ne suffit plus.

## 25. La dérivée change avec la caractéristique

Au-delà accompagné · Laboratoire `frobenius_fp`

Dans Fₚ[X], un entier multiple de p représente le coefficient nul. La dérivée de X^(pⁿ) est donc nulle : (X^(pⁿ)−X)′=−1. Le PGCD du polynôme avec sa dérivée vaut 1.

Sur un corps, un facteur irréductible répété divise aussi la dérivée. Ici, c’est impossible. En revanche, Xᵖ−a a une dérivée nulle et peut être un p-ième pouvoir; la règle familière des racines simples exige de regarder la caractéristique.

## 26. Des racines qui forment un corps

Au-delà accompagné · Laboratoire `frobenius_fp`

Dans une clôture algébrique de Fₚ, l’ensemble des racines de X^(pⁿ)−X possède pⁿ éléments distincts. Si a et b sont racines, (a+b)^(pⁿ)=a^(pⁿ)+b^(pⁿ)=a+b et (ab)^(pⁿ)=ab. L’inverse d’une racine non nulle reste une racine.

Cet ensemble est donc un corps F_(pⁿ). Une racine d’un irréductible de degré d sur Fₚ y appartient exactement lorsque d|n. Cela explique la factorisation du labo. Les éléments supplémentaires ne sont pas de nouveaux résidus modulo p : ils vivent dans une extension de dimension n sur Fₚ.

## 27. Une racine de l’unité n’a pas toujours l’ordre annoncé

Sup · Laboratoire `cyclotomie`

ζ=exp(2πik/n). Le plus petit entier r>0 tel que ζʳ=1 vaut n/PGCD(k,n). La racine est primitive d’ordre n si PGCD(k,n)=1. Par exemple, exp(2πi×4/12) a ordre 3, alors que exp(2πi×5/12) a ordre 12.

En regroupant les racines de Xⁿ−1 selon leur ordre d, on obtient Xⁿ−1=∏_{d|n}Φ_d. Le polynôme Φₙ a donc degré φ(n). La première étape demande seulement les racines de l’unité; l’irréductibilité de Φₙ sur ℚ est un théorème supplémentaire.

## 28. Möbius peut aussi inverser des produits

Au-delà accompagné · Laboratoire `cyclotomie`

Dans le corps des fractions rationnelles, l’identité Xⁿ−1=∏_{d|n}Φ_d donne Φₙ=∏_{d|n}(Xᵈ−1)^μ(n/d). Pour le vérifier, le coefficient de chaque Φ_e dans le produit est Σ_{d|n/e}μ(d), égal à 1 si e=n et à 0 sinon.

Des exposants −1 apparaissent, mais le résultat est un polynôme. Pour n=12, Φ₁₂=(X¹²−1)(X²−1)/[(X⁶−1)(X⁴−1)]=X⁴−X²+1. Le labo effectue la division et affiche le reste nul; un simple graphique ne certifierait pas la simplification.

## 29. La constante de primitive est déterminée par une moyenne

Sup / prolongement · Laboratoire `bernoulli_faulhaber`

Poser B₀=1. Pour m≥1, Bₘ est l’unique primitive de mBₘ₋₁ dont l’intégrale sur [0,1] est nulle. Ainsi B₁=X−1/2, B₂=X²−X+1/6 et B₃=X³−3X²/2+X/2.

Les nombres bₘ=Bₘ(0) sont des rationnels. Cette convention donne b₁=−1/2. La différence finie Bₘ(X+1)−Bₘ(X)=mXᵐ⁻¹ joue pour les sommes le rôle qu’une dérivée joue pour les intégrales. Une convention utilisant +1/2 doit être accompagnée d’une formule de sommation adaptée.

## 30. Faulhaber par annulation des termes intermédiaires

Spé / prolongement · Laboratoire `bernoulli_faulhaber`

Pour p≥1, sommer Bₚ₊₁(k+1)−Bₚ₊₁(k)=(p+1)kᵖ de k=0 à N. Chaque terme intermédiaire apparaît une fois avec chaque signe. Il reste Sₚ(N)=[Bₚ₊₁(N+1)−Bₚ₊₁(0)]/(p+1).

Cette expression est un polynôme en N de degré p+1, de coefficient dominant 1/(p+1). Pour p=3, S₃(N)=N²(N+1)²/4. Le calcul direct sur les entiers sert de contrôle; la preuve repose sur le télescopage, pas sur quelques valeurs numériques.

## 31. Commencer par les deux extrémités

Spé / prolongement · Laboratoire `euler_maclaurin`

Pour l<m entiers, S=Σ_{j=l}^m f(j). Si f est continûment dérivable, S=∫ₗᵐf(x)dx+[f(l)+f(m)]/2+R₀. Le reste est R₀=∫ₗᵐf′(x)B₁({x})dx, avec {x}=x−⌊x⌋ et B₁(u)=u−1/2.

Comme |B₁({x})|≤1/2, |R₀|≤(1/2)∫ₗᵐ|f′|. La formule suppose une somme incluant les deux extrémités. Ajouter des extrémités à une somme qui les exclut changerait les signes; les bornes doivent donc être écrites avant les calculs.

## 32. Corriger n’est pas toujours converger

Au-delà accompagné · Laboratoire `euler_maclaurin`

Pour k≥1 et f de classe C²ᵏ sur [l,m], ajouter Σ_{i=1}^k b₂ᵢ[f^(2i−1)(m)−f^(2i−1)(l)]/(2i)!. Le reste vérifie |Rₖ|≤|b₂ₖ|∫ₗᵐ|f^(2k)|/(2k)!.

Pour un polynôme de degré d, si 2k>d, le reste est nul. Si 2k=d, sa dérivée 2k-ième est constante et l’intégrale de B₂ₖ sur chaque unité est nulle : le reste est encore nul. Pour une fonction générale, les corrections constituent souvent un développement asymptotique; il faut contrôler chaque erreur et ne pas supposer qu’ajouter indéfiniment des termes améliore tout.

## 33. Une substitution avec un point interdit

Sup · Laboratoire `cayley_tangentes`

On cherche les complexes z tels que ((1+z)/(1−z))²ⁿ=1, avec n entier positif et z≠1. Posons w=(1+z)/(1−z). Les candidats sont wₖ=e^(ikπ/n), pour 0≤k<2n.

La résolution de (1+z)=w(1−z) donne z=(w−1)/(w+1). Le candidat w=−1 est impossible : il correspond à k=n. Pour les autres, factoriser e^(ikπ/(2n)) au numérateur et au dénominateur donne **z=i tan(kπ/(2n))**. Les racines sont donc sur l’axe imaginaire.

## 34. Lire une somme et un produit dans les coefficients

Sup / Spé · Laboratoire `cayley_tangentes`

Le polynôme Pₙ(Z)=(Z+1)²ⁿ−(Z−1)²ⁿ est impair. Le binôme donne Pₙ=2Σⱼ impair binom(2n,j)Z^(2n−j). Son degré est 2n−1 et son coefficient dominant 4n.

Sa factorisation est Pₙ=4n∏ₖ≠n(Z−i tan(kπ/(2n))), pour 0≤k<2n. Le coefficient de Z^(2n−2) est nul : la somme des tangentes vaut 0. Le coefficient de Z vaut 4n : le produit des racines non nulles vaut 1. Comme i^(2n−2)=(−1)^(n−1), **∏ₖ₌₁,ₖ≠ₙ²ⁿ⁻¹ tan(kπ/(2n))=(−1)^(n−1)**.

## 35. La somme géométrique fournit les racines

Sup · Laboratoire `geometrique_affine`

Soient c∈ℂ, r>0 et n entier positif. Posons t=(Z−c)/r et Pₙ(Z)=1+t+⋯+tⁿ. L’identité (1−t)Pₙ=1−t^(n+1) montre que les racines correspondent aux racines (n+1)-ièmes de l’unité autres que 1.

Au point t=1, Pₙ=n+1, donc ce point est bien exclu. Ainsi **αₖ=c+r e^(2ikπ/(n+1)), 1≤k≤n**. Chacune est simple : les racines de T^(n+1)−1 sont simples et l’une seulement a été retirée.

## 36. Le cercle ne détermine pas le coefficient dominant

Sup / Spé · Laboratoire `geometrique_affine`

Le terme de plus haut degré de Pₙ=Σⱼ₌₀ⁿ((Z−c)/r)ʲ est r^(−n)Zⁿ. On a donc Pₙ(Z)=r^(−n)∏ₖ₌₁ⁿ(Z−αₖ). Oublier r^(−n) conserve les racines, mais change le polynôme.

Dans le cas c=−1, r=2, Pₙ(0)=2−2^(−n), Pₙ(1)=n+1 et Pₙ(3)=2^(n+1)−1. Viète donne **∏αₖ=(−1)ⁿ(2^(n+1)−1)**. L’évaluation au point 0 contrôle donc le produit des racines.

## 37. Une équation réelle localise les racines complexes

Sup / Spé · Laboratoire `racines_coefficients`

Soit P(Z)=aₙZⁿ+⋯+a₀, avec aₙ≠0 et a₀≠0. Posons Q(r)=rⁿ−Σₖ₌₀ⁿ⁻¹|aₖ/aₙ|rᵏ pour r>0. La fonction h(r)=Q(r)/rⁿ=1−Σ|aₖ/aₙ|/r^(n−k) est strictement croissante, tend vers −∞ en 0 et vers 1 à l’infini.

Elle possède un unique zéro ρ>0. Si P(α)=0, l’inégalité triangulaire donne |α|ⁿ≤Σ|aₖ/aₙ||α|ᵏ, donc h(|α|)≤0 lorsque α≠0. Ainsi **|α|≤ρ**. Une racine nulle vérifie aussi cette borne.

## 38. Une borne inférieure du plus grand module

Spé · Laboratoire `racines_coefficients`

On note α₁,…,αₙ les racines comptées avec multiplicité et M=max|αₖ|. Les relations de Viète donnent |aₖ/aₙ|≤binom(n,k)M^(n−k).

Comme Q(ρ)=0, on obtient ρⁿ≤Σₖ₌₀ⁿ⁻¹binom(n,k)M^(n−k)ρᵏ=(ρ+M)ⁿ−ρⁿ. D’où **(2^(1/n)−1)ρ≤M≤ρ**. Le membre de gauche concerne M, et non chacun des |αₖ|. Les racines numériques illustrent ces inégalités; la preuve n’en dépend pas.

## 39. Rouché : une hypothèse stricte sur tout le bord

Au-delà accompagné · Laboratoire `rouche_disque`

Soient f et g deux polynômes et R>0. Le théorème de Rouché affirme que si |g(z)|<|f(z)| pour tout z tel que |z|=R, alors f et f+g possèdent le même nombre de racines dans |z|<R, comptées avec multiplicité.

Avec P=Z⁵+aZ²+b et f=aZ², on a |g|=|Z⁵+b|≤R⁵+|b|. La condition **|a|R²>R⁵+|b|** est suffisante pour certifier deux racines dans le disque. L’inégalité doit être stricte et valable pour chaque point du cercle.

## 40. Un critère suffisant peut ne pas conclure

Au-delà accompagné · Laboratoire `rouche_disque`

Pour P=Z⁵+aZ²+b, trois comparaisons sont possibles. Si R⁵>|a|R²+|b|, on certifie cinq racines. Si |a|R²>R⁵+|b|, on en certifie deux. Si |b|>R⁵+|a|R², on en certifie zéro.

Lorsque les trois comparaisons échouent, le théorème pourrait encore s’appliquer avec une comparaison plus fine. Le laboratoire affiche alors **« le critère ne conclut pas »**. Il ne transforme jamais l’échec du majorant en une preuve d’absence de racines.

## 41. L’identité qui remplace Rolle dans le plan

Au-delà accompagné · Laboratoire `gauss_lucas`

Écrivons P(Z)=∏ₖ₌₁ⁿ(Z−αₖ), avec les racines comptées autant de fois que leur multiplicité. Pour P(z)≠0, la dérivation du produit donne P′(z)/P(z)=Σₖ1/(z−αₖ).

Si P′(β)=0 et P(β)≠0, cette somme est nulle. Après conjugaison, Σₖ(β−αₖ)/|β−αₖ|²=0. Ainsi **β=Σₖλₖαₖ**, où λₖ=(1/|β−αₖ|²)/(Σⱼ1/|β−αⱼ|²). Tous les poids sont positifs et leur somme vaut 1.

## 42. L’enveloppe convexe contient les racines de la dérivée

Au-delà accompagné · Laboratoire `gauss_lucas`

Un barycentre à poids positifs appartient à l’enveloppe convexe des points utilisés. L’identité précédente prouve donc le théorème de Gauss–Lucas pour les racines β de P′ qui ne sont pas racines de P. Si P(β)=0, β est lui-même l’un des points αₖ : le résultat est immédiat.

Pour un polynôme réel dont toutes les racines sont réelles, l’enveloppe convexe devient l’intervalle entre les racines extrêmes. Rolle fournit alors une information plus précise d’interlacement. **Gauss–Lucas localise dans le plan; il ne fournit pas un ordre entre points complexes.**

## 43. Conjuguer puis retourner les coefficients

Sup / Spé · Laboratoire `reciproque_conjugue`

Soit P(Z)=Σₖ₌₀ⁿaₖZᵏ de degré n. Son réciproque conjugué est P*(Z)=Σₖ₌₀ⁿconj(aₙ₋ₖ)Zᵏ. Pour z≠0, **P*(z)=zⁿconj(P(1/conj(z)))**.

Si α≠0 est racine, 1/conj(α) est racine de P*, avec la même multiplicité. Pour α=ρe^(iθ), l’image est ρ^(−1)e^(iθ) : le module s’inverse et l’argument reste le même. Les points du cercle unité sont fixes.

## 44. Une racine nulle change le degré effectif

Spé · Laboratoire `reciproque_conjugue`

Si le terme constant de P est non nul, P* garde le degré n et un second réciproque conjugué retrouve P. Si P=ZᵐQ avec Q(0)≠0, le degré effectif de P* vaut n−m : les m racines nulles n’ont pas d’image finie.

Le double retournement avec le même degré ambiant n retrouve toujours le vecteur de coefficients initial. Mais, si l’on utilise le degré effectif n−m au second retournement, on obtient Q=P/Zᵐ. **Préciser le degré est indispensable pour parler d’involution en présence d’une racine nulle.**

## 45. Les premières identités de Newton

Sup / Spé · Laboratoire `viete_newton`

Soit P(Z)=Zⁿ+c₁Z^(n−1)+⋯+cₙ, de racines α₁,…,αₙ avec multiplicité. On définit sₖ=Σαⱼᵏ. Pour 1≤k≤n, **sₖ+c₁sₖ₋₁+⋯+cₖ₋₁s₁+kcₖ=0**.

Les premières sont s₁=−c₁, s₂=−c₁s₁−2c₂ et s₃=−c₁s₂−c₂s₁−3c₃. Dans le laboratoire, c₁=c₃=0 : s₁=s₃=0 et s₂=−2a. Les coefficients complexes ne changent aucune de ces identités.

## 46. Après le degré : une récurrence et un lien aux traces

Spé · Laboratoire `viete_newton`

Pour k>n, chaque racine satisfait αⱼⁿ+c₁αⱼ^(n−1)+⋯+cₙ=0. Multiplier par αⱼ^(k−n) puis sommer donne **sₖ+c₁sₖ₋₁+⋯+cₙsₖ₋ₙ=0**. Le terme kcₖ des premières identités disparaît : il n’existe pas de coefficient cₖ au-delà du degré.

Si A est un endomorphisme complexe dont le polynôme caractéristique est P, alors tr(Aᵏ)=sₖ et det(A)=∏αⱼ. Ces relations permettent de relier traces et coefficients caractéristiques; elles restent vraies sans supposer A diagonalisable.

## 47. Pourquoi une racine simple attire localement

Spé / prolongement complexe · Laboratoire `newton_bassins`

Soit α une racine simple de P : P(α)=0 et P′(α)≠0. Pour z proche de α, poser e=z−α. Le développement polynomial donne P(z)=P′(α)e+P″(α)e²/2+O(e³).

Dans la récurrence zₖ₊₁=zₖ−P(zₖ)/P′(zₖ), l’erreur satisfait **eₖ₊₁=[P″(α)/(2P′(α))]eₖ²+O(eₖ³)**. La convergence est donc au moins quadratique pour un point de départ suffisamment proche. Cette conclusion locale ne promet pas la convergence depuis chaque point du plan.

## 48. Le dessin possède une catégorie non classée

Au-delà accompagné · Laboratoire `newton_bassins`

La carte choisit un point initial par pixel et effectue au plus N itérations. Un point reçoit la couleur de αⱼ seulement si sa distance à cette racine devient inférieure à 10⁻⁶. Les autres points restent « non classés ».

Un point non classé peut converger plus lentement, partir très loin ou rencontrer P′=0. Augmenter N peut changer son classement. Le maillage donne une expérience numérique : **il ne démontre ni la frontière exacte des bassins ni la convergence pour tous les points**.

## 49. L’échelle qui contrôle le premier ordre

Spé · Laboratoire `conditionnement_racines`

Soient c∈ℂ, δ>0 et η une petite perturbation complexe. Les racines de (Z−c)²−δ²−η sont c±√(δ²+η). Lorsque |η|≪δ², choisir la branche proche de δ donne √(δ²+η)=δ+η/(2δ)+O(|η|²/δ³).

Le déplacement de chaque racine a donc pour module environ |η|/(2δ). Le coefficient 1/(2δ) augmente lorsque les racines se rapprochent. **La petite quantité pertinente est |η|/δ²**, et non seulement |η|.

## 50. Une racine double ne répond plus linéairement

Spé / prolongement numérique · Laboratoire `conditionnement_racines`

Si δ=0, le facteur devient (Z−c)²−η. Ses racines sont c±√η, à distance exactement √|η| de c. Une perturbation de taille 10⁻⁸ provoque donc un déplacement de taille 10⁻⁴.

Le laboratoire multiplie ce facteur par un polynôme Q de degré 3 à racines fixes : l’ensemble reste un exemple de degré 5 à coefficients complexes. La formule quadratique donne une référence exacte pour mesurer l’erreur du calcul flottant. **Un résidu petit ne suffit pas à certifier une position très précise près d’une racine multiple.**

## 51. Résoudre à un point complexe fixé

Sup / Spé · Laboratoire `recurrence_complexe`

La famille est P₀=1, P₁=2λZ, Pₖ₊₂+λZPₖ₊₁+Pₖ=0. Au point z, posons t=λz et uₖ=Pₖ(z). La suite satisfait uₖ₊₂+tuₖ₊₁+uₖ=0, avec u₀=1 et u₁=2t.

Si r₊ et r₋ sont distincts, racines de r²+tr+1=0, on obtient **uₙ=Ar₊ⁿ+Br₋ⁿ**, avec A=(2t−r₋)/(r₊−r₋), B=1−A. Les racines caractéristiques ne sont pas les racines du polynôme Pₙ : elles dépendent du point d’évaluation z.

## 52. Le cas double et les coefficients complexes

Sup / Spé · Laboratoire `recurrence_complexe`

Lorsque t=±2, l’équation caractéristique a une racine double r=−t/2. La forme générale est uₙ=(A+Bn)rⁿ. Les conditions u₀=1 et u₁=2t donnent A=1 et B=−5 : **uₙ=(1−5n)rⁿ**.

Si Pₙ,₁ désigne la famille source avec λ=1, la récurrence montre Pₙ,λ(Z)=Pₙ,₁(λZ). Les racines tournent donc de l’angle −arg(λ). Dès que λ n’est pas réel, les coefficients peuvent devenir non réels. Cette famille n’est pas celle des Tchebychev usuels : ses données initiales et son signe de récurrence sont différents.

## 53. Trois notions de degré à séparer

Sup · bases algébriques · Laboratoire `monomes_newton`

Pour un polynôme P(x,y)=∑aᵢⱼxⁱyʲ non nul, x et y sont des indéterminées et aᵢⱼ ses coefficients. Un monôme xⁱyʲ a degré total i+j. Le degré total de P est le plus grand i+j avec aᵢⱼ≠0.

Le degré en x est le plus grand i ; celui en y est le plus grand j. Ainsi x⁴+x²y³+y⁴+1 a degré total 5 et degrés partiels 4 et 4. Leur somme, 8, n’est pas le degré total. En considérant P comme un polynôme en x à coefficients dans ℝ[y], on retrouve le degré partiel en x.

## 54. Support et spécialisation : ce que le dessin permet

Spé · prolongement guidé · Laboratoire `monomes_newton`

Le support de P est l’ensemble des exposants (i,j) portant un coefficient non nul. Son enveloppe convexe est le polygone de Newton. Le dessin distingue les monômes extrêmes des monômes intérieurs, sans représenter la courbe réelle P(x,y)=0.

Spécialiser y=y₀ remplace une indéterminée par un nombre. Cette opération peut créer des compensations : P(x,y)=(y−1)x³+x² a degré 3 en x, alors que P(x,1)=x². Les degrés calculés avant et après spécialisation ont donc des significations différentes. Les théorèmes de Newton sur les racines et les intersections exigent des hypothèses supplémentaires.

## 55. Éliminer une variable avant de dessiner

Sup · résolution · Laboratoire `intersection_bezout`

Le cercle x²+y²=r² et la parabole y=x²−h dépendent de r>0 et h réels. Substituer la seconde équation dans la première donne Q(x)=x⁴+(1−2h)x²+h²−r²=0.

Avec t=x², on résout t²+(1−2h)t+h²−r²=0, de discriminant D=1−4h+4r². Pour obtenir des points réels, t doit être réel et non négatif. Si t>0, il donne deux abscisses ±√t ; si t=0, il n’en donne qu’une. Si t est négatif ou non réel, ses racines carrées appartiennent à ℂ et restent pertinentes pour le comptage algébrique.

## 56. Bézout : compter au bon endroit et avec multiplicité

Au-delà · géométrie algébrique · Laboratoire `intersection_bezout`

Deux courbes projectives complexes de degrés d et e sans composante commune ont d×e intersections, comptées avec multiplicité. Le mot « projectives » inclut les points à l’infini ; le mot « complexes » inclut ceux que le dessin réel ne montre pas.

Ici, les équations homogènes sont X²+Y²−r²Z²=0 et YZ−X²+hZ²=0. À Z=0, la seconde impose X=0, puis la première Y=0 : aucun triplet projectif non nul n’est solution. Toutes les intersections sont donc affines. Comme y est imposé par x, on peut les compter par le quartique Q. À r=h=1/2, Q=x⁴ : un seul point (0,−1/2) porte la multiplicité quatre.

## 57. Un déterminant qui élimine y

Spé · déterminants · Laboratoire `resultant_elimination`

Pour F=A(x)y+B(x) et G=C(x)y+D(x), le résultant en y est R(x)=A(x)D(x)−B(x)C(x). Tout point commun (x₀,y₀) annule ce déterminant, car les deux lignes ont un même vecteur (y₀,1) dans leur noyau.

Dans le laboratoire, A=C=x−a, B=−1 et D=−b(x−a). Ainsi R=(x−a)[1−b(x−a)]. Si b≠0, les abscisses candidates sont x=a et x=a+1/b. Le second candidat fournit y=b et une véritable solution ; le premier exige une vérification séparée.

## 58. Le candidat parasite vient d’une chute de degré

Spé / Au-delà · vigilance algébrique · Laboratoire `resultant_elimination`

À x=a, les coefficients de y dans F et G s’annulent. Les équations spécialisées deviennent F=−1 et G=0 : aucun y ne peut satisfaire F=0. Pourtant R(a)=0. Le déterminant détecte la singularité des coefficients, mais cette singularité n’est pas ici un point affine commun.

Pour b=0, G=(x−a)y. Sur F=0, on a (x−a)y=1, donc G=1≠0. Le système n’a aucune solution affine, alors que R=x−a possède un zéro. La règle pratique est de conserver les zéros du résultant comme candidats, puis de revenir aux équations initiales. Cette précaution est aussi essentielle lorsqu’on divise une équation par une expression qui peut s’annuler.

## 59. L’ordre lexicographique expose une substitution

Au-delà · division accompagnée · Laboratoire `groebner_ordre`

Un idéal I=(F,G) est l’ensemble des AF+BG, où A,B sont des polynômes. Pour F=xy−1 et G=y²−x−c, on pose g₁=x−y²+c=−G et g₂=y³−cy−1=yG+F.

Réciproquement, G=−g₁ et F=g₂+yg₁. Les deux familles engendrent donc exactement le même idéal. Avec l’ordre lexicographique x avant y, les termes dominants sont x et y³. Les solutions se calculent par g₂(y)=0 puis x=y²−c. Les monômes non divisibles par x ou y³ sont 1,y,y² : ils donnent une base du quotient, de dimension 3.

## 60. Trois divisions au lieu de deux : le critère qui certifie

Au-delà · certificats · Laboratoire `groebner_ordre`

Avec un ordre qui compare d’abord le degré total, la base devient H=x²+cx−y, F=xy−1 et G=y²−x−c. L’identité H=yF−xG prouve que ce nouvel élément appartient au même idéal. Les termes dominants sont x²,xy,y².

Un S-polynôme multiplie deux éléments pour rendre leurs termes dominants identiques, puis les soustrait. Le critère de Buchberger affirme qu’une famille est une base de Gröbner lorsque tous ces S-polynômes ont un reste nul par division dans la famille. Le laboratoire affiche ces restes exacts. Les monômes restants sont alors 1,x,y : une autre base du même quotient de dimension 3.

## 61. Newton retrouve les puissances à partir des coefficients

Sup / Spé · identités · Laboratoire `symetriques`

Pour trois nombres u,v,w, on définit e₁=u+v+w, e₂=uv+uw+vw, e₃=uvw et pₖ=uᵏ+vᵏ+wᵏ. Le polynôme associé est P(T)=T³−e₁T²+e₂T−e₃.

Les premières identités sont p₁=e₁, p₂=e₁p₁−2e₂ et p₃=e₁p₂−e₂p₁+3e₃. Chaque racine α vérifie α³=e₁α²−e₂α+e₃. Multiplier par αᵏ⁻³ puis sommer donne, pour k≥4, pₖ=e₁pₖ₋₁−e₂pₖ₋₂+e₃pₖ₋₃. On calcule donc les grandes puissances sans expliciter les racines d’une équation cubique.

## 62. Le discriminant décrit les collisions de racines

Spé · racines multiples · Laboratoire `symetriques`

Le discriminant de P(T)=T³−e₁T²+e₂T−e₃ est D=e₁²e₂²−4e₂³−4e₁³e₃−27e₃²+18e₁e₂e₃. Si u,v,w sont ses racines, D=(u−v)²(u−w)²(v−w)². D=0 équivaut donc à une racine multiple.

Pour des coefficients réels, D>0 correspond à trois racines réelles distinctes et D<0 à une racine réelle et deux racines complexes conjuguées. À e₁ fixé, la courbe D(e₂,e₃)=0 sépare ces régions dans le plan des coefficients. Le point du laboratoire reste du côté D≥0, car les trois racines réglées sont réelles. Ce choix ne limite pas la validité des identités algébriques.

## 63. Le gradient seul ne classe pas une singularité

Spé · calcul différentiel · Laboratoire `singularites`

La courbe Fₜ(x,y)=y²−x³−tx²=0 a gradient (−3x²−2tx,2y). Une singularité vérifie Fₜ=0 et ∇Fₜ=0. L’origine est toujours singulière.

Le gradient propose aussi (−2t/3,0), mais Fₜ en ce point vaut −4t³/27 : il n’est sur la courbe que pour t=0, où il coïncide avec l’origine. Il est donc essentiel de vérifier l’équation de la courbe. La hessienne à l’origine est diag(−2t,2) ; son déterminant −4t distingue les signatures quadratiques, sans décrire à lui seul le cas dégénéré t=0.

## 64. Trois signes, trois dessins

Spé / Au-delà · géométrie locale · Laboratoire `singularites`

Pour t>0, y²−tx²=(y−√t x)(y+√t x) : deux tangentes réelles distinctes passent par l’origine, qui est un nœud. Pour t=0, y²=x³ impose x≥0 et y=±x³ᐟ² : la pointe a une tangente double y=0.

Pour t<0, l’équation y²=x²(x+t) ne possède aucune solution avec 0<|x|<|t|. L’origine est donc isolée dans la courbe réelle, même si une branche existe plus loin pour x≥|t|. Le terme quadratique y²+|t|x² est positif hors de l’origine. Cette preuve de signe est plus sûre qu’un zoom sur une image.

## 65. Tous les monômes doivent avoir le même degré

Sup / Au-delà · coordonnées · Laboratoire `homogenisation`

Pour homogénéiser un polynôme affine de degré d, on remplace x,y par X,Y puis on multiplie chaque monôme de degré k par Zᵈ⁻ᵏ. Ainsi y−x²−c devient YZ−X²−cZ², de degré homogène 2.

Un point projectif [X:Y:Z] est un triplet non nul considéré à multiplication commune près. Dans la carte Z≠0, on peut normaliser Z=1 et retrouver les coordonnées x=X/Z,y=Y/Z. Les points Z=0 sont à l’infini de cette carte. Pour la parabole, Z=0 impose X=0, donnant l’unique point [0:1:0]. Aucun symbole ∞ n’est utilisé comme un nombre.

## 66. Une deuxième carte explique le point à l’infini

Au-delà · géométrie projective · Laboratoire `homogenisation`

Dans la carte Y≠0, on pose u=X/Y et v=Z/Y, donc on peut normaliser Y=1. La parabole homogène devient v−u²−cv²=0. Son point [0:1:0] est maintenant représenté par (u,v)=(0,0). La droite v=0 est la droite à l’infini de l’ancienne carte Z≠0.

Pour l’hyperbole xy=c, l’équation homogène XY−cZ²=0 possède à Z=0 les deux points [1:0:0] et [0:1:0]. Dans la carte Y≠0, l’équation est u−cv²=0 et seul le second point est visible. Il faut la carte X≠0 pour voir le premier : cela évite de prendre une carte pour tout le plan projectif.

## 67. La matrice symétrique et ses valeurs propres

Spé · théorème spectral · Laboratoire `formes_quadratiques`

Pour v=(x,y,z), la forme Q=x²+y²+bz²+2axy+2cyz s’écrit vᵀAv avec A=[[1,a,0],[a,1,c],[0,c,b]]. Les termes croisés sont doublés parce que les deux positions symétriques de A contribuent.

Le théorème spectral donne une base orthonormée dans laquelle Q=λ₁u₁²+λ₂u₂²+λ₃u₃². Toutes les valeurs propres positives signifient Q(v)>0 pour v≠0. Des valeurs de signes opposés rendent Q indéfinie. Des valeurs nulles exigent de distinguer semi-définition et indéfinition. Une tranche z=z₀ peut représenter des niveaux fermés même lorsqu’une autre direction de ℝ³ est négative.

## 68. Sylvester et complétion des carrés

Spé · complément formateur · Laboratoire `formes_quadratiques`

Les mineurs principaux successifs sont Δ₁=1, Δ₂=1−a² et Δ₃=b(1−a²)−c². Le critère de Sylvester affirme que A est définie positive si et seulement si Δ₁,Δ₂,Δ₃ sont strictement positifs.

On peut vérifier le critère dans cette famille sans le supposer : Q=(x+ay)²+(1−a²)y²+2cyz+bz². Si 1−a²>0, compléter encore donne Q=(x+ay)²+(1−a²)(y+cz/(1−a²))²+[b−c²/(1−a²)]z². Les trois carrés ont des coefficients strictement positifs exactement lorsque Δ₂>0 et Δ₃>0. Au bord Δ₂=0, cette écriture divisant par Δ₂ n’est plus valable.

## 69. Un minimum global démontré sur tout ℝ²

Sup / Spé · inégalités · Laboratoire `positivite_motzkin`

Pour Mλ=x⁴y²+x²y⁴−λx²y²+1, poser t=|xy|≥0. L’inégalité arithmético-géométrique donne x⁴y²+x²y⁴≥2t³. Ainsi Mλ≥2t³−λt²+1, avec égalité lorsque |x|=|y|.

Pour λ≥0, la dérivée de cette dernière fonction est 2t(3t−λ). Son minimum sur t≥0 vaut 1−λ³/27, atteint en t=λ/3. Lorsque λ>0, les quatre points x,y=±√(λ/3) réalisent l’égalité. Le polynôme est donc non négatif pour 0≤λ≤3, strictement positif pour 0≤λ<3, et possède des valeurs négatives pour λ>3. À λ=3, ses seuls zéros sont (±1,±1).

## 70. Le coefficient négatif interdit toute somme de carrés

Au-delà · contre-exemple de Motzkin · Laboratoire `positivite_motzkin`

À λ=0, M₀=(x²y)²+(xy²)²+1². Pour λ>0, supposons Mλ=∑qᵢ². La partie homogène dominante d’une somme de carrés ne peut se compenser, donc chaque qᵢ a degré au plus 3.

Le coefficient nul de x⁶ impose l’absence de x³ dans chaque qᵢ ; celui de y⁶ impose l’absence de y³. Les coefficients nuls de x⁴,y⁴ imposent ensuite l’absence de x²,y², puis ceux de x²,y² l’absence de x,y. Il reste qᵢ=Aᵢ+Bᵢxy+Cᵢx²y+Dᵢxy². Le coefficient de x²y² dans ∑qᵢ² serait ∑Bᵢ²≥0, mais il vaut −λ. Contradiction. Pour 0<λ≤3, on dispose donc d’un polynôme non négatif qui n’est pas une somme de carrés de polynômes réels.

## 71. Le cercle rend les deux méthodes équivalentes

Spé · optimisation · Laboratoire `lagrange_contrainte`

Sur g(x,y)=x²+y²−r²=0 avec r>0, ∇g=2(x,y) ne s’annule pas. Tout extremum contraint de f=x⁴+y⁴+axy satisfait ∇f=μ∇g. Cette condition est nécessaire, mais il faut encore classer ou comparer les candidats.

Le paramétrage x=r cosθ,y=r sinθ ramène f à une fonction périodique. Sa dérivée est r²cos(2θ)[a−2r²sin(2θ)]. Les directions diagonales cos(2θ)=0 donnent toujours quatre candidats. La seconde famille sin(2θ)=a/(2r²) existe seulement pour |a|≤2r² ; elle donne quatre candidats distincts si l’inégalité est stricte. À l’égalité, elle rejoint deux des diagonales.

## 72. Une parabole donne les bornes globales

Sup / Spé · preuve par substitution · Laboratoire `lagrange_contrainte`

Poser s=sin(2θ)∈[−1,1]. Les identités cos⁴θ+sin⁴θ=1−s²/2 et cosθsinθ=s/2 donnent f=r⁴(1−s²/2)+(ar²/2)s. Cette fonction est une parabole concave de s.

Son minimum sur [−1,1] est donc à une extrémité : min f=r⁴/2−|a|r²/2. Son sommet est à s=a/(2r²). Si |a|≤2r², max f=r⁴+a²/8 ; sinon le maximum est à l’extrémité de même signe que a et vaut r⁴/2+|a|r²/2. Ces formules comparent tous les candidats d’un seul coup. Au seuil, la dérivée seconde peut s’annuler : un développement d’ordre 4 ou la concavité en s permet encore de classer l’extremum.
