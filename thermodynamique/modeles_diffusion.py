"""P23 : calculs de transfert, diffusion et productions d'entropie, sans SciPy."""
from __future__ import annotations
import math
import numpy as np
from commun import metric,series,chart,result,integrate

KB=1.380649e-23
E_CHARGE=1.602176634e-19
NA=6.02214076e23

def curve_scene(title,x,curves,xlabel,ylabel,description,apparatus=None):
    data=dict(kind='curves',title=title,description=description,x=x,
              curves=[dict(label=label,x=x,y=y) for label,y in curves],xLabel=xlabel,yLabel=ylabel)
    if apparatus is not None: data['apparatus']=apparatus
    return data

def heat_scene(title,x,y,z,xlabel,ylabel,zlabel,description,apparatus=None):
    data=dict(kind='heatmap',title=title,description=description,x=x,y=y,z=z,xLabel=xlabel,yLabel=ylabel,zLabel=zlabel)
    if apparatus is not None: data['apparatus']=apparatus
    return data

def erf_array(x):
    return np.array([math.erf(float(z)) for z in np.asarray(x).ravel()]).reshape(np.asarray(x).shape)

def erfc_array(x):
    return np.array([math.erfc(float(z)) for z in np.asarray(x).ravel()]).reshape(np.asarray(x).shape)

def fourier_barre(p):
    L,S,k,T1,T2=float(p['length']),float(p['area'])*1e-4,float(p['conductivity']),float(p['T1']),float(p['T2'])
    x=np.linspace(0,L,301); T=T1+(T2-T1)*x/L; j=k*(T1-T2)/L; P=j*S; R=L/(k*S)
    lengths=np.linspace(.05,2,201)
    return result([metric('Résistance thermique R',R,'K/W'),metric('Courant surfacique vers +x',j,'W/m²'),metric('Puissance algébrique vers +x',P,'W'),metric('Gradient de température',(T2-T1)/L,'K/m')],
        [chart('Température stationnaire entre deux thermostats','x (m)','T (°C)',series('T(x)',x,T)),chart('La puissance dépend de la géométrie','Longueur L (m)','R (K/W)',series('Résistance L/(λS)',lengths,lengths/(k*S))),chart('Courant surfacique et courant total sont distincts','x (m)','j (W/m²)',series('j constant',x,np.full_like(x,j)))],
        curve_scene('La température est linéaire, le courant est uniforme',x,[('Température',T)],'x (m)','T (°C)','Les bords sont thermostats. Le sens positif du courant est de x=0 vers x=L ; il s’inverse si T₁<T₂.',dict(type='bar',length=L,temperatures=[T1,T2],power=P)),
        ['L est la longueur, S la section et λ la conductivité. Les températures de bord sont T₁ et T₂ ; le courant positif est orienté vers +x.', 'Sans source interne et en régime permanent, le bilan local donne dj/dx=0. Fourier j=−λdT/dx conduit alors à T″=0.', 'Les deux valeurs au bord fixent T=T₁+(T₂−T₁)x/L. Le courant surfacique vaut j=λ(T₁−T₂)/L.', 'La puissance est Φ=jS et R=(T₁−T₂)/Φ=L/(λS). Quand les températures sont égales, Φ=0 mais R reste défini par la géométrie.'],
        ['Barre homogène, conductivité constante, section uniforme et faces latérales isolées.', 'Les écarts en °C et en K sont identiques ; les températures absolues sont inutiles dans cette loi linéaire.', 'La puissance est algébrique : aucune valeur absolue ne masque un transfert inversé.'])

def wall_solution(p):
    S=float(p['area']); e1,e2,k1,k2,hi,ho=(float(p[k]) for k in ('e1','e2','k1','k2','hi','ho'))
    resist=np.array([1/(hi*S),e1/(k1*S),e2/(k2*S),1/(ho*S)])
    P=(float(p['Ti'])-float(p['To']))/np.sum(resist)
    temperatures=float(p['Ti'])-P*np.concatenate(([0],np.cumsum(resist)))
    return resist,P,temperatures

def paroi_composite(p):
    R,P,T=wall_solution(p); steps=np.arange(5); thick=np.linspace(.02,.4,201)
    other=R[0]+R[1]+R[3]; power=(p['Ti']-p['To'])/(other+thick/(p['k2']*p['area']))
    percentages=100*R/np.sum(R)
    out=result([metric('Résistance totale',float(np.sum(R)),'K/W'),metric('Puissance de l’intérieur vers l’extérieur',P,'W'),metric('Flux par unité de surface',P/p['area'],'W/m²'),metric('Part de résistance dans l’isolant',float(percentages[2]),'%'),metric('Température de la surface extérieure',float(T[-2]),'°C')],
        [chart('Air, surface, interface, surface, air','Repère 0 à 4 (défini dans le tableau)','T (°C)',series('Températures de part et d’autre des résistances',steps,T)),chart('Renforcer l’isolation','Épaisseur isolante (m)','Puissance (W)',series('Toutes les autres résistances conservées',thick,power)),chart('Répartir les chutes de température','Résistance 0=air intérieur, 1=couche 1, 2=isolant, 3=air extérieur','ΔT (K)',series('ΦRᵢ',np.arange(4),P*R))],
        curve_scene('Deux couches solides et deux échanges convectifs',steps,[('Température',T)],'Repère des interfaces','T (°C)','Les abscisses repèrent les interfaces, pas des épaisseurs fictives de l’air. La même puissance traverse les quatre résistances.',dict(type='wall',thicknesses=[p['e1'],p['e2']],conductivities=[p['k1'],p['k2']],temperatures=T,power=P)),
        ['S est l’aire commune, eᵢ et λᵢ décrivent chaque couche ; hᵢ et hₑ sont les coefficients d’échange avec l’air.', 'Les résistances sont 1/(hᵢS), e₁/(λ₁S), e₂/(λ₂S) et 1/(hₑS). En régime permanent sans source, elles sont parcourues par la même puissance.', 'Additionner les résistances puis calculer Φ=(Tair,int−Tair,ext)/Rtotal. Chaque chute vaut ΦRᵢ et les températures des interfaces sont reconstruites par cumul.', 'Les contacts sont parfaits ici. Un contact imparfait ajouterait une résistance propre, plutôt que modifier arbitrairement une conductivité.'],
        ['Transfert plan unidimensionnel, coefficients constants, rayonnement omis.', 'Les coefficients h représentent les échanges avec des températures d’air imposées ; aucun profil fictif dans l’air n’est calculé.', 'Les flux peuvent être négatifs si l’air extérieur est plus chaud.'])
    out['table']=dict(headers=['Repère','Lieu','Température (°C)'],rows=[[i,label,float(T[i])] for i,label in enumerate(['Air intérieur','Surface intérieure','Interface des couches','Surface extérieure','Air extérieur'])])
    return out

