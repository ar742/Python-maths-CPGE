# Électricité & Technologies — errata des formules

Ces corrections concernent les formules de l’extrait Électricité P15–P19 du recueil de A. R. Les numéros de page sont ceux imprimés dans le recueil. Chaque correction a été vérifiée avec les schémas, les conventions et les relations de la page concernée.

## 1. P15, pages 393 et 395 — pont de Wheatstone

Les impédances sont $Z_1$ entre A–B, $Z_2$ entre B–C, $Z_3$ entre A–D et $Z_4$ entre D–C. La tension d’alimentation est $e=U_{AC}$, et le voltmètre idéal mesure $U_{BD}=V_B-V_D$.

Avec ces connexions, la formule correcte est :

$$
U_{BD}=e\,\frac{Z_2Z_3-Z_1Z_4}{(Z_1+Z_2)(Z_3+Z_4)}.
$$

Les produits $Z_1Z_3-Z_2Z_4$ imprimés au numérateur doivent donc être remplacés. L’équilibre du pont est :

$$
Z_2Z_3=Z_1Z_4.
$$

Vérification : avec $V_C=0$ et $V_A=e$, les diviseurs donnent $V_B=eZ_2/(Z_1+Z_2)$ et $V_D=eZ_4/(Z_3+Z_4)$.

Dans le prolongement p. 395, les quatre impédances valent initialement $Z$. Les variations indiquées — $Z_1,Z_3$ augmentent de $dZ$, $Z_2,Z_4$ diminuent de $dZ$ — conservent deux branches identiques. Pour ces variations :

$$
dU_{BD}=0,
$$

au lieu de $e\,dZ/Z$.

## 2. P17, page 410 — réponse impulsionnelle d’un filtre récursif

Les coefficients $a_n$ sont ceux du dénominateur du transfert, les $b_m$ ceux du numérateur ; $h(k)$ est la réponse impulsionnelle au rang entier $k\geq0$. Le symbole $z^{-1}$ représente un retard d’un échantillon. Avec les notations de la page :

$$
H(z)=\frac{\sum_{m=0}^{M}b_mz^{-m}}{1+\sum_{n=1}^{N}a_nz^{-n}}
=\sum_{k=0}^{\infty}h(k)z^{-k}.
$$

La récurrence correcte est :

$$
h(0)=b_0,\qquad
h(k+1)=b_{k+1}-\sum_{n=0}^{k}a_{k+1-n}h(n),
$$

avec $a_j=0$ pour $j>N$ et $b_j=0$ pour $j>M$. La borne inférieure imprimée $n=1$ doit devenir **$n=0$** : le terme $a_{k+1}h(0)$ manque.

Vérification : pour $H(z)=(1-q)/(1-qz^{-1})$, avec $0<q<1$, on obtient bien $h(0)=1-q$ et $h(1)=q(1-q)$.

## 3. P17, page 414, exercice 4 — isolation sismique

$x_0$ est le déplacement du sol, $x$ celui de la masse et $F$ la force de l’actionneur. Le symbole $p$ désigne la variable de Laplace ; $\omega_r$ est la pulsation propre, $\alpha$ le coefficient force–déplacement et $\eta$ le gain du dérivateur. Les relations données sont :

$$
x(p)=I(p)\bigl(x_0(p)-\alpha F(p)\bigr),\qquad
I(p)=\frac{\omega_r^2}{p^2+\omega_r^2},\qquad
F(p)=\eta p\bigl(x(p)-x_0(p)\bigr).
$$

Elles conduisent au transfert :

$$
G(p)=\frac{x(p)}{x_0(p)}
=\frac{I(p)(1+\alpha\eta p)}{1+\alpha\eta pI(p)}
=\frac{1+\alpha\eta p}{1+\alpha\eta p+p^2/\omega_r^2}.
$$

**Le terme $(\alpha\eta/\omega_r^2)p^3$ imprimé au numérateur doit être supprimé.**

## 4. P17, page 414, exercice 5 — transformation homographique du passe-bas

Le filtre continu est $H(p)=1/(1+\tau p)$, où $\tau$ est la constante de temps. La période d’échantillonnage est $T_e$, $a=2\tau/T_e$, et $z^{-1}$ représente un retard d’un échantillon. La substitution homographique est :

$$
p=\frac{2}{T_e}\frac{1-z^{-1}}{1+z^{-1}}.
$$

Elle donne :

$$
H(z)=\frac{1+z^{-1}}{(1+a)+(1-a)z^{-1}}.
$$

