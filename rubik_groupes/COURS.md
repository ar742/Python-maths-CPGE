# Groupes & Rubik — cours et exercices

Les démonstrations et corrections sont conservées. Les notations précèdent les formules ; les guides détaillés sont dans [PARCOURS.md](PARCOURS.md).

## Un cube, un groupe

*Maths sup*

U,R,F,D,L,B sont les tours des six faces. G est l’ensemble de leurs transformations ; ⟨…⟩ désigne le sous-groupe qu’ils engendrent. S₄₈ est le groupe des permutations des 48 facettes non centrales.

**G = ⟨U, R, F, D, L, B⟩ ⊂ S₄₈**

##### Les objets du groupe


Un élément de G est une **transformation du cube** obtenue par des tours de faces. Deux suites de mouvements représentent le même élément si elles ont exactement le même effet sur toutes les facettes. Les suites écrites sont des mots ; les éléments sont leurs effets.


Les six centres restent fixes. Les 48 autres facettes sont permutées. Chaque transformation est donc une bijection, ce qui donne une représentation fidèle de G dans S₄₈. Sₙ désigne le groupe de toutes les permutations de n objets, de cardinal n!. On peut aussi utiliser S₅₄ en fixant les six centres, comme le fait le programme.




##### Vérifier les axiomes



- **Stabilité :** enchaîner deux transformations autorisées reste autorisé.
- **Associativité :** elle vient de la composition des applications.
- **Neutre e :** ne rien faire.
- **Inverse :** refaire les mouvements en sens inverse, dans l'ordre opposé.


##### Une convention à fixer


Ici, **RU signifie « R, puis U »**. Avec la convention usuelle des fonctions, cela correspond à U ∘ R. Tous les produits du cours sont lus de gauche à droite. Une face est tournée dans le sens horaire lorsqu'on la regarde de l'extérieur.


Le cube résolu sert d'origine. Lui appliquer g identifie sa configuration à g. Les centres sont fixes et leur orientation graphique n'est pas suivie : on étudie le 3×3 standard, sans logos orientés.

## Mots et inverses

*Maths sup*

a₁,…,aₙ sont les mouvements d’un mot ; l’exposant −1 indique l’inverse. Les produits se lisent ici de gauche à droite : exécuter a₁, puis a₂, etc.

**(a₁a₂⋯aₙ)⁻¹ = aₙ⁻¹⋯a₂⁻¹a₁⁻¹**

##### Lire la notation


U : haut ; D : bas ; R : droite ; L : gauche ; F : devant ; B : derrière. R' est le quart de tour inverse de R, et R2 son demi-tour. R⁴ = e, R' = R³, et (R2)⁻¹ = R2.


Les mouvements sont attachés au repère du cube. Déplacer la caméra ne change jamais la signification de R ou de U. Le patron affiche chacune des six faces vue de l'extérieur.




##### Démonstration de la formule


Dans (ab)(b⁻¹a⁻¹), l'associativité permet de regrouper bb⁻¹ puis aa⁻¹, et le résultat est e. De même, (b⁻¹a⁻¹)(ab) = e. L'unicité de l'inverse donne (ab)⁻¹ = b⁻¹a⁻¹. Une récurrence fournit la formule générale.


Le mélange `R U F2` est annulé par `F2 U' R'`. Dans l'onglet Résolution, le bouton « Inverse de l'historique » construit ce mot et permet de le jouer pas à pas.




##### Réduire un mot


`R R` devient `R2`, `R R'` disparaît, et `R2 R'` devient `R`. Ces réductions locales sont exactes, mais ne garantissent pas le plus petit nombre de mouvements.


L'inverse de l'historique résout tous les mélanges créés ici dont l'historique est connu. Pour un cube importé sans historique, il faut chercher un mot à partir de la configuration : c'est un autre problème algorithmique.

## Cycles et ordre

*Sup → Spé*

σ est une permutation ; ord(σ) est le plus petit entier positif k tel que σᵏ=e. e est l’identité et ppcm le plus petit commun multiple.

**ord(σ) = ppcm(longueurs des cycles disjoints)**

