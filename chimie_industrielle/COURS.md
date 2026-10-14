# Chimie pour l’industrie — 48 leçons

Recueil de A. R., fiches C6–C8, pages 545–570. Les applications relient thermochimie, cinétique et électrochimie. Les paramètres didactiques et les limites sont annoncés dans chaque TP.

## 01. Hess : assembler des formations pour calculer une combustion

Sup / spé — thermochimie · Laboratoire `hess_combustion`

Une enthalpie de formation ΔfH° correspond à une mole d’espèce formée à partir des éléments dans leurs états standard. Pour chaque espèce, préciser la phase. Les éléments dans leur état de référence ont ΔfH°=0.

ΔrH°=ΣᵢνᵢΔfHᵢ°.

Pour CH₄+2O₂→CO₂+2H₂O(g), le calcul donne −802,292 kJ par mole de CH₄ avec les données arrondies du TP. Le signe négatif désigne une réaction exothermique. Le cycle de Hess relie les mêmes états par deux chemins.

## 02. Condensation et chaleur utile

Sup / spé — bilan énergétique · Laboratoire `hess_combustion`

Le PCI conserve l’eau des produits à l’état vapeur ; le PCS la considère liquide. La différence est l’enthalpie de condensation de l’eau produite. Dans le TP, une mole d’eau apporte environ 44,004 kJ supplémentaires si elle condense à 298 K.

qdisponible=PCI+f(PCS−PCI) ; qutile=r qdisponible.

Ces énergies sont en MJ·kg⁻¹. Un combustible peut ne produire aucun CO₂ dans sa réaction d’usage tout en ayant des émissions en amont. Le TP compte uniquement les produits de la combustion.

## 03. Construire un chemin thermochimique

Sup / spé — premier principe · Laboratoire `temperature_adiabatique`

La réaction initiale contient 1 mol de NO et 0,5 mol de O₂. À l’avancement ξ, les quantités sont 1−ξ, (1−ξ)/2 et ξ pour NO, O₂ et NO₂. L’inerte reste inchangé.

On peut faire réagir à Tᵢ, puis chauffer les produits jusqu’à T. Avec des Cp constants et une fraction de chaleur cédée f, le bilan à pression constante donne :

Cp,total(ξ)(T−Tᵢ)=−(1−f)ξΔrH°(Tᵢ).

## 04. Kirchhoff et validité du modèle

Spé — thermochimie · Laboratoire `temperature_adiabatique`

Les données sont Cp(NO)=Cp(O₂)=29 et Cp(NO₂)=36 J·mol⁻¹·K⁻¹. Ainsi ΔrCp°=−7,5 J·mol⁻¹·K⁻¹ et ΔrH°(Tᵢ)=ΔrH°(298 K)+ΔrCp°(Tᵢ−298 K).

Le TP calibre ΔrH°(298 K) à partir du bilan expérimental : une conversion totale, Tᵢ=298 K, T=400 K et f=0,93. Lorsque le modèle prédit des températures très élevées, la dépendance des Cp et la dissociation des produits doivent être réintroduites.

## 05. Le quotient réactionnel contient les pressions partielles

Sup / spé — équilibre · Laboratoire `haber_bosch`

Les quantités d’équilibre valent 1−ξ, 3(1−ξ) et 2ξ. Le total, avec nᵢ moles d’inerte, est 4−2ξ+nᵢ. Une activité gazeuse idéale est aⱼ=(nⱼ/ntotal)P/p°.

Q=aNH₃²/(aN₂aH₂³) ; à l’équilibre Q=K°.

Comme la réaction réduit le nombre de moles gazeuses de deux, augmenter P à composition fixée diminue Q et favorise le sens direct. Ajouter de l’inerte à P totale fixée diminue les pressions partielles ; ce n’est pas le même protocole qu’à volume fixé.

## 06. De ΔrG° à une conversion

Spé — thermochimie · Laboratoire `haber_bosch`

Les constantes de référence du modèle sont ΔrH°298=−92,22 kJ·mol⁻¹, ΔrS°298=−198,1 J·mol⁻¹·K⁻¹ et ΔrCp°=−45 J·mol⁻¹·K⁻¹. Intégrer les relations de Kirchhoff donne H(T) et S(T), puis G(T)=H(T)−TS(T).

ln K°=−ΔrG°/(RT).

La dichotomie résout ln Q(ξ)=ln K°. Une forte conversion d’équilibre n’impose aucune vitesse. L’IEA replace ce procédé dans les enjeux actuels de production d’engrais et d’énergie.

## 07. Un tableau d’avancement contraint le solveur

Sup / spé — stœchiométrie · Laboratoire `methanol_co2`

Pour une mole initiale de CO₂ et h moles de H₂, les quantités finales sont 1−ξ, h−3ξ, ξ et ξ. La borne physique est ξmax=min(1,h/3). Le solveur reste strictement à l’intérieur pour évaluer les logarithmes.

