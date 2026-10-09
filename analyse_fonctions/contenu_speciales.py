"""Cours, exercices corrigés et démarches expérimentales : huit fonctions-laboratoires."""
LESSONS = []
EXERCISES = []
GUIDES = {}


def lesson(lab, title, level, html):
    LESSONS.append(dict(lab=lab, title=title, level=level, html=html))


def exercise(lab, title, level, question, answer):
    EXERCISES.append(dict(lab=lab, title=title, level=level, question=question, answer=answer))


lesson('gamma_euler', 'Gamma : convergence, intégration par parties et factorielle', 'Sup → Spé', '''
<p>Une fonction définie par une intégrale impropre demande d’abord un domaine. Pour x réel, considérons Γ(x)=∫₀∞t^(x−1)e^(−t)dt. Au voisinage de 0, e^(−t) tend vers 1 : le critère des puissances donne la convergence si et seulement si x&gt;0. À l’infini, t^(x−1)e^(−t) est intégrable, car l’exponentielle décroissante domine toute puissance. Ainsi <b>le domaine de cette définition réelle est ]0,+∞[</b>.</p>
<p>Effectuer une intégration par parties sur [ε,T], avec u=tˣ et dv=e^(−t)dt. Le terme de bord tˣe^(−t) tend vers 0 aux deux extrémités lorsque x&gt;0. On obtient une relation fonctionnelle :</p>
<div class='formula'>Γ(x+1)=xΓ(x) ; Γ(1)=1 ; Γ(n)=(n−1)! pour n≥1.</div>
<p>Une singularité du noyau en 0 n’empêche pas son intégrabilité : pour x=1/2, le noyau se comporte comme 1/√t. Avec t=u², Γ(1/2)=2∫₀∞e^(−u²)du=√π. Les demi-entiers suivent alors la récurrence : Γ(3/2)=√π/2, Γ(5/2)=3√π/4.</p>
<p>Le curseur de troncature T fournit ∫₀ᵀ, pas Γ tout entière. Distinguer <b>erreur de troncature</b>, liée à la queue, et <b>erreur de quadrature</b>, liée à l’approximation numérique de l’intégrale finie. Lorsque x augmente, le maximum du noyau est en t=x−1 et une troncature courte peut manquer une grande partie de l’aire.</p>''')
lesson('gamma_euler', 'Dériver une intégrale à paramètre et comprendre la convexité', 'Spé · Prolongement', '''
<p>Fixons un compact [a,b] contenu dans ]0,+∞[. La dérivée en x du noyau vaut (ln t)t^(x−1)e^(−t). Pour t≤1, sa valeur absolue est majorée par |ln t|t^(a−1), intégrable ; pour t≥1, par (ln t)t^(b−1)e^(−t), également intégrable. Le théorème de dérivation sous le signe intégral donne, et le raisonnement se répète pour tout entier p :</p>
<div class='formula'>Γ^(p)(x)=∫₀∞(ln t)^p t^(x−1)e^(−t)dt.</div>
<p>En particulier Γ″(x)&gt;0, car le noyau est positif presque partout : Γ est strictement convexe. Une propriété plus forte est la convexité de ln Γ. Avec la densité wₓ(t)=t^(x−1)e^(−t)/Γ(x), le quotient Γ′/Γ est la moyenne de ln t et la dérivée seconde de ln Γ est sa variance.</p>
<div class='formula'>(ln Γ)″(x)=Γ″(x)/Γ(x)−[Γ′(x)/Γ(x)]²=Varₓ(ln t)&gt;0.</div>
<p>La <b>fonction digamma</b> ψ=Γ′/Γ se rencontre dans la dérivation de B(a,b). La relation Γ(x+1)=xΓ(x) donne ψ(x+1)=ψ(x)+1/x. Le théorème de Bohr–Mollerup caractérise Γ par Γ(1)=1, la récurrence et la convexité de ln Γ sur ]0,+∞[ ; ce théorème est un prolongement, pas une exigence de cours en sup. Les définitions sont précisées dans <a href='https://dlmf.nist.gov/5.2'>NIST DLMF, §5.2</a>.</p>''')
exercise('gamma_euler', 'Calculer une intégrale à paramètre sans primitive élémentaire', 'Sup → Spé',
    '<p>Pour a&gt;0, calculer I(a)=∫₀∞t^(3/2)e^(−at)dt. Préciser le changement de variable et les conditions de convergence.</p>',
    '<p>Le noyau est intégrable en 0 car 3/2&gt;−1, et à l’infini car a&gt;0. Poser u=at : dt=du/a et t^(3/2)=u^(3/2)/a^(3/2). Ainsi I(a)=Γ(5/2)/a^(5/2)=<b>3√π/(4a^(5/2))</b>. Il faut transformer à la fois la fonction et l’élément différentiel.</p>')
exercise('gamma_euler', 'Justifier une dérivation et obtenir une identité logarithmique', 'Spé',
    '<p>Pour x&gt;0, établir ∫₀∞(ln t)tˣe^(−t)dt=Γ(x)+xΓ′(x). Justifier la dérivation de la relation de récurrence.</p>',
    '<p>Sur tout compact positif, les noyaux avec ln t sont dominés séparément près de 0 et à l’infini. Γ est donc dérivable et Γ′(x+1)=∫₀∞(ln t)tˣe^(−t)dt. En dérivant Γ(x+1)=xΓ(x), on obtient <b>Γ′(x+1)=Γ(x)+xΓ′(x)</b>. Une identité fonctionnelle et un théorème d’analyse permettent de traiter une intégrale difficile.</p>')
exercise('gamma_euler', 'Un encadrement de la queue dans un cas entier', 'Sup → Spé',
    '<p>Évaluer exactement ∫ᵀ∞t³e^(−t)dt pour T&gt;0, puis en déduire l’erreur de troncature de Γ(4). Une quadrature exacte sur [0,T] suffirait-elle à supprimer cette erreur ?</p>',
    '<p>Trois intégrations par parties donnent <b>e^(−T)(T³+3T²+6T+6)</b>. Γ(4)=6 ; la différence entre 6 et l’intégrale tronquée est ce terme positif. Même une intégration parfaite sur [0,T] laisserait cette queue : augmenter la précision de quadrature et augmenter T corrigent deux erreurs différentes.</p>')

