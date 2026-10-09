"""Figures scientifiques reproductibles à partir des résultats des laboratoires."""
from pathlib import Path
import json
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from catalogue import LABS
from modeles import calculate

COLORS=['#6950a4','#bc8038','#367f96','#b85b77','#7b8c38']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#302d4c','axes.titlecolor':'#302d4c','text.color':'#302d4c','svg.fonttype':'none','figure.facecolor':'#fcfaf6','axes.facecolor':'#fcfaf6'})
def plot_paths(ax,paths,common_x=None):
    for i,p in enumerate(paths):
        x=p.get('x',common_x);y=p['y']
        if x is None: continue
        step=max(1,len(x)//1600)
        ax.plot(x[::step],y[::step],color=COLORS[i%5],label=textwrap.fill(p.get('label','Courbe'),32),lw=1.7)
    ax.legend(fontsize=7,loc='best');ax.grid(alpha=.16)

def scene_figure(ax,s):
    kind=s.get('kind')
    if kind=='heatmap':
        z=np.asarray(s['z']);m=max(float(np.max(np.abs(z))),1e-12)
        im=ax.imshow(z,origin='lower',extent=[min(s['x']),max(s['x']),min(s['y']),max(s['y'])],aspect='auto',cmap='coolwarm',vmin=-m,vmax=m)
        plt.colorbar(im,ax=ax,shrink=.7,label='Résidu de l’équation')
    else:
        if kind in ('field','phase'):
            arrows=s.get('arrows',[])
            if arrows:
                a=np.array([[v['x'],v['y'],v['dx'],v['dy']] for v in arrows])
                ax.quiver(a[:,0],a[:,1],a[:,2],a[:,3],color='#b1a4c9',angles='xy',pivot='middle',width=.003)
        paths=s.get('curves',s.get('paths',[]))
        plot_paths(ax,paths,s.get('x'))
        if s.get('envelope'):
            env=s['envelope'];ax.plot(env.get('x',s.get('x')),env['y'],color=COLORS[1],ls='--',label=textwrap.fill(env.get('label','Majorante'),28));ax.legend(fontsize=7)
        if s.get('bounds'):
            b=s['bounds'];ax.set_xlim(b[:2]);ax.set_ylim(b[2:])
    ax.set_xlabel(s.get('xLabel',s.get('x_label','x')))
    ax.set_ylabel(s.get('yLabel',s.get('y_label','y')))
    ax.set_title(textwrap.fill(s.get('title','Données calculées'),44),fontsize=10,pad=13)

def chart_figure(ax,c):
    plot_paths(ax,c['series'])
    ax.set_xlabel(c['x_label']);ax.set_ylabel(c['y_label'])
    ax.set_title(textwrap.fill(c['title'],46),fontsize=10,pad=13)
    if c.get('x_scale')=='log':ax.set_xscale('log')
    if c.get('y_scale')=='log':ax.set_yscale('log')
    if 'yMin' in c:ax.set_ylim(bottom=c['yMin'])
    if 'yMax' in c:ax.set_ylim(top=c['yMax'])
    if 'xMarker' in c:ax.axvline(c['xMarker'],ls='--',color=COLORS[3],lw=1)

def export(destination, qa_directory=None):
    destination=Path(destination);destination.mkdir(exist_ok=True)
    metadata=[]
    for i,lab in enumerate(LABS,1):
        r=calculate({'lab':lab['id']})
        fig=plt.figure(figsize=(14,8.5));gs=fig.add_gridspec(2,2,width_ratios=[1.08,1],hspace=.66,wspace=.45)
        left=fig.add_subplot(gs[:,0]);scene_figure(left,r['scene'])
        for j,c in enumerate(r['charts'][:2]):chart_figure(fig.add_subplot(gs[j,1]),c)
        fig.suptitle(textwrap.fill(lab['title'],95),fontsize=17,x=.055,y=.965,ha='left',color='#302d4c')
        summary=' · '.join(m['label']+' : '+(f"{m['value']:.5g}" if isinstance(m['value'],(float,int)) else str(m['value']))+(' '+m.get('unit','')) for m in r['metrics'][:2])
        fig.text(.055,.047,textwrap.fill(summary,130),fontsize=9,color='#5c5372')
        if r['scene'].get('kind')=='phase':
            fig.text(.055,.095,textwrap.fill(r['scene']['description'],135),fontsize=8,color='#5c5372')
        fig.text(.055,.015,'Fonctions & Équations · CPGE · Paramètres initiaux ; domaines et hypothèses explicités dans le TP.',fontsize=8,color='#716582')
        fig.subplots_adjust(left=.08,right=.97,top=.855,bottom=.155)
        filename=f'{i:02d}_{lab["id"]}.svg';path=destination/filename
        fig.savefig(path,metadata={'Date':None})
        if qa_directory is not None:
            qa_path=Path(qa_directory);qa_path.mkdir(exist_ok=True)
            fig.savefig(qa_path/(lab['id']+'.png'),dpi=100)
        plt.close(fig)
        text=path.read_text(encoding='utf8');path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf8')
        metadata.append(dict(file=filename,title=lab['title'],labs=[lab['id']],caption='Paramètres initiaux du laboratoire. Intégrandes, résidus ou solutions calculés en Python ; domaines et hypothèses détaillés dans le TP.'))
    (destination/'catalogue.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    (destination/'README.md').write_text('# Figures de Fonctions & Équations\n\n28 figures SVG, issues des calculs des laboratoires. Les valeurs représentées correspondent aux paramètres initiaux. Les axes, conventions, hypothèses et contrôles sont explicités dans les TP.\n\n'+ '\n'.join(f'- [{f["title"]}]({f["file"]})' for f in metadata)+'\n',encoding='utf8')
    return f'{len(metadata)} figures scientifiques exportées.'

if __name__=='__main__':print(export(Path(__file__).parent/'illustrations'))
