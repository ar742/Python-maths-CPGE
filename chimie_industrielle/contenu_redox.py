"""Objectifs et exercices : électrochimie et usages industriels."""
import html
GUIDES={}; LESSONS=[]; EXERCISES=[]
def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=list(map(html.unescape,objects)),hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=list(map(html.unescape,first_steps)),expected=expected)
def lesson(id_,title,level,body): LESSONS.append(dict(lab=id_,title=title,level=level,html=body))
def exercise(id_,title,level,question,answer): EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('nernst_pile','Associer tension, sens spontané, énergie de réaction et quantité d’électricité dans une pile.',
 ['E est la tension réversible de la pile, en V ; E° sa valeur standard. F=96485 C·mol⁻¹ est la constante de Faraday.',
  'aCu²⁺ et aZn²⁺ sont les activités sans dimension, assimilées à c/c°, c°=1 mol·L⁻¹. Q=aZn²⁺/aCu²⁺.',
  'T est en K ; nCu est la quantité de cuivre déposée, en mol. q est la charge passée, en C. Le bilan échange 2 mol d’électrons par mol de cuivre.'],
 ['Solides purs et solutions idéales, sans pertes.','La tension instantanée n’est pas supposée constante pendant une décharge réelle.'],
 ['Équilibrer des demi-équations','Nernst','ΔrG=−nFE','Faraday'],
 'Sup : réaction redox et fonctionnement d’une pile.',
 'Spé : thermochimie électrochimique et énergie réversible.',
 'Piles réelles : activités, polarisation et capacité à établir avec les quantités initiales.',
 ['Avec activités égales, retrouver E=E°.','Diviser aCu²⁺ par 100 et vérifier la diminution de tension.','Pour nCu=0,1 mol, calculer q sans utiliser la tension.'],
 'La tension dépend du quotient réactionnel ; la charge dépend de la stœchiométrie électronique et de la quantité transformée.')
lesson('nernst_pile','Assembler les demi-équations dans le bon sens','Sup — redox',
 '<p>Dans la pile Daniell en fonctionnement spontané, le zinc s’oxyde à l’anode : Zn→Zn²⁺+2e⁻. Le cuivre(II) se réduit à la cathode : Cu²⁺+2e⁻→Cu. Les électrons parcourent le circuit extérieur du zinc vers le cuivre.</p>'
 '<div class="formula">Zn+Cu²⁺→Zn²⁺+Cu ; E°=0,340−(−0,763)=1,103 V.</div><p>Les potentiels de couples sont toujours écrits dans le sens réduction. Une anode est définie par l’oxydation ; son signe dépend du fonctionnement en pile ou en électrolyse.</p>')
lesson('nernst_pile','Nernst et énergie libre donnent le même équilibre','Sup / spé — équilibre',
 '<p>Pour la réaction écrite, Q=aZn²⁺/aCu²⁺ et E=E°−RT ln Q/(2F). L’enthalpie libre de réaction est ΔrG=−2FE. À l’équilibre, E=0 et Q=K°.</p>'
 '<div class="formula">ln K°=2FE°/(RT) ; q=2FnCu.</div><p>Une quantité donnée de cuivre fournit une charge donnée. L’énergie électrique totale d’une décharge est une intégrale ∫E dq si E varie ; multiplier une tension initiale par toute la charge n’est généralement pas exact.</p>')
exercise('nernst_pile','Charge d’un dépôt de cuivre','Sup','<p>Combien de coulombs correspondent à 0,1 mol de Cu²⁺ réduit en Cu ?</p>', '<p>Chaque mole consomme deux moles d’électrons. q=2×96485,332×0,1≈19297 C, soit environ 5,361 Ah. Le potentiel n’intervient pas dans ce bilan de charge.</p>')
exercise('nernst_pile','Pente de Nernst','Sup / spé','<p>À 298,15 K, Q est multiplié par 100. Déterminer la variation de E pour un échange de deux électrons.</p>', '<p>ΔE=−RT ln100/(2F)≈−0,05916 V. Le quotient est sans dimension ; la transformation devient moins favorable dans le sens écrit.</p>')
exercise('nernst_pile','Constante d’équilibre très grande','Spé','<p>Pour E°=1,103 V et n=2 à 298,15 K, évaluer log₁₀ K°.</p>', '<p>log₁₀K°=2FE°/(RT ln10)≈37,29. Une constante grande signifie un équilibre très déplacé vers les produits pour les états et la réaction choisis ; elle ne donne pas la vitesse de transfert de charge.</p>')

