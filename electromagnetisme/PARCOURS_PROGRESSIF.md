# Champs & Matière : un parcours sup / spé

Commencer par forces, symétries et induction. En spé, utiliser les bilans et Maxwell pour expliquer champs, propagation et énergie. Les machines, matériaux et effets modernes viennent ensuite avec leurs modèles.

Prévoir 60 à 90 minutes par séance prioritaire. Les groupes de TP servent à comparer une même technique dans deux contextes ; les quatre branches au-delà sont indépendantes.

Repères MPSI/PCSI puis MP/PC, avec applications aux milieux et machines selon la filière. Le socle concerne champs, induction, conduction, ondes et énergie. Les lois complémentaires sont fournies : Biot–Savart n’est notamment pas un résultat exigible en MP. London, Kerr, MHD/dynamo et guide TE₁₀ complet sont des prolongements, pas des obligations supplémentaires.

[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)

## Avant de commencer

- Notations communes : c est la célérité de la lumière dans le vide, μ₀ sa perméabilité magnétique. Les unités de champ, de courant et de puissance figurent dans chaque TP.
- Sup : forces de Lorentz et Laplace, flux, induction, circuits et oscillateur.
- Sup : symétries, potentiel, produit vectoriel et amplitudes complexes.
- Spé : Gauss, Ampère, Maxwell, Poynting, propagation et conditions aux limites selon la filière.

## Pour chaque séance

1. Prévoir une symétrie, un sens de courant ou un signe de flux avant de calculer.
2. Définir les champs, surfaces et unités utilisés dans le bilan.
3. Changer un seul réglage puis contrôler charge, puissance ou flux.
4. Distinguer formule admise, calcul demandé et description complète d’un matériau réel.

## Sup : trois séances de champs et de couplages

Commencer par les forces et les phases avant les équations locales.

### 1. Un champ se lit par ses sources et ses symétries

**Techniques incontournables** · Sup · champ, potentiel et orientation

Relier charges, courant et géométrie sans confondre champ et ligne tracée.

**À faire :** Noter q la charge, a la séparation des deux charges et r la distance d’observation. Comparer la paire exacte au dipôle lorsque r/a augmente. Dans Oersted, inverser le courant I et prévoir le sens du champ.

**Acquis attendu :** Identifier les directions imposées par symétrie et contrôler le domaine de l’approximation dipolaire.

**Limites et compléments :** Les formules de champ sont données. L’intégration générale de Biot–Savart sera un complément ; une ligne de champ n’est pas une trajectoire de charge.

**TP associés :** Deux charges : quand le dipôle devient exact ; Oersted, spire et solénoïde finis

### 2. Une induction freine et chauffe

**Techniques incontournables** · Sup · Faraday, Lenz et bilan de puissance

Déterminer le signe de la f.é.m. puis vérifier où va l’énergie mécanique.

**À faire :** Choisir le rail. Noter B le champ, ℓ la longueur mobile, v la vitesse, R la résistance et L l’inductance. Prévoir le courant et la force lorsque v change de signe ; comparer les puissances mécaniques et Joule.

**Acquis attendu :** Justifier le freinage et ajouter l’énergie magnétique stockée lorsque L n’est pas négligeable.

**Limites et compléments :** Le sens de Lenz ne remplace pas une convention de flux. Les champs et le circuit sont ceux du modèle annoncé.

**TP associés :** Lenz : le freinage se paie en chaleur

### 3. Un haut-parleur est électrique et mécanique

**Techniques incontournables** · Sup · oscillateur couplé et résonance

Relier force de Laplace et tension induite par un même couplage.

**À faire :** Noter i le courant, v la vitesse de la membrane et κ le coefficient de couplage. Identifier les termes κi et κv dans les deux équations ; faire varier la fréquence puis κ.

**Acquis attendu :** Contrôler les unités et expliquer l’échange de puissance κiv entre circuit et mécanique.

**Limites et compléments :** Le modèle linéaire fournit les paramètres. Directivité acoustique, échauffement et grandes amplitudes ne sont pas calculés.

