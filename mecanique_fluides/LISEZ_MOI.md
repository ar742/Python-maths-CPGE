# Première ouverture — Fluides & Ondes

À la racine du dépôt, double-cliquer sur **Lancer_Mecanique_Fluides.cmd**. Le navigateur ouvre l’atelier local à l’adresse <http://127.0.0.1:8772>. Il faut Python 3.10 ou plus ; NumPy est installé par le lanceur si nécessaire. La première installation demande une connexion, puis les expériences fonctionnent hors ligne.

Sur Windows, Linux ou macOS, dans ce dossier :

```text
python -m pip install -r requirements.txt
python -X utf8 mecanique_fluides.py
```

Garder la fenêtre du programme ouverte pendant l’utilisation. Pour fermer, utiliser Ctrl+C dans cette fenêtre. Un autre port peut être choisi avec `--port 8774`. L’option `--no-browser` permet de lancer le serveur sans ouvrir un onglet.

## Un premier essai

1. Ouvrir **Couette–Poiseuille**. Lire « But du TP et lien avec le cours », puis les repères **sup**, **spé** et **au-delà**. Ils indiquent les outils à réinvestir, sans faire de toutes les extensions des attendus de chaque filière.
2. Choisir **Couette pur** et prévoir le profil avant de regarder la figure. Comparer ensuite **Pression motrice** et **Débit nul mais mouvement** : un débit nul n’impose pas une vitesse nulle partout.
3. Déplier **Un premier parcours en trois gestes**, puis suivre les liens vers les leçons pour justifier l’observation avec les conditions aux limites.
4. Explorer **Houle** : observer la propagation de la crête et les orbites des particules. La vitesse de groupe se lit sur les courbes et dans les résultats ; le temps de l’animation est adapté et les échelles visuelles sont adaptées.

La page d’accueil regroupe les expériences en fondations, écoulements, ondes et passerelles. Les commandes donnent les unités de saisie ; les résultats donnent les unités des grandeurs calculées. **Pause** immobilise la scène animée ; les courbes représentent les calculs Python. **Exporter les résultats** enregistre un instantané JSON de l’expérience courante.

## Étudier et prolonger

Le bouton **Cours & exercices** donne accès aux leçons, aux corrections dépliables et aux figures autonomes. [COURS.md](COURS.md) permet une lecture imprimable sans lancer le serveur. [PARCOURS.md](PARCOURS.md) propose des missions.

Les modèles idéalisés sont explicités : couche limite laminaire, circulation prescrite pour Magnus, tourbillon de Rankine horizontal, acoustique linéaire, MHD simplifiée. Le laboratoire de Navier–Stokes étudie une solution périodique 2D ; l’ouverture sur le problème du millénaire figure dans le cours avec des sources datées.
