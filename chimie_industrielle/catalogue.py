"""Trois domaines, vingt-quatre expériences industrielles."""
from catalogue_thermo import LABS as THERMO
from catalogue_cinetique import LABS as CINETIQUE
from catalogue_redox import LABS as REDOX
LABS=THERMO+CINETIQUE+REDOX
LAB_BY_ID={lab['id']:lab for lab in LABS}