**TP associés :** Haut-parleur : deux équations, un même couplage

## Spé : cinq séances de champs, transport et énergie

Les théorèmes et les hypothèses fixent le calcul avant le tracé.

### 4. Choisir une surface de Gauss

**Techniques incontournables** · Spé · électrostatique et symétries

Calculer champ et potentiel à partir d’une charge enfermée.

**À faire :** Noter Q la charge totale et R le rayon de la sphère. Comparer intérieur et extérieur, puis le câble coaxial. Choisir une surface adaptée et vérifier les raccordements du potentiel et du champ.

**Acquis attendu :** Séparer symétrie, théorème de Gauss et intégration du champ ; retrouver les limites loin de la distribution.

**Limites et compléments :** Le potentiel possède une référence choisie. La formule du dipôle n’est pas valable près de chaque charge.

**TP associés :** Gauss : sphère chargée et câble coaxial ; Deux charges : quand le dipôle devient exact

### 5. Des porteurs expliquent conduction et Hall

**Techniques incontournables** · Spé · transport de charge et bilan des forces

Relier une équation de mouvement à un courant et à un signe de tension.

**À faire :** Noter n la densité, q la charge du porteur, τ le temps de relaxation et B le champ. Dans Drude, comparer fréquence faible et forte devant 1/τ. Dans Hall, inverser B puis le type de porteur.

**Acquis attendu :** Expliquer retard du courant, signe de Hall et rôle de l’épaisseur ; convertir les densités avant le calcul.

**Limites et compléments :** Drude et Hall sont exploités avec leurs hypothèses fournies. Mobilités multiples, structure de bandes et effet Hall quantique sont hors de ces TP.

**TP associés :** Drude : la conduction a une mémoire ; Hall : le signe des porteurs devient mesurable

### 6. Transporter ou stocker l’énergie du champ

**Techniques incontournables** · Spé · Maxwell et Poynting

Distinguer densité d’énergie, flux instantané et flux moyen.

**À faire :** Noter E,B les champs et Π le vecteur de Poynting. Comparer onde progressive et deux ondes opposées. Dans le conducteur, noter σ la conductivité et f la fréquence ; multiplier f par 100.

**Acquis attendu :** Retrouver un flux moyen nul pour la stationnaire et une profondeur de peau divisée par 10 dans le régime retenu.

**Limites et compléments :** Le conducteur obéit ici à Ohm et aux approximations affichées. Une peau très grande à basse fréquence n’est pas un état Meissner.

**TP associés :** Maxwell : transporter ou stocker l'énergie ; Peau harmonique et diffusion magnétique

### 7. Raccorder les champs et les flux

**Techniques incontournables** · Spé · interfaces et diffraction

Vérifier conservation d’énergie et effet d’une ouverture.

**À faire :** Noter n₁,n₂ les indices et R,T les rapports de flux. Commencer à incidence normale et vérifier R+T=1. Pour l’ouverture uniforme, noter a sa largeur et λ la longueur d’onde ; comparer a/λ grand et petit.

**Acquis attendu :** Distinguer coefficient de champ et coefficient énergétique ; prévoir les premiers zéros de diffraction et leurs conditions d’existence.

**Limites et compléments :** Les cas obliques TE/TM, Brewster et le pointage sont des compléments fournis selon le programme suivi. Aucune directivité tridimensionnelle n’est déduite ici.

**TP associés :** Fresnel : flux, Brewster et réflexion totale ; Ouverture : un sinc² dans l'espace angulaire

### 8. Un dipôle rayonne selon une géométrie

**Techniques incontournables** · Spé · ondes, flux et modèle dipolaire fourni

Relier direction, fréquence et puissance dans une approximation annoncée.

**À faire :** Noter p₀ l’amplitude dipolaire, ω la pulsation et θ l’angle à son axe. Choisir « Dipôle imposé », lire les directions de rayonnement nul, puis doubler p₀ à ω fixé. Choisir ensuite « Électron lié » pour comparer la diffusion loin sous la résonance et près d’elle.

