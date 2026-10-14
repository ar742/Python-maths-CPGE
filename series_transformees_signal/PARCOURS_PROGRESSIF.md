# Séries & Signaux : un parcours progressif sup / spé

Partir de sommes finies et de signaux familiers. En spé, justifier les passages à la limite et les opérations sur les séries. Utiliser ensuite ces acquis pour comprendre un spectre, sans confondre les outils du programme avec les théorèmes nouveaux de Fourier ou de Laplace.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Si deux TP sont associés, le second sert de comparaison ou de travail personnel. Les branches facultatives peuvent occuper plusieurs séances.

Repères mathématiques MPSI et MP. Les circuits sont des applications interdisciplinaires. Le programme MP cite Fourier et Laplace comme exemples d’intégrales à paramètre : les calculs de convergence, de continuité et de dérivation utilisent bien le socle. Leur théorie générale, les séries de Fourier, Fejér, Poisson et Shannon sont des prolongements; les formules nouvelles restent fournies.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : sommes géométriques, dérivation, développements limités, intégration sur un segment et nombres complexes.
- Sup : équations différentielles linéaires d’ordres 1 et 2; gain et phase peuvent être repris depuis le cours de physique.
- Spé : séries numériques, convergence simple, uniforme et normale, séries entières, intégrales impropres et convergence dominée.

## Pour chaque séance

1. Lire le but, les objets et les hypothèses avant de modifier un réglage.
2. Prévoir un résultat sur papier, puis comparer à la figure ou au certificat calculé.
3. Faire varier un seul paramètre et justifier ce qui change.
4. Conclure par une preuve courte : résultat, hypothèses et portée de l’expérience.

## Sup : trois préparations concrètes

Calculer sur des sommes finies et des solutions exactes avant d’utiliser les outils de spé.

### 1. Une somme finie et un reste exact

**Techniques incontournables** · Sup · sommes et dérivation

Contrôler une approximation avec l’identité géométrique finie.

**À faire :** Choisir un intervalle strictement intérieur au domaine de convergence. Calculer la somme finie et son reste, puis comparer à la courbe. Rapprocher le bord et expliquer la dégradation.

**Acquis attendu :** Fournir une majoration explicite du reste sur l’intervalle fixé.

**Limites et compléments :** En sup, dériver les polynômes finis. Le théorème de dérivation d’une série entière est repris en spé.

**TP associés :** Dériver une série sur un compact

### 2. Relier équation différentielle et réponse d’un RC

**Techniques incontournables** · Sup · EDO d’ordre 1, application physique

Déterminer la réponse avec la donnée initiale puis interpréter gain, phase et constante de temps.

**À faire :** Commencer par un échelon, résoudre l’équation sans transformée et vérifier la valeur initiale. Comparer ensuite les trois harmoniques d’entrée et leur atténuation.

**Acquis attendu :** Distinguer régime transitoire et régime établi; reconstruire la réponse sinusoïdale à partir du gain et de la phase.

**Limites et compléments :** La transformée de Laplace est fournie comme autre langage du même calcul, sans être requise à ce stade.

**TP associés :** RC : du calcul de Laplace à la réponse temporelle ; RC : gain, phase et déformation de trois harmoniques

### 3. Trois régimes d’un système du second ordre

**Techniques incontournables** · Sup · EDO d’ordre 2, application physique

Reconnaître les régimes amortis et ajuster les constantes à deux données initiales.

**À faire :** Comparer les régimes oscillant, critique et non oscillant. Relier chaque courbe aux racines de l’équation caractéristique, puis vérifier les valeurs initiales.

**Acquis attendu :** Prévoir le régime avant simulation et écrire une solution adaptée, y compris au cas de racine double.

**Limites et compléments :** L’interprétation des pôles de Laplace est facultative. Elle ne doit pas masquer la résolution de l’équation différentielle.

**TP associés :** RLC : pôles, amortissement et trois régimes

## Spé : cinq séances pour justifier les interversions

À chaque fois : préciser le domaine, le mode de convergence et le théorème réellement applicable.

### 4. Simple, uniforme : chercher le vrai maximum

**Techniques incontournables** · Spé · suites de fonctions

Distinguer convergence en chaque point et contrôle uniforme sur un ensemble.

**À faire :** Localiser le maximum par dérivation avant de regarder le maillage. Comparer l’intervalle entier à un intervalle éloigné du bord.