def radial_resistance(ri,ro,k,h,length=1,geometry='cylinder'):
    ro=np.asarray(ro)
    if geometry=='cylinder':
        return np.log(ro/ri)/(2*math.pi*k*length)+1/(2*math.pi*ro*length*h)
    return (1/ri-1/ro)/(4*math.pi*k)+1/(4*math.pi*ro*ro*h)

def isolation_radiale(p):
    ri=p['radius']*.01; ro=ri+p['thickness']*.01; k,h,L=p['conductivity'],p['h'],p['length']; geometry=p['geometry']; dt=p['Ti']-p['To']
    critical=k/h*(2 if geometry=='sphere' else 1); R=float(radial_resistance(ri,ro,k,h,L,geometry)); P=dt/R
    baseline=dt/float(radial_resistance(ri,ri,k,h,L,geometry)); scan=np.linspace(ri,max(ro*1.1,ri*3,critical*1.5),401)
    r=np.linspace(ri,ro,301)
    if geometry=='cylinder':
        Rr=np.log(r/ri)/(2*math.pi*k*L); area=2*math.pi*r*L
    else:
        Rr=(1/ri-1/r)/(4*math.pi*k); area=4*math.pi*r*r
    T=p['Ti']-P*Rr
    return result([metric('Rayon extérieur choisi',ro,'m'),metric('Rayon critique λ/h ou 2λ/h',critical,'m'),metric('Rayon intérieur sous le rayon critique', 'oui' if ri<critical else 'non'),metric('Puissance avec isolant',P,'W'),metric('Puissance sans isolant',baseline,'W'),metric('Variation de la perte',100*(P/baseline-1),'%')],
        [chart('La perte peut d’abord croître avec le rayon extérieur','Rayon extérieur (m)','Puissance (W)',series('Conduction + convection',scan,dt/radial_resistance(ri,scan,k,h,L,geometry)),xMarker=critical,xMarkerLabel='Rayon critique'),chart('Température dans la coque','r (m)','T (°C)',series('Profil dans l’isolant',r,T)),chart('Même puissance, surface différente','r (m)','j radial (W/m²)',series('j=Φ/aire(r)',r,P/area))],
        curve_scene('Résistance radiale et surface extérieure croissante',r,[('Température',T)],'r (m)','T (°C)','Le rayon intérieur reste fixe. Le rayon critique maximise la perte seulement s’il dépasse ce rayon intérieur ; sinon toute épaisseur ajoutée réduit la perte.',dict(type='thermal',geometry=geometry,inner_radius=ri,outer_radius=ro,temperatures=[p['Ti'],float(T[-1]),p['To']],power=P)),
        ['Rᵢ est le rayon intérieur fixe, Rₑ le rayon extérieur et h la convection extérieure. Φ est la puissance radiale totale, constante.', 'Pour un cylindre, Rcond=ln(Rₑ/Rᵢ)/(2πλL) ; pour une sphère, Rcond=(1/Rᵢ−1/Rₑ)/(4πλ). Ajouter Rconv=1/(hSₑ).', 'Dériver Rtotal par rapport à Rₑ. Le minimum de résistance est en λ/h pour le cylindre et 2λ/h pour la sphère.', 'Comparer ce rayon à Rᵢ avant de conclure. La conductivité limite le passage, mais l’augmentation de surface améliore simultanément la convection.'],
        ['Rayon intérieur et température intérieure imposés ; pas de convection intérieure ni de rayonnement.', 'Cylindre long : les extrémités sont ignorées et L désigne sa longueur.', 'La température de la surface solide diffère de celle de l’air extérieur.'])

def igloo(p):
    ri=p['radius']; ro=ri+p['thickness']; k=p['conductivity']; P=p['people']*p['power']; R=(1/ri-1/ro)/(2*math.pi*k)
    Ti=p['To']+P*R; delta=p['target']-p['To']; denominator=P/(2*math.pi*k)-ri*delta
    required=ri*ri*delta/denominator if denominator>0 else 'impossible dans ce modèle pour cette puissance'
    r=np.linspace(ri,ro,301); T=p['To']+P*(1/r-1/ro)/(2*math.pi*k)
    e=np.linspace(.01,2,301); profile=p['To']+P*(1/ri-1/(ri+e))/(2*math.pi*k)
    return result([metric('Puissance disponible',P,'W'),metric('Résistance de la coque hémisphérique',R,'K/W'),metric('Température intérieure du modèle conductif',Ti,'°C'),metric('Validité de la paroi solide','fonte à intégrer : la paroi intérieure dépasse 0 °C' if Ti>0 else 'compatible avec une paroi sous 0 °C'),metric('Épaisseur pour la température visée',required,'m' if isinstance(required,float) else ''),metric('Température limite du modèle à épaisseur croissante',p['To']+P/(2*math.pi*k*ri),'°C')],
        [chart('Profil dans une coque hémisphérique','r (m)','T (°C)',series('Température stationnaire',r,T)),chart('Un bilan fixe la température intérieure','Épaisseur de la paroi (m)','T intérieure (°C)',series('Bilan Φ=P',e,profile),series('Température visée',e,np.full_like(e,p['target'])))],
        curve_scene('Bilan entre occupants et paroi',r,[('Température de la paroi',T)],'r (m)','T (°C)','R désigne le rayon intérieur ; le rayon extérieur vaut R+e. La puissance des personnes est un apport net au local.',dict(type='thermal',geometry='hemisphere',inner_radius=ri,outer_radius=ro,temperatures=[Ti,p['To']],people=p['people'],power=P)),
        ['R est le rayon intérieur, e l’épaisseur et λ la conductivité de la paroi. Chaque personne apporte la puissance nette réglée en watts.', 'Sur une hémisphère, l’aire à distance r est 2πr². Fourier et la constance de Φ donnent Rth=(1/R−1/(R+e))/(2πλ).', 'À l’équilibre Ptotal=Φ : Tint=Text+Ptotal Rth. La température n’est donc pas fixée indépendamment de la puissance et de la paroi.', 'Résoudre pour l’épaisseur demandée. Si la résistance requise dépasse la limite 1/(2πλR), aucune épaisseur finie ne convient dans cette géométrie à rayon intérieur fixé.'],
        ['Sol isolé, paroi homogène, températures de surface imposées égales à celles du local et de l’extérieur ; ventilation omise.', 'La conductivité représente le matériau choisi, neige ou glace ; les deux ne sont pas interchangeables.', 'Modèle conductif idéal à conductivité constante : fonte, humidité et échanges radiatifs ne sont pas inclus. Si la paroi intérieure dépasse 0 °C, le résultat est un calcul conditionnel, pas un équilibre stationnaire réel de neige ou de glace solide.'])

