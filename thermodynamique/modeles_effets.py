"""Bilans et réponses couplées : calculs NumPy, unités SI dans les modèles."""
import cmath
import math
import numpy as np
from commun import metric, series, chart, result

SIGMA=5.670374419e-8
TREF=273.15
RWATER=461.5
FACES=[('Laquée noire',.95),('Laquée blanche',.90),('Métallique mate',.35),('Métallique polie',.04)]


def curves_scene(title,description,curves,xlabel,ylabel,apparatus):
    return dict(kind='curves',title=title,description=description,xLabel=xlabel,yLabel=ylabel,
                curves=[dict(label=label,x=x,y=y) for label,x,y in curves],apparatus=apparatus)


def leslie_power(T,Tamb,area,emissivity,h):
    """Puissances sortantes d'une face ; négatives si elle reçoit de la chaleur."""
    radiation=emissivity*SIGMA*area*(np.asarray(T)**4-Tamb**4)
    convection=h*area*(np.asarray(T)-Tamb)
    return radiation,convection


def cube_leslie(p):
    T,Ta,a,h,C=p['T'],p['Tamb'],p['side'],p['h'],p['capacity']; area=a*a
    emissivities=[epsilon for _,epsilon in FACES]+[.95,.95]
    powers=[float(leslie_power(T,Ta,area,epsilon,h)[0]) for _,epsilon in FACES]
    radiation=SIGMA*area*sum(emissivities)*(T**4-Ta**4); convection=6*h*area*(T-Ta)
    temps=np.linspace(275,480,401); time=np.linspace(0,1800,1801); cooling=np.empty_like(time); cooling[0]=T
    def derivative(temp):
        return -(SIGMA*area*sum(emissivities)*(temp**4-Ta**4)+6*h*area*(temp-Ta))/C
    for j in range(len(time)-1):
        dt=time[j+1]-time[j]; u=cooling[j]
        k1=derivative(u); k2=derivative(u+dt*k1/2); k3=derivative(u+dt*k2/2); k4=derivative(u+dt*k3)
        cooling[j+1]=u+dt*(k1+2*k2+2*k3+k4)/6
    # Même géométrie et même étalonnage pour chaque face ; valeurs pédagogiques.
    eta,responsivity=.05,2.0  # fraction reçue ; mV/W au détecteur
    signals=[eta*responsivity*power for power in powers]
    apparatus=dict(type='radiation',temperature=T,ambient=Ta,side=a,
                   faces=[dict(label=label,emissivity=epsilon,power=power,signal_mV=signal)
                          for (label,epsilon),power,signal in zip(FACES,powers,signals)],
                   radiation_W=radiation,convection_W=convection,heater_W=radiation+convection)
    out=result([metric('Rayonnement net : face noire',powers[0],'W'),metric('Rayonnement net : face polie',powers[3],'W'),
                metric('Rapport noir/poli des signaux, hors équilibre',.95/.04),metric('Rayonnement net du cube',radiation,'W'),
                metric('Convection du cube',convection,'W'),metric('Puissance nécessaire au maintien de T',radiation+convection,'W'),
                metric('Température après 30 min sans chauffage',float(cooling[-1]),'K')],
        [chart('Rayonnement net des quatre surfaces à même température','T (K)','Puissance par face (W)',
               *[series(label,temps,leslie_power(temps,Ta,area,epsilon,h)[0]) for label,epsilon in FACES]),
         chart('Bilan du cube entier : six faces','T (K)','Puissance sortante (W)',
               series('Rayonnement',temps,SIGMA*area*sum(emissivities)*(temps**4-Ta**4)),
               series('Convection',temps,6*h*area*(temps-Ta)),
               series('Somme : chauffage nécessaire à l’équilibre',temps,SIGMA*area*sum(emissivities)*(temps**4-Ta**4)+6*h*area*(temps-Ta))),
         chart('Chauffage coupé : résoudre le bilan différentiel','Temps (s)','Température (K)',
               series('Cube',time,cooling),series('Pièce',time,np.full_like(time,Ta)))],
        curves_scene('Même aire, même distance, émissivités différentes',
            'Les courbes comparent les puissances radiatives nettes à géométrie identique. La thermopile reçoit une fraction de chacune ; elle ne mesure pas la convection.',
            [(label,temps,leslie_power(temps,Ta,area,epsilon,h)[0]) for label,epsilon in FACES],
            'Température T (K)','Rayonnement net d’une face (W)',apparatus),
        ['T et Tₐ sont des températures absolues. Une face a pour aire A=a² ; ε est son émissivité et σ la constante de Stefan–Boltzmann.',
         'La puissance radiative nette sortante est εσA(T⁴−Tₐ⁴). La soustraction représente le rayonnement reçu de la pièce.',
         'La convection apporte hA(T−Tₐ) par face. Le bilan stationnaire du cube est Pchauffage=Prayonnement+Pconvection.',
         'Les quatre faces comparées ont ε=0,95 ; 0,90 ; 0,35 ; 0,04. Les deux autres faces sont supposées à ε=0,95. Ces valeurs sont illustratives.',
         'Après coupure du chauffage, Cₜₕ dT/dt=−Prayonnement−Pconvection. Le calcul suit ce bilan sans remplacer T⁴ par une loi linéaire.'],
        ['Cube à température uniforme ; pièce assimilée à une enceinte noire à Tₐ ; émissivités et h constants.',
         'Fraction radiative reçue η=0,05 et sensibilité de la thermopile G=2 mV/W : U=GηPface. Ce sont des paramètres de montage illustratifs.',
         'À T=Tₐ, tous les signaux nets sont nuls : leur quotient expérimental n’est pas défini, même si le rapport des émissivités l’est.',
         'Pour T<Tₐ, les puissances sont négatives : la pièce réchauffe le cube. Une puissance de maintien négative demande un refroidissement.'])
    out['table']=dict(headers=['Face','ε','Rayonnement net (W)','Signal U (mV)'],
                      rows=[[label,epsilon,power,signal] for (label,epsilon),power,signal in zip(FACES,powers,signals)])
    return out


