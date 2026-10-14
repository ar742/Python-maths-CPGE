# Chimie pour l’industrie — douze séances guidées

Commencer par les trois séances de sup. Les séances suivantes réinvestissent les outils de spé, selon la filière; les compléments de catalyse et de transport sont fournis. Pour chaque TP : lire les objets, prévoir un résultat, essayer les trois gestes et justifier un bilan.

## Séance 01 — Sup · mesurer une vitesse

### Une horloge chimique pour identifier une loi de vitesse

Exploiter les six mesures du TP p.546 pour comparer des lois de vitesse. Comprendre ce qui est mesuré et ce qui dépend du modèle choisi.

**Objets et paramètres**

- t est le temps en secondes ; V est le volume cumulé de thiosulfate associé aux seuils colorés, en mL.
- V∞ est le volume final supposé. La fraction de peroxyde restante est modélisée par y=1−V/V∞.
- κ est un coefficient normalisé, en s⁻¹. L’erreur comparée est la moyenne des carrés des écarts de volume, en mL².

**Repères** — Sup : avancement, vitesse, ordre apparent et temps de demi-réaction. Spé : discuter un ajustement et les conditions de dégénérescence de l’ordre. Identification de paramètres et incertitude expérimentale : les six points ne fournissent pas tous les ordres partiels.

1. Garder V∞=10 mL et repérer V=5 mL à t=315 s.
2. Comparer les trois courbes et les trois erreurs calculées sur V.
3. Choisir V∞=12 mL : expliquer pourquoi l’ajustement change alors que les mesures restent identiques.

**À justifier :** Une droite obtenue après transformation suggère une loi ; la conclusion dépend aussi du modèle de mesure.

### Accélérer sans déplacer l’équilibre

Relier une variation de température à une constante cinétique, puis distinguer accélération et déplacement d’équilibre.

**Objets et paramètres**

- T est la température absolue en K ; Ea l’énergie d’activation, affichée en kJ·mol⁻¹ et convertie en J·mol⁻¹ dans l’exponentielle.
- R=8,314462618 J·mol⁻¹·K⁻¹ est la constante des gaz parfaits. La référence sans catalyse est kref=0,01 s⁻¹ à Tref=500 K.
- ΔEa est l’abaissement de la barrière ; les deux voies partagent le même préfacteur. Leur enthalpie de réaction illustrative vaut −40 kJ·mol⁻¹.

**Repères** — Sup : influence de T, catalyse et constante de vitesse. Spé : exploiter une énergie apparente et distinguer cinétique et thermodynamique. Le modèle représente une comparaison de voies ; l’activité d’un matériau réel peut aussi dépendre de l’adsorption et du transport.

1. À 500 K, vérifier k=0,01 s⁻¹ sans catalyse.
2. Abaisser la barrière de 20 kJ·mol⁻¹ et prévoir le facteur exp(ΔEa/RT).
3. Passer à 750 K : comparer les vitesses et le facteur relatif d’accélération.

**À justifier :** Une barrière plus faible accélère la transformation ; les états initial et final restent les mêmes.

## Séance 02 — Sup → spé · établir un bilan thermique

### Chaleur de combustion et récupération

Comparer une mole et un kilogramme de combustible, puis séparer condensation et récupération de chaleur.

**Objets et paramètres**

- νᵢ est le coefficient stœchiométrique : négatif pour un réactif, positif pour un produit. ΔfHᵢ° est l’enthalpie standard de formation, en kJ·mol⁻¹, à 298 K.
- M est la masse molaire du combustible, en g·mol⁻¹. PCI et PCS sont les chaleurs libérées par kilogramme, respectivement avec eau vapeur et eau liquide.
- f est la fraction d’eau condensée ; r est la fraction de chaleur récupérée. Ces nombres sont compris entre 0 et 1.

