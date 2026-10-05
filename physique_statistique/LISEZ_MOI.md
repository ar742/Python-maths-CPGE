# Ouvrir le volet de physique statistique

Sous Windows, double-cliquer sur **Lancer_Physique_Statistique.cmd** à la racine du dépôt. Python 3.10 ou plus récent est requis. La première ouverture installe NumPy si nécessaire ; garder la fenêtre ouverte pendant l'utilisation.

Le navigateur ouvre <http://127.0.0.1:8770>. Sur les autres systèmes :

```sh
cd physique_statistique
python -m pip install -r requirements.txt
python physique_statistique.py
```

Selon le système, utiliser `python3` au lieu de `python`. Pour choisir une autre adresse locale : `python physique_statistique.py --port 8772`. `Ctrl+C` arrête l'atelier.

Les expériences fonctionnent hors ligne après installation. GitHub présente les sources, le cours et les illustrations ; les calculs sont exécutés sur votre ordinateur. Ouvrir `index.html` seul ne lance pas Python.

Commencer par [le parcours de sept séances](PARCOURS.md), puis consulter [le cours et les corrections](COURS.md). Les résultats s'exportent en JSON depuis chaque laboratoire.
