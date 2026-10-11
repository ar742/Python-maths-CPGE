"""Modèles de commande et de traitement numérique, NumPy seul."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, curve_scene, result


def homogeneous(t, y0, v0, omega, zeta):
    """Solution libre du second ordre, y(0)=y0, y'(0)=v0."""
    t = np.asarray(t)
    if zeta < 1 - 1e-9:
        wd = omega * math.sqrt(1-zeta*zeta)
        return np.exp(-zeta*omega*t)*(y0*np.cos(wd*t)+(v0+zeta*omega*y0)/wd*np.sin(wd*t))
    if zeta > 1 + 1e-9:
        q = math.sqrt(zeta*zeta-1)
        r1, r2 = -omega/(zeta+q), -omega*(zeta+q)
        c1 = (v0-r2*y0)/(r1-r2)
        return c1*np.exp(r1*t)+(y0-c1)*np.exp(r2*t)
    return np.exp(-omega*t)*(y0+(v0+omega*y0)*t)


def rk4(fun, times, initial, max_step):
    """RK4 avec subdivision selon l'échelle la plus rapide du modèle."""
    out = np.empty((len(times), len(initial)), float)
    out[0] = initial
    for j in range(1, len(times)):
        count = max(1, math.ceil((times[j]-times[j-1])/max_step))
        h = (times[j]-times[j-1])/count
        state, tm = out[j-1].copy(), times[j-1]
        for _ in range(count):
            k1 = fun(tm,state); k2 = fun(tm+h/2,state+h*k1/2)
            k3 = fun(tm+h/2,state+h*k2/2); k4 = fun(tm+h,state+h*k3)
            state += h*(k1+2*k2+2*k3+k4)/6; tm += h
        out[j] = state
    return out


def matrix_exponential(matrix):
    """Exponentielle réelle par série mise à l'échelle et élévations au carré.

    Aucune décomposition en vecteurs propres : les blocs de Jordan et les
    pôles multiples conservent leurs termes polynomiaux en temps.
    """
    matrix=np.asarray(matrix,dtype=float)
    norm=float(np.linalg.norm(matrix,ord=np.inf))
    squares=max(0,math.ceil(math.log2(norm/0.5))) if norm else 0
    scaled=matrix/(2**squares)
    exponential=np.eye(len(matrix)); term=exponential.copy()
    for order in range(1,50):
        term=term@scaled/order
        exponential+=term
        if np.linalg.norm(term,ord=np.inf)<=np.finfo(float).eps*np.linalg.norm(exponential,ord=np.inf):
            break
    for _ in range(squares): exponential=exponential@exponential
    return exponential


def bode_charts(omega, h, label='H'):
    return [chart('Gain fréquentiel','Pulsation ω (rad/s)','Gain (dB)',series(label,omega,20*np.log10(np.maximum(np.abs(h),1e-14))),x_scale='log'),
            chart('Phase fréquentielle','Pulsation ω (rad/s)','Phase (°)',series(label,omega,np.unwrap(np.angle(h))*180/np.pi),x_scale='log')]


def laplace_initiales(p):
    tau,K,E,y0 = (float(p[k]) for k in ('tau','gain','input','initial'))
    t = np.linspace(0,6*tau,501)
    free = y0*np.exp(-t/tau); forced = K*E*(-np.expm1(-t/tau)); y=free+forced
    return result([metric('Valeur initiale',y0,'V'),metric('Valeur finale',K*E,'V'),metric('Constante de temps',tau,'s')],
        [chart('Deux contributions qui s’additionnent','Temps t (s)','Sortie (V)',series('Réponse totale',t,y),series('Entrée, état initial nul',t,forced),series('État initial seul',t,free))],
        curve_scene('Un état initial et une entrée',t,[('Sortie totale',y),('Réponse libre',free),('Réponse forcée',forced)],'t (s)','y (V)','La réponse libre et la réponse à l’entrée s’additionnent.',apparatus={'type':'block','blocks':['E','K/(1+τp)','y'],'feedback':'y₀ fixé au départ'}),
        ['Poser τ dy/dt + y = K E pour t>0, avec y(0)=y₀.',
         'La transformée unilatérale donne (1+τp)Y(p)=K E/p+τy₀.',
         'La réponse libre y₀ exp(−t/τ) s’ajoute à K E(1−exp(−t/τ)).',
         'La fonction de transfert K/(1+τp) correspond à y₀=0.'],
        ['Système linéaire, coefficients constants, échelon maintenu.','La formule temporelle est fournie ; l’inversion générale de Laplace est un prolongement mathématique.'])


