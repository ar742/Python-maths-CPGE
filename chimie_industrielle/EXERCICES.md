# Chimie pour l’industrie — 72 exercices corrigés

## 01. Combustion du méthane

Sup · Laboratoire `hess_combustion`

Équilibrer la combustion complète d’une mole de méthane. Donner les quantités de CO₂ et d’eau produites.

**Correction guidée**

CH₄+2O₂→CO₂+2H₂O. Les bilans de C, H et O sont respectés. Une mole de CH₄ produit une mole de CO₂ et deux moles d’eau.

## 02. Passer d’une mole à un kilogramme

Sup · Laboratoire `hess_combustion`

Avec M(CH₄)=16,043 g·mol⁻¹ et une chaleur de combustion de 802,292 kJ·mol⁻¹, calculer le PCI en MJ·kg⁻¹.

**Correction guidée**

Un kilogramme contient 1000/16,043 moles. Le PCI vaut 802,292/16,043≈50,010 MJ·kg⁻¹. Écrire explicitement les facteurs 1000 g/kg et 1000 kJ/MJ montre pourquoi ils se compensent.

## 03. Récupération partielle

Spé · Laboratoire `hess_combustion`

Un combustible a PCI=50 et PCS=55 MJ·kg⁻¹. La moitié de son eau condense ; 80 % de la chaleur disponible est récupérée. Calculer la chaleur utile.

**Correction guidée**

La chaleur disponible vaut 50+0,5(55−50)=52,5 MJ·kg⁻¹. La chaleur utile vaut 0,8×52,5=42 MJ·kg⁻¹. Confondre la fraction condensée avec la récupération globale donnerait un autre bilan.

## 04. Calibrer une enthalpie

Sup / spé · Laboratoire `temperature_adiabatique`

Une mole de NO₂ se forme ; Cp=36 J·mol⁻¹·K⁻¹. T passe de 298 à 400 K et 93 % de la chaleur réactionnelle est cédée. Déduire ΔrH°(298 K) du modèle.

**Correction guidée**

La fraction retenue est 0,07. Donc 36×102=−0,07ΔrH°, d’où ΔrH°=−52,457 kJ·mol⁻¹. Le calcul est un bilan calorimétrique avec les données imposées.

## 05. Doubler la capacité thermique

Sup · Laboratoire `temperature_adiabatique`

À énergie libérée fixée, quel est l’effet d’une capacité thermique totale doublée sur la hausse de température ?

**Correction guidée**

ΔT=Qretenue/Cp,total. Doubler la capacité thermique divise ΔT par deux. La température absolue n’est pas divisée par deux : Tfinal=Tinitial+ΔT.

## 06. L’inerte suffit-il à prévoir un réacteur ?

Spé · Laboratoire `temperature_adiabatique`

Le calcul adiabatique donne une température élevée. Peut-on en déduire que le produit NO₂ sera formé intégralement dans le réacteur réel ?

**Correction guidée**

Non. La conversion totale a été imposée. À haute température, l’équilibre peut favoriser la dissociation ; les Cp réels changent et les transferts déterminent la trajectoire. Il faut coupler bilan énergétique, équilibre et cinétique.

## 07. Contrôler le bilan

Sup · Laboratoire `haber_bosch`

Pour ξ=0,4 et 1 mol d’inerte, donner les quantités finales et le nombre total de moles.

**Correction guidée**

N₂ : 0,6 ; H₂ : 1,8 ; NH₃ : 0,8 ; inerte : 1 mol. Le total vaut 4−0,8+1=4,2 mol. Les nombres d’atomes N et H sont conservés.

## 08. Évaluer l’effet d’une compression

Spé · Laboratoire `haber_bosch`

À T et composition fixées, on double P. Par quel facteur Q est-il multiplié ?

**Correction guidée**

Chaque activité gazeuse double. Le numérateur contient deux puissances et le dénominateur quatre : Q est multiplié par 2^(2−4)=1/4. Si le système était à l’équilibre, Q devient inférieur à K° et la réaction avance.

## 09. Catalyse et équilibre

Sup / spé · Laboratoire `haber_bosch`

Un catalyseur réduit la durée nécessaire pour obtenir une composition proche de l’équilibre. Modifie-t-il K° ?

**Correction guidée**

Non. K° dépend de ΔrG° et T pour les états choisis. Un catalyseur modifie les mécanismes et accélère les transformations directe et inverse ; il ne change pas la position de l’équilibre.

## 10. Limiter par le dihydrogène

Sup · Laboratoire `methanol_co2`

On introduit 1 mol de CO₂ et 2 mol de H₂. Quelle est la borne stœchiométrique de conversion de CO₂ ?

**Correction guidée**

