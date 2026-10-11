"""Trois parcours ; priorité à la commande et au traitement numérique de P17."""
from catalogue_commande import LABS as P1
from catalogue_circuits import LABS as P2
from catalogue_analogique import LABS as P3
LABS=P1+P2+P3
LAB_BY_ID={lab['id']:lab for lab in LABS}
