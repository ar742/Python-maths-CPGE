"""Validation publique des paramètres ; résultats finis et exportables."""
from __future__ import annotations
import json
import math
from numbers import Real
from commun import clean
from catalogue import LAB_BY_ID, GEOMETRIE, ANALYSE
from modeles_geometrie import calculate as geometrie
from modeles_analyse import calculate as analyse
from modeles_ensembles import calculate as ensembles
GEOMETRIE_IDS={lab['id'] for lab in GEOMETRIE}
ANALYSE_IDS={lab['id'] for lab in ANALYSE}

def calculate(data):
    if not isinstance(data,dict):raise ValueError('Objet de paramètres attendu.')
    lab_id=data.get('lab')
    if not isinstance(lab_id,str) or lab_id not in LAB_BY_ID:raise ValueError('Choisir un laboratoire de Topologie & Ensembles.')
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
    engine=geometrie if lab_id in GEOMETRIE_IDS else analyse if lab_id in ANALYSE_IDS else ensembles
    answer=clean(engine(lab_id,params));answer.update(lab=lab_id,params=params)
    json.dumps(answer,allow_nan=False)
    return answer
