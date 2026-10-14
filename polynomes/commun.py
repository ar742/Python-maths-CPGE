"""Contrôles, calculs exacts et données des illustrations de Polynômes."""
from __future__ import annotations
import math
import numpy as np
import sympy as sp

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
def table(title,headers,rows): return dict(title=title,headers=headers,rows=rows)
def result(metrics,charts,scene,steps,assumptions,table=None):
    data=dict(metrics=metrics,charts=charts,scene=scene,steps=steps,assumptions=assumptions)
    if table is not None: data['table']=table
    return data
def curve_scene(title,x,curves,xlabel,ylabel,description='',apparatus=None):
    return dict(kind='curves',title=title,x=x,curves=[dict(label=l,x=x,y=y) for l,y in curves],xLabel=xlabel,yLabel=ylabel,description=description,apparatus=apparatus or {})
def plane_scene(title,points=None,paths=None,circles=None,polygons=None,bounds=None,xlabel='Re(z)',ylabel='Im(z)',description=''):
    return dict(kind='plane',title=title,points=points or [],paths=paths or [],circles=circles or [],polygons=polygons or [],bounds=bounds,xLabel=xlabel,yLabel=ylabel,description=description)
def field_scene(title,x,y,z,description='',points=None,paths=None,levels=None,categorical=False,labels=None):
    return dict(kind='field',title=title,x=x,y=y,z=z,xLabel='x',yLabel='y',description=description,points=points or [],paths=paths or [],levels=levels if levels is not None else [0],categorical=categorical,labels=labels or [])
def exact(value): return sp.Rational(str(value))
def formula(value): return sp.sstr(value).replace('**','^')
def point(z,label='',group=0):
    z=complex(z)
    return dict(x=float(z.real),y=float(z.imag),label=label,group=group)
def clean(value):
    if isinstance(value,np.ndarray): return clean(value.tolist())
    if isinstance(value,np.generic): return clean(value.item())
    if isinstance(value,dict): return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [clean(v) for v in value]
    if isinstance(value,sp.Basic):
        if value.is_Integer: return int(value)
        if value.is_real and value.is_number: return clean(float(value))
        return formula(value)
    if isinstance(value,float) and not math.isfinite(value): raise ArithmeticError('Résultat non fini.')
    if isinstance(value,complex): raise ArithmeticError('Décomposer les valeurs complexes avant export.')
    return value
def integrate(y,x):
    return np.trapezoid(y,x) if hasattr(np,'trapezoid') else np.trapz(y,x)
