"""Cours et corrigés : chaque montage annonce ses grandeurs et son domaine."""

def lesson(lab,title,level,html):
    return dict(lab=lab,title=title,level=level,html=html)

def exercise(lab,title,level,question,answer):
    return dict(lab=lab,title=title,level=level,question=question,answer=answer)

LESSONS = [
lesson('ali_gain_bande','De l’ALI à un pôle au gain bouclé','Spé — physique PSI/PT',
    '<p>Un amplificateur linéaire intégré, ou ALI, compare ses tensions d’entrée v₊ et v₋, en volts. Sa tension différentielle est ε = v₊ − v₋ ; sa sortie est vₛ. Le gain différentiel statique A₀ est sans unité. Le modèle linéaire possède une fréquence de pôle fₚ, en hertz.</p>'
    '<p>Le symbole s représente une dérivation temporelle dans les équations linéaires à conditions initiales nulles. Pour un régime sinusoïdal de fréquence f, on remplace s par jω, avec j² = −1 et ω = 2πf, en rad/s.</p>'
    '<div class="formula">A(s) = A₀/(1 + s/ωₚ), avec ωₚ = 2πfₚ et fₜ = A₀fₚ.</div>'
    '<p>Dans un montage non inverseur, la borne positive reçoit l’entrée vₑ et la borne négative reçoit βvₛ. La fraction β est sans unité. Le gain demandé au modèle idéal est G = 1/β.</p>'
    '<div class="formula">H(s) = A(s)/(1 + βA(s)) = G₀/(1 + s/ω_c), G₀ = A₀/(1 + βA₀), f_c = fₚ(1 + βA₀), ω_c = 2πf_c.</div>'
    '<p>Le pôle bouclé est stable : une perturbation libre décroît exponentiellement. Le produit G₀f_c vaut exactement fₜ dans ce modèle. Augmenter le gain réduit donc la bande. La conservation du produit gain–bande est une capacité de physique PSI/PT.</p>'),
lesson('ali_gain_bande','Reconnaître les limites d’une amplification','Spé — physique PSI/PT ; décalage au-delà',
    '<p>La tension sinusoïdale d’entrée a une amplitude crête E, en volts, et une fréquence f, en hertz. L’amplitude crête linéaire de sortie est S = E|H(j2πf)|. La tension limite Vₛₐₜ est la valeur absolue d’un rail de sortie ; Iₘₐₓ est le courant maximal, en ampères ; Rₗ est la résistance de charge, en ohms.</p>'
    '<div class="formula">S ≤ Vₛₐₜ ; S/Rₗ ≤ Iₘₐₓ ; 2πfS ≤ SR.</div>'
    '<p>La vitesse de balayage SR est la pente maximale de sortie, en V/s, souvent annoncée en V/µs. Une sinusoïde qui exige une pente trop forte se déforme. Une petite charge peut provoquer une limitation de courant avant d’atteindre les rails de tension.</p>'
    '<p>La simulation conserve une tension de sortie comme état. Le modèle à un pôle fournit sa dérivée ; la vitesse de balayage borne cette dérivée, puis les rails arrêtent l’excursion. Le modèle reste causal : la sortie dépend de son état précédent. Le diagramme de Bode ne décrit que le régime linéaire.</p>'
    '<p>Le réglage Vₒₛ, en volts, ajoute un décalage à l’entrée différentielle. Son effet statique est G₀Vₒₛ avant saturation. Ce prolongement est fourni pour explorer une limite du modèle ; la tension de décalage et les courants de polarisation sont explicitement exclus du programme de physique PSI/PT.</p>'),
lesson('suiveur_cascade','Pourquoi un filtre charge le précédent','Sup — physique PTSI ; approfondissement en spé',
    '<p>Deux cellules passe-bas possèdent des résistances R₁ et R₂, en ohms, et des condensateurs C₁ et C₂, en farads. Chaque résistance est en série avec le signal et chaque condensateur est relié à la masse. L’entrée est vₑ, la sortie finale vₛ, en volts. On note H = vₛ/vₑ en régime sinusoïdal et s = j2πf, où f est la fréquence en hertz et j² = −1.</p>'
    '<p>Lorsque les cellules sont directement reliées, la seconde absorbe un courant au nœud de la première. Sa tension n’est donc plus celle de la première cellule étudiée seule. Les lois des nœuds donnent :</p>'
    '<div class="formula">H(s) = 1/[1 + s(R₁C₁ + R₂C₂ + R₁C₂) + s²R₁R₂C₁C₂].</div>'
    '<p>Le terme R₁C₂ traduit cette charge mutuelle. Le produit des deux fonctions de transfert isolées oublie ce terme et ne convient pas à ce branchement. En PTSI, le programme demande d’expliquer l’intérêt d’une forte impédance d’entrée et d’une faible impédance de sortie lors d’une association de filtres.</p>'),
lesson('suiveur_cascade','Le suiveur transmet une tension et fournit le courant','Sup — application accompagnée ; spé — ALI idéal',
    '<p>Le suiveur reçoit la tension de la première cellule à sa borne positive. Sa sortie est directement reliée à sa borne négative. Pour un ALI idéal en régime linéaire stable, v₊ = v₋ et les courants d’entrée sont nuls : sa tension de sortie égale sa tension d’entrée.</p>'
    '<p>Avec R₁, R₂ en ohms, C₁, C₂ en farads et s = j2πf, les cellules deviennent indépendantes :</p>'
    '<div class="formula">H(s) = 1/[(1 + sR₁C₁)(1 + sR₂C₂)].</div>'
    '<p>Le suiveur ne crée aucun gain de tension ; il prélève idéalement une tension sans courant et fournit le courant demandé par l’étage suivant, grâce à son alimentation. Un suiveur réel conserve des limites de bande, de tension et de courant.</p>'
    '<p>Une expérience statique complémentaire emploie un capteur de tension à vide V, en volts, de résistance interne Rₛ, en ohms, et un appareil de lecture de résistance Rₗ, en ohms. La lecture directe vaut VRₗ/(Rₛ + Rₗ). Un suiveur idéal transmet V ; il doit toutefois pouvoir fournir V/Rₗ à la charge.</p>'),
lesson('sommateur_inverseur','Établir une somme pondérée par la loi des nœuds','Sup — lois des circuits ; spé — ALI idéal',
    '<p>Les tensions vₑ₁ et vₑ₂, en volts, atteignent la borne inverseuse d’un ALI par les résistances R₁ et R₂, en ohms. La résistance Rf, en ohms, relie cette borne à la sortie vₛ. La borne positive est reliée à la masse.</p>'
    '<p>En régime linéaire idéal, les deux bornes sont au même potentiel et aucun courant ne pénètre dans l’ALI. La borne inverseuse est donc au potentiel nul ; elle n’est pas reliée matériellement à la masse.</p>'
    '<div class="formula">vₑ₁/R₁ + vₑ₂/R₂ + vₛ/Rf = 0 ; vₛ = −Rf(vₑ₁/R₁ + vₑ₂/R₂).</div>'
    '<p>Les coefficients −Rf/R₁ et −Rf/R₂ sont les poids sans unité. Une petite résistance d’entrée donne un poids plus grand. Le signe négatif vient de la contre-réaction sur la borne inverseuse. Chaque source voit ici sa propre résistance d’entrée.</p>'),
lesson('sommateur_inverseur','Superposition et domaine linéaire du sommateur','Sup — signaux périodiques ; spé — saturation',
    '<p>La première entrée est E₁ sin(2πft) et la seconde E₂ sin(4πft + φ). Les amplitudes E₁ et E₂ sont des valeurs crêtes, en volts ; f est une fréquence en hertz ; t est le temps en secondes ; φ est une phase en radians. Le montage linéaire additionne les deux contributions sans créer de nouvelle fréquence.</p>'
    '<p>Les résistances R₁, R₂ et Rf sont en ohms. Une borne suffisante de la tension de sortie est :</p>'
    '<div class="formula">|vₛ| ≤ Rf(E₁/R₁ + E₂/R₂).</div>'
    '<p>Cette borne est une majoration : les deux sinusoïdes n’atteignent pas nécessairement leurs extrema ensemble. Si elle est inférieure au rail Vₛₐₜ, en volts, l’excursion en tension est possible dans le modèle idéal. Si elle le dépasse, il faut examiner la courbe.</p>'
    '<p>La saturation rend l’opération non linéaire et produit des harmoniques supplémentaires. Le tracé de ce laboratoire limite la somme instantanément aux rails pour montrer cet effet ; il ne simule pas la réponse dynamique d’un ALI réel.</p>'),
lesson('integrateur_derivateur','Intégrer ou dériver : vérifier le signe et la condition initiale','Sup — filtrage ; spé — intégrateur à ALI',
    '<p>La résistance R est en ohms, la capacité C en farads ; l’entrée vₑ et la sortie vₛ sont en volts. Dans un intégrateur inverseur idéal, R est à l’entrée et C en rétroaction. Dans un dérivateur inverseur idéal, C est à l’entrée et R en rétroaction. Le produit RC est un temps, en secondes.</p>'
    '<div class="formula">Intégrateur : dvₛ/dt = −vₑ/(RC). Dérivateur : vₛ = −RC dvₑ/dt.</div>'
    '<p>Pour l’intégrateur, il faut donner vₛ(0) avant de calculer la sortie. Le laboratoire choisit vₛ(0) = 0. Avec vₑ(t) = E sin(ωt), E en volts et ω = 2πf en rad/s, la sortie vaut E[cos(ωt) − 1]/(ωRC). La constante −E/(ωRC) impose le départ à zéro.</p>'
    '<p>Un dérivateur donne −ERCω cos(ωt). Son gain croît avec la fréquence ; un intégrateur idéal a au contraire un gain 1/(RCω). Ces modèles n’ont ni rails ni limitation de pente : leurs grandes tensions signalent que le modèle doit être complété.</p>'),
lesson('integrateur_derivateur','Le dérivateur amélioré évite un gain illimité','Spé — analyse de montage ; technique accompagnée',
    '<p>La branche d’entrée contient le condensateur C, en farads, en série avec R, en ohms. La rétroaction contient R′, en ohms, en parallèle avec C′, en farads. La borne positive est à la masse. Les tensions vₑ et vₛ sont en volts ; H est leur rapport complexe. En régime sinusoïdal, s = jω, avec ω = 2πf en rad/s et j² = −1.</p>'
    '<div class="formula">Zₑ = R + 1/(sC), Zf = R′/(1 + sR′C′), H = −Zf/Zₑ = −R′Cs/[(1 + RCs)(1 + R′C′s)].</div>'
    '<p>Le signe est fixé par le montage inverseur. Si ωRC et ωR′C′ sont petits, H ≈ −jωR′C : la sortie approche −R′C dvₑ/dt. Les fréquences de pôle sont 1/(2πRC) et 1/(2πR′C′), en hertz.</p>'
    '<p>À très haute fréquence, le gain décroît comme 1/ω. La résistance d’entrée et la capacité de rétroaction évitent l’amplification illimitée du dérivateur idéal. Cela aide à réduire la sensibilité aux variations rapides, mais ne remplace pas l’étude de la bande de l’ALI réel.</p>'),
lesson('schmitt_trigger','Retrouver les deux seuils du Schmitt inverseur','Spé — physique PSI/PT',
    '<p>La tension d’entrée vₑ, en volts, est appliquée à la borne négative de l’ALI. La résistance R₁ relie la sortie à la borne positive ; R₂ relie cette borne à la masse. Les résistances sont en ohms. Les sorties saturées valent ±Vₛₐₜ, en volts. La fraction β = R₂/(R₁ + R₂) est sans unité.</p>'
    '<div class="formula">v₊ = βvₛ, ε = v₊ − vₑ.</div>'
    '<p>Une sortie positive exige ε > 0. Elle subsiste donc tant que vₑ < βVₛₐₜ ; en montée, elle bascule vers −Vₛₐₜ au seuil +βVₛₐₜ. Une sortie négative exige ε < 0 ; en descente, elle bascule vers +Vₛₐₜ au seuil −βVₛₐₜ.</p>'
    '<p>La rétroaction positive entretient la saturation au lieu d’établir une égalité des deux entrées. On ne peut donc pas imposer v₊ = v₋ pour ce montage. Le cycle à deux seuils est une capacité de physique PSI/PT.</p>'),
lesson('schmitt_trigger','Mémoire et protection contre de petits franchissements','Spé — physique PSI/PT',
    '<p>Le Schmitt possède un seuil haut Uₕ et un seuil bas Uᵦ, en volts. Ici Uₕ = βVₛₐₜ et Uᵦ = −βVₛₐₜ, avec β une fraction sans unité et Vₛₐₜ le niveau positif de sortie. La largeur Uₕ − Uᵦ vaut 2βVₛₐₜ.</p>'
    '<p>Entre les seuils, deux états de sortie sont possibles. La valeur de l’entrée ne suffit pas : il faut son histoire. On décrit le circuit par une tension d’entrée et un état mémorisé.</p>'
    '<p>Une rampe triangulaire de crête E, en volts, et de fréquence f, en hertz, est parcourue dans les deux sens. Le réglage de bruit ajoute une sinusoïde de crête N, en volts, à la fréquence 23f. Si cette perturbation ne permet pas d’atteindre le seuil opposé après un basculement, elle ne provoque pas de retour immédiat.</p>'
    '<p>Le cycle entrée–sortie se parcourt dans le temps. Une courbe horizontale lorsque E reste sous les seuils est un résultat normal : le circuit conserve l’état initial choisi.</p>'),
lesson('astable','Charge exponentielle entre deux seuils','Spé — physique PSI/PT, oscillateur de relaxation',
    '<p>Le condensateur de capacité C, en farads, reçoit la sortie vₛ à travers R₁, en ohms. Sa tension v_C est appliquée à la borne négative. La borne positive reçoit la commande continue Vₑ à travers R₂ et la sortie à travers R₃. Toutes les tensions sont en volts et toutes les résistances en ohms.</p>'
    '<p>On pose τ = R₁C, en secondes, β = R₂/(R₂ + R₃), sans unité, et h = (1 − β)Vₑ, en volts. Les deux seuils sont L = h − βVₛₐₜ et U = h + βVₛₐₜ. Vₛₐₜ est le niveau positif de saturation.</p>'
    '<div class="formula">τ dv_C/dt + v_C = vₛ ; v_C(t) = vₛ + [v_C(0) − vₛ] exp(−t/τ) lorsque vₛ reste constant.</div>'
    '<p>À sortie positive, le condensateur monte du seuil L vers U. Au seuil U, la sortie devient négative ; le condensateur descend alors vers L. On relie ainsi la loi du condensateur aux conditions de basculement du comparateur.</p>'),
lesson('astable','Période, rapport cyclique et arrêt des oscillations','Spé — physique PSI/PT',
    '<p>Les seuils L et U, en volts, sont définis par le diviseur de rétroaction. La sortie prend ±Vₛₐₜ, en volts ; τ = R₁C est la constante de temps en secondes. Les durées t₊ et t₋ sont celles des sorties positive et négative.</p>'
    '<div class="formula">t₊ = τ ln[(Vₛₐₜ − L)/(Vₛₐₜ − U)] ; t₋ = τ ln[(U + Vₛₐₜ)/(L + Vₛₐₜ)].</div>'
    '<p>La période T vaut t₊ + t₋, la fréquence vaut 1/T et la fraction du temps au niveau positif vaut t₊/T. À commande nulle, h = 0 : les deux durées sont égales.</p>'
    '<div class="formula">T = 2R₁C ln[(1 + β)/(1 − β)] pour Vₑ = 0.</div>'
    '<p>Pour des basculements en temps fini, il faut −Vₛₐₜ < L < U < Vₛₐₜ. Dans ce montage cela équivaut à |Vₑ| < Vₛₐₜ. Au seuil d’arrêt, une cible du condensateur et un seuil coïncident : l’approche est asymptotique et la période tend vers l’infini.</p>'),
lesson('wien','Phase nulle et gain critique du pont de Wien','Spé — physique PSI/PT, oscillateur quasi sinusoïdal',
    '<p>Le pont possède une branche série R₁–C₁ et une branche parallèle R₂–C₂ reliée à la masse. Les résistances sont en ohms et les capacités en farads. La tension de sortie de l’amplificateur est v₂ ; le pont transmet v₁ à son entrée positive. Le rapport B = v₁/v₂ est sans unité. En régime sinusoïdal, s = jω avec ω = 2πf en rad/s et j² = −1.</p>'
    '<div class="formula">B(s) = R₂C₁s/[1 + (R₁C₁ + R₂C₂ + R₂C₁)s + R₁R₂C₁C₂s²].</div>'
    '<p>La phase du pont est nulle à ω₀ = 1/√(R₁R₂C₁C₂). Son gain y vaut 1/Gcrit, avec Gcrit = 1 + R₁/R₂ + C₂/C₁. Un amplificateur non inverseur possède un gain G = 1 + R/R₃ ; R et R₃ sont ses résistances de contre-réaction, en ohms.</p>'
    '<div class="formula">Au seuil sinusoïdal : G = Gcrit, soit R/R₃ = R₁/R₂ + C₂/C₁.</div>'
    '<p>Pour deux branches identiques, la fréquence vaut 1/(2πRC) et le gain critique vaut 3. La simulation permet aussi d’explorer un pont dissymétrique.</p>'),
lesson('wien','Démarrage et rôle des non-linéarités','Spé — physique PSI/PT ; enveloppe accompagnée',
    '<p>On note a = R₁C₁ + R₂C₂ + R₂C₁, en secondes, b = R₂C₁, en secondes, et d = R₁R₂C₁C₂, en secondes carrées. La tension de sortie vₛ est en volts ; G est le gain sans unité de l’amplificateur. Le circuit linéaire bouclé vérifie :</p>'
    '<div class="formula">d vₛ″ + (a − Gb)vₛ′ + vₛ = 0.</div>'
    '<p>Si G est inférieur à a/b, les perturbations s’éteignent. Si G est supérieur, le coefficient d’amortissement est négatif et elles croissent. Au seuil, le modèle linéaire conserve une oscillation, mais ne sélectionne pas une amplitude.</p>'
    '<p>Le tracé emploie une amplitude A, en volts, avec une petite valeur initiale, et une fréquence fixée à ω₀/(2π). Près du seuil, son taux de croissance approché est γ = (Gb − a)/(2d), en s⁻¹. Pour illustrer une stabilisation, on fournit le modèle d’enveloppe A′ = γA(1 − A²/Vlim²) lorsque γ est positif. Vlim est une amplitude conventionnelle en volts.</p>'
    '<p>Ce modèle qualitatif respecte le démarrage et la limitation, mais ne représente pas le mécanisme précis d’une lampe, de diodes ou d’un ALI saturé. Une réalisation réelle fixe son amplitude par sa propre non-linéarité et produit éventuellement des harmoniques.</p>'),
lesson('redresseur_precision','Compenser le seuil de diode par la contre-réaction','Spé — application d’ALI ; montage accompagné',
    '<p>L’entrée e, en volts, rejoint la borne inverseuse par une résistance R₁. Deux branches de rétroaction comportent R₂ et R₃ ainsi que deux diodes opposées. Les trois résistances, en ohms, sont égales. Les tensions vₛ₁ et vₛ₂ sont les sorties des deux branches ; la tension utile est leur différence vₛ₂ − vₛ₁.</p>'
    '<p>Une seule diode conduit à chaque alternance. Lorsque la contre-réaction peut établir le régime linéaire, la borne inverseuse reste au potentiel nul. Pour e > 0, la branche correspondante donne vₛ₁ = −e et vₛ₂ = 0. Pour e < 0, l’autre donne vₛ₁ = 0 et vₛ₂ = −e.</p>'
    '<div class="formula">vₛ₂ − vₛ₁ = |e|.</div>'
    '<p>Le seuil Vᴅ, en volts, est compensé par une excursion supplémentaire de la sortie interne de l’ALI. Le seuil subsiste dans cette tension interne, mais pas dans la différence utile tant que le régime linéaire reste possible.</p>'),
lesson('redresseur_precision','Petits signaux et marge d’alimentation du redresseur','Sup — diodes ; spé — limites d’ALI',
    '<p>Une sinusoïde d’entrée possède une amplitude crête E, en volts. Chaque diode est représentée par un seuil constant Vᴅ, en volts, sans résistance dynamique. Un pont passif traverse deux diodes et fournit max(|e| − 2Vᴅ, 0) dans ce modèle.</p>'
    '<p>Le redresseur à ALI demande une tension interne de valeur absolue |e| + Vᴅ. Avec des rails symétriques ±Vₛₐₜ, sa marge s’écrit :</p>'
    '<div class="formula">E + Vᴅ ≤ Vₛₐₜ.</div>'
    '<p>Une entrée de 0,2 V crête peut donc être redressée par le montage de précision avec des diodes de seuil 0,6 V ; le pont passif ne conduit jamais. Une entrée trop grande ne peut plus être compensée.</p>'
    '<p>Ce laboratoire est quasi statique. Le passage entre les diodes force un changement rapide de la tension interne de l’ALI. Dans une expérience réelle, sa vitesse de balayage, sa bande et sa récupération peuvent créer une erreur de passage par zéro, même si l’alimentation est suffisante.</p>'),
lesson('filtre_etat','Des lois des nœuds au passe-bande à trois ALI','Spé — filtre actif ; calcul accompagné du montage',
    '<p>Les résistances R₁ à R₆ sont en ohms et les deux condensateurs ont la même capacité C, en farads. La tension d’entrée est vₑ. Le premier ALI fournit vₛ₁, le second fournit la sortie vₛ, le troisième fournit vₛ₂ ; toutes ces tensions sont en volts.</p>'
    '<div class="formula">vₛ = −(R₅/R₄)vₛ₁ = −R₆C dvₛ₂/dt ; (R₂/R₁)vₑ + (R₂/R₃)vₛ₂ = −vₛ₁ − R₂C dvₛ₁/dt.</div>'
    '<p>En régime sinusoïdal de pulsation ω = 2πf, en rad/s, le nombre j vérifie j² = −1. On définit le gain central H₀, sans unité, la pulsation centrale ω₀, en rad/s, et le facteur de qualité Q, sans unité.</p>'
    '<div class="formula">H₀ = R₂R₅/(R₁R₄), ω₀ = √[R₅/(R₃R₄R₆)]/C, Q = R₂Cω₀ ; H(jω) = H₀/[1 + jQ(ω/ω₀ − ω₀/ω)].</div>'
    '<p>Le filtre atténue les très basses et les très hautes fréquences. Son gain maximal est H₀ à ω₀. Les bornes à −3 dB, ω₁ et ω₂, sont les pulsations où le gain vaut H₀/√2. Leur différence Δω est exactement 1/(R₂C), et ω₁ω₂ = ω₀².</p>'),
lesson('filtre_etat','Filtrer chaque harmonique d’un créneau','Sup — spectre fourni ; spé — filtrage actif',
    '<p>Le créneau impair prend +E pendant la première demi-période et −E pendant la suivante. E est son amplitude crête, en volts ; Tₑ est sa période, en secondes ; sa pulsation fondamentale vaut ωₑ = 2π/Tₑ, en rad/s. On note k un entier positif.</p>'
    '<div class="formula">vₑ(t) = Σₖ Aₖ sin(kωₑt) + Bₖ cos(kωₑt) ; Aₖ = 4E/(πk) pour k impair, Aₖ = 0 pour k pair, Bₖ = 0.</div>'
    '<p>La parité impaire annule les coefficients cosinus ; l’alternance entre les deux demi-périodes annule les harmoniques paires. Le calcul ne garde qu’un nombre choisi de termes impairs, avec leurs coefficients exacts.</p>'
    '<p>Si H(jkωₑ) possède un module hₖ et une phase φₖ, la contribution de sortie vaut Aₖhₖ sin(kωₑt + φₖ). On ne peut pas multiplier tout le créneau par un gain unique.</p>'
    '<p>Une approximation simple garde seulement les harmoniques dont la pulsation est entre les bornes ω₁ et ω₂ de la bande à −3 dB. Le filtre réel du modèle laisse aussi passer les autres, avec atténuation : la simulation compare la somme complète calculée et cette approximation. Elle affiche également les deux états vₛ₁ et vₛ₂ ; les vérifier permet de détecter un ALI qui saturerait en pratique.</p>'),
lesson('transistor_polarisation','Fixer le point de repos d’un NPN','Au-delà — physique PSI/PT ; modèle fourni',
    '<p>Ce prolongement étudie un transistor NPN amplificateur. Il ne correspond pas à la seule fonction d’interrupteur d’une chaîne de puissance. Le collecteur est relié à l’alimentation Vcc par Rc ; l’émetteur est relié à la masse par Re. La base reçoit un pont : Rb₁ vers la masse et Rb₂ vers l’alimentation. Les résistances sont en ohms et les tensions en volts.</p>'
    '<p>Le gain en courant β est sans unité. Le modèle fourni fixe la tension base–émetteur à Vbe = 0,7 V lorsqu’elle conduit. Le pont de base équivaut à une source Vth = Vcc Rb₁/(Rb₁ + Rb₂), de résistance Rth = Rb₁Rb₂/(Rb₁ + Rb₂).</p>'
    '<div class="formula">Ib = (Vth − Vbe)/[Rth + (β + 1)Re] ; Ic = βIb ; Ve = (β + 1)IbRe ; Vc = Vcc − RcIc.</div>'
    '<p>Les courants Ib et Ic sont en ampères, Ve et Vc en volts. Ces formules supposent le régime actif. Si Vth ne peut établir la jonction, le transistor est bloqué. Si Vc − Ve descend sous la valeur fournie Vce,sat = 0,2 V, il est saturé : Ic = βIb cesse d’être valable. On résout alors les courants avec les deux tensions de jonction imposées.</p>'),
lesson('transistor_polarisation','Amplifier une petite variation autour du repos','Au-delà — modèle petit signal accompagné',
    '<p>Le transistor doit être en régime actif au repos. Le courant de repos Ic, en ampères, fixe la transconductance gm = Ic/Uₜ, en siemens. On fournit Uₜ = 25,85 mV. Le gain en courant β, sans unité, donne la résistance d’entrée interne rπ = β/gm, en ohms.</p>'
    '<p>La résistance d’émetteur Re est éventuellement découplée par Ce, en farads. Le générateur de petite tension e possède une résistance Rg ; un condensateur C₁ le relie à la base. La charge alternative Rₗ est couplée sans modifier le repos. Toutes les résistances sont en ohms.</p>'
    '<p>Pour s = j2πf, avec f en hertz et j² = −1, l’impédance d’émetteur est Ze = Re/(1 + sReCe) si Ce est connecté, et Ze = Re sinon. L’entrée du transistor vaut rπ + (β + 1)Ze ; elle est en parallèle avec la résistance du pont de base.</p>'
    '<div class="formula">Sans atténuation d’entrée : H = −β(Rc ∥ Rₗ)/[rπ + (β + 1)Ze].</div>'
    '<p>Le symbole ∥ désigne une association parallèle. Le signe négatif traduit l’inversion à l’émetteur commun. Un découplage efficace augmente le gain, mais réduit l’amplitude d’entrée admissible. Le modèle ignore les capacités internes et l’effet Early : il ne prédit pas le comportement à haute fréquence. Hors régime actif, le calcul petit signal est désactivé.</p>')
]