Q=aCH₃OH aH₂O/(aCO₂ aH₂³).

Le modèle utilise ΔH°298=−49,5 kJ·mol⁻¹, ΔS°298=−177 J·mol⁻¹·K⁻¹ et ΔCp°=−28 J·mol⁻¹·K⁻¹ arrondis. La réaction donnant CO et les équilibres liquide–vapeur sont exclus. Les données NIST du méthanol permettent un approfondissement documentaire.

## 08. Recyclage : écrire le bilan avant le rendement

Spé — procédé · Laboratoire `methanol_co2`

Après un passage de conversion x, la fraction 1−x du CO₂ reste non convertie. On recycle la fraction r de ce reste et on purge l’autre partie. Les produits sont séparés avant le recyclage.

Fcirculant=Ffrais+r(1−x)Fcirculant ; X=x/[1−r(1−x)].

Cette formule suppose que la conversion x reste la même à chaque passage, grâce au maintien du rapport d’alimentation. Elle donne le bilan du carbone. La circulation augmente aussi ; sa compression et sa séparation ont un coût énergétique absent du TP.

## 09. Pourquoi les lignes changent de pente

Spé — diagramme d’Ellingham · Laboratoire `ellingham_zinc`

Pour 2Zn+O₂→2ZnO, on utilise ΔrG°=ΔrH°−TΔrS°. Le TP reprend les données du zinc page 564 : fusion à 693 K, 6,7 kJ·mol⁻¹ ; vaporisation à 1180 K, 114,8 kJ·mol⁻¹.

Lors d’une transition, le potentiel chimique est continu : ΔHtransition−TtransitionΔStransition=0. Ajouter les variations correspondantes à H° et S° du zinc donne donc des segments raccordés. Le zinc est réactif de la formation : ses contributions sont soustraites deux fois.

## 10. Soustraire pour obtenir la réduction

Spé — méthode · Laboratoire `ellingham_zinc`

Les formations 2Zn+O₂→2ZnO et 2C+O₂→2CO sont toutes deux normalisées à une mole de O₂. Leur différence, divisée par deux, donne ZnO+C→Zn+CO. Avec 2CO+O₂→2CO₂, on obtient ZnO+CO→Zn+CO₂.

ΔrG=ΔrG°+RT ln Q.

Lorsque Zn est gazeux, son activité intervient dans Q ; lorsqu’il est une phase condensée pure, elle vaut 1. ΔrG<0 favorise le sens écrit, sans préciser sa vitesse. Il faut éviter de comparer une courbe par mole de O₂ à une courbe par mole de métal.

## 11. Une réaction endothermique avec un gaz produit

Spé — équilibre hétérogène · Laboratoire `calcination_ciment`

CaCO₃(s)⇌CaO(s)+CO₂(g). Si les deux solides purs sont présents, leurs activités valent 1 et Q=pCO₂/p°. L’approximation du TP est ΔH°=178,3 kJ·mol⁻¹ et ΔS°=160,6 J·mol⁻¹·K⁻¹.

ΔrG=ΔH°−TΔS°+RT ln(pCO₂/p°).

Le seuil du modèle est Téquilibre=ΔH°/[ΔS°−R ln(pCO₂/p°)]. Diminuer pCO₂ abaisse ce seuil. Un seuil thermodynamique n’est pas une température de four suffisante pour une cadence donnée.

## 12. Le CO₂ de réaction ne dépend pas du combustible

Sup / spé — bilan matière-énergie · Laboratoire `calcination_ciment`

Une mole de carbonate donne une mole de CO₂, même si le chauffage est électrique. Pour 1000 kg de CaCO₃, la conversion complète donne environ 439,7 kg de CO₂. L’énergie réactionnelle est nΔH° ; le chauffage des matières s’ajoute dans un procédé réel.

La fraction capturée c donne mCO₂,capturé=c mCO₂ et mCO₂,rejeté=(1−c)mCO₂. Les enjeux actuels du secteur sont documentés par l’IEA. Ici, ni les autres réactions du clinker ni l’énergie du captage ne sont calculées.

## 13. Dériver les deux courbes sans les confondre

Spé — liquide–vapeur · Laboratoire `distillation_ideale`

Raoult donne pA=(1−xL)p*A et pB=xLp*B. À l’ébullition, P=pA+pB. Dans la vapeur idéale, yV=pB/P, d’où yV=αxL/[1+(α−1)xL].

Pébullition=(1−xL)p*A+xLp*B ; 1/Prosée=(1−yV)/p*A+yV/p*B.

Les courbes n’emploient pas la même composition : xL pour l’ébullition et yV pour la rosée. Dans un diagramme isotherme P–composition, le liquide seul est au-dessus du fuseau et la vapeur seule en dessous.

