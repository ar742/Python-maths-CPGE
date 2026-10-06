# Électromagnétisme — dix missions de formation

Le parcours réunit 36 leçons, 48 corrigés et 24 expériences. Pour chaque séance : annoncer une prédiction chiffrée, modifier un seul paramètre à la fois, puis rédiger une justification et une limite du modèle. Une capture d’écran illustre la conclusion ; les unités et le calcul la fondent. Les expériences sont numériques : un réglage proposé n’est pas une consigne de réalisation matérielle.

Les repères **Sup**, **Spé** et **Au-delà** indiquent trois portes d’entrée par les outils. Ils ne remplacent pas les programmes de chaque filière. En MPSI, [l’annexe officielle 2021](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/64/8/spe779_annexe_1373648.pdf), partie 1.7, traite notamment induction, rails, flux et bilans ; elle exclut l’étude générale du champ électromoteur. En PSI, [l’annexe officielle 2021](https://cache.media.education.gouv.fr/file/31/03/9/ensecsup748_annexes_1417039.pdf), parties 4.4 et 5, traite matériaux magnétiques, pertes, transformateur et machine synchrone. Pour les ondes et le rayonnement, consulter les annexes [MP](https://cache.media.education.gouv.fr/file/31/08/5/ensecsup702_annexes_1417085.pdf) et [PC](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf) : leurs capacités et limites diffèrent. L’asynchrone triphasé, les champs locaux détaillés, London, Faraday tensoriel, Kerr localisé et dynamo α² sont proposés comme **extensions accompagnées**. Pour PCSI, PTSI, MPI ou PT, adapter avec le professeur aux textes de la filière ; ce document ne revendique pas une correspondance exhaustive.

Toutes les réponses complexes utilisent **exp(−iωt)**. Une tension doit toujours annoncer ses deux bornes. Les unités affichées par les commandes sont converties en SI par les moteurs ; noter notamment les fs, THz, nm, mH, MS·m⁻¹ et GW·cm⁻². Les hypothèses se trouvent en tête de chaque laboratoire et dans les calculs détaillés.

## Mission 1 — Une bonne approximation a un seuil

Laboratoires : `dipoles`, `gauss`. Leçons 2–6 ; exercices 1–4. Durée indicative : 60 min.

1. **Prévoir.** Calculer l’erreur du potentiel axial d’un dipôle à r=5a ; annoncer ce qui change pour le champ dérivé. Choisir ensuite une surface de Gauss pour une sphère volumique.
2. **Expérimenter.** Doubler r/a, puis le rayon de la sphère à charge fixée. Dans le coaxial, doubler la longueur à rapport b/a fixé.
3. **Justifier.** Rendre une page avec un développement limité, un calcul de flux et deux calculs de l’énergie. Comparer charge fixée et tension fixée.

**Sup :** unités, intégration et énergie. **Spé :** symétrie, gradient, Gauss et développement contrôlé. **Au-delà :** moments multipolaires et unicité de Poisson. **Livrable :** un seuil relatif associé à une grandeur et une géométrie, avec le cas des zéros explicitement discuté.

## Mission 2 — Construire puis mesurer un champ

Laboratoires : `biotsavart`, `helmholtz`, `hall`. Leçons 7–8 et 11 ; exercices 5–8 et 11–12. Durée : 75 min.

1. **Prévoir.** Orienter I,B et la normale d’une spire ; calculer le champ de deux bobines au centre. Pour Hall, fixer I vers +x,B vers +z et UH=V(−w/2)−V(+w/2), puis prédire le signe pour q=−e.
2. **Expérimenter.** Comparer bobine courte et longue ; régler d/R de part et d’autre de un. Inverser les porteurs puis B dans la plaquette de Hall.
3. **Justifier.** Annuler B″(0), convertir une tension en densité dans le modèle à un porteur et proposer une antisymétrisation contre un contact mal placé.

**Sup :** produits vectoriels, superposition et dérivées. **Spé :** magnétostatique et calibration. **Au-delà :** uniformité volumique et transport multibande. **Livrable :** un schéma avec axes et bornes, une tolérance axiale chiffrée et une procédure de mesure discriminant le signe des porteurs.

## Mission 3 — La conduction répond avec mémoire

Laboratoires : `drude`, `peau`. Leçons 9–10 et 23 ; exercices 9–10 et 23–24. Durée : 60 min.

1. **Prévoir.** Déduire σ₀=nq²τ/m*, calculer ωτ, puis prévoir la phase du courant. Estimer la profondeur de peau du cuivre à 1 kHz et 100 kHz.
2. **Expérimenter.** Comparer réponses faible fréquence et inertielle ; passer du régime harmonique à l’échelon de champ magnétique.
3. **Justifier.** Fermer le bilan cinétique/chaleur, puis déduire la diffusion magnétique avec coefficient positif. Comparer δ∝f⁻¹ᐟ² à la profondeur transitoire ∝√t.

**Sup :** ODE d’un échelon, racines et dimensions. **Spé :** phasors, puissance moyenne et propagation dissipative. **Au-delà :** noyau causal et pôles de la réponse. **Livrable :** deux graphiques annotés et l’explication de leur différence, sans assimiler le courant continu à une peau d’épaisseur constante.

## Mission 4 — Convertir sans créer d’énergie

Laboratoires : `induction`, `hautparleur`. Leçons 12–14 ; exercices 13–16. Durée : 75 min.

1. **Prévoir.** Pour le rail, écrire Li̇+Ri=−Bℓv et mv̇=Bℓi avec les orientations de l’atelier. Classer le régime amorti. Calculer f₀ et κ²/b pour le haut-parleur.
2. **Expérimenter.** Comparer le rail inductif oscillant et le cadre entrant dans le champ. Repérer l’immersion complète ; régler le haut-parleur près de sa résonance puis augmenter κ.
3. **Justifier.** Sommer les bilans d’énergie et identifier les termes de couplage qui s’annulent. Montrer que le cadre complètement immergé retrouve une chute libre dans ce modèle.

**Sup :** Lenz, rail et oscillateur. **Spé :** équations couplées et impédance motrice. **Au-delà :** charge acoustique et inductances distribuées. **Livrable :** un bilan qui explique courant, force et chaleur ; une résonance interprétée par la contre-fém, et non par la seule amplitude de déplacement.

## Mission 5 — Une histoire magnétique laisse une aire

Laboratoires : `hysteresis`, `aimantation`. Leçons 15–17 ; exercices 17–18 et 37–38. Durée : 75 min.

1. **Prévoir.** Relier e₂ à Ḃ et H au courant primaire. Estimer les pertes d’un cycle rectangulaire. Calculer la pente faible champ de Langevin puis celle de tanh.
2. **Expérimenter.** Comparer cycle majeur, mineur et réversible ; comparer moments classiques, deux niveaux et diamagnétisme orbital. Modifier le facteur démagnétisant.
3. **Justifier.** Relier ∮H dB à une chaleur par volume ; retrouver l’intégrale orientée de Boltzmann et déclarer Hint=Hext−NM.

**Sup :** intégration et limites de fonctions. **Spé :** mesure H/B et énergie, particulièrement dans le parcours PSI. **Au-delà :** statistiques d’orientation et stabilité de Weiss sur papier. **Livrable :** une distinction entre mémoire de domaines, orientation de moments indépendants et réponse orbitale induite. Le laboratoire d’aimantation ne calcule pas de ferromagnétisme collectif.

## Mission 6 — Synchronisme, glissement et puissance signée

Laboratoires : `synchrone`, `asynchrone`. Leçons 19–20 ; exercices 19–22. Durée : 60–75 min.

1. **Prévoir.** Classer les retards 30° et 150° sous la même charge ; calculer Ωs. Pour l’asynchrone, calculer Pm et PJrotor à s=0,05 puis les signes en génératrice.
2. **Expérimenter.** Comparer branches du couple-angle puis dépasser le seuil statique. Dans le circuit asynchrone, comparer synchronisme, démarrage et glissement négatif ; modifier R₂.
3. **Justifier.** Linéariser autour d’un angle, fermer Pg=Pm+PJrotor et démontrer sur la spire simplifiée l’indépendance du couple moyen par rapport à la phase initiale.

**Sup :** trigonométrie et énergie. **Spé :** stabilité et machine synchrone selon le programme ; phasors comme outils du prolongement asynchrone. **Au-delà :** capture dynamique, commande et circuit triphasé détaillé. **Livrable :** un bilan signé et un seuil statique ; aucune conclusion de démarrage complet sans intégration et conditions initiales.

## Mission 7 — Les limites d’un milieu choisissent ses ondes

Laboratoires : `maxwell`, `interfaces`, `guide`, `plasma`. Leçons 21–26 ; exercices 25–30 et 33–34. Durée : deux séances de 60 min.

1. **Prévoir.** Calculer flux moyen et énergie d’une onde progressive ; déduire r,t,R,T à une interface normale. Calculer fc d’un TE₁₀ puis fp d’un plasma froid.
2. **Expérimenter.** Passer à une onde stationnaire puis à Brewster et réflexion totale. Comparer TE₁₀ au-dessus, sous et à la coupure ; ajouter des collisions au plasma près de ωp.
3. **Justifier.** Raccorder E/H, séparer les variables et choisir une racine passive. Distinguer champ évanescent non nul, puissance moyenne et vitesse de phase.

**Sup :** superposition et phases, avec équations introduites. **Spé :** Maxwell, conditions aux limites et dispersion selon la filière. **Au-delà :** modes guidés complets et distinction transverse/longitudinale. **Livrable :** un tableau comparant les deux coupures et la réflexion totale, avec hypothèses et flux dans chaque régime.

## Mission 8 — Rayonner : taille, phase et couleur

Laboratoires : `antenne`, `rayonnement`. Leçons 28–30 ; exercices 31–32 et 45–46. Durée : 75 min.

1. **Prévoir.** Déduire les premiers zéros d’une ouverture de quatre λ ; prouver qu’ils n’existent pas pour une demi-longueur d’onde. Prévoir le rapport de diffusion entre 450 et 650 nm.
2. **Expérimenter.** Varier l’ouverture et le pointage ; comparer Rayleigh, résonance, Thomson et dipôle imposé.
3. **Justifier.** Intégrer les phases de l’ouverture puis sin²θ sur l’angle solide. Relier la diffusion bleue à λ⁻⁴ en séparant puissance, intensité et section efficace.

**Sup :** géométrie des trajets et ordre de grandeur. **Spé :** Poynting, rayonnement et diffraction selon la filière. **Au-delà :** réseaux, extinction et réaction radiative. **Livrable :** un diagramme angulaire et une puissance intégrée, avec ka≪1 et kr≫1 déclarés ; la tendance du ciel bleu n’est pas présentée comme une simulation complète de l’atmosphère.

## Mission 9 — La matière impose son champ intérieur

Laboratoires : `dielectrique`, `meissner`, `faraday`. Leçons 18,27,31–32 ; exercices 35–36 et 39–42. Durée : deux séances de 60 min.

1. **Prévoir.** Fixer les signes de −divP et ∂tP par conservation. Calculer B(0)/B₀ dans une plaque London ; décomposer ex dans les deux circulaires e±.
2. **Expérimenter.** Comparer absorption et dispersion, sphère statique, plaque épaisse et fine ; choisir les deux histoires du conducteur parfait. Comparer Faraday simple et double passage puis inverser B.
3. **Justifier.** Raccorder les champs et relier les phases propres à θF. Sur papier, compléter par l’orientation de dipôles électriques permanents et séparer Eextérieur,Einterne,Elocal.

**Sup :** ODE, fonctions hyperboliques et Malus. **Spé :** matière et polarisation selon le programme ; matrices complexes comme technique. **Au-delà :** London et non-réciprocité tensorielle, explicitement accompagnées. **Livrable :** trois distinctions : libre/lié, conducteur parfait/Meissner, rotation réciproque/Faraday.

## Mission 10 — Localisation et croissance : deux eigenproblèmes non linéaires ou fermés

Laboratoires : `kerr`, `dynamo`. Leçons 33–36 ; exercices 43–44 et 47–48. Durée : 75 min.

1. **Prévoir.** Trouver l’intégrale première de l’ODE Kerr et la relation amplitude-largeur. Pour α², calculer les deux γ et le seuil avec k=2π/L. Avec les valeurs illustratives U=0,1 mm·s⁻¹,L=1000 km,ηm=1 m²·s⁻¹, retrouver Rm=100 et L²/ηm≈31 700 ans ; le temps de décroissance du sinus est 1/(ηmk²), plus court d’un facteur 4π².
2. **Expérimenter.** Multiplier l’intensité Kerr par quatre ; comparer le sech et la gaussienne libre de même puissance physique, mais de profil différent. Changer l’hélicité puis imposer α=0 avec grand Rm.
3. **Justifier.** Vérifier le sech par dérivation ; distinguer Iref du flux Sz et noter Z=z/(n₀k₀y₀²). Pour la dynamo, montrer que Rm élevé peut coexister avec décroissance et nommer les paramètres prescrits. Relier à la leçon 35 la chaîne physique terrestre : flottabilité thermique/compositionnelle → convection organisée par rotation → induction → champ, avec dissipation et rétroaction de Lorentz. Sources : [USGS](https://www.usgs.gov/programs/geomagnetism/introduction-geomagnetism), [BGS](https://geomag.bgs.ac.uk/education/reversals.html).

**Sup :** exponentielle, dérivation et dimensions. **Spé :** intégrales premières, adimensionnement et valeurs propres comme outils. **Au-delà :** les deux phénomènes spécialisés sont des prolongements ; saturation, instabilité et géométrie globale ne sont pas calculées. **Livrable :** une démonstration et un contre-exemple, puis une liste courte des mécanismes absents qui limitent l’interprétation.

## Évaluation commune

Une production réussie annonce axes, bornes et variables ; justifie la méthode par symétrie ou limites ; conserve les unités dans les conversions ; ferme un bilan ou vérifie un invariant ; termine par une limite concrète. Une courbe seule ne remplace ni une hypothèse ni une démonstration. Les corrigés de [COURS.md](COURS.md) permettent une reprise autonome et les introductions donnent trois premiers gestes réalisables avec les commandes de chaque expérience.
