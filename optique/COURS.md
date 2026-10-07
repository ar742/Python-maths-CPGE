# Optique — lumière, images et expériences

36 leçons, 24 laboratoires et 48 exercices corrigés. Dix missions transversales se trouvent dans [PARCOURS.md](PARCOURS.md).

Les ateliers réinvestissent les TP et les problèmes de l’extrait Optique du recueil : lentilles, Bessel, lunette, microscope, prisme/goniomètre, Michelson et polarisation ; fibres, mirages, arc-en-ciel, Young, doublet, diffraction, apodisation, réseau, Fabry–Perot et génération non linéaire. Les figures et textes de l’application sont originaux.

Les mentions Sup, Spé et Au-delà indiquent des outils et une progression, avec un statut dépendant de la filière. La conjugaison de Gauss et la mesure sur banc fournissent les entrées Sup. Diffraction, interférences, Michelson et polarisation ne sont pas à attribuer indistinctement à tous les programmes. Jones/Poincaré, ABCD de résonateur, filtrage 4f complet, gain saturé et conversion χ² sont des prolongements accompagnés ; les liens officiels de programmes sont regroupés en fin de document.

Conventions : axe de lentille orienté vers la propagation, p<0 pour un objet réel ; λ₀ est dans le vide, la longueur d’onde de milieu vaut λ₀/n ; sinc u=sin(u)/u et sinc 0=1. Les tableaux Jones utilisent Re[Ẽ exp(−iωt)] et S₃=2Im(Ex*Ey). Les matrices de rayons réduits utilisent (y,nθ) ; le paramètre gaussien q associé à (y,θ) est réduit en q/n pour ces mêmes matrices. Les variables, unités et domaines sont repris au début de chaque expérience.

## 1. Du front d’onde au rayon réfracté

*Sup* — laboratoire `snell`.

**Cadre.** Un rayon est la trajectoire géométrique associée à une propagation locale. Cette limite demande une longueur d’onde petite devant les échelles de variation du milieu et des obstacles. Dans un milieu isotrope transparent d’indice n, la vitesse de phase est c/n ; λ₀ désigne ici la longueur d’onde dans le vide, λ=λ₀/n celle du milieu.

n₁ sin i=n₂ sin r ; angle réfléchi=i  
λ₂=λ₀/n₂ ; ν₂=ν₁ ; n₁>n₂ ⇒ ic=arcsin(n₂/n₁)

**Construction.** Mesurer les angles depuis la normale, et non depuis la surface. L’invariance de la phase le long de l’interface conserve la composante tangentielle du vecteur d’onde : k₁ sin i=k₂ sin r. La fréquence demeure la même à une interface immobile. Cette démonstration relie géométrie et électromagnétisme.

**Exemple.** Depuis l’air vers le verre n₂=1,50 à i=45°, r=arcsin(sin45°/1,50)≈28,13°. Dans le sens verre→air, l’angle critique vaut 41,81°. Au-delà il n’existe pas de rayon réfracté propagatif dans l’air, mais un champ évanescent subsiste.

**Technique.** Avant d’appliquer arcsin, vérifier que son argument est compris entre −1 et 1. Tester n₁=n₂, i=0 et la réversibilité donne trois contrôles qui détectent une erreur d’angle ou d’indice.

## 2. Fresnel : un rayon ne transporte pas toujours toute la puissance

*Spé ; prolongement selon filière* — laboratoire `snell`.

**Objets.** À une interface diélectrique non magnétique, le champ électrique s est perpendiculaire au plan d’incidence ; p lui appartient. Les amplitudes de champ et les puissances ont des coefficients différents. Les indices réels positifs et les angles sous le seuil critique définissent ici des milieux sans absorption.

rs=(n₁ cos i−n₂ cos r)/(n₁ cos i+n₂ cos r)  
rp=(n₂ cos i−n₁ cos r)/(n₂ cos i+n₁ cos r)  
R=|r|² ; T=(n₂ cos r)/(n₁ cos i)|t|² ; R+T=1

**Dérivation.** La continuité des champs tangentiels E et H fournit deux équations linéaires. Pour convertir une amplitude transmise en puissance, intégrer le flux normal de Poynting : le facteur n cos(angle) est indispensable. Une convention de base p peut inverser le signe de rp sans changer R.

**Brewster.** Pour p, rp=0 lorsque tan iB=n₂/n₁. Avec n₂/n₁=1,50, iB≈56,31°. Le rayon réfléchi s demeure présent. À incidence normale R=[(n₁−n₂)/(n₁+n₂)]²=4 % pour air/verre ; une plaque à deux faces perd davantage si leurs réflexions sont traitées séparément.

**Lien au TP.** Comparer s et p au goniomètre permet d’identifier une polarisation et de séparer déviation, réflexion et transmission. Le modèle de rayon seul ne décrit ni l’onde évanescente ni les décalages latéraux au voisinage d’une réflexion totale.

## 3. Lentille mince : annoncer les distances orientées

*Sup* — laboratoire `lentille`.

**Convention.** L’axe x est orienté dans le sens de propagation, O est le centre de la lentille, p=OA et p′=OA′ sont algébriques. Un objet réel à gauche donne p<0. Une lentille convergente dans l’air a f′>0 et une divergente f′<0. Un trait pointillé représente un prolongement, pas un rayon transportant de l’énergie.

1/p′−1/p=1/f′ ; p′=f′p/(p+f′)  
γ=A′B′/AB=p′/p ; C=1/f′ en m⁻¹

**Construction.** Un rayon passant par O garde sa direction dans le modèle mince ; un rayon parallèle à l’axe sort par F′ ou semble provenir de F′ ; un rayon passant par F sort parallèlement à l’axe. Les deux premiers suffisent à déterminer l’image, le troisième contrôle le dessin.

**Exemple.** f′=100 mm et p=−300 mm donnent p′=150 mm et γ=−0,50. Avec p=−50 mm, p′=−100 mm et γ=2 : l’image virtuelle est droite et agrandie. Pour p=−f′ l’image est à l’infini ; aucune position finie d’écran ne peut la recueillir.

**Validité.** Conjugaison et grandissement supposent le régime paraxial de Gauss. Agrandir le diaphragme ne modifie pas cette formule idéale, mais modifie lumière collectée, diffraction et aberrations réelles. Les laboratoires correspondants explorent ces effets séparément.

## 4. Newton et ABCD : composer les systèmes sans refaire tous les rayons

*Sup → Spé* — laboratoire `lentille`.

**Deux écritures.** Dans l’air, f=OF=−f′ et les distances depuis les foyers sont FA=p−f, F′A′=p′−f′. Pour les matrices paraxiales, le vecteur utilisé ici est (y, u) avec u=nθ, θ en radians. Cette coordonnée réduite évite de confondre une translation dans le verre avec une translation dans l’air.

FA·F′A′=ff′=−f′²  
T(d, n)=[[1, d/n],[0,1]] ; L(C)=[[1,0],[−C,1]]  
(y₂, u₂)ᵀ=M(y₁, u₁)ᵀ ; det M=1

**Calcul.** Les matrices agissent de droite à gauche dans l’ordre de traversée. Entre un plan objet et un plan image, M=T(d₂,1)L(1/f′)T(d₁,1). La condition d’image est B=0 : tous les rayons de même hauteur objet donnent la même hauteur image indépendamment de leur pente initiale.

**Invariant.** Le déterminant unité exprime la conservation du produit symplectique y₁u₂−y₂u₁ entre deux rayons paraxiaux. Avec le vecteur (y, θ), le déterminant entre deux indices différents devient nentrée/nsortie : le choix des coordonnées doit donc précéder une assertion sur le déterminant.

**Exemple.** Deux lentilles de vergences C₁, C₂ séparées par d dans l’air ont Céquiv=C₁+C₂−dC₁C₂. C₁=10 δ, C₂=5 δ, d=0,10 m donnent Céquiv=10 δ, et non 15 δ. Les plans principaux se déplacent : la focale équivalente seule ne donne pas la position du foyer depuis chaque lentille.

## 5. Bessel et Silbermann : déterminer une focale sans localiser son centre

*Sup ; TP* — laboratoire `bessel`.

**Montage.** Un objet et un écran sont séparés d’une distance D>0 fixe. Une lentille convergente mince se déplace entre eux. Noter x la distance positive objet→lentille, y=D−x la distance lentille→écran. Le grandissement algébrique est γ=−y/x.

1/x+1/(D−x)=1/f′  
x²−Dx+Df′=0 ; x±=(D±√(D²−4Df′))/2  
d=x+−x− ; f′=(D²−d²)/(4D)

**Seuil.** Deux positions nettes existent pour D>4f′ ; elles se confondent pour D=4f′, cas de Silbermann avec γ=−1. Pour D<4f′, l’absence de mise au point sur cet écran est une conséquence de la géométrie et ne prouve pas que la lentille est divergente.

**Exemple.** D=800 mm, d=400 mm donnent f′=150 mm ; les positions depuis l’objet sont x=200 et 600 mm. Les grandissements sont −3 et −1/3 : leur produit vaut 1, ce qui offre un contrôle indépendant par mesure des tailles.

**Méthode.** Faire la netteté sur les mêmes détails fins, repérer les deux positions en approchant de chaque côté et estimer la largeur de la zone de netteté. Un diaphragme facilite parfois ce repérage mais augmente la profondeur de champ et peut rendre la position optimale moins précise.

## 6. Bessel : propager l’incertitude et choisir D

*Sup → Spé ; TP* — laboratoire `bessel`.

**Grandeurs mesurées.** D et d sont des distances positives obtenues par des différences de positions sur le banc. Leurs incertitudes standards peuvent être corrélées si les mêmes lectures interviennent. Le laboratoire illustre l’effet d’un réglage ; l’analyse d’incertitude ci-dessous complète un compte rendu de TP.

f′=D/4−d²/(4D)  
∂f′/∂D=1/4+d²/(4D²) ; ∂f′/∂d=−d/(2D)  
u(f′)²=fD²u(D)²+fd²u(d)²+2fDfd cov(D, d)

**Exemple.** D=800 mm, d=400 mm, u(D)=u(d)=1 mm et indépendance donnent fD=0,3125, fd=−0,25 et u(f′)≈0,400 mm. On rapporte f′=(150,0±0,4) mm avec l’incertitude standard explicitée, sans annoncer artificiellement plusieurs décimales.

**Choix expérimental.** Près de D=4f′, les positions fusionnent : la faible sensibilité algébrique à d ne signifie pas que d est facile à mesurer. Très loin du seuil, une image est petite et moins facile à observer. La qualité de netteté et la longueur du banc comptent autant que les dérivées.

**Prolongement.** Une simulation Monte-Carlo des lectures de positions teste l’approximation linéaire et traite une corrélation. L’incertitude du modèle mince, liée à l’épaisseur ou aux aberrations, ne se réduit pas en répétant indéfiniment les mêmes lectures.

## 7. Lunette astronomique : grossissement et afocalité

*Sup ; TP* — laboratoire `telescope`.

**Système.** La lunette de Kepler comporte un objectif convergent de focale fo et un oculaire convergent de focale fe. Un objet astronomique est décrit par son angle α, non par une hauteur finie placée arbitrairement sur le banc. Quand F′objectif=Foculaire, la sortie est parallèle et l’œil observe sans accommodation.

d=fo+fe ; α′=−(fo/fe)α ; G=α′/α=−fo/fe  
himage≈fo α ; Dsortie=Dobjectif/|G|

**Dérivation.** L’objectif transforme l’angle α en une hauteur intermédiaire foα. L’oculaire transforme cette hauteur en un angle opposé, −h/fe. Le grossissement négatif indique une image renversée. Une lunette de Galilée emploie un oculaire divergent : son grossissement est positif et son écartement fo−|fe|.

**Exemple.** fo=1000 mm, fe=25 mm donnent G=−40 et d=1025 mm. Un détail de diamètre angulaire 1 minute d’arc devient apparent sous environ 40 minutes d’arc, soit 0,667°, dans l’approximation paraxiale. Un objectif de 80 mm donne une pupille de sortie de 2 mm.

**TP.** Régler d’abord l’oculaire sur le réticule, puis l’objectif sur un objet à l’infini. Le changement d’écartement dégrade l’afocalité : augmenter le grossissement affiché ne compense pas une mise au point incorrecte ni une pupille trop petite.

## 8. De la Lune à l’étoile double : grossir, résoudre, échantillonner

*Sup → Spé* — laboratoire `telescope`.

**Trois critères.** Le grossissement change la taille angulaire apparente ; le diamètre collecteur change diffraction et flux ; le pixel du détecteur échantillonne l’image. Ces trois fonctions sont distinctes. Un télescope réfléchissant évite la dispersion d’une lentille principale mais conserve diffraction et aberrations géométriques.

θRayleigh≈1,22 λ₀/D ; séparation image=f θ  
champ par pixel≈p/f ; collecte ∝D²

**Exemple.** À λ₀=550 nm et D=0,20 m, θRayleigh≈3,355 μrad≈0,692 seconde d’arc. Avec f=2 m, la séparation correspondante vaut 6,71 μm au foyer. Un pixel de 10 μm sous-échantillonne cette échelle ; un pixel de 3 μm la représente avec plusieurs échantillons.

**Observation réelle.** La turbulence atmosphérique peut dominer la limite de diffraction ; une obstruction centrale redistribue la lumière dans les anneaux ; des sources de luminosités très différentes ne suivent pas exactement le critère simple de deux points égaux. Les expériences de résolution utilisent donc des hypothèses annoncées.

**Bilan de chaîne.** Doubler fo avec le même diamètre double les tailles au foyer et change l’échantillonnage, mais ne divise pas l’angle de Rayleigh par deux. Pour gagner réellement une résolution angulaire dans ce modèle, augmenter D ou diminuer λ₀.

## 9. Microscope : image intermédiaire et puissance

*Sup ; TP* — laboratoire `microscope`.

**Montage.** L’objectif forme une image réelle agrandie d’un objet proche de son foyer objet. L’oculaire agit comme une loupe de cette image. On note Δ=F′objectif Foculaire l’intervalle optique et d₀=250 mm la distance conventionnelle de comparaison à l’œil nu.

γobjectif≈−Δ/fo ; Goculaire≈d₀/fe  
Gcommercial≈−Δd₀/(fo fe) ; P=α′/AB≈−Δ/(fo fe)

**Signe et unités.** La puissance P est en m⁻¹ car elle divise un angle sans dimension par une taille objet ; le grossissement commercial G est sans dimension. Une expression positive décrit souvent la valeur absolue : le microscope afocal produit ici une image renversée.

**Exemple.** Δ=160 mm, fo=4 mm et fe=25 mm donnent γobjectif≈−40, Goculaire≈10 et G≈−400. Un détail de 5 μm devient une hauteur intermédiaire de 0,20 mm puis un angle de 8 mrad, contre 20 μrad à l’œil nu à 25 cm.

**TP.** Placer l’image intermédiaire dans le plan focal objet de l’oculaire demande un réglage de netteté de l’objectif. Le modèle paraxial aide à comprendre la chaîne ; les objectifs à forte ouverture et les microscopes corrigés à l’infini demandent une description plus complète de la pupille et des lentilles de tube.

## 10. Ouverture numérique : compter la résolution utile

*Spé ; prolongement instrumentation* — laboratoire `microscope`.

**Définition.** L’ouverture numérique NA=n sin u associe l’indice côté objet et le demi-angle du cône collecté. Elle décrit une capacité à collecter des directions et à transmettre des fréquences spatiales. Un fort grossissement avec une faible NA agrandit surtout un flou.

dRayleigh≈0,61 λ₀/NA ; dAbbe≈λ₀/(2NA)  
ordre de grandeur axial : profondeur≈nλ₀/NA²

**Critères.** 0,61 et 1/2 correspondent à des questions différentes : séparation de points incohérents avec un critère de Rayleigh ou limite de transmission de détails périodiques selon illumination. Ne pas présenter les deux nombres comme deux mesures incompatibles d’une unique grandeur universelle.

**Exemple.** À 550 nm, NA=0,25 donne dRayleigh≈1,34 μm ; NA=1,25 donne environ 0,268 μm. La seconde valeur requiert un milieu d’immersion, puisque dans l’air NA≤1. Pour un grossissement objectif de 40, un pixel de 6,5 μm représente 0,1625 μm côté objet.

**Technique.** Ramener toutes les longueurs du détecteur au plan objet, puis comparer taille de pixel, tache et détail demandé. Une formule de résolution ne remplace pas le bilan de contraste, d’éclairement, d’aberration et de bruit d’une observation biologique ou physique.

## 11. Œil réduit, accommodation et corrections

*Sup* — laboratoire `oeil`.

**Modèle.** Un œil réduit est une lentille convergente réglable suivie d’une rétine à distance fixe ℓ. Le modèle utilise ici un espace image assimilé à l’air pour isoler la conjugaison ; sa vergence effective ne représente pas directement toutes les surfaces de l’œil anatomique. L’objet est à distance positive s devant l’œil.

Crequise=1/ℓ+1/s ; pour l’infini Crequise=1/ℓ  
Ccorrection≈1/ℓ−Cœil, relaxé ; addition de vergences pour lentilles en contact

**Exemple.** ℓ=17 mm demande 58,82 δ pour l’infini et 62,82 δ pour un objet à 25 cm : l’accommodation supplémentaire vaut 4 δ. Un œil trop convergent de 2 δ se corrige dans ce modèle par −2 δ ; une accommodation limitée rend la lecture proche difficile.

**Image.** L’image rétinienne est réelle et renversée. Un objet de 10 mm à 1 m produit approximativement une hauteur de −0,17 mm. Le diaphragme pupillaire réduit le flou de défocalisation quand il se ferme, mais augmente la diffraction ; le diamètre optimal résulte d’un compromis.

**Interprétation.** Myopie, hypermétropie et presbytie correspondent ici à des modifications distinctes de convergence, géométrie ou plage d’accommodation. Le modèle sert à apprendre la conjugaison et ses ordres de grandeur ; il ne calcule pas une prescription individuelle.

## 12. Fibre à saut d’indice : du rayon guidé au cône d’entrée

*Sup → Spé* — laboratoire `fibre`.

**Géométrie.** Le cœur a un indice n₁ supérieur à celui de la gaine n₂. Un rayon méridien fait l’angle θ avec l’axe et atteint la paroi sous l’incidence i=π/2−θ. À la face d’entrée normale à l’axe, le milieu extérieur a l’indice n₀.

sin ic=n₂/n₁ ; θ<arccos(n₂/n₁)  
n₀ sin θentrée, max=NA=√(n₁²−n₂²)  
V=(2πa/λ₀)NA ; monomode LP₀₁ si V<2,405 pour une fibre idéale faiblement guidante

**Dérivation.** La réflexion totale demande n₁ sin i>n₂, soit n₁ cosθ>n₂. En combinant avec n₀ sinθentrée=n₁ sinθ on obtient le cône d’acceptance. Le rayon axial et les rayons très inclinés ne passent pas le même temps dans une fibre multimode.

