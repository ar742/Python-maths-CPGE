# Mécanique & Mouvements — 72 exercices corrigés

## 01. Une comète : comparer les deux vitesses extrêmes

Sup · Laboratoire `orbite_kepler`

Une comète décrit une ellipse d’excentricité e=0,8. Exprimer le rapport vp/va entre les vitesses au péricentre et à l’apocentre. Faut-il connaître la masse de l’étoile ?

**Correction guidée**

Aux deux extrémités, la vitesse est tangentielle. La conservation de h donne rp vp=ra va. Comme rp=a(1−e) et ra=a(1+e), **vp/va=(1+e)/(1−e)=9**. La masse de l’étoile intervient dans chaque vitesse, mais se simplifie dans leur rapport.

## 02. Changer la taille de l’orbite

Sup → Spé · Laboratoire `orbite_kepler`

À masse centrale fixée, une deuxième planète a un demi-grand axe quatre fois plus grand. Comparer les périodes et les énergies spécifiques. L’excentricité change-t-elle ces rapports ?

**Correction guidée**

T²∝a³ donne T₂/T₁=4³ᐟ²=**8**. Comme ε=−GM/(2a), ε₂=ε₁/4 : l’énergie devient moins négative. Ces deux résultats ne dépendent pas de l’excentricité tant que les trajectoires restent elliptiques et la masse centrale identique.

## 03. Retrouver l’énergie avec les conditions au péricentre

Spé · Laboratoire `orbite_kepler`

On connaît rp et vp à un péricentre. Donner ε, h, a et e, puis la condition pour obtenir une ellipse. On suppose vp supérieur ou égal à la vitesse circulaire locale.

**Correction guidée**

ε=vp²/2−GM/rp et h=rp vp. Une ellipse exige ε<0, donc vp<√(2GM/rp). Le demi-grand axe vaut a=−GM/(2ε), puis e=1−rp/a. La condition vp≥√(GM/rp) garantit que rp est bien le rayon minimal. À égalité, e=0 ; en dessous, le point initial serait l’apocentre.

## 04. Localiser le centre de masse d’un système binaire

Sup · Laboratoire `deux_corps`

À un instant, deux étoiles de masses 3m et m sont séparées de 4 unités de longueur. Donner leurs distances à G. Si la séparation décrit une ellipse de demi-grand axe 2, quels sont a₁ et a₂ ?

**Correction guidée**

Les distances à G sont inversement proportionnelles aux masses : l’étoile de masse 3m est à **1** et celle de masse m à **3**. Pour l’ellipse relative, a₁=(1/4)×2=0,5 et a₂=(3/4)×2=1,5. Le centre de masse est le foyer commun de leurs deux ellipses.

## 05. Mesurer une masse totale avec une orbite

Spé · Laboratoire `deux_corps`

Une binaire a une séparation de demi-grand axe a=2 UA et une période T=2 ans. Déterminer sa masse totale dans les unités du laboratoire. Pourquoi une seule période ne détermine-t-elle pas les deux masses séparément ?

**Correction guidée**

Avec G=4π², T²=a³/M ; donc **M=8/4=2 masses solaires**. Cette équation porte sur la somme m₁+m₂. Il faut une information supplémentaire, par exemple le rapport a₁/a₂=m₂/m₁ ou celui des vitesses, pour séparer les deux masses.

## 06. Une énergie dépendante du référentiel

Spé · Laboratoire `deux_corps`

Un système binaire isolé de masse totale M passe devant un observateur avec vitesse VG. Exprimer son énergie mécanique dans ce référentiel en fonction de son énergie E* dans le référentiel de G. Pourquoi la forme de l’orbite relative ne change-t-elle pas ?

**Correction guidée**

Le changement galiléen ajoute **½M VG²** à l’énergie cinétique totale ; la séparation et l’énergie potentielle ne changent pas. Ainsi E=E*+½M VG². L’équation de la séparation dépend uniquement de r₂−r₁ : elle conserve la même conique et la même période.

## 07. Lire une ellipse avec un lancement tangent

Sup → Spé · Laboratoire `potentiel_effectif`

Dans les unités GM=r₀=1, prendre η=1,2. Déterminer ε, e, le demi-grand axe et les rayons extrêmes.

**Correction guidée**

ε=(1,44−2)/2=**−0,28**, e=1,44−1=**0,44** et a=−1/(2ε)=25/14≈1,786. Le lancement est au péricentre rp=1. L’apocentre vaut ra=a(1+e)=18/7≈2,571. Vérifier rp+ra=2a et p=h²=1,44.

## 08. Une orbite circulaire est-elle un minimum d’énergie ?

Spé · Laboratoire `potentiel_effectif`

À moment cinétique h fixé, déterminer le rayon et l’énergie de l’orbite circulaire dans un champ GM/r². Interpréter la dérivée seconde du potentiel effectif.

**Correction guidée**

Ueff′=−h²/r³+GM/r² s’annule en rc=h²/(GM). On y trouve εc=−(GM)²/(2h²) et Ueff″(rc)=(GM)⁴/h⁶>0 : c’est un minimum à h fixé. Une petite perturbation radiale produit une oscillation de fréquence √(GM/rc³), et non un retour amorti vers le cercle.

## 09. Une condition initiale trop lente

Spé · Laboratoire `potentiel_effectif`

Le lancement est tangent à r₀=1, avec η=1/2 et GM=1. Le point initial est-il un péricentre ? Calculer le rayon minimal et expliquer pourquoi le centre n’est pas atteint.

**Correction guidée**

ε=−7/8 et e=3/4. Le point initial est l’apocentre. Le paramètre p=h²=1/4 donne **rmin=p/(1+e)=1/7**, tandis que rmax=p/(1−e)=1. Comme h≠0, Ueff tend vers +∞ en zéro : une énergie finie ne permet pas d’atteindre le centre.

## 10. Doubler le rayon orbital

Spé · Laboratoire `transfert_hohmann`