**Repères** — Sup : bilans de matière et premier principe, lecture des états physiques. Spé : thermochimie et énergie de réaction, bilan d’un procédé. Intégration thermique d’une usine et analyse de cycle de vie : seules leurs limites de périmètre sont introduites.

1. Sélectionner CH₄, f=0 et r=1 ; écrire la combustion.
2. Passer à f=1 et calculer l’énergie supplémentaire liée à deux moles d’eau.
3. Comparer H₂ et méthanol par mole, puis par kilogramme.

**À justifier :** Une différence de pouvoir calorifique vient de la composition et de l’état de l’eau ; la récupération est une étape de procédé distincte.

### Échauffement adiabatique d’une réaction

Appliquer un bilan d’enthalpie à une réaction exothermique et prévoir l’effet d’une dilution.

**Objets et paramètres**

- ξ est l’avancement, en mol, de NO+½O₂→NO₂ ; il varie de 0 à 1 pour la charge initiale.
- Tᵢ est la température initiale, en K ; T est la température du mélange. nᵢ est la quantité d’inerte, en mol.
- Cp,total est la capacité thermique du mélange, en J·K⁻¹. f est la fraction de la chaleur réactionnelle cédée à l’extérieur.

**Repères** — Sup : calorimétrie et bilans de matière. Spé : température de réaction et enthalpie standard dépendant de T. Réacteur couplant équilibre, cinétique et transfert : les trois calculs seraient nécessaires à une prévision réelle.

1. Reprendre le preset du recueil : vérifier 400 K avec 93 % de chaleur cédée.
2. Mettre f=0 puis augmenter nᵢ sans changer les réactifs.
3. À ξ=0, vérifier T=Tᵢ ; à ξ=1, contrôler le bilan énergétique.

**À justifier :** L’inerte absorbe de la chaleur sans changer l’avancement imposé ; le bilan énergétique conserve les signes et les capacités thermiques.

## Séance 03 — Sup · relier potentiel et composition

### Pile Daniell : travail et quotient réactionnel

Associer tension, sens spontané, énergie de réaction et quantité d’électricité dans une pile.

**Objets et paramètres**

- E est la tension réversible de la pile, en V ; E° sa valeur standard. F=96485 C·mol⁻¹ est la constante de Faraday.
- aCu²⁺ et aZn²⁺ sont les activités sans dimension, assimilées à c/c°, c°=1 mol·L⁻¹. Q=aZn²⁺/aCu²⁺.
- T est en K ; nCu est la quantité de cuivre déposée, en mol. q est la charge passée, en C. Le bilan échange 2 mol d’électrons par mol de cuivre.

**Repères** — Sup : réaction redox et fonctionnement d’une pile. Spé : thermochimie électrochimique et énergie réversible. Piles réelles : activités, polarisation et capacité à établir avec les quantités initiales.

1. Avec activités égales, retrouver E=E°.
2. Diviser aCu²⁺ par 100 et vérifier la diminution de tension.
3. Pour nCu=0,1 mol, calculer q sans utiliser la tension.

**À justifier :** La tension dépend du quotient réactionnel ; la charge dépend de la stœchiométrie électronique et de la quantité transformée.

### Contrôle industriel : dosage d’un halogénure

Résoudre un dosage par précipitation sans approximation divergente à l’équivalence.

**Objets et paramètres**

- r=V/Véquiv est le volume titrant réduit. c est la concentration initiale de Br⁻ et celle du titrant Ag⁺, en mol·L⁻¹.
- Ks=10^−pKs est le produit de solubilité en activités réduites ; les concentrations sont assimilées aux activités.
- s est la quantité de AgBr solide par litre de mélange. E est le potentiel de l’électrode Ag⁺/Ag, avant soustraction éventuelle d’une référence.

**Repères** — Sup : bilan de titrage et précipitation. Spé : courbe potentiométrique et équilibres simultanés. Contrôle de bains industriels et estimation des incertitudes de mesure.

