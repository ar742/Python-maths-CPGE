"""Buts, variables et premières manipulations des neuf laboratoires quantiques."""
from cours import LESSONS


def guide(intro,objects,assumptions,techniques,steps,sup,spe,beyond,expected):
    return dict(intro=intro,purpose=intro,objects=objects,assumptions=assumptions,
                techniques=techniques,first_steps=steps,levels=dict(sup=sup,spe=spe,beyond=beyond),
                expected=expected,lesson_numbers=[])


LAB_GUIDES={
 'boite':guide(
    'L est le côté du cube et nₓ, nᵧ, n_z les indices des modes. Chercher comment le confinement fixe les énergies, puis superposer deux modes et suivre leur densité de probabilité. Comparer des parois infinies aux conditions périodiques : elles décrivent deux problèmes différents.',
    ['L en nm ; électron de masse mₑ ; x/L est une position sans dimension.','nₓ, nᵧ, n_z sont des entiers ; les parois imposent des indices strictement positifs.','w est le poids du second mode ; δ sa phase initiale en degrés ; τ=tE_L/ℏ le temps réduit.'],
    ['Une particule sans spin, libre dans le cube ; chaque choix de bord fixe ses modes et son échelle E_L.','Le second mode remplace nₓ par nₓ+1. La carte intègre z : elle représente une probabilité marginale en x,y.'],
    ['Séparer les variables et appliquer les conditions aux limites.','Normaliser une fonction d’onde et additionner des amplitudes.','Identifier une dégénérescence et calculer une fréquence de battement.'],
    ['Choisir le fondamental, puis doubler L : prévoir le rapport des énergies.','Choisir nₓ=2, nᵧ=n_z=1 et retrouver les modes de même énergie.','Passer à w=1/2 et modifier le temps : comparer densité locale et énergie moyenne.'],
    'Entrée Sup : ondes, probabilités et unités ; préparation au confinement.',
    'MP §6 et PC §6.5 : puits infini et superposition ; le cube prolonge le problème unidimensionnel.',
    'Normalisation périodique et comptage tridimensionnel des états : prolongements accompagnés.',
    'Une énergie de confinement justifiée et une densité variable sans variation de l’énergie moyenne.'),
 'heisenberg':guide(
    'Δx et Δp sont les écarts types de position et d’impulsion. Avec un paquet gaussien, observer leur produit et l’étalement libre. Dans la fente, étudier plutôt les zéros de diffraction. Les estimations d’énergie relient ces deux descriptions aux échelles de la boîte, de l’atome et de l’oscillateur.',
    ['σ : largeur initiale ; p₀ : impulsion moyenne ; c : coefficient de phase quadratique.','Paquet et estimations en unités réduites ℏ=m=1 ; t et ω sont le temps et la pulsation dans ces unités.','Fente : a en µm, longueur d’onde λ en nm ; Δx est un écart type, pas toute la largeur a.'],
    ['Évolution libre d’un paquet gaussien normalisé.','Fente rectangulaire idéale en champ lointain ; ses bords abrupts rendent le second moment d’impulsion divergent.'],
    ['Calculer des moments et des écarts types.','Lire une transformée de Fourier et contrôler une approximation angulaire.','Minimiser une borne d’énergie en respectant son statut.'],
    ['Prendre c=0,t=0 et comparer ΔxΔp à ℏ/2.','Augmenter t, puis essayer c<0 : observer étalement ou contraction initiale.','Choisir la fente et réduire a ; comparer le premier zéro au produit d’écarts types du paquet.'],
    'Entrée Sup : diffraction, dimensions et ordres de grandeur quantiques.',
    'MP §6 et PC §6.5 : confinement et Heisenberg ; PC introduit le paquet d’ondes, MP le traite ici en prolongement.',
    'Covariance, phase quadratique et estimation variationnelle de l’atome : approfondissements.',
    'Une largeur de diffraction distinguée d’un écart type et une estimation d’énergie accompagnée de ses hypothèses.'),
 'diffusion':guide(
    'E est l’énergie incidente, V₀ la hauteur du potentiel et a la largeur de la barrière. Raccorder la fonction d’onde ψ et sa dérivée ψ′, puis comparer les flux réfléchi et transmis. La marche semi-infinie et la barrière finie permettent de distinguer pénétration évanescente et transmission tunnel.',
    ['E,V₀,a : grandeurs réduites, avec ℏ=m=1 ; x : position.','R et T : probabilités obtenues par les rapports de courants, sans unité.','ψ′ est la dérivée spatiale de ψ ; une amplitude transmise n’est pas à elle seule un rapport de flux.'],
    ['Potentiel réel constant par morceaux, masse identique dans toutes les régions.','Onde incidente depuis la gauche ; états stationnaires ; pas d’absorption.'],
    ['Résoudre une équation différentielle du second ordre.','Appliquer deux raccordements à chaque interface.','Vérifier la conservation R+T=1 et des cas limites.'],
    ['Comparer E<V₀ sur la marche et sur la barrière : prévoir T dans chaque cas.','Sur la barrière, augmenter a et suivre la diminution de T.','Choisir E>V₀ et rechercher une résonance de transmission, puis vérifier R+T.'],
    'Entrée Sup : raccordement d’ondes et conservation d’un flux.',
    'MP §6.3 et PC §6.5 : potentiels constants par morceaux et effet tunnel.',
    'Paquets incidents, barrières multiples et temps de traversée : au-delà du modèle stationnaire.',
    'Des coefficients définis par les courants et une explication de T=0 sur une marche malgré une densité à droite.'),
 'oscillateur':guide(
    'n est le niveau d’un oscillateur quantique ; α est l’amplitude complexe d’un état cohérent. Comparer un état propre stationnaire à un paquet dont la position moyenne oscille. Relier nœuds, énergie et largeur, puis retrouver la dynamique classique des moyennes.',
    ['Position X=x/ℓ avec ℓ=√(ℏ/(mω)) ; temps réduit ωt ; énergies en ℏω.','n entier positif ou nul ; |α| et sa phase fixent le paquet cohérent.','ψ est l’amplitude de probabilité ; |ψ|² sa densité ; Δx et Δp sont les écarts types.'],
    ['Potentiel harmonique idéal ; état propre ou état cohérent normalisé.','Aucun amortissement ni anharmonicité ; une densité spatiale n’est pas une trajectoire.'],
    ['Étudier parité et zéros des polynômes d’Hermite.','Calculer des moments et des commutateurs.','Comparer une équation sur les moyennes à l’équation classique.'],
    ['Comparer n=0,1,3 : compter les nœuds et prévoir les énergies.','Choisir un état cohérent et suivre un cycle en temps réduit.','Faire varier |α| : comparer déplacement moyen, largeur et énergie.'],
    'Entrée Sup : oscillateur classique, gaussienne et énergie minimale.',
    'Outils Spé : équations différentielles, Hermite et opérateurs ; résolution quantique comme prolongement de MP/PC.',
    'États cohérents et construction complète par opérateurs : approfondissements guidés.',
    'Une distinction entre état propre d’énergie et paquet oscillant, avec le rôle de l’énergie de point zéro.'),
 'intrication':guide(
    'A et B désignent deux photons ; a,a′ et b,b′ sont les angles de leurs analyseurs. Comparer une paire de Bell à un mélange de polarisations classiques. Calculer les probabilités conjointes et les probabilités locales, puis tester la combinaison de corrélations appelée CHSH.',
    ['Angles en degrés ; v est le poids de la préparation avant ajout de bruit blanc.','ρ est la matrice densité de la paire ; E(a,b) la moyenne du produit des résultats ±1.','S est la valeur absolue de la combinaison CHSH ; les probabilités locales sont les sommes des issues conjointes.'],
    ['Analyseurs de polarisation linéaire idéaux ; état de Bell Φ⁺ ou mélange HH/VV.','La borne S≤2 concerne des modèles locaux à résultats prédéterminés ; le bruit est explicitement modélisé.'],
    ['Calculer des probabilités et leurs sommes marginales.','Changer de base de mesure.','Distinguer intrication et violation d’une inégalité avec des réglages donnés.'],
    ['Avec les angles optimaux et v=1, comparer S à 2.','Passer au mélange classique sans changer les angles.','Réduire v et comparer les deux seuils : intrication et violation CHSH.'],
    'Entrée Sup : probabilités conjointes, conditionnelles et corrélations.',
    'Outils Spé : matrices, produits tensoriels et valeurs propres ; ce sujet est un prolongement de MP/PC.',
    'Tests de Bell, états mixtes et critères de séparabilité : au-delà du socle CPGE cité.',
    'Une corrélation expliquée dans plusieurs bases et des probabilités locales indépendantes du réglage distant.'),
 'josephson':guide(
    'V est la tension d’une jonction et δ sa différence de phase ; Φ est le flux traversant une boucle SQUID. Étudier d’abord un courant commandé par la phase, puis l’interférence de deux jonctions. Relier une tension à une fréquence et un flux au courant critique maximal.',
    ['I₁,I₂ : courants critiques en µA ; V en µV ; δ en degrés dans le curseur.','Φ/Φ₀ : flux réduit ; Φ₀=h/(2e) en Wb ; h est la constante de Planck et e la charge élémentaire positive.','Le courant critique d’un SQUID est le maximum du courant à flux fixé.'],
    ['Relations Josephson sinusoïdales ; deux jonctions idéales pour le SQUID.','Inductance de boucle négligée ; la tension de sortie d’un appareil réel n’est pas modélisée.'],
    ['Résoudre une équation de phase.','Maximiser A sinδ+B cosδ.','Utiliser périodicité et symétrie pour prévoir des extrema.'],
    ['Choisir une jonction et comparer V=0 à V=1 µV.','Dans le SQUID symétrique, comparer flux 0 et 1/2.','Rendre I₁ et I₂ différents et prévoir le minimum résiduel.'],
    'Entrée Sup : sinusoïdes, phase, flux et unités.',
    'Outils Spé : interférences, dérivation et optimisation ; Josephson/SQUID sont des prolongements de MP/PC.',
    'Supraconductivité macroscopique, polarisation et dissipation d’un SQUID réel.',
    'Une modulation de période Φ₀ et un minimum lié à l’asymétrie des jonctions.'),
 'rabi':guide(
    'Ω est le couplage d’un système à deux niveaux et Δ le désaccord entre excitation et transition. Faire varier le temps pour piloter une population, puis comparer une impulsion résonante à une excitation désaccordée. L’exemple RMN donne séparément les fréquences physiques d’un proton.',
    ['Ω,Δ,t sont les paramètres réduits de l’évolution ; Ωt est un angle sans unité.','B₀ en T : champ statique ; B₁ en µT : amplitude du champ transverse circulaire.','P₁ est la probabilité d’excitation ; γ est le rapport gyromagnétique du proton.'],
    ['Deux niveaux idéaux, état initial |0⟩ et champ circulaire dans le repère tournant.','Pas de relaxation ; les curseurs réduits ne sont pas déduits automatiquement des champs RMN.'],
    ['Exponentier une matrice à l’aide des matrices de Pauli.','Lire amplitude, fréquence et phase d’une oscillation.','Relier durée d’impulsion et rotation.'],
    ['Choisir Δ=0 et l’impulsion π : prévoir P₁.','Choisir l’impulsion π/2 puis comparer populations et phase de l’état.','Augmenter |Δ| : suivre la baisse de l’amplitude maximale.'],
    'Entrée Sup : résonance, oscillations et ordres de grandeur de fréquences.',
    'Outils Spé : repère tournant et matrices ; les rotations quantiques sont un prolongement de MP/PC.',
    'RMN avec relaxation, distributions de fréquences et impulsions façonnées.',
    'Une durée de commande reliée au couplage, et un désaccord qui empêche une inversion complète.'),
 'bloch':guide(
    'Un qubit est un système à deux niveaux. Les angles θ,φ donnent la direction de son vecteur de Bloch et r sa longueur. Appliquer une porte puis choisir un axe de mesure : comparer l’évolution de l’état à la probabilité obtenue, y compris pour un état mélangé.',
    ['θ : colatitude ; φ : azimut ; α : angle de rotation ; curseurs en degrés.','r entre 0 et 1 : longueur du vecteur ; la pureté vaut Tr(ρ²), distincte de r.','ρ : matrice densité ; l’axe de mesure est un vecteur unitaire.'],
    ['Un seul qubit ; portes unitaires idéales et mesure projective.','Un état pur est sur la sphère ; un état mélangé est à l’intérieur.'],
    ['Passer entre coordonnées sphériques et cartésiennes.','Appliquer une matrice unitaire.','Calculer une probabilité avec un produit scalaire.'],
    ['Comparer |0⟩ et |+⟩ avec une mesure suivant Z.','Appliquer Hadamard à |0⟩ puis tourner l’axe de mesure.','Prendre r=0 : vérifier que toutes les mesures donnent 1/2.'],
    'Entrée Sup : géométrie dans l’espace et probabilités.',
    'Outils Spé : matrices hermitiennes et rotations ; le qubit est un prolongement du socle MP/PC.',
    'Canaux quantiques, décohérence et systèmes à plusieurs qubits.',
    'Une probabilité calculée à partir de l’état et de l’axe, avec une pureté conservée par les portes.'),
 'circuits':guide(
    'La base |00⟩,|01⟩,|10⟩,|11⟩ décrit deux qubits. Suivre leurs amplitudes dans une préparation de Bell, puis dans une recherche de Grover parmi quatre états. Comparer une mesure finale aux transformations qui l’ont précédée.',
    ['m entre 0 et 3 : indice de la cible ; k : nombre d’itérations de Grover.','H : porte de Hadamard ; CNOT : inversion du second qubit commandée par le premier.','Une amplitude peut être négative ; sa probabilité est le carré de son module.'],
    ['Simulation exacte de deux qubits ; portes, oracle et mesure idéaux.','Un élément marqué ; aucun bruit et aucune mesure intermédiaire.'],
    ['Multiplier des matrices dans l’ordre du circuit.','Conserver la somme des probabilités.','Interpréter une réflexion des amplitudes autour de leur moyenne.'],
    ['Préparer Bell et identifier les deux issues de mesure possibles.','Choisir Grover avec k=0 puis k=1 : comparer la probabilité de la cible.','Ajouter une seconde itération et expliquer pourquoi le succès diminue.'],
    'Entrée Sup : vecteurs, probabilités et composition d’opérations.',
    'Outils Spé : algèbre linéaire et produits tensoriels ; circuits quantiques hors du socle MP/PC.',
    'Complexité en nombre de requêtes, construction d’un oracle et processeurs quantiques.',
    'Des amplitudes suivies jusqu’à la mesure, sans assimiler une itération supplémentaire à un progrès garanti.')
}
for lab,g in LAB_GUIDES.items():
    g['lesson_numbers']=[i+1 for i,l in enumerate(LESSONS) if l['lab']==lab]

