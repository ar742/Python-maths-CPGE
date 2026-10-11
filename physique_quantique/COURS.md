# Physique quantique — cours et exercices

Volet 05 de Python-maths-CPGE. Neuf laboratoires pour relier ondes, probabilités, énergie et information quantique.

Les résultats théoriques et les observations numériques sont distingués. Les approfondissements sont signalés.

## 1 · Amplitudes, probabilités et états

*SUP · FONDATIONS*

**Notations.** r est la position en m et t le temps en s. ψ et φ sont des fonctions d’onde ; l’étoile * désigne la conjugaison complexe. |n⟩ est un état de base et cₙ son amplitude complexe ; Re et Im désignent les parties réelle et imaginaire.

Une fonction d’onde ψ décrit un état, pas une trajectoire. En représentation spatiale, |ψ(r,t)|² est une densité de probabilité : intégrer sur un domaine donne la probabilité d’y détecter la particule. La normalisation vaut ∫|ψ|²dV=1. Une onde plane sur tout l’espace n’est pas normalisable ; on emploie un paquet d’ondes ou une normalisation dans un volume spécifié.

⟨φ|ψ⟩=∫φ*(r)ψ(r)dV ; |ψ⟩=Σₙcₙ|n⟩ ; cₙ=⟨n|ψ⟩.
Base orthonormée : Σₙ|cₙ|²=1 ; probabilité du résultat n : |cₙ|².

**Pourquoi additionner des amplitudes ?** Pour ψ=c₁ψ₁+c₂ψ₂, |ψ|²=|c₁ψ₁|²+|c₂ψ₂|²+2Re(c₁*c₂ψ₁*ψ₂). Le dernier terme dépend de la phase relative et produit les interférences. Un mélange statistique sans cohérence ne possède pas ce terme. Multiplier tout ψ par une même phase ne change aucune probabilité.

**Compétence de Sup.** Vérifier dimensions et normalisation avant de calculer. En dimension 1, ψ a l’unité m⁻¹ᐟ² ; en dimension 3, m⁻³ᐟ². L’amplitude cₙ est sans dimension. Dans le laboratoire, les axes et unités réduites sont déclarés ; une densité n’est pas une probabilité sans son élément de volume.

## 2 · Schrödinger, conservation et courant

*SUP → SPÉ · FONDATIONS*

**Notations.** i²=−1 ; ℏ=h/(2π) est la constante de Planck réduite. m est la masse, V l’énergie potentielle, H l’opérateur énergie et Δ le laplacien spatial. φₙ et Eₙ sont un état propre et son énergie ; j est le courant de probabilité.

iℏ ∂ₜψ=Hψ ; H=−ℏ²Δ/(2m)+V(r).
État propre : Hφₙ=Eₙφₙ ; ψₙ(r,t)=φₙ(r)e⁻ⁱᴱⁿᵗᐟℏ.
Si H ne dépend pas du temps : |ψ(t)⟩=Σₙcₙe⁻ⁱᴱⁿᵗᐟℏ|n⟩.

Un état propre possède une densité spatiale stationnaire, bien que sa phase évolue. Une superposition de deux énergies distinctes peut avoir une densité variable. Pour un Hamiltonien auto-adjoint, U(t)=exp(−itH/ℏ) est unitaire : la norme et la probabilité totale sont conservées. Sur une onde plane eⁱᵏˣ, le Laplacien donne −k² ; l’énergie libre vaut donc +ℏ²k²/(2m).

ρ(r,t)=|ψ|² ; j=(ℏ/m)Im(ψ*∇ψ).
∂ₜρ+div j=0 ; en 1D, Aeⁱᵏˣ porte j=ℏk|A|²/m.

**Preuve.** Multiplier Schrödinger par ψ*, son conjugué par ψ, puis soustraire. Le potentiel réel s’élimine ; écrire le terme en dérivées comme une divergence donne l’équation de continuité. Le courant réfléchi est négatif : la probabilité de réflexion emploie sa valeur absolue.

**Deux objets différents.** La densité spatiale ρ(r)=|ψ(r)|² est un nombre dépendant de r. L’opérateur densité ρ̂=|ψ⟩⟨ψ|, ou une moyenne de tels projecteurs, est une matrice ou un opérateur de trace 1. Son évolution est iℏρ̂̇=[H,ρ̂]. La conservation spatiale ne comporte pas le facteur iℏ devant ∂ₜ|ψ|².

## 3 · Une particule dans une boîte cubique

*SUP → SPÉ · TP PRIORITAIRE*

**Notations.** L est le côté du cube en m et m la masse de la particule. Les entiers nₓ,nᵧ,n_z identifient les modes ; ℏ est la constante de Planck réduite. E₀ désigne ici l’échelle d’énergie de confinement, appelée E_L dans les commandes.

La particule est libre à l’intérieur du cube 0<x,y,z<L, entouré de parois de potentiel infini. La condition est ψ=0 sur les faces. Elle ne demande pas l’égalité des dérivées aux faces opposées : ajouter cette condition exclurait notamment les modes impairs et le fondamental.

φₙₓₙᵧₙ_z=(2/L)³ᐟ² sin(nₓπx/L) sin(nᵧπy/L) sin(n_zπz/L), nₓ,nᵧ,n_z≥1.
Eₙ=E₀(nₓ²+nᵧ²+n_z²), E₀=π²ℏ²/(2mL²).

**Démonstration.** Séparer ψ=X(x)Y(y)Z(z) dans Hψ=Eψ. Chacun des trois termes ne dépendant que d’une coordonnée est constant : E=Eₓ+Eᵧ+E_z. En 1D, X″+k²X=0 et X(0)=X(L)=0 donnent k=nπ/L. L’intégrale de sin² sur [0,L] vaut L/2 ; multiplier les trois normalisations donne celle du cube.

Le fondamental (1,1,1) a l’énergie 3E₀, non nulle. Le niveau suivant vaut 6E₀ et possède trois états spatiaux : (2,1,1), (1,2,1), (1,1,2). Cette dégénérescence vient des permutations des coordonnées ; elle ne comprend pas le spin. Dilater L d’un facteur 2 divise toutes les énergies par 4.

Une coupe de |ψ|² à z fixé renseigne sur la distribution spatiale ; une marginale en x intègre y et z et vaut 2sin²(nₓπx/L)/L. Une coupe et une marginale sont différentes. La carte du laboratoire est la marginale en (x,y), obtenue en intégrant z : ce n’est pas une coupe à z fixé. Le laboratoire affiche aussi des niveaux et leur dégénérescence, afin de relier séparation des variables, symétries du cube et quantification.

## 4 · Conditions périodiques et battements

*SPÉ · TP ET APPROFONDISSEMENT*

**Notations.** L est la période spatiale ou le côté de la boîte selon les conditions choisies ; k est le vecteur d’onde en m⁻¹. Deux modes d’énergies E₁,E₂ sont superposés avec poids w et phase initiale δ. La pulsation de battement est |E₂−E₁|/ℏ.

Une boîte avec parois et une normalisation périodique décrivent deux problèmes distincts. Avec conditions périodiques, ψ(x+L,y,z)=ψ(x,y,z), et de même pour y,z : les faces opposées sont identifiées. Les modes sont des ondes planes ; il n’y a pas de paroi matérielle infinie.

φₙ(r)=L⁻³ᐟ² exp(2πi n·r/L), n∈Z³.
Eₙ=E₀|n|², E₀=(2π)²ℏ²/(2mL²). Le mode n=0 a E=0.
ψ=√(1−w)φₙe⁻ⁱᴱⁿᵗᐟℏ+√w eⁱᵟφ_me⁻ⁱᴱᵐᵗᐟℏ ; m=n+(1,0,0).

L’orthogonalité des deux modes donne ⟨ψ|ψ⟩=(1−w)+w=1, pour 0≤w≤1. Le paramètre « mélange » du laboratoire est le poids w du second mode dans une **superposition cohérente**. Il ne désigne pas un mélange statistique. L’énergie moyenne est (1−w)Eₙ+wE_m, constante, mais le terme d’interférence évolue à la pulsation |E_m−Eₙ|/ℏ.

Le temps affiché est τ=E₀t/ℏ, avec l’E₀ adapté à la condition de bord. Pour les parois et nₓ=1, mₓ=2, la différence réduite vaut 3 : la période des battements est 2π/3 en τ. L’intégration sur tout le cube annule le terme croisé, bien que la densité locale évolue.

**Ouverture vers PS.** Une grille périodique des vecteurs d’onde permet de compter les états dans l’espace k : un état spatial occupe un volume (2π/L)³. Le comptage asymptotique des modes aux parois donne la même densité dominante à grand volume, mais pas le même fondamental ni les mêmes corrections de bord.

## 5 · Heisenberg : une borne sur des dispersions

*SUP → SPÉ · TP PRIORITAIRE*

**Notations.** x̂ et p̂ sont les opérateurs position et impulsion ; ⟨A⟩ désigne la moyenne d’une observable A. ΔA est son écart type ; [A,B]=AB−BA est un commutateur. σ est la largeur initiale de la gaussienne, p₀ son impulsion moyenne et m la masse.

Δx et Δp sont les écarts types des résultats de mesures sur des systèmes préparés dans un même état. L’inégalité ne décrit pas à elle seule un défaut instrumental. Poser X=x̂−⟨x̂⟩ et P=p̂−⟨p̂⟩ ; on considère des états pour lesquels les moments et les produits utilisés existent.

0≤‖(X+iλP)ψ‖²=(Δx)²+λ²(Δp)²−λℏ, λ réel.
[x̂,p̂]=iℏI ⇒ ΔxΔp≥ℏ/2.

