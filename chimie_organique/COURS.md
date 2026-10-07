# Liaisons & Synthèses — chimie organique CPGE

42 leçons, 30 laboratoires et 60 exercices corrigés. Douze missions transversales se trouvent dans [PARCOURS.md](PARCOURS.md). Le repérage programme/recueil est dans [MATRICE_PROGRAMME.md](MATRICE_PROGRAMME.md).

L’atelier réinvestit l’extrait du recueil : outils électroniques, types de réactions, exemples et suites d’exemples, organomagnésiens, hydrogénation, hydroboration, acylation, énolates, aldol/crotonisation, Michael, Wittig, époxydes, orbitales et Diels–Alder. Les problèmes d’alcènes/alcynes et d’aromatiques deviennent des raisonnements sur conditions, produits, mécanismes et ordre de synthèse. Textes, dessins, simulations et corrigés sont originaux ; les pages du recueil ne sont pas redistribuées.

La progression vise principalement PCSI puis PC/PC*. Le tronc commun PCSI précède les approfondissements de l’option PC ; les chapitres organiques ne sont pas identiques dans toutes les autres filières. Les mentions Sup, PC et Au-delà indiquent le statut de l’outil, non une promesse que toutes les réactions de la réactiothèque sont exigibles sans données. Les transformations supplémentaires du recueil et les extensions numériques sont accompagnées d’une banque, de paramètres ou de règles fournies. Les programmes officiels de 2021 consultés et les sources primaires sont liés en fin de document.

Conventions : flèche pleine pour un doublet, demi-flèche pour un électron ; charges formelles en unités e et charges partielles δ distinctes. Les pKa d’une comparaison d’équilibre appartiennent au même solvant et aux mêmes conditions. Concentrations en mol·L⁻¹, quantités fréquemment en mmol, temps en s, énergies molaires en kJ·mol⁻¹ sauf orbitales en eV ; R=8,314 J·mol⁻¹·K⁻¹. RMN : δ en ppm, J en Hz et fréquence en MHz ; IR : nombre d’onde en cm⁻¹ et T=10⁻ᴬ. Chaque laboratoire expose ses hypothèses et distingue données mesurées, banques de réactions et modèles pédagogiques.

## 1. Lewis : faire parler les électrons avant les noms

*Sup — PCSI* — laboratoire `electrons`.

**Objets.** Une formule de Lewis indique liaisons, doublets non liants et charges formelles. C, N et O de la deuxième période suivent normalement l’octet dans les espèces usuelles ; un carbocation possède un carbone déficient à six électrons. Un radical porte un électron célibataire. Le nombre d’électrons de valence total doit intégrer la charge globale.

qformel = V − Nnonliants − Nliaisons  
Nélectrons = Σ Vatomes − charge globale (en unités e)  
C : V=4 ; N : V=5 ; O : V=6 ; H : V=1

**Calcul.** Dans CH₃OH, l’oxygène possède deux liaisons et quatre électrons non liants : qO=6−4−2=0. Dans CH₃OH₂⁺, trois liaisons et un doublet donnent qO=6−2−3=+1. Dans CH₃O⁻, une liaison et trois doublets donnent qO=6−6−1=−1. La protonation modifie donc aussi la disponibilité d’un doublet et le caractère du groupe partant.

**Exemple emblématique.** Dans un groupe nitro R−N(O)₂, les formes usuelles sont R−N⁺(=O)−O⁻ et R−N⁺(−O⁻)=O. N porte quatre liaisons et aucune paire libre. Elles décrivent une seule espèce délocalisée ; ni un N pentavalent de deuxième période ni deux molécules en équilibre ne sont nécessaires.

**Technique CPGE.** Compter les électrons, compléter les octets, calculer chaque charge puis vérifier que leur somme est la charge globale. Une formule topologique omet les C et les H liés aux C, mais elle n’autorise pas à omettre une charge ou un H labile indispensable au mécanisme.

## 2. Flèches courbes : une comptabilité qui construit le mécanisme

*Sup — PCSI* — laboratoire `electrons`.

**Convention.** Une flèche à deux pointes représente le déplacement d’un doublet. Son origine est un doublet ou une liaison ; sa pointe est un atome recevant la paire ou la liaison qui se forme. Une demi-flèche représente un électron dans un mécanisme radicalaire. Les flèches de réaction et de mésomérie ont d’autres rôles.

Nu:⁻ + C−X → Nu−C + X⁻  
B: + H−A → B−H⁺ + A⁻  
Σ charges et nombre de chaque atome conservés à chaque étape

**Dérivation.** Pour HO⁻+CH₃Br→CH₃OH+Br⁻, une flèche part d’un doublet de O vers C, une seconde de la liaison C−Br vers Br. La charge initiale −1 se retrouve sur Br. Dans l’addition à un carbonyle, l’attaque du C impose en même temps le déplacement des électrons π vers O, sinon le C dépasserait l’octet.

**Exemple.** Protoner un alcool : le doublet de O pointe vers le H d’un acide, dont la liaison H−A pointe vers A. Le nouvel oxonium possède une charge +1 et peut libérer H₂O. Dessiner seulement H⁺ au-dessus d’une flèche globale est insuffisant pour expliquer l’activation microscopique.

**Méthode.** Après chaque étape, redessiner les doublets et recalculer les charges, sans déplacer les noyaux dans une simple forme mésomère. Les réactions concertées peuvent comporter plusieurs flèches simultanées ; cela ne crée pas automatiquement un intermédiaire isolable.

## 3. Polarisation, effet inductif et polarisabilité

*Sup — PCSI* — laboratoire `electrons`.

**Grandeurs.** L’électronégativité χ compare l’attraction d’un atome pour les électrons d’une liaison. La charge partielle δ n’est pas une charge formelle entière. L’effet inductif se transmet par le squelette σ et diminue avec la distance. La polarisabilité mesure la déformation du nuage électronique et ne se confond pas avec χ.

χ(O)>χ(N)>χ(C)>χ(H) sur l’échelle de Pauling  
Cδ+−Oδ− ; Cδ−−Mgδ+  
μinduit = α E ; α : polarisabilité

**Application.** Dans un carbonyle, le C est électrophile ; dans un organomagnésien RMgX, le C lié à Mg est nucléophile et fortement basique. Un substituant CF₃ attire par effet −I ; les alkyles stabilisent souvent un carbocation par des interactions σ et hyperconjugaison. Le classement doit tenir compte aussi de la conjugaison.

**Exemple.** En eau, le pKa de l’acide chloroacétique est voisin de 2,9, celui de l’acide acétique de 4,8. Le Cl stabilise davantage le carboxylate par −I, donc favorise la dissociation. Pour comparer une série, conserver solvant et température ; les nombres sont ici des repères arrondis de lecture.

**Technique.** Séparer trois questions : où sont les sites polarisés, quel intermédiaire serait stabilisé, quelle réaction est réellement accessible ? Une flèche de dipôle ne donne ni une barrière d’activation ni une proportion de produits de synthèse.

## 4. Mésomérie : stabilisation et sites de réaction

*Sup → PC* — laboratoire `electrons`.

**Conditions.** La conjugaison demande des orbitales p ou des doublets correctement orientés. Les formes mésomères conservent positions des noyaux, connectivité σ, charge globale et nombre d’électrons. Leur poids peut être différent : elles ne sont pas nécessairement équiprobables et ne s’interconvertissent pas comme des isomères.

CH₂=CH−CH₂⁺ ↔ ⁺CH₂−CH=CH₂  
R−CO−CH₂⁻ ↔ R−C(O⁻)=CH₂  
−OR et −NR₂ : donneurs +M ; −NO₂, −CN, −COR : attracteurs −M

**Enolate.** L’énolate possède une charge distribuée entre O et le Cα. Il peut former une liaison C−C par attaque du C ou une liaison O−E par attaque de O. L’électrophile, le contre-ion, le solvant et la température interviennent : la seule forme au plus grand poids ne suffit pas à prédire toutes les sélectivités.

**Exemple.** Le doublet de l’azote d’une amide est délocalisé vers C=O : R−C(=O)−NH₂↔R−C(−O⁻)=NH₂⁺. Cela explique la faible basicité de l’azote, la planéité approximative et le caractère partiel de double liaison C−N. Le carbonyle d’amide est ainsi moins électrophile qu’un chlorure d’acyle.

**Technique.** Choisir d’abord le système conjugué, tracer une suite continue de flèches et distinguer stabilisation de réactif, d’intermédiaire et d’état de transition. Pour les halogènes aromatiques, −I et +M coexistent : désactivation et orientation ortho/para ne sont pas contradictoires.

## 5. Acides et bases : comparer dans un même solvant

*Sup — PCSI* — laboratoire `acidebase`.

**Cadre.** HA est un acide de Brønsted et B une base ; leurs formes conjuguées sont A⁻ et BH⁺. Les pKa fournis pour calculer un équilibre doivent correspondre au même solvant, à la même température et à des états standards compatibles. En eau diluée, concentrations et activités sont assimilées dans le TP.

HA + B ⇌ A⁻ + BH⁺  
K ≈ 10^\[pKa(BH⁺)−pKa(HA)\]  
\[A⁻\]/\[HA\] = 10^(pH−pKa) ; fA⁻ = 1/\[1+10^(pKa−pH)\]

**Démonstration.** Diviser Ka(HA) par Ka(BH⁺) fait disparaître l’activité du proton et donne K. Pour des réactifs équimolaires, sans produits initiaux et à volume constant, K=\[x/(c₀−x)\]² : la conversion est √K/(1+√K), distincte de K/(1+K) qui décrirait un rapport de deux formes à pH imposé.

**Exemple.** Acide acétique et NH₃ en eau : pKa=4,76 et 9,25, d’où K≈3,1×10⁴ et une conversion équimolaire ≈99,43 %. Un tampon acétate à pH=5,76 contient en revanche \[A⁻\]/\[HA\]=10 et 90,91 % de forme A⁻. Ces deux situations ne possèdent pas le même bilan.

**Stratégie.** Un carboxylique ou un alcool protonique détruit un organomagnésien par transfert de proton avant l’addition recherchée. Les pKa usuels de carbanions et d’énolates en solvants organiques sont fournis séparément ; on ne les soustrait pas à un pKa aqueux pour annoncer une constante précise.

## 6. Nucléophile, base et groupe partant : trois rôles

*Sup → PC* — laboratoire `acidebase`.

**Définitions.** Un nucléophile fournit une paire à un électrophile pour former une liaison. Une base de Brønsted capte un proton. La basicité est reliée à un équilibre ; la nucléophilie se compare à des constantes de vitesse envers un substrat donné. Un groupe partant reçoit les électrons d’une liaison rompue.

Basicité : K d’un transfert de H⁺ ; nucléophilie : k d’une attaque  
Alcool ROH → oxonium ROH₂⁺ : départ de H₂O facilité  
I⁻, Br⁻, Cl⁻, sulfonates : groupes partants usuels ; HO⁻ : mauvais départ non activé

**Solvant.** Un solvant protique peut solvater fortement un petit anion par liaisons hydrogène et ralentir son attaque. Dans un solvant polaire aprotique, la disponibilité d’un anion peut croître. Les effets de solvant sur ionisation, nucléophile, contre-ion et solubilité doivent être considérés ensemble.

**Exemple.** tert-BuO⁻ est une base forte encombrée : sur un halogénoalcane secondaire, l’élimination est souvent favorisée par rapport à une SN2. I⁻ peut être un bon nucléophile tout en étant une base faible. Dire « base forte donc bon nucléophile » ne résout pas cette comparaison.

**Technique.** Identifier les deux sites concurrents : C électrophile pour substitution, Hβ pour élimination. Justifier le choix avec classe du substrat, encombrement, qualité de départ, solvant et température. Le laboratoire compare des paramètres cinétiques annoncés, pas une table universelle de rendement.

## 7. Configuration R/S : construire les priorités CIP

*Sup — PCSI* — laboratoire `stereo`.

**Objets.** Un centre tétraédrique portant quatre groupes différents est stéréogène. Pour CIP, classer les atomes directement liés par numéro atomique, puis comparer les listes d’atomes du premier rang différent dans l’ordre décroissant. Une liaison multiple se traite avec des atomes dupliqués dans cette règle.

Acide lactique CH₃−CH(OH)−CO₂H : OH > CO₂H > CH₃ > H  
Priorité 4 à l’arrière : 1→2→3 horaire = R, antihoraire = S  
ee = |nR−nS|/(nR+nS) ; xmajoritaire = (1+ee)/2

**Pourquoi.** Les groupes CO₂H et CH₃ commencent tous deux par C ; au rang suivant, le C carboxylique donne \[O,O,O\], le méthyle \[H,H,H\]. L’oxygène porte donc la première priorité, le carboxyle la deuxième. Tourner tout le modèle dans l’espace ne modifie pas R/S ; permuter deux groupes le modifie.

**Exemple.** Un mélange contenant 80 % R et 20 % S possède ee=60 %. Si, aux conditions données, l’énantiomère R pur a αpur=+12°, le mélange idéal donne α=+7,2°. Aucune règle ne relie R au signe + en général ; celui-ci est une propriété mesurée à longueur d’onde, température et solvant donnés.

**Piège.** L’inversion de Walden est géométrique. Si une réaction modifie aussi le classement CIP des substituants, l’étiquette R peut parfois rester R malgré l’inversion. Le TP affiche les priorités de son exemple ; il ne prétend pas attribuer CIP à toute molécule dessinée.

## 8. E/Z, énantiomères et composés méso

*Sup — PCSI* — laboratoire `stereo`.

**Double liaison.** E/Z compare le groupe de priorité CIP la plus élevée sur chacun des deux C de C=C. E signifie côtés opposés, Z même côté. Chaque C doit porter deux substituants différents : le propène CH₂=CH−CH₃ ne possède pas de configuration E/Z.

E : priorités hautes opposées ; Z : priorités hautes du même côté  
2 centres distincts ⇒ au plus 2²=4 configurations  
Acide tartrique : (R,R), (S,S), et forme méso (R,S)≡(S,R)

**Chiralité.** Des énantiomères sont images dans un miroir non superposables ; des diastéréoisomères ne sont pas cette paire miroir. Une molécule à centres stéréogènes peut être achirale si sa symétrie rend l’image miroir superposable. Le nombre 2ⁿ est une borne et doit être corrigé pour les symétries.

**Exemple.** Le but-2-ène E et Z est un couple de diastéréoisomères. Une bromation anti stéréospécifique de E-but-2-ène donne le 2,3-dibromobutane méso ; Z-but-2-ène donne un mélange racémique (R,R)/(S,S) dans un milieu achiral. Deux énantiomères comptent deux structures, même si une RMN en solvant achiral les superpose.

**Technique.** Dessiner les produits en trois dimensions avant de leur attribuer un nom. Distinguer stéréospécificité, qui relie des réactifs stéréoisomères à des produits distincts, et stéréosélectivité, qui favorise un stéréoisomère parmi les possibles.

## 9. Newman et Boltzmann : les conformères ont une population

*Sup → PC* — laboratoire `conformeres`.

**Angle.** La projection de Newman regarde une liaison C−C suivant son axe. Pour le butane, θ désigne l’angle dièdre entre les deux groupes CH₃ : anti à 180°, gauche à ±60°, éclipsé à 0° ou ±120°. Une rotation autour d’une liaison σ change la conformation, pas la constitution ni normalement R/S.

pi = gi exp(−ΔGi/RT) / Σj gj exp(−ΔGj/RT)  
Modèle discret : Ganti=0 ; Ggauche=3,8 kJ·mol⁻¹ ; ganti=1, ggauche=2  
À 298 K : Panti≈0,699 ; Pgauche,total≈0,301

**Calcul.** RT≈2,478 kJ·mol⁻¹, donc exp(−3,8/RT)≈0,216. La fonction de partition réduite vaut 1+2×0,216=1,432. Le facteur 2 représente deux minima gauche, pas deux fois l’énergie. Les ΔG fournis dans ce modèle regroupent les corrections entropiques que l’on ignore dans une seule courbe torsionnelle d’énergie.

**Lien réaction.** Si seule une conformation rare est réactive, son taux de population peut diminuer la vitesse apparente. Cependant un produit majoritaire ne correspond pas nécessairement au conformère majoritaire : il faut aussi connaître les barrières d’attaque et la vitesse d’échange entre conformères.

**Technique.** Repérer minima et barrières, préciser si le calcul utilise une énergie ou une énergie libre, compter la dégénérescence. Une courbe continue de torsion et un modèle à trois minima ne définissent pas exactement la même moyenne statistique.

## 10. Cyclohexane : chaises, axial/équatorial et E2

*Sup → PC* — laboratoire `conformeres`.

**Géométrie.** La chaise du cyclohexane évite l’éclipse des liaisons et maintient des angles proches du tétraèdre. Chaque C possède une liaison axiale et une équatoriale. Un basculement de chaise échange axial et équatorial tout en conservant le caractère haut/bas et donc cis/trans.

Méthylcyclohexane : ΔGax−eq≈7,5 kJ·mol⁻¹, valeur pédagogique  
Péquatorial = 1/\[1+exp(−ΔGax−eq/RT)\] ≈ 95,4 % à 298 K  
E2 dans une chaise : C−X axial et Cβ−H axial opposé

**Conformation.** Un groupe axial subit des interactions 1,3-diaxiales ; un groupe volumineux favorise souvent la position équatoriale. Pour plusieurs substituants, on compare les contraintes simultanées des deux chaises. Le tert-butyle peut servir de verrou conformationnel approximatif.

**Exemple.** Pour trans-1-bromo-2-méthylcyclohexane, une chaise est diaxiale, l’autre diéquatoriale. La chaise réactive place Br axial mais CH₃ occupe le site axial voisin en C2 : il n’y a pas de H axial anti sur C2. L’élimination doit alors utiliser le H anti de C6, même si l’alcène obtenu est moins substitué.

**Technique.** Dessiner les Hβ plutôt que déduire le produit de la seule règle de Zaitsev. Les règles de stabilité donnent une tendance entre voies permises ; la contrainte stéréoelectronique peut supprimer la voie qui serait autrement préférée.

## 11. Formule brute, insaturation et spectrométrie de masse

*Sup → PC* — laboratoire `formule`.

**Cadre.** L’indice d’insaturation IHD s’applique aux formules neutres usuelles à valences C4, N3, H1 et halogènes X1. O et S divalents n’interviennent pas dans cette expression. La masse moyenne molaire et la masse exacte monoisotopique sont deux grandeurs différentes ; m/z dépend de l’ion observé et de sa charge.

IHD = (2C+2+N−H−X)/2  
cycle : 1 ; C=C ou C=O : 1 ; C≡C : 2  
1 Cl : M:M+2≈3:1 ; 1 Br : M:M+2≈1:1

**Exemple.** C₈H₈O₂ donne IHD=(16+2−8)/2=5. Un noyau benzénique en consomme quatre, un carbonyle un : cela admet l’acide phénylacétique, le benzoate de méthyle et d’autres isomères. La formule seule ne les départage pas. C₆H₅Br donne IHD=4 en remplaçant le Br par un H dans le comptage.

**Isotopes.** Pour deux Cl, le développement (3+x)² donne une enveloppe approximative 9:6:1 aux masses M,M+2,M+4. Pour deux Br, (1+x)² donne 1:2:1. Les proportions réelles dépendent des abondances naturelles et de la superposition avec ¹³C ; le TP sépare cette enveloppe pédagogique des fragments chimiques.

**Technique.** Identifier d’abord M⁺·, \[M+H\]⁺ ou un autre ion selon l’ionisation, puis vérifier l’IHD entier et non négatif, les atomes et la cohérence de toutes les données. Un pic intense n’est pas automatiquement l’ion moléculaire.

## 12. Infrarouge : des vibrations au diagnostic fonctionnel

*Sup — PCSI option PC* — laboratoire `ir`.

**Grandeurs.** Le nombre d’onde ṽ est en cm⁻¹ ; une fréquence s’obtient par ν=cṽ avec c exprimé en cm·s⁻¹. Un mode IR actif fait varier le moment dipolaire. La transmittance T=I/I₀ est une fraction ; l’absorbance A=−log₁₀T s’additionne pour les espèces indépendantes.

ṽ = \[1/(2πc)\]√(k/μ) ; μ=m₁m₂/(m₁+m₂)  
A=εℓc ; T=10^(−A)  
C=O souvent 1650–1800 cm⁻¹ ; OH lié : bande large souvent 3200–3600 cm⁻¹

**Dérivation.** Dans un modèle à deux masses et ressort, la coordonnée relative obéit à μq″+kq=0. Une liaison plus raide élève la fréquence ; une masse réduite plus grande l’abaisse. La conjugaison réduit souvent le caractère local de double liaison C=O et son nombre d’onde, sans que cela constitue une loi indépendante du groupe fonctionnel.

**Exemple.** Passer de OH à OD à constante k égale donne ṽOD/ṽOH≈√(μOH/μOD)≈0,728. Une bande OH à 3400 cm⁻¹ devient vers 2475 cm⁻¹ dans cette approximation. A=0,30 correspond à T≈0,501 ; doubler la concentration donne A=0,60 et T≈0,251, pas la moitié de 0,501.

**Diagnostic.** Comparer présence et absence de OH, C=O, NH et CN, puis la région d’empreinte. Les courbes du TP sont des bandes pédagogiques calculées ; une identification expérimentale demande un spectre mesuré et ses conditions, comme les références institutionnelles NIST.

## 13. RMN du proton : déplacements, intégrales et couplages

*Sup — PCSI option PC* — laboratoire `rmn`.

**Grandeurs.** Le déplacement chimique δ=(ν−νréf)/ν₀×10⁶ est en ppm ; J est une constante de couplage en Hz. Les intégrales de massifs, acquises quantitativement, sont proportionnelles au nombre de noyaux. Des protons chimiquement et magnétiquement équivalents ne se dédoublent pas entre eux dans le modèle usuel.

Δν en Hz = Δδ en ppm × ν₀ en MHz  
Premier ordre : Δν/J ≫ 1  
n voisins équivalents spin 1/2 ⇒ n+1 raies, intensités binomiales

**Exemple.** Pour CH₃COOCH₂CH₃, on attend approximativement un singulet 3H vers 2,0 ppm, un quartet 2H vers 4,1 ppm et un triplet 3H vers 1,25 ppm. Le groupe éthyle possède le même J≈7 Hz dans ses deux massifs. À 400 MHz, 7 Hz correspondent à 0,0175 ppm : le couplage ne devient pas 7 ppm.

**Limites.** Deux déplacements séparés de 0,02 ppm à 60 MHz donnent Δν=1,2 Hz : pour J=7 Hz, le premier ordre échoue. À 600 MHz, Δν=12 Hz reste comparable à J. Une augmentation du champ améliore souvent la séparation mais ne garantit pas que toute molécule devienne AX.

**Technique.** Lier chaque intégrale à un nombre d’H, chaque J à une connectivité et chaque δ à un environnement. OH/NH peuvent échanger et ne suivent pas toujours n+1. Le ¹³C découplé fournit un nombre d’environnements ; ses hauteurs ne sont pas généralement des intégrales quantitatives du nombre de C.

## 14. Résoudre une structure par plusieurs données indépendantes

*Sup → PC* — laboratoire `ir`.

**Méthode.** Une caractérisation convaincante croise formule brute, insaturation, IR, RMN et contexte de synthèse. Chaque mesure élimine des structures ; aucune signature isolée ne doit remplacer le bilan complet. UV-visible renseigne notamment sur des transitions électroniques et sur une conjugaison, mais n’attribue pas seul la connectivité.

C₄H₈O₂ : IHD=1 ; M≈88,1 g·mol⁻¹  
IR C=O d’ester + RMN 3H s / 2H q / 3H t ⇒ CH₃COOCH₂CH₃  
Etransition=hc/λ ; λ=300 nm ⇒ E≈4,13 eV

**Raisonnement.** L’IHD=1 autorise carbonyle, cycle ou alcène. L’IR d’ester retient un carbonyle et un lien C−O. La paire quartet/triplet 2H/3H place un groupe éthyle ; son CH₂ vers 4 ppm indique O−CH₂. Le singulet restant 3H se place sur CO−CH₃. Le propanoate de méthyle aurait un OCH₃ singulet et un CH₂ plus proche de 2,3 ppm.

**Sélectivité.** Réduire une cétone insaturée peut modifier C=O seul ou aussi C=C selon le réducteur. Disparition du C=O en IR, apparition de CH−OH et maintien des protons vinyliques en RMN justifient une réduction 1,2 chimiosélective ; la disparition d’une tache de CCM ne suffit pas à l’établir.

**Au-delà guidé.** COSY recherche des corrélations de couplage, HSQC des corrélations ¹H−¹³C à une liaison, HMBC à plus longue distance. Ce sont des extensions introduites avec leurs règles ; leur connaissance n’est pas supposée pour les exercices de base.

## 15. CCM : voir une séparation, suivre une transformation

*Sup — TP PCSI* — laboratoire `ccm`.

**Montage.** Sur silice en phase normale, la phase stationnaire est polaire. Rf est le rapport distance centre de tache/distance front depuis la même ligne de dépôt. Il dépend de la plaque, de l’éluant, de la charge déposée et des conditions. Une valeur n’est pas une constante d’identité absolue.

Rf = dsubstance/dfront ; 0≤Rf≤1  
Rf≈1/(1+k′) dans un modèle de rétention simplifié  
Résolution qualitative : comparer ΔRf aux largeurs des taches

**Solvant.** Augmenter la force éluante en phase normale diminue souvent la rétention sur silice et élève les Rf. Si toutes les taches restent au dépôt ou courent avec le front, la séparation est peu informative. Les gradients du laboratoire simulent une réponse explicitement paramétrée, pas un calcul ab initio d’adsorption.

**Exemple.** Front à 60 mm et tache à 24 mm donnent Rf=0,40. Deux taches à 24 et 27 mm, chacune large de 5 mm, ne sont pas nettement séparées. Une co-tache référence+produit est utile, mais deux molécules différentes peuvent migrer ensemble dans un éluant donné.

**TP.** Prélever une aliquote, arrêter ou diluer sa réaction si nécessaire, déposer peu, comparer réactif et produit avec des références. L’intensité révélée peut varier avec le chromophore et la révélation : elle n’est pas automatiquement un rendement ni une concentration étalonnée.

