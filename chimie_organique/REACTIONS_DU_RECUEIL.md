# Chimie organique — atlas des réactions du recueil

**61 fiches de transformations et de règles**, centrées sur les pages imprimées **524 à 528**, puis **531 à 534**. Cet atlas est l’entrée de lecture pour les types de réactions, leurs produits, leurs règles et leurs mécanismes. Les textes et schémas du programme sont originaux ; les pages du document source ne sont pas redistribuées.

[Parcours guidés de réactions](PARCOURS_REACTIONS.md) · [Présentation et lancement](README.md) · [Cours initial et outils complémentaires](COURS.md)

Une fiche se lit dans l’ordre **substrat → conditions → produits → liaisons modifiées → sélectivité → caractérisation du produit → étapes → question corrigée**. « Caractériser » désigne ici reconnaître la fonction, la connectivité, les charges et la stéréochimie issues d’une transformation. IR, RMN, CCM et autres outils restent des compléments pour vérifier des propositions de produits.

Les familles désignent l’échelle annoncée : **AB** transfert acido-basique ; **AE** addition électrophile ; **AN** addition nucléophile ; **addition–élimination** substitution acyle ; **OR** oxydoréduction ; **E1/E2** éliminations ; **SN1/SN2** substitutions nucléophiles ; **SEA** substitution électrophile aromatique. Une transformation globale peut réunir plusieurs actes, par exemple AE, AN et AB pour l’hydratation acide. Le code AE seul n’est donc jamais employé ici pour masquer une addition–élimination acyle.

Les règles sont accompagnées de leur domaine : Markovnikov par un chemin ionique approprié, anti-Markovnikov par un autre mécanisme, Zaïtsev seulement après avoir vérifié les voies accessibles, orientation aromatique distincte de l’activation. Aucune propriété d’une espèce pure ni borne de stœchiométrie n’est transformée en proportion expérimentale ou rendement universel.

## Repères de pages

| Page imprimée | Fiches de l’atlas | Centre du travail |
| --- | ---: | --- |
| 524 | 4 | Formules, propriétés et règles |
| 525 | 11 | Types de réactions |
| 526 | 17 | Autres exemples / organomagnésiens |
| 527 | 5 | Exemples (suite) |
| 528 | 6 | Exemples (suite) |
| 531 | 8 | Alcènes et alcynes : applications |
| 532 | 2 | Autour du nitrobenzène |
| 533 | 5 | Alcènes et alcynes : applications |
| 534 | 3 | Autour du nitrobenzène |

## Page 524 — Formules, propriétés et règles

### Fiche 1 — Effet inductif : lire la polarisation avant l’attaque

**Famille :** Règle · **Niveau :** Sup → PC · **Identifiant :** `inductif`

**Substrat.** C–X, carbonyle et liaison C–Mg

**Réactifs et conditions.** Comparaison des électronégativités ; groupes −I / +I

**Produit / bilan.** Sites C électrophile ou nucléophile identifiés ; aucune molécule créée par la comparaison

**Liaisons et fonctions modifiées**

- La liaison C–O est polarisée Cδ+–Oδ− ; C–Mg est polarisée Cδ−–Mgδ+.
- Une charge partielle δ n’est pas une charge formelle entière.

**Règles et sélectivité**

- L’effet inductif s’atténue avec la distance ; il faut ajouter conjugaison et encombrement au raisonnement.

**Caractérisation du produit**

- Classer les sites avant de tracer une flèche : le C de C=O reçoit un doublet, le C de RMgX en fournit un.

**Étapes à reconstruire**

1. Identifier les liaisons polarisées.
2. Placer δ+ / δ− sans inventer une espèce ionique libre.
3. Proposer le site d’attaque en fonction du réactif.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `effets` et son scénario. Paramètres : `system=inductive, group=chloro, stage=1`.

**Domaine du modèle.** Le bouton illustre l’effet inductif dans une chaîne portant Cl ; C=O et C–Mg sont ensuite comparés dans carbonyle et grignard.

**Question.** Pourquoi le carbone d’un organomagnésien attaque-t-il un carbonyle ?

**Réponse.** C–Mg présente une polarisation inverse de C–O : le carbone organomagnésien est riche en électrons, celui du carbonyle est pauvre. La formation C–C doit déplacer simultanément les électrons π de C=O vers O.

### Fiche 2 — Effets mésomères : doublets, charges et conjugaison

**Famille :** Règle · **Niveau :** Sup → PC · **Identifiant :** `mesomerie`

**Substrat.** Anisole, chlorobenzène et nitrobenzène

**Réactifs et conditions.** Groupes +M / −M dans un système conjugué

**Produit / bilan.** Contributeurs électroniques d’une même molécule ; sites aromatiques différenciés

**Liaisons et fonctions modifiées**

- Les noyaux et les liaisons σ restent en place.
- Les flèches déplacent des électrons π ou un doublet, en conservant la charge totale.

**Règles et sélectivité**

- OCH₃ est donneur +M ; NO₂ est attracteur −M.
- Cl combine −I et +M : désactivation et orientation ortho/para peuvent coexister.

**Caractérisation du produit**

- Comparer les complexes σ des attaques ortho, méta et para ; une formule mésomère n’est pas un produit isolé.

**Étapes à reconstruire**

1. Repérer une suite d’orbitales p.
2. Construire des contributeurs respectant l’octet.
3. Comparer la stabilisation des intermédiaires accessibles.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `effets` et son scénario. Paramètres : `system=mesomeric, group=nitro, stage=2`.

**Question.** Pourquoi orientation et activation ne doivent-elles pas être confondues ?

**Réponse.** L’orientation compare des voies sur un même aromatique ; l’activation compare leur vitesse à celle du benzène. Un halogène retire par −I tout en stabilisant relativement certains complexes ortho/para par donation +M.

### Fiche 3 — Markovnikov : choisir le carbocation, puis vérifier ses migrations

**Famille :** Règle · **Niveau :** Sup → PC · **Identifiant :** `markovnikov`

**Substrat.** But-1-ène

**Réactifs et conditions.** HBr sans peroxydes ; comparer ensuite hydroboration–oxydation

**Produit / bilan.** 2-bromobutane en voie ionique ; butan-1-ol dans la voie hydroboration–oxydation

**Liaisons et fonctions modifiées**

- Une liaison π disparaît ; une liaison C–H et une liaison C–Br ou C–O sont créées.

**Règles et sélectivité**

- La protonation donne préférentiellement le carbocation le mieux stabilisé.
- Une migration 1,2 peut modifier le squelette avant capture.

**Caractérisation du produit**

- Repérer sur quel carbone se trouve Br ou OH ; contrôler la conservation du squelette, puis rechercher un réarrangement.

**Étapes à reconstruire**

1. Protonation de C=C.
2. Carbocation éventuellement réarrangé.
3. Capture nucléophile ; déprotonation si le nucléophile était H₂O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `effets` et son scénario. Paramètres : `system=markovnikov, group=alkyl, conditions=ordinary, stage=2`.

**Question.** Peut-on appliquer Markovnikov à toutes les additions d’alcènes ?

**Réponse.** Non. Cette justification par le carbocation convient aux additions ioniques concernées. Hydroboration, bromonium et chaîne radicalaire HBr suivent d’autres chemins et doivent être traités avec leur propre mécanisme.

### Fiche 4 — Zaïtsev : tendance de stabilité après le filtre géométrique

**Famille :** Règle · **Niveau :** Sup → PC · **Identifiant :** `zaitsev`

**Substrat.** Pentan-2-ol ; comparer au 2-bromopentane pour le cas à base encombrée

**Réactifs et conditions.** H⁺ / chauffage pour l’alcool ; tert-BuO⁻ pour le dérivé bromé du scénario alternatif

**Produit / bilan.** Pent-2-ène et pent-1-ène possibles ; tendance plus substituée ou moins encombrée selon le chemin

**Liaisons et fonctions modifiées**

- Rupture de Cα–groupe partant et Cβ–H ; création Cα=Cβ.
- OH doit être activé en H₂O partante dans la voie acide ; Br est le départ dans la voie basique alternative.

**Règles et sélectivité**

- Une petite base favorise souvent l’alcène le plus substitué parmi les voies accessibles.
- La géométrie anti, une base encombrée ou la conjugaison peuvent changer cette tendance.

**Caractérisation du produit**

- Dessiner chaque connectivité, puis attribuer E/Z si chaque carbone vinylique possède deux substituants différents.

**Étapes à reconstruire**

1. Lister les Hβ.
2. Éliminer les voies sans géométrie réactive.
3. Comparer seulement les voies restantes.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `effets` et son scénario. Paramètres : `system=zaitsev, group=alkyl, conditions=ordinary, stage=2`.

**Question.** Pourquoi Zaïtsev ne suffit-il pas dans une chaise cyclohexanique ?

**Réponse.** Une E2 standard exige Br axial et un Hβ axial opposé. Si le substituant occupe la place de ce H, le produit correspondant est inaccessible, même s’il serait le plus substitué.

## Page 525 — Types de réactions

### Fiche 5 — Acido-basique : activer un alcool par protonation

**Famille :** AB · **Niveau :** Sup → PC · **Identifiant :** `ab_alcool`

**Substrat.** Alcool ROH

**Réactifs et conditions.** Acide HA dans un milieu compatible

**Produit / bilan.** Oxonium ROH₂⁺ et A⁻

**Liaisons et fonctions modifiées**

- Une liaison O–H se crée ; la liaison H–A cède ses électrons à A.

**Règles et sélectivité**

- Le site basique est un doublet de O ; l’oxonium peut ensuite libérer H₂O.

**Caractérisation du produit**

- O possède trois liaisons et une charge +1 après protonation ; la somme des charges est conservée.

**Étapes à reconstruire**

1. Doublet O → H.
2. Liaison H–A → A.
3. Vérification des charges et du caractère du groupe partant.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `e1` et son scénario. Paramètres : `substrate=secondary, stage=0`.

**Question.** Pourquoi ROH₂⁺ est-il plus utile que ROH pour une substitution acide ?

**Réponse.** Le départ de ROH₂⁺ fournit l’espèce neutre H₂O ; le départ direct de HO⁻ à partir d’un alcool non activé est beaucoup moins favorable.

### Fiche 6 — AE : addition ionique de HBr sur un alcène

**Famille :** AE · **Niveau :** Sup → PC · **Identifiant :** `ae_hbr`

**Substrat.** Propène

**Réactifs et conditions.** HBr, absence de peroxydes

**Produit / bilan.** 2-bromopropane

**Liaisons et fonctions modifiées**

- C=C devient C–C ; H et Br s’ajoutent aux deux carbones.

**Règles et sélectivité**

- Régiochimie Markovnikov dans ce cas sans migration.
- Une espèce carbocationique plane peut être capturée sur les deux faces.

**Caractérisation du produit**

- Br est porté par le carbone secondaire ; l’insaturation a disparu.

**Étapes à reconstruire**

1. Les électrons π captent H ; H–Br se rompt hétérolytiquement.
2. Formation du carbocation secondaire.
3. Br⁻ attaque ce centre.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=propene, reagent=hbr, stage=2`.

**Question.** Quel intermédiaire commande le produit ?

**Réponse.** Le carbocation secondaire issu de la protonation est plus stabilisé que le primaire. Br⁻ capture ensuite le carbone qui porte la charge : la règle se déduit de ce chemin.

### Fiche 7 — AN : hydrure sur un carbonyle

**Famille :** AN · **Niveau :** Sup → PC · **Identifiant :** `an_carbonyle`

**Substrat.** Éthanal

**Réactifs et conditions.** NaBH₄ puis milieu protonant

**Produit / bilan.** Éthanol

**Liaisons et fonctions modifiées**

- Une liaison C–H se forme ; C=O devient C–O, puis O reçoit H.

**Règles et sélectivité**

- L’attaque porte sur Cδ+ ; le carbonyle est plan avant l’addition.

**Caractérisation du produit**

- Disparition de C=O et apparition d’OH ; vérifier le passage d’un C trigonal à un C tétraédrique.

**Étapes à reconstruire**

1. Transfert d’hydrure vers C ; π(C=O) → O.
2. Alcoolate tétraédrique.
3. Protonation de O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `carbonyle` et son scénario. Paramètres : `reaction=addition, stage=2`.

**Question.** Pourquoi le carbone ne doit-il pas garder C=O après l’attaque ?

**Réponse.** Le déplacement du doublet π vers O accompagne nécessairement la formation de la nouvelle liaison ; conserver C=O donnerait cinq liaisons au carbone et violerait l’octet.

### Fiche 8 — Addition–élimination : substituer sur un carbone acyle

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `ae_acyle`

**Substrat.** Chlorure d’éthanoyle et amine

**Réactifs et conditions.** Amine nucléophile ; base piège à HCl

**Produit / bilan.** Amide et sel chlorure

**Liaisons et fonctions modifiées**

- C–N remplace C–Cl ; C=O s’ouvre provisoirement puis se reforme.

**Règles et sélectivité**

- Le C acyle est trigonal au départ ; l’intermédiaire d’addition est tétraédrique.
- Cette substitution acyle ne se décrit pas par une SN2 sur un C tétraédrique.

**Caractérisation du produit**

- La fonction finale reste carbonylée ; nouvelle liaison C(acyle)–N, disparition C–Cl.

**Étapes à reconstruire**

1. Attaque de N ; π(C=O) → O.
2. Retour du doublet de O et départ Cl⁻.
3. Transfert du proton de N à une base.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `acylation` et son scénario. Paramètres : `activation=chloride, amine=2, base=0, stage=2`.

**Question.** Que devient le second équivalent d’amine ?

**Réponse.** Il sert de base et devient ammonium chlorure ; il ne fournit pas un second groupe lié au carbone acyle.

### Fiche 9 — OR : alcool secondaire ⇄ cétone

**Famille :** OR · **Niveau :** Sup → PC · **Identifiant :** `or_alcool`

**Substrat.** Alcool secondaire, par exemple propan-2-ol

**Réactifs et conditions.** Oxydant adapté ; voie inverse NaBH₄

**Produit / bilan.** Propanone ; voie inverse propan-2-ol

**Liaisons et fonctions modifiées**

- L’oxydation enlève deux H au bilan et crée C=O ; la réduction effectue le bilan inverse.

**Règles et sélectivité**

- Un alcool tertiaire n’est pas oxydé en cétone sans rupture de squelette dans ce cadre.

**Caractérisation du produit**

- Comparer OH, C=O, H porté par le carbone fonctionnel et degré d’oxydation de ce carbone.

**Étapes à reconstruire**

1. Identifier la fonction et le carbone oxydé.
2. Établir un bilan adapté au réactif réel.
3. Vérifier la chimiosélectivité avant de proposer le produit.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `oxydoreduction` et son scénario. Paramètres : `substrate=alcohol2, reagent=aqueous, stage=1`.

**Question.** Un tertiaire peut-il donner une cétone par le même simple bilan ?

**Réponse.** Non : le carbone portant OH ne possède pas de H. La conversion en carbonyle sans modifier ses trois liaisons C–C dépasserait sa valence.

### Fiche 10 — E1 : ionisation puis perte de Hβ

**Famille :** E1 · **Niveau :** Sup → PC · **Identifiant :** `e1_type`

**Substrat.** 2-Méthylbutan-2-ol, alcool tertiaire

**Réactifs et conditions.** H⁺ ; chauffage et milieu adaptés à une déshydratation

**Produit / bilan.** 2-Méthylbut-2-ène et/ou 2-méthylbut-1-ène ; H₂O au bilan

**Liaisons et fonctions modifiées**

- Protonation de OH ; départ C–OH₂ avant perte Cβ–H ; une liaison π se forme au dernier acte.

**Règles et sélectivité**

- Un carbocation peut tourner et se réarranger ; l’E1 n’est pas intrinsèquement stéréospécifique.
- La répartition des produits demande des données cinétiques ou expérimentales.

**Caractérisation du produit**

- OH disparaît au bilan de déshydratation ; identifier les Cβ et les alcènes effectivement possibles.

**Étapes à reconstruire**

1. ROH + H⁺ → ROH₂⁺.
2. Départ d’eau et carbocation.
3. Une base prélève Hβ ; Cβ–H → Cα=Cβ ; H⁺ est régénéré au bilan.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `e1` et son scénario. Paramètres : `substrate=tertiary, stage=2`.

**Domaine du modèle.** Le tableau général E1 est illustré ici par un alcool activé en milieu acide, avec H₂O comme départ.

**Question.** La loi de vitesse indique-t-elle la proportion E/Z ?

**Réponse.** Non. Une loi apparente d’ionisation peut décrire la disparition du précurseur activé ; les étapes après ce départ répartissent le flux. Le ratio des alcènes n’est pas fourni par l’ordre un et le paramètre de branchement est une donnée choisie.

### Fiche 11 — E2 : trois déplacements électroniques concertés

**Famille :** E2 · **Niveau :** Sup → PC · **Identifiant :** `e2_type`

**Substrat.** 2-bromobutane

**Réactifs et conditions.** Base ; conformation anti accessible

**Produit / bilan.** But-1-ène et/ou but-2-ène selon les voies retenues

**Liaisons et fonctions modifiées**

- B: → Hβ ; Cβ–H → Cβ=Cα ; Cα–Br → Br⁻, dans un même acte.

**Règles et sélectivité**

- Disposition anti-périplanaire standard ; configuration et conformation du réactif gouvernent le produit.

**Caractérisation du produit**

- La stéréochimie se prédit depuis une projection de Newman ; aucun carbocation intermédiaire.

**Étapes à reconstruire**

1. Placer Hβ et Br anti.
2. Tracer simultanément les trois flèches.
3. Dessiner l’alcène puis appliquer CIP.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `elimination` et son scénario. Paramètres : `system=acyclic, dihedral=180`.

**Question.** Pourquoi une étape concertée peut-elle avoir trois flèches ?

**Réponse.** Le nombre de flèches compte les doublets déplacés, pas le nombre d’intermédiaires. Ici trois doublets se réorganisent simultanément à travers un seul état de transition.

### Fiche 12 — SN1 : carbocation plan et capture des faces

**Famille :** SN1 · **Niveau :** Sup → PC · **Identifiant :** `sn1_type`

**Substrat.** Halogénoalcane ionisable

**Réactifs et conditions.** Solvant ionisant ; eau comme nucléophile dans la solvolyse

**Produit / bilan.** Alcool et X⁻ après transfert de proton

**Liaisons et fonctions modifiées**

- Rupture C–X puis formation C–O ; pas de liaison C–C nouvelle sauf migration.

**Règles et sélectivité**

- Un carbocation libre en milieu achiral donne la limite racémique si un centre chiral se reforme.
- Une paire d’ions peut rendre les deux faces inégalement accessibles.

**Caractérisation du produit**

- Distinguer racémisation limite, mélange de configurations et changement éventuel de constitution.

**Étapes à reconstruire**

1. Ionisation.
2. Capture par H₂O sur un carbone plan.
3. Déprotonation de l’oxonium.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `sn1` et son scénario. Paramètres : `substrate=secondary, bias=0, stage=2`.

**Question.** Une SN1 impose-t-elle toujours exactement 50/50 ?

**Réponse.** C’est la limite d’un carbocation libre dont les faces sont équivalentes. La cage de solvant, la paire d’ions ou un environnement chiral peuvent modifier ce résultat ; il faut préciser le modèle.

### Fiche 13 — SN2 : attaque arrière et inversion de Walden

**Famille :** SN2 · **Niveau :** Sup → PC · **Identifiant :** `sn2_type`

**Substrat.** Halogénoalcane secondaire représenté en 3D

**Réactifs et conditions.** Nucléophile, groupe partant et solvant compatibles

**Produit / bilan.** Produit substitué avec inversion géométrique

**Liaisons et fonctions modifiées**

- Formation C–Nu et rupture C–X simultanées.

**Règles et sélectivité**

- Attaque arrière ; obstruction des centres tertiaires.
- L’inversion géométrique ne signifie R→S qu’après un nouveau classement CIP.

**Caractérisation du produit**

- Conserver les trois autres substituants, suivre leur disposition puis attribuer la configuration du produit.

**Étapes à reconstruire**

1. Nu attaque selon l’axe opposé à C–X.
2. État de transition à deux liaisons partielles.
3. Produit inversé et X⁻.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `sn2` et son scénario. Paramètres : `substrate=secondary, stage=2`.

**Question.** Pourquoi l’état de transition n’est-il pas un intermédiaire à isoler ?

**Réponse.** Il est le sommet du chemin réactionnel, avec liaisons partielles. Le mécanisme SN2 est concerté et n’a pas un minimum d’énergie carbocationique entre attaque et départ.

### Fiche 14 — SEA : addition au cycle puis retour de l’aromaticité

**Famille :** SEA · **Niveau :** Sup → PC · **Identifiant :** `sea_nitration`

**Substrat.** Benzène ou aromatique substitué

**Réactifs et conditions.** HNO₃ / H₂SO₄ : génération de NO₂⁺

**Produit / bilan.** Nitroaromatique

**Liaisons et fonctions modifiées**

- Une liaison Ar–H est remplacée par Ar–NO₂ ; l’aromaticité est provisoirement rompue.

**Règles et sélectivité**

- Complexe σ de Wheland ; orientation par les groupes déjà présents.
- La réaromatisation favorise le départ de H⁺ plutôt qu’une simple addition stable.

**Caractérisation du produit**

- Le produit est toujours aromatique ; substitution et addition ne possèdent pas le même bilan de H.

**Étapes à reconstruire**

1. Former l’électrophile.
2. Attaque des électrons π et complexe σ.
3. Prélèvement de H et reconstitution du système aromatique.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aromatique` et son scénario. Paramètres : `substituent=h, reaction=nitration, stage=2`.