def seebeck_voltage(Th,Tc,S0,slope,Tref=TREF):
    return S0*(np.asarray(Th)-Tc)+slope*((np.asarray(Th)-Tref)**2-(Tc-Tref)**2)/2


def seebeck_inverse(voltage,Tc,S0,slope,Tref=TREF):
    """Branche de calibration où S(T)>0 ; écriture stable lorsque la pente est petite."""
    Sc=S0+slope*(Tc-Tref)
    if abs(slope)<1e-20:
        return Tc+np.asarray(voltage)/Sc
    discriminant=Sc*Sc+2*slope*np.asarray(voltage)
    if np.any(discriminant<=0):
        raise ValueError('La tension sort du domaine monotone de cette calibration.')
    return Tc+2*np.asarray(voltage)/(Sc+np.sqrt(discriminant))


def seebeck(p):
    Th,Tc=p['Th'],p['Tc']; S0=p['S0']*1e-6; slope=p['slope']*1e-6; error=p['cold_error']
    voltage=float(seebeck_voltage(Th,Tc,S0,slope)); recovered=float(seebeck_inverse(voltage,Tc,S0,slope))
    estimated=float(seebeck_inverse(voltage,Tc+error,S0,slope))
    ignored=float(seebeck_inverse(voltage,TREF,S0,slope)); linear=Tc+voltage/S0
    temps=np.linspace(250,700,601); calibration=seebeck_voltage(temps,Tc,S0,slope)
    apparent=seebeck_inverse(calibration,Tc+error,S0,slope)
    apparatus=dict(type='electric',effect='seebeck',hot_K=Th,cold_K=Tc,voltage_V=voltage,
                   estimated_K=estimated,coefficient_V_per_K=S0+slope*(Th-TREF),current_A=0)
    return result([metric('Tension à circuit ouvert',voltage*1000,'mV'),metric('Tₕ retrouvé avec jonction froide exacte',recovered,'K'),
        metric('Température indiquée avec l’erreur de référence',estimated,'K'),metric('Erreur de température correspondante',estimated-Th,'K'),
        metric('Température si Tf est supposée à 273,15 K',ignored,'K'),metric('Température obtenue avec S₀ constant',linear,'K')],
        [chart('Une intégrale donne la calibration','Température Tₕ (K)','Tension (mV)',
               series('Calibration intégrée',temps,1000*calibration),series('Approximation S₀(Tₕ−Tf)',temps,1000*S0*(temps-Tc))),
         chart('Erreur de jonction froide : biais de la température retrouvée','Vraie température Tₕ (K)','Erreur (K)',
               series('Avec la calibration exacte',temps,apparent-temps),series('Sans erreur de référence',temps,temps*0)),
         chart('Le coefficient local n’est pas la tension cumulée','Température T (K)','S(T) (µV/K)',
               series('S₀+s₁(T−Tᵣ)',temps,1e6*(S0+slope*(temps-TREF))),series('S₀',temps,np.full_like(temps,1e6*S0)))],
        curves_scene('Un voltmètre mesure une différence liée à deux jonctions',
            'La calibration dépend de la jonction chaude et de la jonction froide. Déplacer la référence change la température indiquée même lorsque la tension mesurée reste identique.',
            [('Calibration intégrée',temps,1000*calibration),('Approximation à S₀ constant',temps,1000*S0*(temps-Tc))],
            'Température à mesurer (K)','Tension (mV)',apparatus),
        ['Tᵣ=273,15 K est la référence des coefficients. S₀ est en V/K et s₁ en V/K² ; les curseurs les donnent en microvolts.',
         'Poser S(T)=S₀+s₁(T−Tᵣ). La convention de branchement est V=∫ de Tf à Tₕ S(T)dT ; inverser les fils change le signe de V.',
         'L’intégrale vaut S₀(Tₕ−Tf)+s₁[(Tₕ−Tᵣ)²−(Tf−Tᵣ)²]/2. Le calcul inverse cette relation sur sa branche monotone.',
         'La compensation de jonction froide utilise sa température mesurée. Une erreur δTf s’ajoute à Tf lors de l’inversion ; la tension reste celle du montage réel.',
         'À petite erreur, S(Tₕ)δTₕ≈S(Tf)δTf. Le biais n’est donc pas toujours exactement égal à l’erreur sur la jonction froide.'],
        ['Coefficient Seebeck effectif du couple de matériaux ; coefficients illustratifs, sans prétendre étalonner un thermocouple industriel.',
         'Circuit ouvert : courant nul, donc autoéchauffement et chute ohmique négligés.',
         'S(T)>0 dans le domaine de calibration affiché pour toutes les bornes proposées ; la température est déterminée de façon unique.',
         'Les températures absolues sont en K. Un écart de température a la même valeur numérique en kelvins et en degrés Celsius.'])


