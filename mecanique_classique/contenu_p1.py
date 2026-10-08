"""Cours, problèmes corrigés et objectifs expérimentaux de la section P1."""
LESSONS = []
EXERCISES = []
GUIDES = {}


def lesson(lab, title, level, html):
    LESSONS.append(dict(lab=lab, title=title, level=level, html=html))


def exercise(lab, title, level, question, answer):
    EXERCISES.append(dict(lab=lab, title=title, level=level, question=question, answer=answer))


lesson('orbite_kepler', 'Force centrale : du moment cinétique aux trois lois de Kepler', 'Sup → Spé', '''
<p>Choisir le système : une planète de masse m, assez petite pour que l’étoile de masse M soit immobile. Le référentiel lié à l’étoile est supposé galiléen. La force est <b>F=−GMm r/r³</b>, où r désigne le vecteur étoile–planète et r sa norme. L’origine de l’énergie potentielle est prise à l’infini.</p>
<p>Le moment de cette force par rapport à l’étoile est nul. Le théorème du moment cinétique donne L=m r×v constant. Le mouvement reste dans le plan perpendiculaire à L, et h=L/m=r²θ̇ est constant. La vitesse aréolaire, c’est-à-dire l’aire balayée par unité de temps, vaut h/2.</p>
<div class='formula'>ε=v²/2−GM/r ; h=r²θ̇ ; dA/dt=h/2.</div>
<p>Pour obtenir la trajectoire, poser u=1/r. L’équation de Binet donne u″+u=GM/h², les dérivées étant prises par rapport à θ. La solution est une conique, r=p/(1+e cosθ), avec p=h²/(GM). Le choix de θ=0 au péricentre fixe l’orientation de la conique.</p>
<div class='formula'>Pour une ellipse : p=a(1−e²), rp=a(1−e), ra=a(1+e), ε=−GM/(2a).</div>
<p>L’aire de l’ellipse vaut πab=πa²√(1−e²). En divisant par h/2, on obtient T²=4π²a³/(GM). Cette démarche relie explicitement le théorème du moment cinétique, l’énergie et les trois lois de Kepler. Une planète sur une ellipse excentrique ne tourne pas à vitesse uniforme.</p>''')
lesson('orbite_kepler', 'Passer de la trajectoire géométrique à la position au cours du temps', 'Spé · Prolongement', '''
<p>Échantillonner uniformément l’angle polaire ferait avancer la planète à une mauvaise vitesse. Pour calculer une position à l’instant t, on utilise un autre paramètre, <b>l’anomalie excentrique E</b>, qui repère un point de l’ellipse à partir de son cercle auxiliaire.</p>
<div class='formula'>x=a(cos E−e), y=a√(1−e²) sin E ; r=a(1−e cos E).</div>
<p>Le temps est relié à E par l’équation de Kepler : E−e sin E=nt, avec n=2π/T. Pour e&lt;1, sa dérivée 1−e cos E est strictement positive : il existe une unique solution pour chaque temps d’une période. La méthode de Newton consiste à corriger E par −(E−e sin E−nt)/(1−e cos E). Le laboratoire résout cette équation puis dérive les coordonnées pour calculer v.</p>
<div class='formula'>A(t)=½a²√(1−e²)(E−e sin E)=½ht.</div>
<p>Deux vérifications sont complémentaires : l’énergie et h doivent rester constants ; les aires balayées pendant T/12 doivent être égales. Une belle ellipse seule ne vérifie aucune de ces propriétés temporelles. Dans les unités de l’atelier, a=1 UA, M=1 masse solaire donne T=1 an et, à e=0, v=2π UA/an.</p>''')
exercise('orbite_kepler', 'Une comète : comparer les deux vitesses extrêmes', 'Sup',
         '<p>Une comète décrit une ellipse d’excentricité e=0,8. Exprimer le rapport vp/va entre les vitesses au péricentre et à l’apocentre. Faut-il connaître la masse de l’étoile ?</p>',
         '<p>Aux deux extrémités, la vitesse est tangentielle. La conservation de h donne rp vp=ra va. Comme rp=a(1−e) et ra=a(1+e), <b>vp/va=(1+e)/(1−e)=9</b>. La masse de l’étoile intervient dans chaque vitesse, mais se simplifie dans leur rapport.</p>')
exercise('orbite_kepler', 'Changer la taille de l’orbite', 'Sup → Spé',
         '<p>À masse centrale fixée, une deuxième planète a un demi-grand axe quatre fois plus grand. Comparer les périodes et les énergies spécifiques. L’excentricité change-t-elle ces rapports ?</p>',
         '<p>T²∝a³ donne T₂/T₁=4³ᐟ²=<b>8</b>. Comme ε=−GM/(2a), ε₂=ε₁/4 : l’énergie devient moins négative. Ces deux résultats ne dépendent pas de l’excentricité tant que les trajectoires restent elliptiques et la masse centrale identique.</p>')
exercise('orbite_kepler', 'Retrouver l’énergie avec les conditions au péricentre', 'Spé',
         '<p>On connaît rp et vp à un péricentre. Donner ε, h, a et e, puis la condition pour obtenir une ellipse. On suppose vp supérieur ou égal à la vitesse circulaire locale.</p>',
         '<p>ε=vp²/2−GM/rp et h=rp vp. Une ellipse exige ε&lt;0, donc vp&lt;√(2GM/rp). Le demi-grand axe vaut a=−GM/(2ε), puis e=1−rp/a. La condition vp≥√(GM/rp) garantit que rp est bien le rayon minimal. À égalité, e=0 ; en dessous, le point initial serait l’apocentre.</p>')

