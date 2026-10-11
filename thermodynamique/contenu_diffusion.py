"""P23 : cours courts, manipulations concrètes et exercices corrigés."""
LESSONS=[]
EXERCISES=[]
GUIDES={}

def lesson(id_,title,level,html):
    LESSONS.append(dict(lab=id_,title=title,level=level,html=html))

def exercise(id_,title,level,question,answer):
    EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,
                    levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=first_steps,expected=expected)

lesson('fourier_barre','Du bilan local à un profil stationnaire','Sup → Spé','''
<p>Une barre a longueur L en mètres, section S en m² et conductivité λ en W/(m·K). T(x) est sa température ; j est le courant thermique surfacique en W/m², positif vers +x. Les deux bords sont à T₁ et T₂.</p>
<p>Fourier donne <b>j=−λT′</b> : la chaleur va vers les températures décroissantes. Sans source et en régime permanent, un petit tronçon reçoit autant de puissance qu’il en transmet, donc j′=0. Pour λ constant, T″=0.</p>
<p>Les deux valeurs au bord imposent T=T₁+(T₂−T₁)x/L, puis j=λ(T₁−T₂)/L. La puissance totale est Φ=jS, en watts. Doubler la section double Φ sans changer j. Si T₁&lt;T₂, j et Φ deviennent négatifs : c’est une inversion physique du transfert.</p>''')
lesson('fourier_barre','Résistance thermique et limites de l’analogie électrique','Sup','''
<p>R est la résistance thermique de la barre, en K/W ; ΔT=T₁−T₂ est la différence orientée des températures. La relation <b>ΔT=RΦ</b> donne R=L/(λS).</p>
<p>Elle ressemble à U=RI : différence de température et tension jouent des rôles analogues, comme puissance thermique et courant électrique. L’analogie aide à assembler des parois ; elle ne signifie pas que la chaleur est une quantité conservée dans tous les régimes. En transitoire, un tronçon peut stocker de l’énergie interne.</p>
<p>À ΔT=0, la puissance est nulle mais R n’a pas disparu : c’est une propriété géométrique et matérielle. Les écarts en °C et en K sont identiques ; convertir les températures absolues n’est nécessaire que lorsqu’une loi utilise T elle-même, par exemple un calcul d’entropie.</p>''')
exercise('fourier_barre','Section, courant et puissance','Sup','<p>Une barre a L=0,5 m, S=20 cm², λ=80 W/(m·K), T₁=80°C et T₂=20°C. Calculer j, Φ et R.</p>','<p>S=0,002 m². j=80×60/0,5=<b>9 600 W/m²</b>. Φ=jS=<b>19,2 W</b>. R=L/(λS)=<b>3,125 K/W</b>. Vérification : RΦ=60 K. Confondre cm² et m² produirait un facteur 10 000.</p>')
exercise('fourier_barre','Changer le matériau','Sup','<p>À géométrie et températures fixées, remplacer λ=80 par λ=0,04 W/(m·K). Comment changent le profil, la puissance et la résistance ?</p>','<p>Le profil T(x) reste la droite déterminée par les bords. La puissance est divisée par 2 000 et la résistance multipliée par 2 000. Dans l’exemple précédent, Φ=<b>0,0096 W</b> et R=<b>6 250 K/W</b>. Un même profil ne signifie pas un même transfert.</p>')
exercise('fourier_barre','Retrouver le régime permanent à partir du premier principe','Spé','<p>Écrire le bilan d’un tronçon dx, avec capacité volumique ρc constante, puis obtenir l’équation de chaleur.</p>','<p>Le stockage vaut ρcSdx ∂T/∂t. La puissance reçue est S[j(x)−j(x+dx)]≈−Sdx∂j/∂x. Ainsi ρc∂T/∂t=−∂j/∂x. Fourier donne <b>∂T/∂t=χ∂²T/∂x²</b>, χ=λ/(ρc). En permanent, T″=0, ce qui retrouve le laboratoire.</p>')
guide('fourier_barre','Relier le premier principe local, Fourier et la résistance de l’exercice 1.',
 ['L est une longueur en m ; S une section, convertie de cm² en m².', 'λ caractérise le matériau ; j est en W/m² et Φ=jS en W.', 'Le courant positif va du bord x=0 au bord x=L.'],
 ['Barre homogène et faces latérales isolées.', 'Régime permanent, conductivité constante, aucune source interne.'],
 ['Bilan d’un petit volume et dérivation spatiale.', 'Conditions aux bords et conversion d’unités.'],
 'Déterminer le profil linéaire et distinguer j de Φ.', 'Construire l’équation de chaleur et la résistance.', 'Conductivité variable et sources internes.',
 ['Choisir la barre métallique et vérifier les unités de j et Φ.', 'Passer à l’isolant : comparer le même profil à une puissance différente.', 'Inverser les températures et prévoir le signe avant le calcul.'],
 'Écrire une résistance avec sa géométrie et annoncer clairement le sens du flux.')

lesson('paroi_composite','Quatre résistances traversées par une même puissance','Sup → Spé','''
<p>S est l’aire du mur ; e₁,e₂ ses épaisseurs et λ₁,λ₂ les conductivités. hᵢ,hₑ sont les coefficients de convection, en W/(m²·K). Les températures de l’air sont imposées de chaque côté.</p>
<p>Une couche plane a résistance e/(λS). Une interface avec l’air échange la puissance hS(Tsurface−Tair), donc a résistance 1/(hS). En permanent sans source, la même puissance Φ traverse les deux couches et les deux échanges.</p>
<p>La résistance totale est <b>R=1/(hᵢS)+e₁/(λ₁S)+e₂/(λ₂S)+1/(hₑS)</b>. On calcule Φ=(Tint−Text)/R, puis chaque chute de température ΦRᵢ. Les températures de l’air et des surfaces ne sont pas égales en général. Le tableau distingue les cinq lieux.</p>''')
lesson('paroi_composite','Où une amélioration sera-t-elle utile ?','Spé','''
<p>Rᵢ est la résistance d’un élément et Rtotal leur somme. Sa part Rᵢ/Rtotal donne aussi sa part de la chute de température lorsque Φ est uniforme.</p>
<p>Si l’isolant représente presque toute la résistance, augmenter sa conductivité augmente fortement la perte ; améliorer une convection déjà très efficace change peu le résultat. Inversement, un faible coefficient h peut limiter l’ensemble.</p>
<p>Avec les autres éléments fixés, Φ(e₂)=ΔT/[Rautres+e₂/(λ₂S)]. Le gain d’épaisseur suit une loi décroissante mais n’efface pas les autres résistances. Pour plusieurs surfaces indépendantes en parallèle, ce sont les puissances qui s’additionnent et 1/Réquiv=Σ1/Rᵢ. Une fuite thermique peut donc contourner une couche très isolante.</p>''')
exercise('paroi_composite','Brique et isolant','Sup → Spé','<p>Sur S=10 m² : e₁=0,2 m, λ₁=0,8 ; e₂=0,1 m, λ₂=0,04 ; hᵢ=8 et hₑ=20, en unités SI. Tint=20°C, Text=−5°C. Calculer la perte.</p>','<p>Les résistances valent 0,0125 ; 0,025 ; 0,25 ; 0,005 K/W. Leur somme est <b>0,2925 K/W</b>. Φ=25/0,2925≈<b>85,47 W</b>, soit 8,55 W/m². L’isolant représente 85,47 % de la résistance totale.</p>')
exercise('paroi_composite','Une surface extérieure différente de l’air','Sup','<p>Avec les données précédentes, déterminer les températures de surface intérieure et extérieure.</p>','<p>La surface intérieure est à 20−Φ/(hᵢS)≈<b>18,93°C</b>. La surface extérieure est à −5+Φ/(hₑS)≈<b>−4,57°C</b>. Ces écarts permettent justement les échanges convectifs. La température d’interface des solides vaut 20−Φ(0,0125+0,025)≈16,79°C.</p>')
exercise('paroi_composite','Un pont thermique en parallèle','Spé','<p>Un mur et un pont thermique ont respectivement Rmur=0,3 K/W et Rpont=2 K/W. Ils sont soumis au même écart de 24 K. Calculer la puissance totale et comparer à la somme des résistances.</p>','<p>Les puissances valent 24/0,3=80 W et 24/2=12 W. Le total est <b>92 W</b>, et Réquiv=24/92≈<b>0,261 K/W</b>. Additionner 0,3+2 serait traiter les passages en série, ce qui est faux ici : ils relient directement les mêmes deux ambiances.</p>')
guide('paroi_composite','Utiliser l’analogie électrique sans perdre les surfaces et les températures d’interface.',
 ['eᵢ,λᵢ sont propres à chaque couche ; S est commun.', 'hᵢ et hₑ décrivent les échanges avec l’air.', 'Les repères 0 à 4 indiquent les lieux du tableau, pas une distance dans l’air.'],
 ['Conduction plane, contacts parfaits et air thermostaté.', 'Rayonnement et ponts thermiques omis du calcul principal.'],
 ['Assemblage en série et puissances en parallèle.', 'Reconstruction des températures avec ΦR.'],
 'Additionner quatre résistances et calculer une puissance.', 'Identifier les éléments dominants et les températures des surfaces.', 'Ponts thermiques et résistance de contact.',
 ['Choisir brique et isolant puis lire les cinq températures.', 'Réduire l’isolant et observer sa part de résistance.', 'Réduire h extérieur : trouver où la chute de température augmente.'],
 'Distinguer température d’air, température de surface et interface solide.')

