"""Structures publiques de l'atelier : commandes, graphes et bilans."""
from __future__ import annotations
import math
import numpy as np

R = 8.31446261815324

def slider(key, label, lo, hi, step, value, unit='', integer=False):
    return dict(key=key, label=label, min=lo, max=hi, step=step,
                value=value, unit=unit, type='range', integer=integer)

def select(key, label, options, value):
    return dict(key=key, label=label, options=[dict(value=v, label=l) for v,l in options],
                value=value, unit='', type='select')

def preset(label, **values): return dict(label=label, values=values)
def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_, title=title, category=category, intro=intro, controls=controls, presets=presets)
def metric(label, value, unit=''): return dict(label=label, value=value, unit=unit)
def series(label, x, y): return dict(label=label, x=x, y=y)
def chart(title, x_label, y_label, *curves, **scales):
    return dict(title=title, x_label=x_label, y_label=y_label, series=list(curves), **scales)
def scene(kind, title, description, **data): return dict(kind=kind, title=title, description=description, **data)

def atom(id_, element, x, y, label=None, charge=0, **data):
    return dict(id=str(id_), element=element, label=label or element,
                x=float(x), y=float(y), charge=charge, **data)

def bond(a, b, order=1, **data):
    return dict(a=str(a), b=str(b), order=order, **data)

def electron_arrow(start, end, control=None, electrons=2, label=''):
    """Flèche d'électrons dans les coordonnées locales du graphe."""
    sx, sy = start; ex, ey = end
    return dict(start=[sx,sy], end=[ex,ey],
                control=list(control or [(sx+ex)/2, (sy+ey)/2+.65]),
                electrons=electrons, label=label)

def molecule(name, atoms, bonds, arrows=None, **data):
    return dict(name=name, atoms=atoms, bonds=bonds, arrows=arrows or [], **data)

def chain(name, labels, orders=None, **data):
    """Formule semi-développée sur un squelette zigzag ; groupes explicités."""
    def element(label):
        if label.startswith(('OH','O','COO')): return 'O' if label.startswith('O') else 'C'
        if label.startswith(('NH','N')): return 'N'
        if label.startswith('Br'): return 'Br'
        if label.startswith('Cl'): return 'Cl'
        if label in ('H','F','I','S','P','Mg','B'): return label
        return 'C'
    atoms=[atom(i,element(label),i, .2*(i%2),label=label) for i,label in enumerate(labels)]
    orders=orders or [1]*(len(labels)-1)
    return molecule(name,atoms,[bond(i,i+1,order) for i,order in enumerate(orders)], **data)

def benzene(name='Benzène', substituents=None, **data):
    atoms=[atom(i,'C',math.cos(i*math.pi/3),math.sin(i*math.pi/3),label='') for i in range(6)]
    for a in atoms: a['label']=''
    bonds=[bond(i,(i+1)%6,2 if i%2==0 else 1) for i in range(6)]
    for i,label in (substituents or {}).items():
        atoms.append(atom(f's{i}','C',1.8*math.cos(i*math.pi/3),1.8*math.sin(i*math.pi/3),label=label))
        bonds.append(bond(i,f's{i}'))
    return molecule(name,atoms,bonds,**data)

def reaction_scene(title, description, molecules, connectors=None):
    return scene('molecules',title,description,molecules=molecules,connectors=connectors or [])

def mechanism_scene(title, description, frames, index=0):
    return scene('mechanism',title,description,frames=frames,index=int(index))

def bars_scene(title, description, labels, values, unit='', colors=None, **data):
    return scene('bars',title,description,labels=labels,values=values,unit=unit,colors=colors or [],**data)

def energy_profile(levels, barriers, points=401):
    """Profil interpolé pédagogique ; niveaux et barrières fournis en kJ/mol."""
    anchors=[]
    for i,level in enumerate(levels):
        anchors.append((2*i,level))
        if i<len(barriers): anchors.append((2*i+1,barriers[i]))
    grid=np.linspace(0,anchors[-1][0],points); values=np.zeros_like(grid)
    for i in range(len(anchors)-1):
        x0,y0=anchors[i];x1,y1=anchors[i+1];mask=(grid>=x0)&(grid<=x1)
        phase=(grid[mask]-x0)/(x1-x0)
        values[mask]=y0+(y1-y0)*(1-np.cos(np.pi*phase))/2
    return grid,values

def clean(value):
    if isinstance(value,np.ndarray): return clean(value.tolist())
    if isinstance(value,np.generic): return clean(value.item())
    if isinstance(value,dict): return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [clean(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value): raise ArithmeticError('Résultat non fini.')
    if isinstance(value,complex): raise ArithmeticError('Décomposer une amplitude complexe avant export.')
    return value
