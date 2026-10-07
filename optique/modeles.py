"""Entrée unique : paramètres bornés, données scientifiques exportables."""
from __future__ import annotations
import json
import math
from science import clean
from numbers import Real

from catalogue import LAB_BY_ID
from catalogue_geometrie import LABS as GEOMETRIE
from modeles_geometrie import calculate as geometrie
from modeles_ondes import calculate as ondes

GEOMETRIE_IDS = {lab['id'] for lab in GEOMETRIE}


def calculate(data):
    if not isinstance(data, dict):
        raise ValueError('Une expérience attend un objet de paramètres.')
    lab_id = data.get('lab')
    if not isinstance(lab_id, str) or lab_id not in LAB_BY_ID:
        raise ValueError('Choisir un laboratoire de l’atelier.')
    controls = LAB_BY_ID[lab_id]['controls']
    supplied = data.get('params', {})
    if not isinstance(supplied, dict):
        raise ValueError('Les paramètres doivent former un objet.')
    supplied = dict(supplied)
    supplied.update({k:v for k,v in data.items() if k not in ('lab','params')})
    keys = {c['key'] for c in controls}
    if set(supplied)-keys:
        raise ValueError('Paramètre inconnu pour cette expérience.')
    params = {}
    for c in controls:
        value = supplied.get(c['key'], c['value'])
        if c.get('type') == 'select':
            allowed = [option['value'] for option in c['options']]
            if not isinstance(value, str) or value not in allowed:
                raise ValueError('Choix invalide : '+c['label'])
        else:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValueError('Valeur numérique attendue : '+c['label'])
            try:
                value = float(value)
            except (OverflowError, TypeError, ValueError):
                raise ValueError('Nombre fini attendu : '+c['label']) from None
            if not math.isfinite(value) or not c['min'] <= value <= c['max']:
                raise ValueError('Valeur hors des bornes : '+c['label'])
            if c.get('integer') and not value.is_integer():
                raise ValueError('Un entier est attendu : '+c['label'])
        params[c['key']] = value
    result = (geometrie if lab_id in GEOMETRIE_IDS else ondes)(lab_id,params)
    if not isinstance(result, dict):
        raise TypeError('Résultat scientifique invalide.')
    result = clean(result)
    result['lab'],result['params'] = lab_id,params
    # Refuser une donnée non finie avant toute transmission ou mise en cache.
    json.dumps(result,allow_nan=False)
    return result

