"""Objectifs, unités et premiers gestes des vingt-quatre laboratoires.

Sup/Spé indiquent une porte d'entrée par les techniques ; voir PARCOURS.md
pour les textes de programme et les prolongements selon la filière.
"""


def guide(purpose, objects, assumptions, techniques, first_steps, sup, spe,
          beyond, lessons, expected):
    return dict(purpose=purpose, objects=objects, assumptions=assumptions,
                techniques=techniques, first_steps=first_steps,
                levels=dict(sup=sup, spe=spe, beyond=beyond),
                lesson_numbers=lessons, expected=expected)


LAB_GUIDES = {
    "dipoles": guide(
        "Passer de deux charges exactes à un dipôle approché et décider à quelle distance le modèle est assez précis. Les équipotentielles et les lignes de champ rendent visibles la direction de E et les zéros de V.",
        ["q en nC, séparation a en m, moment p=qa en C·m", "Angle en degrés ; distance d’observation r/a sans unité ; E en V·m⁻¹, V en V"],
        ["Deux charges ±q fixes, placées symétriquement, dans le vide", "Approximation dipolaire seulement pour r≫a ; erreur relative à manier avec prudence près d’un zéro"],
        ["Développement limité et contrôle de son ordre", "Gradient d’un potentiel et symétries", "Lecture d’un écart relatif et test d’échelle"],
        ["Avant l’observation, calculer sur papier l’erreur du potentiel axial à r/a=5 et prévoir l’effet d’un doublement de cette distance.", "Choisir le préréglage horizontal, passer de r/a=5 à 10 puis 20 et comparer champ exact et dipolaire ; tourner ensuite le dipôle à 90°.", "Expliquer pourquoi V=0 sur le plan équatorial alors que E y reste non nul ; retrouver l’ordre (a/r)² de l’erreur hors des zéros."],
        "Superposition de Coulomb, dimensions et symétrie ; l’entrée ne demande pas de théorie multipolaire complète.",
        "Taylor multivariable, gradient, énergie et forces ; choisir une grandeur pour quantifier l’approximation.",
        "Moments multipolaires et sensibilité d’une approximation près d’un zéro.", [4,5],
        "Une distance justifiée pour un seuil donné, et une distinction claire entre potentiel nul et champ nul."),
    "gauss": guide(
        "Choisir une surface adaptée à la symétrie puis confronter champ, potentiel, capacité et énergie. La sphère volumique et le coaxial donnent deux exemples où un théorème intégral permet un calcul local.",
        ["Sphère : Q en nC, R en m, E en V·m⁻¹", "Coaxial : a en cm, rapport b/a, longueur en m, U=Vinterne−Vexterne en V ; C en F, W en J"],
        ["Charge volumique uniforme pour la sphère ; potentiel nul à l’infini", "Coaxial idéal sans effets de bord ; vide, conducteurs en équilibre"],
        ["Théorème de Gauss et invariances", "Intégration radiale du potentiel", "Double calcul de l’énergie"],
        ["Prévoir les lois en r de E à l’intérieur et à l’extérieur de la sphère, puis l’effet de R doublé à Q fixé.", "Choisir la sphère, inverser Q et augmenter R ; passer ensuite au coaxial et doubler sa longueur à b/a fixé.", "Retrouver sur papier C=2πε₀ℓ/ln(b/a) et comparer W=½CU² à l’intégrale du champ ; discuter la différence entre Q fixé et U fixé."],
        "Intégration, géométrie et unités ; Gauss est introduit ici comme outil si la filière ne l’a pas encore étudié.",
        "Symétries de champs, potentiel, capacité et bilans électrostatiques selon la filière.",
        "Unicité de Poisson et variations d’énergie avec une source de tension.", [2,3,6],
        "Deux lois radiales démontrées et une capacité dont le signe et les dimensions sont vérifiés."),
    "biotsavart": guide(
        "Relier la géométrie d’un courant au champ magnétique, reconnaître une limite de fil long ou de solénoïde long et contrôler l’approximation dipolaire d’une spire.",
        ["I orienté en A ; rayon R et longueur en m ; nombre N de spires", "B en T ou μT selon l’affichage ; moment magnétique IπR² en A·m²"],
        ["Courants stationnaires dans le vide ; fils idéalisés", "Le champ axial d’une bobine finie diffère de sa limite longue, surtout près des extrémités"],
        ["Produit vectoriel et superposition", "Intégration de Biot–Savart", "Passage à une limite et comparaison relative"],
        ["Dessiner le sens de B pour I>0 puis prévoir le changement lorsque I devient négatif.", "Comparer spire et solénoïde ; à rayon fixé augmenter la longueur, puis inverser I et observer les profils.", "Dériver le champ axial de la spire ; retrouver son moment dipolaire loin sur l’axe et quantifier l’erreur à z=5R sur papier."],
        "Produit vectoriel, intégration et compensation par symétrie.",
        "Magnétostatique, distinction Biot–Savart/Ampère et limites de bobines.",
        "Champs retardés et termes radiatifs absents du calcul stationnaire.", [7,16],
        "Une justification de la méthode selon la source, sans appliquer Ampère comme formule universelle de calcul local."),
    "helmholtz": guide(
        "Fabriquer une région presque uniforme par annulation d’une dérivée. Le réglage géométrique d/R=1 devient une conséquence du calcul et permet une calibration de champ utilisable avec Hall.",
        ["Rayon R en m, écartement d/R sans unité, I en A, N par bobine", "B en T ; uniformité relative sans unité, évaluée dans une région annoncée"],
        ["Deux bobines identiques et coaxiales ; courants de même sens", "Centre sans courant ; symétrie z↦−z et modèle de spires minces"],
        ["Superposition et fonctions paires", "Dérivées secondes et développement quartique", "Calibration et tolérance relative"],
        ["Prévoir le signe de B″(0) pour d<R et d>R ; expliquer pourquoi B′(0)=0 dans les deux cas.", "Comparer les préréglages d/R=0,5,1 et 1,5 ; modifier ensuite I sans changer la géométrie.", "Retrouver d=R par B″(0)=0, puis estimer sur papier une demi-longueur axiale à 0,1 % et contrôler la formule exacte."],
        "Somme de fonctions, parité et dérivation ; estimation dimensionnelle de B.",
        "Développement limité contrôlé et symétries du champ ; liaison mesure/modèle.",
        "Développement hors axe par divB=curlB=0 et optimisation d’une région volumique.", [8,11],
        "Un réglage dérivé et une zone d’uniformité définie par un seuil et une géométrie précis."),
    "drude": guide(
        "Comprendre une conductivité comme réponse avec mémoire. L’échelon et le régime harmonique font distinguer vitesse des porteurs, courant, énergie stockée et chaleur.",
        ["n obtenu à partir de log₁₀(n/m⁻³), τ en fs, masse effective en me", "f en THz, Ecrête en V·m⁻¹ ; σ en S·m⁻¹, j en A·m⁻² ; q=±e"],
        ["Porteurs identiques indépendants, frottement moyen −m*v/τ", "Champ homogène ; pas de rappel élastique ni de transport balistique résolu"],
        ["Équation différentielle du premier ordre", "Réponse complexe avec exp(−iωt)", "Bilan de puissance et convolution causale"],
        ["Prévoir le signe de v et de j pour des électrons puis des porteurs positifs ; calculer ωτ pour le réglage choisi.", "Comparer faible fréquence et réponse inertielle ; changer le signe des porteurs puis doubler τ à densité fixée.", "Retrouver σ=σ₀/(1−iωτ), identifier la partie dissipative et expliquer pourquoi j ne change pas de sens stationnaire lorsque q change de signe."],
        "Résolution d’un échelon et loi d’Ohm obtenue à partir d’un modèle mécanique.",
        "Amplitudes complexes, énergie et réponse linéaire ; contrôle des amplitudes crête et efficace.",
        "Causalité, pôles complexes, permittivité de Drude et statistiques des porteurs.", [9,10],
        "Un courant avec phase et une dissipation positive, accompagnés du domaine de validité du modèle."),
    "hall": guide(
        "Déterminer le signe des porteurs à partir d’une tension transverse dont les bornes sont explicitement définies. Le laboratoire prolonge la force de Lorentz et les mesures de champ calibrées par Helmholtz.",
        ["I vers +x en A ; Bz vers +z en T ; largeur w suivant y et épaisseur t suivant z en mm", "UH=V(y=−w/2)−V(y=+w/2) en V ; q=±e et n en m⁻³"],
        ["Un type de porteur majoritaire ; régime stationnaire", "Circuit ouvert suivant y : jy=0 ; EH=−v×B et UH=IB/(nqt)"],
        ["Trièdre direct et signe d’une charge", "Différence de potentiel et mesure antisymétrisée", "Identification d’une densité dans un modèle déclaré"],
        ["Avec I>0,Bz>0, prévoir vx,Ey puis UH pour q=−e en conservant les bornes annoncées.", "Comparer électrons et trous ; inverser B, puis doubler l’épaisseur et changer la largeur séparément.", "Montrer que UH est indépendant de w à I fixé, proposer [U(B)−U(−B)]/2 contre un parasite pair et discuter le cas de deux populations."],
        "Lorentz, vitesse moyenne et définition du potentiel ; aucune mémorisation d’un signe sans axes.",
        "Conductivité tensorielle, symétries de mesure et extraction de paramètres selon la filière.",
        "Transport multibande, pondération par mobilités et Hall quantique, hors du modèle présenté.", [11,8],
        "Une prédiction du signe reproduite par les inversions et une interprétation prudente de la densité extraite."),
    "induction": guide(
        "Fermer le bilan électromécanique et distinguer un rail toujours actif d’un cadre dont le flux cesse de varier après immersion. Lenz est confronté aux équations et à la chaleur dissipée.",
        ["B en T, largeur active et hauteur du cadre en m, R en Ω", "Rail : L en mH, masse en g, v en m·s⁻¹ ; cadre : distance vers le bas et temps en s"],
        ["Rail : v vers +x, B vers +z, i vers +y ; Li̇+Ri=−Bℓv, mv̇=Bℓi", "Cadre : inductance négligée, champ uniforme après une frontière nette ; immersion complète ⇒ flux constant"],
        ["Flux orienté et fém d’un contour mobile", "Système d’équations différentielles et critère d’amortissement", "Somme des bilans mécanique et électrique"],
        ["Prédire le signe du courant initial du rail et la dérivée de W=mv²/2+Li²/2 avant tout calcul.", "Comparer rail résistif et préréglage inductif oscillant ; choisir ensuite le cadre et repérer l’instant de pleine immersion.", "Démontrer Ẇ=−Ri² pour le rail et Φ constant pour le cadre immergé ; expliquer pourquoi une vitesse limite d’entrée n’est pas une limite globale."],
        "Lenz, énergie et résolution d’une équation linéaire après introduction guidée du flux.",
        "Induction, couplages, transitoires et traitement par morceaux.",
        "Inductances mutuelles, géométries continues et freinage magnétique distribué.", [12,13],
        "Un bilan fermé et deux scénarios distingués par la variation réelle de flux, pas par le seul mouvement."),
    "hautparleur": guide(
        "Lire un transducteur comme deux systèmes couplés par le même coefficient. À la résonance, vitesse élevée et courant faible deviennent compatibles grâce à la contre-fém.",
        ["R en Ω, L en mH, masse en g, raideur k en N·m⁻¹, b en N·s·m⁻¹", "κ en N·A⁻¹=V·s·m⁻¹, f en Hz, tension crête en V ; x,v,i et puissances SI"],
        ["Suspension linéaire, coefficient κ constant, une masse et un amortissement", "u=Ri+Li̇+κv et mv̇+bv+kx=κi ; pas de calcul complet d’enceinte acoustique"],
        ["Oscillateur harmonique forcé", "Impédance réfléchie par un couplage", "Moyenne harmonique et conservation de l’énergie"],
        ["Calculer f₀=√(k/m)/(2π) et prévoir la valeur de κ²/b ajoutée à l’impédance à cette fréquence.", "Placer f près de f₀ puis au-dessus ; doubler κ et comparer vitesse, courant et bilan de puissance.", "Retrouver Zmot=κ²/[b−i(mω−k/ω)] et montrer que ses pertes sont positives ; distinguer résonance mécanique et maxima d’une réponse chargée."],
        "Équations d’oscillateur, circuit RL et bilans séparés.",
        "Couplage réciproque, amplitudes complexes et conversion électromécanique selon la filière.",
        "Charge acoustique, rayonnement d’un piston et modèles distribués de membrane.", [14],
        "Une explication du pic d’impédance et un bilan ui=pertes+variation d’énergie, avec unités de κ vérifiées."),
    "hysteresis": guide(
        "Reconstruire H depuis le courant primaire et B depuis la tension du secondaire ouvert. L’aire du cycle distingue dissipation et énergie stockée dans une réponse à mémoire.",
        ["Hc en A·m⁻¹, Hmax/Hc, Bs en T, μr réversible", "f en Hz, longueur du tore en m, section en cm², N₁,N₂ ; e₂ en V et pertes en J·m⁻³ par cycle"],
        ["Tore à champ approximativement uniforme, secondaire ouvert", "Banque de relais prescrite ; pas de domaines microscopiques ou courants de Foucault calculés"],
        ["Ampère et Faraday en montage mesurable", "Intégration avec constante initiale", "Aire orientée d’un cycle et mémoire"],
        ["Prévoir e₂ lorsqu’un B sinusoïdal est imposé et calculer son déphasage ; estimer l’aire d’un cycle rectangulaire.", "Comparer cycle majeur, cycle mineur et Bs=0 ; changer la fréquence et observer ce qui relève du modèle quasi statique.", "Retrouver H=N₁i₁/ℓ et e₂=−N₂S Ḃ, puis convertir ∮H dB en chaleur et puissance ; expliquer pourquoi ½BH n’est pas une énergie unique du cycle."],
        "Intégration d’une tension et lecture d’une aire ; orientation du bobinage explicitée.",
        "Milieux magnétiques, transformateurs et bilans selon la filière.",
        "Preisach, pertes dynamiques et identification d’une distribution de domaines.", [15,21],
        "Un cycle avec axes et unités calibrés, et une distinction entre mémoire, dissipation et réponse réversible."),
    "synchrone": guide(
        "Comprendre pourquoi deux angles donnant le même couple n’ont pas la même stabilité. Le modèle de dipôle à une paire de pôles rend visibles retard, potentiel incliné et seuil statique de verrouillage.",
        ["Moment m en A·m², B en T, fréquence du champ tournant en Hz", "Retard δ=θchamp−θrotor en degrés, J en kg·m² et charge normalisée Tcharge/(mB)"],
        ["Dipôle physique à une paire de pôles : Tmax=mB, Ωs=2πfchamp", "Charge constante ; diagramme d’équilibre et petite oscillation, pas de démarrage dynamique complet"],
        ["Couple issu d’une énergie", "Équilibres et linéarisation", "Puissance mécanique et seuil"],
        ["Pour Tcharge/Tmax=0,5, trouver les deux retards possibles et prévoir la stabilité de chacun.", "Comparer 30° et 150° à même charge, puis porter la charge au-dessus de 1 ; observer la pente et le potentiel incliné.", "Dériver δ̈=−(Tmax sinδ−Tcharge)/J et expliquer le signe de cosδ ; calculer la petite pulsation et préciser ce qu’un seuil statique ne dit pas du démarrage."],
        "Produit vectoriel, trigonométrie et minimum d’énergie.",
        "Stabilité, verrouillage et machines tournantes, particulièrement dans les parcours où elles sont au programme.",
        "Dynamique de capture, alimentation variable et modèle multipolaire périodique en pθ.", [19],
        "Deux branches classées par leur pente et un seuil interprété sans inventer une simulation de décrochage."),
    "asynchrone": guide(
        "Lire le glissement comme la cause du courant rotorique, puis suivre séparément chaleur du rotor, conversion mécanique et flux d’entrefer dans un circuit équivalent triphasé.",
        ["Tension simple efficace en V, f en Hz, p paires de pôles, s=(Ωs−Ωr)/Ωs", "R₁,R₂ en Ω ; L₁,L₂,Lm en mH ; puissances signées en W et couple en N·m"],
        ["Triphasé équilibré, paramètres ramenés au stator", "Modèle linéaire établi ; s=0 traité par la limite d’une admittance, pertes mécaniques non calculées"],
        ["Amplitudes complexes et associations d’impédances", "Bilan Pg=Pm+PJrotor", "Lecture de trois régimes par les signes"],
        ["Prévoir ce qui arrive au courant rotorique à s=0 et aux signes des puissances pour s<0.", "Comparer faible glissement, rotor arrêté et génératrice ; modifier R₂ et relever le déplacement du maximum de couple.", "Vérifier PJrotor=sPg≥0 et Pm=(1−s)Pg ; sur papier, montrer que la phase initiale d’une spire ne change pas son couple moyen."],
        "Lenz, vitesse relative et bilan de puissance ; le circuit triphasé est une entrée guidée.",
        "Amplitudes complexes, induction et bilans de Spé ; le circuit triphasé asynchrone est ici un prolongement accompagné, à distinguer du programme explicite des machines synchrones en PSI.",
        "Modèles à paramètres variables, saturation et commande vectorielle.", [20],
        "Un partage de puissance cohérent pour moteur et génératrice, et une explication du couple nul au synchronisme."),
    "peau": guide(
        "Distinguer pénétration harmonique et diffusion d’un échelon continu. La même équation de diffusion explique une profondeur δ à fréquence fixée et une profondeur croissant en √t.",
        ["Fréquence f donnée par log₁₀(f/Hz), σ en MS·m⁻¹, μr constant", "Bsurf en mT, temps depuis l’échelon en ms ; δ et √ηmt en m"],
        ["Demi-espace x>0 ; champ tangent, loi d’Ohm locale à coefficients constants", "Courant de déplacement négligeable ; milieu normal, sans équation de London"],
        ["Diffusion et choix de la racine complexe", "Test d’échelle en f⁻¹ᐟ² ou t¹ᐟ²", "Dissipation locale et conditions à l’infini"],
        ["Prévoir le rapport des profondeurs pour f multipliée par 100, puis pour le temps d’échelon multiplié par quatre.", "Comparer cuivre à 1 et 100 kHz en harmonique ; passer en échelon et augmenter le temps.", "Déduire ∂tB=(μσ)⁻¹∂xxB de Maxwell et Ohm ; expliquer pourquoi ω→0 ne produit pas un état Meissner."],
        "Racine carrée, unités et interprétation d’un profil décroissant ; diffusion introduite progressivement.",
        "Propagation dissipative, amplitudes complexes et séparation entre régime établi et transitoire.",
        "Conductivité dispersive, plaque finie et couplage London/composante normale.", [23,31],
        "Deux lois de pénétration différenciées et une vérification du signe diffusif positif."),
    "maxwell": guide(
        "Voir si une onde transporte une puissance moyenne ou échange localement énergie électrique et magnétique. Comparer les champs instantanés au flux de Poynting plutôt que confondre amplitude et énergie.",
        ["f en GHz, amplitude électrique crête de chaque onde en V·m⁻¹", "Ellipticité signée, temps t/T ; B en T, énergie en J·m⁻³ et S en W·m⁻²"],
        ["Vide, ondes planes ; progressive +z ou deux ondes opposées égales", "Convention exp(−iωt), superposition cohérente et polarisations déclarées"],
        ["Superposition harmonique", "Poynting et moyenne temporelle", "Conditions de transversalité"],
        ["Prévoir B=E/c et le signe du flux pour une onde progressive ; prévoir la moyenne du flux pour deux ondes opposées égales.", "Comparer progressive, circulaire et stationnaire ; parcourir t/T et observer les positions des maxima de E,B et énergie.", "Retrouver S=E×H et le bilan local ; distinguer un flux instantané non nul d’un transport moyen nul dans la stationnaire."],
        "Superposition, phases et bilans ; les équations locales sont accompagnées.",
        "Maxwell, ondes électromagnétiques et énergie selon la filière.",
        "Paquets, milieux dispersifs et différence entre vitesse de phase et vitesse de transport.", [1,21,22],
        "Une interprétation séparée du champ, de l’énergie et du flux, avec moyenne et instant distingués."),
    "interfaces": guide(
        "Utiliser des conditions aux limites pour prédire amplitudes et flux. Brewster et réflexion totale donnent deux phénomènes différents qu’une courbe de réflexion seule ne doit pas confondre.",
        ["n₁,n₂ réels sans unité ; incidence en degrés ; TE/TM", "λvide en nm ; r,t complexes, R,T flux normaux relatifs ; longueur évanescente en m"],
        ["Interface plane entre diélectriques isotropes non magnétiques sans pertes", "Pas de charges ou courant libres de surface ; kz transmis choisi décroissant si évanescent"],
        ["Snell comme continuité de phase", "Raccordement E/H et système linéaire", "Bilan R+T=1 et racine évanescente"],
        ["À incidence normale air→verre, prévoir le signe de r et calculer R,T ; ne pas utiliser |t|² seul comme T.", "Comparer TE/TM, sélectionner Brewster puis réflexion totale ; modifier λ à angle fixé et observer l’échelle de pénétration.", "Retrouver les continuités, expliquer l’onde évanescente non nulle avec flux normal moyen nul, puis calculer ses limites sur papier."],
        "Réfraction et phases ; nombres complexes introduits sur un exemple concret.",
        "Conditions aux limites et polarisation selon la filière ; contrôler les flux plutôt que les seules amplitudes.",
        "Milieux absorbants, films minces et couplage par réflexion totale frustrée.", [21,24],
        "Un bilan exact et une distinction justifiée entre zéro de réflexion TM et seuil d’évanescence."),
    "guide": guide(
        "Comprendre qu’une paroi sélectionne un nombre d’onde transverse et une fréquence de coupure. Le TE₁₀ relie séparation des variables, valeurs propres et vitesse de transport.",
        ["Largeur a en mm, f en GHz, Ecrête en V·m⁻¹", "Distance z/a et phase t/T ; β en rad·m⁻¹, fc en Hz, vitesses en m·s⁻¹"],
        ["Guide vide rectangulaire idéal, parois parfaitement conductrices", "Mode TE₁₀ isolé ; excitation depuis z=0, branche décroissante sous coupure"],
        ["Séparation des variables et conditions aux limites", "Dispersion, coupure et eigenmode", "Comparaison phase/groupe/flux"],
        ["Calculer fc=c/(2a), puis prévoir le signe de β² pour 3 et 8 GHz lorsque a=30 mm.", "Comparer propagatif, sous coupure et coupure exacte ; parcourir t/T et augmenter la longueur affichée.", "Retrouver sin(πx/a), β²=(ω/c)²−(π/a)² et vphasevg=c² au-dessus de la coupure ; expliquer l’absence d’un TEM dans le guide creux."],
        "Sinusoïdes, conditions aux extrémités et racine réelle/imaginaire sur un exemple accompagné.",
        "Modes et séparation des variables, selon la filière ou en prolongement guidé.",
        "Familles TE/TM complètes, topologie TEM et guides dissipatifs.", [25],
        "Une coupure calculée et une vitesse de phase supérieure à c interprétée sans confusion avec l’information."),
    "antenne": guide(
        "Déduire un diagramme angulaire d’une intégrale de phases. Taille d’ouverture et pointage font apparaître diffraction, absence possible de zéro et approximation des petits angles.",
        ["Largeur a/λ, λ en mm, pointage en degrés", "Intensité angulaire normalisée sinc² ; phases en radians, sans puissance absolue imposée"],
        ["Ouverture uniforme à rampe de phase prescrite ; observation de Fraunhofer", "Diagramme scalaire dans un plan ; pas de rendement, adaptation ou circuit d’alimentation calculés"],
        ["Intégrale exponentielle complexe", "Différence de trajet et transformée de Fourier", "Domaine angulaire exact versus petit angle"],
        ["Prévoir les premiers zéros pour a/λ=4 et démontrer leur absence à a/λ=0,5.", "Comparer les deux ouvertures, puis utiliser le pointage à 30° ; noter l’asymétrie en angle mais la symétrie en variable de phase.", "Intégrer exp[−ikx(sinθ−sinθ₀)] et expliquer pourquoi θ≈λ/a n’est permis que pour une ouverture grande devant λ ; traiter le réseau de l’exercice 32 sur papier."],
        "Interférences et trigonométrie ; l’intégrale introduit la diffraction.",
        "Fraunhofer, amplitudes complexes et formulation de Fourier selon la filière.",
        "Directivité tridimensionnelle, facteur de réseau et réciprocité d’une antenne.", [29,28],
        "Un diagramme relié à la géométrie et une limite de petit angle explicitement vérifiée."),
    "plasma": guide(
        "Relier une réponse électronique passive à une coupure et à l’absorption. Le choix de la racine de k est confronté au flux de Poynting et à la chaleur, pas seulement au tracé d’une amplitude.",
        ["ω/ωp et ν/ωp ; densité en 10¹⁸ m⁻³ ; Ecrête en V·m⁻¹", "Distance en cm, temps t/T ; εr,k complexes, fp en Hz, pertes en W·m⁻³"],
        ["Plasma froid homogène non magnétisé ; ions immobiles", "Drude avec collisions constantes ; mode transverse et milieu semi-infini"],
        ["Réponse harmonique et racine passive", "Coupure, évanescence et dispersion", "Bilan absorption/Joule"],
        ["Sans collisions, prévoir propagation pour ω/ωp=1,5 et évanescence pour 0,5 ; calculer fp à la densité choisie.", "Comparer ces régimes puis ajouter des collisions près de ω=ωp ; suivre décroissance et pertes.", "Retrouver εr=1−ωp²/[ω(ω+iν)] et le choix Imk≥0 ; sur papier, distinguer le mode longitudinal de l’exercice 34."],
        "Force de rappel collective et équation harmonique ; comparaison à une coupure d’oscillateur.",
        "Propagation dans un milieu conducteur, dispersion et énergie selon la filière.",
        "Plasmas chauds, magnétisés ou stratifiés ; modes propres et amortissements cinétiques.", [10,26],
        "Une coupure et une absorption séparées, avec passivité vérifiée et limites de l’ionosphère déclarées."),
    "dielectrique": guide(
        "Associer dispersion et absorption d’un oscillateur lié, puis relier la polarisation d’une sphère à ses charges de surface. Les champs extérieur, intérieur et local sont distingués.",
        ["ω/ω₀, force d’oscillateur χ₀, γ/ω₀ et ε∞", "Eextérieur en V·m⁻¹, rayon en mm ; P en C·m⁻², εr complexe et charges liées SI"],
        ["Oscillateurs de Lorentz linéaires, amortissement positif", "Sphère électrostatique uniforme pour la limite statique ; pas de transition ferroélectrique universelle déduite"],
        ["Oscillateur forcé et puissance absorbée", "Poisson, raccordement et polarisation", "Distinction charge libre/charge liée"],
        ["Prévoir le signe de Imεr et celui de Reχ loin au-dessous et au-dessus de la résonance.", "Comparer les préréglages sous résonance, résonance et au-dessus ; modifier l’amortissement puis Eextérieur et lire la sphère statique.", "Démontrer ρliée=−divP et σliée=P·n ; retrouver le champ dépolarisant et préciser pourquoi le champ local de Lorentz est une autre construction."],
        "Oscillateur, dérivées et intégration ; polarisation introduite comme densité de dipôles.",
        "Milieux linéaires, énergie et propagation selon la filière.",
        "Champs locaux, Clausius–Mossotti et orientation dipolaire thermique, à traiter sur papier.", [18,27],
        "Deux parties d’une réponse causale reliées et une charge liée de signe correct avec conservation vérifiée."),
    "aimantation": guide(
        "Comparer trois mécanismes : orientation classique, deux niveaux quantiques et moment orbital induit. Le champ démagnétisant d’un ellipsoïde oblige à distinguer champ extérieur et champ interne.",
        ["T en K, μ₀Hextérieur en T, densité en 10²⁷ m⁻³", "Moment en μB, rayon orbital en pm, facteur démagnétisant N ; M,H en A·m⁻¹"],
        ["Moments indépendants ou modèle orbital faible champ ; ellipsoïde uniformément aimanté", "Hint=Hext−NM ; pas de ferromagnétisme ou de transition collective calculés"],
        ["Poids de Boltzmann et dérivée de lnZ", "Série de Langevin et saturation", "Équation auto-cohérente avec champ démagnétisant"],
        ["Prévoir pourquoi les pentes de Langevin et tanh diffèrent d’un facteur trois à moment égal, puis le signe de la contribution diamagnétique.", "Comparer classique et deux niveaux à faible puis basse température ; passer au diamagnétisme et modifier le rayon orbital puis N.", "Retrouver L=cothx−1/x et ses limites ; distinguer cette auto-cohérence géométrique d’un champ moyen de Weiss attractif décrit au cours."],
        "Moments, énergie −μ·B, agitation thermique et limites d’une fonction.",
        "Statistique à deux niveaux et bilans matière, selon la filière ou par un prolongement guidé.",
        "Weiss, énergie libre et stabilité collective ; modèle de domaines distinct de la réponse calculée.", [16,17,18],
        "Trois lois de réponse distinguées par mécanisme, signe et orientations accessibles, sans assimilation à Meissner."),
    "meissner": guide(
        "Voir l’écrantage depuis les deux faces d’une plaque et comprendre ce que London ajoute à la conductivité parfaite. Le test d’histoire initiale distingue conservation du champ et sélection d’un état d’équilibre.",
        ["Demi-épaisseur a et λL en nm, Bextérieur en mT", "Bz(x) en T, jy=−Bz′/μ₀ en A·m⁻² ; choix d’histoire pour la comparaison idéale"],
        ["Plaque homogène dans l’état Meissner, mêmes champs aux faces", "Faible champ, pas de vortex ou de piégeage calculés ; conducteur parfait comparé comme modèle à mémoire"],
        ["Équation différentielle à deux conditions aux limites", "Rotationnel et signe du courant", "Ordre des limites et histoire initiale"],
        ["Calculer B(0)/B₀=1/cosh(a/λL) pour a/λL=1 et 5 et prévoir le sens des courants aux deux faces.", "Comparer plaque épaisse et deux faces proches ; changer l’histoire du conducteur parfait sans changer London.", "Démontrer ΔB=B/λL² et expliquer pourquoi E=0 impose seulement Ḃ=0 ; comparer à la diffusion normale du laboratoire peau."],
        "Exponentielle, hyperboliques et conditions aux limites, avec physique introduite.",
        "Maxwell et résolution d’équations différentielles ; le phénomène supraconducteur est un prolongement.",
        "Phase du condensat, jauge, fluxoïde, type II et vortex, hors de la plaque London simple.", [31,23],
        "Un profil satisfaisant les deux faces et une distinction explicite entre London, peau et conducteur parfait."),
    "faraday": guide(
        "Expliquer une rotation par deux phases propres et tester sa non-réciprocité. Une base circulaire déclarée et des axes de laboratoire fixes permettent un signe reproductible à l’aller-retour.",
        ["Verdet V en rad·T⁻¹·m⁻¹, B longitudinal en T, longueur en cm, λ en nm", "Angles initial/analyseur en degrés ; θ=VBL en radians et modes e±=(ex±i ey)/√2"],
        ["Milieu transparent à rotation pure prescrite ; axes transverses calibrés et miroir à phase commune", "V est prescrit à la longueur d’onde choisie, pas une loi spectrale microscopique calculée"],
        ["Diagonalisation dans une base circulaire", "Matrice de Jones et loi de Malus", "Retour non réciproque versus retour réciproque"],
        ["Calculer θ=VBL et prévoir la transmission entre analyseurs croisés pour un puis deux passages.", "Comparer passage simple et aller-retour ; inverser B puis déplacer l’analyseur pour retrouver l’orientation.", "Décomposer ex en e±, retrouver θ=(k−−k+)L/2 et montrer R(θ)²=R(2θ) ; annoncer ce qui reste prescrit quand λ est modifiée."],
        "Trigonométrie, phase et loi de Malus ; diagonalisation introduite par un exemple.",
        "Polarisation et matrices complexes selon la filière ou par un complément guidé.",
        "Gyrotropie tensorielle, dichroïsme circulaire et relations de réciprocité.", [32,22],
        "Un signe lié à des bases fixes et un double passage qui distingue Faraday d’une simple rotation réciproque."),
    "kerr": guide(
        "Construire et vérifier un profil localisé auto-guidé, puis le comparer à la diffraction libre. Le laboratoire traite le Kerr optique dépendant de l’intensité, avec ses unités et sa réduction monochromatique.",
        ["λvide en μm, n₀, n₂ en 10⁻²⁰ m²·W⁻¹, I₀ en GW·cm⁻² (1 GW·cm⁻²=10¹³ W·m⁻²)", "Distance normalisée z/(n₀k₀y₀²), champ en V·m⁻¹, largeur en m ; I₀=n₀ε₀cE₀²/2"],
        ["Non-linéarité focalisante, enveloppe lente et modèle monochromatique ; Iref=n₀ε₀cE²/2, flux exact Sz=[k/(n₀k₀)]Iref", "Gaussienne libre de même puissance physique intégrée, avec un profil et un pic différents ; pas de Kerr DC ou magnéto-optique"],
        ["Intégrale première d’une équation différentielle non linéaire", "Solution en inverse de cosinus hyperbolique et relation amplitude-largeur", "Adimensionnement et test d’une approximation"],
        ["À n₂ fixé, prévoir l’effet de I₀ multipliée par quatre sur le champ crête et la largeur du profil localisé.", "Comparer les préréglages d’intensité puis augmenter la distance normalisée ; observer le profil auto-guidé et la référence de diffraction libre.", "Vérifier la sech par dérivation et son intégrale première ; sur papier décomposer E³ en ω et 3ω et expliciter la normalisation de l’intensité."],
        "Fonctions hyperboliques, énergie d’un oscillateur fictif et changements d’échelle.",
        "Équations différentielles, amplitudes complexes et diffusion/diffraction comme techniques ; la non-linéarité est un prolongement.",
        "Enveloppes non linéaires, stabilité et solitons ; différencier les trois effets nommés Kerr.", [33,34],
        "Une amplitude et une largeur liées par calcul, et une portée de modèle annoncée sans identifier tout Kerr à une sech."),
    "rayonnement": guide(
        "Passer d’un diagramme dipolaire transverse à une puissance intégrée, puis d’une polarisation induite à une section de diffusion. Rayleigh, résonance et Thomson révèlent trois régimes d’un même modèle.",
        ["Fréquence incidente et propre en THz, γ/ω₀ ; p₀ en 10⁻²⁹ C·m", "Eincident crête en V·m⁻¹ ; intensité en W·m⁻², puissance en W, section efficace en m²"],
        ["Dipôle ponctuel, zone lointaine, source imposée ou électron lié linéaire", "ka≪1 ; kr≫1 ; réaction radiative non résolue dans l’oscillateur simple"],
        ["Projection transverse et retard", "Intégrale d’angle solide", "Analyse asymptotique et section efficace"],
        ["Prévoir les directions où le rayonnement est nul et le facteur de diffusion si f est doublée loin sous f₀.", "Comparer Rayleigh, résonance et Thomson ; choisir ensuite un dipôle imposé et doubler son amplitude.", "Intégrer sin²θ sur la sphère, retrouver P∝ω⁴p₀² et σ=P/I ; relier la loi λ⁻⁴ au ciel bleu avec les limites spectrales et perceptives."],
        "Puissance, trigonométrie et ordre de grandeur ; angle solide introduit progressivement.",
        "Ondes, Poynting et développement dipolaire selon la filière.",
        "Réaction radiative, extinction, diffusion multiple et corrections quantiques.", [28,30],
        "Une puissance indépendante de r, une section en m² et des régimes comparés avec leurs hypothèses."),
    "dynamo": guide(
        "Déduire un seuil d’amplification à partir des valeurs propres d’un modèle α² local. L’hélicité et la diffusion sont confrontées à Rm pour montrer pourquoi un nombre élevé ne suffit pas à entretenir un champ.",
        ["α et U en mm·s⁻¹, diffusivité magnétique en m²·s⁻¹, longueur d’onde L en km", "k=2π/L, temps en années, B₀ en mT ; γ en s⁻¹ et croissance affichée aussi en logarithme"],
        ["Fermeture α² constante prescrite ; deux modes hélicoïdaux de divergence nulle", "Aucune simulation du noyau, convection ou rétroaction ; amplification non saturée du modèle linéaire"],
        ["Élimination E/j dans l’induction MHD", "Mode propre du rotationnel et taux de croissance", "Échelles temporelles, seuil et contre-exemple"],
        ["Calculer k=2π/L et prévoir le signe de γ=±αk−ηmk² pour les deux hélicités.", "Comparer bon mode, mauvaise hélicité et α=0 ; choisir grand Rm sans croissance et modifier U sans changer α.", "Retrouver le seuil |α|>ηmk et montrer que U intervient dans Rm mais pas automatiquement dans α ; expliquer ce qu’il manquerait pour une dynamo terrestre saturée."],
        "Exponentielle, unités et bilan croissance/décroissance sur un modèle accompagné.",
        "Calcul vectoriel, diffusion et valeurs propres comme techniques ; MHD/dynamo sont des prolongements.",
        "Fermeture turbulente, conditions globales, anti-dynamos et rétroaction du champ sur le fluide.", [35,36],
        "Un seuil spectral démontré et une interprétation explicitement limitée d’un modèle local prescrit."),
}


