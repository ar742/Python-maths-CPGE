"""Repères, leçons et exercices originaux pour les circuits et la conversion."""

GUIDES = {}
LESSONS = []
EXERCISES = []

def guide(id_,purpose,objects,hypotheses,techniques,sup,spe,beyond,first_steps,expected):
    GUIDES[id_]=dict(purpose=purpose,objects=objects,hypotheses=hypotheses,techniques=techniques,levels=dict(sup=sup,spe=spe,beyond=beyond),first_steps=first_steps,expected=expected)

def lesson(id_,title,level,html):
    LESSONS.append(dict(lab=id_,title=title,level=level,html=html))

def exercise(id_,title,level,question,answer):
    EXERCISES.append(dict(lab=id_,title=title,level=level,question=question,answer=answer))

guide('pont_wheatstone','Déterminer une résistance inconnue en annulant la tension d’un détecteur.',
    ['A et C sont les bornes d’alimentation; B et D sont les points milieux. Le potentiel de C est pris égal à zéro.', 'E=UAC est la tension d’alimentation (V). R₁ relie A à B, R₂ relie B à C, R₃ relie A à D, R₄ relie D à C (Ω).', 'Rm est la résistance d’entrée du voltmètre branché entre B et D (kΩ dans le réglage, Ω dans les formules). UBD=VB−VD est sa tension (V).', 'Rth est la résistance de Thévenin vue de B et D (Ω). La sensibilité dUBD/dR₄ se mesure en V/Ω.'],
    ['Résistors linéaires, alimentation idéale.', 'Le détecteur ne charge pas le pont à l’équilibre; hors équilibre, sa résistance est prise en compte.'],
    ['Diviseur de tension','Lois des nœuds et des mailles','Générateur de Thévenin','Dérivation et approximation linéaire'],
    'PTSI, physique : circuits résistifs, conventions de tension et mesure indirecte.',
    'PSI/PT : réinvestir les circuits et analyser l’influence d’un instrument; applications aux capteurs en SI.',
    'Ponts d’impédances, jauges de contrainte et mesure différentielle.',
    ['Choisir quatre résistances de 1 kΩ et vérifier UBD=0.', 'Augmenter R₄ de 10 % et prévoir le signe de UBD.', 'Réduire la résistance du voltmètre et comparer la tension au zéro du pont.'],
    'L’équilibre dépend d’un rapport de résistances; la charge du voltmètre modifie la sensibilité, pas le zéro.')
lesson('pont_wheatstone','Suivre les branches avant de poser une formule','Sup · PTSI',
    '<p>A et C alimentent le pont; B et D sont les points milieux. On prend VC=0 et VA=E, où E est la tension appliquée en volts. Les résistances R₁, R₂, R₃ et R₄, en ohms, suivent les connexions A–R₁–B–R₂–C et A–R₃–D–R₄–C.</p><p>Un voltmètre idéal donne VB=ER₂/(R₁+R₂) et VD=ER₄/(R₃+R₄). Sa lecture est UBD=VB−VD. Le pont est donc équilibré si <strong>R₂R₃=R₁R₄</strong>. Cette égalité doit être déduite des connexions, car permuter deux indices change sa forme.</p>')
lesson('pont_wheatstone','Un zéro robuste, une sensibilité modifiée','Spé · mesure',
    '<p>On appelle U₀ la tension du pont à vide, Rm la résistance du voltmètre et Rth la résistance du pont vue de B–D, toutes les résistances étant en ohms. Après extinction de la source idéale, Rth=R₁R₂/(R₁+R₂)+R₃R₄/(R₃+R₄).</p><p>Le voltmètre lit U=U₀Rm/(Rm+Rth). Cette charge atténue une petite tension, mais U=0 reste équivalent à U₀=0. À l’équilibre R₄=R₄*, une petite variation ΔR₄ produit, à vide, ΔU≈−ER₃ΔR₄/(R₃+R₄*)². L’approximation exige |ΔR₄| petit devant R₃+R₄*.</p>')
exercise('pont_wheatstone','Retrouver l’inconnue','Sup',
    'Les branches sont celles du schéma. R₁=2 kΩ, R₂=1 kΩ et R₃=6 kΩ. Quelle valeur de R₄ annule UBD ?',
    'R₂R₃=R₁R₄, donc R₄=3 kΩ. Les deux points milieux sont au potentiel E/3.')
exercise('pont_wheatstone','Prévoir un signe','Sup',
    'E=5 V et les quatre résistances valent 1 kΩ. On remplace R₄ par 1,1 kΩ. Quel est le signe et la valeur à vide de UBD ?',
    'VB=2,5 V et VD=5×1,1/2,1≈2,619 V. UBD≈−0,119 V : augmenter la résistance inférieure droite élève VD.')
exercise('pont_wheatstone','Une résistance de voltmètre finie','Spé',
    'Un pont présente une tension à vide U₀=100 mV et une résistance de Thévenin Rth=1 kΩ. Le voltmètre a Rm=9 kΩ. Que lit-il ? Un réglage à zéro est-il déplacé ?',
    'U=100×9/(9+1)=90 mV. Le zéro ne change pas, car le facteur de charge est strictement positif; la sensibilité diminue de 10 %.')

guide('ligne_transmission','Relier le profil de tension dans un câble à la charge et aux pertes.',
    ['x est la position dans le câble, de 0 à d; d est sa longueur (m).', 'f est la fréquence (MHz au réglage, Hz dans les formules); ω=2πf est la pulsation (rad/s). E est l’amplitude crête à l’entrée (V).', 'R, L, G et C sont les paramètres par mètre : résistance (Ω/m), inductance (H/m), conductance (S/m), capacité (F/m). Les réglages emploient mΩ/m, µH/m, µS/m et pF/m.', 'Zcharge est la résistance terminale (Ω). Z₀ est l’impédance caractéristique (Ω), γ=α+jβ la constante de propagation (m⁻¹). α est l’atténuation et β le nombre d’onde.', 'V(x) et I(x) sont des amplitudes complexes crêtes (V, A). Γ est le coefficient de réflexion sans unité; P(x) est la puissance active (W).'],
    ['Ligne uniforme, régime sinusoïdal établi et charge résistive.', 'La tension à l’entrée est imposée; le générateur n’est pas adapté automatiquement.'],
    ['Maille et nœud sur une portion dx','Exponentielles complexes','Conditions à la charge','Bilan de puissance par unité de longueur'],
    'PTSI, physique : célérité, retard, phase; les équations distribuées sont un prolongement.',
    'PSI, physique des ondes : câble coaxial et propagation; PT : réinvestissement de réflexion et d’ondes stationnaires.',
    'Équations des télégraphistes, impédance d’entrée et adaptation des câbles réels.',
    ['Choisir L=0,25 µH/m et C=100 pF/m; estimer √(L/C).','Comparer les charges de 50 Ω et 200 Ω.','Augmenter R et G, puis lire la diminution de puissance entre les extrémités.'],
    'Une ligne adaptée réfléchit peu; une désadaptation module le profil. Les pertes abaissent la puissance transmise.')
