"""Galerie scientifique vectorielle : géométrie, hypothèses et calculs.

Les figures sont originales et autonomes. Aucune image du recueil n'est copiée.
Les modèles analytiques et les intégrations numériques sont nommés dans leurs
légendes. ``export(dest)`` écrit les SVG et retourne le dossier de destination.
"""
from pathlib import Path
import json
import math
import os
import tempfile
import textwrap

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'cpge-fluides-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np

P = dict(ink='#163b46', blue='#317fa7', teal='#16827e', gold='#ce9b36', rose='#bc6677',
         violet='#7863a3', pale='#e8f3f2', grey='#6a7f85')
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10, 'text.color':P['ink'],
    'axes.labelcolor':P['ink'], 'axes.edgecolor':'#b0bfc0', 'axes.facecolor':'#fcfdfa',
    'axes.spines.top':False, 'axes.spines.right':False, 'xtick.color':P['grey'],
    'ytick.color':P['grey'], 'figure.facecolor':'white', 'svg.fonttype':'none',
    'svg.hashsalt':'cpge-mecanique-fluides', 'axes.formatter.use_mathtext':True})

FIGURES = [
    dict(file='cinematique.svg', title='Suivre une particule ou figer le champ ?', labs=['cinematique'],
         caption='Champ instationnaire v=(1 ; 0,45 sin t), dans des unités de référence : une trajectoire intègre le champ aux instants successifs, une ligne de courant fige t. Le second panneau décompose un gradient linéaire en déformation et rotation.'),
    dict(file='newtonien.svg', title='Déformation, contraintes et dissipation', labs=['newtonien'],
         caption='Pour v=(εx+γ̇y ; −εy), la partie symétrique D commande τ=2ηD, tandis que la rotation rigide ne dissipe pas. Le coefficient de contrainte est η en Pa·s ; ν=η/ρ est en m²/s.'),
    dict(file='couette_poiseuille.svg', title='Couette et Poiseuille : les conditions aux limites décident', labs=['couette','poiseuille'],
         caption='Entre plaques, translation des parois et gradient de pression se superposent. Dans un tube circulaire immobile, la parabole donne ū=u_max/2 et Q=πR⁴G/(8η). G=−d(p+ρgz)/dx fixe le sens du débit.'),
    dict(file='diffusion.svg', title='Une paroi, deux parois : deux problèmes de diffusion', labs=['diffusion'],
         caption='Demi-espace : u/U=erfc[y/(2√(νt))]. Canal de hauteur h : la série de Fourier satisfait u(0,t)=U et u(h,t)=0, puis tend vers Couette. La couche δ=2√(νt) ne croît pas linéairement avec t.'),
    dict(file='blasius.svg', title='Blasius : une couche limite qui s’épaissit en √x', labs=['blasius'],
         caption='Intégration numérique par tir de f‴+ff″/2=0, f(0)=f′(0)=0, f′(∞)=1. La variable ζ=y√(U∞/νx) rassemble les profils et f″(0)≈0,332057 ; δ99≈4,91√(νx/U∞).'),
    dict(file='bernoulli.svg', title='Venturi : accélération et bilan de charge', labs=['bernoulli'],
         caption='Exemple horizontal : Q=0,1 L/s, S1=4 cm² et S2=1 cm². Le débit conservé impose v2=4v1 et la pression diminue de 468,75 Pa pour l’eau. Bernoulli est un bilan sous hypothèses, avec pertes et machines explicitement séparées.'),
    dict(file='sphere.svg', title='Sphère lente : champ de Stokes et vitesse limite', labs=['sphere'],
         caption='Champ exact de Stokes extérieur à une sphère fixe, Re≪1 et adhérence à sa surface. La chute avec poussée d’Archimède et traînée 6πηRu donne v/v∞=1−e^(−t/τ), τ=m/(6πηR) ; l’accélération initiale n’est pas g dans un fluide.'),
    dict(file='vortex_magnus.svg', title='Rotation locale, circulation et portance', labs=['vortex','magnus'],
         caption='Vortex de Rankine : rotation solide au cœur et vitesse en 1/r au dehors ; l’absence de rotation locale extérieure n’annule pas la circulation. Le cylindre potentiel utilise une circulation Γ donnée. Pour Γ positive antihoraire et U∞ vers +x, Fy′=−ρU∞Γ.'),
    dict(file='houle.svg', title='Houle : phase, groupe et orbites de particules', labs=['houle'],
         caption='Dispersion gravito-capillaire ω²=(gk+γk³/ρ)tanh(kh). Les vitesses ω/k et dω/dk diffèrent hors du régime non dispersif. Les orbites linéarisées deviennent elliptiques en profondeur finie ; elles s’aplatissent au fond imperméable.'),
    dict(file='acoustique.svg', title='Interface acoustique : amplitudes et énergie', labs=['acoustique'],
         caption='Exemple idéal Z2/Z1=4 : r_p=3/5, t_p=8/5, mais R=9/25 et T=16/25. Pression et vitesse normale sont continues ; la vitesse réfléchie porte le signe opposé à la pression réfléchie.'),
    dict(file='conduit.svg', title='Guide sonore : mode transverse et coupure', labs=['conduit'],
         caption='Parois rigides : ∂p/∂n=0, modes cos(mπx/a)cos(nπy/b). Au-dessus de la coupure, vφ=c/√(1−fc²/f²) et vg=c√(1−fc²/f²). Le mode uniforme (0,0) n’a pas de coupure ; sous coupure, le nombre d’onde axial est imaginaire.'),
    dict(file='diffraction.svg', title='Diffraction et stroboscope : mesurer sans surinterpréter', labs=['diffraction'],
         caption='Fente idéale : I/I0=sinc²(πa sin θ/λ). Si λ>a, le premier zéro sin θ=λ/a n’existe pas dans le domaine propagatif. À fréquence d’échantillonnage donnée, des oscillations différentes produisent les mêmes points : une image fixe ne détermine pas seule la fréquence.'),
    dict(file='thermo.svg', title='Son et échanges thermiques : comparer les échelles', labs=['thermo'],
         caption='Gaz parfait : cT=√(RT/M), cS=√(γRT/M). La diffusion thermique sur une période donne δth=√(2Dth/ω) ; comparer δth à une dimension du conduit et à 1/k aide à choisir une hypothèse. Une longueur de diffusion ne démontre pas une instabilité thermoacoustique.'),
    dict(file='mhd.svg', title='Hartmann : le champ freine et dissipe', labs=['mhd'],
         caption='Canal y∈[−h,h], écoulement +x, champ +y et circuit transverse fermé Ez=0 : jz=σBu, fx=−σB²u. Ha=Bh√(σ/η). Le profil cosh satisfait l’adhérence et retrouve Poiseuille lorsque B→0 ; la puissance motrice se partage entre viscosité et effet Joule.'),
    dict(file='navier.svg', title='Taylor–Green : un bilan contrôlé, une question générale distincte', labs=['navier'],
         caption='Solution périodique 2D v=A(t)(sin kx cos ky ; −cos kx sin ky), A=Ue^(−2νk²t). L’énergie moyenne E=ρA²/4 décroît par dissipation. Cette solution exacte et les contrôles numériques ne constituent pas une preuve de régularité du problème général 3D.'),
    dict(file='hydrostatique.svg', title='Deux équilibres : rotation et atmosphère', labs=['hydrostatique'],
         caption='Récipient en rotation solide : z_s=z_c+Ω²r²/(2g), avec z_c fixé par le volume. L’atmosphère isotherme et la colonne isentropique donnent deux lois différentes ; la seconde est un modèle idéal jusqu’à l’annulation de sa température.'),
]