## 16. Extraction : séparer par partage et par pH

*Sup — TP PCSI* — laboratoire `extraction`.

**Définitions.** P=\[S\]org/\[S\]aq désigne le partage de la forme neutre à l’équilibre. D est le rapport des concentrations totales dans les deux phases. Pour un acide faible, la forme ionisée reste supposée aqueuse ; un pH maintenu par tampon fixe la fraction neutre. Volumes en mL doivent être employés de façon cohérente dans les rapports.

Acide HA : D=P/\[1+10^(pH−pKa)\]  
Base B : D=P/\[1+10^(pKa(BH⁺)−pH)\]  
Fraction aqueuse après n extractions : q=\[Vaq/(Vaq+D Vorg/n)\]ⁿ

**Démonstration.** Une conservation n₀=CaqVaq+CorgVorg et Corg=DCaq donne q=Vaq/(Vaq+DVorg). Répéter avec du solvant neuf multiplie les fractions résiduelles. L’expression n suppose des contacts indépendants, équilibre atteint, volumes constants et absence de dégradation ou d’émulsion.

**Exemple.** Avec D=5, Vaq=100 mL et 100 mL de solvant total, une extraction laisse 1/6=16,7 % ; deux de 50 mL laissent (1/3,5)²=8,16 %. Un acide de pKa=4,5 et P=10 à pH=6,5 a D≈0,099 : il demeure principalement aqueux. À pH=2,5, D≈9,90.

**Technique.** Identifier la phase supérieure par la densité mesurée ou fournie, pas par le mot organique. Une extraction acido-basique transforme une espèce pour modifier D, puis peut la régénérer. Le modèle à pH imposé doit être complété par un bilan de protons si le milieu n’est pas tamponné.

## 17. SN2 : attaque arrière et cinétique bimoléculaire

*Sup — PCSI* — laboratoire `sn2`.

**Mécanisme.** Nu attaque le C porteur du groupe partant du côté opposé à C−X. Formation C−Nu et rupture C−X sont concertées ; l’état de transition n’est pas un carbocation. La trajectoire met en jeu le recouvrement du doublet nucléophile avec l’orbitale antiliante σ* C−X.

v=k₂\[RX\]\[Nu\] ; k₂ en L·mol⁻¹·s⁻¹  
Nu en grand excès : \[RX\](t)≈\[RX\]₀ exp(−k₂\[Nu\]₀t)  
Inversion géométrique au centre réactif (Walden)

**Exemple.** Avec k₂=0,20 L·mol⁻¹·s⁻¹ et \[Nu\]₀=0,50 mol·L⁻¹ maintenu presque constant, kobs=0,10 s⁻¹ et t₁/₂=6,93 s. Doubler \[Nu\] divise ce temps par deux. L’approximation doit être vérifiée en comparant \[RX\]₀ à \[Nu\]₀, et ne découle pas du seul nom SN2.

**Réactivité.** Méthyle et C primaires peu encombrés sont favorables ; un C tertiaire est inaccessible à la SN2 usuelle. Un groupe néopentyle est primaire mais fortement gêné au voisinage. Un carbone sp² d’halogénure aryle ou vinylique ne suit pas cette attaque SN2 alkyle ordinaire.

**Application.** La synthèse de Williamson forme un éther par RO⁻+R′X→ROR′+X⁻. Placer le groupe alkyle le moins encombré sur R′X limite E2 ; utiliser un halogénure tertiaire pour préparer un éther très encombré par cette route conduit surtout à une élimination.

## 18. SN1 : ioniser, piéger et parfois réarranger

*Sup — PCSI* — laboratoire `sn1`.

**Étapes.** Dans le schéma limite, une ionisation lente RX→R⁺+X⁻ précède une attaque rapide puis, si Nu est neutre, une déprotonation. Les carbocations allyliques, benzyliques et tertiaires sont souvent mieux stabilisés que des primaires. Un solvant ionisant facilite la séparation des charges.

Si ionisation irréversible déterminante : v=k₁\[RX\]  
\[RX\](t)=\[RX\]₀exp(−k₁t) ; t₁/₂=ln2/k₁  
Carbocation plan : deux faces accessibles ; paire d’ions possible

**Stéréochimie.** Un carbocation libre plan, attaqué de façon symétrique en milieu achiral, donne un racémique lorsqu’un seul nouveau centre est formé. Une paire d’ions ou un environnement chiral peut différencier les faces. La perte de configuration n’impose donc pas une proportion 50/50 pour chaque solvolyse réelle.

**Exemple.** Pour k₁=0,015 s⁻¹, t₁/₂≈46,2 s et la fraction restante à 120 s vaut exp(−1,8)≈16,5 %. Ajouter un nucléophile peut modifier la capture et la distribution de produits sans modifier la vitesse limite d’ionisation ; des mécanismes concurrents peuvent cependant changer la loi observée.

**Technique.** Séparer la formation du carbocation de sa capture, examiner une migration d’hydrure ou d’alkyle vers un cation plus stable, et confronter vitesse, produits et stéréochimie. Une loi de premier ordre constitue un indice, pas la preuve unique d’un mécanisme.

## 19. Compétition substitution/élimination : les vitesses sélectionnent

*Sup → PC* — laboratoire `competition`.

**Modèle.** Quatre issues consomment un même substrat S : SN1, E1, SN2, E2. L’ionisation peut être commune à SN1/E1 : on compte alors une seule vitesse d’ionisation, répartie ensuite entre capture et élimination. En conditions pseudo-premier ordre et sans interconversion des produits, les taux apparents λi de chemins indépendants s’additionnent. Le laboratoire règle des constantes déclarées ; une dépendance en température est étudiée dans le laboratoire Cinétique.

d\[S\]/dt=−(Σλi)\[S\] ; Pi(t)=\[S\]₀ λi/(Σλi)\[1−exp(−Σλi t)\]  
Fraction du produit i = λi/Σλi  
k=A exp(−Ea/RT) ; A porte les unités de k

**Exemple.** Si λSN2=0,06 s⁻¹ et λE2=0,02 s⁻¹, la sélectivité de substitution vaut 75 %, quelle que soit la conversion dans ce modèle. À t=20 s, la conversion est 1−exp(−1,6)=79,8 %, mais la quantité de produit SN2 représente 59,9 % du substrat initial. Conversion et sélectivité ne sont pas interchangeables.

**Règles contextualisées.** Un nucléophile peu encombré sur un primaire favorise souvent SN2 ; une base encombrée et un substrat secondaire/tertiaire favorisent E2 ; un substrat pouvant ioniser ouvre SN1/E1. Chauffer peut favoriser certaines éliminations, mais une conclusion quantitative exige les paramètres d’activation ou des mesures.

**Technique.** Déterminer l’ordre expérimental, proposer les voies compatibles, écrire leurs produits et tester le bilan de matière. Un modèle de chemins parallèles est une étude contrôlée de causalité ; ses pourcentages ne sont pas des rendements prédits pour tout réactif commercial.

## 20. E2 : trois mouvements concertés et une géométrie anti

*Sup — PCSI* — laboratoire `elimination`.

**Étape.** Une base arrache Hβ, les électrons Cβ−H forment Cα=Cβ et la liaison Cα−X se rompt vers X. Les trois mouvements sont simultanés. Le recouvrement orbital est favorable lorsque Cβ−H et Cα−X sont anti-périplanaires ; syn peut être imposé dans certains systèmes particuliers.

v=kE2\[RX\]\[B\] ; Δdièdre(Hβ−Cβ−Cα−X)≈180°  
Base peu encombrée : tendance Zaitsev si les voies sont permises  
Base encombrée : produit moins substitué parfois favorisé (Hofmann)

**Exemple.** Le 2-bromobutane peut produire but-1-ène et E/Z-but-2-ène. Des conformations anti différentes donnent les différents alcènes ; E-but-2-ène est souvent favorisé avec une petite base. Une population de conformères et des barrières distinctes sont nécessaires pour chiffrer les proportions.

**Stéréospécificité.** Sur une chaîne portant deux centres, choisir le H anti impose une configuration de l’alcène. Sur cyclohexane, l’exigence devient trans-diaxiale et peut contredire une simple prévision de stabilité. Les atomes H implicitement omis doivent être réintroduits dans le dessin.

**Technique.** Repérer tous les Cβ possédant un H, construire les Newman ou les chaises, éliminer les voies géométriquement interdites, puis comparer les voies restantes. Un alcène sans substituants différents sur chacun des C ne reçoit pas de descripteur E/Z.

## 21. E1 et déshydratation : stabilité et catalyse acide

*Sup → PC* — laboratoire `elimination`.

**Étapes.** Pour un alcool pouvant former un cation stabilisé, protonation de OH facilite le départ de H₂O, puis une base enlève Hβ et donne l’alcène. Le proton est régénéré : l’acide est catalyseur. Un alcool primaire suit souvent une élimination concertée en milieu acide plutôt qu’un carbocation primaire libre.

ROH + H⁺ ⇌ ROH₂⁺ → R⁺ + H₂O → alcène + H⁺  
E1 et SN1 peuvent partager un intermédiaire  
Un catalyseur abaisse les barrières et ne change pas K à température fixée

**Réarrangement.** Une migration de H⁻ ou d’un groupe alkyle au sein du cation peut déplacer le site de charge et donc le squelette du produit. Elle doit être écrite avant l’élimination ou la capture. Le mécanisme E2, sans cation libre, ne permet pas cette même migration intermédiaire.

**Exemple.** La déshydratation de 2-méthylbutan-2-ol donne notamment 2-méthylbut-2-ène et 2-méthylbut-1-ène. Le plus substitué est souvent favorisé dans ces conditions, mais retirer l’eau, la température et les équilibres entre alcènes peuvent changer le résultat final.

**Technique.** Écrire l’activation et les transferts de protons, vérifier la régénération du catalyseur et distinguer vitesse de formation et composition à l’équilibre. Une règle de stabilité sans mécanisme ne permet pas de prédire un squelette réarrangé.

## 22. Profils d’énergie : contrôle cinétique et thermodynamique

*Sup option PC → PC* — laboratoire `cinetique`.

**Conventions.** Un profil G(q) utilise une coordonnée réactionnelle abstraite q, distincte du temps. Un maximum est un état de transition, un minimum interne un intermédiaire. ΔG° compare produits et réactifs ; ΔG‡ compare l’état de transition au réactif de l’étape. Toutes les énergies libres sont ici molaires en kJ·mol⁻¹.

K=exp(−ΔG°/RT)  
k≈κ(kBT/h)exp(−ΔG‡/RT), forme d’Eyring (prolongement)  
Rapport cinétique kA/kB≈exp\[−(ΔG‡A−ΔG‡B)/RT\] si préfacteurs comparables

**Exemple.** À 298 K, un produit A accessible par une barrière plus basse de 5,0 kJ·mol⁻¹ se forme environ 7,5 fois plus vite que B si les préfacteurs sont égaux. Si B est plus stable de 8,0 kJ·mol⁻¹, l’équilibre favorise pourtant B/A≈25. Il faut une possibilité de réversibilité et un temps suffisant pour atteindre cet équilibre.

**Intermédiaires.** Dans S→I→P, une faible accumulation de I peut permettre l’approximation d’état quasi stationnaire d\[I\]/dt≈0, après un régime initial. L’étape dont la barrière locale est la plus élevée n’est pas automatiquement la déterminante globale si le réactif de cette étape est très rare.

**Technique.** Dessiner un bilan énergétique cohérent avec le mécanisme, comparer barrières et profondeurs, choisir un observable temporel puis tester conservation et réversibilité. Les animations ne font pas traverser une barrière à une molécule comme un wagon mécanique.

## 23. Alcènes : orientation, bromonium et hydroboration

*PC ; premières lectures accompagnées en Sup* — laboratoire `alcene`.

**Rôles.** La liaison π d’un alcène est nucléophile. HBr ionique ou une hydratation acide commence par protonation et formation d’un cation ; l’orientation favorise souvent le cation le mieux stabilisé. Une bromation Br₂ passe usuellement par un bromonium ponté, puis une attaque arrière et une addition anti.

Propène + HBr (voie ionique) → majoritairement 2-bromopropane  
1) BH₃ ou borane adapté ; 2) H₂O₂, HO⁻ ⇒ alcool anti-Markovnikov, addition H/OH syn  
Br₂ : addition anti ; H₂/catalyseur : addition syn

**Hydroboration.** H et B s’ajoutent dans une étape concertée, B préférant généralement le C le moins substitué. L’oxydation remplace C−B par C−O avec conservation de la disposition au C concerné. Le bilan syn compare le H ajouté et OH final ; il ne s’agit pas d’une dihydroxylation syn, qui ajoute deux OH.

**Exemple.** Le propène donne propan-2-ol par hydratation acide mais propan-1-ol par hydroboration/oxydation. Le but-2-ène E bromé donne un méso, son isomère Z une paire racémique. Pour un alcène trisubstitué, vérifier simultanément orientation et création éventuelle d’un centre chiral.

**Technique.** Annoncer réactifs, étapes et intermédiaires avant de citer Markovnikov. Une règle d’orientation ne détermine pas la stéréochimie ; des conditions radicalaires ou concertées changent le mécanisme et peuvent changer l’orientation.

## 24. Chaînes radicalaires : HBr sous conditions dédiées

*PC ; prolongement mécanistique accompagné* — laboratoire `radical`.

**Étapes.** Initiation forme des radicaux, propagation consomme un réactif en régénérant un radical, terminaison couple deux radicaux. En présence d’une source radicalaire adaptée, Br· peut s’additionner au propène de façon à former le radical carboné secondaire, puis celui-ci arrache H à HBr.

Br· + CH₂=CHCH₃ → BrCH₂−CH·−CH₃  
BrCH₂−CH·−CH₃ + HBr → BrCH₂CH₂CH₃ + Br·  
Bilan : HBr + propène → 1-bromopropane

**Orientation.** Elle résulte de la stabilité du radical et de la cinétique des deux étapes de propagation, sans carbocation. Le même raisonnement ne s’étend pas automatiquement à HCl et HI : les bilans énergétiques des étapes peuvent interrompre une chaîne efficace.

**Modèle cinétique.** Si Ri est une vitesse d’initiation en mol·L⁻¹·s⁻¹ et kt une constante de terminaison en L·mol⁻¹·s⁻¹, l’état quasi stationnaire donne une concentration radicalaire de l’ordre de √(Ri/(2kt)), selon la convention de comptage de Ri. Une propagation de vitesse kp\[alcène\]\[radical\] augmente alors comme √Ri.

**Technique.** Repérer l’électron célibataire à chaque étape, utiliser des demi-flèches, vérifier la régénération du porteur de chaîne et son bilan net. Les courbes du TP explorent un schéma radicalaire simplifié ; elles n’ajoutent pas une chaîne en l’absence des conditions d’initiation.

## 25. Alcynes : arrêter la réduction et lire la tautomérie

*PC — banque de transformations du recueil* — laboratoire `alcyne`.

**Réactivité.** Une triple liaison compte deux unités d’insaturation et peut subir deux additions successives. La réduction totale par H₂ sur catalyseur adapté donne l’alcane ; une réduction partielle exige un réactif et des conditions spécifiques. Un alcyne terminal possède aussi un H relativement acide pour une liaison C−H.

Alcyne interne + H₂/Lindlar ⇒ alcène Z (syn)  
Métal dissous, conditions adaptées ⇒ alcène E (anti globale)  
Alcyne terminal + H₂O/H⁺/Hg²⁺ ⇒ énol puis méthylcétone, sauf acétylène

**Tautomérie.** Un énol et un carbonyle sont des tautomères, donc des espèces distinctes reliées par transfert de proton et déplacement de liaison π. Ce ne sont pas des formes mésomères. L’hydratation du prop-1-yne forme CH₃−C(OH)=CH₂ puis propanone ; celle de l’acétylène forme l’éthanal.

**Exemple.** But-2-yne : une équivalence d’H₂ sous Lindlar permet Z-but-2-ène ; une réduction par métal dissous permet E-but-2-ène ; H₂ en excès sur un catalyseur non sélectif donne butane. L’hydroboration/oxydation adaptée d’un alcyne terminal conduit plutôt à un aldéhyde.

**Technique.** Distinguer une équivalence stœchiométrique de la capacité du catalyseur à arrêter la réaction. Dessiner d’abord l’énol puis le carbonyle, conserver le squelette C et vérifier si E/Z est défini. Le détail opératoire de ces banques n’est pas exigé sans données fournies.

## 26. Addition nucléophile aux carbonyles : ouvrir π puis protoner

*Sup — PCSI* — laboratoire `carbonyle`.

**Site.** Dans C=O, le C est électrophile et O donneur de doublets. L’attaque d’un nucléophile sur le C déplace les électrons π vers O et donne un intermédiaire tétraédrique. Un aldéhyde est généralement moins encombré et plus électrophile qu’une cétone comparable ; substituants et conjugaison nuancent cette tendance.

R₂C=O + Nu⁻ → R₂C(O⁻)Nu → après protonation R₂C(OH)Nu  
NaBH₄ : transfert d’hydrure puis hydrolyse/protonation ⇒ alcool  
Carbonyle plan : faces Re/Si, souvent deux voies en milieu achiral

**Exemple.** L’hydrure ajouté à propanone donne un alcoolate puis propan-2-ol, sans création de centre chiral. L’ajout à butan-2-one donne butan-2-ol avec deux énantiomères si aucune influence chirale ne différencie les faces. Le doublet nucléophile n’est pas dessiné comme H⁺.

**Milieu acide.** Une protonation de O active le carbonyle envers un nucléophile neutre, comme un alcool. Mais un nucléophile fortement basique est détruit par l’acide ; il faut choisir une séquence compatible. Une même étape formelle « addition » ne se réalise pas par les mêmes conditions pour tous les Nu.

**Technique.** Compter les nouvelles liaisons C−C ou C−H et les charges, puis distinguer l’addition à un aldéhyde/cétone de la substitution sur un dérivé d’acide possédant un groupe éliminable. L’étape finale de traitement aqueux doit apparaître dans le bilan.

## 27. Organomagnésiens : créer une liaison C−C avec un bilan exact

*Sup — PCSI* — laboratoire `grignard`.

**Préparation.** RMgX est obtenu à partir de RX et Mg en milieu éthéré anhydre adapté. L’éther coordonne Mg ; eau, alcools, acides et autres protons labiles consomment le réactif. La formule RMgX est un modèle utile d’espèces agrégées et solvatées, pas un carbanion libre isolé en solution.

RMgX + R′₂C=O → R′₂C(OMgX)R ; puis H₃O⁺ → R′₂C(OH)R  
RMgX + CO₂ → RCO₂MgX ; puis H₃O⁺ → RCO₂H  
RMgX + H−A → RH + sels de Mg

**Classe d’alcool.** Méthanal donne un alcool primaire, un autre aldéhyde un secondaire, une cétone un tertiaire. Le carbone du carbonyle reste dans le produit : CO₂ ajoute un C au squelette de R. Une synthèse rétrograde d’un alcool doit explorer les coupures possibles autour du C portant OH.

**Exemple.** PhMgBr et éthanal donnent 1-phényléthanol après hydrolyse. PhMgBr et CO₂ donnent l’acide benzoïque. Un ester R′COOR″ consomme normalement deux équivalents de RMgX et donne R′C(OH)R₂ : le premier alcoolate intermédiaire élimine OR″ puis la cétone formée réagit encore.

**Technique TP.** Justifier anhydrie, solvant, ordre d’addition, gestion du réactif limitant et hydrolyse terminale. L’absence d’eau n’est pas une décoration du protocole ; elle détermine quelle réaction gagne. Un modèle de compatibilité est plus instructif qu’un rendement fictif arbitraire.

## 28. Époxydes : ouvrir un cycle pour allonger une chaîne

*PC — extension fournie à partir des organomagnésiens* — laboratoire `grignard`.

**Tension et sites.** Un époxyde possède un cycle à trois atomes C−C−O. Sa tension favorise l’ouverture. En conditions nucléophiles basiques, l’attaque ressemble à une SN2 au C le moins encombré et rompt sa liaison C−O. Une activation acide modifie la polarisation et l’orientation possible.

RMgX + oxirane → R−CH₂−CH₂−OMgX ; puis H₃O⁺ → R−CH₂−CH₂OH  
Ouverture nucléophile : attaque arrière, inversion au C attaqué  
Ouverture acide d’un époxyde dissymétrique : orientation à discuter avec les conditions

**Exemple.** CH₃MgBr et oxirane donnent propan-1-ol après hydrolyse : deux C proviennent du cycle et un du nucléophile. Avec un époxyde substitué, redessiner le produit avant d’annoncer OH : l’oxygène demeure lié au C qui n’a pas été attaqué.

**Synthèse du cycle.** L’époxydation d’un alcène par un peracide est concertée et conserve les positions relatives des substituants. Une ouverture anti ultérieure peut construire un diol trans. Les étapes de formation et d’ouverture possèdent donc des exigences stéréochimiques différentes.

**Technique.** Nommer le C attaqué, tracer simultanément attaque et rupture C−O, conserver les atomes et appliquer l’hydrolyse. L’extension du squelette doit être comptée avant la recherche de la fonction finale ; sinon une route peut donner le mauvais nombre de C.

## 29. Oxydoréduction : niveaux d’oxydation et chimiosélectivité

*Sup — PCSI option PC ; approfondissement PC* — laboratoire `oxydoreduction`.

**Comptage.** Pour attribuer le nombre d’oxydation d’un C, partager C−C à égalité, attribuer C−H au C et C−O/C−N/C−X au partenaire plus électronégatif. Une oxydation organique augmente ce nombre ; elle n’exige pas que des électrons libres apparaissent dans le mécanisme moléculaire.

RCH₂OH → RCHO + 2 H⁺ + 2 e⁻  
RCHO + H₂O → RCO₂H + 2 H⁺ + 2 e⁻  
R₂CHOH → R₂CO + 2 H⁺ + 2 e⁻

**Sélectivité.** Une oxydation douce contrôlée d’un primaire peut s’arrêter à l’aldéhyde ; eau, oxydant et conditions peuvent conduire à l’acide. Un tertiaire n’a pas de H sur le C portant OH : l’oxydation en carbonyle avec squelette conservé est indisponible, tandis qu’une oxydation très forte peut casser des liaisons C−C.

**Exemple.** NaBH₄ réduit normalement aldéhydes et cétones dans les conditions usuelles de cours sans réduire un ester simple. LiAlH₄ peut réduire aussi esters et acides, avec des conditions distinctes et une incompatibilité avec les milieux protiques. Réduire une cétone en présence d’un ester est donc un problème de choix de réactif et de vérification IR/RMN.

**Aniline.** La demi-équation de réduction du nitrobenzène est PhNO₂+6H⁺+6e⁻→PhNH₂+2H₂O. Si le produit réel en milieu acide est anilinium, ajouter sa protonation. Pour un métal oxydé, équilibrer l’autre demi-équation avant de calculer réactif limitant et rendement.

**Ester : approfondissement PC.** Un hydrure attaque RCOOR′, l’intermédiaire tétraédrique élimine OR′ et donne un aldéhyde RCHO ; une seconde attaque donne RCH₂O⁻ puis RCH₂OH au traitement final. LiAlH₄ réalise usuellement cette réduction totale. Arrêter à l’aldéhyde demande un réducteur et des conditions spécifiques fournis, par exemple DIBAL-H à basse température avec une stœchiométrie et une hydrolyse adaptées. Le sous-produit R′OH est également récupéré après traitement ; ses atomes ne disparaissent pas.

## 30. Estérification, hydrolyse et saponification

*Sup → PC ; TP* — laboratoire `esterification`.

**Systèmes.** L’estérification acide-alcool et l’hydrolyse acide sont réversibles. La catalyse acide accélère l’approche de l’équilibre dans les deux sens. La saponification basique forme un carboxylate : sa stabilisation acido-basique rend généralement la transformation pratiquement complète dans les conditions étudiées.

RCO₂H + R′OH ⇌ RCO₂R′ + H₂O  
K=aester aeau/(aacide aalcool)  
RCO₂R′ + HO⁻ → RCO₂⁻ + R′OH

**Modèle de TP.** Pour un mélange homogène idéal contenant une mole d’acide, une mole d’alcool et aucune eau/ester initial, K=x²/(1−x)². K=4 donne x=2/3. Ajouter de l’alcool ou retirer de l’eau peut déplacer l’équilibre. Si l’eau est le solvant majoritaire, son activité proche de 1 ne se traite pas comme celle du même mélange équimolaire.

**Mécanisme.** Une addition au carbonyle suivie d’une élimination et de transferts de proton décrit une substitution nucléophile d’acyle. Un milieu acide rend possible le départ d’une molécule neutre ; en milieu basique, l’étape finale de protonation du carboxylate nécessite un traitement acidifiant distinct.

**Technique.** Un montage à reflux accélère la réaction sans confondre durée et équilibre. Pour une synthèse d’acétate ou d’aspirine, calculer rendement isolé après purification, vérifier identité et pureté par plusieurs mesures ; une masse de produit encore humide ne mesure pas le rendement fiable.

**Hydrolyse d’amide : PC.** RCONHR′+H₂O donne RCO₂H+R′NH₂ au bilan neutre, mais en milieu acide l’amine finale est protonée et en milieu basique l’acide est carboxylate. En acide, activation de C=O, attaque d’eau et transferts de H⁺ protonent l’azote avant rupture C−N ; les électrons de la liaison vont vers N, permettant le départ d’une amine ensuite protonée par le milieu. En base, addition de HO⁻ puis transferts et départ conduisent au carboxylate. La mésomérie de l’amide et son groupe partant moins favorable imposent souvent des conditions plus vigoureuses que pour un ester. Il faut écrire les formes réellement dominantes au pH choisi.

## 31. Substitution nucléophile d’acyle : addition puis élimination

*PC — dérivés d’acides* — laboratoire `acylation`.

**Réactivité.** Un dérivé RCOZ possède un C carbonyle électrophile et un substituant Z éliminable après formation de l’intermédiaire tétraédrique. Sa réactivité dépend de l’activation du carbonyle et de l’aptitude de Z à partir. Les chlorures et anhydrides sont souvent plus réactifs que les esters ; les amides sont fortement stabilisées par mésomérie.

