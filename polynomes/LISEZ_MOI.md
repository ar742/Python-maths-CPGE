# Ouvrir Polynômes & Géométrie

1. Télécharger puis extraire **Python-maths-CPGE.zip**.
2. Sous Windows, double-cliquer sur **Lancer_Polynomes.cmd**, à la racine ou dans le dossier `polynomes`.
3. Le navigateur ouvre **http://127.0.0.1:8784**. Lire le but et les notations du TP, puis comparer les exemples proposés.

Python **3.10 ou plus récent** est requis. La première ouverture installe NumPy et SymPy si nécessaire ; une connexion Internet est alors nécessaire. Les laboratoires fonctionnent ensuite hors ligne. Fermer la fenêtre de lancement arrête le serveur.

Le menu **Cours & exercices** propose les leçons, les corrections et les figures de référence. **Exporter les résultats** conserve les réglages, valeurs, tableaux, données des figures et hypothèses dans un fichier JSON. Les liens vers les références publiques demandent une connexion.

## Lancement manuel

Dans le dossier `polynomes`, créer un environnement :

```bash
python -m venv .venv
```

Sous Windows :

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -X utf8 polynomes.py
```

Sous Linux ou macOS :

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python polynomes.py
```

Si le port est occupé, ajouter `--port 8785`. Pour choisir vous-même le navigateur, ajouter `--no-browser`.

## Lire les documents autonomes

[COURS.md](COURS.md) · [EXERCICES.md](EXERCICES.md) · [PARCOURS.md](PARCOURS.md) · [MATRICE_PROGRAMME.md](MATRICE_PROGRAMME.md) · [errata.md](errata.md) · [Figures SVG](illustrations/README.md).

Pour les figures : repérer les axes, les objets représentés et les hypothèses. Les calculs exacts certifient les identités ; une grille numérique ou un nuage de racines approchées sert à observer, sans remplacer la preuve.

## Régénérer les documents

```bash
python export_cours.py
python -m pip install -r requirements-illustrations.txt
python polynomes.py --export-illustrations
```
