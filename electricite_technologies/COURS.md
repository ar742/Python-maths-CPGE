# Électricité & Technologies — 72 leçons

Recueil de A. R., fiches P15–P19, pages 386–433. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.

## 01. Une sortie garde la trace de son état initial

Sup · Physique · Laboratoire `laplace_initiales`

La sortie **y** vérifie τ dy/dt+y=KE après l’application d’une tension constante E. Le gain K et la constante de temps τ sont fixés. À t=0, la sortie vaut y₀.

La solution est y(t)=KE+(y₀−KE)e^(−t/τ). Elle respecte y(0)=y₀ et tend vers KE. Le terme y₀e^(−t/τ) décrit la réponse libre ; KE(1−e^(−t/τ)) décrit la réponse à l’entrée, au repos initial.

## 02. Un transfert suppose un état initial nul

Spé · SI / au-delà · Mathématiques · Laboratoire `laplace_initiales`

On note p la variable de Laplace et Y(p) la transformée unilatérale de y(t). La dérivée devient pY(p)−y₀. Il vient (1+τp)Y(p)=KE/p+τy₀.

Le transfert H(p)=K/(1+τp) relie entrée et sortie quand y₀=0. Il ne contient pas à lui seul la réponse due à un état initial chargé. En SI, on utilise les réponses canoniques ; le calcul d’inversion générale est un prolongement mathématique.

## 03. Passer de la forme canonique au diagramme de Bode

Sup / Spé · Physique et SI · Laboratoire `bode_second_ordre`

Le transfert est H(p)=Kω₀²/(p²+2ζω₀p+ω₀²). K est le gain statique, ω₀ la pulsation propre et ζ l’amortissement. En régime sinusoïdal, on pose p=jω, où j²=−1.

Le module est K/√[(1−(ω/ω₀)²)²+4ζ²(ω/ω₀)²]. Le gain en dB vaut 20 log₁₀|H|. La phase doit tenir compte du quadrant du dénominateur ; elle passe de 0° à −180°. À haute fréquence, la pente tend vers −40 dB par décade.

## 04. Distinguer résonance et dépassement

Spé · SI · Laboratoire `bode_second_ordre`

Une résonance apparaît pour ζ<1/√2 ; sa pulsation vaut ωᵣ=ω₀√(1−2ζ²). Le pic disparaît avant que les oscillations temporelles disparaissent.

Après un échelon unité et un départ au repos, le dépassement relatif vaut exp[−πζ/√(1−ζ²)] pour ζ<1. Pour ζ≥1, la réponse est monotone. Les formules temporelles sont fournies : leur inversion de Laplace n’est pas exigée en SI.

## 05. Réduire un retour négatif

Sup / Spé · SI · Laboratoire `retroaction_sensibilite`

L’entrée est e, la sortie s, le gain direct μ et le gain du capteur β. L’erreur vaut ε=e−βs et la chaîne directe donne s=με au régime permanent.

En remplaçant ε, on obtient s(1+μβ)=μe, puis G=s/e=μ/(1+μβ). Le produit μβ est le gain de boucle statique. Pour μβ grand, G se rapproche de 1/β, à condition que β reste fixé.

## 06. Comparer sensibilité locale et variation finie

Au-delà · SI · Laboratoire `retroaction_sensibilite`

La sensibilité relative à μ est Sμ=(μ/G)dG/dμ=1/(1+μβ). Une petite variation dμ produit dG/G=Sμ dμ/μ.

Pour une variation finie δ, utiliser μ₂=μ(1+δ), puis recalculer G₂ exactement. Une variation de 50 % n’est pas automatiquement petite. Le retour protège surtout contre les variations de la chaîne directe ; une erreur du capteur β affecte aussi la valeur finale.

## 07. Le TP en boucle ouverte

Sup · SI · Laboratoire `moteur_x`

Un amplificateur de gain μ précède le moteur X de transfert K₀/(1+τp). K₀ s’exprime en rad·s⁻¹/V et τ en secondes. Le transfert tension-vitesse est T(p)=μK₀/(1+τp).

À partir du repos, une tension E appliquée en échelon donne Ω(t)=μK₀E(1−e^(−t/τ)). La vitesse permanente est μK₀E et 63,2 % de cette vitesse est atteint à t=τ.

## 08. Fermer le retour du TP

Spé · SI · Laboratoire `moteur_x`

Le capteur convertit Ω′ en tension βΩ′. L’erreur appliquée à l’amplificateur vaut ε=E−βΩ′. En éliminant ε, on obtient T′(p)=μK₀/(1+μβK₀+τp).

La forme canonique donne T₀′=μK₀/(1+μβK₀) et τ′=τ/(1+μβK₀). Le retour raccourcit le transitoire et réduit le gain au même E. Pour demander une vitesse précise, la consigne et l’étalonnage du capteur doivent être interprétés ensemble.

## 09. Deux bilans couplés

Sup / Spé · SI · Laboratoire `moteur_mcc`

La tension U alimente un induit de résistance R et d’inductance L. Le courant i crée le couple ki. La vitesse Ω crée la force contre-électromotrice kΩ. Les constantes ont la même valeur numérique en unités SI.

Les équations sont L di/dt=U−Ri−kΩ et J dΩ/dt=ki−bΩ−Cᵣ. L’inertie J, le frottement visqueux b et le couple résistant Cᵣ définissent la charge. Le courant et la vitesse se déterminent ensemble.

La durée électrique L/R peut être bien plus courte que le démarrage mécanique. La vue courte du courant résout cette montée ; elle la compare au courant (U/R)(1−exp(−Rt/L)) d’un rotor maintenu immobile, où t est le temps en secondes.

## 10. Vérifier l’équilibre et la puissance

Spé · SI · Laboratoire `moteur_mcc`

Au régime permanent, les dérivées sont nulles. On obtient Ω∞=(kU−RCᵣ)/(Rb+k²), puis i∞=(U−kΩ∞)/R. Une charge accrue réduit la vitesse et augmente le courant.

La puissance électrique Ui se répartit entre pertes Joule Ri², variation d’énergie magnétique et puissance convertie kiΩ. Côté mécanique, cette dernière alimente la variation d’énergie cinétique, le frottement bΩ² et la charge CᵣΩ. Le modèle signé ne comporte pas de frottement sec.

## 11. Ajouter une action intégrale

Spé · SI · Laboratoire `correcteur_pi`

La consigne r et la sortie y définissent l’erreur e=r−y. Un PI demande u=Kₚe+v, où dv/dt=(Kₚ/Tᵢ)e. L’action proportionnelle répond immédiatement ; l’action intégrale accumule l’écart.

Si l’équilibre est accessible et le PI actif, dv/dt=0 impose e=0. Une intégrale ne crée pas une commande disponible sans limite : pour un procédé de gain K et une limite uₘₐₓ, il faut |r|≤Kuₘₐₓ.

## 12. Que se passe-t-il pendant une saturation ?

Au-delà · SI · Laboratoire `correcteur_pi`

La commande appliquée u est limitée, alors que Kₚe+v peut continuer de croître. Tant que l’erreur conserve son signe, v s’accumule ; la sortie peut tarder à revenir après la baisse de consigne.

La correction proposée ajoute [u−(Kₚe+v)]/Tᵢ à dv/dt. Elle ramène l’intégrale vers une valeur compatible avec l’actionneur. Cette correction de saturation est un prolongement ; elle ne remplace pas le réglage de stabilité du PI.

## 13. Lire deux distances à une limite

Spé · SI · Laboratoire `stabilite_marges`

La boucle ouverte vaut L(p)=K/[(1+τ₁p)(1+τ₂p)(1+τ₃p)]. À la pulsation ωc où |L|=1, la marge de phase est 180°+arg L(jωc). À la pulsation ωπ où la phase est −180°, la marge de gain en dB vaut −20 log₁₀|L(jωπ)|.