lesson('isolation_radiale','La surface change pendant le transfert radial','Spé','''
<p>Rᵢ est le rayon intérieur, Rₑ le rayon extérieur, λ la conductivité et Φ la puissance totale sortante. h est le coefficient de convection extérieure, en W/(m²·K). Dans un cylindre de longueur L, la surface à rayon r vaut 2πrL ; dans une sphère elle vaut 4πr².</p>
<p>En permanent Φ est constant, mais j=Φ/S(r) varie avec r. Intégrer Fourier entre les deux rayons donne <b>Rcyl=ln(Rₑ/Rᵢ)/(2πλL)</b> et <b>Rsph=(1/Rᵢ−1/Rₑ)/(4πλ)</b>. Une formule plane avec une seule surface ne conviendrait pas à une coque épaisse.</p>
<p>La surface extérieure échange avec l’air par convection : ajouter 1/[hS(Rₑ)]. Sa température se calcule par Tsurface=Tint−ΦRcond ; l’écart restant avec l’air alimente la convection.</p>''')
lesson('isolation_radiale','Le rayon critique vient d’une compétition','Spé','''
<p>h est le coefficient de convection extérieur. Ajouter une épaisseur augmente la résistance conductrice, mais agrandit la surface convective et réduit sa résistance.</p>
<p>Pour le cylindre, dériver Rtotal en Rₑ donne 1/(2πλLRₑ)−1/(2πhLRₑ²). Le minimum est en <b>Rcrit=λ/h</b>. Pour la sphère, le calcul analogue donne <b>Rcrit=2λ/h</b>. Puisque Φ=ΔT/Rtotal, ce minimum maximise la perte.</p>
<p>Le seuil n’est accessible que si Rcrit&gt;Rᵢ. Si le rayon intérieur est déjà plus grand, toute épaisseur ajoutée réduit la perte. L’existence d’un rayon critique ne signifie donc pas que toute isolation augmente le transfert. Le laboratoire compare ces deux cas.</p>''')
exercise('isolation_radiale','Deux rayons critiques','Spé','<p>Avec λ=0,1 W/(m·K) et h=4 W/(m²·K), calculer les rayons critiques. Pour Rᵢ=2 cm, quelles épaisseurs les atteignent ?</p>','<p>Le cylindre a Rcrit=<b>2,5 cm</b>, la sphère <b>5 cm</b>. À rayon intérieur 2 cm, les épaisseurs correspondantes sont 0,5 cm et 3 cm. Si Rᵢ était 10 cm, aucun de ces minima ne serait accessible par ajout d’isolant.</p>')
exercise('isolation_radiale','Puissance constante et courant non constant','Sup → Spé','<p>Une sphère transmet 50 W. Comparer j à r=0,1 m et à r=0,2 m.</p>','<p>j=Φ/(4πr²). Les valeurs sont environ <b>397,9 W/m²</b> et <b>99,47 W/m²</b>. Le courant surfacique est divisé par quatre lorsque le rayon double. La puissance traversant chaque sphère reste bien 50 W.</p>')
exercise('isolation_radiale','Limite d’une coque mince','Spé','<p>Pour une sphère, montrer que la résistance tend vers e/(λSᵢ) lorsque e=Rₑ−Rᵢ est petit devant Rᵢ.</p>','<p>Rsph=e/[4πλRᵢ(Rᵢ+e)]. Pour e/Rᵢ≪1, remplacer Rᵢ+e par Rᵢ au premier ordre : <b>Rsph≈e/(4πλRᵢ²)=e/(λSᵢ)</b>. L’approximation plane est donc locale et suppose une faible variation de surface.</p>')
guide('isolation_radiale','Prolonger la coque de l’exercice 1 et expliquer pourquoi une isolation peut d’abord accroître la perte.',
 ['Rᵢ est fixé ; Rₑ=Rᵢ+e varie.', 'Φ est total en W ; j dépend de l’aire à chaque rayon.', 'λ est la conductivité en W/(m·K), h la convection extérieure en W/(m²·K). λ/h et 2λ/h sont des longueurs.'],
 ['Cylindre long ou sphère complète, pas de source.', 'Convection seulement à l’extérieur, coefficients constants.'],
 ['Bilan radial et intégration de Fourier.', 'Dérivation d’une résistance et comparaison au rayon intérieur.'],
 'Relier surface croissante et courant surfacique.', 'Calculer les résistances radiales et les extrema.', 'Couches multiples cylindriques et échange radiatif.',
 ['Choisir le cylindre et chercher le maximum sur la courbe de perte.', 'Passer à la sphère : comparer les deux seuils.', 'Choisir un rayon intérieur au-dessus du seuil et vérifier la décroissance.'],
 'Dire si le rayon critique est accessible et distinguer Φ constant de j constant.')