**Question.** Quel acte restaure l’aromaticité ?

**Réponse.** La base reprend le proton du carbone qui a capturé E ; les électrons C–H reforment une liaison π dans le cycle.

### Fiche 15 — SEA réversible : sulfonation aromatique

**Famille :** SEA · **Niveau :** Sup → PC · **Identifiant :** `sea_sulfonation`

**Substrat.** Benzène

**Réactifs et conditions.** SO₃ / H₂SO₄ ; conditions d’équilibre

**Produit / bilan.** Acide benzènesulfonique ; désulfonation sous conditions aqueuses chaudes

**Liaisons et fonctions modifiées**

- Ar–H devient Ar–SO₃H ; le noyau conserve six carbones.

**Règles et sélectivité**

- La réversibilité permet d’utiliser SO₃H comme groupe temporaire ; conditions et orientation doivent être précisées.

**Caractérisation du produit**

- Fonction acide sulfonique fortement polaire ; substitution du cycle sans gain de carbone.

**Étapes à reconstruire**

1. Activation de l’électrophile soufré.
2. Formation du complexe σ.
3. Déprotonation et équilibre dépendant du milieu.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aromatique` et son scénario. Paramètres : `substituent=h, reaction=sulfonation, stage=2`.

**Domaine du modèle.** Les barrières du laboratoire sont choisies ; elles ne prédisent pas un rendement réel ni la position d’équilibre.

**Question.** Pourquoi cette réaction est-elle utile comme blocage temporaire ?

**Réponse.** SO₃H peut occuper une position du cycle puis être retiré par désulfonation adaptée. Il faut suivre son effet directeur tant qu’il est présent, et non supprimer arbitrairement ce groupe du schéma.

## Page 526 — Autres exemples / organomagnésiens

### Fiche 16 — C-alkylation : l’énolate est un nucléophile ambident

**Famille :** SN2 / énolate · **Niveau :** Sup → PC · **Identifiant :** `enolate_c`

**Substrat.** Énolate de propanone ou de malonate

**Réactifs et conditions.** Halogénoalcane primaire ; énolate formé préalablement

**Produit / bilan.** Carbonyle alkylé en α

**Liaisons et fonctions modifiées**

- Création Cα–C(alkyle) ; départ X⁻ ; conservation du carbonyle dans la C-alkylation.

**Règles et sélectivité**

- Électrophile primaire favorable à SN2 ; tertiaire propice à élimination.
- C- et O-alkylation sont deux connectivités distinctes.

**Caractérisation du produit**

- Repérer le nouveau nombre de carbones et la fonction C=O ; un éther d’énol n’est pas la même structure.

**Étapes à reconstruire**

1. Déprotonation en α.
2. Délocalisation de l’énolate.
3. Attaque de Cα sur R–X et départ X⁻.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `enolatealkyl` et son scénario. Paramètres : `donor=acetone, electrophile=ethyl, site=C, stage=2`.

**Question.** Un électrophile tertiaire convient-il pour la même SN2 ?

**Réponse.** La SN2 est fortement entravée ; la basicité de l’énolate permet une élimination concurrente. On choisit un autre partenaire ou une autre stratégie pour obtenir la liaison C–C.

### Fiche 17 — Époxydation : conserver la relation E/Z dans un petit cycle

**Famille :** Addition concertée · **Niveau :** Sup → PC · **Identifiant :** `epoxy_peracide`

**Substrat.** (E)- ou (Z)-but-2-ène

**Réactifs et conditions.** Peracide RCO₃H

**Produit / bilan.** Époxyde et acide carboxylique RCO₂H

**Liaisons et fonctions modifiées**

- C=C devient C–C ; deux liaisons C–O se forment avec un seul O transféré.

**Règles et sélectivité**

- Le transfert concerté conserve la relation relative des substituants.
- Dans un milieu achiral, les faces équivalentes peuvent donner une paire d’énantiomères.

**Caractérisation du produit**

- Reconnaître le cycle C–C–O à trois atomes, sans groupe OH dans l’époxyde isolé.

**Étapes à reconstruire**

1. Approche du peracide sur une face.
2. Réorganisation concertée des liaisons.
3. Séparation époxyde / acide.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `epoxydes` et son scénario. Paramètres : `substrate=butene_E, mode=peracid, stage=3`.

**Question.** Combien d’atomes O du peracide sont transférés à l’alcène ?

**Réponse.** Un seul atome O forme le pont époxyde. Le reste du réactif donne l’acide carboxylique ; le bilan doit compter séparément ces deux produits.

### Fiche 18 — Estérification de Fischer : condensation catalysée par H⁺

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `fischer`

**Substrat.** Acide éthanoïque et éthanol

**Réactifs et conditions.** Catalyse acide ; gestion de l’eau et de l’excès d’alcool

**Produit / bilan.** Éthanoate d’éthyle et H₂O

**Liaisons et fonctions modifiées**

- Le groupe OH acyle est remplacé par OEt au bilan ; le carbonyle reste présent.

**Règles et sélectivité**

- Réaction réversible ; catalyse accélère les deux sens sans changer K.
- Un excès ou retrait d’eau déplace l’équilibre.

**Caractérisation du produit**

- Ester : C=O et C–O ; identifier O–CH₂–CH₃ sans confondre avec un simple mélange des réactifs.

**Étapes à reconstruire**

1. Protonation du carbonyle.
2. Addition de l’alcool et transferts de H⁺.
3. Départ d’eau puis régénération de H⁺.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `esterification` et son scénario. Paramètres : `mode=ester, first=1, second=1, water=0, K=4`.

**Question.** Pourquoi chauffer avec un catalyseur ne suffit-il pas à garantir 100 % de conversion ?

**Réponse.** La vitesse et la position d’équilibre sont distinctes. Pour K=4 et stocks équimolaires sans eau ni ester initiaux, l’avancement relatif est 2/3 ; modifier les stocks ou enlever l’eau agit sur l’équilibre.

### Fiche 19 — Ester par chlorure d’acyle : départ activé

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `ester_chlorure`

**Substrat.** Chlorure de benzoyle et éthanol

**Réactifs et conditions.** Alcool ; base piège à HCl possible dans un protocole

**Produit / bilan.** Benzoate d’éthyle et HCl dans le bilan du laboratoire

**Liaisons et fonctions modifiées**

- C(acyle)–Cl remplacée par C(acyle)–OEt ; conservation du squelette aromatique.

**Règles et sélectivité**

- Chlorure d’acyle plus réactif qu’un acide non activé ; l’eau est un nucléophile concurrent.

**Caractérisation du produit**

- Nouvelle fonction ester, disparition du chlorure d’acyle ; vérifier quel O provient de l’alcool.

**Étapes à reconstruire**

1. Attaque du doublet O sur C=O.
2. Intermédiaire tétraédrique.
3. Départ Cl⁻ et déprotonation.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `anhydride` et son scénario. Paramètres : `variant=chloridealcohol, acyl=benzoyl, equivalents=1, stage=2`.

**Domaine du modèle.** Une base externe peut neutraliser HCl dans un protocole ; elle n’est pas comptée comme réactif dans ce scénario. L’eau est une voie concurrente.

**Question.** Quelle précaution chimique impose le chlorure d’acyle ?

**Réponse.** Il faut contrôler l’eau et prévoir une base pour neutraliser l’acide produit ; l’hydrolyse concurrente consomme le dérivé activé.

### Fiche 20 — Hydrolyse d’ester en milieu acide : inverser Fischer

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `hydrolyse_acide`

**Substrat.** Éthanoate d’éthyle et eau

**Réactifs et conditions.** H⁺ catalytique ; eau en excès

**Produit / bilan.** Acide éthanoïque et éthanol

**Liaisons et fonctions modifiées**

- La liaison C(acyle)–OEt est remplacée par C(acyle)–OH.

**Règles et sélectivité**

- Équilibre réversible ; après traitement, la forme protonée dépend du pH.

**Caractérisation du produit**

- Retour de la fonction acide et de l’alcool ; bilan eau/ester/acide/alcool.

**Étapes à reconstruire**

1. Activation du carbonyle par H⁺.
2. Addition de H₂O.
3. Transferts de protons et départ de l’alcool.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `hydrolyseacyle` et son scénario. Paramètres : `derivative=ester, medium=acid, equivalents=1, stage=3`.

**Question.** L’eau est-elle seulement un solvant ?

**Réponse.** Elle est aussi un réactif nucléophile du bilan. Son activité élevée peut favoriser l’hydrolyse ; une stœchiométrie écrite sans H₂O ne permettrait pas de suivre cette dépendance.

### Fiche 21 — Saponification : piéger l’acide en carboxylate

**Famille :** AE-addition-élimination / AB · **Niveau :** Sup → PC · **Identifiant :** `saponification`

**Substrat.** Éthanoate d’éthyle

**Réactifs et conditions.** HO⁻ aqueux

**Produit / bilan.** Éthanoate et éthanol ; acide après acidification séparée

**Liaisons et fonctions modifiées**

- Remplacement OEt par O⁻ au bilan ; consommation nette de HO⁻.

**Règles et sélectivité**

- Le transfert de proton final stabilise le carboxylate et rend le bilan favorable.
- HO⁻ est réactif stœchiométrique dans ce bilan.

**Caractérisation du produit**

- Distinguer RCO₂⁻ dans le milieu basique et RCO₂H après traitement acide.

**Étapes à reconstruire**

1. Attaque HO⁻ sur C=O.
2. Retour du carbonyle et départ de l’alcoolate.
3. Transfert de proton donnant carboxylate et alcool.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `esterification` et son scénario. Paramètres : `mode=saponification, first=1, second=1`.

**Question.** Quel produit doit-on dessiner avant l’acidification ?

**Réponse.** Le carboxylate RCO₂⁻, associé au contre-ion. Dessiner directement l’acide neutre omet le transfert de proton responsable du piégeage basique.

### Fiche 22 — Amide : une amine attaque un chlorure d’acyle

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `amide_chlorure`

**Substrat.** Chlorure d’éthanoyle et amine

**Réactifs et conditions.** Deux équivalents d’amine, ou un équivalent plus une base

**Produit / bilan.** Amide et ammonium chlorure

**Liaisons et fonctions modifiées**

- Création C(acyle)–N ; départ Cl⁻ ; perte d’un H de l’amine attaquante.

**Règles et sélectivité**

- L’amide n’est pas un sel ammonium ; le second équivalent d’amine peut piéger HCl.

**Caractérisation du produit**

- C=O adjacent à N ; caractère partiellement double C–N par conjugaison ; azote moins basique qu’une amine.

**Étapes à reconstruire**

1. Addition nucléophile de N.
2. Élimination du chlorure.
3. Déprotonation par une autre base.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `acylation` et son scénario. Paramètres : `activation=chloride, amine=2, base=0, stage=3`.

**Question.** Pourquoi acide carboxylique + amine à froid n’est-il pas la même voie ?

**Réponse.** Le transfert acido-basique donne souvent un sel ammonium carboxylate. La formation efficace de l’amide demande activation ou conditions de condensation spécifiques.

### Fiche 23 — Anhydride d’acide : unir deux groupes acyle

**Famille :** AE-addition-élimination · **Niveau :** Sup → PC · **Identifiant :** `anhydride_formation`

**Substrat.** Chlorure d’éthanoyle et ion éthanoate

**Réactifs et conditions.** Carboxylate nucléophile ; milieu maîtrisé

**Produit / bilan.** Anhydride éthanoïque et Cl⁻

**Liaisons et fonctions modifiées**

- Création C(acyle)–O(carboxylate) ; départ Cl⁻ ; deux carbonyles conservés.

**Règles et sélectivité**

- Deux groupes acyle différents pourraient donner un anhydride mixte ; le modèle ici est symétrique.

**Caractérisation du produit**

- Identifier le motif R–CO–O–CO–R ; ne pas le confondre avec un peroxyde O–O.

**Étapes à reconstruire**

1. Attaque de l’oxygène carboxylate sur le chlorure d’acyle.
2. Intermédiaire tétraédrique.
3. Retour C=O et départ Cl⁻.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `anhydride` et son scénario. Paramètres : `variant=formation, acyl=acetyl, stage=2`.

**Question.** Le pont de l’anhydride comporte-t-il une liaison O–O ?

**Réponse.** Non : un seul O est lié aux deux carbones carbonylés. R–C(=O)–O–C(=O)–R est un anhydride ; le peracide possède une liaison O–O.

### Fiche 24 — Hémiacétal : première addition d’un alcool

**Famille :** AN / AB · **Niveau :** Sup → PC · **Identifiant :** `hemiacetal`

**Substrat.** Éthanal et éthanol

**Réactifs et conditions.** Catalyse acide ; composition contrôlée

**Produit / bilan.** Hémiacétal CH₃–CH(OH)–OEt

**Liaisons et fonctions modifiées**

- C=O devient C(OH)(OR) ; une liaison C–O(alcool) s’ajoute.

**Règles et sélectivité**

- Équilibre ; un hémiacétal contient un OH et un OR sur le même carbone.

**Caractérisation du produit**

- Carbone anciennement carbonylé désormais tétraédrique ; aucun deuxième OR à ce stade.

**Étapes à reconstruire**

1. Activation du carbonyle.
2. Addition de ROH.
3. Déprotonation de l’oxonium.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `carbonyle` et son scénario. Paramètres : `reaction=acetal, stage=1`.

**Question.** Quel motif distingue hémiacétal et acétal ?

**Réponse.** L’hémiacétal porte OH et OR sur le même C ; l’acétal porte deux OR et n’y conserve pas de OH.

### Fiche 25 — Acétal : protection réversible d’un carbonyle

**Famille :** AE-addition-élimination / AB · **Niveau :** Sup → PC · **Identifiant :** `acetal`

**Substrat.** Éthanal et éthanol, ou carbonyle et diol

**Réactifs et conditions.** H⁺ ; excès alcool ou élimination d’eau

**Produit / bilan.** 1,1-Diéthoxyéthane ; avec diol, acétal cyclique

**Liaisons et fonctions modifiées**

- Remplacement net de l’O carbonylé par deux groupes OR ; formation d’eau.

**Règles et sélectivité**

- Stable dans de nombreux milieux basiques ; hydrolysable en milieu acide aqueux.
- Protéger avant une opération incompatible, déprotéger après.

**Caractérisation du produit**

- Absence de C=O protégé ; présence du carbone C(OR)₂ ; vérifier la taille réelle d’un cycle si un diol est utilisé.

**Étapes à reconstruire**

1. Formation de l’hémiacétal.
2. Protonation OH puis perte d’eau.
3. Capture par un second alcool et déprotonation.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `carbonyle` et son scénario. Paramètres : `reaction=acetal, stage=4, water=0.05`.

**Question.** Retirer l’eau et ajouter H⁺ ont-ils le même rôle ?

**Réponse.** Non : H⁺ catalyse le chemin tandis que le retrait d’un produit modifie le quotient réactionnel et déplace l’équilibre vers l’acétal.

### Fiche 26 — Photohalogénation : addition sur le benzène

**Famille :** Radicalaire / addition · **Niveau :** Sup → PC · **Identifiant :** `benzene_photo`

**Substrat.** Benzène

**Réactifs et conditions.** 3 Cl₂ sous irradiation hν

**Produit / bilan.** Hexachlorocyclohexane : C₆H₆Cl₆, mélange stéréochimique possible

**Liaisons et fonctions modifiées**

- Les trois liaisons π du cycle sont consommées ; six liaisons C–Cl se forment ; les six H restent.

**Règles et sélectivité**

- Conditions photoradicalaires distinctes de Cl₂ / acide de Lewis.
- Le bilan ne sélectionne pas à lui seul un unique isomère du cyclohexane chloré.

**Caractérisation du produit**

- C₆H₆Cl₆ saturé et non aromatique, à distinguer de C₆H₅Cl aromatique issu d’une SEA.

**Étapes à reconstruire**

1. Génération d’espèces radicalaires par la lumière.
2. Additions sur le système π.
3. Bilan de trois Cl₂ pour saturer les trois π.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `photochlore` et son scénario. Paramètres : `mode=addition, chlorine=3, light=on, stage=2`.

**Question.** Quel simple bilan distingue cette transformation de la chloration aromatique ?

**Réponse.** En addition photochimique six Cl sont ajoutés et aucun H n’est remplacé. En SEA un H est remplacé par Cl, l’aromaticité est conservée et HCl est produit.

### Fiche 27 — Alkylation d’amine : former un ammonium quaternaire

**Famille :** SN2 · **Niveau :** Sup → PC · **Identifiant :** `amine_alkyl`

**Substrat.** Triméthylamine ou triéthylamine

**Réactifs et conditions.** Halogénoalcane primaire, par exemple CH₃X

**Produit / bilan.** Sel tétraalkylammonium \[R₃N–CH₃\]⁺ X⁻

**Liaisons et fonctions modifiées**

- Le doublet de N forme C–N ; C–X se rompt ; N porte quatre liaisons et +1.

**Règles et sélectivité**

- Une amine tertiaire ne possède pas de N–H à déprotoner après alkylation.
- Amine et ammonium quaternaire n’ont pas la même basicité ni le même doublet disponible.

**Caractérisation du produit**

- Compter quatre groupes carbonés autour de N et un contre-ion X⁻ ; aucune libération de H⁺ nécessaire.

**Étapes à reconstruire**

1. Attaque arrière de N sur C–X.
2. Départ de X⁻.
3. Formation du sel ionique.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aminealkyl` et son scénario. Paramètres : `amine=trimethyl, electrophile=methyl, stage=2`.

**Question.** Pourquoi N garde-t-il une charge positive ?

**Réponse.** Le N quaternaire possède quatre liaisons et aucun doublet libre. Sans H porté par N, une déprotonation de N ne peut pas rendre une amine tertiaire.

### Fiche 28 — Préparer RMgX : ordre d’introduction et absence de protons

**Famille :** Insertion / OR · **Niveau :** Sup → PC · **Identifiant :** `grignard_prepare`

**Substrat.** Bromoéthane ou bromobenzène

**Réactifs et conditions.** Mg ; solvant éthéré anhydre ; ajout contrôlé RX

**Produit / bilan.** EtMgBr ou PhMgBr

**Liaisons et fonctions modifiées**

- Remplacement du bilan C–Br par C–Mg–Br ; activation du métal.

**Règles et sélectivité**

- L’eau ou un proton acide consomme RMgX en donnant RH.
- L’éther coordonne Mg ; hydrolyse uniquement lors du traitement final après la réaction recherchée.

