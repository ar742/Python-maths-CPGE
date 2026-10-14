"""Buts, méthodes et preuves accompagnées pour les expériences arithmétiques."""
GUIDES={}
LESSONS=[]
EXERCISES=[]
def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=first_steps,expected=expected)
def lesson(id_,title,level,html): LESSONS.append(dict(lab=id_,title=title,level=level,html=html))
def exercise(id_,title,level,question,answer): EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('euclide_bezout','Obtenir un PGCD et savoir le justifier par des divisions puis par une identité de Bézout.',
    ['X est l’indéterminée; x est une valeur réelle utilisée uniquement dans les dessins.', 'A et B sont les polynômes de départ; t translate X en X−t, et c multiplie A.', 'Q et R sont le quotient et le reste d’une division A=BQ+R. D est le PGCD unitaire, U et V ses coefficients de Bézout : AU+BV=D.', 'Les degrés sont des entiers; le degré du polynôme nul vaut −∞ et n’est pas dessiné.'],
    ['Coefficients rationnels, diviseurs non nuls.', 'Les égalités du tableau sont exactes, même si leurs dessins sont numériques.'],
    ['Division euclidienne','Descente des degrés','Normalisation du PGCD','Remontée de l’algorithme'],
    'Division des polynômes, divisibilité, PGCD et Bézout.', 'Applications aux congruences et aux fractions rationnelles.', 'Algorithmes efficaces et calculs dans d’autres corps.',
    ['Choisir le facteur quadratique commun et prévoir le PGCD.', 'Lire la première division, puis vérifier son reste par multiplication.', 'Choisir le TP X⁴ : retrouver le reste par ses valeurs en 1, 2 et 3.'],
    'Le dernier reste non nul donne le PGCD après normalisation; le certificat AU+BV=D est vérifiable sans faire confiance à l’algorithme.')
lesson('euclide_bezout','Pourquoi la division termine','Sup',
    '<p>A et B sont deux polynômes sur un corps K, avec B≠0. La division écrit A=BQ+R avec R=0 ou deg R&lt;deg B. Un diviseur commun de A et B divise aussi R=A−BQ; réciproquement, un diviseur de B et R divise A.</p><p>Ainsi PGCD(A,B)=PGCD(B,R). Les degrés des restes non nuls diminuent strictement : l’algorithme termine. Le dernier reste peut avoir un coefficient dominant différent de 1; on le divise par ce coefficient pour obtenir <strong>le PGCD unitaire</strong>.</p>')
lesson('euclide_bezout','Deux certificats pour un même reste','Sup / spé',
    '<p>U et V sont les polynômes obtenus en remontant les divisions : AU+BV=D, où D est le PGCD unitaire. Cette identité prouve que tout diviseur commun divise D. Pour vérifier complètement le résultat, on contrôle aussi D|A et D|B.</p><p>Dans le TP, A=X⁴ et B=(X−1)(X−2)(X−3). Le reste R a degré au plus 2 et vérifie R(1)=1, R(2)=16, R(3)=81. On trouve R=25X²−60X+36 et Q=X+6. L’interpolation et la division conduisent au même certificat : X⁴=(X+6)B+R.</p>')
exercise('euclide_bezout','Un reste sans division longue','Sup',
    '<p>Calculer le reste de X⁴ modulo (X−1)(X−2)(X−3) en utilisant les trois racines du diviseur.</p>',
    '<p>Écrire R=αX²+βX+γ. Les valeurs 1,16,81 donnent α=25, β=−60, γ=36. Le quotient est X+6; la multiplication vérifie l’identité.</p>')
exercise('euclide_bezout','Composition et congruence','Sup',
    '<p>Dans ℚ[X], poser P=X²+2X−1 et B=P−X. Montrer B|P(P(X))−X, puis calculer le reste de A=X⁴+5X³+5X²−X−2 modulo B.</p>',
    '<p>Modulo B, P(X)≡X, donc P(P(X))≡P(X)≡X. Le développement donne P(P(X))−X=X⁴+4X³+4X²−X−2. A en diffère de X³+X². Avec X²≡1−X, on a X³+X²≡X. Le reste est X.</p>')
exercise('euclide_bezout','Reconnaître le rôle du coefficient dominant','Sup',
    '<p>A=2(X²+1)(X³−2X+1), B=3(X²+1)(X²+X+2). Leurs facteurs cubique et quadratique sont premiers entre eux. Donner PGCD(A,B) et expliquer pourquoi 6(X²+1) n’est pas le PGCD retenu.</p>',
    '<p>Dans ℚ[X], les constantes non nulles sont inversibles. Le facteur commun maximal est X²+1; le PGCD est choisi unitaire. 6(X²+1) est un autre générateur du même idéal, mais son coefficient dominant vaut 6.</p>')

guide('gauss_eisenstein','Distinguer divisibilité, contenu entier et critère d’irréductibilité, puis éviter un raisonnement fondé seulement sur les racines.',
    ['A et B ont des coefficients entiers. c(A) est le PGCD positif de ces coefficients; A/c(A) est sa partie primitive.', 'n est le degré de la famille d’Eisenstein, p un nombre premier et t une translation entière. c multiplie le polynôme primitif.', 'La famille est (X−t)ⁿ+p(X−t)+p. La substitution X→X+t fait apparaître les coefficients du critère.', 'Les réglages n, p et t concernent la famille d’Eisenstein; c agit dans les trois exemples.'],
    ['Coefficients entiers pour le contenu; irréductibilité recherchée sur ℚ.', 'Un critère suffisant qui échoue ne prouve pas la réductibilité.'],
    ['Lemme de Gauss','Réduction modulo un nombre premier','Critère d’Eisenstein','Changement d’indéterminée'],
    'Divisibilité, racines et factorisation dans ℚ[X].', 'Arguments de réduction et de changement de variable dans un exercice guidé.', 'Irréductibilité et anneaux factoriels.',
    ['Avec c=3, vérifier c(AB)=c(A)c(B).', 'Translater l’exemple d’Eisenstein et lire les coefficients modulo p.', 'Choisir X⁴+4 : factoriser avant de conclure à partir des racines.'],
    'Le contenu ne change pas les facteurs non constants sur ℚ. Une preuve d’irréductibilité exige plus que l’absence de racines en degré 4.')