def finite_couette(s, tau, terms=160):
    """u/U à distance s=y/h : paroi inférieure mise en mouvement."""
    s=np.asarray(s,dtype=float)
    if tau<=0:raise ValueError('Le développement requiert t>0.')
    n=np.arange(1,terms+1,dtype=float)[:,None]
    return 1-s-2/math.pi*np.sum(np.sin(n*math.pi*s[None,:])/n*np.exp(-n*n*math.pi**2*tau),axis=0)


def blasius_profile(max_eta=10, steps=500):
    """Tir de l'EDO : RK4, puis dichotomie sur f″(0)."""
    z=np.linspace(0,max_eta,steps+1);h=z[1]-z[0]
    def integrate(a):
        out=np.empty((steps+1,3));out[0]=(0,0,a)
        def rhs(v):return np.array([v[1],v[2],-.5*v[0]*v[2]])
        for i in range(steps):
            v=out[i];k1=rhs(v);k2=rhs(v+h*k1/2);k3=rhs(v+h*k2/2);k4=rhs(v+h*k3)
            out[i+1]=v+h*(k1+2*k2+2*k3+k4)/6
        return out
    low,high=.28,.38
    for _ in range(38):
        middle=(low+high)/2
        if integrate(middle)[-1,1]>1:high=middle
        else:low=middle
    return z,integrate((low+high)/2)


def wave_dispersion(k,h=.5,g=9.81,gamma=.072,rho=1000):
    k=np.asarray(k,dtype=float);a=gamma/rho;q=np.tanh(k*h)
    omega=np.sqrt((g*k+a*k**3)*q)
    derivative=(g+3*a*k*k)*q+(g*k+a*k**3)*h*(1-q*q)
    return omega,omega/k,derivative/(2*omega)


def hartmann_profile(s,ha):
    """u / (Gh²/2η) ; limite continue de Poiseuille à Ha=0."""
    s=np.asarray(s,dtype=float)
    if abs(ha)<1e-4:return 1-s*s
    return 2/ha**2*(1-np.cosh(ha*s)/np.cosh(ha))


def taylor_green(x,y,t=0,nu=.04,k=1,u=1):
    a=u*np.exp(-2*nu*k*k*t)
    vx=a*np.sin(k*x)*np.cos(k*y);vy=-a*np.cos(k*x)*np.sin(k*y)
    pressure=a*a/4*(np.cos(2*k*x)+np.cos(2*k*y))
    return vx,vy,pressure