RCOZ + Nu → intermédiaire tétraédrique → RCONu + Z  
RCOCl + 2 R′NH₂ → RCONHR′ + R′NH₃⁺Cl⁻  
RCOCl + R′NH₂ + base → amide + base protonée + Cl⁻

**Démonstration.** L’amine attaque C=O, O reçoit le doublet π, puis reforme C=O en expulsant Cl⁻. Une déprotonation donne l’amide neutre. HCl ou son équivalent protonique doit être piégé : un second équivalent d’amine peut être consommé uniquement comme base, ou une base séparée peut assurer cette fonction.

**Exemple.** Avec 10 mmol de chlorure d’acyle et seulement 10 mmol d’amine sans base externe, une fraction de l’amine devient ammonium non nucléophile. Une simple règle « 1:1 » ne suffit pas à annoncer 10 mmol d’amide. Si 20 mmol d’amine sont disponibles, le modèle bilan 1:2 permet cette quantité théorique.

**Paracétamol.** L’acylation de l’azote du p-aminophénol par un agent adapté construit une amide en présence d’un OH phénolique. La chimiosélectivité dépend des conditions et se vérifie ensuite : on ne considère pas toutes les fonctions comme des nucléophiles équivalents.

**Peptides : PC.** La liaison peptidique est une amide −CO−NH− reliant deux résidus d’acides α-aminés. Gly−Ala, H₂N−CH₂−CO−NH−CH(CH₃)−CO₂H dans une écriture neutre, possède une extrémité amino N-terminale, une extrémité carboxyle C-terminale et une chaîne latérale CH₃ sur le résidu alanine. Ala−Gly possède un autre ordre et une autre connectivité. Pour une synthèse dirigée, protection du NH₂ de l’acide activé et du CO₂H du partenaire nucléophile peut éviter les auto-couplages ; activation, configuration et déprotection doivent être contrôlées. Les formes ioniques changent avec le pH.

## 32. Activation : rendre la bonne fonction réactive

*Sup option PC → PC* — laboratoire `acylation`.

**Deux leviers.** Activer un nucléophile consiste par exemple à déprotoner ROH en RO⁻. Activer un électrophile consiste à protoner un alcool pour faciliter H₂O comme départ, à fabriquer un sulfonate, ou à convertir un acide en dérivé acylant. Activation et catalyse ne désignent pas toujours la même consommation de réactifs.

ROH → ROTs : rupture O−H puis formation O−S ; liaison C−O conservée  
ROTs + Nu⁻ → RNu + OTs⁻ : SN2 possible, inversion au C réactif  
RCO₂H + R′NH₂ ⇌ sel ammonium carboxylate, avant activation

**Stéréochimie.** La préparation d’un sulfonate sur O conserve la configuration géométrique du C portant l’alcool, car C−O n’est pas rompue. La substitution ultérieure au C peut l’inverser. Une séquence activation→SN2 ne comporte donc pas deux inversions identiques.

**Exemple.** Un alcool secondaire transforme son OH, mauvais groupe partant, en un sulfonate ; un azoture peu basique peut ensuite le remplacer par SN2. Une base forte peut au contraire provoquer E2. Pour une amide, un acide et une amine seuls forment souvent d’abord un sel : l’activation résout une difficulté de réactivité réelle.

**Technique.** Écrire la fonction visée, le type d’activation et le bilan des sous-produits. Identifier les autres fonctions susceptibles de réagir avec l’agent activant. Une banque de réactions fournit les conditions nécessaires, dont le choix peut différer d’un exemple de cours à l’autre.

## 33. Protection : conserver une fonction pendant une étape incompatible

*Sup — PCSI option PC* — laboratoire `protection`.

**Principe.** Une protection transforme temporairement une fonction gênante, résiste à l’étape désirée puis se retire sélectivement. Le coût est plusieurs opérations supplémentaires, des pertes de rendement et des déchets. Un groupe protecteur est choisi à partir de sa stabilité et des fonctions présentes.

Carbonyle + diol ⇌ acétal cyclique + H₂O, catalyse acide  
Acétal généralement stable envers bases/Grignard ; hydrolyse aqueuse acide  
Rendement global de 3 étapes : yglobal=yprotection·yréaction·ydéprotection

**Exemple.** Pour réaliser une addition organomagnésienne sur une fonction tout en conservant un autre carbonyle, protéger sélectivement celui qui doit survivre peut être nécessaire. Former l’acétal, éliminer eau et acide avant RMgX, effectuer l’addition et son traitement, puis hydrolyser l’acétal selon une séquence compatible.

**Bilan.** Trois étapes à 90 %, 85 % et 95 % donnent yglobal≈72,7 %. Une route directe compatible à 80 % peut donc être préférable. Mais un saut de protection menant à un mélange inutilisable n’est pas une optimisation : le nombre d’étapes seul n’évalue pas la qualité d’une route.

**Technique.** Établir une matrice fonction/réactif/conditions, annoncer pourquoi une protection est sélective et démontrer sa récupération par caractérisation. Les séquences du laboratoire comparent compatibilités et bilans déclarés ; elles ne prédisent pas les rendements de toute polyfonctionnalité.

**Autres fonctions : PC.** Un carboxyle peut être protégé en ester, un amino par une amide ou un carbamate de banque, un hydroxyle par un ester, un éther ou un groupe silylé fourni. Chacun résiste à certaines conditions et se retire par d’autres. Une protection ester n’est pas compatible avec un organomagnésien simplement parce qu’elle masque l’acidité : son carbonyle peut subir une addition. Protéger puis déprotéger avec deux réactions connues ne suffit pas ; il faut choisir la fenêtre de stabilité de toute la route. Un groupe benzyle peut se retirer par hydrogénolyse adaptée mais une double liaison à conserver pose alors un problème de chimiosélectivité.

## 34. Aldolisation et crotonisation : construire un motif conjugué

*PC — énolates et création C−C* — laboratoire `aldol`.

**Étapes.** Une base retire un Hα d’un carbonyle énolisable. Le C de l’énolate attaque le carbonyle d’un second partenaire ; après protonation, un β-hydroxycarbonyle apparaît. Une déshydratation ultérieure, appelée crotonisation, donne un carbonyle α,β-insaturé. Aldolisation et crotonisation doivent être distinguées.

RCOCH₂R′ → énolate ; énolate + R″CHO → β-hydroxycarbonyle  
β-hydroxycarbonyle → carbonyle α,β-insaturé + H₂O  
Benzaldéhyde + acétophénone → chalcone + H₂O (bilan condensé)

**Choix croisé.** Deux carbonyles tous deux énolisables peuvent donner plusieurs auto- et aldolisations croisées. Le benzaldéhyde n’a pas de Hα : il joue l’accepteur avec un donneur énolisable choisi. Préformer un énolate et contrôler l’ordre d’addition peut améliorer une sélectivité croisée.

**Exemple.** Acétophénone PhCOCH₃ et benzaldéhyde PhCHO donnent d’abord PhCOCH₂CH(OH)Ph ; déshydratation donne PhCOCH=CHPh. Les Hα du donneur et l’oxygène du carbonyle accepteur permettent de suivre les atomes jusqu’à l’eau éliminée. L’isomère E est souvent favorisé, sans imposer un pourcentage universel.

**Technique.** Repérer les Hα, identifier donneur et accepteur, tracer la nouvelle liaison puis vérifier la position β de OH et α,β de C=C. Une aldolisation intramoléculaire ajoute une contrainte de taille de cycle ; la dilution peut influencer compétition intra/intermoléculaire.

**Crotonisation E1cb : PC.** En base, retirer Hα forme d’abord un carbanion/énolate stabilisé, puis l’élimination de HO⁻ crée le système α,β-conjugué. C’est une élimination par la base conjuguée E1cb, différente d’E1 par carbocation et d’E2 concertée. La stabilisation de l’intermédiaire et la conjugaison finale rendent possible un départ qui serait défavorable dans une simple substitution d’un alcool non activé.

**C-alkylation d’énolate : PC.** Un énolate de cétone peut attaquer un halogénure alkyle accessible par SN2 et créer Cα−Calkyle. Deux sites α d’une cétone dissymétrique donnent des énolates régioisomères : base encombrée, basse température et déprotonation rapide favorisent souvent le site le moins encombré sous contrôle cinétique ; une énolisation réversible peut sélectionner l’énolate plus stable. Base, solvant et temps restent des données nécessaires. Un aldéhyde électrophile peut s’auto-aldoliser en concurrence, ce qui empêche de généraliser simplement l’alkylation de cétone. L’énolate est ambident C/O : compter les conditions et orbitales fournies, pas une charge localisée unique.

## 35. Michael et Wittig : deux constructions C−C différentes

*PC — réactions fournies et stratégies* — laboratoire `michaelwittig`.

**Michael.** Un carbonyle α,β-insaturé possède un site électrophile au C carbonyle et un au Cβ. Des nucléophiles adaptés, comme certains énolates stabilisés, peuvent donner une addition conjuguée 1,4 ; le carbonyle réapparaît après protonation/tautomérie. Des réactifs plus durs favorisent souvent 1,2, selon conditions.

Nu⁻ + RCO−CH=CH₂ → RCO−CH₂−CH₂Nu (après protonation)  
Wittig : R₂C=O + Ph₃P=CHR′ → R₂C=CHR′ + Ph₃P=O  
Ylure : Ph₃P⁺−C⁻HR′ ↔ Ph₃P=CHR′

**Wittig.** Un ylure de phosphore construit C=C en remplaçant l’oxygène du carbonyle par le carbone de l’ylure. Le bilan d’atomes place O sur Ph₃P=O. Ylures non stabilisés et stabilisés ont souvent des tendances Z et E différentes, mais sel, base, solvant et protocole interdisent d’en faire une règle absolue.

**Exemple.** Benzaldéhyde PhCHO et Ph₃P=CH₂ donnent styrène PhCH=CH₂ : ce produit n’a pas d’E/Z. Une addition d’un énolate d’acétoacétate à une énone peut donner un motif 1,5-dicarbonylé après protonation, alors qu’une addition 1,2 produit un alcool allylique.

**Technique.** Comparer les connectivités finales avant les noms de réaction, compter le carbone introduit et vérifier les doubles liaisons restantes. Une sélectivité d’addition 1,4 ne se déduit pas seulement de la présence d’une forme mésomère.

## 36. Aromatiques : orienter la SEA et ordonner les étapes

*PC — substitution électrophile aromatique* — laboratoire `aromatique`.

**Mécanisme.** Une liaison π aromatique attaque un électrophile E⁺ et forme un intermédiaire σ de Wheland qui a perdu temporairement l’aromaticité. La déprotonation rétablit le cycle conjugué. Les substituants affectent à la fois la vitesse et les positions relatives possibles.

Donneurs +M, souvent ortho/para ; −NO₂, −CN, −COR : souvent méta  
Halogènes : désactivants par −I mais ortho/para-directeurs  
Friedel–Crafts généralement indisponible sur noyaux fortement désactivés, dont nitrobenzène

**Justification.** Comparer les formes du complexe σ : un groupe donneur peut stabiliser les attaques ortho/para ; un attracteur −M les pénalise davantage que méta. Ce raisonnement explique l’orientation, mais les proportions exigent les barrières et les conditions ; additionner des dipôles de liaison ne donne pas directement un rapport d’isomères.

**Exemple de stratégie.** Pour une nitroacétophénone méta, acyler le benzène en acétophénone avant la nitration : COCH₃ dirige alors vers méta. Nitrer d’abord donnerait un noyau trop désactivé pour une Friedel–Crafts usuelle. Une alkylation peut réarranger et polyalkyler ; une acylation puis réduction adaptée peut éviter certains de ces problèmes.

**Technique.** Distinguer orientation d’un substituant et activation globale, vérifier incompatibilités avec l’acide de Lewis et réexaminer les directeurs après chaque étape. Une réaction radicalaire sur chaîne latérale n’est pas une SEA sur le noyau.

## 37. CLOA et recouvrement : normaliser les orbitales

*PC ; prolongement algébrique guidé* — laboratoire `orbitales`.

**Objets.** Une orbitale moléculaire ψ est une combinaison d’orbitales atomiques φA,φB normalisées. S=∫φA*φB dτ est sans dimension. Pour deux orbitales réelles similaires, les combinaisons symétrique et antisymétrique ont des normalisations différentes lorsque S n’est pas nul.

ψ+ = (φA+φB)/√\[2(1+S)\]  
ψ− = (φA−φB)/√\[2(1−S)\]  
Cas général : Hc=ESc ; c†Sc=1

**Démonstration.** Intégrer |φA±φB|² donne 1+1±2S. Diviser par 2(1±S) garantit une norme unité. S doit satisfaire |S|<1 pour deux fonctions indépendantes ; S→1 signifie une base presque redondante et rend la combinaison antisymétrique mal conditionnée.

**Exemple.** Pour S=0,20, les dénominateurs sont √2,4≈1,549 et √1,6≈1,265. La normalisation ne détermine pas à elle seule l’énergie ; il faut les éléments de H. Une combinaison constructive peut être liante dans un problème donné, mais le signe d’un coefficient dépend aussi de la phase choisie pour les orbitales de base.

**Technique.** Séparer dessin des phases, normalisation et diagonalisation. L’amplitude signée d’un lobe n’est pas une charge positive ou négative ; |ψ|² donne une densité de probabilité. Le labo fournit un Hamiltonien modèle et annonce ses approximations.

## 38. Hückel et orbitales frontières : passer d’un graphe à une réactivité

*PC ; extension numérique accompagnée* — laboratoire `orbitales`.

**Modèle.** Dans l’approximation de Hückel, une orbitale p par C conjugué, un recouvrement négligé, une énergie α sur chaque site et un couplage β<0 entre voisins définissent un Hamiltonien réel. Les niveaux et coefficients se calculent par diagonalisation. Le remplissage porte deux électrons au plus par orbitale.

H = αI + βA, A : matrice d’adjacence  
Chaîne m sites : Ej=α+2β cos\[jπ/(m+1)\]  
Butadiène : HO=α+0,618β ; BV=α−0,618β ; écart=1,236|β|

**Exemple.** Quatre électrons π du butadiène occupent les deux niveaux les plus bas. La HO a des coefficients dont les phases peuvent être opposées aux deux extrémités selon une phase globale arbitraire. Les densités de site impliquent carrés des amplitudes occupées ; le recouvrement de réaction doit aussi conserver les signes relatifs.

**Réactivité.** Une HO d’un nucléophile et une BV d’un électrophile rapprochées en énergie et de recouvrement adapté favorisent une interaction. Les gros lobes donnent une lecture qualitative de régiosélectivité pour des orbitales dissymétriques fournies, complétée par géométrie et encombrement. Le modèle ne prédit pas un rendement de laboratoire.

**Technique.** Déclarer α,β et la connectivité, vérifier orthonormalité et nombre d’électrons puis comparer deux orientations par leurs phases et amplitudes terminales. Un diene bloqué s-trans ne satisfait pas la géométrie de cycloaddition même avec un écart HO/BV favorable.

## 39. Diels–Alder : concertation, s-cis et endo

*PC — cycloadditions* — laboratoire `dielsalder`.

**Bilan.** Une cycloaddition \[4+2\] combine un diène conjugué et un diénophile pour construire un cycle à six C avec deux nouvelles liaisons σ et une double liaison résiduelle. Le diène doit pouvoir adopter une disposition s-cis. Un diène fixé s-trans est géométriquement inadapté au chemin concerté usuel.

4 électrons π du diène + 2 du diénophile → cycle à 6 centres  
Deux liaisons σ nouvelles ; liaison π résiduelle entre C2 et C3 du diène  
Substituants cis du diénophile ⇒ relation cis conservée dans l’adduit

**Endo/exo.** Avec un diénophile portant un groupe π attracteur, l’adduit endo est souvent favorisé cinétiquement par des interactions et une géométrie adaptées. Le produit exo peut être plus stable selon le système. Réversibilité et température peuvent donc modifier la composition ; aucune règle endo ne remplace les données d’activation.

**Exemple.** Cyclopentadiène et anhydride maléique construisent un adduit bicyclique. Le diène est contraint dans une géométrie favorable ; le diénophile pauvre en électrons favorise une demande électronique normale. Une estimation avec ΔΔG‡=3 kJ·mol⁻¹ à 298 K donne un rapport ≈3,36 seulement si les préfacteurs sont comparables et les voies irréversibles.

**Technique.** Numéroter les six centres, placer les deux nouvelles liaisons, conserver cis/trans du diénophile et vérifier s-cis avant la discussion orbitalaire. La structure endo se définit par la géométrie de l’adduit, pas simplement par une étiquette sur un histogramme.

## 40. Rétrosynthèse : choisir les coupures et l’ordre des fonctions

*Sup option PC → PC* — laboratoire `retrosynthese`.

**Démarche.** Partir de la cible, repérer fonctions et squelette puis couper mentalement une liaison formée par une réaction connue. Les synthons sont des fragments conceptuels chargés ; les réactifs équivalents sont des espèces réalisables. Revenir ensuite dans le sens direct pour vérifier compatibilités et sélectivités.

Alcool tertiaire R₁R₂R₃C−OH ← cétone R₁COR₂ + R₃MgX  
Chalcone ← acétophénone + benzaldéhyde  
Rendement global linéaire = ∏ yi ; convergence : comparer la plus longue séquence linéaire

**Exemples.** L’aspirine s’obtient conceptuellement par acylation du OH phénolique de l’acide salicylique. Le paracétamol par N-acylation du p-aminophénol. La chalcone par condensation croisée suivie de déshydratation. Ces trois cibles font comparer activation d’acyle, chimiosélectivité et création C−C, puis purification et caractérisation.

**Ordre.** Effectuer Friedel–Crafts avant une nitration désactivante, protéger un carbonyle avant un réactif qui doit l’épargner, retirer les milieux protiques avant un organomagnésien. Une route n’est validée qu’après reconstruction directe avec les conditions et le bilan d’atomes.

**Technique.** Définir un réactif limitant pour chaque étape, distinguer transformation théorique, conversion, sélectivité et rendement isolé. Le labo compare des routes dont les rendements et masses sont déclarés ; il invite à discuter leur plausibilité et les mesures nécessaires.

## 41. Synthèse au laboratoire : isoler, mesurer et réduire les pertes

*Sup — TP PCSI ; consolidation PC* — laboratoire `retrosynthese`.

**Chaîne expérimentale.** Une synthèse relie choix des quantités, montage et suivi, arrêt de réaction, extraction, lavage, séchage, purification puis caractérisation. Un reflux garde un mélange chauffé en condensant ses vapeurs ; une distillation sépare selon volatilité. Une recristallisation sépare suivant les solubilités et leurs variations avec la température.

yisolé = nproduit,pur / nproduit,théorique  
Économie d’atomes = Mproduit désiré / Σνi Mi,réactifs (équation équilibrée)  
PMI = masse totale entrante / masse produit ; E-factor = masse déchets / masse produit

**Exemple.** 5,00 g d’acide salicylique (138,12 g·mol⁻¹) correspondent à 36,20 mmol. Pour une transformation 1:1 en aspirine (180,16 g·mol⁻¹), la masse théorique est 6,522 g. Isoler 4,80 g de pureté massique 95 % donne 4,56 g de produit pur, soit 69,9 %, et non 73,6 % de produit pur.

**Indicateurs.** Pour un bilan massique complet et un périmètre identique, E-factor=PMI−1 si toute entrée hors produit devient déchet. Le traitement de l’eau, des solvants recyclés et des catalyseurs doit être annoncé. Une bonne économie d’atomes n’implique pas un petit PMI si des litres de solvant sont consommés.

**Technique.** Prévoir une méthode de contrôle qui distingue identité, pureté et quantité : IR/RMN, CCM, point de fusion comparé, dosage si adapté. Les laboratoires numériques forment le raisonnement du TP ; ils ne remplacent pas un protocole encadré, ses fiches de sécurité et sa gestion des déchets.

## 42. Polymères : une chimie des répétitions et des distributions

*PC ; prolongements statistiques accompagnés* — laboratoire `polymeres`.

**Deux familles.** Une polymérisation en chaîne fait croître des centres actifs ; une polymérisation par étapes fait réagir entre elles les fonctions de toutes les tailles de molécules. Polycondensation et polyaddition décrivent des bilans d’élimination différents et ne coïncident pas exactement avec chaîne/étapes.

Carothers, bifonctionnels équilibrés : Xn=1/(1−p)  
Déséquilibre r≤1 : Xn=(1+r)/(1+r−2rp)  
Distribution géométrique idéale : xn=(1−p)p^(n−1) ; dispersité Đ≈1+p

**Exemple.** Avec r=1, p=0,99 donne Xn=100 ; p=0,999 donne 1000. Si r=0,98 et p=0,99, Xn=1,98/(1,98−1,9404)=50. Une petite erreur de stœchiométrie limite donc fortement la longueur, même si la conversion de fonction est élevée.

**Hypothèses.** Le calcul suppose monomères bifonctionnels, réactivité des fonctions indépendante de la taille, absence de cyclisation et bilan de groupes adapté ; p est la fraction consommée des fonctions initialement limitantes pour r≤1. Des fonctions de valence supérieure permettent un réseau et une gélification hors du modèle linéaire. Les masses Mn et Mw sont des moyennes différentes d’une distribution.

**Lien synthèse.** La synthèse d’une liaison ester ou amide répétée utilise les mêmes notions d’activation et de départ que les petites molécules. La pureté fonctionnelle, la stœchiométrie et l’élimination d’un sous-produit deviennent des leviers du matériau final. Vérifier les hypothèses avant d’extrapoler Xn à un polymère réel.

Diacide HO₂C−A−CO₂H + diol HO−B−OH ⇒ motif polyester \[−CO−A−CO−O−B−O−\]  
Diacide + diamine H₂N−B−NH₂ ⇒ motif polyamide \[−CO−A−CO−NH−B−NH−\]  
Alcène CH₂=CHR ⇒ motif vinylique \[−CH₂−CH(R)−\] par voie de chaîne adaptée

**Monomères : PC.** Le nylon 6,6 associe une diamine à six C et un diacide à six C : le motif est \[−NH−(CH₂)₆−NH−CO−(CH₂)₄−CO−\], à distinguer des six C du diacide incluant ses deux carbonyles. Un polyester aromatique comme PET associe diol et diacide aromatique suivant la banque choisie. Une polymérisation d’alcène par coordination peut être décrite par un cycle fourni : coordination du monomère puis insertion dans la liaison métal−chaîne font croître le motif vinylique. Ce cycle n’est pas une condensation ester et ne suit pas les mêmes populations de Carothers.

## Les 30 introductions de laboratoire

### Laboratoire `electrons`

Apprendre à lire une transformation par les électrons : identifier donneur et accepteur, construire une flèche licite et contrôler les charges. Les quatre familles font distinguer transfert de proton, substitution, homolyse et formes mésomères avant de mémoriser des noms de réaction.

![Illustration scientifique du laboratoire electrons](illustrations/electrons.svg)

**Objets et unités**

- Atomes, liaisons, doublets, charges formelles en unités de charge élémentaire e ; δ représente une charge partielle
- Étapes et flèches du schéma : une paire d’électrons pour une flèche pleine, un électron pour une demi-flèche

**Hypothèses de l’expérience**

- Structures et étapes choisies pour expliciter le formalisme ; les noyaux restent fixes dans une mésomérie
- Les schémas sont une comptabilité de liaison, pas une trajectoire classique complète des électrons

**Techniques à mobiliser**

- Comptage Lewis et octet
- Conservation des atomes et de la charge
- Différenciation hétérolyse/homolyse/mésomérie

**Prédire → expérimenter → justifier**

1. Repérer le site riche et le site pauvre en électrons avant d’afficher une étape ; prévoir la charge de chaque produit.
2. Comparer les scénarios acido-basique, SN2, homolyse et mésomérie ; lire l’origine et la destination de chaque flèche.
3. Redessiner les doublets et calculer la somme des charges après chaque étape ; expliquer pourquoi une mésomérie ne déplace pas les H.

**Niveaux et approfondissements**

- Sup : Lewis, charges et formalisme des mécanismes : tronc commun PCSI.
- Spé : Intermédiaires conjugués et justification électronique des transformations.
- Au-delà : Densités électroniques, méthodes quantiques et chemin réactionnel multidimensionnel.

Leçons de référence : 1, 2, 3, 4.

**Résultat attendu.** Quatre transformations distinguées par une comptabilité exacte, avec des flèches justifiées plutôt que reproduites.

### Laboratoire `acidebase`

Relier un écart de pKa à un bilan de transformation et à la disponibilité d’une forme réactive. L’expérience force à distinguer la conversion de deux stocks finis, la composition d’un tampon et le rôle cinétique d’un nucléophile.

![Illustration scientifique du laboratoire acidebase](illustrations/acidebase.svg)

**Objets et unités**

- pKa d’un acide HA et de BH⁺, sans unité et dans le même solvant ; ratio initial base/acide b sans unité
- K sans unité ; avancement normalisé par le stock d’acide et fraction des espèces conjuguées

**Hypothèses de l’expérience**

- Une seule réaction HA+B⇌A⁻+BH⁺, milieu homogène, activités assimilées à des concentrations
- Le pH d’un tampon n’est pas imposé dans le calcul d’avancement à deux stocks ; tables fournies dans un solvant cohérent

**Techniques à mobiliser**

- Constante d’équilibre issue de deux Ka
- Bilan d’avancement et racine physique
- Distinction basicité/nucléophilie

**Prédire → expérimenter → justifier**

1. Prévoir le sens favorable pour ΔpKa positif, puis comparer stocks équimolaires et excès de base sans confondre K et conversion.
2. Choisir un transfert favorable puis presque équilibré ; augmenter le ratio de base et relever la fraction convertie.
3. Retrouver K=x²/[(1−x)(b−x)], vérifier 0≤x≤min(1,b) et expliquer pourquoi x=K/(1+K) ne vaut pas ici.

**Niveaux et approfondissements**

- Sup : Acido-basicité et réactivité : PCSI, avec données de solvant annoncées.
- Spé : Disponibilité d’énolates, protonation des amines et compatibilité des fonctions.
- Au-delà : Activités, effet de solvant et nivellement ; cinétique de transferts de proton.

