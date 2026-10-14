# Mécanique & Mouvements : un parcours progressif sup / spé

Choisir les bons bilans en sup, puis étudier contacts, référentiels et petites oscillations en spé. Les applications astrophysiques et les anharmonicités relient les calculs à des situations concrètes. La rotation spatiale et les bifurcations avancées restent des branches accompagnées.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.

Repères PCSI et PC, avec MPSI pour les forces centrales et le solide en rotation autour d’un axe fixe. Le socle porte sur énergie, quantité de mouvement, moment cinétique, oscillations et choix du référentiel. Masse réduite, König général, tenseur d’inertie et modèles de roulement sont explicités quand ils dépassent ces attendus; leur présence dans un TP ne les rend pas obligatoires pour toutes les filières.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : deuxième loi de Newton, énergie mécanique, moment cinétique, gravitation et mouvement circulaire.
- Sup : oscillateur harmonique, radians, dérivation, développements limités et rotation autour d’un axe fixe.
- Spé : bilans vectoriels, référentiels non galiléens selon la filière, stabilité d’un équilibre et petites oscillations.

## Pour chaque séance

1. Définir le système, le domaine et les variables avec leurs unités avant tout réglage.
2. Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.
3. Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.
4. Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.

## Sup : quatre séances pour choisir le bon bilan

Définir le système et le référentiel avant d’utiliser une conservation.

### 1. Une orbite se lit avec deux invariants

**Techniques incontournables** · Sup · gravitation et forces centrales

Relier énergie et moment cinétique à la forme accessible d’une trajectoire.

**À faire :** Commencer par une orbite circulaire puis changer la vitesse de lancement. Comparer les aires balayées et les points de rebroussement du potentiel effectif.

**Acquis attendu :** Justifier les conservations et distinguer orbite liée, trajectoire de fuite et région inaccessible.

**Limites et compléments :** L’équation générale des coniques et la résolution de Kepler sont fournies; en sup, priorité aux bilans et aux cas simples.

**TP associés :** Kepler : suivre une planète et mesurer les aires balayées ; Lancement orbital : lire les points de rebroussement

### 2. Quand le petit angle devient insuffisant

**Techniques incontournables** · Sup · énergie et oscillateur harmonique

Construire la linéarisation et identifier sa limite d’utilisation.

**À faire :** Comparer deux petites amplitudes puis une amplitude plus grande. Retrouver l’équation harmonique et utiliser l’énergie pour expliquer le ralentissement près du sommet.

**Acquis attendu :** Vérifier la période harmonique et exprimer les angles en radians avant toute approximation.

**Limites et compléments :** L’intégrale exacte de période est fournie. Sa nature elliptique n’est pas une connaissance préalable.

**TP associés :** Pendule : mesurer la période sans petit angle

### 3. Une barre tourne autour d’un axe fixe

**Techniques incontournables** · Sup · énergie et moment cinétique

Choisir un axe et relier moment d’inertie, couple et énergie de rotation.

**À faire :** Définir l’axe de la barre et écrire le bilan énergétique. Dans le nuage de masses, calculer les distances à un axe fixé puis comparer deux axes.

**Acquis attendu :** Ne pas confondre force et moment d’une force; vérifier les dimensions du moment d’inertie.

**Limites et compléments :** La matrice d’inertie et ses axes principaux sont réservés aux prolongements; le calcul autour d’un axe suffit ici.

**TP associés :** Une barre bascule : énergie, durée et réaction du pivot ; Six masses : quel axe résiste le plus à la rotation ?

### 4. Deux objets échangent leur quantité de mouvement

**Techniques incontournables** · Sup · système et interactions mutuelles

Expliquer ce que conserve un système isolé et ce que chaque objet ne conserve pas seul.

**À faire :** Comparer deux masses égales puis très différentes. Calculer la quantité de mouvement totale et suivre le centre de masse dans le référentiel choisi.

**Acquis attendu :** Faire disparaître les forces internes dans le bilan total et distinguer mouvement d’ensemble et mouvement relatif.

**Limites et compléments :** Masse réduite et identités générales de König sont introduites en application, sans devenir des formules obligatoires pour toutes les voies.

**TP associés :** Deux étoiles : passer au centre de masse

## Spé : quatre séances sur les régimes et les approximations

