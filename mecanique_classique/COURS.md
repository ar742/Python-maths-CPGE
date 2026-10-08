# Mécanique & Mouvements — 48 leçons

Recueil de A. R., P1–P3. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.

## 01. Force centrale : du moment cinétique aux trois lois de Kepler

Sup → Spé · Laboratoire `orbite_kepler`

Choisir le système : une planète de masse m, assez petite pour que l’étoile de masse M soit immobile. Le référentiel lié à l’étoile est supposé galiléen. La force est **F=−GMm r/r³**, où r désigne le vecteur étoile–planète et r sa norme. L’origine de l’énergie potentielle est prise à l’infini.

Le moment de cette force par rapport à l’étoile est nul. Le théorème du moment cinétique donne L=m r×v constant. Le mouvement reste dans le plan perpendiculaire à L, et h=L/m=r²θ̇ est constant. La vitesse aréolaire, c’est-à-dire l’aire balayée par unité de temps, vaut h/2.

ε=v²/2−GM/r ; h=r²θ̇ ; dA/dt=h/2.

Pour obtenir la trajectoire, poser u=1/r. L’équation de Binet donne u″+u=GM/h², les dérivées étant prises par rapport à θ. La solution est une conique, r=p/(1+e cosθ), avec p=h²/(GM). Le choix de θ=0 au péricentre fixe l’orientation de la conique.

Pour une ellipse : p=a(1−e²), rp=a(1−e), ra=a(1+e), ε=−GM/(2a).

L’aire de l’ellipse vaut πab=πa²√(1−e²). En divisant par h/2, on obtient T²=4π²a³/(GM). Cette démarche relie explicitement le théorème du moment cinétique, l’énergie et les trois lois de Kepler. Une planète sur une ellipse excentrique ne tourne pas à vitesse uniforme.

## 02. Passer de la trajectoire géométrique à la position au cours du temps

Spé · Prolongement · Laboratoire `orbite_kepler`

Échantillonner uniformément l’angle polaire ferait avancer la planète à une mauvaise vitesse. Pour calculer une position à l’instant t, on utilise un autre paramètre, **l’anomalie excentrique E**, qui repère un point de l’ellipse à partir de son cercle auxiliaire.

x=a(cos E−e), y=a√(1−e²) sin E ; r=a(1−e cos E).

Le temps est relié à E par l’équation de Kepler : E−e sin E=nt, avec n=2π/T. Pour e<1, sa dérivée 1−e cos E est strictement positive : il existe une unique solution pour chaque temps d’une période. La méthode de Newton consiste à corriger E par −(E−e sin E−nt)/(1−e cos E). Le laboratoire résout cette équation puis dérive les coordonnées pour calculer v.

A(t)=½a²√(1−e²)(E−e sin E)=½ht.

Deux vérifications sont complémentaires : l’énergie et h doivent rester constants ; les aires balayées pendant T/12 doivent être égales. Une belle ellipse seule ne vérifie aucune de ces propriétés temporelles. Dans les unités de l’atelier, a=1 UA, M=1 masse solaire donne T=1 an et, à e=0, v=2π UA/an.

## 03. Système fermé, centre de masse et particule fictive

Sup → Spé · Laboratoire `deux_corps`

Le système est constitué de deux masses m₁ et m₂ qui n’échangent avec l’extérieur ni force ni matière. Les forces gravitationnelles internes sont opposées. Le théorème de la quantité de mouvement impose un mouvement rectiligne uniforme du centre de masse G. Le référentiel de G est donc galiléen.

Poser M=m₁+m₂, r=r₂−r₁ et μr=m₁m₂/M, la **masse réduite**. Dans le référentiel de G, la relation m₁r₁+m₂r₂=0 permet de retrouver les deux positions à partir de la seule séparation r :

r₁=−(m₂/M)r ; r₂=(m₁/M)r.

Soustraire les deux équations du mouvement donne r̈=−GM r/r³. On peut aussi écrire μr r̈=−Gm₁m₂ r/r³ : la particule fictive de masse μr décrit un mouvement central. Ne pas confondre μr, qui est une masse, avec GM, qui est un paramètre gravitationnel de dimension longueur³/temps².

T²=4π²a³/[G(m₁+m₂)] ; a₁=(m₂/M)a ; a₂=(m₁/M)a.

Le demi-grand axe a concerne l’orbite relative, donc a=a₁+a₂. Les deux étoiles ont la même période ; la plus massive décrit la plus petite ellipse autour de G.

## 04. Énergie et moment cinétique : les deux décompositions de König

Spé · Laboratoire `deux_corps`

Dans un référentiel galiléen quelconque, écrire vi=VG+vi*. La condition ∑mivi*=0 annule le terme croisé dans ∑mi vi²/2. On sépare ainsi le mouvement d’ensemble et le mouvement autour du centre de masse.

Ec=½M VG²+½μr vrelative².

Le premier terme décrit la translation de G ; le second décrit le mouvement relatif. L’énergie potentielle mutuelle est −Gm₁m₂/r, comptée **une seule fois** pour la paire. Dans le référentiel de G, l’énergie mécanique vaut donc E*=½μr ṙ²−Gm₁m₂/r.

Ellipse relative : E*=−Gm₁m₂/(2a) ; L*=μr r×ṙ.

Pour le moment cinétique en un point fixe O, Lᵒ=OG×M VG+L*. Ce résultat se démontre par le même remplacement ri=OG+ri*. Par exemple, si m₁=m₂=m, chaque étoile est à distance r/2 de G : Ec*=2×½m(vrelative/2)²=½(m/2)vrelative². La masse réduite vaut bien m/2.

## 05. Éliminer l’angle pour lire le mouvement radial

Spé · Laboratoire `potentiel_effectif`

Une force centrale entraîne la conservation h=r²θ̇. Dans l’énergie spécifique, la vitesse en coordonnées polaires vérifie v²=ṙ²+r²θ̇². En remplaçant θ̇ par h/r², on obtient une énergie qui ne dépend plus que de r et de ṙ.

ε=½ṙ²+Ueff(r) ; Ueff(r)=h²/(2r²)−GM/r.

Le terme h²/(2r²) traduit l’énergie du mouvement angulaire. Ce n’est pas une énergie potentielle gravitationnelle supplémentaire. Pour h≠0, il tend vers +∞ quand r tend vers zéro : le moment cinétique empêche d’atteindre le centre dans ce modèle ponctuel.

Le domaine accessible satisfait Ueff≤ε. Aux rayons où Ueff=ε, ṙ s’annule : le mouvement radial change de sens, sauf dans le cas de l’orbite circulaire. Si ε<0, il existe deux rayons extrêmes ; si ε≥0, aucun rayon maximal ne borne la trajectoire.

rc=h²/(GM) ; Ueff(rc)=−(GM)²/(2h²) ; Ueff″(rc)=(GM)⁴/h⁶>0.

Le minimum définit une orbite circulaire stable. Le signe de la dérivée seconde renseigne sur la stabilité radiale, mais ne doit pas être interprété comme un amortissement : sans dissipation, les perturbations oscillent au lieu de disparaître.

## 06. Classer un lancement et étudier les petites oscillations radiales

Spé · Prolongement · Laboratoire `potentiel_effectif`

À r₀=1 et GM=1, lancer tangentiellement avec vitesse η. On a h=η, ε=(η²−2)/2 et e=|η²−1|. Le seuil de l’échappement est η=√2. Le cercle est obtenu pour η=1 ; un lancement plus lent commence à l’apocentre, un lancement plus rapide commence au péricentre.

Pour un mouvement presque circulaire, écrire r=rc+ρ avec |ρ|≪rc. Au premier ordre, l’équation radiale r̈=−Ueff′(r) donne un oscillateur harmonique :

ρ̈+ωr²ρ≈0 ; ωr²=Ueff″(rc)=GM/rc³.

La fréquence angulaire de l’orbite circulaire est également ωθ=√(GM/rc³). Cette égalité explique, au voisinage du cercle, pourquoi une révolution angulaire correspond à une oscillation radiale : l’ellipse se referme. Pour un autre potentiel central, ces deux fréquences ne sont généralement plus égales et l’orbite peut précesser.

Le graphique aide à lire les racines, mais la condition d’échappement se démontre par l’énergie : à l’infini Ueff tend vers zéro. Le cas ε=0 est une parabole, pas un mouvement rectiligne uniforme.

## 07. Deux changements de vitesse déterminés par l’énergie

Spé · Laboratoire `transfert_hohmann`

