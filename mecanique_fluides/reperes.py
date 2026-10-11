"""Dix-huit missions physiques : prédire, expérimenter, puis justifier.

Les niveaux désignent les outils mobilisés. Les approfondissements sont guidés
et les attendus obligatoires restent ceux du programme de chaque filière.
"""


LAB_GUIDES = {
    "cinematique": {
        "purpose": "Distinguer un champ de vitesse mesuré en des points fixes, la trajectoire d'une particule et une ligne de courant instantanée. Suivre aussi un élément matériel pour relier sa forme à la conservation de la masse.",
        "techniques": ["Intégrer dR/dt=v(R,t) et appliquer la règle de la chaîne.", "Construire un flux orienté et contrôler div v.", "Comparer géométrie instantanée et évolution temporelle."],
        "first_steps": ["Prédire la trajectoire d'un point dans le champ permanent proposé et distinguer trajectoire et ligne de courant par leur définition.", "Suivre la même particule et un petit élément matériel dans le laboratoire ; comparer leur déplacement aux lignes de courant du champ permanent. Le champ instationnaire de l'exercice 2 se traite ensuite sur papier, sans commande correspondante dans ce laboratoire.", "Justifier l'accélération par la dérivée matérielle, puis vérifier si le changement d'aire est compatible avec div v et le bilan de masse."],
        "levels": {"sup": "Mobiliser dérivation, intégration et bilans de débit ; définir chaque courbe avant de la lire.", "spe": "Réutiliser les équations différentielles et les champs de vecteurs pour distinguer descriptions spatiale et matérielle.", "beyond": "La description lagrangienne et l'étude locale du gradient sont des extensions selon la filière ; elles sont explicitées dans les leçons."},
        "lesson_numbers": [1, 2, 3],
        "expected": "Expliquer sur un exemple pourquoi une vitesse locale indépendante du temps peut produire une accélération, et pourquoi une ligne de courant n'est pas toujours une trajectoire.",
    },
    "newtonien": {
        "purpose": "Relier la déformation d'un petit élément de fluide à la contrainte visqueuse et à la puissance dissipée. Comparer un cisaillement et une rotation rigide qui peuvent avoir des vitesses comparables.",
        "techniques": ["Séparer le gradient en partie symétrique D et antisymétrique W.", "Former la traction σn sur une face orientée.", "Contrôler les unités et la positivité de 2ηD:D."],
        "first_steps": ["Prédire quel mouvement déforme les distances entre deux points et lequel les conserve : cisaillement, rotation ou dilatation.", "Observer l'élément matériel, le tenseur de contrainte et la dissipation en changeant la viscosité dynamique ; repérer ce qui change proportionnellement à η.", "Justifier la dissipation par D:W=0 et expliquer pourquoi ν=η/ρ ne remplace pas η dans une contrainte en Pa."],
        "levels": {"sup": "Distinguer force, force par aire, viscosité dynamique et gradient de vitesse à partir de leurs unités.", "spe": "Mobiliser matrices symétriques et antisymétriques, produit scalaire et loi constitutive.", "beyond": "Le calcul tensoriel local est une extension accompagnée selon la filière ; les fluides non newtoniens exigent une autre loi."},
        "lesson_numbers": [3, 4, 5],
        "expected": "Déterminer une traction avec sa normale et reconnaître une rotation rigide sans dissipation visqueuse de cisaillement.",
    },
    "couette": {
        "purpose": "Construire le profil entre une plaque mobile et une plaque fixe, puis relier le travail de la plaque à la dissipation dans le fluide. Comprendre la superposition du cisaillement et d'un entraînement par pression.",
        "techniques": ["Intégrer u''=0 avec deux conditions d'adhérence.", "Intégrer un profil pour calculer le débit par largeur.", "Comparer puissance mécanique reçue et dissipation volumique."],
        "first_steps": ["Prédire l'effet de doubler l'entrefer h à vitesse de plaque U fixée sur le gradient, la contrainte et le débit.", "Comparer profils et puissances pour deux entrefers ; si la pression est aussi motrice, repérer une éventuelle zone de retour près d'une paroi.", "Retrouver le profil par les conditions aux limites et intégrer η(u')² ; annoncer le sens de la traction sur la plaque mobile."],
        "levels": {"sup": "Faire travailler fonctions affines, intégrales et bilan de puissance dans une géométrie simple.", "spe": "Justifier la réduction de l'équation de mouvement et analyser un profil Couette–Poiseuille.", "beyond": "La résolution exacte d'un écoulement permanent ne prouve pas sa stabilité envers toutes les perturbations ; l'échauffement demande un bilan thermique."},
        "lesson_numbers": [4, 8, 11],
        "expected": "Retrouver la force à fournir, son signe et la puissance par unité d'aire sans confondre une composante de contrainte et la traction sur une face.",
    },
    "poiseuille": {
        "purpose": "Expliquer la sensibilité du débit au rayon d'un tube et les associations de résistances hydrauliques. Distinguer pression imposée, débit imposé, vitesse centrale et vitesse moyenne.",
        "techniques": ["Résoudre l'équation radiale avec régularité sur l'axe et adhérence au bord.", "Intégrer sur des couronnes 2πr dr.", "Associer résistances en série et en parallèle à partir des bilans."],
        "first_steps": ["À Δp=p_entrée−p_sortie fixé, prédire le rapport des débits lorsque le rayon est multiplié par deux. Le renversement de signe de Δp se raisonne ensuite sur papier, car le laboratoire propose une chute de pression positive.", "Comparer profil, débit, puissance et nombre de Reynolds dans le tube proposé. Le réseau de branches est un prolongement sur papier avec l'exercice 12, sans commande de réseau dans ce laboratoire.", "Démontrer Q=πR⁴Δp/(8ηL), puis retrouver sur papier les lois d'association en conservant les débits aux jonctions."],
        "levels": {"sup": "Calculer un débit par intégration et réutiliser les associations de résistances.", "spe": "Contrôler les hypothèses de profil développé, les pertes de charge et les conventions Darcy/Fanning.", "beyond": "Les pertes turbulentes ou d'entrée demandent d'autres lois ; le seuil de transition n'est pas universel."},
        "lesson_numbers": [7, 9, 10],
        "expected": "Justifier la loi en R⁴, vérifier Re avec le diamètre annoncé et dire quelles conclusions dépendent du régime laminaire développé.",
    },
    "diffusion": {
        "purpose": "Voir comment le mouvement d'une paroi pénètre dans un fluide initialement immobile. Comparer la diffusion dans un demi-espace et l'approche d'un profil de Couette dans une couche finie.",
        "techniques": ["Chercher une variable de similitude y/(2√(νt)).", "Lire une solution erfc et des modes de Fourier amortis.", "Comparer des temps à h²/ν."],
        "first_steps": ["Prédire la profondeur pénétrée lorsque le temps est multiplié par quatre et distinguer un demi-espace d'un canal de hauteur h.", "Comparer les profils à plusieurs instants, puis changer ν ; dans le canal fini, observer le rapprochement du profil linéaire final.", "Retrouver δ=2√(νt), vérifier ∂ₜu=νu_yy et expliquer pourquoi les grands indices de Fourier disparaissent plus vite."],
        "levels": {"sup": "Utiliser analyse dimensionnelle, fonctions et ordres de grandeur pour reconnaître une loi en √t.", "spe": "Réutiliser équation de diffusion, séparation des variables et séries de Fourier selon la progression.", "beyond": "Le démarrage idéal instantané crée une incompatibilité au coin y=t=0 ; une couche visqueuse se décrit malgré cette limite du protocole."},
        "lesson_numbers": [5, 8, 11],
        "expected": "Définir une profondeur de diffusion avec sa convention, convertir ν en SI et estimer le temps d'établissement d'une couche finie.",
    },
    "blasius": {
        "purpose": "Relier l'épaisseur d'une couche limite laminaire sur une plaque au frottement local. Voir pourquoi une viscosité faible reste décisive près d'une paroi adhérente.",
        "techniques": ["Équilibrer transport suivant x et diffusion suivant y.", "Employer la variable ξ=y√(U/(νx)).", "Distinguer coefficient local et coefficient moyen par intégration."],
        "first_steps": ["Prédire l'effet de doubler la distance au bord d'attaque sur l'épaisseur et la contrainte pariétale, à U et ν fixés.", "Comparer les profils réduits, l'épaisseur à 99 % et le frottement ; repérer la superposition des profils en variable ξ.", "Retrouver δ99≈4,91√(νx/U) et C_f,x≈0,664/√Re_x, puis intégrer pour expliquer le facteur deux du coefficient moyen."],
        "levels": {"sup": "Pratiquer analyse dimensionnelle, racines et contrôle des unités sur les profils.", "spe": "Mobiliser dérivation, équation différentielle non linéaire et changement de variables dans une extension guidée.", "beyond": "Blasius suppose plaque plane, gradient de pression extérieur nul et couche laminaire ; transition et décollement demandent un autre modèle."},
        "lesson_numbers": [7, 11, 12],
        "expected": "Reconnaître la convention de normalisation f'''+ff''/2=0 et distinguer C_f local, moyen et facteur de frottement d'une conduite.",
    },
    "bernoulli": {
        "purpose": "Interpréter l'échange entre pression, vitesse et altitude dans un écoulement idéal. Employer Venturi, Pitot et vidange tout en gardant les conditions de validité du bilan.",
        "techniques": ["Projeter Euler sur une ligne de courant dans le cadre autorisé.", "Combiner conservation du débit et charge mécanique.", "Intégrer une équation de vidange avec une hauteur variable."],
        "first_steps": ["Prédire le changement de pression dans une section rétrécie à débit constant et distinguer pression statique et pression d'arrêt.", "Comparer les pressions et vitesses, puis la diminution du niveau dans une vidange ; vérifier si la vitesse amont peut être négligée.", "Écrire les termes p/ρ, v²/2 et gz avec la même unité, identifier les points comparés et justifier tout terme supprimé."],
        "levels": {"sup": "Combiner bilans, énergie, débit et intégration élémentaire.", "spe": "Contrôler permanent, incompressible, idéal et ligne de courant ; intégrer une équation de niveau variable.", "beyond": "Bernoulli instationnaire avec ∂ₜφ est une extension selon la filière ; pompes et pertes visqueuses modifient le bilan de charge."},
        "lesson_numbers": [14, 15, 19],
        "expected": "Énoncer les hypothèses avant de comparer deux pressions et expliquer pourquoi une vitesse maximale affichée n'est pas une pression indépendante.",
    },
    "sphere": {
        "purpose": "Relier la traînée d'une sphère à sa vitesse dans le régime de Stokes et tester une mesure de viscosité par chute lente. Distinguer les contributions de pression et de frottement.",
        "techniques": ["Former Re avec le diamètre 2a et la vitesse relative.", "Projeter poids, poussée et traînée dans un bilan vertical.", "Contrôler un régime quasi stationnaire avant d'utiliser 6πηaU."],
        "first_steps": ["Prédire comment la vitesse terminale d'une bille change lorsqu'on double son rayon ou la viscosité, en supposant encore Re≪1.", "Comparer vitesse, force et Reynolds ; suivre la part de pression et la part visqueuse de la traînée.", "Retrouver U_lim=2(ρ_s−ρ)ga²/(9η) et vérifier après le calcul Re, effets de parois et validité du traitement transitoire."],
        "levels": {"sup": "Appliquer un bilan de forces et interpréter un régime terminal.", "spe": "Distinguer inertie du solide, inertie du fluide, approximation de Stokes et contribution de pression.", "beyond": "La masse ajoutée, la mémoire hydrodynamique et les parois peuvent corriger une relaxation naïve ; le temps calculé avec la seule traînée stationnaire reste une estimation de modèle."},
        "lesson_numbers": [7, 13, 19],
        "expected": "Construire une mesure de viscosité cohérente et expliquer les parts 1/3 pression et 2/3 frottement dans la traînée de Stokes.",
    },
    "vortex": {
        "purpose": "Comparer vortex ponctuel et vortex de Rankine, avec un cœur régulier et une circulation extérieure. Distinguer vorticité locale, circulation et existence d'un potentiel global.",
        "techniques": ["Calculer circulation et rotationnel dans une géométrie circulaire.", "Intégrer dp/dr=ρv_θ²/r par morceaux.", "Raccorder pression et vitesse au bord du cœur."],
        "first_steps": ["Prédire où se trouvent la vitesse maximale et la vorticité dans un cœur en rotation solide entouré d'un vortex irrotationnel.", "Comparer les profils de vitesse et de pression en changeant le rayon du cœur, d'abord à Ω fixé puis à Γ fixé.", "Retrouver Γ=2πΩa² et démontrer pourquoi curl v=0 hors du cœur n'impose pas une circulation nulle autour de celui-ci."],
        "levels": {"sup": "Mobiliser mouvement circulaire, intégrales et sens d'une circulation.", "spe": "Réutiliser champs de vecteurs, raccordements et bilans radiaux de quantité de mouvement.", "beyond": "Potentiel multivalué et rôle de la topologie sont explicités comme extensions ; le vortex ponctuel est singulier sur l'axe."},
        "lesson_numbers": [3, 16, 17],
        "expected": "Calculer une pression continue dans Rankine et séparer le domaine local irrotationnel d'un domaine où existe un potentiel global monovalué.",
    },
    "magnus": {
        "purpose": "Expliquer une portance par la dissymétrie de pression autour d'un cylindre avec circulation imposée. Lire son signe et la distinguer d'une condition d'adhérence sur un cylindre réellement tournant.",
        "techniques": ["Superposer écoulement uniforme, doublet et circulation.", "Employer Bernoulli dans le domaine idéal.", "Intégrer la pression avec la normale de la surface."],
        "first_steps": ["Pour U selon +x et Γ positif trigonométrique, prédire le côté de plus grande vitesse et le signe de la force verticale.", "Observer vitesses de surface, pression et résultante lorsque Γ change de signe ou s'annule.", "Intégrer la pression pour obtenir F_y'=-ρUΓ, puis expliquer pourquoi choisir Γ par la rotation ne suffit pas à imposer l'adhérence partout."],
        "levels": {"sup": "Faire travailler le lien vitesse–pression et les symétries d'une force résultante.", "spe": "Mobiliser fonctions trigonométriques, intégrales de pression et superposition de potentiels.", "beyond": "La sélection de la circulation, la couche limite et le décollement sont des questions visqueuses ; le modèle idéal ne prédit pas une traînée réelle complète."},
        "lesson_numbers": [14, 16, 18],
        "expected": "Annoncer une convention de Γ, retrouver la force par unité de longueur et distinguer la portance idéale d'une simulation complète de cylindre tournant.",
    },
    "houle": {
        "purpose": "Relier la profondeur, la longueur d'onde et la fréquence d'une onde de surface, puis comparer déplacements des particules, crêtes et paquets. Explorer la transition gravitaire–capillaire.",
        "techniques": ["Linéariser les conditions de surface avec ka≪1 et a/h≪1.", "Utiliser ω²=(gk+γk³/ρ)tanh(kh).", "Dériver ω(k) et interpréter les limites kh≪1 et kh≫1."],
        "first_steps": ["Prédire la forme des orbites à la surface et près du fond, puis l'effet d'une profondeur diminuée à longueur d'onde fixée.", "Comparer orbites, vitesse de phase et vitesse de groupe ; vérifier que f, λ et h satisfont la dispersion plutôt que les choisir indépendamment.", "Retrouver les limites en eau profonde et peu profonde, puis localiser le minimum de c_φ pour les ondes capillaires-gravitaires."],
        "levels": {"sup": "Distinguer vitesse du signal, célérité des crêtes et vitesse des particules ; contrôler les petites amplitudes.", "spe": "Mobiliser équations d'onde, fonctions hyperboliques, dérivation de dispersion et conditions aux limites.", "beyond": "La dérive de Stokes et les asymptotiques d'un impact sont des prolongements ; une orbite fermée de premier ordre ne prouve pas l'absence de tout transport moyen."},
        "lesson_numbers": [20, 21, 22],
        "expected": "Interpréter une orbite sans la confondre avec une crête et reconnaître les régimes où c_g=c_φ, c_φ/2 ou 3c_φ/2.",
    },
    "acoustique": {
        "purpose": "Relier pression, vitesse particulaire, densité et intensité d'une onde acoustique, puis suivre sa réflexion et sa transmission à une interface. Contrôler l'énergie même si l'amplitude de pression transmise dépasse l'incidente.",
        "techniques": ["Linéariser masse et quantité de mouvement autour du repos.", "Employer Z=ρc et distinguer amplitude crête et efficace.", "Raccorder pression et vitesse normale à une interface."],
        "first_steps": ["Prédire le signe de la réflexion de pression quand l'impédance du second milieu est plus grande, puis celui de la vitesse réfléchie.", "Comparer amplitudes et intensités de part et d'autre ; varier fréquence et pression en gardant le contrôle de la petite perturbation.", "Démontrer les deux raccordements et R+T=1 ; expliquer t_p>1 avec la dépendance de l'intensité à Z."],
        "levels": {"sup": "Consolider ondes progressives, intensité, décibels et unités.", "spe": "Réutiliser linéarisation, impédance, conditions d'interface et bilan de puissance.", "beyond": "L'atténuation visqueuse et les pertes thermiques demandent une convention complexe et un modèle supplémentaire ; le bruit reste analysable par Fourier."},
        "lesson_numbers": [23, 24, 27],
        "expected": "Retrouver les coefficients de pression et de vitesse avec leurs signes, calculer une intensité et préciser les hypothèses de cohérence avant d'ajouter des niveaux.",
    },
    "conduit": {
        "purpose": "Comprendre pourquoi une coupure acoustique concerne un mode transverse particulier. Comparer un mode propagatif, un mode évanescent et le mode plan sans coupure d'un conduit rigide.",
        "techniques": ["Séparer les variables avec la condition de Neumann aux parois rigides.", "Calculer k_c²=(mπ/a)²+(nπ/b)² et k_z²=(ω/c)²-k_c².", "Dériver vitesse de groupe et lire une longueur d'évanescence."],
        "first_steps": ["Prédire quels modes passent à une fréquence donnée et vérifier séparément le mode (0,0), puis comparer les deux dimensions du rectangle.", "Observer les motifs transverses et la propagation axiale juste au-dessus et juste au-dessous d'une coupure ; comparer c_g et c_φ.", "Retrouver f_c, c_gc_φ=c² et 1/κ ; expliquer pourquoi une branche évanescente n'interdit pas le transport par un autre mode."],
        "levels": {"sup": "Lire longueurs d'onde, dimensions et modes simples avec des fonctions cosinus.", "spe": "Mobiliser équation de Helmholtz, conditions aux limites et dispersion guidée.", "beyond": "Les pertes de paroi et la propagation multimodale réelle ne sont pas incluses dans le conduit rigide idéal ; c_φ>c n'est pas la vitesse du transport d'énergie."},
        "lesson_numbers": [23, 24, 25],
        "expected": "Associer une coupure à ses indices (m,n), distinguer c_g de c_φ et convertir une décroissance exponentielle en longueur caractéristique.",
    },
    "diffraction": {
        "purpose": "Relier l'ouverture d'une fente au diagramme de diffraction et distinguer une structure physique d'un alias de mesure. Tester la limite des approximations d'angle et la non-unicité d'une image stroboscopique fixe.",
        "techniques": ["Intégrer des contributions cohérentes sur une ouverture uniforme.", "Lire [sin q/q]², q=πa sinθ/λ, avec sa limite en zéro.", "Comparer les fréquences qui donnent la même phase aux instants d'échantillonnage."],
        "first_steps": ["Prédire si le premier zéro existe lorsque λ/a dépasse un, et décider avant tout calcul si sinθ≈θ peut être acceptable.", "Comparer le diagramme angulaire pour plusieurs ouvertures ; examiner ensuite une mesure échantillonnée ou une cadence stroboscopique proche de la vibration.", "Justifier le diagramme par l'intégrale de phase, puis retrouver une fréquence alias et expliquer pourquoi le filtrage doit précéder l'acquisition."],
        "levels": {"sup": "Travailler interférences, fonctions trigonométriques et contrôle d'une approximation.", "spe": "Réutiliser Fourier, largeur d'un diagramme, échantillonnage et repliement spectral.", "beyond": "Le champ lointain, l'ouverture uniforme et la réponse du capteur sont des hypothèses ; une phase stationnaire décrit une asymptotique, pas une amplitude universelle."},
        "lesson_numbers": [22, 25, 26],
        "expected": "Ne pas transformer λ/a>1 en un angle de premier minimum, proposer une largeur définie et donner plusieurs fréquences compatibles avec un protocole ambigu.",
    },
    "thermo": {
        "purpose": "Distinguer compressibilité isotherme et isentropique pour prévoir une célérité. Comparer une longueur de diffusion thermique à l'échelle d'onde et à la taille d'un conduit.",
        "techniques": ["Dériver χ_T et χ_s à partir d'une loi d'état de gaz parfait.", "Former c²=1/(ρχ_s) dans le modèle acoustique isentropique.", "Comparer δ_th=√(2D_th/ω) à c/ω et à un rayon de paroi."],
        "first_steps": ["Prédire laquelle des compressibilités est la plus grande et laquelle des célérités est la plus rapide pour γ>1.", "Comparer les valeurs et la longueur de diffusion thermique à c/ω dans le laboratoire. La comparaison avec un rayon de conduit se fait ensuite sur papier avec l'exercice 38 ; ce rayon n'est pas un curseur du laboratoire.", "Retrouver χ_T=1/p et χ_s=1/(γp), puis expliquer pourquoi les rapports d'échelle ne définissent pas seuls une interpolation entre les deux célérités."],
        "levels": {"sup": "Combiner gaz parfait, unités et analyse dimensionnelle pour lire un ordre de grandeur.", "spe": "Mobiliser dérivées thermodynamiques, petites perturbations et diffusion thermique.", "beyond": "Un modèle thermoacoustique avec conditions thermiques aux murs est nécessaire pour calculer précisément dispersion et atténuation dans un petit conduit."},
        "lesson_numbers": [4, 23, 27],
        "expected": "Annoncer la transformation thermodynamique et distinguer une faible diffusion sur l'échelle d'onde d'un effet de paroi important dans un microconduit.",
    },
    "mhd": {
        "purpose": "Comparer le freinage de Hartmann dans un liquide conducteur et une onde d'Alfvén dans un régime idéal. Comprendre le rôle du circuit électrique, du champ imposé et de l'énergie magnétique.",
        "techniques": ["Former j=σ_e(E+v×B) et calculer j×B avec son signe.", "Résoudre le profil de Hartmann et développer sa limite B→0.", "Éliminer une variable dans les deux équations linéaires d'Alfvén."],
        "first_steps": ["Pour v selon +x, B selon +y et E_z=0, prévoir le sens du courant et de la force magnétique ; annoncer la fermeture électrique utilisée.", "Comparer le profil de Hartmann au profil sans champ et observer l'effet de Ha ; examiner séparément la vitesse et l'énergie de l'onde d'Alfvén.", "Retrouver la limite de Poiseuille plan et vérifier Rm≪1 pour Hartmann ; établir c_A et l'équipartition pour l'onde idéale sans transporter les hypothèses d'un régime à l'autre."],
        "levels": {"sup": "Entrer par produits vectoriels, unités et bilan de forces ; le cadre MHD est une extension guidée.", "spe": "Réutiliser conduction, force de Lorentz, équation différentielle et ondes couplées.", "beyond": "Champ imposé à faible Rm et onde idéale d'induction sont deux régimes distincts ; changer la fermeture du circuit change le courant et le freinage."},
        "lesson_numbers": [5, 6, 28],
        "expected": "Lire Ha et Rm avec leurs longueurs déclarées, justifier le signe du freinage et expliquer le partage d'énergie d'une onde d'Alfvén.",
    },
    "navier": {
        "purpose": "Relier une solution exacte bidimensionnelle de Taylor–Green à ses champs de pression, vorticité et énergie. Situer ce contrôle dans les équations de mouvement et dans la question mathématique tridimensionnelle.",
        "techniques": ["Substituer une solution dans continuité et quantité de mouvement.", "Intégrer le bilan d'énergie sur un domaine périodique.", "Comparer les temps L/U et L²/ν plutôt qu'un seuil universel."],
        "first_steps": ["Prédire la décroissance de l'amplitude et de l'énergie lorsque la viscosité augmente, puis le rapport entre leurs exposants.", "Comparer vitesse, pression, vorticité et énergie de Taylor–Green à plusieurs instants ; vérifier l'identité entre perte d'énergie et dissipation.", "Retrouver A=Ue^{−2νk²t} et expliquer ce qu'une solution exacte 2D ou une borne L² ne démontre pas pour toutes les données 3D ; distinguer l'énoncé historique de l'annonce Clay datée."],
        "levels": {"sup": "Pratiquer unités, exponentielle et bilans dans une solution explicitement donnée.", "spe": "Mobiliser équations locales, intégrations par parties et vorticité dans une extension guidée selon la filière.", "beyond": "Le programme PSI cité exclut Euler et Navier–Stokes ; l'atelier accompagne leur étude et distingue une preuve globale d'un calcul particulier. Le repère Clay est daté du 6 octobre 2026."},
        "lesson_numbers": [5, 6, 7],
        "expected": "Contrôler un bilan analytique, annoncer dimension et frontières, puis expliquer sans extrapolation le lien et la différence avec le problème 3D de Fefferman.",
    },
    "hydrostatique": {
        "purpose": "Construire les forces de pression, la poussée et les sauts capillaires à partir de la géométrie. Distinguer une colonne liquide incompressible d'une atmosphère soumise à une hypothèse thermodynamique.",
        "techniques": ["Intégrer ∇p=ρg en fixant une pression de référence.", "Fermer une surface pour appliquer le théorème de Gauss.", "Équilibrer énergie de surface ou force capillaire et poids."],
        "first_steps": ["Prédire comment la pression change avec l'altitude ; préciser si la densité ou la température est supposée constante.", "Comparer les profils de pression du laboratoire. Les volumes immergés et les effets de rayon ou d'angle de contact sont des prolongements à lire dans la galerie et à calculer sur papier avec les exercices 25 et 27, sans curseurs correspondants dans ce laboratoire.", "Retrouver la loi hydrostatique affichée, puis justifier sur papier Archimède avec une surface fermée et une pression atmosphérique commune ; compter les interfaces dans le saut de Laplace."],
        "levels": {"sup": "Appliquer statique, pression, poussée, gaz parfait et équilibre de forces.", "spe": "Mobiliser intégrales sur une surface, Gauss et stratifications isotherme ou isentropique.", "beyond": "Le volume immergé ne suffit pas à décider une stabilité de roulis ; température réelle, mouillage et courbures imposent des informations supplémentaires."},
        "lesson_numbers": [15, 19, 20],
        "expected": "Calculer une force avec sa référence de pression, compter les interfaces et distinguer équilibre de translation et stabilité de rotation.",
    },
}