Il faut 3 mol de H₂ par mole de CO₂. Donc ξmax=2/3 mol, soit au plus 66,7 % du CO₂ initial. Une méthode numérique qui dépasserait cette borne donnerait une quantité négative de H₂.

## 11. Une boucle de recyclage

Spé · Laboratoire `methanol_co2`

Un passage convertit x=0,25 et r=0,8 du réactif restant est recyclé. Calculer X et Fcirculant/Ffrais.

**Correction guidée**

1−r(1−x)=1−0,8×0,75=0,4. La circulation vaut 1/0,4=2,5 fois le débit frais ; X=0,25/0,4=0,625, soit 62,5 %. Les 37,5 % restants sortent dans la purge.

## 12. Conversion et bilan climatique

Spé — interprétation · Laboratoire `methanol_co2`

Une forte conversion du CO₂ garantit-elle une réduction des émissions sur l’ensemble du procédé ?

**Correction guidée**

Il faut aussi connaître l’origine de H₂ et de l’électricité, la compression, la séparation, le CO₂ d’alimentation et l’usage final du méthanol. Le bilan de conversion du carbone est un bilan de matière ; une comparaison climatique exige un autre périmètre.

## 13. Raccorder à la fusion

Spé · Laboratoire `ellingham_zinc`

Calculer la variation d’entropie de fusion du zinc, avec ΔHfus=6,7 kJ·mol⁻¹ et Tf=693 K.

**Correction guidée**

ΔSfus=ΔHfus/Tf=6700/693≈9,668 J·mol⁻¹·K⁻¹. À Tf, ΔHfus−TfΔSfus=0 : le raccord de G est continu.

## 14. Évacuer un produit gazeux

Spé · Laboratoire `ellingham_zinc`

À 1200 K, Q est divisé par 100. De combien ΔrG diminue-t-il ?

**Correction guidée**

La différence vaut RT ln(1/100)=−RT ln100≈−45,95 kJ·mol⁻¹ réaction avec R=8,314 J·mol⁻¹·K⁻¹. Évacuer les produits peut donc favoriser la réaction, si le protocole modifie effectivement Q de ce facteur.

## 15. Choisir la normalisation

Sup / spé · Laboratoire `ellingham_zinc`

À quoi correspond (Gformation,CO−Gformation,ZnO)/2 lorsque les deux formations consomment chacune une mole de O₂ ?

**Correction guidée**

Inverser 2Zn+O₂→2ZnO et l’ajouter à 2C+O₂→2CO donne 2ZnO+2C→2Zn+2CO. Diviser par deux donne une mole de Zn produite. La grandeur est donc en énergie par mole de cette réduction.

## 16. Seuil sous un bar

Spé · Laboratoire `calcination_ciment`

Calculer la température d’équilibre sous pCO₂=1 bar avec les données du TP.

**Correction guidée**

Le logarithme vaut zéro. Téquilibre=178300/160,6≈1110,2 K. Cette valeur concerne l’approximation à ΔH° et ΔS° constants.

## 17. Conserver la masse

Sup · Laboratoire `calcination_ciment`

Vérifier le bilan d’une mole de CaCO₃ avec M(CaO)=56,076 et M(CO₂)=44,010 g·mol⁻¹.

**Correction guidée**

56,076+44,010=100,086 g·mol⁻¹, masse molaire du carbonate. La masse totale est conservée ; la matière est répartie entre solide et gaz.

## 18. Capture de 90 %

Sup / spé · Laboratoire `calcination_ciment`

Pour 1000 kg de carbonate entièrement converti, on forme environ 439,72 kg de CO₂. En capturer 90 % change-t-il la chaleur réactionnelle ?

**Correction guidée**

Environ 395,75 kg sont capturés et 43,97 kg restent non capturés. La chaleur de la réaction de calcination est inchangée si la conversion est la même. La capture exige son propre bilan énergétique, absent ici.

## 19. Enrichissement d’un étage

Spé · Laboratoire `distillation_ideale`

Avec α=3 et xL=0,4, calculer yV.

**Correction guidée**

yV=3×0,4/[1+2×0,4]=2/3. La vapeur est plus riche en B que le liquide car B a la pression de vapeur la plus élevée.

## 20. Calculer une fraction de vapeur

Sup / spé · Laboratoire `distillation_ideale`

Deux phases ont xL=0,25 et yV=0,75 ; z=0,4. Calculer β.

**Correction guidée**

β=(0,4−0,25)/(0,75−0,25)=0,3. Le bilan donne 0,7×0,25+0,3×0,75=0,4. Les phases contiennent 70 % et 30 % des moles globales.

## 21. L’absence d’azéotrope

Spé · Laboratoire `distillation_ideale`