def bode_second_ordre(p):
    w0,z,K=(float(p[k]) for k in ('omega0','zeta','gain'))
    w=np.geomspace(w0/100,w0*100,501); h=K/(1-(w/w0)**2+2j*z*w/w0)
    t=np.linspace(0,max(12,6/z)/w0,601); y=K*(1-homogeneous(t,1,0,w0,z))
    overshoot=100*math.exp(-math.pi*z/math.sqrt(1-z*z)) if z<1 else 0
    resonance = w0*math.sqrt(1-2*z*z) if z<1/math.sqrt(2) else 'aucune'
    poles=np.roots([1,2*z*w0,w0*w0])
    return result([metric('Dépassement théorique',overshoot,'%'),metric('Pulsation de résonance',resonance,'rad/s'),metric('Gain statique',K)],
        bode_charts(w,h)+[chart('Réponse à un échelon unité','Temps t (s)','Sortie y',series('Second ordre',t,y))],
        curve_scene('Résonance et réponse temporelle',t,[('Sortie y',y),('Valeur finale',np.full_like(t,K))],'t (s)','y','Le coefficient ζ détermine le dépassement ; les pôles sont affichés dans le plan p.',apparatus={'type':'poles','poles':[dict(re=float(r.real),im=float(r.imag)) for r in poles],'zeros':[],'unitCircle':False}),
        ['H(p)=Kω₀²/(p²+2ζω₀p+ω₀²).','Évaluer H(jω), puis calculer 20 log₁₀|H| et arg(H).',
         'Un pic de résonance existe pour ζ<1/√2 ; un dépassement existe pour ζ<1.',
         'Les pôles sont à partie réelle négative pour tous les réglages proposés.'],
        ['Échelon unité, état initial nul.','Gain en dB et phase en degrés ; ω est une pulsation, pas une fréquence en Hz.'])


def retroaction_sensibilite(p):
    mu,beta,d,tau=(float(p[k]) for k in ('mu','beta','variation','tau'))
    mu2=mu*(1+d); g=mu/(1+mu*beta); g2=mu2/(1+mu2*beta)
    t=np.linspace(0,6*tau,501); y=g*(-np.expm1(-t*(1+mu*beta)/tau)); y2=g2*(-np.expm1(-t*(1+mu2*beta)/tau))
    ds=np.linspace(-0.5,0.5,301); rel=((1+ds)/(1+mu*beta*(1+ds))*(1+mu*beta)-1)*100
    sensitivity=1/(1+mu*beta)
    return result([metric('Gain fermé G',g),metric('Sensibilité relative',sensitivity),metric('Variation relative réelle de G',(g2/g-1)*100,'%'),metric('Variation relative de μ',100*d,'%')],
        [chart('Variation du gain fermé','Variation de μ (%)','Variation de G (%)',series('Calcul exact',100*ds,rel),series('Approximation locale',100*ds,100*ds*sensitivity)),
         chart('Réponse à la même entrée unité','Temps t (s)','Sortie',series('Gain direct initial',t,y),series('Gain direct modifié',t,y2))],
        curve_scene('Contre-réaction négative',t,[('Gain μ initial',y),('Gain μ modifié',y2)],'t (s)','s','Les deux systèmes reçoivent la même entrée ; seul leur gain direct μ change.',apparatus={'type':'block','blocks':['e','μ/(1+τp)','s'],'feedback':'−βs'}),
        ['L’erreur est ε=e−βs ; la chaîne directe donne s=μ ε au régime permanent.','Donc G=s/e=μ/(1+μβ).',
         'Pour une petite variation, dG/G=(dμ/μ)/(1+μβ).','La comparaison exacte reste valable quand la variation est trop grande pour cette approximation.'],
        ['Retour négatif, capteur instantané, gains positifs.','Les amplitudes de cette expérience sont normalisées.'])


def moteur_x(p):
    E,mu,K0,tau,beta=(float(p[k]) for k in ('E','mu','K0','tau','beta'))
    T0=mu*K0; factor=1+beta*T0; Tc=T0/factor; tauc=tau/factor
    t=np.linspace(0,6*tau,601); opened=T0*E*(-np.expm1(-t/tau)); closed=Tc*E*(-np.expm1(-t/tauc))
    error=E-beta*closed
    return result([metric('Vitesse finale en boucle ouverte',T0*E,'rad/s'),metric('Vitesse finale en boucle fermée',Tc*E,'rad/s'),metric('Constante de temps fermée τ′',tauc,'s'),metric('Gain statique fermé T₀′',Tc,'rad·s⁻¹/V')],
        [chart('Deux réponses au même échelon E','Temps t (s)','Vitesse Ω (rad/s)',series('Boucle ouverte Ω',t,opened),series('Boucle fermée Ω′',t,closed)),
         chart('Erreur mesurée à l’entrée de l’amplificateur','Temps t (s)','Tension ε (V)',series('ε = E−βΩ′',t,error))],
        curve_scene('Le moteur X, avant et après fermeture du retour',t,[('Ω ouverte',opened),('Ω′ fermée',closed)],'t (s)','Ω (rad/s)','Le même échelon E donne deux gains statiques et deux constantes de temps.',apparatus={'type':'motor','speed':float(closed[-1]),'label':'Moteur X · retour −βΩ′'}),
        ['Le moteur seul a pour fonction K₀/(1+τp). L’amplificateur a pour gain μ.',
         'En boucle ouverte, T(p)=μK₀/(1+τp) et Ω(t)=μK₀E(1−exp(−t/τ)).',
         'Le capteur renvoie βΩ′ : ε=E−βΩ′.',
         'En boucle fermée, T′(p)=μK₀/(1+μβK₀+τp). Ainsi T₀′=μK₀/(1+μβK₀) et τ′=τ/(1+μβK₀).',
         'Une même tension E donne deux vitesses finales différentes : la réduction de τ ne signifie pas une conservation du gain.'],
        ['Modèle du TP P17, moteur du premier ordre et capteur instantané.','Départ à vitesse nulle, aucune saturation.','Les réponses sont calculées directement à partir de l’équation du premier ordre.'])