def peltier_flows(Tc,Th,current,alpha,resistance,conductance):
    delta=Th-Tc; I=np.asarray(current)
    cold=alpha*Tc*I-resistance*I*I/2-conductance*delta
    hot=alpha*Th*I+resistance*I*I/2-conductance*delta
    electric=alpha*delta*I+resistance*I*I
    return cold,hot,electric


def peltier(p):
    Tc,delta,I,alpha,R,K=p['Tc'],p['delta'],p['I'],p['alpha'],p['R'],p['K']; Th=Tc+delta; load=p['load']
    Qc,Qh,power=map(float,peltier_flows(Tc,Th,I,alpha,R,K))
    optimum=alpha*Tc/R; maximum=alpha**2*Tc**2/(2*R)-K*delta
    cop=Qc/power if Qc>0 and power>0 else ('Non défini : courant nul' if power==0 else 'Pas de refroidissement')
    status='Refroidissement : chaleur extraite du côté froid' if Qc>0 else 'Aucune chaleur extraite du côté froid'
    equilibrium=(load+R*I*I/2+K*Th)/(alpha*I+K)
    equilibrium_value=equilibrium if equilibrium<Th else 'Aucun équilibre plus froid que Tₕ pour cette charge'
    currents=np.linspace(0,10,501); qc,qh,pw=peltier_flows(Tc,Th,currents,alpha,R,K)
    differences=np.linspace(0,70,351); qc_delta=peltier_flows(Tc,Tc+differences,I,alpha,R,K)[0]
    entropy=Qh/Th-Qc/Tc
    apparatus=dict(type='electric',effect='peltier',cold_K=Tc,hot_K=Th,current_A=I,
                   cold_W=Qc,hot_W=Qh,electric_W=power,status=status,load_W=load)
    return result([metric('Chaleur extraite Qc',Qc,'W'),metric('Chaleur rejetée Qₕ',Qh,'W'),metric('Puissance électrique P',power,'W'),
        metric('Coefficient de performance Qc/P',cop),metric('Mode de fonctionnement',status),metric('Courant de maximum théorique de Qc',optimum,'A'),
        metric('Maximum théorique de Qc à températures fixées',maximum,'W'),metric('Production d’entropie',entropy,'W·K⁻¹'),
        metric('Température d’équilibre pour la charge choisie',equilibrium_value,'K')],
        [chart('Premier principe : Qₕ=Qc+P','Courant I (A)','Puissance (W)',series('Qc extraite',currents,qc),series('Qₕ rejetée',currents,qh),series('P électrique',currents,pw)),
         chart('Ce qui aide et ce qui pénalise le refroidissement','Courant I (A)','Contribution à Qc (W)',
               series('Transport Peltier αTcI',currents,alpha*Tc*currents),series('Part Joule −RI²/2',currents,-R*currents**2/2),series('Fuite −KΔT',currents,np.full_like(currents,-K*delta)),series('Somme Qc',currents,qc)),
         chart('Un écart de température plus grand pénalise Qc','Écart ΔT (K)','Puissance extraite (W)',series('Qc à Tc et I fixés',differences,qc_delta),series('Charge demandée',differences,np.full_like(differences,load)))],
        curves_scene('Un courant utile ne suffit pas : compter Joule et conduction',
            'Le transport Peltier croît avec I, alors que les pertes Joule croissent comme I². Le courant optimal du refroidissement n’est pas celui qui maximise la consommation électrique.',
            [('Peltier',currents,alpha*Tc*currents),('Joule',currents,-R*currents**2/2),('Conduction',currents,np.full_like(currents,-K*delta)),('Qc total',currents,qc)],
            'Courant I (A)','Contribution à Qc (W)',apparatus),
        ['I≥0 est orienté pour transporter la chaleur du froid vers le chaud. Tₕ=Tc+ΔT ; α est en V/K, R en Ω et K en W/K.',
         'Avec des coefficients constants, Qc=αTcI−RI²/2−KΔT et Qₕ=αTₕI+RI²/2−KΔT. Les pertes Joule sont réparties également entre les faces.',
         'La différence Qₕ−Qc vaut P=αΔTI+RI². Le bilan respecte ainsi le premier principe.',
         'Le coefficient de performance est Qc/P uniquement si Qc>0 et P>0. Un Qc négatif signifie que le côté froid reçoit de la chaleur.',
         'À températures fixées, Qc est une parabole en I : son maximum théorique est atteint pour I=αTc/R. Ce courant peut dépasser les 10 A explorés.',
         'Pour une charge thermique fixée et Tₕ maintenue, résoudre Qc=charge donne la température d’équilibre affichée. Un résultat au-dessus de Tₕ ne représente pas un refroidissement.'],
        ['Modèle stationnaire d’un module entier ; α, R et K sont des constantes effectives, effets Thomson négligés.',
         'Qc est comptée positive si elle quitte la source froide ; Qₕ est positive si elle entre dans la source chaude.',
         'Maintenir Tₕ suppose un dissipateur capable d’évacuer Qₕ. Le modèle ne calcule pas la température de ce dissipateur.',
         'La production d’entropie Qₕ/Tₕ−Qc/Tc est positive ou nulle ; le bilan énergétique seul ne suffit pas à discuter le rendement.'])