**Exemple.** n₁=1,48, n₂=1,46 donnent NA≈0,2425 et θentrée, max≈14,03° dans l’air. Avec a=4 μm, λ₀=1,55 μm, V≈3,93 : le critère monomode n’est pas satisfait. Le seuil sur le rayon est a<2,405λ₀/(2πNA)≈2,45 μm.

**Deux niveaux.** La réflexion totale décrit la trajectoire de rayons quand le cœur est grand devant λ. Le nombre V et le seuil 2,405 appartiennent au problème d’onde cylindrique : ils ne sont pas déduits par le seul dessin d’un rayon. Une fibre courbée, lossy ou fortement guidante demande d’autres corrections.

## 13. Fibre à gradient : réduire la dispersion intermodale

*Spé → Au-delà accompagné* — laboratoire `fibre`.

**Idée.** Un cœur dont l’indice décroît depuis l’axe courbe progressivement les rayons. Les trajectoires éloignées sont plus longues mais parcourent un milieu de vitesse supérieure. Un profil parabolique peut compenser au premier ordre ces deux effets, contrairement au cœur uniforme.

n(r)≈naxe[1−g²r²/2] ; r″(z)+g²r(z)≈0  
r(z)=r₀ cos(gz)+(θ₀/g)sin(gz) ; période≈2π/g  
t≈(1/c)∫n(r)√(1+r′²) dz

**Démonstration.** Dans la limite paraxiale, d(nu)/ds=∇n conduit à r″≈(1/n)∂rn≈−g²r. Pour comparer les temps, garder à la fois le terme d’indice et √(1+r′²)≈1+r′²/2 : supprimer l’un des deux empêche précisément la compensation recherchée.

**Comparaison.** Dans une fibre à saut d’indice uniforme de longueur L, tθ≈n₁L/(c cosθ). Pour L=1 km, n₁=1,48 et θ=10°, l’excès par rapport à l’axe est environ 76,2 ns. Il suffit à élargir une impulsion courte même si aucun rayon ne fuit.

**Limites.** Le modèle de rayons ne décrit pas la dispersion chromatique, la dispersion de polarisation ni les pertes. Les résultats sur les trajectoires et l’acceptance sont complémentaires de la propagation d’un paquet d’ondes dans l’atelier Champs et Matière.

## 14. Mirage : un invariant et une trajectoire parabolique

*Sup → Spé* — laboratoire `mirage`.

**Profil étudié.** L’exemple du recueil est n(z)=n₀√(1+z/a), avec a>0 et z>−a. θ est l’angle du rayon avec l’horizontale ; x est la distance horizontale. Un indice croissant avec z courbe le rayon vers les couches hautes et peut donner une image de sol réfléchissant.

n(z)cosθ=n(z₀)cosθ₀ ; z′=tanθ  
z″=1/[2(a+z₀)cos²θ₀]  
z(x)=z₀+x tanθ₀+x²/[4(a+z₀)cos²θ₀]

**Dérivation.** L’invariance par translation horizontale conserve la composante horizontale du vecteur n u. En élevant au carré, 1+z′²=(a+z)/[(a+z₀)cos²θ₀]. Dériver donne une accélération verticale constante ; intégrer deux fois fixe le coefficient quadratique et les deux conditions initiales.

**Exemple.** a=1000 m, z₀=1 m, θ₀=−1° donnent un point bas à x*=−2(a+z₀)cos²θ₀ tanθ₀≈34,94 m et zmin≈0,695 m. À x≈69,88 m, le rayon revient à son altitude de départ. Ce modèle stylisé ne remplace pas un profil atmosphérique mesuré.

**Interprétation.** Au point bas θ=0, la courbure est finie : on ne doit pas diviser aveuglément par z′=0 dans la dérivation. L’observateur prolonge la tangente à l’arrivée ; c’est ce prolongement rectiligne, distinct du rayon courbe, qui donne une position apparente.

## 15. Arc-en-ciel : une caustique plutôt qu’un rayon privilégié

*Sup → Spé* — laboratoire `arcenciel`.

**Modèle.** Une goutte sphérique d’indice n dans l’air réfracte la lumière à l’entrée, effectue p réflexions internes puis la réfracte à la sortie. i et r sont les angles à la normale. Le rayon primaire correspond à p=1 ; le secondaire à p=2.

sin i=n sin r ; Dp=pπ+2i−2(p+1)r  
D′p=2−2(p+1)cos i/(n cos r)  
sin² i*=[(p+1)²−n²]/[(p+1)²−1]

**Stationnarité.** Des incidences voisines donnent presque la même déviation lorsque D′p=0 : les rayons se concentrent angulairement, ce qui produit une caustique. La divergence du modèle géométrique est régularisée par la diffraction et la taille finie de la source.

**Exemple.** Pour n=4/3 et p=1, i*≈59,39°, r*≈40,20° et Dmin≈137,97°. Le rayon du cercle primaire autour du point antisolaire vaut π−Dmin≈42,03°. Pour p=2, la déviation stationnaire dépasse π et donne un rayon secondaire voisin de 51°. La seconde réflexion réduit l’intensité.

**Dispersion.** Au point stationnaire primaire, ∂D/∂n=4tanr/n. Le violet, de plus grand indice, a une déviation D supérieure donc un rayon antisolaire inférieur : il est à l’intérieur du primaire. Le secondaire inverse l’ordre. Les coefficients de Fresnel rendent aussi les arcs partiellement polarisés.

## 16. Prisme et goniomètre : mesurer une dispersion

*Sup ; TP* — laboratoire `prisme`.

**Montage.** Un collimateur donne une onde quasi plane ; une lunette afocale repère l’angle de sortie. A est l’angle au sommet du prisme ; i, r sont les angles d’entrée, r′, i′ ceux de sortie. Les indices d’entrée et de sortie sont ceux de l’air dans le modèle.

r+r′=A ; D=i+i′−A ; sin i=n sin r  
Dmin=2arcsin[n sin(A/2)]−A  
n=sin[(A+Dmin)/2]/sin(A/2) ; n(λ₀)=a+b/λ₀²

**Démonstration.** Différencier la loi de Snell aux deux faces avec dr′=−dr. La déviation stationnaire est obtenue pour le trajet symétrique i=i′, r=r′=A/2. Vérifier n sin(A/2)≤1 : si cette condition échoue, la transmission à ce trajet est impossible.

**Exemple.** A=60°, n=1,50 donnent Dmin≈37,18°. Inversement, Dmin=40° donne n≈1,5321. Pour mesurer l’indice, suivre le retournement de déplacement de la raie lorsque le prisme tourne, plutôt que chercher le minimum par une unique lecture.

**Cauchy.** La constante b a les unités de λ₀² ; une valeur donnée en μm² doit être convertie si λ est exprimée en nm. Ajuster n en fonction de 1/λ₀² donne une droite dans une fenêtre transparente limitée ; cette loi empirique ne s’étend pas arbitrairement aux résonances d’absorption.

## 17. Aberrations : la sphère face au paraboloïde

*Sup → Spé ; prolongement conception* — laboratoire `aberrations`.

**Deux modèles.** La conjugaison du miroir sphérique résume une limite paraxiale. Le laboratoire compare les réflexions géométriques exactes d’un faisceau axial sur une sphère et sur un paraboloïde. Le sommet est x=0, le centre sphérique x=−R, le faisceau arrive depuis x<0 vers +x ; le foyer paraxial est x=−R/2.

Sphère : x(y)=−R+√(R²−y²) ; parabole : x(y)=−y²/(2R)  
vsortie=vincident−2(vincident·n̂)n̂  
Foyer axial du paraboloïde : xF=−R/2

**Aberration sphérique.** Pour la sphère, les rayons de hauteurs différentes ne coupent pas l’axe au même endroit. Fermer l’ouverture rapproche la surface de sa approximation parabolique : x=−y²/(2R)−y⁴/(8R³)+… . Le cercle de moindre diffusion n’est pas toujours au foyer paraxial. Le calcul exact reste un calcul de rayons : aucun anneau de diffraction n’y est simulé.

**Stigmatisme axial.** Le paraboloïde rend égaux les chemins optiques d’un front plan axial vers F : sa normale bisecte la direction incidente et celle du foyer. Il est donc stigmatique pour cet objet à l’infini sur l’axe, même à grande ouverture géométrique. Une source hors axe peut cependant produire de la coma ; ce succès ne rend pas toutes ses images parfaites.

**Technique.** Déplacer l’écran et comparer l’écart des interceptions à ouverture fixée. Fermer le diaphragme réduit l’erreur géométrique mais augmente la diffraction de l’atelier Airy. Pour une lentille, un autre effet s’ajoute : n(λ) variable donne un chromatisme ; il est absent de la réflexion idéale de ces miroirs.

## 18. Fermat : calculer un chemin stationnaire

*Sup → Spé ; calcul variationnel accompagné* — laboratoire `fermat`.

**Fonction étudiée.** Entre A et B de part et d’autre d’une interface plane, le point de traversée a l’abscisse x. Les hauteurs positives sont h₁, h₂ et la séparation horizontale totale est X. La durée est le chemin optique L divisé par c.

L(x)=n₁√(x²+h₁²)+n₂√[(X−x)²+h₂²]  
L′=n₁ x/√(x²+h₁²)−n₂(X−x)/√[(X−x)²+h₂²]  
L′=0 ⇔ n₁sin i=n₂sin r

**Unicité ici.** L″=n₁h₁²/(x²+h₁²)³ᐟ²+n₂h₂²/[(X−x)²+h₂²]³ᐟ²>0 : cette configuration donne un minimum unique. Dans un système optique général, le principe est celui d’une stationnarité ; des maxima ou selles peuvent intervenir. La convexité doit être prouvée pour parler de minimum.

**Exemple.** Pour n₁=n₂ et h₁=h₂, la symétrie donne x=X/2. Si n₂ augmente, le rayon parcourt moins de distance horizontale dans le second milieu : le passage se déplace vers B. La trajectoire la plus rapide n’est plus le segment euclidien le plus court.

**Lien interdisciplinaire.** Optimisation, convexité, équations d’Euler–Lagrange et intégrales premières sont les mêmes outils que dans l’atelier Distances. Dans un indice variable, la fonctionnelle ∫n ds donne d(nu)/ds=∇n, ce qui relie Fermat, Snell et le mirage.

## 19. Interférer : sommer les amplitudes, moyenner les intensités

*Sup → Spé* — laboratoire `young`.

**Notations.** Deux champs de même fréquence et de même polarisation ont des amplitudes complexes A₁, A₂. Les intensités individuelles I₁, I₂ sont proportionnelles à |A₁|²,|A₂|². Le détecteur moyenne sur un temps grand devant la période optique ; il ne moyenne pas automatiquement à zéro une différence de phase stable.

I=I₁+I₂+2√(I₁I₂) cosφ  
Imax=(√I₁+√I₂)² ; Imin=(√I₁−√I₂)²  
V=(Imax−Imin)/(Imax+Imin)=2√(I₁I₂)/(I₁+I₂)

**Cohérence.** La formule suppose une différence de phase stable. Pour des sources mutuellement indépendantes, la moyenne du terme croisé est nulle et I=I₁+I₂. Des polarisations orthogonales annulent aussi le produit scalaire des champs, même si leur fréquence est identique.

**Exemple.** I₂=I₁/4 donne V=0,80, Imax=2,25I₁ et Imin=0,25I₁. Une frange noire n’est possible qu’avec amplitudes égales, cohérence complète et polarisation compatible. La visibilité peut donc diminuer sans modification de l’interfrange.

**Bilan.** Un maximum local de 4I₁ pour deux faisceaux égaux ne crée pas d’énergie : le champ redistribue le flux entre régions brillantes et sombres. Pour un dispositif complet, les sorties complémentaires et la normalisation spatiale doivent entrer dans le bilan.

## 20. Young réel : deux longueurs, deux échelles

*Sup → Spé* — laboratoire `young`.

**Géométrie.** Les centres des fentes sont séparés de a ; chaque fente a une largeur b. Le plan d’observation est à distance D et la coordonnée transverse est x. Les directions sont paraxiales, les fentes sont uniformément éclairées et l’observation se fait en Fraunhofer, ou dans un plan focal équivalent.

δ≈ax/D ; i=λ₀D/a  
I(x)∝sinc²[πbx/(λ₀D)]·[1+ρ+2√ρ cos(2πax/(λ₀D)+φ₀)]  
sinc u=sin u/u ; sinc 0=1 ; largeur totale du lobe central=2λ₀D/b

**Lecture.** a contrôle l’interfrange ; b contrôle l’enveloppe. Doubler a divise i par deux sans rétrécir l’enveloppe. Doubler b resserre l’enveloppe sans changer les positions idéales des franges. ρ=I₂/I₁ contrôle leur contraste, φ₀ leur translation.

**Exemple.** λ₀=600 nm, D=2 m, a=0,50 mm donnent i=2,40 mm. Avec b=0,040 mm, les premiers zéros de diffraction sont à x=±30 mm. L’ordre interférentiel k=25 coïncide avec un zéro d’enveloppe ; ce maximum est manquant.

**Technique.** Construire la différence de marche avant d’utiliser cos. Le signe de δ ou de φ dépend de l’ordre des trajets ; avec cos, une inversion simultanée ne change pas I. La phase additionnelle d’une lame, d’une translation ou d’une polarisation peut déplacer les franges.

## 21. Réseau : somme géométrique et pouvoir de résolution

*Spé* — laboratoire `reseau`.

**Objets.** N fentes uniformes de largeur b et de pas d sont éclairées sous θ₀. La direction θ donne une différence de marche d(sinθ−sinθ₀). Les raies d’un doublet spectral indépendant s’additionnent en intensité ; elles ne sont pas deux amplitudes cohérentes à une seule fréquence.

φ=2πd(sinθ−sinθ₀)/λ₀ ; A∝∑p=0…N−1 exp(ipφ)  
I∝sinc²[πb(sinθ−sinθ₀)/λ₀]·[sin(Nφ/2)/sin(φ/2)]²  
d(sinθm−sinθ₀)=mλ₀ ; Rrésolution=λ₀/Δλ≈|m|N

**Singularités.** À φ=2πm, le quotient se prolonge par N en amplitude, N² en intensité. Les zéros proches sont à φ=2πm±2π/N. Cette largeur diminue avec N tandis que la séparation des raies augmente avec |m| : leur comparaison donne le critère mN.

**Exemple.** Le doublet 589,0/589,6 nm a λ/Δλ≈982. À l’ordre 1 il faut environ 982 fentes éclairées ; à l’ordre 2 environ 491. Un pas d=2 μm permet l’ordre 2 autour de sinθ≈0,589 ; certains ordres plus élevés sont absents si |sinθm|>1.

**Limites.** Une enveloppe de fente peut supprimer un ordre pourtant géométriquement autorisé. Éclairage non uniforme, largeur de source, aberrations et résolution du détecteur modifient la résolution effective. R=λ/Δλ est un pouvoir spectral sans dimension, distinct d’une séparation spatiale minimale.

## 22. Fraunhofer : intégrer une pupille rectangulaire

*Spé ; TP* — laboratoire `diffraction`.

**Champ.** La diffraction scalaire associe à chaque élément de pupille une amplitude et une phase. En champ lointain ou au foyer d’une lentille, la phase est linéaire en coordonnées de pupille. a, b sont les dimensions du rectangle ; fx, fy sont les fréquences spatiales en m⁻¹.

A(fx, fy)∝∫−a/2ᵃ/² ∫−b/2ᵇ/² t(x, y)e^(−2πi(fx x+fy y)) dxdy  
t=1 ⇒ A∝ab sinc(πa fx)sinc(πb fy)  
fx≈X/(λ₀f′) ; I/I(0)=sinc²(πaX/(λ₀f′))sinc²(πbY/(λ₀f′))

**Calcul.** Séparer l’intégrale bidimensionnelle en produit de deux intégrales. ∫−a/2ᵃ/² exp(−ikx)dx=a sinc(ka/2). Le carré intervient après la somme complexe. Inverser cette succession supprimerait les interférences entre les éléments de pupille.

**Exemple.** a=0,20 mm, b=0,80 mm, f′=300 mm, λ₀=600 nm donnent des premiers zéros à X=±0,90 mm, Y=±0,225 mm. La petite dimension de pupille produit la grande dimension de tache : l’image diffractée croise l’orientation intuitive du trou.

**Régime.** Un écran éloigné demande un nombre de Fresnel a²/(λ₀D) suffisamment petit pour l’approximation lointaine. Le plan focal d’une lentille réalise la transformée de Fourier sous les hypothèses paraxiales. a≪D seul ne suffit pas à garantir Fraunhofer.

## 23. Apodisation cosinus : réduire les lobes a un coût

*Spé → Au-delà accompagné* — laboratoire `diffraction`.

**Pupille.** Sur |x|≤a/2, la transmittance d’amplitude est t(x)=cos(πx/a) ; elle est nulle ailleurs. Elle ne transmet pas uniformément et son carré décrit la transmission locale de puissance. La variable u=πa sinθ/λ₀ sert à comparer avec la fente uniforme.

A(u)∝a·(π/2) cosu/(π²/4−u²)  
A(u)/A(0)=(π²/4) cosu/(π²/4−u²)  
Premiers zéros : u=±3π/2 ; u=±π/2 est une singularité amovible

**Dérivation.** Écrire cos(πx/a) comme la somme de deux exponentielles : l’amplitude est la somme de deux sinc décalés. À u=±π/2, numérateur et dénominateur s’annulent mais leur rapport est fini ; remplacer cette valeur par zéro créerait un faux minimum.

**Compromis.** La demi-largeur du lobe central est 3λ₀/(2a), contre λ₀/a pour la fente uniforme. La puissance transmise à éclairage uniforme est ∫cos²(πx/a)dx=a/2, soit la moitié de celle d’une fente ouverte de même largeur. Une normalisation à I(0)=1 masque cette perte.

**Exemple.** a=1 mm, λ₀=600 nm donnent les premiers zéros à ±0,900 mrad ; à u=π/2, I/I(0)=π²/16≈0,617. Le passage de lobes secondaires faibles à un pic plus large illustre un compromis général de fenêtrage en optique et en traitement du signal.

## 24. Polarisation : Malus, ellipse et lame à retard

*Sup → Spé selon filière* — laboratoire `polarisation`.

**Mesure.** Un analyseur linéaire d’axe â projette le champ sur cet axe. Pour un état rectiligne d’angle θ avec l’analyseur, I=I₀cos²θ. Une intensité constante quand on tourne l’analyseur peut correspondre à un état circulaire ou à une lumière non polarisée ; une lame quart d’onde permet de les distinguer.

Ex=Ax cosωt ; Ey=Ay cos(ωt−δ)  
δlame=2πΔn e/λ₀ ; quart d’onde : |δ|=π/2 ; demi-onde : |δ|=π  
Lame idéale sans pertes ⇒ |Ex|²+|Ey|² conservé