def moteur_mcc(p):
    U,R,L,J,b,k,load=(float(p[key]) for key in ('voltage','R','L','J','friction','k','load'))
    L*=1e-3; J*=1e-3; b*=1e-3
    A=np.array([[-R/L,-k/L],[k/J,-b/J]]); forcing=np.array([U/L,-load/J])
    steady=-np.linalg.solve(A,forcing); poles=np.linalg.eigvals(A)
    duration=6/max(1e-6,-float(np.max(poles.real))); t=np.linspace(0,duration,501)
    # La formule 2×2 ci-dessous reste régulière à un pôle double.
    center=np.trace(A)/2; B=A-center*np.eye(2); discr=(center*center-np.linalg.det(A))
    delta=-steady
    def states_at(times):
        if discr>1e-12:
            d=math.sqrt(discr); e1=np.exp((center+d)*times); e2=np.exp((center-d)*times)
            c=(e1+e2)/2; s=(e1-e2)/(2*d)
        elif discr<-1e-12:
            d=math.sqrt(-discr); e=np.exp(center*times); c=e*np.cos(d*times); s=e*np.sin(d*times)/d
        else:
            c=np.exp(center*times); s=times*c
        return steady[:,None]+delta[:,None]*c+(B@delta)[:,None]*s
    states=states_at(t)
    i,w=states; torque=k*i
    short_t=np.linspace(0,min(duration,8*L/R),401)
    short_i=states_at(short_t)[0]
    locked_i=(U/R)*(-np.expm1(-R*short_t/L))
    return result([metric('Vitesse permanente',float(steady[1]),'rad/s'),metric('Courant permanent',float(steady[0]),'A'),metric('Temps électrique L/R',L/R,'s'),metric('Puissance électrique permanente',U*float(steady[0]),'W')],
        [chart('Démarrage mécanique','Temps t (s)','Vitesse Ω (rad/s)',series('Rotor',t,w)),chart('Courant dans l’induit','Temps t (s)','Courant i (A)',series('Courant i',t,i)),chart('Force contre-électromotrice','Temps t (s)','Tension (V)',series('kΩ',t,k*w)),
         chart('Couples mécaniques','Temps t (s)','Couple (N·m)',series('Couple moteur ki',t,torque),series('Frottement bΩ + charge',t,b*w+load)),
         chart('Premiers instants : l’échelle électrique L/R','Temps t (ms)','Courant i (A)',series('Moteur libre de tourner',short_t*1000,short_i),series('Circuit RL, rotor maintenu immobile',short_t*1000,locked_i))],
        curve_scene('Courant, vitesse et charge',t,[('Vitesse Ω',w)],'t (s)','Ω (rad/s)','La tension de retour kΩ relie le bilan électrique au mouvement du rotor.',apparatus={'type':'motor','speed':float(w[-1]),'current':float(i[-1]),'label':'MCC · tension U · charge Cᵣ'}),
        ['Bilan électrique : L di/dt=U−Ri−kΩ.','Bilan mécanique : J dΩ/dt=ki−bΩ−Cᵣ.',
         'Au régime permanent, Ω∞=(kU−RCᵣ)/(Rb+k²), puis i∞=(U−kΩ∞)/R.',
         'La vue courte résout les premiers instants sur l’échelle électrique L/R. Si le rotor reste immobile, le courant de référence vaut (U/R)(1−exp(−Rt/L)).',
         'Une charge assez forte impose une vitesse permanente négative dans ce modèle signé. Il n’inclut aucun frottement sec ni butée.'],
        ['Flux magnétique constant ; mêmes valeurs numériques de la constante de couple et de la constante de tension en unités SI.','Couple résistant signé et constant dès t=0.','Induit et rotor au repos.'])


def correcteur_pi(p):
    tau,K,kp,Ti,target,limit=(float(p[k]) for k in ('tau','gain','kp','Ti','target','limit'))
    aw=p['aw']=='on'; ki=kp/Ti
    duration=max(8*tau,8*Ti); t=np.linspace(0,duration,701); switch=duration/2
    def command(tm,state):
        r=target if tm<switch else target/10
        e=r-state[0]; raw=kp*e+state[1]; u=float(np.clip(raw,-limit,limit))
        return r,e,raw,u
    def fun(tm,state):
        r,e,raw,u=command(tm,state)
        return np.array([(K*u-state[0])/tau,ki*e+((u-raw)/Ti if aw else 0)])
    dt=min(tau/(6*(1+K*kp)),Ti/10)
    states=rk4(fun,t,[0,0],dt); y,integ=states.T
    rr,err,raw,uu=np.array([command(tm,state) for tm,state in zip(t,states)]).T
    reachable=target<=K*limit
    return result([metric('Première consigne accessible','oui' if reachable else 'non'),metric('Erreur à la fin',float(err[-1])),metric('Commande à la fin',float(uu[-1])),metric('Action intégrale à la fin',float(integ[-1]))],
        [chart('Suivi et changement de consigne','Temps t (s)','Sortie',series('Consigne r',t,rr),series('Sortie y',t,y)),chart('Commande limitée et intégrale','Temps t (s)','Commande',series('Commande appliquée u',t,uu),series('Commande demandée',t,raw),series('Action intégrale v',t,integ))],
        curve_scene('Boucle PI avec limite de commande',t,[('Consigne',rr),('Sortie',y)],'t (s)','y','À mi-parcours, la consigne diminue pour montrer le retour après saturation.',apparatus={'type':'block','blocks':['r−y','Kₚ(1+1/(Tᵢp))','limiteur','K/(1+τp)'],'feedback':'retour unitaire'}),
        ['Poser e=r−y ; la commande demandée vaut Kₚe+v avec dv/dt=(Kₚ/Tᵢ)e.',
         'Limiter u entre −uₘₐₓ et +uₘₐₓ ; le procédé suit τ dy/dt+y=Ku.',
         'À mi-parcours, la consigne passe de r à r/10 pour montrer le retour après saturation.',
         'Avec la correction active, ajouter (u−Kₚe−v)/Tᵢ à dv/dt.',
         'L’erreur permanente s’annule pour un PI actif sans saturation. Kₚ=0 désactive ici les deux actions.'],
        ['Procédé du premier ordre, pas de retard pur.','Réglage PI : SI en spé. Saturation et correction de l’accumulation : prolongement.','Intégration numérique avec un pas inférieur aux échelles rapides du modèle.'])