lesson('ligne_transmission','Passer d’une portion de câble au modèle distribué','Spé · PSI, prolongement PT',
    '<p>À la position x (m), V(x) et I(x) désignent les amplitudes complexes crêtes de tension et de courant. R, L, G et C sont les paramètres par mètre, en Ω/m, H/m, S/m et F/m. La pulsation ω s’exprime en rad/s.</p><p>Sur une portion dx : dV/dx=−(R+jωL)I et dI/dx=−(G+jωC)V. On en déduit γ²=(R+jωL)(G+jωC), où γ=α+jβ est en m⁻¹. Une onde qui avance vers la charge est proportionnelle à e<sup>−γx</sup>. Si R=G=0, la célérité vaut c=1/√(LC), et Z₀=√(L/C) est réel.</p>')
lesson('ligne_transmission','La réflexion explique les bosses de tension','Au-delà · lignes',
    '<p>On appelle Zcharge l’impédance terminale et Z₀ l’impédance caractéristique, en ohms. Le coefficient Γ=(Zcharge−Z₀)/(Zcharge+Z₀) relie l’onde réfléchie à l’onde incidente au bout du câble. Γ=0 signifie adaptation; une tension uniforme n’est toutefois attendue que si les pertes sont faibles.</p><p>Avec V et I en amplitudes crêtes, la puissance active est P=Re(VI*)/2. Les équations locales donnent dP/dx=−(R|I|²+G|V|²)/2. Une bosse d’amplitude n’implique donc pas une création d’énergie : elle peut résulter d’une interférence.</p>')
exercise('ligne_transmission','Ordre de grandeur d’un câble','Sup',
    'Une ligne sans pertes possède L=0,25 µH/m et C=100 pF/m. Calculer son impédance caractéristique et le retard sur 20 m.',
    'Z₀=√(L/C)=50 Ω. c=1/√(LC)=2×10⁸ m/s. Le retard d/c vaut 100 ns.')
exercise('ligne_transmission','Comparer deux terminaisons','Spé',
    'Pour Z₀=50 Ω réel, calculer Γ avec une charge de 50 Ω puis de 200 Ω. Quel pourcentage de la puissance incidente est réfléchi dans le second cas ?',
    'Γ=0 puis Γ=(200−50)/(200+50)=0,6. Pour une ligne sans pertes, la fraction de puissance réfléchie est |Γ|²=0,36, soit 36 %.')
exercise('ligne_transmission','Vérifier une perte locale','Au-delà',
    'En un point, les amplitudes crêtes sont |I|=0,10 A et |V|=5 V. R=0,02 Ω/m et G=2 µS/m. Calculer −dP/dx.',
    '−dP/dx=(R|I|²+G|V|²)/2=(0,02×0,01+2×10⁻⁶×25)/2=1,25×10⁻⁴ W/m. Les deux contributions sont positives.')

guide('rlc_transitoire','Identifier le régime d’un RLC et vérifier son bilan d’énergie.',
    ['E est l’échelon de tension (V). R est la résistance série totale (Ω), L l’inductance (mH au réglage, H dans les calculs), C la capacité (µF au réglage, F dans les calculs).', 't est le temps depuis la fermeture (s, affiché en ms); uC est la tension du condensateur (V) et i le courant de la maille (A).', 'ω₀=1/√(LC) est la pulsation propre (rad/s), ζ=R√(C/L)/2 le rapport d’amortissement sans unité.', 'EC=CuC²/2 et EL=Li²/2 sont les énergies stockées (J); W est le travail de la source et QJ l’énergie dissipée (J).'],
    ['uC(0)=0 et i(0)=0; échelon idéal et composants linéaires.', 'R inclut les résistances de la bobine et de la source lorsqu’elles sont présentes.'],
    ['Loi des mailles','Équation différentielle du second ordre','Continuité des variables de stockage','Bilan énergétique'],
    'PTSI, physique : oscillateurs amortis et circuits à deux éléments de stockage; mathématiques : EDO linéaire.',
    'PSI/PT : réinvestissement des pôles, de l’amortissement et des bilans.',
    'Identification des pertes réelles et amortissements dépendant de la fréquence.',
    ['Comparer R=20 Ω et R=300 Ω à L et C fixés.','Calculer 2√(L/C), puis choisir ce voisinage.','Comparer le travail fourni, les deux stockages et la dissipation cumulée.'],
    'Une résistance faible autorise les échanges oscillants; une résistance forte les amortit. Le bilan inclut toujours la source.')
lesson('rlc_transitoire','Deux conditions initiales pour deux stockages','Sup · PTSI',
    '<p>La maille contient une résistance R (Ω), une inductance L (H) et une capacité C (F). E est la tension de l’échelon (V); uC(t) est celle du condensateur et i(t) le courant (A).</p><p>Les relations i=CduC/dt et E=Ri+Ldi/dt+uC donnent LC uC″+RC uC′+uC=E. Le condensateur initialement déchargé impose uC(0)=0; l’absence de courant initial impose uC′(0)=0. Avec ω₀=1/√(LC) et ζ=R√(C/L)/2, les trois régimes correspondent à ζ&lt;1, ζ=1 et ζ&gt;1. L’absence d’oscillation ne signifie pas une charge instantanée.</p>')
lesson('rlc_transitoire','Un bilan qui ne se limite pas au condensateur','Sup · énergie',
    '<p>Les énergies stockées sont EC=CuC²/2 et EL=Li²/2, en joules. La puissance fournie par la source est Ei, en watts; la puissance dissipée est Ri².</p><p>La loi des mailles multipliée par i donne Ei=Ri²+d(EC+EL)/dt. Le travail de la source depuis t=0 est W=E∫i dt=E×C×uC, où E est la tension d’échelon et C la capacité. À l’établissement complet, uC=E et i=0 : la source a fourni CE², dont CE²/2 est stockée et CE²/2 dissipée. Ce résultat ne dépend pas de la valeur positive de R.</p>')
exercise('rlc_transitoire','Choisir le régime critique','Sup',
    'L=20 mH et C=10 µF. Calculer la résistance critique et la fréquence propre.',
    'Rcrit=2√(L/C)≈89,44 Ω. ω₀≈2236 rad/s et f₀=ω₀/(2π)≈355,9 Hz.')
exercise('rlc_transitoire','Lire un départ sans saut','Sup',
    'Un RLC série déchargé reçoit E=5 V à t=0. Peut-on avoir uC(0+)=5 V ou i(0+)≠0 ? Quelle dérivée démarre le courant ?',
    'La tension du condensateur et le courant de la bobine sont continus : uC(0+)=0 et i(0+)=0. La maille donne di/dt(0+)=E/L. Il peut y avoir un saut de dérivée, pas des variables de stockage.')
