# Chaleur & Transferts — 90 exercices corrigés

## 01. Section, courant et puissance

Sup · Laboratoire `fourier_barre`

Une barre a L=0,5 m, S=20 cm², λ=80 W/(m·K), T₁=80°C et T₂=20°C. Calculer j, Φ et R.

**Correction guidée**

S=0,002 m². j=80×60/0,5=**9 600 W/m²**. Φ=jS=**19,2 W**. R=L/(λS)=**3,125 K/W**. Vérification : RΦ=60 K. Confondre cm² et m² produirait un facteur 10 000.

## 02. Changer le matériau

Sup · Laboratoire `fourier_barre`

À géométrie et températures fixées, remplacer λ=80 par λ=0,04 W/(m·K). Comment changent le profil, la puissance et la résistance ?

**Correction guidée**

Le profil T(x) reste la droite déterminée par les bords. La puissance est divisée par 2 000 et la résistance multipliée par 2 000. Dans l’exemple précédent, Φ=**0,0096 W** et R=**6 250 K/W**. Un même profil ne signifie pas un même transfert.

## 03. Retrouver le régime permanent à partir du premier principe

Spé · Laboratoire `fourier_barre`

Écrire le bilan d’un tronçon dx, avec capacité volumique ρc constante, puis obtenir l’équation de chaleur.

**Correction guidée**

Le stockage vaut ρcSdx ∂T/∂t. La puissance reçue est S[j(x)−j(x+dx)]≈−Sdx∂j/∂x. Ainsi ρc∂T/∂t=−∂j/∂x. Fourier donne **∂T/∂t=χ∂²T/∂x²**, χ=λ/(ρc). En permanent, T″=0, ce qui retrouve le laboratoire.

## 04. Brique et isolant

Sup → Spé · Laboratoire `paroi_composite`

Sur S=10 m² : e₁=0,2 m, λ₁=0,8 ; e₂=0,1 m, λ₂=0,04 ; hᵢ=8 et hₑ=20, en unités SI. Tint=20°C, Text=−5°C. Calculer la perte.

**Correction guidée**

Les résistances valent 0,0125 ; 0,025 ; 0,25 ; 0,005 K/W. Leur somme est **0,2925 K/W**. Φ=25/0,2925≈**85,47 W**, soit 8,55 W/m². L’isolant représente 85,47 % de la résistance totale.

## 05. Une surface extérieure différente de l’air

Sup · Laboratoire `paroi_composite`

Avec les données précédentes, déterminer les températures de surface intérieure et extérieure.

**Correction guidée**

La surface intérieure est à 20−Φ/(hᵢS)≈**18,93°C**. La surface extérieure est à −5+Φ/(hₑS)≈**−4,57°C**. Ces écarts permettent justement les échanges convectifs. La température d’interface des solides vaut 20−Φ(0,0125+0,025)≈16,79°C.

## 06. Un pont thermique en parallèle

Spé · Laboratoire `paroi_composite`

Un mur et un pont thermique ont respectivement Rmur=0,3 K/W et Rpont=2 K/W. Ils sont soumis au même écart de 24 K. Calculer la puissance totale et comparer à la somme des résistances.

**Correction guidée**

Les puissances valent 24/0,3=80 W et 24/2=12 W. Le total est **92 W**, et Réquiv=24/92≈**0,261 K/W**. Additionner 0,3+2 serait traiter les passages en série, ce qui est faux ici : ils relient directement les mêmes deux ambiances.

## 07. Deux rayons critiques

Spé · Laboratoire `isolation_radiale`

Avec λ=0,1 W/(m·K) et h=4 W/(m²·K), calculer les rayons critiques. Pour Rᵢ=2 cm, quelles épaisseurs les atteignent ?

**Correction guidée**

Le cylindre a Rcrit=**2,5 cm**, la sphère **5 cm**. À rayon intérieur 2 cm, les épaisseurs correspondantes sont 0,5 cm et 3 cm. Si Rᵢ était 10 cm, aucun de ces minima ne serait accessible par ajout d’isolant.

## 08. Puissance constante et courant non constant

Sup → Spé · Laboratoire `isolation_radiale`

Une sphère transmet 50 W. Comparer j à r=0,1 m et à r=0,2 m.

**Correction guidée**

j=Φ/(4πr²). Les valeurs sont environ **397,9 W/m²** et **99,47 W/m²**. Le courant surfacique est divisé par quatre lorsque le rayon double. La puissance traversant chaque sphère reste bien 50 W.

## 09. Limite d’une coque mince

Spé · Laboratoire `isolation_radiale`

Pour une sphère, montrer que la résistance tend vers e/(λSᵢ) lorsque e=Rₑ−Rᵢ est petit devant Rᵢ.

**Correction guidée**

Rsph=e/[4πλRᵢ(Rᵢ+e)]. Pour e/Rᵢ≪1, remplacer Rᵢ+e par Rᵢ au premier ordre : **Rsph≈e/(4πλRᵢ²)=e/(λSᵢ)**. L’approximation plane est donc locale et suppose une faible variation de surface.

## 10. Épaisseur conditionnelle dans de la neige

Spé · Laboratoire `igloo`

R=1 m, λ=0,15 W/(m·K), P=100 W, Text=−20°C. Quelle épaisseur le modèle demanderait-il pour Tint=15°C ? Interpréter.

**Correction guidée**

ΔT=35 K. e=35/[100/(2π×0,15)−35]≈**0,492 m**. C’est une valeur du modèle conductif constant. La surface intérieure y dépasserait 0°C : il faut intégrer la fonte, les échanges avec l’air et les autres pertes pour annoncer un équilibre réel de neige solide.

## 11. Même puissance dans de la glace dense

Spé · Laboratoire `igloo`

Avec R=1 m, λ=2 W/(m·K), P=100 W et Text=−20°C, peut-on atteindre 15°C par ajout d’épaisseur dans le même modèle ?

**Correction guidée**

La hausse maximale vaut P/(2πλR)≈**7,96 K**. La température limite du modèle est donc environ −12,04°C, inférieure à 15°C. Le dénominateur de l’épaisseur demandée serait négatif ; **aucune épaisseur positive ne convient** dans ce modèle à rayon intérieur fixe.

## 12. Passer de la sphère à la demi-sphère

Sup → Spé · Laboratoire `igloo`

Pour les mêmes rayons et températures, comparer la puissance transmise par une sphère complète et une hémisphère, sol isolé.

**Correction guidée**