lesson('gauss_eisenstein','Deux énoncés portant le nom de Gauss','Sup / prolongement',
    '<p>A, B et C sont des polynômes sur un corps K. Le <strong>théorème de Gauss de divisibilité</strong> dit : si PGCD(A,B)=1 et A|BC, alors A|C. Bézout fournit AU+BV=1; multiplier par C permet de conclure.</p><p>Pour un polynôme entier non nul P, son contenu c(P) est le PGCD positif de ses coefficients. Le <strong>lemme de Gauss sur le contenu</strong> donne c(PQ)=c(P)c(Q). Un produit de polynômes primitifs est donc primitif. Il relie les factorisations de ℤ[X] et de ℚ[X]. Ces deux énoncés ne portent pas sur les mêmes objets.</p>')
lesson('gauss_eisenstein','Ce qui constitue une preuve d’irréductibilité','Au-delà accompagné',
    '<p>P=aₙXⁿ+⋯+a₀ est un polynôme entier primitif. Pour un nombre premier p, Eisenstein exige p∤aₙ, p|aₖ pour k&lt;n et p²∤a₀. Ces conditions impliquent l’irréductibilité sur ℚ. Elles peuvent devenir visibles après la substitution X→X+t, qui conserve la possibilité d’une factorisation.</p><p>La réduction modulo p fournit un autre certificat si elle conserve le degré et devient irréductible sur Fₚ. Pour X⁴+X+1 sur F₂, aucun facteur linéaire n’existe; le seul quadratique unitaire irréductible X²+X+1 ne le divise pas. À l’inverse, X⁴+4 est sans racine réelle mais se factorise en deux quadratiques.</p>')
exercise('gauss_eisenstein','Gauss par Bézout','Sup',
    '<p>Dans K[X], supposer A|BC et AU+BV=1. Prouver A|C sans invoquer une factorisation de B.</p>',
    '<p>Multiplier l’identité par C : C=AUC+BVC. A divise AUC; il divise BVC puisque A|BC. Il divise donc leur somme C.</p>')
exercise('gauss_eisenstein','Un Eisenstein caché','Au-delà accompagné',
    '<p>P=(X−1)⁵+3(X−1)+3. Prouver P irréductible sur ℚ.</p>',
    '<p>P(X+1)=X⁵+3X+3. Pour p=3, le coefficient dominant n’est pas divisible par 3, tous les autres le sont, et 9 ne divise pas le terme constant 3. Eisenstein s’applique. Une factorisation de P donnerait une factorisation de P(X+1), donc P est irréductible.</p>')
exercise('gauss_eisenstein','L’absence de racines n’est pas un certificat','Sup',
    '<p>Le polynôme X⁴+4 a-t-il une racine rationnelle ? Est-il irréductible sur ℚ ?</p>',
    '<p>Pour tout réel x, x⁴+4&gt;0, donc aucune racine rationnelle. Pourtant X⁴+4=(X²−2X+2)(X²+2X+2). L’absence de racines suffit pour les degrés 2 et 3, mais pas pour le degré 4.</p>')

guide('inverse_quotient','Transformer Bézout en un inverse calculable et repérer ce qui bloque l’inversion.',
    ['K est le corps choisi : ℚ ou Fₚ, où p est premier. M est le polynôme imposant la relation M(X)=0 dans le quotient.', 'A=X²+aX+b est l’élément à inverser; a et b sont des coefficients entiers réduits modulo p sur Fₚ.', 'La classe de P regroupe tous les polynômes P+MQ. Elle possède un représentant de degré inférieur à deg M.', 'U et V sont les coefficients de Bézout; D=PGCD(A,M). Les quatre coordonnées suivent la base 1,X,X²,X³.'],
    ['M est unitaire de degré 4.', 'Les hauteurs des résidus sur Fₚ sont des codes d’affichage entiers; elles n’ont pas la signification d’une distance dans le corps.'],
    ['Bézout','Reste de division','Matrice de multiplication','Diviseur de zéro'],
    'Bézout et calculs de restes.', 'Algèbre linéaire : multiplication par une classe comme endomorphisme.', 'Algèbres quotient et construction de corps finis.',
    ['Trouver l’inverse rationnel par le tableau et vérifier le produit modulo M.', 'Choisir M=(X²+1)(X²+X+1) et A=X²+1.', 'Passer sur F₂ et refaire la division avec des coefficients réduits.'],
    'Une classe est inversible exactement lorsque A et M sont premiers entre eux. Un facteur commun fournit un élément non nul annulé par A.')
lesson('inverse_quotient','La relation M(X)=0 réduit les calculs','Spé / prolongement',
    '<p>K est un corps et M un polynôme unitaire de degré m≥1. Dans K[X]/(M), deux polynômes représentent la même classe si leur différence est divisible par M. La division euclidienne donne un représentant unique de degré inférieur à m.</p><p>Les classes de 1,X,…,Xᵐ⁻¹ forment une base : le quotient est une K-algèbre de dimension m. Multiplier par la classe de A est un endomorphisme; les restes de AXʲ donnent les colonnes de sa matrice. On conserve ici cette dimension même si M est réductible.</p>')