def _axes(ax,title,xlabel='',ylabel='',equal=False):
    ax.set(title=title,xlabel=xlabel,ylabel=ylabel)
    ax.title.set_fontsize(11);ax.grid(alpha=.17,lw=.6)
    if equal:ax.set_aspect('equal',adjustable='box')


def _legend(ax):ax.legend(fontsize=8.5,framealpha=.93,edgecolor='#dce7e4',loc='best')


def _cinematique(axs):
    ax,bx=axs;t=np.linspace(0,6,300);a=.45;t0=1.4
    ax.plot(t,a*(1-np.cos(t)),color=P['blue'],lw=2,label='Trajectoire x=t, y=0,45(1−cos t)')
    for offset in (-.6,-.15,.3):ax.plot(t,offset+a*np.sin(t0)*t,color=P['teal'],alpha=.7,lw=1,label='Lignes de courant à t=1,4' if offset==-.6 else None)
    ax.scatter([t0],[a*(1-np.cos(t0))],color=P['gold'],s=65,zorder=4)
    ax.quiver([t0],[a*(1-np.cos(t0))],[1],[a*np.sin(t0)],angles='xy',scale_units='xy',scale=1.6,color=P['ink'])
    ax.set_ylim(-.7,1.9);_axes(ax,'Une ligne instantanée ne suit pas toute l’histoire','x / Lréf','y / Lréf');_legend(ax)
    theta=np.linspace(0,2*np.pi,160);c=np.array([np.cos(theta),np.sin(theta)])
    gradient=np.array([[.25,-.7],[.7,-.25]]);d=(gradient+gradient.T)/2;w=(gradient-gradient.T)/2
    bx.plot(*c,color=P['grey'],ls='--',label='Cercle initial')
    bx.plot(*((np.eye(2)+.7*d)@c),color=P['gold'],lw=2,label='I+Δt D : déformation')
    r=np.array([[np.cos(.49),-np.sin(.49)],[np.sin(.49),np.cos(.49)]])
    bx.plot(*(r@c),color=P['violet'],lw=1.4,label='exp(Δt W) : rotation')
    bx.quiver([0],[0],[np.cos(.49)],[np.sin(.49)],angles='xy',scale_units='xy',scale=1,color=P['violet'])
    bx.text(0,-1.55,'∇v = D + W ; Dᵀ=D, Wᵀ=−W',ha='center',fontsize=10)
    bx.set_ylim(-1.75,1.4);_axes(bx,'Déformer et tourner sont deux actions différentes','x / Lréf','y / Lréf',True);_legend(bx)


def _newtonien(axs):
    ax,bx=axs;xy=np.linspace(-1,1,9);x,y=np.meshgrid(xy,xy);strain=.25;shear=1
    vx=strain*x+shear*y;vy=-strain*y
    ax.quiver(x,y,vx,vy,color=P['blue'],angles='xy',scale_units='xy',scale=4)
    ax.add_patch(Rectangle((-.42,-.42),.84,.84,fill=False,ec=P['gold'],lw=2))
    ax.annotate('traction τ·n',xy=(.95,.45),xytext=(.42,.1),arrowprops=dict(arrowstyle='->',color=P['rose']),color=P['rose'])
    ax.text(-1,-1.36,'D = [[ε, γ̇/2], [γ̇/2, −ε]] ; τ = 2ηD',fontsize=10)
    ax.set_ylim(-1.55,1.15);_axes(ax,'Le gradient de vitesse fixe les contraintes','x / Lréf','y / Lréf',True)
    rates=np.linspace(-3,3,250)
    for eta,color in [(.1,P['teal']),(.5,P['blue']),(1.0,P['rose'])]:bx.plot(rates,eta*rates,lw=2,label=f'η={eta:g} Pa·s',color=color)
    bx.axhline(0,color=P['grey'],lw=.6);bx.axvline(0,color=P['grey'],lw=.6)
    _axes(bx,'Cisaillement simple : τxy=ηγ̇','Taux de cisaillement γ̇ (s⁻¹)','Contrainte τxy (Pa)');_legend(bx)
    bx.text(.03,.96,'Dissipation : τ:D = 2ηD:D ≥ 0',transform=bx.transAxes,va='top',fontsize=10)