lesson('deux_corps', 'Système fermé, centre de masse et particule fictive', 'Sup → Spé', '''
<p>Le système est constitué de deux masses m₁ et m₂ qui n’échangent avec l’extérieur ni force ni matière. Les forces gravitationnelles internes sont opposées. Le théorème de la quantité de mouvement impose un mouvement rectiligne uniforme du centre de masse G. Le référentiel de G est donc galiléen.</p>
<p>Poser M=m₁+m₂, r=r₂−r₁ et μr=m₁m₂/M, la <b>masse réduite</b>. Dans le référentiel de G, la relation m₁r₁+m₂r₂=0 permet de retrouver les deux positions à partir de la seule séparation r :</p>
<div class='formula'>r₁=−(m₂/M)r ; r₂=(m₁/M)r.</div>
<p>Soustraire les deux équations du mouvement donne r̈=−GM r/r³. On peut aussi écrire μr r̈=−Gm₁m₂ r/r³ : la particule fictive de masse μr décrit un mouvement central. Ne pas confondre μr, qui est une masse, avec GM, qui est un paramètre gravitationnel de dimension longueur³/temps².</p>
<div class='formula'>T²=4π²a³/[G(m₁+m₂)] ; a₁=(m₂/M)a ; a₂=(m₁/M)a.</div>
<p>Le demi-grand axe a concerne l’orbite relative, donc a=a₁+a₂. Les deux étoiles ont la même période ; la plus massive décrit la plus petite ellipse autour de G.</p>''')
lesson('deux_corps', 'Énergie et moment cinétique : les deux décompositions de König', 'Spé', '''
<p>Dans un référentiel galiléen quelconque, écrire vi=VG+vi*. La condition ∑mivi*=0 annule le terme croisé dans ∑mi vi²/2. On sépare ainsi le mouvement d’ensemble et le mouvement autour du centre de masse.</p>
<div class='formula'>Ec=½M VG²+½μr vrelative².</div>
<p>Le premier terme décrit la translation de G ; le second décrit le mouvement relatif. L’énergie potentielle mutuelle est −Gm₁m₂/r, comptée <b>une seule fois</b> pour la paire. Dans le référentiel de G, l’énergie mécanique vaut donc E*=½μr ṙ²−Gm₁m₂/r.</p>
<div class='formula'>Ellipse relative : E*=−Gm₁m₂/(2a) ; L*=μr r×ṙ.</div>
<p>Pour le moment cinétique en un point fixe O, Lᵒ=OG×M VG+L*. Ce résultat se démontre par le même remplacement ri=OG+ri*. Par exemple, si m₁=m₂=m, chaque étoile est à distance r/2 de G : Ec*=2×½m(vrelative/2)²=½(m/2)vrelative². La masse réduite vaut bien m/2.</p>''')
exercise('deux_corps', 'Localiser le centre de masse d’un système binaire', 'Sup',
         '<p>À un instant, deux étoiles de masses 3m et m sont séparées de 4 unités de longueur. Donner leurs distances à G. Si la séparation décrit une ellipse de demi-grand axe 2, quels sont a₁ et a₂ ?</p>',
         '<p>Les distances à G sont inversement proportionnelles aux masses : l’étoile de masse 3m est à <b>1</b> et celle de masse m à <b>3</b>. Pour l’ellipse relative, a₁=(1/4)×2=0,5 et a₂=(3/4)×2=1,5. Le centre de masse est le foyer commun de leurs deux ellipses.</p>')
exercise('deux_corps', 'Mesurer une masse totale avec une orbite', 'Spé',
         '<p>Une binaire a une séparation de demi-grand axe a=2 UA et une période T=2 ans. Déterminer sa masse totale dans les unités du laboratoire. Pourquoi une seule période ne détermine-t-elle pas les deux masses séparément ?</p>',
         '<p>Avec G=4π², T²=a³/M ; donc <b>M=8/4=2 masses solaires</b>. Cette équation porte sur la somme m₁+m₂. Il faut une information supplémentaire, par exemple le rapport a₁/a₂=m₂/m₁ ou celui des vitesses, pour séparer les deux masses.</p>')
exercise('deux_corps', 'Une énergie dépendante du référentiel', 'Spé',
         '<p>Un système binaire isolé de masse totale M passe devant un observateur avec vitesse VG. Exprimer son énergie mécanique dans ce référentiel en fonction de son énergie E* dans le référentiel de G. Pourquoi la forme de l’orbite relative ne change-t-elle pas ?</p>',
         '<p>Le changement galiléen ajoute <b>½M VG²</b> à l’énergie cinétique totale ; la séparation et l’énergie potentielle ne changent pas. Ainsi E=E*+½M VG². L’équation de la séparation dépend uniquement de r₂−r₁ : elle conserve la même conique et la même période.</p>')

lesson('potentiel_effectif', 'Éliminer l’angle pour lire le mouvement radial', 'Spé', '''
<p>Une force centrale entraîne la conservation h=r²θ̇. Dans l’énergie spécifique, la vitesse en coordonnées polaires vérifie v²=ṙ²+r²θ̇². En remplaçant θ̇ par h/r², on obtient une énergie qui ne dépend plus que de r et de ṙ.</p>
<div class='formula'>ε=½ṙ²+Ueff(r) ; Ueff(r)=h²/(2r²)−GM/r.</div>
<p>Le terme h²/(2r²) traduit l’énergie du mouvement angulaire. Ce n’est pas une énergie potentielle gravitationnelle supplémentaire. Pour h≠0, il tend vers +∞ quand r tend vers zéro : le moment cinétique empêche d’atteindre le centre dans ce modèle ponctuel.</p>
<p>Le domaine accessible satisfait Ueff≤ε. Aux rayons où Ueff=ε, ṙ s’annule : le mouvement radial change de sens, sauf dans le cas de l’orbite circulaire. Si ε&lt;0, il existe deux rayons extrêmes ; si ε≥0, aucun rayon maximal ne borne la trajectoire.</p>
<div class='formula'>rc=h²/(GM) ; Ueff(rc)=−(GM)²/(2h²) ; Ueff″(rc)=(GM)⁴/h⁶&gt;0.</div>
<p>Le minimum définit une orbite circulaire stable. Le signe de la dérivée seconde renseigne sur la stabilité radiale, mais ne doit pas être interprété comme un amortissement : sans dissipation, les perturbations oscillent au lieu de disparaître.</p>''')
lesson('potentiel_effectif', 'Classer un lancement et étudier les petites oscillations radiales', 'Spé · Prolongement', '''
<p>À r₀=1 et GM=1, lancer tangentiellement avec vitesse η. On a h=η, ε=(η²−2)/2 et e=|η²−1|. Le seuil de l’échappement est η=√2. Le cercle est obtenu pour η=1 ; un lancement plus lent commence à l’apocentre, un lancement plus rapide commence au péricentre.</p>
<p>Pour un mouvement presque circulaire, écrire r=rc+ρ avec |ρ|≪rc. Au premier ordre, l’équation radiale r̈=−Ueff′(r) donne un oscillateur harmonique :</p>
<div class='formula'>ρ̈+ωr²ρ≈0 ; ωr²=Ueff″(rc)=GM/rc³.</div>
<p>La fréquence angulaire de l’orbite circulaire est également ωθ=√(GM/rc³). Cette égalité explique, au voisinage du cercle, pourquoi une révolution angulaire correspond à une oscillation radiale : l’ellipse se referme. Pour un autre potentiel central, ces deux fréquences ne sont généralement plus égales et l’orbite peut précesser.</p>
<p>Le graphique aide à lire les racines, mais la condition d’échappement se démontre par l’énergie : à l’infini Ueff tend vers zéro. Le cas ε=0 est une parabole, pas un mouvement rectiligne uniforme.</p>''')
exercise('potentiel_effectif', 'Lire une ellipse avec un lancement tangent', 'Sup → Spé',
         '<p>Dans les unités GM=r₀=1, prendre η=1,2. Déterminer ε, e, le demi-grand axe et les rayons extrêmes.</p>',
         '<p>ε=(1,44−2)/2=<b>−0,28</b>, e=1,44−1=<b>0,44</b> et a=−1/(2ε)=25/14≈1,786. Le lancement est au péricentre rp=1. L’apocentre vaut ra=a(1+e)=18/7≈2,571. Vérifier rp+ra=2a et p=h²=1,44.</p>')