guide('electrolyse_h2','Distinguer production faradique, énergie électrique et échange de chaleur dans un électrolyseur.',
 ['I est le courant en A ; Δt la durée convertie en s ; U la tension d’une cellule en V.',
  'ηF est la fraction de charge utilisée pour produire H₂. nH₂=ηF IΔt/(2F) et MH₂=2,016 g·mol⁻¹.',
  'Erev=ΔG°/(2F) et Etn=ΔH°/(2F) sont les tensions réversible et thermoneutre. Qévacuée est positive si le système cède de la chaleur.'],
 ['Une cellule à 298 K, eau liquide et gaz standard.','Auxiliaires, compression et consommation d’électricité en amont exclus.'],
 ['Demi-équations','Faraday','Puissance UI','Bilan thermique et périmètre d’un rendement'],
 'Sup : électrolyse et conversions de charge.',
 'Spé : distinction ΔH/ΔG et tensions énergétiques.',
 'Électrolyse haute température et pilotage par électricité variable.',
 ['À ηF=1, vérifier deux fois moins de O₂ que de H₂.','Fixer I et Δt, augmenter U : la quantité ne change pas, l’énergie oui.','À U bas, lire le signe de la chaleur nette et expliquer l’importation de chaleur.'],
 'Faraday donne la quantité ; la tension fixe l’électricité par mole. ΔG et ΔH correspondent à deux contraintes énergétiques différentes.')
lesson('electrolyse_h2','Une réaction, deux électrons, deux gaz','Sup — bilan redox',
 '<p>En milieu acide, la cathode suit 2H⁺+2e⁻→H₂ ; l’anode suit H₂O→½O₂+2H⁺+2e⁻. Leur somme est H₂O(l)→H₂(g)+½O₂(g). Deux moles d’électrons produisent une mole de H₂.</p>'
 '<div class="formula">nH₂=ηF IΔt/(2F) ; nO₂=nH₂/2.</div><p>La durée se convertit en secondes pour obtenir des coulombs. Une production exprimée en kg utilise la masse molaire en kg·mol⁻¹. Le rendement faradique compte la fraction de courant utile ; il ne mesure pas toutes les pertes énergétiques.</p>')
lesson('electrolyse_h2','Tension réversible et tension thermoneutre','Spé — thermochimie électrochimique',
 '<p>À 298 K, ΔG°≈237,13 et ΔH°≈285,83 kJ·mol⁻¹ pour la décomposition de l’eau liquide. Erev≈1,229 V est la limite du travail électrique réversible ; Etn≈1,481 V correspond à l’enthalpie par charge.</p>'
 '<div class="formula">Qévacuée=UIΔt−nH₂ΔH°.</div><p>À U entre ces deux tensions et à bon rendement faradique, une partie de l’enthalpie doit être fournie comme chaleur. Le <a href="https://www.energy.gov/cmei/fuels/articles/doe-releases-assessment-electrolysis-technology-highlighting-pathways-cut-cost" target="_blank" rel="noopener">rapport DOE sur l’électrolyse</a> décrit les axes actuels de recherche : efficacité, coûts et systèmes intégrés.</p>')
exercise('electrolyse_h2','Production en une heure','Sup','<p>Calculer nH₂ pour I=100 A, Δt=1 h et ηF=1.</p>', '<p>q=100×3600=360000 C ; nH₂=q/(2F)≈1,866 mol. La masse vaut environ 3,761 g et nO₂≈0,933 mol. Il s’agit d’une cellule, pas d’une pile de cellules en série.</p>')
exercise('electrolyse_h2','Tension et consommation spécifique','Sup / spé','<p>Si U est multipliée par 1,2 à I, Δt et ηF constants, comment évoluent production et kWh par kg ?</p>', '<p>La production faradique est inchangée. L’énergie électrique UIΔt et la consommation par kg sont multipliées par 1,2. La chaleur dissipée augmente aussi dans ce modèle.</p>')
exercise('electrolyse_h2','Un rendement électrique supérieur à un','Spé','<p>Avec ηF=1 et U=1,35 V, le quotient ηPCS=Etn/U est supérieur à 1. Contredit-il le premier principe ?</p>', '<p>Non : Etn/U≈1,097 et le système reçoit de la chaleur. Le dénominateur ne compte que l’électricité, tandis que l’énergie du H₂ inclut cette chaleur importée. Un rendement total doit compter toutes les entrées.</p>')

