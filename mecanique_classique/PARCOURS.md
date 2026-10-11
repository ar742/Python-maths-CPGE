# Douze séances de mécanique

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le théorème adapté.

## Séance 01 — P1 · Astrophysique

### Kepler : suivre une planète et mesurer les aires balayées

Retrouver les lois de Kepler à partir de deux théorèmes, puis vérifier qu’une ellipse est parcourue à la bonne vitesse.

**Objets et paramètres**

- a : demi-grand axe, en UA (1 UA ≈ 150 millions de km) ; e : excentricité sans dimension, entre 0 et 1.
- M : masse de l’étoile, en masses solaires ; G : constante de gravitation. Le temps est en années.
- r : distance étoile–planète ; v : vitesse ; h : moment cinétique par unité de masse ; ε : énergie mécanique par unité de masse ; T : période ; L : moment cinétique de la planète.

**Repères** — Sup : Énergie mécanique, mouvement circulaire et unités. Spé : Réinvestir les forces centrales de MPSI ; Binet et l’équation des coniques sont fournis en complément. Au-delà : Équation de Kepler et résolution numérique à temps uniforme.

1. Choisir l’orbite presque circulaire et repérer la constance de r et de v.
2. Augmenter e sans changer a : comparer la période et les vitesses extrêmes.
3. Lire les douze aires et les écarts des bilans pour contrôler le mouvement calculé.

**À justifier :** À a et M fixés, T et ε ne changent pas avec e. Les vitesses varient, mais les aires sur des durées égales restent égales.

### Deux étoiles : passer au centre de masse

Choisir le bon système pour appliquer la quantité de mouvement et ramener deux trajectoires à une seule orbite relative.

**Objets et paramètres**

- m₁,m₂ : masses des étoiles ; M=m₁+m₂ : masse totale, en masses solaires ; q=m₂/m₁ : rapport sans dimension.
- G désigne ici le centre de masse ; dans GM, la lettre G désigne la constante de gravitation.
- r₁,r₂ : positions depuis le centre de masse ; r=r₂−r₁ : séparation ; a : demi-grand axe de cette séparation, en UA ; e : excentricité.
- μr=m₁m₂/M : masse réduite ; temps en années.

**Repères** — Sup : Quantité de mouvement, centre de masse et interactions mutuelles. Spé : Réinvestir les bilans ; masse réduite et König général sont des prolongements pour MPSI/MP. Au-delà : Application à la mesure des masses des étoiles binaires.

1. Choisir deux masses égales et comparer leurs deux ellipses.
2. Diminuer q : voir quelle étoile reste proche de G.
3. À masse totale constante, modifier q puis vérifier que la période ne change pas.

**À justifier :** Le rapport des distances à G est inverse du rapport des masses. La période dépend de la masse totale ; la décomposition énergétique utilise la masse réduite.

## Séance 02 — P1 · Astrophysique

### Lancement orbital : lire les points de rebroussement

Lire une trajectoire centrale à partir d’une courbe d’énergie : domaine accessible, rayons extrêmes, stabilité et échappement.

**Objets et paramètres**

- M : masse centrale ; G : constante de gravitation ; r₀ : distance du lancement. Les unités réduites donnent GM=r₀=1.
- η : vitesse tangentielle initiale divisée par la vitesse circulaire ; h : moment cinétique par unité de masse.
- r : distance au centre ; Ueff : énergie gravitationnelle plus énergie angulaire à h fixé ; ε : énergie mécanique par unité de masse.

**Repères** — Sup : Énergie et condition d’accessibilité. Spé : Potentiel effectif et classification des coniques. Au-delà : Petites oscillations radiales et comparaison avec la fréquence orbitale.

1. Choisir η=1 : la droite d’énergie touche le minimum du potentiel.
2. Choisir η=1,2 puis repérer les deux rayons extrêmes.
3. Passer à η=1,6 : constater l’absence de rayon maximal et ε>0.

**À justifier :** Une vitesse inférieure à la vitesse circulaire commence à l’apocentre. L’échappement exige η≥√2 ; une énergie négative donne une orbite bornée.