exercise('rlc_transitoire','Partager l’énergie de la source','Spé',
    'C=10 µF et E=5 V. Après établissement complet, calculer le travail fourni, l’énergie stockée et l’énergie dissipée.',
    'W=CE²=250 µJ. EC=CE²/2=125 µJ et EL=0. Le résistor a dissipé 125 µJ. Toute la charge injectée, CE, est passée sous la tension constante E.')

guide('resonance_impedance','Trouver une résonance en intensité et relier sa phase à sa puissance.',
    ['U est la tension efficace imposée (V). R, L et C sont la résistance (Ω), l’inductance (mH) et la capacité (µF) du circuit série.', 'f₀ est la fréquence propre (Hz); le réglage f/f₀ est sans unité. ω=2πf est en rad/s.', 'Z est l’impédance complexe (Ω), I le courant efficace complexe (A), φ=arg I−arg U le déphasage du courant (° dans l’affichage).', 'Q=ω₀L/R est le facteur de qualité sans unité; Δf est la largeur à mi-puissance (Hz); p(t) et sa moyenne P sont en W.'],
    ['RLC série, régime sinusoïdal établi; U reste constante pendant le balayage.', 'La résistance représente toutes les pertes série, indépendantes de f dans ce modèle.'],
    ['Impédances complexes','Module et argument','Résonance et demi-puissance','Moyenne d’un produit sinusoïdal'],
    'PTSI, physique : régime sinusoïdal et résonance; mathématiques : nombres complexes.',
    'PSI/PT : exploitation expérimentale d’une résonance; PSI : puissance sinusoïdale.',
    'Distinguer résonance en courant et maximum de tension aux bornes du condensateur.',
    ['Choisir f/f₀=1 et vérifier la phase nulle.','Passer à 0,5 puis à 2; comparer avance et retard du courant.','Multiplier R par dix et observer la largeur de la résonance.'],
    'À la résonance en intensité, le circuit série est résistif. Augmenter R réduit le maximum et élargit la bande.')
lesson('resonance_impedance','La phase révèle la nature du circuit','Sup · PTSI',
    '<p>U et I sont les valeurs efficaces complexes de tension et de courant. Avec une résistance R (Ω), une inductance L (H), une capacité C (F) et la pulsation ω (rad/s), Z=R+j(ωL−1/(ωC)) et I=U/Z.</p><p>En dessous de ω₀=1/√(LC), la partie imaginaire de Z est négative : le courant avance sur la tension. Au-dessus, il retarde. À ω₀, Z=R et Ieff=Ueff/R. La courbe temporelle compare u à Ri, deux tensions en volts : leur décalage représente celui de la tension et du courant.</p>')
lesson('resonance_impedance','Mesurer une largeur par la puissance','Spé · réinvestissement',
    '<p>On note P la puissance moyenne dans la résistance (W), Ieff le courant efficace (A) et f₀ la fréquence de résonance (Hz). P=RIeff² atteint son maximum Ueff²/R à f₀.</p><p>Aux fréquences f− et f+ de mi-puissance, Ieff=Imax/√2, donc |ωL−1/(ωC)|=R. Le calcul donne Δf=f+−f−=R/(2πL) et Q=f₀/Δf=ω₀L/R. Ces relations sont exactes pour ce RLC série. L’approximation f±≈f₀±Δf/2 demande Q grand.</p>')
exercise('resonance_impedance','Tension et courant à l’accord','Sup',
    'À la résonance, Ueff=5 V et R=20 Ω. Trouver le courant efficace, son amplitude crête et la puissance active.',
    'Ieff=0,25 A, Icrête=√2 Ieff≈0,354 A et P=Ueff²/R=1,25 W. Le courant est en phase avec la tension.')
exercise('resonance_impedance','Interpréter une impédance','Sup',
    'Une mesure donne Z=30−40j Ω. Pour Ueff=10 V, calculer Ieff et la phase du courant par rapport à la tension.',
    '|Z|=50 Ω, donc Ieff=0,20 A. arg Z≈−53,13°, donc le courant avance de 53,13° sur la tension. La puissance active vaut R Ieff²=1,2 W.')
exercise('resonance_impedance','Identifier une résistance totale','Spé',
    'Une bobine de L=20 mH est en série dans un RLC. La largeur à mi-puissance est 160 Hz. Quelle résistance série totale en déduire ?',
    'R=2πLΔf≈20,11 Ω. Cette résistance comprend le résistor, les pertes de la bobine et toute résistance source série.')

guide('mesure_impedance','Estimer une impédance sans confondre charge de la voie et incertitude de lecture.',
    ['R, L et C définissent le dipôle série choisi (Ω, mH, µF). f est la fréquence (Hz), E l’amplitude à vide du GBF (V), Rs sa résistance de sortie (Ω).', 'R₀ est le résistor de référence en série (Ω). V₁ et V₂ sont les amplitudes complexes crêtes lues avant R₀ et aux bornes du dipôle (V).', 'Rentrée et Centrée décrivent chaque voie d’oscilloscope (kΩ et pF au réglage). fb est sa bande passante (kHz au réglage).', 'Z est l’impédance du dipôle (Ω), Yvoie l’admittance d’une voie (S). urel est l’incertitude-type relative de chaque amplitude (%); u(|Zmes|) est l’incertitude-type propagée (Ω).', 'Δt est le retard de la voie 2 sur la voie 1 (µs); une valeur négative signifie une avance.'],
    ['Voies identiques, masse commune et régime sinusoïdal.', 'La propagation affichée porte sur deux lectures d’amplitude indépendantes; la phase, les charges et R₀ sont supposés connus.'],
    ['Diviseur de tension complexe','Mesure indirecte de courant','Correction de charge','Propagation différentielle des incertitudes'],
    'PTSI, formation expérimentale : GBF, oscilloscope, résistance d’entrée, bande passante et incertitudes.',
    'PSI/PT : mesure d’impédance, déphasage et interprétation de données.',
    'Voies désappariées et propagation complète incluant les incertitudes de phase.',
    ['Observer les deux voies pour un dipôle RC à 1 kHz.','Réduire la résistance d’entrée et comparer Zmes à Z corrigée.','Monter la fréquence jusqu’à la bande passante et lire la baisse d’amplitude.'],
    'Le rapport des voies annule une réponse commune, mais la voie 2 reste une charge parallèle du dipôle.')
lesson('mesure_impedance','Deux tensions donnent un courant','Sup · PTSI expérimental',
    '<p>Un résistor connu R₀ (Ω) précède le dipôle à mesurer. V₁ est la tension complexe en amont et V₂ la tension aux bornes du dipôle, en volts. Le courant dans R₀ est (V₁−V₂)/R₀ : Zmes=R₀V₂/(V₁−V₂).</p><p>La voie 2 possède une résistance Rentrée (Ω) et une capacité Centrée (F), donc Yvoie=1/Rentrée+jωCentrée. Zmes est le parallèle de cette voie et du dipôle. Si Yvoie est connue, Z=1/(1/Zmes−Yvoie). Réduire la perturbation par une sonde adaptée reste préférable à une correction numériquement mal conditionnée.</p>')
