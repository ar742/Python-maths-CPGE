# Lancer Séries & Signaux

Sous Windows, ouvrir `Lancer_Series_Signaux.cmd`. Le programme utilise Python 3.10+ et NumPy ; la première installation de NumPy demande une connexion Internet. Les ouvertures suivantes fonctionnent hors ligne.

Si Python n’est pas installé, l’installer depuis [python.org](https://www.python.org/downloads/), avec l’option d’ajout au PATH. Relancer le fichier après installation.

L’atelier est disponible sur <http://127.0.0.1:8776>. Garder la fenêtre du programme ouverte pendant les expériences ; `Ctrl+C` ferme le serveur.

Pour un lancement manuel, dans ce dossier :

```bash
python -m pip install -r requirements.txt
python series_transformees_signal.py
```

Si le port est occupé par une autre application :

```bash
python series_transformees_signal.py --port 8781
```

Choisir un laboratoire, lire **But du TP et lien avec le cours**, essayer les trois premières manipulations et confronter la conjecture aux démonstrations. Les préréglages montrent des cas contrastés ; les curseurs changent les paramètres et recalculent les résultats. **Cours & exercices** donne les corrections guidées ; **Exporter les résultats JSON** conserve les calculs affichés.

[Programme complet](README.md) · [Missions](PARCOURS.md).
