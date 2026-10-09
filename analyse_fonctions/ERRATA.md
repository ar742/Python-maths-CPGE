# Corrections de formules vérifiées — extrait Analyse et Fonctions

Les corrections ci-dessous portent exclusivement sur des formules du PDF, vérifiées sur les pages imprimées et dans leur contexte.

## Page 48 — représentation de Γ sur ]0,1[

Dans la représentation suivant les deux intégrales sur ]0,+∞[, le facteur `2` ne s’applique pas à l’intégrale sur ]0,1[. Pour Re(z)>0 :

$$\Gamma(z)=\int_0^1(-\ln t)^{z-1}\,dt.$$

En posant `u=−ln t`, on retrouve `∫₀^∞u^(z−1)e^(−u)du`. Pour z=1, cette intégrale vaut 1, conformément à Γ(1)=1 donné sur la même page.

## Page 48 — changement de variable dans β

Avec `t=1/(1+u)`, les bornes et la différentielle donnent :

$$\beta(x,y)=\int_0^{+\infty}\frac{u^{y-1}}{(1+u)^{x+y}}\,du,\qquad\Re(x)>0,\ \Re(y)>0.$$

Lorsque t va de 0 à 1, u va de +∞ à 0 ; `dt=−du/(1+u)²`. La ligne imprimée avec les bornes 0 et 1 et la différentielle dt est donc remplacée par cette expression.

## Page 48 — jacobien de (s,t) ↦ (u,v)

Pour `u=st` et `v=s(1−t)`, le jacobien en valeur absolue vaut s. La ligne de calcul du produit de deux fonctions gamma s’écrit :

$$\Gamma(x)\Gamma(y)=\int_0^{+\infty}\int_0^1 e^{-s}(st)^{x-1}\bigl(s(1-t)\bigr)^{y-1}\,s\,dt\,ds=\Gamma(x+y)\beta(x,y).$$

Le facteur s donne l’exposant `x+y−1` dans l’intégrale en s et permet de retrouver l’identité finale de la page.

## Page 70 — facteur intégrant de y′+a(x)y=c(x)

Avec `A′=a`, les signes des exponentielles dans les deux formules scalaires sont inversés. Pour la condition `y(x₀)=y₀` :

$$y(x)=e^{-A(x)}\left(y_0e^{A(x_0)}+\int_{x_0}^x c(t)e^{A(t)}\,dt\right).$$

La solution générale s’écrit `y=e^(−A)(C+∫c e^A)`. Vérification directe : `(e^A y)′=e^A(y′+ay)=e^A c`. Cette correction concerne l’équation scalaire écrite avec `+a(x)y` ; la formule matricielle pour `Y′=AY+B` figurant ensuite conserve son expression.
