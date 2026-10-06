"""24 figures scientifiques originales, reproductibles et autonomes.

La galerie ne reproduit aucune page du recueil. Les courbes reprennent les
modèles publiés et les géométries explicitent leurs conditions aux limites.
Matplotlib est un complément pour régénérer les SVG, inutile pour les TP.
"""
from pathlib import Path
import json
import os
import tempfile
import textwrap

os.environ.setdefault('MPLCONFIGDIR',str(Path(tempfile.gettempdir())/'cpge-em-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
import numpy as np

from modeles import calculate
from catalogue import LAB_BY_ID

P=['#594271','#258b81','#b58848','#b36b81','#4c819e']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'text.color':'#342b46',
    'axes.labelcolor':'#342b46','axes.edgecolor':'#bfb0c6','axes.facecolor':'#fcfaf7',
    'axes.spines.top':False,'axes.spines.right':False,'xtick.color':'#75687d',
    'ytick.color':'#75687d','figure.facecolor':'white','svg.fonttype':'none',
    'svg.hashsalt':'cpge-electromagnetisme','axes.formatter.use_mathtext':True})

CAPTIONS={
 'dipoles':('Deux charges et leur approximation dipolaire','Deux charges opposées séparées de a, p dirigé de −q vers +q. Les lignes sont celles de E ; ce ne sont pas des trajectoires. L’erreur relative de l’approximation dipolaire décroît loin des charges.'),
 'gauss':('Une symétrie, deux intégrations','Sphère uniformément chargée en volume : E est linéaire à l’intérieur et décroît en 1/r² à l’extérieur. Le potentiel choisi nul à l’infini est continu, ainsi que sa dérivée, en l’absence de charge surfacique.'),
 'biotsavart':('Une spire est aussi un dipôle magnétique','Biot–Savart est intégré sur la spire. Le champ axial exact μ₀IR²/[2(R²+z²)^(3/2)] retrouve au loin le champ d’un moment m=IπR² ; les lignes de B n’ont pas de source magnétique.'),
 'helmholtz':('Annuler la courbure pour gagner en uniformité','Deux bobines identiques, parcourues dans le même sens. Pour d=R, B″(0)=0 : le premier écart axial est d’ordre quatre. La carte hors axe est obtenue par intégration de Biot–Savart, pas par prolongement arbitraire du profil axial.'),
 'drude':('Une conductivité complexe avec une mémoire','Avec exp(−iωt), σ=ne²τ/[m(1−iωτ)]. La partie réelle dissipe et la partie imaginaire décrit une réponse inertielle. Un changement du signe des porteurs inverse leur vitesse, sans inverser la conductivité longitudinale.'),
 'hall':('Des bornes explicites pour interpréter le signe','Courant I vers +x, B suivant +z et UHall=V(y=−w/2)−V(y=+w/2). L’équilibre q(EH+v×B)=0 donne UHall=IB/(nqt). Le signe dépend des porteurs et du choix des bornes.'),
 'induction':('Lenz ferme aussi un bilan de puissance','Barreau sur rails, i orienté vers +y : L di/dt+Ri=−Bℓv et m dv/dt=Bℓi. L’énergie cinétique et l’énergie magnétique se convertissent en chaleur Joule. Un cadre entièrement immergé dans un champ uniforme a au contraire un flux constant.'),
 'hautparleur':('La même constante relie force et contre-fem','u=Ri+L di/dt+κv et m dv/dt+bv+kx=κi. Les puissances κiv s’annulent dans le bilan total ; la résonance mécanique modifie aussi l’impédance électrique vue par le générateur.'),
 'hysteresis':('Une mémoire mesurée par son aire','Modèle de domaines à relais : une branche dépend de l’histoire. L’aire positive ∮H dB est l’énergie perdue par unité de volume et par cycle. Le transformateur permet de reconstruire H par i₁ et B par intégration de la tension secondaire orientée.'),
 'synchrone':('Angle de charge et stabilité synchrone','Le modèle dipolaire a une paire de pôles et un champ tournant à Ωs. Le couple varie comme sin δ et la stabilité locale de la branche motrice exige cos δ>0. L’angle électrique et l’angle mécanique coïncident seulement dans ce modèle.'),
 'asynchrone':('Le glissement organise la conversion','Dans le schéma équivalent retenu, Pjoule,rotor=s Pentrefer et Pmécanique=(1−s)Pentrefer. Le couple s’annule à s=0 : une cage asynchrone a besoin d’un glissement pour produire un couple.'),
 'peau':('Diffusion magnétique et effet de peau','Conducteur ohmique, déplacement négligé : ∂tB=(μσ)⁻¹ΔB et δ=√[2/(μσω)]. Le profil harmonique est amorti et déphasé ; le transitoire s’étale comme √t. Cette dissipation résistive n’est pas l’effet Meissner.'),
 'maxwell':('L’onde transporte ou échange de l’énergie','E et B sont transverses ; B=(k/ω)×E pour une onde plane progressive. S=E×B/μ₀ est un flux instantané. Deux ondes opposées forment une onde stationnaire de flux moyen nul, avec échanges locaux entre énergies électrique et magnétique.'),
 'interfaces':('Raccorder les champs, comparer les flux','Interface plane sans pertes, indices réels : les amplitudes de Fresnel vérifient les raccordements de Maxwell. R+T=1 avec le facteur de flux normal ; |t|² seul n’est pas T. Brewster concerne TM ; en réflexion totale, le champ transmis est évanescent.'),
 'guide':('Une condition électrique impose la coupure','Guide métallique idéal, TE₁₀ : Ey∝sin(πx/a), fc=c/(2a), β²=(ω/c)²−(π/a)². Les parois imposent E tangentiel nul. Sous la coupure, β imaginaire décrit la décroissance, sans vitesse de groupe propagative.'),
 'antenne':('L’ouverture commande un diagramme angulaire','Champ lointain d’une ouverture uniforme : puissance normalisée sinc²[π(a/λ)(sin θ−sin θ₀)]. La formule porte sur sin θ. Une ouverture plus petite que λ peut ne posséder aucun zéro dans le domaine visible.'),
 'plasma':('Choisir la racine qui absorbe dans le bon sens','Plasma froid de Drude : εr=1−ωp²/[ω(ω+iν)] pour exp(−iωt). La racine passive donne Im k≥0. Une coupure nette concerne le modèle sans collisions ; lorsque ν>0, l’absorption doit être prise en compte.'),
 'dielectrique':('Résonance, absorption et charges liées','Lorentz : χ=χ₀/[1−(ω/ω₀)²−iγω/ω₀²]. Dans un milieu non magnétique, n²=εr. La sphère électrostatique utilise la limite statique de cette loi : σliée=P·n, ρliée=−div P et champ intérieur uniforme.'),
 'aimantation':('Les moments voient le champ intérieur','Langevin classique et tanh pour deux niveaux décrivent deux paramagnétismes distincts ; le diamagnétisme orbital oppose sa réponse au champ. Dans un ellipsoïde uniformément aimanté, Hint=Hext−NM. La courbe ne constitue pas un modèle de ferromagnétisme.'),
 'meissner':('Deux faces, deux courants de London','Plaque x∈[−a,a] : B=B₀ cosh(x/λL)/cosh(a/λL), jy=−(1/μ₀)dB/dx. Le profil expulse le champ à l’équilibre. Dans un conducteur parfait idéal, le champ dépend au contraire du flux initial conservé.'),
 'faraday':('Une rotation qui s’ajoute au retour','Deux indices circulaires différents donnent θ=VBL. L’aller-retour additionne les angles dans des axes fixes du laboratoire. La transmission par un analyseur suit la loi de Malus ; un rotateur réciproque présente un autre comportement au retour.'),
 'kerr':('Diffraction et non-linéarité peuvent se compenser','Milieu Kerr optique focalisant : n=n₀+n₂I. Le modèle paraxial cubique unidimensionnel admet un profil sech localisé auto-guidé. Les intensités calculées donnent aussi un critère de validité ; il ne s’agit ni du Kerr électro-optique statique ni du Kerr magnéto-optique.'),
 'rayonnement':('Rayleigh et Thomson ne suivent pas la même loi','Un dipôle électrique rayonne une puissance angulaire en sin²θ. Avec une polarisabilité quasi constante, la diffusion de Rayleigh varie comme ω⁴ ; pour un électron libre, la réponse inertielle produit la limite de Thomson indépendante de la fréquence.'),
 'dynamo':('Entretenir un champ dans un fluide conducteur','Modèle local α² prescrit : un mode hélicoïdal évolue comme exp[(±αk−ηmk²)t], ηm=1/(μσ). La diffusion concurrence l’induction. Rm>1 n’est pas une condition suffisante de dynamo ; le noyau externe terrestre est un fluide conducteur en mouvement.')}
