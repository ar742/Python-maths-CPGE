# Optimisation & Distances · Maths sup / maths spé

Le deuxième atelier de [Python-maths-CPGE](https://github.com/ar742/Python-maths-CPGE) :
**5 laboratoires interactifs, 10 leçons, 14 exercices corrigés et 5 figures SVG**.
Les calculs sont effectués en Python ; le navigateur affiche les résultats et les objets en trois dimensions.

![Deux ellipsoïdes disjoints et contrôle des bornes](illustrations/deux_ellipsoides.svg)

## Démarrer

Python **3.10 ou plus récent** et **NumPy** sont requis. Aucun compte ni service distant n'est nécessaire pour utiliser l'atelier.

**Windows :** après téléchargement et extraction du dépôt, double-cliquer sur `Lancer_Optimisation.cmd` à la racine.
À la première ouverture, le lanceur crée un environnement Python dans le projet si nécessaire et installe NumPy depuis PyPI.
Une connexion Internet est nécessaire pour cette installation ; les expériences fonctionnent ensuite hors ligne.
Un environnement `.venv` déjà présent à la racine est utilisé en priorité.

**Tous systèmes, depuis ce dossier :**

```console
python -m venv .venv
```

Activer l'environnement : `.venv\Scripts\activate` sous Windows, `source .venv/bin/activate` sous Linux/macOS.
Puis :

```console
python -m pip install -r requirements.txt
python optimisation_distances.py
```

Sur Linux/macOS, la commande initiale peut être `python3`. L'application s'ouvre sur
<http://127.0.0.1:8766>. Garder le terminal ouvert ; **Ctrl+C** l'arrête.
Le port du volet Rubik est 8765 : les deux applications peuvent fonctionner ensemble.

```console
python optimisation_distances.py --port 8767 --no-browser
```

GitHub héberge les sources, les figures et les documents ; les calculs interactifs se lancent localement.
Ouvrir `index.html` seul ne lance pas le moteur Python.

## Les expériences

| Laboratoire | Point de départ | Enrichissement |
| --- | --- | --- |
| Cosinus | TP p. 158 : meilleure droite L² sur [0,π/2] | Degré 0 à 6, poids positif, QR, conditionnement, descente de gradient, droite uniforme minimax exacte. |
| Matrices | Exercice 4 : rotation et sous-espace symétrique | Dimension maximale d'un espace diagonalisable réel ; antisymétriques de déterminant 1 sur ℝ ou ℂ, n de 2 à 10. |
| Produit & boîte | Exercice 6 : maximum de \|xyz\| sur la sphère | Ellipsoïde aligné, huit maxima, boîte inscrite de volume maximal, exposants positifs quelconques. |
| Point & ellipsoïde | Distances euclidiennes minimale et maximale | Ellipsoïde tourné et translaté ; extrema globaux, cas de multiplicité et multiplicateurs singuliers. |
| Deux ellipsoïdes | Distance minimale entre solides convexes disjoints | Centres et axes distincts, rotations, projections alternées, bornes primal-dual, plan à marge maximale et lien SVM. |

Chaque expérience propose des exemples, des curseurs, une explication, des contrôles numériques et un export JSON des paramètres et résultats.
Dans les trois vues géométriques, **glisser sur la figure** tourne la caméra (projection orthographique).

[Parcours conseillé en 60 minutes](PARCOURS.md) · [Cours et exercices à lire séparément](COURS.md)

## Résultats exacts et conventions

- Le TP minimise une **distance au carré** : Imin≈0,00618858317 et d≈0,07866754841.
- La droite uniforme de cos sur [0,π/2] est environ −0,63661977237 t + 1,10525683118 ; son erreur maximale est ≈0,10525683118.
- Pour la rotation : d(Rθ,S₃)=√2\|sin θ\|. La dimension maximale d'un sous-espace de matrices réelles diagonalisables sur ℝ est n(n+1)/2.
- En dimension impaire, notamment **3**, {Aᵀ=−A, det A=1} est **vide**. Pas de distance finie ; convention étendue : +∞.
- En dimension paire, sa distance à Sₙ est **√n**, atteinte lorsque A*A=I. Sur ℂ, « symétrique » signifie Aᵀ=A, pas A*=A.
- Sur l'ellipsoïde aligné de demi-axes a,b,c, max\|xyz\|=abc/(3√3) ; la boîte parallèle aux axes a volume maximal 8abc/(3√3).
- Les distances minimale et maximale d'un point sont calculées pour la **surface** ; la distance au **solide** est indiquée séparément.
- L'expérience à deux ellipsoïdes calcule la distance des **solides**. Pour des solides disjoints, elle coïncide avec celle de leurs surfaces. Elle ne traite pas la distance entre surfaces emboîtées.

## Méthodes et limites numériques

**Cosinus.** Quadrature de Gauss-Legendre à 96 points, polynômes de Legendre normalisés et QR.
Les coefficients affichés sont convertis en monômes pour la lecture. La meilleure droite uniforme est obtenue par une formule exacte et une preuve d'alternance.
Pour les projections de degré ≥2, la norme uniforme est encadrée par un maximum échantillonné et une borne de Lipschitz ; il ne s'agit pas du polynôme minimax de ce degré.

**Point–ellipsoïde.** Deux équations séculaires monotones sont résolues par dichotomie, avec traitement des pôles.
Les matrices D+μI et λI−D sont positives : une identité quadratique prouve le caractère global des extrema.
L'interface affiche les résidus et un représentant lorsqu'il existe plusieurs solutions.

**Deux ellipsoïdes.** Projections alternées exactes à l'arrondi près, au plus 1 200 itérations.
Pour une direction unitaire n, la fonction support donne L=max(0,n·(c₂−c₁)−√(nᵀQ₁n)−√(nᵀQ₂n)).
La paire admissible donne U=\|y−x\|. L'arrêt demande U−L≤10⁻⁸ fois l'échelle géométrique.
Si la limite est atteinte, les bornes restent affichées et la convergence n'est pas annoncée.
Les paramètres admissibles bornent la taille et le coût des calculs.

Tous ces calculs utilisent des nombres flottants. Les bornes primal-dual constituent un **contrôle numérique**, sans arithmétique d'intervalles ni arrondis dirigés.
Une distance très petite doit être interprétée à la précision indiquée.

## Utiliser le moteur dans un programme Python

Depuis ce dossier, par exemple :

```python
from mathematiques import approximation, point_ellipsoide, distance_ellipsoides

tp = approximation({"L": 1.5707963267948966, "degre": 1, "poids": 0})
print(tp["coefficients"], tp["distance"])

point = point_ellipsoide({"centre": [0, 0, 0], "axes": [3, 2, 1],
                         "angles": [15, 20, 30], "point": [4, 2, 1]})
print(point["minimum"]["distance"], point["maximum"]["distance"])

e1 = {"centre": [-2.4, -.6, 0], "axes": [1.8, 1, .7], "angles": [10, 20, 25]}
e2 = {"centre": [2.4, .8, .5], "axes": [1.4, .9, .6], "angles": [-20, 35, -35]}
paire = distance_ellipsoides(e1, e2)
print(paire["inferieure"], paire["superieure"], paire["ecart"])
```

Pour cet exemple orienté : distance≈**2,67047185**, avec un écart primal-dual d'environ **2,29×10⁻⁹**.
Les angles sont en degrés ; R=Rz Ry Rx agit sur des vecteurs colonnes. Les demi-axes sont strictement positifs.

## Figures autonomes et vérifications

Les [5 SVG](illustrations) sont déjà fournis. Matplotlib est seulement nécessaire pour les régénérer :

```console
python -m pip install -r requirements-illustrations.txt
python optimisation_distances.py --export-illustrations
```

Tests du moteur et du serveur :

```console
python -X utf8 -m unittest -v test_mathematiques
```

**29 tests** : formules analytiques, quadrature indépendante, orthogonalité complexe, extrema et cas singuliers,
invariances géométriques, admissibilité, bornes, contraintes SVM, API et entrées invalides.
Ils sont également exécutés sous Windows et Linux dans les vérifications GitHub.

| Fichier | Rôle |
| --- | --- |
| `mathematiques.py` | Calculs et preuves numériques des extrema. |
| `cours.py` | Dix leçons, quatorze exercices et références. |
| `COURS.md` | Version lisible sans lancer l'application. |
| `optimisation_distances.py` | Serveur local, contrôle des requêtes, lancement. |
| `app.js`, `index.html`, `style.css` | Interface et illustrations interactives hors ligne. |
| `illustrations.py` | Figures scientifiques exportées avec Matplotlib. |
| `test_mathematiques.py` | Références indépendantes et tests de fonctionnement. |

Le serveur écoute uniquement sur la boucle locale et contrôle l'hôte, l'origine et le jeton de session.
Les fichiers sources et les fichiers personnels ne sont pas servis par l'application.

## Sources

Le parcours reprend et enrichit le **TP p. 158**, le **SVM p. 159**, les **exercices 4 et 6 p. 162**
du recueil fourni par A. R., ainsi que `distMatrices.txt`. Les pièces jointes originales ne sont pas nécessaires au fonctionnement.
Les démonstrations et figures de ce volet sont nouvelles.

- [David Eberly : Distance from a Point to an Ellipse, an Ellipsoid, or a Hyperellipsoid](https://www.geometrictools.com/Documentation/DistancePointEllipseEllipsoid.pdf).
- [Boyd et Vandenberghe : Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).
- Documentation NumPy : [QR](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html) et [Gauss-Legendre](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html).
