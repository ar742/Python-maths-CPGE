# Quinze séances de thermodynamique

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le bilan adapté.

## Séance 01 — Transferts & diffusion

### Fourier : une barre relie deux thermostats

Relier le premier principe local, Fourier et la résistance de l’exercice 1.

**Objets et paramètres**

- L : longueur en m ; S : section, convertie de cm² en m² ; x : position ; T(x) : température en °C.
- λ : conductivité en W/(m·K) ; j : flux thermique par unité d’aire en W/m² ; Φ=jS : puissance en W, positive de 0 vers L.

**Repères** — Sup : Déterminer le profil linéaire et distinguer j de Φ. Spé : Construire l’équation de chaleur et la résistance. Au-delà : Conductivité variable et sources internes.

1. Choisir la barre métallique et vérifier les unités de j et Φ.
2. Passer à l’isolant : comparer le même profil à une puissance différente.
3. Inverser les températures et prévoir le signe avant le calcul.

**À justifier :** Écrire une résistance avec sa géométrie et annoncer clairement le sens du flux.

### Un mur : conduction et convection en série

Utiliser l’analogie électrique sans perdre les surfaces et les températures d’interface.

**Objets et paramètres**

- eᵢ : épaisseur en m ; λᵢ : conductivité en W/(m·K) de la couche i ; S : surface commune en m².
- hᵢ,hₑ : coefficients de convection intérieur et extérieur en W/(m²·K) ; températures de l’air en °C.
- Φ : puissance traversant le mur en W ; les repères 0 à 4 sont des lieux d’interface, pas des distances dans l’air.

**Repères** — Sup : Additionner quatre résistances et calculer une puissance. Spé : Identifier les éléments dominants et les températures des surfaces. Au-delà : Ponts thermiques et résistance de contact.

1. Choisir brique et isolant puis lire les cinq températures.
2. Réduire l’isolant et observer sa part de résistance.
3. Réduire h extérieur : trouver où la chute de température augmente.

**À justifier :** Distinguer température d’air, température de surface et interface solide.

## Séance 02 — Transferts & diffusion

### Rayon critique : ajouter un isolant peut accroître la perte

Prolonger la coque de l’exercice 1 et expliquer pourquoi une isolation peut d’abord accroître la perte.

**Objets et paramètres**

- Rᵢ : rayon intérieur fixe ; e : épaisseur ; Rₑ=Rᵢ+e : rayon extérieur. Les cm des réglages sont convertis en m.
- λ : conductivité en W/(m·K) ; h : convection extérieure en W/(m²·K) ; longueur du cylindre en m ; températures en °C.
- Φ : puissance totale en W ; j : flux par unité d’aire en W/m², qui varie avec le rayon ; λ/h et 2λ/h sont des longueurs.

**Repères** — Sup : Relier surface croissante et courant surfacique. Spé : Calculer les résistances radiales et les extrema. Au-delà : Couches multiples cylindriques et échange radiatif.

1. Choisir le cylindre et chercher le maximum sur la courbe de perte.
2. Passer à la sphère : comparer les deux seuils.
3. Choisir un rayon intérieur au-dessus du seuil et vérifier la décroissance.

**À justifier :** Dire si le rayon critique est accessible et distinguer Φ constant de j constant.

### Igloo : bilan d’une personne et géométrie hémisphérique

Reprendre l’exercice 2 avec une puissance nette définie et une géométrie sans ambiguïté.

**Objets et paramètres**

- R : rayon intérieur en m ; e : épaisseur en m ; λ : conductivité de la paroi en W/(m·K).
- P : nombre de personnes multiplié par la puissance nette de chacune, en W ; températures extérieure et intérieure en °C.
- La température calculée suppose une paroi solide et des paramètres constants ; le chauffage doit être comparé à la puissance perdue.

**Repères** — Sup : Compter les watts reçus et évacués. Spé : Vérifier la géométrie et la possibilité d’une épaisseur. Au-delà : Fusion, ventilation et rayonnement net.

1. Choisir neige isolante : lire puissance, température et statut de paroi.
2. Passer à la glace dense et expliquer le changement.
3. Changer le nombre de personnes puis regarder si l’épaisseur visée existe.

**À justifier :** Séparer un bilan idéal et une réalisation physique, avec puissance et rayon correctement définis.

