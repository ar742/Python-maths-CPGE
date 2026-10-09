# Quatorze séances d’analyse

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le théorème adapté.

## Séance 01 — Intégrales à paramètre · p. 63

### Théorème 1 : continuité d’une transformée gaussienne

Appliquer le premier théorème de la page 63 avant de calculer une intégrale et relier le résultat à Fourier.

1. Choisir a=0 : vérifier l’intégrale gaussienne.
2. Augmenter a : les oscillations restent dans la même enveloppe.
3. Réduire L puis comparer l’écart observé à la borne totale annoncée.

**À justifier :** Le majorant global prouve la continuité sur ℝ. La compensation réduit F sans invalider la majoration de l’intégrande.

### Théorème 1 : une masse qui se concentre interdit le passage à la limite

Comprendre pourquoi la convergence ponctuelle ne suffit pas pour passer une limite sous une intégrale.

1. Diminuer a en gardant ε fixe : mesurer la masse dans [0,ε].
2. Faire aussi ε=a et constater la fraction 1−e⁻¹.
3. Lire l’enveloppe 1/(et) et vérifier la divergence de son intégrale près de 0.

**À justifier :** Le pic s’efface à chaque point fixé, mais son aire reste égale à 1. Le majorant manquant explique exactement l’échec de la continuité en a=0.

## Séance 02 — Intégrales à paramètre · p. 63

### Théorème 2 : Frullani, un logarithme retrouvé par dérivation

Calculer une intégrale compensée en dérivant un paramètre, puis fixer sa constante par une valeur simple.

1. Choisir a=1,b=2 : retrouver ln 2.
2. Choisir a=b : l’intégrale est nulle, mais sa dérivée en a ne l’est pas.
3. Réduire a et L : lire la borne de queue puis augmenter L.

**À justifier :** La dérivation simplifie l’intégrande. La condition F(b,b)=0 est indispensable pour retrouver ln(b/a).

### Théorème 2 : transformer une intégrale oscillante en arctangente

Transformer une intégrale oscillante en une EDO et comprendre la portée locale du théorème de Leibniz.

1. Choisir a=1 : comparer intégrale et π/4.
2. Diminuer a tout en gardant L fixe : vérifier la borne de la queue.
3. Augmenter L puis expliquer pourquoi le calcul pour a=0 n’est pas justifié par le même majorant.

**À justifier :** Pour a>0, F(a)=arctan(1/a). Un résultat au bord du domaine demande une justification supplémentaire.

## Séance 03 — Intégrales à paramètre · p. 63

### Théorème 3 : dérivées de Γ, moments logarithmiques et convexité

Appliquer le troisième théorème de la page 63 à plusieurs ordres, puis obtenir une inégalité par Cauchy–Schwarz.

1. Choisir n=2,a=2 et comparer les moments à la variance positive.
2. Descendre a à 0,6 : voir l’importance de la queue basse en u.
3. Augmenter q et T : comparer les bornes des queues et l’indicateur de quadrature.

