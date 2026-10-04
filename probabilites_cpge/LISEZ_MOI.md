# Ouvrir Probabilités & Expériences

1. Sur GitHub, choisir **Code → Download ZIP**, puis extraire toute l’archive.
2. Installer Python **3.10 ou plus récent**, si nécessaire, avec l’option d’ajout au PATH.
3. Sous Windows, double-cliquer sur **Lancer_Probabilites.cmd** à la racine du dossier.
4. Le navigateur ouvre <http://127.0.0.1:8767>. Garder le programme Python ouvert.

La première ouverture prépare un environnement Python et installe NumPy depuis PyPI
si nécessaire. Cette étape demande Internet. Les expériences et le cours n’utilisent
ensuite aucun service distant, aucune clé et aucune bibliothèque chargée par CDN.

## Lancement manuel sur tous systèmes

Dans un terminal ouvert dans le dossier `probabilites_cpge` :

```console
python -m venv .venv
```

Activer l’environnement : sous Windows, `.venv\Scripts\activate` ; sous Linux/macOS,
`source .venv/bin/activate`. Puis :

```console
python -m pip install -r requirements.txt
python probabilites_cpge.py
```

Utiliser `python3` si c’est le nom de Python sur votre ordinateur.
Ctrl+C ferme le laboratoire. Un deuxième lancement rouvre une instance déjà démarrée.
Si le port est occupé par une autre application :

```console
python probabilites_cpge.py --port 8768
```

`--no-browser` démarre le serveur sans ouvrir automatiquement un onglet.
GitHub présente les fichiers ; les calculs se font sur votre ordinateur.
Ouvrir `index.html` seul ne démarre pas le programme.

## Utiliser les laboratoires

Choisir un onglet, modifier les paramètres ou sélectionner un exemple.
Les figures et les résultats se recalculent. Les paramètres dépendants sont ajustés :
le nombre de tirages ne dépasse pas l’urne, le rang et le mode propre ne dépassent pas n.

La **graine aléatoire** fixe l’échantillon. Avec les mêmes paramètres et une même version
de NumPy, on obtient la même expérience. « Autre échantillon » change la graine.
Les répétitions représentent des essais indépendants du modèle étudié ; pour Wigner,
elles portent sur les **matrices**, et non sur leurs valeurs propres dépendantes.

« Consulter les valeurs et les moments » déplie le tableau. « Comprendre et démontrer »
présente la méthode, et « Cours & exercices » contient les preuves complètes.
« Exporter les résultats » télécharge un JSON contenant les paramètres, les données
tracées, les résultats théoriques et les observations. Le fichier reste sur votre ordinateur.

## Conventions numériques

- Les lois finies sont calculées en virgule flottante, avec normalisation des poids binomiaux.
- Les histogrammes de masses sont distingués des histogrammes de densité.
- Les maxima/minima sont simulés directement par leur loi Beta exacte, plutôt qu’en
  générant toutes les valeurs d’un échantillon.
- La loi arcsinus est comparée par masses intégrées, car sa densité diverge aux bords.
- Les spectres sont calculés par un algorithme pour matrices symétriques ; les résidus
  sont numériques et les valeurs propres sont comptées avec leur multiplicité.
- Wigner utilise des entrées supérieures i.i.d., centrées, de variance 1, avec une loi fixe.
  Le modèle normal n’est pas le GOE standard : ici la diagonale a aussi une variance 1.
- Les bornes BT sont théoriques, évaluées en virgule flottante. La bande affichée est
  ponctuelle, non simultanée. Wilson et l’approximation normale sont des approximations.
- Dimensions et répétitions sont bornées pour conserver une interface réactive.

## Fichiers utiles

`mathematiques.py` contient les modèles ; `cours.py` les leçons et corrections ;
`probabilites_cpge.py` lance le serveur local ; `test_mathematiques.py` vérifie le tout.
L’application écoute exclusivement sur `127.0.0.1` et contrôle l’hôte, l’origine et la session.

Matplotlib est facultatif : il sert seulement à régénérer les six SVG déjà fournis.
Le cours autonome se régénère avec `python export_cours.py`.

[Parcours pédagogique](PARCOURS.md) · [Cours autonome](COURS.md)
