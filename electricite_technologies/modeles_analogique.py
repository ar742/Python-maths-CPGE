"""Modèles déterministes NumPy ; les limitations et régimes sont déclarés."""
from __future__ import annotations
import math
import numpy as np
from commun import metric as m, series, chart, curve_scene, result


def _time(f, cycles=4, count=1800):
    return np.linspace(0, cycles/f, count)


def _bode(freq, h, title='Réponse en fréquence'):
    return [chart(title+' : gain','Fréquence (Hz)','Gain (dB)',series('Gain',freq,20*np.log10(np.maximum(np.abs(h),1e-16))),x_scale='log'),
            chart(title+' : phase','Fréquence (Hz)','Phase (°)',series('Phase',freq,np.unwrap(np.angle(h))*180/np.pi),x_scale='log')]


def ali_flow(value, target, rate, dt, slew, limit):
    """Flot exact à entrée constante : y' = borne(rate*(target-y), ±slew).

    La tension est ensuite arrêtée aux rails. Il s'agit d'un état causal :
    on ne découpe pas une sinusoïde déjà calculée pour simuler le balayage.
    """
    distance=target-value
    critical=slew/rate
    if abs(distance) <= critical:
        value=target+(value-target)*math.exp(-rate*dt)
    else:
        travel=(abs(distance)-critical)/slew
        if dt <= travel:
            value += math.copysign(slew*dt,distance)
        else:
            edge=target-math.copysign(critical,distance)
            value=target+(edge-target)*math.exp(-rate*(dt-travel))
    return max(-limit,min(limit,value))


def ali_response(t, u, gain, a0, ft, slew, limit, offset=0):
    fp=ft/a0
    gain0=a0/(1+a0/gain)
    rate=2*np.pi*fp*(1+a0/gain)
    y=np.zeros_like(t)
    for k in range(1,len(t)):
        y[k]=ali_flow(float(y[k-1]),gain0*float(u[k-1]+offset),rate,float(t[k]-t[k-1]),slew,limit)
    return y


def ali_gain_bande(p):
    gain,a0,ft=p['gain'],p['a0'],p['ft']*1000
    f,e,rail=p['f']*1000,p['e'],p['vsat']
    current_limit=p['imax']*1e-3*p['rl']
    limit=min(rail,current_limit)
    sr=p['sr']*1e6; offset=p['vos']*1e-3
    fp=ft/a0; g0=a0/(1+a0/gain); fc=fp*(1+a0/gain)
    t=_time(f); u=e*np.sin(2*np.pi*f*t)
    y=ali_response(t,u,gain,a0,ft,sr,limit,offset)
    ideal=gain*u
    freq=np.geomspace(max(1,fc/100),max(fc*100,f*3),500)
    h=g0/(1+1j*freq/fc)
    charts=[chart('Entrée et sortie depuis le repos','Temps (ms)','Tension (V)',series('Entrée',t*1000,u),series('ALI dynamique',t*1000,y),series('Prédiction idéale',t*1000,ideal))]+_bode(freq,h)
    amp=e*g0/math.sqrt(1+(f/fc)**2)
    return result([m('Gain statique bouclé',g0),m('Bande à −3 dB',fc,'Hz'),m('Produit gain × bande',g0*fc,'Hz'),m('Amplitude linéaire attendue',amp,'V'),
                   m('Plafond imposé par la charge',limit,'V'),m('Pente requise en régime linéaire',2*np.pi*f*amp/1e6,'V/µs'),m('Décalage statique',g0*offset,'V')],charts,
                  curve_scene('Une amplification qui garde la mémoire de son état',t*1000,[('Entrée',u),('Sortie',y)],'Temps (ms)','V',
                              'La sortie part de zéro et rejoint le régime forcé ; ses transitions respectent la pente maximale.',
                              {'type':'ali','gain':gain,'vsat':rail,'load':p['rl'],'current_mA':p['imax'],'feedback':'negative'}),
                  ['Poser β = 1/G : l’entrée différentielle vaut e + Vₒₛ − βvₛ.',
                   'Avec A(s) = A₀/(1 + s/ωₚ), calculer G₀ = A₀/(1 + A₀β) et f_c = (fₜ/A₀)(1 + A₀β).',
                   'Propager l’état de sortie avec une entrée constante sur chaque intervalle ; borner sa dérivée et arrêter sa tension aux rails.',
                   'Une charge résistive impose aussi |vₛ| ≤ IₘₐₓRₗ. Comparer les limites de tension, de courant et de pente.'],
                  ['ALI à un pôle, entrée de résistance infinie et sortie de résistance nulle. Charge purement résistive.',
                   'La simulation utilise une entrée échantillonnée maintenue constante par intervalle. Le gain et la phase décrivent seulement le régime linéaire.',
                   'Le décalage Vₒₛ est un prolongement : il est explicitement exclu des contenus de physique PSI/PT. Courants de polarisation et récupération après saturation non modélisés.'])


