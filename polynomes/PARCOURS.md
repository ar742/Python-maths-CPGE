# Dix-huit séances de polynômes et géométrie

Pour les complexes et les polynômes à plusieurs variables, commencer par le [parcours progressif sup / spé](PARCOURS_PROGRESSIF.md) : huit séances prioritaires, puis des approfondissements et des prolongements facultatifs. Le présent document rassemble les guides des 36 TP.

Pour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par une identité exacte, un certificat ou une démonstration.

## Séance 01 — Fractions & Interpolation

### Décomposer la fraction du recueil

Décomposer une fraction comportant un pôle triple, puis vérifier la recomposition.

**Objets et paramètres**

- X est l’indéterminée ; x est une valeur réelle pour le graphique. F=P/Q est la fraction rationnelle.
- s est la translation des pôles : s−1 et s+2. A,B,C,D sont les coefficients des quatre termes polaires.
- La partie entière est le quotient polynomial de P par Q. Un pôle d’ordre m conserve (X−a)^m au dénominateur après simplification.

**Repères** — Sup : Sup : éléments simples sur ℝ et ℂ, division euclidienne. Spé : Spé : réinvestissement dans les intégrales, séries et systèmes linéaires. Au-delà : Les résidus complexes sont introduits dans le TP de regroupement ; aucune intégrale de contour n’est requise.

1. Reprendre le preset de l’exercice 4 et vérifier la partie entière 1.
2. Mettre D=0, puis C=0 : prévoir les ordres restants.
3. Translater les pôles avec s et vérifier que les coefficients polaires ne changent pas.

**À justifier :** La partie entière décrit le comportement polynomial ; les puissances négatives décrivent chaque pôle.

### Extraire une partie polaire par Taylor

Retrouver une décomposition par les dérivées au point du pôle.

**Objets et paramètres**

- g(X)=X⁴+cX²+X+1 est le numérateur ; c est son coefficient réglable.
- a est le point où le dénominateur s’annule ; m est sa puissance entière, de 2 à 5.
- A_k est le coefficient de (X−a)^−k, pour 1≤k≤m ; g^(j)(a) est la dérivée d’ordre j évaluée en a.

**Repères** — Sup : Sup : dérivées, multiplicité, éléments simples. Spé : Spé : réinvestir Taylor dans les calculs locaux. Au-delà : Développement de Laurent : les puissances négatives sont déjà visibles ici, sans théorie des fonctions holomorphes.

1. Avec m=3, retrouver les coefficients g(a), g′(a), g″(a)/2.
2. Choisir a=−1 et c=−1, puis vérifier g(a)=0.
3. Passer à m=5 : le numérateur de degré quatre ne produit aucune partie entière.

**À justifier :** Chaque coefficient polaire correspond à une dérivée ; l’annulation de coefficients révèle la multiplicité commune.

## Séance 02 — Fractions & Interpolation

### Regrouper des pôles complexes conjugués

Passer d’une décomposition complexe à une écriture réelle.

**Objets et paramètres**

- a est la partie réelle des deux pôles, b>0 leur distance à la droite réelle ; α=a+ib.
- u,v,w sont les coefficients réels de F=(uX+v)/[(X−a)²+b²]+w/(X−2).
- c_α est le coefficient de 1/(X−α) ; la barre signifie conjugaison. Re(z), Im(z) sont les coordonnées d’un nombre complexe z.

**Repères** — Sup : Sup : fractions rationnelles sur ℝ et ℂ. Spé : Spé : réinvestir les couples conjugués dans les équations différentielles. Au-delà : Le mot résidu désigne ici un coefficient d’élément simple ; le théorème des résidus n’est pas utilisé.

1. Avec a=0,b=1, factoriser X²+1.
2. Comparer les parties imaginaires opposées des deux coefficients.
3. Mettre w=0 et vérifier la disparition du pôle réel.

**À justifier :** Deux termes complexes conjugués reconstruisent une fraction réelle.

### Reconnaître un trou et un pôle

Décider si un point interdit admet une limite finie.

**Objets et paramètres**

- La fraction initiale est F=(X−a)^k(X²+1)/[(X−a)^m(X−b)(X²+1)].
- a,b sont les deux points interdits réels ; k,m sont des multiplicités entières positives.
- La fraction réduite est obtenue par suppression du PGCD. Un trou est un point interdit où la limite de la formule réduite est finie.

**Repères** — Sup : Sup : limites, factorisation et fractions rationnelles. Spé : Spé : singularités éliminables et prolongements continus. Au-delà : Interprétation dans le corps ℝ(X), où une fraction est une classe d’écritures équivalentes.

1. Prendre k=m et a≠b : distinguer les deux points interdits.
2. Prendre k<m : constater une divergence en a.
3. Choisir a=b puis comparer k avec m+1.

**À justifier :** L’égalité de fractions rationnelles et l’égalité de fonctions sur leur domaine initial sont à distinguer.

## Séance 03 — Fractions & Interpolation

### Choisir les nœuds d’une interpolation

Évaluer un polynôme interpolateur et distinguer interpolation et approximation.

**Objets et paramètres**

- n est le degré maximal ; les n+1 nœuds x_i sont distincts dans [−1,1].
- f(x)=1/(1+cx²) est la fonction de Runge ; c>0 est son paramètre. P_n prend les valeurs f(x_i).
- La matrice de Vandermonde contient les puissances des nœuds ; son conditionnement mesure la sensibilité du système dans la base des monômes.
- L’erreur affichée est max |P_n−f| sur une grille de 1001 points.

**Repères** — Sup : Sup : polynômes de Lagrange, systèmes linéaires et déterminants. Spé : Spé : approximation, normes et stabilité d’un calcul. Au-delà : Phénomène de Runge et formule barycentrique, introduits avec leur mécanisme.

1. Choisir n=14 avec les nœuds équidistants et observer les extrémités.
2. Passer aux nœuds de Tchebychev sans changer le degré.
3. Diminuer n et c ; comparer l’erreur et le conditionnement.

**À justifier :** Un polynôme peut satisfaire exactement toutes les contraintes et mal approcher la fonction entre les nœuds.

### Relier une base orthogonale à une quadrature