## Séance 03 — Transferts & diffusion

### Diffusion 1D : calcul stable et modes de Fourier

Comparer une solution modale à un véritable schéma de diffusion stable.

**Objets et paramètres**

- L est la longueur de barre en m ; χ sa diffusivité, convertie de mm²/s en m²/s.
- N est le nombre de subdivisions ; Δx=L/N est la maille spatiale en m et Δt le pas temporel en s.
- r=χΔt/Δx² est le nombre de Fourier sans dimension ; il contrôle la stabilité.
- T₀ est la température des extrémités en °C. La carte T(x,t) donne la température à la position x en m et au temps t en s.

**Repères** — Sup : Lire le refroidissement et le sens des flux aux bords. Spé : Démontrer le facteur n² et la condition de stabilité. Au-delà : Schémas implicites et estimation d’erreur.

1. Préparer deux modes et suivre la disparition des détails.
2. Comparer FTCS et modes exacts au temps final.
3. Augmenter N : lire l’erreur et le nombre de pas réellement utilisés.

**À justifier :** Contrôler la stabilité avant de confondre un défaut numérique avec un phénomène physique.

### Choc thermique : une profondeur en √(χt)

Relier l’exercice 6, l’échelle de diffusion et un bilan d’énergie indépendant.

**Objets et paramètres**

- x : profondeur en m ; t : temps depuis le choc, converti de min en s ; χ : diffusivité, convertie de mm²/s en m²/s.
- ρc : capacité thermique par volume, en J/(m³·K) ; λ=χρc : conductivité ; températures initiale et de surface en °C.
- χt a la dimension d’une longueur au carré ; l’énergie reçue est rapportée à une unité de surface, en J/m².

**Repères** — Sup : Prévoir une profondeur en √t et le signe du transfert. Spé : Vérifier la solution et les deux calculs d’énergie. Au-delà : Conditions convectives et surface chauffée progressivement.

1. Chauffer la surface et lire flux puis énergie.
2. Multiplier le temps par quatre : tester les trois lois d’échelle.
3. Refroidir et vérifier les valeurs algébriques négatives.

**À justifier :** Distinguer une singularité de flux intégrable et une énergie infinie.

## Séance 04 — Transferts & diffusion

### Onde thermique : filtrer le jour et les saisons

Prolonger l’exercice 7 en comparant les profondeurs atteintes par deux cycles concrets.

**Objets et paramètres**

- P : période journalière ou annuelle en s ; ω=2π/P : pulsation ; χ : diffusivité en m²/s ; z : profondeur en m.
- T₀ : température moyenne ; A : amplitude de surface en K ; θ(z) : amplitude complexe à la profondeur z.
- δ : profondeur de pénétration liée à l’atténuation ; le retard est affiché en heures sans réduction modulo P.

**Repères** — Sup : Comparer qualitativement un jour et une saison. Spé : Calculer amplitude, phase et longueur δ. Au-delà : Réponse fréquentielle et identification d’une diffusivité.

1. Observer le cycle journalier à 0,2 m.
2. Passer au cycle annuel à 2 m et comparer δ.
3. Revenir au jour à 1 m : expliquer la petite amplitude malgré un retard important.

**À justifier :** Lire séparément amplitude et phase, en identifiant la fréquence choisie.

### Biot : quand peut-on supposer une température uniforme ?

Choisir le modèle de refroidissement en confrontant sa validité à un profil spatial.

**Objets et paramètres**

- a : demi-épaisseur convertie de mm en m ; S : aire d’une face ; V=2aS : volume ; Séchange=2S : aire totale d’échange.
- λ : conductivité en W/(m·K) ; h : convection en W/(m²·K) ; Bi=ha/λ : nombre de Biot sans dimension.
- ρc : capacité volumique en J/(m³·K) ; χ=λ/(ρc) : diffusivité ; ρca/h : temps de relaxation uniforme en s ; Tᵢ−Tair : écart initial en K.

**Repères** — Sup : Résoudre le modèle exponentiel uniforme. Spé : Calculer Bi et identifier les trois températures. Au-delà : Détermination des modes avec conditions de Robin.

1. Choisir Bi petit : comparer toutes les températures.
2. Choisir Bi grand : repérer le gradient centre–surface.
3. Réduire l’épaisseur et suivre l’amélioration du modèle capacitif.