**Acquis attendu :** Calculer ou majorer la norme uniforme et expliquer pourquoi un maillage fixe peut manquer le pic.

**Limites et compléments :** Les couches limites d’équations différentielles sont un prolongement; le socle porte sur les quantificateurs et la majoration.

**TP associés :** Le pic qui échappe au maillage

### 5. Passer une limite sous l’intégrale

**Techniques incontournables** · Spé · convergence dominée

Trouver un majorant intégrable indépendant du rang et détecter quand il manque.

**À faire :** Comparer l’aire de la suite concentrée à sa limite ponctuelle. Dans l’autre TP, écrire les trois hypothèses de convergence dominée et contrôler le majorant proposé.

**Acquis attendu :** Justifier une interversion valide et expliquer le contre-exemple sans conclure à partir du dessin seul.

**Limites et compléments :** La convergence vers une masse de Dirac est réservée au prolongement sur les mesures et distributions.

**TP associés :** La limite perd une unité d’aire ; Une domination pour des signaux complexes

### 6. Une annulation donne une série convergente

**Techniques incontournables** · Spé · développements limités et convergence normale

Transformer une différence de termes proches en une majoration sommable.

**À faire :** Calculer le premier terme non nul de la différence. Sur un intervalle fixé, construire une borne indépendante du point et comparer les sommes partielles.

**Acquis attendu :** Séparer le développement à rang fixé de la majoration uniforme nécessaire pour sommer.

**Limites et compléments :** Les difficultés d’arrondi sont un complément pratique; elles ne constituent pas une preuve de convergence.

**TP associés :** Deux termes qui s’annulent ; Dériver une série sur un compact

### 7. Construire une série entière par une EDO

**Techniques incontournables** · Spé · coefficients et rayon de convergence

Identifier les coefficients et justifier les opérations à l’intérieur du rayon de convergence.

**À faire :** Écrire la récurrence issue de l’EDO. Calculer les premiers coefficients, prévoir leur signe et contrôler le résidu. Reprendre ensuite le binôme à exposant non entier.

**Acquis attendu :** Donner le rayon ou le domaine de travail et vérifier que la somme satisfait l’équation avec la bonne donnée initiale.

**Limites et compléments :** Les fonctions hypergéométriques et les estimations complexes de Cauchy restent au-delà du programme.

**TP associés :** Une EDO fabrique les coefficients ; Au-delà du binôme polynomial

### 8. Intégrer une série avec un contrôle du reste

**Techniques incontournables** · Spé · série–intégrale et restes

Choisir un théorème d’intégration terme à terme sur un intervalle non borné.

**À faire :** Calculer les intégrales des termes positifs, puis construire un encadrement de la queue. Comparer l’intégrale partielle et la somme des intégrales.

**Acquis attendu :** Vérifier les hypothèses et accompagner l’approximation d’une borne d’erreur.

**Limites et compléments :** Les espaces fonctionnels abstraits et les transformées thermiques ne sont pas nécessaires à cette preuve.

**TP associés :** Additionner des aires positives

## Trois applications guidées à l’analyse du signal

Les identités et définitions nouvelles sont fournies. On exerce des intégrales, des produits scalaires et des calculs trigonométriques.

### A1. Harmoniques et énergie

**Approfondissement CPGE** · Sup / spé · application de l’orthogonalité

Calculer l’énergie d’une somme finie d’harmoniques et observer ce qui se passe près d’un saut.

**À faire :** Vérifier les intégrales d’orthogonalité et l’identité d’énergie d’une somme finie. Comparer ensuite créneau et triangle reconstruits.

**Acquis attendu :** Distinguer une identité finie prouvée d’un résultat sur une série infinie; expliquer le dépassement près de la discontinuité.

**Limites et compléments :** Parseval général, convergence des séries de Fourier et théorème de Fejér sont des prolongements fournis.

**TP associés :** Synthèse de Fourier : Gibbs et moyennes de Fejér ; Parseval : énergie, harmoniques et sommes classiques

### A2. Une acquisition ne révèle pas toutes les fréquences

**Approfondissement CPGE** · Sup / spé · application aux mesures

Distinguer repliement, fuite spectrale, pas d’affichage et résolution.

**À faire :** Trouver deux fréquences donnant les mêmes échantillons. Comparer ensuite une durée plus longue à l’ajout de zéros, puis un filtre avant la mesure.

