"""Cours, exercices corrigés et guides de dix laboratoires multivariés."""
GUIDES={}
LESSONS=[]
EXERCISES=[]

def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=first_steps,expected=expected)
def lesson(id_,title,level,html): LESSONS.append(dict(lab=id_,title=title,level=level,html=html))
def exercise(id_,title,level,question,answer): EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('monomes_newton','Lire un polynôme à deux indéterminées sans confondre ses différents degrés.',
    ['x et y sont les deux indéterminées. Les coordonnées du dessin principal sont i et j, les exposants du monôme xⁱyʲ ; ce ne sont pas des valeurs de x et y.', 'P(x,y)=xᵐ+ax²yᑫ+yⁿ+c. Les entiers m,n,q fixent des exposants ; a et c sont des coefficients réels, sans unité.', 'Le support est l’ensemble des couples (i,j) dont le coefficient est non nul. Le polygone de Newton est leur enveloppe convexe.', 'Le degré total est le maximum de i+j ; les degrés partiels sont les maximums de i puis de j. Les courbes secondaires sont les tranches y=0 et y=1.'],
    ['Un monôme de coefficient nul est retiré du support.','Le polynôme possède toujours les termes xᵐ et yⁿ : il n’est jamais nul.'],
    ['Identifier les coefficients','Calculer un degré total et des degrés partiels','Enveloppe convexe','Spécialiser une indéterminée'],
    'Sup : règles de calcul sur les polynômes ; commencer par reconnaître des monômes.',
    'Spé : traiter un polynôme en x dont les coefficients sont eux-mêmes des polynômes en y ; relier les degrés à une factorisation.',
    'Polygones de Newton, valuation et comptage d’intersections dans le tore : prolongements, non déduits du seul dessin.',
    ['Prendre m=n=4 et q=3 ; calculer les trois degrés avant de lire les valeurs.','Annuler a : quel point du support disparaît ? Le degré total change-t-il ?','Annuler c, puis comparer la tranche y=0 au polynôme initial.'],
    'Le degré total ne se calcule ni en additionnant les degrés partiels ni en comptant les termes ; une spécialisation peut l’abaisser.')
lesson('monomes_newton','Trois notions de degré à séparer','Sup · bases algébriques',
    '<p>Pour un polynôme P(x,y)=∑aᵢⱼxⁱyʲ non nul, x et y sont des indéterminées et aᵢⱼ ses coefficients. Un monôme xⁱyʲ a degré total i+j. Le degré total de P est le plus grand i+j avec aᵢⱼ≠0.</p><p>Le degré en x est le plus grand i ; celui en y est le plus grand j. Ainsi x⁴+x²y³+y⁴+1 a degré total 5 et degrés partiels 4 et 4. Leur somme, 8, n’est pas le degré total. En considérant P comme un polynôme en x à coefficients dans ℝ[y], on retrouve le degré partiel en x.</p>')
lesson('monomes_newton','Support et spécialisation : ce que le dessin permet','Spé · prolongement guidé',
    '<p>Le support de P est l’ensemble des exposants (i,j) portant un coefficient non nul. Son enveloppe convexe est le polygone de Newton. Le dessin distingue les monômes extrêmes des monômes intérieurs, sans représenter la courbe réelle P(x,y)=0.</p><p>Spécialiser y=y₀ remplace une indéterminée par un nombre. Cette opération peut créer des compensations : P(x,y)=(y−1)x³+x² a degré 3 en x, alors que P(x,1)=x². Les degrés calculés avant et après spécialisation ont donc des significations différentes. Les théorèmes de Newton sur les racines et les intersections exigent des hypothèses supplémentaires.</p>')
exercise('monomes_newton','Ne pas additionner les degrés partiels','Sup',
    'Pour P(x,y)=2x⁵y²−3x²y⁶+y⁷+4, déterminer le support, les degrés partiels et le degré total. Que devient le degré après y=0 ?',
    'Support : {(5,2),(2,6),(0,7),(0,0)}. Les degrés en x et y valent 5 et 7. Les degrés des termes sont 7,8,7,0, donc deg P=8. La spécialisation P(x,0)=4 a degré 0 ; elle ne conserve pas le degré en x.')
exercise('monomes_newton','Le produit additionne les degrés totaux','Sup / Spé',
    'Dans ℝ[x,y], montrer que deg(PQ)=deg P+deg Q pour deux polynômes non nuls. Pourquoi le même argument ne justifie-t-il pas deg(P+Q)=max(deg P,deg Q) sans condition ?',
    'Écrire P=P_d+termes de degré inférieur et Q=Q_e+termes de degré inférieur, où P_d,Q_e sont leurs parties homogènes dominantes. La partie de degré d+e de PQ vaut P_dQ_e≠0, car ℝ[x,y] est intègre. Pour la somme, les parties dominantes peuvent se compenser : (x²+y²)+(−x²−y²+x)=x.')
exercise('monomes_newton','Une enveloppe convexe qui change','Au-delà · accompagné',
    'Pour P=x⁴+y⁴+ax²y³+1, calculer l’aire du polygone de Newton lorsque a=0 puis lorsque a≠0. Le signe de a intervient-il ?',
    'Si a=0, le support extrême est (0,0),(4,0),(0,4), triangle d’aire 8. Si a≠0, le point (2,3) est extérieur au triangle : le quadrilatère (0,0),(4,0),(2,3),(0,4) a aire (12+8)/2=10. Le signe de a ne change pas le support ; seul son caractère nul ou non nul intervient.')

guide('intersection_bezout','Compter des solutions réelles sans perdre les racines complexes ou les multiplicités.',
    ['x,y sont des coordonnées réelles pour le dessin, puis complexes pour le comptage algébrique. Le cercle est x²+y²=r², de rayon r>0 ; la parabole est y=x²−h.', 'r et h sont les paramètres sans unité. Le polynôme éliminé est Q(x)=x⁴+(1−2h)x²+h²−r².', 't=x² permet de ramener Q=0 à une équation du second degré ; D=1−4h+4r² en est le discriminant.', 'La multiplicité est ici celle d’une racine de Q. La substitution y=x²−h identifie cette multiplicité à celle de l’intersection dans cette famille.'],
    ['Les deux courbes de degré 2 n’ont pas de composante commune.','Aucune intersection commune à l’infini : les quatre intersections complexes avec multiplicité sont dans la carte affine.'],
    ['Substitution et équation bicarrée','Discriminant','Racines complexes','Racines multiples et dérivée'],
    'Sup : équations du second degré et racines complexes ; tester t≥0 avant de revenir aux réels.',
    'Spé : multiplicité d’une racine, factorisation et étude de tangence ; calcul algébrique certifié sur un exemple.',
    'Théorème de Bézout pour les courbes projectives et multiplicité d’intersection : prolongement explicitement séparé.',
    ['Choisir r=1,h=9/8 et retrouver quatre abscisses réelles.','Choisir r=1,h=5/4 : montrer que les deux intersections sont tangentes.','Choisir r=h=1/2 : comparer un point géométrique et quatre racines comptées avec multiplicité.'],
    'Un dessin peut montrer zéro, un, deux ou quatre points réels ; le total algébrique reste quatre avec les bonnes conventions.')