Dans les unités GM=r₁=1, transférer un véhicule vers r₂=2. Calculer les deux impulsions et la durée du trajet.

**Correction guidée**

a=3/2. Au départ, vt₁=√(2−2/3)=2/√3 et vc₁=1, d’où Δv₁=2/√3−1≈0,155. À l’arrivée, vt₂=√(1−2/3)=1/√3 et vc₂=1/√2, d’où Δv₂≈0,130. Le coût vaut environ **0,284** et τ=π(3/2)³ᐟ²≈5,77 unités de temps.

## 11. Omettre la seconde impulsion

Sup → Spé · Laboratoire `transfert_hohmann`

Un transfert sortant atteint l’apocentre r₂. Si le moteur ne fonctionne plus, le véhicule reste-t-il sur l’orbite circulaire cible ? Justifier par l’énergie ou la vitesse.

**Correction guidée**

Non : vt₂²=GM(2/r₂−2/(r₁+r₂)) est inférieur à vc₂²=GM/r₂ lorsque r₂>r₁. Le véhicule est trop lent pour une orbite circulaire à ce rayon. Son énergie et son moment cinétique restent ceux de l’ellipse : il repart vers son péricentre r₁.

## 12. Préparer un rendez-vous avec la planète cible

Spé · Prolongement · Laboratoire `transfert_hohmann`

Dans un transfert sortant, la demi-ellipse dure τ et la planète cible tourne à vitesse angulaire n₂ constante. Donner l’angle initial qui permet un rendez-vous au bout du transfert, puis expliquer pourquoi il faut attendre une fenêtre de départ.

**Correction guidée**

Fixer l’angle du véhicule à zéro au départ. Son arrivée a lieu à π. La planète doit satisfaire φ₀+n₂τ=π modulo 2π ; donc **φ₀=π−n₂τ**. Les deux planètes n’ont pas la même vitesse angulaire : leur angle relatif varie, et la condition ne se reproduit qu’à intervalles correspondant à leur période synodique.

## 13. Une déviation de 90°

Spé · Laboratoire `diffusion_gravitationnelle`

Déterminer b pour obtenir une déviation δ=π/2 à vitesse v∞ fixée dans le champ d’un astre de paramètre GM. Calculer l’excentricité correspondante.

**Correction guidée**

tan(δ/2)=GM/(bv∞²). Pour δ=π/2, tan(π/4)=1 ; donc **b=GM/v∞²**. Alors e=√2. Le péricentre vaut rp=(GM/v∞²)/(1+√2), plus petit que le paramètre d’impact b.

## 14. La norme de la vitesse est-elle conservée ?

Sup → Spé · Laboratoire `diffusion_gravitationnelle`

Une sonde possède vitesse lointaine v∞ et passe au rayon minimal rp. Exprimer sa vitesse vp au péricentre. Pourquoi retrouve-t-elle v∞ lorsqu’elle repart loin ?

**Correction guidée**

La conservation de ε donne vp²/2−GM/rp=v∞²/2, soit **vp=√(v∞²+2GM/rp)**. Elle accélère à l’approche, puis ralentit en s’éloignant. Quand r tend vers l’infini, le potentiel tend vers zéro et la vitesse retrouve la norme v∞.

## 15. Borner le gain d’énergie d’un survol

Spé · Prolongement · Laboratoire `diffusion_gravitationnelle`

La déviation vaut δ et les deux vitesses relatives ont norme v∞. Montrer que |ΔEc|/m≤2Vv∞sin(δ/2). Quand la borne peut-elle être atteinte ?

**Correction guidée**

La différence uout−uin est la corde entre deux vecteurs de même norme : sa norme vaut 2v∞sin(δ/2). Cauchy–Schwarz donne |V·(uout−uin)|≤V|uout−uin|, d’où la borne. L’égalité est obtenue lorsque V est parallèle ou antiparallèle à cette différence, selon le signe recherché.

## 16. Changer la distance : attraction ou marée ?

Sup · Laboratoire `marees`

À masse extérieure et taille du corps fixes, doubler D. Comment varient l’accélération du centre et l’accélération de marée au premier ordre ?

**Correction guidée**

L’accélération du centre vaut GM/D² : elle est divisée par **4**. La marée radiale est 2GMx/D³ : elle est divisée par **8**. Confondre attraction et différence d’attraction ferait donc prévoir la mauvaise loi d’échelle.

## 17. Les deux côtés du corps ne sont pas parfaitement symétriques

Spé · Laboratoire `marees`

Développer Δax=GM[(D−x)⁻²−D⁻²] à l’ordre deux en x/D. Comparer les valeurs en x=R et x=−R.

**Correction guidée**

(1−u)⁻²=1+2u+3u²+o(u²). Donc Δax=2GMx/D³+3GMx²/D⁴+o(x²). Le terme linéaire est impair ; le terme quadratique est positif des deux côtés. La face proche subit un étirement un peu plus fort que la face éloignée, à même distance R du centre.

## 18. Une échelle de dislocation et ses limites

Spé · Prolongement · Laboratoire `marees`

Un corps de masse m et de rayon R passe près d’un astre de masse M=100m. Estimer D/R lorsque la marée linéaire devient comparable à sa gravité propre. Cette estimation démontre-t-elle sa rupture ?

**Correction guidée**

Égaliser 2GMR/D³ et Gm/R² donne D/R=(2M/m)¹ᐟ³=200¹ᐟ³≈**5,85**. C’est un ordre de grandeur, pas un critère exact : rotation, propriétés mécaniques et dynamique de la déformation ne sont pas incluses. On vérifie aussi que R/D≈0,17 est seulement modérément petit.

## 19. Quelle quantité de carburant pour un gain donné ?

Sup → Spé · Laboratoire `fusee`

Dans le vide sans pesanteur, une fusée a vitesse d’éjection u=3 km/s et doit gagner Δv=6 km/s. Déterminer m₀/mf et la fraction de la masse initiale qui doit être éjectée.

