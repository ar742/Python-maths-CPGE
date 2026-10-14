"""Objectifs, méthodes et exercices : thermochimie industrielle."""
import html
GUIDES={}; LESSONS=[]; EXERCISES=[]
def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=list(map(html.unescape,objects)),hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=list(map(html.unescape,first_steps)),expected=expected)
def lesson(id_,title,level,body): LESSONS.append(dict(lab=id_,title=title,level=level,html=body))
def exercise(id_,title,level,question,answer): EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('hess_combustion','Comparer une mole et un kilogramme de combustible, puis séparer condensation et récupération de chaleur.',
 ['νᵢ est le coefficient stœchiométrique : négatif pour un réactif, positif pour un produit. ΔfHᵢ° est l’enthalpie standard de formation, en kJ·mol⁻¹, à 298 K.',
  'M est la masse molaire du combustible, en g·mol⁻¹. PCI et PCS sont les chaleurs libérées par kilogramme, respectivement avec eau vapeur et eau liquide.',
  'f est la fraction d’eau condensée ; r est la fraction de chaleur récupérée. Ces nombres sont compris entre 0 et 1.'],
 ['Combustion complète, quantités stœchiométriques et états standard à 298 K.','Aucune énergie de production ou de transport du combustible.'],
 ['Équilibrer une combustion','Loi de Hess','Conversion mol / masse','Définir le périmètre d’un rendement'],
 'Sup : bilans de matière et premier principe, lecture des états physiques.',
 'Spé : thermochimie et énergie de réaction, bilan d’un procédé.',
 'Intégration thermique d’une usine et analyse de cycle de vie : seules leurs limites de périmètre sont introduites.',
 ['Sélectionner CH₄, f=0 et r=1 ; écrire la combustion.','Passer à f=1 et calculer l’énergie supplémentaire liée à deux moles d’eau.','Comparer H₂ et méthanol par mole, puis par kilogramme.'],
 'Une différence de pouvoir calorifique vient de la composition et de l’état de l’eau ; la récupération est une étape de procédé distincte.')
lesson('hess_combustion','Hess : assembler des formations pour calculer une combustion','Sup / spé — thermochimie',
 '<p>Une enthalpie de formation ΔfH° correspond à une mole d’espèce formée à partir des éléments dans leurs états standard. Pour chaque espèce, préciser la phase. Les éléments dans leur état de référence ont ΔfH°=0.</p>'
 '<div class="formula">ΔrH°=ΣᵢνᵢΔfHᵢ°.</div><p>Pour CH₄+2O₂→CO₂+2H₂O(g), le calcul donne −802,292 kJ par mole de CH₄ avec les données arrondies du TP. Le signe négatif désigne une réaction exothermique. Le cycle de Hess relie les mêmes états par deux chemins.</p>')
lesson('hess_combustion','Condensation et chaleur utile','Sup / spé — bilan énergétique',
 '<p>Le PCI conserve l’eau des produits à l’état vapeur ; le PCS la considère liquide. La différence est l’enthalpie de condensation de l’eau produite. Dans le TP, une mole d’eau apporte environ 44,004 kJ supplémentaires si elle condense à 298 K.</p>'
 '<div class="formula">qdisponible=PCI+f(PCS−PCI) ; qutile=r qdisponible.</div><p>Ces énergies sont en MJ·kg⁻¹. Un combustible peut ne produire aucun CO₂ dans sa réaction d’usage tout en ayant des émissions en amont. Le TP compte uniquement les produits de la combustion.</p>')
exercise('hess_combustion','Combustion du méthane','Sup','<p>Équilibrer la combustion complète d’une mole de méthane. Donner les quantités de CO₂ et d’eau produites.</p>', '<p>CH₄+2O₂→CO₂+2H₂O. Les bilans de C, H et O sont respectés. Une mole de CH₄ produit une mole de CO₂ et deux moles d’eau.</p>')
exercise('hess_combustion','Passer d’une mole à un kilogramme','Sup','<p>Avec M(CH₄)=16,043 g·mol⁻¹ et une chaleur de combustion de 802,292 kJ·mol⁻¹, calculer le PCI en MJ·kg⁻¹.</p>', '<p>Un kilogramme contient 1000/16,043 moles. Le PCI vaut 802,292/16,043≈50,010 MJ·kg⁻¹. Écrire explicitement les facteurs 1000 g/kg et 1000 kJ/MJ montre pourquoi ils se compensent.</p>')
exercise('hess_combustion','Récupération partielle','Spé','<p>Un combustible a PCI=50 et PCS=55 MJ·kg⁻¹. La moitié de son eau condense ; 80 % de la chaleur disponible est récupérée. Calculer la chaleur utile.</p>', '<p>La chaleur disponible vaut 50+0,5(55−50)=52,5 MJ·kg⁻¹. La chaleur utile vaut 0,8×52,5=42 MJ·kg⁻¹. Confondre la fraction condensée avec la récupération globale donnerait un autre bilan.</p>')