guide('pile_combustible','Comparer la tension utile, la puissance et le rendement d’une pile à combustible.',
 ['j est le courant par surface en A·cm⁻² ; j₀ est un courant d’échange effectif et jlim une limite de transport dans les mêmes unités.',
  'r est la résistance surfacique en Ω·cm². b=0,060 V est le coefficient d’activation global du modèle.',
  'U est la tension en V ; jU est la puissance par surface en W·cm⁻². ηPCS=U/Etn rapporte l’électricité à l’enthalpie du H₂ consommé.'],
 ['Courbe globale illustrative à 298 K, rendement faradique 1.','Les points de tension non positive ne sont pas des points de production électrique en pile.'],
 ['Lire une polarisation','Additionner les pertes','Maximiser une puissance','Distinguer puissance et rendement'],
 'Sup : redox et puissance électrique.',
 'Spé : polarisation, courant limite et bilan énergétique.',
 'Vieillissement, distribution d’eau et pilotage de piles de cellules.',
 ['À faible j, comparer les pertes d’activation et ohmiques.','Diminuer r, puis augmenter j₀ : identifier la perte modifiée.','Comparer le point de puissance maximale au point de meilleur rendement.'],
 'Le point de puissance maximale impose une tension plus basse ; l’efficacité électrique ne croît pas avec la puissance délivrée.')
lesson('pile_combustible','Trois mécanismes font baisser la tension','Spé — polarisation',
 '<p>La pile consomme H₂+½O₂ et forme H₂O(l). La tension est diminuée par l’activation des réactions aux électrodes, la résistance et le transport des espèces. Le modèle global écrit :</p>'
 '<div class="formula">U=Erev−b asinh[j/(2j₀)]−rj+(RT/2F)ln(1−j/jlim).</div><p>Le logarithme est évalué seulement pour j&lt;jlim. Le coefficient b représente les deux électrodes de manière globale : il n’est pas une identification de leurs paramètres microscopiques. La <a href="https://www.energy.gov/eere/fuelcells/articles/fuel-cell-101" target="_blank" rel="noopener">présentation DOE Fuel Cell 101</a> donne le contexte technologique.</p>')
lesson('pile_combustible','Puissance maximale et rendement : deux critères','Sup / spé — optimisation',
 '<p>La puissance surfacique est p=jU(j). Si U décroît avec j, la puissance peut d’abord augmenter puis diminuer. Un extremum intérieur satisfait U+jU′=0.</p>'
 '<div class="formula">ηPCS=U/Etn ; Etn=ΔH°/(2F).</div><p>Au courant nul, la tension est maximale mais la puissance est nulle. Le TP cherche le plus grand jU sur une grille ; sa valeur est une approximation numérique du maximum. Il ne compte ni compresseur ni autres auxiliaires.</p>')
exercise('pile_combustible','Un point de fonctionnement','Sup','<p>Une pile fournit U=0,70 V à j=0,80 A·cm⁻². Calculer la puissance surfacique et le rendement PCS si Etn=1,481 V.</p>', '<p>p=0,80×0,70=0,56 W·cm⁻² ; ηPCS=0,70/1,481≈47,3 %. Le calcul suppose un rendement faradique de 1 et exclut les auxiliaires.</p>')
exercise('pile_combustible','Une pile avec seulement une résistance','Spé','<p>Pour U=E−rj, déterminer le courant de puissance maximale et la tension correspondante.</p>', '<p>p=Ej−rj² ; p′=E−2rj. Le maximum est en j*=E/(2r), avec U*=E/2 et p*=E²/(4r). Le rendement électrique au maximum est inférieur au rendement limite à petit courant.</p>')
exercise('pile_combustible','Transport à la limite','Spé','<p>Que devient −ln(1−j/jlim) lorsque j approche jlim par valeurs inférieures ?</p>', '<p>La grandeur diverge vers +∞. Le modèle impose une forte perte de tension et ne peut être prolongé à j≥jlim. En production électrique, on s’arrête avant que la tension devienne non positive.</p>')

