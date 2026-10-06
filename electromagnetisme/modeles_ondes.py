"""Ondes et milieux : NumPy, conventions exp(ikz−iωt), calculs finis.

Les figures représentent les solutions des modèles explicitement annoncés.
Les champs complexes sont conservés au calcul ; le protocole JSON ne contient
que leurs parties réelles, imaginaires ou des scalaires physiques réels.
"""
import math
import numpy as np
try:
    from .catalogue_ondes import LABS, LAB_BY_ID
except ImportError:
    from catalogue_ondes import LABS, LAB_BY_ID

C=299792458.
E_CHARGE=1.602176634e-19
H_PLANCK=6.62607015e-34
KB=1.380649e-23
ME=9.1093837139e-31
MU0=1.25663706127e-6
EPS0=1/(MU0*C*C)
Z0=MU0*C
MU_B=E_CHARGE*H_PLANCK/(4*math.pi*ME)
YEAR=365.25*86400
CONVENTION="Convention harmonique : exp(ikz−iωt), champs physiques = parties réelles ; Im k≥0 dans un milieu passif."
REFERENCES={
    "constants":"https://physics.nist.gov/cuu/pdf/all.pdf",
    "fresnel":"https://farside.ph.utexas.edu/teaching/315/Waveshtml/node59.html",
    "drude":"https://farside.ph.utexas.edu/teaching/em/lectures/node103.html",
    "radiation":"https://farside.ph.utexas.edu/teaching/jk1/lectures/node107.html",
    "dynamo":"https://dennou-q.geo.kyushu-u.ac.jp/arch/gfdsemi/2017-11-28/01_Jones/lecture03/pub-web/20171128_jones_lec03.pdf",
    "core":"https://pubmed.ncbi.nlm.nih.gov/20445627/",
}


def metric(label,value,unit=""):
    return dict(label=label,value=value,unit=unit)


def series(label,x,y):
    return dict(label=label,x=x,y=y)


def chart(title,xlabel,ylabel,*curves,**scales):
    return dict(title=title,x_label=xlabel,y_label=ylabel,series=list(curves),**scales)


def scene(kind,title,description,**data):
    return dict(kind=kind,title=title,description=description,**data)