Montrer que yV=xL seulement pour un corps pur lorsque α>1 est constant.

**Correction guidée**

L’égalité donne αx=x[1+(α−1)x], soit (α−1)x(1−x)=0. Avec α>1, x=0 ou x=1. Ce modèle idéal ne possède pas d’azéotrope intérieur.

## 22. Calculer la proportion solide

Sup / spé · Laboratoire `alliage_solidification`

À une température donnée, xL=0,30, xS=0,60 et z=0,45. Calculer fS.

**Correction guidée**

fS=(0,45−0,30)/(0,60−0,30)=0,50. Le liquide et le solide contiennent chacun la moitié des moles ; 0,5×0,30+0,5×0,60=0,45.

## 23. Point pur et fusion

Spé · Laboratoire `alliage_solidification`

Pour un constituant pur, vérifier que l’égalité des potentiels donne T=Tf.

**Correction guidée**

Les fractions valent 1 dans les deux phases, donc le logarithme vaut 0. Il reste ΔHfus(1−T/Tf)=0 ; comme ΔHfus≠0, T=Tf.

## 24. Pourquoi ne pas copier Mg–Ni ?

Spé — lecture · Laboratoire `alliage_solidification`

Un modèle à miscibilité totale peut-il reproduire un diagramme comportant Ni₂Mg et NiMg₂ solides ainsi que des eutectiques ?

**Correction guidée**

Non. Le modèle ne comporte que deux phases de solution, liquide et solide. Des composés définis exigent d’autres potentiels chimiques et domaines ; une coexistence eutectique doit être introduite explicitement. Le modèle sert à apprendre le bilan et la lecture du fuseau.

## 25. Un seuil et une vitesse moyenne

Sup · Laboratoire `horloge_iode`

On suppose V∞=10 mL et y=1−V/V∞. Le volume passe de 4 à 5 mL entre 230 et 315 s. Calculer la vitesse moyenne de consommation de la fraction y et le temps de demi-réaction observé.

**Correction guidée**

y passe de 0,6 à 0,5. La vitesse moyenne −Δy/Δt vaut 0,1/85≈1,1765×10⁻³ s⁻¹. Le seuil y=0,5 est atteint à 315 s : c’est t½ observé. Cette moyenne sur 85 s n’est pas une dérivée instantanée.

## 26. Le coefficient dépend de la normalisation

Sup / Spé · Laboratoire `horloge_iode`

Une réaction suit −dc/dt=kc², avec c en mol·L⁻¹. Poser y=c/c₀ et déterminer la relation entre k et le coefficient κ du modèle y=1/(1+κt). Préciser les unités.

**Correction guidée**

dy/dt=−kc₀y². Après intégration, 1/y−1=kc₀t ; κ=kc₀. Ainsi κ est en s⁻¹, tandis que k est en L·mol⁻¹·s⁻¹. Deux expériences ayant des concentrations initiales différentes peuvent avoir le même k mais des κ différents.

## 27. Ce que l’horloge ne détermine pas

Spé · analyse de données · Laboratoire `horloge_iode`

La loi proposée est v=k[H₂O₂]ᵃ[I⁻]ᵇ[H⁺]ᶜ. Iodure et acidité restent presque constants dans une série. Si l’ajustement indique a≈1, peut-on en déduire b et c ? Comment les étudier ?

**Correction guidée**

Non. La série mesure kappa=k[I⁻]ᵇ[H⁺]ᶜ lorsque a=1 ; elle ne sépare pas les trois facteurs. Pour b, comparer plusieurs séries à acidité fixée en faisant varier [I⁻] : ln(kappa₂/kappa₁)=b ln([I⁻]₂/[I⁻]₁), si le mécanisme reste le même. Faire de même pour c à iodure fixé. Le résultat porte sur les conditions explorées.

## 28. Une référence et une deuxième température

Sup · Laboratoire `arrhenius_catalyse`

Une constante du premier ordre vaut 0,01 s⁻¹ à 500 K. Avec Ea=80 kJ·mol⁻¹, calculer k à 600 K et le temps de demi-réaction.

**Correction guidée**

k₂=0,01 exp[(80000/R)(1/500−1/600)]≈0,24711 s⁻¹. Pour le premier ordre, t½=ln2/k₂≈2,805 s. À 500 K il vaut 69,315 s. L’énergie est convertie en joules pour être cohérente avec R.

## 29. Un gain de barrière, pas un gain d’équilibre

Sup / Spé · Laboratoire `arrhenius_catalyse`

À 500 K, la barrière passe de 80 à 60 kJ·mol⁻¹ avec le même préfacteur. Calculer le facteur d’accélération puis dire ce qu’il permet de conclure sur la constante d’équilibre.