lesson('intersection_bezout','Éliminer une variable avant de dessiner','Sup · résolution',
    '<p>Le cercle x²+y²=r² et la parabole y=x²−h dépendent de r>0 et h réels. Substituer la seconde équation dans la première donne Q(x)=x⁴+(1−2h)x²+h²−r²=0.</p><p>Avec t=x², on résout t²+(1−2h)t+h²−r²=0, de discriminant D=1−4h+4r². Pour obtenir des points réels, t doit être réel et non négatif. Si t>0, il donne deux abscisses ±√t ; si t=0, il n’en donne qu’une. Si t est négatif ou non réel, ses racines carrées appartiennent à ℂ et restent pertinentes pour le comptage algébrique.</p>')
lesson('intersection_bezout','Bézout : compter au bon endroit et avec multiplicité','Au-delà · géométrie algébrique',
    '<p>Deux courbes projectives complexes de degrés d et e sans composante commune ont d×e intersections, comptées avec multiplicité. Le mot « projectives » inclut les points à l’infini ; le mot « complexes » inclut ceux que le dessin réel ne montre pas.</p><p>Ici, les équations homogènes sont X²+Y²−r²Z²=0 et YZ−X²+hZ²=0. À Z=0, la seconde impose X=0, puis la première Y=0 : aucun triplet projectif non nul n’est solution. Toutes les intersections sont donc affines. Comme y est imposé par x, on peut les compter par le quartique Q. À r=h=1/2, Q=x⁴ : un seul point (0,−1/2) porte la multiplicité quatre.</p>')
exercise('intersection_bezout','Trois points, quatre multiplicités','Sup',
    'Déterminer les intersections réelles de x²+y²=1 et y=x²−1.',
    'Q=x⁴−x²=x²(x²−1). Les abscisses sont 0 (multiplicité 2),1 et −1 (multiplicité 1). Les points distincts sont (0,−1),(1,0),(−1,0). Leur multiplicité totale vaut 4. Le cercle et la parabole sont tangents en (0,−1).')
exercise('intersection_bezout','Deux points, deux tangences','Spé',
    'Prendre r=1 et h=5/4. Déterminer les intersections et vérifier la tangence par les dérivées des équations.',
    'Q=x⁴−(3/2)x²+9/16=(x²−3/4)². Les points sont (±√3/2,−1/2), chacun de multiplicité 2. Sur le cercle, 2x+2y y′=0 donne y′=−x/y=2x ; sur la parabole, y′=2x. Les pentes coïncident.')
exercise('intersection_bezout','Le réel ne montre pas tout','Sup / Au-delà',
    'Prendre r=1 et h=−2. Montrer qu’il n’y a aucun point réel commun, puis conserver les quatre solutions algébriques.',
    'Pour x réel, y=x²+2≥2 tandis que le cercle impose |y|≤1 : aucune solution réelle. Q=x⁴+5x²+3. Ses valeurs de t=x² sont (−5±√13)/2, toutes deux négatives. Chacune donne deux racines imaginaires non nulles en x ; y=t+2. Les quatre points complexes sont distincts.')

guide('resultant_elimination','Comprendre pourquoi une élimination fournit des candidats et non toujours des solutions.',
    ['x,y sont les indéterminées ; a,b sont des paramètres réels sans unité. Les équations sont F=(x−a)y−1=0 et G=(x−a)(y−b)=0.', 'R(x)=Résᵧ(F,G) est le résultant par rapport à y : le déterminant de Sylvester des deux expressions affines en y.', 'Le coefficient dominant de F en y est x−a ; il s’annule pour x=a. La fibre au-dessus d’une abscisse x₀ signifie les solutions obtenues en fixant x=x₀.', 'Si b≠0, le point réellement commun est (a+1/b,b). Le champ représente F et les droites représentent G.'],
    ['Les coefficients des réglages sont traités comme rationnels exacts.','La projection sur l’axe x peut introduire un candidat parasite lors d’une chute de degré en y.'],
    ['Déterminant de Sylvester','Factorisation','Substitution dans les équations initiales','Discussion b=0 / b≠0'],
    'Sup : résoudre un système par substitution et distinguer implication et équivalence.',
    'Spé : déterminants, polynômes et racines communes ; retrouver le résultant dans un cas élémentaire.',
    'Élimination algébrique, fibres projectives et spécialisation des degrés : prolongements.',
    ['Prendre a=0,b=1 et trouver les deux zéros du résultant.','Substituer x=0 dans F : expliquer pourquoi ce zéro est rejeté.','Annuler b : le résultant est-il nul ? Existe-t-il encore un point commun ?'],
    'Un candidat d’élimination doit être vérifié dans chaque équation de départ ; sinon une solution fictive peut être retenue.')
lesson('resultant_elimination','Un déterminant qui élimine y','Spé · déterminants',
    '<p>Pour F=A(x)y+B(x) et G=C(x)y+D(x), le résultant en y est R(x)=A(x)D(x)−B(x)C(x). Tout point commun (x₀,y₀) annule ce déterminant, car les deux lignes ont un même vecteur (y₀,1) dans leur noyau.</p><p>Dans le laboratoire, A=C=x−a, B=−1 et D=−b(x−a). Ainsi R=(x−a)[1−b(x−a)]. Si b≠0, les abscisses candidates sont x=a et x=a+1/b. Le second candidat fournit y=b et une véritable solution ; le premier exige une vérification séparée.</p>')