lesson('igloo','Le rayon choisi fait partie de la formule','Sup → Spé','''
<p>R est ici le rayon <b>intérieur</b> de l’igloo et e son épaisseur ; le rayon extérieur vaut R+e. λ est la conductivité de neige ou de glace. P est la puissance thermique nette des occupants, en watts.</p>
<p>Le sol étant supposé isolé, la puissance sort à travers une hémisphère d’aire 2πr². Sa résistance est <b>Rth=[1/R−1/(R+e)]/(2πλ)</b>. Le bilan stationnaire donne Tint=Text+P Rth.</p>
<p>Une puissance métabolique nette n’est pas la puissance radiative totale d’un corps à 310 K. Dans le laboratoire elle est réglée directement : cela permet de comprendre le bilan sans confondre émission et échange net. Les résultats sont ceux d’un modèle conductif idéal ; une paroi intérieure au-dessus de 0°C impose d’étudier sa fonte.</p>''')
lesson('igloo','Chercher une épaisseur et vérifier qu’elle existe','Spé','''
<p>ΔT est l’écart intérieur visé au-dessus de l’extérieur. Pour un apport P fixé, on demande Rth=ΔT/P.</p>
<p>Résoudre donne <b>e=R²ΔT/[P/(2πλ)−RΔT]</b>. L’épaisseur est positive et finie seulement si le dénominateur est positif. À rayon intérieur fixé, la résistance tend vers 1/(2πλR) quand e augmente indéfiniment ; une résistance demandée plus grande est inaccessible dans ce modèle.</p>
<p>Cette recherche ne prouve pas la possibilité d’un véritable igloo solide à température de paroi positive. Le statut de validité signale la fusion : le bilan avec changement de phase et les échanges de surface doivent alors remplacer ce calcul conditionnel. Neige poreuse et glace dense ont par ailleurs des conductivités très différentes.</p>''')
exercise('igloo','Épaisseur conditionnelle dans de la neige','Spé','<p>R=1 m, λ=0,15 W/(m·K), P=100 W, Text=−20°C. Quelle épaisseur le modèle demanderait-il pour Tint=15°C ? Interpréter.</p>','<p>ΔT=35 K. e=35/[100/(2π×0,15)−35]≈<b>0,492 m</b>. C’est une valeur du modèle conductif constant. La surface intérieure y dépasserait 0°C : il faut intégrer la fonte, les échanges avec l’air et les autres pertes pour annoncer un équilibre réel de neige solide.</p>')
exercise('igloo','Même puissance dans de la glace dense','Spé','<p>Avec R=1 m, λ=2 W/(m·K), P=100 W et Text=−20°C, peut-on atteindre 15°C par ajout d’épaisseur dans le même modèle ?</p>','<p>La hausse maximale vaut P/(2πλR)≈<b>7,96 K</b>. La température limite du modèle est donc environ −12,04°C, inférieure à 15°C. Le dénominateur de l’épaisseur demandée serait négatif ; <b>aucune épaisseur positive ne convient</b> dans ce modèle à rayon intérieur fixe.</p>')
exercise('igloo','Passer de la sphère à la demi-sphère','Sup → Spé','<p>Pour les mêmes rayons et températures, comparer la puissance transmise par une sphère complète et une hémisphère, sol isolé.</p>','<p>La surface de transfert hémisphérique est la moitié de celle de la sphère. La résistance est donc doublée et la puissance divisée par deux. Cette conclusion suppose que les surfaces planes de fermeture n’échangent pas ; ajouter un transfert par le sol demanderait un passage en parallèle.</p>')
guide('igloo','Reprendre l’exercice 2 avec une puissance nette définie et une géométrie sans ambiguïté.',
 ['R est intérieur et R+e extérieur.', 'P=nombre de personnes × puissance nette par personne.', 'La température calculée est conditionnelle au modèle de paroi solide constante.'],
 ['Sol isolé et conduction hémisphérique idéale.', 'La fusion n’est pas calculée ; son besoin est indiqué si Tint>0°C.'],
 ['Bilan de puissance et résistance radiale.', 'Résolution d’une épaisseur et contrôle d’une condition d’existence.'],
 'Compter les watts reçus et évacués.', 'Vérifier la géométrie et la possibilité d’une épaisseur.', 'Fusion, ventilation et rayonnement net.',
 ['Choisir neige isolante : lire puissance, température et statut de paroi.', 'Passer à la glace dense et expliquer le changement.', 'Changer le nombre de personnes puis regarder si l’épaisseur visée existe.'],
 'Séparer un bilan idéal et une réalisation physique, avec puissance et rayon correctement définis.')

lesson('diffusion_1d','Deux modes, deux temps de refroidissement','Spé','''
<p>L est la longueur, χ la diffusivité en m²/s et T₀ la température des deux extrémités. θ=T−T₀ est l’écart de température. Le temps réduit est χt/L².</p>
<p>Pour l’équation θt=χθxx et des bords θ=0, un mode sin(nπx/L) décroît avec <b>exp(−n²π²χt/L²)</b>. Le laboratoire prépare le premier mode seul ou une somme des rangs 1 et 3. Le rang 3 décroît neuf fois plus vite.</p>
<p>Le profil se lisse parce que les détails spatiaux fins disparaissent plus vite. Ce n’est pas une perte mystérieuse d’énergie : les extrémités thermostatées évacuent la chaleur. Un système isolé aurait d’autres conditions aux bords et un mode moyen conservé.</p>''')
lesson('diffusion_1d','FTCS : une condition de stabilité qui a un sens physique','Spé','''
<p>Δx est la maille spatiale, Δt le pas temporel et r=χΔt/Δx² le nombre de Fourier du calcul. Le schéma explicite donne θᵢ,suiv=(1−2r)θᵢ+rθᵢ₋₁+rθᵢ₊₁.</p>
<p>Pour <b>0≤r≤1/2</b>, les trois coefficients sont positifs et de somme 1. La nouvelle valeur reste entre les anciennes valeurs voisines : le calcul respecte un principe du maximum discret. Au-delà, cette garantie disparaît et des oscillations numériques peuvent croître.</p>
<p>Le laboratoire ajuste Δt pour rester sous le r demandé. La référence par modes est indépendante. Raffiner seulement le temps ne corrige pas toute l’erreur spatiale ; raffiner l’espace avec un même r impose aussi un pas temporel plus petit.</p>''')
exercise('diffusion_1d','Le premier temps de relaxation','Spé','<p>Avec L=0,2 m et χ=10 mm²/s, calculer le temps de décroissance par e du premier mode.</p>','<p>χ=10⁻⁵ m²/s. Le temps vaut L²/(π²χ)=0,04/(π²×10⁻⁵)≈<b>405,3 s</b>. Celui du troisième mode est neuf fois plus court, environ 45,03 s.</p>')
exercise('diffusion_1d','Une maille plus fine impose un pas plus court','Spé','<p>Pour χ=10⁻⁵ m²/s et Δx=5 mm, quel pas maximal assure r≤1/2 ? Que devient-il si Δx est divisée par deux ?</p>','<p>Δt≤Δx²/(2χ)=25×10⁻⁶/(2×10⁻⁵)=<b>1,25 s</b>. Diviser Δx par deux divise le pas maximal par quatre : <b>0,3125 s</b>. Le coût augmente à la fois dans le nombre de points et le nombre de pas.</p>')
exercise('diffusion_1d','Prévoir le lissage sans simulation','Spé','<p>Le profil initial vaut A[sin(πx/L)+0,4sin(3πx/L)]. Trouver le rapport d’amplitudes des deux modes au temps t.</p>','<p>Le rapport rang 3 / rang 1 vaut <b>0,4 exp(−8π²χt/L²)</b>. Il tend vers zéro. La forme devient donc proportionnelle au premier sinus longtemps avant que toute la barre revienne à T₀.</p>')
guide('diffusion_1d','Comparer une solution modale à un véritable schéma de diffusion stable.',
 ['L est la longueur de barre en m ; χ sa diffusivité, convertie de mm²/s en m²/s.', 'N est le nombre de subdivisions ; Δx=L/N est la maille spatiale en m et Δt le pas temporel en s.', 'r=χΔt/Δx² est le nombre de Fourier sans dimension ; il contrôle la stabilité.', 'T₀ est la température des extrémités en °C. La carte T(x,t) donne la température à la position x en m et au temps t en s.'],
 ['Deux extrémités thermostatées à T₀.', 'Un ou deux modes initiaux ; r≤0,49.'],
 ['Séparation des variables et modes propres.', 'Différences finies, stabilité et principe du maximum.'],
 'Lire le refroidissement et le sens des flux aux bords.', 'Démontrer le facteur n² et la condition de stabilité.', 'Schémas implicites et estimation d’erreur.',
 ['Préparer deux modes et suivre la disparition des détails.', 'Comparer FTCS et modes exacts au temps final.', 'Augmenter N : lire l’erreur et le nombre de pas réellement utilisés.'],
 'Contrôler la stabilité avant de confondre un défaut numérique avec un phénomène physique.')