**À justifier :** Donner la longueur caractéristique et vérifier une approximation avant de l’utiliser.

## Séance 05 — Transferts & diffusion

### Une tache de chaleur : énergie conservée, pic qui s’étale

Relier une carte de température à un bilan énergétique et à des variances définies.

**Objets et paramètres**

- χ : diffusivité en m²/s ; e : épaisseur en m ; ρc : capacité volumique en J/(m³·K) ; ρce : capacité par aire en J/(m²·K).
- Q : énergie initiale en J ; σ₀,σ : largeurs initiale et actuelle dans chaque direction ; t : temps en s.
- La carte utilise les coordonnées x,y en mm ; σ est une largeur par direction, pas le rayon de la tache ; la température de fond est en °C.

**Repères** — Sup : Relier étalement et diminution du maximum. Spé : Vérifier la normalisation et le bilan 2D. Au-delà : Noyau de chaleur et convolution de profils.

1. Lire la carte et l’énergie intégrée.
2. Multiplier le temps par quatre et comparer les largeurs.
3. Réduire la largeur initiale puis retrouver sa disparition progressive.

**À justifier :** Utiliser 2χt par direction et 4χt pour la diffusion radiale en 2D.

### Marche aléatoire : de la loi binomiale à Fick

Déduire la diffusion de sauts probabilistes en gardant une référence exacte.

**Objets et paramètres**

- ε : longueur d’un saut, convertie de µm en m ; τ : durée entre sauts, convertie de ms en s ; N : nombre de pas.
- p : probabilité d’un saut vers +x ; X : position aléatoire ; la variance mesure l’écart à la moyenne, qui peut dériver si p≠1/2.
- D=2p(1−p)ε²/τ : coefficient de diffusion en m²/s ; après t=Nτ, la variance vaut 2Dt.

**Repères** — Sup : Calculer moyenne et variance de X. Spé : Retrouver D et l’équation de Fick. Au-delà : Théorème central limite et advection–diffusion.

1. Choisir peu de pas et observer le caractère discret.
2. Augmenter N : comparer binomiale et gaussienne.
3. Introduire p=0,7 et distinguer déplacement du centre et étalement.

**À justifier :** Relier variance et coefficient diffusif en tenant compte de la parité du réseau.

## Séance 06 — Transferts & diffusion

### Langevin : du mouvement inertiel à Stokes–Einstein

Mettre le TP de Langevin en relation avec les échelles réelles et la moyenne statistique.

**Objets et paramètres**

- a : rayon converti de nm en m ; η : viscosité convertie de mPa·s en Pa·s ; la masse volumique détermine m, masse en kg.
- kB : constante de Boltzmann en J/K ; T : température absolue en K ; τᵥ=m/(6πηa) : temps de relaxation de la vitesse en s.
- D=kBT/(6πηa) : coefficient de diffusion en m²/s, donné par Stokes–Einstein.
- t : durée en s ; le déplacement quadratique moyen (MSD) est donné par direction, en m². Les trajectoires planes sont simulées.

**Repères** — Sup : Identifier rayon, viscosité et température dans D. Spé : Relier Langevin au passage balistique–diffusif. Au-delà : Processus d’Ornstein–Uhlenbeck et transitions corrélées.

1. Observer t≈τᵥ et comparer à 2Dt.
2. Choisir le temps court puis lire le comportement en t².
3. Passer aux secondes et augmenter la viscosité : comparer les amplitudes de diffusion.

**À justifier :** Définir l’état initial et la dimension du déplacement avant d’extraire D.

### Neutrons : diffusion, absorption et bilan de source

Prolonger l’exercice 3 en contrôlant la source par un bilan, pas seulement par une forme exponentielle.

**Objets et paramètres**

- Q : débit de source, converti des millions/s en s⁻¹ ; τ : durée de vie en s ; D : diffusivité convertie de cm²/s en m²/s.
- r : distance à la source ; L=√Dτ : longueur caractéristique en m ; n : densité de neutrons en m⁻³.
- j : flux par unité d’aire en m⁻²·s⁻¹ ; Φ : débit traversant une sphère en s⁻¹.

**Repères** — Sup : Vérifier les dimensions et lire l’atténuation. Spé : Résoudre la densité et le bilan d’absorption. Au-delà : Diffusion multigroupe et réactions en milieu fini.