lesson('resultant_elimination','Le candidat parasite vient d’une chute de degré','Spé / Au-delà · vigilance algébrique',
    '<p>À x=a, les coefficients de y dans F et G s’annulent. Les équations spécialisées deviennent F=−1 et G=0 : aucun y ne peut satisfaire F=0. Pourtant R(a)=0. Le déterminant détecte la singularité des coefficients, mais cette singularité n’est pas ici un point affine commun.</p><p>Pour b=0, G=(x−a)y. Sur F=0, on a (x−a)y=1, donc G=1≠0. Le système n’a aucune solution affine, alors que R=x−a possède un zéro. La règle pratique est de conserver les zéros du résultant comme candidats, puis de revenir aux équations initiales. Cette précaution est aussi essentielle lorsqu’on divise une équation par une expression qui peut s’annuler.</p>')
exercise('resultant_elimination','Un système avec un candidat rejeté','Spé',
    'Résoudre (x−2)y−1=0 et (x−2)(y+1)=0 par résultant, en vérifiant chaque abscisse.',
    'Ici a=2,b=−1. Le résultant vaut (x−2)[1+(x−2)]=(x−2)(x−1). Pour x=2, F=−1 : rejet. Pour x=1, F=−y−1 donne y=−1, qui vérifie G=0. L’unique solution est (1,−1).')
exercise('resultant_elimination','Détecter une contradiction sans calcul lourd','Sup',
    'Montrer que xy=1 et xy=0 n’ont pas de solution, tout en calculant leur résultant par rapport à y.',
    'La contradiction 1=0 suffit. Pour F=xy−1 et G=xy, le déterminant des coefficients en y vaut x×0−(−1)×x=x. Son zéro x=0 est parasite puisque F(0,y)=−1. Un résultant non constant ne prouve donc pas à lui seul l’existence d’un point affine commun.')
exercise('resultant_elimination','Quand la vérification devient suffisante','Spé',
    'Pour F=A(x)y+B(x), G=C(x)y+D(x), supposer A(x₀)≠0 et R(x₀)=0. Prouver qu’un unique y₀ satisfait les deux équations.',
    'F impose y₀=−B(x₀)/A(x₀). Alors G(x₀,y₀)=[A(x₀)D(x₀)−B(x₀)C(x₀)]/A(x₀)=R(x₀)/A(x₀)=0. L’unicité vient de A(x₀)≠0. La chute de degré qui créait le candidat parasite est ainsi exclue par une hypothèse précise.')

guide('groebner_ordre','Prolonger la division euclidienne en choisissant un ordre des monômes et en contrôlant les restes.',
    ['F=xy−1 et G=y²−x−c sont des polynômes en x,y ; c est un entier réglable. I=(F,G) est l’idéal de leurs combinaisons polynomiales AF+BG.', 'Un ordre des monômes précise le terme dominant utilisé pour diviser. « Lex » compare d’abord l’exposant de x ; « degré / lex inverse » compare d’abord le degré total.', 'Une base de Gröbner est une famille qui permet de tester l’appartenance à I par un reste nul. Un S-polynôme annule les termes dominants de deux éléments de la base.', 'Le quotient ℝ[x,y]/I identifie deux polynômes lorsque leur différence appartient à I. Sa base de monômes est indiquée par la table.'],
    ['Deux ordres admissibles fixés ; calcul exact des bases et des divisions.','Toutes les solutions complexes sont finies en nombre ; leur multiplicité totale vaut la dimension 3 du quotient.'],
    ['Combinaisons polynomiales','Division avec un ordre des monômes','Élimination','Contrôle des S-polynômes'],
    'Sup : substitution, divisibilité et opérations sur les polynômes ; aucun préalable sur les idéaux n’est requis pour les premiers essais.',
    'Spé : algèbre linéaire dans un quotient et calcul exact ; comparer des bases de monômes.',
    'Bases de Gröbner, critère de Buchberger et dimension d’une algèbre quotient : notions au-delà du programme.',
    ['Choisir lex et retrouver x=y²−c, puis y³−cy−1=0.','Passer en degré / lex inverse sans changer c : comparer les trois termes dominants.','Prendre c=3 et vérifier les trois points réels ; contrôler que chaque S-polynôme a un reste nul.'],
    'L’ordre change les étapes du calcul et les représentants du quotient ; il ne change ni l’idéal ni l’ensemble des solutions.')
lesson('groebner_ordre','L’ordre lexicographique expose une substitution','Au-delà · division accompagnée',
    '<p>Un idéal I=(F,G) est l’ensemble des AF+BG, où A,B sont des polynômes. Pour F=xy−1 et G=y²−x−c, on pose g₁=x−y²+c=−G et g₂=y³−cy−1=yG+F.</p><p>Réciproquement, G=−g₁ et F=g₂+yg₁. Les deux familles engendrent donc exactement le même idéal. Avec l’ordre lexicographique x avant y, les termes dominants sont x et y³. Les solutions se calculent par g₂(y)=0 puis x=y²−c. Les monômes non divisibles par x ou y³ sont 1,y,y² : ils donnent une base du quotient, de dimension 3.</p>')
lesson('groebner_ordre','Trois divisions au lieu de deux : le critère qui certifie','Au-delà · certificats',
    '<p>Avec un ordre qui compare d’abord le degré total, la base devient H=x²+cx−y, F=xy−1 et G=y²−x−c. L’identité H=yF−xG prouve que ce nouvel élément appartient au même idéal. Les termes dominants sont x²,xy,y².</p><p>Un S-polynôme multiplie deux éléments pour rendre leurs termes dominants identiques, puis les soustrait. Le critère de Buchberger affirme qu’une famille est une base de Gröbner lorsque tous ces S-polynômes ont un reste nul par division dans la famille. Le laboratoire affiche ces restes exacts. Les monômes restants sont alors 1,x,y : une autre base du même quotient de dimension 3.</p>')
exercise('groebner_ordre','Certifier l’égalité des idéaux','Spé / Au-delà',
    'Avec F=xy−1, G=y²−x−c, g₁=x−y²+c et g₂=y³−cy−1, donner les quatre identités qui prouvent (F,G)=(g₁,g₂).',
    'g₁=−G et g₂=yG+F donnent (g₁,g₂)⊂(F,G). Inversement, G=−g₁ et F=g₂+yg₁ donnent (F,G)⊂(g₁,g₂). Il faut les deux inclusions : produire de nouveaux polynômes dans l’idéal ne prouve pas seul qu’ils l’engendrent.')
