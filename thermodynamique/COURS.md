# Chaleur & Transferts — 60 leçons

Recueil de A. R., fiches P22–P24, pages 450–470. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.

## 01. Du bilan local à un profil stationnaire

Sup → Spé · Laboratoire `fourier_barre`

Une barre a longueur L en mètres, section S en m² et conductivité λ en W/(m·K). T(x) est sa température ; j est le courant thermique surfacique en W/m², positif vers +x. Les deux bords sont à T₁ et T₂.

Fourier donne **j=−λT′** : la chaleur va vers les températures décroissantes. Sans source et en régime permanent, un petit tronçon reçoit autant de puissance qu’il en transmet, donc j′=0. Pour λ constant, T″=0.

Les deux valeurs au bord imposent T=T₁+(T₂−T₁)x/L, puis j=λ(T₁−T₂)/L. La puissance totale est Φ=jS, en watts. Doubler la section double Φ sans changer j. Si T₁<T₂, j et Φ deviennent négatifs : c’est une inversion physique du transfert.

## 02. Résistance thermique et limites de l’analogie électrique

Sup · Laboratoire `fourier_barre`

R est la résistance thermique de la barre, en K/W ; ΔT=T₁−T₂ est la différence orientée des températures. La relation **ΔT=RΦ** donne R=L/(λS).

Elle ressemble à U=RI : différence de température et tension jouent des rôles analogues, comme puissance thermique et courant électrique. L’analogie aide à assembler des parois ; elle ne signifie pas que la chaleur est une quantité conservée dans tous les régimes. En transitoire, un tronçon peut stocker de l’énergie interne.

À ΔT=0, la puissance est nulle mais R n’a pas disparu : c’est une propriété géométrique et matérielle. Les écarts en °C et en K sont identiques ; convertir les températures absolues n’est nécessaire que lorsqu’une loi utilise T elle-même, par exemple un calcul d’entropie.

## 03. Quatre résistances traversées par une même puissance

Sup → Spé · Laboratoire `paroi_composite`

S est l’aire du mur ; e₁,e₂ ses épaisseurs et λ₁,λ₂ les conductivités. hᵢ,hₑ sont les coefficients de convection, en W/(m²·K). Les températures de l’air sont imposées de chaque côté.

Une couche plane a résistance e/(λS). Une interface avec l’air échange la puissance hS(Tsurface−Tair), donc a résistance 1/(hS). En permanent sans source, la même puissance Φ traverse les deux couches et les deux échanges.

La résistance totale est **R=1/(hᵢS)+e₁/(λ₁S)+e₂/(λ₂S)+1/(hₑS)**. On calcule Φ=(Tint−Text)/R, puis chaque chute de température ΦRᵢ. Les températures de l’air et des surfaces ne sont pas égales en général. Le tableau distingue les cinq lieux.

## 04. Où une amélioration sera-t-elle utile ?

Spé · Laboratoire `paroi_composite`

Rᵢ est la résistance d’un élément et Rtotal leur somme. Sa part Rᵢ/Rtotal donne aussi sa part de la chute de température lorsque Φ est uniforme.

Si l’isolant représente presque toute la résistance, augmenter sa conductivité augmente fortement la perte ; améliorer une convection déjà très efficace change peu le résultat. Inversement, un faible coefficient h peut limiter l’ensemble.

Avec les autres éléments fixés, Φ(e₂)=ΔT/[Rautres+e₂/(λ₂S)]. Le gain d’épaisseur suit une loi décroissante mais n’efface pas les autres résistances. Pour plusieurs surfaces indépendantes en parallèle, ce sont les puissances qui s’additionnent et 1/Réquiv=Σ1/Rᵢ. Une fuite thermique peut donc contourner une couche très isolante.

## 05. La surface change pendant le transfert radial

Spé · Laboratoire `isolation_radiale`

Rᵢ est le rayon intérieur, Rₑ le rayon extérieur, λ la conductivité et Φ la puissance totale sortante. h est le coefficient de convection extérieure, en W/(m²·K). Dans un cylindre de longueur L, la surface à rayon r vaut 2πrL ; dans une sphère elle vaut 4πr².

En permanent Φ est constant, mais j=Φ/S(r) varie avec r. Intégrer Fourier entre les deux rayons donne **Rcyl=ln(Rₑ/Rᵢ)/(2πλL)** et **Rsph=(1/Rᵢ−1/Rₑ)/(4πλ)**. Une formule plane avec une seule surface ne conviendrait pas à une coque épaisse.

La surface extérieure échange avec l’air par convection : ajouter 1/[hS(Rₑ)]. Sa température se calcule par Tsurface=Tint−ΦRcond ; l’écart restant avec l’air alimente la convection.

## 06. Le rayon critique vient d’une compétition

Spé · Laboratoire `isolation_radiale`

h est le coefficient de convection extérieur. Ajouter une épaisseur augmente la résistance conductrice, mais agrandit la surface convective et réduit sa résistance.

Pour le cylindre, dériver Rtotal en Rₑ donne 1/(2πλLRₑ)−1/(2πhLRₑ²). Le minimum est en **Rcrit=λ/h**. Pour la sphère, le calcul analogue donne **Rcrit=2λ/h**. Puisque Φ=ΔT/Rtotal, ce minimum maximise la perte.

Le seuil n’est accessible que si Rcrit>Rᵢ. Si le rayon intérieur est déjà plus grand, toute épaisseur ajoutée réduit la perte. L’existence d’un rayon critique ne signifie donc pas que toute isolation augmente le transfert. Le laboratoire compare ces deux cas.

## 07. Le rayon choisi fait partie de la formule

Sup → Spé · Laboratoire `igloo`

R est ici le rayon **intérieur** de l’igloo et e son épaisseur ; le rayon extérieur vaut R+e. λ est la conductivité de neige ou de glace. P est la puissance thermique nette des occupants, en watts.

Le sol étant supposé isolé, la puissance sort à travers une hémisphère d’aire 2πr². Sa résistance est **Rth=[1/R−1/(R+e)]/(2πλ)**. Le bilan stationnaire donne Tint=Text+P Rth.

Une puissance métabolique nette n’est pas la puissance radiative totale d’un corps à 310 K. Dans le laboratoire elle est réglée directement : cela permet de comprendre le bilan sans confondre émission et échange net. Les résultats sont ceux d’un modèle conductif idéal ; une paroi intérieure au-dessus de 0°C impose d’étudier sa fonte.

## 08. Chercher une épaisseur et vérifier qu’elle existe

Spé · Laboratoire `igloo`

ΔT est l’écart intérieur visé au-dessus de l’extérieur. Pour un apport P fixé, on demande Rth=ΔT/P.

Résoudre donne **e=R²ΔT/[P/(2πλ)−RΔT]**. L’épaisseur est positive et finie seulement si le dénominateur est positif. À rayon intérieur fixé, la résistance tend vers 1/(2πλR) quand e augmente indéfiniment ; une résistance demandée plus grande est inaccessible dans ce modèle.

Cette recherche ne prouve pas la possibilité d’un véritable igloo solide à température de paroi positive. Le statut de validité signale la fusion : le bilan avec changement de phase et les échanges de surface doivent alors remplacer ce calcul conditionnel. Neige poreuse et glace dense ont par ailleurs des conductivités très différentes.

## 09. Deux modes, deux temps de refroidissement

Spé · Laboratoire `diffusion_1d`

L est la longueur, χ la diffusivité en m²/s et T₀ la température des deux extrémités. θ=T−T₀ est l’écart de température. Le temps réduit est χt/L².

Pour l’équation θt=χθxx et des bords θ=0, un mode sin(nπx/L) décroît avec **exp(−n²π²χt/L²)**. Le laboratoire prépare le premier mode seul ou une somme des rangs 1 et 3. Le rang 3 décroît neuf fois plus vite.

Le profil se lisse parce que les détails spatiaux fins disparaissent plus vite. Ce n’est pas une perte mystérieuse d’énergie : les extrémités thermostatées évacuent la chaleur. Un système isolé aurait d’autres conditions aux bords et un mode moyen conservé.

