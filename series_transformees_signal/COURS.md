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

**Objets et but.** N valeurs sont acquises à F=128 Hz, aux instants k/F, k=0,…,N−1. La durée DFT est T=N/F et le pas natif F/N. Une fréquence située entre deux cases produit une fuite spectrale. La fenêtre de Hann ou de Blackman réduit les lobes secondaires en élargissant le lobe principal ; le signal observé est le produit xkwk.

```text
Xj=Σk=0ᴺ⁻¹xkwk e^(−2iπjk/N)
Amplitude positive isolée ≈2|Xj|/Σwk
CG=(1/N)Σwk ; ENBW=FΣwk²/(Σwk)²
```

**Démonstration.** La fenêtre finie transforme une raie infiniment fine en une copie de son propre spectre. Diviser par Σw corrige le gain cohérent d’une raie sur une case ; cela ne corrige pas exactement tous les biais hors case ni le recouvrement de raies voisines. Les amplitudes DC et Nyquist ne sont pas doublées : ces cases n’ont pas une partenaire distincte dans la représentation monolatérale.

**Lire l’expérience.** Le zero padding n’ajoute aucune mesure. Il échantillonne plus densément le même polynôme trigonométrique et permet de mieux lire un maximum interpolé. Le banc affiche séparément F/N, F/(Nq), le gain cohérent et la bande équivalente de bruit, pour éviter de confondre calibration, interpolation et résolution.

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

## 53. Un chirp ne possède pas une seule fréquence permanente

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Objets et but.** Le chirp est x(t)=cos[2π(f₀t+kt²/2)]. Sa fréquence instantanée est la dérivée de sa phase divisée par 2π : ν(t)=f₀+kt. L’expérience dure 3 s et échantillonne à 128 Hz. Une fenêtre mobile de L valeurs permet de localiser les fréquences au cours du temps.

```text
STFTx(t₀,ν)=∫x(t)w(t−t₀)e^(−2iπνt)dt
νinst(t)=f₀+kt ; durée locale L/F ; pas natif F/L
```

**Démonstration.** On extrait chaque segment, le multiplie par une Hann et calcule une FFT locale. Une fenêtre courte suit un changement rapide mais possède un lobe spectral large. Une fenêtre longue réduit ce lobe, mais le chirp parcourt alors plusieurs fréquences pendant la fenêtre, ce qui étale aussi l’énergie. La carte affiche des dB relatifs à son propre maximum, avec un plancher −65 dB.

**Lire l’expérience.** Les zéros ajoutés à 256 points densifient les colonnes de fréquence ; ils ne changent pas la durée locale L/F. La ligne ν=f₀+kt sert de repère analytique. Une crête de carte est une estimation issue de données fenêtrées, pas une preuve que le signal était stationnaire dans chaque segment.

## 54. Un compromis contrôlé par deux largeurs

**Spé ; prolongement temps–fréquence · TP : spectrogramme**

**Propriété ciblée.** Pour un chirp linéaire, une fenêtre de durée τw voit une variation de fréquence |k|τw. Son propre étalement est de l’ordre de 1/τw. Leur comparaison donne un ordre de grandeur pour choisir une fenêtre adaptée au balayage.

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

**Objets et but.** Un signal utile contient une fondamentale et sa deuxième harmonique. Le banc ajoute un bruit blanc puis applique soit une moyenne glissante causale de M valeurs, soit un filtre récursif de pôle ρ=e^(−1/M). Il filtre aussi le signal utile seul : cette référence sépare la déformation du signal du bruit restant.

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

## Sources

Point de départ : recueil fourni par l’utilisateur, fiches M10 et M11, pages imprimées 98–111. Priorités : TP p.99 ; exercices 4, 5, 10, 11, 12 p.103–105 ; TP RC et intégrale de Dirichlet p.107 ; analyse du signal p.108. Les cours, expériences et problèmes sont rédigés pour cet atelier ; le PDF n’est pas redistribué.

[NIST DLMF, §1.8](https://dlmf.nist.gov/1.8) : séries de Fourier, Parseval et sommation de Poisson. [NIST DLMF, §1.14](https://dlmf.nist.gov/1.14) : transformées de Fourier et Laplace ; les signes et facteurs sont adaptés aux conventions explicitement affichées dans cet atelier.

[MIT OpenCourseWare, Alan V. Oppenheim, Signals and Systems : Sampling](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/) et [Sampling and the Discrete Fourier Transform](https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/resources/samplingdft/) : compléments sur échantillonnage, reconstruction, DFT et fenêtrage.