def _couette_poiseuille(axs):
    ax,bx=axs;s=np.linspace(0,1,240)
    for beta,color in [(-3,P['rose']),(0,P['blue']),(3,P['teal'])]:ax.plot(s+beta*s*(1-s),s,lw=2,color=color,label=f'β=Gh²/(2ηU)={beta:g}')
    ax.axhline(0,color=P['ink'],lw=3);ax.axhline(1,color=P['ink'],lw=3)
    ax.annotate('U →',xy=(1.1,1),xytext=(.6,1.14),arrowprops=dict(arrowstyle='->',color=P['gold']),color=P['gold'])
    _axes(ax,'Entre plaques : u/U = s+βs(1−s)','Vitesse u/U','Distance s=y/h');_legend(ax)
    r=np.linspace(-1,1,240);profile=1-r*r
    bx.plot(profile,r,color=P['blue'],lw=2.2,label='u/u_max=1−(r/R)²')
    bx.fill_betweenx(r,0,profile,color=P['pale']);bx.axhline(-1,color=P['ink'],lw=3);bx.axhline(1,color=P['ink'],lw=3)
    bx.axvline(.5,color=P['rose'],ls='--',label='ū/u_max=1/2')
    bx.text(.06,.05,'u_max = GR²/(4η)\nQ = πR⁴G/(8η)',transform=bx.transAxes,fontsize=11)
    _axes(bx,'Tube circulaire : le débit intègre toute la section','Vitesse u/u_max','Position radiale signée r/R');_legend(bx)


def _diffusion(axs):
    ax,bx=axs;s=np.linspace(0,2,250)
    for tau,color in [(.015,P['violet']),(.06,P['blue']),(.24,P['teal']),(.8,P['gold'])]:
        curve=np.array([math.erfc(v/(2*math.sqrt(tau))) for v in s])
        ax.plot(curve,s,lw=2,color=color,label=f'νt/h²={tau:g}')
    _axes(ax,'Demi-espace : aucune seconde paroi','u/U','Distance y/h');_legend(ax)
    ax.text(.03,.96,'δ/h = 2√(νt/h²)',transform=ax.transAxes,va='top',fontsize=11)
    s=np.linspace(0,1,250)
    for tau,color in [(.015,P['violet']),(.06,P['blue']),(.24,P['teal']),(.8,P['gold'])]:bx.plot(finite_couette(s,tau),s,lw=2,color=color,label=f'νt/h²={tau:g}')
    bx.plot(1-s,s,color=P['ink'],ls='--',label='Couette permanent')
    bx.axhline(0,color=P['ink'],lw=3);bx.axhline(1,color=P['ink'],lw=3)
    _axes(bx,'Canal fini : adhérence aux deux parois','u/U','Distance y/h');_legend(bx)


def _blasius(axs):
    ax,bx=axs;z,sol=blasius_profile();f,fp,fpp=sol.T
    ax.plot(fp,z,lw=2,color=P['blue'],label='f′ : vitesse longitudinale')
    ax.plot(fpp,z,lw=1.5,color=P['rose'],label='f″ : gradient normalisé')
    ax.axvline(.99,color=P['grey'],ls='--',lw=.8);ax.set_ylim(0,8)
    _axes(ax,'Une EDO universelle pour les profils','Valeur adimensionnée','ζ=y√(U∞/(νx))');_legend(ax)
    ax.text(.05,.77,f'f″(0) = {fpp[0]:.6f}\nf′(10) = {fp[-1]:.6f}',transform=ax.transAxes,fontsize=11)
    x=np.linspace(.06,1,250);delta=4.91*np.sqrt(.0001*x)
    bx.fill_between(x,0,delta,color=P['pale']);bx.plot(x,delta,color=P['teal'],lw=2,label='δ99≈4,91√(νx/U∞)')
    for xx in (.12,.3,.6,.9):
        yy=np.linspace(0,.06,160);uu=np.interp(yy/np.sqrt(.0001*xx),z,fp)
        bx.plot(xx+.075*uu,yy,color=P['blue'],lw=1.2)
    bx.axhline(0,color=P['ink'],lw=3);bx.set_xlim(0,1.03);bx.set_ylim(0,.065)
    _axes(bx,'Plaque plane : U∞=1 m/s, ν=10⁻⁴ m²/s','Distance x (m)','Distance y (m)');_legend(bx)


def _bernoulli(axs):
    ax,bx=axs;x=np.linspace(0,5,250);half=.9-.65*np.exp(-(x-2.65)**2/.45)
    ax.fill_between(x,-half,half,color=P['pale']);ax.plot(x,half,color=P['ink'],lw=2);ax.plot(x,-half,color=P['ink'],lw=2)
    for yy in (-.65,-.3,0,.3,.65):ax.plot(x,yy*half/.9,color=P['teal'],lw=.9,alpha=.75)
    for xx,v in [(1,.25),(2.65,1)]:
        hh=float(np.interp(xx,x,half));ax.plot([xx,xx],[-hh,hh],color=P['gold'],ls='--')
        ax.annotate(f'v={v:g} m/s',xy=(xx+.32,0),xytext=(xx-.45,0),arrowprops=dict(arrowstyle='->',color=P['blue']),color=P['blue'],fontsize=9)
    ax.text(.9,1.15,'S1=4 cm²',ha='center');ax.text(2.65,1.15,'S2=1 cm²',ha='center')
    _axes(ax,'Venturi horizontal : Q=0,1 L/s','Coordonnée longitudinale (schéma)','Coordonnée transversale (schéma)');ax.set_ylim(-1.35,1.45)
    names=['Section 1','Section 2','Après pertes'];kin=np.array([.25**2,1,.25**2])/19.62;total=.35
    press=np.array([total,total,total-.025])-kin
    bx.bar(names,press,color=P['teal'],label='p/(ρg)')
    bx.bar(names,kin,bottom=press,color=P['gold'],label='v²/(2g)')
    bx.axhline(total,color=P['ink'],ls='--',lw=1,label='H1=H2 sans perte')
    _axes(bx,'Les hauteurs s’ajoutent ; une perte abaisse le total','','Hauteur de charge (m)');_legend(bx)
    bx.text(.03,.05,'p1−p2 = ρ(v2²−v1²)/2 = 468,75 Pa\nLa troisième colonne illustre une perte de 2,5 cm.',transform=bx.transAxes,fontsize=9)


