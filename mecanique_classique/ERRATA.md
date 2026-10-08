# Corrections de formules vérifiées — extrait Mécanique P1–P3

Les trois corrections ci-dessous concernent uniquement des formules du PDF
source, vérifiées sur les pages imprimées et dans leur contexte. Les notations
du recueil sont conservées. Aucune remarque éditoriale ou pédagogique n’est
incluse.

## P1, page 269 — énergie en coordonnées polaires

Dans la ligne qui précède le potentiel effectif, le terme tangentiel de
l’énergie cinétique contient un facteur `r` à la place de `r²`.
Avec `v² = ṙ² + r² θ̇²`, la formule est :

$$E=\frac{\mu}{2}\left(\dot r^2+r^2\dot\theta^2\right)-\frac{k}{r}.
$$

Elle donne bien le potentiel effectif imprimé dans la même ligne :

$$E_{p,\mathrm{eff}}(r)=\frac{\mu C^2}{2r^2}-\frac{k}{r},\qquad C=\frac{L_0}{\mu}.$$

## P1, page 269 — énergie d’une orbite elliptique

Dans la ligne de la troisième loi de Kepler, l’énergie imprimée avec un
signe positif et un coefficient `m²` devient, pour la masse orbitante `m`
et `k=GMm` dans le modèle du centre fixe :

$$E=-\frac{mk^2}{2L_0^2}(1-e^2)=-\frac{k}{2a}.$$

Vérification : `p=L₀²/(mk)`, `a=p/(1-e²)` et
`E=-k/(2a)`. Pour le problème à deux corps, remplacer `m` par la masse
réduite `μ` dans le premier membre développé. Une orbite elliptique possède
une énergie mécanique négative avec le potentiel `−k/r` de cette page.

## P3, page 289 — coordonnées du centre de la barre sur rotule

Pour les angles du schéma et de la vitesse imprimée (`θ` azimut dans le plan
horizontal, `φ` élévation), la deuxième coordonnée de `OG` est
`L cosφ sinθ`, à la place de `L cosθ sinφ`. Le vecteur complet est :

$$\overrightarrow{OG}=L\begin{pmatrix}
\cos\varphi\cos\theta\\
\cos\varphi\sin\theta\\
\sin\varphi
\end{pmatrix}.$$

Sa norme vaut `L` et sa dérivée redonne les trois composantes de la vitesse
figurant juste après dans le recueil. L’atelier utilise aussi, en l’annonçant
explicitement, la convention colatitude–azimut pour le laboratoire spatial.
