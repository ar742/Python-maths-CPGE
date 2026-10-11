"""Douze leçons, dix-huit exercices corrigés et six guides de la fiche P24."""
LESSONS=[]
EXERCISES=[]


def lesson(lab,title,level,html):
    LESSONS.append(dict(lab=lab,title=title,level=level,html=html))


def exercise(lab,title,level,question,answer):
    EXERCISES.append(dict(lab=lab,title=title,level=level,question=question,answer=answer))


lesson('cube_leslie','TP p. 467 : comparer des émissivités, pas des températures','Sup → Spé', '''
<p>T est la température absolue d’une face, Tₐ celle de la pièce, A son aire et ε son émissivité infrarouge, comprise entre 0 et 1. σ=5,670374419×10⁻⁸ W·m⁻²·K⁻⁴ est la constante de Stefan–Boltzmann. Dans une grande enceinte noire, la puissance radiative nette sortante est :</p>
<div class='formula'>Pᵣ=εσA(T⁴−Tₐ⁴).</div>
<p>Le cube de Leslie présente des surfaces différentes à une même température. À aire, distance et orientation identiques, leurs signaux sont proportionnels à ε. Une laque blanche dans le visible peut être très émissive dans l’infrarouge. Les quatre valeurs utilisées ici sont illustratives.</p>
<p>U est la tension de la thermopile, η la fraction du rayonnement net qu’elle reçoit et G sa sensibilité en volts par watt. Alors U=GηPᵣ. Maintenir les mêmes η et G permet de comparer les surfaces. La thermopile ne mesure pas directement la puissance convective.</p>''')
lesson('cube_leslie','Relier le rayonnement à un bilan et à une équation différentielle','Sup → Spé', '''
<p>a est le côté du cube, h le coefficient de convection et Cₜₕ sa capacité thermique totale en J/K. Les six faces ont une aire a². Noter εᵢ l’émissivité de la face d’indice i et Pₑ la puissance fournie par le chauffage.</p>
<div class='formula'>Cₜₕ dT/dt=Pₑ−σa²(∑ᵢ εᵢ)(T⁴−Tₐ⁴)−6ha²(T−Tₐ).</div>
<p>À l’équilibre, le membre de gauche s’annule. Après coupure du chauffage, Pₑ=0 : le cube tend vers Tₐ. Si T est inférieur à Tₐ, les échanges nets changent de signe et réchauffent le cube.</p>
<p>Pour un petit écart δT=T−Tₐ, T⁴−Tₐ⁴≈4Tₐ³δT. La conductance totale est alors H=a²[4σTₐ³∑ᵢεᵢ+6h] en W/K, et le temps caractéristique vaut Cₜₕ/H. Le calcul du laboratoire conserve toutefois la loi T⁴.</p>''')
exercise('cube_leslie','Rapport des signaux du TP','Sup',
    '<p>Deux faces identiques en aire et en température ont ε₁=0,90 et ε₂=0,05. Elles sont observées avec la même thermopile, à même distance. Quel rapport U₁/U₂ prévoit-on ? Que se passe-t-il à T=Tₐ ?</p>',
    '<p>Les facteurs σ, A, G, η et T⁴−Tₐ⁴ se simplifient : <b>U₁/U₂=ε₁/ε₂=18</b>, si le signal net n’est pas nul. À T=Tₐ, U₁=U₂=0 : le quotient mesuré est indéfini. Le rapport des émissivités reste 18.</p>')
exercise('cube_leslie','Pourquoi soustraire le rayonnement ambiant ?','Sup',
    '<p>Une face d’aire A=0,01 m² et d’émissivité ε=0,95 est à T=373 K dans une pièce à Tₐ=293 K. Estimer la puissance radiative nette. Peut-on utiliser directement des températures en °C ?</p>',
    '<p>La loi donne <b>Pᵣ≈6,46 W</b>. Le rayonnement reçu de la pièce représente environ 3,97 W : le négliger surestime l’échange net. Les puissances quatrièmes portent sur des <b>températures absolues en kelvins</b> ; employer 100 et 20 °C serait incorrect.</p>')