##### Une permutation se décompose en cycles


Les noms concatènent les faces du repère : URF désigne le coin haut–droite–devant ; UF désigne l'arête haut–devant. Ils nomment les emplacements ou les pièces qui s'y trouvent dans le cube résolu.


(UR → BR → DR → FR) signifie que la pièce UR va en BR, celle de BR en DR, etc. Les cycles affichés décrivent le trajet **pièce d'origine → emplacement actuel**. Les points fixes sont omis.


Un cycle de longueur k revient à l'identité après k applications. Des cycles disjoints agissent indépendamment : leur produit revient à l'identité lorsque chacun est revenu, soit après le ppcm de leurs longueurs.




##### Ne pas oublier l'orientation


Une permutation des 8 coins décrit seulement leurs positions. Un coin peut revenir à sa place en restant tourné. La permutation des 48 facettes retient à la fois la position et l'orientation : son ordre est celui de la transformation complète.


Exemple calculé par le moteur : `R U` est d'ordre 105. Le cycle d'arêtes est de longueur 7 ; l'action complète sur les coins a un ordre de 15, malgré un cycle de positions de longueur 5. Leur ppcm est 105.




##### Le théorème de Lagrange


Pour g ∈ G, le sous-groupe cyclique ⟨g⟩ a ord(g) éléments. Ses classes partitionnent G et ont même cardinal, donc ord(g) divise |G|. Cela donne une contrainte sur les ordres possibles.


Le laboratoire calcule l'ordre exactement par les cycles des facettes, sans répéter le mouvement des milliers de fois. Comparez R, RU et R U R' U'.

## L'ordre des gestes

*Maths sup*

R et U sont les tours droite et haut. RU signifie R puis U. Un groupe est abélien lorsque tous ses éléments commutent.

**RU ≠ UR  ⇒  G n'est pas abélien**

##### Associativité n'est pas commutativité


Les parenthèses ne changent pas le résultat d'un enchaînement. En revanche, permuter deux gestes peut le changer : U déplace certaines pièces qui seront ensuite prises par R, et réciproquement.


Dans le laboratoire, entrez A = R et B = U. Les cubes AB et BA apparaissent côte à côte. Les facettes où leurs résultats diffèrent sont marquées. Il suffit d'une seule différence pour prouver que G n'est pas abélien.




##### Quand des mouvements commutent


R et L agissent sur deux couches disjointes, donc RL = LR. Même chose pour U et D, ou F et B. Deux puissances du même mouvement commutent également.


La commutativité de certains couples ne rend pas tout le groupe abélien. La propriété doit être vraie pour tous les couples.


On ne peut pas trier les lettres d'un algorithme comme on trie les termes d'une somme réelle. Toute simplification doit être justifiée par une relation du groupe.

## Les commutateurs

*Sup → Spé*

A et B sont deux transformations ; A⁻¹ et B⁻¹ les annulent. Leur commutateur [A,B] est défini selon la convention chronologique des produits.

**[A, B] = A B A⁻¹ B⁻¹**

##### Mesurer la non-commutativité


[A, B] = e si et seulement si AB = BA : multipliez l'égalité ABA⁻¹B⁻¹ = e à droite par BA. Faire A puis B et défaire A puis B dans cet ordre laisse une trace lorsque A et B ne commutent pas.




##### Un outil de résolution ciblée


Le **support** d'une permutation est l'ensemble des éléments qu'elle ne fixe pas. Un commutateur bien choisi peut avoir un support plus petit que celui de ses facteurs. Ce n'est pas vrai pour tous les commutateurs : il faut examiner leur action.


Prenez `A = R U R'` et `B = D`. Leur commutateur est `R U R' D R U' R' D'`. Le moteur vérifie qu'il agit sur **trois coins, aucune arête**. Son ordre est 3 ; certains coins changent aussi d'orientation.


On peut créer le défaut C⁻¹, puis le corriger par C. Durant l'algorithme, des pièces déjà correctes peuvent bouger ; c'est son effet final qui les préserve. Essayez le défi « Trois coins » dans Résolution.




