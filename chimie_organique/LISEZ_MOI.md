# Premiers pas — Liaisons & Synthèses

1. Installer Python 3.10 ou plus récent, puis double-cliquer sur `Lancer_Chimie_Organique.cmd` à la racine du dépôt. L’installation initiale de NumPy demande une connexion ; les expériences fonctionnent ensuite hors ligne.
2. Ouvrir <http://127.0.0.1:8775> si la page ne s’ouvre pas automatiquement.
3. Commencer par **RMN**, **SN2** ou **Rétrosynthèse**, selon votre objectif. Lire l’introduction : but, variables et hypothèses précèdent les réglages.
4. Faire une prédiction, choisir un préréglage, modifier un paramètre et justifier la différence. La commande d’étape parcourt un mécanisme ; un tableau ou un profil énergétique apporte une autre preuve.
5. Ouvrir la leçon associée, chercher l’exercice avant de déplier son corrigé, puis poursuivre une [mission](PARCOURS.md).

**Structure → réactivité → synthèse → contrôle** : les quatre questions reviennent dans les trente laboratoires. Les repères Sup, Spé et Au-delà situent les techniques ; la [matrice du programme](MATRICE_PROGRAMME.md) précise la filière.

[Présentation complète](README.md) · [Cours et 60 exercices corrigés](COURS.md) · [Trente illustrations](illustrations/README.md).

## Si le démarrage échoue

Le lanceur affiche le problème rencontré. Vérifier que Python est installé et que l’installation initiale de NumPy a abouti. Un port déjà utilisé se contourne avec :

```sh
python -X utf8 chimie_organique.py --port 8780
```

Dans ce cas, ouvrir <http://127.0.0.1:8780>. Le navigateur affiche les cours et calculs de votre propre ordinateur ; fermer la fenêtre de lancement termine le serveur.