1. Avant l’équivalence, identifier l’ion en excès.
2. À r=1, retrouver [Ag⁺]=[Br⁻]=√Ks.
3. Après l’équivalence, vérifier les deux bilans avec la quantité de solide.

**À justifier :** La transition est rapide mais finie ; conserver simultanément Ks et les bilans évite une singularité artificielle à l’équivalence.

## Séance 04 — Spé · choisir une durée et un réacteur

### Arrêter au bon moment pour conserver l’intermédiaire

Chercher l’instant où un intermédiaire utile est le plus concentré, sans confondre disparition du réactif et rendement de cet intermédiaire.

**Objets et paramètres**

- A→B→C décrit deux étapes irréversibles du premier ordre. Les concentrations sont en mol·L⁻¹ ; A₀=1 mol·L⁻¹, B₀=C₀=0.
- k₁ et k₂ sont les constantes, en min⁻¹. t est le temps affiché en minutes.
- topt est l’instant qui maximise B ; la formation k₁A et la consommation k₂B sont en mol·L⁻¹·min⁻¹.

**Repères** — Sup : deux réactions du premier ordre et bilan de conservation. Spé : système linéaire, optimum et limite k₂→k₁. L’optimum de concentration n’intègre ni séparation, ni recyclage, ni coût de traitement.

1. Garder k₁=0,1 et k₂=0,04 min⁻¹ : repérer le pic de B.
2. Lire les deux vitesses à ce pic : elles sont égales.
3. Choisir k₁=k₂=0,1 min⁻¹ : vérifier la formule limite sans division par zéro.

**À justifier :** Il faut arrêter selon la grandeur visée : attendre plus longtemps peut consommer le produit intermédiaire.

### Choisir un temps de séjour et un réacteur

Passer d’une loi du premier ordre à un bilan de matière, puis comparer des organisations de réacteur à temps total égal.

**Objets et paramètres**

- A est le réactif, C₀ sa concentration d’entrée et C sa concentration de sortie, en mol·L⁻¹. X=1−C/C₀ est la conversion.
- k est la constante du premier ordre, en s⁻¹. τ est le séjour total affiché en minutes ; le calcul utilise 60τ secondes.
- N est le nombre entier de cuves identiques en série ; chacune a un séjour τ/N. Da=kτsecondes est le nombre de Damköhler, sans unité.

**Repères** — Sup : loi du premier ordre, bilan de matière et unités. Spé : bilans de la cuve agitée et du piston isotherme du premier ordre, au programme de chimie PC. La série de N cuves et sa limite sont des compléments guidés ; les autres filières peuvent aborder les bilans à partir des équations fournies.

1. Prendre k=0,01 s⁻¹ et τ=5 min ; calculer Da=3.
2. Comparer une cuve, trois cuves et un piston à ce séjour total.
3. Augmenter N sans changer τ : expliquer la convergence vers le piston.

**À justifier :** Une loi cinétique identique peut donner des conversions différentes selon l’organisation des écoulements.

## Séance 05 — Spé · conversion, pression et recyclage

### Ammoniac : température, pression et conversion

Séparer la conversion d’équilibre des contraintes de vitesse dans la synthèse de l’ammoniac.

**Objets et paramètres**

- ξ est l’avancement, en mol, de N₂+3H₂⇌2NH₃ ; la charge contient 1 mol N₂ et 3 mol H₂.
- T est la température en K ; P est la pression totale en bar ; nᵢ est l’inerte en mol. yⱼ=nⱼ/ntotal est la fraction molaire.
- aⱼ=yⱼP/p° est l’activité du gaz idéal, avec p°=1 bar. Q est le quotient réactionnel et K° la constante d’équilibre, tous deux sans dimension.

**Repères** — Sup : stœchiométrie et quotient réactionnel. Spé : thermochimie, équilibre et déplacement par T/P. Fugacités, recyclage et optimisation d’une boucle industrielle : nécessaires pour une prévision sous forte pression.