def ftcs_modes(n,fo_end,fo_step,amplitude=1,profile='two'):
    """x/L et χt/L² réduits. Ajustement du dernier pas, r réel <= fo_step."""
    x=np.linspace(0,1,n+1); dx=1/n
    steps=max(1,int(math.ceil(fo_end/(fo_step*dx*dx)))); dt=fo_end/steps; r=dt/(dx*dx)
    y=amplitude*np.sin(math.pi*x)
    if profile=='two': y+=.4*amplitude*np.sin(3*math.pi*x)
    y[[0,-1]]=0; indexes=set(np.linspace(0,steps,min(81,steps+1)).round().astype(int))
    saved=[y.copy()]; times=[0.]
    for j in range(steps):
        y[1:-1]+=r*(y[:-2]-2*y[1:-1]+y[2:]); y[[0,-1]]=0
        if j+1 in indexes: saved.append(y.copy()); times.append((j+1)*dt)
    times=np.asarray(times); saved=np.asarray(saved)
    exact=amplitude*np.exp(-math.pi**2*times[:,None])*np.sin(math.pi*x)
    if profile=='two': exact+=.4*amplitude*np.exp(-9*math.pi**2*times[:,None])*np.sin(3*math.pi*x)
    return x,times,saved,exact,r,steps

def diffusion_1d(p):
    L,D,A,n,fo=p['length'],p['D']*1e-6,p['amplitude'],int(p['N']),p['time']
    x,t,y,exact,r,steps=ftcs_modes(n,fo,p['fourier'],A,p['profile']); x*=L; t*=L*L/D
    mean=integrate(y,x)/L; exactmean=integrate(exact,x)/L
    return result([metric('Nombre de Fourier réellement utilisé',r),metric('Condition de stabilité r≤1/2','respectée' if r<=.5 else 'non respectée'),metric('Nombre de pas temporels',steps),metric('Temps physique final',float(t[-1]),'s'),metric('Erreur maximale finale',float(np.max(abs(y[-1]-exact[-1]))),'K'),metric('Énergie moyenne restante / initiale',float(mean[-1]/mean[0]))],
        [chart('Comparer un calcul stable à des modes exacts','x (m)','T (°C)',series('Initial',x,p['T0']+y[0]),series('FTCS au temps final',x,p['T0']+y[-1]),series('Modes exacts au temps final',x,p['T0']+exact[-1])),chart('Erreur de discrétisation spatiale et temporelle','x (m)','Écart (K)',series('FTCS−exact',x,y[-1]-exact[-1])),chart('L’énergie sort par les extrémités thermostatées','t (s)','Élévation moyenne (K)',series('FTCS',t,mean),series('Modes exacts, même quadrature spatiale',t,exactmean))],
        heat_scene('La barre refroidit : carte espace–temps',x,t,p['T0']+y,'x (m)','t (s)','T (°C)','Chaque ligne est un état calculé. Les deux extrémités restent à T₀ ; le mode de rang 3 disparaît neuf fois plus vite que le rang 1.',dict(type='bar',length=L,temperatures=p['T0']+y[-1])),
        ['χ est la diffusivité ; L la longueur. Le profil initial est un ou deux sinus et les températures de bord valent T₀.', 'Chaque mode sin(nπx/L) est multiplié par exp(−χn²π²t/L²). Les deux modes constituent ici une référence exacte indépendante du calcul par grille.', 'Le schéma FTCS utilise r=χΔt/Δx². Pour 0≤r≤1/2, la température suivante est une combinaison positive des trois températures voisines : aucun maximum nouveau ne doit apparaître.', 'Le programme choisit le nombre de pas pour ne pas dépasser r réglé. L’énergie de la barre diminue : les extrémités évacuent la chaleur, ce système n’est pas isolé.'],
        ['χ constant, conduction unidimensionnelle et températures de bord imposées.', 'FTCS explicite stable : seuls des nombres de Fourier inférieurs à 1/2 sont proposés.', 'La carte stocke au plus 81 états et ne présente pas tous les pas calculés comme des images indépendantes.'])

def demi_espace(p):
    D=p['D']*1e-6; C=p['capacity']*1e6; k=D*C; final=p['minutes']*60; difference=p['Ts']-p['T0']; depth=math.sqrt(D*final)
    x=np.linspace(0,8*depth,801); T=p['T0']+difference*erfc_array(x/(2*depth)); times=np.linspace(final/1000,final,501)
    flux=k*difference/np.sqrt(math.pi*D*times); energy=2*C*difference*np.sqrt(D*times/math.pi); numeric=C*float(integrate(T-p['T0'],x))
    snapshots=[final/4,final,4*final]
    return result([metric('Conductivité λ=χρc',k,'W/(m·K)'),metric('Longueur √(χt)',depth,'m'),metric('Flux à la surface au temps final',float(flux[-1]),'W/m²'),metric('Énergie reçue par unité de surface',float(energy[-1]),'J/m²'),metric('Énergie du profil, intégrale spatiale',numeric,'J/m²')],
        [chart('Une profondeur caractéristique croît comme √t','x (m)','T (°C)',*[series(f't={seconds/60:g} min',x,p['T0']+difference*erfc_array(x/(2*math.sqrt(D*seconds)))) for seconds in snapshots]),chart('Le flux est grand au début, puis décroît','t (s)','j surface (W/m²)',series('λ(Ts−T₀)/√(πχt)',times,flux)),chart('Intégrer le flux donne l’énergie reçue','t (s)','Énergie par aire (J/m²)',series('2ρc(Ts−T₀)√(χt/π)',times,energy))],
        curve_scene('Le profil de l’exercice 6 s’étend vers l’intérieur',x,[('Température au temps choisi',T)],'Profondeur x (m)','T (°C)','Le solide est semi-infini et la surface x=0 change de température à t=0. La fenêtre va jusqu’à 8√(χt), où la perturbation est négligeable.',dict(type='bar',length=float(x[-1]),temperatures=T)),
        ['χ est la diffusivité et ρc la capacité volumique ; λ=χρc. Le solide commence à T₀ et sa surface est soudain imposée à Ts.', 'La solution est T=T₀+(Ts−T₀)erfc[x/(2√(χt))]. Elle satisfait le bord, la limite profonde et l’état initial pour x>0.', 'Dériver le profil et appliquer Fourier : j(0,t)=λ(Ts−T₀)/√(πχt). Le flux diverge comme t^{−1/2}, mais cette singularité est intégrable.', 'L’énergie par aire est 2ρc(Ts−T₀)√(χt/π), obtenue soit en intégrant le flux dans le temps, soit en intégrant le profil dans l’espace.'],
        ['χ et ρc constants ; aucun changement de phase ni résistance de surface.', 'Le choc idéal crée une incompatibilité au coin x=t=0 ; les formules sont utilisées pour t>0.', 'Flux et énergie restent algébriques ; un refroidissement de surface donne des valeurs négatives.'])