def cascade_transfer(s,r1,r2,c1,c2,buffer=False):
    if buffer:
        return 1/((1+s*r1*c1)*(1+s*r2*c2))
    return 1/(1+s*(r1*c1+r2*c2+r1*c2)+s*s*r1*r2*c1*c2)


def suiveur_cascade(p):
    r1,r2,c1,c2=p['r1']*1000,p['r2']*1000,p['c1']*1e-9,p['c2']*1e-9
    f,e=p['f'],p['e']; fc1=1/(2*np.pi*r1*c1); fc2=1/(2*np.pi*r2*c2)
    freq=np.geomspace(min(fc1,fc2)/100,max(fc1,fc2)*100,500)
    hp=cascade_transfer(2j*np.pi*freq,r1,r2,c1,c2)
    hb=cascade_transfer(2j*np.pi*freq,r1,r2,c1,c2,True)
    hpf=cascade_transfer(2j*np.pi*f,r1,r2,c1,c2); hbf=cascade_transfer(2j*np.pi*f,r1,r2,c1,c2,True)
    t=_time(f,3); wave=np.exp(2j*np.pi*f*t)
    u=e*wave.imag; yp=e*np.imag(hpf*wave); yb=e*np.imag(hbf*wave)
    loading=p['rl']/(p['rs']+p['rl'])
    return result([m('Fréquence propre de la cellule 1',fc1,'Hz'),m('Fréquence propre de la cellule 2',fc2,'Hz'),m('Gain des cellules directement reliées',abs(hpf)),m('Gain avec suiveur',abs(hbf)),m('Lecture directe du capteur',loading*100,'%'),m('Lecture avec suiveur idéal',100,'%')],
        [chart('Charge mutuelle des cellules','Fréquence (Hz)','Gain (dB)',series('Sans suiveur',freq,20*np.log10(abs(hp))),series('Avec suiveur',freq,20*np.log10(abs(hb))),x_scale='log'),
         chart('Régime sinusoïdal établi','Temps (ms)','Tension (V)',series('Entrée',t*1000,u),series('Sans suiveur',t*1000,yp),series('Avec suiveur',t*1000,yb))],
        curve_scene('Séparer deux filtres par un suiveur',t*1000,[('Sans suiveur',yp),('Avec suiveur',yb)],'Temps (ms)','V','Chaque condensateur est relié à la masse. Le suiveur est placé entre les deux cellules.',{'type':'filter','r1':r1,'r2':r2,'c1':c1,'c2':c2,'buffer':True}),
        ['Écrire les lois des nœuds aux deux tensions intermédiaires.',
         'Sans suiveur : H(s) = 1/[1 + s(R₁C₁ + R₂C₂ + R₁C₂) + s²R₁R₂C₁C₂].',
         'Avec suiveur idéal, l’entrée de la seconde cellule ne prélève aucun courant sur la première : H(s) = 1/[(1 + sR₁C₁)(1 + sR₂C₂)].',
         'Pour un capteur de résistance interne Rₛ, la lecture directe sur Rₗ donne Rₗ/(Rₛ + Rₗ) fois sa tension à vide.'],
        ['Deux cellules RC passe-bas et sortie finale non chargée ; ALI suiveur idéal stable, sans limite de courant ni de bande.',
         'Le calcul du capteur est une seconde expérience statique indépendante des deux cellules. L’amplitude affichée concerne seulement les filtres.'])