1. À P=100 bar, augmenter T et prévoir le sens de variation de la conversion.
2. À T fixé, augmenter P puis justifier le rôle de Δνgaz=−2.
3. Ajouter de l’inerte à P totale fixée et contrôler les pressions partielles.

**À justifier :** Basse température favorise ici l’équilibre mais peut ralentir la réaction ; le catalyseur améliore la vitesse sans modifier K°.

### CO₂ vers méthanol : rendement et recyclage

Relier la valorisation du CO₂ à un équilibre et à un bilan stationnaire de recyclage.

**Objets et paramètres**

- ξ est l’avancement de CO₂+3H₂⇌CH₃OH+H₂O. h est le rapport initial H₂/CO₂ ; T et P sont en K et bar.
- x est la fraction de CO₂ convertie par passage à l’équilibre. r est la fraction des réactifs non convertis recyclée après séparation des produits.
- Ffrais et Fcirculant sont des débits de CO₂ dans les mêmes unités ; X est la conversion globale du CO₂ frais.

**Repères** — Sup : tableau d’avancement et conservation du carbone. Spé : équilibre thermochimique et bilan d’une boucle. Fugacités, réactions concurrentes et analyse du cycle de vie : hors du calcul proposé.

1. Avec h=3 et r=0, comparer pression et conversion par passage.
2. Augmenter h : calculer la nouvelle borne ξmax avant de lire la carte.
3. À x fixé, comparer r=0 et r=0,9 ; observer aussi le débit circulant.

**À justifier :** Un recyclage peut augmenter la conversion globale tout en imposant plus de circulation ; convertir CO₂ ne suffit pas à conclure sur les émissions totales.

## Séance 06 — Spé · métaux, ciment et états physiques

### Extraire le zinc : trois états, deux réducteurs

Utiliser les changements d’état et les quotients de réaction pour choisir un réducteur du zinc.

**Objets et paramètres**

- T est en K. ΔrG° est l’enthalpie libre standard d’une réaction normalisée à une mole de O₂ dans la scène principale.
- H°Zn et S°Zn changent par ΔHtransition et ΔHtransition/Ttransition à la fusion puis à la vaporisation.
- Q est le quotient des activités de la réaction de réduction ; le réglage log₁₀ Q modifie ΔrG de RT ln Q. Les courbes de réduction sont par mole de Zn.

**Repères** — Sup : équilibrer les réactions et reconnaître un changement d’état. Spé : Ellingham, thermochimie et choix d’un réducteur. Pyrométallurgie réelle : cinétique, évacuation et condensation des vapeurs.

1. À 600, 900 puis 1400 K, identifier l’état du zinc.
2. Soustraire deux formations normalisées et retrouver ZnO+C→Zn+CO.
3. Diminuer log Q : prévoir le déplacement du domaine favorable.

**À justifier :** On compare des réactions équilibrées et des unités identiques ; un changement d’état modifie la pente sans rendre G discontinu.

### Ciment : calcination et capture du CO₂

Relier la pression du CO₂ au seuil de calcination et séparer émissions de procédé et chaleur réactionnelle.

**Objets et paramètres**

- T est en K ; pCO₂ est la pression partielle en bar, réduite par p°=1 bar dans le logarithme.
- m est la masse de CaCO₃, en kg ; M=100,086 kg·kmol⁻¹. n=m/M est donc en kmol.
- c est la fraction du CO₂ capturée ; elle change la sortie rejetée mais pas la stœchiométrie du carbonate.

**Repères** — Sup : stœchiométrie et calorimétrie. Spé : équilibre hétérogène et thermochimie industrielle. Clinker, captage et électrification des fours : leurs bilans détaillés sont hors du modèle.

1. À pCO₂=1 bar, calculer le seuil ΔH°/ΔS°.
2. Baisser pCO₂ et prévoir le signe de RT ln Q.
3. Pour 1000 kg de carbonate, comparer CO₂ produit, capturé et résiduel.

