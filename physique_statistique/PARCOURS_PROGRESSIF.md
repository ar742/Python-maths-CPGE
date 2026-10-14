# Physique statistique & Équilibres : un parcours sup / spé

Partir du gaz parfait et de l’énergie thermique, puis utiliser Boltzmann pour des niveaux discrets. Réserver les statistiques quantiques et les spins en interaction aux branches avancées.

Prévoir 60 à 90 minutes par séance prioritaire. Les simulations avancées demandent surtout de vérifier préparation, taille et précision, pas de multiplier les réglages.

La sup prépare les liens entre pression, température et énergie. Le socle statistique de spé présenté ici est celui de MP : Boltzmann, deux niveaux, fluctuations et équipartition. Il ne constitue pas un chapitre obligatoire identique dans toutes les filières. Planck, Bose/Fermi et Ising/Onsager sont des prolongements ; une simulation n’est pas une preuve de limite thermodynamique.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Notations communes : kB est la constante de Boltzmann, h celle de Planck ; T est une température absolue en K. kBT est une énergie.
- Sup : gaz parfait, température absolue, énergie, probabilités et bilans de particules.
- Sup : exponentielles, logarithmes, sommes et oscillateur harmonique classique.
- Spé : facteur de Boltzmann, moyenne et variance ; intégrales et séries pour les branches quantiques.

## Pour chaque séance

1. Comparer l’énergie caractéristique à kBT avant de lire la figure.
2. Distinguer probabilité d’un microétat et population d’un niveau.
3. Contrôler une somme de probabilités, une énergie ou un bilan de particules.
4. Pour un calcul tronqué ou simulé, vérifier la précision avant de commenter une limite.

## Sup : deux séances pour relier agitation et énergie

Les distributions nouvelles sont fournies ; les premières justifications portent sur les bilans classiques.

### 1. Du mouvement microscopique à la pression

**Techniques incontournables** · Sup · gaz parfait et énergie cinétique

Relier la pression au mouvement des molécules et contrôler les unités.

**À faire :** Noter T la température, M la masse molaire et n la densité de particules. Choisir le mode pression ; doubler T à n fixé puis changer M. Comparer vitesse quadratique moyenne et pression.

**Acquis attendu :** Retrouver p=nkBT et expliquer pourquoi la masse modifie les vitesses mais pas p à T,n fixés.

**Limites et compléments :** La distribution complète de Maxwell est fournie. Moyenne des vitesses et vitesse quadratique moyenne sont deux grandeurs distinctes.

**TP associés :** Des vitesses microscopiques à la pression

### 2. Compter les termes d’énergie

**Techniques incontournables** · Sup → Spé · modèle classique et capacité

Préparer l’équipartition en distinguant énergie et capacité thermique.

**À faire :** Dans le modèle classique séparé, noter r le nombre de termes quadratiques ajoutés aux trois termes cinétiques. Comparer r=0 et r=2 ; dériver l’énergie fournie par rapport à T avant de lire la capacité.

**Acquis attendu :** Associer une capacité à une variation d’énergie et conserver le nombre de degrés de liberté annoncé.

**Limites et compléments :** L’équipartition devient un résultat du programme MP. Le compteur r ne désigne pas les niveaux de l’oscillateur quantique à une dimension.

**TP associés :** Quantification et équipartition

## Spé : trois séances du socle statistique MP

Normaliser, calculer une moyenne, puis examiner les fluctuations et les limites.

### 3. Deux niveaux et une température

**Techniques incontournables** · Spé · poids de Boltzmann

Passer d’un rapport de poids à deux probabilités normalisées.

**À faire :** Noter ε l’écart entre les niveaux 0 et ε, T la température et N le nombre de sites indépendants. Choisir deux niveaux non dégénérés ; comparer ε à kBT puis calculer populations, énergie moyenne et capacité.

**Acquis attendu :** Justifier les limites froide et chaude ; expliquer pourquoi la capacité présente un maximum intermédiaire.

**Limites et compléments :** Le décalage commun des énergies ne change pas les populations. Dégénérescence et comparaison microcanonique/canonique sont repris en complément.

**TP associés :** Deux niveaux : populations et fluctuations

### 4. Des fluctuations et un moment magnétique

**Techniques incontournables** · Spé · variance et système à deux niveaux

Relier fluctuations, taille du système et réponse à un champ.

**À faire :** Noter U l’énergie totale et N le nombre de sites ; comparer son écart type relatif pour plusieurs N. Pour les spins indépendants, noter μ le moment et B le champ ; utiliser les niveaux ±μB et comparer |μB| à kBT.

**Acquis attendu :** Retrouver une décroissance relative en 1/√N ; distinguer réponse presque linéaire et saturation du moment moyen.

**Limites et compléments :** Le calcul à deux niveaux est le socle MP. La loi de Curie est une application guidée ; interactions et ferromagnétisme réclament un autre modèle.

**TP associés :** Deux niveaux : populations et fluctuations ; Spins, saturation et loi de Curie

### 5. Une boîte retrouve le gaz classique

**Techniques incontournables** · Spé · niveaux discrets et équipartition

Expliquer comment une somme de niveaux donne une énergie thermique classique.

**À faire :** Noter L le côté du cube, m la masse et Nmax le nombre de modes conservés. Augmenter T jusqu’à dépasser l’énergie de confinement ; contrôler la troncature avant de comparer l’énergie par particule à 3kBT/2.