guide('batterie_intercalation','Relier état de charge, occupation des sites, tension et énergie pendant une décharge.',
 ['s est l’état de charge sans dimension, limité ici à 0,05≤s≤0,95. θ− et θ+ sont les fractions de sites occupés dans les deux électrodes.',
  'C est la capacité nominale en Ah, I le courant de décharge en A et r la résistance en Ω. Une variation ds correspond à C ds en Ah.',
  'Uoc est la tension à vide ; U=Uoc−rI sous décharge. W=C∫U(s)ds est l’énergie en Wh, jusqu’au seuil s=0,05.'],
 ['Deux électrodes de sites idéaux ; somme des occupations conservée.','Courbe illustrative sans données commerciales, hystérésis ni vieillissement.'],
 ['Potentiel chimique et Nernst','Conservation du lithium','Charge en Ah','Intégrale de tension pour l’énergie'],
 'Sup : charge, puissance et bilans matière.',
 'Spé : thermodynamique électrochimique et énergie d’un accumulateur.',
 'Modèles d’intercalation non idéale, plateaux de phases et vieillissement.',
 ['À I=0, comparer Uoc pour trois valeurs de s.','Fixer s et augmenter I ; contrôler la chute rI et la puissance Joule rI².','Calculer la charge disponible jusqu’à 5 %, puis expliquer pourquoi W n’est pas toujours CΔs Uinitial.'],
 'La charge compte les électrons transférables ; l’énergie dépend aussi de la tension tout au long de la décharge.')
lesson('batterie_intercalation','Sites occupés et potentiel chimique','Spé — modèle de solution idéale',
 '<p>Une électrode d’intercalation possède des sites occupés par Li et des sites vacants. Dans le modèle idéal, le potentiel chimique molaire est µLi=µ°+RT ln[θ/(1−θ)], où θ est la fraction occupée.</p>'
 '<p>Le TP choisit θ−=0,05+0,90s et θ+=1−θ−. La différence des potentiels chimiques donne la tension à vide Uoc=3,4+(RT/F){ln[θ−/(1−θ−)]−ln[θ+/(1−θ+)]}. La valeur 3,4 V sert de référence illustrative ; les fractions restent loin de 0 et 1.</p>')
lesson('batterie_intercalation','Intégrer une décharge et compter Joule','Sup / spé — énergie',
 '<p>Sous courant de décharge I constant, le modèle donne U=Uoc−rI. La charge associée à un intervalle d’état de charge est q=CΔs en Ah. La puissance Joule est rI² ; elle augmente comme le carré du courant.</p>'
 '<div class="formula">W=C∫ₛfin^ₛdébut U(s)ds, en Wh.</div><p>Le seuil retenu est 5 % ; aucune énergie disponible sous ce seuil n’est revendiquée. Les électrodes réelles peuvent présenter des plateaux de phases, une dépendance de la résistance à s et des limites de courant absentes ici.</p>')
exercise('batterie_intercalation','La charge restante','Sup','<p>Avec C=10 Ah et s=0,65, calculer la charge disponible jusqu’au seuil s=0,05.</p>', '<p>q=10(0,65−0,05)=6 Ah, soit 21600 C. Ce résultat ne donne pas encore l’énergie en Wh : il faut connaître la tension.</p>')
exercise('batterie_intercalation','Une chute ohmique','Sup','<p>Calculer la chute de tension et la chaleur Joule pour I=8 A et r=0,05 Ω.</p>', '<p>rI=0,40 V ; rI²=3,2 W. À courant doublé, la chute double mais la chaleur Joule quadruple.</p>')
exercise('batterie_intercalation','Pourquoi intégrer U ?','Spé','<p>Une décharge de 4 Ah suit U(q)=4,0−0,2q, q étant en Ah déjà délivrés. Calculer l’énergie et comparer à Uinitial×4 Ah.</p>', '<p>W=∫₀⁴(4−0,2q)dq=16−0,1×16=14,4 Wh. Le produit initial 4×4=16 Wh surestime le résultat car la tension diminue pendant la décharge.</p>')