**Quart d’onde.** Une entrée rectiligne à 45° des axes propres et une retardance ±π/2 donnent deux composantes égales en quadrature : un cercle. Une entrée alignée sur un axe propre reste rectiligne. Le signe de la rotation dépend de la convention temporelle et du sens d’observation.

**Demi-onde.** Une entrée rectiligne d’angle θ face à un axe propre d’angle α ressort rectiligne d’angle 2α−θ modulo π. La lame conserve l’intensité ; la transmission de l’analyseur peut ensuite varier jusqu’à l’extinction.

**TP.** Commencer par caractériser la source à l’analyseur seul, introduire la lame et chercher ses axes, puis interpréter les minima et maxima. La couleur, les pertes et l’achromatisme limitent la description d’une lame par une unique retardance indépendante de λ.

## 25. Jones et Poincaré : calcul matriciel et état physique

*Spé → Au-delà accompagné* — laboratoire `polarisation`.

**Convention.** Le champ réel est Re[Ẽ exp(−iωt)]. Jones décrit un état monochromatique complètement polarisé par un vecteur complexe (Ex, Ey). Dans sa base propre la lame applique diag(1, exp(iδ)) ; une rotation réelle ramène ce vecteur dans les axes du banc.

J(α, δ)=R(α)diag(1, e^(iδ))R(−α)  
Ianalyseur=|Ex cosβ+Ey sinβ|²  
S₀=|Ex|²+|Ey|² ; S₁=|Ex|²−|Ey|² ; S₂=2Re(Ex*Ey) ; S₃=2Im(Ex*Ey)

**Sphère.** Pour un état pur, S₁²+S₂²+S₃²=S₀². Les états rectilignes sont sur l’équateur S₃=0 et les deux quadratures circulaires aux pôles. Une phase globale exp(iφ) n’altère ni ellipse ni Stokes. Les angles de l’orientation rectiligne sont doublés sur l’équateur.

**Exemple.** (Ex, Ey)=(1, i)/√2 donne (S₁, S₂, S₃)=(0,0,1), une transmission de 1/2 par tout analyseur linéaire. Une lame quart d’onde convenable convertit cet état en rectiligne et rend une extinction possible.

**Lien quantique.** Une polarisation d’un photon a le même espace complexe à deux composantes qu’un qubit ; la sphère de Poincaré correspond alors à une sphère de Bloch avec conventions d’axes annoncées. Une lumière partiellement polarisée demande Stokes ou une matrice de cohérence : un seul vecteur Jones ne suffit pas.

## 26. Michelson : le facteur deux et les franges localisées

*Spé ; TP* — laboratoire `michelson`.

**Montage.** La séparatrice crée deux trajets d’une même source ; les miroirs les renvoient à la séparatrice. Le déplacement axial e d’un miroir modifie un aller-retour. Une compensatrice égalise les traversées de verre quand le spectre est large.

Lame d’air : δ=2e cos i ; p=2e cos i/λ₀  
Petit angle au foyer : r≈f′i ; δ≈2e−e r²/f′²  
Coin d’air de petit angle α : δ(x)≈δ₀+2αx ; interfrange≈λ₀/(2α)

**Deux figures.** Les anneaux d’égale inclinaison se lisent dans un plan focal : i y est transformé en une distance radiale. Les franges d’égale épaisseur du coin s’observent dans un plan image adapté. Les deux axes de graphique n’ont donc pas le même rôle physique.

**Mesure.** Une translation Δe fait défiler N≈2Δe/λ₀ franges en un point fixé. À 546 nm, Δe=100 μm correspond à environ 366 franges. Dans la lame d’air, deux anneaux brillants voisins ont une différence de rayons au carré de λ₀f′²/e dans l’approximation des petits angles.

**Lumière blanche.** Un spectre large concentre la visibilité près de la différence de marche nulle. La couleur des franges demande de sommer les contributions spectrales ; l’atelier monochromatique montre la géométrie, et le laboratoire Cohérence traite séparément l’enveloppe spectrale.

## 27. Cohérence temporelle : transformer un spectre en visibilité

*Spé* — laboratoire `coherence`.

**Corrélation.** La différence de marche δ introduit le retard τ=δ/c dans l’air. Pour des intensités égales, la visibilité est le module de la cohérence γ(τ). Le spectre S(ν) est une densité positive de puissance ; ses composantes indépendantes se somment en intensité.

γ(τ)=∫S(ν)e^(2πiντ)dν / ∫S(ν)dν ; V=|γ|  
S gaussien de largeur FWHM Δν ⇒ V=exp[−π²Δν²τ²/(4ln2)]  
Deux raies égales ν₁, ν₂ ⇒ V=|cos[π(ν₂−ν₁)τ]|

**Échelles.** La formule τc≈1/Δν donne un ordre de grandeur, mais un temps à 1/e, à moitié visibilité ou une largeur intégrale diffèrent par des facteurs numériques. Toujours déclarer le profil spectral et le seuil utilisé avant de comparer deux longueurs de cohérence.

**Exemple.** Pour Δν=20 GHz, le spectre gaussien atteint V=1/2 à δ=2ln2·c/(πΔν)≈6,62 mm. Un doublet étroit montre au contraire des annulations puis des retours de contraste ; une première annulation ne mesure pas sa largeur intrinsèque de raie.

**Technique.** Travailler en fréquence pour une transformée en retard. Une petite largeur en longueur d’onde vérifie Δν≈cΔλ/λ₀² ; convertir un spectre large de Sλ à Sν demande aussi le jacobien |dλ/dν|.

## 28. Source étendue et doublet : deux pertes de contraste différentes

*Spé ; TP* — laboratoire `coherence`.

**Étendue.** Une source uniforme de largeur s à distance Ds éclaire deux fentes séparées de a. Deux points sources sont pris mutuellement indépendants. Chacun produit des franges décalées ; leur somme peut effacer le contraste sans effacer la puissance reçue.

γspatial=sinc[πas/(λ₀Ds)] ; Vspatial=|γspatial|  
Sous hypothèses séparables : V=|γtemporel γspatial|  
Doublet : première annulation δ≈λ₀²/(2Δλ) ; période de |V|≈λ₀²/Δλ

**Exemple.** Avec λ₀=600 nm, a=0,50 mm, Ds=1 m, le premier zéro spatial est à s=1,20 mm. Une source ponctuelle lève cet effet mais n’annule pas la largeur spectrale. Pour le sodium autour de 589,3 nm et Δλ=0,60 nm, la première annulation temporelle est vers 0,289 mm.

**Michelson.** Au voisinage de l’incidence normale, δ≈2e ; les annulations du doublet sont espacées de Δe≈λ₀²/(2Δλ). Ce facteur deux ne doit pas être confondu avec la demi-période qui situe la première annulation depuis le contact.

**Protocole.** À δ fixé, varier s puis Ds et suivre a s/Ds. À source spatialement fine, balayer δ et comparer gaussien et doublet. Conserver les deux trajets mais sélectionner des sources indépendantes fait disparaître le terme croisé à tout retard dans le modèle.

## 29. Fabry–Perot : additionner une infinité de trajets

*Spé → Au-delà accompagné* — laboratoire `fabryperot`.

**Cavité.** Deux miroirs plans parallèles identiques encadrent une lame d’épaisseur e et d’indice n. R est leur réflectivité de puissance, T=1−R en absence de pertes. θ est l’angle interne ; la longueur d’onde λ₀ est celle du vide.

φ=4πne cosθ/λ₀ ; Atransmis∝T/(1−R e^(iφ))  
It/Iincident=1/[1+F sin²(φ/2)] ; F=4R/(1−R)²  
φ=2πm ⇒ transmission=1 pour deux miroirs identiques sans pertes

**Dérivation.** Chaque aller-retour multiplie l’amplitude par R exp(iφ), car deux facteurs de réflexion d’amplitude de module √R interviennent. La série converge pour R<1. À résonance, les contributions se renforcent malgré la faible transmission d’un miroir isolé.

**Exemple.** R=0,90 donne F=360 et Tmin=1/(1+F)≈0,00277. Le contraste spectral est élevé, mais les résonances se répètent à chaque ordre : un filtre d’ordre peut être nécessaire pour isoler une raie unique.

**Convention.** Le coefficient d’Airy F et la finesse spectrale ne sont pas le même nombre. Des miroirs inégaux, des pertes, une absorption ou une phase de réflexion dispersive réduisent et déplacent les pics. Le modèle idéal utilise ici une cavité vide de pertes et un balayage quasi statique.

## 30. Fabry–Perot : intervalle libre, finesse et angle

*Spé → Au-delà accompagné* — laboratoire `fabryperot`.

**Mesures.** L’intervalle spectral libre sépare deux résonances consécutives en fréquence. La finesse ℱ est ce même intervalle divisé par la largeur FWHM d’un pic. Les expressions simples supposent un indice constant sur la fenêtre ; en milieu dispersif l’indice de groupe remplace l’indice de phase pour l’intervalle.

FSR=c/(2ne cosθ) ; ℱ=π/[2arcsin(1/√F)] si F≥1  
R proche de 1 : ℱ≈π√R/(1−R) ; ΔνFWHM=FSR/ℱ  
νm(θ)=mc/(2ne cosθ)

**Exemple.** Dans l’air, e=5 mm et R=0,90 donnent FSR≈29,98 GHz,ℱ≈29,79 et Δν≈1,01 GHz. Augmenter e rapproche les ordres sans changer cette finesse idéale ; augmenter R resserre les pics en réduisant la largeur relative.

**Angle.** Une direction inclinée a cosθ<1 : sa fréquence résonante augmente pour un ordre fixé, tandis que la longueur d’onde résonante diminue. Une distribution angulaire large mélange des fréquences de résonance différentes et peut élargir un pic.

**Technique.** Pour comparer deux raies, exprimer Δλ et Δν dans la même fenêtre locale puis examiner largeur, ordre et contraste. Un pic fin ne garantit pas l’absence d’ambiguïté d’ordre. Les oscillations de cavité expliquent aussi la sélection longitudinale d’un laser.

## 31. Optique de Fourier : de la lentille au filtrage 4f

*Spé → Au-delà accompagné* — laboratoire `fourier`.

**Chaîne.** Un objet complexe Eobjet(x, y) est placé dans le plan focal objet d’une lentille. Son plan focal image porte, à un facteur de phase et d’échelle près, sa transformée de Fourier. Un masque H(fx, fy) placé là filtre les amplitudes ; une seconde lentille reconstruit un champ image.

XFourier=λ₀ f′ fx ; YFourier=λ₀ f′ fy  
Eimage=TF⁻¹[H·TF(Eobjet)] ; Iimage=|Eimage|²  
TF E(f)=∫E(x)e^(−2πifx)dx

**Lecture.** Un masque passe-bas réduit les hautes fréquences spatiales, donc les détails fins ; un passe-haut accentue les transitions mais modifie leur champ et leur intensité. Une fente verticale du plan de Fourier restreint fx et agit sur la variation horizontale de l’image.

**Exemple.** Avec λ₀=600 nm, f′=200 mm, une fréquence de 20 mm⁻¹ se trouve à 2,40 mm de l’axe dans le plan de Fourier. Doubler f′ double cette position sans modifier la fréquence spatiale de l’objet.

**Précision.** Filtrer une image d’intensité comme un signal réel n’est pas la même opération que filtrer son champ complexe cohérent puis le mettre au carré. Le laboratoire suit cette deuxième chaîne. Deux transformées directes réalisent une inversion spatiale ; l’écriture avec TF⁻¹ utilise des coordonnées image redressées.

## 32. Fourier numérique : phase, Parseval et échantillonnage

*Spé → Au-delà accompagné* — laboratoire `fourier`.

**Objet.** Le champ peut avoir une amplitude uniforme mais une phase variable. Son intensité de départ est alors uniforme, tandis que son spectre complexe contient les variations de phase. Un filtre peut convertir une partie de ces variations en contraste d’intensité.

Eobjet=A e^(iφ(x, y)) ; FFT unitaire ⇒ ∑|E|²=∑|Ẽ|²  
|H|≤1 ⇒ ∑|Eimage|²≤∑|Eobjet|²  
fNyquist=1/(2Δx) ; Δf=1/(NΔx)

**Exemple.** Un pas Δx=10 μm donne fNyquist=50 mm⁻¹. Une fréquence physique de 80 mm⁻¹ ne peut pas être représentée fidèlement par cette grille : elle replie sur une fréquence plus basse. Le réglage d’un masque au-delà de Nyquist n’ajoute pas des détails absents.

**Bilan.** Le filtre identité conserve la norme totale du champ ; un masque opaque perd de l’énergie. Une image dont chaque affichage est séparément renormalisé peut sembler aussi lumineuse dans les deux cas : le bilan chiffré, distinct de la palette de visualisation, empêche cette confusion.

**Limites.** La grille finie correspond à un objet périodisé dans le calcul ; les contours et les bords peuvent introduire des fréquences. Une convolution de PSF convient à l’imagerie incohérente, mais ce laboratoire simule une propagation et un filtrage de champ cohérent.

## 33. Laser : stabilité de cavité et seuil de gain

*Spé → Au-delà accompagné* — laboratoire `laser`.

**Deux questions.** Le mot laser désigne une amplification par émission stimulée avec retour de cavité. Un confinement géométrique stable fournit des modes transverses ; il faut ensuite que le gain compense les pertes pour l’oscillation. Une cavité stable sans inversion de population n’est pas un laser actif.

g₁=1−L/R₁ ; g₂=1−L/R₂ ; zone stable intérieure : 0<g₁g₂<1  
Multiplicateur de puissance aller-retour : Rmiroir1 Rmiroir2 exp[2(g−α)L]  
gseuil=α−ln(Rmiroir1 Rmiroir2)/(2L)

**Variables.** R₁, R₂ dans g₁, g₂ sont des rayons de courbure signés, tandis que Rmiroir sont des réflectivités sans dimension. Le laboratoire règle des courbures 1/R en m⁻¹, pour représenter aussi un miroir plan. g et α sont ici des coefficients de gain et de perte d’intensité en m⁻¹.

**Saturation.** Avec le modèle g(P)=g₀/(1+P/Ps), le régime établi impose g(P)=gseuil, d’où P=Ps(g₀/gseuil−1) quand g₀>gseuil. La puissance transmise au coupleur est approximativement (1−Rmiroir2)P. La pompe fournit l’énergie, la cavité la redistribue.

**Limites.** Les frontières de stabilité sont marginales ; des configurations dégénérées demandent un examen spécifique, notamment le confocal. Le modèle de saturation ne décrit ni compétition multimode, ni dynamique de population, ni largeur de raie ou bruit. Les modes longitudinaux sont espacés approximativement de c/(2nL).

## 34. Faisceau gaussien : conserver la puissance en divergent

*Spé → Au-delà accompagné* — laboratoire `gaussien`.

**Notations.** w(z) est le rayon où l’intensité vaut 1/e² de sa valeur axiale, non un diamètre. w₀ est le waist au plan z=0. Le milieu est homogène d’indice n ; λ₀ est dans le vide. Le faisceau fondamental paraxial TEM₀₀ ne représente pas tout faisceau laser réel.

zR=πn w₀²/λ₀ ; w(z)=w₀√[1+(z/zR)²]  
I(r, z)=2P/[πw(z)²] exp[−2r²/w(z)²] ; θdiv≈λ₀/(πn w₀)  
Rfront=z[1+(zR/z)²] ; ψGouy=arctan(z/zR)

**Intégrale.** La puissance est 2π∫₀∞I r dr=P à tout z. Le maximum diminue quand le faisceau s’élargit ; la puissance ne diminue pas dans ce modèle sans pertes. Au waist Rfront est infini, donc le front est localement plan malgré une divergence future finie.

**Exemple.** w₀=50 μm, λ₀=633 nm, n=1 donnent zR≈12,41 mm et θdiv≈4,03 mrad. À z=zR, w=w₀√2 et Iaxe est divisée par deux. Avec P=2 mW, Iaxe(0)≈5,09×10⁵ W·m⁻².

**Lien.** Focaliser davantage diminue w₀ mais augmente la divergence et réduit zR quadratiquement. Avec les matrices du vecteur (y, θ), q=z+izR obéit à q′=(Aq+B)/(Cq+D), et 1/q=1/Rfront−iλ₀/(πn w²). Pour utiliser à la place le vecteur réduit (y, nθ) de la leçon 4, prendre le paramètre qréduit=q/n, qui suit cette même loi homographique avec ses matrices réduites. Le choix des coordonnées demeure cohérent de la translation au faisceau.

## 35. Airy : une pupille circulaire et deux étoiles indépendantes

*Spé → Au-delà accompagné* — laboratoire `airy`.

**Pupille idéale.** Un disque circulaire uniformément éclairé de diamètre D produit une fonction de Bessel J₁. Les exemples astronomiques du laboratoire sont des pupilles circulaires idéales ; ils ne reproduisent pas la PSF réelle des miroirs segmentés, des branches de support ou d’une atmosphère turbulente.

u=πD sinθ/λ₀ ; I/I(0)=[2J₁(u)/u]²  
Premier zéro : u≈3,831706 ⇒ sinθ₁≈1,21967 λ₀/D  
Étoiles indépendantes : Itotal(x)=I₁ PSF(x−s/2)+I₂ PSF(x+s/2)

**Rayleigh.** Pour deux points de flux égaux et une pupille circulaire sans aberration, la séparation de Rayleigh place le maximum de l’un au premier zéro de l’autre. C’est un critère conventionnel de discernabilité, non une frontière absolue d’inférence à partir de données bruitées.

**Obstruction.** Une pupille annulaire de rapport ε donne A(u)∝2[J₁(u)−εJ₁(εu)]/[u(1−ε²)]. Le pic normalisé peut se resserrer tandis que les anneaux se renforcent et que le flux collecté baisse d’un facteur 1−ε². Utiliser le même repère 1,22λ/D ne prétend pas recalculer le zéro annulaire.

**Exemple.** D=200 mm, λ₀=550 nm donnent le repère de 0,692 seconde d’arc. Doubler D le divise par deux ; doubler seulement le grossissement de l’oculaire ne change pas la PSF angulaire. Un compagnon faible exige un contraste plus grand que deux étoiles égales.

## 36. Optique non linéaire χ² : accord de phase et bilan photonique

*Au-delà accompagné* — laboratoire `nonlineaire`.

**Processus.** Une polarisation quadratique mélange les champs et peut générer une onde à 2ω. Le laboratoire traite le doublage dégénéré d’une seule pompe, avec d=χeff/2. Les indices nω et n2ω et le coefficient d en m·V⁻¹ normalisent l’efficacité. Le désaccord effectif Δk est réglé séparément : une orientation ou un quasi-accord peut le modifier tandis que ces indices de normalisation restent approchés comme fixes. Le banc ne recalcule donc pas automatiquement Δk=(4π/λ₀)(n2ω−nω).

