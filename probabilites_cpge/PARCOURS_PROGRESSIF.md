# Probabilités : un parcours sup / spé

Construire une loi finie, calculer ses moments, puis contrôler ses fluctuations. Les exercices 6, 7 et 8 servent ensuite à relier récurrences, extrema et algèbre linéaire.

Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les approfondissements et les branches au-delà du programme se choisissent ensuite, indépendamment.

Le socle MPSI / MP concerne les univers finis puis les variables discrètes, le conditionnement, l’espérance, la variance et les inégalités probabilistes. Les lois à densité (maximum uniforme, arcsinus, gaussienne), la convergence en loi et les matrices aléatoires sont explicitement des prolongements. Une expérience continue peut exercer des techniques d’intégration, sans ajouter une loi obligatoire au programme MP.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : dénombrement, probabilités conditionnelles, indépendance et variables sur un univers fini.
- Sup : indicatrices, espérance, variance, binomiale et suites récurrentes.
- Spé : variables discrètes, covariance, Markov, Bienaymé–Tchebychev, sommes de Riemann et matrices symétriques.

## Pour chaque séance

1. Lire les objets, les notations et les hypothèses du TP.
2. Prévoir un résultat sur papier, puis ouvrir l’expérience.
3. Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.
4. Conclure par une courte preuve et distinguer résultat exact, approximation et observation.

## Sup : trois séances pour construire le modèle

Commencer par des lois calculables exactement ; la simulation vient après le dénombrement.

### 1. Avec ou sans remise : quel univers ?

**Techniques incontournables** · Sup · dénombrement et loi finie

Choisir un univers équiprobable et décrire la variable observée.

**À faire :** Prendre R=B=10, nombres de boules rouges et bleues, et d=10 tirages. Noter X le nombre de rouges. Retrouver la loi binomiale avec remise puis la formule combinatoire sans remise.

**Acquis attendu :** Expliquer l’indépendance dans un cas et la dépendance dans l’autre ; retrouver E(X)=5 dans les deux modèles.

**Limites et compléments :** Le nom « hypergéométrique » est fourni. L’essentiel est le dénombrement et la vérification du modèle, pas la mémorisation d’une nouvelle loi.

**TP associés :** La remise change la loi

### 2. Même moyenne, variances différentes

**Techniques incontournables** · Sup · indicatrices et variance

Écrire un comptage comme une somme de variables 0 ou 1.

**À faire :** Noter Iⱼ l’indicatrice « le tirage j est rouge » et écrire X=ΣIⱼ. Calculer l’espérance puis les termes croisés de E(X²). Comparer d=10 et d=20 dans une urne de 20 boules.

**Acquis attendu :** Justifier la variance nulle lorsqu’on tire toute l’urne sans remise ; montrer pourquoi la linéarité de l’espérance ne requiert pas l’indépendance.

**Limites et compléments :** Introduire les covariances à partir des probabilités conjointes. Ne pas supposer que des tirages de même probabilité sont indépendants.

**TP associés :** La remise change la loi

### 3. Une marche aléatoire cache une binomiale

**Techniques incontournables** · Sup · Bernoulli et transformation d’une variable

Traduire un déplacement en nombre de succès.

**À faire :** Noter n le nombre de pas, p la probabilité du pas +1 et K le nombre de ces pas. Établir Sₙ=2K−n pour le déplacement. Avec n=20 et p=1/2, calculer la probabilité de retour à l’origine.

**Acquis attendu :** Retrouver K de loi binomiale et P(S₂₀=0)=C(20,10)/2²⁰ ; calculer moyenne et variance du déplacement.

**Limites et compléments :** L’approximation gaussienne et les intervalles de confiance sont facultatifs, au-delà de cette séance de lois finies.

**TP associés :** Observer la loi, maîtriser l’écart

## Spé : trois séances de preuve et de transversalité

Contrôler les écarts, organiser une récurrence et relier trace et moyenne.

### 4. Une fréquence et une borne de fluctuation

**Techniques incontournables** · Spé · Bienaymé–Tchebychev

Déduire un contrôle probabiliste d’un calcul de variance.

**À faire :** Noter Fₙ=K/n la fréquence, p=1/2 et ε=0,1 la tolérance. Calculer Var(Fₙ)=p(1−p)/n ; comparer la probabilité binomiale exacte de |Fₙ−p|≥ε à la borne de Bienaymé–Tchebychev pour plusieurs n.

**Acquis attendu :** Justifier la convergence en probabilité vers p et expliquer pourquoi une borne théorique peut être peu précise mais valable.

**Limites et compléments :** Une trajectoire ne prouve pas la loi des grands nombres. Une borne à un instant donné n’est pas une garantie simultanée pour tous les instants.

**TP associés :** Observer la loi, maîtriser l’écart

### 5. Une moyenne conservée, un second moment qui change

**Techniques incontournables** · Spé · conditionnement sur une loi finie

Calculer à l’étape suivante en conditionnant sur l’état courant.

**À faire :** Noter Xₙ l’état, c sa valeur initiale et λ la part remplacée. À partir de Xₙ=x, calculer les deux valeurs possibles de Xₙ₊₁ et leurs probabilités. Retrouver E(Xₙ)=c et une récurrence pour E[Xₙ(1−Xₙ)].

**Acquis attendu :** Obtenir E[Xₙ(1−Xₙ)]=c(1−c)(1−λ²)ⁿ par récurrence ; expliquer que moyenne constante ne signifie pas loi constante.

