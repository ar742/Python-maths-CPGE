# Ouvrir Mécanique & Mouvements

**Windows :** extraire l’archive puis double-cliquer sur `Lancer_Mecanique.cmd`. Python 3.10+ est requis. Le lanceur utilise un environnement existant, ou en prépare un, puis installe NumPy depuis PyPI si nécessaire.

**Linux et macOS :** ouvrir un terminal dans `mecanique_classique`, puis :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python mecanique_classique.py
```

Ouvrir **http://127.0.0.1:8778** si le navigateur ne s’ouvre pas automatiquement. Garder le terminal ouvert ; `Ctrl+C` arrête l’application. Si le port est occupé, ajouter `--port 8779`.

Commencer par l’une des trois portes d’entrée : **Kepler**, **deux ressorts transverses** ou **cylindre au bord de la table**. Lire le but et les conventions, prévoir le résultat, puis suivre les trois manipulations proposées. Choisir un exemple, faire varier un paramètre, comparer les graphiques et justifier avec le cours. Chercher un exercice avant d’ouvrir sa correction.

La pause et le curseur de lecture permettent d’examiner un état précis. Faire glisser une scène 3D pour changer le point de vue. « Exporter les résultats » télécharge les paramètres, données, bilans et hypothèses au format JSON.

Les expériences fonctionnent hors ligne après installation de NumPy. Matplotlib, facultatif, permet de régénérer les figures.

[Douze séances](PARCOURS.md) · [Cours](COURS.md) · [Exercices](EXERCICES.md) · [Présentation complète](README.md).
