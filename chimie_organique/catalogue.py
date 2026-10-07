"""Trente explorations de la chimie organique, du signal à la synthèse."""
from catalogue_reactivite import LABS as REACTIVITE
from catalogue_analyse import LABS as ANALYSE
LABS = ANALYSE + REACTIVITE
LAB_BY_ID = {lab['id']: lab for lab in LABS}