## 14. La règle du levier est un bilan

Sup / spé — mélange · Laboratoire `distillation_ideale`

Pour une mole globale, le liquide contient 1−β mole et la vapeur β mole. Le bilan du constituant B est z=(1−β)xL+βyV.

β=(z−xL)/(yV−xL).

Cette formule ne s’applique que si les deux phases existent. Elle donne β entre 0 et 1 lorsque xL≤z≤yV. En phase unique, la composition de la phase est z. Une température et une pression ne suffisent pas à déterminer la quantité de chaque phase sans la composition globale.

## 15. Construire un fuseau de solidification

Spé — équilibre de phases · Laboratoire `alliage_solidification`

Dans une solution idéale, µi,phase=µi,pur,phase+RT ln xi,phase. À coexistence, µi,L=µi,S. Avec ΔGfus,i≈ΔHfus,i(1−T/Tf,i), on obtient :

xi,L/xi,S=exp[−ΔHfus,i(1−T/Tf,i)/(RT)].

Les deux relations pour A et B, avec xA+xB=1 dans chaque phase, donnent les compositions du fuseau. Le TP utilise des paramètres proches de Cu–Ni, sans ajustement à des mesures réelles.

## 16. Lire le refroidissement d’un alliage

Sup / spé — bilan · Laboratoire `alliage_solidification`

Au-dessus du liquidus pour z fixé, tout l’alliage est liquide. Entre liquidus et solidus, les compositions xL et xS se lisent aux extrémités d’un segment horizontal à T fixé. Au-dessous du solidus, tout est solide.

fS=(z−xL)/(xS−xL).

Le modèle ne présente pas de palier eutectique : une plage de coexistence remplace le changement d’état isotherme d’un corps pur. Les composés définis et eutectiques du Mg–Ni, page 568, demandent des domaines supplémentaires.

## 17. Une coloration mesure un avancement

Sup · TP du recueil p.546 · Laboratoire `horloge_iode`

On note t le temps, V le volume cumulé associé aux seuils de coloration et V∞ son asymptote supposée. L’atelier reprend six couples : t=50,100,170,230,315,410 s et V=1,2,3,4,5,6 mL.

Le diiode formé est consommé rapidement par le thiosulfate. Les ions iodure sont ainsi régénérés ; lorsque le thiosulfate ajouté est épuisé, le diiode colore l’amidon. Le seuil traduit donc une quantité formée, pas une mesure instantanée de vitesse.

H₂O₂+2I⁻+2H⁺ → I₂+2H₂O ; I₂+2S₂O₃²⁻ → 2I⁻+S₄O₆²⁻.

Dans le modèle, la fraction restante y=c(t)/c₀ vaut 1−V/V∞, où c₀ est la concentration initiale du réactif suivi. Avec V∞=10 mL, V=5 mL donne y=1/2 : le temps de demi-réaction observé est 315 s.

## 18. Comparer des lois, pas des axes différents

Sup / Spé · identification d’un ordre apparent · Laboratoire `horloge_iode`

On note y=c/c₀ la concentration réduite et κ le coefficient normalisé. Les modèles d’ordres 0, 1 et 2 donnent respectivement y=max(1−κt,0), y=exp(−κt) et y=1/(1+κt). Leurs transformations linéaires sont 1−y, −ln y et 1/y−1.

Pour des mesures tᵢ et une transformation zᵢ, l’ajustement passant par l’origine donne κ=Σtᵢzᵢ/Σtᵢ². Chaque courbe est ensuite reconvertie en volume : on compare Σ(Vprévu−Vmesuré)²/6. Comparer les erreurs des trois axes transformés n’aurait pas la même signification.

Avec V∞=10 mL, l’ordre 1 est le meilleur des trois modèles testés : κ≈2,2115×10⁻³ s⁻¹ et t½ ajusté≈313,43 s. Pour les ordres 0 et 2, κ vaut k/c₀ et kc₀ respectivement : son unité normalisée ne donne pas celle de k.

Une seule série où iodure et acidité sont presque constants ne permet pas d’identifier séparément leurs ordres partiels. Il faudrait des séries supplémentaires où ces concentrations varient.

## 19. Arrhénius : calculer avant de chauffer le modèle

Sup · fiche C6 p.548 · Laboratoire `arrhenius_catalyse`

On note T la température en K, Ea l’énergie d’activation en J·mol⁻¹ et R la constante des gaz parfaits. Pour une constante cinétique k(T)=A exp(−Ea/RT), le préfacteur A a la même unité que k.

ln[k(T₂)/k(T₁)]=(Ea/R)(1/T₁−1/T₂).

Le TP utilise k(500 K)=0,01 s⁻¹, puis choisit Ea. Changer Ea conserve cette référence et ajuste donc A. Avec Ea=80 kJ·mol⁻¹, passer de 500 à 600 K multiplie k par environ 24,711 : k(600 K)≈0,24711 s⁻¹.