guide('temperature_adiabatique','Appliquer un bilan d’enthalpie à une réaction exothermique et prévoir l’effet d’une dilution.',
 ['ξ est l’avancement, en mol, de NO+½O₂→NO₂ ; il varie de 0 à 1 pour la charge initiale.',
  'Tᵢ est la température initiale, en K ; T est la température du mélange. nᵢ est la quantité d’inerte, en mol.',
  'Cp,total est la capacité thermique du mélange, en J·K⁻¹. f est la fraction de la chaleur réactionnelle cédée à l’extérieur.'],
 ['Pression constante, conversion imposée et Cp molaires constants.','Une température élevée ne prouve pas que NO₂ reste stable à cette température.'],
 ['Tableau d’avancement','Kirchhoff','Premier principe à pression constante','Contrôle de l’ordre de grandeur'],
 'Sup : calorimétrie et bilans de matière.',
 'Spé : température de réaction et enthalpie standard dépendant de T.',
 'Réacteur couplant équilibre, cinétique et transfert : les trois calculs seraient nécessaires à une prévision réelle.',
 ['Reprendre le preset du recueil : vérifier 400 K avec 93 % de chaleur cédée.','Mettre f=0 puis augmenter nᵢ sans changer les réactifs.','À ξ=0, vérifier T=Tᵢ ; à ξ=1, contrôler le bilan énergétique.'],
 'L’inerte absorbe de la chaleur sans changer l’avancement imposé ; le bilan énergétique conserve les signes et les capacités thermiques.')
lesson('temperature_adiabatique','Construire un chemin thermochimique','Sup / spé — premier principe',
 '<p>La réaction initiale contient 1 mol de NO et 0,5 mol de O₂. À l’avancement ξ, les quantités sont 1−ξ, (1−ξ)/2 et ξ pour NO, O₂ et NO₂. L’inerte reste inchangé.</p>'
 '<p>On peut faire réagir à Tᵢ, puis chauffer les produits jusqu’à T. Avec des Cp constants et une fraction de chaleur cédée f, le bilan à pression constante donne :</p>'
 '<div class="formula">Cp,total(ξ)(T−Tᵢ)=−(1−f)ξΔrH°(Tᵢ).</div>')
lesson('temperature_adiabatique','Kirchhoff et validité du modèle','Spé — thermochimie',
 '<p>Les données sont Cp(NO)=Cp(O₂)=29 et Cp(NO₂)=36 J·mol⁻¹·K⁻¹. Ainsi ΔrCp°=−7,5 J·mol⁻¹·K⁻¹ et ΔrH°(Tᵢ)=ΔrH°(298 K)+ΔrCp°(Tᵢ−298 K).</p>'
 '<p>Le TP calibre ΔrH°(298 K) à partir du bilan expérimental : une conversion totale, Tᵢ=298 K, T=400 K et f=0,93. Lorsque le modèle prédit des températures très élevées, la dépendance des Cp et la dissociation des produits doivent être réintroduites.</p>')
exercise('temperature_adiabatique','Calibrer une enthalpie','Sup / spé','<p>Une mole de NO₂ se forme ; Cp=36 J·mol⁻¹·K⁻¹. T passe de 298 à 400 K et 93 % de la chaleur réactionnelle est cédée. Déduire ΔrH°(298 K) du modèle.</p>', '<p>La fraction retenue est 0,07. Donc 36×102=−0,07ΔrH°, d’où ΔrH°=−52,457 kJ·mol⁻¹. Le calcul est un bilan calorimétrique avec les données imposées.</p>')
exercise('temperature_adiabatique','Doubler la capacité thermique','Sup','<p>À énergie libérée fixée, quel est l’effet d’une capacité thermique totale doublée sur la hausse de température ?</p>', '<p>ΔT=Qretenue/Cp,total. Doubler la capacité thermique divise ΔT par deux. La température absolue n’est pas divisée par deux : Tfinal=Tinitial+ΔT.</p>')
exercise('temperature_adiabatique','L’inerte suffit-il à prévoir un réacteur ?','Spé','<p>Le calcul adiabatique donne une température élevée. Peut-on en déduire que le produit NO₂ sera formé intégralement dans le réacteur réel ?</p>', '<p>Non. La conversion totale a été imposée. À haute température, l’équilibre peut favoriser la dissociation ; les Cp réels changent et les transferts déterminent la trajectoire. Il faut coupler bilan énergétique, équilibre et cinétique.</p>')

