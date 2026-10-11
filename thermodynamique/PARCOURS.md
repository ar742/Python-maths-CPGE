# Quinze séances de thermodynamique

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le bilan adapté.

## Séance 01 — Transferts & diffusion

### Fourier : une barre relie deux thermostats

Relier le premier principe local, Fourier et la résistance de l’exercice 1.

1. Choisir la barre métallique et vérifier les unités de j et Φ.
2. Passer à l’isolant : comparer le même profil à une puissance différente.
3. Inverser les températures et prévoir le signe avant le calcul.

**À justifier :** Écrire une résistance avec sa géométrie et annoncer clairement le sens du flux.

### Un mur : conduction et convection en série

Utiliser l’analogie électrique sans perdre les surfaces et les températures d’interface.

1. Choisir brique et isolant puis lire les cinq températures.
2. Réduire l’isolant et observer sa part de résistance.
3. Réduire h extérieur : trouver où la chute de température augmente.

**À justifier :** Distinguer température d’air, température de surface et interface solide.

## Séance 02 — Transferts & diffusion

### Rayon critique : ajouter un isolant peut accroître la perte

Prolonger la coque de l’exercice 1 et expliquer pourquoi une isolation peut d’abord accroître la perte.

1. Choisir le cylindre et chercher le maximum sur la courbe de perte.
2. Passer à la sphère : comparer les deux seuils.
3. Choisir un rayon intérieur au-dessus du seuil et vérifier la décroissance.

**À justifier :** Dire si le rayon critique est accessible et distinguer Φ constant de j constant.

### Igloo : bilan d’une personne et géométrie hémisphérique

Reprendre l’exercice 2 avec une puissance nette définie et une géométrie sans ambiguïté.

1. Choisir neige isolante : lire puissance, température et statut de paroi.
2. Passer à la glace dense et expliquer le changement.
3. Changer le nombre de personnes puis regarder si l’épaisseur visée existe.

**À justifier :** Séparer un bilan idéal et une réalisation physique, avec puissance et rayon correctement définis.

## Séance 03 — Transferts & diffusion

### Diffusion 1D : calcul stable et modes de Fourier

Comparer une solution modale à un véritable schéma de diffusion stable.

1. Préparer deux modes et suivre la disparition des détails.
2. Comparer FTCS et modes exacts au temps final.
3. Augmenter N : lire l’erreur et le nombre de pas réellement utilisés.

**À justifier :** Contrôler la stabilité avant de confondre un défaut numérique avec un phénomène physique.

### Choc thermique : une profondeur en √(χt)

Relier l’exercice 6, l’échelle de diffusion et un bilan d’énergie indépendant.

1. Chauffer la surface et lire flux puis énergie.
2. Multiplier le temps par quatre : tester les trois lois d’échelle.
3. Refroidir et vérifier les valeurs algébriques négatives.

**À justifier :** Distinguer une singularité de flux intégrable et une énergie infinie.

## Séance 04 — Transferts & diffusion

### Onde thermique : filtrer le jour et les saisons

Prolonger l’exercice 7 en comparant les profondeurs atteintes par deux cycles concrets.

1. Observer le cycle journalier à 0,2 m.
2. Passer au cycle annuel à 2 m et comparer δ.
3. Revenir au jour à 1 m : expliquer la petite amplitude malgré un retard important.

**À justifier :** Lire séparément amplitude et phase, en identifiant la fréquence choisie.

### Biot : quand peut-on supposer une température uniforme ?

Choisir le modèle de refroidissement en confrontant sa validité à un profil spatial.

1. Choisir Bi petit : comparer toutes les températures.
2. Choisir Bi grand : repérer le gradient centre–surface.
3. Réduire l’épaisseur et suivre l’amélioration du modèle capacitif.

**À justifier :** Donner la longueur caractéristique et vérifier une approximation avant de l’utiliser.

## Séance 05 — Transferts & diffusion

### Une tache de chaleur : énergie conservée, pic qui s’étale

Relier une carte de température à un bilan énergétique et à des variances définies.

1. Lire la carte et l’énergie intégrée.
2. Multiplier le temps par quatre et comparer les largeurs.
3. Réduire la largeur initiale puis retrouver sa disparition progressive.

**À justifier :** Utiliser 2χt par direction et 4χt pour la diffusion radiale en 2D.

### Marche aléatoire : de la loi binomiale à Fick

Déduire la diffusion de sauts probabilistes en gardant une référence exacte.

1. Choisir peu de pas et observer le caractère discret.
2. Augmenter N : comparer binomiale et gaussienne.
3. Introduire p=0,7 et distinguer déplacement du centre et étalement.

**À justifier :** Relier variance et coefficient diffusif en tenant compte de la parité du réseau.

## Séance 06 — Transferts & diffusion

### Langevin : du mouvement inertiel à Stokes–Einstein

Mettre le TP de Langevin en relation avec les échelles réelles et la moyenne statistique.

1. Observer t≈τᵥ et comparer à 2Dt.
2. Choisir le temps court puis lire le comportement en t².
3. Passer aux secondes et augmenter la viscosité : comparer les amplitudes de diffusion.