La surface de transfert hémisphérique est la moitié de celle de la sphère. La résistance est donc doublée et la puissance divisée par deux. Cette conclusion suppose que les surfaces planes de fermeture n’échangent pas ; ajouter un transfert par le sol demanderait un passage en parallèle.

## 13. Le premier temps de relaxation

Spé · Laboratoire `diffusion_1d`

Avec L=0,2 m et χ=10 mm²/s, calculer le temps de décroissance par e du premier mode.

**Correction guidée**

χ=10⁻⁵ m²/s. Le temps vaut L²/(π²χ)=0,04/(π²×10⁻⁵)≈**405,3 s**. Celui du troisième mode est neuf fois plus court, environ 45,03 s.

## 14. Une maille plus fine impose un pas plus court

Spé · Laboratoire `diffusion_1d`

Pour χ=10⁻⁵ m²/s et Δx=5 mm, quel pas maximal assure r≤1/2 ? Que devient-il si Δx est divisée par deux ?

**Correction guidée**

Δt≤Δx²/(2χ)=25×10⁻⁶/(2×10⁻⁵)=**1,25 s**. Diviser Δx par deux divise le pas maximal par quatre : **0,3125 s**. Le coût augmente à la fois dans le nombre de points et le nombre de pas.

## 15. Prévoir le lissage sans simulation

Spé · Laboratoire `diffusion_1d`

Le profil initial vaut A[sin(πx/L)+0,4sin(3πx/L)]. Trouver le rapport d’amplitudes des deux modes au temps t.

**Correction guidée**

Le rapport rang 3 / rang 1 vaut **0,4 exp(−8π²χt/L²)**. Il tend vers zéro. La forme devient donc proportionnelle au premier sinus longtemps avant que toute la barre revienne à T₀.

## 16. Multiplier le temps par quatre

Sup → Spé · Laboratoire `demi_espace`

Que deviennent la longueur de pénétration, le flux de surface et l’énergie reçue lorsque t est multiplié par quatre ?

**Correction guidée**

√χt est multipliée par **2**, le flux proportionnel à t⁻¹ᐟ² est divisé par **2**, et l’énergie proportionnelle à √t est multipliée par **2**. Ces lois d’échelle valent à paramètres de matériau et températures fixés.

## 17. Dimension d’une énergie par surface

Sup → Spé · Laboratoire `demi_espace`

Vérifier l’unité de ρcΔT√χt. Pourquoi ne s’agit-il pas d’une énergie totale ?

**Correction guidée**

ρc est en J/(m³·K), ΔT en K et √χt en m : le produit est en **J/m²**. Le problème est invariant dans le plan de la surface. Pour une région d’aire S où cette approximation est valable, multiplier par S donne l’énergie totale.

## 18. Retrouver le bilan par une intégrale d’erfc

Spé · Laboratoire `demi_espace`

Montrer ∫₀∞erfc(u)du=1/√π, puis retrouver l’énergie du profil.

**Correction guidée**

Intégrer par parties : le bord u erfc(u) s’annule et erfc′=−2e⁻ᵘ²/√π. L’intégrale vaut (2/√π)∫₀∞ue⁻ᵘ²du=**1/√π**. Poser x=2√χt u dans ∫ρc(T−T₀)dx donne 2ρcΔT√χt/√π, comme l’intégrale temporelle du flux.

## 19. Pénétration journalière

Spé · Laboratoire `onde_thermique`

Avec χ=1 mm²/s et P=86 400 s, calculer δ. Quelle amplitude reste à z=0,2 m si A=10 K ?

**Correction guidée**

χ=10⁻⁶ m²/s. δ=√(χP/π)≈**0,166 m**. L’amplitude vaut 10exp(−0,2/δ)≈**2,99 K**. La profondeur de 20 cm réduit déjà fortement le cycle journalier.

## 20. Rapport entre saison et journée

Sup → Spé · Laboratoire `onde_thermique`

À matériau fixé, trouver le rapport des profondeurs caractéristiques annuelle et journalière.

**Correction guidée**

Les périodes sont dans le rapport 365,25. Les profondeurs sont donc dans le rapport **√365,25≈19,11**. Pour χ=10⁻⁶ m²/s, δannuelle≈3,17 m.

## 21. Atténuation et retard au même point

Spé · Laboratoire `onde_thermique`

À z=δ, exprimer le retard comme fraction de la période et l’amplitude comme fraction de l’amplitude de surface.

**Correction guidée**

Le retard vaut 1/ω=P/(2π), soit **15,92 % d’une période**. L’amplitude vaut **1/e≈36,79 %** de celle de surface. Les deux résultats viennent du même exposant complexe, mais ont des significations différentes.

## 22. La bonne longueur de Biot

Sup → Spé · Laboratoire `refroidissement_biot`

Une plaque de 20 mm d’épaisseur a λ=80 W/(m·K), h=20 W/(m²·K) et ρc=2 MJ/(m³·K). Calculer Bi et le temps capacitif.

**Correction guidée**

a=10 mm=0,01 m. Bi=ha/λ=**0,0025**, favorable au modèle uniforme. Le temps capacitif vaut ρca/h=**1 000 s**. Employer l’épaisseur totale doublerait les deux résultats alors que les deux faces échangent.

## 23. Pourquoi Bi petit donne le modèle capacitif

Spé · Laboratoire `refroidissement_biot`

Pour Bi≪1, utiliser μtanμ=Bi sur le premier mode pour retrouver le facteur de décroissance uniforme.

**Correction guidée**

Pour μ petit, μtanμ≈μ², donc μ₁²≈Bi et son coefficient tend vers 1. Le facteur exp(−μ₁²χt/a²) devient exp[−Biχt/a²]=**exp[−ht/(ρca)]**. Les modes plus rapides corrigent les petits gradients internes.

## 24. Une surface froide ne signifie pas un centre froid

Sup → Spé · Laboratoire `refroidissement_biot`

À Bi grand, quel point refroidit d’abord ? Quelle température faut-il employer dans le bilan d’énergie totale ?

**Correction guidée**

Les surfaces échangent directement avec l’air et refroidissent d’abord. L’énergie totale est proportionnelle à **la moyenne volumique** de T, pas à sa valeur de surface ni seulement à celle du centre. Le laboratoire trace les trois pour distinguer les grandeurs.

## 25. Doubler une largeur et conserver l’énergie

Sup → Spé · Laboratoire `diffusion_2d`

Si la largeur σ d’une tache 2D double sans changer Q, que devient son maximum ?

**Correction guidée**

Le maximum est Q/(2πρceσ²) : il est divisé par **quatre**. Les aires caractéristiques sont multipliées par quatre. L’énergie totale reste Q, même si le pic est beaucoup plus bas.

