"""Validation des commandes, puis calcul des trois volets de mécanique."""
import math
from catalogue import LAB_BY_ID
from commun import clean
from modeles_p1 import COMPUTE as P1
from modeles_p2 import COMPUTE as P2
from modeles_p3 import COMPUTE as P3
COMPUTE={**P1,**P2,**P3}
def parameters(data):
    if not isinstance(data,dict): raise ValueError('Objet JSON attendu.')
    lab=data.get('lab')
    if not isinstance(lab,str) or lab not in LAB_BY_ID: raise ValueError('Laboratoire inconnu.')
    supplied=data.get('params',{k:v for k,v in data.items() if k!='lab'})
    if not isinstance(supplied,dict): raise ValueError('Paramètres invalides.')
    controls=LAB_BY_ID[lab]['controls']
    if set(supplied)-{c['key'] for c in controls}: raise ValueError('Paramètre inconnu pour ce laboratoire.')
    params={}
    for c in controls:
        v=supplied.get(c['key'],c['value'])
        if c['type']=='select':
            if not isinstance(v,str) or v not in {o['value'] for o in c['options']}: raise ValueError('Choix invalide : '+c['label'])
        else:
            if isinstance(v,bool) or not isinstance(v,(int,float)): raise ValueError('Nombre attendu : '+c['label'])
            try: v=float(v)
            except OverflowError as exc: raise ValueError('Nombre trop grand.') from exc
            if not math.isfinite(v) or not c['min']<=v<=c['max']: raise ValueError('Valeur hors du domaine : '+c['label'])
            if c.get('integer'):
                if not v.is_integer(): raise ValueError('Entier attendu : '+c['label'])
                v=int(v)
        params[c['key']]=v
    return lab,params
def calculate(data):
    lab,params=parameters(data)
    return clean(dict(lab=lab,params=params,**COMPUTE[lab](params)))