def _sphere(axs):
    ax,bx=axs;x=np.linspace(-3,3,130);y=np.linspace(-2,2,110);xx,yy=np.meshgrid(x,y);r=np.hypot(xx,yy)
    rr=np.maximum(r,1);ct=xx/rr;st=yy/rr
    ur=ct*(1-1.5/rr+.5/rr**3);ut=-st*(1-.75/rr-.25/rr**3)
    vx=np.ma.masked_where(r<=1,ur*ct-ut*st);vy=np.ma.masked_where(r<=1,ur*st+ut*ct)
    ax.streamplot(x,y,vx,vy,color=P['blue'],density=1.15,linewidth=.8,arrowsize=.8)
    ax.add_patch(Circle((0,0),1,color=P['pale'],ec=P['ink'],lw=2));ax.text(0,0,'v=0\nadhérence',ha='center',va='center')
    ax.text(-2.85,1.78,'U∞ → ; Re=2ρRU∞/η ≪ 1',fontsize=10)
    _axes(ax,'Solution de Stokes : aucun glissement sur la sphère','x/R','y/R',True)
    t=np.linspace(0,5,200);v=1-np.exp(-t);distance=t-1+np.exp(-t)
    bx.plot(t,v,color=P['teal'],lw=2,label='Vitesse descendante v/v∞')
    bx.plot(t,distance,color=P['gold'],lw=2,label='Distance descendante s/(v∞τ)')
    bx.axhline(1,color=P['grey'],ls='--',lw=.8)
    _axes(bx,'Chute : m dv/dt = (ρb−ρf)Vg−6πηRv','Temps t/τ','Valeur adimensionnée');_legend(bx)
    bx.text(.03,.42,'v∞=2R²g(ρb−ρf)/(9η)\nτ=m/(6πηR)',transform=bx.transAxes,fontsize=10)


def _vortex_magnus(axs):
    ax,bx=axs;r=np.linspace(.015,4,280);v=np.where(r<1,r,1/r);p=np.where(r<1,r*r/2-1,-1/(2*r*r))
    ax.plot(r,v,color=P['blue'],lw=2,label='vθ/(ΩR)')
    ax.plot(r,p,color=P['rose'],lw=2,label='(p−p∞)/(ρΩ²R²)')
    ax.axvline(1,color=P['grey'],ls='--',label='Frontière du cœur r=R')
    ax.fill_betweenx([-1.1,1.1],0,1,color=P['pale'],alpha=.6,zorder=-2);ax.set_ylim(-1.15,1.18)
    _axes(ax,'Vortex de Rankine : circulation Γ=2πΩR²','Distance r/R','Valeur adimensionnée');_legend(ax)
    x=np.linspace(-3,3,150);y=np.linspace(-2.2,2.2,125);xx,yy=np.meshgrid(x,y);r=np.hypot(xx,yy);rr=np.maximum(r,1)
    ct=xx/rr;st=yy/rr;gamma=3*math.pi
    ur=(1-1/rr**2)*ct;ut=-(1+1/rr**2)*st+gamma/(2*math.pi*rr)
    vx=np.ma.masked_where(r<=1,ur*ct-ut*st);vy=np.ma.masked_where(r<=1,ur*st+ut*ct)
    bx.streamplot(x,y,vx,vy,density=1.25,color=P['teal'],linewidth=.8,arrowsize=.8)
    bx.add_patch(Circle((0,0),1,fc=P['pale'],ec=P['ink'],lw=2));bx.annotate('Fy′<0',xy=(0,-1.8),xytext=(0,-.2),arrowprops=dict(arrowstyle='->',lw=2,color=P['rose']),color=P['rose'],ha='center')
    bx.text(-2.85,1.96,'U∞→ ; Γ=3πU∞R, antihoraire',fontsize=10)
    _axes(bx,'Cylindre potentiel : Γ donnée, portance signée','x/R','y/R',True)


