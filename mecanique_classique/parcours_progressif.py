"""Progression : techniques prioritaires, applications CPGE et prolongements."""

PROGRESSION = {'title': 'Mécanique & Mouvements : un parcours progressif sup / spé',
 'intro': 'Choisir les bons bilans en sup, puis étudier contacts, référentiels et petites oscillations en '
          'spé. Les applications astrophysiques et les anharmonicités relient les calculs à des situations '
          'concrètes. La rotation spatiale et les bifurcations avancées restent des branches accompagnées.',
 'scope': 'Repères PCSI et PC, avec MPSI pour les forces centrales et le solide en rotation autour d’un '
          'axe fixe. Le socle porte sur énergie, quantité de mouvement, moment cinétique, oscillations et '
          'choix du référentiel. Masse réduite, König général, tenseur d’inertie et modèles de roulement '
          'sont explicités quand ils dépassent ces attendus; leur présence dans un TP ne les rend pas '
          'obligatoires pour toutes les filières.',
 'prerequisites': ['Sup : deuxième loi de Newton, énergie mécanique, moment cinétique, gravitation et '
                   'mouvement circulaire.',
                   'Sup : oscillateur harmonique, radians, dérivation, développements limités et rotation '
                   'autour d’un axe fixe.',
                   'Spé : bilans vectoriels, référentiels non galiléens selon la filière, stabilité d’un '
                   'équilibre et petites oscillations.'],
 'sources': [{'label': 'Physique PCSI, BO 2021, annexe 2',
              'url': 'https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm'},
             {'label': 'Physique MPSI, BO 2021',
              'url': 'https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm'},
             {'label': 'Programme de physique PC, 2021', 'url': 'https://prepas.org/ups.php?document=92'}],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances pour choisir le bon bilan',
             'intro': 'Définir le système et le référentiel avant d’utiliser une conservation.',
             'sessions': [{'id': 'sup_orbite',
                           'title': '1. Une orbite se lit avec deux invariants',
                           'status': 'socle',
                           'level': 'Sup · gravitation et forces centrales',
                           'labs': ['orbite_kepler', 'potentiel_effectif'],
                           'objective': 'Relier énergie et moment cinétique à la forme accessible d’une '
                                        'trajectoire.',
                           'task': 'Commencer par une orbite circulaire puis changer la vitesse de '
                                   'lancement. Comparer les aires balayées et les points de rebroussement '
                                   'du potentiel effectif.',
                           'success': 'Justifier les conservations et distinguer orbite liée, trajectoire '
                                      'de fuite et région inaccessible.',
                           'limits': 'L’équation générale des coniques et la résolution de Kepler sont '
                                     'fournies; en sup, priorité aux bilans et aux cas simples.'},
                          {'id': 'sup_pendule',
                           'title': '2. Quand le petit angle devient insuffisant',
                           'status': 'socle',
                           'level': 'Sup · énergie et oscillateur harmonique',
                           'labs': ['pendule_exact'],
                           'objective': 'Construire la linéarisation et identifier sa limite '
                                        'd’utilisation.',
                           'task': 'Comparer deux petites amplitudes puis une amplitude plus grande. '
                                   'Retrouver l’équation harmonique et utiliser l’énergie pour expliquer '
                                   'le ralentissement près du sommet.',
                           'success': 'Vérifier la période harmonique et exprimer les angles en radians '
                                      'avant toute approximation.',
                           'limits': 'L’intégrale exacte de période est fournie. Sa nature elliptique '
                                     'n’est pas une connaissance préalable.'},
                          {'id': 'sup_rotation',
                           'title': '3. Une barre tourne autour d’un axe fixe',
                           'status': 'socle',
                           'level': 'Sup · énergie et moment cinétique',
                           'labs': ['barre_bascule', 'inertie_huygens'],
                           'objective': 'Choisir un axe et relier moment d’inertie, couple et énergie de '
                                        'rotation.',
                           'task': 'Définir l’axe de la barre et écrire le bilan énergétique. Dans le '
                                   'nuage de masses, calculer les distances à un axe fixé puis comparer '
                                   'deux axes.',
                           'success': 'Ne pas confondre force et moment d’une force; vérifier les '
                                      'dimensions du moment d’inertie.',
                           'limits': 'La matrice d’inertie et ses axes principaux sont réservés aux '
                                     'prolongements; le calcul autour d’un axe suffit ici.'},
                          {'id': 'sup_interactions',
                           'title': '4. Deux objets échangent leur quantité de mouvement',
                           'status': 'socle',
                           'level': 'Sup · système et interactions mutuelles',
                           'labs': ['deux_corps'],
                           'objective': 'Expliquer ce que conserve un système isolé et ce que chaque objet '
                                        'ne conserve pas seul.',
                           'task': 'Comparer deux masses égales puis très différentes. Calculer la '
                                   'quantité de mouvement totale et suivre le centre de masse dans le '
                                   'référentiel choisi.',
                           'success': 'Faire disparaître les forces internes dans le bilan total et '
                                      'distinguer mouvement d’ensemble et mouvement relatif.',
                           'limits': 'Masse réduite et identités générales de König sont introduites en '
                                     'application, sans devenir des formules obligatoires pour toutes les '
                                     'voies.'}]},
            {'id': 'spe',
             'title': 'Spé : quatre séances sur les régimes et les approximations',
             'intro': 'Vérifier les hypothèses du régime avant d’en exploiter les équations.',
             'sessions': [{'id': 'spe_contact',
                           'title': '5. Adhérer, glisser ou s’arrêter',
                           'status': 'socle',
                           'level': 'Sup / spé · PFD et lois de frottement',
                           'labs': ['coulomb_horizontal', 'plan_incline'],
                           'objective': 'Distinguer frottement d’adhérence et frottement de glissement.',
                           'task': 'Avec la caisse, augmenter la traction puis l’inverser. Écrire le bilan '
                                   'sur un plan incliné et tester l’inégalité d’adhérence avant de choisir '
                                   'la loi de glissement.',
                           'success': 'Justifier chaque changement de régime et le sens de la dissipation.',
                           'limits': 'Le roulement du solide du second TP est un complément guidé; '
                                     'commencer par la caisse en translation. Les attendus précis de '
                                     'Coulomb dépendent de la filière.'},
                          {'id': 'spe_referentiels',
                           'title': '6. Une trajectoire dépend aussi du référentiel',
                           'status': 'socle',
                           'level': 'Spé PC · référentiels en rotation',
                           'labs': ['coriolis', 'foucault'],
                           'objective': 'Séparer force réelle et termes liés au référentiel tournant.',
                           'task': 'Comparer la même trajectoire dans les deux référentiels. Pour '
                                   'Foucault, modifier la latitude et prévoir le signe ainsi que la durée '
                                   'de précession.',
                           'success': 'Écrire correctement les produits vectoriels et distinguer période '
                                      'd’oscillation et période de précession.',
                           'limits': 'La solution complexe détaillée de Foucault est une application '
                                     'fournie; les corrections géophysiques restent au-delà.'},
                          {'id': 'spe_modes',
                           'title': '7. Plusieurs masses : chercher des mouvements simples',
                           'status': 'socle',
                           'level': 'Spé · équations couplées et modes propres',
                           'labs': ['chaine_atomique', 'molecule_co2'],
                           'objective': 'Construire des modes à partir des équations de chaque masse.',
                           'task': 'Commencer par une translation uniforme de la chaîne. Comparer ensuite '
                                   'les deux vibrations du modèle de CO₂ et vérifier les forces dans un '
                                   'mode choisi.',
                           'success': 'Relier chaque forme de vibration à une fréquence et identifier le '
                                      'mode de translation sans rappel.',
                           'limits': 'L’orthogonalité pondérée par les masses est expliquée. Intensités '
                                     'spectroscopiques et théorie générale des phonons sont des '
                                     'prolongements.'},
                          {'id': 'spe_anharmonicite',
                           'title': '8. Linéariser, puis mesurer l’anharmonicité',
                           'status': 'socle',
                           'level': 'Spé · équilibre, stabilité et développement limité',
                           'labs': ['pendule_anharmonique', 'ressorts_transverses'],
                           'objective': 'Relier la courbure du potentiel aux petites oscillations et '
                                        'contrôler une correction.',
                           'task': 'Retrouver le terme cubique du pendule et comparer période harmonique '
                                   'et période corrigée. Dans les ressorts, chercher les équilibres et '
                                   'étudier leur stabilité par le potentiel.',
                           'success': 'Préciser l’amplitude utilisée et le domaine de l’approximation; ne '
                                      'pas conclure à l’instabilité lorsque la courbure est nulle.',
                           'limits': 'La méthode générale de Lindstedt et les théorèmes de bifurcation '
                                     'sont des branches; les premiers développements utilisent les '
                                     'techniques de CPGE.'}]},
            {'id': 'approfondissements',
             'title': 'Trois applications accompagnées des bilans',
             'intro': 'Les formules orbitales ou de contact sont fournies quand elles dépassent le socle.',
             'sessions': [{'id': 'approfondir_espace',
                           'title': 'A1. Changer d’orbite ou effectuer un survol',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · applications astrophysiques',
                           'labs': ['transfert_hohmann', 'diffusion_gravitationnelle'],
                           'objective': 'Suivre l’énergie et la vitesse lors d’un changement de '
                                        'trajectoire.',
                           'task': 'Calculer les deux impulsions de Hohmann, puis comparer le survol dans '
                                   'le référentiel de la planète et dans celui de l’étoile.',
                           'success': 'Identifier le référentiel dans lequel l’énergie est conservée et '
                                      'celui dans lequel un gain ou une perte est possible.',
                           'limits': 'L’optimalité générale des transferts et les fenêtres '
                                     'interplanétaires ne sont pas démontrées par ces deux modèles.'},
                          {'id': 'approfondir_bilans',
                           'title': 'A2. Une différence de champ, une masse échangée',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · marées et propulsion',
                           'labs': ['marees', 'fusee'],
                           'objective': 'Choisir ce que l’on soustrait ou ce qui traverse la frontière du '
                                        'système.',
                           'task': 'Comparer attraction et différence d’attraction dans le TP marées. Pour '
                                   'la fusée, faire le bilan sur un court intervalle en incluant la masse '
                                   'éjectée.',
                           'success': 'Retrouver l’échelle du champ de marée et expliquer l’origine du '
                                      'logarithme dans la vitesse de la fusée.',
                           'limits': 'Tenseur de marée, dislocation et optimisation d’une propulsion '
                                     'réelle demandent des modèles supplémentaires.'},
                          {'id': 'approfondir_solide',
                           'title': 'A3. Le mouvement du centre de masse ne suffit pas',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · solide et contact',
                           'labs': ['konig', 'cylindre_bord', 'plan_incline'],
                           'objective': 'Séparer translation et rotation puis déterminer jusqu’où un '
                                        'régime de contact reste valide.',
                           'task': 'Vérifier la décomposition d’énergie fournie par König. Pour le '
                                   'cylindre au bord, comparer les deux événements possibles et arrêter le '
                                   'modèle au premier seuil.',
                           'success': 'Contrôler à la fois réaction normale et condition de frottement; '
                                      'reconstruire les équations si le régime change.',
                           'limits': 'König général et roulement spatial sont des compléments accompagnés. '
                                     'Les réactions calculées avant glissement ne valent pas après.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Choisir une branche après les bilans, les équilibres et la linéarisation.',
             'sessions': [{'id': 'prolonger_nonlineaire',
                           'title': 'P1. Une raideur nulle et une résonance non linéaire',
                           'status': 'prolongement',
                           'level': 'Au-delà · changements d’échelle et bifurcations',
                           'labs': ['oscillateur_quartique', 'duffing_force', 'ressorts_transverses'],
                           'objective': 'Comprendre ce qui remplace l’approximation harmonique et ce '
                                        'qu’une courbe de réponse ne prouve pas.',
                           'task': 'Dans le potentiel quartique, comparer deux amplitudes et rechercher la '
                                   'loi d’échelle de période. Dans Duffing, comparer la réponse linéaire '
                                   'aux branches de balance harmonique.',
                           'success': 'Distinguer existence d’une réponse approchée, stabilité et '
                                      'réalisation dynamique.',
                           'limits': 'Balance harmonique, bifurcations universelles, hystérésis et chaos '
                                     'nécessitent une étude supplémentaire; le dessin seul ne les établit '
                                     'pas.'},
                          {'id': 'prolonger_rotation',
                           'title': 'P2. La rotation spatiale d’un solide',
                           'status': 'prolongement',
                           'level': 'Au-delà · tenseur d’inertie et gyroscopes',
                           'labs': ['barre_rotule', 'gyroscope', 'inertie_huygens'],
                           'objective': 'Comprendre pourquoi le moment cinétique n’est pas toujours '
                                        'parallèle à la vitesse de rotation.',
                           'task': 'Comparer le cas plan de la barre au mouvement sur rotule. Pour la '
                                   'toupie, modifier la rotation propre et suivre précession et nutation.',
                           'success': 'Distinguer les invariants et les axes; contrôler les conditions qui '
                                      'permettent une précession régulière.',
                           'limits': 'Tenseurs, équations d’Euler et réduction lagrangienne dépassent le '
                                     'modèle de rotation autour d’un axe fixe du socle.'},
                          {'id': 'prolonger_temps',
                           'title': 'P3. Le temps devient difficile près d’une trajectoire limite',
                           'status': 'prolongement',
                           'level': 'Au-delà · séparatrices et calcul orbital',
                           'labs': ['pendule_exact', 'orbite_kepler', 'chaine_atomique'],
                           'objective': 'Comparer une représentation géométrique à une évolution à temps '
                                        'uniforme.',
                           'task': 'Approcher le sommet du pendule puis comparer les positions orbitales à '
                                   'des instants équidistants. En complément, suivre la déformation d’une '
                                   'impulsion dans la chaîne.',
                           'success': 'Expliquer pourquoi une trajectoire régulière peut correspondre à '
                                      'une vitesse très variable ou à une période divergente.',
                           'limits': 'Intégrales elliptiques, résolution de Kepler et vitesse de groupe '
                                     'sont des prolongements dont les outils sont fournis.'}]}],
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP '
             'sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail '
             'personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.',
 'method': ['Définir le système, le domaine et les variables avec leurs unités avant tout réglage.',
            'Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.',
            'Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.',
            'Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.'],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/mecanique_classique/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'orbite_kepler',
  'title': 'Kepler : suivre une planète et mesurer les aires balayées',
  'href': '/?tp=orbite_kepler'},
 {'id': 'deux_corps', 'title': 'Deux étoiles : passer au centre de masse', 'href': '/?tp=deux_corps'},
 {'id': 'potentiel_effectif',
  'title': 'Lancement orbital : lire les points de rebroussement',
  'href': '/?tp=potentiel_effectif'},
 {'id': 'transfert_hohmann',
  'title': 'Rejoindre une autre orbite : deux impulsions de Hohmann',
  'href': '/?tp=transfert_hohmann'},
 {'id': 'diffusion_gravitationnelle',
  'title': 'Survol gravitationnel : dévier sans moteur',
  'href': '/?tp=diffusion_gravitationnelle'},
 {'id': 'marees',
  'title': 'Marées : comparer attraction et différence d’attraction',
  'href': '/?tp=marees'},
 {'id': 'fusee', 'title': 'Fusée : faire le bilan d’un système qui perd de la masse', 'href': '/?tp=fusee'},
 {'id': 'coriolis',
  'title': 'Référentiel tournant : une droite peut devenir une courbe',
  'href': '/?tp=coriolis'},
 {'id': 'chaine_atomique',
  'title': 'Une chaîne : modes propres, propagation et dispersion',
  'href': '/?tp=chaine_atomique'},
 {'id': 'molecule_co2',
  'title': 'CO₂ : trois masses, deux vibrations et une translation',
  'href': '/?tp=molecule_co2'},
 {'id': 'foucault', 'title': 'Foucault : oscillation rapide, précession lente', 'href': '/?tp=foucault'},
 {'id': 'pendule_exact',
  'title': 'Pendule : mesurer la période sans petit angle',
  'href': '/?tp=pendule_exact'},
 {'id': 'pendule_anharmonique',
  'title': 'Anharmonicité : période corrigée et troisième harmonique',
  'href': '/?tp=pendule_anharmonique'},
 {'id': 'ressorts_transverses',
  'title': 'Deux ressorts : créer deux équilibres stables',
  'href': '/?tp=ressorts_transverses'},
 {'id': 'oscillateur_quartique',
  'title': 'Au seuil : un oscillateur sans raideur linéaire',
  'href': '/?tp=oscillateur_quartique'},
 {'id': 'duffing_force',
  'title': 'Duffing : une résonance qui dépend de l’amplitude',
  'href': '/?tp=duffing_force'},
 {'id': 'inertie_huygens',
  'title': 'Six masses : quel axe résiste le plus à la rotation ?',
  'href': '/?tp=inertie_huygens'},
 {'id': 'konig',
  'title': 'Décomposer le mouvement d’un solide : les deux théorèmes de König',
  'href': '/?tp=konig'},
 {'id': 'barre_bascule',
  'title': 'Une barre bascule : énergie, durée et réaction du pivot',
  'href': '/?tp=barre_bascule'},
 {'id': 'barre_rotule',
  'title': 'Une barre sur rotule : mouvement spatial et moment cinétique',
  'href': '/?tp=barre_rotule'},
 {'id': 'cylindre_bord',
  'title': 'Un cylindre au bord de la table : quel événement survient d’abord ?',
  'href': '/?tp=cylindre_bord'},
 {'id': 'coulomb_horizontal',
  'title': 'Tirer, freiner puis inverser une caisse : changer de régime',
  'href': '/?tp=coulomb_horizontal'},
 {'id': 'plan_incline', 'title': 'Glisser ou rouler sur un plan incliné ?', 'href': '/?tp=plan_incline'},
 {'id': 'gyroscope', 'title': 'Toupie pesante : précession lente et nutation', 'href': '/?tp=gyroscope'}]