1. Lire L et le nombre total Qτ.
2. Comparer débit traversant et absorption intérieure à r=L.
3. Modifier τ puis Q : distinguer longueur et simple changement d’amplitude.

**À justifier :** Fixer la constante par la source et vérifier le débit à chaque rayon.

## Séance 07 — Transferts & diffusion

### Électrolyte : diffusion commune et potentiel de jonction

Relier diffusion particulaire, courant électrique et champ créé par une jonction.

**Objets et paramètres**

- cG,cD : concentrations gauche et droite en mol/m³ ; N_A : constante d’Avogadro en mol⁻¹ ; n=N_Ac : nombre d’ions par m³.
- D₊,D₋ : diffusivités converties en m²/s ; T : température en K ; t : temps en s ; e : charge élémentaire positive.
- Γ₊,Γ₋ : flux particulaires en m⁻²·s⁻¹ ; V : potentiel en V ; E=−V′ : champ électrique ; e(Γ₊−Γ₋) : courant par unité d’aire.

**Repères** — Sup : Distinguer flux particulaire et courant électrique. Spé : Calculer le champ et le coefficient ambipolaire. Au-delà : Nernst–Planck, couches de Debye et potentiel de jonction.

1. Comparer les flux des ions et Fick ambipolaire.
2. Égaliser les diffusivités et vérifier le champ nul.
3. Inverser les concentrations et prévoir le signe du potentiel.

**À justifier :** Établir le signe par la convention de potentiel et justifier le flux commun.

### Diffuser sans perdre d’énergie : l’entropie augmente

Vérifier ensemble le premier et le second principe dans un système isolé diffusif.

**Objets et paramètres**

- N : nombre de cellules ; C : capacité de chaque cellule en J/K ; G : conductance entre voisines en W/K.
- Tᵢ : température de la cellule i ; les °C des réglages sont convertis en K pour les rapports et les inverses.
- ΔS : variation d’entropie en J/K ; sa production instantanée est en W/K ; la durée est donnée en multiples du temps de relaxation lent.

**Repères** — Sup : Calculer la température finale par conservation. Spé : Démontrer la positivité et lire sa décroissance. Au-delà : Formes quadratiques, principe du maximum et thermodynamique irréversible.

1. Préparer deux moitiés de températures différentes.
2. Comparer énergie constante, entropie croissante et production décroissante.
3. Choisir l’état uniforme : vérifier les trois bilans nuls.

**À justifier :** Distinguer conservation d’énergie et production d’entropie avec des températures absolues.

## Séance 08 — Potentiels, travaux & machines

### Même état final, travaux différents : suivre trois chemins

Distinguer fonctions d’état et transferts en comparant trois transformations ayant exactement les mêmes extrémités.

**Objets et paramètres**

- T₁,T₂ : températures absolues initiale et finale, en K.
- V₁,V₂ : volumes ; r=V₂/V₁ ; k : exposant de PVᵏ=constante.
- R=8,314 J/(mol·K) : constante molaire des gaz parfaits. cV,cP : capacités molaires à volume et pression constants ; γ=cP/cV.
- W,Q : travail et chaleur reçus en J ; U : énergie interne ; S : entropie. ΔU,ΔS sont leurs variations.

**Repères** — Sup : Gaz parfait, travail de pression, fonctions d’état. Spé : Polytropes et bilan d’entropie. Au-delà : Comparaison de réalisations réversibles et irréversibles.

1. Choisir k=1 : contrôler W=−RT ln r et ΔU=0.
2. Choisir k=1,4 : vérifier Q=0 et ΔS=0.
3. Comparer les deux autres travaux, puis inverser la détente en compression.

**À justifier :** Les aires changent avec le chemin ; ΔU et ΔS sont communes parce que les états initial et final sont communs.

### Surface, fil, condensateur, bobine : une force conjuguée

Reconnaître l’effort et la coordonnée conjugués, contrôler leurs unités et interpréter une restitution d’énergie.

**Objets et paramètres**

- s : réglage sans dimension converti selon le dispositif ; κ : facteur de raideur ou de couplage ; W : travail reçu en J.
- σ,A : tension superficielle en N/m et aire en m² ; k,x : raideur en N/m et allongement en m.
- u,q : tension électrique en V et charge en C ; I,λ : courant en A et flux lié d’une bobine en Wb.