def thermal_wave_parameters(D,period):
    omega=2*math.pi/period; delta=math.sqrt(2*D/omega)
    return omega,delta

def onde_thermique(p):
    period=86400 if p['period']=='day' else 365.25*86400; D=p['D']*1e-6; z=p['depth']; w,delta=thermal_wave_parameters(D,period)
    times=np.linspace(0,2*period,401); depths=np.linspace(0,max(5*delta,z*1.1),121)
    amplitude=p['amplitude']*np.exp(-depths/delta); lag=depths/(delta*w)
    chosen=p['T0']+p['amplitude']*math.exp(-z/delta)*np.cos(w*times-z/delta)
    surface=p['T0']+p['amplitude']*np.cos(w*times)
    field=p['T0']+p['amplitude']*np.exp(-depths[None,:]/delta)*np.cos(w*times[::4,None]-depths[None,:]/delta)
    return result([metric('Profondeur d’atténuation δ',delta,'m'),metric('Amplitude à la profondeur choisie',p['amplitude']*math.exp(-z/delta),'K'),metric('Retard de phase non ramené à une période',z/(delta*w)/3600,'h'),metric('Rapport amplitude / surface',math.exp(-z/delta)),metric('Période physique',period/86400,'jour(s)')],
        [chart('Le maximum arrive plus tard en profondeur','Temps / période','T (°C)',series('Surface',times/period,surface),series(f'Profondeur {z:g} m',times/period,chosen)),chart('Même longueur pour l’atténuation et le déphasage','z (m)','Amplitude (K)',series('A exp(−z/δ)',depths,amplitude)),chart('Le retard croît avec la profondeur','z (m)','Retard (h)',series('z/(δω)',depths,lag/3600))],
        heat_scene('Température du sol sur deux cycles',depths,times[::4]/period,field,'Profondeur z (m)','Temps / période','T (°C)','La couleur montre à la fois la perte d’amplitude et le retard du cycle. Il s’agit d’une solution de l’équation de diffusion en régime périodique établi.',dict(type='thermal',geometry='ground',depth=z,penetration=delta)),
        ['χ est la diffusivité, P la période et ω=2π/P. La surface est imposée à T₀+Acos(ωt).', 'Chercher une solution complexe θ(z)e^{iωt}. L’équation χθ″=iωθ impose θ=Aexp[−(1+i)z/δ], avec δ=√(2χ/ω).', 'Ainsi T=T₀+Aexp(−z/δ)cos(ωt−z/δ). Le retard du maximum vaut z/(δω) ; le déphasage doit être distingué d’un transport sans dissipation.', 'Quand la période est multipliée par un facteur q, δ est multipliée par √q. Le cycle annuel pénètre bien plus profondément que le cycle journalier.'],
        ['Sol semi-infini homogène ; régime établi après disparition du transitoire.', 'Le retard présenté n’est pas réduit modulo une période ; plusieurs cycles de phase peuvent être accumulés.', 'Une amplitude très atténuée signifie que le retard associé serait difficile à mesurer expérimentalement.'])

def slab_eigenvalues(biot,count=80):
    roots=[]
    for n in range(count):
        left=n*math.pi+1e-12; right=(n+.5)*math.pi-1e-12
        for _ in range(55):
            middle=(left+right)/2
            if middle*math.tan(middle)>biot: right=middle
            else: left=middle
        roots.append((left+right)/2)
    return np.asarray(roots)

def slab_temperature(biot,fo,coordinate=None):
    fo=np.asarray(fo,dtype=float); mu=slab_eigenvalues(biot); coef=4*np.sin(mu)/(2*mu+np.sin(2*mu))
    terms=np.exp(-fo[:,None]*mu*mu)*coef
    average=terms@(np.sin(mu)/mu); center=np.sum(terms,axis=1); surface=terms@np.cos(mu)
    average[fo==0]=1; center[fo==0]=1; surface[fo==0]=1
    if coordinate is not None:
        profile=terms@np.cos(mu[:,None]*np.asarray(coordinate)[None,:])
        profile[fo==0]=1
        return average,center,surface,profile
    return average,center,surface