Vérifier les hypothèses du régime avant d’en exploiter les équations.

### 5. Adhérer, glisser ou s’arrêter

**Techniques incontournables** · Sup / spé · PFD et lois de frottement

Distinguer frottement d’adhérence et frottement de glissement.

**À faire :** Avec la caisse, augmenter la traction puis l’inverser. Écrire le bilan sur un plan incliné et tester l’inégalité d’adhérence avant de choisir la loi de glissement.

**Acquis attendu :** Justifier chaque changement de régime et le sens de la dissipation.

**Limites et compléments :** Le roulement du solide du second TP est un complément guidé; commencer par la caisse en translation. Les attendus précis de Coulomb dépendent de la filière.

**TP associés :** Tirer, freiner puis inverser une caisse : changer de régime ; Glisser ou rouler sur un plan incliné ?

### 6. Une trajectoire dépend aussi du référentiel

**Techniques incontournables** · Spé PC · référentiels en rotation

Séparer force réelle et termes liés au référentiel tournant.

**À faire :** Comparer la même trajectoire dans les deux référentiels. Pour Foucault, modifier la latitude et prévoir le signe ainsi que la durée de précession.

**Acquis attendu :** Écrire correctement les produits vectoriels et distinguer période d’oscillation et période de précession.

**Limites et compléments :** La solution complexe détaillée de Foucault est une application fournie; les corrections géophysiques restent au-delà.

**TP associés :** Référentiel tournant : une droite peut devenir une courbe ; Foucault : oscillation rapide, précession lente

### 7. Plusieurs masses : chercher des mouvements simples

**Techniques incontournables** · Spé · équations couplées et modes propres

Construire des modes à partir des équations de chaque masse.

**À faire :** Commencer par une translation uniforme de la chaîne. Comparer ensuite les deux vibrations du modèle de CO₂ et vérifier les forces dans un mode choisi.

**Acquis attendu :** Relier chaque forme de vibration à une fréquence et identifier le mode de translation sans rappel.

**Limites et compléments :** L’orthogonalité pondérée par les masses est expliquée. Intensités spectroscopiques et théorie générale des phonons sont des prolongements.

**TP associés :** Une chaîne : modes propres, propagation et dispersion ; CO₂ : trois masses, deux vibrations et une translation

### 8. Linéariser, puis mesurer l’anharmonicité

**Techniques incontournables** · Spé · équilibre, stabilité et développement limité

Relier la courbure du potentiel aux petites oscillations et contrôler une correction.

**À faire :** Retrouver le terme cubique du pendule et comparer période harmonique et période corrigée. Dans les ressorts, chercher les équilibres et étudier leur stabilité par le potentiel.

**Acquis attendu :** Préciser l’amplitude utilisée et le domaine de l’approximation; ne pas conclure à l’instabilité lorsque la courbure est nulle.

**Limites et compléments :** La méthode générale de Lindstedt et les théorèmes de bifurcation sont des branches; les premiers développements utilisent les techniques de CPGE.

**TP associés :** Anharmonicité : période corrigée et troisième harmonique ; Deux ressorts : créer deux équilibres stables

## Trois applications accompagnées des bilans

Les formules orbitales ou de contact sont fournies quand elles dépassent le socle.

### A1. Changer d’orbite ou effectuer un survol

**Approfondissement CPGE** · Sup / spé · applications astrophysiques

Suivre l’énergie et la vitesse lors d’un changement de trajectoire.

**À faire :** Calculer les deux impulsions de Hohmann, puis comparer le survol dans le référentiel de la planète et dans celui de l’étoile.

**Acquis attendu :** Identifier le référentiel dans lequel l’énergie est conservée et celui dans lequel un gain ou une perte est possible.

**Limites et compléments :** L’optimalité générale des transferts et les fenêtres interplanétaires ne sont pas démontrées par ces deux modèles.

**TP associés :** Rejoindre une autre orbite : deux impulsions de Hohmann ; Survol gravitationnel : dévier sans moteur

### A2. Une différence de champ, une masse échangée

**Approfondissement CPGE** · Sup / spé · marées et propulsion

Choisir ce que l’on soustrait ou ce qui traverse la frontière du système.

