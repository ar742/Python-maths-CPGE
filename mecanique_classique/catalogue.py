"""Les 24 laboratoires P1, P2 et P3 de mécanique."""
from catalogue_p1 import LABS as P1
from catalogue_p2 import LABS as P2
from catalogue_p3 import LABS as P3
LABS=P1+P2+P3
LAB_BY_ID={lab['id']:lab for lab in LABS}