### Rejoindre une autre orbite : deux impulsions de Hohmann

Calculer les deux impulsions nécessaires pour changer d’orbite, puis comparer leur coût en vitesse et le temps de trajet.

**Objets et paramètres**

- L₀ : unité de longueur (7 000 km autour de la Terre, 1 UA autour du Soleil) ; r₁,r₂ : rayons des orbites.
- G : constante de gravitation ; M : masse de l’astre ; a : demi-grand axe de l’ellipse de transfert.
- Δv₁,Δv₂ : changements tangentiels signés de vitesse, en km/s ; |Δv₁|+|Δv₂| : coût total ; τ : durée de la demi-ellipse, affichée en h ou en jours.

**Repères** — Sup : Vitesse circulaire, énergie et ordres de grandeur. Spé : Application accompagnée des bilans d’énergie aux coniques et aux changements de vitesse. Au-delà : Fenêtres de transfert interplanétaire et limites de l’optimalité.

1. Choisir un transfert terrestre vers une orbite haute : identifier les deux tangences.
2. Inverser les deux rayons : vérifier le signe des impulsions et le même coût total.
3. Choisir Soleil : calculer la durée en jours puis comparer à l’ordre de grandeur d’un trajet vers Mars.

**À justifier :** Une ellipse seule ne remplace pas les deux impulsions : sans l’impulsion finale, le véhicule repasse par son orbite initiale.

## Séance 03 — P1 · Astrophysique

### Survol gravitationnel : dévier sans moteur

Comprendre une assistance gravitationnelle en séparant le calcul dans le référentiel de l’astre et la composition des vitesses.

**Objets et paramètres**

- G : constante de gravitation ; M : masse de l’astre. Les longueurs, vitesses et temps sont réduits pour avoir GM=1.
- v∞ : vitesse relative loin de l’astre ; b : distance de l’astre à la droite que suivrait la sonde sans attraction.
- δ : angle de déviation ; rp : distance minimale ; V : vitesse de l’astre dans le second référentiel galiléen.

**Repères** — Sup : Conservation de l’énergie et composition des vitesses. Spé : Application accompagnée : hyperbole gravitationnelle, puis composition des vitesses. Au-delà : Gain ou perte d’énergie lors d’une assistance gravitationnelle.

1. À v∞ fixé, réduire b et comparer δ et rp.
2. Mettre V=0 : le gain lointain doit disparaître.
3. Restaurer V puis inverser l’orientation du survol : comparer les gains signés.

**À justifier :** La gravitation conserve l’énergie dans le référentiel de l’astre, mais la déviation peut modifier l’énergie cinétique dans un autre référentiel.

### Marées : comparer attraction et différence d’attraction

Passer du champ gravitationnel total à sa variation sur un corps, puis contrôler un développement limité par comparaison au champ exact.

**Objets et paramètres**

- m,R : masse et rayon du corps, pris égaux à 1 ; M : masse de l’astre extérieur ; D : distance entre les centres.
- q=M/m et D/R sont sans dimension ; les accélérations sont rapportées à la gravité à la surface du corps.
- Δa : accélération d’un point moins celle du centre ; x : position suivant l’axe dirigé vers l’astre.

**Repères** — Sup : Gravitation, différences de forces et analyse dimensionnelle. Spé : Développement limité d’un champ ; étirement et compression. Au-delà : Matrice du champ de marée, trace nulle et ordre de grandeur d’une dislocation.

1. Choisir le cas lointain et vérifier que champ exact et approximation se superposent.
2. Rapprocher l’astre : suivre l’écart sur la face proche.
3. Comparer les composantes radiale et transverse : leurs signes et leurs coefficients sont différents.

**À justifier :** La marée varie comme D⁻³ et possède un effet sur les deux faces du corps. Le dessin montre un champ, pas une forme d’équilibre.

## Séance 04 — P1 · Bilans et référentiels

### Fusée : faire le bilan d’un système qui perd de la masse

Établir une équation de mouvement quand la masse varie, en indiquant explicitement la vitesse de la matière échangée.

**Objets et paramètres**

