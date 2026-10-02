# Rubik & Groupes — un laboratoire de mathématiques

Application Python illustrée en français, niveau maths sup / maths spé. Le moteur
mathématique est en Python ; le navigateur sert à afficher et manipuler les schémas.

## Lancer le programme

Sous Windows, double-cliquer sur **Lancer_Rubik.cmd**. Une fenêtre de lancement
reste ouverte et le cours s'ouvre dans le navigateur. Le lanceur utilise Python
installé sur la machine. Si Codex est installé avec son environnement Python,
le lanceur peut également utiliser ce dernier.

Sur tout système avec Python **3.10 ou plus récent** :

```console
python rubik_groupes.py
```

Adresse par défaut : <http://127.0.0.1:8765>. Le programme n'écoute que sur la
machine locale. Le cours fonctionne sans connexion et sans installation de
bibliothèque. Garder la fenêtre de lancement ouverte pendant l'utilisation.
Pour arrêter, utiliser Ctrl+C dans cette fenêtre. Si le port est occupé :

```console
python rubik_groupes.py --port 8766
```

L'option `--no-browser` permet de démarrer sans ouvrir automatiquement une page.
Ouvrir `index.html` directement ne suffit pas : le moteur Python doit fonctionner.

## Contenu et manipulations

- **Cours & cube** : dix leçons, avec définitions, démonstrations, exemples et une
  expérience animée par leçon. Du groupe engendré par les faces aux stabilisateurs,
  invariants, graphe de Cayley et sous-groupe de la résolution à deux phases.
- **Laboratoire** : inverse et réduction locale d'un mot, ordre exact, cycles des
  coins, arêtes et facettes, comparaison AB/BA, commutateurs et conjugaison.
- **Résolution** : mélange court ou long, défi de trois coins, solution à jouer
  entièrement ou geste par geste, import et validation d'une configuration.
- **Exercices** : douze problèmes progressifs avec corrections masquées et exemples
  à manipuler. Les thèmes avancés sont signalés ; selon la filière, les actions de
  groupes et produits semi-directs servent d'approfondissement.

Le cube peut être observé sous tous les angles en le faisant glisser. La caméra
ne modifie jamais le repère des mouvements. Le patron montre les six faces vues
de l'extérieur. Les contours dorés marquent les facettes différentes du cube
résolu ; on peut afficher leurs repères U1 à B9. La position courante et
l'historique sont sauvegardés dans le navigateur, lorsque le stockage local est
autorisé.

### Convention mathématique

Un mot se lit de gauche à droite : `R U` signifie R, puis U, donc U ∘ R avec
la composition usuelle des fonctions. Une face est tournée dans le sens horaire
lorsqu'elle est regardée de l'extérieur. `R'` est l'inverse ; `R2` est le demi-tour.
Le programme accepte les six faces URFDLB et ces suffixes, avec ou sans espaces.
Il ne gère pas les rotations globales x/y/z, les mouvements de tranches M/E/S
ni les tours larges. Les six centres sont fixes et leurs logos ne sont pas suivis.

Les cycles de pièces décrivent **pièce d'origine → emplacement actuel** et ne
retiennent pas l'orientation. Les tableaux indiquent au contraire, à chaque place,
la pièce présente et son orientation. Le calcul de l'ordre utilise les facettes
et conserve donc toutes les orientations. Le moteur est construit par rotations
géométriques entières ; aucune table de mouvements n'est recopiée.

## Les méthodes de résolution et leurs limites

1. **Inverse de l'historique** : résout tout mélange créé dans l'application dont
   l'historique est connu. La réduction locale ne garantit pas une solution minimale.
2. **Recherche courte** : exploration en largeur bidirectionnelle, sans lire
   l'historique, jusqu'à six mouvements HTM. En HTM, un quart de tour, son inverse
   et un demi-tour coûtent chacun 1. Une solution trouvée est minimale ; un échec
   à la borne ne signifie pas que le cube est impossible. Une limite de temps est
   signalée séparément.
3. **Résolution générale** : adaptateur vers le module externe facultatif
   `kociemba`. Il permet de résoudre un état légal importé sans historique, même
   si la recherche courte ne suffit pas. Toute solution est vérifiée dans le
   moteur de l'application avant d'être proposée. La méthode à deux phases n'est
   pas une garantie de longueur minimale globale.

### Installer le solveur général facultatif

Avec le même Python que celui qui lance l'application :

```console
python -m pip install -r requirements-optionnels.txt
```

Puis arrêter et relancer le programme. Le bouton « Résoudre par deux phases »
s'active si le module est détecté. L'installation demande une connexion ; selon
la plateforme et les paquets disponibles, des outils de compilation peuvent être
nécessaires. Le cours reste utilisable si cette installation n'est pas faite.
Le module est une dépendance séparée, avec son propre code et sa licence GPL-2.0 :
[dépôt officiel du module](https://github.com/muodov/kociemba).

### Importer un cube

Saisir 54 lettres, dans l'ordre des faces **U R F D L B**, neuf par face, chaque
face regardée de l'extérieur. Les espaces et retours à la ligne sont ignorés.
Une lettre désigne la couleur du centre de cette face, indépendamment du choix
commercial des couleurs. Exemple résolu :

```text
UUUUUUUUU
RRRRRRRRR
FFFFFFFFF
DDDDDDDDD
LLLLLLLLL
BBBBBBBBB
```

L'import vérifie le nombre de couleurs, les centres, l'unicité des pièces,
l'absence de coins miroirs et les trois contraintes de résolubilité. Il est
refusé si un test échoue et le cube courant est conservé. Pour une recherche
courte indépendante de l'historique, créer un mélange de quatre gestes puis
cliquer « Oublier l'historique ».

## Illustrations et code

Le dossier `illustrations` contient des schémas SVG autonomes, lisibles dans un
navigateur, utilisables dans un cours et exportables en image. Pour les régénérer :

```console
python rubik_groupes.py --export-illustrations
```

- `cube.py` : permutations, rotations, coordonnées des pièces, invariants et recherches.
- `cours.py` : textes, expériences et exercices.
- `rubik_groupes.py` : application locale et adaptateur du solveur optionnel.
- `app.js`, `style.css`, `index.html` : interface et dessin des illustrations.
- `test_cube.py` : vérifications mathématiques et tests de l'application.

Pour vérifier les calculs et le serveur :

```console
python -m unittest -v test_cube
```

## Sources pour approfondir

Le cours est rédigé pour cette application. Les références complémentaires et
les conventions d'orientation sont accessibles depuis « Références du cours » :

- [Janet Chen, Group Theory and the Rubik's Cube](https://people.math.harvard.edu/~jjchen/docs/Group%20Theory%20and%20the%20Rubik%27s%20Cube.pdf).
- [Herbert Kociemba, The Cubie Level](https://kociemba.org/math/cubielevel.htm).
- [Herbert Kociemba, The Two-Phase Algorithm](https://kociemba.org/math/twophase.htm).

Le cardinal calculé est 8! × 12! × 3⁷ × 2¹¹ / 2 =
**43 252 003 274 489 856 000**. Les hypothèses sont celles du cube standard 3×3,
à centres fixes et avec les pièces correctes.