## 26. Variance radiale d’une tache

Spé · Laboratoire `diffusion_2d`

σ₀=10 mm, χ=2 mm²/s et t=120 s. Calculer σ et ⟨r²⟩.

**Correction guidée**

σ²=100+2×2×120=**580 mm²**, donc σ≈**24,08 mm**. La moyenne radiale vaut **1 160 mm²**. Le carré de largeur par direction et la moyenne du rayon au carré sont distincts.

## 27. Vérifier la normalisation de la gaussienne

Spé · Laboratoire `diffusion_2d`

Intégrer l’élévation gaussienne sur le plan en coordonnées polaires et vérifier son énergie.

**Correction guidée**

Avec r²=x²+y² et dxdy=rdrdθ, l’intégrale de ρceΔT vaut Q/(2πσ²)×2π∫₀∞r exp(−r²/(2σ²))dr. Poser u=r²/(2σ²), donc rdr=σ²du. L’intégrale vaut **Q∫₀∞e⁻ᵘdu=Q**.

## 28. Le coefficient du recueil

Sup → Spé · Laboratoire `marche_aleatoire`

Une marche sans biais saute de 1 µm toutes les 1 ms. Calculer D et la variance après 100 pas.

**Correction guidée**

D=ε²/(2τ)=10⁻¹²/(2×10⁻³)=**5×10⁻¹⁰ m²/s**. Après t=0,1 s, la variance 2Dt vaut **100 µm²** ; l’écart-type est 10 µm.

## 29. Un biais crée deux phénomènes

Sup → Spé · Laboratoire `marche_aleatoire`

Avec p=0,7, ε=1 µm, τ=1 ms et N=100, calculer moyenne et variance.

**Correction guidée**

La moyenne est N(2p−1)ε=**40 µm**. La variance est 4Np(1−p)ε²=**84 µm²**. La dérive vaut 400 µm/s et D=4,2×10⁻¹⁰ m²/s. La variance se calcule autour de 40 µm, pas autour de l’origine.

## 30. Le facteur de parité dans la gaussienne

Spé · Laboratoire `marche_aleatoire`

Pourquoi une densité gaussienne multipliée par ε sous-estime-t-elle la probabilité d’un site accessible après N sauts ?

**Correction guidée**

Les sites accessibles sont séparés par **2ε**, car le nombre de sauts positifs change la position de 2ε. La probabilité approchée est donc densité×2ε. Employer ε la diviserait par deux et donnerait une somme approchée proche de 1/2.

## 31. Diffusion d’une particule dans l’eau

Spé · Laboratoire `brownien_langevin`

Pour a=500 nm, η=1 mPa·s et T=300 K, calculer D. On prend kB=1,380649×10⁻²³ J/K.

**Correction guidée**

α=6π×10⁻³×5×10⁻⁷≈9,425×10⁻⁹ kg/s. Donc D≈**4,395×10⁻¹³ m²/s**. À long temps, après 0,1 s, le déplacement quadratique par direction vaut environ **0,0879 µm²**.

## 32. Contrôler les deux limites

Spé · Laboratoire `brownien_langevin`

Développer la formule du MSD pour t≪τᵥ et donner un équivalent pour t≫τᵥ.

**Correction guidée**

1−e⁻ᵗ/τᵥ=t/τᵥ−t²/(2τᵥ²)+… . La différence entre crochets vaut t²/(2τᵥ)+… ; le MSD vaut **(D/τᵥ)t²=(kBT/m)t²**. À long temps, la correction constante −2Dτᵥ devient négligeable devant **2Dt**.

## 33. Une mesure 2D ne donne pas le MSD 1D

Sup → Spé · Laboratoire `brownien_langevin`

Dans une image plane, on mesure la moyenne de x²+y². Quel coefficient relie cette mesure au temps dans le régime diffusif ?

**Correction guidée**

Chaque variance vaut 2Dt, donc **⟨x²+y²⟩=4Dt**. Le coefficient de diffusion est le même dans les deux directions. Employer la formule 2Dt sur la distance plane ferait surestimer D d’un facteur deux.

## 34. Dimension et longueur d’absorption

Sup → Spé · Laboratoire `absorption_neutrons`

D=20 cm²/s et τ=0,2 s. Calculer L. Vérifier l’unité de Q/(Dr).

**Correction guidée**

D=0,002 m²/s. L=√(0,002×0,2)=**0,02 m=2 cm**. Q/(Dr) a unité s⁻¹/[(m²/s)m]=**m⁻³**, celle d’une densité.

## 35. Combien sont absorbés avant L ?

Spé · Laboratoire `absorption_neutrons`

À r=L, déterminer la fraction du débit source absorbée à l’intérieur.

**Correction guidée**

Le débit restant est Q(1+1)e⁻¹=2Q/e. La fraction absorbée vaut **1−2/e≈26,42 %**. L n’est donc pas le rayon où la plupart des neutrons ont déjà été absorbés.

## 36. Nombre présent à l’équilibre

Spé · Laboratoire `absorption_neutrons`

Intégrer n sur le volume pour retrouver Qτ.

**Correction guidée**

4πr²n=Qr e⁻ʳ/ᴸ/D. Son intégrale vaut (Q/D)L²∫₀∞u e⁻ᵘdu=**QL²/D=Qτ**. La source peut être ponctuelle tout en produisant un nombre intégré fini.

## 37. Diffusivités égales

Sup → Spé · Laboratoire `diffusion_electrolyte`

Que donnent Damb, E et la jonction si D₊=D₋=D ?

**Correction guidée**

**Damb=D**, E=0 et la différence de potentiel est nulle. Les deux ions ont déjà le même flux diffusif −Dn′ ; aucune migration ne doit les rééquilibrer.

## 38. Coefficient et signe d’une jonction

Spé · Laboratoire `diffusion_electrolyte`

D₊=1,3×10⁻⁹ et D₋=2×10⁻⁹ m²/s, T=300 K, cD/cG=5. Déterminer Damb et le signe de Vdroite−Vgauche.

**Correction guidée**

Damb=2×1,3×2/(1,3+2)×10⁻⁹≈**1,576×10⁻⁹ m²/s**. Comme D₋−D₊>0 et ln5>0, la différence de potentiel est positive. Avec kBT/e≈25,85 mV, elle vaut environ **8,83 mV**.

## 39. Vérifier le flux commun

Spé · Laboratoire `diffusion_electrolyte`

Substituer le champ dans Γ₊ pour retrouver la diffusion ambipolaire.