def refroidissement_biot(p):
    a=p['halfwidth']*.001; k,h,C=p['conductivity'],p['h'],p['capacity']*1e6; D=k/C; Bi=h*a/k
    fo=np.linspace(0,p['time'],501); t=fo*a*a/D; mean,center,surface=slab_temperature(Bi,fo); lump=np.exp(-Bi*fo)
    xx=np.linspace(-1,1,301); final_profile=slab_temperature(Bi,np.array([p['time']]),xx)[3][0]
    excess=p['excess']; air=p['Tair']
    return result([metric('Nombre de Biot h a / λ',Bi),metric('Repère Bi<0,1','modèle uniforme favorable' if Bi<.1 else 'gradients à contrôler'),metric('Temps capacitif ρc a/h',C*a/h,'s'),metric('Temps physique final',float(t[-1]),'s'),metric('Écart maximal moyenne / modèle uniforme',float(np.max(abs(mean-lump))*excess),'K'),metric('Écart centre−surface au temps final',float((center[-1]-surface[-1])*excess),'K')],
        [chart('Trois températures dans la plaque','t (s)','T (°C)',series('Centre exact',t,air+excess*center),series('Moyenne exacte',t,air+excess*mean),series('Surface exacte',t,air+excess*surface),series('Modèle uniforme',t,air+excess*lump)),chart('Le gradient au temps sélectionné','x (mm), faces en ±a','T (°C)',series('Profil exact',xx*a*1000,air+excess*final_profile),series('Modèle uniforme',xx*a*1000,np.full_like(xx,air+excess*lump[-1]))),chart('Tester l’approximation capacitive','χt/a²','Écart moyen (K)',series('Moyenne exacte−uniforme',fo,excess*(mean-lump)))],
        curve_scene('Les faces refroidissent avant le centre',xx*a*1000,[('Plaque',air+excess*final_profile),('Uniforme',np.full_like(xx,air+excess*lump[-1]))],'Position x (mm)','T (°C)','Deux faces convectives, centre de symétrie en x=0. La longueur caractéristique V/S vaut la demi-épaisseur a.',dict(type='wall',thicknesses=[2*a],temperatures=[air+excess*surface[-1],air+excess*center[-1],air+excess*surface[-1]])),
        ['a est la demi-épaisseur, ρc la capacité volumique et h la convection sur chaque face ; χ=λ/(ρc). La plaque commence à Tair+ΔT.', 'Le modèle uniforme donne θ=e^{−ht/(ρca)}. Il suppose que les échanges extérieurs sont lents devant l’homogénéisation interne ; Bi=ha/λ compare ces résistances.', 'Pour la plaque exacte, les modes sont cos(μx/a), avec μtanμ=Bi. Leurs coefficients sont 4sinμ/(2μ+sin2μ), et chaque mode décroît comme e^{−μ²χt/a²}.', 'Comparer température centrale, moyenne et superficielle. Bi<0,1 est un repère pratique ; le graphique mesure l’écart pour les paramètres réellement choisis.'],
        ['Plaque plane infinie latéralement, propriétés constantes et air thermostaté identique sur les deux faces.', 'La référence utilise 80 modes ; l’état initial est uniforme et les profils pour t>0 satisfont la convection.', 'L’air n’est pas inclus dans la capacité thermique du solide.'])

def gaussian_heat(x,y,D,t,sigma0,energy,capacity_surface):
    variance=sigma0*sigma0+2*D*t
    return energy/(2*math.pi*capacity_surface*variance)*np.exp(-(np.asarray(x)**2+np.asarray(y)**2)/(2*variance))

def diffusion_2d(p):
    D=p['D']*1e-6; C=p['capacity']*1e6; thickness=p['thickness']*.001; Cs=C*thickness; sigma0=p['width']*.001; final=p['seconds']; Q=p['energy']
    sigma=math.sqrt(sigma0*sigma0+2*D*final); axis=np.linspace(-5*sigma,5*sigma,121); X,Y=np.meshgrid(axis,axis)
    excess=gaussian_heat(X,Y,D,final,sigma0,Q,Cs); numeric=Cs*float(integrate(integrate(excess,axis),axis))
    t=np.linspace(0,final,301); variances=sigma0*sigma0+2*D*t; r=np.linspace(0,5*sigma,301)
    return result([metric('Largeur dans chaque direction σ(t)',sigma*1000,'mm'),metric('Énergie imposée Q',Q,'J'),metric('Énergie intégrée dans la fenêtre',numeric,'J'),metric('Écart relatif de bilan sur la fenêtre',abs(numeric-Q)/Q),metric('Élévation maximale au temps final',Q/(2*math.pi*Cs*sigma*sigma),'K'),metric('Étalement radial moyen ⟨r²⟩',2*sigma*sigma*1e6,'mm²')],
        [chart('Un pic moins haut, une tache plus large','Distance au centre r (mm)','Élévation (K)',series('Initial',r*1000,gaussian_heat(r,0,D,0,sigma0,Q,Cs)),series('Temps final',r*1000,gaussian_heat(r,0,D,final,sigma0,Q,Cs))),chart('La variance croît linéairement','t (s)','Variance par direction (mm²)',series('σ₀²+2χt',t,variances*1e6)),chart('Le maximum n’est pas l’énergie totale','t (s)','Élévation centrale (K)',series('Q/(2πρceσ²)',t,Q/(2*math.pi*Cs*variances)))],
        heat_scene('Carte de température dans la plaque',axis*1000,axis*1000,p['T0']+excess,'x (mm)','y (mm)','T (°C)','La tache est calculée par la solution gaussienne exacte. La fenêtre atteint ±5σ dans chaque direction ; la différence de bilan inclut la petite queue omise et la quadrature.',dict(type='thermal',geometry='plate',width=sigma,energy=Q)),
        ['χ est la diffusivité ; e l’épaisseur et ρce la capacité par surface. L’énergie initiale Q est répartie selon une gaussienne de largeur σ₀ dans chaque direction.', 'L’équation 2D conserve la forme gaussienne avec σ²=σ₀²+2χt. L’élévation est Qexp[−(x²+y²)/(2σ²)]/(2πρceσ²).', 'La double intégrale de ρce(T−T₀) sur le plan vaut Q à tout instant. La diminution du maximum compense l’augmentation de l’aire chauffée.', 'Chaque variance vaut σ² ; la moyenne radiale ⟨r²⟩=⟨x²+y²⟩ vaut 2σ². La diffusion ajoute donc 4χt à l’étalement radial.'],
        ['Plaque mince infinie, température uniforme dans son épaisseur et aucune perte sur les faces.', 'Une gaussienne initiale de largeur non nulle évite une température infinie au temps zéro.', 'La carte porte sur le temps sélectionné ; aucune température intermédiaire fictive n’est interpolée.'])

def binomial_distribution(n,p):
    k=np.arange(n+1); probabilities=np.array([math.exp(math.lgamma(n+1)-math.lgamma(int(j)+1)-math.lgamma(n-int(j)+1)+j*math.log(p)+(n-j)*math.log1p(-p)) for j in k])
    probabilities/=np.sum(probabilities)
    return k,probabilities

