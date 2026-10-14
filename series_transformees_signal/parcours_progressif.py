"""Progression proposée : socle, approfondissements et prolongements."""

PROGRESSION = {'title': 'Séries & Signaux : un parcours progressif sup / spé',
 'intro': 'Partir de sommes finies et de signaux familiers. En spé, justifier les passages à la limite et '
          'les opérations sur les séries. Utiliser ensuite ces acquis pour comprendre un spectre, sans '
          'confondre les outils du programme avec les théorèmes nouveaux de Fourier ou de Laplace.',
 'scope': 'Repères mathématiques MPSI et MP. Les circuits sont des applications interdisciplinaires. Le '
          'programme MP cite Fourier et Laplace comme exemples d’intégrales à paramètre : les calculs de '
          'convergence, de continuité et de dérivation utilisent bien le socle. Leur théorie générale, les '
          'séries de Fourier, Fejér, Poisson et Shannon sont des prolongements; les formules nouvelles '
          'restent fournies.',
 'prerequisites': ['Sup : sommes géométriques, dérivation, développements limités, intégration sur un '
                   'segment et nombres complexes.',
                   'Sup : équations différentielles linéaires d’ordres 1 et 2; gain et phase peuvent être '
                   'repris depuis le cours de physique.',
                   'Spé : séries numériques, convergence simple, uniforme et normale, séries entières, '
                   'intégrales impropres et convergence dominée.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : trois préparations concrètes',
             'intro': 'Calculer sur des sommes finies et des solutions exactes avant d’utiliser les outils '
                      'de spé.',
             'sessions': [{'id': 'sup_geometrique',
                           'title': '1. Une somme finie et un reste exact',
                           'status': 'socle',
                           'level': 'Sup · sommes et dérivation',
                           'labs': ['geometrie'],
                           'objective': 'Contrôler une approximation avec l’identité géométrique finie.',
                           'task': 'Choisir un intervalle strictement intérieur au domaine de convergence. '
                                   'Calculer la somme finie et son reste, puis comparer à la courbe. '
                                   'Rapprocher le bord et expliquer la dégradation.',
                           'success': 'Fournir une majoration explicite du reste sur l’intervalle fixé.',
                           'limits': 'En sup, dériver les polynômes finis. Le théorème de dérivation d’une '
                                     'série entière est repris en spé.'},
                          {'id': 'sup_rc',
                           'title': '2. Relier équation différentielle et réponse d’un RC',
                           'status': 'socle',
                           'level': 'Sup · EDO d’ordre 1, application physique',
                           'labs': ['rc_reponses', 'rc_bode'],
                           'objective': 'Déterminer la réponse avec la donnée initiale puis interpréter '
                                        'gain, phase et constante de temps.',
                           'task': 'Commencer par un échelon, résoudre l’équation sans transformée et '
                                   'vérifier la valeur initiale. Comparer ensuite les trois harmoniques '
                                   'd’entrée et leur atténuation.',
                           'success': 'Distinguer régime transitoire et régime établi; reconstruire la '
                                      'réponse sinusoïdale à partir du gain et de la phase.',
                           'limits': 'La transformée de Laplace est fournie comme autre langage du même '
                                     'calcul, sans être requise à ce stade.'},
                          {'id': 'sup_rlc',
                           'title': '3. Trois régimes d’un système du second ordre',
                           'status': 'socle',
                           'level': 'Sup · EDO d’ordre 2, application physique',
                           'labs': ['rlc_poles'],
                           'objective': 'Reconnaître les régimes amortis et ajuster les constantes à deux '
                                        'données initiales.',
                           'task': 'Comparer les régimes oscillant, critique et non oscillant. Relier '
                                   'chaque courbe aux racines de l’équation caractéristique, puis vérifier '
                                   'les valeurs initiales.',
                           'success': 'Prévoir le régime avant simulation et écrire une solution adaptée, '
                                      'y compris au cas de racine double.',
                           'limits': 'L’interprétation des pôles de Laplace est facultative. Elle ne doit '
                                     'pas masquer la résolution de l’équation différentielle.'}]},
            {'id': 'spe',
             'title': 'Spé : cinq séances pour justifier les interversions',
             'intro': 'À chaque fois : préciser le domaine, le mode de convergence et le théorème '
                      'réellement applicable.',
             'sessions': [{'id': 'spe_pic',
                           'title': '4. Simple, uniforme : chercher le vrai maximum',
                           'status': 'socle',
                           'level': 'Spé · suites de fonctions',
                           'labs': ['couche_limite'],
                           'objective': 'Distinguer convergence en chaque point et contrôle uniforme sur '
                                        'un ensemble.',
                           'task': 'Localiser le maximum par dérivation avant de regarder le maillage. '
                                   'Comparer l’intervalle entier à un intervalle éloigné du bord.',
                           'success': 'Calculer ou majorer la norme uniforme et expliquer pourquoi un '
                                      'maillage fixe peut manquer le pic.',
                           'limits': 'Les couches limites d’équations différentielles sont un '
                                     'prolongement; le socle porte sur les quantificateurs et la '
                                     'majoration.'},
                          {'id': 'spe_domination',
                           'title': '5. Passer une limite sous l’intégrale',
                           'status': 'socle',
                           'level': 'Spé · convergence dominée',
                           'labs': ['concentration', 'dominee_ex12'],
                           'objective': 'Trouver un majorant intégrable indépendant du rang et détecter '
                                        'quand il manque.',
                           'task': 'Comparer l’aire de la suite concentrée à sa limite ponctuelle. Dans '
                                   'l’autre TP, écrire les trois hypothèses de convergence dominée et '
                                   'contrôler le majorant proposé.',
                           'success': 'Justifier une interversion valide et expliquer le contre-exemple '
                                      'sans conclure à partir du dessin seul.',
                           'limits': 'La convergence vers une masse de Dirac est réservée au prolongement '
                                     'sur les mesures et distributions.'},
                          {'id': 'spe_normale',
                           'title': '6. Une annulation donne une série convergente',
                           'status': 'socle',
                           'level': 'Spé · développements limités et convergence normale',
                           'labs': ['tp99_original', 'geometrie'],
                           'objective': 'Transformer une différence de termes proches en une majoration '
                                        'sommable.',
                           'task': 'Calculer le premier terme non nul de la différence. Sur un intervalle '
                                   'fixé, construire une borne indépendante du point et comparer les '
                                   'sommes partielles.',
                           'success': 'Séparer le développement à rang fixé de la majoration uniforme '
                                      'nécessaire pour sommer.',
                           'limits': 'Les difficultés d’arrondi sont un complément pratique; elles ne '
                                     'constituent pas une preuve de convergence.'},
                          {'id': 'spe_entiere',
                           'title': '7. Construire une série entière par une EDO',
                           'status': 'socle',
                           'level': 'Spé · coefficients et rayon de convergence',
                           'labs': ['arcsin_ex4', 'binomiale_ex10'],
                           'objective': 'Identifier les coefficients et justifier les opérations à '
                                        'l’intérieur du rayon de convergence.',
                           'task': 'Écrire la récurrence issue de l’EDO. Calculer les premiers '
                                   'coefficients, prévoir leur signe et contrôler le résidu. Reprendre '
                                   'ensuite le binôme à exposant non entier.',
                           'success': 'Donner le rayon ou le domaine de travail et vérifier que la somme '
                                      'satisfait l’équation avec la bonne donnée initiale.',
                           'limits': 'Les fonctions hypergéométriques et les estimations complexes de '
                                     'Cauchy restent au-delà du programme.'},
                          {'id': 'spe_aires',
                           'title': '8. Intégrer une série avec un contrôle du reste',
                           'status': 'socle',
                           'level': 'Spé · série–intégrale et restes',
                           'labs': ['integrale_sh_ex11'],
                           'objective': 'Choisir un théorème d’intégration terme à terme sur un intervalle '
                                        'non borné.',
                           'task': 'Calculer les intégrales des termes positifs, puis construire un '
                                   'encadrement de la queue. Comparer l’intégrale partielle et la somme '
                                   'des intégrales.',
                           'success': 'Vérifier les hypothèses et accompagner l’approximation d’une borne '
                                      'd’erreur.',
                           'limits': 'Les espaces fonctionnels abstraits et les transformées thermiques ne '
                                     'sont pas nécessaires à cette preuve.'}]},
            {'id': 'approfondissements',
             'title': 'Trois applications guidées à l’analyse du signal',
             'intro': 'Les identités et définitions nouvelles sont fournies. On exerce des intégrales, des '
                      'produits scalaires et des calculs trigonométriques.',
             'sessions': [{'id': 'approfondir_spectre',
                           'title': 'A1. Harmoniques et énergie',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · application de l’orthogonalité',
                           'labs': ['gibbs_fourier', 'parseval_spectre'],
                           'objective': 'Calculer l’énergie d’une somme finie d’harmoniques et observer ce '
                                        'qui se passe près d’un saut.',
                           'task': 'Vérifier les intégrales d’orthogonalité et l’identité d’énergie d’une '
                                   'somme finie. Comparer ensuite créneau et triangle reconstruits.',
                           'success': 'Distinguer une identité finie prouvée d’un résultat sur une série '
                                      'infinie; expliquer le dépassement près de la discontinuité.',
                           'limits': 'Parseval général, convergence des séries de Fourier et théorème de '
                                     'Fejér sont des prolongements fournis.'},
                          {'id': 'approfondir_mesures',
                           'title': 'A2. Une acquisition ne révèle pas toutes les fréquences',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · application aux mesures',
                           'labs': ['aliasing', 'anti_repliement', 'fenetres_fft', 'resolution'],
                           'objective': 'Distinguer repliement, fuite spectrale, pas d’affichage et '
                                        'résolution.',
                           'task': 'Trouver deux fréquences donnant les mêmes échantillons. Comparer '
                                   'ensuite une durée plus longue à l’ajout de zéros, puis un filtre avant '
                                   'la mesure.',
                           'success': 'Justifier le repliement par une identité trigonométrique; expliquer '
                                      'pourquoi les zéros ajoutés ne créent pas de nouvelles mesures.',
                           'limits': 'La FFT est un outil fourni. Son algorithme et la théorie générale '
                                     'des fenêtres ne sont pas des exigences de mathématiques MP.'},
                          {'id': 'approfondir_asymptotiques',
                           'title': 'A3. Une série pour corriger un modèle physique',
                           'status': 'approfondissement',
                           'level': 'Spé · séries, équivalents et intégration',
                           'labs': ['elliptique_pendule', 'asymptotique_ex5'],
                           'objective': 'Relier une correction mathématique à son domaine d’approximation.',
                           'task': 'Comparer la période du pendule à son approximation harmonique puis à '
                                   'sa première correction. Dans l’autre TP, étudier le rayon et la '
                                   'croissance de la série à partir de ses coefficients.',
                           'success': 'Indiquer le petit paramètre et le domaine où la correction améliore '
                                      'réellement la prévision.',
                           'limits': 'La théorie des fonctions elliptiques et la preuve par concentration '
                                     'de Poisson sont des prolongements; les formules utiles sont '
                                     'fournies.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Choisir une application après les huit séances. Ces méthodes enrichissent les TIPE '
                      'et ne remplacent pas le socle d’analyse.',
             'sessions': [{'id': 'prolonger_fourier',
                           'title': 'P1. Transformées, convolution et régularisation',
                           'status': 'prolongement',
                           'level': 'Au-delà · Fourier et Laplace intégrales',
                           'labs': ['porte_sinc',
                                    'gaussienne',
                                    'convolution_portes',
                                    'dirichlet_abel',
                                    'rc_reponses'],
                           'objective': 'Relier largeur temporelle, spectre et composition des réponses '
                                        'd’un système.',
                           'task': 'Calculer la transformée de la porte avec la convention du TP. Vérifier '
                                   'la phase d’une translation puis la convolution par recouvrement. '
                                   'Comparer à la gaussienne et à une régularisation exponentielle.',
                           'success': 'Conserver les facteurs de normalisation et séparer convergence '
                                      'impropre, absolue et limite régularisée.',
                           'limits': 'Les calculs directs de transformées sont des exemples possibles '
                                     'd’intégrales à paramètre en MP. La théorie générale, le théorème de '
                                     'convolution et les distributions causales sont des prolongements '
                                     'accompagnés.'},
                          {'id': 'prolonger_synthese',
                           'title': 'P2. Lisser, périodiser, reconstruire',
                           'status': 'prolongement',
                           'level': 'Au-delà · Poisson, Fejér et Shannon',
                           'labs': ['poisson_noyau', 'poisson_gaussienne', 'gibbs_fourier', 'shannon'],
                           'objective': 'Comprendre trois opérations sur un signal et leurs hypothèses '
                                        'propres.',
                           'task': 'Comparer lissage par Poisson et moyenne de Fejér. Pour Shannon, faire '
                                   'varier la cadence puis le nombre d’échantillons; distinguer condition '
                                   'de bande et troncature.',
                           'success': 'Séparer l’erreur de troncature d’un défaut d’hypothèse et vérifier '
                                      'les normalisations entre temps et fréquence.',
                           'limits': 'Les théorèmes de Poisson, Fejér et Shannon ne sont pas exigibles en '
                                     'mathématiques MP.'},
                          {'id': 'prolonger_traitement',
                           'title': 'P3. Suivre, transmettre et retrouver un signal',
                           'status': 'prolongement',
                           'level': 'Au-delà · méthodes techniques guidées',
                           'labs': ['spectrogramme', 'modulation', 'correlation_retard', 'debruitage'],
                           'objective': 'Choisir un outil en fonction de la question de mesure.',
                           'task': 'Suivre le chirp avec deux tailles de fenêtre. Retrouver ensuite un '
                                   'message modulé, un retard par corrélation et comparer deux '
                                   'débruitages.',
                           'success': 'Expliquer le compromis temps–fréquence et distinguer réduction du '
                                      'bruit, retard et déformation du signal utile.',
                           'limits': 'Ces traitements sont des applications techniques supplémentaires; '
                                     'aucun algorithme général nouveau n’est présenté comme exigible en '
                                     'CPGE.'}]}],
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
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/series_transformees_signal/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'couche_limite', 'title': 'Le pic qui échappe au maillage', 'href': '/?tp=couche_limite'},
 {'id': 'concentration', 'title': 'La limite perd une unité d’aire', 'href': '/?tp=concentration'},
 {'id': 'tp99_original', 'title': 'Deux termes qui s’annulent', 'href': '/?tp=tp99_original'},
 {'id': 'geometrie', 'title': 'Dériver une série sur un compact', 'href': '/?tp=geometrie'},
 {'id': 'arcsin_ex4', 'title': 'Une EDO fabrique les coefficients', 'href': '/?tp=arcsin_ex4'},
 {'id': 'asymptotique_ex5', 'title': 'Une série entière à l’échelle e²x', 'href': '/?tp=asymptotique_ex5'},
 {'id': 'binomiale_ex10', 'title': 'Au-delà du binôme polynomial', 'href': '/?tp=binomiale_ex10'},
 {'id': 'elliptique_pendule',
  'title': 'La période du pendule devient elliptique',
  'href': '/?tp=elliptique_pendule'},
 {'id': 'integrale_sh_ex11', 'title': 'Additionner des aires positives', 'href': '/?tp=integrale_sh_ex11'},
 {'id': 'dominee_ex12', 'title': 'Une domination pour des signaux complexes', 'href': '/?tp=dominee_ex12'},
 {'id': 'rc_reponses',
  'title': 'RC : du calcul de Laplace à la réponse temporelle',
  'href': '/?tp=rc_reponses'},
 {'id': 'rc_bode', 'title': 'RC : gain, phase et déformation de trois harmoniques', 'href': '/?tp=rc_bode'},
 {'id': 'rlc_poles', 'title': 'RLC : pôles, amortissement et trois régimes', 'href': '/?tp=rlc_poles'},
 {'id': 'dirichlet_abel',
  'title': 'L’intégrale de Dirichlet par régularisation d’Abel',
  'href': '/?tp=dirichlet_abel'},
 {'id': 'porte_sinc',
  'title': 'Porte, sinus cardinal et phase d’une translation',
  'href': '/?tp=porte_sinc'},
 {'id': 'gaussienne',
  'title': 'Gaussienne : Fourier et incertitude temps–fréquence',
  'href': '/?tp=gaussienne'},
 {'id': 'convolution_portes',
  'title': 'Convoluer : l’aire d’un recouvrement mobile',
  'href': '/?tp=convolution_portes'},
 {'id': 'gibbs_fourier',
  'title': 'Synthèse de Fourier : Gibbs et moyennes de Fejér',
  'href': '/?tp=gibbs_fourier'},
 {'id': 'parseval_spectre',
  'title': 'Parseval : énergie, harmoniques et sommes classiques',
  'href': '/?tp=parseval_spectre'},
 {'id': 'poisson_noyau',
  'title': 'Noyau de Poisson : convergence normale et lissage',
  'href': '/?tp=poisson_noyau'},
 {'id': 'poisson_gaussienne',
  'title': 'Poisson : une gaussienne, deux descriptions',
  'href': '/?tp=poisson_gaussienne'},
 {'id': 'shannon', 'title': 'Shannon : reconstruire un paquet à bande limitée', 'href': '/?tp=shannon'},
 {'id': 'aliasing', 'title': 'Repliement : deux fréquences, les mêmes mesures', 'href': '/?tp=aliasing'},
 {'id': 'anti_repliement',
  'title': 'Avant la mesure : le filtre antirepliement',
  'href': '/?tp=anti_repliement'},
 {'id': 'fenetres_fft', 'title': 'FFT : fuite spectrale et fenêtrage', 'href': '/?tp=fenetres_fft'},
 {'id': 'resolution', 'title': 'Résolution : voir deux fréquences proches', 'href': '/?tp=resolution'},
 {'id': 'spectrogramme', 'title': 'Spectrogramme : suivre un chirp', 'href': '/?tp=spectrogramme'},
 {'id': 'modulation', 'title': 'Modulation : traduire le spectre d’un message', 'href': '/?tp=modulation'},
 {'id': 'correlation_retard',
  'title': 'Corrélation : mesurer un temps de vol',
  'href': '/?tp=correlation_retard'},
 {'id': 'debruitage', 'title': 'Débruiter : réduction du bruit et déformation', 'href': '/?tp=debruitage'}]
