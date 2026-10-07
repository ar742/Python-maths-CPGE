"""Les expériences géométriques et ondulatoires du même atelier."""
from catalogue_geometrie import LABS as GEOMETRIE
from catalogue_ondes import LABS as ONDES
LABS = GEOMETRIE + ONDES
LAB_BY_ID = {lab['id']: lab for lab in LABS}