Leçons de référence : 5, 6.

**Résultat attendu.** Une conversion calculée par conservation de matière et une justification du rôle acide/base dans une synthèse.

### Laboratoire `sn2`

Vérifier la cinétique d’une réaction A+B→P tout en suivant l’inversion d’une attaque arrière. L’expérience relie le schéma moléculaire à des concentrations finies : le nom bimoléculaire ne dispense pas de choisir l’intégration adaptée aux stocks.

![Illustration scientifique du laboratoire sn2](illustrations/sn2.svg)

**Objets et unités**

- Concentrations de substrat et nucléophile en mol·L⁻¹, temps en s ; k₂ en L·mol⁻¹·s⁻¹
- Conversion et quantité de produit normalisées ; disposition tétraédrique et état de transition

**Hypothèses de l’expérience**

- Réaction irréversible bimoléculaire unique à k₂ imposé, volume constant ; bilan A+B→P
- L’état de transition montré illustre le mécanisme ; l’inversion géométrique n’est pas une attribution CIP automatique universelle

**Techniques à mobiliser**

- Loi de vitesse et intégration à deux stocks
- Contrôle dimensionnel et pseudo-premier ordre
- Inversion de Walden et accessibilité stérique

**Prédire → expérimenter → justifier**

1. Prévoir l’effet d’un doublement de Nu sur v₀ et tester si Nu peut vraiment être pris constant.
2. Comparer stocks égaux et Nu en excès ; relever t₁/₂ et les concentrations finales sans consommer plus que le réactif limitant.
3. Retrouver les lois d’intégration dans les cas égal/excès, puis expliquer pourquoi primaire, néopentyle et tertiaire ne sont pas équivalents pour une SN2.

**Niveaux et approfondissements**

- Sup : SN2, ordre 2 et stéréochimie : PCSI.
- Spé : Réactions concurrentes, paramètres d’activation et synthèse de Williamson.
- Au-delà : Recouvrement Nu/σ*, dynamique de solvatation et surfaces d’énergie.

Leçons de référence : 17, 7, 19.

**Résultat attendu.** Une inversion expliquée et une loi de concentration validée par ses hypothèses et son réactif limitant.

### Laboratoire `sn1`

Distinguer disparition du substrat, accumulation d’un intermédiaire et formation du produit dans une ionisation suivie d’un piégeage. La stéréochimie fait discuter le cas limite racémique et les effets d’un environnement qui différencie les faces.

![Illustration scientifique du laboratoire sn1](illustrations/sn1.svg)

**Objets et unités**

- k₁ d’ionisation et k₂ de capture apparent en s⁻¹ ; temps en s ; concentrations normalisées
- Fraction de capture sur une face paramétrée, sans unité ; elle illustre un biais et n’est pas une donnée universelle

**Hypothèses de l’expérience**

- Schéma séquentiel irréversible RX→I→P, constantes imposées et bilan S+I+P constant
- Un cation libre symétriquement piégé est un cas limite ; paires d’ions et réarrangements réels demandent des données supplémentaires

**Techniques à mobiliser**

- Système d’équations cinétiques séquentielles
- Étape déterminante et accumulation
- Perte de configuration et différence de faces

**Prédire → expérimenter → justifier**

1. Prévoir si I s’accumule lorsque k₂ devient beaucoup plus petit ou plus grand que k₁.
2. Comparer capture rapide et lente ; observer séparément S, I et P puis faire varier le biais de face.
3. Vérifier S+I+P=1, expliquer quand v≈k₁[S] décrit la disparition et pourquoi elle ne garantit pas une formation immédiate du produit.

**Niveaux et approfondissements**

- Sup : Ionisation SN1 et solvolyse en PCSI ; introduction accompagnée de l’intermédiaire.
- Spé : Étape déterminante, AEQS et réarrangements, approfondissements PC.
- Au-delà : Paires d’ions, participation de groupes voisins et stéréodynamique en solution.

Leçons de référence : 18, 22.

**Résultat attendu.** Une courbe d’intermédiaire interprétée et une distinction entre mécanisme limite et racémisation exacte.

### Laboratoire `competition`

Décider entre substitution et élimination à partir de chemins compatibles, puis séparer conversion et sélectivité. L’expérience compare un embranchement commun après ionisation et les attaques bimoléculaires, sans compter deux fois le même départ lent.

![Illustration scientifique du laboratoire competition](illustrations/competition.svg)

**Objets et unités**

- Constantes et concentrations déclarées dans la simulation ; taux apparents des chemins en s⁻¹
- Stocks de réactifs et fractions de produits ; conversion et sélectivité affichées séparément

**Hypothèses de l’expérience**

- Schéma de chemins parallèles avec une ionisation commune aux issues SN1/E1, puis capture répartie
- Paramètres choisis et réservoirs de Nu/base : les pourcentages ne prédisent pas tous les réactifs et solvants réels

**Techniques à mobiliser**

- Addition et embranchement de flux
- Analyse substrate/Nu/base/solvant
- Bilan produit, conversion et récupération

**Prédire → expérimenter → justifier**

1. Avant le calcul, proposer les chemins accessibles pour un primaire peu encombré puis un tertiaire avec base forte.
2. Faire varier la base et le nucléophile indépendamment ; relever conversion totale et fractions de substitution/élimination.
3. Écrire le bilan de flux avec une seule ionisation, expliquer les chemins supprimés par la structure et calculer le rendement de produit depuis conversion×sélectivité.

**Niveaux et approfondissements**

- Sup : SN1/SN2/E2 et lecture de cinétique, réinvestissement PCSI.
- Spé : Modèle de compétition et effets des barrières, consolidation PC.
- Au-delà : Réseaux multietapes, retour du produit et modèles ajustés à des données expérimentales.

Leçons de référence : 19, 17, 18, 20.

**Résultat attendu.** Un choix de mécanisme argumenté et trois nombres correctement distingués : conversion, sélectivité et rendement isolé.

### Laboratoire `elimination`

Construire les alcènes à partir des Hβ réellement disponibles et de leur géométrie. Le cas cyclohexanique montre pourquoi le produit de stabilité maximale peut être absent lorsque le H anti-périplanaire est empêché.

![Illustration scientifique du laboratoire elimination](illustrations/elimination.svg)

**Objets et unités**

- Angle dièdre et conformation ; disponibilité des Hβ, classe du substrat et nature de la base
- Rapports de voies ou niveaux paramétrés ; configurations E/Z attribuées seulement si elles existent

**Hypothèses de l’expérience**

- E2 concertée avec disposition anti dans les scénarios standards ; E1 présenté comme schéma distinct
- Les proportions illustratives suivent les paramètres affichés ; trans-diaxial impose une contrainte de structure avant les tendances Zaitsev/Hofmann

**Techniques à mobiliser**

- Projection de Newman ou chaise
- Flèches concertées et Hβ
- Classement de connectivités et E/Z

**Prédire → expérimenter → justifier**

1. Énumérer tous les Cβ puis dessiner au moins une conformation anti pour chacun avant d’invoquer Zaitsev.
2. Comparer petite base et base encombrée ; ouvrir le cas trans-1-bromo-2-méthylcyclohexane et basculer la chaise.
3. Expliquer le produit moins substitué lorsque le site axial de C2 est occupé par CH₃ ; distinguer contrainte géométrique et stabilité des produits.

**Niveaux et approfondissements**

- Sup : β-élimination E2 et mécanisme : PCSI.
- Spé : Conformations réactives, E1/E2 et contrôle de stéréochimie.
- Au-delà : Effets isotopiques cinétiques et éliminations syn contraintes.

Leçons de référence : 20, 21, 10.

**Résultat attendu.** Une liste d’alcènes construite depuis les liaisons et les H, accompagnée des voies réellement autorisées.

### Laboratoire `alcene`

Comparer trois dimensions d’une transformation d’alcène : orientation, stéréochimie et rôle des conditions. Les voies ioniques, bromonium et hydroboration donnent des produits différents sans que la seule règle de Markovnikov suffise à les construire.

![Illustration scientifique du laboratoire alcene](illustrations/alcene.svg)

**Objets et unités**

- Substrats choisis : propène, E/Z-but-2-ène et alcène pouvant réarranger ; fonctions et centres créés
- Conditions de la banque, faces d’attaque et disposition syn/anti ; aucun rendement universel associé au seul nom de réaction

**Hypothèses de l’expérience**

- Chaque transformation suit le mécanisme annoncé : carbocation, pont bromonium ou addition concertée
- Les faces sont équivalentes dans un milieu achiral sauf influence indiquée ; règles d’orientation discutées avec réarrangements éventuels

**Techniques à mobiliser**

- Suivi des atomes dans une addition
- Orientation et intermédiaire
- Conservation ou création de stéréochimie

**Prédire → expérimenter → justifier**

1. Prévoir propan-1-ol ou propan-2-ol suivant les conditions, puis dessiner les produits de bromation des deux but-2-ènes.
2. Comparer hydratation acide, HBr ionique, hydroboration/oxydation et bromation ; observer les nouvelles liaisons et les faces.
3. Justifier chaque orientation par son chemin ; expliquer la différence entre H/OH syn et deux OH syn, puis reconnaître méso ou paire d’énantiomères.

**Niveaux et approfondissements**

- Sup : Nucléophile/électrophile, stéréochimie et lecture d’une banque en Sup.
- Spé : Réactivité des alcènes, orientation et stéréospécificité : parcours PC.
- Au-delà : Catalyse énantiosélective et mécanismes d’addition plus fins.

Leçons de référence : 23, 8.

**Résultat attendu.** Quatre voies d’addition distinguées par conditions, connectivité et résultat stéréochimique.

### Laboratoire `alcyne`

Apprendre à arrêter une transformation au bon degré d’insaturation et à suivre un énol jusqu’au carbonyle final. Les comparaisons Lindlar/métal dissous/réduction totale font comprendre le rôle du catalyseur et du bilan d’hydrogène.

![Illustration scientifique du laboratoire alcyne](illustrations/alcyne.svg)

**Objets et unités**

- Alcyne terminal ou interne et équivalents réactifs ; nombre d’unités d’insaturation
- Alcène E/Z si défini, énol intermédiaire, aldéhyde ou cétone finale

**Hypothèses de l’expérience**

- Transformations de banque avec conditions spécifiques, sans extrapolation d’un catalyseur à toutes les réductions
- La tautomérie est un changement d’espèce avec transfert de H ; les conditions sont fournies pour les extensions

**Techniques à mobiliser**

- Comptage des additions
- Stéréochimie syn/anti
- Tautomérie et suivi du C terminal

**Prédire → expérimenter → justifier**

1. Prévoir les produits de but-2-yne sous trois conditions de réduction ; compter les H ajoutés.
2. Comparer Lindlar, métal dissous et réduction totale ; suivre l’hydratation du prop-1-yne puis son hydroboration/oxydation.
3. Redessiner chaque énol avant sa tautomérie et expliquer pourquoi un équivalent global de H₂ sans catalyseur ne garantit pas un alcène pur.

**Niveaux et approfondissements**

- Sup : Insaturation et bilan ; transformations accompagnées à partir d’une banque.
- Spé : Réactivité des alcynes du recueil et choix de conditions : PC.
- Au-delà : Acétylures en synthèse, couplages et catalyse sélective.

Leçons de référence : 25, 11.

**Résultat attendu.** Une fonction finale correctement identifiée et une stratégie d’arrêt au stade alcène justifiée.

### Laboratoire `radical`

Construire une chaîne qui régénère un radical, puis relier initiation, propagation et terminaison à une loi cinétique. HBr radicalaire sert à expliquer une orientation différente sans introduire un carbocation caché.

![Illustration scientifique du laboratoire radical](illustrations/radical.svg)

**Objets et unités**

- Vitesse d’initiation en mol·L⁻¹·s⁻¹ et constante de terminaison en L·mol⁻¹·s⁻¹ ; sélectivité relative par site sans unité
- Concentration radicalaire stationnaire et enthalpies de propagation estimées en kJ·mol⁻¹ ; électrons célibataires et demi-flèches

**Hypothèses de l’expérience**

- Initiateur et conditions adaptés explicitement requis ; chaîne simplifiée avec terminaison choisie
- Un régime quasi stationnaire est une approximation après l’initiation ; HCl/HI ne sont pas assimilés automatiquement à HBr

**Techniques à mobiliser**

- Annulation des intermédiaires dans un bilan
- Demi-flèches et stabilité radicalaire
- AEQS et dépendance en racine carrée

**Prédire → expérimenter → justifier**

1. Écrire les deux propagations de HBr sur propène et prévoir le radical le plus stabilisé.
2. Modifier initiation et terminaison ; relever la concentration stationnaire. En halogénation, comparer la sélectivité par site à celle corrigée par le nombre de H.
3. Vérifier que le radical se régénère dans la propagation et disparaît en terminaison ; retrouver la loi √Ri dans les conditions stationnaires.

**Niveaux et approfondissements**

- Sup : Homolyse, radical et bilan de matière, entrée accompagnée.
- Spé : Mécanismes de chaîne et réactivité comparée : approfondissement PC avec données fournies.
- Au-delà : Polymérisation radicalaire, inhibiteurs et réactions photochimiques.

Leçons de référence : 24, 2.

**Résultat attendu.** Une chaîne fermée au bilan et un effet de l’initiation expliqué par le mécanisme de terminaison.

### Laboratoire `carbonyle`

Identifier ce qui arrive après une attaque du carbonyle : alcoolate d’addition, départ d’un groupe, protection, énolate ou construction de C=C. La banque de familles aide à choisir le bon mécanisme pour la fonction plutôt qu’à traiter tous les C=O de la même façon.

![Illustration scientifique du laboratoire carbonyle](illustrations/carbonyle.svg)

**Objets et unités**

- Famille de carbonyle et nucléophile : charges, fonction voisine, groupe éliminable
- Étapes de la banque et produits après traitement ; nouvelle liaison et fonction conservée ou transformée

**Hypothèses de l’expérience**

- Mécanismes et conditions fournis par famille ; les scénarios ne simulent pas toutes les polyfonctionnalités
- Addition à aldéhyde/cétone et substitution d’acyle sont des bilans distincts ; la protonation finale est indiquée

**Techniques à mobiliser**

- Polarisation C=O et attaque
- Intermédiaire tétraédrique et départ
- Comparaison de fonctions et compatibilité

**Prédire → expérimenter → justifier**

1. Pour une cétone puis un ester, dessiner l’attaque et demander si un groupe peut quitter l’intermédiaire.
2. Comparer les familles proposées, dont acétal, aldol et Wittig ; suivre les atomes plutôt que le seul nom.
3. Écrire le bilan de la famille choisie, restaurer charges/doublets et expliquer pourquoi une cétone formée par Grignard sur ester réagit encore.

**Niveaux et approfondissements**

- Sup : Addition nucléophile aux aldéhydes/cétones : PCSI.
- Spé : Dérivés d’acide, énolates et création C−C : PC.
- Au-delà : Sélectivité faciale, catalyse et paramètres quantiques de réactivité.

Leçons de référence : 26, 31, 33, 34, 35.

**Résultat attendu.** Un mécanisme sélectionné à partir de la fonction et un produit suivi jusqu’au traitement final.

### Laboratoire `grignard`

Créer un squelette C−C tout en comptant les consommations concurrentes. Le laboratoire met au premier plan l’anhydrie, les H labiles, les équivalents d’ester et le traitement aqueux final ; les quantités calculées sont des bornes stœchiométriques.

![Illustration scientifique du laboratoire grignard](illustrations/grignard.svg)

**Objets et unités**

- Quantités d’électrophile, de RMgX et de protons labiles en mmol ; équivalents sans unité
- Classe d’alcool et nombre de C de la cible ; quantité maximale après consommation protique

**Hypothèses de l’expérience**

- RMgX représente une espèce organométallique solvatée ; équivalents et incompatibilités fournis
- Une borne de matière ne donne ni rendement réel ni composition garantie d’un mélange d’ester sous-stœchiométrique

**Techniques à mobiliser**

- Addition carbonylée et hydrolyse
- Bilan d’équivalents et réactif limitant
- Coupure rétrosynthétique et comptage C

**Prédire → expérimenter → justifier**

1. Prévoir primaire/secondaire/tertiaire selon méthanal, aldéhyde ou cétone, puis compter les deux additions sur ester.
2. Introduire des protons labiles à quantité fixée de RMgX ; comparer l’ester, CO₂ et l’oxirane.
3. Calculer le réactif réellement disponible, vérifier les C et justifier l’ordre milieu anhydre→addition→hydrolyse.

**Niveaux et approfondissements**

- Sup : Synthèse magnésienne et compatibilités : tronc commun PCSI.
- Spé : Esters, époxydes et polyfonctionnalité, prolongements fournis PC.
- Au-delà : Agrégation organométallique, échange métal/halogène et couplages.

Leçons de référence : 27, 28, 5.

**Résultat attendu.** Une cible C−C obtenue depuis un bilan d’atomes et d’équivalents, avec incompatibilités explicitement traitées.

### Laboratoire `oxydoreduction`

Relier le niveau d’oxydation d’un carbone aux fonctions transformées et choisir une chimiosélectivité. Les alcools, carbonyles et groupe nitro illustrent une même comptabilité électronique avec des mécanismes et réactifs différents.

![Illustration scientifique du laboratoire oxydoreduction](illustrations/oxydoreduction.svg)

**Objets et unités**

- Fonctions du substrat, nombres d’oxydation et électrons de demi-équation
- Conditions réelles de la banque, fonctions conservées et signatures IR/RMN attendues

**Hypothèses de l’expérience**

- Sélectivités attachées aux conditions fournies ; aucun réducteur universel pour toute molécule
- L’inertie d’un tertiaire concerne l’oxydation douce en carbonyle à squelette conservé, pas toute rupture oxydante forte

**Techniques à mobiliser**

- Demi-équations et bilan d’électrons
- Choix de réactif chimiosélectif
- Validation par plusieurs spectroscopies

**Prédire → expérimenter → justifier**

1. Prévoir les niveaux accessibles depuis un alcool primaire, secondaire puis tertiaire sans casser C−C.
2. Comparer les réductions usuelles NaBH₄ et LiAlH₄ en présence de cétone/ester ; ouvrir la réduction nitro→amine.
3. Équilibrer les protons/eau/électrons, vérifier les fonctions préservées et proposer une donnée spectrale qui réfute un produit concurrent.

**Niveaux et approfondissements**

- Sup : Niveaux d’oxydation, NaBH₄ et alcools : PCSI option PC.
- Spé : Choix de conditions et chimiosélectivité multietapes : PC.
- Au-delà : Oxydations catalytiques, réductions énantiosélectives et électrosynthèse.

Leçons de référence : 29, 12, 13.

**Résultat attendu.** Une demi-équation équilibrée et une sélection de réactif validable expérimentalement.

### Laboratoire `aromatique`

Lire séparément l’activation d’un noyau et l’orientation de sa substitution. Les chemins ortho/méta/para puis les routes ordonnées montrent comment choisir les étapes sans déduire leur vitesse de simples moments dipolaires.

![Illustration scientifique du laboratoire aromatique](illustrations/aromatique.svg)

**Objets et unités**

- Substituant, caractère inductif/mésomère et positions du noyau ; nombre de sites équivalents
- Barrières déclarées en kJ·mol⁻¹ et température en K ; fractions de voies issues du modèle cinétique

**Hypothèses de l’expérience**

- SEA par intermédiaire σ et restauration aromatique ; barrières de démonstration et multiplicité des sites
- Les dipôles caractérisent une structure mais ne servent pas à prédire les proportions ; Friedel–Crafts exclue sur NO₂ fortement désactivant dans les conditions usuelles

**Techniques à mobiliser**

- Mésomérie du complexe de Wheland
- Multiplicité et comparaison de barrières
- Ordre de synthèse et changement de directeurs

**Prédire → expérimenter → justifier**

1. Prévoir les orientations pour OMe, NO₂ et Br, en distinguant direction et activation globale.
2. Comparer les barrières et les multiplicités ortho/méta/para ; examiner acylation avant puis après nitration.
3. Justifier les voies par les complexes σ et les conditions ; montrer pourquoi un calcul de dipôle ne remplace pas un modèle de vitesse.

**Niveaux et approfondissements**

- Sup : Conjugaison et effets électroniques comme prérequis PCSI ; banque accompagnée.
- Spé : SEA, directeurs et stratégies aromatiques : PC avec transformations précisées.
- Au-delà : Effets de substituants quantifiés, Hammett et calcul des états de transition.

Leçons de référence : 36, 4, 22.

**Résultat attendu.** Une orientation argumentée et une route ordonnée dont chaque étape reste réactive.

### Laboratoire `orbitales`

Faire le lien entre l’algèbre linéaire et la réactivité : normaliser une CLOA, remplir les niveaux puis lire phases et coefficients d’une HO/BV. Le modèle de Hückel donne des calculs contrôlables plutôt qu’une règle visuelle sans hypothèses.

![Illustration scientifique du laboratoire orbitales](illustrations/orbitales.svg)

**Objets et unités**

- Recouvrement S sans unité, α et β en eV ; matrice d’adjacence et énergie des niveaux
- Coefficients orbitaux signés, occupation électronique et densité de site ; écart HO/BV en eV

**Hypothèses de l’expérience**

- CLOA et Hückel sont deux approximations annoncées ; Hückel prend un recouvrement nul dans sa base
- La phase globale ne change pas la densité ; remplissage égal des niveaux dégénérés quand indiqué ; pas de rendement synthétique prédit

**Techniques à mobiliser**

- Normalisation d’une combinaison
- Diagonalisation et remplissage
- Recouvrement et coefficients terminaux

**Prédire → expérimenter → justifier**

1. Pour S non nul, prévoir pourquoi √2 ne normalise plus les deux combinaisons ; compter les électrons π.
2. Faire varier le recouvrement, puis comparer chaînes et cycles Hückel ; relever HO/BV et coefficients de site.
3. Vérifier c†Sc=1 ou l’orthonormalité Hückel, conserver le nombre d’électrons et expliquer le rôle des phases relatives dans une interaction.

**Niveaux et approfondissements**

- Sup : Lewis/conjugaison, avec introduction accompagnée de l’outil mathématique.
- Spé : CLOA, orbitales frontières et applications de réactivité PC selon le cadre fourni.
- Au-delà : Méthodes quantiques avec recouvrement, corrélation et calcul de barrières.

Leçons de référence : 37, 38, 39.

**Résultat attendu.** Une combinaison normalisée, des niveaux remplis correctement et une interprétation qualitative sans surpromesse du modèle.

### Laboratoire `cinetique`

Comprendre pourquoi le produit formé le plus vite peut ne pas être le plus stable. Les courbes séparent évolution irréversible, comparaison des barrières et comparaison thermodynamique, afin de choisir une expérience qui peut distinguer les deux contrôles.

![Illustration scientifique du laboratoire cinetique](illustrations/cinetique.svg)

**Objets et unités**

- ΔH‡ en kJ·mol⁻¹, ΔS‡ en J·mol⁻¹·K⁻¹ et température en K ; ΔG‡=ΔH‡−TΔS‡ avec conversion d’unité
- Énergies G des produits en kJ·mol⁻¹, temps en s et coordonnée réactionnelle sans unité distincte du temps ; rapports de voies

**Hypothèses de l’expérience**

- Préfacteurs et barrières imposés dans la comparaison ; Eyring est un prolongement explicité
- Le comparatif d’équilibre ne rend pas réversible l’intégration irréversible ; l’interconversion doit exister pour atteindre la composition thermodynamique

**Techniques à mobiliser**

- Exponentielles et rapports de constantes
- Lecture maximum/minimum de profil
- Conception d’un test temps/température

**Prédire → expérimenter → justifier**

1. Prévoir quelle barrière donne le produit initial majoritaire et quel minimum donne l’équilibre préféré.
2. Varier température et différence de barrières ; observer l’évolution puis la comparaison indépendante d’équilibre.
3. Calculer les deux rapports, vérifier les unités RT et définir les conditions nécessaires pour passer du contrôle cinétique au thermodynamique.

**Niveaux et approfondissements**

- Sup : Loi d’Arrhenius, catalyse et mécanismes : PCSI option PC.
- Spé : Contrôles cinétique/thermodynamique et intermédiaires : PC.
- Au-delà : Eyring, réseaux réversibles et méthodes d’ajustement de cinétiques.

Leçons de référence : 22, 19.

**Résultat attendu.** Deux compositions reliées à deux hypothèses distinctes, accompagnées d’un protocole permettant de les tester.

### Laboratoire `formule`

Commencer une identification par un bilan d’atomes, de masse et d’insaturation. Les signatures isotopiques de Cl/Br montrent qu’une formule fournit des contraintes solides sans déterminer à elle seule la connectivité.

![Illustration scientifique du laboratoire formule](illustrations/formule.svg)

**Objets et unités**

- Nombres entiers d’atomes C,H,N,O et halogènes ; IHD sans unité
- Masse moyenne molaire en g·mol⁻¹, masse monoisotopique et enveloppe isotopique ; m/z dépend du type d’ion

**Hypothèses de l’expérience**

- Formules neutres usuelles et valences annoncées pour IHD ; domaine entier vérifié
- Enveloppe halogène simplifiée et séparée des fragmentations ; pas d’attribution d’ionisation universelle

**Techniques à mobiliser**

- Indice d’insaturation et valences
- Masse moyenne/masse exacte/ion
- Polynômes isotopiques et contraintes structurelles

**Prédire → expérimenter → justifier**

1. Calculer IHD de C₈H₈O₂ et proposer au moins deux structures compatibles avant de regarder les autres données.
2. Ajouter un puis deux Cl ou Br ; lire les enveloppes M/M+2/M+4 et comparer masses moyenne/exacte.
3. Démontrer les rapports par développement binomial, identifier quel ion serait mesuré et expliquer pourquoi IR/RMN restent nécessaires.

**Niveaux et approfondissements**

- Sup : Formule, valences et insaturation ; complément analytique accompagné en PCSI.
- Spé : Résolution de structures et lecture de masse avec données fournies, PC.
- Au-delà : Haute résolution, isotopes multiples et fragmentation mécanistique.

Leçons de référence : 11, 14.