exercise('cube_leslie','Temps de refroidissement près de l’ambiance','Spé',
    '<p>Un cube de côté a=0,10 m possède six faces d’émissivité 0,90. Prendre Tₐ=300 K, h=10 W·m⁻²·K⁻¹ et Cₜₕ=1000 J/K. Linéariser le bilan sans chauffage et calculer le temps caractéristique.</p>',
    '<p>La conductance radiative vaut 4σTₐ³×6×0,90×a²≈0,331 W/K ; celle de convection vaut 6ha²=0,600 W/K. Ainsi H≈0,931 W/K et <b>Cₜₕ/H≈1074 s, soit 17,9 min</b>. L’écart de température suit approximativement une exponentielle décroissante.</p>')

lesson('seebeck','Thermocouple : intégrer un coefficient local','Sup → Spé', '''
<p>Th est la température à mesurer, Tf celle de la jonction froide et V la tension à circuit ouvert. S(T) est le coefficient Seebeck effectif du couple de matériaux, en V/K. Le signe de S correspond au sens de branchement choisi.</p>
<div class='formula'>V=∫ de Tf à Th S(T)dT.</div>
<p>Pour une petite différence de température et un coefficient presque constant, V≈S(Tf)(Th−Tf). Pour une calibration plus large, choisir une température de référence Tᵣ et écrire S(T)=S₀+s₁(T−Tᵣ), où S₀ est en V/K et s₁ en V/K².</p>
<div class='formula'>V=S₀(Th−Tf)+s₁[(Th−Tᵣ)²−(Tf−Tᵣ)²]/2.</div>
<p>La dérivée de la calibration par rapport à Th vaut S(Th). Si S garde un signe strict, cette calibration est monotone et son inversion détermine une seule température.</p>''')
lesson('seebeck','Jonction froide : une mesure à compenser','Spé', '''
<p>Un voltmètre ne mesure pas Th seule : sa tension dépend aussi de Tf. Définir E(T)=∫ de Tᵣ à T S(u)du, où u est la variable d’intégration. La mesure vérifie V=E(Th)−E(Tf).</p>
<div class='formula'>E(Th)=V+E(Tf).</div>
<p>La compensation consiste donc à mesurer Tf et à ajouter sa contribution E(Tf) avant d’inverser E. Ce n’est pas nécessairement l’ajout d’une constante à la température : une calibration non linéaire doit être inversée.</p>
<p>δTf désigne une petite erreur de référence et δTh l’erreur obtenue. À tension fixée, S(Th)δTh≈S(Tf)δTf. Un coefficient variable modifie la sensibilité au biais. Le laboratoire compare cette inversion à l’approximation avec S₀ constant.</p>''')
exercise('seebeck','Retrouver une température avec S constant','Sup',
    '<p>Un thermocouple a S=40 µV/K. Sa jonction froide est à 293,15 K et sa tension vaut +5,20 mV. Déterminer la température chaude avec la convention du laboratoire.</p>',
    '<p>Th−Tf=V/S=5,20×10⁻³/(40×10⁻⁶)=130 K. Donc <b>Th=423,15 K, soit 150 °C</b>. Supposer à tort une jonction froide à 273,15 K donnerait 403,15 K.</p>')
exercise('seebeck','Intégrer plutôt que multiplier','Spé',
    '<p>Prendre Tᵣ=273,15 K, S₀=40 µV/K et s₁=0,02 µV/K². Pour Tf=293,15 K et Th=473,15 K, comparer la tension exacte à S₀(Th−Tf).</p>',
    '<p>Le terme constant vaut 7,20 mV. La correction vaut 0,02[(200)²−(20)²]/2 µV=396 µV. La tension intégrée est donc <b>7,596 mV</b>. L’approximation omet environ 5,2 % de cette tension.</p>')
exercise('seebeck','Propager une erreur de référence','Spé',
    '<p>Les coefficients locaux valent S(Tf)=40 µV/K et S(Th)=44 µV/K. La jonction froide est surestimée de δTf=2 K. Quel biais de température prévoit la linéarisation ?</p>',
    '<p>À tension inchangée, S(Th)δTh≈S(Tf)δTf. Ainsi <b>δTh≈(40/44)×2=1,82 K</b>, positif. La compensation exacte du laboratoire inclut les termes non linéaires.</p>')