def acoustic_branches(omega,conductivity,P0,T0,rho,gamma):
    """Convention exp(iωt−ikx) ; branche acoustique prolongée depuis λ=0."""
    omega=np.asarray(omega,dtype=float); c=math.sqrt(gamma*P0/rho)
    rhocp=gamma*P0/((gamma-1)*T0); s=omega**2/c**2
    if conductivity==0:
        k=omega/c+0j
        ratio=np.full_like(omega,(gamma-1)*T0/(gamma*P0),dtype=complex)
        return k,None,ratio,c,rhocp
    b=1j*omega*rhocp-conductivity*gamma*s; constant=-1j*omega*rhocp*s
    discriminant=b*b-4*conductivity*constant
    # Pour 1<γ<2, Im(discriminant)>0 : la racine principale continue +iωρcₚ.
    root=np.sqrt(discriminant)
    q_ac=-2*constant/(b+root); q_th=(-b-root)/(2*conductivity)
    k_ac=np.sqrt(q_ac); k_th=np.sqrt(q_th)
    ratio=1j*omega/(1j*omega*rhocp+conductivity*q_ac)
    return k_ac,k_th,ratio,c,rhocp


def thermoacoustique(p):
    f,lam,P0,T0,rho,gamma,L=p['frequency'],p['conductivity'],p['P0'],p['T0'],p['rho'],p['gamma'],p['length']
    omega=2*math.pi*f; k,kt,ratio,c,rhocp=acoustic_branches(omega,lam,P0,T0,rho,gamma)
    k,ratio=complex(k),complex(ratio); attenuation=max(0,-k.imag); wavelength=2*math.pi/k.real
    speed=omega/k.real; after=math.exp(-attenuation*L); adiabatic=(gamma-1)*T0/(gamma*P0)
    frequencies=np.geomspace(20,20000,301); ks,_,ratios,_,_=acoustic_branches(2*np.pi*frequencies,lam,P0,T0,rho,gamma)
    positions=np.linspace(0,L,501); zoom=min(L,4*wavelength); x=np.linspace(0,zoom,801)
    wave=np.exp(-1j*k*x); pressure=wave.real; temperature=(ratio/adiabatic*wave).real
    q=k*k; b=1j*omega*rhocp-lam*gamma*omega**2/c**2; constant=-1j*omega*rhocp*omega**2/c**2
    terms=[lam*q*q,b*q,constant]; residual=abs(sum(terms))/sum(abs(t) for t in terms)
    thermal_length='Branche thermique absente pour λ=0' if kt is None else 1/(-complex(kt).imag)
    apparatus=dict(type='acoustic',frequency_Hz=f,length_m=L,zoom_m=zoom,wavenumber_real=k.real,
                   attenuation_per_m=attenuation,temperature_ratio_K_per_Pa=abs(ratio),phase_deg=math.degrees(cmath.phase(ratio)),
                   speed_m_per_s=speed,pressure_amplitude_Pa=1,thermal_length_m=thermal_length)
    return result([metric('Vitesse de phase acoustique',speed,'m·s⁻¹'),metric('Vitesse adiabatique c',c,'m·s⁻¹'),
        metric('Atténuation −Im k',attenuation,'m⁻¹'),metric('Amplitude p(L)/p(0)',after),metric('Longueur d’onde',wavelength,'m'),
        metric('Amplitude |τ/p|',abs(ratio)*1000,'mK·Pa⁻¹'),metric('Phase de τ/p',math.degrees(cmath.phase(ratio)),'°'),
        metric('Longueur de décroissance de la branche thermique',thermal_length,'m'),metric('Résidu relatif de dispersion',residual)],
        [chart('De la vitesse adiabatique à la limite isotherme','Fréquence f (Hz)','Vitesse (m/s)',
               series('Branche acoustique',frequencies,2*np.pi*frequencies/ks.real),series('c adiabatique',frequencies,np.full_like(frequencies,c)),series('c/√γ isotherme',frequencies,np.full_like(frequencies,c/math.sqrt(gamma)))),
         chart('Enveloppe de pression sur toute la longueur','Position x (m)','Amplitude relative',series('exp(Im k × x)',positions,np.exp(k.imag*positions))),
         chart('La température peut être déphasée par rapport à la pression','Fréquence f (Hz)','Phase de τ/p (°)',series('Phase',frequencies,np.angle(ratios,deg=True)))],
        curves_scene('Surpression et température : vue des premières longueurs d’onde',
            'La vue montre au plus quatre longueurs d’onde pour éviter de confondre échantillonnage et oscillations physiques. Les deux amplitudes sont divisées par leurs références adiabatiques ; l’enveloppe sur toute la longueur est tracée séparément.',
            [('p/p₀',x,pressure),('τ/(p₀τ/p adiabatique)',x,temperature)],'Position x (m)','Amplitude réduite',apparatus),
        ['P₀, T₀ et ρ₀ décrivent le gaz parfait au repos ; γ=cₚ/cᵥ. Poser c²=γP₀/ρ₀ et ρ₀cₚ=γP₀/[(γ−1)T₀].',
         'λ est la conductivité thermique, ω=2πf la pulsation et k le nombre d’onde complexe. La convention est exp(iωt−ikx), avec i²=−1.',
         'Poser q=k². L’équation couplée donne λq²+[iωρ₀cₚ−λγω²/c²]q−iωρ₀cₚω²/c²=0.',
         'Choisir la branche acoustique qui tend vers k=ω/c lorsque λ tend vers 0. Sa partie imaginaire est négative : l’amplitude décroît en avançant vers x>0.',
         'L’équation thermique donne τ/p=iω/(iωρ₀cₚ+λk²). Avec exp(iωt), une phase positive indique une avance de la température sur la pression.',
         'L’autre racine est une branche thermique diffusive. Elle n’est pas une seconde onde sonore ; sa longueur de décroissance est indiquée séparément.'],
        ['Perturbations faibles, gaz parfait et coefficients constants ; conduction suivant l’axe, sans viscosité ni pertes aux parois.',
         'La pression d’amplitude p₀=1 Pa sert à normaliser la scène. Le modèle ne constitue pas un calcul complet de moteur ou de réfrigérateur thermoacoustique.',
         'Les grandes conductivités servent à explorer mathématiquement la limite isotherme ; elles ne représentent pas l’air ordinaire.',
         'Les deux repères c et c/√γ sont les limites adiabatique et isotherme. Le domaine 1<γ<2 rend continue la sélection de racine utilisée.'])