lesson('beta_geometrie', 'Bêta, jacobien et factorisation d’une intégrale double', 'Spé', '''
<p>Pour a,b&gt;0, B(a,b)=∫₀¹t^(a−1)(1−t)^(b−1)dt est convergente. Au voisinage de 0, le critère porte sur a−1 ; près de 1, poser v=1−t et utiliser b−1. Le changement t↦1−t démontre immédiatement la symétrie B(a,b)=B(b,a).</p>
<p>Pour comprendre le lien avec gamma, écrire le produit Γ(a)Γ(b) comme une intégrale positive sur le quadrant u&gt;0,v&gt;0. Introduire <b>r=u+v</b>, qui mesure la somme, et <b>t=u/(u+v)</b>, qui mesure une proportion. L’inverse est u=rt et v=r(1−t), avec r&gt;0 et 0&lt;t&lt;1. La matrice des dérivées a pour déterminant −r : la valeur absolue du jacobien est r.</p>
<div class='formula'>e^(−u−v)u^(a−1)v^(b−1)du dv = e^(−r)r^(a+b−1)dr · t^(a−1)(1−t)^(b−1)dt.</div>
<p>Les deux variables se séparent. On obtient <b>Γ(a)Γ(b)=Γ(a+b)B(a,b)</b>. La positivité permet les interversions nécessaires ; le changement de variables dans une intégrale double est présenté ici comme un prolongement guidé. Le facteur r explique pourquoi l’exposant radial est a+b−1 et non a+b−2.</p>
<p>On peut ensuite éviter les intégrales doubles dans bien des calculs : B(a,b+1)=bB(a,b)/(a+b), B(a+1,b)=aB(a,b)/(a+b). Ces deux identités découlent de Γ(x+1)=xΓ(x), mais aussi de 1=t+(1−t) et d’une intégration par parties. Voir les identités dans <a href='https://dlmf.nist.gov/5.12'>NIST DLMF, §5.12</a>.</p>''')
lesson('beta_geometrie', 'Moments, densité et intégrales trigonométriques', 'Sup → Spé', '''
<p>La fonction w(t)=t^(a−1)(1−t)^(b−1)/B(a,b) est positive et son intégrale sur [0,1] vaut 1. Elle constitue une densité de probabilité. Une intégrale de tʳw(t) se ramène au même objet avec a augmenté :</p>
<div class='formula'>E(tʳ)=B(a+r,b)/B(a,b), lorsque a+r&gt;0 ; E(t)=a/(a+b).</div>
<p>Calculer E(t²)=a(a+1)/[(a+b)(a+b+1)], puis retrancher E(t)² pour obtenir Var(t)=ab/[(a+b)²(a+b+1)]. À a=b, la symétrie par rapport à 1/2 donne la moyenne sans aucun calcul. Si a et b sont grands à proportion fixée, la variance diminue : le graphique devient plus concentré.</p>
<p>Le changement t=sin²θ, θ∈[0,π/2], transforme les puissances de sinus et de cosinus en une intégrale bêta. Écrire dt=2sinθcosθdθ est le point décisif.</p>
<div class='formula'>∫₀^(π/2)sinᵖθcosᑫθdθ = ½B((p+1)/2,(q+1)/2), pour p,q&gt;−1.</div>
<p>Cette formule retrouve les intégrales de Wallis et dépasse le cas des exposants entiers. Elle fournit aussi une technique pour vérifier les dimensions d’un changement de variables : les deux facteurs supplémentaires sinθ et cosθ viennent du différentiel et modifient les exposants.</p>''')
exercise('beta_geometrie', 'Une intégrale trigonométrique non entière', 'Sup → Spé',
    '<p>Exprimer ∫₀^(π/2)√(sinθ)cos²θdθ avec les fonctions gamma. Vérifier la convergence aux deux extrémités.</p>',
    '<p>Les exposants p=1/2 et q=2 sont supérieurs à −1. La formule trigonométrique donne ½B(3/4,3/2)=<b>Γ(3/4)Γ(3/2)/(2Γ(9/4))</b>. On peut remplacer Γ(3/2) par √π/2 et Γ(9/4) par (5/4)(1/4)Γ(1/4). Il n’est pas nécessaire de trouver une primitive élémentaire.</p>')
exercise('beta_geometrie', 'Une densité qui se concentre', 'Sup → Spé',
    '<p>On choisit a=2k et b=3k, avec k&gt;0. Calculer la moyenne et la variance. Que deviennent-elles quand k tend vers l’infini ?</p>',
    '<p>La moyenne vaut <b>2/5</b> pour tout k. La variance vaut (6k²)/(25k²(5k+1))=<b>6/[25(5k+1)]</b>, donc tend vers 0. La masse se concentre autour de 2/5. Par l’inégalité de Bienaymé–Tchebychev, la probabilité de s’écarter de cette moyenne de plus de ε est au plus Var/ε² et tend vers 0.</p>')
exercise('beta_geometrie', 'Changer [0,1] en [0,+∞[', 'Spé',
    '<p>Pour a,b&gt;0, montrer B(a,b)=∫₀∞u^(a−1)/(1+u)^(a+b)du. Identifier les comportements aux deux bornes.</p>',
    '<p>Poser t=u/(1+u), donc dt=du/(1+u)² et 1−t=1/(1+u). Les facteurs se rassemblent en u^(a−1)/(1+u)^(a+b). En 0, le noyau est équivalent à u^(a−1) ; à l’infini, à u^(−b−1). Les deux convergences correspondent exactement à <b>a&gt;0 et b&gt;0</b>. Un changement t=1/(1+u) échange plutôt a et b.</p>')

lesson('zeta_series', 'Séries de Riemann et encadrement d’un reste', 'Sup → Spé', '''
<p>Pour s réel supérieur à 1, ζ(s)=Σ_(n≥1)n^(−s). La convergence est celle d’une série de Riemann. Fixons N≥1 et notons S_N la somme jusqu’à N, R_N=ζ(s)−S_N. Puisque t↦t^(−s) est décroissante, les rectangles de largeur 1 entourent l’aire située sous sa courbe.</p>
<div class='formula'>∫_(N+1)^∞t^(−s)dt ≤ R_N ≤ ∫_N^∞t^(−s)dt ; donc (N+1)^(1−s)/(s−1) ≤ R_N ≤ N^(1−s)/(s−1).</div>
<p>Ajouter ces deux bornes à S_N donne un intervalle contenant ζ(s), même si S_N est encore une mauvaise approximation. La largeur de cet intervalle est [N^(1−s)−(N+1)^(1−s)]/(s−1), de l’ordre de N^(−s) ; le reste lui-même est de l’ordre de N^(1−s)/(s−1). <b>Une correction intégrale peut donc resserrer fortement l’information</b> sans additionner beaucoup plus de termes.</p>
<p>Pour s=2, le reste est voisin de 1/N ; pour s=1,1, il est voisin de 10N^(−0,1). Le fait que les derniers termes soient petits ne suffit pas à contrôler leur somme infinie. Une somme partielle et une justification du reste répondent à deux questions différentes.</p>
<p>Les valeurs emblématiques sont ζ(2)=π²/6 et ζ(4)=π⁴/90. Le laboratoire utilise une référence par Euler–Maclaurin ; le raisonnement par rectangles constitue le contrôle indépendant auquel se fier pour un encadrement.</p>''')
lesson('zeta_series', 'Continuité et dérivation : choisir un domaine uniforme', 'Spé', '''
<p>Chaque fonction s↦n^(−s) est continue. Pour transmettre la continuité à une somme infinie, il faut un mode de convergence suffisant. Sur s≥1+δ, avec δ&gt;0 fixé, on a |n^(−s)|≤n^(−1−δ). La série majorante converge : la série définissant ζ est <b>normalement convergente</b> sur ce domaine, et donc uniformément convergente.</p>
<p>Pour dériver, la dérivée d’ordre p est (−ln n)^p n^(−s). Pour tout p et δ&gt;0, (ln n)^p≤C n^(δ/2) à partir d’un certain rang. Les dérivées sont alors majorées par Cn^(−1−δ/2), sommable. Le théorème de dérivation des séries de fonctions s’applique sur tout compact de ]1,+∞[.</p>
<div class='formula'>ζ^(p)(s)=(−1)^pΣ_(n≥2)(ln n)^p/n^s ; ζ′(s)&lt;0 ; ζ″(s)&gt;0.</div>
<p>La fonction ζ est donc strictement décroissante et strictement convexe sur ]1,+∞[. En revanche la convergence n’est pas uniforme sur tout ]1,+∞[ : pour N fixé, la borne du reste devient arbitrairement grande lorsque s approche 1, et le reste diverge lui aussi. Le bon réflexe en CPGE est de travailler d’abord sur <b>un segment à distance positive du bord du domaine</b>.</p>
<p>La représentation réelle et les autres représentations sont documentées dans <a href='https://dlmf.nist.gov/25.5'>NIST DLMF, chapitre 25</a>. Le prolongement complexe et l’hypothèse de Riemann appartiennent à un autre sujet ; les expériences présentes restent sur s&gt;1.</p>''')
exercise('zeta_series', 'Obtenir une précision avec les termes bruts', 'Sup',
    '<p>Pour ζ(2), combien de termes suffisent à garantir ζ(2)−S_N≤10⁻⁴ par comparaison intégrale ? Pourquoi cette garantie est-elle différente de la largeur de l’encadrement corrigé ?</p>',
    '<p>R_N≤1/N, donc <b>N≥10 000</b> suffit. Mais ζ(2) est entre S_N+1/(N+1) et S_N+1/N : la largeur est 1/[N(N+1)], de l’ordre de N⁻². La première garantie utilise S_N seul ; la seconde utilise une correction du reste. À N=100, la largeur corrigée est inférieure à 10⁻⁴.</p>')
