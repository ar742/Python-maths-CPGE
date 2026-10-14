# Énergie & Transferts : un parcours progressif sup / spé

Commencer par les systèmes, les signes et les machines. Donner ensuite la priorité aux transferts et à la diffusion : bilans locaux, conditions aux limites et échelles de temps. Les potentiels et effets couplés offrent des applications; la thermodynamique hors équilibre reste une branche accompagnée.

Prévoir 60 à 90 minutes par séance prioritaire, avec un exercice corrigé. Quand plusieurs TP sont associés, commencer par le premier et utiliser les autres comme comparaisons ou travail personnel. Les approfondissements et branches peuvent être répartis sur plusieurs séances.

Repères PCSI et PC, complétés par MP pour les systèmes ouverts et la diffusion numérique. « Incontournable » désigne les techniques de bilan, de résolution et de contrôle, pas toutes les formules du TP. Helmholtz, exergie, modèles thermoélectriques, Langevin et transport électrolytique sont définis sur place. Le potentiel de Gibbs se relie aussi à la chimie de spé; il n’est pas annoncé comme un acquis identique de toutes les filières.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Sup : système fermé, gaz parfait, premier et deuxième principes, chaleur latente et machines dithermes.
- Sup : travail, énergie, puissance, équations différentielles du premier ordre et température absolue.
- Spé : flux orientés, bilans locaux, lois de Fourier et de Fick, équation de diffusion et conditions aux limites.

## Pour chaque séance

1. Définir le système, le domaine et les variables avec leurs unités avant tout réglage.
2. Prévoir un signe, une échelle ou un bilan sur papier puis comparer à l’expérience.
3. Modifier un paramètre à la fois et contrôler un cas limite ou une conservation.
4. Conclure : ce que le modèle explique, les hypothèses vérifiées et la précision utile.

## Sup : quatre séances pour tenir un bilan

Choisir le système, les échanges et la convention de signe avant de calculer.

### 1. Même état final, échanges différents

**Techniques incontournables** · Sup · premier principe et travail

Distinguer variation d’une fonction d’état et travail échangé.

**À faire :** Comparer les trois chemins du gaz parfait. Calculer le travail par l’aire orientée puis le bilan énergétique. Choisir ensuite un ressort ou un condensateur parmi les travaux généralisés.

**Acquis attendu :** Conserver les signes choisis et expliquer pourquoi les échanges dépendent du chemin.

**Limites et compléments :** Travaux de surface et conventions magnétiques sont des compléments fournis; commencer par pression, ressort et condensateur.

**TP associés :** Même état final, travaux différents : suivre trois chemins ; Surface, fil, condensateur, bobine : une force conjuguée

### 2. Trouver l’état final avec le bon système

**Techniques incontournables** · Sup · calorimétrie et entropie

Identifier la grandeur conservée et décider s’il subsiste plusieurs phases.

**À faire :** Dans le calorimètre isolé, comparer les bilans avant et après changement d’état. Pour les détentes, distinguer le système fermé de Joule et le bilan enthalpique fourni pour l’étranglement.

**Acquis attendu :** Calculer la température finale et distinguer chaleur échangée et entropie créée.

**Limites et compléments :** Le bilan détaillé d’un système ouvert est repris en spé. Van der Waals et l’inversion de Joule–Thomson sont des prolongements.

**TP associés :** Calorimètre : température finale, chaleur latente et entropie ; Joule : U constante ou H constante, deux détentes différentes

### 3. Une machine ne transforme pas toute la chaleur en travail

**Techniques incontournables** · Sup · machines dithermes et cycles

Relier fonctionnement, rendement ou coefficient de performance aux deux principes.

**À faire :** Comparer moteur, réfrigérateur et pompe à chaleur. Vérifier le bilan d’un cycle idéal choisi puis comparer sa performance à la borne de Carnot.

**Acquis attendu :** Employer les températures en kelvins et distinguer un rendement d’un coefficient de performance.

**Limites et compléments :** Les cycles techniques sont des applications idéales; régénération réelle et sources variables demandent un modèle supplémentaire.

**TP associés :** Carnot : moteur, réfrigérateur et pompe à chaleur ; Otto, Diesel, Brayton, Stirling : comparer des cycles calculés

### 4. Des watts traversent une paroi

**Techniques incontournables** · Sup → spé · préparation aux transferts

Distinguer densité de flux, puissance et énergie transférée.

**À faire :** Utiliser la loi de Fourier fournie pour une barre stationnaire. Comparer ensuite les résistances du mur et repérer la plus grande chute de température.

**Acquis attendu :** Vérifier les unités et l’égalité des puissances dans les éléments en série.

**Limites et compléments :** En sup, priorité aux bilans et aux résistances fournies. L’établissement local de Fourier et de l’équation de chaleur est l’objectif de spé.