**À justifier :** Définir l’état initial et la dimension du déplacement avant d’extraire D.

### Neutrons : diffusion, absorption et bilan de source

Prolonger l’exercice 3 en contrôlant la source par un bilan, pas seulement par une forme exponentielle.

1. Lire L et le nombre total Qτ.
2. Comparer débit traversant et absorption intérieure à r=L.
3. Modifier τ puis Q : distinguer longueur et simple changement d’amplitude.

**À justifier :** Fixer la constante par la source et vérifier le débit à chaque rayon.

## Séance 07 — Transferts & diffusion

### Électrolyte : diffusion commune et potentiel de jonction

Relier diffusion particulaire, courant électrique et champ créé par une jonction.

1. Comparer les flux des ions et Fick ambipolaire.
2. Égaliser les diffusivités et vérifier le champ nul.
3. Inverser les concentrations et prévoir le signe du potentiel.

**À justifier :** Établir le signe par la convention de potentiel et justifier le flux commun.

### Diffuser sans perdre d’énergie : l’entropie augmente

Vérifier ensemble le premier et le second principe dans un système isolé diffusif.

1. Préparer deux moitiés de températures différentes.
2. Comparer énergie constante, entropie croissante et production décroissante.
3. Choisir l’état uniforme : vérifier les trois bilans nuls.

**À justifier :** Distinguer conservation d’énergie et production d’entropie avec des températures absolues.

## Séance 08 — Potentiels, travaux & machines

### Même état final, travaux différents : suivre trois chemins

Distinguer fonctions d’état et transferts en comparant trois transformations ayant exactement les mêmes extrémités.

1. Choisir k=1 : contrôler W=−RT ln r et ΔU=0.
2. Choisir k=1,4 : vérifier Q=0 et ΔS=0.
3. Comparer les deux autres travaux, puis inverser la détente en compression.

**À justifier :** Les aires changent avec le chemin ; ΔU et ΔS sont communes parce que les états initial et final sont communs.

### Surface, fil, condensateur, bobine : une force conjuguée

Reconnaître l’effort et la coordonnée conjugués, contrôler leurs unités et interpréter une restitution d’énergie.

1. Étirer le fil : comparer le travail à la variation kx²/2.
2. Passer au condensateur et lire la conversion entre s et q.
3. Choisir la bobine puis inverser les deux états : le travail change de signe.

**À justifier :** Un même schéma d’intégration traite des dispositifs distincts, à condition de définir correctement les grandeurs et les unités.

## Séance 09 — Potentiels, travaux & machines

### Helmholtz : une cloison interne cherche le minimum de F

Utiliser un potentiel sous contraintes et relier son minimum à un véritable équilibre mécanique interne.

1. Mettre ks=0 : l’équilibre égalise les pressions.
2. Ajouter un ressort décentré : les pressions d’équilibre deviennent différentes.
3. Changer la position initiale : le minimum reste le même mais l’énergie libre perdue change.

**À justifier :** Le volume total fixe laisse une variable interne évoluer. Le minimum de F traduit le bilan des forces et sa courbure assure la stabilité.

### Gibbs : l’équilibre d’une réaction A ⇌ B minimise G

Relier composition, potentiel chimique, constante d’équilibre et minimum de Gibbs.

1. Prendre ΔrH°=ΔrS°=0 : trouver x=1/2.
2. À T=300 K, choisir une réaction favorable à B et lire le sens à la composition initiale.
3. Augmenter T avec ΔrH°<0,ΔrS°<0 : observer le changement de majorité.

**À justifier :** ΔrG donne le sens spontané à la composition courante ; ΔrG° seul ne suffit pas. Le minimum fixe un état, pas une cinétique.

## Séance 10 — Potentiels, travaux & machines

### Calorimètre : température finale, chaleur latente et entropie

Établir un bilan de calorimétrie, reconnaître un changement de phase et vérifier le second principe.

1. Choisir les deux corps sans phase et vérifier une moyenne pondérée.
2. Ajouter davantage de glace : identifier le palier à 273,15 K.
3. Choisir le cas froid extrême : l’eau initiale gèle ; contrôler que l’entropie totale reste positive.

**À justifier :** Le bilan choisit la phase finale. Une température au point de fusion ne détermine pas à elle seule les masses de chaque phase.

### Joule : U constante ou H constante, deux détentes différentes

Choisir U ou h selon le système et déterminer le signe réel d’un refroidissement ou d’un réchauffement.

1. Choisir le gaz parfait dans le vide : T reste constante, S augmente.
2. Choisir van der Waals dans le vide : vérifier Δu=0 et le refroidissement.
3. Comparer les deux presets d’étranglement : µJT change de signe et h reste constante.

**À justifier :** Les deux expériences sont adiabatiques mais ne conservent pas la même grandeur. Une chute de pression ne garantit pas un refroidissement.

## Séance 11 — Potentiels, travaux & machines

### Carnot : moteur, réfrigérateur et pompe à chaleur

Construire les performances et les signes d’une machine avec les deux principes, puis chiffrer ses irréversibilités.

