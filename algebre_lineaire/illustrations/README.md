# Douze illustrations d’Algèbre & Réductions

Figures scientifiques SVG autonomes, calculées à partir des modèles de l’atelier. Les identités sont vérifiées exactement ; les tracés décimaux illustrent les résultats.

| Figure | Point de départ |
| --- | --- |
| [GL et anneaux](anneaux.svg) | Unités et inversion selon l’anneau. |
| [Composition géométrique](geometrie.svg) | Déterminant, aire et AB ≠ BA. |
| [Algèbres de Lie](lie.svg) | Crochet, exponentielles et petit commutateur. |
| [Gauss](gauss.svg) | Pivots et équivalence des systèmes. |
| [Spectre et Jordan](spectre.svg) | Multiplicités et noyaux généralisés. |
| [Dunford](dunford.svg) | TP rationnel, partie semi-simple et nilpotence. |
| [Vecteur cyclique](cyclique.svg) | Base de Krylov et compagnon. |
| [Frobenius](frobenius.svg) | Chaîne de facteurs invariants et blocs. |
| [Cayley et traces](cayley.svg) | Vandermonde du TP, Newton et puissances. |
| [Pfaffien](pfaffien.svg) | Appariements signés et déterminant. |
| [Projecteurs](projecteurs.svg) | Somme directe et projection oblique. |
| [Formes quadratiques](quadratiques.svg) | Signature, congruence et niveaux. |

Pour les régénérer depuis le dossier `algebre_lineaire` :

```sh
python -m pip install -r requirements-illustrations.txt
python algebre_lineaire.py --export-illustrations
```

[Retour au parcours](../PARCOURS.md) · [Cours et corrigés](../COURS.md)
