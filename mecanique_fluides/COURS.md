# Mécanique des fluides — cours, laboratoires et exercices corrigés

Vingt-huit leçons, dix-huit laboratoires et quarante exercices. Les variables, unités, hypothèses et conventions sont déclarées avant les calculs. Les missions proposent de prédire, expérimenter et justifier.

Les repères Sup et Spé indiquent les outils mobilisés ; les sujets obligatoires dépendent de la filière. Les équations d'Euler et de Navier–Stokes, notamment exclues du programme PSI cité, et certaines approches exclues du programme PC cité sont étudiées comme extensions accompagnées. Se reporter aux textes officiels référencés et au parcours pour choisir les séances.

## 1 · Observer un champ, suivre une particule

*SUP → SPÉ · CINÉMATIQUE*

Laboratoire : `cinematique`.

**Place dans la formation.** Les repères Sup et Spé indiquent les outils mobilisés, pas un programme obligatoire identique dans toutes les filières. Le programme PSI cité en sources exclut les équations d'Euler et de Navier–Stokes ; le programme PC cité exclut notamment la description lagrangienne, la fonction de courant, l'étude locale du gradient de vitesse et Bernoulli instationnaire. Ces sujets sont ici des extensions guidées, avec leurs définitions et leurs preuves. Le professeur peut choisir les missions compatibles avec sa progression.

**Objets et unités.** Une particule de fluide est un petit volume matériel contenant assez de molécules pour définir une masse volumique ρ en kg·m⁻³. Sa taille doit rester petite devant celle des variations étudiées. La position r est en m, le temps t en s et le champ v(r,t) en m·s⁻¹. Ce modèle de milieu continu ne décrit pas séparément les trajectoires moléculaires.

**Deux descriptions.** La description eulérienne donne v en chaque point fixe. La description lagrangienne suit R(a,t), position de la particule initialement étiquetée par a, avec ∂ₜR=v(R,t). Une ligne de courant est tangente à v à un instant fixé ; une trajectoire suit une même particule au cours du temps. Elles coïncident en écoulement permanent, mais pas en général.

Dₜf=∂ₜf+v·∇f ; accélération a=∂ₜv+(v·∇)v.  
Trajectoire : dR/dt=v(R,t).  
Ligne de courant à t₀ : dr/ds parallèle à v(r,t₀).

**Preuve par la chaîne.** Le long de R(t), dériver f(R(t),t) donne ∂ₜf+Σᵢ(∂ᵢf)dRᵢ/dt. Remplacer dRᵢ/dt par vᵢ produit la dérivée matérielle. Appliquer cette identité aux composantes de v : une vitesse locale indépendante du temps peut donner une accélération, parce que la particule traverse des régions où v change.

**Exemple interprété.** Pour v=(αx,−αy), α=0,5 s⁻¹, une particule partie de (0,20 m,0,10 m) suit x=0,20 exp(αt), y=0,10 exp(−αt). À t=2 s, elle est près de (0,544 m,0,0368 m). Le produit xy reste constant et l'aire d'un petit élément est conservée ; pourtant l'accélération vaut (α²x,α²y), généralement non nulle.

**Mission.** Prédire la direction du déplacement et de l'accélération avant de lire les flèches. Comparer ensuite une courbe instantanée et une trajectoire dans un champ dépendant du temps. Identifier ce qui appartient à l'espace physique, ce qui est une étiquette de particule et ce qui est un paramètre de modèle.

## 2 · Conserver la masse et mesurer un débit

*SUP → SPÉ · BILANS*

Laboratoire : `cinematique`.

**Objets et unités.** ρ(r,t) est la masse volumique, j=ρv le courant de masse en kg·m⁻²·s⁻¹. Pour une section orientée S, Q=∫_S v·n dS est un débit volumique en m³·s⁻¹ et ṁ=∫_Sρv·n dS un débit massique en kg·s⁻¹. Le sens choisi pour la normale fixe le signe du débit.

**Bilan sur un volume fixe.** La masse contenue dans V varie à cause des flux à travers sa frontière. Avec n sortante, d/dt∫_Vρ dV=−∫_∂Vρv·n dS. Une entrée donne un flux sortant négatif et augmente la masse. Cette convention évite d'ajouter des signes différents à chaque face.

∂ₜρ+div(ρv)=0.  
Dₜρ+ρ div v=0.  
ρ>0 et Dₜρ=0 ⇒ div v=0.

**Passage local.** Le théorème de Gauss transforme le flux en ∫_Vdiv(ρv). Puisque le bilan vaut pour tout petit volume, l'intégrande est nul. Développer div(ρv)=v·∇ρ+ρ div v donne la forme matérielle. L'incompressibilité signifie conservation de la masse volumique d'une particule ; elle ne force pas une densité identique pour toutes les particules d'un fluide stratifié.

**Exemple de conduite.** Dans un écoulement permanent sans fuite, le débit massique se conserve. Si le liquide a une densité constante et un profil uniforme, S₁U₁=S₂U₂. Pour Q=2,0 L·min⁻¹, des sections 1,0 cm² et 0,50 cm² donnent U₁=0,333 m·s⁻¹ et U₂=0,667 m·s⁻¹. Réduire la section accélère le fluide ; cela ne permet pas encore de calculer les pressions.

**Mission et limite.** Construire un bilan signé sur un volume entourant une jonction et contrôler les unités. Pour un profil parabolique, intégrer la vitesse plutôt que multiplier la vitesse centrale par la section. Si ρ change dans un gaz, conserver ṁ ; remplacer ce bilan par Q constant serait une hypothèse supplémentaire.

## 3 · Séparer rotation, déformation et dilatation

*SPÉ · EXTENSION GUIDÉE SELON FILIÈRE*

Laboratoire : `newtonien`.

**Objets.** Le gradient Lᵢⱼ=∂vᵢ/∂xⱼ, en s⁻¹, décrit les variations locales de vitesse. Autour d'un point M, v(M+δr)≈v(M)+Lδr. Une translation commune ne déforme pas l'élément. La partie symétrique et la partie antisymétrique de L ont deux effets physiques distincts.

L=D+W ; D=(L+Lᵀ)/2 ; W=(L−Lᵀ)/2.  
Wδr=Ω×δr ; Ω=(curl v)/2.  
Dₜ(dV)=(div v)dV ; div v=tr D.

**Preuve de l'interprétation.** Pour deux particules voisines séparées par δr, la dérivée de |δr|² vaut 2δrᵀDδr, car δrᵀWδr=0. D mesure donc l'allongement ou le raccourcissement. W conserve instantanément les distances et représente une rotation locale. Le déterminant de la transformation infinitésimale I+Ldt vaut 1+tr(L)dt : sa trace mesure la dilatation volumique.

**Deux contre-exemples utiles.** La rotation solide v=(−Ω₀y,Ω₀x,0) a D=0 et curl v=2Ω₀e_z. Le cisaillement v=(γ̇y,0,0) a Dₓᵧ=Dᵧₓ=γ̇/2 et Ω_z=−γ̇/2. Des couches qui glissent les unes sur les autres produisent donc à la fois une rotation locale et une déformation ; elles ne constituent pas une rotation rigide.

**Exemple numérique.** Avec γ̇=100 s⁻¹, deux points séparés verticalement de 1 mm ont une différence de vitesse de 0,10 m·s⁻¹. Les valeurs propres ±50 s⁻¹ de D dans le plan indiquent des directions instantanées d'allongement et de compression. Ces taux ne sont pas des vitesses de particules : il faut encore les multiplier par une longueur.

**Mission.** Suivre un carré matériel et rapprocher son changement de forme de D. Refaire la même observation pour une rotation pure. Démontrer par un produit scalaire pourquoi une rotation peut avoir une vorticité non nulle tout en ne dissipant aucune énergie par cisaillement newtonien.

## 4 · Pression, contrainte et viscosité newtonienne

*SUP → SPÉ · LOI CONSTITUTIVE*

Laboratoire : `newtonien`.

**Objets et unités.** Le tenseur des contraintes σ a l'unité Pa=N·m⁻². Il fournit une traction σn sur une face de normale n. On écrit σ=−pI+τ : la pression p agit normalement, tandis que τ décrit les contraintes visqueuses. La viscosité dynamique η est en Pa·s ; la viscosité cinématique ν=η/ρ est en m²·s⁻¹.

**Hypothèses.** Un fluide newtonien isotrope relie linéairement la contrainte visqueuse au taux de déformation. Pour un liquide incompressible à η constante, τ=2ηD. Pour un fluide compressible, on sépare D₀=D−(div v)I/3 et la viscosité volumique ζ : τ=2ηD₀+ζ(div v)I. La relation τ=η du/dy dans un cisaillement est une contrainte ; ν du/dy n'a pas la bonne unité.

τ=2ηD, si div v=0.  
Φ=τ:∇v=2η D:D≥0.  
Compressible : Φ=2η D₀:D₀+ζ(div v)², avec η,ζ≥0.

**Preuve de la dissipation.** La contraction τ:∇v est la puissance visqueuse par unité de volume, en W·m⁻³. Le produit d'une matrice symétrique par une antisymétrique a une trace nulle : D:W=0. Ainsi τ:L=2ηD:D, somme de carrés. La viscosité transforme une énergie mécanique en énergie interne ; elle ne fait pas disparaître l'énergie totale d'un système isolé.

**Exemple chiffré.** Dans un cisaillement γ̇=1000 s⁻¹ et η=1,0 mPa·s, τₓᵧ=1,0 Pa et Φ=η γ̇²=1000 W·m⁻³. Pour une rotation rigide du même ordre de vitesse, D=0 et Φ=0. Une grande vitesse n'est donc pas, à elle seule, un critère de forte dissipation.

**Mission et prolongement.** Distinguer la force tangentielle, la contrainte et le gradient de vitesse. Vérifier l'unité de chaque produit. Les fluides à seuil, rhéofluidifiants ou viscoélastiques demandent d'autres lois constitutives ; les formules de cet atelier décrivent le modèle newtonien indiqué, pas tout liquide.

## 5 · De Newton à Euler et Navier–Stokes

*SPÉ · EXTENSION GUIDÉE SELON FILIÈRE*

Laboratoire : `navier`.

**Objets et hypothèses.** ρ est la masse volumique, v la vitesse, p la pression, g une accélération extérieure et η la viscosité dynamique. Un bilan de quantité de mouvement sur un volume matériel donne ρDₜv=div σ+ρg. Pour un fluide newtonien incompressible à ρ et η constantes, div σ=−∇p+ηΔv.

ρ[∂ₜv+(v·∇)v]=−∇p+ηΔv+ρg ; div v=0.  
Euler : même bilan en négligeant la viscosité.  
Paroi visqueuse : v=v_paroi ; paroi idéale fixe : v·n=0.

**Pourquoi un Laplacien ?** Avec τᵢⱼ=η(∂ⱼvᵢ+∂ᵢvⱼ), sa divergence vaut η[Δvᵢ+∂ᵢdiv v]. Le second terme disparaît lorsque div v=0. Ce calcul demande η uniforme. Si la viscosité varie, dériver aussi η ; remplacer automatiquement div τ par ηΔv supprimerait des termes physiques.

**Rôle de la pression.** Dans le modèle incompressible, p impose la contrainte div v=0. Prendre la divergence donne, pour une accélération extérieure constante, Δp=−ρΣᵢⱼ(∂ᵢvⱼ)(∂ⱼvᵢ). Les conditions aux limites et une référence additive complètent ce problème. La pression n'est donc pas une variable arbitraire réglée indépendamment du champ de vitesse.

**Une réduction exacte.** Pour v=(u(y,t),0,0), indépendant de x, le terme convectif s'annule. Sans gradient de pression, ∂ₜu=ν∂²_yu. Un champ non uniforme peut donc résoudre une équation linéaire de diffusion sans rendre Navier–Stokes linéaire en général. Avec −∂ₓp=G>0 et en régime permanent, ηu''=−G, base des profils de Poiseuille.

**Mission.** Annoncer les inconnues, le domaine, les conditions aux limites et l'état initial avant de résoudre. Dans le laboratoire bidimensionnel, relier vitesse, pression, vorticité et énergie à la solution exacte présentée. Une image de tourbillons ne prouve ni que la viscosité est nulle ni qu'un calcul tridimensionnel général a été effectué.

## 6 · Énergie, vorticité et la question mathématique de Navier–Stokes

*SPÉ → APPROFONDISSEMENT GUIDÉ*

Laboratoire : `navier`.

**Cadre du bilan.** Considérer une solution régulière incompressible, sans force, dans un domaine périodique ou avec une paroi fixe où v=0. L'énergie cinétique est E=(ρ/2)∫|v|²dV en J. Multiplier l'équation par v et intégrer permet de suivre une grandeur globale, tout en conservant les conditions qui annulent les flux aux frontières.

dE/dt=−η∫|∇v|²dV≤0.  
En 3D : Dₜω=(ω·∇)v+νΔω ; ω=curl v.  
En 2D plan incompressible : Dₜω_z=νΔω_z.

**Preuve du bilan.** Le terme convectif est ∫v·∇(|v|²/2), intégrale d'une divergence ; div v=0 et les frontières choisies le rendent nul. Le travail de pression s'annule de même. Une intégration par parties transforme ∫v·Δv en −∫|∇v|². La borne obtenue contrôle une norme L² et une intégrale temporelle de gradients ; elle n'est pas une borne ponctuelle de tous les gradients.

**Exemple exact du laboratoire.** Le vortex de Taylor–Green a v=(A sin(kx)cos(ky),−A cos(kx)sin(ky)), A=U exp(−2νk²t). Sa pression relative est ρA²[cos(2kx)+cos(2ky)]/4. La densité moyenne d'énergie vaut ρA²/4 et sa dissipation ρνk²A². Des tourbillons visibles décroissent ici selon une formule exacte : ce cas 2D ne teste pas tous les mécanismes 3D, notamment l'étirement des tourbillons.

**Énoncé à distinguer du calcul.** La formulation historique de Fefferman demande une des quatre conclusions suivantes : existence globale régulière pour toute donnée admissible en 3D, sans force, sur ℝ³ (A) ou le domaine périodique (B) ; ou construction de données et forces admissibles pour lesquelles une telle solution globale n'existe pas, dans ces cadres respectifs (C,D). Les données doivent satisfaire les conditions de régularité, divergence et décroissance ou périodicité déclarées dans l'[énoncé officiel et ses corrections](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).