Si K≤1, le gain n’atteint pas 0 dB à une pulsation strictement positive : la marge de phase n’a pas de croisement de référence. Il faut afficher cette absence plutôt qu’une valeur artificielle.

## 14. Comparer aux pôles fermés

Spé · SI / au-delà · Mathématiques · Laboratoire `stabilite_marges`

Avec un retour négatif unitaire, le transfert fermé est L/(1+L). Ses pôles vérifient (1+τ₁p)(1+τ₂p)(1+τ₃p)+K=0. Un pôle à partie réelle positive entraîne une croissance temporelle.

Pour trois constantes égales τ, la limite se produit à K=8 et ωπ=√3/τ. Ce cas permet de vérifier les marges sans faire appel aux critères de Routh ou de Nyquist, qui ne sont pas au programme SI.

## 15. Lire le capteur et le signe de la force

Spé · SI · P17 · Laboratoire `isolation_sismique`

Le déplacement du sol est x₀, celui de la masse x. La plante vérifie x=I(x₀−αF), où I(p)=ωᵣ²/(p²+ωᵣ²). Le capteur mesure **x−x₀** et l’actionneur dérivateur donne F=ηp(x−x₀).

En remplaçant F puis en regroupant x, on obtient G(p)=x/x₀=(ωᵣ²+cp)/(p²+cp+ωᵣ²), avec c=αηωᵣ². Le retour est aussi une anticipation du mouvement du sol : le terme cp apparaît au numérateur.

## 16. Amortir une résonance ne filtre pas tout

Sup · Physique / spé · SI · Laboratoire `isolation_sismique`

Le dénominateur est celui d’un second ordre d’amortissement ζ=c/(2ωᵣ). Pour η>0, le modèle est amorti. Sans contrôle, η=0 : la résonance exacte n’a pas de régime périodique borné.

À haute pulsation, le transfert sans contrôle décroît comme ωᵣ²/ω². Avec le dérivateur idéal, il décroît comme c/ω. Le contrôle atténue la résonance mais peut transmettre davantage le mouvement rapide. Les courbes temporelles incluent le départ au repos.

## 17. Pourquoi les échantillons peuvent tromper

Spé · Physique PT/PSI · Laboratoire `echantillonnage_adc`

Un signal est mesuré à tₖ=k/fₑ. Pour toute fréquence f, ajouter un multiple entier de fₑ conserve la phase à ces instants. Le signal continu d’origine n’est donc pas déterminé par les seules valeurs sans hypothèse de bande limitée.

Pour éviter le repliement d’un signal de fréquence maximale fₘₐₓ, on impose fₑ>2fₘₐₓ et on limite réellement la bande avant l’acquisition. Un filtre antirepliement est nécessaire si des composantes plus rapides sont présentes.

## 18. Coder une tension sur un nombre fini de niveaux

Spé · Physique PT/PSI · Laboratoire `echantillonnage_adc`

Un convertisseur de N bits possède 2ᴺ codes. Pour la plage [−Vₘₐₓ,+Vₘₐₓ], le modèle utilisé a un pas q=2Vₘₐₓ/2ᴺ. Chaque code représente le centre d’un intervalle ; hors saturation, l’erreur reste dans [−q/2,+q/2].

Augmenter N réduit le pas ; cela ne corrige pas une acquisition repliée. L’approximation d’une erreur uniforme donne une valeur RMS q/√12, mais une série déterministe d’échantillons ne suit pas toujours ce modèle statistique.

## 19. Une somme de valeurs retardées

Spé · Physique PT/PSI · Laboratoire `filtre_rif`

Le filtre calcule yₖ=(xₖ+xₖ₋₁+…+xₖ₋ₙ₊₁)/N. Les valeurs antérieures au début sont nulles. Une impulsion x₀=1 puis 0 donne hₖ=1/N pendant N termes, puis hₖ=0.

La réponse impulsionnelle est finie : le filtre est RIF. Pour une entrée constante, la somme des coefficients vaut 1, donc le signal constant est conservé après le remplissage de la mémoire.

## 20. Choisir la fenêtre selon la fréquence

Au-delà · Traitement du signal · Laboratoire `filtre_rif`

On note z la variable du temps discret et z⁻¹ un retard. H(z)=(1/N)Σⱼ₌₀ᴺ⁻¹z⁻ʲ. Sur le cercle unité, z=e^(j2πf/fₑ) ; des annulations apparaissent pour f=m fₑ/N, hors f=0.

Les coefficients symétriques donnent un retard de groupe (N−1)Tₑ/2 hors les zéros. Agrandir la fenêtre ne conserve pas toutes les fréquences utiles : il faut comparer leur gain avec celui du bruit.

## 21. Une suite géométrique dans un filtre

Sup · Mathématiques / spé · Physique · Laboratoire `filtre_rii_z`

La récurrence est yₖ=a yₖ₋₁+(1−a)xₖ, avec y₋₁=0. L’impulsion discrète x₀=1 puis 0 produit hₖ=(1−a)aᵏ. La sortie d’un échelon xₖ=1 vaut 1−a^(k+1).

Si 0<a<1, la mémoire décroît sans alternance. Si −1<a<0, elle alterne ; le filtre ne se comporte plus comme le même passe-bas lent. Pour a=0, yₖ=xₖ : la mémoire disparaît.

## 22. Un pôle et un critère de stabilité

Au-delà · Temps discret · Laboratoire `filtre_rii_z`

Avec une mémoire initiale vide, H(z)=(1−a)/(1−az⁻¹)=(1−a)z/(z−a). Le pôle est a, sauf si a=0 où il se simplifie. La somme Σ|hₖ| vaut |1−a|/(1−|a|) pour |a|<1.

Cette somme finie garantit qu’une entrée bornée produit une sortie bornée. Une réponse qui décroît lentement peut être stable. Il faut distinguer une grande durée de mémoire d’un pôle situé sur ou hors du cercle unité.

## 23. Retrouver Euler implicite dans P17

Spé · Physique / au-delà · Temps discret · Laboratoire `discretisation`

Le filtre analogique vérifie τ dy/dt+y=x. La différence arrière (yₖ−yₖ₋₁)/Tₑ donne yₖ=a yₖ₋₁+b xₖ, avec a=τ/(τ+Tₑ) et b=Tₑ/(τ+Tₑ).

Pour τ=1 ms et Tₑ=50 µs, a=20/21 et b=1/21. Le cas y₀=1, x₁=1 puis 0 donne y₁=1, puis yₖ=(20/21)^(k−1) pour k≥1. La réponse impulsionnelle à état initial nul donne au contraire y₁=1/21.

## 24. Comparer trapèzes et maintien exact

Au-delà · Temps discret · Laboratoire `discretisation`

La règle des trapèzes conduit à yₖ=aB yₖ₋₁+bB(xₖ+xₖ₋₁), où aB=(2τ−Tₑ)/(2τ+Tₑ) et bB=Tₑ/(2τ+Tₑ). Le transfert bilinéaire contient donc **1+z⁻¹** au numérateur.

Une entrée constante sur ]tₖ₋₁,tₖ] donne exactement yₖ=e^(−Tₑ/τ)yₖ₋₁+(1−e^(−Tₑ/τ))xₖ. Les indices fixent la présence d’un retard dans un transfert ZOH : une entrée indexée par la borne gauche agit au pas suivant. La comparaison affiche la convention utilisée.

## 25. Deux pôles conjugués dans le plan z

Au-delà · Temps discret · Laboratoire `polezero_z`