lesson('peltier','Compter séparément transport, Joule et conduction','Sup → Spé', '''
<p>Tc et Th sont les températures froide et chaude en K ; ΔT=Th−Tc. I≥0 est le courant orienté pour refroidir, α le coefficient thermoélectrique du module en V/K, R sa résistance en Ω et K sa conductance thermique en W/K. Qc est la puissance thermique extraite du côté froid ; Qh celle rejetée au côté chaud. Elles sont en W.</p>
<div class='formula'>Qc=αTcI−RI²/2−KΔT ; Qh=αThI+RI²/2−KΔT.</div>
<p>Le transport Peltier est proportionnel au courant. Joule produit une puissance RI², répartie ici également entre les faces. La conduction fait revenir la chaleur du chaud vers le froid et pénalise Qc.</p>
<p>P est la puissance électrique consommée, en W : P=αΔTI+RI². Les formules donnent exactement Qh=Qc+P. À températures fixées, Qc est maximale pour I=αTc/R ; augmenter le courant au-delà renforce surtout Joule.</p>''')
lesson('peltier','Premier et second principes : discuter la performance','Spé', '''
<p>Qc est la puissance thermique extraite, Qh la puissance thermique rejetée et P la puissance électrique consommée, toutes en W. En régime de refroidissement, Qc&gt;0 et P&gt;0. Le coefficient de performance est COP=Qc/P. Un Qc négatif ne correspond pas à un COP de réfrigérateur : le côté froid est alors réchauffé.</p>
<p>La production d’entropie par unité de temps est Σ=Qh/Th−Qc/Tc. Le modèle constant donne :</p>
<div class='formula'>Σ=(RI²/2)(1/Th+1/Tc)+KΔT(1/Tc−1/Th)≥0.</div>
<p>Pour ΔT&gt;0, combiner Σ≥0 et Qh=Qc+P donne COP≤Tc/ΔT, la limite de Carnot. Le premier principe vérifie les puissances ; le second borne la performance.</p>
<p>Si le côté chaud est maintenu à Th et si une charge thermique de puissance Qcharge, en W, arrive au côté froid, l’équilibre impose Qc=Qcharge. Il donne Tc=(Qcharge+RI²/2+KTh)/(αI+K). Cette solution doit être inférieure à Th pour décrire un refroidissement.</p>''')
exercise('peltier','Vérifier un bilan sur des nombres simples','Sup → Spé',
    '<p>Prendre Tc=280 K, Th=300 K, α=0,05 V/K, R=2 Ω, K=1 W/K et I=4 A. Calculer Qc, Qh, P et le COP.</p>',
    '<p>Qc=56−16−20=<b>20 W</b> ; Qh=60+16−20=<b>56 W</b> ; P=4+32=<b>36 W</b>. On retrouve 56=20+36. Le COP vaut <b>20/36≈0,556</b>, bien inférieur à Tc/(Th−Tc)=14.</p>')
exercise('peltier','Un maximum n’est pas une garantie de refroidissement','Spé',
    '<p>À températures fixées, démontrer le courant qui maximise Qc. En déduire une condition nécessaire et suffisante pour qu’il existe un courant avec Qc&gt;0 dans le modèle non limité en courant.</p>',
    '<p>La dérivée est αTc−RI, donc <b>Ioptimal=αTc/R</b>. Le maximum vaut <b>α²Tc²/(2R)−KΔT</b>. Un refroidissement est possible exactement si ce maximum est strictement positif. Une limite technique de courant peut encore restreindre les possibilités.</p>')
exercise('peltier','Charge et température d’équilibre','Spé',
    '<p>Th=300 K, α=0,05 V/K, R=2 Ω, K=1 W/K et I=4 A. Une charge de 10 W arrive au côté froid. Trouver Tc à l’équilibre et vérifier Qc.</p>',
    '<p>Tc=(10+16+300)/(0,20+1)=<b>271,667 K</b>. Alors Qc=0,20Tc−16−(300−Tc)=1,20Tc−316=<b>10 W</b>. La température froide est bien inférieure à Th. L’évacuation de Qh côté chaud reste indispensable.</p>')