lesson('mesure_impedance','Une petite différence amplifie l’incertitude','Sup / spé · mesure',
    '<p>V₁ et V₂ sont les deux tensions complexes; leur différence complexe est D=V₁−V₂. L’incertitude-type relative de chaque lecture d’amplitude est ε, sans unité. La phase et R₀ sont supposés exacts et les deux lectures indépendantes.</p><p>Une propagation différentielle donne u(|Zmes|)/|Zmes|≈√2 ε |Re(V₁/D)|. Quand les deux voies sont proches, le courant déduit d’une différence est peu précis. Deux réponses de bande identiques H(f)=1/(1+jf/fb) se simplifient dans le rapport; leurs faibles amplitudes peuvent pourtant rendre la lecture difficile. Ce calcul ne décrit pas une erreur de phase ou une corrélation entre voies.</p>')
exercise('mesure_impedance','Un diviseur réel','Sup',
    'R₀=1 kΩ. Les amplitudes en phase sont V₁=4 V et V₂=2 V. Les voies sont supposées idéales. Déduire Z.',
    'I=(4−2)/1000=2 mA, puis Z=2/(2×10⁻³)=1 kΩ. La formule utilise des amplitudes de même nature, toutes deux crêtes ou toutes deux efficaces.')
exercise('mesure_impedance','Corriger la résistance d’entrée','Sup',
    'Un résistor de 10 kΩ est mesuré par une voie d’entrée de 100 kΩ, capacité négligeable. Quelle résistance parallèle est obtenue ? Comment retrouver 10 kΩ ?',
    'Rmes=10×100/(10+100)=9,091 kΩ. La correction 1/R=1/Rmes−1/Rentrée donne 10 kΩ. Le biais est de −9,09 %, même avec une lecture sans bruit.')
exercise('mesure_impedance','Préparer une mesure précise','Spé',
    'Les voies sont en phase, V₁=4 V et V₂=3,8 V. Chaque amplitude a une incertitude-type relative indépendante de 0,5 %. Estimer l’incertitude relative sur le module déduit.',
    '√2×0,005×4/0,2≈0,141, soit 14,1 %. La tension différentielle de 0,2 V est trop petite pour ces lectures. Choisir R₀ pour obtenir une chute plus importante, sans rendre V₂ trop faible.')

guide('pont_graetz','Identifier les diodes conductrices et distinguer moyenne, valeur efficace et pertes.',
    ['E est la crête de tension alternative par enroulement (V), f sa fréquence (Hz), t le temps (s). uAB=E sin(2πft) est la tension entre A et B (V).', 'R est la résistance de charge (Ω). Vd est le seuil de chaque diode (V). D₁, D₂, D₃, D₄ sont les diodes du pont.', 'uR et iR sont la tension et le courant de charge (V, A); isource est le courant alternatif (A). La moyenne et la valeur efficace de uR sont en V.', 'Le comparatif à point milieu utilise deux demi-enroulements opposés de même crête E; une seule diode conduit par alternance. Pcharge et Pdiodes sont des puissances moyennes (W).'],
    ['Charge purement résistive, sans filtrage capacitif.', 'Diodes idéales si Vd=0; sinon chute constante et courant inverse nul.'],
    ['Séparation des alternances','Vérification des états de diode','Moyenne et valeur efficace','Bilan de puissance'],
    'PTSI : application documentaire des mailles, valeurs efficaces et non-linéarités; le redresseur n’est pas un cours autonome exigible.',
    'PSI, physique §5.4 : réinvestissement des interrupteurs idéaux dans un autre convertisseur. PT : lien possible avec des systèmes étudiés en SI.',
    'Commutation réelle, résistance source et redressement filtré.',
    ['Prendre Vd=0 et vérifier que les deux sorties se superposent.','Prendre Vd=0,7 V et compter les chutes dans chaque montage.','Réduire E à 2 V et observer les intervalles bloqués.'],
    'La polarité de charge est conservée; le pont traverse deux diodes, le point milieu une seule.')
lesson('pont_graetz','Choisir une paire conductrice','Spé · PSI conversion',
    '<p>uAB est la tension alternative (V) entre les bornes A et B. Le courant iR (A) traverse une charge R (Ω), sous la tension positive uR (V). Chaque diode impose le seuil Vd (V) lorsqu’elle conduit.</p><p>Si uAB&gt;2Vd, D₁ et D₄ conduisent et uR=uAB−2Vd. Si uAB&lt;−2Vd, D₂ et D₃ conduisent et uR=−uAB−2Vd. Entre les seuils, la charge résistive ne reçoit aucun courant. Le résultat est uR=max(|uAB|−2Vd,0). Une hypothèse de conduction doit toujours être vérifiée par le sens du courant et la polarité des diodes bloquées.</p>')
lesson('pont_graetz','Deux montages, deux tensions de référence','Sup / spé · réinvestissement',
    '<p>E est la crête alternative (V) et f sa fréquence (Hz). Pour le pont idéal, uR=E|sin(2πft)|, sa moyenne vaut 2E/π et sa valeur efficace E/√2. L’ondulation a pour fréquence 2f.</p><p>Le montage à point milieu reçoit deux tensions opposées, chacune de crête E. Une seule diode conduit à la fois : avec un seuil Vd, uR=max(E|sin(2πft)|−Vd,0). La comparaison conserve ici la crête par demi-enroulement, pas la tension bout à bout du transformateur. Dans le pont, Psource=Pcharge+2Vd⟨iR⟩; avec des diodes idéales, les pertes du pont sont nulles.</p>')
exercise('pont_graetz','Moyenne et efficace','Sup',
    'Une tension sinusoïdale de crête 12 V et de fréquence 50 Hz alimente un pont idéal et une résistance de 100 Ω. Calculer la moyenne, la valeur efficace et la puissance de charge.',
    '⟨uR⟩=24/π≈7,64 V. Ueff=12/√2≈8,49 V. P=Ueff²/R=0,72 W. L’ondulation est à 100 Hz.')
exercise('pont_graetz','Compter les chutes de tension','Spé',
    'À un instant, |uAB|=5 V et chaque diode a un seuil de 0,7 V. Comparer les tensions de charge du pont et du point milieu à même tension de demi-enroulement.',
    'Le pont donne 5−2×0,7=3,6 V. Le point milieu donne 5−0,7=4,3 V. Ces résultats supposent que les tensions dépassent les seuils; sinon la sortie est nulle.')
exercise('pont_graetz','Fermer un bilan de puissance','Spé',
    'Un pont à seuil Vd=0,7 V débite un courant moyen de 0,10 A. La charge reçoit 2 W. Quelle puissance moyenne fournit la source ?',
    'Les deux diodes parcourues dissipent ensemble 2Vd⟨iR⟩=0,14 W. La source fournit donc 2,14 W. Un simple calcul avec la tension moyenne au carré ne remplace pas ⟨uR²⟩/R.')

