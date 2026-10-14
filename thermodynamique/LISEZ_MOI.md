# Commencer Chaleur & Transferts

1. Sous Windows, ouvrir `Lancer_Thermodynamique.cmd`.
2. Attendre l’ouverture de **http://127.0.0.1:8782** dans le navigateur.
3. Commencer par **Diffusion dans une barre** : lire le but et les variables, prévoir l’évolution, puis essayer les trois manipulations proposées.

La première installation de NumPy nécessite Internet. Ensuite, les calculs et les cours fonctionnent localement, hors ligne. Garder la fenêtre de lancement ouverte ; pour arrêter, appuyer sur **Ctrl+C**.

## Lancement manuel

Dans ce dossier, avec Python 3.10 ou plus :

```bash
python -m pip install -r requirements.txt
python thermodynamique.py
```

Si le port est occupé par une autre application : `python thermodynamique.py --port 8783`. Ouvrir alors **http://127.0.0.1:8783**. Si cet atelier fonctionne déjà sur le port demandé, le lancement reconnaît sa session.

L’onglet **Cours & exercices** relie chaque leçon à son TP. Les fichiers [COURS.md](COURS.md), [EXERCICES.md](EXERCICES.md) et [PARCOURS.md](PARCOURS.md) permettent aussi de travailler directement sur GitHub.

Le bouton **Exporter les résultats** télécharge les paramètres, les courbes, les bilans et les hypothèses au format JSON. Les quatre derniers calculs restent disponibles pendant la session ; un export plus ancien nécessite de refaire le calcul.

Pour régénérer les illustrations : installer `requirements-illustrations.txt`, puis lancer `python thermodynamique.py --export-illustrations`. Ces dépendances sont facultatives pour utiliser les figures déjà fournies.

## Parcours progressif sup / spé

[Lire le parcours](PARCOURS_PROGRESSIF.md) : techniques prioritaires, applications accompagnées de CPGE et branches au-delà du programme. Dans l’atelier lancé, choisir **Parcours sup / spé**. Chaque séance ouvre directement ses TP et permet de revenir à la séance.
