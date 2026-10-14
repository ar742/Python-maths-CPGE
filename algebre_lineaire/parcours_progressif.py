"""Progression proposée : socle, approfondissements et prolongements."""

PROGRESSION = {'title': 'Algèbre & Réductions : un parcours progressif sup / spé',
 'intro': 'Commencer par les systèmes et les changements de base. En spé, utiliser le spectre et les '
          'polynômes d’une matrice pour expliquer sa dynamique. Les structures de Lie et les grandes '
          'classifications viennent ensuite, au choix.',
 'scope': 'Repères MPSI et MP. « Incontournable » désigne les techniques de la séance, pas tous les '
          'résultats du TP. La classification de Jordan, la décomposition de Dunford, la forme de '
          'Frobenius, les algèbres de Lie et le pfaffien sont des prolongements, même si leurs premiers '
          'calculs utilisent des outils de CPGE.',
 'prerequisites': ['Sup : systèmes linéaires, matrices, applications linéaires, image, noyau, rang et '
                   'déterminant.',
                   'Sup : bases, sommes directes, produit scalaire, projection orthogonale et division '
                   'polynomiale.',
                   'Spé : valeurs propres, diagonalisation, polynômes annulateurs et théorème spectral; '
                   'polynôme minimal et décomposition des noyaux en MP.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances de calcul et de géométrie',
             'intro': 'Distinguer une transformation des vecteurs, un changement de base et une opération '
                      'sur les équations.',
             'sessions': [{'id': 'sup_geometrie',
                           'title': '1. Composer, inverser et lire un déterminant',
                           'status': 'socle',
                           'level': 'Sup · calcul matriciel',
                           'labs': ['geometrie'],
                           'objective': 'Comprendre l’ordre d’une composition et relier déterminant, '
                                        'volume et perte de dimension.',
                           'task': 'Choisir deux transformations du cube. Comparer leurs deux ordres, '
                                   'suivre un sommet et prévoir le signe du déterminant. Tester ensuite '
                                   'une transformation singulière.',
                           'success': 'Écrire le produit dans le bon ordre; distinguer matrice inversible '
                                      'et matrice de rang insuffisant.',
                           'limits': 'L’action d’un groupe sert d’interprétation. Aucune théorie des '
                                     'groupes de Lie n’est nécessaire.'},
                          {'id': 'sup_gauss',
                           'title': '2. Résoudre et certifier un système',
                           'status': 'socle',
                           'level': 'Sup · pivot, noyau et image',
                           'labs': ['gauss'],
                           'objective': 'Décrire toutes les solutions, ou prouver qu’il n’en existe '
                                        'aucune.',
                           'task': 'Comparer un système compatible à un système incompatible. Refaire les '
                                   'premières opérations de Gauss et lire les colonnes pivots. Vérifier '
                                   'une solution puis les vecteurs du noyau.',
                           'success': 'Écrire l’ensemble des solutions comme une solution particulière '
                                      'plus le noyau; contrôler le théorème du rang.',
                           'limits': 'Le calcul exact est prioritaire. Conditionnement et erreurs '
                                     'd’arrondi sont des compléments numériques.'},
                          {'id': 'sup_projecteurs',
                           'title': '3. Décomposer sans confondre les projections',
                           'status': 'socle',
                           'level': 'Sup · sommes directes et espaces euclidiens',
                           'labs': ['projecteurs'],
                           'objective': 'Caractériser un projecteur par son image et son noyau; '
                                        'reconnaître quand il est orthogonal.',
                           'task': 'Choisir le mode projection oblique. Décomposer le vecteur, vérifier '
                                   'que projeter deux fois donne le même résultat, puis comparer la '
                                   'direction de projection à une perpendiculaire.',
                           'success': 'Justifier la somme directe et l’identité de projecteur; ne pas '
                                      'attribuer à une projection oblique une propriété de distance '
                                      'minimale.',
                           'limits': 'La construction de projecteurs par Bézout sera reprise en spé. Les '
                                     'projecteurs primaires restent facultatifs.'},
                          {'id': 'sup_inverse',
                           'title': '4. Inverser dans le bon ensemble',
                           'status': 'socle',
                           'level': 'Sup · déterminant et inverse',
                           'labs': ['anneaux'],
                           'objective': 'Maîtriser l’inversibilité sur un corps avant d’explorer les '
                                        'coefficients entiers ou modulaires.',
                           'task': 'Commencer dans les rationnels avec une matrice non singulière. '
                                   'Vérifier le produit avec son inverse. Puis comparer aux entiers : '
                                   'expliquer pourquoi un inverse rationnel peut sortir de l’ensemble '
                                   'autorisé.',
                           'success': 'Employer det non nul sur un corps; identifier précisément '
                                      'l’obstacle quand les coefficients de l’inverse ne sont plus '
                                      'autorisés.',
                           'limits': 'Le théorème sur GLₙ d’un anneau commutatif est fourni en '
                                     'approfondissement; il ne remplace pas le critère étudié sur un '
                                     'corps.'}]},
            {'id': 'spe',
             'title': 'Spé : trois séances pour choisir un invariant',
             'intro': 'Les calculs deviennent des preuves de réduction et des méthodes pour éviter les '
                      'multiplications inutiles.',
             'sessions': [{'id': 'spe_spectre',
                           'title': '5. Valeurs propres et diagonalisation',
                           'status': 'socle',
                           'level': 'Spé · réduction',
                           'labs': ['spectre'],
                           'objective': 'Décider une diagonalisation en examinant les espaces propres, pas '
                                        'seulement la liste des valeurs propres.',
                           'task': 'Comparer deux familles proposées. Calculer un noyau associé à une '
                                   'valeur propre et compter les dimensions des espaces propres. Expliquer '
                                   'un échec de diagonalisation.',
                           'success': 'Construire une base de vecteurs propres quand elle existe; '
                                      'distinguer multiplicité d’une racine et dimension de l’espace '
                                      'propre.',
                           'limits': 'S’arrêter au critère de diagonalisation et aux noyaux. Les chaînes '
                                     'et la classification de Jordan sont réservées aux prolongements.'},
                          {'id': 'spe_cayley',
                           'title': '6. Réduire une grande puissance',
                           'status': 'socle',
                           'level': 'Spé MP · polynômes annulateurs',
                           'labs': ['cayley'],
                           'objective': 'Calculer une puissance matricielle par division euclidienne et '
                                        'Cayley–Hamilton.',
                           'task': 'Choisir la matrice dense et une puissance élevée. Utiliser le polynôme '
                                   'caractéristique fourni pour réduire la puissance, puis vérifier '
                                   'l’égalité matricielle. Comparer une réduction par le polynôme minimal '
                                   'quand il est disponible.',
                           'success': 'Expliquer pourquoi le reste polynomial donne la même matrice et '
                                      'pourquoi changer de base conserve le polynôme caractéristique.',
                           'limits': 'Les identités générales entre traces et coefficients et l’algorithme '
                                     'de Faddeev–LeVerrier sont des compléments fournis.'},
                          {'id': 'spe_quadratiques',
                           'title': '7. Lire le signe d’une forme quadratique',
                           'status': 'socle',
                           'level': 'Spé · matrices symétriques et théorème spectral',
                           'labs': ['quadratiques'],
                           'objective': 'Relier les valeurs propres d’une matrice symétrique au signe de '
                                        'sa forme quadratique.',
                           'task': 'Comparer les cas positif, indéfini et dégénéré. Suivre les lignes de '
                                   'niveau et vérifier les signes sur des vecteurs. Écrire le changement '
                                   'orthonormé qui explique la figure.',
                           'success': 'Distinguer congruence pour une forme et similitude pour un '
                                      'endomorphisme; expliquer un vecteur non nul de valeur quadratique '
                                      'nulle.',
                           'limits': 'La loi d’inertie générale est un prolongement. Le socle est le '
                                     'théorème spectral et l’usage des valeurs propres pour la '
                                     'positivité.'}]},
            {'id': 'approfondissements',
             'title': 'Deux approfondissements avec les outils de CPGE',
             'intro': 'Les objets nouveaux sont définis dans le TP; les preuves utilisent rang, noyau, '
                      'positivité et réduction.',
             'sessions': [{'id': 'approfondir_cyclique',
                           'title': 'A1. Une dynamique engendrée par un vecteur',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · application guidée',
                           'labs': ['cyclique', 'projecteurs'],
                           'objective': 'Construire une famille par applications successives et '
                                        'reconnaître le sous-espace qu’elle engendre.',
                           'task': 'Comparer un vecteur propre à un vecteur témoin cyclique. Contrôler le '
                                   'rang de la famille obtenue et la récurrence affichée. En MP, reprendre '
                                   'les projecteurs construits par Bézout.',
                           'success': 'Relier une dépendance linéaire à une récurrence; justifier la '
                                      'décomposition des noyaux par des polynômes premiers entre eux.',
                           'limits': 'Le nom Krylov, le critère général de cyclicité et le calcul du '
                                     'commutant ne sont pas des exigences supplémentaires.'},
                          {'id': 'approfondir_reseaux',
                           'title': 'A2. Matrices, probabilités et diffusion',
                           'status': 'approfondissement',
                           'level': 'Spé · applications de la réduction',
                           'labs': ['reseaux', 'markov'],
                           'objective': 'Interpréter noyau, positivité et modes lents dans deux modèles '
                                        'concrets.',
                           'task': 'Couper le pont du réseau puis le rétablir. Comparer les noyaux du '
                                   'Laplacien et l’évolution du signal. Dans la chaîne de Markov, vérifier '
                                   'conservation de la somme et loi stationnaire.',
                           'success': 'Établir le bilan conservé et relier les changements de noyau ou '
                                      'd’espace propre à la séparation des groupes.',
                           'limits': 'Les théorèmes généraux de Markov, Fiedler, Kirchhoff et de vitesse '
                                     'de mélange sont des prolongements; une expérience finie ne les '
                                     'démontre pas.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Choisir une branche après le socle. Vérifier les certificats du TP avant de '
                      'chercher une théorie générale.',
             'sessions': [{'id': 'prolonger_reductions',
                           'title': 'P1. Jordan, Dunford et Frobenius',
                           'status': 'prolongement',
                           'level': 'Au-delà · classification et calcul matriciel',
                           'labs': ['spectre', 'dunford', 'frobenius'],
                           'objective': 'Comprendre ce que le seul polynôme caractéristique ne distingue '
                                        'pas.',
                           'task': 'Comparer les accroissements des noyaux, puis vérifier la décomposition '
                                   'proposée par Dunford et la commutation de ses deux parties. Comparer '
                                   'enfin deux formes de Frobenius de même polynôme caractéristique.',
                           'success': 'Expliquer le rôle de chaque invariant et vérifier les changements '
                                      'de base ou polynômes fournis.',
                           'limits': 'Les théorèmes généraux de ces trois classifications ne sont pas '
                                     'exigibles en MPSI / MP.'},
                          {'id': 'prolonger_lie',
                           'title': 'P2. Du commutateur aux représentations de Lie',
                           'status': 'prolongement',
                           'level': 'Au-delà · structures et actions',
                           'labs': ['lie', 'jacobi', 'representations', 'anneaux'],
                           'objective': 'Passer d’un défaut de commutation à une action d’opérateurs sur '
                                        'des polynômes.',
                           'task': 'Développer les trois termes de Jacobi, puis vérifier les relations sur '
                                   'une base de monômes. Comparer deux petites rotations et leur '
                                   'commutateur. Revenir aux anneaux pour le rôle des éléments '
                                   'inversibles.',
                           'success': 'Séparer une identité accessible par développement de la définition '
                                      'et de la théorie d’une algèbre de Lie.',
                           'limits': 'L’exponentielle matricielle est un outil du programme MP. Les '
                                     'représentations irréductibles et le passage global de l’algèbre au '
                                     'groupe sont des prolongements accompagnés.'},
                          {'id': 'prolonger_symplectique',
                           'title': 'P3. Pfaffien et mécanique symplectique',
                           'status': 'prolongement',
                           'level': 'Au-delà · formes alternées et invariants',
                           'labs': ['pfaffien', 'symplectique'],
                           'objective': 'Distinguer conservation du volume et conservation de la forme '
                                        'symplectique.',
                           'task': 'Contrôler le carré du pfaffien sur une matrice antisymétrique de '
                                   'taille paire. Comparer ensuite une transformation symplectique à celle '
                                   'de déterminant 1 proposée comme contre-exemple.',
                           'success': 'Expliquer pourquoi un déterminant égal à 1 ne suffit pas; '
                                      'interpréter séparément énergie, volume et forme conservée.',
                           'limits': 'Pfaffien, produit extérieur et intégrateurs hamiltoniens sont hors '
                                     'programme; leurs définitions et certificats restent fournis.'}]}],
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Si deux TP sont '
             'associés, le second sert de comparaison ou de travail personnel. Les branches facultatives '
             'peuvent occuper plusieurs séances.',
 'method': ['Lire le but, les objets et les hypothèses avant de modifier un réglage.',
            'Prévoir un résultat sur papier, puis comparer à la figure ou au certificat calculé.',
            'Faire varier un seul paramètre et justifier ce qui change.',
            'Conclure par une preuve courte : résultat, hypothèses et portée de l’expérience.'],
 'sources': [{'label': 'Programme de mathématiques MPSI / MP2I',
              'url': 'https://prepas.org/ups.php?document=69'},
             {'label': 'Programme de mathématiques MP', 'url': 'https://prepas.org/ups.php?document=85'}],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/algebre_lineaire/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'anneaux', 'title': 'Le déterminant doit être une unité', 'href': '/?tp=anneaux'},
 {'id': 'geometrie',
  'title': 'Agir dans l’espace : volume, orientation, composition',
  'href': '/?tp=geometrie'},
 {'id': 'lie', 'title': 'Du groupe à son algèbre de Lie', 'href': '/?tp=lie'},
 {'id': 'gauss', 'title': 'Gauss : rang, noyau et systèmes', 'href': '/?tp=gauss'},
 {'id': 'spectre', 'title': 'Spectre, Jordan et choix du corps', 'href': '/?tp=spectre'},
 {'id': 'dunford', 'title': 'Séparer la partie semi-simple et la nilpotente', 'href': '/?tp=dunford'},
 {'id': 'cyclique', 'title': 'Un vecteur peut engendrer toute la dynamique', 'href': '/?tp=cyclique'},
 {'id': 'frobenius', 'title': 'Les facteurs invariants organisent la matrice', 'href': '/?tp=frobenius'},
 {'id': 'cayley', 'title': 'De la trace aux puissances d’une matrice', 'href': '/?tp=cayley'},
 {'id': 'pfaffien', 'title': 'Un déterminant est le carré d’un pfaffien', 'href': '/?tp=pfaffien'},
 {'id': 'projecteurs', 'title': 'Décomposer un espace avec des projecteurs', 'href': '/?tp=projecteurs'},
 {'id': 'quadratiques', 'title': 'Changer de base pour une forme quadratique', 'href': '/?tp=quadratiques'},
 {'id': 'jacobi', 'title': 'Jacobi : trois contributions qui se compensent', 'href': '/?tp=jacobi'},
 {'id': 'representations', 'title': 'sl2 agit sur les polynômes homogènes', 'href': '/?tp=representations'},
 {'id': 'symplectique',
  'title': 'Conserver la forme symplectique, pas seulement le volume',
  'href': '/?tp=symplectique'},
 {'id': 'markov', 'title': 'Six états : circuler, mélanger, converger', 'href': '/?tp=markov'},
 {'id': 'reseaux', 'title': "Le pont d'un réseau se lit dans son Laplacien", 'href': '/?tp=reseaux'}]
