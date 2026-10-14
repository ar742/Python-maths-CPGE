# Physique quantique & Qubits : un parcours sup / spé

Commencer par les échelles de confinement, puis relier fonction d’onde, énergie et courant de probabilité. Choisir ensuite les modèles à deux niveaux et les applications avancées.

Prévoir 60 à 90 minutes par séance prioritaire. Les approfondissements et les trois branches au-delà se choisissent ensuite ; aucun solveur ou calcul quantique préalable n’est requis.

Repères PCSI, MP et PC : interprétation probabiliste, confinement, potentiels par morceaux et superposition. Le cube est une extension de la boîte à une dimension. Oscillateur quantique et transitions de Rabi sont guidés ; qubits, Bell, Grover et Josephson ne deviennent pas des obligations du programme. « Incontournable » désigne la technique de la séance, pas tout le TP.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Notations communes : h est la constante de Planck, ℏ=h/(2π), m une masse et E une énergie. Les unités physiques ou réduites sont précisées dans le TP.
- Sup : ondes, diffraction, modes propres, probabilités et énergie cinétique.
- Sup : sinusoïdes, nombres complexes, dérivation et équations différentielles linéaires.
- Spé : densité de probabilité, normalisation, états stationnaires et raccordements ; matrices pour les branches avancées.

## Pour chaque séance

1. Lire les objets et les unités ; distinguer unités physiques et unités réduites.
2. Prévoir un facteur d’échelle ou un régime avant de calculer.
3. Changer un seul paramètre et vérifier une normalisation, un flux ou une limite.
4. Rédiger la justification et annoncer les propriétés supplémentaires admises.

## Sup : deux séances de confinement et d’échelles

L’analogie avec les ondes prépare le formalisme ; commencer par les observations et les ordres de grandeur.

### 1. Une fente, une impulsion et une incertitude

**Techniques incontournables** · Sup · diffraction et Heisenberg

Comprendre pourquoi une localisation plus étroite impose un étalement spectral plus large.

**À faire :** Choisir le mode fente. Noter a sa largeur et λ la longueur d’onde ; partir de a=4 µm et λ=380 nm, puis prendre a=2 µm à λ fixée. Comparer les premiers zéros de diffraction et relier impulsion et longueur d’onde.

**Acquis attendu :** Prévoir le doublement de la largeur angulaire dans le régime des petits angles ; distinguer largeur de fente et écart type.

**Limites et compléments :** En sup, travailler l’ordre de grandeur. Le produit exact des écarts types, la phase quadratique et la covariance sont réservés à un second passage.

**TP associés :** L’incertitude révèle les échelles classiques

### 2. Des parois imposent des modes

**Techniques incontournables** · Sup · modes propres et confinement

Retrouver la quantification à partir de conditions aux parois.

**À faire :** Choisir les parois et le fondamental. Noter L le côté de la boîte, m la masse et nₓ,nᵧ,n_z les indices positifs. Doubler L à masse fixée ; commencer par la variation sinusoïdale suivant un seul axe.

**Acquis attendu :** Justifier une énergie proportionnelle à 1/L² et l’absence de mode d’indice nul avec ces parois.

**Limites et compléments :** Le problème à une dimension est prioritaire. Comptage des triplets, dégénérescence du cube et conditions périodiques sont des compléments.

**TP associés :** Une particule dans un volume cubique

## Spé : trois séances pour calculer une probabilité et un flux

Les raccordements et les superpositions se vérifient par des équations, pas uniquement par un dessin.

### 3. Superposer des niveaux d’énergie

**Techniques incontournables** · Spé · états stationnaires et évolution

Distinguer densité stationnaire et évolution d’une superposition.

**À faire :** Noter ψ la fonction d’onde, E₁,E₂ les énergies de deux modes et w le poids du second. Comparer w=0 et w=1/2 en faisant varier le temps réduit ; développer |ψ|² et isoler le terme d’interférence.

**Acquis attendu :** Relier la pulsation d’oscillation à (E₂−E₁)/ℏ ; vérifier la normalisation et distinguer densité locale et énergie moyenne.

**Limites et compléments :** Le calcul à deux états dans un puits infini relève de MP/PC. La géométrie cubique fournit ici un exemple accompagné.

**TP associés :** Une particule dans un volume cubique

### 4. Raccorder et conserver le courant

**Techniques incontournables** · Spé · potentiel constant par morceaux

Obtenir réflexion et transmission à partir de la fonction d’onde et de sa dérivée.

**À faire :** Choisir la marche. Noter E l’énergie incidente, V₀ sa hauteur, R et T les rapports de courants. Comparer E<V₀ puis E>V₀ ; écrire les raccordements de ψ et ψ′ au même point.

**Acquis attendu :** Vérifier R+T=1 et expliquer pourquoi un rapport d’amplitudes au carré seul ne donne pas toujours T.

**Limites et compléments :** Utiliser la formule du courant fournie. Un état évanescent dans la marche ne représente pas une transmission à travers une barrière finie.

**TP associés :** Réflexion, pénétration et effet tunnel

### 5. Une barrière finie transmet

**Techniques incontournables** · Spé · effet tunnel

Relier confinement, onde évanescente et dépendance de la transmission.

**À faire :** Choisir la barrière et E<V₀ ; noter a sa largeur. Augmenter a en gardant E,V₀ fixes, puis examiner E>V₀ et une résonance de transmission. Contrôler les flux à chaque essai.