**Correction guidée**

Δv/u=ln(m₀/mf)=2, donc **m₀/mf=e²≈7,39**. La fraction éjectée vaut 1−mf/m₀=1−e⁻²≈86,5 %. Le logarithme explique pourquoi un gain de vitesse élevé devient coûteux en masse.

## 20. Peut-elle commencer par monter ?

Sup · Laboratoire `fusee`

Une fusée démarre avec vitesse nulle. Donner une condition sur la poussée F, la masse initiale m₀ et g pour que l’accélération initiale soit ascendante. Traduire-la avec le rapport χ=m₀/mf et la durée τ.

**Correction guidée**

Il faut **F>m₀g**. Comme q=m₀(1−1/χ)/τ et F=uq, la condition est u(1−1/χ)/τ>g. Si elle n’est pas satisfaite, le modèle sans sol prévoit d’abord une descente ; pour un lancement depuis un sol, une réaction du support doit alors être ajoutée.

## 21. Réduire la durée de combustion

Spé · Laboratoire `fusee`

Deux combustions ont les mêmes m₀, mf et u, mais des durées τ et τ/2. Comparer leurs vitesses finales sous pesanteur uniforme, puis leurs poussées.

**Correction guidée**

Le gain idéal u ln(m₀/mf) est identique. La seconde combustion perd seulement gτ/2, donc sa vitesse finale dépasse la première de **gτ/2**. Sa masse éjectée est identique en deux fois moins de temps : le débit, donc la poussée uq, est doublé.

## 22. Vérifier les signes du produit vectoriel

Sup → Spé · Laboratoire `coriolis`

Un observateur tourne avec Ω>0 autour de z. À un instant, le point a position (r,0,0) et vitesse relative (v,0,0), avec r,v>0. Donner les directions des forces centrifuge et de Coriolis.

**Correction guidée**

Ω×vR=(0,Ωv,0), donc Fcor=(0,−2mΩv,0), vers les y négatifs. Ω×(Ω×r)=(−Ω²r,0,0), donc Fcent=(mΩ²r,0,0), vers les x positifs. Le terme centrifuge est radial vers l’extérieur ; Coriolis est perpendiculaire à la vitesse.

## 23. Conserver une énergie dans les axes tournants

Spé · Laboratoire `coriolis`

Montrer que J=½m|vR|²−½mΩ²|r|² est constant pour un point libre et Ω constant.

**Correction guidée**

Multiplier la dynamique tournante par vR. Le terme de Coriolis a un produit scalaire nul ; il reste d(½m|vR|²)/dt=mΩ²r·vR=d(½mΩ²|r|²)/dt. En soustrayant, **dJ/dt=0**. La constance de Ω est nécessaire pour cette forme du bilan.

## 24. Un point immobile vu depuis des axes tournants

Spé · Laboratoire `coriolis`

Dans le référentiel galiléen, un point est immobile à la distance r du centre. Quelles sont sa vitesse et son accélération dans les axes tournants ? Pourquoi la force centrifuge seule ne donne-t-elle pas le résultat ?

**Correction guidée**

vR=−Ω×r et aR=−Ω²r : les coordonnées décrivent un cercle en sens opposé aux axes. Le terme centrifuge vaut +Ω²r, mais Coriolis vaut −2Ω²r. Leur somme est bien −Ω²r. Omettre Coriolis inverserait donc le sens de l’accélération relative.

## 25. Chaîne périodique : établir la dispersion

Sup → Spé · Laboratoire `chaine_atomique`

N masses m, espacées de a, sont reliées par des ressorts k. Pour uⱼ=Ueⁱ⁽κja−ωt⁾, établir les valeurs permises de κ et la relation de dispersion. Interpréter q=0.

**Correction guidée**

Le PFD donne m üⱼ=k(uⱼ₊₁+uⱼ₋₁−2uⱼ). La périodicité impose eⁱκNa=1, donc κ=2πq/(Na), q entier modulo N. Après substitution, mω²=k(2−2cosκa)=4k sin²(κa/2), d’où ω=2√(k/m)|sin(κa/2)|. Pour q=0, uⱼ est indépendant de j : aucune liaison n’est allongée, et le mode est une translation. À vitesse nulle, le déplacement commun reste constant.

## 26. Combien de modes et quelle énergie ?

Spé · Laboratoire `chaine_atomique`

Pourquoi q et N−q ont-ils la même fréquence sans rendre tous leurs mouvements identiques ? Montrer que la somme des énergies cinétique et élastique est conservée.

**Correction guidée**

Les facteurs e²ⁱπqj/N et e⁻²ⁱπqj/N sont conjugués. Leurs combinaisons réelles donnent un cosinus et un sinus spatiaux de même fréquence ; sauf les cas q=0 et, pour N pair, q=N/2, ce sont deux directions indépendantes dans l’espace des déplacements. Pour E=½m∑u̇ⱼ²+½k∑(uⱼ₊₁−uⱼ)², dériver puis décaler les indices dans la somme périodique : dE/dt=∑u̇ⱼ[m üⱼ−k(uⱼ₊₁+uⱼ₋₁−2uⱼ)]=0. Chaque ressort est compté une fois.

## 27. Vitesse de groupe et précision du milieu continu

Spé → Au-delà · Laboratoire `chaine_atomique`

Pour 0<κa<π, calculer la vitesse de groupe. Trouver le premier écart relatif entre la pulsation exacte et cκ pour κa petit.

**Correction guidée**

ω=2√(k/m)sin(κa/2), donc dω/dκ=a√(k/m)cos(κa/2)=c cos(κa/2). Le développement sin s=s−s³/6+… donne ω=cκ[1−(κa)²/24+O((κa)⁴)]. L’écart relatif à la pulsation linéaire vaut donc (κa)²/24 au premier ordre. La limite continue dépend de la longueur d’onde, pas seulement d’un nombre N élevé.