# Grandeurs réglables et cadre de chaque expérience.
LAB_OBJECTS = {'cinematique': {'objects': ['La position r et la vitesse v sont en m et m·s⁻¹ ; le temps t est en s.',
                             'a règle l’étirement, Ω la rotation et U la translation. L est la '
                             'demi-largeur de la fenêtre en m.',
                             'Une ligne de courant est tangente au champ à un instant ; une trajectoire '
                             'suit le même point au cours du temps.'],
                 'assumptions': ['Champ plan permanent, incompressible ; coefficients uniformes.',
                                 'Le carré représente un petit élément matériel transporté par ce '
                                 'champ.']},
 'newtonien': {'objects': ['η est une viscosité dynamique : 1 mPa·s = 10⁻³ Pa·s ; ρ est une masse '
                           'volumique.',
                           'Les taux de cisaillement γ̇, d’extension a et de rotation Ω sont en s⁻¹.',
                           'D est la partie symétrique du gradient de vitesse ; τ est la contrainte '
                           'visqueuse en Pa. Le produit D:D désigne la somme des carrés de ses '
                           'coefficients.'],
               'assumptions': ['Fluide newtonien incompressible, de viscosité uniforme.',
                               'On compare des mouvements plans prescrits, pas un écoulement calculé '
                               'avec des parois.']},
 'couette': {'objects': ['h est la distance entre les plaques ; y va de la plaque basse à la plaque '
                         'haute.',
                         'U₀ et U₁ sont les vitesses des plaques ; G=−∂p/∂x est en Pa·m⁻¹ et η en '
                         'mPa·s.',
                         'u(y) est la vitesse longitudinale. Le débit affiché est un débit par unité de '
                         'largeur, en m²·s⁻¹.'],
             'assumptions': ['Fluide newtonien incompressible ; écoulement permanent, parallèle et '
                             'développé.',
                             'Adhérence aux deux plaques ; effets d’entrée et de bord négligés.']},
 'poiseuille': {'objects': ['R et L définissent un tube circulaire ; r est la distance à l’axe.',
                            'Δp est la pression d’entrée moins celle de sortie ; η est en mPa·s et ρ en '
                            'kg·m⁻³.',
                            'Q est le débit volumique en m³·s⁻¹ ; la vitesse moyenne sert à calculer le '
                            'nombre de Reynolds avec le diamètre 2R.'],
                'assumptions': ['Fluide newtonien incompressible, régime laminaire permanent et '
                                'développé.',
                                'Adhérence à la paroi ; la validité laminaire doit être contrôlée après '
                                'chaque réglage.']},
 'diffusion': {'objects': ['y mesure la distance à la paroi ; h est réglé en mm.',
                           'ν mesure la diffusion de quantité de mouvement : 1 mm²·s⁻¹ = 10⁻⁶ m²·s⁻¹.',
                           'u(y,t) est la vitesse parallèle ; erfc est la fonction d’erreur '
                           'complémentaire. Dans le canal, les deux parois sont séparées par h.'],
               'assumptions': ['Fluide newtonien, incompressible, viscosité uniforme ; aucun gradient '
                               'de pression.',
                               'Une plaque démarre idéalement à t=0 ; dans le canal, la seconde plaque '
                               'reste fixe.']},
 'blasius': {'objects': ['x suit la plaque et y lui est perpendiculaire ; U∞ est la vitesse loin de la '
                         'plaque.',
                         'ν est la viscosité cinématique convertie en m²·s⁻¹ ; ρ est la masse volumique en kg·m⁻³. Reₓ=U∞x/ν est sans dimension.',
                         'δ₉₉ est la distance où la vitesse atteint 99 % de U∞ ; C_f,x est le '
                         'coefficient de frottement local.'],
             'assumptions': ['Écoulement plan permanent, laminaire et incompressible ; plaque plane '
                             'avec adhérence.',
                             'Vitesse extérieure constante et gradient de pression nul ; approximation '
                             'de couche limite.']},
 'bernoulli': {'objects': ['Q est le débit volumique : 1 L·s⁻¹ = 10⁻³ m³·s⁻¹ ; D₁ et D₂ sont les '
                           'diamètres.',
                           'ρ est en kg·m⁻³, η en mPa·s, ε la rugosité en mm, L la longueur en m et '
                           'z₂−z₁ la dénivellation.',
                           'ΣK est le coefficient des pertes singulières ; α corrige l’énergie '
                           'cinétique. Le rendement de pompe est un rapport sans dimension entre 0 et '
                           '1.'],
               'assumptions': ['Bilan permanent d’un liquide incompressible ; vitesse moyenne dans '
                               'chaque section.',
                               'Les pertes dépendent des corrélations indiquées ; le bilan idéal '
                               's’obtient en les annulant.']},
 'sphere': {'objects': ['R est le rayon ; U est la vitesse relative entre la sphère et le fluide.',
                        'ρ et ρ_s sont les masses volumiques du fluide et du solide ; η est la '
                        'viscosité dynamique.',
                        'La traînée est une force en N. Le nombre de Reynolds est calculé avec le '
                        'diamètre 2R.'],
            'assumptions': ['Sphère rigide isolée dans un fluide newtonien incompressible loin des '
                            'parois.',
                            'La loi de Stokes suppose un nombre de Reynolds petit devant 1 ; le '
                            'transitoire est une estimation quasi stationnaire.']},
 'vortex': {'objects': ['r est la distance à l’axe et v_θ la vitesse tangentielle en m·s⁻¹.',
                        'Le cœur de rayon R tourne à Ω ; Γ est la circulation en m²·s⁻¹, égale à 2πΩR².',
                        'La pression est comparée à sa valeur loin du cœur ; la vorticité est le '
                        'rotationnel de la vitesse, en s⁻¹.'],
            'assumptions': ['Vortex de Rankine plan, permanent et incompressible.',
                            'Modèle prescrit sans viscosité ; vitesse et pression sont raccordées au '
                            'bord du cœur.']},
 'magnus': {'objects': ['ρ est la masse volumique en kg·m⁻³ ; la force affichée est une force par longueur du '
                        'cylindre, en N·m⁻¹.',
                        'Γ est une circulation imposée, pas une vitesse de rotation de paroi.',
                        'La normale extérieure au cylindre fixe le signe de l’intégrale de pression.'],
            'assumptions': ['Fluide idéal incompressible, écoulement plan permanent autour d’un '
                            'cylindre.',
                            'Le modèle impose l’imperméabilité, mais ne décrit ni l’adhérence visqueuse '
                            'ni la sélection réelle de Γ.']},
 'houle': {'objects': ['ρ est la masse volumique en kg·m⁻³ ; k=2π/λ est le nombre d’onde en m⁻¹ et ω la pulsation '
                       'en rad·s⁻¹.',
                       'La vitesse de phase suit les crêtes ; la vitesse de groupe suit l’enveloppe '
                       'd’un paquet étroit.',
                       'Les trajectoires dessinées sont les orbites de premier ordre autour de la '
                       'position au repos.'],
           'assumptions': ['Fluide idéal incompressible et fond horizontal ; surface libre de faible '
                           'amplitude.',
                           'Les critères ka≪1 et a/h≪1 doivent être contrôlés ; les corrections non '
                           'linéaires ne sont pas simulées.']},
 'acoustique': {'objects': ['L’impédance Z=ρc est en Pa·s·m⁻¹ ; elle relie surpression et vitesse '
                            'particulaire.',
                            'R et T sont des rapports d’intensités ; les coefficients de pression sont '
                            'des rapports d’amplitudes.',
                            'La pression réglée est une amplitude crête ; l’intensité moyenne est en '
                            'W·m⁻².'],
                'assumptions': ['Ondes planes de faible amplitude ; deux fluides homogènes, sans '
                                'pertes.',
                                'Incidence normale sur une interface plane ; pression et vitesse '
                                'normale sont continues.']},
 'conduit': {'objects': ['c est la célérité en m·s⁻¹ ; les indices m,n sont des entiers positifs ou '
                         'nuls.',
                         'Le nombre d’onde axial k_z détermine la phase suivant l’axe ; sous la '
                         'coupure, il devient imaginaire.',
                         'Une onde évanescente décroît spatialement ; elle ne possède pas le même '
                         'transport qu’un mode propagatif.'],
             'assumptions': ['Conduit rectangulaire, parois rigides, fluide homogène ; pertes '
                             'négligées.',
                             'Un seul mode transverse est choisi ; la vitesse normale s’annule aux '
                             'parois.']},
 'diffraction': {'objects': ['λ=c/f est la longueur d’onde ; θ est l’angle par rapport à la normale à '
                             'la fente.',
                             'Le diagramme représente une intensité relative, normalisée au maximum '
                             'central.',
                             'La fonction sinc est définie par sinc(x)=sin(x)/x, avec sinc(0)=1.'],
                 'assumptions': ['Fente uniformément excitée ; modèle scalaire et observation en champ '
                                 'lointain.',
                                 'L’approximation des petits angles n’est utilisée que lorsqu’elle est '
                                 'annoncée.']},
 'thermo': {'objects': ['γ=Cp/Cv est le rapport des capacités thermiques ; M est convertie en kg·mol⁻¹.',
                        'La diffusivité thermique D_th est réglée en mm²·s⁻¹ ; la fréquence f est en '
                        'Hz.',
                        'χ_T et χ_s sont les compressibilités isotherme et isentropique, en Pa⁻¹.'],
            'assumptions': ['Gaz parfait autour d’un équilibre uniforme ; petites perturbations.',
                            'Les échelles de diffusion comparent les régimes thermiques ; elles ne '
                            'remplacent pas un calcul complet des pertes acoustiques.']},
 'mhd': {'objects': ['ρ est la masse volumique en kg·m⁻³. Le courant j est en A·m⁻² ; la force j×B est une force par '
                     'volume.',
                     'Pour Hartmann, h est la demi-hauteur du canal en mm et G le gradient moteur en '
                     'Pa·m⁻¹.',
                     'Pour Alfvén, λ et le déplacement sont en m ; μ₀ est la perméabilité du vide.'],
         'assumptions': ['Milieu conducteur homogène, modèle non relativiste ; conditions électriques '
                         'de Hartmann déclarées dans le cours.',
                         'L’onde d’Alfvén est une perturbation linéaire autour d’un champ uniforme ; le '
                         'modèle ne simule pas une dynamo.']},
 'navier': {'objects': ['t est le temps en s et ρ la masse volumique en kg·m⁻³ ; k=2π/L est le nombre d’onde.',
                        'La vitesse, la pression et l’énergie sont calculées pour la solution de '
                        'Taylor–Green.',
                        'La dissipation est une puissance en W ; elle mesure la diminution d’énergie '
                        'cinétique.'],
            'assumptions': ['Fluide incompressible newtonien ; domaine plan périodique, sans force '
                            'extérieure.',
                            'Cette famille exacte régulière ne résout pas le problème général '
                            'tridimensionnel de Navier–Stokes.']},
 'hydrostatique': {'objects': ['Dans le liquide, la profondeur est positive vers le bas ; dans '
                               'l’atmosphère, l’altitude est positive vers le haut.',
                               'p₀ est une pression absolue ; une différence de pression possède la '
                               'même unité, Pa.',
                               'La poussée d’Archimède dépend du volume de fluide déplacé ; g est '
                               'l’accélération de pesanteur.'],
                   'assumptions': ['Fluide au repos dans une pesanteur uniforme.',
                                   'Liquide incompressible ou atmosphère idéale isotherme, selon le '
                                   'mode choisi.']}}