Pompe constante : η=I2ω/Iω, entrée≈[2ω²d²IωL²/(nω² n2ω ε₀c³)] sinc²(ΔkL/2)  
Δk=0 ⇒ η∝IωL² au faible taux ; longueur de cohérence Lc=π/|Δk|  
Manley–Rowe dégénéré : Nω+2N2ω constant ; Iω+I2ω constant

**Dérivation.** Une enveloppe harmonique engendrée vérifie E′2ω∝Eω² exp(iΔkz). Si Eω varie peu, son intégrale de 0 à L est L exp(iΔkL/2)sinc(ΔkL/2). Le carré donne le facteur de phase et la loi L². Un rendement calculé supérieur à 1 annonce l’échec de la pompe constante.

**Déplétion.** Les ondes couplées normalisées du laboratoire conservent |u|²+|v|²=1 ; à accord parfait, η=tanh²(κL). La pompe s’épuise progressivement et le rendement reste borné. Un désaccord peut donner une reconversion et des oscillations plutôt qu’une croissance monotone.

**Lien au recueil.** L’exemple du PDF à deux pompes distinctes de fréquence ω conserve N₁+N₃ et N₂+N₃ : chaque photon généré consomme un photon de chaque pompe. Une seule pompe dégénérée en consomme deux. Deux photons de 1064 nm donnent un photon de 532 nm ; l’énergie est conservée, le nombre total de photons ne l’est pas.

## Les 24 introductions de laboratoire

### Laboratoire `snell`

Comprendre le changement de direction à une interface et reconnaître le seuil où un rayon transmis propagatif cesse d’exister. Les courbes de Fresnel relient ensuite ce tracé au bilan de puissance.

**Objets et unités**

- n₁, n₂ sans unité ; incidence en degrés depuis la normale
- r en degrés ; R et T sont des fractions de puissance, distinctes des amplitudes de champ

**Hypothèses de l’expérience**

- Deux milieux isotropes transparents, non magnétiques, interface plane
- Rayons géométriques ; les courbes s, p ne représentent pas un champ évanescent spatial complet

**Techniques à mobiliser**

- Projection d’un vecteur d’onde
- Trigonométrie et domaine d’arcsin
- Bilan normal de Poynting

**Prédire → expérimenter → justifier**

1. Pour air→verre n=1,50 à 40°, prévoir vers quel côté de la normale le rayon tourne ; calculer ensuite le seuil verre→air.
2. Comparer les trois préréglages et approcher progressivement l’incidence critique de 41,81° ; regarder séparément Rs et Rp.
3. Retrouver n₁sin i=n₂sin r et vérifier R+T=1 avant le seuil ; distinguer réflexion totale et absence de tout champ dans le second milieu.

**Niveaux et approfondissements**

- Sup : Descartes–Snell, angle à la normale, ordre de grandeur et réversibilité.
- Spé : Conditions aux limites, polarisation s/p, Fresnel et conservation du flux selon filière.
- Au-delà : Onde évanescente, décalage de Goos–Hänchen et réflexion totale frustrée.

Leçons de référence : 1, 2.

**Résultat attendu.** Un seuil justifié et une distinction claire entre orientation d’un rayon, amplitude et énergie.

### Laboratoire `lentille`

Suivre le passage entre image réelle, virtuelle et image à l’infini. Les constructions font attribuer un sens physique aux signes de la conjugaison plutôt qu’appliquer une formule à des distances toutes positives.

**Objets et unités**

- Focale affichée en mm : son signe est fourni par le choix convergente/divergente
- Distance objet positive s en mm, p=−s ; hauteur et ouverture en mm ; p′ et γ sont algébriques

**Hypothèses de l’expérience**

- Lentille mince dans l’air, régime paraxial
- Prolongements virtuels pointillés ; l’ouverture règle les rayons représentés, pas une diffraction calculée

**Techniques à mobiliser**

- Conjugaison orientée et grandissement
- Construction par rayons remarquables
- Limite au voisinage du plan focal

**Prédire → expérimenter → justifier**

1. Avec f′=80 mm, prévoir le signe de p′ pour s=200,80 et 50 mm avant de lancer les préréglages.
2. Comparer image réelle, loupe et objet au foyer ; passer ensuite à la lentille divergente avec le même objet.
3. Vérifier 1/p′−1/p=1/f′ et γ=p′/p ; expliquer quels segments sont des rayons et quels segments sont seulement prolongés.

**Niveaux et approfondissements**

- Sup : Gauss, conjugaison, lentille convergente et divergente ; techniques communes de première année.
- Spé : Newton, matrices ABCD et invariant de rayon, introduits si nécessaire.
- Au-delà : Systèmes épais, plans principaux et aberrations hors de Gauss.

Leçons de référence : 3, 4.

**Résultat attendu.** Trois images classées avec leurs signes et une explication de l’échec de projection d’une image virtuelle.

### Laboratoire `bessel`

Reconstituer un TP de détermination de focale : deux mises au point d’un même objet sur un écran fixe. Explorer aussi le seuil de Silbermann et distinguer incertitude propagée et facilité réelle de réglage.

**Objets et unités**

- D, f′, position et écart d en mm ; la commande de position est s/D sans unité
- σD, σd sont des incertitudes standards en mm ; u(f′) en mm et d/u(d) sans unité

**Hypothèses de l’expérience**

- Objet réel, écran fixe, lentille mince convergente
- Propagation linéaire d’incertitudes D, d indépendantes ; la difficulté de netteté n’est pas simulée comme un bruit automatique

**Techniques à mobiliser**

- Équation du second degré et discriminant
- Grandissements réciproques
- Dérivées partielles et incertitude composée

**Prédire → expérimenter → justifier**

1. Prévoir combien de mises au point existent pour D=800,480 et 400 mm avec f′=120 mm.
2. Utiliser les deux positions nettes, déplacer manuellement s/D, puis comparer Silbermann et le cas sans mise au point.
3. Démontrer f′=(D²−d²)/(4D), calculer u(f′) et expliquer pourquoi un petit d/u(d) rend deux positions difficiles à distinguer même si u(f′) n’augmente pas.

**Niveaux et approfondissements**

- Sup : Banc optique, Bessel/Silbermann, mesure et unités.
- Spé : Propagation d’incertitude, corrélation éventuelle et stratégie expérimentale.
- Au-delà : Estimation Monte-Carlo et biais du modèle de lentille mince.

Leçons de référence : 5, 6.

**Résultat attendu.** Une focale avec incertitude déclarée et une décision argumentée sur la distance objet–écran.

### Laboratoire `telescope`

Construire une lunette afocale pour un objet astronomique décrit par sa direction. Comparer grossissement, pupille de sortie et diffraction afin de comprendre ce qu’un changement d’oculaire améliore réellement.

**Objets et unités**

- fo, fe, Dobjectif et défaut de séparation en mm ; angle de l’astre en minutes d’arc
- λ₀ en nm ; grossissement sans unité ; repère angulaire de Rayleigh en secondes d’arc

**Hypothèses de l’expérience**

- Lunette de Kepler à deux lentilles minces ; rayons paraxiaux
- Pupille circulaire idéale pour le repère de diffraction ; turbulence et aberrations non incluses dans ce banc

**Techniques à mobiliser**

- Chaîne angle→hauteur→angle
- Matrices de séparation et afocalité
- Conversion radians/secondes d’arc

**Prédire → expérimenter → justifier**

1. Pour fo=1000 mm, fe=25 mm, calculer G et la séparation afocale ; prévoir l’effet de fe=10 mm.
2. Comparer ×40 et fort grossissement ; augmenter Dobjectif puis introduire un défaut de séparation de 5 mm.
3. Démontrer G=−fo/fe et Dsortie=Dobjectif/|G| ; expliquer pourquoi changer l’oculaire ne modifie pas 1,22λ₀/Dobjectif.

**Niveaux et approfondissements**

- Sup : Lunette, grossissement, image à l’infini et réglages de TP.
- Spé : Diffraction et échantillonnage au foyer ; calcul du défaut d’afocalité.
- Au-delà : Télescopes réfléchissants, seeing, optique adaptative et PSF instrumentale.

Leçons de référence : 7, 8, 35.

**Résultat attendu.** Une chaîne instrumentale où grossissement, collecte de lumière et résolution sont calculés séparément.

### Laboratoire `microscope`

Régler une image intermédiaire pour regarder sans accommodation et suivre l’amplification d’un détail micrométrique. L’ouverture numérique donne un second critère : agrandir davantage ne crée pas des détails transmis.

**Objets et unités**

- fo, fe, intervalle Δ et hauteur objet en mm ; déplacement de l’objet en μm
- NA sans unité, λ₀ en nm, résolution objet en μm ; G sans unité et puissance en m⁻¹

**Hypothèses de l’expérience**

- Objectif et oculaire minces, chaîne afocale de Gauss
- NA limitée à 0,35 dans le banc paraxial ; axes de la scène étirés pour rendre les deux échelles lisibles

**Techniques à mobiliser**

- Conjugaison de l’objectif
- Grandissement et grossissement commercial
- Comparaison de résolution ramenée au plan objet

**Prédire → expérimenter → justifier**

1. Avec fo=8 mm, Δ=160 mm, fe=25 mm, prévoir G et la distance de l’objet légèrement au-delà de fo.
2. Comparer les deux grossissements, puis déplacer l’objet de 20 μm ; modifier NA à oculaire fixé.
3. Retrouver γobjectif=−Δ/fo et G≈γobjectif×250 mm/fe ; expliquer ce que prédit 0,61λ₀/NA et ce que ce critère n’évalue pas.

**Niveaux et approfondissements**

- Sup : Microscope comme objectif et loupe ; réglage d’image intermédiaire du recueil.
- Spé : Diffraction, NA et échantillonnage ; conversion de μm aux mm.
- Au-delà : Objectifs à immersion, microscopes corrigés à l’infini et imagerie incohérente.

Leçons de référence : 9, 10.

**Résultat attendu.** Un réglage afocal calculé, puis un grossissement utile confronté à la résolution et à la défocalisation.

### Laboratoire `oeil`

Utiliser la rétine comme écran fixe pour comprendre accommodation et correction. Un même bilan de conjugaison explique une myopie, une hypermétropie et l’effet du diamètre pupillaire sur deux sortes de flou.

**Objets et unités**

- Distance objet en m ; rétine et pupille en mm
- Excès au repos, correction collée et accommodation en dioptries δ=m⁻¹ ; tache rétinienne en μm

**Hypothèses de l’expérience**

- Œil réduit à une lentille et espace image en air, pour isoler la conjugaison
- Correction en contact ; flou géométrique et repère diffractif sont des échelles, pas une prescription physiologique

**Techniques à mobiliser**

- Conjugaison à écran fixe
- Addition de vergences en contact
- Triangles semblables et comparaison de flous

**Prédire → expérimenter → justifier**

1. Avec rétine à 17 mm, prévoir l’accommodation ajoutée nécessaire pour un objet à 25 cm.
2. Utiliser objet proche, myopie puis myopie corrigée ; diviser ensuite le diamètre pupillaire par deux.
3. Établir Crequise=1/ℓ+1/s et le signe de la correction ; expliquer pourquoi fermer la pupille diminue la défocalisation mais augmente la diffraction.

**Niveaux et approfondissements**

- Sup : Vergence, accommodation et lentilles correctrices dans un modèle réduit.
- Spé : Bilan de chaîne, profondeur de champ et limites de résolution.
- Au-delà : Dioptres de l’œil, astigmatisme, aberrations et optique physiologique.

Leçons de référence : 11, 3, 35.

**Résultat attendu.** Une correction de signe justifié et un compromis de pupille compris à partir de deux lois d’échelle.

### Laboratoire `fibre`

Passer de la réflexion totale au cône d’acceptance d’une fibre, puis mesurer le retard d’un rayon incliné. Le nombre V ouvre un lien avec les modes sans présenter un dessin de rayons comme leur solution ondulatoire.

**Objets et unités**

- Indices cœur/gaine sans unité ; angle d’entrée dans l’air en degrés à l’axe
- Rayon en μm, longueur en m, λ₀ en nm ; temps axial/incliné en μs, étalement en ns ; NA et V sans unité

**Hypothèses de l’expérience**

- Fibre droite à saut d’indice, rayons méridiens ; guidage seulement si ncœur>ngaine
- V est un repère de théorie ondulatoire faiblement guidante ; modes, courbures et pertes ne sont pas calculés

**Techniques à mobiliser**

- Deux applications de Snell
- Trigonométrie d’un trajet en zigzag
- Nombres sans dimension et changement de régime

**Prédire → expérimenter → justifier**

1. Pour n₁=1,48, n₂=1,46, calculer NA et l’angle d’entrée limite avant de tracer le rayon.
2. Comparer entrée de 8° et de 25° ; doubler la longueur puis sélectionner le repère monomode.
3. Démontrer n₀sinθmax=√(n₁²−n₂²) et Δt=n₁L(1/cosθ−1)/c ; distinguer acceptance et seuil V<2,405.

**Niveaux et approfondissements**

- Sup : Réflexion totale et fibre, grand classique du recueil.
- Spé : Dispersion intermodale et ordre de grandeur temporel ; introduction du nombre V.
- Au-delà : Modes cylindriques, gradient d’indice, dispersion chromatique et télécommunications.

Leçons de référence : 12, 13.

**Résultat attendu.** Une entrée acceptée ou rejetée selon un calcul, accompagnée d’un retard et d’une limite explicite du modèle de rayons.

### Laboratoire `mirage`

Retrouver la parabole du profil d’indice du recueil à partir d’un invariant, puis lire le point bas et la position apparente d’un rayon. La comparaison analytique/numérique donne un contrôle de résolution d’équation.

**Objets et unités**

- n₀ sans unité ; échelle a, altitude z₀ et distance x en m
- Angle initial en degrés à l’horizontale ; invariant ncosθ et écart numérique sans unité ou dans l’unité affichée

**Hypothèses de l’expérience**

- n(z)=n₀√(1+z/a), a>0, domaine z≥0
- Profil stylisé ; trajectoire interrompue au sol, les prolongements apparents ne transportent pas de lumière

**Techniques à mobiliser**

- Intégrale première par invariance
- Intégration d’une courbure constante
- Point stationnaire et vérification numérique

**Prédire → expérimenter → justifier**

1. Avec a=20000 m, z₀=2 m, θ₀=−0,5°, prévoir si le rayon touche le sol ou remonte avant.
2. Observer le point bas du préréglage descendant puis le cas qui rencontre le sol ; augmenter a vers 10⁶ m.
3. Retrouver ncosθ constant et vérifier que le coefficient de x² est 1/[4(a+z₀)cos²θ₀] ; comparer la tangente apparente à la courbe réelle.

**Niveaux et approfondissements**

- Sup : Trigonométrie, dérivation et intégration ; entrée progressive vers un milieu non homogène.
- Spé : Loi du rayon, invariant, modèle atmosphérique et contrôle d’erreur.
- Au-delà : Eikonale, Hamiltonien optique et profils d’indice mesurés.

Leçons de référence : 14, 18.

**Résultat attendu.** Une trajectoire démontrée, un point bas calculé et un arrêt au sol interprété sans prolonger le domaine physique.

### Laboratoire `arcenciel`

Faire apparaître une caustique par stationnarité de la déviation, puis relier la dispersion à l’ordre des couleurs. Le rayon dans la goutte et le graphe D(i) donnent deux lectures complémentaires d’un même phénomène.

**Objets et unités**

- Incidence en degrés ; une ou deux réflexions internes
- λ₀ en nm ; Cauchy n=a+b/λ² avec b en μm² ; déviation et rayon antisolaire en degrés

**Hypothèses de l’expérience**

- Goutte sphérique transparente dans l’air ; dispersion de Cauchy sur le visible
- Optique géométrique : la divergence idéale de caustique n’est pas une intensité ondulatoire infinie

**Techniques à mobiliser**

- Composition de déviations
- Dérivée de Snell et stationnarité
- Différentielle d’une déviation spectrale

**Prédire → expérimenter → justifier**

1. À n≈4/3, prévoir le rayon du primaire et vérifier que la déviation D est proche de 138°, pas de 42°.
2. Comparer rouge/violet du primaire puis le secondaire ; déplacer i autour de l’incidence stationnaire.
3. Établir sin²i*=[(p+1)²−n²]/[(p+1)²−1] et expliquer l’ordre inverse des couleurs pour le secondaire.

**Niveaux et approfondissements**

- Sup : Snell, goutte et trigonométrie du grand classique proposé.
- Spé : Caustique, dérivation implicite et dispersion ; lien avec polarisation de Fresnel.
- Au-delà : Airy de caustique, arcs surnuméraires et diffusion de Mie.

Leçons de référence : 15, 2.

**Résultat attendu.** Une différence entre rayon angulaire de l’arc et déviation du rayon, avec un ordre des couleurs justifié.

### Laboratoire `prisme`

Reconstituer la recherche du minimum au goniomètre, convertir une déviation en indice et confronter plusieurs couleurs à Cauchy. Le cas sans émergence apprend à vérifier les domaines trigonométriques.

**Objets et unités**

- A, i, D en degrés ; λ₀ en nm
- n=a+b/λ², a sans unité et b en μm² ; indice déduit au minimum sans unité

**Hypothèses de l’expérience**

- Prisme dans l’air, deux faces planes et milieu transparent
- Cauchy utilisée seulement dans la fenêtre visible ; un trajet peut subir réflexion totale à la seconde face

**Techniques à mobiliser**

- Trigonométrie de deux interfaces
- Recherche d’un minimum par symétrie
- Ajustement linéaire en 1/λ²

**Prédire → expérimenter → justifier**

1. Pour A=60° et n=1,50, prévoir Dmin et l’incidence correspondante.
2. Balayer i de part et d’autre du minimum, comparer 450 et 700 nm, puis observer le préréglage sans émergence.
3. Retrouver n=sin[(A+Dmin)/2]/sin(A/2), préciser les unités de b et proposer une lecture de goniomètre limitant les erreurs.

**Niveaux et approfondissements**

- Sup : Prisme et réglages collimateur/lunette du TP ; déviation minimale.
- Spé : Propagation d’erreur angulaire et mesure spectrale d’un indice.
- Au-delà : Dispersion de Sellmeier et résonances hors du domaine de Cauchy.

Leçons de référence : 16.

**Résultat attendu.** Un indice mesurable depuis un retournement de raie et un contrôle de validité à chacune des faces.

### Laboratoire `aberrations`

Comparer un miroir sphérique et un paraboloïde pour un faisceau axial. Le tracé exact rend visible l’aberration sphérique, son atténuation paraxiale et le stigmatisme axial de la parabole sans les confondre avec la diffraction.

**Objets et unités**

- R en mm ; demi-ouverture/R et position d’écran −x/R sans unité
- Sommet x=0, centre sphérique x=−R ; interceptions et positions focales en mm

**Hypothèses de l’expérience**

- Réflexion géométrique exacte d’un faisceau parallèle à l’axe
- Aucune diffraction, aucun calcul de coma hors axe ; le paraboloïde est stigmatique seulement pour la configuration axiale étudiée

**Techniques à mobiliser**

