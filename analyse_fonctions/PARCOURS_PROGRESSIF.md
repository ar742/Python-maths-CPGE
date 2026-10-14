# Fonctions & Équations : un parcours progressif sup / spé

En sup, identifier une fonction et résoudre une équation différentielle avec ses données initiales. En spé, vérifier les hypothèses des intégrales à paramètre et relier les systèmes linéaires à leurs modes. Les fonctions spéciales fournissent des applications; les ordres fractionnaires restent des prolongements.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Si deux TP sont associés, le second sert de comparaison ou de travail personnel. Les branches facultatives peuvent occuper plusieurs séances.

Repères MPSI et MP. Le socle concerne substitutions, continuité, EDO linéaires et théorèmes d’intégration ou de dérivation à paramètre. Gamma, bêta, zêta et Hermite sont des exemples définis dans les TP, pas des fonctions à connaître par cœur. Faà di Bruno général, calcul fractionnaire, fonctions de Green et théorie générale de Riccati ou de Cauchy–Lipschitz sont des compléments.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : logarithme, exponentielle, trigonométrie, continuité, dérivation et intégration sur un segment.
- Sup : équations différentielles linéaires d’ordres 1 et 2, données initiales et développements limités.
- Spé : intégrales impropres, domination, séries de fonctions, algèbre linéaire et réduction pour les systèmes.

## Pour chaque séance

1. Lire le but, les objets et les hypothèses avant de modifier un réglage.
2. Prévoir un résultat sur papier, puis comparer à la figure ou au certificat calculé.
3. Faire varier un seul paramètre et justifier ce qui change.
4. Conclure par une preuve courte : résultat, hypothèses et portée de l’expérience.

## Sup : quatre séances pour calculer et contrôler

Toujours préciser le domaine et les données initiales avant de proposer une formule.

### 1. Une équation fonctionnelle : choisir les substitutions

**Techniques incontournables** · Sup · équations et symétries

Exploiter les valeurs particulières et la continuité sans deviner trop tôt une forme de solution.

**À faire :** Comparer l’équation en un point, son opposé et aux valeurs particulières autorisées. Dans l’équation additive, obtenir les valeurs entières puis rationnelles et utiliser la densité.

**Acquis attendu :** Justifier le passage des rationnels aux réels par l’hypothèse de continuité.

**Limites et compléments :** Ces équations sont des exercices. Les solutions additives non régulières sont réservées au prolongement.

**TP associés :** Substituer −x : identifier une fonction sans la deviner ; Cauchy : une équation à deux variables détermine une droite

### 2. Transformer une équation sans changer le domaine

**Techniques incontournables** · Sup · logarithme, exponentielle et EDO

Choisir un changement de variable licite et conserver les conditions initiales.

**À faire :** Dans le premier TP, préciser quand un logarithme est autorisé puis ramener le produit à une somme. Dans d’Alembert, vérifier parité et valeurs initiales avant la réduction différentielle proposée.

**Acquis attendu :** Retrouver les familles sous les hypothèses annoncées et vérifier la formule dans l’équation de départ.

**Limites et compléments :** Les classifications fonctionnelles générales et les preuves sans régularité ne sont pas exigibles.

**TP associés :** Produit, logarithme, puissance : changer de variable pour résoudre ; D’Alembert : pourquoi apparaissent cosinus et cosinus hyperbolique ?

### 3. Facteur intégrant et donnée initiale

**Techniques incontournables** · Sup · EDO linéaires d’ordre 1

Résoudre une équation linéaire puis contrôler une approximation numérique.

**À faire :** Construire le facteur intégrant en dérivant le produit. Pour le TP du recueil, retrouver la solution exacte et comparer deux pas d’Euler à données initiales identiques.

**Acquis attendu :** Ajuster la constante avec la valeur initiale et distinguer solution exacte, approximation et erreur.

**Limites et compléments :** La preuve de l’ordre de Runge–Kutta et l’estimation générale d’erreur sont des compléments; la comparaison du pas est une expérience guidée.

**TP associés :** Facteur intégrant : transformer une EDO en intégrale ; Euler et RK4 : mesurer un ordre de convergence

### 4. Deux données pour un oscillateur

**Techniques incontournables** · Sup · EDO linéaires d’ordre 2

Construire une solution homogène et particulière sans perdre une condition initiale.

**À faire :** Comparer les régimes libres, puis un forçage sinusoïdal. Calculer les constantes initiales. Dans la variation des constantes, vérifier la solution particulière proposée par substitution.

**Acquis attendu :** Donner la solution complète et contrôler l’équation, la valeur initiale et la dérivée initiale.

**Limites et compléments :** En sup, vérifier une solution particulière proposée. La méthode de variation des constantes est à travailler en spé, séance 8. Convolution et transformée de Laplace restent des applications facultatives.