lesson('inverse_quotient','L’inverse et le diviseur de zéro viennent du même PGCD','Au-delà accompagné',
    '<p>A est un polynôme et D=PGCD(A,M). Si D=1, Bézout donne AU+MV=1 : la classe de U est l’inverse de celle de A. Réciproquement, un inverse modulo M donne une telle identité, donc D=1.</p><p>Si D a un degré positif, écrire A=DA₁ et M=DM₁. Alors AM₁=A₁M≡0 modulo M, tandis que la classe de M₁ est non nulle car son degré est inférieur à celui de M. Cela donne un témoin concret de non-inversibilité. Le quotient est un corps exactement lorsque M est irréductible.</p>')
exercise('inverse_quotient','Un inverse sans factoriser','Sup / prolongement',
    '<p>Dans ℚ[X]/(X³−2), calculer l’inverse de la classe de X.</p>',
    '<p>X×(X²/2)=X³/2≡1. L’inverse est la classe de X²/2; l’identité exacte est X(X²/2)−(X³−2)/2=1.</p>')
exercise('inverse_quotient','Un diviseur de zéro non nul','Spé / prolongement',
    '<p>M=(X²+1)(X²+X+1). Dans ℚ[X]/(M), montrer que la classe de X²+1 est non nulle et non inversible.</p>',
    '<p>Son degré 2 est inférieur à deg M=4, donc sa classe est non nulle. Son produit par la classe non nulle de X²+X+1 est nul. Un élément inversible ne peut annuler un élément non nul.</p>')
exercise('inverse_quotient','Quatre coefficients, seize éléments','Au-delà accompagné',
    '<p>M=X⁴+X+1 est irréductible sur F₂. Combien d’éléments possède F₂[X]/(M) ? Combien sont inversibles ?</p>',
    '<p>Chaque représentant a quatre coefficients indépendants, valant 0 ou 1 : 2⁴=16 éléments. L’irréductibilité fait du quotient un corps; ses 15 éléments non nuls sont tous inversibles.</p>')

guide('restes_chinois','Remplacer deux congruences par un seul polynôme et comprendre la condition de compatibilité.',
    ['M₁ et M₂ sont les modules polynomiaux. R₁ et R₂ sont les restes prescrits, réglés par les entiers a et b.', 'S est la solution recherchée. S≡Rᵢ modulo Mᵢ signifie Mᵢ|S−Rᵢ.', 'D=PGCD(M₁,M₂) et L=PPCM(M₁,M₂). E₁ et E₂ sont les idempotents lorsque D=1.', 'Un idempotent E vérifie E²≡E modulo L : il sélectionne une des deux conditions.'],
    ['Coefficients rationnels.', 'Pour des modules non premiers entre eux, on teste la compatibilité modulo D avant de chercher S.'],
    ['Bézout','Congruence polynomiale','Inversion modulaire','Idempotents'],
    'Divisibilité, Bézout et congruences par analogie avec l’arithmétique.', 'Interpolation, décomposition d’espaces et projecteurs.', 'Théorème des restes chinois pour les anneaux et les algèbres.',
    ['Reconstituer S dans le cas premier entre eux et contrôler ses deux restes.', 'Observer E₁ et E₂; retrouver S≡R₁E₁+R₂E₂.', 'Comparer les deux cas ayant le facteur X−1 en commun et évaluer les restes en 1.'],
    'Le PGCD contrôle l’existence; le PPCM contrôle l’unicité de la classe solution.')
lesson('restes_chinois','Deux congruences, deux projecteurs','Spé / prolongement',
    '<p>M₁ et M₂ sont premiers entre eux dans K[X]. Bézout donne U₁M₁+U₂M₂=1. Poser E₁=U₂M₂ et E₂=U₁M₁, puis travailler modulo L=M₁M₂.</p><p>E₁ vaut 1 modulo M₁ et 0 modulo M₂; E₂ fait l’inverse. La solution S≡R₁E₁+R₂E₂ possède les restes voulus. Elle est unique modulo L : une différence entre deux solutions est divisible par les deux modules, donc par leur produit. E₁+E₂=1, Eᵢ²≡Eᵢ et E₁E₂≡0 expriment le rôle de projecteurs.</p>')
lesson('restes_chinois','Un facteur commun ne rend pas tout impossible','Au-delà accompagné',
    '<p>D=PGCD(M₁,M₂). Si S possède les deux restes R₁,R₂, alors D divise R₂−R₁. Cette condition est aussi suffisante. Écrire S=R₁+M₁W et diviser la deuxième congruence par D.</p><p>On résout (M₁/D)W≡(R₂−R₁)/D modulo M₂/D; les nouveaux modules sont premiers entre eux. L’unicité est modulo L=PPCM(M₁,M₂). Dans le labo, le facteur X−1 impose la même valeur des deux restes en X=1 : une différence de 1 à cet endroit interdit la solution.</p>')
exercise('restes_chinois','Retrouver l’interpolation','Sup',
    '<p>Déterminer le représentant de degré inférieur à 2 vérifiant S≡2 modulo X−1 et S≡5 modulo X−3.</p>',
    '<p>Écrire S=αX+β. Les équations α+β=2 et 3α+β=5 donnent α=3/2, β=1/2. Les solutions sont (3X+1)/2+(X−1)(X−3)Q.</p>')