lesson('demi_espace','Une solution de similitude pour le choc thermique','Spé','''
<p>x est la profondeur, t le temps, χ la diffusivité et T₀ la température initiale. La surface est imposée à Ts pour t&gt;0. Le matériau est supposé semi-infini.</p>
<p>Pour u sans dimension, la fonction d’erreur est erf(u)=(2/√π)∫₀ᵘexp(−s²)ds, où s est la variable d’intégration. Sa complémentaire est erfc(u)=1−erf(u).</p>
<p>La variable x/(2√χt) regroupe position et temps. La solution est <b>T=T₀+(Ts−T₀)erfc[x/(2√χt)]</b>. Elle vaut Ts au bord et rejoint T₀ en profondeur.</p>
<p>La longueur √χt grandit comme la racine du temps. Pour comparer deux instants, il faut multiplier aussi les profondeurs par √(t₂/t₁). Une perturbation n’a pas de front net : ses petites valeurs s’étendent jusqu’à toute profondeur dans ce modèle diffusif.</p>''')
lesson('demi_espace','Un flux initial singulier peut donner une énergie finie','Spé','''
<p>ρc est la capacité volumique en J/(m³·K), et λ=χρc la conductivité. j(0,t) est le courant surfacique entrant dans le matériau.</p>
<p>Dériver le profil donne <b>j(0,t)=λ(Ts−T₀)/√(πχt)</b>. Ce flux diverge au départ du choc idéal, mais son intégrale temporelle converge : l’énergie reçue par aire vaut <b>2ρc(Ts−T₀)√(χt/π)</b>.</p>
<p>On retrouve cette énergie en intégrant ρc(T−T₀) dans l’espace. Ce double calcul vérifie le premier principe. En refroidissement, le flux et l’énergie reçue sont négatifs. La singularité au départ disparaîtrait avec une variation de surface étalée sur un temps fini.</p>''')
exercise('demi_espace','Multiplier le temps par quatre','Sup → Spé','<p>Que deviennent la longueur de pénétration, le flux de surface et l’énergie reçue lorsque t est multiplié par quatre ?</p>','<p>√χt est multipliée par <b>2</b>, le flux proportionnel à t⁻¹ᐟ² est divisé par <b>2</b>, et l’énergie proportionnelle à √t est multipliée par <b>2</b>. Ces lois d’échelle valent à paramètres de matériau et températures fixés.</p>')
exercise('demi_espace','Dimension d’une énergie par surface','Sup → Spé','<p>Vérifier l’unité de ρcΔT√χt. Pourquoi ne s’agit-il pas d’une énergie totale ?</p>','<p>ρc est en J/(m³·K), ΔT en K et √χt en m : le produit est en <b>J/m²</b>. Le problème est invariant dans le plan de la surface. Pour une région d’aire S où cette approximation est valable, multiplier par S donne l’énergie totale.</p>')
exercise('demi_espace','Retrouver le bilan par une intégrale d’erfc','Spé','<p>Montrer ∫₀∞erfc(u)du=1/√π, puis retrouver l’énergie du profil.</p>','<p>Intégrer par parties : le bord u erfc(u) s’annule et erfc′=−2e⁻ᵘ²/√π. L’intégrale vaut (2/√π)∫₀∞ue⁻ᵘ²du=<b>1/√π</b>. Poser x=2√χt u dans ∫ρc(T−T₀)dx donne 2ρcΔT√χt/√π, comme l’intégrale temporelle du flux.</p>')
guide('demi_espace','Relier l’exercice 6, l’échelle de diffusion et un bilan d’énergie indépendant.',
 ['x est une profondeur ; χt a la dimension d’une longueur au carré.', 'ρc est une capacité par volume ; λ=χρc.', 'Énergie reçue est donnée par unité de surface.'],
 ['Solide semi-infini et surface thermostatée brutalement.', 'Propriétés constantes et pas de changement de phase.'],
 ['Solution de similitude et fonctions erf/erfc.', 'Dérivation de profil, Fourier et intégration de puissance.'],
 'Prévoir une profondeur en √t et le signe du transfert.', 'Vérifier la solution et les deux calculs d’énergie.', 'Conditions convectives et surface chauffée progressivement.',
 ['Chauffer la surface et lire flux puis énergie.', 'Multiplier le temps par quatre : tester les trois lois d’échelle.', 'Refroidir et vérifier les valeurs algébriques négatives.'],
 'Distinguer une singularité de flux intégrable et une énergie infinie.')

lesson('onde_thermique','Une excitation périodique dans une équation de diffusion','Spé','''
<p>z est la profondeur, χ la diffusivité, P la période et ω=2π/P la pulsation. T₀ est la température moyenne et A l’amplitude en K. Au temps t, la surface a température T₀+Acosωt.</p>
<p>θ(z) est l’amplitude complexe de l’écart T−T₀ ; i²=−1. La solution θ(z)eⁱʷᵗ satisfait χθ″=iωθ. La décroissance en profondeur impose θ=Aexp[−(1+i)z/δ], avec <b>δ=√(2χ/ω)</b>. La température réelle vaut T₀+Aexp(−z/δ)cos(ωt−z/δ).</p>
<p>Une même longueur δ contrôle la perte d’amplitude et le déphasage. À z=δ, l’amplitude vaut A/e et la phase retarde de 1 radian. Le dessin est une solution périodique établie ; il ne représente pas le premier jour après l’application du forçage.</p>''')
lesson('onde_thermique','Jour et année : une échelle de temps devient une profondeur','Spé','''
<p>Le retard de phase non ramené à une période est z/(δω). L’amplitude observable vaut Aexp(−z/δ).</p>
<p>Comme δ=√(χP/π), une période q fois plus longue pénètre √q fois plus profondément. Le cycle annuel et le cycle journalier ne chauffent donc pas les mêmes couches du sol.</p>
<p>Une « vitesse de phase » δω=√(2χω) dépend de la fréquence ; ce n’est pas une vitesse de transport sans perte. La diffusion conserve une forte atténuation. Quand une profondeur accumule un grand retard mais une amplitude presque nulle, la phase reste mathématiquement définie alors qu’une mesure devient délicate.</p>''')
exercise('onde_thermique','Pénétration journalière','Spé','<p>Avec χ=1 mm²/s et P=86 400 s, calculer δ. Quelle amplitude reste à z=0,2 m si A=10 K ?</p>','<p>χ=10⁻⁶ m²/s. δ=√(χP/π)≈<b>0,166 m</b>. L’amplitude vaut 10exp(−0,2/δ)≈<b>2,99 K</b>. La profondeur de 20 cm réduit déjà fortement le cycle journalier.</p>')
exercise('onde_thermique','Rapport entre saison et journée','Sup → Spé','<p>À matériau fixé, trouver le rapport des profondeurs caractéristiques annuelle et journalière.</p>','<p>Les périodes sont dans le rapport 365,25. Les profondeurs sont donc dans le rapport <b>√365,25≈19,11</b>. Pour χ=10⁻⁶ m²/s, δannuelle≈3,17 m.</p>')
exercise('onde_thermique','Atténuation et retard au même point','Spé','<p>À z=δ, exprimer le retard comme fraction de la période et l’amplitude comme fraction de l’amplitude de surface.</p>','<p>Le retard vaut 1/ω=P/(2π), soit <b>15,92 % d’une période</b>. L’amplitude vaut <b>1/e≈36,79 %</b> de celle de surface. Les deux résultats viennent du même exposant complexe, mais ont des significations différentes.</p>')
guide('onde_thermique','Prolonger l’exercice 7 en comparant les profondeurs atteintes par deux cycles concrets.',
 ['P est la période journalière ou annuelle, en s ; ω=2π/P est la pulsation.', 'T₀ est la température moyenne ; A est l’amplitude de surface en K. θ(z) est l’amplitude complexe à la profondeur z.', 'δ est une longueur de pénétration, pas une longueur d’onde sans atténuation.', 'Le retard est donné en heures et n’est pas réduit modulo P.'],
 ['Sol semi-infini homogène, régime périodique établi.', 'La surface est imposée ; la diffusivité est constante.'],
 ['Écriture complexe dans une équation différentielle spatiale.', 'Ordres de grandeur et racines carrées des périodes.'],
 'Comparer qualitativement un jour et une saison.', 'Calculer amplitude, phase et longueur δ.', 'Réponse fréquentielle et identification d’une diffusivité.',
 ['Observer le cycle journalier à 0,2 m.', 'Passer au cycle annuel à 2 m et comparer δ.', 'Revenir au jour à 1 m : expliquer la petite amplitude malgré un retard important.'],
 'Lire séparément amplitude et phase, en identifiant la fréquence choisie.')