**Repères** — Sup : Travaux mécanique et électrique, énergies du ressort et du condensateur. Spé : Travaux de surface et généralisation des coordonnées conjuguées. Au-delà : Conventions magnétiques et choix du flux lié.

1. Étirer le fil : comparer le travail à la variation kx²/2.
2. Passer au condensateur et lire la conversion entre s et q.
3. Choisir la bobine puis inverser les deux états : le travail change de signe.

**À justifier :** Un même schéma d’intégration traite des dispositifs distincts, à condition de définir correctement les grandeurs et les unités.

## Séance 09 — Potentiels, travaux & machines

### Helmholtz : une cloison interne cherche le minimum de F

Utiliser un potentiel sous contraintes et relier son minimum à un véritable équilibre mécanique interne.

**Objets et paramètres**

- Vtotal : volume fixé ; T : température en K ; nG,nD : quantités de gaz séparées, en mol ; y=VG/Vtotal : position réduite de la cloison.
- ks : raideur du ressort en N/m ; L : longueur de l’enceinte en m ; ys : position réduite de repos ; yᵢ : position réduite initiale.
- F : énergie libre de Helmholtz en J ; la force sur la cloison se déduit de sa variation à volume et température fixés.

**Repères** — Sup : Pression sur un piston et force d’un ressort. Spé : Potentiel de Helmholtz et critère de stabilité. Au-delà : Minimisation sous contraintes et dissipation interne.

1. Mettre ks=0 : l’équilibre égalise les pressions.
2. Ajouter un ressort décentré : les pressions d’équilibre deviennent différentes.
3. Changer la position initiale : le minimum reste le même mais l’énergie libre perdue change.

**À justifier :** Le volume total fixe laisse une variable interne évoluer. Le minimum de F traduit le bilan des forces et sa courbure assure la stabilité.

### Gibbs : l’équilibre d’une réaction A ⇌ B minimise G

Relier composition, potentiel chimique, constante d’équilibre et minimum de Gibbs.

**Objets et paramètres**

- x : fraction molaire de B dans une mole totale A,B ; xᵢ : fraction initiale ; T : température en K.
- ΔrH° : enthalpie standard de réaction, convertie des kJ/mol en J/mol ; ΔrS° : entropie standard en J/(mol·K).
- G : enthalpie libre en J ; ξ : avancement en mol ; ΔrG : pente par rapport à ξ ; K : constante d’équilibre sans dimension.

**Repères** — Sup : Logarithme, pente et minimum d’une fonction. Spé : Potentiels chimiques et équilibre chimique. Au-delà : Convexité des mélanges et énergie libre disponible.

1. Prendre ΔrH°=ΔrS°=0 : trouver x=1/2.
2. À T=300 K, choisir une réaction favorable à B et lire le sens à la composition initiale.
3. Augmenter T avec ΔrH°<0,ΔrS°<0 : observer le changement de majorité.

**À justifier :** ΔrG donne le sens spontané à la composition courante ; ΔrG° seul ne suffit pas. Le minimum fixe un état, pas une cinétique.

## Séance 10 — Potentiels, travaux & machines

### Calorimètre : température finale, chaleur latente et entropie

Établir un bilan de calorimétrie, reconnaître un changement de phase et vérifier le second principe.

**Objets et paramètres**

- m₁,m₂ : masses en kg ; c : capacité massique en J/(kg·K) ; Ccal : capacité du calorimètre en J/K, initialement à la température du corps chaud.
- Ti : températures initiales en K ; Tm=273,15 K : température de fusion ; L=334 kJ/kg : chaleur latente massique de la glace.
- Tf : température finale et masses finales : inconnues à déterminer avant la variation d’entropie ΔS, en J/K.

**Repères** — Sup : Calorimétrie, chaleurs latentes et températures absolues. Spé : Entropie créée dans un contact irréversible. Au-delà : Métrologie d’une chaleur latente et traitement de tous les régimes.

1. Choisir les deux corps sans phase et vérifier une moyenne pondérée.
2. Ajouter davantage de glace : identifier le palier à 273,15 K.
3. Choisir le cas froid extrême : l’eau initiale gèle ; contrôler que l’entropie totale reste positive.

**À justifier :** Le bilan choisit la phase finale. Une température au point de fusion ne détermine pas à elle seule les masses de chaque phase.