def clean(value):
    if isinstance(value,np.ndarray):return clean(value.tolist())
    if isinstance(value,np.generic):return clean(value.item())
    if isinstance(value,dict):return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [clean(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value):raise ArithmeticError("Valeur non finie dans une expérience d'ondes.")
    if isinstance(value,complex):raise ArithmeticError("Une amplitude complexe doit être exportée par ses composantes réelles.")
    return value


def passive_sqrt(epsilon):
    """Racine passive pour ε avec Im ε≥0, y compris ε réel négatif."""
    epsilon=np.asarray(epsilon,dtype=complex)
    result=np.sqrt(epsilon)
    return np.where(result.imag<0,-result,result)


def _validated(lab,p):
    if lab not in LAB_BY_ID:raise ValueError("Laboratoire d'ondes inconnu.")
    if p is None:p={}
    if not isinstance(p,dict):raise ValueError("Un objet de paramètres est attendu.")
    controls=LAB_BY_ID[lab]["controls"]
    if set(p)-{c["key"] for c in controls}:raise ValueError("Paramètre inconnu pour cette expérience.")
    values={}
    for control in controls:
        key=control["key"];value=p.get(key,control["value"])
        if control["type"]=="select":
            if value not in [o["value"] for o in control["options"]]:raise ValueError("Choix invalide : "+key)
        else:
            if isinstance(value,bool) or not isinstance(value,(int,float)):raise ValueError("Nombre attendu : "+key)
            try:value=float(value)
            except OverflowError:raise ValueError("Nombre non fini : "+key) from None
            if not math.isfinite(value) or not control["min"]<=value<=control["max"]:raise ValueError("Valeur hors domaine : "+key)
        values[key]=value
    return values


def calculate(lab,params=None):
    p=_validated(lab,params)
    result=COMPUTE[lab](p)
    return clean(dict(lab=lab,params=p,**result))


def vacuum_fields(z_over_lambda,time_over_period,amplitude,ellipticity,standing=False):
    z=np.asarray(z_over_lambda);q=2*np.pi*z;t=2*np.pi*time_over_period
    E=np.zeros(z.shape+(3,));B=np.zeros_like(E)
    if not standing:
        phase=q-t
        E[...,0]=amplitude*np.cos(phase);E[...,1]=ellipticity*amplitude*np.sin(phase)
        B[...,0]=-E[...,1]/C;B[...,1]=E[...,0]/C
        mean=np.full_like(z,amplitude**2*(1+ellipticity**2)/(2*Z0))
    else:
        E[...,0]=2*amplitude*np.cos(q)*np.cos(t)
        E[...,1]=-2*ellipticity*amplitude*np.cos(q)*np.sin(t)
        B[...,0]=-2*ellipticity*amplitude*np.sin(q)*np.cos(t)/C
        B[...,1]=2*amplitude*np.sin(q)*np.sin(t)/C
        mean=np.zeros_like(z)
    flux=np.cross(E,B)[...,2]/MU0
    energy_E=.5*EPS0*np.sum(E*E,axis=-1);energy_B=.5/MU0*np.sum(B*B,axis=-1)
    return E,B,flux,mean,energy_E,energy_B


def compute_maxwell(p):
    z=np.linspace(0,2,241);E0=p["amplitude"];ell=p["ellipticity"];standing=p["mode"]=="stationnaire"
    E,B,S,Smean,uE,uB=vacuum_fields(z,p["phase"],E0,ell,standing)
    wavelength=C/(p["frequency"]*1e9)
    average_energy=(1 if standing else .5)*EPS0*E0**2*(1+ell**2)
    return dict(metrics=[metric("Longueur d'onde",wavelength,"m"),metric("Flux moyen vers +z",float(Smean[0]),"W·m⁻²"),
                         metric("Énergie moyenne par volume",average_energy,"J·m⁻³"),metric("Impédance du vide",Z0,"Ω")],
        charts=[chart("E et cB : mêmes unités, directions transverses","z/λ","V·m⁻¹",series("Eₓ",z,E[:,0]),series("Eᵧ",z,E[:,1]),series("cBₓ",z,C*B[:,0]),series("cBᵧ",z,C*B[:,1])),
                chart("Le flux instantané et sa moyenne temporelle","z/λ","W·m⁻²",series("S_z(t)",z,S),series("⟨S_z⟩",z,Smean)),
                chart("Stockage électrique et magnétique","z/λ","J·m⁻³",series("u électrique",z,uE),series("u magnétique",z,uB),series("u total",z,uE+uB))],
        scene=scene("wave","Les champs sont transverses à +z","Les flèches E et B sont des champs instantanés ; leur orientation ne représente pas une trajectoire de particule.",
                    z_over_lambda=z,phase=p["phase"],mode=p["mode"],ellipticity=ell,E=E,cB=C*B,poynting=S,mean_poynting=Smean,amplitude=E0,wavelength_m=wavelength),
        steps=["Pour une onde +z : B=(u_z×E)/c et S=E×B/μ₀.",
               "Le mode stationnaire additionne deux amplitudes électriques égales, avec la même base de Jones et des directions opposées.",
               "La moyenne porte sur une période : ⟨S⟩=0 dans la superposition stationnaire, même si S(t) est localement non nul.",
               "u=ε₀|E|²/2+|B|²/(2μ₀) ; Maxwell donne ∂tu+∂zS_z=0 dans le vide."],
        assumptions=[CONVENTION,"Ondes planes infinies dans le vide ; E₀ est l'amplitude de chacune des ondes, pas celle de leur somme.",
                     "Les constantes μ₀ et mₑ sont issues de CODATA 2022, et ε₀=1/(μ₀c²) ; μ₀ n'est plus une constante SI exacte."])


def fresnel(n1,n2,angle_deg,polarization="TE"):
    angle=np.deg2rad(np.asarray(angle_deg));si=np.sin(angle);ci=np.cos(angle)
    st=n1*si/n2;ct=passive_sqrt(1-st*st)
    if polarization=="TE":
        denominator=n1*ci+n2*ct;r=(n1*ci-n2*ct)/denominator;t=2*n1*ci/denominator
    elif polarization=="TM":
        denominator=n2*ci+n1*ct;r=(n2*ci-n1*ct)/denominator;t=2*n1*ci/denominator
    else:raise ValueError("Polarisation TE ou TM attendue.")
    R=np.abs(r)**2;T=n2*ct.real/(n1*ci)*np.abs(t)**2
    return r,t,R,T,ct,st


def compute_interfaces(p):
    n1,n2=p["n1"],p["n2"];angle=p["angle"];pol=p["polarization"]
    r,t,R,T,ct,st=fresnel(n1,n2,angle,pol);ci=math.cos(math.radians(angle));si=math.sin(math.radians(angle))
    evanescent=bool(ct.imag>0);theta_t=None if evanescent else math.degrees(math.asin(min(1,float(st))))
    if pol=="TE":
        residual_E=abs(1+r-t);residual_H=abs(n1*ci*(1-r)-n2*ct*t)
    else:
        residual_E=abs(ci*(1-r)-ct*t);residual_H=abs(n1*(1+r)-n2*t)
    angles=np.linspace(0,89,241);rs,ts,Rs,Ts,*_=fresnel(n1,n2,angles,"TE");rp,tp,Rp,Tp,*_=fresnel(n1,n2,angles,"TM")
    z=np.linspace(0,3,181);normal_phase=2*np.pi*n2*ct*z;transmitted=t*np.exp(1j*normal_phase)
    critical=math.degrees(math.asin(n2/n1)) if n1>n2 else None
    return dict(metrics=[metric("Réflexion de flux R",float(R)),metric("Transmission normale T",float(T)),metric("R+T",float(R+T)),
                         metric("Angle de Brewster TM",math.degrees(math.atan(n2/n1)) if n1!=n2 else "Indices égaux : pas d'angle isolé","°"),metric("Angle critique",critical if critical is not None else "Pas de réflexion totale","°"),
                         metric("Écart des raccords tangents",float(max(residual_E,residual_H))),
                         metric("Phase de r",float(np.angle(r)) if abs(r)>1e-13 else "Indéfinie : amplitude nulle","rad")],
        charts=[chart("Deux polarisations, deux réflexions","Incidence (°)","Fraction de flux",series("R TE",angles,Rs),series("R TM",angles,Rp),series("T choisi",angles,Ts if pol=="TE" else Tp)),
                chart("Champ transmis à coordonnée tangentielle fixée","z/λ₀","Amplitude rapportée à E incident",series("Re E transmis",z,transmitted.real),series("Im E transmis",z,transmitted.imag),series("Enveloppe |E|",z,np.abs(transmitted)))],
        scene=scene("interface","Réfléchir, transmettre, ou décroître","Le plan est z=0. En réflexion totale, la phase se propage tangentiellement et l'enveloppe décroît dans +z ; aucun rayon normal propagatif n'est inventé.",
                    angle=angle,theta_t=theta_t,n1=n1,n2=n2,polarization=pol,incident=[si,0,ci],reflected=[si,0,-ci],
                    transmitted=None if evanescent else [float(st),0,float(ct.real)],R=float(R),T=float(T),evanescent=evanescent,
                    normal_decay_per_wavelength=float(2*np.pi*n2*ct.imag),r=[float(r.real),float(r.imag)],t=[float(t.real),float(t.imag)],wavelength_m=p["wavelength"]*1e-9),
        steps=["Snell : n₁ sin θᵢ=n₂ sin θₜ ; choisir cos θₜ avec partie imaginaire positive en réflexion totale.",
               "TE : r=(n₁ cos θᵢ−n₂ cos θₜ)/(n₁ cos θᵢ+n₂ cos θₜ). TM utilise la base p=u_y×k̂, différente pour les trois rayons.",
               "TM : r=(n₂ cos θᵢ−n₁ cos θₜ)/(n₂ cos θᵢ+n₁ cos θₜ). Le signe à incidence normale diffère de TE parce que p réfléchi change sa composante tangentielle.",
               "R=|r|² ; T=Re(n₂cos θₜ)/(n₁cos θᵢ)|t|². Les deux continuités tangentielles certifient R+T=1."],
        assumptions=[CONVENTION,"Deux milieux isotropes, non magnétiques, d'indices réels positifs et sans absorption ; interface plane infinie.",
                     "En TM, t et r sont les coefficients dans les bases p indiquées, pas seulement les composantes cartésiennes Ex.",REFERENCES["fresnel"]])


def guide_beta(width,frequency):
    k0=2*np.pi*frequency/C;kc=np.pi/width
    value=k0*k0-kc*kc
    if abs(value)<1e-12*max(k0*k0,kc*kc):value=0.
    return complex(passive_sqrt(value)),kc,k0


def compute_guide(p):
    a=p["width"]*1e-3;f=p["frequency"]*1e9;omega=2*np.pi*f;E0=p["amplitude"]
    beta,kc,k0=guide_beta(a,f);cutoff=C/(2*a);propagating=beta.real>0
    x=np.linspace(0,1,45);z=np.linspace(0,p["length"],91);X,Z=np.meshgrid(x*a,z*a)
    ph=np.exp(1j*beta*Z-2j*np.pi*p["phase"])
    Ey=E0*np.sin(kc*X)*ph;Bx=-beta/omega*Ey;Bz=-1j*kc/omega*E0*np.cos(kc*X)*ph
    power=beta.real/omega*E0**2*a/(4*MU0)
    fs=np.linspace(.15,2.2,241);b=passive_sqrt(fs*fs-1)
    above=fs[fs>1];vg=C*np.sqrt(1-1/above**2);vp=C/np.sqrt(1-1/above**2)
    return dict(metrics=[metric("Fréquence de coupure",cutoff/1e9,"GHz"),metric("Régime","Propagatif" if propagating else "Coupure" if beta==0 else "Évanescent"),
                         metric("Re β",beta.real,"m⁻¹"),metric("Im β",beta.imag,"m⁻¹"),metric("Puissance moyenne par hauteur",power,"W·m⁻¹"),
                         metric("Vitesse de groupe",C*beta.real/k0 if propagating else "Pas de vitesse de groupe propagative","m·s⁻¹"),
                         metric("Vitesse de phase",omega/beta.real if propagating else "Non définie pour une onde évanescente","m·s⁻¹")],
        charts=[chart("Le confinement modifie la dispersion","f/fc","β/(π/a)",series("Re β",fs,b.real),series("Im β",fs,b.imag)),
                chart("Profil transverse au plan z=0","x/a","V·m⁻¹",series("Eᵧ",x,Ey[0].real),series("cBₓ",x,C*Bx[0].real),series("cB_z",x,C*Bz[0].real)),
                chart("Vitesses seulement dans le domaine propagatif","f/fc","Vitesse / c",series("vg/c",above,vg/C),series("vp/c",above,vp/C))],
        scene=scene("guide","TE₁₀ : une composante B longitudinale","Ey s'annule aux parois x=0 et a. Les tableaux donnent les champs à l'instant choisi, pas un écoulement.",
                    x_over_a=x,z_over_a=z,Ey=Ey.real,cBx=C*Bx.real,cBz=C*Bz.real,cutoff_ghz=cutoff/1e9,propagating=propagating,
                    beta_real=beta.real,beta_imag=beta.imag,phase=p["phase"],amplitude=E0,width_m=a),
        steps=["Ey=E₀sin(πx/a) exp(iβz−iωt) et β²=ω²/c²−π²/a².",
               "Faraday ∇×E=iωB donne Bx=−βEy/ω et Bz=−i(π/a)E₀cos(πx/a)exp(iβz−iωt)/ω.",
               "⟨Sz⟩=Re β |Ey|²/(2μ₀ω). Intégrer sin² sur [0,a] donne la puissance par unité de hauteur.",
               "Au-dessus de fc : vg=c²β/ω<c et vp=ω/β>c, avec vg·vp=c². Ces vitesses ne s'appliquent pas sous la coupure."],
        assumptions=[CONVENTION,"Guide métallique parfait, vide à l'intérieur, mode TE₁₀ isolé. L'affichage n'additionne pas les modes supérieurs même quand ils pourraient se propager.",
                     "Sous la coupure, on garde la solution décroissante dans un guide semi-infini ; un tronçon fini raccordé à deux ports pourrait transmettre par effet tunnel."])


def aperture_pattern(angle_deg,aperture_ratio,steering_deg=0):
    return np.sinc(aperture_ratio*(np.sin(np.deg2rad(angle_deg))-math.sin(math.radians(steering_deg))))**2


def compute_antenne(p):
    q=p["aperture"];theta0=p["steering"];angles=np.linspace(-90,90,601);gain=aperture_pattern(angles,q,theta0)
    s0=math.sin(math.radians(theta0));zeros=[]
    for sign in (-1,1):
        value=s0+sign/q
        if -1<=value<=1:zeros.append(math.degrees(math.asin(value)))
    lo,hi=0.,math.pi
    for _ in range(70):
        mid=(lo+hi)/2
        if np.sinc(mid/np.pi)**2>.5:lo=mid
        else:hi=mid
    half_sine=(lo+hi)/(2*np.pi*q)
    hpbw=math.degrees(math.asin(s0+half_sine)-math.asin(s0-half_sine)) if -1<=s0-half_sine and s0+half_sine<=1 else None
    return dict(metrics=[metric("Largeur physique de l'ouverture",q*p["wavelength"],"mm"),metric("Maximum dans la direction choisie",1),
                         metric("Premiers zéros voisins",", ".join(f"{v:.5g}" for v in zeros) if zeros else "Aucun dans le domaine visible","°"),
                         metric("Largeur à mi-puissance",hpbw if hpbw is not None else "Les deux points ne sont pas visibles","°")],
        charts=[chart("Une coupe du diagramme de Fraunhofer","Angle θ (°)","Intensité / maximum",series("Ouverture uniforme",angles,gain)),
                chart("La variable naturelle est sin θ","sin θ−sin θ₀","Intensité / maximum",series("sinc²[π(a/λ)Δsin θ]",np.sin(np.deg2rad(angles))-s0,gain))],
        scene=scene("antenna","L'ouverture fixe les lobes angulaires","Le rayon du diagramme représente une intensité normalisée ; c'est une coupe angulaire et pas un vecteur champ électrique.",
                    angles=angles,gain=gain,steering=theta0,aperture_mm=q*p["wavelength"],wavelength_mm=p["wavelength"],zeros=zeros),
        steps=["L'amplitude est l'intégrale de exp(ikx(sin θ−sin θ₀)) sur une ouverture uniforme de largeur a.",
               "Son carré normalisé vaut sinc²[π(a/λ)(sin θ−sin θ₀)] ; ici sinc u=sin u/u.",
               "Les zéros voisins satisfont sin θ=sin θ₀±λ/a. Ne les afficher que si cette valeur appartient à [−1,1].", 
               "La largeur à mi-puissance est calculée dans l'angle exact ; l'approximation θ≈sin θ n'est pas imposée."],
        assumptions=["Modèle scalaire de diffraction de Fraunhofer, ouverture linéaire uniforme et phase de pointage imposée.",
                     "Distance d'observation très supérieure à a²/λ ; la coupe ne fournit pas à elle seule la directivité d'une antenne 3D."])


def drude_epsilon(ratio,collision):
    r=np.asarray(ratio,dtype=float)
    return 1-1/(r*(r+1j*collision))


def compute_plasma(p):
    wp=math.sqrt(p["density"]*1e18*E_CHARGE**2/(EPS0*ME));omega=p["ratio"]*wp;nu=p["collision"]*wp
    epsilon=complex(drude_epsilon(p["ratio"],p["collision"]));n=complex(passive_sqrt(epsilon));k=omega*n/C
    sigma=EPS0*wp*wp/(nu-1j*omega);length=p["length"]*.01;E0=p["amplitude"]
    # Éviter une onde artificiellement lente par aliasing aux grandes densités.
    # Le catalogue borne ce compte sous 6800 ; aucune fenêtre n'est tronquée.
    spatial_intervals=max(240,math.ceil(16*k.real*length/(2*np.pi)),math.ceil(12*k.imag*length))
    z=np.linspace(0,length,spatial_intervals+1)
    amplitude=E0*np.exp(1j*k*z-2j*np.pi*p["phase"]);flux=n.real/(2*Z0)*E0**2*np.exp(-2*k.imag*z)
    joule=.5*sigma.real*E0**2*np.exp(-2*k.imag*z)
    ratio=np.linspace(.1,3,241);eps=drude_epsilon(ratio,p["collision"]);index=passive_sqrt(eps)
    balance=float(np.max(np.abs(joule-2*k.imag*flux)))
    return dict(metrics=[metric("Fréquence plasma",wp/(2*np.pi*1e9),"GHz"),metric("Re εr",epsilon.real),metric("Im εr",epsilon.imag),
                         metric("Re n",n.real),metric("Im n",n.imag),metric("Profondeur d'amplitude 1/Im k",1/k.imag if k.imag>0 else "Pas d'atténuation","m"),
                         metric("Flux à z=0",float(flux[0]),"W·m⁻²"),metric("Écart local perte de flux / Joule",balance,"W·m⁻³")],
        charts=[chart("Drude : la réponse complexe des électrons","ω/ωp","Permittivité relative",series("Re εr",ratio,eps.real),series("Im εr",ratio,eps.imag)),
                chart("Choisir la branche passive de l'indice","ω/ωp","Indice complexe",series("Re n",ratio,index.real),series("Im n",ratio,index.imag)),
                chart("Onde et enveloppe dans le plasma","z (cm)","V·m⁻¹",series("E réel",z*100,amplitude.real),series("Enveloppe",z*100,np.abs(amplitude))),
                chart("Poynting décroît quand il y a absorption","z (cm)","W·m⁻²",series("Flux moyen",z*100,flux))],
        scene=scene("wave","Drude : la phase et l'enveloppe ont des rôles distincts","Le plasma est non magnétisé et froid. E₀ est imposé au bord de ce modèle de volume ; une interface d'entrée n'est pas raccordée ici.",
                    model="plasma",z_m=z,E=amplitude.real,envelope=np.abs(amplitude),poynting=flux,joule=joule,k_real=k.real,k_imag=k.imag,
                    frequency_hz=omega/(2*np.pi),phase=p["phase"],amplitude=E0),
        steps=["m(v̇+νv)=−eE donne σ=ε₀ωp²/(ν−iω).",
               "εr=1+iσ/(ε₀ω)=1−ωp²/[ω(ω+iν)] ; Im εr≥0 lorsque ν≥0.",
               "k=(ω/c)√εr, branche Im k≥0 ; les champs décroissent comme exp(−Im k z).",
               "⟨Sz⟩=Re n |E|²/(2Z₀), ⟨j·E⟩=Re σ |E|²/2 et −d⟨Sz⟩/dz=⟨j·E⟩.",
               "Sans collision : ω>ωp est propagatif ; ω<ωp est évanescent avec flux normal moyen nul et sans dissipation."],
        assumptions=[CONVENTION,"Électrons libres, ions immobiles, réponse linéaire locale, plasma froid non magnétisé ; ν est une constante phénoménologique.",
                     "Avec ν>0 la coupure idéale est arrondie ; on ne prétend pas qu'une onde absorbée possède une vitesse de groupe de transport réelle universelle.",REFERENCES["drude"]])


def lorentz_epsilon(ratio,strength,damping,epsilon_inf=1):
    r=np.asarray(ratio,dtype=float)
    return epsilon_inf+strength/(1-r*r-1j*damping*r)


def dielectric_sphere(epsilon_static,E_external,radius):
    E_internal=3*E_external/(epsilon_static+2)
    polarization=EPS0*(epsilon_static-1)*E_internal
    dipole=4*np.pi*radius**3/3*polarization
    return E_internal,polarization,dipole


def compute_dielectrique(p):
    epsilon=complex(lorentz_epsilon(p["ratio"],p["strength"],p["damping"],p["epsilon_inf"]));n=complex(passive_sqrt(epsilon))
    polarization=EPS0*(epsilon-1)*p["field"]
    ratio=np.linspace(.05,2.5,301);eps=lorentz_epsilon(ratio,p["strength"],p["damping"],p["epsilon_inf"]);indices=passive_sqrt(eps)
    static=p["epsilon_inf"]+p["strength"];a=p["radius"]*.001;Ein,Pstatic,dipole=dielectric_sphere(static,p["field"],a)
    theta=np.linspace(0,180,181);bound=Pstatic*np.cos(np.deg2rad(theta))
    coords=np.linspace(-3*a,3*a,45);X,Z=np.meshgrid(coords,coords);r2=X*X+Z*Z;outside=r2>=a*a
    safe=np.where(outside,r2,a*a);factor=dipole/(4*np.pi*EPS0*safe**2.5)
    Ex=np.where(outside,3*factor*X*Z,0);Ez=np.where(outside,p["field"]+factor*(3*Z*Z-safe),Ein)
    return dict(metrics=[metric("Re εr",epsilon.real),metric("Im εr",epsilon.imag),metric("Re n",n.real),metric("Im n",n.imag),
                         metric("Polarisation harmonique |P|",abs(polarization),"C·m⁻²"),metric("E interne, sphère statique",Ein,"V·m⁻¹"),
                         metric("Polarisation de la sphère statique",Pstatic,"C·m⁻²"),metric("Charge liée volumique",0,"C·m⁻³")],
        charts=[chart("Lorentz : dispersion et absorption","ω/ω₀","Permittivité relative",series("Re εr",ratio,eps.real),series("Im εr",ratio,eps.imag)),
                chart("L'indice complexe suit la branche passive","ω/ω₀","Indice",series("Re n",ratio,indices.real),series("Im n",ratio,indices.imag)),
                chart("Charges liées à la surface : limite statique","Angle au pôle +z (°)","σ liée (C·m⁻²)",series("P statique cos θ",theta,bound))],
        field=dict(title="Champ électrostatique de la sphère dans E extérieur",x=coords,y=coords,u=Ex,v=Ez,scalar=np.hypot(Ex,Ez),scalar_label="|E| (V·m⁻¹)",x_unit="m",y_unit="m",x_label="x",y_label="z",vector_unit="V·m⁻¹",vector_label="E",geometry="sphere"),
        scene=scene("material","Réponse harmonique et charges liées statiques","Les courbes sont harmoniques ; la sphère est calculée séparément avec εr(0), sans assimiler un problème électrostatique à une onde de volume.",
                    model="lorentz",epsilon=[epsilon.real,epsilon.imag],index=[n.real,n.imag],P=[polarization.real,polarization.imag],
                    bound_charge_angles=theta,bound_charge=bound,sphere_radius_m=a,static_polarization=Pstatic,static_internal_field=Ein),
        steps=["Un électron lié vérifie m(r̈+γṙ+ω₀²r)=−eE ; P=−ne r donne χ=χ₀/(1−(ω/ω₀)²−iγ ω/ω₀²).",
               "D=ε₀εrE, P=ε₀(εr−1)E ; Im εr≥0 assure une absorption positive pour la convention choisie.",
               "ρ liée=−div P et σ liée=P·n. Une polarisation uniforme de la sphère donne ρ liée=0 et σ liée=P cos θ.",
               "La continuité de E tangent et de D normal sans charge libre donne E interne=3E externe/(εr(0)+2)."],
        assumptions=[CONVENTION,"Oscillateur de Lorentz linéaire, homogène, isotrope et amorti ; la permittivité de fond est réelle positive.",
                     "Sphère statique homogène dans le vide, sans charge libre ; le champ extérieur total est le champ uniforme ajouté au dipôle induit."])


def langevin(x):
    x=np.asarray(x,dtype=float);small=np.abs(x)<1e-3
    safe=np.where(small,1.,x)
    regular=1/np.tanh(safe)-1/safe
    return np.where(small,x/3-x**3/45+2*x**5/945,regular)


def magnetization_law(H,temperature,density,moment,model,radius):
    H=np.asarray(H,dtype=float)
    if model=="dia":
        chi=-MU0*density*E_CHARGE**2*radius**2/(6*ME)
        return chi*H
    argument=moment*MU0*H/(KB*temperature)
    return density*moment*(langevin(argument) if model=="classique" else np.tanh(argument))


def magnetic_internal(H_external,temperature,density,moment,model,radius,demag):
    ext=np.asarray(H_external,dtype=float)
    if model=="dia":
        chi=-MU0*density*E_CHARGE**2*radius**2/(6*ME);internal=ext/(1+demag*chi)
    else:
        lo=np.zeros_like(ext);hi=np.abs(ext)
        for _ in range(70):
            mid=(lo+hi)/2;M=magnetization_law(mid,temperature,density,moment,model,radius)
            residual=mid+demag*M-np.abs(ext)
            lo=np.where(residual<0,mid,lo);hi=np.where(residual>=0,mid,hi)
        internal=np.sign(ext)*(lo+hi)/2
    M=magnetization_law(internal,temperature,density,moment,model,radius)
    return internal,M


def compute_aimantation(p):
    T=p["temperature"];density=p["density"]*1e27;moment=p["moment"]*MU_B;radius=p["radius"]*1e-12;model=p["model"];N=p["demag"]
    Hext=p["field"]/MU0;Hin,M=magnetic_internal(Hext,T,density,moment,model,radius,N)
    def susceptibility(temp):
        if model=="dia":return np.full_like(np.asarray(temp,dtype=float),-MU0*density*E_CHARGE**2*radius**2/(6*ME))
        return MU0*density*moment**2/(KB*np.asarray(temp)*(3 if model=="classique" else 1))
    chi=float(susceptibility(T));fields=np.linspace(-5,5,241);h,m=magnetic_internal(fields/MU0,T,density,moment,model,radius,N)
    temperatures=np.linspace(1,500,241);chi_curve=susceptibility(temperatures)
    residual=float(Hin+N*M-Hext)
    return dict(metrics=[metric("Aimantation M",float(M),"A·m⁻¹"),metric("Champ interne H",float(Hin),"A·m⁻¹"),
                         metric("Champ extérieur H",Hext,"A·m⁻¹"),metric("χ intrinsèque à faible champ",chi),metric("χ apparente χ/(1+Nχ)",chi/(1+N*chi)),
                         metric("Écart H interne + NM − H externe",residual,"A·m⁻¹")],
        charts=[chart("Réponse à un champ extérieur","μ₀H externe (T)","M (A·m⁻¹)",series("Modèle avec démagnétisation",fields,m)),
                chart("Susceptibilité dans la limite de champ nul","T (K)","χ",series("Intrinsèque",temperatures,chi_curve),series("Apparente",temperatures,chi_curve/(1+N*chi_curve)))],
        scene=scene("material","Le champ interne doit être calculé avec M","Moments indépendants ou orbites liées isotropes ; la fermeture scalaire représente un ellipsoïde uniformément aimanté suivant un axe principal.",
                    model="magnetization",magnetic_model=model,H_external=Hext,H_internal=float(Hin),M=float(M),demag=N,temperature=T,susceptibility=chi),
        steps=["Langevin : M=nμ[coth x−1/x], x=μ μ₀H interne/(kBT). Pour deux niveaux ±μ : M=nμ tanh x.",
               "À faible champ, χ classique=nμ₀μ²/(3kBT), contre nμ₀μ²/(kBT) pour les deux niveaux.",
               "Diamagnétisme orbital classique isotrope : χ=−μ₀ne²⟨r²⟩/(6mₑ), indépendant de T dans ce modèle.",
               "Résoudre H interne=H externe−NM. La pente apparente au champ nul vaut χ/(1+Nχ)."],
        assumptions=["Le champ saisi est μ₀H externe, pas le champ B interne. Ici B interne=μ₀(H interne+M).",
                     "Pas d'interactions entre moments, de domaines ni de ferromagnétisme. Le modèle tanh représente deux niveaux, pas une fonction de Brillouin pour tout spin.",
                     "Le rayon orbital est un rayon quadratique effectif ⟨r²⟩¹ᐟ² ; en mode dia la densité compte les électrons liés effectifs.",
                     "La courbe χ(T) est une dérivée à champ nul ; elle ne représente pas la pente au champ extérieur non nul sélectionné."])


def london_profile(x,halfwidth,penetration,B0):
    x=np.asarray(x);u=np.abs(x)/penetration;A=halfwidth/penetration
    positive=np.exp(u-A);negative=np.exp(-u-A);denominator=1+np.exp(-2*A)
    B=B0*(positive+negative)/denominator
    derivative=B0/penetration*np.sign(x)*(positive-negative)/denominator
    return B,-derivative/MU0


def compute_meissner(p):
    a=p["halfwidth"]*1e-9;length=p["penetration"]*1e-9;B0=p["field"]*1e-3;x=np.linspace(-a,a,min(1201,max(401,int(12*a/length)+1)))
    B,j=london_profile(x,a,length,B0);Bc=float(london_profile(0,a,length,B0)[0]);initial=B0 if p["history"]=="refroidi_champ" else 0.
    Kright=-(B0-Bc)/MU0
    return dict(metrics=[metric("B au centre",Bc*1000,"mT"),metric("Rapport B centre / B₀",Bc/B0 if B0 else 1/math.cosh(a/length)),
                         metric("Courant intégré sur la demi-plaque droite",Kright,"A·m⁻¹"),metric("Courant intégré sur toute la plaque",0,"A·m⁻¹"),
                         metric("Champ du conducteur parfait idéal",initial*1000,"mT")],
        charts=[chart("La pénétration part des deux faces","x (nm)","Bz (mT)",series("London : supraconducteur",x*1e9,B*1000),series("Conducteur parfait : flux initial gelé",x*1e9,np.full_like(x,initial*1000))),
                chart("Les courants des faces sont opposés","x (nm)","jy (A·m⁻²)",series("−∂xBz / μ₀",x*1e9,j))],
        scene=scene("london","Meissner et mémoire du conducteur parfait","B est dirigé suivant z, parallèle aux faces x=±a. Le courant est suivant y et change de signe entre les deux faces.",
                    x_nm=x*1e9,B_mT=B*1000,jy=j,B_perfect_mT=initial*1000,a_nm=p["halfwidth"],lambda_nm=p["penetration"],history=p["history"]),
        steps=["London statique et Ampère donnent d²Bz/dx²=Bz/λL², avec Bz(−a)=Bz(a)=B₀.",
               "La solution symétrique est Bz=B₀cosh(x/λL)/cosh(a/λL) ; les exponentielles relatives évitent les débordements.",
               "curl B=(0,−∂xBz,0) : jy=−Bz′/μ₀. Intégrer entre 0 et a donne Ky=−(B₀−Bcentre)/μ₀.",
               "Conducteur parfait idéal : E=0 implique ∂tB=0, et non nécessairement B=0. Le Meissner est une propriété d'équilibre distincte."],
        assumptions=["Plaque infinie dans y,z, régime statique London, sans vortex ni dépassement du champ critique ; B₀ est imposé également sur les deux faces.",
                     "Les courants calculés sont des densités réparties dans la plaque. Leur intégrale est un courant par longueur, pas une densité surfacique delta ajoutée au modèle.",
                     "La comparaison de conducteur parfait est un modèle de conservation du champ initial dans le volume ; elle n'est pas une évolution dissipative vers Meissner."])


def jones_rotation(theta):
    return np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])


