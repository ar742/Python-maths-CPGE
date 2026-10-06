# Algèbre et algèbre linéaire : dix missions de CPGE

Le parcours part des TP du recueil personnel, puis construit des liens entre arithmétique, géométrie, réduction, représentations et applications. Chaque séance peut durer 1 h 30 à 2 h ; les prolongements se choisissent selon la filière et le temps disponible. Les leçons SUP constituent l'entrée dans l'atelier ; les critères de réduction demandent les acquis de SPÉ. Frobenius, Jordan détaillé, Lie, représentations, formes alternées, pfaffien et théorie spectrale des graphes sont des extensions guidées ; leur étude ne constitue pas une déclaration de programme commune à toutes les CPGE.

Les **17 laboratoires** manipulent des objets de tailles variées : matrices denses 4×4, réductions 6×6, polynômes à sept coefficients, oscillateurs en dimension 4 ou 6, chaînes de Markov à six états, Laplaciens 8×8. Les petits contre-exemples sont conservés pour les distinctions qu'ils démontrent. Chaque leçon possède sa liste d'objets et variables ; les coefficients d'un polynôme, des probabilités, des impulsions et des températures ne sont pas interchangeables.

Pour chaque mission, suivre cinq étapes : **déclarer les objets et hypothèses ; prévoir une observation ; construire l'objet et lire les figures ; produire une preuve ou un certificat ; traiter un contre-exemple**. Les calculs rationnels admissibles sont exacts ; les trajectoires, courbes et vecteurs propres approchés sont numériques. Le rendu demandé combine une figure annotée, une explication des contrôles et une démonstration lisible sans Python.

## Choisir sa porte d'entrée dans un TP

Chaque laboratoire s'ouvre sur **But du TP et lien avec le cours**. Avant de toucher un curseur, lire le phénomène à comprendre, les techniques à réinvestir et le résultat que l'on devra savoir justifier. Les leçons associées sont accessibles depuis ce bloc. Le détail **Un premier parcours en trois gestes** propose une observation, une comparaison et une conclusion à établir.

- **Sup** : entrer avec les outils de première année — systèmes, bases, matrices, polynômes, déterminants — même lorsque l'objet final est nouveau.
- **Spé** : mobiliser les outils de seconde année pour approfondir l'expérience ; les différences de filière comptent, notamment pour le polynôme minimal et la décomposition des noyaux.
- **Au-delà** : découvrir une construction ou un résultat supplémentaire, avec des définitions fournies et une preuve guidée. Ces notions ne sont pas supposées connues.

