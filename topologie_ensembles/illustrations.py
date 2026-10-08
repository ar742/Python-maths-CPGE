"""Galerie de figures autonomes : données calculées, objets et hypothèses."""
from __future__ import annotations
import json
from pathlib import Path
import textwrap
import numpy as np
from catalogue import LABS
from modeles import calculate

PALETTE=['#217865','#c87540','#8075bb','#aa892c','#b15268']

def geometry(ax,sc):
    from matplotlib.patches import Circle,PathPatch
    from matplotlib.path import Path as MPath
    for p in sc.get('paths',[]):
        pts=np.asarray(p['points']);color=PALETTE[p.get('colorIndex',0)%5]
        if len(pts)==0:continue
        if p.get('fill'):
            vertices=np.vstack((pts,pts[:1]));codes=[MPath.MOVETO]+[MPath.LINETO]*(len(pts)-1)+[MPath.CLOSEPOLY]
            ax.add_patch(PathPatch(MPath(vertices,codes),facecolor=color,alpha=.15,edgecolor='none'))
        plot=np.vstack((pts,pts[:1])) if p.get('closed') else pts
        ax.plot(plot[:,0],plot[:,1],color=color,lw=1.6,ls='--' if p.get('dashed') or p.get('boundaryClosed') is False else '-',label=p.get('label',''))
    points=sc.get('points',[])
    for pt in points:
        color=PALETTE[pt.get('colorIndex',0)%5];excluded='exclu' in pt.get('label','')
        ax.scatter([pt['x']],[pt['y']],s=9 if len(points)>30 else 27,facecolors='none' if excluded else color,edgecolors=color,zorder=5)
        if len(points)<=6:
            ax.annotate(pt.get('label',''),(pt['x'],pt['y']),xytext=(5,7),textcoords='offset points',fontsize=7,color=color)
    for d in sc.get('discs',[]):
        color=PALETTE[d.get('colorIndex',0)%5]
        ax.add_patch(Circle((d['x'],d['y']),max(.005,d['r']),edgecolor=color,facecolor=color if d.get('fill') else 'white' if d['r']<.035 else 'none',alpha=.17 if d.get('fill') else 1,lw=1.3,ls='--' if d.get('closed') is False else '-',zorder=6 if not d.get('fill') else 2,label=d.get('label','')))
    bounds=sc.get('bounds')
    if bounds:ax.set_xlim(bounds[:2]);ax.set_ylim(bounds[2:])
    temporal=any(key in sc for key in ('subsequences','record_indices','fraction_labels'))
    ax.set_aspect('auto' if temporal else 'equal',adjustable='box');ax.axhline(0,color='#b8c9c5',lw=.7);ax.axvline(0,color='#b8c9c5',lw=.7)

def special(ax,sc):
    kind=sc['kind']
    if kind=='diagonal':
        a=np.vstack((sc['matrix'],sc['anti']));ax.imshow(a,cmap='YlGnBu',vmin=0,vmax=1,aspect='auto')
        for i,row in enumerate(a):
            for j,value in enumerate(row):ax.text(j,i,str(value),ha='center',va='center',fontsize=8,color='white' if value else '#1d3d4c')
        for i in range(len(sc['matrix'])):ax.add_patch(__import__('matplotlib').patches.Rectangle((i-.48,i-.48),.96,.96,fill=False,lw=1.8,edgecolor='#e79649'))
        ax.set_yticks(range(len(a)),[str(i+1) for i in range(len(a)-1)]+['a']);ax.set_xticks(range(len(sc['anti'])),range(1,len(sc['anti'])+1))
    elif kind=='cantor':
        for k,intervals in enumerate(sc['levels']):
            for a,b in intervals:ax.plot([a,b],[-k,-k],color=PALETTE[k%3],lw=5,solid_capstyle='butt')
        ax.set_yticks(-np.arange(len(sc['levels'])),[f'K{k}' for k in range(len(sc['levels']))]);ax.set_xlim(-.02,1.02);ax.set_ylim(-len(sc['levels'])+.4,.5)
    elif kind=='matrix':
        a=np.asarray(sc['matrix']);v=max(1,float(np.max(abs(a))));im=ax.imshow(a,cmap='BrBG',vmin=-v,vmax=v)
        if a.shape[0]<=8:
            for i in range(len(a)):
                for j in range(len(a[0])):ax.text(j,i,'0' if abs(a[i,j])<1e-12 else f'{a[i,j]:.3g}',ha='center',va='center',fontsize=8,color='#162f43' if abs(a[i,j])<.65*v else 'white')
        labels=sc.get('labels',[str(i+1) for i in range(len(a))]);ax.set_xticks(range(len(labels)),labels);ax.set_yticks(range(len(labels)),labels)
    else:geometry(ax,sc)