Le trinôme est positif pour tout λ : son discriminant est ≤0. Cela donne la borne. Plus généralement, Cauchy–Schwarz conduit à ΔAΔB≥|⟨[A,B]⟩|/2 pour des observables convenablement définies. Le temps est ici un paramètre : on ne peut pas déduire « de même » une inégalité universelle ΔEΔt à partir d’un opérateur temps canonique. Les relations de durée d’évolution, par exemple Mandelstam–Tamm, demandent un sens précis de la durée.

ψ(x)=(2πσ²)⁻¹ᐟ⁴ exp[−x²/(4σ²)+ip₀x/ℏ] : Δx=σ, Δp=ℏ/(2σ).
Évolution libre : ⟨x⟩=p₀t/m ; Δx(t)=σ√[1+(ℏt/(2mσ²))²].

La gaussienne sans phase quadratique sature la borne à t=0 ; elle s’étale ensuite alors que sa distribution d’impulsion reste inchangée. Une phase quadratique, crée une covariance position–impulsion et peut faire commencer le paquet par une contraction. La borne renforcée est (Δx)²(Δp)²≥ℏ²/4+Cov(x,p)², où Cov=⟨XP+PX⟩/2. La valeur ℏ/2 du produit n’est donc pas préservée par toute évolution libre.

## 6 · Ce qu’Heisenberg permet de retrouver

*SUP → SPÉ · TP CLASSIQUES*

**Notations.** a est la largeur de fente, λ la longueur d’onde et θ l’angle de diffraction. Pour les estimations d’énergie, m est la masse, r une taille de localisation, e la charge élémentaire et ε₀ la permittivité du vide. Pour l’oscillateur, ω est sa pulsation.

**Fente et diffraction.** Localiser transversalement une onde sur une largeur a produit une dispersion de vecteur d’onde de l’ordre 1/a. On retrouve l’échelle angulaire λ/a. Pour une fente rectangulaire idéale, Fraunhofer donne I(θ)∝[sin u/u]², u=πa sinθ/λ, avec la limite 1 en u=0 ; le premier zéro est sinθ=λ/a. Le moteur emploie sinc(v)=sin(πv)/(πv), donc le même profil s’écrit sinc²(a sinθ/λ). Mais le second moment de la distribution d’impulsion de ce profil idéal diverge : Δp n’est pas un nombre fini que l’on pourrait identifier à ℏ/a. Utiliser les premiers zéros pour la fente, les écarts types pour une gaussienne.

**Young et information de chemin.** Deux fentes séparées de d donnent l’interfrange i≈λD/d. Si l’environnement reçoit des états |d₁⟩ et |d₂⟩ selon la fente, le terme d’interférence est multiplié par ⟨d₂|d₁⟩. À poids égaux, la visibilité vaut |⟨d₂|d₁⟩| : états identiques, interférence entière ; états orthogonaux, information de chemin complète et terme croisé nul. Une explication par transfert d’impulsion peut être utile dans un modèle expérimental, mais ne remplace pas ce calcul général.

Oscillateur : ⟨H⟩≥(Δp)²/(2m)+mω²(Δx)²/2
≥ℏ²/[8m(Δx)²]+mω²(Δx)²/2≥ℏω/2.

Les termes contenant les moyennes sont positifs. La minimisation en u=(Δx)² donne u=ℏ/(2mω) et l’énergie ℏω/2. Ici la borne est **exacte et atteinte** : la gaussienne centrée est le fondamental. Pour une boîte de largeur L, Δx≤L/2 donne seulement E≥ℏ²/(2mL²), moins forte que E₁=π²ℏ²/(2mL²).

Hydrogène, estimation : E(r)≈ℏ²/(2mr²)−C/r, C=e²/(4πε₀).
r*=ℏ²/(mC)=a₀≈53 pm ; E(r*)=−mC²/(2ℏ²)≈−13,6 eV.

Le choix p∼ℏ/r est une estimation d’échelle, pas une preuve exacte tirée de ΔxΔp≥ℏ/2. Les coefficients numériques de cette estimation ont été choisis. En complément, la famille normalisée ψ_a=(πa³)⁻¹ᐟ²e⁻ʳᐟᵃ donne exactement ⟨T⟩=ℏ²/(2ma²), ⟨V⟩=−C/a ; le principe variationnel et le fait que ψ_{a₀} soit un état propre rendent alors la valeur exacte dans le modèle coulombien non relativiste à noyau fixe. Le rayon a₀ n’est pas la moyenne radiale de cet état : ⟨r⟩=3a₀/2.

## 7 · Marche de potentiel : raccorder des flux

*SUP → SPÉ · EXERCICE 1*

**Notations.** E est l’énergie incidente, V₀ la hauteur de marche et m la masse constante. Les nombres d’onde sont k₁ à gauche et k₂ à droite ; κ est un taux de décroissance en m⁻¹. r et t sont des amplitudes complexes, R et T des rapports de courants.

Soit V=0 à gauche et V=V₀ à droite ; une onde arrive de gauche. Pour une discontinuité finie de V, avec masse constante, ψ et ψ′ sont continues. Intégrer Schrödinger autour de la marche donne ψ′(x₀+ε)−ψ′(x₀−ε)=(2m/ℏ²)∫_{x₀−ε}^{x₀+ε}(V−E)ψdx : le signe est positif. L’intégrale tend vers 0 pour un potentiel borné, donc ψ′ ne subit pas de saut. Une barrière infinie ou un potentiel delta exigent un autre traitement.

E>V₀ : ψ_g=eⁱᵏ¹ˣ+r e⁻ⁱᵏ¹ˣ ; ψ_d=t eⁱᵏ²ˣ.
k₁=√(2mE)/ℏ ; k₂=√(2m(E−V₀))/ℏ.
1+r=t ; k₁(1−r)=k₂t.
r=(k₁−k₂)/(k₁+k₂) ; t=2k₁/(k₁+k₂).

R=|r|² ; T=(k₂/k₁)|t|²=4k₁k₂/(k₁+k₂)² ; R+T=1.

Le facteur k₂/k₁ vient du courant, et non de la normalisation des amplitudes. Le rapport |t|² peut dépasser 1 sans que T dépasse 1. Une réflexion existe même si E>V₀, alors que le mouvement classique traverserait sans réflexion : la différence de longueurs d’onde impose les raccordements.

Si 0<E<V₀, la solution bornée à droite est t e⁻ᵏˣ, avec κ=√(2m(V₀−E))/ℏ. Elle est évanescente et ne porte aucun flux net : T=0 et R=1. Une densité non nulle au-delà de la marche ne signifie pas une transmission vers +∞. Cette distinction prépare l’effet tunnel à travers une barrière de largeur finie.

## 8 · Barrière finie et effet tunnel

*SPÉ · EXERCICE 2 PRIORITAIRE*

**Notations.** E est l’énergie incidente, V₀ la hauteur de barrière et a sa largeur. m est la masse, κ le taux de décroissance pour E<V₀ et q le nombre d’onde dans la barrière pour E>V₀. T est le rapport du courant transmis au courant incident ; sech u=1/cosh u.

Le potentiel vaut V₀ sur 0<x<a et 0 ailleurs. Raccorder ψ et ψ′ en x=0 et x=a donne quatre équations pour l’onde réfléchie, les deux composantes dans la barrière et l’onde transmise. Pour E<V₀, garder les deux exponentielles dans la région finie : éliminer celle qui croît serait incorrect sur un intervalle borné.

0<E<V₀ : κ=√(2m(V₀−E))/ℏ.
T={1+[V₀²/(4E(V₀−E))]sinh²(κa)}⁻¹.
E>V₀ : q=√(2m(E−V₀))/ℏ.
T={1+[V₀²/(4E(E−V₀))]sin²(qa)}⁻¹.

**Vérifications.** À a→0, T→1. Les deux formules ont la même limite en E=V₀ : T=[1+mV₀a²/(2ℏ²)]⁻¹. Au-dessus de la barrière, qa=ℓπ donne T=1 : des résonances de transmission peuvent supprimer la réflexion. Pour E=V₀/2, la formule sous la barrière se simplifie en T=sech²(κa).

Si κa≫1 : T≈[16E(V₀−E)/V₀²]e⁻²ᵏᵃ.

L’exponentielle explique la grande sensibilité à la largeur et à la masse : κ∝√m. Ce résultat est une probabilité de transmission d’un état incident stationnaire, pas une violation de la conservation d’énergie. La densité dans la barrière n’est pas la trajectoire d’une particule classique ayant une énergie cinétique négative.

Les régions extérieure gauche et droite ont ici le même potentiel et la même masse, donc T=|t|². Si les milieux diffèrent, il faut réintroduire le rapport des vitesses. Le laboratoire emploie ℏ=m=1 et annonce ces unités réduites. Les amplitudes numériques sont comparées à la formule exacte et les flux doivent vérifier R+T=1.

## 9 · Oscillateur harmonique : échelle d’énergie

*SPÉ · CLASSIQUE ET EXTENSION GUIDÉE*

**Notations.** m est la masse et ω la pulsation de l’oscillateur ; ℓ=√(ℏ/(mω)) fixe son échelle de longueur. X=x/ℓ et P=p/√(mℏω) sont sans dimension. a et a† sont les opérateurs d’abaissement et d’élévation ; n est le nombre entier d’excitations.