EXERCISES = [
exercise('ali_gain_bande','Calculer le produit gain–bande','Spé — physique PSI/PT',
    '<p>Un ALI a un gain différentiel statique A₀ = 100 000 et une fréquence de transition fₜ = 1,00 MHz. Le diviseur de rétroaction impose un gain idéal G = 10. Calculer le gain statique bouclé G₀ et sa bande à −3 dB f_c, puis leur produit.</p>',
    '<p>La fréquence du pôle libre vaut fₚ = fₜ/A₀ = 10,0 Hz. Avec β = 1/G = 0,1 : G₀ = A₀/(1 + βA₀) = 9,9990 et f_c = fₚ(1 + βA₀) = 100 010 Hz. Le produit G₀f_c vaut exactement 1 000 000 Hz dans le modèle à un pôle. L’approximation G₀ ≈ G donne f_c ≈ 100 kHz.</p>'),
exercise('ali_gain_bande','Distinguer une limite de pente d’un rail','Spé — physique PSI/PT',
    '<p>Une sortie sinusoïdale serait de 8,0 V crête à 10,0 kHz. Les rails valent ±12 V et la vitesse de balayage maximale SR vaut 0,050 V/µs. La sinusoïde peut-elle être reproduite ? Quelle amplitude maximale une sinusoïde à cette fréquence pourrait-elle avoir ?</p>',
    '<p>La pente maximale requise vaut 2πfS = 502 655 V/s = 0,503 V/µs : dix fois la pente disponible. Les rails permettent 8 V, mais la vitesse de balayage ne le permet pas. Une sinusoïde à 10 kHz doit satisfaire S ≤ SR/(2πf) = 0,796 V crête. Cette borne concerne une sinusoïde ; une sortie déformée peut avoir une autre amplitude et contenir des harmoniques.</p>'),
exercise('ali_gain_bande','Prévoir la limitation par une petite charge','Spé — physique PSI/PT',
    '<p>Un ALI possède des rails ±12 V et un courant maximal de sortie Iₘₐₓ = 10 mA. Il alimente une résistance Rₗ = 100 Ω et devrait fournir 5 V crête. Quel plafond de tension impose la charge ?</p>',
    '<p>La loi d’Ohm impose |vₛ| ≤ IₘₐₓRₗ = 0,010 × 100 = 1,0 V. La prédiction de 5 V demanderait 50 mA. Le plafond effectif est min(12 V, 1 V) = 1 V : la saturation en courant apparaît avant les rails de tension. Remplacer Rₗ par 1 kΩ élève le plafond de courant à 10 V.</p>'),
exercise('suiveur_cascade','Comparer deux cellules identiques à leur fréquence propre','Sup — physique PTSI',
    '<p>Deux cellules identiques possèdent une résistance R et une capacité C. À la pulsation ω = 1/(RC), calculer le module et la phase de la fonction de transfert avec et sans un suiveur idéal entre les cellules. On donne Hsans = 1/[1 + 3jωRC − (ωRC)²].</p>',
    '<p>À ωRC = 1, Hsans = 1/(3j) = −j/3 : son module vaut 1/3 et sa phase −90°. Avec suiveur, Havec = 1/(1 + j)² = 1/(2j) = −j/2 : son module vaut 1/2 et sa phase −90°. Les phases coïncident à cette fréquence, mais les amplitudes diffèrent de 50 %. La seconde cellule charge la première lorsqu’elles sont directement reliées.</p>'),
exercise('suiveur_cascade','Lire un capteur sans perdre sa tension','Sup — physique PTSI',
    '<p>Un capteur possède une tension à vide de 2,00 V et une résistance interne Rₛ = 100 kΩ. L’appareil de lecture possède Rₗ = 10 kΩ. Calculer la lecture directe, puis la lecture avec un suiveur idéal.</p>',
    '<p>La lecture directe est 2 × 10/(100 + 10) = 0,1818 V, soit 9,09 % de la tension à vide. Le suiveur idéal ne prélève pas de courant sur le capteur et restitue 2,00 V. Il doit fournir à l’appareil 2/10 000 = 0,200 mA ; cette demande doit être compatible avec un suiveur réel.</p>'),
exercise('suiveur_cascade','Tester la multiplication des transferts','Spé — physique PSI/PT',
    '<p>Deux filtres isolés ont pour transferts H₁ et H₂. Un étudiant écrit toujours Htotal = H₁H₂ lorsqu’il les relie. Quelle condition manque ? Comment un suiveur idéal la réalise-t-il ?</p>',
    '<p>Le premier filtre doit conserver son transfert sous la charge du second. Une forte impédance d’entrée du second devant l’impédance de sortie du premier permet cette approximation. Le suiveur idéal réalise une impédance d’entrée infinie et une impédance de sortie nulle : le premier ne fournit aucun courant au second, et les transferts se multiplient. La seule existence de deux étages ne suffit pas à justifier le produit.</p>'),
exercise('sommateur_inverseur','Retrouver le signe d’une somme continue','Spé — ALI idéal',
    '<p>Un sommateur inverseur utilise R₁ = 10 kΩ, R₂ = 20 kΩ et Rf = 20 kΩ. Les entrées continues valent vₑ₁ = 0,30 V et vₑ₂ = −0,40 V. Calculer la sortie en régime linéaire.</p>',
    '<p>La loi des nœuds donne vₛ = −(20/10) × 0,30 − (20/20) × (−0,40) = −0,20 V. L’entrée négative fournit une contribution positive à la sortie ; l’entrée positive donne une contribution négative. Les poids sont −2 et −1, sans unité.</p>'),
exercise('sommateur_inverseur','Choisir les poids par les résistances','Spé — montage accompagné',
    '<p>On souhaite vₛ = −3vₑ₁ − 2vₑ₂ avec une résistance de rétroaction Rf = 60 kΩ. Quelles résistances d’entrée R₁ et R₂ choisir ? Quel courant prélève la première entrée lorsque vₑ₁ = 1 V ?</p>',
    '<p>Les rapports imposent R₁ = Rf/3 = 20 kΩ et R₂ = Rf/2 = 30 kΩ. La borne inverseuse est au potentiel nul dans le régime linéaire idéal. La première source fournit donc 1/20 000 = 50 µA. L’impédance d’entrée de ce montage est finie : ce sommateur ne remplace pas un suiveur.</p>'),
exercise('sommateur_inverseur','Repérer quand la formule linéaire cesse de s’appliquer','Spé — saturation',
    '<p>Un sommateur utilise R₁ = R₂ = 10 kΩ, Rf = 100 kΩ et des rails ±12 V. Les entrées continues valent 3,0 V et 0,50 V. Calculer la prédiction linéaire et la sortie du modèle quasi statique limité. Peut-on encore imposer v₋ = 0 dans le circuit réel ?</p>',
    '<p>La prédiction vaut −10(3,0 + 0,50) = −35 V. Le modèle limité affiche −12 V. Le circuit est saturé ; le gain infini ne permet plus d’égaliser les entrées. On ne doit donc pas continuer à utiliser une masse virtuelle pour obtenir tous les courants du circuit saturé. La courbe limitée illustre la perte de linéarité, sans décrire les états internes de l’ALI réel.</p>'),
exercise('integrateur_derivateur','Conserver la constante d’intégration','Spé — physique PSI/PT',
    '<p>Un intégrateur idéal a R = 10 kΩ et C = 10 nF. Son entrée est vₑ(t) = E sin(2πft), avec E = 1,00 V et f = 1,00 kHz. La sortie est nulle à t = 0. Calculer sa valeur à un quart de période, puis à une demi-période.</p>',
    '<p>RC = 100 µs et 2πfRC = 0,628319. La sortie est vₛ(t) = E[cos(2πft) − 1]/(2πfRC). À T/4, elle vaut −1,5915 V ; à T/2, elle vaut −3,1831 V. La seule expression 1,5915 cos(2πft) omettrait la constante initiale et ne partirait pas de zéro.</p>'),
exercise('integrateur_derivateur','Vérifier un dérivateur amélioré en basse fréquence','Spé — analyse du montage',
    '<p>Un dérivateur amélioré possède R = 10 kΩ, C = 10 nF, R′ = 100 kΩ et C′ = 1 nF. L’entrée a une amplitude de 1 V et une fréquence f = 100 Hz. Calculer l’amplitude de sortie et la comparer à la dérivée approchée.</p>',
    '<p>Les deux temps valent RC = R′C′ = 100 µs et R′C = 1,00 ms. Le transfert est −j2πfR′C/(1 + j2πfRC)². Son module vaut 0,628319/[1 + 0,0628319²] = 0,62585. La sortie fait donc 0,62585 V crête. La dérivée approchée donnerait 0,62832 V. Sa phase exacte vaut −90° − 2 arctan(0,0628319) = −97,19° : le signe inverseur doit être conservé.</p>'),
exercise('integrateur_derivateur','Expliquer l’atténuation à très haute fréquence','Spé — filtrage',
    '<p>On donne H(s) = −R′Cs/[(1 + RCs)(1 + R′C′s)]. Les résistances sont en ohms, les capacités en farads. Trouver l’équivalent de H(jω) lorsque les deux produits ωRC et ωR′C′ sont très grands. Quelle pente de gain en décibels en déduire ?</p>',
    '<p>Le dénominateur devient RCR′C′s². Ainsi H(s) ≈ −1/(RC′s), donc H(jω) ≈ j/(RC′ω). Le module décroît comme 1/ω : chaque multiplication par dix de la fréquence réduit le gain de 20 dB. Les deux protections remplacent la croissance illimitée du dérivateur idéal par une atténuation à haute fréquence.</p>'),
exercise('schmitt_trigger','Calculer les seuils et leur largeur','Spé — physique PSI/PT',
    '<p>R₁ = 20 kΩ relie la sortie à l’entrée positive ; R₂ = 10 kΩ relie cette entrée à la masse. Les niveaux de sortie sont ±12 V et l’entrée est appliquée à la borne négative. Trouver les seuils en montée et en descente.</p>',
    '<p>La fraction de sortie est β = 10/(20 + 10) = 1/3. En montée, une sortie +12 V bascule à vₑ = +4,0 V vers −12 V. En descente, une sortie −12 V bascule à vₑ = −4,0 V vers +12 V. La largeur de l’hystérésis est 8,0 V.</p>'),
exercise('schmitt_trigger','Deux sorties possibles pour une même entrée','Spé — mémoire',
    '<p>Les seuils d’un Schmitt sont −4 V et +4 V. L’entrée triangulaire reste entre −3 V et +3 V. Prévoir la sortie si l’état initial vaut +12 V, puis si l’état initial vaut −12 V.</p>',
    '<p>Le signal n’atteint aucun seuil de basculement. Une sortie initiale +12 V demeure +12 V ; une sortie initiale −12 V demeure −12 V. Les deux expériences possèdent la même entrée, mais des sorties différentes. L’état initial constitue la mémoire indispensable à la description du circuit.</p>'),
exercise('schmitt_trigger','Garantir l’absence de commutations parasites','Spé — manipulation accompagnée',
    '<p>Les seuils sont ±4 V. Une entrée de valeur absolue au plus 1,0 V reçoit une perturbation de valeur absolue au plus 0,7 V. Un basculement est-il possible, quel que soit l’état initial ?</p>',
    '<p>L’inégalité triangulaire donne |vₑ| ≤ 1,0 + 0,7 = 1,7 V, strictement inférieur à 4 V. Aucun seuil ne peut être atteint. L’état initial est donc conservé, que la perturbation soit sinusoïdale ou quelconque sous la borne fournie. Ce résultat dépend d’une borne d’amplitude, et non d’une fréquence supposée pour le bruit.</p>'),
exercise('astable','Trouver la période à commande nulle','Spé — physique PSI/PT',
    '<p>Un astable possède R₁ = 10 kΩ, C = 100 nF, R₂ = 10 kΩ et R₃ = 20 kΩ. La commande est nulle et les niveaux de sortie valent ±12 V. Calculer la période et la fréquence.</p>',
    '<p>τ = R₁C = 1,00 ms et β = R₂/(R₂ + R₃) = 1/3. La période est T = 2τ ln[(1 + β)/(1 − β)] = 2 ms × ln 2 = 1,3863 ms. La fréquence vaut 721,35 Hz. Les deux demi-périodes valent 0,69315 ms. Le niveau de saturation fixe les seuils, mais se simplifie dans cette expression de T.</p>'),
exercise('astable','Décaler les durées avec une commande continue','Spé — physique PSI/PT',
    '<p>Reprendre τ = 1 ms, β = 1/3 et Vₛₐₜ = 12 V, avec une commande Vₑ = 5 V. Calculer les seuils, les deux durées et la fraction du temps au niveau positif.</p>',
    '<p>h = (1 − β)Vₑ = 10/3 V. Les seuils sont L = −2/3 V et U = 22/3 V. La charge positive dure t₊ = 1 ms × ln(19/7) = 0,99853 ms ; la charge négative dure t₋ = 1 ms × ln(29/17) = 0,53408 ms. T = 1,53261 ms et t₊/T = 65,15 %. Une commande positive prolonge ici l’état de sortie positif.</p>'),
exercise('astable','Comprendre l’arrêt au seuil de commande','Spé — relaxation',
    '<p>Pourquoi la formule de période ne doit-elle plus être appliquée comme un nombre fini lorsque |Vₑ| atteint Vₛₐₜ ? Que montre la simulation au-delà de cette limite ?</p>',
    '<p>Un seuil devient égal à la tension vers laquelle charge le condensateur. Une charge exponentielle approche sa cible sans l’atteindre en temps fini : une des durées diverge. Au-delà, le seuil est hors de l’intervalle accessible et le cycle s’arrête. La simulation affiche une sortie saturée constante et une fréquence égale à zéro, valeur qui signale l’absence d’oscillation.</p>'),
exercise('wien','Calculer le seuil pour un pont identique','Spé — physique PSI/PT',
    '<p>Les deux résistances du pont valent R = 10 kΩ et ses deux capacités valent C = 10 nF. Trouver la fréquence sélectionnée et le gain critique. Pour un amplificateur non inverseur de gain 1 + Rf/Rg, choisir le rapport Rf/Rg au seuil.</p>',
    '<p>La fréquence est f₀ = 1/(2πRC) = 1591,55 Hz. Le gain critique vaut 1 + 1 + 1 = 3. L’amplificateur doit donc avoir Rf/Rg = 2 au seuil. Pour démarrer à partir d’une petite perturbation, son gain initial doit être légèrement supérieur à 3 ; une non-linéarité doit ensuite stabiliser l’amplitude.</p>'),
exercise('wien','Vérifier un pont dissymétrique','Spé — montage accompagné',
    '<p>Le pont a R₁ = 20 kΩ, R₂ = 10 kΩ, C₁ = 10 nF et C₂ = 20 nF. Calculer f₀ et Gcrit. La règle « gain égal à 3 » reste-t-elle valable ?</p>',
    '<p>√(R₁R₂C₁C₂) = 200 µs, donc f₀ = 1/(2π × 200 µs) = 795,77 Hz. Le gain critique vaut 1 + R₁/R₂ + C₂/C₁ = 1 + 2 + 2 = 5. Le gain 3 conviendrait seulement à deux branches identiques. À gain 3, ce pont dissymétrique ne peut pas démarrer une oscillation dans le modèle linéaire.</p>'),
exercise('wien','Séparer condition de démarrage et amplitude finale','Spé — non-linéarités',
    '<p>Pour un pont identique avec RC = 100 µs, le gain est G = 3,06. Estimer le taux de croissance initial γ près du seuil. Le modèle linéaire permet-il de prévoir une amplitude finale ?</p>',
    '<p>On a a = 3RC, b = RC et d = (RC)². Donc γ ≈ (G − 3)/(2RC) = 0,06/(200 µs) = 300 s⁻¹. L’enveloppe est multipliée par e en environ 3,33 ms au début. Le modèle linéaire continue à croître sans sélectionner d’amplitude. Le plateau du laboratoire vient d’une loi d’enveloppe non linéaire explicitement fournie ; il n’est pas déduit du gain critique.</p>'),
exercise('redresseur_precision','Redresser une tension plus petite que le seuil','Sup — diodes ; spé — ALI',
    '<p>Une entrée sinusoïdale a E = 0,20 V crête. Les diodes ont Vᴅ = 0,60 V. Comparer un pont passif et le redresseur de précision à trois résistances égales ; les rails de l’ALI valent ±12 V.</p>',
    '<p>Le pont passif exige deux seuils, soit 1,20 V : il ne conduit jamais et sa sortie est nulle dans ce modèle. Le redresseur de précision fournit |e|, donc 0,20 V crête. Son ALI doit produire jusqu’à E + Vᴅ = 0,80 V en interne, valeur compatible avec les rails ±12 V. Ce raisonnement est quasi statique.</p>'),
exercise('redresseur_precision','Retrouver la sortie différentielle par alternance','Spé — montage accompagné',
    '<p>Les trois résistances sont égales. En régime compensé, calculer vₛ₁, vₛ₂ et vₛ₂ − vₛ₁ pour e = +0,40 V, puis pour e = −0,40 V.</p>',
    '<p>Pour e = +0,40 V, la branche négative donne vₛ₁ = −0,40 V et vₛ₂ = 0 : la différence vaut +0,40 V. Pour e = −0,40 V, l’autre branche donne vₛ₁ = 0 et vₛ₂ = +0,40 V : la différence vaut encore +0,40 V. Le résultat utile est une différence de deux tensions, et non la seule sortie interne de l’ALI.</p>'),
exercise('redresseur_precision','Évaluer la marge de compensation','Spé — limites d’ALI',
    '<p>Les rails de sortie valent ±3,0 V, le seuil de chaque diode vaut 0,60 V et l’entrée atteint 5,0 V crête. Quelle amplitude reste compensable ? Quelle crête montre le modèle quasi statique ?</p>',
    '<p>La compensation exige |e| + 0,60 ≤ 3,0 V, donc |e| ≤ 2,40 V. La crête utile du modèle limité vaut 2,40 V au lieu des 5,0 V idéaux. Augmenter la fréquence ne corrige pas ce manque de marge ; une expérience rapide peut ajouter une autre erreur, liée à la vitesse ou à la récupération de l’ALI.</p>'),
exercise('filtre_etat','Calculer les caractéristiques du filtre à trois ALI','Spé — physique PSI/PT, montage accompagné',
    '<p>R₁ = R₃ = R₄ = R₅ = R₆ = 10 kΩ, R₂ = 30 kΩ et C = 10 nF. Calculer H₀, ω₀, Q et la largeur de bande en hertz.</p>',
    '<p>H₀ = R₂R₅/(R₁R₄) = 3. Avec des résistances de 10 kΩ dans la formule de fréquence, ω₀ = 1/(10 kΩ × 10 nF) = 10 000 rad/s, soit f₀ = 1591,55 Hz. Q = R₂Cω₀ = 3. Δω = 1/(R₂C) = 3333,33 rad/s ; Δf = Δω/(2π) = 530,52 Hz. Une largeur exprimée en rad/s ne doit pas être confondue avec celle en hertz.</p>'),
exercise('filtre_etat','Isoler le troisième harmonique du créneau','Sup — spectre fourni ; spé — filtre actif',
    '<p>Un créneau impair a une crête E = 1 V. Sa fondamentale vaut fₑ = f₀/3. Le filtre a H₀ = 3 et Q = 3 ; on suppose que seul le troisième harmonique appartient à sa bande à −3 dB. Trouver la sortie obtenue en ne gardant que ce terme.</p>',
    '<p>Le coefficient du troisième harmonique est A₃ = 4E/(3π) = 0,42441 V. Il est exactement à la fréquence centrale, où H = H₀ = 3, réel positif. La sortie approchée est donc vₛ(t) ≈ (4/π) sin(2πf₀t) V, de crête 1,27324 V. La sortie calculée avec toutes les harmoniques comporte aussi les contributions atténuées hors de la bande ; elles ne sont pas nulles.</p>'),
exercise('filtre_etat','Modifier la bande sans déplacer le centre','Spé — réglage de filtre',
    '<p>Dans ce filtre, on double uniquement R₂. Que deviennent ω₀, H₀, Q et Δω ? Peut-on dire que seul le facteur de qualité change ?</p>',
    '<p>La formule de ω₀ ne contient pas R₂ : le centre est inchangé. H₀ est proportionnel à R₂ et double ; Q = R₂Cω₀ double également ; Δω = 1/(R₂C) est divisée par deux. La bande se resserre, mais le gain central augmente aussi. Comparer des sorties sans prendre en compte cette amplification ferait attribuer à tort tout l’effet à la sélection fréquentielle.</p>'),
exercise('transistor_polarisation','Calculer le repos avant le petit signal','Au-delà — modèle fourni',
    '<p>Un NPN a Vcc = 12 V, Rb₁ = 10 kΩ vers la masse, Rb₂ = 47 kΩ vers l’alimentation, Re = 1 kΩ, Rc = 2,2 kΩ et β = 100. On fournit Vbe = 0,7 V et le seuil de saturation Vce,sat = 0,2 V. Calculer le courant de collecteur et vérifier le régime.</p>',
    '<p>Vth = 12 × 10/57 = 2,10526 V et Rth = 10 × 47/57 = 8,24561 kΩ. Ib = (2,10526 − 0,7)/(8,24561 kΩ + 101 kΩ) = 12,863 µA. Ic ≈ 1,2863 mA, Ve ≈ 1,2992 V et Vc ≈ 9,1701 V. Vce ≈ 7,871 V, très supérieur à 0,2 V : le régime actif supposé est cohérent. La résistance du pont n’a pas été négligée.</p>'),
exercise('transistor_polarisation','Comparer gain découplé et gain avec Re','Au-delà — modèle petit signal fourni',
    '<p>Le courant de repos vaut Ic = 1,00 mA, β = 100 et Rc = 2,00 kΩ ; la sortie n’est pas chargée. On fournit Uₜ = 25,85 mV. Le générateur impose directement la petite tension de base. Trouver le gain avec émetteur découplé, puis avec Re = 1,00 kΩ non découplée.</p>',
    '<p>gm = Ic/Uₜ = 0,038685 S et rπ = β/gm = 2585 Ω. Avec découplage idéal, le gain vaut −gmRc = −77,37. Sans découplage, il vaut −βRc/[rπ + (β + 1)Re] = −200 000/(2585 + 101 000) = −1,9308. Le découplage augmente beaucoup le gain ; cette comparaison suppose un générateur idéal, sans atténuation au pont de base ni au condensateur de liaison.</p>'),
exercise('transistor_polarisation','Refuser un petit signal autour d’un repos saturé','Au-delà — validation du modèle',
    '<p>Un calcul avec Ic = βIb donne Vc − Ve = −0,5 V pour un NPN et une alimentation positive. Peut-on utiliser ce courant pour calculer gm = Ic/Uₜ et prédire une amplification ? Quelle démarche suivre ?</p>',
    '<p>Cette tension contredit le régime actif supposé : le transistor est saturé avant ce point. On ne doit pas calculer un amplificateur petit signal autour de cette solution fictive. Il faut résoudre le repos avec les tensions de jonction du modèle saturé, puis modifier le pont, Rc ou Re pour retrouver un régime actif avec de la marge de tension. Le laboratoire désactive sa réponse petit signal quand le repos est bloqué ou saturé.</p>')
]


