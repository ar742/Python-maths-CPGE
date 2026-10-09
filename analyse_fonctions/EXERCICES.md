# Fonctions & Équations — 84 exercices corrigés

## 01. Changer l’échelle de la gaussienne

Spé · Laboratoire `continuite_gauss`

Pour c>0, calculer ∫ℝe⁻ᶜᵗ²cos(at)dt à partir de la formule du laboratoire. Justifier sa continuité en a.

**Correction guidée**

Poser u=√c t. On obtient **√(π/c)exp[−a²/(4c)]**. À c fixé, |e⁻ᶜᵗ²cos(at)|≤e⁻ᶜᵗ², fonction intégrable indépendante de a ; le théorème de continuité s’applique sur ℝ.

## 02. Majorer les deux queues

Sup → Spé · Laboratoire `continuite_gauss`

Montrer ∫L∞e⁻ᵗ²dt≤e⁻ᴸ²/(2L) pour L>0, puis donner une erreur de troncature valable pour tous les a.

**Correction guidée**

Pour t≥L, 1≤t/L. Donc ∫L∞e⁻ᵗ²dt≤(1/L)∫L∞te⁻ᵗ²dt=**e⁻ᴸ²/(2L)**. Comme |cos(at)|≤1 et les deux côtés de ℝ sont symétriques, l’erreur absolue de troncature est au plus **e⁻ᴸ²/L**.

## 03. Calculer une intégrale grâce à une EDO

Spé · Laboratoire `continuite_gauss`

Retrouver F′=−aF/2 en précisant le majorant qui autorise la dérivation et le terme de bord.

**Correction guidée**

|∂f/∂a|≤|t|e⁻ᵗ², intégrable, donc F′=−∫te⁻ᵗ²sin(at). Utiliser te⁻ᵗ²=−(e⁻ᵗ²)′/2 ; e⁻ᵗ²sin(at)→0 aux deux infinis. L’intégration par parties donne **F′=−aF/2**. Avec F(0)=√π, résoudre le problème initial.

## 04. Combien de masse près de 0 ?

Sup → Spé · Laboratoire `continuite_defaut`

Calculer ∫₀ᵋfₐ(t)dt et choisir ε en fonction de a pour capturer 99 % de la masse.

**Correction guidée**

L’intégrale vaut **1−e⁻ᵋ/ᵃ**. Capturer 99 % impose e⁻ᵋ/ᵃ≤0,01, donc **ε≥a ln 100≈4,605a**. La fenêtre doit rester proportionnelle à la largeur de concentration.

## 05. Calculer la borne supérieure des densités

Spé · Laboratoire `continuite_defaut`

Pour t>0 fixé, maximiser e⁻ᵗ/ᵃ/a sur 0<a≤1. Que prouve le résultat concernant un majorant intégrable commun ?

**Correction guidée**

La dérivée logarithmique est (t−a)/a². Pour t≤1, le maximum est en a=t et vaut **1/(et)**. Pour t>1, le maximum est en a=1 et vaut e⁻ᵗ. La divergence de ∫₀¹dt/t interdit tout majorant intégrable commun.

## 06. Comparer deux modes de convergence

Spé · Laboratoire `continuite_defaut`

Prouver fₐ(t)→0 ponctuellement, mais que fₐ ne tend pas vers 0 en norme L¹. Quelle égalité illégitime serait produite par un passage automatique sous l’intégrale ?

**Correction guidée**

Pour t>0, poser u=t/a : fₐ(t)=ue⁻ᵘ/t→0. Au point 0, la valeur est fixée à 0. Pourtant ∫|fₐ|=1. Le passage illégitime donnerait **lim∫fₐ=∫lim fₐ=0**, alors que le membre de gauche vaut 1.

## 07. Un logarithme sans primitive

Spé · Laboratoire `leibniz_frullani`

Calculer ∫₀∞(e⁻²ᵗ−e⁻⁵ᵗ)/t dt. Peut-on intégrer séparément les deux termes ?

**Correction guidée**

La formule donne **ln(5/2)**. Les deux intégrales séparées divergent en 0 ; leur différence est intégrable parce que le numérateur vaut 3t+O(t²). La séparation serait donc illégitime.

## 08. Dériver par rapport aux deux paramètres

Spé · Laboratoire `leibniz_frullani`

À partir de la méthode et de la formule, donner ∂F/∂a et ∂F/∂b. Retrouver a∂F/∂a+b∂F/∂b=0.

**Correction guidée**

Les dérivées sont **−1/a et 1/b**, obtenues en intégrant −e⁻ᵃᵗ et e⁻ᵇᵗ avec une domination locale. Ainsi a(−1/a)+b(1/b)=0. Cela correspond à l’invariance F(λa,λb)=F(a,b).

## 09. Déterminer une coupure suffisante

Sup → Spé · Laboratoire `leibniz_frullani`

Avec a=1,b=2, utiliser la borne simple des queues pour garantir une erreur de troncature au plus 10⁻⁶. Cette garantie couvre-t-elle l’erreur de quadrature ?

**Correction guidée**

La borne vaut e⁻ᴸ. Il suffit de prendre **L≥ln(10⁶)≈13,82**. Cette garantie concerne uniquement la partie omise après L ; il faut contrôler séparément l’erreur de la méthode d’intégration sur [0,L].

## 10. Ajouter une pulsation

Spé · Laboratoire `leibniz_arctan`

Pour a>0, calculer G(ω)=∫₀∞e⁻ᵃᵗsin(ωt)/t dt en dérivant par rapport à ω. Préciser le majorant.

**Correction guidée**

|∂f/∂ω|=e⁻ᵃᵗ|cos(ωt)|≤e⁻ᵃᵗ, intégrable et indépendant de ω. Donc G′(ω)=a/(a²+ω²). Avec G(0)=0, **G(ω)=arctan(ω/a)**.

## 11. La valeur de la constante

Spé · Laboratoire `leibniz_arctan`

Résoudre F′(a)=−1/(1+a²) avec la condition F(a)→0 à l’infini. Pourquoi la condition est-elle nécessaire ?

**Correction guidée**

F(a)=−arctan a+C. La limite impose C=π/2, donc **F(a)=arctan(1/a)** pour a>0. Sans la condition, une constante arbitraire reste possible et l’intégrale n’est pas identifiée.

## 12. Distinguer limite et passage sous l’intégrale

Spé · Laboratoire `leibniz_arctan`

La formule donne limₐ→₀⁺F(a)=π/2. Le majorant local utilisé pour Leibniz autorise-t-il directement ∫sin t/t=π/2 ?

**Correction guidée**

**Non.** Le majorant e⁻⁽ᵃ/²⁾ᵗ n’est pas commun à tous les a proches de 0. Pour identifier l’intégrale non amortie à cette limite, il faut justifier un passage à la limite, par exemple via un contrôle uniforme des queues oscillantes. La limite de la formule seule ne fournit pas cette justification.