- m₀,mf : masses initiale et finale, en tonnes ; χ=m₀/mf : rapport sans dimension ; m(t) : masse restante.
- u : vitesse d’éjection relative à la fusée, en m/s ; q : débit de masse éjectée, positif et constant.
- t : temps ; τ : durée de poussée, en s ; g : pesanteur en m/s² ; v : vitesse verticale en m/s.

**Repères** — Sup : Bilan de quantité de mouvement et logarithme. Spé : Bilans avec matière échangée, selon la filière ; fusée présentée comme application accompagnée. Au-delà : Compromis entre poussée, durée et masse de carburant.

1. Choisir g=0 et vérifier le gain u ln(m₀/mf).
2. Ajouter la pesanteur : comparer les deux courbes de vitesse.
3. Diviser la durée par deux à rapport de masses inchangé : comparer la perte gτ et la poussée.

**À justifier :** Le débit fixe la poussée ; le rapport des masses fixe le gain idéal. Une masse initiale plus grande, à même rapport et durée, donne la même vitesse finale.

### Référentiel tournant : une droite peut devenir une courbe

Reconstruire un mouvement simple dans des axes tournants et vérifier les signes des deux forces d’inertie.

**Objets et paramètres**

- Ω : vitesse angulaire signée des axes autour de z, en rad/s ; t : temps en s.
- v₀ : vitesse constante suivant x dans le référentiel galiléen, en m/s ; vR : vitesse dans les axes tournants.
- (x₀,y₀) : position initiale, en m ; les deux origines coïncident.

**Repères** — Sup : Mouvement rectiligne uniforme et changement de coordonnées. Spé : Référentiel non galiléen, Coriolis et force centrifuge. Au-delà : Invariant énergétique J dans une rotation uniforme.

1. Choisir Ω=0 : retrouver une droite à vitesse constante.
2. Activer une rotation positive : lire séparément les deux termes d’inertie.
3. Changer Ω en −Ω et vérifier les sens puis l’identité des deux courbes de distance.

**À justifier :** La trajectoire courbe appartient aux coordonnées tournantes. Coriolis dépend de la vitesse relative et ne travaille pas ; la force centrifuge seule ne suffit pas.

## Séance 05 — P2 · Oscillateurs

### Une chaîne : modes propres, propagation et dispersion

Écrire le bilan des forces d’une masse, reconnaître un mode propre, puis retrouver l’équation des ondes aux grandes longueurs d’onde.

**Objets et paramètres**

- N : nombre de masses ; j=0,…,N−1 : indice, repris modulo N ; m : masse en kg ; k : raideur en N/m.
- a : espacement au repos, en m ; uⱼ : déplacement en m ; ja+uⱼ : position ; A : déplacement de référence en m.
- q : indice du mode, repris modulo N ; κ=2πq/(Na) : nombre d’onde en rad/m ; ω : pulsation en rad/s.
- Une onde stationnaire est lâchée sans vitesse ; une onde progressive nécessite des vitesses initiales adaptées.

**Repères** — Sup : Écrire l’équation d’une masse et vérifier qu’une préparation uniforme ne déforme aucun ressort. Spé : Calculer les modes, la dispersion et le passage à l’équation d’onde ; relier cette étude à l’exercice 2 du PDF. Au-delà : Vitesse de groupe, déformation d’une impulsion et mécanique harmonique des réseaux cristallins.

1. Choisir « Grande longueur d’onde » et comparer la chaîne exacte à la droite c|κ|.
2. Choisir « Mode alterné » : observer deux masses voisines puis expliquer la pulsation maximale.
3. Choisir « Impulsion locale » et comparer la propagation à la conservation de l’énergie.

**À justifier :** Savoir distinguer une fréquence propre de la fréquence d’une excitation quelconque et justifier la condition |κa|≪1 pour le modèle continu.

### CO₂ : trois masses, deux vibrations et une translation

Identifier les deux vibrations longitudinales de CO₂ et expliquer pourquoi on doit tenir compte des masses avant de diagonaliser.

**Objets et paramètres**