### Joule : U constante ou H constante, deux détentes différentes

Choisir U ou h selon le système et déterminer le signe réel d’un refroidissement ou d’un réchauffement.

**Objets et paramètres**

- u,h : énergie interne et enthalpie molaires en J/mol ; v : volume molaire converti des L/mol en m³/mol ; T : température en K.
- a : attraction en Pa·m⁶/mol² ; b : covolume converti des cm³/mol en m³/mol ; cV : capacité molaire, réglée en multiples de R.
- µJT=(∂T/∂P)h : coefficient de Joule–Thomson ; Tinv : température d’inversion ; P : pression.

**Repères** — Sup : Première loi de Joule et détente irréversible. Spé : Bilan enthalpique d’un étranglement. Au-delà : Van der Waals, inversion et stabilité mécanique.

1. Choisir le gaz parfait dans le vide : T reste constante, S augmente.
2. Choisir van der Waals dans le vide : vérifier Δu=0 et le refroidissement.
3. Comparer les deux presets d’étranglement : µJT change de signe et h reste constante.

**À justifier :** Les deux expériences sont adiabatiques mais ne conservent pas la même grandeur. Une chute de pression ne garantit pas un refroidissement.

## Séance 11 — Potentiels, travaux & machines

### Carnot : moteur, réfrigérateur et pompe à chaleur

Construire les performances et les signes d’une machine avec les deux principes, puis chiffrer ses irréversibilités.

**Objets et paramètres**

- Tc,Tf : températures des sources chaude et froide en K ; Qc,Qf : chaleurs reçues par cycle ; W : travail reçu par la machine.
- η : rendement du moteur ; COP : coefficient de performance du réfrigérateur ou de la pompe à chaleur ; φ : fraction de la performance idéale.
- Les énergies sont en kJ/cycle ; la référence est Qc pour le moteur et W pour le réfrigérateur ou la pompe.

**Repères** — Sup : Machines dithermes et rendement de Carnot. Spé : COP et calcul de l’entropie créée. Au-delà : Différence entre performance globale et trajectoire de cycle.

1. Mettre φ=1 : vérifier l’entropie créée nulle.
2. Réduire φ en moteur : suivre la chaleur rejetée et le travail.
3. Passer du frigo à la PAC : vérifier COPc−COPf=1.

**À justifier :** Les signes résultent du système choisi. Le COP peut dépasser 1, et les pertes se lisent dans le second principe.

### Otto, Diesel, Brayton, Stirling : comparer des cycles calculés

Comparer des cycles à partir de leurs branches calculées, puis comprendre l’effet d’une régénération interne.

**Objets et paramètres**

- r : taux de compression en volumes pour Otto, Diesel et Stirling, en pressions pour Brayton.
- z : paramètre de chauffage, défini selon le cycle dans les réglages et le bilan ; T₁ : température minimale en K.
- cV,cP : capacités molaires à volume et pression constants ; γ=cP/cV ; ε : efficacité du régénérateur de Stirling.

**Repères** — Sup : Transformations élémentaires et aire d’un cycle. Spé : Cycles Otto, Diesel, Brayton et comparaison de rendements. Au-delà : Stirling, régénérateur et sources à température variable.

1. Choisir Otto : repérer les deux isochores dans P,V.
2. Passer à Diesel puis Brayton : identifier les isobares et le sens de r.
3. En Stirling, modifier ε : l’aire ne change pas, mais la chaleur externe et le rendement changent.

**À justifier :** La même convention ferme tous les bilans. La géométrie du cycle et les échanges externes ne donnent pas la même information lorsqu’un régénérateur est présent.

## Séance 12 — Potentiels, travaux & machines

### Compresseur : répartir les rapports de pression pour minimiser le travail

Appliquer le premier principe aux écoulements et optimiser les pressions intermédiaires sous refroidissement.

**Objets et paramètres**

- r : rapport total des pressions ; N : nombre d’étages ; T₁ : température en K, restaurée après chaque refroidisseur.
- f : fraction de ln r affectée au premier étage ; les autres rapports de pression sont égaux ; ηs : rendement isentropique sans dimension.
- Le travail molaire consommé est en J/mol ; un rendement de 1 décrit la compression isentropique idéale.