def piezo_energy(x,q,stiffness,capacity,theta):
    return stiffness*np.asarray(x)**2/2+(np.asarray(q)-theta*np.asarray(x))**2/(2*capacity)


def piezo_response(omega,mass,stiffness,capacity,theta,damping,voltage=1):
    denominator=stiffness-mass*np.asarray(omega)**2+1j*damping*np.asarray(omega)
    displacement=theta*voltage/denominator
    charge=capacity*voltage+theta*displacement
    admittance=1j*np.asarray(omega)*charge/voltage
    return displacement,charge,admittance


def piezo_resonateur(p):
    m=p['mass_mg']*1e-6; k=p['stiffness_MN']*1e6; C=p['capacity_nF']*1e-9; theta=p['theta_mC']*1e-3
    zeta,ratio,V=p['damping'],p['ratio'],p['voltage']; r=2*zeta*math.sqrt(k*m)
    wr=math.sqrt(k/m); wa=math.sqrt((k+theta*theta/C)/m); omega=ratio*wr
    X,Q,Y=map(complex,piezo_response(omega,m,k,C,theta,r,V)); fr=wr/(2*math.pi); fa=wa/(2*math.pi)
    ratios=np.unique(np.concatenate([np.linspace(.5,max(1.8,1.2*wa/wr),1201),np.linspace(.97,1.03,401),np.linspace(.97*wa/wr,1.03*wa/wr,401)]))
    frequencies=ratios*wr; xs,_,ys=piezo_response(frequencies,m,k,C,theta,r,V)
    t=np.linspace(0,4,801); oscillation=np.exp(2j*np.pi*t); static=theta*V/k
    coordinate=np.linspace(-3,3,501); energy=piezo_energy(coordinate*static,C*V,k,C,theta)
    apparatus=dict(type='piezo',frequency_Hz=omega/(2*math.pi),voltage_V=V,displacement_m=abs(X),
                   displacement_phase_deg=math.degrees(cmath.phase(X)),charge_C=abs(Q),current_A=omega*abs(Q),
                   resonance_Hz=fr,antiresonance_Hz=fa,damping_Ns_per_m=r,coupling_C_per_m=theta)
    return result([metric('Fréquence choisie',omega/(2*math.pi)/1000,'kHz'),metric('Résonance : repère sans pertes fᵣ',fr/1000,'kHz'),
        metric('Antirésonance : repère sans pertes fₐ',fa/1000,'kHz'),metric('Amplitude du déplacement',abs(X)*1e6,'µm'),
        metric('Amplitude du courant',omega*abs(Q)*1000,'mA'),metric('Conductance Re Y',Y.real*1000,'mS'),
        metric('Puissance mécanique dissipée moyenne',r*omega**2*abs(X)**2/2*1000,'mW'),metric('Couplage réduit θ²/(kC)',theta**2/(k*C))],
        [chart('Admittance : pic de résonance et creux d’antirésonance','Fréquence réduite f/fᵣ','|Y| (mS)',
               series('Résonateur couplé',ratios,abs(ys)*1000),series('Capacité seule',ratios,frequencies*C*1000),xMarker=wa/wr,xMarkerLabel='Antirésonance sans pertes',y_scale='log'),
         chart('La réponse mécanique dépend de l’amortissement','Fréquence réduite f/fᵣ','Déplacement (µm)',series('|x|',ratios,abs(xs)*1e6),xMarker=1,xMarkerLabel='Résonance sans pertes'),
         chart('Énergie positive à charge q=CV fixée','Déplacement réduit x/(θV/k)','U (nJ)',series('U(x,q)',coordinate,energy*1e9))],
        curves_scene('Une tension excite le mouvement et une charge supplémentaire',
            'Le temps est exprimé en périodes de la tension. Le déplacement et la charge sont divisés par leurs valeurs de référence ; le déphasage et l’amplification restent visibles. Les fréquences fᵣ et fₐ sont des repères calculés sans pertes.',
            [('V/V₀',t,oscillation.real),('x/(θV₀/k)',t,(X/static*oscillation).real),('q/(CV₀)',t,(Q/(C*V)*oscillation).real)],
            'Temps / période','Grandeur réduite',apparatus),
        ['x est en m, q en C et V en V. m est en kg, k en N/m, C en F et θ en C/m, équivalent à N/V. Tous les curseurs sont convertis en unités SI.',
         'L’énergie U(x,q)=kx²/2+(q−θx)²/(2C) donne V=∂U/∂q et F=∂U/∂x. Ainsi q=CV+θx et F=kx−θV.',
         'Avec un frottement r>0, m x″+r x′+kx=θV. Le curseur ζ donne r=2ζ√(km).',
         'Pour la convention exp(iωt), la réponse est x=θV/(k−mω²+iωr) et Y=iωC+iωθ²/(k−mω²+iωr). Le courant est dq/dt.',
         'Sans pertes, ωᵣ²=k/m et ωₐ²=(k+θ²/C)/m. À l’antirésonance, les deux contributions au courant se compensent.',
         'Avec r>0, les courbes restent finies. La puissance moyenne reçue V₀² Re(Y)/2 égale la dissipation mécanique rω²|x|²/2.'],
        ['Un seul mode mécanique et des coefficients constants ; amplitudes assez faibles pour la réponse linéaire.',
         'Le même coefficient θ apparaît dans les effets direct et inverse : le modèle dérive d’une même énergie et respecte la réciprocité.',
         'La charge q est la variable électrique de U. À tension imposée, le potentiel adapté est U−Vq ; sa raideur en x vaut k.',
         'Les repères sans pertes ne sont pas présentés comme les extrema exacts de la réponse amortie. La fenêtre fréquentielle couvre toujours fₐ.'])