**À justifier :** Diminuer la pression de CO₂ favorise la calcination ; la capture change les émissions résiduelles mais conserve le carbone du bilan.

## Séance 07 — Spé · convertir l’énergie électrique et chimique

### Hydrogène : Faraday, tension et bilan énergétique

Distinguer production faradique, énergie électrique et échange de chaleur dans un électrolyseur.

**Objets et paramètres**

- I est le courant en A ; Δt la durée convertie en s ; U la tension d’une cellule en V.
- ηF est la fraction de charge utilisée pour produire H₂. nH₂=ηF IΔt/(2F) et MH₂=2,016 g·mol⁻¹.
- Erev=ΔG°/(2F) et Etn=ΔH°/(2F) sont les tensions réversible et thermoneutre. Qévacuée est positive si le système cède de la chaleur.

**Repères** — Sup : électrolyse et conversions de charge. Spé : distinction ΔH/ΔG et tensions énergétiques. Électrolyse haute température et pilotage par électricité variable.

1. À ηF=1, vérifier deux fois moins de O₂ que de H₂.
2. Fixer I et Δt, augmenter U : la quantité ne change pas, l’énergie oui.
3. À U bas, lire le signe de la chaleur nette et expliquer l’importation de chaleur.

**À justifier :** Faraday donne la quantité ; la tension fixe l’électricité par mole. ΔG et ΔH correspondent à deux contraintes énergétiques différentes.

### Pile à combustible : puissance et pertes

Comparer la tension utile, la puissance et le rendement d’une pile à combustible.

**Objets et paramètres**

- j est le courant par surface en A·cm⁻² ; j₀ est un courant d’échange effectif et jlim une limite de transport dans les mêmes unités.
- r est la résistance surfacique en Ω·cm². b=0,060 V est le coefficient d’activation global du modèle.
- U est la tension en V ; jU est la puissance par surface en W·cm⁻². ηPCS=U/Etn rapporte l’électricité à l’enthalpie du H₂ consommé.

**Repères** — Sup : redox et puissance électrique. Spé : polarisation, courant limite et bilan énergétique. Vieillissement, distribution d’eau et pilotage de piles de cellules.

1. À faible j, comparer les pertes d’activation et ohmiques.
2. Diminuer r, puis augmenter j₀ : identifier la perte modifiée.
3. Comparer le point de puissance maximale au point de meilleur rendement.

**À justifier :** Le point de puissance maximale impose une tension plus basse ; l’efficacité électrique ne croît pas avec la puissance délivrée.

## Séance 08 — Spé · stocker et déposer la matière

### Batterie : état de charge et énergie délivrée

Relier état de charge, occupation des sites, tension et énergie pendant une décharge.

**Objets et paramètres**

- s est l’état de charge sans dimension, limité ici à 0,05≤s≤0,95. θ− et θ+ sont les fractions de sites occupés dans les deux électrodes.
- C est la capacité nominale en Ah, I le courant de décharge en A et r la résistance en Ω. Une variation ds correspond à C ds en Ah.
- Uoc est la tension à vide ; U=Uoc−rI sous décharge. W=C∫U(s)ds est l’énergie en Wh, jusqu’au seuil s=0,05.

**Repères** — Sup : charge, puissance et bilans matière. Spé : thermodynamique électrochimique et énergie d’un accumulateur. Modèles d’intercalation non idéale, plateaux de phases et vieillissement.

1. À I=0, comparer Uoc pour trois valeurs de s.
2. Fixer s et augmenter I ; contrôler la chute rI et la puissance Joule rI².
3. Calculer la charge disponible jusqu’à 5 %, puis expliquer pourquoi W n’est pas toujours CΔs Uinitial.

**À justifier :** La charge compte les électrons transférables ; l’énergie dépend aussi de la tension tout au long de la décharge.

