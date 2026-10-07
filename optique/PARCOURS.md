# Dix missions pour construire un raisonnement d’optique

Chaque mission associe une prédiction écrite, des réglages et un résultat vérifiable. Les durées sont indicatives : 30–50 min pour une première exploration, 1–2 h avec démonstrations et compte rendu. Les valeurs numériques des exercices constituent des contrôles indépendants des réglages par défaut.

**Repères de niveau.** Sup : géométrie de Gauss, trigonométrie, mesure, dérivation et bilans. Spé : réinvestissement d’ondes, d’interférences, de diffraction et d’outils numériques selon la filière. Au-delà : modèles accompagnés, dont Jones/Poincaré, ABCD de résonateur, filtrage cohérent et conversion non linéaire ; ils ne constituent pas un programme obligatoire commun. Chaque TP précise sa porte d’entrée et son approfondissement. Les sources de programmes sont dans [COURS.md](COURS.md).

## Mission 1 — Un rayon choisit-il la ligne la plus courte ?

**Laboratoires :** `snell`, `fermat`. **Entrée : Sup ; approfondissement : Spé.** Leçons 1, 2 et 18 ; exercices 1, 2, 23 et 24.

**Prévoir.** Dessiner le trajet air/verre et les angles à la normale. Avec h₁=8 cm, h₂=5 cm, X=20 cm et indices égaux, calculer l’intersection de la droite ; prévoir son déplacement si n₂ augmente.

**Expérimenter.** Placer volontairement la traversée loin du minimum, puis l’approcher. Comparer Snell dans les deux sens et dépasser le seuil de réflexion totale. Lire les fractions de puissance s, p, en particulier autour de Brewster.

**Justifier.** Dériver L(x), démontrer sa convexité et retrouver n₁sin i=n₂sin r. Relier ce résultat à la conservation de phase tangentielle. Calculer R+T en gardant la distinction amplitude/puissance.

**Livrable :** un schéma orienté, une courbe L(x), un optimum calculé et un seuil de réflexion totale expliqué.

## Mission 2 — Une image nette est une contrainte de conjugaison

**Laboratoires :** `lentille`, `bessel`, `oeil`. **Entrée : Sup ; prolongement : incertitudes.** Leçons 3 à 6 et 11 ; exercices 3 à 6, 11 et 12.

**Prévoir.** Déclarer p, p′ et f′ algébriques. Prédire les images pour un objet avant, sur et après le foyer. Fixer D puis étudier le discriminant de Bessel. Pour l’œil réduit à 17 mm, calculer l’accommodation à 25 cm.

**Expérimenter.** Passer de projection réelle à loupe, utiliser les deux mises au point de Bessel, puis comparer Silbermann et absence de netteté. Corriger une myopie et fermer la pupille en regardant les deux échelles de flou.

**Justifier.** Déduire f′=(D²−d²)/(4D), γ₁γ₂=1 et u(f′). Expliquer pourquoi positions proches et faible dérivée par rapport à d ne garantissent pas une meilleure mesure. Donner le signe de la correction oculaire.

**Livrable :** un tableau nature/position/taille d’images, une focale avec incertitude standard et une correction de signe justifié.

## Mission 3 — Agrandir ne suffit pas à résoudre

**Laboratoires :** `telescope`, `microscope`, `airy`. **Entrée : Sup ; diffraction : Spé selon filière.** Leçons 7 à 10 et 35 ; exercices 7 à 10, 45 et 46.

**Prévoir.** Calculer le grossissement d’une lunette puis d’un microscope. Pour D=200 mm, λ=550 nm, convertir 1,22λ/D en secondes d’arc. Ramener un pixel de caméra au plan objet du microscope.

**Expérimenter.** Changer l’oculaire à diamètre inchangé, puis changer le diamètre. Décaler l’objet du microscope de 20 μm. Dans Airy, comparer étoiles égales, compagnon faible et pupille annulaire.

**Justifier.** Séparer grossissement, collecte, NA, PSF et échantillonnage. Pourquoi somme-t-on les intensités de deux étoiles ? Pourquoi un pic central annulaire plus étroit ne suffit-il pas à garantir une meilleure détection d’un compagnon ?

