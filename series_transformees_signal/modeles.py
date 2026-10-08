"""Validation publique des paramètres ; résultats finis et exportables."""
from __future__ import annotations
import json
import math
from numbers import Real
from commun import clean
from catalogue import LAB_BY_ID, SERIES, TRANSFORMEES
from modeles_series import calculate as series
from modeles_transformees import calculate as transformees
from modeles_signal import calculate as signal
SERIES_IDS={lab['id'] for lab in SERIES}
TRANSFORMEES_IDS={lab['id'] for lab in TRANSFORMEES}

def calculate(data):
    if not isinstance(data,dict):raise ValueError('Objet de paramètres attendu.')
    lab_id=data.get('lab')
    if not isinstance(lab_id,str) or lab_id not in LAB_BY_ID:raise ValueError('Choisir un laboratoire de Séries & Signaux.')
    supplied=data.get('params',{})
    if not isinstance(supplied,dict):raise ValueError('Objet de paramètres attendu.')
    supplied=dict(supplied)
    supplied.update({key:value for key,value in data.items() if key not in ('lab','params')})
    controls=LAB_BY_ID[lab_id]['controls']
    if set(supplied)-{control['key'] for control in controls}:raise ValueError('Paramètre inconnu pour cette expérience.')
    params={}
    for control in controls:
        value=supplied.get(control['key'],control['value'])
        if control['type']=='select':
            if not isinstance(value,str) or value not in [o['value'] for o in control['options']]:raise ValueError('Choix invalide : '+control['label'])
        else:
            if isinstance(value,bool) or not isinstance(value,Real):raise ValueError('Nombre attendu : '+control['label'])
            try:value=float(value)
            except (ValueError,OverflowError,TypeError):raise ValueError('Nombre fini attendu : '+control['label']) from None
            if not math.isfinite(value) or not control['min']<=value<=control['max']:raise ValueError('Valeur hors des bornes : '+control['label'])
            if control.get('integer') and not value.is_integer():raise ValueError('Entier attendu : '+control['label'])
        params[control['key']]=value
    engine=series if lab_id in SERIES_IDS else transformees if lab_id in TRANSFORMEES_IDS else signal
    answer=clean(engine(lab_id,params));answer.update(lab=lab_id,params=params)
    json.dumps(answer,allow_nan=False)
    return answer
