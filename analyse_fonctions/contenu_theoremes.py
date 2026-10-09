"""Vingt leçons, trente exercices corrigés et dix guides de manipulation."""
LESSONS=[]
EXERCISES=[]
GUIDES={}

def lesson(lab,title,level,html):
    LESSONS.append(dict(lab=lab,title=title,level=level,html=html))

def exercise(lab,title,level,question,answer):
    EXERCISES.append(dict(lab=lab,title=title,level=level,question=question,answer=answer))


lesson('cauchy_additive','Cauchy additive : calculer d’abord les valeurs imposées','Sup', '''
<p>Une équation fonctionnelle est une égalité portant sur une fonction inconnue, valable pour tous les paramètres indiqués. Chercher f:ℝ→ℝ telle que f(x+y)=f(x)+f(y). Il faut prouver que les solutions trouvées sont les seules, puis vérifier qu’elles satisfont effectivement l’équation.</p>
<p>Les premières substitutions coûtent peu : x=y=0 donne f(0)=0 ; y=−x donne f(−x)=−f(x). La fonction est impaire. Une récurrence donne f(nx)=nf(x) pour les entiers naturels n, puis pour tous les entiers grâce à l’imparité.</p>
<div class='formula'>f(x/n)=f(x)/n ; f(p/n)=(p/n)f(1), pour p∈ℤ et n≥1.</div>
<p>Les valeurs sur ℚ sont donc déterminées par une seule valeur, a=f(1). Cette étape est algébrique : elle n’utilise pas la continuité. Pour atteindre un réel x, choisir une suite de rationnels rₙ qui converge vers x. Si f est continue, f(x)=lim f(rₙ)=ax.</p>
<p>Enfin, ax vérifie a(x+y)=ax+ay : la réciproque est établie. Dans le laboratoire, une sinusoïde ajoutée à une droite sert à voir qu’une forme graphique plausible ne satisfait pas automatiquement l’équation. Chaque case de la carte évalue le résidu pour un couple (x,y).</p>''')
lesson('cauchy_additive','Régularité, dérivation et portée d’un contrôle numérique','Sup → Spé', '''
<p>Il suffit que f soit continue en un point x₀ : f(x₀+h)−f(x₀)=f(h) montre alors sa continuité en 0. Puis f(x+h)−f(x)=f(h) établit la continuité partout. Une autre hypothèse suffisante est la dérivabilité en 0.</p>
<div class='formula'>Si f est dérivable en 0 : [f(x+h)−f(x)]/h=f(h)/h→f′(0).</div>
<p>La dérivée est donc la même en chaque point. On retrouve f(x)=f′(0)x puisque f(0)=0. Cette preuve fait le lien entre équations fonctionnelles et équations différentielles : f′=a est un problème initial très simple.</p>
<p>Sans régularité, le passage de ℚ à ℝ est illégitime. L’additivité ne prouve pas, à elle seule, que la fonction est linéaire sur ℝ. Ce point est une limite de la méthode, et non un détail à supprimer dans une rédaction de concours.</p>
<p>Pour le candidat ax+b sin x, le défaut vaut b[sin(x+y)−sin x−sin y]. À x=y, il devient b[sin(2x)−2sin x]. Il est nul pour b=0 ; pour b≠0, trouver un seul couple donnant une valeur non nulle suffit à rejeter le candidat. En revanche, vérifier un nombre fini de couples ne suffit jamais à démontrer une identité pour tous les réels.</p>''')
exercise('cauchy_additive','Une valeur suffit-elle ?','Sup','<p>f est continue et additive sur ℝ, avec f(3)=−6. Déterminer f(√2). Que reste-t-il vrai si l’on retire la continuité ?</p>','<p>f(3)=3f(1) impose f(1)=−2. La continuité donne <b>f(x)=−2x</b>, donc f(√2)=−2√2. Sans régularité, seules les valeurs f(r)=−2r pour r rationnel sont ainsi imposées ; cette argumentation ne détermine pas f(√2).</p>')
exercise('cauchy_additive','Une hypothèse locale devient globale','Sup → Spé','<p>Montrer qu’une fonction additive continue en 7 est continue en tout point de ℝ. Éviter de supposer d’emblée une continuité globale.</p>','<p>Pour h→0, f(h)=f(7+h)−f(7)→0. Pour x fixé, f(x+h)−f(x)=f(h)→0. Ainsi <b>f est continue partout</b> ; le raisonnement sur les rationnels permet alors sa classification.</p>')
exercise('cauchy_additive','Détecter une perturbation avec un seul couple','Sup','<p>Le candidat est f(x)=ax+b sin x. Trouver un couple qui force b=0 si l’équation additive est vérifiée.</p>','<p>Choisir x=y=π/2 : f(π)−2f(π/2)=−2b. L’équation impose donc <b>b=0</b>. Cette substitution rejette chaque candidat perturbé sans inspection graphique.</p>')

lesson('cauchy_multiplicative','Quand un produit devient une somme : le logarithme','Sup', '''
<p>Sur ]0,+∞[, chercher une fonction continue telle que f(xy)=f(x)+f(y). Le domaine est essentiel : il est stable par multiplication, inversion et logarithme réel. En x=y=1, on obtient f(1)=0. En y=1/x, on obtient f(1/x)=−f(x).</p>
<p>Le bon changement de variable transforme l’opération qui apparaît dans l’équation. Poser h(u)=f(eᵘ) pour u∈ℝ. Alors eᵘeᵛ=eᵘ⁺ᵛ, et h vérifie une équation additive.</p>
<div class='formula'>h(u+v)=h(u)+h(v) ; h continue ⇒ h(u)=au ⇒ f(x)=a ln x.</div>
<p>La réciproque vient de ln(xy)=ln x+ln y. Pour déterminer a, une valeur comme f(e), ou la dérivée f′(1) lorsqu’elle est disponible, suffit. Par exemple, f(2)=3 donne a=3/ln 2.</p>
<p>Le candidat perturbé du laboratoire vaut a ln x+b(ln x)². Sa version en variable u est au+bu² ; son résidu vaut 2buv. Le défaut se voit donc même si la fonction est monotone sur une petite fenêtre. L’axe de la carte est u=ln x : une même longueur y représente un rapport multiplicatif, et non une différence additive.</p>''')
lesson('cauchy_multiplicative','Fonctions multiplicatives continues : justifier la positivité','Sup → Spé', '''
<p>Considérer maintenant f(xy)=f(x)f(y), sur x,y>0. La fonction nulle est une solution à isoler dès le début. Si f n’est pas nulle, choisir un x pour lequel f(x)≠0 ; l’équation à y=1 donne alors f(1)=1.</p>
<div class='formula'>f(x)f(1/x)=1 ; f(x)=f(√x)²&gt;0.</div>
<p>La première relation interdit les zéros. La seconde assure la positivité, sans avoir à la poser comme une hypothèse indépendante. On peut donc appliquer le logarithme : h(u)=ln f(eᵘ) est continue et additive. Ainsi h(u)=au, et <b>f(x)=xᵃ</b>. Avec la solution nulle, on a la classification complète dans cette classe de fonctions continues réelles.</p>
<p>La réciproque se vérifie directement avec (xy)ᵃ=xᵃyᵃ. Les exposants a peuvent être négatifs ou nuls : a=−1 donne l’inverse, a=0 donne la fonction constante 1, distincte de la fonction nulle.</p>
<p>Si f est dérivable, une méthode complémentaire consiste à dériver l’équation en y puis à poser y=1 : xf′(x)=f′(1)f(x). Résoudre cette équation différentielle sur ]0,+∞[ avec f(1)=1 retrouve la puissance. Les conditions initiales et le domaine excluant 0 doivent figurer dans la rédaction.</p>''')
exercise('cauchy_multiplicative','Identifier une échelle logarithmique','Sup','<p>f est continue sur ]0,+∞[, f(xy)=f(x)+f(y), et f(2)=3. Déterminer f(8), f(1/2) et f(3).</p>','<p>f(x)=(3/ln 2)ln x. Donc <b>f(8)=9, f(1/2)=−3, f(3)=3ln 3/ln 2</b>. Les deux premières valeurs se déduisent aussi directement de l’équation.</p>')
exercise('cauchy_multiplicative','Pourquoi peut-on prendre le logarithme de f ?','Sup → Spé','<p>Pour une solution continue non nulle de f(xy)=f(x)f(y) sur ]0,+∞[, prouver f(x)>0. Déterminer ensuite la solution vérifiant f(4)=2.</p>','<p>f(1)=1 et f(x)f(1/x)=1, donc f ne s’annule pas. Puis f(x)=f(√x)²&gt;0. La classification donne f(x)=xᵃ ; 4ᵃ=2 impose <b>a=1/2</b>, donc f(x)=√x.</p>')
exercise('cauchy_multiplicative','Passer à une équation différentielle','Spé','<p>Supposer f dérivable, multiplicative et non nulle sur ]0,+∞[. Montrer qu’elle vérifie xf′=af, puis résoudre avec f(1)=1.</p>','<p>Dériver en y : xf′(xy)=f(x)f′(y). En y=1, xf′(x)=af(x), avec a=f′(1). Comme f&gt;0, (ln f)′=a/x. Intégrer et utiliser f(1)=1 : <b>f(x)=exp(a ln x)=xᵃ</b>.</p>')