**Correction guidée**

Γ₊=−D₊n′+D₊(D₊−D₋)n′/(D₊+D₋). Réunir les termes donne −D₊[(D₊+D₋)−(D₊−D₋)]n′/(D₊+D₋)=**−2D₊D₋n′/(D₊+D₋)**. Le même calcul pour l’anion donne exactement ce flux.

## 40. Deux corps isolés

Sup → Spé · Laboratoire `entropie_diffusion`

Deux capacités égales C=1 000 J/K sont initialement à 353,15 K et 293,15 K. Donner la température finale et l’entropie produite.

**Correction guidée**

La température finale vaut **323,15 K, soit 50°C**. Le gain est C ln[323,15²/(353,15×293,15)]≈**8,66 J/K**, positif. Utiliser les températures en °C dans le logarithme serait incorrect.

## 41. Production instantanée d’une interface

Spé · Laboratoire `entropie_diffusion`

Avec G=10 W/K, Ti=350 K et Tj=300 K, calculer la puissance et la production d’entropie.

**Correction guidée**

La puissance vers le froid est 10×50=**500 W**. La production vaut G×50²/(350×300)≈**0,2381 W/K**. Le flux peut être signé mais la production reste positive.

## 42. Entropie nulle et état initial uniforme

Sup → Spé · Laboratoire `entropie_diffusion`

Que prédit le système si toutes les cellules commencent à la même température ? Vérifier le bilan local et le gain final.

**Correction guidée**

Toutes les différences entre voisines sont nulles : chaque dérivée Tᵢ′ est nulle. La production instantanée et le gain total valent **zéro**. L’uniformité est le mode conservé ; aucune redistribution ni irréversibilité n’est créée.

## 43. Même détente isotherme, deux réalisations

Sup · Laboratoire `travail_chemins`

Une mole idéale à 300 K double son volume. Calculer le travail réversible et celui d’une détente contre la pression extérieure finale constante Pext=RT/(2V₁). Les deux états finaux sont à 300 K. Quelle réalisation crée de l’entropie ?

**Correction guidée**

Wrév=−RT ln2≈−1,729 kJ. Pour Pext constante, Wirrév=−Pext(V₂−V₁)=−RT/2≈−1,247 kJ. Dans les deux cas ΔU=0 et Q=−W. ΔS=R ln2 ; l’entropie créée avec un thermostat à 300 K vaut ΔS−Q/T=**R(ln2−1/2)>0** dans le second cas, et 0 dans le cas réversible.

## 44. Reconnaître une adiabatique dans la famille polytropique

Sup → Spé · Laboratoire `travail_chemins`

Pour une mole idéale, γ=1,4, T₁=300 K et V₂/V₁=2. Évaluer T₂, W et Q lorsque k=γ. Vérifier le signe du travail.

**Correction guidée**

T₂=300·2^(−0,4)≈227,36 K. cV=R/0,4 et W=cV(T₂−T₁)≈**−1,510 kJ**. Comme l’évolution est adiabatique réversible, Q=0. Le travail est négatif pendant la détente ; l’énergie interne diminue. La relation ΔS=cV ln(T₂/T₁)+R ln2 confirme ΔS=0.

## 45. Ne pas confondre une aire avec une fonction d’état

Sup · Laboratoire `travail_chemins`

Pour r=2 et k=1,4, comparer les travaux des chemins « isochore puis isotherme finale » et « isotherme initiale puis isochore ». Lequel fournit le plus de travail ?

**Correction guidée**

T₂<T₁. Les travaux sont Wa=−RT₂ ln2 et Wb=−RT₁ ln2, donc Wb<Wa<0. Le second chemin fournit plus de travail, car la détente isotherme se fait à une pression plus élevée. **ΔU est identique** pour les deux chemins ; Qa=ΔU−Wa et Qb=ΔU−Wb sont différents. La différence d’aires est compensée par celle des chaleurs échangées.

## 46. Créer une surface ou étirer un fil

Sup · Laboratoire `travaux_generalises`

Une interface liquide de tension σ=0,072 N/m gagne 20 cm². Un fil de raideur k=200 N/m passe d’un allongement de 1 cm à 3 cm. Calculer les deux travaux reçus.

**Correction guidée**

20 cm²=2·10⁻³ m², donc Wsurface=σΔA=**1,44·10⁻⁴ J**. Pour le fil, W=k(xf²−xi²)/2=100(0,03²−0,01²)=**0,080 J**. Un film ayant deux faces exigerait de compter la variation des deux aires. L’expression FfinaleΔx serait incorrecte pour le fil, car sa force varie avec x.

## 47. Décharger un condensateur réversiblement

Sup · Laboratoire `travaux_generalises`

Un condensateur de 2 µF passe de 10 V à 2 V. Quel est le travail reçu par le condensateur ? Quelle énergie peut-il restituer dans le modèle idéal ?

**Correction guidée**

La variation d’énergie est C(uf²−ui²)/2=10⁻⁶(4−100)=**−96 µJ**. Le travail reçu est négatif ; il peut restituer 96 µJ. Dans une décharge résistive, cette énergie devient de la chaleur dans la résistance. La restitution idéale ne signifie donc pas qu’un montage de décharge arbitraire récupère tout sous forme de travail utile.

## 48. Flux lié et énergie magnétique

Sup → Spé · Laboratoire `travaux_generalises`

Une bobine idéale a L=40 mH et I=0,5 A. Calculer le flux lié et son énergie. Retrouver l’énergie en intégrant I dλ.

**Correction guidée**

λ=LI=0,020 Wb et E=LI²/2=**5,0 mJ**. Comme I=λ/L, l’intégrale depuis 0 vaut ∫₀^λ(λ′/L)dλ′=λ²/(2L), même valeur. Le symbole λ désigne le flux lié à toutes les spires ; employer le flux d’une seule spire sans facteur du nombre de spires changerait le résultat.

## 49. Équilibre sans ressort

Sup → Spé · Laboratoire `potentiel_helmholtz`

Une mole à 300 K est répartie en 0,4 mol à gauche et 0,6 mol à droite dans 20 L. Le ressort est retiré. Trouver les volumes d’équilibre et la pression commune.

**Correction guidée**

La condition PG=PD donne VG/VD=nG/nD=2/3. Avec VG+VD=20 L, **VG=8 L et VD=12 L**. La pression est nRT/Vtot=8,314·300/0,020≈**1,247 bar**. Les deux volumes sont différents même si les pressions et températures sont égales.

## 50. Énergie libre perdue pendant une relaxation