def export(destination,png_destination=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    if png_destination:Path(png_destination).mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
    catalogue=[]
    for lab in LABS:
        r=calculate({'lab':lab['id']});sc=r['scene'];charts=list(r['charts']);has_scene=sc['kind'] in ('diagonal','cantor','matrix') or bool(sc.get('bounds') and any(sc.get(k) for k in ('paths','points','discs')))
        if has_scene:charts.insert(0,dict(title=sc['title'],x_label=sc.get('x_label','x'),y_label=sc.get('y_label','y'),series=[],special=True))
        count=len(charts);rows=(count+1)//2
        fig,axes=plt.subplots(rows,2,figsize=(11.5,3.6*rows+1.6),squeeze=False)
        fig.patch.set_facecolor('#f8f7f1');fig.suptitle('\n'.join(textwrap.wrap(lab['title'],74)),fontsize=16,color='#162f43',x=.055,ha='left',y=.97)
        for ax,ch in zip(axes.flat,charts):
            ax.set_facecolor('white');seen=set()
            if ch.get('special'):special(ax,sc)
            for k,curve in enumerate(ch['series']):
                color=PALETTE[k%5];label=curve['label'] if curve['label'] not in seen else '_nolegend_';seen.add(curve['label'])
                if curve.get('style')=='dots':ax.scatter(curve['x'],curve['y'],s=13,color=color,label=label,zorder=4)
                elif curve.get('style')=='stems':ax.vlines(curve['x'],0,curve['y'],color=color,lw=1.5,label=label)
                else:ax.plot(curve['x'],curve['y'],lw=1.6,color=color,label=label)
            if ch.get('x_scale')=='log':ax.set_xscale('log')
            if ch.get('y_scale')=='log':ax.set_yscale('log')
            if ch.get('x_reverse'):ax.invert_xaxis()
            ax.set_title('\n'.join(textwrap.wrap(ch['title'],47)),fontsize=10,loc='left',pad=11,color='#162f43')
            if not ch.get('special') or sc['kind'] not in ('matrix','diagonal','cantor'):
                ax.set_xlabel(ch['x_label'],fontsize=8);ax.set_ylabel(ch['y_label'],fontsize=8);ax.grid(alpha=.16)
            handles,labels=ax.get_legend_handles_labels()
            if handles:
                unique=dict(zip(labels,handles));ax.legend(unique.values(),unique.keys(),loc='best',fontsize=6.5,framealpha=.9)
        for ax in list(axes.flat)[count:]:ax.axis('off')
        parameters=' · '.join(f'{k}={v:g}' if isinstance(v,(int,float)) else f'{k}={v}' for k,v in r['params'].items());caption='Paramètres : '+parameters+'. '+r['assumptions'][0]
        fig.text(.055,.025,'\n'.join(textwrap.wrap(caption,145)),fontsize=7.7,color='#56707c',va='bottom')
        fig.subplots_adjust(left=.075,right=.97,top=.79 if rows==1 else .87,bottom=.22 if rows==1 else .15,hspace=.72,wspace=.31)
        filename=lab['id']+'.svg';target=destination/filename;fig.savefig(target,facecolor=fig.get_facecolor())
        target.write_text('\n'.join(line.rstrip() for line in target.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
        if png_destination:fig.savefig(Path(png_destination)/(lab['id']+'.png'),dpi=110,facecolor=fig.get_facecolor())
        plt.close(fig);catalogue.append(dict(file=filename,title=lab['title'],labs=[lab['id']],caption=caption))
    (destination/'catalogue.json').write_text(json.dumps(catalogue,ensure_ascii=False,indent=2),encoding='utf8')
    text='# Galerie scientifique · Topologie & Ensembles\n\nTrente figures originales, calculées avec les modèles. Les critères topologiques exacts sont expliqués dans chaque TP ; le dessin est une représentation finie.\n\n'
    text+='\n\n'.join(f"## {i+1}. {f['title']}\n\n![{f['title']}]({f['file']})\n\n{f['caption']}" for i,f in enumerate(catalogue))+'\n'
    (destination/'README.md').write_text(text,encoding='utf8');return f'{len(catalogue)} figures SVG créées.'

if __name__=='__main__':print(export(Path(__file__).with_name('illustrations')))
