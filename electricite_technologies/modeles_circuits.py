"""Modèles de circuits. Les états des diodes et les bilans suivent Kirchhoff."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, result, curve_scene, integrate

PI = np.pi

def _scene(title,x,curves,xlabel,ylabel,description,kind,**apparatus):
    return curve_scene(title,x,curves,xlabel,ylabel,description,dict(type=kind,**apparatus))

def _phasor(z):
    return f'{z.real:.5g} {z.imag:+.5g} j'

def bridge_values(E,R1,R2,R3,R4,meter=np.inf):
    """A à E, C à 0; B entre R1/R2, D entre R3/R4; sortie B−D."""
    vb=E*R2/(R1+R2); vd=E*R4/(R3+R4)
    rth=R1*R2/(R1+R2)+R3*R4/(R3+R4)
    uopen=vb-vd
    u=uopen/(1+rth/meter)
    return vb,vd,uopen,u,rth

def pont_wheatstone(p):
    E,R1,R2,R3,R4=(p[k] for k in ('E','R1','R2','R3','R4'))
    meter=p['meter']*1000
    vb,vd,uo,u,rth=bridge_values(E,R1,R2,R3,R4,meter)
    balanced=R2*R3/R1
    scan=np.linspace(.5*balanced,1.5*balanced,301)
    open_curve=E*(R2/(R1+R2)-scan/(R3+scan))
    loaded=open_curve/(1+(R1*R2/(R1+R2)+R3*scan/(R3+scan))/meter)
    sensitivity=-E*R3/(R3+balanced)**2
    return result([metric('Tension UBD mesurée',u,'V'),metric('Tension UBD à vide',uo,'V'),metric('R₄ à l’équilibre',balanced,'Ω'),metric('Résistance de Thévenin vue de B–D',rth,'Ω'),metric('Sensibilité à l’équilibre',1000*sensitivity,'mV/Ω')],
        [chart('Détecter le passage par zéro','R₄ (Ω)','UBD (V)',series('Voltmètre idéal',scan,open_curve),series('Voltmètre réel',scan,loaded))],
        _scene('Un détecteur entre les points milieux',scan,[('UBD à vide',open_curve),('UBD mesurée',loaded)],'R₄ (Ω)','UBD (V)','A alimente les branches A–B–C et A–D–C; le voltmètre mesure VB−VD.','bridge',nodes=['A','B','C','D'],labels=[f'R₁={R1:g} Ω',f'R₂={R2:g} Ω',f'R₃={R3:g} Ω',f'R₄={R4:g} Ω'],values={'E':E,'UBD':u},connections=['A–R₁–B–R₂–C','A–R₃–D–R₄–C','voltmètre B–D']),
        ['Prendre VC=0 et VA=E. Un voltmètre idéal ne fait circuler aucun courant entre B et D.',f'Les diviseurs donnent VB={vb:.6g} V et VD={vd:.6g} V. UBD=E(R₂R₃−R₁R₄)/[(R₁+R₂)(R₃+R₄)].','L’équilibre est R₂R₃=R₁R₄. Une résistance de voltmètre finie atténue la tension, mais ne déplace pas ce zéro.'],
        ['Résistors ohmiques, alimentation idéale; voltmètre représenté par sa résistance d’entrée. Les indices suivent les branches explicitement dessinées.'])

def line_values(p):
    f=p['f']*1e6; w=2*PI*f; L=p['L']*1e-6; C=p['C']*1e-12
    R=p['R']*1e-3; G=p['G']*1e-6; d=p['length']; zload=p['load']
    z0=np.sqrt((R+1j*w*L)/(G+1j*w*C)); gamma=np.sqrt((R+1j*w*L)*(G+1j*w*C))
    reflection=(zload-z0)/(zload+z0)
    x=np.linspace(0,d,401)
    vp=p['E']/(1+reflection*np.exp(-2*gamma*d))
    forward=vp*np.exp(-gamma*x); backward=vp*reflection*np.exp(-gamma*(2*d-x))
    v=forward+backward; i=(forward-backward)/z0
    power=.5*np.real(v*np.conj(i))
    return x,v,i,power,z0,gamma,reflection

def ligne_transmission(p):
    x,v,i,power,z0,gamma,refl=line_values(p); zin=v[0]/i[0]
    w=2*PI*p['f']*1e6; phase=np.unwrap(np.angle(v))*180/PI
    return result([metric('Impédance caractéristique',_phasor(z0),'Ω'),metric('Impédance d’entrée',_phasor(zin),'Ω'),metric('Module de la réflexion à la charge',abs(refl)),metric('Atténuation par mètre',gamma.real,'Np/m'),metric('Retard de phase à travers la ligne',gamma.imag*p['length']/w*1e9,'ns'),metric('Pertes dans la ligne',power[0]-power[-1],'W')],
        [chart('Amplitude de tension','Position x (m)','Amplitude (V)',series('|V(x)|',x,abs(v))),chart('Phase de tension','Position x (m)','Phase (°)',series('arg V(x)',x,phase)),chart('Puissance active transmise','Position x (m)','P (W)',series('½ Re(V I*)',x,power))],
        _scene('Ondes progressive et réfléchie',x,[('Amplitude |V|',abs(v))],'Position (m)','Amplitude (V)','Le générateur impose la tension à x=0; la résistance termine le câble à x=d.','line',labels=[f'd={p["length"]:g} m',f'charge={p["load"]:g} Ω'],values={'reflection':abs(refl),'powerIn':power[0],'powerOut':power[-1]}),
        ['Par mètre, la branche série a l’impédance R+jωL et la branche parallèle l’admittance G+jωC.','Définir γ=√[(R+jωL)(G+jωC)] et Z₀=√[(R+jωL)/(G+jωC)]. Les racines sont prises avec atténuation positive.','À la charge, Γ=(Zcharge−Z₀)/(Zcharge+Z₀). Combiner V⁺e^(−γx) et V⁻e^(γx), puis utiliser I=(Vprogressive−Vréfléchie)/Z₀.','Calculer la puissance active à partir des amplitudes crêtes : P=½Re(VI*). Sa diminution correspond aux pertes R|I|²/2+G|V|²/2 par mètre.'],
        ['Ligne uniforme RLGC et régime sinusoïdal établi. L et C sont des paramètres par unité de longueur; cette modélisation distribuée prolonge le modèle de circuit localisé.'])

def rlc_step(E,R,L,C,t):
    """uC(0)=0 et i(0)=0, expression stable dans les trois régimes."""
    t=np.asarray(t); a=R/(2*L); w0=1/math.sqrt(L*C); disc=a*a-w0*w0
    if abs(disc)<1e-9*w0*w0:
        decay=np.exp(-a*t); u=E*(1-(1+a*t)*decay); du=E*a*a*t*decay
    elif disc<0:
        wd=math.sqrt(-disc); decay=np.exp(-a*t)
        u=E*(1-decay*(np.cos(wd*t)+a/wd*np.sin(wd*t)))
        du=E*w0*w0/wd*decay*np.sin(wd*t)
    else:
        root=math.sqrt(disc); r1=-w0*w0/(a+root); r2=-a-root
        e1=np.exp(r1*t); e2=np.exp(r2*t)
        u=E*(1-(r2*e1-r1*e2)/(r2-r1)); du=-E*r1*r2*(e1-e2)/(r2-r1)
    return u,C*du

def rlc_transitoire(p):
    E=p['E']; R=p['R']; L=p['L']*.001; C=p['C']*1e-6
    w0=1/math.sqrt(L*C); a=R/(2*L); zeta=a/w0
    slow=a if zeta<=1 else w0*w0/(a+math.sqrt(a*a-w0*w0))
    end=min(9/max(slow,1e-12),30*2*PI/w0) if zeta<1 else 9/max(slow,1e-12)
    t=np.linspace(0,end,2401)
    u,i=rlc_step(E,R,L,C,t); ec=.5*C*u*u; el=.5*L*i*i
    work=E*C*u; heat=work-ec-el
    regime='pseudo-périodique' if zeta<1-1e-8 else ('critique' if zeta<1+1e-8 else 'apériodique')
    return result([metric('Régime',regime),metric('Fréquence propre',w0/(2*PI),'Hz'),metric('Résistance critique',2*math.sqrt(L/C),'Ω'),metric('Rapport d’amortissement ζ',zeta),metric('Maximum de uC',np.max(u),'V'),metric('Énergie stockée à la fin affichée',ec[-1]+el[-1],'J'),metric('Énergie dissipée',heat[-1],'J')],
        [chart('Tension du condensateur','Temps (ms)','uC (V)',series('uC',1000*t,u),series('Échelon E',1000*t,np.full_like(t,E))),chart('Courant dans la maille','Temps (ms)','i (A)',series('i=C duC/dt',1000*t,i)),chart('Bilan d’énergie','Temps (ms)','Énergie (mJ)',series('Condensateur',1000*t,1000*ec),series('Bobine',1000*t,1000*el),series('Dissipation cumulée',1000*t,1000*heat),series('Travail fourni',1000*t,1000*work))],
        _scene('Échange entre stockage et dissipation',1000*t,[('uC',u),('E',np.full_like(t,E))],'Temps (ms)','Tension (V)','Dans la maille série, le courant et la tension du condensateur restent continus à la commutation.','circuit',topology='series_rlc',labels=[f'R={R:g} Ω',f'L={p["L"]:g} mH',f'C={p["C"]:g} µF'],values={'E':E}),
        ['Écrire E=Ri+L di/dt+uC et i=C duC/dt : LC uC″+RC uC′+uC=E.','Poser ω₀=1/√(LC), ζ=R√(C/L)/2. Le signe de ζ²−1 distingue les trois régimes.','Utiliser uC(0)=0 et i(0)=0. La durée suit le pôle lent et montre au plus trente périodes propres pour les faibles amortissements.', 'Multiplier la loi des mailles par i : Ei=Ri²+d(Li²/2+CuC²/2)/dt. Le travail reçu est EC uC.'],
        ['Échelon idéal, composants linéaires, condensateur déchargé et courant initial nul. R comprend toute résistance série.'])

def resonance_impedance(p):
    R=p['R']; L=p['L']*.001; C=p['C']*1e-6; U=p['U']; w0=1/math.sqrt(L*C); f0=w0/(2*PI)
    f=np.geomspace(f0/30,30*f0,801); z=R+1j*(2*PI*f*L-1/(2*PI*f*C)); current=U/abs(z)
    fc=f0*p['ratio']; wc=2*PI*fc; zc=R+1j*(wc*L-1/(wc*C)); ic=U/zc
    t=np.linspace(0,2/fc,501); ut=math.sqrt(2)*U*np.cos(wc*t); it=math.sqrt(2)*abs(ic)*np.cos(wc*t+np.angle(ic)); pw=ut*it
    Q=w0*L/R; bandwidth=R/(2*PI*L)
    return result([metric('Fréquence de résonance en intensité',f0,'Hz'),metric('Facteur de qualité Q',Q),metric('Largeur à mi-puissance',bandwidth,'Hz'),metric('Courant efficace à la fréquence choisie',abs(ic),'A'),metric('Phase du courant par rapport à la tension',np.angle(ic)*180/PI,'°'),metric('Puissance active',R*abs(ic)**2,'W')],
        [chart('Résonance en courant','Fréquence (Hz)','Ieff (A)',series('Courant',f,current),x_scale='log'),chart('Phase du courant','Fréquence (Hz)','Phase (°)',series('arg I−arg U',f,-np.angle(z)*180/PI),x_scale='log'),chart('Puissance instantanée','Temps (ms)','p (W)',series('u(t)i(t)',1000*t,pw))],
        _scene('Comparer tension et courant ramené à une tension',1000*t,[('u(t)',ut),('R i(t)',R*it)],'Temps (ms)','Tension (V)','R i(t) représente le courant sur la même échelle de tension; les phases sont conservées.','circuit',topology='series_rlc',labels=[f'R={R:g} Ω',f'L={p["L"]:g} mH',f'C={p["C"]:g} µF'],values={'frequency':fc,'Q':Q}),
        ['En valeurs efficaces complexes : Z=R+j(ωL−1/(ωC)) et I=U/Z.','À ω₀, les réactances s’annulent. L’intensité efficace est U/R et la tension est en phase avec le courant.','La phase du courant est −arg Z. La puissance moyenne est R Ieff², indépendamment de l’oscillation de la puissance instantanée.','Les fréquences de mi-puissance vérifient |ωL−1/(ωC)|=R; leur différence vaut R/(2πL).'],
        ['RLC série et tension efficace imposée constante pendant le balayage. La résonance affichée concerne le courant; la tension du condensateur peut avoir son maximum ailleurs.'])

def impedance_values(p):
    w=2*PI*p['f']; z=complex(p['R'])
    if 'L' in p['kind']: z+=1j*w*p['L']*.001
    if 'C' in p['kind']: z+=1/(1j*w*p['C']*1e-6)
    ys=1/(p['rin']*1000)+1j*w*p['cin']*1e-12
    zp=1/(1/z+ys); r0=p['ref']; zin=1/(1/(r0+zp)+ys)
    v1=p['E']*zin/(p['source']+zin); v2=v1*zp/(r0+zp)
    h=1/(1+1j*p['f']/(p['band']*1000)); m1=v1*h; m2=v2*h
    estimate=r0*m2/(m1-m2); corrected=1/(1/estimate-ys)
    return z,zp,v1,v2,m1,m2,estimate,corrected

def mesure_impedance(p):
    z,zp,v1,v2,m1,m2,estimate,corrected=impedance_values(p)
    f=p['f']; t=np.linspace(0,2/f,601); w=2*PI*f
    a=np.real(m1*np.exp(1j*w*t)); b=np.real(m2*np.exp(1j*w*t)); ideal=np.real(v2*np.exp(1j*w*t))
    relative=p['unc']*.01; stdz=abs(estimate)*relative*math.sqrt(2)*abs(np.real(m1/(m1-m2)))
    delay=(np.angle(m1)-np.angle(m2))/w
    return result([metric('Impédance du dipôle seul',_phasor(z),'Ω'),metric('Impédance obtenue sans correction',_phasor(estimate),'Ω'),metric('Impédance corrigée de la voie 2',_phasor(corrected),'Ω'),metric('Biais de module dû à la charge',100*(abs(estimate)/abs(z)-1),'%'),metric('Incertitude-type de module, lecture seule',stdz,'Ω'),metric('Déphasage voie 2 − voie 1',np.angle(m2/m1)*180/PI,'°'),metric('Retard voie 2 sur voie 1',delay*1e6,'µs')],
        [chart('Lecture à l’oscilloscope','Temps (ms)','Tension (V)',series('Voie 1 : entrée mesurée',1000*t,a),series('Voie 2 : sortie mesurée',1000*t,b),series('Sortie avant limitation de bande',1000*t,ideal))],
        _scene('Deux voies autour du résistor de référence',1000*t,[('Voie 1',a),('Voie 2',b)],'Temps (ms)','Tension (V)','La différence des voies mesure la tension du résistor R₀. Chaque voie possède sa propre charge d’entrée.','circuit',topology='impedance_measure',labels=[f'GBF : Rs={p["source"]:g} Ω',f'R₀={p["ref"]:g} Ω',f'Dipôle {p["kind"]}',f'Voies : {p["rin"]:g} kΩ // {p["cin"]:g} pF'],values={'Z':abs(z),'estimate':abs(estimate)}),
        ['Noter V₁ l’amplitude complexe à l’entrée de R₀ et V₂ celle aux bornes du dipôle. Le courant dans R₀ vaut (V₁−V₂)/R₀.','La formule Zmes=R₀V₂/(V₁−V₂) mesure le parallèle du dipôle et de la voie 2; elle ne mesure pas directement le dipôle seul.','Avec Yvoie=1/Rentrée+jωCentrée, retrouver Z=1/(1/Zmes−Yvoie). La résistance du GBF modifie les amplitudes effectivement appliquées.','Les deux voies ont ici la même fonction H=1/(1+jf/fb) : elle s’annule dans le rapport, mais réduit la lisibilité. L’incertitude affichée propage des lectures d’amplitude indépendantes, avec phase et R₀ supposées connues.'],
        ['Régime sinusoïdal établi; voies identiques modélisées par Rentrée // Centrée et une réponse du premier ordre. Masse commune. Une différence de bande passante ou une incertitude de phase demanderait une propagation supplémentaire.'])

def pont_graetz(p):
    E=p['peak']; f=p['f']; R=p['R']; vd=p['drop']; t=np.linspace(0,2/f,1601)
    u=E*np.sin(2*PI*f*t); bridge=np.maximum(abs(u)-2*vd,0); center=np.maximum(abs(u)-vd,0); i=bridge/R
    mean=integrate(bridge,t)/(t[-1]-t[0]); rms=math.sqrt(integrate(bridge**2,t)/(t[-1]-t[0])); input_i=np.sign(u)*i
    loss=2*vd*mean/R; loadpower=rms*rms/R
    return result([metric('Tension moyenne du pont',mean,'V'),metric('Tension efficace du pont',rms,'V'),metric('Puissance dans la charge',loadpower,'W'),metric('Pertes dans les diodes du pont',loss,'W'),metric('Fréquence de l’ondulation',2*f,'Hz'),metric('Courant efficace dans la charge',rms/R,'A')],
        [chart('Pont et point milieu','Temps (ms)','Tension (V)',series('Tension alternative',1000*t,u),series('Pont de Graetz',1000*t,bridge),series('Point milieu, même crête par demi-enroulement',1000*t,center)),chart('Courants du pont','Temps (ms)','Courant (A)',series('Charge',1000*t,i),series('Source alternative',1000*t,input_i))],
        _scene('Le courant traverse toujours la charge dans le même sens',1000*t,[('Alternative',u),('Charge du pont',bridge)],'Temps (ms)','Tension (V)','uAB>0 : D₁ et D₄ conduisent; uAB<0 : D₂ et D₃ conduisent, sous réserve du seuil.','circuit',topology='graetz',labels=['D₁','D₂','D₃','D₄',f'R={R:g} Ω'],values={'diodeDrop':vd}),
        ['Pour une paire conductrice, écrire |u|=uR+2Vd et iR=uR/R. Si |u|≤2Vd, les quatre diodes sont bloquées.', 'Le pont donne uR=max(|u|−2Vd,0). Avec des diodes idéales : ⟨uR⟩=2E/π et Ueff=E/√2.','Dans un redresseur à point milieu, une seule diode conduit par alternance. À même crête E de chaque demi-enroulement : uR=max(|u|−Vd,0).','Vérifier la puissance source : ⟨u isource⟩=⟨uR²/R⟩+2Vd⟨iR⟩.'],
        ['Charge résistive sans condensateur. Le point milieu utilise deux demi-enroulements opposés, chacun de crête E; la comparaison ne suppose pas la même quantité de cuivre.'])

def doubler_states(p,points=2048,periods=10):
    """Delon, Euler implicite et complémentarité de chaque diode à chaque pas."""
    E=p['peak']; f=p['f']; c1=p['C1']*1e-6; c2=p['C2']*1e-6; R=p['load']; rs=p['source']; vd=p['drop']
    dt=1/(f*points); count=points*periods; t=np.arange(count+1)*dt
    v1=np.zeros(count+1); v2=v1.copy(); id1=v1.copy(); id2=v1.copy()
    gload=1/R; gs=1/rs; a1=c1/dt; a2=c2/dt
    for k in range(1,count+1):
        u=E*math.sin(2*PI*f*(t[k]-dt/2)); e1=u-vd; e2=-u-vd
        for s1,s2 in ((0,0),(1,0),(0,1),(1,1)):
            g1=s1*gs; g2=s2*gs; m11=a1+gload+g1; m22=a2+gload+g2
            b1=a1*v1[k-1]+g1*e1; b2=a2*v2[k-1]+g2*e2; det=m11*m22-gload*gload
            x=(m22*b1-gload*b2)/det; y=(m11*b2-gload*b1)/det
            if (e1-x>=-1e-9 if s1 else e1-x<=1e-9) and (e2-y>=-1e-9 if s2 else e2-y<=1e-9):
                v1[k]=x; v2[k]=y; id1[k]=g1*max(e1-x,0); id2[k]=g2*max(e2-y,0); break
        else: raise ArithmeticError('État des diodes introuvable.')
    return t,v1,v2,id1,id2

def doubleur_tension(p):
    t,a,b,i1,i2=doubler_states(p); v=a+b; n=2048; tail=slice(-n-1,None); tt=t[tail]; vt=v[tail]
    mean=integrate(vt,tt)/(tt[-1]-tt[0]); ripple=np.ptp(vt); u=p['peak']*np.sin(2*PI*p['f']*t)
    show=slice(None,None,8)
    return result([metric('Tension moyenne de sortie, dernière période',mean,'V'),metric('Ondulation crête à crête',ripple,'V'),metric('Limite idéale à vide',2*max(p['peak']-p['drop'],0),'V'),metric('Puissance moyenne reçue par la charge',integrate(vt*vt/p['load'],tt)/(tt[-1]-tt[0]),'W'),metric('Écart entre les deux dernières périodes',abs(mean-integrate(v[-2*n-1:-n],t[-2*n-1:-n])*p['f']),'V')],
        [chart('Démarrage et charge alternée','Temps (ms)','Tension (V)',series('C₁',1000*t[show],a[show]),series('C₂',1000*t[show],b[show]),series('Sortie : uC₁+uC₂',1000*t[show],v[show])),chart('Courants de recharge','Temps (ms)','Courant (A)',series('Diode supérieure',1000*t[show],i1[show]),series('Diode inférieure',1000*t[show],i2[show]))],
        _scene('Deux réservoirs chargés sur des alternances opposées',1000*t[show],[('uC₁',a[show]),('uC₂',b[show]),('Sortie',v[show])],'Temps (ms)','Tension (V)','Le point milieu des condensateurs est relié à un pôle de la source; la charge est branchée entre les deux extrémités.','circuit',topology='delon',labels=[f'C₁={p["C1"]:g} µF',f'C₂={p["C2"]:g} µF',f'Charge={p["load"]:g} Ω'],values={'output':mean}),
        ['Définir uC₁=Vhaut−Vmilieu et uC₂=Vmilieu−Vbas. La charge reçoit leur somme et absorbe iR=(uC₁+uC₂)/R.','La diode supérieure conduit si u−Vd dépasse uC₁; la diode inférieure conduit si −u−Vd dépasse uC₂. Les courants conduits restent positifs.','Écrire C₁uC₁′=iD₁−iR et C₂uC₂′=iD₂−iR. Une diode bloquée ne recharge pas son condensateur; la charge le décharge néanmoins.','À vide, chaque condensateur tend vers E−Vd. Sous charge, résistance source et décharge entre recharges réduisent la moyenne et créent l’ondulation.'],
        ['Doubleur de Delon, diodes à seuil constant et résistance source explicite. Les condensateurs sont initialement déchargés. Dix périodes sont calculées; l’écart affiché indique si l’établissement reste incomplet.'])

def diode_rc_states(p,points=2048,periods=8):
    f=p['f']; E=p['peak']; R=p['R']; C=p['C']*1e-6; rs=p['source']; vd=p['drop']; dt=1/(f*points)
    t=np.arange(periods*points+1)*dt; u=E*np.sin(2*PI*f*t); v=np.zeros_like(t); ids=np.zeros_like(t)
    decay_off=math.exp(-dt/(R*C)); tau_on=C/(1/R+1/rs); decay_on=math.exp(-dt/tau_on)
    for k in range(1,len(t)):
        midpoint=E*math.sin(2*PI*f*(t[k]-.5*dt)); off=v[k-1]*decay_off
        eq=(midpoint-vd)*R/(R+rs); on=eq+(v[k-1]-eq)*decay_on
        v[k]=max(off,on); ids[k]=max((midpoint-vd-v[k])/rs,0)
    return t,u,v,ids

def diode_rc(p):
    t,u,v,ids=diode_rc_states(p); n=2048; tail=slice(-n-1,None); tt=t[tail]; vv=v[tail]; show=slice(None,None,8)
    avg=integrate(vv,tt)*p['f']; frac=np.count_nonzero(ids[-n:]>1e-8)/n
    return result([metric('Constante de décharge RC',p['R']*p['C']*1e-6,'s'),metric('Tension moyenne, dernière période',avg,'V'),metric('Ondulation crête à crête',np.ptp(vv),'V'),metric('Fraction de période en conduction',100*frac,'%'),metric('Courant de recharge maximal',max(ids),'A')],
        [chart('Tension source et sortie','Temps (ms)','Tension (V)',series('Source',1000*t[show],u[show]),series('Condensateur et résistance',1000*t[show],v[show])),chart('Conduction sur la dernière période','Temps (ms)','Courant (A)',series('Diode',1000*tt,ids[tail]),series('Résistance',1000*tt,vv/p['R']))],
        _scene('La diode recharge; la résistance décharge',1000*t[show],[('Source',u[show]),('Sortie',v[show])],'Temps (ms)','Tension (V)','La source est une source de tension. La résistance série limite le courant de recharge et rend son calcul physique.','circuit',topology='diode_rc',labels=[f'Rs={p["source"]:g} Ω',f'C={p["C"]:g} µF',f'R={p["R"]:g} Ω'],values={'ripple':np.ptp(vv),'conduction':frac}),
        ['Orienter iD de la source vers le condensateur et uC du nœud de sortie vers la masse. La loi des nœuds donne C uC′=iD−uC/R.','Diode bloquée : iD=0 et uC décroît comme exp(−t/(RC)). Diode passante : iD=(usource−Vd−uC)/Rs≥0.','L’arrêt de conduction est déterminé par la continuité de tension et la compatibilité du courant.','Pour une source de tension idéale et une diode idéale, la conduction suit uC=usource tant que C usource′+usource/R≥0. Son arrêt est donc en général après le maximum de source.'],
        ['Source de tension sinusoïdale, résistance série non nulle, diode à seuil constant. C et R sont en parallèle. Démarrage à condensateur déchargé; huit périodes sont affichées.'])

def triphase_transformateur(p):
    U1=p['U1']; m=p['turns']; k1=math.sqrt(3) if p['primary']=='Y' else 1; k2=math.sqrt(3) if p['secondary']=='Y' else 1
    coil1=U1/k1; coil2=m*coil1; U20=k2*coil2
    Iref=p['S']*1000/(math.sqrt(3)*U20)*p['fraction']
    zload=U20/(math.sqrt(3)*Iref)*(p['pf']+1j*math.sqrt(max(1-p['pf']**2,0)))
    icoil=U20/math.sqrt(3)/(p['Rseq']+zload)
    vload=icoil*zload; I2=abs(icoil); U2=math.sqrt(3)*abs(vload)
    active=3*abs(icoil)**2*zload.real; copper=3*p['Rseq']*I2**2; losses=copper+p['P0']; eff=active/(active+losses)
    shift=30*((p['secondary']=='Y')-(p['primary']=='Y')); angle=np.array([0,-120,120])*PI/180
    t=np.linspace(0,.04,601); phases=[math.sqrt(2)*U2/math.sqrt(3)*np.cos(2*PI*50*t+a+shift*PI/180+np.angle(vload)) for a in angle]
    return result([metric('Tension d’un enroulement primaire',coil1,'V'),metric('Tension secondaire composée à vide',U20,'V'),metric('Rapport des tensions composées à vide',U20/U1),metric('Courant de ligne secondaire',I2,'A'),metric('Tension composée sous charge',U2,'V'),metric('Puissance utile',active/1000,'kW'),metric('Pertes cuivre',copper,'W'),metric('Rendement',100*eff,'%'),metric('Décalage de couplage à vide du modèle',shift,'°')],
        [chart('Tensions simples du secondaire équilibré','Temps (ms)','Tension (V)',*(series(name,1000*t,v) for name,v in zip(('vaN','vbN','vcN'),phases))),chart('Tension composée et tension simple','Temps (ms)','Tension (V)',series('vaN',1000*t,phases[0]),series('vab=vaN−vbN',1000*t,phases[0]-phases[1]))],
        _scene('Trois phases séparées de 120°',1000*t,list(zip(('vaN','vbN','vcN'),phases)),'Temps (ms)','Tension (V)','Les tensions simples sont rapportées au neutre réel en étoile, ou au neutre fictif en triangle.','phasors',topology='transformer',labels=[p['primary']+'→'+p['secondary'],f'N₂/N₁={m:g}',f'U₁={U1:g} V'],values={'lineVoltage':U2,'phaseVoltage':U2/math.sqrt(3),'phaseShift':shift,'current':I2}),
        ['En étoile, la tension d’un enroulement vaut Uligne/√3; en triangle elle vaut Uligne. Appliquer le rapport de spires à ces tensions d’enroulement.', 'Le rapport de tensions composées à vide vaut (N₂/N₁)k₂/k₁, avec k=√3 en étoile et k=1 en triangle.','Définir Iref=λSref/(√3U₂₀) et la charge étoile équivalente Zcharge=U₂₀(cosφ+j sinφ)/(√3Iref). Calculer le courant réel I₂=(U₂₀/√3)/(Rs+Zcharge) et la tension simple Ucharge=Zcharge I₂.','Les pertes cuivre valent 3Rs|I₂|² et la puissance utile 3Re(Zcharge)|I₂|². Calculer η=Pu/(Pu+Pcuivre+P₀).'],
        ['Système équilibré à 50 Hz; transformateur idéal avec résistance série ramenée à une phase étoile secondaire. Charge linéaire définie par son courant de référence à la tension à vide. Le signe du décalage correspond aux polarités choisies ici; le groupe horaire d’un appareil réel doit être précisé. Réactance de fuite et courant magnétisant non détaillés.'])

def inverter_data(E,shift,N):
    """v=+E de shift·T à T/2, −E de (1/2+shift)T à T."""
    n=np.arange(1,N+1); odd=n%2==1
    complex_coeff=np.where(odd,2*E/(1j*PI*n)*(np.exp(-2j*PI*n*shift)+1),0j)
    amplitude=abs(complex_coeff); rms=E*math.sqrt(1-2*shift); fundamental=amplitude[0]/math.sqrt(2)
    total=math.sqrt(max(rms*rms-fundamental*fundamental,0))/fundamental
    truncated=math.sqrt(np.sum(amplitude[1:]**2))/amplitude[0]
    return n,complex_coeff,amplitude,rms,fundamental,total,truncated

def onduleur_spectre(p):
    E=p['E']; f=p['f']; d=p['shift']; N=int(p['N']); n,coeff,amp,rms,fund,thd,partial=inverter_data(E,d,N)
    _,_,fullamp,_,_,fullthd,_=inverter_data(E,0,N)
    tau=np.arange(0,2,1/1200); phase=tau%1; full=np.where(phase<.5,E,-E)
    delayed=np.where((phase>=d)&(phase<.5),E,np.where(phase>=.5+d,-E,0))
    rebuilt=np.real(np.sum(coeff[:,None]*np.exp(2j*PI*n[:,None]*tau[None,:]),axis=0))
    return result([metric('Valeur efficace pleine onde',E,'V'),metric('Valeur efficace décalée',rms,'V'),metric('Fondamental décalé, valeur efficace',fund,'V'),metric('THD total pleine onde',100*fullthd,'%'),metric('THD total décalé',100*thd,'%'),metric('THD limité aux raies affichées',100*partial,'%'),metric('Dernier rang du spectre',N)],
        [chart('Commandes de l’onduleur','Temps (ms)','Tension (V)',series('Pleine onde',1000*tau/f,full),series('Commande décalée',1000*tau/f,delayed),series('Reconstruction tronquée',1000*tau/f,rebuilt)),chart('Amplitudes crêtes des harmoniques','Fréquence (Hz)','Amplitude crête (V)',series('Pleine onde',n*f,fullamp),series('Commande décalée',n*f,amp),style='bars')],
        _scene('La durée des plateaux change le spectre',1000*tau/f,[('Pleine onde',full),('Décalée',delayed)],'Temps (ms)','Tension (V)','Une commande décalée crée deux intervalles à tension nulle, sans changer la période fondamentale.','power',topology='inverter',labels=[f'E={E:g} V',f'f={f:g} Hz',f'retard={d:g} T'],values={'rms':rms,'THD':thd}),
        ['Définir δ le retard rapporté à T : v=E sur [δT,T/2[, v=−E sur [(1/2+δ)T,T[, et zéro ailleurs.','La durée non nulle est (1−2δ)T : Veff=E√(1−2δ). Pour δ=1/4 : Veff=E/√2.', 'Pour un rang n impair, l’amplitude crête vaut 4E|cos(nπδ)|/(nπ); les rangs pairs sont nuls. À δ=1/4, aucun rang impair n’est entièrement annulé.','Par Parseval : THDtotal=√(Veff²−V₁eff²)/V₁eff. Le THD du spectre tronqué ne compte que les raies affichées et sous-estime le total.'],
        ['Onduleur idéal et signal à demi-périodes opposées; ni filtrage de charge ni temps mort. Les amplitudes du spectre sont calculées à partir du signal, et non lues sur des graduations approchées.'])

def chopper_states(p,points=1200):
    E=p['E']; em=p['emf']; R=p['R']; L=p['L']*.001; f=p['f']*1000; duty=p['duty']; T=1/f; ton=duty*T; toff=(1-duty)*T
    a=math.exp(-R*ton/L); b=math.exp(-R*toff/L); ion=(E-em)/R; ioff=-em/R
    if E<=em: imin=0.; imax=0.; extinction=0.; regime='aucun courant moteur'
    else:
        continuous=(ion*(1-a)*b+ioff*(1-b))/(1-a*b)
        imin=max(continuous,0); imax=ion+(imin-ion)*a
        extinction=L/R*math.log1p(R*imax/em) if em>0 else math.inf
        regime='conduction continue' if continuous>1e-12 else 'conduction discontinue'
    t=np.linspace(0,3*T,3*points+1); tau=np.mod(t,T); on=tau<ton
    i=np.where(on,ion+(imin-ion)*np.exp(-R*tau/L),ioff+(imax-ioff)*np.exp(-R*np.maximum(tau-ton,0)/L))
    i=np.maximum(i,0) if E>em else np.zeros_like(t)
    # Hors conduction, les bornes du moteur prennent sa force électromotrice.
    voltage=np.where(on,E,np.where((tau-ton)<extinction,0,em))
    if E<=em: voltage=np.where(on,E,em)
    source_current=np.where(on,i,0); diode_current=np.where(~on,i,0)
    return t,i,voltage,source_current,diode_current,imin,imax,regime

def hacheur_mcc(p):
    t,i,u,isource,idiod,imin,imax,regime=chopper_states(p); T=1/(p['f']*1000); tail=t>=2*T; tt=t[tail]; ii=i[tail]
    im=integrate(ii,tt)/T; pin=integrate(p['E']*isource[tail],tt)/T; copper=integrate(p['R']*ii**2,tt)/T; mech=p['emf']*im
    avg_u=integrate(u[tail],tt)/T; approx=(p['duty']*p['E']-p['emf'])/p['R']
    return result([metric('Régime',regime),metric('Courant moyen',im,'A'),metric('Ondulation de courant',imax-imin,'A'),metric('Tension moyenne aux bornes du moteur',avg_u,'V'),metric('Puissance reçue de la source',pin,'W'),metric('Puissance électromécanique Eₘ⟨i⟩',mech,'W'),metric('Pertes cuivre',copper,'W'),metric('Écart du bilan de puissance, quadrature',pin-mech-copper,'W')],
        [chart('Commutation et roue libre','Temps (ms)','Tension (V)',series('Tension moteur',1000*t,u)),chart('Répartition des courants','Temps (ms)','Courant (A)',series('Induit',1000*t,i),series('Source / interrupteur',1000*t,isource),series('Diode de roue libre',1000*t,idiod))],
        _scene('La bobine conserve le courant pendant la roue libre',1000*t,[('Courant d’induit',i)],'Temps (ms)','Courant (A)','L’interrupteur alimente la charge à sa fermeture; la diode de roue libre porte le courant après ouverture, jusqu’à son éventuelle extinction.','power',topology='buck_motor',labels=[f'E={p["E"]:g} V',f'Eₘ={p["emf"]:g} V',f'R={p["R"]:g} Ω',f'L={p["L"]:g} mH'],values={'duty':p['duty'],'minimumCurrent':imin,'maximumCurrent':imax}),
        ['Interrupteur fermé : L di/dt+Ri+Eₘ=E. Interrupteur ouvert et diode conductrice : L di/dt+Ri+Eₘ=0.','À extinction, i=0 : la diode se bloque. Le courant ne devient pas négatif dans ce hacheur à un quadrant. Le calcul détermine cet instant.',f'En conduction continue seulement, ⟨u⟩=αE et ⟨i⟩=(αE−Eₘ)/R={approx:.6g} A. Une valeur négative signale que cette hypothèse doit être abandonnée.','En régime périodique, ⟨d(Li²/2)/dt⟩=0. La puissance source se répartit entre R⟨i²⟩ et Eₘ⟨i⟩. Les moyennes affichées sont obtenues par quadrature.'],
        ['Hacheur série idéal à un quadrant, diode de roue libre idéale et charge R–L–Eₘ; Eₘ est constante sur trois périodes. Le modèle décrit le courant électrique; il ne calcule pas la vitesse mécanique.'])

def puissance_values(p):
    U=p['U']; w=2*PI*p['f']; z=p['R']+1j*w*p['L']*.001
    iload=U/z; icap=1j*w*p['C']*1e-6*U; itotal=iload+icap
    complex_power=U*np.conj(itotal); optimal=(w*p['L']*.001)/(w*abs(z)**2)*1e6
    return iload,icap,itotal,complex_power,optimal

def puissances_compensation(p):
    iload,icap,itotal,S,Copt=puissance_values(p); U=p['U']; f=p['f']; w=2*PI*f; apparent=U*abs(itotal); pf=S.real/apparent
    t=np.linspace(0,2/f,801); ut=math.sqrt(2)*U*np.cos(w*t); it=math.sqrt(2)*np.real(itotal*np.exp(1j*w*t)); ict=math.sqrt(2)*np.real(icap*np.exp(1j*w*t)); ilt=math.sqrt(2)*np.real(iload*np.exp(1j*w*t))
    scan=np.linspace(0,max(500,2*Copt),401); currents=abs(iload+1j*w*scan*1e-6*U)
    return result([metric('Puissance active P',S.real,'W'),metric('Puissance réactive Q',S.imag,'var'),metric('Puissance apparente S',apparent,'VA'),metric('Facteur de puissance',pf),metric('Courant efficace de ligne',abs(itotal),'A'),metric('Courant efficace avant compensation',abs(iload),'A'),metric('Capacité de compensation exacte',Copt,'µF'),metric('Économie de courant',100*(1-abs(itotal)/abs(iload)),'%')],
        [chart('Tension et courants','Temps (ms)','Courant (A)',series('Charge RL',1000*t,ilt),series('Condensateur',1000*t,ict),series('Ligne',1000*t,it)),chart('Capacité et courant de ligne','Capacité (µF)','Ieff (A)',series('Courant de ligne',scan,currents)),chart('Puissance instantanée reçue du réseau','Temps (ms)','p (W)',series('u i',1000*t,ut*it))],
        _scene('Additionner les courants complexes',1000*t,[('Charge RL',ilt),('Condensateur',ict),('Ligne',it)],'Temps (ms)','Courant (A)','Le condensateur en parallèle fournit un courant en avance de 90°; la charge RL conserve sa tension et sa puissance active.','phasors',topology='compensation',labels=[f'Ueff={U:g} V',f'R={p["R"]:g} Ω',f'L={p["L"]:g} mH',f'C={p["C"]:g} µF'],values={'P':S.real,'Q':S.imag,'S':apparent,'powerFactor':pf}),
        ['Utiliser les valeurs efficaces complexes : Icharge=U/(R+jωL) et IC=jωCU. Le courant de ligne est leur somme.','La puissance complexe reçue est U Iligne*=P+jQ. Alors S=U|Iligne| et le facteur de puissance vaut P/S.','Le condensateur idéal reçoit une puissance active nulle et Qc=−ωCU². Annuler Qcharge+Qc donne Copt=L/[R²+(ωL)²].','Au-delà de Copt, la ligne devient capacitive; le courant remonte et peut dépasser sa valeur sans compensation. La puissance active de la charge reste constante.'],
        ['Régime sinusoïdal, charge RL série et condensateur idéal en parallèle; tension efficace imposée. Le facteur de puissance P/S égale cosφ dans ce modèle sinusoïdal. Pour un courant déformé, cette égalité ne suffit plus.'])

COMPUTE={name:globals()[name] for name in ('pont_wheatstone','ligne_transmission','rlc_transitoire','resonance_impedance','mesure_impedance','pont_graetz','doubleur_tension','diode_rc','triphase_transformateur','onduleur_spectre','hacheur_mcc','puissances_compensation')}