**Résultat attendu.** Une formule contrôlée et une liste de connectivités candidates compatible avec toutes ses contraintes.

### Laboratoire `stereo`

Construire les priorités CIP d’un cas lisible puis relier composition d’énantiomères et polarimétrie. La manipulation vise à conserver une configuration sous rotation du dessin et à reconnaître les conditions d’une attribution fiable.

![Illustration scientifique du laboratoire stereo](illustrations/stereo.svg)

**Objets et unités**

- Acide lactique : substituants explicitement classés OH>CO₂H>CH₃>H ; configuration et miroir
- Proportions R/S et ee ; rotation spécifique [α]R en °·mL·g⁻¹·dm⁻¹, tube ℓ en dm, concentration c en g/mL ; rotation observée α en degrés

**Hypothèses de l’expérience**

- Un seul couple d’énantiomères, milieu et concentrations comparables ; réponse de polarimétrie linéaire
- Le cas CIP est fourni et ne constitue pas un moteur général d’assignation ; le signe optique n’est pas déduit de R/S

**Techniques à mobiliser**

- Priorités CIP et vue 4 à l’arrière
- Miroir/superposition et symétrie
- Calcul d’ee et contrôle de polarimétrie

**Prédire → expérimenter → justifier**

1. Classer CO₂H et CH₃ au premier rang différent et attribuer la configuration avant de tourner le modèle.
2. Comparer l’image miroir, un mélange racémique et un mélange 80/20 ; modifier [α]R, tube et concentration.
3. Vérifier ee=|xR−xS| et α=[α]Rℓc(xR−xS), justifier R/S indépendamment du signe et nommer les conditions nécessaires à la quantification.

**Niveaux et approfondissements**

- Sup : Stéréoisomérie et CIP : PCSI.
- Spé : Stéréosélectivité de synthèse et caractérisation d’ee.
- Au-delà : Séparation chirale, rotations calculées et catalyse asymétrique.

Leçons de référence : 7, 8.

**Résultat attendu.** Une configuration attribuée par une règle, puis un ee calculé sans assimilation R=+.

### Laboratoire `conformeres`

Passer d’un dessin de Newman ou d’une chaise à des populations thermiques. Le butane et le méthylcyclohexane font expliciter minima, dégénérescence, stabilité et vitesse d’échange plutôt que confondre conformère le plus stable et produit nécessairement majoritaire.

![Illustration scientifique du laboratoire conformeres](illustrations/conformeres.svg)

**Objets et unités**

- Angle dièdre en degrés ; énergie ou différence de G en kJ·mol⁻¹, température en K
- Anti/gauche du butane, chaise axiale/équatoriale ; probabilités sans unité et barrières indicatives

**Hypothèses de l’expérience**

- Profil périodique de torsion interpolé entre niveaux annoncés, et population discrète des minima traitée séparément
- Deux minima gauche comptés ; deux chaises de même dégénérescence ; la barrière ne détermine pas le ratio d’équilibre

**Techniques à mobiliser**

- Projections et rotation autour de σ
- Poids de Boltzmann et dégénérescence
- Basculement axial/équatorial sans changement cis/trans

**Prédire → expérimenter → justifier**

1. Placer anti/gauche/éclipsé, compter les deux minima gauche et prévoir quelle chaise est préférée.
2. Faire varier la température pour butane, dont le coût gauche est fixé à 3,8 kJ·mol⁻¹ ; pour le méthylcyclohexane, changer aussi le coût axial. Lire profil et populations.
3. Retrouver la normalisation des poids, conserver haut/bas après basculement et distinguer population, barrière d’échange et vitesse de réaction.

**Niveaux et approfondissements**

- Sup : Conformation Newman/chaise : PCSI ; populations introduites avec la formule.
- Spé : Conformations réactives, E2 trans-diaxiale et contrôle de synthèse.
- Au-delà : Curtin–Hammett, mécanique moléculaire et intégration de distributions continues.

Leçons de référence : 9, 10, 20.

**Résultat attendu.** Une population qui tient compte de la dégénérescence et une chaise correctement basculée.

### Laboratoire `ir`

Identifier des groupes caractéristiques tout en comprenant le lien vibration/absorption. Les courbes calculées servent à distinguer absorbance additive, transmittance non additive et signatures fonctionnelles, puis à formuler une caractérisation réfutable.

![Illustration scientifique du laboratoire ir](illustrations/ir.svg)

**Objets et unités**

- Nombre d’onde en cm⁻¹, largeur et position des bandes simulées ; concentration et trajet selon l’échelle du modèle
- Absorbance A sans unité et transmittance en % ; molécules choisies et hypothèses de bandes typiques

**Hypothèses de l’expérience**

- Bandes gaussiennes pédagogiques, pas une reproduction de spectre NIST mesuré
- Beer–Lambert dans son domaine déclaré ; environnement, couplages et liaisons hydrogène peuvent modifier un spectre réel

**Techniques à mobiliser**

- Oscillateur harmonique et masse réduite
- Transformation A↔T
- Diagnostic fonctionnel croisé avec RMN

**Prédire → expérimenter → justifier**

1. Prévoir les différences entre éthanol, propanone, acide et ester avant d’ouvrir leurs courbes.
2. Comparer les molécules et doubler concentration/épaisseur ; observer ce qui double et ce qui ne double pas.
3. Justifier les bandes, expliquer les absences et calculer T=10⁻ᴬ ; compléter le diagnostic par une autre donnée plutôt que par une seule bande OH.

**Niveaux et approfondissements**

- Sup : IR et interprétation spectrale : PCSI option PC.
- Spé : Suivi de sélectivité et problèmes multitechnniques de PC.
- Au-delà : Modes normaux couplés, isotopes et spectres quantitatifs expérimentaux.

Leçons de référence : 12, 14, 29.

**Résultat attendu.** Un diagnostic de fonctions, des unités correctes et une distinction nette entre spectre calculé et référence mesurée.

### Laboratoire `rmn`

Résoudre des connectivités à partir de δ, J et intégrales, puis vérifier quand le premier ordre est fiable. Le groupe éthyle, les singulets et les environnements ¹³C forment des problèmes d’assemblage de fragments plutôt que de reconnaissance visuelle de pics.

![Illustration scientifique du laboratoire rmn](illustrations/rmn.svg)

**Objets et unités**

- δ en ppm ; J en Hz ; fréquence du spectromètre en MHz ; intégrales associées à un nombre d’H
- Environnements ¹³C découplés et dégénérescences ; paquets aromatiques explicitement approximatifs

**Hypothèses de l’expérience**

- Simulation de multiplets du premier ordre : Δν/J doit être grand ; aromaticité non résolue en système complet AA′BB′
- OH/NH échangeables modélisés simplement ; spectre ¹³C découplé non réputé quantitatif par ses hauteurs

**Techniques à mobiliser**

- Assemblage intégrale/déplacement/couplage
- Règle n+1 et coefficients binomiaux
- Contrôle Δν/J et environnements équivalents

**Prédire → expérimenter → justifier**

1. Prévoir les trois signaux de l’éthanoate d’éthyle et les distinguer d’un propanoate de méthyle.
2. Comparer les sept molécules, changer la fréquence et élargir les raies ; lire intégrales et même J du groupe éthyle.
3. Convertir J en ppm, vérifier Δν/J et expliquer pourquoi des énantiomères en milieu achiral ou des multiplets superposés ne suffisent pas toujours à une identité unique.

**Niveaux et approfondissements**

- Sup : RMN ¹H et couplages premier ordre : PCSI option PC.
- Spé : Analyse de mélanges et structure combinée en PC ; ¹³C fourni comme complément.
- Au-delà : Couplages forts, RMN bidimensionnelle et environnements chiraux.

Leçons de référence : 13, 14.

**Résultat attendu.** Une structure justifiée par toutes les données, avec diagnostic explicite du domaine premier ordre.

### Laboratoire `ccm`

Choisir une séparation exploitable et un suivi de réaction. La plaque simulée relie force éluante, rétention et largeur des taches pour apprendre à décider quand une CCM informe réellement le TP.

![Illustration scientifique du laboratoire ccm](illustrations/ccm.svg)

**Objets et unités**

- Distance du dépôt, des taches et du front ; Rf sans unité ; proportions de l’éluant
- Largeur et centres des taches ; réponse de rétention paramétrée pour la silice en phase normale

**Hypothèses de l’expérience**

- Modèle pédagogique de rétention et d’étalement, pas calcul universel de toutes les molécules sur silice
- L’intensité de révélation et un Rf ne mesurent pas seuls une quantité ou une identité absolue

**Techniques à mobiliser**

- Rapport de distances et séparation
- Choix de force éluante
- Prélèvement et comparaison à référence/co-tache

**Prédire → expérimenter → justifier**

1. Prévoir si un éluant trop faible ou trop fort sépare mieux deux espèces proches ; distinguer ΔRf et largeurs.
2. Faire varier l’éluant puis observer le dépôt, le front et les taches ; comparer le suivi aux références.
3. Calculer les Rf depuis le même zéro, sélectionner un éluant argumenté et expliquer ce qu’une disparition de tache prouve ou ne quantifie pas.

**Niveaux et approfondissements**

- Sup : CCM, observation et suivi : techniques expérimentales PCSI.
- Spé : Sélection de purification et validation d’une séquence de PC.
- Au-delà : Chromatographie sur colonne, HPLC et quantification étalonnée.

Leçons de référence : 15, 41.

**Résultat attendu.** Un choix d’éluant motivé par la résolution et un compte rendu de suivi sans faux rendement visuel.

### Laboratoire `extraction`

Choisir le nombre de contacts et le pH pour isoler une espèce. Le bilan distingue partage de la forme neutre et distribution totale, puis compare un seul grand contact à plusieurs volumes de solvant neuf.

![Illustration scientifique du laboratoire extraction](illustrations/extraction.svg)

**Objets et unités**

- P de la forme neutre et D total sans unité ; pKa et pH d’un milieu maintenu
- Volumes aqueux/organiques en mL ; nombre entier d’extractions et fractions récupérées

**Hypothèses de l’expérience**

- Équilibre atteint à chaque contact, phases de volumes constants et solvant neuf
- Espèce ionisée supposée aqueuse ; pH tamponné imposé, ni émulsion ni consommation du tampon ni dégradation dans le modèle

**Techniques à mobiliser**

- Conservation de quantité entre deux phases
- Henderson–Hasselbalch et partition
- Optimisation de contacts à volume total fixé

**Prédire → expérimenter → justifier**

1. Prévoir l’effet du pH sur acide puis amine et comparer une extraction de 100 mL à deux de 50 mL.
2. Faire varier nombre de contacts et pH ; relever D et masse restant dans l’eau.
3. Démontrer la fraction résiduelle, vérifier la conservation et nommer ce qui changerait si le tampon ou la séparation de phases devenait insuffisant.

**Niveaux et approfondissements**

- Sup : Ampoule à décanter et partage : TP PCSI.
- Spé : Séparations acido-basiques et bilans couplés dans une synthèse PC.
- Au-delà : Transfert de matière, solvants mutuellement solubles et procédés continus.

Leçons de référence : 16, 5, 41.

**Résultat attendu.** Une récupération prédite sous hypothèses et une sélection du pH fondée sur la forme chimique.

### Laboratoire `esterification`

Retrouver les leviers d’un TP d’ester : excès de réactif, eau initiale et équilibre. Le passage à la saponification fait distinguer une transformation réversible catalysée et un bilan basique pratiquement complet dans le modèle choisi.

![Illustration scientifique du laboratoire esterification](illustrations/esterification.svg)

**Objets et unités**

- Stocks de réactifs, ester et eau ; avancement et K sans unité pour le mélange homogène idéal
- Mode estérification/hydrolyse/saponification ; proportions et réactif limitant

**Hypothèses de l’expérience**

- Activités simplifiées du mélange homogène ; le modèle d’eau réactif n’est pas celui d’un solvant aqueux majoritaire
- Saponification modélisée stœchiométriquement complète pour le limitant ; la cinétique du reflux n’est pas une constante d’équilibre

**Techniques à mobiliser**

- Tableau d’avancement et K
- Déplacement par excès ou eau
- Distinction carboxylate/acide et traitement final

**Prédire → expérimenter → justifier**

1. Pour K=4 et stocks 1/1 sans produit initial, calculer x puis prévoir l’effet d’un excès d’alcool.
2. Comparer estérification, hydrolyse avec eau initiale et saponification ; relever les quantités de chaque forme.
3. Choisir la racine physique, vérifier tous les stocks et expliquer pourquoi catalyse accélère sans changer K, puis pourquoi acidifier un carboxylate est une étape supplémentaire.

**Niveaux et approfondissements**

- Sup : Équilibre et techniques de synthèse : PCSI.
- Spé : Substitution d’acyle, équilibres et optimisation des conditions : PC.
- Au-delà : Activités non idéales, séparation réactive et catalyse enzymatique.

Leçons de référence : 30, 5, 41.

**Résultat attendu.** Un avancement contrôlé et une interprétation distincte des trois bilans ester/acide/carboxylate.

### Laboratoire `acylation`

Construire une amide en comptant à la fois l’attaque et le piégeage de l’acidité libérée. La comparaison chlorure/anhydride et amine/base rappelle qu’un équivalent peut avoir un rôle de neutralisation sans être incorporé à la cible.

![Illustration scientifique du laboratoire acylation](illustrations/acylation.svg)

**Objets et unités**

- Stocks d’amine et de base en équivalents par rapport à l’acyle de référence ; chlorure, anhydride ou acide non activé
- Produit théorique, sel ammonium ou acidité résiduelle ; intermédiaire tétraédrique et sous-produit

**Hypothèses de l’expérience**

- Bilan choisi avec réactivité et base adaptées ; chlorure libère un équivalent acide à piéger
- Les bornes sont stœchiométriques et ne remplacent pas les équilibres, la solubilité et le rendement isolé

**Techniques à mobiliser**

- Addition–élimination d’acyle
- Rôle nucléophile/base de l’amine
- Activation et comptage des équivalents

**Prédire → expérimenter → justifier**

1. Prévoir combien d’équivalents d’amine servent à la cible puis au piégeage de HCl sans base externe.
2. Comparer chlorure et anhydride, ajouter une base séparée et lire le limitant avec des stocks identiques.
3. Écrire l’équation équilibrée et expliquer pourquoi acide+amine peut donner un sel avant l’amide, puis proposer une caractérisation de N-acylation.

**Niveaux et approfondissements**

- Sup : Activation de fonction et transfert de doublets, prérequis PCSI.
- Spé : Dérivés d’acides et substitutions d’acyle : PC.
- Au-delà : Couplage peptidique, agents activants et catalyse d’acylation.

Leçons de référence : 31, 32, 6.

**Résultat attendu.** Une quantité théorique qui respecte la neutralisation et un mécanisme où le groupe partant est identifié.

### Laboratoire `protection`

Évaluer une protection depuis les fonctions à préserver, les conditions à traverser et son coût global. Les séquences comparent un carbonyle masqué avant réduction, une déprotection trop précoce et un OH libre ou protégé avant l’étape organomagnésienne.

![Illustration scientifique du laboratoire protection](illustrations/protection.svg)

**Objets et unités**

- Fonctions présentes et ordre des opérations ; stabilité de l’acétal dans la banque
- Rendements déclarés par opération et rendement global ; étapes de traitement/protection/déprotection

**Hypothèses de l’expérience**

- Protection sélective fournie pour le cas étudié ; sa possibilité n’est pas généralisée à tous les dicarbonyles
- Compatibilité évaluée avec fonction et milieu ; les rendements sont des données de scénario, pas des prédictions ab initio

**Techniques à mobiliser**

- Matrice fonction/réactif/milieu
- Ordre de synthèse et isolement
- Produit des rendements et alternative compatible

**Prédire → expérimenter → justifier**

1. Repérer ce qui réagirait avec l’étape visée ; choisir un acétal pour préserver C=O ou le groupe fourni pour masquer OH.
2. Comparer les séquences correcte, sans protection et déprotégée trop tôt ; lire séparément les routes OH libre/organomagnésien et OH protégé.
3. Justifier chaque opération, vérifier la récupération de la fonction et calculer le rendement global. Les traitements anhydres et aqueux nécessaires sont explicités dans le cours.

**Niveaux et approfondissements**

- Sup : Protection/déprotection et stratégie : PCSI option PC.
- Spé : Polyfonctionnalité et sélectivité des routes de PC.
- Au-delà : Orthogonalité de protections et synthèses totales.

Leçons de référence : 33, 27, 40.

**Résultat attendu.** Une séquence complète compatible et un coût de protection évalué sans compter seulement les étapes.

### Laboratoire `aldol`

Former une liaison C−C en choisissant quel partenaire fournit l’énolate. La chalcone donne un cas emblématique où l’absence d’Hα du benzaldéhyde simplifie une réaction croisée ; l’aldol et le produit crotonisé restent clairement distincts.

![Illustration scientifique du laboratoire aldol](illustrations/aldol.svg)

**Objets et unités**

- Carbonyles donneur/accepteur et présence d’Hα ; mode de préparation de l’énolate et étape observée
- β-hydroxycarbonyle, liaison C−C nouvelle, eau de crotonisation et carbonyle α,β-insaturé

**Hypothèses de l’expérience**

- Choix de donneur et banque de conditions explicités ; sélectivité croisée ne suit pas automatiquement de deux carbonyles mélangés
- L’orientation E fréquente après déshydratation n’est pas un rendement ou un ratio universel

**Techniques à mobiliser**

- Énolate et sites α/β
- Suivi de la liaison C−C
- Distinction aldolisation/condensation complète

**Prédire → expérimenter → justifier**

1. Identifier Hα sur acétophénone et leur absence sur benzaldéhyde ; dessiner le β-hydroxyproduit.
2. Comparer aldol croisé et partenaires énolisables ; déclencher ou omettre la crotonisation.
3. Suivre chaque C et O, compter l’eau du bilan condensé et expliquer les auto/croisements possibles si les deux partenaires donnent un énolate.

**Niveaux et approfondissements**

- Sup : Mésomérie et nucléophile comme prérequis Sup ; réaction fournie pour l’entrée.
- Spé : Énolates, aldolisation et stratégie C−C : PC.
- Au-delà : Aldols énantiosélectives, modèles de transition et aldols intramoléculaires.

Leçons de référence : 34, 4.

**Résultat attendu.** Un donneur/accepteur choisi et deux produits distincts pour l’addition puis la déshydratation.

### Laboratoire `michaelwittig`

Comparer deux façons de construire C−C : ajouter à une énone en 1,2/1,4 ou remplacer l’oxygène d’un carbonyle par le C d’un ylure. Les produits servent à choisir une disconnexion plutôt qu’à mémoriser le même mot addition pour toutes les fonctions.

![Illustration scientifique du laboratoire michaelwittig](illustrations/michaelwittig.svg)

**Objets et unités**

- Accepteur conjugué, type de nucléophile et carbone attaqué ; carbonyle ou alcène restant
- Ylures CHCH₃ non stabilisé et CHCO₂Et stabilisé ; substituants de C=C et tendances E/Z qualitatives, sans ratio chiffré

**Hypothèses de l’expérience**

- Préférences 1,2/1,4 et E/Z rattachées aux conditions du scénario
- Une tendance d’ylure stabilisé/non stabilisé ne fournit pas une composition universelle ; Ph₃P=O figure dans le bilan

**Techniques à mobiliser**

- Repérage de sites 1 et 4
- Conservation du C introduit et O éliminé
- Sélectivité et coupure rétrosynthétique

**Prédire → expérimenter → justifier**

1. Dessiner les produits 1,2 et 1,4 d’une énone avant de choisir le donneur ; vérifier où reste C=O.
2. Comparer Michael et Wittig puis sélectionner les ylures non stabilisé CHCH₃ et stabilisé CHCO₂Et proposés.
3. Écrire le sous-produit phosphine-oxyde, décider si E/Z existe et proposer IR/RMN pour distinguer addition allylique et conjuguée. Le cas méthylène est un exercice complémentaire du cours.

**Niveaux et approfondissements**

- Sup : Nucléophile et carbonyle, avec une banque accompagnée.
- Spé : Michael, Wittig et choix des constructions C−C : PC selon transformations fournies.
- Au-delà : Annulations, ylures spécialisés et mécanismes de sélectivité avancés.

Leçons de référence : 35, 26, 34.

**Résultat attendu.** Une connectivité cible obtenue par la bonne famille, avec bilan d’atomes et limites de sélectivité.

### Laboratoire `dielsalder`

Construire un cycle en conservant la géométrie des partenaires, puis séparer préférence endo cinétique et stabilité exo éventuelle. L’exemple bicyclique associe stéréospécificité, s-cis et interactions orbitalaires à un bilan de six centres.

![Illustration scientifique du laboratoire dielsalder](illustrations/dielsalder.svg)

**Objets et unités**

- Diène et diénophile, disposition s-cis/s-trans, géométrie cis/trans des substituants
- Différence de barrières et de stabilités en kJ·mol⁻¹, température en K ; comparatifs endo/exo

**Hypothèses de l’expérience**

- Cycloaddition concertée [4+2] dans les scénarios fournis ; diène bloqué s-trans interdit dans ce chemin
- Rapport endo/exo de produits appliqué au cas bicyclique cis seulement ; fumarate trans garde un ester endo et l’autre exo. Comparaisons cinétique et thermodynamique indépendantes.

**Techniques à mobiliser**

- Numérotation de six centres
- Conservation stéréochimique et pont
- Rapports exponentiels de deux modèles

**Prédire → expérimenter → justifier**

1. Dessiner les deux liaisons σ nouvelles et la liaison π résiduelle ; prévoir la relation des substituants du maléate puis fumarate.
2. Comparer s-cis et s-trans ; dans le cas cyclopentadiène+maléate cis, faire varier les différences d’énergie endo/exo.
3. Conserver cis/trans du diénophile, calculer chaque rapport applicable avec RT et expliquer quand une rétro-réaction est nécessaire pour observer l’équilibre.

**Niveaux et approfondissements**

- Sup : Conformation/stéréochimie comme prérequis Sup ; cycloaddition introduite par sa banque.
- Spé : Diels–Alder et lecture HO/BV : PC.
- Au-delà : Catalyse asymétrique, demande électronique inverse et synthèses bicycliques.

Leçons de référence : 39, 38, 22.

**Résultat attendu.** Un adduit correctement connecté et deux préférences conditionnelles distinctes, sans règle endo absolue.

### Laboratoire `retrosynthese`

Choisir des coupures, reconstruire chaque route dans le sens direct et comparer une livraison de produit pur. Aspirine, paracétamol, chalcone et routes C−C/aromatiques font mobiliser compatibilités, ordre et indicateurs de matière.

![Illustration scientifique du laboratoire retrosynthese](illustrations/retrosynthese.svg)

**Objets et unités**

- Cible, précurseurs et banques de réaction ; étapes et rendements isolés déclarés en %
- Quantité de référence en mmol, nombre d’opérations et quantité obtenue ; l’économie d’atomes et le PMI sont étudiés dans le cours complémentaire

**Hypothèses de l’expérience**

- Routes définies et compatibles à vérifier ; rendements fournis, sans prédiction universelle de synthèse
- Rendements isolés multipliés sur une séquence ; le calcul de PMI/E-factor demande les données de masse supplémentaires fournies dans les exercices

**Techniques à mobiliser**

- Disconnexion et équivalent synthétique
- Reconstruction directe et ordre des fonctions
- Réactif limitant, pureté et bilan global

**Prédire → expérimenter → justifier**

1. Choisir une cible et proposer une coupure au niveau de la fonction construite ; lister les fonctions qu’elle doit épargner.
2. Comparer routes courtes et plus longues, dont acylation aromatique avant nitration ; modifier le rendement par opération et la quantité de référence.
3. Valider les étapes dans le sens direct, calculer le produit des rendements puis demander quelles mesures prouvent identité, pureté et quantité.

**Niveaux et approfondissements**

- Sup : Analyse de stratégie et TP : PCSI option PC.
- Spé : Rétrosynthèse multietapes, chimiosélectivité et évaluation de route : PC.
- Au-delà : Synthèse totale convergente, procédés et optimisation multicritère.

Leçons de référence : 40, 41, 36, 33.

**Résultat attendu.** Une route défendable par ses transformations et un bilan livré de produit pur.

### Laboratoire `polymeres`

Comprendre pourquoi une conversion de fonction très élevée et une stœchiométrie précise sont nécessaires aux longues chaînes. Le modèle par étapes transforme les bilans ester/amide en un degré moyen de polymérisation, puis le cours introduit les distributions de tailles.

![Illustration scientifique du laboratoire polymeres](illustrations/polymeres.svg)

**Objets et unités**

- Conversion p des fonctions limitantes et rapport de fonctions r≤1, sans unité ; monomères bifonctionnels
- DPn moyen, quantités de monomères/chaînes en mmol et nombre de chaînes actives imposé dans le modèle en chaîne ; distributions et dispersité dans le cours

**Hypothèses de l’expérience**

- Carothers : égalité de réactivité, bifonctionnalité, absence de cyclisation et bilan de fonctions défini
- Polymérisation en chaîne et par étapes distinguées ; distribution idéale ne décrit pas un réseau ramifié ou toute polymérisation radicalaire

**Techniques à mobiliser**

- Conservation des fonctions et chaînes
- Moyennes en nombre/masse
- Sensibilité à p et déséquilibre r

**Prédire → expérimenter → justifier**

1. Comparer p=0,9/0,99/0,999 à r=1 puis prévoir l’effet d’un ratio r=0,98.
2. Faire varier p et r ; lire DPn et les quantités, puis comparer les familles chaîne/étapes à nombre de chaînes actives imposé.
3. Retrouver Carothers et sa limite à p→1, expliquer ce que compte r et utiliser ensuite le problème du cours pour montrer pourquoi Xn seul ne décrit pas toutes les molécules.

**Niveaux et approfondissements**

- Sup : Fonctions organiques et stœchiométrie comme prérequis Sup ; introduction accompagnée.
- Spé : Macromolécules, synthèse et matériaux : parcours PC avec modèle fourni.
- Au-delà : Gélification, réseaux, polymérisations contrôlées et distributions mesurées.

Leçons de référence : 42, 31, 30.

