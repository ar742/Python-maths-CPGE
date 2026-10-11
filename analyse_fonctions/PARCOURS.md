# Quatorze séances d’analyse

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le théorème adapté.

## Séance 01 — Intégrales à paramètre · p. 63

### Théorème 1 : continuité d’une transformée gaussienne

Vérifier les hypothèses du théorème de continuité sous l’intégrale, puis calculer une intégrale gaussienne et retrouver un résultat de Fourier.

**Objets et paramètres**

- a : paramètre réel ; t : variable intégrée sur ℝ ; f(a,t)=e⁻ᵗ²cos(at) : intégrande ; F(a) : son intégrale.
- φ(t)=e⁻ᵗ² : majorant intégrable, indépendant de a ; L : borne de coupure numérique sur [−L,L].

**Repères** — Sup : MPSI : majorations et intégration sur un segment ; passage à une intégrale sur ℝ introduit ici. Spé : Continuité et dérivation d’intégrales à paramètre. Au-delà : Transformée de Fourier de la gaussienne et bornes de quadrature.

1. Choisir a=0 : vérifier l’intégrale gaussienne.
2. Augmenter a : les oscillations restent dans la même enveloppe.
3. Réduire L puis comparer l’écart observé à la borne totale annoncée.

**À justifier :** Le majorant global prouve la continuité sur ℝ. La compensation réduit F sans invalider la majoration de l’intégrande.

### Théorème 1 : une masse qui se concentre interdit le passage à la limite

Comprendre pourquoi la convergence ponctuelle ne suffit pas pour passer une limite sous une intégrale.

**Objets et paramètres**

- a>0 : largeur et échelle du pic ; t>0 : variable intégrée ; fₐ(t)=e⁻ᵗ/ᵃ/a : intégrande.
- F(a)=1 : intégrale complète pour a>0 ; f₀=0 et F(0)=0 ; ε : largeur de la fenêtre près de 0 ; L : borne visible.

**Repères** — Sup : Exponentielle, changement de variable et masse sous une courbe. Spé : Hypothèses du théorème de continuité et contre-exemple. Au-delà : Concentration, convergence L¹ et approximations de masses ponctuelles.

1. Diminuer a en gardant ε fixe : mesurer la masse dans [0,ε].
2. Faire aussi ε=a et constater la fraction 1−e⁻¹.
3. Lire l’enveloppe 1/(et) et vérifier la divergence de son intégrale près de 0.

**À justifier :** Le pic s’efface à chaque point fixé, mais son aire reste égale à 1. Le majorant manquant explique exactement l’échec de la continuité en a=0.

## Séance 02 — Intégrales à paramètre · p. 63

### Théorème 2 : Frullani, un logarithme retrouvé par dérivation

Calculer une intégrale compensée en dérivant un paramètre, puis fixer sa constante par une valeur simple.

**Objets et paramètres**

- a,b>0 : taux de décroissance ; t≥0 : variable intégrée ; F(a,b) : intégrale de (e⁻ᵃᵗ−e⁻ᵇᵗ)/t.
- L : coupure haute ; le quotient est prolongé par b−a en 0 ; on dérive en a en maintenant b fixé.

**Repères** — Sup : MPSI : développements limités, logarithme et intégrales sur un segment ; coupures finies de l’intégrale. Spé : Dérivation d’une intégrale à paramètre et constante d’intégration. Au-delà : Stabilité numérique d’une différence d’exponentielles.

1. Choisir a=1,b=2 : retrouver ln 2.
2. Choisir a=b : l’intégrale est nulle, mais sa dérivée en a ne l’est pas.
3. Réduire a et L : lire la borne de queue puis augmenter L.

**À justifier :** La dérivation simplifie l’intégrande. La condition F(b,b)=0 est indispensable pour retrouver ln(b/a).

### Théorème 2 : transformer une intégrale oscillante en arctangente

Transformer une intégrale oscillante en une EDO et comprendre la portée locale du théorème de Leibniz.

**Objets et paramètres**

- a>0 : amortissement ; t≥0 : variable intégrée ; F(a) : intégrale de e⁻ᵃᵗsin(t)/t, prolongé par 1 en 0.
- L : coupure haute ; F′(a)=−1/(1+a²) : dérivée exacte ; e⁻⁽ᵃ/²⁾ᵗ : majorant local de la dérivée de l’intégrande.