guide('haber_bosch','Séparer la conversion d’équilibre des contraintes de vitesse dans la synthèse de l’ammoniac.',
 ['ξ est l’avancement, en mol, de N₂+3H₂⇌2NH₃ ; la charge contient 1 mol N₂ et 3 mol H₂.',
  'T est la température en K ; P est la pression totale en bar ; nᵢ est l’inerte en mol. yⱼ=nⱼ/ntotal est la fraction molaire.',
  'aⱼ=yⱼP/p° est l’activité du gaz idéal, avec p°=1 bar. Q est le quotient réactionnel et K° la constante d’équilibre, tous deux sans dimension.'],
 ['Gaz parfaits et réaction unique ; approximation de ΔrCp° constant.','La carte est un équilibre sans durée de séjour ni catalyseur modélisé.'],
 ['Tableau d’avancement','Activités gazeuses','ΔrG et constante d’équilibre','Effet de T et P'],
 'Sup : stœchiométrie et quotient réactionnel.',
 'Spé : thermochimie, équilibre et déplacement par T/P.',
 'Fugacités, recyclage et optimisation d’une boucle industrielle : nécessaires pour une prévision sous forte pression.',
 ['À P=100 bar, augmenter T et prévoir le sens de variation de la conversion.','À T fixé, augmenter P puis justifier le rôle de Δνgaz=−2.','Ajouter de l’inerte à P totale fixée et contrôler les pressions partielles.'],
 'Basse température favorise ici l’équilibre mais peut ralentir la réaction ; le catalyseur améliore la vitesse sans modifier K°.')
lesson('haber_bosch','Le quotient réactionnel contient les pressions partielles','Sup / spé — équilibre',
 '<p>Les quantités d’équilibre valent 1−ξ, 3(1−ξ) et 2ξ. Le total, avec nᵢ moles d’inerte, est 4−2ξ+nᵢ. Une activité gazeuse idéale est aⱼ=(nⱼ/ntotal)P/p°.</p>'
 '<div class="formula">Q=aNH₃²/(aN₂aH₂³) ; à l’équilibre Q=K°.</div><p>Comme la réaction réduit le nombre de moles gazeuses de deux, augmenter P à composition fixée diminue Q et favorise le sens direct. Ajouter de l’inerte à P totale fixée diminue les pressions partielles ; ce n’est pas le même protocole qu’à volume fixé.</p>')
lesson('haber_bosch','De ΔrG° à une conversion','Spé — thermochimie',
 '<p>Les constantes de référence du modèle sont ΔrH°298=−92,22 kJ·mol⁻¹, ΔrS°298=−198,1 J·mol⁻¹·K⁻¹ et ΔrCp°=−45 J·mol⁻¹·K⁻¹. Intégrer les relations de Kirchhoff donne H(T) et S(T), puis G(T)=H(T)−TS(T).</p>'
 '<div class="formula">ln K°=−ΔrG°/(RT).</div><p>La dichotomie résout ln Q(ξ)=ln K°. Une forte conversion d’équilibre n’impose aucune vitesse. L’<a href="https://www.iea.org/reports/ammonia-technology-roadmap" target="_blank" rel="noopener">IEA</a> replace ce procédé dans les enjeux actuels de production d’engrais et d’énergie.</p>')