**À justifier :** Γ est C∞ sur ]0,+∞[. Sa log-convexité résulte d’un moment quadratique ; chaque passage sous l’intégrale a un majorant local explicite.

### Théorème 3 : dérivées de Laplace et monotonie complète

Contrôler plusieurs dérivations par un majorant commun et mesurer une troncature avec une queue exacte.

1. Choisir n=4,a=1 et retrouver 24.
2. Choisir n=8,a=0,25,L=12 : voir le maximum sortir de la fenêtre.
3. Augmenter L et mesurer la proportion capturée, au lieu de conclure à partir du dessin seul.

**À justifier :** Les dérivées alternent de signe et leur valeur absolue est un moment positif. Les maxima et les queues expliquent les choix de coupure numérique.

## Séance 04 — C · Équations différentielles

### Euler et RK4 : mesurer un ordre de convergence

Résoudre le TP p. 69 et mesurer la précision de deux méthodes plutôt que juger seulement l’allure des courbes.

1. Choisir le TP et suivre les pentes sur la solution exacte.
2. Choisir le pas grossier puis augmenter N.
3. Lire les ordres mesurés ; vérifier pourquoi diviser le pas par 2 ne produit pas le même gain pour Euler et RK4.

**À justifier :** Justifier l’ordre observé, annoncer la référence utilisée et séparer précision et présentation du graphique.

### Facteur intégrant : transformer une EDO en intégrale

Transformer une équation différentielle linéaire en intégrale définie, puis interpréter la mémoire et la sensibilité.

1. Choisir la relaxation constante et retrouver l’exponentielle.
2. Choisir le coefficient variable et examiner le noyau par l’écart initial.
3. Mettre a=b=F=0 puis expliquer pourquoi les deux solutions restent constantes et distinctes.

**À justifier :** Reconstruire la formule intégrale avec la bonne constante et relier sa dérivée à l’EDO.

## Séance 05 — C · Équations différentielles

### Une condition initiale ne suffit pas toujours

Distinguer une hypothèse d’un théorème, sa conclusion et une preuve effective de non-unicité.

1. Changer τ : noter que la donnée initiale ne change jamais.
2. Lire le quotient pour de petits ε.
3. Passer λ de −1 à 1 : expliquer pourquoi une divergence de deux préparations ne réfute pas l’unicité.

**À justifier :** Savoir expliquer pourquoi un calcul partant de zéro peut sélectionner une solution sans démontrer son unicité.

### Solution maximale : explosion ou saturation

Donner un sens au domaine maximal d’une solution, puis étudier qualitativement un modèle avec saturation.

1. Comparer les deux modèles au réglage initial.
2. Approcher la fraction 0,95 et suivre la droite 1/y.
3. Partir au-dessus de K ; prévoir le sens d’évolution logistique avant le calcul.

**À justifier :** Nommer un intervalle maximal et justifier la saturation par le second membre, sans confondre les deux notions.

## Séance 06 — C · Équations différentielles

### Oscillateur : transitoire, résonance et travail

Relier l’équation d’ordre 2, ses deux données initiales et les applications physiques de la résonance.

1. Choisir le cas critique puis le cas apériodique libre.
2. Comparer la résonance amortie à la résonance sans amortissement.
3. Doubler la durée sans amortissement : expliquer la croissance du maximum et contrôler E−E₀=W−D.

**À justifier :** Énoncer quand une amplitude stationnaire a un sens et quand le temps d’observation fait partie du résultat.

### Variation des constantes : un noyau de Green initial

Résoudre l’exercice 1 p. 71 et interpréter chaque étape de la variation des constantes.

1. Calculer la particulière à données nulles et comparer ses deux coefficients.
2. Ajouter la solution homogène de donnée y₀=1,v₀=2.
3. Supprimer le second membre : vérifier le mode e^{3x} puis examiner l’écart Gauss/RK4.

**À justifier :** Retrouver le signe des coefficients et expliquer pourquoi une particulière doit encore être ajustée au problème initial.

## Séance 07 — C · Équations différentielles

### Euler–Cauchy : singularités et série entière

Résoudre l’exercice 2 p. 71 sans oublier le domaine, puis utiliser les séries entières pour comprendre et calculer.

1. Choisir le prolongement régulier et vérifier le comportement x²/3 près de 0.
2. Activer le mode 1/x sur un intervalle évitant 0.
3. Approcher x=1 puis augmenter le nombre de termes ; comparer convergence de la série et singularité du problème.

**À justifier :** Donner la solution avec son intervalle et distinguer un faux 0/0 d’un véritable mode singulier.

### EDO homogène et Riccati : deux changements de fonction

Comparer deux substitutions classiques en surveillant leurs domaines de validité.

1. Changer c et observer le raccordement en 0.
2. Choisir z₀=−1 puis z₀=1 : vérifier les équilibres de Riccati.
3. Choisir z₀=1,5 ; rapprocher le pôle de Riccati du zéro de u.

**À justifier :** Nommer correctement l’équation et expliciter les points où le changement de fonction cesse d’être valable.

## Séance 08 — C · Équations différentielles

### Trois réservoirs : conservation, modes et exponentielle

Passer de bilans concrets à un système de dimension 3 et utiliser ses modes pour expliquer l’évolution.

1. Choisir des échanges symétriques et retrouver les deux modes de taux 3k.
2. Ralentir un échange et comparer les temps propres.
3. Introduire une perte : comparer les quantités et les proportions au temps final.

**À justifier :** Associer chaque valeur propre à un bilan ou à une relaxation et conserver le sens du troisième réservoir.

### Deux bords : existence, unicité et résonance

Étudier concrètement l’existence et l’unicité sous deux conditions aux bords ; favoriser les applications des théorèmes.

1. Choisir λ=2 : vérifier la solution unique.
2. Choisir la résonance incompatible : interpréter le résidu.
3. Rendre le second membre compatible puis varier l’amplitude libre sans modifier l’équation ni les bords.

**À justifier :** Vérifier la compatibilité avant de conclure à une solution et démontrer pourquoi l’unicité de Cauchy ne suffit pas ici.

## Séance 09 — Équations fonctionnelles

### Cauchy : une équation à deux variables détermine une droite

Résoudre une équation fonctionnelle par substitutions, puis comprendre le rôle exact de la continuité.

1. Choisir b=0 et voir le résidu presque nul aux arrondis près.
2. Ajouter b=0,1 et comparer la faible perturbation de la courbe au défaut de la carte.
3. Tester à la main le couple x=y=π/2, puis lire la preuve de classification.

**À justifier :** La continuité prolonge la linéarité des rationnels aux réels. Un seul contre-exemple rejette une fonction ; des tests finis ne prouvent pas l’identité.

### Produit, logarithme, puissance : changer de variable pour résoudre

Transformer les produits en sommes et retrouver le logarithme ou les puissances en justifiant chaque changement de variable.

1. Choisir le logarithme exact, puis interpréter une case en revenant à x=eᵘ et y=eᵛ.
2. Passer à la puissance avec a=−1 et vérifier f(xy)=f(x)f(y).
3. Activer une perturbation et trouver un couple qui invalide le candidat.

**À justifier :** Le logarithme convertit une structure multiplicative en une structure additive. Le domaine positif et la positivité de f sont des étapes de preuve.

## Séance 10 — Équations fonctionnelles

### D’Alembert : pourquoi apparaissent cosinus et cosinus hyperbolique ?

Faire apparaître une équation différentielle dans une équation fonctionnelle et conserver les conditions initiales.

1. Comparer les deux familles exactes avec le même k.
2. Choisir la solution nulle et identifier l’étape de preuve qui change.
3. Ajouter b=0,1 : la parité persiste, mais les résidus fonctionnel et différentiel révèlent le défaut.

**À justifier :** Les substitutions fournissent des conditions nécessaires. L’EDO et ses conditions initiales donnent les candidats, puis les formules d’addition valident la réciproque.

### Substituer −x : identifier une fonction sans la deviner

Utiliser une substitution adaptée pour calculer f(x) et f(−x) sans présupposer une forme de solution.

1. Choisir b=0 et retrouver les valeurs f(1)=1, f(−1)=0.
2. Comparer la partie paire et la partie impaire à la solution totale.
3. Ajouter un petit b et observer que le résidu ne s’annule pas près de 0.

**À justifier :** Le système détermine une unique solution sur le domaine. En 0, seule une demande de prolongement continu impose la valeur 0.

## Séance 11 — Fonctions spéciales

### Gamma : prolonger la factorielle et contrôler une intégrale impropre

Définir une fonction par une intégrale impropre, reconnaître son domaine et utiliser une intégration par parties pour retrouver la factorielle.

1. Choisir x=1/2 : identifier la singularité en 0 sans conclure à la divergence.
2. Choisir x=5 et comparer Γ(5) à 4!.
3. Choisir x=8, T=5, puis augmenter T : interpréter la part de l’aire retenue.

**À justifier :** L’intégrale existe pour x>0 ; sa relation fonctionnelle est démontrée, et la queue de l’intégrale explique un écart même si la quadrature est précise.

### Bêta : un changement de variables relie deux intégrales

Faire apparaître bêta par un changement de variables et employer le rapport gamma pour calculer des moments ou des intégrales trigonométriques.

1. Choisir a=b=1 : retrouver la densité uniforme.
2. Comparer (2,5) et (5,2) : observer la réflexion autour de 1/2.
3. Choisir a=b=1/2, puis a=b=4 : distinguer singularités intégrables et concentration au centre.

**À justifier :** Les deux paramètres ont des rôles symétriques ; le facteur jacobien r fait apparaître exactement Γ(a+b), et non une autre valeur de gamma.

## Séance 12 — Fonctions spéciales

### Zêta : une somme approchée n’est pas encore une valeur certifiée

Donner une approximation accompagnée d’un encadrement et comprendre pourquoi la convergence devient difficile près de s=1.

1. À s=2, augmenter N puis comparer S_N à π²/6.
2. Passer à s=1,1 avec N=4000 : lire le reste, pas seulement le dernier terme.
3. À s=3/2, doubler N et comparer la diminution du reste à 2^(1−s).

**À justifier :** Une série peut converger très lentement. Le reste se contrôle par des intégrales ; choisir un compact évite d’oublier le bord du domaine.

### Zêta et gamma : de la série à une intégrale de Planck

Justifier le passage d’une série à une intégrale et relier un changement d’échelle à une loi physique en température.

1. Choisir s=4 : comparer la valeur à π⁴/15.
2. Choisir s=1,2 : repérer où se concentre la difficulté d’intégration.
3. Choisir s=6 et T=5, puis augmenter T : distinguer le problème en 0 de la queue à l’infini.

**À justifier :** La positivité justifie l’interversion ; s>1 vient du voisinage de 0. Le changement de fréquence fournit une puissance de température sans nouveau calcul d’intégrale.

## Séance 13 — Fractionnaires · Prolongement

### Intégrer une demi-fois : un noyau pondère toute l’histoire

Prolonger l’intégration répétée à un ordre réel et rendre visible la mémoire d’une impulsion passée.

1. Choisir α=1 : retrouver la primitive ordinaire.
2. Choisir α=β=1/2 sur une puissance : lire le contrôle de composition.
3. Activer l’impulsion, puis comparer α=1/2 et α=3/2 après t=a : la mémoire décroît ou croît.

**À justifier :** L’opérateur dépend de l’histoire entière. Deux demi-intégrations donnent une intégration, avec les coefficients gamma appropriés.

### Caputo et Riemann–Liouville : que devient une constante ?

Comparer deux définitions et montrer qu’une dérivée non locale n’est pas fixée par la seule valeur et la pente à l’instant observé.

1. Choisir q=0,c=0 : comparer les deux dérivées de la constante 1.
2. Choisir q=1 et passer c de 0 à 1 : identifier le terme dû à f(0).
3. Modifier A : vérifier que valeur et pente en t=1 restent identiques, tandis que Caputo change.

**À justifier :** Caputo annule une constante ; RL conserve un terme initial. La mémoire distingue deux fonctions qui se rejoignent avec la même pente.

## Séance 14 — Composition et polynômes

### Faà di Bruno : organiser les dérivées sans perdre les coefficients

Organiser une dérivation à ordre élevé, expliquer les coefficients combinatoires et contrôler une inverse par une méthode indépendante.

1. Choisir n=2 et exp : retrouver les deux termes familiers.
2. Passer à n=4 : lire les trois couples (m₁,m₂) et leurs coefficients.
3. Choisir une inverse à n=6, puis a=0,x₀=0 : utiliser la parité pour contrôler les valeurs.

**À justifier :** Chaque contribution a une origine précise. Le nombre de dérivées de f n’est pas toujours n ; les grandes contributions peuvent se compenser.

### Hermite : dériver une gaussienne, compter des zéros et construire une base

Relier les dérivées d’une gaussienne, une récurrence polynomiale, des intégrations par parties et une équation différentielle.

1. Choisir n=0,m=1 : contrôler la parité et l’orthogonalité.
2. Choisir n=6,m=8 : constater que la parité ne suffit plus à expliquer l’intégrale nulle.
3. Prendre m=n : vérifier la norme 1, puis augmenter n et compter les zéros.

**À justifier :** La récurrence construit les modes ; l’orthogonalité se démontre par intégrations par parties. Les zéros et l’équation différentielle relient algèbre et analyse.