def marche_aleatoire(p):
    n=int(p['N']); probability=p['p']; epsilon=p['step']*1e-6; tau=p['dt']*.001
    k,law=binomial_distribution(n,probability); positions=(2*k-n)*epsilon; mean=n*(2*probability-1)*epsilon; variance=4*n*probability*(1-probability)*epsilon*epsilon
    approx=2*epsilon/np.sqrt(2*math.pi*variance)*np.exp(-(positions-mean)**2/(2*variance))
    D=2*probability*(1-probability)*epsilon*epsilon/tau; drift=(2*probability-1)*epsilon/tau
    rng=np.random.default_rng(2718); jumps=np.where(rng.random((256,n))<probability,epsilon,-epsilon); walks=np.c_[np.zeros(256),np.cumsum(jumps,axis=1)]
    times=np.arange(n+1)*tau; empirical=np.var(walks,axis=0); theory=2*D*times
    return result([metric('Coefficient diffusif centré D',D,'m²/s'),metric('Vitesse moyenne de dérive',drift,'m/s'),metric('Moyenne exacte de la position',mean*1e6,'µm'),metric('Variance exacte de la position',variance*1e12,'µm²'),metric('Somme des probabilités binomiales',float(np.sum(law))),metric('Écart total binomiale / gaussienne sur le réseau',float(np.sum(abs(law-approx))))],
        [chart('La vraie loi et son approximation sur le réseau accessible','x (µm)','Probabilité par site',series('Binomiale exacte',positions*1e6,law),series('Gaussienne × espacement 2ε',positions*1e6,approx)),chart('La variance donne le coefficient de diffusion','t (s)','Variance centrée (µm²)',series('2Dt exact',times,theory*1e12),series('256 marches simulées',times,empirical*1e12)),chart('Une trajectoire n’est pas une moyenne','t (s)','Position (µm)',*[series(f'Marche {j+1}',times,walks[j]*1e6) for j in range(6)],series('Dérive moyenne',times,drift*times*1e6))],
        curve_scene('De sauts discrets à un nuage diffusif',positions*1e6,[('Loi binomiale',law),('Approximation gaussienne',approx)],'Position finale (µm)','Probabilité par site','Après N sauts, seuls les sites ayant la parité de N sont accessibles. Le facteur 2ε transforme la densité gaussienne en probabilité par site.',dict(type='particles',positions=np.c_[walks[:64,-1]*1e6,np.zeros(64)],unit='µm',drift=mean*1e6)),
        ['ε est la longueur d’un saut, τ sa durée et p sa probabilité vers +x. Après N pas, le nombre de sauts positifs suit une loi binomiale.', 'La position vaut (2K−N)ε ; sa moyenne est N(2p−1)ε et sa variance 4Np(1−p)ε².', 'Identifier la variance à 2Dt donne D=2p(1−p)ε²/τ. Sans biais p=1/2, D=ε²/(2τ), comme dans l’exercice 5.', 'Le biais produit en plus une dérive u=(2p−1)ε/τ. La gaussienne approxime les probabilités sur un réseau d’espacement 2ε ; ignorer la parité diviserait leur amplitude par deux.'],
        ['Sauts indépendants, paramètres constants ; loi exacte pour un nombre entier de pas.', 'Les trajectoires utilisent une graine fixe pour être reproductibles ; leurs moyennes fluctuent autour des références.', 'La limite continue exige des distances et temps grands devant un saut et sa durée.'])

def langevin_parameters(radius,viscosity,density,temperature):
    drag=6*math.pi*viscosity*radius; mass=4*math.pi*radius**3*density/3
    return KB*temperature/drag,mass/drag,mass,drag

def langevin_msd(t,D,tau):
    u=np.asarray(t)/tau; expression=u+np.expm1(-u)
    expression=np.where(u<1e-3,u*u/2-u**3/6+u**4/24,expression)
    return 2*D*tau*expression

def langevin_ensemble(D,tau,end,count=256,steps=300):
    rng=np.random.default_rng(31415); dt=end/steps; u=dt/tau; c=math.exp(-u); one=-math.expm1(-u); two=-math.expm1(-2*u)
    sv=D/tau; vv=sv*two; bracket=u-2*one+.5*two
    if u<1e-3: bracket=u**3/3-u**4/4+7*u**5/60
    xx=2*D*tau*bracket; covariance=D*one*one; cross=covariance/math.sqrt(vv); residual=max(0,xx-cross*cross)
    v=rng.normal(size=(count,2))*math.sqrt(sv); position=np.zeros_like(v); snapshots=[position.copy()]
    for _ in range(steps):
        n1=rng.normal(size=(count,2)); n2=rng.normal(size=(count,2))
        position=position+tau*one*v+cross*n1+math.sqrt(residual)*n2
        v=c*v+math.sqrt(vv)*n1; snapshots.append(position.copy())
    return np.linspace(0,end,steps+1),np.asarray(snapshots)

def brownien_langevin(p):
    radius=p['radius']*1e-9; viscosity=p['viscosity']*.001
    D,tau,mass,drag=langevin_parameters(radius,viscosity,p['density'],p['temperature']); end=tau*p['ratio'] if p['regime']=='inertial' else p['seconds']
    t,positions=langevin_ensemble(D,tau,end); exact=langevin_msd(t,D,tau); empirical=np.mean(positions[:,:,0]**2,axis=1)
    unit='nm' if p['regime']=='inertial' else 'µm'; scale=1e9 if unit=='nm' else 1e6; final=positions[-1]*scale
    return result([metric('Diffusion Stokes–Einstein D',D,'m²/s'),metric('Temps de relaxation de vitesse τᵥ',tau,'s'),metric('Durée observée / τᵥ',end/tau),metric('Déplacement quadratique moyen par direction',float(exact[-1]*scale*scale),unit+'²'),metric('Rapport MSD exact / 2Dt',float(exact[-1]/(2*D*end))),metric('Masse de la particule',mass,'kg')],
        [chart('Du régime balistique à la diffusion, par direction','t (s)',f'MSD ({unit}²)',series('Langevin exact',t,exact*scale*scale),series('256 particules simulées',t,empirical*scale*scale),series('Limite diffusive 2Dt',t,2*D*t*scale*scale)),chart('Six trajectoires dans le plan','x ('+unit+')','y ('+unit+')',*[series(f'Particule {j+1}',positions[:,j,0]*scale,positions[:,j,1]*scale) for j in range(6)]),chart('L’inertie réduit le déplacement par rapport à 2Dt','t/τᵥ','MSD / (2Dt)',series('Rapport exact',t[1:]/tau,exact[1:]/(2*D*t[1:])))],
        dict(kind='phase',title='Trajectoires browniennes bidimensionnelles',description='Les deux coordonnées sont calculées par le même processus de Langevin ; chaque variance vaut la formule 1D affichée. Les positions et vitesses sont échantillonnées par transitions gaussiennes exactes.',xLabel='x ('+unit+')',yLabel='y ('+unit+')',bounds=[float(np.min(positions[:,:,0])*scale),float(np.max(positions[:,:,0])*scale),float(np.min(positions[:,:,1])*scale),float(np.max(positions[:,:,1])*scale)],arrows=[],paths=[dict(label=f'Particule {j+1}',x=positions[:,j,0]*scale,y=positions[:,j,1]*scale) for j in range(6)],apparatus=dict(type='particles',positions=final[:64],unit=unit)),
        ['a est le rayon, η la viscosité, m la masse et T la température absolue. Le frottement de Stokes est α=6πηa ; τᵥ=m/α.', 'L’équilibre thermique donne la variance de vitesse kBT/m. La fluctuation et le frottement conduisent à D=kBT/α, sans facteur 1/2.', 'Avec x(0)=0 et une vitesse initiale à l’équilibre, ⟨x²(t)⟩=2D[t−τᵥ(1−e^{−t/τᵥ})]. À temps court, c’est (kBT/m)t² ; à temps long, c’est 2Dt.', 'Les transitions jointes de vitesse et déplacement sont gaussiennes corrélées. Le calcul utilise leur covariance exacte, même lorsque le pas dépasse largement τᵥ ; ce n’est pas un Euler instable.'],
        ['Sphère dans un fluide newtonien, frottement de Stokes, bain à température constante et absence de force extérieure.', 'Vitesse initiale thermique stationnaire : une vitesse initialement nulle donnerait une autre formule aux temps courts.', 'La courbe de référence est une moyenne statistique exacte ; l’ensemble fini fluctue autour. Le MSD 2D total vaudrait deux fois la mesure par direction.'])