lesson('refroidissement_biot','Le modèle uniforme est une hypothèse à contrôler','Sup → Spé','''
<p>La plaque a demi-épaisseur a, capacité volumique ρc et conductivité λ. S est l’aire d’une face ; le volume est V=2aS et l’aire d’échange Séchange=2S. Ses deux faces échangent avec un air à Tair par un coefficient h. Bi=ha/λ est le nombre de Biot.</p>
<p>Supposer la température uniforme donne le bilan ρc(2aS)T′=−2hS(T−Tair). La solution est <b>T−Tair=(Tinitial−Tair)exp[−ht/(ρca)]</b>. La longueur caractéristique V/Séchange vaut a, et non 2a.</p>
<p>La résistance interne devient faible devant celle de convection lorsque Bi est petit. Le repère Bi&lt;0,1 est pratique ; le laboratoire montre l’écart réel et ne le transforme pas en une garantie universelle de précision.</p>''')
lesson('refroidissement_biot','Centre, surface et moyenne : trois températures différentes','Spé · Prolongement','''
<p>χ=λ/(ρc) est la diffusivité et Fo=χt/a² le temps réduit. La coordonnée du centre est x=0 et les faces sont en ±a.</p>
<p>Les modes exacts de la plaque convective sont cos(μx/a), où <b>μtanμ=Bi</b>. Leur coefficient initial est 4sinμ/(2μ+sin2μ), et ils décroissent comme exp(−μ²Fo). La moyenne d’un mode ajoute le facteur sinμ/μ.</p>
<p>Quand Bi est grand, la surface rejoint l’air avant le centre. Le modèle uniforme ne peut représenter ce gradient. La somme de 80 modes du laboratoire sert de référence à température initiale uniforme ; les profils réels se comparent pour t&gt;0.</p>''')
exercise('refroidissement_biot','La bonne longueur de Biot','Sup → Spé','<p>Une plaque de 20 mm d’épaisseur a λ=80 W/(m·K), h=20 W/(m²·K) et ρc=2 MJ/(m³·K). Calculer Bi et le temps capacitif.</p>','<p>a=10 mm=0,01 m. Bi=ha/λ=<b>0,0025</b>, favorable au modèle uniforme. Le temps capacitif vaut ρca/h=<b>1 000 s</b>. Employer l’épaisseur totale doublerait les deux résultats alors que les deux faces échangent.</p>')
exercise('refroidissement_biot','Pourquoi Bi petit donne le modèle capacitif','Spé','<p>Pour Bi≪1, utiliser μtanμ=Bi sur le premier mode pour retrouver le facteur de décroissance uniforme.</p>','<p>Pour μ petit, μtanμ≈μ², donc μ₁²≈Bi et son coefficient tend vers 1. Le facteur exp(−μ₁²χt/a²) devient exp[−Biχt/a²]=<b>exp[−ht/(ρca)]</b>. Les modes plus rapides corrigent les petits gradients internes.</p>')
exercise('refroidissement_biot','Une surface froide ne signifie pas un centre froid','Sup → Spé','<p>À Bi grand, quel point refroidit d’abord ? Quelle température faut-il employer dans le bilan d’énergie totale ?</p>','<p>Les surfaces échangent directement avec l’air et refroidissent d’abord. L’énergie totale est proportionnelle à <b>la moyenne volumique</b> de T, pas à sa valeur de surface ni seulement à celle du centre. Le laboratoire trace les trois pour distinguer les grandeurs.</p>')
guide('refroidissement_biot','Choisir le modèle de refroidissement en confrontant sa validité à un profil spatial.',
 ['a est la demi-épaisseur en m ; S est l’aire d’une face. V=2aS et Séchange=2S donnent volume et aire totale d’échange.', 'λ est la conductivité et h le coefficient de convection. Bi=ha/λ compare résistance interne et externe.', 'ρc est la capacité volumique en J/(m³·K) ; ρca/h est le temps de relaxation du modèle uniforme en s.'],
 ['Plaque homogène, air identique sur les deux faces.', 'Référence par 80 modes, sans changement de phase.'],
 ['Bilan global et comparaison de temps caractéristiques.', 'Modes propres avec une condition convective.'],
 'Résoudre le modèle exponentiel uniforme.', 'Calculer Bi et identifier les trois températures.', 'Détermination des modes avec conditions de Robin.',
 ['Choisir Bi petit : comparer toutes les températures.', 'Choisir Bi grand : repérer le gradient centre–surface.', 'Réduire l’épaisseur et suivre l’amélioration du modèle capacitif.'],
 'Donner la longueur caractéristique et vérifier une approximation avant de l’utiliser.')

lesson('diffusion_2d','Une impulsion répartie dans une plaque mince','Spé','''
<p>Q est l’énergie de la tache en joules, e l’épaisseur de plaque et ρce sa capacité par surface. χ est la diffusivité ; σ₀ est l’écart-type initial dans chaque direction. x,y sont les coordonnées du plan, T₀ la température de fond et σ la largeur par direction au temps t.</p>
<p>La tache gaussienne conserve sa forme : <b>σ²=σ₀²+2χt</b>. Son élévation de température est Qexp[−(x²+y²)/(2σ²)]/(2πρceσ²). La double intégrale de ρce(T−T₀) vaut toujours Q.</p>
<p>Le maximum diminue comme 1/σ² tandis que l’aire caractéristique augmente comme σ². Cette compensation exprime le premier principe. Une largeur initiale non nulle évite le pic infini d’une source ponctuelle au temps zéro.</p>''')
lesson('diffusion_2d','Attention à la dimension d’une variance','Sup → Spé','''
<p>Les variances suivant x et y valent chacune σ². Leur somme donne la moyenne radiale <b>⟨r²⟩=⟨x²+y²⟩=2σ²</b>.</p>
<p>La diffusion ajoute donc 2χt par direction et 4χt au carré de distance radiale en deux dimensions. Confondre ces deux mesures crée un facteur deux. Le même raisonnement donne 6χt en trois dimensions.</p>
<p>La carte est limitée à ±5σ dans les deux directions. Son énergie intégrée diffère très légèrement de Q à cause de la queue exclue et de la quadrature. Une fenêtre fixe trop petite pourrait donner l’impression erronée d’une énergie qui disparaît.</p>''')
exercise('diffusion_2d','Doubler une largeur et conserver l’énergie','Sup → Spé','<p>Si la largeur σ d’une tache 2D double sans changer Q, que devient son maximum ?</p>','<p>Le maximum est Q/(2πρceσ²) : il est divisé par <b>quatre</b>. Les aires caractéristiques sont multipliées par quatre. L’énergie totale reste Q, même si le pic est beaucoup plus bas.</p>')
exercise('diffusion_2d','Variance radiale d’une tache','Spé','<p>σ₀=10 mm, χ=2 mm²/s et t=120 s. Calculer σ et ⟨r²⟩.</p>','<p>σ²=100+2×2×120=<b>580 mm²</b>, donc σ≈<b>24,08 mm</b>. La moyenne radiale vaut <b>1 160 mm²</b>. Le carré de largeur par direction et la moyenne du rayon au carré sont distincts.</p>')
exercise('diffusion_2d','Vérifier la normalisation de la gaussienne','Spé','<p>Intégrer l’élévation gaussienne sur le plan en coordonnées polaires et vérifier son énergie.</p>','<p>Avec r²=x²+y² et dxdy=rdrdθ, l’intégrale de ρceΔT vaut Q/(2πσ²)×2π∫₀∞r exp(−r²/(2σ²))dr. Poser u=r²/(2σ²), donc rdr=σ²du. L’intégrale vaut <b>Q∫₀∞e⁻ᵘdu=Q</b>.</p>')
guide('diffusion_2d','Relier une carte de température à un bilan énergétique et à des variances définies.',
 ['σ est une largeur par direction, pas un rayon net de la tache.', 'ρce est en J/(m²·K), Q en J.', 'La carte utilise de vraies coordonnées x,y en mm.'],
 ['Plaque infinie, aucune perte extérieure.', 'Profil initial gaussien de largeur non nulle.'],
 ['Gaussienne, intégrale polaire et changement de variable.', 'Conservation et somme des variances.'],
 'Relier étalement et diminution du maximum.', 'Vérifier la normalisation et le bilan 2D.', 'Noyau de chaleur et convolution de profils.',
 ['Lire la carte et l’énergie intégrée.', 'Multiplier le temps par quatre et comparer les largeurs.', 'Réduire la largeur initiale puis retrouver sa disparition progressive.'],
 'Utiliser 2χt par direction et 4χt pour la diffusion radiale en 2D.')