Relier trois familles du recueil aux espaces préhilbertiens et à l’intégration.

**Objets et paramètres**

- n est le degré du polynôme ; k est la puissance du moment ∫x^k w(x)dx à vérifier.
- P_n est Legendre, Tchebychev T_n ou Hermite probabiliste H_n, selon le choix.
- w(x) est le poids : 1 sur [−1,1], 1/√(1−x²) sur ]−1,1[, ou exp(−x²/2) sur ℝ.
- x_i sont les n racines de P_n ; W_i sont les poids positifs de quadrature. Le carré de la norme est ∫P_n²w.

**Repères** — Sup : Sup : produits scalaires, bases orthogonales, intégration. Spé : Spé : espaces préhilbertiens et familles de polynômes. Au-delà : Quadrature de Gauss : formule et justification accompagnées.

1. Avec Legendre et n=6, comparer les moments k=10 et k=11.
2. Choisir k=12 et observer la perte de garantie.
3. Passer à Hermite : retrouver le moment gaussien d’ordre dix.

**À justifier :** L’orthogonalité donne des racines entrelacées et une quadrature exacte jusqu’au degré 2n−1.

## Séance 04 — Arithmétique & Divisibilité

### Euclide : du reste au certificat de Bézout

Obtenir un PGCD et savoir le justifier par des divisions puis par une identité de Bézout.

**Objets et paramètres**

- X est l’indéterminée; x est une valeur réelle utilisée uniquement dans les dessins.
- A et B sont les polynômes de départ; t translate X en X−t, et c multiplie A.
- Q et R sont le quotient et le reste d’une division A=BQ+R. D est le PGCD unitaire, U et V ses coefficients de Bézout : AU+BV=D.
- Les degrés sont des entiers; le degré du polynôme nul vaut −∞ et n’est pas dessiné.

**Repères** — Sup : Division des polynômes, divisibilité, PGCD et Bézout. Spé : Applications aux congruences et aux fractions rationnelles. Au-delà : Algorithmes efficaces et calculs dans d’autres corps.

1. Choisir le facteur quadratique commun et prévoir le PGCD.
2. Lire la première division, puis vérifier son reste par multiplication.
3. Choisir le TP X⁴ : retrouver le reste par ses valeurs en 1, 2 et 3.

**À justifier :** Le dernier reste non nul donne le PGCD après normalisation; le certificat AU+BV=D est vérifiable sans faire confiance à l’algorithme.

### Gauss : contenu et preuves d’irréductibilité

Distinguer divisibilité, contenu entier et critère d’irréductibilité, puis éviter un raisonnement fondé seulement sur les racines.

**Objets et paramètres**

- A et B ont des coefficients entiers. c(A) est le PGCD positif de ces coefficients; A/c(A) est sa partie primitive.
- n est le degré de la famille d’Eisenstein, p un nombre premier et t une translation entière. c multiplie le polynôme primitif.
- La famille est (X−t)ⁿ+p(X−t)+p. La substitution X→X+t fait apparaître les coefficients du critère.
- Les réglages n, p et t concernent la famille d’Eisenstein; c agit dans les trois exemples.

**Repères** — Sup : Divisibilité, racines et factorisation dans ℚ[X]. Spé : Arguments de réduction et de changement de variable dans un exercice guidé. Au-delà : Irréductibilité et anneaux factoriels.

1. Avec c=3, vérifier c(AB)=c(A)c(B).
2. Translater l’exemple d’Eisenstein et lire les coefficients modulo p.
3. Choisir X⁴+4 : factoriser avant de conclure à partir des racines.

**À justifier :** Le contenu ne change pas les facteurs non constants sur ℚ. Une preuve d’irréductibilité exige plus que l’absence de racines en degré 4.

## Séance 05 — Arithmétique & Divisibilité

### Inverser dans une algèbre quotient

Transformer Bézout en un inverse calculable et repérer ce qui bloque l’inversion.

**Objets et paramètres**

- K est le corps choisi : ℚ ou Fₚ, où p est premier. M est le polynôme imposant la relation M(X)=0 dans le quotient.
- A=X²+aX+b est l’élément à inverser; a et b sont des coefficients entiers réduits modulo p sur Fₚ.
- La classe de P regroupe tous les polynômes P+MQ. Elle possède un représentant de degré inférieur à deg M.
- U et V sont les coefficients de Bézout; D=PGCD(A,M). Les quatre coordonnées suivent la base 1,X,X²,X³.

**Repères** — Sup : Bézout et calculs de restes. Spé : Algèbre linéaire : multiplication par une classe comme endomorphisme. Au-delà : Algèbres quotient et construction de corps finis.

1. Trouver l’inverse rationnel par le tableau et vérifier le produit modulo M.
2. Choisir M=(X²+1)(X²+X+1) et A=X²+1.
3. Passer sur F₂ et refaire la division avec des coefficients réduits.

**À justifier :** Une classe est inversible exactement lorsque A et M sont premiers entre eux. Un facteur commun fournit un élément non nul annulé par A.

### Restes chinois : recoller deux congruences

Remplacer deux congruences par un seul polynôme et comprendre la condition de compatibilité.

**Objets et paramètres**

- M₁ et M₂ sont les modules polynomiaux. R₁ et R₂ sont les restes prescrits, réglés par les entiers a et b.
- S est la solution recherchée. S≡Rᵢ modulo Mᵢ signifie Mᵢ|S−Rᵢ.
- D=PGCD(M₁,M₂) et L=PPCM(M₁,M₂). E₁ et E₂ sont les idempotents lorsque D=1.
- Un idempotent E vérifie E²≡E modulo L : il sélectionne une des deux conditions.

**Repères** — Sup : Divisibilité, Bézout et congruences par analogie avec l’arithmétique. Spé : Interpolation, décomposition d’espaces et projecteurs. Au-delà : Théorème des restes chinois pour les anneaux et les algèbres.

1. Reconstituer S dans le cas premier entre eux et contrôler ses deux restes.
2. Observer E₁ et E₂; retrouver S≡R₁E₁+R₂E₂.
3. Comparer les deux cas ayant le facteur X−1 en commun et évaluer les restes en 1.

**À justifier :** Le PGCD contrôle l’existence; le PPCM contrôle l’unicité de la classe solution.

## Séance 06 — Arithmétique & Divisibilité

### Möbius : inverser une somme sur les diviseurs

Défaire une somme sur les diviseurs, avec une vérification entière terme par terme.

**Objets et paramètres**

- n est un entier positif et d parcourt ses diviseurs positifs. p désigne un nombre premier dans la définition de μ.
- μ est la fonction de Möbius : 1 en n=1, 0 si n a un facteur carré, (−1)ʳ si n a r facteurs premiers distincts.
- g est la fonction choisie; f(n)=Σ_{d|n}g(d). φ(n) compte les entiers entre 1 et n premiers avec n.
- k n’intervient que dans la famille g(n)=nᵏ. χ est l’unité de la convolution : χ(1)=1, χ(n)=0 pour n>1.

**Repères** — Sup : Divisibilité, PGCD et factorisation des entiers. Spé : Réorganisation de sommes finies et preuves par regroupement. Au-delà : Fonctions arithmétiques et formule de Möbius, accompagnées.

1. Choisir n=30 et repérer les signes des huit diviseurs.
2. Passer à n=36 : observer l’annulation de μ pour les diviseurs contenant un carré.
3. Choisir g=φ et vérifier que f(n)=n, puis inverser cette identité.

**À justifier :** Les contributions signées éliminent les doubles comptages; la convolution avec μ inverse la somme des diviseurs.

### Compter les irréductibles sur Fₚ

Retrouver le nombre d’irréductibles de degré n et vérifier le passage entre nombre de facteurs et nombre de racines.

**Objets et paramètres**

- p est premier; Fₚ est le corps des p résidus. n est un degré positif.
- Iₚ(n) est le nombre de polynômes unitaires irréductibles de degré n dans Fₚ[X].
- μ(d) est la fonction de Möbius et d parcourt les diviseurs positifs de n.
- Il y a pⁿ polynômes unitaires de degré n, car leurs n coefficients non dominants sont libres.

**Repères** — Sup : Polynômes unitaires, factorisation et raisonnement sur le degré. Spé : Bézout et irréductibilité; réorganisation de sommes. Au-delà : Corps finis et dénombrement de leurs polynômes, accompagnés.

1. Prendre p=2,n=2 et vérifier les quatre polynômes candidats.
2. Choisir p=2,n=6; lire les quatre diviseurs de 6 et la somme signée.
3. Prendre p=5,n=2; comparer formule et liste des dix irréductibles.

**À justifier :** Le facteur d dans ΣdIₚ(d) compte les racines de chaque irréductible. Möbius isole le degré recherché.

## Séance 07 — Arithmétique & Divisibilité

### Frobenius : factoriser X^(pⁿ)−X

Relier une factorisation exacte, une dérivée constante et la construction d’un corps fini.

**Objets et paramètres**

- p est premier, n≥1 et P=X^(pⁿ)−X appartient à Fₚ[X].
- Fₚ désigne le corps de base à p éléments; F_(pⁿ) désigne un corps extension à pⁿ éléments.
- d est le degré d’un facteur irréductible Q; sa multiplicité est son nombre d’apparitions dans P.
- Le Frobenius est l’application a→aᵖ. Le deuxième graphique montre uniquement son action sur le corps de base Fₚ.

**Repères** — Sup : Dérivation et multiplicité des racines en caractéristique zéro. Spé : PGCD(P,P′) comme critère de simplicité des racines. Au-delà : Caractéristique positive, Frobenius et corps finis, accompagnés.

1. Choisir p=2,n=3 : prévoir des facteurs de degrés 1 et 3 seulement.
2. Lire P′ et vérifier que toutes les multiplicités valent 1.
3. Passer à n=4; expliquer pourquoi des facteurs de degré 2 apparaissent.

**À justifier :** La dérivée −1 interdit les facteurs répétés; les degrés autorisés sont exactement les diviseurs de n.

### Cyclotomie : racines de l’unité et Möbius

Reconnaître l’ordre exact d’une racine de l’unité et obtenir un polynôme entier par inversion sur les diviseurs.

**Objets et paramètres**

- n≥2 est l’ordre choisi; k parcourt les entiers de 0 à n−1. ζₖ=exp(2πik/n) est une racine de Xⁿ−1.
- ζₖ est primitive si son ordre multiplicatif est exactement n; cela équivaut à PGCD(k,n)=1.
- Φₙ est le polynôme unitaire dont les racines sont les racines primitives d’ordre n. Son degré est φ(n).
- d parcourt les diviseurs de n et μ est la fonction de Möbius. Un exposant −1 dans le produit désigne un dénominateur qui se simplifie exactement.

**Repères** — Sup : Forme exponentielle des complexes, racines n-ièmes et factorisation. Spé : Arithmétique et relations entre racines et coefficients. Au-delà : Polynômes cyclotomiques, irréductibilité et extensions algébriques.

1. Prendre n=12 et sélectionner les quatre racines primitives.
2. Lire X¹²−1=∏Φ_d pour d|12, puis le produit de Möbius.
3. Prendre n=30 : comparer φ(n), le degré et le nombre de points primitifs.

**À justifier :** Les racines de Xⁿ−1 se répartissent selon leur ordre; cette partition construit les Φ_d et rend le quotient de Möbius exact.

## Séance 08 — Arithmétique & Divisibilité

### Bernoulli : transformer une somme en polynôme

Calculer une somme de puissances par télescopage, en gardant une convention unique pour les nombres de Bernoulli.

**Objets et paramètres**

- p≥1 est la puissance des termes; N est le dernier entier sommé. Sₚ(N)=Σ_{k=0}^N kᵖ.
- Bₘ(X) est le polynôme de Bernoulli de degré m; bₘ=Bₘ(0), avec b₁=−1/2.
- Les polynômes sont définis par B₀=1, Bₘ′=mBₘ₋₁ et ∫₀¹Bₘ=0 pour m≥1.
- a est la translation du deuxième dessin Bₚ₊₁(x+a); elle ne modifie pas la somme Sₚ(N).

**Repères** — Sup : Sommes finies, binôme, dérivation et primitive d’un polynôme. Spé : Preuves par récurrence et méthodes de sommation. Au-delà : Nombres de Bernoulli, génératrices et formule de Faulhaber.

1. Retrouver B₂(X) à partir de sa dérivée et de son intégrale nulle.
2. Choisir p=3 et vérifier la formule classique des cubes.
3. Choisir p=7 puis changer N; vérifier l’égalité exacte des deux calculs.

**À justifier :** La différence Bₚ₊₁(X+1)−Bₚ₊₁(X) est (p+1)Xᵖ; le télescopage transforme la somme en une évaluation de polynôme.

### Euler–Maclaurin : corriger une intégrale

Estimer une somme par une intégrale et savoir jusqu’où une correction peut être garantie.

**Objets et paramètres**

- f est la fonction choisie : 1/x, exp(−x/3) ou xᵈ. x est réel et j est l’indice entier de la somme.
- N≥2 est la borne supérieure; S=Σ_{j=1}^Nf(j) inclut 1 et N.
- k est le nombre de corrections de Bernoulli; b₂ᵢ=B₂ᵢ(0) est un nombre rationnel.
- Rₖ est le reste entre S et l’expression corrigée. d n’intervient que pour la fonction polynomiale.

**Repères** — Sup : Primitives, sommes et comparaison avec une intégrale. Spé : Formules de Taylor, intégrations par parties et contrôle d’erreur. Au-delà : Euler–Maclaurin, développements asymptotiques et nombres de Bernoulli.

1. Choisir 1/x et comparer l’intégrale seule à la correction des extrémités.
2. Ajouter k=1 puis k=2 et lire l’erreur avec sa borne.
3. Choisir x⁶, k=3 : expliquer pourquoi la somme devient exacte.

**À justifier :** Une correction est utile lorsqu’elle réduit une erreur contrôlée. Pour un polynôme, assez de dérivées nulles donnent une formule exacte.

## Séance 09 — Racines & Plan complexe

### Racines de l’unité et sommes de tangentes

Résoudre l’exercice 5 de la page 31 puis relier ses tangentes aux coefficients d’un polynôme.

**Objets et paramètres**

- n est un entier positif; le réglage commence à n=2. Pₙ(Z)=(Z+1)²ⁿ−(Z−1)²ⁿ est un polynôme en l’indéterminée Z.
- z est une solution complexe; w=(1+z)/(1−z) est le nouveau complexe lorsque z≠1.
- k numérote les racines de l’unité wₖ=e^(ikπ/n). Leur image αₖ=i tan(kπ/(2n)) est une racine de Pₙ.
- Re et Im désignent les parties réelle et imaginaire. Toutes les quantités sont sans unité.

**Repères** — Sup : Sup : complexes, racines de l’unité et formule du binôme. Spé : Spé : exploiter une factorisation et comparer les coefficients. Au-delà : Transformation de Cayley et point à l’infini; les calculs utilisés restent élémentaires.

1. Choisir n=2 et écrire P₂ à la main.
2. Retrouver les trois racines 0, i et −i.
3. Passer à n=5 et prévoir la somme puis le produit des tangentes non nulles.

**À justifier :** Le degré est 2n−1, le coefficient dominant 4n; le changement de variable ne fournit que 2n−1 racines finies.

### Une somme géométrique dessine un cercle

Résoudre en une seule fois une famille de polynômes, puis transporter ses racines dans le plan.

**Objets et paramètres**

- n est le degré; c est un centre complexe, r un rayon réel strictement positif.
- Pₙ(Z)=Σⱼ₌₀ⁿ((Z−c)/r)ʲ. On pose t=(Z−c)/r pour utiliser une somme géométrique.
- αₖ=c+r e^(2ikπ/(n+1)), pour 1≤k≤n, sont les racines. Le point c+r n’est pas une racine.
- Les coefficients et les racines sont sans unité.

**Repères** — Sup : Sup : sommes géométriques, racines de l’unité et polynômes complexes. Spé : Spé : factorisation d’une famille et contrôle des constantes. Au-delà : Transport des racines; coefficients non réels lorsque Im(c)≠0.

1. Garder c=−1, r=2 et n=3; prévoir les quatre candidats.
2. Identifier le candidat exclu grâce à Pₙ(c+r)=n+1.
3. Donner une partie imaginaire à c : suivre le cercle et les racines.

**À justifier :** Les n racines sont simples et situées sur un cercle; la factorisation comporte le facteur dominant r^(−n).

## Séance 10 — Racines & Plan complexe

### Six racines et une borne de Cauchy

Encadrer les racines d’un polynôme complexe de degré 6 par des inégalités prouvées.

**Objets et paramètres**

- P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i). Les réglages donnent les parties réelles et imaginaires de a et b.
- Dans P=Σₖ₌₀⁶aₖZᵏ, a₆=1. α₁,…,α₆ sont les racines comptées avec multiplicité.
- ρ est l’unique racine positive de Q(r)=r⁶−Σₖ₌₀⁵|aₖ|rᵏ. M=max|αₖ| est le plus grand module.
- Le résidu d’une racine approchée α est |P(α)|; ce n’est pas automatiquement son erreur de position.