exercise('haber_bosch','Contrôler le bilan','Sup','<p>Pour ξ=0,4 et 1 mol d’inerte, donner les quantités finales et le nombre total de moles.</p>', '<p>N₂ : 0,6 ; H₂ : 1,8 ; NH₃ : 0,8 ; inerte : 1 mol. Le total vaut 4−0,8+1=4,2 mol. Les nombres d’atomes N et H sont conservés.</p>')
exercise('haber_bosch','Évaluer l’effet d’une compression','Spé','<p>À T et composition fixées, on double P. Par quel facteur Q est-il multiplié ?</p>', '<p>Chaque activité gazeuse double. Le numérateur contient deux puissances et le dénominateur quatre : Q est multiplié par 2^(2−4)=1/4. Si le système était à l’équilibre, Q devient inférieur à K° et la réaction avance.</p>')
exercise('haber_bosch','Catalyse et équilibre','Sup / spé','<p>Un catalyseur réduit la durée nécessaire pour obtenir une composition proche de l’équilibre. Modifie-t-il K° ?</p>', '<p>Non. K° dépend de ΔrG° et T pour les états choisis. Un catalyseur modifie les mécanismes et accélère les transformations directe et inverse ; il ne change pas la position de l’équilibre.</p>')

guide('methanol_co2','Relier la valorisation du CO₂ à un équilibre et à un bilan stationnaire de recyclage.',
 ['ξ est l’avancement de CO₂+3H₂⇌CH₃OH+H₂O. h est le rapport initial H₂/CO₂ ; T et P sont en K et bar.',
  'x est la fraction de CO₂ convertie par passage à l’équilibre. r est la fraction des réactifs non convertis recyclée après séparation des produits.',
  'Ffrais et Fcirculant sont des débits de CO₂ dans les mêmes unités ; X est la conversion globale du CO₂ frais.'],
 ['Équilibre d’une seule réaction, uniquement en phase gazeuse.','Recyclage avec séparation idéale et rapport H₂/CO₂ maintenu à l’entrée.'],
 ['Réactif limitant','Activités gazeuses','Bilan stationnaire','Série géométrique et purge'],
 'Sup : tableau d’avancement et conservation du carbone.',
 'Spé : équilibre thermochimique et bilan d’une boucle.',
 'Fugacités, réactions concurrentes et analyse du cycle de vie : hors du calcul proposé.',
 ['Avec h=3 et r=0, comparer pression et conversion par passage.','Augmenter h : calculer la nouvelle borne ξmax avant de lire la carte.','À x fixé, comparer r=0 et r=0,9 ; observer aussi le débit circulant.'],
 'Un recyclage peut augmenter la conversion globale tout en imposant plus de circulation ; convertir CO₂ ne suffit pas à conclure sur les émissions totales.')
lesson('methanol_co2','Un tableau d’avancement contraint le solveur','Sup / spé — stœchiométrie',
 '<p>Pour une mole initiale de CO₂ et h moles de H₂, les quantités finales sont 1−ξ, h−3ξ, ξ et ξ. La borne physique est ξmax=min(1,h/3). Le solveur reste strictement à l’intérieur pour évaluer les logarithmes.</p>'
 '<div class="formula">Q=aCH₃OH aH₂O/(aCO₂ aH₂³).</div><p>Le modèle utilise ΔH°298=−49,5 kJ·mol⁻¹, ΔS°298=−177 J·mol⁻¹·K⁻¹ et ΔCp°=−28 J·mol⁻¹·K⁻¹ arrondis. La réaction donnant CO et les équilibres liquide–vapeur sont exclus. Les <a href="https://webbook.nist.gov/cgi/cbook.cgi?Name=methanol&amp;cTC=on&amp;cTG=on" target="_blank" rel="noopener">données NIST du méthanol</a> permettent un approfondissement documentaire.</p>')
lesson('methanol_co2','Recyclage : écrire le bilan avant le rendement','Spé — procédé',
 '<p>Après un passage de conversion x, la fraction 1−x du CO₂ reste non convertie. On recycle la fraction r de ce reste et on purge l’autre partie. Les produits sont séparés avant le recyclage.</p>'
 '<div class="formula">Fcirculant=Ffrais+r(1−x)Fcirculant ; X=x/[1−r(1−x)].</div><p>Cette formule suppose que la conversion x reste la même à chaque passage, grâce au maintien du rapport d’alimentation. Elle donne le bilan du carbone. La circulation augmente aussi ; sa compression et sa séparation ont un coût énergétique absent du TP.</p>')