exercise('potentiel_effectif', 'Une orbite circulaire est-elle un minimum d’énergie ?', 'Spé',
         '<p>À moment cinétique h fixé, déterminer le rayon et l’énergie de l’orbite circulaire dans un champ GM/r². Interpréter la dérivée seconde du potentiel effectif.</p>',
         '<p>Ueff′=−h²/r³+GM/r² s’annule en rc=h²/(GM). On y trouve εc=−(GM)²/(2h²) et Ueff″(rc)=(GM)⁴/h⁶&gt;0 : c’est un minimum à h fixé. Une petite perturbation radiale produit une oscillation de fréquence √(GM/rc³), et non un retour amorti vers le cercle.</p>')
exercise('potentiel_effectif', 'Une condition initiale trop lente', 'Spé',
         '<p>Le lancement est tangent à r₀=1, avec η=1/2 et GM=1. Le point initial est-il un péricentre ? Calculer le rayon minimal et expliquer pourquoi le centre n’est pas atteint.</p>',
         '<p>ε=−7/8 et e=3/4. Le point initial est l’apocentre. Le paramètre p=h²=1/4 donne <b>rmin=p/(1+e)=1/7</b>, tandis que rmax=p/(1−e)=1. Comme h≠0, Ueff tend vers +∞ en zéro : une énergie finie ne permet pas d’atteindre le centre.</p>')

lesson('transfert_hohmann', 'Deux changements de vitesse déterminés par l’énergie', 'Spé', '''
<p>Un transfert de Hohmann relie deux orbites circulaires concentriques, coplanaires et de même sens. Le véhicule quitte la première orbite par une impulsion tangentielle, parcourt une demi-ellipse puis reçoit une deuxième impulsion tangentielle. Les deux cercles sont tangents à l’ellipse.</p>
<div class='formula'>a=(r₁+r₂)/2 ; e=|r₂−r₁|/(r₁+r₂) ; vt(r)=√[GM(2/r−1/a)].</div>
<p>La vitesse circulaire au rayon r vaut vc(r)=√(GM/r). Au départ, Δv₁=vt(r₁)−vc(r₁). À l’arrivée, Δv₂=vc(r₂)−vt(r₂). Lors d’un transfert sortant, les deux impulsions accélèrent ; lors d’un transfert entrant, elles freinent. La quantité de carburant dépend du coût |Δv₁|+|Δv₂|, toujours positif.</p>
<div class='formula'>τ=π√(a³/GM) ; Δvtotal=|Δv₁|+|Δv₂|.</div>
<p>Exemple dans le scénario Terre : r₁=7 000 km et r₂=42 000 km donnent un demi-grand axe de 24 500 km et une durée d’environ 5,3 h. Les deux impulsions sont d’environ 2,33 et 1,43 km/s. La seconde est nécessaire : sans elle, le véhicule redescend le long de l’ellipse.</p>''')
lesson('transfert_hohmann', 'Un transfert interplanétaire exige aussi une condition de rendez-vous', 'Spé · Prolongement', '''
<p>Une trajectoire qui atteint le rayon orbital de Mars ne garantit pas qu’elle atteigne Mars. Dans le modèle circulaire, la planète cible tourne pendant le trajet. Si l’ellipse de transfert couvre un angle π et la planète cible tourne à la vitesse n₂, l’angle d’avance initial nécessaire est :</p>
<div class='formula'>φ₀=π−n₂τ modulo 2π ; n₂=√(GM/r₂³).</div>
<p>Pour r₁=1 UA et r₂=1,524 UA autour du Soleil, la durée est voisine de 259 jours et la planète cible doit se trouver environ 44° en avance au départ. Le laboratoire représente l’ellipse du véhicule, pas les mouvements synchronisés des deux planètes.</p>
<p>Les variations de vitesse sont calculées dans le référentiel de l’astre central. Le coût solaire d’une impulsion à 1 UA ne se confond pas avec le coût d’un départ depuis la surface terrestre : il faut prendre en compte les puits gravitationnels des planètes et les orbites de départ ou de capture.</p>
<p>Ce calcul forme à un enchaînement courant : géométrie des coniques, bilan d’énergie, période de Kepler, puis condition temporelle. Il illustre une famille de transferts à deux impulsions ; des transferts bi-elliptiques ou propulsés continûment demandent une comparaison supplémentaire.</p>
<p>Références de contexte : <a href='https://science.nasa.gov/resource/hohmann-transfer-orbit/' target='_blank' rel='noopener'>NASA : Hohmann Transfer Orbit</a> et <a href='https://pwg.gsfc.nasa.gov/stargaze/Smars2.htm' target='_blank' rel='noopener'>NASA GSFC : Flight to Mars, Calculations</a>.</p>''')
exercise('transfert_hohmann', 'Doubler le rayon orbital', 'Spé',
         '<p>Dans les unités GM=r₁=1, transférer un véhicule vers r₂=2. Calculer les deux impulsions et la durée du trajet.</p>',
         '<p>a=3/2. Au départ, vt₁=√(2−2/3)=2/√3 et vc₁=1, d’où Δv₁=2/√3−1≈0,155. À l’arrivée, vt₂=√(1−2/3)=1/√3 et vc₂=1/√2, d’où Δv₂≈0,130. Le coût vaut environ <b>0,284</b> et τ=π(3/2)³ᐟ²≈5,77 unités de temps.</p>')