**Repères** — Sup : Sup : modules, factorisation sur ℂ et étude de fonctions. Spé : Spé : bornes sur une famille de racines; exercice 9 de M17. Au-delà : Localisation plus fine et conditionnement des racines.

1. Lire les six racines et le disque de rayon ρ.
2. Faire varier Im(a) : observer l’absence de symétrie obligatoire.
3. Comparer M au petit rayon (2^(1/6)−1)ρ : seule la plus éloignée est concernée.

**À justifier :** La borne supérieure vaut pour chaque racine; la borne inférieure vaut pour le maximum de leurs modules.

### Compter les racines dans un disque

Distinguer un comptage numérique d’un certificat valable sur un cercle entier.

**Objets et paramètres**

- P(Z)=Z⁵+aZ²+b, avec a et b complexes; R>0 est le rayon du disque ouvert |z|<R.
- On écrit P=f+g. Le terme f=cZᵏ est choisi parmi Z⁵, aZ² et b; g regroupe les deux autres.
- Sur |z|=R, |f|=|c|Rᵏ. La somme des modules des autres termes fournit un majorant de |g|.
- La marge est |f| moins ce majorant. Le nombre de racines est compté avec multiplicité.

**Repères** — Sup : Sup : modules, polynômes et contrôle des hypothèses. Spé : Spé : réinvestir les inégalités; le théorème est fourni comme prolongement. Au-delà : Rouché et analyse complexe; hors du socle CPGE courant.