exercise('zeta_series', 'Un nombre de termes gigantesque près du bord', 'Spé',
    '<p>Avec s=1,1, utiliser le majorant intégral pour trouver une condition suffisante sur N afin que R_N≤0,1. Commenter cette méthode de calcul.</p>',
    '<p>R_N≤10N^(−0,1). Exiger 10N^(−0,1)≤0,1 donne N^(0,1)≥100, donc <b>N≥10²⁰</b>. La sommation brute devient irréaliste. Une accélération analytique, par exemple Euler–Maclaurin, est utile. Ce résultat explique la lenteur sans prétendre que le majorant est le nombre de termes optimal.</p>')
exercise('zeta_series', 'Dérivation uniforme et signe de la dérivée', 'Spé',
    '<p>Justifier ζ′(s)=−Σ_(n≥2)(ln n)n^(−s) sur [3/2,3]. En déduire la monotonie et la convexité.</p>',
    '<p>Sur ce segment, les termes dérivés sont majorés par (ln n)n^(−3/2), qui est sommable, par exemple car ln n≤Cn^(1/4). La série initiale converge en un point ; le théorème de dérivation des séries s’applique. Les termes de ζ′ sont négatifs et ceux de ζ″=Σ(ln n)²n^(−s) positifs. On obtient <b>ζ′&lt;0 et ζ″&gt;0</b> sur le segment, puis sur tout ]1,+∞[ en changeant de compact.</p>')

lesson('zeta_integrale', 'Une série géométrique sous une intégrale impropre', 'Spé', '''
<p>Le noyau 1/(eᵗ−1) semble différent de la série ζ. Pour t&gt;0, écrire e^(−t)/(1−e^(−t))=Σ_(n≥1)e^(−nt). Multiplier par t^(s−1), puis intégrer sur ]0,+∞[. Comme les termes sont positifs, le théorème de convergence monotone permet de passer de la suite des sommes finies à la somme intégrée, même avant de connaître sa finitude.</p>
<div class='formula'>∫₀∞ t^(s−1)/(eᵗ−1)dt = Σ_(n≥1)∫₀∞t^(s−1)e^(−nt)dt = Γ(s)Σ_(n≥1)n^(−s).</div>
<p>Dans chaque terme, u=nt donne le facteur n^(−s). Pour s&gt;1, la série de Riemann est finie et l’identité donne Γ(s)ζ(s). On retrouve directement la même condition en étudiant le noyau : eᵗ−1∼t en 0, donc t^(s−1)/(eᵗ−1)∼t^(s−2), intégrable si et seulement si s&gt;1. À l’infini, le noyau est équivalent à t^(s−1)e^(−t).</p>
<p>Cette preuve illustre trois étapes distinctes : établir une représentation ponctuelle, <b>justifier une interversion</b>, puis effectuer un changement de variable dans chaque terme. La condition « tous les termes sont positifs » n’est pas une hypothèse accessoire : elle évite de devoir prouver auparavant la convergence dominée d’une somme infinie.</p>
<p>La représentation est donnée dans <a href='https://dlmf.nist.gov/25.5'>NIST DLMF, §25.5</a>. Numériquement, une substitution t=v^q retire la singularité du voisinage de 0 ; additionner une grille uniforme qui commence trop loin de 0 manquerait une partie importante de l’intégrale.</p>''')
lesson('zeta_integrale', 'Application physique : une loi en température obtenue par changement d’échelle', 'Spé · Prolongement', '''
<p>Des distributions thermiques conduisent à des intégrales de la forme I_p(T_phys)=∫₀∞ωᵖ/[exp(ℏω/(kT_phys))−1]dω, avec T_phys&gt;0, k la constante de Boltzmann et ℏ la constante de Planck réduite. Il suffit souvent d’identifier l’échelle de la variable, sans évaluer immédiatement l’intégrale.</p>
<div class='formula'>t=ℏω/(kT_phys) ; I_p(T_phys)=(kT_phys/ℏ)^(p+1)Γ(p+1)ζ(p+1), pour p&gt;0.</div>
<p>La condition p&gt;0 vient de la convergence en 0. Pour p=3, Γ(4)=6 et ζ(4)=π⁴/90 donnent π⁴/15. La dépendance de l’intégrale est donc <b>T_phys⁴</b>. Les facteurs de volume, de polarisation et de vitesse de la lumière dépendent de la quantité physique étudiée ; le laboratoire montre l’intégrale commune, sans les confondre avec elle.</p>
<p>Pour p=2, la constante est 2ζ(3) et la puissance de température est 3. Changer la dimension ou le nombre de puissances de la fréquence dans un comptage de modes modifie la loi d’échelle. Cette démarche fait le lien entre analyse, changement de variables, dimension physique et physique statistique.</p>
<p>Le curseur T de l’expérience désigne la <b>borne de troncature numérique</b>, sans dimension. Il ne faut pas la confondre avec T_phys. Quand la fréquence est remplacée par une pulsation ou inversement, les facteurs 2π se transforment également : annoncer la variable choisie avant de comparer des constantes physiques.</p>''')
exercise('zeta_integrale', 'Une intégrale issue du rayonnement', 'Spé',
    '<p>Calculer ∫₀∞t³/(eᵗ−1)dt en utilisant ζ(4)=π⁴/90. Justifier la convergence indépendamment de la valeur trouvée.</p>',
    '<p>En 0, le noyau est équivalent à t², intégrable. À l’infini il est équivalent à t³e^(−t), intégrable. L’identité donne Γ(4)ζ(4)=6π⁴/90=<b>π⁴/15</b>. La vérification du domaine précède le calcul et ne peut être remplacée par la seule finitude de la formule finale.</p>')
exercise('zeta_integrale', 'Modifier l’échelle sans recalculer l’intégrale', 'Sup → Spé',
    '<p>Pour a&gt;0 et s&gt;1, exprimer ∫₀∞t^(s−1)/(e^(at)−1)dt. Que se passe-t-il si a est multiplié par 2 ?</p>',
    '<p>Poser u=at. Le différentiel apporte 1/a et la puissance apporte a^(1−s), donc l’intégrale vaut <b>a^(−s)Γ(s)ζ(s)</b>. Quand a double, la valeur est multipliée par 2^(−s). Cette propriété permet de contrôler un calcul dimensionnel et de détecter l’oubli d’un facteur dans dt.</p>')
