# Ouvrir Électricité & Technologies

1. Télécharger puis extraire l’archive **Python-maths-CPGE.zip** ; ne pas lancer depuis l’archive.
2. Sous Windows, double-cliquer sur **Lancer_Electricite.cmd**, à la racine ou dans ce dossier.
3. Le navigateur ouvre **http://127.0.0.1:8783**. Choisir un TP, lire son guide puis commencer par les exemples proposés. Le menu « Cours & exercices » donne les leçons et corrigés.

La première ouverture installe NumPy si nécessaire : une connexion Internet est alors requise. Les ouvertures suivantes fonctionnent hors ligne. Une fenêtre de lancement reste ouverte ; la fermer arrête l’atelier. Les réglages sont locaux. « Exporter les résultats » télécharge les paramètres, les courbes et les hypothèses en JSON.

## Lancement manuel

Python 3.10 ou plus récent est requis. Ouvrir un terminal dans le dossier `electricite_technologies` :

```bash
python -m venv .venv
```

Puis sous Windows :

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -X utf8 electricite.py
```

Sous Linux ou macOS :

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python electricite.py
```

Si le port est occupé, ajouter `--port 8784`. Pour garder la main sur le navigateur, ajouter `--no-browser`. L’adresse exacte s’affiche dans le terminal. L’application reconnaît une instance déjà ouverte de ce même atelier.

## Consulter sans serveur

[COURS.md](COURS.md), [EXERCICES.md](EXERCICES.md), [PARCOURS.md](PARCOURS.md) et les [figures SVG](illustrations/README.md) sont des documents autonomes. Aucun PDF personnel n’est inclus.

## Régénérer les documents

```bash
python export_cours.py
python -m pip install -r requirements-illustrations.txt
python electricite.py --export-illustrations
```

Les illustrations livrées sont déjà générées. Leur régénération ne change ni les paramètres initiaux ni les modèles.
