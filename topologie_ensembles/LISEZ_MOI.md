# Ouvrir Topologie & Ensembles

**Windows :** extraire l’archive puis double-cliquer sur `Lancer_Topologie.cmd`. Python 3.10+ est requis. Le lanceur utilise un environnement existant, ou en prépare un, puis installe NumPy depuis PyPI lors de la première ouverture si nécessaire.

**Linux et macOS :** ouvrir un terminal dans `topologie_ensembles`, puis :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python topologie_ensembles.py
```

Ouvrir **http://127.0.0.1:8777** si le navigateur ne s’ouvre pas automatiquement. Garder le terminal ouvert ; `Ctrl+C` arrête l’application. Si le port est occupé par une autre application, ajouter `--port 8782` au lancement.

Commencer par **Explorer les définitions** : comparer les normes puis tester un point sur une sphère. Chaque laboratoire commence par ses buts, les variables et les techniques à réinvestir. Choisir un cas, faire varier les contrôles, expliquer la différence avec le cours, puis chercher un exercice avant d’ouvrir sa correction.

Les expériences, les cours et les figures fonctionnent hors ligne une fois NumPy installé. Matplotlib est un complément facultatif pour régénérer les illustrations ; il n’est pas nécessaire à l’utilisation du laboratoire.

[Parcours et missions](PARCOURS.md) · [Cours](COURS.md) · [Exercices](EXERCICES.md) · [Présentation complète](README.md).