exercise('zeta_integrale', 'Pourquoi s=1 est-il exclu ?', 'Sup → Spé',
    '<p>Étudier ∫₀¹t^(s−1)/(eᵗ−1)dt pour s=1 et pour s=1+δ, δ&gt;0 petit. Identifier l’ordre de grandeur dominant.</p>',
    '<p>Pour s=1, le noyau est équivalent à 1/t : l’intégrale diverge logarithmiquement. Pour s=1+δ, il est équivalent à t^(δ−1), dont l’intégrale sur [0,1] vaut 1/δ. Plus précisément la différence entre le noyau et t^(δ−1) reste uniformément intégrable pour δ dans un petit intervalle positif. L’intégrale vaut donc <b>1/δ+O(1)</b>. Le bord du domaine crée une grande contribution concentrée près de 0.</p>')

lesson('integrale_fractionnaire', 'De Cauchy à une intégration d’ordre réel', 'Spé · Prolongement', '''
<p>Notons Jf(t)=∫₀ᵗf(u)du, primitive choisie nulle à l’origine. Pour n≥1, les intégrations répétées ont une forme unique, obtenue en échangeant l’ordre de deux intégrales sur un triangle :</p>
<div class='formula'>Jⁿf(t)=1/(n−1)! ∫₀ᵗ(t−u)^(n−1)f(u)du.</div>
<p>Le noyau est une puissance et la constante une valeur de gamma. Pour α réel strictement positif, on définit l’intégrale de Riemann–Liouville par J^αf(t)=1/Γ(α)∫₀ᵗ(t−u)^(α−1)f(u)du. Si 0&lt;α&lt;1, le noyau est singulier en u=t mais localement intégrable. Pour une fonction continue sur [0,t], l’intégrale est donc bien définie.</p>
<p>Appliquer cette définition à f(u)=u^q, q&gt;−1. Avec u=tv, les facteurs donnent t^(q+α), et l’intégrale restante est B(q+1,α). L’identité bêta-gamma simplifie le coefficient :</p>
<div class='formula'>J^α(t^q)=Γ(q+1)t^(q+α)/Γ(q+α+1).</div>
<p>À α=1, on retrouve t^(q+1)/(q+1). À α=1/2, J^(1/2)(1)=2√t/√π. Une « demi-intégration » n’est donc pas une primitive ordinaire multipliée par une constante : elle modifie aussi la puissance. Les ordres sont ici réels positifs et la borne initiale est fixée à 0 ; annoncer ces choix fait partie de la définition.</p>''')
lesson('integrale_fractionnaire', 'Loi de composition et réponse à une impulsion', 'Spé · Prolongement', '''
<p>Pour une fonction continue sur chaque intervalle fini et α,β&gt;0, on peut démontrer J^αJ^β=J^(α+β). Le même calcul vaut pour les profils bornés par morceaux de l’expérience. Écrire les deux intégrales sur 0≤v≤u≤t et échanger u et v. À v fixé, l’intégrale intérieure vaut ∫ᵥᵗ(t−u)^(α−1)(u−v)^(β−1)du. Le changement u=v+(t−v)r fournit (t−v)^(α+β−1)B(α,β). Les facteurs gamma donnent le noyau attendu.</p>
<div class='formula'>J^α[J^βf]=J^(α+β)f ; en particulier J^(1/2)J^(1/2)f=Jf.</div>
<p>Une impulsion rectangulaire vaut 1 sur [0,a] et 0 après a. Pour t≤a, le résultat est t^α/Γ(α+1). Pour t&gt;a, le passé utile s’arrête à a, mais son poids dépend encore de t :</p>
<div class='formula'>J^αf(t)=[t^α−(t−a)_+^α]/Γ(α+1), où (v)_+=max(v,0).</div>
<p>Après la fin du signal, une réponse subsiste. Quand t devient grand, t^α−(t−a)^α∼αa t^(α−1). Ainsi la réponse décroît pour α&lt;1, reste constante pour α=1 et croît pour α&gt;1. Ces comportements rendent la <b>mémoire non locale</b> visible. Ils se déduisent d’un développement limité en a/t, pas seulement du graphique.</p>
<p>Cette construction est une introduction au calcul fractionnaire, au-delà des exigences usuelles. La loi de composition des intégrales ne justifie pas automatiquement une loi analogue pour toutes les dérivées fractionnaires : les conditions initiales peuvent y intervenir. Une formulation par convolution est développée par <a href='https://arxiv.org/abs/1612.05103'>Li et Liu, étude des dérivées de Caputo</a>.</p>''')
exercise('integrale_fractionnaire', 'Vérifier deux demi-intégrations', 'Spé · Prolongement',
    '<p>Calculer J^(1/2)(1), puis J^(1/2)[J^(1/2)(1)]. Comparer à J(1).</p>',
    '<p>J^(1/2)(1)=t^(1/2)/Γ(3/2)=2√t/√π. Ensuite J^(1/2)(t^(1/2))=Γ(3/2)t/Γ(2)=√π t/2. En multipliant par 2/√π, on trouve <b>t=J(1)</b>. Les coefficients gamma sont indispensables pour que la composition donne exactement l’ordre 1.</p>')
exercise('integrale_fractionnaire', 'Mémoire après une impulsion', 'Spé · Prolongement',
    '<p>Une impulsion est égale à 1 sur [0,a]. Pour α=1/2, trouver sa réponse après a et un équivalent pour t→+∞.</p>',
    '<p>Pour t&gt;a, la réponse est <b>2(√t−√(t−a))/√π</b>. Rationaliser : √t−√(t−a)=a/(√t+√(t−a))∼a/(2√t). La réponse est donc équivalente à <b>a/√(πt)</b>. Elle tend vers 0, mais ne s’annule pas brusquement après la fin de l’impulsion.</p>')
exercise('integrale_fractionnaire', 'Détecter une confusion d’opérateurs', 'Spé · Prolongement',
    '<p>Un calcul propose J^αf(t)=f(t)t^α/Γ(α+1) pour toute f. Vérifier cette proposition avec f(t)=t et expliquer pourquoi elle marche pourtant pour une constante.</p>',
    '<p>La formule exacte donne J^α(t)=t^(α+1)/Γ(α+2), alors que la proposition donne t^(α+1)/Γ(α+1), soit un facteur α+1 de trop. Pour une constante, on peut sortir f de l’intégrale et intégrer le noyau, ce qui donne effectivement t^α/Γ(α+1). Pour une fonction variable, <b>on ne peut pas remplacer f(u) par f(t)</b> sous une intégrale qui porte sur tout le passé.</p>')