exercise('restes_chinois','Tester l’obstruction au bon endroit','Spé / prolongement',
    '<p>On impose S≡X modulo (X−1)(X+1) et S≡X+1 modulo (X−1)(X+2). Existe-t-il une solution ?</p>',
    '<p>Le PGCD des modules est X−1. Au point X=1, les restes valent 1 et 2. Leur différence 1 n’est pas divisible par X−1 : aucune solution.</p>')
exercise('restes_chinois','Vérifier un idempotent','Spé / prolongement',
    '<p>Dans ℚ[X]/((X−1)(X+1)), poser E₁=(X+1)/2 et E₂=(1−X)/2. Vérifier les identités de projecteurs.</p>',
    '<p>E₁+E₂=1. E₁²−E₁=(X²−1)/4, E₂²−E₂=(X²−1)/4 et E₁E₂=(1−X²)/4 sont nuls modulo X²−1. E₁ sélectionne la valeur en 1; E₂ celle en −1.</p>')

guide('mobius_diviseurs','Défaire une somme sur les diviseurs, avec une vérification entière terme par terme.',
    ['n est un entier positif et d parcourt ses diviseurs positifs. p désigne un nombre premier dans la définition de μ.', 'μ est la fonction de Möbius : 1 en n=1, 0 si n a un facteur carré, (−1)ʳ si n a r facteurs premiers distincts.', 'g est la fonction choisie; f(n)=Σ_{d|n}g(d). φ(n) compte les entiers entre 1 et n premiers avec n.', 'k n’intervient que dans la famille g(n)=nᵏ. χ est l’unité de la convolution : χ(1)=1, χ(n)=0 pour n>1.'],
    ['Tous les diviseurs sont positifs.', 'Les sommes et les factorisations d’entiers sont exactes.'],
    ['Décomposition en facteurs premiers','Somme sur les diviseurs','Convolution de Dirichlet','Inversion de Möbius'],
    'Divisibilité, PGCD et factorisation des entiers.', 'Réorganisation de sommes finies et preuves par regroupement.', 'Fonctions arithmétiques et formule de Möbius, accompagnées.',
    ['Choisir n=30 et repérer les signes des huit diviseurs.', 'Passer à n=36 : observer l’annulation de μ pour les diviseurs contenant un carré.', 'Choisir g=φ et vérifier que f(n)=n, puis inverser cette identité.'],
    'Les contributions signées éliminent les doubles comptages; la convolution avec μ inverse la somme des diviseurs.')
lesson('mobius_diviseurs','Pourquoi μ annule les carrés','Au-delà accompagné',
    '<p>n≥1 possède r facteurs premiers distincts. Les diviseurs d de n pour lesquels μ(d)≠0 correspondent aux choix de sous-ensembles de ces r nombres premiers. Un sous-ensemble de taille j contribue (−1)ʲ.</p><p>Ainsi Σ_{d|n}μ(d)=(1−1)ʳ. La somme vaut 0 pour n&gt;1 et vaut 1 pour n=1. Pour la convolution (f∗g)(n)=Σ_{d|n}f(d)g(n/d), cela s’écrit μ∗1=χ, où χ(1)=1 et χ(n)=0 sinon. La constante 1 est ici une fonction, pas l’unité de la convolution.</p>')
lesson('mobius_diviseurs','Inverser en réorganisant une somme finie','Spé / au-delà accompagné',
    '<p>Supposer f(n)=Σ_{d|n}g(d). Alors Σ_{d|n}μ(d)f(n/d)=Σ_{de|n}μ(d)g(e). Pour chaque e|n, le coefficient de g(e) est Σ_{d|n/e}μ(d), égal à 1 si e=n et à 0 sinon. Il reste donc g(n).</p><p>Pour φ, on classe les entiers a∈{1,…,n} selon PGCD(a,n). Ce regroupement donne Σ_{d|n}φ(d)=n. L’inversion fournit φ(n)=Σ_{d|n}μ(d)n/d=n∏_{p|n}(1−1/p). Le produit est justifié ici par les sous-ensembles de facteurs premiers.</p>')
exercise('mobius_diviseurs','Une inversion concrète','Au-delà accompagné',
    '<p>Utiliser φ(n)=Σ_{d|n}μ(d)n/d pour calculer φ(30).</p>',
    '<p>Les diviseurs sont 1,2,3,5,6,10,15,30. Les contributions sont 30,−15,−10,−6,5,3,2,−1. La somme vaut 8, en accord avec 30(1−1/2)(1−1/3)(1−1/5).</p>')
exercise('mobius_diviseurs','La constante 1 n’est pas χ','Au-delà accompagné',
    '<p>Noter 1 la fonction constante égale à 1. Calculer (1∗1)(12), puis expliquer pourquoi χ est l’unité de convolution.</p>',
    '<p>(1∗1)(12) compte les diviseurs 1,2,3,4,6,12 : résultat 6. Pour (f∗χ)(n), seul d=n contribue puisque χ(n/d) est nul sauf si n/d=1; on retrouve f(n).</p>')
exercise('mobius_diviseurs','Un carré supprime une contribution','Sup / prolongement',
    '<p>Calculer μ(72), μ(30) et μ(1), puis la somme Σ_{d|72}μ(d).</p>',
    '<p>72=2³3² a des facteurs carrés, donc μ(72)=0. 30=2×3×5 donne μ(30)=−1, et μ(1)=1. Seuls 1,2,3,6 donnent des termes non nuls dans la somme : 1−1−1+1=0.</p>')

