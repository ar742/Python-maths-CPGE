"""Cours et problèmes guidés : fractions, interpolation et orthogonalité."""
import html
GUIDES={}; LESSONS=[]; EXERCISES=[]
def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=list(map(html.unescape,objects)),hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=list(map(html.unescape,first_steps)),expected=expected)
def lesson(id_,title,level,html): LESSONS.append(dict(lab=id_,title=title,level=level,html=html))
def exercise(id_,title,level,question,answer): EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('rationnelle_recueil','Décomposer une fraction comportant un pôle triple, puis vérifier la recomposition.',
    ['X est l’indéterminée ; x est une valeur réelle pour le graphique. F=P/Q est la fraction rationnelle.','s est la translation des pôles : s−1 et s+2. A,B,C,D sont les coefficients des quatre termes polaires.','La partie entière est le quotient polynomial de P par Q. Un pôle d’ordre m conserve (X−a)^m au dénominateur après simplification.'],
    ['Coefficients rationnels et dénominateur non nul.','Les ordres sont déterminés sur la fraction réduite ; le tracé est limité près des divergences.'],
    ['Division euclidienne','Factorisation du dénominateur','Évaluation après multiplication par un facteur','Dérivées pour un pôle multiple'],
    'Sup : éléments simples sur ℝ et ℂ, division euclidienne.',
    'Spé : réinvestissement dans les intégrales, séries et systèmes linéaires.',
    'Les résidus complexes sont introduits dans le TP de regroupement ; aucune intégrale de contour n’est requise.',
    ['Reprendre le preset de l’exercice 4 et vérifier la partie entière 1.','Mettre D=0, puis C=0 : prévoir les ordres restants.','Translater les pôles avec s et vérifier que les coefficients polaires ne changent pas.'],
    'La partie entière décrit le comportement polynomial ; les puissances négatives décrivent chaque pôle.')
lesson('rationnelle_recueil','Quotient polynomial et parties polaires','Sup — fractions rationnelles',
    '<p>Une fraction rationnelle F=P/Q est un quotient de polynômes, Q non nul. Réduire F consiste à supprimer leur PGCD. La division P=EQ+R, avec deg R&lt;deg Q, sépare le polynôme E, appelé partie entière, de R/Q.</p>'
    '<p>Dans l’exercice 4, P=X⁴−2X³−7X²+29X−21 et Q=X⁴−5X³+6X²+4X−8=(X+1)(X−2)³. Les coefficients dominants sont égaux : la partie entière vaut 1.</p>'
    '<div class="formula">F=1+2/(X+1)+1/(X−2)+2/(X−2)²+3/(X−2)³.</div>'
    '<p>Multiplier cette égalité par Q permet une vérification polynomialement exacte, même si le graphique ne montre qu’un nombre fini de valeurs.</p>')
lesson('rationnelle_recueil','Identifier les coefficients sans système global','Sup — méthode locale',
    '<p>Soit a un pôle simple. On appelle c le coefficient de 1/(X−a). Après multiplication de F par X−a, les autres termes restent réguliers et le terme c est isolé par évaluation en a.</p>'
    '<p>Pour un pôle triple en b, poser g=(X−b)³F. Les trois coefficients devant (X−b)⁻³, (X−b)⁻² et (X−b)⁻¹ sont respectivement g(b), g′(b) et g″(b)/2. Les termes réguliers multipliés par (X−b)³ n’interviennent pas dans ces évaluations.</p>'
    '<p>Si le premier coefficient est nul, le pôle n’est plus triple. L’ordre effectif se lit après réduction.</p>')
exercise('rationnelle_recueil','Le coefficient au pôle simple','Sup',
    '<p>Pour la fraction de l’exercice 4, multiplier F par X+1 puis évaluer en −1. Déterminer le coefficient du terme simple.</p>',
    '<p>Le coefficient vaut P(−1)/(−3)³. P(−1)=−54, donc il vaut 2. Les termes réguliers multipliés par X+1 s’annulent au point −1.</p>')
