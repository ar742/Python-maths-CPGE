# Séries & Signaux · Exercices corrigés

60 exercices originaux. Chercher la solution avant de lire la correction et réinvestir le laboratoire associé.

## 1. Un compact éloigné de zéro a une norme exacte

**Sup → Spé · TP : couche_limite**

**Énoncé.** Pour n=100 et δ=0,05, calculer la norme sur [δ,1]. Comparer au majorant 1/(nδ) et expliquer pourquoi le maximum global n’est plus dans ce compact.

### Correction guidée

**Corrigé.** Le maximum global est à 1/n=0,01<δ. La fonction décroît donc sur [0,05,1], et la norme vaut 100×0,05/[1+(100×0,05)²]=5/26≈0,1923. Le majorant donne 1/5=0,20. Quand n augmente à δ fixé, les deux quantités tendent vers zéro. L’exclusion d’un voisinage fixe de zéro retire la couche mobile du domaine.

## 2. Une intégrale converge malgré l’échec uniforme

**Sup → Spé · TP : couche_limite**

**Énoncé.** Calculer ∫₀¹fₙ(x)dx et sa limite. Est-ce en contradiction avec l’absence de convergence uniforme ? Quelle domination permet aussi de conclure ?

### Correction guidée

**Corrigé.** Avec u=nx, l’intégrale vaut (1/(2n))ln(1+n²), qui tend vers zéro puisque ln n/n→0. Il n’y a aucune contradiction : la convergence uniforme est une condition suffisante d’interversion, pas une condition nécessaire. Ici 0≤fₙ≤1/2 sur un intervalle fini, et la convergence dominée fournit également la limite de l’intégrale.

## 3. Quantifier où passe l’aire

**Sup → Spé ; mesures au-delà · TP : concentration**

**Énoncé.** Calculer la part d’aire de fₙ entre 0 et c/n pour c>0 et n≥c. Pour c=3, quelle fraction limite de la masse est déjà dans cette fenêtre ?

### Correction guidée

**Corrigé.** Le changement u=nx donne ∫₀ᶜ/ⁿfₙ=∫₀ᶜue^(−u)du=1−(c+1)e^(−c). Pour c=3, cette fraction vaut 1−4e^(−3)≈0,80085. Environ 80 % de la masse est donc dans une fenêtre de largeur 3/n qui tend vers zéro. L’aire totale sur [0,1] tend vers 1 ; la comparaison rend visible la concentration.

## 4. Une famille à paramètre change trois régimes

**Sup → Spé ; mesures au-delà · TP : concentration**

**Énoncé.** Pour gₙ,α(x)=n^αxe^(−nx), α réel, étudier le maximum et l’aire asymptotique sur [0,1]. Déterminer les seuils de convergence uniforme et de perte d’aire.

### Correction guidée

**Corrigé.** Le maximum vaut n^(α−1)/e à x=1/n et l’aire vaut n^(α−2)[1−(n+1)e^(−n)]. La convergence simple vers zéro reste vraie pour tout α fixé. Elle est uniforme si α<1, échoue à α=1 avec une hauteur constante, et le maximum diverge si α>1. L’aire tend vers 0 pour α<2, vers 1 pour α=2 et diverge pour α>2. Les seuils de hauteur et d’aire sont donc différents.

## 5. Une borne de reste pour la somme de fonctions

**Spé · TP : tp99_original**

**Énoncé.** Sur [−2,2], on garde n=1,…,N. Calculer une borne uniforme du reste après N=100 à partir du majorant 5R⁴/(12n⁴). Quel est son ordre en N ?

### Correction guidée

**Corrigé.** La somme des queues satisfait Σn>Nn⁻⁴≤∫N^∞t⁻⁴dt=1/(3N³). Donc ‖S−SN‖∞≤5R⁴/(36N³). Avec R=2 et N=100, la borne est 80/(36×10⁶)≈2,22×10⁻⁶. L’ordre est N⁻³ ; il diffère de l’ordre n⁻⁴ d’un terme individuel, car on additionne toute une queue.

## 6. Une petite différence exige un calcul adapté

**Spé · TP : tp99_original**

**Énoncé.** Pour u=10⁻⁴, estimer cos u−1/√(1+u²). Pourquoi soustraire directement ces deux valeurs peut-il perdre des chiffres ? Quel développement donne une évaluation contrôlée ?

### Correction guidée

**Corrigé.** Le premier terme vaut −u⁴/3≈−3,33×10⁻¹⁷, tandis que les deux nombres soustraits sont proches de 1. En arithmétique flottante usuelle, leur arrondi est du même ordre que la différence recherchée. Le développement −u⁴/3+(14/45)u⁶+O(u⁸) évite cette annulation : ici la correction sextique vaut environ 3,11×10⁻²⁵, négligeable par rapport au terme quartique.

## 7. Choisir un degré avec une précision fixée

**Sup → Spé · TP : geometrie**

**Énoncé.** Sur |x|≤1/2, quel degré N suffit pour garantir |1/(1−x)−PN(x)|≤10⁻³ ? Combien de termes calcule-t-on ?

### Correction guidée

**Corrigé.** La norme exacte vaut (1/2)^(N+1)/(1/2)=2^(−N). Il faut N≥log₂1000≈9,966, donc N=10 suffit. Le polynôme comprend N+1=11 termes. À x=1/2 le reste vaut 1/1024≈0,0009766. La même valeur N ne convient pas automatiquement à r=0,95 : le compact doit entrer dans la spécification.

## 8. Au bord, un rayon ne décide pas tout

**Sup → Spé · TP : geometrie**

**Énoncé.** Comparer Σxⁿ, Σxⁿ/n et Σxⁿ/n² aux points x=1 et x=−1. Les trois rayons valent 1 ; pourquoi leurs comportements au bord sont-ils différents ?

### Correction guidée