**Correction guidée**

Le facteur est exp[20000/(R×500)]≈122,84. La constante catalysée du modèle vaut donc 1,2284 s⁻¹. Ce nombre concerne une vitesse ; il n’implique aucune multiplication de la constante d’équilibre, inchangée à T fixée pour les mêmes réactifs et produits.

## 30. Retrouver une énergie à partir de deux mesures

Spé · Laboratoire `arrhenius_catalyse`

On mesure k₂/k₁=10 entre T₁=450 K et T₂=500 K. Dans le modèle d’Arrhénius à préfacteur constant, calculer Ea.

**Correction guidée**

Ea=R ln10/(1/450−1/500)≈86,151 kJ·mol⁻¹. C’est une énergie apparente sur cet intervalle. Une courbure du graphe ln k en fonction de 1/T indiquerait que cette représentation avec une seule énergie est insuffisante.

## 31. Ne pas perdre un facteur 60

Sup · Laboratoire `reacteurs_residence`

Pour k=0,01 s⁻¹, τ=5 min et N=3 cuves identiques, calculer Da et les conversions cuve, piston et série.

**Correction guidée**

τ=300 s et Da=3. La cuve donne 3/4=75 %. Le piston donne 1−e⁻³≈95,021 %. Trois cuves donnent 1−(1+3/3)⁻³=87,5 %. Les trois organisations ont le même séjour total, pas le même séjour par cuve.

## 32. Quel séjour pour atteindre 90 % ?

Sup / Spé · Laboratoire `reacteurs_residence`

Une réaction du premier ordre a k=0,01 s⁻¹. Déterminer le séjour nécessaire à X=0,90 dans une cuve unique et dans un piston idéal.

**Correction guidée**

Pour la cuve, Da=X/(1−X)=9, donc τ=900 s=15 min. Pour le piston, Da=−ln(1−X)=ln10, donc τ≈230,259 s=3,8376 min. La comparaison concerne ce modèle isotherme ; elle ne constitue pas à elle seule un choix d’équipement.

## 33. Dimensionner un procédé continu

Spé · bilan industriel · Laboratoire `reacteurs_residence`

Un débit volumique Q=2 L·min⁻¹ traverse un réacteur isotherme de constante k=0,01 s⁻¹. On vise X=90 %. Calculer le volume total pour une cuve, un piston et N=3 cuves identiques. Le séjour total est τ=Vtotal/Q.

**Correction guidée**

Pour la cuve, τ=15 min, donc Vtotal=30 L. Pour le piston, τ=ln10/(60k)≈3,83764 min, donc Vtotal≈7,67528 L. Pour trois cuves, 1−X=(1+Da/3)⁻³ donne Da=3(10¹ᐟ³−1)≈3,46330 ; τ≈5,77217 min et Vtotal≈11,54435 L, soit 3,84812 L par cuve. Ces volumes comparent les modèles à même débit et même objectif, sans calcul économique.

## 34. Les deux constantes égales

Sup / Spé · Laboratoire `selectivite_successive`

Dans A→B→C, prendre k₁=k₂=0,1 min⁻¹ et A₀=1 mol·L⁻¹. Calculer l’instant et la concentration du maximum de B.

**Correction guidée**

B(t)=0,1t exp(−0,1t). Sa dérivée s’annule à t=10 min et change de signe de + à −. Bmax=1/e≈0,367879 mol·L⁻¹ ; au même instant A=1/e et C=1−2/e≈0,264241 mol·L⁻¹.

## 35. Contrôler le bilan à 15 minutes

Sup · Laboratoire `selectivite_successive`

Prendre A₀=1 mol·L⁻¹, k₁=0,1 et k₂=0,04 min⁻¹. Calculer A,B,C à t=15 min puis comparer t à topt.

**Correction guidée**

A=e⁻¹·⁵≈0,223130. B=(0,1/−0,06)(e⁻¹·⁵−e⁻⁰·⁶)≈0,542802. C=1−A−B≈0,234067 mol·L⁻¹. topt=ln(0,4)/(−0,06)≈15,2715 min : à 15 min B augmente encore légèrement.

## 36. Le temps très court montre les étapes

Spé · Laboratoire `selectivite_successive`

Pour A→B→C avec A₀>0, B₀=C₀=0 et k₁,k₂>0, obtenir les premiers termes de B(t) et C(t) lorsque t→0⁺.

**Correction guidée**

A=A₀(1−k₁t+k₁²t²/2)+O(t³). L’équation de B donne B=A₀k₁t−A₀k₁(k₁+k₂)t²/2+O(t³). Par conservation, C=A₀k₁k₂t²/2+O(t³). B apparaît au premier ordre en temps ; C nécessite les deux étapes et apparaît au second ordre.