lesson('derivees_fractionnaires', 'Deux définitions et le rôle de la valeur initiale', 'Spé · Prolongement', '''
<p>Limiter d’abord l’étude à 0&lt;α&lt;1 permet de distinguer deux ordres d’opérations. La dérivée de Riemann–Liouville est D_RL^αf=(J^(1−α)f)′ : on intègre puis on dérive. La dérivée de Caputo est D_C^αf=J^(1−α)f′ : on dérive puis on intègre. Pour une fonction absolument continue, ces opérations n’ont pas en général le même résultat.</p>
<div class='formula'>D_C^αf(t)=1/Γ(1−α)∫₀ᵗ(t−u)^(−α)f′(u)du.</div>
<p>Écrire f(u)=f(0)+∫₀ᵘf′(v)dv. Appliquer J^(1−α), puis dériver. Le terme constant produit f(0)t^(−α)/Γ(1−α), et le terme contenant la primitive se simplifie grâce à la loi de composition. Ainsi :</p>
<div class='formula'>D_RL^αf(t)=D_C^αf(t)+f(0)t^(−α)/Γ(1−α), pour t&gt;0.</div>
<p>Pour f=1, Caputo donne 0 et Riemann–Liouville donne t^(−α)/Γ(1−α). Pour f=t^q, q≥1 entier, f(0)=0 et les deux définitions donnent Γ(q+1)t^(q−α)/Γ(q+1−α). Pour f=c+t^q, la constante sépare les deux courbes. À q=0, f est la constante c+1 ; cette situation doit être traitée séparément pour Caputo.</p>
<p>Dans une équation différentielle fractionnaire, annoncer l’opérateur et la borne initiale est indispensable. La dérivée ordinaire d’un ordre entier est un cas distinct ; les expressions comprenant Γ(1−α) ne s’emploient pas naïvement en posant α=1.</p>''')
lesson('derivees_fractionnaires', 'Une même valeur et une même pente ne déterminent pas une dérivée non locale', 'Spé · Prolongement', '''
<p>Considérons sur [0,1] f₁(t)=t et f₂(t)=t+A t(1−t)². À t=1, les deux fonctions ont la valeur 1 et la dérivée ordinaire 1. Les termes ajoutés s’annulent avec leur dérivée à cet instant. Leur passé diffère dès que A≠0.</p>
<p>La linéarité et les dérivées fractionnaires des puissances donnent :</p>
<div class='formula'>D_C^α(f₂−f₁)(t)=A[t^(1−α)/Γ(2−α)−4t^(2−α)/Γ(3−α)+6t^(3−α)/Γ(4−α)].</div>
<p>En t=1, utiliser Γ(3−α)=(2−α)Γ(2−α) et Γ(4−α)=(3−α)(2−α)Γ(2−α). Le coefficient devient −Aα(1−α)/[(2−α)(3−α)Γ(2−α)], non nul pour A≠0 et 0&lt;α&lt;1. Une dérivée de Caputo dépend de f′ sur <b>tout [0,t]</b>, pondérée par (t−u)^(−α), et non du seul voisinage infinitésimal de t.</p>
<p>Pour α=1/2, cette différence est −2A/(15√π). L’expérience compare à la fois les fonctions et leurs dérivées de Caputo ; elle évite de confondre différence de pente et différence de mémoire. Au niveau CPGE, les outils sont la linéarité, les polynômes, la récurrence gamma et le calcul d’intégrales. Le choix d’un modèle physique de mémoire relève d’un prolongement.</p>
<p>La question des valeurs initiales et des opérateurs est étudiée dans <a href='https://arxiv.org/abs/1612.05103'>Li et Liu, définition généralisée des dérivées de Caputo</a>. Le laboratoire reste volontairement dans le cadre classique des fonctions polynomiales régulières.</p>''')
exercise('derivees_fractionnaires', 'Dérivée d’ordre 1/2 d’une constante', 'Spé · Prolongement',
    '<p>Pour f(t)=3 et t&gt;0, calculer D_RL^(1/2)f et D_C^(1/2)f. Expliquer la singularité éventuelle en 0.</p>',
    '<p>J^(1/2)(3)=6√t/√π ; en dérivant, <b>D_RL^(1/2)f=3/√(πt)</b>. Pour Caputo, on dérive d’abord : f′=0 et le résultat est <b>0</b>. La singularité t^(−1/2) en 0 appartient à l’opérateur RL avec borne initiale 0 ; elle ne signifie pas que la fonction constante serait discontinue.</p>')
exercise('derivees_fractionnaires', 'Une puissance nulle à l’origine', 'Spé · Prolongement',
    '<p>Pour f(t)=t², calculer la dérivée de Caputo d’ordre 1/2. Retrouver le même résultat avec la définition de Riemann–Liouville.</p>',
    '<p>La formule donne Γ(3)t^(3/2)/Γ(5/2)=<b>8t^(3/2)/(3√π)</b>. Pour RL, intégrer d’ordre 1/2 : J^(1/2)(t²)=Γ(3)t^(5/2)/Γ(7/2)=16t^(5/2)/(15√π), puis dériver. On retrouve 8t^(3/2)/(3√π). L’égalité vient de f(0)=0 ; elle ne vaut pas pour toute fonction.</p>')
exercise('derivees_fractionnaires', 'Deux histoires identiques au dernier instant', 'Spé · Prolongement',
    '<p>Pour f₁(t)=t et f₂(t)=t+t(1−t)², vérifier f₁(1)=f₂(1) et f₁′(1)=f₂′(1). Calculer l’écart de leurs dérivées de Caputo d’ordre 1/2 en t=1.</p>',
    '<p>Le terme t(1−t)² et sa dérivée s’annulent en 1 : valeur et pente valent 1. L’écart de Caputo est Γ(2)/Γ(3/2)−2Γ(3)/Γ(5/2)+Γ(4)/Γ(7/2), soit (2−16/3+16/5)/√π=<b>−2/(15√π)</b>. La dérivée fractionnaire distingue leurs histoires. Le résultat se vérifie directement en intégrant [1−4u+3u²]/√(1−u) sur [0,1], divisé par √π.</p>')

