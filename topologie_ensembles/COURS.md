# Topologie & Ensembles · Cours et démonstrations

60 leçons originales, avec variables, hypothèses, preuves et applications. [Laboratoires et lancement](README.md).

## 1. Une boule est définie par une inégalité

**Sup → Spé · TP : boules_normes**

**Objets et but.** Dans ℝ², x=(x₁,x₂) désigne un vecteur, a un centre et r>0 un rayon. Une norme mesure une longueur et induit d(x,y)=‖x−y‖. Les boules des normes 1, 2 et ∞ sont respectivement un losange, un disque et un carré : leur forme change, tandis que leurs définitions restent les mêmes. Un voisinage de a contient une boule ouverte centrée en a ; il n’est pas nécessairement ouvert lui-même.

```text
Bₒ(a,r)={x : ‖x−a‖<r} ; B𝒇(a,r)={x : ‖x−a‖≤r}
‖x‖₁=|x₁|+|x₂| ; ‖x‖₂=√(x₁²+x₂²) ; ‖x‖∞=max(|x₁|,|x₂|)
```

**Démonstration.** Si x∈Bₒ(a,r), poser δ=r−‖x−a‖>0. Pour ‖y−x‖<δ, l’inégalité triangulaire donne ‖y−a‖≤‖y−x‖+‖x−a‖<r : la boule est ouverte. La fonction x↦‖x−a‖ est continue, car |‖x−a‖−‖y−a‖|≤‖x−y‖. Son image réciproque de ]−∞,r] est donc fermée. La marge δ doit être strictement positive pour produire un voisinage intérieur.

**Lire l’expérience.** Pour x=(0,7;0,7) et r=1, ‖x‖₁=1,4, ‖x‖₂=√0,98≈0,98995 et ‖x‖∞=0,7. Le point est hors du losange et dans les deux autres boules. Cela ne contredit pas l’équivalence des normes : celle-ci compare des rayons différents, elle n’identifie pas leurs boules de même rayon.

## 2. Des normes différentes donnent la même topologie en dimension finie

**Sup → Spé · TP : boules_normes**

**Propriété ciblée.** Pour x∈ℝᵈ, on compare les normes usuelles avec des constantes indépendantes de x. Ces inclusions de boules transfèrent les définitions d’ouvert, de convergence et de continuité d’une norme à l’autre.

```text
‖x‖∞≤‖x‖₂≤√d‖x‖∞ ; ‖x‖₂≤‖x‖₁≤√d‖x‖₂
βN₂(x)≤N₁(x)≤αN₂(x), α,β>0
```

**Justification.** La première borne découle du maximum des coordonnées et de la somme des carrés ; Cauchy–Schwarz donne la dernière. Plus généralement une norme N vérifie N(x)≤Σ|xᵢ|N(eᵢ), donc est continue pour la norme euclidienne. Sur la sphère euclidienne compacte, elle atteint un minimum m>0 et un maximum M. Par homogénéité, m‖x‖₂≤N(x)≤M‖x‖₂. Le rôle de la dimension finie et de la compacité est essentiel.

## 3. Trois opérations : intérieur, adhérence, frontière

**Sup → Spé · TP : interieur_frontiere**

**Objets et but.** Pour A⊂E métrique, l’intérieur A° contient les points possédant une boule incluse dans A. L’adhérence Ā contient les points dont toutes les boules rencontrent A. La frontière contient les points où toute boule rencontre A et son complémentaire. « Appartenir à A » et « être adhérent à A » sont deux questions différentes.

```text
x∈A° ⇔ ∃r>0, Bₒ(x,r)⊂A
x∈Ā ⇔ ∀r>0, Bₒ(x,r)∩A≠∅
Fr(A)=Ā∖A°=Ā∩(E∖A)̄
```

**Démonstration.** Si x∉Ā, une boule autour de x manque A, donc est incluse dans E∖A : E∖Ā=(E∖A)°. Inverser le rôle des complémentaires donne E∖A°=(E∖A)̄. En prenant l’intersection, on obtient la formule de frontière, intersection de deux fermés. Ainsi Fr(A) est fermée et Fr(A)=Fr(E∖A). Les quantificateurs ∃r et ∀r distinguent rigoureusement intérieur et adhérence.

**Lire l’expérience.** Pour le disque ouvert épointé A={0<‖x‖₂<1}, A°=A, Ā={‖x‖₂≤1} et Fr(A)={0}∪{‖x‖₂=1}. Le centre absent est un point de frontière, même si le dessin n’en montre qu’un trou minuscule. Pour le disque fermé, la frontière est incluse dans A.

## 4. Ouvert et fermé sont des égalités, non des contraires exclusifs

**Sup → Spé · TP : interieur_frontiere**

**Propriété ciblée.** A est ouvert si A=A° ; A est fermé si A=Ā. Certains ensembles vérifient les deux propriétés, certains aucune. Les mots se rapportent toujours à un espace ambiant fixé.

```text
A°⊂A⊂Ā ; (A°)°=A° ; (Ā)̄=Ā
∅ et E sont ouverts et fermés dans E
```

**Justification.** Toute boule témoin d’intérieur rend ses points intérieurs, donc A° est ouvert. Si un fermé F contient A, tout point hors de F a une boule qui évite A, donc Ā⊂F ; Ā est le plus petit fermé contenant A. Dans ℝ connexe, seules ∅ et ℝ sont simultanément ouvertes et fermées. Dans un espace discret, chaque partie l’est : la propriété dépend de l’espace.

## 5. L’adhérence se construit avec des suites

**Sup → Spé · TP : adherence_suite**

**Objets et but.** L’ensemble A={1/n : n≥1} est infini dénombrable ; N règle seulement le nombre de points dessinés. Chaque 1/n est isolé, tandis que 0, absent de A, en est un point d’accumulation. Un point adhérent n’est pas nécessairement un point d’accumulation : un singleton contient son unique point adhérent, isolé.

```text
Ā=A∪{0} ; A°=∅ ; Fr(A)=A∪{0}
x∈Ā ⇔ ∃(aₙ)∈A^ℕ, aₙ→x
```

**Démonstration.** Si x∈Ā, choisir aₙ∈A∩B(x,1/(n+1)) ; alors d(aₙ,x)<1/(n+1), donc aₙ→x. Réciproquement une suite dans A convergeant vers x finit dans toute boule de centre x, qui rencontre donc A. Pour l’ensemble des 1/n, une suite convergente de ses éléments a soit une sous-suite constante, soit des dénominateurs tendant vers l’infini ; sa limite appartient alors à A ou vaut 0.

**Lire l’expérience.** d(0,A)=infₙ1/n=0 mais ce minimum n’est pas atteint dans A. En ajoutant 0, on obtient un fermé borné de ℝ, donc un compact. Agrandir N ne transforme jamais le dessin fini en preuve de l’absence du point 0 dans A.

## 6. Fermeture séquentielle et suites extraites

**Sup → Spé · TP : adherence_suite**

**Propriété ciblée.** Dans un espace métrique, F est fermé si et seulement si toute suite de F qui converge dans l’espace ambiant a sa limite dans F. La convergence de la suite entière ne se confond pas avec l’existence d’une sous-suite convergente.

```text
F fermé ⇔ [(xₙ∈F et xₙ→x∈E) ⇒ x∈F]
φ:ℕ→ℕ strictement croissante ; xφ(n) est une suite extraite
```

**Justification.** La première assertion découle de F=F̄ et de la caractérisation précédente. Une extraction strictement croissante vérifie φ(n)≥n, donc tend vers l’infini ; si xₙ→x, alors xφ(n)→x. L’inverse est faux : (−1)ⁿ possède deux sous-suites constantes de limites 1 et −1, mais ne converge pas.

## 7. Le mot ouvert dépend de l’espace ambiant

**Sup → Spé · TP : topologie_relative**