L’oscillateur décrit le voisinage d’un minimum stable de potentiel : V(x)≈V(0)+mω²x²/2. Il relie la résolution d’une équation différentielle, les polynômes d’Hermite et une méthode algébrique. Les variables réduites sont X=x/ℓ et P=p/√(mℏω), avec ℓ=√(ℏ/(mω)) : [X,P]=i.

a=(X+iP)/√2 ; a†=(X−iP)/√2 ; [a,a†]=I.
H=ℏω(a†a+I/2).
a|n⟩=√n|n−1⟩ ; a†|n⟩=√(n+1)|n+1⟩ ; Eₙ=ℏω(n+1/2).

**Construction.** Pour un état normalisé, ⟨a†a⟩=‖aψ‖²≥0, donc E≥ℏω/2. Chercher aψ₀=0 donne ψ₀′=−xψ₀/ℓ² : ψ₀=(πℓ²)⁻¹ᐟ⁴e⁻ˣ²ᐟ²ˡ². Appliquer n fois a†, puis normaliser par √n!, construit les états. Le commutateur [H,a†]=ℏωa† montre l’espacement constant des énergies. On utilise l’identité de Leibniz correcte [A,BC]=[A,B]C+B[A,C], obtenue en ajoutant et retranchant BAC ; aucun facteur A ne précède [A,BC].

ψₙ(x)=Hₙ(x/ℓ)e⁻ˣ²ᐟ²ˡ²/[π¹ᐟ⁴√(ℓ2ⁿn!)].
H₀=1 ; H₁=2u ; Hₙ₊₁=2uHₙ−2nHₙ₋₁.
⟨x⟩=⟨p⟩=0 ; Δx=ℓ√(n+1/2) ; Δp=√(mℏω)√(n+1/2).

Le produit ΔxΔp=(n+1/2)ℏ sature Heisenberg seulement pour n=0. Chaque ψₙ a n nœuds réels et une parité (−1)ⁿ. Les densités sont stationnaires ; elles peuvent pénétrer dans la zone classiquement interdite |x|>√(2Eₙ/(mω²)). Une densité ne doit pas être lue comme une position déterministe à une date donnée.

## 10 · États cohérents et mouvement classique

*SPÉ · EXTENSION EMBLÉMATIQUE*

**Notations.** a est l’opérateur d’abaissement et α un nombre complexe définissant l’état cohérent. n compte les excitations ; m,ω et ℓ=√(ℏ/(mω)) sont la masse, la pulsation et la longueur de l’oscillateur. H est l’opérateur énergie ; Re α et Im α sont les composantes de α.

a|α⟩=α|α⟩ ; |α⟩=exp(−|α|²/2) Σₙαⁿ|n⟩/√n!.
α(t)=α(0)exp(−iωt) ; ⟨x⟩=√2ℓ Re α(t) ; ⟨p⟩=√(2mℏω) Im α(t).
Δx=ℓ/√2 ; Δp=√(mℏω/2) ; ⟨H⟩=ℏω(|α|²+1/2).

La série est normalisée car Σ|α|²ⁿ/n!=e^{|α|²}. Les phases d’évolution de chaque état propre transforment α en αe⁻ⁱʷᵗ, à une phase globale près. Le paquet gaussien tourne dans le plan position–impulsion et sa largeur reste constante : l’oscillateur conserve la forme des états cohérents.

**Ehrenfest.** Schrödinger donne d⟨x⟩/dt=⟨p⟩/m et d⟨p⟩/dt=−⟨V′(x)⟩. Pour V quadratique, ⟨V′(x)⟩=mω²⟨x⟩ : la moyenne suit exactement l’équation classique. Pour un potentiel général, ⟨V′(x)⟩≠V′(⟨x⟩) en général ; remplacer la moyenne d’une fonction par la fonction de la moyenne demande une approximation de paquet étroit.

Un état cohérent avec α≠0 n’est pas un état propre d’énergie. Sa mesure de n suit une loi de Poisson de moyenne |α|² et de variance |α|². Le mouvement de sa moyenne explique un aspect de la limite classique ; la fluctuation de point zéro et l’incertitude subsistent.

## 11 · Deux systèmes : corrélation et intrication

*SPÉ · TP PRIORITAIRE*

**Notations.** |0⟩ et |1⟩ forment la base d’un qubit ; ⊗ désigne le produit tensoriel. Les coefficients de l’état à deux qubits forment une matrice C. ρ est un opérateur densité et Tr_B la trace sur le second système, qui fournit l’état réduit du premier.

L’espace d’un système composé est un produit tensoriel. Deux qubits ont une base |00⟩, |01⟩, |10⟩, |11⟩. Un état pur est séparable s’il s’écrit |u⟩⊗|v⟩ ; sinon il est intriqué. Une opération locale sur A s’écrit U_A⊗I_B. Les coefficients d’un état pur peuvent être rangés dans une matrice C de taille 2×2.

|ψ⟩=c₀₀|00⟩+c₀₁|01⟩+c₁₀|10⟩+c₁₁|11⟩.
État pur séparable ⇔ det C=c₀₀c₁₁−c₀₁c₁₀=0.
|Φ⁺⟩=(|00⟩+|11⟩)/√2 ; ρ_A=Tr_B |Φ⁺⟩⟨Φ⁺|=I/2.

**Preuve du critère.** Un produit donne cᵢⱼ=uᵢvⱼ, donc C est de rang 1. Réciproquement, une matrice non nulle de rang 1 se factorise ainsi. Le déterminant de Φ⁺ vaut 1/2 : cet état n’est pas un produit. Chaque qubit seul est dans un état mélangé, bien que la paire soit dans un état pur.

ρ_classique=(|00⟩⟨00|+|11⟩⟨11|)/2.
P(00)=P(11)=1/2 dans la base Z pour les deux préparations.
⟨X⊗X⟩=1 pour Φ⁺, mais 0 pour ρ_classique.

La corrélation parfaite dans une seule base ne démontre donc pas l’intrication : le mélange classique donne les mêmes résultats dans cette base. Changer de base révèle la cohérence. Les résultats locaux restent aléatoires ; une opération locale sans sélection de résultat laisse la matrice réduite distante inchangée. L’intrication ne fournit pas un canal de communication instantanée.

Le laboratoire utilise un état de polarisation corrélé Φ⁺. Il le distingue du singulet de deux spins 1/2, |Ψ⁻⟩=(|01⟩−|10⟩)/√2, dont les corrélations de spin sont opposées le long d’un même axe. Le vocabulaire « singulet » et les angles physiques de polariseurs ne doivent pas être interchangés sans préciser la base.

## 12 · Bell, CHSH et bruit de Werner

*SPÉ · TP ET EXTENSION GUIDÉE*

**Notations.** X et Z sont les matrices de Pauli ; M(a) est l’observable d’un analyseur d’angle a. E(a,b) est la moyenne du produit des deux résultats ±1 ; S combine quatre corrélations. v est le poids de l’état de Bell dans le mélange de Werner et I₄ la matrice identité 4×4.

Pour des analyseurs de polarisation rectiligne, l’angle physique a correspond à l’observable M(a)=cos(2a)Z+sin(2a)X. Le facteur 2 vient de la représentation des états de polarisation sur la sphère de Bloch. Les résultats des deux analyseurs sont codés ±1.

Φ⁺ : E(a,b)=cos[2(a−b)].
P₊₊=P₋₋=cos²(a−b)/2 ; P₊₋=P₋₊=sin²(a−b)/2.
S=|E(a,b)+E(a,b′)+E(a′,b)−E(a′,b′)|.

**Borne classique.** Dans un modèle local à résultats ±1 prédéterminés par une variable commune λ, la combinaison vaut A(B+B′)+A′(B−B′). Un des deux termes entre parenthèses vaut 0, l’autre ±2. La moyenne a donc une valeur absolue ≤2, sous les hypothèses de localité et d’indépendance des choix de réglages. Le calcul théorique ne simule pas à lui seul toutes les précautions d’une expérience de Bell.

a=0°, a′=45°, b=22,5°, b′=−22,5° ⇒ S=2√2.
ρ_v=v|Φ⁺⟩⟨Φ⁺|+(1−v)I₄/4 : E_v=v cos[2(a−b)], S_max=2√2v.

La violation CHSH pour cette famille apparaît lorsque v>1/√2. Ce seuil n’est pas celui de l’intrication : pour la famille de Werner choisie, l’état est intriqué dès v>1/3, ce que révèle le critère de transposition partielle en dimension 2×2. Une expérience qui ne viole pas cette inégalité avec ces réglages ne suffit donc pas à déclarer l’état séparable.

Le mélange classique du laboratoire est ρ_classique,v=vρ_classique+(1−v)I₄/4. Il donne E_classique,v=v cos(2a)cos(2b), conserve les marges 1/2 et respecte S≤2. À v=1, on retrouve le mélange de 00 et 11 de la leçon précédente. Comparer les deux familles et des angles non optimaux apprend à distinguer une préparation, des réglages de mesure et un témoin d’intrication.

## 13 · Josephson : phase, courant et tension

*SPÉ · EXERCICE 3 ET EXTENSION*

**Notations.** δ est la différence de phase de la jonction, I_c son courant critique et V sa tension. e est la charge élémentaire ; les paires portent la charge 2e. K désigne l’énergie du couplage lorsqu’elle intervient dans le modèle à deux amplitudes.

Une jonction Josephson relie deux supraconducteurs par un couplage faible. Une phase macroscopique décrit chaque condensat ; leur différence gauge-invariante δ contrôle le supercourant. Une paire de Cooper a une charge de valeur absolue q=2e. Le modèle du laboratoire conserve uniquement les relations Josephson, sans dissipation, capacité ni fluctuations thermiques.

