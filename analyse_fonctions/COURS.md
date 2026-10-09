# Fonctions & Équations — 56 leçons

Recueil de A. R., Fonctions et fiches M5–M6. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.

## 01. Théorème de continuité : identifier un majorant intégrable

Spé · Laboratoire `continuite_gauss`

Pour une intégrale à paramètre F(a)=∫J f(a,t)dt, il faut distinguer le paramètre a et la variable intégrée t. Une continuité en a pour chaque t ne suffit pas lorsque J est non borné ou que l’intégrande présente une singularité. Le théorème de la page 63 demande un majorant intégrable indépendant du paramètre sur le domaine considéré.

f(a,t)=e⁻ᵗ²cos(at), a∈ℝ, t∈ℝ ; |f(a,t)|≤e⁻ᵗ².

Pour chaque t, a↦f(a,t) est continue. Pour chaque a, t↦f(a,t) est continue et intégrable. Le majorant φ(t)=e⁻ᵗ² est positif, indépendant de a et intégrable sur ℝ. Il en résulte que F est définie et continue sur tout ℝ.

La preuve s’écrit avant le calcul explicite. Une intégrande oscillante peut avoir une petite intégrale par compensation ; cela ne fournit pas une domination de sa valeur absolue. La courbe de φ encadre les lobes positifs et négatifs de f et explique pourquoi le théorème s’applique.

Dans une autre application, le majorant peut dépendre d’un voisinage compact de a et rester indépendant du paramètre courant dans ce voisinage. Cette domination locale suffit à démontrer la continuité en chaque point intérieur du domaine.

## 02. Gauss, Fourier et une équation différentielle pour calculer F

Spé · Prolongement · Laboratoire `continuite_gauss`

La continuité ne donne pas encore la valeur de l’intégrale. Pour dériver F, utiliser |∂f/∂a|≤|t|e⁻ᵗ², intégrable. Ainsi F′(a)=−∫ℝte⁻ᵗ²sin(at)dt. Comme (e⁻ᵗ²)′=−2te⁻ᵗ², une intégration par parties annule les termes de bord et simplifie l’intégrale.

F′(a)=−aF(a)/2 ; F(0)=√π ; F(a)=√πe⁻ᵃ²/⁴.

Cette méthode est emblématique : un théorème de dérivation sous l’intégrale fabrique une équation différentielle en paramètre ; une valeur connue fixe la solution. La partie imaginaire de ∫ℝe⁻ᵗ²e⁻ⁱᵃᵗdt est nulle par imparité. La formule est donc aussi une transformée de Fourier de la gaussienne.

