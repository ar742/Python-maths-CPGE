# Polynômes & Géométrie — corrections de formules

Corrections de formules vérifiées dans le contexte de l’extrait du recueil de A. R. : pages imprimées 31, 39 et 165–172. Les conventions et les hypothèses nécessaires sont précisées ci-dessous.

## 1. Page 39, exercice 8 — comptage par Möbius

Soit $p$ un nombre premier et $I_p(n)$ le nombre de polynômes irréductibles unitaires de degré $n$ sur $\mathbb F_p$. La formule correcte, déjà présente avant le produit final du recueil, est :

$$
nI_p(n)=\sum_{d\mid n}\mu(d)p^{n/d}.
$$

Le produit proposé dans la dernière ligne ne remplace pas cette somme en général. Pour $p=2,n=6$, la somme vaut $64-8-4+2=54$, donc $I_2(6)=9$, tandis que le produit imprimé vaut $42$.

## 2. Page 39, exercice 7 — formule du corps engendré

Posons $\theta=\sqrt[4]{3}$. Le corps engendré par $\theta$ est :

$$
\mathbb Q(\theta)=\{a+b\theta+c\theta^2+d\theta^3:(a,b,c,d)\in\mathbb Q^4\}.
$$

Le terme en $\theta^3$ manque dans l’ensemble à trois coefficients affiché. En effet, $X^4-3$ est irréductible par Eisenstein : $1,\theta,\theta^2,\theta^3$ sont indépendants sur $\mathbb Q$. L’ensemble affiché ne contient pas le produit $\theta\theta^2=\theta^3$.

## 3. Page 168 — génératrice des nombres de Bernoulli

Avec la convention $b_0=1$, $b_1=-1/2$, la génératrice est :

$$
\frac{z}{e^z-1}=\sum_{k=0}^{\infty}\frac{b_k}{k!}z^k.
$$

Le dénominateur $1-e^z$ imprimé doit être remplacé par $e^z-1$. Le quotient corrigé, prolongé en $z=0$, vaut $1$ en ce point. Cette correction conserve la convention annoncée dans cette ligne ; elle ne modifie pas la convention $b_1=+1/2$ utilisée plus haut pour Faulhaber.

## 4. Page 168 — réciproque conjugué sur les complexes

Pour $P(X)=\sum_{k=0}^{n}a_kX^k$, le renversement conjugué des $n+1$ coefficients est, pour $z\ne0$ :

$$
P^*(z)=\sum_{k=0}^{n}\overline{a_{n-k}}z^k
=z^n\overline{P(1/\overline z)}.
$$

L’exposant du facteur extérieur est **$n$**, au lieu de $-n$. Pour une racine non nulle $\alpha$ de $P$, la racine correspondante de $P^*$ est **$1/\overline\alpha$**, au lieu de $1/\alpha$ dans le cas général complexe. La recomposition correspondante est :

$$
P(z)=z^n\overline{P^*(1/\overline z)}.
$$

Pour des coefficients réels, les conjugaisons des coefficients disparaissent. Le nombre $n$ reste le degré ambiant fixé dans ces identités.

## 5. Page 169 — coefficient du reste de division

Pour le reste $R(X)=\alpha X+\beta$ de la division de $P$ par $(X-a)(X-b)$, avec $a\ne b$, le parenthésage correct est :

$$
\alpha=\frac{P(b)-P(a)}{b-a},\qquad \beta=P(a)-a\alpha.
$$

Toute la différence $P(b)-P(a)$ est au numérateur.

## 6. Page 169 — produit PGCD–PPCM unitaires

Pour $A,B$ non nuls, notons $\operatorname{lc}(A)$ et $\operatorname{lc}(B)$ leurs coefficients dominants. Puisque le PGCD et le PPCM sont définis **unitaires** page 165 :

$$
\operatorname{PGCD}(A,B)\operatorname{PPCM}(A,B)
=\frac{AB}{\operatorname{lc}(A)\operatorname{lc}(B)}.
$$

La formule imprimée avec $AB$ seul vaut lorsque le produit des coefficients dominants vaut $1$. Exemple : pour $A=2X,B=3X$, le produit des deux polynômes unitaires est $X^2$, et non $6X^2$.

## 7. Pages 169 et 172 — indices des relations de Viète