guide('irreductibles_fp','Retrouver le nombre d’irréductibles de degré n et vérifier le passage entre nombre de facteurs et nombre de racines.',
    ['p est premier; Fₚ est le corps des p résidus. n est un degré positif.', 'Iₚ(n) est le nombre de polynômes unitaires irréductibles de degré n dans Fₚ[X].', 'μ(d) est la fonction de Möbius et d parcourt les diviseurs positifs de n.', 'Il y a pⁿ polynômes unitaires de degré n, car leurs n coefficients non dominants sont libres.'],
    ['On compte les polynômes unitaires pour éviter de compter plusieurs associés.', 'L’énumération complète est effectuée si pⁿ≤125; au-delà, seul le comptage exact par la formule est affiché.'],
    ['Degrés d’une factorisation','Frobenius','Inversion de Möbius','Contrôle par énumération'],
    'Polynômes unitaires, factorisation et raisonnement sur le degré.', 'Bézout et irréductibilité; réorganisation de sommes.', 'Corps finis et dénombrement de leurs polynômes, accompagnés.',
    ['Prendre p=2,n=2 et vérifier les quatre polynômes candidats.', 'Choisir p=2,n=6; lire les quatre diviseurs de 6 et la somme signée.', 'Prendre p=5,n=2; comparer formule et liste des dix irréductibles.'],
    'Le facteur d dans ΣdIₚ(d) compte les racines de chaque irréductible. Möbius isole le degré recherché.')
lesson('irreductibles_fp','D’abord compter tous les facteurs de Frobenius','Au-delà accompagné',
    '<p>p est premier et n≥1. Le polynôme X^(pⁿ)−X a dérivée −1 sur Fₚ, donc ses facteurs irréductibles sont tous simples. Ses facteurs sont exactement les polynômes unitaires irréductibles dont le degré d divise n.</p><p>Noter Iₚ(d) leur nombre. En comparant les degrés, pⁿ=Σ_{d|n}dIₚ(d). Cette identité porte sur des polynômes et leurs degrés; elle ne signifie pas qu’il existe pⁿ résidus différents modulo p.</p>')
lesson('irreductibles_fp','Une formule entière qui se contrôle','Au-delà accompagné',
    '<p>Appliquer l’inversion de Möbius à f(n)=pⁿ et g(n)=nIₚ(n). On obtient <strong>Iₚ(n)=(1/n)Σ_{d|n}μ(d)p^(n/d)</strong>. Le résultat est un entier car il dénombre des objets.</p><p>Pour p=2,n=6 : 6I₂(6)=2⁶−2³−2²+2=54, donc I₂(6)=9. Le labo énumère ici les 64 polynômes unitaires et teste leur irréductibilité. En degré 2, être réductible équivaut à avoir une racine dans le corps; en degré supérieur, ce test ne suffit plus.</p>')
exercise('irreductibles_fp','Le premier quadratique irréductible','Au-delà accompagné',
    '<p>Énumérer les quatre polynômes unitaires de degré 2 sur F₂ et déterminer les irréductibles.</p>',
    '<p>X², X²+1=(X+1)² et X²+X=X(X+1) sont réductibles. X²+X+1 ne s’annule ni en 0 ni en 1, donc il est irréductible. I₂(2)=(4−2)/2=1.</p>')
exercise('irreductibles_fp','Un degré premier','Au-delà accompagné',
    '<p>Calculer I₃(3), puis expliquer pourquoi le dénominateur 3 intervient.</p>',
    '<p>Les diviseurs de 3 sont 1 et 3. I₃(3)=(3³−3)/3=8. Après avoir retiré les trois racines du corps de base, chaque irréductible cubique apporte trois racines distinctes dans l’extension.</p>')
exercise('irreductibles_fp','Isoler un degré composé','Au-delà accompagné',
    '<p>Calculer 6I₂(6) directement, puis I₂(6). Quelle identité générale utilisera-t-on pour les autres degrés ?</p>',
    '<p>Les diviseurs 1,2,3,6 donnent 64−8−4+2=54, donc I₂(6)=9. L’identité générale est la somme Σ_{d|n}μ(d)p^(n/d), dont les exposants n/d varient avec chaque diviseur.</p>')

guide('frobenius_fp','Relier une factorisation exacte, une dérivée constante et la construction d’un corps fini.',
    ['p est premier, n≥1 et P=X^(pⁿ)−X appartient à Fₚ[X].', 'Fₚ désigne le corps de base à p éléments; F_(pⁿ) désigne un corps extension à pⁿ éléments.', 'd est le degré d’un facteur irréductible Q; sa multiplicité est son nombre d’apparitions dans P.', 'Le Frobenius est l’application a→aᵖ. Le deuxième graphique montre uniquement son action sur le corps de base Fₚ.'],
    ['Caractéristique p : p=0 dans les calculs de coefficients.', 'Les facteurs sont exacts. Les racines d’un corps fini ne sont pas représentées comme des racines complexes.'],
    ['Dérivée formelle','PGCD avec la dérivée','Factorisation dans Fₚ[X]','Degrés divisant n'],
    'Dérivation et multiplicité des racines en caractéristique zéro.', 'PGCD(P,P′) comme critère de simplicité des racines.', 'Caractéristique positive, Frobenius et corps finis, accompagnés.',
    ['Choisir p=2,n=3 : prévoir des facteurs de degrés 1 et 3 seulement.', 'Lire P′ et vérifier que toutes les multiplicités valent 1.', 'Passer à n=4; expliquer pourquoi des facteurs de degré 2 apparaissent.'],
    'La dérivée −1 interdit les facteurs répétés; les degrés autorisés sont exactement les diviseurs de n.')