exercise('rationnelle_recueil','Faire disparaître les puissances fortes','Sup',
    '<p>Soit F=1+2/(X+1)+1/(X−2)+C/(X−2)²+D/(X−2)³. Quels choix donnent un pôle simple en 2 ?</p>',
    '<p>Il faut D=0 puis C=0. Le coefficient de 1/(X−2) reste 1, non nul : l’ordre est exactement un. Si ce coefficient était aussi nul, le pôle disparaîtrait.</p>')
exercise('rationnelle_recueil','De la décomposition à une primitive','Sup / spé',
    '<p>Donner une primitive de la fraction du recueil sur chacun des intervalles séparés par −1 et 2.</p>',
    '<p>Une primitive est x+2 ln|x+1|+ln|x−2|−2/(x−2)−3/[2(x−2)²]. La constante d’intégration peut être différente sur chaque intervalle. La dérivation retrouve chaque élément simple.</p>')

guide('poles_multiples','Retrouver une décomposition par les dérivées au point du pôle.',
    ['g(X)=X⁴+cX²+X+1 est le numérateur ; c est son coefficient réglable.','a est le point où le dénominateur s’annule ; m est sa puissance entière, de 2 à 5.','A_k est le coefficient de (X−a)^−k, pour 1≤k≤m ; g^(j)(a) est la dérivée d’ordre j évaluée en a.'],
    ['Taylor polynomial est une identité exacte.','Un zéro de g en a peut réduire l’ordre du pôle.'],
    ['Taylor polynomial','Dérivation successive','Lecture des puissances négatives','Contrôle de multiplicité'],
    'Sup : dérivées, multiplicité, éléments simples.',
    'Spé : réinvestir Taylor dans les calculs locaux.',
    'Développement de Laurent : les puissances négatives sont déjà visibles ici, sans théorie des fonctions holomorphes.',
    ['Avec m=3, retrouver les coefficients g(a), g′(a), g″(a)/2.','Choisir a=−1 et c=−1, puis vérifier g(a)=0.','Passer à m=5 : le numérateur de degré quatre ne produit aucune partie entière.'],
    'Chaque coefficient polaire correspond à une dérivée ; l’annulation de coefficients révèle la multiplicité commune.')
lesson('poles_multiples','Taylor devient une décomposition en puissances','Sup — Taylor exact',
    '<p>Soit g un polynôme de degré d et a un nombre. En posant h=X−a, on écrit exactement g(X)=Σ_{j=0}^d g^(j)(a)h^j/j!. Il n’y a pas de reste d’approximation.</p>'
    '<p>Diviser par h^m donne des puissances h^(j−m). Les indices j&lt;m produisent la partie polaire ; les indices j≥m produisent la partie entière.</p>'
    '<div class="formula">A_k=g^(m−k)(a)/(m−k)!, pour 1≤k≤m.</div>')
lesson('poles_multiples','L’ordre du pôle résiste-t-il à la réduction ?','Sup — zéros et pôles',
    '<p>Soit r la multiplicité du zéro de g en a : g=(X−a)^r u et u(a)≠0. Si r&lt;m, la fraction a un pôle d’ordre m−r. Si r≥m, elle est régulière après simplification.</p>'
    '<p>Le dénominateur initial interdit toujours a à l’expression de départ. La formule réduite peut toutefois fournir un prolongement continu. Cette distinction relie factorisation et limites.</p>')
exercise('poles_multiples','Un pôle triple calculé en une ligne','Sup',
    '<p>Décomposer (X⁴+2X²+X+1)/X³.</p>',
    '<p>La division des monômes donne X+2/X+1/X²+1/X³. Les coefficients polaires sont g″(0)/2=2, g′(0)=1 et g(0)=1 ; la partie entière est X.</p>')
exercise('poles_multiples','Un ordre qui baisse','Sup',
    '<p>Avec g=X⁴−X²+X+1, déterminer l’ordre de g/(X+1)^4 en −1.</p>',
    '<p>g(−1)=0 mais g′(−1)=4(−1)³−2(−1)+1=−1, non nul. Le numérateur possède un zéro simple ; le pôle réduit est donc d’ordre trois.</p>')