I=I_c sinδ ; δ̇=2eV/ℏ.
V constant : δ(t)=δ₀+(2eV/ℏ)t ; f_J=2e|V|/h.

À V=0, une phase constante peut porter un courant continu, limité en valeur absolue par I_c. À tension constante non nulle, le courant oscille. La convention d’orientation fixe le signe de V, I et δ ; la fréquence positive utilise |V|. Une tension de 1 µV donne environ 483,6 MHz.

**Modèle à deux amplitudes.** Écrire ψ_A=√N_Aeⁱᶿᴬ et ψ_B=√N_Beⁱᶿᴮ dans iℏψ̇_A=E_Aψ_A+Kψ_B, iℏψ̇_B=Kψ_A+E_Bψ_B, avec K réel. La partie imaginaire donne Ṅ_A=2K√(N_AN_B)sin(θ_B−θ_A)/ℏ. Le courant de charge qṄ_A a donc une amplitude 2q|K|√(N_AN_B)/ℏ, indépendante de la phase. Si N_A≈N_B sont maintenus par des réservoirs, la différence d’énergie électrochimique E_A−E_B=qV impose δ̇=qV/ℏ, selon l’orientation retenue.

**Correction de convention.** Si les termes diagonaux sont écrits +qV/2 et −qV/2, leur différence vaut qV. Les écrire +qV et −qV double la différence et impose un facteur 2 différent. Une amplitude I_c proportionnelle à δ confondrait l’amplitude avec la linéarisation du courant : pour |δ|≪1, I≈I_cδ, mais I_c reste un paramètre de la jonction.

## 14 · SQUID : une interférence de phases

*SPÉ · APPLICATION EMBLÉMATIQUE*

**Notations.** I₁ et I₂ sont les courants critiques des deux jonctions. Φ est le flux dans la boucle et Φ₀=h/(2e) le quantum de flux, en Wb. δ est la phase moyenne et I_c(Φ) le courant maximal à flux fixé.

Un SQUID continu contient deux jonctions en parallèle dans une boucle. On suppose l’inductance de boucle suffisamment faible pour négliger le flux créé par le courant, et deux relations sinusoïdales de courant. La différence des phases de jonction est fixée, modulo 2π, par le flux appliqué Φ.

Φ₀=h/(2e)≈2,068×10⁻¹⁵ Wb ; δ₁−δ₂=2πΦ/Φ₀.
δ₁=δ̄+πf ; δ₂=δ̄−πf ; f=Φ/Φ₀.
I=(I₁+I₂)sinδ̄ cosπf+(I₁−I₂)cosδ̄ sinπf.

À flux fixé, le courant total est A sinδ̄+B cosδ̄. Son maximum en valeur absolue est √(A²+B²), obtenu en écrivant le sinus déphasé correspondant. Cette maximisation donne directement la modulation du courant critique.

I_c,eff(Φ)=√[I₁²+I₂²+2I₁I₂ cos(2πΦ/Φ₀)].
I₁=I₂=I_c : I_c,eff=2I_c|cos(πΦ/Φ₀)|.

La période est Φ₀. Deux jonctions identiques annulent le courant critique aux demi-entiers ; une asymétrie donne un minimum |I₁−I₂|. Il s’agit d’une interférence de phases quantiques macroscopiques, avec une analogie utile aux deux chemins optiques. Le laboratoire trace le courant critique théorique, pas la tension de sortie d’un appareil réel : cette dernière demande un modèle de polarisation et de dissipation.

## 15 · Spin, RMN et référentiel tournant

*SPÉ · EXERCICE 4 PRIORITAIRE*

**Notations.** X,Y,Z sont les matrices de Pauli et I l’identité 2×2. γ est le rapport gyromagnétique en rad·s⁻¹·T⁻¹, B₀ le champ statique et B₁ l’amplitude du champ circulaire. ω₀ est la pulsation de Larmor, ω celle du champ appliqué ; Δ est leur désaccord selon la convention annoncée.

Un spin 1/2 possède deux niveaux. Les matrices de Pauli sont X=[[0,1],[1,0]], Y=[[0,−i],[i,0]], Z=diag(1,−1), et S=(ℏ/2)σ dans une base de spin donnée. Le couplage magnétique réel est H_Z=−γ S·B. Pour le proton, la fréquence de Larmor en valeur absolue est ω_L=|γ|B₀, avec |γ|/(2π)≈42,58 MHz/T.

Une identité ℏω₀I ne décrit aucune séparation Zeeman : elle ajoute la même énergie aux deux états et seulement une phase globale. Pour étudier un système à deux niveaux, choisir explicitement une base avec des énergies ±ℏω₀/2. Pour une RMN réelle, le signe de γ, l’ordre des états et l’hélicité du champ déterminent les signes des phases ; les probabilités de transition ci-dessous ne dépendent pas de ce choix cohérent.

Modèle circulaire : H(t)=(ℏ/2){ω₀Z+Ω[cos(ωt)X+sin(ωt)Y]}.
R(t)=exp(−iωtZ/2), |ψ⟩=R|χ⟩.
H_rot=R†HR−iℏR†Ṙ=(ℏ/2)(ΔZ+ΩX), Δ=ω₀−ω.

Le changement de référentiel est ici exact pour le champ circulaire idéal choisi. Le calcul produit le terme −ℏωZ/2 : l’oublier supprime le désaccord Δ. Le champ effectif est constant ; résoudre Schrödinger revient à exponentier une matrice 2×2.

**Amplitude radiofréquence.** Pour un champ transverse circulaire d’amplitude B₁, Ω=|γ|B₁. Un champ réel linéaire B_lin cosωt s’écrit comme deux composantes circulaires d’amplitude B_lin/2. L’approximation de l’onde tournante conserve la composante presque résonante, donnant Ω≈|γ|B_lin/2 lorsque |Δ| et Ω sont petits devant ω₀. Cette approximation n’est pas nécessaire pour le modèle circulaire exact. Le laboratoire sépare les paramètres réduits de Rabi et l’exemple physique RMN.

## 16 · Oscillations de Rabi et impulsions

*SPÉ · EXERCICE 4 ET MÉTHODE*

**Notations.** Ω est la pulsation de couplage et Δ le désaccord ; t est le temps. X et Z sont les matrices de Pauli, I l’identité et H_rot l’opérateur énergie dans le repère tournant. U(t) fait évoluer l’état ; P₁ est la probabilité de mesurer |1⟩.

H_rot=(ℏ/2)(ΔZ+ΩX), Ω_R=√(Δ²+Ω²).
U(t)=cos(Ω_Rt/2)I−i sin(Ω_Rt/2)(ΔZ+ΩX)/Ω_R.
Partant de |0⟩ : P₁(t)=Ω²/(Ω²+Δ²) sin²(Ω_Rt/2).

**Preuve.** Les matrices de Pauli anticommutent et X²=Z²=I. Donc (ΔZ+ΩX)²=(Δ²+Ω²)I. Séparer termes pairs et impairs de l’exponentielle donne U. Sa composante hors diagonale appliquée à |0⟩ donne la probabilité annoncée ; l’évolution est unitaire.

À résonance Δ=0, P₁=sin²(Ωt/2) atteint 1 : une impulsion π de durée t_π=π/Ω inverse la population. Une impulsion π/2 de durée π/(2Ω) crée (|0⟩−i|1⟩)/√2 dans la convention d’axe X. Partant de |0⟩, le vecteur de Bloch est (0,−sinΩt,cosΩt) ; l’impulsion π/2 l’amène donc sur l’axe −Y. Les populations valent chacune 1/2, mais il s’agit d’un état pur cohérent et sa phase compte pour la prochaine impulsion.

Hors résonance, l’amplitude maximale Ω²/(Ω²+Δ²) est inférieure à 1 et la pulsation augmente. Une durée π/Ω ne suffit plus à inverser complètement. Sur la sphère de Bloch, l’état tourne autour de l’axe (Ω,0,Δ), au lieu de l’axe X à résonance. Pour un proton et un champ circulaire de 10 µT, t_π≈1,17 ms ; pour un champ linéaire de même amplitude crête, la durée dans l’approximation tournante est environ doublée.

L’impulsion décrite est rectangulaire, sans relaxation T₁/T₂ ni distribution de fréquences. Les courbes illustrent l’évolution cohérente d’un spin idéal ; en RMN macroscopique, le signal mesuré vient d’un ensemble de spins avec préparation et détection appropriées.

## 17 · Un qubit sur et dans la sphère de Bloch

*SPÉ · INFORMATIQUE QUANTIQUE GUIDÉE*

**Notations.** θ est la colatitude et φ l’azimut ; n est le vecteur unitaire correspondant. r∈[0,1] est la longueur du vecteur de Bloch, ρ l’opérateur densité et σ=(X,Y,Z) les matrices de Pauli. m est un axe unitaire de mesure ; Tr est la trace.

|ψ⟩=cos(θ/2)|0⟩+eⁱᵠsin(θ/2)|1⟩, à une phase globale près.
n=(sinθcosφ,sinθsinφ,cosθ).
ρ=(I+r n·σ)/2, 0≤r≤1 ; Tr ρ²=(1+r²)/2.
P(+ selon m)=[1+r n·m]/2.

Un état pur est sur la sphère (r=1) ; un état mélangé est à l’intérieur. r=0 donne I/2. Le curseur de longueur r n’est pas directement la pureté Trρ² : celle-ci varie de 1/2 à 1. Dans la base Z, P(0)=cos²(θ/2) pour un état pur ; la phase φ ne change pas cette mesure, mais elle modifie les mesures en X et Y.