lesson('dalembert','D’Alembert : distinguer la solution nulle et la parité','Sup → Spé', '''
<p>L’équation f(x+y)+f(x−y)=2f(x)f(y) ressemble aux formules d’addition du cosinus. La ressemblance suggère des candidats ; elle ne les identifie pas encore tous. Il faut commencer par les valeurs particulières.</p>
<p>À y=0, 2f(x)=2f(x)f(0). Si f n’est pas identiquement nulle, f(0)=1. À x=0, on obtient f(y)+f(−y)=2f(y), donc f est paire. Si f est dérivable en 0, f′(0)=0.</p>
<div class='formula'>f≡0 ; ou f(0)=1 et f(−x)=f(x).</div>
<p>Les formules d’addition montrent que cos(kx) et cosh(kx) conviennent pour chaque réel k. La fonction constante 1 correspond à k=0. La fonction nulle convient aussi, mais elle n’a pas f(0)=1 : la séparer évite une division injustifiée.</p>
<p>Le laboratoire affiche une carte à deux variables. L’égalité à y=0 seule ne suffit pas, pas plus que la parité seule : une perturbation bx² conserve ces deux premières conditions mais viole généralement l’équation complète. La méthode de résolution doit donc aller au-delà de ces substitutions nécessaires.</p>''')
lesson('dalembert','Une équation fonctionnelle produit un problème initial','Spé', '''
<p>Supposer f de classe C² et non nulle. Deux dérivations par rapport à y donnent f″(x+y)+f″(x−y)=2f(x)f″(y). En y=0, il reste un problème initial d’équation différentielle.</p>
<div class='formula'>f″=λf ; λ=f″(0), f(0)=1, f′(0)=0.</div>
<p>Si λ=−k²&lt;0, la solution est cos(kx). Si λ=k²&gt;0, elle est cosh(kx). Si λ=0, elle est 1. L’unicité du problème initial dans chacune de ces équations linéaires garantit qu’aucune autre fonction C² non nulle n’a été oubliée.</p>
<p>Reste la réciproque : les formules cos(u+v)+cos(u−v)=2cos u cos v et leur version hyperbolique vérifient l’équation fonctionnelle. Résoudre une conséquence différentielle sans cette dernière vérification serait incomplet.</p>
<p>Un autre chemin, proche du TP du recueil, utilise x=y : f(2x)=2f(x)²−1. Cette relation détermine des valeurs sur des subdivisions dyadiques, et les polynômes de Chebyshev organisent les multiples. La continuité permet ensuite un passage par densité. L’atelier privilégie la preuve C² pour faire le lien avec les problèmes initiaux, mais distingue explicitement l’hypothèse choisie.</p>''')
exercise('dalembert','Une solution prescrite par la courbure en 0','Spé','<p>f∈C²(ℝ) vérifie l’équation de d’Alembert et f″(0)=−9. Déterminer f et vérifier la réciproque.</p>','<p>La solution nulle est impossible. Donc f(0)=1, f′(0)=0 et f″=−9f. Le problème initial donne <b>f(x)=cos(3x)</b>. La formule d’addition du cosinus vérifie l’équation initiale.</p>')
exercise('dalembert','La fonction constante ne doit pas être oubliée','Sup','<p>Quelles fonctions constantes vérifient l’équation de d’Alembert ? À quoi correspond le cas λ=0 dans la preuve différentielle ?</p>','<p>Si f=c, l’équation donne 2c=2c², donc <b>c=0 ou c=1</b>. Dans le cas non nul, λ=0 avec f(0)=1 et f′(0)=0 donne uniquement 1. La constante 0 a été isolée avant cette étape.</p>')
exercise('dalembert','Du double angle aux polynômes','Sup → Spé','<p>Déduire des relations sur f(2x) et f(3x) à partir de l’équation, en supposant f(0)=1.</p>','<p>Avec y=x, <b>f(2x)=2f(x)²−1</b>. Avec les paramètres 2x et x, f(3x)+f(x)=2f(2x)f(x), donc <b>f(3x)=4f(x)³−3f(x)</b>. On reconnaît les deux premiers polynômes de Chebyshev non triviaux.</p>')