- mO,mC : masses des oxygènes et du carbone, réglées en u (unité de masse atomique) ; k : raideur d’une liaison, en N/m.
- X=(x₁,x₂,x₃) : déplacements longitudinaux depuis l’équilibre, en pm (picomètres) ; temps en fs (femtosecondes).
- M : matrice des masses ; K : matrice des raideurs ; a : vecteur d’un mode ; ω : sa pulsation. Le problème est Ka=ω²Ma.
- c : vitesse de la lumière ; ω/(2πc), après conversion des longueurs, donne le nombre d’onde spectroscopique en cm⁻¹.

**Repères** — Sup : Observer les deux formes et retrouver qualitativement quel atome peut rester immobile. Spé : Résoudre les modes et démontrer l’orthogonalité pour aᵀMb ; prolongement de l’exercice 3 du PDF. Au-delà : Effets isotopiques et lien avec la spectroscopie ; les intensités infrarouges et Raman demandent d’autres grandeurs.

1. Choisir le mode avec carbone immobile ; vérifier le centre de masse.
2. Choisir le mode avec carbone mobile ; comparer son amplitude aux deux oxygènes.
3. Passer de carbone 12 à carbone 13 : quelle fréquence change et pourquoi ?

**À justifier :** Expliquer les deux pulsations sans confondre masse, raideur et normalisation des vecteurs propres.

## Séance 06 — P2 · Oscillateurs

### Foucault : oscillation rapide, précession lente

Relier la force de Coriolis à la précession du plan d’oscillation et distinguer les secondes des heures.

**Objets et paramètres**

- L : longueur en m ; A : déplacement horizontal initial en m ; λ : latitude en degrés, positive au nord.
- g : pesanteur en m/s² ; ΩTerre : vitesse angulaire terrestre ; Ω=ΩTerre sinλ : sa composante verticale ; ω₀=√(g/L) : pulsation propre, en rad/s.
- T₀=2π/ω₀ : période des petits angles, en s ; z=x+iy regroupe les déplacements horizontaux. Le petit angle est de l’ordre de A/L.
- La durée globale est en heures ; les trois traces sont des enregistrements courts à des heures différentes.

**Repères** — Sup : Comparer T₀ et la durée de précession puis observer le signe de la rotation selon l’hémisphère. Spé : Écrire Coriolis, résoudre l’équation complexe et contrôler les conditions initiales ; exercice 6 du PDF. Au-delà : Corrections d’un pendule sphérique, dissipation et précision d’une mesure géophysique.

1. Choisir le Panthéon et comparer les périodes en secondes et en heures.
2. Mettre la latitude à 0° : justifier la disparition de la précession.
3. Passer à une latitude négative ; expliquer le changement de signe à partir du PFD.

**À justifier :** Distinguer le facteur qui tourne la direction et celui qui décrit l’oscillation rapide, sans supprimer les conditions initiales.

### Pendule : mesurer la période sans petit angle

Retrouver la période du pendule à partir de l’énergie, puis mesurer la limite de l’approximation de petit angle.

**Objets et paramètres**

- θ : angle depuis la verticale descendante ; θₘ : angle du lâcher sans vitesse, réglé en degrés puis converti en radians.
- L : longueur en m ; g=9,81 m/s² ; la masse se simplifie dans l’équation.
- T : période exacte issue de l’énergie ; T₀=2π√(L/g) : période des petits angles, en s.
- L’énergie par unité de masse vaut ½L²θ̇²+gL(1−cosθ), en J/kg.

**Repères** — Sup : Équation et énergie du pendule, modèle harmonique, radians et dimensions. Spé : Intégrale de période et développement en amplitude ; contrôle d’un modèle au-delà de sa linéarisation. Au-delà : Intégrale elliptique, divergence logarithmique près du sommet et géométrie de la séparatrice.

1. Choisir 10° et comparer exact et harmonique sur plusieurs oscillations.
2. Passer à 90° puis comparer T exact, T₀ et la mesure sur la trajectoire.
3. Choisir 165° ; repérer les longs ralentissements près des angles extrêmes et vérifier la liaison supposée.

**À justifier :** Dire quelles hypothèses rendent la période indépendante de l’amplitude, et séparer erreur de modèle et erreur numérique.