Spé · Laboratoire `potentiel_helmholtz`

Sans ressort, pour nG=0,4 et nD=0,6, exprimer F(yᵢ)−F(yéq) si yᵢ=0,75. Quelle entropie est créée si le système relaxe sans travail utile ?

**Correction guidée**

yéq=0,4. La différence vaut −RT[0,4 ln(0,75/0,4)+0,6 ln(0,25/0,6)]≈**683 J** à 300 K. Elle est positive et constitue de l’énergie libre disponible. Sans travail extérieur utile, Scréée=[Finitial−Ffinal]/T≈**2,28 J/K**. Si un travail était récupéré, le bilan devrait le compter et l’entropie créée serait plus faible.

## 51. Quand les pressions ne sont plus égales

Spé · Laboratoire `potentiel_helmholtz`

Avec un ressort, l’équilibre peut-il satisfaire PG≠PD ? Donner la relation et expliquer pourquoi il reste stable.

**Correction guidée**

Le bilan est (PG−PD)A=ksL(yéq−ys). Une différence de pression est donc compatible avec l’équilibre si elle compense la force du ressort. La courbure **F″=RT[nG/y²+nD/(1−y)²]+ksL²** est strictement positive : une petite déviation augmente F. La condition de pression commune n’est valable que si aucune autre force n’agit sur la cloison.

## 52. Une constante d’équilibre donne une composition

Spé · Laboratoire `potentiel_gibbs`

Pour A⇌B idéal et une mole totale, K=4. Quelle est la fraction de B à l’équilibre ? Quel est ΔrG° à 300 K ?

**Correction guidée**

x/(1−x)=4 donne **x=4/5=0,8**. ΔrG°=−RT lnK≈**−3,458 kJ/mol**. Le signe négatif du terme standard favorise B, mais l’équilibre n’est pas un état B pur : l’entropie de mélange fixe une fraction intérieure.

## 53. Changer la température inverse le sens standard

Spé · Laboratoire `potentiel_gibbs`

On prend ΔrH°=−6 kJ/mol et ΔrS°=−10 J/(mol·K). Trouver la température où K=1, puis le sens standard favorisé à 300 et 700 K.

**Correction guidée**

ΔrG°=−6000+10T en J/mol, nul à **600 K**. À 300 K, il vaut −3000 J/mol, donc K>1 et B est majoritaire à l’équilibre. À 700 K, il vaut +1000 J/mol, donc K<1 et A est majoritaire. Le sens spontané à une composition donnée exige toutefois ΔrG=ΔrG°+RT ln(xB/xA), pas seulement ΔrG°.

## 54. Les standards équivalents n’imposent pas un mélange arbitraire

Spé · Laboratoire `potentiel_gibbs`

Si ΔrG°=0, déterminer le minimum de G. Une composition initiale xB=0,1 évolue-t-elle vers B ou vers A ?

**Correction guidée**

La condition RT ln[x/(1−x)]=0 donne **x=1/2**. À x=0,1, la pente est RT ln(1/9)<0 : augmenter la quantité de B diminue G. Les potentiels standards égaux ne rendent pas toutes les compositions équivalentes, car le terme d’entropie de mélange possède un minimum à la coexistence égale.

## 55. Deux corps et un calorimètre non négligeable

Sup · Laboratoire `calorimetrie_entropie`

Un corps chaud a une capacité de 1000 J/K à 330 K, un froid 500 J/K à 270 K, et le calorimètre 100 J/K à 330 K. Trouver Tf et la chaleur gagnée par le froid.

**Correction guidée**

Tf=(1100·330+500·270)/1600=**311,25 K**. Le corps froid reçoit Qf=500(311,25−270)=**20,625 kJ**. Le corps chaud et l’appareil perdent ensemble la même énergie. Négliger Ccal donnerait 310 K : le calorimètre fait partie du système et du bilan.

## 56. Un mélange final au point de fusion

Sup → Spé · Laboratoire `calorimetrie_entropie`

Un kilogramme d’eau à Tm+20 K reçoit 0,5 kg de glace à Tm, sans calorimètre. Quelle masse de glace fond ? Quelle est la température finale ?

**Correction guidée**

Le refroidissement de l’eau jusqu’à Tm fournit 4180·20=83 600 J. Fondre toute la glace exigerait 0,5·334000=167000 J, donc elle ne fond qu’en partie. La masse fondue vaut 83600/334000≈**0,2503 kg**. Il reste environ 0,2497 kg de glace et la température finale est **273,15 K**.

## 57. Déterminer L dans un TP de fusion

Sup · Laboratoire `calorimetrie_entropie`

Une masse m de glace à Tm est ajoutée à de l’eau de masse M à Ti>Tm dans un calorimètre de capacité Ccal. Toute la glace fond et Tf>Tm. Établir la formule donnant L à partir des mesures.

**Correction guidée**

Le chaud perd (Mceau+Ccal)(Ti−Tf). La glace reçoit mL pour fondre puis mceau(Tf−Tm) pour chauffer. Donc **L=[(Mceau+Ccal)(Ti−Tf)−mceau(Tf−Tm)]/m**. Une glace initialement sous Tm demanderait en plus mcglace(Tm−Tglace). Omettre cette étape ou la capacité du calorimètre biaise la mesure.

## 58. Une détente adiabatique qui crée de l’entropie

Sup · Laboratoire `detentes_joule`

Une mole parfaite double son volume dans une enceinte isolée. Donner ΔU, ΔT et ΔS. Comparer à une détente adiabatique réversible qui double aussi le volume.

**Correction guidée**

Dans le vide, ΔU=0, donc **ΔT=0 et ΔS=R ln2≈5,763 J/K**. Cette entropie est entièrement créée. En adiabatique réversible, ΔS=0 et T₂/T₁=2^(1−γ)<1 : le gaz fournit du travail et refroidit. Les deux transformations ont Q=0 mais des travaux et des états finaux différents.

## 59. Attraction et refroidissement dans le vide

Spé · Laboratoire `detentes_joule`

Pour a=0,3 Pa·m⁶/mol², cV=2,5R, vi=2 L/mol et vf=6 L/mol, calculer Tf−Ti dans une détente libre van der Waals. Attention aux unités de volume.

**Correction guidée**

vi=0,002 et vf=0,006 m³/mol. Donc ΔT=(0,3/(2,5R))(1/0,006−1/0,002)≈**−4,81 K**. Une conversion oubliée des litres aurait divisé cette variation par 1000. Le refroidissement découle ici de u constante ; il ne s’agit pas d’un coefficient de Joule–Thomson.