## 10. FTCS : une condition de stabilité qui a un sens physique

Spé · Laboratoire `diffusion_1d`

Δx est la maille spatiale, Δt le pas temporel et r=χΔt/Δx² le nombre de Fourier du calcul. Le schéma explicite donne θᵢ,suiv=(1−2r)θᵢ+rθᵢ₋₁+rθᵢ₊₁.

Pour **0≤r≤1/2**, les trois coefficients sont positifs et de somme 1. La nouvelle valeur reste entre les anciennes valeurs voisines : le calcul respecte un principe du maximum discret. Au-delà, cette garantie disparaît et des oscillations numériques peuvent croître.

Le laboratoire ajuste Δt pour rester sous le r demandé. La référence par modes est indépendante. Raffiner seulement le temps ne corrige pas toute l’erreur spatiale ; raffiner l’espace avec un même r impose aussi un pas temporel plus petit.

## 11. Une solution de similitude pour le choc thermique

Spé · Laboratoire `demi_espace`

x est la profondeur, t le temps, χ la diffusivité et T₀ la température initiale. La surface est imposée à Ts pour t>0. Le matériau est supposé semi-infini.

Pour u sans dimension, la fonction d’erreur est erf(u)=(2/√π)∫₀ᵘexp(−s²)ds, où s est la variable d’intégration. Sa complémentaire est erfc(u)=1−erf(u).

La variable x/(2√χt) regroupe position et temps. La solution est **T=T₀+(Ts−T₀)erfc[x/(2√χt)]**. Elle vaut Ts au bord et rejoint T₀ en profondeur.

La longueur √χt grandit comme la racine du temps. Pour comparer deux instants, il faut multiplier aussi les profondeurs par √(t₂/t₁). Une perturbation n’a pas de front net : ses petites valeurs s’étendent jusqu’à toute profondeur dans ce modèle diffusif.

## 12. Un flux initial singulier peut donner une énergie finie

Spé · Laboratoire `demi_espace`

ρc est la capacité volumique en J/(m³·K), et λ=χρc la conductivité. j(0,t) est le courant surfacique entrant dans le matériau.

Dériver le profil donne **j(0,t)=λ(Ts−T₀)/√(πχt)**. Ce flux diverge au départ du choc idéal, mais son intégrale temporelle converge : l’énergie reçue par aire vaut **2ρc(Ts−T₀)√(χt/π)**.

On retrouve cette énergie en intégrant ρc(T−T₀) dans l’espace. Ce double calcul vérifie le premier principe. En refroidissement, le flux et l’énergie reçue sont négatifs. La singularité au départ disparaîtrait avec une variation de surface étalée sur un temps fini.

## 13. Une excitation périodique dans une équation de diffusion

Spé · Laboratoire `onde_thermique`

z est la profondeur, χ la diffusivité, P la période et ω=2π/P la pulsation. T₀ est la température moyenne et A l’amplitude en K. Au temps t, la surface a température T₀+Acosωt.

θ(z) est l’amplitude complexe de l’écart T−T₀ ; i²=−1. La solution θ(z)eⁱʷᵗ satisfait χθ″=iωθ. La décroissance en profondeur impose θ=Aexp[−(1+i)z/δ], avec **δ=√(2χ/ω)**. La température réelle vaut T₀+Aexp(−z/δ)cos(ωt−z/δ).

Une même longueur δ contrôle la perte d’amplitude et le déphasage. À z=δ, l’amplitude vaut A/e et la phase retarde de 1 radian. Le dessin est une solution périodique établie ; il ne représente pas le premier jour après l’application du forçage.

## 14. Jour et année : une échelle de temps devient une profondeur

Spé · Laboratoire `onde_thermique`

Le retard de phase non ramené à une période est z/(δω). L’amplitude observable vaut Aexp(−z/δ).

Comme δ=√(χP/π), une période q fois plus longue pénètre √q fois plus profondément. Le cycle annuel et le cycle journalier ne chauffent donc pas les mêmes couches du sol.

Une « vitesse de phase » δω=√(2χω) dépend de la fréquence ; ce n’est pas une vitesse de transport sans perte. La diffusion conserve une forte atténuation. Quand une profondeur accumule un grand retard mais une amplitude presque nulle, la phase reste mathématiquement définie alors qu’une mesure devient délicate.

## 15. Le modèle uniforme est une hypothèse à contrôler

Sup → Spé · Laboratoire `refroidissement_biot`

La plaque a demi-épaisseur a, capacité volumique ρc et conductivité λ. S est l’aire d’une face ; le volume est V=2aS et l’aire d’échange Séchange=2S. Ses deux faces échangent avec un air à Tair par un coefficient h. Bi=ha/λ est le nombre de Biot.

Supposer la température uniforme donne le bilan ρc(2aS)T′=−2hS(T−Tair). La solution est **T−Tair=(Tinitial−Tair)exp[−ht/(ρca)]**. La longueur caractéristique V/Séchange vaut a, et non 2a.

La résistance interne devient faible devant celle de convection lorsque Bi est petit. Le repère Bi<0,1 est pratique ; le laboratoire montre l’écart réel et ne le transforme pas en une garantie universelle de précision.

## 16. Centre, surface et moyenne : trois températures différentes

Spé · Prolongement · Laboratoire `refroidissement_biot`

χ=λ/(ρc) est la diffusivité et Fo=χt/a² le temps réduit. La coordonnée du centre est x=0 et les faces sont en ±a.

Les modes exacts de la plaque convective sont cos(μx/a), où **μtanμ=Bi**. Leur coefficient initial est 4sinμ/(2μ+sin2μ), et ils décroissent comme exp(−μ²Fo). La moyenne d’un mode ajoute le facteur sinμ/μ.

Quand Bi est grand, la surface rejoint l’air avant le centre. Le modèle uniforme ne peut représenter ce gradient. La somme de 80 modes du laboratoire sert de référence à température initiale uniforme ; les profils réels se comparent pour t>0.

## 17. Une impulsion répartie dans une plaque mince

Spé · Laboratoire `diffusion_2d`

Q est l’énergie de la tache en joules, e l’épaisseur de plaque et ρce sa capacité par surface. χ est la diffusivité ; σ₀ est l’écart-type initial dans chaque direction. x,y sont les coordonnées du plan, T₀ la température de fond et σ la largeur par direction au temps t.

La tache gaussienne conserve sa forme : **σ²=σ₀²+2χt**. Son élévation de température est Qexp[−(x²+y²)/(2σ²)]/(2πρceσ²). La double intégrale de ρce(T−T₀) vaut toujours Q.

Le maximum diminue comme 1/σ² tandis que l’aire caractéristique augmente comme σ². Cette compensation exprime le premier principe. Une largeur initiale non nulle évite le pic infini d’une source ponctuelle au temps zéro.

## 18. Attention à la dimension d’une variance

Sup → Spé · Laboratoire `diffusion_2d`

Les variances suivant x et y valent chacune σ². Leur somme donne la moyenne radiale **⟨r²⟩=⟨x²+y²⟩=2σ²**.

La diffusion ajoute donc 2χt par direction et 4χt au carré de distance radiale en deux dimensions. Confondre ces deux mesures crée un facteur deux. Le même raisonnement donne 6χt en trois dimensions.

La carte est limitée à ±5σ dans les deux directions. Son énergie intégrée diffère très légèrement de Q à cause de la queue exclue et de la quadrature. Une fenêtre fixe trop petite pourrait donner l’impression erronée d’une énergie qui disparaît.

## 19. La position finale est une binomiale transformée

Sup → Spé · Laboratoire `marche_aleatoire`

ε est la longueur d’un saut et τ sa durée. À chaque pas indépendant, le saut vaut +ε avec probabilité p et −ε avec probabilité 1−p. K compte les sauts positifs sur N pas.

K suit la loi binomiale : P(K=k)=C(N,k)pᵏ(1−p)ᴺ⁻ᵏ. La position vaut **X=(2K−N)ε**. Sa moyenne est N(2p−1)ε et sa variance 4Np(1−p)ε².

