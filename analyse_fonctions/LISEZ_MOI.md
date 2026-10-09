# Ouvrir Fonctions & Équations

**Windows :** extraire l’archive, puis double-cliquer sur `Lancer_Analyse_Fonctions.cmd`. Python 3.10+ est requis ; le lanceur prépare l’environnement et installe NumPy depuis PyPI si nécessaire.

**Linux ou macOS :** ouvrir un terminal dans `analyse_fonctions`, puis :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python analyse_fonctions.py
```

Ouvrir **http://127.0.0.1:8780** si le navigateur ne s’ouvre pas automatiquement. Garder le terminal ouvert ; `Ctrl+C` arrête l’application. Si le port est occupé, ajouter `--port 8781`.

Commencer par **Frullani**, **Euler / RK4** ou **Faà di Bruno**. Lire les objectifs et le domaine, prévoir un résultat, puis suivre les trois manipulations. Modifier un paramètre, comparer les courbes et les contrôles, puis expliquer le résultat avec les leçons associées. Chercher un exercice avant d’ouvrir sa correction.

Mettre le dessin en pause, déplacer le curseur ou survoler une courbe pour lire les valeurs. Le curseur de lecture ne représente pas un temps physique ; les axes précisent les variables. « Exporter les résultats » télécharge les paramètres, données et hypothèses au format JSON.

[Quatorze séances](PARCOURS.md) · [Cours](COURS.md) · [Exercices](EXERCICES.md) · [Présentation complète](README.md).