**Résultat attendu.** Un matériau relié à un bilan de fonctions et à une distribution, avec les hypothèses de linéarité explicites.

## Les 60 exercices corrigés

### 1. Le nitro : octets, charges et formes limites

*Sup* — laboratoire `electrons`.

**Énoncé.** Construire deux formes de Lewis de CH₃NO₂ sans dépasser l’octet de N. Donner les charges formelles sur N et les deux O, compter les électrons de valence, puis expliquer pourquoi ces formes ne sont pas deux molécules en équilibre. Identifier la différence avec une tautomérie carbonyle/énol.

**Corrigé.** CH₃NO₂ possède 4+3×1+5+2×6=24 électrons de valence. Le N est lié au C, doublement à un O et simplement à l’autre : quatre liaisons, aucun doublet, donc qN=5−0−4=+1. O doublement lié a q=6−4−2=0 ; O simplement lié et portant trois doublets a q=6−6−1=−1. La deuxième forme échange les rôles des O, sans déplacer aucun noyau. Leur charge totale vaut 0 et chacune respecte l’octet. La molécule réelle est délocalisée ; ce dessin ne définit pas une conversion temporelle. Une tautomérie énol/carbonyle déplace un H et change une connectivité σ : elle relie des espèces distinctes, et exige un mécanisme de transfert de proton.

### 2. Une attaque sur C=O qui respecte l’octet

*Sup* — laboratoire `electrons`.

**Énoncé.** Pour l’addition de CH₃⁻, employé ici comme synthon, sur le méthanal, écrire l’intermédiaire avant puis après protonation. Décrire l’origine et la destination des deux flèches de la première étape. Vérifier charge et atomes. Préciser quel réactif équivalent pourrait remplacer le synthon dans une synthèse réalisable.

**Corrigé.** Le doublet du carbone de CH₃⁻ attaque le C de H₂C=O ; le doublet π C=O se déplace vers O. On obtient CH₃CH₂O⁻, qui possède une nouvelle liaison C−C et une liaison C−O simple ; C conserve quatre liaisons et O porte la charge −1. Ajouter un proton avec un donneur compatible après l’addition donne CH₃CH₂OH. Le bilan avant protonation conserve deux C, cinq H, un O et la charge −1. Un dessin qui garderait C=O tout en ajoutant CH₃ donnerait un C à cinq liaisons et doit être rejeté par l’octet. CH₃MgBr en milieu anhydre, puis hydrolyse/protonation terminale, est un équivalent synthétique du carbone nucléophile ; CH₃⁻ libre n’est pas le protocole proposé.

### 3. Une conversion acido-basique n’est pas une fraction de tampon

*Sup* — laboratoire `acidebase`.

**Énoncé.** À 25 °C en eau, mélanger des quantités équimolaires d’acide acétique et NH₃, sans produits initiaux. Les pKa fournis sont 4,76 et 9,25. Calculer K puis la fraction convertie avec activités assimilées aux concentrations. Comparer à la fraction d’acétate dans un tampon à pH=5,76.

**Corrigé.** La réaction CH₃CO₂H+NH₃⇌CH₃CO₂⁻+NH₄⁺ a K=10^(9,25−4,76)=10^4,49≈3,09×10⁴. Si f=x/c₀, les deux produits ont concentration x et les deux réactifs c₀−x, donc K=f²/(1−f)². Ainsi f=√K/(1+√K)≈0,9943, soit 99,43 %. Dans le tampon, le pH est imposé par un autre bilan : \[A⁻\]/\[HA\]=10^(5,76−4,76)=10, et fA⁻=10/11=90,91 %. Les valeurs diffèrent parce que le premier problème conserve deux stocks réactifs et produit les deux formes conjuguées, tandis que le second fixe une activité du proton. Utiliser K/(1+K) pour la conversion équimolaire confondrait ces conditions.

### 4. Basicité, nucléophilie et solvant

*Sup → PC* — laboratoire `acidebase`.

**Énoncé.** On veut substituer un bromure secondaire en limitant l’élimination. Comparer qualitativement I⁻ et tert-BuO⁻, puis expliquer pourquoi un classement de nucléophilie doit nommer un substrat et un solvant. Enfin, estimer l’équilibre entre aniline et acide acétique en eau, avec pKa(anilinium)=4,6 et pKa(acide)=4,8.

**Corrigé.** I⁻ est peu basique et polarisable : une substitution est plausible si l’accès au C est suffisant. tert-BuO⁻ est une base forte encombrée ; arracher Hβ et conduire à E2 peut être plus facile qu’attaquer ce C. Ce raisonnement ne garantit pas un rendement et doit être confronté à la classe du substrat, au solvant et à la température. La nucléophilie mesure une vitesse vers un électrophile donné ; la basicité compare un équilibre de protonation. Pour PhNH₂+CH₃CO₂H⇌PhNH₃⁺+CH₃CO₂⁻, K≈10^(4,6−4,8)=0,63. À stocks égaux idéaux, f=√0,63/(1+√0,63)≈44 %. La disponibilité de l’amine nucléophile dépend donc du milieu ; une acidification peut réduire fortement sa réactivité d’acylation.

### 5. SN2 : quand le pseudo-premier ordre est permis

*Sup* — laboratoire `sn2`.

**Énoncé.** Une SN2 a k₂=0,10 L·mol⁻¹·s⁻¹. Comparer a) \[S\]₀=0,010 mol·L⁻¹, \[Nu\]₀=1,00 mol·L⁻¹ ; b) deux concentrations initiales égales à 0,10 mol·L⁻¹. Calculer le temps de demi-réaction dans chaque approximation adaptée et indiquer une mesure qui teste l’ordre en nucléophile.

**Corrigé.** Dans a), consommer tout S ne réduit Nu que de 1 %. On peut prendre \[Nu\]≈1,00 mol·L⁻¹ : kobs=k₂\[Nu\]=0,10 s⁻¹, \[S\]=\[S\]₀e^(−kobs t) et t₁/₂=ln2/0,10=6,93 s. Dans b), \[Nu\]=\[S\] pendant la réaction, donc −d\[S\]/dt=k₂\[S\]² et 1/\[S\]−1/\[S\]₀=k₂t. À moitié, t₁/₂=1/(k₂\[S\]₀)=100 s. Utiliser une exponentielle dans b) donnerait une mauvaise loi. Pour tester l’ordre, mesurer v₀ à \[S\]₀ fixé et doubler \[Nu\]₀ : v₀ doit doubler dans le schéma SN2, tant que les autres conditions restent identiques. L’unité L·mol⁻¹·s⁻¹ de k₂ fournit un contrôle dimensionnel de ces deux calculs.

### 6. Williamson : choisir le bon côté de la coupure

*Sup* — laboratoire `sn2`.

**Énoncé.** Proposer une synthèse de l’éther tert-butyl méthylique par une SN2 de Williamson. Deux coupures sont envisagées : méthanolate+bromure tert-butylique, ou tert-butanolate+iodométhane. Choisir et justifier le couple. Que deviendrait la notion d’inversion si l’halogénure portait un centre stéréogène ?

**Corrigé.** La coupure favorable place le groupe le moins encombré sur l’électrophile : tert-BuO⁻+CH₃I→tert-BuOCH₃+I⁻. Le C méthyle est accessible à l’attaque arrière et ne porte pas de Cβ, donc aucune E2 de ce substrat ne concurrence l’attaque. Avec CH₃O⁻ et tert-BuBr, le C tertiaire est trop encombré pour la SN2 usuelle et la base peut arracher un Hβ pour former isobutène. L’encombrement du nucléophile tert-butanolate n’est pas nul mais l’électrophile méthyle rend la voie choisie beaucoup plus pertinente. Sur un C stéréogène accessible, une SN2 inverse la disposition géométrique ; le descripteur R/S doit être recalculé, car changer le groupe partant peut changer les priorités CIP.

### 7. Une solvolyse de premier ordre

*Sup* — laboratoire `sn1`.

**Énoncé.** Une solvolyse compatible avec une ionisation déterminante laisse 30 % du substrat après 80 s. Estimer k₁ et t₁/₂. La quantité restante change-t-elle si la concentration initiale est divisée par deux ? Discuter ce qu’un résultat de vitesse indépendant d’un nucléophile ajouté permet réellement de conclure.

**Corrigé.** La loi limite est \[S\](t)/\[S\]₀=e^(−k₁t). Donc k₁=−ln0,30/80≈0,01505 s⁻¹ et t₁/₂=ln2/k₁≈46,1 s. Diviser \[S\]₀ par deux conserve la fraction restante à un temps donné, mais divise sa concentration absolue et sa vitesse initiale par deux. L’indépendance de la vitesse envers un nucléophile appuie une ionisation déterminante suivie d’un piégeage rapide, à conditions d’ionisation constantes. Elle ne prouve pas seule la présence d’un cation entièrement libre : paire d’ions, étape précédente et voies parallèles demandent des observations supplémentaires. Il faut examiner réarrangements éventuels et stéréochimie plutôt que transformer une seule mesure d’ordre en identification unique du mécanisme.

### 8. Carbocation et déplacement d’hydrure

*Sup → PC* — laboratoire `sn1`.

**Énoncé.** Le départ d’un groupe X sur 3-méthylbutan-2-yl peut former un carbocation secondaire. Dessiner le squelette initial, proposer une migration d’hydrure permettant un cation plus substitué puis les produits de capture par l’eau. Expliquer pourquoi une SN2 sur le même substrat ne passe pas par cette séquence.

**Corrigé.** Le substrat est CH₃−CH(X)−CH(CH₃)−CH₃. Après départ de X⁻, la charge est sur C2 : CH₃−CH⁺−CH(CH₃)−CH₃. Une migration du H lié à C3 vers C2 déplace le doublet C3−H et la charge vers C3 : CH₃−CH₂−C⁺(CH₃)−CH₃, cation tertiaire. La capture d’eau puis déprotonation donne 2-méthylbutan-2-ol ; une capture avant migration peut donner 3-méthylbutan-2-ol. La proportion dépend des vitesses concurrentes. La SN2 combine attaque et départ dans une étape, sans minimum carbocationique : cette migration d’un intermédiaire n’appartient pas à son schéma. Conserver les cinq C et tous les H montre que l’hydrure migre en interne et n’est pas ajouté depuis le solvant.

### 9. Conversion, sélectivité et rendement de produit

*Sup → PC* — laboratoire `competition`.

**Énoncé.** Deux voies parallèles irréversibles consomment S avec λSN2=0,060 s⁻¹ et λE2=0,020 s⁻¹. À t=20 s, déterminer conversion, fractions des produits formés et quantité de produit SN2 rapportée au stock initial. Une purification récupère 85 % de ce produit ; déterminer le rendement isolé correspondant.

**Corrigé.** λtotal=0,080 s⁻¹, donc \[S\]/\[S\]₀=e^(−1,6)=0,2019 et la conversion vaut 79,81 %. La sélectivité parmi les produits est λSN2/λtotal=0,75 pour substitution et 0,25 pour élimination, car les deux flux suivent le même stock S. Le produit de substitution représente 0,7981×0,75=0,5986, soit 59,86 % du stock initial. Une récupération de 85 % ramène le rendement isolé à 0,5986×0,85=50,88 %. Annoncer 75 % comme rendement isolé confondrait sélectivité, conversion et récupération. Ce calcul dépend de chemins parallèles sans retour ni transformation des produits ; il ne peut être extrapolé à une synthèse dont les constantes ne sont pas connues.

### 10. Détecter deux chemins avec l’ordre apparent

*PC* — laboratoire `competition`.

**Énoncé.** Une consommation suit v=\[S\](k₁+k₂\[Nu\]) avec k₁=0,010 s⁻¹ et k₂=0,20 L·mol⁻¹·s⁻¹. Calculer kobs et la fraction attribuée au chemin bimoléculaire pour \[Nu\]=0,05 puis 0,20 mol·L⁻¹. Quel graphe permet d’identifier les deux contributions et quelle interprétation microscopique demeure à vérifier ?

**Corrigé.** À 0,05 mol·L⁻¹, k₂\[Nu\]=0,010 s⁻¹ : kobs=0,020 s⁻¹ et le chemin bimoléculaire contribue 50 %. À 0,20 mol·L⁻¹, il contribue 0,040 s⁻¹ : kobs=0,050 s⁻¹ et sa fraction vaut 80 %. Le graphe kobs en fonction de \[Nu\] est une droite d’ordonnée à l’origine k₁ et de pente k₂. Deux concentrations ne suffisent pas à contrôler parfaitement une linéarité ; plusieurs points et incertitudes sont souhaitables. On peut proposer une voie unimoléculaire parallèle à une voie bimoléculaire, puis vérifier produits et stéréochimie pour les relier à SN1/SN2 ou à d’autres chemins. L’ordre apparent varie avec \[Nu\] : il n’est pas un entier unique décrivant tout le domaine de compétition.

### 11. E2 : déduire la géométrie avant Zaitsev

*Sup → PC* — laboratoire `elimination`.

**Énoncé.** Énumérer les alcènes possibles par E2 du 2-bromobutane. Préciser le H retiré pour chaque connectivité et expliquer pourquoi E/Z-but-2-ène demandent deux arrangements anti distincts. Une base volumineuse peut-elle modifier la distribution sans supprimer l’exigence anti ?

**Corrigé.** Le substrat CH₃−CHBr−CH₂−CH₃ porte des Hβ sur C1 et C3. Retirer un H de C1 forme CH₂=CH−CH₂−CH₃, but-1-ène, sans E/Z parce qu’un C porte deux H. Retirer un H de C3 forme CH₃−CH=CH−CH₃, but-2-ène E ou Z selon la conformation présentant ce H anti à Br. Une projection Newman sur C2−C3 permet de placer Br devant et le H opposé derrière, puis de suivre les positions des CH₃ lors de l’aplatissement. Une petite base favorise souvent le produit plus substitué ; une base encombrée peut arracher plus facilement un H terminal et accroître le but-1-ène. Elle ne rend pas toutes les orientations de liaison équivalentes : l’exigence de recouvrement anti reste dans le mécanisme E2 usuel.

### 12. Trans-diaxial : un produit moins substitué imposé

*PC* — laboratoire `elimination`.

**Énoncé.** Pour trans-1-bromo-2-méthylcyclohexane, construire les deux chaises en gardant Br et CH₃ sur des faces opposées. Identifier la chaise réactive pour E2 et les Hβ anti disponibles. Le produit issu de l’élimination vers C2, plus substitué, est-il accessible dans cette chaise ?

**Corrigé.** Le trans-1,2 possède une chaise diéquatoriale et, après basculement, une chaise diaxiale. En diéquatorial, Br n’est pas axial et l’E2 trans-diaxiale n’est pas disponible dans la géométrie usuelle. En diaxial, Br est axial en C1 et CH₃ axial de direction opposée en C2 ; le site axial anti de C2 est donc occupé par CH₃, et son H équatorial n’offre pas l’alignement requis. C6 possède en revanche un H axial anti à Br, permettant l’alcène entre C1 et C6. La voie vers C2 plus substituée est supprimée dans ce modèle de chaise, même si sa stabilité pourrait la favoriser après une autre voie ou une isomérisation. Ce contre-exemple montre pourquoi Zaitsev compare des chemins géométriquement autorisés et ne remplace pas le dessin des H.

### 13. Deux but-2-ènes et une bromation anti

*PC* — laboratoire `alcene`.

**Énoncé.** Comparer la bromation par Br₂ de E-but-2-ène et de Z-but-2-ène en milieu achiral, en supposant le mécanisme bromonium puis ouverture anti. Dessiner les stéréoisomères et expliquer pourquoi la stéréospécificité ne signifie pas qu’une réaction ne donne jamais deux produits.

**Corrigé.** Le bromonium ponté peut être formé depuis les deux faces, puis Br⁻ ouvre depuis la face opposée. Pour E-but-2-ène, les deux attaques anti conduisent à la même forme méso du 2,3-dibromobutane : ses centres ont configurations (2R,3S), équivalentes par symétrie à (2S,3R). Pour Z-but-2-ène, les produits sont (2R,3R) et (2S,3S), une paire d’énantiomères en proportions égales dans les hypothèses achirales. Ces deux réactifs stéréoisomères conduisent à des ensembles de produits différents : c’est la stéréospécificité. Elle est compatible avec une paire de produits pour l’un d’eux. Une indication « anti » seule ne fournit pas immédiatement R/S ; il faut dessiner les groupes et appliquer leurs priorités.

### 14. Un alcène, trois orientations à expliquer

*PC* — laboratoire `alcene`.

**Énoncé.** À partir du propène, comparer les produits attendus par a) hydratation acide ; b) hydroboration puis oxydation ; c) HBr ionique. Donner pour chaque voie le rôle de la liaison π, l’intermédiaire ou l’étape concertée et la fonction finale. La voie b ajoute-t-elle deux OH ?

**Corrigé.** La liaison π fournit des électrons dans chaque voie. En a), une protonation conduisant au cation secondaire puis une attaque d’eau et déprotonation donnent propan-2-ol : orientation Markovnikov dans ce schéma. En b), une addition concertée de H−B place préférentiellement B sur le C terminal ; l’oxydation remplace B par OH et donne propan-1-ol, anti-Markovnikov. H ajouté et OH final sont syn dans le suivi stéréochimique ; un seul OH est ajouté, ce n’est pas une dihydroxylation. En c), protonation puis capture par Br⁻ donnent principalement 2-bromopropane. Le propène ne crée pas ici de centre chiral dans a ou c. Les conditions annoncées distinguent ces voies ; le nom du substrat seul ne définit ni l’orientation ni le mécanisme.

### 15. Réduction partielle d’une triple liaison

*PC* — laboratoire `alcyne`.

**Énoncé.** Construire Z-but-2-ène, E-but-2-ène puis butane à partir du but-2-yne, à l’aide d’une banque donnant H₂/Lindlar, une réduction par métal dissous et H₂/catalyseur non sélectif. Expliquer pourquoi « un équivalent d’H₂ » sans indication de catalyseur n’est pas un protocole suffisant.

**Corrigé.** Le but-2-yne CH₃−C≡C−CH₃ donne Z-but-2-ène par l’addition syn d’H₂ sur catalyseur de Lindlar, choisi pour arrêter la réduction au stade alcène. Une réduction partielle par métal dissous dans les conditions fournies conduit globalement à l’addition anti et à E-but-2-ène. Un catalyseur d’hydrogénation non sélectif avec assez de H₂ permet l’addition de deux molécules et donne butane. Le bilan est donc une ou deux additions, mais la répartition de réactif entre molécules compte : avec un catalyseur qui réduit rapidement l’alcène, un équivalent global peut produire un mélange d’alcyne restant et d’alcane plutôt qu’un alcène pur. L’arrêt sélectif dépend de la cinétique et du catalyseur, pas de la stœchiométrie seule.

### 16. L’énol doit être redessiné

*PC* — laboratoire `alcyne`.

**Énoncé.** Une banque donne l’hydratation acide catalysée par Hg²⁺ d’un alcyne terminal. Appliquer au prop-1-yne puis à l’acétylène, dessiner l’énol et le produit carbonylé. Comparer à une hydroboration/oxydation adaptée du prop-1-yne. Pourquoi ces couples énol/carbonyle ne sont-ils pas mésomères ?

**Corrigé.** Pour CH₃−C≡CH, l’hydratation Markovnikov forme l’énol CH₃−C(OH)=CH₂, qui tautomérise en CH₃−CO−CH₃, propanone. Pour HC≡CH, l’énol CH₂=CHOH donne CH₃CHO, éthanal : il ne faut donc pas annoncer une méthylcétone sans cette exception. Une hydroboration/oxydation adaptée du prop-1-yne place OH sur le C terminal dans l’énol CH₃−CH=CHOH, puis donne CH₃CH₂CHO, propanal. Chaque tautomérie déplace un H et modifie une liaison σ O−H/C−H en plus de π ; elle relie des espèces constitutionnellement distinctes. Une mésomérie n’aurait déplacé que des électrons à noyaux fixes. Le carbone terminal de l’alcyne doit être suivi jusqu’au produit pour éviter une inversion de fonction finale.

### 17. Fermer une chaîne radicalaire

*PC* — laboratoire `radical`.

**Énoncé.** Écrire deux étapes de propagation conduisant du propène et HBr au 1-bromopropane en présence d’un initiateur adapté. Identifier le radical carboné et vérifier le bilan net. Proposer une terminaison et expliquer pourquoi le résultat ne se transpose pas automatiquement à HCl.

**Corrigé.** Br· attaque le C terminal de CH₂=CHCH₃ : BrCH₂−CH·−CH₃ est le radical secondaire. Celui-ci prend H à HBr : BrCH₂CH₂CH₃+Br·. Additionner les deux équations annule Br· et l’intermédiaire ; le bilan est propène+HBr=1-bromopropane. Coupler deux radicaux carbonés ou deux Br· constitue une terminaison, qui consomme deux porteurs de chaîne au lieu d’en régénérer un. L’orientation découle du radical formé, sans carbocation. Une chaîne efficace exige que ses étapes de propagation soient suffisamment favorables et rapides ; les énergies de liaison H−Cl, H−Br, H−I et les additions radicalaires diffèrent. La seule présence d’un peroxyde ne justifie donc pas le même bilan utile avec tous les HX.

### 18. Une racine carrée qui révèle la terminaison

*PC — prolongement quantitatif* — laboratoire `radical`.

**Énoncé.** Un modèle stationnaire prend Ri=2×10⁻⁸ mol·L⁻¹·s⁻¹, kt=10⁷ L·mol⁻¹·s⁻¹ et Ri=2kt\[R·\]². Calculer \[R·\]. Si la propagation vaut v=kp\[S\]\[R·\], que devient v quand Ri est multiplié par 9 ? Donner les conditions d’application et le sens d’une très faible concentration radicalaire.

**Corrigé.** La conservation stationnaire donne \[R·\]=√(Ri/(2kt))=√(10⁻¹⁵)=3,16×10⁻⁸ mol·L⁻¹. L’unité suit (mol·L⁻¹·s⁻¹)/(L·mol⁻¹·s⁻¹)=mol²·L⁻² avant la racine. À kp et \[S\] inchangés, v est proportionnelle à √Ri : multiplier Ri par 9 multiplie v par 3, pas par 9. Le résultat suppose régime après initiation initiale, terminaison principalement bimoléculaire entre les radicaux considérés, absence d’inhibiteur dominant et substrat encore disponible. Une concentration minuscule ne signifie pas absence de réaction : le même radical peut effectuer de nombreux cycles de propagation avant terminaison. La convention du facteur 2 doit être conservée entre définition de Ri et équation de terminaison.

### 19. Carbonyle, hydrure et stéréochimie

*Sup* — laboratoire `carbonyle`.

**Énoncé.** Réduire propanone puis butan-2-one par un transfert d’hydrure suivi de protonation. Dessiner les charges et indiquer s’il se crée un centre stéréogène. Dans un milieu achiral, quelle composition stéréochimique est attendue pour le butan-2-ol isolé ? Quelle donnée supplémentaire pourrait rendre les faces inéquivalentes ?

**Corrigé.** L’hydrure fournit une paire à C=O tandis que π se déplace vers O. Propanone donne (CH₃)₂CH−O⁻ puis propan-2-ol ; le C porte deux CH₃ identiques et n’est pas stéréogène. Butan-2-one donne CH₃−CH(O⁻)−CH₂CH₃ puis butan-2-ol ; le C porte OH, H, CH₃ et CH₂CH₃, quatre groupes différents. Ses deux faces équivalentes dans les hypothèses achirales conduisent à un racémique R/S. Un centre chiral préexistant, un réducteur chiral, une enzyme ou un environnement asymétrique peut les différencier et produire un excès. Il faut écrire le traitement de protonation : l’alcoolate n’est pas déjà l’alcool neutre, et H⁻ ne joue pas le rôle de H⁺ dans l’étape d’addition.

### 20. Une addition ne signifie pas une substitution d’acyle

*Sup → PC* — laboratoire `carbonyle`.

**Énoncé.** Comparer l’attaque d’un nucléophile sur propanone et sur éthanoate d’éthyle. Identifier l’intermédiaire tétraédrique dans les deux cas, puis expliquer pourquoi un départ restaurateur du carbonyle est disponible dans l’ester. Avec CH₃MgBr en excès, donner le produit final à partir de cet ester après hydrolyse.

**Corrigé.** Dans les deux attaques, Nu vise le C carbonyle et O reçoit les électrons π. Propanone forme un alcoolate (CH₃)₂C(O⁻)Nu ; ses substituants carbonés ne sont pas des groupes partants ordinaires, donc une simple protonation donne l’alcool d’addition. L’ester CH₃COOEt donne CH₃C(O⁻)(Nu)OEt, qui peut reformer C=O en expulsant EtO⁻ : il s’agit d’addition puis élimination, bilan de substitution d’acyle. Avec Nu apporté par CH₃MgBr, cette étape forme propanone, plus réactive que l’ester, puis une seconde addition donne (CH₃)₃CO⁻ avant hydrolyse en tert-butanol. Deux équivalents de carbone nucléophile sont consommés par ester. S’arrêter à la cétone ne constitue pas la voie usuelle avec cet organomagnésien en excès.

### 21. Trois coupures d’un alcool tertiaire

*Sup* — laboratoire `grignard`.

**Énoncé.** La cible est 2-phénylbutan-2-ol, Ph−C(OH)(CH₃)(CH₂CH₃). Donner trois couples cétone/organomagnésien correspondant aux trois coupures C−C autour du C portant OH. Choisir une proposition simple et indiquer traitement final et incompatibilités qui doivent être contrôlées.

**Corrigé.** Couper la liaison avec Ph donne butan-2-one+PhMgX ; couper avec CH₃ donne propiophénone PhCOCH₂CH₃+CH₃MgX ; couper avec CH₂CH₃ donne acétophénone PhCOCH₃+C₂H₅MgX. Dans chaque cas, le C carbonyle devient le C tertiaire porteur de OH après addition puis hydrolyse/protonation. Le couple acétophénone/éthylmagnésien est une route conceptuellement simple à partir d’espèces courantes. Il faut un milieu et un matériel adaptés anhydres, aucune fonction protonique libre ni autre électrophile incompatible, puis un traitement aqueux terminal distinct. La cible possède un centre stéréogène car les trois groupes carbonés diffèrent ; sans source chirale, les deux faces du carbonyle conduisent normalement à un racémique. Les trois coupures sont possibles conceptuellement, sans garantir les mêmes rendements.

