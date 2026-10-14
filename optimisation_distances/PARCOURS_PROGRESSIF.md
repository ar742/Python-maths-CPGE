# Distances & Optimisation : un parcours sup / spé

Choisir l’objet et la distance avant de chercher un minimum. Commencer par projections et inégalités, puis traiter les contraintes et les certificats numériques.

Prévoir 60 à 90 minutes par séance prioritaire, avec une justification rédigée. Les approfondissements et les branches au-delà du programme se choisissent ensuite, indépendamment.

Les techniques incontournables sont celles de MPSI / MP : intégration, projection sur un sous-espace de dimension finie, compacité, théorème spectral et optimisation sous une contrainte régulière. Une séance prioritaire ne rend pas obligatoire tout son laboratoire. Approximation uniforme, algorithmes de descente, équation séculaire et séparation à marge maximale restent des compléments.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : produit scalaire, norme, projection orthogonale, intégration et calcul matriciel.
- Sup : inégalités, trigonométrie et changement de repère orthonormé.
- Spé : compacité, matrices symétriques, gradient et optimisation sous contrainte.

## Pour chaque séance

1. Lire les objets, les notations et les hypothèses du TP.
2. Prévoir un résultat sur papier, puis ouvrir l’expérience.
3. Modifier un seul réglage et expliquer son effet par un calcul ou un théorème.
4. Conclure par une courte preuve et distinguer résultat exact, approximation et observation.

## Sup : trois séances de projection et d’inégalités

Chercher des cas que l’on peut calculer exactement avant d’explorer les réglages généraux.

### 1. Approcher cosinus : définir le critère

**Techniques incontournables** · Sup · intégration et norme

Distinguer erreur quadratique intégrée et plus grand écart.

**À faire :** Noter t la variable, L=π/2 la borne et p(t)=at+b la droite d’essai. Fixer le degré à 1 et le poids κ à 0. Écrire I(a,b)=∫₀ᴸ(cos t−at−b)²dt ; calculer les intégrales nécessaires puis comparer deux droites d’essai.

**Acquis attendu :** Expliquer pourquoi √I est une distance et pourquoi I est une quadratique en a,b.

**Limites et compléments :** Commencer par l’erreur intégrée. La droite minimax dorée correspond à un autre critère et sera étudiée en complément.

**TP associés :** Approcher cosinus, choisir une norme

### 2. Deux projections : fonctions et matrices

**Techniques incontournables** · Sup · orthogonalité

Utiliser l’orthogonalité pour identifier un meilleur approximant.

**À faire :** Pour le cosinus, imposer l’orthogonalité du résidu aux fonctions 1 et t. Pour une matrice réelle M, écrire M=S+A avec S=(M+Mᵀ)/2 et A=(M−Mᵀ)/2 ; employer le produit scalaire de Frobenius, somme des produits des coefficients.

**Acquis attendu :** Démontrer l’orthogonalité de S et A et retrouver la distance d’une rotation d’angle θ aux matrices symétriques : √2|sin θ|.

**Limites et compléments :** Les projections sont prioritaires ; la contrainte det A=1, le mode complexe et le conditionnement seront repris plus tard.

**TP associés :** Approcher cosinus, choisir une norme ; Projeter une matrice, optimiser une distance

### 3. Une boîte maximale dans un ellipsoïde

**Techniques incontournables** · Sup · inégalité et substitution

Séparer la géométrie des demi-axes et l’optimisation des coordonnées réduites.

**À faire :** Prendre les demi-axes a=3,b=2,c=1 et les trois exposants égaux à 1. Pour un point (x,y,z) de la surface, poser u=x²/a², v=y²/b², w=z²/c². Utiliser u+v+w=1 pour majorer uvw.

**Acquis attendu :** Obtenir le volume maximal 8abc/(3√3), identifier les huit choix de signes et justifier l’égalité.

**Limites et compléments :** L’inégalité arithmético-géométrique peut être démontrée dans le TD. Les exposants quelconques et les multiplicateurs restent facultatifs à ce palier.

**TP associés :** De la sphère à l’ellipsoïde

## Spé : trois séances pour contrôler un extremum

Ajouter existence, condition nécessaire et justification globale.

### 4. Surface, solide et existence des extrema

**Techniques incontournables** · Spé · compacité et continuité

Déterminer sur quel ensemble la distance est minimisée avant de calculer.

**À faire :** Noter p le point extérieur ou intérieur et C le centre de l’ellipsoïde. Sur une sphère de rayon r, comparer distance à la surface et distance au solide. Choisir ensuite p=C et trois demi-axes distincts ; prévoir les extrema sur la surface.

**Acquis attendu :** Justifier l’existence par continuité sur un compact ; retrouver les petit et grand demi-axes au centre et la distance nulle au solide.

**Limites et compléments :** Le calcul général entre deux ellipsoïdes est facultatif. La compacité et la distinction des ensembles sont les objectifs de cette séance.

**TP associés :** Les points les plus proches et les plus éloignés ; La distance entre deux ellipsoïdes

### 5. Optimiser sous une contrainte régulière

**Techniques incontournables** · Spé · gradients et Lagrange

Écrire des conditions nécessaires sans les confondre avec une preuve de minimum global.

**À faire :** Pour l’ellipsoïde, noter g(x,y,z)=x²/a²+y²/b²+z²/c²−1 la contrainte. Vérifier ∇g≠0 sur la surface. Retrouver les candidats du produit de coordonnées puis écrire les équations pour la distance au carré à p.

