# Topologie & Ensembles : un parcours progressif sup / spé

En sup, partir des suites, de la densité et des valeurs intermédiaires. En spé, reformuler ces expériences avec ouverts, fermés, compacts et continuité. Les contre-exemples indiquent à quoi servent les hypothèses.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Si deux TP sont associés, le second sert de comparaison ou de travail personnel. Les branches facultatives peuvent occuper plusieurs séances.

Repères MPSI et MP. En sup, la topologie abstraite n’est pas présupposée. En MP, priorité aux espaces vectoriels normés, à la compacité et à la connexité par arcs. Suites de Cauchy, complétude, Banach, Borel–Lebesgue et connexité générale sont des prolongements, même lorsque leurs exemples se calculent avec les outils du programme.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : intervalles, suites, limites, suites extraites, continuité et théorème des valeurs intermédiaires.
- Sup : vecteurs, produit scalaire, matrices et inégalités de norme.
- Spé : définitions d’un espace vectoriel normé et caractérisation séquentielle; aucun cours d’espaces de Banach n’est requis.

## Pour chaque séance

1. Lire le but, les objets et les hypothèses avant de modifier un réglage.
2. Prévoir un résultat sur papier, puis comparer à la figure ou au certificat calculé.
3. Faire varier un seul paramètre et justifier ce qui change.
4. Conclure par une preuve courte : résultat, hypothèses et portée de l’expérience.

## Sup : trois séances à partir des nombres et des suites

Construire des exemples exacts avant d’introduire le vocabulaire de topologie de spé.

### 1. Approcher sans confondre densité et dénombrement

**Techniques incontournables** · Sup · nombres réels et suites

Approcher un réel par deux types de nombres et comprendre le sens de la densité.

**À faire :** Écrire les deux suites du TP qui approchent la cible réelle. Fixer une précision et trouver un rang convenable. Comparer à la liste finie de fractions affichée.

**Acquis attendu :** Prouver l’existence d’un rationnel et d’un irrationnel dans tout intervalle ouvert non vide.

**Limites et compléments :** Une liste finie ne prouve pas la dénombrabilité. En sup, son énumération est une illustration; les cardinalités infinies seront reprises ensuite.

**TP associés :** Approcher un réel par des rationnels et des irrationnels ; Lister les rationnels et approcher un réel

### 2. Extraire une suite et ajouter sa limite

**Techniques incontournables** · Sup · suites bornées et valeurs d’adhérence

Distinguer convergence de la suite et convergence d’une suite extraite.

**À faire :** Étudier séparément les termes pairs et impairs de la suite proposée. Puis comparer les points 1/n, pour les entiers n positifs, à ce même ensemble complété par 0.

**Acquis attendu :** Produire deux limites de suites extraites et expliquer pourquoi une limite peut manquer à l’ensemble de départ.

**Limites et compléments :** Le vocabulaire adhérence, fermé et compact sera formalisé en spé; la preuve de convergence reste élémentaire.

**TP associés :** Une suite bornée, deux limites de suites extraites ; Ajouter une limite pour fermer un ensemble

### 3. Une itération et le bon intervalle

**Techniques incontournables** · Sup · suites récurrentes et continuité

Étudier une récurrence avec un intervalle stable et contrôler une approximation.

**À faire :** Pour l’itération du cosinus, rechercher un intervalle stable et une borne d’erreur adaptée. Pour Héron, vérifier que les termes sont rationnels et étudier leur limite.

**Acquis attendu :** Utiliser la continuité au passage à la limite, après avoir justifié la convergence.

**Limites et compléments :** Le théorème général des contractions et la complétude de ℚ ne sont pas nécessaires au travail de sup.

**TP associés :** Résoudre x=cos(x) par une suite récurrente ; Héron : des fractions qui tendent vers √2

## Spé : cinq séances sur les définitions et les théorèmes

Rédiger avec les quantificateurs, un voisinage ou une suite; une figure sert à choisir la preuve.

### 4. Ouvert, fermé, intérieur et adhérence

**Techniques incontournables** · Spé MP · espaces normés

Reconnaître les quatre notions et préciser l’espace de travail.

**À faire :** Autour d’un point intérieur, construire un rayon admissible avec l’inégalité triangulaire. Comparer un bord inclus à un bord exclu. Étudier enfin l’intersection infinie des intervalles du TP.

**Acquis attendu :** Expliquer pourquoi un ouvert relatif peut ne pas être ouvert dans l’espace ambiant et pourquoi « fini » est essentiel pour certaines opérations.

