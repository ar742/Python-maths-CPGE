# Un deuxième parcours en 60 minutes

Lancer `Lancer_Optimisation.cmd` depuis la racine, ou suivre [le lancement manuel](LISEZ_MOI.md).
Toutes les expériences se trouvent dans les onglets de la même application.

## 0–15 min · Le TP de cosinus

1. Garder l'intervalle [0,π/2], le degré 1 et le poids 0. Retrouver les coefficients du TP.
2. Comparer **I** et la **distance L²** : quelle relation les relie ?
3. Comparer les droites verte et dorée. Refaire la preuve par les trois erreurs alternées de la droite uniforme.
4. Passer au degré 3, puis 6. Observer l'erreur et le conditionnement en monômes.
5. Augmenter le poids κ : l'erreur près de la droite de l'intervalle compte davantage.

Leçons 2–4 ; exercices 1–4.

## 15–25 min · Matrices et dimension impaire

1. Faire varier θ. Retrouver le minimum et le maximum de la distance à S₃.
2. En dimension 3, expliquer pourquoi l'ensemble antisymétrique de déterminant 1 est vide.
3. Passer à n=4 : retrouver la borne √n avec les deux blocs J.
4. Déformer avec η : le déterminant reste 1, tandis que la norme augmente.
5. Activer le mode complexe, remettre η=0 et varier φ : distinguer transpose et adjoint.

Leçons 5–6 ; exercices 5–8.

## 25–35 min · Ellipsoïde et boîte maximale

1. Choisir « Ellipsoïde 3,2,1 ». Justifier les huit sommets et le volume maximal.
2. Déplacer le point avec longitude et latitude ; comparer sa valeur au maximum.
3. Choisir |x|²|y||z| : prédire les fractions optimales avant de lire le résultat.

Leçon 7 ; exercices 9–10.

## 35–45 min · Un point face à une surface

1. Faire tourner l'ellipsoïde ; observer que les deux extrema changent.
2. Choisir « Au centre ». Pourquoi les multiplicateurs deviennent-ils singuliers ?
3. Comparer la distance minimale à la surface et celle au solide.
4. Vérifier le cas de la sphère : distances |‖p−c‖−r| et ‖p−c‖+r sur la surface.

Leçon 8 ; exercice 11.

## 45–60 min · Deux ellipsoïdes et SVM

1. Garder les centres et axes distincts. Lire les bornes L,U et leur écart.
2. Faire tourner E₂ : pourquoi le segment minimal ne suit-il pas en général la droite des centres ?
3. Choisir les deux sphères et vérifier la distance avec la formule connue.
4. Approcher E₂, puis choisir les solides qui se recouvrent : interpréter le minimum annoncé.
5. Pour le cas séparé, retrouver le plan médian et sa marge. Relier ce problème au SVM de la fiche.
6. Exporter un résultat JSON pour conserver les paramètres et les contrôles.

Leçons 9–10 ; exercices 12–14. Les formules de support constituent l'ouverture de spé.
