"""Expériences, unités et commandes du neuvième atelier."""
from catalogue_conversion import LABS as CONVERSION
from catalogue_ondes import LABS as ONDES

LABS = CONVERSION + ONDES
LAB_BY_ID = {lab['id']: lab for lab in LABS}