**TP associés :** Oscillateur : transitoire, résonance et travail ; Variation des constantes : un noyau de Green initial

## Spé : quatre séances sur les hypothèses et les modes

Trois séances appliquent séparément les théorèmes de continuité, de dérivation et de dérivations successives à paramètre.

### 5. Continuité d’une intégrale à paramètre

**Techniques incontournables** · Spé · domination et continuité

Chercher une domination locale intégrable et comprendre pourquoi la limite ponctuelle ne suffit pas.

**À faire :** Écrire les hypothèses sur l’intégrande et le paramètre. Comparer l’intégrale gaussienne au contre-exemple concentré et expliquer la masse qui échappe à la limite.

**Acquis attendu :** Nommer le théorème applicable et produire un majorant indépendant du paramètre sur un voisinage.

**Limites et compléments :** Fourier de la gaussienne et convergence de mesures sont des compléments; les exemples n’imposent aucune théorie nouvelle.

**TP associés :** Théorème 1 : continuité d’une transformée gaussienne ; Théorème 1 : une masse qui se concentre interdit le passage à la limite

### 6. Dériver pour calculer une intégrale

**Techniques incontournables** · Spé · dérivation à paramètre

Remplacer une intégrale difficile par une dérivée plus simple puis fixer la constante.

**À faire :** Pour Frullani, étudier d’abord les deux extrémités et la compensation. Construire un majorant de la dérivée sur un compact de paramètres, intégrer la relation puis utiliser une valeur de référence.

**Acquis attendu :** Justifier la dérivation et la constante; ne pas séparer deux intégrales divergentes dont la différence converge.

**Limites et compléments :** La limite d’Abel au bord de l’intégrale oscillante est un approfondissement, pas une conséquence automatique du théorème local.

**TP associés :** Théorème 2 : Frullani, un logarithme retrouvé par dérivation ; Théorème 2 : transformer une intégrale oscillante en arctangente

### 7. Plusieurs dérivations sous l’intégrale

**Techniques incontournables** · Spé · régularité et Cauchy–Schwarz

Contrôler chaque dérivée par un majorant intégrable sur le domaine annoncé.

**À faire :** Choisir un compact de paramètres strictement dans le domaine. Écrire les intégrandes dérivés puis vérifier leur domination. Utiliser Cauchy–Schwarz pour la convexité du logarithme de gamma.

**Acquis attendu :** Distinguer régularité à tout ordre sur le domaine et comportement au bord; justifier le signe ou la convexité demandée.

**Limites et compléments :** Digamma, trigamma et monotonie complète sont des noms complémentaires. Laplace sert ici d’exemple d’intégrale à paramètre.

**TP associés :** Théorème 3 : dérivées de Γ, moments logarithmiques et convexité ; Théorème 3 : dérivées de Laplace et monotonie complète

### 8. Variation des constantes et modes d’un système

**Techniques incontournables** · Spé MP · systèmes différentiels et réduction

Construire une solution particulière d’ordre 2, puis relier un système linéaire à ses modes et à ses bilans.

**À faire :** Dans la variation des constantes, calculer le wronskien de la base homogène et les dérivées des deux coefficients variables. Puis, dans le système à trois composantes, écrire et sommer les bilans; comparer les modes rapides et lents.

**Acquis attendu :** Ajuster les deux données initiales d’ordre 2; dans le système, vérifier la conservation et expliquer le rôle des valeurs propres.

**Limites et compléments :** La variation des constantes d’ordre 2 et les systèmes linéaires relèvent du programme MP. La théorie générale des réseaux de diffusion et de la positivité des générateurs est un prolongement.

**TP associés :** Variation des constantes : un noyau de Green initial ; Trois réservoirs : conservation, modes et exponentielle

## Trois approfondissements avec les techniques de CPGE

Des fonctions définies sur place permettent de réinvestir intégration par parties, séries et dérivation.

### A1. Gamma, bêta et zêta comme exercices d’intégration

**Approfondissement CPGE** · Spé · intégrales, séries et restes

Déterminer les domaines avant d’utiliser une récurrence ou une interversion.

**À faire :** Retrouver la factorielle par intégration par parties. Pour zêta, encadrer le reste de la série. Comparer ensuite les formules intégrales de bêta et zêta aux valeurs calculées.

**Acquis attendu :** Accompagner chaque approximation d’une borne et justifier chaque changement de variable ou interversion.

**Limites et compléments :** Les fonctions sont définies dans les TP. Leur prolongement analytique et les théorèmes généraux de caractérisation sont au-delà.

