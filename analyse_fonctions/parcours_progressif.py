"""Progression proposée : socle, approfondissements et prolongements."""

PROGRESSION = {'title': 'Fonctions & Équations : un parcours progressif sup / spé',
 'intro': 'En sup, identifier une fonction et résoudre une équation différentielle avec ses données '
          'initiales. En spé, vérifier les hypothèses des intégrales à paramètre et relier les systèmes '
          'linéaires à leurs modes. Les fonctions spéciales fournissent des applications; les ordres '
          'fractionnaires restent des prolongements.',
 'scope': 'Repères MPSI et MP. Le socle concerne substitutions, continuité, EDO linéaires et théorèmes '
          'd’intégration ou de dérivation à paramètre. Gamma, bêta, zêta et Hermite sont des exemples '
          'définis dans les TP, pas des fonctions à connaître par cœur. Faà di Bruno général, calcul '
          'fractionnaire, fonctions de Green et théorie générale de Riccati ou de Cauchy–Lipschitz sont '
          'des compléments.',
 'prerequisites': ['Sup : logarithme, exponentielle, trigonométrie, continuité, dérivation et intégration '
                   'sur un segment.',
                   'Sup : équations différentielles linéaires d’ordres 1 et 2, données initiales et '
                   'développements limités.',
                   'Spé : intégrales impropres, domination, séries de fonctions, algèbre linéaire et '
                   'réduction pour les systèmes.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances pour calculer et contrôler',
             'intro': 'Toujours préciser le domaine et les données initiales avant de proposer une '
                      'formule.',
             'sessions': [{'id': 'sup_substitutions',
                           'title': '1. Une équation fonctionnelle : choisir les substitutions',
                           'status': 'socle',
                           'level': 'Sup · équations et symétries',
                           'labs': ['identification_symetrie', 'cauchy_additive'],
                           'objective': 'Exploiter les valeurs particulières et la continuité sans deviner '
                                        'trop tôt une forme de solution.',
                           'task': 'Comparer l’équation en un point, son opposé et aux valeurs '
                                   'particulières autorisées. Dans l’équation additive, obtenir les '
                                   'valeurs entières puis rationnelles et utiliser la densité.',
                           'success': 'Justifier le passage des rationnels aux réels par l’hypothèse de '
                                      'continuité.',
                           'limits': 'Ces équations sont des exercices. Les solutions additives non '
                                     'régulières sont réservées au prolongement.'},
                          {'id': 'sup_logarithme',
                           'title': '2. Transformer une équation sans changer le domaine',
                           'status': 'socle',
                           'level': 'Sup · logarithme, exponentielle et EDO',
                           'labs': ['cauchy_multiplicative', 'dalembert'],
                           'objective': 'Choisir un changement de variable licite et conserver les '
                                        'conditions initiales.',
                           'task': 'Dans le premier TP, préciser quand un logarithme est autorisé puis '
                                   'ramener le produit à une somme. Dans d’Alembert, vérifier parité et '
                                   'valeurs initiales avant la réduction différentielle proposée.',
                           'success': 'Retrouver les familles sous les hypothèses annoncées et vérifier la '
                                      'formule dans l’équation de départ.',
                           'limits': 'Les classifications fonctionnelles générales et les preuves sans '
                                     'régularité ne sont pas exigibles.'},
                          {'id': 'sup_edo1',
                           'title': '3. Facteur intégrant et donnée initiale',
                           'status': 'socle',
                           'level': 'Sup · EDO linéaires d’ordre 1',
                           'labs': ['facteur_integrant', 'euler_rk4'],
                           'objective': 'Résoudre une équation linéaire puis contrôler une approximation '
                                        'numérique.',
                           'task': 'Construire le facteur intégrant en dérivant le produit. Pour le TP du '
                                   'recueil, retrouver la solution exacte et comparer deux pas d’Euler à '
                                   'données initiales identiques.',
                           'success': 'Ajuster la constante avec la valeur initiale et distinguer solution '
                                      'exacte, approximation et erreur.',
                           'limits': 'La preuve de l’ordre de Runge–Kutta et l’estimation générale '
                                     'd’erreur sont des compléments; la comparaison du pas est une '
                                     'expérience guidée.'},
                          {'id': 'sup_edo2',
                           'title': '4. Deux données pour un oscillateur',
                           'status': 'socle',
                           'level': 'Sup · EDO linéaires d’ordre 2',
                           'labs': ['oscillateur_resonance', 'variation_constantes'],
                           'objective': 'Construire une solution homogène et particulière sans perdre une '
                                        'condition initiale.',
                           'task': 'Comparer les régimes libres, puis un forçage sinusoïdal. Calculer les '
                                   'constantes initiales. Dans la variation des constantes, vérifier la '
                                   'solution particulière proposée par substitution.',
                           'success': 'Donner la solution complète et contrôler l’équation, la valeur '
                                      'initiale et la dérivée initiale.',
                           'limits': 'En sup, vérifier une solution particulière proposée. La méthode de '
                                     'variation des constantes est à travailler en spé, séance 8. '
                                     'Convolution et transformée de Laplace restent des applications '
                                     'facultatives.'}]},
            {'id': 'spe',
             'title': 'Spé : quatre séances sur les hypothèses et les modes',
             'intro': 'Trois séances appliquent séparément les théorèmes de continuité, de dérivation et '
                      'de dérivations successives à paramètre.',
             'sessions': [{'id': 'spe_continuite',
                           'title': '5. Continuité d’une intégrale à paramètre',
                           'status': 'socle',
                           'level': 'Spé · domination et continuité',
                           'labs': ['continuite_gauss', 'continuite_defaut'],
                           'objective': 'Chercher une domination locale intégrable et comprendre pourquoi '
                                        'la limite ponctuelle ne suffit pas.',
                           'task': 'Écrire les hypothèses sur l’intégrande et le paramètre. Comparer '
                                   'l’intégrale gaussienne au contre-exemple concentré et expliquer la '
                                   'masse qui échappe à la limite.',
                           'success': 'Nommer le théorème applicable et produire un majorant indépendant '
                                      'du paramètre sur un voisinage.',
                           'limits': 'Fourier de la gaussienne et convergence de mesures sont des '
                                     'compléments; les exemples n’imposent aucune théorie nouvelle.'},
                          {'id': 'spe_leibniz',
                           'title': '6. Dériver pour calculer une intégrale',
                           'status': 'socle',
                           'level': 'Spé · dérivation à paramètre',
                           'labs': ['leibniz_frullani', 'leibniz_arctan'],
                           'objective': 'Remplacer une intégrale difficile par une dérivée plus simple '
                                        'puis fixer la constante.',
                           'task': 'Pour Frullani, étudier d’abord les deux extrémités et la compensation. '
                                   'Construire un majorant de la dérivée sur un compact de paramètres, '
                                   'intégrer la relation puis utiliser une valeur de référence.',
                           'success': 'Justifier la dérivation et la constante; ne pas séparer deux '
                                      'intégrales divergentes dont la différence converge.',
                           'limits': 'La limite d’Abel au bord de l’intégrale oscillante est un '
                                     'approfondissement, pas une conséquence automatique du théorème '
                                     'local.'},
                          {'id': 'spe_successives',
                           'title': '7. Plusieurs dérivations sous l’intégrale',
                           'status': 'socle',
                           'level': 'Spé · régularité et Cauchy–Schwarz',
                           'labs': ['derivees_gamma', 'derivees_laplace'],
                           'objective': 'Contrôler chaque dérivée par un majorant intégrable sur le '
                                        'domaine annoncé.',
                           'task': 'Choisir un compact de paramètres strictement dans le domaine. Écrire '
                                   'les intégrandes dérivés puis vérifier leur domination. Utiliser '
                                   'Cauchy–Schwarz pour la convexité du logarithme de gamma.',
                           'success': 'Distinguer régularité à tout ordre sur le domaine et comportement '
                                      'au bord; justifier le signe ou la convexité demandée.',
                           'limits': 'Digamma, trigamma et monotonie complète sont des noms '
                                     'complémentaires. Laplace sert ici d’exemple d’intégrale à '
                                     'paramètre.'},
                          {'id': 'spe_systemes',
                           'title': '8. Variation des constantes et modes d’un système',
                           'status': 'socle',
                           'level': 'Spé MP · systèmes différentiels et réduction',
                           'labs': ['variation_constantes', 'lineaire_systeme'],
                           'objective': 'Construire une solution particulière d’ordre 2, puis relier un '
                                        'système linéaire à ses modes et à ses bilans.',
                           'task': 'Dans la variation des constantes, calculer le wronskien de la base '
                                   'homogène et les dérivées des deux coefficients variables. Puis, dans '
                                   'le système à trois composantes, écrire et sommer les bilans; comparer '
                                   'les modes rapides et lents.',
                           'success': 'Ajuster les deux données initiales d’ordre 2; dans le système, '
                                      'vérifier la conservation et expliquer le rôle des valeurs propres.',
                           'limits': 'La variation des constantes d’ordre 2 et les systèmes linéaires '
                                     'relèvent du programme MP. La théorie générale des réseaux de '
                                     'diffusion et de la positivité des générateurs est un '
                                     'prolongement.'}]},
            {'id': 'approfondissements',
             'title': 'Trois approfondissements avec les techniques de CPGE',
             'intro': 'Des fonctions définies sur place permettent de réinvestir intégration par parties, '
                      'séries et dérivation.',
             'sessions': [{'id': 'approfondir_speciales',
                           'title': 'A1. Gamma, bêta et zêta comme exercices d’intégration',
                           'status': 'approfondissement',
                           'level': 'Spé · intégrales, séries et restes',
                           'labs': ['gamma_euler', 'beta_geometrie', 'zeta_series', 'zeta_integrale'],
                           'objective': 'Déterminer les domaines avant d’utiliser une récurrence ou une '
                                        'interversion.',
                           'task': 'Retrouver la factorielle par intégration par parties. Pour zêta, '
                                   'encadrer le reste de la série. Comparer ensuite les formules '
                                   'intégrales de bêta et zêta aux valeurs calculées.',
                           'success': 'Accompagner chaque approximation d’une borne et justifier chaque '
                                      'changement de variable ou interversion.',
                           'limits': 'Les fonctions sont définies dans les TP. Leur prolongement '
                                     'analytique et les théorèmes généraux de caractérisation sont '
                                     'au-delà.'},
                          {'id': 'approfondir_domaines',
                           'title': 'A2. Une formule doit rester sur le bon intervalle',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · EDO et domaines',
                           'labs': ['euler_cauchy', 'riccati'],
                           'objective': 'Repérer les divisions interdites et les singularités d’une '
                                        'substitution.',
                           'task': 'Dans chaque équation, relever les points exclus et travailler sur un '
                                   'intervalle autorisé. Vérifier les formules fournies par dérivation, '
                                   'puis tester ce qui se passe près du bord.',
                           'success': 'Contrôler l’équation initiale après changement de variable et '
                                      'expliquer pourquoi une formule locale ne définit pas '
                                      'automatiquement une solution globale.',
                           'limits': 'Frobenius, classification des points singuliers et théorie générale '
                                     'de Riccati sont des prolongements.'},
                          {'id': 'approfondir_hermite',
                           'title': 'A3. Dériver une gaussienne et reconnaître une récurrence',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · dérivées, polynômes et intégration par parties',
                           'labs': ['hermite_gauss', 'faa_di_bruno'],
                           'objective': 'Faire apparaître des polynômes par dérivations successives et '
                                        'vérifier leurs propriétés.',
                           'task': 'Calculer les trois premières dérivées de la gaussienne, retrouver les '
                                   'signes et la parité. Vérifier une relation de récurrence et un cas '
                                   'd’orthogonalité par intégrations par parties.',
                           'success': 'Expliquer la convention choisie pour Hermite et vérifier les '
                                      'coefficients sans se contenter du calcul automatique.',
                           'limits': 'La formule générale de Faà di Bruno et les polynômes de Bell ne sont '
                                     'pas exigibles; commencer par les dérivées composées d’ordres 2 et '
                                     '3.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Pour un TIPE ou une lecture accompagnée, choisir une branche après les séances '
                      'prioritaires.',
             'sessions': [{'id': 'prolonger_nonlineaire',
                           'title': 'P1. Unicité, explosion et solutions maximales',
                           'status': 'prolongement',
                           'level': 'Au-delà · EDO non linéaires',
                           'labs': ['cauchy_lipschitz', 'explosion_logistique', 'riccati'],
                           'objective': 'Comprendre pourquoi une donnée initiale ne suffit pas toujours et '
                                        'pourquoi une solution peut avoir une durée de vie finie.',
                           'task': 'Vérifier directement deux solutions du contre-exemple d’unicité. '
                                   'Comparer ensuite le modèle qui explose et celui qui sature; calculer '
                                   'les intervalles maximaux à partir des formules.',
                           'success': 'Séparer existence, unicité, stabilité et existence globale.',
                           'limits': 'Le théorème général de Cauchy–Lipschitz et les résultats globaux sur '
                                     'les EDO non linéaires ne sont pas des exigences supplémentaires de '
                                     'MPSI / MP.'},
                          {'id': 'prolonger_bords',
                           'title': 'P2. Deux points, une fonction de Green',
                           'status': 'prolongement',
                           'level': 'Au-delà · problèmes aux limites',
                           'labs': ['green_bords', 'variation_constantes', 'euler_cauchy'],
                           'objective': 'Comparer données au même point et conditions aux deux extrémités '
                                        'd’un intervalle.',
                           'task': 'Modifier le paramètre du problème aux bords et distinguer solution '
                                   'unique, aucune solution et infinité de solutions. Vérifier la '
                                   'condition intégrale quand l’homogène devient dégénérée.',
                           'success': 'Expliquer pourquoi l’unicité d’un problème initial ne garantit pas '
                                      'celle d’un problème aux limites.',
                           'limits': 'Fonctions de Green, alternative de Fredholm et théorie spectrale des '
                                     'opérateurs sont introduites comme prolongements.'},
                          {'id': 'prolonger_fractionnaire',
                           'title': 'P3. Mémoire et dérivées d’ordre non entier',
                           'status': 'prolongement',
                           'level': 'Au-delà · calcul fractionnaire et combinatoire',
                           'labs': ['integrale_fractionnaire', 'derivees_fractionnaires', 'faa_di_bruno'],
                           'objective': 'Distinguer une dérivée locale d’un opérateur qui dépend du passé '
                                        'et comparer deux conventions.',
                           'task': 'Commencer par les ordres entiers, puis faire varier l’ordre réel de '
                                   'l’intégrale. Comparer la dérivée d’une constante dans les deux '
                                   'définitions. En complément, vérifier les premiers termes de Faà di '
                                   'Bruno.',
                           'success': 'Nommer le noyau, les conditions initiales et la convention avant de '
                                      'comparer les résultats.',
                           'limits': 'Riemann–Liouville, Caputo, polynômes de Bell et formule générale de '
                                     'Faà di Bruno sont hors programme et ne deviennent pas des résultats '
                                     'à mémoriser.'}]}],
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
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/analyse_fonctions/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'continuite_gauss',
  'title': 'Théorème 1 : continuité d’une transformée gaussienne',
  'href': '/?tp=continuite_gauss'},
 {'id': 'continuite_defaut',
  'title': 'Théorème 1 : une masse qui se concentre interdit le passage à la limite',
  'href': '/?tp=continuite_defaut'},
 {'id': 'leibniz_frullani',
  'title': 'Théorème 2 : Frullani, un logarithme retrouvé par dérivation',
  'href': '/?tp=leibniz_frullani'},
 {'id': 'leibniz_arctan',
  'title': 'Théorème 2 : transformer une intégrale oscillante en arctangente',
  'href': '/?tp=leibniz_arctan'},
 {'id': 'derivees_gamma',
  'title': 'Théorème 3 : dérivées de Γ, moments logarithmiques et convexité',
  'href': '/?tp=derivees_gamma'},
 {'id': 'derivees_laplace',
  'title': 'Théorème 3 : dérivées de Laplace et monotonie complète',
  'href': '/?tp=derivees_laplace'},
 {'id': 'euler_rk4', 'title': 'Euler et RK4 : mesurer un ordre de convergence', 'href': '/?tp=euler_rk4'},
 {'id': 'facteur_integrant',
  'title': 'Facteur intégrant : transformer une EDO en intégrale',
  'href': '/?tp=facteur_integrant'},
 {'id': 'cauchy_lipschitz',
  'title': 'Une condition initiale ne suffit pas toujours',
  'href': '/?tp=cauchy_lipschitz'},
 {'id': 'explosion_logistique',
  'title': 'Solution maximale : explosion ou saturation',
  'href': '/?tp=explosion_logistique'},
 {'id': 'oscillateur_resonance',
  'title': 'Oscillateur : transitoire, résonance et travail',
  'href': '/?tp=oscillateur_resonance'},
 {'id': 'variation_constantes',
  'title': 'Variation des constantes : un noyau de Green initial',
  'href': '/?tp=variation_constantes'},
 {'id': 'euler_cauchy',
  'title': 'Euler–Cauchy : singularités et série entière',
  'href': '/?tp=euler_cauchy'},
 {'id': 'riccati',
  'title': 'EDO homogène et Riccati : deux changements de fonction',
  'href': '/?tp=riccati'},
 {'id': 'lineaire_systeme',
  'title': 'Trois réservoirs : conservation, modes et exponentielle',
  'href': '/?tp=lineaire_systeme'},
 {'id': 'green_bords', 'title': 'Deux bords : existence, unicité et résonance', 'href': '/?tp=green_bords'},
 {'id': 'cauchy_additive',
  'title': 'Cauchy : une équation à deux variables détermine une droite',
  'href': '/?tp=cauchy_additive'},
 {'id': 'cauchy_multiplicative',
  'title': 'Produit, logarithme, puissance : changer de variable pour résoudre',
  'href': '/?tp=cauchy_multiplicative'},
 {'id': 'dalembert',
  'title': 'D’Alembert : pourquoi apparaissent cosinus et cosinus hyperbolique ?',
  'href': '/?tp=dalembert'},
 {'id': 'identification_symetrie',
  'title': 'Substituer −x : identifier une fonction sans la deviner',
  'href': '/?tp=identification_symetrie'},
 {'id': 'gamma_euler',
  'title': 'Gamma : prolonger la factorielle et contrôler une intégrale impropre',
  'href': '/?tp=gamma_euler'},
 {'id': 'beta_geometrie',
  'title': 'Bêta : un changement de variables relie deux intégrales',
  'href': '/?tp=beta_geometrie'},
 {'id': 'zeta_series',
  'title': 'Zêta : une somme approchée n’est pas encore une valeur certifiée',
  'href': '/?tp=zeta_series'},
 {'id': 'zeta_integrale',
  'title': 'Zêta et gamma : de la série à une intégrale de Planck',
  'href': '/?tp=zeta_integrale'},
 {'id': 'integrale_fractionnaire',
  'title': 'Intégrer une demi-fois : un noyau pondère toute l’histoire',
  'href': '/?tp=integrale_fractionnaire'},
 {'id': 'derivees_fractionnaires',
  'title': 'Caputo et Riemann–Liouville : que devient une constante ?',
  'href': '/?tp=derivees_fractionnaires'},
 {'id': 'faa_di_bruno',
  'title': 'Faà di Bruno : organiser les dérivées sans perdre les coefficients',
  'href': '/?tp=faa_di_bruno'},
 {'id': 'hermite_gauss',
  'title': 'Hermite : dériver une gaussienne, compter des zéros et construire une base',
  'href': '/?tp=hermite_gauss'}]