lesson('identification_symetrie','Une substitution qui ferme un système','Sup', '''
<p>Chercher f définie sur ℝ privé de 0 telle que f(x)+f(−x)/x=x. Le terme f(−x) suggère une substitution très précise : écrire l’égalité au point −x. Aucun passage à la limite ni aucune dérivation n’est nécessaire.</p>
<div class='formula'>A+B/x=x ; B−A/x=−x, avec A=f(x), B=f(−x).</div>
<p>Multiplier la première équation par x donne xA+B=x². Soustraire la seconde après réarrangement, ou remplacer B=A/x−x : A(1+x²)=x²(x+1). Le déterminant du système ne s’annule jamais sur le domaine.</p>
<div class='formula'>f(x)=x²(x+1)/(1+x²), pour x≠0.</div>
<p>Cette formule prouve l’unicité d’un éventuel candidat. Pour l’existence, calculer f(−x)=x²(1−x)/(1+x²), puis f(x)+f(−x)/x=x. Le raisonnement donne donc exactement une solution sur ℝ privé de 0, sans supposer f continue.</p>
<p>Dans d’autres équations, les substitutions x↦1/x, x↦−x ou les échanges de variables créent de petits systèmes analogues. La bonne substitution réutilise les mêmes valeurs inconnues : elle ne multiplie pas indéfiniment les nouvelles inconnues.</p>''')
lesson('identification_symetrie','Parties paire et impaire, prolongement et comportement à l’infini','Sup → Spé', '''
<p>Toute fonction sur un domaine stable par x↦−x se décompose en f=p+q, où p(x)=[f(x)+f(−x)]/2 est paire et q(x)=[f(x)−f(−x)]/2 est impaire. La solution du laboratoire donne des expressions simples.</p>
<div class='formula'>p(x)=x²/(1+x²) ; q(x)=x³/(1+x²).</div>
<p>Près de 0, f(x)=x²+x³+O(x⁴). La limite en 0 vaut 0 : il existe un unique prolongement continu, obtenu en fixant f(0)=0. Mais l’équation initiale contient 1/x ; elle ne doit pas être présentée comme vérifiée en x=0.</p>
<p>À l’infini, une division polynomiale donne f(x)=x+1−(x+1)/(1+x²). L’asymptote est y=x+1. Sa partie paire tend vers 1, alors que sa partie impaire ressemble à x. Ces deux courbes rendent la décomposition visible et constituent des outils classiques d’étude de fonction.</p>
<p>Le laboratoire ajoute éventuellement b sin x au candidat. L’ajout conserve une allure proche, mais la vérification dans l’égalité initiale révèle un défaut. Au voisinage de 0, ce défaut tend vers −b : la division par x amplifie ici une perturbation qui s’annule elle-même en 0.</p>''')
exercise('identification_symetrie','Déterminer les valeurs en ±1 avant la formule générale','Sup','<p>Pour l’équation f(x)+f(−x)/x=x, calculer f(1) et f(−1) par deux substitutions.</p>','<p>À x=1 : f(1)+f(−1)=1. À x=−1 : f(−1)−f(1)=−1. Additionner et soustraire donne <b>f(1)=1, f(−1)=0</b>. Ces valeurs fournissent un premier contrôle de la formule générale.</p>')
exercise('identification_symetrie','Existence, unicité, domaine','Sup','<p>Résoudre l’équation sur ℝ privé de 0. La valeur f(0) est-elle imposée ? Donner le prolongement continu éventuel.</p>','<p>Le système au couple ±x donne <b>f(x)=x²(x+1)/(1+x²)</b>. La substitution vérifie l’existence. Sur ce domaine, f(0) n’existe pas et n’est donc pas imposée ; si l’on demande une extension à ℝ, sa valeur peut être arbitraire. La continuité en 0 impose la seule valeur <b>0</b>.</p>')
exercise('identification_symetrie','Une erreur petite, un défaut non petit','Sup → Spé','<p>Remplacer la solution par f(x)+b sin x. Calculer le résidu de l’équation et sa limite en 0.</p>','<p>Le défaut est b[sin x−sin x/x]. Comme sin x→0 et sin x/x→1, il tend vers <b>−b</b>. Une perturbation de la fonction qui s’annule en 0 ne donne donc pas forcément un défaut d’équation qui s’annule en 0.</p>')

lesson('continuite_gauss','Théorème de continuité : identifier un majorant intégrable','Spé', '''
<p>Pour une intégrale à paramètre F(a)=∫J f(a,t)dt, il faut distinguer le paramètre a et la variable intégrée t. Une continuité en a pour chaque t ne suffit pas lorsque J est non borné ou que l’intégrande présente une singularité. Le théorème de la page 63 demande un majorant intégrable indépendant du paramètre sur le domaine considéré.</p>
<div class='formula'>f(a,t)=e⁻ᵗ²cos(at), a∈ℝ, t∈ℝ ; |f(a,t)|≤e⁻ᵗ².</div>
<p>Pour chaque t, a↦f(a,t) est continue. Pour chaque a, t↦f(a,t) est continue et intégrable. Le majorant φ(t)=e⁻ᵗ² est positif, indépendant de a et intégrable sur ℝ. Il en résulte que F est définie et continue sur tout ℝ.</p>
<p>La preuve s’écrit avant le calcul explicite. Une intégrande oscillante peut avoir une petite intégrale par compensation ; cela ne fournit pas une domination de sa valeur absolue. La courbe de φ encadre les lobes positifs et négatifs de f et explique pourquoi le théorème s’applique.</p>
<p>Dans une autre application, le majorant peut dépendre d’un voisinage compact de a et rester indépendant du paramètre courant dans ce voisinage. Cette domination locale suffit à démontrer la continuité en chaque point intérieur du domaine.</p>''')
lesson('continuite_gauss','Gauss, Fourier et une équation différentielle pour calculer F','Spé · Prolongement', '''
<p>La continuité ne donne pas encore la valeur de l’intégrale. Pour dériver F, utiliser |∂f/∂a|≤|t|e⁻ᵗ², intégrable. Ainsi F′(a)=−∫ℝte⁻ᵗ²sin(at)dt. Comme (e⁻ᵗ²)′=−2te⁻ᵗ², une intégration par parties annule les termes de bord et simplifie l’intégrale.</p>
<div class='formula'>F′(a)=−aF(a)/2 ; F(0)=√π ; F(a)=√πe⁻ᵃ²/⁴.</div>
<p>Cette méthode est emblématique : un théorème de dérivation sous l’intégrale fabrique une équation différentielle en paramètre ; une valeur connue fixe la solution. La partie imaginaire de ∫ℝe⁻ᵗ²e⁻ⁱᵃᵗdt est nulle par imparité. La formule est donc aussi une transformée de Fourier de la gaussienne.</p>
<p>Numériquement, on remplace ℝ par [−L,L]. Pour L&gt;0, chaque queue est dominée par e⁻ᴸ²/(2L), car t/L≥1 sur [L,+∞[. Les deux queues donnent e⁻ᴸ²/L. Le laboratoire ajoute une borne de l’erreur des trapèzes sur la partie finie, calculée avec un majorant de la dérivée seconde en t. Une valeur petite de F ne garantit pas une petite erreur relative : l’erreur absolue est plus pertinente dans les régimes de forte compensation.</p>''')
exercise('continuite_gauss','Changer l’échelle de la gaussienne','Spé','<p>Pour c&gt;0, calculer ∫ℝe⁻ᶜᵗ²cos(at)dt à partir de la formule du laboratoire. Justifier sa continuité en a.</p>','<p>Poser u=√c t. On obtient <b>√(π/c)exp[−a²/(4c)]</b>. À c fixé, |e⁻ᶜᵗ²cos(at)|≤e⁻ᶜᵗ², fonction intégrable indépendante de a ; le théorème de continuité s’applique sur ℝ.</p>')
exercise('continuite_gauss','Majorer les deux queues','Sup → Spé','<p>Montrer ∫L∞e⁻ᵗ²dt≤e⁻ᴸ²/(2L) pour L&gt;0, puis donner une erreur de troncature valable pour tous les a.</p>','<p>Pour t≥L, 1≤t/L. Donc ∫L∞e⁻ᵗ²dt≤(1/L)∫L∞te⁻ᵗ²dt=<b>e⁻ᴸ²/(2L)</b>. Comme |cos(at)|≤1 et les deux côtés de ℝ sont symétriques, l’erreur absolue de troncature est au plus <b>e⁻ᴸ²/L</b>.</p>')
exercise('continuite_gauss','Calculer une intégrale grâce à une EDO','Spé','<p>Retrouver F′=−aF/2 en précisant le majorant qui autorise la dérivation et le terme de bord.</p>','<p>|∂f/∂a|≤|t|e⁻ᵗ², intégrable, donc F′=−∫te⁻ᵗ²sin(at). Utiliser te⁻ᵗ²=−(e⁻ᵗ²)′/2 ; e⁻ᵗ²sin(at)→0 aux deux infinis. L’intégration par parties donne <b>F′=−aF/2</b>. Avec F(0)=√π, résoudre le problème initial.</p>')

