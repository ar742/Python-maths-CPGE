# Parcours de physique quantique — sept séances CPGE

Ce parcours part des TP et exercices de l’extrait de recueil de A. R., pages imprimées 471–479. Il propose des démarches originales, sans reproduire les fichiers personnels. Chaque séance associe une prédiction écrite, une exploration interactive et une vérification démontrée. Les mentions Sup et Spé décrivent une progression pédagogique ; le programme réglementaire et la profondeur attendue dépendent de la filière. Les extensions sont signalées.

Durée indicative : sept séances de 1 h 30 à 2 h, avec un court travail préparatoire. Aucun appareil ou compte externe n’est nécessaire. L’application Python fonctionne localement ; les calculs numériques illustrent les modèles, ils ne remplacent pas les preuves.

## 1. Construire un état dans un cube

**Objectif Sup → Spé :** relier équation différentielle, conditions aux limites, normalisation et niveaux d’énergie.

**Avant le laboratoire :** résoudre X″+k²X=0 avec X(0)=X(L)=0 ; normaliser le mode fondamental. Vérifier les dimensions de ψ et de E₀. Écrire les trois premiers niveaux et compter les états spatiaux, sans inclure le spin.

**Exploration :** dans « Boîte cubique », comparer (1,1,1), (2,1,1) et (2,2,1), puis doubler L. Relier la carte marginale en (x,y), qui intègre z, à la marginale en x ; expliquer à l’écrit ce qui les distingue d’une coupe à z fixé. Passer aux conditions périodiques et expliquer pourquoi le mode nul apparaît. Revenir aux parois, superposer (1,1,1) et (2,1,1) à poids égaux et varier phase et temps.

**À démontrer :** E=π²ℏ²(nx²+ny²+nz²)/(2mL²), la dégénérescence 3 du second niveau et la période des battements 2πℏ/(3E₀). Montrer que l’énergie moyenne et la norme restent constantes pendant que la densité locale change.

**Contrôle :** exercices 1 à 4. Un compte rendu réussi distingue état propre, superposition cohérente et mélange statistique ; il explique pourquoi l’égalité des dérivées aux faces opposées n’est pas une condition de puits infini.

## 2. Transformer l’incertitude en outil de calcul

**Objectif Sup → Spé :** utiliser une inégalité précise sans confondre écart type et largeur caractéristique.

**Avant le laboratoire :** établir ΔxΔp≥ℏ/2 par la positivité de ‖(X+iλP)ψ‖². Calculer les écarts types d’une gaussienne réelle avec une phase linéaire. Vérifier que p₀ change la moyenne, pas la dispersion.

**Exploration :** dans « Heisenberg », suivre l’étalement libre d’une gaussienne. Ajouter une phase quadratique pour voir l’effet d’une covariance initiale. Dans le mode fente, comparer les positions des premiers zéros lorsque largeur et longueur d’onde varient. Dans les estimations, minimiser l’énergie harmonique et celle du modèle d’hydrogène.

**À démontrer :** la borne exacte E₀=ℏω/2 et la largeur de la gaussienne qui l’atteint. Pour l’hydrogène, annoncer p∼ℏ/r comme une estimation ; en extension, calculer l’énergie de la famille ψ_a∝e^{-r/a}. Expliquer pourquoi ⟨r⟩=3a₀/2 ne vaut pas a₀.

**Contrôle :** exercices 5 à 8. Ajouter une question courte sur Young : pourquoi des états d’environnement orthogonaux selon le chemin font-ils disparaître le terme d’interférence ? Ne pas remplacer la largeur du lobe d’une fente idéale par un Δp fini.

## 3. Raccorder des amplitudes, conserver des flux

**Objectif Sup → Spé :** résoudre les classiques marche et barrière, distinguer densité et transmission.

**Avant le laboratoire :** justifier la continuité de ψ et ψ′ pour un potentiel fini et une masse constante. Calculer le courant d’une onde plane. Écrire les deux raccordements d’une marche pour E>V₀.

**Exploration :** dans « Marche et tunnel », varier E/V₀ et observer amplitudes, courants et densités. À V₀=3E/4, vérifier que |t|² dépasse 1 mais T reste inférieur à 1. Comparer une marche semi-infinie E<V₀ à une barrière finie. Élargir la barrière à énergie constante, puis chercher une résonance au-dessus de V₀.

**À démontrer :** R+T=1, le facteur de vitesse T=(k₂/k₁)|t|², T=sech²(κa) pour V₀=2E, la limite continue au seuil E=V₀ et la condition qa=ℓπ pour une transmission parfaite.

**Contrôle :** exercices 9 à 12. Le rapport final doit expliquer pourquoi une densité évanescente non nulle ne suffit pas à produire un flux transmis ; les unités réduites ℏ=m=1 doivent être distinguées des unités SI.

## 4. L’oscillateur comme pont vers le classique

**Objectif Spé :** comparer méthode différentielle et méthode des opérateurs, puis appliquer Ehrenfest.

**Avant le laboratoire :** calculer [a,a†] et H=ℏω(a†a+1/2). Résoudre aψ₀=0 et construire ψ₁. Prévoir parité, nombre de nœuds et énergie des premiers états.

**Exploration :** dans « Oscillateur harmonique », observer les modes n=0,1,2,5. Comparer leur densité à la zone classiquement permise. Passer à l’état cohérent, prendre α=2 et suivre un cycle dans le plan position–impulsion. Comparer la largeur à celle du fondamental.