Les pôles sont r e^(±jθ), où r est leur module et θ leur angle en radians. Leur polynôme est z²−2r cos(θ)z+r². La récurrence homogène produit des oscillations de fréquence relative θ/(2π), dont l’enveloppe décroît comme rᵏ.

Le critère |r|<1 assure la décroissance. Il concerne le module dans le plan z ; en temps continu, on utilise au contraire la partie réelle du pôle. Les deux critères ne se lisent pas sur le même axe.

## 26. Mettre un creux à une fréquence choisie

Au-delà · Traitement du signal · Laboratoire `polezero_z`

Deux zéros e^(±jψ) sur le cercle unité donnent le numérateur c(1−2cos(ψ)z⁻¹+z⁻²). Sur z=e^(j2πf/fₑ), le gain s’annule pour f/fₑ=ψ/(2π).

Le facteur c normalise le gain continu à 1. Le creux est exact à la fréquence choisie ; une raie voisine n’est pas nécessairement fortement atténuée. Des pôles proches de la même direction peuvent rendre le voisinage plus sélectif.

## 27. Le spectre du multiplicateur de P19

Spé · Physique PSI · Laboratoire `modulation_am`

Le message est cos(2πft) et la porteuse cos(2πFt), avec F>f. La tension modulée est uAM=U[1+m cos(2πft)]cos(2πFt), où U est l’amplitude porteuse et m le taux de modulation. Pour un multiplicateur recevant deux tensions d’amplitudes UBF et UHF, U=Kₘ UBF UHF ; le gain Kₘ s’exprime en V⁻¹.

Le produit donne U cos(2πFt)+(mU/2)cos[2π(F+f)t]+(mU/2)cos[2π(F−f)t]. Le spectre en amplitude comporte une porteuse U et deux bandes latérales mU/2. La largeur de bande de cet exemple monochromatique vaut 2f.

## 28. Suivre l’enveloppe et conserver le signe

Spé · Physique PSI / au-delà · Laboratoire `modulation_am`

Pour 0≤m≤1, U[1+m cos(2πft)] reste positif. Une diode et un circuit RC peuvent suivre les crêtes si 1/F≪RC≪1/f. Ces repères sont approximatifs ; près de m=1, la décharge nécessaire au voisinage des minima impose un choix plus contraignant. Le détecteur simulé est idéal ; les écarts montrent l’ondulation et le suivi imparfait du message.

Pour m>1, le facteur change de signe : l’enveloppe géométrique en prend la valeur absolue. Une détection d’enveloppe ne peut plus retrouver le signe. Une démodulation synchrone multiplie par une porteuse de référence puis filtre les hautes fréquences ; elle est étudiée en physique PSI.

## 29. Suivre les branches avant de poser une formule

Sup · PTSI · Laboratoire `pont_wheatstone`

A et C alimentent le pont; B et D sont les points milieux. On prend VC=0 et VA=E, où E est la tension appliquée en volts. Les résistances R₁, R₂, R₃ et R₄, en ohms, suivent les connexions A–R₁–B–R₂–C et A–R₃–D–R₄–C.

Un voltmètre idéal donne VB=ER₂/(R₁+R₂) et VD=ER₄/(R₃+R₄). Sa lecture est UBD=VB−VD. Le pont est donc équilibré si **R₂R₃=R₁R₄**. Cette égalité doit être déduite des connexions, car permuter deux indices change sa forme.

## 30. Un zéro robuste, une sensibilité modifiée

Spé · mesure · Laboratoire `pont_wheatstone`

On appelle U₀ la tension du pont à vide, Rm la résistance du voltmètre et Rth la résistance du pont vue de B–D, toutes les résistances étant en ohms. Après extinction de la source idéale, Rth=R₁R₂/(R₁+R₂)+R₃R₄/(R₃+R₄).

Le voltmètre lit U=U₀Rm/(Rm+Rth). Cette charge atténue une petite tension, mais U=0 reste équivalent à U₀=0. À l’équilibre R₄=R₄*, une petite variation ΔR₄ produit, à vide, ΔU≈−ER₃ΔR₄/(R₃+R₄*)². L’approximation exige |ΔR₄| petit devant R₃+R₄*.

## 31. Passer d’une portion de câble au modèle distribué

Spé · PSI, prolongement PT · Laboratoire `ligne_transmission`

À la position x (m), V(x) et I(x) désignent les amplitudes complexes crêtes de tension et de courant. R, L, G et C sont les paramètres par mètre, en Ω/m, H/m, S/m et F/m. La pulsation ω s’exprime en rad/s.

Sur une portion dx : dV/dx=−(R+jωL)I et dI/dx=−(G+jωC)V. On en déduit γ²=(R+jωL)(G+jωC), où γ=α+jβ est en m⁻¹. Une onde qui avance vers la charge est proportionnelle à e^(−γx). Si R=G=0, la célérité vaut c=1/√(LC), et Z₀=√(L/C) est réel.

## 32. La réflexion explique les bosses de tension

Au-delà · lignes · Laboratoire `ligne_transmission`

On appelle Zcharge l’impédance terminale et Z₀ l’impédance caractéristique, en ohms. Le coefficient Γ=(Zcharge−Z₀)/(Zcharge+Z₀) relie l’onde réfléchie à l’onde incidente au bout du câble. Γ=0 signifie adaptation; une tension uniforme n’est toutefois attendue que si les pertes sont faibles.

Avec V et I en amplitudes crêtes, la puissance active est P=Re(VI*)/2. Les équations locales donnent dP/dx=−(R|I|²+G|V|²)/2. Une bosse d’amplitude n’implique donc pas une création d’énergie : elle peut résulter d’une interférence.

## 33. Deux conditions initiales pour deux stockages

Sup · PTSI · Laboratoire `rlc_transitoire`

La maille contient une résistance R (Ω), une inductance L (H) et une capacité C (F). E est la tension de l’échelon (V); uC(t) est celle du condensateur et i(t) le courant (A).

Les relations i=CduC/dt et E=Ri+Ldi/dt+uC donnent LC uC″+RC uC′+uC=E. Le condensateur initialement déchargé impose uC(0)=0; l’absence de courant initial impose uC′(0)=0. Avec ω₀=1/√(LC) et ζ=R√(C/L)/2, les trois régimes correspondent à ζ<1, ζ=1 et ζ>1. L’absence d’oscillation ne signifie pas une charge instantanée.

## 34. Un bilan qui ne se limite pas au condensateur

Sup · énergie · Laboratoire `rlc_transitoire`

Les énergies stockées sont EC=CuC²/2 et EL=Li²/2, en joules. La puissance fournie par la source est Ei, en watts; la puissance dissipée est Ri².

La loi des mailles multipliée par i donne Ei=Ri²+d(EC+EL)/dt. Le travail de la source depuis t=0 est W=E∫i dt=E×C×uC, où E est la tension d’échelon et C la capacité. À l’établissement complet, uC=E et i=0 : la source a fourni CE², dont CE²/2 est stockée et CE²/2 dissipée. Ce résultat ne dépend pas de la valeur positive de R.

## 35. La phase révèle la nature du circuit

Sup · PTSI · Laboratoire `resonance_impedance`

U et I sont les valeurs efficaces complexes de tension et de courant. Avec une résistance R (Ω), une inductance L (H), une capacité C (F) et la pulsation ω (rad/s), Z=R+j(ωL−1/(ωC)) et I=U/Z.

En dessous de ω₀=1/√(LC), la partie imaginaire de Z est négative : le courant avance sur la tension. Au-dessus, il retarde. À ω₀, Z=R et Ieff=Ueff/R. La courbe temporelle compare u à Ri, deux tensions en volts : leur décalage représente celui de la tension et du courant.

## 36. Mesurer une largeur par la puissance

Spé · réinvestissement · Laboratoire `resonance_impedance`

