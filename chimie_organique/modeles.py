"""Validation des paramètres puis calcul, dans un cadre pédagogique explicite."""
from __future__ import annotations
import json
import math
from numbers import Real
from commun import clean
from catalogue import LAB_BY_ID
from catalogue_reactivite import LABS as REACTIVITE
from modeles_reactivite import calculate as reactivite
from modeles_analyse import calculate as analyse

REACTIVITE_IDS = {lab['id'] for lab in REACTIVITE}

def calculate(data):
    if not isinstance(data,dict): raise ValueError('Les paramètres attendent un objet.')
    lab_id = data.get('lab')
    if not isinstance(lab_id,str) or lab_id not in LAB_BY_ID:
        raise ValueError('Choisir un laboratoire de chimie organique.')
    supplied = data.get('params',{})
    if not isinstance(supplied,dict): raise ValueError('Les paramètres attendent un objet.')
    supplied = dict(supplied)
    supplied.update({key:value for key,value in data.items() if key not in ('lab','params')})
    controls = LAB_BY_ID[lab_id]['controls']
    if set(supplied)-{control['key'] for control in controls}:
        raise ValueError('Paramètre inconnu pour cette expérience.')
    params = {}
    for control in controls:
        value = supplied.get(control['key'],control['value'])
        if control['type']=='select':
            if not isinstance(value,str) or value not in [o['value'] for o in control['options']]:
                raise ValueError('Choix invalide : '+control['label'])
        else:
            if isinstance(value,bool) or not isinstance(value,Real):
                raise ValueError('Nombre attendu : '+control['label'])
            try: value=float(value)
            except (ValueError,OverflowError,TypeError):
                raise ValueError('Nombre fini attendu : '+control['label']) from None
            if not math.isfinite(value) or not control['min']<=value<=control['max']:
                raise ValueError('Valeur hors des bornes : '+control['label'])
            if control.get('integer') and not value.is_integer():
                raise ValueError('Un entier est attendu : '+control['label'])
        params[control['key']] = value
    result=(reactivite if lab_id in REACTIVITE_IDS else analyse)(lab_id,params)
    if not isinstance(result,dict): raise TypeError('Résultat scientifique invalide.')
    result=clean(result)
    result.update(lab=lab_id,params=params)
    json.dumps(result,allow_nan=False)
    return result