Pour déterminer Ea à partir de mesures, représenter ln k en fonction de 1/T : la pente vaut −Ea/R. Les températures en degrés Celsius doivent être converties avant ce calcul.

## 20. Le catalyseur change le chemin

Sup / Spé · vitesse et équilibre · Laboratoire `arrhenius_catalyse`

On note ΔEa la diminution de la barrière, en J·mol⁻¹. À température fixée, si le préfacteur est le même pour les deux voies, kcat/k=exp(ΔEa/RT). À 500 K, un abaissement de 20 kJ·mol⁻¹ donne un facteur environ 122,84.

Le profil dessiné relie les mêmes réactifs et produits : leur différence d’énergie, ici choisie égale à −40 kJ·mol⁻¹, ne change pas. L’énergie d’activation mesure une barrière ; l’enthalpie de réaction mesure une différence entre états.

Un catalyseur ouvre une voie pour l’aller et le retour. À T fixée, il ne modifie pas la constante d’équilibre. Il peut aider un procédé à atteindre plus vite sa conversion thermodynamiquement accessible ; il ne garantit pas un rendement particulier.

Adsorption, sélectivité, désactivation et diffusion dans le grain sont des questions distinctes, étudiées dans les autres laboratoires.

## 21. Une cuve agitée se calcule par un bilan

Sup / Spé · application industrielle guidée · Laboratoire `reacteurs_residence`

On note Q le débit volumique, Vréac le volume de la cuve et τ=Vréac/Q le temps de séjour. Pour A→B, C₀ et C sont les concentrations d’entrée et de sortie ; k est la constante du premier ordre.

À l’état stationnaire, la concentration uniforme de la cuve vaut celle de la sortie. Le bilan Q(C₀−C)=Vréac kC donne C=C₀/(1+kτ). La conversion X=1−C/C₀ vaut donc Da/(1+Da), avec Da=kτ.

Le débit doit être exprimé avec le même temps que k. Ici k est en s⁻¹ et le curseur τ en minutes : Da=60kτ. Pour k=0,01 s⁻¹ et τ=5 min, Da=3 et X=75 %.

La cuve mélangée expose tout le réacteur à la concentration de sortie. Cette propriété explique sa comparaison avec le piston pour cette seule cinétique du premier ordre.

## 22. Piston et cuves en série

Spé · socle PC et complément guidé · Laboratoire `reacteurs_residence`

On note τ le séjour total en secondes. Dans le réacteur piston idéal, chaque élément de fluide suit dC/dt=−kC : la conversion de sortie vaut Xpiston=1−exp(−kτ).

Pour N cuves identiques à même séjour total, chaque cuve a un séjour τ/N. Les concentrations se multiplient par 1/(1+Da/N), d’où XN=1−(1+Da/N)⁻ᴺ. N=1 retrouve la cuve unique ; la limite N→∞ retrouve le piston.

Avec Da=3 et N=3, XN=1−2⁻³=87,5 %, contre 95,021 % pour le piston. Les bilans de la cuve agitée et du piston du premier ordre relèvent du programme PC ; la série de cuves est un complément. Ajouter des appareils augmente aussi contraintes de mélange, coût et transferts, non calculés ici.

## 23. Former puis consommer un produit utile

Sup / Spé · fiche C6 p.548 · Laboratoire `selectivite_successive`

On note A,B,C les concentrations dans le schéma A→B→C. Les constantes k₁,k₂ sont positives et dans la même unité de temps. Avec A(0)=A₀, B(0)=C(0)=0, les bilans sont A′=−k₁A, B′=k₁A−k₂B et C′=k₂B.

A=A₀e⁻ᵏ¹ᵗ ; B=A₀k₁(e⁻ᵏ¹ᵗ−e⁻ᵏ²ᵗ)/(k₂−k₁) si k₁≠k₂ ; C=A₀−A−B.

B est d’abord formé, puis consommé. Un maximum intérieur vérifie k₁A=k₂B : sa formation compense sa consommation. La conversion de A continue pourtant à augmenter. Ce modèle donne une première lecture des stratégies de sélectivité lors de transformations successives.

## 24. Un optimum avec un cas limite régulier

Spé · dérivation et passage à la limite · Laboratoire `selectivite_successive`

On note topt l’instant du maximum de B. Pour k₁≠k₂, annuler B′ donne topt=ln(k₂/k₁)/(k₂−k₁), positif quel que soit l’ordre des deux constantes.

Si k₁=k₂=k, la formule précédente doit être remplacée par sa limite : B=A₀kt exp(−kt). Son maximum est obtenu à t=1/k et vaut A₀/e. Une différence de deux exponentielles divisée par une petite différence de constantes demande aussi un calcul numérique adapté.