lesson('faa_di_bruno', 'Classer les termes de la dérivée d’une composition', 'Spé · Prolongement', '''
<p>Les premières dérivées de h=f∘g sont h′=f′(g)g′ et h″=f″(g)(g′)²+f′(g)g″. À l’ordre 3, h‴=f‴(g)(g′)³+3f″(g)g′g″+f′(g)g‴. Le coefficient 3 ne vient pas d’une approximation : il compte les trois façons d’obtenir le même produit.</p>
<p>À l’ordre n, notons mⱼ le nombre de facteurs g^(j). Chaque facteur correspond à j dérivations, donc Σⱼjmⱼ=n. Si k=Σⱼmⱼ, la dérivée de f est d’ordre k. La formule de Faà di Bruno est :</p>
<div class='formula'>(f∘g)^(n)=Σ_[Σⱼjmⱼ=n] n! f^(k)(g) ∏ⱼ[(g^(j)/j!)^mⱼ/mⱼ!], avec k=Σⱼmⱼ.</div>
<p>Le facteur n! compte des affectations ordonnées ; les j! retirent les permutations internes et les mⱼ! retirent l’ordre entre blocs de même taille. Cette lecture combinatoire aide à retenir la formule sans oublier une factorielle. Les <b>polynômes de Bell partiels</b> B_(n,k) rassemblent les termes qui ont le même k.</p>
<div class='formula'>B_(0,0)=1 ; B_(n,k)=Σ_(j=1)^(n−k+1) C(n−1,j−1)xⱼB_(n−j,k−1).</div>
<p>Ici g=1+ax+bx² : g^(j)=0 pour j≥3. On ne conserve donc que m₁+2m₂=n. Il reste ⌊n/2⌋+1 contributions structurelles, bien moins que dans le cas général. Le tableau indique m₁,m₂,k, le coefficient n!/[m₁!m₂!2^m₂] et la contribution au point x₀. Un terme peut être nul au point choisi sans disparaître de la formule.</p>''')
lesson('faa_di_bruno', 'Dériver une inverse et une logarithmique : deux méthodes complémentaires', 'Spé', '''
<p>Si g ne s’annule pas, prendre f(z)=1/z dans Faà di Bruno. Comme f^(k)(z)=(−1)^k k!/z^(k+1), on obtient les dérivées de h=1/g. Une méthode souvent plus rapide dans un exercice consiste à partir de gh=1 et appliquer la formule de Leibniz.</p>
<div class='formula'>h^(n)=−1/g · Σ_(j=1)^n C(n,j)g^(j)h^(n−j), pour n≥1.</div>
<p>Cette récurrence exige la valeur de h et de ses dérivées précédentes au même point. Pour une quadratique, seuls j=1 et j=2 subsistent. Elle se calcule sans symbolisme compliqué et fournit un contrôle indépendant de la formule de composition.</p>
<p>Pour f=ln, annoncer g&gt;0 sur le domaine réel. On a f^(k)(z)=(−1)^(k−1)(k−1)!/zᵏ pour k≥1. L’exponentielle, elle, vérifie f^(k)=f à tous les ordres ; tous les coefficients combinatoires viennent donc des dérivées de g. L’exemple g=−x² conduit aux polynômes d’Hermite.</p>
<p>Dans l’expérience, g=1+ax+bx² est globalement positive car son minimum est 1−a²/(4b)≥0,375 avec les bornes des curseurs. Cela assure la définition de 1/g et ln(g), même lorsqu’on change de scénario. Aux ordres élevés, de grandes contributions peuvent se compenser : comparer <b>la somme signée</b> et les contributions est plus instructif que regarder seulement leur valeur absolue.</p>''')
exercise('faa_di_bruno', 'Dérivée quatrième : reconstruire les coefficients', 'Spé',
    '<p>Pour g quadratique, exprimer (f∘g)^(4) en fonction de f^(2),f^(3),f^(4),g′ et g″. Retrouver les coefficients en listant m₁+2m₂=4.</p>',
    '<p>Les couples (m₁,m₂) sont (4,0),(2,1),(0,2). Les coefficients 4!/[m₁!m₂!2^m₂] sont 1,6,3. Ainsi <b>(f∘g)^(4)=f^(4)(g)(g′)⁴+6f^(3)(g)(g′)²g″+3f″(g)(g″)²</b>. Dans le cas général il faudrait aussi les termes contenant g‴ et g^(4), qui sont ici nuls.</p>')
exercise('faa_di_bruno', 'Une inverse avec une récurrence de Leibniz', 'Spé',
    '<p>Soit h(x)=1/(1+x²). Sans utiliser de différences finies, calculer h^(6)(0), puis h^(2r)(0) et h^(2r+1)(0).</p>',
    '<p>La fonction est paire : les dérivées impaires en 0 sont nulles. Avec g=1+x², la récurrence donne h^(n)(0)=−n(n−1)h^(n−2)(0), puisque g′(0)=0 et g″=2. Partant de h(0)=1, on obtient <b>h^(2r)(0)=(−1)^r(2r)!</b>, donc h^(6)(0)=−720. Cela coïncide avec le développement Σ(−1)^r x^(2r) pour |x|&lt;1.</p>')
exercise('faa_di_bruno', 'Un coefficient de Bell contrôlé par une exponentielle', 'Spé · Prolongement',
    '<p>Pour g(x)=x, expliquer pourquoi la formule de Faà di Bruno ne conserve qu’un terme. Pour g(x)=x², quels termes peuvent contribuer en x=0 ?</p>',
    '<p>Si g=x, g′=1 et les dérivées supérieures sont nulles : seul m₁=n subsiste, donnant f^(n)(x). Si g=x², en 0 on a g′=0 et g″=2. Il faut m₁=0, donc n doit être pair, n=2r. Le coefficient donne <b>(f(x²))^(2r)(0)=(2r)!f^(r)(0)/r!</b>, et les dérivées impaires sont nulles. Pour f=exp, cela donne (2r)!/r!, vérifiable avec exp(x²)=Σx^(2r)/r!.</p>')

lesson('hermite_gauss', 'Rodrigues et Faà di Bruno : les polynômes d’Hermite', 'Spé', '''
<p>Chaque dérivée de e^(−x²) est cette gaussienne multipliée par un polynôme. Fixons la convention des physiciens :</p>
<div class='formula'>Hₙ(x)=(−1)^n e^(x²)(dⁿ/dxⁿ)e^(−x²) ; H₀=1, H₁=2x, H₂=4x²−2.</div>
<p>Prendre f=exp et g=−x² dans Faà di Bruno : seuls g′=−2x et g″=−2 interviennent. La condition m₁+2m₂=n donne la formule finie :</p>
<div class='formula'>Hₙ(x)=n!Σ_(j=0)^⌊n/2⌋(−1)^j(2x)^(n−2j)/[j!(n−2j)!].</div>
<p>On lit immédiatement le degré n, le coefficient dominant 2ⁿ et la parité Hₙ(−x)=(−1)^nHₙ(x). À l’origine, les degrés impairs donnent 0 et H_(2r)(0)=(−1)^r(2r)!/r!. Les récurrences Hₙ′=2nH_(n−1) et H_(n+1)=2xHₙ−2nH_(n−1) sont des outils efficaces pour calculer la famille et ses dérivées.</p>
<p>Elles permettent de vérifier l’équation différentielle Hₙ″−2xHₙ′+2nHₙ=0. Une famille de polynômes, une formule de dérivation et une équation différentielle se rejoignent dans un même objet. Le laboratoire ne remplace pas la dérivée par une approximation à partir d’une grille : il calcule les polynômes par récurrence.</p>
<p>Les conventions des familles orthogonales sont précisées dans <a href='https://dlmf.nist.gov/18.3'>NIST DLMF, §18.3</a>. La convention dite probabiliste utilise un poids e^(−x²/2) pour les polynômes et une autre échelle ; ne pas mélanger les deux suites.</p>''')
lesson('hermite_gauss', 'Orthogonalité, fonctions normalisées et oscillateur harmonique', 'Spé · Prolongement', '''
<p>Pour m&lt;n, écrire Hₙe^(−x²)=(−1)^n(dⁿ/dxⁿ)e^(−x²). Dans ∫ℝHₘHₙe^(−x²)dx, effectuer n intégrations par parties. Les termes de bord s’annulent car une gaussienne domine chaque polynôme, et Hₘ^(n)=0. Le produit scalaire est donc nul. Pour m=n, Hₙ^(n)=2ⁿn!, ce qui donne la norme.</p>
<div class='formula'>∫ℝHₙHₘe^(−x²)dx = √π 2ⁿn! δ_(n,m).</div>
<p>Définir ψₙ(x)=Hₙ(x)e^(−x²/2)/[π^(1/4)√(2ⁿn!)]. Les fonctions ψₙ ont une norme 1 et sont deux à deux orthogonales pour l’intégrale ordinaire sur ℝ. <b>Le poids est désormais inclus dans chaque fonction</b> : le produit de deux enveloppes e^(−x²/2) redonne e^(−x²).</p>
<p>En dérivant ψₙ puis en utilisant l’équation de Hₙ, on obtient −ψₙ″+x²ψₙ=(2n+1)ψₙ. C’est la forme sans dimension de l’équation stationnaire de l’oscillateur harmonique quantique. L’analyse classique explique le calcul et la normalisation ; l’interprétation des niveaux d’énergie est un prolongement vers la physique quantique.</p>
<p>L’orthogonalité ne résulte pas seulement d’une différence de parité. Si n et m sont de parités opposées, l’intégrande est impaire et son intégrale nulle par symétrie ; s’ils sont de même parité et différents, les intégrations par parties fournissent la preuve. Le laboratoire propose ces deux cas pour distinguer les arguments.</p>''')
exercise('hermite_gauss', 'Dériver trois fois une gaussienne', 'Sup → Spé',
    '<p>Calculer H₃ avec la récurrence, puis (d³/dx³)e^(−x²). Vérifier la parité.</p>',
    '<p>H₃=2xH₂−4H₁=2x(4x²−2)−8x=<b>8x³−12x</b>. La dérivée troisième est (−1)³H₃e^(−x²)=<b>(12x−8x³)e^(−x²)</b>. Elle est impaire, comme la troisième dérivée d’une fonction paire. Le signe (−1)^n de Rodrigues ne doit pas être omis.</p>')