## 13. Dériver la relation de récurrence

Spé · Laboratoire `derivees_gamma`

À partir de Γ(a+1)=aΓ(a), donner des relations pour Γ′ et Γ″. Les dérivations sont-elles justifiées ?

**Correction guidée**

Γ est C∞ sur ]0,+∞[ grâce aux majorants locaux. On obtient **Γ′(a+1)=Γ(a)+aΓ′(a)**, puis **Γ″(a+1)=2Γ′(a)+aΓ″(a)**. Ces relations contrôlent les moments logarithmiques d’un intervalle de paramètres au suivant.

## 14. Log-convexité avec Cauchy–Schwarz

Spé · Laboratoire `derivees_gamma`

Prouver Γ′(a)²≤Γ(a)Γ″(a), et expliquer pourquoi l’inégalité est stricte.

**Correction guidée**

Appliquer Cauchy–Schwarz aux fonctions u(t)=t⁽ᵃ⁻¹⁾/²e⁻ᵗ/² et v(t)=u(t)ln t. Les carrés de leurs normes valent Γ(a) et Γ″(a), et leur produit scalaire vaut Γ′(a). L’égalité exigerait ln t constante presque partout pour un poids strictement positif, ce qui est impossible. Donc **Γ′²<ΓΓ″**.

## 15. Un seul majorant pour plusieurs ordres

Spé · Laboratoire `derivees_gamma`

Pour a∈[1/2,3] et k=0,1,2,3, proposer un majorant intégrable commun de tᵃ⁻¹|ln t|ᵏe⁻ᵗ.

**Correction guidée**

Pour t≤1, prendre **t⁻¹/²(1+|ln t|³)e⁻ᵗ**. Pour t≥1, prendre **t²(1+(ln t)³)e⁻ᵗ**. Le changement s=−ln t prouve l’intégrabilité du premier morceau ; la décroissance exponentielle prouve celle du second. La domination est indépendante de a et de k dans les ensembles indiqués.

## 16. Une intégrale de moment

Sup → Spé · Laboratoire `derivees_laplace`

Calculer ∫₀∞t⁷e⁻²ᵗdt de deux façons : changement de variable et dérivation d’une intégrale à paramètre.

**Correction guidée**

Avec u=2t, l’intégrale vaut Γ(8)/2⁸=**7!/256=19,6875**. En dérivant sept fois F(a)=1/a, F⁽⁷⁾(a)=−7!/a⁸ ; l’intégrale positive est −F⁽⁷⁾(2). La dérivation nécessite le majorant local explicité dans le cours.

## 17. Connaître la masse perdue

Spé · Laboratoire `derivees_laplace`

Pour n=1 et a=1, calculer exactement la queue après L. Trouver la fraction capturée pour L=4.

**Correction guidée**

Une intégration par parties donne **R₁(L)=e⁻ᴸ(L+1)**. La masse totale vaut 1 ; la fraction capturée pour L=4 est **1−5e⁻⁴≈0,9084**. Le maximum est pourtant en t=1, bien à l’intérieur de la fenêtre.

## 18. Transmettre un signe aux dérivées

Spé · Prolongement · Laboratoire `derivees_laplace`

Soit w≥0 et H(a)=∫₀∞e⁻ᵃᵗw(t)dt. Sous les hypothèses permettant la dérivation à chaque ordre, montrer H complètement monotone. Que devient l’affirmation si w change de signe ?

**Correction guidée**

Le théorème donne (−1)ⁿH⁽ⁿ⁾(a)=∫₀∞tⁿe⁻ᵃᵗw(t)dt≥0. Donc **H est complètement monotone**. Si w change de signe, les dérivées peuvent encore être définies, mais l’argument de positivité ne s’applique plus ; la monotonie complète n’est pas assurée.

## 19. TP : résoudre sans perdre la solution constante

Sup · Laboratoire `euler_rk4`

Résoudre y′=cos(x)(y+1), y(0)=y₀. Pourquoi diviser par y+1 demande-t-il une précaution ?

**Correction guidée**

Poser z=y+1 et dériver ze^(−sin x) : la dérivée est nulle. Ainsi z=(y₀+1)e^(sin x) et y=(y₀+1)e^(sin x)−1. Pour y₀=−1, z=0 et y≡−1 ; une division par z aurait exclu cette solution. Toutes les formules sont globales et vérifient la condition initiale.

## 20. Maxima, minima et périodicité du TP

Sup · Laboratoire `euler_rk4`

Pour y(0)=0, déterminer la période, les extrema et leurs abscisses. Que change y₀<−1 ?

**Correction guidée**

y=e^(sin x)−1 est 2π-périodique. Sa dérivée e^(sin x)cos x a le signe de cos x. Les maxima e−1 sont en π/2+2kπ ; les minima e^(−1)−1 sont en 3π/2+2kπ. Si y₀<−1, le facteur y₀+1 est négatif et les types des extrema s’inversent. Si y₀=−1, la fonction est constante.

## 21. Choisir un maillage par un ordre mesuré

Spé · Laboratoire `euler_rk4`

Une méthode donne E(h)=3,2×10⁻⁴ et E(h/2)=2,0×10⁻⁵. Estimer son ordre et le pas requis pour E≤10⁻⁶, en supposant le régime asymptotique atteint.

**Correction guidée**

Le rapport vaut 16, donc p≈log₂16=4. Après une nouvelle division par 2, E(h/4)≈1,25×10⁻⁶ ; ce n’est pas encore suffisant. Après deux divisions, E(h/8)≈7,81×10⁻⁸. Une estimation continue donnerait h_(nouveau)≈(h/2)(10⁻⁶/2×10⁻⁵)¹ᐟ⁴≈0,473(h/2). Il faut vérifier ce choix par un raffinement supplémentaire, car l’ordre est observé et non garanti par ces seules données.

## 22. Le facteur intégrant à coefficient variable

Sup · Laboratoire `facteur_integrant`

Résoudre y′+(a+bx)y=Fcos(ωx), y(0)=y₀, sous forme d’intégrale définie. Vérifier le signe de la primitive.

**Correction guidée**

A(x)=ax+bx²/2 satisfait A′=a+bx. Alors (eᴬy)′=eᴬFcos(ωx). Intégrer entre 0 et x donne y=e^(−A(x))[y₀+F∫₀ˣe^(A(s))cos(ωs)ds]. En dérivant, le premier terme produit −A′y et la borne variable fournit Fcos(ωx) ; on retrouve bien y′+(a+bx)y=Fcos(ωx).

## 23. Deux préparations, un même forçage

Sup → Spé · Laboratoire `facteur_integrant`

Deux solutions ont les données y₀ et y₀+1. Calculer leur différence et expliquer pourquoi sa décroissance ne force pas la décroissance de chacune.

**Correction guidée**

Leur différence d satisfait d′+(a+bx)d=0, d(0)=1. Donc d=e^(−ax−bx²/2). Pour a,b≥0 et x≥0, d est décroissante. Chaque solution possède toutefois une contribution forcée oscillante ; elle peut croître sur certains intervalles. La stabilité de la différence est une propriété distincte du sens de variation d’une trajectoire.

## 24. Circuit RC : retrouver la convolution

Sup → Spé · Laboratoire `facteur_integrant`

Un condensateur vérifie RC u′+u=V(t), avec u(0)=u₀. Donner sa solution et interpréter le noyau pour un échelon V(t)=V₀.

**Correction guidée**

Après division, a=1/(RC) et c=V/(RC). Ainsi u(t)=u₀e^(−t/(RC))+(1/(RC))∫₀ᵗe^(−(t−s)/(RC))V(s)ds. Pour V constant, u=V₀+(u₀−V₀)e^(−t/(RC)). Le noyau pondère les contributions passées et la constante RC fixe le temps de relaxation. R,C doivent être strictement positifs et constants.

## 25. Construire trois solutions avec la même donnée

Spé → Au-delà · Laboratoire `cauchy_lipschitz`

Vérifier que yτ(t)=max(t−τ,0)², τ≥0, résout y′=2√max(y,0), y(0)=0. Examiner la dérivabilité à τ.

**Correction guidée**

Pour t<τ, y=0 et y′=0 ; pour t>τ, y=(t−τ)² et y′=2(t−τ)=2√y. À τ, les quotients différentiels tendent vers 0 des deux côtés. y est donc C¹, et les deux membres valent 0 à τ. Toutes les valeurs τ≥0 donnent la même donnée initiale et des solutions différentes : l’unicité échoue.

## 26. Localement lipschitzien ou seulement continu ?

Spé → Au-delà · Laboratoire `cauchy_lipschitz`

Comparer f(y)=λy et g(y)=2√max(y,0) au voisinage de 0. Que peut-on conclure si une hypothèse suffisante d’un théorème échoue ?

**Correction guidée**

|f(y)−f(z)|≤|λ||y−z| : f est lipschitzienne. Pour ε>0, |g(ε)−g(0)|/ε=2/√ε n’est pas borné au voisinage de 0 ; g n’est pas localement lipschitzienne en 0. L’échec de cette hypothèse ne suffit pas en général à réfuter l’unicité. Ici la famille explicite yτ fournit en plus le contre-exemple nécessaire.

## 27. Unicité et instabilité ne se contredisent pas

Sup → Spé · Laboratoire `cauchy_lipschitz`

Pour y′=2y, comparer les données 0 et 10⁻⁶. Donner le temps où la différence atteint 10⁻². Pourquoi chaque solution reste-t-elle unique ?

**Correction guidée**

Les solutions sont 0 et 10⁻⁶e²ᵗ. L’écart atteint 10⁻² lorsque e²ᵗ=10⁴, soit t=2ln10≈4,605. Les deux données sont différentes ; l’unicité ne demande pas que leurs solutions restent proches. Pour une donnée fixée, la différence de deux prétendues solutions serait Ce²ᵗ avec C=0, donc elles coïncideraient.

## 28. Déterminer un intervalle maximal

Spé → Au-delà · Laboratoire `explosion_logistique`

Résoudre y′=ay², a>0, y(0)=y₀>0, et donner le domaine maximal contenant 0. Peut-on prolonger la solution avec la même expression après le pôle ?

**Correction guidée**

La solution est y=y₀/(1−ay₀t). Son pôle t*=1/(ay₀) donne le domaine ]−∞,t*[ contenant 0. Comme y→+∞ à gauche de t*, aucun prolongement réel continu n’est possible à t*. La branche algébrique définie après le pôle est une autre solution sur un autre intervalle ; elle n’est pas un prolongement à travers t*.

## 29. Logistique : résoudre et prévoir le sens du mouvement

Sup → Spé · Laboratoire `explosion_logistique`

Résoudre z′=rz(1−z/K), z(0)=z₀>0. Traiter également les équilibres et discuter les cas z₀<K et z₀>K.

**Correction guidée**

Les équilibres sont 0 et K ; il faut les noter avant de séparer les variables. Pour une donnée positive, z=K/[1+(K/z₀−1)e^(−rt)]. Si z₀<K, le dénominateur décroît vers 1 et z croît vers K. Si z₀>K, le dénominateur croît vers 1 et z décroît vers K. z₀=K donne la constante K ; z₀=0 donne la constante 0.

## 30. Linéariser au bon équilibre

Spé · Laboratoire `explosion_logistique`

Poser z=K+η dans la logistique. Trouver le taux de relaxation des petites perturbations et le comparer à celui près de 0.

**Correction guidée**

η′=r(K+η)(−η/K)=−rη−rη²/K. Au premier ordre η′≈−rη, donc η≈η₀e^(−rt). Près de 0, z′≈rz, donc une petite perturbation positive croît comme eʳᵗ. K est stable et 0 est instable à droite. La linéarisation décrit des écarts suffisamment petits, pas tout le mouvement à grande amplitude.

## 31. Amortissement critique avec des données explicites

Sup · Laboratoire `oscillateur_resonance`

Résoudre y″+2ω₀y′+ω₀²y=0, y(0)=1,y′(0)=0, ω₀>0. Vérifier le comportement au départ.

**Correction guidée**

La racine double −ω₀ donne y=(A+Bt)e^(−ω₀t). A=1 et y′(0)=B−ω₀A=0 imposent B=ω₀. Donc y=(1+ω₀t)e^(−ω₀t), y′=−ω₀²te^(−ω₀t). La dérivée est nulle au départ puis négative, et y tend vers 0 sans oscillation. Un sinus de pulsation nulle n’aurait pas fourni le facteur t nécessaire.

## 32. La résonance non amortie est une croissance

Sup → Spé · Laboratoire `oscillateur_resonance`

Résoudre y″+ω₀²y=Fcos(ω₀t), y(0)=y′(0)=0. Vérifier par dérivation puis commenter l’amplitude.

**Correction guidée**

Une particulière est y=Ft sin(ω₀t)/(2ω₀). Elle vérifie les deux données nulles. Sa dérivée vaut F[sin(ω₀t)+ω₀tcos(ω₀t)]/(2ω₀), et sa dérivée seconde ajoutée à ω₀²y vaut Fcos(ω₀t). L’enveloppe Ft/(2ω₀) croît ; il n’existe aucune amplitude stationnaire finie. Sur une durée fixée, un maximum reste mesurable, mais dépend de cette durée.

## 33. Résonance en déplacement et puissance

Spé · Laboratoire `oscillateur_resonance`

Établir |U| pour l’oscillateur amorti forcé, déterminer son maximum éventuel et retrouver le bilan d’énergie.

**Correction guidée**

U=F/(ω₀²−ω²+2iζω₀ω), donc |U|=F/[ω₀²√((1−r²)²+4ζ²r²)], r=ω/ω₀. Dériver le dénominateur au carré donne r²=1−2ζ² ; une résonance à r>0 existe si ζ<1/√2. Multiplier l’EDO par y′ donne E′=Fcos(ωt)y′−2ζω₀(y′)². Une moyenne sur un régime périodique établi impose puissance injectée moyenne égale à puissance dissipée moyenne.

## 34. Le Wronskien de l’exercice 1

Spé · Laboratoire `variation_constantes`

Pour y″−5y′+6y=g, calculer le Wronskien de e²ˣ,e³ˣ et les dérivées des coefficients de variation des constantes.

**Correction guidée**

W=e²ˣ3e³ˣ−2e²ˣe³ˣ=e⁵ˣ. Imposer a′e²ˣ+b′e³ˣ=0 et 2a′e²ˣ+3b′e³ˣ=g. Cramer donne a′=−ge^(−2x), b′=ge^(−3x). Pour g=eˣ/cosh²x, a′=−e^(−x)/cosh²x et b′=e^(−2x)/cosh²x. W ne s’annule jamais, donc la construction est valable sur tout ℝ.

## 35. Une particulière à deux données nulles

Spé · Laboratoire `variation_constantes`

Poser K(u)=e³ᵘ−e²ᵘ et y_p(x)=∫₀ˣK(x−s)g(s)ds. Vérifier l’EDO et les données y_p(0)=y_p′(0)=0.

**Correction guidée**

K(0)=0, K′(0)=1 et K″−5K′+6K=0. La première dérivation donne y_p′=∫₀ˣK′(x−s)g(s)ds ; la seconde ajoute g(x). Combiner les trois intégrales donne y_p″−5y_p′+6y_p=g. À x=0 les intégrales sont nulles, donc y_p et y_p′ le sont. Ces identités demandent seulement g continue pour les dérivations considérées.

## 36. Ajuster deux constantes et mesurer la sensibilité

Spé · Laboratoire `variation_constantes`

Ajouter une homogène à la particulière précédente pour imposer y(0)=y₀,y′(0)=v₀. Comment une petite erreur ε sur v₀ se propage-t-elle ?

**Correction guidée**

On résout A+B=y₀, 2A+3B=v₀, d’où A=3y₀−v₀ et B=v₀−2y₀. Une erreur ε sur v₀ change la solution de ε(e³ˣ−e²ˣ). Elle est fortement amplifiée pour x>0. Ce comportement vient du problème lui-même ; un contrôle numérique doit comparer l’erreur à une échelle adaptée au mouvement et ne pas supposer une stabilité absente.

## 37. Transformer une équation d’Euler–Cauchy

Spé · Laboratoire `euler_cauchy`

Pour x>0, poser x=eᵗ et Y(t)=y(eᵗ). Exprimer Y′ et Y″, puis transformer x²y″+xy′−y=f(x).

**Correction guidée**

Y′=xy′ et Y″=xy′+x²y″. L’équation devient Y″−Y=f(eᵗ). L’homogène a pour solutions eᵗ,e^(−t), qui redonnent x et 1/x. Le changement impose x>0 ; on peut traiter x<0 avec x=−eᵗ. Le point 0 n’est atteint que lorsque t→−∞ et doit être étudié par prolongement.

## 38. Identifier la série et ses premiers coefficients

Spé · Laboratoire `euler_cauchy`

Résoudre par série entière x²y″+xy′−y=x²/(1−x²) au voisinage de 0. Quels coefficients sont libres ?

**Correction guidée**

Pour y=∑aₘxᵐ, le membre gauche vaut ∑(m²−1)aₘxᵐ. Le second membre est ∑ₙ≥₁x²ⁿ. On obtient a₀=0, a₁ libre, a₂ₙ=1/(4n²−1), et les autres coefficients impairs nuls. Ainsi y=a₁x+x²/3+x⁴/15+x⁶/35+… . Le rayon de la particulière est 1. La série est régulière et ne contient pas le mode 1/x.

## 39. Prolonger une formule présentant 0/0

Spé · Laboratoire `euler_cauchy`

Étudier en 0 P(x)=[(x²−1)ln|(1+x)/(1−x)|+2x]/(4x). Donner P(0),P′(0),P″(0) et préciser les singularités restantes.

**Correction guidée**

ln((1+x)/(1−x))=2(x+x³/3+x⁵/5+…). La substitution donne P=x²/3+x⁴/15+… . Le prolongement est analytique, P(0)=P′(0)=0 et P″(0)=2/3. Un terme C₂/x ne serait pas prolongeable régulièrement et doit être exclu. Les points ±1 restent singuliers pour le second membre de l’EDO ; ce calcul en 0 ne les supprime pas.

## 40. Vérifier une solution globale au point singulier

Spé · Laboratoire `riccati`

Pour c>0, vérifier sur tout ℝ que y=cx²−1/(4c) satisfait xy′=y+√(x²+y²). Pourquoi c>0 est-il utile ?

**Correction guidée**

On calcule x²+y²=(cx²+1/(4c))². Le facteur cx²+1/(4c) est positif si c>0 ; sa valeur absolue est donc lui-même. Le membre droit vaut 2cx², comme xy′ avec y′=2cx. À x=0 il vaut −1/(4c)+1/(4c)=0. La positivité de c fixe le signe de la racine ; sans elle, on ne pourrait pas supprimer la valeur absolue de la même manière.

## 41. Riccati : produire un pôle par une solution linéaire

Spé → Au-delà · Laboratoire `riccati`

Transformer z′=z²−1 par z=−u′/u, imposer z(0)=z₀ et trouver le temps d’explosion pour z₀>1.

**Correction guidée**

z′=z²−u″/u, donc prendre u″=u. Avec u(0)=1,u′(0)=−z₀, u=cosh t−z₀sinh t. Il s’annule lorsque tanh t=1/z₀, donc t*=argth(1/z₀)>0. Le quotient z=(z₀cosh t−sinh t)/u explose à ce point, alors que u reste une solution régulière de l’EDO linéaire. Le changement est valable seulement entre deux zéros de u.

## 42. Deux équilibres de Riccati et leur stabilité

Spé · Laboratoire `riccati`

Étudier qualitativement z′=z²−1 autour de −1 et 1, puis vérifier les solutions constantes dans la formule explicite.

**Correction guidée**

Le second membre vaut (z−1)(z+1) : il est positif pour z<−1 et z>1, négatif entre −1 et 1. Les trajectoires proches de −1 y reviennent, celles proches de 1 s’en éloignent. Dans la formule explicite, z₀=−1 donne u=eᵗ et z=−1 ; z₀=1 donne u=e^(−t) et z=1. Ces deux cas doivent être conservés, notamment avant une séparation par z²−1.

## 43. Écrire la matrice et le bilan total

Spé · Laboratoire `lineaire_systeme`

Écrire A pour trois réservoirs symétriquement couplés de taux k₁₂,k₂₃,k₁₃, avec perte δ. Montrer S′=−δS.

**Correction guidée**

A a pour diagonale (−k₁₂−k₁₃−δ,−k₁₂−k₂₃−δ,−k₁₃−k₂₃−δ), et pour coefficients hors diagonale kᵢⱼ. Les sommes de colonnes sont −δ, donc (1,1,1)AY=−δ(Y₁+Y₂+Y₃). Ainsi S′=−δS et S=S₀e^(−δt). La perte peut réduire chaque quantité sans modifier la conservation des échanges internes.

## 44. Échanges identiques : diagonaliser sans déterminant

Spé · Laboratoire `lineaire_systeme`

Avec tous les taux égaux à k>0 et δ=0, déterminer les modes et l’évolution d’une quantité initiale placée dans le premier réservoir.

**Correction guidée**

A=k(J−3I), où J est la matrice de tous les 1. Le vecteur uniforme a valeur propre 0 ; tout vecteur de somme nulle a valeur propre −3k. Décomposer (1,0,0)=(1/3,1/3,1/3)+(2/3,−1/3,−1/3). Donc Y₁=1/3+(2/3)e^(−3kt), Y₂=Y₃=1/3−(1/3)e^(−3kt). Ces trois quantités sont positives et de somme 1.

## 45. Démontrer les taux négatifs et interpréter les proportions

Spé · Laboratoire `lineaire_systeme`

Pour δ=0, démontrer vᵀAv≤0. Que deviennent les valeurs propres et les proportions lorsqu’on ajoute une perte uniforme δ ?

**Correction guidée**

vᵀAv=−∑ᵢ<ⱼkᵢⱼ(vᵢ−vⱼ)²≤0. Le noyau est le mode uniforme puisque les taux sont positifs ; les autres valeurs propres sont strictement négatives. Ajouter −δI translate toutes les valeurs propres de −δ. Comme S=e^(−δt), les proportions P=Y/S satisfont P′=(A+δI)P et retrouvent le système conservatif. Elles tendent vers 1/3, tandis que les quantités tendent vers 0 si δ>0.

## 46. Unicité de Cauchy contre non-unicité aux bords

Spé · Laboratoire `green_bords`

Donner un exemple où y″+y=0, y(0)=y(π)=0 possède une infinité de solutions. Comparer à y(0)=0,y′(0)=1.

**Correction guidée**

Toutes les fonctions Csin x satisfont les deux valeurs aux bords, donc l’unicité échoue. Pour le problème de Cauchy, écrire y=Acos x+Bsin x ; y(0)=0 impose A=0 et y′(0)=1 impose B=1. La solution est sin x. Deux conditions ne jouent pas le même rôle lorsqu’elles sont imposées en deux points ou au même point.

## 47. Démontrer l’incompatibilité à la résonance

Spé · Laboratoire `green_bords`

Montrer qu’il n’existe aucune solution de y″+y=sin x sur [0,π] avec y(0)=y(π)=0.

**Correction guidée**

Multiplier par sin x et intégrer. Deux intégrations par parties, les quatre valeurs aux bords étant nulles, donnent ∫₀^π(y″+y)sin x dx=0. Le second membre impose ∫₀^πsin²x dx=π/2, contradiction. Ce raisonnement démontre l’absence de solution ; tracer une très grande courbe obtenue en divisant par un petit dénominateur ne la remplacerait pas.

## 48. Compatibilité et amplitude libre d’un troisième mode

Spé → Au-delà · Laboratoire `green_bords`

Résoudre y″+9y=sin x+(1/2)sin(2x), y(0)=y(π)=0. Expliquer pourquoi aucune donnée du second membre ne fixe le mode sin(3x).

**Correction guidée**

Une particulière est (1/8)sin x+(1/10)sin(2x), car 9−1=8 et (1/2)/(9−4)=1/10. Ajouter Csin(3x), C réel, donne toutes les solutions satisfaisant les bords. Le second membre est orthogonal à sin(3x), donc compatible avec la valeur résonante 9 ; il ne détermine pas l’amplitude du mode appartenant au noyau. Une condition supplémentaire adaptée pourrait la fixer.

## 49. Une valeur suffit-elle ?

Sup · Laboratoire `cauchy_additive`

f est continue et additive sur ℝ, avec f(3)=−6. Déterminer f(√2). Que reste-t-il vrai si l’on retire la continuité ?

**Correction guidée**

f(3)=3f(1) impose f(1)=−2. La continuité donne **f(x)=−2x**, donc f(√2)=−2√2. Sans régularité, seules les valeurs f(r)=−2r pour r rationnel sont ainsi imposées ; cette argumentation ne détermine pas f(√2).

## 50. Une hypothèse locale devient globale

Sup → Spé · Laboratoire `cauchy_additive`

Montrer qu’une fonction additive continue en 7 est continue en tout point de ℝ. Éviter de supposer d’emblée une continuité globale.

**Correction guidée**

Pour h→0, f(h)=f(7+h)−f(7)→0. Pour x fixé, f(x+h)−f(x)=f(h)→0. Ainsi **f est continue partout** ; le raisonnement sur les rationnels permet alors sa classification.

## 51. Détecter une perturbation avec un seul couple

Sup · Laboratoire `cauchy_additive`

Le candidat est f(x)=ax+b sin x. Trouver un couple qui force b=0 si l’équation additive est vérifiée.

**Correction guidée**

Choisir x=y=π/2 : f(π)−2f(π/2)=−2b. L’équation impose donc **b=0**. Cette substitution rejette chaque candidat perturbé sans inspection graphique.

## 52. Identifier une échelle logarithmique

Sup · Laboratoire `cauchy_multiplicative`

f est continue sur ]0,+∞[, f(xy)=f(x)+f(y), et f(2)=3. Déterminer f(8), f(1/2) et f(3).

**Correction guidée**

f(x)=(3/ln 2)ln x. Donc **f(8)=9, f(1/2)=−3, f(3)=3ln 3/ln 2**. Les deux premières valeurs se déduisent aussi directement de l’équation.

## 53. Pourquoi peut-on prendre le logarithme de f ?

Sup → Spé · Laboratoire `cauchy_multiplicative`

Pour une solution continue non nulle de f(xy)=f(x)f(y) sur ]0,+∞[, prouver f(x)>0. Déterminer ensuite la solution vérifiant f(4)=2.

**Correction guidée**

f(1)=1 et f(x)f(1/x)=1, donc f ne s’annule pas. Puis f(x)=f(√x)²>0. La classification donne f(x)=xᵃ ; 4ᵃ=2 impose **a=1/2**, donc f(x)=√x.

## 54. Passer à une équation différentielle

Spé · Laboratoire `cauchy_multiplicative`

Supposer f dérivable, multiplicative et non nulle sur ]0,+∞[. Montrer qu’elle vérifie xf′=af, puis résoudre avec f(1)=1.

**Correction guidée**

Dériver en y : xf′(xy)=f(x)f′(y). En y=1, xf′(x)=af(x), avec a=f′(1). Comme f>0, (ln f)′=a/x. Intégrer et utiliser f(1)=1 : **f(x)=exp(a ln x)=xᵃ**.

## 55. Une solution prescrite par la courbure en 0

Spé · Laboratoire `dalembert`

f∈C²(ℝ) vérifie l’équation de d’Alembert et f″(0)=−9. Déterminer f et vérifier la réciproque.

**Correction guidée**

La solution nulle est impossible. Donc f(0)=1, f′(0)=0 et f″=−9f. Le problème initial donne **f(x)=cos(3x)**. La formule d’addition du cosinus vérifie l’équation initiale.

## 56. La fonction constante ne doit pas être oubliée

Sup · Laboratoire `dalembert`

Quelles fonctions constantes vérifient l’équation de d’Alembert ? À quoi correspond le cas λ=0 dans la preuve différentielle ?

**Correction guidée**

Si f=c, l’équation donne 2c=2c², donc **c=0 ou c=1**. Dans le cas non nul, λ=0 avec f(0)=1 et f′(0)=0 donne uniquement 1. La constante 0 a été isolée avant cette étape.

## 57. Du double angle aux polynômes

Sup → Spé · Laboratoire `dalembert`

Déduire des relations sur f(2x) et f(3x) à partir de l’équation, en supposant f(0)=1.

**Correction guidée**

Avec y=x, **f(2x)=2f(x)²−1**. Avec les paramètres 2x et x, f(3x)+f(x)=2f(2x)f(x), donc **f(3x)=4f(x)³−3f(x)**. On reconnaît les deux premiers polynômes de Chebyshev non triviaux.

## 58. Déterminer les valeurs en ±1 avant la formule générale

Sup · Laboratoire `identification_symetrie`

Pour l’équation f(x)+f(−x)/x=x, calculer f(1) et f(−1) par deux substitutions.

**Correction guidée**

À x=1 : f(1)+f(−1)=1. À x=−1 : f(−1)−f(1)=−1. Additionner et soustraire donne **f(1)=1, f(−1)=0**. Ces valeurs fournissent un premier contrôle de la formule générale.

## 59. Existence, unicité, domaine

Sup · Laboratoire `identification_symetrie`

Résoudre l’équation sur ℝ privé de 0. La valeur f(0) est-elle imposée ? Donner le prolongement continu éventuel.

**Correction guidée**

Le système au couple ±x donne **f(x)=x²(x+1)/(1+x²)**. La substitution vérifie l’existence. Sur ce domaine, f(0) n’existe pas et n’est donc pas imposée ; si l’on demande une extension à ℝ, sa valeur peut être arbitraire. La continuité en 0 impose la seule valeur **0**.

## 60. Une erreur petite, un défaut non petit

Sup → Spé · Laboratoire `identification_symetrie`

Remplacer la solution par f(x)+b sin x. Calculer le résidu de l’équation et sa limite en 0.

**Correction guidée**

Le défaut est b[sin x−sin x/x]. Comme sin x→0 et sin x/x→1, il tend vers **−b**. Une perturbation de la fonction qui s’annule en 0 ne donne donc pas forcément un défaut d’équation qui s’annule en 0.

## 61. Calculer une intégrale à paramètre sans primitive élémentaire

Sup → Spé · Laboratoire `gamma_euler`

Pour a>0, calculer I(a)=∫₀∞t^(3/2)e^(−at)dt. Préciser le changement de variable et les conditions de convergence.

**Correction guidée**

Le noyau est intégrable en 0 car 3/2>−1, et à l’infini car a>0. Poser u=at : dt=du/a et t^(3/2)=u^(3/2)/a^(3/2). Ainsi I(a)=Γ(5/2)/a^(5/2)=**3√π/(4a^(5/2))**. Il faut transformer à la fois la fonction et l’élément différentiel.

## 62. Justifier une dérivation et obtenir une identité logarithmique

Spé · Laboratoire `gamma_euler`

Pour x>0, établir ∫₀∞(ln t)tˣe^(−t)dt=Γ(x)+xΓ′(x). Justifier la dérivation de la relation de récurrence.

**Correction guidée**

Sur tout compact positif, les noyaux avec ln t sont dominés séparément près de 0 et à l’infini. Γ est donc dérivable et Γ′(x+1)=∫₀∞(ln t)tˣe^(−t)dt. En dérivant Γ(x+1)=xΓ(x), on obtient **Γ′(x+1)=Γ(x)+xΓ′(x)**. Une identité fonctionnelle et un théorème d’analyse permettent de traiter une intégrale difficile.

## 63. Un encadrement de la queue dans un cas entier

Sup → Spé · Laboratoire `gamma_euler`

Évaluer exactement ∫ᵀ∞t³e^(−t)dt pour T>0, puis en déduire l’erreur de troncature de Γ(4). Une quadrature exacte sur [0,T] suffirait-elle à supprimer cette erreur ?

**Correction guidée**

Trois intégrations par parties donnent **e^(−T)(T³+3T²+6T+6)**. Γ(4)=6 ; la différence entre 6 et l’intégrale tronquée est ce terme positif. Même une intégration parfaite sur [0,T] laisserait cette queue : augmenter la précision de quadrature et augmenter T corrigent deux erreurs différentes.

## 64. Une intégrale trigonométrique non entière

Sup → Spé · Laboratoire `beta_geometrie`

Exprimer ∫₀^(π/2)√(sinθ)cos²θdθ avec les fonctions gamma. Vérifier la convergence aux deux extrémités.

**Correction guidée**

Les exposants p=1/2 et q=2 sont supérieurs à −1. La formule trigonométrique donne ½B(3/4,3/2)=**Γ(3/4)Γ(3/2)/(2Γ(9/4))**. On peut remplacer Γ(3/2) par √π/2 et Γ(9/4) par (5/4)(1/4)Γ(1/4). Il n’est pas nécessaire de trouver une primitive élémentaire.

## 65. Une densité qui se concentre

Sup → Spé · Laboratoire `beta_geometrie`

On choisit a=2k et b=3k, avec k>0. Calculer la moyenne et la variance. Que deviennent-elles quand k tend vers l’infini ?

**Correction guidée**

La moyenne vaut **2/5** pour tout k. La variance vaut (6k²)/(25k²(5k+1))=**6/[25(5k+1)]**, donc tend vers 0. La masse se concentre autour de 2/5. Par l’inégalité de Bienaymé–Tchebychev, la probabilité de s’écarter de cette moyenne de plus de ε est au plus Var/ε² et tend vers 0.

## 66. Changer [0,1] en [0,+∞[

Spé · Laboratoire `beta_geometrie`

Pour a,b>0, montrer B(a,b)=∫₀∞u^(a−1)/(1+u)^(a+b)du. Identifier les comportements aux deux bornes.

**Correction guidée**

Poser t=u/(1+u), donc dt=du/(1+u)² et 1−t=1/(1+u). Les facteurs se rassemblent en u^(a−1)/(1+u)^(a+b). En 0, le noyau est équivalent à u^(a−1) ; à l’infini, à u^(−b−1). Les deux convergences correspondent exactement à **a>0 et b>0**. Un changement t=1/(1+u) échange plutôt a et b.

## 67. Obtenir une précision avec les termes bruts

Sup · Laboratoire `zeta_series`

Pour ζ(2), combien de termes suffisent à garantir ζ(2)−S_N≤10⁻⁴ par comparaison intégrale ? Pourquoi cette garantie est-elle différente de la largeur de l’encadrement corrigé ?

**Correction guidée**

R_N≤1/N, donc **N≥10 000** suffit. Mais ζ(2) est entre S_N+1/(N+1) et S_N+1/N : la largeur est 1/[N(N+1)], de l’ordre de N⁻². La première garantie utilise S_N seul ; la seconde utilise une correction du reste. À N=100, la largeur corrigée est inférieure à 10⁻⁴.

## 68. Un nombre de termes gigantesque près du bord

Spé · Laboratoire `zeta_series`

Avec s=1,1, utiliser le majorant intégral pour trouver une condition suffisante sur N afin que R_N≤0,1. Commenter cette méthode de calcul.

**Correction guidée**

R_N≤10N^(−0,1). Exiger 10N^(−0,1)≤0,1 donne N^(0,1)≥100, donc **N≥10²⁰**. La sommation brute devient irréaliste. Une accélération analytique, par exemple Euler–Maclaurin, est utile. Ce résultat explique la lenteur sans prétendre que le majorant est le nombre de termes optimal.

## 69. Dérivation uniforme et signe de la dérivée

Spé · Laboratoire `zeta_series`

Justifier ζ′(s)=−Σ_(n≥2)(ln n)n^(−s) sur [3/2,3]. En déduire la monotonie et la convexité.

**Correction guidée**

Sur ce segment, les termes dérivés sont majorés par (ln n)n^(−3/2), qui est sommable, par exemple car ln n≤Cn^(1/4). La série initiale converge en un point ; le théorème de dérivation des séries s’applique. Les termes de ζ′ sont négatifs et ceux de ζ″=Σ(ln n)²n^(−s) positifs. On obtient **ζ′<0 et ζ″>0** sur le segment, puis sur tout ]1,+∞[ en changeant de compact.

## 70. Une intégrale issue du rayonnement

Spé · Laboratoire `zeta_integrale`

Calculer ∫₀∞t³/(eᵗ−1)dt en utilisant ζ(4)=π⁴/90. Justifier la convergence indépendamment de la valeur trouvée.

**Correction guidée**

En 0, le noyau est équivalent à t², intégrable. À l’infini il est équivalent à t³e^(−t), intégrable. L’identité donne Γ(4)ζ(4)=6π⁴/90=**π⁴/15**. La vérification du domaine précède le calcul et ne peut être remplacée par la seule finitude de la formule finale.

## 71. Modifier l’échelle sans recalculer l’intégrale

Sup → Spé · Laboratoire `zeta_integrale`

Pour a>0 et s>1, exprimer ∫₀∞t^(s−1)/(e^(at)−1)dt. Que se passe-t-il si a est multiplié par 2 ?

**Correction guidée**

Poser u=at. Le différentiel apporte 1/a et la puissance apporte a^(1−s), donc l’intégrale vaut **a^(−s)Γ(s)ζ(s)**. Quand a double, la valeur est multipliée par 2^(−s). Cette propriété permet de contrôler un calcul dimensionnel et de détecter l’oubli d’un facteur dans dt.

## 72. Pourquoi s=1 est-il exclu ?

Sup → Spé · Laboratoire `zeta_integrale`

Étudier ∫₀¹t^(s−1)/(eᵗ−1)dt pour s=1 et pour s=1+δ, δ>0 petit. Identifier l’ordre de grandeur dominant.

**Correction guidée**

Pour s=1, le noyau est équivalent à 1/t : l’intégrale diverge logarithmiquement. Pour s=1+δ, il est équivalent à t^(δ−1), dont l’intégrale sur [0,1] vaut 1/δ. Plus précisément la différence entre le noyau et t^(δ−1) reste uniformément intégrable pour δ dans un petit intervalle positif. L’intégrale vaut donc **1/δ+O(1)**. Le bord du domaine crée une grande contribution concentrée près de 0.

## 73. Vérifier deux demi-intégrations

Spé · Prolongement · Laboratoire `integrale_fractionnaire`

Calculer J^(1/2)(1), puis J^(1/2)[J^(1/2)(1)]. Comparer à J(1).

**Correction guidée**

J^(1/2)(1)=t^(1/2)/Γ(3/2)=2√t/√π. Ensuite J^(1/2)(t^(1/2))=Γ(3/2)t/Γ(2)=√π t/2. En multipliant par 2/√π, on trouve **t=J(1)**. Les coefficients gamma sont indispensables pour que la composition donne exactement l’ordre 1.

## 74. Mémoire après une impulsion

Spé · Prolongement · Laboratoire `integrale_fractionnaire`

Une impulsion est égale à 1 sur [0,a]. Pour α=1/2, trouver sa réponse après a et un équivalent pour t→+∞.

**Correction guidée**

Pour t>a, la réponse est **2(√t−√(t−a))/√π**. Rationaliser : √t−√(t−a)=a/(√t+√(t−a))∼a/(2√t). La réponse est donc équivalente à **a/√(πt)**. Elle tend vers 0, mais ne s’annule pas brusquement après la fin de l’impulsion.

## 75. Détecter une confusion d’opérateurs

Spé · Prolongement · Laboratoire `integrale_fractionnaire`

Un calcul propose J^αf(t)=f(t)t^α/Γ(α+1) pour toute f. Vérifier cette proposition avec f(t)=t et expliquer pourquoi elle marche pourtant pour une constante.

**Correction guidée**

La formule exacte donne J^α(t)=t^(α+1)/Γ(α+2), alors que la proposition donne t^(α+1)/Γ(α+1), soit un facteur α+1 de trop. Pour une constante, on peut sortir f de l’intégrale et intégrer le noyau, ce qui donne effectivement t^α/Γ(α+1). Pour une fonction variable, **on ne peut pas remplacer f(u) par f(t)** sous une intégrale qui porte sur tout le passé.

## 76. Dérivée d’ordre 1/2 d’une constante

Spé · Prolongement · Laboratoire `derivees_fractionnaires`

Pour f(t)=3 et t>0, calculer D_RL^(1/2)f et D_C^(1/2)f. Expliquer la singularité éventuelle en 0.

**Correction guidée**

J^(1/2)(3)=6√t/√π ; en dérivant, **D_RL^(1/2)f=3/√(πt)**. Pour Caputo, on dérive d’abord : f′=0 et le résultat est **0**. La singularité t^(−1/2) en 0 appartient à l’opérateur RL avec borne initiale 0 ; elle ne signifie pas que la fonction constante serait discontinue.

## 77. Une puissance nulle à l’origine

Spé · Prolongement · Laboratoire `derivees_fractionnaires`

Pour f(t)=t², calculer la dérivée de Caputo d’ordre 1/2. Retrouver le même résultat avec la définition de Riemann–Liouville.

**Correction guidée**

La formule donne Γ(3)t^(3/2)/Γ(5/2)=**8t^(3/2)/(3√π)**. Pour RL, intégrer d’ordre 1/2 : J^(1/2)(t²)=Γ(3)t^(5/2)/Γ(7/2)=16t^(5/2)/(15√π), puis dériver. On retrouve 8t^(3/2)/(3√π). L’égalité vient de f(0)=0 ; elle ne vaut pas pour toute fonction.

## 78. Deux histoires identiques au dernier instant

Spé · Prolongement · Laboratoire `derivees_fractionnaires`

Pour f₁(t)=t et f₂(t)=t+t(1−t)², vérifier f₁(1)=f₂(1) et f₁′(1)=f₂′(1). Calculer l’écart de leurs dérivées de Caputo d’ordre 1/2 en t=1.

**Correction guidée**

Le terme t(1−t)² et sa dérivée s’annulent en 1 : valeur et pente valent 1. L’écart de Caputo est Γ(2)/Γ(3/2)−2Γ(3)/Γ(5/2)+Γ(4)/Γ(7/2), soit (2−16/3+16/5)/√π=**−2/(15√π)**. La dérivée fractionnaire distingue leurs histoires. Le résultat se vérifie directement en intégrant [1−4u+3u²]/√(1−u) sur [0,1], divisé par √π.

## 79. Dérivée quatrième : reconstruire les coefficients

Spé · Laboratoire `faa_di_bruno`

Pour g quadratique, exprimer (f∘g)^(4) en fonction de f^(2),f^(3),f^(4),g′ et g″. Retrouver les coefficients en listant m₁+2m₂=4.

**Correction guidée**

Les couples (m₁,m₂) sont (4,0),(2,1),(0,2). Les coefficients 4!/[m₁!m₂!2^m₂] sont 1,6,3. Ainsi **(f∘g)^(4)=f^(4)(g)(g′)⁴+6f^(3)(g)(g′)²g″+3f″(g)(g″)²**. Dans le cas général il faudrait aussi les termes contenant g‴ et g^(4), qui sont ici nuls.

## 80. Une inverse avec une récurrence de Leibniz

Spé · Laboratoire `faa_di_bruno`

Soit h(x)=1/(1+x²). Sans utiliser de différences finies, calculer h^(6)(0), puis h^(2r)(0) et h^(2r+1)(0).

**Correction guidée**

La fonction est paire : les dérivées impaires en 0 sont nulles. Avec g=1+x², la récurrence donne h^(n)(0)=−n(n−1)h^(n−2)(0), puisque g′(0)=0 et g″=2. Partant de h(0)=1, on obtient **h^(2r)(0)=(−1)^r(2r)!**, donc h^(6)(0)=−720. Cela coïncide avec le développement Σ(−1)^r x^(2r) pour |x|<1.

## 81. Un coefficient de Bell contrôlé par une exponentielle

Spé · Prolongement · Laboratoire `faa_di_bruno`

Pour g(x)=x, expliquer pourquoi la formule de Faà di Bruno ne conserve qu’un terme. Pour g(x)=x², quels termes peuvent contribuer en x=0 ?

**Correction guidée**

Si g=x, g′=1 et les dérivées supérieures sont nulles : seul m₁=n subsiste, donnant f^(n)(x). Si g=x², en 0 on a g′=0 et g″=2. Il faut m₁=0, donc n doit être pair, n=2r. Le coefficient donne **(f(x²))^(2r)(0)=(2r)!f^(r)(0)/r!**, et les dérivées impaires sont nulles. Pour f=exp, cela donne (2r)!/r!, vérifiable avec exp(x²)=Σx^(2r)/r!.

## 82. Dériver trois fois une gaussienne

Sup → Spé · Laboratoire `hermite_gauss`

Calculer H₃ avec la récurrence, puis (d³/dx³)e^(−x²). Vérifier la parité.

**Correction guidée**

H₃=2xH₂−4H₁=2x(4x²−2)−8x=**8x³−12x**. La dérivée troisième est (−1)³H₃e^(−x²)=**(12x−8x³)e^(−x²)**. Elle est impaire, comme la troisième dérivée d’une fonction paire. Le signe (−1)^n de Rodrigues ne doit pas être omis.

## 83. Orthogonalité sans argument de parité

Spé · Laboratoire `hermite_gauss`

Calculer ∫ℝH₂(x)e^(−x²)dx, puis expliquer pourquoi ∫ℝH₂H₄e^(−x²)dx=0 bien que l’intégrande soit paire.

**Correction guidée**

H₂=4x²−2. La relation ∫ℝx²e^(−x²)dx=√π/2 donne 4√π/2−2√π=0. Pour H₂H₄, écrire H₄e^(−x²)=(d⁴/dx⁴)e^(−x²) et intégrer quatre fois par parties : H₂^(4)=0. Les termes de bord s’annulent. **Une intégrande paire peut avoir une intégrale nulle par compensation** ; la parité seule ne fournit pas ce résultat.

## 84. Retrouver une équation différentielle pour la fonction normalisée

Spé · Prolongement · Laboratoire `hermite_gauss`

À partir de Hₙ″−2xHₙ′+2nHₙ=0, vérifier −ψₙ″+x²ψₙ=(2n+1)ψₙ pour ψₙ=CₙHₙe^(−x²/2).

**Correction guidée**

On a ψₙ″=Cₙe^(−x²/2)[Hₙ″−2xHₙ′+(x²−1)Hₙ]. Remplacer Hₙ″−2xHₙ′ par −2nHₙ donne ψₙ″=(x²−2n−1)ψₙ, donc **−ψₙ″+x²ψₙ=(2n+1)ψₙ**. La constante Cₙ se simplifie ; elle sert à la norme, pas à la vérification de cette équation homogène.