def bisect(fun,lo,hi):
    for _ in range(70):
        mid=math.sqrt(lo*hi)
        if fun(mid)>0: lo=mid
        else: hi=mid
    return math.sqrt(lo*hi)


def stabilite_marges(p):
    K=float(p['K']); taus=np.array([float(p[k]) for k in ('tau1','tau2','tau3')])
    def tf(w): return K/np.prod(1+1j*np.asarray(w)[...,None]*taus,axis=-1)
    lo=1e-5/max(taus); hi=1e5/min(taus); w=np.geomspace(lo,hi,701); h=tf(w)
    wpi=bisect(lambda v:math.pi-np.sum(np.arctan(v*taus)),lo,hi)
    gm=1/abs(tf(wpi)); gdb=20*math.log10(gm)
    if K>1:
        wc=bisect(lambda v:abs(tf(v))-1,lo,hi); pm=180-np.sum(np.arctan(wc*taus))*180/math.pi
    else: wc='aucun'; pm='non définie : gain toujours < 1'
    den=np.poly(-1/taus)*np.prod(taus); den[-1]+=K; roots=np.roots(den); stable=np.max(roots.real)<-1e-10
    # Trois états physiques en cascade, avec retour de la dernière sortie.
    # La propagation matricielle reste régulière si plusieurs pôles coïncident.
    t=np.linspace(0,8*max(taus),601)
    dynamics=np.array([[-1/taus[0],0,-K/taus[0]],
                       [1/taus[1],-1/taus[1],0],
                       [0,1/taus[2],-1/taus[2]]])
    propagator=matrix_exponential(dynamics*(t[1]-t[0]))
    steady=np.full(3,K/(1+K)); deviation=-steady.copy()
    y=np.zeros_like(t)
    for index in range(1,len(t)):
        deviation=propagator@deviation
        y[index]=steady[2]+deviation[2]
    return result([metric('Boucle fermée stable','oui' if stable else 'non'),metric('Marge de phase',pm,'°'),metric('Marge de gain',gdb,'dB'),metric('Pulsation à gain unité',wc,'rad/s')],
        bode_charts(w,h,'Boucle ouverte L')+[chart('Réponse de la boucle fermée','Temps t (s)','Sortie y',series('Échelon unité',t,y))],
        curve_scene('Pôles de la boucle fermée',t,[('Sortie y',y)],'t (s)','y','Les pôles du plan p vérifient ici la stabilité indiquée par les marges.',apparatus={'type':'poles','poles':[dict(re=float(z.real),im=float(z.imag)) for z in roots],'zeros':[],'unitCircle':False}),
        ['L(p)=K/[(1+τ₁p)(1+τ₂p)(1+τ₃p)]. Le retour est négatif et unitaire.',
         'À |L(jωc)|=1, la marge de phase est 180°+arg L(jωc). Si K≤1, ce croisement n’existe pas.',
         'À arg L(jωπ)=−180°, la marge de gain vaut −20 log₁₀|L(jωπ)|.',
         'Les pôles fermés sont les racines de (1+τ₁p)(1+τ₂p)(1+τ₃p)+K. Leur partie réelle vérifie ici la conclusion graphique.'],
        ['Trois pôles stables, aucune annulation de pôle, aucun retard.','Cette comparaison concerne ce modèle ; les marges ne remplacent pas une analyse adaptée à toute boucle.','Lecture des marges : programme SI spé ; calcul des racines fourni.'])