**TP associés :** Fourier : une barre relie deux thermostats ; Un mur : conduction et convection en série

## Spé : quatre séances prioritaires sur la diffusion

Un profil calculé doit satisfaire le bilan local, l’état initial et les conditions aux limites.

### 5. Construire et résoudre la diffusion à une dimension

**Techniques incontournables** · Spé · bilan local et conditions aux limites

Relier les dérivées spatiales à la variation temporelle et contrôler un calcul numérique.

**À faire :** Établir l’équation de chaleur par bilan d’une tranche. Comparer deux pas de calcul dans Diffusion 1D. Dans le demi-espace, prévoir la profondeur affectée puis vérifier son évolution en racine du temps.

**Acquis attendu :** Préciser température initiale et conditions de bord; distinguer un phénomène physique d’une instabilité du schéma.

**Limites et compléments :** La fonction spéciale de la solution de choc thermique est fournie. Schémas implicites et théorie d’erreur générale sont des prolongements.

**TP associés :** Diffusion 1D : calcul stable et modes de Fourier ; Choc thermique : une profondeur en √(χt)

### 6. Le thermique filtre les variations rapides

**Techniques incontournables** · Spé · temps de diffusion et réponse harmonique

Comparer atténuation, retard de phase et validité d’une température uniforme.

**À faire :** Comparer une excitation journalière à une excitation annuelle. Dans le refroidissement, modifier le nombre de Biot et confronter centre, surface et moyenne.

**Acquis attendu :** Relier la longueur de pénétration à la diffusivité et à la période; expliciter l’hypothèse du modèle uniforme.

**Limites et compléments :** Les modes convectifs sont fournis. Leur résolution générale et l’identification inverse de diffusivité sont des compléments.

**TP associés :** Onde thermique : filtrer le jour et les saisons ; Biot : quand peut-on supposer une température uniforme ?

### 7. Le pic diminue, l’énergie reste, l’entropie augmente

**Techniques incontournables** · Spé · conservation et second principe

Distinguer valeur maximale, intégrale d’énergie et création d’entropie.

**À faire :** Suivre l’étalement de la tache et vérifier sa normalisation. Dans le système isolé, calculer la température d’équilibre et le signe de la création d’entropie.

**Acquis attendu :** Identifier ce que conserve le modèle et ce qui évolue irréversiblement.

**Limites et compléments :** Le noyau de chaleur général, convolution et principes variationnels hors équilibre sont des prolongements.

**TP associés :** Une tache de chaleur : énergie conservée, pic qui s’étale ; Diffuser sans perdre d’énergie : l’entropie augmente

### 8. Diffuser de la matière avec ou sans absorption

**Techniques incontournables** · Spé PC · Fick, source et bilan

Relier une variance, un flux et une équation de diffusion.

**À faire :** Calculer moyenne et variance de la marche symétrique avec les données du TP. Dans le modèle de neutrons, écrire séparément diffusion, source et absorption.

**Acquis attendu :** Retrouver l’échelle de diffusion et vérifier le bilan intégral de l’absorption.

**Limites et compléments :** Le modèle neutronique est une application fournie, pas un cours de réacteur. La théorie probabiliste continue vient en prolongement.

**TP associés :** Marche aléatoire : de la loi binomiale à Fick ; Neutrons : diffusion, absorption et bilan de source

## Quatre approfondissements appliqués

Choisir une question et utiliser les bilans déjà acquis. Les nouveaux coefficients et potentiels sont définis dans le TP.

### A1. L’équilibre comme minimum d’un potentiel adapté

**Approfondissement CPGE** · Spé · contraintes et équilibre

Choisir une fonction à minimiser en précisant ce qui reste imposé.

**À faire :** Dans la cloison élastique, calculer la force et vérifier le minimum de Helmholtz à température et volume total fixés. Dans la réaction idéale, comparer pente de Gibbs et déplacement vers l’équilibre.

**Acquis attendu :** Relier signe d’une dérivée et sens d’évolution, puis séparer condition stationnaire et stabilité.

**Limites et compléments :** Les potentiels sont fournis. Gibbs se relie à la chimie de spé; Helmholtz et la minimisation générale ne sont pas un acquis commun de physique de toutes les voies.

**TP associés :** Helmholtz : une cloison interne cherche le minimum de F ; Gibbs : l’équilibre d’une réaction A ⇌ B minimise G

### A2. Plus d’isolant signifie-t-il moins de pertes ?

**Approfondissement CPGE** · Sup / spé · géométrie et résistances

Tenir compte de la variation de surface dans un bilan thermique.

**À faire :** Comparer une paroi plane à la géométrie radiale. Chercher le rayon critique, puis vérifier le bilan de l’igloo et l’existence d’une épaisseur admissible.