lesson('continuite_defaut','Un contre-exemple qui explique l’hypothèse de domination','Spé', '''
<p>Pour a&gt;0 et t&gt;0, poser fₐ(t)=e⁻ᵗ/ᵃ/a. Pour a=0, poser f₀(t)=0 ; au point t=0, fixer aussi fₐ(0)=0. Changer la valeur d’une intégrande en un seul point ne change pas son intégrale.</p>
<p>À chaque t&gt;0 fixé, la décroissance exponentielle domine le facteur 1/a : fₐ(t)→0 quand a→0⁺. Le même résultat est vrai en t=0 avec la définition choisie. On a donc une convergence ponctuelle vers f₀ sur tout le domaine.</p>
<div class='formula'>t=au ⇒ ∫₀∞fₐ(t)dt=∫₀∞e⁻ᵘdu=1 ; ∫₀∞f₀(t)dt=0.</div>
<p>L’intégrale n’est pas continue au paramètre 0. Les hypothèses de continuité ponctuelle ne suffisent pas : la masse reste égale à 1 mais se concentre dans une fenêtre de largeur comparable à a. Pour ε&gt;0 fixé, la masse dans [0,ε] vaut 1−e⁻ᵋ/ᵃ et tend vers 1.</p>
<p>Le majorant manquant peut être identifié explicitement. Pour 0&lt;t≤1, la borne supérieure de fₐ(t) sur 0&lt;a≤1 est atteinte en a=t et vaut 1/(et). Tout majorant commun aurait une intégrale divergente près de 0. Le premier théorème de la page 63 ne peut donc pas être utilisé dans un voisinage comprenant a=0.</p>''')
lesson('continuite_defaut','Domination locale et changement de variable adapté au pic','Spé · Prolongement', '''
<p>La difficulté se situe au bord a=0. Autour d’un a strictement positif, on peut choisir α∈[a/2,2a]. Comme 1/α≤2/a et e⁻ᵗ/ᵅ≤e⁻ᵗ/⁽²ᵃ⁾, un majorant local simple existe.</p>
<div class='formula'>fα(t)≤(2/a)e⁻ᵗ/⁽²ᵃ⁾ ; ∫₀∞(2/a)e⁻ᵗ/⁽²ᵃ⁾dt=4.</div>
<p>Le théorème prouve la continuité de l’intégrale sur ]0,+∞[, où elle vaut effectivement 1. Il ne fournit aucun prolongement continu à 0. La différence entre domination locale à un point intérieur et domination jusqu’à une extrémité du domaine est une technique récurrente en analyse.</p>
<p>Une grille numérique uniforme sur [0,L] risque de manquer le pic dès que son pas devient grand devant a. En revanche, le changement de variable t=au transforme l’intégrande et le facteur dt en e⁻ᵘdu : la largeur du pic est normalisée. Les masses affichées dans le laboratoire utilisent les formules exactes, et non une somme qui pourrait donner une fausse disparition de la masse.</p>
<p>La famille illustre également la différence entre convergence ponctuelle et convergence en norme intégrale : ∫|fₐ−f₀|=1. Dire que chaque valeur converge ne signifie pas que la totalité de l’aire sous les courbes converge.</p>''')
exercise('continuite_defaut','Combien de masse près de 0 ?','Sup → Spé','<p>Calculer ∫₀ᵋfₐ(t)dt et choisir ε en fonction de a pour capturer 99 % de la masse.</p>','<p>L’intégrale vaut <b>1−e⁻ᵋ/ᵃ</b>. Capturer 99 % impose e⁻ᵋ/ᵃ≤0,01, donc <b>ε≥a ln 100≈4,605a</b>. La fenêtre doit rester proportionnelle à la largeur de concentration.</p>')
exercise('continuite_defaut','Calculer la borne supérieure des densités','Spé','<p>Pour t&gt;0 fixé, maximiser e⁻ᵗ/ᵃ/a sur 0&lt;a≤1. Que prouve le résultat concernant un majorant intégrable commun ?</p>','<p>La dérivée logarithmique est (t−a)/a². Pour t≤1, le maximum est en a=t et vaut <b>1/(et)</b>. Pour t&gt;1, le maximum est en a=1 et vaut e⁻ᵗ. La divergence de ∫₀¹dt/t interdit tout majorant intégrable commun.</p>')
exercise('continuite_defaut','Comparer deux modes de convergence','Spé','<p>Prouver fₐ(t)→0 ponctuellement, mais que fₐ ne tend pas vers 0 en norme L¹. Quelle égalité illégitime serait produite par un passage automatique sous l’intégrale ?</p>','<p>Pour t&gt;0, poser u=t/a : fₐ(t)=ue⁻ᵘ/t→0. Au point 0, la valeur est fixée à 0. Pourtant ∫|fₐ|=1. Le passage illégitime donnerait <b>lim∫fₐ=∫lim fₐ=0</b>, alors que le membre de gauche vaut 1.</p>')

lesson('leibniz_frullani','Frullani : compenser une singularité avant de dériver','Spé', '''
<p>Étudier F(a,b)=∫₀∞(e⁻ᵃᵗ−e⁻ᵇᵗ)/t dt pour a,b&gt;0. Il serait incorrect de séparer les deux termes : chacun comporte une divergence en 0. C’est leur différence qui est intégrable.</p>
<div class='formula'>e⁻ᵃᵗ−e⁻ᵇᵗ=(b−a)t+O(t²) ; f(a,b,0)=b−a par prolongement.</div>
<p>À l’infini, le théorème des accroissements finis appliqué à c↦e⁻ᶜᵗ donne |f(a,b,t)|≤|b−a|e⁻ᵐⁱⁿ⁽ᵃ,ᵇ⁾ᵗ, ce qui prouve l’intégrabilité. Le signe de F est celui de b−a.</p>
<p>Fixer b et dériver en a : ∂f/∂a=−e⁻ᵃᵗ. Pour un point a&gt;0 fixé, travailler sur le voisinage α∈[a/2,3a/2]. Le majorant e⁻⁽ᵃ/²⁾ᵗ est continu et intégrable. Le deuxième théorème de la page 63 donne ∂F/∂a=−1/a.</p>
<p>La domination doit être indépendante de α à l’intérieur du voisinage choisi. La notation « a fixé » désigne le centre du voisinage, pas le paramètre courant de l’intégrande. Cette distinction évite un majorant dépendant de la variable qu’il était censé contrôler uniformément.</p>''')
lesson('leibniz_frullani','Fixer une constante et contrôler les limites d’intégration','Spé', '''
<p>De ∂F/∂a=−1/a, on déduit F(a,b)=−ln a+C(b). Le fait que b soit un paramètre ne permet pas de traiter C comme une constante absolue ; elle peut dépendre de b. Pour l’identifier, choisir a=b.</p>
<div class='formula'>F(b,b)=0 ⇒ C(b)=ln b ⇒ F(a,b)=ln(b/a).</div>
<p>On retrouve les lois logarithmiques : F(a,c)=F(a,b)+F(b,c), et le changement t=u/a montre que F ne dépend que du rapport b/a. Le résultat donne de nombreuses intégrales impropres dont une primitive directe serait peu commode.</p>
<p>La troncature à L laisse une queue. La majoration de l’intégrande donne |F−∫₀ᴸf|≤|b−a|e⁻ᵐᴸ/m, avec m=min(a,b). Cette borne est volontairement simple et peut être large. Pour la dérivée, la queue a une valeur exacte e⁻ᵃᴸ/a en valeur absolue.</p>
<p>En calcul numérique, soustraire e⁻ᵃᵗ et e⁻ᵇᵗ pour t très petit perd des chiffres significatifs. La réécriture avec expm1, qui calcule précisément eᵘ−1 près de 0, respecte la compensation. Le quotient est prolongé par b−a en 0. Cette précaution illustre la différence entre une expression mathématiquement correcte et une évaluation numérique stable.</p>''')
exercise('leibniz_frullani','Un logarithme sans primitive','Spé','<p>Calculer ∫₀∞(e⁻²ᵗ−e⁻⁵ᵗ)/t dt. Peut-on intégrer séparément les deux termes ?</p>','<p>La formule donne <b>ln(5/2)</b>. Les deux intégrales séparées divergent en 0 ; leur différence est intégrable parce que le numérateur vaut 3t+O(t²). La séparation serait donc illégitime.</p>')
exercise('leibniz_frullani','Dériver par rapport aux deux paramètres','Spé','<p>À partir de la méthode et de la formule, donner ∂F/∂a et ∂F/∂b. Retrouver a∂F/∂a+b∂F/∂b=0.</p>','<p>Les dérivées sont <b>−1/a et 1/b</b>, obtenues en intégrant −e⁻ᵃᵗ et e⁻ᵇᵗ avec une domination locale. Ainsi a(−1/a)+b(1/b)=0. Cela correspond à l’invariance F(λa,λb)=F(a,b).</p>')
exercise('leibniz_frullani','Déterminer une coupure suffisante','Sup → Spé','<p>Avec a=1,b=2, utiliser la borne simple des queues pour garantir une erreur de troncature au plus 10⁻⁶. Cette garantie couvre-t-elle l’erreur de quadrature ?</p>','<p>La borne vaut e⁻ᴸ. Il suffit de prendre <b>L≥ln(10⁶)≈13,82</b>. Cette garantie concerne uniquement la partie omise après L ; il faut contrôler séparément l’erreur de la méthode d’intégration sur [0,L].</p>')