## 60. Lire correctement un coefficient de Joule–Thomson

Spé · Laboratoire `detentes_joule`

Dans une petite chute de pression de 2 bar, μJT vaut −0,20 K/bar et varie peu. Quel est le signe de ΔT ? Pourquoi l’approche locale n’est-elle pas suffisante pour une grande détente ?

**Correction guidée**

ΔP=−2 bar, donc ΔT≈μJTΔP=**+0,40 K** : le gaz se réchauffe. Pour une grande variation, μJT change avec l’état et peut même changer de signe. Il faut suivre la ligne d’enthalpie constante, intégrer le coefficient avec son évolution, ou résoudre h(T,v)=hi comme dans le laboratoire.

## 61. Rendement et chaleur rejetée

Sup · Laboratoire `carnot_ditherme`

Un moteur réversible échange avec des sources à 600 et 300 K. Il reçoit 10 kJ du chaud. Donner son travail reçu et la chaleur reçue depuis le froid.

**Correction guidée**

η=1−300/600=0,5. Le travail reçu est **W=−5 kJ** et le bilan donne **Qf=−5 kJ**. L’entropie échangée 10000/600−5000/300 est nulle. Les 5 kJ rejetés ne sont pas une perte due à un défaut technique : même une machine réversible doit rejeter de la chaleur.

## 62. Deux COP pour les mêmes sources

Sup · Laboratoire `carnot_ditherme`

Une machine réversible fonctionne entre 270 et 300 K et reçoit 1 kJ de travail. Donner ses COP frigorifique et de pompe à chaleur, puis Qf et Qc.

**Correction guidée**

COPf=270/30=**9** et COPc=300/30=**10**. Elle reçoit Qf=9 kJ et rejette 10 kJ, donc Qc=−10 kJ. Le bilan est 1+9−10=0. La relation COPc−COPf=1 exprime exactement la contribution du travail.

## 63. Mesurer les irréversibilités d’un moteur

Sup → Spé · Laboratoire `carnot_ditherme`

Entre 600 et 300 K, un moteur reçoit Qc=10 kJ mais ne fournit que 3 kJ. Calculer Qf et l’entropie créée par cycle.

**Correction guidée**

W=−3 kJ, donc Qf=−7 kJ. Scréée=−Qc/Tc−Qf/Tf=−10000/600+7000/300=**6,667 J/K**. Le rendement 0,3 est inférieur à Carnot 0,5. Le déficit de performance et la création d’entropie sont deux lectures du même second principe.

## 64. Otto : une efficacité indépendante de la chaleur ajoutée

Sup → Spé · Laboratoire `cycles_moteurs`

Pour un cycle Otto avec r=8 et γ=1,4, calculer le rendement. Si z=T₃/T₂ augmente sans modifier r ni γ, le rendement idéal change-t-il ?

**Correction guidée**

η=1−8^(−0,4)≈**0,5647**. À r et γ fixés, le rendement idéal ne dépend pas de z ; chaleur reçue et travail fourni augmentent dans le même rapport. En pratique, z accroît la température et les contraintes, ce que le modèle à capacités constantes ne prend pas en compte.

## 65. Diesel : vérifier la limite d’un chauffage très bref

Spé · Laboratoire `cycles_moteurs`

Dans la formule du rendement Diesel, faire tendre z vers 1. Pourquoi la limite ressemble-t-elle à Otto sans être un cycle produisant un travail fini ?

**Correction guidée**

(z^γ−1)/(γ(z−1)) tend vers 1 par dérivation ou développement limité. Le rendement tend vers **1−r^(1−γ)**. Mais Qchaud=cP(T₃−T₂) tend vers 0 et le travail également : le cycle s’effondre. Une limite de rendement ne signifie pas une production d’énergie finie.

## 66. Le régénérateur change la chaleur externe, pas l’aire du cycle

Spé · Laboratoire `cycles_moteurs`

Dans Stirling avec Tf=300 K, Tc=480 K, r=8 et γ=1,4, comparer les rendements sans régénérateur et avec un régénérateur parfait.

**Correction guidée**

Le travail fourni vaut R·180 ln8≈**3112 J/mol**. Avec un régénérateur parfait, Qchaud=R·480 ln8≈8299 J/mol et η=1−300/480=**0,375**. Sans régénérateur, ajouter cV·180≈3742 J/mol : Qchaud≈12041 J/mol et η≈**0,2585**. Les deux diagrammes P,V sont identiques ; les échanges externes diffèrent.

## 67. Pression intermédiaire optimale

Spé · Laboratoire `compresseur_etages`

L’air passe de 1 à 16 bar avec deux étages identiques et refroidissement intermédiaire à 300 K. Donner la pression intermédiaire optimale et les rapports de pression des étages.

**Correction guidée**

Pintermédiaire=√(1·16)=**4 bar**. Les rapports sont 4 et 4. Une moyenne arithmétique 8,5 bar ne donne pas le minimum, car la contrainte est multiplicative. Avec ηs=1, le travail vaut 2cP·300[4^(2/7)−1]≈**292,9 kJ/kg**, inférieur au travail d’un seul étage.

## 68. Fermer le bilan global d’énergie

Spé · Laboratoire `compresseur_etages`

Deux étages reçoivent chacun 100 kJ/kg. Le refroidisseur rejette 100 kJ/kg entre eux. Quelle est la variation d’enthalpie entre l’entrée globale et la sortie finale ?

**Correction guidée**

Le travail total reçu est 200 kJ/kg et la chaleur reçue est −100 kJ/kg. Donc **Δh=w+q=100 kJ/kg**. Les travaux de pression sont déjà inclus dans Δh. La sortie finale est chaude parce qu’on ne la refroidit pas dans le modèle ; le rejet intermédiaire ne supprime que l’augmentation d’enthalpie du premier étage.

## 69. La limite de nombreux étages

Spé · Laboratoire `compresseur_etages`

Démontrer la limite de wmin lorsque N tend vers l’infini. Que change un rendement isentropique ηs<1 constant ?

**Correction guidée**

Rtot^(a/N)=exp(a lnRtot/N)=1+a lnRtot/N+o(1/N). Ainsi wmin→cPT₁a lnRtot/ηs=**rairT₁lnRtot/ηs**. Pour ηs=1, c’est le travail isotherme réversible. Si ηs<1 reste constant, la limite est plus élevée : multiplier les étages n’efface pas ce modèle de pertes internes.

## 70. Énergie libérée et travail maximal

Spé · Laboratoire `exergie_corps`