Les grandes matrices sont structurées pour éclairer une méthode ; leur traitement intégral à la main n'est pas le but de l'expérience. Les repères décrivent une progression pédagogique, à adapter à la filière. Les programmes officiels de [MPSI](https://www.education.gouv.fr/bo/21/Special1/ESRS2035779A.htm), de [MP](https://www.education.gouv.fr/bo/21/Hebdo31/ESRS2111702A.htm) et des [autres filières de seconde année](https://www.education.gouv.fr/pid285/bulletin_officiel.html?pid_bo=40451) permettent de situer les prolongements.

## Séance 1 · Des unités aux structures

**Leçons 1–3 ; exercices 1–4 ; laboratoires anneaux et géométrie.**

Préparer les définitions de groupe, anneau, corps, unité, idéal et sous-espace. Commencer avec diag(2,1), puis construire la matrice dense 4×4 de l'exercice 1 comme L diag(2,1,1,1)Lᵀ. Changer l'anneau : ℚ, ℤ, modulo 6, modulo 5. Consigner le déterminant et l'existence d'un inverse. La même matrice doit fournir quatre réponses correctement justifiées, sans remplacer « unité » par « non nul ».

Démontrer le critère matriciel par l'adjugée, puis celui des unités modulo n par Bézout. Compter les colonnes indépendantes dans GL₂(𝔽₃), et expliquer les quatre coordonnées libres d'un relèvement modulo 9. Faire apparaître 48 puis 3888 sans les obtenir par une énumération exhaustive.

Construire sur papier la table des six homographies du TP à partir des images de 0,1,∞. Comparer deux ordres de composition avec le laboratoire géométrique. Le changement de coordonnées (x,y)↦(ln x,y) donne un exemple de structure vectorielle transportée ; il faut identifier son zéro et la multiplication par le scalaire 0.

**Contrôle.** Expliquer en cinq phrases pourquoi une loi idempotente non triviale ne peut être une loi de groupe. Donner une unité modulo 8 dont l'ordre n'est pas φ(8). Pour aller plus loin : division dans ℤ[i], deux carrés, borne de commutation 5/8 et injection des groupes finis de matrices entières modulo un premier impair.

## Séance 2 · Bases, suppléments, matrices et Gauss

**Leçons 4–6 ; exercices 5–11 ; laboratoires géométrie et Gauss.**

Construire les polynômes de Lagrange des nœuds 0,1,2, puis transformer les évaluations en un système de coordonnées. Démontrer la liberté par les évaluations avant de vérifier le rang. Reprendre les suppléments du TP : fonctions d'intégrale nulle et constantes, puis division par X²+1 dans K₃[X]. Détecter pourquoi retirer le polynôme nul détruit l'espace vectoriel.

Pour une matrice représentant E→F, expliquer la taille à partir des colonnes images des vecteurs de base. Composer A et B sur un vecteur, puis contrôler les produits calculés. Définir P par ses colonnes et établir A_nouvelle=P⁻¹A_ancienneP. Garder ce choix tout au long du parcours.

Faire Gauss à la main sur les exemples 9 et 10 ; écrire le système après chaque opération. Identifier les variables libres, un point particulier, le noyau et les colonnes pivots de la matrice initiale. Prouver l'inégalité de Sylvester avec la restriction de g à Im f. La forme échelonnée ne sera jamais présentée comme une forme de Jordan.

**Contrôle.** Rendre la droite affine de solutions du système 4×4 de l'exercice 9, puis le certificat yᵀA=0,yᵀb=1 de l'exercice 10. Identifier la donnée modifiée et les trois pivots. Déterminer l'effet des opérations élémentaires sur le déterminant. Prolongement numérique : rapprocher les nœuds d'une Vandermonde et distinguer sensibilité numérique et dépendance exacte.

## Séance 3 · Projections et distances

**Leçon 7 et première lecture de la leçon 20 ; exercices 12–13 et 30, première partie ; laboratoires projecteurs et quadratiques.**

Vérifier P²=P pour une projection oblique, calculer son image et son noyau, et décomposer un vecteur. Faire varier le cisaillement et retrouver l'unique valeur donnant une projection orthogonale. Comparer la distance du vecteur à son image oblique et à son projeté orthogonal.

Démontrer E=Im P⊕Ker P et le minimum de distance par Pythagore. Passer ensuite aux matrices munies de la norme de Frobenius : calculer S=(A+Aᵀ)/2 et K=(A−Aᵀ)/2 dans l'exercice 13, établir leur orthogonalité, puis minimiser la distance à l'espace des symétriques. Sur ℂ, justifier l'emploi de l'adjoint A†.

Observer les contours de q=xᵀSx pour une forme positive, indéfinie et dégénérée. Chercher un vecteur isotrope non nul qui n'appartient pas au noyau. Cette introduction géométrique sera reprise après le théorème spectral ; elle permet déjà de différencier une forme quadratique et l'endomorphisme de même matrice.

**Contrôle.** Produire un contre-exemple chiffré à « tout projecteur donne le point le plus proche ». Démontrer la formule dist_F(A,Sym)=‖(A−Aᵀ)/2‖_F. Prolongement : relier la projection orthogonale aux moindres carrés du volet d'optimisation.

## Séance 4 · Spectre, corps et commutation

**Leçons 8–9 ; exercices 14–16 ; laboratoires spectre et projecteurs.**

Comparer la rotation de quart de tour sur ℚ, ℝ et ℂ. Écrire son polynôme caractéristique avant de chercher des vecteurs propres. Comparer ensuite I₆ et une matrice dense semblable à J₄(1)⊕J₂(1), qui ont le même polynôme caractéristique. Calculer les dimensions des espaces propres et expliquer la différence sans utiliser seulement un dessin.

Prouver qu'une matrice B commutant avec A conserve les espaces propres de A. En déduire la codiagonalisation de deux matrices diagonalisables commutantes. Pour diag(1,3), construire les projecteurs par interpolation et déterminer son commutant entier. Conjuguer cet exemple, puis observer que les projecteurs spectraux peuvent être obliques.

La collision des deux valeurs propres doit être traitée comme un changement d'hypothèses. On ne remplace pas un dénominateur nul par un nombre très petit. Le laboratoire signale le passage à un seul facteur primaire ; la séance suivante explique le rôle du polynôme minimal.

**Contrôle.** Donner un exemple diagonalisable sur ℂ mais pas sur ℝ, puis un exemple scindé et non diagonalisable. Expliquer pourquoi une matrice scalaire possède un commutant beaucoup plus grand que son algèbre de polynômes.

## Séance 5 · Cayley–Hamilton et le TP Vandermonde

**Leçons 10–11 et partie Vandermonde de la leçon 16 ; exercices 17–19 ; laboratoire Cayley.**

Construire χ et μ et clarifier leur différence. Refaire la preuve de Cayley–Hamilton par comparaison des coefficients de l'adjugée. Chaque élève doit pouvoir expliquer pourquoi les coefficients obtenus sont des polynômes en A : c'est ce qui autorise l'élimination conduisant à χ(A)=0.

Reprendre exactement la matrice du TP des nœuds 1,2,3,5. Calculer trace 137 et déterminant 48, puis s₁,…,s₄ et χ=X⁴−137X³+799X²−646X+48. Contrôler la même identité par χ(A), sans considérer ce contrôle sur une matrice comme une preuve du théorème général.

Réduire X⁴⁰ modulo (X−1)² et comparer à un binôme nilpotent. Prouver ensuite que [A,B]=A impose la nilpotence en caractéristique 0. Le contre-exemple Iₚ sur 𝔽ₚ explique précisément pourquoi le raisonnement par traces ne s'exporte pas à toute caractéristique.

**Contrôle.** Calculer une grande puissance sans multiplication matricielle répétée et justifier le reste polynomial. Énoncer les hypothèses de Jacobi avec inverse et du logarithme local. Prolongement : Faddeev–LeVerrier et dérivée du déterminant, à relier au calcul différentiel.

## Séance 6 · Dunford, Jordan et fonctions de matrices

**Leçons 12–13 ; exercices 20–22 ; laboratoire Dunford.**

Reconstituer P et A du TP imprimé p.137 ; vérifier AP=PJ avant toute conclusion. Déterminer D=I et N=A−I, l'indice de nilpotence et les chaînes. Expliciter exp(tA) avec sa somme finie. Ce premier exemple permet de voir la décomposition sans masquer la base.

Construire les projecteurs primaires par Bézout lorsque le polynôme minimal est scindé, puis démontrer existence et unicité de Dunford. Étudier les dimensions de Ker(A−λI)ᵏ pour retrouver les tailles des blocs. Distinguer la formulation diagonalisable sur K de la formulation semisimple après extension de corps.

Pour A=2I+N₃, construire un logarithme, puis l'exponentier explicitement. Déclarer le choix de logarithme scalaire, et arrêter la série grâce à N₃³=0. La théorie générale de Jordan est une extension selon la filière ; les chaînes et les formules finies peuvent se travailler sur ces exemples sans supposer ce théorème général déjà acquis.

**Contrôle.** À partir des dimensions 2,4,5,6 de noyaux successifs en dimension 6, retrouver les blocs de tailles 4 et 2. Comparer au profil 3,5,6 donnant les blocs 3,2,1. Écrire χ et μ et annoncer si la matrice est cyclique. Le preset nilpotent42 conjugue le premier exemple par une matrice rationnelle dense : les chaînes existent même lorsqu'elles ne sont plus visibles dans les coefficients. Prolongement : résolution d'un système différentiel x′=Ax et distinction entre logarithmes réels et complexes.

## Séance 7 · Krylov, compagnons, Frobenius et circulantes

**Leçons 14–16 ; exercices 23–26 ; laboratoires cyclique et Frobenius.**

Pour diag(1,2,3), tester (1,1,1) puis un vecteur propre. Une base de Krylov valide démontre l'existence d'un vecteur cyclique ; un vecteur inadéquat ne démontre pas son inexistence. Construire le compagnon 6×6 de p=(X−1)²(X+1)(X²−X−1)(X−2), établir μ=χ à partir des itérés de e₁, puis retrouver la récurrence de l'exercice 24.

Le laboratoire Frobenius propose des facteurs invariants connus puis un changement de base. Vérifier leur divisibilité, la somme des degrés, χ comme produit et μ comme dernier facteur. Comparer les familles 6×6 meme_chi_a et meme_chi_b de l'exercice 25 ; elles ont le même χ mais des minimaux de degrés 4 et 6. Reprendre ensuite les deux facteurs X²+1 sur ℚ, puis leur lecture sur ℂ. Le théorème général de structure des modules peut être admis comme extension ; l'action de X dans chaque quotient polynomial et les identités des exemples doivent être démontrées.

Prolonger par la permutation cyclique et la base de Fourier sur ℂ. Calculer les valeurs propres d'une circulante comme évaluations d'un polynôme aux racines de l'unité. Relier un compagnon à une récurrence linéaire et expliquer l'apparition des facteurs polynomiaux pour une racine répétée.

**Contrôle.** Réfuter le quantificateur « tout vecteur non nul » dans la cyclicité. Donner χ et μ des deux familles 6×6, décider laquelle est cyclique et expliquer pourquoi le corps n'a pas besoin de contenir les racines pour la forme de Frobenius.

## Séance 8 · Jacobi et représentations : des actions plutôt que des tableaux

**Leçons 17–18 et 21–22 ; exercices 27–28 et 31–34 ; laboratoires Lie, Jacobi et représentations.**

Commencer avec trois axes obliques dans so₃. Calculer x×(y×z) et les deux autres contributions ; les représenter en flèches et retrouver leur somme nulle. Passer aux générateurs denses sp₄ du laboratoire. Demander explicitement trois contributions non nulles : annuler un générateur produirait une vérification beaucoup moins instructive.

Écrire les douze produits de Jacobi, marquer les six paires opposées et déduire ad_[X,Y]=[ad_X,ad_Y] en appliquant les opérateurs à un témoin général T. Identifier l'espace de dimension n² sur lequel ad agit. Le triplet de Heisenberg rappelle qu'un élément central dans une sous-algèbre n'est pas l'identité.

Construire E,F,H par dérivation dans V₄, puis dans V₆. Le diagramme de poids explique les matrices 5×5 et 7×7. Appliquer exp(tE) à une forme et vérifier la substitution p(x,y+tx) ; comparer avec l'action de E−F. La figure du polynôme sur le cercle et le diagramme des coefficients doivent être annotés avec deux variables distinctes : point (x,y) et vecteur de coefficients.

**Livrable et correction attendue.** Fournir les trois contributions, l'expansion complète, les relations sl₂ et la chaîne de sept poids. La preuve d'irréductibilité doit utiliser les projecteurs polynomiaux de H pour isoler un monôme, puis E,F ; constater seulement que les flèches sont reliées ne suffit pas. Distinguer « puissance symétrique » et « polynôme invariant sous x↔y ». Les représentations sont un approfondissement guidé selon la filière.

## Séance 9 · Conserver une géométrie : Sp₄, Sp₆ et le pfaffien

**Leçons 19,20,23 ; exercices 29–30 et 35–36 ; laboratoires symplectique, pfaffien et quadratiques.**

Mission : décider si une méthode conserve seulement un volume, une énergie, ou la forme symplectique. Déclarer z=(q,p), l'ordre des composantes, la matrice K et le couplage relatif κ. Construire A=JK, puis montrer AᵀJ+JA=0. Le modèle proposé utilise V=diag(ω)Rκdiag(ω) ; κ ne représente pas la raideur d'un terme (q₁−q₂)².

Pour deux pulsations égales, calculer les modes (1,1),(1,−1), puis leurs pulsations ω√(1±κ). Pour trois modes de pulsations 1 et κ=1/2, calculer les valeurs 1,1±√2/2 de V. Identifier les courbes q₁,q₂,q₃ et expliquer ce que montre une projection d'un état de dimension 6.

Comparer sur le même horizon Euler explicite et Cayley. Prouver le défaut h²AᵀJA d'Euler et l'identité symplectique de Cayley avec B=I−hA/2,D=I+hA/2. Prouver aussi la conservation de K dans ce modèle quadratique. Diminuer h et observer l'erreur de phase 2 arctan(hω/2)−hω par mode. Une énergie constante ne prouve pas une trajectoire exacte.

Calculer le pfaffien sur 15 puis 105 appariements en dimensions 6 et 8, observer le signe quand det P change de signe et le rang quand P devient singulière. La preuve de congruence puis Pf(MᵀJM)=det M·Pf J donne det M=1. La matrice diag(2,1,1,1/2) montre que la réciproque échoue en dimension 4. Revenir à l'inertie et au lien Hessienne/convexité pour rattacher l'application à l'optimisation.

**Livrable et correction attendue.** Une construction 4×4 ou 6×6, deux contrôles exacts (J,K), une figure de trajectoires, une courbe d'énergie et une estimation de phase. Énoncer le domaine d'inversibilité de Cayley. La conservation exacte d'une énergie quadratique ne doit pas être annoncée pour tout Hamiltonien non linéaire. Les groupes symplectiques et le pfaffien restent des extensions guidées.

## Séance 10 · Deux graphes, deux évolutions : Markov et diffusion

**Leçons 24–25 ; exercices 37–40 ; laboratoires Markov et réseaux.**

Commencer par les six états des deux triangles orientés. Déclarer la convention colonne Pᵢⱼ=j→i, les probabilités p et les paramètres bridge,bias,teleport. Identifier ce qui change dans le graphe, les six courbes de probabilité et les flux stationnaires. Tester d'abord l'absence de liaison, puis un pont faible, puis la téléportation.

Mission Markov : contrôler la positivité et les sommes de colonnes, repérer les classes, résoudre (P−I)π=0 avec 1ᵀπ=1 et vérifier les flux. Le maintien positif assure l'apériodicité de chaque classe, mais pas l'irréductibilité. Les deux triangles séparés ont une famille de stationnaires ; l'irréductibilité rétablie donne une stationnaire unique. Un biais de cycle peut produire des flux non réversibles malgré la convergence. L'exemple théorique du cycle 6 et saut uniforme montre séparément une formule fermée de Pᵏ ; il ne se confond pas avec la famille des triangles.

Passer aux huit sommets des deux K₄ reliés par un pontη. Les variables u sont un contraste de température ou un signal signé, pas automatiquement des probabilités. Former L=B diag(w)Bᵀ et prouver sa positivité. Déterminer le nombre de composantes par le noyau, puis prédire le mode lent à partir du quotient de Rayleigh.

Mission réseau : démontrer λ₂≤η/2 avec le vecteur constant ±1/√8, calculer τ=256η par les arbres et contrôler le cofacteur 7×7. Pour η=1/4, expliquer pourquoi 64 est une somme pondérée alors que le graphe non pondéré compte 256 arbres. Étudier exp(−tL)u₀ et montrer conservation de moyenne et décroissance de norme. Quand η=0, le contraste entre les blocs ne diffuse pas.

**Livrable et correction attendue.** Deux graphes annotés, les matrices 6×6 et 8×8 reliées à leurs sommets, une preuve de stationnarité, une distinction stationnarité/réversibilité, une borne de Fiedler et un calcul de cofacteur. Le signe d'un vecteur de Fiedler ne prouve pas une partition optimale, et une valeur propre multiple rend ce vecteur non unique. Ces applications utilisent les outils de SPÉ ; leurs théorèmes généraux sont des approfondissements à adapter à la filière.

## Traces d'apprentissage et évaluation

Pour chaque TP, conserver l'anneau ou le corps, l'exemple initial, une conjecture, un contrôle exact, une démonstration et un contre-exemple supprimant une hypothèse. Les preuves doivent pouvoir être écrites sans Python ; le programme apporte les illustrations, les variations de paramètres et des certificats lisibles.

Une évaluation courte peut mêler quatre questions : résoudre un système exact, décider d'une réduction sur deux corps, construire un polynôme en A, expliquer une distinction géométrique. Une évaluation de synthèse peut reprendre le TP Vandermonde ou Dunford, puis introduire une matrice ayant le même χ et un μ différent. Une seconde synthèse peut demander de reconstruire les matrices d'un oscillateur ou d'un graphe depuis les objets. Les corrigés des **40 exercices** restent accessibles après une recherche autonome.
