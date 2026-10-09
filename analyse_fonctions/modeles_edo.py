"""EDO : formules exactes, quadratures de Gauss et vérifications indépendantes."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, result, integrate

_GX, _GW = np.polynomial.legendre.leggauss(64)

def rk4(f, y0, end, steps=1600):
    t = np.linspace(0, float(end), int(steps)+1)
    y = np.empty((len(t),)+np.asarray(y0, dtype=float).shape)
    y[0] = y0
    h=t[1]-t[0]
    for j in range(steps):
        k1=np.asarray(f(t[j], y[j])); k2=np.asarray(f(t[j]+h/2, y[j]+h*k1/2))
        k3=np.asarray(f(t[j]+h/2, y[j]+h*k2/2)); k4=np.asarray(f(t[j+1], y[j]+h*k3))
        y[j+1]=y[j]+h*(k1+2*k2+2*k3+k4)/6
    return t,y

def gauss_to(x, function):
    """Intégrales orientées de 0 à chacune des abscisses x."""
    x=np.asarray(x,dtype=float)
    s=x[:,None]*(1+_GX[None,:])/2
    return x/2*np.sum(function(s)*_GW[None,:],axis=1)

def scene_field(title, f, bounds, paths, description='', phase=False):
    xmin,xmax,ymin,ymax=bounds
    arrows=[]
    sx=(xmax-xmin)/14; sy=(ymax-ymin)/12
    for x in np.linspace(xmin+sx/2,xmax-sx/2,14):
        for y in np.linspace(ymin+sy/2,ymax-sy/2,12):
            vector=f(float(x),float(y))
            if vector is None: continue
            dx,dy=vector if phase else (1,vector)
            norm=math.hypot(dx/sx,dy/sy)
            if norm>0 and math.isfinite(norm):
                arrows.append(dict(x=x,y=y,dx=.65*dx/norm,dy=.65*dy/norm))
    return dict(kind='phase' if phase else 'field',title=title,description=description,
                bounds=list(bounds),x_label='y' if phase else 'x ou t',y_label='y′' if phase else 'y',
                arrows=arrows,paths=[dict(label=label,x=x,y=y) for label,x,y in paths])

def scalar_bounds(t,*values):
    lo=min(float(np.min(v)) for v in values); hi=max(float(np.max(v)) for v in values)
    margin=max((hi-lo)*.12,.2)
    return [float(t[0]),float(t[-1]),lo-margin,hi+margin]

def euler_solution(y0,end,n):
    t=np.linspace(0,end,n+1); y=np.empty(n+1); y[0]=y0; h=end/n
    for j in range(n): y[j+1]=y[j]+h*math.cos(t[j])*(y[j]+1)
    return t,y

def euler_rk4(p):
    T=float(p['T']); n=int(p['N']); y0=float(p['y0'])
    f=lambda x,y: np.cos(x)*(y+1)
    t,eu=euler_solution(y0,T,n); _,rk=rk4(f,y0,T,n)
    exact=(y0+1)*np.exp(np.sin(t))-1
    ns=np.array([20,40,80,160,320]); h=T/ns
    euler_errors=[]; rk_errors=[]
    for count in ns:
        tt,yy=euler_solution(y0,T,int(count)); _,rr=rk4(f,y0,T,int(count))
        ref=(y0+1)*np.exp(np.sin(tt))-1
        euler_errors.append(float(np.max(np.abs(yy-ref)))); rk_errors.append(max(float(np.max(np.abs(rr-ref))),1e-16))
    order_e=math.log(euler_errors[-2]/euler_errors[-1],2)
    order_r=math.log(rk_errors[-2]/rk_errors[-1],2)
    return result([metric('Pas h',T/n),metric('Erreur maximale Euler',float(np.max(abs(eu-exact)))),metric('Erreur maximale RK4',float(np.max(abs(rk-exact)))),metric('Ordre mesuré Euler',order_e),metric('Ordre mesuré RK4',order_r)],
        [chart('Même équation, mêmes données initiales','x (rad)','y',series('Solution exacte',t,exact),series('Euler',t,eu),series('RK4',t,rk)),
         chart('Erreurs dans le temps','x','Erreur absolue',series('Euler',t,np.abs(eu-exact)),series('RK4',t,np.abs(rk-exact))),
         chart('Mesurer un ordre : erreur en fonction du pas','Pas h','Erreur maximale',series('Euler, ordre 1',h,euler_errors),series('RK4, ordre 4',h,rk_errors),x_scale='log',y_scale='log')],
        scene_field('Le champ indique la pente de la solution',f,scalar_bounds(t,exact,eu),[('Exacte',t,exact),('Euler',t,eu),('RK4',t,rk)],'Chaque segment représente la direction (1, cos(x)(y+1)).'),
        ['Poser z=y+1. L’équation devient z′=cos(x)z ; z(x)=(y₀+1)e^{sin x}. Aucune division par z n’est nécessaire pour inclure la solution y=−1.',
         'Euler emploie la pente au début du pas. RK4 combine quatre évaluations de pente ; les deux calculs partent exactement de y₀.',
         'Comparer aux mêmes abscisses la solution exacte et le calcul. L’erreur affichée est le maximum de |y_num−y_exact| sur les nœuds.',
         'Si E(h)≈Chᵖ, log₂(E(h)/E(h/2))≈p. Le graphique et les ordres utilisent cinq maillages indépendants ; ce n’est pas une droite imposée.'],
        ['L’équation est linéaire à coefficients continus sur ℝ ; sa solution exacte est globale.', 'Les ordres 1 et 4 sont asymptotiques pour un intervalle fixé. Un pas très grossier peut être hors de cette zone.', 'Les abscisses des trigonométriques sont en radians ; toutes les autres variables de ce modèle sont sans dimension.'])

def integrating_solution(t,a,b,force,omega,y0):
    t=np.asarray(t); A=a*t+b*t*t/2
    s=t[:,None]*(1+_GX[None,:])/2
    kernel=np.exp(-(A[:,None]-(a*s+b*s*s/2)))
    return y0*np.exp(-A)+t/2*np.sum(kernel*force*np.cos(omega*s)*_GW,axis=1)

def facteur_integrant(p):
    a,b,F,w,y0,T=(float(p[k]) for k in ('a','b','F','omega','y0','T'))
    t=np.linspace(0,T,501); y=integrating_solution(t,a,b,F,w,y0); A=a*t+b*t*t/2
    tr,yr=rk4(lambda x,z:F*np.cos(w*x)-(a+b*x)*z,y0,T,1200)
    ref=integrating_solution(tr,a,b,F,w,y0)
    difference=np.exp(-A)
    return result([metric('Facteur intégrant à T',math.exp(float(A[-1]))),metric('Écart final entre données initiales séparées de 1',float(difference[-1])),metric('Écart quadrature / RK4',float(np.max(abs(yr-ref)))),metric('Valeur y(T)',float(y[-1]))],
        [chart('Solution construite par intégration','x','y',series('Variation des constantes',t,y),series('RK4 indépendant',tr[::3],yr[::3])),chart('Le même forçage, deux données initiales','x','y',series('y(0)=y₀',t,y),series('y(0)=y₀+1',t,y+difference)),chart('Équation et facteur intégrant','x','Valeur',series('a+bx',t,a+b*t),series('Forçage F cos(ωx)',t,F*np.cos(w*t)),series('Écart e^{−A(x)}',t,difference))],
        scene_field('Pentes d’une équation linéaire à coefficient variable',lambda x,z:F*math.cos(w*x)-(a+b*x)*z,scalar_bounds(t,y,y+difference),[('y₀',t,y),('y₀+1',t,y+difference)],'Les directions donnent y′=F cos(ωx)−(a+bx)y. Les deux trajectoires possèdent le même forçage et un écart initial de 1.'),
        ['Prendre A(x)=ax+bx²/2 et multiplier par eᴬ : (eᴬy)′=eᴬFcos(ωx). Le signe de A découle de cette dérivation.', 'Intégrer de 0 à x : y=e^{−A(x)}y₀+∫₀ˣe^{−(A(x)−A(s))}Fcos(ωs)ds. Le noyau est calculé directement, sans multiplier deux exponentielles énormes.', 'La différence entre deux solutions ayant le même second membre satisfait d′+(a+bx)d=0 ; d=e^{−A} pour un écart initial 1.', 'La quadrature de Gauss et RK4 suivent des constructions différentes ; leur accord vérifie le calcul et non les hypothèses du modèle.'],
        ['a,b≥0 dans les réglages : la différence des solutions ne croît pas pour x≥0.', 'Le second membre et le coefficient sont continus : il existe une solution unique sur tout ℝ.', 'Les paramètres et variables sont ici sans dimension ; l’interprétation thermique ou électrique demande d’ajouter les unités du modèle.'])

def cauchy_lipschitz(p):
    delay,lam,eps,T=(float(p[k]) for k in ('delay','lam','epsilon','T'))
    t=np.linspace(0,T,501); waits=[0,delay,T]; curves=[np.maximum(t-tau,0)**2 for tau in waits]
    unique=eps*np.exp(lam*t); quotients=np.geomspace(1e-6,.1,100)
    return result([metric('Solutions montrées pour la même donnée y(0)=0',3),metric('Pente de la branche au départ',0),metric('Rapport 2√ε / ε',2/math.sqrt(eps)),metric('Amplification linéaire e^{λT}',math.exp(lam*T))],
        [chart('Non-unicité : on choisit un instant de départ','t','y',*[series(f'Départ τ={tau:g}',t,y) for tau,y in zip(waits,curves)]),chart('Linéaire : la donnée nulle reste nulle','t','y',series('y(0)=0 : unique solution',t,np.zeros_like(t)),series('y(0)=ε',t,unique)),chart('Tester la condition de Lipschitz au voisinage de 0','ε','|f(ε)−f(0)|/ε',series('2/√ε : non borné',quotients,2/np.sqrt(quotients)),series('|λ| : borné',quotients,np.full_like(quotients,abs(lam))),x_scale='log',y_scale='log')],
        scene_field('Trois trajectoires passent par (0,0)',lambda x,y:2*math.sqrt(max(y,0)),[0,T,-.3,T*T*1.05],[('Départ immédiat',t,curves[0]),('Départ choisi',t,curves[1]),('Repos',t,curves[2])],'Les directions correspondent à y′=2√max(y,0). La pente nulle permet ici plusieurs instants de départ à partir d’une donnée identique.'),
        ['Pour tout τ≥0, yτ(t)=0 si t≤τ et yτ(t)=(t−τ)² si t≥τ. Les deux valeurs et les deux dérivées se raccordent à τ.', 'Chaque yτ vérifie y′=2√max(y,0) et y(0)=0. Le second membre est continu ; cela ne suffit donc pas à garantir l’unicité.', 'Au voisinage de 0, [f(ε)−f(0)]/ε=2/√ε n’est pas borné : f n’est pas localement lipschitzienne en y.', 'Pour y′=λy, la différence de deux solutions est Ce^{λt}. Une même donnée initiale impose C=0 : l’unicité est démontrée directement.'],
        ['Le théorème général de Cauchy–Lipschitz est un prolongement ; existence et unicité des EDO linéaires sont les points d’appui CPGE.', 'La non-unicité est établie par des solutions exactes ; un seul tracé numérique ne pourrait pas la prouver.', 'Une propriété suffisante n’est pas nécessaire : l’échec d’une hypothèse ne signifie pas que toute équation de ce type manque d’unicité.'])

def explosion_logistique(p):
    a,y0,r,K,frac=(float(p[k]) for k in ('a','y0','r','K','fraction'))
    star=1/(a*y0); end=frac*star; t=np.linspace(0,end,501)
    explosive=y0/(1-a*y0*t); logistic=K/(1+(K/y0-1)*np.exp(-r*t))
    _,num=rk4(lambda x,y:a*y*y,y0,end,2000)
    tref=np.linspace(0,end,2001); exact=y0/(1-a*y0*tref)
    yy=np.linspace(0,max(K*1.4,y0*1.1),301)
    return result([metric('Temps d’explosion t*',star),metric('Distance finale à l’explosion',star-end),metric('Niveau logistique stable K',K),metric('Croissance quadratique y(T)',float(explosive[-1])),metric('Erreur relative maximale RK4',float(np.max(abs(num-exact)/exact)))],
        [chart('Explosion et saturation, même donnée initiale','t','Valeur',series('y′=ay²',t,explosive),series('z′=rz(1−z/K)',t,logistic),series('Équilibre K',t,np.full_like(t,K))),chart('Portrait de la loi logistique','z','z′',series('r z(1−z/K)',yy,r*yy*(1-yy/K)),series('Pente nulle',yy,np.zeros_like(yy))),chart('La quantité 1/y révèle le temps maximal','t','1/y',series('1/y₀−at',t,1/explosive))],
        scene_field('La croissance quadratique avant le temps d’explosion',lambda t,y:a*y*y,scalar_bounds(t,explosive),[('Solution maximale à droite',t,explosive)],'Le graphique s’arrête strictement avant t*. Il ne relie pas artificiellement les branches à travers une asymptote.'),
        ['Pour y₀>0, intégrer (1/y)′=−a donne y=y₀/(1−ay₀t). La solution contenant t=0 est définie sur ]−∞,t*[ avec t*=1/(ay₀).', 'Le second membre ay² est localement lipschitzien. L’explosion ne contredit donc pas l’existence et l’unicité locales.', 'Pour z′=rz(1−z/K), les équilibres sont 0 et K. Sur 0<z<K la dérivée est positive ; au-dessus de K elle est négative.', 'La formule z=K/[1+(K/z₀−1)e^{−rt}] montre que toute donnée z₀>0 tend vers K à droite, sans dépassement de cet équilibre.'],
        ['a,r,K,y₀ sont strictement positifs ; aucune formule n’est évaluée au temps d’explosion.', 'Une solution maximale est maximale par prolongement de son domaine, pas par comparaison de ses valeurs.', 'Le modèle logistique n’est pas une loi universelle de population : le terme de saturation est une hypothèse explicitement choisie.'])

def homogeneous_oscillator(t,w0,zeta,y0,v0):
    t=np.asarray(t,dtype=float); gamma=zeta*w0
    if abs(zeta-1)<1e-10:
        b=v0+gamma*y0; y=np.exp(-gamma*t)*(y0+b*t)
        v=np.exp(-gamma*t)*(b-gamma*(y0+b*t))
    elif zeta<1:
        w=w0*math.sqrt(1-zeta*zeta); b=(v0+gamma*y0)/w
        c=np.cos(w*t); s=np.sin(w*t); y=np.exp(-gamma*t)*(y0*c+b*s)
        v=np.exp(-gamma*t)*(-gamma*(y0*c+b*s)-w*y0*s+w*b*c)
    else:
        d=w0*math.sqrt(zeta*zeta-1); r1=-gamma+d; r2=-gamma-d
        a=(v0-r2*y0)/(r1-r2); b=y0-a
        y=a*np.exp(r1*t)+b*np.exp(r2*t); v=r1*a*np.exp(r1*t)+r2*b*np.exp(r2*t)
    return y,v

def oscillator_exact(t,w0,zeta,w,force,y0=0,v0=0):
    t=np.asarray(t)
    if zeta==0 and abs(w-w0)<1e-10:
        yp=force*t*np.sin(w0*t)/(2*w0)
        vp=force*(np.sin(w0*t)+w0*t*np.cos(w0*t))/(2*w0)
        h,hv=homogeneous_oscillator(t,w0,zeta,y0,v0)
    else:
        complex_amplitude=force/complex(w0*w0-w*w,2*zeta*w0*w)
        wave=complex_amplitude*np.exp(1j*w*t)
        yp=wave.real; vp=(1j*w*wave).real
        h,hv=homogeneous_oscillator(t,w0,zeta,y0-complex_amplitude.real,v0-(1j*w*complex_amplitude).real)
    return h+yp,hv+vp

def oscillateur_resonance(p):
    w0,zeta,ratio,F,y0,v0=(float(p[k]) for k in ('omega0','zeta','ratio','F','y0','v0'))
    w=w0*ratio; end=int(p['cycles'])*2*math.pi/w0; t=np.linspace(0,end,1601)
    y,v=oscillator_exact(t,w0,zeta,w,F,y0,v0); energy=(v*v+w0*w0*y*y)/2
    dt=t[1]-t[0]; injection=F*np.cos(w*t)*v; loss=2*zeta*w0*v*v
    work=np.concatenate(([0],np.cumsum((injection[:-1]+injection[1:])*dt/2)))
    diss=np.concatenate(([0],np.cumsum((loss[:-1]+loss[1:])*dt/2)))
    residual=energy-energy[0]-work+diss
    rr=np.linspace(.1,2,201)
    if zeta>0:
        response=F/(w0*w0*np.sqrt((1-rr*rr)**2+(2*zeta*rr)**2)); response_title='Amplitude établie pour ζ>0'; ylabel='Amplitude stationnaire'
    else:
        horizon=np.linspace(0,end,401)
        response=np.array([np.max(np.abs(oscillator_exact(horizon,w0,0,float(r*w0),F)[0])) for r in rr]); response_title='Sans amortissement : maximum sur la durée observée'; ylabel='Maximum sur un temps fini'
    if F == 0:
        amplitude_label='Amplitude stationnaire' if zeta>0 else 'Amplitude de la particulière forcée'
        amplitude_value=0.0
    elif zeta>0:
        amplitude_label='Amplitude stationnaire'
        amplitude_value=F/abs(complex(w0*w0-w*w,2*zeta*w0*w))
    elif abs(w-w0)>1e-10:
        amplitude_label='Amplitude de la particulière harmonique'
        amplitude_value=F/abs(w0*w0-w*w)
    else:
        amplitude_label='Amplitude stationnaire'
        amplitude_value='pas de valeur finie'
    bounds=[float(min(y))-.3,float(max(y))+.3,float(min(v))-.3,float(max(v))+.3]
    return result([metric('Durée calculée',end),metric('Régime libre', 'sous-amorti' if zeta<1 else ('critique' if zeta==1 else 'apériodique')),metric('Maximum |y| sur la durée',float(np.max(abs(y)))),metric('Résidu du bilan énergétique',float(np.max(abs(residual)))),metric(amplitude_label,amplitude_value)],
        [chart('Solution exacte avec le transitoire','t','y',series('y(t)',t,y)),chart(response_title,'ω/ω₀',ylabel,series('Réponse calculée',rr,response)),chart('Vérifier le bilan E−E₀=W−D','t','Énergie réduite',series('E−E₀',t,energy-energy[0]),series('Travail injecté',t,work),series('Travail−dissipation',t,work-diss))],
        scene_field('Portrait de phase : position et vitesse',lambda x,v:(v,F-2*zeta*w0*v-w0*w0*x),bounds,[('Trajectoire temporelle',y,v)],'Le champ du système forcé est figé à t=0 ; la trajectoire, elle, emploie bien F cos(ωt).',phase=True),
        ['Résoudre r²+2ζω₀r+ω₀²=0 : racines complexes si ζ<1, double si ζ=1, réelles négatives si ζ>1. Les formules du transitoire sont adaptées à chacun des trois cas.', 'Hors résonance non amortie, une particulière est Re[F e^{iωt}/(ω₀²−ω²+2iζω₀ω)]. Ajuster le transitoire pour obtenir exactement y(0)=y₀ et y′(0)=v₀.', 'Si ζ=0 et ω=ω₀, prendre y_p=Ft sin(ω₀t)/(2ω₀). L’enveloppe croît : utiliser une amplitude stationnaire serait incorrect.', 'Multiplier par y′ : E′=Fcos(ωt)y′−2ζω₀(y′)², avec E=[(y′)²+ω₀²y²]/2. Les intégrales de puissance sont calculées sur le maillage affiché.'],
        ['Variables réduites correspondant à une masse unité ; F est une accélération dans une interprétation mécanique.', 'La courbe établie ne s’applique qu’au régime amorti. Pour ζ=0, le graphique compare des maxima sur le même horizon fini ; hors résonance, la particulière harmonique ne supprime pas le mouvement libre persistant.', 'Si F=0, la particulière forcée est nulle, même si le rapport de pulsations vaut 1. Un mouvement libre peut subsister selon les données initiales.', 'Une petite erreur du bilan provient de l’intégration des puissances par trapèzes ; la trajectoire est donnée par la formule exacte.'])

def variation_solution(t,amplitude,y0,v0):
    t=np.asarray(t); g=lambda x:amplitude*np.exp(x)/np.cosh(x)**2
    s=t[:,None]*(1+_GX)/2
    delta=t[:,None]-s
    yp=t/2*np.sum((np.exp(3*delta)-np.exp(2*delta))*g(s)*_GW,axis=1)
    vp=t/2*np.sum((3*np.exp(3*delta)-2*np.exp(2*delta))*g(s)*_GW,axis=1)
    A=3*y0-v0; B=v0-2*y0; yh=A*np.exp(2*t)+B*np.exp(3*t)
    vh=2*A*np.exp(2*t)+3*B*np.exp(3*t)
    return yh+yp,vh+vp,yp,yh

def variation_constantes(p):
    amp,y0,v0,T=(float(p[k]) for k in ('amplitude','y0','v0','T'))
    t=np.linspace(0,T,501); y,v,yp,yh=variation_solution(t,amp,y0,v0)
    tr,num=rk4(lambda x,z:np.array([z[1],5*z[1]-6*z[0]+amp*math.exp(x)/math.cosh(x)**2]),np.array([y0,v0]),T,1600)
    ref=variation_solution(tr,amp,y0,v0)[0]
    a=gauss_to(t,lambda x:-amp*np.exp(-x)/np.cosh(x)**2)
    b=gauss_to(t,lambda x:amp*np.exp(-2*x)/np.cosh(x)**2)
    return result([metric('Wronskien W(T)=e^{5T}',math.exp(5*T)),metric('Valeur y(T)',float(y[-1])),metric('Valeur y′(T)',float(v[-1])),metric('Écart maximal avec RK4',float(np.max(abs(ref-num[:,0]))))],
        [chart('Superposition : homogène et particulière','x','y',series('Solution totale',t,y),series('Homogène ajustée',t,yh),series('Particulière à données nulles',t,yp)),chart('Les constantes deviennent des fonctions','x','Coefficient',series('a(x), avec a(0)=0',t,a),series('b(x), avec b(0)=0',t,b)),chart('Un contrôle indépendant de la reconstruction','x','Écart absolu',series('|Gauss−RK4|',tr,abs(ref-num[:,0])))],
        scene_field('Plan (y,y′) : distinguer les deux données initiales',lambda y,v:(v,5*v-6*y+amp),[float(min(y))-.5,float(max(y))+.5,float(min(v))-.5,float(max(v))+.5],[('Solution',y,v)],'Le champ est figé à x=0 ; le second membre dépend de x dans la trajectoire réelle.',phase=True),
        ['L’équation homogène a pour solutions e^{2x} et e^{3x}. Leur Wronskien est e^{5x}, donc elles sont indépendantes sur tout ℝ.', 'Imposer a′e^{2x}+b′e^{3x}=0. Le système de Cramer donne a′=−e^{−x}/cosh²x et b′=e^{−2x}/cosh²x, multipliés par l’amplitude choisie.', 'Avec a(0)=b(0)=0, y_p=∫₀ˣ[e^{3(x−s)}−e^{2(x−s)}]g(s)ds. Ce noyau vaut 0 à x=s et sa dérivée en x vaut 1 : il produit les bonnes données initiales.', 'La partie homogène est (3y₀−v₀)e^{2x}+(v₀−2y₀)e^{3x}. Les coefficients répondent à deux conditions, pas à une seule.'],
        ['Toutes les fonctions sont continues sur ℝ ; la solution du problème de Cauchy existe et est unique sur ℝ.', 'Les exponentielles croissantes rendent l’équation sensible aux erreurs initiales. Le domaine affiché est volontairement limité à [0,3].', 'La particulière est calculée par quadrature de Gauss ; la reconstruction est contrôlée par un RK4 indépendant.'])

def euler_particular(x,terms=40):
    x=np.asarray(x,dtype=float); y=np.zeros_like(x); v=np.zeros_like(x); a=np.zeros_like(x)
    small=abs(x)<.04
    for n in range(1,terms+1):
        coefficient=1/(4*n*n-1); z=x[small]
        y[small]+=coefficient*z**(2*n); v[small]+=2*n*coefficient*z**(2*n-1); a[small]+=2*n*(2*n-1)*coefficient*z**(2*n-2)
    z=x[~small]
    if z.size:
        S=.5*np.log(np.abs((1+z)/(1-z)))
        y[~small]=.5+.5*(z-1/z)*S
        v[~small]=.5*(1+1/z**2)*S-.5/z
        a[~small]=1/(z*z*(1-z*z))-S/z**3
    return y,v,a

def euler_cauchy(p):
    gap,C1,C2=(float(p[k]) for k in ('gap','C1','C2')); terms=int(p['terms']); domain=p['domain']
    if domain=='regular': x=np.linspace(0,1-gap,501); C2=0
    elif domain=='singular': x=np.linspace(gap,1-gap,501)
    else: x=np.linspace(1+gap,3,501)
    yp,vp,ap=euler_particular(x); inverse=np.divide(C2,x,out=np.zeros_like(x),where=x!=0)
    y=yp+C1*x+inverse; v=vp+C1-np.divide(C2,x*x,out=np.zeros_like(x),where=x!=0)
    acc=ap+np.divide(2*C2,x**3,out=np.zeros_like(x),where=x!=0)
    forcing=x*x/(1-x*x); residual=x*x*acc+x*v-y-forcing
    z=np.linspace(0,1-gap,501); ref=euler_particular(z)[0]; partial=np.zeros_like(z)
    for n in range(1,terms+1): partial+=z**(2*n)/(4*n*n-1)
    return result([metric('Mode 1/x utilisé',C2),metric('Rayon de convergence de la particulière',1),metric('Erreur maximale de la série sur [0,1−écart]',float(np.max(abs(partial-ref)))),metric('Résidu maximal de l’équation',float(np.max(abs(residual)))),metric('Valeur au bord gauche',float(y[0]))],
        [chart('Une solution sur un intervalle déterminé','x','y',series('Solution totale',x,y),series('Particulière',x,yp),series('Mode C₁x',x,C1*x),series('Mode C₂/x',x,inverse)),chart('Série entière de la particulière régulière','x dans [0,1−écart]','y_p',series('Formule exacte',z,ref),series(f'{terms} termes',z,partial)),chart('La singularité de l’équation reste visible','x','Second membre / résidu',series('x²/(1−x²)',x,forcing),series('Résidu x²y″+xy′−y−f',x,residual))],
        dict(kind='field',title='Fonction, domaines et modes homogènes',description=('La trajectoire est tracée à droite de x=1, sur [1+écart,3]. Aucun segment ne traverse le point singulier x=1.' if domain=='outside' else 'La trajectoire s’arrête avant x=1. Aucun segment n’est tracé à travers un point singulier.'),bounds=scalar_bounds(x,y,yp),arrows=[],paths=[dict(label='Solution',x=x,y=y),dict(label='Particulière',x=x,y=yp)],x_label='x',y_label='y'),
        ['Tester y=xᵐ dans l’équation homogène donne m²−1=0. Sur un intervalle évitant 0, les deux modes sont x et 1/x.', 'Dans |x|<1, identifier les coefficients de la série : y_p=∑ₙ≥₁x^{2n}/(4n²−1). Le terme x est libre ; le terme 1/x est exclu d’un prolongement régulier en 0.', 'La somme est y_p=[(x²−1)ln|(1+x)/(1−x)|+2x]/(4x), avec y_p(0)=0. Près de 0 le calcul utilise la série pour éviter une soustraction de nombres presque égaux.', 'Les points ±1 sont singuliers pour le second membre. Le point 0 est dégénéré pour le coefficient de y″ : il faut vérifier le prolongement, pas appliquer automatiquement un théorème d’ordre 2 sous forme normale.'],
        ['Sur le réglage régulier, C₂ est imposé à 0, même si le curseur possède une valeur différente.', 'La série est comparée seulement dans |x|<1 ; la formule logarithmique permet une résolution sur d’autres intervalles évitant −1,0,1.', 'Sur la branche régulière, y(0)=0 et y′(0)=C₁ ; y_p commence par x²/3. Le prolongement est analytique.'])

def riccati(p):
    c,extent,z0,T=(float(p[k]) for k in ('c','extent','z0','T'))
    x=np.linspace(-extent,extent,501); y=c*x*x-1/(4*c); v=2*c*x
    residual=x*v-y-np.hypot(x,y)
    star=math.atanh(1/z0) if z0>1 else None; end=min(T,.85*star) if star is not None else T
    t=np.linspace(0,end,501); u=np.cosh(t)-z0*np.sinh(t); z=(z0*np.cosh(t)-np.sinh(t))/u
    curves=[(cc,cc*x*x-1/(4*cc)) for cc in (.25,.5,1)]
    return result([metric('Valeur raccordée y(0)',-1/(4*c)),metric('Résidu de l’équation homogène',float(np.max(abs(residual)))),metric('Durée effectivement calculée pour Riccati',end),metric('Explosion Riccati à droite',star if star is not None else 'aucune pour ces données'),metric('Plus petit |u| sur le tracé',float(np.min(abs(u))))],
        [chart('Famille globale de l’équation du recueil','x','y',series('Paramètre choisi c',x,y),*[series(f'c={cc:g}',x,yy) for cc,yy in curves]),chart('Une véritable équation de Riccati : z′=z²−1','t','z / u',series('z=−u′/u',t,z),series('u, solution de u″=u',t,u)),chart('Vérifier le raccordement et l’équation','x','Valeur',series('y′=2cx',x,v),series('xy′−y−√(x²+y²)',x,residual))],
        scene_field('L’équation homogène hors de x=0',lambda x,y:None if abs(x)<1e-6 else (y+math.hypot(x,y))/x,scalar_bounds(x,y),[('Solution globale raccordée',x,y)],'La pente n’est pas calculée par division au point x=0 ; la solution globale y=cx²−1/(4c) y est vérifiée directement.'),
        ['Pour x>0, poser z=y/x : xz′=√(1+z²), donc argsh z=ln x+constante. Sur x<0, tenir compte du signe de |x| dans la racine.', 'Les branches qui se raccordent en 0 donnent y=cx²−1/(4c), avec c>0. En effet √(x²+y²)=cx²+1/(4c), ce qui vérifie l’équation y compris en 0.', 'Cette équation est homogène après substitution y/x ; ce n’est pas une équation de Riccati. Pour comparer, prendre z′=z²−1.', 'Dans Riccati, poser z=−u′/u. On obtient z′=z²−u″/u ; u″=u convient. Avec u(0)=1 et u′(0)=−z₀, u=cosh t−z₀sinh t. Les zéros de u sont les pôles de z.'],
        ['c>0 ; la famille affichée est définie et dérivable sur tout ℝ.', 'Le changement z=y/x est réalisé seulement hors de 0 ; le raccordement est ensuite contrôlé séparément.', 'Pour Riccati avec z₀>1, le calcul s’arrête à 85 % du premier pôle. Aucun tracé ne traverse une explosion.'])

def reservoir_matrix(k12,k23,k13,decay=0):
    return np.array([[-k12-k13,k12,k13],[k12,-k12-k23,k23],[k13,k23,-k13-k23]],dtype=float)-decay*np.eye(3)

def lineaire_systeme(p):
    k12,k23,k13,decay,T=(float(p[k]) for k in ('k12','k23','k13','decay','T'))
    A=reservoir_matrix(k12,k23,k13,decay); values,Q=np.linalg.eigh(A)
    initial=np.eye(3)[int(p['initial'])-1]; coeff=Q.T@initial; t=np.linspace(0,T,501)
    Y=(np.exp(t[:,None]*values)*coeff)@Q.T; expected=np.exp(-decay*t); total=np.sum(Y,axis=1)
    normalized=Y/expected[:,None]; rates=-values
    modes=np.exp(t[:,None]*values)*coeff
    arrows=[]
    A0=A+decay*np.eye(3)
    for x in np.linspace(0,1,12):
        for y in np.linspace(0,1,12):
            if x+y>1: continue
            v=A0@np.array([x,y,1-x-y]); norm=math.hypot(v[0],v[1])
            if norm>1e-12: arrows.append(dict(x=x,y=y,dx=.04*v[0]/norm,dy=.04*v[1]/norm))
    return result([metric('Dimension du système',3),metric('Quantité totale à T',float(total[-1])),metric('Résidu du bilan total',float(np.max(abs(total-expected)))),metric('Taux lent de retour des proportions',float(-np.sort(np.linalg.eigvalsh(A0))[-2])),metric('Plus petite quantité calculée',float(np.min(Y)))],
        [chart('Trois quantités couplées','t','Quantité',*[series(f'Réservoir {j+1}',t,Y[:,j]) for j in range(3)],series('Total',t,total)),chart('Proportions : vers un tiers dans chaque réservoir','t','Fraction du total',*[series(f'Proportion {j+1}',t,normalized[:,j]) for j in range(3)],series('1/3',t,np.full_like(t,1/3))),chart('Évolution de trois coordonnées propres','t','Coefficient de mode',*[series(f'Mode {j+1} : taux {rates[j]:.3g}',t,modes[:,j]) for j in range(3)])],
        dict(kind='phase',title='Le triangle des répartitions possibles',description='Axes : fractions des réservoirs 1 et 2 ; la troisième vaut 1−x−y. Le champ décrit les proportions, même en présence d’une perte uniforme.',bounds=[-.05,1.05,-.05,1.05],arrows=arrows,paths=[dict(label='Répartition',x=normalized[:,0],y=normalized[:,1])],x_label='Fraction 1',y_label='Fraction 2',nodes=[dict(label=str(i+1),amounts=Y[:,i]) for i in range(3)]),
        ['Écrire les trois bilans. Un échange de i vers j est proportionnel à Yᵢ−Yⱼ ; les termes gagnés dans un réservoir sont perdus dans l’autre.', 'La matrice A est symétrique. Écrire A=Q diag(λⱼ)Qᵀ puis Y(t)=Q diag(e^{λⱼt})QᵀY₀ ; les valeurs propres sont toutes non positives.', 'Les sommes des colonnes valent −δ : S′=−δS, donc S=e^{−δt} pour S(0)=1. Avec δ=0 la quantité est conservée.', 'Les proportions P=e^{δt}Y satisfont le système conservatif. Le vecteur (1,1,1) est son mode nul ; les deux autres modes décroissent, donc P tend vers (1/3,1/3,1/3).'],
        ['Trois réservoirs de même volume, échanges symétriques constants et éventuelle perte uniforme.', 'Les quantités initiales sont positives et de somme 1 ; la matrice conserve la positivité.', 'Le portrait utilise les proportions et non les quantités absolues, qui diminuent si δ>0.'])

def green_bords(p):
    lam,a,b,free=(float(p[k]) for k in ('lam','a','b','free'))
    x=np.linspace(0,math.pi,501); f=a*np.sin(x)+b*np.sin(2*x); y=np.zeros_like(x)
    root=int(round(math.sqrt(lam))); resonant=root>=1 and abs(lam-root*root)<1e-10
    incompatible=0.0
    for n,coefficient in [(1,a),(2,b)]:
        if resonant and n==root: incompatible=coefficient
        else: y+=coefficient/(lam-n*n)*np.sin(n*x)
    if resonant and abs(incompatible)<1e-12: y+=free*np.sin(root*x)
    residual=-incompatible*np.sin(root*x) if resonant else np.zeros_like(x)
    status='aucune solution' if abs(incompatible)>1e-12 else ('infinité de solutions' if resonant else 'solution unique')
    scan=np.linspace(0,12,601); shot=np.empty_like(scan); shot[0]=math.pi
    shot[1:]=np.sin(math.pi*np.sqrt(scan[1:]))/np.sqrt(scan[1:])
    scene_label='Partie non résonante : ce n’est pas une solution' if abs(incompatible)>1e-12 else 'Solution choisie'
    return result([metric('Statut du problème aux deux bords',status),metric('Mode homogène résonant',root if resonant else 'aucun'),metric('Projection du second membre sur le mode résonant',incompatible*math.pi/2 if resonant else 0),metric('Valeur |y(π)| du tracé',abs(float(y[-1]))),metric('Résidu maximal du tracé',float(np.max(abs(residual))))],
        [chart(scene_label,'x dans [0,π]','y',series(scene_label,x,y)),chart('Tester la compatibilité','x','Valeur',series('Second membre f',x,f),series('Résidu y″+λy−f',x,residual),series('Mode nul sin(nx)',x,np.sin(root*x) if resonant else np.zeros_like(x))),chart('Méthode de tir : y(0)=0, y′(0)=1','λ','y(π)',series('sin(π√λ)/√λ',scan,shot),xMarker=lam,xMarkerLabel='λ choisi')],
        dict(kind='field',title='Deux valeurs au bord ne sont pas deux données au même point',description='Si la compatibilité échoue, la courbe montrée est seulement la partie non résonante ; le résidu interdit de l’appeler solution.',bounds=scalar_bounds(x,y),arrows=[],paths=[dict(label=scene_label,x=x,y=y)],x_label='x',y_label='y'),
        ['L’équation homogène y″+λy=0, avec y(0)=0, donne y=Csin(√λx) pour λ>0. La condition y(π)=0 force C=0 sauf si λ=n².', 'Décomposer f=a sin x+b sin(2x). Hors résonance, chaque composante donne yₙ=fₙ sin(nx)/(λ−n²).', 'À λ=n², multiplier l’équation par sin(nx), intégrer par parties deux fois et utiliser les bords : ∫₀^π f sin(nx)dx doit être nul. Sinon il n’existe aucune solution.', 'Si cette projection est nulle, ajouter librement Csin(nx) à une particulière. Les deux valeurs aux bords n’assurent donc pas toujours l’unicité, contrairement aux données de Cauchy y(0),y′(0).'],
        ['Conditions de Dirichlet sur [0,π], fonctions réelles ; le second membre n’utilise que les deux premiers modes sinus.', 'L’amplitude libre est utilisée seulement lorsque le problème est résonant et compatible.', 'Les cas exacts λ=1,4,9 sont traités séparément. Les très grandes réponses près de ces valeurs traduisent une réelle sensibilité du problème.'])

MODELS = {name:globals()[name] for name in ('euler_rk4','facteur_integrant','cauchy_lipschitz','explosion_logistique','oscillateur_resonance','variation_constantes','euler_cauchy','riccati','lineaire_systeme','green_bords')}
COMPUTE = MODELS