### Cuivrage : épaisseur, charge et transport

Passer de la charge à l’épaisseur et identifier la limitation par transport devant une cathode.

**Objets et paramètres**

- I est en A ; Δt est donné en min puis converti en s. S est la surface en cm² ; ρCu=8,96 g·cm⁻³.
- c∞ est la concentration de Cu²⁺ loin de la surface ; δ est l’épaisseur de diffusion en µm. D=7×10⁻¹⁰ m²·s⁻¹ est le coefficient de diffusion.
- Ilim=2FDc∞S/δ après conversion SI ; Iutile=min(I,Ilim). e est l’épaisseur de dépôt en µm.

**Repères** — Sup : bilan d’électrolyse et géométrie du revêtement. Spé : courant limite et diffusion. Rugosité, dendrites et électrodépôt à impulsions.

1. À faible I, vérifier que doubler le temps double l’épaisseur.
2. Augmenter I jusqu’au plateau : contrôler Iutile.
3. Diminuer δ pour représenter l’agitation et retrouver le profil de concentration.

**À justifier :** La charge utile gouverne l’épaisseur ; le courant total ne reste pas proportionnel au dépôt si le transport devient limitant.

## Séance 09 — Spé · protéger et sélectionner les métaux

### Corrosion : potentiel mixte et anode sacrificielle

Déterminer un potentiel mixte et comprendre comment une anode sacrificielle protège le fer.

**Objets et paramètres**

- E est le potentiel commun des métaux connectés, en V. jFe et jZn sont positifs pour la dissolution, négatifs pour une réduction nette.
- jO₂<0 est le courant cathodique d’oxygène et jlim>0 sa valeur limite, en mA·cm⁻². a=SZn/SFe est le rapport de surfaces.
- Le courant total, ramené à la surface du fer, est jFe+a jZn+jO₂. Une somme nulle définit le potentiel mixte au circuit ouvert.

**Repères** — Sup : oxydation du fer et sens du courant. Spé : potentiel mixte, limitation de transport et protection. Corrosion localisée et dimensionnement de la durée de vie du revêtement.

1. Avec a=0, repérer jFe=−jO₂ au potentiel mixte.
2. Connecter du zinc et prévoir le déplacement de E avant le calcul.
3. Diminuer jlim : relier l’apport d’oxygène à la perte du fer.

**À justifier :** Un potentiel standard ne donne pas seul une vitesse de corrosion ; les courants partiels et leurs surfaces déterminent le fonctionnement connecté.

### Hydrométallurgie : complexer pour changer la sélectivité

Relier une constante de complexation à un potentiel conditionnel et à la stabilité de Cu(I).

**Objets et paramètres**

- β₁ et β₂ sont les constantes des complexes Cu(I)+2NH₃ et Cu(II)+4NH₃. aNH₃ est l’activité du ligand libre.
- ctotal est la somme du cuivre libre et complexé pour un nombre d’oxydation donné. Le facteur L=1+βaNH₃^m relie ctotal et clibre.
- E1 et E2 sont les potentiels standard conditionnels Cu(I)/Cu et Cu(II)/Cu. Dans Frost, les points ont abscisse nombre d’oxydation et ordonnée nE°.

**Repères** — Sup : état d’oxydation et réaction de complexation. Spé : couplage complexation-redox et potentiels conditionnels. Séparation hydrométallurgique et optimisation multi-équilibres.

1. Avec peu de NH₃, retrouver approximativement les potentiels libres.
2. Augmenter NH₃ : comparer les deux chutes de potentiel.
3. Placer Cu(I) par rapport à la corde Cu(0)–Cu(II), puis calculer ΔG de dismutation.

**À justifier :** Une complexation stabilise une espèce dissoute et peut changer la stabilité relative des nombres d’oxydation ; il faut garder la pondération par les électrons.

## Séance 10 — Compléments · sites catalytiques et transport

