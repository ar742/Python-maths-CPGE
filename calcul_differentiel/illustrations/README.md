# Huit illustrations scientifiques

Figures SVG vectorielles produites par Python et Matplotlib, consultables hors ligne.
Les vues spatiales sont des projections dont les axes sont indiqués.

| Figure | Sujet |
| --- | --- |
| [Jacobiennes](jacobiennes.svg) | Coordonnées sphériques, face transformée et reste après linéarisation. |
| [Intégrale elliptique](elliptique.svg) | Maillage transformé et convergence de la quadrature. |
| [Taylor](taylor.svg) | Coupe d’une selle, tangente, Taylor 2 et ordres des restes. |
| [Matrices](matrices.svg) | Déterminant, approximation affine et reste de l’inverse. |
| [Optimisation](optimisation.svg) | Descente de gradient et Newton sur une quadratique orientée. |
| [Algèbres de Lie](lie.svg) | Rotation, approximation du tangent et crochet de commutateur. |
| [Gaussienne étendue](gaussienne.svg) | Ellipses décentrées, log I en B₁ et tangente. |
| [Green et Fubini](green_fubini.svg) | Coupures différentes et limites différentes pour Fubini. |

Le plancher 10⁻¹⁶ sur les graphiques logarithmiques est visuel. Les effets d’arrondi
aux petits pas ne modifient pas les résultats théoriques.

Régénérer depuis le dossier du volet :

```console
python -m pip install -r requirements-illustrations.txt
python illustrations.py
```