##### Une contrainte utile


La signature est un homomorphisme vers {−1, +1}, groupe abélien. Ainsi sgn([σ, τ]) = 1. Un commutateur a donc une permutation paire des coins et une permutation paire des arêtes : il ne peut pas échanger seulement deux coins.


Le petit commutateur R U R' U' n'agit pas seulement sur trois pièces : il affecte quatre coins et trois arêtes. Le laboratoire permet de distinguer les positions modifiées et les orientations modifiées.

## Préparer et conjuguer

*Maths spé*

C est la manœuvre à réutiliser ; S prépare les pièces et S⁻¹ annule cette préparation. SCS⁻¹ est le conjugué de C.

**S C S⁻¹ : préparer → agir → revenir**

##### Changer le lieu de l'action


Supposons qu'une manœuvre C corrige un défaut dans une zone donnée. On effectue un réglage S pour amener les pièces dans cette zone, puis C, puis S⁻¹ pour défaire le réglage. Le résultat est un conjugué de C.


Avec notre convention chronologique, le support de SCS⁻¹ est l'image du support de C par S⁻¹. Le sens de transport serait écrit autrement avec une composition des fonctions lue de droite à gauche.




##### Ce qui est conservé


(SCS⁻¹)ⁿ = SCⁿS⁻¹, par annulation successive des S⁻¹S. Les deux transformations ont donc le même ordre. La conjugaison renomme les positions d'une permutation ; elle conserve les longueurs de ses cycles sur les facettes.


Dans l'exemple, S = F et C est le commutateur de la leçon précédente. Il affecte encore trois coins et aucune arête, mais les coins concernés sont différents. Comparez les noms des pièces et le diagramme des cycles.


Conjuguer un algorithme connu permet de le réutiliser : préparer les pièces, exécuter la manœuvre, puis annuler la préparation. Ce procédé est particulièrement utile pour les résolutions par cycles de pièces.

## Les états possibles

*Maths spé*

co et eo sont les orientations des coins modulo 3 et des arêtes modulo 2. σc et σe sont leurs permutations ; sgn est la signature. Σ additionne toutes les orientations de la famille concernée.

**Σ co ≡ 0 (mod 3) ; Σ eo ≡ 0 (mod 2) ; sgn(σc) = sgn(σe)**

##### Position et orientation


Une configuration est décrite par les permutations σc ∈ S₈ et σe ∈ S₁₂, les orientations co ∈ (ℤ/3ℤ)⁸ des coins et eo ∈ (ℤ/2ℤ)¹² des arêtes. Le programme utilise le repère d'orientation de Kociemba, défini dans les sources et dans le code.


Chaque place de coin a un ordre de faces, par exemple (U, R, F) pour URF. co est l'indice 0, 1 ou 2 où se trouve la facette U ou D de la pièce dans cet ordre. Pour une arête, on ordonne ses deux couleurs et les deux faces de sa place : eo vaut 0 si sa première couleur occupe la première face, 1 sinon. Les ordres de référence sont ceux des tableaux de noms de pièces du programme.




##### Trois contraintes


Les tours de faces conservent la somme des orientations des coins modulo 3 et celle des arêtes modulo 2. Chaque quart de tour fait un 4-cycle de coins et un 4-cycle d'arêtes : les deux signatures changent ensemble. Les trois conditions affichées sont donc nécessaires.


Un seul coin tourné, une seule arête retournée ou seulement deux arêtes échangées sont impossibles par des tours de faces. Les essais d'états impossibles dans Résolution montrent la contrainte violée, sans remplacer le cube courant.


Pour un 3×3 standard avec les bonnes pièces, des coins non miroirs et des centres fixes, ces trois conditions sont également **suffisantes**. La preuve de suffisance demande de construire des manœuvres générant toutes les permutations et orientations autorisées ; elle ne découle pas du seul comptage.




##### Compter les configurations accessibles


|G| = 8! × 12! × 3⁷ × 2¹¹ / 2
= 43 252 003 274 489 856 000