exercise('transfert_hohmann', 'Omettre la seconde impulsion', 'Sup → Spé',
         '<p>Un transfert sortant atteint l’apocentre r₂. Si le moteur ne fonctionne plus, le véhicule reste-t-il sur l’orbite circulaire cible ? Justifier par l’énergie ou la vitesse.</p>',
         '<p>Non : vt₂²=GM(2/r₂−2/(r₁+r₂)) est inférieur à vc₂²=GM/r₂ lorsque r₂&gt;r₁. Le véhicule est trop lent pour une orbite circulaire à ce rayon. Son énergie et son moment cinétique restent ceux de l’ellipse : il repart vers son péricentre r₁.</p>')
exercise('transfert_hohmann', 'Préparer un rendez-vous avec la planète cible', 'Spé · Prolongement',
         '<p>Dans un transfert sortant, la demi-ellipse dure τ et la planète cible tourne à vitesse angulaire n₂ constante. Donner l’angle initial qui permet un rendez-vous au bout du transfert, puis expliquer pourquoi il faut attendre une fenêtre de départ.</p>',
         '<p>Fixer l’angle du véhicule à zéro au départ. Son arrivée a lieu à π. La planète doit satisfaire φ₀+n₂τ=π modulo 2π ; donc <b>φ₀=π−n₂τ</b>. Les deux planètes n’ont pas la même vitesse angulaire : leur angle relatif varie, et la condition ne se reproduit qu’à intervalles correspondant à leur période synodique.</p>')

lesson('diffusion_gravitationnelle', 'Une trajectoire hyperbolique à énergie positive', 'Spé', '''
<p>Dans le référentiel de l’astre, une sonde arrive avec vitesse v∞. La droite de sa trajectoire asymptotique se trouve à distance b de l’astre : b est le <b>paramètre d’impact</b>. L’énergie spécifique ε et le moment cinétique spécifique h sont fixés par ces conditions lointaines.</p>
<div class='formula'>ε=v∞²/2 ; h=bv∞ ; e=√[1+b²v∞⁴/(GM)²] &gt;1.</div>
<p>La conique r=p/(1+e cosθ), p=h²/(GM), tend vers l’infini lorsque 1+e cosθ=0. Les deux asymptotes donnent la déviation δ entre les directions entrante et sortante.</p>
<div class='formula'>δ=2arcsin(1/e)=2arctan[GM/(bv∞²)] ; rp=p/(1+e).</div>
<p>À b fixé, augmenter v∞ diminue la déviation : la sonde passe trop vite pour être fortement déviée. À v∞ fixé, réduire b augmente la déviation et diminue rp. Le modèle ponctuel n’empêche pas de passer à l’intérieur d’un astre réel : il faut donc contrôler séparément que rp reste supérieur au rayon matériel si l’on donne des unités physiques.</p>
<p>Sans moteur ni atmosphère, l’énergie mécanique est conservée et la vitesse lointaine sortante a la même norme v∞ que la vitesse lointaine entrante. Une accélération transitoire près du centre ne signifie pas un gain net d’énergie dans ce référentiel.</p>''')
lesson('diffusion_gravitationnelle', 'Assistance gravitationnelle : changer de référentiel pour comprendre le gain', 'Spé · Prolongement', '''
<p>Noter uin et uout les vitesses relatives à la planète à grande distance. Elles ont la même norme v∞, mais des directions différentes. Si la planète se déplace à vitesse V dans un autre référentiel galiléen, les vitesses de la sonde deviennent vin=uin+V et vout=uout+V.</p>
<div class='formula'>ΔEc/m=½(|uout+V|²−|uin+V|²)=V·(uout−uin).</div>
<p>Le produit scalaire peut être positif ou négatif. La même déviation peut donc faire gagner ou perdre de l’énergie selon le côté du passage et le sens du mouvement de la planète. Si V=0, le gain est nul : une planète immobile ne peut pas produire un gain net d’énergie cinétique lointaine.</p>
<p>Dans le modèle du laboratoire, la vitesse V de l’astre est prescrite et sa variation est négligée. Pour le système fermé planète–sonde, la variation de l’énergie de la sonde est compensée par celle de la planète ; le rapport des masses rend la modification de l’orbite de la planète très faible.</p>
<p>La méthode attendue est de ne pas mélanger les référentiels : déterminer d’abord la conique dans le référentiel de la planète, puis effectuer une composition des vitesses. <a href='https://www.esa.int/Enabling_Support/Operations/What_are_gravity_assists' target='_blank' rel='noopener'>ESA : What are gravity assists?</a></p>''')
exercise('diffusion_gravitationnelle', 'Une déviation de 90°', 'Spé',
         '<p>Déterminer b pour obtenir une déviation δ=π/2 à vitesse v∞ fixée dans le champ d’un astre de paramètre GM. Calculer l’excentricité correspondante.</p>',
         '<p>tan(δ/2)=GM/(bv∞²). Pour δ=π/2, tan(π/4)=1 ; donc <b>b=GM/v∞²</b>. Alors e=√2. Le péricentre vaut rp=(GM/v∞²)/(1+√2), plus petit que le paramètre d’impact b.</p>')
exercise('diffusion_gravitationnelle', 'La norme de la vitesse est-elle conservée ?', 'Sup → Spé',
         '<p>Une sonde possède vitesse lointaine v∞ et passe au rayon minimal rp. Exprimer sa vitesse vp au péricentre. Pourquoi retrouve-t-elle v∞ lorsqu’elle repart loin ?</p>',
         '<p>La conservation de ε donne vp²/2−GM/rp=v∞²/2, soit <b>vp=√(v∞²+2GM/rp)</b>. Elle accélère à l’approche, puis ralentit en s’éloignant. Quand r tend vers l’infini, le potentiel tend vers zéro et la vitesse retrouve la norme v∞.</p>')
exercise('diffusion_gravitationnelle', 'Borner le gain d’énergie d’un survol', 'Spé · Prolongement',
         '<p>La déviation vaut δ et les deux vitesses relatives ont norme v∞. Montrer que |ΔEc|/m≤2Vv∞sin(δ/2). Quand la borne peut-elle être atteinte ?</p>',
         '<p>La différence uout−uin est la corde entre deux vecteurs de même norme : sa norme vaut 2v∞sin(δ/2). Cauchy–Schwarz donne |V·(uout−uin)|≤V|uout−uin|, d’où la borne. L’égalité est obtenue lorsque V est parallèle ou antiparallèle à cette différence, selon le signe recherché.</p>')