exercise('groebner_ordre','Un calcul matriciel dans le quotient','Au-delà · algèbre linéaire',
    'Prendre c=0. Dans la base (1,y,y²) du quotient, écrire la matrice de la multiplication par y et son polynôme caractéristique.',
    'La relation est y³=1. Les images sont y, y², 1, donc la matrice, par colonnes, est [[0,0,1],[1,0,0],[0,1,0]]. Son polynôme caractéristique est T³−1. Les trois solutions complexes en y sont les racines cubiques de l’unité ; x=y².')
exercise('groebner_ordre','Un S-polynôme contrôlable à la main','Au-delà · technique',
    'Avec H=x²+cx−y et F=xy−1, calculer S=yH−xF. Montrer qu’il se réduit à zéro par H,F,G où G=y²−x−c.',
    'S=cxy−y²+x=c(xy−1)−(y²−x−c)=cF−G. Son reste est donc nul en retirant cF puis −G. Cette identité est un certificat explicite, indépendant d’une inspection du dessin.')

guide('symetriques','Passer des racines aux coefficients puis aux sommes de puissances, sans perdre l’invariance par permutation.',
    ['u,v,w sont trois racines réelles réglables. T est l’indéterminée du polynôme P(T)=(T−u)(T−v)(T−w).', 'e₁=u+v+w, e₂=uv+uw+vw et e₃=uvw sont les fonctions symétriques élémentaires.', 'pₖ=uᵏ+vᵏ+wᵏ est la somme des puissances d’ordre k. D=(u−v)²(u−w)²(v−w)² est le discriminant.', 'Le champ est dessiné dans le plan des coefficients (e₂,e₃), avec e₁ fixé ; il ne représente pas le plan des racines. Tous les nombres sont sans unité.'],
    ['Les racines choisies sont réelles ; les identités sont valables aussi pour des racines complexes.','Les tableaux utilisent des rationnels exacts, tandis que les courbes affichent des approximations.'],
    ['Relations coefficients–racines','Identités de Newton','Récurrence','Discriminant et racines multiples'],
    'Sup : développer un produit, factoriser et relier coefficients et racines.',
    'Spé : sommes de puissances, traces et polynôme caractéristique ; calculer sans diagonaliser.',
    'Théorème fondamental des polynômes symétriques et géométrie du discriminant : prolongements.',
    ['Choisir trois racines distinctes et reconstruire P avant de lire le graphique.','Permuter u,v,w : contrôler l’invariance des coefficients et des sommes pₖ.','Faire coïncider deux racines ; observer D=0 et la position dans le plan des coefficients.'],
    'Les coefficients symétriques regroupent toute l’information utile pour les sommes de puissances ; le discriminant repère la collision des racines.')
lesson('symetriques','Newton retrouve les puissances à partir des coefficients','Sup / Spé · identités',
    '<p>Pour trois nombres u,v,w, on définit e₁=u+v+w, e₂=uv+uw+vw, e₃=uvw et pₖ=uᵏ+vᵏ+wᵏ. Le polynôme associé est P(T)=T³−e₁T²+e₂T−e₃.</p><p>Les premières identités sont p₁=e₁, p₂=e₁p₁−2e₂ et p₃=e₁p₂−e₂p₁+3e₃. Chaque racine α vérifie α³=e₁α²−e₂α+e₃. Multiplier par αᵏ⁻³ puis sommer donne, pour k≥4, pₖ=e₁pₖ₋₁−e₂pₖ₋₂+e₃pₖ₋₃. On calcule donc les grandes puissances sans expliciter les racines d’une équation cubique.</p>')
lesson('symetriques','Le discriminant décrit les collisions de racines','Spé · racines multiples',
    '<p>Le discriminant de P(T)=T³−e₁T²+e₂T−e₃ est D=e₁²e₂²−4e₂³−4e₁³e₃−27e₃²+18e₁e₂e₃. Si u,v,w sont ses racines, D=(u−v)²(u−w)²(v−w)². D=0 équivaut donc à une racine multiple.</p><p>Pour des coefficients réels, D>0 correspond à trois racines réelles distinctes et D&lt;0 à une racine réelle et deux racines complexes conjuguées. À e₁ fixé, la courbe D(e₂,e₃)=0 sépare ces régions dans le plan des coefficients. Le point du laboratoire reste du côté D≥0, car les trois racines réglées sont réelles. Ce choix ne limite pas la validité des identités algébriques.</p>')
exercise('symetriques','Calculer une somme sans résoudre une cubique','Spé',
    'Soient α,β,γ les racines complexes de T³−3T²+2T−1. Calculer α²+β²+γ² puis α⁴+β⁴+γ⁴.',
    'e₁=3,e₂=2,e₃=1. p₁=3, p₂=9−4=5, p₃=3×5−2×3+3=12. Ensuite p₄=3×12−2×5+1×3=29. Aucune résolution explicite de la cubique n’est nécessaire.')
exercise('symetriques','Une expression symétrique qui n’est pas une puissance','Sup / Spé',
    'Exprimer (u−v)²+(v−w)²+(w−u)² en e₁=u+v+w et e₂=uv+uw+vw.',
    'La somme vaut 2(u²+v²+w²)−2(uv+uw+vw)=2p₂−2e₂=2e₁²−6e₂. Pour u,v,w réels, elle est non négative ; on retrouve e₁²≥3e₂, avec égalité si et seulement si u=v=w.')
exercise('symetriques','Des traces sans diagonalisation','Spé · algèbre linéaire',
    'Une matrice A de taille 3 a polynôme caractéristique T³−3T²+2T−1. Calculer tr(A²) et tr(A⁴), même si A n’est pas diagonalisable.',
    'Sur ℂ, A est triangulisable : la diagonale de Aᵏ contient αᵏ,βᵏ,γᵏ, avec multiplicité. Ainsi tr(Aᵏ)=pₖ, sans hypothèse de diagonalisation. Newton donne tr(A²)=5 et tr(A⁴)=29. Les mêmes valeurs se retrouvent en utilisant Cayley–Hamilton et les premières traces.')

