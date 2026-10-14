# Électricité & Technologies : un parcours progressif sup / spé

Commencer par les circuits, leurs bilans et les limites des mesures. Relier ensuite temps, fréquence, électronique et acquisition. L’asservissement se construit depuis un modèle simple de moteur; les commandes avancées et la synthèse générale de filtres restent des branches.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.

Repères de physique PTSI, PSI et PT, avec les fonctions de transfert et performances étudiées en sciences industrielles. Ils servent à situer les compétences, sans imposer une spécialisation de l’atelier. Le socle concerne circuits, mesures, ALI, signaux et boucles élémentaires. Les inversions générales de Laplace, la transformée en z, Routh, Nyquist, l’anti-saturation intégrale et les transistors petits signaux sont des prolongements accompagnés.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : lois des nœuds et des mailles, résistance, condensateur, bobine, énergie et régime sinusoïdal.
- Sup : nombres complexes, EDO d’ordres 1 et 2, gain, phase, constante de temps et mesure à l’oscilloscope.
- Spé : filtrage, modèles d’ALI et acquisition; schémas-blocs, fonctions de transfert et critères de performance en SI.

## Pour chaque séance

1. Définir le système, le domaine et les variables avec leurs unités avant tout réglage.
2. Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.
3. Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.
4. Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.

## Sup : quatre séances sur le circuit et sa mesure

Une réponse calculée ne vaut que pour les conventions, le modèle et les instruments annoncés.

### 1. Équilibrer un pont et mesurer une tension

**Techniques incontournables** · Sup · circuits résistifs

Utiliser deux diviseurs de tension et comprendre le zéro d’une mesure différentielle.

**À faire :** Équilibrer les quatre branches puis modifier une résistance. Prévoir le signe de la tension mesurée et comparer à la courbe de sensibilité.

**Acquis attendu :** Écrire les tensions dans le bon sens et vérifier le rapport d’équilibre.

**Limites et compléments :** Jauges, ponts d’impédances et influence détaillée d’un instrument sont des applications supplémentaires.

**TP associés :** Équilibrer un pont de Wheatstone

### 2. Relier transitoire, résonance et second ordre

**Techniques incontournables** · Sup · stockage, EDO et régime sinusoïdal

Reconnaître les régimes et relier l’amortissement à la réponse fréquentielle.

**À faire :** Commencer par la charge du RLC et ses données initiales. Comparer les trois régimes, puis repérer la résonance en courant et la confronter au gain du second ordre.

**Acquis attendu :** Distinguer réponse libre, réponse forcée et grandeur dont on cherche le maximum.

**Limites et compléments :** La position générale des pôles et l’inversion de Laplace sont des compléments; les équations élémentaires suffisent au travail de sup.

**TP associés :** RLC : charge, oscillation et amortissement ; RLC sinusoïdal : trouver la résonance ; Relier résonance et réponse d’un second ordre

### 3. L’appareil peut modifier ce qu’il mesure

**Techniques incontournables** · Sup · impédance et formation expérimentale

Relier charge d’un instrument, déphasage et fonctionnement d’une cascade.

**À faire :** Mesurer l’impédance avec les amplitudes et phases proposées. Comparer deux filtres reliés directement puis séparés par un suiveur.

**Acquis attendu :** Expliquer quand une association de filtres permet de multiplier les gains et quand les impédances l’empêchent.

**Limites et compléments :** En sup, le suiveur est un modèle fourni; ses limites de courant et de bande sont reprises en spé.

**TP associés :** Mesurer une impédance avec un GBF ; Suiveur et association de filtres

### 4. Séparer la commande et l’état initial

**Techniques incontournables** · Sup · EDO et conversion électromécanique

Contrôler les données initiales et les échanges d’énergie d’un moteur modélisé.

**À faire :** Comparer deux états initiaux pour une même entrée. Dans le moteur continu, écrire séparément le bilan électrique et le bilan mécanique avant de suivre courant et vitesse.

**Acquis attendu :** Distinguer transitoire et régime établi; identifier les termes de conversion et de dissipation.

**Limites et compléments :** Les formules de Laplace sont fournies comme autre écriture. Leur inversion générale n’est pas exigée en SI.

**TP associés :** Séparer l’entrée et l’état initial ; Relier courant et vitesse d’un moteur continu

## Spé : cinq séances sur électronique, signaux et boucles

Valider le régime de fonctionnement avant d’employer une relation entrée–sortie.

### 5. Un ALI amplifie sous conditions

**Techniques incontournables** · Spé · ALI et filtres analogiques

Établir une relation idéale puis tester bande, saturation et vitesse de balayage.

**À faire :** Calculer le gain inverseur ou sommateur par les nœuds. Augmenter fréquence et amplitude dans l’ALI réel, puis repérer le domaine où le montage intègre ou dérive.

