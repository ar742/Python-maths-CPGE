"""Figures SVG originales, calculées avec les mêmes données que les laboratoires."""
from __future__ import annotations
from pathlib import Path
import math
import json
import textwrap
import numpy as np

COLORS=['#2c7564','#c76c4e','#7961a2','#bd9853','#5d91a2']
INK='#254e43';PAPER='#fffdf7';MUTED='#6b7869';PINK='#b45880'

def graph(ax, molecule):
    from matplotlib.path import Path as CurvePath
    from matplotlib.patches import PathPatch, Polygon
    atoms={str(a['id']):a for a in molecule.get('atoms',[])}
    bounds_points=[(a['x'],a['y']) for a in atoms.values()]
    for q in molecule.get('arrows',[]): bounds_points.extend([q['start'],q['end'],q.get('control',q['start'])])
    if bounds_points:
        px,py=np.array(bounds_points).T
        scale=min(ax.get_window_extent().width/(max(px)-min(px)+1.3),ax.get_window_extent().height/(max(py)-min(py)+1.3))
        bond_gap=4.5/max(scale,1)
    else: bond_gap=.07
    for bond in molecule.get('bonds',[]):
        a=atoms.get(str(bond['a']));b=atoms.get(str(bond['b']))
        if a is None or b is None: continue
        x,y=a['x'],a['y'];xx,yy=b['x'],b['y'];dx,dy=xx-x,yy-y
        norm=math.hypot(dx,dy) or 1;nx,ny=-dy/norm,dx/norm
        style=bond.get('style',bond.get('stereo',''));color=bond.get('color',INK)
        if style=='wedge':
            ax.add_patch(Polygon([[x,y],[xx+nx*.06,yy+ny*.06],[xx-nx*.06,yy-ny*.06]],color=color))
        elif style in ('dash','hashed'):
            for step in np.linspace(.1,.9,7):
                half=.065*step
                ax.plot([x+step*dx-half*nx,x+step*dx+half*nx],[y+step*dy-half*ny,y+step*dy+half*ny],color=color,lw=1)
        else:
            order=bond.get('order',1);n=3 if order==3 else 2 if order>=1.5 else 1
            for i in range(n):
                offset=(i-(n-1)/2)*bond_gap
                ax.plot([x+nx*offset,xx+nx*offset],[y+ny*offset,yy+ny*offset],color=color,lw=1.9,
                        ls='--' if style=='dashed' or order==1.5 and i==1 else '-')
    points=[]
    for atom in atoms.values():
        x,y=atom['x'],atom['y'];points.append((x,y));label=atom.get('label',atom['element'])
        if not label and not atom.get('charge') and not atom.get('radical'): continue
        color={'O':COLORS[1],'N':COLORS[2],'Cl':COLORS[0],'Br':PINK,'S':COLORS[3],'P':COLORS[3],'Mg':COLORS[4]}.get(atom['element'],INK)
        ax.text(x,y,label,ha='center',va='center',fontsize=11,color=color,
                bbox=dict(facecolor=PAPER,edgecolor='none',pad=1.2),zorder=4)
        charge=atom.get('charge',0)
        if charge:
            sign='+' if charge>0 else '−';charge_text=sign if abs(charge)==1 else str(abs(charge))+sign
            ax.annotate(charge_text,(x,y),xytext=(12,9),textcoords='offset points',color=color,fontsize=9,zorder=5)
        if atom.get('radical'): ax.annotate('•',(x,y),xytext=(12,10),textcoords='offset points',color=color)
        for k in range(min(3,atom.get('lone_pairs',0))):
            ax.annotate('··',(x,y),xytext=(-6+9*k,12),textcoords='offset points',color=color,fontsize=10,zorder=5)
    for arrow in molecule.get('arrows',[]):
        start=arrow['start'];end=arrow['end'];control=arrow.get('control',[(start[0]+end[0])/2,(start[1]+end[1])/2+.65])
        path=CurvePath([start,control,end],[CurvePath.MOVETO,CurvePath.CURVE3,CurvePath.CURVE3])
        ax.add_patch(PathPatch(path,facecolor='none',edgecolor=PINK,lw=1.8,zorder=6))
        tangent=np.array(end)-np.array(control);norm=np.linalg.norm(tangent) or 1;tangent=tangent/norm
        normal=np.array([-tangent[1],tangent[0]])
        tail=np.array(end)-.12*tangent
        one=tail+.065*normal;two=tail-.065*normal
        ax.plot([one[0],end[0]],[one[1],end[1]],color=PINK,lw=1.8,zorder=7)
        if arrow.get('electrons',2)!=1: ax.plot([two[0],end[0]],[two[1],end[1]],color=PINK,lw=1.8,zorder=7)
        points.extend([start,end,control])
        if arrow.get('label'): ax.text(control[0],control[1]+.12,arrow['label'],color=PINK,fontsize=8,ha='center')
    if points:
        x,y=np.array(points).T;x0,x1=min(x),max(x);y0,y1=min(y),max(y)
        ax.set_xlim(x0-.65,x1+.65);ax.set_ylim(y0-.65,y1+.65)
    ax.set_aspect('equal',adjustable='box');ax.axis('off')

