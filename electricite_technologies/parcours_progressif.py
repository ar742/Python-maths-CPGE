"""Progression : techniques prioritaires, applications CPGE et prolongements."""

PROGRESSION = {'title': 'Électricité & Technologies : un parcours progressif sup / spé',
 'intro': 'Commencer par les circuits, leurs bilans et les limites des mesures. Relier ensuite temps, '
          'fréquence, électronique et acquisition. L’asservissement se construit depuis un modèle simple '
          'de moteur; les commandes avancées et la synthèse générale de filtres restent des branches.',
 'scope': 'Repères de physique PTSI, PSI et PT, avec les fonctions de transfert et performances étudiées '
          'en sciences industrielles. Ils servent à situer les compétences, sans imposer une '
          'spécialisation de l’atelier. Le socle concerne circuits, mesures, ALI, signaux et boucles '
          'élémentaires. Les inversions générales de Laplace, la transformée en z, Routh, Nyquist, '
          'l’anti-saturation intégrale et les transistors petits signaux sont des prolongements '
          'accompagnés.',
 'prerequisites': ['Sup : lois des nœuds et des mailles, résistance, condensateur, bobine, énergie et '
                   'régime sinusoïdal.',
                   'Sup : nombres complexes, EDO d’ordres 1 et 2, gain, phase, constante de temps et '
                   'mesure à l’oscilloscope.',
                   'Spé : filtrage, modèles d’ALI et acquisition; schémas-blocs, fonctions de transfert et '
                   'critères de performance en SI.'],
 'sources': [{'label': 'Programme de physique-chimie PTSI, 2021',
              'url': 'https://www.lyceedecachan.fr/wp-content/uploads/2023/07/Programme-PC-PTSI.pdf'},
             {'label': 'Programme de physique-chimie PSI, 2021',
              'url': 'https://prepas.org/ups.php?document=94'},
             {'label': 'Programme de physique-chimie PT, 2021',
              'url': 'https://prepas.org/ups.php?document=96'},
             {'label': 'Sciences industrielles PCSI–PSI, BO 2021, annexe 4',
              'url': 'https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm'}],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances sur le circuit et sa mesure',
             'intro': 'Une réponse calculée ne vaut que pour les conventions, le modèle et les instruments '
                      'annoncés.',
             'sessions': [{'id': 'sup_pont',
                           'title': '1. Équilibrer un pont et mesurer une tension',
                           'status': 'socle',
                           'level': 'Sup · circuits résistifs',
                           'labs': ['pont_wheatstone'],
                           'objective': 'Utiliser deux diviseurs de tension et comprendre le zéro d’une '
                                        'mesure différentielle.',
                           'task': 'Équilibrer les quatre branches puis modifier une résistance. Prévoir '
                                   'le signe de la tension mesurée et comparer à la courbe de sensibilité.',
                           'success': 'Écrire les tensions dans le bon sens et vérifier le rapport '
                                      'd’équilibre.',
                           'limits': 'Jauges, ponts d’impédances et influence détaillée d’un instrument '
                                     'sont des applications supplémentaires.'},
                          {'id': 'sup_rlc',
                           'title': '2. Relier transitoire, résonance et second ordre',
                           'status': 'socle',
                           'level': 'Sup · stockage, EDO et régime sinusoïdal',
                           'labs': ['rlc_transitoire', 'resonance_impedance', 'bode_second_ordre'],
                           'objective': 'Reconnaître les régimes et relier l’amortissement à la réponse '
                                        'fréquentielle.',
                           'task': 'Commencer par la charge du RLC et ses données initiales. Comparer les '
                                   'trois régimes, puis repérer la résonance en courant et la confronter '
                                   'au gain du second ordre.',
                           'success': 'Distinguer réponse libre, réponse forcée et grandeur dont on '
                                      'cherche le maximum.',
                           'limits': 'La position générale des pôles et l’inversion de Laplace sont des '
                                     'compléments; les équations élémentaires suffisent au travail de '
                                     'sup.'},
                          {'id': 'sup_instruments',
                           'title': '3. L’appareil peut modifier ce qu’il mesure',
                           'status': 'socle',
                           'level': 'Sup · impédance et formation expérimentale',
                           'labs': ['mesure_impedance', 'suiveur_cascade'],
                           'objective': 'Relier charge d’un instrument, déphasage et fonctionnement d’une '
                                        'cascade.',
                           'task': 'Mesurer l’impédance avec les amplitudes et phases proposées. Comparer '
                                   'deux filtres reliés directement puis séparés par un suiveur.',
                           'success': 'Expliquer quand une association de filtres permet de multiplier les '
                                      'gains et quand les impédances l’empêchent.',
                           'limits': 'En sup, le suiveur est un modèle fourni; ses limites de courant et '
                                     'de bande sont reprises en spé.'},
                          {'id': 'sup_initiales',
                           'title': '4. Séparer la commande et l’état initial',
                           'status': 'socle',
                           'level': 'Sup · EDO et conversion électromécanique',
                           'labs': ['laplace_initiales', 'moteur_mcc'],
                           'objective': 'Contrôler les données initiales et les échanges d’énergie d’un '
                                        'moteur modélisé.',
                           'task': 'Comparer deux états initiaux pour une même entrée. Dans le moteur '
                                   'continu, écrire séparément le bilan électrique et le bilan mécanique '
                                   'avant de suivre courant et vitesse.',
                           'success': 'Distinguer transitoire et régime établi; identifier les termes de '
                                      'conversion et de dissipation.',
                           'limits': 'Les formules de Laplace sont fournies comme autre écriture. Leur '
                                     'inversion générale n’est pas exigée en SI.'}]},
            {'id': 'spe',
             'title': 'Spé : cinq séances sur électronique, signaux et boucles',
             'intro': 'Valider le régime de fonctionnement avant d’employer une relation entrée–sortie.',
             'sessions': [{'id': 'spe_ali',
                           'title': '5. Un ALI amplifie sous conditions',
                           'status': 'socle',
                           'level': 'Spé · ALI et filtres analogiques',
                           'labs': ['ali_gain_bande', 'sommateur_inverseur', 'integrateur_derivateur'],
                           'objective': 'Établir une relation idéale puis tester bande, saturation et '
                                        'vitesse de balayage.',
                           'task': 'Calculer le gain inverseur ou sommateur par les nœuds. Augmenter '
                                   'fréquence et amplitude dans l’ALI réel, puis repérer le domaine où le '
                                   'montage intègre ou dérive.',
                           'success': 'Ne pas imposer l’égalité des tensions d’entrée hors du régime '
                                      'linéaire stable; expliquer la première limite rencontrée.',
                           'limits': 'Décalage d’entrée et dérivateur amélioré sont des compléments; leurs '
                                     'détails ne sont pas un acquis supplémentaire obligatoire.'},
                          {'id': 'spe_oscillateurs',
                           'title': '6. Le retour peut donner une mémoire ou une oscillation',
                           'status': 'socle',
                           'level': 'Spé · non-linéarités et oscillateurs',
                           'labs': ['schmitt_trigger', 'astable', 'wien'],
                           'objective': 'Distinguer contre-réaction, hystérésis et auto-oscillation.',
                           'task': 'Tracer les deux seuils de Schmitt. Utiliser ces seuils pour calculer la '
                                   'période de l’astable, puis comparer au démarrage quasi sinusoïdal de '
                                   'Wien.',
                           'success': 'Suivre les états de saturation et expliquer ce qui fixe la période '
                                      'ou limite l’amplitude.',
                           'limits': 'Les mécanismes physiques fins de stabilisation d’amplitude et les '
                                     'délais d’un comparateur sont des prolongements.'},
                          {'id': 'spe_numerique',
                           'title': '7. Échantillonner puis filtrer sans perdre la question de mesure',
                           'status': 'socle',
                           'level': 'Spé · acquisition et filtrage numérique',
                           'labs': ['echantillonnage_adc', 'filtre_rif', 'filtre_rii_z'],
                           'objective': 'Séparer repliement, quantification et mémoire d’un filtre.',
                           'task': 'Choisir une cadence admissible puis faire varier la résolution du '
                                   'convertisseur. Comparer ensuite moyenne finie et récurrence du '
                                   'passe-bas.',
                           'success': 'Écrire la règle de calcul de la sortie, préciser l’initialisation '
                                      'et expliquer le retard introduit.',
                           'limits': 'La transformée en z et les résultats généraux de stabilité sont des '
                                     'branches. Les récurrences du filtre sont données et vérifiables '
                                     'directement.'},
                          {'id': 'spe_retour',
                           'title': '8. Une boucle de moteur change les performances',
                           'status': 'socle',
                           'level': 'Sup / spé · schémas-blocs et asservissement',
                           'labs': ['retroaction_sensibilite', 'moteur_x'],
                           'objective': 'Relier gain de boucle, écart final et constante de temps.',
                           'task': 'Reprendre le moteur X avec puis sans retour négatif. Modifier un seul '
                                   'gain et prévoir l’effet sur précision et rapidité; comparer la '
                                   'sensibilité à une variation du moteur.',
                           'success': 'Établir la relation en boucle fermée et distinguer amélioration de '
                                      'performance et amplification du bruit.',
                           'limits': 'Les sensibilités logarithmiques et la robustesse générale sont des '
                                     'compléments; rester au modèle fourni pour les conclusions '
                                     'quantitatives.'},
                          {'id': 'spe_correction',
                           'title': '9. Corriger sans oublier la stabilité',
                           'status': 'socle',
                           'level': 'Spé · performances et correction en SI',
                           'labs': ['correcteur_pi', 'stabilite_marges'],
                           'objective': 'Comparer action proportionnelle et intégrale à partir d’un cahier '
                                        'des charges simple.',
                           'task': 'Choisir une consigne, comparer les réponses P et PI puis lire les '
                                   'marges sur la boucle ouverte. Vérifier précision, dépassement et temps '
                                   'de réponse.',
                           'success': 'Expliquer l’effet de l’intégrale sur l’écart permanent et le '
                                      'compromis avec la stabilité.',
                           'limits': 'Commencer sans saturation. Anti-saturation intégrale, Routh et '
                                     'critère général de Nyquist sont réservés aux prolongements.'}]},
            {'id': 'approfondissements',
             'title': 'Quatre approfondissements techniques accompagnés',
             'intro': 'Choisir un TP principal par séance; les autres proposent des comparaisons pour un '
                      'TD ou un travail personnel.',
             'sessions': [{'id': 'approfondir_puissance',
                           'title': 'A1. Choisir une conversion et vérifier ses puissances',
                           'status': 'approfondissement',
                           'level': 'Spé · conversion, particulièrement PSI',
                           'labs': ['hacheur_mcc',
                                    'onduleur_spectre',
                                    'triphase_transformateur',
                                    'puissances_compensation'],
                           'objective': 'Relier commutations, énergie de la charge et courant fourni par '
                                        'la source.',
                           'task': 'Choisir hacheur–moteur ou onduleur comme TP principal et vérifier les '
                                   'bilans. Comparer ensuite le rôle du transformateur et celui d’une '
                                   'compensation de puissance réactive.',
                           'success': 'Distinguer valeur moyenne, efficace, puissance active et facteur de '
                                      'puissance.',
                           'limits': 'Hacheur et onduleur sont centraux en PSI; le triphasé détaillé est '
                                     'un contexte fourni. Harmoniques de puissance et modulation avancée '
                                     'ne sont pas requis.'},
                          {'id': 'approfondir_diodes',
                           'title': 'A2. Une diode fait changer les équations',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · circuits par morceaux',
                           'labs': ['pont_graetz', 'diode_rc', 'redresseur_precision'],
                           'objective': 'Identifier la conduction et la continuité de tension d’un '
                                        'condensateur.',
                           'task': 'Comparer redressement en pont et diode avec lissage RC. Refaire le '
                                   'bilan sur un intervalle de conduction puis de blocage. Tester le '
                                   'redresseur à ALI comme comparaison.',
                           'success': 'Choisir l’état d’une diode avant d’appliquer les lois de circuit et '
                                      'relier recharge, ondulation et charge.',
                           'limits': 'Les schémas et modèles de diodes sont fournis; recouvrement réel et '
                                     'récupération après saturation sont des compléments.'},
                          {'id': 'approfondir_transmission',
                           'title': 'A3. Transmettre sans confondre spectre et réflexion',
                           'status': 'approfondissement',
                           'level': 'Spé · modulation et propagation',
                           'labs': ['modulation_am', 'ligne_transmission'],
                           'objective': 'Relier un codage du signal et les conditions de transport dans '
                                        'une ligne.',
                           'task': 'Prévoir les bandes latérales d’une modulation d’amplitude puis tester '
                                   'une démodulation. Dans la ligne, comparer terminaison adaptée et '
                                   'réfléchissante.',
                           'success': 'Distinguer la fréquence de la porteuse, celle du message et le '
                                      'retard de propagation.',
                           'limits': 'La modulation est au programme PSI. Détection détaillée par diode et '
                                     'équations générales des télégraphistes restent des modèles '
                                     'accompagnés.'},
                          {'id': 'approfondir_filtres',
                           'title': 'A4. Passer d’un filtre continu à une réalisation',
                           'status': 'approfondissement',
                           'level': 'Spé · modèles et filtrage',
                           'labs': ['discretisation', 'filtre_etat'],
                           'objective': 'Comparer approximation temporelle et limites internes d’un '
                                        'filtre.',
                           'task': 'Augmenter le pas des trois discrétisations du passe-bas. Dans le '
                                   'filtre à trois ALI, sélectionner une bande puis surveiller chaque '
                                   'tension interne.',
                           'success': 'Expliquer pourquoi une bonne sortie apparente ne garantit pas '
                                      'l’absence de saturation dans le montage.',
                           'limits': 'La transformation bilinéaire et la synthèse générale à variables '
                                     'd’état sont fournies comme compléments.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Approfondir après avoir contrôlé les bilans, les signaux et les performances '
                      'élémentaires.',
             'sessions': [{'id': 'prolonger_commande',
                           'title': 'P1. Pôles numériques, saturation et isolation active',
                           'status': 'prolongement',
                           'level': 'Au-delà · commande et plan z',
                           'labs': ['polezero_z',
                                    'correcteur_pi',
                                    'stabilite_marges',
                                    'isolation_sismique'],
                           'objective': 'Étudier ce que le modèle idéal de boucle ne prend pas en compte.',
                           'task': 'Déplacer un pôle numérique et suivre la réponse. Tester ensuite '
                                   'saturation et accumulation de l’intégrale. Dans l’isolation sismique, '
                                   'comparer atténuation utile et domaine du retour idéal.',
                           'success': 'Séparer stabilité linéaire, effets non linéaires de saturation et '
                                      'limites physiques d’un correcteur.',
                           'limits': 'Stabilité générale dans le plan z, anti-saturation et critères de '
                                     'Routh ou Nyquist sont des prolongements, pas des attendus généraux '
                                     'de SI.'},
                          {'id': 'prolonger_composants',
                           'title': 'P2. Polariser un transistor et multiplier une tension',
                           'status': 'prolongement',
                           'level': 'Au-delà · modèles de composants',
                           'labs': ['transistor_polarisation', 'doubleur_tension'],
                           'objective': 'Comprendre un modèle qui dépend d’un point de fonctionnement ou '
                                        'd’une séquence de charge.',
                           'task': 'Pour le transistor, vérifier le régime avant le gain de petit signal. '
                                   'Pour le doubleur, suivre les deux charges et comparer tension à vide '
                                   'et sous charge.',
                           'success': 'Ne pas appliquer une linéarisation hors de son domaine et expliquer '
                                      'les pertes du multiplicateur chargé.',
                           'limits': 'Transistor amplificateur, démarrage et asymétrie d’un multiplicateur '
                                     'sont des modèles fournis au-delà des attendus de physique PSI/PT.'},
                          {'id': 'prolonger_qualite',
                           'title': 'P3. De l’instrument idéal à la qualité du signal et de l’énergie',
                           'status': 'prolongement',
                           'level': 'Au-delà · limites et conception',
                           'labs': ['ali_gain_bande',
                                    'filtre_etat',
                                    'puissances_compensation',
                                    'onduleur_spectre'],
                           'objective': 'Distinguer précision d’amplitude, distorsion, saturation et coût '
                                        'énergétique.',
                           'task': 'Comparer le signal utile aux tensions internes d’un filtre puis au '
                                   'spectre de sortie d’un onduleur. Examiner ce qu’une compensation '
                                   'fondamentale laisse des harmoniques.',
                           'success': 'Définir la grandeur de performance recherchée avant de choisir une '
                                      'amélioration.',
                           'limits': 'Dimensionnement complet, bruit des composants et facteur de '
                                     'puissance général en régime déformé demandent une étude '
                                     'supplémentaire.'}]}],
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP '
             'sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail '
             'personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.',
 'method': ['Définir le système, le domaine et les variables avec leurs unités avant tout réglage.',
            'Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.',
            'Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.',
            'Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.'],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/electricite_technologies/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'laplace_initiales',
  'title': 'Séparer l’entrée et l’état initial',
  'href': '/?tp=laplace_initiales'},
 {'id': 'bode_second_ordre',
  'title': 'Relier résonance et réponse d’un second ordre',
  'href': '/?tp=bode_second_ordre'},
 {'id': 'retroaction_sensibilite',
  'title': 'Mesurer l’effet d’une contre-réaction',
  'href': '/?tp=retroaction_sensibilite'},
 {'id': 'moteur_x', 'title': 'Reprendre le moteur X de la fiche P17', 'href': '/?tp=moteur_x'},
 {'id': 'moteur_mcc', 'title': 'Relier courant et vitesse d’un moteur continu', 'href': '/?tp=moteur_mcc'},
 {'id': 'correcteur_pi',
  'title': 'Suivre une consigne avec un correcteur PI',
  'href': '/?tp=correcteur_pi'},
 {'id': 'stabilite_marges',
  'title': 'Lire les marges d’une boucle ouverte',
  'href': '/?tp=stabilite_marges'},
 {'id': 'isolation_sismique',
  'title': 'Atténuer le mouvement du sol par un retour',
  'href': '/?tp=isolation_sismique'},
 {'id': 'echantillonnage_adc',
  'title': 'Distinguer repliement et quantification',
  'href': '/?tp=echantillonnage_adc'},
 {'id': 'filtre_rif', 'title': 'Construire un filtre à mémoire finie', 'href': '/?tp=filtre_rif'},
 {'id': 'filtre_rii_z', 'title': 'Suivre la mémoire d’un filtre récursif', 'href': '/?tp=filtre_rii_z'},
 {'id': 'discretisation',
  'title': 'Comparer trois discrétisations d’un passe-bas',
  'href': '/?tp=discretisation'},
 {'id': 'polezero_z', 'title': 'Placer les pôles et les zéros dans le plan z', 'href': '/?tp=polezero_z'},
 {'id': 'modulation_am',
  'title': 'Transmettre un message par modulation d’amplitude',
  'href': '/?tp=modulation_am'},
 {'id': 'pont_wheatstone', 'title': 'Équilibrer un pont de Wheatstone', 'href': '/?tp=pont_wheatstone'},
 {'id': 'ligne_transmission',
  'title': 'Une ligne : propagation et réflexion',
  'href': '/?tp=ligne_transmission'},
 {'id': 'rlc_transitoire',
  'title': 'RLC : charge, oscillation et amortissement',
  'href': '/?tp=rlc_transitoire'},
 {'id': 'resonance_impedance',
  'title': 'RLC sinusoïdal : trouver la résonance',
  'href': '/?tp=resonance_impedance'},
 {'id': 'mesure_impedance', 'title': 'Mesurer une impédance avec un GBF', 'href': '/?tp=mesure_impedance'},
 {'id': 'pont_graetz', 'title': 'Redresser les deux alternances', 'href': '/?tp=pont_graetz'},
 {'id': 'doubleur_tension',
  'title': 'Doubleur : charger deux condensateurs',
  'href': '/?tp=doubleur_tension'},
 {'id': 'diode_rc', 'title': 'Diode et RC : suivre les états de conduction', 'href': '/?tp=diode_rc'},
 {'id': 'triphase_transformateur',
  'title': 'Triphasé : tensions et transformateur',
  'href': '/?tp=triphase_transformateur'},
 {'id': 'onduleur_spectre',
  'title': 'Onduleur : commande pleine onde ou décalée',
  'href': '/?tp=onduleur_spectre'},
 {'id': 'hacheur_mcc',
  'title': 'Hacheur série : alimenter une machine à courant continu',
  'href': '/?tp=hacheur_mcc'},
 {'id': 'puissances_compensation',
  'title': 'Puissance : réduire le courant par compensation',
  'href': '/?tp=puissances_compensation'},
 {'id': 'ali_gain_bande', 'title': 'ALI : gain, bande et limites', 'href': '/?tp=ali_gain_bande'},
 {'id': 'suiveur_cascade', 'title': 'Suiveur et association de filtres', 'href': '/?tp=suiveur_cascade'},
 {'id': 'sommateur_inverseur', 'title': 'Sommateur inverseur', 'href': '/?tp=sommateur_inverseur'},
 {'id': 'integrateur_derivateur',
  'title': 'Intégrer et dériver une tension',
  'href': '/?tp=integrateur_derivateur'},
 {'id': 'schmitt_trigger', 'title': 'Comparateur à hystérésis', 'href': '/?tp=schmitt_trigger'},
 {'id': 'astable', 'title': 'Oscillateur de relaxation', 'href': '/?tp=astable'},
 {'id': 'wien', 'title': 'Oscillateur à pont de Wien', 'href': '/?tp=wien'},
 {'id': 'redresseur_precision',
  'title': 'Redresseur de précision : valeur absolue',
  'href': '/?tp=redresseur_precision'},
 {'id': 'filtre_etat', 'title': 'Filtre actif à trois ALI', 'href': '/?tp=filtre_etat'},
 {'id': 'transistor_polarisation',
  'title': 'Transistor : polarisation et petits signaux',
  'href': '/?tp=transistor_polarisation'}]