FIGURES=[dict(file=key+'.svg',title=title,labs=[key],caption=caption) for key,(title,caption) in CAPTIONS.items()]


def chart(ax,c,title=None):
    for i,s in enumerate(c['series']):
        ax.plot(s['x'],s['y'],label=s['label'],color=P[i%len(P)],lw=2)
    ax.set(xlabel=c['x_label'],ylabel=c['y_label'],title=title or c['title'])
    if c.get('x_scale')=='log':ax.set_xscale('log')
    if c.get('y_scale')=='log':ax.set_yscale('log')
    ax.grid(alpha=.2)
    ax.legend(fontsize=8,loc='best')


def field(ax,f):
    x,y=np.array(f['x']),np.array(f['y'])
    u,v=np.array(f['u']),np.array(f['v'])
    scalar=np.array(f['scalar'])
    cap=np.quantile(np.abs(scalar),.93) or 1
    ax.pcolormesh(x,y,np.clip(scalar,-cap,cap),cmap='PuOr_r',shading='auto',alpha=.32,vmin=-cap,vmax=cap,rasterized=False)
    speed=np.hypot(u,v)
    u=np.ma.masked_where(~np.isfinite(speed),u)
    v=np.ma.masked_where(~np.isfinite(speed),v)
    for c in f.get('charges',[]):
        X,Y=np.meshgrid(x,y)
        mask=np.hypot(X-c['x'],Y-c['y'])<c.get('mask_radius',0)
        u=np.ma.masked_where(mask,u);v=np.ma.masked_where(mask,v)
        ax.scatter([c['x']],[c['y']],s=80,color=P[2] if c['q']>0 else P[0],zorder=5)
        ax.text(c['x'],c['y'],'+' if c['q']>0 else '−',color='white',ha='center',va='center',zorder=6)
    ax.streamplot(x,y,u,v,color=P[1],density=1.2,linewidth=.9,arrowsize=.9)
    for wire in f.get('wires',[]):ax.add_patch(Circle((wire['x'],wire['y']),wire['radius'],color=P[2],zorder=7))
    if f.get('obstacle'):
        o=f['obstacle'];ax.add_patch(Circle((o.get('x',0),o.get('y',0)),o['r'],color='#ead9ba',zorder=7))
    ax.set(xlabel=f.get('x_label','x')+' ('+f.get('x_unit','m')+')',ylabel=f.get('y_label','y')+' ('+f.get('y_unit','m')+')',title=f['title'],aspect='equal')
    ax.locator_params(axis='both',nbins=5)