## 28. CO₂ : retrouver les modes sans calculer un déterminant

Spé · Laboratoire `molecule_co2`

Pour trois masses mO,mC,mO et deux liaisons k, tester les formes (1,1,1), (1,0,−1) et (1,b,1). Déterminer leurs pulsations et b.

**Correction guidée**

La première forme annule K : ω=0. Pour (1,0,−1), Ka=k a et Ma=mO a, donc ω₁²=k/mO. Pour le troisième mode non nul, le centre de masse est fixe : 2mO+mC b=0, donc b=−2mO/mC. La première ligne Ka=ω²Ma donne k(1−b)=ω²mO, donc ω₂²=k/mO+2k/mC. Les trois formes sont indépendantes et couvrent les trois coordonnées longitudinales.

## 29. Pourquoi diagonaliser une matrice symétrique ?

Spé · Laboratoire `molecule_co2`

Le problème est Ka=ω²Ma avec M positive diagonale. Le transformer en un problème symétrique et démontrer l’orthogonalité des modes de fréquences différentes.

**Correction guidée**

Poser b=M¹ᐟ²a donne D b=ω²b, D=M⁻¹ᐟ²KM⁻¹ᐟ². Comme K est symétrique, D l’est aussi. Pour deux modes, aᵢᵀKaⱼ=ωⱼ²aᵢᵀMaⱼ et, par symétrie, aᵢᵀKaⱼ=ωᵢ²aᵢᵀMaⱼ. Si ωᵢ²≠ωⱼ², aᵢᵀMaⱼ=0. C’est cette orthogonalité pondérée qui supprime les termes croisés dans l’énergie.

## 30. Carbone 13 : quelle raie se déplace ?

Spé · Laboratoire `molecule_co2`

On remplace ¹²C par ¹³C sans changer k ni les oxygènes ¹⁶O. Calculer le rapport des deuxièmes fréquences et identifier le mode inchangé.

**Correction guidée**

ω₁²=k/(16u) est inchangé. Pour le mode avec carbone mobile, ω₂²=(k/u)(1/16+2/mC), où mC vaut 12 ou 13 en unités u. Le rapport ω₂(13)/ω₂(12)=√[(1/16+2/13)/(1/16+2/12)]≈0,9716. La fréquence baisse d’environ 2,84 %. Le déplacement des raies découle ici de la masse ; le modèle ne prédit pas leurs intensités.

## 31. Foucault : équation complexe et conditions initiales

Spé · Laboratoire `foucault`

Partir de ẍ+ω₀²x=2Ωẏ et ÿ+ω₀²y=−2Ωẋ. Résoudre avec x(0)=A,y(0)=0 et vitesse nulle, en posant z=x+iy.

**Correction guidée**

L’addition donne z̈+2iΩż+ω₀²z=0. Avec z=e⁻ⁱΩt w, on obtient ẅ+ν²w=0, ν²=ω₀²+Ω². Les conditions initiales sont w(0)=A et ẇ(0)=iΩA, donc w=A[cosνt+i(Ω/ν)sinνt]. Finalement z=Ae⁻ⁱΩt[cosνt+i(Ω/ν)sinνt]. Le facteur lent et l’oscillation rapide remplissent des rôles différents ; les deux sont nécessaires à la solution.

## 32. Un tour au Panthéon et à l’équateur

Sup → Spé · Laboratoire `foucault`

Avec λ=49° et L=67 m, estimer les périodes d’oscillation et de précession. Que devient la précession à l’équateur et dans l’hémisphère sud ?

**Correction guidée**

T₀=2π√(67/9,81)≈16,42 s. Ω=(2π/86164,0905)sin49°, donc le tour orienté complet dure 86164,0905/sin49°≈114171 s≈31,71 h. La direction non orientée d’une droite revient en la moitié de cette durée. À λ=0, Ω=0 : aucune précession dans le modèle. Au sud, sinλ est négatif, donc le sens de rotation est inversé ; sa durée positive dépend de |sinλ|.

## 33. Coriolis conserve-t-elle l’énergie ?

Spé · Laboratoire `foucault`

Montrer directement à partir des deux équations linéaires que E=½m(ẋ²+ẏ²)+½mω₀²(x²+y²) est conservée.

**Correction guidée**

Dériver : Ė=m[ẋ(ẍ+ω₀²x)+ẏ(ÿ+ω₀²y)]=m(2Ωẋẏ−2Ωẏẋ)=0. Cette annulation traduit v⃗·(Ω⃗×v⃗)=0 : Coriolis dévie la vitesse sans fournir de travail. Elle peut donc changer l’orientation du mouvement sans dissiper son énergie dans le modèle.

## 34. Pendule : passer de l’énergie à la période

Sup → Spé · Laboratoire `pendule_exact`

Un pendule est lâché à θₘ sans vitesse. Établir l’intégrale de la période et expliquer pourquoi le calcul ne dépend pas de la masse.

**Correction guidée**

La conservation de ½mL²θ̇²+mgL(1−cosθ) donne θ̇²=(2g/L)(cosθ−cosθₘ) : m se simplifie. Par symétrie, T=4∫₀^{θₘ}dθ/√[(2g/L)(cosθ−cosθₘ)]. Avec sin(θ/2)=sin(θₘ/2)sinφ, les racines de cosθ−cosθₘ se compensent dans le changement de variable, donnant T=4√(L/g)∫₀^{π/2}dφ/√[1−sin²(θₘ/2)sin²φ].

## 35. Angle maximal pour une erreur de 1 %

Sup · Laboratoire `pendule_exact`

À partir de T/T₀≈1+θₘ²/16, estimer l’angle pour lequel la correction de période atteint 1 %. Donner les unités et la portée de cette estimation.

**Correction guidée**