Pour A₀=1 mol·L⁻¹, k₁=0,1 et k₂=0,04 min⁻¹, topt≈15,2715 min et Bmax≈0,542884 mol·L⁻¹. À t=15 min, A≈0,223130, B≈0,542802 et C≈0,234067 mol·L⁻¹ : leur somme reste 1.

## 25. Un bilan de sites remplace une loi puissance

Spé · catalyse hétérogène guidée · Laboratoire `catalyse_surface`

On note θlibre la fraction de sites vacants et θA,θB celles occupées. Les pressions pA,pB sont en bar ; KA,KB sont en bar⁻¹. À l’équilibre d’adsorption, θA=KApAθlibre et θB=KBpBθlibre.

θlibre=1/(1+KApA+KBpB) ; θA=KApA/(1+KApA+KBpB) ; θB=KBpB/(1+KApA+KBpB).

Ces relations viennent de θlibre+θA+θB=1. Avec pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, le dénominateur vaut 5 : 20 % des sites sont libres, 40 % portent A et 40 % portent B.

Ce modèle aide à lire l’effet d’une espèce concurrente sur un matériau catalytique. Il ne prétend pas représenter un catalyseur commercial précis.

## 26. Saturation, inhibition et ordre apparent

Spé · prolongement vers les procédés · Laboratoire `catalyse_surface`

On note kcat la constante de transformation de A adsorbé et vsite=kcatθA la vitesse par site. Dans l’atelier kcat=1 s⁻¹. À pB fixé, une faible pA donne vsite≈kcatKApA/(1+KBpB), presque proportionnelle à pA ; à forte pA, vsite tend vers kcat.

L’ordre local en A est nA=∂ln(vsite)/∂ln(pA)=(1+KBpB)/(1+KApA+KBpB). Il passe de presque 1 à presque 0. L’ordre local en B est nB=−KBpB/(1+KApA+KBpB), négatif lorsque B occupe des sites.

Un ordre apparent variable ne contredit pas un mécanisme : il peut résulter d’un équilibre d’adsorption suivi d’une transformation. La carte représente une fraction de sites, pas une température ni une concentration dans le grain.

## 27. L’AEQS élimine les intermédiaires, pas les bilans

Spé · mécanisme source p.549–550 · Laboratoire `ethanal_aeqs`

On note c=[CH₃CHO] la concentration d’éthanal et z=[CH₃·] celle du radical méthyle, en mol·L⁻¹. L’amorçage a pour vitesse k₁c ; la propagation CH₃·+CH₃CHO a pour vitesse k₅zc ; la terminaison de deux méthyles a pour vitesse k₆z².

Les autres intermédiaires du recueil sont CHO·, H· et CH₃CO·. Leurs bilans quasi stationnaires donnent k₂[CHO·]=k₁c, k₃[H·]c=k₁c et k₄[CH₃CO·]=k₁c+k₅zc. Le bilan du méthyle devient 2k₁c−2k₆z²=0.

z=√(k₁c/k₆) ; vE=2k₁c+k₅√(k₁/k₆)c³ᐟ².

Le facteur 2 est conservé. Le mécanisme donne vCO=vE, vH₂=vC₂H₆=k₁c et vCH₄=k₅zc. Le tableau contrôle les atomes, même lorsque le régime d’amorçage n’est pas négligeable.

## 28. Un ordre non entier et une énergie composée

Spé · AEQS et Arrhénius · Laboratoire `ethanal_aeqs`

On pose u=2k₁c et w=k₅√(k₁/k₆)c³ᐟ², les deux contributions à vE=u+w. L’ordre local vaut nlocal=(u+1,5w)/(u+w). Il est compris entre 1 et 3/2 ; le régime 3/2 exige w≫u.

Si kᵢ suit Arrhénius d’énergie Eᵢ, le coefficient de propagation k₅√(k₁/k₆) a l’énergie Eprop=E₅+(E₁−E₆)/2. Le recueil donne E₁=318, E₅=42 et E₆=0 kJ·mol⁻¹ : Eprop=201 kJ·mol⁻¹.

Pour la vitesse totale à c fixé, Eapp=(318u+201w)/(u+w). L’énergie 201 n’est donc pas celle de tous les régimes. La définition de longueur retenue donne L=vE/(k₁c)=2+w/(k₁c) ; les valeurs réglables ne présupposent pas L≥100.

Le rôle de l’AEQS est de simplifier un système cinétique. Sa validité physique se discute à partir des échelles de temps, séparément du contrôle algébrique des bilans.

## 29. Deux courbes pour un bilan de chaleur

Sup / Spé · cinétique et thermochimie · Laboratoire `emballement_thermique`

On note q(T) la puissance volumique de production, Ta la température du fluide extérieur et h le coefficient d’évacuation. La capacité thermique volumique Cth est constante. Les unités sont W·L⁻¹ pour q, W·L⁻¹·K⁻¹ pour h et J·L⁻¹·K⁻¹ pour Cth.