def schematic_hall(ax,p):
    ax.add_patch(Rectangle((.1,.2),.8,.45,facecolor='#e1f0eb',edgecolor=P[1],lw=2))
    ax.annotate('',(.75,.42),(.22,.42),arrowprops=dict(arrowstyle='->',color=P[2],lw=3))
    ax.text(.45,.47,'I → +x',ha='center')
    ax.text(.5,.74,'y=+w/2 : borne − de UHall',ha='center',fontsize=9)
    ax.text(.5,.10,'y=−w/2 : borne + de UHall',ha='center',fontsize=9)
    for x in np.linspace(.17,.83,7):
        ax.add_patch(Circle((x,.57),.015,fill=False,edgecolor=P[0]));ax.plot(x,.57,'.',color=P[0])
    ax.text(.5,.88,'B vers +z (sort du dessin)',ha='center')
    ax.set(xlim=(0,1),ylim=(0,1),title='Le signe exige un repère et deux bornes');ax.axis('off')


def draw_special(ax,key,r):
    s=r.get('scene',{})
    if r.get('field'):
        field(ax,r['field'])
        radius=r['params'].get('R') if key=='gauss' else r['scene']['sphere_radius_m'] if key=='dielectrique' else None
        if radius:ax.add_patch(Circle((0,0),radius,fill=False,edgecolor=P[0],lw=1.5,ls='--'))
        return True
    if key in ('antenne','rayonnement'):
        theta=np.array(s['angles'])*np.pi/180
        power=np.array(s.get('gain',s.get('pattern')))
        # Diagramme cartésien équivalent au polaire, rayon = puissance relative.
        for rr in [.25,.5,.75,1]:ax.add_patch(Circle((0,0),rr,fill=False,edgecolor='#d6cadb',lw=.7))
        if key=='rayonnement':
            ax.plot(power*np.sin(theta),power*np.cos(theta),color=P[1],lw=2)
            ax.plot(-power*np.sin(theta),power*np.cos(theta),color=P[1],lw=2)
            ax.annotate('+z · axe du dipôle',xy=(0,.99),xytext=(.15,.82),ha='left',fontsize=8,arrowprops=dict(arrowstyle='->',color=P[0]))
        else:ax.plot(power*np.cos(theta),power*np.sin(theta),color=P[1],lw=2)
        ax.set(aspect='equal',xlabel='Puissance relative · direction horizontale',ylabel='Puissance relative · direction verticale',title='Diagramme de puissance normalisé')
        return True
    if key=='hall':schematic_hall(ax,r['params']);return True
    if key=='faraday':
        theta=s['theta_single']
        initial=r['params']['initial']*np.pi/180
        for i,a in enumerate([initial,initial+theta,initial+2*theta]):
            x=1+3*i;ax.add_patch(Circle((x,0),.9,fill=False,edgecolor='#c8b7d1'))
            ax.plot([x-.85*np.cos(a),x+.85*np.cos(a)],[-.85*np.sin(a),.85*np.sin(a)],color=P[2] if i==0 else P[1],lw=4)
            ax.text(x,-1.4,['Entrée','Un passage','Aller-retour'][i],ha='center')
        ax.set(xlim=(-.3,8.4),ylim=(-2,1.8),aspect='equal',title='Axes fixes du laboratoire : les rotations s’ajoutent');ax.axis('off');return True
    if key=='guide':
        E=np.array(s['Ey']);x=np.array(s['x_over_a']);z=np.array(s['z_over_a'])
        if E.shape==(len(z),len(x)):
            im=ax.pcolormesh(z,x,E.T,shading='auto',cmap='PuOr_r')
        else:im=ax.pcolormesh(z,x,E,shading='auto',cmap='PuOr_r')
        ax.set(xlabel='z/a',ylabel='x/a',title='TE₁₀ : champ Ey (V/m), parois x/a=0 et 1')
        ax.figure.colorbar(im,ax=ax,pad=.03,label='Ey (V/m)');return True
    if key=='maxwell':
        z=np.array(s['z_over_lambda']);E=np.array(s['E']);B=np.array(s['cB'])
        ax.plot(z,E[:,0],color=P[2],label='Ex (V/m)');ax.plot(z,B[:,1],color=P[1],label='cBy (V/m)')
        ax.set(xlabel='z/λ',ylabel='Champ et cB (V/m)',title='Même unité pour comparer E et cB');ax.legend(fontsize=8);ax.grid(alpha=.2);return True
    if key=='meissner':
        ax.fill_between(s['x_nm'],s['B_mT'],color='#d9efea')
        ax.plot(s['x_nm'],s['B_mT'],color=P[1],lw=2,label='Équilibre London')
        ax.plot(s['x_nm'],np.full(len(s['x_nm']),s['B_perfect_mT']),color=P[0],ls='--',label='Conducteur parfait · histoire choisie')
        ax.set(xlabel='x (nm)',ylabel='B (mT)',title='La pénétration se fait depuis les deux faces');ax.legend(fontsize=8);ax.grid(alpha=.2);return True
    if key=='dynamo':
        from matplotlib.patches import Ellipse
        ax.add_patch(Circle((0,0),1,facecolor='#e2d8e9',edgecolor=P[0],lw=1.5))
        ax.add_patch(Circle((0,0),.72,facecolor='#c2e5dc',edgecolor=P[1],lw=1.5))
        ax.add_patch(Circle((0,0),.27,facecolor='#e9c988',edgecolor=P[2],lw=1.5))
        for x in [-.49,.49]:
            ax.add_patch(Ellipse((x,0),.26,.54,fill=False,edgecolor=P[1],lw=1.5))
            ax.annotate('',(x+.12,.04),(x+.12,-.08),arrowprops=dict(arrowstyle='->',color=P[1],lw=1.5))
        ax.annotate('Rotation Ω',(0,1.05),(0,1.43),ha='center',fontsize=9,arrowprops=dict(arrowstyle='->',color=P[0]))
        ax.text(0,0,'Solide',ha='center',va='center',fontsize=8)
        ax.text(0,.48,'Noyau externe\nliquide conducteur',ha='center',va='center',fontsize=8,color=P[1])
        ax.text(0,-.88,'Manteau',ha='center',fontsize=8)
        ax.text(0,-1.18,'Convection thermique et compositionnelle',ha='center',fontsize=8)
        ax.text(0,-1.40,'Mouvement → induction · rétroaction j×B',ha='center',fontsize=8)
        ax.set(xlim=(-1.4,1.4),ylim=(-1.55,1.6),aspect='equal',title='Géodynamo : coupe qualitative, rayons non à l’échelle');ax.axis('off');return True
    if key=='kerr':
        ax.plot(s['transverse'],s['intensity'],color=P[1],label='Profil auto-guidé')
        ax.plot(s['transverse'],s['linear_intensity'],color=P[0],ls='--',label='Gauss libre · même puissance')
        ax.set(xlabel='y/y₀',ylabel='Intensité relative',title='Diffraction comparée au profil Kerr localisé');ax.legend(fontsize=8);ax.grid(alpha=.2);return True
    return False