lesson('thermoacoustique','P24 : les équations de l’onde et de la chaleur se couplent','Spé · Prolongement', '''
<p>P₀, T₀ et ρ₀ sont la pression, la température et la masse volumique au repos d’un gaz parfait. γ=cₚ/cᵥ est le rapport des capacités thermiques massiques ; c²=γP₀/ρ₀ définit la célérité adiabatique. λ est la conductivité thermique. La position est x et le temps t ; p(x,t) est la surpression et τ(x,t) la variation de température.</p>
<div class='formula'>λ ∂²τ/∂x²=ρ₀cₚ ∂τ/∂t−∂p/∂t ; ρ₀cₚ=γP₀/[(γ−1)T₀].</div>
<p>La conservation de la masse, la dynamique sans viscosité et la loi du gaz parfait donnent l’autre équation : ∂²p/∂x²=(γ/c²)∂²[p−(P₀/T₀)τ]/∂t². Une compression modifie la température ; sa diffusion agit en retour sur la pression.</p>
<p>i est le nombre complexe vérifiant i²=−1 ; f est la fréquence en Hz, ω=2πf la pulsation et k le nombre d’onde. Chercher p=p₀exp(iωt−ikx) et τ=τ₀exp(iωt−ikx), où p₀ et τ₀ sont les amplitudes complexes. Le système homogène admet une solution non nulle lorsque son déterminant est nul.</p>
<div class='formula'>λq²+[iωρ₀cₚ−λγω²/c²]q−iωρ₀cₚω²/c²=0, avec q=k².</div>''')
lesson('thermoacoustique','Choisir la branche physique et lire les nombres complexes','Spé · Au-delà', '''
<p>La branche acoustique est celle qui tend vers k=ω/c lorsque λ tend vers 0. L’autre solution est une branche thermique diffusive. Elles ne représentent pas deux sons de même nature.</p>
<p>Écrire k=kᵣ+ikᵢ, avec kᵣ&gt;0. La convention exp(iωt−ikx) donne une amplitude proportionnelle à exp(kᵢx). Une onde atténuée vers x&gt;0 impose kᵢ≤0. La vitesse de phase vaut ω/kᵣ et la longueur d’onde 2π/kᵣ.</p>
<div class='formula'>τ₀/p₀=iω/(iωρ₀cₚ+λk²).</div>
<p>Le module de ce rapport est en K/Pa. Sa phase décrit le déphasage de température par rapport à la pression ; avec exp(iωt), une phase positive est une avance. Sans conduction, τ₀/p₀=(γ−1)T₀/(γP₀). Pour une conduction très forte, la célérité acoustique tend vers c/√γ, la valeur isotherme.</p>
<p>Cette expérience isole la conduction dans le volume du gaz. La viscosité, les échanges aux parois et les éléments d’un moteur thermoacoustique demanderaient d’autres équations.</p>''')
exercise('thermoacoustique','Retrouver le son adiabatique','Spé',
    '<p>Dans la relation quadratique du cours, poser λ=0. Déterminer k² et le rapport τ₀/p₀. Pourquoi la branche thermique ne reste-t-elle pas une seconde racine finie ?</p>',
    '<p>La relation devient iωρ₀cₚ(k²−ω²/c²)=0, d’où <b>k²=ω²/c²</b> et k=ω/c pour une propagation vers x&gt;0. Le rapport vaut <b>1/(ρ₀cₚ)=(γ−1)T₀/(γP₀)</b>. Le coefficient de k⁴ s’annule : l’équation perd un degré et l’autre racine part à l’infini.</p>')
exercise('thermoacoustique','Le signe de l’atténuation dépend de la convention','Spé',
    '<p>Avec la convention exp(iωt−ikx), prendre k=20−0,03i m⁻¹. Quelle fraction d’amplitude reste après 50 m ? Quel signe faudrait-il avec exp(iωt+ikx) pour la même atténuation vers x&gt;0 ?</p>',
    '<p>L’amplitude est multipliée par exp(−0,03×50)=<b>exp(−1,5)≈0,223</b>. Avec exp(iωt+ikx), l’enveloppe est exp(−Im(k)x) : il faudrait alors <b>Im(k)&gt;0</b>. Toujours développer l’exponentielle avant d’imposer un signe.</p>')
exercise('thermoacoustique','Faible conduction : vérifier une approximation','Spé · Au-delà',
    '<p>Noter β=−Im(k) l’atténuation et supposer λω/(ρ₀cₚc²)≪1. En développant k² près de ω²/c², montrer β≈λ(γ−1)ω²/(2ρ₀cₚc³). Quel effet prévoit-on si l’on double la fréquence ?</p>',
    '<p>Écrire q=ω²/c²+δq dans le polynôme et ne garder que le premier ordre en λ : δq=−iλ(γ−1)ω³/(ρ₀cₚc⁴). Puis k≈ω/c+δq c/(2ω), d’où la formule annoncée. <b>β est multipliée par 4</b> si f double dans ce régime. La résolution exacte permet de vérifier les limites de l’approximation.</p>')