### 22. Un ester et un proton labile dans le même bilan

*Sup → PC* — laboratoire `grignard`.

**Énoncé.** On dispose de 10 mmol d’un ester simple et de 25 mmol de RMgX. Un contaminant protonique HA représente 8 mmol et consomme un équivalent de RMgX par proton. Dans un modèle bilan sans autre réaction, quelle quantité maximale de produit tertiaire l’ester peut-il donner ? Où vont les autres atomes de l’ester ?

**Corrigé.** Après consommation de HA, il reste 25−8=17 mmol de RMgX disponibles pour l’addition. Un ester simple R′COOR″ demande normalement deux équivalents pour former R′C(OH)R₂ : nmax=min(10,17/2)=8,5 mmol dans ce modèle. Le groupe OR″ est expulsé sous forme alcoolate/sels puis donne R″OH lors du traitement ; le C et O du carbonyle deviennent ceux du centre alcool tertiaire. Le déficit peut laisser aussi des intermédiaires ou des mélanges dans une expérience réelle, donc 8,5 mmol est une borne stœchiométrique et non une prédiction de pureté. L’anhydrie et l’élimination des H labiles évitent une consommation chimique concurrente avant la création C−C. L’hydrolyse terminale est volontairement effectuée après l’addition, pas au départ.

### 23. Réduire le nitrobenzène : électrons puis quantités

*Sup → PC* — laboratoire `oxydoreduction`.

**Énoncé.** Équilibrer en milieu acide PhNO₂→PhNH₂ avec H₂O, H⁺ et e⁻. Un métal Sn est supposé s’oxyder uniquement en Sn⁴⁺. Écrire le bilan pour deux nitrobenzènes. Avec 20 mmol de PhNO₂ et 24 mmol de Sn, déterminer une borne de quantité d’aniline avant protonation acido-basique.

**Corrigé.** La demi-équation est PhNO₂+6H⁺+6e⁻→PhNH₂+2H₂O. Sn→Sn⁴⁺+4e⁻ ; pour annuler 12 électrons, multiplier la première par 2 et la seconde par 3 : 2PhNO₂+3Sn+12H⁺→2PhNH₂+3Sn⁴⁺+4H₂O. Atomes et charge +12 sont conservés. Le ratio Sn/aniline est 3/2, donc 24 mmol de Sn permettent au plus 16 mmol d’aniline, contre 20 mmol par le nitrobenzène : Sn est limitant dans les hypothèses. En milieu fortement acide, PhNH₂ se protonne en PhNH₃⁺ ; si cette espèce est le produit écrit, ajouter un proton par molécule dans le bilan. Des états d’oxydation métalliques différents ou des réactions parasites exigeraient un autre modèle stœchiométrique.

### 24. Réduire la cétone en conservant l’ester

*Sup option PC* — laboratoire `oxydoreduction`.

**Énoncé.** Une molécule porte une cétone et un ester. Une banque fournit NaBH₄ dans ses conditions usuelles et LiAlH₄ dans un solvant anhydre adapté. Choisir pour produire un hydroxyester puis proposer des observations IR/RMN validant la chimiosélectivité. Pourquoi un alcool tertiaire ne s’oxyde-t-il pas simplement en cétone à squelette conservé ?

**Corrigé.** NaBH₄ est le choix usuel pour réduire la cétone sans réduire un ester simple dans les conditions fournies ; LiAlH₄ est plus réactif et peut modifier aussi l’ester. L’hydrure attaque le carbonyle de cétone, puis la protonation donne OH. On attend disparition ou forte diminution de sa bande C=O, conservation de la bande d’ester et apparition d’une signature OH ; la RMN doit montrer le nouvel environnement CH−OH si le C porte H et conserver les groupes ester. Une seule tache de CCM ne prouve pas cette connectivité. Un tertiaire R₃COH ne possède aucun H sur ce C : former R₂C=O tout en conservant trois liaisons C−C serait incompatible avec l’octet ; une oxydation forte doit alors rompre ou réorganiser le squelette. La règle d’oxydation douce n’affirme pas une inertie absolue envers tout oxydant.

### 25. L’ordre nitration/acylation compte

*PC* — laboratoire `aromatique`.

**Énoncé.** Construire une route conceptuelle benzène→m-nitroacétophénone avec une banque nitration et acylation de Friedel–Crafts. Comparer les deux ordres possibles. Donner le rôle de l’intermédiaire σ et expliquer pourquoi la direction méta ne suffit pas à conclure que toute transformation aromatique ultérieure est possible.

**Corrigé.** Acyler d’abord le benzène en acétophénone PhCOCH₃, puis nitrer : le groupe COCH₃ est attracteur −M et désactive les positions ortho/para plus fortement dans les complexes σ, de sorte que méta est favorisé. Nitrer d’abord forme nitrobenzène, fortement désactivé ; une acylation de Friedel–Crafts usuelle n’est alors pas une étape viable à supposer. Dans une SEA, l’attaque forme un complexe σ non aromatique, puis le départ de H⁺ restaure l’aromaticité. L’orientation compare les voies lorsque la réaction est accessible ; l’activation globale compare leurs vitesses au benzène et peut empêcher une réaction donnée. La route doit donc être reconstruite dans le sens direct avec sa banque de conditions, pas validée uniquement par la position finale des substituants.

### 26. Les halogènes dirigent sans activer

*PC* — laboratoire `aromatique`.

**Énoncé.** Comparer les effets de OMe, NO₂ et Br sur une SEA. Les groupes Br et OMe dirigent tous deux ortho/para : sont-ils également activants ? On attribue deux dipôles identiques de module μ à un benzène disubstitué avec angle θ ; exprimer leur somme et dire quelle information manque pour en déduire des proportions de synthèse.

**Corrigé.** OMe donne par +M et active souvent le noyau ; NO₂ attire par −M et −I, désactive et favorise méta. Br attire par −I tout en possédant une donation de doublet +M : il désactive globalement mais dirige ortho/para. Orientation et activation sont donc des propriétés distinctes. Deux vecteurs de module μ à angle θ ont un module résultant |μtotal|=√(2μ²+2μ²cosθ)=2μ|cos(θ/2)| dans ce modèle vectoriel. Ce calcul décrit un dipôle de structure donnée ; il ne fournit ni les ΔG‡ des voies de formation ni leur réversibilité. Les proportions cinétiques exigent des constantes de vitesse ou barrières, les proportions à l’équilibre des énergies libres des isomères. Mesurer un dipôle peut caractériser une structure sans mesurer sa vitesse de formation.

### 27. Normaliser une combinaison non orthogonale

*PC — guidé* — laboratoire `orbitales`.

**Énoncé.** Deux orbitales réelles normalisées possèdent un recouvrement S=0,30. Normaliser φA+φB et φA−φB, calculer la norme qu’auraient les combinaisons divisées simplement par √2 et discuter le comportement quand S tend vers 1. Les signes des lobes correspondent-ils à des charges ?

**Corrigé.** L’intégrale de |φA+φB|² est 2+2S=2,60 ; celle de |φA−φB|² vaut 2−2S=1,40. Les combinaisons normalisées sont donc (φA+φB)/√2,60 et (φA−φB)/√1,40, avec dénominateurs 1,612 et 1,183. Les diviser par √2 donnerait des normes carrées 1+S=1,30 et 1−S=0,70, donc une normalisation incorrecte lorsque S≠0. Quand S→1, les fonctions deviennent presque redondantes et le dénominateur antisymétrique tend vers zéro : la base est mal conditionnée, non un générateur physique d’énergie infinie. Les signes représentent des phases d’amplitude ; la densité est |ψ|² et ne porte pas ce signe. Multiplier toute l’orbitale par −1 ne change aucune densité observée.

### 28. Le butadiène comme problème de valeurs propres

*PC — guidé* — laboratoire `orbitales`.

**Énoncé.** On fournit Ej=α+2βcos(jπ/5), j=1..4, β=−2,50 eV pour un modèle Hückel du butadiène. Donner les niveaux relatifs à α, remplir quatre électrons, calculer l’écart HO/BV et une longueur d’onde associée hc=1240 eV·nm. Cette estimation est-elle un spectre UV expérimental complet ?

**Corrigé.** Les cosinus donnent les facteurs 1,618 ; 0,618 ; −0,618 ; −1,618. Puisque β<0, les niveaux croissants sont α−4,045, α−1,545, α+1,545 et α+4,045 eV. Quatre électrons occupent les deux premiers avec deux électrons par orbitale ; HO est le deuxième, BV le troisième. Leur écart vaut 3,090 eV et λ≈1240/3,090=401 nm si l’on assimile cet écart à une transition permise. Il s’agit d’une illustration de remplissage et de dimensionnement, non d’une valeur tabulée du butadiène réel : le β choisi, les interactions électroniques, la géométrie, les règles de transition et la relaxation ne sont pas décrits complètement. La connectivité et l’orthonormalité de la base doivent être déclarées avant cette diagonalisation.

### 29. Deux barrières et deux stabilités

*PC* — laboratoire `cinetique`.

**Énoncé.** À 298 K, deux voies irréversibles de mêmes préfacteurs ont ΔG‡A=60 et ΔG‡B=65 kJ·mol⁻¹. Calculer la fraction initiale de A. Si les produits s’interconvertissent ensuite et B est plus stable de 8 kJ·mol⁻¹, calculer la fraction de B à l’équilibre. Donner les hypothèses supplémentaires du second résultat.

**Corrigé.** RT=8,314×298/1000≈2,478 kJ·mol⁻¹. kA/kB=exp((65−60)/RT)≈7,52 ; parmi les produits nouvellement formés, fA=7,52/(1+7,52)=88,3 %. À l’équilibre, GB−GA=−8 kJ·mol⁻¹ donc B/A=exp(8/RT)≈25,2 et fB≈96,2 %. La composition finale oppose ainsi préférence cinétique pour A et préférence thermodynamique pour B. Le second calcul exige des produits capables de s’interconvertir ou de retourner à un réseau commun, assez de temps, température constante et activités comparables dans l’état standard choisi. Chauffer ou attendre ne garantit pas l’équilibre si la barrière de retour reste inaccessible. Une catalyse modifie l’approche de cet équilibre sans changer le rapport thermodynamique à T fixée.

### 30. Une expérience qui identifie l’énergie d’activation

*Sup option PC → PC* — laboratoire `cinetique`.

**Énoncé.** Une constante de même ordre passe de k₁=0,010 à k₂=0,040 lorsque T passe de 298 à 318 K. Utiliser Arrhenius à préfacteur constant pour estimer Ea. Expliquer pourquoi comparer les logarithmes d’une constante de premier ordre et d’une constante de second ordre serait une opération différente, et proposer un contrôle expérimental.

**Corrigé.** ln(k₂/k₁)=Ea/R(1/T₁−1/T₂). Ici ln4=1,386 et 1/298−1/318≈2,110×10⁻⁴ K⁻¹ ; Ea≈8,314×1,386/(2,110×10⁻⁴)=54,6 kJ·mol⁻¹. Le ratio est sans dimension parce que k₁ et k₂ ont le même type et les mêmes unités. Une constante s⁻¹ ne peut être rapportée sans précision à une constante L·mol⁻¹·s⁻¹ : il faudrait définir les concentrations et les constantes apparentes pertinentes. Plusieurs températures permettent de tester une droite ln k contre 1/T et d’estimer une incertitude. Un changement de mécanisme, de solubilité ou de régime de diffusion peut courber cette droite, donc deux points ne démontrent pas la constance de Ea sur une large plage.

### 31. Une formule qui ne suffit pas à une identité

*Sup* — laboratoire `formule`.

**Énoncé.** Une espèce neutre a formule C₈H₈O₂. Calculer son indice d’insaturation. Proposer deux connectivités incluant un cycle benzénique et un carbonyle, puis indiquer quelles différences IR/RMN permettent de choisir entre benzoate de méthyle et acide phénylacétique. Préciser quel pic attendre pour \[M+H\]⁺ si M nominal vaut 136.

**Corrigé.** IHD=(2×8+2−8)/2=5 : benzène utilise quatre unités, C=O une. Benzoate de méthyle PhCOOCH₃ et acide phénylacétique PhCH₂CO₂H possèdent cette formule. Le premier donne un OCH₃ singulet 3H et une fonction ester ; le second un CH₂ benzylique 2H et un proton acide échangeable, avec une bande OH carboxylique très large. Tous deux ont cinq H aromatiques : ce seul massif ne les distingue pas. Un ion \[M+H\]⁺ de charge +1 se trouve nominalement à m/z=137, pas 136, tandis qu’un ion moléculaire M⁺· serait à 136. Il faut donc nommer la méthode d’ionisation et ne pas assimiler masse moyenne, masse exacte et m/z. Ces connectivités respectent les huit C et l’IHD, mais les données supplémentaires font l’identité.

### 32. Compter les halogènes par les enveloppes isotopiques

*Sup → PC* — laboratoire `formule`.

**Énoncé.** Une enveloppe M, M+2, M+4 est proche de 9:6:1 ; une autre proche de 1:2:1. Interpréter avec les approximations abondance Cl=3:1 et Br=1:1. Pour une molécule contenant un Cl et un Br, calculer l’enveloppe prévue. Que manque-t-il pour lire toute une spectrométrie de masse réelle ?

**Corrigé.** Deux Cl donnent (3+x)²=9+6x+x² : les coefficients 9:6:1 correspondent aux nombres de noyaux lourds 0,1,2. Deux Br donnent (1+x)²=1+2x+x², donc 1:2:1. Un Cl et un Br donnent (3+x)(1+x)=3+4x+x², soit 3:4:1. L’écart de masse est environ 2 unités par isotope lourd dans cette lecture nominale. Les sommes normalisent les intensités si l’on veut des fractions : pour le mélange Cl/Br, 3/8,4/8,1/8. Une enveloppe réelle contient aussi ¹³C, autres isotopes, résolution finie, fragments pouvant perdre un halogène et parfois plusieurs ions ; le motif est un indice de composition de l’ion étudié, pas une attribution unique de structure moléculaire.

### 33. Polarimétrie et excès énantiomérique

*Sup* — laboratoire `stereo`.

**Énoncé.** Pour un couple d’énantiomères, l’échantillon pur R tourne de +10,0° dans les conditions de mesure. Un mélange ne contenant que R et S, de même concentration totale et même trajet, tourne de +3,0°. Déterminer ee et proportions. La configuration R serait-elle toujours positive ? Reprendre si une impureté achirale dilue la concentration sans correction.

**Corrigé.** À composition et réponse linéaires, αmélange=(xR−xS)αR,pur. Avec xR+xS=1, xR−xS=0,30, donc ee=30 %, xR=0,65 et xS=0,35. Le signe + indique seulement l’énantiomère majoritaire pour la référence donnée ; R ne signifie pas dextrogyre en général. Si une impureté achirale diminue la concentration réelle en analyte mais que l’on compare à une référence plus concentrée, une rotation plus faible peut venir de la dilution autant que d’un ee plus faible. Il faut connaître concentration, longueur du trajet, solvant, température, longueur d’onde et pureté avant d’en déduire les proportions. Le laboratoire paramètre une rotation de référence explicitement et ne fabrique pas une relation universelle R=+.

### 34. Deux centres ne donnent pas toujours quatre molécules

*Sup* — laboratoire `stereo`.

**Énoncé.** Compter les stéréoisomères de l’acide tartrique HO₂C−CH(OH)−CH(OH)−CO₂H. Classer les paires et expliquer pourquoi la forme (R,S) peut être achirale. Comparer à une chaîne dissymétrique ayant deux centres indépendants et des extrémités différentes.

**Corrigé.** Les configurations formelles sont (R,R), (S,S), (R,S) et (S,R), mais les extrémités identiques permettent la superposition de (R,S) et (S,R) : elles désignent la même forme méso. Il y a donc trois stéréoisomères. (R,R)/(S,S) forment une paire d’énantiomères ; chacun est diastéréoisomère du méso. La forme méso possède des centres stéréogènes mais sa symétrie rend l’image miroir superposable : centres stéréogènes et chiralité globale ne sont pas synonymes. Dans une chaîne dissymétrique à deux centres sans symétrie ni autre contrainte, 2²=4 isomères peuvent subsister, en deux paires miroir. Une projection doit être accompagnée d’une vraie opération de rotation/symétrie, car permuter arbitrairement un seul couple de groupes inverserait un centre et ne serait pas une rotation globale.

### 35. Anti et gauche : ne pas oublier deux minima

*Sup → PC* — laboratoire `conformeres`.

**Énoncé.** Pour un modèle discret du butane, Ganti=0 et deux états gauche ont chacun ΔG=3,8 kJ·mol⁻¹. Calculer Panti et Pgauche total à 298 K. Refaire la limite T très élevée dans ce modèle. Pourquoi un modèle intégrant toute la courbe de torsion peut-il donner une autre population ?

**Corrigé.** À 298 K, RT=2,478 kJ·mol⁻¹ et w=exp(−3,8/RT)≈0,216. Z=1+2w≈1,432, donc Panti=1/Z≈69,9 % et Pgauche,total=2w/Z≈30,1 %, chaque gauche valant environ 15,1 %. Oublier le facteur 2 surestimerait anti. Dans la limite T→∞ de ces seuls trois états, les poids deviennent égaux : anti→1/3 et gauche total→2/3. Une intégration d’exp\[−V(θ)/RT\] sur l’angle compte la largeur de chaque puits, les zones entre minima et les corrections que ΔG peut déjà inclure ; elle n’est pas identique à trois états ponctuels. À haute température, le modèle discret peut aussi perdre sa pertinence. La dégénérescence et la nature énergie/énergie libre doivent donc être déclarées avant la moyenne statistique.

### 36. Le basculement d’une chaise conserve la face

*Sup → PC* — laboratoire `conformeres`.

**Énoncé.** Un méthylcyclohexane a ΔGax−eq=7,5 kJ·mol⁻¹ à 298 K dans le modèle. Calculer le rapport axial/équatorial et la population équatoriale. Lors du basculement, CH₃ axial haut devient-il équatorial haut ou bas ? Expliquer la différence entre conformation et configuration cis/trans pour un cyclohexane disubstitué.

**Corrigé.** ax/eq=exp(−7,5/2,478)≈0,0485 ; Peq=1/(1+0,0485)≈95,4 %. Ce rapport compare deux chaises de dégénérescence égale dans le modèle, et non deux chemins de réaction. Lors du basculement, un CH₃ axial haut devient équatorial haut : axial/équatorial change, haut/bas demeure. Pour un cycle disubstitué, deux groupes sur la même face restent cis après basculement, deux faces opposées restent trans ; les arrangements axiaux et équatoriaux associés dépendent des positions 1,2/1,3/1,4. Une barrière de basculement gouverne la vitesse de changement mais ne doit pas être ajoutée aux ΔG des minima pour calculer la population d’équilibre. Ce distinguo sert ensuite aux E2 trans-diaxiales.

### 37. Isotope et ressort : un nombre d’onde prédit

*Sup option PC* — laboratoire `ir`.

**Énoncé.** Une bande OH est à 3400 cm⁻¹. Avec mO=16u, mH=1u et mD=2u, estimer la bande OD en gardant la même constante de force. Déterminer la fréquence de OH avec c=3,00×10¹⁰ cm·s⁻¹ et dire pourquoi l’intensité d’une bande ne se déduit pas de la seule masse réduite.

**Corrigé.** μOH=16/17u≈0,941u ; μOD=32/18u≈1,778u. Le rapport est ṽOD/ṽOH=√(μOH/μOD)≈0,728, d’où ṽOD≈2474 cm⁻¹. La fréquence OH vaut ν=cṽ=3,00×10¹⁰×3400=1,02×10¹⁴ s⁻¹. La constante de force est supposée identique ; liaisons hydrogène et couplages de modes peuvent modifier cette estimation. L’activité et l’intensité IR dépendent de la variation du moment dipolaire avec la coordonnée normale, pas seulement de μ et k. Une liaison qui vibre n’absorbe pas nécessairement de façon intense en IR. L’unité de c doit correspondre au cm⁻¹ pour éviter un facteur 100 ; employer c en m·s⁻¹ impose de convertir le nombre d’onde en m⁻¹.

### 38. Additionner les absorbances, pas les transmittances

*Sup option PC* — laboratoire `ir`.

**Énoncé.** Deux espèces indépendantes donnent à un nombre d’onde des absorbances A₁=0,20 et A₂=0,35, à la même longueur de trajet. Déterminer la transmittance du mélange, puis son évolution si les deux concentrations doublent. Comment une réduction cétone→alcool pourrait-elle être suivie sans conclure uniquement d’une bande OH ?

**Corrigé.** L’absorbance totale vaut A=0,20+0,35=0,55, donc T=10^(−0,55)≈0,282, soit 28,2 %. Après doublement des concentrations, A=1,10 et T≈0,0794, soit 7,94 %. Ce sont les absorbances qui s’additionnent ; additionner deux pourcentages de transmittance n’a pas de sens pour les transmissions successives équivalentes. Pour suivre une réduction, observer la décroissance d’une bande C=O identifiée et l’apparition de signatures d’alcool, avec un étalonnage si l’on veut une quantité. Une bande OH peut aussi provenir d’eau ou d’un alcool solvant ; la RMN et un contrôle de pureté complètent la conclusion. Dans le TP, les gaussiennes sont calculées et ne sont pas vendues comme des spectres mesurés de référence.

### 39. Éthanoate ou propanoate ?

*Sup option PC* — laboratoire `rmn`.

**Énoncé.** Une espèce C₄H₈O₂ donne un singulet 3H à 2,05 ppm, un triplet 3H à 1,25 ppm et un quartet 2H à 4,12 ppm, les deux derniers avec J=7,2 Hz. Proposer la structure. Combien d’environnements ¹³C attend-on ? À 400 MHz, quel espacement en ppm sépare les raies du quartet ?

**Corrigé.** Triplet 3H et quartet 2H avec même J forment un groupe CH₂CH₃. Le CH₂ à 4,12 ppm est lié à O ; le singulet CH₃ vers 2,05 ppm est un méthyle acyle sans H voisin couplant à travers le carbonyle dans ce modèle. La structure est CH₃COOCH₂CH₃, éthanoate d’éthyle. Ses quatre C sont distincts : C=O, CH₃ acyle, OCH₂ et CH₃ terminal donnent quatre environnements ¹³C découplés. L’espacement d’un quartet est J/ν₀=7,2/400=0,018 ppm ; le groupe entier span trois espacements, 0,054 ppm, dans le premier ordre. Le propanoate de méthyle aurait un OCH₃ singulet vers 3,7 ppm et son CH₂ à côté de C=O vers 2,3 ppm : ses intégrales 3/2/3 seules ne suffisent pas à le distinguer.

### 40. Quantifier un mélange par deux singulets

*Sup option PC → PC* — laboratoire `rmn`.

**Énoncé.** Un mélange contient propanone et acide éthanoïque. Le singulet de propanone (6H) intègre 18 unités et le CH₃ acide (3H) 12 unités. Déterminer les fractions molaires si l’acquisition est quantitative. Puis considérer deux protons à Δδ=0,05 ppm et J=8 Hz : comparer Δν/J à 60 et 600 MHz.

**Corrigé.** Les quantités sont proportionnelles aux intégrales divisées par les H responsables : npropanone∝18/6=3 et nacide∝12/3=4. Les fractions molaires valent donc 3/7≈42,9 % et 4/7≈57,1 %, pas 60/40 issus des intégrales brutes. L’acquisition doit permettre relaxation et réponse adaptées ; une superposition de pics empêcherait cette lecture. À 60 MHz, Δν=0,05×60=3 Hz et Δν/J=0,375 ; à 600 MHz, Δν=30 Hz et le rapport vaut 3,75. Le champ plus élevé améliore la séparation en Hz mais ce dernier rapport n’est encore pas « très grand » : la règle n+1 du premier ordre peut demeurer insuffisante. Une simulation de raies de premier ordre doit donc annoncer ce diagnostic plutôt que prétendre résoudre un système fortement couplé.

### 41. Choisir un éluant qui sépare réellement

*Sup TP* — laboratoire `ccm`.

**Énoncé.** Trois éluants donnent respectivement RfA/RfB : 0,05/0,10 ; 0,35/0,60 ; 0,85/0,90. Choisir pour séparer, sachant un front à 60 mm et des taches de largeur 4 mm. Calculer Δd pour chacun. Pourquoi deux taches à même Rf ne prouvent-elles pas une identité moléculaire ?

**Corrigé.** Les écarts Δd=ΔRf×60 mm valent 3 mm, 15 mm et 3 mm. Le deuxième éluant sépare nettement deux taches de largeur 4 mm, avec des Rf ni au dépôt ni au front ; les deux autres peuvent superposer les taches malgré une migration globale différente. Le choix doit aussi garder une révélation efficace et une charge de dépôt raisonnable. Une même valeur de Rf est une propriété du couple molécule/éluant/plaque et peut être partagée par des structures différentes. Une co-tache référence+inconnu et un autre éluant apportent des tests utiles, mais IR/RMN ou une autre caractérisation restent nécessaires. L’intensité ne donne pas directement la pureté sans réponse révélatrice et étalonnage ; une tache de produit unique peut cacher plusieurs composés coéluants.

### 42. Suivre une réaction par prélèvements raisonnés

*Sup TP* — laboratoire `ccm`.

**Énoncé.** Pendant une synthèse, une tache de réactif baisse et une tache de produit apparaît. Proposer une comparaison par CCM qui permet de discuter la fin de réaction. Un échantillon continue de réagir après prélèvement : quel biais s’introduit ? Peut-on calculer un rendement isolé à partir d’une disparition visuelle ?

**Corrigé.** Déposer sur une même plaque une référence du réactif, une du produit si disponible, plusieurs prélèvements à des temps connus et éventuellement une co-tache. Choisir un éluant séparateur et une charge comparable. Si l’aliquote réagit encore, son temps de mesure n’est plus son temps de prélèvement : il faut prévoir une trempe, dilution ou condition d’arrêt adaptée, puis vérifier que cette opération ne crée pas elle-même de produit. La disparition visuelle signifie au mieux que le réactif descend sous le seuil de détection de cette révélation ; elle ne prouve pas conversion exactement 100 %. Le rendement isolé y=nproduit,pur/nthéorique demande récupération, masse ou quantité, identité et pureté. Une CCM forme un outil de suivi et de choix d’opération, à compléter par un bilan quantitatif indépendant.