def compute_faraday(p):
    L=p["length"]*.01;theta=p["verdet"]*p["field"]*L;passes=2 if p["passes"]=="double" else 1
    initial=math.radians(p["initial"]);analyzer=math.radians(p["analyzer"])
    input=np.array([math.cos(initial),math.sin(initial)]);output=jones_rotation(passes*theta)@input
    transmission=float((np.array([math.cos(analyzer),math.sin(analyzer)])@output)**2)
    wavelength=p["wavelength"]*1e-9;difference=p["verdet"]*p["field"]*wavelength/np.pi
    distance=np.linspace(0,passes*L,181);faraday_angle=initial+p["verdet"]*p["field"]*distance
    reciprocal_angle=initial+p["verdet"]*p["field"]*(distance if passes==1 else np.where(distance<=L,distance,2*L-distance))
    analyzer_angles=np.linspace(-90,90,181);curve=np.cos(initial+passes*theta-np.deg2rad(analyzer_angles))**2
    return dict(metrics=[metric("Rotation d'un passage",math.degrees(theta),"°"),metric("Rotation totale",math.degrees(passes*theta),"°"),
                         metric("Transmission de l'analyseur",transmission),metric("n− − n+ déduit de Verdet",difference),
                         metric("Norme Jones finale",float(output@output))],
        charts=[chart("Les rotations du retour : axes de laboratoire fixes","Chemin cumulé (cm)","Angle du champ linéaire (°)",series("Faraday",distance*100,np.rad2deg(faraday_angle)),series("Rotation réciproque",distance*100,np.rad2deg(reciprocal_angle))),
                chart("Lire la polarisation avec un analyseur","Angle analyseur (°)","Transmission normalisée",series("Loi de Malus",analyzer_angles,curve))],
        scene=scene("faraday","Deux phases circulaires font tourner une droite","e±=(ex±i ey)/√2. θ=(k−−k+)L/2 ; le retour utilise les mêmes axes ex,ey fixes dans le laboratoire.",
                    theta_single=theta,theta_total=passes*theta,input=input,output=output,passes=passes,analyzer=analyzer,transmission=transmission,
                    circular_difference=difference,verdet=p["verdet"],field=p["field"],length_m=L),
        steps=["Le modèle de Verdet pose θ=VBL ; il absorbe la dépendance spectrale et matérielle dans V.",
               "Dans e±=(ex±i ey)/√2, les phases exp(ik±L) donnent la rotation θ=(k−−k+)L/2.",
               "La matrice dans les axes fixes est R(θ). Au retour, Faraday donne R(θ)R(θ)=R(2θ), à une phase de miroir globale sans effet sur Malus.",
               "Une rotation réciproque idéale donne au contraire R(−θ)R(θ)=I. L'intensité analysée vaut cos²(φinitial+θtotal−φanalyseur)."],
        assumptions=[CONVENTION,"Milieu transparent sans dichroïsme, champ longitudinal uniforme, Verdet réel imposé ; la valeur ne prétend pas modéliser sa dispersion près d'une résonance.",
                     "Retour par un miroir idéal à incidence normale, phase de réflexion commune aux deux composantes. Les bases locales attachées au sens de propagation demanderaient une conversion supplémentaire."])


