"""Contrats des expériences de mécanique : unités, tracés et scènes calculées."""
from __future__ import annotations
import math
import numpy as np

def slider(key,label,lo,hi,step,value,unit='',integer=False):
    return dict(key=key,label=label,min=lo,max=hi,step=step,value=value,unit=unit,type='range',integer=integer)
def select(key,label,options,value):
    return dict(key=key,label=label,options=[dict(value=v,label=l) for v,l in options],value=value,unit='',type='select')
def preset(label,**values): return dict(label=label,values=values)
def lab(id_,title,category,intro,controls,presets):
    return dict(id=id_,title=title,category=category,intro=intro,controls=controls,presets=presets)
def metric(label,value,unit=''): return dict(label=label,value=value,unit=unit)
def series(label,x,y): return dict(label=label,x=x,y=y)
def chart(title,x_label,y_label,*curves,**scales):
    return dict(title=title,x_label=x_label,y_label=y_label,series=list(curves),**scales)
def result(metrics,charts,scene,steps,assumptions):
    return dict(metrics=metrics,charts=charts,scene=scene,steps=steps,assumptions=assumptions)
def clean(value):
    if isinstance(value,np.ndarray): return clean(value.tolist())
    if isinstance(value,np.generic): return clean(value.item())
    if isinstance(value,dict): return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [clean(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value): raise ArithmeticError('Résultat non fini.')
    if isinstance(value,complex): raise ArithmeticError('Décomposer les valeurs complexes avant export.')
    return value
def integrate(y,x):
    return np.trapezoid(y,x) if hasattr(np,'trapezoid') else np.trapz(y,x)
