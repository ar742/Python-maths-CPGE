# Prendre en main Champs & Matière

Double-cliquer sur **Lancer_Electromagnetisme.cmd** à la racine du dépôt.
La fenêtre reste ouverte pendant l’utilisation et le navigateur affiche
<http://127.0.0.1:8773>. Python 3.10+ et NumPy sont nécessaires ; après leur
installation, l’atelier fonctionne hors ligne.

1. Choisir une expérience dans les cartes ou le menu.
2. Lire **But du TP et lien avec le cours** : question, attendu, techniques,
   repères sup / spé / au-delà et premières manipulations.
3. Commencer par un exemple prédéfini, formuler une prédiction, puis modifier
   un seul paramètre à la fois.
4. Comparer la scène, les mesures et les courbes. Les échelles d’animation
   servent à voir ; les unités et valeurs physiques figurent dans les résultats.
5. Justifier avec les équations et les hypothèses, puis ouvrir le corrigé associé.

Trois entrées conseillées :

- **Helmholtz :** comparer d/R=0,5, 1 et 1,5 ; expliquer l’annulation de B″(0).
- **Interface :** incidence normale, Brewster TM et réflexion totale ;
  contrôler les flux plutôt que les seuls carrés d’amplitudes.
- **Haut-parleur :** repérer la résonance et vérifier la réciprocité entre
  force de Laplace et contre-fem.

Le bouton **Pause** fige les animations. Les cartes de champ sont statiques :
leurs lignes orientées ne décrivent pas le mouvement de charges. **Exporter
les résultats** produit un JSON lisible, avec paramètres, tableaux et hypothèses.

[Les dix missions](PARCOURS.md) proposent une progression de plusieurs séances.
[Le cours](COURS.md) rassemble les démonstrations et les 48 corrigés.

Pour choisir un autre port :

```text
python -X utf8 electromagnetisme.py --port 8775
```

Fermer le terminal arrête l’atelier. Si le même atelier est déjà ouvert,
le lanceur reprend son adresse ; une application différente sur le même port
demande d’en choisir un autre.