lesson('marees', 'La marée est une différence de forces, pas la force gravitationnelle totale', 'Sup → Spé', '''
<p>Un corps et son centre de masse subissent ensemble l’attraction d’un astre extérieur. Ce mouvement commun ne les déforme pas. La déformation est liée à la <b>différence</b> entre le champ gravitationnel en un point du corps et le champ au centre.</p>
<p>Placer l’astre à distance D sur l’axe positif x. Pour un point d’abscisse x par rapport au centre, la différence d’accélération radiale vaut exactement :</p>
<div class='formula'>Δax=GM[(D−x)⁻²−D⁻²] ≈ (2GM/D³)x si |x|≪D.</div>
<p>La face proche, x&gt;0, est davantage accélérée vers l’astre ; la face éloignée, x&lt;0, l’est moins que le centre. Après soustraction du mouvement du centre, les deux faces s’éloignent de lui. On obtient ainsi un étirement suivant l’axe centre–astre.</p>
<div class='formula'>Dans le plan transverse : Δay≈−(GM/D³)y et Δaz≈−(GM/D³)z.</div>
<p>Le champ linéaire possède donc les trois coefficients (2,−1,−1)GM/D³. Le signe négatif transverse correspond à une compression. Leur somme est nulle, en accord avec la divergence nulle du champ gravitationnel dans une région qui ne contient pas la masse de l’astre.</p>''')
lesson('marees', 'Développement limité, ordre de grandeur et portée du modèle', 'Spé · Prolongement', '''
<p>La petite quantité du développement limité n’est pas la masse de l’astre : c’est le rapport R/D entre la taille du corps et la distance à l’astre. Le premier terme omis du champ radial est proportionnel à x²/D⁴. Pour un corps de rayon R, l’erreur relative du premier ordre est donc d’ordre R/D.</p>
<div class='formula'>Accélération de marée ≈2GMR/D³ ; gravité propre en surface =Gm/R².</div>
<p>Leur rapport est 2(M/m)(R/D)³. Il permet de repérer les situations où la différence d’attraction devient comparable à la cohésion gravitationnelle du corps. Cette comparaison fournit une échelle de distance, D/R≈(2M/m)¹ᐟ³, mais <b>pas une limite exacte de dislocation</b>.</p>
<p>Une limite de Roche pour un fluide doit inclure la rotation orbitale et le modèle d’équilibre ; un corps solide ajoute une résistance mécanique. Le laboratoire ne calcule ni équilibre fluide ni rupture. Les segments du dessin montrent le champ linéarisé, sans prétendre représenter la forme finale d’un corps.</p>
<p>L’étude relie mécanique, calcul différentiel et astrophysique : développer un champ vectoriel au voisinage d’un point, interpréter sa matrice de dérivées et vérifier le domaine de validité de l’approximation.</p>''')
exercise('marees', 'Changer la distance : attraction ou marée ?', 'Sup',
         '<p>À masse extérieure et taille du corps fixes, doubler D. Comment varient l’accélération du centre et l’accélération de marée au premier ordre ?</p>',
         '<p>L’accélération du centre vaut GM/D² : elle est divisée par <b>4</b>. La marée radiale est 2GMx/D³ : elle est divisée par <b>8</b>. Confondre attraction et différence d’attraction ferait donc prévoir la mauvaise loi d’échelle.</p>')
exercise('marees', 'Les deux côtés du corps ne sont pas parfaitement symétriques', 'Spé',
         '<p>Développer Δax=GM[(D−x)⁻²−D⁻²] à l’ordre deux en x/D. Comparer les valeurs en x=R et x=−R.</p>',
         '<p>(1−u)⁻²=1+2u+3u²+o(u²). Donc Δax=2GMx/D³+3GMx²/D⁴+o(x²). Le terme linéaire est impair ; le terme quadratique est positif des deux côtés. La face proche subit un étirement un peu plus fort que la face éloignée, à même distance R du centre.</p>')
exercise('marees', 'Une échelle de dislocation et ses limites', 'Spé · Prolongement',
         '<p>Un corps de masse m et de rayon R passe près d’un astre de masse M=100m. Estimer D/R lorsque la marée linéaire devient comparable à sa gravité propre. Cette estimation démontre-t-elle sa rupture ?</p>',
         '<p>Égaliser 2GMR/D³ et Gm/R² donne D/R=(2M/m)¹ᐟ³=200¹ᐟ³≈<b>5,85</b>. C’est un ordre de grandeur, pas un critère exact : rotation, propriétés mécaniques et dynamique de la déformation ne sont pas incluses. On vérifie aussi que R/D≈0,17 est seulement modérément petit.</p>')