## 37. Supprimer un compétiteur

Sup / Spé · Laboratoire `catalyse_surface`

Prendre pA=1 bar, KA=2 et KB=1 bar⁻¹. Comparer θA et vsite pour pB=2 bar puis pB=0 ; kcat=1 s⁻¹.

**Correction guidée**

Avec B, θA=2/(1+2+2)=0,4 et vsite=0,4 s⁻¹. Sans B, θA=2/(1+2)=2/3 et vsite=2/3 s⁻¹. Le facteur est (2/3)/0,4=5/3 ; on change la répartition des sites, pas kcat.

## 38. La pression de demi-saturation

Spé · Laboratoire `catalyse_surface`

Dans le modèle compétitif, déterminer la pression pA telle que θA=1/2 à pB fixé. Appliquer à KA=2 bar⁻¹, KB=1 bar⁻¹ et pB=2 bar.

**Correction guidée**

2KApA=1+KApA+KBpB donne pA=(1+KBpB)/KA. Ici pA=3/2=1,5 bar. La présence du compétiteur augmente la pression nécessaire pour occuper la moitié des sites avec A.

## 39. Deux ordres locaux au même point

Spé · Laboratoire `catalyse_surface`

Pour pA=1 bar, pB=2 bar, KA=2 et KB=1 bar⁻¹, calculer nA=∂ln vsite/∂ln pA et nB=∂ln vsite/∂ln pB. Interpréter leurs signes.

**Correction guidée**

Le dénominateur vaut 5. nA=1−KApA/5=3/5 ; nB=−KBpB/5=−2/5. Augmenter A accroît la vitesse avec un effet déjà atténué par saturation. Augmenter B la réduit. Ce sont des dérivées locales, pas des ordres constants valables partout.

## 40. Le facteur deux de terminaison

Spé · Laboratoire `ethanal_aeqs`

Une terminaison CH₃·+CH₃·→C₂H₆ a pour vitesse de réaction k₆z². Écrire son terme dans le bilan de z. Avec l’AEQS du mécanisme source, justifier z=√(k₁c/k₆).

**Correction guidée**

Chaque événement consomme deux radicaux : le terme est −2k₆z², tandis que la formation d’éthane vaut +k₆z². Après élimination des autres intermédiaires, le méthyle reçoit 2k₁c et les termes de propagation se compensent : 0=2k₁c−2k₆z². On obtient z²=k₁c/k₆, sans facteur √2 supplémentaire.

## 41. Un régime proche de 3/2

Spé · Laboratoire `ethanal_aeqs`

Prendre c=0,1 mol·L⁻¹, k₁=10⁻⁶ s⁻¹, k₅=10² et k₆=10⁶ L·mol⁻¹·s⁻¹. Calculer z, u=2k₁c, w=k₅zc, l’ordre local et L.

**Correction guidée**

z=√10⁻¹³≈3,1623×10⁻⁷ mol·L⁻¹. u=2×10⁻⁷ et w≈3,1623×10⁻⁶ mol·L⁻¹·s⁻¹. Ainsi nlocal=(u+1,5w)/(u+w)≈1,47026. L=(u+w)/(k₁c)≈33,6228. La propagation domine mais n’est pas seule ; l’ordre n’est pas exactement 3/2.

## 42. Énergie apparente et conservation du carbone

Spé · synthèse · Laboratoire `ethanal_aeqs`

Avec u,w définis dans le cours et les énergies source E₁=318, E₅=42, E₆=0 kJ·mol⁻¹, déterminer Eprop et Eapp. Vérifier le bilan du carbone à partir de vCO=u+w, vCH₄=w et vC₂H₆=u/2.

**Correction guidée**

Eprop=42+(318−0)/2=201 kJ·mol⁻¹. Eapp=(318u+201w)/(u+w), qui tend vers 201 seulement si w/u→∞. Le carbone entrant disparaît à 2vE=2(u+w) ; il ressort à vCO+vCH₄+2vC₂H₆=(u+w)+w+u=2(u+w). Le bilan est conservé pour tout rapport u/w.

## 43. Une pente décide de la stabilité

Spé · Laboratoire `emballement_thermique`

Au premier équilibre T*=303,230 K des réglages par défaut, q(T*)=h(T*−Ta) avec Ta=300 K et h=0,2 W·L⁻¹·K⁻¹. Prendre Ea=60000 J·mol⁻¹. Calculer F′(T*) et conclure.

**Correction guidée**