exercise('methanol_co2','Limiter par le dihydrogène','Sup','<p>On introduit 1 mol de CO₂ et 2 mol de H₂. Quelle est la borne stœchiométrique de conversion de CO₂ ?</p>', '<p>Il faut 3 mol de H₂ par mole de CO₂. Donc ξmax=2/3 mol, soit au plus 66,7 % du CO₂ initial. Une méthode numérique qui dépasserait cette borne donnerait une quantité négative de H₂.</p>')
exercise('methanol_co2','Une boucle de recyclage','Spé','<p>Un passage convertit x=0,25 et r=0,8 du réactif restant est recyclé. Calculer X et Fcirculant/Ffrais.</p>', '<p>1−r(1−x)=1−0,8×0,75=0,4. La circulation vaut 1/0,4=2,5 fois le débit frais ; X=0,25/0,4=0,625, soit 62,5 %. Les 37,5 % restants sortent dans la purge.</p>')
exercise('methanol_co2','Conversion et bilan climatique','Spé — interprétation','<p>Une forte conversion du CO₂ garantit-elle une réduction des émissions sur l’ensemble du procédé ?</p>', '<p>Il faut aussi connaître l’origine de H₂ et de l’électricité, la compression, la séparation, le CO₂ d’alimentation et l’usage final du méthanol. Le bilan de conversion du carbone est un bilan de matière ; une comparaison climatique exige un autre périmètre.</p>')

guide('ellingham_zinc','Utiliser les changements d’état et les quotients de réaction pour choisir un réducteur du zinc.',
 ['T est en K. ΔrG° est l’enthalpie libre standard d’une réaction normalisée à une mole de O₂ dans la scène principale.',
  'H°Zn et S°Zn changent par ΔHtransition et ΔHtransition/Ttransition à la fusion puis à la vaporisation.',
  'Q est le quotient des activités de la réaction de réduction ; le réglage log₁₀ Q modifie ΔrG de RT ln Q. Les courbes de réduction sont par mole de Zn.'],
 ['Oxydes et carbone purs, gaz parfaits et approximation d’Ellingham.','Les transitions du zinc sont celles sous pression de référence.'],
 ['Loi de Hess sur G','Comparer des réactions de même normalisation','Continuité aux transitions','Signe de ΔrG'],
 'Sup : équilibrer les réactions et reconnaître un changement d’état.',
 'Spé : Ellingham, thermochimie et choix d’un réducteur.',
 'Pyrométallurgie réelle : cinétique, évacuation et condensation des vapeurs.',
 ['À 600, 900 puis 1400 K, identifier l’état du zinc.','Soustraire deux formations normalisées et retrouver ZnO+C→Zn+CO.','Diminuer log Q : prévoir le déplacement du domaine favorable.'],
 'On compare des réactions équilibrées et des unités identiques ; un changement d’état modifie la pente sans rendre G discontinu.')
lesson('ellingham_zinc','Pourquoi les lignes changent de pente','Spé — diagramme d’Ellingham',
 '<p>Pour 2Zn+O₂→2ZnO, on utilise ΔrG°=ΔrH°−TΔrS°. Le TP reprend les données du zinc page 564 : fusion à 693 K, 6,7 kJ·mol⁻¹ ; vaporisation à 1180 K, 114,8 kJ·mol⁻¹.</p>'
 '<p>Lors d’une transition, le potentiel chimique est continu : ΔHtransition−TtransitionΔStransition=0. Ajouter les variations correspondantes à H° et S° du zinc donne donc des segments raccordés. Le zinc est réactif de la formation : ses contributions sont soustraites deux fois.</p>')
lesson('ellingham_zinc','Soustraire pour obtenir la réduction','Spé — méthode',
 '<p>Les formations 2Zn+O₂→2ZnO et 2C+O₂→2CO sont toutes deux normalisées à une mole de O₂. Leur différence, divisée par deux, donne ZnO+C→Zn+CO. Avec 2CO+O₂→2CO₂, on obtient ZnO+CO→Zn+CO₂.</p>'
 '<div class="formula">ΔrG=ΔrG°+RT ln Q.</div><p>Lorsque Zn est gazeux, son activité intervient dans Q ; lorsqu’il est une phase condensée pure, elle vaut 1. ΔrG&lt;0 favorise le sens écrit, sans préciser sa vitesse. Il faut éviter de comparer une courbe par mole de O₂ à une courbe par mole de métal.</p>')