**Acquis attendu :** Expliquer la forte décroissance avec la largeur et distinguer réflexion quantique, tunnel et transmission résonante.

**Limites et compléments :** Selon la filière, l’expression de T est admise ou obtenue par raccordement. Temps de traversée, paquets incidents et barrières multiples restent hors du calcul demandé.

**TP associés :** Réflexion, pénétration et effet tunnel ; L’incertitude révèle les échelles classiques

## Approfondissements : deux modèles accompagnés

Ces modèles utilisent les outils de CPGE ; leur spectre et leurs lois nouvelles sont fournis.

### 6. Relier le spectre à l’oscillateur classique

**Approfondissement CPGE** · Sup / Spé · EDO et énergie

Comparer énergie minimale, nœuds et mouvement moyen.

**À faire :** Noter ω la pulsation, n le nombre d’excitations et ℓ=√(ℏ/(mω)) la longueur caractéristique. Comparer n=0,1,3, puis choisir un état cohérent et suivre la position moyenne pendant un cycle.

**Acquis attendu :** Retrouver les espacements ℏω du spectre fourni ; distinguer mouvement moyen et densité de probabilité.

**Limites et compléments :** La résolution de l’oscillateur quantique et les états cohérents sont des compléments. Les opérateurs de création ne sont pas une connaissance préalable.

**TP associés :** Du spectre quantique à l’oscillation classique ; L’incertitude révèle les échelles classiques

### 7. Une résonance transfère une population

**Approfondissement CPGE** · Spé · résonance et modèle à deux niveaux

Exploiter une loi de transition fournie pour choisir durée et désaccord.

**À faire :** Noter Ω le couplage, Δ le désaccord et t le temps réduit. Comparer les impulsions π et π/2 à Δ=0, puis augmenter |Δ| ; lire séparément les repères physiques B₀,B₁ de RMN.

**Acquis attendu :** Justifier l’inversion à résonance et la diminution de l’amplitude maximale Ω²/(Ω²+Δ²).

**Limites et compléments :** Rabi, spin et repère tournant quantique sont des applications fournies, hors du socle quantique MP/PC cité. Les réglages réduits ne sont pas les champs physiques de RMN.

**TP associés :** Piloter une transition par résonance

## Au-delà : trois branches au choix

Les définitions et les conventions de base sont apportées par l’atelier.

### A. Du qubit aux circuits

**Au-delà du programme** · Au-delà · Bloch, portes et Grover

Associer amplitudes, géométrie et probabilités de mesure.

**À faire :** Noter θ,φ les angles du vecteur de Bloch et r sa longueur. Comparer |0⟩ et |+⟩, puis r=0. Dans le circuit à deux qubits, préparer Bell ; pour Grover, comparer zéro, une et deux itérations.

**Acquis attendu :** Vérifier la somme des probabilités et expliquer pourquoi ajouter une itération peut réduire la probabilité de succès.

**Limites et compléments :** Matrices densité, produits tensoriels et algorithmes quantiques sont des prolongements. Le dessin d’une sphère ne représente pas une trajectoire spatiale de particule.

**TP associés :** Un qubit sur la sphère de Bloch ; Construire Bell, puis chercher avec Grover

### B. Corrélation, intrication et test de Bell

**Au-delà du programme** · Au-delà · probabilités conjointes

Distinguer une corrélation classique d’une violation du modèle local testé.

**À faire :** Noter a,a′ et b,b′ les angles des deux analyseurs, v le poids de Bell et S la combinaison CHSH. Comparer Bell, mélange classique et bruit aux mêmes angles ; contrôler les probabilités marginales.

**Acquis attendu :** Distinguer seuil d’intrication et seuil de violation CHSH ; expliquer pourquoi les corrélations ne permettent pas de signaler à distance.

**Limites et compléments :** CHSH et séparabilité sont hors du programme. La borne classique requiert les hypothèses annoncées ; une corrélation seule ne suffit pas.

**TP associés :** Deux photons, une corrélation quantique ; Construire Bell, puis chercher avec Grover

### C. Une phase devient un courant mesurable

**Au-delà du programme** · Au-delà · Josephson et SQUID

Relier phase, tension et flux dans un modèle supraconducteur.

**À faire :** Noter V la tension, I₁,I₂ les courants critiques et Φ₀=h/(2e) le quantum de flux. Comparer une jonction à V=0 puis V=1 µV ; dans le SQUID, comparer Φ/Φ₀=0 et 1/2 avec jonctions égales puis différentes.

**Acquis attendu :** Retrouver fréquence proportionnelle à V et modulation périodique du courant critique ; justifier le minimum résiduel si I₁≠I₂.

**Limites et compléments :** Josephson et la supraconductivité sont des prolongements. Dissipation, inductance de boucle et électronique de lecture d’un SQUID réel ne sont pas calculées.

**TP associés :** La phase commande le courant

## Repères de programme

- [PCSI 2021 · physique, introduction quantique (annexe 2)](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/65/0/spe780_annexe_1373650.pdf#page=65)
- [MP 2021 · physique quantique, §6 (BO complet)](https://www.enseignementsup-recherche.gouv.fr/sites/default/files/imported_files/documents/BO_31_MESRI_1417448.pdf#page=61)
- [PC 2021 · approche ondulatoire, §6.5 (annexe 2)](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf#page=54)
