"""Trois parcours, en commençant par les transferts et la diffusion."""
from catalogue_diffusion import LABS as P1
from catalogue_potentiels import LABS as P2
from catalogue_effets import LABS as P3
LABS=P1+P2+P3
LAB_BY_ID={lab['id']:lab for lab in LABS}
