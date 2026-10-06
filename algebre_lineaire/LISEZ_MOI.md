# Ouvrir Algèbre & Réductions

1. Télécharger [Python-maths-CPGE](https://github.com/ar742/Python-maths-CPGE) avec **Code → Download ZIP**, puis **extraire** l’archive.
2. Disposer de **Python 3.10 ou plus récent**, installé depuis [python.org](https://www.python.org/downloads/). Sous Windows, activer l’ajout de Python au PATH si l’installateur le propose.
3. Double-cliquer sur **Lancer_Algebre_Lineaire.cmd** à la racine du dossier. Le premier lancement installe NumPy et SymPy au besoin.
4. Garder la fenêtre du programme ouverte. L’atelier s’affiche dans le navigateur à <http://127.0.0.1:8771>.

Les dix-sept laboratoires, vingt-cinq leçons et quarante exercices corrigés fonctionnent ensuite hors ligne. **Ctrl+C** arrête le serveur.

## Premier essai

Lire d'abord le bloc **But du TP et lien avec le cours** : il annonce ce que l'expérience doit vous apprendre et les techniques à mobiliser. Les repères **Sup**, **Spé** et **Au-delà** distinguent les acquis de votre niveau des prolongements à découvrir. Les boutons ouvrent les leçons de préparation ; **Un premier parcours en trois gestes** propose les premières manipulations à justifier.

Depuis l’accueil, ouvrir **Réseaux & Laplacien** : diminuer la conductance du pont, observer le mode lent, puis couper le pont. Explorer ensuite **Jacobi** pour suivre la compensation de trois doubles crochets non nuls, et **Mécanique symplectique** pour comparer Cayley à Euler sur deux oscillateurs couplés. Dans **Dunford**, choisir le TP du recueil et parcourir les étapes du calcul. Les [dix missions progressives](PARCOURS.md) guident la suite.

## Saisir les matrices

- Matrice : `1 2/3;0 1` ou une ligne par retour à la ligne. Les espaces séparent les coefficients. Les fractions gardent leur valeur exacte.
- Vecteur : `1;2;3`. Pour Gauss, le nombre de composantes doit correspondre au nombre de lignes de A.
- Cliquer sur **Appliquer les données** après une saisie. Un message décrit les entrées incompatibles.
- Dans Spectre/Jordan, Dunford, Cyclique et Cayley, choisir **Votre matrice rationnelle**. La taille maximale est 4×4. Le choix du corps appartient aux laboratoires de réduction.
- **Exporter les résultats** télécharge un fichier JSON contenant le dernier calcul validé. Après une modification, recalculer avant d’exporter.

## Sur Linux, macOS ou dans un terminal Windows

```sh
cd algebre_lineaire
python -m pip install -r requirements.txt
python algebre_lineaire.py
```

Utiliser `python3` selon le système. Si le port est occupé par une autre application :

```sh
python algebre_lineaire.py --port 8773
```

Le terminal indique l’adresse à ouvrir. `--no-browser` permet de lancer le serveur sans ouvrir automatiquement le navigateur. Ouvrir `index.html` seul ne lance pas les calculs.

[Présentation](README.md) · [Cours autonome](COURS.md) · [Clarifications du recueil](ERRATA.md) · [Galerie scientifique](illustrations/README.md)
