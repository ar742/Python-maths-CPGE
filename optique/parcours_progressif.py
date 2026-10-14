"""Progression : techniques prioritaires, applications CPGE et prolongements."""

PROGRESSION = {'title': 'Lumière & Images : un parcours progressif sup / spé',
 'intro': 'Construire une image et réussir une mesure en sup. En spé, relier différence de marche, '
          'contraste et résolution. Les cavités, le traitement d’image et la conversion de fréquence '
          'deviennent ensuite des branches au choix.',
 'scope': 'Repères PCSI et PC, avec les acquis de première année communs aux filières scientifiques. « '
          'Incontournable » désigne les techniques de la séance. Les chapitres d’optique ondulatoire et de '
          'polarisation dépendent de la filière; ici, le parcours de spé prend PC comme référence. Jones, '
          'les fonctions spéciales, les faisceaux gaussiens et l’optique non linéaire sont fournis comme '
          'compléments, pas comme un cours supplémentaire à mémoriser.',
 'prerequisites': ['Sup : angles à la normale, lois de Snell–Descartes, distances orientées, lentilles '
                   'minces et conditions de Gauss.',
                   'Sup : trigonométrie, nombres complexes, mesure d’une focale et incertitudes.',
                   'Spé : superposition, chemin optique, phase, interférences et diffraction; la '
                   'polarisation est abordée avec les repères de PC.'],
 'sources': [{'label': 'Physique PCSI, BO 2021, annexe 2',
              'url': 'https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm'},
             {'label': 'Programme de physique PC, 2021', 'url': 'https://prepas.org/ups.php?document=92'}],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances pour former et mesurer une image',
             'intro': 'Prévoir d’abord le trajet et les signes. Une mesure doit s’accompagner d’un modèle '
                      'et d’une incertitude.',
             'sessions': [{'id': 'sup_refraction',
                           'title': '1. Réfracter ou guider un rayon',
                           'status': 'socle',
                           'level': 'Sup · Snell–Descartes et réflexion totale',
                           'labs': ['snell', 'fibre'],
                           'objective': 'Prévoir le sens de la réfraction et l’existence d’un angle '
                                        'critique.',
                           'task': 'Comparer air–verre et verre–air. Calculer l’angle critique, puis '
                                   'expliquer le cône d’acceptance de la fibre avec la réflexion totale.',
                           'success': 'Mesurer les angles à la normale et vérifier que la réflexion totale '
                                      'exige un indice incident plus grand.',
                           'limits': 'En sup, s’arrêter aux rayons. Fresnel, modes de fibre et dispersion '
                                     'détaillée sont des compléments.'},
                          {'id': 'sup_lentille',
                           'title': '2. L’image change de nature au passage du foyer',
                           'status': 'socle',
                           'level': 'Sup · conjugaison et grandissement',
                           'labs': ['lentille'],
                           'objective': 'Construire une image réelle, virtuelle ou à l’infini avec des '
                                        'distances orientées.',
                           'task': 'Déplacer l’objet de part et d’autre du foyer d’une lentille '
                                   'convergente. Calculer position et grandissement, puis comparer à la '
                                   'lentille divergente.',
                           'success': 'Expliquer les signes et reconnaître le cas où aucune image à '
                                      'distance finie ne peut être calculée.',
                           'limits': 'Plans principaux et lentilles épaisses ne sont pas requis; les '
                                     'rayons paraxiaux restent l’hypothèse du modèle.'},
                          {'id': 'sup_mesure',
                           'title': '3. Mesurer une focale ou un indice',
                           'status': 'socle',
                           'level': 'Sup · banc optique, goniomètre et incertitudes',
                           'labs': ['bessel', 'prisme'],
                           'objective': 'Relier un réglage expérimental à une grandeur calculée.',
                           'task': 'Dans Bessel, comparer les deux positions de mise au point et leur '
                                   'fusion au cas limite. Dans le prisme, repérer la déviation minimale et '
                                   'reconstruire l’indice avec la formule fournie.',
                           'success': 'Choisir une configuration mesurable, conserver les unités et '
                                      'identifier la contribution dominante à l’incertitude.',
                           'limits': 'La dispersion de Sellmeier et les biais d’un modèle de lentille '
                                     'mince sont des prolongements.'},
                          {'id': 'sup_instruments',
                           'title': '4. Régler une lunette et corriger un œil',
                           'status': 'socle',
                           'level': 'Sup · association de lentilles et vergence',
                           'labs': ['telescope', 'oeil'],
                           'objective': 'Distinguer grandissement angulaire, mise au point et pouvoir de '
                                        'résolution.',
                           'task': 'Régler la lunette afocale, puis changer l’oculaire sans changer '
                                   'l’objectif. Avec l’œil réduit, comparer accommodation et correction de '
                                   'la myopie.',
                           'success': 'Expliquer où se forment les images et pourquoi grossir davantage ne '
                                      'crée pas de détail supplémentaire.',
                           'limits': 'Le calcul de résolution par diffraction sera repris en spé. Le '
                                     'modèle réduit n’est pas une description physiologique complète.'}]},
            {'id': 'spe',
             'title': 'Spé : quatre séances pour interpréter une figure d’ondes',
             'intro': 'Calculer une différence de marche, puis relier le résultat à une mesure de '
                      'contraste, de longueur ou de spectre.',
             'sessions': [{'id': 'spe_young',
                           'title': '5. Deux trajets, des franges et un contraste',
                           'status': 'socle',
                           'level': 'Spé · interférences à deux ondes',
                           'labs': ['young', 'coherence'],
                           'objective': 'Séparer position des franges, enveloppe et visibilité.',
                           'task': 'Prévoir l’interfrange, puis modifier séparément écart des fentes, '
                                   'largeur et déséquilibre des intensités. Comparer ensuite une source '
                                   'monochromatique à un doublet.',
                           'success': 'Relier les modifications à une différence de marche ou au '
                                      'contraste, sans confondre enveloppe de diffraction et franges.',
                           'limits': 'La cohérence générale par fonctions de corrélation est un '
                                     'prolongement. Les cas simples sont expliqués à partir des phases.'},
                          {'id': 'spe_michelson',
                           'title': '6. Mesurer avec le Michelson',
                           'status': 'socle',
                           'level': 'Spé · interférométrie, référence PC',
                           'labs': ['michelson'],
                           'objective': 'Identifier les réglages en lame d’air et en coin d’air.',
                           'task': 'Comparer anneaux et franges rectilignes. Déplacer un miroir, compter '
                                   'les franges et reconstruire un déplacement avec la longueur d’onde '
                                   'connue.',
                           'success': 'Préciser le lieu d’observation et conserver le facteur dû à '
                                      'l’aller-retour.',
                           'limits': 'Le degré d’autonomie de réglage dépend de la filière. La '
                                     'spectroscopie de Fourier complète est une branche supplémentaire.'},
                          {'id': 'spe_resolution',
                           'title': '7. Largeur d’une tache et séparation de deux raies',
                           'status': 'socle',
                           'level': 'Spé · diffraction et interférences multiples',
                           'labs': ['diffraction', 'reseau', 'airy'],
                           'objective': 'Distinguer position des maxima et finesse d’un instrument.',
                           'task': 'Commencer par l’ouverture rectangulaire, puis modifier le nombre de '
                                   'fentes d’un réseau. Comparer enfin deux étoiles avec la formule de '
                                   'résolution circulaire fournie.',
                           'success': 'Prévoir comment ouverture, longueur d’onde et nombre de fentes '
                                      'changent la largeur observée.',
                           'limits': 'Les fonctions de Bessel et la théorie de l’apodisation sont '
                                     'fournies; aucune connaissance de ces fonctions n’est présupposée.'},
                          {'id': 'spe_polarisation',
                           'title': '8. Reconnaître et transformer une polarisation',
                           'status': 'socle',
                           'level': 'Spé · formation expérimentale PC',
                           'labs': ['polarisation'],
                           'objective': 'Utiliser polariseur, analyseur et lame à retard pour identifier '
                                        'un état lumineux.',
                           'task': 'Vérifier Malus sur une lumière rectiligne, puis placer une lame quart '
                                   'd’onde et comparer les positions des axes. Faire tourner l’analyseur.',
                           'success': 'Distinguer une extinction possible d’une intensité indépendante de '
                                      'l’analyseur et relier ces observations à la polarisation.',
                           'limits': 'Le formalisme matriciel de Jones est fourni. Stokes, Poincaré et le '
                                     'qubit de polarisation sont des prolongements.'}]},
            {'id': 'approfondissements',
             'title': 'Trois approfondissements avec les outils de CPGE',
             'intro': 'Reprendre une approximation connue et mesurer ce qu’elle laisse de côté.',
             'sessions': [{'id': 'approfondir_image',
                           'title': 'A1. Plus grand ne signifie pas mieux résolu',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · instruments et limites du modèle',
                           'labs': ['microscope', 'aberrations'],
                           'objective': 'Relier image intermédiaire, ouverture et aberration géométrique.',
                           'task': 'Régler le microscope à l’infini et modifier l’ouverture numérique. '
                                   'Comparer ensuite miroir sphérique et paraboloïde pour des rayons '
                                   'proches puis éloignés de l’axe.',
                           'success': 'Séparer défaut de mise au point, aberration et limite de '
                                      'diffraction.',
                           'limits': 'Objectifs réels et conception d’un télescope demandent d’autres '
                                     'modèles; les comparaisons ici sont accompagnées.'},
                          {'id': 'approfondir_chemin',
                           'title': 'A2. Un trajet extrémal peut devenir courbe',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · optimisation et gradients d’indice',
                           'labs': ['fermat', 'mirage'],
                           'objective': 'Retrouver Snell par un temps de parcours et suivre un rayon dans '
                                        'un indice variable.',
                           'task': 'Chercher le point de passage qui rend le temps stationnaire dans '
                                   'Fermat. Dans Mirage, faire varier le gradient d’indice et comparer la '
                                   'courbure du rayon.',
                           'success': 'Définir le temps ou le chemin optique optimisé et vérifier les '
                                      'hypothèses du profil choisi.',
                           'limits': 'La théorie variationnelle générale, l’eikonale et l’Hamiltonien '
                                     'optique sont au-delà du programme.'},
                          {'id': 'approfondir_arc',
                           'title': 'A3. L’arc-en-ciel est une déviation stationnaire',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · trigonométrie, dérivation et dispersion',
                           'labs': ['arcenciel'],
                           'objective': 'Expliquer pourquoi de nombreux rayons ressortent près d’une même '
                                        'direction.',
                           'task': 'Tracer la déviation en fonction de l’incidence, localiser son extremum '
                                   'et comparer deux indices correspondant à deux couleurs.',
                           'success': 'Relier l’ordre des couleurs à la dispersion et distinguer un angle '
                                      'stationnaire d’un rayon unique.',
                           'limits': 'Les arcs surnuméraires, les caustiques d’Airy et la diffusion de Mie '
                                     'sont des prolongements.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Choisir une branche après les mesures et les figures d’interférences.',
             'sessions': [{'id': 'prolonger_cavite',
                           'title': 'P1. Une cavité sélectionne des fréquences',
                           'status': 'prolongement',
                           'level': 'Au-delà · interférences multiples et laser',
                           'labs': ['fabryperot', 'laser', 'coherence'],
                           'objective': 'Relier résonance, finesse, stabilité de cavité et seuil '
                                        'd’amplification.',
                           'task': 'Comparer deux réflectivités dans Fabry–Perot. Dans Laser, vérifier '
                                   'séparément la stabilité géométrique de la cavité et le bilan de gain '
                                   'au seuil.',
                           'success': 'Distinguer sélection fréquentielle et amplification; préciser ce '
                                      'que le modèle de seuil ne décrit pas.',
                           'limits': 'Airy de cavité, modes propres et dynamique des populations sont '
                                     'définis sur place et ne constituent pas un socle commun exigible.'},
                          {'id': 'prolonger_fourier',
                           'title': 'P2. Filtrer une image et propager un faisceau fini',
                           'status': 'prolongement',
                           'level': 'Au-delà · Fourier optique et faisceaux gaussiens',
                           'labs': ['fourier', 'gaussien', 'airy'],
                           'objective': 'Relier fréquence spatiale, ouverture et finesse d’une structure '
                                        'observée.',
                           'task': 'Placer successivement un filtre passe-bas et un filtre coupant les '
                                   'basses fréquences dans le banc 4f. Comparer ensuite la taille minimale '
                                   'et la divergence du faisceau gaussien.',
                           'success': 'Distinguer fréquence spatiale et fréquence temporelle; expliquer le '
                                      'compromis entre largeur du faisceau et divergence.',
                           'limits': 'Paramètre complexe du faisceau, phase de Gouy, déconvolution et '
                                     'fonctions de transfert générales sont des compléments accompagnés.'},
                          {'id': 'prolonger_nonlineaire',
                           'title': 'P3. Convertir la fréquence dans un cristal',
                           'status': 'prolongement',
                           'level': 'Au-delà · optique non linéaire',
                           'labs': ['nonlineaire'],
                           'objective': 'Comprendre le rôle de l’accord de phase et du bilan d’énergie.',
                           'task': 'Comparer accord et désaccord de phase, puis diminuer l’hypothèse de '
                                   'pompe non épuisée. Suivre séparément les puissances des deux '
                                   'fréquences.',
                           'success': 'Expliquer pourquoi la longueur du cristal ne suffit pas à garantir '
                                      'une conversion croissante.',
                           'limits': 'Susceptibilité d’ordre 2, Manley–Rowe et conversion paramétrique '
                                     'dépassent les attendus CPGE; les équations et notations sont '
                                     'fournies.'}]}],
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP '
             'sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail '
             'personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.',
 'method': ['Définir le système, le domaine et les variables avec leurs unités avant tout réglage.',
            'Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.',
            'Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.',
            'Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.'],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/optique/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'snell', 'title': 'Snell : réfraction et réflexion totale', 'href': '/?tp=snell'},
 {'id': 'lentille',
  'title': "Conjugaison : image réelle, virtuelle ou à l'infini",
  'href': '/?tp=lentille'},
 {'id': 'bessel', 'title': 'Bessel : mesurer une focale et ses incertitudes', 'href': '/?tp=bessel'},
 {'id': 'telescope', 'title': 'Lunette astronomique : grossir ou résoudre ?', 'href': '/?tp=telescope'},
 {'id': 'microscope',
  'title': 'Microscope : image intermédiaire et ouverture numérique',
  'href': '/?tp=microscope'},
 {'id': 'oeil', 'title': 'Œil : accommodation, défauts et correction', 'href': '/?tp=oeil'},
 {'id': 'fibre', 'title': "Fibre : cône d'acceptance et dispersion modale", 'href': '/?tp=fibre'},
 {'id': 'mirage', 'title': "Mirage : un rayon courbe dans un gradient d'indice", 'href': '/?tp=mirage'},
 {'id': 'arcenciel',
  'title': "Arc-en-ciel : stationnarité et dispersion d'une goutte",
  'href': '/?tp=arcenciel'},
 {'id': 'prisme', 'title': 'Prisme : goniomètre, minimum et Cauchy', 'href': '/?tp=prisme'},
 {'id': 'aberrations', 'title': 'Miroir : la sphère face au paraboloïde', 'href': '/?tp=aberrations'},
 {'id': 'fermat', 'title': 'Fermat : choisir le passage le plus rapide', 'href': '/?tp=fermat'},
 {'id': 'young', 'title': 'Young : franges, enveloppe et déséquilibre', 'href': '/?tp=young'},
 {'id': 'reseau', 'title': 'Réseau : résoudre un doublet spectral', 'href': '/?tp=reseau'},
 {'id': 'diffraction', 'title': 'Ouvertures : rectangle et apodisation', 'href': '/?tp=diffraction'},
 {'id': 'polarisation', 'title': 'Jones : lame à retard et analyseur', 'href': '/?tp=polarisation'},
 {'id': 'michelson', 'title': "Michelson : anneaux et coin d'air", 'href': '/?tp=michelson'},
 {'id': 'coherence',
  'title': 'Cohérence : spectre, source étendue et battements',
  'href': '/?tp=coherence'},
 {'id': 'fabryperot', 'title': "Fabry–Perot : coefficient d'Airy et finesse", 'href': '/?tp=fabryperot'},
 {'id': 'fourier', 'title': 'Banc 4f : filtrer vraiment une image', 'href': '/?tp=fourier'},
 {'id': 'laser', 'title': 'Laser : stabilité, seuil et saturation', 'href': '/?tp=laser'},
 {'id': 'gaussien', 'title': 'Faisceau gaussien : waist, diffraction et Gouy', 'href': '/?tp=gaussien'},
 {'id': 'airy', 'title': 'Airy : séparer deux étoiles', 'href': '/?tp=airy'},
 {'id': 'nonlineaire',
  'title': 'χ² : doubler la fréquence et épuiser la pompe',
  'href': '/?tp=nonlineaire'}]
