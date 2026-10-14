"""Figures scientifiques autonomes issues des calculs des 24 laboratoires."""
from pathlib import Path
import json
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon
from matplotlib.colors import ListedColormap,SymLogNorm
from catalogue import LABS
from modeles import calculate
COLORS=['#8663a4','#1e9192','#b78639','#b85c4c','#647e4d','#8192a6']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'svg.fonttype':'none','figure.facecolor':'#fbfaf7','axes.facecolor':'#fbfaf7','axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.16,'axes.labelcolor':'#303c55','text.color':'#303c55','axes.titlecolor':'#303c55'})

def paths(ax,curves):
    for i,p in enumerate(curves):
        if not p.get('x'): continue
        ax.plot(p['x'],np.asarray(p['y'],dtype=float),color=COLORS[i%6],lw=1.5,label=textwrap.fill(p.get('label','Courbe'),27))

def scene(ax,s):
    curves=s.get('curves',s.get('paths',[]))
    if s['kind']=='field':
        z=np.asarray(s['z']); x=np.asarray(s['x']); y=np.asarray(s['y'])
        if s.get('categorical'):
            img=ax.pcolormesh(x,y,z,shading='nearest',cmap=ListedColormap(COLORS),vmin=-.5,vmax=5.5,rasterized=True)
            labels=s.get('labels',[])
            cb=ax.figure.colorbar(img,ax=ax,shrink=.57,pad=.025,ticks=range(len(labels)))
            cb.ax.set_yticklabels([textwrap.fill(t,16) for t in labels],fontsize=7)
        else:
            maximum=max(1e-12,np.max(abs(z)))
            if np.min(z)>=0:
                img=ax.pcolormesh(x,y,z,shading='nearest',cmap='viridis',vmin=np.min(z),vmax=np.max(z),rasterized=True)
            else:
                img=ax.pcolormesh(x,y,z,shading='nearest',cmap='PuOr_r',norm=SymLogNorm(linthresh=maximum/12,vmin=-maximum,vmax=maximum),rasterized=True)
            cb=ax.figure.colorbar(img,ax=ax,shrink=.62,pad=.03)
            cb.set_label(s.get('valueLabel','Valeur calculée'),fontsize=8)
            levels=[v for v in s.get('levels',[0]) if np.min(z)<v<np.max(z)]
            if levels: ax.contour(x,y,z,levels=levels,colors=COLORS[2],linewidths=1.5)
        paths(ax,s.get('paths',[]));ax.set_aspect('equal' if s.get('equalAspect') else 'auto',adjustable='box')
    elif s['kind']=='plane':
        paths(ax,s.get('paths',[]))
        for i,c in enumerate(s.get('circles',[])):
            ax.add_patch(Circle((c['x'],c['y']),c['r'],fill=False,ls='--',lw=1.2,color=COLORS[(i+1)%6],label=textwrap.fill(c.get('label','Cercle'),27)))
        for p in s.get('polygons',[]):
            if len(p['x'])>=3: ax.add_patch(Polygon(np.column_stack((p['x'],p['y'])),facecolor='#1e919215',edgecolor=COLORS[1],ls='--',label=p.get('label','Enveloppe convexe')))
        if s.get('bounds'):
            x0,x1,y0,y1=s['bounds']
            if x0==x1:x0-=1;x1+=1
            if y0==y1:y0-=1;y1+=1
            ax.set_xlim(x0,x1);ax.set_ylim(y0,y1)
        ax.set_aspect('equal' if s.get('equalAspect') else 'auto',adjustable='box');ax.axhline(0,color='#9ba7b4',lw=.6);ax.axvline(0,color='#9ba7b4',lw=.6)
    else:
        paths(ax,curves)
    points=s.get('points',[])
    for i,p in enumerate(points):
        color=COLORS[p.get('group',0)%6]
        ax.scatter(p['x'],p['y'],s=30,facecolors='none' if p.get('hollow') else color,edgecolors=color,zorder=5)
        if len(points)<=6 and p.get('label'): ax.annotate(p['label'] if len(p['label'])<13 else f'P{i+1}',(p['x'],p['y']),xytext=(5,6),textcoords='offset points',fontsize=8,color=color)
    handles,labels=ax.get_legend_handles_labels()
    if handles:ax.legend(fontsize=7,loc='best')
    ax.set_title(textwrap.fill(s['title'],42),fontsize=11,pad=14)
    ax.set_xlabel(s.get('xLabel','x'));ax.set_ylabel(s.get('yLabel','y'))