**Acquis attendu :** Expliquer le compromis entre résistance conductrice et surface d’échange.

**Limites et compléments :** Ponts thermiques, ventilation, fusion et rayonnement net ne sont pas inclus dans ces deux modèles.

**TP associés :** Rayon critique : ajouter un isolant peut accroître la perte ; Igloo : bilan d’une personne et géométrie hémisphérique

### A3. Un système ouvert ou une vapeur change les contraintes

**Approfondissement CPGE** · Spé · enthalpie, compression et changements d’état

Choisir un bilan adapté à la matière traversante et aux limites de phase.

**À faire :** Comparer compression en un et plusieurs étages avec refroidissement intermédiaire. Pour la vapeur, comparer les évolutions de pression et de saturation au début de la détente.

**Acquis attendu :** Justifier la répartition des rapports de pression et repérer le seuil où le modèle monophasé cesse de suffire.

**Limites et compléments :** L’optimisation générale des étages et la nucléation des gouttes sont des compléments; le TP brouillard s’arrête au début de condensation.

**TP associés :** Compresseur : répartir les rapports de pression pour minimiser le travail ; Détente d’une vapeur saturante : décider du début de condensation

### A4. Mesurer et refroidir avec des effets couplés

**Approfondissement CPGE** · Sup / spé · bilans et calibration

Comparer mesure de température, émission et puissance de refroidissement.

**À faire :** Choisir un TP principal : comparer les surfaces de Leslie, calibrer le thermocouple avec sa jonction froide, ou écrire le bilan complet du module Peltier. Utiliser les autres comme comparaisons.

**Acquis attendu :** Conserver les unités et les signes; distinguer signal de mesure, chaleur transférée et consommation électrique.

**Limites et compléments :** Les lois radiatives et coefficients thermoélectriques utiles sont fournis. Aucun modèle microscopique de transport n’est requis.

**TP associés :** Cube de Leslie : comparer des surfaces à même température ; Thermocouple : calibrer et compenser la jonction froide ; Module Peltier : refroidir demande un bilan complet

## Trois branches au-delà du programme

Approfondir les modèles couplés après avoir maîtrisé les bilans et les échelles de diffusion.

### P1. Du mouvement inertiel à la diffusion brownienne

**Au-delà du programme** · Au-delà · Langevin et fluctuations

Distinguer régimes balistique et diffusif.

**À faire :** Comparer les durées devant le temps de relaxation du TP. Faire varier rayon, viscosité et température, puis confronter la diffusion à la marche symétrique.

**Acquis attendu :** Relier les échelles aux paramètres et distinguer trajectoire aléatoire et moyenne statistique.

**Limites et compléments :** Langevin, Ornstein–Uhlenbeck et limite brownienne sont des théories supplémentaires accompagnées.

**TP associés :** Langevin : du mouvement inertiel à Stokes–Einstein ; Marche aléatoire : de la loi binomiale à Fick

### P2. Énergie disponible et transports hors équilibre

**Au-delà du programme** · Au-delà · exergie et transport électrolytique

Comprendre comment un gradient permet un travail ou produit un courant et une dissipation.

**À faire :** Comparer travail maximal réversible et simple mise en contact du corps chaud. Dans l’électrolyte, distinguer flux des deux espèces et courant électrique.

**Acquis attendu :** Expliquer pourquoi conserver l’énergie ne signifie pas conserver sa capacité à fournir un travail.

**Limites et compléments :** Exergie, Nernst–Planck, couches de Debye et thermodynamique irréversible dépassent le socle; leurs hypothèses sont précisées.

**TP associés :** Corps fini : une différence de température vaut-elle du travail ? ; Électrolyte : diffusion commune et potentiel de jonction ; Diffuser sans perdre d’énergie : l’entropie augmente

### P3. Quand chaleur, son et électricité se répondent

**Au-delà du programme** · Au-delà · thermoacoustique et piézoélectricité

Relier une réponse mécanique à un transfert thermique ou électrique.

**À faire :** Dans l’onde couplée, faire varier le temps de diffusion thermique. Dans le quartz, comparer résonance et antirésonance et vérifier la réciprocité du couplage.

**Acquis attendu :** Identifier les variables conjuguées et distinguer réponse oscillante et branche diffusive.

**Limites et compléments :** Les modèles de machines thermoacoustiques et de résonateurs piézoélectriques sont des prolongements fournis, pas des résultats à mémoriser.

**TP associés :** Onde sonore : coupler compression et diffusion thermique ; Quartz : réciprocité, résonance et antirésonance

## Repères de programme

- [Physique PCSI, BO 2021, annexe 2](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm)
- [Programme de physique PC, 2021](https://prepas.org/ups.php?document=92)
- [Programme de physique-chimie MP, 2021](https://prepas.org/ups.php?document=87)