lesson('leibniz_arctan','Dériver un paramètre enlève une difficulté de l’intégrande','Spé', '''
<p>Pour a&gt;0, définir F(a)=∫₀∞e⁻ᵃᵗsin(t)/t dt. En 0, sin(t)/t→1 ; à l’infini, la présence de e⁻ᵃᵗ assure l’intégrabilité absolue. La difficulté du facteur 1/t suggère de dériver par rapport à a.</p>
<div class='formula'>∂f/∂a=−e⁻ᵃᵗsin t ; |∂f/∂α|≤e⁻⁽ᵃ/²⁾ᵗ pour α≥a/2.</div>
<p>Pour chaque point a&gt;0, cette majoration locale est intégrable. Les hypothèses de Leibniz sont remplies et F′(a)=−∫₀∞e⁻ᵃᵗsin t dt. L’intégrale restante s’obtient par exponentielle complexe ou par deux intégrations par parties.</p>
<div class='formula'>∫₀∞e⁻ᵃᵗsin t dt=1/(1+a²) ; F′(a)=−1/(1+a²).</div>
<p>L’intégrale inconnue est donc solution d’une équation différentielle en paramètre. Pour la déterminer, la primitive de F′ ne suffit pas : il faut une condition supplémentaire. Ici, une limite à l’infini remplace une valeur initiale.</p>''')
lesson('leibniz_arctan','Une condition à l’infini et la limite au bord du domaine','Spé · Prolongement', '''
<p>Pour t≥0, |sin t|≤t. Il en résulte |F(a)|≤∫₀∞e⁻ᵃᵗdt=1/a. Ainsi F(a)→0 quand a→+∞. Comme F′(a)=−1/(1+a²), on obtient la constante d’intégration.</p>
<div class='formula'>F(a)=π/2−arctan a=arctan(1/a), pour a&gt;0.</div>
<p>Avec une pulsation ω réelle, le même raisonnement donne ∫₀∞e⁻ᵃᵗsin(ωt)/t dt=arctan(ω/a). Dériver en ω, sous domination e⁻ᵃᵗ, est une autre voie : la dérivée vaut ∫₀∞e⁻ᵃᵗcos(ωt)dt=a/(a²+ω²), et la valeur à ω=0 est nulle.</p>
<p>La formule suggère la limite π/2 quand a→0⁺. Mais le majorant e⁻⁽ᵃ/²⁾ᵗ dépend du point a et n’est plus intégrable uniformément jusqu’à 0. Identifier la limite de la formule n’est pas encore justifier l’égalité avec l’intégrale impropre non amortie ∫₀∞sin t/t dt : cette identification demande un argument d’Abel ou un contrôle indépendant de ses queues.</p>
<p>Pour a&gt;0 et L&gt;0, la queue absolue est au plus e⁻ᵃᴸ/(aL). L’enveloppe de la dérivée donne e⁻ᵃᴸ/a. En abaissant a, il faut augmenter la coupure pour obtenir la même borne ; le laboratoire rend cette nécessité visible.</p>''')
exercise('leibniz_arctan','Ajouter une pulsation','Spé','<p>Pour a&gt;0, calculer G(ω)=∫₀∞e⁻ᵃᵗsin(ωt)/t dt en dérivant par rapport à ω. Préciser le majorant.</p>','<p>|∂f/∂ω|=e⁻ᵃᵗ|cos(ωt)|≤e⁻ᵃᵗ, intégrable et indépendant de ω. Donc G′(ω)=a/(a²+ω²). Avec G(0)=0, <b>G(ω)=arctan(ω/a)</b>.</p>')
exercise('leibniz_arctan','La valeur de la constante','Spé','<p>Résoudre F′(a)=−1/(1+a²) avec la condition F(a)→0 à l’infini. Pourquoi la condition est-elle nécessaire ?</p>','<p>F(a)=−arctan a+C. La limite impose C=π/2, donc <b>F(a)=arctan(1/a)</b> pour a&gt;0. Sans la condition, une constante arbitraire reste possible et l’intégrale n’est pas identifiée.</p>')
exercise('leibniz_arctan','Distinguer limite et passage sous l’intégrale','Spé','<p>La formule donne limₐ→₀⁺F(a)=π/2. Le majorant local utilisé pour Leibniz autorise-t-il directement ∫sin t/t=π/2 ?</p>','<p><b>Non.</b> Le majorant e⁻⁽ᵃ/²⁾ᵗ n’est pas commun à tous les a proches de 0. Pour identifier l’intégrale non amortie à cette limite, il faut justifier un passage à la limite, par exemple via un contrôle uniforme des queues oscillantes. La limite de la formule seule ne fournit pas cette justification.</p>')