exercise('poles_multiples','Construire une partie polaire imposée','Spé — synthèse',
    '<p>Pour m=3, chercher un numérateur polynomial g donnant les coefficients 2, −1, 3 devant (X−a)⁻¹, (X−a)⁻², (X−a)⁻³.</p>',
    '<p>Il faut g(a)=3, g′(a)=−1 et g″(a)=4. Ainsi g=3−(X−a)+2(X−a)²+(X−a)³q(X), où q est un polynôme arbitraire. La fraction vaut q+2/(X−a)−1/(X−a)²+3/(X−a)³.</p>')

guide('reel_complexe','Passer d’une décomposition complexe à une écriture réelle.',
    ['a est la partie réelle des deux pôles, b&gt;0 leur distance à la droite réelle ; α=a+ib.','u,v,w sont les coefficients réels de F=(uX+v)/[(X−a)²+b²]+w/(X−2).','c_α est le coefficient de 1/(X−α) ; la barre signifie conjugaison. Re(z), Im(z) sont les coordonnées d’un nombre complexe z.'],
    ['b reste strictement positif, donc les pôles non réels sont distincts.','L’écriture réelle a des coefficients réels ; les résidus se conjuguent.'],
    ['Factorisation sur ℂ','Coefficient d’un pôle simple','Conjugaison','Regroupement sur ℝ'],
    'Sup : fractions rationnelles sur ℝ et ℂ.',
    'Spé : réinvestir les couples conjugués dans les équations différentielles.',
    'Le mot résidu désigne ici un coefficient d’élément simple ; le théorème des résidus n’est pas utilisé.',
    ['Avec a=0,b=1, factoriser X²+1.','Comparer les parties imaginaires opposées des deux coefficients.','Mettre w=0 et vérifier la disparition du pôle réel.'],
    'Deux termes complexes conjugués reconstruisent une fraction réelle.')
lesson('reel_complexe','Le coefficient d’un pôle non réel','Sup — factorisation complexe',
    '<p>Avec a,b,u,v réels et b&gt;0, les racines du quadratique (X−a)²+b² sont α=a+ib et β=a−ib. Le coefficient c_α du pôle α est obtenu en multipliant par X−α.</p>'
    '<div class="formula">c_α=(uα+v)/(α−β) ; c_β=conj(c_α).</div>'
    '<p>On peut aussi écrire le dénominateur Q et calculer c_α=P(α)/Q′(α) pour une fraction P/Q à pôle simple α. Cette règle vient de Q=(X−α)q et Q′(α)=q(α).</p>')
lesson('reel_complexe','Pourquoi la somme reste réelle','Sup — conjugaison',
    '<p>Pour une valeur réelle x, les nombres c_α/(x−α) et conj(c_α)/(x−conj(α)) sont conjugués. Leur somme vaut deux fois la partie réelle du premier.</p>'
    '<p>Sur le plan complexe du TP, les points sont les pôles. La courbe réelle représente les valeurs de la fraction sur ℝ : ce sont deux objets distincts, à relier par la factorisation.</p>'
    '<div class="formula">c_α/(X−α)+conj(c_α)/(X−conj(α))=(uX+v)/[(X−a)²+b²].</div>')
exercise('reel_complexe','Décomposer 1/(X²+1)','Sup',
    '<p>Déterminer les coefficients des termes en 1/(X−i) et 1/(X+i).</p>',
    '<p>Au pôle i, le coefficient est 1/(2i)=−i/2. Au pôle −i, il vaut i/2. Ainsi 1/(X²+1)=−i/[2(X−i)]+i/[2(X+i)].</p>')
exercise('reel_complexe','Regrouper deux fractions conjuguées','Sup',
    '<p>Regrouper (1+i)/(X−i)+(1−i)/(X+i) en une fraction réelle.</p>',
    '<p>Le numérateur est (1+i)(X+i)+(1−i)(X−i)=2X−2. La somme vaut donc (2X−2)/(X²+1).</p>')
exercise('reel_complexe','Une primitive réelle à retrouver','Sup / spé',
    '<p>Intégrer (2x+1)/(x²+1) sur ℝ.</p>',
    '<p>Le terme 2x/(x²+1) donne ln(x²+1). Le terme 1/(x²+1) donne arctan x. Une primitive réelle est ln(x²+1)+arctan x. La décomposition complexe explique le couple de pôles ; elle n’oblige pas à choisir des logarithmes complexes.</p>')