def _houle(axs):
    ax,bx=axs;k=np.geomspace(.03,4000,300);omega,phase,group=wave_dispersion(k)
    ax.loglog(k,phase,color=P['blue'],lw=2,label='vφ=ω/k')
    ax.loglog(k,group,color=P['gold'],lw=2,label='vg=dω/dk')
    ax.axvline(math.sqrt(1000*9.81/.072),color=P['grey'],ls='--',label='kℓc=1 ; ℓc=√(γ/(ρg))')
    _axes(ax,'Eau : h=0,5 m, γ=0,072 N/m','Nombre d’onde k (rad/m)','Vitesse (m/s)');_legend(ax)
    h=.15;wave=8;amplitude=.004;theta=np.linspace(0,2*np.pi,160)
    for depth,color in [(-.012,P['blue']),(-.06,P['teal']),(-.12,P['gold']),(-h,P['rose'])]:
        aa=amplitude*np.cosh(wave*(depth+h))/np.sinh(wave*h);bb=amplitude*np.sinh(wave*(depth+h))/np.sinh(wave*h)
        bx.plot(100*aa*np.cos(theta),100*(depth+bb*np.sin(theta)),color=color,lw=2,label=f'z0={100*depth:g} cm')
    bx.axhline(0,color=P['grey'],ls='--',lw=.8);bx.axhline(-15,color=P['ink'],lw=3)
    bx.text(.03,.97,'ξ0=4 mm ; k=8 rad/m ; h=15 cm',transform=bx.transAxes,va='top',fontsize=10)
    _axes(bx,'Orbites au premier ordre : le fond reste imperméable','Déplacement horizontal (cm)','Profondeur et déplacement vertical (cm)');_legend(bx)


def _acoustique(axs):
    ax,bx=axs;r=.6;tp=1.6;ratio=4;left=np.linspace(-2*np.pi,0,200);right=np.linspace(0,2*np.pi,200)
    ax.plot(left,(1+r)*np.cos(left),color=P['blue'],lw=2,label='p/p_inc')
    ax.plot(right,tp*np.cos(right/2),color=P['blue'],lw=2)
    ax.plot(left,(1-r)*np.cos(left),color=P['rose'],lw=1.8,label='Z1 v/p_inc')
    ax.plot(right,tp/ratio*np.cos(right/2),color=P['rose'],lw=1.8)
    ax.axvline(0,color=P['ink'],lw=2);ax.text(-4.5,1.85,'Milieu 1');ax.text(2,1.85,'Milieu 2 : Z2=4Z1')
    ax.set_ylim(-1.95,2.1);_axes(ax,'À l’interface, p et v normale sont continus','Coordonnée k1 x (c2=2c1)','Amplitude normalisée');_legend(ax)
    bx.bar(['r pression','t pression','R énergie','T énergie'],[r,tp,r*r,4*ratio/(1+ratio)**2],color=[P['blue'],P['teal'],P['rose'],P['gold']])
    bx.axhline(1,color=P['grey'],ls='--',lw=.8);bx.set_ylim(0,2)
    _axes(bx,'Une amplitude transmise >1 ne crée pas d’énergie','','Coefficient adimensionné')
    bx.text(.03,.96,'rp=(Z2−Z1)/(Z2+Z1)\nR=rp² ; T=4Z1Z2/(Z1+Z2)²\nR+T=1',transform=bx.transAxes,va='top',fontsize=10)


def _conduit(axs):
    ax,bx=axs;x=np.linspace(0,1,180);y=np.linspace(0,.6,130);xx,yy=np.meshgrid(x,y);p=np.cos(np.pi*xx)*np.cos(2*np.pi*yy/.6)
    cmap=ax.contourf(xx,yy,p,levels=np.linspace(-1,1,15),cmap='RdBu_r')
    ax.contour(xx,yy,p,levels=[0],colors=P['ink'],linewidths=.8)
    for edge in [0,1]:ax.axvline(edge,color=P['ink'],lw=3)
    for edge in [0,.6]:ax.axhline(edge,color=P['ink'],lw=3)
    _axes(ax,'Section du mode (m,n)=(1,2), parois rigides','x/a','y/a',True)
    ax.text(.02,-.22,'p⊥∝cos(πx/a) cos(2πy/b) ; b=0,6a',transform=ax.transAxes,fontsize=10)
    r=np.linspace(1.003,5,350);q=np.sqrt(1-1/r**2)
    bx.plot(r,1/q,color=P['blue'],lw=2,label='vφ/c')
    bx.plot(r,q,color=P['gold'],lw=2,label='vg/c')
    bx.axhline(1,color=P['grey'],ls='--');bx.set_ylim(0,4);bx.set_xlim(.6,5)
    bx.axvspan(.6,1,color=P['pale']);bx.text(.66,2.8,'Évanescent',rotation=90,fontsize=10)
    _axes(bx,'La coupure modifie le transport axial','Fréquence f/fc','Vitesse/c');_legend(bx)
    bx.text(.35,.93,'vφ vg=c² ; (0,0) : fc=0',transform=bx.transAxes,va='top',fontsize=10)