**Livrable :** un budget de résolution de deux instruments, avec hypothèses de pupille et de cohérence explicitement indiquées.

## Mission 4 — Un milieu dirige les rayons et change leurs temps

**Laboratoires :** `fibre`, `mirage`. **Entrée : Sup ; invariant et propagation : Spé.** Leçons 12 à 14 ; exercices 13 à 16.

**Prévoir.** Calculer NA pour n₁=1,48, n₂=1,46. Pour le mirage a=20000 m, z₀=2 m, θ₀=−0,5°, prévoir le point bas et une éventuelle intersection avec le sol.

**Expérimenter.** Comparer rayon accepté et rayon rejeté par la fibre. Doubler L et comparer les retards. Pour le mirage, comparer parabole et trajectoire intégrée ; augmenter a puis observer un cas arrêté au sol et son prolongement apparent.

**Justifier.** Établir le cône d’acceptance et Δt=nL(1/cosθ−1)/c. Retrouver ncosθ invariant et le coefficient quadratique de la parabole. Distinguer rayons, fibre monomode et propagation d’un paquet spectral.

**Livrable :** deux invariants ou seuils calculés et une estimation d’étalement temporel, avec le domaine z≥0 respecté.

## Mission 5 — La dispersion crée des couleurs, la stationnarité les concentre

**Laboratoires :** `prisme`, `arcenciel`. **Entrée : Sup ; dérivation et caustique : Spé.** Leçons 15 et 16 ; exercices 17 à 20.

**Prévoir.** Calculer Dmin pour A=60°, n=1,50. Dans une goutte n=4/3, distinguer Dmin et rayon de l’arc autour du point antisolaire. Prévoir quelle couleur est à l’intérieur du primaire.

**Expérimenter.** Balayer l’incidence du prisme autour du retournement de raie, puis les longueurs d’onde. Dans la goutte, varier i autour de la stationnarité et comparer une/deux réflexions internes.

**Justifier.** Retrouver les formules d’indice au goniomètre et l’incidence stationnaire de la goutte. Ajuster n=a+b/λ² en annonçant les unités de b. Déduire le déplacement spectral par ∂D/∂n et expliquer le secondaire.

**Livrable :** une mesure d’indice depuis une déviation, un graphe D(i) et une explication de l’ordre des couleurs des deux arcs.

## Mission 6 — La meilleure focalisation est un compromis de modèles

**Laboratoires :** `aberrations`, `gaussien`. **Entrée : Sup ; diffraction et faisceaux : Spé/Au-delà.** Leçons 17 et 34 ; exercices 21, 22, 43 et 44.

**Prévoir.** Comparer sphère et parabole par développement de x(y). Pour un waist de 50 μm à 633 nm, prévoir zR et la divergence. Que change une ouverture plus petite pour l’aberration et pour la diffraction ?

**Expérimenter.** Fermer l’ouverture d’un miroir sphérique, déplacer l’écran, puis choisir le paraboloïde. Comparer petit/grand waist et les plans z=0, zR,3zR du gaussien ; vérifier la puissance intégrée.

**Justifier.** Prouver l’égalité des chemins vers le foyer du paraboloïde et annoncer sa portée axiale. Intégrer I(r, z) pour P constant. Relier la fermeture géométrique à une croissance de la largeur ondulatoire.

**Livrable :** un tableau qui sépare aberration, défocalisation, diffraction et taille du waist, accompagné de deux preuves courtes.

## Mission 7 — Une frange qui disparaît laisse plusieurs explications

**Laboratoires :** `young`, `michelson`, `coherence`. **Entrée : superposition ; Spé pour cohérence et TP.** Leçons 19, 20 et 26 à 28 ; exercices 25, 26 et 33 à 36.

**Prévoir.** Calculer interfrange/enveloppe de Young. Calculer le nombre de franges dû à une translation de miroir. Prévoir la différence entre enveloppe gaussienne, doublet et perte de cohérence spatiale.

