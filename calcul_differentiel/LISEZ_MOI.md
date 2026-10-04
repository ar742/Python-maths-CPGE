# Ouvrir le quatrième volet

Télécharger le dépôt avec **Code → Download ZIP**, puis extraire l’archive.
Python **3.10 ou plus récent** est requis.

## Windows

Double-cliquer sur **Lancer_Calcul_Differentiel.cmd**, à la racine ou dans ce dossier.
Le lanceur utilise l’environnement Python du dépôt s’il existe, sinon en crée un.
Il installe NumPy depuis PyPI si NumPy manque : cette première étape demande Internet.
L’atelier fonctionne ensuite hors ligne et s’ouvre sur http://127.0.0.1:8768/.
Garder le terminal ouvert. **Ctrl+C** arrête le serveur.

## Lancement manuel, tous systèmes

Depuis `calcul_differentiel` :

```console
python -m venv .venv
```

Activer cet environnement sous Windows :

```console
.venv\Scripts\activate
```

Ou sous Linux/macOS :

```console
source .venv/bin/activate
```

Puis :

```console
python -m pip install -r requirements.txt
python calcul_differentiel.py
```

Utiliser `python3` à la place de `python` si nécessaire. NumPy est la seule
dépendance de l’application. Le fichier HTML seul ne démarre pas les calculs.
L’application n’utilise aucun CDN, aucun compte et aucun service de calcul distant.

## Si le navigateur ne s’ouvre pas

Ouvrir l’adresse affichée dans le terminal. Pour démarrer sans ouverture automatique :

```console
python calcul_differentiel.py --no-browser
```

Si un autre programme occupe le port :

```console
python calcul_differentiel.py --port 8769
```

Un second lancement sur le port d’un atelier déjà démarré rouvre cet atelier.
Fermer le terminal arrête le serveur ; il ne s’agit pas d’une installation permanente.

## Utiliser les laboratoires

Choisir un onglet, ouvrir un exemple puis déplacer les curseurs. Les paramètres
sans effet dans le mode choisi sont grisés. Les points critiques fractionnaires des
exemples utilisent leur valeur exacte, même si le curseur ne peut représenter toutes
les fractions. Une valeur numérique très petite n’est pas une preuve d’égalité.

Les graphiques des restes ont des échelles logarithmiques et un plancher visuel
à 10⁻¹⁶. Les valeurs brutes sont conservées dans le JSON. Les vues 3D sont des
projections dont les axes sont indiqués ; aucune profondeur interactive n’est cachée.

**Exporter les résultats** enregistre l’expérience affichée dans le dossier de
téléchargements du navigateur. Le serveur conserve les quatre dernières expériences
pour le téléchargement ; si un export a expiré, recalculer l’expérience.

## Compléments facultatifs

Le cours reste lisible dans **COURS.md**, sans serveur. **PARCOURS.md** propose des
séances avec objectifs, manipulations et questions de rédaction.
SymPy est facultatif pour `tp_symbolique.py` ; Matplotlib est facultatif pour
régénérer les illustrations. Les figures SVG fournies s’ouvrent dans un navigateur
et peuvent être insérées dans des fiches.

```console
python -m pip install -r requirements-symbolique.txt
python tp_symbolique.py
python -m pip install -r requirements-illustrations.txt
python illustrations.py
python -X utf8 -m unittest -v test_mathematiques
```

Les sources personnelles PDF/TXT ne sont pas requises pour exécuter le programme.