exercise('ellingham_zinc','Raccorder à la fusion','Spé','<p>Calculer la variation d’entropie de fusion du zinc, avec ΔHfus=6,7 kJ·mol⁻¹ et Tf=693 K.</p>', '<p>ΔSfus=ΔHfus/Tf=6700/693≈9,668 J·mol⁻¹·K⁻¹. À Tf, ΔHfus−TfΔSfus=0 : le raccord de G est continu.</p>')
exercise('ellingham_zinc','Évacuer un produit gazeux','Spé','<p>À 1200 K, Q est divisé par 100. De combien ΔrG diminue-t-il ?</p>', '<p>La différence vaut RT ln(1/100)=−RT ln100≈−45,95 kJ·mol⁻¹ réaction avec R=8,314 J·mol⁻¹·K⁻¹. Évacuer les produits peut donc favoriser la réaction, si le protocole modifie effectivement Q de ce facteur.</p>')
exercise('ellingham_zinc','Choisir la normalisation','Sup / spé','<p>À quoi correspond (Gformation,CO−Gformation,ZnO)/2 lorsque les deux formations consomment chacune une mole de O₂ ?</p>', '<p>Inverser 2Zn+O₂→2ZnO et l’ajouter à 2C+O₂→2CO donne 2ZnO+2C→2Zn+2CO. Diviser par deux donne une mole de Zn produite. La grandeur est donc en énergie par mole de cette réduction.</p>')

guide('calcination_ciment','Relier la pression du CO₂ au seuil de calcination et séparer émissions de procédé et chaleur réactionnelle.',
 ['T est en K ; pCO₂ est la pression partielle en bar, réduite par p°=1 bar dans le logarithme.',
  'm est la masse de CaCO₃, en kg ; M=100,086 kg·kmol⁻¹. n=m/M est donc en kmol.',
  'c est la fraction du CO₂ capturée ; elle change la sortie rejetée mais pas la stœchiométrie du carbonate.'],
 ['CaCO₃ et CaO purs, réaction unique et ΔH°, ΔS° constants.','Le bilan de conversion complète est un objectif théorique, indépendamment du point choisi sur la carte.'],
 ['Activités des solides','ΔrG et équilibre','Bilan massique','Distinguer capture et formation'],
 'Sup : stœchiométrie et calorimétrie.',
 'Spé : équilibre hétérogène et thermochimie industrielle.',
 'Clinker, captage et électrification des fours : leurs bilans détaillés sont hors du modèle.',
 ['À pCO₂=1 bar, calculer le seuil ΔH°/ΔS°.','Baisser pCO₂ et prévoir le signe de RT ln Q.','Pour 1000 kg de carbonate, comparer CO₂ produit, capturé et résiduel.'],
 'Diminuer la pression de CO₂ favorise la calcination ; la capture change les émissions résiduelles mais conserve le carbone du bilan.')
lesson('calcination_ciment','Une réaction endothermique avec un gaz produit','Spé — équilibre hétérogène',
 '<p>CaCO₃(s)⇌CaO(s)+CO₂(g). Si les deux solides purs sont présents, leurs activités valent 1 et Q=pCO₂/p°. L’approximation du TP est ΔH°=178,3 kJ·mol⁻¹ et ΔS°=160,6 J·mol⁻¹·K⁻¹.</p>'
 '<div class="formula">ΔrG=ΔH°−TΔS°+RT ln(pCO₂/p°).</div><p>Le seuil du modèle est Téquilibre=ΔH°/[ΔS°−R ln(pCO₂/p°)]. Diminuer pCO₂ abaisse ce seuil. Un seuil thermodynamique n’est pas une température de four suffisante pour une cadence donnée.</p>')
lesson('calcination_ciment','Le CO₂ de réaction ne dépend pas du combustible','Sup / spé — bilan matière-énergie',
 '<p>Une mole de carbonate donne une mole de CO₂, même si le chauffage est électrique. Pour 1000 kg de CaCO₃, la conversion complète donne environ 439,7 kg de CO₂. L’énergie réactionnelle est nΔH° ; le chauffage des matières s’ajoute dans un procédé réel.</p>'
 '<p>La fraction capturée c donne mCO₂,capturé=c mCO₂ et mCO₂,rejeté=(1−c)mCO₂. Les enjeux actuels du secteur sont documentés par l’<a href="https://www.iea.org/energy-system/industry/cement" target="_blank" rel="noopener">IEA</a>. Ici, ni les autres réactions du clinker ni l’énergie du captage ne sont calculées.</p>')