### 43. Un volume total, une ou deux extractions

*Sup TP* — laboratoire `extraction`.

**Énoncé.** Une substance a D=5 entre phase organique et aqueuse. Vaq=100 mL et le volume total de solvant neuf est 100 mL. Comparer une extraction et deux extractions de 50 mL. Démontrer le bilan d’une extraction puis indiquer les hypothèses qui empêchent une optimisation aveugle avec un nombre arbitrairement grand de contacts.

**Corrigé.** À l’équilibre Corg=DCaq et n₀=CaqVaq+DCaqVorg. La fraction aqueuse est q=Vaq/(Vaq+DVorg). Un contact de 100 mL laisse 100/(100+500)=1/6=16,67 % ; deux de 50 mL laissent \[100/(100+250)\]²=(2/7)²=8,16 %. Les récupérations sont donc 83,33 % et 91,84 %. Les deux contacts utilisent du solvant neuf et atteignent l’équilibre à volumes constants. Des volumes très petits rendent pertes de transfert, solubilité mutuelle, émulsions, temps de séparation et saturation non négligeables ; le modèle idéal ne fournit pas seul le meilleur protocole réel. On doit aussi vérifier que le produit n’est ni dégradé ni ionisé différemment entre contacts et que D demeure constant.

### 44. Séparer un acide par un pH maintenu

*Sup TP → PC* — laboratoire `extraction`.

**Énoncé.** Un acide HA a pKa=4,5 en eau et P=10 pour sa forme neutre. Le milieu aqueux est tamponné à pH=6,5, puis dans une autre étape à pH=2,5. Calculer D aux deux pH et la fraction extraite avec volumes égaux. Une substance neutre de P=10 accompagne-t-elle la même variation ?

**Corrigé.** D=P/\[1+10^(pH−pKa)\]. À pH=6,5, D=10/101≈0,0990 et la fraction organique pour volumes égaux est D/(1+D)≈9,01 %. À pH=2,5, D=10/1,01≈9,901 et la fraction vaut ≈90,83 %. Le changement de pH permet de garder HA ionisé en phase aqueuse, puis de le régénérer sous forme neutre extractible. Une substance neutre de P=10 conserve, dans le modèle, une fraction organique 10/11=90,91 % à ces deux pH ; cette différence permet une séparation. Les calculs supposent seulement HA neutre en organique, équilibre atteint et pH effectivement maintenu. Sans tampon assez capable, le transfert de protons et les quantités d’acide changent le pH et imposent un bilan couplé.

### 45. Déplacer l’équilibre sans changer sa constante

*Sup* — laboratoire `esterification`.

**Énoncé.** Un modèle homogène idéal d’estérification possède K=4, avec aucune eau ni ester initiaux. Calculer la conversion pour 1 mol d’acide+1 mol d’alcool, puis 1 mol d’acide+5 mol d’alcool. Une catalyse acide change-t-elle K ? Que devient le calcul si l’eau est un solvant en très grand excès ?

**Corrigé.** Avec stocks 1/1, K=x²/(1−x)²=4, donc x=2/3 mol, soit 66,67 % de l’acide. Avec stocks 1/5, K=x²/\[(1−x)(5−x)\]=4 : 3x²−24x+20=0. La racine physique est x=(24−√336)/6≈0,94495 mol ; l’autre dépasse le stock limitant. L’excès d’alcool élève la conversion à 94,49 % dans ce modèle sans changer K à T fixée. Le catalyseur accélère aller et retour et ne modifie pas l’équilibre. Si l’eau est solvant en excès, son activité est souvent prise proche de 1 et les activités des solutés suivent un autre choix de standard : on ne réutilise pas aveuglément x² comme produit ester/eau du mélange initial anhydre.

### 46. Saponifier puis acidifier : deux étapes de bilan

*Sup → PC* — laboratoire `esterification`.

**Énoncé.** On fait réagir 12 mmol d’un ester avec 10 mmol de HO⁻ dans un modèle de saponification complète de l’équivalent limitant. Déterminer ester restant, carboxylate et alcool formés. Combien de H⁺ faut-il au minimum pour convertir le carboxylate en acide, en négligeant les autres bases présentes ?

**Corrigé.** Le bilan RCOOR′+HO⁻→RCOO⁻+R′OH consomme les réactifs 1:1. HO⁻ est limitant ; l’avancement est 10 mmol. Restent 2 mmol d’ester, se forment 10 mmol de carboxylate et 10 mmol d’alcool. La conversion de l’ester vaut 10/12=83,33 % dans ce modèle. Acidifier le carboxylate demande RCOO⁻+H⁺→RCOOH, au moins 10 mmol de H⁺, puis un milieu suffisamment acide pour favoriser la forme neutre selon son pKa. Dans une manipulation réelle, un excès de HO⁻ ou d’autres bases consommerait aussi l’acide. Le produit de la saponification est un sel carboxylate ; le nommer directement acide carboxylique sans le traitement final manquerait une étape de séparation souvent essentielle.

### 47. L’amine peut aussi être la base

*PC* — laboratoire `acylation`.

**Énoncé.** Une banque décrit RCOCl+2R′NH₂→RCONHR′+R′NH₃⁺Cl⁻. On mélange 10 mmol de chlorure d’acyle et 14 mmol d’amine sans autre base. Calculer la quantité théorique dans ce modèle. Refaire avec 10 mmol d’amine et au moins 10 mmol d’une base externe adaptée. Identifier la fonction de chaque équivalent.

**Corrigé.** Sans base externe, une molécule d’amine forme la liaison amide et une autre capte le proton équivalent à HCl. La borne est min(10,14/2)=7 mmol d’amide ; l’amine limite le bilan 1:2. Avec une base externe adaptée, l’amine peut être consacrée à l’acylation : 10 mmol d’amine et 10 mmol d’acyle permettent 10 mmol d’amide, tandis que la base piège 10 mmol de protons. Ce modèle n’affirme pas que chaque expérience sans base s’arrête précisément à 7 mmol : solubilité, transferts et acidité peuvent compliquer la distribution. Il expose pourquoi le rôle nucléophile et le rôle base sont distincts et pourquoi il faut comptabiliser les deux. Le mécanisme passe par attaque de l’amine, intermédiaire tétraédrique, départ de Cl⁻ puis déprotonation.

### 48. Une N-acylation emblématique : le paracétamol

*PC* — laboratoire `acylation`.

**Énoncé.** À partir de p-aminophénol, on utilise une banque d’acylation sélective conduisant au paracétamol. Nommer la fonction créée et celle conservée. Proposer des données de caractérisation prouvant la cible plutôt qu’un produit O-acétylé. Le p-aminophénol et le paracétamol ont masses molaires 109,13 et 151,16 g·mol⁻¹ : quelle masse théorique vient de 2,00 g de réactif limitant ?

**Corrigé.** N-acétyler le NH₂ forme une amide −NHCOCH₃ tandis que le OH phénolique est conservé. Un produit O-acétylé posséderait un ester et une amine libre : la connectivité diffère malgré une acétylation au même nombre d’atomes ajouté. Il faut comparer IR (amide, NH et OH), RMN (CH₃ acyle, environnements aromatiques, protons échangeables avec prudence), et éventuellement une référence de point de fusion/pureté ; une masse ou une CCM seules ne suffisent pas. Le stock est 2,00/109,13=18,33 mmol ; la masse théorique 1:1 vaut 0,01833×151,16≈2,77 g. La chimiosélectivité est une propriété des conditions fournies et doit être observée ; elle n’est pas décrétée simplement parce qu’une molécule porte deux nucléophiles.

### 49. Protéger n’est utile que si la suite est compatible

*Sup option PC* — laboratoire `protection`.

**Énoncé.** Une route exige de conserver un carbonyle pendant une étape organomagnésienne sur un autre site. La banque permet sa conversion sélective en acétal, stable dans l’étape suivante. Or le mélange de protection contient eau et acide. Proposer l’ordre des opérations et identifier ce qui arriverait si RMgX était ajouté immédiatement à ce milieu.

**Corrigé.** La séquence est protéger le carbonyle choisi par acétalisation sous conditions adaptées, isoler ou préparer un milieu débarrassé d’eau et d’acide, réaliser l’étape organomagnésienne en milieu anhydre, effectuer son traitement terminal puis hydrolyser l’acétal en milieu aqueux acide compatible avec le produit. RMgX ajouté au mélange de protection réagit avec H labiles et eau : RMgX+HA→RH+sels, avant la création C−C visée. Une protection correctement dessinée ne suffit donc pas : les conditions résiduelles comptent. Il faut aussi vérifier que les deux carbonyles de départ peuvent être discriminés et que la déprotection n’altère pas le nouveau produit. Cette route dépend d’une banque déclarant la sélectivité de protection ; on ne peut la supposer pour toute molécule à plusieurs carbonyles.

### 50. Le coût de trois opérations supplémentaires

*Sup option PC → PC* — laboratoire `protection`.

**Énoncé.** Une voie protégée comporte des rendements isolés 90 %, 85 % et 95 %. Une autre voie directement compatible donne 80 %. Comparer les rendements globaux et le produit obtenu depuis 10 mmol de cible théorique. Peut-on décider uniquement par ces nombres si la voie directe a un problème de sélectivité non mesuré ?

**Corrigé.** La voie protégée donne y=0,90×0,85×0,95=0,72675, soit 72,68 % ; depuis 10 mmol théoriques on isole 7,2675 mmol. La voie directe à 80 % donne 8,0 mmol, donc davantage si les deux rendements concernent bien le même produit pur et des périmètres comparables. Les pertes se multiplient, elles ne se moyennent pas. Cependant un « 80 % » de mélange non caractérisé n’est pas comparable à 72,68 % de cible pure : la sélectivité et la purification peuvent modifier le bilan. La décision doit intégrer compatibilité, identité, pureté, coût, nombre d’isolements et consommation de solvants. Une protection ajoute des déchets, mais évite parfois une réaction destructrice incontournable ; une optimisation suppose une alternative concrètement valide.

### 51. Construire la chalcone en suivant les atomes

*PC* — laboratoire `aldol`.

**Énoncé.** Nommer donneur et accepteur pour former la chalcone PhCOCH=CHPh depuis acétophénone et benzaldéhyde. Dessiner le β-hydroxycarbonyle puis l’eau éliminée. Pourquoi l’absence d’Hα du benzaldéhyde simplifie-t-elle la réaction croisée ? Calculer la masse théorique depuis 10 mmol de chaque partenaire avec Mchalcone=208,26 g·mol⁻¹.

**Corrigé.** L’acétophénone PhCOCH₃ possède des Hα et fournit l’énolate carboné ; le benzaldéhyde PhCHO sans Hα est l’accepteur électrophile. L’attaque forme PhCOCH₂CH(O⁻)Ph puis PhCOCH₂CH(OH)Ph après protonation, β-hydroxycétone. La déshydratation enlève un Hα et le OHβ dans le bilan net d’une eau pour produire PhCOCH=CHPh. Le benzaldéhyde ne forme pas un énolate par déprotonation α, ce qui réduit les possibilités d’auto-aldolisation et de croisements, sans supprimer toute réaction parasite. Le bilan cible est 1:1 ; 10 mmol permettent au plus 0,010×208,26=2,0826 g de chalcone. Il faut encore mesurer rendement, configuration et pureté ; le produit E souvent favorisé n’est pas un pourcentage imposé par la formule seule.

### 52. Pourquoi deux carbonyles énolisables compliquent une aldol

*PC* — laboratoire `aldol`.

**Énoncé.** Mélanger sans sélection deux aldéhydes A et B tous deux énolisables. Énumérer les couples donneur/accepteur possibles sans détailler leurs régioisomères. Proposer deux stratégies réduisant cette multiplicité, puis expliquer pourquoi une déshydratation ne doit pas être incluse automatiquement dans toute aldolisation.

**Corrigé.** Les couples sont A/A, B/B, A/B et B/A, donc deux auto- et deux croisements distincts avant même de considérer plusieurs sites α et la stéréochimie. Un énolate préformé de A, puis l’addition contrôlée de B, peut rendre A donneur privilégié si la banque de conditions le permet. Choisir un accepteur non énolisable, par exemple benzaldéhyde, supprime aussi une source d’énolate ; un autre levier est la dilution ou une réaction intramoléculaire adaptée. Le produit initial est un β-hydroxycarbonyle ; la crotonisation demande des conditions de déshydratation et peut être réversible ou concurrencée. Le bilan aldolisation n’élimine pas d’eau alors que le bilan condensation complète en élimine une. Identifier l’étape observée est nécessaire pour lire une masse molaire et un spectre corrects.

### 53. Addition 1,2 ou 1,4 : des cibles différentes

*PC* — laboratoire `michaelwittig`.

**Énoncé.** Un accepteur est CH₃COCH=CH₂. Comparer les connectivités finales après addition protonée d’un Nu carboné en 1,2 et en 1,4. Où reste le carbonyle ? Quel type de donneur énolate pourrait favoriser une addition de Michael dans une banque adaptée ? Proposer une caractérisation discriminante.

**Corrigé.** En 1,2, Nu attaque le C du carbonyle : le produit après protonation est CH₃C(OH)(Nu)CH=CH₂, un alcool allylique, avec C=C conservée et C=O transformée. En 1,4, Nu se fixe sur le Cβ terminal ; les déplacements π donnent un énolate puis la protonation/tautomérie conduit à CH₃COCH₂CH₂Nu, carbonyle conservé et C=C saturée. Un énolate stabilisé, comme celui d’un β-dicarbonyle, est un donneur fréquent de Michael dans les conditions appropriées ; « énolate » ne garantit cependant pas universellement 1,4. En IR/RMN, le premier produit perd C=O et garde les protons vinyliques, tandis que le second garde C=O et perd les signatures de l’alcène de l’accepteur. La nouvelle liaison doit être localisée avant d’invoquer une règle dur/mou.

### 54. Wittig : choisir le carbone introduit

*PC* — laboratoire `michaelwittig`.

**Énoncé.** Proposer un ylure transformant benzaldéhyde en styrène puis en PhCH=CHCH₃. Écrire les produits secondaires du bilan de Wittig. Pour le second alcène, quelles configurations sont possibles et pourquoi une tendance Z d’un ylure non stabilisé n’est-elle pas une composition chiffrée universelle ?

**Corrigé.** PhCHO+Ph₃P=CH₂→PhCH=CH₂+Ph₃P=O construit le styrène ; le carbone terminal porte deux H, donc aucune configuration E/Z. Pour PhCH=CHCH₃, employer l’ylure Ph₃P=CHCH₃ : le carbone de l’ylure porte H et CH₃, celui de l’aldéhyde H et Ph, permettant E et Z. L’oxygène du carbonyle devient celui de Ph₃P=O ; le nombre de C introduit se lit directement sur l’ylure. Un ylure non stabilisé présente souvent une préférence Z dans certains protocoles, mais formation de l’ylure, contre-ions, sels, solvant et température modifient les voies. La banque doit préciser des conditions et, si un ratio est nécessaire, fournir une sélectivité mesurée ou un modèle déclaré. Une règle qualitative ne vaut pas un rendement ni un rapport exact.

### 55. Les six centres d’une Diels–Alder

*PC* — laboratoire `dielsalder`.

**Énoncé.** Numéroter C1–C4 d’un diène et C5–C6 d’un diénophile. Donner les nouvelles liaisons et la liaison π restante après \[4+2\], puis discuter un diène bloqué s-trans et le devenir de deux substituants cis sur C5/C6. Que faut-il ajouter pour discuter endo/exo d’un adduit bicyclique ?

**Corrigé.** Une orientation choisie forme C1−C6 et C4−C5, transforme les anciennes liaisons π terminales et laisse C2=C3 ; la seconde orientation échange C5/C6 si les partenaires sont dissymétriques. Le cycle C1−C2−C3−C4−C5−C6 compte six centres, deux nouvelles liaisons σ et une π résiduelle. Un diène bloqué s-trans ne rapproche pas les extrémités dans la géométrie concertée ordinaire : un bon écart HO/BV ne supprime pas cette contrainte. Des substituants cis du diénophile gardent leur relation cis, par conservation de sa stéréochimie. Endo/exo compare ensuite leur orientation vis-à-vis du pont de l’adduit bicyclique, distincte de cis/trans ; il faut dessiner le pont et les groupes π attracteurs avant de discuter une préférence cinétique.

### 56. Endo cinétique ne veut pas dire exo impossible

*PC* — laboratoire `dielsalder`.

**Énoncé.** Un modèle irréversible à 298 K donne une barrière endo plus basse de 3 kJ·mol⁻¹ que l’exo, avec mêmes préfacteurs. Déterminer le rapport et les fractions. Dans un autre modèle réversible, exo est plus stable de 2 kJ·mol⁻¹ : déterminer la composition d’équilibre et les conditions sous lesquelles elle remplace la première.

**Corrigé.** En cinétique, kendo/kexo=exp(3/2,478)≈3,36, donc fendo≈3,36/4,36=77,1 % et fexo≈22,9 %. À l’équilibre du deuxième modèle, Gexo−Gendo=−2 kJ·mol⁻¹, donc exo/endo=exp(2/2,478)≈2,24 : fexo≈69,2 % et fendo≈30,8 %. Les deux compositions répondent à deux situations différentes ; on ne les moyenne pas. L’équilibre exige une réversibilité accessible, une interconversion via un réseau commun et assez de temps à température contrôlée. Un adduit endo peut rester piégé si la rétro-Diels–Alder est trop lente. Ces nombres sont des conséquences d’énergies déclarées, non des valeurs universelles de cyclopentadiène/anhydride maléique dans n’importe quel solvant.

### 57. Aspirine : masse humide et pureté

*Sup TP → PC* — laboratoire `retrosynthese`.

**Énoncé.** Une synthèse 1:1 utilise 5,00 g d’acide salicylique, M=138,12 g·mol⁻¹, agent acylant en excès. Elle isole 4,80 g d’un solide à 95 % massique d’aspirine, M=180,16 g·mol⁻¹. Calculer rendement apparent et rendement en produit pur. Proposer une cause de surestimation de masse et une preuve de la fonction acétylée.

**Corrigé.** nlim=5,00/138,12=0,03620 mol ; mth=0,03620×180,16=6,522 g. Le rendement apparent sur masse brute est 4,80/6,522≈73,6 %. La masse de produit pur est 0,95×4,80=4,56 g, d’où ypur≈69,9 %. Eau ou solvant résiduel, réactif coprécipité et sels peuvent augmenter la masse sans augmenter l’aspirine. La cible est une O-acétylation du OH phénolique de l’acide salicylique, conservant le carboxylique ; IR/RMN, comparaison à une référence et contrôle de pureté doivent confirmer cette connectivité. L’excès d’agent acylant ne rend pas automatiquement la conversion et la récupération complètes : le rendement mesure la chaîne de réaction, isolation et purification.

### 58. Économie d’atomes et PMI racontent deux choses

*PC* — laboratoire `retrosynthese`.

**Énoncé.** Le bilan conceptuel aspirinique salicylique+anhydride éthanoïque→aspirine+acide éthanoïque utilise masses molaires 138,12,102,09,180,16 et60,05. Calculer l’économie d’atomes. Une opération consomme au total 240 g d’entrées pour 4,56 g de produit pur ; calculer PMI et E-factor pour un bilan complet au même périmètre. Comparer ces indicateurs.

**Corrigé.** L’équation équilibrée conserve 138,12+102,09=180,16+60,05=240,21 g pour une mole de cible. L’économie d’atomes vaut 180,16/240,21≈75,0 %. Elle repose sur l’équation, pas sur la récupération réelle ni les litres de solvants. PMI=240/4,56≈52,63 g/g. Si toutes les autres entrées deviennent déchets et que le bilan est complet, E-factor=(240−4,56)/4,56=51,63=PMI−1. Il faut annoncer si eau et solvants recyclés sont inclus ; changer le périmètre modifie ces nombres. Une réaction à 75 % d’économie d’atomes peut donc avoir un PMI élevé. Réduire volume de solvant, pertes de purification et excès de réactif constitue une autre optimisation que choisir une équation plus atomique.

### 59. Carothers : une stœchiométrie presque égale

*PC* — laboratoire `polymeres`.

**Énoncé.** Utiliser Xn=(1+r)/(1+r−2rp), r≤1, pour une polymérisation par étapes bifonctionnelle. Comparer r=1,p=0,99 puis r=0,98,p=0,99. Donner la limite p→1 pour r=0,98 et expliquer quelle pureté est concernée par ce calcul.

**Corrigé.** Pour r=1, Xn=2/(2−2p)=1/(1−p)=100 à p=0,99. Pour r=0,98, Xn=1,98/(1,98−2×0,98×0,99)=1,98/0,0396=50. À conversion complète, la limite vaut (1+r)/(1−r)=1,98/0,02=99. Une différence de seulement 2 % entre stocks de fonctions plafonne donc la longueur même si les fonctions limitantes réagissent presque toutes. Le ratio r concerne les quantités de groupes fonctionnels réactifs, pas simplement les masses de deux monomères ni leur pureté analytique totale. Une impureté monofonctionnelle peut arrêter des chaînes et nécessite un autre bilan. Le modèle suppose égalité de réactivité, absence de cyclisation et bifonctionnalité ; un réseau ramifié ne suit pas cette expression linéaire.

### 60. Une distribution n’est pas une chaîne unique

*PC — prolongement statistique* — laboratoire `polymeres`.

**Énoncé.** On fournit la distribution en nombre xn=(1−p)p^(n−1), n≥1, d’un modèle idéal équilibré à p=0,80. Vérifier sa normalisation, donner Xn=1/(1−p) et la dispersité Đ=1+p, puis estimer Xw. Quelle fraction en nombre possède au moins 10 unités ? Une forte moyenne garantit-elle des chaînes toutes longues ?

**Corrigé.** La série géométrique donne Σxn=(1−p)/(1−p)=1. Xn=1/(1−0,80)=5 ; Đ=1+0,80=1,80, donc Xw=ĐXn=9 si masses de motifs identiques et effets d’extrémité négligés. La fraction en nombre n≥10 est Σn≥10(1−p)p^(n−1)=p⁹=0,80⁹≈13,42 %. Les moyennes pondèrent différemment les chaînes : Xw accorde davantage de poids aux longues. Une distribution large peut contenir beaucoup de petites molécules même avec une moyenne importante, donc un matériau ne se décrit pas par « une chaîne de longueur Xn ». Ces formules résultent d’une polymérisation par étapes idéale équilibrée, pas de toute croissance radicalaire ni d’un mélange cyclisé ou ramifié.

## Sources primaires et programmes

- [MESRI — programmes PCSI, arrêté de 2021](https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm)
- [MESRI — annexe PCSI, chimie : structures, réactions, caractérisation et stratégie](https://cache.media.education.gouv.fr/file/SPE1-MEN-MESRI-4-2-2021/65/0/spe780_annexe_1373650.pdf)
- [MESRI — programmes PC et PC*, arrêté de 2021](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111703A.htm)
- [MESRI — annexe 3 PC : programme de chimie](https://cache.media.education.gouv.fr/file/31/23/0/ensecsup703_annexes_1417230.pdf)
- [IUPAC Gold Book — nucléophilie et distinction avec la basicité](https://goldbook.iupac.org/terms/view/N04251)
- [IUPAC — synthèse stéréosélective, terminologie](https://old.goldbook.iupac.org/html/S/S05990.html)
- [IUPAC — glossaire de chimie organique physique](https://iupac.org/wp-content/uploads/2021/05/PAC-REC-18-10-10.R6_PR20210507.pdf)
- [MIT — Organic Chemistry I : structure, substitution, élimination, carbonyles](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2003/)
- [MIT — Lewis, charges formelles et mésomérie](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2003/a962254320d5add4b31a77925dddfce9_01.pdf)
- [MIT — Organic Chemistry II : stéréochimie, mécanismes et synthèse](https://ocw.mit.edu/courses/5-13-organic-chemistry-ii-fall-2003/)
- [MIT — spectroscopies, systèmes conjugués et transformations](https://ocw.mit.edu/courses/5-13-organic-chemistry-ii-fall-2003/pages/lecture-notes/)
- [MIT — identification combinant formule, IR, masse et RMN](https://ocw.mit.edu/courses/5-13-organic-chemistry-ii-fall-2003/c6fe40cdadfb1733da5045528cf44e9f_unit1_study_gd.pdf)
- [MIT — techniques de laboratoire et caractérisation](https://ocw.mit.edu/courses/5-310-laboratory-chemistry-fall-2019/)
- [NIST — éthanoate d’éthyle, spectre IR gazeux et conditions de mesure](https://webbook.nist.gov/cgi/cbook.cgi?ID=C141786&Index=26&Type=IR-SPEC&Units=CAL)
- [NIH PubChem — identité et données de l’éthanoate d’éthyle](https://pubchem.ncbi.nlm.nih.gov/compound/Ethyl-Acetate)
- [IUPAC — excès énantiomérique](https://old.goldbook.iupac.org/html/E/E02070.html)
- [NIST — compositions isotopiques du chlore](https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ascii=ascii2&ele=Cl&isotype=some)
- [MIT — mécanismes de substitution et d’élimination](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/864a502e7a69a6b5b737b8322ae23ac4_subelim.pdf)
- [MIT — dérivés d’acide, organomagnésiens et réductions](https://ocw.mit.edu/courses/5-13-organic-chemistry-ii-fall-2003/ca016d97ac06ccf746484dc89c790340_outline_sg_v.pdf)
- [IUPAC — théorie de l’état de transition](https://goldbook.iupac.org/terms/view/T06470)
- [IUPAC — aromaticité](https://goldbook.iupac.org/terms/view/A00441)
- [MIT — laboratoire de cycloaddition Diels–Alder](https://ocw.mit.edu/courses/5-37-introduction-to-organic-synthesis-laboratory-spring-2009/resources/mit5_37s09_lec01_mod7/)