θₘ²/16≈0,01 donne θₘ≈0,4 rad≈22,9°. C’est une estimation à l’ordre θₘ² ; le terme suivant 11θₘ⁴/3072≈9,17×10⁻⁵ ajoute environ 0,0092 %. Pour une tolérance rigoureuse, il faut comparer à l’intégrale exacte ou encadrer les termes négligés. La substitution de 22,9 en degrés dans θₘ² aurait été incorrecte.

## 36. Grand angle et validité d’un fil

Spé · Laboratoire `pendule_exact`

Pour un lâcher sans vitesse, exprimer la tension d’un fil en fonction de θ et θₘ. Pourquoi utiliser une tige pour atteindre des amplitudes proches de π ?

**Correction guidée**

La projection radiale donne tension=mLθ̇²+mgcosθ. L’énergie donne Lθ̇²=2g(cosθ−cosθₘ), donc tension=mg(3cosθ−2cosθₘ). Au lâcher elle vaut mgcosθₘ. Si θₘ>π/2, elle serait négative : un fil ne peut transmettre cette compression et se détendrait. Une tige rigide de masse négligeable conserve alors la distance et permet l’étude de T→∞ quand θₘ→π. Il faut distinguer la liaison physique du seul dessin d’un segment.

## 37. Dériver le potentiel tronqué

Sup · Laboratoire `pendule_anharmonique`

Développer le potentiel du pendule à l’ordre 4, en déduire l’équation avec rappel cubique et préciser pourquoi elle ne constitue pas un modèle global.

**Correction guidée**

1−cosθ=θ²/2−θ⁴/24+O(θ⁶), donc V=mgL(θ²/2−θ⁴/24)+O(θ⁶). Le moment −V′=−mgL(θ−θ³/6)+O(θ⁵), et mL²θ̈=−V′ donne θ̈+(g/L)(θ−θ³/6)=0 à l’ordre retenu. Le polynôme V tronqué tend vers −∞ à grand |θ|, tandis que le potentiel exact est périodique et borné. Le développement n’a de sens qu’au voisinage de θ=0.

## 38. Coefficient de la troisième harmonique

Spé → Au-delà · Laboratoire `pendule_anharmonique`

Chercher θ=A cosτ+A³[c cosτ+d cos3τ], τ=Ωt, Ω=ω₀(1+sA²), avec θ(0)=A. Déterminer s,c,d au premier ordre utile.

**Correction guidée**

Dans θ̈+ω₀²(θ−θ³/6)=0, le terme cubique vaut A³cos³τ/6=A³(3cosτ+cos3τ)/24. L’équation au rang 1 impose −2s−1/8=0, donc s=−1/16. Au rang 3, (1−9)d−1/24=0, donc d=−1/192. La condition θ(0)=A impose c+d=0, donc c=1/192. On obtient θ=A[(1+A²/192)cosτ−(A²/192)cos3τ]. A est bien l’amplitude au point de rebroussement ; l’amplitude de la fondamentale est A(1+A²/192).

## 39. Pourquoi seulement des harmoniques impaires ?

Spé · Laboratoire `pendule_anharmonique`

Pour une oscillation symétrique autour de 0, on a θ(t+T/2)=−θ(t). Montrer que les coefficients de Fourier de rang pair sont nuls.

**Correction guidée**

Décomposer l’intégrale du coefficient en [0,T/2] et [T/2,T]. Dans la seconde partie, remplacer t par s+T/2. Le signal apporte un facteur −1 et e⁻²ⁱπnt/T apporte (−1)ⁿ. Le coefficient est proportionnel à 1−(−1)ⁿ : il s’annule si n est pair, y compris la moyenne n=0. Pour un potentiel symétrique et un mouvement entre deux points opposés, cette propriété rend le spectre impair ; une asymétrie du système pourrait produire des rangs pairs.

## 40. Deux ressorts : force et équilibres

Sup → Spé · Laboratoire `ressorts_transverses`

Deux attaches sont en (0,±L), la masse en (x,0). Établir V, la force selon x et toutes les positions d’équilibre.

**Correction guidée**

Chaque longueur vaut ℓ=√(x²+L²), donc V=2×½k(ℓ−L₀)²=k(ℓ−L₀)². Comme dℓ/dx=x/ℓ, F=−V′=−2k(1−L₀/ℓ)x. Les équilibres sont x=0 ou ℓ=L₀. Le second cas existe pour L≤L₀ et donne x=±√(L₀²−L²), deux équilibres distincts si L<L₀. À L=L₀, les trois expressions coïncident au centre et la stabilité demande le terme quartique.

## 41. Petites oscillations dans chaque puits

Spé · Laboratoire `ressorts_transverses`

Calculer V″ au centre et aux minima latéraux. En déduire les pulsations de petites oscillations et discuter la limite L→L₀.

**Correction guidée**

V″(x)=2k[1−L₀L²/(x²+L²)³ᐟ²]. Au centre, V″(0)=2k(1−L₀/L), positif si L>L₀. La pulsation centrale vaut √[2k(1−L₀/L)/m]. Aux minima latéraux ℓ=L₀, V″=2k(1−L²/L₀²), donc ωlat=√[2k(1−L²/L₀²)/m]. Ces pulsations tendent vers 0 au seuil. À amplitude finie, le modèle quartique fournit alors une période différente de celle d’une linéarisation.

## 42. Confinement ou traversée des deux puits ?

Spé · Laboratoire `ressorts_transverses`

Pour L=0,7L₀, m=1 kg, k=40 N/m et L₀=1 m, trouver la barrière centrale. Une masse lâchée sans vitesse en x=0,8 m peut-elle franchir le centre ? Et en x=1,5 m ?

**Correction guidée**

V(0)=40(1−0,7)²=3,6 J. À x=0,8 m, ℓ=√(0,64+0,49)=√1,13 et E=40(√1,13−1)²≈0,159 J : E<3,6, donc le centre est inaccessible. À x=1,5 m, ℓ=√2,74≈1,6553 et E≈17,18 J : le centre est accessible et la masse peut traverser les deux puits. La masse n’intervient pas dans ce test énergétique au lâcher ; elle intervient dans la durée du mouvement.