def sommateur_inverseur(p):
    r1,r2,rf=p['r1'],p['r2'],p['rf']; f=p['f']; t=_time(f,3)
    u1=p['e1']*np.sin(2*np.pi*f*t)
    u2=p['e2']*np.sin(4*np.pi*f*t+np.deg2rad(p['phase']))
    predicted=-rf*(u1/r1+u2/r2); y=np.clip(predicted,-p['vsat'],p['vsat'])
    return result([m('Poids de l’entrée 1',-rf/r1),m('Poids de l’entrée 2',-rf/r2),m('Borne supérieure de |sortie idéale|',rf*(p['e1']/r1+p['e2']/r2),'V'),m('Maximum calculé de |sortie idéale|',float(np.max(abs(predicted))),'V')],
        [chart('Somme de deux fréquences','Temps (ms)','Tension (V)',series('Entrée 1 : f',t*1000,u1),series('Entrée 2 : 2f',t*1000,u2),series('Somme idéale',t*1000,predicted),series('Sortie limitée',t*1000,y))],
        curve_scene('Deux résistances pondèrent les tensions',t*1000,[('Entrée 1',u1),('Entrée 2',u2),('Sortie',y)],'Temps (ms)','V','Les courants des deux entrées se rejoignent à la borne inverseuse.',{'type':'ali','r1':r1*1000,'r2':r2*1000,'rf':rf*1000,'inputs':2}),
        ['En régime linéaire, v₋ = v₊ = 0 et les courants d’entrée de l’ALI sont nuls.',
         'La loi des nœuds donne vₑ₁/R₁ + vₑ₂/R₂ + vₛ/Rf = 0.',
         'D’où vₛ = −Rf(vₑ₁/R₁ + vₑ₂/R₂). Les deux résistances d’entrée fixent les poids.',
         'Le signal de la seconde entrée a ici une fréquence 2f : vérifier sa contribution séparément.'],
        ['ALI idéal ; saturation représentée par une limitation algébrique quasi statique. Les états internes d’un ALI réel, sa bande et sa vitesse de balayage ne sont pas simulés ici.',
         'La formule de somme ne décrit le circuit réel que lorsque la contre-réaction peut maintenir un fonctionnement linéaire.'])


def derivative_transfer(s,r,c,rf,cf):
    return -rf*c*s/((1+r*c*s)*(1+rf*cf*s))


def integrateur_derivateur(p):
    r,c,rf,cf=p['r']*1000,p['c']*1e-9,p['rf']*1000,p['cf']*1e-9
    e,f=p['e'],p['f']; omega=2*np.pi*f; t=_time(f,3); u=e*np.sin(omega*t)
    freq=np.geomspace(1,1e7,500); s=2j*np.pi*freq
    mode=p['mode']
    if mode=='integrateur':
        h=-1/(s*r*c); y=e/(omega*r*c)*(np.cos(omega*t)-1)
        label='Intégrale depuis t = 0'; amp=e/(omega*r*c)
        steps=['Le condensateur de rétroaction reçoit le courant vₑ/R.', 'Avec vₛ(0) = 0, vₛ(t) = −(1/RC)∫₀ᵗvₑ(u) du.', 'Pour vₑ = E sin(ωt), vₛ = E[cos(ωt) − 1]/(ωRC). La composante constante fixe la condition initiale.']
    elif mode=='derivee':
        h=-s*r*c; y=-r*c*e*omega*np.cos(omega*t); label='Dérivée idéale'; amp=e*r*c*omega
        steps=['Le condensateur d’entrée porte le courant C dvₑ/dt.', 'La résistance de rétroaction R donne vₛ = −RC dvₑ/dt.', 'Pour une sinusoïde, le gain en amplitude vaut RCω et la sortie est opposée à sa dérivée.']
    else:
        h=derivative_transfer(s,r,c,rf,cf)
        hf=derivative_transfer(1j*omega,r,c,rf,cf); y=e*np.imag(hf*np.exp(1j*omega*t)); label='Dérivateur amélioré'; amp=e*abs(hf)
        steps=['L’impédance d’entrée est R + 1/(sC), celle de rétroaction est R′/(1 + sR′C′).',
               'Le montage est inverseur : H(s) = −R′Cs/[(1 + RCs)(1 + R′C′s)].',
               'Si ωRC et ωR′C′ sont petits, vₛ ≈ −R′C dvₑ/dt. Les deux pôles empêchent le gain de croître sans limite.']
    charts=[chart('Opération sur une sinusoïde','Temps (ms)','Tension (V)',series('Entrée',t*1000,u),series(label,t*1000,y))]+_bode(freq,h)
    return result([m('Échelle RC',r*c*1e6,'µs'),m('Amplitude sinusoïdale de sortie',amp,'V'),m('Pôle lié à RC',1/(2*np.pi*r*c),'Hz'),m('Pôle lié à R′C′',1/(2*np.pi*rf*cf),'Hz')],charts,
        curve_scene(label,t*1000,[('Entrée',u),('Sortie',y)],'Temps (ms)','V','Les tensions peuvent dépasser une alimentation réelle : ce laboratoire teste d’abord les modèles idéaux.',{'type':'ali','mode':mode,'r':r,'c':c,'rf':rf,'cf':cf}),steps,
        ['ALI idéal de gain infini ; aucune saturation ni limite de pente. Les autres laboratoires permettent de tester ces limites.',
         'Dérivateurs en régime sinusoïdal établi. Intégrateur calculé depuis t = 0 avec une sortie initiale nulle ; son diagramme fréquentiel concerne la partie sinusoïdale.'])


