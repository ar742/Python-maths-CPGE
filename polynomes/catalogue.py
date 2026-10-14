"""Les quatre parcours de l’atelier Polynômes."""
from catalogue_classiques import LABS as L0
from catalogue_arithmetique import LABS as L1
from catalogue_complexes import LABS as L2
from catalogue_multivaries import LABS as L3
LABS=L0+L1+L2+L3
LAB_BY_ID={l['id']:l for l in LABS}