lesson('marche_aleatoire','La position finale est une binomiale transformée','Sup → Spé','''
<p>ε est la longueur d’un saut et τ sa durée. À chaque pas indépendant, le saut vaut +ε avec probabilité p et −ε avec probabilité 1−p. K compte les sauts positifs sur N pas.</p>
<p>K suit la loi binomiale : P(K=k)=C(N,k)pᵏ(1−p)ᴺ⁻ᵏ. La position vaut <b>X=(2K−N)ε</b>. Sa moyenne est N(2p−1)ε et sa variance 4Np(1−p)ε².</p>
<p>Après N pas, seuls les indices de même parité que N sont accessibles. Leur espacement est 2ε. Une gaussienne est une densité ; multiplier par 2ε permet de la comparer à une probabilité par site. Le laboratoire conserve cette distinction.</p>''')
lesson('marche_aleatoire','Retrouver Fick et distinguer dérive de diffusion','Spé','''
<p>t=Nτ est le temps. La dérive moyenne a vitesse u=(2p−1)ε/τ. Identifier la variance centrée à 2Dt donne <b>D=2p(1−p)ε²/τ</b>.</p>
<p>Sans biais p=1/2, D=ε²/(2τ). La relation P(x,t+τ)=[P(x−ε,t)+P(x+ε,t)]/2 et des développements limités retrouvent ∂P/∂t=D∂²P/∂x².</p>
<p>Avec biais, le centre se déplace et la variance se calcule autour de ce centre. La limite diffusive centrée donne une équation d’advection–diffusion. Une moyenne sur 256 marches reste bruitée ; la binomiale et ses moments exacts fournissent les références indépendantes.</p>''')
exercise('marche_aleatoire','Le coefficient du recueil','Sup → Spé','<p>Une marche sans biais saute de 1 µm toutes les 1 ms. Calculer D et la variance après 100 pas.</p>','<p>D=ε²/(2τ)=10⁻¹²/(2×10⁻³)=<b>5×10⁻¹⁰ m²/s</b>. Après t=0,1 s, la variance 2Dt vaut <b>100 µm²</b> ; l’écart-type est 10 µm.</p>')
exercise('marche_aleatoire','Un biais crée deux phénomènes','Sup → Spé','<p>Avec p=0,7, ε=1 µm, τ=1 ms et N=100, calculer moyenne et variance.</p>','<p>La moyenne est N(2p−1)ε=<b>40 µm</b>. La variance est 4Np(1−p)ε²=<b>84 µm²</b>. La dérive vaut 400 µm/s et D=4,2×10⁻¹⁰ m²/s. La variance se calcule autour de 40 µm, pas autour de l’origine.</p>')
exercise('marche_aleatoire','Le facteur de parité dans la gaussienne','Spé','<p>Pourquoi une densité gaussienne multipliée par ε sous-estime-t-elle la probabilité d’un site accessible après N sauts ?</p>','<p>Les sites accessibles sont séparés par <b>2ε</b>, car le nombre de sauts positifs change la position de 2ε. La probabilité approchée est donc densité×2ε. Employer ε la diviserait par deux et donnerait une somme approchée proche de 1/2.</p>')
guide('marche_aleatoire','Déduire la diffusion de sauts probabilistes en gardant une référence exacte.',
 ['ε est en µm puis converti en m ; τ est en ms puis en s.', 'p est une probabilité vers +x ; N le nombre de pas.', 'La variance est centrée, contrairement au déplacement quadratique non centré en présence de biais.'],
 ['Sauts indépendants et paramètres constants.', 'Binomiale exacte ; gaussienne seulement approximative.'],
 ['Moments d’une binomiale et changement affine.', 'Développements limités et limite diffusive.'],
 'Calculer moyenne et variance de X.', 'Retrouver D et l’équation de Fick.', 'Théorème central limite et advection–diffusion.',
 ['Choisir peu de pas et observer le caractère discret.', 'Augmenter N : comparer binomiale et gaussienne.', 'Introduire p=0,7 et distinguer déplacement du centre et étalement.'],
 'Relier variance et coefficient diffusif en tenant compte de la parité du réseau.')