**Caractérisation du produit**

- Vérifier les équivalents disponibles plutôt que supposer un organomagnésien intact dans un milieu humide.

**Étapes à reconstruire**

1. Amorcer le contact Mg / RX.
2. Former l’organomagnésien en milieu sec.
3. Éviter eau et fonctions protiques pendant son utilisation.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `grignardprep` et son scénario. Paramètres : `group=ethyl, halide=Br, water=0, progress=1, stage=2`.

**Question.** Pourquoi une hydrolyse avant l’addition détruit-elle le projet ?

**Réponse.** RMgX est une base forte : son carbone prélève H et donne RH. Il ne reste alors plus le nucléophile carboné requis pour construire C–C.

### Fiche 29 — RMgX + méthanal : allonger d’un carbone

**Famille :** AN / AB · **Niveau :** Sup → PC · **Identifiant :** `grignard_methanal`

**Substrat.** Méthanal

**Réactifs et conditions.** EtMgBr puis hydrolyse séparée

**Produit / bilan.** Propan-1-ol

**Liaisons et fonctions modifiées**

- Création Et–CH₂ ; C=O devient C–OH après hydrolyse.

**Règles et sélectivité**

- Le méthanal donne un alcool primaire, car son C fonctionnel ne porte pas de groupe carboné avant l’addition.

**Caractérisation du produit**

- Trois C au total ; carbone portant OH lié à un seul C.

**Étapes à reconstruire**

1. Et attaque C=O ; π → O.
2. Alcoolate magnésien.
3. Protonation lors du traitement.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `grignard` et son scénario. Paramètres : `substrate=methanal, alkyl=ethyl, equivalents=1, water=0, stage=2`.

**Question.** De quel partenaire vient le carbone portant OH ?

**Réponse.** Du méthanal. L’éthyle devient son substituant carboné, ce qui allonge la chaîne d’un carbone par rapport à EtMgBr.

### Fiche 30 — RMgX + aldéhyde : alcool secondaire

**Famille :** AN / AB · **Niveau :** Sup → PC · **Identifiant :** `grignard_aldehyde`

**Substrat.** Éthanal

**Réactifs et conditions.** PhMgBr puis hydrolyse

**Produit / bilan.** 1-Phényléthanol

**Liaisons et fonctions modifiées**

- Formation C(carbonyle)–Ph ; création d’un carbone tétraédrique portant OH.

**Règles et sélectivité**

- Deux faces du carbonyle plan ; milieu achiral donnant le mélange racémique dans ce cas.

**Caractérisation du produit**

- Alcool secondaire, groupe CH₃ et Ph sur le C–OH ; vérifier R/S après représentation 3D.

**Étapes à reconstruire**

1. Addition nucléophile.
2. Alcoolate magnésien.
3. Hydrolyse finale.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `grignard` et son scénario. Paramètres : `substrate=aldehyde, alkyl=phenyl, equivalents=1, stage=2`.

**Question.** Pourquoi un centre chiral apparaît-il ici ?

**Réponse.** Le carbone fonctionnel porte OH, H, CH₃ et Ph : quatre groupes différents. Les deux faces planes donnent les deux configurations en milieu achiral.

### Fiche 31 — RMgX + cétone : alcool tertiaire

**Famille :** AN / AB · **Niveau :** Sup → PC · **Identifiant :** `grignard_cetone`

**Substrat.** Propanone

**Réactifs et conditions.** EtMgBr puis hydrolyse

**Produit / bilan.** 2-Méthylbutan-2-ol

**Liaisons et fonctions modifiées**

- Le C carbonylé reçoit un troisième substituant carboné ; C=O devient C–OH.

**Règles et sélectivité**

- Alcool tertiaire ; absence de centre chiral ici, car les deux CH₃ sont identiques.

**Caractérisation du produit**

- C–OH lié à trois C ; compter cinq C au produit et contrôler la valence.

**Étapes à reconstruire**

1. Transfert Et vers C=O.
2. Alcoolate.
3. Protonation de O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `grignard` et son scénario. Paramètres : `substrate=ketone, alkyl=ethyl, equivalents=1, stage=2`.

**Question.** Toute addition à une cétone crée-t-elle de la chiralité ?

**Réponse.** Non : elle donne un alcool tertiaire mais un centre chiral exige quatre groupes différents. Ici les deux méthyles rendent le centre achiral.

### Fiche 32 — RMgX + CO₂ : carboxylation

**Famille :** AN / AB · **Niveau :** Sup → PC · **Identifiant :** `grignard_co2`

**Substrat.** Dioxyde de carbone

**Réactifs et conditions.** PhMgBr puis traitement acide

**Produit / bilan.** Acide benzoïque

**Liaisons et fonctions modifiées**

- Création Ph–C(CO₂) ; un C est ajouté au squelette ; carboxylate avant traitement.

**Règles et sélectivité**

- Le carbone de CO₂ devient celui du groupe carboxylique.

**Caractérisation du produit**

- RCO₂⁻ avant acidification, RCO₂H après ; formule C₇H₆O₂ pour l’acide benzoïque.

**Étapes à reconstruire**

1. Attaque du carbone nucléophile sur CO₂.
2. Carboxylate magnésien.
3. Acidification séparée.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `grignard` et son scénario. Paramètres : `substrate=co2, alkyl=phenyl, equivalents=1, stage=2`.

**Question.** L’hydrolyse donne-t-elle un alcool dans ce cas ?

**Réponse.** Non. L’intermédiaire est un carboxylate : le traitement protonne cette fonction et livre un acide carboxylique.

## Page 527 — Exemples (suite)

### Fiche 33 — Hydrogénation : saturation et addition syn

**Famille :** Addition / OR · **Niveau :** Sup → PC · **Identifiant :** `hydrogenation`

**Substrat.** (E)- ou (Z)-but-2-ène

**Réactifs et conditions.** H₂ / catalyseur métallique adapté

**Produit / bilan.** Butane

**Liaisons et fonctions modifiées**

- C=C devient C–C ; un H est livré à chacun des deux carbones.

**Règles et sélectivité**

- Addition sur une même face dans le modèle de surface ; adsorption et désorption expliquent le bilan syn.

**Caractérisation du produit**

- Disparition de l’insaturation ; E/Z n’existe plus dans le butane.

**Étapes à reconstruire**

1. Adsorption du substrat et activation de H₂.
2. Transfert des H sur la même face dans le modèle.
3. Désorption du produit.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=butene_Z, reagent=hydrogen, stage=2`.

**Question.** Le butane garde-t-il l’étiquette Z de son précurseur ?

**Réponse.** Non : E/Z est une configuration d’une double liaison. La rotation autour de la nouvelle liaison simple produit des conformères du même butane.

### Fiche 34 — Hydroboration–oxydation : alcool anti-Markovnikov

**Famille :** Addition concertée / OR · **Niveau :** Sup → PC · **Identifiant :** `hydroboration`

**Substrat.** Propène

**Réactifs et conditions.** 1. BH₃ ; 2. H₂O₂ / HO⁻

**Produit / bilan.** Propan-1-ol

**Liaisons et fonctions modifiées**

- Première étape : création C–B et C–H ; deuxième : remplacement C–B par C–O avec rétention.

**Règles et sélectivité**

- B se fixe préférentiellement sur le C le moins encombré ; H et B s’ajoutent syn.
- Après oxydation, H et OH gardent cette relation relative ; pas de carbocation libre.

**Caractérisation du produit**

- Alcool primaire au lieu du secondaire de l’hydratation acide du propène.

**Étapes à reconstruire**

1. Addition concertée H–B.
2. Oxydation du groupe organoboré.
3. Traitement donnant l’alcool.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=propene, reagent=borane, stage=2`.

**Question.** OH est-il transféré depuis BH₃ lors de la première étape ?

**Réponse.** Non : la première étape fixe H et B. La fonction OH apparaît pendant l’oxydation et le traitement suivants ; séparer les étapes explique l’orientation et la stéréochimie.

### Fiche 35 — Friedel–Crafts : alkylation aromatique

**Famille :** SEA · **Niveau :** Sup → PC · **Identifiant :** `fc_alkyl`

**Substrat.** Benzène

**Réactifs et conditions.** Halogénoalcane / acide de Lewis dans un cas compatible

**Produit / bilan.** Alkylbenzène et HX

**Liaisons et fonctions modifiées**

- Ar–H devient Ar–R ; une liaison C–C se forme.

**Règles et sélectivité**

- Réarrangements possibles selon l’électrophile ; produit alkylé souvent plus réactif, donc polyalkylation possible.
- Un noyau fortement désactivé par NO₂ ne convient pas à la voie usuelle.

**Caractérisation du produit**

- Un alkyle remplace un H du cycle ; aromaticité finale conservée.

**Étapes à reconstruire**

1. Activation du dérivé halogéné.
2. Attaque du cycle et complexe σ.
3. Déprotonation et restauration de l’aromaticité.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aromatique` et son scénario. Paramètres : `substituent=h, reaction=alkylation, stage=2`.

**Question.** Pourquoi une simple règle ortho/para ne prédit-elle pas une synthèse complète ?

**Réponse.** Il faut aussi vérifier la possibilité de la réaction, les migrations du groupe alkyle et la réactivité accrue du produit. Orientation, conversion et monoalkylation sont des questions distinctes.

### Fiche 36 — Friedel–Crafts : acylation pour contrôler le squelette

**Famille :** SEA · **Niveau :** Sup → PC · **Identifiant :** `fc_acyl`

**Substrat.** Benzène

**Réactifs et conditions.** Chlorure d’éthanoyle / AlCl₃ puis traitement

**Produit / bilan.** Acétophénone

**Liaisons et fonctions modifiées**

- Création Ar–C(=O)CH₃ ; remplacement d’un H aromatique.

**Règles et sélectivité**

- Ion acylium stabilisé ; pas de migration de squelette de type carbocation alkyle.
- COCH₃ désactive le cycle et oriente une nitration suivante vers méta.

**Caractérisation du produit**

- Cétone aromatique conjuguée ; le carbonyle fait partie du groupe ajouté.

**Étapes à reconstruire**

1. Formation d’un électrophile acyle.
2. Complexe σ.
3. Réaromatisation puis libération du carbonyle complexé au traitement.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aromatique` et son scénario. Paramètres : `substituent=h, reaction=acylation, stage=2`.

**Question.** Quel ordre permet d’obtenir une nitroacétophénone méta par cette stratégie ?

**Réponse.** Acyler d’abord un noyau compatible, puis nitrer : COCH₃ dirige vers méta. Nitrer d’abord donne un noyau trop désactivé pour la Friedel–Crafts usuelle.

### Fiche 37 — Aldolisation croisée : donner et recevoir ne sont pas symétriques

**Famille :** AN / énolate · **Niveau :** Sup → PC · **Identifiant :** `aldol_croisee`

**Substrat.** Acétophénone et benzaldéhyde

**Réactifs et conditions.** Base ; conditions adaptées à l’addition

**Produit / bilan.** β-Hydroxycétone PhCO–CH₂–CH(OH)–Ph

**Liaisons et fonctions modifiées**

- Création Cα(donneur)–C(carbonyle accepteur) ; C=O de l’accepteur devient alcool.

**Règles et sélectivité**

- Le benzaldéhyde n’a pas de Hα et sert d’accepteur.
- Deux partenaires énolisables non dirigés peuvent multiplier les produits.

**Caractérisation du produit**

- Produit possédant à la fois C=O et OH en β ; compter les deux noyaux Ph.

**Étapes à reconstruire**

1. Formation de l’énolate de l’acétophénone.
2. Attaque du Cα sur le benzaldéhyde.
3. Protonation de l’alcoolate.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aldol` et son scénario. Paramètres : `donor=acetophenone, acceptor=benzaldehyde, mode=aldol, stage=3`.

**Question.** Quel carbonyle est conservé ?

**Réponse.** Celui du donneur acétophénone. Le carbonyle du benzaldéhyde reçoit l’attaque et devient le groupe OH de la β-hydroxycétone.

## Page 528 — Exemples (suite)

### Fiche 38 — Crotonisation : construire l’énone conjuguée

**Famille :** E / E1cb · **Niveau :** Sup → PC · **Identifiant :** `crotonisation`

**Substrat.** β-Hydroxycétone issue de l’aldolisation acétophénone/benzaldéhyde

**Réactifs et conditions.** Conditions déshydratantes adaptées, souvent base et chauffage

**Produit / bilan.** Chalcone PhCO–CH=CH–Ph et eau au bilan

**Liaisons et fonctions modifiées**

- Perte de Hα et OHβ au bilan ; nouvelle Cα=Cβ conjuguée à C=O.

**Règles et sélectivité**

- La conjugaison stabilise l’énone ; E souvent favorisé dans ce cas mais les conditions sont requises.
- En base, E1cb est une description utile quand l’énolate précède le départ d’un mauvais groupe partant.

**Caractérisation du produit**

- OH disparaît ; deux carbones vinyliques apparaissent ; C=O reste présent.

**Étapes à reconstruire**

1. Déprotonation en α.
2. Énolate / base conjuguée stabilisée.
3. Élimination formant la conjugaison ; bilan net H₂O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aldol` et son scénario. Paramètres : `donor=acetophenone, acceptor=benzaldehyde, mode=condensation, stage=3`.

**Question.** Pourquoi la crotonisation n’est-elle pas une nouvelle aldolisation ?

**Réponse.** L’aldolisation crée la liaison C–C par addition ; la crotonisation convertit le β-hydroxycarbonyle déjà formé en carbonyle α,β-insaturé par élimination.

### Fiche 39 — Amide via anhydride : choisir le départ et piéger l’acide

**Famille :** AE-addition-élimination / AB · **Niveau :** Sup → PC · **Identifiant :** `amide_anhydride`

**Substrat.** Anhydride éthanoïque et amine

**Réactifs et conditions.** Amine nucléophile ; autre base ou second équivalent

**Produit / bilan.** Amide et carboxylate d’ammonium selon le traitement

**Liaisons et fonctions modifiées**

- Une moitié acyle devient amide ; l’autre fournit un carboxylate / acide.

**Règles et sélectivité**

- Ne pas compter deux amides pour un anhydride dans ce simple bilan d’acylation.
- La basicité des espèces détermine la forme acide ou salifiée en fin de réaction.

**Caractérisation du produit**

- Un C=O adjacent à N dans l’amide et un carboxylate distinct ; N peut garder un H selon l’amine.

**Étapes à reconstruire**

1. Addition de l’amine au carbone acyle.
2. Élimination du carboxylate.
3. Transferts de protons vers la base disponible.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `acylation` et son scénario. Paramètres : `activation=anhydride, amine=2, base=0, stage=3`.

**Question.** Quel fragment de l’anhydride devient le groupe partant ?

**Réponse.** Le carboxylate de l’autre moitié acyle. Sa structure stabilisée rend cette addition–élimination possible ; ce fragment ne reste pas lié au N du produit.

### Fiche 40 — Michael : l’attaque conjuguée construit une liaison en β

**Famille :** AN conjuguée · **Niveau :** Sup → PC · **Identifiant :** `michael`

**Substrat.** Énolate stabilisé de malonate et but-3-én-2-one

**Réactifs et conditions.** Base puis traitement protonant

**Produit / bilan.** Adduit portant le motif carbonyle et une nouvelle liaison C–C en β

**Liaisons et fonctions modifiées**

- Création C(donneur)–Cβ(accepteur) ; Cα=Cβ est consommée ; le carbonyle de l’accepteur revient après protonation.

**Règles et sélectivité**

- Nucléophile stabilisé favorable à 1,4 dans ce cas.
- Un Grignard dur donne souvent une attaque 1,2 ; un organocuprate favorise fréquemment 1,4.

**Caractérisation du produit**

- Adduit 1,4 : C=O présent et double liaison conjuguée consommée ; adduit 1,2 : alcool et C=C conservée.

**Étapes à reconstruire**

1. Attaque du C nucléophile sur Cβ.
2. Délocalisation vers l’énolate de l’accepteur.
3. Protonation et retour du carbonyle.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `michaelwittig` et son scénario. Paramètres : `reaction=michael, reagent=enolate, stage=3`.

**Question.** Comment distinguer les produits 1,2 et 1,4 sans retenir seulement leur nom ?

**Réponse.** On suit les liaisons : 1,2 transforme C=O en alcool tout en gardant C=C ; 1,4 consomme C=C et conserve le carbonyle après traitement.

### Fiche 41 — Wittig : remplacer C=O par C=C

**Famille :** Oléfination / AN · **Niveau :** Sup → PC · **Identifiant :** `wittig`

**Substrat.** Benzaldéhyde et ylure de phosphore

**Réactifs et conditions.** Ylure choisi puis traitement

**Produit / bilan.** Alcène et oxyde de triphénylphosphine

**Liaisons et fonctions modifiées**

- Le C du carbonyle se lie au C de l’ylure ; O quitte le substrat pour former Ph₃P=O.

**Règles et sélectivité**

- Stabilisation de l’ylure et conditions influencent E/Z ; aucune règle absolue indépendante du réactif.

**Caractérisation du produit**

- Le carbone carbonylé appartient désormais à C=C ; reconnaître l’oxyde de phosphine comme coproduit distinct.

**Étapes à reconstruire**

1. Attaque du carbone de l’ylure.
2. Formation d’un oxaphosphétane dans la description du modèle.
3. Fragmentation vers alcène et Ph₃P=O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `michaelwittig` et son scénario. Paramètres : `reaction=wittig, reagent=unstabilized, stage=3`.

**Question.** Où va l’oxygène du carbonyle ?

**Réponse.** Dans l’oxyde de phosphine. Le compter uniquement dans l’alcène ferait violer le bilan d’atomes : l’oléfination enlève la fonction oxygénée du substrat.

### Fiche 42 — Oxyde d’éthylène : époxydation catalytique ciblée

**Famille :** OR / catalyse · **Niveau :** Sup → PC · **Identifiant :** `epoxy_industriel`

**Substrat.** Éthylène

**Réactifs et conditions.** O₂ / argent dans le procédé catalytique adapté

**Produit / bilan.** Oxyde d’éthylène : C₂H₄O

**Liaisons et fonctions modifiées**

- Ajout d’un O en pont ; C=C devient C–C.

**Règles et sélectivité**

- Exemple industriel lié à l’éthylène ; ne pas généraliser O₂/Ag à tous les alcènes sans données.
- La sélectivité du catalyseur doit éviter l’oxydation totale.

**Caractérisation du produit**

- Cycle à trois atomes C–C–O ; bilan global 2 C₂H₄ + O₂ → 2 C₂H₄O.

**Étapes à reconstruire**

1. Activation catalytique de l’oxygène.
2. Transfert à l’alcène dans les conditions du procédé.
3. Séparation du produit.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `epoxydes` et son scénario. Paramètres : `substrate=ethylene, mode=silver, stage=3`.

**Domaine du modèle.** Procédé à l’argent réservé ici à l’éthylène ; sélectivité et mécanisme complet de surface non calculés.

**Question.** Pourquoi le bilan global ne fournit-il pas un mécanisme élémentaire ?

**Réponse.** Il garantit la conservation des atomes. Les espèces adsorbées, étapes de surface et sélectivité nécessitent un modèle catalytique supplémentaire.

### Fiche 43 — Époxyde : libérer la tension par une attaque nucléophile

**Famille :** SN2 / AN · **Niveau :** Sup → PC · **Identifiant :** `epoxy_ouverture`

**Substrat.** Oxyde d’éthylène

**Réactifs et conditions.** HO⁻ puis traitement protonant ; autre nucléophile selon le projet

**Produit / bilan.** Éthane-1,2-diol pour HO⁻ après protonation

**Liaisons et fonctions modifiées**

- Rupture d’une liaison C–O du cycle et formation C–Nu ; l’autre C–O devient OH.

**Règles et sélectivité**

- En milieu basique : attaque arrière sur le site le moins encombré.
- Les conditions acides ont une autre pondération électronique ; ne pas les confondre.

**Caractérisation du produit**

- Ouverture du cycle C–C–O ; suivre quel carbone porte Nu et lequel porte OH.