# Notations propres aux prolongements ; les définitions précèdent les formules.
LAB_GUIDES["kerr"]["objects"].insert(0, "x est la position transverse, u son amplitude de champ ; sech(s)=1/cosh(s). k₀=2π/λ est le nombre d’onde dans le vide et y₀ l’échelle de largeur du profil.")
LAB_GUIDES["dynamo"]["objects"].insert(0, "α est un coefficient d’induction prescrit et ηm la diffusivité magnétique. L est la longueur d’onde ; le signe de l’hélicité distingue deux modes propres du rotationnel.")

LAB_LEVELS = {'dipoles': 'MP/PC : électrostatique, gradient, développement limité et énergie dipolaire.',
 'gauss': 'MP/PC : loi de Gauss, symétries, potentiel et capacité ; choisir une surface adaptée.',
 'biotsavart': 'MP/PC : magnétostatique et symétries ; les formules de géométrie finie sont établies ou '
               'fournies.',
 'helmholtz': 'MP/PC : superposition, symétrie et développement limité ; calibration expérimentale du '
              'champ.',
 'drude': 'MP/PC : loi d’Ohm, réponse linéaire et énergie. Drude est un modèle mécanique fourni pour '
          'expliquer la conductivité.',
 'hall': 'Réinvestissement de Lorentz et du potentiel MP/PC ; modèle de Hall à un porteur fourni comme '
         'application de mesure.',
 'induction': 'Acquis de Sup, puis bilans de Spé MP/PC/PSI : induction, conversion et transitoires.',
 'hautparleur': 'Oscillateur forcé, circuit et conversion selon la filière ; couplage électromécanique '
                'accompagné.',
 'hysteresis': 'PSI : milieux magnétiques et transformateur. Pour MP/PC, réinvestissement d’Ampère, '
               'Faraday et des bilans dans un prolongement.',
 'synchrone': 'PSI : machine synchrone. Les outils de stabilité et de couple sont accessibles aux '
              'autres filières dans ce modèle fourni.',
 'asynchrone': 'Amplitudes complexes, induction et bilans de Spé ; le circuit triphasé asynchrone est '
               'un prolongement accompagné.',
 'peau': 'MP/PC : propagation dans un conducteur, diffusion, énergie et comparaison des échelles.',
 'maxwell': 'MP/PC : Maxwell, ondes planes, polarisation et bilan de Poynting.',
 'interfaces': 'MP/PC : réflexion et transmission ; les coefficients obliques TE/TM et Brewster '
               'complètent les cas du programme suivi.',
 'guide': 'Équation d’onde et conditions aux limites de Spé ; le mode TE₁₀ complet est un prolongement '
          'guidé.',
 'antenne': 'MP/PC : ondes, superposition et diffraction. Diagramme d’antenne et pointage sont des '
            'applications accompagnées.',
 'plasma': 'MP/PC : propagation dispersive et milieu conducteur ; le modèle froid collisionnel est '
           'fourni et contrôlé énergétiquement.',
 'dielectrique': 'Ondes et réponses linéaires MP/PC ; polarisation macroscopique, champ local et sphère '
                 'diélectrique selon la filière ou en prolongement.',
 'aimantation': 'MP §7 : Boltzmann et système à deux niveaux ; PSI : milieux magnétiques. Langevin et '
                'champ démagnétisant prolongent ce socle.',
 'meissner': 'Outils MP/PC : Maxwell et équations différentielles ; supraconductivité et équations de '
             'London sont un prolongement.',
 'faraday': 'PC : polarisation ; techniques d’algèbre linéaire et de phases en MP/PC. Le modèle '
            'circulaire de Faraday est un prolongement guidé.',
 'kerr': 'Techniques Spé : équation différentielle, intégrale première et diffraction. Kerr et profil '
         'localisé sont des prolongements.',
 'rayonnement': 'MP/PC : Poynting et rayonnement dipolaire. Diffusion résonante et réaction radiative '
                'demandent les modèles fournis.',
 'dynamo': 'Calcul vectoriel, diffusion et valeurs propres de Spé ; MHD et dynamo α² restent des '
           'prolongements.'}