def schmitt_states(u,beta,vsat,initial=1):
    y=np.empty_like(u); state=initial
    for k,value in enumerate(u):
        if state>0 and value>=beta*vsat: state=-1
        elif state<0 and value<=-beta*vsat: state=1
        y[k]=state*vsat
    return y


def schmitt_trigger(p):
    beta=p['r2']/(p['r1']+p['r2']); threshold=beta*p['vsat']; t=_time(p['f'],2,2300)
    phase=(t*p['f'])%1; u=p['e']*(1-4*np.abs(phase-0.5))+p['noise']*np.sin(2*np.pi*23*p['f']*t)
    y=schmitt_states(u,beta,p['vsat'],1 if p['initial']=='haut' else -1)
    return result([m('Seuil de montée',threshold,'V'),m('Seuil de descente',-threshold,'V'),m('Largeur de l’hystérésis',2*threshold,'V'),m('Nombre de basculements',int(np.count_nonzero(np.diff(y))))],
        [chart('La sortie conserve son état entre les seuils','Temps (ms)','Tension (V)',series('Entrée',t*1000,u),series('Sortie',t*1000,y),series('Seuil haut',t*1000,np.full_like(t,threshold)),series('Seuil bas',t*1000,np.full_like(t,-threshold))),
         chart('Cycle entrée–sortie parcouru dans le temps','Entrée (V)','Sortie (V)',series('Trajet',u,y))],
        curve_scene('Deux seuils et un état mémorisé',t*1000,[('Entrée',u),('Sortie',y)],'Temps (ms)','V','L’entrée est appliquée à la borne négative. La borne positive reçoit une fraction de la sortie.',{'type':'schmitt','beta':beta,'high':threshold,'low':-threshold,'vsat':p['vsat']}),
        ['La borne positive reçoit v₊ = βvₛ, avec β = R₂/(R₁ + R₂). La borne négative reçoit vₑ.',
         'Pour vₛ = +Vₛₐₜ, cet état subsiste tant que vₑ < βVₛₐₜ ; en montée il bascule au seuil haut.',
         'Pour vₛ = −Vₛₐₜ, cet état subsiste tant que vₑ > −βVₛₐₜ ; en descente il bascule au seuil bas.',
         'Entre les seuils, la tension d’entrée seule ne détermine pas la sortie : il faut connaître son état précédent.'],
        ['ALI idéal en saturation, niveaux symétriques et basculements instantanés. Le signal ajouté est une sinusoïde déterministe à 23f, pas une mesure de bruit aléatoire.',
         'À l’égalité exacte avec un seuil, on adopte le nouvel état ; cette convention ne modifie pas les seuils physiques.'])


def astable_parameters(p):
    tau=p['r1']*1000*p['c']*1e-9; beta=p['r2']/(p['r2']+p['r3']); h=(1-beta)*p['ve']; v=p['vsat']
    low,high=h-beta*v,h+beta*v
    if not (-v<low<high<v): return tau,beta,low,high,None,None
    plus=tau*math.log((v-low)/(v-high)); minus=tau*math.log((high+v)/(low+v))
    return tau,beta,low,high,plus,minus