Après N pas, seuls les indices de même parité que N sont accessibles. Leur espacement est 2ε. Une gaussienne est une densité ; multiplier par 2ε permet de la comparer à une probabilité par site. Le laboratoire conserve cette distinction.

## 20. Retrouver Fick et distinguer dérive de diffusion

Spé · Laboratoire `marche_aleatoire`

t=Nτ est le temps. La dérive moyenne a vitesse u=(2p−1)ε/τ. Identifier la variance centrée à 2Dt donne **D=2p(1−p)ε²/τ**.

Sans biais p=1/2, D=ε²/(2τ). La relation P(x,t+τ)=[P(x−ε,t)+P(x+ε,t)]/2 et des développements limités retrouvent ∂P/∂t=D∂²P/∂x².

Avec biais, le centre se déplace et la variance se calcule autour de ce centre. La limite diffusive centrée donne une équation d’advection–diffusion. Une moyenne sur 256 marches reste bruitée ; la binomiale et ses moments exacts fournissent les références indépendantes.

## 21. Stokes–Einstein fixe l’échelle de diffusion

Spé · Laboratoire `brownien_langevin`

a est le rayon d’une sphère, η la viscosité dynamique et T la température absolue. kB=1,380649×10⁻²³ J/K est la constante de Boltzmann ; v est une composante de vitesse. Le coefficient de frottement vaut α=6πηa. La masse m vient du rayon et de la masse volumique.

Le modèle de Langevin équilibre frottement et fluctuations thermiques. Avec l’équilibre de vitesse ⟨v²⟩=kBT/m par direction, il donne **D=kBT/α=kBT/(6πηa)** et le temps de relaxation de vitesse τᵥ=m/α.

Une particule plus grande ou un fluide plus visqueux diffuse moins vite. Le coefficient D est en m²/s ; τᵥ est en secondes. Le laboratoire distingue cette relaxation très rapide d’une observation brownienne sur des fractions de seconde.

## 22. Le carré du déplacement passe de t² à t

Spé · Prolongement · Laboratoire `brownien_langevin`

x(0)=0 et la vitesse initiale est déjà à l’équilibre thermique. La corrélation des vitesses vaut ⟨v(t)v(s)⟩=(kBT/m)e⁻|ᵗ⁻ˢ|/τᵥ.

Intégrer cette corrélation sur les deux temps donne **⟨x²(t)⟩=2D[t−τᵥ(1−e⁻ᵗ/τᵥ)]**. Pour t≪τᵥ, le développement limité retrouve (kBT/m)t², mouvement balistique. Pour t≫τᵥ, on retrouve 2Dt.

Les trajectoires utilisent les transitions gaussiennes exactes conjointes de vitesse et déplacement. Leur bruit est corrélé ; ce calcul reste valable si le pas dépasse τᵥ. Une vitesse initialement nulle donnerait une autre évolution aux temps courts. Les deux coordonnées du dessin ont chacune la variance 1D affichée.

## 23. Une source ponctuelle fixe une normalisation

Spé · Laboratoire `absorption_neutrons`

n(r) est la densité en m⁻³ ; D le coefficient diffusif, τ la durée de vie et Q le débit de source en s⁻¹. L=√Dτ est une longueur.

Hors de la source, le bilan permanent donne DΔn−n/τ=0. En symétrie sphérique, u=rn satisfait u″=u/L². La décroissance à l’infini impose n=Ae⁻ʳ/ᴸ/r.

Le courant est j=−Dn′. La limite du débit 4πr²j lorsque r→0 doit être Q ; elle impose **n=Qe⁻ʳ/ᴸ/(4πDr)**. La densité en 0 est singulière ; le laboratoire exclut ce point au lieu d’inventer une valeur finie.

## 24. Suivre le débit et compter l’absorption

Spé · Laboratoire `absorption_neutrons`

Φ(r)=4πr²j est le débit traversant une sphère de rayon r. La formule de densité donne **Φ=Q(1+r/L)e⁻ʳ/ᴸ**.

La différence Q−Φ est le nombre absorbé par seconde à l’intérieur. La somme source=absorption+débit sortant vérifie la conservation localement et globalement. La dérivée d’absorption par rayon vaut Qr e⁻ʳ/ᴸ/L².

L’intégrale de n sur tout le volume vaut Qτ : une injection Q avec durée de vie moyenne τ maintient ce nombre de particules. Le flux surfacique j, le débit Φ et la densité n ne portent pas les mêmes unités.

## 25. Deux ions doivent diffuser ensemble à courant nul

Spé · Prolongement · Laboratoire `diffusion_electrolyte`

D₊ et D₋ sont les diffusivités d’un cation et d’un anion monovalents. n est leur densité commune, E le champ et e la charge élémentaire positive. La température T est absolue ; kB est la constante de Boltzmann, en J/K. Γ₊ et Γ₋ sont les flux particulaires en m⁻²·s⁻¹ ; le signe prime indique une dérivée selon la position x.

Diffusion et migration donnent Γ₊=−D₊n′+D₊enE/(kBT), Γ₋=−D₋n′−D₋enE/(kBT). Le courant électrique nul impose Γ₊=Γ₋.

On obtient **E=(kBT/e)(D₊−D₋)n′/[(D₊+D₋)n]**. Les deux flux deviennent −Damb n′, avec **Damb=2D₊D₋/(D₊+D₋)**. Un champ compense donc la différence de diffusivité. Si les deux coefficients sont égaux, le champ disparaît.

## 26. Le signe du potentiel découle de E=−V′

Spé · Laboratoire `diffusion_electrolyte`

V est le potentiel et c la concentration en mol/m³. N_A=6,02214076×10²³ mol⁻¹ est la constante d’Avogadro ; n=N_Ac. Comme le quotient n′/n vaut c′/c, la concentration molaire convient pour calculer le champ.

Intégrer **V′=−E** donne Vdroite−Vgauche=(kBT/e)(D₋−D₊)ln(cDroite/cGauche)/(D₊+D₋). Le signe dépend des deux diffusivités et du sens du gradient ; il ne doit pas être deviné.

cG et cD sont les concentrations initiales à gauche et à droite ; t est le temps depuis leur mise en contact. Le profil est c=(cG+cD)/2+(cD−cG)erf[x/(2√Damb t)]/2. Le champ de jonction est local et généralement non uniforme. La quasi-neutralité concerne le volume ; les fines couches de charge aux interfaces ne sont pas résolues.

## 27. Une redistribution adiabatique conserve l’énergie

Sup → Spé · Laboratoire `entropie_diffusion`

N est le nombre de cellules. C est leur capacité thermique identique, G la conductance entre voisines et Tᵢ la température absolue de la cellule i. Les extrémités sont isolées.

Chaque bilan vaut C Tᵢ′=GΣvoisins(Tvoisin−Tᵢ). En sommant, tous les échanges internes s’annulent : **U=CΣTᵢ est constant**. À l’équilibre les températures deviennent égales à leur moyenne initiale.

La matrice de ce système est symétrique et négative ; son mode uniforme est conservé, ses autres modes décroissent. Le laboratoire calcule cette évolution exactement par diagonalisation. « Adiabatique » ne signifie donc pas que chaque cellule garde sa température : c’est l’ensemble qui ne reçoit pas de transfert externe.

## 28. La positivité apparaît à chaque interface

Spé · Laboratoire `entropie_diffusion`

Une interface entre Ti et Tj transmet Φ=G(Ti−Tj). Sa contribution à la variation d’entropie totale vaut Φ(1/Tj−1/Ti).

On obtient **G(Ti−Tj)²/(TiTj)≥0**, car les températures absolues et G sont positives. La somme de ces termes est la production irréversible ; elle s’annule seulement quand tous les voisins ont même température.

Avec des capacités constantes, le gain est ΔS=CΣln[Tᵢ(t)/Tᵢ(0)]. À l’équilibre, il atteint C[Nln(Tmoyenne)−ΣlnTᵢ(0)]≥0. L’énergie constante et l’entropie croissante ne sont pas contradictoires : elles décrivent deux bilans distincts.