guide('singularites','Distinguer trois formes de courbe au voisinage d’un point où le gradient s’annule.',
    ['x,y sont les coordonnées réelles. Fₜ(x,y)=y²−x³−tx² définit la courbe Fₜ=0 ; t est un paramètre réel sans unité.', 'Le gradient est (∂F/∂x,∂F/∂y). Un point singulier satisfait F=0 et les deux dérivées nulles.', 'La partie homogène de plus bas degré est y²−tx². Elle détermine les directions tangentes candidates.', 'La hessienne à l’origine est diag(−2t,2). Les branches exactes sont y=±|x|√(x+t), lorsqu’elles sont réelles.'],
    ['La classification illustrée est locale à l’origine.','Les singularités sont vérifiées dans les équations, pas estimées par la couleur du maillage.'],
    ['Gradient et dérivées partielles','Factorisation de la partie quadratique','Hessienne','Étude locale et signe'],
    'Sup : courbes, factorisation et racine carrée ; examiner les branches sans vocabulaire géométrique avancé.',
    'Spé : dérivées partielles, gradient, hessienne et approximation locale dans les filières concernées.',
    'Singularités des courbes algébriques, cône tangent et multiplicité locale : prolongements.',
    ['Prendre t=1 : retrouver les deux droites tangentes en factorisant y²−x².','Annuler t : expliquer pourquoi une seule tangente ne suffit pas à obtenir une branche régulière.','Prendre t=−1 : prouver que l’origine est isolée à l’aide du signe de x−1.'],
    'Le gradient nul signale un point à examiner ; la partie homogène et le signe distinguent nœud, pointe et point isolé.')
lesson('singularites','Le gradient seul ne classe pas une singularité','Spé · calcul différentiel',
    '<p>La courbe Fₜ(x,y)=y²−x³−tx²=0 a gradient (−3x²−2tx,2y). Une singularité vérifie Fₜ=0 et ∇Fₜ=0. L’origine est toujours singulière.</p><p>Le gradient propose aussi (−2t/3,0), mais Fₜ en ce point vaut −4t³/27 : il n’est sur la courbe que pour t=0, où il coïncide avec l’origine. Il est donc essentiel de vérifier l’équation de la courbe. La hessienne à l’origine est diag(−2t,2) ; son déterminant −4t distingue les signatures quadratiques, sans décrire à lui seul le cas dégénéré t=0.</p>')
lesson('singularites','Trois signes, trois dessins','Spé / Au-delà · géométrie locale',
    '<p>Pour t>0, y²−tx²=(y−√t x)(y+√t x) : deux tangentes réelles distinctes passent par l’origine, qui est un nœud. Pour t=0, y²=x³ impose x≥0 et y=±x³ᐟ² : la pointe a une tangente double y=0.</p><p>Pour t&lt;0, l’équation y²=x²(x+t) ne possède aucune solution avec 0&lt;|x|&lt;|t|. L’origine est donc isolée dans la courbe réelle, même si une branche existe plus loin pour x≥|t|. Le terme quadratique y²+|t|x² est positif hors de l’origine. Cette preuve de signe est plus sûre qu’un zoom sur une image.</p>')
exercise('singularites','Écarter un faux point singulier','Spé',
    'Pour F=y²−x³−2x², résoudre ∇F=0 puis déterminer les points singuliers de F=0.',
    '∂F/∂y=2y impose y=0 ; ∂F/∂x=−x(3x+4) impose x=0 ou x=−4/3. Au second candidat F=−32/27≠0. Seule l’origine est singulière sur la courbe. Les tangentes y=±√2 x sont distinctes.')
exercise('singularites','Une pointe paramétrée sans racine carrée','Sup / Spé',
    'Pour y²=x³, donner un paramétrage polynomial couvrant toute la courbe réelle et expliquer le comportement de sa vitesse à l’origine.',
    'x=s²,y=s³, s∈ℝ, vérifie l’équation et couvre la courbe réelle : pour x>0, s=y/x. La vitesse vaut (2s,3s²), donc s=0 donne le vecteur nul. Le quotient y/x=s tend vers 0, ce qui montre la tangente y=0, mais le paramétrage n’est pas régulier à l’origine.')
exercise('singularites','Un point isolé démontré par une boule','Spé',
    'Pour t=−1, montrer que la boule ouverte de rayon 1/2 centrée à l’origine ne contient aucun autre point de y²=x²(x−1).',
    'Dans cette boule, |x|<1/2. Si x≠0, x−1<0 et x²(x−1)<0, impossible pour y²≥0. Si x=0, l’équation donne y=0. La seule intersection avec la boule est donc l’origine. Cela établit l’isolement au sens topologique.')

guide('homogenisation','Comprendre les points à l’infini par un changement explicite de coordonnées, sans les assimiler à de grands nombres.',
    ['X,Y,Z sont trois coordonnées homogènes. [X:Y:Z] désigne un triplet non nul modulo multiplication par un scalaire commun non nul.', 'Dans la carte Z≠0, x=X/Z et y=Y/Z sont les coordonnées usuelles. Dans la carte Y≠0, u=X/Y et v=Z/Y sont les coordonnées affichées.', 'c>0 est un paramètre sans unité. Les équations sont y−x²−c=0 ou xy−c=0 ; leurs homogénéisations sont YZ−X²−cZ² et XY−cZ².', 'Un point à l’infini de la carte usuelle satisfait Z=0. Dans la carte Y≠0, sa position suit donc v=0.'],
    ['Équations homogènes de degré 2 ; courbes non dégénérées dans la plage c>0.','Une carte ne contient pas tous les points projectifs. Le point [1:0:0] exige notamment Y=0 et échappe à la carte Y≠0.'],
    ['Homogénéiser par les degrés','Substitution','Rapports de coordonnées','Vérification des points avec Z=0'],
    'Sup : monômes homogènes et changements de variables par substitution.',
    'Spé : coordonnées, espaces quotient et équations de coniques ; outils algébriques à réinvestir.',
    'Plan projectif et cartes affines : prolongement au-delà des programmes CPGE.',
    ['Homogénéiser y−x²−c, puis poser Z=0 pour trouver [0:1:0].','Passer dans la carte Y≠0 : retrouver ce point en (u,v)=(0,0).','Choisir xy=c ; trouver les deux points à l’infini et dire lequel est absent de cette carte.'],
    'Une courbe reste la même, mais ses coordonnées changent ; un point à l’infini d’une carte peut être un point ordinaire d’une autre.')