## Séance 07 — P2 · Oscillateurs

### Anharmonicité : période corrigée et troisième harmonique

Donner un sens observable au développement limité d’ordre 4 : une période corrigée et une troisième harmonique.

**Objets et paramètres**

- θ(t) : angle au temps t ; θₘ : angle maximal, réglé en degrés puis converti en radians ; L : longueur en m ; g : pesanteur en m/s².
- ω₀=√(g/L) : pulsation propre en rad/s ; T₀=2π/ω₀ : période des petits angles ; T : période exacte, en s.
- Le potentiel tronqué conserve θ² et θ⁴ ; sa dérivée donne un rappel en θ et θ³.
- Une harmonique de rang j oscille j fois par période ; A₁ et A₃ sont les amplitudes des rangs 1 et 3, en radians. Le spectre est mesuré sur quatre périodes exactes.

**Repères** — Sup : Retrouver le terme cubique de la force et prévoir un rappel plus faible que le rappel linéaire. Spé : Comparer T≈T₀(1+θₘ²/16) et les harmoniques ; priorité à l’exercice 7 du PDF. Au-delà : Méthode de Lindstedt, choix de la convention d’amplitude et séries de Fourier d’un mouvement non linéaire.

1. Commencer à 10° : lire la correction de période et le rapport A₃/A₁.
2. Passer à 50° : identifier le rang 3 et comparer le signal exact à l’approximation.
3. Passer à 80° : expliquer les écarts de période et l’apparition de rangs supérieurs.

**À justifier :** Relier le terme θ³ à des harmoniques nouvelles, et annoncer l’ordre et la convention d’amplitude d’une formule approchée.

### Deux ressorts : créer deux équilibres stables

Utiliser le potentiel exact pour trouver les équilibres, leur stabilité et les déplacements accessibles à énergie donnée.

**Objets et paramètres**

- x : position de la masse m (kg) ; attaches en (0,±L) ; L,L₀ : longueurs en m ; k : raideur en N/m.
- L₀ : longueur à vide ; √(x²+L²) : longueur actuelle ; ρ=L/L₀ : rapport qui commande les équilibres.
- L’écart initial, en multiples de L₀, est ajouté au centre ou au minimum de droite. V : énergie potentielle en J ; V(0) : niveau de la barrière si L<L₀.

**Repères** — Sup : Construire V puis faire le lien entre le signe de la force et la pente de V. Spé : Étudier tous les équilibres, leurs petites oscillations et la barrière ; second système de l’exercice 7 du PDF. Au-delà : Bifurcation symétrique, trajectoire séparatrice et perte de validité d’une approximation locale.

1. Choisir « Un seul puits » et identifier le minimum central.
2. Choisir « Deux puits : rester à droite » : comparer E à V(0) avant de lire le mouvement.
3. Choisir « Franchir la barrière », puis placer L/L₀ à 1 et examiner la disparition du terme quadratique.

**À justifier :** Prévoir le confinement ou la traversée sans intégrer, et calculer une pulsation autour du bon équilibre.

## Séance 08 — P2 · Oscillateurs

### Au seuil : un oscillateur sans raideur linéaire

Comprendre un équilibre stable dont la linéarisation ne décrit aucune oscillation, puis établir la loi T∝1/A.

**Objets et paramètres**

- L₀ : longueur à vide en m ; k : raideur en N/m ; m : masse en kg. Au seuil L=L₀, le potentiel commence en x⁴.
- β=k/L₀² : coefficient du rappel cubique, en N/m³ ; A : amplitude du lâcher en m ; le curseur donne A/L₀.
- T : période en s. Le modèle quartique et les ressorts exacts ont le même premier terme, mais diffèrent à grande amplitude.

**Repères** — Sup : Voir pourquoi V″=0 ne signifie pas instabilité et calculer la force cubique. Spé : Établir T(A) par énergie et tester sa dépendance en amplitude ; prolongement direct de l’exercice 7. Au-delà : Changements d’échelle et périodes dans les potentiels en x²ᵖ.

