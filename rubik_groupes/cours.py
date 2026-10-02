"""Cours original en français, expériences et exercices de niveau CPGE.

Les HTML ci-dessous sont des ressources locales de confiance, jamais du texte
fourni par un visiteur. Les notations utilisent une multiplication chronologique.
"""

LESSONS = [
    {"id": "groupe", "title": "Un cube, un groupe", "level": "Maths sup", "subtitle": "Transformer un objet concret en objet algébrique.",
     "formula": "G = ⟨U, R, F, D, L, B⟩ ⊂ S₄₈", "demo": "R", "demo_label": "Observer un quart de tour",
     "html": """
<h3>Les objets du groupe</h3>
<p>Un élément de G est une <strong>transformation du cube</strong> obtenue par des tours de faces. Deux suites de mouvements représentent le même élément si elles ont exactement le même effet sur toutes les facettes. Les suites écrites sont des <em>mots</em> ; les éléments sont leurs effets.</p>
<p>Les six centres restent fixes. Les 48 autres facettes sont permutées. Chaque transformation est donc une bijection, ce qui donne une représentation fidèle de G dans S₄₈. Sₙ désigne le groupe de toutes les permutations de n objets, de cardinal n!. On peut aussi utiliser S₅₄ en fixant les six centres, comme le fait le programme.</p>
<h3>Vérifier les axiomes</h3>
<ul><li><strong>Stabilité :</strong> enchaîner deux transformations autorisées reste autorisé.</li><li><strong>Associativité :</strong> elle vient de la composition des applications.</li><li><strong>Neutre e :</strong> ne rien faire.</li><li><strong>Inverse :</strong> refaire les mouvements en sens inverse, dans l'ordre opposé.</li></ul>
<h3>Une convention à fixer</h3>
<p>Ici, <strong>RU signifie « R, puis U »</strong>. Avec la convention usuelle des fonctions, cela correspond à U ∘ R. Tous les produits du cours sont lus de gauche à droite. Une face est tournée dans le sens horaire lorsqu'on la regarde de l'extérieur.</p>
<div class="insight">Le cube résolu sert d'origine. Lui appliquer g identifie sa configuration à g. Les centres sont fixes et leur orientation graphique n'est pas suivie : on étudie le 3×3 standard, sans logos orientés.</div>
"""},
    {"id": "inverse", "title": "Mots et inverses", "level": "Maths sup", "subtitle": "Une première méthode de résolution, et sa limite.",
     "formula": "(a₁a₂⋯aₙ)⁻¹ = aₙ⁻¹⋯a₂⁻¹a₁⁻¹", "demo": "R U F2", "demo_label": "Créer un mélange connu",
     "html": """
<h3>Lire la notation</h3>
<p>U : haut ; D : bas ; R : droite ; L : gauche ; F : devant ; B : derrière. R' est le quart de tour inverse de R, et R2 son demi-tour. R⁴ = e, R' = R³, et (R2)⁻¹ = R2.</p>
<p>Les mouvements sont attachés au repère du cube. Déplacer la caméra ne change jamais la signification de R ou de U. Le patron affiche chacune des six faces vue de l'extérieur.</p>
<h3>Démonstration de la formule</h3>
<p>Dans (ab)(b⁻¹a⁻¹), l'associativité permet de regrouper bb⁻¹ puis aa⁻¹, et le résultat est e. De même, (b⁻¹a⁻¹)(ab) = e. L'unicité de l'inverse donne (ab)⁻¹ = b⁻¹a⁻¹. Une récurrence fournit la formule générale.</p>
<p>Le mélange <code>R U F2</code> est annulé par <code>F2 U' R'</code>. Dans l'onglet Résolution, le bouton « Inverse de l'historique » construit ce mot et permet de le jouer pas à pas.</p>
<h3>Réduire un mot</h3>
<p><code>R R</code> devient <code>R2</code>, <code>R R'</code> disparaît, et <code>R2 R'</code> devient <code>R</code>. Ces réductions locales sont exactes, mais ne garantissent pas le plus petit nombre de mouvements.</p>
<div class="insight">L'inverse de l'historique résout tous les mélanges créés ici dont l'historique est connu. Pour un cube importé sans historique, il faut chercher un mot à partir de la configuration : c'est un autre problème algorithmique.</div>
"""},
    {"id": "permutations", "title": "Cycles et ordre", "level": "Sup → Spé", "subtitle": "Combien de répétitions pour revenir au départ ?",
     "formula": "ord(σ) = ppcm(longueurs des cycles disjoints)", "demo": "R U", "demo_label": "Analyser RU (ordre 105)",
     "html": """
<h3>Une permutation se décompose en cycles</h3>
<p>Les noms concatènent les faces du repère : URF désigne le coin haut–droite–devant ; UF désigne l'arête haut–devant. Ils nomment les emplacements ou les pièces qui s'y trouvent dans le cube résolu.</p>
<p>(UR → BR → DR → FR) signifie que la pièce UR va en BR, celle de BR en DR, etc. Les cycles affichés décrivent le trajet <strong>pièce d'origine → emplacement actuel</strong>. Les points fixes sont omis.</p>
<p>Un cycle de longueur k revient à l'identité après k applications. Des cycles disjoints agissent indépendamment : leur produit revient à l'identité lorsque chacun est revenu, soit après le ppcm de leurs longueurs.</p>
<h3>Ne pas oublier l'orientation</h3>
<p>Une permutation des 8 coins décrit seulement leurs <em>positions</em>. Un coin peut revenir à sa place en restant tourné. La permutation des 48 facettes retient à la fois la position et l'orientation : son ordre est celui de la transformation complète.</p>
<p>Exemple calculé par le moteur : <code>R U</code> est d'ordre 105. Le cycle d'arêtes est de longueur 7 ; l'action complète sur les coins a un ordre de 15, malgré un cycle de positions de longueur 5. Leur ppcm est 105.</p>
<h3>Le théorème de Lagrange</h3>
<p>Pour g ∈ G, le sous-groupe cyclique ⟨g⟩ a ord(g) éléments. Ses classes partitionnent G et ont même cardinal, donc ord(g) divise |G|. Cela donne une contrainte sur les ordres possibles.</p>
<div class="insight">Le laboratoire calcule l'ordre exactement par les cycles des facettes, sans répéter le mouvement des milliers de fois. Comparez R, RU et R U R' U'.</div>
"""},
    {"id": "noncommutatif", "title": "L'ordre des gestes", "level": "Maths sup", "subtitle": "Pourquoi RU et UR donnent deux cubes différents.",
     "formula": "RU ≠ UR  ⇒  G n'est pas abélien", "demo": "R U", "demo_label": "Appliquer R puis U",
     "html": """
<h3>Associativité n'est pas commutativité</h3>
<p>Les parenthèses ne changent pas le résultat d'un enchaînement. En revanche, permuter deux gestes peut le changer : U déplace certaines pièces qui seront ensuite prises par R, et réciproquement.</p>
<p>Dans le laboratoire, entrez A = R et B = U. Les cubes AB et BA apparaissent côte à côte. Les facettes où leurs résultats diffèrent sont marquées. Il suffit d'une seule différence pour prouver que G n'est pas abélien.</p>
<h3>Quand des mouvements commutent</h3>
<p>R et L agissent sur deux couches disjointes, donc RL = LR. Même chose pour U et D, ou F et B. Deux puissances du même mouvement commutent également.</p>
<p>La commutativité de certains couples ne rend pas tout le groupe abélien. La propriété doit être vraie pour <em>tous</em> les couples.</p>
<div class="insight">On ne peut pas trier les lettres d'un algorithme comme on trie les termes d'une somme réelle. Toute simplification doit être justifiée par une relation du groupe.</div>
"""},
    {"id": "commutateurs", "title": "Les commutateurs", "level": "Sup → Spé", "subtitle": "Concentrer l'effet sur quelques pièces.",
     "formula": "[A, B] = A B A⁻¹ B⁻¹", "demo": "R U R' D R U' R' D'", "demo_label": "Cycle de trois coins seulement",
     "html": """
<h3>Mesurer la non-commutativité</h3>
<p>[A, B] = e si et seulement si AB = BA : multipliez l'égalité ABA⁻¹B⁻¹ = e à droite par BA. Faire A puis B et défaire A puis B dans cet ordre laisse une trace lorsque A et B ne commutent pas.</p>
<h3>Un outil de résolution ciblée</h3>
<p>Le <strong>support</strong> d'une permutation est l'ensemble des éléments qu'elle ne fixe pas. Un commutateur bien choisi peut avoir un support plus petit que celui de ses facteurs. Ce n'est pas vrai pour tous les commutateurs : il faut examiner leur action.</p>
<p>Prenez <code>A = R U R'</code> et <code>B = D</code>. Leur commutateur est <code>R U R' D R U' R' D'</code>. Le moteur vérifie qu'il agit sur <strong>trois coins, aucune arête</strong>. Son ordre est 3 ; certains coins changent aussi d'orientation.</p>
<p>On peut créer le défaut C⁻¹, puis le corriger par C. Durant l'algorithme, des pièces déjà correctes peuvent bouger ; c'est son <em>effet final</em> qui les préserve. Essayez le défi « Trois coins » dans Résolution.</p>
<h3>Une contrainte utile</h3>
<p>La signature est un homomorphisme vers {−1, +1}, groupe abélien. Ainsi sgn([σ, τ]) = 1. Un commutateur a donc une permutation paire des coins et une permutation paire des arêtes : il ne peut pas échanger seulement deux coins.</p>
<div class="insight">Le petit commutateur R U R' U' n'agit pas seulement sur trois pièces : il affecte quatre coins et trois arêtes. Le laboratoire permet de distinguer les positions modifiées et les orientations modifiées.</div>
"""},
    {"id": "conjugaison", "title": "Préparer et conjuguer", "level": "Maths spé", "subtitle": "Transporter une manœuvre utile vers d'autres pièces.",
     "formula": "S C S⁻¹ : préparer → agir → revenir", "demo": "F R U R' D R U' R' D' F'", "demo_label": "Transporter le cycle de trois coins",
     "html": """
<h3>Changer le lieu de l'action</h3>
<p>Supposons qu'une manœuvre C corrige un défaut dans une zone donnée. On effectue un réglage S pour amener les pièces dans cette zone, puis C, puis S⁻¹ pour défaire le réglage. Le résultat est un conjugué de C.</p>
<p>Avec notre convention chronologique, le support de SCS⁻¹ est l'image du support de C par S⁻¹. Le sens de transport serait écrit autrement avec une composition des fonctions lue de droite à gauche.</p>
<h3>Ce qui est conservé</h3>
<p>(SCS⁻¹)ⁿ = SCⁿS⁻¹, par annulation successive des S⁻¹S. Les deux transformations ont donc le même ordre. La conjugaison renomme les positions d'une permutation ; elle conserve les longueurs de ses cycles sur les facettes.</p>
<p>Dans l'exemple, S = F et C est le commutateur de la leçon précédente. Il affecte encore trois coins et aucune arête, mais les coins concernés sont différents. Comparez les noms des pièces et le diagramme des cycles.</p>
<div class="insight">Conjuguer un algorithme connu permet de le réutiliser. C'est le principe « setup, algorithme, undo setup », particulièrement utile pour les résolutions par cycles de pièces.</div>
"""},
    {"id": "invariants", "title": "Les états possibles", "level": "Maths spé", "subtitle": "Pourquoi certaines configurations ne peuvent pas être résolues.",
     "formula": "Σ co ≡ 0 (mod 3) ; Σ eo ≡ 0 (mod 2) ; sgn(σc) = sgn(σe)", "demo": "F R U B L2 D", "demo_label": "Vérifier les trois invariants",
     "html": """
<h3>Position et orientation</h3>
<p>Une configuration est décrite par les permutations σc ∈ S₈ et σe ∈ S₁₂, les orientations co ∈ (ℤ/3ℤ)⁸ des coins et eo ∈ (ℤ/2ℤ)¹² des arêtes. Le programme utilise le repère d'orientation de Kociemba, défini dans les sources et dans le code.</p>
<p>Chaque place de coin a un ordre de faces, par exemple (U, R, F) pour URF. co est l'indice 0, 1 ou 2 où se trouve la facette U ou D de la pièce dans cet ordre. Pour une arête, on ordonne ses deux couleurs et les deux faces de sa place : eo vaut 0 si sa première couleur occupe la première face, 1 sinon. Les ordres de référence sont ceux des tableaux de noms de pièces du programme.</p>
<h3>Trois contraintes</h3>
<p>Les tours de faces conservent la somme des orientations des coins modulo 3 et celle des arêtes modulo 2. Chaque quart de tour fait un 4-cycle de coins et un 4-cycle d'arêtes : les deux signatures changent ensemble. Les trois conditions affichées sont donc nécessaires.</p>
<p>Un seul coin tourné, une seule arête retournée ou seulement deux arêtes échangées sont impossibles par des tours de faces. Les essais d'états impossibles dans Résolution montrent la contrainte violée, sans remplacer le cube courant.</p>
<p>Pour un 3×3 standard avec les bonnes pièces, des coins non miroirs et des centres fixes, ces trois conditions sont également <strong>suffisantes</strong>. La preuve de suffisance demande de construire des manœuvres générant toutes les permutations et orientations autorisées ; elle ne découle pas du seul comptage.</p>
<h3>Compter les configurations accessibles</h3>
<div class="equation">|G| = 8! × 12! × 3⁷ × 2¹¹ / 2<br>= 43 252 003 274 489 856 000</div>
<p>Le huitième twist et le douzième flip sont imposés par les sommes. Une fois la permutation des coins choisie, seule la moitié des permutations d'arêtes a la bonne parité. Parmi les 8! × 12! × 3⁸ × 2¹² assemblages avec les bonnes pièces, un sur douze est accessible.</p>
<div class="insight">Avoir neuf facettes de chaque couleur ne suffit pas à décrire un cube légal. L'import contrôle aussi les pièces, leur chiralité, les centres et les trois invariants.</div>
"""},
    {"id": "structure", "title": "Actions et stabilisateurs", "level": "Maths spé · approfondissement", "subtitle": "La structure algébrique d'une résolution progressive.",
     "formula": "G → P ⊂ S₈ × S₁₂ ; ker = (ℤ/3ℤ)⁷ × (ℤ/2ℤ)¹¹", "demo": "R U R' D R U' R' D'", "demo_label": "Observer des pièces préservées",
     "html": """
<h3>Oublier les orientations</h3>
<p>L'application π : G → S₈ × S₁₂ qui ne garde que les positions est un homomorphisme. Son image P contient exactement les couples de permutations de même signature. Son noyau contient les transformations qui fixent toutes les positions, mais peuvent changer des orientations.</p>
<p>Ce noyau est isomorphe à (ℤ/3ℤ)⁷ × (ℤ/2ℤ)¹¹. La conjugaison par une permutation déplace les coordonnées d'orientation. On ne doit donc pas modéliser le groupe entier comme un produit direct de quatre groupes indépendants.</p>
<p>Un cadre plus large est le produit des deux groupes de permutations avec orientations : ((ℤ/3ℤ)⁸ ⋊ S₈) × ((ℤ/2ℤ)¹² ⋊ S₁₂). G y est le sous-groupe défini par les trois contraintes de la leçon précédente.</p>
<h3>Préserver ce qui est résolu</h3>
<p>Pour un ensemble A de facettes, son stabilisateur point par point est Stab(A) = {g ∈ G : g(a) = a pour tout a ∈ A}. C'est un sous-groupe : l'identité, les produits et les inverses fixent encore A.</p>
<p>Si A ⊂ B, alors Stab(B) ⊂ Stab(A). Résoudre progressivement davantage de pièces conduit ainsi à des sous-groupes de plus en plus petits. Il faut fixer toutes les facettes d'une pièce pour préserver aussi son orientation.</p>
<h3>Orbites et limites d'un choix d'algorithmes</h3>
<p>L'orbite x·H est l'ensemble des positions atteignables depuis x avec H, pour notre action à droite. Si la cible n'est pas dans cette orbite, aucun mot composé des générateurs de H ne l'atteindra. La formule orbite-stabilisateur donne |x·H| = |H| / |Stab_H(x)|.</p>
<div class="insight">Une méthode par couches choisit des algorithmes dont l'effet final appartient au stabilisateur des pièces déjà résolues. Les gestes intermédiaires peuvent temporairement les déplacer.</div>
"""},
    {"id": "cayley", "title": "Chercher une solution", "level": "Maths spé · algorithmique", "subtitle": "Résoudre revient à trouver un chemin dans un graphe.",
     "formula": "distance(g, e) = longueur minimale d'un mot qui résout g", "demo": "R U F2 L", "demo_label": "Préparer une recherche courte",
     "html": """
<h3>Le graphe de Cayley</h3>
<p>Les sommets sont les éléments de G. Une arête relie g à gs pour un mouvement s parmi les 18 tours de faces U, U', U2, etc. Le graphe est non orienté car l'inverse de chaque générateur est encore dans cette liste.</p>
<p>La distance dépend de la métrique : ici, un quart de tour, son inverse ou un demi-tour coûtent chacun 1 (<strong>HTM</strong>). Dans la métrique QTM, un demi-tour coûte 2. Ne comparez pas des longueurs sans préciser cette convention.</p>
<h3>Recherche en largeur bidirectionnelle</h3>
<p>Le solveur pédagogique construit une boule autour du cube résolu et une autre autour de l'état courant. Leur intersection fournit un chemin. Avec des explorations par distance croissante et des coûts uniformes, la solution trouvée est minimale dans la borne choisie.</p>
<p>Pour une borne 6, il suffit d'explorer jusqu'à 3 mouvements de chaque côté. Le programme travaille uniquement sur l'état, sans lire l'historique. Il exclut deux mouvements consécutifs d'une même face, toujours réductibles à un seul mouvement ou au neutre.</p>
<h3>Pourquoi limiter la profondeur ?</h3>
<p>Le nombre de mots augmente exponentiellement. La recherche exhaustive de tout G est hors de portée de ce petit programme. Un échec à la borne 6 signifie seulement « pas de solution en six mouvements ou moins ».</p>
<div class="insight">Créez un mélange court, oubliez l'historique, puis lancez la recherche : la solution dépend bien de la configuration. Le nombre d'états visités est affiché après le calcul.</div>
"""},
    {"id": "phases", "title": "Vers une résolution générale", "level": "Maths spé · approfondissement", "subtitle": "L'idée de Kociemba : entrer dans un sous-groupe, puis y résoudre.",
     "formula": "G ⊃ H = ⟨U, D, R2, L2, F2, B2⟩ ⊃ {e}", "demo": "R2 U F2 D' L2 B2", "demo_label": "Créer un état dans H",
     "html": """
<h3>Un sous-groupe intermédiaire</h3>
<p>Dans le repère d'orientation utilisé ici, H est exactement l'ensemble des états où tous les coins et arêtes ont une orientation nulle et où les quatre arêtes FR, FL, BL, BR occupent les quatre places de la tranche médiane. Leurs permutations à l'intérieur de la tranche restent libres.</p>
<p>Les générateurs de H conservent ces propriétés. La réciproque, qui affirme qu'ils engendrent tous les états ainsi décrits, est un résultat supplémentaire. L'indicateur « Dans H » du simulateur vérifie les trois propriétés sur le cube courant.</p>
<h3>Deux phases</h3>
<ol><li>Trouver une suite amenant l'état dans H : orienter les pièces et placer les arêtes médianes dans leur tranche.</li><li>Résoudre cet état en n'utilisant que les générateurs de H.</li></ol>
<p>Il y a 3⁷ × 2¹¹ × 495 = 2 217 093 120 classes relatives à H et |H| = 8! × 8! × 4! / 2 = 19 508 428 800 états. Les coordonnées de la phase 1 décrivent ces classes, sans mémoriser toute la configuration.</p>
<h3>Ce que propose l'application</h3>
<p>La résolution par historique et la recherche courte sont intégrées sans dépendances. Un adaptateur <strong>optionnel</strong> utilise le module séparé <code>kociemba</code> pour résoudre un état général importé. L'application vérifie ensuite la solution en l'appliquant dans son propre moteur.</p>
<p>Le module externe fournit un solveur pratique à deux phases. Une solution courte obtenue ainsi n'est pas, en général, une preuve de minimalité globale. Sans ce module, le programme reste entièrement utilisable pour le cours et les expériences.</p>
<div class="insight">La stratégie algébrique réduit progressivement l'espace à explorer. Elle explique comment dépasser les limites d'une recherche brute, sans se limiter à mémoriser des suites de gestes.</div>
"""},
]

