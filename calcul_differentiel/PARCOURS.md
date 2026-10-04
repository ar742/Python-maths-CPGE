# Un parcours de travail : conjecturer, calculer, démontrer

Le volet comprend **8 laboratoires, 14 leçons et 18 exercices**. Pour chaque séance,
écrire la conjecture avant de lire la correction. Les extensions Lie et gaussienne
sont accessibles avec des rappels, mais dépassent certaines filières CPGE.

## Séance 1 · Sup : linéariser et distinguer les notions · 45 min

Ouvrir **Différentielle & Taylor**, fonction lisse. Changer la direction ; comparer
fonction, tangente et parabole de Taylor. Exporter les restes puis estimer leur pente
en coordonnées logarithmiques. Lire les leçons 1 et 5.

Ouvrir **Chemin courbe**. Expliquer pourquoi une direction fixe ne voit pas le chemin
y=x³. Faire les exercices 1 et 7. Livrable : définition de la différentielle,
preuve de son unicité et contre-exemple « dérivées directionnelles ⇒ différentiabilité ».

## Séance 2 · Spé : les deux TP de coordonnées et d’intégrales · 60 min

Ouvrir **Jacobiennes**, comparer les trois systèmes. En sphérique, identifier les
colonnes, calculer le signe du déterminant et ouvrir le pôle singulier. Séparer
singularité de la carte et différentiabilité de F. Leçons 2 à 4 ; exercices 2 et 3.

Ouvrir **Intégrale elliptique** et **TP du recueil**. Retrouver les coefficients 81
et −4, puis le facteur 6r. Prédire l’effet d’un changement de demi-axe sur chaque
terme de l’intégrale. Vérifier numériquement puis rédiger la preuve exacte.
Exercices 4 et 5. Complément : lancer `tp_symbolique.py` après avoir calculé J à la main.

## Séance 3 · Spé : le TP matriciel · 45 min

Ouvrir **Matrices**, puis **À l’identité** et **Matrice singulière**. Pourquoi le
déterminant garde-t-il une différentielle, contrairement à l’inverse ? Choisir une
matrice presque singulière et observer les restes. Leçon 6 ; exercices 8 et 9.

Livrable : démontrer les deux différentielles et expliquer leur domaine de validité.
Pour n quelconque, relier cofacteurs, adjointe classique et trace.

## Séance 4 · Spé : Hessienne, Rayleigh et algorithmes · 60 min

Ouvrir les trois points critiques de l’**exercice 1**. Refaire les déterminants de
H ; expliquer le cas dégénéré par une coupe qui change de signe. Exercice 6.

Ouvrir **Rayleigh & Newton**. Faire varier l’orientation et l’écart spectral.
Comparer un pas stable, le seuil αλmax=2 et un pas trop grand. Expliquer Newton
en un pas sur cette quadratique. Ouvrir **Rayleigh**, puis approcher la direction
minimale. Leçons 7 et 8 ; exercices 10 à 12.

Livrable : distinguer Hessienne semi-définie, définie positive et stricte convexité ;
démontrer la condition de convergence et l’erreur quadratique du quotient.

## Séance 5 · Extension : la différentielle explique Lie · 60 min

Ouvrir **Algèbres de Lie**. Comparer GL, SL et SO en dimension 3. Vérifier trace,
déterminant et défaut d’orthogonalité dans les valeurs détaillées. Passer à SO(2) :
le crochet disparaît. Revenir à SO(3) et étudier le quotient du commutateur par s².
Leçons 9 et 10 ; exercices 13 et 14.

Livrable : calculer les espaces tangents par dérivation des contraintes, puis
établir les réciproques grâce à exp(tX). Développer le commutateur à l’ordre 2.
Faire le lien avec les commutateurs du volet Rubik, en distinguant les deux cadres.

## Séance 6 · Extension : l’intégrale gaussienne étendue · 60 min

Ouvrir **Gaussienne étendue**, puis **Exemple calculable**. Vérifier le résultat à
la main. Faire varier B₁ et B₂ : prédire le centre et la tangente à log I. Tourner
les axes ; augmenter la dimension puis la précision des axes suivants.

Lire les leçons 11 et 12. Faire les exercices 15 et 16. Livrable : compléter le
carré, diagonaliser, calculer la jacobienne et justifier les dérivées sous l’intégrale.
Interpréter les dérivées comme moments et covariance, en lien avec le volet probabilités.
Séparer la borne de troncature de l’erreur de quadrature observée.

## Séance 7 · Spé : les hypothèses d’intégration · 45 min

Dans **Green & Fubini**, retrouver l’orientation positive et la circulation −13/60.
Calculer par la frontière puis par le domaine ; inverser le sens. Exercice 17.

Ouvrir **Coupure symétrique**, puis **Coupures inégales**. Faire tendre les coupures
avec des vitesses différentes. Leçons 13 et 14 ; exercice 18. Livrable : expliquer
la divergence de l’intégrale absolue et le statut des deux intégrales itérées.

## Pour un oral

Choisir une figure, formuler précisément le résultat, annoncer ses hypothèses puis
donner une preuve de cinq minutes. Expliquer ce que le calcul numérique confirme
et ce qu’il ne peut pas prouver. Les corrections du recueil sont un bon exercice
de contrôle : vérifier une dérivée, un signe et une classification avant de conclure.