lesson('frobenius_fp','La dérivée change avec la caractéristique','Au-delà accompagné',
    '<p>Dans Fₚ[X], un entier multiple de p représente le coefficient nul. La dérivée de X^(pⁿ) est donc nulle : (X^(pⁿ)−X)′=−1. Le PGCD du polynôme avec sa dérivée vaut 1.</p><p>Sur un corps, un facteur irréductible répété divise aussi la dérivée. Ici, c’est impossible. En revanche, Xᵖ−a a une dérivée nulle et peut être un p-ième pouvoir; la règle familière des racines simples exige de regarder la caractéristique.</p>')
lesson('frobenius_fp','Des racines qui forment un corps','Au-delà accompagné',
    '<p>Dans une clôture algébrique de Fₚ, l’ensemble des racines de X^(pⁿ)−X possède pⁿ éléments distincts. Si a et b sont racines, (a+b)^(pⁿ)=a^(pⁿ)+b^(pⁿ)=a+b et (ab)^(pⁿ)=ab. L’inverse d’une racine non nulle reste une racine.</p><p>Cet ensemble est donc un corps F_(pⁿ). Une racine d’un irréductible de degré d sur Fₚ y appartient exactement lorsque d|n. Cela explique la factorisation du labo. Les éléments supplémentaires ne sont pas de nouveaux résidus modulo p : ils vivent dans une extension de dimension n sur Fₚ.</p>')
exercise('frobenius_fp','Huit racines, quatre facteurs','Au-delà accompagné',
    '<p>Vérifier sur F₂ : X⁸−X=X(X+1)(X³+X+1)(X³+X²+1). Pourquoi les cubiques sont-ils irréductibles ?</p>',
    '<p>Une multiplication modulo 2 donne X⁸+X, égal à X⁸−X dans F₂. Chaque cubique vaut 1 en 0 et en 1 : aucun facteur linéaire, donc irréductibilité en degré 3. Les degrés totalisent 1+1+3+3=8.</p>')
exercise('frobenius_fp','Pas de quadratiques dans X⁸−X','Au-delà accompagné',
    '<p>Pourquoi X²+X+1, irréductible sur F₂, ne divise-t-il pas X⁸−X ? Dans quel polynôme de Frobenius de plus petit degré apparaît-il ?</p>',
    '<p>Son degré 2 ne divise pas 3. Il ne figure donc pas dans X^(2³)−X. Il apparaît dans X^(2²)−X=X⁴−X, puisque 2 divise 2.</p>')
exercise('frobenius_fp','Une extension a plusieurs coordonnées','Au-delà accompagné',
    '<p>α est une racine de X⁴+X+1, irréductible sur F₂. Décrire les éléments de F₂[α] et la réduction de α⁴.</p>',
    '<p>Les éléments s’écrivent de façon unique a₀+a₁α+a₂α²+a₃α³ avec aᵢ∈{0,1}; il y en a 16. La relation α⁴+α+1=0 donne α⁴=α+1 en caractéristique 2.</p>')

guide('cyclotomie','Reconnaître l’ordre exact d’une racine de l’unité et obtenir un polynôme entier par inversion sur les diviseurs.',
    ['n≥2 est l’ordre choisi; k parcourt les entiers de 0 à n−1. ζₖ=exp(2πik/n) est une racine de Xⁿ−1.', 'ζₖ est primitive si son ordre multiplicatif est exactement n; cela équivaut à PGCD(k,n)=1.', 'Φₙ est le polynôme unitaire dont les racines sont les racines primitives d’ordre n. Son degré est φ(n).', 'd parcourt les diviseurs de n et μ est la fonction de Möbius. Un exposant −1 dans le produit désigne un dénominateur qui se simplifie exactement.'],
    ['Calculs polynomiaux exacts sur ℚ, avec coefficients finaux dans ℤ.', 'Les racines sont ici complexes, sur le cercle unité.'],
    ['Racines de l’unité','Ordre dans un groupe','Factorisation par les diviseurs','Inversion multiplicative de Möbius'],
    'Forme exponentielle des complexes, racines n-ièmes et factorisation.', 'Arithmétique et relations entre racines et coefficients.', 'Polynômes cyclotomiques, irréductibilité et extensions algébriques.',
    ['Prendre n=12 et sélectionner les quatre racines primitives.', 'Lire X¹²−1=∏Φ_d pour d|12, puis le produit de Möbius.', 'Prendre n=30 : comparer φ(n), le degré et le nombre de points primitifs.'],
    'Les racines de Xⁿ−1 se répartissent selon leur ordre; cette partition construit les Φ_d et rend le quotient de Möbius exact.')
lesson('cyclotomie','Une racine de l’unité n’a pas toujours l’ordre annoncé','Sup',
    '<p>ζ=exp(2πik/n). Le plus petit entier r&gt;0 tel que ζʳ=1 vaut n/PGCD(k,n). La racine est primitive d’ordre n si PGCD(k,n)=1. Par exemple, exp(2πi×4/12) a ordre 3, alors que exp(2πi×5/12) a ordre 12.</p><p>En regroupant les racines de Xⁿ−1 selon leur ordre d, on obtient Xⁿ−1=∏_{d|n}Φ_d. Le polynôme Φₙ a donc degré φ(n). La première étape demande seulement les racines de l’unité; l’irréductibilité de Φₙ sur ℚ est un théorème supplémentaire.</p>')