def astable(p):
    tau,beta,low,high,plus,minus=astable_parameters(p); v=p['vsat']
    if plus is None:
        t=np.linspace(0,8*tau,1600); state=1 if p['ve']>=0 else -1
        y=np.full_like(t,state*v); vc=state*v*(1-np.exp(-t/tau)); period=0; duty=0
        description='La commande empêche d’atteindre l’un des seuils : la sortie reste dans un état saturé.'
    else:
        period=plus+minus; duty=plus/period; t=np.linspace(0,4*period,2200); phase=t%period
        positive=phase<plus; y=np.where(positive,v,-v)
        vc=np.where(positive,v+(low-v)*np.exp(-phase/tau),-v+(high+v)*np.exp(-(phase-plus)/tau))
        description='Le condensateur charge vers le niveau de sortie jusqu’au seuil suivant, puis le sens de charge change.'
    threshold=(1-beta)*p['ve']+beta*y
    return result([m('Constante de temps',tau*1000,'ms'),m('Seuil bas',low,'V'),m('Seuil haut',high,'V'),m('Période (0 si arrêt)',period*1000,'ms'),m('Fréquence (0 si arrêt)',1/period if period else 0,'Hz'),m('Fraction du temps au niveau positif',100*duty,'%')],
        [chart('Charge et basculements','Temps (ms)','Tension (V)',series('Condensateur v_C',t*1000,vc),series('Sortie vₛ',t*1000,y),series('Seuil instantané v₊',t*1000,threshold))],
        curve_scene('Un condensateur fait basculer le comparateur',t*1000,[('Condensateur',vc),('Sortie',y)],'Temps (ms)','V',description,{'type':'oscillator','mode':'astable','r':p['r1']*1000,'c':p['c']*1e-9,'low':low,'high':high,'vsat':v}),
        ['Poser τ = R₁C, β = R₂/(R₂ + R₃) et h = (1 − β)Vₑ. Les seuils valent h ± βVₛₐₜ.',
         'Pour une sortie positive, v_C tend vers +Vₛₐₜ : t₊ = τ ln[(Vₛₐₜ − seuil bas)/(Vₛₐₜ − seuil haut)].',
         'Pour une sortie négative, v_C tend vers −Vₛₐₜ : t₋ = τ ln[(seuil haut + Vₛₐₜ)/(seuil bas + Vₛₐₜ)].',
         'La période est t₊ + t₋. À commande nulle, T = 2τ ln[(1 + β)/(1 − β)]. Les oscillations exigent |Vₑ| < Vₛₐₜ.'],
        ['Basculements instantanés, condensateur idéal et niveaux de saturation symétriques. Le montage conserve la commande continue prévue dans le schéma de départ.',
         'En oscillation, le tracé débute au seuil bas dans le régime périodique. En arrêt, le condensateur est initialement déchargé. La limite |Vₑ| = Vₛₐₜ est atteinte seulement en un temps infini.'])


def wien(p):
    r1,r2,c1,c2=p['r1']*1000,p['r2']*1000,p['c1']*1e-9,p['c2']*1e-9
    a=r1*c1+r2*c2+r2*c1; b=r2*c1; d=r1*r2*c1*c2
    w0=1/math.sqrt(d); f0=w0/(2*np.pi); critical=a/b; gain=p['margin']*critical
    growth=(gain*b-a)/(2*d); t=_time(f0,24,2500); seed=p['seed']; v=p['vsat']
    if growth>1e-10:
        decay=np.exp(-2*growth*t)
        amplitude=1/np.sqrt(decay/(seed*seed)+(1-decay)/(v*v))
    elif growth< -1e-10:
        amplitude=seed*np.exp(growth*t)
    else:
        amplitude=np.full_like(t,seed)
    y=amplitude*np.cos(w0*t)
    freq=np.geomspace(f0/100,f0*100,500); s=2j*np.pi*freq; feedback=b*s/(1+a*s+d*s*s)
    return result([m('Fréquence sélectionnée',f0,'Hz'),m('Gain critique',critical),m('Gain réglé',gain),m('Taux initial de croissance approché',growth,'s⁻¹'),m('Amplitude finale du modèle',float(amplitude[-1]),'V')],
        [chart('Démarrage ou extinction : modèle d’enveloppe','Temps (ms)','Tension (V)',series('Oscillation',t*1000,y),series('Enveloppe positive',t*1000,amplitude),series('Enveloppe négative',t*1000,-amplitude))]+_bode(freq,feedback,'Pont seul'),
        curve_scene('Le pont sélectionne une fréquence',t*1000,[('Sortie',y),('Enveloppe',amplitude)],'Temps (ms)','V','Le gain critique est calculé sur le circuit. La limitation de l’enveloppe est un modèle pédagogique déclaré.',{'type':'oscillator','mode':'wien','r1':r1,'r2':r2,'c1':c1,'c2':c2,'gain':gain,'critical':critical}),
        ['Le pont a pour transfert B(s) = R₂C₁s/[1 + (R₁C₁ + R₂C₂ + R₂C₁)s + R₁R₂C₁C₂s²].',
         'La phase est nulle pour ω₀ = 1/√(R₁R₂C₁C₂). À cette pulsation, B = 1/Gcrit avec Gcrit = 1 + R₁/R₂ + C₂/C₁.',
         'Pour un amplificateur non inverseur de gain G = 1 + R/R₃, le seuil impose G = Gcrit. Le démarrage exige G > Gcrit.',
         'L’équation linéaire est d vₛ″ + (a − Gb)vₛ′ + vₛ = 0. Près du seuil, le taux de croissance de l’enveloppe vaut γ ≈ (Gb − a)/(2d).'],
        ['Pont et ALI idéaux pour le seuil. La fréquence et le gain critique sont exacts pour le modèle linéaire du pont.',
         'Le tracé utilise une approximation d’enveloppe près du seuil : A′ = γA(1 − A²/Vlim²) si γ > 0, et A′ = γA sinon. Vlim fixe une amplitude conventionnelle ; elle ne prédit pas celle d’un ALI ou d’une lampe réelle.',
         'Loin du seuil, l’enveloppe n’est pas une prédiction quantitative du circuit ; le réglage garde surtout sa valeur qualitative. Les harmoniques de saturation et la bande de l’ALI sont omises.'])


