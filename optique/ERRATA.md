# Optique — corrections de formules vérifiées

Ces quatre points concernent uniquement des formules de l’extrait fourni et leur vérification dans son contexte. Les numéros indiquent la pagination du recueil, puis la page de l’extrait PDF. Les conventions équivalentes et les remarques éditoriales ou pédagogiques ne figurent pas dans ce document.

## 1. Mirage : intégration de la courbure

**Recueil p. 337 — PDF p. 11, corrigé de l’exercice 3.**

Pour le profil $n(z)=n_0\sqrt{1+z/a}$ et l’angle $\theta_0$ avec l’horizontale, la dérivée seconde donnée est

$$z''(x)=\frac{1}{2(a+z_0)\cos^2\theta_0}.$$

La trajectoire obtenue avec $z(0)=z_0$ et $z'(0)=\tan\theta_0$ est donc

$$\boxed{z(x)=z_0+x\tan\theta_0+\frac{x^2}{4(a+z_0)\cos^2\theta_0}}.$$

Le dénominateur du terme en $x^2$ est **4**, au lieu de 2 dans la dernière ligne. Vérification : $(Ax^2)''=2A$ ; le coefficient corrigé redonne exactement la dérivée seconde qui précède.

## 2. Fente : largeur totale de la tache centrale

**Recueil p. 344 — PDF p. 18, diffraction par une fente de largeur $a$.**

Dans la limite paraxiale de Fraunhofer, les deux premiers zéros sont à

$$x_-=-\frac{\lambda D}{a},\qquad x_+=+\frac{\lambda D}{a}.$$

La largeur **totale**, mesurée entre ces zéros, est donc

$$\boxed{L=x_+-x_-=\frac{2\lambda D}{a}}.$$

$\lambda D/a$ est la demi-largeur $R$, et non cette largeur totale. Cette correction est cohérente avec la ligne angulaire de la même page : $\theta\simeq2R/D\simeq2\lambda/a$.

## 3. Apodisation cosinus : intensité et zéros

**Recueil p. 348 — PDF p. 22, corrigé de l’exercice 7.**

La transmittance d’amplitude est $t(x,y)=t_0\cos(\pi x/a)$ dans le rectangle. Avec $u=\pi a\sin\theta/\lambda_0$, le changement de variable dans l’amplitude imprimée donne

$$s(u)=Aab t_0 e^{i\varphi_0}\frac{\pi}{2}\frac{\cos u}{\pi^2/4-u^2}.$$

Si l’intensité est normalisée par $I=|s|^2$, sa formule est

$$\boxed{I(u)=|A|^2a^2b^2t_0^2\frac{\pi^2}{4}\left(\frac{\cos u}{\pi^2/4-u^2}\right)^2},\qquad
\boxed{I_{\max}=I(0)=\frac{4|A|^2a^2b^2t_0^2}{\pi^2}}.$$

Le facteur $\pi^2$ manque dans le prefacteur de l’intensité réécrite avec $u$ ; le maximum doit également être quadratique dans l’amplitude. Avec une autre constante globale de conversion champ→intensité, cette constante multiplie les deux expressions ensemble. La forme normalisée, indépendante de cette constante, est

$$\frac{I(u)}{I(0)}=\left(\frac{\pi^2}{4}\frac{\cos u}{\pi^2/4-u^2}\right)^2.$$

Les zéros de l’apodisation sont aux demi-entiers

$$\boxed{\left|\frac{a\sin\theta}{\lambda_0}\right|=\frac32,\frac52,\frac72,\ldots},$$

et non aux entiers. Les points $u=\pm\pi/2$ sont des singularités **amovibles**, pas des zéros : $I(\pm\pi/2)/I(0)=\pi^2/16\simeq0{,}617$. La décomposition du cosinus en deux exponentielles, puis l’intégration de ces exponentielles, vérifie amplitude, intensité et limites.

## 4. Génération à $2\omega$ : dépendance quadratique en fréquence

**Recueil p. 350 — PDF p. 24, corrigé de l’exercice 11, régime de pompes constantes.**

L’équation d’enveloppe donnée est

$$\frac{dE_3}{dz}=-\frac{i\omega\chi_{\rm eff}}{c n_3}E_1E_2e^{i\Delta k z}.$$

En prenant $E_3(0)=0$ et $E_1,E_2$ constants, son intégration puis le module au carré donnent

$$\boxed{|E_3(L)|^2=\frac{\omega^2|\chi_{\rm eff}|^2}{c^2 n_3^2}|E_1|^2|E_2|^2L^2\operatorname{sinc}^2\!\left(\frac{\Delta kL}{2}\right)}.$$

Le prefacteur de la ligne qui suit l’équation dans le corrigé est linéaire en $\omega$ ; il doit être **quadratique en $\omega$**. Le passage de $|E_3|^2$ à une intensité physique doit en outre conserver une même convention de normalisation pour les trois champs. La vérification ci-dessus utilise directement l’équation d’enveloppe de cette page, sans supposer un choix supplémentaire pour ce prefacteur d’intensité.