def kerr_soliton_parameters(wavelength,n0,n2,intensity):
    k0=2*np.pi/wavelength;delta=n2*intensity
    A=k0*k0*n0*delta;beta=n0*n0*EPS0*C*n2;E0=math.sqrt(2*intensity/(n0*EPS0*C))
    width=1/math.sqrt(A);k=math.sqrt(n0*n0*k0*k0+A)
    return width,k,E0,A,beta


def compute_kerr(p):
    wavelength=p["wavelength"]*1e-6;n0=p["n0"];n2=p["n2"]*1e-20;I0=p["intensity"]*1e13
    width,k,E0,A,beta=kerr_soliton_parameters(wavelength,n0,n2,I0);k0=2*np.pi/wavelength
    transverse=np.linspace(-6,6,241);amplitude=1/np.cosh(transverse);intensity=amplitude**2
    index=np.sqrt(n0*n0+2*n0*n2*I0*intensity)
    distance=p["distance"];spread=math.sqrt(1+distance**2)
    flux_factor=k/(n0*k0)
    linear=2*flux_factor/np.sqrt(np.pi)/spread*np.exp(-transverse**2/spread**2)
    distances=np.linspace(0,3,151)
    normalized_residual=amplitude*(1-2*amplitude**2)-amplitude+2*amplitude**3
    return dict(metrics=[metric("Largeur sech y₀",width*1e6,"µm"),metric("Indice effectif k/k₀",k/k0),metric("Indice au sommet",float(index.max())),
                         metric("Champ au sommet E₀",E0,"V·m⁻¹"),metric("Intensité de référence I₀",I0,"W·m⁻²"),
                         metric("Flux intégré par largeur x",2*I0*width*k/(n0*k0),"W·m⁻¹"),metric("Écart ODE normalisée",float(np.max(np.abs(normalized_residual))))],
        charts=[chart("Sech : localisation et puissance","y/y₀","Grandeur normalisée",series("E/E₀",transverse,amplitude),series("Flux sech / I₀",transverse,flux_factor*intensity),series("Flux Gauss / I₀, même puissance",transverse,linear)),
                chart("Le Kerr optique relève l'indice au centre","y/y₀","n(y)−n₀",series("Indice exact du modèle εr",transverse,index-n0)),
                chart("Référence de diffraction libre, même échelle initiale","z/(n₀k₀ y₀²)","Largeur / y₀",series("Solution sech stationnaire",distances,np.ones_like(distances)),series("Faisceau gaussien linéaire",distances,np.sqrt(1+distances**2)))],
        scene=scene("kerr","Une intensité localisée construit son guide","La solution est monochromatique et stationnaire ; le Gauss comparatif se diffracte dans un modèle paraxial linéaire avec même puissance initiale, et pas le même pic.",
                    transverse=transverse,amplitude=amplitude,intensity=flux_factor*intensity,reference_intensity=intensity,index=index,width_m=width,normalized_distance=distance,linear_intensity=linear,n0=n0,I0=I0),
        steps=["Le modèle harmonique εr,eff=n₀²+β|Ê|² utilise Iref=n₀ε₀c|Ê|²/2 et β=n₀²ε₀cn₂ ; il est cohérent à l'ordre faible avec n(I)=n₀+n₂I.",
               "Poser E(y,z,t)=Ef(y)exp(ikz−iωt) réduit Maxwell à Ef″=A Ef−βk₀²Ef³, A=k²−n₀²k₀²>0.",
               "L'intégrale première avec Ef et Ef′ nuls à l'infini donne (Ef′)²=A Ef²−βk₀²Ef⁴/2.",
               "Ef=E₀sech(y/y₀), y₀=1/√A et E₀²=2A/(βk₀²). L'intensité réelle de Poynting vaut k/(n₀k₀) Iref.",
               "Le Gauss libre comparatif a largeur y₀√(1+Z²), Z=z/(n₀k₀ y₀²). Son intensité I/I₀ vaut 2κ/[√π n₀k₀√(1+Z²)] exp[−(y/y₀)²/(1+Z²)], ce qui conserve exactement la puissance intégrée du sech."],
        assumptions=[CONVENTION,"Réduction monochromatique locale cubique focalisante, pertes et dispersion temporelle négligées ; la génération d'harmoniques est ignorée. β est un coefficient effectif harmonique : une loi instantanée PNL=ε₀χ³ E réel³ donnerait β=3χ³/4 après projection sur le fondamental.",
                     "I₀ et Iref sont définis avec l'indice linéaire n₀. Le flux physique du sech vaut κ/(n₀k₀) fois Iref ; la gaussienne de référence conserve ce flux intégré, et son pic initial est donc différent.",
                     "Auto-guidage dans une seule direction transverse ; pas une preuve de stabilité d'un faisceau 3D ni une simulation complète de propagation non linéaire.",
                     "Kerr optique = réponse à l'intensité de l'onde. Ne pas l'identifier au Kerr électro-optique sous champ statique, au Pockels ni au Kerr magnéto-optique.",
                     "Les intensités du modèle ne constituent pas une recommandation expérimentale : saturation, absorption et dommages matériels sont absents."])


