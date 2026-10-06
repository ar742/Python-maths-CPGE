"""Douze expériences d'ondes et de réponse des milieux : contrôles publics."""


def slider(key, label, lo, hi, step, value, unit=""):
    return dict(key=key,label=label,min=lo,max=hi,step=step,value=value,unit=unit,type="range")


def select(key, label, options, value):
    return dict(key=key,label=label,options=[dict(value=v,label=l) for v,l in options],value=value,unit="",type="select")


def preset(label, **values):
    return dict(label=label,values=values)


def lab(id_, title, category, intro, controls, presets):
    return dict(id=id_,title=title,category=category,intro=intro,controls=controls,presets=presets)


LABS = [
    lab("maxwell","Maxwell : transporter ou stocker l'énergie","Ondes",
        "Comparer une onde progressive à deux ondes opposées : E, B, énergie et flux instantané ne se confondent pas avec leurs moyennes temporelles.",[
            select("mode","Superposition",[("progressive","Onde progressive +z"),("stationnaire","Deux ondes opposées égales")],"progressive"),
            slider("frequency","Fréquence",.1,10,.1,1,"GHz"),slider("amplitude","Amplitude E₀ d'une onde",1,1000,1,100,"V·m⁻¹"),
            slider("ellipticity","Rapport des composantes en quadrature",-1,1,.05,0),slider("phase","Temps t/T",0,1,.01,.25)], [
                preset("Transport linéaire",mode="progressive",ellipticity=0,phase=.25),
                preset("Polarisation circulaire",mode="progressive",ellipticity=1,phase=.125),
                preset("Stockage stationnaire",mode="stationnaire",ellipticity=0,phase=.125)]),
    lab("interfaces","Fresnel : flux, Brewster et réflexion totale","Ondes",
        "Les amplitudes complexes raccordent les champs ; R et T mesurent les flux normaux. Une onde évanescente ne donne pas un flux transmis normal.",[
            slider("n1","Indice du milieu incident",.7,3,.05,1),slider("n2","Indice du milieu transmis",.7,3,.05,1.5),
            slider("angle","Angle d'incidence",0,89,.1,30,"°"),
            select("polarization","Polarisation",[("TE","TE : E perpendiculaire au plan"),("TM","TM : E dans le plan")],"TE"),
            slider("wavelength","Longueur d'onde dans le vide",400,1600,10,600,"nm")],[
                preset("Incidence normale",n1=1,n2=1.5,angle=0,polarization="TE"),
                preset("Brewster : TM",n1=1,n2=1.5,angle=56.309932474,polarization="TM"),
                preset("Réflexion totale",n1=1.5,n2=1,angle=60,polarization="TE")]),
    lab("guide","Guide TE₁₀ : propagation et coupure","Ondes",
        "Le confinement impose un nombre d'onde transverse. Sous la coupure, β est imaginaire et une exponentielle décroissante ne transporte pas de puissance moyenne vers +z.",[
            slider("width","Largeur a du guide",10,100,1,30,"mm"),slider("frequency","Fréquence",1,30,.1,8,"GHz"),
            slider("amplitude","Amplitude électrique E₀",1,1000,1,100,"V·m⁻¹"),
            slider("length","Longueur affichée z/a",1,10,.1,4),slider("phase","Temps t/T",0,1,.01,.25)],[
                preset("TE₁₀ propagatif",width=30,frequency=8,phase=.125),
                preset("Sous la coupure",width=30,frequency=3,phase=.125),
                preset("À la coupure",width=30,frequency=4.996540966666667,phase=.25)]),
    lab("antenne","Ouverture : un sinc² dans l'espace angulaire","Ondes",
        "Une ouverture uniforme et une rampe de phase donnent un diagramme de Fraunhofer en sin θ. Une ouverture plus petite que λ peut n'avoir aucun zéro visible.",[
            slider("aperture","Largeur a/λ",.2,12,.1,4),slider("wavelength","Longueur d'onde",1,100,1,30,"mm"),
            slider("steering","Direction de pointage",-60,60,1,0,"°")],[
                preset("Ouverture de quatre λ",aperture=4,steering=0),
                preset("Sous-longueur d'onde",aperture=.5,steering=0),
                preset("Pointage oblique",aperture=8,steering=30)]),
    lab("plasma","Plasma froid : coupure, collisions et absorption","Milieux",
        "Le modèle de Drude a une permittivité passive pour exp(−iωt). La bonne racine de k décroît dans +z ; le travail Joule correspond à la perte du flux de Poynting.",[
            slider("ratio","Pulsation ω/ωp",.1,3,.01,1.2),slider("collision","Fréquence de collision ν/ωp",0,1,.01,.05),
            slider("density","Densité électronique",.01,100,.01,1,"10¹⁸ m⁻³"),slider("amplitude","Amplitude à z=0",1,1000,1,100,"V·m⁻¹"),
            slider("length","Distance affichée",.1,30,.1,10,"cm"),slider("phase","Temps t/T",0,1,.01,.25)],[
                preset("Propagation sans collisions",ratio=1.5,collision=0),
                preset("Onde évanescente",ratio=.5,collision=0),
                preset("Collisions près de la coupure",ratio=1,collision=.2)]),
    lab("dielectrique","Lorentz et charges liées d'une sphère","Milieux",
        "Relier résonance, absorption et polarisation ; comparer cette réponse harmonique à la limite électrostatique d'une sphère diélectrique dans un champ uniforme.",[
            slider("ratio","Pulsation ω/ω₀",.05,2.5,.01,.8),slider("strength","Force d'oscillateur χ₀",.1,5,.1,1),
            slider("damping","Amortissement γ/ω₀",.01,.5,.01,.08),slider("epsilon_inf","Permittivité relative de fond",1,5,.1,1),
            slider("field","Champ imposé E₀",1,10000,10,1000,"V·m⁻¹"),slider("radius","Rayon de la sphère",.1,10,.1,2,"mm")],[
                preset("Sous la résonance",ratio=.5,damping=.05),
                preset("Résonance absorbante",ratio=1,damping=.1),
                preset("Au-dessus de la résonance",ratio=1.5,strength=2,damping=.05)]),
    lab("aimantation","Dia et paramagnétisme : modèle et champ interne","Milieux",
        "Comparer Langevin classique, spins à deux niveaux et diamagnétisme orbital. L'ellipsoïde uniforme impose H interne = H externe − N M ; ce modèle ne décrit pas le ferromagnétisme.",[
            select("model","Réponse magnétique",[("classique","Moments classiques : Langevin"),("quantique","Deux niveaux : tanh"),("dia","Diamagnétisme orbital")],"classique"),
            slider("temperature","Température",1,500,1,100,"K"),slider("field","μ₀H externe",-5,5,.05,1,"T"),
            slider("density","Densité de moments / électrons liés",.01,10,.01,1,"10²⁷ m⁻³"),
            slider("moment","Moment magnétique",.5,10,.5,1,"μB"),slider("radius","Rayon orbital quadratique effectif",30,300,10,100,"pm"),
            slider("demag","Facteur démagnétisant N",0,1,.01,1/3)],[
                preset("Langevin classique",model="classique",temperature=100,field=1),
                preset("Saturation de deux niveaux",model="quantique",temperature=2,field=5),
                preset("Courant orbital diamagnétique",model="dia",field=2,radius=150)]),
    lab("meissner","London : pénétration depuis les deux faces","Milieux",
        "Une plaque supraconductrice expulse le champ sur la longueur de London ; les courants des deux faces sont opposés. La conservation du flux d'un conducteur parfait dépend, elle, de l'histoire initiale.",[
            slider("halfwidth","Demi-épaisseur a",20,1000,10,200,"nm"),slider("penetration","Longueur λL",10,300,10,50,"nm"),
            slider("field","Champ extérieur B₀",-100,100,1,20,"mT"),
            select("history","Comparaison avec le conducteur parfait",[("refroidi_champ","Initialement plongé dans B₀"),("champ_apres","Initialement sans champ")],"refroidi_champ")],[
                preset("Plaque épaisse",halfwidth=500,penetration=50,history="refroidi_champ"),
                preset("Les deux faces interagissent",halfwidth=50,penetration=100),
                preset("Champ appliqué après",halfwidth=500,penetration=50,history="champ_apres")]),
    lab("faraday","Faraday : une rotation non réciproque","Milieux",
        "Les deux modes circulaires accumulent des phases différentes. Dans des axes de laboratoire fixes, l'aller-retour Faraday ajoute les rotations, alors qu'une rotation réciproque s'annule.",[
            slider("verdet","Constante de Verdet V",-500,500,10,100,"rad·T⁻¹·m⁻¹"),slider("field","Champ longitudinal B",-1,1,.05,.5,"T"),
            slider("length","Longueur du milieu",.1,20,.1,2,"cm"),slider("wavelength","Longueur d'onde",400,1000,10,633,"nm"),
            slider("initial","Angle initial",-90,90,1,0,"°"),slider("analyzer","Angle de l'analyseur",-90,90,1,90,"°"),
            select("passes","Trajet",[("simple","Un passage"),("double","Aller-retour : deux passages")],"simple")],[
                preset("Analyseurs croisés",verdet=100,field=.5,length=2,passes="simple"),
                preset("Retour non réciproque",verdet=100,field=.5,length=2,passes="double"),
                preset("Inverser B",verdet=100,field=-.5,length=2,passes="double")]),
    lab("kerr","Kerr optique : un profil sech auto-guidé","Milieux",
        "Le Kerr optique dépend de l'intensité de l'onde. Une réduction monochromatique localisée admet une solution sech ; elle n'est pas l'effet Kerr électro-optique dû à un champ statique.",[
            slider("wavelength","Longueur d'onde dans le vide",.4,2,.05,1,"µm"),slider("n0","Indice linéaire",1,2.5,.05,1.5),
            slider("n2","Coefficient Kerr n₂",1,100,1,3,"10⁻²⁰ m²·W⁻¹"),slider("intensity","Intensité de référence au sommet",.1,100,.1,10,"GW·cm⁻²"),
            slider("distance","Distance z/(n₀k₀ y₀²)",0,3,.1,1)],[
                preset("Soliton localisé",intensity=10,n2=3,distance=1),
                preset("Intensité quatre fois plus grande",intensity=40,n2=3,distance=1),
                preset("Comparer à la diffraction libre",intensity=10,n2=3,distance=3)]),
    lab("rayonnement","Dipôle : Rayleigh, résonance, Thomson","Ondes",
        "Intégrer un diagramme de puissance sin²θ. Un électron élastiquement lié mène à une diffusion en ω⁴ loin sous la résonance et à la limite Thomson au-dessus.",[
            select("model","Source",[("dipole","Moment dipolaire imposé"),("lie","Électron élastiquement lié")],"lie"),
            slider("frequency","Fréquence incidente",1,1000,1,100,"THz"),slider("resonance","Fréquence propre f₀",10,3000,10,1000,"THz"),
            slider("damping","Amortissement γ/ω₀",.001,.5,.001,.05),slider("dipole","Amplitude du dipôle imposé",.1,100,.1,1,"10⁻²⁹ C·m"),
            slider("field","Amplitude incidente E₀",1,1000,1,100,"V·m⁻¹")],[
                preset("Rayleigh : ω≪ω₀",model="lie",frequency=100,resonance=1000),
                preset("Résonance",model="lie",frequency=500,resonance=500,damping=.05),
                preset("Vers Thomson",model="lie",frequency=1000,resonance=10,damping=.05),
                preset("Dipôle imposé",model="dipole",frequency=100,dipole=1)]),
    lab("dynamo","Dynamo : croissance contre diffusion, sans seuil universel","Passerelles",
        "Un mode hélicoïdal d'un modèle α² local croît comme exp((sαk−ηm k²)t). Ce bilan représente une fermeture prescrite, pas une simulation du noyau terrestre ; Rm seul ne prouve pas une dynamo.",[
            slider("alpha","Coefficient α prescrit",-1,1,.01,.1,"mm·s⁻¹"),slider("diffusivity","Diffusivité magnétique ηm",.1,10,.1,1,"m²·s⁻¹"),
            slider("length","Longueur d'onde L",1,3500,1,1000,"km"),slider("velocity","Vitesse caractéristique U",.01,10,.01,.5,"mm·s⁻¹"),
            slider("years","Temps",0,100,1,10,"années"),slider("amplitude","Amplitude initiale B₀",.1,10,.1,3,"mT"),
            select("helicity","Hélicité du mode",[("plus","curl B = +k B"),("minus","curl B = −k B")],"plus")],[
                preset("Croissance du bon mode",alpha=.1,diffusivity=1,length=1000,helicity="plus"),
                preset("Diffusion sans induction",alpha=0,diffusivity=1,length=1000),
                preset("Mauvaise hélicité",alpha=.1,diffusivity=1,length=1000,helicity="minus"),
                preset("Grand Rm sans croissance",alpha=0,velocity=10,length=1000)])
]

LAB_BY_ID={item["id"]:item for item in LABS}