1. Choisir le premier exemple : vérifier |a|>1+|b| pour R=1.
2. Passer à R=2 et prévoir un autre terme dominant.
3. Prendre R=1,6 : lire pourquoi ce critère ne donne plus de certificat.

**À justifier :** Une inégalité analytique sur tout le bord certifie le comptage; une courbe échantillonnée ne suffit pas.

## Séance 11 — Racines & Plan complexe

### La dérivée reste dans l’enveloppe convexe

Prolonger l’interlacement réel des racines par une propriété géométrique du plan complexe.

**Objets et paramètres**

- α₁,…,α₅ sont cinq racines complexes données. P(Z)=∏ₖ₌₁⁵(Z−αₖ); le réglage déplace α₅.
- β₁,…,β₄ sont les racines de P′, triées par parties réelle puis imaginaire pour les numéroter.
- L’enveloppe convexe est le plus petit ensemble convexe contenant les αₖ; le dessin montre son polygone.
- Lorsque P(β)≠0, les poids λₖ sont proportionnels à 1/|β−αₖ|² et leur somme vaut 1.

**Repères** — Sup : Sup : dérivation des polynômes et racines multiples; convexité du plan. Spé : Spé : combiner identité algébrique et preuve géométrique. Au-delà : Théorème de Gauss–Lucas, prolongement fourni et démontré.