## 29. Travail orienté et fonctions d’état : annoncer le système

Sup · Laboratoire `travail_chemins`

Le système est une quantité fixée de gaz dans un cylindre. On note Pext la pression extérieure, V le volume et W le travail **reçu par le gaz**. Pendant une variation infinitésimale de volume, le déplacement du piston donne δW=−Pext dV. Une détente augmente V et fournit du travail au milieu extérieur : W est négatif. Une compression reçoit du travail : W est positif.

P est la pression du gaz et T sa température absolue en K. R=8,314 J/(mol·K) est la constante molaire des gaz parfaits. Pour un chemin mécaniquement réversible, Pext=P à une différence infinitésimale près. Dans le diagramme P,V, W=−∫P dV est l’opposé de l’aire orientée sous la courbe. Une isochore a dV=0 et un travail nul ; une isotherme réversible d’une mole de gaz parfait vérifie P=RT/V.

U est l’énergie interne et Q la chaleur reçue, en J. cV et cP sont les capacités thermiques molaires à volume et pression constants, en J/(mol·K). Les indices 1 et 2 repèrent les états initial et final. L’expérience contient une mole.

Wiso=−RT ln(V₂/V₁) ; ΔU=cV(T₂−T₁) ; Q=ΔU−W.

U est une fonction d’état : deux chemins aux mêmes extrémités ont la même variation d’énergie interne. W et Q sont des transferts, non des fonctions d’état ; ils diffèrent en général. La convention reçue positive doit être conservée dans le premier principe ΔU=W+Q et dans toutes les branches.

## 30. Polytrope : une contrainte de chemin détermine aussi la température

Sup → Spé · Laboratoire `travail_chemins`

On appelle k l’exposant de la loi PVᵏ=constante, et r=V₂/V₁ le rapport des volumes. Pour une mole idéale, PV=RT. En combinant les deux relations, T₂=T₁r^(1−k). Comparer des chemins sans préciser leurs températures finales peut donc comparer des **états finaux différents**. Le laboratoire construit deux chemins supplémentaires aux mêmes extrémités : chauffage isochore puis isotherme à T₂ ; isotherme à T₁ puis chauffage isochore.

Pour k≠1 : W=−RT₁[r^(1−k)−1]/(1−k). Pour k=1 : W=−RT₁ ln r.

Les deux autres travaux valent respectivement −RT₂ ln r et −RT₁ ln r. Pour chacun, calculer ensuite Q=ΔU−W. Si γ=cP/cV et cP−cV=R, le cas k=γ donne Q=0 : la polytrope est l’adiabatique réversible. Le cas k=1 est l’isotherme ; les autres valeurs nécessitent un échange thermique.

La variation d’entropie est ΔS=cV ln(T₂/T₁)+R ln r. Elle est nulle pour k=γ. Un chemin réversible à température variable échange avec une suite de sources adaptées ; il ne faut pas conclure qu’un unique thermostat assure cette réversibilité. La pression utilisée dans W=−∫P dV suppose l’équilibre mécanique, contrairement à une détente rapide contre une pression extérieure constante.

## 31. Un produit effort–coordonnée doit avoir l’unité d’une énergie

Sup → Spé · Laboratoire `travaux_generalises`

Le travail n’est pas limité au produit pression–volume. Pour une extension x d’un fil soumis à une traction F, le travail reçu est F dx ; pour une interface d’aire A et de tension superficielle σ, il est σ dA. La tension superficielle est en N/m et l’aire en m² : leur produit est en N·m=J. Une seule interface et un film à deux faces ne possèdent pas la même aire totale.

Pour un condensateur, noter q la charge de l’armature positive, u la tension et C la capacité. Une charge dq transférée sous la tension u apporte δW=u dq. Pour une bobine idéale, noter λ le flux lié, L l’inductance et I l’intensité. La loi électrique u=dλ/dt donne δW=uI dt=I dλ.

δWfil=F dx ; δWsurface=σ dA ; δWélectrique=u dq ; δWbobine=I dλ.

Ces coordonnées et leurs efforts conjugués sont différents : ne pas remplacer un flux lié par une induction B sans préciser le volume, la géométrie et le nombre de spires. Pour un milieu magnétique matériel, des conventions supplémentaires sont nécessaires. Le modèle de bobine utilisé ici évite cette ambiguïté et permet un bilan d’énergie direct.

## 32. Énergies stockées et restitution : intégrer la loi d’effort

Sup · Laboratoire `travaux_generalises`

Un fil idéal de raideur k suit F=kx. Le condensateur suit u=q/C et la bobine I=λ/L. Intégrer chaque effort depuis la coordonnée nulle fournit les énergies stockées :

Efil=kx²/2 ; Econdensateur=q²/(2C)=Cu²/2 ; Ebobine=λ²/(2L)=LI²/2.

Pour la surface à tension constante, Esurface=σA à une origine près. Entre deux états, W est la différence des énergies stockées. Si la coordonnée finale est plus petite que l’initiale, l’énergie est restituée et W<0. Ce changement de signe ne correspond pas à une énergie stockée négative : c’est sa **variation** qui est négative.

L’expérience utilise un curseur s sans dimension et annonce sa conversion selon le dispositif. Par exemple, une bobine a λ=5s mWb ; un fil a x=0,02s m. Revenir aux unités SI avant l’intégration empêche les erreurs de facteurs 10³ ou 10⁶. Les dispositifs sont supposés sans pertes : l’énergie mécanique ou électrique reçue n’est pas dissipée en chaleur.

## 33. Pourquoi F décroît sous température et volume imposés

Spé · Laboratoire `potentiel_helmholtz`

On note U l’énergie interne, S l’entropie et T₀ la température d’un thermostat. Considérer un système fermé dans une enceinte extérieure rigide, sans travail extérieur autre que celui de pression ; ce dernier est nul puisque le volume extérieur est fixe. La température est imposée égale à T₀. Le premier principe donne ΔU=Q et le second ΔS=Q/T₀+Scréée.

F=U−T₀S ; ΔF=−T₀Scréée≤0.

Une variation interne peut donc abaisser F même si le volume total est fixe : deux compartiments échangent du volume derrière une cloison interne mobile. **La contrainte porte sur le volume extérieur**, pas sur chacun des volumes internes. Si un ressort agit sur la cloison, l’inclure dans le système pour que son énergie figure dans F.