1. Commencer à A=0,04L₀ et comparer quartique et ressorts exacts.
2. Doubler l’amplitude : vérifier que T quartique est divisée par deux.
3. Passer à A=0,80L₀ : attribuer l’écart de période aux termes négligés du potentiel.

**À justifier :** Justifier la stabilité au-delà du seul critère V″>0 et distinguer une loi exacte d’une loi asymptotique.

### Duffing : une résonance qui dépend de l’amplitude

Relier l’oscillateur forcé du cours à une résonance non linéaire, en contrôlant le transitoire et le bilan de puissance.

**Objets et paramètres**

- ω₀ : pulsation propre ; xréf : longueur de référence ; τ=ω₀t et u=x/xréf : temps et position sans dimension.
- r=ω/ω₀ : rapport de pulsations ; ζ : amortissement réduit ; f : amplitude réduite de forçage ; β : coefficient cubique réduit.
- L’amplitude est celle de la composante à la fréquence imposée, mesurée sur dix périodes. Les courbes approchées ne décident pas de la stabilité des racines.

**Repères** — Sup : Amplitude et phase de l’oscillateur linéaire, transitoire et puissance dissipée. Spé : Résonance et bilan moyen ; TP d’oscillations forcées de la fiche P2. Au-delà : Balance harmonique de Duffing, réponses multiples et préparation d’une étude de stabilité ou d’hystérésis.

1. Choisir la référence linéaire et retrouver A=f/(2ζ) pour r=1.
2. Choisir le rappel durcissant : comparer le point mesuré aux amplitudes approchées.
3. Changer u(0) et augmenter le nombre de périodes ; comparer les deux fenêtres avant de conclure.

**À justifier :** Dire ce qui est calculé exactement par le modèle temporel, ce qui est approché par une harmonique, et quel contrôle indique un transitoire persistant.

## Séance 09 — P3 · Solides, rotation et contacts

### Six masses : quel axe résiste le plus à la rotation ?

Comprendre pourquoi un même objet est plus facile à faire tourner autour de certaines directions que d’autres.

**Objets et paramètres**

- mᵢ : six masses ponctuelles, en kg ; M : masse totale ; G : centre de masse ; rᵢ : positions depuis G, en m.
- O : point de l’axe ; OG : décalage en m ; u : direction unitaire, réglée par angle avec la verticale et azimut, en degrés.
- L’allongement suivant x multiplie les coordonnées de l’assemblage ; I_G,I_O : matrices d’inertie en kg·m².

**Repères** — Sup : MPSI : moment d’inertie pour une rotation autour d’un axe fixe ; distance d’un point à un axe. Spé : Prolongement pour MPSI/MP : Huygens tensoriel et axes principaux, reliés à l’algèbre linéaire. Au-delà : Inertie tensorielle d’un satellite et dynamique tridimensionnelle.

1. Placer G à l’origine O (ses coordonnées x et y nulles), puis comparer les deux courbes.
2. Décaler O puis orienter l’axe parallèlement à OG.
3. Allonger l’assemblage et identifier la plus petite inertie principale.

**À justifier :** Les inerties augmentent d’une quantité M|OG×u|² ; le déplacement parallèle à l’axe ne change rien.

### Décomposer le mouvement d’un solide : les deux théorèmes de König

Décomposer un mouvement réel en translation de G et rotation autour de G, puis vérifier deux identités indépendantes.

**Objets et paramètres**

- M : masse totale en kg ; G : centre de masse ; O : origine fixe ; OG : position en m.
- v_G : vitesse de G en m/s ; Ω : vitesse angulaire en rad/s ; rᵢ=GMᵢ : position d’une masse depuis G.
- E_c : énergie cinétique en J ; L_O : moment cinétique en O ; L_G : moment cinétique propre.

**Repères** — Sup : MPSI : mouvement de G, solide en translation ou en rotation autour d’un axe fixe. Spé : Prolongement pour MPSI/MP : les deux identités de König pour une cinématique générale. Au-delà : Référentiel barycentrique accéléré : identité cinématique et théorème dynamique sont deux questions différentes.

1. Choisir la translation seule et lire l’énergie de rotation.
2. Choisir la rotation seule puis observer les six vitesses.
3. Combiner les mouvements et déplacer la position initiale de G.

