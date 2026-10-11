# Un parcours pour préparer les CPGE et les concours

Pour chaque étape : **prévoir**, **expérimenter**, **démontrer**, puis **discuter les limites**.
Écrire une conjecture avant de déplacer les curseurs. Consulter la correction ensuite.

## Séance 1 — Choisir le bon modèle (35 à 45 minutes)

Ouvrir « Urnes & dépendance », exemple exercice 4. Prévoir l’espérance pour 10 rouges,
10 bleues et 10 tirages. Comparer les deux lois. Tirer toute l’urne : expliquer la variance
nulle. Démontrer la formule par dénombrement puis retrouver l’espérance par indicatrices.

Leçons 1–3 ; exercices 1–5. Objectif : ne pas supposer l’indépendance par habitude.

## Séance 2 — De la marche à la preuve des grands nombres (45 minutes)

Ouvrir « Fréquences & fluctuations », exemple marche du TP. Retrouver Sₙ=2K−n
et la contrainte de parité. Comparer un événement rare et une loi plus équilibrée.
Augmenter n : comparer la probabilité exacte et la borne de Tchebychev.
Changer la graine : la fréquence converge-t-elle de manière monotone ?

Leçons 4–6 ; exercices 6–7. Objectif : distinguer loi, fréquence et approximation.

## Séance 3 — Priorité exercice 6 : une polarisation (50 à 60 minutes)

Commencer par λ=0,25, c=0,35. Prédire le devenir de la moyenne et de la variance.
Comparer polarisation lente et rapide. Déplier les moments à l’étape n.
Une trajectoire qui se rapproche de 0 signifie-t-elle que l’espérance tend vers 0 ?

Établir les deux espérances conditionnelles. Résoudre la récurrence du second moment.
Utiliser Xₙ(1−Xₙ) pour majorer la masse centrale, puis démontrer la convergence de tous
les moments. Finir par la preuve de la convergence en loi avec les fonctions continues.

Leçons 7–8 ; exercices 8–10. Objectif : conserver une espérance tout en changeant de loi.
Le théorème des martingales bornées est une extension facultative.

## Séance 4 — Priorité exercice 7 : les extrêmes (45 à 60 minutes)

Observer les maxima pour n=1, 20, 100. Écrire {Mₙ≤x} comme une intersection.
Comparer minimum et maximum ; choisir ensuite un rang intérieur.
Passer à « Écart n(1−Mₙ/θ) » : comprendre pourquoi une limite exponentielle apparaît.

Avec θ=3, déplier le tableau du maximum : comparer une estimation brute, sa correction
sans biais et l’intervalle exact 95 % du premier maximum simulé. Démontrer sa couverture.

Leçons 9–10 ; exercices 11–13. Objectif : distinguer limite de la variable et limite
de son écart renormalisé. Les intervalles statistiques sont un prolongement.

## Séance 5 — Priorité exercice 8 : probabilité et algèbre (60 minutes)

Dans « Arcsinus », augmenter n. Expliquer la concentration aux bords via le cosinus.
Faire varier l’indice du mode : retrouver les sinusoïdes propres du chemin.
Prouver les valeurs propres, puis la loi limite par une somme de Riemann.
Calculer Tr(Tₙ²) sans diagonaliser : le second moment limite doit être 2.

Dans « Wigner », comparer les trois lois d’entrées et plusieurs matrices indépendantes.
Le second moment limite est maintenant 1. Comparer les moments pairs au tableau de Catalan.
Pourquoi les valeurs propres d’une même matrice ne sont-elles pas des répétitions indépendantes ?

Leçons 11–12 ; exercices 14–16. Objectif : relier probabilités, intégration, trigonométrie
et réduction des matrices. Le théorème général de Wigner est admis, et ses hypothèses
et conclusions sont distinguées de la partie entièrement démontrée.

## Bilan oral (10 minutes)

Expliquer sans écran : le rôle de l’indépendance ; pourquoi une densité peut dépasser 1 ;
pourquoi une simulation ne prouve pas une convergence ; la différence entre arcsinus
et demi-cercle ; ce qu’ajoute un contrôle de variance à une convergence des moyennes.

[Ouvrir le cours et les corrections](COURS.md)

<!-- REPERES_EXPERIENCES -->

## Guides des expériences