**Repère daté, vérifié le 6 octobre 2026.** Le Clay Mathematics Institute a annoncé le 11 septembre 2026 une résolution apparemment obtenue et un processus d'évaluation délibérément progressif. Cette annonce ne confirme pas dans ce texte l'attribution d'un prix. Le présent atelier explique l'énoncé et les bilans classiques ; il ne prétend pas vérifier la preuve annoncée. [Annonce primaire du Clay](https://www.claymath.org/news/navier-stokes-announcement/).

**Mission.** Retrouver analytiquement la décroissance de Taylor–Green, puis contrôler le bilan d'énergie affiché. Expliquer en trois phrases pourquoi une simulation finie, une solution particulière et une borne d'énergie ne démontrent pas à elles seules une assertion globale pour toutes les données 3D.

## 7 · Reynolds et similitude : choisir une échelle

*SUP → SPÉ · ANALYSE DIMENSIONNELLE*

Laboratoire : `navier`.

**Objets et unités.** Choisir une vitesse U, une longueur L et une viscosité cinématique ν. Le nombre Re=UL/ν est sans dimension. Les temps de transport et de diffusion sont t_adv=L/U et t_ν=L²/ν : Re=t_ν/t_adv. Une longueur doit être déclarée, par exemple le diamètre d'un tube ou la distance au bord d'attaque d'une plaque.

Re=ρUL/η=UL/ν.  
Avec x=Lx*, t=(L/U)t*, v=Uv* :  
∂ₜ*v*+(v*·∇*)v*=−∇*p*+(1/Re)Δ*v*, si les autres forces sont omises.

**Preuve et portée.** L'inertie convective a l'échelle ρU²/L ; la force visqueuse a l'échelle ηU/L². Leur rapport fournit Re. Ce rapport d'échelles reste utile lorsqu'un terme particulier s'annule exactement par symétrie : il ne faut pas définir Re en divisant deux valeurs locales éventuellement nulles.

**Exemple interprété.** Pour l'eau modélisée par ν=1,0 mm²·s⁻¹, U=0,10 m·s⁻¹ et un diamètre de 1,0 mm, Re=100. Dans un tube de 10 mm au même U, Re=1000. Pour une bille, utiliser son diamètre et sa vitesse relative ; pour Blasius, Re_x=Ux/ν varie le long de la plaque.

**Un seuil n'est pas une loi universelle.** Les valeurs voisines de quelques milliers concernent des transitions dans certains écoulements de conduite et dépendent des perturbations et de la géométrie. Un écoulement autour d'un obstacle, une couche limite et un cisaillement entre plaques n'ont pas tous le même seuil. Re élevé ne justifie pas la suppression de la viscosité au contact d'une paroi adhérente.

**Mission.** Prédire comment Re change lorsqu'on double U ou L, puis comparer des cas ayant le même Re avec des géométries semblables. Pour les ondes, ajouter les rapports d'échelles pertinents : Mach U/c pour la compressibilité, Froude U/√(gL) pour la gravité et Bond ρgL²/γ pour la capillarité.

## 8 · Couette : un profil linéaire et un bilan de puissance

*SUP → SPÉ · ÉCOULEMENT VISQUEUX*

Laboratoire : `couette`.

**Géométrie.** Deux plaques planes sont séparées par h en m. La plaque y=0 a la vitesse U, celle y=h est fixe. Le fluide est newtonien, incompressible, permanent ; les effets des bords et le gradient de pression parallèle sont négligés. On cherche v=(u(y),0,0), avec adhérence u(0)=U et u(h)=0.

u''=0 ⇒ u(y)=U(1−y/h).  
τₓᵧ=ηu'=−ηU/h.  
Puissance reçue par aire de plaque : ηU²/h.  
Dissipation par volume : Φ=η(U/h)².

**Démonstration.** La continuité est satisfaite et la convection vaut zéro. Navier–Stokes donne ηu''=0. Les deux conditions aux limites déterminent les constantes. Le signe de la traction tangentielle dépend de la normale de la face ; la force sur la plaque mobile s'oppose à U. Sa puissance motrice positive vaut la valeur absolue de la contrainte fois U.

**Vérification énergétique.** Intégrer Φ sur une tranche d'épaisseur h donne ηU²/h par unité d'aire, exactement la puissance fournie par la plaque. Le profil ne stocke plus d'énergie cinétique en régime permanent. La température ne peut rester fixe sans un échange thermique ou une approximation limitée dans le temps.

**Exemple.** Avec η=0,10 Pa·s, h=1,0 mm et U=0,20 m·s⁻¹, la contrainte a pour module 20 Pa et la puissance surfacique vaut 4,0 W·m⁻². Doubler h à U fixé divise ces deux grandeurs par deux, tandis que le débit par largeur Uh/2 augmente.

**Mission.** Comparer le profil de vitesse, le glissement d'un rectangle matériel et la force à exercer. Si l'on ajoute un gradient de pression, superposer une parabole au profil linéaire ; on obtient Couette–Poiseuille, dont une partie peut s'écouler en sens opposé. La formule exacte d'un profil ne constitue pas une preuve de stabilité envers toutes les perturbations.

## 9 · Poiseuille : la loi en R⁴ se démontre

*SUP → SPÉ · TP PRIORITAIRE*

Laboratoire : `poiseuille`.

**Convention et unités.** Un tube droit de longueur L et rayon R transporte un fluide newtonien incompressible en régime permanent pleinement développé. On définit Δp=p_entrée−p_sortie, positif pour un écoulement selon +x. η est en Pa·s, Q en m³·s⁻¹. Les conditions sont adhérence u(R)=0 et régularité au centre.

0=Δp/L+η(1/r)(ru')'.  
u(r)=Δp(R²−r²)/(4ηL).  
Q=πR⁴Δp/(8ηL) ; U_moy=ΔpR²/(8ηL)=u(0)/2.

**Preuve du profil.** Multiplier l'équation par r et intégrer donne ru'=−Δp r²/(2ηL)+C. La régularité en r=0 impose C=0 ; la seconde intégration et u(R)=0 donnent la parabole. Aucune singularité logarithmique n'est autorisée sur l'axe. Si l'on définit au contraire p_sortie−p_entrée, le profil porte le signe opposé.

**Preuve du débit.** Une couronne de rayon r et épaisseur dr a l'aire 2πr dr. Intégrer u(r)2πr de 0 à R donne Q. La puissance hydraulique ΔpQ est positive et égale à l'intégrale de la dissipation visqueuse. La résistance ℛ=Δp/Q=8ηL/(πR⁴) a l'unité Pa·s·m⁻³.

**Exemple interprété.** Prendre R=0,50 mm, L=0,10 m, η=1,0 mPa·s et Δp=100 Pa. On obtient Q≈2,45×10⁻⁸ m³·s⁻¹, soit 1,47 mL·min⁻¹, et U_moy≈0,0313 m·s⁻¹. Avec ρ=1000 kg·m⁻³, Re_D≈31,3 : le régime visqueux laminaire est cohérent. Une augmentation de R de 10 % multiplie Q par 1,1⁴≈1,464, à Δp fixé.

**Mission.** Reconstituer le débit à partir du profil avant de lire sa valeur. Distinguer le rayon du diamètre, la vitesse centrale de la moyenne et le régime d'entrée du régime développé. Comparer deux conduites de rayons différents à pression imposée, puis à débit imposé : la même loi conduit à deux lectures différentes.

## 10 · Conduites, résistances et pertes de charge

*SPÉ · BILANS ET RÉSEAUX*

Laboratoire : `poiseuille`.

**Objets.** Q est le débit, ℛ une résistance hydraulique laminaire et H=p/(ρg)+z+U²/(2g) une charge en m. Une perte de charge est une diminution irréversible de H dans le sens de l'écoulement ; elle n'est pas toujours identique à la seule baisse de pression, car altitude et vitesse peuvent varier.

Série : ℛ_eq=Σℛᵢ ; parallèle : 1/ℛ_eq=Σ1/ℛᵢ.  
Tube circulaire développé : Δp=f_D(L/D)ρU_moy²/2.  
En régime laminaire : f_D=64/Re_D.  
Perte singulière : Δp=KρU_ref²/2, convention U_ref à déclarer.

**Preuve des associations.** En série, le même Q traverse chaque tube et les baisses de pression s'ajoutent : Δp_total=QΣℛᵢ. En parallèle, les deux extrémités sont communes, donc chaque branche a le même Δp ; les débits s'ajoutent. Ces relations viennent de la continuité et de la loi linéaire, comme pour un réseau électrique résistif.

**Lien avec Poiseuille.** Remplacer R=D/2 et Q=U_moyπD²/4 dans Δp=8ηLQ/(πR⁴) donne Δp=32ηLU_moy/D². Comparer avec Darcy–Weisbach conduit à f_D=64/Re_D. Ce facteur de Darcy vaut quatre fois le facteur de Fanning : un coefficient sans sa convention n'est pas exploitable.

**Exemple.** Deux tubes identiques de résistance ℛ en parallèle ont ℛ_eq=ℛ/2 ; ils doublent le débit sous une même pression. En série ils donnent 2ℛ et divisent le débit par deux. Ces règles ne restent pas linéaires si une branche a Δp∝Q² ; il faut alors résoudre l'égalité de pression avec sa loi propre.

**Mission.** Écrire un bilan de charge entre deux sections en indiquant la puissance d'une pompe reçue par le fluide : la charge gagnée vaut P_pompe/(ρgQ). Vérifier que les pertes sont positives. Les lois de pertes turbulentes et les coefficients de coudes sont des modèles empiriques ; leurs domaines d'application doivent accompagner une valeur calculée.

## 11 · Une paroi démarre : diffusion de quantité de mouvement

*SPÉ · PREMIER PROBLÈME DE STOKES*

Laboratoire : `diffusion`.

**Géométrie et unités.** Le fluide occupe y≥0, initialement au repos. À t=0 la paroi y=0 prend la vitesse constante U. On suppose un écoulement parallèle, sans gradient de pression, et ν uniforme. L'équation ∂ₜu=ν∂²_yu doit respecter u(0,t)=U et u(y,t)→0 lorsque y→∞. Une valeur de ν en mm²·s⁻¹ se multiplie par 10⁻⁶ pour devenir une valeur SI.

ξ=y/(2√(νt)) ; u/U=erfc ξ.  
δ(t)=2√(νt) : longueur caractéristique, pas un front net.  
|τ_paroi|=ηU/√(πνt), pour t>0.

**Preuve par similitude.** Les seules échelles disponibles donnent y/√(νt). Poser u=UF(ξ) réduit l'équation à F''+2ξF'=0. Donc F'=C exp(−ξ²). Intégrer avec F(0)=1 et F(∞)=0 donne la fonction complémentaire d'erreur. La racine porte sur νt tout entier : une longueur proportionnelle à t aurait la mauvaise dimension.

**Ce que mesure δ.** À y=δ, u/U=erfc(1)≈0,157 ; au-delà, le fluide n'est pas rigoureusement au repos. La diffusion a des queues non nulles. La contrainte de paroi diverge dans le modèle d'un départ instantané, mais sa puissance intégrée sur un petit intervalle de temps reste finie. Un moteur réel impose une accélération et régularise le tout début.

**Exemple et paroi opposée.** Pour ν=1,0 mm²·s⁻¹ et t=1,0 s, δ=2,0 mm. Pour t=4,0 s, δ=4,0 mm : multiplier le temps par quatre double l'épaisseur. Si une seconde paroi fixe est située à y=h, le demi-espace est une approximation tant que √(νt)≪h ; ensuite le profil tend vers Couette.

Sur 0<y<h : u/U=1−y/h−Σₙ≥₁[2/(nπ)]sin(nπy/h) exp(−n²π²νt/h²).

**Mission.** Comparer les profils à deux temps en gardant y/√t constant, puis introduire une paroi éloignée. Démontrer la série en soustrayant le profil permanent et en développant la condition initiale en sinus. Les temps, l'épaisseur et les contraintes relient ici un problème de diffusion aux intégrales gaussiennes du volet de calcul différentiel.

## 12 · Blasius : une couche limite qui s'épaissit

*SPÉ · APPROFONDISSEMENT GUIDÉ*

Laboratoire : `blasius`.

**Hypothèses.** Un fluide newtonien incompressible suit une plaque plane fixe, avec une vitesse extérieure U constante et un gradient de pression extérieur nul. L'écoulement est permanent, plan, laminaire ; la couche visqueuse est mince devant x, distance au bord d'attaque. u et v sont les vitesses parallèle et normale à la plaque.

u∂ₓu+v∂ᵧu=ν∂²ᵧu ; ∂ₓu+∂ᵧv=0.  
ξ=y√(U/(νx)) ; ψ=√(νUx)f(ξ).  
u/U=f' ; v=½√(νU/x)(ξf'−f).  
f'''+½ff''=0 ; f(0)=f'(0)=0, f'(∞)=1.

**Pourquoi cette variable ?** Comparer U²/x et νU/δ² donne δ≈√(νx/U). Le temps disponible pour diffuser pendant le transport jusqu'à x est x/U. La fonction de courant impose automatiquement la continuité ; sa substitution dans l'équation de mouvement produit l'équation de Blasius. Le coefficient 1/2 dépend de la définition choisie de ξ.

**Solution et contrôles.** Les conditions au mur expriment l'imperméabilité et l'adhérence. La condition loin du mur raccorde la couche au fluide extérieur. Avec la convention affichée, f''(0)≈0,332057 et δ₉₉≈4,91√(νx/U). Le coefficient local de frottement C_f=τ_w/(ρU²/2) vaut 0,664114/√Re_x ; il n'est pas le coefficient moyen sur toute une plaque.

**Exemple.** Avec U=10 m·s⁻¹, ν=1,5×10⁻⁵ m²·s⁻¹ et x=0,10 m, Re_x≈6,67×10⁴ et δ₉₉≈1,90 mm. La couche est mince, δ₉₉/x≈0,019. Le modèle fournit un profil laminaire sous ses hypothèses ; ce calcul ne démontre pas que toute expérience à ce Re sera sans transition.

**Mission.** Prédire l'effet de x et U sur l'épaisseur, puis superposer les profils en coordonnées ξ. Relier la pente au mur à la contrainte. Intégrer ensuite le frottement local pour retrouver le coefficient moyen 1,328/√Re_L. Un gradient de pression défavorable ou un décollement demande un autre modèle : on ne l'obtient pas en prolongeant automatiquement Blasius.

## 13 · Une sphère lente : traînée de Stokes et sédimentation

*SPÉ · TP PRIORITAIRE*

Laboratoire : `sphere`.

**Objets et régime.** Une sphère rigide de rayon R se déplace relativement à un fluide de densité ρ_f et viscosité η. La vitesse relative est w. Le nombre Re_D=2ρ_fR|w|/η doit être petit devant 1 ; la sphère doit être éloignée des parois. Le problème permanent réduit s'écrit ∇p=ηΔv, div v=0, avec adhérence sur la sphère et vitesse uniforme loin d'elle.

Traînée sur la sphère : F_d=−6πηR w.  
Avec S=πR² : C_D=24/Re_D.  
w_lim=2(ρ_s−ρ_f)gR²/(9η), orientation vers le bas si ρ_s>ρ_f.

**Une preuve contrôlable de la force.** Pour une sphère fixe dans un courant Ue_z, la solution de Stokes a u_r=Ucosθ[1−3R/(2r)+R³/(2r³)], u_θ=−Usinθ[1−3R/(4r)−R³/(4r³)] et p−p_∞=−3ηURcosθ/(2r²). Vérifier la divergence, les frontières et l'équation constitue un certificat de solution, pas une simple courbe ajustée.

**Intégration de la traction.** Sur r=R, la traction projetée sur z vaut −p_∞cosθ+3ηU/(2R). L'intégrale du premier terme est nulle ; celle du second sur l'aire 4πR² donne 6πηRU. La pression fournit un tiers de la force et le cisaillement deux tiers. Changer de référentiel restitue une traînée opposée à la vitesse relative.

**Chute et modèle réduit.** Avec w positif vers le bas, m dw/dt=(ρ_s−ρ_f)Vg−6πηRw. Si w(0)=0, w=w_lim(1−exp(−t/τ)), τ=m/(6πηR)=2ρ_sR²/(9η). Cette loi de traînée instantanée néglige la masse ajoutée et la mémoire visqueuse : la vitesse limite permanente est plus robuste que la description des toutes premières accélérations.

**Exemple et mission.** Pour R=0,10 mm, ρ_s=2500 kg·m⁻³, ρ_f=1000 kg·m⁻³ et η=0,10 Pa·s, w_lim≈0,327 mm·s⁻¹ et Re_D≈6,54×10⁻⁴ : l'hypothèse de faible Reynolds est cohérente. Calculer Re avec la vitesse trouvée fait partie de la résolution. Comparer les forces de poids, de poussée et de traînée, puis expliquer pourquoi la même formule ne prédit pas la chute rapide d'une grosse bille dans l'eau.

## 14 · Bernoulli : une énergie sous hypothèses

*SUP → SPÉ · FLUIDE PARFAIT*

Laboratoire : `bernoulli`.

**Cadre.** Le fluide est incompressible de masse volumique constante ρ ; la viscosité est négligée, l'écoulement est permanent et la pesanteur est −g e_z. L'équation d'Euler est ρ(v·∇)v=−∇p−ρg e_z. Une ligne de courant relie les points auxquels on applique le bilan.

Sur une même ligne de courant : p/ρ+gz+|v|²/2=C.  
Charge : H=p/(ρg)+z+|v|²/(2g).  
Si l'écoulement est aussi irrotationnel, C peut être commun dans un domaine connecté.

**Preuve.** Prendre le produit scalaire d'Euler avec un déplacement dl tangent à v. L'identité (v·∇)v=∇(|v|²/2)−v×curl v montre que le terme de rotation est orthogonal à dl. On obtient la différentielle d(p/ρ+gz+|v|²/2)=0 le long de la ligne. Sans irrotationnalité, deux lignes peuvent avoir des constantes différentes.

**Venturi et Pitot.** Dans un Venturi horizontal, continuité et Bernoulli donnent p₁−p₂=(ρ/2)(U₂²−U₁²). Un Pitot compare pression statique et pression d'arrêt, p_arrêt−p=(ρ/2)U², si les pertes sont négligeables. Un liquide ralentissant vers un point d'arrêt augmente sa pression : le signe découle du bilan d'énergie.

**Exemple.** Pour de l'eau à ρ=1000 kg·m⁻³, U₁=1 m·s⁻¹ et une section divisée par deux, U₂=2 m·s⁻¹ et p₁−p₂=1500 Pa. Une dénivellation de 0,153 m d'eau représente cette pression. Une baisse de pression mesurée supérieure à cette valeur peut révéler des pertes ou un profil non uniforme ; elle ne se corrige pas en changeant arbitrairement le signe de Bernoulli.

**Mission.** Avant de calculer, indiquer si les points partagent une ligne de courant, si l'écoulement est permanent et si des machines ou pertes interviennent. Une pression négative relative à l'atmosphère peut être admissible ; une pression absolue proche de la pression de vapeur signale une limite du modèle monophasique.

## 15 · Bernoulli non stationnaire, vidange et tube en U

*SPÉ · EXTENSION GUIDÉE SELON FILIÈRE*

Laboratoire : `bernoulli`.

**Potentiel et unités.** Dans un écoulement idéal irrotationnel, on écrit localement v=∇φ, φ en m²·s⁻¹. Pour ρ constant et pesanteur uniforme, Euler devient un gradient nul. Le terme ∂ₜφ a l'unité m²·s⁻², comme p/ρ, gz et v²/2 ; il compte dans un démarrage ou une oscillation.

∂ₜφ+|∇φ|²/2+p/ρ+gz=C(t).  
Changer φ en φ+χ(t) change C en C+χ'(t), pas la vitesse.

**Démonstration et portée.** Le champ étant un gradient, ∂ₜv=∇∂ₜφ et (v·∇)v=∇(v²/2). L'équation impose donc la constance spatiale de leur somme avec p/ρ+gz ; cette constante peut dépendre du temps. Elle ne dépend pas arbitrairement du point. Supprimer ∂ₜφ exige une approximation justifiée, et non seulement une image instantanée du fluide.

**Vidange quasi stationnaire.** Pour un réservoir de section S, un petit orifice de section s et une hauteur h, l'approximation s≪S donne la vitesse de Torricelli √(2gh). Continuité : S dh/dt=−s√(2gh). Ainsi √h=√h₀−(s/S)√(g/2)t jusqu'à la vidange. Les contractions du jet et pertes réelles demandent un coefficient de débit mesuré.

**Tube en U.** Pour un tube de section constante, longueur de liquide L et déplacements ±x des surfaces, la différence de hauteur vaut 2x. La masse ρSL reçoit une force de rappel −2ρgSx : x''+(2g/L)x=0. À L=1 m, la période vaut environ 1,42 s. On doit utiliser un bilan d'accélération ; le Bernoulli permanent ne décrit pas cette oscillation.

**Mission.** Comparer un bilan de pression, un bilan de quantité de mouvement et un bilan énergétique pour le tube. Dans une vidange, préciser le domaine où h(t) reste positif et arrêter la formule à l'instant de vidage. Pour des sections variables, raisonner avec le débit et l'inertance ∫dl/S(l), plutôt qu'attribuer la même vitesse à tout le liquide.

## 16 · Potentiel, fonction de courant et circulation

*SPÉ · EXTENSION GUIDÉE SELON FILIÈRE*

Laboratoire : `vortex`.

**Objets.** Pour un champ plan incompressible, une fonction de courant locale ψ vérifie v_x=∂ᵧψ et v_y=−∂ₓψ ; ses courbes de niveau sont des lignes de courant. ψ a l'unité m²·s⁻¹. Si curl v=0, un potentiel local φ donne v=∇φ. Un potentiel global monovalué exige aussi des conditions sur la topologie du domaine.

div v=0 ; ω_z=∂ₓv_y−∂ᵧv_x=−Δψ.  
Potentiel irrotationnel et incompressible : Δφ=0.  
f(z)=φ+iψ ; f'(z)=v_x−iv_y dans un domaine analytique.

**Preuve géométrique.** Calculer ∇ψ·v donne ψ_xψ_y−ψ_yψ_x=0 : ψ reste constant le long d'une ligne de courant instantanée. Lorsque v=∇φ, les lignes ψ=constante et φ=constante sont orthogonales hors des points où v=0. Ces relations concernent le potentiel scalaire plan ; les niveaux d'un potentiel vectoriel 3D ne définissent pas directement les lignes de courant.

**Source et puits.** Un débit par unité de profondeur q, en m²·s⁻¹, impose 2πr v_r=q. Donc v_r=q/(2πr), φ=(q/2π)ln(r/a). q>0 décrit une source et q<0 un puits. Le logarithme emploie un rapport sans dimension ; l'axe ponctuel est exclu du domaine du modèle.

**Le contre-exemple du tourbillon.** Avec v_θ=Γ/(2πr), la vorticité est nulle pour r>0, mais ∮v·dl=Γ. Le potentiel φ=Γθ/(2π) change de Γ après un tour complet : il n'est pas monovalué sur l'anneau. L'absence locale de rotation ne suffit donc pas à assurer un potentiel global. Stokes ne s'applique pas à un disque contenant une singularité non incluse dans le domaine.

**Mission.** Lire séparément le champ de vitesse, les lignes de courant et la circulation. Vérifier les signes d'une source, d'un puits et d'un tourbillon. La superposition de potentiels est licite pour l'équation de Laplace ; les pressions obtenues ensuite par Bernoulli comportent v² et ne se superposent pas linéairement.

## 17 · Rankine : un cœur tournant sans singularité de vitesse

*SPÉ · TP TOURBILLON*

Laboratoire : `vortex`.

**Modèle.** Le tourbillon de Rankine est plan, permanent et incompressible. Le cœur r≤a tourne comme un solide avec Ω, en s⁻¹ ; à l'extérieur, la circulation est constante et la vorticité nulle. Le champ n'a qu'une composante azimutale v_θ(r). On néglige les vitesses verticale et radiale ainsi que les variations verticales de pression.

v_θ=Ωr si r≤a ; v_θ=Ωa²/r si r≥a.  
Γ(r)=2πr v_θ ; ω_z=2Ω dans le cœur, 0 à l'extérieur.  
p(r)−p_∞=ρΩ²(r²/2−a²), r≤a.  
p(r)−p_∞=−ρΩ²a⁴/(2r²), r≥a.

**Preuve du champ.** Dans le cœur, la circulation est l'intégrale de la vorticité sur le disque : Γ=2Ωπr². À l'extérieur, agrandir le contour n'ajoute plus de vorticité et Γ=2πΩa². Les deux vitesses coïncident à r=a ; la vitesse est nulle sur l'axe et maximale au raccord, au lieu de diverger comme celle d'un vortex ponctuel.

**Preuve de la pression.** L'accélération centripète est −v_θ²/r. Euler donne dp/dr=ρv_θ²/r. Intégrer d'abord depuis l'infini pour la partie extérieure, puis raccorder la pression à r=a pour le cœur. On obtient p(0)=p_∞−ρΩ²a². Appliquer une constante de Bernoulli unique au cœur rotationnel aurait fourni un résultat incorrect.

**Exemple.** Avec ρ=1,2 kg·m⁻³, Ω=4 s⁻¹ et a=5 m, la vitesse maximale vaut 20 m·s⁻¹ et la baisse de pression centrale 480 Pa. Le modèle représente un mécanisme centrifuge, pas une prévision complète de tornade : transport vertical, turbulence et échanges de chaleur ne sont pas résolus.

**Mission.** Comparer les courbes de vitesse, vorticité, circulation et pression ; elles ne portent ni la même unité ni les mêmes raccords. Faire varier a à Ω fixé, puis Ω à circulation fixée : les deux expériences ne donnent pas le même changement de vitesse maximale. Vérifier la continuité de p et v, sans imposer celle de la vorticité.

## 18 · Cylindre, circulation et effet Magnus

*SPÉ · PORTANCE IDÉALE*

Laboratoire : `magnus`.

**Objets et convention.** Un cylindre de rayon a est plongé dans un courant Ue_x. Le fluide est idéal, incompressible et irrotationnel hors du cylindre. Γ est une circulation prescrite, positive dans le sens trigonométrique. La force calculée est par unité de longueur du cylindre, en N·m⁻¹ ; le modèle n'est pas celui d'une sphère ou d'un ballon.

φ=U(r+a²/r)cosθ+Γθ/(2π).  
v_r=U(1−a²/r²)cosθ ; v_θ=−U(1+a²/r²)sinθ+Γ/(2πr).  
Sur r=a : p=p_∞+(ρ/2)[U²−v_θ²].  
F_x'=0 ; F_y'=−ρUΓ.

**Construction.** La solution harmonique U(r+a²/r)cosθ est choisie pour retrouver le courant loin du cylindre et v_r=0 sur sa surface. Ajouter le vortex ne modifie pas cette imperméabilité. Son potentiel est multivalué, mais sa vitesse est bien définie hors de l'axe. Il faut conserver cette distinction pour lire correctement la circulation.

**Preuve de la portance.** Écrire v_θ(a)=−2U sinθ+Γ/(2πa), puis intégrer la traction −p a(cosθ,sinθ)dθ. Les termes constants et quadratiques en sinθ ne contribuent pas à F_y ; le terme croisé donne −ρUΓ. Les termes de F_x s'annulent. Avec la convention choisie, une circulation positive et un courant vers +x donnent donc une force vers −y.

**Exemple interprété.** Pour ρ=1,2 kg·m⁻³, U=10 m·s⁻¹ et Γ=0,80 m²·s⁻¹, F_y'=−9,6 N·m⁻¹. Inverser Γ inverse la portance. Le modèle a une traînée nulle, résultat de d'Alembert sous ses hypothèses ; la traînée réelle et le sillage exigent la viscosité et souvent la séparation.

**Mission et limite de la rotation imposée.** Suivre les points d'arrêt et le profil de pression. Le choix Γ=2πa²Ω peut représenter une fermeture simple de circulation associée à une rotation, mais ne démontre pas l'adhérence sur toute la surface dans le courant U. Le modèle idéal prend Γ comme donnée ; le mécanisme réel de sélection de cette circulation dépend des frontières et de la viscosité.

## 19 · Hydrostatique, Archimède et atmosphère

*SUP → SPÉ · TP DE STATIQUE*

Laboratoire : `hydrostatique`.

**Objets et signes.** La cote z croît vers le haut ; la pesanteur vaut −g e_z. Dans un fluide au repos, ∇p=ρg_vec, donc dp/dz=−ρg. La pression p est en Pa et peut être absolue ou relative à l'atmosphère : il faut préciser la référence. La masse volumique peut varier avec z.

Liquide de ρ uniforme : p(z)=p(z₀)−ρg(z−z₀).  
Force de pression : −∫_S p n dS.  
Poussée : F_A=−∫_V ρg_vec dV ; uniforme : F_A=−ρV_immergé g_vec.

**Preuve d'Archimède.** La surface du solide enferme le volume qui serait occupé par le fluide déplacé. Le théorème de Gauss transforme −∫p n dS en −∫∇p dV, puis l'hydrostatique donne l'opposé du poids du fluide déplacé. La poussée s'applique au centre de masse de ce volume de fluide ; il ne coïncide pas forcément avec le centre de masse du solide.

**Exemple et flottabilité.** À 3,0 m sous une surface d'eau de ρ=1000 kg·m⁻³, la surpression est 29,4 kPa pour g=9,81 m·s⁻². Un solide homogène de densité 600 kg·m⁻³ flotte avec 60 % de son volume immergé, si aucune autre force verticale n'intervient. La stabilité au roulis demande en plus un bilan de moments et la position du métacentre ; l'équilibre vertical seul ne suffit pas.

**Atmosphère isotherme.** Pour un gaz parfait de température T constante et masse molaire M en kg·mol⁻¹, ρ=Mp/(RT). L'équation dp/dz=−Mgp/(RT) donne p=p₀exp(−z/H), H=RT/(Mg). À T=293 K et M=0,029 kg·mol⁻¹, H≈8,56 km. Ce modèle n'impose pas que l'atmosphère réelle soit isotherme.

**Mission.** Distinguer un gradient de pression d'une pression uniforme ajoutée. Refaire un manomètre par égalité des pressions à une même altitude dans chaque liquide connecté. Pour un récipient en rotation solide, l'accélération radiale conduit à la surface z=z_c+Ω²r²/(2g) ; une force centrifuge n'est pas une seconde pesanteur uniforme.

## 20 · Capillarité : courbure, énergie et loi de Jurin

*SUP → SPÉ · INTERFACES*

Laboratoire : `hydrostatique`.

**Grandeurs et hypothèses.** La tension superficielle γ est en N·m⁻¹, équivalent à J·m⁻². Elle représente un coût d'aire à température et composition fixées. L'angle de contact θ est mesuré dans le liquide et dépend du couple de matériaux et de l'état de surface. Dans le modèle idéal de Young, réduire le rayon du tube ne fixe pas à lui seul cet angle.

Saut de pression : p_int−p_ext=γ(1/R₁+1/R₂), courbures orientées.  
Goutte ou bulle à une interface sphérique : Δp=2γ/a.  
Bulle de savon à deux interfaces : Δp≈4γ/a.  
Jurin : h=2γ cosθ/(ρgR).

**Preuve énergétique pour une sphère.** Une augmentation da fait varier l'aire de 8πa da et le volume de 4πa² da. Équilibrer le travail Δp dV et le coût γ dS donne Δp=2γ/a. Une pellicule avec deux interfaces a environ le double de coût. La formule montre pourquoi il faut identifier les surfaces présentes avant de compter un facteur deux.

**Preuve de Jurin.** Dans un tube de rayon R, la tension tire verticalement avec la résultante 2πRγ cosθ. Le poids d'une colonne de hauteur h est ρgπR²h. Leur équilibre donne Jurin si le réservoir est grand et l'effet du volume du ménisque négligeable. cosθ>0 produit une montée ; cosθ<0 une dépression.

**Exemple et nombre de Bond.** Pour γ=0,072 N·m⁻¹, ρ=1000 kg·m⁻³, R=0,50 mm et θ=0, h≈2,94 cm. Le nombre Bo=ρgR²/γ≈0,034 compare gravité et capillarité ; il est petit. Une goutte de rayon 1 mm présente une surpression de 144 Pa, même si son intérieur semble macroscopiquement au repos.

**Mission.** Prédire la hauteur en doublant R, puis en changeant le signe de cosθ. Contrôler l'énergie associée à une aire créée. La capillarité intervient aussi dans la dispersion de la houle : une courbure variable de la surface ajoute une force de rappel qui devient importante aux petites longueurs d'onde.

## 21 · Houle : des frontières à la dispersion

*SPÉ · TP PRIORITAIRE DE SURFACE*

Laboratoire : `houle`.

**Objets et hypothèses.** Une couche d'eau de profondeur h repose sur un fond z=−h ; la surface moyenne est z=0. L'élévation ξ(x,t)=a cos(kx−ωt) a une amplitude a en m. k=2π/λ est en m⁻¹ et ω=2πf en s⁻¹. Le fluide est idéal, incompressible et irrotationnel ; on linéarise si ka≪1 et a/h≪1.

**Équations aux frontières.** Le potentiel φ satisfait Δφ=0. Le fond impose ∂_zφ=0 à z=−h. À la surface linéarisée, ∂ₜξ=∂_zφ exprime que la surface se déplace avec le fluide. La condition dynamique vaut ∂ₜφ+gξ−(γ/ρ)∂²_xξ=0 ; la courbure fournit une force de rappel supplémentaire.

φ=(aω/k)[cosh(k(z+h))/sinh(kh)] sin(kx−ωt).  
ω²=(gk+γk³/ρ)tanh(kh).  
Sans capillarité : ω²=gk tanh(kh).

**Démonstration.** Une dépendance sinusoïdale en x transforme Laplace en f''−k²f=0. L'imperméabilité du fond sélectionne cosh(k(z+h)). La condition cinématique fixe le coefficient du potentiel. Substituer ensuite dans la condition dynamique donne la relation de dispersion ; on ne choisit pas indépendamment f et λ pour une onde libre donnée.

**Orbites matérielles.** Au premier ordre, les déplacements horizontal et vertical d'une particule à la profondeur z₀ ont les amplitudes a cosh(k(z₀+h))/sinh(kh) et a sinh(k(z₀+h))/sinh(kh). Les orbites sont des ellipses, circulaires en eau profonde, aplaties près du fond. Leur moyenne de déplacement est nulle à cet ordre ; une dérive de Stokes est un effet d'ordre supérieur non résolu par cette linéarisation.

**Exemple interprété.** Pour λ=h=1 m, g=9,81 m·s⁻² et une capillarité négligée, k=2π m⁻¹ et f≈1,25 Hz. Avec a=1 cm, ka≈0,063 et a/h=0,01, la faible amplitude est cohérente. Une image seule de la surface ne donne pas la profondeur ni les trajectoires : les orbites doivent être reconstruites à partir du champ sous la surface.

**Mission.** Prévoir l'effet de h sur ω à λ fixé, puis suivre une crête et une particule séparément. Vérifier les conditions au fond et la pente de la surface. La cuve du recueil devient ici un laboratoire de comparaison des données mesurées et de la relation de dispersion, avec hypothèses annoncées.

## 22 · Phase, groupe, capillarité et paquet de houle

*SPÉ · DISPERSION ET ÉNERGIE*

Laboratoire : `houle`.

**Variables.** Une crête d'onde monochromatique se déplace à c_φ=ω/k. L'enveloppe d'un paquet étroit de nombres d'onde se déplace à c_g=dω/dk. Ces vitesses sont en m·s⁻¹. Elles ne sont pas les vitesses instantanées des particules d'eau, qui oscillent avec des amplitudes proportionnelles à aω.

Gravité seule : c_g/c_φ=½[1+2kh/sinh(2kh)].  
Eau profonde : c_φ=√(g/k), c_g=c_φ/2.  
Eau peu profonde, kh≪1 : c_φ≈c_g≈√(gh).

**Preuve du groupe.** Superposer deux ondes proches (k,ω) et (k+δk,ω+δω). L'identité trigonométrique sépare une oscillation rapide et une enveloppe cos[(δk x−δω t)/2]. Sa vitesse est δω/δk, qui tend vers dω/dk. Différencier ω²=gk tanh(kh) donne la formule affichée et ses deux limites.

**Capillarité et minimum.** En eau profonde, c_φ²=g/k+γk/ρ. La dérivée s'annule pour k*=√(ρg/γ). Pour de l'eau avec γ=0,072 N·m⁻¹ et ρ=1000 kg·m⁻³, λ*≈1,70 cm et la vitesse minimale vaut environ 0,231 m·s⁻¹. En régime capillaire dominant, ω∝k³ᐟ² et c_g=3c_φ/2 : le groupe peut avancer plus vite que les crêtes.

**Énergie et impact.** Pour la houle gravitaire linéaire, l'énergie moyenne par unité de surface est ρga²/2 et son flux par unité de largeur est cette énergie fois c_g. Un impact ponctuel excite de nombreux k. En eau profonde, la phase kr−√(gk)t est stationnaire pour k≈gt²/(4r²), donnant la phase dominante −gt²/(4r). L'amplitude dépend aussi du spectre de la source et de la géométrie ; une loi universelle 1/r ne se déduit pas de cette phase seule.

**Exemple et mission.** Pour λ=1 m en eau profonde sans capillarité, c_φ≈1,25 m·s⁻¹ et c_g≈0,625 m·s⁻¹. Observer des crêtes qui traversent un paquet illustre cette différence. Mesurer les deux vitesses sur des distances et temps déclarés ; ne pas attribuer au fluide le déplacement de l'enveloppe.

## 23 · Acoustique : linéariser un fluide compressible

*SUP → SPÉ · TP D'ONDES*

Laboratoire : `acoustique`.

**Objets et approximation.** Autour d'un équilibre uniforme au repos, écrire p=p₀+p₁, ρ=ρ₀+ρ₁ et v=v₁. p₁ est une surpression en Pa, v₁ une vitesse particulaire en m·s⁻¹ et ρ₁ une variation en kg·m⁻³. On garde les termes de premier ordre si |p₁|≪p₀, |ρ₁|≪ρ₀ et |v₁|≪c.

ρ₀∂ₜv₁=−∇p₁ ; ∂ₜρ₁+ρ₀ div v₁=0.  
p₁=c²ρ₁ ; c²=(∂p/∂ρ)_s=1/(ρ₀χ_s).  
∂²ₜp₁=c²Δp₁ ; ω²=c²k².

**Démonstration.** La continuité et Euler linéarisés donnent deux équations couplées. Prendre la divergence d'Euler, dériver la continuité en t et éliminer v₁ donne ∂²ₜρ₁=Δp₁. La relation thermodynamique isentropique p₁=c²ρ₁ ferme le système. Le gaz est compressible, même si l'amplitude de cette compression est petite.

**Vitesse et propagation.** En 1D, p₁=f(t−x/c)+g(t+x/c). Une onde droite exp[i(kx−ωt)] avec k>0 a c_φ=c_g=c dans le modèle non dispersif. La vitesse v₁ est un mouvement oscillant local ; elle n'est pas égale à c. Pour un gaz parfait, c=√(γRT/M), où M est en kg·mol⁻¹ et γ=c_p/c_v.

**Exemple.** Avec γ=1,4, T=290 K et M=0,029 kg·mol⁻¹, c≈341 m·s⁻¹. Une onde de fréquence 200 Hz a λ≈1,71 m. Une variation de température change c : une longueur d'onde mesurée sans température déclarée ne donne pas une fréquence universelle.

**Extension dissipative.** En négligeant la conduction thermique, une viscosité longitudinale ν_l=(4η/3+ζ)/ρ₀ donne p₁,tt−c²Δp₁−ν_l∂ₜΔp₁=0. Avec exp[i(kx−ωt)], k²(1−iωτ)=ω²/c², τ=ν_l/c² ; choisir Im k>0 pour une atténuation vers +x. Si ωτ≪1, Im k≈ν_lω²/(2c³). Les pertes thermiques, de relaxation et de paroi ne sont pas incluses dans ce seul terme.

**Mission.** Comparer surpression, déplacement et vitesse particulaire, puis retrouver l'équation d'onde depuis les bilans. Annoncer la convention complexe avant de lire le signe d'une atténuation. L'acoustique ne remplace pas le fluide par un transport de particules à la célérité c.

## 24 · Impédance, réflexion et intensité acoustique

*SUP → SPÉ · ÉNERGIE ET INTERFACES*

Laboratoire : `acoustique`.

**Objets et unités.** L'impédance acoustique d'une onde plane est Z=ρ₀c en Pa·s·m⁻¹. Avec x orienté vers la droite, une onde allant à droite satisfait p₁=Zv₁,x ; une onde à gauche satisfait p₁=−Zv₁,x. Il faut préciser si un coefficient de réflexion concerne la pression ou la composante de vitesse.

e=ρ₀|v₁|²/2+p₁²/(2ρ₀c²) ; flux J=p₁v₁.  
Onde plane progressive : I=p̂²/(2Z)=p_rms²/Z.  
r_p=(Z₂−Z₁)/(Z₁+Z₂) ; t_p=2Z₂/(Z₁+Z₂).  
r_v=−r_p ; t_v=2Z₁/(Z₁+Z₂).

**Preuve énergétique.** Multiplier Euler linéarisé par v₁ et l'équation de pression par p₁/(ρ₀c²). La somme donne ∂ₜe+div(p₁v₁)=0. Pour une sinusoïde de pression d'amplitude crête p̂, la moyenne de cos² est 1/2 ; cela explique le facteur deux entre amplitude crête et efficace.

**Raccordement à incidence normale.** Deux fluides idéaux en contact ont une pression et une vitesse normale continues. Écrire p_i+p_r=p_t et (p_i−p_r)/Z₁=p_t/Z₂ donne r_p et t_p. Les fractions d'intensité sont R=r_p² et T=(Z₁/Z₂)t_p²=4Z₁Z₂/(Z₁+Z₂)² ; elles satisfont R+T=1 sans absorption.

**Exemple et décibels.** Si Z₂=4Z₁, r_p=0,6 et t_p=1,6, mais R=0,36 et T=0,64. Une amplitude transmise supérieure à l'incidente ne crée pas d'énergie : son impédance change. Le niveau L_I=10log₁₀(I/I₀), avec I₀=10⁻¹² W·m⁻², vaut 70 dB pour I=10⁻⁵ W·m⁻².

**Mission.** Retrouver séparément les signes de pression et de vitesse réfléchies. Dix sources incohérentes d'intensité égale ajoutent 10 dB ; dix amplitudes identiques parfaitement cohérentes et en phase peuvent ajouter 20 dB au point étudié. La règle d'addition demande donc une hypothèse sur les phases, pas seulement le nombre de sources.

## 25 · Son guidé : modes, coupure et onde évanescente

*SPÉ · SÉPARATION DES VARIABLES*

Laboratoire : `conduit`.

**Géométrie.** Un conduit rectangulaire rigide a une section a×b ; x∈[0,a], y∈[0,b] et l'axe de propagation est z. On néglige les pertes. La paroi impose une vitesse normale nulle ; Euler acoustique transforme cette condition en dérivée normale de pression nulle. Il s'agit de Neumann, pas de pression nulle sur les murs.

p̂_mn∝cos(mπx/a)cos(nπy/b) exp(ik_z z).  
k_c²=(mπ/a)²+(nπ/b)² ; k_z²=ω²/c²−k_c².  
ω_c=ck_c ; f_c=(c/2)√[(m/a)²+(n/b)²].  
Pour ω>ω_c : c_φ,z=ω/k_z ; c_g,z=c²k_z/ω ; c_φ,z c_g,z=c².

**Démonstration.** Chercher un produit X(x)Y(y)Z(z) dans Helmholtz Δp̂+(ω/c)²p̂=0. Les dérivées nulles aux murs sélectionnent les cosinus et leurs nombres d'onde discrets. La dispersion restante dépend de k_z. Différencier ω²=c²(k_z²+k_c²) donne le groupe axial, différent de c pour un mode transversal non uniforme.

**Trois régimes.** Le mode (0,0) a k_c=0 : il n'a pas de coupure. Pour un autre mode et ω<ω_c, k_z=iκ, et une branche décroît comme exp(−κz) ; elle est évanescente. À la coupure, k_z=0 et le flux axial propagatif s'annule dans le modèle idéal. La propagation axiale d'un mode non uniforme demande donc strictement ω>ω_c.

**Exemple du recueil.** Avec a=5 mm, b=10 mm et c=340 m·s⁻¹, f_c,01=17 kHz et f_c,10=34 kHz. Cela ne signifie pas qu'aucun son inférieur à 17 kHz ne traverse le conduit : le mode plan (0,0) existe. À f=20 kHz pour (0,1), c_g,z≈179 m·s⁻¹ et c_φ,z≈645 m·s⁻¹.

**Mission.** Identifier les indices du mode avant de changer la fréquence. Observer les nœuds transversaux, la distance d'atténuation sous coupure et le paquet au-dessus. Une vitesse de phase supérieure à c dans un guide ne constitue pas un transport de l'énergie à cette vitesse ; les conditions aux extrémités déterminent en plus des résonances éventuelles.

## 26 · Diffraction, Fourier et ambiguïtés de mesure

*SUP → SPÉ · TP DE SIGNAUX*

Laboratoire : `diffraction`.

**Objets et régime.** Une ouverture de largeur a reçoit une onde monochromatique de longueur λ=c/f. Dans un modèle scalaire de fente uniformément excitée, au champ lointain, les contributions sont additionnées en amplitude. θ est un angle depuis l'axe ; une directivité réelle peut aussi dépendre de l'émetteur, du récepteur et des bords.

A(θ)/A(0)=sin q/q ; q=πa sinθ/λ, limite 1 en q=0.  
I(θ)/I(0)=(sin q/q)².  
Premier zéro : sinθ=λ/a, seulement si λ≤a.  
Si θ≪1 et λ≪a : θ≈λ/a.

**Preuve par une intégrale.** Les points x de la fente ont un déphasage kx sinθ. Intégrer exp(ikx sinθ) de −a/2 à a/2 donne a sin q/q. C'est une transformée de Fourier de l'ouverture. Mettre la moyenne de l'intensité à la place de cette somme d'amplitudes détruirait les interférences et les zéros.

**Le TP de 25 kHz.** Avec c=340 m·s⁻¹, λ=13,6 mm. Pour a=10 mm, λ/a=1,36>1 : il n'existe aucun premier zéro physique dans |θ|≤π/2. La valeur 1,36 rad n'est donc pas un angle de premier minimum obtenu par approximation des petits angles. Le modèle prédit un étalement large ; on peut définir une largeur à mi-hauteur et préciser cette convention.

**Bruit et Fourier.** Un son périodique peut présenter des harmoniques ; un bruit peut aussi être analysé spectralement, avec un spectre souvent large ou continu. Tout enregistrement fini possède une transformée discrète de Fourier. Le timbre ne se réduit pas à une seule fréquence, et une période apparente demande de distinguer fondamental, harmonique dominant et fenêtre de mesure.

**Échantillonnage et stroboscope.** Aux instants n/f_s, des fréquences séparées d'un multiple de f_s ont les mêmes phases. Un échantillonnage uniforme ne distingue donc pas ces signaux sans hypothèse de bande et filtrage préalable. Une image immobile sous des éclairs à 50 Hz peut correspondre à plusieurs fréquences de vibration ; connaître la fréquence d'excitation ou varier progressivement le stroboscope lève l'ambiguïté.

**Mission.** Prédire l'existence d'un zéro avant de chercher son angle. Comparer une aperture, son spectre et sa diffraction, puis examiner un alias de fréquence ou un battement stroboscopique. Annoter longueur, angle, fréquence d'échantillonnage et régime de champ lointain : ils répondent à des questions différentes.

## 27 · Thermodynamique : isentropique, isotherme et dissipation

*SPÉ · COUPLAGE GUIDÉ*

Laboratoire : `thermo`.

**Objets et unités.** Pour un gaz parfait, p=ρRT/M, avec T en K, M en kg·mol⁻¹ et γ=c_p/c_v. Les compressibilités χ_T et χ_s sont en Pa⁻¹ ; l'indice s fixe l'entropie massique. La conductivité thermique κ_th, en W·m⁻¹·K⁻¹, est distincte de la viscosité η. La diffusivité thermique D_th est en m²·s⁻¹.

χ_T=1/p ; χ_s=1/(γp).  
c_T=√(RT/M) ; c_s=√(γRT/M).  
Énergie interne : ρDₜe=−p div v+Φ−div q+r.  
Fourier : q=−κ_th∇T ; Φ=τ:∇v≥0.

**Démonstration thermodynamique.** À T fixe, p est proportionnel à ρ, donc (∂p/∂ρ)_T=RT/M. Pour une transformation isentropique d'un gaz parfait à γ constant, pρ⁻γ est constant ; sa dérivation donne (∂p/∂ρ)_s=γp/ρ. Ces deux célérités décrivent deux limites physiques, pas deux choix arbitraires de calcul.

**Échelle de diffusion thermique.** Une variation périodique à la pulsation ω diffuse sur δ_th=√(2D_th/ω). Dans une onde, la longueur réduite λ/(2π)=c/ω fournit une échelle de comparaison ; un petit rapport δ_th/(λ/2π) favorise une approximation locale isentropique dans le volume. Dans un petit conduit, comparer aussi δ_th au rayon ou à l'écartement des parois : des couches thermiques peuvent modifier ce diagnostic.

**Exemple.** Avec T=290 K, M=0,029 kg·mol⁻¹ et γ=1,4, c_T≈288 m·s⁻¹ et c_s≈341 m·s⁻¹. Pour D_th=2,0×10⁻⁵ m²·s⁻¹ à 1 kHz, δ_th≈80 µm. Cette épaisseur est petite devant c_s/ω≈54 mm, mais pas devant un canal de rayon 50 µm. Le laboratoire compare ces échelles ; il ne prétend pas interpoler une célérité universelle entre les deux limites.

**Dissipation et mission.** Dans le Couette de la leçon 8, Φ=4000 W·m⁻³. Avec ρ=1000 kg·m⁻³ et une capacité massique effective c=4000 J·kg⁻¹·K⁻¹, un modèle uniforme sans perte donne dT/dt=0,001 K·s⁻¹. Retrouver cette chaleur depuis la puissance de la plaque, puis annoncer les frontières thermiques. Euler sans dissipation, Navier–Stokes isotherme et un modèle thermiquement fermé ne décrivent pas le même système.

## 28 · MHD : courants, freinage de Hartmann et ondes d'Alfvén

*SPÉ · EXTENSION ÉLECTROMAGNÉTIQUE GUIDÉE*

Laboratoire : `mhd`.

**Objets et unités.** Un fluide conducteur possède une conductivité électrique σ_e en S·m⁻¹. B est l'induction magnétique en T, j le courant en A·m⁻² et μ₀ la perméabilité. La loi d'Ohm mobile j=σ_e(E+v×B) couple mouvement et courant. La force volumique de Lorentz est j×B ; sa direction dépend des champs et de la fermeture du circuit.

ρDₜv=−∇p+ηΔv+j×B.  
∂ₜB=curl(v×B)+η_BΔB ; div B=0 ; η_B=1/(μ₀σ_e).  
Rm=UL/η_B=μ₀σ_eUL : Reynolds magnétique, différent de Re.

**Hartmann : hypothèses particulières.** Le canal a des parois y=±h, h étant ici la demi-largeur. L'écoulement u(y)e_x est poussé par G=−∂ₓp>0 et B=B e_y. Dans un circuit transversal court-circuité, E_z=0 donne j_z=σ_euB et une force −σ_eB²u e_x. On suppose Rm≪1 pour négliger la modification du champ imposé. Un canal isolé électriquement peut créer un E_z différent : ce résultat n'est pas indépendant du circuit.

ηu''−σ_eB²u+G=0 ; u(±h)=0.  
Ha=Bh√(σ_e/η).  
u(y)=G/(σ_eB²)[1−cosh(Ha y/h)/cosh(Ha)].  
B→0 : u→G(h²−y²)/(2η), Poiseuille plan.

**Preuve et énergie.** Résoudre l'équation différentielle avec sa symétrie et les deux parois donne le cosinus hyperbolique. Son développement à petit B fournit le profil parabolique ; la formule avec B au dénominateur demande cette limite, pas une division par zéro. Le freinage mécanique alimente la dissipation Joule j²/σ_e. Avec un champ et un circuit imposés, suivre les échanges électriques fait partie du bilan total.

**Un autre régime : Alfvén idéal.** Autour d'un fluide uniforme au repos et B₀e_z, des perturbations transverses u,b variant selon z satisfont ρ∂ₜu=(B₀/μ₀)∂_zb et ∂ₜb=B₀∂_zu, en négligeant les dissipations. Elles donnent une onde à c_A=B₀/√(μ₀ρ), avec énergies cinétique et magnétique égales pour une onde progressive. Ce régime de champ transporté idéal ne se confond pas avec l'approximation de Hartmann à faible Rm.

**Exemple et mission.** Dans un modèle conducteur ρ=6000 kg·m⁻³, σ_e=3,0×10⁶ S·m⁻¹ et B=0,20 T, un mouvement uniforme avec E_z=0 s'amortit sur ρ/(σ_eB²)=0,050 s. Déclarer le sens de v×B et de j×B avant de lire le freinage. Comparer ensuite Re, Rm et Ha : chacun confronte des mécanismes différents. Le couplage MHD est une extension guidée, avec appui sur mécanique, thermodynamique et électromagnétisme.

## Les dix-huit missions de laboratoire

### cinematique

Distinguer un champ de vitesse mesuré en des points fixes, la trajectoire d'une particule et une ligne de courant instantanée. Suivre aussi un élément matériel pour relier sa forme à la conservation de la masse.

Leçons de référence : 1, 2, 3.

**Techniques à mobiliser**

- Intégrer dR/dt=v(R,t) et appliquer la règle de la chaîne.
- Construire un flux orienté et contrôler div v.
- Comparer géométrie instantanée et évolution temporelle.

**Prédire → expérimenter → justifier**

1. Prédire la trajectoire d'un point dans le champ permanent proposé et distinguer trajectoire et ligne de courant par leur définition.
2. Suivre la même particule et un petit élément matériel dans le laboratoire ; comparer leur déplacement aux lignes de courant du champ permanent. Le champ instationnaire de l'exercice 2 se traite ensuite sur papier, sans commande correspondante dans ce laboratoire.
3. Justifier l'accélération par la dérivée matérielle, puis vérifier si le changement d'aire est compatible avec div v et le bilan de masse.

**Entrées et approfondissements**

- Sup : Mobiliser dérivation, intégration et bilans de débit ; définir chaque courbe avant de la lire.
- Spé : Réutiliser les équations différentielles et les champs de vecteurs pour distinguer descriptions spatiale et matérielle.
- Approfondissement : La description lagrangienne et l'étude locale du gradient sont des extensions selon la filière ; elles sont explicitées dans les leçons.

**Résultat attendu.** Expliquer sur un exemple pourquoi une vitesse locale indépendante du temps peut produire une accélération, et pourquoi une ligne de courant n'est pas toujours une trajectoire.

### newtonien

Relier la déformation d'un petit élément de fluide à la contrainte visqueuse et à la puissance dissipée. Comparer un cisaillement et une rotation rigide qui peuvent avoir des vitesses comparables.

Leçons de référence : 3, 4, 5.

**Techniques à mobiliser**

- Séparer le gradient en partie symétrique D et antisymétrique W.
- Former la traction σn sur une face orientée.
- Contrôler les unités et la positivité de 2ηD:D.

**Prédire → expérimenter → justifier**

1. Prédire quel mouvement déforme les distances entre deux points et lequel les conserve : cisaillement, rotation ou dilatation.
2. Observer l'élément matériel, le tenseur de contrainte et la dissipation en changeant la viscosité dynamique ; repérer ce qui change proportionnellement à η.
3. Justifier la dissipation par D:W=0 et expliquer pourquoi ν=η/ρ ne remplace pas η dans une contrainte en Pa.

**Entrées et approfondissements**

- Sup : Distinguer force, force par aire, viscosité dynamique et gradient de vitesse à partir de leurs unités.
- Spé : Mobiliser matrices symétriques et antisymétriques, produit scalaire et loi constitutive.
- Approfondissement : Le calcul tensoriel local est une extension accompagnée selon la filière ; les fluides non newtoniens exigent une autre loi.

**Résultat attendu.** Déterminer une traction avec sa normale et reconnaître une rotation rigide sans dissipation visqueuse de cisaillement.

### couette

Construire le profil entre une plaque mobile et une plaque fixe, puis relier le travail de la plaque à la dissipation dans le fluide. Comprendre la superposition du cisaillement et d'un entraînement par pression.

Leçons de référence : 4, 8, 11.

**Techniques à mobiliser**

- Intégrer u''=0 avec deux conditions d'adhérence.
- Intégrer un profil pour calculer le débit par largeur.
- Comparer puissance mécanique reçue et dissipation volumique.

**Prédire → expérimenter → justifier**

1. Prédire l'effet de doubler l'entrefer h à vitesse de plaque U fixée sur le gradient, la contrainte et le débit.
2. Comparer profils et puissances pour deux entrefers ; si la pression est aussi motrice, repérer une éventuelle zone de retour près d'une paroi.
3. Retrouver le profil par les conditions aux limites et intégrer η(u')² ; annoncer le sens de la traction sur la plaque mobile.

**Entrées et approfondissements**

- Sup : Faire travailler fonctions affines, intégrales et bilan de puissance dans une géométrie simple.
- Spé : Justifier la réduction de l'équation de mouvement et analyser un profil Couette–Poiseuille.
- Approfondissement : La résolution exacte d'un écoulement permanent ne prouve pas sa stabilité envers toutes les perturbations ; l'échauffement demande un bilan thermique.

**Résultat attendu.** Retrouver la force à fournir, son signe et la puissance par unité d'aire sans confondre une composante de contrainte et la traction sur une face.

### poiseuille

Expliquer la sensibilité du débit au rayon d'un tube et les associations de résistances hydrauliques. Distinguer pression imposée, débit imposé, vitesse centrale et vitesse moyenne.

Leçons de référence : 7, 9, 10.

**Techniques à mobiliser**

- Résoudre l'équation radiale avec régularité sur l'axe et adhérence au bord.
- Intégrer sur des couronnes 2πr dr.
- Associer résistances en série et en parallèle à partir des bilans.

**Prédire → expérimenter → justifier**

1. À Δp=p_entrée−p_sortie fixé, prédire le rapport des débits lorsque le rayon est multiplié par deux. Le renversement de signe de Δp se raisonne ensuite sur papier, car le laboratoire propose une chute de pression positive.
2. Comparer profil, débit, puissance et nombre de Reynolds dans le tube proposé. Le réseau de branches est un prolongement sur papier avec l'exercice 12, sans commande de réseau dans ce laboratoire.
3. Démontrer Q=πR⁴Δp/(8ηL), puis retrouver sur papier les lois d'association en conservant les débits aux jonctions.

**Entrées et approfondissements**

- Sup : Calculer un débit par intégration et réutiliser les associations de résistances.
- Spé : Contrôler les hypothèses de profil développé, les pertes de charge et les conventions Darcy/Fanning.
- Approfondissement : Les pertes turbulentes ou d'entrée demandent d'autres lois ; le seuil de transition n'est pas universel.

**Résultat attendu.** Justifier la loi en R⁴, vérifier Re avec le diamètre annoncé et dire quelles conclusions dépendent du régime laminaire développé.

### diffusion

Voir comment le mouvement d'une paroi pénètre dans un fluide initialement immobile. Comparer la diffusion dans un demi-espace et l'approche d'un profil de Couette dans une couche finie.

Leçons de référence : 5, 8, 11.

**Techniques à mobiliser**

- Chercher une variable de similitude y/(2√(νt)).
- Lire une solution erfc et des modes de Fourier amortis.
- Comparer des temps à h²/ν.

**Prédire → expérimenter → justifier**

1. Prédire la profondeur pénétrée lorsque le temps est multiplié par quatre et distinguer un demi-espace d'un canal de hauteur h.
2. Comparer les profils à plusieurs instants, puis changer ν ; dans le canal fini, observer le rapprochement du profil linéaire final.
3. Retrouver δ=2√(νt), vérifier ∂ₜu=νu_yy et expliquer pourquoi les grands indices de Fourier disparaissent plus vite.

**Entrées et approfondissements**

- Sup : Utiliser analyse dimensionnelle, fonctions et ordres de grandeur pour reconnaître une loi en √t.
- Spé : Réutiliser équation de diffusion, séparation des variables et séries de Fourier selon la progression.
- Approfondissement : Le démarrage idéal instantané crée une incompatibilité au coin y=t=0 ; une couche visqueuse se décrit malgré cette limite du protocole.

**Résultat attendu.** Définir une profondeur de diffusion avec sa convention, convertir ν en SI et estimer le temps d'établissement d'une couche finie.

### blasius

Relier l'épaisseur d'une couche limite laminaire sur une plaque au frottement local. Voir pourquoi une viscosité faible reste décisive près d'une paroi adhérente.

Leçons de référence : 7, 11, 12.

**Techniques à mobiliser**

- Équilibrer transport suivant x et diffusion suivant y.
- Employer la variable ξ=y√(U/(νx)).
- Distinguer coefficient local et coefficient moyen par intégration.

**Prédire → expérimenter → justifier**

1. Prédire l'effet de doubler la distance au bord d'attaque sur l'épaisseur et la contrainte pariétale, à U et ν fixés.
2. Comparer les profils réduits, l'épaisseur à 99 % et le frottement ; repérer l'effondrement des profils en variable ξ.
3. Retrouver δ99≈4,91√(νx/U) et C_f,x≈0,664/√Re_x, puis intégrer pour expliquer le facteur deux du coefficient moyen.

**Entrées et approfondissements**

- Sup : Pratiquer analyse dimensionnelle, racines et contrôle des unités sur les profils.
- Spé : Mobiliser dérivation, équation différentielle non linéaire et changement de variables dans une extension guidée.
- Approfondissement : Blasius suppose plaque plane, gradient de pression extérieur nul et couche laminaire ; transition et décollement demandent un autre modèle.

**Résultat attendu.** Reconnaître la convention de normalisation f'''+ff''/2=0 et distinguer C_f local, moyen et facteur de frottement d'une conduite.

### bernoulli

Interpréter l'échange entre pression, vitesse et altitude dans un écoulement idéal. Employer Venturi, Pitot et vidange tout en gardant les conditions de validité du bilan.

Leçons de référence : 14, 15, 19.

**Techniques à mobiliser**

- Projeter Euler sur une ligne de courant dans le cadre autorisé.
- Combiner conservation du débit et charge mécanique.
- Intégrer une équation de vidange avec une hauteur variable.

**Prédire → expérimenter → justifier**

1. Prédire le changement de pression dans une section rétrécie à débit constant et distinguer pression statique et pression d'arrêt.
2. Comparer les pressions et vitesses, puis la diminution du niveau dans une vidange ; vérifier si la vitesse amont peut être négligée.
3. Écrire les termes p/ρ, v²/2 et gz avec la même unité, identifier les points comparés et justifier tout terme supprimé.

**Entrées et approfondissements**

- Sup : Combiner bilans, énergie, débit et intégration élémentaire.
- Spé : Contrôler permanent, incompressible, idéal et ligne de courant ; intégrer une équation de niveau variable.
- Approfondissement : Bernoulli instationnaire avec ∂ₜφ est une extension selon la filière ; pompes et pertes visqueuses modifient le bilan de charge.

**Résultat attendu.** Énoncer les hypothèses avant de comparer deux pressions et expliquer pourquoi une vitesse maximale affichée n'est pas une pression indépendante.

### sphere

Relier la traînée d'une sphère à sa vitesse dans le régime de Stokes et tester une mesure de viscosité par chute lente. Distinguer les contributions de pression et de frottement.

Leçons de référence : 7, 13, 19.

**Techniques à mobiliser**

- Former Re avec le diamètre 2a et la vitesse relative.
- Projeter poids, poussée et traînée dans un bilan vertical.
- Contrôler un régime quasi stationnaire avant d'utiliser 6πηaU.

**Prédire → expérimenter → justifier**

1. Prédire comment la vitesse terminale d'une bille change lorsqu'on double son rayon ou la viscosité, en supposant encore Re≪1.
2. Comparer vitesse, force et Reynolds ; suivre la part de pression et la part visqueuse de la traînée.
3. Retrouver U_lim=2(ρ_s−ρ)ga²/(9η) et vérifier après le calcul Re, effets de parois et validité du traitement transitoire.

**Entrées et approfondissements**

- Sup : Appliquer un bilan de forces et interpréter un régime terminal.
- Spé : Distinguer inertie du solide, inertie du fluide, approximation de Stokes et contribution de pression.
- Approfondissement : La masse ajoutée, la mémoire hydrodynamique et les parois peuvent corriger une relaxation naïve ; le temps calculé avec la seule traînée stationnaire reste une estimation de modèle.

**Résultat attendu.** Construire une mesure de viscosité cohérente et expliquer les parts 1/3 pression et 2/3 frottement dans la traînée de Stokes.

### vortex

Comparer vortex ponctuel et vortex de Rankine, avec un cœur régulier et une circulation extérieure. Distinguer vorticité locale, circulation et existence d'un potentiel global.

Leçons de référence : 3, 16, 17.

**Techniques à mobiliser**

- Calculer circulation et rotationnel dans une géométrie circulaire.
- Intégrer dp/dr=ρv_θ²/r par morceaux.
- Raccorder pression et vitesse au bord du cœur.

**Prédire → expérimenter → justifier**

1. Prédire où se trouvent la vitesse maximale et la vorticité dans un cœur en rotation solide entouré d'un vortex irrotationnel.
2. Comparer les profils de vitesse et de pression en changeant le rayon du cœur, d'abord à Ω fixé puis à Γ fixé.
3. Retrouver Γ=2πΩa² et démontrer pourquoi curl v=0 hors du cœur n'impose pas une circulation nulle autour de celui-ci.

**Entrées et approfondissements**

- Sup : Mobiliser mouvement circulaire, intégrales et sens d'une circulation.
- Spé : Réutiliser champs de vecteurs, raccordements et bilans radiaux de quantité de mouvement.
- Approfondissement : Potentiel multivalué et rôle de la topologie sont explicités comme extensions ; le vortex ponctuel est singulier sur l'axe.

**Résultat attendu.** Calculer une pression continue dans Rankine et séparer le domaine local irrotationnel d'un domaine où existe un potentiel global monovalué.

### magnus

Expliquer une portance par la dissymétrie de pression autour d'un cylindre avec circulation imposée. Lire son signe et la distinguer d'une condition d'adhérence sur un cylindre réellement tournant.

Leçons de référence : 14, 16, 18.

**Techniques à mobiliser**

- Superposer écoulement uniforme, doublet et circulation.
- Employer Bernoulli dans le domaine idéal.
- Intégrer la pression avec la normale de la surface.

**Prédire → expérimenter → justifier**

1. Pour U selon +x et Γ positif trigonométrique, prédire le côté de plus grande vitesse et le signe de la force verticale.
2. Observer vitesses de surface, pression et résultante lorsque Γ change de signe ou s'annule.
3. Intégrer la pression pour obtenir F_y'=-ρUΓ, puis expliquer pourquoi choisir Γ par la rotation ne suffit pas à imposer l'adhérence partout.

**Entrées et approfondissements**

- Sup : Faire travailler le lien vitesse–pression et les symétries d'une force résultante.
- Spé : Mobiliser fonctions trigonométriques, intégrales de pression et superposition de potentiels.
- Approfondissement : La sélection de la circulation, la couche limite et le décollement sont des questions visqueuses ; le modèle idéal ne prédit pas une traînée réelle complète.

**Résultat attendu.** Annoncer une convention de Γ, retrouver la force par unité de longueur et distinguer la portance idéale d'une simulation complète de cylindre tournant.

### houle

Relier la profondeur, la longueur d'onde et la fréquence d'une onde de surface, puis comparer déplacements des particules, crêtes et paquets. Explorer la transition gravitaire–capillaire.

Leçons de référence : 20, 21, 22.

**Techniques à mobiliser**

- Linéariser les conditions de surface avec ka≪1 et a/h≪1.
- Utiliser ω²=(gk+γk³/ρ)tanh(kh).
- Dériver ω(k) et interpréter les limites kh≪1 et kh≫1.

**Prédire → expérimenter → justifier**

1. Prédire la forme des orbites à la surface et près du fond, puis l'effet d'une profondeur diminuée à longueur d'onde fixée.
2. Comparer orbites, vitesse de phase et vitesse de groupe ; vérifier que f, λ et h satisfont la dispersion plutôt que les choisir indépendamment.
3. Retrouver les limites en eau profonde et peu profonde, puis localiser le minimum de c_φ pour les ondes capillaires-gravitaires.

**Entrées et approfondissements**

- Sup : Distinguer vitesse du signal, célérité des crêtes et vitesse des particules ; contrôler les petites amplitudes.
- Spé : Mobiliser équations d'onde, fonctions hyperboliques, dérivation de dispersion et conditions aux limites.
- Approfondissement : La dérive de Stokes et les asymptotiques d'un impact sont des prolongements ; une orbite fermée de premier ordre ne prouve pas l'absence de tout transport moyen.

**Résultat attendu.** Interpréter une orbite sans la confondre avec une crête et reconnaître les régimes où c_g=c_φ, c_φ/2 ou 3c_φ/2.

### acoustique

Relier pression, vitesse particulaire, densité et intensité d'une onde acoustique, puis suivre sa réflexion et sa transmission à une interface. Contrôler l'énergie même si l'amplitude de pression transmise dépasse l'incidente.

Leçons de référence : 23, 24, 27.

**Techniques à mobiliser**

- Linéariser masse et quantité de mouvement autour du repos.
- Employer Z=ρc et distinguer amplitude crête et efficace.
- Raccorder pression et vitesse normale à une interface.

**Prédire → expérimenter → justifier**

1. Prédire le signe de la réflexion de pression quand l'impédance du second milieu est plus grande, puis celui de la vitesse réfléchie.
2. Comparer amplitudes et intensités de part et d'autre ; varier fréquence et pression en gardant le contrôle de la petite perturbation.
3. Démontrer les deux raccordements et R+T=1 ; expliquer t_p>1 avec la dépendance de l'intensité à Z.

**Entrées et approfondissements**

- Sup : Consolider ondes progressives, intensité, décibels et unités.
- Spé : Réutiliser linéarisation, impédance, conditions d'interface et bilan de puissance.
- Approfondissement : L'atténuation visqueuse et les pertes thermiques demandent une convention complexe et un modèle supplémentaire ; le bruit reste analysable par Fourier.

**Résultat attendu.** Retrouver les coefficients de pression et de vitesse avec leurs signes, calculer une intensité et préciser les hypothèses de cohérence avant d'ajouter des niveaux.

### conduit

Comprendre pourquoi une coupure acoustique concerne un mode transverse particulier. Comparer un mode propagatif, un mode évanescent et le mode plan sans coupure d'un conduit rigide.

Leçons de référence : 23, 24, 25.

**Techniques à mobiliser**

- Séparer les variables avec la condition de Neumann aux parois rigides.
- Calculer k_c²=(mπ/a)²+(nπ/b)² et k_z²=(ω/c)²-k_c².
- Dériver vitesse de groupe et lire une longueur d'évanescence.

**Prédire → expérimenter → justifier**

1. Prédire quels modes passent à une fréquence donnée et vérifier séparément le mode (0,0), puis comparer les deux dimensions du rectangle.
2. Observer les motifs transverses et la propagation axiale juste au-dessus et juste au-dessous d'une coupure ; comparer c_g et c_φ.
3. Retrouver f_c, c_gc_φ=c² et 1/κ ; expliquer pourquoi une branche évanescente n'interdit pas le transport par un autre mode.

**Entrées et approfondissements**

- Sup : Lire longueurs d'onde, dimensions et modes simples avec des fonctions cosinus.
- Spé : Mobiliser équation de Helmholtz, conditions aux limites et dispersion guidée.
- Approfondissement : Les pertes de paroi et la propagation multimodale réelle ne sont pas incluses dans le conduit rigide idéal ; c_φ>c n'est pas la vitesse du transport d'énergie.

**Résultat attendu.** Associer une coupure à ses indices (m,n), distinguer c_g de c_φ et convertir une décroissance exponentielle en longueur caractéristique.

### diffraction

Relier l'ouverture d'une fente au diagramme de diffraction et distinguer une structure physique d'un alias de mesure. Tester la limite des approximations d'angle et la non-unicité d'une image stroboscopique fixe.

Leçons de référence : 22, 25, 26.

**Techniques à mobiliser**

- Intégrer des contributions cohérentes sur une ouverture uniforme.
- Lire [sin q/q]², q=πa sinθ/λ, avec sa limite en zéro.
- Comparer les fréquences qui donnent la même phase aux instants d'échantillonnage.

**Prédire → expérimenter → justifier**

1. Prédire si le premier zéro existe lorsque λ/a dépasse un, et décider avant tout calcul si sinθ≈θ peut être acceptable.
2. Comparer le diagramme angulaire pour plusieurs ouvertures ; examiner ensuite une mesure échantillonnée ou une cadence stroboscopique proche de la vibration.
3. Justifier le diagramme par l'intégrale de phase, puis retrouver une fréquence alias et expliquer pourquoi le filtrage doit précéder l'acquisition.

**Entrées et approfondissements**

- Sup : Travailler interférences, fonctions trigonométriques et contrôle d'une approximation.
- Spé : Réutiliser Fourier, largeur d'un diagramme, échantillonnage et repliement spectral.
- Approfondissement : Le champ lointain, l'ouverture uniforme et la réponse du capteur sont des hypothèses ; une phase stationnaire décrit une asymptotique, pas une amplitude universelle.

**Résultat attendu.** Ne pas transformer λ/a>1 en un angle de premier minimum, proposer une largeur définie et donner plusieurs fréquences compatibles avec un protocole ambigu.

### thermo

Distinguer compressibilité isotherme et isentropique pour prévoir une célérité. Comparer une longueur de diffusion thermique à l'échelle d'onde et à la taille d'un conduit.

Leçons de référence : 4, 23, 27.

**Techniques à mobiliser**

- Dériver χ_T et χ_s à partir d'une loi d'état de gaz parfait.
- Former c²=1/(ρχ_s) dans le modèle acoustique isentropique.
- Comparer δ_th=√(2D_th/ω) à c/ω et à un rayon de paroi.

**Prédire → expérimenter → justifier**

1. Prédire laquelle des compressibilités est la plus grande et laquelle des célérités est la plus rapide pour γ>1.
2. Comparer les valeurs et la longueur de diffusion thermique à c/ω dans le laboratoire. La comparaison avec un rayon de conduit se fait ensuite sur papier avec l'exercice 38 ; ce rayon n'est pas un curseur du laboratoire.
3. Retrouver χ_T=1/p et χ_s=1/(γp), puis expliquer pourquoi les rapports d'échelle ne définissent pas seuls une interpolation entre les deux célérités.

**Entrées et approfondissements**

- Sup : Combiner gaz parfait, unités et analyse dimensionnelle pour lire un ordre de grandeur.
- Spé : Mobiliser dérivées thermodynamiques, petites perturbations et diffusion thermique.
- Approfondissement : Un modèle thermoacoustique avec conditions thermiques aux murs est nécessaire pour calculer précisément dispersion et atténuation dans un petit conduit.

**Résultat attendu.** Annoncer la transformation thermodynamique et distinguer une faible diffusion sur l'échelle d'onde d'un effet de paroi important dans un microconduit.

### mhd

Comparer le freinage de Hartmann dans un liquide conducteur et une onde d'Alfvén dans un régime idéal. Comprendre le rôle du circuit électrique, du champ imposé et de l'énergie magnétique.

Leçons de référence : 5, 6, 28.

**Techniques à mobiliser**

- Former j=σ_e(E+v×B) et calculer j×B avec son signe.
- Résoudre le profil de Hartmann et développer sa limite B→0.
- Éliminer une variable dans les deux équations linéaires d'Alfvén.

**Prédire → expérimenter → justifier**

1. Pour v selon +x, B selon +y et E_z=0, prévoir le sens du courant et de la force magnétique ; annoncer la fermeture électrique utilisée.
2. Comparer le profil de Hartmann au profil sans champ et observer l'effet de Ha ; examiner séparément la vitesse et l'énergie de l'onde d'Alfvén.
3. Retrouver la limite de Poiseuille plan et vérifier Rm≪1 pour Hartmann ; établir c_A et l'équipartition pour l'onde idéale sans transporter les hypothèses d'un régime à l'autre.

**Entrées et approfondissements**

- Sup : Entrer par produits vectoriels, unités et bilan de forces ; le cadre MHD est une extension guidée.
- Spé : Réutiliser conduction, force de Lorentz, équation différentielle et ondes couplées.
- Approfondissement : Champ imposé à faible Rm et onde idéale d'induction sont deux régimes distincts ; changer la fermeture du circuit change le courant et le freinage.

**Résultat attendu.** Lire Ha et Rm avec leurs longueurs déclarées, justifier le signe du freinage et expliquer le partage d'énergie d'une onde d'Alfvén.

### navier

Relier une solution exacte bidimensionnelle de Taylor–Green à ses champs de pression, vorticité et énergie. Situer ce contrôle dans les équations de mouvement et dans la question mathématique tridimensionnelle.

Leçons de référence : 5, 6, 7.

**Techniques à mobiliser**

- Substituer une solution dans continuité et quantité de mouvement.
- Intégrer le bilan d'énergie sur un domaine périodique.
- Comparer les temps L/U et L²/ν plutôt qu'un seuil universel.

**Prédire → expérimenter → justifier**

1. Prédire la décroissance de l'amplitude et de l'énergie lorsque la viscosité augmente, puis le rapport entre leurs exposants.
2. Comparer vitesse, pression, vorticité et énergie de Taylor–Green à plusieurs instants ; vérifier l'identité entre perte d'énergie et dissipation.
3. Retrouver A=Ue^{−2νk²t} et expliquer ce qu'une solution exacte 2D ou une borne L² ne démontre pas pour toutes les données 3D ; distinguer l'énoncé historique de l'annonce Clay datée.

**Entrées et approfondissements**

- Sup : Pratiquer unités, exponentielle et bilans dans une solution explicitement donnée.
- Spé : Mobiliser équations locales, intégrations par parties et vorticité dans une extension guidée selon la filière.
- Approfondissement : Le programme PSI cité exclut Euler et Navier–Stokes ; l'atelier accompagne leur étude et distingue une preuve globale d'un calcul particulier. Le repère Clay est daté du 6 octobre 2026.

**Résultat attendu.** Contrôler un bilan analytique, annoncer dimension et frontières, puis expliquer sans extrapolation le lien et la différence avec le problème 3D de Fefferman.

### hydrostatique

Construire les forces de pression, la poussée et les sauts capillaires à partir de la géométrie. Distinguer une colonne liquide incompressible d'une atmosphère soumise à une hypothèse thermodynamique.

Leçons de référence : 15, 19, 20.

**Techniques à mobiliser**

- Intégrer ∇p=ρg en fixant une pression de référence.
- Fermer une surface pour appliquer le théorème de Gauss.
- Équilibrer énergie de surface ou force capillaire et poids.

**Prédire → expérimenter → justifier**

1. Prédire comment la pression change avec l'altitude ; préciser si la densité ou la température est supposée constante.
2. Comparer les profils de pression du laboratoire. Les volumes immergés et les effets de rayon ou d'angle de contact sont des prolongements à lire dans la galerie et à calculer sur papier avec les exercices 25 et 27, sans curseurs correspondants dans ce laboratoire.
3. Retrouver la loi hydrostatique affichée, puis justifier sur papier Archimède avec une surface fermée et une pression atmosphérique commune ; compter les interfaces dans le saut de Laplace.

**Entrées et approfondissements**

- Sup : Appliquer statique, pression, poussée, gaz parfait et équilibre de forces.
- Spé : Mobiliser intégrales sur une surface, Gauss et stratifications isotherme ou isentropique.
- Approfondissement : Le volume immergé ne suffit pas à décider une stabilité de roulis ; température réelle, mouillage et courbures imposent des informations supplémentaires.

**Résultat attendu.** Calculer une force avec sa référence de pression, compter les interfaces et distinguer équilibre de translation et stabilité de rotation.

## Les quarante exercices corrigés

### 1 · Une vitesse permanente peut accélérer

*SUP → SPÉ* — laboratoire `cinematique`.

**Énoncé.** Dans v=(αx,−αy), prendre α=0,5 s⁻¹ et R(0)=(0,20 m,0,10 m). Déterminer la trajectoire, la ligne de courant initiale, la divergence et l'accélération. Calculer R(2 s). Un fluide incompressible a-t-il nécessairement une accélération nulle ?

**Corrigé.** Intégrer x'=αx et y'=−αy donne x=0,20e^{αt}, y=0,10e^{−αt}. Le produit xy=0,020 m² définit la ligne de courant, qui coïncide avec la trajectoire parce que le champ est permanent. div v=α−α=0 et curl v=0. L'accélération vaut (v·∇)v=(α²x,α²y). À 2 s, R≈(0,544 m,0,0368 m) et a≈(0,136 m·s⁻²,0,00920 m·s⁻²).

**Interprétation.** L'incompressibilité porte sur les volumes matériels ; elle ne supprime ni l'advection ni les changements de vitesse le long d'une trajectoire. Le carré de α, en s⁻², doit multiplier une longueur.

### 2 · Trajectoire parabolique, courant rectiligne

*SPÉ · EXTENSION CINÉMATIQUE* — laboratoire `cinematique`.

**Énoncé.** Considérer v=(U,At), avec U>0 et A en m·s⁻². Une particule part de l'origine. Trouver sa trajectoire et les lignes de courant à t₀. Déterminer divergence, vorticité et accélération ; comparer la particule aux flèches instantanées.

**Corrigé.** R(t)=(Ut,At²/2), donc y=Ax²/(2U²), une parabole. À t=t₀, dy/dx=At₀/U est constant : les lignes de courant sont des droites y=(At₀/U)x+C. div v=0, curl v=0 ; a=(0,A) car le champ ne dépend pas de la position. Une ligne de courant instantanée n'est pas la trajectoire. Les unités de A distinguent ici accélération imposée et gradient spatial de vitesse.

### 3 · Débit, section et densité variable

*SUP · BILAN* — laboratoire `cinematique`.

**Énoncé.** Un liquide traverse des sections 1,0 cm² et 0,50 cm² avec Q=2,0 L·min⁻¹. Calculer les vitesses uniformes. Reprendre pour un gaz dont la densité passe de 1,2 à 0,8 kg·m⁻³ avec le même débit volumique entrant. Quel débit est conservé ?

**Corrigé.** Q₁=3,333×10⁻⁵ m³·s⁻¹. Pour le liquide : U₁=0,333 et U₂=0,667 m·s⁻¹. Pour le gaz : ṁ=ρ₁Q₁=4,0×10⁻⁵ kg·s⁻¹ ; Q₂=ṁ/ρ₂=5,0×10⁻⁵ m³·s⁻¹, donc U₂=1,0 m·s⁻¹. Le débit massique est conservé dans ce régime permanent sans fuite. Un Q identique aux deux sections aurait imposé une masse créée ou détruite.

### 4 · Cisaillement et rotation solide

*SPÉ · TENSEURS GUIDÉS* — laboratoire `newtonien`.

**Énoncé.** Comparer v=(γ̇y,0,0) et v=(−Ωy,Ωx,0). Calculer L,D,W,div v et curl v. Pour η=1,0 mPa·s et γ̇=1000 s⁻¹, déterminer la contrainte tangentielle et la dissipation. Pourquoi la rotation solide ne donne-t-elle pas ce frottement ?

**Corrigé.** Dans le cisaillement, Lₓᵧ=γ̇, Dₓᵧ=Dᵧₓ=γ̇/2, Wₓᵧ=γ̇/2, Wᵧₓ=−γ̇/2. div v=0 et curl v=−γ̇e_z. τₓᵧ=ηγ̇=1,0 Pa, Φ=ηγ̇²=1000 W·m⁻³. Pour la rotation, L est antisymétrique, D=0, W=L, div v=0 et curl v=2Ωe_z. La loi τ=2ηD donne τ=0 : la viscosité réagit à la déformation relative, pas à la seule rotation du repère matériel.

### 5 · Dissiper malgré un Laplacien nul

*SPÉ · BILAN LOCAL* — laboratoire `newtonien`.

**Énoncé.** Dans un domaine borné, v=(ax,−ay,0) est imposé par les frontières. Calculer Δv, D et Φ pour η constant. Peut-on déduire de Δv=0 l'absence de dissipation ? Que devient l'énergie en régime permanent ?

**Corrigé.** Δv=0, D=diag(a,−a,0), donc D:D=2a² et Φ=4ηa²>0 si a≠0. La force visqueuse volumique ηΔv est nulle, mais les contraintes aux frontières effectuent du travail. La formule ∫v·Δv=−∫|∇v|² ne vaut sans terme de bord que sous des conditions adaptées, ici non satisfaites. En régime permanent, le travail des frontières alimente la chaleur et les flux du domaine. Ce contre-exemple oblige à déclarer les frontières avant d'appliquer un bilan global.

### 6 · Vérifier Taylor–Green sans simuler un problème général

*SPÉ · EXTENSION NS* — laboratoire `navier`.

**Énoncé.** Pour v=(A sin(kx)cos(ky),−A cos(kx)sin(ky)), A=Ue^{−2νk²t}, vérifier div v=0 et trouver p−p₀. Sur une cellule périodique, calculer l'énergie par unité de volume et sa dérivée. Le résultat prouve-t-il l'existence régulière de toute solution 3D ?

**Corrigé.** La divergence s'annule terme à terme. Δv=−2k²v et ∂ₜv=−2νk²v ; les termes visqueux et temporels se compensent. La convection vaut (A²k sin(2kx)/2,A²k sin(2ky)/2), donc p−p₀=ρA²[cos(2kx)+cos(2ky)]/4. Les moyennes de sin² et cos² valent 1/2 : E/V=ρA²/4 et −d(E/V)/dt=ρνk²A². C'est un certificat pour une famille particulière 2D. Il ne quantifie pas toutes les données initiales 3D et ne remplace pas l'évaluation de la preuve annoncée par le Clay en septembre 2026.

### 7 · Même eau, trois Reynolds

*SUP → SPÉ · ÉCHELLES* — laboratoire `blasius`.

**Énoncé.** Avec ν=1,0 mm²·s⁻¹ et U=0,10 m·s⁻¹, calculer Re pour un tube de diamètre 1 mm, puis 10 mm, et Re_x à x=0,10 m sur une plaque. Déterminer les temps d'advection et de diffusion pour la dernière longueur. Un seuil 2000 décide-t-il tous ces régimes ?

**Corrigé.** ν=10⁻⁶ m²·s⁻¹. Les Reynolds sont 100,1000 et 10 000. Pour L=0,10 m : t_adv=1 s et t_ν=10 000 s ; leur rapport vaut bien Re. Sur la plaque, δ₉₉≈4,91√(νx/U)=4,91 mm sous les hypothèses de Blasius. Le seuil de transition d'une conduite ne s'applique pas automatiquement à une plaque. Les nombres doivent conserver leur longueur de référence ; écrire seulement « Re=10 000 » perd une partie de l'information physique.

### 8 · Couette : force et puissance

*SUP → SPÉ* — laboratoire `couette`.

**Énoncé.** Deux plaques de 0,010 m², séparées de 1,0 mm, contiennent un fluide de η=0,10 Pa·s. L'une se déplace à 0,20 m·s⁻¹, l'autre est fixe. Calculer le profil, la force résistante, la puissance nécessaire et la dissipation intégrée. Négliger les bords.

**Corrigé.** Avec y=0 sur la plaque mobile, u=0,20(1−y/0,001) m·s⁻¹. |τ|=ηU/h=20 Pa, donc |F|=0,20 N et P=FU=0,040 W. Φ=η(U/h)²=4000 W·m⁻³ ; le volume Ah=10⁻⁵ m³ donne ΦAh=0,040 W. La puissance motrice et la dissipation coïncident. La force du fluide sur la plaque s'oppose au mouvement ; la contrainte sur une face doit conserver le sens de sa normale.

### 9 · Couette–Poiseuille et inversion du courant

*SPÉ · SUPERPOSITION* — laboratoire `couette`.

**Énoncé.** Entre y=0 mobile à U>0 et y=h fixe, ajouter G=−dp/dx constant. Trouver u et le débit par largeur. Pour quelles valeurs de G un courant opposé apparaît-il près de la paroi fixe ? Un débit global positif l'interdit-il ?

**Corrigé.** La solution est u=U(1−y/h)+G y(h−y)/(2η)=(h−y)[U/h+Gy/(2η)]. Le débit par largeur q=Uh/2+Gh³/(12η). Si G<−2ηU/h², le crochet devient négatif près de y=h : une zone de reflux apparaît. Pourtant q reste positif si G>−6ηU/h². Il existe donc un intervalle de paramètres donnant un débit net positif et un courant local inverse. La linéarité utilisée vient de ce champ parallèle dont la convection est nulle, pas d'une superposition générale des solutions NS.

### 10 · Poiseuille : calculer puis valider

*SUP → SPÉ · TP* — laboratoire `poiseuille`.

**Énoncé.** Pour R=0,50 mm, L=0,10 m, η=1,0 mPa·s, ρ=1000 kg·m⁻³ et Δp=p_entrée−p_sortie=100 Pa, déterminer le profil, Q, U_moy, Re_D et la puissance hydraulique. Quel signe a le résultat si l'on échange les deux pressions ?

**Corrigé.** u=Δp(R²−r²)/(4ηL), u_max=0,0625 m·s⁻¹ et U_moy=0,03125 m·s⁻¹. Q=2,454×10⁻⁸ m³·s⁻¹=1,47 mL·min⁻¹. Re_D=ρU_moy(2R)/η=31,25 et ΔpQ=2,454 µW. Le faible Re est cohérent avec le régime laminaire développé supposé. Échanger les pressions inverse u et Q ; la puissance dissipée ΔpQ reste positive. Les conditions d'entrée et la longueur nécessaire à l'établissement du profil restent à vérifier dans une expérience réelle.

### 11 · Mesurer un rayon avec une loi en quatrième puissance

*SPÉ · IDENTIFICATION* — laboratoire `poiseuille`.

**Énoncé.** Sous Δp,L,η connus, exprimer le rayon à partir du débit. Une hausse de 10 % du rayon multiplie-t-elle le débit par 1,4 exactement ? Établir la sensibilité différentielle de R aux données et discuter l'intérêt d'un modèle de tube cylindrique.

**Corrigé.** R=[8ηLQ/(πΔp)]^{1/4}. Une hausse de 10 % donne Q₂/Q₁=1,1⁴=1,4641 ; 1,4 n'est que l'approximation linéaire au premier ordre. La différentielle logarithmique donne dR/R=(dη/η+dL/L+dQ/Q−dΔp/Δp)/4. Cette relation décrit des petites perturbations signées ; une estimation d'incertitude doit préciser leur mode de combinaison. Un tube non cylindrique, une fuite ou une viscosité variable produit un biais de modèle que cette formule de sensibilité ne supprime pas.

### 12 · Un petit réseau hydraulique

*SPÉ · ASSOCIATIONS* — laboratoire `poiseuille`.

**Énoncé.** Une conduite de résistance ℛ alimente deux conduites de même longueur en parallèle. La première a résistance ℛ ; le rayon de la seconde est divisé par deux à η identique. Calculer la résistance totale et le partage du débit entre branches. Toutes les conduites restent développées et laminaires.

**Corrigé.** La seconde branche a résistance 16ℛ. Le parallèle vaut [1/ℛ+1/(16ℛ)]⁻¹=16ℛ/17 ; avec la conduite amont en série, ℛ_total=33ℛ/17. Les branches partagent la même chute de pression ; leurs débits sont dans le rapport 16:1. La branche large reçoit 16/17 du débit total et l'étroite 1/17. Une section divisée par quatre n'entraîne pas simplement un débit divisé par quatre : la résistance suit R⁻⁴.

### 13 · Retrouver la similitude de Stokes

*SPÉ · DIFFUSION* — laboratoire `diffusion`.

**Énoncé.** Pour une paroi brusquement mise à U dans y≥0, chercher u/U=F(y/(2√νt)). Établir l'équation de F et ses conditions. Avec ν=1 mm²·s⁻¹, calculer δ à 1 s et 4 s, et u/U à y=δ. δ est-elle la limite d'un fluide exactement au repos ?

**Corrigé.** La substitution donne F''+2ξF'=0, F(0)=1 et F(∞)=0. Intégrer F'=C exp(−ξ²) produit F=erfc ξ. δ=2√νt vaut 2 mm puis 4 mm ; à y=δ, u/U≈0,1573. La fonction erfc est positive pour toute distance finie : δ est une échelle, pas un front. La contrainte η∂_yu à la paroi vaut −ηU/√(πνt), signe conforme au profil décroissant.

### 14 · Deux parois : établir le transitoire de Couette

*SPÉ · SÉRIES DE FOURIER* — laboratoire `diffusion`.

**Énoncé.** Le fluide 0<y<h est initialement au repos ; u(0,t)=U et u(h,t)=0 pour t>0. Soustraire le profil permanent puis construire la série en sinus. Pour h=1 mm et ν=1 mm²·s⁻¹, estimer le temps où le premier mode d'écart est inférieur à 1 % de U.

**Corrigé.** w=u/U−(1−y/h) a des frontières homogènes et w(y,0)=−(1−y/h). Ses coefficients sinus valent −2/(nπ), d'où la série de la leçon 11. Le premier temps de relaxation est τ₁=h²/(π²ν)=0,1013 s. L'amplitude maximale du premier écart vaut (2/π)e^{−t/τ₁}; elle devient <0,01 pour t>τ₁ln[2/(0,01π)]≈0,421 s. À ce temps les modes supérieurs sont fortement amortis ; l'estimation n'est pas une description du coin discontinu y=0,t=0.

### 15 · Frottement local et moyen de Blasius

*SPÉ · COUCHE LIMITE GUIDÉE* — laboratoire `blasius`.

**Énoncé.** Avec ξ=y√(U/(νx)), établir C_f,x à partir de f''(0)=0,332057. Intégrer le frottement sur une plaque de longueur L pour obtenir C_f,moy. À U=10 m·s⁻¹, x=0,10 m, ν=1,5×10⁻⁵ m²·s⁻¹ et ρ=1,2 kg·m⁻³, calculer τ_w et δ₉₉.

**Corrigé.** ∂_yu au mur vaut U f''(0)√(U/(νx)). Avec η=ρν, C_f,x=2f''(0)/√Re_x=0,664114/√Re_x. Intégrer x^{-1/2} sur [0,L] double le coefficient : C_f,moy=1,328228/√Re_L. Numériquement Re_x≈66 667, C_f,x≈0,002572, τ_w≈0,154 Pa et δ₉₉≈1,90 mm. Le modèle singulier au bord d'attaque a une traînée intégrable ; sa validité suppose couche mince, écoulement laminaire et gradient de pression nul.

### 16 · D'où viennent 6π et 24/Re ?

*SPÉ · STOKES GUIDÉ* — laboratoire `sphere`.

**Énoncé.** Pour la solution permanente de la sphère donnée dans la leçon 13, intégrer la traction selon l'axe du courant. Séparer pression et cisaillement. En déduire C_D si la surface de référence est πR². Quelles hypothèses interdisent d'utiliser ce résultat pour toute vitesse ?

**Corrigé.** À r=R, le terme de pression variable projette 3ηU cos²θ/(2R), dont l'intégrale vaut 2πηRU ; le cisaillement projette 3ηU sin²θ/(2R), donnant 4πηRU. La pression uniforme s'intègre en zéro. Ainsi F=6πηRU. De F=(1/2)C_DρπR²U², on déduit C_D=12η/(ρRU)=24/Re_D. L'inertie est négligée, la sphère est rigide avec adhérence et les parois sont lointaines. Un régime rapide, un confinement ou une bulle mobile exige une autre loi.

### 17 · Bille : vitesse limite et viscosimétrie

*SPÉ · MODÈLE DE CHUTE* — laboratoire `sphere`.

**Énoncé.** Une bille de R=0,10 mm et ρ_s=2500 kg·m⁻³ chute dans ρ_f=1000 kg·m⁻³ à la vitesse limite 0,327 mm·s⁻¹. Inférer η et vérifier Re_D. Écrire ensuite la solution du modèle linéaire instantané, et nommer les termes qu'il néglige au démarrage.

**Corrigé.** η=2(ρ_s−ρ_f)gR²/(9w_lim)≈0,100 Pa·s et Re_D≈6,54×10⁻⁴. Le bilan m w'=(ρ_s−ρ_f)Vg−6πηRw donne w=w_lim(1−e^{−t/τ}), τ=2ρ_sR²/(9η)≈55,6 µs. Ce temps appartient au modèle simplifié : la masse ajoutée, l'histoire de diffusion visqueuse et le confinement ne sont pas inclus. La mesure permanente doit s'effectuer loin des parois et après établissement de la vitesse ; inférer une viscosité depuis les premières microsecondes avec ce seul modèle serait insuffisant.

### 18 · Venturi et pression d'arrêt

*SUP → SPÉ* — laboratoire `bernoulli`.

**Énoncé.** Un Venturi horizontal a S₂=S₁/2, U₁=1,0 m·s⁻¹ et ρ=1000 kg·m⁻³. Trouver U₂ et p₁−p₂. Quel écart de pression mesurerait un Pitot à chaque section ? Pourquoi peut-on avoir p₂ plus faible et une pression d'arrêt identique ?

**Corrigé.** Continuité : U₂=2U₁=2 m·s⁻¹. Bernoulli donne p₁−p₂=1500 Pa. Le Pitot mesure p_arrêt−p₁=500 Pa et p_arrêt−p₂=2000 Pa. Les deux pressions d'arrêt coïncident si les points correspondent au même bilan idéal : p₁+ρU₁²/2=p₂+ρU₂²/2. La baisse de pression statique convertit une part de l'énergie de pression en énergie cinétique ; elle ne représente pas ici une perte dissipative.

### 19 · Vidange : le temps n'est pas proportionnel à h

*SUP → SPÉ · ÉQUATION DIFFÉRENTIELLE* — laboratoire `bernoulli`.

**Énoncé.** Prendre S=0,020 m², s=2,0×10⁻⁴ m² et h₀=0,50 m. Dans le modèle quasi stationnaire idéal, déterminer h(t), le temps de vidange et celui où la hauteur est divisée par deux. Préciser les hypothèses et le domaine de la formule.

**Corrigé.** S h'=−s√(2gh), donc h=(√h₀−(s/S)√(g/2)t)² tant que la parenthèse est positive. Le temps total T=(S/s)√(2h₀/g)≈31,9 s. h=h₀/2 survient à t=T(1−1/√2)≈9,35 s. Prolonger le carré au-delà de T prédirait un remplissage fictif : on arrête le modèle à h=0. s/S=0,01 soutient la petite vitesse de surface ; viscosité, contraction du jet et variation rapide du champ sont négligées.

### 20 · Tube en U à sections différentes

*SPÉ · BILAN D'INERTIE* — laboratoire `bernoulli`.

**Énoncé.** Dans un tube en U, S(l) est la section le long du liquide. Les surfaces ont les sections S₁ et S₂. Définir q(t) comme le petit volume transféré d'une branche vers l'autre. Établir l'énergie cinétique et la pulsation des petites oscillations. Retrouver le cas uniforme de longueur L.

**Corrigé.** Le débit est q' et la vitesse locale q'/S(l). L'énergie cinétique vaut (ρ/2)q'² I, I=∫dl/S(l), en m⁻¹. Les déplacements de surfaces sont q/S₁ et −q/S₂ ; l'énergie potentielle supplémentaire est (ρg/2)q²(1/S₁+1/S₂). L'équation est Iq''+g(1/S₁+1/S₂)q=0, donc ω²=g(1/S₁+1/S₂)/I. Pour une section uniforme S, I=L/S et ω²=2g/L. Ce résultat conserve la masse et la variation locale de vitesse ; remplacer I par L sans unité de section échoue dimensionnellement.

### 21 · Irrotationnel ne veut pas dire potentiel global

*SPÉ · TOPOLOGIE GUIDÉE* — laboratoire `vortex`.

**Énoncé.** Sur l'anneau a<r<b, v_r=0 et v_θ=Γ/(2πr), Γ≠0. Calculer divergence, vorticité et circulation. Trouver un potentiel local et montrer qu'il n'est pas globalement monovalué. Pourquoi Stokes ne donne-t-il pas une circulation nulle ?

**Corrigé.** La divergence est nulle. La composante de vorticité vaut (1/r)d(rv_θ)/dr=0 sur l'anneau, tandis que ∮v·dl=2πr v_θ=Γ. Localement φ=Γθ/(2π) vérifie v=∇φ ; après un tour, φ augmente de Γ. Un gradient global monovalué aurait une intégrale nulle sur tout contour fermé, contradiction. Le disque bordé par le cercle traverse le trou où le champ n'est pas défini ; les hypothèses de Stokes sur ce disque ne sont donc pas réunies.

### 22 · Rankine : raccorder vitesse et pression

*SPÉ · TP* — laboratoire `vortex`.

**Énoncé.** Pour ρ=1,2 kg·m⁻³, Ω=4 s⁻¹ et a=5 m, construire le champ Rankine. Calculer Γ extérieure, v_max, p(a)−p_∞ et p(0)−p_∞. Vérifier la continuité de p et expliquer pourquoi un Bernoulli global ne convient pas au cœur.

**Corrigé.** Le cœur donne v_θ=Ωr, l'extérieur Ωa²/r. Γ=2πΩa²=200π≈628 m²·s⁻¹ et v_max=Ωa=20 m·s⁻¹. Euler radial impose p'=ρv_θ²/r. À a, p−p_∞=−ρΩ²a²/2=−240 Pa ; au centre, −ρΩ²a²=−480 Pa. Les deux expressions se raccordent à a. Le cœur a une vorticité 2Ω et des constantes de Bernoulli pouvant varier d'une ligne circulaire à l'autre ; la condition irrotationnelle globale manque.

### 23 · Réduire le cœur à circulation fixée

*SPÉ · PARAMÈTRE ET CONTRÔLE* — laboratoire `vortex`.

**Énoncé.** Dans Rankine, fixer Γ et ρ, puis diviser le rayon du cœur par deux. Comment varient Ω, la vitesse maximale et la baisse de pression centrale ? Cette limite reproduit-elle un champ régulier sur l'axe lorsque a tend vers zéro ?

**Corrigé.** Γ=2πΩa² donne Ω=Γ/(2πa²). Diviser a par deux multiplie Ω par quatre, v_max=Γ/(2πa) par deux et p_∞−p(0)=ρΓ²/(4π²a²) par quatre. La limite a→0 devient le vortex ponctuel hors de l'axe, mais la vitesse et la baisse de pression deviennent singulières au centre. Ce n'est pas une limite régulière sur tout le domaine. Une pression absolue trop faible et la compressibilité peuvent rendre le modèle physique inapplicable avant cette limite mathématique.

### 24 · Portance et signe de la circulation

*SPÉ · MAGNUS GUIDÉ* — laboratoire `magnus`.

**Énoncé.** Pour un cylindre, prendre U=10 m·s⁻¹ selon +x, Γ=0,80 m²·s⁻¹ positif trigonométrique et ρ=1,2 kg·m⁻³. Retrouver F_y' par l'intégrale de pression, puis calculer sa valeur. La relation Γ=2πa²Ω assure-t-elle l'adhérence sur tout le cylindre ?

**Corrigé.** À r=a, v_θ=−2U sinθ+g₀ avec g₀=Γ/(2πa). Dans p=p_∞+ρ(U²−v_θ²)/2, le terme utile à F_y' est +2ρUg₀ sinθ. Ainsi −a∫p sinθdθ=−2πaρUg₀=−ρUΓ=−9,6 N·m⁻¹ ; F_x'=0 dans le modèle idéal. Le terme −2U sinθ reste présent même si g₀=aΩ, donc la vitesse tangentielle n'est pas partout aΩ. Cette fermeture fixe une circulation moyenne, pas une condition d'adhérence visqueuse complète.

### 25 · Une pression uniforme ne change pas Archimède

*SUP · STATIQUE* — laboratoire `hydrostatique`.

**Énoncé.** Un solide homogène de volume 2,0 L et masse 1,2 kg flotte dans de l'eau à 1000 kg·m⁻³. Trouver son volume immergé. Refaire la preuve de la poussée, puis expliquer l'effet d'une pression uniforme ajoutée sur tout le fluide. Peut-on décider la stabilité du roulis à partir du seul volume ?

**Corrigé.** L'équilibre vertical impose ρV_imm=m, donc V_imm=1,2 L, 60 % du volume. En pression relative à l'atmosphère commune, fermer la surface mouillée par la surface horizontale de flottaison, où la pression relative est nulle. Gauss donne alors −∫_S p_rel n dS=−∫_{V_imm}∇p_rel dV=−ρV_imm g_vec. Ajouter la même constante à la pression extérieure de toutes les faces, dans l'air et dans l'eau, ajoute −p_c∫_{S_fermée}n dS=0. Une constante ajoutée seulement sur la surface mouillée n'a pas forcément une résultante nulle. Le roulis dépend des moments, de la géométrie, du centre de masse et du déplacement du centre de poussée ; le pourcentage immergé ne suffit pas à en décider.

### 26 · Isotherme ou colonne isentropique ?

*SPÉ · HYDROSTATIQUE ET THERMO* — laboratoire `hydrostatique`.

**Énoncé.** Dans un gaz parfait de M=0,029 kg·mol⁻¹, γ=1,4, T₀=290 K et g=9,81 m·s⁻², établir p(z) pour une colonne isotherme puis pour une colonne de même entropie massique à toutes les altitudes. Montrer le domaine de validité du second modèle. Prendre R=8,314 J·mol⁻¹·K⁻¹.

**Corrigé.** Isotherme : H=RT₀/(Mg)≈8,47 km, p=p₀e^{−z/H}. Isentropique : pρ^{-γ}=constante et p=ρRT/M. La relation hydrostatique donne T=T₀−gz/c_p, c_p=γR/[M(γ−1)]≈1003 J·kg⁻¹·K⁻¹, puis p=p₀(T/T₀)^{γ/(γ−1)}. Le gradient vaut environ −9,78 K·km⁻¹. La formule exige T>0, donc z<c_pT₀/g≈29,7 km ; son extinction n'est pas une frontière universelle de l'atmosphère réelle. L'isothermie et l'entropie uniforme sont deux hypothèses différentes de stratification.

### 27 · Une ou deux interfaces capillaires

*SUP → SPÉ* — laboratoire `hydrostatique`.

**Énoncé.** Avec γ=0,072 N·m⁻¹, calculer le saut de pression pour une goutte de rayon 1 mm, puis pour une bulle de savon mince du même rayon. Dans un tube de R=0,50 mm, θ=0 et ρ=1000 kg·m⁻³, déterminer la montée capillaire et son signe pour θ=120°. Justifier les facteurs.

**Corrigé.** La variation γdS=Δp dV d'une sphère donne Δp=2γ/a=144 Pa à une interface. Deux interfaces d'une pellicule donnent environ 288 Pa. L'équilibre vertical 2πRγ cosθ=ρgπR²h donne h≈2,94 cm pour θ=0 ; pour θ=120°, cosθ=−1/2 et h≈−1,47 cm. Il s'agit d'une dépression. La tension est une énergie par aire ; le nombre d'interfaces et le sens des courbures sont des données physiques, pas des facteurs ajustés après le calcul.

### 28 · La fréquence de houle n'est pas une donnée libre

*SPÉ · TP DE CUVE* — laboratoire `houle`.

**Énoncé.** Pour une cuve h=1 m, une longueur λ=1 m et une amplitude a=1 cm, négliger la capillarité. Déduire la fréquence, la vitesse de phase et vérifier la linéarisation. Refaire le raisonnement lorsque h devient très petit à λ fixé. Peut-on choisir simultanément n'importe quel f ?

**Corrigé.** k=2π m⁻¹, ω=√[gk tanh(kh)]≈7,85 s⁻¹, donc f≈1,25 Hz et c_φ=ω/k≈1,25 m·s⁻¹. ka≈0,0628 et a/h=0,01 sont petits. Si kh≪1, tanh(kh)≈kh : ω≈k√(gh), c_φ≈√(gh) et f≈√(gh)/λ. Il faut aussi conserver a/h≪1 lorsque la profondeur diminue. La dispersion contraint f,λ,h ; une fréquence imposée expérimentalement sélectionne une longueur d'onde compatible, au lieu d'autoriser un choix indépendant.

### 29 · Une particule d'eau ne suit pas une crête

*SPÉ · ORBITES LINÉAIRES* — laboratoire `houle`.

**Énoncé.** En eau profonde, une houle de λ=1 m et a=1 cm passe au-dessus d'une particule à z₀=−0,50 m. Trouver le rayon de son orbite linéaire et l'amplitude de sa vitesse. Comparer cette vitesse à c_φ. Que peut-on conclure sur le transport moyen de matière ?

**Corrigé.** En eau profonde, les deux amplitudes de déplacement sont a e^{kz₀}. Avec k=2π m⁻¹, le rayon vaut a e^{-π}≈0,432 mm. L'amplitude de vitesse vaut ωa e^{-π}≈3,39 mm·s⁻¹, très inférieure à c_φ≈1,25 m·s⁻¹. La trajectoire de premier ordre est fermée et n'a pas de déplacement moyen. Cela ne prouve pas l'absence de toute dérive réelle : la dérive de Stokes est d'ordre supérieur et les courants moyens peuvent modifier l'expérience.

### 30 · Le minimum des ondes capillaires-gravitaires

*SPÉ · OPTIMISATION ET DISPERSION* — laboratoire `houle`.

**Énoncé.** En eau profonde, c_φ²=g/k+γk/ρ. Trouver le minimum pour γ=0,072 N·m⁻¹ et ρ=1000 kg·m⁻³. Montrer que c_g=c_φ à ce point. Comparer les limites dominées par la gravité et par la capillarité.

**Corrigé.** Dériver donne −g/k²+γ/ρ=0, donc k*=√(ρg/γ)≈369 m⁻¹, λ*≈1,70 cm et c_min=(4gγ/ρ)^{1/4}≈0,231 m·s⁻¹. Puisque ω=kc_φ, c_g=c_φ+k dc_φ/dk ; au minimum le second terme est nul. Gravité dominante : ω∝k^{1/2}, c_g=c_φ/2. Capillarité dominante : ω∝k^{3/2}, c_g=3c_φ/2. Le paquet et les crêtes ne se déplacent donc pas toujours dans le même rapport.

### 31 · Impact : phase stationnaire et crêtes apparentes

*SPÉ · APPROFONDISSEMENT ASYMPTOTIQUE* — laboratoire `houle`.

**Énoncé.** Pour une source impulsive en eau profonde, étudier la phase Φ(k)=kr−√(gk)t à r,t>0. Trouver le k stationnaire et la phase correspondante. Dans cette phase dominante, poser Φ*=−2πp avec p entier positif et déterminer r_p(t). Pourquoi une loi d'amplitude 1/r ne suit-elle pas de ce calcul ?

**Corrigé.** ∂_kΦ=r−(t/2)√(g/k)=0 donne k*=gt²/(4r²), puis Φ*=−gt²/(4r). Le choix de phase dominante −2πp donne r_p=gt²/(8πp), r_p'=gt/(4πp) et r_p''=g/(4πp). Pour p=2 à t=1 s, r≈0,195 m. Ces crêtes sont une description asymptotique avec une convention de phase ; un décalage de source ou de phase stationnaire change leur repérage. L'amplitude dépend du poids spectral, des facteurs géométriques et de Φ'' : elle n'est pas déterminée par la seule position de la phase stationnaire. Ce prolongement se travaille sur papier à partir de la dispersion illustrée.

### 32 · Une pression acoustique de 1 Pa

*SUP → SPÉ · GRANDEURS ET UNITÉS* — laboratoire `acoustique`.

**Énoncé.** Une onde plane progressive de f=1 kHz a une amplitude de pression crête p̂=1 Pa dans ρ₀=1,2 kg·m⁻³ et c=340 m·s⁻¹. Calculer Z, l'amplitude de vitesse et de déplacement, l'amplitude de densité, I et L_I. Prendre p₀=10⁵ Pa et vérifier l'approximation acoustique.

**Corrigé.** Z=408 Pa·s·m⁻¹, v̂=p̂/Z≈2,45 mm·s⁻¹, ŝ=v̂/(2πf)≈0,390 µm et ρ̂=p̂/c²≈8,65×10⁻⁶ kg·m⁻³. I=p̂²/(2Z)≈1,225×10⁻³ W·m⁻² ; L_I≈90,9 dB pour I₀=10⁻¹² W·m⁻². Les rapports p̂/p₀=10⁻⁵, ρ̂/ρ₀≈7,21×10⁻⁶ et v̂/c≈7,21×10⁻⁶ sont petits. La célérité ne doit pas être confondue avec la vitesse de quelques mm·s⁻¹ des particules.

### 33 · Réfléchir sans créer d'énergie

*SPÉ · INTERFACE* — laboratoire `acoustique`.

**Énoncé.** Une onde plane rencontre normalement une interface sans absorption, Z₂=4Z₁. Déterminer les coefficients de pression et de vitesse, puis les fractions d'énergie. Établir les raccordements plutôt que mémoriser un signe.

**Corrigé.** Continuité : p_i+p_r=p_t et (p_i−p_r)/Z₁=p_t/Z₂. Ainsi r_p=3/5, t_p=8/5, r_v=−3/5 et t_v=2/5. R=9/25=0,36 ; T=(Z₁/Z₂)t_p²=16/25=0,64. R+T=1. Le signe négatif de r_v vient du sens de propagation réfléchi dans la relation p=−Zv_x. t_p>1 ne viole pas l'énergie : une même pression représente une intensité différente dans un milieu d'impédance différente.

### 34 · Dix violons : dix ou vingt décibels ?

*SUP → SPÉ · COHÉRENCE* — laboratoire `acoustique`.

**Énoncé.** Un instrument fournit I=10⁻⁵ W·m⁻² au point de mesure. Calculer son niveau. Comparer dix instruments d'intensité identique dans deux modèles : phases indépendantes, puis amplitudes parfaitement cohérentes et en phase. Un bruit peut-il être étudié par Fourier ?

**Corrigé.** Le niveau individuel est 70 dB. Avec phases indépendantes, les termes croisés ont une moyenne nulle : I_total=10I=10⁻⁴ W·m⁻², soit 80 dB. Avec amplitudes égales en phase, l'amplitude est multipliée par dix et l'intensité par cent, soit 90 dB au point considéré. Un bruit enregistré peut être analysé par transformée de Fourier ; son spectre n'est simplement pas limité à une famille d'harmoniques d'un fondamental périodique. L'addition de niveaux sans hypothèse sur les phases n'est donc pas une règle générale.

### 35 · Le mode plan passe sous 17 kHz

*SPÉ · CONDUIT RIGIDE* — laboratoire `conduit`.

**Énoncé.** Dans a=5 mm,b=10 mm,c=340 m·s⁻¹, calculer les coupures (0,0),(0,1),(1,0). Pour (0,1) à 20 kHz, déterminer k_z,c_g et c_φ. À 10 kHz, calculer la longueur 1/κ d'une branche évanescente. Quel mode peut malgré tout transporter ce son ?

**Corrigé.** Les coupures sont 0,17 kHz et 34 kHz. Pour 20 kHz, k_z=(2πf/c)√[1−(17/20)²]≈194,7 m⁻¹, c_g≈179,1 m·s⁻¹ et c_φ≈645,4 m·s⁻¹ ; leur produit vaut c². À 10 kHz, κ=(2π/c)√(17 000²−10 000²)≈254 m⁻¹ et 1/κ≈3,94 mm. Le mode (0,1) décroît axialement, mais le mode plan (0,0) reste propagatif. Une coupure appartient à un mode, pas à tous les sons du conduit.

### 36 · Le TP de diffraction à 25 kHz

*SUP → SPÉ · TP* — laboratoire `diffraction`.

**Énoncé.** Une fente uniforme de a=10 mm reçoit f=25 kHz dans c=340 m·s⁻¹. Calculer λ et décider si un premier zéro existe. Pour un modèle Fraunhofer, définir plutôt la demi-largeur à mi-intensité à partir de q≈1,39156 où (sin q/q)²=1/2. Préciser les limites de cette mesure.

**Corrigé.** λ=13,6 mm et λ/a=1,36>1. L'équation sinθ=λ/a n'a aucune solution réelle : 1,36 rad n'est pas un angle de premier minimum. Pour la demi-intensité, sinθ_{1/2}=1,39156λ/(πa)≈0,6024, donc θ_{1/2}≈0,647 rad, environ 37°. La largeur totale entre les deux demi-intensités est environ 74°. Cette valeur dépend du modèle d'ouverture uniforme en champ lointain ; une directivité d'émetteur, une distance insuffisante ou un capteur non uniforme modifie la mesure.

### 37 · Alias numérique et image stroboscopique

*SUP → SPÉ · TP DE MESURE* — laboratoire `diffraction`.

**Énoncé.** Échantillonner cos(2πft) à f_s=44,1 kHz pour f=25 kHz. Trouver une fréquence inférieure à f_s/2 donnant les mêmes valeurs. Un stroboscope à 50 Hz produit une image fixe : peut-on conclure à f=50 Hz ? Que produisent f=49 Hz et f=51 Hz dans un modèle de phase simple ?

**Corrigé.** Aux temps n/f_s, cos[2π(f_s−f)n/f_s]=cos(2πfn/f_s). L'alias est 19,1 kHz, inférieur à 22,05 kHz. Le filtre anti-repliement doit agir avant l'acquisition ; analyser après coup les valeurs seules ne restitue pas la fréquence supprimée. Pour le stroboscope, une vibration de fréquence m×50 Hz peut répéter sa phase à chaque éclair. À 49 et 51 Hz, la phase avance apparemment de −1 et +1 tour par seconde relativement aux éclairs. Varier la cadence et connaître l'excitation distingue ces possibilités ; une seule image fixe ne prouve pas l'unicité de f.

### 38 · Deux compressibilités et deux longueurs thermiques

*SPÉ · THERMODYNAMIQUE* — laboratoire `thermo`.

**Énoncé.** Pour un gaz parfait à p=10⁵ Pa, T=290 K, M=0,029 kg·mol⁻¹ et γ=1,4, calculer χ_T,χ_s,c_T,c_s. À f=1 kHz avec D_th=2×10⁻⁵ m²·s⁻¹, comparer δ_th à c_s/ω et au rayon 50 µm d'un petit conduit. Peut-on choisir une interpolation linéaire de célérité depuis ces rapports ?

**Corrigé.** χ_T=10⁻⁵ Pa⁻¹, χ_s≈7,14×10⁻⁶ Pa⁻¹ ; c_T≈288,3 m·s⁻¹ et c_s≈341,2 m·s⁻¹. δ_th=√(2D_th/ω)≈79,8 µm, c_s/ω≈54,3 mm : le rapport de volume est environ 0,00147. Mais δ_th/R≈1,60 : les frontières thermiques peuvent être importantes dans ce petit conduit. Ces contrôles d'échelle ne donnent pas une formule universelle d'interpolation ; un modèle couplé et des conditions thermiques aux murs sont nécessaires pour prédire précisément dispersion et pertes.

### 39 · Hartmann : circuit et limite sans champ

*SPÉ · EXTENSION MHD* — laboratoire `mhd`.

**Énoncé.** Dans le canal y=±h, prendre h=1 mm, η=0,002 Pa·s, σ_e=3×10⁶ S·m⁻¹, B=0,20 T et G=12 000 Pa·m⁻¹, avec E_z=0. Déduire Ha et u(0), puis montrer la limite B→0. Pour ρ=6000 kg·m⁻³, vérifier Rm avec U≈0,10 m·s⁻¹ et L=h.

**Corrigé.** v×B=uB e_z, donc j_z=σ_euB et j×B=−σ_eB²u e_x. Ha≈7,75 et u(0)=G[1−1/cosh(Ha)]/(σ_eB²)≈0,0999 m·s⁻¹. Développer cosh(Ha y/h)/cosh(Ha) donne 1+(Ha²/2)(y²/h²−1)+O(Ha⁴), donc u→G(h²−y²)/(2η). Rm=μ₀σ_eUh≈3,77×10⁻⁴, cohérent avec le champ imposé. Si le circuit interdit ce courant, E_z doit être déterminé autrement ; on ne conserve pas automatiquement le même freinage.

### 40 · Alfvén : signe, vitesse et partage d'énergie

*SPÉ · APPROFONDISSEMENT MHD* — laboratoire `mhd`.

**Énoncé.** Dans le modèle idéal ρ∂ₜu=(B₀/μ₀)∂_zb et ∂ₜb=B₀∂_zu, chercher une onde exp[i(kz−ωt)], k>0. Établir ω,c_A et la relation signée entre b et u. Pour ρ=10⁻⁶ kg·m⁻³,B₀=1 mT et une amplitude û=10 m·s⁻¹, calculer b̂ et les énergies moyennes. Prendre μ₀≈4π×10⁻⁷ H·m⁻¹.

**Corrigé.** Éliminer b donne ω²=k²B₀²/(μ₀ρ). Pour ω>0, c_A=B₀/√(μ₀ρ)≈892 m·s⁻¹ et b=−√(μ₀ρ)u. L'amplitude magnétique a le module 11,2 µT ; son signe fixe la phase relative pour cette direction. Les énergies moyennes sont ρû²/4 et b̂²/(4μ₀), égales à 2,5×10⁻⁵ J·m⁻³ chacune. Le flux moyen vaut c_A fois leur somme, environ 0,0446 W·m⁻². û/c_A et |b̂|/B₀≈0,0112 soutiennent la linéarisation. Le régime idéal d'induction et d'onde ne se déduit pas de la seule hypothèse Rm≪1 du canal de Hartmann.

## Sources et conventions

- Recueil personnel A. R., extrait de 30 pages : fiches P4 (pages imprimées 291–299), P6 (306–311), P7 (312–321), P8 (322–326). Les preuves, exemples et illustrations de l'atelier sont reformulés ; les pages et images du PDF personnel ne sont pas redistribuées.
- [MIT, Dick K. P. Yue, Marine Hydrodynamics (2005)](https://ocw.mit.edu/courses/2-20-marine-hydrodynamics-13-021-spring-2005/pages/lecture-notes/) : bilans, contraintes, vorticité, écoulements idéaux, couches limites et ondes de surface. Les dérivations du présent cours sont développées directement avec ses conventions déclarées.
- [MIT, Mark Drela et Ali Merchant, Aerodynamics of Viscous Fluids (2003)](https://ocw.mit.edu/courses/16-13-aerodynamics-of-viscous-fluids-fall-2003/pages/lecture-notes/) : cinématique, lois de conservation, écoulements visqueux et équations de couche limite.
- [MIT, Introduction to Plasma Physics I, chapitre 5 (2006)](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2006/0940abd0f5c16aa3972c8796c8ca52e2_chap5.pdf) : modèle linéaire des ondes et introduction aux ondes d'Alfvén. La MHD est proposée comme prolongement guidé.
- [Charles L. Fefferman, énoncé officiel du problème de Navier–Stokes](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) : formulation historique des quatre alternatives A–D et conditions du problème 3D. Lire également les corrections jointes au document.
- [Clay Mathematics Institute, annonce du 11 septembre 2026](https://www.claymath.org/news/navier-stokes-announcement/) : résolution apparemment obtenue et processus d'évaluation annoncé. Repère vérifié le 6 octobre 2026 ; le cours ne conclut pas à une attribution de prix confirmée.
- [Bulletin officiel, programme de physique PSI, annexe](https://cache.media.education.gouv.fr/file/31/03/9/ensecsup748_annexes_1417039.pdf) : les équations d'Euler et Navier–Stokes sont exclues du programme indiqué ; elles sont traitées ici comme extensions accompagnées.
- [Bulletin officiel, programme de physique PC, annexe](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf) : les exclusions relatives à certaines approches de cinématique et de dynamique doivent être respectées. Sup/Spé désigne dans cet atelier les outils mobilisés, et non une obligation identique pour chaque filière.
- Conventions : coordonnées et unités précisées dans chaque TP ; Δp=p_entrée−p_sortie pour Poiseuille ; η dynamique et ν=η/ρ cinématique ; exp[i(kx−ωt)] pour l'atténuation ; amplitudes acoustiques crête distinguées des valeurs efficaces. Les références vérifient les modèles ; aucune de leurs figures n'est reproduite.