def isolation_sismique(p):
    wr,alpha,eta,f,A=(float(p[k]) for k in ('omega_r','alpha','eta','frequency','amplitude')); A*=1e-3
    c=alpha*eta*wr*wr; wdrive=2*math.pi*f; t=np.linspace(0,8/f,1201)
    ground=A*np.cos(wdrive*t)
    def motion(cc):
        den=wr*wr-wdrive*wdrive+1j*cc*wdrive
        if abs(den)<1e-10*wr*wr:
            return A*wr*t*np.sin(wr*t)/2
        H=(wr*wr+1j*cc*wdrive)/den; C=A*H.real; D=-A*H.imag
        particular=C*np.cos(wdrive*t)+D*np.sin(wdrive*t)
        return particular+homogeneous(t,-C,-D*wdrive,wr,cc/(2*wr))
    uncontrolled=motion(0); controlled=motion(c)
    wf=np.geomspace(wr/30,wr*30,501); wf=wf[np.abs(wf-wr)>1e-12*wr]
    h0=wr*wr/(wr*wr-wf*wf); hc=(wr*wr+1j*c*wf)/(wr*wr-wf*wf+1j*c*wf)
    den=wr*wr-wdrive*wdrive+1j*c*wdrive
    amp=abs((wr*wr+1j*c*wdrive)/den) if abs(den)>1e-12 else 'pas de régime périodique borné'
    return result([metric('Amortissement ajouté ζ',c/(2*wr)),metric('Rapport d’amplitudes permanent |G|',amp),metric('Pulsation propre ωᵣ',wr,'rad/s'),metric('Coefficient de vitesse c',c,'s⁻¹')],
        [chart('Déplacements depuis le repos','Temps t (s)','Position (mm)',series('Sol x₀',t,ground*1000),series('Masse sans contrôle',t,uncontrolled*1000),series('Masse avec contrôle',t,controlled*1000)),
         chart('Transmission du mouvement du sol','Pulsation ω (rad/s)','Gain (dB)',series('Sans contrôle',wf,20*np.log10(np.abs(h0))),series('Avec contrôle',wf,20*np.log10(np.maximum(np.abs(hc),1e-14))),x_scale='log')],
        curve_scene('Pendule inversé : sol, capteur, actionneur',t,[('Sol x₀ (mm)',ground*1000),('Masse contrôlée (mm)',controlled*1000)],'t (s)','x (mm)','Le capteur mesure x−x₀ ; l’actionneur dérive cet écart pour produire la force F.',apparatus={'type':'seismic','amplitude':A*1000,'controlled':eta>0,'label':'F = η d(x−x₀)/dt'}),
        ['Le système de P17 vérifie x(p)=I(p)[x₀(p)−αF(p)], avec I(p)=ωᵣ²/(p²+ωᵣ²).',
         'Le capteur mesure x−x₀ et l’actionneur donne F(p)=ηp[x(p)−x₀(p)].',
         'Poser c=αηωᵣ². Le transfert fermé est G(p)=(ωᵣ²+cp)/(p²+cp+ωᵣ²).',
         'Le dénominateur décrit l’amortissement ; le numérateur dépend aussi du contrôle. À haute fréquence, le contrôle peut augmenter la transmission.',
         'La simulation démarre avec x=0 et dx/dt=0 ; elle inclut le transitoire. Sans amortissement, la résonance exacte n’a pas de régime permanent borné.'],
        ['Petits angles ; raideur effective C−Mgl positive.','α=l²/(C−Mgl), ωᵣ²=(C−Mgl)/(Ml²) ; donc αωᵣ²=1/M. Les réglages impliquent M=1/(αωᵣ²).','Dérivateur idéal, capteur et actionneur sans retard ; schéma repris de l’exercice 4.'])


def adc_codes(values,bits,fullscale):
    levels=2**bits; quantum=2*fullscale/levels
    codes=np.clip(np.floor((np.asarray(values)+fullscale)/quantum),0,levels-1).astype(int)
    return codes,-fullscale+(codes+0.5)*quantum,quantum


def echantillonnage_adc(p):
    f,fe,A,V,phi=(float(p[k]) for k in ('frequency','sample_rate','amplitude','fullscale','phase')); N=int(p['bits']); phi*=np.pi/180
    duration=8/min(f,fe/4); count=min(401,max(30,int(duration*fe)+1)); ts=np.arange(count)/fe
    dense=np.linspace(0,ts[-1],2001); analog=A*np.sin(2*np.pi*f*dense+phi); samples=A*np.sin(2*np.pi*f*ts+phi)
    codes,quantized,q=adc_codes(samples,N,V); alias=abs((f+fe/2)%fe-fe/2)
    # Fréquence signée : elle conserve exactement les échantillons et leur phase.
    signed=(f+fe/2)%fe-fe/2; folded=A*np.sin(2*np.pi*signed*dense+phi)
    err=quantized-samples; clipped=np.abs(samples)>V
    return result([metric('Fréquence repliée',alias,'Hz'),metric('Pas de quantification q',q,'V'),metric('Erreur RMS mesurée',float(np.sqrt(np.mean(err*err))),'V'),metric('Échantillons hors plage',int(np.count_nonzero(clipped)))],
        [chart('Un signal continu et ses codes','Temps t (s)','Tension (V)',series('Signal analogique',dense,analog),series('Signal replié compatible',dense,folded),series('Échantillons quantifiés',ts,quantized)),
         chart('Erreur de conversion','Échantillon k','Erreur (V)',series('Tension codée − tension exacte',np.arange(count),err)),
         chart('Codes du convertisseur','Échantillon k','Code entier',series('Code',np.arange(count),codes))],
        curve_scene('Acquérir un signal',ts,[('Échantillons exacts',samples),('Valeurs converties',quantized)],'t (s)','u (V)','La conversion en codes ajoute une erreur distincte de l’ambiguïté d’échantillonnage.',apparatus={'type':'block','blocks':['u(t)','échantillonneur','CAN '+str(N)+' bits'],'feedback':'fₑ = '+str(int(fe))+' Hz'}),
        ['Échantillonner aux instants tₖ=k/fₑ. Deux fréquences séparées par un multiple de fₑ peuvent donner les mêmes échantillons.',
         'La fréquence ramenée dans [−fₑ/2,fₑ/2[ est ((f+fₑ/2) modulo fₑ)−fₑ/2.',
         'Le convertisseur bipolaire comporte 2ᴺ codes. Ici, q=2Vₘₐₓ/2ᴺ et chaque code est représenté par le centre de son intervalle.',
         'Hors saturation, |erreur|≤q/2. Le modèle q/√12 est une approximation statistique ; l’erreur réelle d’une sinusoïde peut différer.',
         'Le théorème de Nyquist-Shannon exige un signal limité en bande et fₑ>2fₘₐₓ ; le seuil seul ne supprime pas les composantes hautes fréquences.'],
        ['Quantification idéale par intervalles uniformes ; saturation aux codes extrêmes.','Aucun filtre antirepliement ajouté.','Les signaux repliés ne sont pas présentés comme une reconstruction unique.'])