for _lab, _definitions in LAB_OBJECTS.items():
    LAB_GUIDES[_lab].update(_definitions)

LAB_LEVELS = {'cinematique': 'PC §4.3 : champ eulérien, lignes de courant numériques et dérivée particulaire. Le '
                'suivi détaillé d’un élément matériel est un prolongement.',
 'newtonien': 'PC §4.3 et parcours PSI : cisaillement newtonien et bilans. La décomposition tensorielle '
              'générale est un prolongement accompagné.',
 'couette': 'Outils PC/PSI : viscosité, adhérence, équations différentielles et puissances. La '
            'dérivation locale depuis Navier–Stokes est fournie comme prolongement.',
 'poiseuille': 'Outils PC/PSI : bilans, viscosité et nombres de Reynolds. La résolution radiale exacte '
               'et les réseaux prolongent ces techniques.',
 'diffusion': 'MP/PC : équation de diffusion et temps caractéristique ; application visqueuse guidée. '
              'La résolution de Navier–Stokes reste un prolongement selon la filière.',
 'blasius': 'Techniques Spé : changement de variables, équation différentielle et frottement. La '
            'théorie de Blasius est un prolongement spécialisé.',
 'bernoulli': 'PC §4.3 : Bernoulli permanent incompressible. Pompes et pertes prolongent les bilans '
              'énergétiques des systèmes ouverts MP/PC/PSI.',
 'sphere': 'PC §4.3 : nombre de Reynolds et choix d’une traînée linéaire ou quadratique. La '
           'démonstration complète du champ de Stokes est un prolongement.',
 'vortex': 'PC §4.3 : rotationnel et potentiel des vitesses ; calculs de Rankine et topologie du '
           'domaine comme prolongements.',
 'magnus': 'PC §4.3 : vitesse, pression et Bernoulli. Doublet, fonction de courant et sélection de la '
           'circulation sont des prolongements.',
 'houle': 'Techniques Spé : conditions aux limites, dispersion, vitesse de phase et de groupe. La houle '
          'gravitaire-capillaire est un prolongement accompagné.',
 'acoustique': 'PC §6.1.2 et §6.3 : linéarisation, onde sonore, impédance et interface ; bilans et '
               'amplitudes complexes à réinvestir.',
 'conduit': 'PC : acoustique et conditions aux limites. Modes transverses et fréquence de coupure '
            'prolongent l’étude des ondes planes.',
 'diffraction': 'Techniques MP/PC : superposition d’ondes et différence de phase. Le modèle acoustique '
                'de fente réinvestit la diffraction optique.',
 'thermo': 'MP/PC : gaz parfait, isentropique, compressibilité et diffusion thermique ; lien explicite '
           'avec la propagation acoustique PC.',
 'mhd': 'Outils MP/PC/PSI : Lorentz, Ohm, induction et bilans. Hartmann et Alfvén sont des '
        'prolongements interdisciplinaires.',
 'navier': 'Outils Spé : champs, équation différentielle et bilan dissipatif. Navier–Stokes et '
           'Taylor–Green sont ici des prolongements, notamment en PSI.',
 'hydrostatique': 'Acquis de Sup : équilibre, pression, poussée d’Archimède et gaz parfait ; '
                  'réinvestissement dans les bilans de Spé.'}
for _lab, _level in LAB_LEVELS.items():
    LAB_GUIDES[_lab]["levels"]["spe"] = _level