Cth dT/dt=F(T)=q(T)−h(T−Ta) ; q(T)=qref exp[(Ea/R)(1/300−1/T)].

Un équilibre T* est une intersection des deux courbes : F(T*)=0. La chaleur produite croît selon Arrhénius ; la chaleur évacuée croît linéairement dans ce modèle. À Ta=300 K, qref=0,5 W·L⁻¹, Ea=60 kJ·mol⁻¹ et h=0,2 W·L⁻¹·K⁻¹, deux équilibres sont trouvés dans [300,390 K], vers 303,230 et 338,459 K.

La concentration est maintenue dans le modèle : aucun épuisement du réactif ne limite la chaleur. La représentation n’est donc pas celle d’un lot fermé complet.

## 30. Une intersection peut repousser la trajectoire

Spé · stabilité et limite du calcul · Laboratoire `emballement_thermique`

On note δT=T−T* le petit écart à un équilibre simple. La linéarisation donne Cth δT′≈F′(T*)δT. Si F′<0, un petit écart décroît : l’équilibre est localement stable. Si F′>0, il augmente : l’équilibre est instable.

La dérivée vaut F′(T)=q(T)Ea/(RT²)−h, avec Ea en joules. Pour les réglages par défaut, elle vaut environ −0,14930 au premier équilibre et +0,28454 W·L⁻¹·K⁻¹ au second.

Une intégration sur 1800 s n’est pas une preuve d’équilibre : depuis 300 K, elle atteint environ 303,018 K, encore distinct de 303,230 K. Depuis un départ plus chaud que l’équilibre instable, elle peut sortir du domaine étudié.

Le logiciel interrompt l’évolution à Ta+90 K. Une courbe arrêtée représente une limite du calcul ; elle ne donne ni la température maximale réelle, ni l’effet des changements de phase ou de la consommation des réactifs.

## 31. Deux temps pour un grain poreux

Spé · prolongement réaction−diffusion · Laboratoire `diffusion_grain`

On note R le rayon du grain en mètres, Deff la diffusivité effective en m²·s⁻¹ et k la constante du premier ordre en s⁻¹. Le temps diffusif est td=R²/Deff ; le temps chimique est tc=1/k.

φ²=td/tc=kR²/Deff.

Si φ est petit, la diffusion est rapide devant la consommation : la concentration reste presque uniforme. Si φ est grand, le réactif est davantage consommé près de la surface avant d’atteindre le centre.

Avec R=500 µm=5×10⁻⁴ m, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹, td=25 s, tc=10 s et φ=√2,5≈1,58114. Diminuer R réduit td au carré, sans changer ici la cinétique intrinsèque.

## 32. Un profil radial et une efficacité moyenne

Spé · génie des catalyseurs, résultat fourni · Laboratoire `diffusion_grain`

On note ρ=r/R la distance réduite, C la concentration et Cs sa valeur de surface. Le bilan stationnaire sphérique est Deff ΔC−kC=0, avec C(R)=Cs et une solution régulière au centre.

C/Cs=sinh(φρ)/(ρ sinhφ) ; au centre, C(0)/Cs=φ/sinhφ.

Le facteur d’efficacité est la moyenne volumique de C/Cs pour une cinétique du premier ordre : η=3∫₀¹(C/Cs)ρ²dρ=3(φ cothφ−1)/φ². Le facteur ρ² vient des coquilles sphériques ; une moyenne sur le rayon seul serait incorrecte.

Pour φ→0, η=1−φ²/15+2φ⁴/315+… ; pour φ grand, η≈3/φ. Les réglages par défaut donnent η≈0,86509 et C(0)/Cs≈0,67937. Ce facteur décrit l’utilisation interne du grain, sans calculer son coût ou la perte de charge du réacteur.

## 33. Assembler les demi-équations dans le bon sens

Sup — redox · Laboratoire `nernst_pile`

Dans la pile Daniell en fonctionnement spontané, le zinc s’oxyde à l’anode : Zn→Zn²⁺+2e⁻. Le cuivre(II) se réduit à la cathode : Cu²⁺+2e⁻→Cu. Les électrons parcourent le circuit extérieur du zinc vers le cuivre.

Zn+Cu²⁺→Zn²⁺+Cu ; E°=0,340−(−0,763)=1,103 V.

Les potentiels de couples sont toujours écrits dans le sens réduction. Une anode est définie par l’oxydation ; son signe dépend du fonctionnement en pile ou en électrolyse.

## 34. Nernst et énergie libre donnent le même équilibre

Sup / spé — équilibre · Laboratoire `nernst_pile`