1. Observer les racines de P′ à l’intérieur du polygone.
2. Déplacer α₅ très loin puis vers l’intérieur.
3. Choisir une racine β de P′ et vérifier les cinq poids positifs de son barycentre.

**À justifier :** Les racines de P′ restent dans l’enveloppe convexe des racines de P, même sans coefficients réels.

### Réciproque conjugué et cercle unité

Distinguer le réciproque réel du réciproque conjugué complexe et traiter correctement une racine nulle.

**Objets et paramètres**

- P(Z)=Σₖ₌₀⁵aₖZᵏ a cinq racines données et un coefficient dominant 1+0,4i.
- Le réciproque conjugué de degré ambiant 5 est P*(Z)=Σₖ₌₀⁵conj(a₅₋ₖ)Zᵏ.
- La racine mobile α₁=ρe^(iθ) est réglée par son module ρ et son argument θ, en degrés.
- Une racine non nulle α est envoyée vers 1/conj(α); le cercle unité est |z|=1.

**Repères** — Sup : Sup : calcul complexe, racines et coefficients. Spé : Spé : identités de polynômes et cas limites. Au-delà : Polynômes autoinversifs et localisation sur le cercle unité.

1. Choisir ρ=0,7 : vérifier que le module de l’image vaut 1/ρ.
2. Choisir ρ=1 : observer une racine fixe.
3. Choisir ρ=0 : lire la perte de degré et la convention nécessaire au second retournement.

**À justifier :** Le module s’inverse, l’argument se conserve; zéro exige un traitement séparé du degré.

## Séance 12 — Racines & Plan complexe

### Viète et Newton avec des coefficients complexes

Calculer des sommes de puissances sans résoudre un polynôme complexe de degré 6.

**Objets et paramètres**

- P(Z)=Z⁶+aZ⁴+(1+i)Z²+bZ+(0,5−0,8i). Les réglages donnent a et b complexes.
- On écrit aussi P=Z⁶+c₁Z⁵+⋯+c₆; c₁=0, c₂=a, c₃=0, c₄=1+i, c₅=b et c₆=0,5−0,8i.
- α₁,…,α₆ sont les racines avec multiplicité. sₖ=Σⱼ₌₁⁶αⱼᵏ est la somme de puissances d’ordre k.
- m choisit la somme sₘ affichée; toutes les quantités sont sans unité.

**Repères** — Sup : Sup : somme, produit et coefficients d’un polynôme scindé. Spé : Spé : relations déterminant–traces et calcul de sommes de puissances. Au-delà : Fonctions symétriques et lien avec le spectre d’un endomorphisme.

1. Choisir m=1 et justifier s₁=0.
2. Choisir m=4 : calculer s₄=2a²−4(1+i) avant de lire le résultat.
3. Passer à m=8 : utiliser la récurrence sans terme 8c₈.

**À justifier :** Les coefficients déterminent les sommes; résoudre les racines n’est utile que comme vérification numérique.

### Quatre racines, quatre bassins de Newton

Comprendre la portée locale de Newton et la dépendance au point initial dans le plan complexe.

**Objets et paramètres**

- P est un polynôme complexe de degré 4, donné par quatre racines simples α₁,…,α₄. P′ est sa dérivée.
- z₀ est un point de départ complexe; zₖ₊₁=zₖ−P(zₖ)/P′(zₖ) lorsque le dénominateur n’est pas nul.
- N est le nombre maximal d’itérations; le maillage comporte M points par côté dans une fenêtre carrée.
- Une couleur signifie qu’une racine est atteinte à distance inférieure à 10⁻⁶. « Non classé » est une cinquième catégorie.
- L’orbite choisie utilise les réglages Re(z₀), Im(z₀); le résidu est |P(zₖ)|.

**Repères** — Sup : Sup : dérivation des polynômes et suites récurrentes. Spé : Spé : Newton pour un problème réel; cette carte complexe est un prolongement. Au-delà : Bassins d’attraction et frontières en dynamique complexe.

1. Repérer les quatre racines et leurs couleurs.
2. Déplacer z₀ de part et d’autre d’une frontière et suivre les orbites.
3. Réduire N puis l’augmenter : comparer la catégorie non classée.

**À justifier :** Newton converge vite près d’une racine simple, mais une fenêtre et un nombre d’itérations finis ne donnent pas un théorème global.