**Objets et but.** On fixe X=[0,1] avec la distance héritée de ℝ. Une boule de X vaut Bℝ(x,r)∩X. L’ensemble A=[0,b[ pour 0<b≤1 est ouvert dans X, bien qu’il ne soit pas ouvert dans ℝ. Le bord de l’espace n’est pas automatiquement une frontière relative.

```text
U ouvert dans X ⇔ ∃O ouvert dans E, U=X∩O
F fermé dans X ⇔ ∃C fermé dans E, F=X∩C
```

**Démonstration.** Si U=X∩O, tout x∈U possède une boule ambiante incluse dans O ; son intersection avec X est incluse dans U. Réciproquement choisir pour chaque x∈U une boule B(x,rₓ) dont l’intersection avec X est incluse dans U ; la réunion O de ces boules est ouverte et X∩O=U. La caractérisation des fermés se déduit en prenant les complémentaires dans X.

**Lire l’expérience.** A=X∩]−1/2,b[. Le point zéro est intérieur relativement à X : pour r<b, B_X(0,r)=[0,r[⊂A. Dans ℝ, aucune boule autour de zéro n’est incluse dans A, car elle contient des réels négatifs. Si b>1 dans le laboratoire, A=X tout entier et sa frontière relative est vide.

## 8. Adhérence relative et compacité intrinsèque

**Sup → Spé · TP : topologie_relative**

**Propriété ciblée.** L’adhérence se restreint simplement à X, mais l’intérieur ne suit pas la même formule. La compacité d’une partie K⊂X reste la même dans X et dans l’espace ambiant métrique E.

```text
adh_X(A)=X∩adh_E(A)
int_X(A) peut être plus grand que X∩int_E(A)
```

**Justification.** Les boules relatives rencontrent A exactement lorsque leurs boules ambiantes le rencontrent, d’où la formule d’adhérence pour A⊂X. Pour la compacité, les suites et leurs limites dans K sont les mêmes avec la distance héritée : la caractérisation séquentielle est inchangée. En revanche être fermé dans X ne signifie pas être fermé dans E si X n’est lui-même pas fermé dans E.

## 9. Opérations finies et infinies ne se confondent pas

**Sup → Spé · TP : operations_ouverts**

**Objets et but.** La stabilité des ouverts utilise le nombre d’ensembles intersectés. Une intersection finie permet de prendre le minimum d’un nombre fini de rayons positifs. Ce minimum peut devenir nul lorsque l’on passe à une infinité de contraintes.

```text
⋃ᵢUᵢ ouvert ; U₁∩…∩Uₘ ouvert
⋂ᵢFᵢ fermé ; F₁∪…∪Fₘ fermé
⋂n≥1]−1/n,1/n[={0}
```

**Démonstration.** Dans une réunion, un point appartient à au moins un ouvert et garde la boule témoin de cet ouvert. Dans une intersection finie, si x∈Uⱼ et B(x,rⱼ)⊂Uⱼ, prendre r=minⱼrⱼ>0. Pour la famille ]−1/n,1/n[, tout x≠0 est exclu dès que n>1/|x| ; seul zéro reste. Le singleton {0} n’est pas ouvert dans ℝ.

**Lire l’expérience.** L’intersection après N contraintes est toujours ]−1/N,1/N[, ouverte ; l’intersection infinie est fermée mais non ouverte. De même ⋃n≥1[1/n,1]=]0,1], bien que chaque terme et chaque réunion finie soient fermés. Le passage N→∞ n’est pas une opération finie.

## 10. Densité : l’hypothèse ouvert de l’exercice 8

**Sup → Spé · TP : operations_ouverts**

**Propriété ciblée.** Si A et B sont denses dans E et si A est ouvert, leur intersection est dense. L’ouverture d’un des deux ensembles constitue la réserve de place nécessaire pour utiliser deux fois la densité.

```text
Ā=B̄=E, A ouvert ⇒ (A∩B)̄=E
```

**Justification.** Fixer une boule B(x,r). Par densité de A, elle contient a∈A. L’ensemble B(x,r)∩A est ouvert et contient a, donc contient B(a,ρ) pour un ρ>0. Par densité de B, cette dernière boule contient b∈B. Alors b∈A∩B∩B(x,r), ce qui prouve la densité. Sans ouverture, ℚ et ℝ∖ℚ sont deux parties denses d’intersection vide.

## 11. La distance à un ensemble ne demande pas de projection unique

**Sup → Spé · TP : distance_ensemble**

**Objets et but.** Pour A non vide dans un espace métrique, d(x,A)=inf_{a∈A}d(x,a). Il s’agit d’un infimum, et non automatiquement d’un minimum. La fonction x↦d(x,A) est définie partout et renseigne sur l’adhérence de A.

```text
d(x,A)=inf_{a∈A}d(x,a)
|d(x,A)−d(y,A)|≤d(x,y)
d(x,A)=0 ⇔ x∈Ā
```

**Démonstration.** Pour chaque a∈A, d(x,a)≤d(x,y)+d(y,a). Prendre l’infimum donne d(x,A)≤d(x,y)+d(y,A), puis échanger x et y. Si d(x,A)=0, pour tout ε>0 un a∈A vérifie d(x,a)<ε ; x est adhérent. Réciproquement l’adhérence fournit de tels points pour chaque ε. Pour un compact A, a↦d(x,a) est continue et atteint son minimum ; dans ℝᵈ un fermé non vide suffit également, en restreignant la recherche à une boule bornée.

**Lire l’expérience.** Pour un disque fermé D(c,r), d(x,D)=max(‖x−c‖₂−r,0). Pour une union de deux disques, prendre le minimum des deux distances. Sur la médiatrice de deux disques disjoints, les deux projections peuvent être distinctes : la distance est toujours continue, alors que le choix d’un point projeté peut sauter.

## 12. Existence et unicité d’un point le plus proche sont deux problèmes distincts

**Sup → Spé · TP : distance_ensemble**

**Propriété ciblée.** Une projection minimisante p appartient à A et vérifie d(x,p)=d(x,A). Un ensemble non convexe peut admettre plusieurs minimisants. Un ensemble non fermé peut n’en admettre aucun, même si la distance est nulle.

```text
A=]0,1[, x=0 : d(x,A)=0 sans minimum
A={−1,1}, x=0 : deux projections, −1 et 1
```

**Justification.** Le premier cas suit de 1/n→0 sans appartenance de zéro. Dans le second, les distances sont toutes deux 1. En dimension finie, un fermé assure l’existence, tandis que la convexité et la stricte convexité de la norme euclidienne assurent l’unicité. En norme 1 ou ∞, un convexe fermé peut posséder plusieurs points minimisants : l’unicité doit toujours être reliée à la géométrie de la norme.

## 13. Convexe : un segment entier doit rester dans l’ensemble

**Sup → Spé · TP : convexite**

**Objets et but.** Dans un espace vectoriel réel, C est convexe si tout segment reliant deux de ses points reste dans C. Sur un espace complexe, la convexité utilise également des coefficients réels t∈[0,1]. Une vérification numérique de quelques points du segment ne prouve pas cette propriété universelle.

```text
C convexe ⇔ ∀x,y∈C, ∀t∈[0,1], (1−t)x+ty∈C
Convexe ⇒ connexe par arcs ⇒ connexe
```

**Démonstration.** Pour une boule centrée en a, ‖(1−t)x+ty−a‖≤(1−t)‖x−a‖+t‖y−a‖. Cela reste ≤r pour une boule fermée et <r pour une boule ouverte, extrémités comprises. Le segment γ(t)=(1−t)x+ty est continu et relie x à y, d’où la connexité par arcs. Cette dernière implique la connexité, car une séparation de l’ensemble induirait une séparation de l’intervalle [0,1].

**Lire l’expérience.** L’anneau {1/2≤‖x‖₂≤1} n’est pas convexe : les points (0,8;0) et (−0,8;0) y appartiennent, mais leur milieu est zéro, exclu. Pourtant on les relie par un demi-cercle dans l’anneau. Un seul segment défaillant suffit à réfuter la convexité ; aucun nombre fini de segments réussis ne suffit à l’établir.

## 14. Intersections de convexes et ensembles étoilés

**Sup → Spé · TP : convexite**

**Propriété ciblée.** Une intersection quelconque de convexes est convexe. Un ensemble étoilé possède un point c depuis lequel tous les segments restent dans l’ensemble ; il est donc connexe par arcs, sans être nécessairement convexe.

```text
Cᵢ convexes ⇒ ⋂ᵢCᵢ convexe
Étoilé de centre c : ∀x∈A, [c,x]⊂A
```

**Justification.** Si x et y appartiennent à tous les Cᵢ, chaque combinaison convexe appartient à tous les Cᵢ. Pour un ensemble étoilé, relier x à c puis c à y par deux segments fournit un chemin. Le critère étoilé ne demande rien sur le segment direct entre x et y. L’ensemble des matrices diagonalisables est étoilé de centre zéro : tA reste diagonalisable ; il est ainsi connexe par arcs, même si une somme de matrices diagonalisables peut ne pas l’être.

## 15. L’enveloppe convexe rassemble tous les barycentres

**Sup → Spé · TP : enveloppe_convexe**

**Objets et but.** Pour des points a₁,…,aₘ de ℝᵈ, leur enveloppe convexe est le plus petit convexe qui les contient. Les poids d’un barycentre sont positifs ou nuls et leur somme vaut 1. Un barycentre à poids quelconques peut sortir du polytope : les signes ne sont pas un détail.

```text
conv{a₁,…,aₘ}={Σᵢλᵢaᵢ : λᵢ≥0, Σᵢλᵢ=1}
Δₘ={λ∈ℝᵐ : λᵢ≥0, Σᵢλᵢ=1}
```

**Démonstration.** L’ensemble des barycentres contient les aᵢ et est convexe : une combinaison de deux familles de poids admissibles reste admissible. Tout convexe contenant les points contient leurs combinaisons convexes finies, par récurrence sur le nombre de termes. Ce double argument établit la minimalité. Δₘ est fermé borné ; l’application λ↦Σλᵢaᵢ est continue, donc l’enveloppe d’un ensemble fini est compacte.

**Lire l’expérience.** Le nuage généré possède N points, mais seuls les sommets extrêmes définissent le bord du polygone. Les points intérieurs restent utiles pour des barycentres sans créer de nouvelles arêtes. L’algorithme de chaînes monotones utilise le signe d’un déterminant pour supprimer les tournants qui ne délimitent pas le bord convexe.

## 16. Carathéodory réduit le nombre de points utiles

**Sup → Spé · TP : enveloppe_convexe**

**Propriété ciblée.** Dans ℝᵈ, tout point d’une enveloppe convexe s’exprime à l’aide d’au plus d+1 points. Dans le plan, trois suffisent pour un barycentre ; cela ne signifie pas que le polygone entier possède trois sommets.

```text
x∈conv(A) ⇒ x=Σᵢ₌₁ᵈ⁺¹λᵢaᵢ, λᵢ≥0, Σλᵢ=1
```

**Justification.** Si une combinaison utilise m>d+1 poids strictement positifs, les vecteurs (aᵢ,1) de ℝᵈ⁺¹ sont liés. Il existe μ non nul tel que Σμᵢaᵢ=0 et Σμᵢ=0. Faire varier les poids λᵢ−tμᵢ ne change ni x ni leur somme. Choisir t=min_{μᵢ>0}λᵢ/μᵢ rend au moins un poids nul sans en rendre aucun négatif. Répéter jusqu’à m≤d+1. Ce résultat est un prolongement au-delà des techniques usuelles de barycentre.

## 17. La projection euclidienne se caractérise par un angle

**Spé · TP : projection_convexe**

**Objets et but.** C est un convexe fermé non vide de ℝᵈ euclidien, x un point et p sa projection. Le minimum de la distance existe ; son unicité utilise le carré de la norme euclidienne. La condition angulaire compare x−p à toutes les directions z−p de C.

```text
p=P_C(x) ⇔ p∈C et ∀z∈C, ⟨x−p,z−p⟩≤0
```

**Démonstration.** L’existence découle d’une suite minimisante bornée et de la compacité d’une boule fermée en dimension finie. Pour la nécessité, p+t(z−p)∈C et la dérivée à droite de ‖x−p−t(z−p)‖² en t=0 doit être positive ou nulle, soit −2⟨x−p,z−p⟩≥0. Pour la suffisance, développer ‖x−z‖²=‖x−p‖²+‖z−p‖²−2⟨x−p,z−p⟩≥‖x−p‖². L’inégalité est stricte si z≠p, donc p est unique.

**Lire l’expérience.** Pour un polytope à sommets vⱼ, l’expression ⟨x−p,z−p⟩ est affine en z. Vérifier l’inégalité sur tous les sommets suffit alors pour tous leurs barycentres. Le laboratoire peut donc certifier une propriété universelle par un nombre fini de contraintes, grâce à cette structure analytique, et non grâce à un maillage du bord.

## 18. La projection ne dilate pas les distances

**Spé · TP : projection_convexe**

**Propriété ciblée.** Pour x,y∈ℝᵈ, les projections p=P_C(x), q=P_C(y) satisfont une borne plus précise que la continuité. Elle joue un rôle dans les algorithmes de descente et de point fixe.

```text
‖P_C(x)−P_C(y)‖₂²≤⟨P_C(x)−P_C(y),x−y⟩
‖P_C(x)−P_C(y)‖₂≤‖x−y‖₂
```

**Justification.** La caractérisation donne ⟨x−p,q−p⟩≤0 et ⟨y−q,p−q⟩≤0. Les additionner et réorganiser produit ‖p−q‖²≤⟨p−q,x−y⟩. Cauchy–Schwarz donne la borne lipschitzienne, en divisant par ‖p−q‖ si elle n’est pas nulle. Ce résultat demande une norme issue d’un produit scalaire et un convexe fermé.

## 19. Un trou empêche un segment, pas forcément un chemin

**Sup → Spé · TP : connexite_chemins**

**Objets et but.** Un chemin dans A est une application continue γ:[0,1]→A. A est connexe par arcs si toute paire de points se relie par un chemin. A est connexe si l’on ne peut le partager en deux ouverts relatifs non vides disjoints. Une droite épointée se sépare ; un plan épointé permet de contourner le point retiré.

```text
A connexe ⇔ aucune partition A=U⊔V avec U,V ouverts relatifs non vides
γ(0)=a, γ(1)=b et γ([0,1])⊂A
```

**Démonstration.** Dans ℝ²∖{0}, on relie a à a/‖a‖ par un segment radial de rayon strictement positif, puis les directions a/‖a‖ et b/‖b‖ par un arc de cercle, puis b/‖b‖ à b. Les raccords sont continus et restent hors de zéro. On peut aussi choisir un point c hors des droites ℝa et ℝb et utiliser les deux segments [a,c] et [c,b]. Sur ℝ∖{0}, les parties ]−∞,0[ et ]0,+∞[ constituent une séparation.

**Lire l’expérience.** L’anneau fermé est connexe par arcs mais non convexe. Deux disques fermés séparés par un écart positif sont chacun connexes et forment deux composantes distinctes. Les chemins dessinés sont construits par des formules ; leurs propriétés ne se déduisent pas du seul nombre de pixels.

## 20. Exercice 7 : ℝ et ℝ² ne sont pas homéomorphes

**Sup → Spé · TP : connexite_chemins**

**Propriété ciblée.** Un homéomorphisme est une bijection continue dont l’inverse est continu. Il conserve la connexité et la connexité par arcs, également après retrait de points correspondants.

```text
ℝ²∖{0} connexe par arcs ; ℝ∖{a} non connexe
Donc ℝ² et ℝ ne sont pas homéomorphes
```

**Justification.** Supposons h:ℝ²→ℝ homéomorphisme et posons a=h(0). Sa restriction serait un homéomorphisme de ℝ²∖{0} sur ℝ∖{a}. L’image continue d’un connexe est connexe : une séparation de l’image se tirerait en arrière en une séparation du départ. Or ℝ∖{a}=]−∞,a[⊔]a,+∞[ est séparé, contradiction. Ce raisonnement distingue cardinalité et topologie : ℝ et ℝ² possèdent pourtant le même cardinal.

## 21. Bolzano–Weierstrass extrait, il ne fait pas converger toute la suite

**Sup → Spé · TP : bolzano_weierstrass**

**Objets et but.** Toute suite bornée de ℝᵈ possède une sous-suite convergente. La conclusion porte sur une extraction φ strictement croissante. La suite initiale peut continuer à osciller ; la limite extraite appartient à l’adhérence des valeurs, pas nécessairement à l’ensemble où elles étaient prises.

```text
Suite bornée dans ℝᵈ ⇒ ∃φ strictement croissante, ∃ℓ∈ℝᵈ, xφ(n)→ℓ
```

**Démonstration.** En dimension un, enfermer les valeurs dans un intervalle fermé I₀. Diviser en deux et garder une moitié contenant une infinité de termes. Répéter : les Iₖ sont emboîtés, fermés et de longueur |I₀|/2ᵏ. Leur intersection contient un unique ℓ. Choisir nₖ>nₖ₋₁ avec x_nₖ∈Iₖ ; alors |x_nₖ−ℓ|≤|I₀|/2ᵏ. En ℝᵈ, extraire successivement pour chaque coordonnée ; une extraction d’une suite déjà convergente conserve sa limite.

**Lire l’expérience.** Le laboratoire choisit uₙ=(−1)ⁿ+1/(n+1) et extrait les indices pairs et impairs. Les limites sont respectivement 1 et −1, avec erreur exacte 1/(n+1), sans qu’il soit nécessaire de deviner la limite sur un nuage. La preuve de bissection précédente traite aussi des suites moins explicites. Une suite bornée de matrices 4×4 se traite comme une suite de 16 coordonnées.

## 22. Boule fermée et sphère : la bonne extraction à deux étages

**Sup → Spé · TP : bolzano_weierstrass**

**Propriété ciblée.** Dans un espace normé non nul, la boule unité fermée est compacte si et seulement si la sphère unité est compacte. Pour le sens difficile, il faut extraire simultanément les directions et les rayons, en gérant les termes nuls.

```text
xₙ=rₙvₙ, rₙ=‖xₙ‖∈[0,1], ‖vₙ‖=1 lorsque xₙ≠0
```

**Justification.** Si la boule est compacte, la sphère est fermée dans cette boule, donc compacte. Réciproquement, si une suite de la boule possède une infinité de termes nuls, elle a une sous-suite constante. Sinon retirer un préfixe et écrire xₙ=rₙvₙ. Extraire les directions par compacité de la sphère, puis extraire les rayons de la sous-suite obtenue par compacité de [0,1]. Le produit converge vers rv dans la boule. Il faut réutiliser les mêmes indices pour les deux facteurs.

## 23. Le TP p.17 : records aléatoires et extraction rigoureuse

**Sup → Spé · TP : extraction_aleatoire**

**Objets et but.** On génère des variables indépendantes Uₙ uniformes sur [0,3] et cherche à approcher une cible a intérieure. Un record rapproche le point retenu de a ; une extraction doit en plus conserver des indices strictement croissants. Une simulation finie ne prouve ni une convergence presque sûre ni l’existence d’une infinité de records.

```text
0<ε≤min(a,3−a) : P(|Uₙ−a|<ε)=2ε/3
P(aucun succès dans m essais)=(1−2ε/3)ᵐ
```

**Démonstration.** Pour ε fixé, l’indépendance fait tendre la probabilité d’absence de succès vers zéro lorsque m→∞. Pour chaque k≥1, le rayon εₖ=min(1/k,a/2,(3−a)/2)>0 définit une infinité de succès presque sûrement : la probabilité de ne plus avoir de succès après un rang donné est zéro. L’intersection dénombrable de ces événements de probabilité un garde la probabilité un. On choisit alors nₖ>nₖ₋₁ avec |U_nₖ−a|<εₖ, ce qui construit une sous-suite convergeant vers a presque sûrement.

**Lire l’expérience.** La cible vaut 1 dans le recueil. Les lots géométriquement croissants facilitent la recherche, mais une étape peut ne pas améliorer le record. La version garantie par bissection du labo BW ne choisit pas une cible d’avance ; le modèle aléatoire justifie au contraire, sous indépendance et loi uniforme, pourquoi la cible choisie peut être atteinte par une extraction.

## 24. Prévoir un budget d’essais avant de lancer

**Sup → Spé · TP : extraction_aleatoire**

**Propriété ciblée.** La distance du meilleur point parmi m essais peut être étudiée exactement pour de petits rayons qui ne touchent pas les bords. Cela fournit une garantie probabiliste et non une certitude sur une réalisation particulière.

```text
Dₘ=min₁≤j≤m|Uⱼ−a|
P(Dₘ>ε)=(1−2ε/3)ᵐ, 0<ε≤min(a,3−a)
```

**Justification.** Dₘ>ε signifie que les m essais évitent tous l’intervalle ]a−ε,a+ε[. Les événements sont indépendants, d’où le produit des probabilités. Pour 0<α<1 et 2ε<3, imposer P(Dₘ≤ε)≥1−α demande m≥ln(α)/ln(1−2ε/3), arrondi à l’entier supérieur. Dans le cas a=3/2, ε=3/2, la probabilité par essai vaut 1 : un essai suffit presque sûrement, sans utiliser un logarithme de zéro. Si le voisinage déborde [0,3], sa longueur réelle d’intersection remplace 2ε.

## 25. Cauchy ne signifie convergent que dans un espace complet

**Sup → Spé · TP : cauchy_rationnels**

**Objets et but.** Une suite de Cauchy rapproche tous ses termes suffisamment tardifs entre eux, sans annoncer encore de point limite dans l’espace étudié. La suite rationnelle de Newton u₀=2, uₙ₊₁=uₙ/2+1/uₙ reste dans ℚ et tend vers √2 dans ℝ ; elle fournit le contre-exemple du recueil à la complétude de ℚ.

```text
Cauchy : ∀ε>0, ∃N, ∀m,n≥N, d(uₘ,uₙ)<ε
uₙ₊₁−√2=(uₙ−√2)²/(2uₙ)
```

**Démonstration.** Les uₙ sont rationnels positifs. L’identité affichée donne uₙ≥√2 ; de plus uₙ₊₁−uₙ=(2−uₙ²)/(2uₙ)≤0. La suite décroît et converge dans ℝ vers ℓ≥√2 ; passer à la limite dans la récurrence donne ℓ²=2. Toute suite convergente est de Cauchy par d(uₘ,uₙ)≤d(uₘ,ℓ)+d(uₙ,ℓ). Aucune limite rationnelle n’est possible, car une éventuelle limite dans ℚ serait également √2 dans ℝ, par unicité.

**Lire l’expérience.** Les étapes sont u₁=3/2, u₂=17/12, u₃=577/408. Si √2=p/q avec p,q premiers entre eux, p²=2q² impose p pair, puis q pair, contradiction : la limite n’est pas rationnelle. Le labo conserve les fractions exactes ; un affichage décimal fini ne peut prouver cette irrationalité ni l’égalité exacte à √2.

## 26. Fermés et sous-espaces complets

**Sup → Spé · TP : cauchy_rationnels**

**Propriété ciblée.** Toute partie complète d’un espace métrique est fermée dans cet espace. Dans un espace complet, toute partie fermée est complète. On doit conserver l’hypothèse de complétude de l’espace ambiant pour le second sens.

```text
A complet ⇒ A fermé dans E
E complet et A fermé ⇒ A complet
E complet ⇔ toute suite de Cauchy converge dans E
```

**Justification.** Si aₙ∈A tend dans E vers x, elle est de Cauchy ; la complétude de A donne une limite a∈A, et l’unicité impose x=a. Ainsi A est fermé. Réciproquement une suite de Cauchy de A converge dans E par complétude de E ; la fermeture de A place cette limite dans A. Un espace normé complet est appelé Banach.

## 27. Compact : toute suite possède une limite extraite dans l’ensemble

**Sup → Spé · TP : compacts_recouvrements**

**Objets et but.** En espace métrique, la compacité peut se définir par extraction de suites, ou par recouvrements ouverts : tout recouvrement ouvert admet un sous-recouvrement fini. Dans ℝᵈ et ℂᵈ, ces propriétés équivalent à « fermé et borné ». En dimension infinie, fermé et borné ne suffit plus.

```text
K compact ⇔ ∀(xₙ)∈K^ℕ, ∃φ strictement croissante, xφ(n)→x∈K
K⊂⋃ᵢUᵢ ⇒ K⊂Uᵢ₁∪…∪Uᵢₘ pour un nombre fini d’indices
```

**Démonstration.** Un compact métrique est borné : sinon choisir d(xₙ,a)>n, ce qui interdit toute sous-suite convergente. Il est fermé : pour une suite de K convergeant vers x, une extraction converge dans K et son unique limite est x. Dans ℝᵈ, réciproquement BW donne une limite extraite pour toute suite d’un fermé borné ; la fermeture garde cette limite dans K. L’équivalence avec les recouvrements ouverts est un théorème des espaces métriques, développé dans la leçon suivante.

**Lire l’expérience.** Dans le labo, les ouverts centrés aux j/m, j=0,…,m, couvrent [0,1] exactement lorsque r>1/(2m) : au seuil d’égalité, les milieux des mailles restent exclus. Les Uₙ=]−1,1−1/n[ recouvrent [0,1[ mais aucune réunion finie ne suffit. Une collection finie de points dessinés admet toujours un sous-recouvrement fini, même si l’ensemble infini étudié n’est pas compact.

## 28. Pourquoi les recouvrements détectent les suites

**Sup → Spé · TP : compacts_recouvrements**

**Propriété ciblée.** Dans un espace métrique, la compacité séquentielle implique la précompacité : pour tout ε>0, un nombre fini de boules de rayon ε couvre K. Elle permet ensuite de passer d’un recouvrement arbitraire à un sous-recouvrement fini.

```text
K compact ⇒ ∀ε>0, K couvert par un nombre fini de boules de rayon ε
Recouvrement ouvert de K ⇒ ∃δ>0 : chaque B_K(x,δ) est incluse dans un membre
```

**Justification.** Si aucune couverture finie par boules de rayon ε n’existe, choisir xₙ en dehors des boules centrées aux points précédents : les distances mutuelles sont ≥ε, donc aucune sous-suite ne converge. Pour le second fait, s’il échouait, choisir xₙ dont la boule de rayon 1/n n’est contenue dans aucun membre. Extraire xₙ→x ; un ouvert du recouvrement contenant x contient B_K(x,r). Pour n assez grand, B_K(xₙ,1/n)⊂B_K(x,r), contradiction. Une couverture finie par boules de rayon δ donne alors un sous-recouvrement fini.

## 29. Un compact transforme les infimums en minimums

**Sup → Spé · TP : valeurs_extremes**

**Objets et but.** Pour f:K→ℝ continue sur un compact non vide, les extrema existent et sont atteints. Trois hypothèses sont à vérifier séparément : K non vide, K compact, f continue. Un graphique sur un segment peut suggérer un extremum, mais une extrémité exclue ou une discontinuité change la conclusion.

```text
∃x₋,x₊∈K, ∀x∈K, f(x₋)≤f(x)≤f(x₊)
```

**Démonstration.** L’image continue d’un compact est compacte, donc f(K) est un fermé borné de ℝ. Son supremum M existe. Choisir yₙ∈f(K) avec M−1/n<yₙ≤M ; comme f(K) est fermé, M∈f(K). Il existe donc x₊ avec f(x₊)=M ; même argument pour le minimum. On peut aussi extraire une suite maximisante dans K puis utiliser la continuité.

**Lire l’expérience.** Le labo maximise ℓθ(x,y)=x cosθ+y sinθ sur x²/a²+y²/b²≤1, a,b>0. Poser x=au,y=bv et appliquer Cauchy–Schwarz donne M=√(a²cos²θ+b²sin²θ), atteint en (a²cosθ/M,b²sinθ/M). Sur le domaine strict <1, M reste le supremum mais n’est pas atteint ; multiplier le point extremal par 1−1/N construit une suite maximisante.

## 30. Coercivité et existence d’un minimiseur

**Sup → Spé · TP : valeurs_extremes**

**Propriété ciblée.** Une fonction continue f:ℝᵈ→ℝ est coercive si f(x)→+∞ lorsque ‖x‖→+∞. Elle possède alors un minimum global, même si le domaine n’est pas compact.

```text
∀M∈ℝ, ∃R>0, ‖x‖≥R ⇒ f(x)≥M
f coercive et continue ⇒ ∃x*, f(x*)=infℝᵈ f
```

**Justification.** Choisir M=f(0)+1 et un rayon R tel que hors de la boule de rayon R, f≥M. Sur la boule fermée, f atteint son minimum m≤f(0)<M. Ce minimiseur est global puisque toutes les valeurs extérieures sont plus grandes. En dimension infinie la boule fermée n’est pas forcément compacte, donc ce raisonnement ne se transfère pas tel quel.

## 31. Heine : un même rayon fonctionne partout sur un compact

**Sup → Spé · TP : heine_continuite**

**Objets et but.** La continuité en a autorise un rayon δ dépendant de a et de ε. La continuité uniforme choisit δ avant tous les couples x,y du domaine. Le théorème de Heine transforme la continuité en continuité uniforme sur un compact ; il ne transforme pas automatiquement une fonction en fonction lipschitzienne.

```text
Continue : ∀a∈A, ∀ε>0, ∃δ>0, ∀x∈A, d(x,a)<δ ⇒ d(f(x),f(a))<ε
Uniforme : ∀ε>0, ∃δ>0, ∀x,y∈A, d(x,y)<δ ⇒ d(f(x),f(y))<ε
```

**Démonstration.** Supposons f continue sur K compact mais non uniformément continue. Il existe ε₀>0 et des couples xₙ,yₙ∈K avec d(xₙ,yₙ)<1/n et d(f(xₙ),f(yₙ))≥ε₀. Extraire xₙ→a dans K ; alors yₙ→a par l’inégalité triangulaire. La continuité donne f(xₙ)→f(a), f(yₙ)→f(a), contradiction. L’extraction est l’endroit exact où la compacité intervient.

**Lire l’expérience.** Le labo choisit f(x)=sin(x²), 2R-lipschitzienne sur [−R,R] car |f′|≤2R. Sur ℝ, les points xₙ=√(2πn) et yₙ=√(2πn+π/2) vérifient yₙ−xₙ=(π/2)/(xₙ+yₙ)→0, mais leurs images valent 0 et 1. La fonction n’est donc pas uniformément continue sur ℝ. La fenêtre d’affichage bornée ne doit pas remplacer le domaine analytique tout entier.

## 32. Lipschitz, Hölder et domaine non compact

**Sup → Spé · TP : heine_continuite**

**Propriété ciblée.** Une application L-lipschitzienne est uniformément continue. Une borne de type Hölder |f(x)−f(y)|≤C|x−y|ᵅ avec α>0 suffit également. La compacité est une condition suffisante de Heine, pas nécessaire à toute continuité uniforme.

```text
√x sur [0,+∞[ : |√x−√y|≤√|x−y|
Pour ε>0, δ=ε² convient
```

**Justification.** Si x≥y≥0, (√x−√y)²=x+y−2√xy≤x−y, car y≤√xy. La borne est symétrique et donne la continuité uniforme sur un domaine non compact. Pourtant √x n’est pas lipschitzienne près de zéro : |√x−0|/|x−0|=1/√x est non borné. On sépare ainsi trois notions que le dessin seul peut confondre.

## 33. Exercice 6 : produit compact, puis image compacte

**Spé · TP : image_compacte**

**Objets et but.** A et B sont des compacts métriques, f:A×B→F est continue. Le produit est muni, par exemple, de d((a,b),(a′,b′))=max(d_A(a,a′),d_B(b,b′)). On veut prouver que f(A×B) est compact. Le choix des indices est crucial : deux extractions indépendantes ne s’assemblent pas automatiquement.

```text
A,B compacts ⇒ A×B compact
f continue ⇒ f(A×B) compact
```

**Démonstration.** Pour une suite (aₙ,bₙ), extraire aφ(n)→a∈A. De la suite bφ(n), extraire à nouveau bφ(ψ(n))→b∈B. Les aφ(ψ(n)) convergent encore vers a ; le couple extrait converge donc vers (a,b). Pour une suite zₙ∈f(A×B), choisir un antécédent (aₙ,bₙ) de chaque zₙ ; extraire ces couples et utiliser la continuité. Cette preuve fonctionne pour un nombre fini de facteurs.

**Lire l’expérience.** L’addition envoie A×B sur la somme de Minkowski A+B. Le labo ajoute une ellipse pleine de demi-axes a,b à un segment [−sv,sv], v=(cosθ,sinθ). Pour w=(cosφ,sinφ), le maximum de ⟨w,z⟩ sur la somme vaut √(a²cos²φ+b²sin²φ)+s|cos(φ−θ)|. Cette fonction d’appui donne des extrema exacts sans mailler toutes les paires du produit.

## 34. Deux compacts disjoints sont séparés par une distance positive

**Spé · TP : image_compacte**

**Propriété ciblée.** Pour A,B compacts non vides et disjoints d’un espace métrique, la distance minimale entre les deux ensembles est strictement positive. « Fermés disjoints » seul ne suffit pas.

```text
dist(A,B)=min_{a∈A,b∈B}d(a,b)>0
```

**Justification.** La fonction (a,b)↦d(a,b) est continue et atteint un minimum m sur le compact A×B. Si m=0, les points minimisants a et b seraient égaux, contradiction à A∩B=∅. Pour deux fermés non compacts de ℝ², A={(x,0):x∈ℝ}, B={(x,eˣ):x∈ℝ}, les ensembles sont disjoints mais leur distance est zéro, car eˣ→0 quand x→−∞.

## 35. Une application linéaire est continue si elle possède une borne uniforme

**Spé · TP : applications_lineaires**

**Objets et but.** Pour u:E→F linéaire entre espaces normés, la continuité en zéro suffit à la continuité partout. Elle équivaut à l’existence d’un C≥0 vérifiant ‖u(x)‖≤C‖x‖ pour tous les vecteurs. En dimension finie au départ, cette borne existe toujours ; en dimension infinie elle doit être prouvée.

```text
u continue ⇔ u continue en 0 ⇔ ∃C≥0, ∀x∈E, ‖u(x)‖≤C‖x‖
‖u‖op=sup_{‖x‖≤1}‖u(x)‖
```

**Démonstration.** La continuité en zéro avec ε=1 donne δ>0 tel que ‖z‖<δ ⇒ ‖u(z)‖<1. Pour x≠0, appliquer ceci à z=δx/(2‖x‖) donne ‖u(x)‖≤(2/δ)‖x‖. Réciproquement la borne entraîne ‖u(x)−u(y)‖≤C‖x−y‖, donc u est lipschitzienne. Dans une base finie, u(x)=Σxᵢu(eᵢ), et l’inégalité triangulaire avec l’équivalence des normes fournit C.

**Lire l’expérience.** Pour les matrices réelles denses de dimension 4 à 8 du labo, la norme euclidienne d’opérateur vaut la plus grande valeur singulière. Le laboratoire compare cette borne exacte aux gains de directions testées. Un nombre fini de directions ne donne pas à lui seul le supremum ; la décomposition en valeurs singulières le certifie.

## 36. Une application linéaire non continue en dimension infinie

**Spé · TP : applications_lineaires**

**Propriété ciblée.** Sur l’espace des polynômes réels muni de la norme uniforme sur [0,1], l’application u(P)=P′(1) est linéaire mais non continue. Les dérivées peuvent amplifier fortement une petite fonction.

```text
Pₙ(x)=xⁿ/n : ‖Pₙ‖∞=1/n→0, u(Pₙ)=1
‖u∘v‖op≤‖u‖op‖v‖op pour u,v continus
```

**Justification.** Si u était continue, Pₙ→0 impliquerait u(Pₙ)→0, contradiction. Pour la composition, appliquer ‖u(v(x))‖≤‖u‖op‖v(x)‖≤‖u‖op‖v‖op‖x‖ et prendre le supremum sur la boule unité. La présence de polynômes de degrés arbitraires est précisément ce qui empêche de traiter le premier espace comme un espace de dimension fixe.

## 37. En dimension infinie, le choix de norme change les convergences

**Spé → au-delà · TP : normes_dimension_infinie**

**Objets et but.** Sur C([0,1],ℝ), on compare ‖f‖∞=max|f|, ‖f‖₁=∫|f| et ‖f‖₂=√∫|f|². Ces expressions sont des normes sur les fonctions continues : une intégrale nulle impose f=0 par continuité. Elles ne sont pas toutes équivalentes ; un pic peut être haut mais étroit.

```text
‖f‖₁≤‖f‖₂≤‖f‖∞
fₙ(x)=xⁿ : ‖fₙ‖∞=1, ‖fₙ‖₁=1/(n+1), ‖fₙ‖₂=1/√(2n+1)
```

**Démonstration.** La première inégalité résulte de Cauchy–Schwarz sur un intervalle de longueur 1 ; la seconde de |f|≤‖f‖∞. Si les normes 1 et ∞ étaient équivalentes, il existerait C indépendant de f avec ‖f‖∞≤C‖f‖₁. Pour fₙ=xⁿ, cela donnerait 1≤C/(n+1), impossible. Ainsi fₙ→0 pour les normes intégrales mais pas pour la norme uniforme.

**Lire l’expérience.** Les graphiques présentent des pics dont l’aire décroît tandis que la hauteur reste constante. Les normes exactes sont calculées avant toute quadrature ; un maillage incapable de résoudre le pic n’a pas le droit d’en déduire une norme nulle. Chaque sous-espace de polynômes de degré ≤d possède cependant des normes équivalentes, avec des constantes dépendant de d.

## 38. Complétude et complétion dépendent aussi de la norme

**Spé → au-delà · TP : normes_dimension_infinie**

**Propriété ciblée.** C([0,1]) muni de la norme uniforme est complet. Avec une norme intégrale, des suites de fonctions continues peuvent approcher une fonction discontinue dans l’espace complété L¹ ou L². La topologie et la complétude doivent donc être distinguées.

```text
Uniformément Cauchy dans C([0,1]) ⇒ limite continue uniforme
Convergence L¹ ne garantit pas une limite continue
```

**Justification.** Une suite uniformément de Cauchy converge point par point par complétude de ℝ. Passer à la limite dans la borne uniforme de Cauchy donne la convergence uniforme vers f. Pour prouver la continuité de f en a, majorer |f(x)−f(a)| par deux erreurs uniformes et |fₙ(x)−fₙ(a)| pour un n fixé. Des rampes continues de largeur 1/n autour de 1/2 approchent au contraire une marche dans L¹ : aucune limite continue ne représente cette marche presque partout.

## 39. Exercice 9 : une infinité de modes séparés dans la boule unité

**Spé · TP : boule_non_compacte**

**Objets et but.** E=C([0,2π],ℂ) est muni de la norme ‖f‖₂=(∫|f|²)¹ᐟ². Les modes eₙ(t)=e^(int)/√(2π) sont continus et de norme 1. Deux modes distincts restent à distance √2, quelle que soit leur fréquence : une extraction ne peut les rapprocher.

```text
⟨eₚ,e_q⟩=δpq ; ‖eₙ‖₂=1
p≠q ⇒ ‖eₚ−e_q‖₂²=2
```

**Démonstration.** Pour p≠q, ∫₀²πe^(i(p−q)t)dt=[e^(i(p−q)t)/(i(p−q))]₀²π=0. Chaque norme carrée vaut 1 ; développer le carré de la différence donne 1+1−2Re0=2. Toute extraction de modes garde des indices distincts et une distance √2 entre deux termes différents ; elle n’est pas de Cauchy, donc ne converge pas. La boule unité fermée est fermée et bornée mais non compacte : c’est un contre-exemple en dimension infinie.

**Lire l’expérience.** Le recueil utilise les modes non normalisés uₙ=e^(int), de norme √(2π), et leur distance 2√π. Le passage à eₙ change les valeurs en 1 et √2. Le maillage peut faire apparaître des modes identiques par aliasing ; l’orthogonalité et les distances affichées doivent reposer sur leurs intégrales exactes.

## 40. Fermé borné, complet et compact : trois questions

**Spé · TP : boule_non_compacte**

**Propriété ciblée.** Dans un espace métrique, tout compact est complet et précompact. Une boule en dimension infinie peut manquer de précompacité, même si l’espace ambiant est complet. Le théorème de Riesz caractérise les espaces normés de dimension finie par la compacité de leur boule unité.

```text
E normé sur ℝ ou ℂ : boule unité fermée compacte ⇔ dim E<∞
Compact métrique ⇔ complet et précompact
```

**Justification.** Un compact est précompact par le raisonnement des points ε-séparés et complet, car une suite de Cauchy possède une extraction convergente qui entraîne la convergence de la suite entière. Pour des modes séparés de √2, des boules de rayon r<√2/2 ne peuvent chacune contenir deux modes ; aucune couverture finie ne suffit. Ce défaut persiste dans l’espace de Hilbert complet L²([0,2π]), qui contient les mêmes modes.

## 41. Infini dénombrable : énumérer sans perdre ni répéter

**Sup · TP : denombrer_rationnels**

**Objets et but.** Un ensemble est fini s’il possède un cardinal entier ; il est infini sinon. Un ensemble infini est dénombrable s’il existe une bijection avec ℕ. ℤ, ℕ² et ℚ sont dénombrables, malgré leur apparence très différente. Pour ℚ, représenter chaque nombre sous forme p/q, avec q>0 et pgcd(|p|,q)=1, évite les répétitions.

```text
ℚ={p/q : p∈ℤ, q∈ℕ*, pgcd(|p|,q)=1}
Parcours par hauteurs h=|p|+q ; chaque étage est fini
```

**Démonstration.** Pour chaque h≥1, il n’existe qu’un nombre fini de couples avec |p|+q=h. Tous les rationnels possèdent un représentant réduit unique et apparaissent à un étage fini. Ranger les étages dans l’ordre, puis les p dans chaque étage, fournit une liste sans répétition couvrant ℚ. L’infinitude est assurée par l’injection n↦n ; la liste devient donc une bijection avec ℕ. Pour ℕ², le parcours par diagonales n+m constante donne le même mécanisme.

**Lire l’expérience.** Le panneau de fractions trace seulement les étages jusqu’à une hauteur H. Leur nombre fini est un extrait de l’énumération infinie. La densité de ℚ est une autre propriété : elle parle des voisinages dans ℝ et ne découle pas de la seule énumération.

## 42. Une réunion dénombrable d’ensembles dénombrables

**Sup · TP : denombrer_rationnels**

**Propriété ciblée.** Si Aₖ est dénombrable pour chaque k∈ℕ, les éléments se rangent dans un tableau double (k,n). Un parcours diagonal couvre leur union ; on supprime les répétitions éventuelles. Ce mécanisme relie produits et unions dénombrables.

```text
ℕ×ℕ dénombrable ; ⋃k∈ℕAₖ au plus dénombrable
Un sous-ensemble d’un dénombrable est au plus dénombrable
```

**Justification.** Une énumération de Aₖ fournit une surjection de ℕ² sur l’union. Composer avec l’énumération diagonale donne une liste ; conserver uniquement la première occurrence de chaque élément donne une injection dans ℕ et, si l’union est infinie, une bijection avec ℕ. Pour un sous-ensemble B⊂ℕ infini, choisir successivement son plus petit élément non encore choisi énumère B.

## 43. La diagonale de Cantor interdit toute liste complète

**Sup → Spé · TP : diagonale_cantor**

**Objets et but.** Supposer que toutes les suites binaires aient été rangées en lignes s₀,s₁,…, chaque sₙ étant une suite infinie de zéros et uns. La suite d dont le n-ième chiffre est opposé au n-ième chiffre de la n-ième ligne échappe à toutes les lignes. La fenêtre finie illustre ce mécanisme mais n’est pas l’objet du théorème.

```text
dₙ=1−sₙ(n) ; ∀n, d≠sₙ
{0,1}^ℕ n’est pas dénombrable
```

**Démonstration.** Pour chaque n, d diffère de sₙ au moins à la coordonnée n. Si la liste était surjective, d serait égale à une ligne sₖ, mais leur k-ième chiffre est différent, contradiction. Ce raisonnement ne choisit pas « un rang après le dernier » : il change un chiffre de chaque ligne dans une liste infinie. Un tableau N×N ne réfute qu’une liste finie de N mots et ne démontre pas à lui seul la non-dénombrabilité.

**Lire l’expérience.** Pour relier le tableau à des réels sans ambiguïté d’écriture binaire, encoder les suites dans des chiffres ternaires 0 et 2 : x(s)=Σ₂sₙ/3ⁿ⁺¹. Si deux suites diffèrent au premier rang k, l’écart initial vaut 2/3ᵏ⁺¹ et la queue peut compenser au plus 1/3ᵏ⁺¹ ; l’écart total reste positif.

## 44. Cantor : aucun ensemble n’énumère toutes ses parties

**Sup → Spé · TP : diagonale_cantor**

**Propriété ciblée.** Pour toute application f:E→P(E), la partie D={x∈E : x∉f(x)} n’appartient pas à son image. Cette version formule la diagonale sans chiffres et montre |P(E)|>|E| au sens des injections et surjections.

```text
D={x∈E : x∉f(x)}
Si D=f(a), alors a∈D ⇔ a∉D : contradiction
```

**Justification.** L’équivalence provient directement de la définition de D. Une injection E→P(E) est donnée par x↦{x}, tandis qu’aucune surjection E→P(E) n’existe par le raisonnement diagonal. En prenant E=ℕ, les parties de ℕ s’identifient à leurs indicatrices binaires, ce qui retrouve le résultat de la première leçon.

## 45. Le compact de Cantor : énormément de points, aucun intervalle

**Sup → Spé · TP : ensemble_cantor**

**Objets et but.** On part de C₀=[0,1] et enlève le tiers ouvert central de chaque intervalle à chaque étape. Cₙ est la réunion de 2ⁿ intervalles fermés de longueur 3⁻ⁿ. Le compact limite C=⋂Cₙ est non dénombrable, d’intérieur vide et totalement discontinu : ses composantes connexes sont des singletons.

```text
C=⋂n≥0Cₙ ; longueur totale de Cₙ=(2/3)ⁿ
C={Σn≥0 2sₙ/3ⁿ⁺¹ : sₙ∈{0,1}}
```

**Démonstration.** Chaque Cₙ est fermé dans [0,1], donc l’intersection est un fermé borné de ℝ, compact et non vide (elle contient 0 et 1). L’encodage ternaire injectif de toutes les suites binaires prouve la non-dénombrabilité. Aucun intervalle non trivial ne reste dans C : si sa longueur est >3⁻ⁿ, il ne peut être inclus dans un seul intervalle de Cₙ et rencontre un trou. Un connexe de ℝ étant un intervalle, les connexes contenus dans C se réduisent à un point.

**Lire l’expérience.** La longueur totale affichée tend vers zéro, alors que le cardinal reste celui du continu. La longueur et le cardinal mesurent donc deux phénomènes différents. Le dessin de Cₙ, qui contient encore des intervalles, n’a pas la même connexité que la limite C.

## 46. Un compact sans points isolés

**Sup → Spé · TP : ensemble_cantor**

**Propriété ciblée.** C est parfait : il est fermé et chacun de ses points est limite de points distincts de C. La propriété s’établit en modifiant un chiffre ternaire arbitrairement tardif.

```text
∀x∈C, ∀ε>0, ∃y∈C, 0<|x−y|<ε
```

**Justification.** Coder x par une suite de chiffres 0 et 2. Changer uniquement le chiffre de rang n donne un autre point yₙ∈C, distinct, à distance 2/3ⁿ⁺¹. Pour n assez grand, cette distance est <ε. Ainsi aucune extrémité de la construction, pas même zéro ou un, n’est isolée. Fermeture et absence de points isolés définissent ici un ensemble parfait.

## 47. Densité et cardinalité répondent à deux questions différentes

**Sup → Spé · TP : rationnels_irrationnels**

**Objets et but.** Dans ℝ, ℚ et ℝ∖ℚ sont tous deux denses. Pourtant ℚ est dénombrable et l’ensemble des irrationnels ne l’est pas. La densité signifie que tout voisinage rencontre l’ensemble ; elle ne donne aucun nombre de points ni aucune appartenance d’un point limite.

```text
qₙ=⌊10ⁿx⌋/10ⁿ : 0≤x−qₙ<10⁻ⁿ
rₙ=qₙ+√2/10ⁿ : rₙ∉ℚ et rₙ→x
```

**Démonstration.** qₙ est rationnel et converge vers x. rₙ est irrationnel, car ajouter à un rationnel le multiple rationnel non nul d’un irrationnel reste irrationnel ; son écart à x est au plus (1+√2)10⁻ⁿ. Tout réel est ainsi limite de suites appartenant à chacun des deux ensembles. Si les irrationnels étaient dénombrables, leur union avec ℚ rendrait ℝ dénombrable, contradiction à Cantor.

**Lire l’expérience.** L’intérieur de chacun des deux ensembles est vide et leur adhérence est ℝ ; leur frontière est donc ℝ. Une visualisation finie peut montrer deux familles d’approximants, mais elle ne peut représenter tous les points rationnels ou irrationnels d’un intervalle.

## 48. La fonction de Dirichlet et les limites sur un dense

**Sup → Spé · TP : rationnels_irrationnels**

**Propriété ciblée.** La fonction 𝟙_ℚ vaut 1 sur les rationnels et 0 sur les irrationnels ; elle est discontinue partout. Deux fonctions continues égales sur un dense sont, en revanche, égales partout. La continuité est l’hypothèse qui fait passer de valeurs denses à toutes les valeurs.

```text
f,g continues sur E et f=g sur D dense ⇒ f=g sur E
```

**Justification.** Pour a∈E métrique, choisir dₙ∈D avec dₙ→a. La continuité donne f(a)=lim f(dₙ)=lim g(dₙ)=g(a). Pour 𝟙_ℚ, les suites qₙ et rₙ ci-dessus approchent tout a mais leurs images valent constamment 1 et 0 ; une même limite ne peut être obtenue. L’appartenance de a à ℚ ne change pas cette contradiction.

## 49. Connexe ne signifie pas toujours connexe par arcs

**Spé → au-delà · TP : sinus_topologue**

**Objets et but.** Le sinus du topologue est S=G∪V, où G={(x,sin(1/x)):0<x≤1} et V={0}×[−1,1]. G est connexe par arcs ; son adhérence ajoute toute la verticale V. Le nouvel ensemble S est compact et connexe, mais n’est pas connexe par arcs.

```text
S=Ḡ ; G connexe ⇒ Ḡ connexe
Aucune trajectoire continue dans S ne relie V à G
```

**Démonstration.** L’image continue de ]0,1] par x↦(x,sin(1/x)) est connexe. Pour y∈[−1,1], choisir θ avec sinθ=y et xₙ=1/(θ+2πn)>0 pour n assez grand ; les points de G tendent vers (0,y). Aucune autre limite n’apparaît, donc S=Ḡ. L’adhérence d’un connexe est connexe : une séparation relative de l’adhérence imposerait une séparation de G, et un côté ouvert non vide doit rencontrer G par densité. S est fermé borné, donc compact.

**Lire l’expérience.** Le tracé ne représente que x≥δ>0, plus la verticale limite dessinée séparément. Cette union finie visible peut paraître disjointe : elle n’est pas l’ensemble infini S. La preuve de connexité vient de l’adhérence ; la preuve de l’absence de chemin utilise toutes les oscillations arbitrairement proches de zéro.

## 50. Pourquoi aucun chemin ne peut quitter la verticale

**Spé → au-delà · TP : sinus_topologue**

**Propriété ciblée.** Supposons γ(t)=(x(t),y(t)) continue dans S, avec un point sur V et plus tard x(t)>0. Sur une composante ]a,b[ de {t:x(t)>0}, le rayon x tend vers zéro à l’extrémité a ; cela impose une oscillation de y incompatible avec sa continuité.

```text
Sur x(t)>0 : y(t)=sin(1/x(t))
x(a)=0 ⇒ des temps t→a imposent y(t)=1 et y(t)=−1
```

**Justification.** Fixer un t₀ de cette composante avec x(t₀)>0. Pour tout voisinage temporel ]a,a+η[, prendre un t₁ dedans avec x(t₁)>0. Par continuité et x(a)=0, x([a,t₁]) contient [0,x(t₁)]. Les valeurs 1/(π/2+2πn) et 1/(3π/2+2πn) y appartiennent pour n assez grand, donc des temps dans [a,t₁] donnent y=1 et y=−1. En faisant η→0, ces deux valeurs empêchent l’existence d’une limite de y en a. La contradiction exclut tout chemin entre V et G.

## 51. Le signe du déterminant sépare les matrices réelles inversibles

**Spé · TP : gl_composantes**

**Objets et but.** On identifie M₄(ℝ) à ℝ¹⁶ avec la norme de Frobenius. GL₄(ℝ)={A:det A≠0} est ouvert, dense et non borné. Les ensembles det>0 et det<0 constituent ses deux composantes connexes par arcs. SL₄(ℝ)={A:det A=1} est un sous-groupe différent de l’ensemble det>0.

```text
GLₙ⁺(ℝ)={A:det A>0}, GLₙ⁻(ℝ)={A:det A<0}
SLₙ(ℝ)={A:det A=1} ; SLₙ(ℝ)⊂GLₙ⁺(ℝ)
```

**Démonstration.** Le déterminant est polynomial continu, donc GL est l’image réciproque de ℝ∖{0}, ouverte. Pour toute A, le polynôme t↦det(A+tI) possède un coefficient dominant 1 et seulement un nombre fini de racines ; il existe des t arbitrairement petits avec A+tI inversible, d’où la densité. Sur un chemin inversible réel, le déterminant reste non nul ; le TVI interdit de changer de signe. Chaque signe est connexe par arcs par décomposition polaire A=QP : faire varier P positif vers I, puis Q dans SO(n), ou dans sa composante de réflexion.

**Lire l’expérience.** La famille A(t)=Q diag(t,1,2,3) R, Q,R orthogonales denses de déterminant 1, a det A=6t et devient singulière en t=0. Sur ℂ, le chemin Q diag(e^(iθ),1,2,3) R relie ses extrémités sans annuler le déterminant : le détour complexe n’existe pas dans GL₄(ℝ).

## 52. GLₙ(ℂ) est connexe par arcs, contrairement au cas réel

**Spé · TP : gl_composantes**

**Propriété ciblée.** Les valeurs complexes non nulles contournent zéro. Une réduction polaire sépare les étirements positifs d’une matrice unitaire ; les phases des valeurs propres de cette dernière fournissent un chemin.

```text
A=UP, P hermitienne positive définie
P_t=(1−t)P+tI ; U_t=V diag(e^(i(1−t)θⱼ))V*
```

**Justification.** P_t reste positive définie car z*P_tz est strictement positif pour z≠0. Écrire U=V diag(e^(iθⱼ))V* par le théorème spectral unitaire donne un chemin U_t de U vers I. La concaténation relie A à U puis à I dans GLₙ(ℂ). Les phases sont choisies pour les valeurs propres de la matrice considérée ; il n’est pas nécessaire de choisir une phase globale continue pour toutes les matrices simultanément.

## 53. Un groupe matriciel compact et un groupe fermé non borné

**Spé · TP : orthogonal_compact**

**Objets et but.** O(4)={Q:QᵀQ=I} conserve les longueurs euclidiennes. Chaque matrice orthogonale possède des colonnes unitaires orthogonales et ‖Q‖F=2. Le groupe SL₄(ℝ) est lui aussi fermé, mais peut étirer une direction tout en comprimant une autre : le déterminant ne contrôle pas la taille.

```text
O(n) fermé et ‖Q‖F=√n ⇒ O(n) compact
D_t=diag(eᵗ,e⁻ᵗ,1,1)∈SL₄(ℝ), ‖D_t‖F²=e²ᵗ+e⁻²ᵗ+2
```

**Démonstration.** L’application Q↦QᵀQ est continue ; O(n) est son image réciproque du singleton I, donc fermé. Les coefficients des colonnes sont bornés et la norme de Frobenius est √n : en dimension finie, O(n) est compact. SL est le fermé det⁻¹({1}), mais D_t montre qu’il est non borné, donc non compact. Les deux arguments utilisent des propriétés distinctes : une équation continue produit la fermeture, une estimation produit la bornitude.

**Lire l’expérience.** Le laboratoire multiplie des rotations dans deux plans de ℝ⁴, ou une réflexion, à gauche par Q et à droite par R, deux matrices orthogonales denses de déterminant 1. Ces isométries rendent les matrices pleinement 4×4 sans changer leurs valeurs singulières. La projection 2D d’un objet de ℝ⁴ peut masquer certaines distances ; les métriques proviennent des quatre coordonnées.

## 54. SO(n), orientations et chemins de rotations

**Spé · TP : orthogonal_compact**

**Propriété ciblée.** Une matrice orthogonale réelle a un déterminant ±1. O(n) possède deux composantes, tandis que SO(n)={Q∈O(n):det Q=1} est connexe par arcs. Dans ℝ⁴ une rotation n’est pas nécessairement décrite par un unique angle.

```text
QᵀQ=I ⇒ (det Q)²=1
Q∈SO(n) se réduit orthogonalement en blocs de rotations et blocs 1
```

**Justification.** Prendre le déterminant de QᵀQ=I donne le signe ±1. Une forme canonique réelle orthogonale décompose Q en rotations planes et en ±1 ; les −1 sont en nombre pair lorsque det Q=1 et se regroupent en rotations d’angle π. Ramener continûment tous les angles à zéro relie Q à I dans SO(n). Une réflexion fixe transforme cette composante en celle de déterminant −1. Le signe ne peut varier sur un chemin orthogonal par continuité.

## 55. Une contraction transforme la complétude en convergence garantie

**Spé → au-delà · TP : point_fixe**

**Objets et but.** Sur un espace métrique complet non vide X, une application T:X→X q-lipschitzienne avec 0≤q<1 possède un unique point fixe. À partir de x₀, les itérations xₙ₊₁=T(xₙ) convergent vers ce point. La stabilité du domaine T(X)⊂X et la complétude doivent être contrôlées avant l’itération.

```text
d(Tx,Ty)≤q d(x,y), 0≤q<1
d(xₙ,x*)≤qⁿd(x₁,x₀)/(1−q)
```

**Démonstration.** Par récurrence d(xₙ₊₁,xₙ)≤qⁿd(x₁,x₀). La somme géométrique borne d(xₘ,xₙ) par qⁿd(x₁,x₀)/(1−q), donc la suite est de Cauchy. La complétude donne une limite x*. T est continue, d’où T(x*)=x*. Si a et b étaient fixes, d(a,b)≤q d(a,b), donc a=b. Faire m→∞ dans la borne de Cauchy produit l’estimation d’erreur affichée.

**Lire l’expérience.** T(x)=cos x envoie [0,1] dans [cos1,1]⊂[0,1] et possède q=sin1<1 par l’inégalité des accroissements finis. Pour T(x)=ax+b sur ℝ, le taux est |a| : un point fixe peut exister même si l’itération n’est pas contractante, mais la garantie de Banach disparaît.

## 56. Existence du point fixe et convergence de l’itération se séparent

**Spé → au-delà · TP : point_fixe**

**Propriété ciblée.** Pour l’application affine T(x)=ax+b, si a≠1 le point fixe vaut b/(1−a), mais son attractivité dépend de |a|. Si a=1, il peut n’y avoir aucun point fixe ou en exister une infinité.

```text
xₙ−x*=aⁿ(x₀−x*) si a≠1
a=1,b≠0 : aucun fixe ; a=1,b=0 : tous les points fixes
```

**Justification.** Soustraire l’identité x*=ax*+b de la récurrence donne le facteur a à chaque étape. Pour |a|<1, l’erreur tend vers zéro ; pour |a|>1 elle grandit sauf départ exactement au point fixe. Pour a=−1 elle alterne sans décroître sauf ce départ. Ainsi résoudre algébriquement T(x)=x ne prouve pas la convergence de l’algorithme proposé.

## 57. Un niveau continu change la géométrie des composantes

**Spé · TP : chemins_niveaux**

**Objets et but.** La fonction F_a(x,y)=((x−a)²+y²)((x+a)²+y²), avec a>0, est le produit des carrés des distances aux foyers (±a,0). Les sous-niveaux fermés C_{a,b}={F_a≤b⁴}, b>0, illustrent le passage de deux lobes séparés à un ensemble connexe. Un sous-niveau fermé n’a pas la même connexité que le sous-niveau strict au niveau critique.

```text
C_{a,b}=F_a⁻¹(]−∞,b⁴]) fermé
b<a : deux composantes ; b=a : lobes joints en 0 ; b>a : une composante
```

**Démonstration.** F_a est continue et coercive de degré quatre, donc chaque sous-niveau est fermé borné, compact. Sur la médiatrice x=0, F_a(0,y)=(a²+y²)²≥a⁴. Si b<a, aucun point de C ne touche x=0 : les deux signes de x séparent les lobes. En coordonnées polaires, F_a=r⁴−2a²r²cos2θ+a⁴ ; pour b≥a, chaque direction admise contient un intervalle radial commençant à zéro. Le sous-niveau fermé est étoilé de centre zéro et donc connexe par arcs. Pour b=a, les deux lobes ne se rejoignent qu’en zéro.

**Lire l’expérience.** Le contour est une courbe de Cassini. Pour b<a, écrire z=x+iy : F_a=|z²−a²|². Le disque fermé |w−a²|≤b² reste dans Re w>0 ; sa racine carrée continue de partie réelle positive décrit exactement le lobe x>0, et son opposé le lobe x<0. Chaque lobe est donc connexe par arcs, et il y a exactement deux composantes. Le maillage peut créer un faux pont ; les inégalités exactes et le statut ouvert ou fermé décident de la classification.

## 58. Images réciproques et valeurs intermédiaires

**Spé · TP : chemins_niveaux**

**Propriété ciblée.** Pour une fonction continue f, l’image réciproque d’un ouvert est ouverte et celle d’un fermé est fermée. L’image continue d’un connexe est connexe. Ces deux principes expliquent la nature des sous-niveaux et les obstacles à un chemin.

```text
f continue ⇒ {f<c} ouvert, {f≤c} fermé
γ chemin ⇒ f∘γ satisfait le TVI
```

**Justification.** Si f(x)<c, la continuité préserve cette stricte marge dans une boule autour de x, d’où l’ouverture. La fermeture du sous-niveau large découle du complémentaire {f>c}. Si un chemin reliait un point d’abscisse négative à un point d’abscisse positive dans C_{a,b} pour b<a, sa coordonnée x passerait par zéro par TVI, mais aucun point de ce sous-niveau n’a x=0. Le TVI fournit ici un certificat d’impossibilité.

## 59. Une bijection continue peut avoir un inverse discontinu

**Spé · TP : homeomorphisme**

**Objets et but.** Un homéomorphisme f:X→Y est une bijection continue dont l’inverse est continu. Il conserve les ouverts relatifs, compacts, connexes et convergences. Une bijection continue seule ne suffit pas : l’enroulement f:[0,2π[→S¹, t↦(cos t,sin t), possède un inverse discontinu au point (1,0).

```text
tₙ=2π−1/n : f(tₙ)→f(0), mais tₙ ne tend pas vers 0
Bijection continue ≠ nécessairement homéomorphisme
```

**Démonstration.** L’enroulement est continu et bijectif sur l’intervalle semi-ouvert, car chaque angle possède un représentant unique dans [0,2π[. Les images de tₙ convergent vers (1,0), mais leurs antécédents restent proches de 2π, et non de zéro. La caractérisation séquentielle de la continuité montre donc que f⁻¹ est discontinue à (1,0). Le défaut vient du raccord des deux bouts du cercle sans raccord correspondant dans le domaine.

**Lire l’expérience.** Le plongement g(t)=(t,t²,t³), t∈[−1,1], a un inverse égal à la projection sur la première coordonnée, donc est un homéomorphisme vers son image. La courbe est tracée avec une projection graphique, mais les trois coordonnées définissent l’application étudiée.

## 60. Un compact répare l’inverse d’une injection continue

**Spé · TP : homeomorphisme**

**Propriété ciblée.** Si K est compact et F est métrique, une application continue injective f:K→F est un homéomorphisme de K sur f(K). Ce théorème du recueil fournit la continuité de l’inverse sans calcul explicite.

```text
K compact, f continue injective ⇒ f:K→f(K) homéomorphisme
```

**Justification.** La bijectivité sur l’image est automatique. Tout fermé A de K est compact ; son image f(A) est compacte, donc fermée dans F et dans f(K). Pour g=f⁻¹, g⁻¹(A)=f(A) est donc fermé pour chaque fermé A de K : g est continue. L’argument utilise le fait qu’un compact est fermé dans un espace métrique, plus généralement Hausdorff. L’intervalle [0,2π[ du contre-exemple n’est pas compact.

## Sources

Point de départ : recueil fourni par l’utilisateur, fiche M1 « Topologie et ensembles », pages imprimées 12–25. Définitions p.15–16, TP de suite extraite aléatoire p.17, propriétés p.19–21, infographie essentielle p.22, exercices 6–9 p.23 et corrigés p.25. Les expériences, cours et problèmes de cet atelier sont nouvellement rédigés. Le PDF, ses scans et ses figures ne sont pas redistribués.

[MIT OpenCourseWare, Paige Bright, Introduction to Metric Spaces](https://ocw.mit.edu/courses/18-s190-introduction-to-metric-spaces-january-iap-2023/pages/lecture-notes/) : compléments sur les espaces métriques, les recouvrements et la complétude.

[Jiří Lebl, Basic Analysis, Completeness and compactness](https://www.jirka.org/ra/html/sec_metcompact.html) : compléments universitaires sur la compacité en espaces métriques ; [Continuous functions](https://www.jirka.org/ra/html/sec_metcont.html) : continuité, images compactes et topologie.