## 43. Un minimum sans terme quadratique

Sup · Laboratoire `oscillateur_quartique`

Au seuil L=L₀, développer le potentiel des ressorts au premier ordre non nul. Pourquoi x=0 reste-t-il stable malgré V″(0)=0 ?

**Correction guidée**

√(L₀²+x²)=L₀+x²/(2L₀)+O(x⁴), donc V=k[x²/(2L₀)+O(x⁴)]²=kx⁴/(4L₀²)+O(x⁶). Le terme dominant est pair et positif pour x≠0 : le centre est un minimum strict. La condition V″(0)>0 est suffisante pour un minimum, mais V″(0)=0 ne permet pas de conclure ; il faut regarder les termes suivants. Le premier rappel est −(k/L₀²)x³.

## 44. Période quartique par quadrature

Spé · Laboratoire `oscillateur_quartique`

Pour m ẍ=−βx³, x(0)=A>0 et ẋ(0)=0, établir la période et montrer exactement que doubler A la divise par deux.

**Correction guidée**

E=½m ẋ²+βx⁴/4=βA⁴/4, donc ẋ²=β(A⁴−x⁴)/(2m). Ainsi T=4√(2m/β)∫₀ᴬ dx/√(A⁴−x⁴)=4√(2m/β)A⁻¹∫₀¹du/√(1−u⁴). L’intégrale est indépendante de A ; T(2A)=T(A)/2. Avec u=sinφ, elle devient ∫₀^{π/2}dφ/√(1+sin²φ), ce qui facilite le calcul numérique.

## 45. Généraliser à un potentiel en x²ᵖ

Spé → Au-delà · Laboratoire `oscillateur_quartique`

Pour V(x)=a x²ᵖ, a>0 et p entier positif, prévoir la dépendance de T en l’amplitude A. Retrouver les cas harmonique et quartique.

**Correction guidée**

Au lâcher E=aA²ᵖ. Alors T=4√(m/2a)∫₀ᴬ dx/√(A²ᵖ−x²ᵖ). Poser x=Au donne T=4√(m/2a) A¹⁻ᵖ∫₀¹du/√(1−u²ᵖ). La période est indépendante de A pour p=1, harmonique. Pour p=2, elle varie comme A⁻¹. Pour p>1, elle diverge à faible amplitude ; cela traduit un rappel de plus en plus faible près du minimum plat.

## 46. Retrouver l’oscillateur forcé linéaire

Sup → Spé · Laboratoire `duffing_force`

Pour u″+2ζu′+u=f cos(rτ), établir l’amplitude établie et la pulsation de résonance en déplacement, si elle existe.

**Correction guidée**

Avec u=Re(Ueⁱʳτ), U=f/(1−r²+2iζr). Donc A=f/√[(1−r²)²+4ζ²r²]. Minimiser le dénominateur en r>0 donne rres²=1−2ζ². La résonance en déplacement existe si ζ<1/√2. Avec Q=1/(2ζ), rres=√[1−1/(2Q²)] ; la pulsation résonante n’est exactement ω₀ qu’à la limite d’un amortissement faible. Une résonance en vitesse ou en puissance n’utilise pas la même fonction à maximiser.

## 47. Balance harmonique de Duffing

Spé → Au-delà · Laboratoire `duffing_force`

En ne gardant que la fondamentale dans u³, établir l’équation en A² de la réponse approximative à u″+2ζu′+u+βu³=f cos(rτ). Peut-on conclure à la stabilité à partir de ses seules racines ?

**Correction guidée**

Écrire u≈Acos(rτ−φ) et cos³ψ=(3cosψ+cos3ψ)/4. Les projections donnent fcosφ=A(1−r²+3βA²/4) et fsinφ=2ζrA. Après élévation au carré et somme : A²[(1−r²+3βA²/4)²+(2ζr)²]=f². Avec Z=A², (9β²/16)Z³+(3β/2)(1−r²)Z²+[(1−r²)²+4ζ²r²]Z−f²=0. Les racines positives sont des réponses candidates ; la stabilité et l’erreur due au rang 3 exigent une analyse supplémentaire.

## 48. Puissances moyennes et durée du transitoire

Spé · Laboratoire `duffing_force`

Établir le bilan d’énergie réduit. Pour β=0, quel critère sur la durée d’observation permet d’attendre la disparition d’un transitoire ? Pourquoi ce seul critère ne règle-t-il pas tous les cas non linéaires ?

**Correction guidée**

E=½u′²+½u²+βu⁴/4 donne E′=fcos(rτ)u′−2ζu′². Sur une période d’une réponse établie, la moyenne de E′ est nulle, donc les puissances moyennes injectée et dissipée sont égales. Dans le cas linéaire sous-amorti, le transitoire décroît comme e⁻ζτ : attendre ζτ≫1 réduit son amplitude. Dans le cas non linéaire, plusieurs attracteurs, modulations ou relaxations lentes près d’une bifurcation peuvent exister. Il faut comparer des fenêtres successives et, au besoin, prolonger le calcul.

## 49. Quatre masses et trois inerties principales

Sup → Spé · Laboratoire `inertie_huygens`

Quatre masses identiques m sont aux points (±a,0,0) et (0,±b,0). Donner I_G et les inerties principales.

**Correction guidée**

Par symétrie, les produits d’inertie sont nuls. I_G=diag(2mb²,2ma²,2m(a²+b²)). Les axes x,y,z sont principaux. Si a>b, l’axe x minimise l’inertie. La masse totale est 4m.

## 50. Un axe décalé qui ne change pas d’inertie

Spé · Laboratoire `inertie_huygens`

On déplace le point d’attache de d parallèlement à l’axe de rotation u. Pourquoi l’inertie autour de cet axe ne change-t-elle pas ?

**Correction guidée**

Huygens donne ΔI=M|d×u|². Si d est parallèle à u, ΔI=0 : les deux points définissent le même axe géométrique, et non deux axes distincts.