def plot_chart(ax, chart):
    for i,curve in enumerate(chart.get('series',[])):
        ax.plot(curve['x'],curve['y'],color=COLORS[i%len(COLORS)],lw=1.8,label=curve['label'])
    if chart.get('x_scale')=='log': ax.set_xscale('log')
    if chart.get('y_scale')=='log': ax.set_yscale('log')
    if chart.get('x_reverse'): ax.invert_xaxis()
    if chart.get('x_scale')!='log': ax.ticklabel_format(axis='x',style='plain',useOffset=False)
    ax.set_xlabel(chart.get('x_label',''),fontsize=10);ax.set_ylabel(chart.get('y_label',''),fontsize=10)
    ax.set_title('\n'.join(textwrap.wrap(chart['title'],51)),fontsize=12,color=INK,loc='left',pad=13)
    ax.grid(alpha=.2);ax.tick_params(labelsize=9)
    if chart.get('series'): ax.legend(frameon=False,fontsize=9,loc='best')
    for spine in ax.spines.values(): spine.set_color('#d2dacb')

def draw_scene(ax, data):
    from matplotlib.patches import Circle,Rectangle,Polygon
    kind=data.get('kind');ax.set_facecolor(PAPER)
    ax.set_title('\n'.join(textwrap.wrap(data.get('title','Lire les structures'),60)),fontsize=10,color=INK,loc='left',pad=8)
    if kind=='mechanism':
        frames=data.get('frames',[]);index=max(0,min(len(frames)-1,data.get('index',0)))
        if frames:
            selected=frames[index];graph(ax,selected.get('molecule',selected))
            ax.text(.02,-.03,f"Étape {index+1}/{len(frames)} · {selected.get('name',selected.get('title',''))}",transform=ax.transAxes,fontsize=9,color=MUTED)
    elif kind=='molecules':
        ax.axis('off');molecules=data.get('molecules',[]);count=len(molecules)
        cols=count if count<=3 else 2;rows=math.ceil(count/max(cols,1))
        for i,molecule in enumerate(molecules):
            col=i%cols;row=i//cols
            child=ax.inset_axes([col/cols+.01,1-(row+1)/rows+.015,.94/cols,.79/rows])
            graph(child,molecule)
            child.set_title('\n'.join(textwrap.wrap(molecule.get('name',''),18 if count==3 else 27)),fontsize=10,color=INK,pad=5)
        if count==3 and any(isinstance(c,dict) and c.get('a')==0 and c.get('b')==2 for c in data.get('connectors',[])):
            ax.text(1/3,.52,'+',transform=ax.transAxes,ha='center',color=COLORS[1],fontsize=14)
            ax.text(2/3,.52,'→',transform=ax.transAxes,ha='center',color=COLORS[1],fontsize=17)
    elif kind=='spectrum':
        ax.plot(data['x'],data['y'],color=COLORS[0],lw=1.4)
        if data.get('reverse_x') or 'ppm' in data.get('x_label','') or 'cm' in data.get('x_label',''): ax.invert_xaxis()
        ax.set_xlabel(data.get('x_label',''));ax.set_ylabel(data.get('y_label','Signal simulé'));ax.grid(alpha=.2)
        unique_peaks=list({q.get('label',''):q for q in data.get('peaks',[])}.values())
        for peak in unique_peaks[:5]:
            position=peak.get('position',peak.get('x'));ax.axvline(position,color='#c4cec0',lw=.7,ls='--')
            ax.text(position,.96,peak.get('label',''),rotation=90,transform=ax.get_xaxis_transform(),va='top',fontsize=8,color=COLORS[1])
        groups={}
        for peak in data.get('peaks',[]): groups.setdefault(peak.get('label',''),[]).append(peak.get('position',peak.get('x')))
        multiple=next(((label,positions) for label,positions in groups.items() if len(positions)>1),None)
        if multiple:
            label,positions=multiple;lo=min(positions)-.055;hi=max(positions)+.055
            x=np.asarray(data['x']);y=np.asarray(data['y']);mask=(x>=lo)&(x<=hi)
            child=ax.inset_axes([.075,.25,.33,.31]);child.set_facecolor(PAPER)
            child.plot(x[mask],y[mask],color=COLORS[1],lw=1.2);child.invert_xaxis()
            child.set_title('Détail : '+label,fontsize=8,color=COLORS[1]);child.set_xlabel('δ / ppm',fontsize=8);child.set_yticks([]);child.tick_params(labelsize=7)
    elif kind=='dipoles':
        ax.axis('off')
        child=ax.inset_axes([0,.12,.45,.78]);graph(child,data['molecule'])
        child.set_title('Positions des NO₂',fontsize=9,color=INK)
        vector=ax.inset_axes([.55,.12,.45,.78]);vector.set_aspect('equal')
        scale=max(1,data.get('mu0',1),data.get('magnitude',1))
        for item in data.get('vectors',[]):
            start=item['start'];end=item['end']
            if math.dist(start,end)<1e-10:continue
            color=COLORS[2] if item['role']=='resultant' else COLORS[0]
            if item['role']=='component':vector.plot([start[0],end[0]],[start[1],end[1]],ls='--',color=MUTED,lw=1)
            else:vector.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=color,lw=2))
        vector.axhline(0,color='#d2dacb',lw=.5);vector.axvline(0,color='#d2dacb',lw=.5)
        vector.set_xlim(-scale*1.1,scale*1.1);vector.set_ylim(-scale*1.1,scale*1.1)
        vector.set_title('Somme vectorielle / D',fontsize=9,color=INK);vector.tick_params(labelsize=7)
        ax.text(.02,0,f"{data['isomer']} : |μ| = {data['magnitude']:.3g} D ; angle {data['angle_deg']:g}°",transform=ax.transAxes,fontsize=9,color=INK)
    elif kind=='newman' and data.get('variant')=='e2':
        ax.axis('off');child=ax.inset_axes([0,.1,.52,.82])
        draw_scene(child,dict(data,variant='plain',cip_projection=True,title='Regard C3 → C4'))
        if data.get('product'):
            product=ax.inset_axes([.59,.15,.4,.68]);graph(product,data['product'])
            product.set_title('Produit '+data['product_configuration'],fontsize=9,color=INK)
        else:ax.text(.62,.5,'Pas de conformation anti',transform=ax.transAxes,fontsize=10,color=COLORS[1])
    elif kind=='bars':
        values=data.get('values',[]);labels=data.get('labels',[])
        ax.barh(np.arange(len(values)),values,color=[COLORS[i%len(COLORS)] for i in range(len(values))])
        ax.set_yticks(np.arange(len(labels)),['\n'.join(textwrap.wrap(q,15)) for q in labels],fontsize=8);ax.invert_yaxis();ax.set_xlabel(data.get('unit',''));ax.grid(axis='x',alpha=.2)
    elif kind=='newman' and data.get('variant')=='cyclohexane' and data.get('molecules'):
        draw_scene(ax,dict(data,kind='molecules'))
    elif kind=='newman':
        ax.add_patch(Circle((0,0),.45,fill=False,color=COLORS[0],lw=2));angle=math.radians(data.get('angle',0))
        # Le repère CIP est construit avec y vers le haut ; le canvas utilise y vers le bas.
        # Inverser les deux angles conserve la configuration, contrairement à une réflexion.
        angles=[-math.pi/2,math.pi/6,5*math.pi/6]
        if data.get('cip_projection'):
            angles=[-a for a in angles];angle=-angle
        for i,a in enumerate(angles):
            aa=a+angle
            ax.plot([.45*math.cos(aa),math.cos(aa)],[.45*math.sin(aa),math.sin(aa)],color=COLORS[1],lw=2)
            ax.text(1.18*math.cos(aa),1.18*math.sin(aa),data.get('back',['H']*3)[i],ha='center',va='center',color=COLORS[1],fontsize=11)
            ax.plot([0,.9*math.cos(a)],[0,.9*math.sin(a)],color=COLORS[0],lw=2)
            ax.text(1.08*math.cos(a),1.08*math.sin(a),data.get('front',['H']*3)[i],ha='center',va='center',color=COLORS[0],fontsize=11)
        ax.plot(0,0,'o',color=COLORS[0]);ax.set_xlim(-1.55,1.55);ax.set_ylim(-1.55,1.5);ax.set_aspect('equal');ax.axis('off')
        ax.text(0,-1.5,f"Dièdre : {data.get('angle',0):g}°",ha='center',fontsize=10,color=MUTED)
    elif kind=='stereo':
        for vector in data.get('vectors',[]):
            x,y,z=vector['xyz'];xx=x+.3*z;yy=y-.25*z
            if z>0: ax.add_patch(Polygon([[0,0],[xx+.04,yy-.04],[xx-.04,yy+.04]],color=COLORS[0]))
            else: ax.plot([0,xx],[0,yy],color=INK,lw=2,ls='--' if z<0 else '-')
            ax.text(xx*1.15,yy*1.15,str(vector['rank'])+'. '+vector['label'],ha='center',fontsize=10,color=INK)
        ax.plot(0,0,'o',color=INK);ax.set_xlim(-1.8,1.8);ax.set_ylim(-1.8,1.8);ax.set_aspect('equal');ax.axis('off')
        ax.text(.02,.03,'Configuration : '+str(data.get('configuration','')),transform=ax.transAxes,fontsize=12,color=COLORS[0])
    elif kind=='chromatography':
        ax.add_patch(Rectangle((0,0),1,1,facecolor='#eee9d7',edgecolor=MUTED));ax.axhline(.08,color=INK,lw=1);ax.axhline(.92,color=COLORS[4],ls='--',lw=1)
        lanes=list(dict.fromkeys(q.get('lane',0) for q in data.get('spots',[])))
        for i,lane in enumerate(lanes):
            x=(i+1)/(len(lanes)+1)
            for spot in data.get('spots',[]):
                if spot.get('lane',0)==lane:
                    y=.08+.84*spot['rf'];ax.plot(x,y,'o',color=COLORS[i%len(COLORS)],ms=11)
                    ax.annotate(spot.get('label',''),(x,y),xytext=(8,3),textcoords='offset points',fontsize=8)
            ax.text(x,-.065,str(lane),ha='center',fontsize=9)
        ax.set_xlim(-.08,1.08);ax.set_ylim(-.14,1.09);ax.axis('off')
    elif kind=='extraction':
        ax.add_patch(Polygon([[-.3,1.5],[-.3,1.1],[-.85,.7],[-.75,0],[0,-.8],[.75,0],[.85,.7],[.3,1.1],[.3,1.5]],facecolor='#e2edf0',edgecolor=INK,lw=1.5))
        ax.add_patch(Polygon([[-.75,.65],[-.73,.03],[0,-.72],[.73,.03],[.75,.65]],facecolor='#f2d9bd',edgecolor='none'))
        ax.plot([0,0],[-.8,-1.1],color=INK,lw=3);ax.plot([-.16,.16],[-.98,-.98],color=COLORS[0],lw=3)
        ax.text(0,.84,'Phase supérieure',ha='center',fontsize=9);ax.text(0,-.05,'Phase inférieure',ha='center',fontsize=9)
        ax.text(-1.1,-1.4,f"Organique : {data.get('organic',0):.4g} {data.get('unit','')}\nAqueuse : {data.get('aqueous',0):.4g} {data.get('unit','')}",fontsize=10,color=INK)
        ax.set_xlim(-1.3,1.3);ax.set_ylim(-1.65,1.65);ax.set_aspect('equal');ax.axis('off')
    elif kind=='network':
        nodes={str(n['id']):n for n in data.get('nodes',[])}
        for edge in data.get('edges',[]):
            a=nodes.get(str(edge['a']));b=nodes.get(str(edge['b']))
            if not a or not b: continue
            ax.annotate('',xy=(b['x'],b['y']),xytext=(a['x'],a['y']),arrowprops=dict(arrowstyle='->',color=COLORS[0],shrinkA=25,shrinkB=25))
            ax.text((a['x']+b['x'])/2,(a['y']+b['y'])/2+.75,'\n'.join(textwrap.wrap(('' if edge.get('label')=='Séquence explicite' else edge.get('label','')),24)),fontsize=7,ha='center',color=MUTED)
        for node in nodes.values():
            ax.text(node['x'],node['y'],'\n'.join(textwrap.wrap(node.get('label',str(node['id'])),14)),ha='center',va='center',fontsize=9,color=INK,bbox=dict(boxstyle='round,pad=.5',facecolor='#e8f0dc' if node.get('active') or str(node['id'])==str(data.get('active')) else PAPER,edgecolor='#cbd7c0'))
        if nodes:
            x=[n['x'] for n in nodes.values()];y=[n['y'] for n in nodes.values()];ax.set_xlim(min(x)-.75,max(x)+.75);ax.set_ylim(min(y)-.75,max(y)+.75)
        if data.get('molecule'):
            ax.set_ylim(min(y)-2.5,max(y)+.75)
            child=ax.inset_axes([.18,-.03,.64,.38]);graph(child,data['molecule'])
            child.set_title(data['molecule'].get('name','Structure suivie'),fontsize=9,color=INK,pad=3)
        ax.axis('off')
    elif kind=='orbitals':
        levels=data.get('levels',[]);index=max(0,min(len(levels)-1,data.get('selected',0)))
        if levels:
            for i,c in enumerate(levels[index].get('coefficients',[])):
                radius=.55*abs(c)
                if abs(c)<1e-9: ax.plot(i,0,'o',color=MUTED,ms=3)
                ax.add_patch(Circle((i,.22),radius,color=COLORS[0] if c>=0 else COLORS[2],alpha=.8))
                ax.add_patch(Circle((i,-.22),radius,color=COLORS[2] if c>=0 else COLORS[0],alpha=.8))
                ax.text(i,-.75,f'{c:.3f}',ha='center',fontsize=10)
            n=len(levels[index].get('coefficients',[]));ax.set_xlim(-.7,n-.3);ax.set_ylim(-1.2,1.2);ax.set_aspect('equal');ax.axis('off')
            ax.text(.02,.05,levels[index].get('label','')+' · sites numérotés ; couleurs = signes',transform=ax.transAxes,color=MUTED,fontsize=10)
    elif kind=='energy':
        curves=data.get('curves') or [dict(x=data['x'],y=data['y'],label='')]
        for i,c in enumerate(curves): ax.plot(c['x'],c['y'],color=COLORS[i%len(COLORS)],lw=2,label=c.get('label',''))
        if len(curves)>1: ax.legend(frameon=False,fontsize=8)
        ax.set_xlabel(data.get('x_label','Coordonnée de réaction'));ax.set_ylabel(data.get('y_label','Énergie (kJ·mol⁻¹)'));ax.grid(alpha=.2)
    else:
        ax.axis('off');ax.text(.1,.5,'Les bilans et les conditions\nprécèdent le choix du modèle.',transform=ax.transAxes,fontsize=14,color=INK)