Numériquement, on remplace ℝ par [−L,L]. Pour L>0, chaque queue est dominée par e⁻ᴸ²/(2L), car t/L≥1 sur [L,+∞[. Les deux queues donnent e⁻ᴸ²/L. Le laboratoire ajoute une borne de l’erreur des trapèzes sur la partie finie, calculée avec un majorant de la dérivée seconde en t. Une valeur petite de F ne garantit pas une petite erreur relative : l’erreur absolue est plus pertinente dans les régimes de forte compensation.

## 03. Un contre-exemple qui explique l’hypothèse de domination

Spé · Laboratoire `continuite_defaut`

Pour a>0 et t>0, poser fₐ(t)=e⁻ᵗ/ᵃ/a. Pour a=0, poser f₀(t)=0 ; au point t=0, fixer aussi fₐ(0)=0. Changer la valeur d’une intégrande en un seul point ne change pas son intégrale.

À chaque t>0 fixé, la décroissance exponentielle domine le facteur 1/a : fₐ(t)→0 quand a→0⁺. Le même résultat est vrai en t=0 avec la définition choisie. On a donc une convergence ponctuelle vers f₀ sur tout le domaine.

t=au ⇒ ∫₀∞fₐ(t)dt=∫₀∞e⁻ᵘdu=1 ; ∫₀∞f₀(t)dt=0.

L’intégrale n’est pas continue au paramètre 0. Les hypothèses de continuité ponctuelle ne suffisent pas : la masse reste égale à 1 mais se concentre dans une fenêtre de largeur comparable à a. Pour ε>0 fixé, la masse dans [0,ε] vaut 1−e⁻ᵋ/ᵃ et tend vers 1.

Le majorant manquant peut être identifié explicitement. Pour 0<t≤1, la borne supérieure de fₐ(t) sur 0<a≤1 est atteinte en a=t et vaut 1/(et). Tout majorant commun aurait une intégrale divergente près de 0. Le premier théorème de la page 63 ne peut donc pas être utilisé dans un voisinage comprenant a=0.

## 04. Domination locale et changement de variable adapté au pic

Spé · Prolongement · Laboratoire `continuite_defaut`

La difficulté se situe au bord a=0. Autour d’un a strictement positif, on peut choisir α∈[a/2,2a]. Comme 1/α≤2/a et e⁻ᵗ/ᵅ≤e⁻ᵗ/⁽²ᵃ⁾, un majorant local simple existe.

fα(t)≤(2/a)e⁻ᵗ/⁽²ᵃ⁾ ; ∫₀∞(2/a)e⁻ᵗ/⁽²ᵃ⁾dt=4.

Le théorème prouve la continuité de l’intégrale sur ]0,+∞[, où elle vaut effectivement 1. Il ne fournit aucun prolongement continu à 0. La différence entre domination locale à un point intérieur et domination jusqu’à une extrémité du domaine est une technique récurrente en analyse.

Une grille numérique uniforme sur [0,L] risque de manquer le pic dès que son pas devient grand devant a. En revanche, le changement de variable t=au transforme l’intégrande et le facteur dt en e⁻ᵘdu : la largeur du pic est normalisée. Les masses affichées dans le laboratoire utilisent les formules exactes, et non une somme qui pourrait donner une fausse disparition de la masse.

La famille illustre également la différence entre convergence ponctuelle et convergence en norme intégrale : ∫|fₐ−f₀|=1. Dire que chaque valeur converge ne signifie pas que la totalité de l’aire sous les courbes converge.

## 05. Frullani : compenser une singularité avant de dériver

Spé · Laboratoire `leibniz_frullani`

Étudier F(a,b)=∫₀∞(e⁻ᵃᵗ−e⁻ᵇᵗ)/t dt pour a,b>0. Il serait incorrect de séparer les deux termes : chacun comporte une divergence en 0. C’est leur différence qui est intégrable.

e⁻ᵃᵗ−e⁻ᵇᵗ=(b−a)t+O(t²) ; f(a,b,0)=b−a par prolongement.

À l’infini, le théorème des accroissements finis appliqué à c↦e⁻ᶜᵗ donne |f(a,b,t)|≤|b−a|e⁻ᵐⁱⁿ⁽ᵃ,ᵇ⁾ᵗ, ce qui prouve l’intégrabilité. Le signe de F est celui de b−a.

Fixer b et dériver en a : ∂f/∂a=−e⁻ᵃᵗ. Pour un point a>0 fixé, travailler sur le voisinage α∈[a/2,3a/2]. Le majorant e⁻⁽ᵃ/²⁾ᵗ est continu et intégrable. Le deuxième théorème de la page 63 donne ∂F/∂a=−1/a.

La domination doit être indépendante de α à l’intérieur du voisinage choisi. La notation « a fixé » désigne le centre du voisinage, pas le paramètre courant de l’intégrande. Cette distinction évite un majorant dépendant de la variable qu’il était censé contrôler uniformément.

## 06. Fixer une constante et contrôler les limites d’intégration

Spé · Laboratoire `leibniz_frullani`

De ∂F/∂a=−1/a, on déduit F(a,b)=−ln a+C(b). Le fait que b soit un paramètre ne permet pas de traiter C comme une constante absolue ; elle peut dépendre de b. Pour l’identifier, choisir a=b.

F(b,b)=0 ⇒ C(b)=ln b ⇒ F(a,b)=ln(b/a).

On retrouve les lois logarithmiques : F(a,c)=F(a,b)+F(b,c), et le changement t=u/a montre que F ne dépend que du rapport b/a. Le résultat donne de nombreuses intégrales impropres dont une primitive directe serait peu commode.

La troncature à L laisse une queue. La majoration de l’intégrande donne |F−∫₀ᴸf|≤|b−a|e⁻ᵐᴸ/m, avec m=min(a,b). Cette borne est volontairement simple et peut être large. Pour la dérivée, la queue a une valeur exacte e⁻ᵃᴸ/a en valeur absolue.

En calcul numérique, soustraire e⁻ᵃᵗ et e⁻ᵇᵗ pour t très petit perd des chiffres significatifs. La réécriture avec expm1, qui calcule précisément eᵘ−1 près de 0, respecte la compensation. Le quotient est prolongé par b−a en 0. Cette précaution illustre la différence entre une expression mathématiquement correcte et une évaluation numérique stable.

## 07. Dériver un paramètre enlève une difficulté de l’intégrande

Spé · Laboratoire `leibniz_arctan`

Pour a>0, définir F(a)=∫₀∞e⁻ᵃᵗsin(t)/t dt. En 0, sin(t)/t→1 ; à l’infini, la présence de e⁻ᵃᵗ assure l’intégrabilité absolue. La difficulté du facteur 1/t suggère de dériver par rapport à a.

∂f/∂a=−e⁻ᵃᵗsin t ; |∂f/∂α|≤e⁻⁽ᵃ/²⁾ᵗ pour α≥a/2.

Pour chaque point a>0, cette majoration locale est intégrable. Les hypothèses de Leibniz sont remplies et F′(a)=−∫₀∞e⁻ᵃᵗsin t dt. L’intégrale restante s’obtient par exponentielle complexe ou par deux intégrations par parties.

∫₀∞e⁻ᵃᵗsin t dt=1/(1+a²) ; F′(a)=−1/(1+a²).

L’intégrale inconnue est donc solution d’une équation différentielle en paramètre. Pour la déterminer, la primitive de F′ ne suffit pas : il faut une condition supplémentaire. Ici, une limite à l’infini remplace une valeur initiale.

## 08. Une condition à l’infini et la limite au bord du domaine

Spé · Prolongement · Laboratoire `leibniz_arctan`

Pour t≥0, |sin t|≤t. Il en résulte |F(a)|≤∫₀∞e⁻ᵃᵗdt=1/a. Ainsi F(a)→0 quand a→+∞. Comme F′(a)=−1/(1+a²), on obtient la constante d’intégration.

F(a)=π/2−arctan a=arctan(1/a), pour a>0.

Avec une pulsation ω réelle, le même raisonnement donne ∫₀∞e⁻ᵃᵗsin(ωt)/t dt=arctan(ω/a). Dériver en ω, sous domination e⁻ᵃᵗ, est une autre voie : la dérivée vaut ∫₀∞e⁻ᵃᵗcos(ωt)dt=a/(a²+ω²), et la valeur à ω=0 est nulle.

La formule suggère la limite π/2 quand a→0⁺. Mais le majorant e⁻⁽ᵃ/²⁾ᵗ dépend du point a et n’est plus intégrable uniformément jusqu’à 0. Identifier la limite de la formule n’est pas encore justifier l’égalité avec l’intégrale impropre non amortie ∫₀∞sin t/t dt : cette identification demande un argument d’Abel ou un contrôle indépendant de ses queues.

Pour a>0 et L>0, la queue absolue est au plus e⁻ᵃᴸ/(aL). L’enveloppe de la dérivée donne e⁻ᵃᴸ/a. En abaissant a, il faut augmenter la coupure pour obtenir la même borne ; le laboratoire rend cette nécessité visible.

## 09. Γ est C∞ : contrôler chaque ordre près de 0 et à l’infini

Spé · Laboratoire `derivees_gamma`

Pour a>0, Γ(a)=∫₀∞tᵃ⁻¹e⁻ᵗdt. La singularité éventuelle en 0 est intégrable car a−1>−1 ; à l’infini, l’exponentielle domine les puissances. Dériver n fois par rapport à a fait apparaître (ln t)ⁿ.

∂ᵏ[tᵃ⁻¹e⁻ᵗ]/∂aᵏ=tᵃ⁻¹(ln t)ᵏe⁻ᵗ.

Fixer un voisinage [m,M] de a, avec 0<m<a<M, et un entier n. Pour 0<t≤1, tᵅ⁻¹≤tᵐ⁻¹ ; pour t≥1, tᵅ⁻¹≤tᴹ⁻¹. Pour 0≤k≤n, |ln t|ᵏ≤1+|ln t|ⁿ.

φ(t)=tᵐ⁻¹(1+|ln t|ⁿ)e⁻ᵗ si t≤1 ; φ(t)=tᴹ⁻¹(1+(ln t)ⁿ)e⁻ᵗ si t≥1.

Près de 0, le changement s=−ln t transforme la majoration en une puissance de s multipliée par e⁻ᵐˢ ; à l’infini, l’exponentielle assure à nouveau l’intégrabilité. Le troisième théorème de la page 63 donne Γ∈Cⁿ et Γ⁽ᵏ⁾=∫∂ᵏf. Comme n est arbitraire, Γ est C∞ sur ]0,+∞[. Chaque compact du domaine possède ses majorants ; il n’est pas nécessaire d’en chercher un valable jusqu’à a=0.

## 10. Log-convexité : une inégalité intégrale devient une variance

Spé · Prolongement · Laboratoire `derivees_gamma`

La fonction pₐ(t)=tᵃ⁻¹e⁻ᵗ/Γ(a) est positive et d’intégrale 1. On peut lire les dérivées de Γ comme des moments du logarithme : E(ln t)=Γ′/Γ et E((ln t)²)=Γ″/Γ.

(ln Γ)″=Γ″/Γ−(Γ′/Γ)²=Var(ln t)>0.

La variance est strictement positive car ln t n’est pas constante pour cette densité positive sur ]0,+∞[. Cette interprétation probabiliste donne la convexité stricte de ln Γ. Sans probabilités, Cauchy–Schwarz appliqué à √pₐ et (ln t)√pₐ fournit exactement la même inégalité.

En particulier, pour 0≤θ≤1, Γ((1−θ)a+θb)≤Γ(a)¹⁻ᶿΓ(b)ᶿ. La récurrence Γ(a+1)=aΓ(a), obtenue par intégration par parties, relie les dérivées aux factorielles mais ne suffit pas à elle seule à caractériser une interpolation continue du factorial.

Le laboratoire intègre en u=ln t : Γ⁽ⁿ⁾(a)=∫ℝuⁿexp(au−eᵘ)du. Il conserve le facteur dt=eᵘdu. Les coupures u=−q ln 10 et t=T donnent des queues explicites. L’écart entre deux quadratures indique une sensibilité numérique ; les bornes affichées contrôlent les queues, pas automatiquement l’erreur de quadrature.

## 11. Dériver à tout ordre une transformée de Laplace

Spé · Laboratoire `derivees_laplace`

Pour a>0, F(a)=∫₀∞e⁻ᵃᵗdt=1/a. Dériver formellement sous l’intégrale produit (−t)ᵏe⁻ᵃᵗ. Le troisième théorème de la page 63 transforme ce calcul formel en démonstration lorsqu’on fournit les majorants requis.

Fixer a>0, un ordre n et un voisinage α∈[a/2,3a/2]. Pour t≥0 et 0≤k≤n, tᵏ≤1+tⁿ. Ainsi les dérivées partielles sont toutes dominées par une même fonction intégrable.

|(−t)ᵏe⁻ᵅᵗ|≤(1+tⁿ)e⁻⁽ᵃ/²⁾ᵗ.

Le théorème donne F⁽ᵏ⁾(a)=∫₀∞(−t)ᵏe⁻ᵃᵗdt. En dérivant 1/a, on en déduit l’identité valable à chaque ordre entier.

∫₀∞tⁿe⁻ᵃᵗdt=n!/aⁿ⁺¹.

On peut aussi la prouver par n intégrations par parties, ou avec u=at et Γ(n+1)=n!. Les méthodes se contrôlent mutuellement. Cette identité est un outil central pour les transformées de Laplace, les moments de lois exponentielles et les modèles linéaires dont on résout les équations différentielles dans le domaine transformé.

## 12. Monotonie complète et queues d’intégrale

Spé · Prolongement · Laboratoire `derivees_laplace`

Une fonction F est complètement monotone sur ]0,+∞[ si elle est C∞ et si (−1)ⁿF⁽ⁿ⁾≥0 pour tout entier n≥0. Ici, la représentation intégrale donne un résultat encore strict : l’intégrande tⁿe⁻ᵃᵗ est positive pour t>0.

(−1)ⁿF⁽ⁿ⁾(a)=n!/aⁿ⁺¹>0.

F décroît, F″ est positive, F‴ est négative, et ainsi de suite. Le même raisonnement fonctionne pour ∫e⁻ᵃᵗw(t)dt avec w≥0, sous des hypothèses de domination adaptées. Une propriété de signe d’une densité se transmet donc aux dérivées de sa transformée.

Pour l’intégration numérique, la densité tⁿe⁻ᵃᵗ atteint son maximum en n/a. Une grande valeur de n, ou un petit a, déplace la partie importante de l’aire vers la droite. Une coupure fixe peut alors perdre une proportion majeure de la masse.

Rₙ(L)=∫L∞tⁿe⁻ᵃᵗdt=e⁻ᵃᴸ∑ⱼ₌₀ⁿ[n!/(n−j)!] Lⁿ⁻ʲ/aʲ⁺¹.

Cette formule exacte provient d’intégrations par parties répétées et permet de contrôler la troncature. À l’ordre n, la fraction capturée jusqu’à L vaut 1−Rₙ(L)/(n!/aⁿ⁺¹). Le laboratoire oppose cette masse à la simple position du maximum : avoir le maximum dans la fenêtre ne signifie pas encore avoir toute la queue.

## 13. Du champ de pentes à la solution exacte du TP

Sup · Laboratoire `euler_rk4`

Une EDO y′=f(x,y) ne donne pas directement les valeurs de y : elle indique la **pente** d’une courbe lorsqu’elle passe par (x,y). La condition y(0)=y₀ choisit une trajectoire. Le champ de petites directions du laboratoire représente (1,f(x,y)), ramené à une longueur lisible ; cette normalisation ne change pas la pente.

Dans le TP p. 69, f(x,y)=cos(x)(y+1). Poser z=y+1 transforme l’équation en z′=cos(x)z. Multiplier par e^(−sin x) donne (ze^(−sin x))′=0. Par conséquent **y(x)=(y₀+1)e^(sin x)−1**, sur ℝ. Cette démonstration inclut le cas y₀=−1 sans diviser par y+1.

Pour y₀=0, y′ a le signe de cos x ; les maxima sont atteints en π/2+2kπ, avec valeur e−1, et les minima en 3π/2+2kπ, avec valeur e^(−1)−1. Une formule exacte fournit ici un étalon pour l’expérience numérique.

**Technique attendue :** changement de fonction, équation linéaire du premier ordre, condition initiale puis tableau de variations. Le dessin aide à interpréter ; la vérification par dérivation démontre.

## 14. Euler, RK4 et les deux erreurs à distinguer

Sup → Spé · Laboratoire `euler_rk4`

Sur xⱼ=jh, Euler explicite pose yⱼ₊₁=yⱼ+h f(xⱼ,yⱼ). Son erreur sur *un* pas, en partant d’une valeur exacte, est O(h²) ; les erreurs propagées sur un intervalle fixé donnent généralement une erreur globale O(h). Ces deux ordres répondent à deux questions différentes.

RK4 calcule k₁=f(x,y), k₂=f(x+h/2,y+hk₁/2), k₃=f(x+h/2,y+hk₂/2), k₄=f(x+h,y+hk₃), puis y_(suiv)=y+h(k₁+2k₂+2k₃+k₄)/6. Pour une fonction suffisamment régulière et un intervalle fixé, son erreur globale est O(h⁴).

Le laboratoire mesure E(h)=maxⱼ|yⱼ−y(xⱼ)| et l’ordre p≈log₂[E(h)/E(h/2)]. Une droite de pente p apparaît dans des coordonnées logarithmiques lorsque le maillage est assez fin. Un pas grossier, un intervalle trop long ou les arrondis peuvent masquer ce comportement.

**Application :** choisir une précision avant de résoudre un problème sans solution exacte. Il faut alors comparer des maillages successifs, surveiller un bilan ou une quantité conservée et ne pas confondre le lissage du graphique avec la précision.

## 15. Le facteur intégrant : le signe se retrouve par dérivation

Sup · Laboratoire `facteur_integrant`

On étudie y′+a(x)y=c(x), avec a,c continues sur un intervalle I. Prendre une primitive A de a, puis calculer **(eᴬy)′=eᴬ(y′+ay)=eᴬc**. L’intégration entre x₀ et x donne y(x)=e^(−A(x))[e^(A(x₀))y₀+∫_(x₀)^(x)e^(A(s))c(s)ds]. Le facteur devant la parenthèse est e^(−A).

Dans l’atelier a(x)=a+bx et c(x)=Fcos(ωx), donc A(x)=ax+bx²/2 et x₀=0. On peut aussi écrire l’intégrale avec le noyau e^(−(A(x)−A(s))). Pour 0≤s≤x et a,b≥0 ce noyau est au plus 1 ; cette forme évite de produire séparément des exponentielles très grandes.

Les constantes d’intégration ne sont pas une décoration : le premier terme y₀e^(−A(x)) impose la donnée initiale. La vérification consiste à dériver la formule et à l’évaluer en 0.

**Applications CPGE :** circuit RC soumis à une tension variable, bilan thermique avec coefficient d’échange variable ou relaxation chimique linéarisée. Chaque application demande de préciser les unités et le domaine de validité.

## 16. Sensibilité, mémoire et variation des constantes

Spé · Laboratoire `facteur_integrant`

Deux solutions du même second membre, séparées initialement de d₀, ont pour différence d(x)=d₀e^(−(A(x)−A(x₀))). Ce résultat permet de mesurer la sensibilité à la préparation initiale sans résoudre deux problèmes complets.

Lorsque a(x)≥0 à droite de x₀, l’écart ne croît pas. Cela ne veut pas dire que chaque solution décroît : le forçage c peut faire osciller y. Il faut distinguer **évolution de la solution** et **évolution de la différence de deux solutions**.

Le noyau e^(−∫ₛˣa(u)du) pondère les contributions passées. Pour a constant positif, une contribution ancienne décroît exponentiellement ; pour a+bx, la mémoire dépend des deux instants. La linéarité permet de sommer ces contributions, même si le forçage n’est pas sinusoïdal.

La quadrature de Gauss du laboratoire évalue cette intégrale. Un RK4 indépendant intègre l’EDO elle-même : leur accord fournit un contrôle numérique. Il ne prouve pas qu’un modèle thermique ou électrique serait pertinent sans ses hypothèses physiques.

## 17. Unicité : la démontrer ou construire un contre-exemple

Spé → Au-delà · Laboratoire `cauchy_lipschitz`

Pour une EDO linéaire à coefficients continus, une donnée initiale détermine une solution unique sur l’intervalle de continuité. Le théorème de Cauchy–Lipschitz prolonge cette propriété à certaines EDO non linéaires : f doit être continue et **localement lipschitzienne par rapport à y**. Ce théorème général est présenté comme un prolongement, sans remplacer les démonstrations linéaires accessibles en CPGE.

La continuité seule ne suffit pas. Avec f(y)=2√max(y,0), les fonctions yτ(t)=0 pour t≤τ et yτ(t)=(t−τ)² pour t≥τ, τ≥0, sont C¹. À l’instant τ, les valeurs valent 0 et les dérivées valent 0 des deux côtés. Elles vérifient toutes y′=f(y) et y(0)=0.

Le quotient |f(ε)−f(0)|/ε=2/√ε tend vers +∞. Aucune constante locale ne borne donc ce quotient près de 0 : l’hypothèse de Lipschitz manque exactement au point de départ.

## 18. Existence, unicité et stabilité sont trois propriétés distinctes

Spé → Au-delà · Laboratoire `cauchy_lipschitz`

Pour y′=λy, la solution de donnée ε est εe^(λt). Deux trajectoires peuvent rester proches, ou s’éloigner rapidement si λ>0, tout en étant chacune parfaitement unique. L’unicité interdit deux trajectoires pour *la même* donnée ; la stabilité compare des données voisines.

Le cas y′=2√max(y,0) montre aussi une limite du calcul numérique. Euler ou RK4, partant exactement de y=0, obtiennent y=0 à chaque pas. Cela ne démontre pas l’unicité : ces méthodes sélectionnent une solution parmi plusieurs. L’existence d’autres solutions exige une construction ou un raisonnement.

Enfin, l’échec d’une hypothèse suffisante ne prouve pas à lui seul l’échec de la conclusion. Pour établir la non-unicité, le laboratoire donne trois solutions et les vérifie ; constater seulement que f n’est pas lipschitzienne serait insuffisant.

**Réflexe formateur :** nommer la propriété étudiée, écrire ses quantificateurs, puis fournir la preuve adaptée — différence de solutions, formule explicite ou contre-exemple.

## 19. Une solution maximale peut exploser en temps fini

Spé → Au-delà · Laboratoire `explosion_logistique`

Pour y′=ay² avec a>0 et y(0)=y₀>0, on obtient (1/y)′=−a et **y(t)=y₀/(1−ay₀t)**. Le premier pôle à droite est t*=1/(ay₀). La solution contenant 0 est définie sur ]−∞,t*[ ; elle ne peut être prolongée à t* comme fonction réelle continue.

Le second membre ay² est dérivable en y, donc localement lipschitzien. L’explosion est compatible avec l’existence et l’unicité *locales*. Pour une existence globale, il faut d’autres contrôles, par exemple empêcher y de quitter tout domaine borné en temps fini.

L’expression algébrique existe aussi pour t>t*, mais cette branche n’est pas un prolongement de la solution initiale à travers le pôle. Une courbe ne doit pas relier les deux côtés de l’asymptote.

Le mot « maximale » porte sur le domaine de définition par prolongement. Il ne signifie pas que la fonction atteint un maximum, ni qu’elle domine toutes les autres solutions.

## 20. Logistique : équilibres, monotonie et linéarisation

Sup → Spé · Laboratoire `explosion_logistique`

La loi z′=rz(1−z/K), r,K>0, possède deux équilibres : 0 et K. Pour 0<z<K, z′>0 ; pour z>K, z′<0. Une donnée positive conduit à z(t)=K/[1+(K/z₀−1)e^(−rt)] et z(t)→K lorsque t→+∞.

Près de K, poser z=K+η. On trouve η′=−rη−(r/K)η². Au premier ordre, η≈η₀e^(−rt) : le taux de retour vaut r. Près de 0, z′≈rz : les petites perturbations positives croissent ; 0 est instable à droite.

Cette étude rassemble plusieurs techniques : recherche des zéros du second membre, tableau de signes, séparation des variables, limites et développement limité autour d’un équilibre. La formule explicite confirme le raisonnement qualitatif.

Comparer à y′=ay² montre ce que change le terme de saturation. La logistique évite l’explosion pour les données positives à droite ; elle ne transforme pas tout modèle non linéaire en modèle global. Les paramètres et le sens physique du freinage doivent être justifiés.

## 21. Équation caractéristique : trois régimes, deux données

Sup · Laboratoire `oscillateur_resonance`

L’équation libre y″+2ζω₀y′+ω₀²y=0 conduit à r²+2ζω₀r+ω₀²=0. Pour 0≤ζ<1, les racines sont −ζω₀±iω₀√(1−ζ²) et le mouvement combine sinus et cosinus amortis. Pour ζ=1, y=(A+Bt)e^(−ω₀t). Pour ζ>1, il existe deux exponentielles réelles décroissantes.

Une donnée y(0) fixe seulement une combinaison des deux constantes. Il faut aussi y′(0) pour déterminer le mouvement : c’est un **problème de Cauchy d’ordre 2**. Les deux conditions sont prises au même instant.

Un amortissement critique ne donne pas un sinus de fréquence nulle : c’est la racine double qui impose le facteur t. Le laboratoire change de formule au seuil, au lieu de diviser par une pulsation devenue nulle.

Le portrait (y,y′) visualise la position et la vitesse. En mouvement libre, son champ est autonome ; sous forçage il dépend aussi du temps. Le champ affiché est alors explicitement figé à t=0 tandis que la trajectoire tient compte de tout le forçage.

## 22. Résonance : régime établi, croissance et bilan

Sup → Spé · Laboratoire `oscillateur_resonance`

Pour le forçage Fcos(ωt), une particulière hors résonance non amortie s’obtient en écriture complexe : U=F/(ω₀²−ω²+2iζω₀ω). L’amplitude établie est |U|. La partie homogène ajuste les données initiales et constitue le transitoire.

Si ζ>0, maximiser |U| donne ω_(res)=ω₀√(1−2ζ²), lorsqu’il existe un maximum à pulsation positive, donc pour ζ<1/√2. Résonance en déplacement et pulsation propre ne sont pas exactement identiques.

Si ζ=0 et ω=ω₀, le dénominateur s’annule. Une particulière est **Ft sin(ω₀t)/(2ω₀)** : son enveloppe croît avec t. Il n’existe pas d’amplitude stationnaire finie. Le laboratoire compare alors des maxima sur un horizon fixé.

Avec E=[(y′)²+ω₀²y²]/2, l’équation multipliée par y′ donne E′=Fcos(ωt)y′−2ζω₀(y′)². Intégrer donne E−E₀=W−D. C’est un contrôle portant sur la trajectoire entière, plus instructif qu’un seul accord à l’instant final.

## 23. Variation des constantes et Wronskien

Spé · Laboratoire `variation_constantes`

Pour y″−5y′+6y=g(x), les solutions homogènes y₁=e^(2x), y₂=e^(3x) ont W=y₁y₂′−y₁′y₂=e^(5x)≠0. Elles constituent donc une base de l’espace des solutions homogènes.

Écrire y_p=a(x)y₁+b(x)y₂ puis imposer a′y₁+b′y₂=0 simplifie la dérivation. L’équation donne a′y₁′+b′y₂′=g. Par Cramer : **a′=−gy₂/W, b′=gy₁/W**.

Pour l’exercice 1 p. 71, g=eˣ/cosh²x : a′=−e^(−x)/cosh²x et b′=e^(−2x)/cosh²x. Des intégrales définies de 0 à x évitent de perdre une constante ; elles produisent une particulière de données initiales nulles.

Une particulière ne fournit pas encore la solution du problème de Cauchy. Ajouter Ae^(2x)+Be^(3x) puis résoudre A+B=y₀ et 2A+3B=v₀ donne A=3y₀−v₀ et B=v₀−2y₀.

## 24. Du Wronskien à la réponse impulsionnelle initiale

Spé → Au-delà · Laboratoire `variation_constantes`

En réunissant les deux intégrales de coefficients, on obtient y_p(x)=∫₀ˣK(x−s)g(s)ds, avec **K(u)=e^(3u)−e^(2u)**. Le noyau satisfait K(0)=0, K′(0)=1 et K″−5K′+6K=0.

Dériver sous l’intégrale donne y_p′=∫₀ˣK′(x−s)g(s)ds puis y_p″=g(x)+∫₀ˣK″(x−s)g(s)ds. Le terme g(x) vient de K′(0)=1. Par conséquent y_p″−5y_p′+6y_p=g et y_p(0)=y_p′(0)=0.

Le noyau exprime la superposition de réponses à des sollicitations élémentaires. Cette construction est un pont entre variation des constantes, convolution et transformée de Laplace.

Les deux modes homogènes sont croissants. Une petite erreur de donnée initiale peut être amplifiée, même si la formule et l’algorithme sont corrects. Le graphique d’écart Gauss/RK4 distingue cette sensibilité du problème et la précision des deux calculs.

## 25. Euler–Cauchy : la forme normale et ses limites

Spé · Laboratoire `euler_cauchy`

L’équation x²y″+xy′−y=x²/(1−x²) présente trois abscisses particulières : ±1 rendent le second membre singulier ; 0 annule le coefficient dominant. Sur un intervalle évitant ces points, on peut diviser par x² et appliquer les résultats linéaires usuels.

Pour l’homogène, chercher y=xᵐ donne m(m−1)+m−1=m²−1. Les deux solutions sont x et 1/x, indépendantes sur tout intervalle évitant 0. Le changement x=eᵗ, x>0, transforme aussi x²y″+xy′ en la dérivée seconde de Y(t)=y(eᵗ).

Une solution particulière est y_p=[(x²−1)ln|(1+x)/(1−x)|+2x]/(4x). Le laboratoire la vérifie par ses dérivées et par le résidu de l’équation. Une formule contenant ln|…| peut être valable sur plusieurs intervalles ; les constantes de résolution sont choisies séparément sur chacun.

Dans un prolongement régulier à travers 0, le coefficient de 1/x doit disparaître. Il reste le mode C₁x et une particulière régulière. Le coefficient annulé exige une étude directe ; une division par x² aurait supprimé précisément le point à examiner.

## 26. Série entière : résoudre et régulariser un calcul

Spé · Laboratoire `euler_cauchy`

Pour |x|<1, x²/(1−x²)=∑ₙ≥₁x^(2n). Sur un monôme xᵐ, l’opérateur L[y]=x²y″+xy′−y agit par multiplication par m²−1. On cherche donc y_p=∑ₙ≥₁x^(2n)/(4n²−1).

Le coefficient du mode x reste libre car L[x]=0. Les termes impairs de rang au moins 3 sont nuls. La particulière commence par x²/3+x⁴/15+x⁶/35 ; ainsi y_p(0)=y_p′(0)=0 et y_p″(0)=2/3.

La série a rayon 1 : le rapport des coefficients tend vers 1 lorsqu’on la considère comme série en x². Une somme de N termes approche bien la fonction près de 0 mais plus lentement près de |x|=1.

Cette série sert aussi au calcul numérique. Dans la formule logarithmique, deux termes presque égaux se soustraient au voisinage de 0. La série évite cette perte de précision. Elle ne doit en revanche pas être utilisée pour |x|>1, où elle diverge.

## 27. Une EDO homogène et un raccordement à vérifier

Spé · Laboratoire `riccati`

L’exercice 3 p. 71 est xy′=y+√(x²+y²). Hors de 0, poser z=y/x. Pour x>0, xz′=√(1+z²), d’où argsh z=ln x+A. Pour x<0, la racine contient |x| ; ce signe modifie l’équation transformée.

Les branches compatibles avec un raccordement continu en 0 donnent la famille **y=cx²−1/(4c), c>0**. Elle est en fait dérivable sur ℝ. Pour la vérifier, noter x²+y²=(cx²+1/(4c))². Comme c>0, la racine vaut cx²+1/(4c), et xy′=2cx²=y+√(x²+y²).

À x=0, l’équation impose y(0)+|y(0)|=0, donc y(0)≤0. La famille obtenue a y(0)<0 et y′(0)=0. Une condition imposée au point singulier doit être vérifiée directement.

L’équation est dite homogène après division et substitution y/x ; elle n’a pas la forme quadratique caractéristique d’une équation de Riccati. Le laboratoire présente séparément les deux méthodes.

## 28. Riccati : une non-linéarité quadratique se linéarise

Spé → Au-delà · Laboratoire `riccati`

Une équation de Riccati a la forme z′=a(t)z²+b(t)z+c(t). Dans l’exemple z′=z²−1, poser **z=−u′/u** sur un intervalle où u≠0. Alors z′=z²−u″/u, et l’équation linéaire u″=u convient.

Pour imposer z(0)=z₀, choisir u(0)=1 et u′(0)=−z₀. On obtient u=cosh t−z₀sinh t et z=(z₀cosh t−sinh t)/(cosh t−z₀sinh t). Le changement n’est valable que tant que le dénominateur reste non nul.

Les équilibres z=−1 et z=1 sont visibles dans z′=(z−1)(z+1). −1 est attractif, 1 est répulsif. Si z₀>1, u s’annule en t*=argth(1/z₀) et z explose à droite. L’EDO linéaire u″=u reste régulière : c’est le quotient qui devient singulier.

**Technique de prolongement :** reconnaître une structure, calculer la dérivée du changement et surveiller son domaine. Linéariser un problème n’autorise pas à oublier les divisions introduites.

## 29. Trois bilans deviennent une équation matricielle

Spé · Laboratoire `lineaire_systeme`

Yᵢ(t) est la quantité présente dans le réservoir i. Les échanges symétriques de taux kᵢⱼ donnent Y₁′=k₁₂(Y₂−Y₁)+k₁₃(Y₃−Y₁)−δY₁, et deux équations analogues. Sous forme matricielle : **Y′=AY**.

La matrice A est symétrique ; les termes hors diagonale sont les taux positifs, et la diagonale est l’opposé de la somme des taux sortants, moins δ. Sommer les trois bilans annule tous les échanges : S′=−δS. Pour S(0)=1, S=e^(−δt).

Diagonaliser A=QDQᵀ transforme le système en Z′=DZ, avec Z=QᵀY. Chaque coordonnée propre satisfait Zⱼ′=λⱼZⱼ, donc Zⱼ=Zⱼ(0)e^(λⱼt). Revenir à Y donne l’exponentielle matricielle e^(tA)=Q diag(e^(λⱼt))Qᵀ.

Ce système à trois dimensions relie réellement algèbre linéaire et analyse. Les valeurs propres ne sont pas seulement calculées : elles donnent les temps de relaxation et les grandeurs conservées.

## 30. Mode conservé et deux modes de relaxation

Spé → Au-delà · Laboratoire `lineaire_systeme`

Sans perte, A(1,1,1)ᵀ=0. Le mode uniforme est constant. Pour tout vecteur v, −vᵀAv=k₁₂(v₁−v₂)²+k₂₃(v₂−v₃)²+k₁₃(v₁−v₃)²≥0. Les deux autres valeurs propres sont négatives puisque les trois taux sont strictement positifs.

La projection de Y₀ sur le mode uniforme donne (S₀/3)(1,1,1). Les autres composantes décroissent : à quantité conservée 1, chaque réservoir tend vers 1/3. Le plus petit taux non nul donne la relaxation la plus lente.

Avec perte uniforme δ, tous les modes sont multipliés par e^(−δt). Les proportions P=Y/S satisfont le système sans perte ; elles tendent toujours vers 1/3. Il faut distinguer une quantité qui tend vers 0 d’une proportion qui tend vers 1/3.

Le portrait de phase se situe dans le triangle P₁≥0, P₂≥0, P₁+P₂≤1, puisque P₃=1−P₁−P₂. La représentation plane respecte la conservation au lieu d’oublier le troisième réservoir.

## 31. Deux conditions aux bords : une autre question que Cauchy

Spé · Laboratoire `green_bords`

Le problème de Cauchy y(0)=α, y′(0)=β fixe deux données au même point et admet une solution unique lorsque les coefficients sont continus. Les conditions y(0)=y(π)=0 imposent deux valeurs en deux points ; l’argument de Cauchy ne s’y applique pas automatiquement.

Considérer y″+λy=f sur [0,π]. Pour λ>0, une solution homogène s’annulant en 0 est Csin(√λx). Elle s’annule aussi en π pour tout C lorsque λ=n². Ces valeurs créent un noyau non nul pour le problème aux bords.

Pour f=a sin x+b sin(2x), hors λ=1,4, la particulière a sin x/(λ−1)+b sin(2x)/(λ−4) satisfait les bords. Si λ n’est aucun carré entier positif, elle est unique. Si λ=9, par exemple, on peut encore ajouter Csin(3x).

La méthode de tir démarre y(0)=0,y′(0)=1. Pour l’homogène, sa valeur finale sin(π√λ)/√λ détecte les valeurs résonantes ; à λ=0 la limite vaut π. Un zéro signifie que la pente initiale ne peut pas être déterminée par la seule valeur finale.

## 32. Compatibilité : l’alternative se prouve par intégration

Spé → Au-delà · Laboratoire `green_bords`

À λ=n², multiplier l’équation par s(x)=sin(nx). Les deux intégrations par parties utilisent y(0)=y(π)=s(0)=s(π)=0 et s″=−n²s. Il vient **∫₀^π f(x)sin(nx)dx=0**. C’est une condition nécessaire d’existence.

Pour le second membre du laboratoire, les sinus sont orthogonaux : ∫sin²(nx)=π/2, et ∫sin(mx)sin(nx)=0 pour m≠n. À λ=1, il faut a=0 ; à λ=4, il faut b=0. Si cette condition manque, il n’existe aucune solution.

Si la condition est satisfaite, la partie non résonante donne une particulière, et Csin(nx) reste libre. Il existe alors une infinité de solutions. Le curseur « amplitude libre » modifie réellement la solution sans changer l’équation ni les bords.

La proximité d’une valeur résonante produit une grande réponse : un coefficient contient 1/(λ−n²). Cette sensibilité correspond au phénomène physique de résonance. À la valeur exacte, il faut traiter la compatibilité ; remplacer un dénominateur nul par un petit nombre fabriquerait une fausse solution.

## 33. Cauchy additive : calculer d’abord les valeurs imposées

Sup · Laboratoire `cauchy_additive`

Une équation fonctionnelle est une égalité portant sur une fonction inconnue, valable pour tous les paramètres indiqués. Chercher f:ℝ→ℝ telle que f(x+y)=f(x)+f(y). Il faut prouver que les solutions trouvées sont les seules, puis vérifier qu’elles satisfont effectivement l’équation.

Les premières substitutions coûtent peu : x=y=0 donne f(0)=0 ; y=−x donne f(−x)=−f(x). La fonction est impaire. Une récurrence donne f(nx)=nf(x) pour les entiers naturels n, puis pour tous les entiers grâce à l’imparité.

f(x/n)=f(x)/n ; f(p/n)=(p/n)f(1), pour p∈ℤ et n≥1.

Les valeurs sur ℚ sont donc déterminées par une seule valeur, a=f(1). Cette étape est algébrique : elle n’utilise pas la continuité. Pour atteindre un réel x, choisir une suite de rationnels rₙ qui converge vers x. Si f est continue, f(x)=lim f(rₙ)=ax.

Enfin, ax vérifie a(x+y)=ax+ay : la réciproque est établie. Dans le laboratoire, une sinusoïde ajoutée à une droite sert à voir qu’une forme graphique plausible ne satisfait pas automatiquement l’équation. Chaque case de la carte évalue le résidu pour un couple (x,y).

## 34. Régularité, dérivation et portée d’un contrôle numérique

Sup → Spé · Laboratoire `cauchy_additive`

Il suffit que f soit continue en un point x₀ : f(x₀+h)−f(x₀)=f(h) montre alors sa continuité en 0. Puis f(x+h)−f(x)=f(h) établit la continuité partout. Une autre hypothèse suffisante est la dérivabilité en 0.

Si f est dérivable en 0 : [f(x+h)−f(x)]/h=f(h)/h→f′(0).

La dérivée est donc la même en chaque point. On retrouve f(x)=f′(0)x puisque f(0)=0. Cette preuve fait le lien entre équations fonctionnelles et équations différentielles : f′=a est un problème initial très simple.

Sans régularité, le passage de ℚ à ℝ est illégitime. L’additivité ne prouve pas, à elle seule, que la fonction est linéaire sur ℝ. Ce point est une limite de la méthode, et non un détail à supprimer dans une rédaction de concours.

Pour le candidat ax+b sin x, le défaut vaut b[sin(x+y)−sin x−sin y]. À x=y, il devient b[sin(2x)−2sin x]. Il est nul pour b=0 ; pour b≠0, trouver un seul couple donnant une valeur non nulle suffit à rejeter le candidat. En revanche, vérifier un nombre fini de couples ne suffit jamais à démontrer une identité pour tous les réels.

## 35. Quand un produit devient une somme : le logarithme

Sup · Laboratoire `cauchy_multiplicative`

Sur ]0,+∞[, chercher une fonction continue telle que f(xy)=f(x)+f(y). Le domaine est essentiel : il est stable par multiplication, inversion et logarithme réel. En x=y=1, on obtient f(1)=0. En y=1/x, on obtient f(1/x)=−f(x).

Le bon changement de variable transforme l’opération qui apparaît dans l’équation. Poser h(u)=f(eᵘ) pour u∈ℝ. Alors eᵘeᵛ=eᵘ⁺ᵛ, et h vérifie une équation additive.

h(u+v)=h(u)+h(v) ; h continue ⇒ h(u)=au ⇒ f(x)=a ln x.

La réciproque vient de ln(xy)=ln x+ln y. Pour déterminer a, une valeur comme f(e), ou la dérivée f′(1) lorsqu’elle est disponible, suffit. Par exemple, f(2)=3 donne a=3/ln 2.

Le candidat perturbé du laboratoire vaut a ln x+b(ln x)². Sa version en variable u est au+bu² ; son résidu vaut 2buv. Le défaut se voit donc même si la fonction est monotone sur une petite fenêtre. L’axe de la carte est u=ln x : une même longueur y représente un rapport multiplicatif, et non une différence additive.

## 36. Fonctions multiplicatives continues : justifier la positivité

Sup → Spé · Laboratoire `cauchy_multiplicative`

Considérer maintenant f(xy)=f(x)f(y), sur x,y>0. La fonction nulle est une solution à isoler dès le début. Si f n’est pas nulle, choisir un x pour lequel f(x)≠0 ; l’équation à y=1 donne alors f(1)=1.

f(x)f(1/x)=1 ; f(x)=f(√x)²>0.

La première relation interdit les zéros. La seconde assure la positivité, sans avoir à la poser comme une hypothèse indépendante. On peut donc appliquer le logarithme : h(u)=ln f(eᵘ) est continue et additive. Ainsi h(u)=au, et **f(x)=xᵃ**. Avec la solution nulle, on a la classification complète dans cette classe de fonctions continues réelles.

La réciproque se vérifie directement avec (xy)ᵃ=xᵃyᵃ. Les exposants a peuvent être négatifs ou nuls : a=−1 donne l’inverse, a=0 donne la fonction constante 1, distincte de la fonction nulle.

Si f est dérivable, une méthode complémentaire consiste à dériver l’équation en y puis à poser y=1 : xf′(x)=f′(1)f(x). Résoudre cette équation différentielle sur ]0,+∞[ avec f(1)=1 retrouve la puissance. Les conditions initiales et le domaine excluant 0 doivent figurer dans la rédaction.

## 37. D’Alembert : distinguer la solution nulle et la parité

Sup → Spé · Laboratoire `dalembert`

L’équation f(x+y)+f(x−y)=2f(x)f(y) ressemble aux formules d’addition du cosinus. La ressemblance suggère des candidats ; elle ne les identifie pas encore tous. Il faut commencer par les valeurs particulières.

À y=0, 2f(x)=2f(x)f(0). Si f n’est pas identiquement nulle, f(0)=1. À x=0, on obtient f(y)+f(−y)=2f(y), donc f est paire. Si f est dérivable en 0, f′(0)=0.

f≡0 ; ou f(0)=1 et f(−x)=f(x).

Les formules d’addition montrent que cos(kx) et cosh(kx) conviennent pour chaque réel k. La fonction constante 1 correspond à k=0. La fonction nulle convient aussi, mais elle n’a pas f(0)=1 : la séparer évite une division injustifiée.

Le laboratoire affiche une carte à deux variables. L’égalité à y=0 seule ne suffit pas, pas plus que la parité seule : une perturbation bx² conserve ces deux premières conditions mais viole généralement l’équation complète. La méthode de résolution doit donc aller au-delà de ces substitutions nécessaires.

## 38. Une équation fonctionnelle produit un problème initial

Spé · Laboratoire `dalembert`

Supposer f de classe C² et non nulle. Deux dérivations par rapport à y donnent f″(x+y)+f″(x−y)=2f(x)f″(y). En y=0, il reste un problème initial d’équation différentielle.

f″=λf ; λ=f″(0), f(0)=1, f′(0)=0.

Si λ=−k²<0, la solution est cos(kx). Si λ=k²>0, elle est cosh(kx). Si λ=0, elle est 1. L’unicité du problème initial dans chacune de ces équations linéaires garantit qu’aucune autre fonction C² non nulle n’a été oubliée.

Reste la réciproque : les formules cos(u+v)+cos(u−v)=2cos u cos v et leur version hyperbolique vérifient l’équation fonctionnelle. Résoudre une conséquence différentielle sans cette dernière vérification serait incomplet.

Un autre chemin, proche du TP du recueil, utilise x=y : f(2x)=2f(x)²−1. Cette relation détermine des valeurs sur des subdivisions dyadiques, et les polynômes de Chebyshev organisent les multiples. La continuité permet ensuite un passage par densité. L’atelier privilégie la preuve C² pour faire le lien avec les problèmes initiaux, mais distingue explicitement l’hypothèse choisie.

## 39. Une substitution qui ferme un système

Sup · Laboratoire `identification_symetrie`

Chercher f définie sur ℝ privé de 0 telle que f(x)+f(−x)/x=x. Le terme f(−x) suggère une substitution très précise : écrire l’égalité au point −x. Aucun passage à la limite ni aucune dérivation n’est nécessaire.

A+B/x=x ; B−A/x=−x, avec A=f(x), B=f(−x).

Multiplier la première équation par x donne xA+B=x². Soustraire la seconde après réarrangement, ou remplacer B=A/x−x : A(1+x²)=x²(x+1). Le déterminant du système ne s’annule jamais sur le domaine.

f(x)=x²(x+1)/(1+x²), pour x≠0.

Cette formule prouve l’unicité d’un éventuel candidat. Pour l’existence, calculer f(−x)=x²(1−x)/(1+x²), puis f(x)+f(−x)/x=x. Le raisonnement donne donc exactement une solution sur ℝ privé de 0, sans supposer f continue.

Dans d’autres équations, les substitutions x↦1/x, x↦−x ou les échanges de variables créent de petits systèmes analogues. La bonne substitution réutilise les mêmes valeurs inconnues : elle ne multiplie pas indéfiniment les nouvelles inconnues.

## 40. Parties paire et impaire, prolongement et comportement à l’infini

Sup → Spé · Laboratoire `identification_symetrie`

Toute fonction sur un domaine stable par x↦−x se décompose en f=p+q, où p(x)=[f(x)+f(−x)]/2 est paire et q(x)=[f(x)−f(−x)]/2 est impaire. La solution du laboratoire donne des expressions simples.

p(x)=x²/(1+x²) ; q(x)=x³/(1+x²).

Près de 0, f(x)=x²+x³+O(x⁴). La limite en 0 vaut 0 : il existe un unique prolongement continu, obtenu en fixant f(0)=0. Mais l’équation initiale contient 1/x ; elle ne doit pas être présentée comme vérifiée en x=0.

À l’infini, une division polynomiale donne f(x)=x+1−(x+1)/(1+x²). L’asymptote est y=x+1. Sa partie paire tend vers 1, alors que sa partie impaire ressemble à x. Ces deux courbes rendent la décomposition visible et constituent des outils classiques d’étude de fonction.

Le laboratoire ajoute éventuellement b sin x au candidat. L’ajout conserve une allure proche, mais la vérification dans l’égalité initiale révèle un défaut. Au voisinage de 0, ce défaut tend vers −b : la division par x amplifie ici une perturbation qui s’annule elle-même en 0.

## 41. Gamma : convergence, intégration par parties et factorielle

Sup → Spé · Laboratoire `gamma_euler`

Une fonction définie par une intégrale impropre demande d’abord un domaine. Pour x réel, considérons Γ(x)=∫₀∞t^(x−1)e^(−t)dt. Au voisinage de 0, e^(−t) tend vers 1 : le critère des puissances donne la convergence si et seulement si x>0. À l’infini, t^(x−1)e^(−t) est intégrable, car l’exponentielle décroissante domine toute puissance. Ainsi **le domaine de cette définition réelle est ]0,+∞[**.

Effectuer une intégration par parties sur [ε,T], avec u=tˣ et dv=e^(−t)dt. Le terme de bord tˣe^(−t) tend vers 0 aux deux extrémités lorsque x>0. On obtient une relation fonctionnelle :

Γ(x+1)=xΓ(x) ; Γ(1)=1 ; Γ(n)=(n−1)! pour n≥1.

Une singularité du noyau en 0 n’empêche pas son intégrabilité : pour x=1/2, le noyau se comporte comme 1/√t. Avec t=u², Γ(1/2)=2∫₀∞e^(−u²)du=√π. Les demi-entiers suivent alors la récurrence : Γ(3/2)=√π/2, Γ(5/2)=3√π/4.

Le curseur de troncature T fournit ∫₀ᵀ, pas Γ tout entière. Distinguer **erreur de troncature**, liée à la queue, et **erreur de quadrature**, liée à l’approximation numérique de l’intégrale finie. Lorsque x augmente, le maximum du noyau est en t=x−1 et une troncature courte peut manquer une grande partie de l’aire.

## 42. Dériver une intégrale à paramètre et comprendre la convexité

Spé · Prolongement · Laboratoire `gamma_euler`

Fixons un compact [a,b] contenu dans ]0,+∞[. La dérivée en x du noyau vaut (ln t)t^(x−1)e^(−t). Pour t≤1, sa valeur absolue est majorée par |ln t|t^(a−1), intégrable ; pour t≥1, par (ln t)t^(b−1)e^(−t), également intégrable. Le théorème de dérivation sous le signe intégral donne, et le raisonnement se répète pour tout entier p :

Γ^(p)(x)=∫₀∞(ln t)^p t^(x−1)e^(−t)dt.

En particulier Γ″(x)>0, car le noyau est positif presque partout : Γ est strictement convexe. Une propriété plus forte est la convexité de ln Γ. Avec la densité wₓ(t)=t^(x−1)e^(−t)/Γ(x), le quotient Γ′/Γ est la moyenne de ln t et la dérivée seconde de ln Γ est sa variance.

(ln Γ)″(x)=Γ″(x)/Γ(x)−[Γ′(x)/Γ(x)]²=Varₓ(ln t)>0.

La **fonction digamma** ψ=Γ′/Γ se rencontre dans la dérivation de B(a,b). La relation Γ(x+1)=xΓ(x) donne ψ(x+1)=ψ(x)+1/x. Le théorème de Bohr–Mollerup caractérise Γ par Γ(1)=1, la récurrence et la convexité de ln Γ sur ]0,+∞[ ; ce théorème est un prolongement, pas une exigence de cours en sup. Les définitions sont précisées dans [NIST DLMF, §5.2](https://dlmf.nist.gov/5.2).

## 43. Bêta, jacobien et factorisation d’une intégrale double

Spé · Laboratoire `beta_geometrie`

Pour a,b>0, B(a,b)=∫₀¹t^(a−1)(1−t)^(b−1)dt est convergente. Au voisinage de 0, le critère porte sur a−1 ; près de 1, poser v=1−t et utiliser b−1. Le changement t↦1−t démontre immédiatement la symétrie B(a,b)=B(b,a).

Pour comprendre le lien avec gamma, écrire le produit Γ(a)Γ(b) comme une intégrale positive sur le quadrant u>0,v>0. Introduire **r=u+v**, qui mesure la somme, et **t=u/(u+v)**, qui mesure une proportion. L’inverse est u=rt et v=r(1−t), avec r>0 et 0<t<1. La matrice des dérivées a pour déterminant −r : la valeur absolue du jacobien est r.

e^(−u−v)u^(a−1)v^(b−1)du dv = e^(−r)r^(a+b−1)dr · t^(a−1)(1−t)^(b−1)dt.

Les deux variables se séparent. On obtient **Γ(a)Γ(b)=Γ(a+b)B(a,b)**. La positivité permet les interversions nécessaires ; le changement de variables dans une intégrale double est présenté ici comme un prolongement guidé. Le facteur r explique pourquoi l’exposant radial est a+b−1 et non a+b−2.

On peut ensuite éviter les intégrales doubles dans bien des calculs : B(a,b+1)=bB(a,b)/(a+b), B(a+1,b)=aB(a,b)/(a+b). Ces deux identités découlent de Γ(x+1)=xΓ(x), mais aussi de 1=t+(1−t) et d’une intégration par parties. Voir les identités dans [NIST DLMF, §5.12](https://dlmf.nist.gov/5.12).

## 44. Moments, densité et intégrales trigonométriques

Sup → Spé · Laboratoire `beta_geometrie`

La fonction w(t)=t^(a−1)(1−t)^(b−1)/B(a,b) est positive et son intégrale sur [0,1] vaut 1. Elle constitue une densité de probabilité. Une intégrale de tʳw(t) se ramène au même objet avec a augmenté :

E(tʳ)=B(a+r,b)/B(a,b), lorsque a+r>0 ; E(t)=a/(a+b).

Calculer E(t²)=a(a+1)/[(a+b)(a+b+1)], puis retrancher E(t)² pour obtenir Var(t)=ab/[(a+b)²(a+b+1)]. À a=b, la symétrie par rapport à 1/2 donne la moyenne sans aucun calcul. Si a et b sont grands à proportion fixée, la variance diminue : le graphique devient plus concentré.

Le changement t=sin²θ, θ∈[0,π/2], transforme les puissances de sinus et de cosinus en une intégrale bêta. Écrire dt=2sinθcosθdθ est le point décisif.

∫₀^(π/2)sinᵖθcosᑫθdθ = ½B((p+1)/2,(q+1)/2), pour p,q>−1.

Cette formule retrouve les intégrales de Wallis et dépasse le cas des exposants entiers. Elle fournit aussi une technique pour vérifier les dimensions d’un changement de variables : les deux facteurs supplémentaires sinθ et cosθ viennent du différentiel et modifient les exposants.

## 45. Séries de Riemann et encadrement d’un reste

Sup → Spé · Laboratoire `zeta_series`

Pour s réel supérieur à 1, ζ(s)=Σ_(n≥1)n^(−s). La convergence est celle d’une série de Riemann. Fixons N≥1 et notons S_N la somme jusqu’à N, R_N=ζ(s)−S_N. Puisque t↦t^(−s) est décroissante, les rectangles de largeur 1 entourent l’aire située sous sa courbe.

∫_(N+1)^∞t^(−s)dt ≤ R_N ≤ ∫_N^∞t^(−s)dt ; donc (N+1)^(1−s)/(s−1) ≤ R_N ≤ N^(1−s)/(s−1).

Ajouter ces deux bornes à S_N donne un intervalle contenant ζ(s), même si S_N est encore une mauvaise approximation. La largeur de cet intervalle est [N^(1−s)−(N+1)^(1−s)]/(s−1), de l’ordre de N^(−s) ; le reste lui-même est de l’ordre de N^(1−s)/(s−1). **Une correction intégrale peut donc resserrer fortement l’information** sans additionner beaucoup plus de termes.

Pour s=2, le reste est voisin de 1/N ; pour s=1,1, il est voisin de 10N^(−0,1). Le fait que les derniers termes soient petits ne suffit pas à contrôler leur somme infinie. Une somme partielle et une justification du reste répondent à deux questions différentes.

Les valeurs emblématiques sont ζ(2)=π²/6 et ζ(4)=π⁴/90. Le laboratoire utilise une référence par Euler–Maclaurin ; le raisonnement par rectangles constitue le contrôle indépendant auquel se fier pour un encadrement.

## 46. Continuité et dérivation : choisir un domaine uniforme

Spé · Laboratoire `zeta_series`

Chaque fonction s↦n^(−s) est continue. Pour transmettre la continuité à une somme infinie, il faut un mode de convergence suffisant. Sur s≥1+δ, avec δ>0 fixé, on a |n^(−s)|≤n^(−1−δ). La série majorante converge : la série définissant ζ est **normalement convergente** sur ce domaine, et donc uniformément convergente.

Pour dériver, la dérivée d’ordre p est (−ln n)^p n^(−s). Pour tout p et δ>0, (ln n)^p≤C n^(δ/2) à partir d’un certain rang. Les dérivées sont alors majorées par Cn^(−1−δ/2), sommable. Le théorème de dérivation des séries de fonctions s’applique sur tout compact de ]1,+∞[.

ζ^(p)(s)=(−1)^pΣ_(n≥2)(ln n)^p/n^s ; ζ′(s)<0 ; ζ″(s)>0.

La fonction ζ est donc strictement décroissante et strictement convexe sur ]1,+∞[. En revanche la convergence n’est pas uniforme sur tout ]1,+∞[ : pour N fixé, la borne du reste devient arbitrairement grande lorsque s approche 1, et le reste diverge lui aussi. Le bon réflexe en CPGE est de travailler d’abord sur **un segment à distance positive du bord du domaine**.

La représentation réelle et les autres représentations sont documentées dans [NIST DLMF, chapitre 25](https://dlmf.nist.gov/25.5). Le prolongement complexe et l’hypothèse de Riemann appartiennent à un autre sujet ; les expériences présentes restent sur s>1.

## 47. Une série géométrique sous une intégrale impropre

Spé · Laboratoire `zeta_integrale`

Le noyau 1/(eᵗ−1) semble différent de la série ζ. Pour t>0, écrire e^(−t)/(1−e^(−t))=Σ_(n≥1)e^(−nt). Multiplier par t^(s−1), puis intégrer sur ]0,+∞[. Comme les termes sont positifs, le théorème de convergence monotone permet de passer de la suite des sommes finies à la somme intégrée, même avant de connaître sa finitude.

∫₀∞ t^(s−1)/(eᵗ−1)dt = Σ_(n≥1)∫₀∞t^(s−1)e^(−nt)dt = Γ(s)Σ_(n≥1)n^(−s).

Dans chaque terme, u=nt donne le facteur n^(−s). Pour s>1, la série de Riemann est finie et l’identité donne Γ(s)ζ(s). On retrouve directement la même condition en étudiant le noyau : eᵗ−1∼t en 0, donc t^(s−1)/(eᵗ−1)∼t^(s−2), intégrable si et seulement si s>1. À l’infini, le noyau est équivalent à t^(s−1)e^(−t).

Cette preuve illustre trois étapes distinctes : établir une représentation ponctuelle, **justifier une interversion**, puis effectuer un changement de variable dans chaque terme. La condition « tous les termes sont positifs » n’est pas une hypothèse accessoire : elle évite de devoir prouver auparavant la convergence dominée d’une somme infinie.

La représentation est donnée dans [NIST DLMF, §25.5](https://dlmf.nist.gov/25.5). Numériquement, une substitution t=v^q retire la singularité du voisinage de 0 ; additionner une grille uniforme qui commence trop loin de 0 manquerait une partie importante de l’intégrale.

## 48. Application physique : une loi en température obtenue par changement d’échelle

Spé · Prolongement · Laboratoire `zeta_integrale`

Des distributions thermiques conduisent à des intégrales de la forme I_p(T_phys)=∫₀∞ωᵖ/[exp(ℏω/(kT_phys))−1]dω, avec T_phys>0, k la constante de Boltzmann et ℏ la constante de Planck réduite. Il suffit souvent d’identifier l’échelle de la variable, sans évaluer immédiatement l’intégrale.

t=ℏω/(kT_phys) ; I_p(T_phys)=(kT_phys/ℏ)^(p+1)Γ(p+1)ζ(p+1), pour p>0.

La condition p>0 vient de la convergence en 0. Pour p=3, Γ(4)=6 et ζ(4)=π⁴/90 donnent π⁴/15. La dépendance de l’intégrale est donc **T_phys⁴**. Les facteurs de volume, de polarisation et de vitesse de la lumière dépendent de la quantité physique étudiée ; le laboratoire montre l’intégrale commune, sans les confondre avec elle.

Pour p=2, la constante est 2ζ(3) et la puissance de température est 3. Changer la dimension ou le nombre de puissances de la fréquence dans un comptage de modes modifie la loi d’échelle. Cette démarche fait le lien entre analyse, changement de variables, dimension physique et physique statistique.

Le curseur T de l’expérience désigne la **borne de troncature numérique**, sans dimension. Il ne faut pas la confondre avec T_phys. Quand la fréquence est remplacée par une pulsation ou inversement, les facteurs 2π se transforment également : annoncer la variable choisie avant de comparer des constantes physiques.

## 49. De Cauchy à une intégration d’ordre réel

Spé · Prolongement · Laboratoire `integrale_fractionnaire`

Notons Jf(t)=∫₀ᵗf(u)du, primitive choisie nulle à l’origine. Pour n≥1, les intégrations répétées ont une forme unique, obtenue en échangeant l’ordre de deux intégrales sur un triangle :

Jⁿf(t)=1/(n−1)! ∫₀ᵗ(t−u)^(n−1)f(u)du.

Le noyau est une puissance et la constante une valeur de gamma. Pour α réel strictement positif, on définit l’intégrale de Riemann–Liouville par J^αf(t)=1/Γ(α)∫₀ᵗ(t−u)^(α−1)f(u)du. Si 0<α<1, le noyau est singulier en u=t mais localement intégrable. Pour une fonction continue sur [0,t], l’intégrale est donc bien définie.

Appliquer cette définition à f(u)=u^q, q>−1. Avec u=tv, les facteurs donnent t^(q+α), et l’intégrale restante est B(q+1,α). L’identité bêta-gamma simplifie le coefficient :

J^α(t^q)=Γ(q+1)t^(q+α)/Γ(q+α+1).

À α=1, on retrouve t^(q+1)/(q+1). À α=1/2, J^(1/2)(1)=2√t/√π. Une « demi-intégration » n’est donc pas une primitive ordinaire multipliée par une constante : elle modifie aussi la puissance. Les ordres sont ici réels positifs et la borne initiale est fixée à 0 ; annoncer ces choix fait partie de la définition.

## 50. Loi de composition et réponse à une impulsion

Spé · Prolongement · Laboratoire `integrale_fractionnaire`

Pour une fonction continue sur chaque intervalle fini et α,β>0, on peut démontrer J^αJ^β=J^(α+β). Le même calcul vaut pour les profils bornés par morceaux de l’expérience. Écrire les deux intégrales sur 0≤v≤u≤t et échanger u et v. À v fixé, l’intégrale intérieure vaut ∫ᵥᵗ(t−u)^(α−1)(u−v)^(β−1)du. Le changement u=v+(t−v)r fournit (t−v)^(α+β−1)B(α,β). Les facteurs gamma donnent le noyau attendu.

J^α[J^βf]=J^(α+β)f ; en particulier J^(1/2)J^(1/2)f=Jf.

Une impulsion rectangulaire vaut 1 sur [0,a] et 0 après a. Pour t≤a, le résultat est t^α/Γ(α+1). Pour t>a, le passé utile s’arrête à a, mais son poids dépend encore de t :

J^αf(t)=[t^α−(t−a)_+^α]/Γ(α+1), où (v)_+=max(v,0).

Après la fin du signal, une réponse subsiste. Quand t devient grand, t^α−(t−a)^α∼αa t^(α−1). Ainsi la réponse décroît pour α<1, reste constante pour α=1 et croît pour α>1. Ces comportements rendent la **mémoire non locale** visible. Ils se déduisent d’un développement limité en a/t, pas seulement du graphique.

Cette construction est une introduction au calcul fractionnaire, au-delà des exigences usuelles. La loi de composition des intégrales ne justifie pas automatiquement une loi analogue pour toutes les dérivées fractionnaires : les conditions initiales peuvent y intervenir. Une formulation par convolution est développée par [Li et Liu, étude des dérivées de Caputo](https://arxiv.org/abs/1612.05103).

## 51. Deux définitions et le rôle de la valeur initiale

Spé · Prolongement · Laboratoire `derivees_fractionnaires`

Limiter d’abord l’étude à 0<α<1 permet de distinguer deux ordres d’opérations. La dérivée de Riemann–Liouville est D_RL^αf=(J^(1−α)f)′ : on intègre puis on dérive. La dérivée de Caputo est D_C^αf=J^(1−α)f′ : on dérive puis on intègre. Pour une fonction absolument continue, ces opérations n’ont pas en général le même résultat.

D_C^αf(t)=1/Γ(1−α)∫₀ᵗ(t−u)^(−α)f′(u)du.

Écrire f(u)=f(0)+∫₀ᵘf′(v)dv. Appliquer J^(1−α), puis dériver. Le terme constant produit f(0)t^(−α)/Γ(1−α), et le terme contenant la primitive se simplifie grâce à la loi de composition. Ainsi :

D_RL^αf(t)=D_C^αf(t)+f(0)t^(−α)/Γ(1−α), pour t>0.

Pour f=1, Caputo donne 0 et Riemann–Liouville donne t^(−α)/Γ(1−α). Pour f=t^q, q≥1 entier, f(0)=0 et les deux définitions donnent Γ(q+1)t^(q−α)/Γ(q+1−α). Pour f=c+t^q, la constante sépare les deux courbes. À q=0, f est la constante c+1 ; cette situation doit être traitée séparément pour Caputo.

Dans une équation différentielle fractionnaire, annoncer l’opérateur et la borne initiale est indispensable. La dérivée ordinaire d’un ordre entier est un cas distinct ; les expressions comprenant Γ(1−α) ne s’emploient pas naïvement en posant α=1.

## 52. Une même valeur et une même pente ne déterminent pas une dérivée non locale

Spé · Prolongement · Laboratoire `derivees_fractionnaires`

Considérons sur [0,1] f₁(t)=t et f₂(t)=t+A t(1−t)². À t=1, les deux fonctions ont la valeur 1 et la dérivée ordinaire 1. Les termes ajoutés s’annulent avec leur dérivée à cet instant. Leur passé diffère dès que A≠0.

La linéarité et les dérivées fractionnaires des puissances donnent :

D_C^α(f₂−f₁)(t)=A[t^(1−α)/Γ(2−α)−4t^(2−α)/Γ(3−α)+6t^(3−α)/Γ(4−α)].

En t=1, utiliser Γ(3−α)=(2−α)Γ(2−α) et Γ(4−α)=(3−α)(2−α)Γ(2−α). Le coefficient devient −Aα(1−α)/[(2−α)(3−α)Γ(2−α)], non nul pour A≠0 et 0<α<1. Une dérivée de Caputo dépend de f′ sur **tout [0,t]**, pondérée par (t−u)^(−α), et non du seul voisinage infinitésimal de t.

Pour α=1/2, cette différence est −2A/(15√π). L’expérience compare à la fois les fonctions et leurs dérivées de Caputo ; elle évite de confondre différence de pente et différence de mémoire. Au niveau CPGE, les outils sont la linéarité, les polynômes, la récurrence gamma et le calcul d’intégrales. Le choix d’un modèle physique de mémoire relève d’un prolongement.

La question des valeurs initiales et des opérateurs est étudiée dans [Li et Liu, définition généralisée des dérivées de Caputo](https://arxiv.org/abs/1612.05103). Le laboratoire reste volontairement dans le cadre classique des fonctions polynomiales régulières.

## 53. Classer les termes de la dérivée d’une composition

Spé · Prolongement · Laboratoire `faa_di_bruno`

Les premières dérivées de h=f∘g sont h′=f′(g)g′ et h″=f″(g)(g′)²+f′(g)g″. À l’ordre 3, h‴=f‴(g)(g′)³+3f″(g)g′g″+f′(g)g‴. Le coefficient 3 ne vient pas d’une approximation : il compte les trois façons d’obtenir le même produit.

À l’ordre n, notons mⱼ le nombre de facteurs g^(j). Chaque facteur correspond à j dérivations, donc Σⱼjmⱼ=n. Si k=Σⱼmⱼ, la dérivée de f est d’ordre k. La formule de Faà di Bruno est :

(f∘g)^(n)=Σ_[Σⱼjmⱼ=n] n! f^(k)(g) ∏ⱼ[(g^(j)/j!)^mⱼ/mⱼ!], avec k=Σⱼmⱼ.

Le facteur n! compte des affectations ordonnées ; les j! retirent les permutations internes et les mⱼ! retirent l’ordre entre blocs de même taille. Cette lecture combinatoire aide à retenir la formule sans oublier une factorielle. Les **polynômes de Bell partiels** B_(n,k) rassemblent les termes qui ont le même k.

B_(0,0)=1 ; B_(n,k)=Σ_(j=1)^(n−k+1) C(n−1,j−1)xⱼB_(n−j,k−1).

Ici g=1+ax+bx² : g^(j)=0 pour j≥3. On ne conserve donc que m₁+2m₂=n. Il reste ⌊n/2⌋+1 contributions structurelles, bien moins que dans le cas général. Le tableau indique m₁,m₂,k, le coefficient n!/[m₁!m₂!2^m₂] et la contribution au point x₀. Un terme peut être nul au point choisi sans disparaître de la formule.

## 54. Dériver une inverse et une logarithmique : deux méthodes complémentaires

Spé · Laboratoire `faa_di_bruno`

Si g ne s’annule pas, prendre f(z)=1/z dans Faà di Bruno. Comme f^(k)(z)=(−1)^k k!/z^(k+1), on obtient les dérivées de h=1/g. Une méthode souvent plus rapide dans un exercice consiste à partir de gh=1 et appliquer la formule de Leibniz.

h^(n)=−1/g · Σ_(j=1)^n C(n,j)g^(j)h^(n−j), pour n≥1.

Cette récurrence exige la valeur de h et de ses dérivées précédentes au même point. Pour une quadratique, seuls j=1 et j=2 subsistent. Elle se calcule sans symbolisme compliqué et fournit un contrôle indépendant de la formule de composition.

Pour f=ln, annoncer g>0 sur le domaine réel. On a f^(k)(z)=(−1)^(k−1)(k−1)!/zᵏ pour k≥1. L’exponentielle, elle, vérifie f^(k)=f à tous les ordres ; tous les coefficients combinatoires viennent donc des dérivées de g. L’exemple g=−x² conduit aux polynômes d’Hermite.

Dans l’expérience, g=1+ax+bx² est globalement positive car son minimum est 1−a²/(4b)≥0,375 avec les bornes des curseurs. Cela assure la définition de 1/g et ln(g), même lorsqu’on change de scénario. Aux ordres élevés, de grandes contributions peuvent se compenser : comparer **la somme signée** et les contributions est plus instructif que regarder seulement leur valeur absolue.

## 55. Rodrigues et Faà di Bruno : les polynômes d’Hermite

Spé · Laboratoire `hermite_gauss`

Chaque dérivée de e^(−x²) est cette gaussienne multipliée par un polynôme. Fixons la convention des physiciens :

Hₙ(x)=(−1)^n e^(x²)(dⁿ/dxⁿ)e^(−x²) ; H₀=1, H₁=2x, H₂=4x²−2.

Prendre f=exp et g=−x² dans Faà di Bruno : seuls g′=−2x et g″=−2 interviennent. La condition m₁+2m₂=n donne la formule finie :

Hₙ(x)=n!Σ_(j=0)^⌊n/2⌋(−1)^j(2x)^(n−2j)/[j!(n−2j)!].

On lit immédiatement le degré n, le coefficient dominant 2ⁿ et la parité Hₙ(−x)=(−1)^nHₙ(x). À l’origine, les degrés impairs donnent 0 et H_(2r)(0)=(−1)^r(2r)!/r!. Les récurrences Hₙ′=2nH_(n−1) et H_(n+1)=2xHₙ−2nH_(n−1) sont des outils efficaces pour calculer la famille et ses dérivées.

Elles permettent de vérifier l’équation différentielle Hₙ″−2xHₙ′+2nHₙ=0. Une famille de polynômes, une formule de dérivation et une équation différentielle se rejoignent dans un même objet. Le laboratoire ne remplace pas la dérivée par une approximation à partir d’une grille : il calcule les polynômes par récurrence.

Les conventions des familles orthogonales sont précisées dans [NIST DLMF, §18.3](https://dlmf.nist.gov/18.3). La convention dite probabiliste utilise un poids e^(−x²/2) pour les polynômes et une autre échelle ; ne pas mélanger les deux suites.

## 56. Orthogonalité, fonctions normalisées et oscillateur harmonique

Spé · Prolongement · Laboratoire `hermite_gauss`

Pour m<n, écrire Hₙe^(−x²)=(−1)^n(dⁿ/dxⁿ)e^(−x²). Dans ∫ℝHₘHₙe^(−x²)dx, effectuer n intégrations par parties. Les termes de bord s’annulent car une gaussienne domine chaque polynôme, et Hₘ^(n)=0. Le produit scalaire est donc nul. Pour m=n, Hₙ^(n)=2ⁿn!, ce qui donne la norme.

∫ℝHₙHₘe^(−x²)dx = √π 2ⁿn! δ_(n,m).

Définir ψₙ(x)=Hₙ(x)e^(−x²/2)/[π^(1/4)√(2ⁿn!)]. Les fonctions ψₙ ont une norme 1 et sont deux à deux orthogonales pour l’intégrale ordinaire sur ℝ. **Le poids est désormais inclus dans chaque fonction** : le produit de deux enveloppes e^(−x²/2) redonne e^(−x²).

En dérivant ψₙ puis en utilisant l’équation de Hₙ, on obtient −ψₙ″+x²ψₙ=(2n+1)ψₙ. C’est la forme sans dimension de l’équation stationnaire de l’oscillateur harmonique quantique. L’analyse classique explique le calcul et la normalisation ; l’interprétation des niveaux d’énergie est un prolongement vers la physique quantique.

L’orthogonalité ne résulte pas seulement d’une différence de parité. Si n et m sont de parités opposées, l’intégrande est impaire et son intégrale nulle par symétrie ; s’ils sont de même parité et différents, les intégrations par parties fournissent la preuve. Le laboratoire propose ces deux cas pour distinguer les arguments.