def saturation_log_ratio(T,Tstar,A,B,R=RWATER):
    T=np.asarray(T)
    return -A/R*(1/T-1/Tstar)-B/R*np.log(T/Tstar)


def condensation_margin(T,latent,gamma,R=RWATER):
    """Marge positive : la saturation décroît plus vite que l'adiabat lors d'une détente."""
    return np.asarray(latent)/(R*np.asarray(T))-gamma/(gamma-1)


def brouillard(p):
    Tstar,latent,B,gamma,drop=p['Tstar'],p['latent_MJ']*1e6,p['B'],p['gamma'],p['drop']; A=latent+B*Tstar
    critical=A*(gamma-1)/(RWATER*gamma+B*(gamma-1)); margin=float(condensation_margin(Tstar,latent,gamma))
    temperature=np.linspace(Tstar-drop,Tstar,501)
    saturation=np.exp(saturation_log_ratio(temperature,Tstar,A,B))
    exponent=gamma/(gamma-1)
    def log_excess(T):
        return exponent*np.log(np.asarray(T)/Tstar)-saturation_log_ratio(T,Tstar,A,B)
    descending=np.linspace(Tstar,Tstar-drop,1001); excess=log_excess(descending)
    violations=np.flatnonzero(excess>1e-12)
    onset=None
    if margin>1e-12:
        onset=Tstar
    elif len(violations):
        j=int(violations[0]); high=descending[j-1]; low=descending[j]
        for _ in range(55):
            middle=(high+low)/2
            if log_excess(middle)>0: low=middle
            else: high=middle
        onset=(high+low)/2
    last=Tstar-drop if onset is None else onset
    gas_temperature=np.linspace(last,Tstar,301) if last<Tstar else np.array([Tstar])
    gas_pressure=(gas_temperature/Tstar)**exponent
    status=('Condensation dès le début de la détente' if margin>1e-12 else
            'Pentes égales : le premier ordre ne conclut pas' if abs(margin)<=1e-12 else
            'Pas de condensation pour une détente infinitésimale')
    tx=np.linspace(250,380,141); ly=np.linspace(.2,2.8,131); TT,LL=np.meshgrid(tx,ly*1e6)
    classification=condensation_margin(TT,LL,gamma)
    apparatus=dict(type='fog',initial_K=Tstar,requested_final_K=Tstar-drop,last_vapour_K=last,
                   initial_latent_J_per_kg=latent,condensation=onset is not None,onset_K=onset,
                   margin=margin,status=status,gas_law_stopped=onset is not None)
    return result([metric('Diagnostic des pentes initiales',status),metric('Température limite du critère',critical,'K'),
        metric('Marge initiale L*/(RT*)−γ/(γ−1)',margin),metric('Dernière température de vapeur seule tracée',last,'K'),
        metric('Début de condensation dans la fenêtre',onset if onset is not None else 'Non atteint','K'),
        metric('Constante A=L*+BT*',A/1e6,'MJ·kg⁻¹')],
        [chart('Saturation et partie admissible de la détente','Température T (K)','Pression / P*',
               series('Courbe de saturation',temperature,saturation),series('Vapeur seule : arrêt au début de condensation',gas_temperature,gas_pressure)),
         chart('Comparer les dérivées logarithmiques','Température T (K)','d ln P / dT (K⁻¹)',
               series('Saturation : L(T)/(RT²)',temperature,(A-B*temperature)/(RWATER*temperature**2)),
               series('Gaz parfait isentropique : γ/[(γ−1)T]',temperature,exponent/temperature))],
        dict(kind='heatmap',title='Quand une détente infinitésimale produit-elle de la condensation ?',
             description='Chaque case représente un état initial saturé indépendant. Une marge positive annonce la condensation lors d’un faible refroidissement. La carte varie T* et L* ; elle ne représente pas une trajectoire après changement d’état.',
             x=tx,y=ly,z=classification,xLabel='Température initiale T* (K)',yLabel='Chaleur latente initiale L* (MJ/kg)',
             zLabel='Marge sans dimension',apparatus=apparatus),
        ['T* et P* désignent l’état initial saturé. L*=L(T*) est en J/kg ; B est en J/(kg·K) et A=L*+BT*. Toutes les températures sont absolues.',
         'La constante R=461,5 J/(kg·K) est massique. La formule de Clapeyron approchée donne d ln Pₛₐₜ/dT=(A−BT)/(RT²).',
         'Son intégration donne ln(Pₛₐₜ/P*)=−(A/R)(1/T−1/T*)−(B/R)ln(T/T*).',
         'Tant que la vapeur reste seule et la détente réversible, P/P*=(T/T*)^{γ/(γ−1)}. Comparer les pentes à T* avant de conclure.',
         'Pour un petit dT négatif, une pente de saturation plus grande fait décroître Pₛₐₜ plus vite. La vapeur atteint alors la sursaturation : T*<A(γ−1)/[Rγ+B(γ−1)].',
         'Le calcul arrête la courbe de vapeur seule à la première condensation. La chaleur latente libérée interdit de prolonger ensuite cette loi de Laplace.'],
        ['Vapeur d’eau assimilée à un gaz parfait, volume du liquide négligé devant celui de la vapeur ; loin du point critique.',
         'Détente adiabatique et quasistatique avant condensation ; γ constant ; loi de Regnault locale, non table précise de vapeur d’eau.',
         'Les rapports de pression sont normalisés par P*, sans fixer sa valeur. La courbe de saturation est une référence d’équilibre.',
         'La marge nulle signifie que la comparaison au premier ordre ne suffit pas. Le modèle intégré peut alors révéler un effet à l’ordre suivant.',
         'Aucune quantité de liquide, taille de goutte ni évolution diphasée n’est calculée. L(T)>0 dans toute la fenêtre proposée.'])


COMPUTE={name:globals()[name] for name in ['cube_leslie','seebeck','peltier','thermoacoustique','piezo_resonateur','brouillard']}
