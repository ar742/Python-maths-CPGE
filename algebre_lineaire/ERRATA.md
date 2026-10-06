# Conventions et corrections pour l'atelier d'algèbre

Source : extrait personnel **MemoCPGEScientifAR2027-Alg-AlgLin.pdf**, 32 pages, numérotation imprimée **124–155**. Les lignes ci-dessous indiquent des corrections locales et des hypothèses à conserver lorsqu'on exploite ses TP. Elles servent à rendre les expériences et les démonstrations cohérentes ; elles ne remplacent pas le recueil. Le PDF personnel et ses images ne sont pas redistribués avec l'atelier.

## Corrections qui changent un résultat

| Pages du PDF / imprimées | Point à préciser ou corriger | Formulation retenue et contrôle |
|---|---|---|
| 1 / 124 | Un idéal ne doit pas être exclu parce qu'il est nul. | {0} est un idéal. Dans l'atelier, « anneau principal » signifie anneau intègre dont tous les idéaux sont principaux ; ℤ/nℤ a tous ses idéaux principaux, mais n'est pas intègre si n est composé. |
| 1 / 124 | Taille d'une matrice d'application E→F. | Si dim E=n, dim F=p, la matrice a **p lignes et n colonnes**. Chaque colonne décrit l'image d'un vecteur de la base de E. |
| 4,13 / 127,136 | Définition de la cyclicité : quantificateur. | Il existe **au moins un** v tel que (v,Av,…,Aⁿ⁻¹v) soit une base. Ce n'est pas tout v≠0 : un vecteur propre de diag(1,2,3) n'engendre qu'une droite. |
| 4,6 / 127,129 | GL⁺ et GL⁻ identifiés à des déterminants fixés. | Sur ℝ : GL⁺={det>0}, GL⁻={det<0}, tandis que SL={det=1}. diag(2,1) appartient à GL⁺ sans appartenir à SL. |
| 5 / 128 | Les ensembles de polynômes des questions de supplément doivent être des espaces vectoriels. | Garder le polynôme nul dans Kₙ[X]. Pour Q de degré d : G=QKₙ₋d[X], H=K_d₋₁[X]. Pour les Bernstein, écrire **Vect** de la famille ; une famille seule n'est pas un sous-espace. |
| 6 / 129 | Probabilité de commutation dans un groupe non abélien. | La borne est **≤5/8**, et l'égalité est possible, notamment pour le groupe diédral d'ordre 8. Pour un élément central, le centralisateur est tout le groupe. |
| 6 / 129 | Réduction d'un sous-groupe fini de GLₙ(ℤ) modulo p. | L'injectivité démontrée vaut pour un premier **p≥3**. Modulo 2, −I et I ont même image. Une matrice d'ordre fini est diagonalisable en caractéristique 0 ; ses valeurs propres peuvent être répétées. |
| 7 / 130 | Ordre des unités et cardinalité de GL₂ modulo pᵅ. | Chaque ordre **divise** φ(n), sans être toujours égal à φ(n). Le relèvement ajoute **p⁴⁽ᵅ⁻¹⁾**, car quatre entrées sont libres : modulo 9, la cardinalité est 3⁴·48=3888. |
| 8 / 131 | Contrainte d'orthogonalité indéfinie. | Pour J_pq=diag(Iₚ,−I_q), écrire MᵀJ_pqM=J_pq. Remplacer le membre droit par I ne décrit pas O(p,q). |
| 8 / 131 | Algèbre de Lie, Pauli et représentation adjointe. | Le crochet est bilinéaire et alterné, satisfait Jacobi ; ici il est le **commutateur**, non un crochet de Poisson. Les Pauli sont hermitiennes ; −iσₖ/2 forme une base réelle de su₂. Ad_g(X)=gXg⁻¹ a le centre scalaire pour noyau sur GLₙ, donc n'est pas injective en général. |
| 8 / 131 | Réalisation de Heisenberg par matrices finies. | [E₁₂,E₂₃]=E₁₃, central dans l'algèbre engendrée, mais E₁₃≠I. En caractéristique 0, [A,B]=I est impossible en dimension finie non nulle : tr[A,B]=0≠n. |
| 15 / 138 | Un vecteur réalisant μ_A ne rend pas automatiquement A cyclique. | Il peut avoir μ_v=μ_A avec deg μ_A<n. La base complète de Krylov exige précisément **deg μ_A=n**. Frobenius donne ensuite plusieurs blocs lorsque cette condition échoue. |
| 15 / 138 | Inverse d'une matrice symplectique. | Avec J=[[0,I],[−I,0]], MᵀJM=J donne **M⁻¹=J⁻¹MᵀJ=−JMᵀJ**. Le contrôle M=I doit rendre I. |
| 18–19 / 141–142 | Image de la dérivation sur les fonctions lisses. | D:C∞(ℝ)→C∞(ℝ) est surjective, car toute fonction lisse admet une primitive lisse. Son noyau est l'espace des constantes ; l'image n'exclut pas les constantes. |
| 23 / 146 | « Trigonalisation par pivot de Gauss ». | Gauss produit une équivalence de lignes EA, ou une factorisation avec pivots. Une trigonalisation de réduction est une **similitude** P⁻¹AP. Les opérations de lignes ne conservent pas généralement le spectre. |
| 24 / 147 | Logarithme matriciel présenté sans restriction de z. | La série de log(I+zA) est locale, par exemple pour |z|‖A‖<1, avec la branche près de I. log det(I+zA)=tr log(I+zA) n'est pas une identité globale de branches complexes pour tout z. |
| 29–30 / 152–153 | Logarithme d'un bloc de Jordan inversible. | Pour λI+N et exp ℓ=λ : L=ℓI+Σₖ≥₁(−1)ᵏ⁺¹(N/λ)ᵏ/k, somme finie. Le terme ℓI est **ajouté**, et ne multiplie pas la série. |
| 28–30 / 151–153 | Racine d'une triangulaire : division par une somme éventuellement nulle. | Pour les branches diagonales α,γ d'une racine d'ordre r, le coefficient hors diagonale satisfait βΣⱼ₌₀ʳ⁻¹αʲγʳ⁻¹⁻ʲ=b. Si la somme vaut 0, traiter séparément b=0 et b≠0 ; ne pas diviser sans hypothèse. |
| 28–30 / 151–153 | Signe du déterminant de Vandermonde. | Pour Vᵢⱼ=λⱼⁱ⁻¹ : det V=∏ᵢ<ⱼ(λⱼ−λᵢ). En taille 2, les nœuds 1,2 donnent +1. La taille 4 du TP, avec six facteurs, ne détecte pas à elle seule une inversion de tous les signes. |