guide('corrosion_protection','Déterminer un potentiel mixte et comprendre comment une anode sacrificielle protège le fer.',
 ['E est le potentiel commun des métaux connectés, en V. jFe et jZn sont positifs pour la dissolution, négatifs pour une réduction nette.',
  'jO₂<0 est le courant cathodique d’oxygène et jlim>0 sa valeur limite, en mA·cm⁻². a=SZn/SFe est le rapport de surfaces.',
  'Le courant total, ramené à la surface du fer, est jFe+a jZn+jO₂. Une somme nulle définit le potentiel mixte au circuit ouvert.'],
 ['Milieu aéré à pH 7 ; paramètres cinétiques didactiques.','Pas de passivation, de piqûres ou de résistance d’électrolyte.'],
 ['Nernst','Branches intensité-potentiel','Conservation du courant','Faraday pour une perte métallique'],
 'Sup : oxydation du fer et sens du courant.',
 'Spé : potentiel mixte, limitation de transport et protection.',
 'Corrosion localisée et dimensionnement de la durée de vie du revêtement.',
 ['Avec a=0, repérer jFe=−jO₂ au potentiel mixte.','Connecter du zinc et prévoir le déplacement de E avant le calcul.','Diminuer jlim : relier l’apport d’oxygène à la perte du fer.'],
 'Un potentiel standard ne donne pas seul une vitesse de corrosion ; les courants partiels et leurs surfaces déterminent le fonctionnement connecté.')
lesson('corrosion_protection','La corrosion est un fonctionnement électrochimique local','Sup / spé — redox',
 '<p>Le fer peut s’oxyder : Fe→Fe²⁺+2e⁻. Dans une eau aérée, la réduction de l’oxygène consomme ces électrons. Une même pièce peut porter des sites anodiques et cathodiques sans générateur externe.</p>'
 '<p>Le TP emploie Nernst pour les couples Fe²⁺/Fe et Zn²⁺/Zn. Les branches métalliques suivent une loi réversible en sinh ; la réduction d’O₂ combine activation et transport limité. La perte métallique nette correspond à la partie positive du courant du fer.</p>')
lesson('corrosion_protection','Écrire la somme des courants avec les surfaces','Spé — potentiel mixte',
 '<p>Pour des métaux connectés, E est commun. Les densités de courant doivent être multipliées par leurs surfaces avant d’être ajoutées. Ramenée à la surface du fer, la conservation donne :</p>'
 '<div class="formula">jFe(E)+a jZn(E)+jO₂(E)=0.</div><p>Le zinc peut porter l’oxydation à un potentiel où la dissolution du fer est fortement réduite. Une surface de zinc limitée ou un revêtement consommé change la protection. Le calcul instantané ne donne pas sa durée de vie.</p>')
exercise('corrosion_protection','Bilan de corrosion en eau aérée','Sup','<p>Assembler Fe→Fe²⁺+2e⁻ et O₂+4H⁺+4e⁻→2H₂O.</p>', '<p>Multiplier la demi-équation du fer par deux : 2Fe+O₂+4H⁺→2Fe²⁺+2H₂O. Le pH impose les activités ; en milieu neutre, une écriture avec OH⁻ et la formation d’hydroxydes peut être plus adaptée au bilan global.</p>')
exercise('corrosion_protection','Surface et conservation du courant','Spé','<p>Au potentiel mixte, jFe=0,001, jZn=0,020 et jO₂=−0,041 mA·cm⁻². Trouver a.</p>', '<p>0,001+0,020a−0,041=0 donne a=2. Les densités sont ramenées à la surface du fer après multiplication de la contribution zinc par a.</p>')
exercise('corrosion_protection','Charge et masse perdue','Sup / spé','<p>Un courant de dissolution de 1 mA circule pendant 24 h pour Fe→Fe²⁺. Calculer la masse de fer perdue.</p>', '<p>q=0,001×86400=86,4 C ; nFe=q/(2F)≈4,477×10⁻⁴ mol. Avec MFe=55,845 g·mol⁻¹, m≈0,0250 g. Ce bilan suppose que tout le courant anodique est associé à cette dissolution.</p>')