def plot_chart(ax,c):
    if c.get('style')=='bars':
        for i,p in enumerate(c['series']):
            ax.vlines(p['x'],0,p['y'],color=COLORS[i%6],label=textwrap.fill(p['label'],28),lw=1.8)
            ax.scatter(p['x'],p['y'],color=COLORS[i%6],s=12)
        ax.axhline(0,color='#8998aa',lw=.6)
    else: paths(ax,c['series'])
    if c.get('x_scale')=='log':ax.set_xscale('log')
    if c.get('y_scale')=='log':ax.set_yscale('log')
    ax.set_title(textwrap.fill(c['title'],43),fontsize=10,pad=13)
    ax.set_xlabel(c['x_label']);ax.set_ylabel(c['y_label'])
    ax.legend(fontsize=7,loc='best')

def export(destination,qa_directory=None):
    out=Path(destination);out.mkdir(exist_ok=True)
    metadata=[]
    for i,l in enumerate(LABS,1):
        r=calculate({'lab':l['id']})
        fig=plt.figure(figsize=(14,9)); gs=fig.add_gridspec(2,2,width_ratios=[1.05,1],hspace=.7,wspace=.47)
        scene(fig.add_subplot(gs[:,0]),r['scene'])
        for j,c in enumerate(r['charts'][:2]):plot_chart(fig.add_subplot(gs[j,1]),c)
        if len(r['charts'])==1:
            ax=fig.add_subplot(gs[1,1]);ax.axis('off')
            ax.text(0,1,'À justifier',fontsize=12,va='top',weight='bold')
            message='\n\n'.join(textwrap.fill(t,58) for t in r['steps'][:3])
            ax.text(0,.82,message,fontsize=9,va='top',linespacing=1.35)
        fig.suptitle(textwrap.fill(l['title'],90),fontsize=17,x=.06,y=.97,ha='left')
        summary=' · '.join(m['label']+' : '+(f"{m['value']:.5g}" if isinstance(m['value'],(float,int)) else str(m['value'])) for m in r['metrics'][:2])
        fig.text(.06,.062,textwrap.fill(summary,130),fontsize=9,color='#5c6074')
        fig.text(.06,.024,'Chimie pour l’industrie · CPGE · Paramètres initiaux ; définitions, hypothèses et preuves dans le TP.',fontsize=8,color='#737a88')
        fig.subplots_adjust(left=.08,right=.97,top=.86,bottom=.19)
        name=f'{i:02d}_{l["id"]}.svg'; fig.savefig(out/name,metadata={'Date':None})
        if qa_directory:
            qa=Path(qa_directory);qa.mkdir(exist_ok=True);fig.savefig(qa/(l['id']+'.png'),dpi=100)
        plt.close(fig)
        text=(out/name).read_text(encoding='utf8');(out/name).write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf8')
        metadata.append(dict(file=name,title=l['title'],labs=[l['id']],caption='Figure calculée aux paramètres initiaux. Les identités exactes et les observations numériques sont distinguées dans le TP.'))
    (out/'catalogue.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    (out/'README.md').write_text('# Figures de Chimie pour l’industrie\n\n24 figures SVG issues des modèles des laboratoires : bilans énergétiques, réacteurs, surfaces catalytiques, grains poreux, cellules électrochimiques et diagrammes de phases. Les paramètres sont ceux des exemples initiaux ; le TP donne les définitions et les preuves.\n\n'+'\n'.join(f'- [{m["title"]}]({m["file"]})' for m in metadata)+'\n',encoding='utf8')
    return f'{len(metadata)} figures scientifiques exportées.'
if __name__=='__main__':print(export(Path(__file__).parent/'illustrations'))