lesson('derivees_gamma','Γ est C∞ : contrôler chaque ordre près de 0 et à l’infini','Spé', '''
<p>Pour a&gt;0, Γ(a)=∫₀∞tᵃ⁻¹e⁻ᵗdt. La singularité éventuelle en 0 est intégrable car a−1&gt;−1 ; à l’infini, l’exponentielle domine les puissances. Dériver n fois par rapport à a fait apparaître (ln t)ⁿ.</p>
<div class='formula'>∂ᵏ[tᵃ⁻¹e⁻ᵗ]/∂aᵏ=tᵃ⁻¹(ln t)ᵏe⁻ᵗ.</div>
<p>Fixer un voisinage [m,M] de a, avec 0&lt;m&lt;a&lt;M, et un entier n. Pour 0&lt;t≤1, tᵅ⁻¹≤tᵐ⁻¹ ; pour t≥1, tᵅ⁻¹≤tᴹ⁻¹. Pour 0≤k≤n, |ln t|ᵏ≤1+|ln t|ⁿ.</p>
<div class='formula'>φ(t)=tᵐ⁻¹(1+|ln t|ⁿ)e⁻ᵗ si t≤1 ; φ(t)=tᴹ⁻¹(1+(ln t)ⁿ)e⁻ᵗ si t≥1.</div>
<p>Près de 0, le changement s=−ln t transforme la majoration en une puissance de s multipliée par e⁻ᵐˢ ; à l’infini, l’exponentielle assure à nouveau l’intégrabilité. Le troisième théorème de la page 63 donne Γ∈Cⁿ et Γ⁽ᵏ⁾=∫∂ᵏf. Comme n est arbitraire, Γ est C∞ sur ]0,+∞[. Chaque compact du domaine possède ses majorants ; il n’est pas nécessaire d’en chercher un valable jusqu’à a=0.</p>''')
lesson('derivees_gamma','Log-convexité : une inégalité intégrale devient une variance','Spé · Prolongement', '''
<p>La fonction pₐ(t)=tᵃ⁻¹e⁻ᵗ/Γ(a) est positive et d’intégrale 1. On peut lire les dérivées de Γ comme des moments du logarithme : E(ln t)=Γ′/Γ et E((ln t)²)=Γ″/Γ.</p>
<div class='formula'>(ln Γ)″=Γ″/Γ−(Γ′/Γ)²=Var(ln t)&gt;0.</div>
<p>La variance est strictement positive car ln t n’est pas constante pour cette densité positive sur ]0,+∞[. Cette interprétation probabiliste donne la convexité stricte de ln Γ. Sans probabilités, Cauchy–Schwarz appliqué à √pₐ et (ln t)√pₐ fournit exactement la même inégalité.</p>
<p>En particulier, pour 0≤θ≤1, Γ((1−θ)a+θb)≤Γ(a)¹⁻ᶿΓ(b)ᶿ. La récurrence Γ(a+1)=aΓ(a), obtenue par intégration par parties, relie les dérivées aux factorielles mais ne suffit pas à elle seule à caractériser une interpolation continue du factorial.</p>
<p>Le laboratoire intègre en u=ln t : Γ⁽ⁿ⁾(a)=∫ℝuⁿexp(au−eᵘ)du. Il conserve le facteur dt=eᵘdu. Les coupures u=−q ln 10 et t=T donnent des queues explicites. L’écart entre deux quadratures indique une sensibilité numérique ; les bornes affichées contrôlent les queues, pas automatiquement l’erreur de quadrature.</p>''')
exercise('derivees_gamma','Dériver la relation de récurrence','Spé','<p>À partir de Γ(a+1)=aΓ(a), donner des relations pour Γ′ et Γ″. Les dérivations sont-elles justifiées ?</p>','<p>Γ est C∞ sur ]0,+∞[ grâce aux majorants locaux. On obtient <b>Γ′(a+1)=Γ(a)+aΓ′(a)</b>, puis <b>Γ″(a+1)=2Γ′(a)+aΓ″(a)</b>. Ces relations contrôlent les moments logarithmiques d’un intervalle de paramètres au suivant.</p>')
exercise('derivees_gamma','Log-convexité avec Cauchy–Schwarz','Spé','<p>Prouver Γ′(a)²≤Γ(a)Γ″(a), et expliquer pourquoi l’inégalité est stricte.</p>','<p>Appliquer Cauchy–Schwarz aux fonctions u(t)=t⁽ᵃ⁻¹⁾/²e⁻ᵗ/² et v(t)=u(t)ln t. Les carrés de leurs normes valent Γ(a) et Γ″(a), et leur produit scalaire vaut Γ′(a). L’égalité exigerait ln t constante presque partout pour un poids strictement positif, ce qui est impossible. Donc <b>Γ′²&lt;ΓΓ″</b>.</p>')
exercise('derivees_gamma','Un seul majorant pour plusieurs ordres','Spé','<p>Pour a∈[1/2,3] et k=0,1,2,3, proposer un majorant intégrable commun de tᵃ⁻¹|ln t|ᵏe⁻ᵗ.</p>','<p>Pour t≤1, prendre <b>t⁻¹/²(1+|ln t|³)e⁻ᵗ</b>. Pour t≥1, prendre <b>t²(1+(ln t)³)e⁻ᵗ</b>. Le changement s=−ln t prouve l’intégrabilité du premier morceau ; la décroissance exponentielle prouve celle du second. La domination est indépendante de a et de k dans les ensembles indiqués.</p>')

lesson('derivees_laplace','Dériver à tout ordre une transformée de Laplace','Spé', '''
<p>Pour a&gt;0, F(a)=∫₀∞e⁻ᵃᵗdt=1/a. Dériver formellement sous l’intégrale produit (−t)ᵏe⁻ᵃᵗ. Le troisième théorème de la page 63 transforme ce calcul formel en démonstration lorsqu’on fournit les majorants requis.</p>
<p>Fixer a&gt;0, un ordre n et un voisinage α∈[a/2,3a/2]. Pour t≥0 et 0≤k≤n, tᵏ≤1+tⁿ. Ainsi les dérivées partielles sont toutes dominées par une même fonction intégrable.</p>
<div class='formula'>|(−t)ᵏe⁻ᵅᵗ|≤(1+tⁿ)e⁻⁽ᵃ/²⁾ᵗ.</div>
<p>Le théorème donne F⁽ᵏ⁾(a)=∫₀∞(−t)ᵏe⁻ᵃᵗdt. En dérivant 1/a, on en déduit l’identité valable à chaque ordre entier.</p>
<div class='formula'>∫₀∞tⁿe⁻ᵃᵗdt=n!/aⁿ⁺¹.</div>
<p>On peut aussi la prouver par n intégrations par parties, ou avec u=at et Γ(n+1)=n!. Les méthodes se contrôlent mutuellement. Cette identité est un outil central pour les transformées de Laplace, les moments de lois exponentielles et les modèles linéaires dont on résout les équations différentielles dans le domaine transformé.</p>''')
lesson('derivees_laplace','Monotonie complète et queues d’intégrale','Spé · Prolongement', '''
<p>Une fonction F est complètement monotone sur ]0,+∞[ si elle est C∞ et si (−1)ⁿF⁽ⁿ⁾≥0 pour tout entier n≥0. Ici, la représentation intégrale donne un résultat encore strict : l’intégrande tⁿe⁻ᵃᵗ est positive pour t&gt;0.</p>
<div class='formula'>(−1)ⁿF⁽ⁿ⁾(a)=n!/aⁿ⁺¹&gt;0.</div>
<p>F décroît, F″ est positive, F‴ est négative, et ainsi de suite. Le même raisonnement fonctionne pour ∫e⁻ᵃᵗw(t)dt avec w≥0, sous des hypothèses de domination adaptées. Une propriété de signe d’une densité se transmet donc aux dérivées de sa transformée.</p>
<p>Pour l’intégration numérique, la densité tⁿe⁻ᵃᵗ atteint son maximum en n/a. Une grande valeur de n, ou un petit a, déplace la partie importante de l’aire vers la droite. Une coupure fixe peut alors perdre une proportion majeure de la masse.</p>
<div class='formula'>Rₙ(L)=∫L∞tⁿe⁻ᵃᵗdt=e⁻ᵃᴸ∑ⱼ₌₀ⁿ[n!/(n−j)!] Lⁿ⁻ʲ/aʲ⁺¹.</div>
<p>Cette formule exacte provient d’intégrations par parties répétées et permet de contrôler la troncature. À l’ordre n, la fraction capturée jusqu’à L vaut 1−Rₙ(L)/(n!/aⁿ⁺¹). Le laboratoire oppose cette masse à la simple position du maximum : avoir le maximum dans la fenêtre ne signifie pas encore avoir toute la queue.</p>''')
exercise('derivees_laplace','Une intégrale de moment','Sup → Spé','<p>Calculer ∫₀∞t⁷e⁻²ᵗdt de deux façons : changement de variable et dérivation d’une intégrale à paramètre.</p>','<p>Avec u=2t, l’intégrale vaut Γ(8)/2⁸=<b>7!/256=19,6875</b>. En dérivant sept fois F(a)=1/a, F⁽⁷⁾(a)=−7!/a⁸ ; l’intégrale positive est −F⁽⁷⁾(2). La dérivation nécessite le majorant local explicité dans le cours.</p>')
exercise('derivees_laplace','Connaître la masse perdue','Spé','<p>Pour n=1 et a=1, calculer exactement la queue après L. Trouver la fraction capturée pour L=4.</p>','<p>Une intégration par parties donne <b>R₁(L)=e⁻ᴸ(L+1)</b>. La masse totale vaut 1 ; la fraction capturée pour L=4 est <b>1−5e⁻⁴≈0,9084</b>. Le maximum est pourtant en t=1, bien à l’intérieur de la fenêtre.</p>')
exercise('derivees_laplace','Transmettre un signe aux dérivées','Spé · Prolongement','<p>Soit w≥0 et H(a)=∫₀∞e⁻ᵃᵗw(t)dt. Sous les hypothèses permettant la dérivation à chaque ordre, montrer H complètement monotone. Que devient l’affirmation si w change de signe ?</p>','<p>Le théorème donne (−1)ⁿH⁽ⁿ⁾(a)=∫₀∞tⁿe⁻ᵃᵗw(t)dt≥0. Donc <b>H est complètement monotone</b>. Si w change de signe, les dérivées peuvent encore être définies, mais l’argument de positivité ne s’applique plus ; la monotonie complète n’est pas assurée.</p>')


