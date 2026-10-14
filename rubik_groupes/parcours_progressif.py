"""Parcours progressif : socle CPGE et prolongements facultatifs."""

PROGRESSION = {'title': 'Rubik & Groupes : un parcours sup / spé',
 'intro': 'Partir de gestes dont on peut vérifier l’effet, puis passer aux permutations, aux sous-groupes et '
          'aux invariants. La résolution sert de terrain d’expérimentation, sans devenir un objectif de '
          'vitesse.',
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les '
             'approfondissements et les branches au-delà du programme se choisissent ensuite, '
             'indépendamment.',
 'scope': 'Repères MPSI / MP : le socle est la composition, les permutations, la signature et, en MP, les '
          'groupes cycliques et sous-groupes engendrés. Le groupe particulier du cube est un exemple fourni. '
          'Commutateurs, actions, graphe de Cayley et résolution par phases restent des compléments. Ouvrir '
          'une séance ne joue aucun mouvement et conserve le cube sauvegardé.',
 'prerequisites': ['Sup : applications, bijections, composition et inverse ; calculs de divisibilité et '
                   'ppcm.',
                   'Fin de sup : permutations, cycles et signature.',
                   'Spé : groupes, sous-groupes engendrés, ordre d’un élément et groupe cyclique.'],
 'method': ['Lire les objets, les notations et les hypothèses du TP.',
            'Prévoir un résultat sur papier, puis ouvrir l’expérience.',
            'Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.',
            'Conclure par une courte preuve et distinguer résultat exact, approximation et observation.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : trois séances pour lire et composer',
             'intro': 'Écrire les calculs avant de jouer les mouvements. La convention est chronologique : '
                      'RU signifie R puis U.',
             'sessions': [{'id': 'sup_transformations',
                           'title': '1. Distinguer un mot de son effet',
                           'status': 'socle',
                           'level': 'Sup · applications et groupe',
                           'labs': ['groupe', 'analyse'],
                           'objective': 'Vérifier stabilité, associativité, neutre et inverse sur un exemple '
                                        'concret.',
                           'task': 'Noter R le quart de tour de la face droite et e l’identité. Analyser R, '
                                   'RR, R2 et RRRR ; comparer leurs effets et expliquer pourquoi des mots '
                                   'différents peuvent représenter la même transformation.',
                           'success': 'Retrouver R²=R2 et R⁴=e, puis relier l’associativité à la composition '
                                      'des applications.',
                           'limits': 'Le nombre total de configurations est fourni ; sa démonstration ne '
                                     'fait pas partie de cette première séance.'},
                          {'id': 'sup_inverses',
                           'title': '2. Annuler une suite de mouvements',
                           'status': 'socle',
                           'level': 'Sup · inverse d’une composée',
                           'labs': ['inverse', 'analyse'],
                           'objective': 'Calculer un inverse en changeant l’ordre des facteurs.',
                           'task': 'Pour le mot R U F2, où U tourne la face du haut et F la face avant, '
                                   'écrire l’inverse sur papier. Analyser ensuite le mot suivi de cet '
                                   'inverse ; jouer la vérification seulement après le calcul.',
                           'success': "Obtenir F2 U' R' et justifier l’identité par associativité, sans "
                                      'supposer la commutation des tours.',
                           'limits': 'Réduire des facteurs voisins raccourcit parfois un mot ; cela ne '
                                     'prouve pas que le résultat a une longueur minimale.'},
                          {'id': 'sup_permutations',
                           'title': '3. Décomposer en cycles et tester la commutation',
                           'status': 'socle',
                           'level': 'Fin de sup · groupe symétrique',
                           'labs': ['permutations', 'noncommutatif', 'analyse', 'compare'],
                           'objective': 'Lire une permutation et comparer deux composées sur les mêmes '
                                        'objets.',
                           'task': 'Comparer A=R et B=U, puis A=R et B=L, où L est le tour de la face '
                                   'gauche. Décrire un cycle affiché et calculer la signature à partir des '
                                   'longueurs des cycles disjoints.',
                           'success': 'Identifier au moins une facette qui distingue RU de UR ; expliquer la '
                                      'commutation de faces opposées par leurs supports disjoints.',
                           'limits': 'Les cycles des positions des pièces omettent leur orientation. Le '
                                     'calcul de l’ordre complet se fait sur les facettes.'}]},
            {'id': 'spe',
             'title': 'Spé : trois séances pour construire des preuves',
             'intro': 'Passer du calcul d’un exemple à une propriété du sous-groupe engendré.',
             'sessions': [{'id': 'spe_ordre',
                           'title': '4. Ordre et sous-groupe cyclique',
                           'status': 'socle',
                           'level': 'Spé · ordre et génération',
                           'labs': ['permutations', 'analyse'],
                           'objective': 'Relier les cycles d’une permutation à l’ordre de l’élément et à ses '
                                        'puissances.',
                           'task': 'Noter g l’effet du mot RU. À partir des cycles des facettes, calculer '
                                   'leur ppcm ; retrouver l’ordre 105 et déterminer combien d’éléments '
                                   'contient le sous-groupe engendré par g.',
                           'success': 'Justifier gᵏ=e si et seulement si 105 divise k, sans jouer 105 '
                                      'répétitions.',
                           'limits': 'Le groupe cyclique engendré par un élément est au programme MP ; sa '
                                     'présence dans le cube est l’exemple du TP.'},
                          {'id': 'spe_invariants',
                           'title': '5. Prouver une invariance sur les générateurs',
                           'status': 'socle',
                           'level': 'Spé · signature et congruences',
                           'labs': ['invariants'],
                           'objective': 'Démontrer une condition nécessaire sur les transformations '
                                        'accessibles.',
                           'task': 'Noter σc la permutation des coins et σe celle des arêtes. Vérifier sur '
                                   'un quart de tour que leurs signatures sont égales, puis expliquer '
                                   'pourquoi cette égalité se conserve par produit et inverse. Examiner les '
                                   'exemples impossibles sans les importer comme état courant.',
                           'success': 'Exclure l’échange de deux coins seuls ; distinguer comptage des '
                                      'couleurs, signature et sommes d’orientations.',
                           'limits': 'Les orientations du cube sont des données expliquées. La suffisance de '
                                     'l’ensemble des conditions d’accessibilité est un théorème particulier '
                                     'fourni, hors socle.'},
                          {'id': 'spe_resolution',
                           'title': '6. De la génération à une solution vérifiée',
                           'status': 'socle',
                           'level': 'Spé · mots, génération et inverse',
                           'labs': ['inverse', 'resolution'],
                           'objective': 'Distinguer existence d’un mot inverse, construction d’une solution '
                                        'et optimalité.',
                           'task': 'Créer volontairement un mélange court après avoir noté l’état de départ. '
                                   'Comparer l’inverse de l’historique à une recherche bornée et vérifier '
                                   'les solutions. Un échec de recherche à profondeur fixée doit être '
                                   'interprété avec sa limite.',
                           'success': 'Expliquer pourquoi un historique connu suffit pour construire une '
                                      'solution, tandis qu’un cube importé demande une recherche.',
                           'limits': 'Le socle est le raisonnement algébrique sur les mots. La recherche '
                                     'bidirectionnelle est un complément algorithmique, sans obligation de '
                                     'connaître un solveur complet.'}]},
            {'id': 'complements',
             'title': 'Approfondissements : deux constructions guidées',
             'intro': 'Les définitions nouvelles sont fournies ; les calculs réinvestissent inverse et '
                      'composition.',
             'sessions': [{'id': 'complement_commutateur',
                           'title': '7. Localiser un défaut de commutation',
                           'status': 'approfondissement',
                           'level': 'Sup / Spé · calcul dans un groupe',
                           'labs': ['commutateurs', 'compare'],
                           'objective': 'Utiliser le commutateur [A,B]=ABA⁻¹B⁻¹ et suivre les pièces '
                                        'affectées.',
                           'task': 'Comparer les commutateurs obtenus avec les faces R,U puis R,L. Prévoir '
                                   'lequel vaut e, puis analyser les cycles et orientations de l’autre.',
                           'success': 'Démontrer [A,B]=e si et seulement si AB=BA dans la convention de '
                                      'l’atelier.',
                           'limits': 'Le calcul est accessible avec les axiomes ; les sous-groupes dérivés '
                                     'et la théorie des commutateurs ne sont pas demandés.'},
                          {'id': 'complement_conjugaison',
                           'title': '8. Transporter une manœuvre',
                           'status': 'approfondissement',
                           'level': 'Spé · conjugaison guidée',
                           'labs': ['conjugaison', 'compare'],
                           'objective': 'Conserver le type des cycles en changeant les pièces sur lesquelles '
                                        'une manœuvre agit.',
                           'task': 'Noter A une manœuvre analysée et S un mot de préparation. Comparer A et '
                                   'SAS⁻¹ ; établir par récurrence l’identité (SAS⁻¹)ᵏ=SAᵏS⁻¹.',
                           'success': 'En déduire l’égalité des ordres et expliquer le déplacement des '
                                      'supports observés.',
                           'limits': 'La conjugaison est ici un exercice algébrique fourni ; aucune '
                                     'classification des classes de conjugaison n’est exigée.'}]},
            {'id': 'beyond',
             'title': 'Au-delà : structure et algorithmes de résolution',
             'intro': 'Choisir ces deux branches après les séances prioritaires ; les théories propres au '
                      'cube sont facultatives.',
             'sessions': [{'id': 'beyond_actions',
                           'title': 'A. Actions, stabilisateurs et comptage',
                           'status': 'prolongement',
                           'level': 'Au-delà · groupe agissant sur un ensemble',
                           'labs': ['structure', 'invariants'],
                           'objective': 'Comprendre une résolution progressive à partir des objets déjà '
                                        'fixés.',
                           'task': 'Lire la définition du stabilisateur d’une pièce, puis d’un ensemble de '
                                   'pièces. Relier les contraintes de permutations et d’orientations au '
                                   'comptage des états possibles.',
                           'success': 'Distinguer groupe de transformations, ensemble sur lequel il agit et '
                                      'sous-groupe qui fixe un objet.',
                           'limits': 'Actions, formule orbite-stabilisateur et structure complète du groupe '
                                     'du cube ne sont pas présentées comme des obligations MPSI / MP.'},
                          {'id': 'beyond_phases',
                           'title': 'B. Graphes de Cayley et résolution par phases',
                           'status': 'prolongement',
                           'level': 'Au-delà · algorithmique et sous-groupes',
                           'labs': ['cayley', 'phases', 'resolution'],
                           'objective': 'Comparer la recherche d’un plus court chemin et une stratégie par '
                                        'sous-groupes.',
                           'task': 'Lire la convention HTM : chaque quart de tour, tour inverse ou demi-tour '
                                   'compte un mouvement. Comparer recherche courte et méthode en deux phases '
                                   '; expliquer pourquoi une solution vérifiée peut ne pas être optimale.',
                           'success': 'Relier sommets, mouvements autorisés, profondeur et sous-groupe '
                                      'intermédiaire.',
                           'limits': 'La méthode de Kociemba nécessite un module optionnel. Son algorithme, '
                                     'les tables de recherche et les bornes globales de distance sont des '
                                     'prolongements.'}]}],
 'sources': [{'label': 'Programme officiel de mathématiques MPSI',
              'url': 'https://prepas.org/ups.php?document=69'},
             {'label': 'Programme officiel de mathématiques MP',
              'url': 'https://prepas.org/ups.php?document=85'}],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/rubik_groupes/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'analyse', 'title': 'Lire une transformation', 'href': '/?tp=analyse'},
 {'id': 'compare', 'title': 'Comparer et construire', 'href': '/?tp=compare'},
 {'id': 'resolution', 'title': 'Résolution', 'href': '/?tp=resolution'},
 {'id': 'groupe', 'title': 'Un cube, un groupe', 'href': '/?tp=groupe'},
 {'id': 'inverse', 'title': 'Mots et inverses', 'href': '/?tp=inverse'},
 {'id': 'permutations', 'title': 'Cycles et ordre', 'href': '/?tp=permutations'},
 {'id': 'noncommutatif', 'title': 'L’ordre des gestes', 'href': '/?tp=noncommutatif'},
 {'id': 'commutateurs', 'title': 'Les commutateurs', 'href': '/?tp=commutateurs'},
 {'id': 'conjugaison', 'title': 'Préparer et conjuguer', 'href': '/?tp=conjugaison'},
 {'id': 'invariants', 'title': 'Tester une configuration : invariants', 'href': '/?tp=invariants'},
 {'id': 'structure', 'title': 'Actions et stabilisateurs', 'href': '/?tp=structure'},
 {'id': 'cayley', 'title': 'Chercher une solution', 'href': '/?tp=cayley'},
 {'id': 'phases', 'title': 'Vers une résolution générale', 'href': '/?tp=phases'}]
