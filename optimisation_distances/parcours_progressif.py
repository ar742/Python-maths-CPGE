"""Parcours progressif : socle CPGE et prolongements facultatifs."""

PROGRESSION = {'title': 'Distances & Optimisation : un parcours sup / spé',
 'intro': 'Choisir l’objet et la distance avant de chercher un minimum. Commencer par projections et '
          'inégalités, puis traiter les contraintes et les certificats numériques.',
 'duration': 'Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les '
             'approfondissements et les branches au-delà du programme se choisissent ensuite, '
             'indépendamment.',
 'scope': 'Les techniques incontournables sont celles de MPSI / MP : intégration, projection sur un '
          'sous-espace de dimension finie, compacité, théorème spectral et optimisation sous une contrainte '
          'régulière. Une séance prioritaire ne rend pas obligatoire tout son laboratoire. Approximation '
          'uniforme, algorithmes de descente, équation séculaire et séparation à marge maximale restent des '
          'compléments.',
 'prerequisites': ['Sup : produit scalaire, norme, projection orthogonale, intégration et calcul matriciel.',
                   'Sup : inégalités, trigonométrie et changement de repère orthonormé.',
                   'Spé : compacité, matrices symétriques, gradient et optimisation sous contrainte.'],
 'method': ['Lire les objets, les notations et les hypothèses du TP.',
            'Prévoir un résultat sur papier, puis ouvrir l’expérience.',
            'Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.',
            'Conclure par une courte preuve et distinguer résultat exact, approximation et observation.'],
 'stages': [{'id': 'sup',
             'title': 'Sup : trois séances de projection et d’inégalités',
             'intro': 'Chercher des cas que l’on peut calculer exactement avant d’explorer les réglages '
                      'généraux.',
             'sessions': [{'id': 'sup_normes',
                           'title': '1. Approcher cosinus : définir le critère',
                           'status': 'socle',
                           'level': 'Sup · intégration et norme',
                           'labs': ['approximation'],
                           'objective': 'Distinguer erreur quadratique intégrée et plus grand écart.',
                           'task': 'Noter t la variable, L=π/2 la borne et p(t)=at+b la droite d’essai. '
                                   'Fixer le degré à 1 et le poids κ à 0. Écrire I(a,b)=∫₀ᴸ(cos t−at−b)²dt ; '
                                   'calculer les intégrales nécessaires puis comparer deux droites d’essai.',
                           'success': 'Expliquer pourquoi √I est une distance et pourquoi I est une '
                                      'quadratique en a,b.',
                           'limits': 'Commencer par l’erreur intégrée. La droite minimax dorée correspond à '
                                     'un autre critère et sera étudiée en complément.'},
                          {'id': 'sup_projection',
                           'title': '2. Deux projections : fonctions et matrices',
                           'status': 'socle',
                           'level': 'Sup · orthogonalité',
                           'labs': ['approximation', 'matrices'],
                           'objective': 'Utiliser l’orthogonalité pour identifier un meilleur approximant.',
                           'task': 'Pour le cosinus, imposer l’orthogonalité du résidu aux fonctions 1 et t. '
                                   'Pour une matrice réelle M, écrire M=S+A avec S=(M+Mᵀ)/2 et A=(M−Mᵀ)/2 ; '
                                   'employer le produit scalaire de Frobenius, somme des produits des '
                                   'coefficients.',
                           'success': 'Démontrer l’orthogonalité de S et A et retrouver la distance d’une '
                                      'rotation d’angle θ aux matrices symétriques : √2|sin θ|.',
                           'limits': 'Les projections sont prioritaires ; la contrainte det A=1, le mode '
                                     'complexe et le conditionnement seront repris plus tard.'},
                          {'id': 'sup_boite',
                           'title': '3. Une boîte maximale dans un ellipsoïde',
                           'status': 'socle',
                           'level': 'Sup · inégalité et substitution',
                           'labs': ['produit'],
                           'objective': 'Séparer la géométrie des demi-axes et l’optimisation des '
                                        'coordonnées réduites.',
                           'task': 'Prendre les demi-axes a=3,b=2,c=1 et les trois exposants égaux à 1. Pour '
                                   'un point (x,y,z) de la surface, poser u=x²/a², v=y²/b², w=z²/c². '
                                   'Utiliser u+v+w=1 pour majorer uvw.',
                           'success': 'Obtenir le volume maximal 8abc/(3√3), identifier les huit choix de '
                                      'signes et justifier l’égalité.',
                           'limits': 'L’inégalité arithmético-géométrique peut être démontrée dans le TD. '
                                     'Les exposants quelconques et les multiplicateurs restent facultatifs à '
                                     'ce palier.'}]},
            {'id': 'spe',
             'title': 'Spé : trois séances pour contrôler un extremum',
             'intro': 'Ajouter existence, condition nécessaire et justification globale.',
             'sessions': [{'id': 'spe_existence',
                           'title': '4. Surface, solide et existence des extrema',
                           'status': 'socle',
                           'level': 'Spé · compacité et continuité',
                           'labs': ['point', 'paire'],
                           'objective': 'Déterminer sur quel ensemble la distance est minimisée avant de '
                                        'calculer.',
                           'task': 'Noter p le point extérieur ou intérieur et C le centre de l’ellipsoïde. '
                                   'Sur une sphère de rayon r, comparer distance à la surface et distance au '
                                   'solide. Choisir ensuite p=C et trois demi-axes distincts ; prévoir les '
                                   'extrema sur la surface.',
                           'success': 'Justifier l’existence par continuité sur un compact ; retrouver les '
                                      'petit et grand demi-axes au centre et la distance nulle au solide.',
                           'limits': 'Le calcul général entre deux ellipsoïdes est facultatif. La compacité '
                                     'et la distinction des ensembles sont les objectifs de cette séance.'},
                          {'id': 'spe_contrainte',
                           'title': '5. Optimiser sous une contrainte régulière',
                           'status': 'socle',
                           'level': 'Spé · gradients et Lagrange',
                           'labs': ['produit', 'point'],
                           'objective': 'Écrire des conditions nécessaires sans les confondre avec une '
                                        'preuve de minimum global.',
                           'task': 'Pour l’ellipsoïde, noter g(x,y,z)=x²/a²+y²/b²+z²/c²−1 la contrainte. '
                                   'Vérifier ∇g≠0 sur la surface. Retrouver les candidats du produit de '
                                   'coordonnées puis écrire les équations pour la distance au carré à p.',
                           'success': 'Contrôler la contrainte, comparer les valeurs candidates et retrouver '
                                      'une justification globale dans les cas élémentaires.',
                           'limits': 'Les multiplicateurs pour une contrainte régulière sont au programme '
                                     'MP. L’équation séculaire et ses cas singuliers sont des prolongements '
                                     'du calcul général.'},
                          {'id': 'spe_spectral',
                           'title': '6. La dimension change l’existence',
                           'status': 'socle',
                           'level': 'Spé · déterminant et théorème spectral',
                           'labs': ['matrices'],
                           'objective': 'Vérifier que l’ensemble contraint existe, puis exploiter une '
                                        'matrice positive.',
                           'task': 'Noter A une matrice réelle antisymétrique de taille n et imposer det '
                                   'A=1. Comparer n=3 puis n=4. Pour n pair, utiliser les valeurs propres '
                                   'positives de AᵀA et leur produit pour obtenir ‖A‖F≥√n.',
                           'success': 'Prouver que l’ensemble est vide en dimension impaire ; construire un '
                                      'exemple atteignant √n en dimension paire.',
                           'limits': 'La distance de cet ensemble particulier est un exercice guidé. En '
                                     'complexe, transposée et adjoint doivent être distingués avant de '
                                     'réutiliser la preuve.'}]},
            {'id': 'complements',
             'title': 'Approfondissements : deux critères et une précision',
             'intro': 'Réutiliser le socle dans des méthodes fournies.',
             'sessions': [{'id': 'complement_uniforme',
                           'title': '7. L² et uniforme ne choisissent pas la même droite',
                           'status': 'approfondissement',
                           'level': 'Sup / Spé · convexité et extrema',
                           'labs': ['approximation'],
                           'objective': 'Comprendre comment la norme choisie modifie le meilleur '
                                        'approximant.',
                           'task': 'Garder L=π/2, degré 1 et κ=0. Comparer la projection verte et la droite '
                                   'uniforme dorée ; étudier le résidu aux extrémités et à ses points '
                                   'critiques. Puis rendre le poids κ positif et expliquer quelle droite '
                                   'dépend de ce poids.',
                           'success': 'Relier les contacts du résidu uniforme à une majoration sur tout '
                                      'l’intervalle ; distinguer ce contrôle d’un maximum simplement '
                                      'échantillonné.',
                           'limits': 'Le résultat général d’alternance en approximation uniforme n’est pas '
                                     'au programme. La construction affine du TP est un exemple accompagné.'},
                          {'id': 'complement_encadrement',
                           'title': '8. Un calcul doit rendre des comptes',
                           'status': 'approfondissement',
                           'level': 'Spé · Cauchy–Schwarz et majoration',
                           'labs': ['paire'],
                           'objective': 'Lire une borne inférieure et une valeur admissible pour contrôler '
                                        'un minimum.',
                           'task': 'Choisir « Deux sphères ». Noter D la distance des centres et r₁,r₂ leurs '
                                   'rayons ; retrouver max(0,D−r₁−r₂). Comparer les bornes affichées L et U, '
                                   'puis passer aux ellipsoïdes d’axes distincts.',
                           'success': 'Expliquer pourquoi deux points admissibles donnent une borne '
                                      'supérieure et une projection sur une direction unitaire une borne '
                                      'inférieure.',
                           'limits': 'Les bornes du logiciel sont en virgule flottante, sans arithmétique '
                                     'd’intervalles. Un écart petit contrôle le problème numérique, pas une '
                                     'certification exacte de tous les arrondis.'}]},
            {'id': 'beyond',
             'title': 'Au-delà : trois pistes au choix',
             'intro': 'Le programme fournit les outils pour entrer dans ces branches ; les théories '
                      'nouvelles restent facultatives.',
             'sessions': [{'id': 'beyond_descente',
                           'title': 'A. Descente de gradient et conditionnement',
                           'status': 'prolongement',
                           'level': 'Au-delà · optimisation numérique',
                           'labs': ['approximation'],
                           'objective': 'Relier le pas d’un algorithme à la géométrie d’une quadratique.',
                           'task': 'Suivre la descente dans le plan des paramètres a,b. Comparer l’arrivée à '
                                   'l’optimum exact, puis augmenter le degré et regarder le conditionnement '
                                   'de la matrice de Gram et de la base normalisée.',
                           'success': 'Distinguer mauvais choix de pas, sensibilité des coordonnées et '
                                      'existence d’un minimum unique.',
                           'limits': 'Algorithmes de descente, QR et analyse générale du conditionnement '
                                     'sont des compléments numériques.'},
                          {'id': 'beyond_seculaire',
                           'title': 'B. Distance générale à un ellipsoïde',
                           'status': 'prolongement',
                           'level': 'Au-delà · équation séculaire et cas singuliers',
                           'labs': ['point'],
                           'objective': 'Traiter des extrema avec plusieurs axes et des multiplicateurs '
                                        'singuliers.',
                           'task': 'Partir d’un point extérieur, puis du centre et d’un axe principal. Lire '
                                   'le tableau de contrainte, de stationnarité et de matrice de preuve ; '
                                   'comparer un cas régulier et un cas singulier.',
                           'success': 'Identifier ce qui garantit un extremum global, même quand plusieurs '
                                      'points réalisent la même distance.',
                           'limits': 'La résolution de l’équation séculaire et son traitement singulier sont '
                                     'fournis, au-delà des techniques exigibles.'},
                          {'id': 'beyond_separation',
                           'title': 'C. Séparation et marge maximale',
                           'status': 'prolongement',
                           'level': 'Au-delà · convexité et apprentissage',
                           'labs': ['paire'],
                           'objective': 'Relier la distance entre deux convexes à une direction séparatrice.',
                           'task': 'Choisir des ellipsoïdes disjoints et orientés différemment. Comparer '
                                   'leur segment minimal au segment des centres ; examiner le plan médian et '
                                   'la marge affichée. Faire ensuite se recouvrir les solides.',
                           'success': 'Expliquer la disparition d’une séparation stricte et distinguer '
                                      'distance des solides et distance des surfaces.',
                           'limits': 'Fonctions support, dualité convexe et SVM à marge maximale sont des '
                                     'prolongements ; les calculs de Cauchy–Schwarz restent le point '
                                     'd’entrée.'}]}],
 'sources': [{'label': 'Programme officiel de mathématiques MPSI',
              'url': 'https://prepas.org/ups.php?document=69'},
             {'label': 'Programme officiel de mathématiques MP',
              'url': 'https://prepas.org/ups.php?document=85'}],
 'document_url': 'https://github.com/ar742/Python-maths-CPGE/blob/main/optimisation_distances/PARCOURS_PROGRESSIF.md'}

LAB_LINKS = [{'id': 'approximation', 'title': 'Approcher cosinus, choisir une norme', 'href': '/?tp=approximation'},
 {'id': 'matrices', 'title': 'Projeter une matrice, optimiser une distance', 'href': '/?tp=matrices'},
 {'id': 'produit', 'title': 'De la sphère à l’ellipsoïde', 'href': '/?tp=produit'},
 {'id': 'point', 'title': 'Les points les plus proches et les plus éloignés', 'href': '/?tp=point'},
 {'id': 'paire', 'title': 'La distance entre deux ellipsoïdes', 'href': '/?tp=paire'}]
