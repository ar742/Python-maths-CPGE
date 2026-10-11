# Séries & Signaux · Cours et démonstrations

60 leçons originales, avec variables, hypothèses, preuves et applications. [Laboratoires et lancement](README.md).

## 1. Le pic mobile sépare convergence simple et uniforme

**Sup → Spé · TP : couche_limite**

**Objets et but.** Pour améliorer l’expérience de convergence de la page 99, on commence par fₙ(x)=nx/(1+n²x²) sur [0,1]. Le point x est fixé avant le passage n→∞ en convergence simple. En convergence uniforme, le point le plus défavorable peut au contraire dépendre de n. Le compact [δ,1], δ>0, permet de localiser précisément l’obstacle.

```text
fₙ(x)→0 pour chaque x∈[0,1]
fₙ′(x)=n(1−n²x²)/(1+n²x²)²
‖fₙ‖∞,[0,1]=1/2 en x=1/n ; ‖fₙ‖∞,[δ,1]≤1/(nδ)
```

**Démonstration.** En x=0 la valeur est nulle. En x>0, on a fₙ(x)≤1/(nx), donc la limite est zéro. La dérivée s’annule à 1/n et change de signe : le maximum vaut 1/2. Il ne tend pas vers zéro, donc la convergence uniforme échoue sur [0,1]. Sur [δ,1], la borne indépendante de x tend vers zéro ; la convergence y est uniforme.

**Lire l’expérience.** La variable de loupe u=nx montre fₙ(u/n)=u/(1+u²), un profil qui ne dépend pas de n. La bosse devient étroite sans perdre de hauteur. Une grille fixe peut manquer son sommet et donner l’impression d’une convergence uniforme : le maximum analytique est donc calculé indépendamment du tracé.

## 2. Les quantificateurs font la différence

**Sup → Spé · TP : couche_limite**

**Propriété ciblée.** La convergence simple laisse le rang dépendre de x ; la convergence uniforme exige un rang qui convient simultanément à tous les x du domaine. Choisir xₙ=1/n fournit un contre-exemple directement adapté à cette différence.

```text
Simple : ∀x,∀ε>0,∃N(x,ε),∀n≥N, |fₙ(x)|≤ε
Uniforme : ∀ε>0,∃N(ε),∀n≥N,∀x, |fₙ(x)|≤ε
```

**Justification.** Pour ε=1/4, aucun rang N ne peut contrôler tous les x puisque, pour chaque n≥N, xₙ=1/n donne fₙ(xₙ)=1/2. Ce point mobile ne contredit pas la convergence simple : dans cette dernière, x est fixé une fois pour toutes. Sur [δ,1], N>1/(δε) convient, ce qui exhibe un rang uniforme concret.

## 3. Une aire peut se concentrer sur un point

**Sup → Spé ; mesures au-delà · TP : concentration**

**Objets et but.** La deuxième expérience améliorée étudie fₙ(x)=n²xe^(−nx) sur [0,1]. Pour chaque x fixé la limite est zéro, mais l’aire ne disparaît pas. Ce contre-exemple oblige à vérifier les hypothèses d’une interversion limite–intégrale au lieu de se fier à une convergence visuelle.

```text
fₙ(x)→0 ; maximum=n/e en x=1/n
∫₀¹fₙ(x)dx=∫₀ⁿue^(−u)du=1−(n+1)e^(−n)→1
limn∫fₙ ≠ ∫limnfₙ
```

**Démonstration.** À x>0 fixé, l’exponentielle domine tout polynôme en n, donc n²xe^(−nx)→0. La dérivée est n²e^(−nx)(1−nx), d’où le sommet en 1/n. Le changement u=nx révèle une hauteur de l’ordre de n, une largeur de l’ordre de 1/n et une aire de l’ordre de 1. Le profil dilaté fₙ(u/n)/n=ue^(−u) conserve la masse.

**Lire l’expérience.** Le point fixe x₀ permet de distinguer croissance initiale et limite finale : une valeur peut augmenter pendant plusieurs rangs avant de décroître. La courbe d’aire est obtenue par une formule exacte, indépendante du maillage. Il ne peut exister de majorant intégrable commun, car la convergence dominée imposerait une limite d’aire nulle.

## 4. La masse limite agit comme une Dirac

**Sup → Spé ; mesures au-delà · TP : concentration**

**Propriété ciblée.** Au-delà du cours usuel de suites de fonctions, une famille peut converger comme mesure plutôt que comme fonction. Pour chaque φ continue sur [0,1], l’aire pondérée par φ tend vers φ(0).

```text
∫₀¹φ(x)fₙ(x)dx=∫₀ⁿφ(u/n)ue^(−u)du→φ(0)
∫₀^∞ue^(−u)du=1
```

**Justification.** Prolonger l’intégrande par zéro pour u>n. Pour chaque u fixé, φ(u/n) tend vers φ(0), et le module est majoré par ‖φ‖∞ue^(−u), intégrable. La convergence dominée s’applique dans la variable dilatée u, même si elle échoue avec un majorant commun dans la variable x. Cela annonce la distribution de Dirac sans lui attribuer une valeur infinie ordinaire.

## 5. Une annulation d’ordre deux améliore la série

**Spé · TP : tp99_original**

**Objets et but.** Le TP de la page 99 est conservé comme expérience complémentaire : fₙ(x)=cos(x/n)−[1+(x/n)²]^(−1/2). Les deux expressions ont la même limite 1 et le même terme quadratique. Leur différence commence à l’ordre quatre. Une justification uniforme demande pourtant un majorant sur tout le compact, pas seulement un développement à x fixé.

```text
cos u=1−u²/2+u⁴/24+O(u⁶)
(1+u²)^(−1/2)=1−u²/2+3u⁴/8+O(u⁶)
fₙ(x)=−x⁴/(3n⁴)+O(x⁶/n⁶)
```

**Démonstration.** Taylor avec reste donne |cos u−1+u²/2|≤u⁴/24. Pour v=u²≥0, la dérivée seconde de (1+v)^(−1/2) est au plus 3/4, d’où un reste ≤3u⁴/8. Ainsi |fₙ(x)|≤5R⁴/(12n⁴) pour |x|≤R. La série de ces majorants converge, donc Σfₙ converge normalement sur tout compact réel.

**Lire l’expérience.** Le banc compare n⁴fₙ à −x⁴/3 et compare la somme partielle au terme local −π⁴x⁴/270. Ce dernier est un développement au voisinage de zéro, pas la formule de la somme sur tout ℝ. Pour les petites valeurs de x/n, le calcul utilise une expression stable afin d’éviter la soustraction de deux nombres presque égaux à 1.

## 6. Sommer un développement local demande un reste sommable

**Spé · TP : tp99_original**

**Propriété ciblée.** Sur un voisinage |x|≤r<1, les restes d’ordre six des deux fonctions sont uniformément contrôlés. Leur somme en n conserve un ordre O(x⁶). On peut ainsi relier le coefficient local de la somme à ζ(4).

```text
S(x)=Σn≥1fₙ(x)=−[ζ(4)/3]x⁴+O(x⁶)
ζ(4)=π⁴/90 ⇒ S(x)=−π⁴x⁴/270+O(x⁶)
```

**Justification.** Choisir r<1 fixe permet de majorer les dérivées qui contrôlent le reste de chaque terme par une constante indépendante de n, puisque |x/n|≤r. Le reste est alors ≤C|x|⁶/n⁶, et Σn⁻⁶ converge. Le terme quartique se somme séparément. Le raisonnement explique pourquoi un simple équivalent terme à terme ne suffit pas sans un contrôle de la famille.

## 7. Le disque de convergence protège les opérations

**Sup → Spé · TP : geometrie**

**Objets et but.** La série géométrique donne un modèle exact pour distinguer rayon de convergence, convergence sur un compact et précision d’une somme finie. Le banc utilise PN(x)=Σk=0ᴺxᵏ sur [−r,r], avec r<1. N est le degré : le polynôme possède N+1 termes.

```text
PN=(1−x^(N+1))/(1−x) ; S=1/(1−x)
S−PN=x^(N+1)/(1−x)
‖S−PN‖∞,[−r,r]=r^(N+1)/(1−r)
```

**Démonstration.** L’identité finie se démontre par télescopage après multiplication par 1−x. Pour |x|<1, x^(N+1)→0. Sur |x|≤r, la norme de xᵏ est rᵏ, donc la série converge normalement. Le maximum du reste est atteint à x=r, ce qui rend la borne exacte. Près de r=1, le dénominateur petit amplifie l’erreur.

**Lire l’expérience.** Dériver terme à terme donne Σk≥1kx^(k−1)=1/(1−x)². La série dérivée est encore normale sur tout compact intérieur, puisque Σkr^(k−1) converge. La somme dérivée demande davantage de termes pour une même précision ; le rayon demeure 1, mais les majorants changent.

## 8. Les dérivées demandent leur propre contrôle uniforme

**Sup → Spé · TP : geometrie**

**Propriété ciblée.** La convergence uniforme des fonctions seule ne permet pas de dériver leur limite. Pour la série géométrique, on calcule le reste de la série dérivée et l’on dispose donc d’une justification supplémentaire.

```text
Σk>Nkr^(k−1)=rᴺ[(N+1)−Nr]/(1−r)²
‖S′−PN′‖∞,[−r,r]≤ce même nombre
```