**Corrigé.** Pour Σxⁿ, le terme ne tend pas vers zéro aux deux points, donc divergence. Pour Σxⁿ/n, à x=1 c’est l’harmonique divergente ; à x=−1 la série alternée converge conditionnellement. Pour Σxⁿ/n², la convergence est absolue aux deux points. Le rayon décrit le disque ouvert et l’extérieur ; chaque point du cercle frontière demande une étude propre.

## 9. Construire quatre termes sans dériver huit fois

**Spé · TP : arcsin_ex4**

**Énoncé.** Partir de l’EDO pour calculer le polynôme à quatre termes impairs et son résidu. Donner une majoration du reste sur |x|≤1/2.

### Correction guidée

**Corrigé.** La récurrence donne c₀=1, c₁=2/3, c₂=8/15 et c₃=16/35. Donc P₄=x+(2/3)x³+(8/15)x⁵+(16/35)x⁷. Le résidu vaut −8×(16/35)x⁸=−128x⁸/35. Le majorant du reste est (1/2)⁹/[1−(1/2)²]=1/384≈0,002604. Cette borne est suffisante mais peut être améliorée avec le premier coefficient omis.

## 10. Reconnaître une primitive et la singularité

**Spé · TP : arcsin_ex4**

**Énoncé.** Montrer que f=(1/2)[(arcsin x)²]′. En déduire une série pour (arcsin x)² et l’équivalent de f(x) quand x→1⁻.

### Correction guidée

**Corrigé.** La règle de dérivation donne [(arcsin x)²]′=2arcsin x/√(1−x²). En intégrant la série sur un compact intérieur et en utilisant arcsin0=0, (arcsin x)²=Σk≥0cₖx^(2k+2)/(k+1). Quand x→1⁻, arcsin x→π/2 et √(1−x²)~√[2(1−x)], donc f(x)~π/[2√2√(1−x)]. Cette singularité explique le rayon 1 et l’échec d’une approximation uniforme jusqu’au bord.

## 11. Une troncature avant le cœur de la somme

**Spé ; lien probabiliste · TP : asymptotique_ex5**

**Énoncé.** Pour x=30, estimer λ=e²x et l’ordre des indices significatifs. Pourquoi N=100 ne peut-il pas être choisi en se fondant seulement sur le rayon infini ?

### Correction guidée

**Corrigé.** λ≈7,389×30≈221,67. Les poids de Poisson se concentrent autour de ce nombre, avec un écart type √λ≈14,89. Une troncature à 100 est très loin avant la zone dominante et perd l’essentiel de la somme normalisée. Le rayon infini garantit la convergence pour tout x fixé, mais ne donne aucun degré uniforme permettant une bonne approximation à tous les x.

## 12. Un transfert élémentaire sans loi de probabilité

**Spé ; lien probabiliste · TP : asymptotique_ex5**

**Énoncé.** Supposer bn>0, an/bn→1 et B(x)=Σbnxⁿ croît plus vite que tout polynôme lorsque x→+∞. Démontrer A(x)/B(x)→1 pour x positif, puis l’appliquer ici.

### Correction guidée

**Corrigé.** Pour ε>0, choisir m tel que (1−ε)bn≤an≤(1+ε)bn pour n≥m. Multiplier par xⁿ≥0 et sommer la queue : les différences entre les sommes entières et ces queues sont des polynômes de degré inférieur à m. Diviser par B(x) fait disparaître ces polynômes, puis ε→0 donne le résultat. Ici bn=e^(2n)/n!, B=exp(e²x) à un polynôme près, ce qui établit l’équivalent demandé.

## 13. Calculer les coefficients et leurs signes

**Spé · TP : binomiale_ex10**

**Énoncé.** Donner les quatre premiers termes de (1−u)^(−1/2) puis de (1−u)^(3/2). Quel α faut-il utiliser pour la seconde fonction ?

### Correction guidée

**Corrigé.** Pour α=1/2, la récurrence donne 1+(1/2)u+(3/8)u²+(5/16)u³+… . La seconde fonction correspond à α=−3/2, d’où c₁=−3/2, c₂=3/8 et c₃=1/16 ; le début est 1−(3/2)u+(3/8)u²+(1/16)u³+… . Le signe ne suit pas une alternance perpétuelle : il dépend du nombre de facteurs négatifs dans (α)ₙ.

## 14. Le produit d’une série et sa dérivée

**Spé · TP : binomiale_ex10**

**Énoncé.** À partir de g(u)=(1−u)^(−1/2), montrer que (1−u)^(−3/2)=2g′(u). Retrouver le coefficient de uⁿ et le rayon.

### Correction guidée

**Corrigé.** La dérivée vaut g′=(1/2)(1−u)^(−3/2). En dérivant terme à terme sur tout compact |u|≤r<1, le coefficient de uⁿ de 2g′ est 2(n+1)binom(2n+2,n+1)/4^(n+1), égal à (2n+1)binom(2n,n)/4ⁿ. La multiplication par un facteur polynomial en n ne change pas le rayon 1. Le résultat s’obtient sans refaire toutes les dérivées.

## 15. Une correction à petite amplitude en radians

**Sup → Spé · TP : elliptique_pendule**

**Énoncé.** Déduire de la série le premier terme de T/T₀ en fonction de θ₀ lorsque θ₀→0. Estimer l’allongement relatif pour θ₀=20°.

### Correction guidée

**Corrigé.** Comme k=sin(θ₀/2)~θ₀/2, T/T₀=1+θ₀²/16+O(θ₀⁴), avec θ₀ en radians. Pour 20°=π/9≈0,3491, la correction vaut θ₀²/16≈0,007615, soit 0,762 %. Introduire 20 directement dans cette formule serait une erreur d’unité ; l’amplitude doit être convertie avant le développement.

## 16. Pourquoi la période diverge près du sommet

**Sup → Spé · TP : elliptique_pendule**

**Énoncé.** Étudier qualitativement K(k) lorsque k→1⁻. Au point k=1, que devient l’intégrande près de φ=π/2 ? Pourquoi les sommes de peu de termes sont-elles insuffisantes ?