R_j(α)=exp(−iασ_j/2)=cos(α/2)I−i sin(α/2)σ_j.
H=(X+Z)/√2 ; H|0⟩=|+⟩ ; H|1⟩=|−⟩.
H : (x,y,z)→(z,−y,x) ; X : (x,y,z)→(x,−y,−z).

Les rotations unitaires tournent le vecteur de Bloch et conservent sa longueur. Elles ne purifient pas un état mélangé. Une rotation de 2π donne −|ψ⟩ au niveau du vecteur d’état mais la même matrice densité : la phase globale n’est pas observable sur le qubit isolé.

Les portes ne sont pas interchangeables : X puis H diffère de H puis X. L’analogie avec les rotations et leurs générateurs relie ce volet à l’algèbre de Lie du volet de calcul différentiel. Attention : la sphère d’un seul qubit ne représente pas l’état complet de deux qubits ; une matrice réduite I/2 ne précise pas si le qubit provient d’un mélange classique ou d’une paire intriquée.

## 18 · Circuits : Bell et Grover à deux qubits

*SPÉ · EXTENSION INFORMATIQUE QUANTIQUE*

**Notations.** H désigne ici la porte de Hadamard, et CNOT une porte à contrôle et cible. Les quatre états de base sont ordonnés |00⟩,|01⟩,|10⟩,|11⟩. Pour Grover, |m⟩ est l’état marqué, |s⟩ la superposition uniforme, O_m l’oracle et D la réflexion autour de |s⟩.

Un circuit compose des transformations unitaires et finit par une mesure. La base est ordonnée |00⟩, |01⟩, |10⟩, |11⟩ ; le premier qubit est celui de gauche. La porte CNOT a pour contrôle le premier qubit et inverse le second seulement si le contrôle vaut 1.

|00⟩ → (H⊗I)|00⟩=(|00⟩+|10⟩)/√2
→ CNOT : (|00⟩+|11⟩)/√2=|Φ⁺⟩.

H crée des amplitudes sur deux chemins logiques ; CNOT les corrèle sans mesure intermédiaire. Mesurer ensuite dans la base Z donne 00 ou 11 avec probabilités 1/2. Mesurer le contrôle entre les deux portes détruirait la cohérence et préparerait une corrélation classique, pas ce même état de Bell.

Grover, N=4 et un élément marqué m : |s⟩=(1/2)Σₓ|x⟩.
O_m=I−2|m⟩⟨m| ; D=2|s⟩⟨s|−I ; G=DO_m.
P_m(k)=sin²[(2k+1)θ], sinθ=1/2, donc θ=π/6.

L’oracle inverse seulement le signe de l’amplitude marquée. Le diffuseur reflète les amplitudes autour de leur moyenne : aₓ→2ā−aₓ. Après un oracle, les amplitudes valent −1/2 pour m et +1/2 ailleurs ; la moyenne vaut 1/4. La réflexion donne 1 pour m et 0 ailleurs : une itération réussit avec probabilité 1 dans ce modèle exact.

Ajouter des itérations peut diminuer le succès : pour k=0,1,2,3,4, les probabilités sont 1/4,1,1/4,1/4,1. Le gain asymptotique de Grover concerne le nombre de requêtes à un oracle accessible de façon cohérente, de l’ordre √N au lieu de N pour une recherche non structurée classique. Il ne dispense ni de construire l’oracle ni de lire le résultat par mesure. Le laboratoire est un simulateur exact de deux qubits, pas un calcul sur un processeur quantique.

## Préparer les laboratoires

### boite

Expliquer la quantification par les conditions aux limites, puis observer le battement de deux modes.

**Objets et unités.**

- L est le côté du cube en nm et mₑ la masse de l’électron ; x/L est une position réduite. ℏ=h/(2π), où h est la constante de Planck.
- nₓ,nᵧ,n_z identifient les modes ; les parois imposent des indices entiers strictement positifs. E_L est l’échelle d’énergie du mode unidimensionnel.
- w est le poids du second mode et δ sa phase initiale en degrés ; τ=tE_L/ℏ est le temps réduit. La densité |ψ|² se déduit de la fonction d’onde ψ.

**Hypothèses.**

- Une particule sans spin, libre dans le cube ; chaque choix de bord fixe ses modes et son échelle E_L.
- Le second mode remplace nₓ par nₓ+1. La carte intègre z : elle représente une probabilité marginale en x,y.

**Techniques.** Séparer les variables et appliquer les conditions aux limites.; Normaliser une fonction d’onde et additionner des amplitudes.; Identifier une dégénérescence et calculer une fréquence de battement.

**Première expérience.**

1. Choisir le fondamental, puis doubler L : prévoir le rapport des énergies.
2. Choisir nₓ=2, nᵧ=n_z=1 et retrouver les modes de même énergie.
3. Passer à w=1/2 et modifier le temps : comparer densité locale et énergie moyenne.

**Sup.** ondes, probabilités et unités ; préparation au confinement.
**Spé et filières.** MP §6 et PC §6.5 : puits infini et superposition ; le cube prolonge le problème unidimensionnel.
**Prolongements.** Normalisation périodique et comptage tridimensionnel des états : prolongements accompagnés.
**Résultat attendu.** Une énergie de confinement justifiée et une densité variable sans variation de l’énergie moyenne.

### heisenberg

Distinguer un écart type d’une largeur de diffraction et utiliser Heisenberg pour estimer une énergie minimale.

**Objets et unités.**

- σ est l’écart type initial de position, p₀ l’impulsion moyenne et c le coefficient de phase quadratique. Δx et Δp sont les écarts types de position et d’impulsion.
- m est la masse et ℏ la constante de Planck réduite ; les unités sont choisies pour ℏ=m=1. t est le temps et ω la pulsation dans ces unités.
- Pour la fente, a est sa largeur en µm et λ la longueur d’onde en nm ; la largeur a diffère d’un écart type.

**Hypothèses.**

- Évolution libre d’un paquet gaussien normalisé.
- Fente rectangulaire idéale en champ lointain ; ses bords abrupts rendent le second moment d’impulsion divergent.

**Techniques.** Calculer des moments et des écarts types.; Lire une transformée de Fourier et contrôler une approximation angulaire.; Minimiser une borne d’énergie en respectant son statut.

**Première expérience.**

1. Prendre c=0,t=0 et comparer ΔxΔp à ℏ/2.
2. Augmenter t, puis essayer c<0 : observer étalement ou contraction initiale.
3. Choisir la fente et réduire a ; comparer le premier zéro au produit d’écarts types du paquet.

**Sup.** diffraction, dimensions et ordres de grandeur quantiques.
**Spé et filières.** MP §6 et PC §6.5 : confinement et Heisenberg ; PC introduit le paquet d’ondes, MP le traite ici en prolongement.
**Prolongements.** Covariance, phase quadratique et estimation variationnelle de l’atome : approfondissements.
**Résultat attendu.** Une largeur de diffraction distinguée d’un écart type et une estimation d’énergie accompagnée de ses hypothèses.

### diffusion

Raccorder les fonctions d’onde, puis expliquer réflexion et transmission avec les courants de probabilité.

**Objets et unités.**

- E est l’énergie incidente, V₀ la hauteur du potentiel et a la largeur de barrière ; x est la position. m est la masse et ℏ la constante de Planck réduite ; les unités donnent ℏ=m=1.
- ψ est la fonction d’onde et ψ′ sa dérivée spatiale ; les raccordements portent sur ces deux fonctions.
- R et T sont les rapports de courants réfléchi et transmis à l’incident, sans dimension ; une amplitude de ψ ne suffit pas à donner T.

**Hypothèses.**

- Potentiel réel constant par morceaux, masse identique dans toutes les régions.
- Onde incidente depuis la gauche ; états stationnaires ; pas d’absorption.

**Techniques.** Résoudre une équation différentielle du second ordre.; Appliquer deux raccordements à chaque interface.; Vérifier la conservation R+T=1 et des cas limites.

**Première expérience.**

1. Comparer E<V₀ sur la marche et sur la barrière : prévoir T dans chaque cas.
2. Sur la barrière, augmenter a et suivre la diminution de T.
3. Choisir E>V₀ et rechercher une résonance de transmission, puis vérifier R+T.

**Sup.** raccordement d’ondes et conservation d’un flux.
**Spé et filières.** MP §6.3 et PC §6.5 : potentiels constants par morceaux et effet tunnel.
**Prolongements.** Paquets incidents, barrières multiples et temps de traversée : au-delà du modèle stationnaire.
**Résultat attendu.** Des coefficients définis par les courants et une explication de T=0 sur une marche malgré une densité à droite.

### oscillateur

Relier le spectre à ses états propres et comparer le mouvement moyen d’un état cohérent au mouvement classique.

**Objets et unités.**

- m est la masse, ω la pulsation et ℏ la constante de Planck réduite. ℓ=√(ℏ/(mω)) est une longueur ; X=x/ℓ est la position réduite et ωt le temps réduit.
- n≥0 compte les excitations ; α est l’amplitude complexe d’un état cohérent, réglée par son module et sa phase. L’énergie est mesurée en ℏω.
- ψ est la fonction d’onde, |ψ|² sa densité de probabilité ; Δx et Δp sont les écarts types de position et d’impulsion.

**Hypothèses.**

- Potentiel harmonique idéal ; état propre ou état cohérent normalisé.
- Aucun amortissement ni anharmonicité ; une densité spatiale n’est pas une trajectoire.

**Techniques.** Étudier parité et zéros des polynômes d’Hermite.; Calculer des moments et des commutateurs.; Comparer une équation sur les moyennes à l’équation classique.