**Limites et compléments :** Les exemples sont choisis dans des espaces normés; aucune théorie générale des espaces topologiques n’est requise.

**TP associés :** Choisir une boule autour d’un point ; Reconnaître un point intérieur ou adhérent ; Chercher un ouvert dans l’espace choisi ; Comparer une opération finie à une infinie

### 5. La compacité fait atteindre les bornes

**Techniques incontournables** · Spé MP · compacts et continuité

Appliquer fermé et borné en dimension finie, puis image continue d’un compact.

**À faire :** Comparer l’ellipse pleine avec et sans son bord. Calculer les bornes de la fonction linéaire du TP et décider si elles sont atteintes. Reprendre l’ellipse augmentée d’un segment.

**Acquis attendu :** Vérifier chaque hypothèse avant de conclure à un minimum ou à un maximum.

**Limites et compléments :** La fonction d’appui et la somme de Minkowski sont des noms complémentaires; la preuve repose sur produit et image continue de compacts.

**TP associés :** Une borne supérieure peut ne pas être atteinte ; Additionner deux compacts : une ellipse et un segment

### 6. Convexe, connexe par arcs : construire ou interdire

**Techniques incontournables** · Spé MP · chemins et valeurs intermédiaires

Distinguer un segment contenu dans un ensemble d’un chemin continu quelconque.

**À faire :** Chercher deux points dont le segment sort de l’ensemble non convexe. Construire un chemin dans le plan privé de 0, puis expliquer par le TVI pourquoi la droite privée de 0 se comporte autrement.

**Acquis attendu :** Employer une paire de points comme contre-exemple à la convexité et une fonction continue pour interdire un chemin.

**Limites et compléments :** La connexité générale sans chemins est réservée à un prolongement; le TP de niveaux est un exercice sur les arcs.

**TP associés :** Vérifier si un segment reste dans l’ensemble ; Construire un chemin qui évite un point ; Relier deux régions : le rôle d’un point de contact

### 7. Majorations et rôle de la dimension

**Techniques incontournables** · Spé MP · normes et applications linéaires

Prouver une continuité par une borne de norme et comprendre la portée de l’équivalence des normes.

**À faire :** Majorer la longueur de l’image d’un vecteur par la matrice du TP. Puis calculer les trois normes de la fonction x↦xⁿ sur [0,1], où n est un entier positif.

**Acquis attendu :** Expliquer pourquoi les normes considérées ne sont pas équivalentes sur l’espace entier des fonctions, sans contredire le théorème de dimension finie.

**Limites et compléments :** La décomposition en valeurs singulières et les espaces Lᵖ complétés sont des prolongements. Une majoration explicite suffit au socle.

**TP associés :** En dimension finie, une application linéaire est continue ; Converger en moyenne ne veut pas dire uniformément

### 8. Continuité, uniforme et lipschitzienne

**Techniques incontournables** · Spé MP · théorème de Heine

Savoir quelle constante dépend du point et ce qu’un compact permet d’uniformiser.

**À faire :** Comparer la fonction du TP sur un intervalle compact puis sur ℝ. Avec la racine carrée, chercher pourquoi une borne lipschitzienne échoue. Démontrer enfin que la distance à un ensemble est 1-lipschitzienne.

**Acquis attendu :** Rédiger les quantificateurs dans le bon ordre et distinguer continuité uniforme et Lipschitz.

**Limites et compléments :** La régularité de Hölder est un vocabulaire complémentaire; sa borne précise peut être vérifiée sans théorie nouvelle.

**TP associés :** Continuité uniforme : un même rayon pour tous les points ; Trouver les points les plus proches

## Deux approfondissements utilisant le socle

Matrices, barycentres et contre-exemples donnent des preuves accessibles avec les définitions de MP.

### A1. Des ensembles de matrices comme exemples

**Approfondissement CPGE** · Sup / spé · déterminant, norme et compacité

Employer continuité polynomiale, bornitude et TVI dans un espace de matrices.

**À faire :** Prouver séparément fermeture et bornitude des matrices orthogonales. Comparer aux matrices de déterminant 1. Puis suivre un déterminant réel le long d’un chemin.

**Acquis attendu :** Justifier la compacité du premier ensemble, le contre-exemple du second et l’obstacle au changement de signe sur ℝ.

**Limites et compléments :** La classification globale des composantes de GL et la décomposition polaire dépassent cette application des outils du programme.

**TP associés :** Quand un ensemble de matrices est-il compact ? ; Changer le signe du déterminant en restant inversible ?

### A2. Une distance est-elle atteinte et unique ?