guide('electrodepot','Passer de la charge à l’épaisseur et identifier la limitation par transport devant une cathode.',
 ['I est en A ; Δt est donné en min puis converti en s. S est la surface en cm² ; ρCu=8,96 g·cm⁻³.',
  'c∞ est la concentration de Cu²⁺ loin de la surface ; δ est l’épaisseur de diffusion en µm. D=7×10⁻¹⁰ m²·s⁻¹ est le coefficient de diffusion.',
  'Ilim=2FDc∞S/δ après conversion SI ; Iutile=min(I,Ilim). e est l’épaisseur de dépôt en µm.'],
 ['Couche plane stationnaire et concentration extérieure maintenue.','Le dépôt est uniforme et les courants parasites sont seulement comptés comme charge non utile.'],
 ['Faraday','Fick stationnaire','Analyse des unités','Masse, volume et épaisseur'],
 'Sup : bilan d’électrolyse et géométrie du revêtement.',
 'Spé : courant limite et diffusion.',
 'Rugosité, dendrites et électrodépôt à impulsions.',
 ['À faible I, vérifier que doubler le temps double l’épaisseur.','Augmenter I jusqu’au plateau : contrôler Iutile.','Diminuer δ pour représenter l’agitation et retrouver le profil de concentration.'],
 'La charge utile gouverne l’épaisseur ; le courant total ne reste pas proportionnel au dépôt si le transport devient limitant.')
lesson('electrodepot','Faraday donne le volume déposé','Sup — électrolyse',
 '<p>Cu²⁺+2e⁻→Cu. La quantité déposée est n=IutileΔt/(2F), sa masse m=nM et son volume V=m/ρ. Pour un dépôt uniforme sur S, e=V/S.</p>'
 '<div class="formula">e=IutileΔt M/(2FρS).</div><p>Le TP emploie M en g·mol⁻¹, ρ en g·cm⁻³ et S en cm² pour obtenir e en cm, puis multiplie par 10⁴ pour obtenir des µm. Il est préférable de choisir un jeu d’unités cohérent avant le calcul.</p>')
lesson('electrodepot','Diffusion et courant limite','Spé — transport',
 '<p>Dans la couche de diffusion plane stationnaire, le flux molaire est J=D(c∞−csurface)/δ. La densité de courant est j=2FJ. La concentration de surface ne peut pas être négative.</p>'
 '<div class="formula">jlim=2FDc∞/δ ; c(x)=c∞[1−(Iutile/Ilim)(1−x/δ)].</div><p>À la limite, csurface=0. Diminuer δ par agitation augmente le courant limite. Le TP représente simplement Iutile=min(I,Ilim) ; il ne prédit pas les réactions parasites ou la forme microscopique du dépôt.</p>')
exercise('electrodepot','Épaisseur après trente minutes','Sup / spé','<p>Pour Iutile=1 A, Δt=30 min et S=100 cm², calculer l’épaisseur de cuivre.</p>', '<p>n=1800/(2F)≈0,009328 mol ; m≈0,5928 g. e=m/(8,96×100)≈0,0006616 cm, soit environ 6,616 µm.</p>')
exercise('electrodepot','Convertir pour Fick','Spé','<p>Convertir c=0,1 mol·L⁻¹, δ=100 µm et S=500 cm² en SI.</p>', '<p>c=100 mol·m⁻³, δ=10⁻⁴ m et S=0,05 m². Avec D=7×10⁻¹⁰ m²·s⁻¹, Ilim=2FDcS/δ≈6,754 A.</p>')
exercise('electrodepot','Dépasser la limite','Spé','<p>Le courant limite vaut 2 A. On impose 5 A pendant 1 h et le modèle donne Iutile=2 A. Calculer le rendement faradique du dépôt et la charge parasite.</p>', '<p>ηF=2/5=40 %. La charge parasite est (5−2)×3600=10800 C. Elle n’ajoute pas de cuivre selon le modèle ; il faut connaître les autres réactions pour en déduire les produits.</p>')