1. Mettre φ=1 : vérifier l’entropie créée nulle.
2. Réduire φ en moteur : suivre la chaleur rejetée et le travail.
3. Passer du frigo à la PAC : vérifier COPc−COPf=1.

**À justifier :** Les signes résultent du système choisi. Le COP peut dépasser 1, et les pertes se lisent dans le second principe.

### Otto, Diesel, Brayton, Stirling : comparer des cycles calculés

Comparer des cycles à partir de leurs branches calculées, puis comprendre l’effet d’une régénération interne.

1. Choisir Otto : repérer les deux isochores dans P,V.
2. Passer à Diesel puis Brayton : identifier les isobares et le sens de r.
3. En Stirling, modifier ε : l’aire ne change pas, mais la chaleur externe et le rendement changent.

**À justifier :** La même convention ferme tous les bilans. La géométrie du cycle et les échanges externes ne donnent pas la même information lorsqu’un régénérateur est présent.

## Séance 12 — Potentiels, travaux & machines

### Compresseur : répartir les rapports de pression pour minimiser le travail

Appliquer le premier principe aux écoulements et optimiser les pressions intermédiaires sous refroidissement.

1. Avec N=2, choisir f=1/2 : retrouver la moyenne géométrique.
2. Éloigner f du minimum : comparer le travail.
3. Augmenter N puis réduire ηs : distinguer gain d’étagement et pertes internes.

**À justifier :** Les pressions optimales forment une suite géométrique. Le refroidisseur rejette une chaleur et ne fournit pas un travail d’arbre négatif.

### Corps fini : une différence de température vaut-elle du travail ?

Quantifier le travail maximal d’un corps fini et distinguer conservation de l’énergie et destruction d’exergie.

1. Comparer C(Ti−T₀) à B pour un corps chaud.
2. Mettre φ=0 : le contact direct fournit zéro travail et détruit B.
3. Choisir Ti<T₀ : le corps se réchauffe mais un travail maximal positif existe.

**À justifier :** L’exergie dépend de l’environnement et s’annule à l’équilibre. L’énergie ne disparaît pas quand l’exergie est détruite.

## Séance 13 — Effets couplés & mesures

### Cube de Leslie : comparer des surfaces à même température

Comparer des émissivités, puis transformer les échanges thermiques en bilan du cube.

1. Choisir le preset TP et comparer les quatre signaux.
2. Rapprocher T de Tₐ : distinguer un signal nul d’une faible émissivité.
3. Augmenter h puis observer chauffage nécessaire et refroidissement.

**À justifier :** Le TP compare les surfaces ; le bilan inclut aussi la convection, que la thermopile ne mesure pas.

### Thermocouple : calibrer et compenser la jonction froide

Passer d’une tension mesurée à une température avec une référence connue.

1. Mettre s₁=0 : retrouver V=S₀(Th−Tf).
2. Choisir une calibration courbe et comparer la température retrouvée à l’approximation.
3. Ajouter 5 K d’erreur froide et expliquer le biais avec les coefficients locaux.

**À justifier :** Une tension de thermocouple dépend de deux températures. La compensation froide fait partie de la mesure.

## Séance 14 — Effets couplés & mesures

### Module Peltier : refroidir demande un bilan complet

Décider si un module refroidit et vérifier ses bilans d’énergie et d’entropie.

1. Avec le premier preset, vérifier Qh=Qc+P.
2. Passer au courant excessif : repérer le rôle du terme en I².
3. Couper le courant, puis faire varier la charge pour discuter l’équilibre.

**À justifier :** Un courant non nul ne garantit pas le refroidissement. Le signe de Qc décide du mode de fonctionnement.

### Onde sonore : coupler compression et diffusion thermique

Résoudre deux équations couplées et donner un sens à un nombre d’onde complexe.

1. Choisir λ=0 : retrouver c et la relation adiabatique entre τ et p.
2. Choisir une conduction renforcée : comparer vitesse et phase.
3. Modifier f et L ; distinguer longueur d’onde et longueur d’atténuation.

**À justifier :** La conduction change la relation température–pression et atténue l’onde. Le signe de Im k dépend de la convention.

## Séance 15 — Effets couplés & mesures

### Quartz : réciprocité, résonance et antirésonance

Déduire les effets direct et inverse d’une même énergie, puis étudier un résonateur.

1. Choisir le premier preset et observer l’amplification autour de fᵣ.
2. Renforcer θ : voir fₐ s’éloigner de fᵣ.
3. Augmenter ζ : le pic reste fini et le creux devient moins profond.

**À justifier :** Résonance et antirésonance sont deux mécanismes distincts. La réciprocité et la passivité proviennent de la même énergie.

### Détente d’une vapeur saturante : décider du début de condensation

Comparer deux pentes pour décider du début d’un changement d’état.

1. Prendre les valeurs de vapeur d’eau et comparer les pentes initiales.
2. Réduire L* : chercher la frontière de la carte où la marge s’annule.
3. Observer que la courbe de vapeur seule s’arrête à la condensation.

**À justifier :** Le critère explique le début du brouillard. Il ne donne pas l’évolution ultérieure du mélange liquide–vapeur.