guide('doubleur_tension','Comprendre la charge alternée de deux condensateurs et l’effet de la charge résistive.',
    ['E et f sont la crête de tension alternative (V) et sa fréquence (Hz). Le point milieu des condensateurs est relié à un pôle de cette source.', 'C₁ est la capacité supérieure et C₂ la capacité inférieure (µF au réglage). uC₁=Vhaut−Vmilieu et uC₂=Vmilieu−Vbas sont positives en fonctionnement normal (V).', 'R est la résistance entre les deux extrémités (Ω); Rs est la résistance série source (Ω); Vd est le seuil des diodes (V).', 'iD₁ et iD₂ sont les courants de recharge (A); iR=(uC₁+uC₂)/R est le courant de charge (A). L’ondulation est la différence entre maximum et minimum de sortie (V).'],
    ['Doubleur de Delon; condensateurs initialement déchargés.', 'Diodes à seuil constant; résistance source explicite pour limiter les courants.'],
    ['États des diodes','Lois des nœuds','Charge et décharge de condensateurs','Valeurs moyennes et régime établi'],
    'PTSI : prolongement des circuits RC et des stockages d’énergie.',
    'PSI : application des fonctions de commutation; PT/SI : mise en contexte de l’alimentation d’un système.',
    'Démarrage, asymétrie des capacités et conduction non linéaire.',
    ['Choisir une charge de 100 kΩ et lire les deux tensions de condensateur.','Réduire R à 1 kΩ et suivre la baisse de sortie.','Choisir C₁≠C₂ et comparer leurs ondulations.'],
    'La tension doublée est une limite à vide. Sous charge, chaque condensateur perd de la charge pendant les intervalles sans recharge.')
lesson('doubleur_tension','Deux condensateurs, une somme de tensions','Sup / spé · prolongement',
    '<p>Dans le doubleur de Delon, le point milieu M des condensateurs est relié à un pôle de la source alternative. On définit u₁=Vhaut−VM et u₂=VM−Vbas, en volts. La sortie entre les extrémités vaut u₁+u₂.</p><p>Pour une crête alternative E (V) et un seuil de diode Vd (V), l’alternance positive recharge le condensateur supérieur; l’alternance négative recharge l’inférieur. À vide et après établissement, chacun atteint E−Vd, soit une sortie 2(E−Vd). Un doubleur ne multiplie donc pas toute tension instantanée par deux; il accumule deux charges sur des alternances opposées.</p>')
lesson('doubleur_tension','Une diode bloquée ne conserve pas toujours la charge','Spé · PSI, application',
    '<p>La charge résistive R (Ω) reçoit iR=(u₁+u₂)/R (A). Les capacités C₁ et C₂ sont en farads, et les courants des diodes iD₁ et iD₂ en ampères.</p><p>Les nœuds donnent C₁u₁′=iD₁−iR et C₂u₂′=iD₂−iR. Si une diode est bloquée, son condensateur conserve sa charge uniquement à vide. Sous charge, il se décharge. Une capacité plus petite présente, pour un même débit, une pente plus forte. Le calcul utilise une résolution implicite des deux tensions et vérifie, à chaque pas, courant positif dans chaque diode conductrice et tension inverse dans chaque diode bloquée.</p>')
exercise('doubleur_tension','Limite à vide','Sup',
    'Un doubleur de Delon reçoit une sinusoïde de crête E=12 V. Chaque diode a un seuil de 0,7 V. Donner les tensions établies à vide.',
    'Chaque condensateur atteint environ 11,3 V. La sortie vaut 22,6 V, après la charge sur les deux alternances. Ce résultat ne décrit pas le démarrage ni le fonctionnement sous charge.')
exercise('doubleur_tension','Capacités différentes','Spé',
    'Pendant un court intervalle, les deux diodes sont bloquées et le courant de charge est 2 mA. C₁=50 µF et C₂=100 µF. Donner les pentes des deux tensions.',
    'u₁′=−iR/C₁=−40 V/s et u₂′=−20 V/s. La sortie décroît à −60 V/s. La plus petite capacité présente la plus forte ondulation.')
exercise('doubleur_tension','Estimer un stockage','Sup',
    'À vide, deux condensateurs de 100 µF portent chacun 12 V. Quelle énergie totale stockent-ils ? Quelle capacité équivalente donnerait la même énergie sous 24 V ?',
    'Énergie totale : 2×(100×10⁻⁶×12²/2)=14,4 mJ. La capacité équivalente sous 24 V est 50 µF, puisque les deux capacités égales sont en série entre les extrémités.')

guide('diode_rc','Déterminer quand une diode recharge réellement un condensateur.',
    ['usource(t)=E sin(2πft) est une tension imposée (V), de crête E (V) et fréquence f (Hz). Rs est la résistance série de la source (Ω).', 'La diode conduit de la source vers la sortie; Vd est son seuil (V), iD son courant orienté positif (A).', 'R et C sont en parallèle à la sortie : résistance en Ω, capacité en µF au réglage. uC=uR est leur tension (V).', 'τ=RC est le temps de décharge (s). L’ondulation est une tension crête à crête (V); la fraction de conduction est un pourcentage de période.'],
    ['Source de tension sinusoïdale; diode à seuil constant; Rs>0.', 'Condensateur initialement déchargé, huit périodes calculées.'],
    ['Loi des nœuds','Conditions de conduction et de blocage','Relaxation exponentielle','Comparaison des échelles RC et 1/f'],
    'PTSI, physique : RC et approche expérimentale des fonctions électroniques; diode comme modèle fourni.',
    'PSI : commutation spontanée et lissage de tension. PT/SI : analyse d’une alimentation ou d’un détecteur.',
    'Détection d’enveloppe, temps de conduction et impulsions de recharge.',
    ['Avec R=1 kΩ et C=100 µF, suivre une recharge et une décharge.','Passer à R=100 Ω et C=1 µF, puis comparer RC à T.','Afficher le courant de diode et repérer les changements d’état sur la dernière période.'],
    'L’arrêt de conduction est déterminé par la continuité de tension et la compatibilité du courant.')
lesson('diode_rc','Une seule équation de nœud, deux états','Sup / spé · RC et diode',
    '<p>La sortie uC (V) alimente une résistance R (Ω) et une capacité C (F) en parallèle. La diode fournit le courant iD (A). La source impose usource (V), avec une résistance série Rs (Ω) et un seuil Vd (V).</p><p>La loi des nœuds est C uC′=iD−uC/R. Si la diode est bloquée, iD=0 et la tension décroît exponentiellement. Si elle conduit, iD=(usource−Vd−uC)/Rs≥0. Il faut aussi vérifier que la diode bloquée n’est pas polarisée dans le sens passant. Le modèle ne remplace donc pas le circuit par une impédance unique valable sur toute une période.</p>')