exercise('hermite_gauss', 'Orthogonalité sans argument de parité', 'Spé',
    '<p>Calculer ∫ℝH₂(x)e^(−x²)dx, puis expliquer pourquoi ∫ℝH₂H₄e^(−x²)dx=0 bien que l’intégrande soit paire.</p>',
    '<p>H₂=4x²−2. La relation ∫ℝx²e^(−x²)dx=√π/2 donne 4√π/2−2√π=0. Pour H₂H₄, écrire H₄e^(−x²)=(d⁴/dx⁴)e^(−x²) et intégrer quatre fois par parties : H₂^(4)=0. Les termes de bord s’annulent. <b>Une intégrande paire peut avoir une intégrale nulle par compensation</b> ; la parité seule ne fournit pas ce résultat.</p>')
exercise('hermite_gauss', 'Retrouver une équation différentielle pour la fonction normalisée', 'Spé · Prolongement',
    '<p>À partir de Hₙ″−2xHₙ′+2nHₙ=0, vérifier −ψₙ″+x²ψₙ=(2n+1)ψₙ pour ψₙ=CₙHₙe^(−x²/2).</p>',
    '<p>On a ψₙ″=Cₙe^(−x²/2)[Hₙ″−2xHₙ′+(x²−1)Hₙ]. Remplacer Hₙ″−2xHₙ′ par −2nHₙ donne ψₙ″=(x²−2n−1)ψₙ, donc <b>−ψₙ″+x²ψₙ=(2n+1)ψₙ</b>. La constante Cₙ se simplifie ; elle sert à la norme, pas à la vérification de cette équation homogène.</p>')