On note P la puissance moyenne dans la résistance (W), Ieff le courant efficace (A) et f₀ la fréquence de résonance (Hz). P=RIeff² atteint son maximum Ueff²/R à f₀.

Aux fréquences f− et f+ de mi-puissance, Ieff=Imax/√2, donc |ωL−1/(ωC)|=R. Le calcul donne Δf=f+−f−=R/(2πL) et Q=f₀/Δf=ω₀L/R. Ces relations sont exactes pour ce RLC série. L’approximation f±≈f₀±Δf/2 demande Q grand.

## 37. Deux tensions donnent un courant

Sup · PTSI expérimental · Laboratoire `mesure_impedance`

Un résistor connu R₀ (Ω) précède le dipôle à mesurer. V₁ est la tension complexe en amont et V₂ la tension aux bornes du dipôle, en volts. Le courant dans R₀ est (V₁−V₂)/R₀ : Zmes=R₀V₂/(V₁−V₂).

La voie 2 possède une résistance Rentrée (Ω) et une capacité Centrée (F), donc Yvoie=1/Rentrée+jωCentrée. Zmes est le parallèle de cette voie et du dipôle. Si Yvoie est connue, Z=1/(1/Zmes−Yvoie). Réduire la perturbation par une sonde adaptée reste préférable à une correction numériquement mal conditionnée.

## 38. Une petite différence amplifie l’incertitude

Sup / spé · mesure · Laboratoire `mesure_impedance`

V₁ et V₂ sont les deux tensions complexes; leur différence complexe est D=V₁−V₂. L’incertitude-type relative de chaque lecture d’amplitude est ε, sans unité. La phase et R₀ sont supposés exacts et les deux lectures indépendantes.

Une propagation différentielle donne u(|Zmes|)/|Zmes|≈√2 ε |Re(V₁/D)|. Quand les deux voies sont proches, le courant déduit d’une différence est peu précis. Deux réponses de bande identiques H(f)=1/(1+jf/fb) se simplifient dans le rapport; leurs faibles amplitudes peuvent pourtant rendre la lecture difficile. Ce calcul ne décrit pas une erreur de phase ou une corrélation entre voies.

## 39. Choisir une paire conductrice

Spé · PSI conversion · Laboratoire `pont_graetz`

uAB est la tension alternative (V) entre les bornes A et B. Le courant iR (A) traverse une charge R (Ω), sous la tension positive uR (V). Chaque diode impose le seuil Vd (V) lorsqu’elle conduit.

Si uAB>2Vd, D₁ et D₄ conduisent et uR=uAB−2Vd. Si uAB<−2Vd, D₂ et D₃ conduisent et uR=−uAB−2Vd. Entre les seuils, la charge résistive ne reçoit aucun courant. Le résultat est uR=max(|uAB|−2Vd,0). Une hypothèse de conduction doit toujours être vérifiée par le sens du courant et la polarité des diodes bloquées.

## 40. Deux montages, deux tensions de référence

Sup / spé · réinvestissement · Laboratoire `pont_graetz`

E est la crête alternative (V) et f sa fréquence (Hz). Pour le pont idéal, uR=E|sin(2πft)|, sa moyenne vaut 2E/π et sa valeur efficace E/√2. L’ondulation a pour fréquence 2f.

Le montage à point milieu reçoit deux tensions opposées, chacune de crête E. Une seule diode conduit à la fois : avec un seuil Vd, uR=max(E|sin(2πft)|−Vd,0). La comparaison conserve ici la crête par demi-enroulement, pas la tension bout à bout du transformateur. Dans le pont, Psource=Pcharge+2Vd⟨iR⟩; avec des diodes idéales, les pertes du pont sont nulles.

## 41. Deux condensateurs, une somme de tensions

Sup / spé · prolongement · Laboratoire `doubleur_tension`

Dans le doubleur de Delon, le point milieu M des condensateurs est relié à un pôle de la source alternative. On définit u₁=Vhaut−VM et u₂=VM−Vbas, en volts. La sortie entre les extrémités vaut u₁+u₂.

Pour une crête alternative E (V) et un seuil de diode Vd (V), l’alternance positive recharge le condensateur supérieur; l’alternance négative recharge l’inférieur. À vide et après établissement, chacun atteint E−Vd, soit une sortie 2(E−Vd). Un doubleur ne multiplie donc pas toute tension instantanée par deux; il accumule deux charges sur des alternances opposées.

## 42. Une diode bloquée ne conserve pas toujours la charge

Spé · PSI, application · Laboratoire `doubleur_tension`

La charge résistive R (Ω) reçoit iR=(u₁+u₂)/R (A). Les capacités C₁ et C₂ sont en farads, et les courants des diodes iD₁ et iD₂ en ampères.

Les nœuds donnent C₁u₁′=iD₁−iR et C₂u₂′=iD₂−iR. Si une diode est bloquée, son condensateur conserve sa charge uniquement à vide. Sous charge, il se décharge. Une capacité plus petite présente, pour un même débit, une pente plus forte. Le calcul utilise une résolution implicite des deux tensions et vérifie, à chaque pas, courant positif dans chaque diode conductrice et tension inverse dans chaque diode bloquée.

## 43. Une seule équation de nœud, deux états

Sup / spé · RC et diode · Laboratoire `diode_rc`

La sortie uC (V) alimente une résistance R (Ω) et une capacité C (F) en parallèle. La diode fournit le courant iD (A). La source impose usource (V), avec une résistance série Rs (Ω) et un seuil Vd (V).

La loi des nœuds est C uC′=iD−uC/R. Si la diode est bloquée, iD=0 et la tension décroît exponentiellement. Si elle conduit, iD=(usource−Vd−uC)/Rs≥0. Il faut aussi vérifier que la diode bloquée n’est pas polarisée dans le sens passant. Le modèle ne remplace donc pas le circuit par une impédance unique valable sur toute une période.

## 44. Le maximum de source ne fixe pas le blocage

Spé · commutation · Laboratoire `diode_rc`

Pour étudier la limite idéale, on note E la crête de source, ω sa pulsation et τ=RC le temps de décharge. Avec une source de tension idéale et une diode sans seuil, la conduction impose uC=E sin(ωt).

Le courant demandé à la diode serait iD=CEω cos(ωt)+E sin(ωt)/R. Il reste positif au maximum de source, où cos(ωt)=0. Le blocage intervient lorsque ce courant devient nul, en général après ce maximum : tan(ωt)=−ωRC sur la branche descendante positive. La reprise dépend de la rencontre de la source montante avec la tension résiduelle du condensateur. Une source de courant imposé demanderait un autre circuit et d’autres équations.

## 45. Le rapport de spires porte sur les bobinages

Spé · PSI; contexte PT/SI · Laboratoire `triphase_transformateur`

U₁ et U₂₀ sont les tensions composées efficaces primaire et secondaire à vide (V). Le rapport de spires m=N₂/N₁ est sans unité. On définit k=√3 pour une étoile et k=1 pour un triangle.

Un enroulement primaire reçoit U₁/k₁; l’enroulement secondaire associé fournit mU₁/k₁. La tension composée secondaire vaut donc U₂₀=mU₁k₂/k₁. Pour un couplage D→Y, le rapport de tensions de ligne est √3m. Le neutre des tensions simples est réel en étoile ou fictif en triangle. Les décalages de 30° dépendent aussi de la polarité des enroulements et du groupe horaire.

## 46. Calculer la puissance avec des grandeurs de ligne

Spé · conversion · Laboratoire `triphase_transformateur`

U₂ est la tension composée efficace (V), I₂ le courant de ligne efficace (A) et cosφ le facteur de puissance d’une charge équilibrée sinusoïdale. Sa puissance utile vaut Pu=√3U₂I₂cosφ.

