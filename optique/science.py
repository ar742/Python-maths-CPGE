"""Données scientifiques partagées : amplitudes, unités et tableaux finis."""
from __future__ import annotations
import math
import numpy as np

def metric(label, value, unit=""):
    return dict(label=label, value=value, unit=unit)

def series(label, x, y):
    return dict(label=label, x=x, y=y)

def chart(title, x_label, y_label, *curves, **scales):
    return dict(title=title, x_label=x_label, y_label=y_label,
                series=list(curves), **scales)

def scene(kind, title, description, **data):
    return dict(kind=kind, title=title, description=description, **data)

def clean(value):
    if isinstance(value, np.ndarray): return clean(value.tolist())
    if isinstance(value, np.generic): return clean(value.item())
    if isinstance(value, dict): return {str(k): clean(v) for k,v in value.items()}
    if isinstance(value, (list,tuple)): return [clean(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ArithmeticError("Un calcul a produit une valeur non finie.")
    if isinstance(value, complex):
        raise ArithmeticError("Exporter une amplitude complexe par ses composantes.")
    return value