Les repères distinguent les outils de sup, ceux de spé et les prolongements. Ils s’appuient sur les programmes de mathématiques [MPSI](https://prepas.org/ups.php?document=69) et [MP](https://prepas.org/ups.php?document=85).

### La moyenne conservée et la polarisation

Exercice 6 : suivre une population dont la moyenne reste constante, alors que les individus se rapprochent de 0 ou de 1. Déduire cette séparation d’une récurrence sur les moments.

**Objets et notations**

- Xₙ est l’état après n étapes ; c est l’état initial, entre 0 et 1

- λ est la part remplacée à chaque étape ; ε définit la zone centrale [ε,1−ε]

- À partir de Xₙ=x, Bₙ₊₁ vaut 1 avec probabilité x, sinon 0 ; Xₙ₊₁=(1−λ)x+λBₙ₊₁

- Les répétitions sont des trajectoires indépendantes ; la graine reproduit leur tirage. Toutes ces grandeurs sont sans unité

**Hypothèses**

- 0<c<1 et 0<λ<1 ; la probabilité du prochain succès dépend de l’état courant

- Les moments affichés ont une formule exacte ; les fréquences simulées fluctuent

**Techniques à mobiliser**

- Conditionner sur l’étape précédente

- Résoudre une récurrence affine

- Majorer une probabilité avec une variable positive

**Trois premières manipulations**

1. Commencer avec c=0,5 : comparer moyenne et variance à plusieurs étapes.

2. Augmenter λ : expliquer la disparition plus rapide de la zone centrale.

3. Prendre c=0,2 : prévoir la proportion limite proche de 1, puis vérifier la borne théorique.

**Repères CPGE**

**Sup :** Bernoulli, espérance, variance et récurrences.

**Spé :** Calculs par probabilités totales et majorations de probabilités.

**Au-delà :** Espérance conditionnelle, convergence en loi, martingales et convergence presque sûre : hors programme MPSI/MP. Ici les calculs conditionnels se ramènent à des sommes finies.

**À retenir :** La moyenne constante ne signifie pas que chaque trajectoire converge vers cette moyenne.

### Maximum, minimum et rang

Exercice 7 : chercher la plus grande valeur d’un échantillon, puis mesurer son écart à la borne de l’intervalle. Partir de l’événement où toutes les observations sont sous un même seuil.

**Objets et notations**

- U₁,…,Uₙ sont les observations ; n est la taille de l’échantillon

- θ>0 est la borne supérieure de [0,θ] ; Mₙ=max Uⱼ et mₙ=min Uⱼ

- U₍ₖ₎ est la k-ième valeur après classement, 1≤k≤n

- Le mode écart observe Zₙ=n(1−Mₙ/θ). L’échelle de θ est une unité arbitraire ; Zₙ est sans dimension

**Hypothèses**

- Observations indépendantes, uniformes sur [0,θ]

- Les répétitions génèrent des échantillons distincts ; elles ne construisent pas toutes une même suite emboîtée

**Techniques à mobiliser**

- Écrire une intersection d’événements

- Calculer une répartition

- Comparer une valeur exacte et un biais d’estimation

**Trois premières manipulations**

1. Choisir n=1 : retrouver la loi uniforme.

2. Augmenter n pour le maximum : prévoir sa moyenne et son rapprochement de θ.

3. Passer à l’écart Zₙ puis au rang médian : distinguer les variables observées.

**Repères CPGE**

**Sup :** événements, indépendance et produits de probabilités.

**Spé :** réutilisation de la binomiale pour compter les observations sous un seuil.

**Au-delà :** Prolongement accompagné : variables à densité, statistiques d’ordre et estimation ; hors socle probabiliste MPSI/MP.

**À retenir :** La loi du maximum s’obtient par un événement simple ; sa limite seule ne donne pas sa vitesse.

### Cosinus et loi arcsinus

Exercice 8 : calculer le spectre d’une matrice tridiagonale, puis expliquer sa répartition par une somme de Riemann. Une concentration près des bords peut venir d’une transformation déterministe.

**Objets et notations**

- Tₙ est la matrice n×n avec des 1 juste au-dessus et au-dessous de la diagonale, 0 ailleurs

- Les valeurs propres sont λₖ=2cos(kπ/(n+1)), pour 1≤k≤n

- Le mode choisi fixe k ; les composantes du vecteur propre sont sin(jkπ/(n+1)), 1≤j≤n

- Le moment d’ordre r est la moyenne des λₖʳ ; toutes les grandeurs sont sans unité

**Hypothèses**

- Matrice réelle symétrique, spectre réel ; n ne désigne pas le nombre de simulations

- Chaque valeur propre reçoit le même poids 1/n

**Techniques à mobiliser**

- Vérifier un vecteur propre

- Utiliser une identité trigonométrique

- Transformer une somme de Riemann

**Trois premières manipulations**

1. Prendre n=12 et regarder le vecteur du premier mode.

2. Augmenter n : comparer les valeurs propres à la répartition limite.

3. Choisir le moment 2 : retrouver Tr(Tₙ²)/n=2(n−1)/n.

**Repères CPGE**

**Sup :** trigonométrie, sommes et intégration.

**Spé :** réduction des matrices symétriques, trace et sommes de Riemann.

**Au-delà :** interprétation par une loi à densité arcsinus, hors programme probabiliste MP.

**À retenir :** La même formule décrit les valeurs propres et une limite de sommes ; aucun tirage aléatoire n’est nécessaire.

### Matrices aléatoires et demi-cercle

Comparer trois lois d’entrées aléatoires et mesurer les moments de leurs valeurs propres. Comprendre ce que peut illustrer une simulation, sans la prendre pour une preuve du théorème de Wigner.

**Objets et notations**

- Wₙ est symétrique n×n ; ses entrées du triangle supérieur sont tirées indépendamment

- Aₙ=Wₙ/√n est la matrice étudiée ; λⱼ sont ses valeurs propres

- Le nombre de matrices règle les tirages indépendants, pas le nombre de valeurs propres par matrice

- Le moment d’ordre r est Tr(Aₙʳ)/n ; les valeurs sont sans unité

**Hypothèses**

- Trois lois fixes, centrées, de variance 1 et à moments finis

- La loi du demi-cercle est une référence limite ; une dimension finie peut donner des valeurs hors de [−2,2]

**Techniques à mobiliser**

- Normaliser une variance

- Appliquer le théorème spectral

- Relier trace, puissances et moyenne spectrale

**Trois premières manipulations**

1. Choisir les signes ±1 : vérifier le second moment proche de 1.

2. Changer la loi des entrées en gardant la dimension.

3. Augmenter le nombre de matrices : distinguer fluctuation de simulation et effet de la dimension.

**Repères CPGE**

**Sup :** variables centrées, variance et indépendance.

**Spé :** matrices symétriques, valeurs propres et traces.

**Au-delà :** théorème de Wigner et matrices aléatoires ; résultat admis, hors programme MPSI/MP.

**À retenir :** La loi du demi-cercle et la loi arcsinus du laboratoire précédent concernent deux modèles différents.

### Urnes et dépendance

Comparer des tirages avec et sans remise. Retrouver le nombre moyen de rouges, puis expliquer pourquoi la dépendance modifie la variance.

**Objets et notations**

- R et B sont les nombres de boules rouges et bleues ; N=R+B

- d est le nombre de tirages, avec 1≤d≤N dans la comparaison sans remise

- X compte les rouges tirées ; p=R/N est la probabilité d’un rouge au premier tirage

- Iⱼ vaut 1 si le tirage j est rouge, sinon 0 ; X=ΣIⱼ. Les quantités sont des nombres ou des probabilités

**Hypothèses**

- Boules choisies uniformément ; avec remise, les tirages sont indépendants

- Sans remise, on choisit une partie de taille d ; la loi est hypergéométrique

**Techniques à mobiliser**

- Dénombrer les parties d’une urne

- Écrire une somme d’indicatrices

- Développer une variance avec covariances

**Trois premières manipulations**

1. Prendre R=B=10 et d=10 : prévoir l’espérance dans les deux modèles.

2. Tirer toute l’urne sans remise : expliquer la variance nulle.

3. Augmenter N à proportion rouge fixe : observer la proximité avec la binomiale.

**Repères CPGE**

**Sup :** dénombrement, lois finies et indicatrices.

**Spé :** covariance, dépendance et variance d’une somme.

**Au-delà :** approximation d’un prélèvement faible par des tirages indépendants.

**À retenir :** Une même espérance peut accompagner des lois et des variances différentes.

### Marche, fréquences et fluctuations

Relier une fréquence de succès à la binomiale et à une marche aléatoire. Comparer une probabilité exacte de fluctuation à la borne de Bienaymé–Tchebychev.

**Objets et notations**

- n est le nombre d’essais d’un bloc ; p est la probabilité constante de succès

- K compte les succès et Fₙ=K/n est leur fréquence

- La marche a déplacement Sₙ=2K−n, avec des pas +1 ou −1

- ε>0 est la tolérance sur Fₙ−p. Les répétitions portent sur des blocs indépendants ; les grandeurs sont sans unité

**Hypothèses**

- Essais Bernoulli indépendants et de même paramètre p

- Aux bornes p=0 ou 1, le résultat est déterministe ; l’approximation normale exige une variance non nulle

**Techniques à mobiliser**

- Passer d’une binomiale à une marche

- Calculer la variance d’une moyenne

- Appliquer une inégalité de probabilité

**Trois premières manipulations**

1. Choisir n=20 et p=0,5 : traduire le retour de la marche en K=10.

2. Augmenter n : observer les fluctuations de K/n à tolérance fixe.

3. Comparer probabilité binomiale et borne théorique ; changer la graine pour voir la variabilité simulée.

**Repères CPGE**

**Sup :** binomiale, espérance et variance.

**Spé :** Bienaymé–Tchebychev et loi faible des grands nombres.

**Au-delà :** approximation normale et intervalle de Wilson, extensions statistiques hors programme MP.

**À retenir :** La borne prouve un contrôle pour un instant fixé ; une trajectoire simulée ne fournit pas une garantie simultanée.