**Expérimenter.** Déséquilibrer les fentes puis changer a et b séparément. Comparer Michelson lame/coin dans leurs plans adaptés. Dans Cohérence, balayer δ puis la largeur de source en maintenant les autres paramètres.

**Justifier.** Identifier une baisse de visibilité due aux amplitudes, au spectre, à l’étendue ou à l’indépendance des sources. Distinguer le facteur deux de Michelson de la première annulation d’un doublet. Déclarer un seuil de longueur de cohérence.

**Livrable :** un arbre de diagnostic expérimental, trois courbes contrastées et un protocole qui sépare deux causes de perte de contraste.

## Mission 8 — Deux spectromètres, deux mécanismes de finesse

**Laboratoires :** `reseau`, `fabryperot`. **Entrée : Spé ; interférences multiples accompagnées.** Leçons 21, 29 et 30 ; exercices 27, 28, 37 et 38.

**Prévoir.** Estimer N pour le doublet 589,0/589,6 nm. Pour R=0,90, e=5 mm, calculer coefficient d’Airy, ISL et finesse. Vérifier les ordres accessibles du réseau.

**Expérimenter.** Augmenter N puis m. Dans la cavité, changer R, e et angle interne séparément ; comparer résonance, antirésonance et absence de miroir réfléchissant.

**Justifier.** Les deux profils naissent d’une somme complexe, finie pour le réseau et infinie pour la cavité. Comparer largeur, séparation, répétition d’ordre et enveloppe de transmission. Ne pas appeler finesse le coefficient 4R/(1−R)².

**Livrable :** deux budgets de résolution spectrale et une justification du choix d’instrument selon largeur et ambiguïté d’ordre.

## Mission 9 — Transformer le champ avant de mesurer son intensité

**Laboratoires :** `polarisation`, `diffraction`, `fourier`. **Entrée : Spé ; Jones et 4f : Au-delà accompagné.** Leçons 22 à 25, 31 et 32 ; exercices 29 à 32, 39 et 40.

**Prévoir.** Calculer la sortie d’un quart d’onde à 45°. Identifier les zéros d’une pupille rectangle puis cosinus. Placer dans le plan Fourier les fréquences d’une modulation de période 50 μm.

**Expérimenter.** Tourner un analyseur après la lame, comparer apodisation et rectangle, puis filtrer un objet d’amplitude et de phase. Suivre norme Jones, transmission de pupille et bilan de puissance Fourier.

**Justifier.** Dans chaque expérience, l’opération porte d’abord sur un champ complexe ; le détecteur observe son module au carré. Distinguer conversion de polarisation, redistribution de fréquence spatiale et absorption passive. Vérifier une limite amovible et Nyquist.

**Livrable :** trois transformations de champ décrites par une matrice, une intégrale ou un masque, puis leurs intensités et bilans.

## Mission 10 — Entretenir et convertir une lumière laser

**Laboratoires :** `laser`, `nonlineaire`, `gaussien`. **Entrée : Spé par les ODE ; Au-delà accompagné.** Leçons 33, 34 et 36 ; exercices 41 à 44, 47 et 48.

**Prévoir.** Distinguer rayon de courbure et réflectivité, calculer stabilité et seuil d’un résonateur. Pour une pompe de 1064 nm, prévoir le photon généré et le facteur énergétique 2. Estimer la loi faible de conversion.

**Expérimenter.** Comparer gain insuffisant, oscillation saturée et géométrie instable, puis la frontière confocale. Dans le cristal, allonger L à accord parfait, changer Δk et comparer pompe constante/ondes couplées.

**Justifier.** Établir le seuil logarithmique et la puissance saturée. Retrouver sinc² par intégration de phase ; repérer la violation η>1 qui invalide la pompe constante. Vérifier Iω+I2ω et Nω+2N2ω ; expliquer la variante à deux pompes du recueil.

**Livrable :** un modèle de chaîne laser→faisceau→cristal comprenant source d’énergie, stabilité, seuil, focalisation et conservation, avec les extensions clairement identifiées.