exercise('calcination_ciment','Seuil sous un bar','Spé','<p>Calculer la température d’équilibre sous pCO₂=1 bar avec les données du TP.</p>', '<p>Le logarithme vaut zéro. Téquilibre=178300/160,6≈1110,2 K. Cette valeur concerne l’approximation à ΔH° et ΔS° constants.</p>')
exercise('calcination_ciment','Conserver la masse','Sup','<p>Vérifier le bilan d’une mole de CaCO₃ avec M(CaO)=56,076 et M(CO₂)=44,010 g·mol⁻¹.</p>', '<p>56,076+44,010=100,086 g·mol⁻¹, masse molaire du carbonate. La masse totale est conservée ; la matière est répartie entre solide et gaz.</p>')
exercise('calcination_ciment','Capture de 90 %','Sup / spé','<p>Pour 1000 kg de carbonate entièrement converti, on forme environ 439,72 kg de CO₂. En capturer 90 % change-t-il la chaleur réactionnelle ?</p>', '<p>Environ 395,75 kg sont capturés et 43,97 kg restent non capturés. La chaleur de la réaction de calcination est inchangée si la conversion est la même. La capture exige son propre bilan énergétique, absent ici.</p>')

guide('distillation_ideale','Lire les compositions coexistantes et calculer la proportion de vapeur à partir d’un bilan.',
 ['z est la fraction molaire globale de B ; xL est celle dans le liquide et yV celle dans la vapeur.',
  'p*A et p*B sont les pressions de vapeur des corps purs à la température fixée, en bar. α=p*B/p*A>1 mesure la volatilité relative.',
  'β est la fraction molaire de vapeur parmi les deux phases ; P est la pression totale.'],
 ['Liquide idéal, gaz parfaits et aucune réaction.','Constituants A et B didactiques, pas un mélange réel identifié.'],
 ['Raoult','Pressions partielles','Lecture d’un fuseau','Règle du levier'],
 'Sup : fractions molaires et bilans de matière.',
 'Spé : diagrammes binaires et distillation.',
 'Dimensionnement d’une colonne et azéotropes : prolongements après le modèle idéal.',
 ['Au preset deux phases, vérifier xL<z<yV.','Augmenter P : identifier la disparition de la vapeur.','Fixer z et augmenter α : comparer enrichissement et fraction vapeur.'],
 'La vapeur est enrichie en B, le plus volatil ; la règle du levier conserve la composition globale.')
lesson('distillation_ideale','Dériver les deux courbes sans les confondre','Spé — liquide–vapeur',
 '<p>Raoult donne pA=(1−xL)p*A et pB=xLp*B. À l’ébullition, P=pA+pB. Dans la vapeur idéale, yV=pB/P, d’où yV=αxL/[1+(α−1)xL].</p>'
 '<div class="formula">Pébullition=(1−xL)p*A+xLp*B ; 1/Prosée=(1−yV)/p*A+yV/p*B.</div><p>Les courbes n’emploient pas la même composition : xL pour l’ébullition et yV pour la rosée. Dans un diagramme isotherme P–composition, le liquide seul est au-dessus du fuseau et la vapeur seule en dessous.</p>')
lesson('distillation_ideale','La règle du levier est un bilan','Sup / spé — mélange',
 '<p>Pour une mole globale, le liquide contient 1−β mole et la vapeur β mole. Le bilan du constituant B est z=(1−β)xL+βyV.</p>'
 '<div class="formula">β=(z−xL)/(yV−xL).</div><p>Cette formule ne s’applique que si les deux phases existent. Elle donne β entre 0 et 1 lorsque xL≤z≤yV. En phase unique, la composition de la phase est z. Une température et une pression ne suffisent pas à déterminer la quantité de chaque phase sans la composition globale.</p>')
exercise('distillation_ideale','Enrichissement d’un étage','Spé','<p>Avec α=3 et xL=0,4, calculer yV.</p>', '<p>yV=3×0,4/[1+2×0,4]=2/3. La vapeur est plus riche en B que le liquide car B a la pression de vapeur la plus élevée.</p>')
exercise('distillation_ideale','Calculer une fraction de vapeur','Sup / spé','<p>Deux phases ont xL=0,25 et yV=0,75 ; z=0,4. Calculer β.</p>', '<p>β=(0,4−0,25)/(0,75−0,25)=0,3. Le bilan donne 0,7×0,25+0,3×0,75=0,4. Les phases contiennent 70 % et 30 % des moles globales.</p>')
exercise('distillation_ideale','L’absence d’azéotrope','Spé','<p>Montrer que yV=xL seulement pour un corps pur lorsque α>1 est constant.</p>', '<p>L’égalité donne αx=x[1+(α−1)x], soit (α−1)x(1−x)=0. Avec α>1, x=0 ou x=1. Ce modèle idéal ne possède pas d’azéotrope intérieur.</p>')