def filtre_rif(p):
    N=int(p['N']); fe=float(p['sample_rate']); nu=float(p['frequency']); noise=float(p['noise'])
    k=np.arange(250); useful=np.sin(2*np.pi*nu*k); x=useful+0.6*np.sin(2*np.pi*noise*k); coeff=np.ones(N)/N
    y=np.convolve(x,coeff)[:len(x)]; h=np.zeros(80); h[:N]=coeff
    freq=np.linspace(0,0.5,501); H=np.exp(-2j*np.pi*freq[:,None]*np.arange(N))@coeff
    usefulgain=abs(np.exp(-2j*np.pi*nu*np.arange(N))@coeff); noisegain=abs(np.exp(-2j*np.pi*noise*np.arange(N))@coeff)
    return result([metric('Retard de groupe',(N-1)/(2*fe),'s'),metric('Gain sur le signal utile',float(usefulgain)),metric('Gain sur le bruit',float(noisegain)),metric('Nombre de coefficients non nuls',N)],
        [chart('Moyenne glissante','Échantillon k','Amplitude',series('Entrée bruitée',k,x),series('Sortie filtrée',k,y),series('Signal utile',k,useful)),
         chart('Réponse impulsionnelle finie','Échantillon k','hₖ',series('Coefficients 1/N',np.arange(80),h)),
         chart('Gain du filtre RIF','Fréquence f (Hz)','Gain (dB)',series('Moyenne de N valeurs',freq*fe,20*np.log10(np.maximum(abs(H),1e-12))))],
        curve_scene('Mémoire finie de N échantillons',k,[('Entrée',x),('Sortie',y)],'k','amplitude','La moyenne utilise N valeurs successives et décale aussi le signal utile.',apparatus={'type':'block','blocks':['xₖ','N retards et sommes','yₖ'],'feedback':'yₖ = (xₖ+…+xₖ₋ₙ₊₁)/N'}),
        ['La sortie est yₖ=(1/N)Σⱼ₌₀ᴺ⁻¹ xₖ₋ⱼ ; les entrées antérieures au début valent zéro.',
         'H(z)=(1/N)Σⱼ₌₀ᴺ⁻¹z⁻ʲ : la réponse impulsionnelle vaut 1/N pour 0≤k<N, puis 0.',
         'Le retard de groupe est (N−1)Tₑ/2 hors les zéros du transfert.',
         'Les fréquences non nulles m fₑ/N sont annulées tant qu’elles restent dans la bande [0,fₑ/2]. Une grande fenêtre atténue aussi le signal utile.'],
        ['Filtre causal, mémoire initiale nulle.','Signal utile et bruit sinusoïdaux de fréquences distinctes ; aucune composante au-delà de fₑ/2.'])


def filtre_rii_z(p):
    a=float(p['a']); N=int(p['N']); k=np.arange(N); h=(1-a)*a**k; step=1-a**(k+1)
    f=np.linspace(0,0.5,501); H=(1-a)/(1-a*np.exp(-2j*np.pi*f))
    return result([metric('Pôle dans le plan z',a),metric('Gain statique',1),metric('Somme de |hₖ|, sur tout k',abs(1-a)/(1-abs(a))),metric('Mémoire d’e⁻¹',(-1/math.log(abs(a)) if a else 0),'échantillons')],
        [chart('Impulsion et échelon à état initial nul','Échantillon k','Amplitude',series('hₖ=(1−a)aᵏ',k,h),series('Réponse à l’échelon',k,step)),
         chart('Gain du filtre récursif','Fréquence relative f/fₑ','Gain (dB)',series('H',f,20*np.log10(abs(H))))],
        curve_scene('Une sortie gardée en mémoire',k,[('Impulsion',h),('Échelon',step)],'k','yₖ','Le coefficient a réinjecte une part de la sortie précédente.',apparatus={'type':'poles','poles':([dict(re=a,im=0)] if a else []),'zeros':([dict(re=0,im=0)] if a else []),'unitCircle':True}),
        ['La récurrence est yₖ=a yₖ₋₁+(1−a)xₖ, avec y₋₁=0.',
         'L’impulsion discrète vaut x₀=1 puis xₖ=0 pour k>0 : hₖ=(1−a)aᵏ.',
         'H(z)=(1−a)/(1−az⁻¹)=(1−a)z/(z−a). Le pôle est z=a.',
         'La stabilité entrée bornée-sortie bornée demande Σ|hₖ|<∞, ici |a|<1. Un a négatif produit une alternance et favorise les hautes fréquences.'],
        ['Tous les réglages proposés vérifient |a|<1.','État initial nul pour l’impulsion et l’échelon.','a=0 supprime le pôle après simplification : le filtre est alors une identité.'])


