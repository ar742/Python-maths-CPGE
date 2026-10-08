# Douze missions : du passage à la limite à la chaîne de mesure

Chaque mission suit trois étapes : prédire sans calcul numérique, expérimenter avec les paramètres, justifier en citant les hypothèses du théorème. Les indications sup/spé se lisent selon la filière ; les prolongements sont introduits dans les cours associés.

## 1. Un maximum qui se cache — sup vers spé

Ouvrir **Le pic qui échappe au maillage**. Comparer n=15 et n=800, puis fixer δ=0,2. Localiser exactement le maximum par dérivation et expliquer pourquoi la norme sur [0,1] reste 1/2, tandis que celle sur [δ,1] tend vers zéro. Une image presque plate suffit-elle à conclure ?

## 2. Une aire que la limite oublie — spé

Ouvrir **La limite perd une unité d’aire**. Représenter la variable u=nx et calculer l’intégrale par changement de variable. Identifier précisément l’hypothèse manquante de la convergence dominée. Comparer avec l’exercice 12, où une domination existe.

## 3. Fabriquer un développement — spé, exercice 4

Ouvrir **Une EDO fabrique les coefficients**. Retrouver la récurrence dans `(1−x²)f′−xf=1`, calculer les quatre premiers termes impairs, puis comparer r=0,6 et r=0,98. Expliquer le rôle du rayon de convergence et du compact.

## 4. Sommer à une autre échelle — spé, exercice 5

Ouvrir **Une série entière à l’échelle e²x**. Montrer `n³log(1+2/n²)=2n−2/n+O(n⁻³)`. Prédire l’équivalent, puis comparer une somme tronquée avant le pic à une somme suffisamment longue. Justifier le passage de l’équivalent des coefficients à l’équivalent de la somme en isolant un nombre fini de termes.

## 5. Sortir des petites oscillations — spé, exercice 10

Passer de **Au-delà du binôme polynomial** au **Pendule elliptique**. Prédire si la période augmente ou diminue avec l’amplitude. Retrouver `I(k)=2K(k)` et `T/T₀=I(k)/π`, puis expliquer la divergence à l’approche de 180°. Comparer somme partielle, quadrature et mouvement calculé.

## 6. Additionner et dominer — spé, exercices 11 et 12

Calculer `∫₀∞t/sinh(t)dt` avec les aires des modes positifs, puis tester la convergence dominée sur une fonction complexe et une fonction à saut. Pour chaque échange limite–intégrale ou somme–intégrale, écrire la condition qui l’autorise. Encadrer le reste de la somme sur les entiers impairs.

## 7. Un circuit, trois entrées — sup physique vers spé, TP p.107

Ouvrir **RC : du calcul de Laplace à la réponse temporelle**. Comparer pas, impulsion et rampe ; changer y₀. Retrouver `(1+τp)Y=U+τy₀`, vérifier le saut dû à l’impulsion et le retard asymptotique aτ de la rampe. Relier ensuite gain et phase à la recomposition de trois harmoniques.

## 8. Un saut persistant — spé, séries de Fourier

Ouvrir **Gibbs et Fejér**, puis **Parseval**. Augmenter N sans confondre réduction de la largeur du dépassement et disparition de sa hauteur. Comparer le triangle continu au créneau ; retrouver les sommes en `1/n²` et `1/n⁴` par l’énergie.

## 9. Reconstruire sans perdre les facteurs — spé et prolongement, p.108

Ouvrir **Poisson : une gaussienne**, puis **Shannon**. Passer de la périodisation temporelle aux raies de Fourier, puis du peigne de mesure aux copies du spectre. Écrire les facteurs F et 1/F. Comparer un chevauchement spectral à une simple insuffisance du nombre de mesures utilisées pour reconstruire.

## 10. Concevoir une acquisition — sup physique vers spé et prolongement

Ouvrir **Repliement**, **Filtre antirepliement**, puis **FFT et fenêtrage**. Choisir F et la coupure analogique avant de mesurer. Comparer rectangle, Hann et Blackman sur une fréquence hors case. Expliquer ce que le gain cohérent corrige et ce qu’il ne corrige pas.

## 11. Résoudre ou localiser — spé et prolongement

Ouvrir **Résolution**, puis **Spectrogramme**. Comparer huit fois plus de zéros à huit fois plus de mesures. Sur le chirp, choisir une fenêtre pour suivre la fréquence, puis une autre pour distinguer des raies proches. La fenêtre optimale dépend-elle de la question posée ?

## 12. Transmettre, détecter, débruiter — prolongement interdisciplinaire

Explorer **Modulation**, **Corrélation et temps de vol**, puis **Débruiter**. Retrouver les bandes latérales, expliquer la perte en quadrature du récepteur, estimer le retard d’un écho bruité et convertir τ en cτ/2. Distinguer enfin bruit résiduel et déformation du signal utile ; comparer une variance théorique à une réalisation finie.