- Normale d’une courbe et réflexion vectorielle
- Développement limité d’une surface
- Égalité de chemins optiques

**Prédire → expérimenter → justifier**

1. Prévoir ce que devient le foyer des rayons marginaux d’une sphère par rapport à −R/2.
2. Comparer sphère à ouverture/R=0,45 puis 0,05 ; déplacer l’écran et choisir la parabole avec la grande ouverture.
3. Montrer x(y)=−y²/(2R)−y⁴/(8R³)+… pour la sphère et prouver x+PF=R/2 pour le paraboloïde.

**Niveaux et approfondissements**

- Sup : Miroir, normale, loi de réflexion et limite de Gauss.
- Spé : Aberration longitudinale, DL et comparaison d’un modèle exact à une approximation.
- Au-delà : Conception de télescopes, coma hors axe et combinaison aberrations/diffraction.

Leçons de référence : 17, 35.

**Résultat attendu.** Une erreur géométrique quantifiée et un succès axial du paraboloïde dont les limites sont précisées.

### Laboratoire `fermat`

Faire naître Snell d’une optimisation du temps de trajet. La position de traversée volontairement imparfaite permet de comparer un segment plus court à un chemin plus rapide, avec une preuve de convexité.

**Objets et unités**

- Séparation X, altitude h₁ et profondeur h₂ en cm ; point de passage x/X sans unité
- n₁, n₂ sans unité ; chemin optique converti en longueur et durée L/c

**Hypothèses de l’expérience**

- Deux milieux homogènes séparés par une interface plane
- Un trajet à deux segments, minimum unique ici ; le principe général est une stationnarité

**Techniques à mobiliser**

- Dérivation d’une fonction de position
- Convexité et unicité d’un optimum
- Traduction d’une dérivée en angles de Snell

**Prédire → expérimenter → justifier**

1. À indices égaux, h₁=8 cm, h₂=5 cm, X=20 cm, calculer la traversée du segment direct.
2. Comparer indices égaux puis n₂=1,50 ; déplacer le passage manuel autour du minimum indiqué.
3. Dériver L(x), identifier n₁sin i−n₂sin r et montrer L″>0 ; relier cet invariant au rayon courbe du mirage.

**Niveaux et approfondissements**

- Sup : Optimisation à une variable, racines et interprétation du chemin optique.
- Spé : Principe de Fermat, unicité et intégrales premières.
- Au-delà : Calcul variationnel, Hamiltonien et points conjugués.

Leçons de référence : 18, 14.

**Résultat attendu.** Une loi de réfraction dérivée d’un minimum et une démonstration de l’unicité pour cette géométrie.

### Laboratoire `young`

Identifier séparément franges d’interférence et enveloppe de diffraction. Le laboratoire montre aussi qu’un minimum non noir peut venir d’un déséquilibre, et qu’une somme d’intensités sans corrélation garde de la lumière.

**Objets et unités**

- λ en nm ; séparation a et largeur b en mm ; D en m
- I₂/I₁ sans unité ; phase additionnelle en degrés ; x et interfrange en mm

**Hypothèses de l’expérience**

- Fraunhofer paraxial, fentes uniformes de même largeur
- Source commune et polarisation compatible en mode cohérent ; sources indépendantes sans terme croisé

**Techniques à mobiliser**

- Différence de marche et phase
- Somme d’amplitudes complexes
- Deux lois d’échelle i=λD/a et L=2λD/b

**Prédire → expérimenter → justifier**

1. Pour λ=600 nm, D=2 m, a=0,50 mm, b=0,040 mm, prévoir interfrange et premiers zéros d’enveloppe.
2. Doubler a puis b séparément ; comparer déséquilibre I₂/I₁=0,10, sources indépendantes et une seule fente.
3. Retrouver visibilité 2√ρ/(1+ρ), déplacement dû à 90° de phase et maxima manquants dans l’enveloppe.

**Niveaux et approfondissements**

- Sup : Superposition, phase, interfrange et acquisition de courbes.
- Spé : Diffraction de fentes, cohérence et contraste ; statut des chapitres selon filière.
- Au-delà : Interférence de particules et corrélation mutuelle de champs partiellement cohérents.

Leçons de référence : 19, 20, 27.

**Résultat attendu.** Deux échelles mesurées et une cause de perte de contraste identifiée sans confusion avec un changement d’interfrange.

### Laboratoire `reseau`

Résoudre un doublet grâce à la largeur des maxima d’un ensemble de fentes. Augmenter N affine les pics ; changer l’ordre m augmente la dispersion, sous réserve que cet ordre existe et soit transmis par l’enveloppe.

**Objets et unités**

- λ centrale et écart du doublet en nm ; pas d en μm ; N entier et fraction ouverte b/d
- Incidence en degrés ; ordre m entier ; λ/Δλ et mN sans unité

**Hypothèses de l’expérience**

- N fentes identiques éclairées uniformément, Fraunhofer
- Deux raies indépendantes sommées en intensité ; Rayleigh idéal sans bruit ni aberrations

**Techniques à mobiliser**

- Somme géométrique complexe
- Limite amovible du quotient de sinus
- Comparaison séparation/largeur et critère de Rayleigh

**Prédire → expérimenter → justifier**

1. Pour 589,3 nm et Δλ=0,60 nm, estimer combien de fentes il faut à l’ordre 1 puis à l’ordre 2.
2. Comparer N=100, le voisinage N=982 puis l’ordre 2 ; choisir le préréglage d’ordre absent.
3. Démontrer d(sinθ−sinθ₀)=mλ, montrer Ipic∝N² et expliquer l’effet de l’enveloppe b/d sur les ordres manquants.

**Niveaux et approfondissements**

- Sup : Interférence de plusieurs sources après introduction guidée d’une somme complexe.
- Spé : Réseaux, dispersion et pouvoir spectral R≈mN selon filière.
- Au-delà : Éclairement apodisé, largeur de raie, blaze et instruments spectrographiques.

Leçons de référence : 21, 22.

**Résultat attendu.** Un seuil de résolution estimé et une distinction entre ordre absent géométriquement et ordre supprimé par diffraction.

### Laboratoire `diffraction`

Reconstruire la forme d’une figure depuis une pupille, puis découvrir le compromis d’apodisation. Les premiers zéros et le bilan de transmission obligent à distinguer demi-largeur, largeur totale et normalisation au pic.

**Objets et unités**

- Largeur a et hauteur b de pupille en mm ; λ en nm ; focale en mm
- Coordonnées focales en mm ; transmittance cosinus d’amplitude ; intensité relative au pic et énergie transmise

**Hypothèses de l’expérience**

- Diffraction scalaire de Fraunhofer au plan focal, illumination uniforme
- Apodisation t=cos(πx/a) sur |x|≤a/2 ; valeurs amovibles prolongées, pas mises à zéro

**Techniques à mobiliser**

- Intégrale d’une exponentielle
- Séparation d’une transformée bidimensionnelle
- Comparaison lobes centraux/lobes secondaires/puissance

**Prédire → expérimenter → justifier**

1. Pour a=0,20 mm, b=0,80 mm, f=300 mm, λ=600 nm, prévoir quel axe de la tache sera le plus large.
2. Comparer rectangle et fente ; choisir l’apodisation avec la même largeur et regarder le premier zéro.
3. Intégrer la pupille, retrouver la demi-largeur λf/a puis 3λf/(2a) apodisée et montrer que la transmission totale cosinus vaut 1/2.

**Niveaux et approfondissements**

- Sup : Superposition et intégration après introduction du principe de diffraction.
- Spé : Fraunhofer, pupille rectangulaire et transmittance ; programme selon filière.
- Au-delà : Fenêtrage, apodisation optimisée et compromis résolution/contraste.

Leçons de référence : 22, 23.

**Résultat attendu.** Des dimensions de pupille retrouvées depuis les zéros, et un compromis d’apodisation argumenté avec son coût en flux.

### Laboratoire `polarisation`

Transformer puis analyser un état du champ électrique. L’ellipse, les composantes et la sphère de Poincaré permettent de relier un calcul Jones à une mesure au polariseur, y compris un état circulaire sans extinction directe.

**Objets et unités**

- Angles d’entrée, de lame et d’analyseur en degrés ; retardance δ en degrés
- Jones normalisé, transmission sans unité ; Stokes S₁/S₀, S₂/S₀, S₃/S₀ sur la sphère

**Hypothèses de l’expérience**

- État monochromatique entièrement polarisé ; lame idéale sans pertes
- Convention exp(−iωt), seconde composante multipliée par exp(iδ), S₃=2Im(Ex*Ey)

**Techniques à mobiliser**

- Projection et loi de Malus
- Changement de base et matrice unitaire
- Ellipse paramétrée et invariance de norme

**Prédire → expérimenter → justifier**

1. Prévoir l’état issu d’une droite à 45° et d’une lame à δ=90° ; calculer la transmission attendue d’un analyseur.
2. Comparer quart d’onde, demi-onde, état circulaire et extinction ; tourner l’analyseur sans changer l’état avant lui.
3. Retrouver la matrice de lame et les Stokes ; proposer le protocole analyseur+lame qui distingue cercle et lumière non polarisée.

**Niveaux et approfondissements**

- Sup : Malus, projection vectorielle et contrôle d’un état rectiligne.
- Spé : Lames à retard et détermination de polarisation, notamment TP de la filière PC.
- Au-delà : Jones, Poincaré, Stokes partiels et lien au qubit de polarisation.

Leçons de référence : 24, 25.

**Résultat attendu.** Une transformation expliquée par ses composantes et une mesure de transmission, avec convention du sens de rotation déclarée.

### Laboratoire `michelson`

Passer du montage à sa différence de marche et à son plan d’observation. Les anneaux d’inclinaison et les franges de coin donnent deux méthodes de mesure distinctes, avec le facteur deux d’un aller-retour.

**Objets et unités**

- λ en nm ; écart miroir e en μm ; angle α du coin en mrad
- Focale et coordonnées d’observation en mm ; champ en degrés ; phase additionnelle en degrés

**Hypothèses de l’expérience**

- Source monochromatique et bras cohérents ; compensation de verre idéale
- Anneaux dans un plan focal ; coin dans un plan image adapté, géométrie de petits angles

**Techniques à mobiliser**

- Calcul de chemin optique aller-retour
- Développement de cos i
- Identification du plan de localisation

**Prédire → expérimenter → justifier**

1. Prévoir le nombre de franges pour une translation de 100 μm à λ=546 nm et le changement de rayons au carré.
2. Comparer anneaux, contact optique et coin ; doubler l’inclinaison du coin en conservant λ.
3. Démontrer δ=2e cos i puis δ≈δ₀+2αx ; dire pourquoi l’axe radial du foyer et x d’un coin n’ont pas le même sens physique.

**Niveaux et approfondissements**

- Sup : Interférences à deux trajets et notion de différence de marche introduites progressivement.
- Spé : Michelson, lame d’air, coin, réglages expérimentaux et mesure selon filière.
- Au-delà : Spectroscopie de Fourier et enveloppe de lumière blanche dans Cohérence.

Leçons de référence : 26, 27, 28.

**Résultat attendu.** Une méthode de mesure choisie avec son plan d’observation et un facteur deux vérifié.

### Laboratoire `coherence`

Expliquer une perte de visibilité à partir du spectre ou de la taille de source. Le doublet montre des retours de contraste, contrairement à l’enveloppe gaussienne : une première annulation ne résume pas la cohérence.

**Objets et unités**

- λ et écart de doublet en nm ; largeur FWHM Δν en GHz ; différence de marche en mm
- Largeur source s et séparation a en mm ; Ds en m ; visibilité et γ normalisés

**Hypothèses de l’expérience**

- Raies indépendantes spectralement ; spectre gaussien ou deux raies fines égales
- Source spatiale uniforme, points indépendants et géométrie paraxiale ; contributions temporelle/spatiale séparables

**Techniques à mobiliser**

- Transformée de Fourier d’un spectre
- Somme trigonométrique et battements
- Produit de corrélations et choix d’un seuil de visibilité

**Prédire → expérimenter → justifier**

1. Avec Δν=20 GHz, prévoir l’ordre de longueur c/Δν ; pour le doublet 0,60 nm, prévoir une annulation plus rapprochée.
2. Balayer δ avec la source ponctuelle, comparer gaussien et doublet, puis élargir la source et utiliser sources indépendantes.
3. Calculer V=exp[−π²Δν²(δ/c)²/(4ln2)], les annulations du doublet et le premier zéro as=λDs ; distinguer les trois causes testées.

**Niveaux et approfondissements**

- Sup : Phase, contraste et somme de signaux ; entrée accompagnée en cohérence.
- Spé : Cohérence temporelle et spatiale, doublet du recueil et diagnostics de TP.
- Au-delà : Wiener–Khintchine et Van Cittert–Zernike avec profils de sources plus généraux.

Leçons de référence : 27, 28, 19.

**Résultat attendu.** Une perte de contraste diagnostiquée par des réglages indépendants et un seuil de cohérence clairement défini.

### Laboratoire `fabryperot`

Voir comment de nombreux trajets résonnent et apprendre à lire une finesse spectrale. Les pics étroits demandent de vérifier également répétition d’ordre, angle interne et différence entre coefficient d’Airy et finesse.

**Objets et unités**

- Épaisseur e en mm, indice n et réflectivité R sans unité ; λ₀ en nm
- Angle interne en degrés ; désaccord/ISL sans unité ; ISL et largeur affichées en GHz ; finesse sans unité

**Hypothèses de l’expérience**

- Deux miroirs identiques sans absorption ; série stationnaire d’amplitudes
- n constant sur la fenêtre, angle interne connu ; le coefficient F=4R/(1−R)² diffère de ℱ spectrale

**Techniques à mobiliser**

- Série géométrique complexe
- Largeur à mi-hauteur
- Séparation fréquence/longueur d’onde/ordre

**Prédire → expérimenter → justifier**

1. Prévoir transmission en résonance pour R=0,85, puis distinguer ce résultat de la transmission d’un miroir seul.
2. Comparer résonance, antirésonance, haute finesse et R=0 ; doubler e puis changer l’angle interne.
3. Retrouver la loi d’Airy, calculer ISL=c/(2ne cosθ) et ℱ ; expliquer ce que les réglages de R et e changent séparément.

**Niveaux et approfondissements**

- Sup : Sommes complexes après introduction des deux trajets de Michelson.
- Spé : Interférences multiples et résonances ; prolongement accompagné selon filière.
- Au-delà : Pertes, indice de groupe, spectroscopie haute résolution et cavités optomécaniques.

Leçons de référence : 29, 30.

**Résultat attendu.** Un pic caractérisé par trois nombres distincts : position, intervalle libre et largeur.

### Laboratoire `fourier`

Construire un véritable filtrage du champ d’un objet. Une image de phase et les bilans de Parseval font distinguer amplitude, phase, intensité, contraste et énergie, au-delà d’un simple effet de flou sur une photographie.

**Objets et unités**

- Fréquence de coupure en mm⁻¹ ; pas objet en μm ; λ₀ en nm ; focale en mm
- Objet complexe E ; image |E|² ; spectre affiché logarithmiquement ; puissance relative sans unité

**Hypothèses de l’expérience**

- Montage 4f cohérent paraxial, masque passif |H|≤1
- FFT unitaire sur grille finie périodisée ; intensités avant/après affichées avec une échelle commune

**Techniques à mobiliser**

- Transformée et coordonnées du plan focal
- Norme de champ et théorème de Parseval
- Échantillonnage et fréquence de Nyquist

**Prédire → expérimenter → justifier**

1. Avec λ=600 nm, f=200 mm, prévoir où se trouve une modulation de période 50 μm dans le plan de Fourier.
2. Comparer aucun masque, passe-bas, passe-haut, fente verticale ; choisir ensuite l’objet de phase et suivre son contraste.
3. Vérifier le bilan identité puis masque passif ; calculer fNyquist et expliquer pourquoi on filtre le champ avant de prendre son module au carré.

**Niveaux et approfondissements**

- Sup : Sinusoïdes, dimensions et lecture d’une image ; notion de fréquence spatiale guidée.
- Spé : Diffraction et transformée de pupille selon filière ; lien à l’informatique scientifique.
- Au-delà : Filtrage cohérent, contraste de phase, fonctions de transfert et problèmes inverses.

Leçons de référence : 31, 32, 22.

**Résultat attendu.** Une transformation d’image interprétée avec sa fréquence physique et un bilan de puissance qui résiste à la normalisation visuelle.

### Laboratoire `laser`

Séparer la stabilité du trajet paraxial et l’apparition d’une oscillation entretenue. Le gain saturé fournit ensuite une puissance limitée et met le rôle du coupleur en relation avec la perte de cavité.

**Objets et unités**

- L en mm ; courbures 1/R en m⁻¹ ; réflectivités de puissance sans unité
- Gain g₀ et perte α en m⁻¹ d’intensité ; Ps et puissance en W ; λ₀ en nm

**Hypothèses de l’expérience**

- Cavité paraxiale à deux miroirs, gain uniforme saturant g(P)=g₀/(1+P/Ps)
- Critère de stabilité intérieur strict ; confocal classé marginal par ce test, ses modes ne sont pas déclarés inexistants

**Techniques à mobiliser**

- Matrice aller-retour et valeurs propres
- Condition de seuil logarithmique
- Bilan gain/pertes et saturation

**Prédire → expérimenter → justifier**

1. Avec L=200 mm et courbures 2 m⁻¹, prévoir g₁g₂ puis le seuil avec réflectivités 0,99 et 0,90.
2. Comparer gain suffisant et insuffisant à géométrie fixe ; choisir l’instabilité avec miroir convexe puis le confocal marginal.
3. Retrouver gseuil=α−ln(R₁R₂)/(2L), P=Ps(g₀/gseuil−1) et identifier les sujets absents du modèle : bruit, multimode, dynamique des populations.

**Niveaux et approfondissements**

- Sup : Exponentielle, logarithme et bilan d’amplification introduits progressivement.
- Spé : ABCD, résonance et émission stimulée ; entrée guidée hors programme commun.
- Au-delà : Modes propres, rate equations, compétition modale et oscillations de relaxation.

Leçons de référence : 33, 4, 30.

**Résultat attendu.** Deux décisions indépendantes — confinement et seuil — puis une puissance saturée dont la source d’énergie est identifiée.

### Laboratoire `gaussien`

Relier un petit waist à une grande divergence et contrôler que l’élargissement ne perd pas de puissance. La courbure et la phase de Gouy révèlent ce que le simple dessin de rayons ne contient pas.

**Objets et unités**

- Rayon w₀ à 1/e² en μm, λ₀ en nm, indice n sans unité et P en mW
- Plan z/zR sans unité ; w, zR et courbure dans les unités affichées ; I en W·m⁻² et Gouy affiché en degrés

**Hypothèses de l’expérience**

- TEM₀₀ paraxial dans un milieu homogène transparent
- Rayon d’intensité w, pas diamètre ; aucun diaphragme ni perte ; fronts et enveloppe représentés à des échelles annoncées