def redresseur_precision(p):
    t=_time(p['f'],3); e=p['e']*np.sin(2*np.pi*p['f']*t); ideal=abs(e); cap=max(p['vsat']-p['vd'],0)
    corrected=np.minimum(ideal,cap); v1=-np.where(e>0,corrected,0); v2=np.where(e<0,corrected,0)
    internal=-np.sign(e)*np.minimum(ideal+p['vd'],p['vsat']); passive=np.maximum(ideal-2*p['vd'],0)
    return result([m('Amplitude de l’entrée',p['e'],'V'),m('Seuil total du pont passif',2*p['vd'],'V'),m('Amplitude maximale compensable',cap,'V'),m('Crête de la sortie de précision',min(p['e'],cap),'V')],
        [chart('Redresser une petite tension','Temps (ms)','Tension (V)',series('Entrée',t*1000,e),series('Valeur absolue idéale',t*1000,ideal),series('Pont de diodes',t*1000,passive),series('Sortie différentielle de précision',t*1000,corrected)),
         chart('Tensions nécessaires dans le montage à ALI','Temps (ms)','Tension (V)',series('vₛ₁',t*1000,v1),series('vₛ₂',t*1000,v2),series('Sortie interne de l’ALI',t*1000,internal))],
        curve_scene('La contre-réaction compense le seuil des diodes',t*1000,[('Entrée',e),('Précision',corrected),('Pont passif',passive)],'Temps (ms)','V','Trois résistances égales ; la tension utile est vₛ₂ − vₛ₁. Les deux diodes conduisent alternativement.',{'type':'ali','mode':'rectifier','vd':p['vd'],'vsat':p['vsat']}),
        ['Avec trois résistances égales et une contre-réaction active, e > 0 donne vₛ₁ = −e et vₛ₂ = 0.',
         'Pour e < 0, vₛ₁ = 0 et vₛ₂ = −e. La tension différentielle vₛ₂ − vₛ₁ vaut donc |e|.',
         'L’ALI fournit en interne une excursion supplémentaire égale au seuil Vᴅ. La compensation exige |e| + Vᴅ ≤ Vₛₐₜ.',
         'Un pont passif traverse deux diodes : sa sortie est max(|e| − 2Vᴅ, 0) dans le modèle à seuil.'],
        ['Modèle quasi statique, diodes à seuil constant et résistance dynamique nulle, trois résistances égales et sortie différentielle non chargée.',
         'Les rails limitent la sortie utile à Vₛₐₜ − Vᴅ. Les transitions internes près de e = 0 sont instantanées ici : la récupération et la vitesse de l’ALI réel ne sont pas modélisées.'])


def state_parameters(p):
    r=[p['r'+str(k)]*1000 for k in range(1,7)]; c=p['c']*1e-9
    r1,r2,r3,r4,r5,r6=r
    h0=r2*r5/(r1*r4); w0=math.sqrt(r5/(r3*r4*r6))/c; q=r2*c*w0; width=1/(r2*c)
    low=(math.sqrt(4*w0*w0+width*width)-width)/2
    high=(math.sqrt(4*w0*w0+width*width)+width)/2
    return r,c,h0,w0,q,low,high


def state_transfer(omega,h0,w0,q):
    omega=np.asarray(omega)
    return h0/(1+1j*q*(omega/w0-w0/omega))


