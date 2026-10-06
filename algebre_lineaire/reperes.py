"""Buts, portes d'entrée et gestes de départ des laboratoires d'algèbre.

Les niveaux désignent les acquis mobilisés dans une progression pédagogique.
Les objets spécialisés sont présentés comme des prolongements guidés ; les
attendus du programme dépendent de la filière, comme le précise l'interface.
"""


LAB_GUIDES = {
    "anneaux": {
        "purpose": (
            "Décider si une même matrice possède un inverse lorsque l'on change l'ensemble de calcul. "
            "L'expérience fait travailler une question essentielle : pourquoi « déterminant non nul » suffit-il dans un corps, mais pas dans un anneau ?"
        ),
        "techniques": [
            "Construire l'inverse avec l'adjugée et contrôler son ensemble de coefficients.",
            "Employer Bézout pour reconnaître une unité modulo un entier.",
            "Compter les bases en choisissant successivement des colonnes indépendantes.",
        ],
        "first_steps": [
            "Choisir « Dense : Q ou Z ? » : noter det U, prévoir si l'inverse rationnel restera entier, puis passer de ℚ à ℤ sans changer U.",
            "Choisir « Dense non unité modulo 6 » : chercher pourquoi le déterminant ne possède pas d'inverse modulo 6, même s'il n'est pas nul.",
            "Choisir « Dense unimodulaire », puis faire varier n dans le cardinal de GLₙ(𝔽ₚ) : retrouver les exclusions pⁿ−pᵏ au choix de chaque colonne.",
        ],
        "levels": {
            "sup": "Réutiliser déterminants, systèmes linéaires et Bézout ; distinguer un nombre non nul d'un élément inversible avant toute division.",
            "spe": "Relier inversibilité, bases et dénombrement ; justifier le cardinal de GLₙ sur un corps fini plutôt que retenir sa formule.",
            "beyond": "Explorer les anneaux avec diviseurs de zéro et comprendre pourquoi un pivot non inversible n'interdit pas toujours l'inversibilité de la matrice.",
        },
        "lesson_numbers": [1, 2, 6],
        "expected": "Savoir annoncer l'ensemble de calcul et y justifier chaque inverse ou division utilisé.",
    },
    "geometrie": {
        "purpose": (
            "Faire agir deux transformations linéaires sur un cube, puis inverser leur ordre. "
            "La figure aide à séparer trois notions que le calcul peut confondre : composition, conservation du volume et conservation de l'orientation."
        ),
        "techniques": [
            "Lire les images des vecteurs de base dans les colonnes d'une matrice.",
            "Interpréter AB comme l'application de B puis de A à un vecteur colonne.",
            "Relier le signe et la valeur absolue du déterminant à la géométrie.",
        ],
        "first_steps": [
            "Avant de comparer AB et BA dans « Volume et non-commutation », prévoir si l'ordre compte ; identifier ensuite un sommet dont les deux images diffèrent.",
            "Choisir « Orientation de l'espace » : lire le signe de det A et distinguer renversement d'orientation et changement de volume.",
            "Choisir « Écrasement sur un plan » : relier det A=0, perte de dimension de l'image et impossibilité de reconstruire tous les vecteurs initiaux.",
        ],
        "levels": {
            "sup": "Consolider matrices d'applications linéaires, composition, image, noyau et déterminant grâce à un objet géométrique dont on suit les sommets.",
            "spe": "Distinguer changement de base, opération sur les lignes et transformation réelle de l'objet ; mobiliser les invariants d'une similitude.",
            "beyond": "Interpréter GLₙ comme un groupe agissant sur l'espace et distinguer ses sous-groupes liés au volume, à l'orientation ou à une métrique.",
        },
        "lesson_numbers": [3, 5],
        "expected": "Pouvoir expliquer une déformation à partir de sa matrice, sans déduire une identité exacte de sa seule apparence.",
    },
    "lie": {
        "purpose": (
            "Observer comment un mouvement continu de matrices se décrit au voisinage de l'identité. "
            "En composant deux petits mouvements dans des ordres opposés, on fait apparaître le commutateur XY−YX et son rôle de premier défaut de commutation."
        ),
        "techniques": [
            "Développer une exponentielle matricielle au voisinage de zéro.",
            "Comparer un défaut d'ordre h à un défaut d'ordre h².",
            "Dériver une identité de conservation pour obtenir une condition linéaire.",
        ],
        "first_steps": [
            "Choisir « Trois rotations d'axes obliques » et comparer l'orbite exp(tX)v à sa tangente (I+tX)v près de t=0.",
            "Prévoir l'effet d'une diminution du « Petit pas h », puis lire les erreurs, notamment celle du commutateur de groupe divisé par h², et identifier sa limite [X,Y].",
            "Choisir « Générateurs denses sp4 » et comparer la condition XᵀJ+JX=0 à la conservation EᵀJE=J par E=exp(tX).",
        ],
        "levels": {
            "sup": "Entrer par le produit matriciel, les dérivées et les développements limités ; les algèbres de Lie sont ici un prolongement guidé.",
            "spe": "Réutiliser séries, exponentielle et équations différentielles linéaires, lorsqu'elles sont étudiées, pour passer d'une conservation globale à une relation infinitésimale.",
            "beyond": "Étudier le lien entre groupes de matrices et algèbres de Lie ; interpréter le crochet comme une information sur les mouvements composés.",
        },
        "lesson_numbers": [17, 18, 21],
        "expected": "Savoir justifier pourquoi l'ordre h² du commutateur de groupe révèle XY−YX et distinguer preuve exacte et contrôle numérique.",
    },
    "gauss": {
        "purpose": (
            "Décider si quatre équations déterminent une solution, plusieurs solutions ou aucune. "
            "L'expérience apprend à produire un certificat de compatibilité et une description complète des solutions, plutôt qu'à obtenir seulement un vecteur affiché."
        ),
        "techniques": [
            "Échelonner simultanément A et le second membre dans [A|b].",
            "Comparer rg A et rg[A|b] pour décider la compatibilité.",
            "Utiliser les variables libres et le théorème du rang pour décrire le noyau.",
        ],
        "first_steps": [
            "Choisir « 4 équations dépendantes, rang 3 » : suivre les pivots et repérer l'équation redondante ainsi que la variable libre.",
            "Avant « La même matrice, incompatible », prévoir l'effet du changement de b ; retrouver ensuite la ligne 0=c non nulle qui certifie l'absence de solution.",
            "Choisir « Système surdéterminé » : comparer nombre d'équations, rang et dimension du noyau ; vérifier la solution ou la famille proposée par substitution.",
        ],
        "levels": {
            "sup": "Maîtriser le pivot de Gauss, les bases de l'image et du noyau, puis écrire les solutions sous la forme x₀+Ker A.",
            "spe": "Employer le rang et les sous-espaces comme certificats ; distinguer opérations élémentaires, équivalence matricielle et similitude dans les problèmes de réduction.",
            "beyond": "Comparer calcul exact et calcul approché : un petit résidu ne garantit pas une petite erreur lorsque le système est mal conditionné.",
        },
        "lesson_numbers": [4, 6],
        "expected": "Savoir conclure avec une justification du rang, de la compatibilité et du nombre de paramètres libres.",
    },
    "spectre": {
        "purpose": (
            "Comparer deux matrices denses 6×6 de même polynôme caractéristique mais aux chaînes différentes. "
            "La question est de déterminer ce que les valeurs propres disent réellement, et quelles informations supplémentaires révèlent les noyaux de (A−λI)ᵏ."
        ),
        "techniques": [
            "Distinguer multiplicité d'une racine et dimension de son espace propre.",
            "Calculer les dimensions de noyaux successifs et leurs accroissements.",
            "Tester la diagonalisation dans le corps choisi, sans oublier le caractère scindé.",
        ],
        "first_steps": [
            "Choisir « Deux chaînes 4+2 » : prévoir les dimensions des noyaux depuis le dessin, puis comparer à « Même χ, autre Jordan » et relever χ et μ.",
            "Lire une chaîne dessinée : après k applications de A−λI, compter combien de ses vecteurs sont devenus nuls.",
            "Choisir « Rotation et choix du corps » dans « Matrice exemple » et passer de ℝ à ℂ : expliquer pourquoi le verdict de diagonalisation change.",
        ],
        "levels": {
            "sup": "Entrer par les noyaux, rangs et compositions d'applications ; la forme de Jordan est présentée comme une extension, sans exiger sa classification.",
            "spe": "Mobiliser espaces propres et critères de diagonalisation ; en MP/MPI, exploiter aussi le polynôme minimal et les sous-espaces caractéristiques.",
            "beyond": "Reconstruire la forme de Jordan à partir des accroissements des noyaux ; comprendre pourquoi le spectre seul ne classe pas les similitudes.",
        },
        "lesson_numbers": [8, 10, 13],
        "expected": "Savoir présenter deux matrices de même χ dont la structure diffère et désigner l'invariant qui permet de les distinguer.",
    },
    "dunford": {
        "purpose": (
            "Décomposer une dynamique linéaire en une partie semi-simple D et une partie nilpotente N qui commutent. "
            "Les chaînes et le calcul polynomial rendent visible ce qui relève des valeurs propres, et ce qui conserve une mémoire transitoire le long des chaînes."
        ),
        "techniques": [
            "Certifier A=D+N, DN=ND et Nᵛ=0 par des égalités matricielles.",
            "Utiliser Bézout pour inverser un polynôme modulo le polynôme minimal.",
            "Développer les puissances d'une somme de deux matrices qui commutent.",
        ],
        "first_steps": [
            "Choisir « Trois valeurs propres » : lire D et N dans les matrices exactes, puis vérifier la somme A=D+N et la commutation.",
            "Prévoir l'indice ν depuis la chaîne la plus longue ; suivre les rangs de Nᵏ et retrouver le premier exposant donnant Nᵛ=0.",
            "Choisir « Semi-simple sur R » : observer que D peut être semi-simple sans être diagonalisable sur ℝ ; comparer au verdict sur ℂ.",
        ],
        "levels": {
            "sup": "Entrer par puissances matricielles, commutation et binôme ; Dunford est un prolongement guidé, dont on vérifie d'abord les identités proposées.",
            "spe": "Réutiliser réduction et polynômes annulateurs ; en MP/MPI, mobiliser polynôme minimal, Bézout et décomposition des noyaux pour préparer cette extension.",
            "beyond": "Construire Dunford par Newton dans une algèbre quotient et calculer puissances ou exponentielles en séparant contributions semi-simples et nilpotentes.",
        },
        "lesson_numbers": [10, 12, 13],
        "expected": "Savoir vérifier une décomposition proposée, lire son indice de nilpotence et préciser le corps sur lequel D est diagonalisable.",
    },
    "cyclique": {
        "purpose": (
            "Itérer un vecteur v par une matrice A et mesurer quelle partie de l'espace ces itérés explorent. "
            "Une même matrice peut être entièrement décrite à partir d'un bon vecteur, mais presque invisible à partir d'un vecteur propre."
        ),
        "techniques": [
            "Calculer le rang de (v,Av,…,Aⁿ⁻¹v).",
            "Traduire une dépendance linéaire entre itérés en récurrence scalaire.",
            "Construire une matrice compagnon dans une base d'itérés.",
        ],
        "first_steps": [
            "Choisir « La suite et sa récurrence » : suivre la croissance du rang jusqu'à 6 et lire la relation portée par le dernier retour du graphe.",
            "Prévoir le rang à partir d'un vecteur propre, puis choisir « Un vecteur propre ne suffit pas » : expliquer le rang 1 malgré une matrice cyclique.",
            "Choisir « L'endomorphisme n'est pas cyclique » : comparer deg μ et la dimension 6, puis expliquer pourquoi aucun vecteur ne peut engendrer tout l'espace.",
        ],
        "levels": {
            "sup": "Travailler familles libres, rang et suites récurrentes ; la base de Krylov est simplement une famille de vecteurs obtenus par applications successives.",
            "spe": "Relier sous-espace stable, polynôme annulateur du vecteur et récurrence ; approfondir le critère μ=χ lorsque le polynôme minimal est étudié.",
            "beyond": "Comprendre les endomorphismes cycliques, leur commutant et les méthodes de Krylov ; distinguer toute la dynamique de ce qu'une observation scalaire révèle.",
        },
        "lesson_numbers": [10, 14, 16],
        "expected": "Savoir prouver qu'un vecteur est cyclique ou ne l'est pas et en déduire une récurrence exacte pour une observation de ses itérés.",
    },
    "frobenius": {
        "purpose": (
            "Décrire une matrice à l'aide de blocs compagnons sans devoir trouver toutes ses valeurs propres. "
            "La comparaison de deux exemples 6×6 montre pourquoi le produit des facteurs invariants donne χ, alors que le dernier facteur donne une autre information, μ."
        ),
        "techniques": [
            "Lire la relation polynomiale dans la dernière colonne d'un compagnon.",
            "Vérifier divisibilité des facteurs, produit χ et dernier facteur μ.",
            "Certifier un changement de base par AP=PF.",
        ],
        "first_steps": [
            "Choisir « Deux facteurs, μ de degré 4 », puis « Même χ, μ de degré 6 » : comparer les facteurs et le nombre de blocs compagnons.",
            "Avant de faire varier « Changement de base entier », prévoir les invariants conservés ; constater que A change, mais pas les facteurs ni la forme de Frobenius.",
            "Choisir « Sans racine réelle » : lire les compagnons de X²+1 et expliquer comment une description rationnelle reste possible sans base propre réelle.",
        ],
        "levels": {
            "sup": "Entrer par produits de polynômes, division euclidienne et changements de base ; la classification de Frobenius est une extension guidée.",
            "spe": "Mobiliser sous-espaces stables et matrices compagnons ; en MP/MPI, comparer χ et μ pour comprendre les limites d'une classification par χ seul.",
            "beyond": "Relier facteurs invariants, forme de Smith de XI−A et modules sur K[X] pour classifier les similitudes sans hypothèse de scindement.",
        },
        "lesson_numbers": [10, 14, 15],
        "expected": "Savoir lire les invariants d'une décomposition donnée et expliquer pourquoi elle fonctionne même lorsque χ n'est pas scindé.",
    },
    "cayley": {
        "purpose": (
            "Calculer une grande puissance de matrice avec un nombre borné de coefficients. "
            "On reconstruit aussi χ à partir des traces et on cherche comment une division euclidienne remplace une longue succession de produits matriciels."
        ),
        "techniques": [
            "Évaluer un polynôme annulateur en une matrice.",
            "Réduire Xᵏ modulo μ puis évaluer le reste en A.",
            "Reconstruire χ par les identités de Newton et contrôler les divisions nécessaires.",
        ],
        "first_steps": [
            "Choisir « Calcul exact en 6D » : comparer χ et μ, puis vérifier le certificat χ(A)=0 dans les résultats exacts.",
            "Prévoir une borne du degré du reste, puis choisir « Une puissance élevée » : lire le reste de X³⁰ modulo μ et justifier deg reste<deg μ.",
            "Choisir « Le TP Vandermonde » : suivre les traces jusqu'au déterminant et vérifier que Newton et Faddeev donnent les mêmes coefficients.",
        ],
        "levels": {
            "sup": "Réutiliser division euclidienne, traces et calcul matriciel ; on peut d'abord vérifier l'annulation fournie sans supposer connu le théorème de Cayley–Hamilton.",
            "spe": "Travailler Cayley–Hamilton et les polynômes annulateurs lorsqu'ils sont au programme ; en MP/MPI, optimiser la réduction avec le polynôme minimal.",
            "beyond": "Étudier l'algèbre K[A], les identités de Newton et Faddeev–LeVerrier ; examiner pourquoi certaines divisions échouent en caractéristique positive.",
        },
        "lesson_numbers": [10, 11, 16],
        "expected": "Savoir remplacer Aᵏ par un polynôme de petit degré en A et justifier cette réduction par une identité annulatrice.",
    },
    "pfaffien": {
        "purpose": (
            "Explorer pourquoi le déterminant d'une matrice antisymétrique de taille paire est un carré. "
            "Les appariements montrent les produits et les signes du pfaffien ; les changements de coordonnées révèlent ce que ce carré oublie sur l'orientation."
        ),
        "techniques": [
            "Former des appariements et calculer le signe d'une permutation.",
            "Comparer det A à Pf(A)² sur une matrice antisymétrique.",
            "Contrôler une congruence PᵀAP et son effet sur rang et orientation.",
        ],
        "first_steps": [
            "Choisir « 15 appariements d'une matrice dense » : déplacer le sélecteur des appariements et retrouver un terme à partir de son signe et de ses trois paires.",
            "Prévoir l'effet de det P=−1, puis choisir « Changement d'orientation » : comparer Pf(PᵀAP) à det(P)Pf(A) et expliquer pourquoi le carré perd ce signe.",
            "Choisir « La transformation perd un rang » : constater det P=0 et vérifier que la loi de congruence reste vraie, même si P n'est plus un changement de base inversible.",
        ],
        "levels": {
            "sup": "Entrer par antisymétrie, déterminants, permutations et dénombrement des paires ; le pfaffien est un objet supplémentaire dont la construction est explicitée.",
            "spe": "Réutiliser transposée, rang et changement de coordonnées pour contrôler les identités ; relier antisymétrie et formes bilinéaires lorsque celles-ci sont étudiées.",
            "beyond": "Étudier formes alternées et produit extérieur ; utiliser la loi du pfaffien pour démontrer det M=1 pour une matrice symplectique.",
        },
        "lesson_numbers": [5, 19, 23],
        "expected": "Savoir calculer un terme signé du pfaffien et distinguer l'effet d'une congruence sur le pfaffien de son effet sur le déterminant.",
    },
    "projecteurs": {
        "purpose": (
            "Décomposer un vecteur en composantes que l'on peut calculer séparément. "
            "En confrontant projecteurs polynomiaux et projection oblique, on distingue une somme directe algébrique d'une projection qui minimise effectivement une distance."
        ),
        "techniques": [
            "Déduire E=Im P⊕Ker P de P²=P.",
            "Construire des projecteurs polynomiaux par Bézout entre facteurs premiers entre eux.",
            "Employer l'orthogonalité et Pythagore pour certifier une distance minimale.",
        ],
        "first_steps": [
            "Choisir « Somme directe spectrale » : déplacer le vecteur avec x, y, z et vérifier que ses deux composantes s'ajoutent au vecteur initial.",
            "Prévoir ce qui subsiste quand les valeurs propres se confondent, puis choisir « Valeurs propres confondues » : expliquer la composante unique et le projecteur I.",
            "Choisir « Projection oblique », puis faire varier l'inclinaison : comparer le point projeté au pied perpendiculaire et retrouver le cas orthogonal à inclinaison nulle.",
        ],
        "levels": {
            "sup": "Comprendre image, noyau et somme directe d'un projecteur ; comparer une décomposition de vecteur à une recherche de point le plus proche.",
            "spe": "Mobiliser projections orthogonales ; en MP/MPI, appliquer Bézout et la décomposition des noyaux, proposés ici en approfondissement pour les autres filières.",
            "beyond": "Étudier les projecteurs primaires lorsque le polynôme minimal a des facteurs multiples et comprendre les précautions nécessaires à la fusion des valeurs propres.",
        },
        "lesson_numbers": [7, 9, 10],
        "expected": "Savoir certifier une décomposition par projecteurs et dire quelles hypothèses supplémentaires assurent une distance euclidienne minimale.",
    },
    "quadratiques": {
        "purpose": (
            "Relier le signe d'une expression quadratique à des courbes de niveau et à un relief. "
            "En changeant la base, on cherche les propriétés conservées par congruence et on comprend pourquoi cette opération diffère d'une similitude."
        ),
        "techniques": [
            "Compléter les carrés ou orthogonaliser pour écrire une somme de carrés signés.",
            "Distinguer PᵀSP de P⁻¹SP et vérifier le changement de coordonnées.",
            "Lire signe, rang et directions nulles pour interpréter une Hessienne.",
        ],
        "first_steps": [
            "Choisir « Ellipses », puis « Hyperboles » : comparer le relief z=q(x,y), les niveaux q=1 et l'inertie affichée.",
            "Prévoir si un cisaillement peut transformer une selle en vallée, puis varier « Cisaillement de la base » : contrôler l'inertie et la congruence exacte.",
            "Choisir « Isotropie » : trouver un vecteur non nul où q s'annule et expliquer pourquoi une diagonale nulle n'impose pas une matrice nulle.",
        ],
        "levels": {
            "sup": "Partir de complétions de carrés, coniques et changements de coordonnées ; interpréter le signe d'une expression à deux variables sans classification abstraite.",
            "spe": "Réutiliser matrices symétriques et théorème spectral selon la filière ; relier la positivité d'une Hessienne à l'étude d'un extremum local.",
            "beyond": "Étudier la loi d'inertie et la classification par congruence ; traiter les vecteurs isotropes sans diviser par une valeur quadratique nulle.",
        },
        "lesson_numbers": [5, 8, 20],
        "expected": "Savoir reconnaître une forme positive, indéfinie ou dégénérée et justifier ce diagnostic par une réduction exacte, au-delà de la figure.",
    },
    "jacobi": {
        "purpose": (
            "Comprendre comment trois doubles commutateurs non nuls peuvent avoir une somme exactement nulle. "
            "Le laboratoire conduit d'une compensation observable à une preuve par douze produits, puis montre pourquoi l'application ad_X:T↦[X,T] respecte les crochets."
        ),
        "techniques": [
            "Développer des doubles commutateurs en respectant l'ordre des facteurs.",
            "Regrouper les mots matriciels identiques avec des signes opposés.",
            "Identifier une application linéaire et comparer deux compositions d'opérateurs.",
        ],
        "first_steps": [
            "Choisir « Jacobi non trivial dans so3 » : constater que les trois contributions sont non nulles et que leur triangle vectoriel se ferme.",
            "Utiliser « Comparer un mot de Jacobi » : retrouver les deux occurrences opposées de ce mot, puis répéter le raisonnement pour les six mots.",
            "Prévoir l'effet de X=0, puis choisir « Un cas devenu trivial » et « Compensation dans sp4 » : distinguer annulation triviale et identité générale.",
        ],
        "levels": {
            "sup": "Travailler associativité, distributivité et ordre des produits ; l'identité de Jacobi est accessible par développement, même avant l'étude des algèbres de Lie.",
            "spe": "Mobiliser endomorphismes, linéarité et commutation pour vérifier [ad_X,ad_Y]=ad_[X,Y] ; distinguer action sur toutes les matrices et restriction à une sous-algèbre.",
            "beyond": "Comprendre Jacobi comme axiome d'une algèbre de Lie et construire sa représentation adjointe ; relier le noyau de cette dernière au centre.",
        },
        "lesson_numbers": [17, 18, 21],
        "expected": "Savoir prouver Jacobi par compensation des produits et en déduire la propriété de représentation de ad.",
    },
    "representations": {
        "purpose": (
            "Faire agir trois opérateurs différentiels sur des polynômes homogènes et traduire cette action en matrices de dimension m+1. "
            "Le diagramme des poids relie dérivation, espaces propres et sous-espaces stables ; les mouvements distinguent noyau d'un opérateur et noyau d'une représentation."
        ),
        "techniques": [
            "Dériver un monôme et écrire ses coordonnées dans la base xᵐ⁻ᵏyᵏ.",
            "Calculer les commutateurs E, F, H sur chaque vecteur de base.",
            "Utiliser les valeurs propres de H et les flèches E/F pour étudier la stabilité.",
        ],
        "first_steps": [
            "Choisir « Forme quartique et 5 poids » : dériver x⁴, x³y et x²y² à la main, puis retrouver poids et coefficients des flèches.",
            "Choisir « Action nilpotente » : suivre le déplacement des coefficients sous E et expliquer pourquoi exp(tE) est ici une somme finie.",
            "Prévoir l'effet de −I sur un monôme, puis comparer les degrés 3 et 4 avec « Noyau de groupe selon la parité » ; distinguer ce noyau de Ker E et du noyau d'algèbre Ker ρ.",
        ],
        "levels": {
            "sup": "Entrer par dérivation des monômes, bases et dimension d'un espace de polynômes ; les représentations de Lie sont ici un prolongement explicité.",
            "spe": "Réutiliser diagonalisation, nilpotence et sous-espaces stables pour expliquer le diagramme ; contrôler les relations d'opérateurs sur une base plutôt que numériquement.",
            "beyond": "Étudier les représentations irréductibles de sl₂, leurs poids et le passage au groupe SL₂ ; distinguer noyaux de groupe et d'algèbre.",
        },
        "lesson_numbers": [4, 18, 22],
        "expected": "Savoir reconstruire E, F et H depuis leurs actions sur les monômes et expliquer les informations différentes portées par leurs noyaux.",
    },
    "symplectique": {
        "purpose": (
            "Faire évoluer des oscillateurs couplés et comparer deux façons de calculer leurs trajectoires. "
            "Le TP met à l'épreuve une idée tentante : conserver le volume suffirait-il à préserver les relations entre positions et impulsions, ou faut-il l'identité plus forte MᵀJM=J ?"
        ),
        "techniques": [
            "Passer d'une énergie quadratique à l'équation u′=JKu.",
            "Vérifier les identités de conservation par produits et transposées.",
            "Comparer schémas d'Euler et de Cayley à pas et état initial identiques.",
        ],
        "first_steps": [
            "Choisir « Deux modes couplés » et animer les oscillateurs : relier qᵢ et pᵢ aux portraits de phase et à l'énergie totale.",
            "Choisir « Euler dérive » : comparer les deux courbes d'énergie au même pas h et distinguer conservation exacte avant arrondis et erreur d'intégration.",
            "Prévoir si det M=1 suffit, puis choisir « Volume ne suffit pas » : constater le défaut MᵀJM−J non nul et expliquer le contre-exemple.",
        ],
        "levels": {
            "sup": "Entrer par oscillateur harmonique, énergie, dérivation et produits matriciels ; les coordonnées de phase et Sp₄/Sp₆ sont introduites comme extensions.",
            "spe": "Relier systèmes différentiels linéaires, formes quadratiques positives et comparaison numérique de schémas ; contrôler un invariant par sa dérivée ou une identité matricielle.",
            "beyond": "Étudier mécanique hamiltonienne, groupe symplectique et intégrateurs géométriques ; distinguer conservation de volume, de forme symplectique et d'une énergie donnée.",
        },
        "lesson_numbers": [17, 19, 23],
        "expected": "Savoir réfuter l'implication « déterminant 1 ⇒ symplectique » et expliquer les invariants effectivement préservés par le schéma de Cayley proposé.",
    },
    "markov": {
        "purpose": (
            "Suivre la redistribution d'une loi de probabilité entre six états et prédire sa limite. "
            "On distingue la stationnarité, où chaque état reçoit autant qu'il émet, de l'équilibre détaillé, qui annule chacun des courants entre deux états."
        ),
        "techniques": [
            "Traduire les probabilités conditionnelles en une matrice de transition par colonnes.",
            "Résoudre (M−I)π=0 avec des coordonnées positives ou nulles de somme 1.",
            "Comparer les flux πⱼMᵢⱼ et πᵢMⱼᵢ plutôt que la seule symétrie de M.",
        ],
        "first_steps": [
            "Choisir « Circulation non réversible » et animer : comparer pₖ, sa limite et les flux stationnaires pour constater une circulation malgré une loi fixe.",
            "Choisir « Équilibre détaillé » : retrouver l'annulation de chaque courant net et vérifier que cela n'exige pas une matrice M symétrique.",
            "Prévoir la limite sans pont ni mélange uniforme, puis choisir « Deux classes fermées » : varier la loi initiale et expliquer les masses conservées et dim Ker(M−I)=2.",
        ],
        "levels": {
            "sup": "Réutiliser probabilités conditionnelles, formule des probabilités totales et produits matriciels ; vérifier à chaque étape positivité et somme des probabilités égale à 1.",
            "spe": "Mobiliser vecteurs propres, puissances de matrices et convergence ; relier pluralité des lois stationnaires et dimension de l'espace propre associé à 1.",
            "beyond": "Étudier irréductibilité, apériodicité, réversibilité et vitesse de mélange ; séparer équilibre des bilans locaux et absence de circulation sur les cycles.",
        },
        "lesson_numbers": [6, 8, 24],
        "expected": "Savoir calculer et vérifier une loi stationnaire, puis dire si elle est unique et si elle permet des courants persistants.",
    },
    "reseaux": {
        "purpose": (
            "Relier un pont fragile entre deux groupes de sommets au ralentissement d'une diffusion. "
            "Le Laplacien transforme une question de réseau en calcul de noyau, de forme quadratique, de valeur propre et de déterminant : chaque outil raconte une propriété différente."
        ),
        "techniques": [
            "Construire L=BWBᵀ et reconnaître les fonctions constantes dans son noyau.",
            "Développer xᵀLx comme somme pondérée de carrés de différences.",
            "Relier les modes propres à la décroissance d'une solution de x′=−Lx.",
        ],
        "first_steps": [
            "Choisir « Un pont fragile » : lire le signe du vecteur de Fiedler, puis animer la diffusion du contraste +1/−1 entre les deux groupes.",
            "Prévoir l'effet d'une coupure sur la limite, puis choisir « Le pont est coupé » : relier moyennes séparément conservées, dim Ker L=2 et λ₂=0.",
            "Choisir « Diffusion d'une impulsion » et faire varier le poids du pont : comparer vitesse d'homogénéisation, λ₂ et cofacteur de Kirchhoff, somme pondérée des arbres couvrants.",
        ],
        "levels": {
            "sup": "Entrer par matrices, noyau, rang et sommes de carrés ; le graphe décrit les liaisons, tandis que le Laplacien agit sur leurs valeurs.",
            "spe": "Réutiliser théorème spectral et équations différentielles linéaires selon la filière ; comprendre pourquoi les petites valeurs propres donnent des modes lents.",
            "beyond": "Étudier connectivité algébrique, vecteur de Fiedler et théorème de Kirchhoff ; distinguer nombre d'arbres et somme de leurs poids lorsque les conductances varient.",
        },
        "lesson_numbers": [8, 20, 25],
        "expected": "Savoir expliquer l'effet d'une coupure ou d'un pont faible en reliant figure, dimension du noyau, énergie et mode propre lent.",
    },
}