**TP associés :** Gamma : prolonger la factorielle et contrôler une intégrale impropre ; Bêta : un changement de variables relie deux intégrales ; Zêta : une somme approchée n’est pas encore une valeur certifiée ; Zêta et gamma : de la série à une intégrale de Planck

### A2. Une formule doit rester sur le bon intervalle

**Approfondissement CPGE** · Sup / spé · EDO et domaines

Repérer les divisions interdites et les singularités d’une substitution.

**À faire :** Dans chaque équation, relever les points exclus et travailler sur un intervalle autorisé. Vérifier les formules fournies par dérivation, puis tester ce qui se passe près du bord.

**Acquis attendu :** Contrôler l’équation initiale après changement de variable et expliquer pourquoi une formule locale ne définit pas automatiquement une solution globale.

**Limites et compléments :** Frobenius, classification des points singuliers et théorie générale de Riccati sont des prolongements.

**TP associés :** Euler–Cauchy : singularités et série entière ; EDO homogène et Riccati : deux changements de fonction

### A3. Dériver une gaussienne et reconnaître une récurrence

**Approfondissement CPGE** · Sup / spé · dérivées, polynômes et intégration par parties

Faire apparaître des polynômes par dérivations successives et vérifier leurs propriétés.

**À faire :** Calculer les trois premières dérivées de la gaussienne, retrouver les signes et la parité. Vérifier une relation de récurrence et un cas d’orthogonalité par intégrations par parties.

**Acquis attendu :** Expliquer la convention choisie pour Hermite et vérifier les coefficients sans se contenter du calcul automatique.

**Limites et compléments :** La formule générale de Faà di Bruno et les polynômes de Bell ne sont pas exigibles; commencer par les dérivées composées d’ordres 2 et 3.

**TP associés :** Hermite : dériver une gaussienne, compter des zéros et construire une base ; Faà di Bruno : organiser les dérivées sans perdre les coefficients

## Trois branches au-delà du programme

Pour un TIPE ou une lecture accompagnée, choisir une branche après les séances prioritaires.

### P1. Unicité, explosion et solutions maximales

**Au-delà du programme** · Au-delà · EDO non linéaires

Comprendre pourquoi une donnée initiale ne suffit pas toujours et pourquoi une solution peut avoir une durée de vie finie.

**À faire :** Vérifier directement deux solutions du contre-exemple d’unicité. Comparer ensuite le modèle qui explose et celui qui sature; calculer les intervalles maximaux à partir des formules.

**Acquis attendu :** Séparer existence, unicité, stabilité et existence globale.

**Limites et compléments :** Le théorème général de Cauchy–Lipschitz et les résultats globaux sur les EDO non linéaires ne sont pas des exigences supplémentaires de MPSI / MP.

**TP associés :** Une condition initiale ne suffit pas toujours ; Solution maximale : explosion ou saturation ; EDO homogène et Riccati : deux changements de fonction

### P2. Deux points, une fonction de Green

**Au-delà du programme** · Au-delà · problèmes aux limites

Comparer données au même point et conditions aux deux extrémités d’un intervalle.

**À faire :** Modifier le paramètre du problème aux bords et distinguer solution unique, aucune solution et infinité de solutions. Vérifier la condition intégrale quand l’homogène devient dégénérée.

**Acquis attendu :** Expliquer pourquoi l’unicité d’un problème initial ne garantit pas celle d’un problème aux limites.

**Limites et compléments :** Fonctions de Green, alternative de Fredholm et théorie spectrale des opérateurs sont introduites comme prolongements.

**TP associés :** Deux bords : existence, unicité et résonance ; Variation des constantes : un noyau de Green initial ; Euler–Cauchy : singularités et série entière

### P3. Mémoire et dérivées d’ordre non entier

**Au-delà du programme** · Au-delà · calcul fractionnaire et combinatoire

Distinguer une dérivée locale d’un opérateur qui dépend du passé et comparer deux conventions.

**À faire :** Commencer par les ordres entiers, puis faire varier l’ordre réel de l’intégrale. Comparer la dérivée d’une constante dans les deux définitions. En complément, vérifier les premiers termes de Faà di Bruno.

**Acquis attendu :** Nommer le noyau, les conditions initiales et la convention avant de comparer les résultats.

**Limites et compléments :** Riemann–Liouville, Caputo, polynômes de Bell et formule générale de Faà di Bruno sont hors programme et ne deviennent pas des résultats à mémoriser.

**TP associés :** Intégrer une demi-fois : un noyau pondère toute l’histoire ; Caputo et Riemann–Liouville : que devient une constante ? ; Faà di Bruno : organiser les dérivées sans perdre les coefficients

## Repères de programme

- [Programme de mathématiques MPSI / MP2I](https://prepas.org/ups.php?document=69)
- [Programme de mathématiques MP](https://prepas.org/ups.php?document=85)
