"""Progression proposée : socle, approfondissements et prolongements."""

PROGRESSION = {'title': 'Topologie & Ensembles : un parcours progressif sup / spé',
 'intro': 'En sup, partir des suites, de la densité et des valeurs intermédiaires. En spé, reformuler ces '
          'expériences avec ouverts, fermés, compacts et continuité. Les contre-exemples indiquent à quoi '
          'servent les hypothèses.',
 'scope': 'Repères MPSI et MP. En sup, la topologie abstraite n’est pas présupposée. En MP, priorité aux '
          'espaces vectoriels normés, à la compacité et à la connexité par arcs. Suites de Cauchy, '
          'complétude, Banach, Borel–Lebesgue et connexité générale sont des prolongements, même lorsque '
          'leurs exemples se calculent avec les outils du programme.',
 'prerequisites': ['Sup : intervalles, suites, limites, suites extraites, continuité et théorème des '
                   'valeurs intermédiaires.',
                   'Sup : vecteurs, produit scalaire, matrices et inégalités de norme.',
                   'Spé : définitions d’un espace vectoriel normé et caractérisation séquentielle; aucun '
                   'cours d’espaces de Banach n’est requis.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : trois séances à partir des nombres et des suites',
             'intro': 'Construire des exemples exacts avant d’introduire le vocabulaire de topologie de '
                      'spé.',
             'sessions': [{'id': 'sup_densite',
                           'title': '1. Approcher sans confondre densité et dénombrement',
                           'status': 'socle',
                           'level': 'Sup · nombres réels et suites',
                           'labs': ['rationnels_irrationnels', 'denombrer_rationnels'],
                           'objective': 'Approcher un réel par deux types de nombres et comprendre le sens '
                                        'de la densité.',
                           'task': 'Écrire les deux suites du TP qui approchent la cible réelle. Fixer une '
                                   'précision et trouver un rang convenable. Comparer à la liste finie de '
                                   'fractions affichée.',
                           'success': 'Prouver l’existence d’un rationnel et d’un irrationnel dans tout '
                                      'intervalle ouvert non vide.',
                           'limits': 'Une liste finie ne prouve pas la dénombrabilité. En sup, son '
                                     'énumération est une illustration; les cardinalités infinies seront '
                                     'reprises ensuite.'},
                          {'id': 'sup_suites',
                           'title': '2. Extraire une suite et ajouter sa limite',
                           'status': 'socle',
                           'level': 'Sup · suites bornées et valeurs d’adhérence',
                           'labs': ['bolzano_weierstrass', 'adherence_suite'],
                           'objective': 'Distinguer convergence de la suite et convergence d’une suite '
                                        'extraite.',
                           'task': 'Étudier séparément les termes pairs et impairs de la suite proposée. '
                                   'Puis comparer les points 1/n, pour les entiers n positifs, à ce même '
                                   'ensemble complété par 0.',
                           'success': 'Produire deux limites de suites extraites et expliquer pourquoi une '
                                      'limite peut manquer à l’ensemble de départ.',
                           'limits': 'Le vocabulaire adhérence, fermé et compact sera formalisé en spé; la '
                                     'preuve de convergence reste élémentaire.'},
                          {'id': 'sup_iteration',
                           'title': '3. Une itération et le bon intervalle',
                           'status': 'socle',
                           'level': 'Sup · suites récurrentes et continuité',
                           'labs': ['point_fixe', 'cauchy_rationnels'],
                           'objective': 'Étudier une récurrence avec un intervalle stable et contrôler une '
                                        'approximation.',
                           'task': 'Pour l’itération du cosinus, rechercher un intervalle stable et une '
                                   'borne d’erreur adaptée. Pour Héron, vérifier que les termes sont '
                                   'rationnels et étudier leur limite.',
                           'success': 'Utiliser la continuité au passage à la limite, après avoir justifié '
                                      'la convergence.',
                           'limits': 'Le théorème général des contractions et la complétude de ℚ ne sont '
                                     'pas nécessaires au travail de sup.'}]},
            {'id': 'spe',
             'title': 'Spé : cinq séances sur les définitions et les théorèmes',
             'intro': 'Rédiger avec les quantificateurs, un voisinage ou une suite; une figure sert à '
                      'choisir la preuve.',
             'sessions': [{'id': 'spe_ouverts',
                           'title': '4. Ouvert, fermé, intérieur et adhérence',
                           'status': 'socle',
                           'level': 'Spé MP · espaces normés',
                           'labs': ['boules_normes',
                                    'interieur_frontiere',
                                    'topologie_relative',
                                    'operations_ouverts'],
                           'objective': 'Reconnaître les quatre notions et préciser l’espace de travail.',
                           'task': 'Autour d’un point intérieur, construire un rayon admissible avec '
                                   'l’inégalité triangulaire. Comparer un bord inclus à un bord exclu. '
                                   'Étudier enfin l’intersection infinie des intervalles du TP.',
                           'success': 'Expliquer pourquoi un ouvert relatif peut ne pas être ouvert dans '
                                      'l’espace ambiant et pourquoi « fini » est essentiel pour certaines '
                                      'opérations.',
                           'limits': 'Les exemples sont choisis dans des espaces normés; aucune théorie '
                                     'générale des espaces topologiques n’est requise.'},
                          {'id': 'spe_compacts',
                           'title': '5. La compacité fait atteindre les bornes',
                           'status': 'socle',
                           'level': 'Spé MP · compacts et continuité',
                           'labs': ['valeurs_extremes', 'image_compacte'],
                           'objective': 'Appliquer fermé et borné en dimension finie, puis image continue '
                                        'd’un compact.',
                           'task': 'Comparer l’ellipse pleine avec et sans son bord. Calculer les bornes '
                                   'de la fonction linéaire du TP et décider si elles sont atteintes. '
                                   'Reprendre l’ellipse augmentée d’un segment.',
                           'success': 'Vérifier chaque hypothèse avant de conclure à un minimum ou à un '
                                      'maximum.',
                           'limits': 'La fonction d’appui et la somme de Minkowski sont des noms '
                                     'complémentaires; la preuve repose sur produit et image continue de '
                                     'compacts.'},
                          {'id': 'spe_chemins',
                           'title': '6. Convexe, connexe par arcs : construire ou interdire',
                           'status': 'socle',
                           'level': 'Spé MP · chemins et valeurs intermédiaires',
                           'labs': ['convexite', 'connexite_chemins', 'chemins_niveaux'],
                           'objective': 'Distinguer un segment contenu dans un ensemble d’un chemin '
                                        'continu quelconque.',
                           'task': 'Chercher deux points dont le segment sort de l’ensemble non convexe. '
                                   'Construire un chemin dans le plan privé de 0, puis expliquer par le '
                                   'TVI pourquoi la droite privée de 0 se comporte autrement.',
                           'success': 'Employer une paire de points comme contre-exemple à la convexité et '
                                      'une fonction continue pour interdire un chemin.',
                           'limits': 'La connexité générale sans chemins est réservée à un prolongement; '
                                     'le TP de niveaux est un exercice sur les arcs.'},
                          {'id': 'spe_normes',
                           'title': '7. Majorations et rôle de la dimension',
                           'status': 'socle',
                           'level': 'Spé MP · normes et applications linéaires',
                           'labs': ['applications_lineaires', 'normes_dimension_infinie'],
                           'objective': 'Prouver une continuité par une borne de norme et comprendre la '
                                        'portée de l’équivalence des normes.',
                           'task': 'Majorer la longueur de l’image d’un vecteur par la matrice du TP. Puis '
                                   'calculer les trois normes de la fonction x↦xⁿ sur [0,1], où n est un '
                                   'entier positif.',
                           'success': 'Expliquer pourquoi les normes considérées ne sont pas équivalentes '
                                      'sur l’espace entier des fonctions, sans contredire le théorème de '
                                      'dimension finie.',
                           'limits': 'La décomposition en valeurs singulières et les espaces Lᵖ complétés '
                                     'sont des prolongements. Une majoration explicite suffit au socle.'},
                          {'id': 'spe_heine',
                           'title': '8. Continuité, uniforme et lipschitzienne',
                           'status': 'socle',
                           'level': 'Spé MP · théorème de Heine',
                           'labs': ['heine_continuite', 'distance_ensemble'],
                           'objective': 'Savoir quelle constante dépend du point et ce qu’un compact '
                                        'permet d’uniformiser.',
                           'task': 'Comparer la fonction du TP sur un intervalle compact puis sur ℝ. Avec '
                                   'la racine carrée, chercher pourquoi une borne lipschitzienne échoue. '
                                   'Démontrer enfin que la distance à un ensemble est 1-lipschitzienne.',
                           'success': 'Rédiger les quantificateurs dans le bon ordre et distinguer '
                                      'continuité uniforme et Lipschitz.',
                           'limits': 'La régularité de Hölder est un vocabulaire complémentaire; sa borne '
                                     'précise peut être vérifiée sans théorie nouvelle.'}]},
            {'id': 'approfondissements',
             'title': 'Deux approfondissements utilisant le socle',
             'intro': 'Matrices, barycentres et contre-exemples donnent des preuves accessibles avec les '
                      'définitions de MP.',
             'sessions': [{'id': 'approfondir_matrices',
                           'title': 'A1. Des ensembles de matrices comme exemples',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · déterminant, norme et compacité',
                           'labs': ['orthogonal_compact', 'gl_composantes'],
                           'objective': 'Employer continuité polynomiale, bornitude et TVI dans un espace '
                                        'de matrices.',
                           'task': 'Prouver séparément fermeture et bornitude des matrices orthogonales. '
                                   'Comparer aux matrices de déterminant 1. Puis suivre un déterminant '
                                   'réel le long d’un chemin.',
                           'success': 'Justifier la compacité du premier ensemble, le contre-exemple du '
                                      'second et l’obstacle au changement de signe sur ℝ.',
                           'limits': 'La classification globale des composantes de GL et la décomposition '
                                     'polaire dépassent cette application des outils du programme.'},
                          {'id': 'approfondir_distance',
                           'title': 'A2. Une distance est-elle atteinte et unique ?',
                           'status': 'approfondissement',
                           'level': 'Spé · compacité, produit scalaire et contre-exemples',
                           'labs': ['distance_ensemble', 'projection_convexe', 'boule_non_compacte'],
                           'objective': 'Distinguer existence d’un point minimisant, unicité et dimension '
                                        'finie.',
                           'task': 'Comparer les deux disques à un triangle convexe. Vérifier l’inégalité '
                                   'du produit scalaire fournie pour le point projeté. Puis calculer la '
                                   'distance entre deux fonctions de la boule non compacte.',
                           'success': 'Relier existence à la compacité quand elle s’applique et expliquer '
                                      'pourquoi fermé borné ne suffit plus en dimension infinie.',
                           'limits': 'Le théorème général de projection sur un convexe fermé est un '
                                     'complément fourni. Espaces de Hilbert et théorème de Riesz sont '
                                     'au-delà.'},
                          {'id': 'approfondir_barycentres',
                           'title': 'A3. Des points à leur enveloppe convexe',
                           'status': 'approfondissement',
                           'level': 'Sup / spé · vecteurs et convexité',
                           'labs': ['enveloppe_convexe'],
                           'objective': 'Construire des combinaisons convexes et interpréter leurs '
                                        'coefficients.',
                           'task': 'Déplacer les points du nuage puis modifier les poids du barycentre. '
                                   'Vérifier qu’ils sont non négatifs et de somme 1 avant de conclure que '
                                   'le barycentre reste dans le polygone.',
                           'success': 'Justifier par récurrence qu’une combinaison convexe finie de points '
                                      'd’un convexe reste dans cet ensemble.',
                           'limits': 'Le théorème général de représentation de Carathéodory et la théorie '
                                     'des polytopes ne sont pas exigibles; les calculs utilisent seulement '
                                     'les vecteurs et la définition de convexité.'}]},
            {'id': 'prolongements',
             'title': 'Trois branches au-delà du programme',
             'intro': 'Ces branches complètent les exemples, sans ajouter des théorèmes exigibles au '
                      'parcours prioritaire.',
             'sessions': [{'id': 'prolonger_completude',
                           'title': 'P1. Cauchy, complétude et contractions',
                           'status': 'prolongement',
                           'level': 'Au-delà · espaces complets',
                           'labs': ['cauchy_rationnels',
                                    'point_fixe',
                                    'compacts_recouvrements',
                                    'extraction_aleatoire'],
                           'objective': 'Comprendre comment de nouvelles formulations décrivent la '
                                        'convergence et l’existence.',
                           'task': 'Avec Héron, distinguer rapprochement des termes et appartenance de la '
                                   'limite à l’espace choisi. Comparer ensuite contraction, recouvrements '
                                   'ouverts du segment et extraction aléatoire.',
                           'success': 'Identifier l’hypothèse supplémentaire utilisée dans chaque '
                                      'formulation et séparer une simulation finie d’un énoncé infini.',
                           'limits': 'Cauchy, complétude, Banach, Borel–Lebesgue et convergence presque '
                                     'sûre de l’extraction sont des compléments non exigibles en MP.'},
                          {'id': 'prolonger_cantor',
                           'title': 'P2. Compter sans mesurer une longueur',
                           'status': 'prolongement',
                           'level': 'Au-delà · cardinalités et Cantor',
                           'labs': ['denombrer_rationnels', 'diagonale_cantor', 'ensemble_cantor'],
                           'objective': 'Séparer densité, cardinalité et longueur dans trois '
                                        'constructions.',
                           'task': 'Expliquer pourquoi l’énumération rencontre toute fraction réduite. '
                                   'Rédiger l’argument diagonal pour une liste infinie puis suivre les '
                                   'étapes de Cantor.',
                           'success': 'Distinguer le tableau fini de la preuve infinie et expliquer '
                                      'pourquoi une longueur tendant vers zéro ne signifie pas un ensemble '
                                      'vide.',
                           'limits': 'Les faits de dénombrabilité et de non-dénombrabilité figurent en MP; '
                                     'leurs preuves détaillées et les propriétés fines de Cantor sont '
                                     'proposées en prolongement.'},
                          {'id': 'prolonger_global',
                           'title': 'P3. Chemins, inverse continu et géométrie globale',
                           'status': 'prolongement',
                           'level': 'Au-delà · exemples topologiques',
                           'labs': ['sinus_topologue',
                                    'homeomorphisme',
                                    'gl_composantes',
                                    'chemins_niveaux'],
                           'objective': 'Voir les limites d’une intuition tirée d’un tracé ou d’une '
                                        'bijection.',
                           'task': 'Comparer les deux paramétrages du TP inverse, puis construire des '
                                   'suites proches d’une coupure. Étudier les limites verticales du sinus '
                                   'du topologue et le passage entre régions de niveau.',
                           'success': 'Distinguer continuité de l’application et de son inverse; séparer '
                                      'connexité générale et connexité par arcs.',
                           'limits': 'Homéomorphismes, espaces de Hausdorff et classification globale des '
                                     'groupes sont des notions supplémentaires accompagnées.'}]}],
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
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/topologie_ensembles/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'boules_normes', 'title': 'Choisir une boule autour d’un point', 'href': '/?tp=boules_normes'},
 {'id': 'interieur_frontiere',
  'title': 'Reconnaître un point intérieur ou adhérent',
  'href': '/?tp=interieur_frontiere'},
 {'id': 'adherence_suite',
  'title': 'Ajouter une limite pour fermer un ensemble',
  'href': '/?tp=adherence_suite'},
 {'id': 'topologie_relative',
  'title': 'Chercher un ouvert dans l’espace choisi',
  'href': '/?tp=topologie_relative'},
 {'id': 'operations_ouverts',
  'title': 'Comparer une opération finie à une infinie',
  'href': '/?tp=operations_ouverts'},
 {'id': 'distance_ensemble',
  'title': 'Trouver les points les plus proches',
  'href': '/?tp=distance_ensemble'},
 {'id': 'convexite', 'title': 'Vérifier si un segment reste dans l’ensemble', 'href': '/?tp=convexite'},
 {'id': 'enveloppe_convexe',
  'title': 'Former un convexe à partir de points',
  'href': '/?tp=enveloppe_convexe'},
 {'id': 'projection_convexe',
  'title': 'Projeter sur un triangle ou un rectangle',
  'href': '/?tp=projection_convexe'},
 {'id': 'connexite_chemins',
  'title': 'Construire un chemin qui évite un point',
  'href': '/?tp=connexite_chemins'},
 {'id': 'bolzano_weierstrass',
  'title': 'Une suite bornée, deux limites de suites extraites',
  'href': '/?tp=bolzano_weierstrass'},
 {'id': 'extraction_aleatoire',
  'title': 'Le TP : garder les termes qui se rapprochent de 1',
  'href': '/?tp=extraction_aleatoire'},
 {'id': 'cauchy_rationnels',
  'title': 'Héron : des fractions qui tendent vers √2',
  'href': '/?tp=cauchy_rationnels'},
 {'id': 'compacts_recouvrements',
  'title': 'Des intervalles ouverts couvrent-ils tout le segment ?',
  'href': '/?tp=compacts_recouvrements'},
 {'id': 'valeurs_extremes',
  'title': 'Une borne supérieure peut ne pas être atteinte',
  'href': '/?tp=valeurs_extremes'},
 {'id': 'heine_continuite',
  'title': 'Continuité uniforme : un même rayon pour tous les points',
  'href': '/?tp=heine_continuite'},
 {'id': 'image_compacte',
  'title': 'Additionner deux compacts : une ellipse et un segment',
  'href': '/?tp=image_compacte'},
 {'id': 'applications_lineaires',
  'title': 'En dimension finie, une application linéaire est continue',
  'href': '/?tp=applications_lineaires'},
 {'id': 'normes_dimension_infinie',
  'title': 'Converger en moyenne ne veut pas dire uniformément',
  'href': '/?tp=normes_dimension_infinie'},
 {'id': 'boule_non_compacte',
  'title': 'Fermée et bornée ne suffit plus en dimension infinie',
  'href': '/?tp=boule_non_compacte'},
 {'id': 'denombrer_rationnels',
  'title': 'Lister les rationnels et approcher un réel',
  'href': '/?tp=denombrer_rationnels'},
 {'id': 'diagonale_cantor',
  'title': 'Construire une suite absente de la liste',
  'href': '/?tp=diagonale_cantor'},
 {'id': 'ensemble_cantor',
  'title': 'Construire un compact en retirant des intervalles',
  'href': '/?tp=ensemble_cantor'},
 {'id': 'rationnels_irrationnels',
  'title': 'Approcher un réel par des rationnels et des irrationnels',
  'href': '/?tp=rationnels_irrationnels'},
 {'id': 'sinus_topologue',
  'title': 'Un ensemble compact dans lequel certains points ne se relient pas',
  'href': '/?tp=sinus_topologue'},
 {'id': 'gl_composantes',
  'title': 'Changer le signe du déterminant en restant inversible ?',
  'href': '/?tp=gl_composantes'},
 {'id': 'orthogonal_compact',
  'title': 'Quand un ensemble de matrices est-il compact ?',
  'href': '/?tp=orthogonal_compact'},
 {'id': 'point_fixe', 'title': 'Résoudre x=cos(x) par une suite récurrente', 'href': '/?tp=point_fixe'},
 {'id': 'chemins_niveaux',
  'title': 'Relier deux régions : le rôle d’un point de contact',
  'href': '/?tp=chemins_niveaux'},
 {'id': 'homeomorphisme',
  'title': 'Une bijection continue a-t-elle une réciproque continue ?',
  'href': '/?tp=homeomorphisme'}]