**Repères** — Sup : Énergie et pression d’un gaz. Spé : Compresseur ouvert et refroidissement intermédiaire. Au-delà : Optimisation de N rapports et limite isotherme.

1. Avec N=2, choisir f=1/2 : retrouver la moyenne géométrique.
2. Éloigner f du minimum : comparer le travail.
3. Augmenter N puis réduire ηs : distinguer gain d’étagement et pertes internes.

**À justifier :** Les pressions optimales forment une suite géométrique. Le refroidisseur rejette une chaleur et ne fournit pas un travail d’arbre négatif.

### Corps fini : une différence de température vaut-elle du travail ?

Quantifier le travail maximal d’un corps fini et distinguer conservation de l’énergie et destruction d’exergie.

**Objets et paramètres**

- C : capacité thermique totale en J/K ; Ti : température initiale du corps ; T₀ : température de l’environnement, en K.
- B : travail maximal disponible en J ; φ : fraction récupérée ; W,Q : transferts reçus par corps et machine, en J.
- Scréée : entropie créée totale en J/K ; l’exergie B mesure l’énergie convertible en travail pour cet environnement.

**Repères** — Sup : Contact thermique et variation d’énergie. Spé : Machine réversible entre un corps fini et un thermostat. Au-delà : Exergie et relation entre destruction d’exergie et entropie créée.

1. Comparer C(Ti−T₀) à B pour un corps chaud.
2. Mettre φ=0 : le contact direct fournit zéro travail et détruit B.
3. Choisir Ti<T₀ : le corps se réchauffe mais un travail maximal positif existe.

**À justifier :** L’exergie dépend de l’environnement et s’annule à l’équilibre. L’énergie ne disparaît pas quand l’exergie est détruite.

## Séance 13 — Effets couplés & mesures

### Cube de Leslie : comparer des surfaces à même température

Comparer des émissivités, puis transformer les échanges thermiques en bilan du cube.

**Objets et paramètres**

- T,Tₐ : températures du cube et de la pièce en K ; a : côté en m ; A=a² : aire d’une face en m².
- ε : émissivité infrarouge sans dimension ; h : convection en W/(m²·K) ; Cₜₕ : capacité thermique totale en J/K.
- U : signal de la thermopile ; les pertes de chaque face deviennent un bilan de refroidissement du cube.

**Repères** — Sup : Unités, bilan énergétique et équation différentielle. Spé : Rayonnement, convection et linéarisation près de l’ambiance. Au-delà : Étalonnage radiométrique et estimation des échanges.

1. Choisir le preset TP et comparer les quatre signaux.
2. Rapprocher T de Tₐ : distinguer un signal nul d’une faible émissivité.
3. Augmenter h puis observer chauffage nécessaire et refroidissement.

**À justifier :** Le TP compare les surfaces ; le bilan inclut aussi la convection, que la thermopile ne mesure pas.

### Thermocouple : calibrer et compenser la jonction froide

Passer d’une tension mesurée à une température avec une référence connue.

**Objets et paramètres**

- Th : température à mesurer ; Tf : température de jonction froide ; Tᵣ=273,15 K : référence ; toutes sont en K.
- S₀ : coefficient Seebeck à Tᵣ, réglé en µV/K ; s₁ : sa pente en µV/K² ; V : tension à circuit ouvert.
- δTf : erreur simulée de la température de référence, en K ; elle perturbe la température déduite de V.

**Repères** — Sup : Primitives, unités et calibration affine. Spé : Inversion non linéaire et propagation d’incertitude. Au-delà : Thermocouples réels et coefficients dépendant de la température.

1. Mettre s₁=0 : retrouver V=S₀(Th−Tf).
2. Choisir une calibration courbe et comparer la température retrouvée à l’approximation.
3. Ajouter 5 K d’erreur froide et expliquer le biais avec les coefficients locaux.

**À justifier :** Une tension de thermocouple dépend de deux températures. La compensation froide fait partie de la mesure.

## Séance 14 — Effets couplés & mesures

### Module Peltier : refroidir demande un bilan complet

Décider si un module refroidit et vérifier ses bilans d’énergie et d’entropie.

**Objets et paramètres**

- Tc : température froide en K ; ΔT : écart entre faces en K ; Th=Tc+ΔT : température chaude maintenue.
- I : courant en A ; α : coefficient en V/K ; R : résistance électrique en Ω ; K : conductance thermique en W/K.
- Qc,Qh,P : puissances extraite, rejetée et électrique consommée, en W ; la charge thermique réglée est la puissance à extraire.