def discrete_responses(tau,Te,signal,N):
    a=tau/(tau+Te); b=Te/(tau+Te); ab=(2*tau-Te)/(2*tau+Te); bb=Te/(2*tau+Te); az=math.exp(-Te/tau)
    x=np.zeros(N+1); x[1:]=1 if signal=='step' else 0; x[1]=1
    initial=1 if signal=='source' else 0
    e=np.zeros(N+1); bil=e.copy(); exact=e.copy(); e[0]=bil[0]=exact[0]=initial
    # xₖ est maintenu sur ]tₖ₋₁,tₖ] pour comparer les trois méthodes aux mêmes données.
    for k in range(1,N+1):
        e[k]=a*e[k-1]+b*x[k]
        bil[k]=ab*bil[k-1]+bb*(x[k]+x[k-1])
        exact[k]=az*exact[k-1]+(1-az)*x[k]
    return x,e,bil,exact


def discretisation(p):
    tau=float(p['tau'])*1e-3; Te=float(p['Te'])*1e-6; signal=p['signal']; N=min(700,max(30,math.ceil(6*tau/Te)))
    x,e,bil,zoh=discrete_responses(tau,Te,signal,N); k=np.arange(N+1); t=k*Te*1000
    a=tau/(tau+Te); b=Te/(tau+Te); ab=(2*tau-Te)/(2*tau+Te); az=math.exp(-Te/tau)
    return result([metric('Coefficient Euler a',a),metric('Coefficient Euler b',b),metric('Première sortie Euler y₁',float(e[1])),metric('Pôle bilinéaire',ab),metric('Pôle ZOH',az)],
        [chart('Même entrée, trois récurrences','Temps t (ms)','Sortie yₖ',series('Euler implicite',t,e),series('Bilinéaire',t,bil),series('Exacte, entrée maintenue',t,zoh)),
         chart('Écarts à la propagation exacte','Temps t (ms)','Écart',series('Euler − ZOH',t,e-zoh),series('Bilinéaire − ZOH',t,bil-zoh))],
        curve_scene('Transformer un premier ordre analogique',t,[('Euler implicite',e),('Bilinéaire',bil),('ZOH exact',zoh)],'t (ms)','yₖ','Le premier échantillon d’entrée ne doit pas être confondu avec la valeur initiale de la sortie.',apparatus={'type':'block','blocks':['xₖ','récurrence','yₖ'],'feedback':'τ = '+str(p['tau'])+' ms · Tₑ = '+str(p['Te'])+' µs'}),
        ['Euler implicite remplace p par (1−z⁻¹)/Tₑ : H(z)=1/[(1+τ/Tₑ)−(τ/Tₑ)z⁻¹].',
         'Donc yₖ=[τ/(τ+Tₑ)]yₖ₋₁+[Tₑ/(τ+Tₑ)]xₖ.',
         'La transformation bilinéaire remplace p par (2/Tₑ)(1−z⁻¹)/(1+z⁻¹). Son numérateur est proportionnel à 1+z⁻¹.',
         'La propagation exacte sous maintien vaut yₖ=e^(−Tₑ/τ)yₖ₋₁+(1−e^(−Tₑ/τ))xₖ.',
         'Convention : x₀=0 et x₁=1. Euler utilise xₖ ; la règle des trapèzes utilise (xₖ+xₖ₋₁)/2. La propagation ZOH exacte prend xₖ constant sur ]tₖ₋₁,tₖ]. Les trois conventions donnent des premières sorties différentes.',
         'Pour τ=1 ms, Tₑ=50 µs : a=20/21 et b=1/21. Avec y₀=1 et x₁=1, y₁=1, puis y₂=20/21. Avec y₀=0, l’impulsion donne y₁=1/21.'],
        ['Le cas du recueil combine une entrée impulsionnelle discrète et un état initial non nul.','Une impulsion discrète d’amplitude 1 n’est pas une impulsion de Dirac d’aire 1 s.','ZOH désigne ici une entrée constante par intervalle. Le transfert usuel indexé par sa valeur à gauche comporte un retard z⁻¹ supplémentaire.'])


def polezero_z(p):
    r=float(p['radius']); theta=float(p['angle'])*np.pi/180; psi=float(p['zero_angle'])*np.pi/180; N=int(p['N'])
    den=np.array([1,-2*r*math.cos(theta),r*r]); num=np.array([1,-2*math.cos(psi),1]); scale=np.sum(den)/np.sum(num); num*=scale
    h=np.zeros(N)
    for k in range(N):
        h[k]=(num[k] if k<3 else 0)-(den[1]*h[k-1] if k>0 else 0)-(den[2]*h[k-2] if k>1 else 0)
    f=np.linspace(0,0.5,601); q=np.exp(-2j*np.pi*f); H=(num[0]+num[1]*q+num[2]*q*q)/(1+den[1]*q+den[2]*q*q)
    poles=[dict(re=r*math.cos(theta),im=s*r*math.sin(theta)) for s in (-1,1)]; zeros=[dict(re=math.cos(psi),im=s*math.sin(psi)) for s in (-1,1)]
    return result([metric('Module des pôles',r),metric('Fréquence relative des pôles',theta/(2*np.pi)),metric('Fréquence relative annulée',psi/(2*np.pi)),metric('Gain à fréquence nulle',1)],
        [chart('Réponse impulsionnelle','Échantillon k','hₖ',series('Filtre à deux pôles',np.arange(N),h)),
         chart('Gain avec un creux spectral','Fréquence relative f/fₑ','Gain (dB)',series('H',f,20*np.log10(np.maximum(abs(H),1e-12)))),
         chart('Pôles et zéros','Partie réelle de z','Partie imaginaire de z',series('Cercle unité',np.cos(np.linspace(0,2*np.pi,241)),np.sin(np.linspace(0,2*np.pi,241))),series('Pôles',[v['re'] for v in poles],[v['im'] for v in poles]),series('Zéros',[v['re'] for v in zeros],[v['im'] for v in zeros]))],
        curve_scene('Une oscillation amortie en temps discret',np.arange(N),[('Réponse impulsionnelle',h)],'k','hₖ','Le rayon des pôles fixe la décroissance ; leur angle fixe la fréquence relative.',apparatus={'type':'poles','poles':poles,'zeros':zeros,'unitCircle':True}),
        ['Le dénominateur est 1−2r cos(θ)z⁻¹+r²z⁻² ; ses pôles sont r exp(±jθ).',
         'Le numérateur est c[1−2cos(ψ)z⁻¹+z⁻²] ; ses zéros sont exp(±jψ).',
         'Le coefficient c est choisi pour H(1)=1. La fréquence relative associée à θ est θ/(2π).',
         'Les pôles sont strictement à l’intérieur du cercle unité. Approcher r=1 allonge la décroissance sans rendre les réglages proposés instables.'],
        ['Filtre réel, causal, état initial nul.','La fonction en z est un prolongement du filtrage numérique en physique ; le calcul des pôles n’y est pas posé comme exigence générale.'])