**Première expérience.**

1. Comparer n=0,1,3 : compter les nœuds et prévoir les énergies.
2. Choisir un état cohérent et suivre un cycle en temps réduit.
3. Faire varier |α| : comparer déplacement moyen, largeur et énergie.

**Sup.** oscillateur classique, gaussienne et énergie minimale.
**Spé et filières.** Outils Spé : équations différentielles, Hermite et opérateurs ; résolution quantique comme prolongement de MP/PC.
**Prolongements.** États cohérents et construction complète par opérateurs : approfondissements guidés.
**Résultat attendu.** Une distinction entre état propre d’énergie et paquet oscillant, avec le rôle de l’énergie de point zéro.

### intrication

Comparer corrélations quantiques et classiques sans confondre probabilités conjointes et probabilités marginales.

**Objets et unités.**

- a,a′ règlent les orientations de l’analyseur A ; b,b′ celles de B, en degrés. Les résultats de chaque mesure sont ±1.
- v∈[0,1] est le poids de Bell dans le mélange avec le bruit blanc ; l’autre préparation est un mélange de polarisations horizontales et verticales.
- E(a,b) est la moyenne du produit des résultats ; S est la combinaison CHSH de quatre corrélations. Les probabilités marginales concernent un seul analyseur.

**Hypothèses.**

- Analyseurs de polarisation linéaire idéaux ; état de Bell Φ⁺ ou mélange HH/VV.
- La borne S≤2 concerne des modèles locaux à résultats prédéterminés ; le bruit est explicitement modélisé.

**Techniques.** Calculer des probabilités et leurs sommes marginales.; Changer de base de mesure.; Distinguer intrication et violation d’une inégalité avec des réglages donnés.

**Première expérience.**

1. Avec les angles optimaux et v=1, comparer S à 2.
2. Passer au mélange classique sans changer les angles.
3. Réduire v et comparer les deux seuils : intrication et violation CHSH.

**Sup.** probabilités conjointes, conditionnelles et corrélations.
**Spé et filières.** Outils Spé : matrices, produits tensoriels et valeurs propres ; ce sujet est un prolongement de MP/PC.
**Prolongements.** Tests de Bell, états mixtes et critères de séparabilité : au-delà du socle CPGE cité.
**Résultat attendu.** Une corrélation expliquée dans plusieurs bases et des probabilités locales indépendantes du réglage distant.

### josephson

Prévoir la fréquence d’une jonction sous tension et la modulation du courant critique d’une boucle à deux jonctions.

**Objets et unités.**

- I₁,I₂ sont les courants critiques en µA ; V est la tension en µV et δ la différence de phase en degrés.
- Φ est le flux dans la boucle et Φ₀=h/(2e) son quantum, en Wb ; h est la constante de Planck et e la charge élémentaire. Le curseur règle Φ/Φ₀.
- I_c(Φ) est le courant maximal du SQUID à flux fixé ; f_J est la fréquence du courant alternatif d’une jonction sous tension.

**Hypothèses.**

- Relations Josephson sinusoïdales ; deux jonctions idéales pour le SQUID.
- Inductance de boucle négligée ; la tension de sortie d’un appareil réel n’est pas modélisée.

**Techniques.** Résoudre une équation de phase.; Maximiser A sinδ+B cosδ.; Utiliser périodicité et symétrie pour prévoir des extrema.

**Première expérience.**

1. Choisir une jonction et comparer V=0 à V=1 µV.
2. Dans le SQUID symétrique, comparer flux 0 et 1/2.
3. Rendre I₁ et I₂ différents et prévoir le minimum résiduel.

**Sup.** sinusoïdes, phase, flux et unités.
**Spé et filières.** Outils Spé : interférences, dérivation et optimisation ; Josephson/SQUID sont des prolongements de MP/PC.
**Prolongements.** Supraconductivité macroscopique, polarisation et dissipation d’un SQUID réel.
**Résultat attendu.** Une modulation de période Φ₀ et un minimum lié à l’asymétrie des jonctions.

### rabi

Choisir une impulsion qui réalise une transition et expliquer la baisse de sa probabilité hors résonance.

**Objets et unités.**

- Ω est le couplage, Δ le désaccord et t le temps en unités réduites ; Ω_R=√(Ω²+Δ²) est la pulsation de Rabi.
- B₀ est le champ statique en T, B₁ l’amplitude circulaire en µT ; γ est le rapport gyromagnétique du proton. Ces réglages donnent des repères physiques séparés des curseurs réduits.
- P₁ est la probabilité du niveau |1⟩ et r le vecteur de Bloch ; l’état initial est |0⟩. Une impulsion π inverse les populations à résonance.

**Hypothèses.**

- Deux niveaux idéaux, état initial |0⟩ et champ circulaire dans le repère tournant.
- Pas de relaxation ; les curseurs réduits ne sont pas déduits automatiquement des champs RMN.

**Techniques.** Exponentier une matrice à l’aide des matrices de Pauli.; Lire amplitude, fréquence et phase d’une oscillation.; Relier durée d’impulsion et rotation.

**Première expérience.**

1. Choisir Δ=0 et l’impulsion π : prévoir P₁.
2. Choisir l’impulsion π/2 puis comparer populations et phase de l’état.
3. Augmenter |Δ| : suivre la baisse de l’amplitude maximale.

**Sup.** résonance, oscillations et ordres de grandeur de fréquences.
**Spé et filières.** Outils Spé : repère tournant et matrices ; les rotations quantiques sont un prolongement de MP/PC.
**Prolongements.** RMN avec relaxation, distributions de fréquences et impulsions façonnées.
**Résultat attendu.** Une durée de commande reliée au couplage, et un désaccord qui empêche une inversion complète.

### bloch

Représenter un état, une transformation et une mesure avec des vecteurs, puis relier géométrie et probabilités.

**Objets et unités.**

- θ est la colatitude et φ l’azimut, en degrés ; r∈[0,1] est la longueur du vecteur de Bloch. La pureté de l’état est (1+r²)/2.
- ρ est la matrice densité ; X,Y,Z sont les matrices de Pauli. Les portes Rx,Ry,Rz sont des rotations d’angle α en degrés.
- L’axe de mesure est défini par sa colatitude et son azimut ; les probabilités concernent les deux résultats ±1.

**Hypothèses.**

- Un seul qubit ; portes unitaires idéales et mesure projective.
- Un état pur est sur la sphère ; un état mélangé est à l’intérieur.

**Techniques.** Passer entre coordonnées sphériques et cartésiennes.; Appliquer une matrice unitaire.; Calculer une probabilité avec un produit scalaire.

**Première expérience.**

1. Comparer |0⟩ et |+⟩ avec une mesure suivant Z.
2. Appliquer Hadamard à |0⟩ puis tourner l’axe de mesure.
3. Prendre r=0 : vérifier que toutes les mesures donnent 1/2.

**Sup.** géométrie dans l’espace et probabilités.
**Spé et filières.** Outils Spé : matrices hermitiennes et rotations ; le qubit est un prolongement du socle MP/PC.
**Prolongements.** Canaux quantiques, décohérence et systèmes à plusieurs qubits.
**Résultat attendu.** Une probabilité calculée à partir de l’état et de l’axe, avec une pureté conservée par les portes.

### circuits

Suivre les amplitudes d’un circuit à deux qubits et expliquer pourquoi une itération de Grover retrouve la cible.

**Objets et unités.**

- Les quatre états de base sont |00⟩,|01⟩,|10⟩,|11⟩ ; le premier qubit est celui de gauche. Une amplitude complexe au carré en module donne une probabilité.
- H est la porte de Hadamard ; CNOT inverse la cible si le contrôle vaut 1. Une paire de Bell est une superposition intriquée de deux états.
- m=0,1,2,3 est l’indice de la cible marquée ; k est le nombre d’itérations de Grover. L’oracle inverse le signe de l’amplitude ciblée.

**Hypothèses.**

- Simulation exacte de deux qubits ; portes, oracle et mesure idéaux.
- Un élément marqué ; aucun bruit et aucune mesure intermédiaire.

**Techniques.** Multiplier des matrices dans l’ordre du circuit.; Conserver la somme des probabilités.; Interpréter une réflexion des amplitudes autour de leur moyenne.

**Première expérience.**

1. Préparer Bell et identifier les deux issues de mesure possibles.
2. Choisir Grover avec k=0 puis k=1 : comparer la probabilité de la cible.
3. Ajouter une seconde itération et expliquer pourquoi le succès diminue.

**Sup.** vecteurs, probabilités et composition d’opérations.
**Spé et filières.** Outils Spé : algèbre linéaire et produits tensoriels ; circuits quantiques hors du socle MP/PC.
**Prolongements.** Complexité en nombre de requêtes, construction d’un oracle et processeurs quantiques.
**Résultat attendu.** Des amplitudes suivies jusqu’à la mesure, sans assimiler une itération supplémentaire à un progrès garanti.

## Exercices corrigés

### 1 · Normaliser le cube

L est le côté en m ; m est la masse et ℏ la constante de Planck réduite. Normaliser sin(πx/L)sin(πy/L)sin(πz/L) dans le cube. Donner son énergie et ses unités.

**Correction.** Chaque intégrale de sin² vaut L/2. Le facteur de normalisation est donc √(8/L³). La fonction d’onde a l’unité m⁻³ᐟ². Le fondamental a E=3π²ℏ²/(2mL²). Pour un électron avec L=1 nm, E≈1,13 eV. Doubler L donne E/4.

### 2 · Dégénérescence : ce qu’on compte