def dipole_power(moment,omega):
    return moment**2*omega**4/(12*np.pi*EPS0*C**3)


SIGMA_THOMSON=E_CHARGE**4/(6*np.pi*EPS0**2*ME**2*C**4)


def bound_cross_section(ratio,damping):
    r=np.asarray(ratio,dtype=float)
    return SIGMA_THOMSON*r**4/((1-r*r)**2+damping*damping*r*r)


def compute_rayonnement(p):
    omega=2*np.pi*p["frequency"]*1e12;omega0=2*np.pi*p["resonance"]*1e12;gamma=p["damping"]*omega0
    moment=p["dipole"]*1e-29
    sigma=bound_cross_section(omega/omega0,p["damping"])
    if p["model"]=="lie":moment=abs(E_CHARGE**2*p["field"]/(ME*(omega0**2-omega**2-1j*gamma*omega)))
    power=dipole_power(moment,omega);theta=np.linspace(0,180,241);pattern=np.sin(np.deg2rad(theta))**2
    differential=3*power/(8*np.pi)*pattern
    ratio=np.geomspace(.02,100,241);cross=bound_cross_section(ratio,p["damping"])
    frequencies=np.geomspace(1,1000,181)*1e12
    powers=dipole_power(moment,2*np.pi*frequencies)
    incident=.5*EPS0*C*p["field"]**2
    return dict(metrics=[metric("Amplitude dipolaire p₀",moment,"C·m"),metric("Puissance rayonnée moyenne",power,"W"),
                         metric("Section de diffusion",float(sigma) if p["model"]=="lie" else "Non définie pour le dipôle imposé","m²"),
                         metric("Section Thomson",SIGMA_THOMSON,"m²"),metric("I incident × σ",float(incident*sigma) if p["model"]=="lie" else "Comparaison non applicable","W")],
        charts=[chart("Rayonner perpendiculairement au dipôle","Angle θ avec l'axe du dipôle (°)","dP/dΩ (W·sr⁻¹)",series("Diagramme dipolaire",theta,differential)),
                chart("Diffusion d'un électron lié","ω/ω₀","σ/σ Thomson",series("Rayleigh → résonance → Thomson",ratio,cross/SIGMA_THOMSON),x_scale="log",y_scale="log"),
                chart("Loi ω⁴ pour un moment p₀ maintenu constant","f (THz)","Puissance (W)",series("Dipôle imposé à l'amplitude sélectionnée",frequencies/1e12,powers),x_scale="log",y_scale="log")],
        scene=scene("radiation","Un diagramme de puissance, pas un champ radial","Le dipôle est dirigé suivant z. La coupe sin²θ représente dP/dΩ ; les champs rayonnés seraient transverses en coordonnées sphériques.",
                    angles=theta,pattern=pattern,total_power=power,source=p["model"],dipole_moment=moment,frequency_hz=p["frequency"]*1e12),
        steps=["Un dipôle p=p₀cos(ωt)u_z donne d⟨P⟩/dΩ=p₀²ω⁴sin²θ/(32π²ε₀c³).",
               "Intégrer sur une sphère : ∫sin²θdΩ=8π/3, d'où ⟨P⟩=p₀²ω⁴/(12πε₀c³).",
               "Pour l'électron lié, p₀=e²E₀/[mₑ|ω₀²−ω²−iγω|] et σ=σT r⁴/[(1−r²)²+(γ/ω₀)²r²].",
               "À r≪1, σ∝ω⁴ ; près de r=1, l'amortissement borne le pic ; à r≫1, σ→σT.",
               "L'intensité incidente est ε₀cE₀²/2 : la puissance diffusée de l'électron lié égale Iincident σ."],
        assumptions=[CONVENTION,"Rayonnement dipolaire électrique non relativiste dans le vide, loin de la source ; pas de champ proche ni de multipôles supérieurs.",
                     "Le diagramme θ est polarisé suivant l'axe du dipôle ; une moyenne de lumière non polarisée demanderait une autre distribution angulaire.",
                     "Le pic est celui d'un oscillateur amorti phénoménologique ; le tableau ne traite pas un atome quantique multirésonant.",REFERENCES["radiation"]])


