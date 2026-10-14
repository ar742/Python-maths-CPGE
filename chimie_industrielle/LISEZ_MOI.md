# Ouvrir Chimie pour l’industrie

1. Télécharger puis extraire **Python-maths-CPGE.zip**.
2. Sous Windows, double-cliquer sur **Lancer_Chimie_Industrie.cmd**, à la racine ou dans ce dossier.
3. Le navigateur ouvre **http://127.0.0.1:8786**. Choisir une expérience, lire son but et ses notations, puis suivre les trois premiers gestes.

Python **3.10 ou plus récent** est requis. À la première ouverture, une connexion permet d’installer NumPy et SymPy si nécessaire. Les TP fonctionnent ensuite hors ligne. Fermer la fenêtre de lancement arrête le serveur.

Commencer par l’horloge iodée, les bilans de combustion et la pile Daniell. Le [parcours de douze séances](PARCOURS.md) organise ensuite les procédés et les compléments. Le menu **Cours & exercices** donne accès aux 48 leçons, 72 TD corrigés et 24 figures.

**Exporter les résultats** conserve les paramètres, tableaux, bilans, hypothèses et données des figures en JSON. Les références industrielles s’ouvrent en ligne.

## Lancement manuel

Dans ce dossier :

```bash
python -m venv .venv
```

Sous Windows :

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -X utf8 chimie_industrielle.py
```

Sous Linux ou macOS :

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python chimie_industrielle.py
```

Si le port est occupé, ajouter `--port 8787`. Pour choisir le navigateur, ajouter `--no-browser`.

## Lire et régénérer les documents

[Cours](COURS.md) · [Exercices](EXERCICES.md) · [Séances](PARCOURS.md) · [Repères](MATRICE_PROGRAMME.md) · [Applications](APPLICATIONS_INDUSTRIELLES.md).

```bash
python export_cours.py
python -m pip install -r requirements-illustrations.txt
python chimie_industrielle.py --export-illustrations
```

Les valeurs sont liées aux hypothèses affichées. Une carte numérique sert à observer ; les bilans et les preuves expliquent ce que le résultat établit.

## Parcours progressif sup / spé

Ouvrir **Parcours sup / spé** dans l’atelier : techniques incontournables, approfondissements accompagnés et prolongements au-delà du programme. Chaque séance donne un but, un travail, un acquis attendu et ses limites, avec accès direct aux TP et retour à la séance. Le [parcours autonome](PARCOURS_PROGRESSIF.md) est aussi consultable sans lancer le serveur.

[Errata des formules](errata.md) : corrections vérifiées dans les fiches C6–C8 du recueil, avec pages, conventions et contrôles.