lesson('fusee', 'Choisir un système fermé pour obtenir l’équation de la fusée', 'Sup → Spé', '''
<p>La fusée seule est un système ouvert : sa masse m diminue. Pour appliquer un bilan de quantité de mouvement, considérer entre t et t+dt le système fermé formé de la fusée et du gaz qui est éjecté pendant cette durée. La masse éjectée est −dm&gt;0.</p>
<p>Si la vitesse de la fusée est v et la vitesse relative d’éjection vers l’arrière est u&gt;0, la vitesse galiléenne du gaz est v−u. Au premier ordre, la variation de quantité de mouvement du système vaut m dv+u dm. Sous une pesanteur uniforme verticale descendante, elle est égale à −mg dt.</p>
<div class='formula'>m dv=−u dm−mg dt ; m dv/dt=uq−mg avec q=−dm/dt&gt;0.</div>
<p>La poussée est uq. On ne peut pas appliquer à la fusée seule l’équation d(mv)/dt=−mg sans ajouter le flux de quantité de mouvement du gaz. La formule d’un corps absorbant de la matière immobile dans un référentiel ne doit pas être utilisée pour une éjection à vitesse relative non nulle.</p>
<p>Sans pesanteur, intégrer dm/m entre m₀ et mf donne Δv=u ln(m₀/mf). À vitesse d’éjection fixée, c’est le rapport de masses qui détermine le gain, et non la seule masse de carburant en kilogrammes.</p>''')
lesson('fusee', 'Débit constant : vitesse, déplacement et pertes gravitationnelles', 'Spé', '''
<p>Avec un débit q constant et une durée de poussée τ, m(t)=m₀−qt et mf=m₀−qτ. À g constant et avec v(0)=0, l’intégration du bilan donne :</p>
<div class='formula'>v(t)=u ln[m₀/m(t)]−gt ; Δvfinal=u ln(m₀/mf)−gτ.</div>
<p>Le premier terme est le gain idéal. Le second est une perte de vitesse due à la pesanteur pendant la poussée. À même rapport de masses et même u, une durée plus courte diminue cette perte ; elle exige cependant un débit et une poussée plus élevés.</p>
<div class='formula'>z(t)−z₀=u{t+[m(t)/q]ln[m(t)/m₀]}−½gt².</div>
<p>On peut vérifier cette expression en la dérivant : les deux termes constants issus de la dérivée se simplifient et il reste u ln(m₀/m)−gt. L’accélération a=uq/m−g augmente au cours de la combustion puisque m diminue.</p>
<p>Exemple : u=3 000 m/s, m₀/mf=3 et τ=60 s donnent un gain idéal de 3 296 m/s. Sous g=9,8 m/s², la perte est 588 m/s et la vitesse finale environ 2 708 m/s. Le modèle ne prend pas en compte un sol, la traînée ou la diminution de g avec l’altitude.</p>''')
exercise('fusee', 'Quelle quantité de carburant pour un gain donné ?', 'Sup → Spé',
         '<p>Dans le vide sans pesanteur, une fusée a vitesse d’éjection u=3 km/s et doit gagner Δv=6 km/s. Déterminer m₀/mf et la fraction de la masse initiale qui doit être éjectée.</p>',
         '<p>Δv/u=ln(m₀/mf)=2, donc <b>m₀/mf=e²≈7,39</b>. La fraction éjectée vaut 1−mf/m₀=1−e⁻²≈86,5 %. Le logarithme explique pourquoi un gain de vitesse élevé devient coûteux en masse.</p>')
exercise('fusee', 'Peut-elle commencer par monter ?', 'Sup',
         '<p>Une fusée démarre avec vitesse nulle. Donner une condition sur la poussée F, la masse initiale m₀ et g pour que l’accélération initiale soit ascendante. Traduire-la avec le rapport χ=m₀/mf et la durée τ.</p>',
         '<p>Il faut <b>F&gt;m₀g</b>. Comme q=m₀(1−1/χ)/τ et F=uq, la condition est u(1−1/χ)/τ&gt;g. Si elle n’est pas satisfaite, le modèle sans sol prévoit d’abord une descente ; pour un lancement depuis un sol, une réaction du support doit alors être ajoutée.</p>')
exercise('fusee', 'Réduire la durée de combustion', 'Spé',
         '<p>Deux combustions ont les mêmes m₀, mf et u, mais des durées τ et τ/2. Comparer leurs vitesses finales sous pesanteur uniforme, puis leurs poussées.</p>',
         '<p>Le gain idéal u ln(m₀/mf) est identique. La seconde combustion perd seulement gτ/2, donc sa vitesse finale dépasse la première de <b>gτ/2</b>. Sa masse éjectée est identique en deux fois moins de temps : le débit, donc la poussée uq, est doublé.</p>')

lesson('coriolis', 'Composition des accélérations dans un référentiel tournant', 'Spé', '''
<p>Deux référentiels partagent une origine fixe. Le premier est galiléen ; les axes du second tournent à vitesse angulaire constante Ω autour de z. Pour un vecteur r, la dérivation dans les deux référentiels vérifie (dr/dt)I=(dr/dt)R+Ω×r.</p>
<p>Une seconde dérivation donne aI=aR+2Ω×vR+Ω×(Ω×r). Comme le point du laboratoire est libre, aI=0. L’observateur tournant peut donc écrire sa dynamique avec des forces d’inertie :</p>
<div class='formula'>m aR=−2mΩ×vR−mΩ×(Ω×r).</div>
<p>Le premier terme est la force de Coriolis, qui dépend de la vitesse relative. Le second est la force centrifuge, dirigée vers l’extérieur de l’axe. Pour r=(x,y,0), Ω=(0,0,Ω), leurs composantes divisées par m sont (2Ωvy,−2Ωvx) et Ω²(x,y).</p>
<p>Si Ω variait, il faudrait ajouter le terme d’Euler −mΩ̇×r. Si l’origine accélérait, un autre terme d’entraînement apparaîtrait. Le laboratoire fixe ces deux effets à zéro pour isoler la rotation uniforme.</p>''')
lesson('coriolis', 'Une vérification exacte par rotation des coordonnées', 'Spé · Prolongement', '''
<p>Dans le référentiel galiléen, un point libre de vitesse constante v₀ suivant x possède les coordonnées (x₀+v₀t,y₀). Un observateur tournant utilise une matrice de rotation d’angle −Ωt :</p>
<div class='formula'>xR=cos(Ωt)(x₀+v₀t)+sin(Ωt)y₀ ; yR=−sin(Ωt)(x₀+v₀t)+cos(Ωt)y₀.</div>
<p>Cette solution exacte permet de vérifier les signes des termes d’inertie. La norme de la position est conservée par la rotation, mais la vitesse relative n’a généralement pas la même norme que la vitesse galiléenne : elle contient aussi le terme −Ω×r.</p>
<p>La force de Coriolis ne travaille pas : son produit scalaire avec vR est nul. La force centrifuge dérive du potentiel −mΩ²(x²+y²)/2. Pour Ω constant, l’énergie dans le référentiel tournant possède donc un invariant :</p>
<div class='formula'>J=½m|vR|²−½mΩ²|r|² = constante.</div>
<p>Cette constante ne se confond pas avec l’énergie cinétique galiléenne ½mv₀². Elle s’exprime aussi J=EI−ΩLz,I pour ce mouvement libre. Le calcul entraîne à distinguer coordonnées, vitesses et référentiels dans les bilans.</p>''')
exercise('coriolis', 'Vérifier les signes du produit vectoriel', 'Sup → Spé',
         '<p>Un observateur tourne avec Ω&gt;0 autour de z. À un instant, le point a position (r,0,0) et vitesse relative (v,0,0), avec r,v&gt;0. Donner les directions des forces centrifuge et de Coriolis.</p>',
         '<p>Ω×vR=(0,Ωv,0), donc Fcor=(0,−2mΩv,0), vers les y négatifs. Ω×(Ω×r)=(−Ω²r,0,0), donc Fcent=(mΩ²r,0,0), vers les x positifs. Le terme centrifuge est radial vers l’extérieur ; Coriolis est perpendiculaire à la vitesse.</p>')