**Étapes à reconstruire**

1. Attaque arrière du nucléophile.
2. Rupture C–O et alcoolate.
3. Protonation au traitement.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `epoxydes` et son scénario. Paramètres : `substrate=ethylene, mode=basic, nucleophile=water, stage=3`.

**Question.** Pourquoi l’oxygène n’est-il pas éliminé de la molécule ?

**Réponse.** Une seule des deux liaisons C–O du cycle est rompue ; l’autre conserve O sur le squelette, sous forme alcoolate puis alcool.

## Page 531 — Alcènes et alcynes : applications

### Fiche 44 — Br₂ sur alcène E : bromonium puis ouverture anti

**Famille :** AE · **Niveau :** Sup → PC · **Identifiant :** `bromation_e`

**Substrat.** (E)-but-2-ène

**Réactifs et conditions.** Br₂ sans irradiation radicalaire

**Produit / bilan.** 2,3-Dibromobutane méso dans ce cas

**Liaisons et fonctions modifiées**

- C=C consommée ; deux C–Br formées.

**Règles et sélectivité**

- Intermédiaire ponté bromonium ; attaque de Br⁻ sur la face opposée.
- La relation anti est stéréospécifique et le substrat E mène ici au méso.

**Caractérisation du produit**

- Deux centres stéréogènes mais une structure achirale par symétrie ; ne pas compter systématiquement 2² isomères.

**Étapes à reconstruire**

1. Polarisation de Br₂ et formation du bromonium.
2. Ouverture anti par Br⁻.
3. Attribution des configurations et test de symétrie.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=butene_E, reagent=bromine, stage=2`.

**Question.** Deux centres stéréogènes garantissent-ils une molécule chirale ?

**Réponse.** Non. Le 2,3-dibromobutane méso possède une symétrie qui rend l’image miroir superposable malgré ses deux centres.

### Fiche 45 — Hydratation acide : AE puis capture nucléophile

**Famille :** AE / AN / AB · **Niveau :** Sup → PC · **Identifiant :** `hydratation_acide`

**Substrat.** Propène

**Réactifs et conditions.** H₂O / H⁺

**Produit / bilan.** Propan-2-ol et catalyseur régénéré

**Liaisons et fonctions modifiées**

- H et OH s’ajoutent au bilan ; H⁺ n’est pas consommé net.

**Règles et sélectivité**

- Orientation par carbocation ; réarrangements possibles sur des substrats adaptés.

**Caractérisation du produit**

- OH en C2 ; alcool secondaire ; distinguer le bilan global et les actes élémentaires.

**Étapes à reconstruire**

1. Protonation de C=C : acte électrophile.
2. Capture du carbocation par H₂O : acte nucléophile.
3. Déprotonation : acte acido-basique.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=propene, reagent=water, stage=2`.

**Question.** Une réaction globale peut-elle contenir plusieurs types d’actes élémentaires ?

**Réponse.** Oui. L’hydratation acide combine protonation électrophile, capture nucléophile et transfert de proton. Il faut annoncer l’échelle du classement choisi.

### Fiche 46 — E1 du recueil : deux positions β, deux connectivités

**Famille :** E1 · **Niveau :** Sup → PC · **Identifiant :** `e1_rearrangement`

**Substrat.** 2-Chloro-3-méthylbutane

**Réactifs et conditions.** Milieu permettant l’ionisation ; base disponible ; conditions précisées

**Produit / bilan.** 2-Méthylbut-2-ène et/ou 3-méthylbut-1-ène pour les deux branches représentées

**Liaisons et fonctions modifiées**

- Départ de Cl⁻ puis perte de H sur l’un des Cβ ; une liaison C=C se forme.

**Règles et sélectivité**

- Les deux positions β représentées n’aboutissent pas au même degré de substitution.
- Le branchement du modèle est imposé ; il ne déduit pas un pourcentage de la seule règle de Zaïtsev.
- Un carbocation peut se réarranger sous certaines conditions ; les migrations sont hors du modèle des deux éliminations directes représentées.

**Caractérisation du produit**

- Dessiner chaque alcène et recompter cinq C ; distinguer alcène interne et terminal.

**Étapes à reconstruire**

1. C–Cl → Cl⁻ et carbocation secondaire.
2. Choisir un Hβ sur chacun des deux sites.
3. La base capte H ; C–H forme la nouvelle liaison π.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `e1` et son scénario. Paramètres : `substrate=source, stage=3`.

**Question.** Quel élément du raisonnement permet de dessiner les deux produits ?

**Réponse.** L’énumération des sites β et de leurs H. La stabilité peut ensuite comparer les voies accessibles, mais ne remplace ni le dessin des liaisons ni des données de branchement pour un pourcentage.

### Fiche 47 — E2 du recueil : (3S,4S)/(3R,4R) vers E

**Famille :** E2 · **Niveau :** Sup → PC · **Identifiant :** `e2_source_e`

**Substrat.** 3-Bromo-3,4-diméthylhexane, paire (3S,4S)/(3R,4R)

**Réactifs et conditions.** Base ; H de C4 anti à Br

**Produit / bilan.** (E)-3,4-Diméthylhex-3-ène pour l’élimination C3–C4

**Liaisons et fonctions modifiées**

- Rupture C3–Br et C4–H ; formation C3=C4.

**Règles et sélectivité**

- Les deux réactifs énantiomères donnent le même alcène E achiral dans cette voie.
- D’autres Hβ permettent d’autres régioisomères : ils ne sont pas supprimés par l’étiquette E2.

**Caractérisation du produit**

- Sur chaque C vinylique Et est prioritaire sur CH₃ ; Et opposés donnent E.

**Étapes à reconstruire**

1. Construire Newman suivant C3–C4 sans changer R/S.
2. Placer H4 et Br anti par rotation.
3. Supprimer H et Br et attribuer E/Z du produit.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `e2stereo` et son scénario. Paramètres : `configuration=SS, dihedral=180, beta=c4`.

**Question.** Pourquoi SS et RR aboutissent-ils au même E ?

**Réponse.** Ils sont images miroir au départ. La double liaison plane du produit E de cette connectivité ne garde pas ces centres tétraédriques ; le miroir est superposable.

### Fiche 48 — Ozonolyse : couper pour reconstruire l’alcène initial

**Famille :** OR / coupure · **Niveau :** Sup → PC · **Identifiant :** `ozonolyse`

**Substrat.** But-2-ène E ou Z

**Réactifs et conditions.** 1. O₃ ; 2. traitement réducteur indiqué

**Produit / bilan.** Deux molécules d’éthanal

**Liaisons et fonctions modifiées**

- C=C coupée ; chacun des deux anciens carbones devient un carbone carbonylé.

**Règles et sélectivité**

- Le traitement final compte : réducteur et oxydant ne conduisent pas toujours aux mêmes fonctions.
- La coupure ne conserve pas une information E/Z dans les deux fragments éthanal.

**Caractérisation du produit**

- Chaque C de la double liaison portant H donne ici un aldéhyde ; sans H il donnerait une cétone.

**Étapes à reconstruire**

1. Réaction de l’ozone avec C=C.
2. Intermédiaires oxygénés.
3. Traitement et séparation des carbonyles.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=butene_E, reagent=ozone, stage=2`.

**Question.** Comment retrouver C=C à partir de deux fragments carbonylés ?

**Réponse.** Relier les deux carbones carbonylés par une double liaison après avoir retiré leurs O dans le raisonnement rétrosynthétique. Les substituants conservés reconstruisent la constitution, pas nécessairement E/Z.

### Fiche 49 — Alcyne + deux HX : halogénure vinylique puis geminal

**Famille :** AE · **Niveau :** Sup → PC · **Identifiant :** `alcyne_hcl`

**Substrat.** Propyne

**Réactifs et conditions.** 1 puis 2 équivalents HCl dans le cas du recueil

**Produit / bilan.** 2-Chloroprop-1-ène puis 2,2-dichloropropane

**Liaisons et fonctions modifiées**

- Une première π est consommée ; la seconde addition sature la liaison restante.
- Deux Cl finissent sur le même carbone : geminal.

**Règles et sélectivité**

- Distinguer 1 et 2 équivalents ; l’intermédiaire vinylique n’est pas encore un alcane.

**Caractérisation du produit**

- Après 1 HX : C=C présente ; après 2 HX : deux halogènes sur un seul C et absence de liaison multiple.

**Étapes à reconstruire**

1. Première addition HX sur C≡C.
2. Halogénoalcène.
3. Deuxième addition sur C=C.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcyne` et son scénario. Paramètres : `substrate=propyne, reagent=hcl2, stage=2`.

**Question.** Que signifie geminal, et pourquoi préciser les équivalents ?

**Réponse.** Geminal signifie deux halogènes sur le même carbone. Un équivalent livre ici le chlorure vinylique ; un second consomme la double liaison restante et livre le dichlorure saturé.

### Fiche 50 — Réduction partielle d’alcyne : sélectionner Z

**Famille :** OR / addition syn · **Niveau :** Sup → PC · **Identifiant :** `alcyne_lindlar`

**Substrat.** But-2-yne

**Réactifs et conditions.** H₂ / catalyseur de Lindlar

**Produit / bilan.** (Z)-but-2-ène

**Liaisons et fonctions modifiées**

- C≡C devient C=C ; un H ajouté sur chaque C.

**Règles et sélectivité**

- Addition syn et catalyseur modéré permettant l’arrêt à l’alcène.
- Na / NH₃ liquide fournit un autre chemin, souvent l’alcène E.

**Caractérisation du produit**

- Une insaturation reste ; deux CH₃ du même côté de C=C donnent Z.

**Étapes à reconstruire**

1. Adsorption sur le catalyseur adapté.
2. Livraison syn de H.
3. Désorption de l’alcène sans réduction exhaustive dans les conditions choisies.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcyne` et son scénario. Paramètres : `substrate=butyne, reagent=lindlar, stage=2`.

**Question.** Faut-il deux équivalents H₂ pour atteindre l’alcène ?

**Réponse.** Un équivalent H₂ suffit au bilan alcyne→alcène. Deux équivalents sont nécessaires pour alcyne→alcane.

### Fiche 51 — Hydratation d’alcyne : énol transitoire, cétone isolée

**Famille :** AE / tautomérie · **Niveau :** Sup → PC · **Identifiant :** `alcyne_hydratation`

**Substrat.** Propyne

**Réactifs et conditions.** H₂O / H⁺ / Hg²⁺ dans le cas du recueil

**Produit / bilan.** Énol puis propanone

**Liaisons et fonctions modifiées**

- Hydratation de C≡C vers C=C–OH ; transfert de proton et déplacement de π vers C=O.

**Règles et sélectivité**

- Orientation du cas terminal conduisant à la méthylcétone.
- Une hydroboration sélective/oxydation d’un terminal offre au contraire un aldéhyde.

**Caractérisation du produit**

- Ne pas isoler graphiquement l’énol comme produit final si le traitement conduit au carbonyle ; cétone C=O sans OH vinylique.

**Étapes à reconstruire**

1. Activation de l’alcyne et addition de l’eau.
2. Énol.
3. Tautomérie catalysée vers la cétone.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcyne` et son scénario. Paramètres : `substrate=propyne, reagent=mercury, stage=2`.

**Question.** La tautomérie est-elle une mésomérie ?

**Réponse.** Non : elle déplace un proton et change des liaisons σ, donc décrit des espèces distinctes. Une mésomérie ne déplace pas les noyaux.

## Page 532 — Autour du nitrobenzène

### Fiche 52 — Nitrobenzène : charges correctes avant de réagir

**Famille :** Structure / mésomérie · **Niveau :** Sup → PC · **Identifiant :** `nitro_lewis`

**Substrat.** Nitrobenzène C₆H₅NO₂

**Réactifs et conditions.** Comptabilité de Lewis et conjugaison

**Produit / bilan.** Deux contributeurs principaux Ph–N⁺(=O)–O⁻ et Ph–N⁺(–O⁻)=O

**Liaisons et fonctions modifiées**

- Aucun produit créé ; les deux O échangent leur rôle de liaison simple/double dans les contributeurs.

**Règles et sélectivité**

- N de deuxième période respecte l’octet : quatre liaisons au total, charge +1.
- Le groupe nitro retire par −I et −M.

**Caractérisation du produit**

- Vérifier neutralité globale, octets, deux O équivalents dans la description délocalisée et absence de doublet libre sur N.

**Étapes à reconstruire**

1. Compter les électrons de valence.
2. Placer N⁺ et O⁻.
3. Déplacer des doublets sans déplacer les atomes.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `nitrobenzene` et son scénario. Paramètres : `mode=lewis, contributor=oxygen_a, stage=0`.

**Question.** Peut-on dessiner deux N=O et une liaison N–Ph sans charges ?

**Réponse.** Ce N aurait cinq liaisons et dix électrons autour de lui ; il n’est pas une représentation de Lewis usuelle respectant l’octet. Les contributeurs N⁺/O⁻ résolvent le comptage.

### Fiche 53 — Nitration du nitrobenzène : orientation et désactivation

**Famille :** SEA · **Niveau :** Sup → PC · **Identifiant :** `nitro_nitration`

**Substrat.** Nitrobenzène

**Réactifs et conditions.** HNO₃ / H₂SO₄ ; conditions compatibles avec un noyau désactivé

**Produit / bilan.** Dinitrobenzènes ; isomère méta généralement favorisé

**Liaisons et fonctions modifiées**

- Un H aromatique est remplacé par NO₂ ; un second groupe nitro apparaît.

**Règles et sélectivité**

- NO₂ retire par −M et −I ; les complexes ortho/para sont moins favorables.
- Une orientation qualititative ne fournit pas les proportions sans données expérimentales ou cinétiques.

**Caractérisation du produit**

- Dessiner les connectivités 1,2 / 1,3 / 1,4 puis utiliser la symétrie pour le diagnostic, sans convertir un dipôle en rendement.

**Étapes à reconstruire**

1. Formation de NO₂⁺.
2. Comparer les complexes σ des trois positions.
3. Déprotonation et retour de l’aromaticité.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `aromatique` et son scénario. Paramètres : `substituent=nitro, reaction=nitration, stage=2`.

**Question.** Le caractère méta-directeur signifie-t-il que le nitrobenzène est activé ?

**Réponse.** Non : méta compare les voies sur le nitrobenzène. La désactivation compare leur vitesse à celle du benzène ; toutes peuvent être plus lentes.

## Page 533 — Alcènes et alcynes : applications

### Fiche 54 — Br₂ sur alcène Z : paire d’énantiomères

**Famille :** AE · **Niveau :** Sup → PC · **Identifiant :** `bromation_z`

**Substrat.** (Z)-but-2-ène

**Réactifs et conditions.** Br₂ sans lumière

**Produit / bilan.** Mélange (2R,3R)/(2S,3S) de 2,3-dibromobutane

**Liaisons et fonctions modifiées**

- Même bilan de connectivité que le substrat E, mais autre stéréochimie.

**Règles et sélectivité**

- Addition anti ; les deux faces donnent une paire racémique en milieu achiral.

**Caractérisation du produit**

- Comparer le produit au méso issu du réactif E ; une RMN achirale ne distingue pas les deux énantiomères.

**Étapes à reconstruire**

1. Bromonium depuis chacune des faces équivalentes.
2. Ouverture anti.
3. Dessiner les deux produits 3D avant CIP.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=butene_Z, reagent=bromine, stage=2`.

**Question.** Quelle observation démontre la stéréospécificité ?

**Réponse.** Les alcènes E et Z, sous un même mécanisme anti, donnent des ensembles stéréochimiques différents : méso pour E dans ce cas, paire racémique pour Z.

### Fiche 55 — E2 du recueil : (3S,4R)/(3R,4S) vers Z

**Famille :** E2 · **Niveau :** Sup → PC · **Identifiant :** `e2_source_z`

**Substrat.** 3-Bromo-3,4-diméthylhexane, paire (3S,4R)/(3R,4S)

**Réactifs et conditions.** Base ; H de C4 anti à Br

**Produit / bilan.** (Z)-3,4-Diméthylhex-3-ène pour l’élimination C3–C4

**Liaisons et fonctions modifiées**

- Même rupture C3–Br / C4–H que l’autre paire, mais configuration relative distincte.

**Règles et sélectivité**

- La disposition anti impose ici Et du même côté ; E2 est stéréospécifique pour la voie choisie.

**Caractérisation du produit**

- Et prioritaire sur CH₃ de chaque côté ; priorités du même côté donnent Z.

**Étapes à reconstruire**

1. Dessiner l’isomère SR ou RS.
2. Mettre Br et H4 anti par rotation propre.
3. Lire Z après l’élimination.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `e2stereo` et son scénario. Paramètres : `configuration=SR, dihedral=180, beta=c4`.

**Question.** Peut-on obtenir l’autre E/Z en tournant simplement une liaison après la réaction ?

**Réponse.** Non : la rotation libre autour de C=C n’est pas permise sans casser le système π. La rotation avant l’E2 respecte les configurations et ne change pas le produit stéréospécifique de cette voie.

### Fiche 56 — Oxydation douce : dihydroxylation syn

**Famille :** OR / addition syn · **Niveau :** Sup → PC · **Identifiant :** `diol_syn`

**Substrat.** But-2-ène

**Réactifs et conditions.** Oxydant adapté en conditions douces, diluées et froides

**Produit / bilan.** Butane-2,3-diol

**Liaisons et fonctions modifiées**

- C=C devient C–C ; deux C–O créées ; pas de coupure C–C dans ces conditions.

**Règles et sélectivité**

- Addition syn ; les conditions fortes peuvent au contraire cliver la liaison.

**Caractérisation du produit**

- Diol vicinal avec deux OH sur carbones voisins ; comparer à l’époxyde qui contient un seul O pontant.

**Étapes à reconstruire**

1. Addition sur une face selon le mécanisme de l’oxydant.
2. Intermédiaire cyclique oxygéné.
3. Hydrolyse vers le diol.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcene` et son scénario. Paramètres : `substrate=butene_E, reagent=diol, stage=2`.

**Question.** Un même oxydant garantit-il le même produit quelle que soit la température ?

**Réponse.** Non. Concentration, température et traitement déterminent si la transformation s’arrête au diol ou poursuit l’oxydation jusqu’à des fragments carbonylés ou acides.

### Fiche 57 — Alcyne + Br₂ : contrôler une ou deux additions

**Famille :** AE · **Niveau :** Sup → PC · **Identifiant :** `alcyne_br`

**Substrat.** Propyne ou but-2-yne

**Réactifs et conditions.** 1 puis 2 équivalents Br₂

**Produit / bilan.** Dibromoalcène puis tétrabromoalcane

**Liaisons et fonctions modifiées**

- Première addition : perte d’une π et création de deux C–Br ; deuxième : deux C–Br supplémentaires.

**Règles et sélectivité**

- Addition anti prédominante dans les cas standards de première addition.
- Le tétrabromure possède deux Br sur chacun des anciens C sp.

**Caractérisation du produit**

- Compter quatre Br au produit saturé ; distinguer ce tétrabromure du dibromure geminal issu de 2 HBr.

**Étapes à reconstruire**