guide('annulations','Décider si un point interdit admet une limite finie.',
    ['La fraction initiale est F=(X−a)^k(X²+1)/[(X−a)^m(X−b)(X²+1)].','a,b sont les deux points interdits réels ; k,m sont des multiplicités entières positives.','La fraction réduite est obtenue par suppression du PGCD. Un trou est un point interdit où la limite de la formule réduite est finie.'],
    ['Les limites sont calculées dans ℝ.','Si a=b, les facteurs du dénominateur se regroupent avant de compter les ordres.'],
    ['Domaine d’une expression','PGCD et simplification','Limites en un point','Comparaison de multiplicités'],
    'Sup : limites, factorisation et fractions rationnelles.',
    'Spé : singularités éliminables et prolongements continus.',
    'Interprétation dans le corps ℝ(X), où une fraction est une classe d’écritures équivalentes.',
    ['Prendre k=m et a≠b : distinguer les deux points interdits.','Prendre k&lt;m : constater une divergence en a.','Choisir a=b puis comparer k avec m+1.'],
    'L’égalité de fractions rationnelles et l’égalité de fonctions sur leur domaine initial sont à distinguer.')
lesson('annulations','Réduire un quotient et conserver son domaine','Sup — fonctions et polynômes',
    '<p>Deux écritures P/Q et A/B représentent la même fraction rationnelle si PB=AQ. Comme fonctions numériques, elles coïncident là où leurs deux dénominateurs sont non nuls.</p>'
    '<p>Par exemple (X²−1)/(X−1)=X+1 dans ℝ(X). L’expression de gauche reste interdite en x=1 ; la fonction x↦x+1 fournit son prolongement continu. Le trou a pour ordonnée 2.</p>')
lesson('annulations','Lorsque les points interdits se confondent','Sup — multiplicités',
    '<p>Dans le TP, les facteurs X²+1 se simplifient et n’ont pas de zéro réel. Si a≠b, l’ordre en a dépend de m−k, tandis que b reste un pôle simple.</p>'
    '<p>Si a=b, le dénominateur contient (X−a)^(m+1). La fraction réduite devient (X−a)^(k−m−1). Le seuil entre trou et pôle se déplace donc d’une unité. L’identité des points doit être vérifiée avant de lire les multiplicités.</p>')
exercise('annulations','Un trou avec une limite non nulle','Sup',
    '<p>Déterminer la limite en 2 de (x³−8)/(x−2), et préciser le domaine initial.</p>',
    '<p>x³−8=(x−2)(x²+2x+4). La formule réduite vaut x²+2x+4 et tend vers 12. Le domaine initial est ℝ privé de 2 ; on peut prolonger la fonction en attribuant la valeur 12.</p>')
exercise('annulations','Une collision change le diagnostic','Sup',
    '<p>Avec k=m=2, comparer F=(X−a)^k/[(X−a)^m(X−b)] lorsque a≠b puis lorsque a=b.</p>',
    '<p>Si a≠b, la formule réduite est 1/(X−b) : trou en a, pôle simple en b. Si a=b, elle devient 1/(X−a) : le point unique est un pôle. L’annulation des facteurs n’efface pas le facteur supplémentaire X−b.</p>')
exercise('annulations','Toutes les limites possibles','Spé — synthèse',
    '<p>Supposer a=b. Classer le point a selon les valeurs de k−m−1.</p>',
    '<p>Si k−m−1&lt;0, il reste un pôle d’ordre m+1−k. Si k−m−1=0, la formule réduite est constante 1 et la limite vaut 1. Si k−m−1&gt;0, la limite vaut 0. Dans les deux derniers cas, le point est toujours exclu de l’expression initiale.</p>')

