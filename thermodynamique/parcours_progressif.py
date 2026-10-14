"""Progression : techniques prioritaires, applications CPGE et prolongements."""

PROGRESSION = {'title': 'Énergie & Transferts : un parcours progressif sup / spé',
 'intro': 'Commencer par les systèmes, les signes et les machines. Donner ensuite la priorité aux '
          'transferts et à la diffusion : bilans locaux, conditions aux limites et échelles de temps. Les '
          'potentiels et effets couplés offrent des applications; la thermodynamique hors équilibre reste '
          'une branche accompagnée.',
 'scope': 'Repères PCSI et PC, complétés par MP pour les systèmes ouverts et la diffusion numérique. « '
          'Incontournable » désigne les techniques de bilan, de résolution et de contrôle, pas toutes les '
          'formules du TP. Helmholtz, exergie, modèles thermoélectriques, Langevin et transport '
          'électrolytique sont définis sur place. Le potentiel de Gibbs se relie aussi à la chimie de spé; '
          'il n’est pas annoncé comme un acquis identique de toutes les filières.',
 'prerequisites': ['Sup : système fermé, gaz parfait, premier et deuxième principes, chaleur latente et '
                   'machines dithermes.',
                   'Sup : travail, énergie, puissance, équations différentielles du premier ordre et '
                   'température absolue.',
                   'Spé : flux orientés, bilans locaux, lois de Fourier et de Fick, équation de diffusion '
                   'et conditions aux limites.'],
 'sources': [{'label': 'Physique PCSI, BO 2021, annexe 2',
              'url': 'https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm'},
             {'label': 'Programme de physique PC, 2021', 'url': 'https://prepas.org/ups.php?document=92'},
             {'label': 'Programme de physique-chimie MP, 2021',
              'url': 'https://prepas.org/ups.php?document=87'}],
 'stages': [{'id': 'sup',
             'title': 'Sup : quatre séances pour tenir un bilan',
             'intro': 'Choisir le système, les échanges et la convention de signe avant de calculer.',
             'sessions': [{'id': 'sup_travail',
                           'title': '1. Même état final, échanges différents',
                           'status': 'socle',
                           'level': 'Sup · premier principe et travail',
                           'labs': ['travail_chemins', 'travaux_generalises'],
                           'objective': 'Distinguer variation d’une fonction d’état et travail échangé.',
                           'task': 'Comparer les trois chemins du gaz parfait. Calculer le travail par '
                                   'l’aire orientée puis le bilan énergétique. Choisir ensuite un ressort '
                                   'ou un condensateur parmi les travaux généralisés.',
                           'success': 'Conserver les signes choisis et expliquer pourquoi les échanges '
                                      'dépendent du chemin.',
                           'limits': 'Travaux de surface et conventions magnétiques sont des compléments '
                                     'fournis; commencer par pression, ressort et condensateur.'},
                          {'id': 'sup_calorimetrie',
                           'title': '2. Trouver l’état final avec le bon système',
                           'status': 'socle',
                           'level': 'Sup · calorimétrie et entropie',
                           'labs': ['calorimetrie_entropie', 'detentes_joule'],
                           'objective': 'Identifier la grandeur conservée et décider s’il subsiste '
                                        'plusieurs phases.',
                           'task': 'Dans le calorimètre isolé, comparer les bilans avant et après '
                                   'changement d’état. Pour les détentes, distinguer le système fermé de '
                                   'Joule et le bilan enthalpique fourni pour l’étranglement.',
                           'success': 'Calculer la température finale et distinguer chaleur échangée et '
                                      'entropie créée.',
                           'limits': 'Le bilan détaillé d’un système ouvert est repris en spé. Van der '
                                     'Waals et l’inversion de Joule–Thomson sont des prolongements.'},
                          {'id': 'sup_machines',
                           'title': '3. Une machine ne transforme pas toute la chaleur en travail',
                           'status': 'socle',
                           'level': 'Sup · machines dithermes et cycles',
                           'labs': ['carnot_ditherme', 'cycles_moteurs'],
                           'objective': 'Relier fonctionnement, rendement ou coefficient de performance '
                                        'aux deux principes.',
                           'task': 'Comparer moteur, réfrigérateur et pompe à chaleur. Vérifier le bilan '
                                   'd’un cycle idéal choisi puis comparer sa performance à la borne de '
                                   'Carnot.',
                           'success': 'Employer les températures en kelvins et distinguer un rendement '
                                      'd’un coefficient de performance.',
                           'limits': 'Les cycles techniques sont des applications idéales; régénération '
                                     'réelle et sources variables demandent un modèle supplémentaire.'},
                          {'id': 'sup_transferts',
                           'title': '4. Des watts traversent une paroi',
                           'status': 'socle',
                           'level': 'Sup → spé · préparation aux transferts',
                           'labs': ['fourier_barre', 'paroi_composite'],
                           'objective': 'Distinguer densité de flux, puissance et énergie transférée.',
                           'task': 'Utiliser la loi de Fourier fournie pour une barre stationnaire. '
                                   'Comparer ensuite les résistances du mur et repérer la plus grande '
                                   'chute de température.',
                           'success': 'Vérifier les unités et l’égalité des puissances dans les éléments '
                                      'en série.',
                           'limits': 'En sup, priorité aux bilans et aux résistances fournies. '
                                     'L’établissement local de Fourier et de l’équation de chaleur est '
                                     'l’objectif de spé.'}]},
            {'id': 'spe',
             'title': 'Spé : quatre séances prioritaires sur la diffusion',
             'intro': 'Un profil calculé doit satisfaire le bilan local, l’état initial et les conditions '
                      'aux limites.',
             'sessions': [{'id': 'spe_diffusion',
                           'title': '5. Construire et résoudre la diffusion à une dimension',
                           'status': 'socle',
                           'level': 'Spé · bilan local et conditions aux limites',
                           'labs': ['diffusion_1d', 'demi_espace'],
                           'objective': 'Relier les dérivées spatiales à la variation temporelle et '
                                        'contrôler un calcul numérique.',
                           'task': 'Établir l’équation de chaleur par bilan d’une tranche. Comparer deux '
                                   'pas de calcul dans Diffusion 1D. Dans le demi-espace, prévoir la '
                                   'profondeur affectée puis vérifier son évolution en racine du temps.',
                           'success': 'Préciser température initiale et conditions de bord; distinguer un '
                                      'phénomène physique d’une instabilité du schéma.',
                           'limits': 'La fonction spéciale de la solution de choc thermique est fournie. '
                                     'Schémas implicites et théorie d’erreur générale sont des '
                                     'prolongements.'},
                          {'id': 'spe_oscillations',
                           'title': '6. Le thermique filtre les variations rapides',
                           'status': 'socle',
                           'level': 'Spé · temps de diffusion et réponse harmonique',
                           'labs': ['onde_thermique', 'refroidissement_biot'],
                           'objective': 'Comparer atténuation, retard de phase et validité d’une '
                                        'température uniforme.',
                           'task': 'Comparer une excitation journalière à une excitation annuelle. Dans le '
                                   'refroidissement, modifier le nombre de Biot et confronter centre, '
                                   'surface et moyenne.',
                           'success': 'Relier la longueur de pénétration à la diffusivité et à la période; '
                                      'expliciter l’hypothèse du modèle uniforme.',
                           'limits': 'Les modes convectifs sont fournis. Leur résolution générale et '
                                     'l’identification inverse de diffusivité sont des compléments.'},
                          {'id': 'spe_bilans',
                           'title': '7. Le pic diminue, l’énergie reste, l’entropie augmente',
                           'status': 'socle',
                           'level': 'Spé · conservation et second principe',
                           'labs': ['diffusion_2d', 'entropie_diffusion'],
                           'objective': 'Distinguer valeur maximale, intégrale d’énergie et création '
                                        'd’entropie.',
                           'task': 'Suivre l’étalement de la tache et vérifier sa normalisation. Dans le '
                                   'système isolé, calculer la température d’équilibre et le signe de la '
                                   'création d’entropie.',
                           'success': 'Identifier ce que conserve le modèle et ce qui évolue '
                                      'irréversiblement.',
                           'limits': 'Le noyau de chaleur général, convolution et principes variationnels '
                                     'hors équilibre sont des prolongements.'},
                          {'id': 'spe_particules',
                           'title': '8. Diffuser de la matière avec ou sans absorption',
                           'status': 'socle',
                           'level': 'Spé PC · Fick, source et bilan',
                           'labs': ['marche_aleatoire', 'absorption_neutrons'],
                           'objective': 'Relier une variance, un flux et une équation de diffusion.',
                           'task': 'Calculer moyenne et variance de la marche symétrique avec les données '
                                   'du TP. Dans le modèle de neutrons, écrire séparément diffusion, source '
                                   'et absorption.',
                           'success': 'Retrouver l’échelle de diffusion et vérifier le bilan intégral de '
                                      'l’absorption.',
                           'limits': 'Le modèle neutronique est une application fournie, pas un cours de '
                                     'réacteur. La théorie probabiliste continue vient en prolongement.'}]},
            {'id': 'approfondissements',
             'title': 'Quatre approfondissements appliqués',
             'intro': 'Choisir une question et utiliser les bilans déjà acquis. Les nouveaux coefficients '
                      'et potentiels sont définis dans le TP.',
             'sessions': [{'id': 'approfondir_potentiels',
                           'title': 'A1. L’équilibre comme minimum d’un potentiel adapté',
                           'status': 'approfondissement',
                           'level': 'Spé · contraintes et équilibre',
                           'labs': ['potentiel_helmholtz', 'potentiel_gibbs'],
                           'objective': 'Choisir une fonction à minimiser en précisant ce qui reste '
                                        'imposé.',
                           'task': 'Dans la cloison élastique, calculer la force et vérifier le minimum de '
                                   'Helmholtz à température et volume total fixés. Dans la réaction '
                                   'idéale, comparer pente de Gibbs et déplacement vers l’équilibre.',
                           'success': 'Relier signe d’une dérivée et sens d’évolution, puis séparer '
                                      'condition stationnaire et stabilité.',
                           'limits': 'Les potentiels sont fournis. Gibbs se relie à la chimie de spé; '
                                     'Helmholtz et la minimisation générale ne sont pas un acquis commun '
                                     'de physique de toutes les voies.'},
                          {'id': 'approfondir_isolation',
                           'title': 'A2. Plus d’isolant signifie-t-il moins de pertes ?',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · géométrie et résistances',
                           'labs': ['isolation_radiale', 'igloo'],
                           'objective': 'Tenir compte de la variation de surface dans un bilan thermique.',
                           'task': 'Comparer une paroi plane à la géométrie radiale. Chercher le rayon '
                                   'critique, puis vérifier le bilan de l’igloo et l’existence d’une '
                                   'épaisseur admissible.',
                           'success': 'Expliquer le compromis entre résistance conductrice et surface '
                                      'd’échange.',
                           'limits': 'Ponts thermiques, ventilation, fusion et rayonnement net ne sont pas '
                                     'inclus dans ces deux modèles.'},
                          {'id': 'approfondir_transformations',
                           'title': 'A3. Un système ouvert ou une vapeur change les contraintes',
                           'status': 'approfondissement',
                           'level': 'Spé · enthalpie, compression et changements d’état',
                           'labs': ['compresseur_etages', 'brouillard'],
                           'objective': 'Choisir un bilan adapté à la matière traversante et aux limites '
                                        'de phase.',
                           'task': 'Comparer compression en un et plusieurs étages avec refroidissement '
                                   'intermédiaire. Pour la vapeur, comparer les évolutions de pression et '
                                   'de saturation au début de la détente.',
                           'success': 'Justifier la répartition des rapports de pression et repérer le '
                                      'seuil où le modèle monophasé cesse de suffire.',
                           'limits': 'L’optimisation générale des étages et la nucléation des gouttes sont '
                                     'des compléments; le TP brouillard s’arrête au début de '
                                     'condensation.'},
                          {'id': 'approfondir_mesures',
                           'title': 'A4. Mesurer et refroidir avec des effets couplés',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · bilans et calibration',
                           'labs': ['cube_leslie', 'seebeck', 'peltier'],
                           'objective': 'Comparer mesure de température, émission et puissance de '
                                        'refroidissement.',
                           'task': 'Choisir un TP principal : comparer les surfaces de Leslie, calibrer le '
                                   'thermocouple avec sa jonction froide, ou écrire le bilan complet du '
                                   'module Peltier. Utiliser les autres comme comparaisons.',
                           'success': 'Conserver les unités et les signes; distinguer signal de mesure, '
                                      'chaleur transférée et consommation électrique.',
                           'limits': 'Les lois radiatives et coefficients thermoélectriques utiles sont '
                                     'fournis. Aucun modèle microscopique de transport n’est requis.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Approfondir les modèles couplés après avoir maîtrisé les bilans et les échelles de '
                      'diffusion.',
             'sessions': [{'id': 'prolonger_brownien',
                           'title': 'P1. Du mouvement inertiel à la diffusion brownienne',
                           'status': 'prolongement',
                           'level': 'Au-delà · Langevin et fluctuations',
                           'labs': ['brownien_langevin', 'marche_aleatoire'],
                           'objective': 'Distinguer régimes balistique et diffusif.',
                           'task': 'Comparer les durées devant le temps de relaxation du TP. Faire varier '
                                   'rayon, viscosité et température, puis confronter la diffusion à la '
                                   'marche symétrique.',
                           'success': 'Relier les échelles aux paramètres et distinguer trajectoire '
                                      'aléatoire et moyenne statistique.',
                           'limits': 'Langevin, Ornstein–Uhlenbeck et limite brownienne sont des théories '
                                     'supplémentaires accompagnées.'},
                          {'id': 'prolonger_irreversible',
                           'title': 'P2. Énergie disponible et transports hors équilibre',
                           'status': 'prolongement',
                           'level': 'Au-delà · exergie et transport électrolytique',
                           'labs': ['exergie_corps', 'diffusion_electrolyte', 'entropie_diffusion'],
                           'objective': 'Comprendre comment un gradient permet un travail ou produit un '
                                        'courant et une dissipation.',
                           'task': 'Comparer travail maximal réversible et simple mise en contact du corps '
                                   'chaud. Dans l’électrolyte, distinguer flux des deux espèces et courant '
                                   'électrique.',
                           'success': 'Expliquer pourquoi conserver l’énergie ne signifie pas conserver sa '
                                      'capacité à fournir un travail.',
                           'limits': 'Exergie, Nernst–Planck, couches de Debye et thermodynamique '
                                     'irréversible dépassent le socle; leurs hypothèses sont précisées.'},
                          {'id': 'prolonger_couplages',
                           'title': 'P3. Quand chaleur, son et électricité se répondent',
                           'status': 'prolongement',
                           'level': 'Au-delà · thermoacoustique et piézoélectricité',
                           'labs': ['thermoacoustique', 'piezo_resonateur'],
                           'objective': 'Relier une réponse mécanique à un transfert thermique ou '
                                        'électrique.',
                           'task': 'Dans l’onde couplée, faire varier le temps de diffusion thermique. '
                                   'Dans le quartz, comparer résonance et antirésonance et vérifier la '
                                   'réciprocité du couplage.',
                           'success': 'Identifier les variables conjuguées et distinguer réponse '
                                      'oscillante et branche diffusive.',
                           'limits': 'Les modèles de machines thermoacoustiques et de résonateurs '
                                     'piézoélectriques sont des prolongements fournis, pas des résultats à '
                                     'mémoriser.'}]}],
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP '
             'sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail '
             'personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.',
 'method': ['Définir le système, le domaine et les variables avec leurs unités avant tout réglage.',
            'Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.',
            'Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.',
            'Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.'],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/thermodynamique/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'fourier_barre',
  'title': 'Fourier : une barre relie deux thermostats',
  'href': '/?tp=fourier_barre'},
 {'id': 'paroi_composite',
  'title': 'Un mur : conduction et convection en série',
  'href': '/?tp=paroi_composite'},
 {'id': 'isolation_radiale',
  'title': 'Rayon critique : ajouter un isolant peut accroître la perte',
  'href': '/?tp=isolation_radiale'},
 {'id': 'igloo', 'title': 'Igloo : bilan d’une personne et géométrie hémisphérique', 'href': '/?tp=igloo'},
 {'id': 'diffusion_1d',
  'title': 'Diffusion 1D : calcul stable et modes de Fourier',
  'href': '/?tp=diffusion_1d'},
 {'id': 'demi_espace', 'title': 'Choc thermique : une profondeur en √(χt)', 'href': '/?tp=demi_espace'},
 {'id': 'onde_thermique',
  'title': 'Onde thermique : filtrer le jour et les saisons',
  'href': '/?tp=onde_thermique'},
 {'id': 'refroidissement_biot',
  'title': 'Biot : quand peut-on supposer une température uniforme ?',
  'href': '/?tp=refroidissement_biot'},
 {'id': 'diffusion_2d',
  'title': 'Une tache de chaleur : énergie conservée, pic qui s’étale',
  'href': '/?tp=diffusion_2d'},
 {'id': 'marche_aleatoire',
  'title': 'Marche aléatoire : de la loi binomiale à Fick',
  'href': '/?tp=marche_aleatoire'},
 {'id': 'brownien_langevin',
  'title': 'Langevin : du mouvement inertiel à Stokes–Einstein',
  'href': '/?tp=brownien_langevin'},
 {'id': 'absorption_neutrons',
  'title': 'Neutrons : diffusion, absorption et bilan de source',
  'href': '/?tp=absorption_neutrons'},
 {'id': 'diffusion_electrolyte',
  'title': 'Électrolyte : diffusion commune et potentiel de jonction',
  'href': '/?tp=diffusion_electrolyte'},
 {'id': 'entropie_diffusion',
  'title': 'Diffuser sans perdre d’énergie : l’entropie augmente',
  'href': '/?tp=entropie_diffusion'},
 {'id': 'travail_chemins',
  'title': 'Même état final, travaux différents : suivre trois chemins',
  'href': '/?tp=travail_chemins'},
 {'id': 'travaux_generalises',
  'title': 'Surface, fil, condensateur, bobine : une force conjuguée',
  'href': '/?tp=travaux_generalises'},
 {'id': 'potentiel_helmholtz',
  'title': 'Helmholtz : une cloison interne cherche le minimum de F',
  'href': '/?tp=potentiel_helmholtz'},
 {'id': 'potentiel_gibbs',
  'title': 'Gibbs : l’équilibre d’une réaction A ⇌ B minimise G',
  'href': '/?tp=potentiel_gibbs'},
 {'id': 'calorimetrie_entropie',
  'title': 'Calorimètre : température finale, chaleur latente et entropie',
  'href': '/?tp=calorimetrie_entropie'},
 {'id': 'detentes_joule',
  'title': 'Joule : U constante ou H constante, deux détentes différentes',
  'href': '/?tp=detentes_joule'},
 {'id': 'carnot_ditherme',
  'title': 'Carnot : moteur, réfrigérateur et pompe à chaleur',
  'href': '/?tp=carnot_ditherme'},
 {'id': 'cycles_moteurs',
  'title': 'Otto, Diesel, Brayton, Stirling : comparer des cycles calculés',
  'href': '/?tp=cycles_moteurs'},
 {'id': 'compresseur_etages',
  'title': 'Compresseur : répartir les rapports de pression pour minimiser le travail',
  'href': '/?tp=compresseur_etages'},
 {'id': 'exergie_corps',
  'title': 'Corps fini : une différence de température vaut-elle du travail ?',
  'href': '/?tp=exergie_corps'},
 {'id': 'cube_leslie',
  'title': 'Cube de Leslie : comparer des surfaces à même température',
  'href': '/?tp=cube_leslie'},
 {'id': 'seebeck',
  'title': 'Thermocouple : calibrer et compenser la jonction froide',
  'href': '/?tp=seebeck'},
 {'id': 'peltier', 'title': 'Module Peltier : refroidir demande un bilan complet', 'href': '/?tp=peltier'},
 {'id': 'thermoacoustique',
  'title': 'Onde sonore : coupler compression et diffusion thermique',
  'href': '/?tp=thermoacoustique'},
 {'id': 'piezo_resonateur',
  'title': 'Quartz : réciprocité, résonance et antirésonance',
  'href': '/?tp=piezo_resonateur'},
 {'id': 'brouillard',
  'title': 'Détente d’une vapeur saturante : décider du début de condensation',
  'href': '/?tp=brouillard'}]
