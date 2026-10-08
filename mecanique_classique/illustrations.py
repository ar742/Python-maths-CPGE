"""Figures scientifiques autonomes issues des calculs des 24 laboratoires."""
from pathlib import Path
import json
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from catalogue import LABS
from modeles import calculate

COLORS=['#17675e','#bc8038','#467c9c','#aa6578','#729244']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#173944','axes.titlecolor':'#173944','text.color':'#173944','svg.fonttype':'none','figure.facecolor':'#fbfaf5','axes.facecolor':'#fbfaf5'})
def scene_figure(ax,s,lab_id,params):
    kind=s.get('kind')
    if kind in ('orbits','trajectory') and s.get('paths'):
        for j,p in enumerate(s['paths']): ax.plot(p['x'],p['y'],color=COLORS[j%5],label=textwrap.fill(p.get('label') or '_nolegend_',45))
        if lab_id in ('orbite_kepler','potentiel_effectif','transfert_hohmann','diffusion_gravitationnelle'): ax.scatter([0],[0],s=100,color=COLORS[1],marker='*',label='Centre attracteur')
        ax.set_aspect('equal',adjustable='datalim');unit={'orbite_kepler':'UA','deux_corps':'UA','coriolis':'m','fusee':'km','marees':'R','transfert_hohmann':'L₀','diffusion_gravitationnelle':'unité réduite','potentiel_effectif':'r₀','foucault':'m','konig':'m'}.get(lab_id,'m');ax.set_xlabel('x ('+unit+')');ax.set_ylabel('y ('+unit+')');ax.legend(fontsize=7)
    elif kind=='pendulum':
        theta=np.asarray(s['theta']);L=s.get('length',1)
        indices=[int(np.argmin(abs(theta-a))) for a in np.linspace(theta.min(),theta.max(),5)]
        for j,i in enumerate(indices):
            x=L*np.sin(theta[i]);y=-L*np.cos(theta[i]);ax.plot([0,x],[0,y],color=COLORS[j%5],alpha=.65);ax.scatter([x],[y],color=COLORS[j%5],s=35)
        ax.axvline(0,color='#abbcb4',lw=.8);ax.set_aspect('equal');ax.set_xlabel('x (m)');ax.set_ylabel('z (m)')
    elif kind=='chain':
        pos=np.asarray(s['positions']);eq=np.asarray(s.get('eq_positions',pos[0]))
        for j,i in enumerate(np.linspace(0,max(1,len(pos)//8),4,dtype=int)):
            ax.plot(pos[i],np.full(len(eq),j),'-o',color=COLORS[j%5],label='État '+str(j+1))
        ax.set_xlabel('Position dessinée (pm), déplacements amplifiés ×4' if lab_id=='molecule_co2' else 'Position longitudinale (m)');ax.set_yticks([]);ax.legend(fontsize=7)
    elif kind=='rod':
        theta=np.asarray(s['theta']);L=s.get('length',1)
        for j,i in enumerate(np.linspace(0,len(theta)-1,5,dtype=int)):
            ax.plot([0,L*np.sin(theta[i])],[0,L*np.cos(theta[i])],color=COLORS[j%5],lw=3)
        ax.scatter([0],[0],color=COLORS[1],s=40,label='Pivot O');ax.set_aspect('equal');ax.set_xlabel('x (m)');ax.set_ylabel('z (m)')
    elif kind=='rolling':
        R=s.get('radius',1);theta=np.asarray(s['theta']);u=np.linspace(0,2*np.pi,120)
        for j,i in enumerate(np.linspace(0,len(theta)-1,4,dtype=int)):
            x=R*np.sin(theta[i]);y=R*np.cos(theta[i]);ax.plot(x+R*np.cos(u),y+R*np.sin(u),color=COLORS[j%5]);ax.plot([0,x],[0,y],color=COLORS[j%5],lw=.8)
        ax.plot([-2*R,0],[0,0],color='#748e8b',lw=4);ax.scatter([0],[0],color=COLORS[1]);ax.set_aspect('equal');ax.set_xlabel('x (m)');ax.set_ylabel('z (m)')
    elif kind in ('inertia','rigid3d','gyroscope'):
        if kind=='inertia':
            pts=np.asarray(s.get('points',[]));ax.scatter(pts[:,0],pts[:,1],pts[:,2],s=35,color=COLORS[1]);ax.set_xlabel('x (m)');ax.set_ylabel('y (m)');ax.set_zlabel('z (m)')
            center=np.asarray(s.get('center',[0,0,0]));length=max(.5,float(np.max(np.abs(pts-center))))*.8
            limits=[pts]
            for j,v in enumerate(np.asarray(s.get('principal_axes',np.eye(3))).T):
                ends=center+np.array([-length,length])[:,None]*v;limits.append(ends)
                ax.plot(ends[:,0],ends[:,1],ends[:,2],color=COLORS[j%5],label=f'Axe principal {j+1} par G')
            u=np.asarray(s.get('axis',[0,0,1]));ends=np.array([-length,length])[:,None]*u;limits.append(ends)
            ax.plot(ends[:,0],ends[:,1],ends[:,2],color=COLORS[3],ls='--',label='Axe choisi par O')
            ax.scatter(*center,color=COLORS[0],marker='D',s=40);ax.scatter(0,0,0,color=COLORS[3],s=30)
            vertices=np.concatenate(limits);lo=vertices.min(axis=0);hi=vertices.max(axis=0);mid=(lo+hi)/2;half=max(hi-lo)*.58
            ax.set_xlim(mid[0]-half,mid[0]+half);ax.set_ylim(mid[1]-half,mid[1]+half);ax.set_zlim(mid[2]-half,mid[2]+half);ax.legend(fontsize=7,loc='upper left')
        else:
            v=np.asarray(s.get('axis',[[0,0,1]]));ax.plot(v[:,0],v[:,1],v[:,2],color=COLORS[0]);ax.quiver(0,0,0,*v[0],color=COLORS[1]);ax.set_xlabel('nₓ');ax.set_ylabel('nᵧ');ax.set_zlabel('n_z')
        ax.set_box_aspect((1,1,1))
    elif kind=='oscillator':
        x=np.asarray(s['x']);L=params.get('L0',1)*params.get('rho',1)
        xmax=max(L*1.6,float(np.max(np.abs(x)))*1.3,.2)
        ax.plot([-xmax,xmax],[0,0],color='#a0b1ab',lw=2,label='Rail horizontal')
        if lab_id in ('ressorts_transverses','oscillateur_quartique'):
            for y in (-L,L):
                a=np.array([0,y]);b=np.array([x[0],0]);v=b-a;n=np.array([-v[1],v[0]])/np.linalg.norm(v)
                f=np.linspace(0,1,31);zig=np.sin(np.arange(31)*np.pi/2)*L*.06;zig[[0,-1]]=0
                points=a+f[:,None]*v+zig[:,None]*n
                ax.plot(points[:,0],points[:,1],color=COLORS[0]);ax.scatter([0],[y],marker='s',s=35,color=COLORS[1])
            ax.annotate('Distance L',xy=(0,L),xytext=(-xmax*.8,L*.7),arrowprops={'arrowstyle':'->','color':COLORS[1]})
        else:
            ax.plot([-xmax,x[0]],[0,0],color=COLORS[0],lw=4,label='Rappel élastique')
        ax.scatter([x[0]],[0],s=180,color=COLORS[1],label='Masse au lâcher')
        ax.plot([float(np.min(x)),float(np.max(x))],[0,0],color=COLORS[3],lw=5,alpha=.35,label='Positions parcourues')
        ax.set_xlim(-xmax,xmax);ax.set_ylim(-L*1.35,L*1.35);ax.set_aspect('equal');ax.set_xlabel('x (m)' if 'L0' in params else 'Position réduite u');ax.set_ylabel('y (m)' if 'L0' in params else 'Schéma du dispositif');ax.legend(fontsize=7)
    elif kind=='friction':
        x=np.asarray(s.get('x',[0]));v=np.asarray(s.get('v',[0]));ax.plot(x,v,color=COLORS[0]);ax.set_xlabel('Position x (m)');ax.set_ylabel('Vitesse v (m/s)')
    else:
        ax.text(.5,.55,s.get('title','Modèle mécanique'),ha='center',va='center',transform=ax.transAxes,wrap=True)
    ax.set_title(textwrap.fill(s.get('title','Le modèle en images'),43),loc='left',fontsize=11,pad=12,wrap=True)
    if kind not in ('inertia','rigid3d','gyroscope'): ax.grid(alpha=.17)

def export(folder,preview=None):
    folder=Path(folder);folder.mkdir(exist_ok=True,parents=True);metadata=[]
    for i,lab in enumerate(LABS,1):
        r=calculate({'lab':lab['id']});s=r['scene'] or {};fig=plt.figure(figsize=(13.4,8.2),layout='constrained')
        grid=fig.add_gridspec(2,2,width_ratios=[1.05,1])
        a=fig.add_subplot(grid[:,0],projection='3d' if s.get('kind') in ('inertia','rigid3d','gyroscope') else None)
        scene_figure(a,s,lab['id'],r['params'])
        for j,c in enumerate(r['charts'][:2]):
            ax=fig.add_subplot(grid[j,1]);
            for k,line in enumerate(c['series']):ax.plot(line['x'],line['y'],color=COLORS[k%5],label=textwrap.fill(line['label'],48),lw=1.65)
            ax.set_xlabel(c['x_label']);ax.set_ylabel(c['y_label']);ax.set_title(textwrap.fill(c['title'],55),loc='left',fontsize=10,wrap=True);ax.grid(alpha=.2);ax.legend(fontsize=7)
            if 'yMin' in c:ax.set_ylim(bottom=c['yMin'])
            if 'yMax' in c:ax.set_ylim(top=c['yMax'])
            if 'xMarker' in c:
                ax.axvline(c['xMarker'],color=COLORS[3],ls='--',lw=1.5,label=c.get('xMarkerLabel','Seuil'))
                if lab['id']=='cylindre_bord':
                    ax.axvspan(c['xMarker'],max(max(v['x']) for v in c['series']),color=COLORS[1],alpha=.07)
                ax.legend(fontsize=7)
            if c.get('x_scale')=='log':ax.set_xscale('log')
            if c.get('y_scale')=='log':ax.set_yscale('log')
        fig.suptitle(f'{i:02d} · '+lab['title'],fontsize=15,fontweight='bold',wrap=True)
        file=f'{i:02d}_{lab["id"]}.svg';fig.savefig(folder/file,format='svg',metadata={'Date':None});
        svg=(folder/file).read_text(encoding='utf8')
        (folder/file).write_text('\n'.join(line.rstrip() for line in svg.splitlines())+'\n',encoding='utf8')
        if preview and i in (1,4,8,10,13,14,17,19,21,22,24):
            Path(preview).mkdir(exist_ok=True,parents=True);fig.savefig(Path(preview)/(file[:-4]+'.png'),dpi=115)
        plt.close(fig)
        metadata.append(dict(file=file,title=lab['title'],labs=[lab['id']],caption='Paramètres initiaux du laboratoire. Géométrie et courbes issues du calcul Python ; les hypothèses et les unités sont détaillées dans le TP.'))
    (folder/'catalogue.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf8')
    (folder/'README.md').write_text('# Figures de mécanique\n\n24 figures SVG autonomes calculées avec NumPy et Matplotlib. Chaque figure associe le mouvement ou la géométrie à deux graphiques de référence. Les paramètres initiaux sont ceux du laboratoire associé.\n\nRégénération : `python mecanique_classique.py --export-illustrations`.\n',encoding='utf8')
    return str(folder)
if __name__=='__main__':print(export(Path(__file__).parent/'illustrations'))