def make_figure(lab, result):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({'svg.hashsalt':'chimie-organique-cpge','svg.fonttype':'none','font.family':'DejaVu Sans','text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':MUTED})
    fig,(left,right)=plt.subplots(1,2,figsize=(12.4,6.1),gridspec_kw={'width_ratios':[1.05,1]})
    fig.patch.set_facecolor(PAPER);left.set_facecolor(PAPER);right.set_facecolor(PAPER)
    fig.subplots_adjust(left=.07,right=.96,top=.73,bottom=.22,wspace=.30)
    fig.suptitle('\n'.join(textwrap.wrap(lab['title'],85)),x=.055,y=.96,ha='left',fontsize=17,fontweight='bold',color=INK)
    fig.text(.055,.855,lab['category']+' · Liaisons & Synthèses · CPGE',fontsize=10,color=COLORS[0])
    draw_scene(left,result.get('scene',{}))
    charts=[c for c in result.get('charts',[]) if c.get('series')]
    if charts: plot_chart(right,charts[1] if lab['id']=='rmn' and len(charts)>1 else charts[0])
    else:
        right.axis('off');right.set_title('Les grandeurs et les décisions',fontsize=12,color=INK,loc='left')
        y=.95
        for metric in result.get('metrics',[])[:7]:
            value=metric['value'];value=f'{value:.5g}' if isinstance(value,(int,float)) else str(value)
            text='\n'.join(textwrap.wrap(metric['label']+' : '+value+' '+metric.get('unit',''),53))
            right.text(.02,y,text,transform=right.transAxes,fontsize=11,color=INK,va='top');y-=.13+.04*text.count('\n')
    caption=result.get('scene',{}).get('description','')
    fig.text(.055,.12,'\n'.join(textwrap.wrap(caption,151)),fontsize=9,color=MUTED,va='top')
    fig.text(.055,.035,'Figure originale issue des calculs Python · paramètres du préréglage initial · données et limites explicitées dans le TP',fontsize=8,color=MUTED)
    return fig

