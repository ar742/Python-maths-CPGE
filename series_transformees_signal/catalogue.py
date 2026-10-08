"""Trente expériences reliées aux fiches M10 et M11."""
from catalogue_series import LABS as SERIES
from catalogue_transformees import LABS as TRANSFORMEES
from catalogue_signal import LABS as SIGNAL
LABS=SERIES+TRANSFORMEES+SIGNAL
LAB_BY_ID={lab['id']:lab for lab in LABS}