L’orientation du huitième coin et celle de la douzième arête sont imposées par les sommes. Une fois la permutation des coins choisie, seule la moitié des permutations d'arêtes a la bonne parité. Parmi les 8! × 12! × 3⁸ × 2¹² assemblages avec les bonnes pièces, un sur douze est accessible.


Avoir neuf facettes de chaque couleur ne suffit pas à décrire un cube légal. L'import contrôle aussi les pièces, leur chiralité, les centres et les trois invariants.

## Actions et stabilisateurs

*Maths spé · approfondissement*

P est l’ensemble des couples de permutations de coins et d’arêtes obtenus en oubliant leurs orientations. ker est le noyau de cette application ; ℤ/mℤ décrit les orientations modulo m. Cette structure est un approfondissement.

**G → P ⊂ S₈ × S₁₂ ; ker = (ℤ/3ℤ)⁷ × (ℤ/2ℤ)¹¹**

##### Oublier les orientations


L'application π : G → S₈ × S₁₂ qui ne garde que les positions est un homomorphisme. Son image P contient exactement les couples de permutations de même signature. Son noyau contient les transformations qui fixent toutes les positions, mais peuvent changer des orientations.


Ce noyau est isomorphe à (ℤ/3ℤ)⁷ × (ℤ/2ℤ)¹¹. La conjugaison par une permutation déplace les coordonnées d'orientation. On ne doit donc pas modéliser le groupe entier comme un produit direct de quatre groupes indépendants.


Un cadre plus large est le produit des deux groupes de permutations avec orientations : ((ℤ/3ℤ)⁸ ⋊ S₈) × ((ℤ/2ℤ)¹² ⋊ S₁₂). G y est le sous-groupe défini par les trois contraintes de la leçon précédente.




##### Préserver ce qui est résolu


Pour un ensemble A de facettes, son stabilisateur point par point est Stab(A) = {g ∈ G : g(a) = a pour tout a ∈ A}. C'est un sous-groupe : l'identité, les produits et les inverses fixent encore A.


Si A ⊂ B, alors Stab(B) ⊂ Stab(A). Résoudre progressivement davantage de pièces conduit ainsi à des sous-groupes de plus en plus petits. Il faut fixer toutes les facettes d'une pièce pour préserver aussi son orientation.




##### Orbites et limites d'un choix d'algorithmes


L'orbite x·H est l'ensemble des positions atteignables depuis x avec H, pour notre action à droite. Si la cible n'est pas dans cette orbite, aucun mot composé des générateurs de H ne l'atteindra. La formule orbite-stabilisateur donne |x·H| = |H| / |Stab_H(x)|.


Une méthode par couches choisit des algorithmes dont l'effet final appartient au stabilisateur des pièces déjà résolues. Les gestes intermédiaires peuvent temporairement les déplacer.

## Chercher une solution

*Maths spé · algorithmique*

g est la configuration actuelle et e le cube résolu. La distance du graphe compte les mouvements : un quart de tour, son inverse ou un demi-tour valent chacun 1 (convention HTM).

**distance(g, e) = longueur minimale d'un mot qui résout g**

##### Le graphe de Cayley


Les sommets sont les éléments de G. Une arête relie g à gs pour un mouvement s parmi les 18 tours de faces U, U', U2, etc. Le graphe est non orienté car l'inverse de chaque générateur est encore dans cette liste.


La distance dépend de la métrique : ici, un quart de tour, son inverse ou un demi-tour coûtent chacun 1 (**HTM**). Dans la métrique QTM, un demi-tour coûte 2. Ne comparez pas des longueurs sans préciser cette convention.




##### Recherche en largeur bidirectionnelle


Le solveur pédagogique construit une boule autour du cube résolu et une autre autour de l'état courant. Leur intersection fournit un chemin. Avec des explorations par distance croissante et des coûts uniformes, la solution trouvée est minimale dans la borne choisie.


Pour une borne 6, il suffit d'explorer jusqu'à 3 mouvements de chaque côté. Le programme travaille uniquement sur l'état, sans lire l'historique. Il exclut deux mouvements consécutifs d'une même face, toujours réductibles à un seul mouvement ou au neutre.