**Acquis attendu :** Retrouver le rôle de la dimension et distinguer limite classique et approximation numérique mal tronquée.

**Limites et compléments :** MP étudie d’abord la boîte à une dimension. Le cube accompagne le comptage ; les particules identiques et la dégénérescence quantique ne sont pas supposées ici.

**TP associés :** Les niveaux d’un cube deviennent un gaz ; Quantification et équipartition

## Approfondissements : transport et gel des excitations

Les équations et distributions nécessaires sont apportées par les TP.

### 6. Une fuite sélectionne des molécules

**Approfondissement CPGE** · Sup / Spé · bilan et équation différentielle

Distinguer population dans le gaz et flux à travers un petit trou.

**À faire :** Choisir effusion ; noter S l’aire du trou, V le volume et τ le temps caractéristique. Doubler S puis V. Passer aux deux compartiments de températures T₁,T₂ différentes et chercher la condition de flux stationnaire.

**Acquis attendu :** Justifier l’effet de S/V sur τ et expliquer pourquoi l’égalité des flux ne donne pas forcément l’égalité des pressions.

**Limites et compléments :** Effusion et transpiration thermique sont des applications guidées. Le modèle suppose gaz dilué, trou adapté et températures imposées.

**TP associés :** Des vitesses microscopiques à la pression

### 7. Des niveaux qui cessent d’être équipartis

**Approfondissement CPGE** · Spé · spectre fourni et sommes

Comparer énergie de point zéro, excitation thermique et capacité.

**À faire :** Noter ν la fréquence et hν le quantum d’énergie. Dans l’oscillateur, comparer kBT≪hν puis kBT≫hν. Dans le modèle à trois niveaux, noter g la dégénérescence du niveau intermédiaire et modifier g.

**Acquis attendu :** Distinguer une énergie non nulle à basse T d’une capacité qui tend vers zéro ; additionner les probabilités des microétats d’un niveau.

**Limites et compléments :** Le spectre quantique et la dégénérescence sont fournis. Le modèle d’Einstein quantique complet dépasse le socle classique MP.

**TP associés :** Quantification et équipartition ; Deux niveaux : populations et fluctuations ; Les niveaux d’un cube deviennent un gaz

## Au-delà : trois branches de physique moderne

Ces modèles introduisent des concepts supplémentaires explicités avant utilisation.

### A. Le spectre d’un corps noir

**Au-delà du programme** · Au-delà · Planck et rayonnement thermique

Relier position du maximum et puissance totale en conservant la variable spectrale.

**À faire :** Noter T la température, λ la longueur d’onde et Bλ la luminance par unité de longueur d’onde. Comparer 300 K et 5800 K, puis 3000 K et 6000 K ; prévoir maximum et flux. Comparer Planck à Rayleigh–Jeans.

**Acquis attendu :** Retrouver λmax proportionnelle à 1/T et le flux proportionnel à T⁴ ; distinguer fraction visible et rendement électrique.

**Limites et compléments :** La loi complète et le comptage photonique sont des prolongements. Changer de fréquence à longueur d’onde nécessite de transformer aussi la densité spectrale.

**TP associés :** Le rayonnement échappe à la catastrophe

### B. Particules identiques : Bose et Fermi

**Au-delà du programme** · Au-delà · occupations et potentiel chimique

Comprendre pourquoi une occupation moyenne n’est pas une probabilité de présence limitée à 1 pour tous les gaz.

**À faire :** Noter ε l’énergie d’un état et μ le potentiel chimique. En comparaison, prendre μ/(kBT)=−6 ; examiner la limite diluée. Passer aux gaz Fermi puis Bose à nombre imposé et comparer T aux températures caractéristiques.

**Acquis attendu :** Distinguer contrainte de nombre, occupation d’un état, énergie de Fermi et population du condensat.

**Limites et compléments :** Bose/Fermi, grand canonique et condensation sont hors du socle statistique MP. La masse et la densité des modes Fermi/Bose ne désignent pas le même gaz.

**TP associés :** Bosons, fermions et limite diluée ; Les niveaux d’un cube deviennent un gaz

### C. Des spins indépendants aux spins couplés

**Au-delà du programme** · Au-delà · Ising et Onsager

Séparer calcul fini, simulation et transition dans une limite théorique.

**À faire :** Noter sᵢ=±1 les spins, J leur couplage et θ=kBT/J la température réduite. Commencer par la chaîne exacte ; passer au carré avec deux préparations et augmenter la durée puis la taille.

**Acquis attendu :** Contrôler l’effet de préparation et l’autocorrélation ; distinguer aimantation moyenne signée, valeur absolue et résultat thermodynamique.

**Limites et compléments :** Ising/Onsager et la méthode de Monte-Carlo sont des prolongements. Une figure sur un réseau fini ne prouve ni une température critique exacte ni un exposant.

**TP associés :** De la chaîne d’Ising au réseau d’Onsager ; Spins, saturation et loi de Curie

## Repères de programme

- [PCSI 2021 · thermodynamique et gaz parfait (annexe 2)](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/65/0/spe780_annexe_1373650.pdf#page=58)
- [MP 2021 · thermodynamique statistique, §7 (BO complet)](https://www.enseignementsup-recherche.gouv.fr/sites/default/files/imported_files/documents/BO_31_MESRI_1417448.pdf#page=64)
