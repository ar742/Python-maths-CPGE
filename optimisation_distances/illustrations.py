"""Figures scientifiques SVG autonomes ; Matplotlib requis pour régénérer."""
from pathlib import Path
import os
import tempfile
import numpy as np
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'python-maths-cpge-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mathematiques import approximation, produit, point_ellipsoide, distance_ellipsoides

INK, GREEN, GOLD, ROSE = '#17363d', '#23745c', '#c79432', '#b66375'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,
                    'axes.spines.right':False,'axes.labelcolor':INK,'text.color':INK,
                    'axes.titleweight':'bold','axes.edgecolor':'#b9c6bc','grid.color':'#dce3db',
                    'svg.fonttype':'none','svg.hashsalt':'python-maths-cpge',
                    'savefig.facecolor':'#f8f6ef','figure.facecolor':'#f8f6ef'})


def surface(ax,c,B,color):
    lon,lat=np.meshgrid(np.linspace(0,2*np.pi,49),np.linspace(-np.pi/2,np.pi/2,25))
    u=np.array([np.cos(lat)*np.cos(lon),np.cos(lat)*np.sin(lon),np.sin(lat)])
    xyz=np.einsum('ij,jkl->ikl',B,u)+np.array(c)[:,None,None]
    ax.plot_wireframe(*xyz,rstride=3,cstride=4,color=color,alpha=.42,linewidth=.6)


def axes3d(ax,limits):
    ax.set(xlabel='x',ylabel='y',zlabel='z',xlim=limits[0],ylim=limits[1],zlim=limits[2])
    spans=[b-a for a,b in limits];ax.set_box_aspect(spans);ax.view_init(22,-55)
    ax.xaxis.pane.fill=ax.yaxis.pane.fill=ax.zaxis.pane.fill=False