**Repères** — Sup : Exponentielles complexes et intégration par parties. Spé : Leibniz, EDO en paramètre et limite à l’infini. Au-delà : Limite d’Abel de l’intégrale de Dirichlet.

1. Choisir a=1 : comparer intégrale et π/4.
2. Diminuer a tout en gardant L fixe : vérifier la borne de la queue.
3. Augmenter L puis expliquer pourquoi le calcul pour a=0 n’est pas justifié par le même majorant.

**À justifier :** Pour a>0, F(a)=arctan(1/a). Un résultat au bord du domaine demande une justification supplémentaire.

## Séance 03 — Intégrales à paramètre · p. 63

### Théorème 3 : dérivées de Γ, moments logarithmiques et convexité

Justifier les dérivations successives d’une intégrale, puis utiliser Cauchy–Schwarz pour démontrer la convexité du logarithme de gamma.

**Objets et paramètres**

- a>0 : paramètre de Γ ; t>0 : variable intégrée ; n≥0 : ordre entier de dérivation.
- u=ln t : variable du tracé ; q : exposant de la coupure basse ε=10⁻ᑫ ; T : coupure haute.
- Γ⁽ⁿ⁾ : intégrale de tᵃ⁻¹e⁻ᵗ(ln t)ⁿ ; la dérivée seconde de ln Γ est la variance de ln t sous la loi gamma.

**Repères** — Sup : MPSI : récurrence et intégration par parties ; valeurs de gamma aux entiers présentées avec une coupure. Spé : Dérivation à plusieurs ordres et inégalité de Cauchy–Schwarz. Au-delà : Fonctions digamma et trigamma, moments d’une loi gamma.

1. Choisir n=2,a=2 et comparer les moments à la variance positive.
2. Descendre a à 0,6 : voir l’importance de la queue basse en u.
3. Augmenter q et T : comparer les bornes des queues et l’indicateur de quadrature.