Un transfert de Hohmann relie deux orbites circulaires concentriques, coplanaires et de même sens. Le véhicule quitte la première orbite par une impulsion tangentielle, parcourt une demi-ellipse puis reçoit une deuxième impulsion tangentielle. Les deux cercles sont tangents à l’ellipse.

a=(r₁+r₂)/2 ; e=|r₂−r₁|/(r₁+r₂) ; vt(r)=√[GM(2/r−1/a)].

La vitesse circulaire au rayon r vaut vc(r)=√(GM/r). Au départ, Δv₁=vt(r₁)−vc(r₁). À l’arrivée, Δv₂=vc(r₂)−vt(r₂). Lors d’un transfert sortant, les deux impulsions accélèrent ; lors d’un transfert entrant, elles freinent. La quantité de carburant dépend du coût |Δv₁|+|Δv₂|, toujours positif.

τ=π√(a³/GM) ; Δvtotal=|Δv₁|+|Δv₂|.

Exemple dans le scénario Terre : r₁=7 000 km et r₂=42 000 km donnent un demi-grand axe de 24 500 km et une durée d’environ 5,3 h. Les deux impulsions sont d’environ 2,33 et 1,43 km/s. La seconde est nécessaire : sans elle, le véhicule redescend le long de l’ellipse.

## 08. Un transfert interplanétaire exige aussi une condition de rendez-vous

Spé · Prolongement · Laboratoire `transfert_hohmann`

Une trajectoire qui atteint le rayon orbital de Mars ne garantit pas qu’elle atteigne Mars. Dans le modèle circulaire, la planète cible tourne pendant le trajet. Si l’ellipse de transfert couvre un angle π et la planète cible tourne à la vitesse n₂, l’angle d’avance initial nécessaire est :

φ₀=π−n₂τ modulo 2π ; n₂=√(GM/r₂³).

Pour r₁=1 UA et r₂=1,524 UA autour du Soleil, la durée est voisine de 259 jours et la planète cible doit se trouver environ 44° en avance au départ. Le laboratoire représente l’ellipse du véhicule, pas les mouvements synchronisés des deux planètes.

Les variations de vitesse sont calculées dans le référentiel de l’astre central. Le coût solaire d’une impulsion à 1 UA ne se confond pas avec le coût d’un départ depuis la surface terrestre : il faut prendre en compte les puits gravitationnels des planètes et les orbites de départ ou de capture.

Ce calcul forme à un enchaînement courant : géométrie des coniques, bilan d’énergie, période de Kepler, puis condition temporelle. Il illustre une famille de transferts à deux impulsions ; des transferts bi-elliptiques ou propulsés continûment demandent une comparaison supplémentaire.