LAB_OBJECTS = {'boite': ['L est le côté du cube en nm et mₑ la masse de l’électron ; x/L est une position réduite. '
           'ℏ=h/(2π), où h est la constante de Planck.',
           'nₓ,nᵧ,n_z identifient les modes ; les parois imposent des indices entiers strictement '
           'positifs. E_L est l’échelle d’énergie du mode unidimensionnel.',
           'w est le poids du second mode et δ sa phase initiale en degrés ; τ=tE_L/ℏ est le temps réduit. '
           'La densité |ψ|² se déduit de la fonction d’onde ψ.'],
 'heisenberg': ['σ est l’écart type initial de position, p₀ l’impulsion moyenne et c le coefficient de '
                'phase quadratique. Δx et Δp sont les écarts types de position et d’impulsion.',
                'm est la masse et ℏ la constante de Planck réduite ; les unités sont choisies pour ℏ=m=1. '
                't est le temps et ω la pulsation dans ces unités.',
                'Pour la fente, a est sa largeur en µm et λ la longueur d’onde en nm ; la largeur a '
                'diffère d’un écart type.'],
 'diffusion': ['E est l’énergie incidente, V₀ la hauteur du potentiel et a la largeur de barrière ; x est '
               'la position. m est la masse et ℏ la constante de Planck réduite ; les unités donnent '
               'ℏ=m=1.',
               'ψ est la fonction d’onde et ψ′ sa dérivée spatiale ; les raccordements portent sur ces '
               'deux fonctions.',
               'R et T sont les rapports de courants réfléchi et transmis à l’incident, sans dimension ; '
               'une amplitude de ψ ne suffit pas à donner T.'],
 'oscillateur': ['m est la masse, ω la pulsation et ℏ la constante de Planck réduite. ℓ=√(ℏ/(mω)) est une '
                 'longueur ; X=x/ℓ est la position réduite et ωt le temps réduit.',
                 'n≥0 compte les excitations ; α est l’amplitude complexe d’un état cohérent, réglée par '
                 'son module et sa phase. L’énergie est mesurée en ℏω.',
                 'ψ est la fonction d’onde, |ψ|² sa densité de probabilité ; Δx et Δp sont les écarts '
                 'types de position et d’impulsion.'],
 'intrication': ['a,a′ règlent les orientations de l’analyseur A ; b,b′ celles de B, en degrés. Les '
                 'résultats de chaque mesure sont ±1.',
                 'v∈[0,1] est le poids de Bell dans le mélange avec le bruit blanc ; l’autre préparation '
                 'est un mélange de polarisations horizontales et verticales.',
                 'E(a,b) est la moyenne du produit des résultats ; S est la combinaison CHSH de quatre '
                 'corrélations. Les probabilités marginales concernent un seul analyseur.'],
 'josephson': ['I₁,I₂ sont les courants critiques en µA ; V est la tension en µV et δ la différence de '
               'phase en degrés.',
               'Φ est le flux dans la boucle et Φ₀=h/(2e) son quantum, en Wb ; h est la constante de '
               'Planck et e la charge élémentaire. Le curseur règle Φ/Φ₀.',
               'I_c(Φ) est le courant maximal du SQUID à flux fixé ; f_J est la fréquence du courant '
               'alternatif d’une jonction sous tension.'],
 'rabi': ['Ω est le couplage, Δ le désaccord et t le temps en unités réduites ; Ω_R=√(Ω²+Δ²) est la '
          'pulsation de Rabi.',
          'B₀ est le champ statique en T, B₁ l’amplitude circulaire en µT ; γ est le rapport '
          'gyromagnétique du proton. Ces réglages donnent des repères physiques séparés des curseurs '
          'réduits.',
          'P₁ est la probabilité du niveau |1⟩ et r le vecteur de Bloch ; l’état initial est |0⟩. Une '
          'impulsion π inverse les populations à résonance.'],
 'bloch': ['θ est la colatitude et φ l’azimut, en degrés ; r∈[0,1] est la longueur du vecteur de Bloch. La '
           'pureté de l’état est (1+r²)/2.',
           'ρ est la matrice densité ; X,Y,Z sont les matrices de Pauli. Les portes Rx,Ry,Rz sont des '
           'rotations d’angle α en degrés.',
           'L’axe de mesure est défini par sa colatitude et son azimut ; les probabilités concernent les '
           'deux résultats ±1.'],
 'circuits': ['Les quatre états de base sont |00⟩,|01⟩,|10⟩,|11⟩ ; le premier qubit est celui de gauche. '
              'Une amplitude complexe au carré en module donne une probabilité.',
              'H est la porte de Hadamard ; CNOT inverse la cible si le contrôle vaut 1. Une paire de Bell '
              'est une superposition intriquée de deux états.',
              'm=0,1,2,3 est l’indice de la cible marquée ; k est le nombre d’itérations de Grover. '
              'L’oracle inverse le signe de l’amplitude ciblée.']}