## Séance 13 — Racines & Plan complexe

### Deux racines proches amplifient une perturbation

Voir pourquoi deux racines proches rendent leur calcul sensible, puis traiter la racine double avec une formule exacte.

**Objets et paramètres**

- c=0,2+0,3i est le centre fixe; δ≥0 est la demi-distance initiale entre c−δ et c+δ.
- Q(Z) est le produit des trois facteurs correspondant aux racines fixes −2+0,4i, 1,7+1,3i et 1−1,9i.
- Pδ(Z)=[(Z−c)²−δ²]Q(Z). Sa perturbation est Pδ,η=[(Z−c)²−δ²−η]Q(Z).
- η=εe^(iφ), où ε=10ᵉ>0 et φ est l’argument réglé en degrés. La formule exacte des racines mobiles est c±√(δ²+η).

**Repères** — Sup : Sup : racines d’une équation quadratique complexe et multiplicité. Spé : Spé : développements limités et comparaison d’échelles. Au-delà : Conditionnement numérique des racines et coalescence.

1. Commencer avec δ=0,4 et ε=10⁻⁶; comparer au premier ordre ε/(2δ).
2. Diminuer δ jusqu’à √ε : repérer la perte de validité du premier ordre.
3. Fixer δ=0 : vérifier un déplacement √ε, quel que soit l’argument φ.

**À justifier :** Deux racines simples bien séparées réagissent linéairement; une racine double peut se séparer à l’échelle √ε.

### Une récurrence, deux racines caractéristiques

Résoudre une récurrence de polynômes avec ses véritables données initiales, y compris lorsque les racines caractéristiques se confondent.

**Objets et paramètres**

- n est un rang entier et λ=e^(iθ) un complexe de module 1; θ se règle en degrés.
- P₀(Z)=1, P₁(Z)=2λZ, Pₖ₊₂(Z)+λZPₖ₊₁(Z)+Pₖ(Z)=0. λ=1 retrouve l’exercice 6 de M17.
- z est le point complexe d’évaluation; t=λz. Les racines caractéristiques r₊, r₋ vérifient r²+tr+1=0.
- Pour les racines distinctes, A et B sont les constantes donnant Pₙ(z)=Ar₊ⁿ+Br₋ⁿ. Elles sont fixées par P₀ et P₁.

**Repères** — Sup : Sup : suites récurrentes et polynômes; le cas complexe prolonge le calcul réel. Spé : Spé : représentation d’une famille et identité polynomiale. Au-delà : Stabilité du calcul près de racines caractéristiques confondues.

1. Choisir λ=1 et calculer P₂=−2Z²−1 à la main.
2. Fixer z=2 : vérifier la formule avec une racine caractéristique double.
3. Changer θ : observer la rotation des racines et les coefficients non réels.

**À justifier :** L’équation caractéristique ne suffit pas : les deux valeurs initiales déterminent la famille et la forme du cas double.

## Séance 14 — Plusieurs variables & Géométrie

### Lire les monômes dans un plan d’exposants

Lire un polynôme à deux indéterminées sans confondre ses différents degrés.

**Objets et paramètres**

- x et y sont les deux indéterminées. Les coordonnées du dessin principal sont i et j, les exposants du monôme xⁱyʲ ; ce ne sont pas des valeurs de x et y.
- P(x,y)=xᵐ+ax²yᑫ+yⁿ+c. Les entiers m,n,q fixent des exposants ; a et c sont des coefficients réels, sans unité.
- Le support est l’ensemble des couples (i,j) dont le coefficient est non nul. Le polygone de Newton est leur enveloppe convexe.
- Le degré total est le maximum de i+j ; les degrés partiels sont les maximums de i puis de j. Les courbes secondaires sont les tranches y=0 et y=1.

**Repères** — Sup : Sup : règles de calcul sur les polynômes ; commencer par reconnaître des monômes. Spé : Spé : traiter un polynôme en x dont les coefficients sont eux-mêmes des polynômes en y ; relier les degrés à une factorisation. Au-delà : Polygones de Newton, valuation et comptage d’intersections dans le tore : prolongements, non déduits du seul dessin.

1. Prendre m=n=4 et q=3 ; calculer les trois degrés avant de lire les valeurs.
2. Annuler a : quel point du support disparaît ? Le degré total change-t-il ?
3. Annuler c, puis comparer la tranche y=0 au polynôme initial.

**À justifier :** Le degré total ne se calcule ni en additionnant les degrés partiels ni en comptant les termes ; une spécialisation peut l’abaisser.

### Un cercle et une parabole : où sont les quatre intersections ?

Compter des solutions réelles sans perdre les racines complexes ou les multiplicités.

**Objets et paramètres**

- x,y sont des coordonnées réelles pour le dessin, puis complexes pour le comptage algébrique. Le cercle est x²+y²=r², de rayon r>0 ; la parabole est y=x²−h.
- r et h sont les paramètres sans unité. Le polynôme éliminé est Q(x)=x⁴+(1−2h)x²+h²−r².
- t=x² permet de ramener Q=0 à une équation du second degré ; D=1−4h+4r² en est le discriminant.
- La multiplicité est ici celle d’une racine de Q. La substitution y=x²−h identifie cette multiplicité à celle de l’intersection dans cette famille.

**Repères** — Sup : Sup : équations du second degré et racines complexes ; tester t≥0 avant de revenir aux réels. Spé : Spé : multiplicité d’une racine, factorisation et étude de tangence ; calcul algébrique certifié sur un exemple. Au-delà : Théorème de Bézout pour les courbes projectives et multiplicité d’intersection : prolongement explicitement séparé.

1. Choisir r=1,h=9/8 et retrouver quatre abscisses réelles.
2. Choisir r=1,h=5/4 : montrer que les deux intersections sont tangentes.
3. Choisir r=h=1/2 : comparer un point géométrique et quatre racines comptées avec multiplicité.

**À justifier :** Un dessin peut montrer zéro, un, deux ou quatre points réels ; le total algébrique reste quatre avec les bonnes conventions.

## Séance 15 — Plusieurs variables & Géométrie

### Éliminer y, puis vérifier chaque candidat