Pour un polynôme de degré $n$, de coefficient dominant $a_n$, les racines $\alpha_1,\ldots,\alpha_n$ sont comptées avec multiplicité. Pour $1\le k\le n$ :

$$
\sum_{1\le i_1<\cdots<i_k\le n}\alpha_{i_1}\cdots\alpha_{i_k}
=(-1)^k\frac{a_{n-k}}{a_n}.
$$

Les indices sont **strictement croissants**. Des valeurs de racines peuvent se répéter ; un même indice ne doit pas être choisi plusieurs fois dans un produit.

## 8. Page 171, exercice 1 — composition du polynôme choisi

Avec $P(X)=X^2+2X-1$, la première égalité de composition doit être :

$$
P(P(X))=(X^2+2X-1)^2+2(X^2+2X-1)-1
=X^4+4X^3+4X^2-2.
$$

Le facteur **$2$** manque devant la seconde occurrence de $P(X)$ dans cette première ligne. Le développement final et le reste $X$ annoncés ensuite sont corrects.

## 9. Page 171, exercice 2 — coefficient dominant de la dérivée

Le polynôme de l’exercice est unitaire, de degré $n$, avec des racines réelles distinctes $a_i$ de multiplicités $m_i$. Les points $c_i$ sont les racines de la dérivée entre deux racines successives. La factorisation correcte est :

$$
P'(X)=n\prod_{i=1}^{r}(X-a_i)^{m_i-1}
\prod_{i=1}^{r-1}(X-c_i).
$$

Le facteur **$n$** manque : la dérivée d’un polynôme unitaire de degré $n$ a pour coefficient dominant $n$.

## 10. Page 171, exercice 5 — somme géométrique, factorisation et produit

Le polynôme défini dans l’énoncé est $P_n(X)=\sum_{k=0}^{n}((1+X)/2)^k$. Ses racines sont $\alpha_k=2e^{2ik\pi/(n+1)}-1$, pour $1\le k\le n$. Les formules corrigées sont :

$$
P_n(1)=n+1,\qquad
P_n(X)=2^{-n}\prod_{k=1}^{n}(X-\alpha_k),
$$

$$
\prod_{k=1}^{n}\alpha_k=(-1)^n(2^{n+1}-1).
$$

Il faut compter les $n+1$ termes au point $1$, conserver le coefficient dominant $2^{-n}$ et diviser le terme constant par ce coefficient dans le produit des racines.

## 11. Page 172, exercice 8 — Legendre et intégrations par parties

Avec la notation $L_n$ pour les polynômes de Legendre, la parité s’écrit :

$$
L_n(-X)=(-1)^nL_n(X).
$$

Le $P_n$ de la ligne imprimée doit être remplacé par $L_n$. Pour les termes aux bornes des intégrations par parties, poser $A_n(x)=(1-x^2)^n$. Ce sont les dérivées de **$A_n$** qui s’annulent :

$$
A_n^{(\ell)}(1)=A_n^{(\ell)}(-1)=0\quad(0\le\ell<n),
$$

et non celles de $L_k$ en général. Dans la décomposition du polynôme de Rodrigues sur $L_0,\ldots,L_n$, les coefficients vérifient $\lambda_k=0$ pour $k<n$ et $\lambda_n=1$ ; la nullité ne s’étend pas au coefficient de degré $n$.

## 12. Page 172, exercice 9 — fonction de la borne de Cauchy

Soit $P(X)=\sum_{k=0}^{n}a_kX^k$, avec $a_n\ne0$ et au moins un coefficient inférieur non nul. Pour $r>0$, la fonction définie dans le corrigé est :

$$
h(r)=1-\sum_{k=0}^{n-1}\left|\frac{a_k}{a_n}\right|r^{k-n},\qquad
h'(r)=\sum_{k=0}^{n-1}(n-k)\left|\frac{a_k}{a_n}\right|r^{k-n-1}>0.
$$

Elle est donc **strictement croissante**, avec :

$$
\lim_{r\to0^+}h(r)=-\infty,\qquad \lim_{r\to+\infty}h(r)=1.
$$

Les limites et le sens de variation imprimés sont inversés. Pour une racine $\alpha$ de $P$, la relation correcte est :

$$
\alpha^n=-\sum_{k=0}^{n-1}\frac{a_k}{a_n}\alpha^k.
$$

Le signe moins manque dans cette égalité. L’inégalité triangulaire et l’encadrement final du rayon maximal restent valables.