lesson('homogenisation','Tous les monômes doivent avoir le même degré','Sup / Au-delà · coordonnées',
    '<p>Pour homogénéiser un polynôme affine de degré d, on remplace x,y par X,Y puis on multiplie chaque monôme de degré k par Zᵈ⁻ᵏ. Ainsi y−x²−c devient YZ−X²−cZ², de degré homogène 2.</p><p>Un point projectif [X:Y:Z] est un triplet non nul considéré à multiplication commune près. Dans la carte Z≠0, on peut normaliser Z=1 et retrouver les coordonnées x=X/Z,y=Y/Z. Les points Z=0 sont à l’infini de cette carte. Pour la parabole, Z=0 impose X=0, donnant l’unique point [0:1:0]. Aucun symbole ∞ n’est utilisé comme un nombre.</p>')
lesson('homogenisation','Une deuxième carte explique le point à l’infini','Au-delà · géométrie projective',
    '<p>Dans la carte Y≠0, on pose u=X/Y et v=Z/Y, donc on peut normaliser Y=1. La parabole homogène devient v−u²−cv²=0. Son point [0:1:0] est maintenant représenté par (u,v)=(0,0). La droite v=0 est la droite à l’infini de l’ancienne carte Z≠0.</p><p>Pour l’hyperbole xy=c, l’équation homogène XY−cZ²=0 possède à Z=0 les deux points [1:0:0] et [0:1:0]. Dans la carte Y≠0, l’équation est u−cv²=0 et seul le second point est visible. Il faut la carte X≠0 pour voir le premier : cela évite de prendre une carte pour tout le plan projectif.</p>')
exercise('homogenisation','Une conique et ses points à l’infini','Sup / Au-delà',
    'Homogénéiser x²+2xy+3y²−1=0. Chercher ses points à l’infini réels puis complexes.',
    'L’équation est X²+2XY+3Y²−Z²=0. À Z=0, X²+2XY+3Y²=(X+Y)²+2Y² : aucun point projectif réel. Sur ℂ, Y≠0 et X/Y=−1±i√2. Les deux points complexes à l’infini sont [−1+i√2:1:0] et [−1−i√2:1:0].')
exercise('homogenisation','Retrouver la transition entre cartes','Spé / Au-delà',
    'Un point affine de la parabole y=x²+c a y≠0. Exprimer ses coordonnées u,v dans la carte Y≠0 et vérifier v−u²−cv²=0.',
    'Le point s’écrit [x:y:1], donc u=x/y et v=1/y. Alors v−u²−cv²=(y−x²−c)/y²=0. Inversement, si v≠0, x=u/v et y=1/v. Le point (u,v)=(0,0) ne peut pas revenir dans la carte affine, car la transition diviserait par v=0.')
exercise('homogenisation','Une droite et une parabole','Spé / Au-delà',
    'Montrer que la droite y=mx+b n’a aucun point commun à l’infini avec y=x²+c, puis expliquer pourquoi leur nombre complexe d’intersections avec multiplicité vaut deux.',
    'La droite homogène est Y−mX−bZ=0 ; la parabole à l’infini possède seulement [0:1:0], qui ne satisfait pas la droite. En affine, x²−mx+(c−b)=0 est une équation monique de degré 2, donc deux racines complexes avec multiplicité. Le cas de discriminant nul est une tangence.')

guide('formes_quadratiques','Classer une forme en trois variables à partir d’une matrice symétrique et comparer cette classification à une tranche plane.',
    ['x,y,z sont trois variables réelles. Q=x²+y²+bz²+2axy+2cyz ; a,b,c sont des coefficients réels sans unité.', 'A est la matrice symétrique [[1,a,0],[a,1,c],[0,c,b]], telle que Q(v)=vᵀAv pour v=(x,y,z). La hessienne de Q vaut 2A.', 'λ₁,λ₂,λ₃ sont les valeurs propres de A. La signature compte les valeurs positives, négatives et nulles.', 'Δ₁,Δ₂,Δ₃ sont les mineurs principaux successifs. Le champ ne représente que la tranche z=z₀, où z₀ est le réglage « valeur de la tranche ».'],
    ['Matrice symétrique réelle : une base orthonormée de vecteurs propres existe.','La classification numérique des signes utilise une tolérance de 10⁻¹⁰. Les formules des mineurs restent explicites.'],
    ['Déterminant','Théorème spectral','Critère de Sylvester','Hessienne et tranches'],
    'Sup : matrice d’une expression quadratique, déterminant et complétion des carrés.',
    'Spé : théorème spectral pour les matrices symétriques ; extrema et hessienne dans les programmes concernés.',
    'Signature et critère général de Sylvester peuvent être traités comme compléments ; distinguer stricte positivité et semi-définition.',
    ['Prendre a=c=0,b=2 et prévoir les trois valeurs propres.','Prendre a=3/2 : montrer une direction négative dans le plan z=0.','Fixer a=1,b=c=0 puis comparer le noyau de Q aux directions propres nulles.'],
    'Le signe des valeurs propres classe Q dans tout ℝ³ ; une tranche isolée peut masquer une direction nulle ou négative.')
lesson('formes_quadratiques','La matrice symétrique et ses valeurs propres','Spé · théorème spectral',
    '<p>Pour v=(x,y,z), la forme Q=x²+y²+bz²+2axy+2cyz s’écrit vᵀAv avec A=[[1,a,0],[a,1,c],[0,c,b]]. Les termes croisés sont doublés parce que les deux positions symétriques de A contribuent.</p><p>Le théorème spectral donne une base orthonormée dans laquelle Q=λ₁u₁²+λ₂u₂²+λ₃u₃². Toutes les valeurs propres positives signifient Q(v)>0 pour v≠0. Des valeurs de signes opposés rendent Q indéfinie. Des valeurs nulles exigent de distinguer semi-définition et indéfinition. Une tranche z=z₀ peut représenter des niveaux fermés même lorsqu’une autre direction de ℝ³ est négative.</p>')
lesson('formes_quadratiques','Sylvester et complétion des carrés','Spé · complément formateur',
    '<p>Les mineurs principaux successifs sont Δ₁=1, Δ₂=1−a² et Δ₃=b(1−a²)−c². Le critère de Sylvester affirme que A est définie positive si et seulement si Δ₁,Δ₂,Δ₃ sont strictement positifs.</p><p>On peut vérifier le critère dans cette famille sans le supposer : Q=(x+ay)²+(1−a²)y²+2cyz+bz². Si 1−a²>0, compléter encore donne Q=(x+ay)²+(1−a²)(y+cz/(1−a²))²+[b−c²/(1−a²)]z². Les trois carrés ont des coefficients strictement positifs exactement lorsque Δ₂>0 et Δ₃>0. Au bord Δ₂=0, cette écriture divisant par Δ₂ n’est plus valable.</p>')