guide('interpolation','Évaluer un polynôme interpolateur et distinguer interpolation et approximation.',
    ['n est le degré maximal ; les n+1 nœuds x_i sont distincts dans [−1,1].','f(x)=1/(1+cx²) est la fonction de Runge ; c&gt;0 est son paramètre. P_n prend les valeurs f(x_i).','La matrice de Vandermonde contient les puissances des nœuds ; son conditionnement mesure la sensibilité du système dans la base des monômes.','L’erreur affichée est max |P_n−f| sur une grille de 1001 points.'],
    ['L’unicité théorique concerne des valeurs exactes ; l’évaluation est numérique.','Les deux répartitions utilisent le même nombre de nœuds.'],
    ['Lagrange et unicité','Choix d’une base','Conditionnement','Évaluation d’une erreur'],
    'Sup : polynômes de Lagrange, systèmes linéaires et déterminants.',
    'Spé : approximation, normes et stabilité d’un calcul.',
    'Phénomène de Runge et formule barycentrique, introduits avec leur mécanisme.',
    ['Choisir n=14 avec les nœuds équidistants et observer les extrémités.','Passer aux nœuds de Tchebychev sans changer le degré.','Diminuer n et c ; comparer l’erreur et le conditionnement.'],
    'Un polynôme peut satisfaire exactement toutes les contraintes et mal approcher la fonction entre les nœuds.')
lesson('interpolation','Lagrange : existence et unicité','Sup — interpolation',
    '<p>Soient n+1 nœuds distincts x₀,…,x_n et des valeurs y₀,…,y_n. Le polynôme L_i(X)=∏_{j≠i}(X−x_j)/(x_i−x_j) vaut 1 au nœud i et 0 aux autres.</p>'
    '<div class="formula">P(X)=Σ_{i=0}^n y_i L_i(X), deg P≤n.</div>'
    '<p>Si deux polynômes de degré au plus n satisfont les mêmes contraintes, leur différence possède n+1 racines distinctes. Elle est donc nulle. Cette preuve évite de calculer un déterminant.</p>')
lesson('interpolation','Changer les nœuds plutôt que monter le degré','Spé — prolongement numérique',
    '<p>Le poids barycentrique w_i est 1/∏_{j≠i}(x_i−x_j). Pour x différent des nœuds, l’interpolateur s’évalue par [Σ w_i y_i/(x−x_i)]/[Σ w_i/(x−x_i)]. Aux nœuds, on reprend directement la valeur y_i.</p>'
    '<p>Cette écriture évite le développement dans les monômes. Elle ne supprime pas le phénomène de Runge : celui-ci concerne le choix des nœuds et l’approximation. Les nœuds de Tchebychev, cos((2i+1)π/[2(n+1)]), se resserrent aux extrémités et améliorent ce cas.</p>')
exercise('interpolation','Un reste de division obtenu par trois valeurs','Sup — TP p.166',
    '<p>Déterminer le reste de X⁴ par (X−1)(X−2)(X−3), à partir de ses valeurs aux trois racines.</p>',
    '<p>Le reste R=αX²+βX+γ vérifie R(1)=1, R(2)=16, R(3)=81. La résolution donne α=25, β=−60, γ=36. Vérifier : X⁴=(X+6)(X³−6X²+11X−6)+25X²−60X+36.</p>')
exercise('interpolation','Pourquoi la différence s’annule','Sup',
    '<p>Deux polynômes de degré au plus quatre coïncident en cinq points distincts. Montrer qu’ils sont égaux.</p>',
    '<p>Leur différence a degré au plus quatre et possède cinq racines distinctes. Un polynôme non nul ne peut pas avoir plus de racines que son degré. La différence est donc nulle.</p>')
exercise('interpolation','Une fonction invisible aux nœuds','Spé — contre-exemple',
    '<p>À des nœuds x₀,…,x_n, les données sont toutes nulles. Construire une fonction non nulle qui a pourtant ces valeurs.</p>',
    '<p>Prendre f(x)=∏_{i=0}^n(x−x_i). Son interpolateur de degré au plus n est le polynôme nul, alors que f n’est pas identiquement nulle. Le contrôle aux nœuds ne suffit pas à contrôler l’erreur entre eux.</p>')