À l’équilibre, la première variation admissible de F est nulle. Pour démontrer la stabilité, il faut examiner la dérivée seconde ou un minimum global. Une courbe monotone sans variable interne ne suffit pas à illustrer un équilibre. Pour des contraintes T,V et quantités de matière fixées, le minimum de Helmholtz est discuté dans les [cours de thermodynamique du MIT](https://ocw.mit.edu/courses/3-00-thermodynamics-of-materials-fall-2002/).

## 34. Cloison et ressort : transformer le minimum en bilan de forces

Spé · Prolongement · Laboratoire `potentiel_helmholtz`

Une enceinte de volume total Vtot=20 L et de longueur L=0,20 m contient une mole. Noter nG et nD les quantités à gauche et à droite, y=VG/Vtot, ys la position réduite de repos et ks la raideur du ressort. La cloison a pour abscisse Ly ; la section est A=Vtot/L. Pour un gaz parfait à T fixe, la dépendance de F en V est −nRT lnV.

F(y)=−RT[nG ln y+nD ln(1−y)]+ksL²(y−ys)²/2+constante.

Dériver puis diviser par −L : −F′/L=(PG−PD)A−ksL(y−ys), avec PG=nGRT/(yVtot) et PD=nDRT/[(1−y)Vtot]. Le minimum traduit donc le bilan des forces. Sans ressort, PG=PD et yéq=nG/(nG+nD).

La courbure est F″=RT[nG/y²+nD/(1−y)²]+ksL²>0. F tend vers +∞ aux deux limites y→0 et y→1 : il existe un unique minimum intérieur stable. Une dissipation interne peut conduire à ce minimum, mais la thermodynamique ne prédit ni la vitesse de relaxation ni d’éventuelles oscillations. Le chemin exponentiel du laboratoire illustre une décroissance et reste annoncé comme un chemin choisi.

## 35. G et le sens d’une réaction sous T,P fixées

Spé · Laboratoire `potentiel_gibbs`

On note H=U+PV l’enthalpie, G=H−TS l’enthalpie libre et μi le potentiel chimique de l’espèce i. Pour une évolution monotherme et monobare, sans travail utile extérieur autre que la pression, le premier et le second principes donnent ΔG≤0. Le minimum doit être recherché parmi les compositions permises par la conservation des éléments.

Le modèle est une réaction A⇌B, avec une mole totale et la fraction x de B. Les deux espèces ont des activités idéales aB=x et aA=1−x ; elles ont la même variation du nombre total de moles. Noter ξ l’avancement en mol et ΔrG° la différence μB°−μA°. R est la constante molaire des gaz parfaits. La pente de G par rapport à ξ est l’énergie libre de réaction.

ΔrG=ΔrG°+RT ln[x/(1−x)] ; dG=ΔrG dξ.

Si ΔrG<0, la réaction directe diminue G ; si ΔrG>0, le sens inverse le diminue. À l’équilibre intérieur, ΔrG=0 et x/(1−x)=K, avec K=exp(−ΔrG°/RT). Ce critère concerne le sens et l’état final, pas la vitesse d’une réaction ni la hauteur d’une barrière d’activation.

## 36. Entropie de mélange et minimum unique

Spé · Laboratoire `potentiel_gibbs`

Noter ΔrH° l’enthalpie standard et ΔrS° l’entropie standard de la conversion A→B. Dans le modèle, elles sont constantes et ΔrG°=ΔrH°−TΔrS°. L’énergie libre d’une mole, à une constante indépendante de x près, s’écrit :

G(x)=xΔrG°+RT[(1−x)ln(1−x)+xlnx].

Le premier terme favorise l’espèce de plus faible potentiel standard. Le second est −T fois l’entropie de mélange et favorise une coexistence. La courbure G″=RT[1/x+1/(1−x)] est positive sur ]0,1[ ; la pente passe de −∞ à +∞ aux deux bords. Le minimum intérieur est donc unique.

Si ΔrH°<0 et ΔrS°<0, la réaction favorise B aux basses températures mais peut favoriser A aux températures élevées. La température où K=1 est ΔrH°/ΔrS°, si elle est positive. Le graphique G explique cette transition sans une règle de signe mémorisée hors contexte. L’énergie standard doit être convertie en J/mol avant de la comparer à RT.

## 37. Un calorimètre isolé impose un bilan, pas des chaleurs indépendantes

Sup · Laboratoire `calorimetrie_entropie`

Le système est l’ensemble du calorimètre et de son contenu, isolé de l’extérieur. Noter m₁,m₂ les masses, c₁,c₂ les capacités massiques, Ccal la capacité totale du calorimètre et T₁,T₂ les températures initiales. Tf est la température finale commune. Le calorimètre est initialement à T₁. Sans changement de phase, toutes les capacités sont constantes.

(m₁c₁+Ccal)(Tf−T₁)+m₂c₂(Tf−T₂)=0.

La température finale est une moyenne pondérée par les capacités, non par les seules masses. La chaleur gagnée par le corps froid est perdue par le corps chaud et le calorimètre ; leur somme est nulle. Les capacités totales sont en J/K, les capacités massiques en J/(kg·K) : annoncer le type évite de multiplier deux fois par une masse.

La variation d’entropie d’un corps à capacité C constante est C ln(Tf/Tinitiale). Additionner les contributions, avec les températures en kelvins. Comme le système est isolé, ΔStotal=Scréée≥0. Une baisse de l’entropie du corps chaud n’est pas une violation du second principe : il porte ici sur la somme de tous les corps.

## 38. Une chaleur latente impose de déterminer le régime de phase

Sup → Spé · Laboratoire `calorimetrie_entropie`

À pression atmosphérique, prendre Tm=273,15 K, cglace=2100 J/(kg·K), ceau=4180 J/(kg·K) et L=334 kJ/kg, chaleur latente massique de fusion. Choisir la glace à Tm comme référence d’enthalpie massique. Alors hglace=cglace(T−Tm) et heau=L+ceau(T−Tm). Le système isolé conserve l’enthalpie totale à l’approximation des phases condensées.

Noter E l’enthalpie initiale relative et M=m₁+m₂ la masse totale. Si E<0, tout finit sous forme de glace avec Tf<Tm. Si 0≤E≤ML, les deux phases coexistent à Tm et la masse liquide vaut E/L. Si E>ML, tout est liquide et l’excédent chauffe l’eau. Ces trois régimes permettent de traiter aussi la **congélation d’eau initialement chaude**.

sglace et seau sont les entropies massiques, en J/(kg·K), avec la glace à Tm comme référence.

sglace=cglace ln(T/Tm) ; seau=L/Tm+ceau ln(T/Tm).

La fusion reçoit L par kilogramme et augmente l’entropie de L/Tm. Les étapes de chauffage à température variable donnent des logarithmes. Calculer d’abord la phase et les masses finales, puis l’entropie : utiliser uniquement mcΔT à travers la fusion donnerait un bilan erroné. Dans un TP, mesurer la masse perdue par vaporisation ou la masse fondue permet de déterminer une chaleur latente, à condition de compter les pertes et la capacité de l’appareil.

## 39. Détente dans le vide : conserver U dans un système fermé

Sup → Spé · Laboratoire `detentes_joule`

Une enceinte rigide et isolée contient initialement du gaz d’un côté et le vide de l’autre. Retirer la séparation ne produit pas de travail extérieur : aucune pression extérieure n’agit sur un piston déplacé. Noter U l’énergie interne totale, Q la chaleur reçue et W le travail reçu ; Q=W=0 donne ΔU=0.

Pour un gaz parfait, l’énergie molaire u=cVT ne dépend que de T. La température finale égale donc l’initiale. Mais le volume augmente et l’entropie créée vaut R ln(vf/vi)>0 par mole. **Adiabatique n’implique pas isentropique** : cette détente est irréversible.

Le modèle de van der Waals utilise v, volume molaire, a>0, paramètre d’attraction en Pa·m⁶/mol², et b, covolume en m³/mol. Sa pression est P=RT/(v−b)−a/v² et u=cVT−a/v. Conserver u donne :

Tf−Ti=(a/cV)(1/vf−1/vi).

Pour vf>vi, cette différence est négative. L’énergie potentielle d’attraction augmente quand les molécules s’éloignent, au détriment de la part thermique. La courbe du laboratoire relie une famille d’états finaux ; elle n’affirme pas que la détente libre suit des états intermédiaires d’équilibre.

## 40. Joule–Thomson : conserver H et déterminer le signe de la température

Spé · Laboratoire `detentes_joule`

Un étranglement est un écoulement permanent à travers une vanne ou un milieu poreux. Le système ouvert est adiabatique, sans travail d’arbre ; les variations des énergies cinétique et potentielle sont négligées. Noter h=u+Pv l’enthalpie molaire : les travaux de poussée à l’entrée et à la sortie y sont inclus. Le bilan impose hsortie=hentrée, contrairement à la conservation de U dans le vide.

Pour van der Waals à cV constant, h=[cV+Rv/(v−b)]T−2a/v. À h initial fixé, la température s’obtient exactement par T(v)=[hi+2a/v]/[cV+Rv/(v−b)]. Définir μJT=(∂T/∂P)h et cP=(∂h/∂T)P. La relation dh=cP dT+[v−T(∂v/∂T)P]dP donne :

μJT=[T(∂v/∂T)P−v]/cP ; Tinv(v)=2a(1−b/v)²/(Rb).

Une chute de pression a dP<0 : μJT>0 produit un refroidissement, μJT<0 un réchauffement. La température d’inversion dépend du volume ou de la pression ; 2a/(Rb) est seulement sa limite diluée supérieure. Le domaine stable vérifie −(∂P/∂v)T>0. La notion et le TP sont présentés par l’[université de Mayence](https://interaktiv.chemie.uni-mainz.de/vpcgp/jt-man.en.html). Le laboratoire reste sur une branche gazeuse stable, sans liquéfaction.

## 41. Deux bilans suffisent à construire les bornes de Carnot

Sup · Laboratoire `carnot_ditherme`

Noter Tc la température absolue de la source chaude, Tf celle de la source froide, avec Tc>Tf>0. Qc et Qf sont les chaleurs **reçues par la machine** depuis ces sources ; W est son travail reçu. Après un cycle, l’énergie interne et l’entropie de la machine ont leur valeur initiale.

W+Qc+Qf=0 ; Qc/Tc+Qf/Tf+Scréée=0, avec Scréée≥0.

Pour un moteur, Qc>0, Qf<0 et W<0. Le rendement η=−W/Qc est borné par 1−Tf/Tc. L’égalité exige Scréée=0. Elle ne dépend pas de la nature du fluide : c’est une borne issue du second principe. Le cycle de Carnot d’un gaz parfait la réalise par deux isothermes et deux adiabatiques réversibles.

Les températures doivent être en kelvins : un rapport de degrés Celsius n’a pas de sens thermodynamique. Un rendement maximal ne fixe pas la puissance d’une machine : les bilans du laboratoire sont par cycle et ne fournissent pas une durée.

## 42. Réfrigérateur et PAC : la même machine, deux quantités utiles

Sup → Spé · Laboratoire `carnot_ditherme`

Une machine frigorifique reçoit un travail W>0 et une chaleur Qf>0 depuis la source froide ; elle rejette vers le chaud, donc Qc<0. Le coefficient de performance frigorifique est COPf=Qf/W. Pour une pompe à chaleur, la chaleur utile est −Qc et COPc=−Qc/W.

COPf≤Tf/(Tc−Tf) ; COPc≤Tc/(Tc−Tf) ; COPc=1+COPf.

Un COP supérieur à 1 ne signifie pas créer de l’énergie : la chaleur utile comprend une chaleur prélevée dans une autre source, plus le travail reçu. Les deux COP ne peuvent pas être choisis indépendamment. L’expérience multiplie le COP frigorifique idéal par un facteur φ entre 0,3 et 1 ; le COP de PAC est ensuite déduit du bilan. Le moteur utilise η=φηCarnot.

Les diagrammes P,V et T,S sont ceux d’une **référence réversible**. Lorsque φ<1, les échanges et l’entropie créée décrivent un modèle global irréversible ; on ne prétend pas connaître sa trajectoire réelle. Une aire ou un rectangle de référence n’est pas un bilan d’irréversibilité d’une machine dont le cycle n’a pas été spécifié.

## 43. Construire quatre branches avant de calculer un rendement

Sup → Spé · Laboratoire `cycles_moteurs`

Le gaz idéal du cycle contient une mole. Noter γ=cP/cV, r le taux de compression et z le paramètre de chauffage. Les capacités constantes valent cV=R/(γ−1) et cP=γR/(γ−1). Le cycle Otto comporte deux adiabatiques réversibles et deux isochores ; Diesel remplace le chauffage isochore par un chauffage isobare ; Brayton comporte deux adiabatiques et deux isobares.

Pour Otto et Diesel, r=V₁/V₂>1 ; pour Brayton, r=P₂/P₁>1. Dans Otto/Brayton, z=T₃/T₂ ; dans Diesel, z=V₃/V₂=T₃/T₂ pendant le chauffage isobare. Pour Diesel, z<r laisse ensuite une détente jusqu’au volume initial.

Adiabatique réversible : TV^(γ−1)=constante. Isochore : W=0, Q=cVΔT. Isobare : W=−RΔT, Q=cPΔT.

Le tableau donne des travaux reçus par le **gaz fermé** sur chaque branche. Pour une turbine ou un compresseur ouvert réel, le travail d’arbre se calcule avec l’enthalpie ; le travail net de cycle Brayton correspond au bilan idéal de la turbine et du compresseur, mais les travaux de branches fermées et ouverts ne se confondent pas. Les contraintes des cycles sont présentées par [NASA Glenn](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/engine-thermodynamic-analysis/).

## 44. Rendements, sources et régénération : les hypothèses font le résultat

Spé · Laboratoire `cycles_moteurs`

Le travail total reçu W et les chaleurs externes Qchaud>0,Qfroid<0 vérifient W+Qchaud+Qfroid=0. Le rendement est η=−W/Qchaud. Les états du cycle donnent :

ηOtto=1−r^(1−γ) ; ηDiesel=1−[(z^γ−1)/(γ(z−1))]r^(1−γ) ; ηBrayton=1−r^((1−γ)/γ).

Stirling combine une compression isotherme froide, un chauffage isochore, une détente isotherme chaude et un refroidissement isochore. Noter Tf,Tc ses températures et ε l’efficacité du régénérateur. Ce dernier stocke puis restitue une chaleur interne entre les deux isochores.

Qchaud=RTc ln r+(1−ε)cV(Tc−Tf) ; −W=R(Tc−Tf)ln r.

À ε=1, le rendement devient 1−Tf/Tc ; sans récupération, le chauffage externe augmente et le rendement baisse, alors que l’aire P,V reste la même. Pour Otto, Diesel et Brayton, les échanges à température variable n’équivalent pas à deux isothermes. Si les seules sources sont à Tmax et Tmin, ils créent de l’entropie même si les compressions sont isentropiques. Un rendement croissant avec r ne suffit pas à optimiser un moteur réel : températures maximales, contraintes mécaniques et pertes sont ici hors modèle.

## 45. Système ouvert : utiliser l’enthalpie et le travail d’arbre

Spé · Laboratoire `compresseur_etages`

Un compresseur traite un écoulement permanent. Noter h l’enthalpie massique, w le travail d’arbre reçu par kilogramme et q la chaleur reçue par kilogramme. u est l’énergie interne massique, en J/kg ; v est le volume massique, en m³/kg ; P est la pression. Les travaux de poussée à l’entrée et à la sortie sont inclus dans h=u+Pv ; ils ne doivent pas être ajoutés une deuxième fois.

rair est la constante massique du gaz. cP est la capacité thermique massique à pression constante, en J/(kg·K). Tentrée et Tsortie sont les températures absolues avant et après l’étage.

hsortie−hentrée=w+q ; adiabatique : w=cP(Tsortie−Tentrée).

Pour l’air parfait du modèle, rair=287 J/(kg·K), γ=1,4 et cP=1004,5 J/(kg·K). Noter rp=Psortie/Pentrée. Une compression isentropique donne Ts,sortie=Tentrée rp^((γ−1)/γ). Le rendement isentropique ηs est le rapport du travail idéal au travail réel : ηs=(Ts,sortie−Tentrée)/(Tsortie−Tentrée).

Un refroidisseur isobare n’a pas de travail d’arbre ; q=cP(Tsortie−Tentrée)<0. Il diminue le volume massique et réduit le travail de l’étage suivant. Sans refroidissement intermédiaire, découper une compression réversible en plusieurs étages ne change pas son travail ; c’est le refroidissement, non le nombre de machines à lui seul, qui apporte le gain.

## 46. Minimum : les pressions forment une progression géométrique

Spé · Laboratoire `compresseur_etages`

Noter N le nombre d’étages, Rtot le rapport total de pressions, xi le rapport de pression de l’étage i et a=(γ−1)/γ. Les refroidisseurs ramènent le gaz à T₁ ; tous les étages ont le même ηs. Leur travail total vaut cPT₁Σ(xiᵃ−1)/ηs, avec ∏xi=Rtot.

Poser ui=lnxi : la contrainte devient Σui=lnRtot. La fonction exp(au) est strictement convexe. Sa somme est minimale quand tous les ui sont égaux. Donc xi=Rtot^(1/N), et les pressions intermédiaires valent Pentrée Rtot^(i/N).

wmin=NcPT₁[Rtot^(a/N)−1]/ηs ; pour N=2, Pintermédiaire=√(PentréePsortie).

Quand N→∞, le modèle approche rairT₁lnRtot/ηs ; la borne réversible isotherme est rairT₁lnRtot et n’est atteinte que si ηs=1. Le refroidissement à un thermostat fixe T₁ crée lui-même de l’entropie, car le gaz est initialement plus chaud. Les hypothèses « refroidissement complet » et « refroidissement réversible » sont donc distinctes.

## 47. Un corps fini : refroidir n’est pas tout convertir en travail

Spé · Laboratoire `exergie_corps`

Un corps a une capacité thermique totale constante C et une température initiale Ti. L’environnement est un thermostat à T₀. Le système considéré inclut le corps et une machine cyclique, qui finit dans son état initial ; le corps finit à T₀. On note W le travail reçu par cet ensemble et Q sa chaleur reçue depuis l’environnement.

La variation d’énergie du corps est ΔU=C(T₀−Ti), et celle de son entropie ΔS=C ln(T₀/Ti). Le second principe donne ΔS=Q/T₀+Scréée, donc Q≤T₀ΔS. Avec ΔU=W+Q, le travail fourni −W est maximal pour Scréée=0.

Wmax,fourni=C[(Ti−T₀)−T₀ln(Ti/T₀)].

Cette quantité est l’exergie thermique du corps relative à l’environnement, sous les hypothèses du modèle. Pour Ti>T₀, elle est inférieure à C(Ti−T₀), l’énergie libérée par refroidissement : une partie doit rejoindre l’environnement. Pour Ti<T₀, une machine peut prélever de la chaleur dans l’environnement chaud et en rejeter dans le corps froid tout en fournissant du travail.

## 48. Entropie créée et exergie détruite

Spé · Prolongement · Laboratoire `exergie_corps`

Noter B l’exergie initiale calculée ci-dessus et φ la fraction récupérée sous forme de travail. L’ensemble corps+machine fournit φB ; son travail reçu est donc −φB. Le bilan d’énergie impose Q=ΔU+φB, et le second principe donne :

Scréée=(1−φ)B/T₀ ; Bdétruite=T₀Scréée ; travail fourni+Bdétruite=B.

Le terme T₀Scréée est l’exergie détruite ; l’énergie totale, elle, reste conservée. Pour un contact direct, φ=0 : aucun travail n’est récupéré et toute l’exergie est détruite. Pour une succession réversible de machines de Carnot, φ=1 et la création d’entropie est nulle.

Poser z=(Ti−T₀)/T₀ : B=CT₀[z−ln(1+z)]. Cette fonction est positive pour Ti≠T₀ et nulle à l’équilibre. Pour une faible différence de température δT, le développement limité donne B≈CδT²/(2T₀). L’énergie thermique varie au premier ordre, mais le travail disponible seulement au second : des écarts de température faibles fournissent peu d’exergie même si le corps a une grande capacité.

## 49. TP p. 467 : comparer des émissivités, pas des températures

Sup → Spé · Laboratoire `cube_leslie`

T est la température absolue d’une face, Tₐ celle de la pièce, A son aire et ε son émissivité infrarouge, comprise entre 0 et 1. σ=5,670374419×10⁻⁸ W·m⁻²·K⁻⁴ est la constante de Stefan–Boltzmann. Dans une grande enceinte noire, la puissance radiative nette sortante est :

Pᵣ=εσA(T⁴−Tₐ⁴).

Le cube de Leslie présente des surfaces différentes à une même température. À aire, distance et orientation identiques, leurs signaux sont proportionnels à ε. Une laque blanche dans le visible peut être très émissive dans l’infrarouge. Les quatre valeurs utilisées ici sont illustratives.

U est la tension de la thermopile, η la fraction du rayonnement net qu’elle reçoit et G sa sensibilité en volts par watt. Alors U=GηPᵣ. Maintenir les mêmes η et G permet de comparer les surfaces. La thermopile ne mesure pas directement la puissance convective.

## 50. Relier le rayonnement à un bilan et à une équation différentielle

Sup → Spé · Laboratoire `cube_leslie`

a est le côté du cube, h le coefficient de convection et Cₜₕ sa capacité thermique totale en J/K. Les six faces ont une aire a². Noter εᵢ l’émissivité de la face d’indice i et Pₑ la puissance fournie par le chauffage.

Cₜₕ dT/dt=Pₑ−σa²(∑ᵢ εᵢ)(T⁴−Tₐ⁴)−6ha²(T−Tₐ).

À l’équilibre, le membre de gauche s’annule. Après coupure du chauffage, Pₑ=0 : le cube tend vers Tₐ. Si T est inférieur à Tₐ, les échanges nets changent de signe et réchauffent le cube.

Pour un petit écart δT=T−Tₐ, T⁴−Tₐ⁴≈4Tₐ³δT. La conductance totale est alors H=a²[4σTₐ³∑ᵢεᵢ+6h] en W/K, et le temps caractéristique vaut Cₜₕ/H. Le calcul du laboratoire conserve toutefois la loi T⁴.

## 51. Thermocouple : intégrer un coefficient local

Sup → Spé · Laboratoire `seebeck`

Th est la température à mesurer, Tf celle de la jonction froide et V la tension à circuit ouvert. S(T) est le coefficient Seebeck effectif du couple de matériaux, en V/K. Le signe de S correspond au sens de branchement choisi.

V=∫ de Tf à Th S(T)dT.

Pour une petite différence de température et un coefficient presque constant, V≈S(Tf)(Th−Tf). Pour une calibration plus large, choisir une température de référence Tᵣ et écrire S(T)=S₀+s₁(T−Tᵣ), où S₀ est en V/K et s₁ en V/K².

V=S₀(Th−Tf)+s₁[(Th−Tᵣ)²−(Tf−Tᵣ)²]/2.

La dérivée de la calibration par rapport à Th vaut S(Th). Si S garde un signe strict, cette calibration est monotone et son inversion détermine une seule température.

## 52. Jonction froide : une mesure à compenser

Spé · Laboratoire `seebeck`

Un voltmètre ne mesure pas Th seule : sa tension dépend aussi de Tf. Définir E(T)=∫ de Tᵣ à T S(u)du, où u est la variable d’intégration. La mesure vérifie V=E(Th)−E(Tf).

E(Th)=V+E(Tf).

La compensation consiste donc à mesurer Tf et à ajouter sa contribution E(Tf) avant d’inverser E. Ce n’est pas nécessairement l’ajout d’une constante à la température : une calibration non linéaire doit être inversée.

δTf désigne une petite erreur de référence et δTh l’erreur obtenue. À tension fixée, S(Th)δTh≈S(Tf)δTf. Un coefficient variable modifie la sensibilité au biais. Le laboratoire compare cette inversion à l’approximation avec S₀ constant.

## 53. Compter séparément transport, Joule et conduction

Sup → Spé · Laboratoire `peltier`

Tc et Th sont les températures froide et chaude en K ; ΔT=Th−Tc. I≥0 est le courant orienté pour refroidir, α le coefficient thermoélectrique du module en V/K, R sa résistance en Ω et K sa conductance thermique en W/K. Qc est la puissance thermique extraite du côté froid ; Qh celle rejetée au côté chaud. Elles sont en W.

Qc=αTcI−RI²/2−KΔT ; Qh=αThI+RI²/2−KΔT.

Le transport Peltier est proportionnel au courant. Joule produit une puissance RI², répartie ici également entre les faces. La conduction fait revenir la chaleur du chaud vers le froid et pénalise Qc.

P est la puissance électrique consommée, en W : P=αΔTI+RI². Les formules donnent exactement Qh=Qc+P. À températures fixées, Qc est maximale pour I=αTc/R ; augmenter le courant au-delà renforce surtout Joule.

## 54. Premier et second principes : discuter la performance

Spé · Laboratoire `peltier`

Qc est la puissance thermique extraite, Qh la puissance thermique rejetée et P la puissance électrique consommée, toutes en W. En régime de refroidissement, Qc>0 et P>0. Le coefficient de performance est COP=Qc/P. Un Qc négatif ne correspond pas à un COP de réfrigérateur : le côté froid est alors réchauffé.

La production d’entropie par unité de temps est Σ=Qh/Th−Qc/Tc. Le modèle constant donne :

Σ=(RI²/2)(1/Th+1/Tc)+KΔT(1/Tc−1/Th)≥0.

Pour ΔT>0, combiner Σ≥0 et Qh=Qc+P donne COP≤Tc/ΔT, la limite de Carnot. Le premier principe vérifie les puissances ; le second borne la performance.

Si le côté chaud est maintenu à Th et si une charge thermique de puissance Qcharge, en W, arrive au côté froid, l’équilibre impose Qc=Qcharge. Il donne Tc=(Qcharge+RI²/2+KTh)/(αI+K). Cette solution doit être inférieure à Th pour décrire un refroidissement.

## 55. P24 : les équations de l’onde et de la chaleur se couplent

Spé · Prolongement · Laboratoire `thermoacoustique`

P₀, T₀ et ρ₀ sont la pression, la température et la masse volumique au repos d’un gaz parfait. γ=cₚ/cᵥ est le rapport des capacités thermiques massiques ; c²=γP₀/ρ₀ définit la célérité adiabatique. λ est la conductivité thermique. La position est x et le temps t ; p(x,t) est la surpression et τ(x,t) la variation de température.

λ ∂²τ/∂x²=ρ₀cₚ ∂τ/∂t−∂p/∂t ; ρ₀cₚ=γP₀/[(γ−1)T₀].

La conservation de la masse, la dynamique sans viscosité et la loi du gaz parfait donnent l’autre équation : ∂²p/∂x²=(γ/c²)∂²[p−(P₀/T₀)τ]/∂t². Une compression modifie la température ; sa diffusion agit en retour sur la pression.

i est le nombre complexe vérifiant i²=−1 ; f est la fréquence en Hz, ω=2πf la pulsation et k le nombre d’onde. Chercher p=p₀exp(iωt−ikx) et τ=τ₀exp(iωt−ikx), où p₀ et τ₀ sont les amplitudes complexes. Le système homogène admet une solution non nulle lorsque son déterminant est nul.

λq²+[iωρ₀cₚ−λγω²/c²]q−iωρ₀cₚω²/c²=0, avec q=k².

## 56. Choisir la branche physique et lire les nombres complexes

Spé · Au-delà · Laboratoire `thermoacoustique`

La branche acoustique est celle qui tend vers k=ω/c lorsque λ tend vers 0. L’autre solution est une branche thermique diffusive. Elles ne représentent pas deux sons de même nature.

Écrire k=kᵣ+ikᵢ, avec kᵣ>0. La convention exp(iωt−ikx) donne une amplitude proportionnelle à exp(kᵢx). Une onde atténuée vers x>0 impose kᵢ≤0. La vitesse de phase vaut ω/kᵣ et la longueur d’onde 2π/kᵣ.

τ₀/p₀=iω/(iωρ₀cₚ+λk²).

Le module de ce rapport est en K/Pa. Sa phase décrit le déphasage de température par rapport à la pression ; avec exp(iωt), une phase positive est une avance. Sans conduction, τ₀/p₀=(γ−1)T₀/(γP₀). Pour une conduction très forte, la célérité acoustique tend vers c/√γ, la valeur isotherme.

Cette expérience isole la conduction dans le volume du gaz. La viscosité, les échanges aux parois et les éléments d’un moteur thermoacoustique demanderaient d’autres équations.

## 57. Une énergie commune impose la réciprocité

Spé · Laboratoire `piezo_resonateur`

x est le déplacement en m, q la charge en C, k>0 la raideur en N/m, C>0 la capacité en F et θ le couplage en C/m, équivalent à N/V. Le modèle prend pour énergie interne :

U(x,q)=kx²/2+(q−θx)²/(2C).

V=∂U/∂q est la tension et F=∂U/∂x la force extérieure conjuguée au déplacement. Calculer d’abord ces dérivées à x ou q fixé, puis éliminer q.

q=CV+θx ; F=kx−θV.

La charge produite par une déformation et la force produite par une tension font intervenir le même θ. Les deux dérivées croisées de U sont égales : c’est la réciprocité. U est positive pour tout (x,q) non nul ; le couplage ne détruit pas la stabilité de ce modèle.

À tension imposée, employer U−Vq puis éliminer q donne kx²/2−θVx−CV²/2. La raideur vaut alors k. À charge q=0 imposée, elle vaut k+θ²/C : la condition électrique change la réponse mécanique.

## 58. Relier la vibration à une admittance électrique

Spé · Laboratoire `piezo_resonateur`

m est la masse, r>0 le coefficient de frottement en N·s/m et V₀ l’amplitude de la tension harmonique. Avec i²=−1 et ω la pulsation, écrire V(t)=Re[V₀exp(iωt)]. La dynamique est m x″+r x′+kx=θV. x₀ est l’amplitude complexe du déplacement : x(t)=Re[x₀exp(iωt)].

x₀=θV₀/(k−mω²+iωr).

La charge vaut q₀=CV₀+θx₀, le courant a pour amplitude I₀=iωq₀ et l’admittance est Y=I₀/V₀. Ainsi :

Y=iωC+iωθ²/(k−mω²+iωr).

Sans pertes, la résonance vérifie ωᵣ²=k/m. L’antirésonance, où les courants capacitif et mécanique se compensent, vérifie ωₐ²=(k+θ²/C)/m. Les fréquences valent fᵣ=ωᵣ/(2π) et fₐ=ωₐ/(2π).

Le curseur ζ est un amortissement relatif : r=2ζ√(km). Avec ζ>0, les pics sont finis. Les repères sans pertes ne sont pas les extrema exacts de la réponse amortie. La puissance moyenne électrique V₀²Re(Y)/2 égale la dissipation rω²|x₀|²/2.

## 59. Exercice 1 p. 469 : intégrer la courbe de saturation

Spé · Laboratoire `brouillard`

T est la température absolue, Pₛₐₜ(T) la pression de saturation et L(T) la chaleur latente massique en J/kg. R=461,5 J·kg⁻¹·K⁻¹ est la constante massique de la vapeur d’eau. Elle doit être associée à une chaleur latente massique, et non molaire.

En assimilant la vapeur à un gaz parfait et en négligeant le volume du liquide, la relation de Clapeyron donne d ln Pₛₐₜ/dT=L(T)/(RT²). La loi de Regnault est L(T)=A−BT, avec A en J/kg et B en J·kg⁻¹·K⁻¹.

T* est une température de référence, P*=Pₛₐₜ(T*) et L*=L(T*). Poser A=L*+BT*. L’intégration à partir de T* donne :

ln(Pₛₐₜ/P*)=−(A/R)(1/T−1/T*)−(B/R)ln(T/T*).

Le laboratoire représente des rapports de pression : aucune valeur de P* n’est nécessaire pour comparer les pentes. Les coefficients servent à une étude locale du mécanisme, loin du point critique.

## 60. Comparer les pentes avant de changer de phase

Spé · Laboratoire `brouillard`

Une vapeur initialement saturante se détend adiabatiquement et quasistatiquement. Tant qu’elle reste seule, la loi de Laplace d’un gaz parfait donne P/P*=(T/T*)^{γ/(γ−1)}, avec γ=cₚ/cᵥ>1.

Lors d’un petit refroidissement dT<0, la saturation diminue plus vite que la pression de la vapeur si sa dérivée est plus grande au point initial. La vapeur seule ne peut alors rester à l’équilibre : la condensation commence.

L*/(RT*) > γ/(γ−1), soit T* < A(γ−1)/[Rγ+B(γ−1)].

Le sens de l’inégalité vient du signe négatif de dT. À égalité des pentes, le premier ordre ne suffit pas. La carte montre la marge L*/(RT*)−γ/(γ−1) pour des états initiaux indépendants.

Au début de la condensation, la chaleur latente modifie l’évolution. La loi de Laplace de la vapeur seule doit s’arrêter. Les tracés ne calculent ni la quantité condensée ni l’état final du mélange : il faudrait un bilan diphasé supplémentaire.