**Acquis attendu :** Retrouver la dépendance en p₀² et, pour un dipôle imposé, en ω⁴ ; distinguer puissance totale et section efficace.

**Limites et compléments :** Le champ rayonné et le modèle d’oscillateur sont fournis. La théorie complète du rayonnement, l’extinction et la réaction radiative dépassent cette séance.

**TP associés :** Dipôle : Rayleigh, résonance, Thomson

## Approfondissements : quatre applications accompagnées

Les formules nouvelles réinvestissent champs, circuits et réponses linéaires.

### 9. Fabriquer une zone de champ uniforme

**Approfondissement CPGE** · Sup / Spé · magnétostatique et dérivées

Comparer géométrie d’une source et uniformité d’un champ.

**À faire :** Noter R le rayon des bobines, d leur séparation et I le courant. Avec la formule axiale fournie, comparer d/R<1, d/R=1 et d/R>1 ; calculer la courbure au centre.

**Acquis attendu :** Justifier le choix Helmholtz par une dérivée seconde nulle, sans confondre uniforme localement et constant partout.

**Limites et compléments :** Biot–Savart est fourni, hors résultat exigible MP. Le calcul de champ d’un solénoïde fini est un complément à la symétrie et à Ampère.

**TP associés :** Oersted, spire et solénoïde finis ; Helmholtz : fabriquer une zone uniforme

### 10. Transformer la puissance et la perdre

**Approfondissement CPGE** · Spé · moteurs et matériaux, selon la filière

Lire angle de charge, glissement et pertes sans confondre leurs modèles.

**À faire :** Noter Ωs la vitesse synchrone, Ωr celle du rotor et s=(Ωs−Ωr)/Ωs le glissement. Comparer rotor arrêté, faible glissement et génératrice. Dans le transformateur, relier aire du cycle B(H), fréquence et puissance dissipée.

**Acquis attendu :** Contrôler les signes des puissances et le bilan du rotor ; distinguer pertes Joule et hystérésis.

**Limites et compléments :** Les modèles triphasés et le cycle didactique sont fournis. Ils ne remplacent pas la commande vectorielle ou le dimensionnement d’une machine réelle.

**TP associés :** Synchrone : angle de charge et stabilité ; Asynchrone : glissement et partage de puissance ; Mesurer B et H, reconstruire une hystérésis

### 11. Une réponse collective donne une coupure

**Approfondissement CPGE** · Spé · dispersion dans un plasma froid

Interpréter une relation de dispersion à partir d’un mouvement de charges.

**À faire :** Noter ωp la pulsation plasma, ω celle de l’onde et ν la fréquence de collision. Commencer à ν=0 et comparer ω/ωp=0,5 et 1,5 ; ajouter ensuite ν près de la coupure.

**Acquis attendu :** Distinguer propagation, évanescence et absorption ; choisir le signe du nombre d’onde complexe compatible avec une décroissance.

**Limites et compléments :** Le plasma froid et son modèle collisionnel sont fournis. Plasma chaud, champ magnétique et amortissement cinétique ne sont pas déduits de cette relation.

**TP associés :** Plasma froid : coupure, collisions et absorption

### 12. Un milieu répond au champ

**Approfondissement CPGE** · Spé · oscillateur, dipôles et polarisation

Comparer réponses électrique et magnétique avec leurs variables propres.

**À faire :** Noter P la polarisation, M l’aimantation et θ l’angle de Faraday. Pour Lorentz, changer fréquence et amortissement ; pour les moments, comparer énergie magnétique et thermique. Dans Faraday, comparer passage simple et aller-retour.

**Acquis attendu :** Distinguer dispersion, saturation et rotation non réciproque ; contrôler les unités de θ=VBℓ.

**Limites et compléments :** Langevin, champ démagnétisant et modes circulaires sont des compléments guidés selon la filière. Le modèle n’est pas une description générale de tous les matériaux.