La résistance Rs (Ω) est ramenée à une phase étoile secondaire : Pcuivre=3RsI₂². Avec les pertes constantes P₀ (W), η=Pu/(Pu+Pcuivre+P₀). Le courant de référence Iref=λSref/(√3U₂₀) définit la charge par Zcharge=U₂₀(cosφ+j sinφ)/(√3Iref). Le calcul sous charge utilise I₂=(U₂₀/√3)/(Rs+Zcharge). Le courant réel baisse donc quand la résistance série devient importante. Une perte fixe pénalise surtout les faibles charges; les pertes cuivre croissent comme I₂².

## 47. Intégrer le signal réellement commandé

Sup / spé · valeurs efficaces · Laboratoire `onduleur_spectre`

E est la tension du bus continu (V), T la période (s) et δ le retard rapporté à T. La tension v est +E sur [δT,T/2[, −E sur [(1/2+δ)T,T[, et nulle ailleurs.

Sa durée non nulle est (1−2δ)T : Veff²=E²(1−2δ). Pour δ=1/4 et E=175 V, Veff=E/√2≈123,74 V. En pleine onde, Veff=E=175 V. Ces résultats ne dépendent pas d’une troncature du spectre. Les valeurs aux instants de commutation, isolés, ne changent pas les intégrales.

## 48. Le fondamental et toutes les autres raies

Spé · Fourier · Laboratoire `onduleur_spectre`

Pour un harmonique de rang n, An est son amplitude crête (V), et Vn,eff=An/√2 sa valeur efficace. La symétrie v(t+T/2)=−v(t) annule les rangs pairs. Pour n impair, An=4E|cos(nπδ)|/(nπ).

Le fondamental est donc A₁=4Ecos(πδ)/π. Le THD total vaut √(Veff²−V₁eff²)/V₁eff, par Parseval. À δ=0 et δ=1/4, ce rapport vaut dans les deux cas √(π²/8−1)≈48,34 %. Le décalage T/4 diminue les amplitudes, mais n’annule aucun rang impair. Le THD calculé avec seulement les raies affichées est plus petit; la reconstruction tronquée présente des oscillations près des sauts.

## 49. La roue libre est une partie du circuit

Spé · PSI §5.4 · Laboratoire `hacheur_mcc`

Une source continue E (V) alimente une machine représentée par R (Ω), L (H) et la force contre-électromotrice Eₘ (V). Le courant i (A) est positif en fonctionnement moteur. L’interrupteur est fermé pendant αT, où T est la période et α le rapport cyclique.

Fermé : L i′+Ri+Eₘ=E. Ouvert, si la diode de roue libre conduit : L i′+Ri+Eₘ=0. Le courant reste continu et décroît. Quand il atteint zéro, la diode se bloque; le modèle à un quadrant interdit de poursuivre vers un courant négatif. La tension de la machine vaut alors Eₘ jusqu’à la prochaine fermeture.

## 50. Moyennes et bilan du moteur

Spé · PSI conversion · Laboratoire `hacheur_mcc`

En régime périodique établi, ⟨di/dt⟩=0. Si le courant reste strictement positif pendant l’ouverture, la tension moteur u (V) alterne entre E et zéro : ⟨u⟩=αE et ⟨i⟩=(αE−Eₘ)/R.

En conduction discontinue, l’état à courant nul ajoute un intervalle à u=Eₘ. Il faut calculer cet intervalle avant les moyennes. Le bilan de puissance est ⟨E iS⟩=R⟨i²⟩+Eₘ⟨i⟩, où iS est le courant de source. La bobine a une variation d’énergie moyenne nulle. Le terme Eₘ⟨i⟩ représente la conversion électromécanique; R⟨i⟩² sous-estime les pertes cuivre dès que le courant ondule.

## 51. Utiliser des valeurs efficaces complexes

Spé · PSI §5.1 · Laboratoire `puissances_compensation`

U est la tension efficace complexe de référence (V), réelle ici. I est le courant efficace complexe reçu par la charge (A). La puissance complexe est U I*=P+jQ, en VA : P est sa partie active en watts, Q sa partie réactive en vars.

La puissance apparente est S=U|I|, et le facteur de puissance est P/S. Pour un courant sinusoïdal de retard φ, P=UIeff cosφ et Q=UIeff sinφ. La puissance instantanée u(t)i(t) oscille à deux fois la fréquence de source autour de P. En régime déformé, le facteur de puissance reste P/(UeffIeff), mais ne se réduit plus au seul cosinus d’un déphasage.

## 52. Trouver la bonne capacité, puis s’arrêter

Spé · bilan · Laboratoire `puissances_compensation`

La charge série possède R (Ω) et L (H), à la pulsation ω (rad/s). Sous U (V efficace), son courant est Icharge=U/(R+jωL). Une capacité C (F) en parallèle fournit IC=jωCU.

Le courant de ligne est Icharge+IC. La charge absorbe Qcharge=U²ωL/[R²+(ωL)²], tandis que le condensateur a Qc=−ωCU². La compensation parfaite exige Copt=L/[R²+(ωL)²]. Elle minimise le courant de ligne à puissance active inchangée. Pour C>Copt, la puissance réactive devient négative et le courant augmente de nouveau : une compensation excessive n’améliore pas le bilan.

## 53. De l’ALI à un pôle au gain bouclé

Spé — physique PSI/PT · Laboratoire `ali_gain_bande`

Un amplificateur linéaire intégré, ou ALI, compare ses tensions d’entrée v₊ et v₋, en volts. Sa tension différentielle est ε = v₊ − v₋ ; sa sortie est vₛ. Le gain différentiel statique A₀ est sans unité. Le modèle linéaire possède une fréquence de pôle fₚ, en hertz.

Le symbole s représente une dérivation temporelle dans les équations linéaires à conditions initiales nulles. Pour un régime sinusoïdal de fréquence f, on remplace s par jω, avec j² = −1 et ω = 2πf, en rad/s.

A(s) = A₀/(1 + s/ωₚ), avec ωₚ = 2πfₚ et fₜ = A₀fₚ.

Dans un montage non inverseur, la borne positive reçoit l’entrée vₑ et la borne négative reçoit βvₛ. La fraction β est sans unité. Le gain demandé au modèle idéal est G = 1/β.

H(s) = A(s)/(1 + βA(s)) = G₀/(1 + s/ω_c), G₀ = A₀/(1 + βA₀), f_c = fₚ(1 + βA₀), ω_c = 2πf_c.

Le pôle bouclé est stable : une perturbation libre décroît exponentiellement. Le produit G₀f_c vaut exactement fₜ dans ce modèle. Augmenter le gain réduit donc la bande. La conservation du produit gain–bande est une capacité de physique PSI/PT.

## 54. Reconnaître les limites d’une amplification

Spé — physique PSI/PT ; décalage au-delà · Laboratoire `ali_gain_bande`

La tension sinusoïdale d’entrée a une amplitude crête E, en volts, et une fréquence f, en hertz. L’amplitude crête linéaire de sortie est S = E|H(j2πf)|. La tension limite Vₛₐₜ est la valeur absolue d’un rail de sortie ; Iₘₐₓ est le courant maximal, en ampères ; Rₗ est la résistance de charge, en ohms.

S ≤ Vₛₐₜ ; S/Rₗ ≤ Iₘₐₓ ; 2πfS ≤ SR.

La vitesse de balayage SR est la pente maximale de sortie, en V/s, souvent annoncée en V/µs. Une sinusoïde qui exige une pente trop forte se déforme. Une petite charge peut provoquer une limitation de courant avant d’atteindre les rails de tension.

La simulation conserve une tension de sortie comme état. Le modèle à un pôle fournit sa dérivée ; la vitesse de balayage borne cette dérivée, puis les rails arrêtent l’excursion. Le modèle reste causal : la sortie dépend de son état précédent. Le diagramme de Bode ne décrit que le régime linéaire.

Le réglage Vₒₛ, en volts, ajoute un décalage à l’entrée différentielle. Son effet statique est G₀Vₒₛ avant saturation. Ce prolongement est fourni pour explorer une limite du modèle ; la tension de décalage et les courants de polarisation sont explicitement exclus du programme de physique PSI/PT.

## 55. Pourquoi un filtre charge le précédent

Sup — physique PTSI ; approfondissement en spé · Laboratoire `suiveur_cascade`

Deux cellules passe-bas possèdent des résistances R₁ et R₂, en ohms, et des condensateurs C₁ et C₂, en farads. Chaque résistance est en série avec le signal et chaque condensateur est relié à la masse. L’entrée est vₑ, la sortie finale vₛ, en volts. On note H = vₛ/vₑ en régime sinusoïdal et s = j2πf, où f est la fréquence en hertz et j² = −1.

Lorsque les cellules sont directement reliées, la seconde absorbe un courant au nœud de la première. Sa tension n’est donc plus celle de la première cellule étudiée seule. Les lois des nœuds donnent :

H(s) = 1/[1 + s(R₁C₁ + R₂C₂ + R₁C₂) + s²R₁R₂C₁C₂].

Le terme R₁C₂ traduit cette charge mutuelle. Le produit des deux fonctions de transfert isolées oublie ce terme et ne convient pas à ce branchement. En PTSI, le programme demande d’expliquer l’intérêt d’une forte impédance d’entrée et d’une faible impédance de sortie lors d’une association de filtres.

## 56. Le suiveur transmet une tension et fournit le courant

Sup — application accompagnée ; spé — ALI idéal · Laboratoire `suiveur_cascade`

Le suiveur reçoit la tension de la première cellule à sa borne positive. Sa sortie est directement reliée à sa borne négative. Pour un ALI idéal en régime linéaire stable, v₊ = v₋ et les courants d’entrée sont nuls : sa tension de sortie égale sa tension d’entrée.

Avec R₁, R₂ en ohms, C₁, C₂ en farads et s = j2πf, les cellules deviennent indépendantes :

H(s) = 1/[(1 + sR₁C₁)(1 + sR₂C₂)].

Le suiveur ne crée aucun gain de tension ; il prélève idéalement une tension sans courant et fournit le courant demandé par l’étage suivant, grâce à son alimentation. Un suiveur réel conserve des limites de bande, de tension et de courant.

Une expérience statique complémentaire emploie un capteur de tension à vide V, en volts, de résistance interne Rₛ, en ohms, et un appareil de lecture de résistance Rₗ, en ohms. La lecture directe vaut VRₗ/(Rₛ + Rₗ). Un suiveur idéal transmet V ; il doit toutefois pouvoir fournir V/Rₗ à la charge.

## 57. Établir une somme pondérée par la loi des nœuds

Sup — lois des circuits ; spé — ALI idéal · Laboratoire `sommateur_inverseur`

Les tensions vₑ₁ et vₑ₂, en volts, atteignent la borne inverseuse d’un ALI par les résistances R₁ et R₂, en ohms. La résistance Rf, en ohms, relie cette borne à la sortie vₛ. La borne positive est reliée à la masse.

En régime linéaire idéal, les deux bornes sont au même potentiel et aucun courant ne pénètre dans l’ALI. La borne inverseuse est donc au potentiel nul ; elle n’est pas reliée matériellement à la masse.

vₑ₁/R₁ + vₑ₂/R₂ + vₛ/Rf = 0 ; vₛ = −Rf(vₑ₁/R₁ + vₑ₂/R₂).

Les coefficients −Rf/R₁ et −Rf/R₂ sont les poids sans unité. Une petite résistance d’entrée donne un poids plus grand. Le signe négatif vient de la contre-réaction sur la borne inverseuse. Chaque source voit ici sa propre résistance d’entrée.

## 58. Superposition et domaine linéaire du sommateur

Sup — signaux périodiques ; spé — saturation · Laboratoire `sommateur_inverseur`

La première entrée est E₁ sin(2πft) et la seconde E₂ sin(4πft + φ). Les amplitudes E₁ et E₂ sont des valeurs crêtes, en volts ; f est une fréquence en hertz ; t est le temps en secondes ; φ est une phase en radians. Le montage linéaire additionne les deux contributions sans créer de nouvelle fréquence.

Les résistances R₁, R₂ et Rf sont en ohms. Une borne suffisante de la tension de sortie est :

|vₛ| ≤ Rf(E₁/R₁ + E₂/R₂).

Cette borne est une majoration : les deux sinusoïdes n’atteignent pas nécessairement leurs extrema ensemble. Si elle est inférieure au rail Vₛₐₜ, en volts, l’excursion en tension est possible dans le modèle idéal. Si elle le dépasse, il faut examiner la courbe.

La saturation rend l’opération non linéaire et produit des harmoniques supplémentaires. Le tracé de ce laboratoire limite la somme instantanément aux rails pour montrer cet effet ; il ne simule pas la réponse dynamique d’un ALI réel.

## 59. Intégrer ou dériver : vérifier le signe et la condition initiale

Sup — filtrage ; spé — intégrateur à ALI · Laboratoire `integrateur_derivateur`

La résistance R est en ohms, la capacité C en farads ; l’entrée vₑ et la sortie vₛ sont en volts. Dans un intégrateur inverseur idéal, R est à l’entrée et C en rétroaction. Dans un dérivateur inverseur idéal, C est à l’entrée et R en rétroaction. Le produit RC est un temps, en secondes.

Intégrateur : dvₛ/dt = −vₑ/(RC). Dérivateur : vₛ = −RC dvₑ/dt.

Pour l’intégrateur, il faut donner vₛ(0) avant de calculer la sortie. Le laboratoire choisit vₛ(0) = 0. Avec vₑ(t) = E sin(ωt), E en volts et ω = 2πf en rad/s, la sortie vaut E[cos(ωt) − 1]/(ωRC). La constante −E/(ωRC) impose le départ à zéro.

Un dérivateur donne −ERCω cos(ωt). Son gain croît avec la fréquence ; un intégrateur idéal a au contraire un gain 1/(RCω). Ces modèles n’ont ni rails ni limitation de pente : leurs grandes tensions signalent que le modèle doit être complété.

## 60. Le dérivateur amélioré évite un gain illimité

Spé — analyse de montage ; technique accompagnée · Laboratoire `integrateur_derivateur`

La branche d’entrée contient le condensateur C, en farads, en série avec R, en ohms. La rétroaction contient R′, en ohms, en parallèle avec C′, en farads. La borne positive est à la masse. Les tensions vₑ et vₛ sont en volts ; H est leur rapport complexe. En régime sinusoïdal, s = jω, avec ω = 2πf en rad/s et j² = −1.

Zₑ = R + 1/(sC), Zf = R′/(1 + sR′C′), H = −Zf/Zₑ = −R′Cs/[(1 + RCs)(1 + R′C′s)].

Le signe est fixé par le montage inverseur. Si ωRC et ωR′C′ sont petits, H ≈ −jωR′C : la sortie approche −R′C dvₑ/dt. Les fréquences de pôle sont 1/(2πRC) et 1/(2πR′C′), en hertz.

À très haute fréquence, le gain décroît comme 1/ω. La résistance d’entrée et la capacité de rétroaction évitent l’amplification illimitée du dérivateur idéal. Cela aide à réduire la sensibilité aux variations rapides, mais ne remplace pas l’étude de la bande de l’ALI réel.

## 61. Retrouver les deux seuils du Schmitt inverseur

Spé — physique PSI/PT · Laboratoire `schmitt_trigger`

La tension d’entrée vₑ, en volts, est appliquée à la borne négative de l’ALI. La résistance R₁ relie la sortie à la borne positive ; R₂ relie cette borne à la masse. Les résistances sont en ohms. Les sorties saturées valent ±Vₛₐₜ, en volts. La fraction β = R₂/(R₁ + R₂) est sans unité.

v₊ = βvₛ, ε = v₊ − vₑ.

Une sortie positive exige ε > 0. Elle subsiste donc tant que vₑ < βVₛₐₜ ; en montée, elle bascule vers −Vₛₐₜ au seuil +βVₛₐₜ. Une sortie négative exige ε < 0 ; en descente, elle bascule vers +Vₛₐₜ au seuil −βVₛₐₜ.

La rétroaction positive entretient la saturation au lieu d’établir une égalité des deux entrées. On ne peut donc pas imposer v₊ = v₋ pour ce montage. Le cycle à deux seuils est une capacité de physique PSI/PT.

## 62. Mémoire et protection contre de petits franchissements

Spé — physique PSI/PT · Laboratoire `schmitt_trigger`

Le Schmitt possède un seuil haut Uₕ et un seuil bas Uᵦ, en volts. Ici Uₕ = βVₛₐₜ et Uᵦ = −βVₛₐₜ, avec β une fraction sans unité et Vₛₐₜ le niveau positif de sortie. La largeur Uₕ − Uᵦ vaut 2βVₛₐₜ.

Entre les seuils, deux états de sortie sont possibles. La valeur de l’entrée ne suffit pas : il faut son histoire. On décrit le circuit par une tension d’entrée et un état mémorisé.

Une rampe triangulaire de crête E, en volts, et de fréquence f, en hertz, est parcourue dans les deux sens. Le réglage de bruit ajoute une sinusoïde de crête N, en volts, à la fréquence 23f. Si cette perturbation ne permet pas d’atteindre le seuil opposé après un basculement, elle ne provoque pas de retour immédiat.

Le cycle entrée–sortie se parcourt dans le temps. Une courbe horizontale lorsque E reste sous les seuils est un résultat normal : le circuit conserve l’état initial choisi.

## 63. Charge exponentielle entre deux seuils

Spé — physique PSI/PT, oscillateur de relaxation · Laboratoire `astable`

Le condensateur de capacité C, en farads, reçoit la sortie vₛ à travers R₁, en ohms. Sa tension v_C est appliquée à la borne négative. La borne positive reçoit la commande continue Vₑ à travers R₂ et la sortie à travers R₃. Toutes les tensions sont en volts et toutes les résistances en ohms.

On pose τ = R₁C, en secondes, β = R₂/(R₂ + R₃), sans unité, et h = (1 − β)Vₑ, en volts. Les deux seuils sont L = h − βVₛₐₜ et U = h + βVₛₐₜ. Vₛₐₜ est le niveau positif de saturation.

τ dv_C/dt + v_C = vₛ ; v_C(t) = vₛ + [v_C(0) − vₛ] exp(−t/τ) lorsque vₛ reste constant.

À sortie positive, le condensateur monte du seuil L vers U. Au seuil U, la sortie devient négative ; le condensateur descend alors vers L. On relie ainsi la loi du condensateur aux conditions de basculement du comparateur.

## 64. Période, rapport cyclique et arrêt des oscillations

Spé — physique PSI/PT · Laboratoire `astable`

Les seuils L et U, en volts, sont définis par le diviseur de rétroaction. La sortie prend ±Vₛₐₜ, en volts ; τ = R₁C est la constante de temps en secondes. Les durées t₊ et t₋ sont celles des sorties positive et négative.

t₊ = τ ln[(Vₛₐₜ − L)/(Vₛₐₜ − U)] ; t₋ = τ ln[(U + Vₛₐₜ)/(L + Vₛₐₜ)].

La période T vaut t₊ + t₋, la fréquence vaut 1/T et la fraction du temps au niveau positif vaut t₊/T. À commande nulle, h = 0 : les deux durées sont égales.

T = 2R₁C ln[(1 + β)/(1 − β)] pour Vₑ = 0.

Pour des basculements en temps fini, il faut −Vₛₐₜ < L < U < Vₛₐₜ. Dans ce montage cela équivaut à |Vₑ| < Vₛₐₜ. Au seuil d’arrêt, une cible du condensateur et un seuil coïncident : l’approche est asymptotique et la période tend vers l’infini.

## 65. Phase nulle et gain critique du pont de Wien

Spé — physique PSI/PT, oscillateur quasi sinusoïdal · Laboratoire `wien`

Le pont possède une branche série R₁–C₁ et une branche parallèle R₂–C₂ reliée à la masse. Les résistances sont en ohms et les capacités en farads. La tension de sortie de l’amplificateur est v₂ ; le pont transmet v₁ à son entrée positive. Le rapport B = v₁/v₂ est sans unité. En régime sinusoïdal, s = jω avec ω = 2πf en rad/s et j² = −1.

B(s) = R₂C₁s/[1 + (R₁C₁ + R₂C₂ + R₂C₁)s + R₁R₂C₁C₂s²].

La phase du pont est nulle à ω₀ = 1/√(R₁R₂C₁C₂). Son gain y vaut 1/Gcrit, avec Gcrit = 1 + R₁/R₂ + C₂/C₁. Un amplificateur non inverseur possède un gain G = 1 + R/R₃ ; R et R₃ sont ses résistances de contre-réaction, en ohms.

Au seuil sinusoïdal : G = Gcrit, soit R/R₃ = R₁/R₂ + C₂/C₁.

Pour deux branches identiques, la fréquence vaut 1/(2πRC) et le gain critique vaut 3. La simulation permet aussi d’explorer un pont dissymétrique.

## 66. Démarrage et rôle des non-linéarités

Spé — physique PSI/PT ; enveloppe accompagnée · Laboratoire `wien`

On note a = R₁C₁ + R₂C₂ + R₂C₁, en secondes, b = R₂C₁, en secondes, et d = R₁R₂C₁C₂, en secondes carrées. La tension de sortie vₛ est en volts ; G est le gain sans unité de l’amplificateur. Le circuit linéaire bouclé vérifie :

d vₛ″ + (a − Gb)vₛ′ + vₛ = 0.

Si G est inférieur à a/b, les perturbations s’éteignent. Si G est supérieur, le coefficient d’amortissement est négatif et elles croissent. Au seuil, le modèle linéaire conserve une oscillation, mais ne sélectionne pas une amplitude.

Le tracé emploie une amplitude A, en volts, avec une petite valeur initiale, et une fréquence fixée à ω₀/(2π). Près du seuil, son taux de croissance approché est γ = (Gb − a)/(2d), en s⁻¹. Pour illustrer une stabilisation, on fournit le modèle d’enveloppe A′ = γA(1 − A²/Vlim²) lorsque γ est positif. Vlim est une amplitude conventionnelle en volts.

Ce modèle qualitatif respecte le démarrage et la limitation, mais ne représente pas le mécanisme précis d’une lampe, de diodes ou d’un ALI saturé. Une réalisation réelle fixe son amplitude par sa propre non-linéarité et produit éventuellement des harmoniques.

## 67. Compenser le seuil de diode par la contre-réaction

Spé — application d’ALI ; montage accompagné · Laboratoire `redresseur_precision`

L’entrée e, en volts, rejoint la borne inverseuse par une résistance R₁. Deux branches de rétroaction comportent R₂ et R₃ ainsi que deux diodes opposées. Les trois résistances, en ohms, sont égales. Les tensions vₛ₁ et vₛ₂ sont les sorties des deux branches ; la tension utile est leur différence vₛ₂ − vₛ₁.

Une seule diode conduit à chaque alternance. Lorsque la contre-réaction peut établir le régime linéaire, la borne inverseuse reste au potentiel nul. Pour e > 0, la branche correspondante donne vₛ₁ = −e et vₛ₂ = 0. Pour e < 0, l’autre donne vₛ₁ = 0 et vₛ₂ = −e.

vₛ₂ − vₛ₁ = |e|.

Le seuil Vᴅ, en volts, est compensé par une excursion supplémentaire de la sortie interne de l’ALI. Le seuil subsiste dans cette tension interne, mais pas dans la différence utile tant que le régime linéaire reste possible.

## 68. Petits signaux et marge d’alimentation du redresseur

Sup — diodes ; spé — limites d’ALI · Laboratoire `redresseur_precision`

Une sinusoïde d’entrée possède une amplitude crête E, en volts. Chaque diode est représentée par un seuil constant Vᴅ, en volts, sans résistance dynamique. Un pont passif traverse deux diodes et fournit max(|e| − 2Vᴅ, 0) dans ce modèle.

Le redresseur à ALI demande une tension interne de valeur absolue |e| + Vᴅ. Avec des rails symétriques ±Vₛₐₜ, sa marge s’écrit :

E + Vᴅ ≤ Vₛₐₜ.

Une entrée de 0,2 V crête peut donc être redressée par le montage de précision avec des diodes de seuil 0,6 V ; le pont passif ne conduit jamais. Une entrée trop grande ne peut plus être compensée.

Ce laboratoire est quasi statique. Le passage entre les diodes force un changement rapide de la tension interne de l’ALI. Dans une expérience réelle, sa vitesse de balayage, sa bande et sa récupération peuvent créer une erreur de passage par zéro, même si l’alimentation est suffisante.

## 69. Des lois des nœuds au passe-bande à trois ALI

Spé — filtre actif ; calcul accompagné du montage · Laboratoire `filtre_etat`

Les résistances R₁ à R₆ sont en ohms et les deux condensateurs ont la même capacité C, en farads. La tension d’entrée est vₑ. Le premier ALI fournit vₛ₁, le second fournit la sortie vₛ, le troisième fournit vₛ₂ ; toutes ces tensions sont en volts.

vₛ = −(R₅/R₄)vₛ₁ = −R₆C dvₛ₂/dt ; (R₂/R₁)vₑ + (R₂/R₃)vₛ₂ = −vₛ₁ − R₂C dvₛ₁/dt.

En régime sinusoïdal de pulsation ω = 2πf, en rad/s, le nombre j vérifie j² = −1. On définit le gain central H₀, sans unité, la pulsation centrale ω₀, en rad/s, et le facteur de qualité Q, sans unité.

H₀ = R₂R₅/(R₁R₄), ω₀ = √[R₅/(R₃R₄R₆)]/C, Q = R₂Cω₀ ; H(jω) = H₀/[1 + jQ(ω/ω₀ − ω₀/ω)].

Le filtre atténue les très basses et les très hautes fréquences. Son gain maximal est H₀ à ω₀. Les bornes à −3 dB, ω₁ et ω₂, sont les pulsations où le gain vaut H₀/√2. Leur différence Δω est exactement 1/(R₂C), et ω₁ω₂ = ω₀².

## 70. Filtrer chaque harmonique d’un créneau

Sup — spectre fourni ; spé — filtrage actif · Laboratoire `filtre_etat`

Le créneau impair prend +E pendant la première demi-période et −E pendant la suivante. E est son amplitude crête, en volts ; Tₑ est sa période, en secondes ; sa pulsation fondamentale vaut ωₑ = 2π/Tₑ, en rad/s. On note k un entier positif.

vₑ(t) = Σₖ Aₖ sin(kωₑt) + Bₖ cos(kωₑt) ; Aₖ = 4E/(πk) pour k impair, Aₖ = 0 pour k pair, Bₖ = 0.

La parité impaire annule les coefficients cosinus ; l’alternance entre les deux demi-périodes annule les harmoniques paires. Le calcul ne garde qu’un nombre choisi de termes impairs, avec leurs coefficients exacts.

Si H(jkωₑ) possède un module hₖ et une phase φₖ, la contribution de sortie vaut Aₖhₖ sin(kωₑt + φₖ). On ne peut pas multiplier tout le créneau par un gain unique.

Une approximation simple garde seulement les harmoniques dont la pulsation est entre les bornes ω₁ et ω₂ de la bande à −3 dB. Le filtre réel du modèle laisse aussi passer les autres, avec atténuation : la simulation compare la somme complète calculée et cette approximation. Elle affiche également les deux états vₛ₁ et vₛ₂ ; les vérifier permet de détecter un ALI qui saturerait en pratique.

## 71. Fixer le point de repos d’un NPN

Au-delà — physique PSI/PT ; modèle fourni · Laboratoire `transistor_polarisation`

Ce prolongement étudie un transistor NPN amplificateur. Il ne correspond pas à la seule fonction d’interrupteur d’une chaîne de puissance. Le collecteur est relié à l’alimentation Vcc par Rc ; l’émetteur est relié à la masse par Re. La base reçoit un pont : Rb₁ vers la masse et Rb₂ vers l’alimentation. Les résistances sont en ohms et les tensions en volts.

Le gain en courant β est sans unité. Le modèle fourni fixe la tension base–émetteur à Vbe = 0,7 V lorsqu’elle conduit. Le pont de base équivaut à une source Vth = Vcc Rb₁/(Rb₁ + Rb₂), de résistance Rth = Rb₁Rb₂/(Rb₁ + Rb₂).

Ib = (Vth − Vbe)/[Rth + (β + 1)Re] ; Ic = βIb ; Ve = (β + 1)IbRe ; Vc = Vcc − RcIc.

Les courants Ib et Ic sont en ampères, Ve et Vc en volts. Ces formules supposent le régime actif. Si Vth ne peut établir la jonction, le transistor est bloqué. Si Vc − Ve descend sous la valeur fournie Vce,sat = 0,2 V, il est saturé : Ic = βIb cesse d’être valable. On résout alors les courants avec les deux tensions de jonction imposées.

## 72. Amplifier une petite variation autour du repos

Au-delà — modèle petit signal accompagné · Laboratoire `transistor_polarisation`

Le transistor doit être en régime actif au repos. Le courant de repos Ic, en ampères, fixe la transconductance gm = Ic/Uₜ, en siemens. On fournit Uₜ = 25,85 mV. Le gain en courant β, sans unité, donne la résistance d’entrée interne rπ = β/gm, en ohms.

La résistance d’émetteur Re est éventuellement découplée par Ce, en farads. Le générateur de petite tension e possède une résistance Rg ; un condensateur C₁ le relie à la base. La charge alternative Rₗ est couplée sans modifier le repos. Toutes les résistances sont en ohms.

Pour s = j2πf, avec f en hertz et j² = −1, l’impédance d’émetteur est Ze = Re/(1 + sReCe) si Ce est connecté, et Ze = Re sinon. L’entrée du transistor vaut rπ + (β + 1)Ze ; elle est en parallèle avec la résistance du pont de base.

Sans atténuation d’entrée : H = −β(Rc ∥ Rₗ)/[rπ + (β + 1)Ze].

Le symbole ∥ désigne une association parallèle. Le signe négatif traduit l’inversion à l’émetteur commun. Un découplage efficace augmente le gain, mais réduit l’amplitude d’entrée admissible. Le modèle ignore les capacités internes et l’effet Early : il ne prédit pas le comportement à haute fréquence. Hors régime actif, le calcul petit signal est désactivé.