for _lab, _level in LAB_LEVELS.items():
    LAB_GUIDES[_lab]["levels"]["spe"] = _level

LAB_OBJECTS = {'dipoles': ['q est la valeur positive des charges ±q, en nC ; a leur séparation en m. Le moment dipolaire '
             'p va de −q vers +q et vaut q a.',
             'r est la distance au centre ; le rapport r/a mesure l’éloignement. L’angle règle la '
             'direction du dipôle.',
             'E est le champ électrique en V·m⁻¹ et V le potentiel en V ; une équipotentielle est une '
             'courbe où V est constant.'],
 'gauss': ['Sphère : Q est la charge totale en nC, R son rayon en m et r la distance au centre. E est le '
           'champ électrique en V·m⁻¹ et V le potentiel en V.',
           'Coaxial : a est le rayon du conducteur interne en cm, b celui du conducteur externe et ℓ la '
           'longueur en m. La tension est V_interne−V_externe.',
           'C est la capacité en F ; W l’énergie électrostatique en J. ε₀ est la permittivité du vide.'],
 'biotsavart': ['I est le courant orienté en A, R le rayon de spire en m et ℓ la longueur du fil ou '
                'solénoïde en m. N est le nombre de spires.',
                'B est le champ magnétique en T ; z est la position sur l’axe. μ₀ est la perméabilité du '
                'vide en H·m⁻¹.',
                'Le moment magnétique m=NIπR² est en A·m² ; sa direction suit la règle de la main droite.'],
 'helmholtz': ['R est le rayon commun en m ; d est l’écartement des centres, réglé par d/R. I est le '
               'courant en A et N le nombre de spires de chaque bobine.',
               'z est la position sur l’axe ; B(z) le champ axial en T. B′ et B″ désignent ses dérivées '
               'par rapport à z.',
               'L’uniformité relative mesure la variation de B par rapport à B(0), dans la région '
               'annoncée.'],
 'drude': ['n est la densité de porteurs en m⁻³ ; le curseur règle log₁₀ de sa valeur numérique dans cette '
           'unité. q=±e est leur charge, e étant la charge élémentaire.',
           'τ est le temps de relaxation en fs ; m* est la masse effective en multiples de la masse '
           'électronique mₑ. f est la fréquence en THz et ω=2πf.',
           'E est l’amplitude crête ou l’échelon du champ en V·m⁻¹ ; v la vitesse moyenne, j la densité de '
           'courant en A·m⁻² et σ la conductivité en S·m⁻¹.'],
 'hall': ['I est le courant vers +x en A ; Bz le champ vers +z en T ; w la largeur suivant y et t '
          'l’épaisseur suivant z, en mm.',
          'q=±e est la charge des porteurs et n leur densité en m⁻³ ; le curseur règle log₁₀ de la valeur '
          'numérique de n.',
          'U_H=V(y=−w/2)−V(y=+w/2) est la tension de Hall en V ; E_H est le champ transverse.'],
 'induction': ['Bz est le champ uniforme en T ; ℓ la longueur active du barreau ou largeur du cadre en m ; '
               'la hauteur du cadre est en m.',
               'R est la résistance totale en Ω, L l’inductance du rail en mH et m la masse mobile réglée '
               'en g. v est la vitesse en m·s⁻¹ et i le courant en A.',
               'Φ est le flux magnétique en Wb, la fém une tension en V ; t est le temps en s et W '
               'l’énergie mécanique et magnétique en J.'],
 'hautparleur': ['x est le déplacement de membrane en m, v sa vitesse en m·s⁻¹ et i le courant en A. m est '
                 'sa masse réglée en g, k la raideur en N·m⁻¹ et b l’amortissement en N·s·m⁻¹.',
                 'R est la résistance électrique en Ω et L l’inductance en mH ; f est la fréquence en Hz '
                 'et u la tension en V, d’amplitude crête réglable.',
                 'κ est le coefficient réciproque en N·A⁻¹=V·s·m⁻¹ : il produit la force κi et la tension '
                 'induite κv.'],
 'hysteresis': ['H est le champ magnétique en A·m⁻¹ et B l’induction en T ; Hc est l’échelle coercitive, '
                'Hmax l’amplitude et Bs la contribution saturée. μr est la perméabilité relative '
                'réversible.',
                'ℓ est la longueur moyenne du tore en m, S sa section réglée en cm² ; N₁,N₂ sont les '
                'nombres de spires primaire et secondaire. i₁ est le courant primaire en A, e₂ la fém '
                'secondaire en V.',
                'f est la fréquence en Hz ; l’aire orientée du cycle H–B donne une perte d’énergie '
                'volumique en J·m⁻³ par cycle.'],
 'synchrone': ['ℳ est le moment magnétique du dipôle rotor en A·m² ; B l’amplitude du champ tournant en T '
               'et f sa fréquence en Hz. Le modèle possède une seule paire de pôles.',
               'δ est le retard du rotor en degrés ; T_charge le couple résistant en N·m et T_max le '
               'couple maximal. Leur rapport est sans dimension.',
               'J est le moment d’inertie en kg·m². Le potentiel incliné permet d’identifier les positions '
               'd’équilibre et leur stabilité.'],
 'asynchrone': ['p est le nombre de paires de pôles et f la fréquence électrique en Hz ; Ωs est la vitesse '
                'synchrone et Ωr celle du rotor en rad·s⁻¹. Le glissement s=(Ωs−Ωr)/Ωs est sans dimension.',
                'La tension est efficace par phase en V. R₁,R₂ sont les résistances en Ω, L₁,L₂ les '
                'inductances de fuite en mH et Lm l’inductance de magnétisation en mH. Les paramètres du '
                'rotor sont ramenés au stator.',
                'Les courants sont efficaces en A ; les puissances sont en W et le couple en N·m. La '
                'puissance d’entrefer est celle reçue électromagnétiquement par le rotor.'],
 'peau': ['σ est la conductivité en MS·m⁻¹ et μr la perméabilité relative ; μ=μ₀μr, avec μ₀ la '
          'perméabilité du vide. f est la fréquence en Hz, réglée par son logarithme décimal.',
          'B₀ est le champ de surface en mT ; x mesure la profondeur dans le métal. Pour l’échelon, t est '
          'le temps réglé en ms.',
          'δ est la profondeur de peau harmonique en m ; le coefficient de diffusion magnétique est '
          '1/(μσ), en m²·s⁻¹.'],
 'maxwell': ['E est le champ électrique en V·m⁻¹ et B le champ magnétique en T ; E₀ est l’amplitude d’une '
             'onde. f est la fréquence en GHz, T=1/f la période et t/T le temps réduit.',
             'Le rapport des composantes en quadrature règle la polarisation ; une valeur de module 1 '
             'donne une polarisation circulaire.',
             'Π est le vecteur de Poynting en W·m⁻² ; u est la densité d’énergie en J·m⁻³. Une moyenne '
             'temporelle est prise sur une période.'],
 'interfaces': ['n₁,n₂ sont les indices réels des milieux incident et transmis. θ est l’angle d’incidence '
                'à la normale, en degrés ; λ est la longueur d’onde dans le vide, en nm.',
                'TE signifie que E est perpendiculaire au plan d’incidence ; TM qu’il appartient à ce '
                'plan. r,t sont les coefficients complexes de champ électrique.',
                'R,T sont les rapports de flux d’énergie normaux réfléchi et transmis. Un champ évanescent '
                'peut exister sans flux normal transmis.'],
 'guide': ['a est la largeur du guide en mm ; f la fréquence en GHz et E₀ l’amplitude électrique en V·m⁻¹. '
           'z est la position axiale et z/a la distance réduite.',
           'Le mode TE₁₀ a un champ électrique axial nul et une seule variation suivant la largeur. f_c '
           'est sa fréquence de coupure en Hz.',
           'k_z est le nombre d’onde axial en m⁻¹ ; v_φ est la vitesse de phase et v_g la vitesse de '
           'groupe. t/T est le temps réduit sur une période.'],
 'antenne': ['a est la largeur de l’ouverture et λ la longueur d’onde réglée en mm ; a/λ est sans '
             'dimension.',
             'θ est la direction d’observation et θ₀ la direction de pointage, en degrés. Le diagramme '
             'représente une intensité normalisée.',
             'sinc(u)=sin(u)/u, avec sinc(0)=1, décrit la somme des amplitudes issues d’une ouverture '
             'uniforme.'],
 'plasma': ['n est la densité électronique réglée en 10¹⁸ m⁻³ ; ωp est la pulsation plasma en rad·s⁻¹. ω '
            'est la pulsation de l’onde et ν la fréquence de collision en s⁻¹.',
            'Les curseurs règlent ω/ωp et ν/ωp. E₀ est l’amplitude de champ à z=0 en V·m⁻¹ ; z est réglé '
            'en cm et t/T est le temps réduit.',
            'k est le nombre d’onde complexe en m⁻¹ ; sa partie imaginaire règle l’atténuation. Π est le '
            'flux de Poynting en W·m⁻².'],
 'dielectrique': ['ω₀ est la pulsation propre d’un électron lié, γ son amortissement et χ₀ la force de '
                  'réponse sans dimension. Les curseurs règlent ω/ω₀ et γ/ω₀.',
                  'ε∞ est la permittivité relative de fond ; E₀ le champ imposé en V·m⁻¹ et R le rayon de '
                  'sphère réglé en mm.',
                  'P est la polarisation, moment dipolaire par volume en C·m⁻² ; χ est la susceptibilité '
                  'complexe et εr la permittivité relative.'],
 'aimantation': ['T est la température en K ; μ₀H_ext est le champ appliqué en T. n est la densité de '
                 'moments ou d’électrons liés, réglée en 10²⁷ m⁻³.',
                 'μ est la norme du moment en multiples du magnéton de Bohr μB, en J·T⁻¹. Le rayon orbital '
                 'quadratique effectif est réglé en pm.',
                 'M est l’aimantation en A·m⁻¹ et N le facteur démagnétisant sans dimension ; '
                 'H_int=H_ext−NM définit le champ interne de l’ellipsoïde.'],
 'meissner': ['a est la demi-épaisseur de la plaque et λL la longueur de pénétration de London, en nm. x '
              'est la position entre les faces x=±a.',
              'B₀ est le champ extérieur réglé en mT ; B(x) est le profil intérieur en T. j est la densité '
              'de courant en A·m⁻².',
              'L’histoire indique si le conducteur parfait contenait un champ initial. L’état Meissner '
              'impose un autre état d’équilibre.'],
 'faraday': ['V est la constante de Verdet en rad·T⁻¹·m⁻¹ ; B le champ longitudinal en T, ℓ la longueur '
             'réglée en cm et λ la longueur d’onde en nm.',
             'θ=VBℓ est la rotation en rad ; les angles de polarisation initiale et d’analyseur sont '
             'réglés en degrés.',
             'e₊,e₋ sont les vecteurs des deux polarisations circulaires ; k₊,k₋ leurs nombres d’onde. Les '
             'axes transverses restent ceux du laboratoire au retour.'],
 'kerr': ['λ est la longueur d’onde dans le vide en µm, n₀ l’indice linéaire et n₂ le coefficient Kerr '
          'réglé en 10⁻²⁰ m²·W⁻¹. I₀ est l’intensité de référence au sommet en GW·cm⁻² ; 1 GW·cm⁻²=10¹³ '
          'W·m⁻².',
          'x est la position transverse, u son amplitude réelle de champ en V·m⁻¹ ; sech(s)=1/cosh(s). '
          'k₀=2π/λ est le nombre d’onde dans le vide et y₀ l’échelle de largeur.',
          'z est la distance de propagation et z/(n₀k₀y₀²) la distance réduite. I_ref=n₀ε₀cE²/2 définit '
          'l’intensité de référence ; ε₀ est la permittivité du vide et c la célérité de la lumière.'],
 'rayonnement': ['f est la fréquence incidente et f₀ la fréquence propre en THz ; γ est l’amortissement en '
                 's⁻¹ et ω₀=2πf₀.',
                 'p₀ est l’amplitude du moment dipolaire réglée en 10⁻²⁹ C·m ; E₀ est l’amplitude '
                 'électrique incidente en V·m⁻¹.',
                 'I est l’intensité incidente en W·m⁻², P la puissance diffusée en W et σ=P/I la section '
                 'efficace en m². r est la distance à la source ; k=2π/λ est le nombre d’onde.'],
 'dynamo': ['α est un coefficient d’induction prescrit et U une vitesse caractéristique, en mm·s⁻¹ ; ηm '
            'est la diffusivité magnétique en m²·s⁻¹.',
            'L est la longueur d’onde en km et k=2π/L le nombre d’onde ; B₀ est l’amplitude initiale en mT '
            'et t le temps réglé en années.',
            'Le signe d’hélicité distingue deux modes propres du rotationnel ; γ est leur taux de '
            'croissance en s⁻¹. Rm=UL/ηm est le nombre de Reynolds magnétique.']}
for _lab, _objects in LAB_OBJECTS.items():
    LAB_GUIDES[_lab]["objects"] = _objects