**À justifier :** L’énergie est une somme positive ; le moment cinétique est une somme vectorielle qui dépend de O.

## Séance 10 — P3 · Solides, rotation et contacts

### Une barre bascule : énergie, durée et réaction du pivot

Trouver la vitesse d’une barre qui tombe, puis la force de son pivot : Huygens fournit l’inertie, l’énergie la vitesse et le PFD la réaction.

**Objets et paramètres**

- M : masse en kg ; 2L : longueur totale en m ; O : pivot ; G : milieu ; g : pesanteur.
- θ : angle depuis la verticale ascendante ; θ₁,θ₂ : angles initial et final observés, réglés en degrés.
- I_O : moment d’inertie en kg·m² ; Rᵣ,Rθ : composantes radiale et tangentielle de la force du pivot, en N ; Δt : durée en s.

**Repères** — Sup : MPSI : énergie, moment cinétique et rotation d’un solide autour d’un axe fixe. Spé : Approfondissement : réaction du pivot et quadrature exacte d’un mouvement non linéaire. Au-delà : Séparatrice d’un système conservatif : trajectoire limite issue d’un équilibre instable.

1. Comparer les temps d’une barre courte et d’une barre longue.
2. Abaisser le premier angle à 0,2° et observer l’augmentation du temps.
3. Lire le changement de signe de Rᵣ puis contrôler l’énergie totale.

**À justifier :** La durée dépend de √L et diverge près de la verticale ; la réaction peut tirer parce que la liaison est un pivot.

### Une barre sur rotule : mouvement spatial et moment cinétique

Voir ce qui change lorsqu’une barre ne reste plus dans un plan et contrôler le calcul par deux invariants.

**Objets et paramètres**

- M : masse en kg ; 2L : longueur en m ; O : rotule fixe ; G : milieu ; g : pesanteur.
- n : axe unitaire de la barre ; θ : angle avec la verticale ascendante ; φ : azimut ; vitesses angulaires en rad/s.
- I⊥ : moment d’inertie transversal ; E : énergie en J ; L_z : composante verticale du moment cinétique ; temps en s.

**Repères** — Sup : MPSI : vecteurs position et vitesse ; reprendre d’abord le cas plan de la barre. Spé : Prolongement pour MPSI/MP : rotation spatiale, moment cinétique tensoriel et invariants. Au-delà : Réduction lagrangienne, potentiel effectif et stabilité des rotations coniques.

1. Lancer le pendule plan et regarder la trajectoire.
2. Donner une vitesse d’azimut et comparer la trajectoire spatiale.
3. Tester la rotation presque conique puis lire les écarts d’énergie et de L_z.

**À justifier :** L’énergie et L_z restent constants à l’erreur numérique près ; l’azimut initial peut empêcher le passage par une verticale.

## Séance 11 — P3 · Solides, rotation et contacts

### Un cylindre au bord de la table : quel événement survient d’abord ?

Calculer le mouvement d’un cylindre au bord d’une table, puis déterminer l’angle où le frottement ne suffit plus à maintenir l’adhérence.

**Objets et paramètres**

- m : masse en kg ; R : rayon en m ; g : pesanteur ; θ : angle de basculement du centre, depuis la verticale.
- N,T : composantes normale et tangentielle de la réaction, en N ; fₛ : coefficient maximal d’adhérence, sans dimension.
- I est le point de contact avec l’arête ; I_I : moment d’inertie autour de celle-ci. Le calcul s’arrête au premier glissement.

**Repères** — Sup : MPSI : énergie et rotation autour d’un axe fixe pendant la phase d’adhérence. Spé : MP : inégalité de Coulomb ; prolongement : contact d’un solide roulant au bord d’une table. Au-delà : Après le seuil : reconstruire un modèle de contact avec glissement, sans reprendre les anciennes réactions.

1. Choisir un faible frottement et repérer l’intersection T=fₛN.
2. Augmenter fₛ et comparer ce seuil au seuil N=0.
3. Observer que l’animation s’arrête au glissement et lire les hypothèses.