**Approfondissement CPGE** · Spé · compacité, produit scalaire et contre-exemples

Distinguer existence d’un point minimisant, unicité et dimension finie.

**À faire :** Comparer les deux disques à un triangle convexe. Vérifier l’inégalité du produit scalaire fournie pour le point projeté. Puis calculer la distance entre deux fonctions de la boule non compacte.

**Acquis attendu :** Relier existence à la compacité quand elle s’applique et expliquer pourquoi fermé borné ne suffit plus en dimension infinie.

**Limites et compléments :** Le théorème général de projection sur un convexe fermé est un complément fourni. Espaces de Hilbert et théorème de Riesz sont au-delà.

**TP associés :** Trouver les points les plus proches ; Projeter sur un triangle ou un rectangle ; Fermée et bornée ne suffit plus en dimension infinie

### A3. Des points à leur enveloppe convexe

**Approfondissement CPGE** · Sup / spé · vecteurs et convexité

Construire des combinaisons convexes et interpréter leurs coefficients.

**À faire :** Déplacer les points du nuage puis modifier les poids du barycentre. Vérifier qu’ils sont non négatifs et de somme 1 avant de conclure que le barycentre reste dans le polygone.

**Acquis attendu :** Justifier par récurrence qu’une combinaison convexe finie de points d’un convexe reste dans cet ensemble.

**Limites et compléments :** Le théorème général de représentation de Carathéodory et la théorie des polytopes ne sont pas exigibles; les calculs utilisent seulement les vecteurs et la définition de convexité.

**TP associés :** Former un convexe à partir de points

## Trois branches au-delà du programme

Ces branches complètent les exemples, sans ajouter des théorèmes exigibles au parcours prioritaire.

### P1. Cauchy, complétude et contractions

**Au-delà du programme** · Au-delà · espaces complets

Comprendre comment de nouvelles formulations décrivent la convergence et l’existence.

**À faire :** Avec Héron, distinguer rapprochement des termes et appartenance de la limite à l’espace choisi. Comparer ensuite contraction, recouvrements ouverts du segment et extraction aléatoire.

**Acquis attendu :** Identifier l’hypothèse supplémentaire utilisée dans chaque formulation et séparer une simulation finie d’un énoncé infini.

**Limites et compléments :** Cauchy, complétude, Banach, Borel–Lebesgue et convergence presque sûre de l’extraction sont des compléments non exigibles en MP.

**TP associés :** Héron : des fractions qui tendent vers √2 ; Résoudre x=cos(x) par une suite récurrente ; Des intervalles ouverts couvrent-ils tout le segment ? ; Le TP : garder les termes qui se rapprochent de 1

### P2. Compter sans mesurer une longueur

**Au-delà du programme** · Au-delà · cardinalités et Cantor

Séparer densité, cardinalité et longueur dans trois constructions.

**À faire :** Expliquer pourquoi l’énumération rencontre toute fraction réduite. Rédiger l’argument diagonal pour une liste infinie puis suivre les étapes de Cantor.

**Acquis attendu :** Distinguer le tableau fini de la preuve infinie et expliquer pourquoi une longueur tendant vers zéro ne signifie pas un ensemble vide.

**Limites et compléments :** Les faits de dénombrabilité et de non-dénombrabilité figurent en MP; leurs preuves détaillées et les propriétés fines de Cantor sont proposées en prolongement.

**TP associés :** Lister les rationnels et approcher un réel ; Construire une suite absente de la liste ; Construire un compact en retirant des intervalles

### P3. Chemins, inverse continu et géométrie globale

**Au-delà du programme** · Au-delà · exemples topologiques

Voir les limites d’une intuition tirée d’un tracé ou d’une bijection.

**À faire :** Comparer les deux paramétrages du TP inverse, puis construire des suites proches d’une coupure. Étudier les limites verticales du sinus du topologue et le passage entre régions de niveau.

**Acquis attendu :** Distinguer continuité de l’application et de son inverse; séparer connexité générale et connexité par arcs.

**Limites et compléments :** Homéomorphismes, espaces de Hausdorff et classification globale des groupes sont des notions supplémentaires accompagnées.

**TP associés :** Un ensemble compact dans lequel certains points ne se relient pas ; Une bijection continue a-t-elle une réciproque continue ? ; Changer le signe du déterminant en restant inversible ? ; Relier deux régions : le rôle d’un point de contact

## Repères de programme

- [Programme de mathématiques MPSI / MP2I](https://prepas.org/ups.php?document=69)
- [Programme de mathématiques MP](https://prepas.org/ups.php?document=85)