**Acquis attendu :** Ne pas imposer l’égalité des tensions d’entrée hors du régime linéaire stable; expliquer la première limite rencontrée.

**Limites et compléments :** Décalage d’entrée et dérivateur amélioré sont des compléments; leurs détails ne sont pas un acquis supplémentaire obligatoire.

**TP associés :** ALI : gain, bande et limites ; Sommateur inverseur ; Intégrer et dériver une tension

### 6. Le retour peut donner une mémoire ou une oscillation

**Techniques incontournables** · Spé · non-linéarités et oscillateurs

Distinguer contre-réaction, hystérésis et auto-oscillation.

**À faire :** Tracer les deux seuils de Schmitt. Utiliser ces seuils pour calculer la période de l’astable, puis comparer au démarrage quasi sinusoïdal de Wien.

**Acquis attendu :** Suivre les états de saturation et expliquer ce qui fixe la période ou limite l’amplitude.

**Limites et compléments :** Les mécanismes physiques fins de stabilisation d’amplitude et les délais d’un comparateur sont des prolongements.

**TP associés :** Comparateur à hystérésis ; Oscillateur de relaxation ; Oscillateur à pont de Wien

### 7. Échantillonner puis filtrer sans perdre la question de mesure

**Techniques incontournables** · Spé · acquisition et filtrage numérique

Séparer repliement, quantification et mémoire d’un filtre.

**À faire :** Choisir une cadence admissible puis faire varier la résolution du convertisseur. Comparer ensuite moyenne finie et récurrence du passe-bas.

**Acquis attendu :** Écrire la règle de calcul de la sortie, préciser l’initialisation et expliquer le retard introduit.

**Limites et compléments :** La transformée en z et les résultats généraux de stabilité sont des branches. Les récurrences du filtre sont données et vérifiables directement.

**TP associés :** Distinguer repliement et quantification ; Construire un filtre à mémoire finie ; Suivre la mémoire d’un filtre récursif

### 8. Une boucle de moteur change les performances

**Techniques incontournables** · Sup / spé · schémas-blocs et asservissement

Relier gain de boucle, écart final et constante de temps.

**À faire :** Reprendre le moteur X avec puis sans retour négatif. Modifier un seul gain et prévoir l’effet sur précision et rapidité; comparer la sensibilité à une variation du moteur.

**Acquis attendu :** Établir la relation en boucle fermée et distinguer amélioration de performance et amplification du bruit.

**Limites et compléments :** Les sensibilités logarithmiques et la robustesse générale sont des compléments; rester au modèle fourni pour les conclusions quantitatives.

**TP associés :** Mesurer l’effet d’une contre-réaction ; Reprendre le moteur X de la fiche P17

### 9. Corriger sans oublier la stabilité

**Techniques incontournables** · Spé · performances et correction en SI

Comparer action proportionnelle et intégrale à partir d’un cahier des charges simple.

**À faire :** Choisir une consigne, comparer les réponses P et PI puis lire les marges sur la boucle ouverte. Vérifier précision, dépassement et temps de réponse.

**Acquis attendu :** Expliquer l’effet de l’intégrale sur l’écart permanent et le compromis avec la stabilité.

**Limites et compléments :** Commencer sans saturation. Anti-saturation intégrale, Routh et critère général de Nyquist sont réservés aux prolongements.

**TP associés :** Suivre une consigne avec un correcteur PI ; Lire les marges d’une boucle ouverte

## Quatre approfondissements techniques accompagnés

Choisir un TP principal par séance; les autres proposent des comparaisons pour un TD ou un travail personnel.

### A1. Choisir une conversion et vérifier ses puissances

**Approfondissement CPGE** · Spé · conversion, particulièrement PSI

Relier commutations, énergie de la charge et courant fourni par la source.

**À faire :** Choisir hacheur–moteur ou onduleur comme TP principal et vérifier les bilans. Comparer ensuite le rôle du transformateur et celui d’une compensation de puissance réactive.

**Acquis attendu :** Distinguer valeur moyenne, efficace, puissance active et facteur de puissance.

**Limites et compléments :** Hacheur et onduleur sont centraux en PSI; le triphasé détaillé est un contexte fourni. Harmoniques de puissance et modulation avancée ne sont pas requis.

**TP associés :** Hacheur série : alimenter une machine à courant continu ; Onduleur : commande pleine onde ou décalée ; Triphasé : tensions et transformateur ; Puissance : réduire le courant par compensation

### A2. Une diode fait changer les équations

**Approfondissement CPGE** · Sup / spé · circuits par morceaux

Identifier la conduction et la continuité de tension d’un condensateur.

**À faire :** Comparer redressement en pont et diode avec lissage RC. Refaire le bilan sur un intervalle de conduction puis de blocage. Tester le redresseur à ALI comme comparaison.