Pour l’entrée $x_k$ et la sortie $y_k$, l’équation aux différences correcte est :

$$
(1+a)y_k+(1-a)y_{k-1}=x_k+x_{k-1}.
$$

Il faut corriger **le signe du numérateur et celui devant $(1-a)z^{-1}$**. Le gain sur un signal constant vaut alors $H(1)=1$, comme pour le passe-bas continu.

## 5. P18, page 420, exercice 1 — dérivateur amélioré

$R,C$ sont les composants de la branche d’entrée ; $R',C'$ ceux de la contre-réaction. Les tensions complexes sont $V_e,V_s$, $j^2=-1$ et $\omega$ est la pulsation du régime sinusoïdal.

Le transfert du montage inverseur est :

$$
H(j\omega)=\frac{V_s}{V_e}
=-\frac{j\omega R'C}{(1+j\omega RC)(1+j\omega R'C')}.
$$

**Le signe moins manque dans le corrigé.** En notant $I$ le courant de la branche d’entrée et $Z_f$ l’impédance de contre-réaction, la relation correspondante est $V_s=-Z_fI$.

## 6. P18, page 421, exercice 5 — opérateur valeur absolue, alternance négative

Cette entrée reprend **les notations des équations du corrigé** : $e$ est la tension d’entrée, $V_s$ la sortie de l’ALI et $V_{s2}$ la tension du nœud entre $R_2$ et $D_2$. Les étiquettes $V_s$ et $V_{s2}$ sont interverties sur le schéma. Le modèle de diode emploie le seuil $u_{\mathrm{Seuil}}$ et la résistance dynamique $r_D$. Pour $e<0$, $D_2$ conduit et :

$$
i_{D2}=-\frac{e}{R_1}>0,\qquad
V_{s2}=-e\frac{R_2}{R_1},\qquad
V_s=V_{s2}+u_{\mathrm{Seuil}}+r_Di_{D2}.
$$

Ainsi :

$$
V_s=u_{\mathrm{Seuil}}-e\frac{r_D+R_2}{R_1}.
$$

**Le signe devant le terme contenant $e$ doit être moins.**

## 7. P18, page 422, exercice 6 — calcul des coefficients de Fourier

$V_e(t)$ est le créneau alternatif impair d’amplitude $E$, de période $T_e$ et de pulsation $\omega_e=2\pi/T_e$. Pour l’entier $k\geq1$, $A_k$ est le coefficient du sinus et $B_k$ celui du cosinus.

La décomposition de l’intégrale doit s’écrire :

$$
A_k=\frac{2}{T_e}\int_0^{T_e/2}V_e(t)\sin(k\omega_et)\,dt
+\frac{2}{T_e}\int_{T_e/2}^{T_e}V_e(t)\sin(k\omega_et)\,dt.
$$

**Le premier préfacteur $2E/T_e$ imprimé doit devenir $2/T_e$** : l’amplitude $E$ est déjà contenue dans $V_e(t)$.

Les coefficients finaux imprimés sont corrects :

$$
A_k=\frac{2E}{\pi k}\bigl(1-(-1)^k\bigr),\qquad B_k=0.
$$

## 8. P18, page 422, exercice 6 — reconstruction de la sortie filtrée

Dans cette section, $p\geq0$ est un **indice entier d’harmonique**. On pose $\Omega_p=(2p+1)\omega_e$. L’ensemble $\Delta_p$ contient les indices des harmoniques retenues dans la bande passante, comme défini dans le recueil. $H(j\Omega_p)$ est le transfert complexe du filtre à cette pulsation.

L’approximation de la sortie réelle est :

$$
V_s(t)\approx\sum_{p\in\Delta_p}\frac{4E}{\pi(2p+1)}
\left|H(j\Omega_p)\right|
\sin\!\left(\Omega_pt+\arg H(j\Omega_p)\right).
$$

Dans l’écriture exponentielle, cela revient à :

$$
V_s(t)\approx\sum_{p\in\Delta_p}\frac{4E}{2j\pi(2p+1)}
\left[H(j\Omega_p)e^{j\Omega_pt}-H(-j\Omega_p)e^{-j\Omega_pt}\right],
$$

avec $H(-j\Omega_p)=\overline{H(j\Omega_p)}$. **L’exponentielle de fréquence négative doit recevoir ce transfert conjugué**, au lieu du même $H(j\Omega_p)$ que l’exponentielle de fréquence positive. La formule imprimée coïncide avec cette expression lorsque les transferts des harmoniques retenues sont réels.