def _diffraction(axs):
    ax,bx=axs;theta=np.linspace(-np.pi/2,np.pi/2,700)
    for ratio,color in [(.5,P['rose']),(1,P['gold']),(4,P['blue'])]:ax.plot(np.degrees(theta),np.sinc(ratio*np.sin(theta))**2,color=color,lw=2,label=f'a/λ={ratio:g}')
    ax.axvline(math.degrees(math.asin(.25)),color=P['blue'],ls='--',lw=.8)
    _axes(ax,'Fente idéale : utiliser sin θ, pas θ à grand angle','Angle θ (degrés)','Intensité I/I0');_legend(ax)
    ax.text(.03,.08,'λ>a : pas de premier zéro propagatif',transform=ax.transAxes,fontsize=10)
    times=np.linspace(0,.12,900);sample=np.arange(0,.121,.02)
    bx.plot(times, np.cos(2*np.pi*75*times),color=P['blue'],lw=1.3,label='75 Hz')
    bx.plot(times,np.cos(2*np.pi*25*times),color=P['gold'],lw=1.8,label='25 Hz')
    bx.scatter(sample,np.cos(2*np.pi*75*sample),color=P['ink'],s=45,zorder=5,label='Éclairs : 50 Hz')
    _axes(bx,'Deux fréquences, les mêmes échantillons','Temps (s)','Signal normalisé');_legend(bx)


def _thermo(axs):
    ax,bx=axs;temperatures=np.linspace(230,400,230);c_t=np.sqrt(8.314462618*temperatures/.02897);c_s=np.sqrt(1.4)*c_t
    ax.plot(temperatures,c_t,color=P['gold'],lw=2,label='cT : isotherme')
    ax.plot(temperatures,c_s,color=P['blue'],lw=2,label='cS : isentropique')
    _axes(ax,'Gaz parfait : γ=1,4 ; M=28,97 g/mol','Température (K)','Célérité (m/s)');_legend(ax)
    frequency=np.geomspace(1,1e6,300);omega=2*np.pi*frequency;delta=np.sqrt(2*2.2e-5/omega)
    bx.loglog(frequency,1000*delta,color=P['rose'],lw=2,label='δth=√(2Dth/ω)')
    bx.loglog(frequency,1000*343/omega,color=P['teal'],lw=2,label='1/k≈cS/ω')
    bx.axhline(.5,color=P['gold'],ls='--',label='Dimension transverse : 0,5 mm')
    _axes(bx,'Dth=2,2×10⁻⁵ m²/s : quelle distance diffuse ?','Fréquence (Hz)','Longueur (mm)');_legend(bx)


def _mhd(axs):
    ax,bx=axs;s=np.linspace(-1,1,300)
    for ha,color in [(0,P['blue']),(1,P['teal']),(3,P['gold']),(8,P['rose'])]:ax.plot(hartmann_profile(s,ha),s,color=color,lw=2,label=f'Ha={ha}')
    ax.axhline(-1,color=P['ink'],lw=3);ax.axhline(1,color=P['ink'],lw=3)
    _axes(ax,'Même gradient G : le champ réduit le débit','u/(Gh²/2η)','Position y/h');_legend(ax)
    ha=np.linspace(0,10,150);visc=[];joule=[];pressure=[]
    for value in ha:
        u=hartmann_profile(s,value)
        du=-2*s if value<1e-4 else -2*np.sinh(value*s)/(value*np.cosh(value))
        integrate=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
        vv=float(integrate(du*du,s));jj=float(integrate(value*value*u*u,s));visc.append(vv);joule.append(jj)
        pressure.append(2*float(integrate(u,s)))
    visc=np.array(visc);joule=np.array(joule);pressure=np.array(pressure)
    bx.plot(ha,visc/pressure,color=P['blue'],lw=2,label='Part visqueuse / GQ')
    bx.plot(ha,joule/pressure,color=P['rose'],lw=2,label='Part Joule / GQ')
    bx.plot(ha,(visc+joule)/pressure,color=P['ink'],ls='--',lw=1,label='Bilan intégré : somme ≈1')
    _axes(bx,'Puissance de pression = viscosité + effet Joule','Nombre de Hartmann Ha','Fraction de puissance');_legend(bx)
    bx.text(.40,.25,'Hypothèse électrique : Ez=0\njz=σBu ; fx=−σB²u',transform=bx.transAxes,fontsize=10)


def _navier(axs):
    ax,bx=axs;x=np.linspace(0,2*np.pi,70);y=x.copy();xx,yy=np.meshgrid(x,y);vx,vy,pressure=taylor_green(xx,yy)
    vort=2*np.sin(xx)*np.sin(yy)
    ax.contourf(xx,yy,vort,levels=15,cmap='RdBu_r',alpha=.8)
    ax.quiver(xx[::5,::5],yy[::5,::5],vx[::5,::5],vy[::5,::5],color=P['ink'],angles='xy',scale_units='xy',scale=2.7,width=.004)
    _axes(ax,'Taylor–Green périodique : quatre tourbillons','kx','ky',True)
    ax.text(.02,-.2,'Couleur : ωz/(kU) ; flèches : vitesse à t=0',transform=ax.transAxes,fontsize=10)
    t=np.linspace(0,12,250);energy=np.exp(-4*.04*t)
    bx.plot(t,energy,color=P['blue'],lw=2,label='E(t)/E(0)=e^(−4νk²t)')
    bx.plot(t,1-energy,color=P['rose'],lw=2,label='Dissipation cumulée / E(0)')
    bx.axhline(1,color=P['grey'],ls='--',lw=.8)
    _axes(bx,'Le bilan ferme : énergie restante + énergie dissipée','Temps (s), ν=0,04 m²/s, k=1 m⁻¹','Fraction de l’énergie initiale');_legend(bx)
    bx.text(.03,.44,'Solution exacte 2D, domaine périodique.\nCe contrôle ne prouve pas le résultat général 3D.',transform=bx.transAxes,fontsize=9.5)