E₀=π²ℏ²/(2mL²) est l’échelle d’énergie ; m est la masse et L le côté. Donner la dégénérescence spatiale des niveaux 6E₀ et 9E₀ aux parois. Que devient celle-ci si les trois longueurs sont différentes ?

**Correction.** 6=4+1+1 : trois permutations de (2,1,1), donc g=3. 9=4+4+1 : trois permutations de (2,2,1), donc g=3. On ne compte pas le spin. Pour des côtés Lx,Ly,Lz, E=π²ℏ²(nx²/Lx²+ny²/Ly²+nz²/Lz²)/(2m). Des longueurs différentes lèvent en général les dégénérescences de permutation ; des coïncidences accidentelles restent possibles.

### 3 · Parois ou périodicité ?

Pourquoi ne pas imposer ψ′(0)=ψ′(L) dans le puits infini ? Comparer le fondamental avec le problème périodique.

**Correction.** Pour sin(nπx/L), ψ′(L)=(−1)ⁿψ′(0). L’égalité éliminerait les n impairs, dont n=1 : elle ne fait pas partie des conditions du puits infini. Une normalisation périodique admet ψ=L⁻³ᐟ², d’énergie 0. Ce n’est pas le même problème physique que des parois de potentiel infini.

### 4 · Une densité qui bat, une énergie constante

Les triplets sont les indices des deux modes ; E₀=π²ℏ²/(2mL²). Dans la boîte aux parois, superposer à poids égaux (1,1,1) et (2,1,1). Donner l’énergie moyenne et la période de la densité.

**Correction.** Les énergies valent 3E₀ et 6E₀. L’énergie moyenne est 9E₀/2, indépendante du temps. Le terme croisé oscille à 3E₀/ℏ : T=2πℏ/(3E₀), soit 2π/3 en temps réduit τ. Le terme croisé s’annule après intégration sur tout le cube, ce qui conserve la normalisation.

### 5 · Une gaussienne minimale

σ est une longueur, p₀ l’impulsion moyenne et ℏ la constante de Planck réduite. Pour ψ=(2πσ²)⁻¹ᐟ⁴exp[−x²/(4σ²)+ip₀x/ℏ], calculer les deux écarts types et leur produit.

**Correction.** |ψ|² est une gaussienne de variance σ². La transformée de Fourier est une gaussienne centrée en p₀, de variance ℏ²/(4σ²). Donc Δx=σ, Δp=ℏ/(2σ), et ΔxΔp=ℏ/2. p₀ déplace la moyenne sans changer les dispersions. Une phase quadratique non nulle ajoute une covariance et augmente généralement ce produit.

### 6 · La largeur d’une fente est-elle un écart type ?

θ est l’angle à la normale et λ la longueur d’onde. Une fente rectangulaire de largeur a produit [sin u/u]², avec u=πa sinθ/λ et la limite 1 en u=0. Donner l’échelle du premier zéro et expliquer pourquoi Δp≈ℏ/a n’est pas ici un calcul exact d’écart type.

**Correction.** Le premier zéro vérifie |sinθ|=λ/a. Aux petits angles θ≈λ/a, si ce rapport est petit. La densité d’impulsion du profil rectangulaire possède une enveloppe en 1/p² : l’intégrale de p²|ψ̃(p)|² diverge. Δp est donc infini pour cette fente idéale. La largeur du lobe central est un indicateur différent ; une ouverture gaussienne permet un calcul d’écarts types finis.

### 7 · Heisenberg donne exactement le fondamental harmonique

m est la masse, ω la pulsation et u=(Δx)² la variance de position. Minimiser ℏ²/(8mu)+mω²u/2, u>0. Quand la borne sur l’énergie est-elle atteinte ?

**Correction.** La dérivée vaut −ℏ²/(8mu²)+mω²/2. Elle s’annule en u=ℏ/(2mω), et la valeur est ℏω/2. Pour atteindre la borne, les moyennes x et p doivent être nulles et l’inégalité d’Heisenberg saturée avec la largeur optimale. La gaussienne du fondamental satisfait ces conditions ; ici la borne est exacte.

### 8 · Hydrogène : ordre de grandeur et preuve

m est la masse de l’électron, e la charge élémentaire et ε₀ la permittivité du vide. Minimiser E(r)=ℏ²/(2mr²)−C/r, avec C=e²/(4πε₀). Peut-on appeler r* la moyenne radiale exacte du fondamental ?

**Correction.** E′=−ℏ²/(mr³)+C/r² donne r*=ℏ²/(mC)=a₀ et E*=−mC²/(2ℏ²). La relation p∼ℏ/r est une estimation : elle ne transforme pas cette minimisation en preuve issue de Heisenberg. Dans le fondamental coulombien exact, ψ∝e^{-r/a₀} et ⟨r⟩=3a₀/2. Le paramètre a₀ est l’échelle de décroissance, non cette moyenne. Une preuve variationnelle explicite avec ψ_a distingue correctement les deux démarches.

### 9 · La transmission n’est pas |t|²

E est l’énergie incidente ; r,t sont les amplitudes réfléchie et transmise, R,T les rapports de courants. Une marche vérifie V₀=3E/4. Calculer r, t, R et T pour une onde incidente d’amplitude 1.

**Correction.** k₂=k₁/2. Les raccordements donnent r=1/3 et t=4/3. R=1/9. Le courant transmis donne T=(k₂/k₁)|t|²=(1/2)(16/9)=8/9. R+T=1 ; |t|²=16/9 n’est pas une probabilité de transmission.

### 10 · Évanescent ne veut pas dire transmis

E est l’énergie incidente, V₀ la hauteur de marche et ψ la fonction d’onde. Pourquoi une marche semi-infinie avec E<V₀ peut-elle avoir |ψ|² non nul à droite tout en ayant T=0 ?

**Correction.** La solution bornée à droite est Ce^{-κx}. Sa dérivée est −κ fois elle-même, donc ψ*ψ′ est réel et j=(ℏ/m)Im(ψ*ψ′)=0. Il existe une pénétration de la densité, mais aucun flux net vers +∞. La conservation du courant impose R=1. Une barrière finie est différente, car les deux exponentielles sont présentes et un courant transmis peut exister après elle.

### 11 · Tunnel : un cas simplifié

E est l’énergie incidente, a la largeur et κ=√(2m(V₀−E))/ℏ le taux de décroissance. Pour une barrière V₀=2E, simplifier T et déterminer son comportement lorsque κa est grand.

**Correction.** V₀²/[4E(V₀−E)]=1, donc T=1/(1+sinh²κa)=sech²κa. Pour κa≫1, coshκa≈e^{κa}/2 et T≈4e^{-2κa}. La formule exponentielle est asymptotique : à a=0 elle donnerait 4, alors que la formule exacte donne 1.

### 12 · Au-dessus de la barrière

Dans les unités ℏ=m=1, avec V₀=1 et a=π/2, trouver la première énergie E>V₀ de transmission parfaite. Donner aussi la limite de T en E=V₀.

**Correction.** Il faut qa=π, q=√[2(E−V₀)]. Avec a=π/2, q=2, d’où E=3. À E=V₀, sin²(qa)/(E−V₀) tend vers 2ma²/ℏ². Donc T=[1+mV₀a²/(2ℏ²)]^{-1}, ici [1+π²/8]^{-1}. La transmission n’est pas forcément nulle ou parfaite à ce seuil.

### 13 · Construire le premier état excité

ψ₀ est le fondamental ; a† élève d’un niveau, E₁ est l’énergie du premier excité et Δx,Δp sont les écarts types. À partir de ψ₀, utiliser a† pour obtenir ψ₁ et donner E₁, la parité et ΔxΔp.

**Correction.** Avec u=x/ℓ, a†=(u−∂u)/√2. Sur e^{-u²/2}, a† donne √2u fois le même profil : ψ₁=√2(x/ℓ)ψ₀. Son énergie est 3ℏω/2 et sa parité impaire. Δx=ℓ√(3/2), Δp=√(mℏω)√(3/2), donc ΔxΔp=3ℏ/2, supérieur à la borne minimale.

### 14 · Un état qui suit le mouvement classique

α définit l’état cohérent, ω la pulsation, m la masse et ℓ=√(ℏ/(mω)) la longueur de l’oscillateur. Pour un état cohérent α(0)=2 réel, donner ⟨x(t)⟩, ⟨p(t)⟩, l’énergie et la variance du nombre d’excitations.

**Correction.** α(t)=2e^{-iωt}. Donc ⟨x⟩=2√2ℓcosωt et ⟨p⟩=−2√(2mℏω)sinωt. L’énergie moyenne vaut (4+1/2)ℏω. La distribution de n est de Poisson de moyenne 4 et de variance 4. Les dispersions x et p restent celles du fondamental. Ce n’est pas un état stationnaire d’énergie.

### 15 · Même corrélation, états différents

Φ⁺=(|00⟩+|11⟩)/√2 ; X,Z sont les matrices de Pauli. Comparer Φ⁺ et ρ_classique=(|00><00|+|11><11|)/2 après mesure en Z, puis en X sur les deux qubits.

**Correction.** En Z, les deux états donnent 00 ou 11 à probabilités 1/2. En X, Φ⁺=(|++>+|-->)/√2 : mêmes résultats à probabilités 1/2 et corrélation +1. Pour ρ_classique, chaque composante 00 ou 11 donne quatre couples X équiprobables ; la corrélation est 0. Une seule base de mesure ne suffit donc pas à distinguer cette intrication d’une corrélation classique.

### 16 · Le calcul de CHSH