##### Pourquoi limiter la profondeur ?


Le nombre de mots augmente exponentiellement. La recherche exhaustive de tout G est hors de portée de ce petit programme. Un échec à la borne 6 signifie seulement « pas de solution en six mouvements ou moins ».


Créez un mélange court, oubliez l'historique, puis lancez la recherche : la solution dépend bien de la configuration. Le nombre d'états visités est affiché après le calcul.

## Vers une résolution générale

*Maths spé · approfondissement*

G est le groupe complet ; H est le sous-groupe engendré par les mouvements entre chevrons. R2 est un demi-tour de la face droite, et de même pour les autres faces ; e est le cube résolu.

**G ⊃ H = ⟨U, D, R2, L2, F2, B2⟩ ⊃ {e}**

##### Un sous-groupe intermédiaire


Dans le repère d'orientation utilisé ici, H est exactement l'ensemble des états où tous les coins et arêtes ont une orientation nulle et où les quatre arêtes FR, FL, BL, BR occupent les quatre places de la tranche médiane. Leurs permutations à l'intérieur de la tranche restent libres.


Les générateurs de H conservent ces propriétés. La réciproque, qui affirme qu'ils engendrent tous les états ainsi décrits, est un résultat supplémentaire. L'indicateur « Dans H » du simulateur vérifie les trois propriétés sur le cube courant.




##### Deux phases



- Trouver une suite amenant l'état dans H : orienter les pièces et placer les arêtes médianes dans leur tranche.
- Résoudre cet état en n'utilisant que les générateurs de H.
Il y a 3⁷ × 2¹¹ × 495 = 2 217 093 120 classes relatives à H et |H| = 8! × 8! × 4! / 2 = 19 508 428 800 états. Les coordonnées de la phase 1 décrivent ces classes, sans mémoriser toute la configuration.




##### Ce que propose l'application


La résolution par historique et la recherche courte sont intégrées sans dépendances. Un adaptateur **optionnel** utilise le module séparé `kociemba` pour résoudre un état général importé. L'application vérifie ensuite la solution en l'appliquant dans son propre moteur.


Le module externe fournit un solveur pratique à deux phases. Une solution courte obtenue ainsi n'est pas, en général, une preuve de minimalité globale. Sans ce module, le programme reste entièrement utilisable pour le cours et les expériences.


La stratégie algébrique réduit progressivement l'espace à explorer. Elle explique comment dépasser les limites d'une recherche brute, sans se limiter à mémoriser des suites de gestes.

## Exercices corrigés

### 01 · L'inverse d'un mélange

Écrire l'inverse de R U2 F' L, puis justifier l'ordre des facteurs.

**Correction.** L' F U2 R'. On inverse chaque mouvement et on lit le mot en sens inverse. Le produit du mot initial avec ce mot se réduit à e par annulations successives.

### 02 · Réduction locale

Réduire R R U U' R' R2. A-t-on forcément trouvé une solution minimale pour tout mot ?

**Correction.** U U' disparaît. Les puissances de R donnent R^(1+1−1+2) = R³ = R'. Les réductions locales ne suffisent pas en général à garantir la minimalité, car d'autres relations peuvent impliquer plusieurs faces.

### 03 · Une preuve de non-commutativité

Montrer que RU ≠ UR en suivant la pièce initialement en UR.

**Correction.** Après R puis U, l'arête UR termine en BR : U ne touche plus cette arête. Après U puis R, elle termine en UF : R ne touche pas UF. Les images diffèrent.

### 04 · Puissances d'un quart de tour

Quels sont les ordres de R, R2, R' ? Combien d'éléments contient ⟨R⟩ ?