lesson('brownien_langevin','Stokes–Einstein fixe l’échelle de diffusion','Spé','''
<p>a est le rayon d’une sphère, η la viscosité dynamique et T la température absolue. kB=1,380649×10⁻²³ J/K est la constante de Boltzmann ; v est une composante de vitesse. Le coefficient de frottement vaut α=6πηa. La masse m vient du rayon et de la masse volumique.</p>
<p>Le modèle de Langevin équilibre frottement et fluctuations thermiques. Avec l’équilibre de vitesse ⟨v²⟩=kBT/m par direction, il donne <b>D=kBT/α=kBT/(6πηa)</b> et le temps de relaxation de vitesse τᵥ=m/α.</p>
<p>Une particule plus grande ou un fluide plus visqueux diffuse moins vite. Le coefficient D est en m²/s ; τᵥ est en secondes. Le laboratoire distingue cette relaxation très rapide d’une observation brownienne sur des fractions de seconde.</p>''')
lesson('brownien_langevin','Le carré du déplacement passe de t² à t','Spé · Prolongement','''
<p>x(0)=0 et la vitesse initiale est déjà à l’équilibre thermique. La corrélation des vitesses vaut ⟨v(t)v(s)⟩=(kBT/m)e⁻|ᵗ⁻ˢ|/τᵥ.</p>
<p>Intégrer cette corrélation sur les deux temps donne <b>⟨x²(t)⟩=2D[t−τᵥ(1−e⁻ᵗ/τᵥ)]</b>. Pour t≪τᵥ, le développement limité retrouve (kBT/m)t², mouvement balistique. Pour t≫τᵥ, on retrouve 2Dt.</p>
<p>Les trajectoires utilisent les transitions gaussiennes exactes conjointes de vitesse et déplacement. Leur bruit est corrélé ; ce calcul reste valable si le pas dépasse τᵥ. Une vitesse initialement nulle donnerait une autre évolution aux temps courts. Les deux coordonnées du dessin ont chacune la variance 1D affichée.</p>''')
exercise('brownien_langevin','Diffusion d’une particule dans l’eau','Spé','<p>Pour a=500 nm, η=1 mPa·s et T=300 K, calculer D. On prend kB=1,380649×10⁻²³ J/K.</p>','<p>α=6π×10⁻³×5×10⁻⁷≈9,425×10⁻⁹ kg/s. Donc D≈<b>4,395×10⁻¹³ m²/s</b>. À long temps, après 0,1 s, le déplacement quadratique par direction vaut environ <b>0,0879 µm²</b>.</p>')
exercise('brownien_langevin','Contrôler les deux limites','Spé','<p>Développer la formule du MSD pour t≪τᵥ et donner un équivalent pour t≫τᵥ.</p>','<p>1−e⁻ᵗ/τᵥ=t/τᵥ−t²/(2τᵥ²)+… . La différence entre crochets vaut t²/(2τᵥ)+… ; le MSD vaut <b>(D/τᵥ)t²=(kBT/m)t²</b>. À long temps, la correction constante −2Dτᵥ devient négligeable devant <b>2Dt</b>.</p>')
exercise('brownien_langevin','Une mesure 2D ne donne pas le MSD 1D','Sup → Spé','<p>Dans une image plane, on mesure la moyenne de x²+y². Quel coefficient relie cette mesure au temps dans le régime diffusif ?</p>','<p>Chaque variance vaut 2Dt, donc <b>⟨x²+y²⟩=4Dt</b>. Le coefficient de diffusion est le même dans les deux directions. Employer la formule 2Dt sur la distance plane ferait surestimer D d’un facteur deux.</p>')
guide('brownien_langevin','Mettre le TP de Langevin en relation avec les échelles réelles et la moyenne statistique.',
 ['a est un rayon, η une viscosité ; les conversions nm et mPa·s sont explicites.', 'm est la masse en kg ; kB est la constante de Boltzmann en J/K ; T est la température en K.', 'τᵥ=m/(6πηa) est la relaxation de vitesse en s ; t est la durée observée en s.', 'Le MSD affiché est par direction ; les positions du plan sont réellement simulées.'],
 ['Frottement de Stokes et bain thermique homogène.', 'Vitesse initiale stationnaire et absence de force extérieure.'],
 ['Équipartition, dimensions et corrélation de vitesse.', 'Développements limités et estimation statistique.'],
 'Identifier rayon, viscosité et température dans D.', 'Relier Langevin au passage balistique–diffusif.', 'Processus d’Ornstein–Uhlenbeck et transitions corrélées.',
 ['Observer t≈τᵥ et comparer à 2Dt.', 'Choisir le temps court puis lire le comportement en t².', 'Passer aux secondes et augmenter la viscosité : comparer les amplitudes de diffusion.'],
 'Définir l’état initial et la dimension du déplacement avant d’extraire D.')

lesson('absorption_neutrons','Une source ponctuelle fixe une normalisation','Spé','''
<p>n(r) est la densité en m⁻³ ; D le coefficient diffusif, τ la durée de vie et Q le débit de source en s⁻¹. L=√Dτ est une longueur.</p>
<p>Hors de la source, le bilan permanent donne DΔn−n/τ=0. En symétrie sphérique, u=rn satisfait u″=u/L². La décroissance à l’infini impose n=Ae⁻ʳ/ᴸ/r.</p>
<p>Le courant est j=−Dn′. La limite du débit 4πr²j lorsque r→0 doit être Q ; elle impose <b>n=Qe⁻ʳ/ᴸ/(4πDr)</b>. La densité en 0 est singulière ; le laboratoire exclut ce point au lieu d’inventer une valeur finie.</p>''')
lesson('absorption_neutrons','Suivre le débit et compter l’absorption','Spé','''
<p>Φ(r)=4πr²j est le débit traversant une sphère de rayon r. La formule de densité donne <b>Φ=Q(1+r/L)e⁻ʳ/ᴸ</b>.</p>
<p>La différence Q−Φ est le nombre absorbé par seconde à l’intérieur. La somme source=absorption+débit sortant vérifie la conservation localement et globalement. La dérivée d’absorption par rayon vaut Qr e⁻ʳ/ᴸ/L².</p>
<p>L’intégrale de n sur tout le volume vaut Qτ : une injection Q avec durée de vie moyenne τ maintient ce nombre de particules. Le flux surfacique j, le débit Φ et la densité n ne portent pas les mêmes unités.</p>''')
exercise('absorption_neutrons','Dimension et longueur d’absorption','Sup → Spé','<p>D=20 cm²/s et τ=0,2 s. Calculer L. Vérifier l’unité de Q/(Dr).</p>','<p>D=0,002 m²/s. L=√(0,002×0,2)=<b>0,02 m=2 cm</b>. Q/(Dr) a unité s⁻¹/[(m²/s)m]=<b>m⁻³</b>, celle d’une densité.</p>')
exercise('absorption_neutrons','Combien sont absorbés avant L ?','Spé','<p>À r=L, déterminer la fraction du débit source absorbée à l’intérieur.</p>','<p>Le débit restant est Q(1+1)e⁻¹=2Q/e. La fraction absorbée vaut <b>1−2/e≈26,42 %</b>. L n’est donc pas le rayon où la plupart des neutrons ont déjà été absorbés.</p>')
exercise('absorption_neutrons','Nombre présent à l’équilibre','Spé','<p>Intégrer n sur le volume pour retrouver Qτ.</p>','<p>4πr²n=Qr e⁻ʳ/ᴸ/D. Son intégrale vaut (Q/D)L²∫₀∞u e⁻ᵘdu=<b>QL²/D=Qτ</b>. La source peut être ponctuelle tout en produisant un nombre intégré fini.</p>')
guide('absorption_neutrons','Prolonger l’exercice 3 en contrôlant la source par un bilan, pas seulement par une forme exponentielle.',
 ['Q est un débit, τ une durée de vie, D une diffusivité.', 'L=√Dτ est une longueur caractéristique.', 'n, j et Φ ont respectivement les unités m⁻³, m⁻²·s⁻¹ et s⁻¹.'],
 ['Milieu homogène infini avec absorption linéaire.', 'La source idéale est singulière et r=0 n’est pas tracé.'],
 ['Laplacien radial et changement u=rn.', 'Normalisation par flux et intégrale volumique.'],
 'Vérifier les dimensions et lire l’atténuation.', 'Résoudre la densité et le bilan d’absorption.', 'Diffusion multigroupe et réactions en milieu fini.',
 ['Lire L et le nombre total Qτ.', 'Comparer débit traversant et absorption intérieure à r=L.', 'Modifier τ puis Q : distinguer longueur et simple changement d’amplitude.'],
 'Fixer la constante par la source et vérifier le débit à chaque rayon.')