def absorption_neutrons(p):
    D=p['D']*1e-4; tau=p['lifetime']; Q=p['source']*1e6; L=math.sqrt(D*tau); u=np.linspace(.01,6,601); r=u*L
    density=Q*np.exp(-u)/(4*math.pi*D*r); flux=Q*np.exp(-u)*(1+u)/(4*math.pi*r*r); through=Q*(1+u)*np.exp(-u); absorbed=Q-through
    low,high=0.,12.
    for _ in range(60):
        mid=(low+high)/2
        if (1+mid)*math.exp(-mid)>.1: low=mid
        else: high=mid
    return result([metric('Longueur de diffusion L=√(Dτ)',L,'m'),metric('Nombre total de neutrons présents Qτ',Q*tau),metric('Rayon contenant 90 % des absorptions',(low+high)/2*L,'m'),metric('Débit traversant la dernière sphère',float(through[-1]),'s⁻¹'),metric('Résidu relatif du bilan de source',float(np.max(abs(through+absorbed-Q))/Q))],
        [chart('Densité radiale : une source ponctuelle, sans valeur finie en 0','r (m)','n (m⁻³)',series('Q e^{−r/L}/(4πDr)',r,density),y_scale='log'),chart('La puissance de la source se répartit','r/L','Débit (s⁻¹)',series('Neutrons traversant la sphère',u,through),series('Absorbés à l’intérieur',u,absorbed),series('Source Q',u,np.full_like(u,Q))),chart('Flux surfacique et atténuation','r (m)','j radial (m⁻²·s⁻¹)',series('−D dn/dr',r,flux),y_scale='log')],
        curve_scene('Diffusion et absorption autour d’une source',r,[('Densité',density)],'r (m)','n (m⁻³)','La source est en r=0 ; la densité y est singulière. Le premier point dessiné est r=0,01L, tandis que la normalisation de la source est obtenue par la limite du débit.',dict(type='particles',geometry='source',length=L,source=Q)),
        ['D est le coefficient de diffusion, τ la durée de vie et Q le débit injecté. L=√(Dτ) est la longueur où les deux mécanismes se concurrencent.', 'Hors de la source, le régime stationnaire satisfait DΔn−n/τ=0. En symétrie sphérique, poser u=rn donne u″=u/L².', 'La décroissance à l’infini impose n=Ae^{−r/L}/r. La condition lim_{r→0}4πr²j=Q fixe A=Q/(4πD).', 'Le débit traversant r vaut Q(1+r/L)e^{−r/L}. Son complément est l’absorption à l’intérieur ; leur somme égale Q pour tout r. L’intégrale du nombre présent vaut Qτ.'],
        ['Milieu homogène infini et absorption linéaire, pas de multiplication des neutrons.', 'Source ponctuelle idéale : n(0) n’est pas définie et n’est jamais remplacée par une valeur finie.', 'La densité, le flux surfacique et le débit total ont trois unités différentes.'])

def ambipolar(Dp,Dm):
    return 2*Dp*Dm/(Dp+Dm)