**Limites et compléments :** À chaque rang fixé, les valeurs possibles sont finies. Le langage des martingales et les résultats de convergence presque sûre ne sont pas nécessaires.

**TP associés :** La moyenne tient, la population se sépare

### 6. Une moyenne spectrale par la trace

**Techniques incontournables** · Spé · théorème spectral et sommes de Riemann

Relier un calcul matriciel à une moyenne de valeurs propres.

**À faire :** Noter Tₙ la matrice du chemin : 1 juste au-dessus et au-dessous de la diagonale, 0 ailleurs. Vérifier les vecteurs propres de composantes sin(jkπ/(n+1)) puis retrouver Tr(Tₙ²)/n=2(n−1)/n.

**Acquis attendu :** Justifier les valeurs propres 2cos(kπ/(n+1)) et leur second moment limite 2, sans avoir besoin d’un tirage aléatoire.

**Limites et compléments :** Réduction des matrices symétriques et sommes de Riemann sont le socle. L’interprétation du spectre par une loi à densité arcsinus reste facultative.

**TP associés :** Un cosinus fait émerger la loi arcsinus

## Approfondissements : génératrices et polarisation

Deux séances qui exploitent des outils du programme sans imposer de théorème de processus aléatoire.

### 7. Calculer une loi par un produit

**Approfondissement CPGE** · Spé · fonctions génératrices

Retrouver la loi d’une somme de Bernoulli indépendantes.

**À faire :** Pour K, nombre de succès dans n essais indépendants de probabilité p, développer la fonction génératrice G(t)=(1−p+pt)ⁿ. Retrouver les coefficients, l’espérance et la variance par dérivation en t=1.

**Acquis attendu :** Relier l’indépendance au produit des génératrices et retrouver les calculs du laboratoire.

**Limites et compléments :** Les fonctions génératrices discrètes appartiennent au programme MP. L’extension aux transformées de variables à densité n’est pas demandée.

**TP associés :** Observer la loi, maîtriser l’écart ; La remise change la loi

### 8. Prouver la disparition de la zone centrale

**Approfondissement CPGE** · Spé · variable positive et majoration

Transformer un moment en une borne de probabilité.

**À faire :** Noter ε∈]0,1/2[ et utiliser Xₙ(1−Xₙ)≥ε(1−ε) sur l’événement ε≤Xₙ≤1−ε. Employer la récurrence de la séance 5 puis comparer au diagramme pour plusieurs valeurs de λ.

**Acquis attendu :** Obtenir une borne tendant vers zéro et expliquer la concentration près de 0 et 1, sans confondre convergence de la loi et comportement d’une trajectoire.

**Limites et compléments :** La preuve est un exercice avec outils CPGE. La théorie générale des chaînes de Markov, des martingales et de leurs limites est hors du socle.

**TP associés :** La moyenne tient, la population se sépare

## Au-delà : trois applications probabilistes

Les définitions continues sont apportées par le cours ; ces branches sont facultatives en MPSI / MP.

### A. Maximum, minimum et estimation

**Au-delà du programme** · Au-delà · lois à densité et statistique

Calculer la répartition d’un maximum à partir d’une intersection d’événements.

**À faire :** Noter U₁,…,Uₙ des observations uniformes indépendantes sur [0,θ], θ>0. Retrouver P(Mₙ≤x)=(x/θ)ⁿ pour 0≤x≤θ, puis sa moyenne. Examiner l’écart Zₙ=n(1−Mₙ/θ).

**Acquis attendu :** Distinguer observation maximale, biais de l’estimation et changement d’échelle ; expliquer l’apparition d’une limite exponentielle.

**Limites et compléments :** Lois uniformes à densité, statistiques d’ordre, estimation et convergence en loi sont des prolongements probabilistes.

**TP associés :** Le maximum approche la frontière

### B. Du cosinus à une densité

**Au-delà du programme** · Au-delà · loi arcsinus

Transformer une limite de sommes de Riemann en une mesure continue.

**À faire :** Reprendre les valeurs 2cos(kπ/(n+1)) et la variable angulaire uniforme sur [0,π]. Faire le changement de variable pour retrouver la densité 1/(π√(4−x²)) sur ]−2,2[.

**Acquis attendu :** Vérifier la normalisation, la symétrie et le moment d’ordre 2 ; expliquer les fortes concentrations près des extrémités.

**Limites et compléments :** La somme de Riemann et la substitution sont des techniques CPGE. Leur interprétation en loi à densité est un complément fourni.

**TP associés :** Un cosinus fait émerger la loi arcsinus

### C. Matrices aléatoires et demi-cercle

**Au-delà du programme** · Au-delà · théorème de Wigner admis

Comparer une matrice déterministe et une matrice à entrées aléatoires.

**À faire :** Noter Aₙ=Wₙ/√n la matrice symétrique normalisée. Choisir d’abord les signes ±1, puis changer la loi des entrées en gardant leur variance égale à 1. Comparer les moments du spectre et l’effet du nombre de matrices simulées.

**Acquis attendu :** Distinguer le demi-cercle de Wigner de la loi arcsinus ; relier le second moment à la normalisation et séparer fluctuation et effet de dimension.

**Limites et compléments :** Le théorème de Wigner, l’universalité et les moments de Catalan sont hors programme. Les histogrammes l’illustrent sans le démontrer.

**TP associés :** Des matrices aléatoires au demi-cercle

## Repères de programme

- [Programme officiel de mathématiques MPSI](https://prepas.org/ups.php?document=69)
- [Programme officiel de mathématiques MP](https://prepas.org/ups.php?document=85)