**Correction.** Les ordres sont 4, 2 et 4. ⟨R⟩ = {e, R, R2, R'} contient 4 éléments et est isomorphe à ℤ/4ℤ.

### 05 · Positions et orientations

Une permutation des coins forme un cycle de longueur 5. Peut-on affirmer que la transformation complète est d'ordre 5 ?

**Correction.** Non : les orientations et les arêtes sont oubliées. Pour RU, le cycle non trivial des positions de coins a longueur 5, mais l'action complète sur les coins a ordre 15 et la transformation entière ordre 105.

### 06 · Signature et commutateur

Pourquoi un commutateur ne peut-il pas échanger seulement deux arêtes et fixer toutes les autres pièces ?

**Correction.** La signature de la projection sur les arêtes est un homomorphisme vers un groupe abélien. Elle vaut +1 sur tout commutateur. Une transposition d'arêtes a signature −1 : elle est impossible pour un commutateur.

### 07 · Ordre d'un conjugué

S et C sont deux éléments du groupe du cube. Prouver ord(SCS⁻¹) = ord(C).

**Correction.** Pour tout n, (SCS⁻¹)ⁿ = SCⁿS⁻¹. L'une des puissances vaut e si et seulement si l'autre vaut e. Les ensembles d'exposants qui annulent les deux éléments sont donc les mêmes.

### 08 · Les trois impossibilités

Quel invariant interdit : un seul coin tourné ; une seule arête retournée ; deux arêtes échangées seules ?

**Correction.** Respectivement : la somme des orientations des coins modulo 3 ; la somme des orientations des arêtes modulo 2 ; l'égalité des signatures des coins et arêtes. Les couleurs seules ne suffisent pas à vérifier ces contraintes.

### 09 · Un assemblage sur douze

Retrouver le facteur 1/12 entre tous les assemblages des bonnes pièces et les états accessibles.

**Correction.** La somme des twists impose un facteur 1/3, celle des orientations des arêtes un facteur 1/2, et l'égalité des signatures un facteur 1/2. Les choix sont indépendants dans le modèle d'assemblage. Le facteur total est 1/(3×2×2) = 1/12.

### 10 · Stabiliser des pièces

Prouver que les transformations fixant toutes les facettes de quatre arêtes données forment un sous-groupe.

**Correction.** L'identité fixe ces facettes. Le produit de deux transformations qui les fixent les fixe encore. L'inverse d'une bijection fixant un point fixe ce point. Le critère de sous-groupe est satisfait. Fixer les pièces seulement en position ne garantirait pas leur orientation.

### 11 · Une recherche infructueuse

La recherche jusqu'à 6 HTM ne trouve pas de solution. Peut-on conclure que le cube est impossible ?

**Correction.** Non. L'échec prouve seulement qu'il n'existe pas de solution de longueur ≤ 6 si la recherche a été exhaustive dans cette borne. Une interruption par limite de temps ne prouve même pas cette absence. L'impossibilité physique se vérifie par les pièces et les invariants.

### 12 · Les classes de H

G est le groupe du cube et H=⟨U,D,R2,L2,F2,B2⟩. À partir de |G| et |H| donnés dans la leçon, calculer [G:H], le nombre de classes de H dans G. Pourquoi ne faut-il pas appeler automatiquement G/H un groupe quotient ?

**Correction.** [G:H] = 2 217 093 120 = 3⁷×2¹¹×495. Les classes forment toujours un ensemble, mais un groupe quotient exige un sous-groupe normal. H n'est pas normal : R2 appartient à H, alors que F R2 F' peut sortir de H (à vérifier dans le laboratoire).

## Sources et conventions

**[Janet Chen · Group Theory and the Rubik's Cube](https://people.math.harvard.edu/~jjchen/docs/Group%20Theory%20and%20the%20Rubik%27s%20Cube.pdf)** — Cours mathématique complémentaire : groupes, actions et caractérisation des états accessibles.

**[Herbert Kociemba · The Cubie Level](https://kociemba.org/math/cubielevel.htm)** — Référence des noms de pièces et du repère des orientations utilisé par le moteur.

**[Herbert Kociemba · The Two-Phase Algorithm](https://kociemba.org/math/twophase.htm)** — Sous-groupe intermédiaire H et stratégie de résolution à deux phases.

**[Module Python optionnel kociemba](https://github.com/muodov/kociemba)** — Dépendance séparée pour la résolution générale ; elle n'est pas requise pour le cours.