**Techniques à mobiliser**

- Intégrale radiale de puissance
- Lois d’échelle w₀, zR, divergence
- Phase complexe et limite au waist

**Prédire → expérimenter → justifier**

1. Pour w₀=50 μm, λ₀=633 nm, n=1, prévoir zR et le changement d’intensité axiale à z=zR.
2. Comparer waist, zR, puis petit et grand waist ; doubler P en conservant la géométrie.
3. Intégrer I(r, z) et vérifier P constant ; expliquer Rfront infini au waist, la phase de Gouy et la divergence accrue quand w₀ diminue.

**Niveaux et approfondissements**

- Sup : Gaussienne, intégrale et dimensions ; premier lien rayon/onde.
- Spé : Diffraction d’un faisceau fini et propagation d’enveloppe, prolongement accompagné.
- Au-delà : Paramètre q, ABCD gaussien, qualité M² et modes d’ordre supérieur.

Leçons de référence : 34, 33.

**Résultat attendu.** Un compromis de focalisation calculé et une puissance conservée malgré la baisse du maximum.

### Laboratoire `airy`

Tester la discernabilité de deux objets astronomiques ponctuels et comprendre une pupille annulaire. La somme de PSF de deux étoiles indépendantes rend visibles résolution et contraste sans inventer une phase commune.

**Objets et unités**

- D en mm, λ₀ en nm, séparation divisée par 1,22λ₀/D sans unité
- Rapport des flux et obstruction ε sans unité ; angle en secondes d’arc ; profils et taches d’intensité

**Hypothèses de l’expérience**

- Pupille circulaire ou annulaire idéale, points indépendants sans turbulence
- Le repère Rayleigh choisi est celui de la pupille pleine ; le zéro annulaire calculé peut différer, PSF de Webb non simulée

**Techniques à mobiliser**

- Transformée d’une pupille circulaire
- Somme d’intensités incohérentes
- Comparaison séparation/largeur/contraste

**Prédire → expérimenter → justifier**

1. À D=200 mm, λ₀=550 nm, calculer le repère Rayleigh et prévoir l’effet de D doublé.
2. Comparer séparation 1 puis 0,5, compagnon faible et obstruction ε=0,40 ; lire ensemble coupe et figure bidimensionnelle.
3. Expliquer le rôle de J₁ et le prolongement en u=0 ; montrer que l’obstruction perd la fraction ε² du flux et renforce les anneaux.

**Niveaux et approfondissements**

- Sup : Dimensions et conversion d’angles ; distinction collecte/grossissement.
- Spé : Diffraction circulaire et séparation de deux points, avec Bessel introduite si nécessaire.
- Au-delà : PSF réelle, estimation sous-Rayleigh, contraste de compagnon et déconvolution.

Leçons de référence : 35, 8.

**Résultat attendu.** Une comparaison de résolution qui tient compte du flux relatif et de la pupille, sans présenter Rayleigh comme frontière absolue.

### Laboratoire `nonlineaire`

Suivre la conversion du fondamental vers sa seconde harmonique et voir pourquoi la pompe constante finit par échouer. L’accord de phase relie une intégrale de champ, une loi sinc² et un bilan énergétique/photonique.

**Objets et unités**

- λω en nm, Iω en GW·cm⁻², d=χeff/2 en pm·V⁻¹, L en mm
- Indices effectifs sans unité ; Δk en mm⁻¹ réglé par orientation ; rendement et fractions d’énergie sans unité

**Hypothèses de l’expérience**

- Doublage dégénéré d’une seule pompe, ondes colinéaires, enveloppes lentes sans absorption
- Δk est un contrôle effectif indépendant des indices scalaires ; modèle faible seulement si η≪1, modèle couplé conserve |u|²+|v|²=1

**Techniques à mobiliser**

- Intégrale d’une exponentielle et sinc²
- Équations d’enveloppes couplées
- Manley–Rowe et conservation de l’énergie

**Prédire → expérimenter → justifier**

1. Pour 1064 nm, prévoir la longueur d’onde produite et le nombre de photons fondamentaux consommés par photon généré.
2. Comparer faible conversion et déplétion ; allonger L à accord parfait puis introduire Δk et regarder la reconversion.
3. Retrouver la loi η∝IωL²sinc²(ΔkL/2), identifier son échec si η>1 et vérifier Nω+2N2ω constant ; relier au PDF à deux pompes distinctes.

**Niveaux et approfondissements**

- Sup : Carré d’un sinus, énergie d’un photon et intégrale de phase, après introduction guidée.
- Spé : Réinvestissement de Maxwell et des ODE, mais la génération χ² n’est pas un acquis commun obligatoire.
- Au-delà : Accord birefringent, Manley–Rowe, déplétion, paramétrique et cristaux non linéaires.

Leçons de référence : 36, 34.

**Résultat attendu.** Un rendement borné dans le modèle couplé, une conversion spectrale et un bilan de photons dont la pondération est explicitée.

## Les 48 exercices corrigés

### 1. Deux sens de traversée

*Sup* — laboratoire `snell`.

**Énoncé.** Un rayon traverse air→verre n=1,50 sous 45°. Déterminer l’angle réfracté, la longueur d’onde dans le verre pour λ₀=600 nm et le seuil de réflexion totale dans le trajet inverse. Expliquer quelle grandeur reste inchangée à l’interface.

**Corrigé.** Snell donne sin r=sin45°/1,50, soit r≈28,13°. Dans le verre λ=600/1,50=400 nm tandis que ν=c/λ₀≈4,997×10¹⁴ Hz est inchangée : les conditions aux limites sont imposées à chaque instant. Pour verre→air, ic=arcsin(1/1,50)≈41,81°. Le trajet réciproque sous 28,13° sort sous 45° : il reste sous ce seuil. Mesurer les angles à la surface donnerait un résultat faux. La vitesse de phase et la longueur d’onde changent ensemble, sans modification de la fréquence.

### 2. Une interface transmet 96 %, pas 100 %

*Spé* — laboratoire `snell`.

**Énoncé.** À incidence normale air→verre n=1,50, établir r et t du champ électrique à partir de la continuité de E et H. Calculer R, T. Déterminer ensuite l’incidence de Brewster pour la polarisation p.

**Corrigé.** Les équations 1+r=t et n₁(1−r)=n₂t donnent r=(n₁−n₂)/(n₁+n₂)=−0,20 et t=2n₁/(n₁+n₂)=0,80. Donc R=0,040 et T=(n₂/n₁)t²=1,50×0,64=0,960 ; R+T=1. Le carré t² seul ne mesure pas une transmission de puissance : l’impédance diffère entre les milieux. Pour p, l’annulation de rp donne tan iB=n₂/n₁, d’où iB≈56,31°. Le faisceau s ne s’annule pas à cette incidence, ce qui permet d’obtenir une réflexion polarisée.

### 3. Une loupe produit-elle une image sur l’écran ?

*Sup* — laboratoire `lentille`.

**Énoncé.** Une lentille de f′=80 mm observe un objet de hauteur 12 mm situé à 50 mm devant elle. Calculer position, nature et taille de l’image. Refaire le calcul pour l’objet à 200 mm.

**Corrigé.** Les distances sont p=−50 mm et f′=+80 mm. p′=f′p/(p+f′)=−133,33 mm ; γ=p′/p=+2,6667, donc la hauteur est +32 mm. L’image est virtuelle et droite ; un écran placé au point apparent ne reçoit pas ces rayons convergents. À p=−200 mm, p′=133,33 mm, γ=−2/3 et A′B′=−8 mm : l’image est réelle, renversée et projetable. Les deux résultats ont le même |p′| par coïncidence des nombres ; leur signe décrit des situations optiques différentes.

### 4. Deux lentilles séparées : la somme des vergences échoue

*Sup → Spé* — laboratoire `lentille`.

**Énoncé.** Deux lentilles minces ont f′₁=100 mm et f′₂=200 mm, séparées de 100 mm dans l’air. Calculer M=L₂T(d)L₁ et la vergence équivalente. Expliquer pourquoi la focale équivalente ne localise pas directement le foyer depuis L₂.

**Corrigé.** En mètres, C₁=10 et C₂=5 δ. T a les coefficients A=D=1, B=0,10 m, C=0 ; le produit M=L₂TL₁ donne A=0, B=0,10 m, C=−10 m⁻¹, D=0,50. det M=0×0,50−0,10×(−10)=1. La vergence vaut −C=10 δ et f′équiv=100 mm. Pour une entrée parallèle uentrée=0, ysortie=A yentrée=0 : les rayons traversent l’axe au plan de L₂. Le foyer arrière est donc à ce plan, pas à 100 mm de L₂ ; cette dernière longueur se mesure depuis le plan principal image.

### 5. Mesure de Bessel et tailles réciproques

*Sup ; TP* — laboratoire `bessel`.

**Énoncé.** On mesure D=800 mm et deux positions de lentille séparées de d=400 mm. Calculer f′, les deux distances depuis l’objet et leurs grandissements. Quel test supplémentaire utiliser avec une mire graduée ?

**Corrigé.** f′=(D²−d²)/(4D)=(640000−160000)/3200=150 mm. Les positions sont (D−d)/2=200 mm et (D+d)/2=600 mm. À la première, l’image est à 600 mm de la lentille et γ=−600/200=−3 ; à la seconde γ=−200/600=−1/3. Les deux images sont renversées et γ₁γ₂=1. Mesurer les tailles d’un même intervalle de mire vérifie ce produit et la nature des deux réglages. Si D<4f′ aucune des deux positions réelles n’existe ; à D=4f′ elles se confondent à mi-distance.

### 6. Bessel : une incertitude calculée et une limite expérimentale

*Sup → Spé* — laboratoire `bessel`.

**Énoncé.** Pour D=800 mm, d=400 mm, u(D)=u(d)=1 mm indépendants, calculer u(f′). Interpréter l’idée de se rapprocher de D=4f′ pour diminuer la sensibilité à d.

**Corrigé.** f′=D/4−d²/(4D), donc fD=1/4+d²/(4D²)=0,3125 et fd=−d/(2D)=−0,25. L’incertitude standard est √[(0,3125)²+(0,25)²] mm≈0,400 mm. On rapporte (150,0±0,4) mm avec le statut standard de l’incertitude. Quand D→4f′, d→0 et fd→0, mais les deux mises au point deviennent indiscernables : u(d) n’a aucune raison de rester 1 mm. Un choix expérimental doit inclure la précision réelle de netteté, les corrélations de lecture et les limites du modèle mince.

### 7. Changer l’oculaire d’une lunette

*Sup* — laboratoire `telescope`.

**Énoncé.** Une lunette afocale possède fo=1000 mm et D=100 mm. Comparer les oculaires de 25 et 10 mm : séparation, grossissement et pupille de sortie. Un détail de 1 minute d’arc devient apparent sous quel angle ?

**Corrigé.** Avec fe=25 mm, d=1025 mm, G=−40 et la pupille de sortie vaut 100/40=2,50 mm. Avec fe=10 mm, d=1010 mm, G=−100 et la pupille vaut 1,00 mm. Le détail de 1 minute d’arc devient apparent sous 40 minutes puis 100 minutes d’arc, soit environ 0,667° et 1,667°, avec inversion. Il faut régler de nouveau l’écartement : conserver 1025 mm avec le second oculaire ne reste pas afocal. Le diamètre objectif inchangé garde la même limite de diffraction angulaire ; le fort grossissement peut simplement rendre un flou plus grand.

### 8. Un détecteur au foyer d’un télescope

*Sup → Spé* — laboratoire `telescope`.

**Énoncé.** Pour D=200 mm, f=2000 mm, λ₀=550 nm, déterminer la séparation de Rayleigh angulaire et sa taille au foyer. Un pixel de 10 μm représente-t-il correctement cette séparation ? Que change un doublement de f à D fixé ?

**Corrigé.** θR=1,22λ₀/D=3,355×10⁻⁶ rad≈0,692 seconde d’arc. Au foyer, s=fθR=6,71 μm. Un pixel de 10 μm est plus large que cette séparation : l’image est sous-échantillonnée à cette échelle, même si une modélisation de pixels peut parfois estimer une position. Avec f doublée, s=13,42 μm et le champ angulaire d’un pixel est divisé par deux ; θR reste inchangé car D ne change pas. L’angle de résolution, la taille physique de PSF et l’échantillonnage du détecteur répondent à trois paramètres distincts.

### 9. Régler un microscope afocal

*Sup ; TP* — laboratoire `microscope`.

**Énoncé.** Un microscope a fo=8 mm, fe=25 mm et Δ=160 mm. Trouver la position de l’objet donnant une image intermédiaire au foyer de l’oculaire, le grandissement de l’objectif et le grossissement commercial avec d₀=250 mm.

**Corrigé.** L’image intermédiaire est à p′=fo+Δ=168 mm de l’objectif. La conjugaison donne 1/p=1/168−1/8=−160/1344 mm⁻¹, soit p=−8,40 mm. Le grandissement exact du modèle mince vaut γ=p′/p=−20, égal ici à −Δ/fo. L’oculaire grossit par d₀/fe=10, donc G=−200. Un objet de 0,050 mm produit une image intermédiaire de −1,00 mm puis un angle d’environ 0,040 rad en valeur absolue. L’objet doit donc être légèrement au-delà du foyer, pas exactement au foyer, ce qui donnerait une image à l’infini avant l’oculaire.

### 10. Grossissement utile et résolution du microscope

*Spé* — laboratoire `microscope`.

**Énoncé.** Comparer à λ₀=550 nm les résolutions de Rayleigh pour NA=0,10 et 0,25. Un objectif ×20 avec pixels de 6,5 μm côté caméra échantillonne-t-il suffisamment le second cas ? Quel serait l’effet d’un oculaire plus grossissant sur NA ?

**Corrigé.** dR≈0,61λ₀/NA donne 3,355 μm pour NA=0,10 et 1,342 μm pour NA=0,25. Chaque pixel de la caméra représente 6,5/20=0,325 μm côté objet : le second détail couvre environ 4,13 pixels, une échelle raisonnablement échantillonnée dans ce modèle. L’oculaire ou un agrandissement supplémentaire change la taille apparente, pas la NA de l’objectif ni sa PSF ramenée à l’objet. Les valeurs supposent une pupille idéale et des points incohérents ; un objet périodique en illumination cohérente peut appeler un autre critère.

### 11. Accommodation à distance connue

*Sup* — laboratoire `oeil`.

**Énoncé.** Dans l’œil réduit à ℓ=17 mm, calculer les vergences requises à l’infini, à 1 m et à 25 cm. Un excès de vergence de +3 δ est-il compensé par une lentille convergente ou divergente en contact ?

**Corrigé.** La conjugaison à rétine fixe donne C=1/ℓ+1/s. À l’infini C=58,8235 δ ; à 1 m C=59,8235 δ ; à 25 cm C=62,8235 δ. L’accommodation ajoutée au repos normal est donc 0 δ, 1 δ et 4 δ respectivement. Un excès de +3 δ doit être compensé par −3 δ, une correction divergente en contact ; une convergence supplémentaire ferait avancer davantage le foyer. Le calcul utilise le modèle d’espace image en air et la correction collée ; une lentille distante de l’œil exige une composition de conjugaisons plutôt qu’une addition directe.

### 12. Pupille et défocalisation : fermer n’est pas toujours gagner

*Sup → Spé* — laboratoire `oeil`.

**Énoncé.** Un faisceau convergerait 0,50 mm devant une rétine à ℓ=17 mm. Pour une pupille de 4 mm, estimer le diamètre du flou géométrique. Comparer le diamètre de tache d’Airy à 550 nm avec cette valeur ; que change une pupille divisée par deux ?

**Corrigé.** Le foyer est à q=16,50 mm. Par triangles semblables, le diamètre géométrique à la rétine est b=D|ℓ−q|/q=4×0,50/16,50≈0,121 mm, soit 121 μm. L’Airy idéale a un diamètre entre premiers zéros 2,44λℓ/D≈5,70 μm : la défocalisation domine ici. Fermer à 2 mm divise le flou géométrique par deux mais double le diamètre diffractif à 11,4 μm. À forte fermeture et bonne mise au point, la diffraction finit donc par limiter le gain. Ces deux flous ne se somment pas universellement comme des diamètres ; leur comparaison donne des échelles.

### 13. Acceptance et seuil monomode

*Sup → Spé* — laboratoire `fibre`.

**Énoncé.** Une fibre idéale a n₁=1,48, n₂=1,46 et un rayon de cœur a=4 μm. Calculer NA, l’angle d’entrée maximal dans l’air et V à 1550 nm. Quelle limite sur a donnerait V<2,405 ?

**Corrigé.** NA=√(1,48²−1,46²)≈0,24249. L’angle d’entrée maximal est arcsin(NA)≈14,03°. V=2πaNA/λ₀≈3,932>2,405 : ce repère de fibre faiblement guidante ne garantit pas un régime monomode. Résoudre V<2,405 donne a<2,405λ₀/(2πNA)≈2,447 μm. La condition d’acceptance est géométrique ; le seuil 2,405 résulte de l’équation d’onde et de ses conditions aux limites cylindriques. Un rayon accepté dans une fibre très petite ne constitue pas à lui seul un calcul de mode.

### 14. Le guidage ne supprime pas la dispersion temporelle

*Sup → Spé* — laboratoire `fibre`.

**Énoncé.** Dans une fibre uniforme de longueur 1 km et d’indice 1,48, comparer le temps d’un rayon axial à celui d’un rayon guidé à θ=8° avec l’axe. Donner un développement au second ordre en θ et expliquer le principe d’un gradient d’indice.

**Corrigé.** Le temps axial vaut t₀=nL/c≈4,937 μs. Le rayon incliné parcourt L/cosθ, donc tθ=t₀/cos8° et Δt≈48,5 ns. Pour θ petit en radians, 1/cosθ=1+θ²/2+O(θ⁴), d’où Δt≈t₀θ²/2 ; avec θ≈0,1396, l’estimation donne environ 48,1 ns. La réflexion totale évite la fuite mais ne rend pas les longueurs égales. Un indice décroissant radialement fait parcourir les trajets éloignés dans un milieu plus rapide et peut compenser une partie de cet excès. Dispersion chromatique et pertes restent des mécanismes distincts.

### 15. Localiser le point bas d’un mirage

*Sup → Spé* — laboratoire `mirage`.

**Énoncé.** Pour n(z)=n₀√(1+z/a), prendre a=20000 m, z₀=2 m et θ₀=−0,5°. À partir de z(x)=z₀+x tanθ₀+Ax², déterminer A, le point bas et le retour à l’altitude initiale. Le rayon rencontre-t-il le sol ?