PRESETS = [
    {"name": "Quart de tour", "sequence": "R"},
    {"name": "RU : ordre 105", "sequence": "R U"},
    {"name": "Commutateur [R,U]", "sequence": "R U R' U'"},
    {"name": "Trois coins", "sequence": "R U R' D R U' R' D'"},
    {"name": "Trois coins conjugués", "sequence": "F R U R' D R U' R' D' F'"},
    {"name": "Dans le sous-groupe H", "sequence": "R2 U F2 D' L2 B2"},
]

EXERCISES = [
    {"level": "Sup", "title": "01 · L'inverse d'un mélange", "question": "Écrire l'inverse de R U2 F' L, puis justifier l'ordre des facteurs.",
     "answer": "L' F U2 R'. On inverse chaque mouvement et on lit le mot en sens inverse. Le produit du mot initial avec ce mot se réduit à e par annulations successives.", "demo": "R U2 F' L"},
    {"level": "Sup", "title": "02 · Réduction locale", "question": "Réduire R R U U' R' R2. A-t-on forcément trouvé une solution minimale pour tout mot ?",
     "answer": "U U' disparaît. Les puissances de R donnent R^(1+1−1+2) = R³ = R'. Les réductions locales ne suffisent pas en général à garantir la minimalité, car d'autres relations peuvent impliquer plusieurs faces.", "demo": "R R U U' R' R2"},
    {"level": "Sup", "title": "03 · Une preuve de non-commutativité", "question": "Montrer que RU ≠ UR en suivant la pièce initialement en UR.",
     "answer": "Après R puis U, l'arête UR termine en BR : U ne touche plus cette arête. Après U puis R, elle termine en UF : R ne touche pas UF. Les images diffèrent.", "demo": "R U"},
    {"level": "Sup", "title": "04 · Puissances d'un quart de tour", "question": "Quels sont les ordres de R, R2, R' ? Combien d'éléments contient ⟨R⟩ ?",
     "answer": "Les ordres sont 4, 2 et 4. ⟨R⟩ = {e, R, R2, R'} contient 4 éléments et est isomorphe à ℤ/4ℤ.", "demo": "R2"},
    {"level": "Sup → Spé", "title": "05 · Positions et orientations", "question": "Une permutation des coins forme un cycle de longueur 5. Peut-on affirmer que la transformation complète est d'ordre 5 ?",
     "answer": "Non : les orientations et les arêtes sont oubliées. Pour RU, le cycle non trivial des positions de coins a longueur 5, mais l'action complète sur les coins a ordre 15 et la transformation entière ordre 105.", "demo": "R U"},
    {"level": "Spé", "title": "06 · Signature et commutateur", "question": "Pourquoi un commutateur ne peut-il pas échanger seulement deux arêtes et fixer toutes les autres pièces ?",
     "answer": "La signature de la projection sur les arêtes est un homomorphisme vers un groupe abélien. Elle vaut +1 sur tout commutateur. Une transposition d'arêtes a signature −1 : elle est impossible pour un commutateur.", "demo": "R U R' U'"},
    {"level": "Spé", "title": "07 · Ordre d'un conjugué", "question": "Prouver ord(SCS⁻¹) = ord(C).",
     "answer": "Pour tout n, (SCS⁻¹)ⁿ = SCⁿS⁻¹. L'une des puissances vaut e si et seulement si l'autre vaut e. Les ensembles d'exposants qui annulent les deux éléments sont donc les mêmes.", "demo": "F R U R' D R U' R' D' F'"},
    {"level": "Spé", "title": "08 · Les trois impossibilités", "question": "Quel invariant interdit : un seul coin tourné ; une seule arête retournée ; deux arêtes échangées seules ?",
     "answer": "Respectivement : la somme des twists modulo 3 ; la somme des flips modulo 2 ; l'égalité des signatures des coins et arêtes. Les couleurs seules ne suffisent pas à vérifier ces contraintes.", "demo": "F R U"},
    {"level": "Spé", "title": "09 · Un assemblage sur douze", "question": "Retrouver le facteur 1/12 entre tous les assemblages des bonnes pièces et les états accessibles.",
     "answer": "La somme des twists impose un facteur 1/3, celle des flips un facteur 1/2, et l'égalité des signatures un facteur 1/2. Les choix sont indépendants dans le modèle d'assemblage. Le facteur total est 1/(3×2×2) = 1/12.", "demo": "F R U B L2 D"},
    {"level": "Spé", "title": "10 · Stabiliser des pièces", "question": "Prouver que les transformations fixant toutes les facettes de quatre arêtes données forment un sous-groupe.",
     "answer": "L'identité fixe ces facettes. Le produit de deux transformations qui les fixent les fixe encore. L'inverse d'une bijection fixant un point fixe ce point. Le critère de sous-groupe est satisfait. Fixer les pièces seulement en position ne garantirait pas leur orientation.", "demo": "R U R' D R U' R' D'"},
    {"level": "Spé · algorithmique", "title": "11 · Une recherche infructueuse", "question": "La recherche jusqu'à 6 HTM ne trouve pas de solution. Peut-on conclure que le cube est impossible ?",
     "answer": "Non. L'échec prouve seulement qu'il n'existe pas de solution de longueur ≤ 6 si la recherche a été exhaustive dans cette borne. Une interruption par limite de temps ne prouve même pas cette absence. L'impossibilité physique se vérifie par les pièces et les invariants.", "demo": "R U F2 L D B R2"},
    {"level": "Spé · approfondissement", "title": "12 · Les classes de H", "question": "À partir de |G| et |H|, calculer [G:H]. Pourquoi ne faut-il pas appeler automatiquement G/H un groupe quotient ?",
     "answer": "[G:H] = 2 217 093 120 = 3⁷×2¹¹×495. Les classes forment toujours un ensemble, mais un groupe quotient exige un sous-groupe normal. H n'est pas normal : R2 appartient à H, alors que F R2 F' peut sortir de H (à vérifier dans le laboratoire).", "demo": "F R2 F'"},
]

SOURCES = [
    {"title": "Janet Chen · Group Theory and the Rubik's Cube", "url": "https://people.math.harvard.edu/~jjchen/docs/Group%20Theory%20and%20the%20Rubik%27s%20Cube.pdf", "description": "Cours mathématique complémentaire : groupes, actions et caractérisation des états accessibles."},
    {"title": "Herbert Kociemba · The Cubie Level", "url": "https://kociemba.org/math/cubielevel.htm", "description": "Référence des noms de pièces et du repère des orientations utilisé par le moteur."},
    {"title": "Herbert Kociemba · The Two-Phase Algorithm", "url": "https://kociemba.org/math/twophase.htm", "description": "Sous-groupe intermédiaire H et stratégie de résolution à deux phases."},
    {"title": "Module Python optionnel kociemba", "url": "https://github.com/muodov/kociemba", "description": "Dépendance séparée pour la résolution générale ; elle n'est pas requise pour le cours."},
]