guide('cuivre_complexation','Relier une constante de complexation à un potentiel conditionnel et à la stabilité de Cu(I).',
 ['β₁ et β₂ sont les constantes des complexes Cu(I)+2NH₃ et Cu(II)+4NH₃. aNH₃ est l’activité du ligand libre.',
  'ctotal est la somme du cuivre libre et complexé pour un nombre d’oxydation donné. Le facteur L=1+βaNH₃^m relie ctotal et clibre.',
  'E1 et E2 sont les potentiels standard conditionnels Cu(I)/Cu et Cu(II)/Cu. Dans Frost, les points ont abscisse nombre d’oxydation et ordonnée nE°.'],
 ['Ligand libre maintenu ; solutions idéales à 298 K.','Pas de protonation de NH₃, autres complexes ou précipitation.'],
 ['Nernst','Bilan de complexation','Ajouter des énergies et non des potentiels','Frost et dismutation'],
 'Sup : état d’oxydation et réaction de complexation.',
 'Spé : couplage complexation-redox et potentiels conditionnels.',
 'Séparation hydrométallurgique et optimisation multi-équilibres.',
 ['Avec peu de NH₃, retrouver approximativement les potentiels libres.','Augmenter NH₃ : comparer les deux chutes de potentiel.','Placer Cu(I) par rapport à la corde Cu(0)–Cu(II), puis calculer ΔG de dismutation.'],
 'Une complexation stabilise une espèce dissoute et peut changer la stabilité relative des nombres d’oxydation ; il faut garder la pondération par les électrons.')
lesson('cuivre_complexation','Du cuivre total au potentiel conditionnel','Spé — équilibres couplés',
 '<p>Pour Cu(I), ctotal=clibre(1+β₁aNH₃²) ; pour Cu(II), ctotal=clibre(1+β₂aNH₃⁴). Ces expressions conservent l’espèce libre même à faible activité de ligand.</p>'
 '<div class="formula">E°cond=E°−(RT/nF)ln(1+βaNH₃^m).</div><p>Le TP donne E°Cu⁺/Cu=0,521 V et E°Cu²⁺/Cu=0,340 V, puis β₁=10^10,8 et β₂=10^11,8 par défaut. Le mot conditionnel indique que le ligand libre est fixé et que Nernst utilise la concentration totale de chaque état.</p>')
lesson('cuivre_complexation','Frost : la corde donne le signe de dismutation','Spé — bilan d’énergie',
 '<p>Les points de Frost sont Cu(0) : (0,0), Cu(I) : (1,E1), Cu(II) : (2,2E2). Le potentiel Cu(II)/Cu(I) vaut 2E2−E1 car les énergies de réaction, pondérées par F, s’ajoutent.</p>'
 '<div class="formula">2Cu(I)→Cu(0)+Cu(II) : ΔG°=2F(E2−E1).</div><p>Si E1 dépasse la corde d’ordonnée E2 au point d’abscisse 1, ΔG° est négatif et la dismutation standard est favorisée. Une composition réelle introduit aussi RT ln Q ; le diagramme ne remplace pas ce quotient.</p>')
exercise('cuivre_complexation','Un facteur de complexation','Spé','<p>Pour β=10⁸, m=2 et aNH₃=10⁻³, calculer L et la fraction libre.</p>', '<p>L=1+10⁸×10⁻⁶=101. La fraction libre est 1/L≈0,00990, soit environ 0,99 %. Remplacer L par βa^m serait une approximation ; elle n’est pas nécessaire ici.</p>')
exercise('cuivre_complexation','Pondérer un potentiel','Spé','<p>Avec E1=0,52 V et E2=0,34 V pour les réductions vers Cu(0), déterminer le potentiel Cu(II)/Cu(I).</p>', '<p>La réduction Cu(II)→Cu(0) échange deux électrons ; Cu(I)→Cu(0) en échange un. Donc −FE21=−2FE2+FE1 et E21=2E2−E1=0,16 V.</p>')
exercise('cuivre_complexation','Dismutation de Cu(I)','Spé','<p>Pour E1=0,52 et E2=0,34 V, donner le signe de ΔG° pour 2Cu(I)→Cu(0)+Cu(II).</p>', '<p>ΔG°=2F(0,34−0,52)=−0,36F≈−34,7 kJ·mol⁻¹ réaction. La dismutation standard est favorisée. Une complexation assez forte de Cu(I) peut abaisser E1 et inverser cette conclusion.</p>')