**À faire :** Comparer attraction et différence d’attraction dans le TP marées. Pour la fusée, faire le bilan sur un court intervalle en incluant la masse éjectée.

**Acquis attendu :** Retrouver l’échelle du champ de marée et expliquer l’origine du logarithme dans la vitesse de la fusée.

**Limites et compléments :** Tenseur de marée, dislocation et optimisation d’une propulsion réelle demandent des modèles supplémentaires.

**TP associés :** Marées : comparer attraction et différence d’attraction ; Fusée : faire le bilan d’un système qui perd de la masse

### A3. Le mouvement du centre de masse ne suffit pas

**Approfondissement CPGE** · Sup / spé · solide et contact

Séparer translation et rotation puis déterminer jusqu’où un régime de contact reste valide.

**À faire :** Vérifier la décomposition d’énergie fournie par König. Pour le cylindre au bord, comparer les deux événements possibles et arrêter le modèle au premier seuil.

**Acquis attendu :** Contrôler à la fois réaction normale et condition de frottement; reconstruire les équations si le régime change.

**Limites et compléments :** König général et roulement spatial sont des compléments accompagnés. Les réactions calculées avant glissement ne valent pas après.

**TP associés :** Décomposer le mouvement d’un solide : les deux théorèmes de König ; Un cylindre au bord de la table : quel événement survient d’abord ? ; Glisser ou rouler sur un plan incliné ?

## Trois branches au-delà du programme

Choisir une branche après les bilans, les équilibres et la linéarisation.

### P1. Une raideur nulle et une résonance non linéaire

**Au-delà du programme** · Au-delà · changements d’échelle et bifurcations

Comprendre ce qui remplace l’approximation harmonique et ce qu’une courbe de réponse ne prouve pas.

**À faire :** Dans le potentiel quartique, comparer deux amplitudes et rechercher la loi d’échelle de période. Dans Duffing, comparer la réponse linéaire aux branches de balance harmonique.

**Acquis attendu :** Distinguer existence d’une réponse approchée, stabilité et réalisation dynamique.

**Limites et compléments :** Balance harmonique, bifurcations universelles, hystérésis et chaos nécessitent une étude supplémentaire; le dessin seul ne les établit pas.

**TP associés :** Au seuil : un oscillateur sans raideur linéaire ; Duffing : une résonance qui dépend de l’amplitude ; Deux ressorts : créer deux équilibres stables

### P2. La rotation spatiale d’un solide

**Au-delà du programme** · Au-delà · tenseur d’inertie et gyroscopes

Comprendre pourquoi le moment cinétique n’est pas toujours parallèle à la vitesse de rotation.

**À faire :** Comparer le cas plan de la barre au mouvement sur rotule. Pour la toupie, modifier la rotation propre et suivre précession et nutation.

**Acquis attendu :** Distinguer les invariants et les axes; contrôler les conditions qui permettent une précession régulière.

**Limites et compléments :** Tenseurs, équations d’Euler et réduction lagrangienne dépassent le modèle de rotation autour d’un axe fixe du socle.

**TP associés :** Une barre sur rotule : mouvement spatial et moment cinétique ; Toupie pesante : précession lente et nutation ; Six masses : quel axe résiste le plus à la rotation ?

### P3. Le temps devient difficile près d’une trajectoire limite

**Au-delà du programme** · Au-delà · séparatrices et calcul orbital

Comparer une représentation géométrique à une évolution à temps uniforme.

**À faire :** Approcher le sommet du pendule puis comparer les positions orbitales à des instants équidistants. En complément, suivre la déformation d’une impulsion dans la chaîne.

**Acquis attendu :** Expliquer pourquoi une trajectoire régulière peut correspondre à une vitesse très variable ou à une période divergente.

**Limites et compléments :** Intégrales elliptiques, résolution de Kepler et vitesse de groupe sont des prolongements dont les outils sont fournis.

**TP associés :** Pendule : mesurer la période sans petit angle ; Kepler : suivre une planète et mesurer les aires balayées ; Une chaîne : modes propres, propagation et dispersion

## Repères de programme

- [Physique PCSI, BO 2021, annexe 2](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm)
- [Physique MPSI, BO 2021](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm)
- [Programme de physique PC, 2021](https://prepas.org/ups.php?document=92)
