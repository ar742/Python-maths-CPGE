"""Validation stricte des réglages, puis calcul exact ou numérique."""
import math
from catalogue import LAB_BY_ID
from commun import clean
from modeles_classiques import COMPUTE as C0
from modeles_arithmetique import COMPUTE as C1
from modeles_complexes import COMPUTE as C2
from modeles_multivaries import COMPUTE as C3
COMPUTE={**C0,**C1,**C2,**C3}
def parameters(data):
    if not isinstance(data,dict): raise ValueError('Objet JSON attendu.')
    name=data.get('lab')
    if not isinstance(name,str) or name not in LAB_BY_ID: raise ValueError('Laboratoire inconnu.')
    supplied=data.get('params',{k:v for k,v in data.items() if k!='lab'})
    if not isinstance(supplied,dict): raise ValueError('Paramètres invalides.')
    controls=LAB_BY_ID[name]['controls']
    if set(supplied)-{c['key'] for c in controls}: raise ValueError('Paramètre inconnu pour ce laboratoire.')
    params={}
    for c in controls:
        value=supplied.get(c['key'],c['value'])
        if c['type']=='select':
            if not isinstance(value,str) or value not in {o['value'] for o in c['options']}: raise ValueError('Choix invalide : '+c['label'])
        else:
            if isinstance(value,bool) or not isinstance(value,(int,float)): raise ValueError('Nombre attendu : '+c['label'])
            try: value=float(value)
            except OverflowError as exc: raise ValueError('Nombre trop grand.') from exc
            if not math.isfinite(value) or not c['min']<=value<=c['max']: raise ValueError('Valeur hors du domaine : '+c['label'])
            if c.get('integer'):
                if not value.is_integer(): raise ValueError('Entier attendu : '+c['label'])
                value=int(value)
        params[c['key']]=value
    return name,params
def calculate(data):
    name,params=parameters(data)
    return clean(dict(lab=name,params=params,**COMPUTE[name](params)))
