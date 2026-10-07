"""Figures scientifiques originales reproductibles ; Matplotlib est facultatif."""
from __future__ import annotations
import json
import textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from catalogue import LABS
from modeles import calculate

PALETTE=['#147c95','#df8654','#6c55a4','#55906c','#b5486b']
plt.rcParams.update({'font.size':10,'axes.titlesize':12,'axes.labelsize':10,
                    'axes.spines.top':False,'axes.spines.right':False,
                    'svg.hashsalt':'optique-cpge','figure.facecolor':'#f7f4ec',
                    'axes.facecolor':'#fffdf8','text.color':'#173f4c',
                    'axes.labelcolor':'#173f4c'})

def curves(ax,c):
    for i,s in enumerate(c['series']):
        ax.plot(s['x'],s['y'],color=PALETTE[i%5],label=s['label'],lw=1.8)
    ax.set(title='\n'.join(textwrap.wrap(c['title'],50)),xlabel=c['x_label'],ylabel=c['y_label'])
    if c.get('x_scale')=='log':ax.set_xscale('log')
    if c.get('y_scale')=='log':ax.set_yscale('log')
    ax.grid(alpha=.18)
    ax.legend(fontsize=8,loc='best')

def rays(ax,s,lab_id):
    xmin,xmax,ymin,ymax=s['bounds']
    for i,p in enumerate(s['paths']):
        xy=np.array(p['points'])
        ax.plot(xy[:,0],xy[:,1],color=p.get('color',PALETTE[i%5]),
                ls='--' if p.get('dashed') else '-',lw=1.5,alpha=p.get('opacity',1))
    for e in s.get('elements',[]):
        x,y=e.get('x',0),e.get('y',0);height=e.get('height',(ymax-ymin)*.5)
        kind=e['kind']
        if e.get('points'):
            xy=np.array(e['points']);ax.plot(xy[:,0],xy[:,1],color=PALETTE[0],lw=1.4,ls='--' if e.get('dashed') else '-')
        elif kind=='circle':ax.add_patch(Circle((x,y),e['radius'],facecolor='#147c9510',edgecolor=PALETTE[0],lw=1.4))
        elif kind=='object':
            ax.annotate('',xy=(x,y+height),xytext=(x,y),arrowprops=dict(arrowstyle='->',color=PALETTE[3],lw=2))
        elif kind=='point':
            ax.scatter([x],[y],s=22,color=PALETTE[3],zorder=6)
        elif kind in ('lens','mirror','screen','retina'):
            ax.plot([x,x],[y-height/2,y+height/2],color=PALETTE[0],lw=2.5)
        if e.get('label'):
            if kind=='point':
                ax.annotate(e['label'],(x,y),xytext=(5,7),textcoords='offset points',fontsize=8,color=PALETTE[0],clip_on=True)
            else:ax.text(x,y-height*.6,e['label'],fontsize=8,color=PALETTE[0],clip_on=True)
    for a in s.get('annotations',[]):ax.text(a['x'],a['y'],a['text'],fontsize=8,clip_on=True)
    ax.set(xlim=(xmin,xmax),ylim=(ymin,ymax),xlabel='Position longitudinale ('+s.get('unit','')+')',ylabel='Position transverse ('+s.get('unit','')+')')
    if lab_id in ('snell','arcenciel','prisme','fermat','aberrations'):ax.set_aspect('equal',adjustable='box')
    else:ax.text(.01,.98,'Axes à échelles distinctes',transform=ax.transAxes,va='top',fontsize=8,color=PALETTE[0])
    ax.grid(alpha=.13)