**Justification.** Dériver la queue r^(N+1)/(1−r) pour r∈[0,1[ fournit la formule. La série dérivée converge normalement sur le compact et la série initiale converge en un point ; le théorème de dérivation des séries identifie alors la dérivée de la somme. Ce contrôle peut être réutilisé pour primitives, solutions d’EDO et fonctions génératrices.

## 9. L’exercice 4 : une EDO donne la série entière

**Spé · TP : arcsin_ex4**

**Objets et but.** On cherche le développement de f(x)=arcsin(x)/√(1−x²) au voisinage de zéro. Plutôt que multiplier deux longues séries, on calcule une équation différentielle et une condition initiale. La construction de la série puis l’unicité de cette EDO justifient son identification à la fonction.

```text
(1−x²)f′−xf=1 ; f(0)=0
a₀=0, a₁=1, (n+2)aₙ₊₂=(n+1)aₙ
f(x)=Σk≥0 [4ᵏ(k!)²/(2k+1)!]x^(2k+1), |x|<1
```

**Démonstration.** La dérivée du quotient vérifie l’EDO. En remplaçant f par Σanxⁿ et en identifiant les coefficients, les termes pairs sont nuls et cₖ=a₂ₖ₊₁ vérifie c₀=1, cₖ=(2k/(2k+1))cₖ₋₁. Le quotient des termes non nuls tend vers x², donc le rayon est 1. Sur ce disque les opérations sont licites et la série résout l’EDO avec la bonne valeur initiale.

**Lire l’expérience.** Les premiers termes sont x+(2/3)x³+(8/15)x⁵+(16/35)x⁷. Les coefficients restent positifs et au plus 1, donnant un majorant géométrique du reste sur |x|≤r<1. Les singularités ±1 expliquent le ralentissement de convergence, pas une erreur dans la récurrence.

## 10. Un résidu d’EDO contrôle une construction algébrique

**Spé · TP : arcsin_ex4**

**Propriété ciblée.** Le polynôme PN qui garde N termes impairs ne satisfait pas exactement l’EDO. Son résidu possède pourtant une forme très simple, qui permet de détecter une erreur de coefficient.

```text
PN=Σk=0ᴺ⁻¹cₖx^(2k+1)
(1−x²)PN′−xPN−1=−2N cN−1 x^(2N)
‖f−PN‖∞,|x|≤r≤r^(2N+1)/(1−r²)
```

**Justification.** Tous les coefficients internes du résidu s’annulent par la récurrence. Seul le degré maximal, produit de −x²PN′−xPN, subsiste avec le facteur −2N. Pour le reste de fonction, 0<cₖ≤1 permet de sommer Σk≥Nr^(2k+1). Une petite erreur de résidu et une borne de reste sont deux contrôles différents, complémentaires au dessin.

## 11. L’exercice 5 : du coefficient à une croissance entière

**Spé ; lien probabiliste · TP : asymptotique_ex5**

**Objets et but.** Pour n≥2, aₙ=(1+2/n²)^(n³)/n! et S(x)=Σn≥2aₙxⁿ. L’exercice demande le rayon puis un équivalent lorsque x→+∞. Le développement du logarithme doit précéder l’exponentiation ; confondre e²x avec 2x changerait complètement la croissance.

```text
n³ln(1+2/n²)=2n−2/n+O(n⁻³)
aₙ~e^(2n)/n! ; R=+∞
S(x)~exp(e²x), x→+∞
```

**Démonstration.** Les racines n-ièmes satisfont aₙ^(1/n)=exp[n²ln(1+2/n²)]/(n!)^(1/n). Le premier facteur tend vers e² et le second dénominateur tend vers l’infini, donc R=∞ par Cauchy–Hadamard. Le quotient aₙ/(e^(2n)/n!) tend vers 1. Pour passer à la somme à x positif, encadrer les coefficients à partir d’un rang fixe ; la contribution des premiers rangs est un polynôme négligeable devant exp(e²x).

**Lire l’expérience.** L’expérience pose λ=e²x et calcule S(x)e^(−λ), qui tend vers 1. Les poids dominants se trouvent autour de n≈λ : une somme arrêtée avant ce cœur peut paraître bien calculée mais manquer presque tout le résultat. Les logarithmes évitent les débordements causés par des valeurs exponentielles énormes.

## 12. Une loi de Poisson fournit un transfert rigoureux

**Spé ; lien probabiliste · TP : asymptotique_ex5**

**Propriété ciblée.** Le coefficient normalisé rₙ=(1+2/n²)^(n³)e^(−2n) est dans ]0,1[ et tend vers 1. Le rapport de sommes est donc une espérance sous une loi de Poisson, à laquelle manquent les rangs 0 et 1.

```text
S(x)e^(−λ)=Σn≥2rₙe^(−λ)λⁿ/n!, λ=e²x
P(Nλ=n)=e^(−λ)λⁿ/n!
```

**Justification.** Fixer ε>0 puis choisir m avec |rₙ−1|≤ε pour n≥m. La masse des rangs n<m est e^(−λ) fois un polynôme en λ, donc tend vers zéro. Sur les autres rangs, l’erreur est au plus ε fois une masse au plus 1. Le rapport tend vers 1. Cette preuve exploite x>0 et des poids positifs ; elle ne s’étend pas automatiquement à une direction complexe.

## 13. L’exercice 10 : le binôme pour un exposant non entier

**Spé · TP : binomiale_ex10**

**Objets et but.** On pose α=p+1/2, p entier, et f(u)=(1−u)^(−α). Le banc considère des demi-entiers positifs et négatifs, afin de ne pas réduire le binôme à une suite toujours positive. La série se construit par une EDO : (1−u)f′=αf et f(0)=1.

```text
c₀=1 ; cₙ₊₁=(α+n)cₙ/(n+1)
(1−u)^(−α)=Σn≥0[(α)ₙ/n!]uⁿ, |u|<1
α=1/2 : cₙ=binom(2n,n)/4ⁿ
```

**Démonstration.** Le symbole (α)ₙ désigne le produit α(α+1)…(α+n−1), avec (α)₀=1. Identifier les coefficients dans l’EDO donne la récurrence. Pour les demi-entiers non entiers du banc, le rapport des modules des termes tend vers |u|, donc R=1. La série obtenue résout l’EDO sur le disque et fournit le développement voulu ; une fonction C∞ seule ne suffirait pas à garantir cette analyticité.

**Lire l’expérience.** Pour α>0, les coefficients sont positifs ; près de u=1 ils deviennent difficiles à sommer avec peu de termes. Pour α négatif non entier, la fonction peut rester finie au bord mais possède une singularité de dérivées ou de branche, conservant R=1. Les signes des coefficients doivent être lus dans la récurrence, pas imposés par analogie au cas α=1/2.

## 14. Une dérivée déplace l’exposant dans le bon sens

**Spé · TP : binomiale_ex10**

**Propriété ciblée.** La dérivation répétée fournit un produit croissant d’exposants. Elle explique les coefficients de Taylor et prépare l’intégration de la racine inverse dans l’exercice elliptique.

```text
dᵏ/duᵏ (1−u)^(−α)=(α)ₖ(1−u)^(−α−k)
f_p′=(p+1/2)f_{p+1}
f_p^(k)=[2^(−k)Π_{j=0}^{k−1}(2p+1+2j)]f_{p+k}
```

**Justification.** La première dérivée combine le signe de l’exposant −α et celui de la dérivée de 1−u, donnant +α. Chaque dérivation augmente l’exposant α d’une unité et multiplie par cette nouvelle valeur. En zéro, on obtient f^(k)(0)=(α)ₖ, puis cₖ=f^(k)(0)/k!. Pour α=1/2, réarranger le produit des nombres impairs donne binom(2k,k)/4ᵏ.

## 15. Le pendule relie une série à une période non linéaire

**Sup → Spé · TP : elliptique_pendule**

**Objets et but.** L’exercice 10 contient I(k)=∫₀π[1−k²sin²t]^(−1/2)dt, |k|<1. Pour un pendule idéal de longueur ℓ, lancé sans vitesse à l’angle θ₀, poser k=sin(θ₀/2). La conservation de l’énergie conduit à T=4√(ℓ/g)K(k), où K=I/2 ; le facteur 2 entre I et K est essentiel.

```text
I(k)=πΣn≥0[binom(2n,n)/4ⁿ]²k^(2n)
T₀=2π√(ℓ/g) ; T/T₀=I(k)/π
T/T₀=1+k²/4+9k⁴/64+…
```

**Démonstration.** Développer la racine inverse en u=k²sin²t. Pour |k|≤r<1, les termes sont majorés par cnr²ⁿ, ce qui justifie l’intégration terme à terme. Wallis donne ∫₀πsin²ⁿt dt=πbinom(2n,n)/4ⁿ ; les deux coefficients binomiaux se multiplient. Tous les termes sont positifs, donc les sommes partielles sous-estiment la période.

**Lire l’expérience.** Le modèle harmonique sinθ≈θ prédit une période indépendante de l’amplitude. La série elliptique montre la correction réelle et son coût près de la séparatrice θ₀=180°. La longueur multiplie les périodes par √ℓ sans modifier T/T₀. La trajectoire numérique illustre ce résultat et reste distincte de la quadrature qui calcule la période.

## 16. Retrouver le changement de variable énergétique

**Sup → Spé · TP : elliptique_pendule**

**Propriété ciblée.** L’équation θ″+(g/ℓ)sinθ=0 possède une énergie conservée. En choisissant l’amplitude maximale, on exprime la vitesse puis le quart de période avec sin(θ/2)=k sinφ.

```text
θ̇²=(4g/ℓ)[k²−sin²(θ/2)]
T/4=√(ℓ/g)∫₀π/₂dφ/√(1−k²sin²φ)
```

**Justification.** L’énergie par unité de masse vaut ℓ²θ̇²/2+gℓ(1−cosθ), égale à gℓ(1−cosθ₀). Utiliser 1−cosθ=2sin²(θ/2), puis différencier sin(θ/2)=k sinφ. Le facteur cosφ s’annule avec la racine de k²−sin²(θ/2), donnant K. Ce calcul justifie à la fois le module k et le facteur quatre, sans supposer petites oscillations.

## 17. L’exercice 11 : additionner des intégrales positives

**Spé · TP : integrale_sh_ex11**

**Objets et but.** Pour t>0, t/sinh t=2te^(−t)/(1−e^(−2t)). Le développement géométrique donne une série de fonctions positives dont chaque aire se calcule par intégration par parties. Le prolongement continu de t/sinh t vaut 1 en zéro, mais chaque somme partielle de la série vaut 0 en ce point.

```text
t/sinh t=Σn≥0 2t e^(−(2n+1)t), t>0
∫₀^∞2t e^(−(2n+1)t)dt=2/(2n+1)²
∫₀^∞t/sinh t dt=π²/4
```

**Démonstration.** Le changement u=(2n+1)t ramène chaque aire à [2/(2n+1)²]∫₀∞ue^(−u)du. La somme des intégrales absolues est finie, puisque Σ1/(2n+1)² converge. Le théorème d’intégration des séries, ou la convergence monotone pour cette famille positive, permet l’échange sur ]0,+∞[. La somme sur les impairs vaut (1−1/4)ζ(2)=π²/8.

**Lire l’expérience.** Le banc calcule les aires sur tout [0,+∞[ et utilise [0,T] seulement pour la représentation. Une queue à grande valeur de t et un reste de série après N sont donc séparés. Le décalage au point t=0 ne modifie aucune intégrale, mais interdit de prétendre à une convergence uniforme jusqu’à ce bord.

## 18. La norme choisie change le type de convergence

**Spé · TP : integrale_sh_ex11**

**Propriété ciblée.** Cette série converge absolument dans L¹ mais n’est pas normale pour la norme uniforme sur ]0,+∞[. Les deux constats sont compatibles et relient séries de fonctions, espaces normés et intégration.

```text
‖2t e^(−(2n+1)t)‖₁=2/(2n+1)²
‖2t e^(−(2n+1)t)‖∞=2/[e(2n+1)]
Σ‖terme‖₁<∞ ; Σ‖terme‖∞=∞
```

**Justification.** Le maximum du terme se trouve en t=1/(2n+1), donnant la seconde norme. Les aires forment une série en 1/n² ; les maxima une série en 1/n. Sur un domaine t≥δ>0, les maxima des grands rangs passent au bord δ et décroissent exponentiellement, ce qui rétablit une convergence normale uniforme loin de zéro.

## 19. L’exercice 12 : dominer un signal réel ou complexe

**Spé · TP : dominee_ex12**

**Objets et but.** Pour f continue par morceaux sur [0,1], on compare In=∫₀¹f(t)(1−t/n)ⁿdt à I=∫₀¹f(t)e^(−t)dt. Le noyau est réel positif, mais f peut être complexe ou posséder un saut. La domination porte sur |f|, et le théorème s’applique aux deux composantes complexes.

```text
(1−t/n)ⁿ→e^(−t), 0≤(1−t/n)ⁿ≤1
|f(t)(1−t/n)ⁿ|≤|f(t)|, intégrable
In→I par convergence dominée
```

**Démonstration.** Pour t fixé, n ln(1−t/n)→−t. Le cas n=1,t=1 est défini directement par le noyau 0 et ne gêne pas le passage à la limite en n. Une fonction continue par morceaux sur un segment est bornée et intégrable ; |f| fournit un majorant indépendant de n. Les parties réelle et imaginaire convergent donc toutes deux vers les composantes de I.

**Lire l’expérience.** Pour f=e^(iωt), le banc dessine le chemin des In dans le plan complexe et calcule I=[e^(−1+iω)−1]/(−1+iω). Pour un saut en 0,4, la quadrature se fait sur deux intervalles. Ces précautions distinguent une identité de convergence d’un simple calcul numérique sur une grille.

## 20. Une borne quantitative issue du logarithme

**Spé · TP : dominee_ex12**

**Propriété ciblée.** La convergence dominée donne une limite mais pas de vitesse automatique. Ici le logarithme permet d’obtenir une borne uniforme pour le noyau, puis une borne de l’erreur d’intégrale en fonction de ‖f‖₁.

```text
n≥2 : 0≤e^(−t)−(1−t/n)ⁿ≤1/[2(n−1)]
|In−I|≤‖f‖₁/[2(n−1)]
```

**Justification.** Poser q=−n ln(1−t/n)−t=Σk≥2tᵏ/(k n^(k−1)). Pour 0≤t≤1, q≤t²/[2n(1−t/n)]≤1/[2(n−1)]. La différence des noyaux vaut e^(−t)(1−e^(−q)), majorée par q grâce à 1−e^(−q)≤q. Multiplier par |f|, intégrer puis utiliser l’inégalité triangulaire donne la borne annoncée.

## 21. Un RC : Laplace conserve aussi l’état initial

**Sup → Spé · TP : rc_reponses**

**Objets et but.** Le TP de la page 107 suit la tension y aux bornes du condensateur d’un RC. On note τ=RC en secondes, u la tension d’entrée en volts et y₀=y(0⁻). La loi de maille donne τy′+y=u. Une entrée affine est ici u(t)=b+at pour t>0 : a est une pente en V/s, b une ordonnée en V. Les noms a et b sont donc volontairement explicités avant tout calcul.

```text
τy′+y=u ; Y(p)=[U(p)+τy₀]/(1+τp)
Pas A : y=A+(y₀−A)e^(−t/τ)
Rampe b+at : y=b+at−aτ+(y₀−b+aτ)e^(−t/τ)
```

**Démonstration.** Une intégration par parties donne L(y′)=pY−y₀. Pour la rampe, U=b/p+a/p² ; on sépare un polynôme particulier b+at−aτ et un transitoire Ce^(−t/τ). La condition initiale fournit C=y₀−b+aτ. Pour une impulsion d’aire A en V·s, intégrer l’équation autour de zéro donne le saut τ[y(0⁺)−y(0⁻)]=A ; la contribution impulsionnelle vaut (A/τ)e^(−t/τ).

**Lire l’expérience.** Avec τ=0,8 s, a=0,7 V/s, b=0,4 V et y₀=0, la sortie vaut 0,7t−0,16+0,16e^(−t/0,8). Elle part de zéro et, après le transitoire, suit la pente de l’entrée avec un retard en tension aτ=0,56 V. Vérifier l’état initial et l’équation différentielle est plus sûr que reconnaître seulement une forme exponentielle.

## 22. La convolution décrit le repos initial

**Sup → Spé · TP : rc_reponses**

**Propriété ciblée.** Pour y₀=0, la réponse d’un système linéaire invariant est la convolution de son entrée avec h(t)=𝟙_{t≥0}e^(−t/τ)/τ. L’indicatrice 𝟙 assure la causalité ; elle est distincte du transfert H(p). Un état initial non nul ajoute une solution homogène et ne se cache pas dans le même produit de transfert.

```text
y(t)=∫₀ᵗ h(t−s)u(s)ds + y₀e^(−t/τ)
H(p)=L(h)(p)=1/(1+τp), Re p>−1/τ
```

**Justification.** Le facteur intégrant e^(t/τ) transforme l’équation en [ye^(t/τ)]′=u e^(t/τ)/τ. Intégrer de 0 à t fournit directement la convolution et le terme initial. L’intégrale de h sur [0,+∞[ vaut 1 : le gain statique est donc 1, tandis que h a l’unité s⁻¹. La transformée de h existe dans le demi-plan indiqué, ce qui inclut l’axe imaginaire pour τ>0.

## 23. Une fréquence : gain et phase sont deux informations

**Sup → Spé · TP : rc_bode**

**Objets et but.** Pour une entrée sinusoïdale après extinction du transitoire, le RC agit sur l’exponentielle complexe e^(iωt). La fréquence ν est en Hz, la pulsation ω=2πν en rad/s ; il faut cette conversion avant de placer la coupure. Le gain mesure un rapport d’amplitudes, la phase un décalage du motif.

```text
H(iω)=1/(1+iωτ)
|H|=1/√(1+ω²τ²), arg H=−arctan(ωτ)
νc=1/(2πτ) ; GdB=20log₁₀|H|
```

**Démonstration.** Remplacer y par Ye^(iωt) et u par Ue^(iωt) dans τy′+y=u donne (1+iωτ)Y=U. Une entrée cos(ωt+φ) devient |H|cos(ωt+φ+arg H). À la coupure, le gain vaut 1/√2 et la phase −π/4. À haute fréquence le gain est équivalent à 1/(ωτ), soit une pente −20 dB par décade ; à basse fréquence il tend vers 1.

**Lire l’expérience.** Le banc combine trois harmoniques : chacune possède son propre gain et sa propre phase. Une sortie plus lisse n’est donc pas seulement une version de l’entrée réduite par une constante. À τ=0,2 s, νc≈0,796 Hz ; une fondamentale de 0,8 Hz est déjà atténuée, et ses harmoniques davantage.

## 24. Pourquoi Laplace donne Fourier sur l’axe imaginaire

**Sup → Spé · TP : rc_bode**

**Propriété ciblée.** L’évaluation de H(p) en p=iω est justifiée ici parce que h est absolument intégrable. Cette propriété assure la stabilité du filtre en amplitude et l’existence de son intégrale de Fourier.

```text
H(iω)=∫₀^∞ h(t)e^(−iωt)dt
‖h*u‖∞ ≤ ‖h‖₁‖u‖∞
```

**Justification.** Pour h(t)=e^(−t/τ)/τ sur t≥0, l’intégrale de |h| vaut 1. On peut donc fixer ω réel et faire le calcul sans régularisation. L’inégalité de convolution se déduit de |∫h(s)u(t−s)ds|≤‖u‖∞∫|h|. Un transfert possédant un pôle sur l’axe imaginaire demanderait un autre examen : écrire p=iω dans une expression rationnelle ne justifie pas à lui seul une réponse permanente bornée.

## 25. Les pôles d’un second ordre organisent le transitoire

**Spé, physique et SI selon filière · TP : rlc_poles**

**Objets et but.** Le modèle normalisé y″+2ζω₀y′+ω₀²y=ω₀²u représente notamment un circuit RLC ou un oscillateur mécanique. La pulsation propre ω₀ a l’unité rad/s, ζ est sans unité. Le banc part du repos et compare un pas unitaire et une impulsion unitaire.

```text
H(p)=ω₀²/(p²+2ζω₀p+ω₀²)
p±=−ζω₀ ± ω₀√(ζ²−1)
ζ<1 : paire complexe ; ζ=1 : pôle double ; ζ>1 : deux pôles réels
```

**Démonstration.** Le dénominateur se factorise à partir de l’équation caractéristique. Pour ζ<1, poser ωd=ω₀√(1−ζ²) donne des termes e^(−ζω₀t)cos(ωdt) et e^(−ζω₀t)sin(ωdt). À ζ=1, les deux modes fusionnent : la seconde solution est te^(−ω₀t). On ne peut pas utiliser deux coefficients de fractions simples distinctes au point de fusion.

**Lire l’expérience.** Le plan des pôles donne la vitesse de décroissance par leur partie réelle et la fréquence d’oscillation par leur partie imaginaire. Une augmentation de ζ supprime le dépassement, mais un ζ très élevé crée aussi un pôle lent proche de zéro. « Plus amorti » ne signifie donc pas systématiquement « plus rapide ».

## 26. Calculer le dépassement sans lire approximativement un graphe

**Spé, physique et SI selon filière · TP : rlc_poles**

**Propriété ciblée.** Pour 0<ζ<1, la réponse au pas possède un premier maximum à π/ωd. Sa hauteur au-dessus de la valeur finale se calcule exactement à partir de la réponse impulsionnelle.

```text
h(t)=(ω₀²/ωd)e^(−ζω₀t)sin(ωdt)
Mp=exp[−πζ/√(1−ζ²)], tp=π/ωd
```

**Justification.** La dérivée de la réponse au pas est h. Elle s’annule la première fois pour ωdt=π, avec changement de signe positif vers négatif. Dans y=1−e^(−ζω₀t)[cos(ωdt)+(ζω₀/ωd)sin(ωdt)], substituer ce temps donne y(tp)=1+e^(−πζ/√(1−ζ²)). Pour ζ≥1, la réponse au pas au repos est monotone dans ce modèle.

## 27. Une intégrale conditionnelle calculée par Laplace

**Spé · TP : dirichlet_abel**

**Objets et but.** La page 107 propose I=∫₀^∞ sin(t)/t dt. L’intégrale impropre converge, mais ∫|sin(t)|/t diverge. L’expérience introduit p>0 dans Ip=∫₀^∞ e^(−pt)sin(t)/t dt, puis fait tendre p vers zéro. La borne finie L et le paramètre p sont deux opérations distinctes.

```text
Ip′=−∫₀^∞ e^(−pt)sin(t)dt=−1/(1+p²)
Ip=π/2−arctan p ; limp→0⁺ Ip=π/2
```

**Démonstration.** Sur tout compact p≥p₀>0, une domination exponentielle permet de dériver sous l’intégrale. On utilise L(sin)(p)=1/(1+p²), puis la condition Ip→0 lorsque p→+∞ pour déterminer la constante d’intégration. Pour retrouver l’intégrale sans amortissement, il reste à justifier le passage au bord p=0 ; une domination par 1/t ne convient pas sur l’infini.

**Lire l’expérience.** Le banc affiche valeur fermée, intégrale amortie tronquée et intégrale non amortie tronquée. Leur proximité numérique ne remplace pas le contrôle de la queue. Pour p petit, augmenter L ; pour une borne L fixée, on n’a que la limite d’une intégrale sur [0,L].

## 28. Contrôler uniformément une queue oscillante

**Spé · TP : dirichlet_abel**

**Propriété ciblée.** L’intégration par parties donne une borne O(1/L) pour les queues de sin(t)/t, avec ou sans amortissement p≥0. C’est ce contrôle qui permet la limite d’Abel sans convergence dominée absolue sur [0,+∞[.

```text
|∫L^∞ e^(−pt)sin(t)/t dt|≤2/L, p≥0
∫L^∞ sin(t)/t dt = cos L/L − ∫L^∞ cos(t)/t² dt
```

**Justification.** Poser a(t)=e^(−pt)/t, positive décroissante. L’intégration par parties sur [L,R] avec la primitive −cos t majore l’intégrale par a(L)+a(R)+∫L^R|a′|≤2a(L). Puis R→∞ donne ≤2/L indépendamment de p. Sur [0,L], la fonction sin(t)/t se prolonge en 1 et le passage p→0 est dominé. On contrôle alors d’abord la queue, puis le paramètre.

## 29. Un signal bref occupe un spectre large

**Sup → Spé · TP : porte_sinc**

**Objets et but.** La porte Π vaut 1 pour |t|<1/2. Une porte de durée L centrée en t₀ est f(t)=Π((t−t₀)/L), d’amplitude 1. Fourier est ici en Hz : f̂(ν)=∫ℝf(t)e^(−2iπνt)dt. On écrit sincₙ(u)=sin(πu)/(πu), avec sincₙ(0)=1 ; la sinc du PDF sin z/z vaut sincₙ(z/π).

```text
f̂(ν)=L sincₙ(Lν)e^(−2iπνt₀)
Premiers zéros : ν=±1/L ; f̂(0)=L
```

**Démonstration.** Intégrer e^(−2iπνt) entre t₀−L/2 et t₀+L/2 donne un facteur de translation puis sin(πνL)/(πν). Sa limite en zéro est L, l’aire de la porte. Réduire L élargit le lobe principal ; déplacer t₀ modifie la phase sans changer le module. Aux zéros du spectre, la phase n’est pas définie et ne doit pas être interprétée comme une mesure fiable.

**Lire l’expérience.** Une porte de 0,25 s possède ses premiers zéros à ±4 Hz ; une porte de 2 s les possède à ±0,5 Hz. Le rapport durée–largeur est exact pour ces zéros. Ce n’est pas le produit de deux écarts types d’énergie, car le spectre sinc de la porte possède un second moment divergent.

## 30. Translations et dilatations : dériver les facteurs

**Sup → Spé · TP : porte_sinc**

**Propriété ciblée.** Un changement de variable conserve le facteur d’aire et fixe le sens des déplacements du spectre. C’est un outil commun à la porte, aux gaussiennes et au peigne de Dirac.

```text
TF[f(t−t₀)](ν)=e^(−2iπνt₀)f̂(ν)
TF[f(t/a)](ν)=|a|f̂(aν), a≠0
```

**Justification.** Dans la première intégrale, poser u=t−t₀ ; dans la seconde, u=t/a. Pour a<0, inverser les bornes compense le signe du Jacobien et produit |a|. Si l’on normalise la dilatation par 1/|a| pour garder une aire 1, ce facteur disparaît de la transformée. On distingue donc toujours largeur, amplitude et aire.

## 31. Une gaussienne dans deux domaines

**Sup → Spé ; incertitude en prolongement · TP : gaussienne**

**Objets et but.** On étudie f(t)=A exp[−t²/(2σ²)], où σ>0 mesure la largeur de l’amplitude et A son amplitude. Pour parler d’incertitude temps–fréquence, les densités sont |f|² et |f̂|² normalisées par l’énergie. Leur largeur n’est pas directement le σ écrit dans l’amplitude.

```text
f̂(ν)=Aσ√(2π)e^(−2π²σ²ν²)
E=∫|f|²dt=A²σ√π
Δt=σ/√2 ; Δν=1/(2√2πσ) ; Δt·Δν=1/(4π)
```

**Démonstration.** La TF peut se déduire sans déplacer une intégrale complexe : f′=−tf/σ² implique, par intégration par parties et dérivation en ν, f̂′=−4π²σ²ν f̂. L’aire f̂(0)=Aσ√(2π) fournit la constante. Les densités d’énergie sont ensuite des gaussiennes de paramètres plus étroits ; calculer leurs moments donne les deux écarts types affichés.

**Lire l’expérience.** Multiplier A par deux quadruple l’énergie sans changer les deux largeurs normalisées. Réduire σ par deux réduit Δt par deux et double Δν. Ce modèle relie impulsions optiques, paquets d’ondes et mesure du signal, avec une convention en Hz qui explique le facteur 4π.

## 32. La borne d’incertitude par Cauchy–Schwarz

**Sup → Spé ; incertitude en prolongement · TP : gaussienne**

**Propriété ciblée.** Pour un signal centré suffisamment régulier, à énergie finie, tel que tf et f′ appartiennent à L², une intégration par parties puis Cauchy–Schwarz donnent la borne temps–fréquence. Les exemples discontinus n’ont pas automatiquement ces moments finis.

```text
‖f‖₂² = −2 Re∫t f̄(t)f′(t)dt
‖tf‖₂‖f′‖₂ ≥ ‖f‖₂²/2
TF(f′)=2iπνf̂ ⇒ Δt·Δν≥1/(4π)
```

**Justification.** Intégrer la dérivée de t|f|² avec un terme de bord nul. Majorer la partie réelle par le module du produit scalaire, puis par les normes L². Parseval transforme ‖f′‖₂ en 2π‖νf̂‖₂. L’égalité de Cauchy–Schwarz impose f′ proportionnel à tf avec une constante réelle négative, ce qui conduit à une gaussienne centrée.

## 33. Une convolution se lit comme un recouvrement

**Sup → Spé · TP : convolution_portes**

**Objets et but.** On prend deux portes d’amplitude 1, de largeurs L₁ et L₂, centrées respectivement en 0 et d. La convolution bilatérale vaut ∫ℝ f(u)g(t−u)du. Pour ces fonctions indicatrices, l’intégrale est exactement la longueur de l’intersection de deux intervalles : une construction géométrique devient une formule de signal.

```text
(f*g)(t)=max(0,min(L₁/2,t−d+L₂/2)−max(−L₁/2,t−d−L₂/2))
TF(f*g)=L₁L₂ sincₙ(L₁ν)sincₙ(L₂ν)e^(−2iπνd)
```

**Démonstration.** Le premier intervalle est [−L₁/2,L₁/2] ; le second, obtenu en résolvant |t−u−d|<L₂/2, est [t−d−L₂/2,t−d+L₂/2]. Leur intersection donne la formule avec min et max. Pour L₁=L₂=L, le résultat est (L−|t−d|) positif sur |t−d|<L : un triangle. Si les largeurs diffèrent, un plateau apparaît lorsque la petite porte est entièrement dans la grande.

**Lire l’expérience.** Le curseur de sonde t déplace le second intervalle et rend visible l’intégrale avant de regarder le produit spectral. Le résultat possède l’unité s si les amplitudes sont sans unité ; sa hauteur n’est pas automatiquement 1. L’aire de la convolution vaut L₁L₂.

## 34. Pourquoi une convolution devient un produit

**Sup → Spé · TP : convolution_portes**

**Propriété ciblée.** Pour f et g dans L¹, le produit d’intégrabilité permet Fubini. Le calcul utilise deux variables indépendantes ; remplacer la convolution par le produit f(t)g(t) conduirait au résultat spectral inverse.

```text
∫ℝ∫ℝ|f(u)g(t−u)|du dt=‖f‖₁‖g‖₁
TF(f*g)(ν)=f̂(ν)ĝ(ν)
```

**Justification.** Dans l’intégrale double de la TF, poser v=t−u. L’exponentielle e^(−2iπνt) devient e^(−2iπνu)e^(−2iπνv), et les deux intégrales se séparent. Cette preuve explique à la fois le produit spectral et l’identité d’aire en évaluant en ν=0. Pour un système causal, les prolongements nuls avant zéro réduisent l’intégrale aux bornes 0 et t.

## 35. Un saut survit dans les sommes partielles

**Spé ; premières harmoniques accessibles en Sup · TP : gibbs_fourier**

**Objets et but.** Les pages 110-111 associent créneaux, rampes et triangles à leurs séries de Fourier. L’expérience compare Sₙ, qui garde les harmoniques |k|≤N, et la moyenne de Fejér σₙ, qui pondère chaque coefficient par 1−|k|/(N+1). Les deux reconstructions ont des comportements différents au voisinage d’un saut.

```text
Créneau ±1 : f(t)=(4/π)Σk≥0 sin[2π(2k+1)t/T]/(2k+1)
σN=Σ|k|≤N(1−|k|/(N+1))cₖe^(2iπkt/T)
```

**Démonstration.** Les coefficients d’un créneau décroissent comme 1/k. La série converge vers la demi-somme des limites latérales aux sauts, mais les sommes partielles développent un dépassement qui se resserre sans disparaître en hauteur. La limite du dépassement vaut environ 0,08949 fois le saut. Un triangle continu possède des coefficients en 1/k², donc une convergence normale et uniforme.

**Lire l’expérience.** Le curseur N est le dernier indice harmonique, pas le nombre de termes non nuls. Le créneau n’utilise que les indices impairs. La moyenne de Fejér élargit la transition mais limite le dépassement grâce à un noyau positif ; sa stabilité peut être préférable à une troncature brutale.

## 36. Fejér est une moyenne positive

**Spé ; premières harmoniques accessibles en Sup · TP : gibbs_fourier**

**Propriété ciblée.** La moyenne des N+1 premières sommes partielles est une convolution périodique avec un noyau positif de masse 1. Elle conserve donc les bornes d’un signal réel borné, contrairement au noyau de Dirichlet.

```text
KN(θ)=[sin((N+1)θ/2)]²/[(N+1)sin²(θ/2)]≥0
KN(0)=N+1, par prolongement aux points 2πℤ
(1/2π)∫₋π^πKN(θ)dθ=1
σN(f)=(1/2π)∫₋π^πKN(u)f(θ−u)du
```

**Justification.** Développer la somme géométrique Σj=0ᴺe^(ijθ), puis son module carré, donne les poids triangulaires 1−|k|/(N+1). Le coefficient constant du noyau est 1, d’où sa masse normalisée. Si m≤f≤M, multiplier par le noyau positif et intégrer fournit m≤σN(f)≤M. Pour f continue périodique, la concentration du noyau donne la convergence uniforme.

## 37. Une somme de carrés devient une énergie

**Spé · TP : parseval_spectre**

**Objets et but.** L’énergie moyenne d’un signal périodique est E=(1/T)∫₀ᵀ|f|²dt. Les coefficients cₙ sont normalisés par 1/T. Parseval affirme E=Σ|cₙ|², ou, pour une fonction réelle, E=a₀²/4+(1/2)Σ(an²+bn²). Une aire sur une période et une puissance moyenne ne possèdent pas le même facteur T.

```text
E=Σn∈ℤ|cₙ|²=a₀²/4+(1/2)Σn≥1(an²+bn²)
‖f−SN‖²moy=E−Σ|n|≤N|cₙ|²
```

**Démonstration.** Les fonctions e^(2iπnt/T) sont orthonormales pour le produit scalaire (1/T)∫f ḡ. Développer le carré d’une somme partielle élimine les termes croisés. La projection minimise ensuite l’erreur L² dans l’espace des harmoniques retenues. Le théorème de complétude permet de passer de Bessel à Parseval pour f dans L² périodique.

**Lire l’expérience.** Pour le créneau ±1, E=1 et bn=4/(πn) pour n impair : Σk≥0 1/(2k+1)²=π²/8. Pour le triangle entre 0 et 1, E=1/3, la composante moyenne contribue 1/4 et les autres donnent Σ1/(2k+1)⁴=π⁴/96. La somme de Bâle et ζ(4) en découlent en séparant indices pairs et impairs.

## 38. Une projection harmonique est le meilleur compromis L²

**Spé · TP : parseval_spectre**

**Propriété ciblée.** L’orthogonalité fixe les coefficients optimaux indépendamment de la forme graphique du signal. Ajouter un mode augmente l’énergie capturée sans détériorer l’erreur quadratique, même si un dépassement ponctuel augmente.

```text
‖f−v‖²=‖f−SN‖²+‖SN−v‖²
v appartient à span{e^(2iπkt/T), |k|≤N}
```

**Justification.** Le résidu f−SN est orthogonal à chaque mode retenu, donc à SN−v. Le développement du carré donne Pythagore. Les notions de meilleur ajustement quadratique, de Gibbs et de convergence uniforme répondent ainsi à trois questions différentes : une projection optimale L² ne minimise pas automatiquement l’erreur maximale.

## 39. Une série normale fabrique un filtre de lissage

**Spé ; prolongement harmonique · TP : poisson_noyau**

**Objets et but.** Le noyau de Poisson de la page 108 est Pᵣ(t)=Σk∈ℤr^|k|e^(2iπkt/T), avec |r|<1. Le banc emploie 0≤r<1. La série est normale puisque Σr^|k| converge, et sa masse sur une période vaut T. Le filtre normalisé est donc une convolution périodique par Pᵣ/T.

```text
Pᵣ(t)=(1−r²)/(1−2r cos(2πt/T)+r²)
∫₀ᵀPᵣ(t)dt=T
Reste après |k|≤N : ‖RN‖∞≤2r^(N+1)/(1−r)
```

**Démonstration.** Séparer k=0, k>0 et k<0 puis sommer deux séries géométriques donne la forme fermée. Le coefficient constant vaut 1, ce qui explique la masse. Pour le reste, chaque exponentielle a un module 1 ; la somme des deux queues géométriques fournit une majoration uniforme indépendante de t. À r proche de 1, un petit N peut donc être très insuffisant.

**Lire l’expérience.** Filtrer une série de Fourier multiplie son coefficient cₖ par r^|k|. Les hautes harmoniques sont davantage atténuées. Quand r→1⁻, le noyau devient étroit et haut autour des multiples de T ; il approche l’identité pour les signaux continus, avec une valeur de demi-somme aux sauts réguliers.

## 40. La positivité donne un principe de maximum

**Spé ; prolongement harmonique · TP : poisson_noyau**

**Propriété ciblée.** Pour 0≤r<1, Pᵣ est positif et de masse T. Son action sur un signal réel borné est donc une moyenne pondérée ; elle ne crée pas de valeur extérieure à l’intervalle des amplitudes d’entrée.

```text
(Pᵣ*f)pér(t)=(1/T)∫₀ᵀPᵣ(t−u)f(u)du
m≤f≤M ⇒ m≤(Pᵣ*f)pér≤M
```

**Justification.** Le numérateur 1−r² est positif et le dénominateur est |1−re^(2iπt/T)|²>0. On multiplie les inégalités m≤f≤M par Pᵣ/T et intègre ; la masse normalisée vaut 1. La convergence vers f pour r→1 utilise ensuite la continuité uniforme sur une période et le fait que la masse hors d’un petit voisinage de zéro tend vers zéro.

## 41. Poisson : périodiser le temps discrétise le spectre

**Spé ; prolongement harmonique · TP : poisson_gaussienne**

**Objets et but.** La page 108 relie un signal s et sa périodisation f(t)=Σk∈ℤs(t+kT). Pour la gaussienne s(t)=exp[−t²/(2σ²)], toutes les dérivées décroissent rapidement : les échanges de séries et d’intégrales se justifient. Les deux constructions affichées sont une somme de gaussiennes dans le temps et une série de cosinus.

```text
cₙ=ŝ(n/T)/T=(σ√(2π)/T)e^(−2π²σ²n²/T²)
f(t)=c₀+2Σn≥1cₙcos(2πnt/T)
```

**Démonstration.** Dans cₙ=(1/T)∫₀ᵀΣks(t+kT)e^(−2iπnt/T)dt, poser u=t+kT pour chaque terme. Les intervalles [kT,(k+1)T] couvrent ℝ et le facteur e^(2iπnk) vaut 1 : on obtient ŝ(n/T)/T. Insérer la TF gaussienne donne les coefficients. Leur décroissance quadratique exponentielle assure la convergence normale de la série spectrale.

**Lire l’expérience.** Lorsque σ/T est petit, les impulsions sont séparées et de nombreuses raies sont utiles. Lorsque σ/T est grand, la périodisation varie peu et c₀ domine. Le banc augmente automatiquement la borne de la somme directe pour couvrir les gaussiennes éloignées ; N règle surtout la troncature spectrale, dont l’erreur n’est pas celle de l’identité exacte.

## 42. La formule de Jacobi comme cas particulier de Poisson

**Spé ; prolongement harmonique · TP : poisson_gaussienne**

**Propriété ciblée.** Évaluer une périodisation gaussienne en zéro transforme une somme lentement convergente en une autre rapidement convergente. Cette dualité relie Fourier aux fonctions thêta et donne une technique de calcul.

```text
Σk∈ℤe^(−πa k²)=(1/√a)Σn∈ℤe^(−πn²/a), a>0
```

**Justification.** Appliquer Poisson avec T=1 à s(t)=e^(−πa t²), dont la TF en Hz vaut a^(−1/2)e^(−πν²/a). Si a est petit, la somme directe exige beaucoup de k ; la somme duale a des termes exponentiellement faibles dès |n|=1. Pour a grand, on choisit l’autre côté. Le changement de représentation accélère le calcul sans changer la quantité mathématique.

## 43. Shannon : un support spectral avant une reconstruction

**Spé ; signal selon filière · TP : shannon**

**Objets et but.** Le paquet s(t)=sincₙ²(Bt)cos(2πf₀t) appartient à L¹ et L², contrairement à une sinusoïde permanente. B est en Hz et décrit la demi-largeur des deux triangles spectraux, centrés en ±f₀. La plus grande fréquence du support est W=f₀+B. Le banc prend F>2W comme critère strict de marge avant de reconstruire.

```text
ŝ(ν)=[Λ((ν−f₀)/B)+Λ((ν+f₀)/B)]/(2B)
Λ(u)=max(1−|u|,0)
s(t)=Σn∈ℤs(n/F)sincₙ(Ft−n), si F>2W
```

**Démonstration.** La TF de sincₙ(Bt) est une porte de hauteur 1/B et de largeur B. Le carré dans le temps convolue ces deux portes dans le spectre, donnant Λ(ν/B)/B. Multiplier par cos(2πf₀t) crée deux translations, avec un facteur 1/2. Le peigne de pas 1/F répète ensuite ce spectre tous les F Hz, avec facteur F ; un filtre de gain 1/F dans la bande centrale restitue le signal.

**Lire l’expérience.** La formule utilise une infinité d’échantillons. L’expérience n’en garde que 2M+1 : au-dessus du seuil, une erreur peut encore provenir de cette troncature. Augmenter M à F fixé sépare cet effet du repliement. Le seuil exact au bord demande de préciser la classe de signaux : en L², des valeurs spectrales ponctuelles ne comptent pas comme une raie de Dirac.

## 44. La sinc interpolatrice et son facteur de gain

**Spé ; signal selon filière · TP : shannon**

**Propriété ciblée.** Poser a=1/F et φ=s·Σδ(t−na). L’échantillonnage multiplie par un peigne dans le temps, donc crée des copies spectrales. Le facteur de reconstruction vient de l’aire des impulsions et ne peut pas être omis.

```text
φ̂(ν)=FΣk∈ℤŝ(ν−kF)
ŝ(ν)=(1/F)φ̂(ν)Π(ν/F)
TF⁻¹[(1/F)Π(ν/F)]=sincₙ(Ft)
```

**Justification.** Le filtre idéal garde seulement la copie centrale lorsque les bandes sont séparées. La TF inverse de Π(ν/F) vaut F sincₙ(Ft), et le gain 1/F annule ce F. Convoluer les impulsions de poids s(n/F) avec sincₙ(Ft) donne la somme de Shannon. Aux instants j/F, sincₙ(j−n)=0 pour j≠n et vaut 1 pour j=n : les mesures sont exactement interpolées.

## 45. Les mesures identifient une fréquence modulo F

**Sup → Spé · TP : aliasing**

**Objets et but.** Une sinusoïde de fréquence f est mesurée aux instants k/F. Ajouter un multiple entier de F à f ne change aucune valeur de l’exponentielle complexe. Le représentant signé dans [−F/2,F/2[ conserve aussi la phase ; prendre seulement sa valeur absolue demanderait d’adapter cette phase.

```text
e^(2iπ(f+ℓF)k/F)=e^(2iπfk/F), ℓ∈ℤ
fₐ=((f+F/2) modulo F)−F/2
sin(2πfk/F+φ)=sin(2πfₐk/F+φ)
```

**Démonstration.** La différence des arguments est 2πℓk, multiple de 2π. Les signaux sont identiques sur la grille, mais distincts entre ses points. Pour F=24 Hz et f=19 Hz, le représentant est −5 Hz. La courbe sin(−2π5t+φ) a exactement les mêmes valeurs mesurées. L’ambiguïté est une perte d’information, pas une erreur du calcul de FFT.

**Lire l’expérience.** Le cas f=F/2 mérite une expérience séparée : sin(πk+φ)=(−1)ᵏsinφ. Les phases φ et π−φ deviennent indiscernables, et une phase nulle produit une suite entièrement nulle. Les sinusoïdes permanentes ont une énergie infinie ; elles servent ici à démontrer l’ambiguïté et ne sont pas confondues avec le paquet de Shannon.

## 46. Un repliement négatif change la lecture de la phase

**Sup → Spé · TP : aliasing**

**Propriété ciblée.** Pour une sinusoïde réelle, un représentant fréquentiel négatif peut être écrit à fréquence positive, mais sa phase est modifiée. Cela explique les animations où le motif semble tourner dans l’autre sens.

```text
sin(−ωt+φ)=sin(ωt+π−φ)
cos(−ωt+φ)=cos(ωt−φ)
```

**Justification.** Ces identités suivent des parités du sinus et du cosinus. Elles évitent d’attribuer au signal apparent la phase initiale inchangée à la fréquence positive. Un signal complexe distingue le sens de rotation par le signe de la fréquence ; un signal réel combine nécessairement des fréquences opposées conjuguées.

## 47. Un filtre analogique précède la perte d’information

**Spé ; SI et physique selon filière · TP : anti_repliement**

**Objets et but.** La chaîne contient une composante utile de 3 Hz et une perturbation de fréquence fₚ, puis un échantillonneur de cadence F. Un Butterworth analogique d’ordre n et coupure fc atténue la perturbation avant la mesure. Le module seul ne suffit pas à recomposer les sinusoïdes : la phase complexe est aussi utilisée.

```text
|H(i2πν)|=1/√[1+(ν/fc)^(2n)]
pₖ=2πfc exp[iπ(2k+1+n)/(2n)], k=0,…,n−1
H(p)=Πk[−pₖ/(p−pₖ)] ; H(0)=1
```

**Démonstration.** Les pôles sont tous dans le demi-plan gauche ; les paires conjuguées produisent un filtre réel stable. À ν=fc, le gain est 1/√2 quel que soit n. À haute fréquence, la pente asymptotique vaut −20n dB par décade. Le banc filtre chaque composante en régime permanent par son gain complexe, puis mesure la sortie aux instants k/F.

**Lire l’expérience.** Un parasite de 72 Hz mesuré à 50 Hz se replie à 22 Hz. Le filtre peut réduire son amplitude, mais un filtre numérique placé après la mesure ne connaît plus son origine à 72 Hz. Un Butterworth n’a pas de support spectral strictement borné : l’atténuation limite le repliement, elle ne transforme pas le signal en signal parfaitement bandé.

## 48. Déterminer l’ordre d’un filtre à partir d’une spécification

**Spé ; SI et physique selon filière · TP : anti_repliement**

**Propriété ciblée.** Une contrainte de gain à une fréquence supérieure à fc donne un ordre minimal par un logarithme. Il faut ensuite contrôler l’atténuation de la composante utile et accepter une phase associée au filtre causal.

```text
Gain à fp ≤ ε ⇒ (fp/fc)^(2n)≥ε⁻²−1
n≥ln(ε⁻²−1)/[2ln(fp/fc)], fp>fc
```

**Justification.** Mettre au carré l’inégalité 1/√(1+x^(2n))≤ε, puis isoler x^(2n). Comme x>1, le logarithme est croissant et positif, d’où la borne sur n. On prend ensuite le plus petit entier admissible. Le gain à la fréquence utile se calcule séparément : une bonne suppression du parasite ne garantit pas la fidélité de toute la bande utile.

## 49. Une FFT observe un signal multiplié par une fenêtre

**Spé ; prolongement numérique · TP : fenetres_fft**

**Objets et but.** N valeurs sont acquises à F=128 Hz, aux instants k/F, k=0,…,N−1. La durée DFT est T=N/F et le pas natif F/N. Une fréquence située entre deux cases produit une fuite spectrale. La fenêtre de Hann ou de Blackman réduit les lobes secondaires en élargissant le lobe principal ; le signal observé est le produit xkwk. Ici xk est la mesure au rang k et wk le coefficient de la fenêtre. FFT désigne le calcul rapide de la transformée de Fourier discrète (DFT). CG est le gain cohérent, moyenne des coefficients de fenêtre ; ENBW est la largeur de bande équivalente de bruit, en Hz.

```text
Xj=Σk=0ᴺ⁻¹xkwk e^(−2iπjk/N)
Amplitude positive isolée ≈2|Xj|/Σwk
CG=(1/N)Σwk ; ENBW=FΣwk²/(Σwk)²
```

**Démonstration.** La fenêtre finie transforme une raie infiniment fine en une copie de son propre spectre. Diviser par Σw corrige le gain cohérent d’une raie sur une case ; cela ne corrige pas exactement tous les biais hors case ni le recouvrement de raies voisines. Les amplitudes DC et Nyquist ne sont pas doublées : ces cases n’ont pas une partenaire distincte dans la représentation monolatérale.

**Lire l’expérience.** L’ajout de zéros n’ajoute aucune mesure. Il échantillonne plus densément le même polynôme trigonométrique et permet de mieux lire un maximum interpolé. Le banc affiche séparément F/N, F/(Nq), le gain cohérent et la bande équivalente de bruit, pour éviter de confondre calibration, interpolation et résolution.

## 50. Distinguer DFT et approximation d’une TF continue

**Spé ; prolongement numérique · TP : fenetres_fft**

**Propriété ciblée.** La DFT est une somme algébrique de N valeurs sans unité de temps ajoutée. Une approximation de l’intégrale de Fourier exige le pas Δt, et une origine temporelle t₀ ajoute une phase.

```text
f̂(νj)≈Δt e^(−2iπνjt₀)Σk=0ᴺ⁻¹f(t₀+kΔt)e^(−2iπjk/N)
νj=j/(NΔt) ; TF en Hz
```

**Justification.** C’est la somme de Riemann de f(t)e^(−2iπνjt). À chaque instant, l’exponentielle se factorise en une phase d’origine puis en e^(−2iπjk/N). Omettre Δt change la normalisation et les unités ; omettre t₀ change la phase mais pas le module. La troncature temporelle et le remplacement par une somme restent deux approximations distinctes.

## 51. La durée de mesure distingue des fréquences proches

**Sup → Spé ; expérimentation numérique · TP : resolution**

**Objets et but.** Deux cosinus d’amplitudes égales ont des fréquences 18 et 18+Δf Hz. Leur somme possède des battements et leur spectre observé résulte de deux lobes de fenêtre qui peuvent se recouvrir. Le banc garde F=128 Hz et compare une acquisition longue à un simple ajout de zéros.

```text
cos(2πf₁t)+cos(2πf₂t)=2cos(πΔft)cos[2π(f₁+f₂)t/2]
T=N/F ; pas natif=1/T ; premiers zéros de Hann à environ ±2/T
```

**Démonstration.** La formule trigonométrique distingue une porteuse à la fréquence moyenne et une enveloppe de module 2|cos(πΔft)|. Si ΔfT est petit, la fenêtre ne montre qu’une faible partie d’un battement et les lobes se recouvrent fortement. Allonger T réduit les lobes en fréquence ; ajouter des zéros augmente seulement le nombre de points d’affichage.

**Lire l’expérience.** Le repère 1/T est un pas de grille, pas une loi universelle de séparation de deux pics. La fenêtre, le rapport d’amplitudes, les phases et le bruit comptent aussi. Pour Hann, la largeur entre premiers zéros d’un lobe est environ 4/T : une séparation critique différente apparaît selon le critère retenu.

## 52. Battements : enveloppe signée et enveloppe observée

**Sup → Spé ; expérimentation numérique · TP : resolution**

**Propriété ciblée.** L’enveloppe signée cos(πΔft) et son module n’ont pas la même période. Les maxima visibles d’intensité ou de module se répètent avec période 1/Δf, tandis que le facteur signé a période 2/Δf.

```text
A(t)=2|cos(πΔft)|
Période des maxima de A : 1/Δf ; premiers minima : 1/(2Δf)
```

**Justification.** Les maxima de |cos θ| se reproduisent après π plutôt qu’après 2π. Les zéros apparaissent à θ=π/2+kπ, donnant les dates (k+1/2)/Δf. Cette distinction évite un facteur deux lorsque l’on mesure l’écart des fréquences à partir de battements acoustiques ou d’un oscilloscope.

## 53. Suivre une fréquence qui varie au cours du temps

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Objets et but.** Le signal à fréquence balayée (chirp) est x(t)=cos[2π(f₀t+kt²/2)]. Sa fréquence instantanée est la dérivée de sa phase divisée par 2π : ν(t)=f₀+kt. L’expérience dure 3 s et échantillonne à 128 Hz. Une fenêtre mobile de L valeurs permet de localiser les fréquences au cours du temps. f₀ est la fréquence initiale en Hz, k la vitesse du balayage en Hz/s ; STFT désigne la transformée de Fourier sur des fenêtres temporelles successives.

```text
STFTx(t₀,ν)=∫x(t)w(t−t₀)e^(−2iπνt)dt
νinst(t)=f₀+kt ; durée locale L/F ; pas natif F/L
```

**Démonstration.** On extrait chaque segment, le multiplie par une Hann et calcule une FFT locale. Une fenêtre courte suit un changement rapide mais possède un lobe spectral large. Une fenêtre longue réduit ce lobe, mais le chirp parcourt alors plusieurs fréquences pendant la fenêtre, ce qui étale aussi l’énergie. La carte affiche des dB relatifs à son propre maximum, avec un plancher −65 dB.

**Lire l’expérience.** Les zéros ajoutés à 256 points densifient les colonnes de fréquence ; ils ne changent pas la durée locale L/F. La ligne ν=f₀+kt sert de repère analytique. Une crête de carte est une estimation issue de données fenêtrées, pas une preuve que le signal était stationnaire dans chaque segment.

## 54. Un compromis contrôlé par deux largeurs

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Propriété ciblée.** Pour un signal à fréquence balayée linéaire, une fenêtre de durée τw voit une variation de fréquence |k|τw. Son propre étalement est de l’ordre de 1/τw. Leur comparaison donne un ordre de grandeur pour choisir une fenêtre adaptée au balayage.

```text
Variation dans une fenêtre : |k|τw
Étalement d’une fenêtre : C/τw
Équilibre d’échelles : τw de l’ordre de 1/√|k|
```

**Justification.** La première largeur augmente avec τw, la seconde diminue. En les équilibrant sans prétendre fixer une constante universelle, on obtient τw² de l’ordre de 1/|k|. Le choix final dépend de la fenêtre et du critère de lecture. Cette argumentation d’échelles explique pourquoi la plus longue fenêtre n’est pas toujours la meilleure pour un signal dont la fréquence varie.

## 55. Multiplier un message déplace son spectre

**Sup → Spé ; communications en prolongement · TP : modulation**

**Objets et but.** La modulation d’amplitude utilise s(t)=[1+m cos(2πfmt)]cos(2πfct). Le message varie à fm, la porteuse à fc ; m est une profondeur sans unité. Pour 0≤m≤1, l’enveloppe signée ne devient pas négative. Le banc compare ce signal et une démodulation synchrone dont l’oscillateur local peut être déphasé ou légèrement désaccordé.

```text
s(t)=cos(2πfct)+(m/2)cos[2π(fc−fm)t]+(m/2)cos[2π(fc+fm)t]
Après mélange ×2cos[2π(fc+Δf)t+φ] et passe-bas :
y(t)=[1+m cos(2πfmt)]cos(2πΔft+φ)
```

**Démonstration.** Le produit de deux cosinus se transforme en demi-somme aux fréquences somme et différence. Le mélange synchrone ramène une copie vers les basses fréquences et en crée une seconde autour de 2fc ; le passe-bas idéal du modèle retire cette seconde copie. À Δf=0, le gain est cosφ ; à φ=π/2, la composante utile disparaît malgré un signal reçu non nul.

**Lire l’expérience.** Les barres spectrales positives du banc sont des amplitudes de cosinus : 1 et m/2. En TF bilatérale de distributions, chaque cosinus possède deux Dirac de poids moitié de cette amplitude. Lorsque m>1, l’enveloppe change de signe ; son module ne permet plus de restituer directement le message par un détecteur d’enveloppe.

## 56. Le théorème de modulation et ses facteurs 1/2

**Sup → Spé ; communications en prolongement · TP : modulation**

**Propriété ciblée.** Pour un signal a intégrable, une exponentielle translate sa TF et un cosinus produit deux translations. Ce théorème s’applique à un paquet de durée finie autant qu’à la décomposition idéale en raies.

```text
TF[a(t)e^(2iπfct)](ν)=â(ν−fc)
TF[a(t)cos(2πfct)](ν)=[â(ν−fc)+â(ν+fc)]/2
```

**Justification.** Regrouper les exponentielles dans l’intégrale définit directement â(ν−fc). Décomposer cos=(e^(iθ)+e^(−iθ))/2 donne la seconde égalité. La distinction entre deux bandes complexes et les amplitudes de cosinus réels évite de doubler à tort les coefficients lors d’un bilan d’énergie.

## 57. Une corrélation estime un retard dans le bruit

**Spé ; mesure et probabilités · TP : correlation_retard**

**Objets et but.** La convention de la page 108 est Cfg(τ)=∫ℝḡ(t)f(t+τ)dt. g est l’impulsion émise, f sa copie retardée reçue et bruitée. Avec cette convention, une réception f(t)=g(t−d) donne un pic à τ=d. Les mesures sont faites à 200 Hz ; le pas de recherche vaut donc 5 ms.

```text
Cfg(τ)=∫ḡ(t)f(t+τ)dt
γfg(τ)=Cfg(τ)/(‖f‖₂‖g‖₂) ; |γfg|≤1
Distance aller-retour : D=cτ/2
```

**Démonstration.** La corrélation est un produit scalaire glissant : elle devient grande lorsque le signal reçu ressemble à une translation du signal émis. La normalisation utilise les énergies globales, conservées par une translation sur ℝ. La fenêtre de trois secondes et la grille numérique introduisent une troncature et une quantification ; le bruit peut déplacer le maximum entre plusieurs oscillations de l’impulsion codée.

**Lire l’expérience.** La graine choisit une réalisation reproductible du bruit gaussien, sans changer son écart type théorique. La distance déduite suppose un trajet aller-retour dans un milieu de vitesse c connue. Une grille de 5 ms donne à elle seule un pas de distance c×0,005/2 ; elle ne garantit pas une erreur de mesure de ce seul ordre en bruit fort.

## 58. Cauchy–Schwarz et Wiener–Khintchine

**Spé ; mesure et probabilités · TP : correlation_retard**

**Propriété ciblée.** La borne de cohérence et la TF de l’autocorrélation se déduisent de produits scalaires et d’un changement de variable. Elles relient la page 108 aux techniques d’espaces préhilbertiens et au bilan spectral d’énergie.

```text
Cff(0)=‖f‖₂² ; Cfg(τ)=conj[Cgf(−τ)]
TF(Cfg)(ν)=f̂(ν)conj[ĝ(ν)]
TF(Cff)(ν)=|f̂(ν)|²
```

**Justification.** Appliquer Cauchy–Schwarz à g et f(·+τ) donne la borne normalisée. Pour la TF, intégrer e^(−2iπντ)ḡ(t)f(t+τ), poser u=t+τ puis séparer les intégrales : f̂(ν)∫ḡ(t)e^(2iπνt)dt. L’autocorrélation est ainsi la TF inverse de la densité d’énergie spectrale. La conjugaison est essentielle pour les signaux complexes.

## 59. Débruiter distingue bruit résiduel et signal déformé

**Spé ; prolongement numérique · TP : debruitage**

**Objets et but.** Un signal utile contient une fondamentale et sa deuxième harmonique. Le banc ajoute un bruit blanc puis applique soit une moyenne glissante causale de M valeurs, soit un filtre récursif de pôle ρ=e^(−1/M). Il filtre aussi le signal utile seul : cette référence sépare la déformation du signal du bruit restant. RMS signifie valeur efficace, racine de la moyenne des carrés ; M est la longueur de mémoire et ρ le coefficient du filtre récursif.

```text
Moyenne : yk=(1/M)Σj=0ᴹ⁻¹xk−j
RC numérique : yk=ρyk−1+(1−ρ)xk
Bruit résiduel=L(s+b)−L(s) ; distorsion=L(s)−s
```

**Démonstration.** La linéarité donne L(s+b)=L(s)+L(b). Comparer seulement la sortie à l’entrée propre mélange deux effets : supprimer le bruit et modifier le signal utile. La moyenne glissante possède une phase de retard et des zéros spectraux ; le récursif possède une mémoire exponentielle. Les bilans RMS excluent une partie initiale pour limiter l’effet du repos initial.

**Lire l’expérience.** Une longue mémoire réduit davantage le bruit blanc indépendant mais peut effacer une harmonique ou retarder fortement la forme. L’expérience donne un facteur de variance théorique et une RMS mesurée sur une réalisation finie : elles n’ont pas à coïncider exactement. La durée et la graine permettent d’interpréter cette fluctuation.

## 60. Le bruit blanc donne une somme de carrés de coefficients

**Spé ; prolongement numérique · TP : debruitage**

**Propriété ciblée.** Si bk sont centrés, indépendants et de variance σ², une sortie Σhjbk−j possède une variance σ²Σhj². Le calcul justifie des facteurs exacts pour les deux filtres, après extinction du transitoire.

```text
Var(Σhj bk−j)=σ²Σhj²
Moyenne M : facteur 1/M
Récursif : facteur (1−ρ)/(1+ρ)
```

**Justification.** Développer le carré de la somme. Les termes croisés ont une espérance nulle par indépendance et centrage. Pour la moyenne, M coefficients 1/M donnent 1/M. Pour le récursif, hj=(1−ρ)ρʲ, j≥0, et la série géométrique des carrés vaut (1−ρ)²/(1−ρ²)=(1−ρ)/(1+ρ). Un bruit coloré exigerait ses covariances et ne suit pas ce calcul simple.

## Repères avant les 30 expériences

### Laboratoire couche_limite

Un pic se déplace vers le bord de l’intervalle sans perdre de hauteur. L’étudier par dérivation permet de distinguer convergence en chaque point, convergence uniforme et convergence uniforme loin du bord.

**Objets et unités**

- n est le rang entier de la suite et x la position sur [0,1], sans unité. δ fixe un sous-intervalle éloigné de zéro ; la norme uniforme est la borne supérieure des valeurs absolues sur l’intervalle étudié.
- n entier, x∈[0,1] et fₙ(x)=nx/(1+n²x²) sans unité
- δ>0 fixe le compact [δ,1] ; u=nx est la coordonnée de loupe
- Le sommet est calculé analytiquement, pas estimé sur les points du graphe

**Hypothèses**

- Domaine fixe [0,1] pour la convergence simple et uniforme globale
- La comparaison locale utilise un δ positif fixé avant n→∞

**Techniques**

- Étude d’une dérivée et d’un maximum
- Quantificateurs de convergence
- Changement d’échelle u=nx

**Prévoir, manipuler, justifier**

1. Pour n=15, prévoir la position 1/n et la hauteur du pic avant de déplacer les curseurs.
2. Passer à n=800 puis comparer le tracé global, la loupe et les deux normes ; garder δ=0,03 fixe.
3. Écrire la preuve de CS, le contre-exemple à CU et la borne 1/(nδ) sur le compact ; expliquer ce qu’un maillage peut manquer.

**Niveaux et prolongements**

- Sup : Dérivation, signe, maximum et lecture de quantificateurs ; entrée progressive vers les suites de fonctions.
- Spé : Convergence simple et uniforme, norme uniforme (borne supérieure des valeurs absolues) et convergence locale sur les compacts.
- Au-delà : Couches limites et limites singulières d’équations différentielles.

**Résultat attendu.** Trois conclusions distinctes : CS sur [0,1], échec CU global, CU sur chaque [δ,1].

### Laboratoire concentration

Une suite de fonctions tend vers zéro en chaque point, alors que son aire tend vers un nombre non nul. Un changement d’échelle localise la concentration et montre quelle hypothèse manque pour échanger limite et intégrale.

**Objets et unités**

- fₙ(x)=n²xe^(−nx), x∈[0,1], n entier
- x₀ est un point fixe où l’on suit la suite numérique fₙ(x₀)
- Aire exacte, position 1/n, hauteur n/e ; loupe u=nx

**Hypothèses**

- Fonctions positives ; limite simple nulle, y compris en zéro
- La famille ne possède pas de domination intégrable commune sur [0,1]

**Techniques**

- Exponentielle contre puissance
- Intégration par parties et changement de variable
- Vérification des hypothèses de convergence dominée

**Prévoir, manipuler, justifier**

1. Pour n=8, prévoir simultanément hauteur, largeur caractéristique et aire ; ne conclure ni d’après la hauteur seule ni d’après un point.
2. Comparer n=8 puis n=200 et observer fₙ(x₀) avec x₀=0,2 ; utiliser la loupe pour conserver le profil.
3. Calculer 1−(n+1)e^(−n) et justifier pourquoi une domination intégrable commune est impossible.

**Niveaux et prolongements**

- Sup : Limites exponentielles, étude de fonction et calcul d’aire.
- Spé : Convergence dominée, contre-exemple à l’interversion et changement de variable adapté.
- Au-delà : Convergence de mesures vers une Dirac et concentration de masse.

**Résultat attendu.** Une limite ponctuelle nulle et une limite d’aire égale à 1, réconciliées par une couche de largeur 1/n.

### Laboratoire tp99_original

Soustraire deux fonctions très proches fait disparaître leurs premiers termes de développement. Retrouver le premier terme restant permet de majorer la série sur un intervalle fixé et de justifier sa convergence normale.

**Objets et unités**

- fₙ(x)=cos(x/n)−[1+(x/n)²]^(−1/2)
- R fixe [−R,R] ; n règle un terme ; N règle la somme des n=1,…,N
- n⁴fₙ et −π⁴x⁴/270 comparent deux développements locaux distincts

**Hypothèses**

- Majoration Taylor valable pour tout x réel sur un compact fixé
- Le terme quartique de la somme est une approximation en zéro, pas son expression globale
- Évaluation stable des petites différences

**Techniques**

- Développements limités et cancellation
- Critère de Weierstrass
- Borne d’une queue par une intégrale

**Prévoir, manipuler, justifier**

1. Avec R=1 et n=40, prédire les deux termes quadratiques puis expliquer leur annulation.
2. Comparer n⁴fₙ à −x⁴/3 ; augmenter ensuite R jusqu’à 4 et distinguer somme et approximation quartique.
3. Démontrer |fₙ|≤5R⁴/(12n⁴), puis la borne 5R⁴/(36N³) du reste de la somme.

**Niveaux et prolongements**

- Sup : Développements limités usuels, différences de fonctions proches et sommabilité de n⁻⁴.
- Spé : Convergence normale sur les compacts et sommation contrôlée d’un développement.
- Au-delà : Conditionnement numérique et calcul de différences par des développements stables.

**Résultat attendu.** Une justification de CN accompagnée d’un reste uniforme et d’une distinction entre identité et développement local.

### Laboratoire geometrie

Approcher une fonction et sa dérivée avec les sommes d’une série géométrique. Calculer les restes permet de justifier la dérivation terme à terme et de comprendre pourquoi les estimations se dégradent près du bord.

**Objets et unités**

- N est le dernier exposant conservé et r le rayon du sous-intervalle d’étude, avec r strictement inférieur à 1. Le reste est la différence entre la fonction exacte et la somme partielle.
- PN(x)=Σk=0ᴺxᵏ comporte N+1 termes
- r<1 définit le compact ∣x∣≤r ; R=1 est le rayon de convergence
- Deux restes affichés : somme et dérivée

**Hypothèses**

- Le compact reste strictement intérieur au disque
- Les normes des restes sont majorées analytiquement

**Techniques**

- Télescopage
- Somme géométrique et norme uniforme (borne supérieure des valeurs absolues)
- Convergence normale de la série dérivée

**Prévoir, manipuler, justifier**

1. Avec r=0,5, prévoir un degré garantissant une erreur de 10⁻³, puis comparer à la borne affichée.
2. Garder N=20 et déplacer r de 0,5 à 0,95 ; observer la dérivée et la somme séparément.
3. Calculer les deux queues et expliquer pourquoi le même rayon ne donne pas la même précision pour les dérivées.

**Niveaux et prolongements**

- Sup : Identité géométrique finie, limites et dérivation de polynômes.
- Spé : Séries entières, convergence normale sur les compacts et opérations terme à terme.
- Au-delà : Estimations de Cauchy et approximation de fonctions analytiques.

**Résultat attendu.** Un degré choisi à partir d’une borne et une dérivation de série justifiée sur un domaine annoncé.

### Laboratoire arcsin_ex4

Construire un développement en série à partir d’une équation différentielle. Identifier les coefficients puis comparer la somme à la fonction exacte entraîne les techniques de récurrence et de contrôle d’un reste.

**Objets et unités**

- f(x)=arcsin x/√(1−x²), ∣x∣<1
- N est le nombre de termes impairs ; le degré vaut 2N−1
- r fixe le compact ; cₖ est le coefficient de x^(2k+1)

**Hypothèses**

- L’analyticité est construite par une série de rayon 1 puis l’unicité de l’EDO
- Les singularités ±1 restent hors du domaine de contrôle uniforme

**Techniques**

- EDO du premier ordre
- Identification de coefficients
- Récurrence et majorant géométrique

**Prévoir, manipuler, justifier**

1. Pour N=4, retrouver c₀,c₁,c₂,c₃ à la main avant de lire le graphe des coefficients.
2. Comparer r=0,6 et r=0,98 avec N=20 ; repérer l’amplification du reste près du bord.
3. Calculer (1−x²)PN′−xPN−1 et retrouver son unique terme maximal ; justifier le rayon 1.

**Niveaux et prolongements**

- Sup : Dérivation de composées et récurrence de nombres ; introduction accompagnée de l’EDO.
- Spé : Développement en série entière par EDO, opérations sur les compacts et contrôle du résidu.
- Au-delà : Asymptotique des coefficients et singularités analytiques.

**Résultat attendu.** Un DSE démontré avec rayon, parité, récurrence et test algébrique indépendant.

### Laboratoire asymptotique_ex5

Une série entière contient des coefficients difficiles à évaluer directement. Les réécrire avec des exponentielles et des poids de Poisson permet d’étudier le rayon de convergence et un équivalent lorsque la variable devient grande.

**Objets et unités**

- aₙ=(1+2/n²)^(n³)/n!, n≥2 ; S(x)=Σaₙxⁿ
- λ=e²x ; rₙ=aₙn!/e^(2n) ; x>0
- N est le dernier rang conservé ; rapport S_N/e^λ et rapport S/e^λ sont distincts

**Hypothèses**

- Transfert asymptotique pour x→+∞ avec coefficients positifs
- Calculs normalisés en logarithmes ; la somme automatique est tronquée loin après le cœur n≈λ

**Techniques**

- Logarithme et développement limité
- Cauchy–Hadamard
- Encadrement des coefficients ou poids de Poisson

**Prévoir, manipuler, justifier**

1. Pour x=2, calculer λ ; examiner quels indices portent l’essentiel de la somme.
2. Passer à x=30 et N=100 puis augmenter N au-delà de λ ; comparer rapport partiel et rapport de référence.
3. Démontrer R=∞ et le transfert S(x)~exp(e²x) en séparant un début polynomial d’une queue positive.

**Niveaux et prolongements**

- Sup : Exponentielles, factorielles et ordre de grandeur ; calculs préparatoires accompagnés.
- Spé : Rayon, équivalents de coefficients et transfert justifié de somme.
- Au-delà : Concentration de Poisson, approximation de Laplace et arithmétique logarithmique.

**Résultat attendu.** Une preuve de l’équivalent et une troncature argumentée, sans confondre exp(e²x) et exp(2x).

### Laboratoire binomiale_ex10

Prolonger la formule du binôme à un exposant qui n’est pas entier. Suivre les coefficients, leur signe et le reste explique le développement en série entière et prépare le calcul d’une intégrale elliptique.

**Objets et unités**

- p entier de −3 à 3 ; α=p+1/2
- N est le nombre de termes ; u∈[−r,r], r<1
- c₀=1 et cₙ₊₁=(α+n)cₙ/(n+1)

**Hypothèses**

- Puissance réelle bien définie pour u<1
- Les demi-entiers du banc ne donnent pas de polynômes finis
- Borne de reste par rapport de termes ou borne de Cauchy

**Techniques**

- Dérivation répétée
- Récurrence multiplicative
- Rayon et convergence sur les compacts

**Prévoir, manipuler, justifier**

1. Choisir p=0 et retrouver 1,1/2,3/8,5/16 ; comparer à la formule binomiale centrale.
2. Choisir p=−3 puis p=3 ; prévoir les signes et observer la forte singularité près de u=1.
3. Justifier le rayon 1 et calculer f_p′ en précisant le signe et le sens du déplacement de p.

**Niveaux et prolongements**

- Sup : Dérivation des puissances et premiers coefficients, avec guidage.
- Spé : Binôme généralisé, séries entières et singularité au bord.
- Au-delà : Symboles de Pochhammer, fonctions hypergéométriques et bornes complexes de Cauchy.

**Résultat attendu.** Une formule de coefficients et de dérivées cohérente, avec signes contrôlés.

### Laboratoire elliptique_pendule

La période d’un pendule augmente avec l’amplitude de ses oscillations. Partir de l’énergie puis intégrer une série permet de mesurer l’écart au modèle harmonique et de justifier une correction de ce modèle.

**Objets et unités**

- θ₀ en degrés dans le contrôle, en radians dans les développements
- ℓ en m, g=9,81 m·s⁻² ; k=sin(θ₀/2)
- I(k) est sur [0,π], K=I/2 ; T/T₀=I/π ; N compte les termes

**Hypothèses**

- Pendule idéal sans frottement, vitesse initiale nulle
- Période par quadrature de Gauss ; trajectoire par Runge–Kutta d’ordre 4
- Pas de passage à θ₀=180° où la période diverge

**Techniques**

- Énergie et intégrale première
- Série binomiale et Wallis
- Convergence normale puis borne de queue positive

**Prévoir, manipuler, justifier**

1. Comparer θ₀=10° puis 120° et prédire le signe de la correction à T₀.
2. Garder θ₀=160° et augmenter N ; changer ensuite ℓ pour vérifier que le rapport T/T₀ ne change pas.
3. Retrouver T=4√(ℓ/g)K, puis I=2K, et expliquer la divergence près de la séparatrice.

**Niveaux et prolongements**

- Sup : Énergie du pendule et modèle harmonique ; première correction accompagnée.
- Spé : Intégrale elliptique, échange série–intégrale et contrôle du reste.
- Au-delà : Séparatrice, fonctions elliptiques et comparaison de solveurs numériques.

**Résultat attendu.** Une période non linéaire calculée avec le bon facteur 2 et une limite des petites oscillations justifiée.

### Laboratoire integrale_sh_ex11

Décomposer une fonction positive en une somme de fonctions dont les aires sont connues. Comparer les aires partielles et le reste apprend à justifier l’intégration d’une série sur un intervalle non borné.

**Objets et unités**

- f(t)=t/sinh t, prolongée en 1 à t=0
- N modes n=0,…,N−1 ; chaque aire vaut 2/(2n+1)²
- T borne la fenêtre dessinée ; les aires affichées sont sur [0,+∞[

**Hypothèses**

- Identité de série pour t>0 ; un point isolé ne modifie pas l’intégrale
- Termes positifs et somme des intégrales absolues finie
- La série ne converge pas uniformément près de zéro

**Techniques**

- Série géométrique
- Intégration par parties
- Théorème d’intégration des séries et comparaison intégrale

**Prévoir, manipuler, justifier**

1. Avec N=3, calculer à la main les trois premières aires et observer ce que le tracé manque près de zéro.
2. Augmenter N jusqu’à 200 puis T ; suivre séparément la borne de reste de série et la queue au-delà de T.
3. Démontrer l’interversion et déduire π²/4 de la somme sur les indices impairs.

**Niveaux et prolongements**

- Sup : Séries numériques positives et intégrales élémentaires accompagnées.
- Spé : Intégration de séries de fonctions, normes L¹/sup et encadrements de restes.
- Au-delà : Convergence dans des espaces fonctionnels et transformées thermiques.

**Résultat attendu.** Une valeur exacte π²/4 avec une justification d’interversion et deux erreurs de troncature distinguées.

### Laboratoire dominee_ex12

Remplacer un noyau exponentiel par une suite de fonctions plus élémentaires dans une intégrale. Chercher une majoration indépendante du rang permet de justifier le passage à la limite, y compris pour un signal complexe.

**Objets et unités**

- t∈[0,1], n entier ; noyau (1−t/n)ⁿ
- ω sans dimension dans exp(iωt) ou sin(ωt)
- In complexe est représentée par Re et Im ; signal à saut en 0,4

**Hypothèses**

- f continue par morceaux, ∣f∣ intégrable
- Quadrature de Gauss sur chaque intervalle de continuité ; limite calculée analytiquement
- Pour n=1,t=1, le noyau est défini par 0

**Techniques**

- Convergence simple et domination
- Intégrales complexes
- Inégalité de logarithme et borne quantitative

**Prévoir, manipuler, justifier**

1. Choisir la famille affine avec n=1 et prédire le signe de la différence entre les noyaux.
2. Passer au signal complexe et augmenter n ; lire son chemin d’intégrales dans le plan complexe.
3. Vérifier la domination par |f| et démontrer |In−I|≤‖f‖₁/[2(n−1)] pour n≥2 ; tester ensuite le saut.

**Niveaux et prolongements**

- Sup : Limite de (1−t/n)ⁿ et intégration de fonctions réelles/complexes, avec accompagnement.
- Spé : Convergence dominée, fonctions continues par morceaux et contrôle quantitatif.
- Au-delà : Convergence d’opérateurs intégraux et extrapolation numérique.

**Résultat attendu.** Une interversion justifiée et une borne d’erreur indépendante de la quadrature.

### Laboratoire rc_reponses

Prévoir la tension d’un condensateur soumis à un échelon, une rampe ou une impulsion. Relier l’équation différentielle à la transformée de Laplace permet de traiter l’entrée et la charge initiale séparément.

**Objets et unités**

- τ=RC en s ; u,y,y₀ en V
- Rampe u=at+b : a en V/s, b en V
- Un pas a une amplitude A en V ; une impulsion une aire A en V·s

**Hypothèses**

- RC idéal, τ>0, entrée causale
- y₀=y(0⁻) est explicite ; une impulsion produit un saut A/τ
- Le transfert décrit la réponse au repos initial, l’état initial ajoute un terme homogène

**Techniques**

- EDO linéaire du premier ordre
- Laplace unilatérale et fractions simples
- Convolution causale et contrôle par substitution

**Prévoir, manipuler, justifier**

1. Pour τ=0,8,a=0,7,b=0,4,y₀=0, prévoir la pente finale et le décalage aτ avant de lire la courbe.
2. Comparer pas, rampe et impulsion, puis imposer y₀=1,2 ; vérifier le départ de chaque sortie.
3. Écrire Y=[U+τy₀]/(1+τp) et retrouver la solution ; pour l’impulsion, intégrer la maille autour de zéro.

**Niveaux et prolongements**

- Sup : Circuits RC, équation différentielle et constante de temps.
- Spé : Transformée de Laplace, réponse impulsionnelle et conditions initiales selon filière.
- Au-delà : Systèmes d’état, distributions causales et identification expérimentale.

**Résultat attendu.** Trois réponses temporelles vérifiées, avec pente/intercept et aire d’impulsion explicités.

### Laboratoire rc_bode

Faire traverser un filtre RC à un signal contenant trois harmoniques. Le gain et la phase de chaque harmonique expliquent la forme de la sortie et donnent un sens concret au diagramme de Bode.

**Objets et unités**

- R est la résistance, C la capacité et τ=RC la constante de temps. H est la fonction de transfert, rapport complexe sortie/entrée ; son module est le gain et son argument le déphasage.
- τ en s ; fréquence fondamentale ν₁ en Hz ; ω=2πν en rad/s
- H(iω) est complexe ; GdB=20log₁₀∣H∣ et phase en degrés
- Signal à trois harmoniques, recomposées avec leur gain et leur phase

**Hypothèses**

- RC idéal en régime permanent
- Réponse impulsionnelle intégrable, donc axe imaginaire dans le domaine de convergence
- Transitoire initial non représenté dans cette expérience de Bode

**Techniques**

- Complexes et régime sinusoïdal
- Asymptotes et coupure
- Superposition harmonique

**Prévoir, manipuler, justifier**

1. Calculer νc pour τ=0,2 s et prévoir gain et phase vers 0,8 Hz.
2. Comparer fondamentale sous la coupure et harmoniques filtrées ; modifier τ à fréquence fixe.
3. Recomposer une somme de trois sinusoïdes et justifier pourquoi la sortie n’est pas une réduction uniforme de l’entrée.

**Niveaux et prolongements**

- Sup : Régime sinusoïdal, gain, phase et diagrammes fréquentiels.
- Spé : Filtrage harmonique, relation Laplace–Fourier et stabilité.
- Au-delà : Identification fréquentielle et conception de filtres.

**Résultat attendu.** Une coupure calculée et une déformation expliquée par les gains ET les phases.

### Laboratoire rlc_poles

Un circuit du second ordre peut osciller, revenir sans oscillation ou être à la limite de ces régimes. La position des pôles relie ces comportements à l’équation différentielle et au facteur d’amortissement.

**Objets et unités**

- ω₀ est la pulsation propre et ζ le facteur d’amortissement. Un pôle est une racine du dénominateur de la fonction de transfert ; la partie réelle règle la décroissance et la partie imaginaire l’oscillation.
- ω₀ en rad/s ; ζ sans unité
- Entrée pas ou impulsion unitaire ; repos initial
- Pôles p± en s⁻¹, parties réelle et imaginaire affichées séparément

**Hypothèses**

- Système normalisé y″+2ζω₀y′+ω₀²y=ω₀²u
- ζ>0, système stable
- Régime critique traité avec te^(−ω₀t), sans division par des pôles confondus

**Techniques**

- Équation caractéristique
- Laplace et modes exponentiels
- Limite critique et calcul de dépassement

**Prévoir, manipuler, justifier**

1. À ω₀=6,ζ=0,15, prévoir le signe des parties réelles et l’existence d’oscillations.
2. Comparer ζ=0,15,1,1,8 sur le pas ; repérer le pôle lent à fort amortissement.
3. Calculer ωd et le premier dépassement pour ζ<1 ; retrouver la réponse critique par passage à la limite.

**Niveaux et prolongements**

- Sup : Oscillateur amorti et EDO du second ordre.
- Spé : Pôles, stabilité, réponse indicielle et identification selon filière.
- Au-delà : Commande, espace d’état et amortissement optimal suivant un cahier des charges.

**Résultat attendu.** Une classification des trois régimes et un temps de maximum ou de décroissance relié aux pôles.

### Laboratoire dirichlet_abel

Calculer une intégrale oscillante qui ne converge pas absolument. Introduire un amortissement exponentiel permet de dériver sous l’intégrale, puis de distinguer la limite mathématique de la troncature numérique.

**Objets et unités**

- p>0 amortit e^(−pt) ; L est la borne d’intégration
- Ip=∫₀∞e^(−pt)sin(t)/t dt ; valeur exacte π/2−arctan p
- sin(t)/t se prolonge en 1 à zéro

**Hypothèses**

- Intégrale non amortie conditionnellement convergente
- Contrôle uniforme de la queue oscillante ≤2/L
- Intégrales numériques sur des bornes finies distinctes des formules sur [0,+∞[

**Techniques**

- Dérivation sous intégrale
- Laplace de sin
- Intégration par parties et limite d’Abel

**Prévoir, manipuler, justifier**

1. Avec p=0,6,L=40, comparer les trois quantités exactes/amorties/tronquées.
2. Réduire p à 0,02 puis augmenter L ; distinguer les effets des deux paramètres.
3. Démontrer Ip′=−1/(1+p²), fixer la constante à p→∞ et justifier p→0 grâce à une borne de queue uniforme.

**Niveaux et prolongements**

- Sup : Intégration par parties, sinus cardinal et oscillations.
- Spé : Intégrales impropres, dérivation sous intégrale et convergence conditionnelle.
- Au-delà : Méthodes d’Abel, distributions et quadratures oscillantes.

**Résultat attendu.** La valeur π/2 obtenue avec un passage au bord justifié et des erreurs identifiées.

### Laboratoire porte_sinc

Une impulsion rectangulaire plus courte occupe un spectre plus large. Calculer sa transformée puis déplacer l’impulsion permet de séparer le module du spectre et la phase associée au retard.

**Objets et unités**

- L en s ; t₀ centre temporel en s
- Porte d’amplitude 1 ; f̂ a l’unité s
- sincₙ(u)=sin(πu)/(πu), sincₙ(0)=1 ; le PDF écrit aussi sin z/z

**Hypothèses**

- TF bilatérale en Hz, noyau e^(−2iπνt)
- Module et phase distingués ; phase indéfinie aux zéros
- Porte idéale discontinue, spectre non borné

**Techniques**

- Intégrale exponentielle
- Translation et dilatation
- Limite en zéro et bilan d’aire

**Prévoir, manipuler, justifier**

1. Pour L=1, t₀=0, calculer l’aire et les deux premiers zéros spectraux.
2. Réduire L à 0,3 puis déplacer t₀ de 0 à 1,3 à L fixé ; distinguer changements de module et de phase.
3. Démontrer f̂=L sincₙ(Lν)e^(−2iπνt₀), puis préparer une porte d’aire 1 en divisant l’amplitude par L.

**Niveaux et prolongements**

- Sup : Intégration complexe, oscillations et unités de fréquence.
- Spé : Fourier, phase de retard et distribution de Dirac en introduction.
- Au-delà : Résolution spectrale, limites de moments et distributions tempérées.

**Résultat attendu.** Une TF normalisée avec aire, premiers zéros et phase de translation cohérents.

### Laboratoire gaussienne

Comparer la durée d’une impulsion gaussienne à la largeur de son spectre. Définir les écarts types à partir de l’énergie permet de calculer leur produit et de relier Fourier à une inégalité de Cauchy–Schwarz.

**Objets et unités**

- σ en s est la largeur de l’amplitude Aexp[−t²/(2σ²)]
- Δt et Δν sont les écarts types de ∣f∣²/E et ∣f̂∣²/E
- E=A²σ√π ; Fourier en Hz

**Hypothèses**

- Gaussienne sur ℝ, à moments finis
- Borne d’incertitude en prolongement selon filière
- Les demi-largeurs ou premiers zéros sont d’autres mesures

**Techniques**

- Intégrale gaussienne
- Équation différentielle pour la TF
- Moments quadratiques et Cauchy–Schwarz

**Prévoir, manipuler, justifier**

1. Pour σ=0,6,A=1, calculer Δt et Δν avant de lire les graphes.
2. Doubler A puis diviser σ par deux ; séparer énergie et largeurs normalisées.
3. Démontrer la TF par f′=−tf/σ², puis retrouver ΔtΔν=1/(4π) avec les bonnes densités.

**Niveaux et prolongements**

- Sup : Gaussienne et changements d’échelle, avec calculs de moments accompagnés.
- Spé : Parseval et inégalité de Cauchy–Schwarz appliqués à un signal régulier.
- Au-delà : Incertitude de Heisenberg, paquets d’ondes et fonctions de Gabor.

**Résultat attendu.** Une largeur d’énergie correcte et un facteur 4π expliqué par la convention en Hz.

### Laboratoire convolution_portes

Faire glisser deux intervalles et mesurer la longueur de leur intersection. Cette construction donne la convolution de deux portes et explique, par Fourier, pourquoi leurs spectres se multiplient.

**Objets et unités**

- L₁,L₂ et d en s ; amplitude des deux portes égale à 1
- t sonde le recouvrement de [−L₁/2,L₁/2] et [t−d−L₂/2,t−d+L₂/2]
- Convolution de dimension s, aire totale L₁L₂

**Hypothèses**

- Convolution bilatérale sur ℝ
- Portes à support compact, Fubini justifié
- Triangle si largeurs égales, trapèze sinon

**Techniques**

- Intersection d’intervalles
- Intégrale et convolution
- Fubini et produit de TF

**Prévoir, manipuler, justifier**

1. Choisir L₁=L₂=1,d=0 et prévoir support, sommet et aire du triangle.
2. Passer à L₁=0,6,L₂=2,d=0,5 ; déplacer la sonde et mesurer le plateau.
3. Retrouver la formule min/max et vérifier l’aire au point spectral ν=0.

**Niveaux et prolongements**

- Sup : Intervalles, aires et fonctions définies par morceaux.
- Spé : Convolution, changements de variables et théorème de convolution de Fourier.
- Au-delà : Réponses de systèmes linéaires et B-splines.

**Résultat attendu.** Un triangle ou trapèze normalisé et son produit spectral, avec unités et aire vérifiées.

### Laboratoire gibbs_fourier

Reconstruire un créneau ou un triangle à partir de ses harmoniques. Comparer somme partielle et moyenne de Fejér permet d’expliquer le dépassement près d’un saut et le rôle du mode de convergence.

**Objets et unités**

- S_N est la somme partielle des harmoniques et σ_N la moyenne de Fejér, moyenne des premières sommes partielles. L² désigne ici l’erreur mesurée par l’intégrale de son carré sur une période.
- N est le dernier indice harmonique, pas le nombre de coefficients non nuls
- T période en s ; créneau ±1, triangle 0→1, rampe −1→1
- Fejér pondère par 1−∣k∣/(N+1)

**Hypothèses**

- Signaux périodiques réguliers par morceaux
- Valeur limite aux sauts = demi-somme latérale
- La comparaison utilise le même dernier indice N

**Techniques**

- Parité et coefficients de Fourier
- Convergence normale vs saut
- Moyenne de Cesàro et noyau positif

**Prévoir, manipuler, justifier**

1. Choisir le créneau, prévoir sa valeur reconstruite au saut et le sens du dépassement.
2. Comparer N=10 et N=55 puis le triangle ; observer somme partielle et Fejér séparément.
3. Justifier l’échec de CU pour le créneau, la CN du triangle et le contrôle d’amplitude de Fejér.

**Niveaux et prolongements**

- Sup : Harmoniques et synthèse de signaux, avec coefficients fournis.
- Spé : Séries de Fourier, convergence aux raccords et norme L².
- Au-delà : Théorème de Fejér, constantes de Lebesgue et approximation positive.

**Résultat attendu.** Une explication du dépassement persistant et un choix de sommation adapté au signal.

### Laboratoire parseval_spectre

Répartir l’énergie d’un signal périodique entre ses harmoniques. L’orthogonalité et Parseval permettent de contrôler l’énergie conservée par une reconstruction et de retrouver des sommes numériques classiques.

**Objets et unités**

- T est la période, c_n le coefficient complexe de la n-ième harmonique et S_N la reconstruction jusqu’au rang N. L’énergie moyenne est l’intégrale du carré du signal divisée par T.
- E=(1/T)∫∣f∣²dt ; cₙ normalisés par 1/T
- N borne les harmoniques conservées ; énergie capturée et reste séparés
- Triangle 0→1 : moyenne 1/2 ; créneau ±1 : moyenne 0

**Hypothèses**

- Signaux réels périodiques dans L²
- Les carrés des amplitudes portent un facteur 1/2 hors composante continue
- La norme moyenne ne décrit pas une erreur maximale

**Techniques**

- Orthogonalité
- Parseval et Pythagore
- Séparation d’indices pairs/impairs

**Prévoir, manipuler, justifier**

1. Pour le créneau, calculer l’énergie de la première harmonique avant de lire son pourcentage.
2. Passer au triangle et repérer la contribution 1/4 de sa moyenne ; augmenter N.
3. Déduire π²/6 et π⁴/90 avec Parseval puis expliquer pourquoi un faible reste L² ne supprime pas Gibbs.

**Niveaux et prolongements**

- Sup : Produit scalaire, trigonométrie et énergie de sinusoïdes.
- Spé : Projection, Parseval et sommes classiques de Fourier.
- Au-delà : Complétude dans L² et compression spectrale.

**Résultat attendu.** Un bilan exact d’énergie et deux sommes numériques obtenues avec les facteurs corrects.

### Laboratoire poisson_noyau

Lisser un créneau en atténuant progressivement ses harmoniques. Une série géométrique fournit le noyau de Poisson ; majorer son reste relie le lissage à la convergence normale et à la convolution.

**Objets et unités**

- r∈[0,1[ ; T période en s ; N dernier indice
- Pᵣ de masse T ; filtre périodique normalisé par 1/T
- Chaque harmonique est multipliée par r^∣k∣

**Hypothèses**

- Le banc reste à r≤0,97
- La limite r→1 se traite après la somme infinie
- La borne de queue est uniforme en t pour r fixé

**Techniques**

- Deux séries géométriques
- Critère de Weierstrass
- Convolution périodique et positivité

**Prévoir, manipuler, justifier**

1. Avec r=0,35, prévoir quelles harmoniques survivent ; vérifier la moyenne inchangée.
2. Comparer r=0,94,N=70 à r=0,97,N=12 ; observer noyau exact et noyau tronqué.
3. Démontrer la masse T, le reste≤2r^(N+1)/(1−r) et l’absence de dépassement pour le filtrage exact.

**Niveaux et prolongements**

- Sup : Sommes géométriques complexes et premières harmoniques.
- Spé : Convergence normale, convolution et contrôle uniforme.
- Au-delà : Équation de Laplace dans le disque et extension harmonique.

**Résultat attendu.** Un filtre de masse 1 dont précision et effet sur chaque coefficient sont quantifiés.

### Laboratoire poisson_gaussienne

Répéter une impulsion gaussienne dans le temps et reconstruire le même signal par ses raies spectrales. Comparer les deux sommes explique la périodisation et les facteurs de normalisation de Fourier.

**Objets et unités**

- σ et T en s ; N borne les raies ∣k∣≤N
- cₖ=ŝ(k/T)/T ; c₀=σ√(2π)/T
- La somme temporelle utilise automatiquement assez de répétitions lointaines

**Hypothèses**

- Gaussienne de Schwartz, TF en Hz
- Identité exacte, deux approximations tronquées
- L’écart affiché compare ces troncatures, pas une erreur du théorème

**Techniques**

- Périodisation et coefficients
- TF gaussienne
- Fubini et convergence normale

**Prévoir, manipuler, justifier**

1. Avec σ=0,14,T=1,5, prévoir si le signal ressemble à des impulsions séparées.
2. Augmenter σ à 1 puis réduire N ; comparer c₀ et les raies restantes.
3. Démontrer cₖ=ŝ(k/T)/T et utiliser l’identité gaussienne pour choisir la somme la plus rapide.

**Niveaux et prolongements**

- Sup : Gaussiennes répétées et lecture de spectre discret.
- Spé : Sommation de Poisson et normalisations temps–fréquence.
- Au-delà : Fonctions thêta, accélération de séries et réseaux de Bravais.

**Résultat attendu.** Une identité vérifiée par deux constructions avec sa moyenne et ses facteurs 1/T explicites.

### Laboratoire shannon

Reconstruire une impulsion à partir de mesures prises à intervalles réguliers. Comparer la cadence à la bande du signal distingue les conditions du théorème de Shannon et l’erreur due au nombre fini de mesures.

**Objets et unités**

- s(t)=sincₙ²(Bt)cos(2πf₀t), B,f₀,F en Hz
- M mesures de chaque côté :2M+1 valeurs ; tₙ=n/F
- Support spectral jusqu’à W=f₀+B ; marge choisie F>2W

**Hypothèses**

- Signal continu dans L¹∩L²
- La formule exacte utilise une infinité de mesures
- La somme affichée est tronquée ; les courbes spectrales conservent le facteur F du peigne

**Techniques**

- Porte/triangle en TF
- Peigne de Dirac et Shannon
- Borne de bande vs erreur de troncature

**Prévoir, manipuler, justifier**

1. Avec B=3,f₀=5, dessiner les deux bandes et calculer le seuil strict 16 Hz.
2. Comparer F=24 et F=12 puis, au-dessus du seuil, M=8 et M=40.
3. Retrouver les facteurs du peigne et du filtre idéal ; expliquer pourquoi la réussite aux points ne prouve pas une reconstruction entre points.

**Niveaux et prolongements**

- Sup : Mesure discrète et sinc avec un guidage spectral.
- Spé : Shannon, produits de TF et normalisations selon filière.
- Au-delà : Espaces de Paley–Wiener, reconstruction stable et échantillonnage non uniforme.

**Résultat attendu.** Un seuil justifié par un support, puis deux erreurs distinctes : repliement et somme finie.

### Laboratoire aliasing

Deux sinusoïdes différentes peuvent donner exactement les mêmes échantillons. Calculer leur fréquence apparente et leur phase permet de comprendre le repliement spectral et la limite d’une mesure discrète.

**Objets et unités**

- f,F en Hz ; phase φ en degrés
- Échantillons à k/F ; représentant signé dans [−F/2,F/2[
- Fréquence absolue du motif et phase adaptée sont deux informations

**Hypothèses**

- Sinusoïdes idéales périodiques, illustration d’ambiguïté
- Elles sont distinctes du paquet à énergie finie du labo Shannon
- Au bord de Nyquist, la phase n’est pas complètement identifiable

**Techniques**

- Congruence de phases modulo 2π
- Parité du sinus/cosinus
- Contre-exemple de mesure

**Prévoir, manipuler, justifier**

1. Avec F=24,f=19,φ=30°, prédire le représentant−5 Hz puis comparer les points.
2. Choisir f=12 Hz et tester plusieurs phases, dont 0° ; observer une sinusoïde invisible aux instants de mesure.
3. Écrire l’égalité des arguments modulo 2π et une représentation à fréquence positive avec phase corrigée.

**Niveaux et prolongements**

- Sup : Sinusoïdes, phases et périodicité.
- Spé : Repliement et limite d’un théorème de reconstruction.
- Au-delà : Signaux complexes, modulation IQ et bandes repliées.

**Résultat attendu.** Une ambiguïté démontrée par une égalité exacte de mesures et un cas limite interprété.

### Laboratoire anti_repliement

Une perturbation trop rapide peut apparaître comme une fausse fréquence après mesure. Placer un filtre analogique avant l’échantillonneur permet de comparer l’atténuation nécessaire à la cadence choisie.

**Objets et unités**

- F,fc et fréquence parasite en Hz ; utile à 3 Hz
- n ordre Butterworth ; amplitude parasite sans unité
- Pôles analogiques en s⁻¹ ; gains complexes avec phase

**Hypothèses**

- Butterworth analogique idéal stable en régime permanent
- Coupure à−3,01 dB, pas suppression exacte hors bande
- Le filtre numérique après mesure ne distingue pas des contributions repliées identiques

**Techniques**

- Pôles du demi-plan gauche
- Inégalités de gain
- Chaîne analogique puis mesure discrète

**Prévoir, manipuler, justifier**

1. Calculer le repliement de 72 Hz à F=50 Hz avant de regarder les sorties.
2. Comparer n=1 et n=4 à fc=12 Hz ; suivre le gain utile et le gain parasite.
3. Déterminer un ordre minimal pour une atténuation spécifiée et expliquer pourquoi fc doit aussi respecter la bande utile.

**Niveaux et prolongements**

- Sup : Filtres, diagrammes de gain et cadence de mesure.
- Spé : Ordre, pôles et conception selon cahier des charges en physique/SI.
- Au-delà : Filtres analogiques réels, tolérances et architectures de conversion.

**Résultat attendu.** Une atténuation chiffrée avant mesure avec un compromis utile/parasite clairement annoncé.

### Laboratoire fenetres_fft

Observer une sinusoïde pendant une durée finie et calculer son spectre numérique. Comparer les fenêtres et l’ajout de zéros permet de distinguer fuite spectrale, calibration d’amplitude et résolution.

**Objets et unités**

- FFT désigne l’algorithme rapide de calcul de la transformée de Fourier discrète (DFT). w_k sont les coefficients de la fenêtre ; CG est le gain cohérent, moyenne des w_k, et ENBW la largeur de bande équivalente de bruit, en Hz.
- F=128 Hz fixe ; N valeurs, durée DFT N/F
- f en Hz ; fenêtre périodique rect/Hann/Blackman
- padding ajoute des zéros ; CG et ENBW décrivent gain cohérent et bande de bruit

**Hypothèses**

- Cosinus isolé de phase 0,3 rad ; FFT monolatérale
- Amplitude corrigée par Σw et doublée hors DC/Nyquist
- Une raie hors case garde un biais dépendant de la fenêtre

**Techniques**

- DFT et sommes de Riemann
- Produit temporel/convolution spectrale
- Calibration d’amplitude et largeur de lobe

**Prévoir, manipuler, justifier**

1. Choisir f=13 Hz,N=256,rect : calculer la case native 26 avant de lire la FFT.
2. Passer à 13,375 Hz puis comparer les fenêtres ; observer lobe principal et lobes secondaires.
3. Augmenter uniquement padding ; distinguer F/N et F/(N·padding), et retrouver le facteur de calibrationΣw.

**Niveaux et prolongements**

- Sup : Sinusoïde mesurée et observation finie, introduction numérique.
- Spé : Fourier/DFT, résolution et calibration selon filière.
- Au-delà : ENBW, estimateurs spectraux et métrologie du bruit.

**Résultat attendu.** Un spectre avec fréquence, amplitude et limite de résolution explicitement distinguées.

### Laboratoire resolution

Chercher à séparer deux fréquences proches à partir d’une acquisition finie. Faire varier sa durée puis ajouter seulement des zéros permet de distinguer une meilleure résolution d’un affichage plus fin du même spectre.

**Objets et unités**

- Δf est l’écart des deux fréquences en Hz ; T est la durée d’acquisition en s. Le facteur q d’ajout de zéros multiplie le nombre de valeurs de calcul du spectre sans augmenter le nombre N de mesures.
- F=128 Hz ; N règle la durée T=N/F
- Deux fréquences 18 et 18+ΔfHz ; amplitudes égales
- padding règle l’interpolation, pas la durée

**Hypothèses**

- Signal sans bruit et phases initiales nulles
- Fenêtre de Hann : largeur entre premiers zéros environ 4/T
- Pas natif 1/T et résolution effective distincts

**Techniques**

- Formule de somme de cosinus
- Battements
- Compromis durée/fréquence

**Prévoir, manipuler, justifier**

1. Pour Δf=1 Hz, prévoir l’intervalle entre maxima et le premier zéro d’enveloppe.
2. Comparer N=64,padding=8 et N=512,padding=1 ; observer le même pas mais des lobes différents.
3. Exprimer le rôle de Δf·T et annoncer le critère de séparation utilisé, sans faire de 1/T une loi universelle.

**Niveaux et prolongements**

- Sup : Battements et lecture d’enveloppe.
- Spé : Résolution spectrale, fenêtres et acquisition.
- Au-delà : Superrésolution paramétrique, estimation et rapport signal/bruit.

**Résultat attendu.** Une comparaison démontrant que durée et interpolation produisent des informations différentes.

### Laboratoire spectrogramme

Suivre un signal dont la fréquence augmente au cours du temps. Calculer des spectres sur une fenêtre mobile révèle le compromis entre localisation temporelle et précision fréquentielle.

**Objets et unités**

- Un signal à fréquence balayée (chirp) possède une fréquence instantanée variable. f₀ et f₁ sont ses fréquences initiale et finale ; L est le nombre de points de la fenêtre mobile. STFT désigne la transformée de Fourier calculée sur ces fenêtres successives.
- F=128 Hz, durée 3 s ; chirp de f₀ à f₁
- L points par Hann mobile, avance 8 points
- Carte en dB relatifs au maximum, FFT locales complétées à 256 points

**Hypothèses**

- Fréquences du signal à fréquence balayée sous 64 Hz
- Carte relative, sans calibration absolue de puissance
- Une fenêtre locale ne rend pas exactement stationnaire un signal à fréquence balayée

**Techniques**

- Dérivation de phase
- Transformée de Fourier à fenêtre
- Analyse d’échelles temporelle/fréquentielle

**Prévoir, manipuler, justifier**

1. Calculer la pente pour 8→48 Hz en 3 s et prévoir la fréquence à 1,2 s.
2. Comparer L=16 puis 128 ; repérer largeur fréquentielle et étalement temporel.
3. Évaluer |k|L/F et F/L, puis expliquer la normalisation relative et le rôle de la ligne analytique.

**Niveaux et prolongements**

- Sup : Phase et fréquence instantanée ; lecture d’une carte guidée.
- Spé : Analyse temps–fréquence en prolongement du programme selon filière.
- Au-delà : STFT, ondelettes, réaffectation et signaux non stationnaires.

**Résultat attendu.** Une fenêtre choisie avec deux échelles et une carte dont les unités relatives sont comprises.

### Laboratoire modulation

Transporter un message lent sur une porteuse plus rapide, puis le retrouver par multiplication et filtrage. Les identités trigonométriques expliquent les bandes latérales et les erreurs de phase ou de fréquence du récepteur.

**Objets et unités**

- f_m est la fréquence du message et f_c celle de la porteuse ; m est la profondeur de modulation. Δf et φ sont les erreurs de fréquence et de phase de l’oscillateur utilisé pour retrouver le message.
- fm et fc en Hz ; m profondeur sans unité
- Δf est le désaccord local en Hz ; φ phase en degrés
- Barres positives = amplitudes de cosinus, non poids bilatéraux de Dirac

**Hypothèses**

- AM à porteuse transmise et canal idéal
- Démodulation par passe-bas idéal supprimant analytiquement les termes autour de 2fc
- Pour m>1, l’enveloppe signée traverse zéro

**Techniques**

- Produit de cosinus
- Translation de TF
- Démodulation et phase

**Prévoir, manipuler, justifier**

1. Avec m=0,7,fm=3,fc=30, prévoir fréquences et amplitudes des trois raies positives.
2. Comparer φ=0° et 90°, puis Δf=0,8 Hz ; distinguer disparition et battements.
3. Développer les produits trigonométriques et tester m=1,4 pour expliquer la limite d’une détection d’enveloppe.

**Niveaux et prolongements**

- Sup : Identités trigonométriques, modulation et détection guidées.
- Spé : Spectre AM et démodulation synchrone selon filière.
- Au-delà : Modulations IQ, porteuse supprimée et communications numériques.

**Résultat attendu.** Une chaîne d’émission/réception reconstruite avec les facteurs 1/2 et l’effet de phase.

### Laboratoire correlation_retard

Retrouver une impulsion retardée dans un signal bruité. Le maximum de corrélation estime le temps de vol ; un bilan des trajets permet ensuite de convertir ce retard en distance.

**Objets et unités**

- τ est le retard testé, en s ; c est la vitesse de propagation, en m/s. La corrélation mesure la ressemblance entre émission et réception pour ce retard ; le facteur deux de la distance provient du trajet aller-retour.
- Émission g, réception f ; Cfg(τ)=∫ḡ(t)f(t+τ)dt
- Cadence 200 Hz, grille de retard 5 ms ; retard en s
- Vitesse c en m/s ; distance cτ/2 ; graine choisit une réalisation de bruit

**Hypothèses**

- Fenêtre finie de 3 s, signaux réels, bruit gaussien
- Normalisation par les énergies globales ; module ≤1 par Cauchy–Schwarz
- Bruit et maxima secondaires peuvent déplacer le pic

**Techniques**

- Produit scalaire glissant
- Cauchy–Schwarz
- Temps de vol et convention de corrélation

**Prévoir, manipuler, justifier**

1. Pour un retard 0,6 s et c=350m/s, prévoir la distance et le signe du pic.
2. Augmenter le bruit puis changer la graine sans changer le retard ; observer la robustesse et ses limites.
3. Écrire Cfg=Cgg(τ−d), calculer le pas de distance et relier TF(Cff) à |f̂|².

**Niveaux et prolongements**

- Sup : Temps de vol et produit scalaire sur des données.
- Spé : Corrélation, normalisation et Fourier selon filière.
- Au-delà : Filtre adapté, radar/sonar et probabilités de détection.

**Résultat attendu.** Un retard de signe fixé, une distance calculée et une limite de précision sans certitude inventée.

### Laboratoire debruitage

Réduire un bruit sans effacer les variations utiles du signal. Comparer une moyenne glissante à un filtre récursif permet de mesurer séparément le bruit résiduel, le retard et la déformation introduite.

**Objets et unités**

- M est le nombre de valeurs moyennées ou l’échelle de mémoire du filtre récursif ; ρ est son coefficient de mémoire. RMS signifie valeur efficace : la racine de la moyenne des carrés sur l’intervalle de bilan.
- F=128 Hz ; signal sin(2πft)+0,25sin(4πft)
- M longueur de mémoire ; récursif de pôleρ=e^(−1/M)
- Écart type du bruit et RMS de sortie ; début du signal exclu du bilan

**Hypothèses**

- Bruit blanc centré indépendant, réalisation reproductible
- Filtres au repos initial ; transitoire partiellement écarté
- Bilan théorique stationnaire et RMS finie distincts

**Techniques**

- Convolution discrète et récurrence
- Linéarité
- Variance d’une somme indépendante et phase du filtre

**Prévoir, manipuler, justifier**

1. Pour moyenne M=9, prévoir le facteur 1/9 de variance et le retard 4/F.
2. Comparer mémoire 5 à 31 puis le récursif ; observer bruit résiduel et signal propre filtré.
3. Démontrer σ²Σh² et les deux facteurs théoriques ; expliquer pourquoi une sortie très lisse peut être une mauvaise mesure du signal utile.

**Niveaux et prolongements**

- Sup : Moyenne, bruit et retards, première expérimentation accompagnée.
- Spé : Filtres numériques et calcul de variance en lien avec probabilités.
- Au-delà : Filtrage de Wiener, bruit coloré et estimation optimale.

**Résultat attendu.** Un compromis bruit/distorsion chiffré à partir de deux références distinctes.



## Sources

Point de départ : recueil fourni par l’utilisateur, fiches M10 et M11, pages imprimées 98–111. Priorités : TP p.99 ; exercices 4, 5, 10, 11, 12 p.103–105 ; TP RC et intégrale de Dirichlet p.107 ; analyse du signal p.108. Les cours, expériences et problèmes sont rédigés pour cet atelier ; le PDF n’est pas redistribué.

[NIST DLMF, §1.8](https://dlmf.nist.gov/1.8) : séries de Fourier, Parseval et sommation de Poisson. [NIST DLMF, §1.14](https://dlmf.nist.gov/1.14) : transformées de Fourier et Laplace ; les signes et facteurs sont adaptés aux conventions explicitement affichées dans cet atelier.

[MIT OpenCourseWare, Alan V. Oppenheim, Signals and Systems : Sampling](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/) et [Sampling and the Discrete Fourier Transform](https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/resources/samplingdft/) : compléments sur échantillonnage, reconstruction, DFT et fenêtrage.