**Acquis attendu :** Contrôler la contrainte, comparer les valeurs candidates et retrouver une justification globale dans les cas élémentaires.

**Limites et compléments :** Les multiplicateurs pour une contrainte régulière sont au programme MP. L’équation séculaire et ses cas singuliers sont des prolongements du calcul général.

**TP associés :** De la sphère à l’ellipsoïde ; Les points les plus proches et les plus éloignés

### 6. La dimension change l’existence

**Techniques incontournables** · Spé · déterminant et théorème spectral

Vérifier que l’ensemble contraint existe, puis exploiter une matrice positive.

**À faire :** Noter A une matrice réelle antisymétrique de taille n et imposer det A=1. Comparer n=3 puis n=4. Pour n pair, utiliser les valeurs propres positives de AᵀA et leur produit pour obtenir ‖A‖F≥√n.

**Acquis attendu :** Prouver que l’ensemble est vide en dimension impaire ; construire un exemple atteignant √n en dimension paire.

**Limites et compléments :** La distance de cet ensemble particulier est un exercice guidé. En complexe, transposée et adjoint doivent être distingués avant de réutiliser la preuve.

**TP associés :** Projeter une matrice, optimiser une distance

## Approfondissements : deux critères et une précision

Réutiliser le socle dans des méthodes fournies.

### 7. L² et uniforme ne choisissent pas la même droite

**Approfondissement CPGE** · Sup / Spé · convexité et extrema

Comprendre comment la norme choisie modifie le meilleur approximant.

**À faire :** Garder L=π/2, degré 1 et κ=0. Comparer la projection verte et la droite uniforme dorée ; étudier le résidu aux extrémités et à ses points critiques. Puis rendre le poids κ positif et expliquer quelle droite dépend de ce poids.

**Acquis attendu :** Relier les contacts du résidu uniforme à une majoration sur tout l’intervalle ; distinguer ce contrôle d’un maximum simplement échantillonné.

**Limites et compléments :** Le résultat général d’alternance en approximation uniforme n’est pas au programme. La construction affine du TP est un exemple accompagné.

**TP associés :** Approcher cosinus, choisir une norme

### 8. Un calcul doit rendre des comptes

**Approfondissement CPGE** · Spé · Cauchy–Schwarz et majoration

Lire une borne inférieure et une valeur admissible pour contrôler un minimum.

**À faire :** Choisir « Deux sphères ». Noter D la distance des centres et r₁,r₂ leurs rayons ; retrouver max(0,D−r₁−r₂). Comparer les bornes affichées L et U, puis passer aux ellipsoïdes d’axes distincts.

**Acquis attendu :** Expliquer pourquoi deux points admissibles donnent une borne supérieure et une projection sur une direction unitaire une borne inférieure.

**Limites et compléments :** Les bornes du logiciel sont en virgule flottante, sans arithmétique d’intervalles. Un écart petit contrôle le problème numérique, pas une certification exacte de tous les arrondis.

**TP associés :** La distance entre deux ellipsoïdes

## Au-delà : trois pistes au choix

Le programme fournit les outils pour entrer dans ces branches ; les théories nouvelles restent facultatives.

### A. Descente de gradient et conditionnement

**Au-delà du programme** · Au-delà · optimisation numérique

Relier le pas d’un algorithme à la géométrie d’une quadratique.

**À faire :** Suivre la descente dans le plan des paramètres a,b. Comparer l’arrivée à l’optimum exact, puis augmenter le degré et regarder le conditionnement de la matrice de Gram et de la base normalisée.

**Acquis attendu :** Distinguer mauvais choix de pas, sensibilité des coordonnées et existence d’un minimum unique.

**Limites et compléments :** Algorithmes de descente, QR et analyse générale du conditionnement sont des compléments numériques.

**TP associés :** Approcher cosinus, choisir une norme

### B. Distance générale à un ellipsoïde

**Au-delà du programme** · Au-delà · équation séculaire et cas singuliers

Traiter des extrema avec plusieurs axes et des multiplicateurs singuliers.

**À faire :** Partir d’un point extérieur, puis du centre et d’un axe principal. Lire le tableau de contrainte, de stationnarité et de matrice de preuve ; comparer un cas régulier et un cas singulier.

**Acquis attendu :** Identifier ce qui garantit un extremum global, même quand plusieurs points réalisent la même distance.

**Limites et compléments :** La résolution de l’équation séculaire et son traitement singulier sont fournis, au-delà des techniques exigibles.

**TP associés :** Les points les plus proches et les plus éloignés

### C. Séparation et marge maximale

**Au-delà du programme** · Au-delà · convexité et apprentissage

Relier la distance entre deux convexes à une direction séparatrice.

**À faire :** Choisir des ellipsoïdes disjoints et orientés différemment. Comparer leur segment minimal au segment des centres ; examiner le plan médian et la marge affichée. Faire ensuite se recouvrir les solides.

**Acquis attendu :** Expliquer la disparition d’une séparation stricte et distinguer distance des solides et distance des surfaces.

**Limites et compléments :** Fonctions support, dualité convexe et SVM à marge maximale sont des prolongements ; les calculs de Cauchy–Schwarz restent le point d’entrée.

**TP associés :** La distance entre deux ellipsoïdes

## Repères de programme

- [Programme officiel de mathématiques MPSI](https://prepas.org/ups.php?document=69)
- [Programme officiel de mathématiques MP](https://prepas.org/ups.php?document=85)