guide('alliage_solidification','Distinguer composition d’une phase et quantité de cette phase pendant la solidification.',
 ['z est la fraction molaire globale de B ; xL et xS sont ses fractions dans le liquide et le solide.',
  'T est en K ; Tf,i et ΔHfus,i sont température et enthalpie molaire de fusion de chaque corps pur.',
  'fS est la fraction molaire de solide. Le liquidus donne xL(T), le solidus xS(T) lorsque les phases coexistent.'],
 ['Solutions idéales dans les deux phases, miscibilité totale et pression fixée.','Ni eutectique ni composé défini : modèle distinct du diagramme Mg–Ni.'],
 ['Égalité des potentiels chimiques','Diagramme binaire','Règle du levier','Fraction molaire versus massique'],
 'Sup : bilan de composition et changements d’état.',
 'Spé : équilibres de phases et diagrammes d’alliages.',
 'Thermodynamique des solutions non idéales et solidification hors équilibre.',
 ['À z=0,5, refroidir de 1800 à 1300 K ; repérer les trois domaines.','Dans le fuseau, comparer xL, z et xS.','Vérifier z=(1−fS)xL+fSxS, puis comparer au Mg–Ni du recueil.'],
 'La composition des cristaux diffère de celle du liquide ; les proportions se calculent par un bilan, pas par la hauteur des courbes.')
lesson('alliage_solidification','Construire un fuseau de solidification','Spé — équilibre de phases',
 '<p>Dans une solution idéale, µi,phase=µi,pur,phase+RT ln xi,phase. À coexistence, µi,L=µi,S. Avec ΔGfus,i≈ΔHfus,i(1−T/Tf,i), on obtient :</p>'
 '<div class="formula">xi,L/xi,S=exp[−ΔHfus,i(1−T/Tf,i)/(RT)].</div><p>Les deux relations pour A et B, avec xA+xB=1 dans chaque phase, donnent les compositions du fuseau. Le TP utilise des paramètres proches de Cu–Ni, sans ajustement à des mesures réelles.</p>')
lesson('alliage_solidification','Lire le refroidissement d’un alliage','Sup / spé — bilan',
 '<p>Au-dessus du liquidus pour z fixé, tout l’alliage est liquide. Entre liquidus et solidus, les compositions xL et xS se lisent aux extrémités d’un segment horizontal à T fixé. Au-dessous du solidus, tout est solide.</p>'
 '<div class="formula">fS=(z−xL)/(xS−xL).</div><p>Le modèle ne présente pas de palier eutectique : une plage de coexistence remplace le changement d’état isotherme d’un corps pur. Les composés définis et eutectiques du Mg–Ni, page 568, demandent des domaines supplémentaires.</p>')
exercise('alliage_solidification','Calculer la proportion solide','Sup / spé','<p>À une température donnée, xL=0,30, xS=0,60 et z=0,45. Calculer fS.</p>', '<p>fS=(0,45−0,30)/(0,60−0,30)=0,50. Le liquide et le solide contiennent chacun la moitié des moles ; 0,5×0,30+0,5×0,60=0,45.</p>')
exercise('alliage_solidification','Point pur et fusion','Spé','<p>Pour un constituant pur, vérifier que l’égalité des potentiels donne T=Tf.</p>', '<p>Les fractions valent 1 dans les deux phases, donc le logarithme vaut 0. Il reste ΔHfus(1−T/Tf)=0 ; comme ΔHfus≠0, T=Tf.</p>')
exercise('alliage_solidification','Pourquoi ne pas copier Mg–Ni ?','Spé — lecture','<p>Un modèle à miscibilité totale peut-il reproduire un diagramme comportant Ni₂Mg et NiMg₂ solides ainsi que des eutectiques ?</p>', '<p>Non. Le modèle ne comporte que deux phases de solution, liquide et solide. Des composés définis exigent d’autres potentiels chimiques et domaines ; une coexistence eutectique doit être introduite explicitement. Le modèle sert à apprendre le bilan et la lecture du fuseau.</p>')