def diffusion_electrolyte(p):
    Dp,Dm=p['Dp']*1e-9,p['Dm']*1e-9; T=p['temperature']; Da=ambipolar(Dp,Dm); time=p['seconds']; width=math.sqrt(Da*time)
    x=np.linspace(-8*width,8*width,801); delta=p['right']-p['left']; concentration=(p['left']+p['right'])/2+delta/2*erf_array(x/(2*width)); gradient=delta/(2*math.sqrt(math.pi)*width)*np.exp(-x*x/(4*width*width))
    coefficient=KB*T/E_CHARGE*(Dp-Dm)/(Dp+Dm); field=coefficient*gradient/concentration; potential=-coefficient*np.log(concentration/p['left'])
    number=concentration*NA; dn=gradient*NA
    plus=-Dp*dn+Dp*E_CHARGE/(KB*T)*number*field; minus=-Dm*dn-Dm*E_CHARGE/(KB*T)*number*field
    target=-Da*dn; normalized=np.max(abs(plus-minus))/max(float(np.max(abs(plus)+abs(minus))),1e-30)
    return result([metric('Coefficient de diffusion ambipolaire',Da,'m²/s'),metric('Différence Vdroite−Vgauche',-coefficient*math.log(p['right']/p['left'])*1000,'mV'),metric('Champ maximal en valeur absolue',float(np.max(abs(field))),'V/m'),metric('Résidu relatif du courant électrique nul',float(normalized)),metric('Longueur √(Damb t)',width*1000,'mm')],
        [chart('Le sel diffuse avec un coefficient commun','x (mm)','c (mol/m³)',series('Profil c(x,t)',x*1000,concentration)),chart('Le potentiel est opposé à l’intégrale du champ','x (mm)','V−Vgauche (mV)',series('Potentiel de jonction',x*1000,potential*1000)),chart('Les deux ions ont le même flux particulaire','x (mm)','Flux (m⁻²·s⁻¹)',series('Cation, diffusion + migration',x*1000,plus),series('Anion, diffusion + migration',x*1000,minus),series('Fick ambipolaire',x*1000,target)),chart('Le champ est local et généralement non uniforme','x (mm)','E (V/m)',series('Champ de jonction',x*1000,field))],
        curve_scene('Un gradient de sel crée un champ de jonction',x*1000,[('Concentration',concentration)],'x (mm)','c (mol/m³)','Les ions monovalents restent quasi neutres dans le volume. Le champ ajuste leurs flux sans imposer un courant électrique extérieur.',dict(type='particles',geometry='electrolyte',left=p['left'],right=p['right'],potential_difference=-coefficient*math.log(p['right']/p['left']))),
        ['D₊ et D₋ sont les diffusivités des ions monovalents ; n=N_Ac est leur densité commune. E=−dV/dx fixe la convention de potentiel.', 'Les flux sont Γ₊=−D₊n′+D₊enE/(kBT) et Γ₋=−D₋n′−D₋enE/(kBT). Imposer le courant e(Γ₊−Γ₋)=0.', 'On trouve E=(kBT/e)(D₊−D₋)n′/[(D₊+D₋)n] et Γ₊=Γ₋=−Damb n′, avec Damb=2D₊D₋/(D₊+D₋).', 'Intégrer V′=−E donne Vdroite−Vgauche=(kBT/e)(D₋−D₊)ln(nDroite/nGauche)/(D₊+D₋). Si les diffusivités sont égales, le champ et la jonction disparaissent.'],
        ['Électrolyte dilué monovalent, température uniforme, diffusivités constantes et courant électrique total nul.', 'Quasi-neutralité dans le volume : les couches de charge aux interfaces ne sont pas résolues.', 'Le profil erfc décrit la mise en contact de deux demi-espaces ; le champ peut varier avec x.'])

def insulated_chain_matrix(n,conductance,capacity):
    A=np.zeros((n,n)); rate=conductance/capacity
    for j in range(n-1):
        A[j,j]-=rate; A[j+1,j+1]-=rate; A[j,j+1]+=rate; A[j+1,j]+=rate
    return A

def entropie_diffusion(p):
    n=int(p['N']); C,G=p['capacity'],p['conductance']; A=insulated_chain_matrix(n,G,C); values,Q=np.linalg.eigh(A)
    initial=np.where(np.arange(n)<n//2,p['hot'],p['cold'])+273.15; slow=1/(2*G/C*(1-math.cos(math.pi/n))); end=p['ratio']*slow
    values[-1]=0.0  # Le mode uniforme est exactement conservé.
    t=np.linspace(0,end,401); temperatures=(np.exp(t[:,None]*values)*(Q.T@initial))@Q.T
    if np.all(initial==initial[0]): temperatures=np.full((len(t),n),initial[0])
    entropy=C*np.sum(np.log(temperatures/initial),axis=1); diff=np.diff(temperatures,axis=1); production=G*np.sum(diff*diff/(temperatures[:,:-1]*temperatures[:,1:]),axis=1)
    energy=C*np.sum(temperatures,axis=1); final_T=float(np.mean(initial)); maximum=C*(n*math.log(final_T)-float(np.sum(np.log(initial))))
    if np.all(initial==initial[0]): maximum=0.0
    return result([metric('Température finale prévue',final_T-273.15,'°C'),metric('Temps de relaxation le plus lent',slow,'s'),metric('Variation relative maximale d’énergie',float(np.max(abs(energy-energy[0]))/energy[0])),metric('Entropie produite au temps final',float(entropy[-1]),'J/K'),metric('Entropie produite à l’équilibre',maximum,'J/K'),metric('Production instantanée finale',float(production[-1]),'W/K')],
        [chart('Chaque température converge vers la moyenne énergétique','t (s)','T (°C)',*[series(f'Cellule {j+1}',t,temperatures[:,j]-273.15) for j in sorted(set([0,n//2,n-1]))],series('Équilibre',t,np.full_like(t,final_T-273.15))),chart('L’énergie se conserve, l’entropie augmente','t (s)','ΔS (J/K)',series('Entropie totale moins initiale',t,entropy),series('Gain final maximal',t,np.full_like(t,maximum))),chart('Chaque interface produit une quantité positive','t (s)','dS/dt (W/K)',series('Σ G(Tᵢ−Tⱼ)²/(TᵢTⱼ)',t,production))],
        heat_scene('Chaîne isolée : redistribution interne de chaleur',np.arange(1,n+1),t[::4],temperatures[::4]-273.15,'Indice de cellule','t (s)','T (°C)','Les cellules échangent entre voisines et aucun flux ne traverse les extrémités. L’énergie totale est conservée ; les températures absolues interviennent dans l’entropie.',dict(type='bar',cells=n,temperatures=temperatures[-1]-273.15)),
        ['C est la capacité de chaque cellule et G la conductance entre voisines. Les températures sont converties en kelvins avant de calculer l’entropie.', 'Chaque bilan est C dTᵢ/dt=G∑voisins(Tvoisin−Tᵢ). La matrice symétrique est diagonalisee et l’évolution est calculée par ses modes exacts.', 'Sommer les bilans annule les échanges : U=C∑Tᵢ est constant. Le système isolé rejoint la moyenne arithmétique puisque les capacités sont égales.', 'À une interface, dS/dt=G(Tᵢ−Tⱼ)(1/Tⱼ−1/Tᵢ)=G(Tᵢ−Tⱼ)²/(TᵢTⱼ)≥0. Sommer donne la production irréversible ; ΔS=C∑ln(Tᵢ/Tᵢ,initial).'],
        ['Capacités et conductances positives constantes ; pas de changement de phase ni d’échange extérieur.', 'Le zéro de l’énergie interne et les constantes additives d’entropie sont arbitraires ; seuls leurs bilans et variations sont utilisés.', 'Les très petits écarts numériques d’énergie ou d’entropie au départ proviennent de la diagonalisation en double précision.'])

COMPUTE={name:globals()[name] for name in ('fourier_barre','paroi_composite','isolation_radiale','igloo','diffusion_1d','demi_espace','onde_thermique','refroidissement_biot','diffusion_2d','marche_aleatoire','brownien_langevin','absorption_neutrons','diffusion_electrolyte','entropie_diffusion')}