### Une surface saturée peut ralentir la production

Relier les sites disponibles d’un catalyseur à la vitesse, puis comprendre saturation et compétition entre espèces.

**Objets et paramètres**

- pA et pB sont les pressions partielles en bar. KA et KB sont des constantes d’adsorption en bar⁻¹ ; leurs produits avec les pressions sont sans unité.
- θA, θB et θlibre sont les fractions de sites occupés par A, par B ou libres ; leur somme vaut 1.
- Seul A adsorbé se transforme. kcat=1 s⁻¹ est fixé ; vsite=kcatθA est une vitesse par site, en s⁻¹.

**Repères** — Sup : équilibre, fractions et comparaison de vitesses. Spé : mécanisme apparent et ordre local dépendant des conditions. Langmuir compétitif est un modèle fourni ; les surfaces réelles peuvent présenter plusieurs types de sites.

1. Avec pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, calculer les trois fractions.
2. Supprimer B : comparer la disponibilité des sites et la vitesse.
3. Augmenter pA : observer la saturation sans dépasser kcat.

**À justifier :** La pression accélère à faible occupation ; elle n’augmente pas indéfiniment une vitesse limitée par les sites.

### Un catalyseur poreux ne travaille pas toujours partout

Comprendre pourquoi les sites au centre d’un grain poreux peuvent manquer de réactif, même si la chimie intrinsèque est rapide.

**Objets et paramètres**

- R est le rayon du grain, affiché en µm et converti en m ; r est la distance au centre et ρ=r/R la coordonnée réduite.
- Deff est la diffusivité effective, en m²·s⁻¹ ; k est la constante du premier ordre, en s⁻¹.
- C est la concentration dans le grain et Cs celle imposée à sa surface. La carte représente C/Cs, sans unité.
- φ=R√(k/Deff) est le module de Thiele ; η est le rapport de la consommation réelle à celle d’un grain partout à Cs.

**Repères** — Sup : diffusion, temps caractéristique et premier ordre. Spé : couplage réaction−diffusion et étude asymptotique. Le module de Thiele et le facteur d’efficacité sont des compléments de génie chimique, explicités dans le TP.

1. Avec R=500 µm, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹, calculer φ.
2. Réduire le rayon sans changer k : observer la remontée de C au centre.
3. Choisir la diffusion limitante et comparer η au profil du grain.

**À justifier :** Une grande surface interne n’assure pas que tous les sites travaillent ; la diffusion doit alimenter la réaction.

## Séance 11 — Spé et complément thermique · mécanisme et stabilité

### Une chaîne radicalaire produit un ordre non entier

Reprendre le mécanisme radicalaire p.549–550, garder les termes d’amorçage et de propagation, puis discuter l’ordre non entier.

**Objets et paramètres**

- E désigne l’éthanal CH₃CHO ; c=[E] est sa concentration, en mol·L⁻¹. Le point · indique un radical.
- k₁ est la constante d’amorçage, en s⁻¹ ; k₅ et k₆ celles de propagation et terminaison, en L·mol⁻¹·s⁻¹.
- vE est la vitesse de disparition d’E, en mol·L⁻¹·s⁻¹. L=vE/(k₁c) est la longueur de chaîne selon la définition du recueil.
- nlocal=d ln(vE)/d ln c est l’ordre local ; Eapp est l’énergie apparente locale, en kJ·mol⁻¹.

**Repères** — Sup : vitesse, mécanisme et bilan de matière. Spé : mécanismes en chaîne, AEQS et régime de propagation dominante. La validation dynamique de l’AEQS demande des échelles de temps ; un petit taux de radicaux ne suffit pas à la démontrer.

1. Avec les réglages par défaut, vérifier que l’ordre local est proche de 1,47 et non exactement 3/2.
2. Choisir le préréglage où l’amorçage devient plus visible : observer l’ordre qui se rapproche de 1.
3. Lire le tableau : vérifier les conservations du carbone, de l’hydrogène et de l’oxygène.

