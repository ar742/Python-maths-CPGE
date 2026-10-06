# 24 figures scientifiques originales

Une figure accompagne chaque laboratoire. Le [catalogue](catalogue.json) donne
les titres, les légendes, les conditions de validité et le laboratoire associé.
Les SVG se lisent directement dans le navigateur et restent nets à l’impression.

Les cartes utilisent des **lignes de champ orientées**, sans les présenter
comme des trajectoires ; le contraste des zones proches des sources est borné
pour garder lisible le reste du champ. Les profils, bilans et diagrammes angulaires
portent leurs unités ou leur normalisation. Les courbes sont produites par les
modèles publiés ; les schémas géométriques explicitent leurs conventions.

Pour régénérer la galerie, depuis le dossier `electromagnetisme` :

```text
python -m pip install -r requirements-illustrations.txt
python -X utf8 illustrations.py
```

Matplotlib n’est pas nécessaire pour utiliser les expériences interactives.
Aucune image du PDF de référence n’est copiée dans cette galerie.