**À justifier :** Pour tout fₛ fini, le glissement précède le seuil de perte de contact calculé avec l’adhérence hypothétique.

### Tirer, freiner puis inverser une caisse : changer de régime

Choisir la bonne branche de Coulomb puis suivre un arrêt et, éventuellement, une inversion du mouvement.

**Objets et paramètres**

- m : masse en kg ; g : pesanteur ; F : force algébrique suivant la droite, en N ; N=mg : réaction normale.
- v₀ : vitesse initiale vers la droite, en m/s ; fₛ,f_d : coefficients statique et dynamique, sans dimension ; le curseur règle f_d/fₛ.
- T : frottement algébrique en N ; Q : énergie dissipée en J ; t : temps en s. Au repos, on teste une inégalité ; en glissement, on fixe le sens par la vitesse.

**Repères** — Sup : MPSI : PFD, équilibre et travail d’une force constante. Spé : MP : frottements solides en translation et simulation avec changement du mode de glissement. Au-delà : Traction variable, événements multiples et modèle de contact avec adhérence/glissement.

1. En mode repos, appliquer 10 N puis 18 N et identifier le seuil.
2. Choisir « Freiner puis rester au repos » : lire le temps d’arrêt et le changement de frottement.
3. Choisir « Freiner puis repartir à gauche » : vérifier le passage continu de v par zéro et le bilan d’énergie.

**À justifier :** Avant l’arrêt, le frottement s’oppose à v₀ ; ensuite il équilibre F ou change de sens si la caisse repart. Q reste positif même lorsque le déplacement net diminue.

## Séance 12 — P3 · Solides, rotation et contacts

### Glisser ou rouler sur un plan incliné ?

Comparer caisse et objets roulants sans imposer le roulement avant d’avoir vérifié sa possibilité.

**Objets et paramètres**

- m : masse en kg ; R : rayon en m pour les objets roulants ; α : inclinaison en degrés ; g : pesanteur.
- I_G : moment d’inertie ; k=I_G/(mR²) : coefficient sans dimension ; fₛ,f_d : coefficients de frottement.
- v_G : vitesse du centre ; ω : vitesse angulaire ; v_contact=v_G−Rω : vitesse relative au contact ; t : temps en s.

**Repères** — Sup : MPSI : projections du PFD et bilan d’énergie sur un plan incliné. Spé : MP : frottement de la caisse en translation ; prolongement : roulement et couplage translation-rotation. Au-delà : Résistance au roulement, déformation de contact et changements de régime.

1. Comparer cylindre, boule et cerceau avec assez de frottement.
2. Diminuer fₛ pour provoquer le glissement et comparer v_G à Rω.
3. Observer la dissipation : nulle en roulement idéal, positive en glissement.

**À justifier :** Le frottement statique répartit l’énergie entre translation et rotation sans en dissiper ; le frottement dynamique dissipe par glissement.

### Toupie pesante : précession lente et nutation

Comprendre la précession par un bilan de moment cinétique et voir les limites de l’approximation de rotation rapide.

**Objets et paramètres**

- m : masse en kg ; ℓ=OG : distance pivot–centre de masse en m ; R : rayon du rotor ; n : axe unitaire ; θ : inclinaison.
- I₁,I₃ : moments d’inertie transversal et axial en kg·m² ; ω₃ : rotation propre, convertie des tr/s en rad/s.
- Ω_p : vitesse angulaire de précession ; L : moment cinétique ; E : énergie ; t : temps en s. La nutation est la variation de θ.

**Repères** — Sup : MPSI : couple, produit vectoriel et rotation autour d’un axe fixe comme préparation. Spé : Prolongement pour MPSI/MP : gyroscope, précession, nutation et rotation spatiale. Au-delà : Équations de la toupie pesante, deux branches de précession régulière et applications astrophysiques.

1. Lancer rapidement en précession lente approchée et comparer les deux azimuts.
2. Lâcher sans précession initiale puis observer la nutation.
3. Réduire la vitesse propre et vérifier si l’approximation reste raisonnable.

**À justifier :** La précession lente diminue quand la rotation propre augmente ; la nutation dépend aussi du lancement.