exercise('coriolis', 'Conserver une énergie dans les axes tournants', 'Spé',
         '<p>Montrer que J=½m|vR|²−½mΩ²|r|² est constant pour un point libre et Ω constant.</p>',
         '<p>Multiplier la dynamique tournante par vR. Le terme de Coriolis a un produit scalaire nul ; il reste d(½m|vR|²)/dt=mΩ²r·vR=d(½mΩ²|r|²)/dt. En soustrayant, <b>dJ/dt=0</b>. La constance de Ω est nécessaire pour cette forme du bilan.</p>')
exercise('coriolis', 'Un point immobile vu depuis des axes tournants', 'Spé',
         '<p>Dans le référentiel galiléen, un point est immobile à la distance r du centre. Quelles sont sa vitesse et son accélération dans les axes tournants ? Pourquoi la force centrifuge seule ne donne-t-elle pas le résultat ?</p>',
         '<p>vR=−Ω×r et aR=−Ω²r : les coordonnées décrivent un cercle en sens opposé aux axes. Le terme centrifuge vaut +Ω²r, mais Coriolis vaut −2Ω²r. Leur somme est bien −Ω²r. Omettre Coriolis inverserait donc le sens de l’accélération relative.</p>')


GUIDES = {
    'orbite_kepler': dict(
        purpose='Retrouver les lois de Kepler à partir de deux théorèmes, puis vérifier qu’une ellipse est parcourue à la bonne vitesse.',
        objects=['a : demi-grand axe de l’ellipse, en unités astronomiques ; e : excentricité, entre 0 et 1.', 'M : masse de l’étoile ; r : distance instantanée ; h : moment cinétique par unité de masse.', 'ε : énergie mécanique par unité de masse, avec énergie potentielle nulle à l’infini.'],
        hypotheses=['Référentiel lié à une étoile supposée fixe et galiléen.', 'Planète de masse négligeable ; interaction gravitationnelle seule.'],
        techniques=['Écrire un moment de force et conclure à la conservation de L.', 'Utiliser ε et h aux points extrêmes.', 'Relier l’aire d’une ellipse à la vitesse aréolaire.'],
        levels=dict(sup='Énergie mécanique, mouvement circulaire et unités.', spe='Force centrale, Binet, coniques et lois de Kepler.', beyond='Équation de Kepler et résolution numérique à temps uniforme.'),
        first_steps=['Choisir l’orbite presque circulaire et repérer la constance de r et de v.', 'Augmenter e sans changer a : comparer la période et les vitesses extrêmes.', 'Lire les douze aires et les écarts des bilans pour contrôler le mouvement calculé.'],
        expected='À a et M fixés, T et ε ne changent pas avec e. Les vitesses varient, mais les aires sur des durées égales restent égales.'),
    'deux_corps': dict(
        purpose='Choisir le bon système pour appliquer la quantité de mouvement et ramener deux trajectoires à une seule orbite relative.',
        objects=['m₁ et m₂ : masses des étoiles ; M=m₁+m₂.', 'q=m₂/m₁ : rapport des masses ; G : centre de masse.', 'r=r₂−r₁ : séparation ; a : demi-grand axe de cette séparation ; μr : masse réduite.'],
        hypotheses=['Système isolé composé de deux masses ponctuelles.', 'Référentiel de G galiléen ; pas de force extérieure.'],
        techniques=['Annuler la somme des forces internes dans un bilan global.', 'Résoudre les relations barycentriques.', 'Décomposer l’énergie cinétique et utiliser Kepler avec la masse totale.'],
        levels=dict(sup='Quantité de mouvement, centre de masse et interactions mutuelles.', spe='Masse réduite, théorèmes de König et mouvement central relatif.', beyond='Application à la mesure des masses des étoiles binaires.'),
        first_steps=['Choisir deux masses égales et comparer leurs deux ellipses.', 'Diminuer q : voir quelle étoile reste proche de G.', 'À masse totale constante, modifier q puis vérifier que la période ne change pas.'],
        expected='Le rapport des distances à G est inverse du rapport des masses. La période dépend de la masse totale ; la décomposition énergétique utilise la masse réduite.'),
    'potentiel_effectif': dict(
        purpose='Lire une trajectoire centrale à partir d’une courbe d’énergie : domaine accessible, rayons extrêmes, stabilité et échappement.',
        objects=['r₀=1 et GM=1 définissent les unités réduites.', 'η : vitesse tangentielle initiale divisée par la vitesse circulaire.', 'Ueff : énergie gravitationnelle plus énergie angulaire à h fixé ; ε : énergie spécifique du lancement.'],
        hypotheses=['Lancement tangent : la vitesse radiale initiale est nulle.', 'Astre ponctuel, force centrale conservative ; h reste constant.'],
        techniques=['Éliminer θ̇ grâce à h=r²θ̇.', 'Résoudre Ueff=ε et interpréter une racine.', 'Étudier un minimum par la dérivée seconde ; discuter le signe de ε.'],
        levels=dict(sup='Énergie et condition d’accessibilité.', spe='Potentiel effectif et classification des coniques.', beyond='Petites oscillations radiales et comparaison avec la fréquence orbitale.'),
        first_steps=['Choisir η=1 : la droite d’énergie touche le minimum du potentiel.', 'Choisir η=1,2 puis repérer les deux rayons extrêmes.', 'Passer à η=1,6 : constater l’absence de rayon maximal et ε>0.'],
        expected='Une vitesse inférieure à la vitesse circulaire commence à l’apocentre. L’échappement exige η≥√2 ; une énergie négative donne une orbite bornée.'),
    'transfert_hohmann': dict(
        purpose='Concevoir un changement d’orbite avec la relation de vis-viva, puis distinguer coût en vitesse et durée de transfert.',
        objects=['r₁ et r₂ : rayons des deux orbites circulaires, en multiples de L₀.', 'Δv₁ et Δv₂ : variations tangentielles signées ; leur somme en valeur absolue mesure le coût.', 'τ : temps de parcours de la demi-ellipse.'],
        hypotheses=['Orbites coplanaires et de même sens, astre unique.', 'Impulsions instantanées ; mouvement libre entre les deux.'],
        techniques=['Déterminer le demi-grand axe avec les deux rayons extrêmes.', 'Comparer vitesse elliptique et vitesse circulaire.', 'Employer une demi-période de Kepler et, en prolongement, une condition de rendez-vous.'],
        levels=dict(sup='Vitesse circulaire, énergie et ordres de grandeur.', spe='Coniques, relation énergétique de vis-viva et impulsions.', beyond='Fenêtres de transfert interplanétaire et limites de l’optimalité.'),
        first_steps=['Choisir un transfert terrestre vers une orbite haute : identifier les deux tangences.', 'Inverser les deux rayons : vérifier le signe des impulsions et le même coût total.', 'Choisir Soleil : calculer la durée en jours puis comparer à l’ordre de grandeur d’un trajet vers Mars.'],
        expected='Une ellipse seule ne remplace pas les deux impulsions : sans l’impulsion finale, le véhicule repasse par son orbite initiale.'),
    'diffusion_gravitationnelle': dict(
        purpose='Comprendre une assistance gravitationnelle en séparant le calcul dans le référentiel de l’astre et la composition des vitesses.',
        objects=['v∞ : vitesse relative loin de l’astre ; b : paramètre d’impact.', 'δ : angle entre les directions lointaines entrante et sortante ; rp : distance minimale.', 'V : vitesse de l’astre dans le second référentiel galiléen.'],
        hypotheses=['Masse de sonde négligeable, astre à vitesse prescrite.', 'Gravitation newtonienne sans atmosphère ni collision ; unités GM=1.'],
        techniques=['Fixer ε et h à grande distance.', 'Déterminer l’excentricité et les asymptotes d’une hyperbole.', 'Développer la différence de deux normes carrées après un changement galiléen.'],
        levels=dict(sup='Conservation de l’énergie et composition des vitesses.', spe='Hyperbole gravitationnelle et angle de déviation.', beyond='Gain ou perte d’énergie lors d’une assistance gravitationnelle.'),
        first_steps=['À v∞ fixé, réduire b et comparer δ et rp.', 'Mettre V=0 : le gain lointain doit disparaître.', 'Restaurer V puis inverser l’orientation du survol : comparer les gains signés.'],
        expected='La gravitation conserve l’énergie dans le référentiel de l’astre, mais la déviation peut modifier l’énergie cinétique dans un autre référentiel.'),
    'marees': dict(
        purpose='Passer du champ gravitationnel total à sa variation sur un corps, puis contrôler un développement limité par comparaison au champ exact.',
        objects=['R : rayon du corps, pris égal à 1 ; D/R : distance relative de l’astre.', 'q=M/m : rapport de la masse extérieure à la masse du corps.', 'Δa : accélération d’un point moins accélération du centre.'],
        hypotheses=['Champ instantané d’un astre ponctuel ; réponse du corps non calculée.', 'Approximation linéaire valable si R/D≪1.'],
        techniques=['Soustraire le mouvement commun du centre.', 'Développer (1−x/D)⁻² au premier ordre.', 'Comparer les lois en D⁻² et D⁻³ ; établir un rapport sans dimension.'],
        levels=dict(sup='Gravitation, différences de forces et analyse dimensionnelle.', spe='Développement limité d’un champ ; étirement et compression.', beyond='Matrice du champ de marée, trace nulle et ordre de grandeur d’une dislocation.'),
        first_steps=['Choisir le cas lointain et vérifier que champ exact et approximation se superposent.', 'Rapprocher l’astre : suivre l’écart sur la face proche.', 'Comparer les composantes radiale et transverse : leurs signes et leurs coefficients sont différents.'],
        expected='La marée varie comme D⁻³ et possède un effet sur les deux faces du corps. Le dessin montre un champ, pas une forme d’équilibre.'),
    'fusee': dict(
        purpose='Établir une équation de mouvement quand la masse varie, en indiquant explicitement la vitesse de la matière échangée.',
        objects=['m₀ et mf : masses initiale et finale ; χ=m₀/mf.', 'u : vitesse du gaz par rapport à la fusée ; q : débit de masse éjectée.', 'τ : durée de la poussée ; g : pesanteur uniforme.'],
        hypotheses=['Gaz éjecté à vitesse relative et débit constants.', 'Mouvement vertical, absence de traînée et de réaction d’un sol.'],
        techniques=['Construire un système fermé sur la durée dt.', 'Distinguer vitesse relative et galiléenne du gaz.', 'Intégrer un bilan avec masse variable ; comparer des pertes gravitationnelles.'],
        levels=dict(sup='Bilan de quantité de mouvement et logarithme.', spe='Système ouvert, flux de matière et évolution énergétique.', beyond='Compromis entre poussée, durée et masse de carburant.'),
        first_steps=['Choisir g=0 et vérifier le gain u ln(m₀/mf).', 'Ajouter la pesanteur : comparer les deux courbes de vitesse.', 'Diviser la durée par deux à rapport de masses inchangé : comparer la perte gτ et la poussée.'],
        expected='Le débit fixe la poussée ; le rapport des masses fixe le gain idéal. Une masse initiale plus grande, à même rapport et durée, donne la même vitesse finale.'),
    'coriolis': dict(
        purpose='Reconstruire un mouvement simple dans des axes tournants et vérifier les signes des deux forces d’inertie.',
        objects=['Ω : vitesse angulaire signée des axes autour de z.', 'v₀ : vitesse constante dans le référentiel galiléen ; vR : vitesse relative aux axes tournants.', '(x₀,y₀) : position initiale commune aux deux repères.'],
        hypotheses=['Point libre ; origine commune fixe ; rotation uniforme.', 'Aucune force réelle : toute accélération relative vient du changement de référentiel.'],
        techniques=['Composer puis dériver les vitesses.', 'Calculer Ω×v et Ω×(Ω×r) avec leurs signes.', 'Contrôler la somme des termes d’inertie et utiliser une rotation orthogonale.'],
        levels=dict(sup='Mouvement rectiligne uniforme et changement de coordonnées.', spe='Référentiel non galiléen, Coriolis et force centrifuge.', beyond='Invariant énergétique J dans une rotation uniforme.'),
        first_steps=['Choisir Ω=0 : retrouver une droite à vitesse constante.', 'Activer une rotation positive : lire séparément les deux termes d’inertie.', 'Changer Ω en −Ω et vérifier les sens puis l’identité des deux courbes de distance.'],
        expected='La trajectoire courbe appartient aux coordonnées tournantes. Coriolis dépend de la vitesse relative et ne travaille pas ; la force centrifuge seule ne suffit pas.')
}