**Corrigé.** A=1/[4(a+z₀)cos²θ₀]≈1,2499702×10⁻⁵ m⁻¹. z′=tanθ₀+2Ax s’annule à x*=−tanθ₀/(2A)≈349,08 m. Le minimum est zmin=z₀−tan²θ₀/(4A)≈0,4768 m : il reste au-dessus du sol dans ce modèle. Le second passage à z=z₀ est x=−tanθ₀/A≈698,17 m. La valeur n₀ disparaît de la trajectoire car elle multiplie à la fois l’invariant et le profil ; elle reste dans le temps de parcours. Modifier a contrôle directement la courbure et peut changer l’interception du sol.

### 16. Vérifier une trajectoire sans intégrateur

*Spé* — laboratoire `mirage`.

**Énoncé.** Dériver depuis l’invariant n(z)cosθ=n(z₀)cosθ₀ la courbure z″ et vérifier le coefficient de x². Déterminer une condition algébrique pour qu’un rayon initialement descendant touche z=0.

**Corrigé.** Avec z′=tanθ, 1+z′²=1/cos²θ=(a+z)/[(a+z₀)cos²θ₀]. En dérivant hors du point bas puis en prolongeant continûment, z″=1/[2(a+z₀)cos²θ₀]. Une primitive avec z′(0)=tanθ₀ puis z(0)=z₀ donne A=1/[4(a+z₀)cos²θ₀], car (Ax²)″=2A. Le minimum vaut z₀−(a+z₀)sin²θ₀. Pour θ₀<0, une rencontre du sol est possible lorsque (a+z₀)sin²θ₀≥z₀, avec égalité pour une tangence. Une simulation physique du domaine z≥0 s’arrête à la première rencontre plutôt que continuer sous le sol.

### 17. Angle du premier arc-en-ciel

*Sup → Spé* — laboratoire `arcenciel`.

**Énoncé.** Pour une goutte d’indice n=4/3, établir l’incidence stationnaire du trajet à une réflexion et calculer le rayon de l’arc primaire autour du point antisolaire. Expliquer le rôle de D′=0.

**Corrigé.** D=π+2i−4r et sin i=n sin r donnent dr/di=cos i/(n cos r). D′=0 impose cos i/(n cos r)=1/2. En élevant au carré et utilisant sin²r=sin²i/n², 4(1−sin²i)=n²−sin²i, donc sin²i=(4−n²)/3. Pour n=4/3, i≈59,39°, r≈40,20° et Dmin≈137,970°. Le rayon antisolaire est 180°−Dmin≈42,030°. D′=0 concentre les incidences voisines dans une petite plage de directions, une caustique ; la diffraction et la source finie bornent la luminosité réellement observée.

### 18. Pourquoi le rouge est-il à l’extérieur ?

*Spé* — laboratoire `arcenciel`.

**Énoncé.** Au rayon stationnaire primaire pour n=4/3, calculer ∂D/∂n. Estimer la variation du rayon antisolaire lorsque l’indice augmente de 0,006. Donner le sens du déplacement sans confondre déviation et rayon de l’arc.

**Corrigé.** À i fixé, cos r ∂r/∂n=−sin r/n, donc ∂r/∂n=−tanr/n. D=π+2i−4r donne ∂D/∂n=4tanr/n≈2,53546 rad par unité d’indice au point stationnaire. Le déplacement d’i* ne contribue pas au premier ordre puisque ∂D/∂i=0. Pour Δn=0,006, ΔD≈0,01521 rad≈0,872°. Le rayon antisolaire β=π−D diminue donc d’environ 0,872°. Le violet possède l’indice plus grand et se place à l’intérieur du primaire ; le rouge à l’extérieur. L’ordre est inversé dans l’arc secondaire à deux réflexions.

### 19. Retrouver l’indice avec un goniomètre

*Sup ; TP* — laboratoire `prisme`.

**Énoncé.** Un prisme d’angle A=60° donne Dmin=40°. Calculer n et l’incidence au minimum. Estimer la variation d’indice associée à une erreur de 0,10° sur Dmin, A étant supposé exact.

**Corrigé.** Le trajet symétrique a r=r′=30° et i=i′=(A+Dmin)/2=50°. n=sin50°/sin30°≈1,532089. À A fixé, ∂n/∂Dmin=cos[(A+Dmin)/2]/[2sin(A/2)]≈0,642788 rad⁻¹. Une erreur de 0,10°=1,74533×10⁻³ rad donne Δn≈1,122×10⁻³. Utiliser directement 0,10 dans la dérivée en radians surestimerait l’erreur d’un facteur 180/π. Le minimum se repère par un retournement de la raie, puis les lectures de deux orientations peuvent limiter certaines erreurs d’alignement.

### 20. Cauchy : un ajustement avec unités

*Sup → Spé* — laboratoire `prisme`.

**Énoncé.** On ajuste n(λ)=a+b/λ² avec λ en μm. Les mesures sont n(0,50)=1,496 et n(0,70)=1,4881633. Déterminer a, b puis n à 600 nm. Quel indice donnerait l’erreur consistant à insérer 600 sans conversion ?

**Corrigé.** La différence vaut b(1/0,50²−1/0,70²). Elle donne b≈0,004000 μm² puis a=n(0,50)−4b≈1,480000. À 600 nm=0,600 μm, n=1,48+0,004/0,600²≈1,491111. Insérer 600 tout en gardant b en μm² donnerait 1,480000011, presque sans dispersion, une erreur d’unités. Le tracé de n en fonction de 1/λ² doit être linéaire dans la fenêtre de validité du modèle. Une extrapolation à une fréquence résonante ou à l’absorption ne se justifie pas par ces deux points.

### 21. Un miroir sphérique rapproche les rayons marginaux

*Sup → Spé* — laboratoire `aberrations`.

**Énoncé.** Le miroir sphérique est x=−R+√(R²−y²), les rayons incidents vont vers +x. Montrer que l’intersection axiale du rayon de hauteur y est xf=−R+R/[2√(1−(y/R)²)]. Calculer xf pour y/R=0,05 et 0,45 avec R=400 mm.

**Corrigé.** Au point P, une normale unitaire est n̂=(√(1−q²), q), q=y/R. La réflexion de (1,0) donne v=(−1+2q²,−2q√(1−q²)). En posant xaxe=xP−y vx/vy et en simplifiant, xf=−R+R/[2√(1−q²)]. Pour q=0,05, xf≈−199,750 mm ; pour q=0,45, xf≈−176,043 mm. Le foyer paraxial est −R/2=−200 mm ; les rayons marginaux focalisent plus près du sommet. Le signe et l’origine x=0 sont essentiels : une distance positive au miroir décrirait les mêmes positions avec un signe opposé.

### 22. Un paraboloïde axial est exactement stigmatique

*Spé* — laboratoire `aberrations`.

**Énoncé.** Pour x=−y²/(2R), montrer qu’un front plan axial arrivant vers +x possède le même chemin géométrique jusqu’à F=(−R/2,0) pour chaque point P du miroir. En déduire le sens de la réflexion et discuter le hors axe.

**Corrigé.** La distance PF vérifie PF²=(x+R/2)²+y². En substituant x=−y²/(2R), on obtient PF=R/2+y²/(2R)=R/2−x. Depuis un front plan x=x₀ avant le miroir, le trajet vaut (x−x₀)+PF=R/2−x₀, indépendant de y. La normale de la surface bisecte alors la direction incidente et PF conformément à la réflexion : tous les rayons axiaux passent en F. Cette propriété est exacte en géométrie, mais une pupille finie diffracte encore. Hors axe, l’égalité de chemins démontrée n’est plus valable ; la coma peut dégrader l’image.

### 23. Fermat : démontrer le minimum, pas seulement le trouver

*Sup → Spé* — laboratoire `fermat`.

**Énoncé.** A et B sont à h₁=8 cm et h₂=5 cm de part et d’autre d’une interface ; leur séparation horizontale est X=20 cm. Pour des indices égaux, trouver le point de traversée et prouver son unicité. Que devient la position si seul n₂ augmente ?

**Corrigé.** L(x)=n₁√(x²+h₁²)+n₂√[(X−x)²+h₂²]. Quand n₁=n₂, L′=0 donne x/h₁=(X−x)/h₂, donc x=Xh₁/(h₁+h₂)=160/13≈12,3077 cm : c’est l’intersection du segment AB. Pour tout n₁, n₂>0, L″=n₁h₁²/(x²+h₁²)³ᐟ²+n₂h₂²/[(X−x)²+h₂²]³ᐟ²>0, donc le minimum est unique. Augmenter n₂ rend L′ négatif au point précédent ; le nouveau zéro se déplace vers x plus grand, réduisant la longueur horizontale dans le milieu lent. La longueur euclidienne peut augmenter tandis que la durée diminue.

### 24. Principe variationnel et invariant du mirage

*Spé → Au-delà accompagné* — laboratoire `fermat`.

**Énoncé.** Pour un indice n(z), écrire la fonctionnelle en paramètre x puis retrouver l’invariant horizontal par l’identité de Beltrami. Montrer comment on retrouve ncosθ et expliquer pourquoi Fermat parle en général de stationnarité.

**Corrigé.** Le chemin optique est L[z]=∫n(z)√(1+z′²) dx. L’intégrande ℒ ne dépend pas explicitement de x ; l’identité de Beltrami donne ℒ−z′∂ℒ/∂z′=n(z)/√(1+z′²)=constante. Comme z′=tanθ, il s’agit de ncosθ. Cette intégrale première donne la trajectoire du mirage sans résoudre immédiatement une équation vectorielle. δL=0 ne suffit pas à prouver un minimum : il faut examiner la seconde variation ou la géométrie. La fonction à deux segments du laboratoire est strictement convexe, mais d’autres systèmes optiques possèdent plusieurs trajets stationnaires ou des points conjugués.

### 25. Young : franges dans l’enveloppe

*Sup → Spé* — laboratoire `young`.

**Énoncé.** Pour λ₀=600 nm, D=2 m, a=0,50 mm, b=0,040 mm, calculer l’interfrange, les premiers zéros de diffraction et le nombre de maxima d’interférence strictement dans le lobe central. Que donne un doublement de a ?

**Corrigé.** i=λD/a=2,40 mm. Les zéros d’enveloppe sont à ±λD/b=±30,0 mm. Les maxima interférentiels sont x=ki avec k entier ; |k|<30/2,4=12,5 donne k=−12,…,12, donc 25 maxima dans le lobe central. Si a double, i devient 1,20 mm et |k|<25 ; on compte 49 maxima, les ordres ±25 tombant exactement sur les zéros et étant manquants. La largeur totale d’enveloppe reste 60 mm puisque b n’a pas changé. Un graphique doit donc faire voir deux échelles indépendantes, pas appeler interfrange la largeur de la tache diffractée.

### 26. Contraste, phase et sources indépendantes

*Sup → Spé* — laboratoire `young`.

**Énoncé.** Les deux fentes ont I₂=0,10I₁. Calculer visibilité, maximum et minimum. Une phase additionnelle de π/2 déplace les maxima de combien d’interfranges ? Comparer avec deux sources indépendantes.

**Corrigé.** V=2√0,10/1,10≈0,57496. Imax=(1+√0,10)²I₁≈1,73246I₁ et Imin=(1−√0,10)²I₁≈0,46754I₁. Avec φ(x)=2πx/i+φ₀, φ₀=π/2 impose xk=i(k−1/4), donc une translation de −i/4 selon cette convention. La visibilité reste la même. Deux sources indépendantes donnent ⟨cosφ⟩=0 : I=1,10I₁ multiplié par les enveloppes pertinentes, sans franges. La puissance moyenne ne disparaît pas quand la corrélation est supprimée. Une intensité déséquilibrée donne des minima non noirs même avec cohérence complète.

### 27. Résoudre le doublet du sodium avec un réseau

*Spé* — laboratoire `reseau`.

**Énoncé.** Un réseau de pas d=2 μm observe les raies 589,0 et 589,6 nm à incidence normale. Estimer l’angle de l’ordre 1, la séparation angulaire et le nombre minimal de fentes éclairées selon Rayleigh. Refaire le seuil à l’ordre 2.

**Corrigé.** À λm=589,3 nm, sinθ₁=λm/d=0,29465, donc θ₁≈17,137°. En différenciant d sinθ=mλ, Δθ≈mΔλ/(d cosθ)≈3,14×10⁻⁴ rad≈0,0180° à l’ordre 1. Le critère |m|N≥λm/Δλ donne N≥982,17, soit 983 fentes pour satisfaire strictement les valeurs arrondies ici. À l’ordre 2 il donne N≥491,08, soit 492 ; sinθ₂=0,5893 reste inférieur à 1. L’indication approximative 982 ou 491 décrit le voisinage du critère, mais une décision entière précise exige les longueurs d’onde et le seuil retenus.

### 28. Ordres manquants et pic du réseau

*Spé* — laboratoire `reseau`.

**Énoncé.** Un réseau comporte N fentes de pas d et de largeur b=d/2. Montrer que les ordres pairs non nuls sont supprimés par l’enveloppe. Évaluer la somme d’amplitudes exactement au maximum malgré son quotient apparent 0/0.

**Corrigé.** À l’ordre m, d sinθ=mλ et le facteur de fente vaut sinc(πb sinθ/λ)=sinc(πmb/d)=sinc(πm/2). Pour m=±2,±4,… il s’annule ; l’ordre zéro reste présent par prolongement sinc0=1. La somme ∑p=0…N−1exp(ipφ) vaut directement N à φ=2πm. Le quotient sin(Nφ/2)/sin(φ/2) a alors une limite de module N, donc l’intensité du facteur réseau vaut N². Mettre numérateur et dénominateur séparément à zéro créerait un pic absent artificiellement. Les ordres doivent encore satisfaire |sinθ|≤1 pour être propagatifs.

### 29. Rectangle : mesurer les deux dimensions d’une pupille

*Spé ; TP* — laboratoire `diffraction`.

**Énoncé.** Une pupille uniforme produit au foyer f=300 mm sous λ=600 nm ses premiers zéros à X=±0,90 mm et Y=±0,225 mm. Retrouver a, b et les largeurs totales centrales. Justifier l’orientation de la figure.

**Corrigé.** Les premiers zéros satisfont aX/(λf)=±1 et bY/(λf)=±1. Donc a=λf/0,90 mm=0,20 mm et b=λf/0,225 mm=0,80 mm. Les largeurs centrales sont 1,80 mm horizontalement et 0,450 mm verticalement. La pupille est quatre fois plus large verticalement, mais sa tache centrale est quatre fois plus étroite selon cette direction, conséquence du changement d’échelle de la transformée de Fourier. La position d’un premier zéro mesure une demi-largeur ; une largeur totale utilise les deux zéros symétriques, avec le facteur deux correspondant.

### 30. Apodisation : un faux zéro devient un point régulier

*Spé → Au-delà* — laboratoire `diffraction`.

**Énoncé.** Pour t(x)=cos(πx/a) sur |x|≤a/2, établir A(u)/A(0), u=πa sinθ/λ. Trouver I/I(0) à u=π/2, les premiers zéros et la puissance transmise relative à une fente uniforme.

**Corrigé.** Décomposer cos en deux exponentielles et intégrer donne A(u)=a(π/2)cosu/(π²/4−u²), donc A/A(0)=(π²/4)cosu/(π²/4−u²). À u→π/2, l’Hôpital donne cosu/(π²/4−u²)→1/π ; A/A(0)→π/4 et I/I(0)=π²/16≈0,61685, une valeur non nulle. Les premiers vrais zéros sont u=±3π/2, donc sinθ=±3λ/(2a). La puissance transmise vaut ∫−a/2ᵃ/²cos²(πx/a)dx=a/2 contre a pour t=1 : elle est divisée par deux. Des tracés normalisés au pic doivent être accompagnés de ce bilan.

### 31. Produire une polarisation circulaire

*Sup → Spé* — laboratoire `polarisation`.

**Énoncé.** Avec exp(−iωt), l’entrée Jones normalisée est (cosθ, sinθ). Une lame d’axes x, y multiplie Ey par exp(iδ). Déterminer le résultat pour θ=45°, δ=90°, ses Stokes et la transmission par un analyseur quelconque.

**Corrigé.** Le champ devient (1, i)/√2. Les composantes réelles sont cosωt/√2 et sinωt/√2 : le vecteur décrit un cercle dans le plan transverse. S₀=1, S₁=0, S₂=0, S₃=2Im(Ex*Ey)=1. L’analyseur d’angle β reçoit (cosβ+i sinβ)/√2 ; son module au carré vaut 1/2 pour tout β. À θ=0 ou 90°, une seule composante existe et la lame ne produit pas de cercle. Pour attribuer gauche/droite, il faut aussi déclarer le sens d’observation ; les valeurs complexes et Stokes donnent ici une convention sans ambiguïté.

### 32. Une demi-onde tourne la polarisation

*Spé* — laboratoire `polarisation`.

**Énoncé.** Une entrée rectiligne fait 30° avec x. La lame demi-onde a son axe propre à 10° de x. Trouver l’orientation de sortie et la transmission d’un analyseur à 80°. Quel angle d’analyseur donne une extinction ?

**Corrigé.** Dans la base de la lame, l’entrée est à θ−α=20°. La retardance π change le signe de la seconde composante, donc l’angle relatif devient −20°. Après retour aux axes du banc, θsortie=α−20°=−10°, égal à 2α−θ. L’analyseur à 80° est orthogonal à cet état puisque 80°−(−10°)=90°, donc sa transmission est cos²90°=0 dans le modèle idéal. Les angles de polarisation sont définis modulo 180° : une sortie à 170° est le même état rectiligne. La lame seule conserve la puissance ; c’est l’analyseur qui rejette le faisceau orthogonal.

### 33. Michelson : compter des franges et des anneaux

*Spé ; TP* — laboratoire `michelson`.

**Énoncé.** Dans un Michelson à λ=546 nm, le miroir mobile avance de 100 μm. Combien de franges défilent en incidence normale ? Pour e=0,50 mm et f=200 mm, calculer l’écart de r² entre anneaux brillants consécutifs.

**Corrigé.** Le miroir modifie un aller-retour : Δδ=2Δe=200 μm, donc N=Δδ/λ≈366,30 franges ; un comptage de 366 correspond à un déplacement voisin de 99,918 μm. Pour la lame d’air, δ≈2e−e r²/f². Deux anneaux brillants successifs diffèrent d’un ordre, donc |Δr²|=λf²/e=0,546 μm×(200 mm)²/(0,50 mm)=43,68 mm². Cette différence est constante, tandis que Δr ne l’est pas. Les anneaux se resserrent vers l’extérieur et le centre n’est pas automatiquement un maximum pour une épaisseur quelconque.

### 34. Coin d’air et identification du plan d’observation

*Spé ; TP* — laboratoire `michelson`.

**Énoncé.** Un coin d’air a α=0,15 mrad sous λ=600 nm. Déterminer l’interfrange et son changement pour α doublé. Pourquoi observe-t-on cette figure dans un plan image plutôt que confondre x avec l’angle du montage en lame d’air ?