def physical_scene(ax,s,lab_id):
    kind=s['kind']
    ax.set_title('\n'.join(textwrap.wrap(s['title'],54)))
    if kind=='rays':rays(ax,s,lab_id)
    elif kind=='image':
        panel=(s.get('panels') or [dict(values=s['intensity'],title=s['title'])])[-1]
        data=np.array(panel.get('values',panel.get('intensity')))
        if data.ndim!=2:raise ValueError('Une image scientifique attend un tableau 2D.')
        x=panel.get('x',s.get('x',np.arange(data.shape[1])));y=panel.get('y',s.get('y',np.arange(data.shape[0])))
        im=ax.imshow(np.sqrt(np.maximum(0,data)),origin='lower',extent=[x[0],x[-1],y[0],y[-1]],cmap='magma',aspect='equal')
        ax.set(xlabel=panel.get('x_label',s.get('x_label','x')),ylabel=panel.get('y_label',s.get('y_label','y')))
        plt.colorbar(im,ax=ax,fraction=.046,pad=.03,label='√I (unités du modèle)')
    elif kind=='fringes':
        x=np.array(s.get('x_mm',s.get('x')));intensity=np.array(s['intensity'])
        ax.imshow(np.sqrt(np.maximum(0,intensity))[None,:],aspect='auto',origin='lower',extent=[x[0],x[-1],0,1],cmap='inferno')
        ax.set(xlabel='Position sur l’écran (mm)',yticks=[])
        ax.text(.02,.95,'Affichage √I',transform=ax.transAxes,color='white',va='top',fontsize=9)
    elif kind=='polarisation':
        ax.plot(s['ellipse_x'],s['ellipse_y'],color=PALETTE[1],lw=2.5)
        ax.axhline(0,color='#829795',lw=.6);ax.axvline(0,color='#829795',lw=.6)
        ax.set(xlabel='Eₓ / amplitude incidente',ylabel='Eᵧ / amplitude incidente',aspect='equal')
        ax.grid(alpha=.18)
    elif kind=='beam':
        z=np.array(s['z_mm']);w=np.array(s['w_mm'])
        ax.fill_between(z,-w,w,color=PALETTE[1],alpha=.18);ax.plot(z,w,color=PALETTE[1]);ax.plot(z,-w,color=PALETTE[1])
        ax.axhline(0,color='#829795',ls='--',lw=.6);ax.set(xlabel='z (mm)',ylabel='Rayon à 1/e² de l’intensité (mm)')
        ax.grid(alpha=.18)
    elif kind=='nonlinear':
        for key,title,color in [('pump1','Pompe 1, ω',PALETTE[1]),('pump2','Pompe 2, ω',PALETTE[2]),('harmonic','Harmonique, 2ω',PALETTE[0])]:
            ax.plot(s['z_mm'],s[key],label=title,color=color)
        ax.set(xlabel='z (mm)',ylabel='Intensité (unités du modèle)');ax.legend(fontsize=8);ax.grid(alpha=.18)
    elif kind=='cavity':
        ax.set(xlim=(-.2,1.4),ylim=(-.5,.6),aspect='equal',xticks=[],yticks=[])
        for x in (0,1):ax.plot([x,x],[-.3,.3],color=PALETTE[0],lw=4)
        for i in range(5):ax.plot([i%2,1-i%2],[-.22+i*.09,-.13+i*.09],color=PALETTE[1],alpha=.85-i*.12)
        ax.arrow(-.2,0,.18,0,width=.004,color=PALETTE[1],length_includes_head=True)
        ax.arrow(1.02,0,.28,0,width=.004,color=PALETTE[1],length_includes_head=True)
        ax.text(.5,.38,'Trajets multiples · schéma',ha='center',fontsize=10)
        ax.text(0,-.44,'M₁');ax.text(1,-.44,'M₂')
        for spine in ax.spines.values():spine.set_visible(False)
    else:raise ValueError('Scène scientifique inconnue : '+kind)

def export(destination):
    destination=Path(destination);destination.mkdir(exist_ok=True,parents=True)
    figures=[]
    for lab in LABS:
        r=calculate(dict(lab=lab['id']));s=r['scene']
        fig,axes=plt.subplots(1,2,figsize=(12.5,5.5),gridspec_kw={'width_ratios':[1.1,1]})
        physical_scene(axes[0],s,lab['id']);curves(axes[1],r['charts'][0])
        fig.suptitle(lab['title'],fontsize=16,y=.98)
        caption=s['description']
        fig.text(.045,.035,'\n'.join(textwrap.wrap(caption,170)),fontsize=9,color='#526f73',va='bottom')
        fig.tight_layout(rect=[0,.15,1,.92])
        fig.savefig(destination/(lab['id']+'.svg'),metadata={'Date':None,'Creator':'Python-maths-CPGE · Optique','Description':caption})
        plt.close(fig)
        figures.append(dict(file=lab['id']+'.svg',title=lab['title'],labs=[lab['id']],caption=caption))
    (destination/'catalogue.json').write_text(json.dumps(figures,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    return f'{len(figures)} figures enregistrées dans {destination}'

if __name__=='__main__':print(export(Path(__file__).parent/'illustrations'))