lesson('piezo_resonateur','Une énergie commune impose la réciprocité','Spé', '''
<p>x est le déplacement en m, q la charge en C, k&gt;0 la raideur en N/m, C&gt;0 la capacité en F et θ le couplage en C/m, équivalent à N/V. Le modèle prend pour énergie interne :</p>
<div class='formula'>U(x,q)=kx²/2+(q−θx)²/(2C).</div>
<p>V=∂U/∂q est la tension et F=∂U/∂x la force extérieure conjuguée au déplacement. Calculer d’abord ces dérivées à x ou q fixé, puis éliminer q.</p>
<div class='formula'>q=CV+θx ; F=kx−θV.</div>
<p>La charge produite par une déformation et la force produite par une tension font intervenir le même θ. Les deux dérivées croisées de U sont égales : c’est la réciprocité. U est positive pour tout (x,q) non nul ; le couplage ne détruit pas la stabilité de ce modèle.</p>
<p>À tension imposée, employer U−Vq puis éliminer q donne kx²/2−θVx−CV²/2. La raideur vaut alors k. À charge q=0 imposée, elle vaut k+θ²/C : la condition électrique change la réponse mécanique.</p>''')
lesson('piezo_resonateur','Relier la vibration à une admittance électrique','Spé', '''
<p>m est la masse, r&gt;0 le coefficient de frottement en N·s/m et V₀ l’amplitude de la tension harmonique. Avec i²=−1 et ω la pulsation, écrire V(t)=Re[V₀exp(iωt)]. La dynamique est m x″+r x′+kx=θV. x₀ est l’amplitude complexe du déplacement : x(t)=Re[x₀exp(iωt)].</p>
<div class='formula'>x₀=θV₀/(k−mω²+iωr).</div>
<p>La charge vaut q₀=CV₀+θx₀, le courant a pour amplitude I₀=iωq₀ et l’admittance est Y=I₀/V₀. Ainsi :</p>
<div class='formula'>Y=iωC+iωθ²/(k−mω²+iωr).</div>
<p>Sans pertes, la résonance vérifie ωᵣ²=k/m. L’antirésonance, où les courants capacitif et mécanique se compensent, vérifie ωₐ²=(k+θ²/C)/m. Les fréquences valent fᵣ=ωᵣ/(2π) et fₐ=ωₐ/(2π).</p>
<p>Le curseur ζ est un amortissement relatif : r=2ζ√(km). Avec ζ&gt;0, les pics sont finis. Les repères sans pertes ne sont pas les extrema exacts de la réponse amortie. La puissance moyenne électrique V₀²Re(Y)/2 égale la dissipation rω²|x₀|²/2.</p>''')
exercise('piezo_resonateur','Deux contraintes électriques, deux raideurs','Spé',
    '<p>À partir de U(x,q), comparer la raideur lorsque q=0 et lorsque V est imposée. Avec k=10⁶ N/m, C=10⁻⁹ F et θ=0,01 C/m, quelle est la raideur à charge nulle ?</p>',
    '<p>À q=0, U=(k+θ²/C)x²/2 : la raideur vaut <b>1,10×10⁶ N/m</b>. À tension imposée, le potentiel U−Vq après élimination de q a pour dérivée seconde en x <b>k=10⁶ N/m</b>. Mélanger les variables fixées ferait perdre cette différence.</p>')
exercise('piezo_resonateur','Résonance et antirésonance d’un mode','Spé',
    '<p>m=2×10⁻⁴ kg, k=10⁶ N/m, C=10⁻⁹ F et θ=0,01 C/m. Calculer fᵣ et fₐ sans pertes. Quel rapport permet de déterminer θ²/(kC) ?</p>',
    '<p>fᵣ=√(k/m)/(2π)≈<b>11,254 kHz</b>. Comme θ²/(kC)=0,10, fₐ=fᵣ√1,10≈<b>11,803 kHz</b>. Le rapport donne <b>θ²/(kC)=(fₐ/fᵣ)²−1</b>. L’écart entre ces repères mesure le couplage du modèle.</p>')