**Corrigé.** δ(x)=δ₀+2αx ; une augmentation d’un ordre demande 2αi=λ, d’où i=λ/(2α)=600×10⁻⁹/(3×10⁻⁴)=2,00 mm. Pour α=0,30 mrad, i=1,00 mm. x repère une épaisseur locale du coin, tandis que les anneaux d’une lame plane sont des franges d’égale inclinaison et leur distance focale représente une direction. Le plan image du coin localise les variations d’épaisseur. Une mauvaise localisation d’observation peut dégrader les franges d’une source étendue ; déplacer la lentille sans reconsidérer cette distinction n’est pas un simple changement d’échelle.

### 35. Demi-visibilité d’un spectre gaussien

*Spé* — laboratoire `coherence`.

**Énoncé.** Le spectre en fréquence est gaussien de largeur FWHM Δν=20 GHz. À quelle différence de marche la visibilité tombe-t-elle à 1/2 ? Donner V pour δ=2 mm et expliquer pourquoi une largeur de cohérence exige un seuil.

**Corrigé.** V=exp[−π²Δν²(δ/c)²/(4ln2)]. Résoudre V=1/2 donne δ1/2=2ln2·c/(πΔν)≈6,615 mm. À δ=2 mm, l’exposant vaut environ −0,06336, donc V≈0,9386. Le raccourci c/Δν≈14,99 mm donne une échelle, pas cette demi-visibilité. Un seuil à 1/e, une largeur totale autour de δ=0 ou une intégrale de V² donneraient d’autres nombres. La visibilité est un module ; la phase rapide centrée sur la fréquence moyenne situe les franges mais ne change pas cette enveloppe gaussienne.

### 36. Doublet et source étendue : un diagnostic à deux réglages

*Spé* — laboratoire `coherence`.

**Énoncé.** Un doublet autour de 589,3 nm a Δλ=0,60 nm. Estimer la première annulation de visibilité et l’écart des annulations en position e du miroir de Michelson. Pour Young à λ=600 nm, a=0,50 mm, Ds=1 m, quelle largeur uniforme s annule la cohérence spatiale ?

**Corrigé.** Δν≈cΔλ/λ² et V=|cos(πΔνδ/c)| donnent la première annulation δ₀≈λ²/(2Δλ)≈0,28940 mm. Les annulations suivantes sont séparées de Δδ≈λ²/Δλ≈0,57879 mm. Avec δ=2e, e₀≈0,14470 mm et leur espacement Δe≈0,28940 mm. Pour la source uniforme, le premier zéro de sinc[πas/(λDs)] impose s=λDs/a=1,20 mm. Réduire s peut rétablir le contraste spatial mais ne supprime pas les annulations périodiques du doublet. Balayer e puis s sépare donc deux mécanismes qui produisent tous deux une baisse de visibilité.

### 37. Les deux nombres appelés F au Fabry–Perot

*Spé → Au-delà* — laboratoire `fabryperot`.

**Énoncé.** Une cavité idéale a R=0,90 et e=5 mm dans l’air. Calculer coefficient d’Airy F, transmission minimale, FSR, finesse ℱ et largeur FWHM d’un pic. Ne pas assimiler F à ℱ.

**Corrigé.** F=4R/(1−R)²=360 et Tmin=1/(1+F)=1/361≈0,002770. FSR=c/(2e)≈29,979 GHz. La demi-hauteur implique sin²(φ/2)=1/F, donc la largeur totale de phase est 4arcsin(1/√F). La finesse est ℱ=2π/[4arcsin(1/√F)]≈29,790 ; l’approximation π√R/(1−R)≈29,804 est proche. La largeur en fréquence vaut FSR/ℱ≈1,006 GHz. F=360 mesure le coefficient du sinus dans la transmission ; ℱ≈29,8 est un rapport d’intervalle spectral à largeur, deux objets distincts.

### 38. Résonance et angle d’une lame

*Spé → Au-delà* — laboratoire `fabryperot`.

**Énoncé.** La cavité a n=1,50, e=1 mm et λ₀=600 nm à incidence normale. Calculer l’ordre. Pour un angle interne θ=2°, estimer le décalage de longueur d’onde du même ordre et expliquer l’effet d’un faisceau angulairement large.

**Corrigé.** La résonance vérifie 2ne cosθ=mλ₀. À θ=0, m=2×1,50×1 mm/(600 nm)=5000. À ordre fixé, λ(θ)=λ(0)cosθ≈600×0,999390827=599,6345 nm ; le décalage est environ −0,3655 nm. L’expansion donne Δλ/λ≈−θ²/2 avec θ en radians. Un faisceau à plusieurs angles mélange des résonances déplacées, ce qui peut élargir le pic mesuré même si les miroirs gardent le même R. L’angle externe doit d’abord être converti par Snell ; substituer 2° externe à l’angle interne change ce décalage.

### 39. Où placer le masque de Fourier ?

*Spé* — laboratoire `fourier`.

**Énoncé.** Un objet porte une modulation de période 50 μm. Le montage 4f utilise λ=600 nm et f=200 mm. À quelle distance du centre se trouvent ses deux fréquences ? Un disque passe-bas de rayon 1,5 mm les conserve-t-il ?

**Corrigé.** La fréquence est ν=1/(50 μm)=20 mm⁻¹=20000 m⁻¹. Le plan de Fourier donne X=λfν=600×10⁻⁹×0,20×20000=2,40 mm ; les deux composantes d’une modulation cosinus sont à ±2,40 mm. Le masque de rayon 1,5 mm ne les transmet pas ; il conserve la composante moyenne au centre et réduit cette modulation. Sa coupure est νc=1,5 mm/(λf)=12,5 mm⁻¹. Ce calcul concerne une modulation d’amplitude du champ cohérent ; appliquer directement le masque au spectre d’une intensité photographique représenterait une autre expérience.

### 40. Parseval, masque passif et aliasing

*Spé → Au-delà* — laboratoire `fourier`.

**Énoncé.** La grille a un pas de 10 μm et 256 points sur un axe. Calculer fréquence de Nyquist et espacement spectral. Un masque H de module ≤1 peut-il augmenter la puissance totale du champ ? Une modulation de 80 mm⁻¹ est-elle fidèle sur cette grille ?

**Corrigé.** Δx=0,010 mm donne fNyquist=1/(2Δx)=50 mm⁻¹ et Δf=1/(NΔx)=1/2,56≈0,390625 mm⁻¹. Pour une FFT unitaire, Parseval donne ∑|Eimage|²=∑|H Ẽ|²≤∑|Ẽ|²=∑|Eobjet|². Un filtre passif peut augmenter localement une intensité par redistribution mais pas la norme totale. 80 mm⁻¹ dépasse Nyquist ; avec une fréquence d’échantillonnage de 100 mm⁻¹ elle se replie à −20 mm⁻¹, indistinguable sur ces échantillons. Augmenter la coupure d’un masque ne récupère pas l’information perdue avant le filtrage.

### 41. Une cavité stable qui ne lase pas

*Spé → Au-delà* — laboratoire `laser`.

**Énoncé.** L=0,20 m, Rcourbure1=Rcourbure2=0,50 m, Rmiroir1=0,99, Rmiroir2=0,90 et α=0,05 m⁻¹. Tester la stabilité et calculer gseuil. Le gain g₀=0,10 m⁻¹ suffit-il ?

**Corrigé.** g₁=g₂=1−0,20/0,50=0,60, donc leur produit 0,36 est à l’intérieur de 0<g₁g₂<1 : la cavité possède un confinement paraxial stable. Le seuil d’intensité est gseuil=α−ln(0,99×0,90)/(2L)=0,05−ln(0,891)/0,40≈0,338527 m⁻¹. g₀=0,10 est inférieur : le multiplicateur aller-retour R₁R₂exp[2(g₀−α)L] reste inférieur à 1. La présence d’un mode stable ne produit pas une amplification suffisante. Les R de courbure ont des unités de m et les réflectivités sont sans dimension, malgré une lettre souvent commune.

### 42. Saturation et puissance de sortie

*Spé → Au-delà* — laboratoire `laser`.

**Énoncé.** Reprendre gseuil=0,338527 m⁻¹, avec g₀=1 m⁻¹ et Ps=2 W. Utiliser g(P)=g₀/(1+P/Ps) pour estimer P et la puissance transmise par le coupleur à R=0,90. Que devient le résultat sous le seuil ?

**Corrigé.** Le régime établi impose g(P)=gseuil. P=Ps(g₀/gseuil−1)=2(1/0,338527−1)≈3,908 W. Le coupleur transmet ici environ (1−0,90)P≈0,3908 W. En dessous du seuil la solution algébrique serait négative, mais elle n’est pas une puissance physique : ce modèle d’oscillation prend P=0 sans traiter l’émission spontanée. La saturation est une réduction du gain disponible, non un mécanisme qui crée de l’énergie. Le résultat simplifié suppose un gain uniforme et un seul mode, sans dynamique de population ni distinction plus fine des puissances parcourant chaque direction.

### 43. Waist et intensité maximale

*Spé → Au-delà* — laboratoire `gaussien`.

**Énoncé.** Un TEM₀₀ dans l’air a w₀=50 μm, λ₀=633 nm, P=2 mW. Calculer zR, la divergence, l’intensité axiale au waist et à zR. Quelles grandeurs restent constantes lorsque le faisceau s’élargit ?

**Corrigé.** zR=πw₀²/λ₀≈12,4076 mm ; θdiv≈λ₀/(πw₀)≈4,030 mrad. Iaxe(0)=2P/(πw₀²)≈5,093×10⁵ W·m⁻². À z=zR, w=√2w₀ et Iaxe est divisée par deux, environ 2,546×10⁵ W·m⁻². La puissance totale reste P car 2π∫I(r, z)rdr=P à chaque z. La divergence concerne le rayon à 1/e² et non le diamètre complet ; un angle d’ouverture total donnerait environ 2θdiv. La courbure du front d’onde et la phase de Gouy évoluent également, sans perte d’énergie dans ce milieu idéal.

### 44. Quelle fraction de puissance traverse un diaphragme ?

*Spé* — laboratoire `gaussien`.

**Énoncé.** Intégrer l’intensité gaussienne pour trouver la fraction de P dans un disque de rayon a. Calculer cette fraction pour a=w et a=2w. À z=zR, un diaphragme de rayon fixe w₀ transmet quelle fraction ?

**Corrigé.** La puissance du disque est 2π∫₀ᵃ[2P/(πw²)]exp(−2r²/w²)rdr=P[1−exp(−2a²/w²)]. À a=w, la fraction vaut 1−e⁻²≈0,864665 ; à a=2w, 1−e⁻⁸≈0,999665. À z=zR, w=√2w₀ ; le diaphragme fixe a=w₀ transmet 1−e⁻¹≈0,632121. Le faisceau sans diaphragme conserve sa puissance, mais le flux transmis par une ouverture fixe diminue quand il s’élargit. Une troncature nette modifie aussi la diffraction en aval ; prolonger ensuite exactement le même TEM₀₀ serait une approximation supplémentaire.

### 45. Deux étoiles et une pupille circulaire

*Spé* — laboratoire `airy`.

**Énoncé.** Deux étoiles de même flux sont séparées de 0,70 seconde d’arc. À λ=550 nm, quel diamètre circulaire idéal atteint le critère de Rayleigh ? Pourquoi doit-on sommer leurs intensités plutôt que leurs amplitudes ?

**Corrigé.** θ=0,70/206264,806≈3,3937×10⁻⁶ rad. D≈1,22λ/θ≈0,19772 m, soit environ 198 mm. Les étoiles ont des phases mutuellement indépendantes à l’échelle de la mesure : la moyenne du produit croisé des champs est nulle. Le profil est donc la somme de deux PSF d’intensité centrées aux deux positions, pas le carré d’une somme d’amplitudes à phase fixée. Rayleigh suppose deux flux égaux et une pupille idéale ; une étoile dix fois plus faible peut être beaucoup plus difficile à détecter à la même séparation. Le grossissement d’un oculaire ne change pas le diamètre D.

### 46. Obstruction : un pic étroit ne suffit pas

*Spé → Au-delà* — laboratoire `airy`.

**Énoncé.** Une pupille annulaire a le rapport ε=0,40 entre diamètre central opaque et diamètre extérieur. Calculer la fraction de flux collecté et établir la limite A(0) de A(u)=2[J₁(u)−εJ₁(εu)]/[u(1−ε²)]. Pourquoi ne conclut-on pas seulement à une meilleure résolution si le pic se resserre ?

**Corrigé.** La surface transparente est πD²(1−ε²)/4, soit une fraction 1−0,16=0,84 de celle du disque plein. Comme J₁(u)=u/2+O(u³), le numérateur vaut u(1−ε²)+O(u³) et A(0)=1 avec cette normalisation au pic. La PSF redistribue davantage d’énergie dans les anneaux ; sa largeur centrale et son contraste de compagnon faible ne s’améliorent pas nécessairement ensemble. Le repère 1,22λ/D est celui du disque plein, pas le premier zéro recalculé de l’anneau. Une comparaison normalisée au maximum masque aussi les 16 % de lumière perdue.

### 47. Conversion χ² et première extinction de phase

*Au-delà accompagné* — laboratoire `nonlineaire`.

**Énoncé.** Avec λω=1064 nm, d=5 pm·V⁻¹, nω=n2ω=1,65, Iω=0,20 GW·cm⁻², L=1 mm, estimer le rendement de pompe constante à accord parfait. Quel désaccord Δk donne sa première annulation ? La même formule reste-t-elle crédible à L=3 mm ?

**Corrigé.** Convertir Iω=0,20×10¹³=2×10¹² W·m⁻² et ω=2πc/λω. η=2ω²d²IωL²/(nω²n2ωε₀c³)≈0,29245 à accord parfait. La première annulation de sinc²(ΔkL/2) est |Δk|L/2=π, donc |Δk|=2π/L≈6,283 mm⁻¹. À L=3 mm, la loi L² donnerait η≈2,632>1, impossible avec une seule pompe sans apport supplémentaire : la déplétion doit être incluse. Même 29 % n’est plus une conversion très faible ; le modèle couplé est préférable pour un résultat précis. Le coefficient d=χeff/2 dépend de la convention tensorielle annoncée.

### 48. Un bilan de photons qui n’est pas leur nombre total

*Au-delà accompagné* — laboratoire `nonlineaire`.

**Énoncé.** Une pompe à 1064 nm fournit 10⁶ photons par intervalle et convertit 60 % de son énergie en seconde harmonique. Compter les photons résiduels et générés. Avec η=tanh²(κL), trouver κL pour η=1/2 ; comparer au modèle faible η≈(κL)².

**Corrigé.** Un photon harmonique à 532 nm possède deux fois l’énergie d’un photon fondamental. La conversion de 60 % transforme donc 600000 photons fondamentaux en 300000 photons harmoniques ; il reste 400000 photons fondamentaux. Nω+2N2ω=400000+600000=10⁶ est conservé, tandis que Nω+N2ω=700000 ne l’est pas. η=1/2 donne κL=artanh(1/√2)≈0,881374 ; l’approximation faible donnerait alors η≈0,77686 et surestime la conversion. Dans l’exemple à deux pompes distinctes du recueil, chaque photon harmonique consomme un photon dans chaque branche : on conserve N₁+N₃ et N₂+N₃ séparément.

## Sources primaires et programmes

- [BO 2021 — MPSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm) et [PCSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm) : repères de première année, méthodes expérimentales et conjugaison paraxiale.
- [BO 2021 — MP](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111702A.htm), [PC](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111703A.htm) et [PSI](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111748A.htm) : le statut des interférences, de la diffraction, de la polarisation et des extensions dépend de la filière.
- [MIT — Optics, N. Fang](https://www.ocw.mit.edu/courses/2-71-optics-spring-2014/pages/lecture-notes/) : cours primaire couvrant instrumentation, eikonale, interférences, diffraction et polarisation. Les dérivations et expériences de cet atelier sont originales.
- [MIT — matrices en optique paraxiale](https://www.ocw.mit.edu/courses/2-71-optics-spring-2014/resources/mit2_71s14_lec4_notes/) : coordonnées de rayon et composition ABCD ; nous annonçons explicitement u=nθ.
- [MIT — Fraunhofer](https://www.ocw.mit.edu/courses/2-71-optics-spring-2014/resources/mit2_71s14_lec14_notes/) : diffraction et transformée de Fourier de pupille.
- [MIT — Optics 2009, G. Barbastathis et C. Sheppard](https://ocw.mit.edu/courses/2-71-optics-spring-2009/resources/lecture-notes/) : instruments, aberrations et filtrage spatial, pour les prolongements accompagnés.
- [MIT — Optical Engineering](https://ocw.mit.edu/courses/2-717j-optical-engineering-spring-2002/pages/lecture-notes/) : optique statistique, cohérence et fonction de transfert, au-delà du socle de l’atelier.
- [MIT — Fundamentals of Photonics, F. Kärtner](https://www.ocw.mit.edu/courses/6-974-fundamentals-of-photonics-quantum-electronics-spring-2006/bf3bdeb971819ddc9c68719d28bb2745_classnotes.pdf) : modes, faisceaux gaussiens et liens entre rayons et ondes.
- [MIT — Ultrafast Optics](https://ocw.mit.edu/courses/6-977-ultrafast-optics-spring-2005/pages/lecture-notes/) : gain, saturation, lasers et propagation non linéaire ; ces thèmes sont signalés comme prolongements.
- [NASA — Webb, questions scientifiques](https://science.nasa.gov/mission/webb/faqs-full/) et [NASA — Hubble et Webb](https://science.nasa.gov/mission/hubble/observatory/hubble-vs-webb/) : diamètre et domaine spectral des instruments. Notre expérience Airy utilise une pupille circulaire idéale, pas la PSF segmentée réelle de Webb.
- [NASA — Designing a Satellite Imaging System](https://science.nasa.gov/wp-content/uploads/2023/09/Electromagnetic_Math.pdf) : applications de la limite angulaire d’une pupille circulaire à l’imagerie.
- [National Eye Institute — erreurs de réfraction](https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases/refractive-errors/types-refractive-errors) : distinction qualitative myopie, hypermétropie, astigmatisme et presbytie ; le laboratoire reste un œil réduit pédagogique.
- [University of Sydney — Fibre Optics](https://www.physics.usyd.edu.au/~jbh/share/PHYS1901/chapter8-Fibre-Optics.pdf) : acceptance, dispersion et distinction des rayons et modes guidés.
- [University of Texas — cohérence](https://farside.ph.utexas.edu/teaching/315/Waves/node92.html), [diffraction de plusieurs fentes](https://farside.ph.utexas.edu/teaching/315/Waveshtml/node93.html) et [diffraction de pupilles, R. Fitzpatrick](https://farside.ph.utexas.edu/teaching/315/Waves/node98.html) : développements primaires pour les expériences ondulatoires.
- [MIT — Gaussian Beams and Resonators](https://ocw.mit.edu/courses/6-974-fundamentals-of-photonics-quantum-electronics-spring-2006/e9852c138493233bc2813f683da5b199_gaussian_bem_res.pdf) : paramètres q, Gouy et stabilité ABCD de cavité.