def export(directory, preview=None):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    if preview:Path(preview).mkdir(parents=True,exist_ok=True)
    files=[]
    def save(fig,name):
        fig.savefig(directory/f'{name}.svg',bbox_inches='tight',metadata={'Creator':'Python-maths-CPGE · A. R.', 'Date':None})
        svg = directory/f'{name}.svg'
        svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',
                       encoding='utf-8', newline='\n')
        if preview:fig.savefig(Path(preview)/f'{name}.png',dpi=130,bbox_inches='tight')
        files.append(name+'.svg');plt.close(fig)
    d=approximation({});x=np.array(d['x'])
    fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
    fig.suptitle('Approcher cosinus : deux normes, deux meilleures droites',fontsize=17)
    for vals,col,label in [(d['cos'],INK,'cos t'),(d['projection'],GREEN,'Projection L²'),(d['uniforme'],GOLD,'Meilleure droite uniforme')]:
        axs[0].plot(x,vals,color=col,label=label,lw=2)
    axs[0].set(xlabel='t',ylabel='Valeur',title='Sur [0, π/2]');axs[0].grid(alpha=.6);axs[0].legend(fontsize=9)
    axs[1].plot(x,np.array(d['cos'])-d['projection'],color=GREEN,label='Résidu L²',lw=2)
    axs[1].plot(x,np.array(d['cos'])-d['uniforme'],color=GOLD,label='Résidu uniforme',lw=2)
    axs[1].axhline(0,color=INK,lw=.8)
    mm=d['minimax'];axs[1].scatter([0,mm['contact'],np.pi/2],[-mm['erreur'],mm['erreur'],-mm['erreur']],color=GOLD,zorder=4)
    axs[1].set(xlabel='t',ylabel='cos t − droite',title='Alternance : −E, +E, −E');axs[1].grid(alpha=.6);axs[1].legend(fontsize=9)
    save(fig,'cosinus_deux_normes')
    fig,ax=plt.subplots(figsize=(10,5.2),layout='constrained');theta=np.linspace(-180,180,721)
    ax.plot(theta,np.sqrt(2)*abs(np.sin(np.radians(theta))),color=GREEN,lw=2)
    ax.scatter([-90,0,90],[np.sqrt(2),0,np.sqrt(2)],color=ROSE,zorder=4)
    ax.set(title='Exercice 4 · Distance de la rotation aux matrices symétriques',xlabel='Angle θ (degrés)',ylabel='Distance de Frobenius',xticks=np.arange(-180,181,45))
    ax.text(.18,.12,'d(Rθ, S₃) = √2 |sin θ|',transform=ax.transAxes,fontsize=16,color=GREEN);ax.grid(alpha=.6)
    save(fig,'rotation_projection')
    d=produit({'axes':[3,2,1]});fig=plt.figure(figsize=(10,6),layout='constrained');ax=fig.add_subplot(projection='3d')
    surface(ax,[0,0,0],np.diag(d['axes']),INK);p=np.array(d['maximiseurs']);ax.scatter(*p.T,color=GREEN,s=25,depthshade=False)
    for i,a in enumerate(p):
        for j,b in enumerate(p):
            if i<j and np.count_nonzero(a!=b)==1:ax.plot(*np.array([a,b]).T,color=GOLD,lw=1.8)
    axes3d(ax,[(-3.2,3.2),(-2.2,2.2),(-1.2,1.2)])
    ax.set_title('Exercice 6 · La boîte de volume maximal dans un ellipsoïde',pad=20)
    fig.text(.025,.045,'Demi-axes : 3, 2, 1   •   Demi-côtés : aᵢ/√3   •   Volume maximal : 16/√3',fontsize=11)
    save(fig,'ellipsoide_boite')
    d=point_ellipsoide({'centre':[.4,-.2,.1],'axes':[2,1.2,.8],'angles':[15,25,35],'point':[3,2,1]})
    fig=plt.figure(figsize=(10,6),layout='constrained');ax=fig.add_subplot(projection='3d');surface(ax,d['centre'],d['B'],INK)
    for label,color in [('minimum',GREEN),('maximum',GOLD)]:
        pts=np.array([d['point'],d[label]['point']]);ax.plot(*pts.T,color=color,lw=2.5,label=f"{label.capitalize()} : {d[label]['distance']:.4f}")
        ax.scatter(*pts[-1],color=color,s=30)
    ax.scatter(*d['point'],color=ROSE,s=45);ax.text(*d['point'],' p',color=ROSE)
    axes3d(ax,[(-2.5,3.5),(-2.4,2.4),(-1.8,1.8)]);ax.legend(loc='upper left',fontsize=10)
    ax.set_title('Distance d’un point à une surface ellipsoïdale orientée',pad=20)
    save(fig,'point_ellipsoide')
    e1={'centre':[-2.4,-.6,0],'axes':[1.8,1,.7],'angles':[10,20,25]}
    e2={'centre':[2.4,.8,.5],'axes':[1.4,.9,.6],'angles':[-20,35,-35]}
    d=distance_ellipsoides(e1,e2)
    fig=plt.figure(figsize=(12,6),layout='constrained');ax=fig.add_subplot(121,projection='3d');right=fig.add_subplot(122)
    surface(ax,d['e1']['centre'],d['e1']['B'],GREEN);surface(ax,d['e2']['centre'],d['e2']['B'],INK)
    pts=np.array([d['p1'],d['p2']]);ax.plot(*pts.T,color=GOLD,lw=3);ax.scatter(*pts.T,color=GOLD,s=30)
    axes3d(ax,[(-4.5,4.5),(-2.2,2.4),(-1.2,2)]);ax.set_title('Centres et axes distincts',pad=18)
    hist=np.array(d['historique']);right.plot(hist[:,0],hist[:,2],color=GOLD,marker='o',label='Borne supérieure U')
    right.plot(hist[:,0],hist[:,1],color=GREEN,marker='o',label='Borne inférieure L');right.legend(fontsize=9);right.grid(alpha=.6)
    right.set(xlabel='Itération',ylabel='Distance',title='Un contrôle global de l’optimisation')
    fig.suptitle('Deux ellipsoïdes disjoints : projections et fonctions support',fontsize=16)
    fig.supxlabel(f"Distance ≈ {d['superieure']:.8f}   •   Écart primal-dual ≈ {d['ecart']:.2e}   •   Virgule flottante",fontsize=10,color=INK)
    save(fig,'deux_ellipsoides')
    return files


if __name__=='__main__':
    print(export(Path(__file__).resolve().parent/'illustrations'))