def _hydrostatique(axs):
    ax,bx=axs;r=np.linspace(-.18,.18,200);omega=8;g=9.81;mean=.18;radius=.18;zc=mean-omega**2*radius**2/(4*g);surface=zc+omega**2*r*r/(2*g)
    ax.fill_between(r,0,surface,color=P['pale']);ax.plot(r,surface,color=P['blue'],lw=2,label='Surface libre en rotation')
    ax.axhline(mean,color=P['gold'],ls='--',label='Hauteur moyenne conservée')
    ax.axvline(-radius,color=P['ink'],lw=3);ax.axvline(radius,color=P['ink'],lw=3);ax.axhline(0,color=P['ink'],lw=3)
    ax.set_ylim(-.015,.3);_axes(ax,'Volume constant : zc=h̄−Ω²R²/(4g)','Coordonnée radiale signée (m)','Hauteur z (m)');_legend(ax)
    s=np.linspace(0,3.4,280);isotherm=np.exp(-s);adiab=np.maximum(1-(1.4-1)/1.4*s,0)**(1.4/(1.4-1))
    bx.plot(isotherm,s,color=P['blue'],lw=2,label='Isotherme : e^(−z/H0)')
    bx.plot(adiab,s,color=P['rose'],lw=2,label='Isentropique : (1−2z/(7H0))^(7/2)')
    _axes(bx,'Deux lois d’équilibre sous des hypothèses différentes','Pression p/p0','Altitude z/H0 ; H0=RT0/(Mg)');_legend(bx)


BUILDERS = dict(cinematique=_cinematique,newtonien=_newtonien,couette_poiseuille=_couette_poiseuille,
    diffusion=_diffusion,blasius=_blasius,bernoulli=_bernoulli,sphere=_sphere,vortex_magnus=_vortex_magnus,
    houle=_houle,acoustique=_acoustique,conduit=_conduit,diffraction=_diffraction,thermo=_thermo,
    mhd=_mhd,navier=_navier,hydrostatique=_hydrostatique)


def export(destination, preview=None, names=None):
    """Exporter tous les SVG, ou une sélection utile pour la vérification."""
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    if preview is not None:preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    chosen=set(names) if names is not None else set(BUILDERS)
    for config in FIGURES:
        key=Path(config['file']).stem
        if key not in chosen:continue
        fig,axs=plt.subplots(1,2,figsize=(13.8,6.6))
        BUILDERS[key](axs)
        for axis in axs:
            for annotation in axis.texts:
                annotation.set_bbox(dict(facecolor='white',edgecolor='none',alpha=.88,pad=1.7))
        fig.suptitle(config['title'],x=.055,y=.96,ha='left',fontsize=17,fontweight='bold',color=P['ink'])
        caption='\n'.join(textwrap.wrap(config['caption'],150))
        fig.text(.055,.045,caption,fontsize=9.2,color=P['grey'],va='bottom',linespacing=1.4)
        fig.subplots_adjust(left=.075,right=.965,bottom=.235,top=.83,wspace=.3)
        fig.savefig(destination/config['file'],format='svg',metadata={'Title':config['title'],
            'Description':config['caption']+' Laboratoires : '+', '.join(config['labs']), 'Date':None})
        if preview is not None:fig.savefig(preview/(key+'.png'),dpi=125)
        plt.close(fig)
    if names is None:
        lines=['# Galerie scientifique : mécanique des fluides et acoustique','',
               'Seize illustrations vectorielles originales couvrent les dix-huit TP. Les axes, conventions et hypothèses sont indiqués dans chaque figure. Les schémas ne reprennent aucune image du PDF privé.','']
        for config in FIGURES:
            lines += [f"## {config['title']}",'',f"![{config['title']}]({config['file']})",'',config['caption'],'',
                      'Laboratoires : '+', '.join('`'+lab+'`' for lab in config['labs'])+'.','']
        (destination/'README.md').write_text('\n'.join(lines),encoding='utf-8',newline='\n')
        (destination/'catalogue.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2)+'\n',
                                                encoding='utf-8',newline='\n')
    return destination


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description='Exporter la galerie scientifique en SVG.')
    parser.add_argument('--preview',type=Path)
    parser.add_argument('--destination',type=Path,default=Path(__file__).with_name('illustrations'))
    options=parser.parse_args();print(export(options.destination,options.preview))