guide('dosage_potentiometrique','Résoudre un dosage par précipitation sans approximation divergente à l’équivalence.',
 ['r=V/Véquiv est le volume titrant réduit. c est la concentration initiale de Br⁻ et celle du titrant Ag⁺, en mol·L⁻¹.',
  'Ks=10^−pKs est le produit de solubilité en activités réduites ; les concentrations sont assimilées aux activités.',
  's est la quantité de AgBr solide par litre de mélange. E est le potentiel de l’électrode Ag⁺/Ag, avant soustraction éventuelle d’une référence.'],
 ['Précipitation à l’équilibre et solution idéale à 298 K.','Complexation, adsorption et potentiel de référence exclus.'],
 ['Bilan de dilution','Produit de solubilité','Quadratique stable','Nernst et équivalence'],
 'Sup : bilan de titrage et précipitation.',
 'Spé : courbe potentiométrique et équilibres simultanés.',
 'Contrôle de bains industriels et estimation des incertitudes de mesure.',
 ['Avant l’équivalence, identifier l’ion en excès.','À r=1, retrouver [Ag⁺]=[Br⁻]=√Ks.','Après l’équivalence, vérifier les deux bilans avec la quantité de solide.'],
 'La transition est rapide mais finie ; conserver simultanément Ks et les bilans évite une singularité artificielle à l’équivalence.')
lesson('dosage_potentiometrique','Conserver les ions avec la dilution','Sup / spé — titrage',
 '<p>Le titrant et la solution initiale ont la même concentration c ; le volume équivalent vaut donc le volume initial. Après ajout r=V/Véquiv, les concentrations totales par volume de mélange sont cAg=c r/(1+r) et cBr=c/(1+r).</p>'
 '<p>Si une quantité s de solide AgBr par litre est présente : [Ag⁺]+s=cAg et [Br⁻]+s=cBr. Leur différence vaut d=cAg−cBr. L’équilibre impose [Ag⁺][Br⁻]=Ks.</p>')
lesson('dosage_potentiometrique','Le saut n’est pas une divergence','Spé — résolution exacte',
 '<p>Lorsque le solide existe, la racine positive est [Ag⁺]=(d+√(d²+4Ks))/2. Pour d négatif, on emploie la forme conjuguée 2Ks/[√(d²+4Ks)−d] afin d’éviter une perte de précision.</p>'
 '<div class="formula">À r=1 : [Ag⁺]=[Br⁻]=√Ks ; E=E°+(RT/F)ln aAg⁺.</div><p>Avant formation du solide, les concentrations libres sont les totales. À r=0, aucune activité Ag⁺ n’est imposée et Nernst ne définit pas un potentiel Ag⁺/Ag : le point reste vide. La courbe reprend le dosage de la page 557 en gardant les deux équilibres.</p>')
exercise('dosage_potentiometrique','Concentrations à l’équivalence','Sup / spé','<p>Avec Ks=10⁻¹² et concentrations totales égales, calculer [Ag⁺] et [Br⁻] si le solide est présent.</p>', '<p>Le bilan de différence donne [Ag⁺]=[Br⁻]. Leur produit vaut Ks, donc les deux valent 10⁻⁶ mol·L⁻¹ dans l’approximation idéale.</p>')
exercise('dosage_potentiometrique','Potentiel au point équivalent','Spé','<p>Avec E°Ag⁺/Ag=0,800 V, pKs=12 et T=298,15 K, calculer E à l’équivalence.</p>', '<p>log₁₀ aAg⁺=−pKs/2=−6. E=0,800+0,059159×(−6)≈0,4450 V. La valeur est finie ; une expression simplifiée valable loin de l’équivalence ne doit pas être prolongée jusqu’à ce point.</p>')
exercise('dosage_potentiometrique','Contrôler un bilan avant l’équivalence','Sup / spé','<p>Avec c=0,1 mol·L⁻¹ et r=0,8, donner les totaux dilués et l’excès de bromure.</p>', '<p>cAg=0,1×0,8/1,8≈0,044444 et cBr=0,1/1,8≈0,055556 mol·L⁻¹. Leur différence vaut −0,011111. Si le solide existe, [Br⁻]−[Ag⁺]=0,011111 ; cette égalité reste exacte dans le modèle à Ks fini.</p>')