def filtre_etat(p):
    r,c,h0,w0,q,low,high=state_parameters(p); r1,r2,r3,r4,r5,r6=r
    f,e=p['f'],p['e']; t=_time(f,3,2200); out=np.zeros_like(t); v1=np.zeros_like(t); v2=np.zeros_like(t); selected=np.zeros_like(t); partial=np.zeros_like(t)
    ns=np.array([1]) if p['signal']=='sinus' else np.arange(1,2*int(p['harmonics']),2)
    coeff=np.full(len(ns),e) if p['signal']=='sinus' else 4*e/(np.pi*ns)
    omegas=2*np.pi*f*ns; hs=state_transfer(omegas,h0,w0,q); inside=(omegas>=low)&(omegas<=high)
    for n,amp,omega,h,keep in zip(ns,coeff,omegas,hs,inside):
        wave=np.exp(1j*omega*t); partial+=amp*wave.imag; contribution=amp*np.imag(h*wave); out+=contribution
        v1+=-r4/r5*contribution; v2+=amp*np.imag((-h/(1j*omega*r6*c))*wave)
        if keep: selected+=contribution
    incoming=e*np.sin(2*np.pi*f*t) if p['signal']=='sinus' else np.where(np.sin(2*np.pi*f*t)>=0,e,-e)
    freq=np.geomspace(w0/(2*np.pi*100),w0/(2*np.pi)*100,500); h=state_transfer(2*np.pi*freq,h0,w0,q)
    return result([m('Fréquence centrale',w0/(2*np.pi),'Hz'),m('Gain au centre H₀',h0),m('Facteur de qualité Q',q),m('Borne basse à −3 dB',low/(2*np.pi),'Hz'),m('Borne haute à −3 dB',high/(2*np.pi),'Hz'),m('Largeur de bande',1/(2*np.pi*r2*c),'Hz'),m('Harmoniques calculées dans la bande',int(sum(inside)))],
        [chart('Créneau et sélection harmonique','Temps (ms)','Tension (V)',series('Entrée',t*1000,incoming),series('Sortie : toutes les harmoniques calculées',t*1000,out),series('Approximation : harmoniques dans la bande',t*1000,selected)),
         chart('Tensions internes du filtre','Temps (ms)','Tension (V)',series('vₛ₁',t*1000,v1),series('vₛ₂',t*1000,v2)),
         chart('Spectre analytique calculé','Fréquence (Hz)','Amplitude crête (V)',series('Entrée',f*ns,coeff),series('Sortie',f*ns,coeff*abs(hs)),style='bars')]+_bode(freq,h),
        curve_scene('Trois ALI, deux tensions internes',t*1000,[('Sortie',out),('État vₛ₁',v1),('État vₛ₂',v2)],'Temps (ms)','V','La première contre-réaction associe R₂ et C ; le troisième ALI intègre la sortie. Deux condensateurs ont la même capacité.',{'type':'filter','mode':'state','resistors':r,'c':c,'f0':w0/(2*np.pi),'q':q}),
        ['Les trois sorties vérifient vₛ = −(R₅/R₄)vₛ₁ = −R₆C dvₛ₂/dt.',
         'La loi des nœuds du premier ALI donne (R₂/R₁)vₑ + (R₂/R₃)vₛ₂ = −(vₛ₁ + R₂C dvₛ₁/dt).',
         'En régime sinusoïdal : H(jω) = H₀/[1 + jQ(ω/ω₀ − ω₀/ω)], H₀ = R₂R₅/(R₁R₄), ω₀ = √[R₅/(R₃R₄R₆)]/C, Q = R₂Cω₀.',
         'Le créneau alternatif impair de crête E a Aₖ = 4E/(πk) pour k impair, et Aₖ = Bₖ = 0 pour k pair. Chaque terme de sortie garde son gain et sa phase propres.',
         'La largeur exacte vaut Δω = ω₀/Q = 1/(R₂C). La courbe limitée à la bande supprime volontairement les termes hors bande : elle n’est qu’une approximation de la sortie.'],
        ['Trois ALI idéaux en régime linéaire, deux capacités identiques et sortie non chargée ; des tensions internes élevées peuvent invalider cette hypothèse dans un montage réel.',
         'Régime périodique établi sans transitoire. Le spectre du créneau possède une infinité de termes : le calcul en garde le nombre choisi, avec leurs coefficients exacts. La discontinuité du créneau conserve le phénomène de Gibbs dans sa reconstruction.'])


def transistor_dc(p):
    vcc=p['vcc']; rb1,rb2,rc,re=[p[k]*1000 for k in ('rb1','rb2','rc','re')]; beta=p['beta']; vbe=0.7
    vth=vcc*rb1/(rb1+rb2); rth=rb1*rb2/(rb1+rb2)
    ib=max((vth-vbe)/(rth+(beta+1)*re),0); ic=beta*ib; ve=(beta+1)*ib*re; vc=vcc-ic*rc
    regime='actif' if ib>0 else 'bloqué'
    if ib>0 and vc-ve<0.2:
        ve=((vcc-0.2)/rc+(vth-vbe)/rth)/(1/rc+1/rth+1/re)
        ib=max((vth-vbe-ve)/rth,0); ic=max((vcc-ve-0.2)/rc,0); vc=ve+0.2; regime='saturé'
    return vth,rth,ib,ic,ve,vc,regime