Pour la réaction écrite, Q=aZn²⁺/aCu²⁺ et E=E°−RT ln Q/(2F). L’enthalpie libre de réaction est ΔrG=−2FE. À l’équilibre, E=0 et Q=K°.

ln K°=2FE°/(RT) ; q=2FnCu.

Une quantité donnée de cuivre fournit une charge donnée. L’énergie électrique totale d’une décharge est une intégrale ∫E dq si E varie ; multiplier une tension initiale par toute la charge n’est généralement pas exact.

## 35. Une réaction, deux électrons, deux gaz

Sup — bilan redox · Laboratoire `electrolyse_h2`

En milieu acide, la cathode suit 2H⁺+2e⁻→H₂ ; l’anode suit H₂O→½O₂+2H⁺+2e⁻. Leur somme est H₂O(l)→H₂(g)+½O₂(g). Deux moles d’électrons produisent une mole de H₂.

nH₂=ηF IΔt/(2F) ; nO₂=nH₂/2.

La durée se convertit en secondes pour obtenir des coulombs. Une production exprimée en kg utilise la masse molaire en kg·mol⁻¹. Le rendement faradique compte la fraction de courant utile ; il ne mesure pas toutes les pertes énergétiques.

## 36. Tension réversible et tension thermoneutre

Spé — thermochimie électrochimique · Laboratoire `electrolyse_h2`

À 298 K, ΔG°≈237,13 et ΔH°≈285,83 kJ·mol⁻¹ pour la décomposition de l’eau liquide. Erev≈1,229 V est la limite du travail électrique réversible ; Etn≈1,481 V correspond à l’enthalpie par charge.

Qévacuée=UIΔt−nH₂ΔH°.

À U entre ces deux tensions et à bon rendement faradique, une partie de l’enthalpie doit être fournie comme chaleur. Le rapport DOE sur l’électrolyse décrit les axes actuels de recherche : efficacité, coûts et systèmes intégrés.

## 37. Trois mécanismes font baisser la tension

Spé — polarisation · Laboratoire `pile_combustible`

La pile consomme H₂+½O₂ et forme H₂O(l). La tension est diminuée par l’activation des réactions aux électrodes, la résistance et le transport des espèces. Le modèle global écrit :

U=Erev−b asinh[j/(2j₀)]−rj+(RT/2F)ln(1−j/jlim).

Le logarithme est évalué seulement pour j<jlim. Le coefficient b représente les deux électrodes de manière globale : il n’est pas une identification de leurs paramètres microscopiques. La présentation DOE Fuel Cell 101 donne le contexte technologique.

## 38. Puissance maximale et rendement : deux critères

Sup / spé — optimisation · Laboratoire `pile_combustible`

La puissance surfacique est p=jU(j). Si U décroît avec j, la puissance peut d’abord augmenter puis diminuer. Un extremum intérieur satisfait U+jU′=0.

ηPCS=U/Etn ; Etn=ΔH°/(2F).

Au courant nul, la tension est maximale mais la puissance est nulle. Le TP cherche le plus grand jU sur une grille ; sa valeur est une approximation numérique du maximum. Il ne compte ni compresseur ni autres auxiliaires.

## 39. Sites occupés et potentiel chimique

Spé — modèle de solution idéale · Laboratoire `batterie_intercalation`

Une électrode d’intercalation possède des sites occupés par Li et des sites vacants. Dans le modèle idéal, le potentiel chimique molaire est µLi=µ°+RT ln[θ/(1−θ)], où θ est la fraction occupée.

Le TP choisit θ−=0,05+0,90s et θ+=1−θ−. La différence des potentiels chimiques donne la tension à vide Uoc=3,4+(RT/F){ln[θ−/(1−θ−)]−ln[θ+/(1−θ+)]}. La valeur 3,4 V sert de référence illustrative ; les fractions restent loin de 0 et 1.

## 40. Intégrer une décharge et compter Joule

Sup / spé — énergie · Laboratoire `batterie_intercalation`

Sous courant de décharge I constant, le modèle donne U=Uoc−rI. La charge associée à un intervalle d’état de charge est q=CΔs en Ah. La puissance Joule est rI² ; elle augmente comme le carré du courant.

W=C∫ₛfin^ₛdébut U(s)ds, en Wh.

Le seuil retenu est 5 % ; aucune énergie disponible sous ce seuil n’est revendiquée. Les électrodes réelles peuvent présenter des plateaux de phases, une dépendance de la résistance à s et des limites de courant absentes ici.

## 41. La corrosion est un fonctionnement électrochimique local

Sup / spé — redox · Laboratoire `corrosion_protection`

Le fer peut s’oxyder : Fe→Fe²⁺+2e⁻. Dans une eau aérée, la réduction de l’oxygène consomme ces électrons. Une même pièce peut porter des sites anodiques et cathodiques sans générateur externe.