guide('orthogonaux','Relier trois familles du recueil aux espaces préhilbertiens et à l’intégration.',
    ['n est le degré du polynôme ; k est la puissance du moment ∫x^k w(x)dx à vérifier.','P_n est Legendre, Tchebychev T_n ou Hermite probabiliste H_n, selon le choix.','w(x) est le poids : 1 sur [−1,1], 1/√(1−x²) sur ]−1,1[, ou exp(−x²/2) sur ℝ.','x_i sont les n racines de P_n ; W_i sont les poids positifs de quadrature. Le carré de la norme est ∫P_n²w.'],
    ['Le degré n va de 2 à 12 ; les trois familles ont des racines réelles simples.','Les deux courbes de la scène sont mises à l’échelle séparément, sans déplacer leurs racines.'],
    ['Produit scalaire intégral','Orthogonalisation','Parité et moments','Exactitude d’une quadrature'],
    'Sup : produits scalaires, bases orthogonales, intégration.',
    'Spé : espaces préhilbertiens et familles de polynômes.',
    'Quadrature de Gauss : formule et justification accompagnées.',
    ['Avec Legendre et n=6, comparer les moments k=10 et k=11.','Choisir k=12 et observer la perte de garantie.','Passer à Hermite : retrouver le moment gaussien d’ordre dix.'],
    'L’orthogonalité donne des racines entrelacées et une quadrature exacte jusqu’au degré 2n−1.')
lesson('orthogonaux','Trois produits scalaires, trois bases','Sup / spé — espaces préhilbertiens',
    '<p>Pour deux polynômes A,B, on définit ⟨A,B⟩=∫A(x)B(x)w(x)dx. Les poids du TP sont positifs et les moments nécessaires existent. La famille de degré croissant obtenue par orthogonalisation est une base de chaque espace de polynômes de degré borné.</p>'
    '<p>Legendre est normalisé par L_n(1)=1. Tchebychev vérifie T_n(cos θ)=cos(nθ). Hermite probabiliste vérifie H₀=1, H₁=X et H_{n+1}=XH_n−nH_{n−1}. Les trois normalisations sont précisées : elles ne sont pas interchangeables.</p>'
    '<div class="formula">‖L_n‖²=2/(2n+1) ; ‖T_n‖²=π/2 pour n≥1 ; ‖H_n‖²=√(2π)n!.</div>')
lesson('orthogonaux','Pourquoi n nœuds intègrent jusqu’au degré 2n−1','Au-delà — quadrature de Gauss',
    '<p>Soit P_n le polynôme orthogonal de degré n et x_i ses racines simples. Les poids W_i sont choisis pour intégrer exactement les polynômes de degré au plus n−1.</p>'
    '<p>Pour un polynôme R de degré au plus 2n−1, diviser R=P_nQ+S avec deg Q≤n−1 et deg S≤n−1. L’intégrale de P_nQ est nulle par orthogonalité ; ses valeurs aux nœuds sont nulles aussi. La formule est donc exacte pour R.</p>'
    '<p>Pour R=P_n², la quadrature donne zéro mais l’intégrale est strictement positive. Le degré 2n−1 est ainsi le meilleur degré garanti pour ces n nœuds.</p>')
exercise('orthogonaux','Vérifier une orthogonalité de Legendre','Sup',
    '<p>Avec L₀=1 et L₂=(3X²−1)/2, calculer ∫_{−1}^1 L₀L₂.</p>',
    '<p>L’intégrale vaut [x³−x]_{−1}^1/2=0. La constante et le polynôme de degré deux sont orthogonaux pour le poids uniforme.</p>')
exercise('orthogonaux','Les deux conventions d’Hermite','Sup / spé',
    '<p>Déterminer H₂ et Ĥ₂, sachant H₁=X dans la convention probabiliste et Ĥ₁=2X dans la convention physique.</p>',
    '<p>Les récurrences donnent H₂=X²−1 et Ĥ₂=4X²−2. La relation Ĥ₂(X)=2H₂(√2X) est vérifiée. Une comparaison exige de préciser le poids gaussien et le changement d’échelle.</p>')
exercise('orthogonaux','Deux nœuds, quatre moments','Au-delà — application guidée',
    '<p>Pour Legendre n=2, les nœuds sont ±1/√3 et les deux poids valent 1. Vérifier la formule pour 1,x,x²,x³ puis tester x⁴.</p>',
    '<p>Les sommes valent 2,0,2/3,0 : ce sont les quatre intégrales exactes. Pour x⁴, la quadrature donne 2/9 alors que l’intégrale vaut 2/5. Le degré trois est garanti ; le degré quatre ne l’est pas.</p>')
