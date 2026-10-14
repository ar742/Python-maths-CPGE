"""Parcours progressif : socle CPGE et prolongements facultatifs."""

PROGRESSION = {'title': 'Probabilités : un parcours sup / spé',
 'intro': 'Construire une loi finie, calculer ses moments, puis contrôler ses fluctuations. Les exercices 6, '
          '7 et 8 servent ensuite à relier récurrences, extrema et algèbre linéaire.',
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les '
             'approfondissements et les branches au-delà du programme se choisissent ensuite, '
             'indépendamment.',
 'scope': 'Le socle MPSI / MP concerne les univers finis puis les variables discrètes, le conditionnement, '
          'l’espérance, la variance et les inégalités probabilistes. Les lois à densité (maximum uniforme, '
          'arcsinus, gaussienne), la convergence en loi et les matrices aléatoires sont explicitement des '
          'prolongements. Une expérience continue peut exercer des techniques d’intégration, sans ajouter '
          'une loi obligatoire au programme MP.',
 'prerequisites': ['Sup : dénombrement, probabilités conditionnelles, indépendance et variables sur un '
                   'univers fini.',
                   'Sup : indicatrices, espérance, variance, binomiale et suites récurrentes.',
                   'Spé : variables discrètes, covariance, Markov, Bienaymé–Tchebychev, sommes de Riemann et '
                   'matrices symétriques.'],
 'method': ['Lire les objets, les notations et les hypothèses du TP.',
            'Prévoir un résultat sur papier, puis ouvrir l’expérience.',
            'Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.',
            'Conclure par une courte preuve et distinguer résultat exact, approximation et observation.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : trois séances pour construire le modèle',
             'intro': 'Commencer par des lois calculables exactement ; la simulation vient après le '
                      'dénombrement.',
             'sessions': [{'id': 'sup_urne',
                           'title': '1. Avec ou sans remise : quel univers ?',
                           'status': 'socle',
                           'level': 'Sup · dénombrement et loi finie',
                           'labs': ['urne'],
                           'objective': 'Choisir un univers équiprobable et décrire la variable observée.',
                           'task': 'Prendre R=B=10, nombres de boules rouges et bleues, et d=10 tirages. '
                                   'Noter X le nombre de rouges. Retrouver la loi binomiale avec remise puis '
                                   'la formule combinatoire sans remise.',
                           'success': 'Expliquer l’indépendance dans un cas et la dépendance dans l’autre ; '
                                      'retrouver E(X)=5 dans les deux modèles.',
                           'limits': 'Le nom « hypergéométrique » est fourni. L’essentiel est le '
                                     'dénombrement et la vérification du modèle, pas la mémorisation d’une '
                                     'nouvelle loi.'},
                          {'id': 'sup_indicatrices',
                           'title': '2. Même moyenne, variances différentes',
                           'status': 'socle',
                           'level': 'Sup · indicatrices et variance',
                           'labs': ['urne'],
                           'objective': 'Écrire un comptage comme une somme de variables 0 ou 1.',
                           'task': 'Noter Iⱼ l’indicatrice « le tirage j est rouge » et écrire X=ΣIⱼ. '
                                   'Calculer l’espérance puis les termes croisés de E(X²). Comparer d=10 et '
                                   'd=20 dans une urne de 20 boules.',
                           'success': 'Justifier la variance nulle lorsqu’on tire toute l’urne sans remise ; '
                                      'montrer pourquoi la linéarité de l’espérance ne requiert pas '
                                      'l’indépendance.',
                           'limits': 'Introduire les covariances à partir des probabilités conjointes. Ne '
                                     'pas supposer que des tirages de même probabilité sont indépendants.'},
                          {'id': 'sup_marche',
                           'title': '3. Une marche aléatoire cache une binomiale',
                           'status': 'socle',
                           'level': 'Sup · Bernoulli et transformation d’une variable',
                           'labs': ['fluctuations'],
                           'objective': 'Traduire un déplacement en nombre de succès.',
                           'task': 'Noter n le nombre de pas, p la probabilité du pas +1 et K le nombre de '
                                   'ces pas. Établir Sₙ=2K−n pour le déplacement. Avec n=20 et p=1/2, '
                                   'calculer la probabilité de retour à l’origine.',
                           'success': 'Retrouver K de loi binomiale et P(S₂₀=0)=C(20,10)/2²⁰ ; calculer '
                                      'moyenne et variance du déplacement.',
                           'limits': 'L’approximation gaussienne et les intervalles de confiance sont '
                                     'facultatifs, au-delà de cette séance de lois finies.'}]},
            {'id': 'spe',
             'title': 'Spé : trois séances de preuve et de transversalité',
             'intro': 'Contrôler les écarts, organiser une récurrence et relier trace et moyenne.',
             'sessions': [{'id': 'spe_grands_nombres',
                           'title': '4. Une fréquence et une borne de fluctuation',
                           'status': 'socle',
                           'level': 'Spé · Bienaymé–Tchebychev',
                           'labs': ['fluctuations'],
                           'objective': 'Déduire un contrôle probabiliste d’un calcul de variance.',
                           'task': 'Noter Fₙ=K/n la fréquence, p=1/2 et ε=0,1 la tolérance. Calculer '
                                   'Var(Fₙ)=p(1−p)/n ; comparer la probabilité binomiale exacte de |Fₙ−p|≥ε '
                                   'à la borne de Bienaymé–Tchebychev pour plusieurs n.',
                           'success': 'Justifier la convergence en probabilité vers p et expliquer pourquoi '
                                      'une borne théorique peut être peu précise mais valable.',
                           'limits': 'Une trajectoire ne prouve pas la loi des grands nombres. Une borne à '
                                     'un instant donné n’est pas une garantie simultanée pour tous les '
                                     'instants.'},
                          {'id': 'spe_recurrence',
                           'title': '5. Une moyenne conservée, un second moment qui change',
                           'status': 'socle',
                           'level': 'Spé · conditionnement sur une loi finie',
                           'labs': ['polarisation'],
                           'objective': 'Calculer à l’étape suivante en conditionnant sur l’état courant.',
                           'task': 'Noter Xₙ l’état, c sa valeur initiale et λ la part remplacée. À partir '
                                   'de Xₙ=x, calculer les deux valeurs possibles de Xₙ₊₁ et leurs '
                                   'probabilités. Retrouver E(Xₙ)=c et une récurrence pour E[Xₙ(1−Xₙ)].',
                           'success': 'Obtenir E[Xₙ(1−Xₙ)]=c(1−c)(1−λ²)ⁿ par récurrence ; expliquer que '
                                      'moyenne constante ne signifie pas loi constante.',
                           'limits': 'À chaque rang fixé, les valeurs possibles sont finies. Le langage des '
                                     'martingales et les résultats de convergence presque sûre ne sont pas '
                                     'nécessaires.'},
                          {'id': 'spe_spectre',
                           'title': '6. Une moyenne spectrale par la trace',
                           'status': 'socle',
                           'level': 'Spé · théorème spectral et sommes de Riemann',
                           'labs': ['arcsinus'],
                           'objective': 'Relier un calcul matriciel à une moyenne de valeurs propres.',
                           'task': 'Noter Tₙ la matrice du chemin : 1 juste au-dessus et au-dessous de la '
                                   'diagonale, 0 ailleurs. Vérifier les vecteurs propres de composantes '
                                   'sin(jkπ/(n+1)) puis retrouver Tr(Tₙ²)/n=2(n−1)/n.',
                           'success': 'Justifier les valeurs propres 2cos(kπ/(n+1)) et leur second moment '
                                      'limite 2, sans avoir besoin d’un tirage aléatoire.',
                           'limits': 'Réduction des matrices symétriques et sommes de Riemann sont le socle. '
                                     'L’interprétation du spectre par une loi à densité arcsinus reste '
                                     'facultative.'}]},
            {'id': 'complements',
             'title': 'Approfondissements : génératrices et polarisation',
             'intro': 'Deux séances qui exploitent des outils du programme sans imposer de théorème de '
                      'processus aléatoire.',
             'sessions': [{'id': 'complement_generatrices',
                           'title': '7. Calculer une loi par un produit',
                           'status': 'approfondissement',
                           'level': 'Spé · fonctions génératrices',
                           'labs': ['fluctuations', 'urne'],
                           'objective': 'Retrouver la loi d’une somme de Bernoulli indépendantes.',
                           'task': 'Pour K, nombre de succès dans n essais indépendants de probabilité p, '
                                   'développer la fonction génératrice G(t)=(1−p+pt)ⁿ. Retrouver les '
                                   'coefficients, l’espérance et la variance par dérivation en t=1.',
                           'success': 'Relier l’indépendance au produit des génératrices et retrouver les '
                                      'calculs du laboratoire.',
                           'limits': 'Les fonctions génératrices discrètes appartiennent au programme MP. '
                                     'L’extension aux transformées de variables à densité n’est pas '
                                     'demandée.'},
                          {'id': 'complement_polarisation',
                           'title': '8. Prouver la disparition de la zone centrale',
                           'status': 'approfondissement',
                           'level': 'Spé · variable positive et majoration',
                           'labs': ['polarisation'],
                           'objective': 'Transformer un moment en une borne de probabilité.',
                           'task': 'Noter ε∈]0,1/2[ et utiliser Xₙ(1−Xₙ)≥ε(1−ε) sur l’événement ε≤Xₙ≤1−ε. '
                                   'Employer la récurrence de la séance 5 puis comparer au diagramme pour '
                                   'plusieurs valeurs de λ.',
                           'success': 'Obtenir une borne tendant vers zéro et expliquer la concentration '
                                      'près de 0 et 1, sans confondre convergence de la loi et comportement '
                                      'd’une trajectoire.',
                           'limits': 'La preuve est un exercice avec outils CPGE. La théorie générale des '
                                     'chaînes de Markov, des martingales et de leurs limites est hors du '
                                     'socle.'}]},
            {'id': 'beyond',
             'title': 'Au-delà : trois applications probabilistes',
             'intro': 'Les définitions continues sont apportées par le cours ; ces branches sont '
                      'facultatives en MPSI / MP.',
             'sessions': [{'id': 'beyond_extremes',
                           'title': 'A. Maximum, minimum et estimation',
                           'status': 'prolongement',
                           'level': 'Au-delà · lois à densité et statistique',
                           'labs': ['extremes'],
                           'objective': 'Calculer la répartition d’un maximum à partir d’une intersection '
                                        'd’événements.',
                           'task': 'Noter U₁,…,Uₙ des observations uniformes indépendantes sur [0,θ], θ>0. '
                                   'Retrouver P(Mₙ≤x)=(x/θ)ⁿ pour 0≤x≤θ, puis sa moyenne. Examiner l’écart '
                                   'Zₙ=n(1−Mₙ/θ).',
                           'success': 'Distinguer observation maximale, biais de l’estimation et changement '
                                      'd’échelle ; expliquer l’apparition d’une limite exponentielle.',
                           'limits': 'Lois uniformes à densité, statistiques d’ordre, estimation et '
                                     'convergence en loi sont des prolongements probabilistes.'},
                          {'id': 'beyond_arcsinus',
                           'title': 'B. Du cosinus à une densité',
                           'status': 'prolongement',
                           'level': 'Au-delà · loi arcsinus',
                           'labs': ['arcsinus'],
                           'objective': 'Transformer une limite de sommes de Riemann en une mesure continue.',
                           'task': 'Reprendre les valeurs 2cos(kπ/(n+1)) et la variable angulaire uniforme '
                                   'sur [0,π]. Faire le changement de variable pour retrouver la densité '
                                   '1/(π√(4−x²)) sur ]−2,2[.',
                           'success': 'Vérifier la normalisation, la symétrie et le moment d’ordre 2 ; '
                                      'expliquer les fortes concentrations près des extrémités.',
                           'limits': 'La somme de Riemann et la substitution sont des techniques CPGE. Leur '
                                     'interprétation en loi à densité est un complément fourni.'},
                          {'id': 'beyond_wigner',
                           'title': 'C. Matrices aléatoires et demi-cercle',
                           'status': 'prolongement',
                           'level': 'Au-delà · théorème de Wigner admis',
                           'labs': ['wigner'],
                           'objective': 'Comparer une matrice déterministe et une matrice à entrées '
                                        'aléatoires.',
                           'task': 'Noter Aₙ=Wₙ/√n la matrice symétrique normalisée. Choisir d’abord les '
                                   'signes ±1, puis changer la loi des entrées en gardant leur variance '
                                   'égale à 1. Comparer les moments du spectre et l’effet du nombre de '
                                   'matrices simulées.',
                           'success': 'Distinguer le demi-cercle de Wigner de la loi arcsinus ; relier le '
                                      'second moment à la normalisation et séparer fluctuation et effet de '
                                      'dimension.',
                           'limits': 'Le théorème de Wigner, l’universalité et les moments de Catalan sont '
                                     'hors programme. Les histogrammes l’illustrent sans le démontrer.'}]}],
 'sources': [{'label': 'Programme officiel de mathématiques MPSI',
              'url': 'https://prepas.org/ups.php?document=69'},
             {'label': 'Programme officiel de mathématiques MP',
              'url': 'https://prepas.org/ups.php?document=85'}],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/probabilites_cpge/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'urne', 'title': 'La remise change la loi', 'href': '/?tp=urne'},
 {'id': 'fluctuations', 'title': 'Observer la loi, maîtriser l’écart', 'href': '/?tp=fluctuations'},
 {'id': 'polarisation', 'title': 'La moyenne tient, la population se sépare', 'href': '/?tp=polarisation'},
 {'id': 'arcsinus', 'title': 'Un cosinus fait émerger la loi arcsinus', 'href': '/?tp=arcsinus'},
 {'id': 'extremes', 'title': 'Le maximum approche la frontière', 'href': '/?tp=extremes'},
 {'id': 'wigner', 'title': 'Des matrices aléatoires au demi-cercle', 'href': '/?tp=wigner'}]