## 51. Inertie d’un parallélépipède anisotrope

Spé · Laboratoire `inertie_huygens`

Un parallélépipède homogène a pour côtés a,b,c et masse M. Calculer son inertie autour de u=(1,1,1)/√3 passant par G.

**Correction guidée**

Les inerties principales valent M(b²+c²)/12, M(a²+c²)/12 et M(a²+b²)/12. Donc I(u)=M(a²+b²+c²)/18. Le vecteur u n’est pas en général un axe principal : I_Gu peut ne pas être parallèle à u.

## 52. Translation et rotation d’un cylindre

Sup · Laboratoire `konig`

Un cylindre plein de masse 2 kg et rayon 0,2 m roule à 3 m/s. Calculer les deux parts d’énergie.

**Correction guidée**

ω=v/R=15 rad/s et I_G=mR²/2=0,04 kg·m². E_translation=mv²/2=9 J ; E_rotation=I_Gω²/2=4,5 J ; E_totale=13,5 J.

## 53. Annuler le moment cinétique sans annuler l’énergie

Spé · Laboratoire `konig`

Un solide se déplace avec un moment orbital opposé à son moment propre. Peut-il avoir L_O=0 et E_c>0 ?

**Correction guidée**

Oui : L_O=L_orbital+L_G s’annule si les deux vecteurs sont opposés et de même norme. L’énergie vaut une somme de termes positifs ; elle ne s’annule que si toutes les vitesses sont nulles. Un bilan de moments cinétiques ne remplace pas un bilan d’énergie.

## 54. Pourquoi choisir le centre de masse ?

Spé · Laboratoire `konig`

Dans la décomposition des vitesses par rapport à un point A quelconque, quel terme empêche de retrouver directement König ?

**Correction guidée**

Le terme croisé vaut v_A·Σmᵢvᵢ/A. Il n’est pas nul en général. Il disparaît pour le référentiel barycentrique parce que ΣmᵢGMᵢ=0 à tout instant. Si A est fixe mais distinct de G, les autres termes doivent être conservés.

## 55. Vitesse au passage à l’horizontale

Sup · Laboratoire `barre_bascule`

Une barre de longueur 2L=1,6 m suit la trajectoire limite issue de la verticale. Déterminer θ̇ à θ=90°.

**Correction guidée**

I_O=4ML²/3 et ½I_Oθ̇²=MgL donnent θ̇=√(3g/(2L))≈4,289 rad/s. La vitesse de G vaut Lθ̇≈3,431 m/s. La masse se simplifie.

## 56. Une réaction normale peut-elle être négative ?

Spé · Laboratoire `barre_bascule`

La composante radiale de la réaction du pivot s’annule pour cosθ=3/5. La barre perd-elle alors sa liaison ?

**Correction guidée**

Non. Un pivot idéal peut tirer ou pousser ; il impose la position de O. Rᵣ change simplement de signe à θ≈53,13°. Une condition de perte de contact N=0 s’applique à une liaison unilatérale, pas à ce pivot.

## 57. Le temps dépend logarithmiquement de la perturbation

Spé · Laboratoire `barre_bascule`

Comparer les temps de θ₁ à θ₂ quand θ₁ et θ₁/10 sont petits.

**Correction guidée**

La formule exacte est Δt=2√(L/(3g)) ln[tan(θ₂/4)/tan(θ₁/4)]. Pour θ₁≪1, tan(θ₁/4)≈θ₁/4. Diviser θ₁ par 10 ajoute donc environ 2√(L/(3g)) ln 10 au temps ; on ne multiplie pas ce temps par dix.

## 58. Une expression sphérique doit conserver la longueur

Sup → Spé · Laboratoire `barre_rotule`

Avec θ colatitude et φ azimut, écrire OG et vérifier sa norme.

**Correction guidée**

OG=L(sinθcosφ,sinθsinφ,cosθ). Sa norme au carré vaut L²[sin²θ(cos²φ+sin²φ)+cos²θ]=L². Changer de convention exige de modifier toutes les composantes et les dérivées.

## 59. Le mouvement reste-t-il plan ?

Spé · Laboratoire `barre_rotule`

Si la barre est initialement dans le plan xz et possède une vitesse dans ce même plan, montrer qu’elle y reste.

**Correction guidée**

Alors n_y=ṅ_y=0. L’équation n̈=−λ(e_z−n_zn)−|ṅ|²n donne n̈_y=(λn_z−|ṅ|²)n_y=0. L’unicité de la solution maintient n_y=0. Une vitesse initiale d’azimut non nulle rompt cette condition.

## 60. Rotation conique d’une barre

Spé · Laboratoire `barre_rotule`

Pour une barre de demi-longueur L, chercher une solution θ constante, φ̇ constante non nulle.

**Correction guidée**

L’équation de θ donne sinθ[φ̇²cosθ+3g/(4L)]=0. Pour θ non vertical, φ̇²=−3g/(4Lcosθ), donc cosθ<0. Avec L=0,7 m et θ=120°, φ̇≈4,585 rad/s.

## 61. Retrouver N par la projection normale

Spé · Laboratoire `cylindre_bord`

Pendant l’adhérence au bord, partir de l’énergie et calculer la réaction N.

**Correction guidée**

Énergie : θ̇²=(4g/(3R))(1−cosθ). La projection radiale du PFD donne N−mgcosθ=−mRθ̇². Remplacer conduit à N=(mg/3)(7cosθ−4). L’expression n’est valable que tant que la cinématique d’adhérence subsiste.

## 62. Le glissement précède toujours le seuil N=0

Spé · Laboratoire `cylindre_bord`

Montrer que tout coefficient fₛ fini entraîne un seuil de glissement avant arccos(4/7).

**Correction guidée**

Sur cet intervalle, T/N=sinθ/(7cosθ−4). Il vaut 0 en θ=0 et tend vers +∞ à droite. Sa dérivée vaut (7−4cosθ)/(7cosθ−4)²>0. Une unique égalité T/N=fₛ existe donc avant N=0 pour fₛ>0.