def modulation_am(p):
    fm=float(p['message']); F=fm*int(p['ratio']); m=float(p['m']); U=float(p['U']); RC=float(p['rc'])/fm
    t=np.linspace(0,4/fm,int(4*F/fm*45)+1); env=U*(1+m*np.cos(2*np.pi*fm*t)); carrier=np.cos(2*np.pi*F*t); am=env*carrier
    # Diode idéale, charge instantanée aux crêtes positives, décharge RC entre crêtes.
    detected=np.zeros_like(t); detected[0]=max(0,am[0]); decay=math.exp(-(t[1]-t[0])/RC)
    for k in range(1,len(t)): detected[k]=max(0,am[k],detected[k-1]*decay)
    freq=[F-fm,F,F+fm]; amplitudes=[m*U/2,U,m*U/2]
    power=U*U/2*(1+m*m/2); eff=m*m/(2+m*m)*100
    return result([metric('Fréquence porteuse F',F,'Hz'),metric('Amplitude des bandes latérales',m*U/2,'V'),metric('Puissance moyenne pour R=1 Ω',power,'W'),metric('Part de puissance des bandes latérales',eff,'%'),metric('Enveloppe fidèle possible','oui, avec RC adapté' if m<=1 else 'non : surmodulation')],
        [chart('Signal AM et enveloppe','Temps t (ms)','Tension (V)',series('AM',t*1000,am),series('Enveloppe algébrique',t*1000,env),series('Détecteur diode-RC',t*1000,detected)),
         chart('Trois raies du spectre en amplitude','Fréquence (Hz)','Amplitude crête (V)',series('Porteuse et bandes latérales',freq,amplitudes),style='bars'),
         chart('Message reçu après retrait de la composante constante','Temps t (ms)','Tension (V)',series('Détecteur diode-RC, puis retrait de U',t*1000,detected-U),series('Détection synchrone et passe-bas idéaux',t*1000,env-U))],
        curve_scene('Une porteuse dont l’amplitude porte le message',t*1000,[('AM',am),('Enveloppe idéale',env),('Détecteur RC',detected)],'t (ms)','u (V)','La diode suit les crêtes positives ; elle perd le signe lors d’une surmodulation.',apparatus={'type':'block','blocks':['1+m cos(2πft)','multiplicateur × porteuse','diode + RC'],'feedback':'1/F ≪ RC ≪ 1/f'}),
        ['Le message est cos(2πft), la porteuse cos(2πFt), et uAM(t)=U[1+m cos(2πft)]cos(2πFt).',
         'Le produit de cosinus donne les raies F, F−f et F+f ; leurs amplitudes sont U, mU/2 et mU/2.',
         'Le détecteur diode-RC charge le condensateur aux crêtes et le laisse se décharger entre elles.',
         'Choisir 1/F≪RC≪1/f : trop petit, RC laisse l’ondulation de porteuse ; trop grand, il ne suit plus le message. Ces repères approximatifs se resserrent lorsque m approche 1.',
         'Pour m>1, le facteur 1+m cos(2πft) change de signe. L’enveloppe géométrique devient sa valeur absolue et le détecteur perd le signe du message.',
         'La comparaison synchrone multiplie par 2cos(2πFt), puis retire idéalement les raies rapides. Après retrait de U, elle conserve Um cos(2πft), même pour m>1.'],
        ['Modulation AM à porteuse conservée, fréquences distinctes F>f.','Détecteur idéal sans seuil ni résistance interne ; aucune charge de réception.','Détection synchrone de référence parfaitement accordée en fréquence et en phase ; passe-bas idéal entre f et 2F−f.','Le calcul de puissance est normalisé pour une résistance de 1 Ω.'])


COMPUTE={name:globals()[name] for name in ('laplace_initiales','bode_second_ordre','retroaction_sensibilite','moteur_x','moteur_mcc','correcteur_pi','stabilite_marges','isolation_sismique','echantillonnage_adc','filtre_rif','filtre_rii_z','discretisation','polezero_z','modulation_am')}