exercise('formes_quadratiques','Une preuve exacte de positivité','Spé',
    'Prendre a=1/2,b=2,c=1/2. Prouver que Q est définie positive et donner une décomposition en carrés.',
    'Δ₂=3/4 et Δ₃=2×3/4−1/4=5/4>0. La complétion donne Q=(x+y/2)²+(3/4)(y+2z/3)²+(5/3)z². Tous les coefficients sont positifs ; Q ne s’annule qu’en (0,0,0).')
exercise('formes_quadratiques','Une direction négative suffit','Sup / Spé',
    'Prendre a=3/2,b=2,c=1/2. Sans calculer les valeurs propres, montrer que Q est indéfinie.',
    'Q(1,0,0)=1>0. Avec z=0 et x=−y=1, Q=1+1+2×(3/2)×(−1)=−1<0. Deux vecteurs donnant des signes opposés suffisent à prouver l’indéfinition. Le déterminant seul ne fournirait pas cette conclusion dans tous les cas.')
exercise('formes_quadratiques','Déterminer le noyau sur un bord','Spé',
    'Pour a=1,b=c=0, classer Q et déterminer son lieu d’annulation. Une tranche z=0 suffit-elle à voir tout ce lieu ?',
    'Q=(x+y)², donc semi-définie positive. Son lieu d’annulation est le plan x+y=0, avec z arbitraire. A a valeurs propres 2,0,0 et un noyau de dimension 2. La tranche z=0 ne montre que la droite x+y=0 ; elle masque la seconde direction nulle.')

guide('positivite_motzkin','Prouver un signe sur tout le plan et distinguer ce signe d’une représentation en carrés de polynômes.',
    ['x,y sont deux variables réelles. Mλ=x⁴y²+x²y⁴−λx²y²+1 ; λ∈[0,4] est le paramètre sans unité.', 't=|xy|≥0 est une variable auxiliaire de la preuve ; elle n’est pas une troisième indéterminée.', '« Non négatif » signifie Mλ(x,y)≥0 pour tout couple réel. Une somme de carrés polynomiaux est une expression ∑qᵢ(x,y)² avec qᵢ à coefficients réels.', 'Le minimum global est 1−λ³/27. Pour λ>0, il est atteint aux quatre points x,y=±√(λ/3), marqués sur le champ.'],
    ['Le signe est démontré par inégalités exactes, et non conclu d’un échantillonnage.','Les sommes de carrés considérées ne contiennent aucun dénominateur ; les sommes de carrés de fractions rationnelles sont un autre problème.'],
    ['Inégalité arithmético-géométrique','Réduction à une fonction d’une variable','Degré dominant','Comparaison des coefficients'],
    'Sup : inégalités, dérivation et étude d’un polynôme d’une variable après une substitution judicieuse.',
    'Spé : minimum global, forme dominante et raisonnement par les coefficients ; relier à la positivité des formes quadratiques.',
    'Polynôme de Motzkin et problème des sommes de carrés : complément au-delà du programme.',
    ['Prendre λ=0 et écrire les trois carrés visibles.','Prendre λ=3 ; prouver Mλ≥0 puis trouver les quatre zéros.','Prendre λ=4 ; calculer Mλ(1,1) et retrouver le minimum indiqué.'],
    'La positivité d’un polynôme multivarié ne donne pas automatiquement une somme de carrés polynomiaux ; le contre-exemple est démontré par coefficients.')
lesson('positivite_motzkin','Un minimum global démontré sur tout ℝ²','Sup / Spé · inégalités',
    '<p>Pour Mλ=x⁴y²+x²y⁴−λx²y²+1, poser t=|xy|≥0. L’inégalité arithmético-géométrique donne x⁴y²+x²y⁴≥2t³. Ainsi Mλ≥2t³−λt²+1, avec égalité lorsque |x|=|y|.</p><p>Pour λ≥0, la dérivée de cette dernière fonction est 2t(3t−λ). Son minimum sur t≥0 vaut 1−λ³/27, atteint en t=λ/3. Lorsque λ>0, les quatre points x,y=±√(λ/3) réalisent l’égalité. Le polynôme est donc non négatif pour 0≤λ≤3, strictement positif pour 0≤λ&lt;3, et possède des valeurs négatives pour λ>3. À λ=3, ses seuls zéros sont (±1,±1).</p>')
lesson('positivite_motzkin','Le coefficient négatif interdit toute somme de carrés','Au-delà · contre-exemple de Motzkin',
    '<p>À λ=0, M₀=(x²y)²+(xy²)²+1². Pour λ>0, supposons Mλ=∑qᵢ². La partie homogène dominante d’une somme de carrés ne peut se compenser, donc chaque qᵢ a degré au plus 3.</p><p>Le coefficient nul de x⁶ impose l’absence de x³ dans chaque qᵢ ; celui de y⁶ impose l’absence de y³. Les coefficients nuls de x⁴,y⁴ imposent ensuite l’absence de x²,y², puis ceux de x²,y² l’absence de x,y. Il reste qᵢ=Aᵢ+Bᵢxy+Cᵢx²y+Dᵢxy². Le coefficient de x²y² dans ∑qᵢ² serait ∑Bᵢ²≥0, mais il vaut −λ. Contradiction. Pour 0&lt;λ≤3, on dispose donc d’un polynôme non négatif qui n’est pas une somme de carrés de polynômes réels.</p>')
exercise('positivite_motzkin','Une preuve en trois termes','Sup',
    'Prouver x⁴y²+x²y⁴+1≥3x²y² pour tous x,y réels et déterminer les cas d’égalité.',
    'Appliquer l’inégalité arithmético-géométrique aux trois termes non négatifs A=x⁴y²,B=x²y⁴,C=1. Leur produit vaut x⁶y⁶, donc (ABC)¹ᐟ³=x²y². L’égalité exige A=B=C=1, d’où |x|=|y|=1. Les quatre couples (±1,±1) réalisent l’égalité.')
exercise('positivite_motzkin','Un minimum exact, pas seulement un contre-exemple','Spé',
    'Pour λ=4, calculer le minimum global de Mλ et tous les points où il est atteint. Comparer avec la valeur en (1,1).',
    'Le minimum est 1−4³/27=−37/27, réalisé en x,y=±√(4/3)=±2/√3. La valeur M₄(1,1)=−1 démontre déjà la non-positivité, mais n’est pas le minimum. L’égalité |x|=|y| dans la réduction et t=4/3 donnent exactement les quatre points minimisants.')