## 63. Petit coefficient de frottement

Spé · Laboratoire `cylindre_bord`

Obtenir une approximation de l’angle de début de glissement quand fₛ≪1.

**Correction guidée**

L’équation sinθ=fₛ(7cosθ−4) donne θ≈3fₛ en radians au premier ordre. Pour fₛ=0,05, on trouve environ 0,15 rad, soit 8,6°. Une correction quadratique en θ diminue légèrement cette estimation.

## 64. Le frottement statique se règle sur la sollicitation

Sup · Laboratoire `coulomb_horizontal`

Une caisse de 4 kg repose sur un sol avec fₛ=0,4. Quelle est la réaction tangentielle sous une traction de 8 N ?

**Correction guidée**

Le seuil vaut fₛmg=15,696 N. Comme 8 N est inférieur, la caisse peut rester immobile : T=−8 N. Employer T=−fₛmg donnerait une accélération injustifiée.

## 65. Sous une force constante, dresser le bilan

Sup → Spé · Laboratoire `coulomb_horizontal`

m=2 kg, F=12 N, fₛ=0,5 et f_d=0,3. Calculer a puis la chaleur dissipée après 2 s.

**Correction guidée**

F dépasse 9,81 N. T=−5,886 N et a=3,057 m/s². Après 2 s, x=6,114 m, Q=5,886×6,114≈35,99 J ; W_F=73,368 J et E_c≈37,38 J. Leur différence est Q.

## 66. Freinage, arrêt et reprise inverse

Spé · MP · Laboratoire `coulomb_horizontal`

Une caisse de masse 2 kg est lancée à 3 m/s. fₛ=0,5 et f_d=0,3. Comparer les forces constantes F=−8 N et F=−12 N : temps et position d’arrêt, régime suivant, distance parcourue après inversion.

**Correction guidée**

Pendant le mouvement initial, T=−5,886 N. Sous −8 N, a₁=−6,943 m/s², t_a≈0,4321 s et x_a≈0,6481 m. Comme 8<9,81 N, la caisse adhère ensuite et T devient +8 N. Sous −12 N, a₁=−8,943 m/s², t_a≈0,3355 s et x_a≈0,5032 m. Puis 12>9,81 N entraîne une reprise inverse : T=+5,886 N et a₂=−3,057 m/s². Pour t>t_a, x=x_a−(3,057/2)(t−t_a)², v=−3,057(t−t_a) et la distance parcourue vaut x_a+|x−x_a|. Multiplier cette distance par 5,886 N donne Q ; vérifier Fx=½m(v²−3²)+Q.

## 67. Une caisse ne glisse pas : ne saturer pas Coulomb

Sup · Laboratoire `plan_incline`

Sur un plan d’angle 20°, m=3 kg et fₛ=0,5. Calculer N et T.

**Correction guidée**

tan20°≈0,364<0,5 : l’adhérence est possible. N=mgcos20°≈27,66 N et T=mgsin20°≈10,07 N. Le plafond fₛN≈13,83 N est supérieur à la réaction nécessaire.

## 68. Comparer les temps de descente

Spé · Laboratoire `plan_incline`

Une boule et un cerceau descendent une même distance d en roulement sans glissement. Quel est le rapport de leurs temps ?

**Correction guidée**

a_boule=(5/7)g sinα et a_cerceau=(1/2)g sinα. Avec d=at²/2, t_cerceau/t_boule=√(a_boule/a_cerceau)=√(10/7)≈1,195. Vérifier auparavant les conditions de roulement pour chacun.

## 69. Travail du frottement et absence de dissipation

Spé · Laboratoire `plan_incline`

Pour un cylindre roulant sans glissement, le travail −Tx_G sur G est négatif. Pourquoi n’y a-t-il pas de perte d’énergie mécanique ?

**Correction guidée**

Le couple en G fournit un travail +TRΔrotation. Or x_G=RΔrotation, donc la somme vaut zéro. La puissance d’une force sur le solide se calcule avec la vitesse du point où elle s’applique ; ce point est instantanément immobile en roulement sur un plan fixe.

## 70. Ne pas confondre tours par seconde et radians par seconde

Sup → Spé · Laboratoire `gyroscope`

Une toupie a m=1 kg, ℓ=0,15 m, I₃=0,0018 kg·m² et une rotation propre de 18 tr/s. Estimer sa précession lente.

**Correction guidée**

ω₃=2π×18≈113,097 rad/s. Ω_p=mgℓ/(I₃ω₃)≈7,228 rad/s, soit environ 1,150 tr/s. Le rapport Ω_p/ω₃≈0,064 renseigne sur la séparation des vitesses, sans garantir une absence de nutation.

## 71. La rotation propre constante ne rend pas L constant

Spé · Laboratoire `gyroscope`

Expliquer comment s=L·n peut être constant alors que L change de direction.

**Correction guidée**

Le couple est perpendiculaire à n et la cinématique assure L·ṅ=0. Donc d(L·n)/dt=L̇·n+L·ṅ=0. En revanche L̇=M_O est généralement non nul. La constance de la composante axiale n’implique pas celle du vecteur entier ni de sa norme.

## 72. Précession régulière : les deux branches

Au-delà · Laboratoire `gyroscope`

Une toupie conserve θ et précesse à Ω_p. Retrouver l’équation quadratique qui remplace l’approximation lente.

**Correction guidée**

Avec ṅ=Ω_p e_z×n, L=I₁Ω_p(e_z−cosθ n)+sn. Dériver L et identifier au couple mgℓ e_z×n : Ω_p(s−I₁Ω_pcosθ)=mgℓ, soit I₁cosθ Ω_p²−sΩ_p+mgℓ=0. Pour une rotation rapide, la petite racine approche mgℓ/s. La réalité des racines dépend du discriminant.