S=E(a,b)+E(a,b′)+E(a′,b)−E(a′,b′), où E est la corrélation de résultats ±1 ; v est le poids de Bell. Pour Φ⁺, prendre a=0°, a′=45°, b=22,5°, b′=−22,5°. Calculer S. Que devient S pour v=0,6 dans la famille de Werner ?

**Correction.** Les trois premiers termes E valent √2/2 et le quatrième −√2/2. Donc S=2√2. Pour Werner, chaque corrélation est multipliée par v : à v=0,6, S=1,2√2≈1,697<2. Pourtant cette famille est intriquée pour v>1/3. Absence de violation de CHSH ne signifie pas absence d’intrication.

### 17 · Une fréquence Josephson

V est la tension et δ₀ la phase initiale ; le quantum de charge est 2e. Une jonction idéale est maintenue à 2 µV. Calculer la fréquence du courant et expliquer ce qui se passe si V=0 mais δ₀=π/6.

**Correction.** f_J=2e|V|/h≈967,2 MHz. Le courant vaut I_csin(δ₀+2eVt/ℏ). À V=0, la phase est constante et I=I_c/2, un supercourant continu. I_c ne devient pas I_cδ₀ : c’est le courant qui se linéarise en I_cδ₀ pour une petite phase.

### 18 · Pourquoi les deux jonctions doivent-elles se ressembler ?

I₁,I₂ sont les courants critiques des jonctions ; Φ₀=h/(2e) est le quantum de flux. Un SQUID idéal possède I₁=12 µA et I₂=8 µA. Donner les maxima et minima du courant critique, ainsi que leur flux.

**Correction.** I_eff=√[I₁²+I₂²+2I₁I₂cos(2πΦ/Φ₀)]. Aux entiers Φ/Φ₀, le maximum vaut I₁+I₂=20 µA. Aux demi-entiers, le minimum vaut |I₁−I₂|=4 µA. Il ne s’annule pas. Une boucle d’inductance négligeable et des relations sinusoïdales sont les hypothèses de cette formule.

### 19 · Pourquoi ℏω₀I ne décrit pas la RMN

I est l’identité 2×2, ω₀ une pulsation et H₀ l’opérateur énergie. Montrer qu’un Hamiltonien H₀=ℏω₀I ne produit aucun écart entre les deux niveaux. Quel Hamiltonien utiliser pour une séparation ℏω₀ ?

**Correction.** L’évolution est U=e^{-iω₀t}I : chaque amplitude reçoit la même phase globale. Les deux valeurs propres sont égales, donc il n’existe aucune pulsation de transition ω₀. Dans une base où l’ordre des niveaux est explicite, prendre H₀=(ℏω₀/2)Z, de valeurs propres ±ℏω₀/2. En RMN physique, H_Z=−γS·B fixe l’ordre par le signe de γ et la base.

### 20 · Impulsions π et π/2

Ω est le couplage et Δ le désaccord dans le repère tournant. À résonance, avec Ω=1 en unités réduites, donner l’état après t=π/2 puis t=π, en partant de |0>. Que change un désaccord Δ=Ω ?

**Correction.** U=cos(t/2)I−isin(t/2)X. À π/2 : (|0>−i|1>)/√2 ; à π : −i|1>, équivalent à |1> à phase globale près. Si Δ=Ω, la probabilité maximale est 1/2 et la pulsation √2Ω : aucune durée n’inverse totalement la population dans ce modèle constant.

### 21 · Deux amplitudes de champ, deux durées

γ/(2π)≈42,577 MHz·T⁻¹ pour le proton ; f_L est sa fréquence de Larmor et t_π la durée d’une impulsion π. Pour un proton, B₀=1 T et B₁=10 µT circulaire, estimer f_L et t_π. Comparer à un champ linéaire de même amplitude crête.

**Correction.** f_L≈42,58 MHz. Ω=|γ|B₁≈2π×425,8 rad/s, donc t_π=π/Ω≈1,17 ms. Un champ linéaire de même amplitude crête contient une composante co-rotative de 5 µT : dans l’approximation tournante, Ω est divisé par 2 et t_π≈2,35 ms. Toujours préciser si B₁ est l’amplitude circulaire ou l’amplitude crête linéaire.

### 22 · La phase qu’une mesure Z ne voit pas

X,Y,Z sont les matrices de Pauli et i²=−1. Comparer |+>=(|0>+|1>)/√2 et |+i>=(|0>+i|1>)/√2 en mesures Z, X et Y.

**Correction.** Les deux donnent P_Z(0)=P_Z(1)=1/2. Le vecteur de Bloch de |+> est (1,0,0) : X donne +1 sûrement et Y donne ±1 équiprobables. Celui de |+i> est (0,1,0) : Y donne +1 sûrement et X donne ±1 équiprobables. Une phase relative est observable après choix d’une base adaptée ; une phase globale ne l’est pas.

### 23 · Préparer Bell avec deux portes

H est la porte de Hadamard ; CNOT inverse le second qubit si le premier vaut 1. Appliquer H sur le premier qubit de |00>, puis CNOT. Pourquoi mesurer entre les deux opérations change-t-il l’état préparé ?

**Correction.** H⊗I produit (|00>+|10>)/√2, puis CNOT produit (|00>+|11>)/√2. Une mesure Z du premier qubit entre les portes, dont on oublie le résultat, prépare un mélange de 00 et 10. CNOT le transforme en mélange de 00 et 11 : mêmes probabilités Z que Bell, mais cohérences nulles et corrélation XX nulle.

### 24 · Grover : une itération suffit, deux nuisent

N est le nombre d’états de base ; l’oracle inverse le signe de l’amplitude de l’état marqué. Pour N=4 et un état marqué, calculer les amplitudes après une itération de Grover, puis la probabilité de succès après deux itérations.

**Correction.** Au départ toutes les amplitudes valent 1/2. L’oracle rend l’amplitude marquée −1/2 ; la moyenne devient 1/4. Le diffuseur a→2×1/4−a donne 1 pour l’état marqué et 0 pour les trois autres. Après deux itérations, P=sin²(5π/6)=1/4 : continuer fait dépasser la cible. Le gain concerne les appels cohérents à l’oracle, qui est ici explicitement simulé.

## Sources et conventions

Recueil de A. R., extrait MemoCPGEScientifAR2027-PQ.pdf, pages imprimées 471–479 : introduction, TP de boîte cubique, incertitude et intrication, exercices de marche, tunnel, Josephson et RMN. Le PDF personnel n’est pas inclus dans le dépôt.

Leçons, preuves, corrigés et illustrations rédigés pour ce volet. L’oscillateur harmonique est approfondi ; la sphère de Bloch, CHSH, le SQUID idéal et les circuits Bell/Grover sont des extensions guidées, à distinguer des attendus communs aux différentes filières CPGE.

Référence complémentaire : MIT OpenCourseWare, 8.04 Quantum Physics I, notes 11 sur le puits : https://www.ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/a565b327f85c7721b18f1074dbd69ede_MIT8_04S16_LecNotes11.pdf ; notes 16 sur la marche : https://www.ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/2cfb1c11b0f9093bb8b452c5cebf24dd_MIT8_04S16_LecNotes16.pdf .

Référence complémentaire : MIT OpenCourseWare, 8.04, notes 14–15 sur l’oscillateur harmonique : https://www.ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/3b4ee73bda5abd93cbb2a89ae9b6765b_MIT8_04S16_LecNotes14_15.pdf ; 6.763 Applied Superconductivity, cours 12 sur le SQUID : https://www.ocw.mit.edu/courses/6-763-applied-superconductivity-fall-2005/c485ff655dd6168e0614445848899583_lecture12.pdf .

Constantes physiques : NIST, valeurs recommandées CODATA 2022, tableau officiel : https://physics.nist.gov/cuu/Constants/Table/allascii.txt . Les exemples numériques emploient le proton non blindé, γp/(2π)=42,577478461 MHz/T ; cette constante ne modélise pas les déplacements chimiques d’une RMN réelle.

Références complémentaires : IBM Quantum, bits, portes et sphère de Bloch : https://quantum.cloud.ibm.com/learning/en/courses/utility-scale-quantum-computing/bits-gates-and-circuits ; définition de RX : https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.RXGate ; test CHSH : https://quantum.cloud.ibm.com/docs/en/tutorials/chsh-inequality .

Référence complémentaire : IBM Quantum, analyse de l’algorithme de Grover : https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/analysis . Le présent laboratoire travaille exactement sur quatre états et un seul élément marqué.

Conventions : unités SI pour les exemples physiques déclarés ; ℏ=m=1 pour la diffusion ; ℏ=m=ω=1 pour l’oscillateur. Angles des curseurs en degrés, angles des formules en radians. Pour la boîte τ=E₀t/ℏ, avec E₀ dépendant des conditions de bord. Le mélange w du TP de boîte est un poids dans une superposition cohérente.

Conventions d’intrication : Φ⁺=(|00>+|11>)/√2 ; analyseurs de polarisation M(a)=cos(2a)Z+sin(2a)X ; CHSH avec les signes +,+,+,−. Matrices de qubits dans l’ordre |0>,|1> ; deux qubits dans l’ordre |00>,|01>,|10>,|11>, contrôle CNOT à gauche.

Limites des modèles : fente rectangulaire traitée par largeur de lobe, et non par variance finie ; hydrogène heuristique distingué d’une démonstration variationnelle ; SQUID sans inductance ni dissipation ; Rabi sans relaxation ; champ circulaire exact distingué de l’approximation tournante d’un champ linéaire ; circuits simulés sur ordinateur classique.