### Correction guidée

**Corrigé.** À k=1, l’intégrande vaut 1/|cosφ| sur [0,π/2[, et cosφ~π/2−φ près du bord. Son intégrale diverge logarithmiquement. Pour k proche de 1, le pendule passe longtemps près de son point haut, où la vitesse est faible. Le facteur k²ⁿ décroît alors lentement et de nombreux termes sont nécessaires ; une approximation quadratique de sinθ ne peut représenter cette séparatrice.

## 17. Un encadrement du reste de série

**Spé · TP : integrale_sh_ex11**

**Énoncé.** Après N termes n=0,…,N−1, montrer que le reste RN est entre 1/(2N+1) et 1/(2N+1)+2/(2N+1)². Quelle valeur N garantit RN<0,01 avec cette borne ?

### Correction guidée

**Corrigé.** La fonction a(x)=2/(2x+1)² est positive décroissante. Pour la queue Σn≥Na(n), l’encadrement intégral donne ∫N∞a≤RN≤a(N)+∫N∞a, et l’intégrale vaut 1/(2N+1). Pour N=50, la borne supérieure dépasse légèrement 0,01 ; pour N=51 elle vaut environ 0,0098973. N=51 suffit donc selon cette garantie.

## 18. Le point zéro ne change pas l’aire

**Spé · TP : integrale_sh_ex11**

**Énoncé.** La somme de la série vaut 0 en t=0 si l’on y évalue les termes un par un, tandis que le prolongement de t/sinh t vaut 1. Pourquoi l’intégration reste-t-elle correcte ? Que dit cette différence de la convergence uniforme près de zéro ?

### Correction guidée

**Corrigé.** Modifier une fonction en un point ne change pas son intégrale. L’identité de série sur t>0 suffit donc au calcul impropre. Chaque somme partielle tend vers 0 lorsque t→0⁺, tandis que l’intégrande complet tend vers 1 ; pour tout N, l’erreur près de zéro tend vers 1. La convergence uniforme sur ]0,T] échoue, même si la convergence L¹ est absolue.

## 19. Une fonction complexe possède une limite fermée

**Spé · TP : dominee_ex12**

**Énoncé.** Pour f(t)=e^(iωt), calculer I et une borne de |In−I| pour n≥2. Quelle valeur n suffit à garantir une erreur au plus 0,005 indépendamment de ω ?

### Correction guidée

**Corrigé.** L’intégrale vaut I=[exp(−1+iω)−1]/(−1+iω), puisque −1+iω n’est jamais nul pour ω réel. On a |f|=1 et ‖f‖₁=1, donc l’erreur est au plus 1/[2(n−1)]. Pour une garantie 0,005, il faut n−1≥100, donc n=101 suffit. La borne ne dépend pas de la fréquence, même si l’erreur réelle peut être bien plus petite par oscillation.

## 20. Une discontinuité n’interdit pas la domination

**Spé · TP : dominee_ex12**