Un corps de capacité 1000 J/K refroidit de 600 à 300 K dans un environnement à 300 K. Comparer l’énergie perdue par le corps et le travail maximal.

**Correction guidée**

Le corps perd 1000·300=**300 kJ**. Le travail maximal est 1000[300−300ln2]≈**92,06 kJ**. La différence, environ 207,94 kJ, est rejetée à l’environnement dans la réalisation réversible. Transformer les 300 kJ intégralement en travail violerait le bilan d’entropie.

## 71. Une réserve froide peut produire du travail

Spé · Laboratoire `exergie_corps`

Un corps à 180 K, de capacité 1000 J/K, est plongé dans un environnement à 300 K. Calculer son exergie et le sens de la chaleur reçue depuis l’environnement dans le cas réversible.

**Correction guidée**

B=1000[−120−300ln(0,6)]≈**33,25 kJ**. Le corps gagne ΔU=120 kJ ; pour fournir ce travail, l’ensemble reçoit Q=ΔU+B≈**153,25 kJ** de l’environnement. Le corps froid sert de source froide à une machine : la chaleur reçue dépasse l’énergie stockée, et la différence est le travail fourni.

## 72. Une faible différence de température

Spé · Laboratoire `exergie_corps`

Pour Ti=T₀+δT avec |δT|≪T₀, établir un équivalent de l’exergie. L’équivalent distingue-t-il un corps un peu chaud d’un corps un peu froid ?

**Correction guidée**

Avec z=δT/T₀, ln(1+z)=z−z²/2+o(z²). Donc B=CT₀[z−ln(1+z)]∼**CδT²/(2T₀)**. Le terme dominant est le même pour les deux signes de δT. La capacité à produire du travail existe des deux côtés de l’équilibre et disparaît quadratiquement lorsque l’écart se réduit.

## 73. Rapport des signaux du TP

Sup · Laboratoire `cube_leslie`

Deux faces identiques en aire et en température ont ε₁=0,90 et ε₂=0,05. Elles sont observées avec la même thermopile, à même distance. Quel rapport U₁/U₂ prévoit-on ? Que se passe-t-il à T=Tₐ ?

**Correction guidée**

Les facteurs σ, A, G, η et T⁴−Tₐ⁴ se simplifient : **U₁/U₂=ε₁/ε₂=18**, si le signal net n’est pas nul. À T=Tₐ, U₁=U₂=0 : le quotient mesuré est indéfini. Le rapport des émissivités reste 18.

## 74. Pourquoi soustraire le rayonnement ambiant ?

Sup · Laboratoire `cube_leslie`

Une face d’aire A=0,01 m² et d’émissivité ε=0,95 est à T=373 K dans une pièce à Tₐ=293 K. Estimer la puissance radiative nette. Peut-on utiliser directement des températures en °C ?

**Correction guidée**

La loi donne **Pᵣ≈6,46 W**. Le rayonnement reçu de la pièce représente environ 3,97 W : le négliger surestime l’échange net. Les puissances quatrièmes portent sur des **températures absolues en kelvins** ; employer 100 et 20 °C serait incorrect.

## 75. Temps de refroidissement près de l’ambiance

Spé · Laboratoire `cube_leslie`

Un cube de côté a=0,10 m possède six faces d’émissivité 0,90. Prendre Tₐ=300 K, h=10 W·m⁻²·K⁻¹ et Cₜₕ=1000 J/K. Linéariser le bilan sans chauffage et calculer le temps caractéristique.

**Correction guidée**

La conductance radiative vaut 4σTₐ³×6×0,90×a²≈0,331 W/K ; celle de convection vaut 6ha²=0,600 W/K. Ainsi H≈0,931 W/K et **Cₜₕ/H≈1074 s, soit 17,9 min**. L’écart de température suit approximativement une exponentielle décroissante.

## 76. Retrouver une température avec S constant

Sup · Laboratoire `seebeck`

Un thermocouple a S=40 µV/K. Sa jonction froide est à 293,15 K et sa tension vaut +5,20 mV. Déterminer la température chaude avec la convention du laboratoire.

**Correction guidée**

Th−Tf=V/S=5,20×10⁻³/(40×10⁻⁶)=130 K. Donc **Th=423,15 K, soit 150 °C**. Supposer à tort une jonction froide à 273,15 K donnerait 403,15 K.

## 77. Intégrer plutôt que multiplier

Spé · Laboratoire `seebeck`

Prendre Tᵣ=273,15 K, S₀=40 µV/K et s₁=0,02 µV/K². Pour Tf=293,15 K et Th=473,15 K, comparer la tension exacte à S₀(Th−Tf).

**Correction guidée**

Le terme constant vaut 7,20 mV. La correction vaut 0,02[(200)²−(20)²]/2 µV=396 µV. La tension intégrée est donc **7,596 mV**. L’approximation omet environ 5,2 % de cette tension.

## 78. Propager une erreur de référence

Spé · Laboratoire `seebeck`

Les coefficients locaux valent S(Tf)=40 µV/K et S(Th)=44 µV/K. La jonction froide est surestimée de δTf=2 K. Quel biais de température prévoit la linéarisation ?

**Correction guidée**

À tension inchangée, S(Th)δTh≈S(Tf)δTf. Ainsi **δTh≈(40/44)×2=1,82 K**, positif. La compensation exacte du laboratoire inclut les termes non linéaires.

## 79. Vérifier un bilan sur des nombres simples

Sup → Spé · Laboratoire `peltier`

Prendre Tc=280 K, Th=300 K, α=0,05 V/K, R=2 Ω, K=1 W/K et I=4 A. Calculer Qc, Qh, P et le COP.

**Correction guidée**

Qc=56−16−20=**20 W** ; Qh=60+16−20=**56 W** ; P=4+32=**36 W**. On retrouve 56=20+36. Le COP vaut **20/36≈0,556**, bien inférieur à Tc/(Th−Tc)=14.

## 80. Un maximum n’est pas une garantie de refroidissement

Spé · Laboratoire `peltier`

À températures fixées, démontrer le courant qui maximise Qc. En déduire une condition nécessaire et suffisante pour qu’il existe un courant avec Qc>0 dans le modèle non limité en courant.

**Correction guidée**

La dérivée est αTc−RI, donc **Ioptimal=αTc/R**. Le maximum vaut **α²Tc²/(2R)−KΔT**. Un refroidissement est possible exactement si ce maximum est strictement positif. Une limite technique de courant peut encore restreindre les possibilités.

## 81. Charge et température d’équilibre

Spé · Laboratoire `peltier`