**Repères** — Sup : Joule, conduction, signes et conservation de l’énergie. Spé : Performance, optimisation et production d’entropie. Au-delà : Dissipateurs et modèles thermoélectriques dépendant de la température.

1. Avec le premier preset, vérifier Qh=Qc+P.
2. Passer au courant excessif : repérer le rôle du terme en I².
3. Couper le courant, puis faire varier la charge pour discuter l’équilibre.

**À justifier :** Un courant non nul ne garantit pas le refroidissement. Le signe de Qc décide du mode de fonctionnement.

### Onde sonore : coupler compression et diffusion thermique

Résoudre deux équations couplées et donner un sens à un nombre d’onde complexe.

**Objets et paramètres**

- P₀ : pression en Pa ; T₀ : température en K ; ρ₀ : masse volumique en kg/m³ ; γ : rapport des capacités ; λ : conductivité en W/(m·K).
- f : fréquence en Hz ; ω=2πf : pulsation ; k : nombre d’onde complexe en m⁻¹ ; q=k² ; L : longueur observée en m.
- p : petite surpression en Pa ; τ : petite perturbation de température en K ; le nombre d’onde décrit phase et atténuation.

**Repères** — Sup : Ondes sinusoïdales et exponentielles complexes. Spé : Équation de la chaleur et dispersion d’une onde couplée. Au-delà : Branche diffusive et éléments de modèles thermoacoustiques.

1. Choisir λ=0 : retrouver c et la relation adiabatique entre τ et p.
2. Choisir une conduction renforcée : comparer vitesse et phase.
3. Modifier f et L ; distinguer longueur d’onde et longueur d’atténuation.

**À justifier :** La conduction change la relation température–pression et atténue l’onde. Le signe de Im k dépend de la convention.

## Séance 15 — Effets couplés & mesures

### Quartz : réciprocité, résonance et antirésonance

Déduire les effets direct et inverse d’une même énergie, puis étudier un résonateur.

**Objets et paramètres**

- x : déplacement en m ; q : charge en C ; V : tension en V ; θ : couplage réciproque, en C/m ou N/V.
- m : masse convertie des mg en kg ; k : raideur convertie des MN/m en N/m ; C : capacité convertie des nF en F ; ζ : amortissement réduit.
- r=2ζ√(km) : coefficient de frottement ; Y : courant divisé par tension ; fᵣ,fₐ : fréquences de résonance et d’antirésonance sans pertes.

**Repères** — Sup : Énergie du ressort, condensateur et oscillateur. Spé : Dérivées croisées, potentiel adapté et admittance complexe. Au-delà : Circuits équivalents de résonateurs et identification du couplage.

1. Choisir le premier preset et observer l’amplification autour de fᵣ.
2. Renforcer θ : voir fₐ s’éloigner de fᵣ.
3. Augmenter ζ : le pic reste fini et le creux devient moins profond.

**À justifier :** Résonance et antirésonance sont deux mécanismes distincts. La réciprocité et la passivité proviennent de la même énergie.

### Détente d’une vapeur saturante : décider du début de condensation

Comparer deux pentes pour décider du début d’un changement d’état.

**Objets et paramètres**

- T*,P* : température et pression initiales saturées ; L* : chaleur latente massique à T*, convertie des MJ/kg en J/kg.
- B : pente en J/(kg·K) ; A=L*+BT* : constante de L(T)=A−BT ; R=461,5 J/(kg·K) : constante massique de la vapeur.
- γ : rapport des capacités thermiques ; ΔT : refroidissement en K ; la marge compare les pentes réduites des courbes adiabatique et de saturation.

**Repères** — Sup : Logarithmes, intégration et comparaison de variations. Spé : Clapeyron, lois de Laplace et début de condensation. Au-delà : Bilans diphasés et modèles de nucléation des gouttes.

1. Prendre les valeurs de vapeur d’eau et comparer les pentes initiales.
2. Réduire L* : chercher la frontière de la carte où la marge s’annule.
3. Observer que la courbe de vapeur seule s’arrête à la condensation.

**À justifier :** Le critère explique le début du brouillard. Il ne donne pas l’évolution ultérieure du mélange liquide–vapeur.