1. Addition de Br₂ sur une π.
2. Alcène dibromé.
3. Nouvelle addition de Br₂.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcyne` et son scénario. Paramètres : `substrate=propyne, reagent=br2, stage=2`.

**Question.** Pourquoi 2 HBr et 2 Br₂ n’aboutissent-ils pas au même nombre de Br ?

**Réponse.** HBr livre un Br par équivalent tandis que Br₂ en livre deux. Le comptage des atomes précède toute lecture du nom de mécanisme.

### Fiche 58 — Réduction exhaustive d’alcyne : saturer deux π

**Famille :** OR / addition · **Niveau :** Sup → PC · **Identifiant :** `alcyne_h2_total`

**Substrat.** But-2-yne

**Réactifs et conditions.** H₂ en excès / métal actif

**Produit / bilan.** Butane

**Liaisons et fonctions modifiées**

- C≡C devient C–C ; quatre H ajoutés au bilan.

**Règles et sélectivité**

- Le catalyseur et l’excès différencient cette voie de Lindlar.
- Pas de configuration E/Z au produit saturé.

**Caractérisation du produit**

- Bilan C₄H₆ + 2 H₂ → C₄H₁₀ ; indice d’insaturation passe de 2 à 0.

**Étapes à reconstruire**

1. Première hydrogénation vers alcène.
2. Deuxième hydrogénation.
3. Produit saturé.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `alcyne` et son scénario. Paramètres : `substrate=butyne, reagent=hydrogen, stage=2`.

**Question.** Pourquoi le catalyseur doit-il être précisé avec H₂ ?

**Réponse.** La formule H₂ seule ne dit pas si la réaction s’arrête à l’alcène ou va à l’alcane. Activité, nature de la surface et quantité de H₂ déterminent les conditions de sélectivité.

## Page 534 — Autour du nitrobenzène

### Fiche 59 — Nitrobenzène → aniline : trois réductions à deux électrons

**Famille :** OR / AB · **Niveau :** Sup → PC · **Identifiant :** `nitro_reduction`

**Substrat.** Nitrobenzène

**Réactifs et conditions.** Réducteur métal/acide adapté puis neutralisation

**Produit / bilan.** Aniline ; nitroso et hydroxylamine comme états intermédiaires de la banque

**Liaisons et fonctions modifiées**

- PhNO₂ → PhNO → PhNHOH → PhNH₂ ; conservation de la liaison C–N.

**Règles et sélectivité**

- Bilan acide : PhNO₂ + 6 H⁺ + 6 e⁻ → PhNH₂ + 2 H₂O.
- En milieu acide, l’aniline peut être protonée ; la neutralisation est une opération distincte.

**Caractérisation du produit**

- Le groupe NO₂ devient NH₂, sans hydrogénation obligatoire du cycle ; suivre N, O, H et charge à chaque état.

**Étapes à reconstruire**

1. Deux électrons et deux H⁺ : nitro → nitroso + H₂O.
2. Deux électrons et deux H⁺ : nitroso → hydroxylamine.
3. Deux électrons et deux H⁺ : hydroxylamine → aniline + H₂O.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `nitrobenzene` et son scénario. Paramètres : `mode=reduction, stage=3`.

**Question.** Pourquoi le total vaut-il six électrons et deux eaux ?

**Réponse.** Additionner les trois bilans 2 e⁻ / 2 H⁺ annule les intermédiaires. Les premier et dernier actes forment chacun une eau, soit le bilan global 6 e⁻, 6 H⁺ et 2 H₂O.

### Fiche 60 — Dinitrobenzènes : somme de vecteurs, pas somme de rendements

**Famille :** Caractérisation / vecteurs · **Niveau :** Sup → PC · **Identifiant :** `nitro_dipoles`

**Substrat.** Isomères ortho, méta et para du dinitrobenzène

**Réactifs et conditions.** Modèle de deux dipôles égaux μ₀ radiaux dans un hexagone régulier

**Produit / bilan.** Normes idéalisées √3 μ₀, μ₀ et 0

**Liaisons et fonctions modifiées**

- Aucune liaison modifiée ; somme vectorielle de deux contributions fixes.

**Règles et sélectivité**

- Angles entre directions : 60° pour ortho, 120° pour méta, 180° pour para.
- Le modèle néglige les effets d’interaction entre substituants.

**Caractérisation du produit**

- Pour μ₀=4,03 D : environ 6,98 D, 4,03 D et 0 D dans ce modèle.
- Une molécule polaire ne représente pas une fraction du mélange ; composition et propriété doivent être séparées.

**Étapes à reconstruire**

1. Choisir les deux directions.
2. Additionner les composantes.
3. Calculer μ²=μ₀²+μ₀²+2μ₀² cos θ.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `dipolesnitro` et son scénario. Paramètres : `isomer=ortho, mu0=4.03, rotation=0`.

**Question.** Ces trois normes suffisent-elles à retrouver trois proportions de produits ?

**Réponse.** Non : elles caractérisent trois isomères dans un modèle. Pour remonter aux fractions d’un mélange il faut un protocole de mesure et une loi de mélange, avec assez d’informations indépendantes.

### Fiche 61 — Ordre des SEA : construire une cible à quatre substituants

**Famille :** SEA / stratégie · **Niveau :** Sup → PC · **Identifiant :** `nitro_strategie`

**Substrat.** Bromobenzène comme point de départ

**Réactifs et conditions.** Acylation compatible puis nitration puis chloration, avec choix d’isomères

**Produit / bilan.** Cible portant COCH₃ en C1, Cl en C3, Br en C4, NO₂ en C5

**Liaisons et fonctions modifiées**

- Trois H du noyau remplacés successivement par COCH₃, NO₂ et Cl ; Br initial conservé.

**Règles et sélectivité**

- Une première acylation sur le bromobenzène permet de choisir l’isomère para utile.
- COCH₃ méta-directeur et Br ortho/para-directeur peuvent converger ; NO₂ change ensuite les possibilités.
- Une route plausible n’est pas la preuve d’un produit unique ni d’un rendement garanti.

**Caractérisation du produit**

- Numéroter le cycle ; contrôler les relations ortho/méta/para à chaque étape ; suivre la formule finale C₈H₅BrClNO₃.

**Étapes à reconstruire**

1. Acyler avant d’installer un groupe nitro fortement désactivant.
2. Choisir/isoler l’isomère compatible avec la cible.
3. Réévaluer l’orientation de chaque nouvelle SEA sur le noyau alors présent.

**Expérience.** Dans l’application, la fiche ouvre le laboratoire `nitrobenzene` et son scénario. Paramètres : `mode=strategy, route=bromobenzene, stage=3`.

**Question.** Pourquoi tester un ordre inverse dans le laboratoire ?

**Réponse.** Le groupe NO₂ installé d’abord rend la Friedel–Crafts usuelle incompatible. L’ordre de synthèse doit satisfaire la réactivité aussi bien que les règles d’orientation.

## Douze approfondissements de cours

Ces douze leçons complètent le cours initial ; leurs numéros ici sont locaux à ce document. L’application les rassemble avec les leçons existantes pour une navigation commune.

### Leçon complémentaire 1 — Des règles aux mécanismes : quatre filtres avant un produit

*Sup → PC* · laboratoire `effets`.

**But et pages.** La page 524 prépare les tableaux de réactions : effet inductif, mésomérie, Markovnikov et Zaïtsev. Ces règles n’ont pas le même objet. La polarisation localise un site riche ou pauvre en électrons ; la conjugaison stabilise des espèces ; Markovnikov compare des orientations d’addition ; Zaïtsev compare souvent des alcènes accessibles. On les mobilise après avoir identifié le substrat et le chemin élémentaire.

Cδ+–Oδ− ; Cδ−–Mgδ+  
Nu: → C électrophile ; π(C=O) → O  
Formation d’alcène : Cβ–H et Cα–X rompus, Cα=Cβ créée

**Exemple emblématique.** Comparer l’hydratation acide et l’hydroboration–oxydation du propène : elles donnent respectivement propan-2-ol et propan-1-ol. Le premier chemin passe par une protonation et un carbocation ; le second fixe H et B concertément, puis remplace C–B par C–O. Le produit anti-Markovnikov n’est donc pas une exception arbitraire : son mécanisme répond à une autre question.

**Mésomérie et aromaticité.** Un chlorobenzène combine effet −I désactivant et donation +M qui favorise relativement ortho/para ; un nitrobenzène combine −I et −M et oriente généralement méta. Orientation compare les positions sur un même noyau, activation compare la réactivité à celle du benzène. Les contributeurs doivent conserver noyaux, charge totale et liaisons σ, avec octet pour C, N et O.

**Méthode CPGE.** Le raisonnement s’écrit en quatre filtres : possibilité chimique, acte élémentaire, contraintes de géométrie, puis sélectivité. Pour une E2 cyclohexanique, vérifier Hβ axial anti avant d’invoquer l’alcène le plus substitué. Enfin caractériser le produit par connectivité, fonctions, configuration et bilan d’atomes ; une règle d’orientation ne fournit pas un rendement chiffré.

### Leçon complémentaire 2 — E1 : intermédiaire plan, rotation et concurrence SN1

*Sup → PC* · laboratoire `e1`.

**But et pages.** Le tableau de la page 525 oppose clairement une E1 en plusieurs actes à une E2 concertée. Une E1 commence par l’ionisation d’un groupe partant, puis un Hβ est repris par une base. Le laboratoire suit le 2-chloro-3-méthylbutane de l’exercice 531/533, avec départ Cl⁻, et des déshydratations d’alcool où OH doit être protoné pour partir comme H₂O. La constitution, la stabilisation du cation et le milieu comptent ; une capture SN1 du même cation est une autre sortie, pas un second départ indépendant à compter deux fois.

Cas chlorure : RX → R⁺ + X⁻  
Cas alcool : ROH + H⁺ ⇌ ROH₂⁺ ; ROH₂⁺ → R⁺ + H₂O  
R⁺ + B → alcène + BH⁺ ; A(t)/A₀=exp(−kion t)

**Objets du laboratoire.** A désigne le stock précurseur de l’ionisation dans un modèle apparent où conditions et activation éventuelle sont incorporées à kion. Le curseur fournit cette constante choisie en s⁻¹, et le temps en s commande X(t)=1−exp(−kion t). La fraction de branchement vers l’alcène choisi est une donnée imposée, pas la conséquence universelle de Zaïtsev. Ce choix distingue conversion, distribution et rendement isolé ; les courbes ne décrivent pas toutes les solvolyses ou déshydratations.

**Exemple de stéréochimie.** Un cation plan peut tourner autour des liaisons simples avant de perdre Hβ. Les réactifs de configurations différentes ne sont donc pas nécessairement reliés de manière unique à E ou Z. Un alcène plus stable peut être favorisé, mais la géométrie, le solvant, la réversibilité et les vitesses de sortie comptent. Des migrations 1,2 peuvent aussi déplacer le centre cationique avant l’élimination.

**Technique CPGE.** Dessiner les Cβ et tous les Hβ, écrire au moins une voie de perte de proton et comparer à une capture SN1. Une base forte en quantité élevée peut imposer une E2 : l’ordre un observé seul ne justifie pas n’importe quelles conditions. Dans une copie, annoncer le modèle puis justifier ce qu’il permet réellement de conclure sur la constitution et la stéréochimie.

### Leçon complémentaire 3 — Énolate ambident : C-alkylation et O-alkylation

*Spé — PC, banque accompagnée* · laboratoire `enolatealkyl`.

**But et pages.** La première transformation de la page 526 fait de l’énolate un outil de construction de liaison C–C. Déprotoner en α d’un carbonyle donne une espèce conjuguée : une forme montre la charge sur O, une autre sur Cα. Ces deux dessins appartiennent à un même ion ambident ; la forme qui paraît la plus stable ne suffit pas à désigner le site le plus réactif dans toutes les conditions.

R–CO–CH₂⁻ ↔ R–C(O⁻)=CH₂  
C-alkylation : énolate + R′X → R–CO–CH₂R′ + X⁻  
O-alkylation : énolate + R′X → éther d’énol + X⁻

**Choisir l’électrophile.** Un dérivé méthyle ou primaire peu encombré permet une attaque SN2 avec départ X⁻. Un tertiaire ne se remplace pas par la même attaque arrière : une base forte peut plutôt prélever Hβ et éliminer. L’usage d’un malonate stabilisé, d’un contre-ion et d’un solvant adaptés appartient au choix de stratégie ; le laboratoire annonce une banque de connectivités et un bilan, sans prédire un ratio C/O expérimental.

**Exemple construit.** La C-éthylation de l’énolate de propanone donne pentan-2-one : les trois C de la propanone et les deux C du groupe éthyle se retrouvent dans le produit. Une O-éthylation donne au contraire un éther d’énol ; le carbonyle n’a pas la même forme. Le donneur possède encore des Hα après une monoalkylation, si bien qu’un nouvel excès de base et d’électrophile peut multiplier les substitutions.

**Technique CPGE.** Avant toute flèche, repérer le Cα, le proton retiré, le C porteur de X et le groupe transféré. Après l’attaque, redessiner C=O et compter les carbones. Comparer deux connectivités C/O et dire laquelle le protocole recherche. La séparation entre formation de l’énolate et addition de l’électrophile évite de confondre acidité, nucléophilie et nombre d’équivalents.

### Leçon complémentaire 4 — Alkylation d’amine : passer du doublet au sel

*Sup → PC* · laboratoire `aminealkyl`.

**But et pages.** La page 526 met côte à côte alkylation d’amine et acylation : ces opérations forment toutes deux une liaison C–N mais ne donnent pas la même fonction. Alkylation attaque le carbone d’un halogénoalcane ; acylation attaque un carbone carbonylé et conserve une fonction C=O. Le laboratoire d’alkylation suit une amine tertiaire afin que la charge du produit ne puisse pas être effacée par une déprotonation imaginaire de N.

R₃N: + R′X → \[R₃N–R′\]⁺ X⁻  
Charge formelle N = 5−Nnonliants−Nliaisons  
N tertiaire : 5−2−3=0 ; N quaternaire : 5−0−4=+1

**Mécanisme.** Le doublet de N attaque à l’arrière un carbone méthyle ou primaire, et le doublet C–X part vers X. Quatre liaisons σ entourent désormais N, sans doublet non liant disponible. Le contre-ion X⁻ est une espèce distincte indispensable au bilan de charge. Un ammonium quaternaire n’est donc pas une amine simplement dessinée avec un substituant supplémentaire sans charge.

**Stratégie et sélectivité.** Alkyler une amine primaire n’arrête pas nécessairement la réaction au monoalkylé : l’amine secondaire reste nucléophile, puis la tertiaire peut encore donner le quaternaire. Substrats et conditions doivent limiter ou orienter les alkylations successives. Le modèle de tertiaire choisi isole la dernière étape ; il ne prédit pas la distribution d’une amine primaire face à un excès d’halogénoalcane.

**Caractériser le produit.** Contrôler nombre de groupes autour de N, charge, contre-ion et présence ou absence de carbonyle adjacent. Par exemple triéthylamine + bromure de benzyle forme benzyltriéthylammonium bromure ; le groupe benzyle est transféré entier, y compris son CH₂. Une réaction de la même amine avec un chlorure d’acyle peut servir de piégeage de proton ou d’autres chemins : on ne transpose pas ce dessin de SN2 sans revoir l’électrophile.

### Leçon complémentaire 5 — Anhydrides : bilan de groupes acyle et rôle de la base

*Spé — PC* · laboratoire `anhydride`.

**But et pages.** Les pages 526 et 528 présentent formation d’anhydride et emploi de dérivés activés pour fabriquer esters ou amides. Un anhydride comporte R–C(=O)–O–C(=O)–R′, avec un seul O central. Il ne possède pas la liaison O–O d’un peracide. Le laboratoire distingue former ce motif, l’hydrolyser, l’alcoolyser et l’utiliser pour acyler une amine.

RCOCl + R′CO₂⁻ → RCO–O–COR′ + Cl⁻  
(RCO)₂O + R′OH → RCOOR′ + RCO₂H  
(RCO)₂O + R′NH₂ → RCONHR′ + RCO₂H

**Chemin commun.** Un nucléophile attaque un carbone acyle trigonal ; le doublet π passe sur O et l’intermédiaire devient tétraédrique. Le retour du doublet de O rétablit C=O et expulse le groupe partant. Dans l’anhydride, ce départ est un carboxylate stabilisé. Transferts de protons et milieu final déterminent ensuite acide ou carboxylate, amine ou ammonium : ils doivent être écrits séparément de la nouvelle liaison.

**Exemple et piège.** Acétyler une amine par l’anhydride éthanoïque forme une seule liaison N–COCH₃ par événement d’acylation de ce bilan, avec l’autre moitié libérée comme acide/carboxylate. Un deuxième équivalent d’amine peut piéger cet acide ; il ne signifie pas deux groupes acétyle liés au même N. Une base externe permet de conserver plus d’amine nucléophile, selon son choix et son propre comportement chimique.

**Technique CPGE.** Colorer mentalement les deux carbones acyle, identifier le fragment retenu et le fragment qui quitte. Compter équivalents disponibles pour la liaison recherchée et pour neutraliser le coproduit. Lorsqu’un acide non activé rencontre une amine, vérifier d’abord le sel acido-basique plutôt qu’écrire une condensation spontanée. Le laboratoire fournit des bornes de bilan et des états, sans transformer ces bornes en rendement isolé.

### Leçon complémentaire 6 — Deux chlorations du benzène : lumière ou acide de Lewis

*Sup → PC, banque accompagnée* · laboratoire `photochlore`.

**But et pages.** La photoaddition de Cl₂ de la page 526 est un excellent contrepoint aux SEA de la page 525. Le même couple benzène/chlore peut être présenté sous des conditions qui changent entièrement le bilan. En présence d’un acide de Lewis et dans les conditions de substitution, un H du noyau est remplacé par Cl et l’aromaticité revient. Sous irradiation dans le cas de photoaddition, la saturation du système π conserve les H initiaux.

SEA : C₆H₆ + Cl₂ → C₆H₅Cl + HCl  
Photoaddition : C₆H₆ + 3 Cl₂ → C₆H₆Cl₆  
Insaturations : benzène 4 ; chlorobenzène 4 ; hexachlorocyclohexane 1

**Lecture électronique.** La SEA passe par un complexe σ qui réaromatise après déprotonation. La lumière peut générer des espèces radicalaires et ouvrir une famille d’additions sur le système π ; le produit saturé comporte six C tétraédriques du cycle. Une demi-flèche déplace un électron, une flèche pleine un doublet : ces deux notations ne doivent pas être confondues, même si le bilan atomique semble similaire.

**Stéréochimie et portée.** Le bilan C₆H₆Cl₆ fixe la composition, pas un unique arrangement des six Cl autour du cyclohexane. Les isomères relatifs doivent être distingués et une formule plane générique ne prédit pas leurs proportions. Le laboratoire compare motifs et disponibilités stœchiométriques ; il ne simule pas la cinétique complète d’une chaîne photoradicalaire ou une distribution mesurée des stéréoisomères.

**Technique CPGE.** Avant le mécanisme, noter quantité de Cl₂ et condition hν ou catalyseur. Après le mécanisme, recompter C, H et Cl, puis l’indice d’insaturation. Le chlorobenzène a perdu un H et garde trois π ; l’hexachlorocyclohexane garde six H et n’a plus les π du benzène. C’est un diagnostic de produit directement issu des transformations, sans détour par un catalogue général de spectroscopies.

### Leçon complémentaire 7 — Organomagnésien : préparer le réactif avant d’allonger le squelette

*Sup → PC* · laboratoire `grignardprep`.

**But et pages.** Le montage et les bilans d’organomagnésiens de la page 526 ne sont pas accessoires à l’addition carbonylée : ils expliquent pourquoi le réactif carboné peut exister au moment utile. Un halogénoalcane ou un halogénoaromatique réagit avec Mg en solvant éthéré sec ; le solvant coordonne le métal et la réaction exige un contrôle des fonctions protiques. On ajoute l’électrophile avant l’hydrolyse finale, pas après.

RX + Mg → RMgX  
RMgX + H₂O → RH + MgXOH (bilan simplifié)  
Capacité pour une addition simple ≤ min(1, équiv. RMgX disponibles)

**Grandeurs du modèle.** Les quantités sont normalisées par une quantité de RX de référence. Mg, eau et progression de formation fixent une borne stœchiométrique disponible ; ce n’est pas une cinétique de démarrage du magnésium. Le schéma ionique R⁻/MgX⁺ permet de lire les flèches, sans décrire les agrégats réels en éther. Un proton labile consomme un équivalent de réactif, avant toute addition attendue.

**Exemple formateur.** PhMgBr ajoute un groupe phényle à l’éthanal et fournit, après protonation de l’alcoolate, 1-phényléthanol. Avec CO₂, le carbone capturé devient le carbone carboxylique et le produit après acidification est l’acide benzoïque. Avec un époxyde simple, l’ouverture peut allonger la chaîne. Ces diagnostics suivent l’électrophile : hydrolyse finale n’est pas synonyme d’alcool dans tous les cas.

**Technique CPGE.** Écrire séparément préparation, construction C–C et traitement. Dans une molécule polyfonctionnelle, marquer eau, OH, CO₂H, NH ou autre proton incompatible et prévoir protection ou quantité supplémentaire justifiée. Pour un ester, deux additions successives changent la stœchiométrie : ne pas transposer la règle un équivalent par carbonyle d’un aldéhyde. L’exemple sec doit servir à comprendre un montage, pas à garantir une manipulation sans données expérimentales.

### Leçon complémentaire 8 — Hydrolyse acyle : un motif, trois réactivités, deux milieux

*Sup → PC* · laboratoire `hydrolyseacyle`.

**But et pages.** La page 526 écrit l’hydrolyse des dérivés carboxyliques avec un groupe Z. Déployer Z=Cl, OR ou NHR montre que le même bilan général n’impose ni la même vitesse ni les mêmes conditions. Chlorure d’acyle très réactif, ester et amide conjugué ne doivent pas être traités comme trois molécules interchangeables. Le laboratoire permet aussi de distinguer produit acide et produit carboxylate.

RCOZ + H₂O → RCO₂H + HZ (bilan générique)  
RCOOR′ + HO⁻ → RCO₂⁻ + R′OH  
RCONHR′ + HO⁻ → RCO₂⁻ + R′NH₂ (conditions adaptées)

**Mécanisme et activation.** La substitution au carbone acyle passe par addition, puis élimination d’un groupe partant ; protonations et déprotonations rendent certaines étapes possibles. En milieu acide, la protonation du carbonyle augmente son caractère électrophile et peut activer un départ. En milieu basique, HO⁻ attaque puis le produit carboxylique est piégé sous forme carboxylate. Une amide stabilisée exige généralement des conditions plus sévères que le chlorure d’acyle.

**Exemple et formes finales.** Hydrolyser un ester en milieu acide donne un équilibre acide/alcool dans un bilan dépendant de l’eau. Saponifier le même ester produit un carboxylate dans le milieu de réaction ; acidifier ensuite permet d’isoler l’acide. Hydrolyser une amide peut donner une amine libre en base, mais une forme ammonium en acide. Le pH final détermine les charges observées : l’étape de traitement doit être annoncée.

**Technique CPGE.** Nommer le groupe Z et écrire le produit de départ HZ ou Z⁻ avec la bonne charge. Suivre les deux fragments organiques, surtout lorsqu’un ester ou une amide porte plusieurs carbones. Comparer la conjugaison de Z avec C=O et la qualité du groupe partant pour justifier des différences qualitatives de réactivité ; sans constantes ni protocole, le simulateur ne fournit pas une durée d’hydrolyse expérimentale.

### Leçon complémentaire 9 — Nitrobenzène : Lewis, réduction et ordre des SEA

*Spé — PC, banque accompagnée* · laboratoire `nitrobenzene`.

**But et pages.** Les exercices 532 et 534 rassemblent représentation de Lewis, réduction en aniline et stratégie aromatique. Le groupe nitro n’est pas une case isolée : ses charges expliquent sa conjugaison attractrice, celle-ci explique l’orientation, et la forte désactivation limite les transformations compatibles. Les formules et la numérotation du cycle doivent rester lisibles à chaque étape.

Ph–N⁺(=O)–O⁻ ↔ Ph–N⁺(–O⁻)=O  
PhNO₂ → PhNO → PhNHOH → PhNH₂  
PhNO₂ + 6 H⁺ + 6 e⁻ → PhNH₂ + 2 H₂O

**Réduction pas à pas.** Une banque d’états nitro, nitroso, hydroxylamine et amine rend le comptage vérifiable. Chacun des trois passages consomme deux électrons et deux protons dans le bilan acide choisi ; les premier et dernier libèrent une eau. Le métal réel fournit les électrons dans le protocole correspondant. En milieu acide, le produit aminé peut être protoné, puis neutralisé lors du traitement. Écrire seulement Fe/H⁺ ne remplace pas ce bilan.

**Stratégie emblématique.** Une cible portant COCH₃, Br, NO₂ et Cl exige de choisir l’ordre des SEA. Une acylation préalable d’un bromobenzène permet d’isoler l’isomère para utile ; COCH₃ oriente ensuite méta tandis que Br oriente ortho/para. Chaque nouveau groupe change la carte des sites. La séquence envisagée doit encore préciser conditions, isomères obtenus et séparations ; une convergence de directeurs n’établit pas un rendement de 100 %.

**Technique CPGE.** Vérifier d’abord l’octet du N et les charges N⁺/O⁻, ensuite la conservation des atomes pendant la réduction. Pour une stratégie, numéroter le cycle, dresser l’effet de chaque substituant, vérifier que la transformation est possible, puis discuter orientation. Une nitration avant une Friedel–Crafts usuelle peut désactiver le noyau au point d’interdire l’étape : réactivité et orientation sont deux filtres indépendants.

### Leçon complémentaire 10 — Dipôles des dinitrobenzènes : géométrie et limite du modèle

*Sup → PC* · laboratoire `dipolesnitro`.

**But et pages.** Le problème du nitrobenzène des pages 532 et 534 invite à relier substitution et moments dipolaires. On construit un modèle géométrique explicite : deux contributions égales μ₀ portées par les deux directions substituées d’un hexagone régulier. μ₀ est une valeur fournie en Debye. Le modèle compare des isomères, pas des vitesses de réaction ni des proportions issues d’une nitration.

μ² = μ₀² + μ₀² + 2 μ₀² cos θ  
Ortho θ=60° : μ=√3 μ₀ ; méta θ=120° : μ=μ₀  
Para θ=180° : μ=0 ; 1 D ≈ 3,33564×10⁻³⁰ C·m

**Dérivation et exemple.** Le carré de la norme d’une somme de vecteurs fait intervenir le produit scalaire. Les angles 60°, 120° et 180° sont les écarts entre directions radiales, non l’angle de valence local entre deux liaisons dans un même carbone. Avec μ₀=4,03 D, les trois normes valent approximativement 6,98 D, 4,03 D et 0 D. Tourner toute la molécule dans le plan change les composantes mais laisse la norme identique.

**Caractérisation.** Une norme nulle pour para dans ce modèle vient de la symétrie de deux vecteurs égaux opposés ; elle ne signifie ni absence de liaisons polaires ni absence de polarisabilité. Une valeur non nulle peut aider à discuter une constitution, en complément d’autres données. Les interactions entre substituants et la géométrie réelle peuvent modifier les valeurs mesurées : le modèle est annoncé afin de ne pas confondre calcul vectoriel et mesure universelle.

**Technique CPGE.** Dessiner les directions, projeter les vecteurs, additionner les composantes puis calculer la norme. Ne jamais additionner seulement les normes. Pour un mélange, la mesure et sa loi de réponse doivent être données avant toute inversion : trois propriétés de trois espèces ne fixent pas trois fractions. La régiosélectivité de nitration vient des chemins de réaction et des données de produits, pas de la taille du dipôle de l’isomère pur.

### Leçon complémentaire 11 — E2 du recueil : configurations conservées jusqu’à l’élimination

*Spé — PC* · laboratoire `e2stereo`.

**But et pages.** Les deux paires de 3-bromo-3,4-diméthylhexane des pages 531 et 533 rendent l’E2 stéréospécifique réellement testable. On choisit la voie C3–C4 : Br est porté par C3 et le H éliminé par C4. La projection de Newman doit conserver les configurations R/S tout en permettant la rotation de la liaison C3–C4 avant la réaction. Une permutation de substituants pour fabriquer artificiellement un dessin anti serait un changement d’isomère.

H4–C4–C3–Br anti : dièdre 180°  
(3S,4S) ou (3R,4R) → (E)-3,4-diméthylhex-3-ène  
(3S,4R) ou (3R,4S) → (Z)-3,4-diméthylhex-3-ène

**Lecture CIP.** Sur chaque carbone de l’alcène C3=C4, Et est prioritaire sur CH₃ : au premier rang tous commencent par C, mais le rang suivant de l’éthyle contient C,H,H contre H,H,H pour le méthyle. Les deux Et opposés définissent E, du même côté Z. Les centres tétraédriques C3 et C4 disparaissent pendant cette élimination ; le produit de cette connectivité ne garde donc pas leurs deux étiquettes R/S.

**Régiochimie et portée.** C3 est aussi voisin d’autres sites β, notamment C2 et un méthyle. Prendre leur H construit d’autres connectivités d’alcènes. Une assertion E/Z pour la voie C3–C4 n’est pas une preuve que ces régioisomères sont absents. Les populations de conformations, les bases et les barrières détermineraient leurs proportions ; le laboratoire n’invente pas ces données et sépare la voie choisie de la sélection cinétique réelle.

**Technique CPGE.** Procéder dans cet ordre : attribuer les configurations de départ, dessiner Newman, tourner une extrémité sans échanger ses groupes, chercher H/Br anti, tracer les trois flèches E2 puis appliquer CIP au produit. Comparer SS/RR à SR/RS démontre la stéréospécificité sans utiliser Zaïtsev comme substitut au dessin. Une rotation de la molécule produit un autre point de vue, pas un autre stéréoisomère.

### Leçon complémentaire 12 — Époxyde : former le pont, puis choisir le carbone d’ouverture

*Spé — PC, banque accompagnée* · laboratoire `epoxydes`.

**But et pages.** Les pages 526 et 528 présentent l’époxydation d’un alcène et le cas industriel de l’oxyde d’éthylène. Le cycle à trois atomes C–C–O concentre deux propriétés utiles : il conserve une relation stéréochimique lors d’une formation concertée, puis il s’ouvre avec rupture d’une liaison C–O sous attaque nucléophile. Un époxyde est un éther cyclique contraint, pas un diol déjà ouvert.

Alcène + RCO₃H → époxyde + RCO₂H  
2 C₂H₄ + O₂ → 2 C₂H₄O : procédé Ag adapté à l’éthylène  
Époxyde + MeO⁻ → alcoolate ouvert ; traitement → méthoxyalcool

**Former le pont.** Le transfert d’un O par peracide est concerté et conserve la relation des groupes de l’alcène : (E)-but-2-ène donne l’époxyde à méthyles trans, (Z)-but-2-ène celui à méthyles cis. Les faces équivalentes sont à prendre en compte pour les énantiomères. Le procédé O₂/Ag est un autre contexte, réservé ici à l’éthylène ; son bilan ne démontre ni toutes les étapes de surface ni une sélectivité de 100 %.

**Ouvrir en base ou en acide.** Pour un époxyde dissymétrique tel que l’oxyde de propylène, MeO⁻ en milieu basique attaque le carbone le moins encombré à l’arrière et rompt sa liaison C–O. En milieu acide, l’époxyde protoné peut favoriser l’attaque d’un nucléophile neutre MeOH sur le carbone plus substitué ; il subsiste une attaque arrière et une inversion géométrique au carbone ciblé. Une ouverture acide n’impose donc pas un carbocation libre isolé dans ce modèle.

**Caractériser depuis les liaisons.** Avec méthoxyde sur l’oxyde de propylène, le produit de la banque basique porte OMe en bout de chaîne et OH sur le carbone secondaire après protonation. Avec méthanol en acide, l’autre régioisomère de la banque porte OMe sur le carbone secondaire et OH en bout de chaîne. L’O initial de l’époxyde reste attaché au carbone non attaqué. Suivre l’origine de chaque O et la rupture C–O distingue immédiatement les produits et oblige à annoncer le traitement final.

## Douze introductions d’expériences

### Laboratoire `effets`

Transformer quatre règles de la page 524 en arguments de mécanisme. L’expérience fait lire sites, conjugaison, orientation d’addition et géométrie d’élimination avant de nommer un produit.

**Objets et unités**

- Charge formelle entière et charge partielle δ ; structures et contributeurs d’un même système
- Connexions créées/rompues ; régiochimie et stéréochimie sans rendement chiffré

**Hypothèses**

- Scénarios choisis pour comparer des règles ; les effets électroniques ne sont pas des constantes de vitesse
- Les formes mésomères gardent noyaux, charge et squelette σ

**Techniques**

- Lecture δ+/δ−
- Comptage d’octet et formes mésomères
- Filtre mécanisme/géométrie avant orientation

**Prédire → expérimenter → justifier**

1. Comparer C–O et C–Mg et proposer les sites de réaction avant les étapes.
2. Choisir Markovnikov puis Zaïtsev ; écrire pour chacun quelle liaison et quel intermédiaire sont concernés.
3. Ouvrir un cas où géométrie ou mécanisme change la règle et justifier le produit par les liaisons.

**Niveaux**

- Sup : Polarisation, effets électroniques et règles usuelles en PCSI.
- Spé : Conjugaison des intermédiaires et sélectivité en PC.
- Au-delà : Calcul de densité électronique, contre-ions et solvatation.

Leçons complémentaires : 1.

**Résultat attendu.** Une justification en étapes, distinguant règle de constitution, contrainte géométrique et donnée cinétique.

### Laboratoire `e1`

Relier le schéma E1 de la page 525 à l’ionisation et aux Hβ, puis distinguer conversion et répartition des produits. La branche choisie du modèle sert à tester un bilan, pas à prédire une sélectivité universelle.

**Objets et unités**

- kion apparent en s⁻¹, temps en s ; fraction transformée du stock initial
- Cβ et Hβ ; C–Cl du cas source ou alcool/oxonium, carbocation et fraction de branchement imposée

**Hypothèses**

- Ionisation d’ordre un choisie ; substrats hors du domaine signalés
- Fraction de produits fournie comme paramètre ; capture SN1 et élimination sont des sorties du même flux

**Techniques**

- Lecture de l’étape déterminante
- Énumération des Hβ
- Séparation conversion/sélectivité/rendement

**Prédire → expérimenter → justifier**

1. Dans le cas source, dessiner le départ Cl⁻ et les Hβ ; comparer à un alcool qui doit d’abord être protoné.
2. Changer le temps puis la constante ; faire varier la branche vers l’alcène en gardant la disparition totale sous contrôle.
3. Calculer la fraction du stock devenue cible et comparer à une E2 concertée.

**Niveaux**

- Sup : Mécanismes par étapes et notions de cinétique en PCSI.
- Spé : Compétition SN1/E1, rotations et réarrangements en PC.
- Au-delà : Paires d’ions et réseaux cinétiques ajustés.

Leçons complémentaires : 2.

**Résultat attendu.** Un produit justifié par son Hβ et trois nombres correctement distingués.

### Laboratoire `enolatealkyl`

Reprendre la C-alkylation de la page 526 avec un vrai choix de site C/O. L’expérience montre comment une même espèce ambidente peut conduire à deux fonctions et pourquoi l’électrophile primaire compte.

**Objets et unités**

- Carbone α du donneur, O de l’énolate et C porteur de X
- Équivalents de nucléophile ; liaison C–C ou O–C et motif de produit

**Hypothèses**

- Banque de connectivités choisies ; aucun ratio expérimental C/O calculé
- Mécanisme SN2 standard pour méthyle/primaire ; tertiaire testé comme incompatibilité

**Techniques**

- Deux contributeurs d’énolate
- Construction atomique d’une SN2
- Comparaison cétone/éther d’énol

**Prédire → expérimenter → justifier**

1. Écrire les deux contributeurs de l’énolate et localiser les sites nucléophiles.
2. Passer de C à O puis du primaire au tertiaire ; noter fonctions et voies possibles.
3. Recompter les carbones et expliquer pourquoi un excès ne corrige pas une SN2 entravée.

**Niveaux**

- Sup : Repérage de Cα, acidité et flèches avec banque fournie.
- Spé : Énolates, synthèse C–C et sélectivité en PC.
- Au-delà : Énolates cinétiques/thermodynamiques et influence des contre-ions.

Leçons complémentaires : 3.

**Résultat attendu.** Deux produits de connectivités distinctes, avec un choix d’électrophile argumenté.

### Laboratoire `aminealkyl`

Faire parler la dernière réaction de la page 526 : une alkylation d’amine tertiaire donne un ammonium quaternaire. La lecture de charge et du fragment benzyle transforme le bilan en mécanisme réellement vérifiable.

**Objets et unités**

- Doublet N, carbone porteur de X, quatre groupes autour de N au produit
- Charge +1 du cation et contre-ion X⁻ ; équivalents en unités du stock d’amine

**Hypothèses**

- Tertiaire choisie pour isoler la quaternisation ; distribution d’une primaire non modélisée
- Électrophile méthyle ou benzyle de la banque, attaque arrière

**Techniques**

- Flèches SN2
- Charge formelle de N
- Distinction alkylation/acylation

**Prédire → expérimenter → justifier**

1. Prévoir nombre de liaisons et charge de N avant de lancer l’étape.
2. Comparer méthyle et benzyle ; vérifier le CH₂ du groupe benzyle et le contre-ion.
3. Expliquer pourquoi aucun transfert de N–H ne peut neutraliser cette amine quaternisée.

**Niveaux**

- Sup : Lewis, SN2 et fonctions azotées en PCSI.
- Spé : Alkylations successives et stratégie sélective en PC.
- Au-delà : Catalyse de transfert de phase et synthèse d’amines contrôlée.

Leçons complémentaires : 4.

**Résultat attendu.** Un sel complet dessiné avec charges, contre-ion et fragments carbonés conservés.

### Laboratoire `anhydride`

Relier les pages 526 et 528 : former un anhydride puis transférer un de ses groupes acyle. Les scénarios montrent le destin distinct des deux moitiés et le rôle du piège à acide.

**Objets et unités**

- Deux carbones acyle, un O pont et groupe partant carboxylate
- Équivalents de nucléophile et base ; fonctions ester, amide ou acide

**Hypothèses**

- Banque de dérivés symétriques ; transferts de protons simplifiés mais bilans annoncés
- Bornes stœchiométriques sans cinétique ni rendement d’isolement

**Techniques**

- Addition–élimination
- Bilan des deux fragments acyle
- Séparation réaction de liaison et neutralisation

**Prédire → expérimenter → justifier**

1. Dessiner le motif sans liaison O–O et colorer ses deux carbones acyle.
2. Comparer formation, hydrolyse, alcoolyse et amidation ; suivre le groupe qui quitte.
3. Changer le mode de piège à acide et expliquer le rôle d’un second équivalent d’amine.

**Niveaux**

- Sup : Fonctions et comptage des liaisons avec banque fournie.
- Spé : Dérivés carboxyliques et activation en PC.
- Au-delà : Agents de couplage et acylation chimiosélective.

Leçons complémentaires : 5.

**Résultat attendu.** Un bilan complet des deux moitiés de l’anhydride, avec les formes acido-basiques indiquées.

### Laboratoire `photochlore`

Comparer la photoaddition de la page 526 à la SEA de la page 525 sur le même benzène. Le contrôle des conditions et du bilan H/Cl fait reconnaître deux familles de produits sans confondre lumière et catalyse de Lewis.

**Objets et unités**

- Quantité de Cl₂ en équivalents ; condition de lumière et mode choisi
- H conservés/substitués ; nombre de π et motif aromatique ou saturé

**Hypothèses**

- Bilans limites choisis ; distribution complète d’isomères chlorés non prédite
- Pas de cinétique photoradicalaire ni de simulation du spectre lumineux

**Techniques**

- Comptage H/Cl
- Indice d’insaturation
- Distinction flèche doublet/demi-flèche

**Prédire → expérimenter → justifier**

1. Prévoir les formules pour substitution d’un H et addition de trois Cl₂.
2. Changer mode, lumière et quantité de chlore ; vérifier si le stock peut réaliser le bilan cible.
3. Identifier aromaticité restante et information stéréochimique absente de la formule brute.

**Niveaux**

- Sup : Bilans et familles de réactions en PCSI.
- Spé : Aromaticité et voies radicalaires avec banque accompagnée.
- Au-delà : Photochimie, cinétiques de chaînes et catalyse sélective.

Leçons complémentaires : 6.

**Résultat attendu.** Deux produits correctement différenciés par leur formule et leurs liaisons, sans rendement inventé.

### Laboratoire `grignardprep`

Relier le montage de la page 526 à la réactivité du carbone organomagnésien. Une préparation sèche est une condition de construction C–C ; les contaminants protiques réduisent le stock utile avant l’addition recherchée.

**Objets et unités**

- Quantités RX/Mg/protons en équivalents et progression de formation choisie
- Réactif RMgX disponible, produit RH de destruction et borne de capacité d’addition

**Hypothèses**

- Bilan normalisé par RX ; pas de cinétique de démarrage réelle du Mg
- Protons consommés prioritairement ; structure agrégée de RMgX non calculée

**Techniques**

- Ordre préparation/addition/traitement
- Bilan des protons incompatibles
- Suivi du carbone nucléophile

**Prédire → expérimenter → justifier**

1. Prévoir le devenir de RMgX si l’eau est ajoutée avant le carbonyle.
2. Comparer milieu sec et eau ; réduire le stock de Mg ou la progression de formation.
3. Calculer la quantité disponible et choisir un électrophile avec un traitement final adapté.

**Niveaux**

- Sup : Organomagnésiens et préparation en PCSI selon le parcours.
- Spé : Polyfonctionnalité et protection en PC.
- Au-delà : Agrégation, équilibres de Schlenk et chimie organométallique.

Leçons complémentaires : 7.

**Résultat attendu.** Une séquence compatible et une borne stœchiométrique distinguée du rendement.

### Laboratoire `hydrolyseacyle`

Déployer le Z de l’hydrolyse générique de la page 526. Le laboratoire compare chlorure d’acyle, ester et amide, puis le milieu acide/base pour faire écrire les bonnes fonctions et charges finales.

**Objets et unités**

- Groupe Z, carbone acyle et fragment libéré ; étapes 0 à 3
- Équivalents du réactif de milieu ; carboxylique/carboxylate et amine/ammonium

**Hypothèses**

- Banque de mécanismes et formes finales ; constantes de vitesse absentes
- Une amide ne reçoit pas arbitrairement la même réactivité qu’un chlorure

**Techniques**

- Addition–élimination acyle
- Qualité du départ et conjugaison
- Traitement acido-basique final

**Prédire → expérimenter → justifier**

1. Écrire pour chaque Z le fragment qui part et celui qui reste.
2. Passer d’acide à base ; suivre charge du fragment carboxylique et de la fonction azotée.
3. Comparer les conditions qualitatives et expliquer pourquoi une borne de bilan n’est pas une durée d’hydrolyse.

**Niveaux**

- Sup : Estérification/hydrolyse et stœchiométrie en PCSI.
- Spé : Dérivés acyle et amides en PC.
- Au-delà : Catalyse enzymatique et activation de liaison peptidique.

Leçons complémentaires : 8.

**Résultat attendu.** Un produit de milieu et un produit après traitement distincts, avec un classement de réactivité expliqué.

### Laboratoire `nitrobenzene`

Réunir les questions des pages 532 et 534 dans un fil organique : charges de Lewis, réduction du groupe nitro et ordre de construction d’un noyau substitué. L’expérience associe chaque règle à une structure réellement présente.

**Objets et unités**

- N⁺/O⁻ et octets ; états nitro/nitroso/hydroxylamine/aniline
- H⁺, e⁻, H₂O dans les demi-bilans ; positions numérotées du cycle et groupes directeurs

**Hypothèses**

- États de réduction d’une banque ; le métal réel et les conditions doivent être fournis
- Stratégie aromatique représentée comme faisabilité à discuter, sans rendement ou isomère unique garanti

**Techniques**

- Comptabilité de Lewis
- Équilibrage redox par étapes
- Ordre de synthèse compatible avec les SEA

**Prédire → expérimenter → justifier**

1. Contrôler deux formes nitro en conservant octet et charge globale.
2. Suivre les trois réductions ; sommer leurs bilans et préciser la neutralisation finale.
3. Comparer route depuis bromobenzène et route qui nitre trop tôt ; numéroter les positions et justifier les limites.

**Niveaux**

- Sup : Lewis, charges et bilans avec banque fournie.
- Spé : Réactivité aromatique, réduction et stratégie en PC.
- Au-delà : Réduction catalytique sélective et voies de synthèse multigroupes.

Leçons complémentaires : 9.

**Résultat attendu.** Une réduction équilibrée et une stratégie contrôlée par réactivité puis orientation.

### Laboratoire `dipolesnitro`

Transformer la géométrie des pages 532/534 en un calcul vectoriel transparent. Les trois isomères ont des contributions de directions différentes ; l’expérience empêche de confondre propriété d’espèce pure et proportion de produits.

**Objets et unités**

- Deux vecteurs de norme μ₀ en Debye ; directions ortho/méta/para
- Composantes, norme de la somme et rotation commune en degrés

**Hypothèses**

- Hexagone régulier, deux contributions égales et indépendantes
- Aucune loi de mesure d’un mélange ni cinétique de nitration déduite du dipôle

**Techniques**

- Produit scalaire
- Addition des composantes
- Analyse des données nécessaires à un problème inverse

**Prédire → expérimenter → justifier**

1. Prévoir le cas para par symétrie puis dessiner les trois angles.
2. Changer l’isomère et tourner toute la molécule ; comparer composantes et norme.
3. Dériver √3μ₀, μ₀, 0 et expliquer quelles informations manquent pour un mélange.

**Niveaux**

- Sup : Vecteurs et polarité moléculaire en PCSI.
- Spé : Isomérie aromatique et interprétation de propriétés en PC.
- Au-delà : Calcul de moments dipolaires et mesures diélectriques.

Leçons complémentaires : 10.

**Résultat attendu.** Trois normes correctement dérivées, sans conversion abusive en pourcentages de nitration.

### Laboratoire `e2stereo`

Reconstruire l’exercice de 3-bromo-3,4-diméthylhexane des pages 531 et 533. SS/RR et SR/RS deviennent deux expériences distinctes qui prouvent la relation stéréospécifique entre configurations de départ et E/Z de la voie C3–C4.

**Objets et unités**

- Configurations (3R/S,4R/S), vue Newman C3–C4 et dièdre H–C–C–Br
- Choix de Cβ ; substituants Et/CH₃ et priorité CIP sur l’alcène

**Hypothèses**

- E2 anti standard et configurations conservées pendant rotation propre
- La voie choisie ne prédit pas sa proportion parmi les autres régioisomères

**Techniques**

- Projection Newman sans permutation
- Trois flèches concertées
- CIP puis E/Z après élimination

**Prédire → expérimenter → justifier**

1. Dessiner SS puis placer H4 et Br anti par une rotation licite.
2. Comparer RR, SR et RS ; changer le Hβ choisi et observer la connectivité.
3. Attribuer E/Z avec Et prioritaire, puis dire quelles données quantifieraient les voies concurrentes.

**Niveaux**

- Sup : Lecture 3D accompagnée et rappel SN2/E2 en PCSI.
- Spé : Stéréospécificité et régiosélectivité en PC.
- Au-delà : Effets isotopiques et barrières conformationnelles.

Leçons complémentaires : 11.

**Résultat attendu.** Une correspondance SS/RR→E, SR/RS→Z justifiée, avec les autres voies explicitement distinguées.

### Laboratoire `epoxydes`

Relier les époxydes des pages 526/528 à une vraie comparaison de voies. L’expérience forme un pont O avec conservation relative des groupes, puis l’ouvre sur un carbone différent selon acidité et nucléophile.

**Objets et unités**

- Alcène E/Z ou éthylène ; époxyde C–C–O et origine de chaque O
- Méthoxyde ou méthanol, eau ou HO⁻ selon le milieu ; étapes et attaque arrière

**Hypothèses**

- Banque de produits de peracide et d’ouverture ; pas de ratio régioisomérique calculé
- Procédé Ag limité à l’éthylène ; sélectivité et surface réelle non calculées

**Techniques**

- Conservation cis/trans à l’époxydation
- Sélection du C d’ouverture
- Bilan des O et transferts de protons

**Prédire → expérimenter → justifier**

1. Comparer E et Z au peracide et prévoir la relation trans/cis de l’époxyde.
2. Choisir oxyde de propylène ; comparer MeO⁻ en base à MeOH en acide et suivre quel O reste sur quel C.
3. Écrire les produits après traitement puis distinguer le bilan O₂/Ag de celui du peracide.

**Niveaux**

- Sup : Fonctions, structures et flèches avec banque accompagnée.
- Spé : Stéréochimie concertée et ouverture régiosélective en PC.
- Au-delà : Époxydation asymétrique et catalyse d’oxydation.

Leçons complémentaires : 12.

**Résultat attendu.** Deux régioisomères correctement suivis et une distinction entre relation stéréochimique, bilan et modèle catalytique.

## Vingt-quatre problèmes corrigés de réactions

### Problème complémentaire 1 — Markovnikov face à hydroboration : même substrat, deux produits

*Sup → PC* · laboratoire `effets`.

**Énoncé.** On dispose de propène. Construire le produit de H₂O/H⁺, celui de 1. BH₃ ; 2. H₂O₂/HO⁻ et celui de HBr sans peroxydes. Pour chacun, nommer le premier acte, localiser l’intermédiaire ou l’état concerté et préciser ce que la règle de Markovnikov permet de conclure.

**Corrigé.** L’hydratation acide donne propan-2-ol : la protonation favorise le carbocation secondaire, H₂O le capture puis perd H⁺. HBr sans peroxydes donne 2-bromopropane par le même choix de carbocation, suivi de Br⁻. L’hydroboration fixe concertément H et B, B sur le C terminal moins encombré ; l’oxydation remplace C–B par C–O avec rétention et donne propan-1-ol. Aucun carbocation libre n’est requis pour cette voie, donc le raisonnement par sa stabilité ne lui est pas applicable. Dans tous les cas les trois C sont conservés et une seule π est consommée. Syn/anti est une relation relative, tandis que Markovnikov décrit ici une orientation de connectivité : ce sont deux informations différentes.

### Problème complémentaire 2 — Halogène aromatique : désactiver tout en dirigeant ortho/para

*Spé — PC* · laboratoire `effets`.

**Énoncé.** Comparer chlorobenzène, anisole et nitrobenzène pour une nitration. Séparer effet inductif et mésomère, direction préférée et activation par rapport au benzène. Expliquer pourquoi la taille d’un moment dipolaire ne constitue pas une preuve de vitesse ou de proportion de produits.

**Corrigé.** Cl retire par −I, ce qui désactive le noyau, mais peut donner par +M et stabiliser relativement les complexes σ ortho/para. OCH₃ possède aussi un effet −I mais sa donation +M forte active le cycle et dirige ortho/para dans les conditions classiques. NO₂ combine −I et −M : le noyau est fortement désactivé et méta est généralement favorisé parce que les complexes ortho/para comportent des contributions défavorables supplémentaires. Orientation compare les sites sur une même molécule ; activation compare à une référence. Un moment dipolaire est une propriété vectorielle d’une espèce, et ne fournit ni barrière d’activation ni constante de vitesse. Les proportions exigent des données sur les flux ou les produits, avec conditions spécifiées.

### Problème complémentaire 3 — E1 : conversion et fraction d’un produit sont deux nombres

*Sup → PC* · laboratoire `e1`.

**Énoncé.** Une disparition de RX suit kion=0,020 s⁻¹. Dans un modèle d’embranchement imposé, 70 % du flux ionisé donne un alcène cible et 30 % une substitution. Calculer après 100 s conversion et fraction du stock initial devenue alcène ; discuter ce qui change si l’alcène cible est isolé avec seulement 80 % de récupération.

**Corrigé.** La fraction ionisée est X=1−exp(−0,020×100)=1−exp(−2)≈0,8647. La fraction du stock initial allant vers l’alcène vaut X×0,70≈0,6053, soit 60,53 %. Celle allant vers substitution vaut 25,94 %, et 13,53 % de RX reste. Une récupération de 80 % de l’alcène abaisse le rendement isolé à 0,6053×0,80≈0,4842, soit 48,42 %. Le bilan 13,53+60,53+25,94≈100 % concerne le réacteur ; les pertes d’isolement constituent un bilan distinct. La fraction de branchement choisie ne découle pas de l’ordre un et ne doit pas être annoncée comme une constante universelle d’E1. Les deux issues partagent le même départ ionisant : additionner deux disparitions indépendantes compterait deux fois le flux.

### Problème complémentaire 4 — E1 ou E2 : démontrer plutôt que réciter Zaïtsev

*Spé — PC* · laboratoire `e1`.

**Énoncé.** Pour un halogénoalcane secondaire possédant des Hβ, comparer un milieu ionisant avec faible base et un milieu contenant une base forte. Donner mécanisme, loi de vitesse attendue dans les modèles limites, possibilités de réarrangement et relation éventuelle entre configuration du réactif et E/Z des alcènes.

**Corrigé.** Le milieu ionisant peut permettre E1 : départ C–X puis carbocation, éventuellement migration et rotation, enfin prélèvement Hβ. Si l’ionisation est déterminante, la disparition est d’ordre un en RX ; le cation peut aussi être capturé en SN1. Une base forte peut favoriser E2 : B→Hβ, Cβ–H→Cβ=Cα et Cα–X→X⁻ dans un acte concerté. Le modèle limite a v=k₂\[RX\]\[B\], sans carbocation susceptible de se réarranger. Le filtre anti-périplanaire relie alors la stéréochimie à la conformation de départ. Pour E1 les rotations après ionisation suppriment généralement ce lien stéréospécifique. Zaïtsev ne décide ni de l’existence du cation ni des H géométriquement accessibles ; il donne une tendance parmi des voies déjà possibles. Les conditions et la qualité du départ restent à préciser.

### Problème complémentaire 5 — C-éthylation ou O-éthylation : reconstruire la connectivité

*Spé — PC* · laboratoire `enolatealkyl`.

**Énoncé.** On forme l’énolate de propanone et on le fait réagir avec bromoéthane. Écrire les deux contributeurs de l’énolate, construire une C-alkylation et une O-alkylation possibles et identifier le produit qui conserve une fonction cétone. Compter les carbones et expliquer le rôle du choix C/O dans le laboratoire.

**Corrigé.** L’énolate s’écrit CH₃COCH₂⁻↔CH₃C(O⁻)=CH₂. Une attaque du Cα sur CH₂Br avec départ Br⁻ donne CH₃COCH₂CH₂CH₃, pentan-2-one : trois C du donneur et deux de l’éthyle. Une attaque de O donne CH₃C(OEt)=CH₂, un éther d’énol à cinq C, avec une double liaison C=C et aucune fonction cétone telle qu’au produit de C-alkylation. Le choix C/O sélectionne deux connectivités de la banque ; il ne calcule pas leur rapport expérimental. Le contre-ion, le solvant et l’électrophile influencent cette sélectivité dans une synthèse réelle. Le comptage permet de reconnaître une erreur fréquente consistant à ajouter Et à O puis à dessiner simultanément le même carbonyle et le même Cα alkylé : cela représenterait une autre transformation.

### Problème complémentaire 6 — Énolate et tertiaire : une liaison cible peut être inaccessible

*Spé — PC* · laboratoire `enolatealkyl`.

**Énoncé.** Comparer l’éthylation d’un énolate de malonate par bromoéthane et sa réaction avec un halogénure tert-butyle. Pourquoi n’est-il pas suffisant d’augmenter l’excès d’électrophile pour obtenir la même C-alkylation ? Discuter l’hydrogène restant après une monoalkylation d’un malonate.

**Corrigé.** Bromoéthane possède un carbone primaire accessible à une attaque SN2 ; l’énolate carboné peut former une liaison C–CH₂CH₃ et expulser Br⁻. Le carbone tertiaire du halogénure tert-butyle est fortement encombré : la même SN2 est entravée, tandis que l’énolate basique peut enlever un Hβ et former un alcène. Ajouter plus de ce réactif ne supprime pas l’obstruction ni la compétition d’élimination. Un malonate initialement CH₂(CO₂R)₂ devient CH(Et)(CO₂R)₂ après monoalkylation et possède encore un H sur ce carbone ; une nouvelle déprotonation suivie d’alkylation est donc possible avec des conditions et stocks adaptés. On contrôle base, équivalents et séquence, sans assimiler disponibilité stœchiométrique à sélectivité ou rendement isolé.

### Problème complémentaire 7 — Benzyltriéthylammonium : conserver charge et fragment transféré

*Sup → PC* · laboratoire `aminealkyl`.

**Énoncé.** Construire le produit de triéthylamine et bromure de benzyle. Tracer les deux flèches de la substitution, donner la charge du N et le contre-ion, puis expliquer pourquoi une déprotonation de N ne donne pas une amine neutre portant encore les quatre groupes.

**Corrigé.** Le doublet de N attaque le CH₂ porteur de Br dans PhCH₂Br ; les électrons C–Br vont vers Br. Le produit est \[Et₃N–CH₂Ph\]⁺ Br⁻ : le benzyle transféré comprend le CH₂, qui ne doit pas être supprimé pour écrire une liaison directe N–Ph. N possède quatre liaisons σ et aucun doublet libre : sa charge formelle vaut 5−0−4=+1. Comme l’amine tertiaire initiale ne possède pas de N–H, aucun proton de N ne peut être retiré pour neutraliser cette charge. Le produit est un sel d’ammonium quaternaire, distinct d’une amine et d’une amide. Le bilan conserve C, H, N et Br ; les espèces peuvent être associées ioniquement, mais le contre-ion ne crée pas une cinquième liaison covalente autour de N.

### Problème complémentaire 8 — Alkylation répétée et acylation : deux stratégies différentes

*Spé — PC* · laboratoire `aminealkyl`.

**Énoncé.** Une synthèse cherche une amine secondaire à partir d’une primaire. Expliquer pourquoi un excès d’halogénoalcane n’est pas toujours une stratégie sélective. Comparer avec l’attaque d’une amine sur un chlorure d’acyle et préciser les fonctions qu’il faut reconnaître dans les produits.

**Corrigé.** Après une première alkylation, l’amine secondaire conserve un doublet et reste nucléophile ; elle peut donner une tertiaire, puis un ammonium quaternaire. Un excès d’halogénoalcane favorise donc des transformations successives plutôt qu’un arrêt assuré au produit recherché. Des protections, stœchiométries et autres méthodes de synthèse doivent être examinées avec les données du problème. L’acylation attaque un carbone de C=O et passe par addition–élimination ; elle donne un amide dont le N est adjacent à un carbonyle et dont le doublet est délocalisé. L’alkylation donne une liaison C–N à un carbone non acyle et peut donner un sel quaternaire. Les charges, le nombre de substituants et la présence de C=O distinguent immédiatement ces produits ; le mot « liaison C–N » seul ne les caractérise pas.

### Problème complémentaire 9 — Anhydride et amine : où passe la seconde moitié ?

*Spé — PC* · laboratoire `anhydride`.

**Énoncé.** Pour un anhydride éthanoïque et une amine primaire RNH₂, écrire le bilan d’une acylation, puis le bilan avec un second équivalent d’amine piégeant l’acide coproduit. Identifier les deux carbones acyle et distinguer cette voie d’une condensation de l’acide non activé.

**Corrigé.** Le bilan d’acylation s’écrit (CH₃CO)₂O+RNH₂→CH₃CONHR+CH₃CO₂H. Le nucléophile attaque un des deux C acyle, et la seconde moitié sort comme carboxylate avant les transferts de H. Si une seconde amine capte le proton de l’acide, le bilan ajoute CH₃CO₂H+RNH₂⇌CH₃CO₂⁻+RNH₃⁺, avec la position d’équilibre liée aux acidités dans le milieu choisi. Il y a une molécule d’amide dans ce bilan, pas deux amides produits par la même simple substitution. Une base externe adaptée peut jouer le rôle du second équivalent. L’acide non activé et l’amine donnent facilement un sel par transfert de proton ; la liaison amide exige activation ou condensation spécifique. Les deux groupes acyle ont donc des destins différents malgré leur symétrie au départ.

### Problème complémentaire 10 — Peracide, anhydride, ester : les oxygènes imposent les chemins

*Sup → PC* · laboratoire `anhydride`.

**Énoncé.** Dessiner les motifs d’un anhydride, d’un peracide et d’un ester. Expliquer lequel peut transférer O à un alcène dans une époxydation et lequel peut acyler un alcool. Construire le bilan d’alcoolyse de l’anhydride éthanoïque par l’éthanol et contrôler chaque O.

**Corrigé.** Anhydride : RCO–O–COR′, un O pont entre deux carbones acyle ; peracide : RCO–O–OH, avec liaison O–O ; ester : RCO–OR′, avec un seul groupe acyle. Le peracide est le donneur d’O dans l’époxydation concertée ; il donne un époxyde et RCO₂H. L’anhydride est un donneur de groupe acyle en addition–élimination ; avec EtOH, (CH₃CO)₂O+EtOH→CH₃COOEt+CH₃CO₂H. L’oxygène de l’alcool devient l’O lié à Et dans l’ester ; une moitié de l’anhydride fournit le groupe acétyle incorporé, l’autre le carboxylate/acide coproduit. Identifier ces motifs évite de dessiner un transfert de deux O ou un pont O–O dans un anhydride. La même lettre O n’implique pas le même rôle mécanique.

### Problème complémentaire 11 — Benzène + Cl₂ : bilan H conservé ou H substitué

*Sup → PC* · laboratoire `photochlore`.

**Énoncé.** Écrire les deux bilans limites benzène/Cl₂ sous conditions de SEA et sous irradiation conduisant à l’hexachlorocyclohexane. Pour chaque produit, calculer l’indice d’insaturation et expliquer quelle information stéréochimique reste absente du seul bilan global.

**Corrigé.** SEA : C₆H₆+Cl₂→C₆H₅Cl+HCl ; un H est remplacé et les trois π du cycle sont retrouvées. IHD=(2×6+2−5−1)/2=4, soit un cycle et trois π. Photoaddition : C₆H₆+3Cl₂→C₆H₆Cl₆ ; les six H sont conservés et six Cl ajoutés, sans perte de squelette. IHD=(14−6−6)/2=1, correspondant seulement au cycle saturé. Cette formule ne fixe pas les relations haut/bas, cis/trans ou axial/équatorial des six Cl ; différents isomères sont possibles. Les conditions sont donc nécessaires pour choisir la famille de réaction, et les données stéréochimiques pour choisir un isomère. Écrire C₆H₅Cl dans le scénario de saturation confond une substitution d’un H avec l’addition à trois π.

### Problème complémentaire 12 — Addition photochimique et substitution radicalaire : ne pas confondre

*Spé — PC* · laboratoire `photochlore`.

**Énoncé.** Comparer photoaddition de Cl₂ sur benzène et monohalogénation radicalaire d’isobutane. Lister les liaisons rompues/formées au bilan, préciser le rôle de la lumière et dire pourquoi la formule du réactif Cl₂ ne suffit pas à prévoir la distribution des produits.

**Corrigé.** La photoaddition sur le benzène consomme des π et crée C–Cl tout en conservant les H, jusqu’au bilan C₆H₆Cl₆ pour trois Cl₂. Une monohalogénation radicalaire d’isobutane remplace un C–H par C–Cl et forme HCl au bilan : les propagations sont prélèvement de H par Cl• puis transfert de Cl depuis Cl₂ au radical carboné. La lumière peut amorcer des radicaux par homolyse mais ne prescrit pas à elle seule toutes les propagations possibles sur n’importe quel substrat. Pour l’isobutane, nombre d’H de chaque type et réactivité relative déterminent une distribution ; pour l’hexachlorocyclohexane, arrangement des Cl et étapes d’addition interviennent. Les deux scénarios utilisent des demi-flèches mais leurs bilans de H, d’insaturation et de produits sont distincts.

### Problème complémentaire 13 — Réactif organomagnésien humide : calculer le stock utile

*Sup → PC* · laboratoire `grignardprep`.

**Énoncé.** Un modèle de préparation part d’une unité de RX avec assez de Mg ; 0,80 unité de RMgX a été formée. Une contamination représente 0,15 équivalent de proton consommant le réactif. Quelle quantité maximale reste-t-il pour une addition simple ? Que changerait la présence supplémentaire de 0,40 équivalent d’alcool libre ?

**Corrigé.** Après consommation de 0,15 équivalent de proton, la borne de RMgX disponible vaut max(0,0,80−0,15)=0,65 équivalent. Une addition simple nécessitant un RMgX par électrophile ne peut donc convertir plus de 65 % d’une unité de substrat, même si aucune autre perte n’existe. Avec 0,40 équivalent d’alcool libre supplémentaire, la borne tombe à max(0,0,80−0,15−0,40)=0,25 équivalent, soit 25 %. Ces nombres sont des capacités stœchiométriques, pas une vitesse ni un rendement isolé. Les protons donnent RH et consomment le carbone nucléophile avant la construction C–C ; on ne peut les soustraire après avoir supposé une conversion totale. Une protection compatible ou une préparation plus sèche doit être réfléchie avec le protocole.

### Problème complémentaire 14 — Méthanal, cétone, CO₂ : un réactif, trois diagnostics

*Sup → PC* · laboratoire `grignardprep`.

**Énoncé.** On prépare EtMgBr dans un milieu sec. Comparer son action sur méthanal, propanone et CO₂, suivie du traitement adapté. Nommer les produits, compter leurs carbones et expliquer pourquoi écrire « hydrolyse → alcool » comme règle générale donnerait une erreur.

**Corrigé.** Méthanal+EtMgBr donne après hydrolyse propan-1-ol : le C du méthanal devient CH₂OH et les deux C de Et complètent une chaîne de trois C. Propanone+EtMgBr donne 2-méthylbutan-2-ol à cinq C : les deux CH₃ initiaux et Et sont liés au C fonctionnel, donc alcool tertiaire achiral dans ce cas. CO₂+EtMgBr donne un carboxylate puis acide propanoïque à trois C après acidification ; le C de CO₂ est le C carboxylique, et la fonction reste de type acide. Le traitement protonne l’intermédiaire adapté : alcoolate pour les deux carbonyles, carboxylate pour CO₂. Le même organomagnésien n’impose donc pas une seule famille de produit. Préparation sèche, addition puis traitement sont trois moments distincts à conserver dans la séquence.

### Problème complémentaire 15 — Hydrolyse acide ou saponification : dessiner le milieu final

*Sup → PC* · laboratoire `hydrolyseacyle`.

**Énoncé.** Comparer l’hydrolyse acide de l’éthanoate d’éthyle et sa saponification. Nommer la forme du fragment carboxylique avant traitement, préciser rôle de l’eau ou de HO⁻, puis écrire l’opération qui permet d’obtenir l’acide neutre à partir du milieu basique.

**Corrigé.** En hydrolyse acide, eau et ester conduisent à acide éthanoïque et éthanol dans un équilibre catalysé par H⁺ ; le catalyseur est régénéré et un excès d’eau favorise la voie inverse de Fischer. En saponification, HO⁻ attaque le carbone acyle, le carbonyle se reforme avec départ de l’alcoolate, puis le transfert de proton donne CH₃CO₂⁻ et EtOH. Le carboxylate est la forme à écrire dans le milieu basique : HO⁻ est consommé au bilan. Une acidification séparée ajoute H⁺ pour transformer CH₃CO₂⁻ en CH₃CO₂H ; le pH choisi doit favoriser la forme neutre. Les bilans ne se différencient pas seulement par le mot « catalyse » : charges, stœchiométrie et position d’équilibre changent. Le fragment éthyle quitte l’acyle mais reste dans l’alcool.

### Problème complémentaire 16 — Chlorure, ester et amide : un Z ne signifie pas une même vitesse

*Spé — PC* · laboratoire `hydrolyseacyle`.

**Énoncé.** La notation RCOZ cache Z=Cl, OEt ou NHMe. Identifier les produits organiques de l’hydrolyse complète, puis discuter qualitativement leurs conditions. Pourquoi une amide demande-t-elle généralement des conditions plus sévères qu’un chlorure d’acyle ? Donner les formes amine/ammonium selon le milieu.

**Corrigé.** Les trois dérivés donnent le fragment RCO₂H ou RCO₂⁻ selon le milieu. Cl conduit à chlorure/HCl, OEt à éthanol, NHMe à méthylamine ou méthylammonium selon pH. Le chlorure d’acyle est fortement électrophile et possède un bon groupe partant ; il s’hydrolyse facilement. L’ester possède une donation du groupe OR et un départ qui demande des transferts adaptés. Dans l’amide, la donation du doublet de N stabilise le motif, diminue l’électrophilie du C et donne à C–N un caractère partiellement double ; le départ d’un anion amidure serait défavorable sans activation. Acide/base et chauffage rendent les étapes possibles. En milieu acide l’amine est souvent protonée, en base elle peut être libre. Le tableau de produits ne constitue pas un tableau de constantes de vitesse ni une garantie de conversion sous n’importe quelles conditions.

### Problème complémentaire 17 — Nitro → aniline : annuler les intermédiaires, pas les atomes

*Spé — PC* · laboratoire `nitrobenzene`.

**Énoncé.** Équilibrer en milieu acide les trois passages PhNO₂→PhNO, PhNO→PhNHOH, PhNHOH→PhNH₂ à l’aide de H⁺, e⁻ et H₂O. Les additionner et distinguer ce bilan de la forme acido-basique de l’amine obtenue dans le réacteur avant neutralisation.

**Corrigé.** Premier passage : PhNO₂+2H⁺+2e⁻→PhNO+H₂O. Deuxième : PhNO+2H⁺+2e⁻→PhNHOH. Troisième : PhNHOH+2H⁺+2e⁻→PhNH₂+H₂O. L’addition annule PhNO et PhNHOH, espèces produites puis consommées, et donne PhNO₂+6H⁺+6e⁻→PhNH₂+2H₂O. Chaque étape conserve N, O, H et charge : par exemple 2H⁺+2e⁻ apporte une charge nulle. Le métal choisi fournit le flux d’électrons selon sa demi-équation propre. En milieu acide, PhNH₂ peut ensuite recevoir H⁺ et former PhNH₃⁺ ; ce transfert de proton n’est pas une réduction supplémentaire du N. Une neutralisation permet de récupérer l’aniline libre. Supprimer l’eau du bilan global perdrait les deux O du groupe nitro initial.

### Problème complémentaire 18 — Aromatique à quatre groupes : planifier avant de nitrer

*Spé — PC* · laboratoire `nitrobenzene`.

**Énoncé.** On cherche une cible portant COCH₃ en C1, Br en C4, NO₂ en C5 et Cl en C3. Partir du bromobenzène : proposer un ordre acylation/nitration/chloration, repérer les convergences d’orientation et expliquer quelles données manquent encore pour déclarer une synthèse sélective à rendement élevé.

**Corrigé.** Acyler le bromobenzène avant d’installer NO₂ permet d’envisager la Friedel–Crafts usuelle ; choisir ou isoler l’acylé para place COCH₃ en C1 et Br en C4. COCH₃ dirige ensuite méta (C3/C5) tandis que Br dirige ortho (C3/C5), donc les deux effets convergent pour une nitration dans cette paire symétrique. Une fois NO₂ en C5, la chloration doit être réévaluée : les groupes présents modifient simultanément orientation, vitesse et complexation, et C3 est une position à discuter pour la cible. Cette carte de direction ne démontre pas un produit unique. Conditions de nitration/chloration, proportions, séparations et compatibilité du catalyseur sont nécessaires. Nitrer d’abord un noyau puis imposer une Friedel–Crafts classique échoue au filtre de réactivité sur un aromatique fortement désactivé. Le laboratoire représente une route plausible et une route bloquée, sans inventer un rendement.

### Problème complémentaire 19 — Trois dinitrobenzènes : dériver les trois normes

*Sup → PC* · laboratoire `dipolesnitro`.

**Énoncé.** Dans un hexagone régulier, deux dipôles de norme μ₀=4,03 D suivent les directions substituées. Calculer les normes de la somme pour ortho, méta et para par produit scalaire. Donner les valeurs en Debye et expliquer pourquoi l’angle 120° ne doit pas être appliqué indistinctement aux trois isomères.

**Corrigé.** Pour deux vecteurs μ₁ et μ₂, |μ₁+μ₂|²=|μ₁|²+|μ₂|²+2μ₁·μ₂=2μ₀²(1+cosθ). Les directions radiales des substituants sont séparées de 60° en ortho, 120° en méta et 180° en para. On obtient respectivement √3μ₀≈6,98 D, μ₀=4,03 D et 0 D. L’angle de valence local dans un C aromatique est voisin de 120°, mais ce n’est pas l’écart entre deux dipôles situés à des positions différentes du cycle. Une rotation commune de la molécule modifie les composantes et conserve la norme. Le cas para annule deux vecteurs égaux opposés ; les liaisons locales restent polaires. Ces résultats supposent deux contributions inchangées par la seconde substitution et une géométrie idéale, donc sont un modèle annoncé plutôt qu’une table universelle de mesures.

### Problème complémentaire 20 — Propriété d’un isomère et composition d’un mélange

*Spé — PC* · laboratoire `dipolesnitro`.

**Énoncé.** On connaît les trois moments dipolaires idéalisés ortho/méta/para d’un dinitrobenzène. Peut-on en déduire les proportions de la nitration ? Une mesure unique de réponse d’un mélange suffirait-elle ? Formuler les informations indépendantes qu’une résolution inverse exige.

**Corrigé.** Les moments de trois espèces pures ne fournissent aucune fraction de produit : les fractions résultent des flux réactionnels et des conditions. Même une réponse mesurée du mélange doit être reliée à une loi physique donnée ; on ne peut supposer qu’elle est une moyenne linéaire des normes des vecteurs. Si une telle moyenne linéaire était explicitement postulée, elle donnerait une équation xₒμₒ+xₘμₘ+xₚμₚ=μmes, plus xₒ+xₘ+xₚ=1. Il resterait en général un degré de liberté pour trois fractions, sous contraintes de positivité ; il faudrait une mesure ou donnée indépendante supplémentaire. D’autres techniques peuvent distinguer les espèces avec leurs lois de réponse propres. Le calcul vectoriel caractérise une géométrie moléculaire tandis que la sélectivité de nitration exige un mécanisme ou des données expérimentales : il faut conserver cette séparation dans le raisonnement.

### Problème complémentaire 21 — E2 SS/RR : obtenir E sans échanger les substituants

*Spé — PC* · laboratoire `e2stereo`.

**Énoncé.** Pour (3S,4S)-3-bromo-3,4-diméthylhexane, sélectionner l’élimination de Br en C3 et H en C4. Construire une projection anti, attribuer E/Z du produit et traiter l’énantiomère RR. Expliquer pourquoi une permutation de deux groupes de Newman n’est pas une rotation permise.

**Corrigé.** On regarde C3–C4 en conservant les trois groupes attachés à chacun de ces C. Une rotation de la liaison aligne H4 anti à Br, sans modifier S/S. L’E2 consomme C3–Br et C4–H et crée C3=C4. Sur chaque C vinylique, Et est prioritaire sur CH₃ : le rang suivant C,H,H dépasse H,H,H. Dans cette configuration les deux Et sont opposés, donc produit (E)-3,4-diméthylhex-3-ène. L’énantiomère RR donne son image miroir, superposable au même alcène E, car les centres C3/C4 sont devenus trigonal-plans. Permuter deux groupes sur un seul C changerait sa configuration et fabriquerait un autre réactif, alors qu’une rotation propre conserve l’ordre circulaire. Le dessin anti doit être obtenu par une opération géométrique licite, pas par déplacement opportuniste des étiquettes.

### Problème complémentaire 22 — E2 SR/RS : Z pour une voie, pas exclusion de toutes les autres

*Spé — PC* · laboratoire `e2stereo`.

**Énoncé.** Reprendre l’élimination C3–C4 du 3-bromo-3,4-diméthylhexane pour les configurations SR et RS. Comparer à SS/RR, puis lister les autres types de Cβ voisins de C3. Quelle conclusion sur la proportion Z/E ou les régioisomères dépasse les seules données de stéréospécificité ?

**Corrigé.** En gardant la configuration SR ou RS et en plaçant H4 et Br anti par une rotation propre, les Et prioritaires se trouvent du même côté après formation C3=C4 : la voie choisie donne le (Z)-3,4-diméthylhex-3-ène. SS/RR donne E sous cette même contrainte de voie, ce qui démontre la stéréospécificité. C3 est aussi voisin de C2 et d’un groupe méthyle : leurs H peuvent conduire à des doubles liaisons de connectivités différentes si des géométries réactives sont accessibles. Ni la relation SR→Z ni la règle de Zaïtsev ne quantifie leurs flux. Il faudrait populations des conformères, barrières, base, milieu et température ou données mesurées pour prédire la distribution. Enfin le rapport E/Z d’un mélange de réactifs dépend aussi de leur composition initiale ; on ne peut attribuer un pourcentage depuis une seule formule de départ.

### Problème complémentaire 23 — Époxyder E ou Z : trans/cis, puis compter les O

*Sup → PC* · laboratoire `epoxydes`.

**Énoncé.** Comparer l’époxydation de (E)- et (Z)-but-2-ène par un peracide. Dessiner la relation des méthyles dans les produits et écrire le coproduit. Comparer ensuite au bilan industriel d’éthylène/O₂/Ag ; pourquoi ne doit-on pas promettre la même voie catalytique pour tous les alcènes ?

**Corrigé.** Le peracide livre un seul O pontant aux deux C de C=C dans une opération concertée : la relation E mène aux méthyles trans sur le cycle époxyde, la relation Z aux méthyles cis. Les deux faces d’attaque doivent être discutées selon la symétrie du produit ; un milieu achiral ne favorise pas spontanément un énantiomère. Le coproduit est RCO₂H, ce qui conserve les autres O et le groupe acyle du peracide. Pour l’éthylène dans le procédé à l’argent, 2C₂H₄+O₂→2C₂H₄O équilibre l’oxygène moléculaire. Ce bilan est une banque industrielle spécifique et ne démontre pas toutes les étapes de catalyse, ni l’absence de combustion ou autres oxydations. Substrat, catalyseur et conditions de sélectivité sont indispensables avant de généraliser cette voie à un alcène substitué.

### Problème complémentaire 24 — Ouvrir le même époxyde avec MeO⁻ ou MeOH/H⁺

*Spé — PC* · laboratoire `epoxydes`.

**Énoncé.** Pour l’oxyde de propylène, comparer MeO⁻ en base puis protonation et MeOH en milieu acide. Localiser l’attaque, l’O resté dans le squelette et le groupe OH final. Expliquer pourquoi écrire MeO⁻ en présence d’un excès d’acide masque le rôle réel du nucléophile.

**Corrigé.** En base, le méthoxyde attaque à l’arrière le CH₂ le moins encombré ; la liaison de ce C à l’O du cycle se rompt, et l’O initial reste sur le C secondaire. Après protonation, on obtient CH₃–CH(OH)–CH₂OMe. Dans la banque acide, l’époxyde est d’abord protoné et MeOH neutre attaque préférentiellement le C secondaire ; l’O initial reste sur le CH₂ et, après déprotonation, le produit est CH₃–CH(OMe)–CH₂OH. L’attaque est arrière avec inversion géométrique au C ciblé quand un centre stéréogène y est défini. MeO⁻ est rapidement protonné dans un milieu fortement acide : dessiner durablement la même forte base comme nucléophile libre y serait incohérent. Les deux régioisomères se distinguent par l’origine de chaque O, la rupture C–O choisie et les transferts de protons explicités.

## Sources et statut pédagogique

La lecture suit les pages ciblées du recueil fourni. Les programmes officiels, les références de définitions IUPAC et les sources institutionnelles de méthodes sont détaillés dans [COURS.md](COURS.md). PCSI puis PC/PC* constituent le parcours principal ; les réactions de banque accompagnée et les prolongements ne sont pas déclarés exigibles uniformément dans toutes les filières. Dans les niveaux au-delà, les thèmes sont proposés comme ouverture et ne sont pas promis par les calculs du laboratoire.