GUIDES = {
'ali_gain_bande': dict(
    purpose='Séparer trois causes de déformation d’une sortie amplifiée : bande finie, limites de tension ou de courant, et vitesse de balayage.',
    objects=['ALI : composant qui compare v₊ et v₋ et produit vₛ ; ces tensions et l’entrée vₑ sont en volts. La rétroaction est négative.',
             'G est le gain idéal demandé ; A₀ le gain différentiel statique ; β = 1/G la fraction réinjectée. Ces trois nombres sont sans unité.',
             'f est la fréquence d’entrée, fₜ la fréquence de transition et f_c la bande bouclée, en hertz ; le contrôle f et fₜ est affiché en kHz. ω = 2πf est en rad/s.',
             'E est l’amplitude crête d’entrée et Vₛₐₜ le rail positif, en volts ; Rₗ est la résistance de charge en ohms ; Iₘₐₓ le courant limite, affiché en mA.',
             'SR est la pente maximale de sortie, affichée en V/µs ; Vₒₛ est le décalage d’entrée affiché en mV. Le temps t est affiché en ms.',
             'G₀ est le gain statique bouclé sans unité. Le symbole s représente la dérivation du modèle ; j² = −1 et s = jω en régime sinusoïdal.'],
    hypotheses=['ALI à un pôle, résistance d’entrée infinie et résistance de sortie nulle ; charge résistive.', 'État de sortie initialement nul ; pente et rails appliqués pendant la propagation causale de cet état.', 'Le diagramme de Bode reste celui du modèle linéaire ; le décalage est un prolongement fourni.'],
    techniques=['Boucler un gain à un pôle par un diviseur de rétroaction.', 'Comparer une excursion de tension, un courant de charge et une pente.', 'Lire un gain à −3 dB et vérifier les unités du produit gain–bande.'],
    levels=dict(sup='PTSI : gain complexe, ordre 1, régime sinusoïdal et loi d’Ohm.',spe='Physique PSI/PT : modèle d’ALI, produit gain–bande, saturation et limites de courant et de balayage.',beyond='Décalage d’entrée ; il est exclu des contenus de physique PSI/PT et reste ici accompagné.'),
    first_steps=['Choisir le régime linéaire et multiplier le gain demandé par quatre : suivre la bande.', 'Choisir « Pente limitée » puis augmenter SR : observer le retour vers une sinusoïde.', 'Choisir « Courant limité » puis augmenter Rₗ : prévoir le nouveau plafond IₘₐₓRₗ.'],
    expected='Justifier quelle limite agit en premier et distinguer le gain linéaire d’une sortie déformée.'),
'suiveur_cascade': dict(
    purpose='Vérifier quand les fonctions de transfert de deux étages peuvent se multiplier et mesurer l’intérêt d’un suiveur.',
    objects=['Une cellule RC possède une résistance en série et un condensateur vers la masse ; R₁ et R₂ sont affichées en kΩ, C₁ et C₂ en nF.',
             'vₑ et vₛ sont les tensions d’entrée et de sortie, en volts ; E est la crête d’entrée ; f la fréquence en hertz ; t le temps affiché en ms.',
             'Le suiveur reçoit la première tension à sa borne positive ; sa sortie rejoint sa borne négative. Il transmet la tension et fournit le courant au second étage.',
             'H est le rapport complexe sortie/entrée, sans unité ; s = j2πf et j² = −1. Les fréquences propres 1/(2πRC) sont en hertz.',
             'Une seconde expérience statique possède un capteur de résistance interne Rₛ et une lecture de résistance Rₗ, affichées en kΩ. Leur rapport fixe la perte à la lecture.'],
    hypotheses=['Deux condensateurs idéaux, sortie finale non chargée et régime sinusoïdal établi.', 'Suiveur idéal, sans courant d’entrée ni limite de courant de sortie ; les limites réelles se testent dans le laboratoire ALI.', 'Les paramètres de capteur servent à une comparaison statique indépendante des cellules RC.'],
    techniques=['Écrire deux lois des nœuds et repérer le courant prélevé par l’étage suivant.', 'Comparer un transfert chargé au produit de deux transferts isolés.', 'Employer un diviseur de tension pour estimer la perturbation d’une mesure.'],
    levels=dict(sup='Physique PTSI : intérêt des impédances lors d’une cascade, filtre du premier ordre et fonctions de transfert fournies.',spe='Physique PSI/PT : relation entrée–sortie du suiveur et association des filtres.',beyond='Dimensionnement de la charge, des courants et de la bande d’un suiveur réel.'),
    first_steps=['Choisir deux cellules identiques à leur fréquence propre : comparer les amplitudes.', 'Augmenter R₁ devant R₂ : observer la perturbation due au second étage.', 'Choisir la lecture d’un capteur : prévoir la perte puis la comparer au suiveur idéal.'],
    expected='Expliquer avec les impédances et les courants pourquoi une cascade peut changer le transfert de ses étages.'),
'sommateur_inverseur': dict(
    purpose='Construire une somme de deux signaux dont les poids et les signes sont prévisibles par la loi des nœuds.',
    objects=['Les tensions d’entrée vₑ₁ et vₑ₂ et la sortie vₛ sont en volts ; E₁ et E₂ sont les amplitudes crêtes des deux entrées.',
             'R₁ et R₂ relient les deux sources à la borne inverseuse ; Rf assure la contre-réaction. Leurs valeurs sont affichées en kΩ.',
             'La borne positive est à la masse. En régime linéaire idéal, la borne inverseuse est au potentiel nul sans liaison directe à la masse.',
             'La première entrée est à la fréquence f, en hertz ; la seconde à 2f avec une phase φ affichée en degrés. Le temps t est affiché en ms.',
             'Vₛₐₜ est la limite de tension de sortie, en volts ; les poids −Rf/R₁ et −Rf/R₂ sont sans unité.'],
    hypotheses=['ALI idéal en régime linéaire pour la somme ; courants d’entrée nuls.', 'La limitation aux rails est quasi statique et ne simule pas un ALI dynamique.', 'Les tensions d’entrée sont celles de sources imposées ; chaque source voit une résistance d’entrée finie.'],
    techniques=['Orienter les courants et appliquer la loi des nœuds.', 'Décomposer une sortie en contributions par superposition.', 'Vérifier le domaine linéaire avant d’employer une masse virtuelle.'],
    levels=dict(sup='PTSI : lois des nœuds, superposition et somme de sinusoïdes.',spe='PSI/PT : montage inverseur idéal, non-linéarité par saturation.',beyond='Sommation à plusieurs entrées ; réalisation pratique avec bruit et impédances de source.'),
    first_steps=['Choisir les poids 2 et 1, puis annuler chaque entrée à tour de rôle.', 'Doubler R₂ : prévoir le changement du second terme.', 'Choisir la saturation : comparer la prédiction idéale et la sortie limitée.'],
    expected='Déterminer les coefficients d’une somme et expliquer la perte de superposition après saturation.'),
'integrateur_derivateur': dict(
    purpose='Relier une dérivée ou une intégrale à des composants et distinguer condition initiale et régime sinusoïdal.',
    objects=['vₑ est l’entrée, vₛ la sortie et E la crête d’entrée, en volts ; f est en hertz, ω = 2πf en rad/s et t est affiché en ms.',
             'L’intégrateur possède une résistance d’entrée R et une capacité de rétroaction C. Le dérivateur idéal permute ces éléments.',
             'Le dérivateur amélioré possède R et C en série à l’entrée, R′ et C′ en parallèle en rétroaction ; les résistances sont affichées en kΩ et les capacités en nF.',
             'RC et R′C′ sont des temps, en secondes. H est le transfert sans unité ; j² = −1 et s = jω en régime sinusoïdal.',
             'La borne positive de l’ALI est à la masse ; la contre-réaction utilise sa borne inverseuse. L’intégrateur part ici de vₛ(0) = 0.'],
    hypotheses=['ALI et composants idéaux, sans rails ni vitesse de balayage maximale.', 'Dérivateurs en régime établi ; intégrateur calculé depuis une condition initiale annoncée.', 'Les graphiques de Bode décrivent la partie sinusoïdale, même si une intégration ajoute une constante.'],
    techniques=['Calculer une impédance en série ou en parallèle.', 'Dériver ou intégrer une sinusoïde en conservant le signe inverseur.', 'Lire les conditions de validité d’une approximation par comparaison de ωRC à 1.'],
    levels=dict(sup='Physique PTSI : conditions de fonctionnement d’un filtre comme intégrateur ou dérivateur.',spe='Physique PSI/PT : établir la relation du montage intégrateur et utiliser l’ALI idéal.',beyond='Dérivateur amélioré étudié pas à pas ; stabilité et bruit d’une réalisation réelle.'),
    first_steps=['Choisir l’intégrateur : vérifier le départ à zéro et la composante constante.', 'Choisir le dérivateur idéal : multiplier la fréquence par dix et observer l’amplitude.', 'Choisir le dérivateur amélioré : parcourir les deux fréquences de pôle.'],
    expected='Établir une opération temporelle avec sa condition initiale et identifier une bande où l’approximation de dérivée convient.'),
'schmitt_trigger': dict(
    purpose='Mettre en évidence une mémoire de circuit à partir de deux seuils de basculement.',
    objects=['L’ALI reçoit la tension d’entrée vₑ à sa borne négative ; sa sortie vₛ prend les niveaux ±Vₛₐₜ, en volts.',
             'R₁ relie la sortie à l’entrée positive et R₂ cette entrée à la masse ; leurs valeurs sont affichées en kΩ. β = R₂/(R₁ + R₂) est sans unité.',
             'Les seuils haut et bas sont ±βVₛₐₜ, en volts. E est la crête de la rampe triangulaire et N celle de la perturbation ajoutée, en volts.',
             'f est la fréquence de la rampe en hertz ; la perturbation est une sinusoïde à 23f ; le temps t est affiché en ms.',
             'L’état initial indique le signe de la sortie avant le premier échantillon. Il reste nécessaire lorsque l’entrée demeure entre les seuils.'],
    hypotheses=['ALI saturé idéal à rétroaction positive ; aucune égalité imposée des deux entrées.', 'Niveaux symétriques et commutations instantanées.', 'La perturbation est déterministe ; elle illustre des franchissements et ne représente pas une mesure statistique de bruit.'],
    techniques=['Calculer le diviseur de tension de la rétroaction positive.', 'Étudier séparément chaque état saturé et sa condition de maintien.', 'Parcourir le cycle dans le temps et distinguer entrée présente et état précédent.'],
    levels=dict(sup='PTSI : diviseur de tension, signaux périodiques et reconnaissance d’une non-linéarité.',spe='Physique PSI/PT : cycle du comparateur à hystérésis et notion de mémoire.',beyond='Temporisations réelles et choix d’un comparateur spécialisé.'),
    first_steps=['Observer les basculements d’une rampe qui dépasse les deux seuils.', 'Réduire l’amplitude sous les seuils et changer l’état initial.', 'Ajouter la perturbation puis élargir l’hystérésis : expliquer les basculements obtenus.'],
    expected='Prédire un état et un basculement avec le seuil correspondant, en tenant compte de l’histoire de l’entrée.'),
'astable': dict(
    purpose='Calculer une période d’oscillation à partir d’une charge exponentielle et de seuils de comparateur.',
    objects=['R₁ charge le condensateur C depuis la sortie de l’ALI ; R₂ relie sa borne positive à la commande continue Vₑ et R₃ à la sortie.',
             'Les résistances sont affichées en kΩ et C en nF. La tension du condensateur v_C, la sortie vₛ, la commande Vₑ et le niveau Vₛₐₜ sont en volts.',
             'τ = R₁C est le temps de charge, en secondes ; β = R₂/(R₂ + R₃) est sans unité ; h = (1 − β)Vₑ est en volts.',
             'Les seuils L = h − βVₛₐₜ et U = h + βVₛₐₜ sont en volts ; t₊ et t₋ sont les durées des deux états, en secondes.',
             'La période T = t₊ + t₋ est affichée en ms ; la fréquence 1/T est en hertz ; le rapport t₊/T est affiché en pourcentage.'],
    hypotheses=['Condensateur idéal, ALI à sortie ±Vₛₐₜ et commutations instantanées.', 'Tracé périodique commencé au seuil bas si les oscillations sont possibles.', 'En arrêt, sortie dans l’état de saturation cohérent avec la commande et condensateur initialement déchargé.'],
    techniques=['Résoudre une charge RC à sortie constante.', 'Calculer un temps d’atteinte par un logarithme.', 'Vérifier qu’un seuil se situe strictement avant la cible de charge.'],
    levels=dict(sup='PTSI : régime transitoire RC, exponentielles et continuité de la tension d’un condensateur.',spe='Physique PSI/PT : séquences, conditions de basculement et période d’un oscillateur de relaxation.',beyond='Commande du rapport cyclique par tension continue et délais de comparateur.'),
    first_steps=['Mettre la commande à zéro et vérifier les durées égales.', 'Augmenter la commande positive : prévoir quel état s’allonge.', 'Atteindre la limite |Vₑ| = Vₛₐₜ : expliquer l’arrêt sans utiliser une période finie.'],
    expected='Déduire la période et le rapport cyclique des seuils et reconnaître une commande qui bloque les oscillations.'),
'wien': dict(
    purpose='Trouver une condition de démarrage d’oscillation et comprendre pourquoi le modèle linéaire ne fixe pas son amplitude.',
    objects=['Le pont comporte une branche série R₁–C₁ et une branche parallèle R₂–C₂ vers la masse ; les résistances sont affichées en kΩ, les capacités en nF.',
             'B est le rapport de tension du pont sans unité ; G est le gain non inverseur de l’amplificateur ; Gcrit est son gain critique. Le contrôle règle G/Gcrit.',
             'f₀ est la fréquence sélectionnée en hertz et ω₀ = 2πf₀ en rad/s ; s = jω et j² = −1 dans le modèle harmonique.',
             'a = R₁C₁ + R₂C₂ + R₂C₁ et b = R₂C₁ sont en secondes ; d = R₁R₂C₁C₂ est en secondes carrées ; γ est le taux initial de croissance en s⁻¹.',
             'A est l’amplitude de l’enveloppe en volts ; la petite perturbation initiale et l’échelle Vlim sont en volts ; le temps t est affiché en ms.'],
    hypotheses=['Pont idéal et amplificateur de gain constant pour calculer le seuil exact.', 'Enveloppe approchée près du seuil à fréquence f₀ ; loi non linéaire fournie pour limiter son amplitude.', 'L’échelle de limitation représente un choix pédagogique, pas une amplitude prédite par un ALI réel.'],
    techniques=['Chercher une phase nulle puis le gain de boucle unité.', 'Relier le signe d’un coefficient d’équation différentielle au démarrage.', 'Distinguer le seuil linéaire et la stabilisation non linéaire de l’amplitude.'],
    levels=dict(sup='PTSI : fonction de transfert fournie et régime sinusoïdal.',spe='Physique PSI/PT : oscillateur quasi sinusoïdal, condition de démarrage et rôle des non-linéarités.',beyond='Modèle d’enveloppe accompagné ; mécanismes réels de régulation d’amplitude.'),
    first_steps=['Choisir un pont identique et retrouver un gain critique de 3.', 'Passer du gain inférieur au seuil au gain légèrement supérieur.', 'Dissymétriser les branches : recalculer la fréquence et le gain critique avant d’observer.'],
    expected='Justifier la fréquence et le gain de démarrage, et préciser quelle hypothèse fournit le plateau d’amplitude.'),
'redresseur_precision': dict(
    purpose='Montrer comment la contre-réaction compense un seuil de diode et vérifier sa marge d’alimentation.',
    objects=['L’entrée e, la sortie interne de l’ALI et les tensions de branche vₛ₁ et vₛ₂ sont en volts ; la sortie utile est vₛ₂ − vₛ₁.',
             'Les trois résistances d’entrée et de rétroaction sont égales ; les deux diodes des branches conduisent alternativement. La borne positive est à la masse.',
             'E est la crête de l’entrée sinusoïdale en volts ; f sa fréquence en hertz ; le temps t est affiché en ms.',
             'Vᴅ est le seuil d’une diode et Vₛₐₜ la limite positive de sortie de l’ALI, en volts. Le pont passif comparé traverse deux diodes.',
             'L’amplitude compensable Vₛₐₜ − Vᴅ tient compte de la tension supplémentaire que l’ALI fournit en interne.'],
    hypotheses=['Modèle quasi statique ; diodes à seuil constant sans résistance dynamique.', 'Trois résistances égales et sorties de branche non chargées.', 'Les rails arrêtent la compensation ; les transitoires de passage par zéro sont omis.'],
    techniques=['Étudier la diode conductrice séparément dans chaque alternance.', 'Appliquer la loi des nœuds dans le régime compensé.', 'Comparer un seuil passif et la réserve de tension d’une contre-réaction.'],
    levels=dict(sup='PTSI : modèle de diode fourni, alternances et loi des nœuds.',spe='PSI/PT : application d’ALI et reconnaissance des limites de tension ; redresseur accompagné.',beyond='Erreur de passage par zéro, récupération après saturation et diodes réelles.'),
    first_steps=['Choisir une petite tension et comparer le pont passif à la sortie de précision.', 'Mettre le seuil des diodes à zéro : retrouver la valeur absolue dans les deux modèles.', 'Réduire Vₛₐₜ devant E + Vᴅ : prévoir la crête compensable.'],
    expected='Expliquer l’absence de seuil dans la sortie utile et la présence d’une tension supplémentaire à l’intérieur du montage.'),
'filtre_etat': dict(
    purpose='Relier les trois ALI à un passe-bande puis filtrer les harmoniques d’un créneau avec leurs gains et phases.',
    objects=['R₁ est à l’entrée ; R₂ est la rétroaction du premier ALI ; R₃ ramène la sortie de l’intégrateur ; R₄ et R₅ fixent l’inversion ; R₆ entre dans l’intégrateur. Les résistances sont affichées en kΩ.',
             'Les deux condensateurs ont une capacité commune C affichée en nF. Les tensions vₑ, vₛ, vₛ₁ et vₛ₂ sont en volts ; les deux dernières sont les états internes.',
             'H₀ est le gain central et Q le facteur de qualité, sans unité ; ω₀ est la pulsation centrale en rad/s et f₀ = ω₀/(2π) la fréquence centrale en hertz.',
             'ω₁ et ω₂ sont les bornes à −3 dB, en rad/s ; Δω = ω₂ − ω₁ est la largeur en rad/s ; Δf = Δω/(2π) est en hertz.',
             'E est la crête d’entrée en volts ; f est sa fondamentale en hertz, ωₑ = 2πf en rad/s ; k est un entier positif. Aₖ et Bₖ sont les coefficients sinusoïdaux en volts.',
             'Le nombre choisi compte les harmoniques impaires retenues ; j² = −1 définit le transfert complexe H(jω). Le temps t est affiché en ms.'],
    hypotheses=['Trois ALI idéaux en régime linéaire, deux capacités identiques et sortie non chargée.', 'Régime périodique établi ; la somme d’un créneau est tronquée au nombre d’harmoniques choisi.', 'L’approximation dans la bande supprime les autres termes ; la sortie complète calculée conserve leur atténuation réelle dans le modèle.'],
    techniques=['Écrire les trois relations entre sortie et tensions internes.', 'Calculer un gain et une phase pour chaque harmonique.', 'Relier Q, largeur et bornes à −3 dB ; comparer rad/s et Hz.'],
    levels=dict(sup='Physique PTSI : utiliser un spectre fourni pour simuler le filtrage d’un signal périodique.',spe='Physique PSI/PT : filtres actifs, analyse spectrale et stabilité ; calcul du montage accompagné.',beyond='Synthèse de filtre à variables d’état et surveillance des saturations internes.'),
    first_steps=['Choisir une sinusoïde au centre et retrouver le gain H₀.', 'Choisir une fondamentale égale au tiers du centre : comparer somme complète et troisième harmonique.', 'Augmenter R₂ : prévoir la largeur et le gain central avant de regarder les courbes.'],
    expected='Construire la sortie d’un filtre à partir d’un spectre et expliquer les effets distincts du centre, du gain et de la largeur.'),
'transistor_polarisation': dict(
    purpose='Dans un prolongement guidé, valider le repos d’un NPN avant de calculer son amplification de petites variations.',
    objects=['Un transistor NPN possède une base, un collecteur et un émetteur. Vcc est l’alimentation en volts ; Rc relie le collecteur à Vcc et Re l’émetteur à la masse.',
             'Rb₁ relie la base à la masse et Rb₂ la base à Vcc ; les résistances sont affichées en kΩ. Vth et Rth sont leur source et résistance de Thévenin.',
             'Ib et Ic sont les courants de base et de collecteur, en ampères ; Ve et Vc les tensions de repos en volts ; β est le gain en courant sans unité.',
             'Le modèle fixe Vbe = 0,7 V et Vce,sat = 0,2 V. Uₜ = 25,85 mV fixe gm = Ic/Uₜ, en siemens, et rπ = β/gm, en ohms, uniquement en régime actif.',
             'Le générateur possède une résistance Rg ; Rₗ est une charge en alternatif. C₁ relie l’entrée à la base ; Ce découple Re. Les capacités sont affichées en µF.',
             'e est une petite variation de tension de crête E, en volts, à la fréquence f en hertz ; s = j2πf avec j² = −1. Ze est l’impédance d’émetteur en ohms ; t est affiché en ms.'],
    hypotheses=['NPN et tensions de jonction fournies ; effet Early négligé et résistance dynamique collecteur–émetteur infinie.', 'La charge alternative ne modifie pas le repos ; les capacités internes du transistor sont omises.', 'Calcul petit signal autorisé seulement au repos actif ; les limites tracées sont des repères quasi statiques, sans modèle de saturation dynamique.'],
    techniques=['Remplacer un pont résistif par son équivalent de Thévenin.', 'Résoudre et vérifier un point de repos avant une linéarisation.', 'Calculer l’effet d’un condensateur de liaison et d’un découplage sur le gain.'],
    levels=dict(sup='PTSI : lois des circuits, équivalent résistif et impédances capacitives réinvestis.',spe='Appui méthodologique : valider un modèle avant de l’utiliser. Le transistor amplificateur n’est pas une exigence de physique PSI/PT.',beyond='Polarisation et petits signaux d’un transistor ; modèle accompagné distinct de l’interrupteur de puissance en SI.'),
    first_steps=['Choisir le régime actif et vérifier la marge collecteur–émetteur.', 'Déconnecter Ce : comparer le gain et le rôle de Re.', 'Choisir saturation ou blocage au repos : expliquer pourquoi la réponse petit signal est désactivée.'],
    expected='Identifier le régime de repos et justifier les conditions où une petite variation peut être amplifiée.')
}