Comprendre pourquoi une élimination fournit des candidats et non toujours des solutions.

**Objets et paramètres**

- x,y sont les indéterminées ; a,b sont des paramètres réels sans unité. Les équations sont F=(x−a)y−1=0 et G=(x−a)(y−b)=0.
- R(x)=Résᵧ(F,G) est le résultant par rapport à y : le déterminant de Sylvester des deux expressions affines en y.
- Le coefficient dominant de F en y est x−a ; il s’annule pour x=a. La fibre au-dessus d’une abscisse x₀ signifie les solutions obtenues en fixant x=x₀.
- Si b≠0, le point réellement commun est (a+1/b,b). Le champ représente F et les droites représentent G.

**Repères** — Sup : Sup : résoudre un système par substitution et distinguer implication et équivalence. Spé : Spé : déterminants, polynômes et racines communes ; retrouver le résultant dans un cas élémentaire. Au-delà : Élimination algébrique, fibres projectives et spécialisation des degrés : prolongements.

1. Prendre a=0,b=1 et trouver les deux zéros du résultant.
2. Substituer x=0 dans F : expliquer pourquoi ce zéro est rejeté.
3. Annuler b : le résultant est-il nul ? Existe-t-il encore un point commun ?

**À justifier :** Un candidat d’élimination doit être vérifié dans chaque équation de départ ; sinon une solution fictive peut être retenue.

### Changer l’ordre des monômes, conserver les solutions

Prolonger la division euclidienne en choisissant un ordre des monômes et en contrôlant les restes.

**Objets et paramètres**

- F=xy−1 et G=y²−x−c sont des polynômes en x,y ; c est un entier réglable. I=(F,G) est l’idéal de leurs combinaisons polynomiales AF+BG.
- Un ordre des monômes précise le terme dominant utilisé pour diviser. « Lex » compare d’abord l’exposant de x ; « degré / lex inverse » compare d’abord le degré total.
- Une base de Gröbner est une famille qui permet de tester l’appartenance à I par un reste nul. Un S-polynôme annule les termes dominants de deux éléments de la base.
- Le quotient ℝ[x,y]/I identifie deux polynômes lorsque leur différence appartient à I. Sa base de monômes est indiquée par la table.

**Repères** — Sup : Sup : substitution, divisibilité et opérations sur les polynômes ; aucun préalable sur les idéaux n’est requis pour les premiers essais. Spé : Spé : algèbre linéaire dans un quotient et calcul exact ; comparer des bases de monômes. Au-delà : Bases de Gröbner, critère de Buchberger et dimension d’une algèbre quotient : notions au-delà du programme.

1. Choisir lex et retrouver x=y²−c, puis y³−cy−1=0.
2. Passer en degré / lex inverse sans changer c : comparer les trois termes dominants.
3. Prendre c=3 et vérifier les trois points réels ; contrôler que chaque S-polynôme a un reste nul.

**À justifier :** L’ordre change les étapes du calcul et les représentants du quotient ; il ne change ni l’idéal ni l’ensemble des solutions.

## Séance 16 — Plusieurs variables & Géométrie

### Trois racines, trois coefficients symétriques

Passer des racines aux coefficients puis aux sommes de puissances, sans perdre l’invariance par permutation.

**Objets et paramètres**

- u,v,w sont trois racines réelles réglables. T est l’indéterminée du polynôme P(T)=(T−u)(T−v)(T−w).
- e₁=u+v+w, e₂=uv+uw+vw et e₃=uvw sont les fonctions symétriques élémentaires.
- pₖ=uᵏ+vᵏ+wᵏ est la somme des puissances d’ordre k. D=(u−v)²(u−w)²(v−w)² est le discriminant.
- Le champ est dessiné dans le plan des coefficients (e₂,e₃), avec e₁ fixé ; il ne représente pas le plan des racines. Tous les nombres sont sans unité.

**Repères** — Sup : Sup : développer un produit, factoriser et relier coefficients et racines. Spé : Spé : sommes de puissances, traces et polynôme caractéristique ; calculer sans diagonaliser. Au-delà : Théorème fondamental des polynômes symétriques et géométrie du discriminant : prolongements.

1. Choisir trois racines distinctes et reconstruire P avant de lire le graphique.
2. Permuter u,v,w : contrôler l’invariance des coefficients et des sommes pₖ.
3. Faire coïncider deux racines ; observer D=0 et la position dans le plan des coefficients.

**À justifier :** Les coefficients symétriques regroupent toute l’information utile pour les sommes de puissances ; le discriminant repère la collision des racines.

### Nœud, pointe ou point isolé ?

Distinguer trois formes de courbe au voisinage d’un point où le gradient s’annule.

**Objets et paramètres**

- x,y sont les coordonnées réelles. Fₜ(x,y)=y²−x³−tx² définit la courbe Fₜ=0 ; t est un paramètre réel sans unité.
- Le gradient est (∂F/∂x,∂F/∂y). Un point singulier satisfait F=0 et les deux dérivées nulles.
- La partie homogène de plus bas degré est y²−tx². Elle détermine les directions tangentes candidates.
- La hessienne à l’origine est diag(−2t,2). Les branches exactes sont y=±|x|√(x+t), lorsqu’elles sont réelles.

**Repères** — Sup : Sup : courbes, factorisation et racine carrée ; examiner les branches sans vocabulaire géométrique avancé. Spé : Spé : dérivées partielles, gradient, hessienne et approximation locale dans les filières concernées. Au-delà : Singularités des courbes algébriques, cône tangent et multiplicité locale : prolongements.

1. Prendre t=1 : retrouver les deux droites tangentes en factorisant y²−x².
2. Annuler t : expliquer pourquoi une seule tangente ne suffit pas à obtenir une branche régulière.
3. Prendre t=−1 : prouver que l’origine est isolée à l’aide du signe de x−1.

**À justifier :** Le gradient nul signale un point à examiner ; la partie homogène et le signe distinguent nœud, pointe et point isolé.

## Séance 17 — Plusieurs variables & Géométrie

### Voir un point à l’infini dans une autre carte

Comprendre les points à l’infini par un changement explicite de coordonnées, sans les assimiler à de grands nombres.

**Objets et paramètres**