q(T*)≈0,64603 W·L⁻¹. F′=qEa/(RT*²)−h≈−0,14930 W·L⁻¹·K⁻¹. Le signe est négatif : les petits écarts décroissent. Le temps caractéristique linéaire vaut Cth/|F′|≈669,80 s pour Cth=100 J·L⁻¹·K⁻¹.

## 44. L’évacuation ne produit pas toujours de la chaleur

Sup · Laboratoire `emballement_thermique`

À Ta=300 K, h=0,2 W·L⁻¹·K⁻¹, qref=0,5 W·L⁻¹ et Cth=100 J·L⁻¹·K⁻¹, calculer dT/dt à T=300 K. Expliquer le signe du terme −h(T−Ta) si T<Ta.

**Correction guidée**

À 300 K, q=qref=0,5 et l’échange vaut zéro : dT/dt=0,5/100=0,005 K·s⁻¹. Si T<Ta, −h(T−Ta)>0 : le fluide extérieur réchauffe le milieu. L’expression d’échange représente un transfert selon l’écart de température, pas une perte positive dans tous les cas.

## 45. Une courbe arrêtée n’est pas un état final

Spé · interprétation · Laboratoire `emballement_thermique`

Le calcul s’interrompt lorsque T atteint la limite Ta+90 K avant 1800 s. Peut-on donner cette température comme maximum du procédé ? Quelles conclusions restent justifiées ?

**Correction guidée**

Non. On sait que la trajectoire calculée a quitté le domaine où le modèle est exploré ; on ne connaît pas son maximum après cet arrêt. On peut commenter le signe du bilan avant la sortie et les équilibres simples localisés dans l’intervalle. Un procédé réel peut épuiser ses réactifs, changer de phase ou modifier ses transferts : ces effets sont absents du modèle.

## 46. Un rayon en micromètres

Sup / Spé · Laboratoire `diffusion_grain`

Un grain a R=500 µm, Deff=10⁻⁸ m²·s⁻¹ et k=0,1 s⁻¹. Calculer td, tc et φ. Que devient φ si le rayon est divisé par deux ?

**Correction guidée**

R=5×10⁻⁴ m, donc td=R²/Deff=25 s et tc=10 s. φ=√(25/10)≈1,58114. Si R est divisé par deux, td est divisé par quatre et φ par deux. La constante k est conservée : on modifie l’alimentation interne, pas la réaction intrinsèque.

## 47. Le centre n’est pas singulier

Spé · limite · Laboratoire `diffusion_grain`

On fournit C/Cs=sinh(φρ)/(ρ sinhφ), avec φ>0 et ρ=r/R. Déterminer sa limite au centre. Pour φ=2, calculer C(0)/Cs et η.

**Correction guidée**

sinh(φρ)=φρ+O(ρ³), donc C(0)/Cs=φ/sinhφ. À φ=2, ce rapport vaut environ 0,551441. Le facteur η=3(2coth2−1)/4≈0,805972. La moyenne volumique reste supérieure à la concentration centrale réduite.

## 48. Presque tout le grain est alimenté

Spé · développement limité · Laboratoire `diffusion_grain`

À partir de cothφ=1/φ+φ/3−φ³/45+2φ⁵/945+O(φ⁷), retrouver le développement de η=3(φcothφ−1)/φ². Estimer η pour φ=0,1.

**Correction guidée**

φcothφ−1=φ²/3−φ⁴/45+2φ⁶/945+O(φ⁸). Ainsi η=1−φ²/15+2φ⁴/315+O(φ⁶). À φ=0,1, η≈0,999333968 : la consommation est presque celle d’un grain uniformément à Cs. Le développement évite aussi la soustraction numérique de deux nombres presque égaux.

## 49. Charge d’un dépôt de cuivre

Sup · Laboratoire `nernst_pile`

Combien de coulombs correspondent à 0,1 mol de Cu²⁺ réduit en Cu ?

**Correction guidée**

Chaque mole consomme deux moles d’électrons. q=2×96485,332×0,1≈19297 C, soit environ 5,361 Ah. Le potentiel n’intervient pas dans ce bilan de charge.

## 50. Pente de Nernst

Sup / spé · Laboratoire `nernst_pile`

À 298,15 K, Q est multiplié par 100. Déterminer la variation de E pour un échange de deux électrons.

**Correction guidée**

ΔE=−RT ln100/(2F)≈−0,05916 V. Le quotient est sans dimension ; la transformation devient moins favorable dans le sens écrit.

## 51. Constante d’équilibre très grande

Spé · Laboratoire `nernst_pile`

Pour E°=1,103 V et n=2 à 298,15 K, évaluer log₁₀ K°.

**Correction guidée**

log₁₀K°=2FE°/(RT ln10)≈37,29. Une constante grande signifie un équilibre très déplacé vers les produits pour les états et la réaction choisis ; elle ne donne pas la vitesse de transfert de charge.

