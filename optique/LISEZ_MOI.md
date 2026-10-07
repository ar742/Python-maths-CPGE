# Ouvrir Lumière & Images

## Windows

Télécharger le dépôt avec **Code → Download ZIP** sur GitHub, puis extraire
l’archive. Double-cliquer sur **Lancer_Optique.cmd** à la racine du dossier,
ou sur celui du dossier `optique`.

Il faut **Python 3.10 ou plus récent**. Lors de la première ouverture, le lanceur
crée un environnement Python et installe NumPy si nécessaire ; cette étape
demande une connexion Internet. Les ouvertures suivantes fonctionnent hors ligne.
Garder la fenêtre de lancement ouverte pendant les expériences.

L’atelier s’ouvre dans le navigateur à <http://127.0.0.1:8774>.
**Ctrl+C** dans la fenêtre de lancement arrête le serveur.

## Windows, Linux et macOS : lancement manuel

Depuis le dossier `optique`, avec le même Python pour ces commandes :

```text
python -m pip install -r requirements.txt
python -X utf8 optique.py
```

Sur certains systèmes, la commande s’appelle `python3`.
Si le port est occupé par un autre programme :

```text
python -X utf8 optique.py --port 8776
```

Ouvrir alors l’adresse indiquée dans la fenêtre de lancement. Si le serveur
de cet atelier fonctionne déjà, le lanceur retrouve son adresse.

## Première séance

Commencer par **Lentille**, **Young** ou **Œil**. Avant de modifier une commande,
lire « But du TP et lien avec le cours », noter une prédiction, puis comparer
les résultats à la leçon associée. Les exemples pré-réglés donnent des cas
contrastés et les hypothèses accompagnent chaque résultat.

L’onglet **Cours & exercices** contient les corrections, accessibles après
une tentative personnelle. Le [parcours de dix missions](PARCOURS.md) relie
ces expériences. **Exporter les résultats** conserve les paramètres, les
tableaux calculés et les hypothèses dans un fichier JSON.

GitHub présente le cours et les sources ; le navigateur local réalise les TP
avec Python. Ouvrir `index.html` seul ne lance pas les calculs.

## Figures et vérifications facultatives

Les figures SVG sont déjà fournies. Pour les régénérer :

```text
python -m pip install -r requirements-illustrations.txt
python -X utf8 optique.py --export-illustrations
```

Pour vérifier les modèles et le serveur :

```text
python -X utf8 -m unittest -v test_geometrie test_ondes test_entree test_pedagogie test_serveur
```

En cas d’erreur, lancer manuellement le programme et conserver le message
affiché : il permet d’identifier la bibliothèque manquante ou le port occupé.
