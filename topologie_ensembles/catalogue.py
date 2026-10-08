"""Trente expériences pour passer de la définition au théorème."""
from catalogue_geometrie import LABS as GEOMETRIE
from catalogue_analyse import LABS as ANALYSE
from catalogue_ensembles import LABS as ENSEMBLES
LABS=GEOMETRIE+ANALYSE+ENSEMBLES
LAB_BY_ID={lab['id']:lab for lab in LABS}