**TP associés :** Lorentz et charges liées d'une sphère ; Dia et paramagnétisme : modèle et champ interne ; Faraday : une rotation non réciproque

## Au-delà : quatre branches modernes

Ces branches introduisent les équations et concepts supplémentaires avant leur emploi.

### A. Un supraconducteur n’est pas seulement un métal parfait

**Au-delà du programme** · Au-delà · London et Meissner

Distinguer histoire d’un champ et profil d’équilibre supraconducteur.

**À faire :** Noter a la demi-épaisseur et λL la longueur de London. Comparer a/λL=1 puis 5 ; lire B(0)/B₀. Changer l’histoire du conducteur parfait et comparer au profil London.

**Acquis attendu :** Expliquer pourquoi E=0 impose un champ constant dans le temps, tandis que Meissner impose un autre état d’équilibre.

**Limites et compléments :** London, jauge et supraconductivité sont hors du socle. Les vortex et les supraconducteurs de type II ne sont pas décrits par cette plaque.

**TP associés :** London : pénétration depuis les deux faces ; Peau harmonique et diffusion magnétique

### B. Une onde modifie le milieu qui la guide

**Au-delà du programme** · Au-delà · Kerr et profil non linéaire

Relier intensité, variation d’indice et largeur d’une onde localisée.

**À faire :** Noter n₂ le coefficient Kerr, I₀ l’intensité de crête et y₀ la largeur caractéristique. Multiplier I₀ par quatre à n₂ fixé ; comparer profil auto-guidé et diffraction libre après une même distance réduite.

**Acquis attendu :** Vérifier les facteurs d’échelle et la solution sech fournie ; annoncer la normalisation de l’intensité.

**Limites et compléments :** Optique non linéaire et solitons sont des prolongements. Une solution exacte d’enveloppe ne prouve pas sa stabilité ni son réalisme à toute intensité.

**TP associés :** Kerr optique : un profil sech auto-guidé

### C. Une induction peut croître ou diffuser

**Au-delà du programme** · Au-delà · MHD et dynamo

Comparer les termes d’un modèle de génération magnétique.

**À faire :** Noter α le coefficient d’induction prescrit, ηm la diffusivité et k=2π/L. Calculer γ=±αk−ηmk² ; comparer les deux hélicités puis un grand Reynolds magnétique sans croissance.

**Acquis attendu :** Justifier le signe de γ et distinguer coefficient α, vitesse U et nombre Rm=UL/ηm.

**Limites et compléments :** Le modèle α² n’est pas une simulation complète du noyau terrestre. Fermeture turbulente, saturation et conditions globales sont des prolongements.

**TP associés :** Dynamo : croissance contre diffusion, sans seuil universel

### D. Un guide creux impose ses modes

**Au-delà du programme** · Au-delà · mode électromagnétique TE₁₀

Relier géométrie transverse, coupure et dispersion axiale.

**À faire :** Noter a la largeur du guide, f sa fréquence et fc=c/(2a). Comparer f<fc, f=fc et f>fc ; examiner le profil sin(πx/a), puis les vitesses de phase et de groupe.

**Acquis attendu :** Retrouver le changement de signe du carré du nombre d’onde axial et expliquer pourquoi une vitesse de phase supérieure à c ne transporte pas un signal à cette vitesse.

**Limites et compléments :** Le champ TE₁₀ complet est un prolongement fourni. Les familles de modes, les pertes et la relativité ne sont pas des prérequis supplémentaires.

**TP associés :** Guide TE₁₀ : propagation et coupure

## Repères de programme

- [MPSI 2021 · physique-chimie (annexe 2)](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/64/8/spe779_annexe_1373648.pdf#page=38)
- [PCSI 2021 · physique (annexe 2)](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/65/0/spe780_annexe_1373650.pdf#page=34)
- [MP 2021 · champs et ondes (BO complet)](https://www.enseignementsup-recherche.gouv.fr/sites/default/files/imported_files/documents/BO_31_MESRI_1417448.pdf#page=54)
- [PC 2021 · électromagnétisme et ondes (annexe 2)](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf)