def transistor_polarisation(p):
    vth,rth,ib,ic,ve,vc,regime=transistor_dc(p); beta=p['beta']; rc,re,rg,rl=[p[k]*1000 for k in ('rc','re','rg','rl')]
    c1,ce=p['c1']*1e-6,p['ce']*1e-6; f=p['f']; gm=ic/0.02585 if regime=='actif' else 0
    rpi=beta/gm if gm else 0; load=rc*rl/(rc+rl)
    def response(freq):
        if not gm: return np.zeros_like(np.asarray(freq),dtype=complex)
        s=2j*np.pi*np.asarray(freq); ze=re/(1+s*re*ce) if p['bypass']=='oui' else np.full_like(s,re)
        ztr=rpi+(beta+1)*ze; zin=rth*ztr/(rth+ztr)
        return -beta*load/ztr*zin/(rg+1/(s*c1)+zin)
    hf=response(f); t=_time(f,3); u=p['e']*np.sin(2*np.pi*f*t)
    variation=p['e']*np.imag(hf*np.exp(2j*np.pi*f*t)); predicted=vc+variation
    low=min(p['vcc'],ve+0.2); y=np.clip(predicted,low,p['vcc']) if regime=='actif' else np.full_like(t,vc)
    freq=np.geomspace(0.1,1e6,500); h=response(freq)
    return result([m('Tension de Thévenin de base',vth,'V'),m('Courant de base',ib*1e6,'µA'),m('Courant de collecteur',ic*1000,'mA'),m('Tension de collecteur au repos',vc,'V'),m('Tension collecteur–émetteur au repos',vc-ve,'V'),m('Régime au repos',regime),m('Gain petit signal à f',float(abs(hf))),m('Transconductance (0 hors régime actif)',gm*1000,'mS')],
        [chart('Tension de sortie autour du point de repos','Temps (ms)','Tension (V)',series('Prédiction petit signal',t*1000,predicted),series('Repère des limites de fonctionnement',t*1000,y)),
         chart('Petites variations autour du repos','Temps (ms)','Variation de tension (V)',series('Entrée',t*1000,u),series('Collecteur',t*1000,variation))]+_bode(freq,h,'Modèle en basses fréquences'),
        curve_scene('Polariser avant d’amplifier',t*1000,[('Entrée, variation',u),('Collecteur, variation',variation)],'Temps (ms)','V','Le pont de base fixe le repos. Le condensateur de liaison bloque la composante continue du générateur.',{'type':'ali','mode':'transistor','vcc':p['vcc'],'vc':vc,'ve':ve,'regime':regime}),
        ['Remplacer le pont de base par Vth = Vcc Rb₁/(Rb₁ + Rb₂) et Rth = Rb₁Rb₂/(Rb₁ + Rb₂).',
         'En régime actif, Ib = (Vth − 0,7 V)/[Rth + (β + 1)Re], Ic = βIb, Ve = (β + 1)IbRe et Vc = Vcc − RcIc.',
         'Vérifier le régime : blocage si le pont ne peut polariser la jonction ; saturation si Vc − Ve < 0,2 V. En saturation, résoudre les courants avec Vbe = 0,7 V et Vce = 0,2 V.',
         'En régime actif seulement, gm = Ic/Uₜ et rπ = β/gm. La résistance dynamique collecteur–émetteur est ici infinie.',
         'Le découplage réduit l’impédance d’émetteur en alternatif et augmente le gain. Le condensateur d’entrée et la résistance du générateur influencent aussi les basses fréquences.'],
        ['Prolongement accompagné hors du programme de physique PSI/PT : le transistor amplificateur est étudié par un modèle fourni, sans le confondre avec sa fonction d’interrupteur en sciences industrielles.',
         'NPN, Uₜ = 25,85 mV, Vbe constant au repos et effet Early omis. Les capacités internes du transistor sont ignorées : la réponse affichée n’est pas un modèle de haute fréquence.',
         'Le petit signal n’est calculé qu’en régime actif. Le tracé limité est un repère quasi statique de perte de validité, pas un modèle dynamique du transistor saturé ; la charge alternative ne modifie pas le point de repos.'])


COMPUTE={name:globals()[name] for name in ('ali_gain_bande','suiveur_cascade','sommateur_inverseur','integrateur_derivateur','schmitt_trigger','astable','wien','redresseur_precision','filtre_etat','transistor_polarisation')}