lesson('diode_rc','Le maximum de source ne fixe pas le blocage','Spé · commutation',
    '<p>Pour étudier la limite idéale, on note E la crête de source, ω sa pulsation et τ=RC le temps de décharge. Avec une source de tension idéale et une diode sans seuil, la conduction impose uC=E sin(ωt).</p><p>Le courant demandé à la diode serait iD=CEω cos(ωt)+E sin(ωt)/R. Il reste positif au maximum de source, où cos(ωt)=0. Le blocage intervient lorsque ce courant devient nul, en général après ce maximum : tan(ωt)=−ωRC sur la branche descendante positive. La reprise dépend de la rencontre de la source montante avec la tension résiduelle du condensateur. Une source de courant imposé demanderait un autre circuit et d’autres équations.</p>')
exercise('diode_rc','Décharge entre deux recharges','Sup',
    'Une diode est bloquée. R=1 kΩ, C=100 µF et la sortie vaut initialement 10 V. Calculer la tension 20 ms plus tard.',
    'τ=RC=0,10 s. uC=10 exp(−0,020/0,10)≈8,19 V. La décharge n’est pas linéaire sur une durée comparable à τ.')
exercise('diode_rc','Vérifier l’état supposé','Spé',
    'usource=8 V, uC=9 V, Rs=20 Ω et Vd=0,7 V. L’hypothèse de diode conductrice est-elle admissible ?',
    'Elle imposerait iD=(8−0,7−9)/20=−85 mA, interdit dans ce modèle. La diode est bloquée, et le condensateur alimente seul la résistance.')
exercise('diode_rc','Le quart de période est-il un arrêt ?','Spé',
    'Dans la limite source idéale et diode idéale, uC suit E sin(ωt) pendant la conduction. R est finie. Évaluer iD à t=T/4 et conclure.',
    'À T/4, uC=E et uC′=0 : iD=E/R>0. La diode ne se bloque donc pas exactement au maximum de la sinusoïde. Il faut attendre C usource′+usource/R=0 sur la branche descendante.')

guide('triphase_transformateur','Appliquer le rapport de spires à un enroulement avant de calculer les grandeurs de ligne.',
    ['U₁ est la tension composée primaire efficace (V). Les tensions simples sont mesurées entre phase et neutre; les tensions composées entre phases.', 'N₁ et N₂ sont les nombres de spires; m=N₂/N₁ est sans unité. D signifie triangle, Y étoile. En triangle, un enroulement reçoit Uligne; en étoile, Uligne/√3.', 'Sref est la puissance apparente de référence (kVA au réglage). λ est la fraction du courant nominal; cosφ est le facteur de puissance de la charge.', 'U₂₀ et U₂ sont les tensions composées secondaires à vide et sous charge (V); I₂ est le courant de ligne (A).', 'Rs est la résistance série ramenée à une phase étoile secondaire (Ω); P₀ représente des pertes constantes (W). Pu, Pcuivre et η sont la puissance utile (W), les pertes cuivre (W), le rendement sans unité.'],
    ['Système équilibré à 50 Hz; polarités de bobinages fixées pour l’illustration.', 'Transformateur idéal avec résistance série secondaire et charge linéaire; pas de courant magnétisant détaillé.'],
    ['Différence de deux sinusoïdes décalées de 120°','Rapport de spires','Puissance triphasée équilibrée','Bilan de rendement'],
    'PTSI, physique : induction mutuelle et loi des tensions du transformateur; triphasé comme prolongement.',
    'PSI, physique : transformateur et conversion de puissance. Triphasé en PSI/PT : contexte technique, à relier au programme de SI effectivement étudié.',
    'Groupes horaires, essais à vide et en court-circuit, réactance de fuite.',
    ['Comparer D→Y à Y→Y avec le même rapport de spires.','Comparer vaN à vab et reconnaître le facteur √3.','Augmenter le courant de charge et lire les pertes cuivre ainsi que le rendement.'],
    'Le rapport de tensions de ligne inclut les couplages; le rendement nécessite les pertes, pas seulement le rapport de spires.')
lesson('triphase_transformateur','Le rapport de spires porte sur les bobinages','Spé · PSI; contexte PT/SI',
    '<p>U₁ et U₂₀ sont les tensions composées efficaces primaire et secondaire à vide (V). Le rapport de spires m=N₂/N₁ est sans unité. On définit k=√3 pour une étoile et k=1 pour un triangle.</p><p>Un enroulement primaire reçoit U₁/k₁; l’enroulement secondaire associé fournit mU₁/k₁. La tension composée secondaire vaut donc U₂₀=mU₁k₂/k₁. Pour un couplage D→Y, le rapport de tensions de ligne est √3m. Le neutre des tensions simples est réel en étoile ou fictif en triangle. Les décalages de 30° dépendent aussi de la polarité des enroulements et du groupe horaire.</p>')
lesson('triphase_transformateur','Calculer la puissance avec des grandeurs de ligne','Spé · conversion',
    '<p>U₂ est la tension composée efficace (V), I₂ le courant de ligne efficace (A) et cosφ le facteur de puissance d’une charge équilibrée sinusoïdale. Sa puissance utile vaut Pu=√3U₂I₂cosφ.</p><p>La résistance Rs (Ω) est ramenée à une phase étoile secondaire : Pcuivre=3RsI₂². Avec les pertes constantes P₀ (W), η=Pu/(Pu+Pcuivre+P₀). Le courant de référence Iref=λSref/(√3U₂₀) définit la charge par Zcharge=U₂₀(cosφ+j sinφ)/(√3Iref). Le calcul sous charge utilise I₂=(U₂₀/√3)/(Rs+Zcharge). Le courant réel baisse donc quand la résistance série devient importante. Une perte fixe pénalise surtout les faibles charges; les pertes cuivre croissent comme I₂².</p>')
exercise('triphase_transformateur','Triangle–étoile','Spé',
    'Le primaire est en triangle sous U₁=400 V. Le secondaire est en étoile et N₂/N₁=0,5. Calculer la tension d’un enroulement secondaire et la tension composée à vide.',
    'Chaque enroulement primaire reçoit 400 V; chaque secondaire fournit 200 V. La tension composée secondaire vaut √3×200≈346,4 V. Le rapport de tensions de ligne est 0,866, et non 0,5.')
exercise('triphase_transformateur','Puissance d’une charge équilibrée','Spé',
    'Une charge triphasée équilibrée reçoit U₂=400 V, I₂=10 A et cosφ=0,8. Trouver sa puissance active et apparente.',
    'S=√3×400×10≈6,928 kVA. P=S×0,8≈5,543 kW. Les valeurs de U₂ et I₂ sont composées et de ligne, toutes deux efficaces.')
exercise('triphase_transformateur','Rendement à partir des pertes','Spé',
    'Pu=10 kW, I₂=20 A, Rs=0,02 Ω par phase équivalente étoile et P₀=100 W. Calculer les pertes et le rendement.',
    'Pcuivre=3×0,02×20²=24 W. Pabs=10000+24+100=10124 W. η=10000/10124≈98,78 %. Le rapport de spires ne suffit pas à prévoir ce rendement.')

