# Neuf illustrations scientifiques — physique quantique

Ces figures accompagnent le [parcours](../PARCOURS.md) et le [cours](../COURS.md). Elles sont produites par Matplotlib à partir des modèles Python de l’atelier. Les unités et approximations figurent dans chaque laboratoire.

## Boîte cubique : superposition et densité marginale

![Superposition de deux états d’une boîte cubique](boite.svg)

## Heisenberg : gaussienne libre

![Étalement d’un paquet gaussien et impulsion conservée](heisenberg.svg)

## Barrière : réflexion et tunnel

![Potentiel et amplitudes de la barrière](diffusion.svg)

## Oscillateur : niveau n = 3

![Fonction propre et niveaux d’énergie](oscillateur.svg)

## Intrication : probabilités de Bell

![Probabilités conjointes et corrélations](intrication.svg)

## SQUID : deux jonctions différentes

![Interférence et somme des courants](josephson.svg)

## RMN : Rabi avec désaccord

![Oscillations et trajectoire de Bloch en projection](rabi.svg)

## Bloch : rotation du qubit

![Sphère de Bloch en projection et mesure Z](bloch.svg)

## Informatique : une itération de Grover

![Probabilités finales et étapes de Grover](circuits.svg)

Pour régénérer ces illustrations depuis le dossier `physique_quantique` :

```sh
python -m pip install -r requirements-illustrations.txt
python physique_quantique.py --export-illustrations
```
