"""Les intégrales à paramètre et les EDO précèdent les prolongements."""
from catalogue_speciales import LABS as S
from catalogue_theoremes import LABS as T
from catalogue_edo import LABS as E
LABS = T[4:] + E + T[:4] + S
LAB_BY_ID = {lab['id']: lab for lab in LABS}