for _lab, _objects in LAB_OBJECTS.items():
    LAB_GUIDES[_lab]["objects"] = _objects

LAB_PURPOSES = {'boite': 'Expliquer la quantification par les conditions aux limites, puis observer le battement de deux '
          'modes.',
 'heisenberg': 'Distinguer un écart type d’une largeur de diffraction et utiliser Heisenberg pour estimer '
               'une énergie minimale.',
 'diffusion': 'Raccorder les fonctions d’onde, puis expliquer réflexion et transmission avec les courants '
              'de probabilité.',
 'oscillateur': 'Relier le spectre à ses états propres et comparer le mouvement moyen d’un état cohérent '
                'au mouvement classique.',
 'intrication': 'Comparer corrélations quantiques et classiques sans confondre probabilités conjointes et '
                'probabilités marginales.',
 'josephson': 'Prévoir la fréquence d’une jonction sous tension et la modulation du courant critique d’une '
              'boucle à deux jonctions.',
 'rabi': 'Choisir une impulsion qui réalise une transition et expliquer la baisse de sa probabilité hors '
         'résonance.',
 'bloch': 'Représenter un état, une transformation et une mesure avec des vecteurs, puis relier géométrie '
          'et probabilités.',
 'circuits': 'Suivre les amplitudes d’un circuit à deux qubits et expliquer pourquoi une itération de '
             'Grover retrouve la cible.'}
for _lab, _purpose in LAB_PURPOSES.items():
    LAB_GUIDES[_lab]["purpose"] = _purpose
    LAB_GUIDES[_lab]["levels"]["sup"] = LAB_GUIDES[_lab]["levels"]["sup"].removeprefix("Entrée Sup : ")