guide('onduleur_spectre','Comparer une valeur efficace et un spectre sans confondre THD total et THD tronqué.',
    ['E est la tension continue du bus (V), f la fréquence fondamentale (Hz), T=1/f la période (s).', 'δ est le retard d’allumage divisé par T, sans unité; la commande pleine onde correspond à δ=0. v vaut +E de δT à T/2, −E de (1/2+δ)T à T, zéro ailleurs.', 'n est le rang harmonique, N le dernier rang affiché. An est l’amplitude crête d’une raie (V); Vn,eff=An/√2 est sa valeur efficace (V).', 'Veff est la valeur efficace totale (V). THD est le rapport efficace des harmoniques hors fondamental au fondamental, sans unité, affiché en %.'],
    ['Onduleur idéal, demi-périodes opposées, tension moyenne nulle.', 'La reconstruction n’utilise que les N premiers rangs; la valeur efficace totale vient du signal exact.'],
    ['Intégrale d’une fonction par morceaux','Coefficients de Fourier','Parseval','Distinction crête / efficace'],
    'PTSI : valeurs efficaces, décomposition fournie et filtrage d’un signal périodique.',
    'PSI, physique §5.4 : structure d’onduleur; analyse spectrale réinvestie. PT : réinvestissement de l’analyse harmonique, contexte possible en SI.',
    'Modulation de largeur d’impulsion, filtrage de charge et temps morts.',
    ['Comparer les plateaux pleine onde et δ=1/4 pour E=175 V.','Comparer amplitudes crêtes et valeurs efficaces du fondamental.','Augmenter N et lire la convergence du THD tronqué vers le THD total.'],
    'La commande à T/4 réduit tension efficace et fondamental dans le même rapport. Pour ce signal idéal précis, son THD total égale celui de la pleine onde.')
lesson('onduleur_spectre','Intégrer le signal réellement commandé','Sup / spé · valeurs efficaces',
    '<p>E est la tension du bus continu (V), T la période (s) et δ le retard rapporté à T. La tension v est +E sur [δT,T/2[, −E sur [(1/2+δ)T,T[, et nulle ailleurs.</p><p>Sa durée non nulle est (1−2δ)T : Veff²=E²(1−2δ). Pour δ=1/4 et E=175 V, Veff=E/√2≈123,74 V. En pleine onde, Veff=E=175 V. Ces résultats ne dépendent pas d’une troncature du spectre. Les valeurs aux instants de commutation, isolés, ne changent pas les intégrales.</p>')
lesson('onduleur_spectre','Le fondamental et toutes les autres raies','Spé · Fourier',
    '<p>Pour un harmonique de rang n, An est son amplitude crête (V), et Vn,eff=An/√2 sa valeur efficace. La symétrie v(t+T/2)=−v(t) annule les rangs pairs. Pour n impair, An=4E|cos(nπδ)|/(nπ).</p><p>Le fondamental est donc A₁=4Ecos(πδ)/π. Le THD total vaut √(Veff²−V₁eff²)/V₁eff, par Parseval. À δ=0 et δ=1/4, ce rapport vaut dans les deux cas √(π²/8−1)≈48,34 %. Le décalage T/4 diminue les amplitudes, mais n’annule aucun rang impair. Le THD calculé avec seulement les raies affichées est plus petit; la reconstruction tronquée présente des oscillations près des sauts.</p>')
exercise('onduleur_spectre','Valeurs efficaces à T/4','Sup',
    'Un onduleur délivre E=175 V. La commande décalée vaut ±E pendant au total la moitié de la période et zéro le reste. Trouver les valeurs efficaces pleine onde et décalée.',
    'Pleine onde : Ueff=175 V. Commande décalée : Veff=175√(1/2)≈123,74 V. Ce sont des valeurs efficaces du signal complet, pas du seul fondamental.')
exercise('onduleur_spectre','Un THD calculé exactement','Spé',
    'Pour la pleine onde idéale de crête E, A₁=4E/π et Ueff=E. Calculer le THD total.',
    'U₁eff=4E/(π√2). THD=√(E²−8E²/π²)/(4E/(π√2))=√(π²/8−1)≈0,4834, soit 48,34 %. Le résultat est indépendant de E.')
exercise('onduleur_spectre','Rang 3 et commande décalée','Spé',
    'Avec δ=1/4, le troisième harmonique est-il annulé ? Quel est A₃/A₁ ?',
    '|cos(3π/4)|=cos(π/4)=1/√2. Donc A₃/A₁=1/3 : la raie de rang 3 reste présente. Une diminution de la valeur efficace totale ne prouve pas une diminution du THD.')

guide('hacheur_mcc','Calculer un courant d’induit avec les vrais états d’un hacheur série et de sa diode de roue libre.',
    ['E est la tension continue d’alimentation (V). Eₘ est la force contre-électromotrice de la machine (V), supposée constante sur les périodes affichées.', 'R est la résistance d’induit (Ω), L son inductance (mH). i est le courant d’induit positif en fonctionnement moteur (A).', 'f est la fréquence de hachage (kHz au réglage), T=1/f la période (s), α la fraction de période pendant laquelle l’interrupteur est fermé.', 'u est la tension aux bornes de l’ensemble R–L–Eₘ (V). iS et iD sont les courants de source et de roue libre (A).', 'imin, imax et ⟨i⟩ sont les courants minimal, maximal et moyen (A). Psource, R⟨i²⟩ et Eₘ⟨i⟩ sont les puissances moyennes (W).'],
    ['Interrupteur et diode de roue libre idéaux, convertisseur à un quadrant.', 'R, L et Eₘ constants; régime périodique électrique. La vitesse et le couple ne sont pas intégrés.'],
    ['Équations RL par état','Continuité du courant','Instant d’extinction','Moyenne d’une dérivée périodique','Bilan de puissance'],
    'PTSI : prolongement du RL et de la conversion électromécanique; le hacheur est abordé à partir d’un modèle fourni.',
    'PSI, physique §5.4 : hacheur série et moteur à courant continu, contenu central. PT : contexte de motorisation en SI, à distinguer du programme de physique.',
    'Conduction discontinue, ondulation exacte et couplage à la dynamique mécanique.',
    ['Lire le courant pendant fermeture et roue libre avec α=0,6.','Réduire L et f, puis observer l’extinction avant la fermeture suivante.','Augmenter Eₘ au-dessus de E et vérifier l’absence de courant moteur.'],
    'La relation ⟨u⟩=αE suppose une roue libre active pendant toute l’ouverture. L’extinction impose un troisième état.')
lesson('hacheur_mcc','La roue libre est une partie du circuit','Spé · PSI §5.4',
    '<p>Une source continue E (V) alimente une machine représentée par R (Ω), L (H) et la force contre-électromotrice Eₘ (V). Le courant i (A) est positif en fonctionnement moteur. L’interrupteur est fermé pendant αT, où T est la période et α le rapport cyclique.</p><p>Fermé : L i′+Ri+Eₘ=E. Ouvert, si la diode de roue libre conduit : L i′+Ri+Eₘ=0. Le courant reste continu et décroît. Quand il atteint zéro, la diode se bloque; le modèle à un quadrant interdit de poursuivre vers un courant négatif. La tension de la machine vaut alors Eₘ jusqu’à la prochaine fermeture.</p>')