**À justifier :** Γ est C∞ sur ]0,+∞[. Sa log-convexité résulte d’un moment quadratique ; chaque passage sous l’intégrale a un majorant local explicite.

### Théorème 3 : dérivées de Laplace et monotonie complète

Contrôler plusieurs dérivations par un majorant commun et mesurer une troncature avec une queue exacte.

**Objets et paramètres**

- a>0 : paramètre ; t≥0 : variable intégrée ; n≥0 : ordre entier de dérivation ; F(a)=∫₀∞e⁻ᵃᵗdt.
- tⁿe⁻ᵃᵗ : intégrande positive, de maximum en t=n/a ; L : borne de troncature.
- F⁽ⁿ⁾=(−1)ⁿn!/aⁿ⁺¹ : dérivée exacte. Les valeurs tracées et les queues permettent de contrôler le calcul.

**Repères** — Sup : Exponentielle, dérivées successives et intégration par parties. Spé : MP : dérivations successives d’intégrales à paramètre ; Laplace fournit l’application. Au-delà : Monotonie complète et représentations par une densité positive.

1. Choisir n=4,a=1 et retrouver 24.
2. Choisir n=8,a=0,25,L=12 : voir le maximum sortir de la fenêtre.
3. Augmenter L et mesurer la proportion capturée, au lieu de conclure à partir du dessin seul.

**À justifier :** Les dérivées alternent de signe et leur valeur absolue est un moment positif. Les maxima et les queues expliquent les choix de coupure numérique.

## Séance 04 — C · Équations différentielles

### Euler et RK4 : mesurer un ordre de convergence

Résoudre l’équation du TP p. 69, puis mesurer comment l’erreur d’Euler et de Runge–Kutta diminue quand on affine le pas.

**Objets et paramètres**

- x : abscisse sans dimension (argument du cosinus en radians) ; y(x) : fonction recherchée ; y₀=y(0) : donnée initiale.
- L’équation est y′=f(x,y), avec f(x,y)=cos(x)(y+1). Sa solution exacte est y(x)=(1+y₀)e^{sin x}−1.
- T : abscisse finale ; N : nombre de pas ; h=T/N : longueur du pas.
- E : erreur maximale aux points calculés par rapport à la solution exacte ; RK4 : méthode de Runge–Kutta à quatre étapes.

**Repères** — Sup : Retrouver la solution ; pour y₀=0, étudier y=e^{sin x}−1 et ses extrema. Spé : Comparer Euler à RK4, distinguer erreur locale et globale. Au-delà : Contrôle d’erreur et choix d’une méthode sur des EDO sans solution exacte.

1. Choisir le TP et suivre les pentes sur la solution exacte.
2. Choisir le pas grossier puis augmenter N.
3. Lire les ordres mesurés ; vérifier pourquoi diviser le pas par 2 ne produit pas le même gain pour Euler et RK4.

**À justifier :** Justifier l’ordre observé, annoncer la référence utilisée et séparer précision et présentation du graphique.

### Facteur intégrant : transformer une EDO en intégrale

Transformer une équation différentielle linéaire en intégrale définie, puis interpréter la mémoire et la sensibilité.

**Objets et paramètres**

- x : variable ; y(x) : inconnue ; y₀ : valeur en 0. Tous les paramètres sont sans dimension.
- L’équation est y′+(a+bx)y=Fcos(ωx) : a,b règlent le coefficient de y ; F et ω règlent l’amplitude et la pulsation du second membre.
- A(x)=ax+bx²/2 : primitive du coefficient ; eᴬ : facteur intégrant ; les deux préparations ont un écart initial de 1.

**Repères** — Sup : Construire le facteur intégrant en vérifiant son signe. Spé : Interpréter le noyau et démontrer la décroissance de l’écart. Au-delà : Mémoire d’un système linéaire à coefficient variable.

1. Choisir la relaxation constante et retrouver l’exponentielle.
2. Choisir le coefficient variable et examiner le noyau par l’écart initial.
3. Mettre a=b=F=0 puis expliquer pourquoi les deux solutions restent constantes et distinctes.

**À justifier :** Reconstruire la formule intégrale avec la bonne constante et relier sa dérivée à l’EDO.

## Séance 05 — C · Équations différentielles

### Une condition initiale ne suffit pas toujours

Trouver plusieurs solutions pour une même donnée initiale et voir quelle hypothèse garantit l’unicité dans un autre problème.

**Objets et paramètres**

- t : temps réduit ; y(t) : inconnue ; τ : instant de départ d’une solution en attente de y′=2√|y|, avec y(0)=0.
- λ : coefficient de l’autre équation, y′=λy ; ε : écart initial entre ses deux solutions.
- Une constante de Lipschitz bornerait le quotient des écarts du second membre par ceux des arguments ; 2/√ε devient non borné près de 0.

**Repères** — Sup : Vérifier directement chaque solution et chaque donnée initiale. Spé : Séparer unicité et stabilité ; expliquer le contre-exemple. Au-delà : Existence locale, conditions de Lipschitz et limites d’une simulation.

1. Changer τ : noter que la donnée initiale ne change jamais.
2. Lire le quotient pour de petits ε.
3. Passer λ de −1 à 1 : expliquer pourquoi une divergence de deux préparations ne réfute pas l’unicité.

**À justifier :** Savoir expliquer pourquoi un calcul partant de zéro peut sélectionner une solution sans démontrer son unicité.

### Solution maximale : explosion ou saturation

Calculer jusqu’à quel instant une solution existe, puis comparer une croissance qui explose à une croissance qui se stabilise.

**Objets et paramètres**

- t : temps réduit ; y₀>0 : valeur initiale commune ; a>0 : coefficient de y′=ay².
- t*=1/(ay₀) : temps d’explosion ; le curseur donne la fraction de ce temps observée, strictement inférieure à 1.
- r>0 : taux logistique ; K>0 : niveau d’équilibre du modèle y′=ry(1−y/K).

**Repères** — Sup : Résoudre les deux équations et lire leurs tableaux de variations. Spé : Relier saturation et stabilité ; distinguer solution locale et globale. Au-delà : Solution maximale, explosion et contrôle a priori.

1. Comparer les deux modèles au réglage initial.
2. Approcher la fraction 0,95 et suivre la droite 1/y.
3. Partir au-dessus de K ; prévoir le sens d’évolution logistique avant le calcul.

**À justifier :** Nommer un intervalle maximal et justifier la saturation par le second membre, sans confondre les deux notions.

## Séance 06 — C · Équations différentielles

### Oscillateur : transitoire, résonance et travail

Relier l’équation d’ordre 2, ses deux données initiales et les applications physiques de la résonance.

**Objets et paramètres**

- t : temps ; y : position ; y′ : vitesse ; y₀,y′₀ : les deux données initiales. Le modèle utilise une masse unité et des unités réduites.
- ω₀ : pulsation propre ; ω : pulsation imposée ; ζ : amortissement réduit ; F : amplitude du forçage Fcos(ωt).
- E=[(y′)²+ω₀²y²]/2 : énergie réduite ; W : travail du forçage ; D : énergie dissipée. La durée est réglée en périodes propres.

**Repères** — Sup : Identifier les trois régimes libres et ajuster les constantes. Spé : Calculer l’amplitude et sa résonance, vérifier le travail. Au-delà : Réponse impulsionnelle et interprétation spectrale.

1. Choisir le cas critique puis le cas apériodique libre.
2. Comparer la résonance amortie à la résonance sans amortissement.
3. Doubler la durée sans amortissement : expliquer la croissance du maximum et contrôler E−E₀=W−D.

**À justifier :** Énoncer quand une amplitude stationnaire a un sens et quand le temps d’observation fait partie du résultat.

### Variation des constantes : un noyau de Green initial

Résoudre l’exercice 1 p. 71 : construire une solution particulière, puis ajuster les deux données initiales.

**Objets et paramètres**

- x : variable ; y₀=y(0),v₀=y′(0) : données initiales ; le curseur amplitude multiplie g(x)=eˣ/cosh²x.
- e²ˣ,e³ˣ : modes homogènes ; W=e⁵ˣ : leur Wronskien (déterminant des fonctions et de leurs dérivées).
- a(x),b(x) : coefficients variables de la particulière à données initiales nulles ; tous les paramètres sont sans dimension.

**Repères** — Sup : Identifier la base homogène et les deux conditions initiales. Spé : Construire a′,b′ puis le noyau intégral. Au-delà : Convolution, réponse impulsionnelle et transformée de Laplace.

1. Calculer la particulière à données nulles et comparer ses deux coefficients.
2. Ajouter la solution homogène de donnée y₀=1,v₀=2.
3. Supprimer le second membre : vérifier le mode e^{3x} puis examiner l’écart Gauss/RK4.

**À justifier :** Retrouver le signe des coefficients et expliquer pourquoi une particulière doit encore être ajustée au problème initial.

## Séance 07 — C · Équations différentielles

### Euler–Cauchy : singularités et série entière

Résoudre l’exercice 2 p. 71 sur les bons intervalles, puis comparer la formule exacte à sa série entière près de zéro.

**Objets et paramètres**

- x : variable ; y(x) : inconnue ; ±1 : pôles du second membre ; 0 : zéro du coefficient de y″.
- C₁,C₂ : constantes des modes C₁x,C₂/x ; la branche régulière impose C₂=0.
- N : nombre de termes de la série particulière ; l’écart réglé éloigne des abscisses singulières. La série est comparée sur [0,1−écart].

**Repères** — Sup : Repérer les points où une formule ou une division demande une précaution. Spé : Construire la série, les modes et le prolongement analytique. Au-delà : Points singuliers réguliers et méthode de Frobenius.

1. Choisir le prolongement régulier et vérifier le comportement x²/3 près de 0.
2. Activer le mode 1/x sur un intervalle évitant 0.
3. Approcher x=1 puis augmenter le nombre de termes ; comparer convergence de la série et singularité du problème.

**À justifier :** Donner la solution avec son intervalle et distinguer un faux 0/0 d’un véritable mode singulier.

### EDO homogène et Riccati : deux changements de fonction

Comparer deux substitutions classiques en surveillant leurs domaines de validité.

**Objets et paramètres**

- x : variable de l’exercice 3 ; y(x) : inconnue ; c>0 : constante de la famille y=cx²−1/(4c). Le changement z=y/x exclut 0.
- Dans l’expérience Riccati distincte, t est la variable et z₀=z(0) la donnée de z′=z²−1.
- u(t) : fonction auxiliaire ; z=−u′/u exige u≠0. La durée demandée est arrêtée avant un pôle.

**Repères** — Sup : Vérifier directement la famille et sa valeur en 0. Spé : Retrouver les changements et les signes dans la racine. Au-delà : EDO de Riccati, pôles et réduction à une équation linéaire.

1. Changer c et observer le raccordement en 0.
2. Choisir z₀=−1 puis z₀=1 : vérifier les équilibres de Riccati.
3. Choisir z₀=1,5 ; rapprocher le pôle de Riccati du zéro de u.

**À justifier :** Nommer correctement l’équation et expliciter les points où le changement de fonction cesse d’être valable.

## Séance 08 — C · Équations différentielles

### Trois réservoirs : conservation, modes et exponentielle

Passer de bilans concrets à un système de dimension 3 et utiliser ses modes pour expliquer l’évolution.

**Objets et paramètres**

- t : temps réduit ; Yᵢ : quantité du réservoir i ; S=Y₁+Y₂+Y₃ : total ; Pᵢ=Yᵢ/S : proportion.
- kᵢⱼ : taux d’échange symétriques positifs ; δ : taux de perte commun ; A : matrice des trois bilans Y′=AY.
- Une quantité totale de 1 est placée dans le réservoir choisi. Le triangle des proportions utilise P₁,P₂ et P₃=1−P₁−P₂.

**Repères** — Sup : Écrire les trois bilans et vérifier la quantité totale. Spé : Calculer les modes et interpréter le taux lent. Au-delà : Réseaux de diffusion et générateurs conservant la positivité.

1. Choisir des échanges symétriques et retrouver les deux modes de taux 3k.
2. Ralentir un échange et comparer les temps propres.
3. Introduire une perte : comparer les quantités et les proportions au temps final.

**À justifier :** Associer chaque valeur propre à un bilan ou à une relaxation et conserver le sens du troisième réservoir.

### Deux bords : existence, unicité et résonance

Imposer la valeur d’une solution en deux points et déterminer quand il existe une solution unique, aucune ou une infinité.

**Objets et paramètres**

- x∈[0,π] : variable ; y(x) : inconnue, avec y(0)=y(π)=0 ; a,b : amplitudes du second membre a sin x+b sin(2x).
- λ : coefficient de y dans y″+λy=f ; f : second membre. Pour un entier n≥1, λ=n² est une valeur résonante.
- C : amplitude libre du mode sin(nx), utilisée seulement à la résonance compatible.

**Repères** — Sup : Résoudre l’homogène et comparer données au même point / deux points. Spé : Établir la condition intégrale et classer unique / aucune / infinité. Au-delà : Alternative de Fredholm, fonctions de Green et problèmes spectraux.

1. Choisir λ=2 : vérifier la solution unique.
2. Choisir la résonance incompatible : interpréter le résidu.
3. Rendre le second membre compatible puis varier l’amplitude libre sans modifier l’équation ni les bords.

**À justifier :** Vérifier la compatibilité avant de conclure à une solution et démontrer pourquoi l’unicité de Cauchy ne suffit pas ici.

## Séance 09 — Équations fonctionnelles

### Cauchy : une équation à deux variables détermine une droite

Résoudre une équation fonctionnelle par substitutions, puis comprendre le rôle exact de la continuité.

**Objets et paramètres**

- x,y : arguments réels indépendants ; f : fonction testée ; a : pente de la solution f(x)=ax.
- b : amplitude de la perturbation sinusoïdale ; R(x,y)=f(x+y)−f(x)−f(y) : défaut d’égalité affiché dans chaque case.

**Repères** — Sup : Valeurs particulières, parité, récurrence et continuité. Spé : Comparaison de preuves par densité et par dérivation. Au-delà : Solutions additives sans hypothèse de régularité.

1. Choisir b=0 et voir le résidu presque nul aux arrondis près.
2. Ajouter b=0,1 et comparer la faible perturbation de la courbe au défaut de la carte.
3. Tester à la main le couple x=y=π/2, puis lire la preuve de classification.

**À justifier :** La continuité prolonge la linéarité des rationnels aux réels. Un seul contre-exemple rejette une fonction ; des tests finis ne prouvent pas l’identité.

### Produit, logarithme, puissance : changer de variable pour résoudre

Transformer les produits en sommes et retrouver le logarithme ou les puissances en justifiant chaque changement de variable.

**Objets et paramètres**

- x,y>0 : arguments ; u=ln x,v=ln y : axes de la carte ; f : fonction testée.
- a : coefficient du logarithme ou exposant de la puissance, selon l’équation ; b : amplitude du défaut en ln x ou dans l’exposant.

**Repères** — Sup : Logarithme, exponentielle et changement de variable. Spé : Classification, dérivation et EDO xf′=af. Au-delà : Rôle des hypothèses de régularité dans les morphismes.

1. Choisir le logarithme exact, puis interpréter une case en revenant à x=eᵘ et y=eᵛ.
2. Passer à la puissance avec a=−1 et vérifier f(xy)=f(x)f(y).
3. Activer une perturbation et trouver un couple qui invalide le candidat.

**À justifier :** Le logarithme convertit une structure multiplicative en une structure additive. Le domaine positif et la positivité de f sont des étapes de preuve.

## Séance 10 — Équations fonctionnelles

### D’Alembert : pourquoi apparaissent cosinus et cosinus hyperbolique ?

Faire apparaître une équation différentielle dans une équation fonctionnelle et conserver les conditions initiales.

**Objets et paramètres**

- x,y : arguments réels ; f : fonction testée ; k : fréquence du cosinus ou taux du cosinus hyperbolique.
- λ : coefficient de l’équation f″=λf pour les familles exactes ; b : coefficient de la perturbation bx², qui conserve la parité.

**Repères** — Sup : Parité, identités trigonométriques et hyperboliques. Spé : Équation différentielle linéaire et unicité du problème initial. Au-delà : Subdivisions dyadiques et polynômes de Chebyshev.

1. Comparer les deux familles exactes avec le même k.
2. Choisir la solution nulle et identifier l’étape de preuve qui change.
3. Ajouter b=0,1 : la parité persiste, mais les résidus fonctionnel et différentiel révèlent le défaut.

**À justifier :** Les substitutions fournissent des conditions nécessaires. L’EDO et ses conditions initiales donnent les candidats, puis les formules d’addition valident la réciproque.

### Substituer −x : identifier une fonction sans la deviner

Utiliser une substitution adaptée pour calculer f(x) et f(−x) sans présupposer une forme de solution.

**Objets et paramètres**

- x≠0 : argument ; f(x),f(−x) : deux inconnues d’un système linéaire obtenu par substitution.
- b : amplitude du défaut b sin x ; R>0 : étendue visible |x|≤R.

**Repères** — Sup : Systèmes, symétrie, parité et étude de fonction. Spé : Stratégies de substitutions −x, 1/x et échanges de variables. Au-delà : Propagation des défauts près d’un point exclu du domaine.

1. Choisir b=0 et retrouver les valeurs f(1)=1, f(−1)=0.
2. Comparer la partie paire et la partie impaire à la solution totale.
3. Ajouter un petit b et observer que le résidu ne s’annule pas près de 0.

**À justifier :** Le système détermine une unique solution sur le domaine. En 0, seule une demande de prolongement continu impose la valeur 0.

## Séance 11 — Fonctions spéciales

### Gamma : prolonger la factorielle et contrôler une intégrale impropre

Définir une fonction par une intégrale impropre, reconnaître son domaine et utiliser une intégration par parties pour retrouver la factorielle.

**Objets et paramètres**

- x>0 : argument de Γ ; t>0 : variable intégrée, distincte de x ; Γ(x) : intégrale complète de t^(x−1)e^(−t).
- T : borne haute de troncature ; on étudie séparément le noyau près de 0 et à l’infini.

**Repères** — Sup : MPSI : équivalents, intégration sur un segment et récurrence ; l’intégrale impropre est introduite ici. Spé : Fonction définie par une intégrale et dérivation sous le signe intégral. Au-delà : Log-convexité et caractérisation de gamma.

1. Choisir x=1/2 : identifier la singularité en 0 sans conclure à la divergence.
2. Choisir x=5 et comparer Γ(5) à 4!.
3. Choisir x=8, T=5, puis augmenter T : interpréter la part de l’aire retenue.

**À justifier :** L’intégrale existe pour x>0 ; sa relation fonctionnelle est démontrée, et la queue de l’intégrale explique un écart même si la quadrature est précise.

### Bêta : un changement de variables relie deux intégrales

Faire apparaître bêta par un changement de variables et employer le rapport gamma pour calculer des moments ou des intégrales trigonométriques.

**Objets et paramètres**

- a,b>0 : paramètres ; t∈[0,1] : variable de proportion ; B(a,b) : intégrale qui normalise t^(a−1)(1−t)^(b−1).
- u,v>0 : variables auxiliaires du changement ; r=u+v : leur somme ; moyenne et variance : moments de la densité normalisée.

**Repères** — Sup : Symétrie, puissances, moments et changement trigonométrique. Spé : Lien gamma-bêta, normalisation et récurrences. Au-delà : Changement de variables dans le quadrant et famille de lois bêta.

1. Choisir a=b=1 : retrouver la densité uniforme.
2. Comparer (2,5) et (5,2) : observer la réflexion autour de 1/2.
3. Choisir a=b=1/2, puis a=b=4 : distinguer singularités intégrables et concentration au centre.

**À justifier :** Les deux paramètres ont des rôles symétriques ; le facteur jacobien r fait apparaître exactement Γ(a+b), et non une autre valeur de gamma.

## Séance 12 — Fonctions spéciales

### Zêta : une somme approchée n’est pas encore une valeur certifiée

Donner une approximation accompagnée d’un encadrement et comprendre pourquoi la convergence devient difficile près de s=1.

**Objets et paramètres**

- s>1 : exposant de la série de Riemann ; n≥1 : indice ; ζ(s) : somme de 1/nˢ.
- N : nombre de termes ; S_N : somme finie ; R_N=ζ(s)−S_N : reste positif, encadré par deux intégrales.

**Repères** — Sup : MPSI : sommes finies, suites et comparaison à une intégrale ; entrée guidée vers les séries. Spé : MP : séries de Riemann, encadrement du reste, continuité et dérivation des séries de fonctions. Au-delà : Accélération Euler–Maclaurin et singularité de bord.

1. À s=2, augmenter N puis comparer S_N à π²/6.
2. Passer à s=1,1 avec N=4000 : lire le reste, pas seulement le dernier terme.
3. À s=3/2, doubler N et comparer la diminution du reste à 2^(1−s).

**À justifier :** Une série peut converger très lentement. Le reste se contrôle par des intégrales ; choisir un compact évite d’oublier le bord du domaine.

### Zêta et gamma : de la série à une intégrale de Planck

Justifier le passage d’une série à une intégrale et relier un changement d’échelle à une loi physique en température.

**Objets et paramètres**

- s>1 : paramètre ; t≥0 : variable sans dimension ; Γ(s)ζ(s) : valeur de l’intégrale de t^(s−1)/(eᵗ−1).
- T : borne numérique de troncature, distincte de T_phys, température absolue de l’application au rayonnement.

**Repères** — Sup : Équivalents, convergence et changements de variable. Spé : Interversion série–intégrale et fonctions définies par intégrale. Au-delà : Rayonnement thermique et rôle de la dimension dans les lois de température.

1. Choisir s=4 : comparer la valeur à π⁴/15.
2. Choisir s=1,2 : repérer où se concentre la difficulté d’intégration.
3. Choisir s=6 et T=5, puis augmenter T : distinguer le problème en 0 de la queue à l’infini.

**À justifier :** La positivité justifie l’interversion ; s>1 vient du voisinage de 0. Le changement de fréquence fournit une puissance de température sans nouveau calcul d’intégrale.

## Séance 13 — Fractionnaires · Prolongement

### Intégrer une demi-fois : un noyau pondère toute l’histoire

Prolonger l’intégration répétée à un ordre réel et rendre visible la mémoire d’une impulsion passée.

**Objets et paramètres**

- t≥0 : instant observé ; u : instant du passé intégré ; α,β>0 : ordres réels d’intégration.
- f : fonction intégrée choisie ; q : exposant de la puissance t^q ; a : durée de l’impulsion.
- Γ : fonction gamma ; J^α : intégrale à borne initiale 0, de noyau (t−u)^(α−1)/Γ(α). Les paramètres sont sans dimension.

**Repères** — Sup : Primitive nulle en 0 et intégrations répétées. Spé : Calcul d’intégrales à paramètre (MP) ; convolution et interversion double expliquées en complément. Au-delà : Intégrales d’ordre non entier et lois de mémoire.

1. Choisir α=1 : retrouver la primitive ordinaire.
2. Choisir α=β=1/2 sur une puissance : lire le contrôle de composition.
3. Activer l’impulsion, puis comparer α=1/2 et α=3/2 après t=a : la mémoire décroît ou croît.

**À justifier :** L’opérateur dépend de l’histoire entière. Deux demi-intégrations donnent une intégration, avec les coefficients gamma appropriés.

### Caputo et Riemann–Liouville : que devient une constante ?

Comparer deux définitions et montrer qu’une dérivée non locale n’est pas fixée par la seule valeur et la pente à l’instant observé.

**Objets et paramètres**

- t>0 : instant ; 0<α<1 : ordre de dérivation ; q≥0 : entier ; c : constante dans f(t)=c+t^q.
- Pour q≥1, f(0)=c ; pour q=0, f(0)=c+1. RL désigne Riemann–Liouville ; Caputo désigne l’autre convention.
- A : amplitude de la modification du passé dans t+A t(1−t)². Toutes ces fonctions ont la même valeur et la même pente en t=1.

**Repères** — Sup : Dérivation d’une constante et polynômes. Spé : Noyaux singuliers intégrables et contrôle de la valeur initiale. Au-delà : Dérivées de Caputo et de Riemann–Liouville.

1. Choisir q=0,c=0 : comparer les deux dérivées de la constante 1.
2. Choisir q=1 et passer c de 0 à 1 : identifier le terme dû à f(0).
3. Modifier A : vérifier que valeur et pente en t=1 restent identiques, tandis que Caputo change.

**À justifier :** Caputo annule une constante ; RL conserve un terme initial. La mémoire distingue deux fonctions qui se rejoignent avec la même pente.

## Séance 14 — Composition et polynômes

### Faà di Bruno : organiser les dérivées sans perdre les coefficients

Calculer une dérivée composée d’ordre élevé, expliquer ses coefficients combinatoires et vérifier le résultat par un développement limité.

**Objets et paramètres**

- x : variable ; n≥0 : ordre entier de dérivation ; f : fonction extérieure choisie ; g(x)=1+ax+bx² : fonction intérieure.
- a,b : coefficients de g ; x₀ : point du tableau ; m₁,m₂ : nombres de facteurs g′,g″, avec m₁+2m₂=n.
- k=m₁+m₂ : ordre de dérivation de f ; les lignes donnent les contributions à (f∘g)⁽ⁿ⁾(x₀).

**Repères** — Sup : Dérivée seconde et produits composés. Spé : Leibniz, récurrences de dérivées et développements limités. Au-delà : Faà di Bruno et polynômes de Bell.

1. Choisir n=2 et exp : retrouver les deux termes familiers.
2. Passer à n=4 : lire les trois couples (m₁,m₂) et leurs coefficients.
3. Choisir une inverse à n=6, puis a=0,x₀=0 : utiliser la parité pour contrôler les valeurs.

**À justifier :** Chaque contribution a une origine précise. Le nombre de dérivées de f n’est pas toujours n ; les grandes contributions peuvent se compenser.

### Hermite : dériver une gaussienne, compter des zéros et construire une base

Relier les dérivées d’une gaussienne, une récurrence polynomiale, des intégrations par parties et une équation différentielle.

**Objets et paramètres**

- x∈ℝ : variable ; n,m≥0 : degrés ; Hₙ : polynôme d’Hermite des physiciens, avec H₀=1 et H₁=2x.
- ψₙ : fonction normalisée proportionnelle à Hₙe^(−x²/2) ; ∫ℝψₙψₘ : produit scalaire.
- Une norme égale à 1 et un produit scalaire nul pour n≠m traduisent l’orthonormalité.

**Repères** — Sup : Gaussienne, dérivation et parité. Spé : Polynômes, orthogonalité et intégrales impropres. Au-delà : Base de Hermite et oscillateur harmonique quantique.

1. Choisir n=0,m=1 : contrôler la parité et l’orthogonalité.
2. Choisir n=6,m=8 : constater que la parité ne suffit plus à expliquer l’intégrale nulle.
3. Prendre m=n : vérifier la norme 1, puis augmenter n et compter les zéros.

**À justifier :** La récurrence construit les modes ; l’orthogonalité se démontre par intégrations par parties. Les zéros et l’équation différentielle relient algèbre et analyse.