lesson('cyclotomie','Möbius peut aussi inverser des produits','Au-delà accompagné',
    '<p>Dans le corps des fractions rationnelles, l’identité Xⁿ−1=∏_{d|n}Φ_d donne Φₙ=∏_{d|n}(Xᵈ−1)^μ(n/d). Pour le vérifier, le coefficient de chaque Φ_e dans le produit est Σ_{d|n/e}μ(d), égal à 1 si e=n et à 0 sinon.</p><p>Des exposants −1 apparaissent, mais le résultat est un polynôme. Pour n=12, Φ₁₂=(X¹²−1)(X²−1)/[(X⁶−1)(X⁴−1)]=X⁴−X²+1. Le labo effectue la division et affiche le reste nul; un simple graphique ne certifierait pas la simplification.</p>')
exercise('cyclotomie','Distinguer six racines et deux primitives','Sup',
    '<p>Donner les racines primitives d’ordre 6 et leur polynôme.</p>',
    '<p>Les entiers k premiers avec 6 sont 1 et 5. Les deux racines sont exp(±iπ/3); leur somme vaut 1 et leur produit vaut 1. Φ₆=X²−X+1.</p>')
exercise('cyclotomie','Un ordre premier','Sup / prolongement',
    '<p>Pour p premier, exprimer Φₚ(X) et Φₚ(1).</p>',
    '<p>Toutes les racines p-ièmes sauf 1 sont primitives. Φₚ=(Xᵖ−1)/(X−1)=1+X+⋯+X^(p−1), donc Φₚ(1)=p.</p>')
exercise('cyclotomie','Un quotient qui redevient entier','Au-delà accompagné',
    '<p>Utiliser les diviseurs de 12 pour obtenir Φ₁₂. Pourquoi le terme X−1 n’intervient-il pas dans le produit de Möbius ?</p>',
    '<p>Les exposants μ(12/d) sont nuls pour d=1,3. Les autres donnent Φ₁₂=(X¹²−1)(X²−1)/[(X⁶−1)(X⁴−1)]=X⁴−X²+1. μ(12)=0 car 12 contient le carré 2².</p>')

guide('bernoulli_faulhaber','Calculer une somme de puissances par télescopage, en gardant une convention unique pour les nombres de Bernoulli.',
    ['p≥1 est la puissance des termes; N est le dernier entier sommé. Sₚ(N)=Σ_{k=0}^N kᵖ.', 'Bₘ(X) est le polynôme de Bernoulli de degré m; bₘ=Bₘ(0), avec b₁=−1/2.', 'Les polynômes sont définis par B₀=1, Bₘ′=mBₘ₋₁ et ∫₀¹Bₘ=0 pour m≥1.', 'a est la translation du deuxième dessin Bₚ₊₁(x+a); elle ne modifie pas la somme Sₚ(N).'],
    ['p≥1 évite la convention 0⁰.', 'Calculs rationnels exacts; la convention b₁=−1/2 est conservée dans toute l’expérience.'],
    ['Différence finie','Télescopage','Primitive polynomiale','Développement de Bernoulli'],
    'Sommes finies, binôme, dérivation et primitive d’un polynôme.', 'Preuves par récurrence et méthodes de sommation.', 'Nombres de Bernoulli, génératrices et formule de Faulhaber.',
    ['Retrouver B₂(X) à partir de sa dérivée et de son intégrale nulle.', 'Choisir p=3 et vérifier la formule classique des cubes.', 'Choisir p=7 puis changer N; vérifier l’égalité exacte des deux calculs.'],
    'La différence Bₚ₊₁(X+1)−Bₚ₊₁(X) est (p+1)Xᵖ; le télescopage transforme la somme en une évaluation de polynôme.')
lesson('bernoulli_faulhaber','La constante de primitive est déterminée par une moyenne','Sup / prolongement',
    '<p>Poser B₀=1. Pour m≥1, Bₘ est l’unique primitive de mBₘ₋₁ dont l’intégrale sur [0,1] est nulle. Ainsi B₁=X−1/2, B₂=X²−X+1/6 et B₃=X³−3X²/2+X/2.</p><p>Les nombres bₘ=Bₘ(0) sont des rationnels. Cette convention donne b₁=−1/2. La différence finie Bₘ(X+1)−Bₘ(X)=mXᵐ⁻¹ joue pour les sommes le rôle qu’une dérivée joue pour les intégrales. Une convention utilisant +1/2 doit être accompagnée d’une formule de sommation adaptée.</p>')
lesson('bernoulli_faulhaber','Faulhaber par annulation des termes intermédiaires','Spé / prolongement',
    '<p>Pour p≥1, sommer Bₚ₊₁(k+1)−Bₚ₊₁(k)=(p+1)kᵖ de k=0 à N. Chaque terme intermédiaire apparaît une fois avec chaque signe. Il reste Sₚ(N)=[Bₚ₊₁(N+1)−Bₚ₊₁(0)]/(p+1).</p><p>Cette expression est un polynôme en N de degré p+1, de coefficient dominant 1/(p+1). Pour p=3, S₃(N)=N²(N+1)²/4. Le calcul direct sur les entiers sert de contrôle; la preuve repose sur le télescopage, pas sur quelques valeurs numériques.</p>')
exercise('bernoulli_faulhaber','Construire B₂','Sup',
    '<p>Avec B₁=X−1/2, déterminer B₂ en utilisant B₂′=2B₁ et ∫₀¹B₂=0.</p>',
    '<p>Une primitive est X²−X+c. Son intégrale est 1/3−1/2+c; elle s’annule pour c=1/6. Donc B₂=X²−X+1/6.</p>')
exercise('bernoulli_faulhaber','Sommer sans récurrence forte','Sup / prolongement',
    '<p>B₃=X³−3X²/2+X/2. Retrouver Σ_{k=0}^N k².</p>',
    '<p>B₃(X+1)−B₃(X)=3X². Le télescopage donne B₃(N+1)/3, puisque B₃(0)=0. Après développement : N(N+1)(2N+1)/6.</p>')