lesson('hacheur_mcc','Moyennes et bilan du moteur','Spé · PSI conversion',
    '<p>En régime périodique établi, ⟨di/dt⟩=0. Si le courant reste strictement positif pendant l’ouverture, la tension moteur u (V) alterne entre E et zéro : ⟨u⟩=αE et ⟨i⟩=(αE−Eₘ)/R.</p><p>En conduction discontinue, l’état à courant nul ajoute un intervalle à u=Eₘ. Il faut calculer cet intervalle avant les moyennes. Le bilan de puissance est ⟨E iS⟩=R⟨i²⟩+Eₘ⟨i⟩, où iS est le courant de source. La bobine a une variation d’énergie moyenne nulle. Le terme Eₘ⟨i⟩ représente la conversion électromécanique; R⟨i⟩² sous-estime les pertes cuivre dès que le courant ondule.</p>')
exercise('hacheur_mcc','Courant moyen en conduction continue','Spé · PSI',
    'E=48 V, Eₘ=20 V, R=2 Ω et α=0,6. Supposer la conduction continue. Calculer la tension et le courant moyens.',
    '⟨u⟩=0,6×48=28,8 V. ⟨i⟩=(28,8−20)/2=4,4 A. Il reste à vérifier, avec L et f, que le courant minimal est positif.')
exercise('hacheur_mcc','Calculer l’instant d’extinction','Spé · PSI',
    'À l’ouverture, i(0)=2 A, L=1 mH, R=2 Ω et Eₘ=10 V. La roue libre impose Li′+Ri+Eₘ=0. Quand le courant atteint-il zéro ?',
    'i(t)=−Eₘ/R+(2+Eₘ/R)exp(−Rt/L). Le zéro est t₀=(L/R)ln(1+Ri(0)/Eₘ)=0,5 ms×ln(1,4)≈0,168 ms. Après t₀, la diode se bloque.')
exercise('hacheur_mcc','Évaluer les pertes d’un courant ondulé','Spé',
    'Le courant d’induit a une moyenne de 4 A et un écart-type temporel de 1 A. R=2 Ω et Eₘ=20 V. Calculer les puissances cuivre et électromécanique.',
    '⟨i²⟩=⟨i⟩²+σi²=17 A². Pcuivre=34 W et Pconversion=Eₘ⟨i⟩=80 W. Avec des interrupteurs idéaux, la source fournit 114 W. Utiliser R⟨i⟩² aurait omis 2 W.')

guide('puissances_compensation','Réduire le courant de ligne sans modifier la puissance active d’une charge.',
    ['U est la tension efficace de source (V), f sa fréquence (Hz), ω=2πf sa pulsation (rad/s).', 'R et L sont la résistance (Ω) et l’inductance (mH) en série dans la charge. C est la capacité ajoutée en parallèle (µF).', 'Icharge, IC et Iligne sont les courants efficaces complexes (A). Le courant positif entre dans chaque branche.', 'P est la puissance active (W), Q la puissance réactive (var), S la puissance apparente (VA), P/S le facteur de puissance sans unité.', 'Copt est la capacité qui annule Q (µF). La compensation peut réduire ou augmenter le module du courant de ligne.'],
    ['Régime sinusoïdal établi; tension imposée et composants idéaux.', 'Le condensateur est en parallèle, donc la charge RL conserve la même tension.'],
    ['Addition de courants complexes','Puissance complexe en valeurs efficaces','Compensation d’une puissance réactive','Minimisation d’un module'],
    'PTSI : nombres complexes et puissance instantanée; la compensation est un prolongement.',
    'PSI, physique §5.1 : puissance active, facteur de puissance et adaptation énergétique. PT : contexte technique de la conversion et des systèmes électriques en SI.',
    'Puissance en régime déformé, harmoniques et facteur de puissance global.',
    ['Choisir C=0 et lire P, Q et le courant de ligne.','Régler C près de Copt; repérer le courant minimal.','Dépasser Copt et observer le retour d’un courant réactif, de signe opposé.'],
    'Le minimum de courant correspond à Q=0; ajouter trop de capacité détériore le facteur de puissance.')
lesson('puissances_compensation','Utiliser des valeurs efficaces complexes','Spé · PSI §5.1',
    '<p>U est la tension efficace complexe de référence (V), réelle ici. I est le courant efficace complexe reçu par la charge (A). La puissance complexe est U I*=P+jQ, en VA : P est sa partie active en watts, Q sa partie réactive en vars.</p><p>La puissance apparente est S=U|I|, et le facteur de puissance est P/S. Pour un courant sinusoïdal de retard φ, P=UIeff cosφ et Q=UIeff sinφ. La puissance instantanée u(t)i(t) oscille à deux fois la fréquence de source autour de P. En régime déformé, le facteur de puissance reste P/(UeffIeff), mais ne se réduit plus au seul cosinus d’un déphasage.</p>')
lesson('puissances_compensation','Trouver la bonne capacité, puis s’arrêter','Spé · bilan',
    '<p>La charge série possède R (Ω) et L (H), à la pulsation ω (rad/s). Sous U (V efficace), son courant est Icharge=U/(R+jωL). Une capacité C (F) en parallèle fournit IC=jωCU.</p><p>Le courant de ligne est Icharge+IC. La charge absorbe Qcharge=U²ωL/[R²+(ωL)²], tandis que le condensateur a Qc=−ωCU². La compensation parfaite exige Copt=L/[R²+(ωL)²]. Elle minimise le courant de ligne à puissance active inchangée. Pour C&gt;Copt, la puissance réactive devient négative et le courant augmente de nouveau : une compensation excessive n’améliore pas le bilan.</p>')
exercise('puissances_compensation','Puissance d’un courant en retard','Spé',
    'Ueff=230 V, Ieff=5 A et le courant retarde de 36,87°. Calculer P, Q et S.',
    'cosφ=0,8 et sinφ=0,6. S=1150 VA, P=920 W et Q=690 var. Le facteur de puissance vaut 0,8; Q est positif pour la charge inductive.')
exercise('puissances_compensation','Choisir un condensateur','Spé',
    'Une charge absorbe Q=690 var sous 230 V à 50 Hz. Quelle capacité parallèle idéale annule cette puissance réactive ?',
    'Qc=−ωCU², donc C=690/(2π×50×230²)≈41,52 µF. Sa puissance active idéale est nulle; la source fournit toujours la puissance active de la charge.')
exercise('puissances_compensation','Détecter une surcompensation','Spé',
    'Sous U=230 V, une charge absorbe P=920 W et Q=690 var. Le condensateur fournit Qc=−1000 var. Calculer le nouveau courant de ligne.',
    'Qtotal=−310 var. S=√(920²+310²)≈970,8 VA et Iligne=S/U≈4,22 A. Le courant était 5 A sans compensation, mais son minimum à Q=0 serait P/U=4 A. Le courant est désormais en avance.')