Le TP emploie Nernst pour les couples Fe²⁺/Fe et Zn²⁺/Zn. Les branches métalliques suivent une loi réversible en sinh ; la réduction d’O₂ combine activation et transport limité. La perte métallique nette correspond à la partie positive du courant du fer.

## 42. Écrire la somme des courants avec les surfaces

Spé — potentiel mixte · Laboratoire `corrosion_protection`

Pour des métaux connectés, E est commun. Les densités de courant doivent être multipliées par leurs surfaces avant d’être ajoutées. Ramenée à la surface du fer, la conservation donne :

jFe(E)+a jZn(E)+jO₂(E)=0.

Le zinc peut porter l’oxydation à un potentiel où la dissolution du fer est fortement réduite. Une surface de zinc limitée ou un revêtement consommé change la protection. Le calcul instantané ne donne pas sa durée de vie.

## 43. Faraday donne le volume déposé

Sup — électrolyse · Laboratoire `electrodepot`

Cu²⁺+2e⁻→Cu. La quantité déposée est n=IutileΔt/(2F), sa masse m=nM et son volume V=m/ρ. Pour un dépôt uniforme sur S, e=V/S.

e=IutileΔt M/(2FρS).

Le TP emploie M en g·mol⁻¹, ρ en g·cm⁻³ et S en cm² pour obtenir e en cm, puis multiplie par 10⁴ pour obtenir des µm. Il est préférable de choisir un jeu d’unités cohérent avant le calcul.

## 44. Diffusion et courant limite

Spé — transport · Laboratoire `electrodepot`

Dans la couche de diffusion plane stationnaire, le flux molaire est J=D(c∞−csurface)/δ. La densité de courant est j=2FJ. La concentration de surface ne peut pas être négative.

jlim=2FDc∞/δ ; c(x)=c∞[1−(Iutile/Ilim)(1−x/δ)].

À la limite, csurface=0. Diminuer δ par agitation augmente le courant limite. Le TP représente simplement Iutile=min(I,Ilim) ; il ne prédit pas les réactions parasites ou la forme microscopique du dépôt.

## 45. Du cuivre total au potentiel conditionnel

Spé — équilibres couplés · Laboratoire `cuivre_complexation`

Pour Cu(I), ctotal=clibre(1+β₁aNH₃²) ; pour Cu(II), ctotal=clibre(1+β₂aNH₃⁴). Ces expressions conservent l’espèce libre même à faible activité de ligand.

E°cond=E°−(RT/nF)ln(1+βaNH₃^m).

Le TP donne E°Cu⁺/Cu=0,521 V et E°Cu²⁺/Cu=0,340 V, puis β₁=10^10,8 et β₂=10^11,8 par défaut. Le mot conditionnel indique que le ligand libre est fixé et que Nernst utilise la concentration totale de chaque état.

## 46. Frost : la corde donne le signe de dismutation

Spé — bilan d’énergie · Laboratoire `cuivre_complexation`

Les points de Frost sont Cu(0) : (0,0), Cu(I) : (1,E1), Cu(II) : (2,2E2). Le potentiel Cu(II)/Cu(I) vaut 2E2−E1 car les énergies de réaction, pondérées par F, s’ajoutent.

2Cu(I)→Cu(0)+Cu(II) : ΔG°=2F(E2−E1).

Si E1 dépasse la corde d’ordonnée E2 au point d’abscisse 1, ΔG° est négatif et la dismutation standard est favorisée. Une composition réelle introduit aussi RT ln Q ; le diagramme ne remplace pas ce quotient.

## 47. Conserver les ions avec la dilution

Sup / spé — titrage · Laboratoire `dosage_potentiometrique`

Le titrant et la solution initiale ont la même concentration c ; le volume équivalent vaut donc le volume initial. Après ajout r=V/Véquiv, les concentrations totales par volume de mélange sont cAg=c r/(1+r) et cBr=c/(1+r).

Si une quantité s de solide AgBr par litre est présente : [Ag⁺]+s=cAg et [Br⁻]+s=cBr. Leur différence vaut d=cAg−cBr. L’équilibre impose [Ag⁺][Br⁻]=Ks.

## 48. Le saut n’est pas une divergence

Spé — résolution exacte · Laboratoire `dosage_potentiometrique`

Lorsque le solide existe, la racine positive est [Ag⁺]=(d+√(d²+4Ks))/2. Pour d négatif, on emploie la forme conjuguée 2Ks/[√(d²+4Ks)−d] afin d’éviter une perte de précision.

À r=1 : [Ag⁺]=[Br⁻]=√Ks ; E=E°+(RT/F)ln aAg⁺.

Avant formation du solide, les concentrations libres sont les totales. À r=0, aucune activité Ag⁺ n’est imposée et Nernst ne définit pas un potentiel Ag⁺/Ag : le point reste vide. La courbe reprend le dosage de la page 557 en gardant les deux équilibres.