def export(destination, previews=None):
    import matplotlib.pyplot as plt
    from catalogue import LABS
    from modeles import calculate
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True);metadata=[]
    if previews: Path(previews).mkdir(parents=True,exist_ok=True)
    for lab in LABS:
        result=calculate({'lab':lab['id']});fig=make_figure(lab,result);file=lab['id']+'.svg'
        fig.savefig(destination/file,format='svg',metadata={'Date':None,'Title':lab['title'],'Description':result['scene']['description']})
        if previews: fig.savefig(Path(previews)/(lab['id']+'.png'),dpi=115)
        plt.close(fig)
        metadata.append(dict(file=file,title=lab['title'],caption=result['scene']['description'],labs=[lab['id']]))
    (destination/'catalogue.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    lines=['# Galerie : Liaisons & Synthèses','', f'{len(metadata)} figures originales issues des mêmes données et calculs que les laboratoires. Les conditions, paramètres et limites figurent dans chaque TP.','']
    for item in metadata: lines.extend(['## '+item['title'],'','!['+item['title']+']('+item['file']+')','',item['caption'],''])
    (destination/'README.md').write_text('\n'.join(lines),encoding='utf-8',newline='\n')
    return f'{len(metadata)} figures SVG créées dans {destination}'

if __name__=='__main__':
    print(export(Path(__file__).resolve().parent/'illustrations'))