def export(dest,preview_dir=None):
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=True)
    if preview_dir:Path(preview_dir).mkdir(parents=True,exist_ok=True)
    for meta in FIGURES:
        key=meta['labs'][0]
        # Choisir une phase qui montre à la fois les champs transverses.
        overrides={'phase':.125,'mode':'stationnaire'} if key=='maxwell' else {'phase':.125} if key=='guide' else {'passes':'double'} if key=='faraday' else {}
        r=calculate(dict(lab=key,**overrides))
        fig,axes=plt.subplots(1,2,figsize=(12.4,5.7),gridspec_kw={'wspace':.36})
        fig.subplots_adjust(left=.08,right=.97,bottom=.26,top=.80)
        special=draw_special(axes[0],key,r)
        charts=r.get('charts',[])
        if not special:chart(axes[0],charts[0])
        index=1 if (not special or key in ['maxwell','meissner','rayonnement','kerr']) and len(charts)>1 else 0
        if key=='helmholtz':
            ax=axes[1]
            for i,d in enumerate([.5,1,1.5]):
                rr=calculate(dict(lab=key,spacing=d))
                c=rr['charts'][0];ss=c['series'][0]
                values=np.array(ss['y']);center=values[len(values)//2]
                ax.plot(ss['x'],values/(center or 1),label=f'd/R={d:g}',color=P[i])
            ax.set(xlabel=c['x_label'],ylabel='Baxis / B(0)',title='Écarter les bobines change la courbure');ax.legend(fontsize=8);ax.grid(alpha=.2)
        elif key=='interfaces':
            ax=axes[0];ax.clear();ax.axvline(0,color=P[0],lw=2);ax.axhline(0,color='#c8b7d1',ls=':')
            a=np.radians(r['scene']['angle']);b=np.radians(r['scene']['theta_t'])
            for start,end,color in [((-np.cos(a),-np.sin(a)),(0,0),P[2]),((0,0),(-np.cos(a),np.sin(a)),P[1]),((0,0),(np.cos(b),np.sin(b)),P[0])]:
                ax.annotate('',end,start,arrowprops=dict(arrowstyle='->',color=color,lw=2.5))
            ax.text(-1.1,.9,f"R={r['scene']['R']:.4f}",color=P[1]);ax.text(.2,.9,f"T={r['scene']['T']:.4f}",color=P[0]);ax.text(.5,-.12,'+z → normale',fontsize=8)
            ax.set(xlim=(-1.2,1.2),ylim=(-1.1,1.1),aspect='equal',title='Interface TE · rayons et fractions de flux');ax.axis('off')
            angle=np.linspace(0,89,180)
            for i,pol in enumerate(['TE','TM']):
                vals=[calculate(dict(lab=key,angle=float(a),polarization=pol))['scene']['R'] for a in angle]
                axes[1].plot(angle,vals,label=pol,color=P[i])
            axes[1].axvline(np.degrees(np.arctan(1.5)),ls=':',color=P[2],label='Brewster TM')
            axes[1].set(xlabel='Angle incident (°)',ylabel='Flux réfléchi / incident',title='Même interface, deux polarisations');axes[1].legend(fontsize=8);axes[1].grid(alpha=.2)
        elif key=='peau':chart(axes[1],calculate(dict(lab='peau',mode='step'))['charts'][0])
        else:
            chart(axes[1],charts[index])
            if key=='dynamo':axes[1].set_title('Croissance du mode local α² prescrit')
            if key=='biotsavart':
                z=np.linspace(1.5,6,100);radius=r['params']['R'];I=r['params']['I']
                B=1.25663706127e-6*I/(2*radius*z**3)*1e6
                axes[1].plot(z,B,ls='--',color=P[2],label='Limite dipolaire, |z|≥1,5R')
                axes[1].plot(-z,B,ls='--',color=P[2]);axes[1].legend(fontsize=8)
        for ax in axes:ax.set_title(textwrap.fill(ax.get_title(),width=48),fontsize=10)
        fig.suptitle(meta['title'],x=.07,ha='left',fontsize=17,fontweight='bold')
        fig.text(.07,.89,'ÉLECTROMAGNÉTISME · CPGE SUP / SPÉ · CHAMPS & MATIÈRE',color='#75687d',fontsize=9)
        fig.text(.07,.11,textwrap.fill(meta['caption'],width=155),fontsize=9,linespacing=1.5,va='top')
        fig.savefig(dest/meta['file'],metadata={'Date':None,'Title':meta['title'],'Description':meta['caption']})
        if preview_dir:fig.savefig(Path(preview_dir)/(key+'.png'),dpi=90)
        plt.close(fig)
    (dest/'catalogue.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    return dest


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description='Régénérer les 24 figures scientifiques')
    parser.add_argument('--preview-dir')
    args=parser.parse_args()
    print(export(Path(__file__).resolve().parent/'illustrations',args.preview_dir))