def guide(purpose,objects,hypotheses,techniques,levels,first_steps,expected):
    return dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,levels=levels,first_steps=first_steps,expected=expected)

GUIDES={
 'cauchy_additive':guide('Résoudre une équation fonctionnelle par substitutions, puis comprendre le rôle exact de la continuité.',
    ['x et y : deux arguments réels indépendants.','a : pente de la solution ax ; b : amplitude d’une perturbation sinusoïdale.','R(x,y)=f(x+y)−f(x)−f(y) : défaut d’égalité, en chaque case de la carte.'],
    ['f continue en au moins un point pour la classification en droites.','La carte teste une famille de candidats et un nombre fini de couples.'],
    ['Substituer 0 et −x ; utiliser une récurrence.','Déterminer f sur ℚ puis passer à ℝ par densité et continuité.','Distinguer conditions nécessaires et vérification de la réciproque.'],
    dict(sup='Valeurs particulières, parité, récurrence et continuité.',spe='Comparaison de preuves par densité et par dérivation.',beyond='Solutions additives sans hypothèse de régularité.'),
    ['Choisir b=0 et voir le résidu presque nul aux arrondis près.','Ajouter b=0,1 et comparer la faible perturbation de la courbe au défaut de la carte.','Tester à la main le couple x=y=π/2, puis lire la preuve de classification.'],
    'La continuité prolonge la linéarité des rationnels aux réels. Un seul contre-exemple rejette une fonction ; des tests finis ne prouvent pas l’identité.'),
 'cauchy_multiplicative':guide('Transformer les produits en sommes et retrouver le logarithme ou les puissances en justifiant chaque changement de variable.',
    ['x,y>0 : arguments des fonctions ; u=ln x et v=ln y : axes de la carte.','a : coefficient du logarithme ou exposant de la puissance.','b : défaut quadratique en ln x, ou défaut dans l’exposant de la puissance.'],
    ['Fonctions réelles continues sur ]0,+∞[.','La famille puissance visualisée est strictement positive ; la fonction nulle est traitée dans le cours.'],
    ['Poser h(u)=f(eᵘ), ou h(u)=ln f(eᵘ).','Établir f(1), l’absence de zéros et la positivité avant de prendre ln f.','Résoudre Cauchy additive puis vérifier dans l’équation initiale.'],
    dict(sup='Logarithme, exponentielle et changement de variable.',spe='Classification, dérivation et EDO xf′=af.',beyond='Rôle des hypothèses de régularité dans les morphismes.'),
    ['Choisir le logarithme exact, puis interpréter une case en revenant à x=eᵘ et y=eᵛ.','Passer à la puissance avec a=−1 et vérifier f(xy)=f(x)f(y).','Activer une perturbation et trouver un couple qui invalide le candidat.'],
    'Le logarithme convertit une structure multiplicative en une structure additive. Le domaine positif et la positivité de f sont des étapes de preuve.'),
 'dalembert':guide('Faire apparaître une équation différentielle dans une équation fonctionnelle et conserver les conditions initiales.',
    ['k : fréquence du cosinus ou taux du cosinus hyperbolique.','λ : coefficient de l’EDO f″=λf pour la famille exacte.','b x² : perturbation conservant la parité et, dans les familles non nulles, f(0)=1.'],
    ['La classification présentée par dérivation suppose f∈C²(ℝ).','f≡0 est une solution distincte, isolée avant le cas f(0)=1.'],
    ['Substituer 0 et établir la parité.','Dériver deux fois en y puis poser y=0.','Résoudre f″=λf avec f(0)=1 et f′(0)=0 ; vérifier les formules d’addition.'],
    dict(sup='Parité, identités trigonométriques et hyperboliques.',spe='Équation différentielle linéaire et unicité du problème initial.',beyond='Subdivisions dyadiques et polynômes de Chebyshev.'),
    ['Comparer les deux familles exactes avec le même k.','Choisir la solution nulle et identifier l’étape de preuve qui change.','Ajouter b=0,1 : la parité persiste, mais les résidus fonctionnel et différentiel révèlent le défaut.'],
    'Les substitutions fournissent des conditions nécessaires. L’EDO et ses conditions initiales donnent les candidats, puis les formules d’addition valident la réciproque.'),
 'identification_symetrie':guide('Utiliser une substitution adaptée pour calculer f(x) et f(−x) sans présupposer une forme de solution.',
    ['x≠0 : argument de l’équation.','f(x), f(−x) : deux inconnues d’un système linéaire.','b : amplitude d’un défaut ajouté ; R : étendue de l’intervalle visible.'],
    ['L’équation initiale est définie sur ℝ privé de 0.','La continuité n’est pas nécessaire à l’identification ; elle sert seulement au prolongement en 0.'],
    ['Remplacer x par −x puis résoudre un système de deux équations.','Vérifier l’existence après l’unicité.','Décomposer en parties paire et impaire ; étudier limite et asymptote.'],
    dict(sup='Systèmes, symétrie, parité et étude de fonction.',spe='Stratégies de substitutions −x, 1/x et échanges de variables.',beyond='Propagation des défauts près d’un point exclu du domaine.'),
    ['Choisir b=0 et retrouver les valeurs f(1)=1, f(−1)=0.','Comparer la partie paire et la partie impaire à la solution totale.','Ajouter un petit b et observer que le résidu ne s’annule pas près de 0.'],
    'Le système détermine une unique solution sur le domaine. En 0, seule une demande de prolongement continu impose la valeur 0.'),
 'continuite_gauss':guide('Appliquer le premier théorème de la page 63 avant de calculer une intégrale et relier le résultat à Fourier.',
    ['a : paramètre réel ; t : variable intégrée sur ℝ.','L : coupure du calcul sur [−L,L].','φ(t)=e⁻ᵗ² : majorant global ; F(a) : aire algébrique sous l’intégrande.'],
    ['Continuité en a pour chaque t et continuité de l’intégrande en t.','Le majorant φ est indépendant de a et intégrable sur ℝ.'],
    ['Identifier domaine du paramètre et domaine d’intégration.','Majorer une valeur absolue par une fonction intégrable.','Combiner Leibniz, intégration par parties et EDO ; contrôler les queues.'],
    dict(sup='Intégrales impropres et majorations de fonctions.',spe='Continuité et dérivation d’intégrales à paramètre.',beyond='Transformée de Fourier de la gaussienne et bornes de quadrature.'),
    ['Choisir a=0 : vérifier l’intégrale gaussienne.','Augmenter a : les oscillations restent dans la même enveloppe.','Réduire L puis comparer l’écart observé à la borne totale annoncée.'],
    'Le majorant global prouve la continuité sur ℝ. La compensation réduit F sans invalider la majoration de l’intégrande.'),
 'continuite_defaut':guide('Comprendre pourquoi la convergence ponctuelle ne suffit pas pour passer une limite sous une intégrale.',
    ['a>0 : largeur et échelle du pic.','ε : largeur d’une fenêtre proche de 0 ; L : borne d’affichage.','fₐ=e⁻ᵗ/ᵃ/a pour t>0 ; F(a)=1 ; f₀=0 et F(0)=0.'],
    ['La valeur en t=0 est fixée à 0 pour tout a ; elle ne change aucune intégrale.','Aucun majorant intégrable commun ne couvre tous les a proches de 0.'],
    ['Calculer une limite ponctuelle et une intégrale par changement de variable.','Maximiser sur le paramètre pour tester l’existence d’un majorant.','Distinguer domination locale intérieure, limite au bord et convergence L¹.'],
    dict(sup='Exponentielle, changement de variable et masse sous une courbe.',spe='Hypothèses du théorème de continuité et contre-exemple.',beyond='Concentration, convergence L¹ et approximations de masses ponctuelles.'),
    ['Diminuer a en gardant ε fixe : mesurer la masse dans [0,ε].','Faire aussi ε=a et constater la fraction 1−e⁻¹.','Lire l’enveloppe 1/(et) et vérifier la divergence de son intégrale près de 0.'],
    'Le pic s’efface à chaque point fixé, mais son aire reste égale à 1. Le majorant manquant explique exactement l’échec de la continuité en a=0.'),
 'leibniz_frullani':guide('Calculer une intégrale compensée en dérivant un paramètre, puis fixer sa constante par une valeur simple.',
    ['a,b>0 : taux de décroissance des deux exponentielles.','t : variable intégrée ; L : coupure haute.','Le quotient en 0 est prolongé par b−a ; la dérivée en a vaut −e⁻ᵃᵗ.'],
    ['Dérivation à b fixé, sur un voisinage restant à distance de a=0.','Domination locale de la dérivée par e⁻⁽ᵃ/²⁾ᵗ.'],
    ['Utiliser un développement limité pour la compensation en 0.','Appliquer Leibniz avec un majorant intégrable de ∂f/∂a.','Intégrer −1/a puis utiliser F(b,b)=0 ; contrôler la queue.'],
    dict(sup='Développements limités, logarithme et intégrales impropres.',spe='Dérivation d’une intégrale à paramètre et constante d’intégration.',beyond='Stabilité numérique d’une différence d’exponentielles.'),
    ['Choisir a=1,b=2 : retrouver ln 2.','Choisir a=b : l’intégrale est nulle, mais sa dérivée en a ne l’est pas.','Réduire a et L : lire la borne de queue puis augmenter L.'],
    'La dérivation simplifie l’intégrande. La condition F(b,b)=0 est indispensable pour retrouver ln(b/a).'),
 'leibniz_arctan':guide('Transformer une intégrale oscillante en une EDO et comprendre la portée locale du théorème de Leibniz.',
    ['a>0 : amortissement ; t : variable intégrée.','F(a) : intégrale de e⁻ᵃᵗsin(t)/t ; F′(a)=−1/(1+a²).','L : coupure ; e⁻⁽ᵃ/²⁾ᵗ : majorant local de la dérivée.'],
    ['Le quotient sin(t)/t est prolongé par 1 en 0.','La domination est locale pour a>0 ; elle ne permet pas directement de passer à a=0.'],
    ['Dériver pour enlever un facteur 1/t.','Calculer une intégrale exponentielle-trigonométrique.','Fixer une constante avec une limite ; distinguer troncature et quadrature.'],
    dict(sup='Exponentielles complexes et intégration par parties.',spe='Leibniz, EDO en paramètre et limite à l’infini.',beyond='Limite d’Abel de l’intégrale de Dirichlet.'),
    ['Choisir a=1 : comparer intégrale et π/4.','Diminuer a tout en gardant L fixe : vérifier la borne de la queue.','Augmenter L puis expliquer pourquoi le calcul pour a=0 n’est pas justifié par le même majorant.'],
    'Pour a>0, F(a)=arctan(1/a). Un résultat au bord du domaine demande une justification supplémentaire.'),
 'derivees_gamma':guide('Appliquer le troisième théorème de la page 63 à plusieurs ordres, puis obtenir une inégalité par Cauchy–Schwarz.',
    ['a>0 : paramètre de Γ ; n : ordre entier de dérivation.','u=ln t : variable du tracé ; q fixe ε=10⁻ᑫ ; T fixe la coupure haute.','Γ⁽ⁿ⁾ : moment de (ln t)ⁿ ; variance de ln t : dérivée seconde de ln Γ.'],
    ['Domination sur un voisinage compact de a, en séparant 0<t≤1 et t≥1.','Un même majorant contrôle les ordres 0 à n.'],
    ['Majorer des puissances et des logarithmes près de 0.','Changer de variable en conservant le facteur dt.','Dériver à l’ordre n ; utiliser Cauchy–Schwarz ou une variance pour la log-convexité.'],
    dict(sup='Gamma aux entiers, intégration par parties et impropres.',spe='Dérivation à plusieurs ordres et inégalité de Cauchy–Schwarz.',beyond='Fonctions digamma et trigamma, moments d’une loi gamma.'),
    ['Choisir n=2,a=2 et comparer les moments à la variance positive.','Descendre a à 0,6 : voir l’importance de la queue basse en u.','Augmenter q et T : comparer les bornes des queues et l’indicateur de quadrature.'],
    'Γ est C∞ sur ]0,+∞[. Sa log-convexité résulte d’un moment quadratique ; chaque passage sous l’intégrale a un majorant local explicite.'),
 'derivees_laplace':guide('Contrôler plusieurs dérivations par un majorant commun et mesurer une troncature avec une queue exacte.',
    ['a>0 : paramètre de Laplace ; n : ordre entier.','tⁿe⁻ᵃᵗ : densité positive, de maximum n/a.','L : coupure ; F⁽ⁿ⁾=(−1)ⁿn!/aⁿ⁺¹.'],
    ['Sur α∈[a/2,3a/2], (1+tⁿ)e⁻⁽ᵃ/²⁾ᵗ contrôle tous les ordres jusqu’à n.','La densité positive sert à calculer les masses ; le signe de la dérivée dépend de n.'],
    ['Appliquer le théorème Cⁿ sous le signe intégral.','Contrôler une factorielle par changement de variable ou intégrations par parties.','Trouver un maximum et utiliser une formule exacte de queue.'],
    dict(sup='Exponentielle, dérivées successives et intégration par parties.',spe='Théorème Cⁿ des intégrales à paramètre et transformée de Laplace.',beyond='Monotonie complète et représentations par une densité positive.'),
    ['Choisir n=4,a=1 et retrouver 24.','Choisir n=8,a=0,25,L=12 : voir le maximum sortir de la fenêtre.','Augmenter L et mesurer la proportion capturée, au lieu de conclure à partir du dessin seul.'],
    'Les dérivées alternent de signe et leur valeur absolue est un moment positif. Les maxima et les queues expliquent les choix de coupure numérique.')
}