- X,Y,Z sont trois coordonnées homogènes. [X:Y:Z] désigne un triplet non nul modulo multiplication par un scalaire commun non nul.
- Dans la carte Z≠0, x=X/Z et y=Y/Z sont les coordonnées usuelles. Dans la carte Y≠0, u=X/Y et v=Z/Y sont les coordonnées affichées.
- c>0 est un paramètre sans unité. Les équations sont y−x²−c=0 ou xy−c=0 ; leurs homogénéisations sont YZ−X²−cZ² et XY−cZ².
- Un point à l’infini de la carte usuelle satisfait Z=0. Dans la carte Y≠0, sa position suit donc v=0.

**Repères** — Sup : Sup : monômes homogènes et changements de variables par substitution. Spé : Spé : coordonnées, espaces quotient et équations de coniques ; outils algébriques à réinvestir. Au-delà : Plan projectif et cartes affines : prolongement au-delà des programmes CPGE.

1. Homogénéiser y−x²−c, puis poser Z=0 pour trouver [0:1:0].
2. Passer dans la carte Y≠0 : retrouver ce point en (u,v)=(0,0).
3. Choisir xy=c ; trouver les deux points à l’infini et dire lequel est absent de cette carte.

**À justifier :** Une courbe reste la même, mais ses coordonnées changent ; un point à l’infini d’une carte peut être un point ordinaire d’une autre.

### Une forme quadratique en trois variables

Classer une forme en trois variables à partir d’une matrice symétrique et comparer cette classification à une tranche plane.

**Objets et paramètres**

- x,y,z sont trois variables réelles. Q=x²+y²+bz²+2axy+2cyz ; a,b,c sont des coefficients réels sans unité.
- A est la matrice symétrique [[1,a,0],[a,1,c],[0,c,b]], telle que Q(v)=vᵀAv pour v=(x,y,z). La hessienne de Q vaut 2A.
- λ₁,λ₂,λ₃ sont les valeurs propres de A. La signature compte les valeurs positives, négatives et nulles.
- Δ₁,Δ₂,Δ₃ sont les mineurs principaux successifs. Le champ ne représente que la tranche z=z₀, où z₀ est le réglage « valeur de la tranche ».

**Repères** — Sup : Sup : matrice d’une expression quadratique, déterminant et complétion des carrés. Spé : Spé : théorème spectral pour les matrices symétriques ; extrema et hessienne dans les programmes concernés. Au-delà : Signature et critère général de Sylvester peuvent être traités comme compléments ; distinguer stricte positivité et semi-définition.

1. Prendre a=c=0,b=2 et prévoir les trois valeurs propres.
2. Prendre a=3/2 : montrer une direction négative dans le plan z=0.
3. Fixer a=1,b=c=0 puis comparer le noyau de Q aux directions propres nulles.

**À justifier :** Le signe des valeurs propres classe Q dans tout ℝ³ ; une tranche isolée peut masquer une direction nulle ou négative.

## Séance 18 — Plusieurs variables & Géométrie

### Positif ne signifie pas somme de carrés

Prouver un signe sur tout le plan et distinguer ce signe d’une représentation en carrés de polynômes.

**Objets et paramètres**

- x,y sont deux variables réelles. Mλ=x⁴y²+x²y⁴−λx²y²+1 ; λ∈[0,4] est le paramètre sans unité.
- t=|xy|≥0 est une variable auxiliaire de la preuve ; elle n’est pas une troisième indéterminée.
- « Non négatif » signifie Mλ(x,y)≥0 pour tout couple réel. Une somme de carrés polynomiaux est une expression ∑qᵢ(x,y)² avec qᵢ à coefficients réels.
- Le minimum global est 1−λ³/27. Pour λ>0, il est atteint aux quatre points x,y=±√(λ/3), marqués sur le champ.

**Repères** — Sup : Sup : inégalités, dérivation et étude d’un polynôme d’une variable après une substitution judicieuse. Spé : Spé : minimum global, forme dominante et raisonnement par les coefficients ; relier à la positivité des formes quadratiques. Au-delà : Polynôme de Motzkin et problème des sommes de carrés : complément au-delà du programme.

1. Prendre λ=0 et écrire les trois carrés visibles.
2. Prendre λ=3 ; prouver Mλ≥0 puis trouver les quatre zéros.
3. Prendre λ=4 ; calculer Mλ(1,1) et retrouver le minimum indiqué.

**À justifier :** La positivité d’un polynôme multivarié ne donne pas automatiquement une somme de carrés polynomiaux ; le contre-exemple est démontré par coefficients.

### Optimiser un quartique sur un cercle

Comparer deux méthodes exactes d’optimisation et voir comment les points stationnaires changent avec un paramètre.

**Objets et paramètres**

- f(x,y)=x⁴+y⁴+axy est la fonction à optimiser ; a est un coefficient réel et x,y sont réels, sans unité.
- La contrainte g(x,y)=x²+y²−r²=0 est un cercle de rayon r>0. θ est l’angle en radians : x=r cosθ,y=r sinθ.
- μ est le multiplicateur dans ∇f=μ∇g. La condition équivalente sur le cercle est d f(r cosθ,r sinθ)/dθ=0.
- s=sin(2θ) varie dans [−1,1]. Le seuil |a|=2r² est la valeur à laquelle certaines familles de points stationnaires se rejoignent.

**Repères** — Sup : Sup : trigonométrie, dérivation et extrema sur un intervalle ; le paramétrage suffit. Spé : Spé : gradient et extrema sous contrainte dans les filières concernées ; les preuves de bornes restent accessibles par une substitution. Au-delà : Bifurcations et extrema dégénérés : prolongements ; la condition stationnaire ne remplace pas la comparaison globale.

1. Prendre a=0,r=1 ; retrouver quatre axes et quatre diagonales stationnaires.
2. Choisir a=1 puis a=2 : identifier les points qui se rejoignent.
3. Choisir a=4 et comparer le minimum et le maximum calculés à ceux du paramétrage angulaire.

**À justifier :** Le nombre de stationnaires varie, mais les bornes globales se calculent exactement en ramenant le problème à une parabole sur [−1,1].