exercise('positivite_motzkin','Pourquoi l’analogie avec les quadratiques échoue','Spé / Au-delà',
    'Une forme quadratique réelle non négative est une somme de carrés de formes linéaires. Expliquer pourquoi ce fait ne se généralise pas à tous les polynômes de deux variables.',
    'Le théorème spectral diagonalise une matrice symétrique : Q=∑λᵢuᵢ², et λᵢ≥0 fournit des carrés (√λᵢuᵢ)². Le polynôme de Motzkin M₃ est de degré 6, non négatif par l’inégalité arithmético-géométrique, mais la comparaison des coefficients interdit M₃=∑qᵢ². La matrice d’une forme quadratique n’encode donc pas directement tous les degrés supérieurs.')

guide('lagrange_contrainte','Comparer deux méthodes exactes d’optimisation et voir comment les points stationnaires changent avec un paramètre.',
    ['f(x,y)=x⁴+y⁴+axy est la fonction à optimiser ; a est un coefficient réel et x,y sont réels, sans unité.', 'La contrainte g(x,y)=x²+y²−r²=0 est un cercle de rayon r>0. θ est l’angle en radians : x=r cosθ,y=r sinθ.', 'μ est le multiplicateur dans ∇f=μ∇g. La condition équivalente sur le cercle est d f(r cosθ,r sinθ)/dθ=0.', 's=sin(2θ) varie dans [−1,1]. Le seuil |a|=2r² est la valeur à laquelle certaines familles de points stationnaires se rejoignent.'],
    ['Le cercle est compact et non vide ; f est continue, donc possède un minimum et un maximum globaux.','Le gradient de g ne s’annule pas sur le cercle, ce qui autorise la condition de Lagrange.'],
    ['Compacité et existence des extrema','Paramétrage trigonométrique','Gradient et multiplicateur de Lagrange','Factorisation de la dérivée','Discussion d’un paramètre'],
    'Sup : trigonométrie, dérivation et extrema sur un intervalle ; le paramétrage suffit.',
    'Spé : gradient et extrema sous contrainte dans les filières concernées ; les preuves de bornes restent accessibles par une substitution.',
    'Bifurcations et extrema dégénérés : prolongements ; la condition stationnaire ne remplace pas la comparaison globale.',
    ['Prendre a=0,r=1 ; retrouver quatre axes et quatre diagonales stationnaires.','Choisir a=1 puis a=2 : identifier les points qui se rejoignent.','Choisir a=4 et comparer le minimum et le maximum calculés à ceux du paramétrage angulaire.'],
    'Le nombre de stationnaires varie, mais les bornes globales se calculent exactement en ramenant le problème à une parabole sur [−1,1].')
lesson('lagrange_contrainte','Le cercle rend les deux méthodes équivalentes','Spé · optimisation',
    '<p>Sur g(x,y)=x²+y²−r²=0 avec r>0, ∇g=2(x,y) ne s’annule pas. Tout extremum contraint de f=x⁴+y⁴+axy satisfait ∇f=μ∇g. Cette condition est nécessaire, mais il faut encore classer ou comparer les candidats.</p><p>Le paramétrage x=r cosθ,y=r sinθ ramène f à une fonction périodique. Sa dérivée est r²cos(2θ)[a−2r²sin(2θ)]. Les directions diagonales cos(2θ)=0 donnent toujours quatre candidats. La seconde famille sin(2θ)=a/(2r²) existe seulement pour |a|≤2r² ; elle donne quatre candidats distincts si l’inégalité est stricte. À l’égalité, elle rejoint deux des diagonales.</p>')
lesson('lagrange_contrainte','Une parabole donne les bornes globales','Sup / Spé · preuve par substitution',
    '<p>Poser s=sin(2θ)∈[−1,1]. Les identités cos⁴θ+sin⁴θ=1−s²/2 et cosθsinθ=s/2 donnent f=r⁴(1−s²/2)+(ar²/2)s. Cette fonction est une parabole concave de s.</p><p>Son minimum sur [−1,1] est donc à une extrémité : min f=r⁴/2−|a|r²/2. Son sommet est à s=a/(2r²). Si |a|≤2r², max f=r⁴+a²/8 ; sinon le maximum est à l’extrémité de même signe que a et vaut r⁴/2+|a|r²/2. Ces formules comparent tous les candidats d’un seul coup. Au seuil, la dérivée seconde peut s’annuler : un développement d’ordre 4 ou la concavité en s permet encore de classer l’extremum.</p>')
exercise('lagrange_contrainte','Huit candidats et deux bornes','Sup / Spé',
    'Optimiser x⁴+y⁴+xy sur x²+y²=1 et compter les points stationnaires.',
    'a=r=1. Les candidats satisfont cos(2θ)=0 ou sin(2θ)=1/2 : les deux familles fournissent huit points distincts. Avec s∈[−1,1], f=1−s²/2+s/2. Le minimum vaut 0, atteint lorsque s=−1, soit x=−y=±1/√2. Le maximum vaut 9/8, atteint lorsque s=1/2, soit xy=1/4 avec x²+y²=1 : quatre points.')
exercise('lagrange_contrainte','Une seconde dérivée nulle mais un maximum','Spé / Au-delà',
    'Pour a=2,r=1, examiner f sur le cercle au voisinage de θ=π/4. La dérivée seconde s’annule : peut-on conclure ?',
    'Avec s=sin(2θ), f=1−s²/2+s=3/2−(s−1)²/2. À θ=π/4+h, s=cos(2h)=1−2h²+O(h⁴), donc f=3/2−2h⁴+O(h⁶). C’est un maximum strict local, malgré la dérivée seconde nulle. L’écriture exacte fournit aussi le maximum global 3/2.')
exercise('lagrange_contrainte','Changer le rayon change le seuil','Spé',
    'Optimiser x⁴+y⁴+4xy sur x²+y²=4. Déterminer le nombre de points stationnaires et les valeurs extrêmes.',
    'r=2,a=4 : le seuil est 2r²=8 et |a|<8, donc huit stationnaires. Le minimum vaut r⁴/2−|a|r²/2=8−8=0 ; le maximum vaut r⁴+a²/8=16+2=18. Les maxima vérifient sin(2θ)=a/(2r²)=1/2, soit xy=1. Les minima vérifient x=−y=±√2.')
