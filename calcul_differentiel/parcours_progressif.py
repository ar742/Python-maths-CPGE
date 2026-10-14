"""Parcours progressif : socle CPGE et prolongements facultatifs."""

PROGRESSION = {'title': 'Calcul différentiel & Transformations : un parcours sup / spé',
 'intro': 'Partir d’une approximation à une variable, puis construire la différentielle comme application '
          'linéaire. Relier ensuite jacobiennes, matrices, extrema et contraintes avant de choisir les '
          'prolongements.',
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les '
             'approfondissements et les branches au-delà du programme se choisissent ensuite, '
             'indépendamment.',
 'scope': 'Repères MPSI / MP : dérivées partielles en sup ; différentielle, règle de la chaîne, gradients, '
          'Hessienne, Taylor–Young d’ordre 2 et optimisation sous contrainte en MP. Les groupes de Lie, les '
          'intégrales multiples, Green–Riemann et Fubini sont des prolongements. Le parcours distingue ces '
          'théories des calculs d’intégration et de matrice qui leur servent de point d’entrée.',
 'prerequisites': ['Sup : dérivation, développements limités, primitives, trigonométrie et matrices.',
                   'Fin de sup : fonctions de deux variables et dérivées partielles.',
                   'Spé : espaces euclidiens, théorème spectral, topologie en dimension finie et calcul '
                   'différentiel.'],
 'method': ['Lire les objets, les notations et les hypothèses du TP.',
            'Prévoir un résultat sur papier, puis ouvrir l’expérience.',
            'Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.',
            'Conclure par une courte preuve et distinguer résultat exact, approximation et observation.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : deux séances pour préparer la différentielle',
             'intro': 'Les expériences sont abordées par des courbes et des calculs accessibles à une '
                      'variable.',
             'sessions': [{'id': 'sup_direction',
                           'title': '1. Dériver le long d’une droite',
                           'status': 'socle',
                           'level': 'Sup · dérivées et approximation affine',
                           'labs': ['taylor'],
                           'objective': 'Comprendre une dérivée directionnelle à partir d’une fonction d’une '
                                        'variable.',
                           'task': 'Noter a le point de base, u une direction unitaire et t le déplacement. '
                                   'Pour la fonction lisse du TP, étudier φ(t)=f(a+tu) : calculer φ′(0), '
                                   'comparer la tangente puis réduire l’intervalle h.',
                           'success': 'Distinguer la pente dans une direction, les dérivées partielles et '
                                      'l’erreur d’approximation.',
                           'limits': 'À ce palier, rester sur la courbe φ. La notion complète de '
                                     'différentielle et la classification par Hessienne arrivent en spé.'},
                          {'id': 'sup_coordonnees',
                           'title': '2. Des coordonnées transforment des vecteurs',
                           'status': 'socle',
                           'level': 'Sup · trigonométrie et dérivées partielles',
                           'labs': ['jacobiennes'],
                           'objective': 'Identifier les directions radiale, angulaire et verticale.',
                           'task': 'Partir des coordonnées polaires x=ρcosθ,y=ρsinθ, puis cylindriques en '
                                   'ajoutant z. Noter ρ le rayon et θ l’angle en radians dans les dérivées ; '
                                   'calculer les deux colonnes des dérivées partielles et leur déterminant.',
                           'success': 'Retrouver le facteur ρ et expliquer la perte d’une direction lorsque '
                                      'ρ=0 ; ne pas confondre les degrés des curseurs avec les radians du '
                                      'calcul.',
                           'limits': 'Le calcul de la matrice est accessible en sup ; son interprétation '
                                     'comme matrice d’une différentielle sera formalisée en spé.'}]},
            {'id': 'spe',
             'title': 'Spé : quatre séances incontournables',
             'intro': 'La linéarité, les hypothèses et la preuve d’extremum précèdent l’observation des '
                      'graphiques.',
             'sessions': [{'id': 'spe_jacobienne',
                           'title': '3. Une application linéaire tangente',
                           'status': 'socle',
                           'level': 'Spé · différentielle et règle de la chaîne',
                           'labs': ['jacobiennes', 'taylor'],
                           'objective': 'Passer d’un calcul de dérivées à une approximation valable pour '
                                        'tous les petits déplacements.',
                           'task': 'Noter F la transformation de coordonnées et J sa jacobienne au point de '
                                   'base. Comparer F(a+v)−F(a) à Jv lorsque le déplacement v diminue ; en '
                                   'sphérique, expliquer la singularité au pôle. Vérifier la dérivée d’une '
                                   'composée.',
                           'success': 'Écrire F(a+v)=F(a)+Jv+o(‖v‖) et distinguer dérivées directionnelles '
                                      'et différentiabilité dans le mode pathologique.',
                           'limits': 'Une image qui se rapproche soutient le calcul du reste ; elle ne '
                                     'démontre pas à elle seule la différentiabilité.'},
                          {'id': 'spe_matrices',
                           'title': '4. Différencier le déterminant et l’inverse',
                           'status': 'socle',
                           'level': 'Spé · applications matricielles',
                           'labs': ['matrices'],
                           'objective': 'Utiliser multilinéarité et dérivation d’un produit matriciel.',
                           'task': 'Noter A la matrice de base et H la direction fixée du TP. Partir de A=I, '
                                   'identité, puis dériver det(A+tH) à t=0. Pour l’inverse, dériver '
                                   '(A+tH)(A+tH)⁻¹=I et garder l’ordre des facteurs.',
                           'success': 'Retrouver Ddet(I)[H]=Tr H et Dinv(A)[H]=−A⁻¹HA⁻¹ ; expliquer pourquoi '
                                      'la seconde formule exige l’inversibilité.',
                           'limits': 'Les formules se démontrent comme exercices. Le conditionnement et les '
                                     'seuils numériques sont des diagnostics, pas de nouvelles hypothèses '
                                     'algébriques.'},
                          {'id': 'spe_extrema',
                           'title': '5. Point critique, Hessienne et conclusion',
                           'status': 'socle',
                           'level': 'Spé · Taylor–Young et théorème spectral',
                           'labs': ['taylor', 'optimisation'],
                           'objective': 'Distinguer conditions nécessaires, conditions suffisantes et cas '
                                        'dégénéré.',
                           'task': 'Noter ∇f le gradient et Hf la matrice hessienne. Dans le TP Taylor, '
                                   'comparer un minimum, une selle et un point dégénéré ; examiner plusieurs '
                                   'coupes. Pour la quadratique positive du TP optimisation, calculer son '
                                   'gradient puis compléter le carré.',
                           'success': 'Justifier un minimum strict par une Hessienne définie positive ; '
                                      'expliquer pourquoi une Hessienne seulement positive ne conclut pas '
                                      'toujours.',
                           'limits': 'Hessienne et Taylor–Young d’ordre 2 sont au programme MP. La théorie '
                                     'abstraite de la différentielle seconde et les algorithmes de Newton '
                                     'restent hors du socle.'},
                          {'id': 'spe_rayleigh',
                           'title': '6. Un extremum sous une contrainte',
                           'status': 'socle',
                           'level': 'Spé · quotient de Rayleigh',
                           'labs': ['optimisation'],
                           'objective': 'Relier optimisation sur la sphère et valeurs propres d’une matrice '
                                        'symétrique.',
                           'task': 'Choisir le mode Rayleigh et noter A la matrice symétrique, u un vecteur '
                                   'unitaire, R(u)=uᵀAu. Vérifier la régularité de la contrainte uᵀu=1 ; '
                                   'retrouver la condition Au=λu et comparer les valeurs aux axes propres.',
                           'success': 'Justifier l’existence sur la sphère compacte et les extrema égaux aux '
                                      'valeurs propres extrêmes.',
                           'limits': 'Le calcul sous une contrainte régulière est au programme MP. Les '
                                     'méthodes d’itération pour trouver des vecteurs propres sont '
                                     'facultatives.'}]},
            {'id': 'complements',
             'title': 'Approfondissements : deux ponts vers les applications',
             'intro': 'Les résultats nécessaires sont donnés ; priorité aux contrôles de calcul.',
             'sessions': [{'id': 'complement_descente',
                           'title': '7. Du spectre au choix d’un pas',
                           'status': 'approfondissement',
                           'level': 'Spé · suites géométriques et algorithme',
                           'labs': ['optimisation'],
                           'objective': 'Analyser une itération à partir de ses composantes propres.',
                           'task': 'Noter α le pas de descente, λmax la plus grande valeur propre et x* le '
                                   'minimum de la quadratique. Écrire la récurrence de l’erreur ; comparer '
                                   'αλmax<2 puis αλmax>2. Comparer avec Newton sur cette quadratique.',
                           'success': 'Déduire la condition 0<α<2/λmax et expliquer pourquoi Newton atteint '
                                      'ici le minimum en un pas, à l’arrondi près.',
                           'limits': 'L’étude de suites géométriques et la diagonalisation sont le socle. '
                                     'Les méthodes de descente et de Newton sont des applications numériques '
                                     'accompagnées.'},
                          {'id': 'complement_tangentes',
                           'title': '8. Une contrainte de groupe donne une contrainte linéaire',
                           'status': 'approfondissement',
                           'level': 'Spé · dériver une identité matricielle',
                           'labs': ['lie'],
                           'objective': 'Exercer la dérivation d’un produit et du déterminant avant '
                                        'd’introduire une théorie de Lie.',
                           'task': 'Noter M(t) une courbe matricielle avec M(0)=I et X=M′(0). Dériver '
                                   'M(t)ᵀM(t)=I puis det M(t)=1 ; retrouver Xᵀ=−X dans le premier cas et Tr '
                                   'X=0 dans le second.',
                           'success': 'Expliquer le passage d’une équation non linéaire sur M à une équation '
                                      'linéaire sur sa vitesse X.',
                           'limits': 'La dérivation utilise les outils MP. Les groupes et algèbres de Lie, '
                                     'leurs représentations et leur classification ne sont pas au '
                                     'programme.'}]},
            {'id': 'beyond',
             'title': 'Au-delà : trois branches à choisir',
             'intro': 'Les intégrales multiples et la théorie de Lie sont annoncées comme nouvelles, avec '
                      'leurs définitions.',
             'sessions': [{'id': 'beyond_integration',
                           'title': 'A. Aires transformées, Green et Fubini',
                           'status': 'prolongement',
                           'level': 'Au-delà · intégrales multiples',
                           'labs': ['elliptique', 'green_fubini'],
                           'objective': 'Comprendre les facteurs de mesure et les hypothèses de permutation '
                                        'des intégrales.',
                           'task': 'Sur le quart d’ellipse, retrouver |det J|=abr, où a,b sont les demi-axes '
                                   'et r le rayon réduit. Dans Green, inverser l’orientation du contour. '
                                   'Dans Fubini, comparer des coupures symétriques et dissymétriques près de '
                                   'l’origine singulière.',
                           'success': 'Expliquer séparément facteur d’aire, signe d’orientation et défaut '
                                      'd’intégrabilité absolue.',
                           'limits': 'Le changement de variables multiple, Green–Riemann et Fubini sont des '
                                     'prolongements hors du programme MPSI / MP ; primitives et limites '
                                     'restent les outils de calcul.'},
                          {'id': 'beyond_gaussienne',
                           'title': 'B. Une gaussienne en plusieurs dimensions',
                           'status': 'prolongement',
                           'level': 'Au-delà · intégrales et probabilités multivariées',
                           'labs': ['gaussienne'],
                           'objective': 'Compléter le carré et interpréter une matrice symétrique positive.',
                           'task': 'Noter A la matrice définie positive, B le terme linéaire et μ=A⁻¹B le '
                                   'centre. Retrouver la complétion du carré dans exp(−xᵀAx/2+Bᵀx), puis '
                                   'comparer les ellipses pour plusieurs valeurs de B.',
                           'success': 'Séparer le déplacement du centre, réglé par B, et l’étalement, réglé '
                                      'par A⁻¹ ; comparer quadrature et masse omise.',
                           'limits': 'La diagonalisation et la complétion du carré réutilisent le programme. '
                                     'Intégrales multiples, covariance multivariée et dérivation de ces '
                                     'intégrales sont des prolongements fournis.'},
                          {'id': 'beyond_lie',
                           'title': 'C. Exponentielle et crochet de Lie',
                           'status': 'prolongement',
                           'level': 'Au-delà · groupes et algèbres de Lie',
                           'labs': ['lie'],
                           'objective': 'Relier des matrices tangentes à des transformations finies et à '
                                        'leur défaut de commutation.',
                           'task': 'Noter X,Y les matrices tangentes et [X,Y]=XY−YX leur crochet. Comparer '
                                   'SO(2) et SO(3), puis observer exp(tX) et le quotient du commutateur par '
                                   'le carré d’un petit pas.',
                           'success': 'Relier antisymétrie à conservation des longueurs et trace nulle à '
                                      'conservation du déterminant ; distinguer identité exacte et '
                                      'développement limité.',
                           'limits': 'L’exponentielle matricielle fait partie des outils MP. La structure de '
                                     'Lie et l’interprétation du crochet sont des prolongements ; les très '
                                     'petits pas sont sensibles à l’arrondi.'}]}],
 'sources': [{'label': 'Programme officiel de mathématiques MPSI',
              'url': 'https://prepas.org/ups.php?document=69'},
             {'label': 'Programme officiel de mathématiques MP',
              'url': 'https://prepas.org/ups.php?document=85'}],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/calcul_differentiel/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'taylor', 'title': 'La fonction, sa tangente et sa courbure', 'href': '/?tp=taylor'},
 {'id': 'jacobiennes', 'title': 'Une jacobienne transforme les directions', 'href': '/?tp=jacobiennes'},
 {'id': 'matrices', 'title': 'Différencier le déterminant et l’inverse', 'href': '/?tp=matrices'},
 {'id': 'optimisation', 'title': 'Du gradient aux valeurs propres', 'href': '/?tp=optimisation'},
 {'id': 'elliptique', 'title': 'L’intégrale change avec la mesure', 'href': '/?tp=elliptique'},
 {'id': 'lie', 'title': 'Le tangent engendre une transformation', 'href': '/?tp=lie'},
 {'id': 'gaussienne', 'title': 'Une intégrale révèle moyenne et covariance', 'href': '/?tp=gaussienne'},
 {'id': 'green_fubini', 'title': 'Intégrer : orientation et hypothèses', 'href': '/?tp=green_fubini'}]