## 52. Production en une heure

Sup · Laboratoire `electrolyse_h2`

Calculer nH₂ pour I=100 A, Δt=1 h et ηF=1.

**Correction guidée**

q=100×3600=360000 C ; nH₂=q/(2F)≈1,866 mol. La masse vaut environ 3,761 g et nO₂≈0,933 mol. Il s’agit d’une cellule, pas d’une pile de cellules en série.

## 53. Tension et consommation spécifique

Sup / spé · Laboratoire `electrolyse_h2`

Si U est multipliée par 1,2 à I, Δt et ηF constants, comment évoluent production et kWh par kg ?

**Correction guidée**

La production faradique est inchangée. L’énergie électrique UIΔt et la consommation par kg sont multipliées par 1,2. La chaleur dissipée augmente aussi dans ce modèle.

## 54. Un rendement électrique supérieur à un

Spé · Laboratoire `electrolyse_h2`

Avec ηF=1 et U=1,35 V, le quotient ηPCS=Etn/U est supérieur à 1. Contredit-il le premier principe ?

**Correction guidée**

Non : Etn/U≈1,097 et le système reçoit de la chaleur. Le dénominateur ne compte que l’électricité, tandis que l’énergie du H₂ inclut cette chaleur importée. Un rendement total doit compter toutes les entrées.

## 55. Un point de fonctionnement

Sup · Laboratoire `pile_combustible`

Une pile fournit U=0,70 V à j=0,80 A·cm⁻². Calculer la puissance surfacique et le rendement PCS si Etn=1,481 V.

**Correction guidée**

p=0,80×0,70=0,56 W·cm⁻² ; ηPCS=0,70/1,481≈47,3 %. Le calcul suppose un rendement faradique de 1 et exclut les auxiliaires.

## 56. Une pile avec seulement une résistance

Spé · Laboratoire `pile_combustible`

Pour U=E−rj, déterminer le courant de puissance maximale et la tension correspondante.

**Correction guidée**

p=Ej−rj² ; p′=E−2rj. Le maximum est en j*=E/(2r), avec U*=E/2 et p*=E²/(4r). Le rendement électrique au maximum est inférieur au rendement limite à petit courant.

## 57. Transport à la limite

Spé · Laboratoire `pile_combustible`

Que devient −ln(1−j/jlim) lorsque j approche jlim par valeurs inférieures ?

**Correction guidée**

La grandeur diverge vers +∞. Le modèle impose une forte perte de tension et ne peut être prolongé à j≥jlim. En production électrique, on s’arrête avant que la tension devienne non positive.

## 58. La charge restante

Sup · Laboratoire `batterie_intercalation`

Avec C=10 Ah et s=0,65, calculer la charge disponible jusqu’au seuil s=0,05.

**Correction guidée**

q=10(0,65−0,05)=6 Ah, soit 21600 C. Ce résultat ne donne pas encore l’énergie en Wh : il faut connaître la tension.

## 59. Une chute ohmique

Sup · Laboratoire `batterie_intercalation`

Calculer la chute de tension et la chaleur Joule pour I=8 A et r=0,05 Ω.

**Correction guidée**

rI=0,40 V ; rI²=3,2 W. À courant doublé, la chute double mais la chaleur Joule quadruple.

## 60. Pourquoi intégrer U ?

Spé · Laboratoire `batterie_intercalation`

Une décharge de 4 Ah suit U(q)=4,0−0,2q, q étant en Ah déjà délivrés. Calculer l’énergie et comparer à Uinitial×4 Ah.

**Correction guidée**

W=∫₀⁴(4−0,2q)dq=16−0,1×16=14,4 Wh. Le produit initial 4×4=16 Wh surestime le résultat car la tension diminue pendant la décharge.

## 61. Bilan de corrosion en eau aérée

Sup · Laboratoire `corrosion_protection`

Assembler Fe→Fe²⁺+2e⁻ et O₂+4H⁺+4e⁻→2H₂O.

**Correction guidée**

Multiplier la demi-équation du fer par deux : 2Fe+O₂+4H⁺→2Fe²⁺+2H₂O. Le pH impose les activités ; en milieu neutre, une écriture avec OH⁻ et la formation d’hydroxydes peut être plus adaptée au bilan global.

## 62. Surface et conservation du courant

Spé · Laboratoire `corrosion_protection`

Au potentiel mixte, jFe=0,001, jZn=0,020 et jO₂=−0,041 mA·cm⁻². Trouver a.

**Correction guidée**

0,001+0,020a−0,041=0 donne a=2. Les densités sont ramenées à la surface du fer après multiplication de la contribution zinc par a.