lesson('diffusion_electrolyte','Deux ions doivent diffuser ensemble à courant nul','Spé · Prolongement','''
<p>D₊ et D₋ sont les diffusivités d’un cation et d’un anion monovalents. n est leur densité commune, E le champ et e la charge élémentaire positive. La température T est absolue ; kB est la constante de Boltzmann, en J/K. Γ₊ et Γ₋ sont les flux particulaires en m⁻²·s⁻¹ ; le signe prime indique une dérivée selon la position x.</p>
<p>Diffusion et migration donnent Γ₊=−D₊n′+D₊enE/(kBT), Γ₋=−D₋n′−D₋enE/(kBT). Le courant électrique nul impose Γ₊=Γ₋.</p>
<p>On obtient <b>E=(kBT/e)(D₊−D₋)n′/[(D₊+D₋)n]</b>. Les deux flux deviennent −Damb n′, avec <b>Damb=2D₊D₋/(D₊+D₋)</b>. Un champ compense donc la différence de diffusivité. Si les deux coefficients sont égaux, le champ disparaît.</p>''')
lesson('diffusion_electrolyte','Le signe du potentiel découle de E=−V′','Spé','''
<p>V est le potentiel et c la concentration en mol/m³. N_A=6,02214076×10²³ mol⁻¹ est la constante d’Avogadro ; n=N_Ac. Comme le quotient n′/n vaut c′/c, la concentration molaire convient pour calculer le champ.</p>
<p>Intégrer <b>V′=−E</b> donne Vdroite−Vgauche=(kBT/e)(D₋−D₊)ln(cDroite/cGauche)/(D₊+D₋). Le signe dépend des deux diffusivités et du sens du gradient ; il ne doit pas être deviné.</p>
<p>cG et cD sont les concentrations initiales à gauche et à droite ; t est le temps depuis leur mise en contact. Le profil est c=(cG+cD)/2+(cD−cG)erf[x/(2√Damb t)]/2. Le champ de jonction est local et généralement non uniforme. La quasi-neutralité concerne le volume ; les fines couches de charge aux interfaces ne sont pas résolues.</p>''')
exercise('diffusion_electrolyte','Diffusivités égales','Sup → Spé','<p>Que donnent Damb, E et la jonction si D₊=D₋=D ?</p>','<p><b>Damb=D</b>, E=0 et la différence de potentiel est nulle. Les deux ions ont déjà le même flux diffusif −Dn′ ; aucune migration ne doit les rééquilibrer.</p>')
exercise('diffusion_electrolyte','Coefficient et signe d’une jonction','Spé','<p>D₊=1,3×10⁻⁹ et D₋=2×10⁻⁹ m²/s, T=300 K, cD/cG=5. Déterminer Damb et le signe de Vdroite−Vgauche.</p>','<p>Damb=2×1,3×2/(1,3+2)×10⁻⁹≈<b>1,576×10⁻⁹ m²/s</b>. Comme D₋−D₊&gt;0 et ln5&gt;0, la différence de potentiel est positive. Avec kBT/e≈25,85 mV, elle vaut environ <b>8,83 mV</b>.</p>')
exercise('diffusion_electrolyte','Vérifier le flux commun','Spé','<p>Substituer le champ dans Γ₊ pour retrouver la diffusion ambipolaire.</p>','<p>Γ₊=−D₊n′+D₊(D₊−D₋)n′/(D₊+D₋). Réunir les termes donne −D₊[(D₊+D₋)−(D₊−D₋)]n′/(D₊+D₋)=<b>−2D₊D₋n′/(D₊+D₋)</b>. Le même calcul pour l’anion donne exactement ce flux.</p>')
guide('diffusion_electrolyte','Relier diffusion particulaire, courant électrique et champ créé par une jonction.',
 ['c est la concentration molaire ; N_A est la constante d’Avogadro en mol⁻¹. n=N_Ac compte les ions par m³.', 'D₊,D₋ sont les diffusivités, converties en m²/s.', 'e est la charge élémentaire positive ; Γ₊,Γ₋ sont les flux particulaires en m⁻²·s⁻¹. E=−V′ et courant=e(Γ₊−Γ₋) fixent les signes.'],
 ['Ions monovalents dilués, volume quasi neutre.', 'Température uniforme et courant extérieur nul.'],
 ['Flux de diffusion et migration.', 'Élimination du champ, logarithme et solution de Fick.'],
 'Distinguer flux particulaire et courant électrique.', 'Calculer le champ et le coefficient ambipolaire.', 'Nernst–Planck, couches de Debye et potentiel de jonction.',
 ['Comparer les flux des ions et Fick ambipolaire.', 'Égaliser les diffusivités et vérifier le champ nul.', 'Inverser les concentrations et prévoir le signe du potentiel.'],
 'Établir le signe par la convention de potentiel et justifier le flux commun.')

lesson('entropie_diffusion','Une redistribution adiabatique conserve l’énergie','Sup → Spé','''
<p>N est le nombre de cellules. C est leur capacité thermique identique, G la conductance entre voisines et Tᵢ la température absolue de la cellule i. Les extrémités sont isolées.</p>
<p>Chaque bilan vaut C Tᵢ′=GΣvoisins(Tvoisin−Tᵢ). En sommant, tous les échanges internes s’annulent : <b>U=CΣTᵢ est constant</b>. À l’équilibre les températures deviennent égales à leur moyenne initiale.</p>
<p>La matrice de ce système est symétrique et négative ; son mode uniforme est conservé, ses autres modes décroissent. Le laboratoire calcule cette évolution exactement par diagonalisation. « Adiabatique » ne signifie donc pas que chaque cellule garde sa température : c’est l’ensemble qui ne reçoit pas de transfert externe.</p>''')
lesson('entropie_diffusion','La positivité apparaît à chaque interface','Spé','''
<p>Une interface entre Ti et Tj transmet Φ=G(Ti−Tj). Sa contribution à la variation d’entropie totale vaut Φ(1/Tj−1/Ti).</p>
<p>On obtient <b>G(Ti−Tj)²/(TiTj)≥0</b>, car les températures absolues et G sont positives. La somme de ces termes est la production irréversible ; elle s’annule seulement quand tous les voisins ont même température.</p>
<p>Avec des capacités constantes, le gain est ΔS=CΣln[Tᵢ(t)/Tᵢ(0)]. À l’équilibre, il atteint C[Nln(Tmoyenne)−ΣlnTᵢ(0)]≥0. L’énergie constante et l’entropie croissante ne sont pas contradictoires : elles décrivent deux bilans distincts.</p>''')
exercise('entropie_diffusion','Deux corps isolés','Sup → Spé','<p>Deux capacités égales C=1 000 J/K sont initialement à 353,15 K et 293,15 K. Donner la température finale et l’entropie produite.</p>','<p>La température finale vaut <b>323,15 K, soit 50°C</b>. Le gain est C ln[323,15²/(353,15×293,15)]≈<b>8,66 J/K</b>, positif. Utiliser les températures en °C dans le logarithme serait incorrect.</p>')
exercise('entropie_diffusion','Production instantanée d’une interface','Spé','<p>Avec G=10 W/K, Ti=350 K et Tj=300 K, calculer la puissance et la production d’entropie.</p>','<p>La puissance vers le froid est 10×50=<b>500 W</b>. La production vaut G×50²/(350×300)≈<b>0,2381 W/K</b>. Le flux peut être signé mais la production reste positive.</p>')
exercise('entropie_diffusion','Entropie nulle et état initial uniforme','Sup → Spé','<p>Que prédit le système si toutes les cellules commencent à la même température ? Vérifier le bilan local et le gain final.</p>','<p>Toutes les différences entre voisines sont nulles : chaque dérivée Tᵢ′ est nulle. La production instantanée et le gain total valent <b>zéro</b>. L’uniformité est le mode conservé ; aucune redistribution ni irréversibilité n’est créée.</p>')
guide('entropie_diffusion','Vérifier ensemble le premier et le second principe dans un système isolé diffusif.',
 ['N est le nombre de cellules ; C est leur capacité en J/K et G la conductance entre voisines en W/K.', 'T en kelvins entre dans les rapports et les inverses.', 'ΔS est en J/K ; la production instantanée en W/K.'],
 ['Cellules identiques, échanges entre voisines seulement.', 'Extrémités isolées, capacités et conductances constantes.'],
 ['Bilan local, somme des échanges et modes propres.', 'Variation logarithmique d’entropie et somme de termes positifs.'],
 'Calculer la température finale par conservation.', 'Démontrer la positivité et lire sa décroissance.', 'Formes quadratiques, principe du maximum et thermodynamique irréversible.',
 ['Préparer deux moitiés de températures différentes.', 'Comparer énergie constante, entropie croissante et production décroissante.', 'Choisir l’état uniforme : vérifier les trois bilans nuls.'],
 'Distinguer conservation d’énergie et production d’entropie avec des températures absolues.')