exercise('piezo_resonateur','Vérifier la passivité par un bilan de puissance','Spé',
    '<p>Poser D=k−mω²+iωr et x₀=θV₀/D. Montrer que Re(Y)≥0 et que V₀²Re(Y)/2=rω²|x₀|²/2.</p>',
    '<p>En multipliant par le conjugué de D, <b>Re(Y)=θ²rω²/[(k−mω²)²+(rω)²]</b> est positive. Or |x₀|²=θ²V₀²/|D|² : les deux puissances sont identiques. Le signe positif provient du frottement r&gt;0 ; il contrôle la cohérence du couplage.</p>')

lesson('brouillard','Exercice 1 p. 469 : intégrer la courbe de saturation','Spé', '''
<p>T est la température absolue, Pₛₐₜ(T) la pression de saturation et L(T) la chaleur latente massique en J/kg. R=461,5 J·kg⁻¹·K⁻¹ est la constante massique de la vapeur d’eau. Elle doit être associée à une chaleur latente massique, et non molaire.</p>
<p>En assimilant la vapeur à un gaz parfait et en négligeant le volume du liquide, la relation de Clapeyron donne d ln Pₛₐₜ/dT=L(T)/(RT²). La loi de Regnault est L(T)=A−BT, avec A en J/kg et B en J·kg⁻¹·K⁻¹.</p>
<p>T* est une température de référence, P*=Pₛₐₜ(T*) et L*=L(T*). Poser A=L*+BT*. L’intégration à partir de T* donne :</p>
<div class='formula'>ln(Pₛₐₜ/P*)=−(A/R)(1/T−1/T*)−(B/R)ln(T/T*).</div>
<p>Le laboratoire représente des rapports de pression : aucune valeur de P* n’est nécessaire pour comparer les pentes. Les coefficients servent à une étude locale du mécanisme, loin du point critique.</p>''')
lesson('brouillard','Comparer les pentes avant de changer de phase','Spé', '''
<p>Une vapeur initialement saturante se détend adiabatiquement et quasistatiquement. Tant qu’elle reste seule, la loi de Laplace d’un gaz parfait donne P/P*=(T/T*)^{γ/(γ−1)}, avec γ=cₚ/cᵥ&gt;1.</p>
<p>Lors d’un petit refroidissement dT&lt;0, la saturation diminue plus vite que la pression de la vapeur si sa dérivée est plus grande au point initial. La vapeur seule ne peut alors rester à l’équilibre : la condensation commence.</p>
<div class='formula'>L*/(RT*) &gt; γ/(γ−1), soit T* &lt; A(γ−1)/[Rγ+B(γ−1)].</div>
<p>Le sens de l’inégalité vient du signe négatif de dT. À égalité des pentes, le premier ordre ne suffit pas. La carte montre la marge L*/(RT*)−γ/(γ−1) pour des états initiaux indépendants.</p>
<p>Au début de la condensation, la chaleur latente modifie l’évolution. La loi de Laplace de la vapeur seule doit s’arrêter. Les tracés ne calculent ni la quantité condensée ni l’état final du mélange : il faudrait un bilan diphasé supplémentaire.</p>''')
exercise('brouillard','Garder une même base d’unités','Sup → Spé',
    '<p>La chaleur latente massique de l’eau vaut environ 2,44×10⁶ J/kg. La masse molaire vaut M=0,018 kg/mol. Convertir la chaleur latente et la constante R en grandeurs molaires. Quel rapport doit rester inchangé ?</p>',
    '<p>L molaire vaut ML≈<b>43 920 J/mol</b> ; R molaire vaut MR≈<b>8,307 J·mol⁻¹·K⁻¹</b> avec la constante arrondie du modèle. Le rapport <b>L/R</b> est identique dans les deux bases. Employer 8,314 avec 2,44×10⁶ J/kg mélangerait les unités.</p>')
exercise('brouillard','Prévoir le début pour une vapeur d’eau','Spé',
    '<p>Prendre T*=293,15 K, L*=2,44×10⁶ J/kg, R=461,5 J·kg⁻¹·K⁻¹ et γ=1,33. Comparer les deux pentes logarithmiques à T*. Que prévoir lors d’une faible détente ?</p>',
    '<p>La pente de saturation est L*/(RT*²)≈<b>0,0615 K⁻¹</b>. La pente isentropique vaut γ/[(γ−1)T*]≈<b>0,01375 K⁻¹</b>. Pour dT&lt;0, la saturation décroît plus vite : <b>la condensation commence</b>. Il ne faut pas continuer la loi de gaz parfait seul dans le mélange.</p>')