**À démontrer :** l’échelle Eₙ=ℏω(n+1/2), ΔxΔp=(n+1/2)ℏ et l’évolution α(t)=αe^{-iωt}. Établir les équations d’Ehrenfest et expliquer pourquoi leur fermeture sur les moyennes est exacte pour un potentiel quadratique, mais pas pour un potentiel quelconque.

**Contrôle :** exercices 13 et 14. Extension : dériver la distribution de Poisson des occupations d’un état cohérent. Ne pas appeler état propre d’énergie un paquet qui oscille.

## 5. Distinguer corrélation et intrication

**Objectif Spé, extension guidée :** comprendre le produit tensoriel, les matrices réduites et une inégalité de Bell.

**Avant le laboratoire :** montrer que det C=0 caractérise un état pur séparable de deux qubits. Calculer ρ_A pour Φ⁺, puis comparer Φ⁺ au mélange classique de 00 et 11. Le premier est pur globalement, le second non ; leurs matrices réduites sont identiques.

**Exploration :** dans « Intrication et Bell », comparer les mesures en Z puis en X. Choisir les angles 0°,45°,22,5°,−22,5° et calculer CHSH. Ajouter du bruit de Werner et repérer le seuil de violation. Comparer avec les corrélations du mélange classique et des réglages non optimaux.

**À démontrer :** la borne locale S≤2 et la valeur quantique 2√2. Montrer que les marges restent 1/2, indépendantes de l’angle distant. Distinguer « cet état est intriqué » de « ces réglages violent CHSH ». Le seuil de Werner v>1/3 pour l’intrication est une extension ; le seuil CHSH v>1/√2 découle directement de la corrélation.

**Contrôle :** exercices 15 et 16. Une explication convaincante précise l’état Φ⁺ et les conventions de polarisation ; elle ne le confond pas avec le singulet de deux spins 1/2 et ne propose pas une transmission instantanée de message.

## 6. Deux applications : Josephson/SQUID et RMN/Rabi

**Objectif Spé :** relier phase, couplage, changement de référentiel et observables mesurables. Cette séance peut être divisée en deux séances selon la filière.

**Avant le laboratoire :** dériver la variation des populations d’un modèle à deux amplitudes Josephson, en fixant q=2e et une différence électrochimique qV. Revoir l’exponentielle d’une combinaison de matrices de Pauli et la transformation d’un Hamiltonien en référentiel tournant.

**Exploration :** dans « Josephson et SQUID », comparer V=0 à une tension constante, puis parcourir une période de flux. Déséquilibrer les deux courants critiques et prévoir le minimum résiduel. Dans « RMN et Rabi », comparer résonance et désaccord, puis préparer des impulsions π et π/2. Faire varier séparément B₀ et B₁ dans l’exemple RMN physique.

**À démontrer :** f_J=2e|V|/h, I_c,eff=√(I₁²+I₂²+2I₁I₂cos(2πΦ/Φ₀)), et P₁(t)=Ω²sin²(√(Ω²+Δ²)t/2)/(Ω²+Δ²). Montrer pourquoi un Hamiltonien proportionnel à I ne produit pas une séparation Zeeman.

**Contrôle :** exercices 17 à 21. Toujours déclarer les hypothèses : SQUID de faible inductance ; Rabi sans relaxation ; champ circulaire idéal exact ou champ linéaire avec approximation tournante. Le facteur 2 de l’amplitude circulaire d’un champ linéaire et la charge 2e doivent être explicités.

## 7. Voir et programmer des qubits

**Objectif Spé, extension informatique quantique :** représenter un état, mesurer dans plusieurs bases et composer des portes sans perdre les phases.

**Avant le laboratoire :** calculer les probabilités de |+> et |+i> en Z, X et Y. Relier ρ=(I+r·σ)/2 à Trρ²=(1+|r|²)/2. Écrire H, X et CNOT dans les bases annoncées.

**Exploration :** dans « Sphère de Bloch », appliquer H et plusieurs rotations à un état pur, puis à un état mélangé. Modifier l’axe de mesure. Dans « Circuits », suivre chaque étape de préparation de Bell, puis Grover sur quatre états, avec chacun des états marqués et de zéro à quatre itérations.

**À démontrer :** la préparation de Φ⁺ par H puis CNOT ; le rôle d’une mesure intermédiaire qui détruit la cohérence. Pour Grover, calculer à la main la réflexion des amplitudes autour de leur moyenne et montrer qu’une itération donne une probabilité 1, mais deux redonnent 1/4.

**Contrôle :** exercices 22 à 24. Le bilan doit distinguer un qubit d’un bit, une superposition d’un mélange, une simulation classique d’un processeur quantique et la complexité en appels à un oracle du coût de sa construction.

## Petit oral de synthèse

Choisir un laboratoire et préparer cinq minutes d’explication : hypothèses du modèle, grandeur affichée et unité, prédiction calculée, test réalisé, puis limite de validité. Tirer ensuite une question parmi : « pourquoi T n’est-il pas |t|² ? », « une corrélation parfaite prouve-t-elle l’intrication ? », « où intervient la phase ? », « pourquoi l’énergie fondamentale n’est-elle pas nulle ? », « quand le changement de référentiel est-il exact ? ».

Une bonne réponse ne récite pas seulement une formule : elle sait la justifier, annoncer son domaine d’application et reconnaître ce que le graphe seul ne prouve pas.