## 63. Charge et masse perdue

Sup / spé · Laboratoire `corrosion_protection`

Un courant de dissolution de 1 mA circule pendant 24 h pour Fe→Fe²⁺. Calculer la masse de fer perdue.

**Correction guidée**

q=0,001×86400=86,4 C ; nFe=q/(2F)≈4,477×10⁻⁴ mol. Avec MFe=55,845 g·mol⁻¹, m≈0,0250 g. Ce bilan suppose que tout le courant anodique est associé à cette dissolution.

## 64. Épaisseur après trente minutes

Sup / spé · Laboratoire `electrodepot`

Pour Iutile=1 A, Δt=30 min et S=100 cm², calculer l’épaisseur de cuivre.

**Correction guidée**

n=1800/(2F)≈0,009328 mol ; m≈0,5928 g. e=m/(8,96×100)≈0,0006616 cm, soit environ 6,616 µm.

## 65. Convertir pour Fick

Spé · Laboratoire `electrodepot`

Convertir c=0,1 mol·L⁻¹, δ=100 µm et S=500 cm² en SI.

**Correction guidée**

c=100 mol·m⁻³, δ=10⁻⁴ m et S=0,05 m². Avec D=7×10⁻¹⁰ m²·s⁻¹, Ilim=2FDcS/δ≈6,754 A.

## 66. Dépasser la limite

Spé · Laboratoire `electrodepot`

Le courant limite vaut 2 A. On impose 5 A pendant 1 h et le modèle donne Iutile=2 A. Calculer le rendement faradique du dépôt et la charge parasite.

**Correction guidée**

ηF=2/5=40 %. La charge parasite est (5−2)×3600=10800 C. Elle n’ajoute pas de cuivre selon le modèle ; il faut connaître les autres réactions pour en déduire les produits.

## 67. Un facteur de complexation

Spé · Laboratoire `cuivre_complexation`

Pour β=10⁸, m=2 et aNH₃=10⁻³, calculer L et la fraction libre.

**Correction guidée**

L=1+10⁸×10⁻⁶=101. La fraction libre est 1/L≈0,00990, soit environ 0,99 %. Remplacer L par βa^m serait une approximation ; elle n’est pas nécessaire ici.

## 68. Pondérer un potentiel

Spé · Laboratoire `cuivre_complexation`

Avec E1=0,52 V et E2=0,34 V pour les réductions vers Cu(0), déterminer le potentiel Cu(II)/Cu(I).

**Correction guidée**

La réduction Cu(II)→Cu(0) échange deux électrons ; Cu(I)→Cu(0) en échange un. Donc −FE21=−2FE2+FE1 et E21=2E2−E1=0,16 V.

## 69. Dismutation de Cu(I)

Spé · Laboratoire `cuivre_complexation`

Pour E1=0,52 et E2=0,34 V, donner le signe de ΔG° pour 2Cu(I)→Cu(0)+Cu(II).

**Correction guidée**

ΔG°=2F(0,34−0,52)=−0,36F≈−34,7 kJ·mol⁻¹ réaction. La dismutation standard est favorisée. Une complexation assez forte de Cu(I) peut abaisser E1 et inverser cette conclusion.

## 70. Concentrations à l’équivalence

Sup / spé · Laboratoire `dosage_potentiometrique`

Avec Ks=10⁻¹² et concentrations totales égales, calculer [Ag⁺] et [Br⁻] si le solide est présent.

**Correction guidée**

Le bilan de différence donne [Ag⁺]=[Br⁻]. Leur produit vaut Ks, donc les deux valent 10⁻⁶ mol·L⁻¹ dans l’approximation idéale.

## 71. Potentiel au point équivalent

Spé · Laboratoire `dosage_potentiometrique`

Avec E°Ag⁺/Ag=0,800 V, pKs=12 et T=298,15 K, calculer E à l’équivalence.

**Correction guidée**

log₁₀ aAg⁺=−pKs/2=−6. E=0,800+0,059159×(−6)≈0,4450 V. La valeur est finie ; une expression simplifiée valable loin de l’équivalence ne doit pas être prolongée jusqu’à ce point.

## 72. Contrôler un bilan avant l’équivalence

Sup / spé · Laboratoire `dosage_potentiometrique`

Avec c=0,1 mol·L⁻¹ et r=0,8, donner les totaux dilués et l’excès de bromure.

**Correction guidée**

cAg=0,1×0,8/1,8≈0,044444 et cBr=0,1/1,8≈0,055556 mol·L⁻¹. Leur différence vaut −0,011111. Si le solide existe, [Br⁻]−[Ag⁺]=0,011111 ; cette égalité reste exacte dans le modèle à Ks fini.