**Acquis attendu :** Choisir l’état d’une diode avant d’appliquer les lois de circuit et relier recharge, ondulation et charge.

**Limites et compléments :** Les schémas et modèles de diodes sont fournis; recouvrement réel et récupération après saturation sont des compléments.

**TP associés :** Redresser les deux alternances ; Diode et RC : suivre les états de conduction ; Redresseur de précision : valeur absolue

### A3. Transmettre sans confondre spectre et réflexion

**Approfondissement CPGE** · Spé · modulation et propagation

Relier un codage du signal et les conditions de transport dans une ligne.

**À faire :** Prévoir les bandes latérales d’une modulation d’amplitude puis tester une démodulation. Dans la ligne, comparer terminaison adaptée et réfléchissante.

**Acquis attendu :** Distinguer la fréquence de la porteuse, celle du message et le retard de propagation.

**Limites et compléments :** La modulation est au programme PSI. Détection détaillée par diode et équations générales des télégraphistes restent des modèles accompagnés.

**TP associés :** Transmettre un message par modulation d’amplitude ; Une ligne : propagation et réflexion

### A4. Passer d’un filtre continu à une réalisation

**Approfondissement CPGE** · Spé · modèles et filtrage

Comparer approximation temporelle et limites internes d’un filtre.

**À faire :** Augmenter le pas des trois discrétisations du passe-bas. Dans le filtre à trois ALI, sélectionner une bande puis surveiller chaque tension interne.

**Acquis attendu :** Expliquer pourquoi une bonne sortie apparente ne garantit pas l’absence de saturation dans le montage.

**Limites et compléments :** La transformation bilinéaire et la synthèse générale à variables d’état sont fournies comme compléments.

**TP associés :** Comparer trois discrétisations d’un passe-bas ; Filtre actif à trois ALI

## Trois branches au-delà du programme

Approfondir après avoir contrôlé les bilans, les signaux et les performances élémentaires.

### P1. Pôles numériques, saturation et isolation active

**Au-delà du programme** · Au-delà · commande et plan z

Étudier ce que le modèle idéal de boucle ne prend pas en compte.

**À faire :** Déplacer un pôle numérique et suivre la réponse. Tester ensuite saturation et accumulation de l’intégrale. Dans l’isolation sismique, comparer atténuation utile et domaine du retour idéal.

**Acquis attendu :** Séparer stabilité linéaire, effets non linéaires de saturation et limites physiques d’un correcteur.

**Limites et compléments :** Stabilité générale dans le plan z, anti-saturation et critères de Routh ou Nyquist sont des prolongements, pas des attendus généraux de SI.

**TP associés :** Placer les pôles et les zéros dans le plan z ; Suivre une consigne avec un correcteur PI ; Lire les marges d’une boucle ouverte ; Atténuer le mouvement du sol par un retour

### P2. Polariser un transistor et multiplier une tension

**Au-delà du programme** · Au-delà · modèles de composants

Comprendre un modèle qui dépend d’un point de fonctionnement ou d’une séquence de charge.

**À faire :** Pour le transistor, vérifier le régime avant le gain de petit signal. Pour le doubleur, suivre les deux charges et comparer tension à vide et sous charge.

**Acquis attendu :** Ne pas appliquer une linéarisation hors de son domaine et expliquer les pertes du multiplicateur chargé.

**Limites et compléments :** Transistor amplificateur, démarrage et asymétrie d’un multiplicateur sont des modèles fournis au-delà des attendus de physique PSI/PT.

**TP associés :** Transistor : polarisation et petits signaux ; Doubleur : charger deux condensateurs

### P3. De l’instrument idéal à la qualité du signal et de l’énergie

**Au-delà du programme** · Au-delà · limites et conception

Distinguer précision d’amplitude, distorsion, saturation et coût énergétique.

**À faire :** Comparer le signal utile aux tensions internes d’un filtre puis au spectre de sortie d’un onduleur. Examiner ce qu’une compensation fondamentale laisse des harmoniques.

**Acquis attendu :** Définir la grandeur de performance recherchée avant de choisir une amélioration.

**Limites et compléments :** Dimensionnement complet, bruit des composants et facteur de puissance général en régime déformé demandent une étude supplémentaire.

**TP associés :** ALI : gain, bande et limites ; Filtre actif à trois ALI ; Puissance : réduire le courant par compensation ; Onduleur : commande pleine onde ou décalée

## Repères de programme

- [Programme de physique-chimie PTSI, 2021](https://www.lyceedecachan.fr/wp-content/uploads/2023/07/Programme-PC-PTSI.pdf)
- [Programme de physique-chimie PSI, 2021](https://prepas.org/ups.php?document=94)
- [Programme de physique-chimie PT, 2021](https://prepas.org/ups.php?document=96)
- [Sciences industrielles PCSI–PSI, BO 2021, annexe 4](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm)