GUIDES = {
    'gamma_euler': dict(
        purpose='Définir une fonction par une intégrale impropre, reconnaître son domaine et utiliser une intégration par parties pour retrouver la factorielle.',
        objects=['x : argument positif de Γ ; t : variable intégrée, différente de x.', 'T : borne supérieure de troncature ; Γ(x) : intégrale complète.', 't^(x−1)e^(−t) : noyau dont on étudie d’abord les deux extrémités.'],
        hypotheses=['x réel strictement positif.', 'Quadrature après retrait de la singularité à 0 ; comparaison à une référence indépendante.'],
        techniques=['Critères de convergence des puissances.', 'Intégration par parties avec contrôle des termes de bord.', 'Changement de variable et distinction entre troncature et quadrature.'],
        levels=dict(sup='Intégrales impropres, équivalents et récurrence de la factorielle.', spe='Fonction définie par une intégrale et dérivation sous le signe intégral.', beyond='Log-convexité et caractérisation de gamma.'),
        first_steps=['Choisir x=1/2 : identifier la singularité en 0 sans conclure à la divergence.', 'Choisir x=5 et comparer Γ(5) à 4!.', 'Choisir x=8, T=5, puis augmenter T : interpréter la part de l’aire retenue.'],
        expected='L’intégrale existe pour x>0 ; sa relation fonctionnelle est démontrée, et la queue de l’intégrale explique un écart même si la quadrature est précise.'),
    'beta_geometrie': dict(
        purpose='Faire apparaître bêta par un changement de variables et employer le rapport gamma pour calculer des moments ou des intégrales trigonométriques.',
        objects=['a,b : deux paramètres positifs ; t : proportion dans [0,1].', 'B(a,b) : constante de normalisation ; r=u+v : variable radiale du changement.', 'Moyenne et variance : intégrales de t et de t² avec la densité normalisée.'],
        hypotheses=['Les deux singularités éventuelles aux extrémités sont intégrables car a,b>0.', 'Densités comparées sur le même intervalle ; aucun point infini n’est remplacé par une valeur finie.'],
        techniques=['Changement t↦1−t et symétrie.', 'Jacobien d’un changement dans une intégrale double, guidé.', 'Moments obtenus en augmentant un exposant et intégrales de Wallis.'],
        levels=dict(sup='Symétrie, puissances, moments et changement trigonométrique.', spe='Lien gamma-bêta, normalisation et récurrences.', beyond='Changement de variables dans le quadrant et famille de lois bêta.'),
        first_steps=['Choisir a=b=1 : retrouver la densité uniforme.', 'Comparer (2,5) et (5,2) : observer la réflexion autour de 1/2.', 'Choisir a=b=1/2, puis a=b=4 : distinguer singularités intégrables et concentration au centre.'],
        expected='Les deux paramètres ont des rôles symétriques ; le facteur jacobien r fait apparaître exactement Γ(a+b), et non une autre valeur de gamma.'),
    'zeta_series': dict(
        purpose='Donner une approximation accompagnée d’un encadrement et comprendre pourquoi la convergence devient difficile près de s=1.',
        objects=['s>1 : exposant de la série de Riemann.', 'N : nombre de termes ; S_N : somme finie ; R_N : reste positif.', 'Deux bornes intégrales : intervalle garanti contenant ζ(s).'],
        hypotheses=['Étude sur le domaine réel s>1.', 'La référence numérique est distincte des bornes mathématiques du reste.'],
        techniques=['Comparaison série–intégrale par décroissance.', 'Encadrement et ordre de grandeur du reste.', 'Convergence normale sur un domaine à distance positive du bord.'],
        levels=dict(sup='Séries de Riemann et encadrement du reste.', spe='Continuité et dérivation des séries de fonctions.', beyond='Accélération Euler–Maclaurin et singularité de bord.'),
        first_steps=['À s=2, augmenter N puis comparer S_N à π²/6.', 'Passer à s=1,1 avec N=4000 : lire le reste, pas seulement le dernier terme.', 'À s=3/2, doubler N et comparer la diminution du reste à 2^(1−s).'],
        expected='Une série peut converger très lentement. Le reste se contrôle par des intégrales ; choisir un compact évite d’oublier le bord du domaine.'),
    'zeta_integrale': dict(
        purpose='Justifier le passage d’une série à une intégrale et relier un changement d’échelle à une loi physique en température.',
        objects=['s : paramètre réel >1 ; t : variable sans dimension.', 'T : borne numérique de troncature, distincte de T_phys, température.', 'Γ(s)ζ(s) : valeur complète ; somme d’exponentielles : représentation du noyau.'],
        hypotheses=['Termes positifs, permettant la convergence monotone.', 'Troncature à T et retrait numérique de la singularité de 0.'],
        techniques=['Série géométrique et interversion justifiée.', 'Étude aux bornes par équivalents.', 'Changement d’échelle et analyse dimensionnelle.'],
        levels=dict(sup='Équivalents, convergence et changements de variable.', spe='Interversion série–intégrale et fonctions définies par intégrale.', beyond='Rayonnement thermique et rôle de la dimension dans les lois de température.'),
        first_steps=['Choisir s=4 : comparer la valeur à π⁴/15.', 'Choisir s=1,2 : repérer où se concentre la difficulté d’intégration.', 'Choisir s=6 et T=5, puis augmenter T : distinguer le problème en 0 de la queue à l’infini.'],
        expected='La positivité justifie l’interversion ; s>1 vient du voisinage de 0. Le changement de fréquence fournit une puissance de température sans nouveau calcul d’intégrale.'),
    'integrale_fractionnaire': dict(
        purpose='Prolonger l’intégration répétée à un ordre réel et rendre visible la mémoire d’une impulsion passée.',
        objects=['α,β : ordres réels d’intégration ; t : instant observé.', 'q : exposant de la puissance t^q ; a : durée de l’impulsion.', 'J^α : intégrale à borne initiale 0 ; noyau (t−u)^(α−1)/Γ(α).'],
        hypotheses=['Ordres positifs et fonctions intégrables sur chaque intervalle fini.', 'Réponses analytiques ; contrôle indépendant de la composition sur une puissance.'],
        techniques=['Formule de Cauchy pour les intégrations répétées.', 'Changement u=tv et identité bêta.', 'Fubini sur un triangle et développement limité d’une réponse tardive.'],
        levels=dict(sup='Primitive nulle en 0 et intégrations répétées.', spe='Convolution, gamma et interversion de deux intégrales.', beyond='Intégrales d’ordre non entier et lois de mémoire.'),
        first_steps=['Choisir α=1 : retrouver la primitive ordinaire.', 'Choisir α=β=1/2 sur une puissance : lire le contrôle de composition.', 'Activer l’impulsion, puis comparer α=1/2 et α=3/2 après t=a : la mémoire décroît ou croît.'],
        expected='L’opérateur dépend de l’histoire entière. Deux demi-intégrations donnent une intégration, avec les coefficients gamma appropriés.'),
    'derivees_fractionnaires': dict(
        purpose='Comparer deux définitions et montrer qu’une dérivée non locale n’est pas fixée par la seule valeur et la pente à l’instant observé.',
        objects=['0<α<1 : ordre de dérivation ; q : entier non négatif.', 'c : constante ajoutée ; f(0)=c pour q≥1, et c+1 pour q=0.', 'A : amplitude de la modification du passé dans t+A t(1−t)².'],
        hypotheses=['Fonctions polynomiales régulières sur un intervalle commençant en 0.', 'Les courbes singulières de RL sont dessinées seulement pour t>0.'],
        techniques=['Ordre des opérations dériver/intégrer.', 'Linéarité et formule des puissances.', 'Comparaison de conditions ponctuelles et d’une intégrale de mémoire.'],
        levels=dict(sup='Dérivation d’une constante et polynômes.', spe='Noyaux singuliers intégrables et contrôle de la valeur initiale.', beyond='Dérivées de Caputo et de Riemann–Liouville.'),
        first_steps=['Choisir q=0,c=0 : comparer les deux dérivées de la constante 1.', 'Choisir q=1 et passer c de 0 à 1 : identifier le terme dû à f(0).', 'Modifier A : vérifier que valeur et pente en t=1 restent identiques, tandis que Caputo change.'],
        expected='Caputo annule une constante ; RL conserve un terme initial. La mémoire distingue deux fonctions qui se rejoignent avec la même pente.'),
    'faa_di_bruno': dict(
        purpose='Organiser une dérivation à ordre élevé, expliquer les coefficients combinatoires et contrôler une inverse par une méthode indépendante.',
        objects=['n : ordre de dérivation ; g(x)=1+ax+bx².', 'm₁,m₂ : nombres de facteurs g′ et g″ ; m₁+2m₂=n.', 'k=m₁+m₂ : ordre de dérivée de f ; x₀ : point du tableau.'],
        hypotheses=['Fonction extérieure exp, inverse ou logarithme.', 'g reste positive pour toutes les bornes proposées.'],
        techniques=['Règle de chaîne et formule de Leibniz.', 'Partitions d’un ordre de dérivation et récurrence de Bell.', 'Récurrence des dérivées d’une inverse obtenue par gh=1.'],
        levels=dict(sup='Dérivée seconde et produits composés.', spe='Leibniz, récurrences de dérivées et développements limités.', beyond='Faà di Bruno et polynômes de Bell.'),
        first_steps=['Choisir n=2 et exp : retrouver les deux termes familiers.', 'Passer à n=4 : lire les trois couples (m₁,m₂) et leurs coefficients.', 'Choisir une inverse à n=6, puis a=0,x₀=0 : utiliser la parité pour contrôler les valeurs.'],
        expected='Chaque contribution a une origine précise. Le nombre de dérivées de f n’est pas toujours n ; les grandes contributions peuvent se compenser.'),
    'hermite_gauss': dict(
        purpose='Relier les dérivées d’une gaussienne, une récurrence polynomiale, des intégrations par parties et une équation différentielle.',
        objects=['Hₙ : polynôme de degré n, convention des physiciens H₁=2x.', 'ψₙ : fonction Hₙe^(−x²/2) normalisée sur ℝ.', 'm : second degré ; ∫ψₙψₘ : produit scalaire.'],
        hypotheses=['Convention et poids fixés explicitement.', 'Intégrales numériques sur [−11,11], comparées aux identités exactes.'],
        techniques=['Récurrence et parité.', 'Rodrigues et Faà di Bruno pour exp(−x²).', 'Intégrations par parties répétées et transformation d’une équation différentielle.'],
        levels=dict(sup='Gaussienne, dérivation et parité.', spe='Polynômes, orthogonalité et intégrales impropres.', beyond='Base de Hermite et oscillateur harmonique quantique.'),
        first_steps=['Choisir n=0,m=1 : contrôler la parité et l’orthogonalité.', 'Choisir n=6,m=8 : constater que la parité ne suffit plus à expliquer l’intégrale nulle.', 'Prendre m=n : vérifier la norme 1, puis augmenter n et compter les zéros.'],
        expected='La récurrence construit les modes ; l’orthogonalité se démontre par intégrations par parties. Les zéros et l’équation différentielle relient algèbre et analyse.')
}

SOURCES = [
    dict(title='NIST DLMF — définition de gamma et digamma', url='https://dlmf.nist.gov/5.2'),
    dict(title='NIST DLMF — identités et intégrales bêta', url='https://dlmf.nist.gov/5.12'),
    dict(title='NIST DLMF — représentations intégrales de zêta', url='https://dlmf.nist.gov/25.5'),
    dict(title='NIST DLMF — conventions des polynômes orthogonaux', url='https://dlmf.nist.gov/18.3'),
    dict(title='Li et Liu — dérivées de Caputo et formulation par convolution', url='https://arxiv.org/abs/1612.05103')
]