**Acquis attendu :** Justifier le repliement par une identité trigonométrique; expliquer pourquoi les zéros ajoutés ne créent pas de nouvelles mesures.

**Limites et compléments :** La FFT est un outil fourni. Son algorithme et la théorie générale des fenêtres ne sont pas des exigences de mathématiques MP.

**TP associés :** Repliement : deux fréquences, les mêmes mesures ; Avant la mesure : le filtre antirepliement ; FFT : fuite spectrale et fenêtrage ; Résolution : voir deux fréquences proches

### A3. Une série pour corriger un modèle physique

**Approfondissement CPGE** · Spé · séries, équivalents et intégration

Relier une correction mathématique à son domaine d’approximation.

**À faire :** Comparer la période du pendule à son approximation harmonique puis à sa première correction. Dans l’autre TP, étudier le rayon et la croissance de la série à partir de ses coefficients.

**Acquis attendu :** Indiquer le petit paramètre et le domaine où la correction améliore réellement la prévision.

**Limites et compléments :** La théorie des fonctions elliptiques et la preuve par concentration de Poisson sont des prolongements; les formules utiles sont fournies.

**TP associés :** La période du pendule devient elliptique ; Une série entière à l’échelle e²x

## Trois branches au-delà du programme

Choisir une application après les huit séances. Ces méthodes enrichissent les TIPE et ne remplacent pas le socle d’analyse.

### P1. Transformées, convolution et régularisation

**Au-delà du programme** · Au-delà · Fourier et Laplace intégrales

Relier largeur temporelle, spectre et composition des réponses d’un système.

**À faire :** Calculer la transformée de la porte avec la convention du TP. Vérifier la phase d’une translation puis la convolution par recouvrement. Comparer à la gaussienne et à une régularisation exponentielle.

**Acquis attendu :** Conserver les facteurs de normalisation et séparer convergence impropre, absolue et limite régularisée.

**Limites et compléments :** Les calculs directs de transformées sont des exemples possibles d’intégrales à paramètre en MP. La théorie générale, le théorème de convolution et les distributions causales sont des prolongements accompagnés.

**TP associés :** Porte, sinus cardinal et phase d’une translation ; Gaussienne : Fourier et incertitude temps–fréquence ; Convoluer : l’aire d’un recouvrement mobile ; L’intégrale de Dirichlet par régularisation d’Abel ; RC : du calcul de Laplace à la réponse temporelle

### P2. Lisser, périodiser, reconstruire

**Au-delà du programme** · Au-delà · Poisson, Fejér et Shannon

Comprendre trois opérations sur un signal et leurs hypothèses propres.

**À faire :** Comparer lissage par Poisson et moyenne de Fejér. Pour Shannon, faire varier la cadence puis le nombre d’échantillons; distinguer condition de bande et troncature.

**Acquis attendu :** Séparer l’erreur de troncature d’un défaut d’hypothèse et vérifier les normalisations entre temps et fréquence.

**Limites et compléments :** Les théorèmes de Poisson, Fejér et Shannon ne sont pas exigibles en mathématiques MP.

**TP associés :** Noyau de Poisson : convergence normale et lissage ; Poisson : une gaussienne, deux descriptions ; Synthèse de Fourier : Gibbs et moyennes de Fejér ; Shannon : reconstruire un paquet à bande limitée

### P3. Suivre, transmettre et retrouver un signal

**Au-delà du programme** · Au-delà · méthodes techniques guidées

Choisir un outil en fonction de la question de mesure.

**À faire :** Suivre le chirp avec deux tailles de fenêtre. Retrouver ensuite un message modulé, un retard par corrélation et comparer deux débruitages.

**Acquis attendu :** Expliquer le compromis temps–fréquence et distinguer réduction du bruit, retard et déformation du signal utile.

**Limites et compléments :** Ces traitements sont des applications techniques supplémentaires; aucun algorithme général nouveau n’est présenté comme exigible en CPGE.

**TP associés :** Spectrogramme : suivre un chirp ; Modulation : traduire le spectre d’un message ; Corrélation : mesurer un temps de vol ; Débruiter : réduction du bruit et déformation

## Repères de programme

- [Programme de mathématiques MPSI / MP2I](https://prepas.org/ups.php?document=69)
- [Programme de mathématiques MP](https://prepas.org/ups.php?document=85)