exercise('bernoulli_faulhaber','Contrôler une génératrice au voisinage de zéro','Spé / prolongement',
    '<p>La fonction G(z)=z/(exp(z)−1), prolongée en z=0, engendre les nombres bₘ=Bₘ(0). Calculer ses trois premiers termes et les comparer à B₁,B₂.</p>',
    '<p>exp(z)−1=z+z²/2+z³/6+⋯. L’inversion donne G(z)=1−z/2+z²/12+O(z³). Le coefficient de zᵐ est bₘ/m! : b₀=1, b₁=−1/2, b₂=1/6.</p>')

guide('euler_maclaurin','Estimer une somme par une intégrale et savoir jusqu’où une correction peut être garantie.',
    ['f est la fonction choisie : 1/x, exp(−x/3) ou xᵈ. x est réel et j est l’indice entier de la somme.', 'N≥2 est la borne supérieure; S=Σ_{j=1}^Nf(j) inclut 1 et N.', 'k est le nombre de corrections de Bernoulli; b₂ᵢ=B₂ᵢ(0) est un nombre rationnel.', 'Rₖ est le reste entre S et l’expression corrigée. d n’intervient que pour la fonction polynomiale.'],
    ['f est suffisamment dérivable sur [1,N]; ici les trois familles sont indéfiniment dérivables.', 'La borne utilise l’intégrale de la valeur absolue d’une dérivée; les dérivées nécessaires ont un signe constant pour les familles proposées.'],
    ['Comparaison somme–intégrale','Termes aux extrémités','Intégration par parties','Majoration du reste'],
    'Primitives, sommes et comparaison avec une intégrale.', 'Formules de Taylor, intégrations par parties et contrôle d’erreur.', 'Euler–Maclaurin, développements asymptotiques et nombres de Bernoulli.',
    ['Choisir 1/x et comparer l’intégrale seule à la correction des extrémités.', 'Ajouter k=1 puis k=2 et lire l’erreur avec sa borne.', 'Choisir x⁶, k=3 : expliquer pourquoi la somme devient exacte.'],
    'Une correction est utile lorsqu’elle réduit une erreur contrôlée. Pour un polynôme, assez de dérivées nulles donnent une formule exacte.')
lesson('euler_maclaurin','Commencer par les deux extrémités','Spé / prolongement',
    '<p>Pour l&lt;m entiers, S=Σ_{j=l}^m f(j). Si f est continûment dérivable, S=∫ₗᵐf(x)dx+[f(l)+f(m)]/2+R₀. Le reste est R₀=∫ₗᵐf′(x)B₁({x})dx, avec {x}=x−⌊x⌋ et B₁(u)=u−1/2.</p><p>Comme |B₁({x})|≤1/2, |R₀|≤(1/2)∫ₗᵐ|f′|. La formule suppose une somme incluant les deux extrémités. Ajouter des extrémités à une somme qui les exclut changerait les signes; les bornes doivent donc être écrites avant les calculs.</p>')
lesson('euler_maclaurin','Corriger n’est pas toujours converger','Au-delà accompagné',
    '<p>Pour k≥1 et f de classe C²ᵏ sur [l,m], ajouter Σ_{i=1}^k b₂ᵢ[f^(2i−1)(m)−f^(2i−1)(l)]/(2i)!. Le reste vérifie |Rₖ|≤|b₂ₖ|∫ₗᵐ|f^(2k)|/(2k)!.</p><p>Pour un polynôme de degré d, si 2k&gt;d, le reste est nul. Si 2k=d, sa dérivée 2k-ième est constante et l’intégrale de B₂ₖ sur chaque unité est nulle : le reste est encore nul. Pour une fonction générale, les corrections constituent souvent un développement asymptotique; il faut contrôler chaque erreur et ne pas supposer qu’ajouter indéfiniment des termes améliore tout.</p>')
exercise('euler_maclaurin','Les carrés deviennent exacts','Sup / prolongement',
    '<p>Appliquer Euler–Maclaurin à f(x)=x² sur [0,N], avec une correction et b₂=1/6, pour retrouver Σ_{j=0}^N j².</p>',
    '<p>L’intégrale vaut N³/3, les demi-extrémités N²/2, et la correction b₂[f′(N)−f′(0)]/2!=N/6. Leur somme est N(N+1)(2N+1)/6. La dérivée seconde est constante : le reste intègre B₂ sur des intervalles entiers et vaut 0.</p>')
exercise('euler_maclaurin','Une borne pour la somme harmonique','Spé / prolongement',
    '<p>Pour f(x)=1/x et N≥2, écrire l’approximation avec k=1 et majorer son reste.</p>',
    '<p>S≈ln N+(1+1/N)/2+(1−1/N²)/12. f″=2/x³, donc |R₁|≤(1/12)∫₁ᴺ2/x³ dx=(1−1/N²)/12. La borne garantit l’écart, même si elle peut être bien supérieure à l’erreur observée.</p>')
exercise('euler_maclaurin','Savoir quand s’arrêter','Spé / prolongement',
    '<p>Pour un polynôme f de degré 7 et une somme sur des bornes entières, combien de corrections suffisent à garantir un reste nul ? Justifier par la formule du reste.</p>',
    '<p>Quatre corrections suffisent : 2k=8&gt;7, donc f^(8)=0. Le reste R₄ est nul. Cela fournit un arrêt garanti, indépendamment de la forme des coefficients du polynôme.</p>')