def dynamo_growth(alpha,diffusivity,length,helicity=1):
    k=2*np.pi/length
    return helicity*alpha*k-diffusivity*k*k,k


def compute_dynamo(p):
    alpha=p["alpha"]*.001;eta=p["diffusivity"];L=p["length"]*1000;U=p["velocity"]*.001;B0=p["amplitude"]*.001;s=1 if p["helicity"]=="plus" else -1
    growth,k=dynamo_growth(alpha,eta,L,s);time=p["years"]*YEAR;logratio=growth*time/math.log(10)
    years=np.linspace(0,p["years"],181);logs=growth*years*YEAR/math.log(10)
    shape_z=np.linspace(0,1,181);shape=np.column_stack([np.cos(2*np.pi*shape_z),-s*np.sin(2*np.pi*shape_z),np.zeros_like(shape_z)])
    ks=np.geomspace(2*np.pi/(3500e3),2*np.pi/1000,241);gs=s*alpha*ks-eta*ks*ks
    initial_energy=B0**2/(2*MU0);induction_rate=2*s*alpha*k;diffusion_rate=2*eta*k*k
    amplitude_text=(B0*math.exp(growth*time)*1000) if -650<=growth*time<=650 else f"10^({math.log10(B0*1000)+logratio:.6g})"
    return dict(metrics=[metric("Rm=UL/ηm",U*L/eta),metric("Taux de croissance du mode",growth,"s⁻¹"),metric("Taux par année",growth*YEAR,"an⁻¹"),
                         metric("Temps diffusif du mode 1/(ηm k²)",1/(eta*k*k)/YEAR,"années"),metric("log₁₀(|B|/B₀)",logratio),
                         metric("Amplitude du mode",amplitude_text,"mT"),metric("Énergie initiale par volume",initial_energy,"J·m⁻³"),
                         metric("Production relative d'énergie",induction_rate,"s⁻¹"),metric("Dissipation relative d'énergie",diffusion_rate,"s⁻¹")],
        charts=[chart("Croissance exacte affichée sans débordement","Temps (années)","Logarithme décimal du rapport",series("log₁₀ |B/B₀|",years,logs),series("log₁₀ énergie/énergie initiale",years,2*logs)),
                chart("Une longueur d'onde peut croître, une autre décroître","k (m⁻¹)","Taux sαk−ηm k² (s⁻¹)",series("Mode d'hélicité choisi",ks,gs),x_scale="log"),
                chart("Une forme hélicoïdale, normalisée séparément de son amplitude","z/L","B/B amplitude",series("Bx",shape_z,shape[:,0]),series("By",shape_z,shape[:,1]))],
        scene=scene("dynamo","Induction et diffusion sur un mode prescrit","Le dessin est normalisé : son amplitude physique est donnée par le logarithme, sans limiter artificiellement une exponentielle. Il ne représente pas une géodynamo résolue.",
                    z_over_L=shape_z,B_normalized=shape,growth_rate=growth,log_amplitude_ratio=logratio,helicity=s,alpha=alpha,diffusivity=eta,initial_amplitude_T=B0,
                    relative_induction_energy=induction_rate,relative_diffusion_energy=diffusion_rate),
        steps=["MHD résistive : ∂tB=∇×(u×B)+ηmΔB, div B=0 et ηm=1/(μ₀σ).",
               "La fermeture locale à champ moyen remplace l'effet turbulent par une force électromotrice αB ; α constant donne ∂tB=α curl B+ηmΔB.",
               "Le mode B=(cos kz,−s sin kz,0) vérifie curl B=s kB et ΔB=−k²B : g=sαk−ηm k².",
               "L'énergie du mode est proportionnelle à B² : son taux relatif est 2g=2sαk−2ηm k². La production puise dans un écoulement ici prescrit, sans rétroaction de Lorentz.",
               "Rm mesure le rapport advection/diffusion sur l'échelle L ; un grand Rm avec α=0 ne fait pas croître ce mode. Une dynamo complète dépend des géométries, symétries et conditions aux limites."],
        assumptions=["Modèle local α² cinématique, coefficients uniformes et mode périodique : ni seuil universel de Rm, ni convection terrestre résolue, ni saturation non linéaire.",
                     "Le contrôle U sert seulement au repère Rm. α est prescrit indépendamment ; le laboratoire n'en déduit pas une statistique de turbulence.",
                     "Repère terrestre : les travaux de Gillet et al. (2010) discutent un champ interne de l'ordre de plusieurs mT, contre environ 0,3 mT pour la partie radiale résolue à la frontière noyau-manteau. Les valeurs choisies ici sont des scénarios, pas des mesures déduites du modèle.",
                     REFERENCES["dynamo"],REFERENCES["core"]])


COMPUTE={"maxwell":compute_maxwell,"interfaces":compute_interfaces,"guide":compute_guide,"antenne":compute_antenne,
         "plasma":compute_plasma,"dielectrique":compute_dielectrique,"aimantation":compute_aimantation,
         "meissner":compute_meissner,"faraday":compute_faraday,"kerr":compute_kerr,
         "rayonnement":compute_rayonnement,"dynamo":compute_dynamo}