**À justifier :** L’ordre 3/2 et l’énergie 201 kJ·mol⁻¹ décrivent un régime dominant, pas tous les réglages possibles.

### Chaleur produite et chaleur évacuée : quel équilibre ?

Coupler une vitesse d’Arrhénius à un bilan thermique. Comprendre pourquoi une température d’équilibre peut être stable ou instable.

**Objets et paramètres**

- T est la température du milieu et Ta celle du fluide extérieur, en K. qref est la puissance produite à 300 K, en W·L⁻¹.
- Ea est l’énergie d’activation en kJ·mol⁻¹ ; R est la constante des gaz parfaits. h est le coefficient d’évacuation, en W·L⁻¹·K⁻¹.
- Cth=100 J·L⁻¹·K⁻¹ est la capacité thermique volumique fixée. T₀ est la température initiale.
- Le bilan F(T)=q(T)−h(T−Ta) est une puissance volumique ; sa dérivée classe les équilibres simples.

**Repères** — Sup : premier principe et évolution d’une température. Spé : rétroaction cinétique, linéarisation et stabilité. La prévention d’un emballement réel exige un modèle et des données adaptés ; l’atelier étudie seulement le bilan didactique annoncé.

1. Avec les réglages par défaut, repérer les deux intersections et lire leurs stabilités.
2. Passer de T₀=300 à 350 K sans changer l’appareil : comparer les trajectoires.
3. Réduire h puis lire l’état du calcul ; distinguer sortie du domaine et température finale atteinte.

**À justifier :** La température accélère la production ; l’évacuation doit être comparée à cette accélération, pas seulement à une puissance initiale.

## Séance 12 — Spé · séparer et solidifier un mélange

### Distillation : liquide, vapeur et règle du levier

Lire les compositions coexistantes et calculer la proportion de vapeur à partir d’un bilan.

**Objets et paramètres**

- z est la fraction molaire globale de B ; xL est celle dans le liquide et yV celle dans la vapeur.
- p*A et p*B sont les pressions de vapeur des corps purs à la température fixée, en bar. α=p*B/p*A>1 mesure la volatilité relative.
- β est la fraction molaire de vapeur parmi les deux phases ; P est la pression totale.

**Repères** — Sup : fractions molaires et bilans de matière. Spé : diagrammes binaires et distillation. Dimensionnement d’une colonne et azéotropes : prolongements après le modèle idéal.

1. Au preset deux phases, vérifier xL<z<yV.
2. Augmenter P : identifier la disparition de la vapeur.
3. Fixer z et augmenter α : comparer enrichissement et fraction vapeur.

**À justifier :** La vapeur est enrichie en B, le plus volatil ; la règle du levier conserve la composition globale.

### Solidification : composition et fraction solide

Distinguer composition d’une phase et quantité de cette phase pendant la solidification.

**Objets et paramètres**

- z est la fraction molaire globale de B ; xL et xS sont ses fractions dans le liquide et le solide.
- T est en K ; Tf,i et ΔHfus,i sont température et enthalpie molaire de fusion de chaque corps pur.
- fS est la fraction molaire de solide. Le liquidus donne xL(T), le solidus xS(T) lorsque les phases coexistent.

**Repères** — Sup : bilan de composition et changements d’état. Spé : équilibres de phases et diagrammes d’alliages. Thermodynamique des solutions non idéales et solidification hors équilibre.

1. À z=0,5, refroidir de 1800 à 1300 K ; repérer les trois domaines.
2. Dans le fuseau, comparer xL, z et xS.
3. Vérifier z=(1−fS)xL+fSxS, puis comparer au Mg–Ni du recueil.

**À justifier :** La composition des cristaux diffère de celle du liquide ; les proportions se calculent par un bilan, pas par la hauteur des courbes.
