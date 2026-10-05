"""Figures scientifiques autonomes : Matplotlib facultatif pour l'application."""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'python-maths-cpge-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from modeles import calculate

PALETTE={'green':'#23745c','gold':'#c79432','rose':'#b66375','mint':'#8dc9ac','ink':'#17363d'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'text.color':PALETTE['ink'],'axes.labelcolor':PALETTE['ink'],'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','svg.hashsalt':'python-maths-cpge-quantique'})
CONFIGS=[('boite','TP · Confinement dans un cube et superposition',dict(mix=.5,time=.4)),
         ('heisenberg','TP · Heisenberg, étalement et corrélations',dict(time=3)),
         ('diffusion','Marche et barrière · Réflexion et effet tunnel',{}),
         ('oscillateur','Oscillateur · Fonctions propres et niveaux quantifiés',dict(n=3)),
         ('intrication','Intrication · Probabilités et corrélations de Bell',dict(a=22.5)),
         ('josephson','SQUID · Interférence de deux jonctions',dict(I2=5)),
         ('rabi','RMN · Oscillations de Rabi et repère tournant',dict(detuning=.8)),
         ('bloch','Qubit · Sphère de Bloch, rotations et mesure',dict(gate='Ry',angle=90)),
         ('circuits','Informatique quantique · Grover sur quatre états',dict(mode='grover',iterations=1))]


def export(folder=None,preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name('illustrations')
    folder.mkdir(parents=True,exist_ok=True)
    if preview:preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    files=[]
    for lab,title,params in CONFIGS:
        result=calculate(dict(lab=lab,**params))
        fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
        fig.suptitle(title,fontweight='bold',fontsize=16)
        for ax,data in zip(axes,result['charts']):
            if 'grid' in data:
                from matplotlib.colors import LinearSegmentedColormap
                g=data['grid'];cmap=LinearSegmentedColormap.from_list('presence',['#f8f6ef',PALETTE['green']])
                im=ax.pcolormesh(g['x'],g['y'],g['z'],shading='nearest',cmap=cmap)
                fig.colorbar(im,ax=ax,label='Densité marginale × L²')
            seen=set()
            for s in data['series']:
                label=s['label'] if s['label'] not in seen else '_nolegend_';seen.add(s['label']);color=PALETTE[s['color']]
                if s['kind']=='dots':ax.scatter(s['x'],s['y'],s=24,color=color,label=label,zorder=5)
                elif s['kind']=='bars':ax.bar(s['x'],s['y'],width=.5,color=color,label=label)
                elif s['kind']=='stems':
                    ax.vlines(s['x'],0,s['y'],color=color,lw=1.5,label=label);ax.scatter(s['x'],s['y'],s=18,color=color)
                elif s['kind']=='step':ax.step(s['x'],s['y'],where='post',color=color,label=label)
                else:ax.plot(s['x'],s['y'],color=color,lw=1 if s['color']=='mint' else 1.8,label=label)
            ax.set(title=data['title'],xlabel=data['xlabel'],ylabel=data['ylabel'])
            if data['logx']:ax.set_xscale('log')
            if data['logy']:ax.set_yscale('log')
            if data['equal']:ax.set_aspect('equal',adjustable='datalim')
            ax.grid(alpha=.18)
            if data['series']:ax.legend(fontsize=8,loc='best')
        path=folder/(lab+'.svg');fig.savefig(path,metadata={'Date':None,'Creator':'Python-maths-CPGE · Physique quantique'})
        text=path.read_text(encoding='utf-8')
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8',newline='\n')
        if preview:fig.savefig(preview/(lab+'.png'),dpi=125)
        plt.close(fig);files.append(path.name)
    return files


if __name__=='__main__':print(export())