Th=300 K, α=0,05 V/K, R=2 Ω, K=1 W/K et I=4 A. Une charge de 10 W arrive au côté froid. Trouver Tc à l’équilibre et vérifier Qc.

**Correction guidée**

Tc=(10+16+300)/(0,20+1)=**271,667 K**. Alors Qc=0,20Tc−16−(300−Tc)=1,20Tc−316=**10 W**. La température froide est bien inférieure à Th. L’évacuation de Qh côté chaud reste indispensable.

## 82. Retrouver le son adiabatique

Spé · Laboratoire `thermoacoustique`

Dans la relation quadratique du cours, poser λ=0. Déterminer k² et le rapport τ₀/p₀. Pourquoi la branche thermique ne reste-t-elle pas une seconde racine finie ?

**Correction guidée**

La relation devient iωρ₀cₚ(k²−ω²/c²)=0, d’où **k²=ω²/c²** et k=ω/c pour une propagation vers x>0. Le rapport vaut **1/(ρ₀cₚ)=(γ−1)T₀/(γP₀)**. Le coefficient de k⁴ s’annule : l’équation perd un degré et l’autre racine part à l’infini.

## 83. Le signe de l’atténuation dépend de la convention

Spé · Laboratoire `thermoacoustique`

Avec la convention exp(iωt−ikx), prendre k=20−0,03i m⁻¹. Quelle fraction d’amplitude reste après 50 m ? Quel signe faudrait-il avec exp(iωt+ikx) pour la même atténuation vers x>0 ?

**Correction guidée**

L’amplitude est multipliée par exp(−0,03×50)=**exp(−1,5)≈0,223**. Avec exp(iωt+ikx), l’enveloppe est exp(−Im(k)x) : il faudrait alors **Im(k)>0**. Toujours développer l’exponentielle avant d’imposer un signe.

## 84. Faible conduction : vérifier une approximation

Spé · Au-delà · Laboratoire `thermoacoustique`

Noter β=−Im(k) l’atténuation et supposer λω/(ρ₀cₚc²)≪1. En développant k² près de ω²/c², montrer β≈λ(γ−1)ω²/(2ρ₀cₚc³). Quel effet prévoit-on si l’on double la fréquence ?

**Correction guidée**

Écrire q=ω²/c²+δq dans le polynôme et ne garder que le premier ordre en λ : δq=−iλ(γ−1)ω³/(ρ₀cₚc⁴). Puis k≈ω/c+δq c/(2ω), d’où la formule annoncée. **β est multipliée par 4** si f double dans ce régime. La résolution exacte permet de vérifier les limites de l’approximation.

## 85. Deux contraintes électriques, deux raideurs

Spé · Laboratoire `piezo_resonateur`

À partir de U(x,q), comparer la raideur lorsque q=0 et lorsque V est imposée. Avec k=10⁶ N/m, C=10⁻⁹ F et θ=0,01 C/m, quelle est la raideur à charge nulle ?

**Correction guidée**

À q=0, U=(k+θ²/C)x²/2 : la raideur vaut **1,10×10⁶ N/m**. À tension imposée, le potentiel U−Vq après élimination de q a pour dérivée seconde en x **k=10⁶ N/m**. Mélanger les variables fixées ferait perdre cette différence.

## 86. Résonance et antirésonance d’un mode

Spé · Laboratoire `piezo_resonateur`

m=2×10⁻⁴ kg, k=10⁶ N/m, C=10⁻⁹ F et θ=0,01 C/m. Calculer fᵣ et fₐ sans pertes. Quel rapport permet de déterminer θ²/(kC) ?

**Correction guidée**

fᵣ=√(k/m)/(2π)≈**11,254 kHz**. Comme θ²/(kC)=0,10, fₐ=fᵣ√1,10≈**11,803 kHz**. Le rapport donne **θ²/(kC)=(fₐ/fᵣ)²−1**. L’écart entre ces repères mesure le couplage du modèle.

## 87. Vérifier la passivité par un bilan de puissance

Spé · Laboratoire `piezo_resonateur`

Poser D=k−mω²+iωr et x₀=θV₀/D. Montrer que Re(Y)≥0 et que V₀²Re(Y)/2=rω²|x₀|²/2.

**Correction guidée**

En multipliant par le conjugué de D, **Re(Y)=θ²rω²/[(k−mω²)²+(rω)²]** est positive. Or |x₀|²=θ²V₀²/|D|² : les deux puissances sont identiques. Le signe positif provient du frottement r>0 ; il contrôle la cohérence du couplage.

## 88. Garder une même base d’unités

Sup → Spé · Laboratoire `brouillard`

La chaleur latente massique de l’eau vaut environ 2,44×10⁶ J/kg. La masse molaire vaut M=0,018 kg/mol. Convertir la chaleur latente et la constante R en grandeurs molaires. Quel rapport doit rester inchangé ?

**Correction guidée**

L molaire vaut ML≈**43 920 J/mol** ; R molaire vaut MR≈**8,307 J·mol⁻¹·K⁻¹** avec la constante arrondie du modèle. Le rapport **L/R** est identique dans les deux bases. Employer 8,314 avec 2,44×10⁶ J/kg mélangerait les unités.

## 89. Prévoir le début pour une vapeur d’eau

Spé · Laboratoire `brouillard`

Prendre T*=293,15 K, L*=2,44×10⁶ J/kg, R=461,5 J·kg⁻¹·K⁻¹ et γ=1,33. Comparer les deux pentes logarithmiques à T*. Que prévoir lors d’une faible détente ?

**Correction guidée**

La pente de saturation est L*/(RT*²)≈**0,0615 K⁻¹**. La pente isentropique vaut γ/[(γ−1)T*]≈**0,01375 K⁻¹**. Pour dT<0, la saturation décroît plus vite : **la condensation commence**. Il ne faut pas continuer la loi de gaz parfait seul dans le mélange.

## 90. Retrouver l’intégrale et vérifier son signe

Spé · Laboratoire `brouillard`

Intégrer d ln Pₛₐₜ/dT=A/(RT²)−B/(RT) entre T* et T. Vérifier la valeur en T=T* et le sens de variation si A−BT>0.

**Correction guidée**

Une primitive est −A/(RT)−(B/R)ln T. La différence donne **−(A/R)(1/T−1/T*)−(B/R)ln(T/T*)**, nulle à T=T*. Si L(T)=A−BT>0, d ln Pₛₐₜ/dT>0 : la pression de saturation augmente avec T. Les deux termes intégrés doivent être considérés ensemble.
