"""Réactions du recueil, expériences associées et outils de caractérisation."""
from catalogue_reactivite import LABS as REACTIVITE
from catalogue_analyse import LABS as ANALYSE
from catalogue_recueil import LABS as RECUEIL
from catalogue_exos_recueil import LABS as EXOS_RECUEIL
from catalogue_epoxydes import LABS as EPOXYDES
BASE_LABS = ANALYSE + REACTIVITE
LABS = RECUEIL + EXOS_RECUEIL + EPOXYDES + REACTIVITE + ANALYSE
LAB_BY_ID = {lab['id']: lab for lab in LABS}