## Hypothèses et conventions conservées dans les TP

| Sujet | Convention de l'atelier et raison |
|---|---|
| Changements de base | P contient les nouveaux vecteurs écrits dans l'ancienne base. On vérifie **AP=PB**, puis B=P⁻¹AP. Une forme quadratique se transforme par **PᵀSP**, pas par cette similitude. |
| Dunford et Jordan, p.137–138 | La formulation avec D **diagonalisable sur K** et la forme de Jordan demandent un polynôme scindé sur K. La version de Dunford **semisimple** existe sur un corps parfait, dont ℚ, ℝ, ℂ ; elle peut ne pas être diagonalisable dans le corps de base. Frobenius existe sur tout corps. |
| Newton et nilpotence par traces, p.139 et 147 | L'atelier travaille en caractéristique 0 pour les divisions par k. En caractéristique p, Iₚ a tr(Iₚᵏ)=0 sans être nilpotente. La trace cyclique, elle, ne demande pas cette hypothèse. |
| Jacobi et dérivée du pfaffien, p.147 | Les formules contenant A⁻¹ demandent A inversible. La dérivée du déterminant par les cofacteurs vaut également aux matrices singulières. |
| Pfaffien, p.147 | En taille 4 : Pf A=a₁₂a₃₄−a₁₃a₂₄+a₁₄a₂₃. Pour [[0,M],[−Mᵀ,0]], le facteur est (−1)ᵐ⁽ᵐ⁻¹⁾/². Le pfaffien dépend de l'ordre des coordonnées ; il n'est pas défini en choisissant arbitrairement la racine positive du déterminant. |
| Frobenius métrique, p.148–150 | Sur ℂ, écrire sans ambiguïté **A†=conj(A)ᵀ** et ‖A‖_F²=tr(A†A)=Σ|aᵢⱼ|². Les hermitiennes forment un espace vectoriel réel. Cette norme n'est pas la forme canonique de Frobenius. |
| Inertie d'une forme réelle | L'ordre choisi est **(n₊,n₋,n₀)**. D'autres références ordonnent leurs composantes différemment ; il faut lire leurs définitions avant de comparer. Un vecteur isotrope peut être hors du noyau. |
| Corps et calcul numérique | Un coefficient rationnel est traité exactement. Une figure et des valeurs propres arrondies n'établissent ni une multiplicité exacte ni une indépendance. Aucun petit seuil numérique ne remplace une hypothèse algébrique. |

La question exponentielle E₆ imprimée p.133 est cohérente : exp(x)exp(2y+3)exp(−z−2)=e équivaut à x+2y−z=0. Elle décrit bien un plan vectoriel ; une transcription linéaire sans exposants peut donner une impression contraire.

## Repères de vérification

Les définitions et preuves du module sont reformulées. Les références primaires consultées sont les [notes MIT Algebra I](https://ocw.mit.edu/courses/res-18-011-algebra-i-student-notes-fall-2021/), les [notes de Keith Conrad sur ℤ[i]](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/Zinotes.pdf), le [cours UCSD Math200B sur les facteurs invariants](https://mathweb.ucsd.edu/~asalehig/math200b-18-w.html), les [notes MIT de Pavel Etingof sur Lie](https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/mit18_745_f20_lec_full.pdf) et les [notes MIT de Michel Goemans sur le pfaffien](https://math.mit.edu/~goemans/18455S20/lecs-algmat.pdf).

Les leçons et exercices indiquent leur niveau ; Lie, pfaffien, classification générale de Frobenius et détails de Jordan sont proposés comme **extensions guidées**, à choisir selon la filière. Les exemples de petite dimension sont prouvés avec les outils de SUP/SPÉ indiqués dans le parcours.