exercise('brouillard','Retrouver l’intégrale et vérifier son signe','Spé',
    '<p>Intégrer d ln Pₛₐₜ/dT=A/(RT²)−B/(RT) entre T* et T. Vérifier la valeur en T=T* et le sens de variation si A−BT&gt;0.</p>',
    '<p>Une primitive est −A/(RT)−(B/R)ln T. La différence donne <b>−(A/R)(1/T−1/T*)−(B/R)ln(T/T*)</b>, nulle à T=T*. Si L(T)=A−BT&gt;0, d ln Pₛₐₜ/dT&gt;0 : la pression de saturation augmente avec T. Les deux termes intégrés doivent être considérés ensemble.</p>')


def guide(purpose,objects,hypotheses,techniques,levels,first_steps,expected):
    return dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,
                levels=levels,first_steps=first_steps,expected=expected)


GUIDES={
 'cube_leslie':guide('Comparer des émissivités, puis transformer les échanges thermiques en bilan du cube.',
    ['T, Tₐ : températures absolues du cube et de la pièce.','a : côté ; A=a² : aire d’une face ; ε : émissivité infrarouge.','h : convection ; Cₜₕ : capacité thermique totale ; U : signal de thermopile.'],
    ['Température uniforme et surfaces observées à même distance.','Émissivités et coefficient de convection constants ; enceinte à Tₐ.'],
    ['Écrire une puissance nette avec T⁴−Tₐ⁴.','Comparer des rapports à géométrie identique.','Établir un bilan stationnaire puis une équation différentielle.'],
    dict(sup='Unités, bilan énergétique et équation différentielle.',spe='Rayonnement, convection et linéarisation près de l’ambiance.',beyond='Étalonnage radiométrique et estimation des échanges.'),
    ['Choisir le preset TP et comparer les quatre signaux.','Rapprocher T de Tₐ : distinguer un signal nul d’une faible émissivité.','Augmenter h puis observer chauffage nécessaire et refroidissement.'],
    'Le TP compare les surfaces ; le bilan inclut aussi la convection, que la thermopile ne mesure pas.'),
 'seebeck':guide('Passer d’une tension mesurée à une température avec une référence connue.',
    ['Th : température inconnue ; Tf : température de jonction froide.','Tᵣ=273,15 K ; S₀ : coefficient à Tᵣ ; s₁ : sa pente en température.','V : tension à circuit ouvert ; δTf : erreur de référence simulée.'],
    ['Coefficient effectif S(T)>0 sur le domaine de calibration.','Courant nul ; jonctions et référence mesurées à l’équilibre.'],
    ['Intégrer un coefficient local au lieu de le multiplier aveuglément.','Inverser une fonction monotone.','Propager une petite erreur avec la différentielle.'],
    dict(sup='Primitives, unités et calibration affine.',spe='Inversion non linéaire et propagation d’incertitude.',beyond='Thermocouples réels et coefficients dépendant de la température.'),
    ['Mettre s₁=0 : retrouver V=S₀(Th−Tf).','Choisir une calibration courbe et comparer la température retrouvée à l’approximation.','Ajouter 5 K d’erreur froide et expliquer le biais avec les coefficients locaux.'],
    'Une tension de thermocouple dépend de deux températures. La compensation froide fait partie de la mesure.'),
 'peltier':guide('Décider si un module refroidit et vérifier ses bilans d’énergie et d’entropie.',
    ['Tc : côté froid ; Th=Tc+ΔT : côté chaud maintenu.','I : courant ; α : coefficient du module ; R : résistance ; K : conductance thermique.','Qc : puissance thermique extraite ; Qh : puissance thermique rejetée ; P : puissance électrique consommée. Toutes trois sont en W.'],
    ['Régime stationnaire et coefficients constants ; Joule réparti par moitié.','COP de refroidissement défini seulement pour Qc>0 et P>0.'],
    ['Séparer trois contributions à une puissance.','Optimiser une parabole et respecter une limite de courant.','Appliquer premier et second principes ; résoudre un équilibre chargé.'],
    dict(sup='Joule, conduction, signes et conservation de l’énergie.',spe='Performance, optimisation et production d’entropie.',beyond='Dissipateurs et modèles thermoélectriques dépendant de la température.'),
    ['Avec le premier preset, vérifier Qh=Qc+P.','Passer au courant excessif : repérer le rôle du terme en I².','Couper le courant, puis faire varier la charge pour discuter l’équilibre.'],
    'Un courant non nul ne garantit pas le refroidissement. Le signe de Qc décide du mode de fonctionnement.'),
 'thermoacoustique':guide('Résoudre deux équations couplées et donner un sens à un nombre d’onde complexe.',
    ['P₀, T₀, ρ₀ : état au repos ; γ : rapport des capacités ; λ : conductivité.','f : fréquence ; ω=2πf : pulsation ; k : nombre d’onde ; q=k².','p : surpression ; τ : température perturbée ; L : longueur observée.'],
    ['Petites perturbations d’un gaz parfait ; conduction axiale sans viscosité.','Convention exp(iωt−ikx), branche acoustique continue depuis λ=0.'],
    ['Passer d’équations différentielles à un système algébrique harmonique.','Annuler son déterminant et sélectionner une branche.','Lire vitesse, atténuation et phase ; vérifier des limites physiques.'],
    dict(sup='Ondes sinusoïdales et exponentielles complexes.',spe='Équation de la chaleur et dispersion d’une onde couplée.',beyond='Branche diffusive et éléments de modèles thermoacoustiques.'),
    ['Choisir λ=0 : retrouver c et la relation adiabatique entre τ et p.','Choisir une conduction renforcée : comparer vitesse et phase.','Modifier f et L ; distinguer longueur d’onde et longueur d’atténuation.'],
    'La conduction change la relation température–pression et atténue l’onde. Le signe de Im k dépend de la convention.'),
 'piezo_resonateur':guide('Déduire les effets direct et inverse d’une même énergie, puis étudier un résonateur.',
    ['x : déplacement ; q : charge ; V : tension ; θ : couplage réciproque.','m : masse ; k : raideur ; C : capacité ; ζ : amortissement relatif sans dimension. Le frottement vaut r=2ζ√(km).','Y : courant divisé par tension ; fᵣ et fₐ : repères sans pertes.'],
    ['Énergie U(x,q) positive ; m, k et C positifs, r strictement positif.','Un mode linéaire ; convention harmonique exp(iωt).'],
    ['Différencier une énergie en gardant les bonnes variables fixes.','Résoudre un oscillateur forcé en régime harmonique.','Distinguer un pic d’amplitude, une compensation de courant et un bilan de puissance.'],
    dict(sup='Énergie du ressort, condensateur et oscillateur.',spe='Dérivées croisées, potentiel adapté et admittance complexe.',beyond='Circuits équivalents de résonateurs et identification du couplage.'),
    ['Choisir le premier preset et observer l’amplification autour de fᵣ.','Renforcer θ : voir fₐ s’éloigner de fᵣ.','Augmenter ζ : le pic reste fini et le creux devient moins profond.'],
    'Résonance et antirésonance sont deux mécanismes distincts. La réciprocité et la passivité proviennent de la même énergie.'),
 'brouillard':guide('Comparer deux pentes pour décider du début d’un changement d’état.',
    ['T*, P* : état initial saturé ; L* : chaleur latente massique à T*.','B : pente de la baisse de chaleur latente, en J/(kg·K). L(T)=A−BT ; A=L*+BT* ; R=461,5 J/(kg·K).','γ : rapport des capacités ; ΔT : refroidissement exploré ; marge : différence de pentes réduites.'],
    ['Vapeur assimilée à un gaz parfait loin du point critique ; volume liquide négligé.','Loi de Laplace utilisée seulement avant condensation, pour une détente adiabatique quasistatique.'],
    ['Intégrer Clapeyron avec une loi approchée de chaleur latente.','Comparer des dérivées en tenant compte du signe de dT.','Arrêter un modèle dès que ses hypothèses cessent de s’appliquer.'],
    dict(sup='Logarithmes, intégration et comparaison de variations.',spe='Clapeyron, lois de Laplace et début de condensation.',beyond='Bilans diphasés et modèles de nucléation des gouttes.'),
    ['Prendre les valeurs de vapeur d’eau et comparer les pentes initiales.','Réduire L* : chercher la frontière de la carte où la marge s’annule.','Observer que la courbe de vapeur seule s’arrête à la condensation.'],
    'Le critère explique le début du brouillard. Il ne donne pas l’évolution ultérieure du mélange liquide–vapeur.')
}