**Énoncé.** Prendre f=1 sur [0,0,4[ et f=−3/4 sur [0,4,1]. Calculer I et ‖f‖₁. Montrer pourquoi la valeur choisie exactement en 0,4 ne joue aucun rôle.

### Correction guidée

**Corrigé.** I=∫₀⁰,⁴e^(−t)dt−(3/4)∫₀,₄¹e^(−t)dt=1−(7/4)e^(−0,4)+(3/4)e^(−1). La norme L¹ vaut 0,4+(3/4)×0,6=0,85, donc |In−I|≤0,85/[2(n−1)]. Une valeur en un point ne modifie ni l’intégrale ni cette norme. Le théorème exige ici la continuité par morceaux et l’intégrabilité du majorant, pas une continuité globale.

## 21. Une rampe n’est pas une sortie identique décalée dès t=0

**Sup → Spé · TP : rc_reponses**

**Énoncé.** Un RC au repos reçoit u(t)=2+3t V pour t>0, avec τ=0,5 s. Calculer y(t), y′(0⁺) et le décalage asymptotique u−y. Vérifier la solution en la substituant dans la maille.

### Correction guidée

**Corrigé.** La solution est y=0,5+3t−0,5e^(−2t). À zéro elle vaut 0. Sa dérivée est 3+e^(−2t), donc y′(0⁺)=4 V/s=u(0⁺)/τ. Ensuite 0,5y′+y=(1,5+0,5e^(−2t))+(0,5+3t−0,5e^(−2t))=2+3t. Le décalage tend vers aτ=1,5 V. Le retard asymptotique n’autorise pas à remplacer la solution pour tout t par u(t−τ), qui imposerait un état initial différent.

## 22. L’aire d’une impulsion commande le saut

**Sup → Spé · TP : rc_reponses**

**Énoncé.** Un condensateur possède y(0⁻)=0,8 V. Une impulsion d’entrée d’aire A=0,6 V·s lui est appliquée avec τ=0,3 s ; l’entrée est nulle ensuite. Trouver y(0⁺), y(t>0) et son aire. Quelle grandeur distingue une impulsion d’un pas ?

### Correction guidée

**Corrigé.** L’intégration donne y(0⁺)=0,8+0,6/0,3=2,8 V, puis y(t)=2,8e^(−t/0,3). Son aire est 2,8×0,3=0,84 V·s, dont 0,24 provient de l’état initial et 0,60 de l’impulsion. Le paramètre d’une impulsion est son aire A, et non une tension de plateau : Aδ(t) a l’unité V puisque δ a l’unité s⁻¹. Un pas est décrit au contraire par une amplitude constante en volts.

## 23. Concevoir une atténuation plutôt que choisir τ au hasard

**Sup → Spé · TP : rc_bode**

**Énoncé.** On veut conserver au moins 0,95 de l’amplitude à 2 Hz et atténuer à au plus 0,10 l’amplitude à 50 Hz avec un seul RC. Déterminer les contraintes sur τ et conclure.

### Correction guidée

**Corrigé.** La première contrainte donne τ≤√(1/0,95²−1)/(4π)≈0,0262 s. La seconde donne τ≥√99/(100π)≈0,0317 s. Les intervalles ne se rencontrent pas : un RC d’ordre un ne répond pas à ce cahier des charges. Il faut modifier les spécifications ou employer un filtre plus sélectif. Ce raisonnement utilise des gains d’amplitude ; remplacer 20log par 10log sans passer à une puissance changerait le sens des données.

## 24. Reconstruire deux harmoniques avec leurs phases

**Sup → Spé · TP : rc_bode**

**Énoncé.** Pour τ=1/(2π) s, u(t)=cos(2πt)+(1/3)cos(6πt). Donner le régime permanent de la sortie et les gains en dB à 1 et 3 Hz.

### Correction guidée

**Corrigé.** On a ωτ=1 pour 1 Hz et 3 pour 3 Hz. La sortie est (1/√2)cos(2πt−π/4)+(1/(3√10))cos(6πt−arctan3). Les gains valent −3,010 dB et −10 dB. Le coefficient 1/3 était déjà dans l’entrée et ne doit pas être compté dans le gain propre du filtre. Le rapport entre les harmoniques change, ce qui modifie la forme du signal.

## 25. Retrouver l’amortissement à partir du dépassement

**Spé, physique et SI selon filière · TP : rlc_poles**

**Énoncé.** Une réponse au pas de gain statique 1 dépasse sa valeur finale de 20 %. Calculer ζ, puis ω₀ si le premier maximum est observé à 0,40 s.

### Correction guidée

**Corrigé.** Avec L=−ln0,20≈1,609, L=πζ/√(1−ζ²), donc ζ=L/√(π²+L²)≈0,456. Puis ωd=π/0,40≈7,854 rad/s et ω₀=ωd/√(1−ζ²)≈8,83 rad/s. Cette identification repose sur le modèle du second ordre au repos ; un zéro, un état initial ou d’autres modes pourraient modifier le dépassement.

## 26. La limite critique crée un facteur t

**Spé, physique et SI selon filière · TP : rlc_poles**

**Énoncé.** Montrer que la réponse impulsionnelle précédente tend vers ω₀²te^(−ω₀t) lorsque ζ→1⁻. En déduire la réponse critique au pas.

### Correction guidée

**Corrigé.** Lorsque ζ→1⁻, ωd→0 et sin(ωdt)/ωd→t pour chaque t fixé. Le facteur exponentiel tend vers e^(−ω₀t), d’où hcrit=ω₀²te^(−ω₀t). En intégrant de zéro à t, ycrit=1−(1+ω₀t)e^(−ω₀t). Sa dérivée est positive pour t>0, son départ et sa valeur finale sont respectivement 0 et 1. Cela retrouve la solution à pôle double sans diviser par deux pôles qui se confondent.

## 27. Choisir une borne pour une précision garantie

**Spé · TP : dirichlet_abel**

**Énoncé.** On approxime I par ∫₀ᴸ sin(t)/t dt. Quelle borne L suffit pour garantir une erreur au plus 0,01 d’après l’estimation générale ? Pourquoi un résultat numérique proche de π/2 avec L=20 ne donne-t-il pas cette garantie ?

### Correction guidée

**Corrigé.** La borne 2/L≤0,01 impose L≥200. Elle est suffisante, pas nécessaire : certaines phases de L annulent partiellement la queue. À L=20, la majoration ne donne que 0,10 ; une petite erreur observée peut provenir d’une compensation circonstancielle. La précision de la quadrature sur [0,L] doit aussi être séparée de l’erreur de troncature.

## 28. Généraliser l’échelle de l’intégrale de Dirichlet

**Spé · TP : dirichlet_abel**

**Énoncé.** Pour b>0 et p>0, calculer J(p,b)=∫₀^∞ e^(−pt)sin(bt)/t dt. Déterminer sa limite quand p→0⁺ et le résultat pour b<0.

### Correction guidée

**Corrigé.** En dérivant par rapport à b sous domination exponentielle, ∂bJ=∫₀^∞ e^(−pt)cos(bt)dt=p/(p²+b²), avec J(p,0)=0. Donc J=arctan(b/p). Pour b>0 la limite vaut π/2 ; pour b<0 elle vaut −π/2 par imparité. Une dilatation t↦bt explique l’indépendance en la valeur positive de b pour l’intégrale non amortie.

## 29. Lire une durée à partir de zéros spectraux

**Sup → Spé · TP : porte_sinc**

**Énoncé.** Une porte réelle d’amplitude A=3 V possède un premier zéro positif à 5 Hz et est centrée en t₀=0,12 s. Calculer sa durée, sa transformée en zéro et sa phase à 1 Hz.

### Correction guidée

**Corrigé.** La durée est L=1/5=0,20 s. On a f̂(0)=AL=0,60 V·s. À 1 Hz, sincₙ(0,20)>0, donc la phase est −2π×1×0,12=−0,24π rad, soit −43,2°. Au-delà d’un zéro où la sinc change de signe, un π supplémentaire entre dans l’argument : une droite de phase seule ne décrit pas tous les lobes.

## 30. Une porte d’aire 1 prépare la distribution de Dirac

**Sup → Spé · TP : porte_sinc**

**Énoncé.** Poser dε(t)=Π(t/ε)/ε. Montrer que son aire vaut 1, sa TF vaut sincₙ(εν), et que ∫dε(t)φ(t)dt→φ(0) pour toute fonction test continue près de zéro. Est-ce une convergence uniforme de fonctions ?

### Correction guidée

**Corrigé.** L’aire vaut ε/ε=1 et la formule de la porte donne d̂ε=sincₙ(εν), qui tend vers 1 à fréquence fixée. L’action sur φ est la moyenne (1/ε)∫₋ε/₂^ε/₂φ(t)dt ; son écart à φ(0) est majoré par le maximum de |φ(t)−φ(0)| sur ce petit intervalle, donc tend vers zéro. La hauteur 1/ε diverge et aucune fonction limite uniforme n’apparaît : il s’agit de convergence au sens des distributions.

## 31. Séparer amplitude et largeur d’énergie

**Sup → Spé ; incertitude en prolongement · TP : gaussienne**

**Énoncé.** Pour A=2 et σ=0,40 s, calculer E, Δt, Δν et leur produit. Qu’arrive-t-il en remplaçant A par 1 ?

### Correction guidée

**Corrigé.** E=4×0,40√π≈2,836 unités d’amplitude²·s. Δt≈0,2828 s, Δν≈0,2813 Hz et leur produit≈0,07958=1/(4π). Avec A=1, E est divisé par quatre, tandis que les densités normalisées et les écarts types restent identiques. Employer σ=0,40 comme écart type de |f|² donnerait un facteur √2 erroné.

## 32. Pourquoi la porte ne sature pas la même borne

**Sup → Spé ; incertitude en prolongement · TP : gaussienne**

**Énoncé.** Comparer f(t)=Π(t/L) à une gaussienne. La durée finie de la porte entraîne-t-elle un Δν fini ? Examiner ∫ν²|f̂(ν)|²dν.

### Correction guidée

**Corrigé.** La transformée vaut L sincₙ(Lν). Donc ν²|f̂|²=sin²(πLν)/π², dont l’intégrale sur ℝ diverge. La porte possède un Δt fini mais un Δν infini dans ce sens. Le produit largeur entre premiers zéros × durée est une autre mesure, qui reste utile mais n’est pas l’incertitude par moments quadratiques. La discontinuité de la porte produit ici la queue spectrale trop lente.

## 33. Un trapèze calculé par des intervalles

**Sup → Spé · TP : convolution_portes**

**Énoncé.** Deux portes de largeurs 1 s et 3 s sont centrées en 0 et 2 s. Déterminer support, plateau, hauteur maximale et aire de leur convolution.

### Correction guidée

**Corrigé.** Le centre du résultat est d=2 s. Son support fermé est [2−(1+3)/2,2+(1+3)/2]=[0,4]. Le plateau existe pour |t−2|≤(3−1)/2=1, donc t∈[1,3], à hauteur min(1,3)=1 s. Les bords montent et descendent linéairement sur une seconde. L’aire vaut L₁L₂=3 s² ; on la retrouve par le rectangle central d’aire 2 et deux triangles d’aire 1/2 chacun.

## 34. Un triangle d’aire 1 et son spectre

**Sup → Spé · TP : convolution_portes**

**Énoncé.** Poser qL(t)=Π(t/L)/L. Calculer qL*qL et sa TF ; vérifier l’aire et la valeur au centre. Que devient cette famille quand L→0 ?

### Correction guidée

**Corrigé.** La convolution vaut (1/L)(1−|t|/L) pour |t|<L et 0 sinon. Sa TF est sincₙ²(Lν), son aire est 1 et sa valeur au centre est 1/L. Elle agit sur une fonction test comme une moyenne triangulaire de support rétrécissant, donc tend vers δ au sens des distributions. Son point haut diverge ; il ne s’agit pas de convergence uniforme vers une fonction ordinaire.

## 35. Une série uniforme ne peut créer un saut

**Spé ; premières harmoniques accessibles en Sup · TP : gibbs_fourier**

**Énoncé.** Montrer sans calcul de maximum que les sommes de Fourier d’un créneau ne convergent pas uniformément sur une période entière. Cela interdit-il la convergence en moyenne quadratique ?

### Correction guidée

**Corrigé.** Chaque somme partielle est continue. Une limite uniforme de fonctions continues serait continue, tandis que le créneau et sa version à demi-somme restent discontinus aux raccords. La convergence uniforme est donc impossible sur toute la période. Elle n’interdit pas la convergence L² : les coefficients en 1/k donnent une somme de carrés convergente et Parseval contrôle l’énergie du reste.

## 36. Le triangle normalisé possède une série normale

**Spé ; premières harmoniques accessibles en Sup · TP : gibbs_fourier**

**Énoncé.** Pour le triangle f(t)=|2t/T| sur [−T/2,T/2], prolongé périodiquement, retrouver sa moyenne et justifier la convergence normale de f=1/2−(4/π²)Σk≥0 cos[2π(2k+1)t/T]/(2k+1)².

### Correction guidée

**Corrigé.** La moyenne de |2t/T| sur une période vaut 1/2. La fonction est paire ; les coefficients sinusoïdaux sont nuls. Deux intégrations par parties par morceaux donnent an=−4/(π²n²) pour n impair et 0 pour n pair. La série des normes est majorée par (4/π²)Σ1/(2k+1)², convergente. La limite est donc continue et uniforme, en cohérence avec les raccords continus du triangle.

## 37. Retrouver ζ(2) à partir d’un créneau

**Spé · TP : parseval_spectre**

**Énoncé.** Sachant Σk≥0 1/(2k+1)²=π²/8, calculer Σn≥1 1/n². Quel pourcentage de l’énergie du créneau est contenu dans sa première harmonique ?

### Correction guidée

**Corrigé.** En séparant les pairs, ζ(2)=π²/8+ζ(2)/4, donc ζ(2)=π²/6. La première harmonique contribue b₁²/2=8/π²≈0,8106, soit 81,06 % de l’énergie moyenne totale. Ce nombre n’est pas le pourcentage d’amplitude ou une erreur uniforme : le créneau reste mal reproduit près de ses sauts malgré une forte énergie capturée.

## 38. Un triangle et la puissance quatrième

**Spé · TP : parseval_spectre**

**Énoncé.** Pour un triangle entre 0 et 1, E=1/3 et a₀=1. Les coefficients non constants valent −4/(π²n²) pour n impair. Déduire les sommes sur les impairs et sur tous les entiers en puissance quatrième.

### Correction guidée

**Corrigé.** Parseval donne 1/3=1/4+(8/π⁴)Σimpairs1/n⁴. La différence 1/12 conduit à Σimpairs1/n⁴=π⁴/96. Puis ζ(4)=π⁴/96+ζ(4)/16, donc ζ(4)=π⁴/90. La composante continue ne doit pas être oubliée : elle porte à elle seule une énergie 1/4, et son absence changerait la somme obtenue.

## 39. Dimensionner une troncature proche de r=1

**Spé ; prolongement harmonique · TP : poisson_noyau**

**Énoncé.** Pour r=0,9, combien d’harmoniques N suffisent à garantir un reste uniforme au plus 0,01 ? Utiliser seulement la majoration géométrique.

### Correction guidée

**Corrigé.** La condition 2×0,9^(N+1)/0,1≤0,01 équivaut à 0,9^(N+1)≤0,0005. Donc N+1≥ln(0,0005)/ln(0,9)≈72,14. Le plus petit entier satisfaisant cette borne est N=72. Il s’agit d’une garantie suffisante ; les annulations peuvent réduire l’erreur ailleurs. Le ralentissement lorsque r approche 1 relie concrètement convergence normale et coût du calcul.

## 40. Un filtrage qui garde exactement la moyenne

**Spé ; prolongement harmonique · TP : poisson_noyau**

**Énoncé.** Un signal possède c₀=3, c₁=c₋₁=1 et c₂=c₋₂=1/2. Écrire sa version filtrée par le noyau avec r=1/2. Calculer l’énergie avant et après.

### Correction guidée

**Corrigé.** L’entrée vaut 3+2cos(2πt/T)+cos(4πt/T). Les coefficients deviennent c₀=3, c±1=1/2 et c±2=1/8, donc la sortie vaut 3+cos(2πt/T)+(1/4)cos(4πt/T). Parseval donne Eavant=9+2+1/2=11,5 et Eaprès=9+1/2+1/32=9,53125. La moyenne reste 3, tandis que l’énergie des variations décroît.

## 41. Une moyenne qui ne dépend pas du recouvrement

**Spé ; prolongement harmonique · TP : poisson_gaussienne**

**Énoncé.** Une gaussienne de largeur σ=0,30 s est répétée toutes les T=1,50 s. Trouver la moyenne de la périodisation et le rapport c₁/c₀. Interpréter les unités.

### Correction guidée

**Corrigé.** La moyenne vaut c₀=σ√(2π)/T≈0,5013. Le rapport c₁/c₀=e^(−2π²(0,30/1,50)²)≈0,4540. La TF ŝ a l’unité seconde pour une amplitude sans unité ; la division par T donne des coefficients sans unité. La moyenne est l’aire d’une impulsion divisée par la période, même lorsque les impulsions se recouvrent.

## 42. Choisir le côté rapide d’une identité

**Spé ; prolongement harmonique · TP : poisson_gaussienne**

**Énoncé.** Estimer Σk∈ℤe^(−π·0,01·k²) en utilisant la forme duale. Quelle valeur dominante apparaît, et quel ordre de grandeur a le premier terme omis si l’on garde seulement n=0 ?

### Correction guidée

**Corrigé.** Poisson donne 10Σn∈ℤe^(−100πn²), donc la valeur dominante est 10. Les deux premiers termes non nuls donnent une correction 20e^(−100π), inférieure à 10⁻¹³⁴ ; les autres sont beaucoup plus petits. La somme directe possède au contraire plusieurs termes significatifs autour de zéro. L’exemple montre l’intérêt algorithmique de la transformée, au-delà d’une simple vérification graphique.

## 43. Un paquet possède une bande entière, pas une seule fréquence

**Spé ; signal selon filière · TP : shannon**

**Énoncé.** Pour B=3 Hz et f₀=5 Hz, tracer mentalement le support de ŝ. Parmi F=12,16,24 Hz, quelle fréquence possède une marge strictement positive ? Une somme sinc finie y est-elle exacte partout ?

### Correction guidée

**Corrigé.** Les bandes sont [2,8] et [−8,−2] Hz ; W=8. Le critère strict est F>16. F=12 entraîne un chevauchement des copies, F=16 est le bord sans marge et F=24 laisse une marge. À F=24, l’identité exacte exige tous les n∈ℤ. Une somme finie reste une approximation ; en particulier des échantillons extérieurs à la fenêtre affichée contribuent encore à l’intérieur.

## 44. Vérifier l’interpolation ne vérifie pas le théorème

**Spé ; signal selon filière · TP : shannon**

**Énoncé.** Soit rM(t)=Σn=−Mᴹs(n/F)sincₙ(Ft−n). Montrer que rM(j/F)=s(j/F) pour |j|≤M, même lorsque F est trop faible. Pourquoi la réussite aux points mesurés ne détecte-t-elle pas l’aliasing ?

### Correction guidée

**Corrigé.** À t=j/F, toutes les sinc sauf n=j s’annulent, donc rM(j/F)=s(j/F). Cette propriété algébrique ne dépend pas du support spectral. Un signal replié peut partager les mêmes mesures avec un autre signal à bande plus basse ; la reconstruction les interpole mais choisit alors cette autre possibilité entre les instants. Le contrôle spectral doit précéder la comparaison des points.

## 45. Deux fréquences exactes, une seule suite

**Sup → Spé · TP : aliasing**

**Énoncé.** Un capteur mesure à 30 Hz un signal sin(2π·23t+π/6). Trouver son représentant signé et une écriture à fréquence positive donnant les mêmes échantillons.

### Correction guidée

**Corrigé.** Le représentant est 23−30=−7 Hz. La suite est celle de sin(−2π·7t+π/6), soit sin(2π·7t+5π/6). La différence des arguments entre 23 et −7 Hz vaut 2πk aux instants k/30. Entre ces instants les courbes diffèrent ; aucune méthode fondée sur ces seules mesures ne peut choisir la fréquence physique sans hypothèse supplémentaire.

## 46. À Nyquist, une sinusoïde peut disparaître

**Sup → Spé · TP : aliasing**

**Énoncé.** Pour F=40 Hz et f=20 Hz, comparer les phases 0, π/2 et π/6. Peut-on déduire toute la phase d’une suite non nulle ?

### Correction guidée

**Corrigé.** Les suites valent respectivement 0, (−1)ᵏ et (1/2)(−1)ᵏ. La mesure ne connaît que sinφ ; π/6 et 5π/6 donnent donc la même suite. Une phase 0 ou π efface entièrement une sinusoïde pourtant non nulle entre les points. Ce contre-exemple justifie une marge stricte dans une expérience de mesure de sinusoïdes arbitraires.

## 47. Un ordre minimal chiffré

**Spé ; SI et physique selon filière · TP : anti_repliement**

**Énoncé.** Avec fc=10 Hz, on impose une amplitude parasite à 60 Hz inférieure à 1 % de l’amplitude initiale. Calculer l’ordre Butterworth minimal, puis le gain à 3 Hz.

### Correction guidée

**Corrigé.** Il faut n≥ln9999/(2ln6)≈2,57, donc n=3. Le gain à 60 Hz vaut 1/√(1+6⁶)≈0,00463, inférieur à 0,01. À 3 Hz, le gain est 1/√(1+0,3⁶)≈0,999636. Le calcul porte sur des amplitudes, d’où le seuil −40 dB pour 1 %. L’ordre 2 ne suffit pas : son gain à 60 Hz vaut environ 0,0278.

## 48. Un parasite replié sur le signal utile devient indissociable

**Spé ; SI et physique selon filière · TP : anti_repliement**

**Énoncé.** Un signal utile de 8 Hz et un parasite de 42 Hz sont mesurés à F=50 Hz. Montrer que le parasite se replie sur la même fréquence absolue. Un passe-bas numérique peut-il séparer les deux contributions ?

### Correction guidée

**Corrigé.** Le représentant signé de 42 Hz est 42−50=−8 Hz. Pour des signaux réels, cela correspond à une composante de 8 Hz avec une phase adaptée. Après mesure, les deux contributions occupent la même fréquence et se combinent en amplitude et phase. Un filtre numérique agissant sur 8 Hz modifie les deux ensemble ; la distinction requiert une hypothèse supplémentaire ou un filtrage analogique préalable.

## 49. Calibrer une raie exactement sur une case

**Spé ; prolongement numérique · TP : fenetres_fft**

**Énoncé.** Un cosinus d’amplitude 2 à 10 Hz est mesuré à 128 Hz sur N=256 points, sans fenêtre autre que la rectangulaire. Trouver l’indice de sa case positive et son module DFT. Refaire avec une fenêtre de Hann périodique.

### Correction guidée

**Corrigé.** Le pas est 128/256=0,5 Hz, donc j=20. La raie positive vaut N×2/2=256 ; le doublement monolatéral et la division par N redonnent 2. La Hann périodique a Σw=N/2=128 ; pour cette raie isolée, son module central vaut AΣw/2=128 et 2|X|/Σw redonne encore 2. Les cases voisines sont remplies par le lobe de la fenêtre.

## 50. Des zéros changent une grille, pas une acquisition

**Spé ; prolongement numérique · TP : fenetres_fft**

**Énoncé.** Avec N=128 à F=128 Hz, comparer une FFT de 128 points et une FFT après ajout de zéros jusqu’à 1024 points. Donner les pas et la durée de mesure. Quelles informations restent identiques ?

### Correction guidée

**Corrigé.** La durée d’acquisition reste T=1 s et le pas natif est 1 Hz. Le zero padding donne un pas de lecture 0,125 Hz. Les 128 valeurs mesurées, la fenêtre temporelle, ses lobes et le bruit acquis restent identiques. Le spectre est mieux interpolé ; deux raies que le lobe ne sépare pas ne deviennent pas séparées parce que l’on affiche davantage de points.

## 51. Mesurer un écart avec des battements

**Sup → Spé ; expérimentation numérique · TP : resolution**

**Énoncé.** Deux sons proches présentent des maxima d’enveloppe toutes les 0,40 s. Calculer l’écart de fréquences et la date du premier minimum si les deux cosinus sont en phase en t=0. Une acquisition de 0,10 s contient-elle un battement complet ?

### Correction guidée

**Corrigé.** L’écart vaut Δf=1/0,40=2,5 Hz. Le premier minimum arrive à 1/(2Δf)=0,20 s. Une durée de 0,10 s ne couvre pas même ce premier minimum ; elle contient seulement une portion du motif de battement. La précision d’une analyse paramétrique peut dépendre du modèle et du bruit, mais la fenêtre ne présente pas directement un cycle complet.

## 52. Comparer durée et interpolation

**Sup → Spé ; expérimentation numérique · TP : resolution**

**Énoncé.** Pour F=128 Hz, comparer N=64 avec padding 8 et N=512 avec padding 1. Les deux grilles spectrales ont-elles le même pas ? Leurs lobes de Hann ont-ils la même largeur ?

### Correction guidée

**Corrigé.** Les deux calculs affichent un pas 128/512=0,25 Hz. Pourtant les durées sont respectivement 0,5 s et 4 s. Les largeurs entre premiers zéros de Hann sont environ 4/T, soit 8 Hz et 1 Hz. Une grille identique masque donc des résolutions très différentes : dans le premier cas on a interpolé une acquisition courte, dans le second acquis huit fois plus longtemps.

## 53. Calculer une fréquence instantanée

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Énoncé.** Un chirp passe de 8 Hz à 48 Hz en 3 s. Écrire sa phase, sa fréquence à 1,2 s et le nombre de périodes de phase accumulées pendant les 3 s.

### Correction guidée

**Corrigé.** La pente vaut k=(48−8)/3=40/3 Hz/s. La phase est 2π(8t+(20/3)t²), à une constante près. À 1,2 s, ν=8+(40/3)×1,2=24 Hz. Le nombre de périodes accumulées est ∫₀³ν(t)dt=8×3+(40/3)×9/2=84. Ce nombre dépend de la fréquence moyenne 28 Hz, et non uniquement de la fréquence finale.

## 54. Une carte relative n’est pas un niveau absolu

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Énoncé.** La carte emploie D=10log₁₀(P/Pmax). Quelle puissance relative représentent −20 dB et −40 dB ? Si l’amplitude du chirp est doublée, la carte renormalisée change-t-elle ?

### Correction guidée

**Corrigé.** −20 dB correspond à P/Pmax=10⁻² et −40 dB à 10⁻⁴. Doubler l’amplitude multiplie toutes les puissances par quatre, y compris Pmax ; les rapports restent identiques et la carte relative ne change pas. Pour une calibration absolue, il faudrait conserver les unités et une référence de puissance fixe. Le logarithme de puissance utilise 10log, contrairement au 20log d’un rapport d’amplitudes.

## 55. Puissance d’une modulation AM

**Sup → Spé ; communications en prolongement · TP : modulation**

**Énoncé.** Pour m=0,8 et une porteuse d’amplitude 1, calculer les amplitudes des bandes latérales et l’énergie moyenne totale du signal idéal. Quelle fraction vient de la porteuse ?

### Correction guidée

**Corrigé.** Les deux bandes ont chacune amplitude m/2=0,4. Pour des fréquences distinctes sur une moyenne longue, les cosinus sont orthogonaux : la puissance vaut 1/2+2×0,4²/2=0,66. La porteuse fournit 0,50/0,66≈75,76 %. Plus généralement P=(1/2)(1+m²/2). Le bilan ne s’obtient pas en additionnant les amplitudes, mais leurs carrés avec le facteur 1/2.

## 56. Phase perdue et oscillateur local désaccordé

**Sup → Spé ; communications en prolongement · TP : modulation**

**Énoncé.** Un démodulateur synchrone a Δf=0 et φ=60°. Quelle fraction d’amplitude récupère-t-il ? Avec φ=0 et Δf=0,5 Hz, à quelle première date le signal démodulé est-il multiplié par zéro ?

### Correction guidée

**Corrigé.** À fréquence correcte, le gain cos60° vaut 1/2 : il récupère la moitié de l’amplitude du signal de base, y compris sa composante moyenne. Avec Δf=0,5 Hz, le facteur est cos(πt) ; son premier zéro arrive à t=0,5 s. Ce battement ne vient pas du message mais du désaccord local. Le modèle supprime analytiquement les fréquences proches de 2fc et suppose un canal idéal.

## 57. Fixer le signe du retard

**Spé ; mesure et probabilités · TP : correlation_retard**

**Énoncé.** Si f(t)=g(t−0,60), exprimer Cfg(τ) avec Cgg. Pour une vitesse c=350 m/s, calculer la distance d’aller-retour et le pas de distance correspondant à 200 Hz.

### Correction guidée

**Corrigé.** Cfg(τ)=∫ḡ(t)g(t+τ−0,60)dt=Cgg(τ−0,60), donc le maximum principal est attendu à τ=0,60 s. La distance vaut 350×0,60/2=105 m et le pas vaut 350/(2×200)=0,875 m. Si l’on échangeait f et g, le pic passerait au retard opposé ; annoncer la convention est donc nécessaire.

## 58. Une corrélation maximale n’est pas une certitude statistique

**Spé ; mesure et probabilités · TP : correlation_retard**

**Énoncé.** Pourquoi une forte corrélation près du retard attendu est-elle utile, mais ne suffit-elle pas à garantir une distance exacte ? Citer trois sources d’écart déjà présentes dans le banc et proposer une comparaison contrôlée.

### Correction guidée

**Corrigé.** La corrélation additionne des produits sur toute l’impulsion et favorise une forme connue, mais le bruit possède aussi des projections sur cette forme. Ici la réalisation finie du bruit, la grille de 5 ms et les maxima secondaires de l’impulsion modulée peuvent déplacer le pic ; la troncature joue aussi. Garder le retard et la vitesse fixes, augmenter le bruit puis changer la graine distingue un comportement moyen de la réussite d’une réalisation particulière. Aucune probabilité d’erreur chiffrée ne découle du seul maximum affiché.

## 59. Réduire le bruit sans oublier le retard

**Spé ; prolongement numérique · TP : debruitage**

**Énoncé.** Une moyenne glissante causale de M=9 mesures fonctionne à F=128 Hz. Pour un bruit blanc d’écart type 0,6, calculer l’écart type de sortie théorique et le retard de groupe de la moyenne.

### Correction guidée

**Corrigé.** Le facteur de variance est 1/9, donc l’écart type devient 0,6/3=0,2. La réponse harmonique est une exponentielle e^(−iω(M−1)/2) multipliée par un quotient de sinus ; hors changement de signe, son retard est (M−1)/(2F)=8/256=0,03125 s. Cette baisse du bruit n’empêche ni atténuation de certaines fréquences ni décalage du signal.

## 60. Récursif : somme infinie et gain statique

**Spé ; prolongement numérique · TP : debruitage**

**Énoncé.** Pour yk=ρyk−1+(1−ρ)xk, 0<ρ<1, déterminer la réponse impulsionnelle, son gain statique et le facteur de variance. Comparer sa mémoire au repos initial et au régime permanent.

### Correction guidée

**Corrigé.** Au repos, une impulsion en k=0 produit hj=(1−ρ)ρʲ pour j≥0. Leur somme vaut 1 : une entrée constante est retrouvée après le transitoire. Le facteur de variance vaut (1−ρ)/(1+ρ). Pour ρ=e^(−1/M), le transitoire décroît en environ M échantillons par facteur e ; une réalisation commencée en y−1=0 n’est pas immédiatement stationnaire. Écarter un début de signal rend la comparaison au bilan stationnaire plus pertinente.