Références de contexte : [NASA : Hohmann Transfer Orbit](https://science.nasa.gov/resource/hohmann-transfer-orbit/) et [NASA GSFC : Flight to Mars, Calculations](https://pwg.gsfc.nasa.gov/stargaze/Smars2.htm).

## 09. Une trajectoire hyperbolique à énergie positive

Spé · Laboratoire `diffusion_gravitationnelle`

Dans le référentiel de l’astre, une sonde arrive avec vitesse v∞. La droite de sa trajectoire asymptotique se trouve à distance b de l’astre : b est le **paramètre d’impact**. L’énergie spécifique ε et le moment cinétique spécifique h sont fixés par ces conditions lointaines.

ε=v∞²/2 ; h=bv∞ ; e=√[1+b²v∞⁴/(GM)²] >1.

La conique r=p/(1+e cosθ), p=h²/(GM), tend vers l’infini lorsque 1+e cosθ=0. Les deux asymptotes donnent la déviation δ entre les directions entrante et sortante.

δ=2arcsin(1/e)=2arctan[GM/(bv∞²)] ; rp=p/(1+e).

À b fixé, augmenter v∞ diminue la déviation : la sonde passe trop vite pour être fortement déviée. À v∞ fixé, réduire b augmente la déviation et diminue rp. Le modèle ponctuel n’empêche pas de passer à l’intérieur d’un astre réel : il faut donc contrôler séparément que rp reste supérieur au rayon matériel si l’on donne des unités physiques.

Sans moteur ni atmosphère, l’énergie mécanique est conservée et la vitesse lointaine sortante a la même norme v∞ que la vitesse lointaine entrante. Une accélération transitoire près du centre ne signifie pas un gain net d’énergie dans ce référentiel.

## 10. Assistance gravitationnelle : changer de référentiel pour comprendre le gain

Spé · Prolongement · Laboratoire `diffusion_gravitationnelle`

Noter uin et uout les vitesses relatives à la planète à grande distance. Elles ont la même norme v∞, mais des directions différentes. Si la planète se déplace à vitesse V dans un autre référentiel galiléen, les vitesses de la sonde deviennent vin=uin+V et vout=uout+V.

ΔEc/m=½(|uout+V|²−|uin+V|²)=V·(uout−uin).

Le produit scalaire peut être positif ou négatif. La même déviation peut donc faire gagner ou perdre de l’énergie selon le côté du passage et le sens du mouvement de la planète. Si V=0, le gain est nul : une planète immobile ne peut pas produire un gain net d’énergie cinétique lointaine.

Dans le modèle du laboratoire, la vitesse V de l’astre est prescrite et sa variation est négligée. Pour le système fermé planète–sonde, la variation de l’énergie de la sonde est compensée par celle de la planète ; le rapport des masses rend la modification de l’orbite de la planète très faible.

La méthode attendue est de ne pas mélanger les référentiels : déterminer d’abord la conique dans le référentiel de la planète, puis effectuer une composition des vitesses. [ESA : What are gravity assists?](https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists)

## 11. La marée est une différence de forces, pas la force gravitationnelle totale

Sup → Spé · Laboratoire `marees`

Un corps et son centre de masse subissent ensemble l’attraction d’un astre extérieur. Ce mouvement commun ne les déforme pas. La déformation est liée à la **différence** entre le champ gravitationnel en un point du corps et le champ au centre.

Placer l’astre à distance D sur l’axe positif x. Pour un point d’abscisse x par rapport au centre, la différence d’accélération radiale vaut exactement :

Δax=GM[(D−x)⁻²−D⁻²] ≈ (2GM/D³)x si |x|≪D.

La face proche, x>0, est davantage accélérée vers l’astre ; la face éloignée, x<0, l’est moins que le centre. Après soustraction du mouvement du centre, les deux faces s’éloignent de lui. On obtient ainsi un étirement suivant l’axe centre–astre.

Dans le plan transverse : Δay≈−(GM/D³)y et Δaz≈−(GM/D³)z.

Le champ linéaire possède donc les trois coefficients (2,−1,−1)GM/D³. Le signe négatif transverse correspond à une compression. Leur somme est nulle, en accord avec la divergence nulle du champ gravitationnel dans une région qui ne contient pas la masse de l’astre.

## 12. Développement limité, ordre de grandeur et portée du modèle

Spé · Prolongement · Laboratoire `marees`

La petite quantité du développement limité n’est pas la masse de l’astre : c’est le rapport R/D entre la taille du corps et la distance à l’astre. Le premier terme omis du champ radial est proportionnel à x²/D⁴. Pour un corps de rayon R, l’erreur relative du premier ordre est donc d’ordre R/D.

Accélération de marée ≈2GMR/D³ ; gravité propre en surface =Gm/R².

Leur rapport est 2(M/m)(R/D)³. Il permet de repérer les situations où la différence d’attraction devient comparable à la cohésion gravitationnelle du corps. Cette comparaison fournit une échelle de distance, D/R≈(2M/m)¹ᐟ³, mais **pas une limite exacte de dislocation**.

Une limite de Roche pour un fluide doit inclure la rotation orbitale et le modèle d’équilibre ; un corps solide ajoute une résistance mécanique. Le laboratoire ne calcule ni équilibre fluide ni rupture. Les segments du dessin montrent le champ linéarisé, sans prétendre représenter la forme finale d’un corps.

L’étude relie mécanique, calcul différentiel et astrophysique : développer un champ vectoriel au voisinage d’un point, interpréter sa matrice de dérivées et vérifier le domaine de validité de l’approximation.

## 13. Choisir un système fermé pour obtenir l’équation de la fusée

Sup → Spé · Laboratoire `fusee`

La fusée seule est un système ouvert : sa masse m diminue. Pour appliquer un bilan de quantité de mouvement, considérer entre t et t+dt le système fermé formé de la fusée et du gaz qui est éjecté pendant cette durée. La masse éjectée est −dm>0.

Si la vitesse de la fusée est v et la vitesse relative d’éjection vers l’arrière est u>0, la vitesse galiléenne du gaz est v−u. Au premier ordre, la variation de quantité de mouvement du système vaut m dv+u dm. Sous une pesanteur uniforme verticale descendante, elle est égale à −mg dt.

m dv=−u dm−mg dt ; m dv/dt=uq−mg avec q=−dm/dt>0.

La poussée est uq. On ne peut pas appliquer à la fusée seule l’équation d(mv)/dt=−mg sans ajouter le flux de quantité de mouvement du gaz. La formule d’un corps absorbant de la matière immobile dans un référentiel ne doit pas être utilisée pour une éjection à vitesse relative non nulle.

Sans pesanteur, intégrer dm/m entre m₀ et mf donne Δv=u ln(m₀/mf). À vitesse d’éjection fixée, c’est le rapport de masses qui détermine le gain, et non la seule masse de carburant en kilogrammes.

## 14. Débit constant : vitesse, déplacement et pertes gravitationnelles

Spé · Laboratoire `fusee`

Avec un débit q constant et une durée de poussée τ, m(t)=m₀−qt et mf=m₀−qτ. À g constant et avec v(0)=0, l’intégration du bilan donne :

v(t)=u ln[m₀/m(t)]−gt ; Δvfinal=u ln(m₀/mf)−gτ.

Le premier terme est le gain idéal. Le second est une perte de vitesse due à la pesanteur pendant la poussée. À même rapport de masses et même u, une durée plus courte diminue cette perte ; elle exige cependant un débit et une poussée plus élevés.

z(t)−z₀=u{t+[m(t)/q]ln[m(t)/m₀]}−½gt².

On peut vérifier cette expression en la dérivant : les deux termes constants issus de la dérivée se simplifient et il reste u ln(m₀/m)−gt. L’accélération a=uq/m−g augmente au cours de la combustion puisque m diminue.

Exemple : u=3 000 m/s, m₀/mf=3 et τ=60 s donnent un gain idéal de 3 296 m/s. Sous g=9,8 m/s², la perte est 588 m/s et la vitesse finale environ 2 708 m/s. Le modèle ne prend pas en compte un sol, la traînée ou la diminution de g avec l’altitude.

## 15. Composition des accélérations dans un référentiel tournant

Spé · Laboratoire `coriolis`

Deux référentiels partagent une origine fixe. Le premier est galiléen ; les axes du second tournent à vitesse angulaire constante Ω autour de z. Pour un vecteur r, la dérivation dans les deux référentiels vérifie (dr/dt)I=(dr/dt)R+Ω×r.

Une seconde dérivation donne aI=aR+2Ω×vR+Ω×(Ω×r). Comme le point du laboratoire est libre, aI=0. L’observateur tournant peut donc écrire sa dynamique avec des forces d’inertie :

m aR=−2mΩ×vR−mΩ×(Ω×r).

Le premier terme est la force de Coriolis, qui dépend de la vitesse relative. Le second est la force centrifuge, dirigée vers l’extérieur de l’axe. Pour r=(x,y,0), Ω=(0,0,Ω), leurs composantes divisées par m sont (2Ωvy,−2Ωvx) et Ω²(x,y).

Si Ω variait, il faudrait ajouter le terme d’Euler −mΩ̇×r. Si l’origine accélérait, un autre terme d’entraînement apparaîtrait. Le laboratoire fixe ces deux effets à zéro pour isoler la rotation uniforme.

## 16. Une vérification exacte par rotation des coordonnées

Spé · Prolongement · Laboratoire `coriolis`

Dans le référentiel galiléen, un point libre de vitesse constante v₀ suivant x possède les coordonnées (x₀+v₀t,y₀). Un observateur tournant utilise une matrice de rotation d’angle −Ωt :

xR=cos(Ωt)(x₀+v₀t)+sin(Ωt)y₀ ; yR=−sin(Ωt)(x₀+v₀t)+cos(Ωt)y₀.

Cette solution exacte permet de vérifier les signes des termes d’inertie. La norme de la position est conservée par la rotation, mais la vitesse relative n’a généralement pas la même norme que la vitesse galiléenne : elle contient aussi le terme −Ω×r.

La force de Coriolis ne travaille pas : son produit scalaire avec vR est nul. La force centrifuge dérive du potentiel −mΩ²(x²+y²)/2. Pour Ω constant, l’énergie dans le référentiel tournant possède donc un invariant :

J=½m|vR|²−½mΩ²|r|² = constante.

Cette constante ne se confond pas avec l’énergie cinétique galiléenne ½mv₀². Elle s’exprime aussi J=EI−ΩLz,I pour ce mouvement libre. Le calcul entraîne à distinguer coordonnées, vitesses et référentiels dans les bilans.

## 17. Des forces entre voisins aux modes propres d’une chaîne

Sup → Spé · Laboratoire `chaine_atomique`

On considère N masses identiques m, espacées de a au repos et reliées par des ressorts de raideur k. La variable u_(j)(t) désigne le **déplacement** de la masse j : sa position est ja+u_(j). Les indices sont périodiques, u_(j+N)=u_(j). Il y a N masses distinctes ; une masse supplémentaire dessinée pour fermer la cellule ne constitue pas un degré de liberté supplémentaire.

1. Bilan mécanique local

Le ressort de droite exerce k(u_(j+1)−u_(j)) et celui de gauche −k(u_(j)−u_(j−1)). Le principe fondamental donne m ü_(j)=k(u_(j+1)+u_(j−1)−2u_(j)). L’énergie totale est E=½m∑u̇_(j)²+½k∑(u_(j+1)−u_(j))² ; chaque ressort doit être compté une seule fois.

2. Chercher une forme commune de mouvement

Avec u_(j)=Re(Ue^(i(κja−ωt))), la périodicité impose κa=2πq/N. Substituer donne mω²=k(2−e^(iκa)−e^(−iκa))=4k sin²(κa/2). La pulsation positive est donc **ω=2√(k/m)|sin(κa/2)|**. q et q+N désignent le même mode ; q et N−q ont la même fréquence.

3. Interpréter le mode nul

Pour q=0, toutes les masses ont le même déplacement. Aucun ressort n’est allongé : ω=0. Le mouvement peut être une translation uniforme si l’on donne une vitesse initiale commune ; avec une vitesse initiale nulle, le déplacement commun reste constant.

**Technique CPGE :** distinguer position et déplacement, faire le bilan de deux forces, utiliser l’écriture complexe puis revenir au mouvement réel. Un mode propre fait osciller toutes les masses à une pulsation unique ; une préparation locale est une superposition de modes.

## 18. Du réseau discret à l’équation des ondes

Spé → Au-delà · Laboratoire `chaine_atomique`

Le paramètre qui contrôle le passage au continu est |κa| : la longueur d’onde doit être grande devant l’espacement. Pour |κa|≪1, sin(κa/2)≈κa/2 et ω≈c|κ|, avec **c=a√(k/m)**. La dispersion linéaire du milieu continu est seulement la tangente au voisinage de κ=0.

Développement spatial

Si u_(j)(t)≈u(ja,t), alors u(x+a)+u(x−a)−2u(x)=a²∂²u/∂x²+(a⁴/12)∂⁴u/∂x⁴+… . Au premier ordre utile, ∂²u/∂t²=c²∂²u/∂x². Le premier terme négligé explique pourquoi un réseau réel devient dispersif à courte longueur d’onde.

Deux vitesses à distinguer

Dans la première zone 0<κa<π, la vitesse de phase vaut ω/κ et la vitesse de groupe dω/dκ=c cos(κa/2). Elles tendent vers c quand κa→0. À κa=π, deux masses voisines se déplacent en sens opposés et la vitesse de groupe s’annule ; cela ne signifie pas que chaque masse est immobile.

Une impulsion n’est pas une sinusoïde

La transformée de Fourier discrète écrit u_(j)(0)=∑Q_(q)e^(2iπqj/N). Chaque coefficient évolue avec sa propre pulsation. Des vitesses de groupe différentes déforment une perturbation localisée ; dans une cellule périodique, les perturbations peuvent ensuite revenir vers leur point de départ.

**Limite du modèle :** les nombres choisis décrivent une maquette mécanique. L’application à des vibrations cristallines utilise exactement cette mécanique harmonique, mais l’énergie quantifiée des phonons demande un modèle quantique distinct. Le laboratoire ne l’ajoute pas implicitement.

## 19. CO₂ : diagonaliser avec une matrice de masse

Spé · Laboratoire `molecule_co2`

Les déplacements longitudinaux des trois atomes forment X=(x₁,x₂,x₃)ᵀ. Les oxygènes ont la masse m_(O), le carbone m_(C). L’énergie cinétique est T=½ẊᵀMẊ, M=diag(m_(O),m_(C),m_(O)) ; le potentiel est V=½XᵀKX, avec K=k[[1,−1,0],[−1,2,−1],[0,−1,1]]. Les deux ressorts représentent les liaisons chimiques autour de leur longueur d’équilibre.

Équations et valeurs propres

Le PFD, ou les équations de Lagrange, donne **MẌ+KX=0**. Un mode X=a cos(ωt) vérifie Ka=ω²Ma. Comme les masses sont différentes, diagonaliser K seul ne donne pas les pulsations. Poser b=M^(1/2)a : la matrice D=M^(−1/2)KM^(−1/2) est réelle symétrique et Db=ω²b.

Les trois mouvements

- (1,1,1), ω=0 : translation de la molécule dans la direction étudiée.
- (1,0,−1), ω₁²=k/m_(O) : les oxygènes sont en opposition, le carbone reste immobile.
- (1,−2m_(O)/m_(C),1), ω₂²=k/m_(O)+2k/m_(C) : les oxygènes vont ensemble et le carbone en sens opposé.

Pour les deux vibrations, ∑m_(j)a_(j)=0 : le centre de masse reste fixe. Ce contrôle donne immédiatement le rapport d’amplitude du carbone dans le second mode.

**À retenir :** le mode nul appartient ici à un modèle longitudinal. Les flexions transversales de CO₂ ne sont pas contenues dans ces trois coordonnées ; elles nécessitent un autre potentiel et d’autres degrés de liberté.

## 20. Énergie des modes, isotopes et nombres d’onde

Spé → Au-delà · Laboratoire `molecule_co2`

Si a_(i) et a_(j) correspondent à des valeurs propres différentes, la symétrie de K donne (ω_(i)²−ω_(j)²)a_(i)ᵀMa_(j)=0. Les modes sont donc orthogonaux pour le produit scalaire **pondéré par les masses**. Leur norme usuelle n’a aucune raison d’être 1 ni de représenter une énergie.

Découpler le mouvement

Avec des modes normalisés par a_(i)ᵀMa_(j)=δ_(ij), écrire X=∑Q_(i)a_(i). On obtient T=½∑Q̇_(i)² et V=½∑ω_(i)²Q_(i)². Chaque coordonnée vibratoire vérifie Q̈_(i)+ω_(i)²Q_(i)=0 ; la translation vérifie Q̈₀=0.

Changer la masse sans changer la liaison

Un remplacement isotopique change ici M, mais laisse k constant. Si seul m_(C) augmente, ω₁ reste identique car le carbone ne participe pas à ce mode ; ω₂ diminue. Cette comparaison est plus formatrice qu’une simple substitution numérique dans √(k/m), car tous les atomes ne contribuent pas de la même façon.

Relier les unités à la spectroscopie

La fréquence est ν=ω/(2π), en Hz. Le nombre d’onde spectroscopique est ν/c, en m⁻¹, puis ν/(100c), en cm⁻¹. Il ne faut pas le confondre avec le nombre d’onde angulaire κ=2π/λ. L’unité de masse atomique vaut u=1,66053906660×10⁻²⁷ kg ; 1 pm=10⁻¹² m.

**Prolongement :** le modèle prédit des fréquences mécaniques, sans calculer quelles vibrations sont actives en infrarouge ou en Raman. Les intensités et règles de sélection dépendent des variations du moment dipolaire et de la polarisabilité ; elles ne se déduisent pas des seules valeurs propres de D.

## 21. Le pendule de Foucault : écrire le PFD terrestre

Spé · Laboratoire `foucault`

On utilise des axes horizontaux x,y et un axe vertical z orienté vers le haut. La pesanteur effective vaut −g e_(z) ; l’accélération centrifuge stationnaire est incluse dans cette pesanteur. La vitesse angulaire terrestre a une composante verticale Ω=Ω_(T) sin λ, où λ est la latitude, positive au nord.

Identifier la force qui dévie

Le PFD dans le référentiel terrestre contient la force de Coriolis −2mΩ⃗_(T)×v⃗. Aux petits angles, la tension est voisine de mg et son rappel horizontal vaut −mg(x,y)/L. Après projection et au premier ordre des déplacements horizontaux : **ẍ+ω₀²x=2Ωẏ ; ÿ+ω₀²y=−2Ωẋ**, avec ω₀²=g/L.

Contrôles immédiats

La force de Coriolis est perpendiculaire à la vitesse, donc elle ne travaille pas. Pour ces équations linéaires, ½m(ẋ²+ẏ²)+½mω₀²(x²+y²) est conservée. À l’équateur Ω=0 et les deux oscillateurs ne sont plus couplés ; changer de signe la latitude change de signe la déviation.

Vérifier les hypothèses

A/L mesure l’ordre de grandeur de l’angle. Le rapport |Ω|/ω₀ compare les deux échelles de temps et vaut quelques 10⁻⁴ pour un grand pendule. La composante horizontale de la rotation terrestre ne contribue pas au même ordre au mouvement horizontal linéarisé ; elle intervient dans les corrections de la tension et dans des termes de plus petit ordre.

**Technique CPGE :** nommer le référentiel, dessiner les axes, distinguer pesanteur effective et forces d’inertie, projeter le PFD puis vérifier le signe par le produit vectoriel. L’équation obtenue est un modèle de petits déplacements, pas celle d’un pendule sphérique arbitraire.

## 22. Une oscillation rapide dans un plan qui tourne lentement

Spé → Au-delà · Laboratoire `foucault`

Poser z=x+iy regroupe les deux équations en z̈+2iΩż+ω₀²z=0. Le changement de variable **z=e^(−iΩt)w(t)** donne ẅ+(ω₀²+Ω²)w=0. Le facteur complexe e^(−iΩt) tourne la figure ; w(t) décrit son oscillation rapide.

Respecter les conditions initiales

Le lâcher sans vitesse dans les axes terrestres impose z(0)=A et ż(0)=0. Il faut donc w(0)=A et ẇ(0)=iΩA. Avec ν=√(ω₀²+Ω²), on obtient w=A[cos(νt)+i(Ω/ν)sin(νt)]. Remplacer w par une constante supprimerait l’oscillation ; négliger son petit terme imaginaire introduirait une vitesse initiale terrestre non nulle.

Trois durées à ne pas confondre

La période rapide est 2π/ν≈2π√(L/g). La direction tourne à la vitesse orientée −Ω. Un tour complet prend 2π/|Ω|=T_(sidéral)/|sin λ|. Le jour sidéral vaut 86164,0905 s ; utiliser 24 h est une approximation raisonnable pour un premier calcul, mais le laboratoire emploie le jour sidéral.

Une droite n’a pas de sens privilégié : son orientation est définie modulo π. La durée d’un retour de la même droite est donc π/|Ω| ; la durée affichée dans le bilan est celle d’un tour orienté complet de 2π. Ces deux lectures doivent être distinguées.

Observer sans créer de fausse lenteur

Une trajectoire sur plusieurs heures ne peut pas être correctement représentée avec seulement quelques centaines de points espacés de minutes. Le laboratoire affiche trois enregistrements courts et suffisamment échantillonnés, séparés dans le temps. L’angle de précession, lui, varie réellement à l’échelle des heures.

## 23. Pendule exact : obtenir une période à partir de l’énergie

Sup → Spé · Laboratoire `pendule_exact`

L’angle θ est compté depuis la verticale descendante. Une masse ponctuelle m est reliée à un point fixe par une liaison de longueur L. Pour un fil, la tension doit rester positive ; pour un lâcher sans vitesse à plus de 90°, il faut une **tige rigide** sans masse. Le modèle à grande amplitude du laboratoire utilise cette possibilité.

L’équation mécanique

Le moment du poids donne mL²θ̈=−mgL sin θ. Ainsi θ̈+(g/L) sin θ=0. L’énergie vaut E=½mL²θ̇²+mgL(1−cos θ). Si l’on lâche à θₘ sans vitesse, E=mgL(1−cos θₘ) et |θ̇|=√[(2g/L)(cos θ−cos θₘ)].

Le temps d’un quart d’oscillation

Par symétrie, T=4∫₀^{θₘ}dθ/√[(2g/L)(cos θ−cos θₘ)]. L’intégrande devient infinie au point de rebroussement mais cette singularité est intégrable. Poser sin(θ/2)=s sin φ, s=sin(θₘ/2), élimine cette difficulté : **T=4√(L/g)∫₀^{π/2}dφ/√(1−s²sin²φ)**.

Contrôler plutôt que supposer

Le laboratoire calcule T par une quadrature de Gauss à 96 points. Il calcule séparément la trajectoire par l’algorithme de Verlet et mesure T entre deux passages descendants par θ=0. L’accord de ces méthodes et la variation de l’énergie fournissent des contrôles indépendants.

**Résultat physique :** la masse n’intervient ni dans l’équation ni dans la période. En revanche, θₘ intervient dans la période exacte. L’isochronisme est une propriété approchée du pendule aux petits angles.

## 24. Petits angles, sommet instable et contrôle numérique

Sup → Spé · Laboratoire `pendule_exact`

Pour θₘ petit, développer l’intégrande de la période donne T/T₀=1+θₘ²/16+11θₘ⁴/3072+O(θₘ⁶), avec T₀=2π√(L/g). Les angles doivent être exprimés en **radians** : 60° vaut π/3, et non 60 dans cette formule.

Que se passe-t-il près de θ=π ?

θ=π est un équilibre instable du pendule à tige. Au niveau d’énergie E=2mgL, la trajectoire sépare oscillations et rotations. Pour θₘ=π−ε, ε petit et positif, la période diverge comme 4√(L/g) ln(8/ε). Le pendule passe un temps très long près du sommet, où le moment du poids devient très faible.

Le portrait de phase

Les petites orbites autour de (θ,θ̇)=(0,0) sont presque elliptiques. À énergie croissante, elles s’approchent de la trajectoire séparatrice passant par les sommets instables. Une grande période n’est pas une grande vitesse : elle provient surtout du ralentissement à proximité du sommet.

L’algorithme de Verlet

Avec a(θ)=−(g/L)sin θ : θ_(n+1)=θ_(n)+hθ̇_(n)+½h²a(θ_(n)), puis θ̇_(n+1)=θ̇_(n)+½h[a(θ_(n))+a(θ_(n+1))]. Cette méthode conserve bien la géométrie des trajectoires conservatives sans conserver exactement l’énergie à chaque pas. Diminuer h doit améliorer le bilan.

**Technique :** séparer l’erreur de modèle, par exemple sin θ≈θ, de l’erreur de discrétisation. Une trajectoire numérique précise du modèle linéaire ne devient pas pour autant une trajectoire exacte du pendule réel.

## 25. Développement quartique : corriger le rappel du pendule

Sup → Spé · Laboratoire `pendule_anharmonique`

V=mgL(1−cos θ) donne V=mgL(θ²/2−θ⁴/24+O(θ⁶)). Le moment généralisé −∂V/∂θ est −mgL(θ−θ³/6+O(θ⁵)). Le mouvement tronqué vérifie donc **θ̈+ω₀²(θ−θ³/6)=0**. Le terme cubique réduit le rappel par rapport au modèle linéaire : on parle d’un oscillateur assouplissant.

Pourquoi la correction change aussi la période

Remplacer seulement la sinusoïde par une sinusoïde légèrement déformée à la même fréquence laisse une erreur de phase qui grandit au fil des oscillations. Il faut chercher une pulsation Ω=ω₀(1−θₘ²/16)+O(θₘ⁴), d’où T=T₀(1+θₘ²/16)+O(θₘ⁴).

Une approximation locale

Le polynôme θ²/2−θ⁴/24 possède un minimum local en 0, mais tend vers −∞ lorsque |θ|→∞. Le potentiel exact, lui, est périodique et borné. Le polynôme tronqué n’est donc pas un potentiel global de pendule ; l’utiliser à des angles arbitrairement grands produit un autre système.

Le laboratoire limite les comparaisons à θₘ≤80°. Le modèle avec rappel cubique est intégré avec les mêmes conditions initiales que le modèle exact. La différence mesurée provient d’abord des termes supprimés du développement ; la variation d’énergie du calcul exact contrôle séparément l’intégration.

**Points d’appui CPGE :** développement limité, lien force–potentiel, stabilité locale, dimensions et conservation de l’énergie. Les corrections de pulsation obtenues par méthode perturbative constituent un prolongement de ces techniques.

## 26. D’où vient la troisième harmonique ?

Spé → Au-delà · Laboratoire `pendule_anharmonique`

La non-linéarité cubique produit une composante de rang 3 car cos³ψ=(3cosψ+cos3ψ)/4. Chercher θ=θₘ cos(Ωt)+θₘ³b(Ωt)+… fait apparaître une correction à la fréquence fondamentale et une oscillation à 3Ω.

Fixer la convention d’amplitude

Dans ce laboratoire, θₘ est l’angle au point de rebroussement, et θ̇(0)=0. À l’ordre utile : **θ≈θₘ[(1+θₘ²/192)cos(Ωt)−(θₘ²/192)cos(3Ωt)]**, avec Ω≈ω₀(1−θₘ²/16). Les deux corrections se compensent à t=0 : θ(0)=θₘ. Utiliser l’amplitude de la fondamentale comme paramètre conduirait à une écriture légèrement différente.

Mesurer un spectre sans faux étalement

Sur un nombre entier de périodes exactes, projeter θ(t) sur cos(jωt) et sin(jωt). Pour chaque rang, l’amplitude est la racine de la somme des carrés des deux coefficients. L’ajustement aux rangs impairs 1,3,…,9 évite de confondre une fréquence de FFT arrondie avec une véritable nouvelle harmonique.

La symétrie θ(t+T/2)=−θ(t) annule les harmoniques paires. Au premier ordre utile, A₃/A₁≈θₘ²/192. À plus grande amplitude, les rangs 5,7,… deviennent détectables et la formule à deux harmoniques cesse de suffire.

Ce que l’on compare

Une période peut être bien approchée alors que la forme du signal l’est moins, ou inversement. Les trois graphiques — trajectoire, période et harmoniques — testent trois propriétés distinctes du modèle. Une correction perturbative ne doit pas être jugée uniquement sur une seule oscillation.

## 27. Deux ressorts transversaux : une force géométriquement non linéaire

Sup → Spé · Laboratoire `ressorts_transverses`

Les points d’attache sont (0,L) et (0,−L). La masse se déplace suivant x sur le rail y=0. Chaque ressort a raideur k et longueur à vide L₀ ; sa longueur instantanée est ℓ=√(x²+L²). On suppose que les ressorts transmettent aussi la compression.

Deux méthodes pour obtenir la force

Chaque ressort stocke ½k(ℓ−L₀)². Leur somme donne **V(x)=k(√(x²+L²)−L₀)²**. En dérivant : V′=2k(1−L₀/ℓ)x et m ẍ=−V′. On peut aussi projeter sur x chacune des deux forces de Hooke ; le facteur x/ℓ explique la même expression.

Chercher tous les équilibres

V′=0 impose x=0 ou ℓ=L₀. Pour L>L₀, seul le centre existe. Pour L<L₀, les positions x=±√(L₀²−L²) s’ajoutent ; les deux ressorts y retrouvent leur longueur à vide. Ne retenir que la solution x=0 manquerait les minima les plus importants.

Étudier la stabilité

V″(0)=2k(1−L₀/L). Le centre est stable si L>L₀ et instable si L<L₀. Aux équilibres latéraux, V″=2k(1−L²/L₀²)>0. Les pulsations de petites oscillations valent √(V″/m), évaluées au minimum étudié.

**Technique CPGE :** construire une énergie potentielle complète, dériver, trouver toutes les racines, puis étudier la stabilité et la validité d’une linéarisation. La loi de Hooke linéaire n’implique pas une force linéaire dans une coordonnée liée à une géométrie variable.

## 28. Deux puits, barrière d’énergie et changement de stabilité

Spé → Au-delà · Laboratoire `ressorts_transverses`

Le paramètre de commande est ρ=L/L₀. Pour ρ>1, le potentiel possède un seul minimum au centre. Pour ρ<1, le centre devient un maximum local et deux minima symétriques apparaissent. Le graphe des équilibres en fonction de ρ montre ce changement de stabilité, appelé une bifurcation de type fourche dans les modèles symétriques.

Prévoir le mouvement sans intégrer

E=½m ẋ²+V(x) impose V(x)≤E. Pour L<L₀, la barrière centrale vaut V(0)=k(L₀−L)². Si E<V(0), une masse à droite reste dans le puits droit. Si E>V(0), elle peut traverser le centre. À E=V(0), la trajectoire peut tendre asymptotiquement vers l’équilibre instable : la durée caractéristique diverge.

Développement autour du centre

Pour |x|≪L : V(x)=k(L−L₀)²+k(1−L₀/L)x²+[kL₀/(4L³)]x⁴+O(x⁶). Le coefficient de x² change de signe au seuil ; le coefficient de x⁴ est positif. Ce développement explique la forme locale du changement de stabilité.

Le développement est autour du centre, et non autour des minima latéraux. Si l’on veut une approximation harmonique dans un puits, il faut poser ξ=x−xₑ et développer V(xₑ+ξ)=V(xₑ)+½V″(xₑ)ξ²+… . Confondre ces deux centres de développement conduit à une mauvaise pulsation.

Lire le portrait de phase

Les courbes fermées autour de chaque minimum représentent les oscillations confinées. Au-dessus de la barrière, une seule orbite peut entourer les deux minima. Le calcul temporel du laboratoire vérifie cette prédiction énergétique ; il ne remplace pas le raisonnement sur V≤E.

## 29. Minimum quartique : la stabilité ne se réduit pas à V″ > 0

Sup → Spé · Laboratoire `oscillateur_quartique`

Au seuil L=L₀, √(L₀²+x²)−L₀=x²/(2L₀)+O(x⁴). Les deux ressorts donnent V=kx⁴/(4L₀²)+O(x⁶). On pose β=k/L₀², en N/m³, et on étudie le modèle **V=βx⁴/4**. La force vaut −βx³.

Un équilibre stable avec V″(0)=0

V(x)>V(0) pour tout x≠0 : le centre est un minimum strict. Il est stable malgré une dérivée seconde nulle. Le critère V″>0 est suffisant, mais une dérivée seconde nulle exige d’examiner le premier terme non nul du développement ; ici ce terme est pair et positif.

Pourquoi la fréquence linéaire est inutilisable

Linéariser m ẍ=−βx³ au centre donne ẍ=0. Cela signifie que le rappel linéaire est nul, et non que toute perturbation réelle s’éloigne sans retour. Pour calculer les petites oscillations, il faut conserver le premier terme de rappel existant, même s’il est non linéaire.

Une amplitude et une période

Au lâcher x=A>0, ẋ=0 et E=βA⁴/4. Pour tout A positif, le mouvement est périodique entre −A et A. À amplitude nulle, le mouvement est stationnaire ; il n’y a pas de période mesurable. La limite T→∞ lorsque A→0 est compatible avec cette situation.

**Transfert de technique :** un minimum en x⁶ ou x⁸ demanderait le même examen. Pour V∝x^(2p) avec p>1, le rappel dominant est en x^(2p−1) et la période dépend nécessairement de l’amplitude.

## 30. La loi T ∝ 1/A : énergie et changement d’échelle

Spé → Au-delà · Laboratoire `oscillateur_quartique`

La conservation de l’énergie donne ẋ²=(β/2m)(A⁴−x⁴). Un quart de période est l’intégrale de dx/|ẋ| entre 0 et A. Avec u=x/A : **T=4√(2m/β) A⁻¹ I**, où I=∫₀¹du/√(1−u⁴).

Régulariser l’intégrale

Au point u=1, l’intégrande a une singularité intégrable. Poser u=sin φ donne I=∫₀^{π/2}dφ/√(1+sin²φ), sans singularité. Numériquement, I≈1,31103 et T≈7,41630√(m/β)/A. Les dimensions sont correctes : √(m/β) est en m·s.

Retrouver la même loi sans quadrature

Avec x=Au et τ=A√(β/m)t, l’équation devient u″+u³=0, u(0)=1, u′(0)=0. Tous les mouvements ont la même période en τ ; en secondes, leur période est donc proportionnelle à 1/A. Doubler A divise exactement T par deux dans le modèle quartique pur.

Comparer au modèle exact des ressorts

V_(exact)=k(√(L₀²+x²)−L₀)² partage le même premier terme, mais possède des corrections en x⁶ et au-delà. Le produit T×A n’y est plus exactement constant. Le laboratoire calcule une seconde période par quadrature dans ce potentiel, puis la compare à la loi quartique.

**Interprétation :** l’égalité T∝1/A est un résultat exact du modèle V=βx⁴/4. Pour les ressorts, c’est une loi asymptotique quand A/L₀→0. La distinction entre modèle exact et approximation locale permet de donner un sens physique à l’écart mesuré.

## 31. Oscillateur forcé : énergie, régime établi et Duffing

Sup → Spé · Laboratoire `duffing_force`

Le cours linéaire étudie m ẍ+λẋ+kx=F₀cos(ωt). Avec ω₀=√(k/m), ζ=λ/(2mω₀), r=ω/ω₀, x=x_(réf)u et τ=ω₀t, on obtient u″+2ζu′+u=f cos(rτ), où f=F₀/(mω₀²x_(réf)).

Ajouter une force cubique

Un potentiel V=½kx²+¼b x⁴ donne un terme b x³ dans l’équation. Après réduction, **u″+2ζu′+u+βu³=f cos(rτ)**, avec β=b x_(réf)²/k. Le laboratoire choisit β≥0, un rappel durcissant et un potentiel borné inférieurement.

Le bilan énergétique

La multiplication par u′ donne dE/dτ=f cos(rτ)u′−2ζu′², avec E=½u′²+½u²+βu⁴/4. L’amplitude de la force seule ne suffit pas à prévoir son travail : c’est le produit force×vitesse qui donne la puissance. En régime périodique établi, l’énergie moyenne ne change plus et les puissances moyennes injectée et dissipée sont égales.

Une réponse calculée, pas supposée

Le calcul part de u(0) choisi et de u′(0)=0. L’intégration à fréquence fixe garde le transitoire. L’amplitude fondamentale est mesurée sur les dix dernières périodes, puis sur les dix précédentes. Leur écart sert à vérifier si la réponse est presque stationnaire ; une durée finie ne le garantit pas.

**Repères :** oscillateur linéaire amorti forcé et puissances moyennes : cours CPGE. Le terme cubique, les réponses multiples et les bifurcations : prolongement explicite. Les unités physiques se retrouvent avec x=x_(réf)u et t=τ/ω₀.

## 32. Une approximation de la résonance non linéaire

Spé → Au-delà · Laboratoire `duffing_force`

Pour une réponse presque sinusoïdale, chercher u≈A cos(rτ−φ). Comme cos³ψ=(3cosψ+cos3ψ)/4, négliger le rang 3 revient à remplacer βu³ par (3βA²/4)u dans la composante fondamentale.

Éliminer le déphasage

Projeter l’équation sur le cosinus et le sinus donne f²=A²[(1−r²+3βA²/4)²+(2ζr)²]. Avec Z=A², c’est un polynôme cubique. Pour β=0, on retrouve l’amplitude linéaire A=f/√[(1−r²)²+(2ζr)²]. Pour β>0, la pulsation effective augmente avec A : la résonance se déforme vers les fréquences élevées.

Ce que signifient trois racines

Trois racines positives donnent trois amplitudes candidates de cette approximation. Elles ne prouvent pas que trois mouvements stables existent. Il faut examiner la stabilité des réponses périodiques et les harmoniques supprimées. Une préparation initiale et un balayage lent peuvent sélectionner des réponses différentes ; le laboratoire calcule une seule évolution à fréquence fixe.

Lire les contrôles

Le point mesuré sur la courbe de réponse est la fondamentale du mouvement intégré. Son écart aux racines approchées peut provenir d’harmoniques importantes, d’un transitoire ou d’une réponse non simplement périodique. Le bilan du travail et de la dissipation contrôle la méthode numérique, pas la pertinence de l’approximation à une harmonique.

**Prolongement guidé :** pour démontrer une hystérésis, il faudrait construire deux balayages temporels lents, croissant et décroissant, et vérifier leurs vitesses. La seule forme repliée d’une équation approchée ne suffit pas ; cette expérience prépare cette étude sans la prétendre réalisée.

## 33. Construire une matrice d’inertie à partir de masses ponctuelles

Spé · prolongement MPSI/MP · Laboratoire `inertie_huygens`

Pour un solide, l’inertie dépend de la direction de rotation. On mesure rᵢ=GMᵢ et on représente les positions par des colonnes. Une même formule doit donner tous les moments autour des axes passant par G.

I_G=Σmᵢ[(rᵢ·rᵢ)Id−rᵢrᵢᵀ] ; I(u)=uᵀI_Gu, |u|=1 ; E_c,rotation=½ΩᵀI_GΩ.

Démonstration et méthode

La distance au carré entre Mᵢ et l’axe de direction u vaut |rᵢ×u|²=|rᵢ|²−(rᵢ·u)². Sommer après multiplication par mᵢ donne la forme quadratique. I_G est symétrique et positive ; elle est définie positive si les masses ne sont pas toutes sur une même droite. Le théorème spectral fournit une base orthonormée d’axes principaux.

Application

Une tige mince a une inertie nulle suivant sa propre direction dans le modèle idéal, mais une forte inertie autour d’un axe perpendiculaire. Un satellite allongé ne réagit donc pas de la même façon à tous les couples.

## 34. Huygens : déplacer un axe sans changer sa direction

Spé · prolongement MPSI/MP · Laboratoire `inertie_huygens`

O est un point quelconque et d=OG. Le théorème de Huygens relie les inerties autour de deux axes parallèles, l’un passant par G, l’autre par O. Sa version matricielle conserve les produits d’inertie.

I_O=I_G+M[(d·d)Id−ddᵀ] ; I_O(u)=I_G(u)+M|d×u|².

Démonstration et méthode

Dans la somme définissant I_O, remplacer OMᵢ par d+rᵢ. Tous les termes linéaires en rᵢ s’annulent parce que Σmᵢrᵢ=0. Il reste I_G et le terme de translation. En multipliant à gauche par uᵀ et à droite par u, on retrouve Huygens scalaire. Si d est parallèle à u, la distance entre les axes vaut zéro : il s’agit du même axe.

Application

Pour une barre homogène de longueur 2L, I_G=ML²/3 autour d’un axe transverse et I_O=4ML²/3 autour d’un pivot situé à l’extrémité.

## 35. Second théorème de König : le terme croisé disparaît en G

Spé · prolongement MPSI/MP · Laboratoire `konig`

Le référentiel barycentrique a son origine en G et ses axes restent parallèles à ceux du laboratoire. Il peut être accéléré : le théorème de König est d’abord une identité cinématique.

E_c=½M|v_G|²+E_c,G ; vᵢ=v_G+vᵢ/G ; Σmᵢvᵢ/G=0.

Démonstration et méthode

Développer chaque carré |v_G+vᵢ/G|². Le terme croisé est v_G·Σmᵢvᵢ/G, nul par dérivation de ΣmᵢGMᵢ=0. Pour un solide rigide, vᵢ/G=Ω×GMᵢ et E_c,G=½ΩᵀI_GΩ. Il ne faut pas remplacer cette énergie par ½Iω² sans avoir identifié l’axe et l’inertie adaptés.

Application

Pour une roue roulant sans glissement, v_G=Rω. Avec I_G=kmR², E_c=½m(1+k)v_G². Le même gain de hauteur donne moins de vitesse de translation à un cerceau qu’à une boule.

## 36. Premier théorème de König : moment orbital et moment propre

Spé · prolongement MPSI/MP · Laboratoire `konig`

Un solide peut tourner autour de son centre de masse tout en se déplaçant par rapport à O. Ces deux mouvements contribuent au moment cinétique en O, qui est un vecteur.

L_O=OG×Mv_G+L_G ; L_G=I_GΩ pour un solide rigide.

Démonstration et méthode

Insérer OMᵢ=OG+GMᵢ et vᵢ=v_G+vᵢ/G dans ΣOMᵢ×mᵢvᵢ. Les deux sommes croisées s’annulent grâce aux définitions de G et du référentiel barycentrique. Le terme OG×Mv_G est dit orbital ; le terme L_G décrit le mouvement autour de G. Les deux peuvent être opposés et se compenser.

Application

Une patineuse en mouvement possède un moment orbital par rapport au bord de la patinoire et un moment propre si elle tourne. Le choix du point O change le premier, pas le second.

## 37. Basculement d’une barre : exploiter l’énergie avant le PFD

Sup → Spé · Laboratoire `barre_bascule`

Une barre homogène de longueur 2L est fixée à une extrémité. L’angle θ=0 correspond à la verticale ascendante, équilibre instable. Le pivot ne se déplace pas et sa réaction ne travaille pas.

I_O=4ML²/3 ; E=½I_Oθ̇²+MgLcosθ ; θ̈=(3g/(4L))sinθ.

Démonstration et méthode

Le moment du poids en O vaut MgLsinθ dans le sens de croissance de θ. Le théorème du moment cinétique donne I_Oθ̈=MgLsinθ. Multiplier par θ̇ retrouve la conservation de l’énergie. Sur la trajectoire limite E=MgL, θ̇²=(3g/(2L))(1−cosθ), puis θ̇=√(3g/L)sin(θ/2) pour un basculement vers les angles croissants.

Application

À θ=90°, θ̇=√(3g/(2L)) et la vitesse de G vaut √(3gL/2). Une barre longue acquiert une plus grande vitesse linéaire, mais bascule avec une plus faible vitesse angulaire.

## 38. Durée exacte et force du pivot : deux calculs complémentaires

Spé · Laboratoire `barre_bascule`

L’énergie donne la vitesse sans calculer la réaction. Pour la réaction, il faut ensuite revenir au PFD et employer l’accélération normale autant que l’accélération tangentielle.

Δt=2√(L/(3g))ln[tan(θ₂/4)/tan(θ₁/4)] ; Rᵣ=Mg(5cosθ−3)/2 ; Rθ=−Mg sinθ/4.

Démonstration et méthode

Intégrer dt=dθ/[√(3g/L)sin(θ/2)] en utilisant une primitive 2ln tan(θ/4). Dans la base eᵣ,eθ, a_G=−Lθ̇²eᵣ+Lθ̈eθ et Mg=−Mgcosθ eᵣ+Mgsinθ eθ. Soustraire le poids à Ma_G donne les deux composantes de R. Rᵣ peut être négatif : un pivot est une liaison qui peut tirer, contrairement à un contact unilatéral.

Application

Le temps diverge logarithmiquement quand θ₁ tend vers 0. Cela traduit l’équilibre instable : une barre exactement dressée, sans perturbation, ne commence pas à tomber spontanément.

## 39. Barre sur rotule : préciser la convention des angles

Spé · prolongement MPSI/MP · Laboratoire `barre_rotule`

La rotule fixe O et autorise une orientation spatiale. On choisit θ comme angle avec la verticale ascendante et φ comme azimut. Cette convention est annoncée pour éviter de mélanger colatitude et élévation.

n=(sinθcosφ,sinθsinφ,cosθ) ; OG=Ln ; v_G=Lṅ ; E_c=½I⊥|ṅ|², I⊥=4ML²/3.

Démonstration et méthode

Différencier n composante par composante, ou employer ṅ=θ̇eθ+φ̇sinθ eφ. La vitesse angulaire perpendiculaire à la barre est Ω⊥=n×ṅ. La composante parallèle à n ne modifie pas son axe. Pour une barre mince, l’inertie axiale est négligée : L_O=I⊥n×ṅ, mais il serait incorrect d’affirmer que toute vitesse angulaire est déterminée par OG et v_G.

Application

Un lancer sans vitesse d’azimut donne un mouvement plan. Avec φ̇ initiale non nulle, la conservation de L_z peut empêcher la barre de traverser la verticale.

## 40. Énergie et moment vertical : réduire le pendule spatial

Spé · prolongement MPSI/MP · Laboratoire `barre_rotule`

Le couple du poids n’a pas de composante verticale. La rotule ne transmet aucun couple. Deux constantes du mouvement permettent de décrire l’évolution de l’inclinaison sans résoudre toutes les composantes.

L_z=I⊥sin²θ φ̇ ; E=½I⊥θ̇²+L_z²/(2I⊥sin²θ)+MgLcosθ.

Démonstration et méthode

Le théorème du moment cinétique donne dL_z/dt=0. Insérer φ̇=L_z/(I⊥sin²θ) dans l’énergie produit un potentiel effectif en θ. Pour L_z≠0, le terme en 1/sin²θ diverge près des verticales. Une rotation conique vérifie θ̇=0 et φ̇²=−(3g/(4L))/cosθ ; elle exige donc θ>90° avec notre convention.

Application

Pour L=0,7 m et θ=120°, la rotation conique demande φ̇≈4,585 rad/s. Le laboratoire vérifie cette valeur et montre la nutation si l’on perturbe l’inclinaison.

## 41. Au bord de la table : commencer par le régime d’adhérence

Spé · Laboratoire `cylindre_bord`

Le cylindre plein est en contact avec une arête fixe. Pendant l’adhérence, il pivote autour de cette arête et le point matériel en contact a une vitesse nulle.

I_I=3mR²/2 ; θ̇²=(4g/(3R))(1−cosθ) ; T=(mg/3)sinθ ; N=(mg/3)(7cosθ−4).

Démonstration et méthode

Huygens donne I_I=I_G+mR². La perte d’énergie potentielle mgR(1−cosθ) fournit l’énergie de rotation. Le PFD tangent à la trajectoire du centre donne mRθ̈=mg sinθ−T ; la projection normale donne N=mg cosθ−mRθ̇². En remplaçant θ̇² et θ̈=(2g/(3R))sinθ, on trouve les expressions affichées.

Application

Les réactions ne sont pas constantes : le contact demande de plus en plus de réaction tangentielle alors que sa réaction normale diminue. La géométrie amplifie donc le risque de glissement.

## 42. Une formule cesse d’être utilisable quand le contact change

Spé · Laboratoire `cylindre_bord`

Un contact unilatéral ne peut exercer une force normale négative. L’adhérence impose en outre |T|≤fₛN. Il faut rechercher le premier événement qui viole ces conditions.

Glissement : sinθ=fₛ(7cosθ−4) ; référence de perte de contact en adhérence : θ_N=arccos(4/7).

Démonstration et méthode

Sur 0<θ<θ_N, T/N=sinθ/(7cosθ−4) croît de 0 à +∞. Pour tout coefficient statique fini positif, l’égalité T=fₛN survient donc avant N=0. Après glissement, le point de contact n’est plus fixe : ni I_Iθ̇²/2 ni l’ancienne expression de N ne décrivent automatiquement le mouvement réel. Il faut reconstruire la cinématique et employer T=f_dN avec le bon sens du glissement.

Application

Un algorithme de simulation doit arrêter ce régime au seuil détecté. Prolonger son animation jusqu’à θ_N donnerait une prédiction physiquement injustifiée.

## 43. Loi de Coulomb : une inégalité au repos, une égalité en glissement

Spé · MP · Laboratoire `coulomb_horizontal`

La force de frottement tangentielle est déterminée par le régime du contact. Le coefficient statique donne une borne, pas la valeur obligatoire de la réaction.

Adhérence : |T|≤fₛN ; glissement : T⃗=−f_dN v⃗_contact/|v⃗_contact|.

Démonstration et méthode

Sur un sol horizontal avec une traction F, le PFD vertical donne N=mg. Si la caisse reste au repos, le PFD horizontal impose T=−F, possible seulement si |F|≤fₛmg. Au-delà, elle démarre dans le sens de F ; pour une traction constante, T=−f_dmg signe(F) et a=(F+T)/m. À la limite statique, l’adhérence reste admissible : une perturbation peut provoquer le passage au régime cinétique.

Application

Une caisse de 3 kg avec fₛ=0,45 reste au repos sous 10 N, mais glisse sous 18 N. Pour f_d=0,315, l’accélération vaut environ 2,91 m/s².

## 44. Freinage et inversion : résoudre un changement de régime

Spé · MP · Laboratoire `coulomb_horizontal`

En glissement, le frottement extrait de l’énergie mécanique et la transforme en chaleur. Le signe de la force dépend de la vitesse relative des deux surfaces, et non d’un axe arbitrairement choisi.

Avant l’arrêt : a₁=(F−f_dmg)/m ; t_a=−v₀/a₁ si a₁<0 ; après : adhérence si |F|≤fₛmg, sinon a₂=(F+f_dmg)/m pour une reprise vers la gauche.

Démonstration et méthode

Partir avec v₀>0 impose T=−f_dmg, quelle que soit la direction de F. Avec a₁<0, v=v₀+a₁t et x=v₀t+a₁t²/2 jusqu’à t_a. À cet instant, tester Coulomb statique : soit x reste égal à x_a, soit la caisse repart avec x=x_a+a₂(t−t_a)²/2 et v=a₂(t−t_a). Les deux raccordements sont continus. Le bilan W_F=ΔE_c+Q garde l’énergie initiale, et Q=f_dmg×distance parcourue. Après inversion, cette distance est x_a+|x−x_a|, et non |x|.

Application

Pour m=3 kg, fₛ=0,45 et f_d=0,315, une force F=−6 N freine puis maintient la caisse immobile ; F=−18 N freine puis relance vers la gauche. La simulation traite explicitement ce changement de mode de contact, attendu dans le programme MP.

## 45. Pourquoi une boule descend-elle plus vite qu’un cerceau ?

Spé · MP / prolongement roulement · Laboratoire `plan_incline`

Les deux solides gagnent la même énergie gravitationnelle par unité de masse. Mais la répartition entre translation et rotation dépend du nombre sans dimension k=I_G/(mR²).

a=g sinα/(1+k) ; T=kmg sinα/(1+k) ; adhérence : [k/(1+k)]tanα≤fₛ.

Démonstration et méthode

Projeter le PFD sur la pente : ma=mg sinα−T. Prendre le moment en G : I_Gω̇=TR. Imposer la condition de roulement a=Rω̇ seulement si la force requise respecte Coulomb. Pour k=2/5, 1/2 et 1, les accélérations sont respectivement (5/7), (2/3) et (1/2)g sinα.

Application

Le roulement sans glissement n’exige pas T=fₛN : il exige T≤fₛN. Augmenter fₛ au-delà du seuil ne change donc pas l’accélération d’un solide déjà en roulement idéal.

## 46. Le frottement statique peut modifier la translation sans dissiper

Spé · MP / prolongement roulement · Laboratoire `plan_incline`

Le travail de la force tangentielle sur le centre de masse n’est pas à lui seul la puissance de cette force pour tout le solide. Il faut additionner translation et rotation.

P_T=−Tv_G+TRω=−T(v_G−Rω) ; roulement : v_G=Rω ⇒ P_T=0.

Démonstration et méthode

Le frottement ralentit la translation mais accélère la rotation. Sans glissement, les deux puissances se compensent. En glissement, T=f_dN s’oppose à la vitesse du point de contact : la puissance totale est négative. Pour un solide initialement au repos dont le contact glisse vers le bas, a=g(sinα−f_dcosα) et ω̇=f_dgcosα/(kR). Vérifier que a−Rω̇ reste positif justifie le sens choisi pour T.

Application

Une caisse peut rester immobile sur un plan où une boule roule. Les conditions tanα≤fₛ et [k/(1+k)]tanα≤fₛ répondent à deux problèmes différents.

## 47. Le couple du poids produit une précession

Spé · prolongement MPSI/MP · Laboratoire `gyroscope`

Une toupie tourne rapidement autour de son axe n. Son moment cinétique est alors principalement porté par cet axe. Le couple du poids est perpendiculaire à n : il dévie le moment cinétique plutôt qu’il ne le réduit.

L≈I₃ω₃n ; M_O=−mgℓn×e_z ; Ω_p≈mgℓ/(I₃ω₃).

Démonstration et méthode

Supposer une précession lente autour de la verticale et une inclinaison constante. Alors dL/dt≈Ω_p e_z×L. Identifier cette expression au couple du poids donne la fréquence angulaire approchée. La vitesse propre ω₃ doit être en rad/s : 18 tr/s correspond à 36π rad/s. Le rapport Ω_p/ω₃ teste une séparation des échelles, mais les conditions initiales peuvent toujours exciter une nutation.

Application

Doubler la vitesse propre divise la précession lente par deux. Ce mécanisme relie le TP de gyroscope aux précessions d’axes en astrophysique et, par analogie du moment cinétique, à la précession de Larmor.

## 48. Dépasser l’approximation : intégrer un solide de révolution

Spé · prolongement MPSI/MP · Laboratoire `gyroscope`

Les équations vectorielles évitent les difficultés des angles d’Euler aux pôles. I₁ désigne l’inertie transversale autour de O et I₃ l’inertie axiale.

s=L·n=I₃ω₃ ; ṅ=(L×n)/I₁ ; L̇=−mgℓn×e_z ; E=|L−sn|²/(2I₁)+s²/(2I₃)+mgℓn_z.

Démonstration et méthode

La composante axiale s est constante parce que le couple du poids n’a pas de composante suivant n. Décomposer L en sn et sa composante perpendiculaire. La cinématique ṅ=Ω×n donne l’équation de n. L_z et l’énergie totale sont aussi conservés. La nutation correspond à une variation périodique de l’inclinaison, visible quand le lancement ne place pas exactement la toupie sur une précession régulière.

Application

Une précession régulière exacte doit vérifier I₁cosθ Ω_p²−sΩ_p+mgℓ=0. L’approximation lente est la petite racine lorsque s²≫4I₁mgℓcosθ ; il peut exister une seconde branche rapide.
