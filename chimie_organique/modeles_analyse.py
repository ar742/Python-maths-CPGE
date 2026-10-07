"""Modèles bornés de caractérisation et stratégie organique.

Les courbes spectroscopiques sont des simulations pédagogiques documentées,
les bibliothèques de réactions des cas explicitement nommés. Aucun moteur de
recherche de structure ou de réactivité universel n'est implicite.
"""
from __future__ import annotations
import math
import numpy as np
from commun import (R, atom, bond, molecule, chain, benzene, electron_arrow,
                    metric, series, chart, scene, bars_scene, reaction_scene,
                    mechanism_scene, energy_profile)


def result(metrics, charts, visual, steps, assumptions, **data):
    return dict(metrics=metrics, charts=charts, scene=visual, steps=steps,
                assumptions=assumptions, **data)


def formula_text(counts):
    return ''.join(k + (str(n) if n > 1 else '') for k,n in counts.items() if n)


ISOTOPES = {
 'Cl': [(34.968852682,.7576),(36.965902602,.2424)],
 'Br': [(78.9183376,.5069),(80.9162897,.4931)]
}
LIGHT_MASS = {'C':12.,'H':1.00782503223,'N':14.00307400443,'O':15.99491461957,
              'Cl':34.968852682,'Br':78.9183376}
AVERAGE_MASS = {'C':12.011,'H':1.008,'N':14.007,'O':15.999,'Cl':35.45,'Br':79.904}


def isotope_envelope(counts):
    """Toutes combinaisons Cl/Br : masses exactes et probabilités conditionnelles.

    C, H, N et O sont ici fixés à leur isotope léger : leur satellite M+1 ne
    fait pas partie de ce modèle de signatures halogénées.
    """
    base=sum(LIGHT_MASS[k]*counts[k] for k in LIGHT_MASS)
    peaks=[(base,1.,0)]
    for element in ('Cl','Br'):
        lo,hi=ISOTOPES[element]; delta=hi[0]-lo[0]
        for _ in range(counts[element]):
            peaks=[(mass+d,prob*q,index+j) for mass,prob,index in peaks
                   for d,q,j in ((0.,lo[1],0),(delta,hi[1],1))]
    grouped={}
    for mass,prob,index in peaks:
        grouped.setdefault(index,[0.,0.])
        grouped[index][0]+=prob; grouped[index][1]+=mass*prob
    return [dict(position=s/p,intensity=p,offset=2*k,label='M' if k==0 else f'M+{2*k}')
            for k,(p,s) in sorted(grouped.items())]


def formule(p):
    counts={k:int(p[k]) for k in LIGHT_MASS}
    ihd=(2*counts['C']+2+counts['N']-counts['H']-counts['Cl']-counts['Br'])/2
    admissible=ihd>=0 and abs(ihd-round(ihd))<1e-12
    peaks=isotope_envelope(counts)
    xs=[];ys=[]
    for peak in peaks:
        xs.extend([peak['position']-.025,peak['position'],peak['position']+.025]);ys.extend([0,100*peak['intensity'],0])
    combinations=[]
    if admissible:
        combinations=[f'{cycles} cycle(s), {double} double(s), {triple} triple(s)'
                      for triple in range(int(ihd)//2+1)
                      for double in range(int(ihd)-2*triple+1)
                      for cycles in [int(ihd)-2*triple-double]][:10]
    visual=scene('spectrum','Empreinte isotopique Cl/Br',
        'Probabilités conditionnelles aux isotopes légers de C, H, N, O ; M+1 (¹³C) et fragmentation non simulés.',
        x=xs,y=ys,x_label='Masse isotopique du neutre / u',y_label='Probabilité / %',peaks=peaks)
    return result([metric('Formule',formula_text(counts)),metric('IHD = (2C+2+N−H−X)/2',ihd),
        metric('Masse monoisotopique neutre',peaks[0]['position'],'u'),metric('Masse molaire moyenne approchée',sum(AVERAGE_MASS[k]*counts[k] for k in counts),'g/mol'),
        metric('Compatibilité CHNOX fermé', 'Admissible, non suffisante' if admissible else 'Incompatible dans ce modèle'),metric('Somme des probabilités',sum(q['intensity'] for q in peaks))],
        [chart('Signature halogénée','Masse / u','Probabilité / %',series('Cl/Br : isotopes naturels',xs,ys))],visual,
        ['Compter X = Cl + Br comme des hydrogènes pour l’IHD ; O n’intervient pas.',
         'Un cycle ou une double liaison vaut un degré, une triple en vaut deux.',
         'Croiser ensuite IR, RMN et connectivité : les premières combinaisons possibles sont ' + (' ; '.join(combinations) if combinations else 'absentes pour cette formule.')],
        ['Entités neutres usuelles à valences C4, H1, N3, O2, X1 et couche fermée : un IHD entier positif est nécessaire, pas suffisant.',
         'Les masses indiquent le neutre ; un ion [M+H]⁺ ou M⁺· requiert son propre bilan de masse et de charge.',
         'Abondances Cl/Br tabulées NIST ; elles peuvent varier naturellement. Les pics proches Cl/Br de même classe M+2k sont regroupés à leur barycentre.'],
        counts=counts,ihd=ihd,admissible=admissible,isotopes=peaks)


def stereo(p):
    # Rank 4 points away; 1 -> 2 -> 3 is clockwise in the reference view.
    vectors=np.array([[0,1,1/3],[math.sqrt(3)/2,-.5,1/3],[-math.sqrt(3)/2,-.5,1/3],[0,0,-1]],float)
    theta=math.radians(p['angle']); c,s=math.cos(theta),math.sin(theta)
    rotation=np.array([[c,0,s],[0,1,0],[-s,0,c]])
    vectors=vectors@rotation.T
    if p['mirror']=='mirror': vectors[:,0]*=-1
    determinant=float(np.linalg.det(np.stack([vectors[i]-vectors[3] for i in range(3)])))
    configuration='R' if determinant<0 else 'S'
    signed_ee=2*p['fraction']-1
    observed=p['alpha']*p['length']*p['concentration']*signed_ee
    labels=['OH','COOH','CH₃','H']
    fraction=np.linspace(0,1,101)
    return result([metric('Configuration du tétraèdre',configuration),metric('Déterminant orienté',determinant),
        metric('Excès énantiomérique',100*abs(signed_ee),'%'),metric('R dans le mélange',100*p['fraction'],'%'),metric('Rotation observée',observed,'°'),metric('CIP fourni','OH > COOH > CH₃ > H')],
        [chart('Composition et pouvoir rotatoire','Fraction molaire R','Rotation / °',series('α = [α]R ℓ c (xR−xS)',fraction,p['alpha']*p['length']*p['concentration']*(2*fraction-1)))],
        scene('stereo','Acide lactique : configuration et miroir',
          'Axes de vue fixes ; la rotation du solide conserve la configuration. Les quatre rangs sont donnés, pas calculés par un moteur CIP.',
          vectors=[dict(rank=i+1,label=labels[i],xyz=v.tolist()) for i,v in enumerate(vectors)],configuration=configuration,ee=100*abs(signed_ee),rotation=observed),
        ['Au premier niveau, O > C > H. Pour départager les deux C, COOH présente [O,O,O] et CH₃ [H,H,H], avec duplications CIP de C=O.',
         'R/S est invariant par rotation propre ; le miroir change le signe du déterminant et échange R et S.',
         'ee = |xR−xS| ; le signe de [α]R est une donnée expérimentale indépendante du descripteur R.'],
        ['Un seul centre stéréogène, classement CIP fixé. Aucun traitement général d’isotopes, de centres multiples ou de pseudoasymétrie.',
         'Additivité idéale des rotations des deux énantiomères ; même solvant, température et longueur d’onde, sans autre espèce active.',
         'Les coordonnées constituent un tétraèdre orienté ; la rotation de l’affichage ne fait pas varier xR.'],
        vectors=vectors,determinant=determinant,configuration=configuration,ee=abs(signed_ee),observed_rotation=observed)


def butane_energy(angle):
    """Interpolation cosinus périodique entre les conformations de référence."""
    theta=np.asarray(angle)%360
    levels=np.array([21.,3.8,16.,0.,16.,3.8,21.])
    interval=np.floor(theta/60).astype(int)
    t=(theta-60*interval)/60
    return levels[interval]+(levels[interval+1]-levels[interval])*(1-np.cos(np.pi*t))/2


def methylcyclohexane_chair(axial):
    """Projection de deux chaises, même substituant up avant/après inversion.

    Un hexagone xy régulier à z alterné ±1/(4√2) donne des angles de liaison
    tétraédriques exacts. La projection est orthographique oblique, sans
    perspective : les longueurs dans l'image ne sont pas des distances 3D.
    """
    h=1/(4*math.sqrt(2));sign=1 if axial else -1
    xyz=np.array([[math.cos(i*math.pi/3),math.sin(i*math.pi/3),sign*h*(-1)**i] for i in range(6)])
    def project(v):return v[0]+.2*v[1], .2*v[1]+.8*v[2]
    atoms=[atom(i,'C',*project(v),xyz=v.tolist()) for i,v in enumerate(xyz)]
    for a in atoms:a['label']=''
    # C0 up axial in one chair, up equatorial in the inverted chair.
    direction=np.array([0,0,math.sqrt(9/8)]) if axial else np.array([1,0,1/math.sqrt(8)])
    substituent=xyz[0]+direction
    atoms.append(atom('m','C',*project(substituent),'CH₃',xyz=substituent.tolist()))
    return molecule('CH₃ axial up' if axial else 'CH₃ équatorial up',atoms,
                    [bond(i,(i+1)%6) for i in range(6)]+[bond(0,'m')])


def conformeres(p):
    T=p['temperature'];theta=np.linspace(0,360,721)
    if p['system']=='butane':
        weights=np.array([1.,2*math.exp(-3800/(R*T))]); populations=weights/weights.sum()
        energies=butane_energy(theta);current=float(butane_energy(p['angle']))
        label=['Anti : un minimum','Gauche : deux minima']
        phi=p['angle']%360
        population=float(populations[0]) if abs(phi-180)<1e-8 else float(populations[1]/2) if min(abs(phi-60),abs(phi-300))<1e-8 else None
        description='Interpolation cosinus entre Eanti=0, Egauche(60°)=3,8, Eeclipsé(120°)=16 et Esyn(0°)=21 kJ/mol : profil pédagogique, pas un champ de force moléculaire.'
        metrics=[metric('Énergie au dièdre choisi',current,'kJ/mol'),metric('Population anti',100*populations[0],'%'),metric('Population des deux gauche',100*populations[1],'%'),metric('Un seul gauche',50*populations[1],'%'),metric('Dégénérescences anti/gauche','1 / 2')]
        visual=scene('newman','Projection de Newman du butane',description,angle=p['angle'],front=['CH₃','H','H'],back=['CH₃','H','H'],population=population,variant='butane')
        if population is None:
            del visual['population']
            visual['caption']='Ce dièdre n’est pas l’un des trois minima du modèle discret de populations.'
        charts=[chart('Barrière de rotation (profil pédagogique)','Dièdre / °','E / kJ·mol⁻¹',series('Butane',theta,energies))]
        levels=[0.,3.8]
    else:
        weights=np.array([1.,math.exp(-p['delta']*1000/(R*T))]);populations=weights/weights.sum();label=['Chaise équatoriale','Chaise axiale'];levels=[0.,p['delta']]
        metrics=[metric('Population équatoriale',100*populations[0],'%'),metric('Population axiale',100*populations[1],'%'),metric('ΔG axial−équatorial',p['delta'],'kJ/mol'),metric('Dégénérescences','1 / 1')]
        visual=scene('newman','Méthylcyclohexane : deux chaises',
          'Inversion de chaise : axial ⇄ équatorial, tandis que up/down et la configuration ne s’inversent pas.',angle=p['angle'],front=['CH₃','H','H'],back=['CH₃','H','H'],population=float(populations[0]),variant='cyclohexane',populations=populations.tolist())
        visual['molecules']=[methylcyclohexane_chair(False),methylcyclohexane_chair(True)]
        x,e=energy_profile([0,p['delta']],[45])
        charts=[chart('Inversion de chaise : barrière illustrative','Coordonnée de réaction','G / kJ·mol⁻¹',series('Deux chaises',x,e))]
    temperatures=np.linspace(200,500,151);deg=np.array([1,2] if p['system']=='butane' else [1,1])
    w=deg[:,None]*np.exp(-np.asarray(levels)[:,None]*1000/(R*temperatures));w/=w.sum(axis=0)
    charts.append(chart('Populations d’équilibre','T / K','Population / %',*(series(l,temperatures,100*w[i]) for i,l in enumerate(label))))
    return result(metrics,charts,visual,
       ['Une conformation change par rotation autour d’une liaison simple ou inversion de chaise ; une configuration ne change pas ainsi.',
        'Compter les états : Pi = gi exp(−Gi/RT)/Σj gj exp(−Gj/RT). La hauteur de la barrière influence la vitesse, pas ce rapport d’équilibre.',
        'Le butane anti est un minimum, les deux gauche sont deux états distincts équivalents ; une Newman éclipsée n’est pas un conformère peuplé stable.'],
       ['Population discrète des minima : approximation harmonicités/entropies semblables. Ce n’est pas l’intégrale statistique continue du profil interpolé.',
        'Niveaux de référence pédagogiques typiques ; les différences de G dépendent du milieu. Le méthylcyclohexane a deux chaises non équivalentes.',
        'Pour E2, le dièdre pertinent est Hβ–Cβ–Cα–groupe partant, pas nécessairement CH₃–C–C–CH₃.'],populations=populations,levels=levels)


def structure(name):
    structures={
      'ethanol':chain('Éthanol',['CH₃','CH₂','OH']),
      'ethanoate':molecule('Éthanoate d’éthyle',[atom('a','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O'),atom('e','O',2,0,'O'),atom('m','C',3,0,'CH₂'),atom('t','C',4,0,'CH₃')],[bond('a','c'),bond('c','o',2),bond('c','e'),bond('e','m'),bond('m','t')]),
      'acetone':molecule('Propanone',[atom('a','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O'),atom('b','C',2,0,'CH₃')],[bond('a','c'),bond('c','o',2),bond('c','b')]),
      'acide':molecule('Acide éthanoïque',[atom('a','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O'),atom('h','O',2,0,'OH')],[bond('a','c'),bond('c','o',2),bond('c','h')]),
      'anisole':benzene('Méthoxybenzène (anisole)',{0:'OCH₃'}),
      'benzaldehyde':benzene('Benzaldéhyde',{0:'CHO'}),
      'acetophenone':benzene('Acétophénone',{0:'COCH₃'})}
    return structures[name]


# position cm-1, maximum absorbance at factors c=l=1, sigma cm-1, assignment
IR_BANDS={
 'ethanol':[(3350,.55,150,'O–H lié, large'),(2970,.25,30,'C–H sp³'),(2890,.18,30,'C–H sp³'),(1050,.6,28,'C–O')],
 'ethanoate':[(2980,.25,30,'C–H sp³'),(1740,.9,22,'C=O ester'),(1240,.65,25,'C–O ester'),(1050,.45,25,'C–O')],
 'acetone':[(2970,.3,30,'C–H sp³'),(1715,.95,20,'C=O cétone'),(1360,.3,25,'Déformation CH₃')],
 'acide':[(3000,.6,330,'O–H acide, très large'),(1710,.9,24,'C=O acide'),(1280,.45,30,'C–O')],
 'anisole':[(3060,.18,22,'C–H aromatique'),(1600,.3,20,'C=C aromatique'),(1500,.35,20,'C=C aromatique'),(1250,.6,25,'Ar–O'),(1030,.4,25,'C–O')],
 'benzaldehyde':[(3060,.15,25,'C–H aromatique'),(2820,.22,16,'C–H aldéhyde : bande'),(2720,.25,16,'C–H aldéhyde : doublet de Fermi'),(1700,.8,22,'C=O conjugué'),(1600,.3,22,'Cycle aromatique')],
 'acetophenone':[(3060,.18,25,'C–H aromatique'),(2960,.25,28,'C–H sp³'),(1685,.85,22,'C=O cétone conjuguée'),(1600,.35,20,'Cycle aromatique'),(1500,.25,20,'Cycle aromatique')]
}


def ir(p):
    x=np.linspace(500,4000,1751);bands=IR_BANDS[p['molecule']]
    A=sum(height*np.exp(-.5*((x-center)/(sigma*p['width']))**2) for center,height,sigma,label in bands)*p['concentration']*p['path']
    transmission=100*10**(-A)
    peaks=[dict(position=center,label=f'{label} · {center} cm⁻¹',sigma=sigma*p['width'],absorbance=height*p['concentration']*p['path']) for center,height,sigma,label in bands]
    return result([metric('Molécule',structure(p['molecule'])['name']),metric('Bandes documentées',len(bands)),metric('Absorbance maximale',float(np.max(A))),metric('Transmission minimale',float(np.min(transmission)),'%'),metric('Nature des données','Simulation pédagogique')],
       [chart('IR : bandes de fonctions','Nombre d’onde / cm⁻¹','Transmission / %',series('T = 100 × 10⁻ᴬ',x,transmission),x_reverse=True),
        chart('Beer–Lambert : addition des absorbances','Nombre d’onde / cm⁻¹','Absorbance',series('A = ε ℓ c (échelle relative)',x,A),x_reverse=True)],
       scene('spectrum','Spectre IR simulé',
          'Les positions, amplitudes et largeurs sont des paramètres pédagogiques typiques, pas un enregistrement expérimental.',
          x=x,y=transmission,x_label='Nombre d’onde / cm⁻¹',y_label='Transmission / %',peaks=peaks,molecule=structure(p['molecule']),reverse_x=True),
       [f"{label} : centre {center} cm⁻¹, σ initial {sigma} cm⁻¹, A au centre de la bande isolée {height:.2f}." for center,height,sigma,label in bands]+[
          'Les absorbances des contributions s’additionnent, les transmissions se multiplient. Doubler c ou ℓ double A, sans doubler la diminution de T.',
          'Associer l’absence/présence de plusieurs bandes à la formule brute et à la RMN ; la zone d’empreinte n’est pas une identification certaine ici.'],
       ['Bandes gaussiennes superposées, milieu et température fixes, diffusion et saturation instrumentale ignorées.',
        'Concentration et trajet sont des facteurs relatifs : aucune valeur d’ε molaire expérimentale n’est prétendue.',
        'Liaison hydrogène, conjugaison et environnement déplacent les bandes réelles.'],wavenumber=x,absorbance=A,transmittance=transmission,bands=peaks)


# delta ppm, number of protons, multiplicity n+1, J Hz, label, partnered group.
H_SIGNALS={
 'ethanol':[(1.20,3,3,7.,'CH₃','CH₂'),(3.65,2,4,7.,'CH₂','CH₃'),(2.,1,1,0.,'OH échangeable',None)],
 'ethanoate':[(1.25,3,3,7.2,'CH₃ éthyle','OCH₂'),(2.05,3,1,0.,'CH₃–C=O',None),(4.12,2,4,7.2,'OCH₂','CH₃ éthyle')],
 'acetone':[(2.17,6,1,0.,'Deux CH₃ équivalents',None)],
 'acide':[(2.10,3,1,0.,'CH₃',None),(11.2,1,1,0.,'OH acide échangeable',None)],
 'anisole':[(3.80,3,1,0.,'OCH₃',None),(6.90,3,1,0.,'Paquet aromatique non résolu (3H)',None),(7.25,2,1,0.,'Paquet aromatique non résolu (2H)',None)],
 'benzaldehyde':[(7.50,3,1,0.,'Paquet aromatique non résolu (3H)',None),(7.85,2,1,0.,'Paquet aromatique non résolu (2H)',None),(9.98,1,1,0.,'CHO : petits couplages ignorés',None)],
 'acetophenone':[(2.60,3,1,0.,'CH₃–C=O',None),(7.45,3,1,0.,'Paquet aromatique non résolu (3H)',None),(7.95,2,1,0.,'Paquet aromatique non résolu (2H)',None)]
}
C_SIGNALS={
 'ethanol':[(18.3,1),(58.1,1)],'ethanoate':[(14.2,1),(20.8,1),(60.4,1),(170.7,1)],
 'acetone':[(30.7,2),(206.,1)],'acide':[(20.8,1),(178.,1)],
 'anisole':[(55.3,1),(114.1,2),(120.7,1),(129.5,2),(159.6,1)],
 'benzaldehyde':[(128.7,2),(129.7,2),(134.5,1),(136.5,1),(191.8,1)],
 'acetophenone':[(26.6,1),(128.3,2),(128.6,2),(133.,1),(137.,1),(198.,1)]
}


def rmn(p):
    proton=p['nucleus']=='H';frequency=p['frequency'];width=p['linewidth']/frequency
    if proton:
        source=H_SIGNALS[p['molecule']]
        upper=max(13.,max(q[0] for q in source)*p['shift_scale']+1)
        grids=[np.linspace(-.5,upper,1001)]
        # Resolve narrow lines locally rather than oversampling an empty 13 ppm window.
        for delta,_,multiplicity,J,label,_ in source:
            positions=delta*p['shift_scale']+(np.arange(multiplicity)-(multiplicity-1)/2)*J/frequency
            gamma=width/2*(12 if 'Paquet' in label else 1)
            grids.extend(pos+np.linspace(-20,20,161)*gamma for pos in positions)
        x=np.unique(np.concatenate(grids));x=x[(x>=-.5)&(x<=upper)]
    else:
        x=np.linspace(-10,220,4801)
    y=np.zeros_like(x);signals=[];peaks=[];ratios=[]
    if proton:
        source=H_SIGNALS[p['molecule']];partner={label:delta for delta,_,_,_,label,_ in source}
        for delta,integral,multiplicity,J,label,paired in source:
            center=delta*p['shift_scale'];coeff=np.array([math.comb(multiplicity-1,i) for i in range(multiplicity)],float);coeff/=coeff.sum()
            positions=center+(np.arange(multiplicity)-(multiplicity-1)/2)*J/frequency
            gamma=width/2*(12 if 'Paquet' in label else 1)
            profile=sum(q*gamma/np.pi/((x-pos)**2+gamma**2) for pos,q in zip(positions,coeff))
            trapezoid=getattr(np,'trapezoid',np.trapz)
            profile*=integral/trapezoid(profile,x);y+=profile
            signals.append(dict(delta=center,integral=integral,multiplicity=multiplicity,J=J,label=label,positions=positions,weights=coeff,area=float(trapezoid(profile,x))))
            peaks.extend(dict(position=float(pos),label=label,intensity=float(q)) for pos,q in zip(positions,coeff))
            if paired and J:
                ratios.append(abs(delta-partner[paired])*p['shift_scale']*frequency/J)
    else:
        for delta,deg in C_SIGNALS[p['molecule']]:
            # C intensities deliberately not proportional to number of carbons.
            gamma=.22;y+=gamma/np.pi/((x-delta)**2+gamma**2)
            signals.append(dict(delta=delta,integral=None,degeneracy=deg,multiplicity=1,J=0.,label=f'{deg} C équivalent(s)'))
            peaks.append(dict(position=delta,label=f'{deg} C équivalent(s)'))
    dx=np.diff(x);cumulative=np.r_[0,np.cumsum((y[:-1]+y[1:])*dx/2)]
    ratio=min(ratios) if ratios else None
    integral_sum=sum(q['integral'] for q in signals) if proton else sum(q['degeneracy'] for q in signals)
    metrics=[metric('Molécule',structure(p['molecule'])['name']),metric('Environnements représentés',len(signals)),metric('Total intégré ¹H' if proton else 'Carbones comptés avec dégénérescences',integral_sum),metric('Fréquence ¹H',frequency,'MHz'),metric('Δν/J minimal couplé','Aucun groupe couplé explicite' if ratio is None else ratio),metric('Domaine premier ordre','Non quantitatif pour aromatiques non résolus' if p['molecule'] in ('anisole','benzaldehyde','acetophenone') else ('Pas de couplage traité' if ratio is None else 'Satisfaisant dans ce modèle' if ratio>=10 else 'Approximation fragile : effets de second ordre'))]
    charts=[chart('RMN simulée : δ reste en ppm','δ / ppm','Amplitude arbitraire',series('¹H' if proton else '¹³C découplé',x,y),x_reverse=True)]
    if proton: charts.append(chart('L’aire ne se confond pas avec la hauteur','δ / ppm','Intégrale / H',series('Intégrale cumulée depuis les grands δ',x,cumulative[-1]-cumulative),x_reverse=True))
    descriptions=[]
    for q in signals:
        if proton:
            multi='paquet m approximatif' if 'Paquet' in q['label'] else {1:'s',2:'d',3:'t',4:'q'}.get(q['multiplicity'],str(q['multiplicity']))
            descriptions.append(f"{q['label']} : δ = {q['delta']:.2f} ppm, {q['integral']} H, {multi}"+(f", J = {q['J']:.1f} Hz." if q['J'] else '.'))
        else: descriptions.append(f"δ = {q['delta']:.1f} ppm : {q['degeneracy']} C équivalent(s), raie découplée.")
    return result(metrics,charts,scene('spectrum','Spectre RMN pédagogique',
        'Positions typiques, raies lorentziennes ; les paquets aromatiques représentent des zones, sans prétendre résoudre leur système de spins.',
        x=x,y=y,x_label='δ / ppm',y_label='Amplitude arbitraire',peaks=peaks,molecule=structure(p['molecule']),integral=cumulative if proton else None,reverse_x=True),
        descriptions+['Entre raies d’un multiplet de premier ordre, Δδ = J/ν₀. J en Hz ne change pas avec le champ ; la séparation en ppm diminue.',
         '¹H : les aires sont normalisées au nombre de H des groupes. ¹³C découplé : les hauteurs ne sont pas une intégration quantitative des C.',
         'OH rapidement échangeable : position variable et couplages non retenus ; les approximations aromatiques ne sont pas des singulets réels.'],
        ['Le premier ordre suppose des spins couplés avec Δν/J assez grand ; Δν/J ≥ 10 est un repère, pas une garantie générale.',
         'La règle n+1 ne s’applique ici qu’à des voisins équivalents spin 1/2 avec même J. Pas de couplages à longue portée ni de second ordre simulé.',
         'Le contrôle de rapprochement des δ est un test pédagogique du domaine ; il ne prétend pas reproduire un changement particulier de solvant.',
        'En ¹³C découplé les positions restent fixes ; les contrôles de fréquence ¹H, de largeur en Hz et d’écart de δ ne sont pas appliqués au tracé ¹³C.'],signals=signals,ppm=x,intensity=y,integral=cumulative,ratio=ratio,total_integral=integral_sum)


def ccm(p):
    f=p['eluent'];conv=p['conversion'];front=p['front']
    # Explicit competition model: k' decreases exponentially with polar fraction.
    def retention(eluent,constant): return 1/(1+constant*np.exp(-4*eluent))
    constants={'Réactif R (plus retenu)':12.,'Produit P':4.,'Impureté I':7.}
    rf={label:float(retention(f,k)) for label,k in constants.items()}
    spots=[dict(label='R',rf=rf['Réactif R (plus retenu)'],lane=0,intensity=1),dict(label='P',rf=rf['Produit P'],lane=1,intensity=1)]
    if conv<1: spots.append(dict(label='R',rf=rf['Réactif R (plus retenu)'],lane=2,intensity=1-conv))
    if conv>0: spots.append(dict(label='P',rf=rf['Produit P'],lane=2,intensity=conv))
    spots.append(dict(label='I',rf=rf['Impureté I'],lane=2,intensity=.15))
    distance=abs(rf['Produit P']-rf['Réactif R (plus retenu)'])*front
    resolution=distance/(2*p['width'])
    grid=np.linspace(0,1,151)
    return result([metric('Rf réactif',rf['Réactif R (plus retenu)']),metric('Rf produit',rf['Produit P']),metric('Distance R/P',distance,'cm'),metric('Séparation / diamètre de tache',resolution),metric('Conversion représentée',100*conv,'%'),metric('Identité démontrée par seul Rf','Non')],
        [chart('Force éluante et rétention sur silice','Fraction polaire de l’éluant','Rf',*(series(label,grid,retention(grid,k)) for label,k in constants.items()))],
        scene('chromatography','Plaque de CCM : témoins et mélange',
          'Modèle k′ = k′₀ exp(−4φ), Rf = 1/(1+k′). Les intensités indiquent des quantités relatives avec même réponse détecteur, hypothèse pédagogique.',
          spots=spots,front=front,eluent=f,baseline=0,lanes=['Témoin R','Témoin P','Mélange'],spot_width=p['width']),
        ['Tracer le dépôt et le front : Rf = distance tache/distance front, mesurées depuis la même ligne de dépôt.',
         'Une tache au niveau du témoin est compatible avec son identité, pas une preuve ; plusieurs molécules peuvent coéluer.',
         'L’impureté reste visible même à conversion totale : conversion, pureté et rendement isolé sont trois grandeurs distinctes.'],
        ['Silice en phase normale : rétention paramétrée, pas calculée ab initio depuis une structure.',
         'Pas de surcharge, traînée ni gradient d’élution ; φ est une fraction de solvant polaire et les constantes sont pédagogiques.',
         'Quantités et intensités de révélation ne sont proportionnelles que sous l’hypothèse d’une réponse identique.'],rf=rf,spots=spots,resolution=resolution)


def neutral_fraction(solute,pH):
    if solute=='acid': return 1/(1+10**(pH-4.2))
    if solute=='base': return 1/(1+10**(4.6-pH))
    return 1.


def extraction(p):
    va=p['aqueous_volume'];vo=p['organic_volume'];n=int(p['stages']);alpha=neutral_fraction(p['solute'],p['pH']);D=p['partition']*alpha
    q=va/(va+D*vo/n);remaining=q**n;extracted=1-remaining
    stages=[dict(stage=i,aqueous=q**i,organic_collected=1-q**i,organic_this_stage=(q**(i-1)-q**i) if i else 0.) for i in range(n+1)]
    ph=np.linspace(1,12,221);Ds=np.array([p['partition']*neutral_fraction(p['solute'],x) for x in ph]);eff=1-(va/(va+Ds*vo/n))**n
    counts=np.arange(1,9);recovery=1-(va/(va+D*vo/counts))**counts
    return result([metric('Fraction neutre aqueuse',100*alpha,'%'),metric('D = [total]org/[total]aq',D),metric('Soluté extrait',100*extracted,'%'),metric('Soluté restant dans l’eau',100*remaining,'%'),metric('Chaque portion organique',vo/n,'mL'),metric('Bilan matière',remaining+extracted,'mol pour n₀ = 1 mol')],
        [chart('pH et efficacité d’extraction','pH imposé','Extrait / %',series(f'{n} extraction(s)',ph,100*eff)),chart('Fractionner un volume organique total fixé','Nombre d’extractions','Extrait / %',series('Même volume organique total',counts,100*recovery))],
        scene('extraction','Partage et collecte des phases',
          'À chaque étape, on conserve le soluté aqueux et collecte une nouvelle phase organique. Les quantités ci-dessous sont rapportées à n₀ = 1 mol.',
          aqueous=remaining,organic=extracted,n_initial=1.,unit='mol',vol_aqueous=va,vol_organic=vo/n,organic_on_top=p['position']=='top',stages=stages,labels={'aqueous':'Phase aqueuse conservée','organic':'Phases organiques réunies'}),
        ['Seule la forme neutre est supposée soluble dans le solvant organique : K partage le neutre, D partage la quantité totale.',
         ('Acide HA : αneutre = 1/(1+10^(pH−pKₐ)).' if p['solute']=='acid' else 'Base B : αneutre = 1/(1+10^(pKₐ(BH⁺)−pH)).' if p['solute']=='base' else 'Composé neutre : D = K, indépendant du pH dans ce modèle.'),
         f'Pour chaque portion {vo/n:.2f} mL : q = Va/(Va+DVo/n) = {q:.5f}. Après {n} étapes, naq/n₀ = qⁿ.'],
        ['pH imposé par une phase aqueuse tamponnée de capacité suffisante : consommation du tampon et pH auto-cohérent non calculés.',
         'Équilibre à chaque étape, volumes additifs constants, pas d’émulsion, ni paire d’ions organosoluble, ni dimérisation de l’acide.',
         'La phase organique peut être en haut ou en bas selon le solvant ; sa position est une donnée, jamais une propriété universelle.'],neutral=alpha,distribution=D,remaining=remaining,extracted=extracted,stages=stages)


def equilibrium_extent(a,b,c,d,K):
    """A+B ⇌ C+D, activities proportional to amounts in one common volume."""
    lo=-min(c,d);hi=min(a,b)
    for _ in range(100):
        x=(lo+hi)/2;residual=(c+x)*(d+x)-K*(a-x)*(b-x)
        if residual>0: hi=x
        else: lo=x
    return (lo+hi)/2


def esterification(p):
    a,b=p['first'],p['second'];initial_product=p['water'];mode=p['mode']
    if mode=='ester':
        labels=['Acide','Alcool','Ester','Eau'];K=p['K'];c,d=0.,initial_product
        reactants=[chain('Acide éthanoïque',['CH₃','COOH']),chain('Éthanol',['CH₃','CH₂','OH'])]
        products=[structure('ethanoate'),chain('Eau',['H','O','H'])]
    elif mode=='hydrolysis':
        labels=['Ester','Eau','Acide','Alcool'];K=1/p['K'];c,d=initial_product,0.
        reactants=[structure('ethanoate'),chain('Eau',['H','O','H'])]
        products=[chain('Acide éthanoïque',['CH₃','COOH']),structure('ethanol')]
    else:
        labels=['Ester','HO⁻','Carboxylate','Alcool'];K=None;c=d=0.
        reactants=[structure('ethanoate'),molecule('Hydroxyde',[atom('o','O',0,0,'OH',-1)],[])]
        products=[chain('Éthanoate',['CH₃','COO⁻']),structure('ethanol')]
    xe=equilibrium_extent(a,b,c,d,K) if K is not None else min(a,b)
    xi=p['progress']*xe;amounts=np.array([a-xi,b-xi,c+xi,d+xi])
    x=np.linspace(0,xe,151);rows=[a-x,b-x,c+x,d+x]
    residual=None if K is None else (c+xe)*(d+xe)-K*(a-xe)*(b-xe)
    return result([metric('Avancement observé',xi,'mol'),metric('Avancement à l’équilibre / limite',xe,'mol'),metric('Conversion du premier réactif',100*xi/a,'%'),metric('K de la transformation','Piégeage carboxylate, modèle total' if K is None else K),metric('Catalyse acide','Accélère, ne change pas K' if K is not None else 'HO⁻ consommé : pas un catalyseur'),metric('Matière non négative',bool(np.all(amounts>=-1e-12)))],
        [chart('Tableau d’avancement : conservation 1:1','ξ / mol','n / mol',*(series(label,x,row) for label,row in zip(labels,rows)))],
        reaction_scene('Estérification, hydrolyse ou saponification',
          'Même squelette acyle ; en milieu basique le produit est le carboxylate, qui doit être acidifié si l’on veut isoler l’acide.',reactants+products,[dict(a=0,b=2,label='⇌, H⁺ catalytique' if K is not None else 'HO⁻ consommé')]),
        ['Construire n = n₀ + νξ avant tout calcul ; chaque ξ consomme un acyle et forme une liaison acyle–O ou la rompt.',
         'Équilibre idéal homogène : K = nC nD/(nA nB), le volume commun s’élimine ; chercher ξ dans le domaine des quantités positives.' if K is not None else 'Après addition–élimination, l’acide est déprotoné par la base ; le carboxylate limite la réaction inverse dans les conditions du modèle.',
         'Le curseur d’avancement parcourt un tableau de matière ; il n’est pas une durée et ne constitue pas une loi cinétique.'],
        ['Estérification et hydrolyse acide : mélange homogène idéal, volume fixe, eau explicitement comptée et aucun retrait en continu.',
         'Khydrolyse = 1/Kestérification avec les mêmes conventions d’activité ; utiliser eau pure de solvant impose une autre écriture.',
         'Saponification : conversion totale du réactif limitant approximée, sans vitesse simulée, pas d’équilibration acide ultérieure ; les contrôles K et produit initial ne sont pas appliqués à ce bilan basique.'],extent=xi,equilibrium_extent=xe,amounts=amounts,initial=[a,b,c,d],labels=labels,K=K,equilibrium_residual=residual)


def acyl_graph(name,lg='Cl',tetrahedral=False,amine=False,protonated=False,arrows=None):
    atoms=[atom('m','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1.1,'O',-1 if tetrahedral else 0,lone_pairs=3 if tetrahedral else 2)]
    bonds=[bond('m','c'),bond('c','o',1 if tetrahedral else 2)]
    if lg:
        atoms.append(atom('lg','Cl' if lg=='Cl' else 'O',2,0,lg));bonds.append(bond('c','lg'))
    if amine:
        atoms.append(atom('n','N',1,-1.1,'NH₂CH₃' if tetrahedral or protonated else 'NHCH₃',1 if tetrahedral or protonated else 0,lone_pairs=0 if tetrahedral or protonated else 1));bonds.append(bond('c','n'))
    return molecule(name,atoms,bonds,arrows or [])


def acylation(p):
    activation=p['activation'];a=p['amine'];base=p['base']
    if activation=='acid':
        amount=0.;salt=min(1,a);frames=[reaction_scene('Acide + amine non activés','Acide/base prédomine ; les protonations entre plusieurs bases ne sont pas calculées.',[structure('acide'),chain('Méthylamine',['CH₃','NH₂']),chain('Sel',['CH₃','COO⁻']),chain('Méthylammonium',['CH₃','NH₃⁺'])])]
        visual=frames[0];acid_trapped=None if base else salt;freeamine=None if base else max(0,a-salt);freebase=None if base else 0.;lg='OH'
    else:
        # One primary amine forms each amide; a second amine or external base traps one acid.
        amount=min(1.,a,(a+base)/2);acid_trapped=amount
        consumed_base=min(base,amount);consumed_amine=amount+(amount-consumed_base)
        freeamine=a-consumed_amine;freebase=base-consumed_base
        lg='Cl' if activation=='chloride' else 'OCOCH₃'
        start=acyl_graph('Dérivé activé + attaque N',lg,arrows=[electron_arrow([2,-1.1],[1,0],[1.55,-.9]),electron_arrow([1,.5],[1,1.1],[1.35,.85])])
        start['atoms'].append(atom('n','N',2,-1.1,'NH₂CH₃',lone_pairs=1))
        tetra=acyl_graph('Intermédiaire tétraédrique',lg,True,True,arrows=[electron_arrow([.9,1.3],[1,.5],[.6,.8]),electron_arrow([1.5,0],[2,0],[1.75,.45])])
        collapsed=acyl_graph('Amide protoné',None,False,True,True)
        collapsed['atoms'].append(atom('counter','Cl' if activation=='chloride' else 'O',3,0,'Cl' if activation=='chloride' else 'CH₃COO',-1))
        final=acyl_graph('N-Méthyléthanamide',None,False,True,False)
        final['atoms']+= [atom('salt','N',3,-.4,'BH',1),atom('counter','Cl' if activation=='chloride' else 'O',4,-.4,'Cl' if activation=='chloride' else 'CH₃COO',-1)]
        visual=mechanism_scene('Substitution nucléophile acyle',
           'Les flèches déplacent un doublet du nucléophile puis la liaison π C=O ; élimination et déprotonation achèvent la substitution.',[start,tetra,collapsed,final],p['stage'])
    amines=np.linspace(.2,3,141);yield_curve=np.minimum(1,np.minimum(amines,(amines+base)/2)) if activation!='acid' else np.zeros_like(amines)
    return result([metric('Amide formé (bilan modèle)',amount,'équiv.'),metric('Acide piégé',acid_trapped if acid_trapped is not None else 'Protonations non calculées','équiv.' if acid_trapped is not None else ''),metric('Amine libre restante',freeamine if freeamine is not None else 'Protonations non calculées','équiv.' if freeamine is not None else ''),metric('Base extérieure restante',freebase if freebase is not None else 'Protonations non calculées','équiv.' if freebase is not None else ''),metric('Acide libéré','HCl' if activation=='chloride' else 'Acide éthanoïque' if activation=='anhydride' else 'Sel acide/base'),metric('Activation','Nécessaire pour cette amidification douce')],
        [chart('Bilan amine et piège à acide','Amine initiale / équiv.','Amide / équiv.',series('Bilan maximum avec piège stœchiométrique',amines,yield_curve))],visual,
        ['Le N porte un doublet et attaque le C électrophile ; le C n’accepte pas cinq liaisons : la liaison π C=O se déplace vers O.',
         'Chlorure/anhydride : l’intermédiaire tétraédrique élimine Cl⁻/carboxylate puis l’azote est déprotoné.',
         'Sans base extérieure, prévoir deux amines par acyle : une incorporée, une protonée. Avec une équivalence de base non nucléophile, une amine suffit.',
         'Acide carboxylique + amine non activés : le modèle montre le sel ; une amidification directe exige une autre activation ou des conditions déshydratantes explicites.'],
        ['Réactions de dérivés activés supposées rapides et sélectives ; le calcul donne un bilan maximal avec chaque acide produit entièrement piégé.',
         'Le calcul n’est pas une loi d’équilibre complète : protonations partielles et réactivité du sel ne sont pas modélisées.',
        'B désigne la base extérieure ou une deuxième amine ; le sel BH⁺/Cl⁻ ou BH⁺/éthanoate est dessiné sans liaisons covalentes entre ions.',
         'Une base tertiaire adaptée joue le rôle de piège à acide ; le chlorure d’acyle n’est pas obtenu par simple mélange d’acide et d’amine.'],amide=amount,freeamine=freeamine,freebase=freebase,acid_trapped=acid_trapped)


def protection_carbonyl_structure(state):
    """États atomisés de la protection d'une cétone dans un cétoester."""
    labels=['CH₃','C','CH₂','CH₂','C' if state in ('initial','protected') else 'CH₂']
    atoms=[atom(str(i),'C',i-1,.2*(i%2),label) for i,label in enumerate(labels)]
    bonds=[bond(i,i+1) for i in range(4)]
    if state in ('protected','reduced'):
        # C1, Oa, CH2a, CH2b, Ob is a five-membered 1,3-dioxolane ring.
        atoms += [atom('oa','O',-.6,1.1,'O'),atom('ca','C',-.5,2.1,'CH₂'),atom('cb','C',.5,2.1,'CH₂'),atom('ob','O',.6,1.1,'O')]
        bonds += [bond('1','oa'),bond('oa','ca'),bond('ca','cb'),bond('cb','ob'),bond('ob','1')]
    else:
        atoms.append(atom('ok','O',0,1.3,'OH' if state=='wrong' else 'O'))
        bonds.append(bond('1','ok',1 if state=='wrong' else 2))
        if state=='wrong': atoms[1]['label']='CH'
    if state in ('initial','protected'):
        atoms += [atom('oe','O',3,1.1,'O'),atom('om','O',4,0,'O'),atom('me','C',5,0,'CH₃')]
        bonds += [bond('4','oe',2),bond('4','om'),bond('om','me')]
    else:
        atoms.append(atom('oe','O',4,0,'OH'));bonds.append(bond('4','oe'))
    name={'initial':'4-Oxopentanoate de méthyle','protected':'Cétone protégée en 1,3-dioxolane','reduced':'Ester réduit, acétal cyclique conservé','target':'5-Hydroxypentan-2-one','wrong':'Réduction non protégée : pentane-1,4-diol'}[state]
    return molecule(name,atoms,bonds)


def protection(p):
    route=p['route'];stage=int(p['stage']);viable=route in ('valid','protected_grignard');y=p['yield']**3 if viable else 0.
    if route in ('valid','unprotected','premature'):
        initial=protection_carbonyl_structure('initial')
        protected=protection_carbonyl_structure('protected')
        reduced=protection_carbonyl_structure('reduced')
        target=protection_carbonyl_structure('target')
        wrong=protection_carbonyl_structure('wrong')
        molecules=[initial,protected,reduced,target] if route=='valid' else [initial,wrong,wrong,wrong] if route=='unprotected' else [initial,protected,initial,wrong]
        edge_labels=['HOCH₂CH₂OH, H⁺, retrait H₂O','LiAlH₄ puis hydrolyse contrôlée','H⁺ aqueux, déprotection'] if viable else ['Opération incompatible avec la cible']*3
        explanation='L’acétal est stable au réducteur basique choisi ; la déprotection acide restaure ensuite la cétone.' if viable else 'LiAlH₄ réduit aussi la cétone exposée : la fonction C=O de la cible n’est pas conservée.'
    else:
        initial=chain('2-Bromoéthanol',['HO','CH₂','CH₂','Br']);protected=chain('Alcool protégé (éther silylé)',['TBSO','CH₂','CH₂','Br'])
        coupled=chain('Après Mg, propanone et hydrolyse',['TBSO','CH₂','CH₂','C(OH)(CH₃)₂'])
        target=chain('3-Méthylbutane-1,3-diol',['HO','CH₂','CH₂','C(OH)(CH₃)₂'])
        molecules=[initial,protected,coupled,target] if viable else [initial,chain('Acido-basique consomme RMgBr',['RO⁻MgBr⁺']),chain('Hydrocarbure après protonation',['RH']),initial]
        edge_labels=['TBSCl, base adaptée','Mg anhydre, propanone, puis hydrolyse','Déprotection TBS adaptée'] if viable else ['Proton OH : destruction du réactif']*3
        explanation='Le proton O–H libre détruit un organomagnésien ; une protection compatible permet la création C–C avant déprotection.'
    nodes=[dict(id=str(i),label=m['name'],x=i,y=(.2 if i%2 else 0),molecule=m) for i,m in enumerate(molecules)]
    edges=[dict(a=str(i),b=str(i+1),label=edge_labels[i]) for i in range(3)]
    return result([metric('Séquence compatible',viable),metric('Étape visualisée',stage),metric('Rendement global conditionnel',100*y,'%'),metric('Nombre d’opérations de la route viable',3),metric('Bibliothèque','Deux objectifs, cinq séquences')],
        [chart('Coût en rendement de trois opérations','Rendement par étape','Rendement global / %',series('Route viable : η³',np.linspace(.5,1,101),100*np.linspace(.5,1,101)**3))],
        scene('network','Protection et ordre des opérations',explanation,nodes=nodes,edges=edges,active=str(stage),molecule=molecules[stage]),
        ['Identifier les fonctions à conserver et les incompatibilités avant de choisir un réactif.',
         explanation,'Protection et déprotection ajoutent des opérations : le gain de chimiosélectivité doit compenser les pertes de rendement.',
         'Chaque nœud donne une formule semi-développée ; les groupes entre parenthèses sont des abréviations explicitement nommées.'],
        ['Bibliothèque de deux cibles et réactifs imposés, sans moteur de compatibilité universel.',
         'Acétalisation catalysée par H⁺ et retrait d’eau ; hydrolyse acide aqueuse de l’acétal. La séquence exige un traitement contrôlé entre réducteur et milieu acide.',
         'TBS = tert-butyldiméthylsilyle ; protection/déprotection et travail de l’organomagnésien doivent être compatibles avec les autres fonctions.',
         'Rendements par opération imposés, pas prédits à partir de la structure.'],viable=viable,global_yield=y,molecules=molecules,active=stage)


def enolate_graph(phenyl=True):
    return molecule('Énolate : forme C nucléophile',[atom('r','C',0,0,'Ph' if phenyl else 'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O',lone_pairs=2),atom('a','C',2,0,'CH₂',-1,lone_pairs=1)],
       [bond('r','c'),bond('c','o',2),bond('c','a')])


def aldol(p):
    donor=p['donor'];acceptor=p['acceptor'];mode=p['mode'];blocked=donor=='benzaldehyde';selective=not blocked and (acceptor=='benzaldehyde' or mode=='directed')
    rd='Ph' if donor=='acetophenone' else 'CH₃';ra='Ph' if acceptor=='benzaldehyde' else 'CH₃'
    donor_m=structure('acetophenone' if donor=='acetophenone' else 'acetone' if donor=='acetone' else 'benzaldehyde')
    acc=structure('benzaldehyde') if acceptor=='benzaldehyde' else chain('Éthanal',['CH₃','CHO'])
    eno=enolate_graph(donor=='acetophenone');eno['arrows']=[electron_arrow([2.2,0],[3.3,0],[2.8,.6])]
    eno['atoms'].extend([atom('ac','C',3.3,0,'CH'),atom('ao','O',3.3,1.1,'O',lone_pairs=2),atom('ar','C',4.3,0,ra)])
    eno['bonds'].extend([bond('ac','ao',2),bond('ac','ar')]);eno['arrows'].append(electron_arrow([3.3,.55],[3.3,1.1],[3.7,.8]))
    def beta_hydroxy(name,charged):
        return molecule(name,[atom('r','C',0,0,rd),atom('c','C',1,0,'C'),atom('o','O',1,1,'O',lone_pairs=2),atom('a','C',2,0,'CH₂'),atom('b','C',3,0,'CH'),atom('bo','O',3,1,'O' if charged else 'OH',-1 if charged else 0,lone_pairs=3 if charged else 2),atom('ar','C',4,0,ra)],
          [bond('r','c'),bond('c','o',2),bond('c','a'),bond('a','b'),bond('b','bo'),bond('b','ar')])
    alkoxide=beta_hydroxy('Alcoolate β : liaison C–C nouvelle',True)
    aldol_m=beta_hydroxy('β-Hydroxycétone',False)
    condensation=chain('Énone conjuguée',[rd,'CO','CH','CH',ra],[1,1,2,1])
    frames=[donor_m,eno,alkoxide,condensation if mode=='condensation' else aldol_m]
    if blocked: frames=[donor_m]*4
    label='Chalcone' if donor=='acetophenone' and acceptor=='benzaldehyde' and mode=='condensation' else 'β-Hydroxycétone' if mode!='condensation' else 'Énone conjuguée'
    ex,e=energy_profile([0,7,-12,-20 if mode=='condensation' else -12],[42,30,27])
    return result([metric('Hα du donneur',0 if blocked else 3 if donor=='acetophenone' else 6),metric('Voie énolate possible',not blocked),metric('Croisée contrôlée dans les conditions choisies',selective),metric('Produit visé',label if not blocked else 'Pas d’énolate de ce donneur'),metric('Liaison C–C nouvelle',0 if blocked else 1),metric('Crotonisation','− H₂O et conjugaison' if mode=='condensation' else 'Non demandée')],
        [chart('Profil mécanistique illustratif, non mesuré','Coordonnée de réaction','G / kJ·mol⁻¹',series('Étapes imposées',ex,e))],
        mechanism_scene('De l’énolate au squelette carboné',
          'Ph = phényle ; la forme mésomère C de l’énolate porte le doublet qui forme C–C. Les groupes CO sont des carbonyles abrégés.',frames,p['stage']),
        ['Vérifier Hα avant d’écrire un énolate. Le benzaldéhyde a un H sur CHO, mais aucun carbone α portant H : il ne donne pas cet énolate.',
         'Le Cα de l’énolate attaque le C de C=O accepteur, pendant que les électrons π se déplacent sur O ; protoner donne le β-hydroxycarbonyle.',
         'Crotonisation : éliminer H₂O entre Cα et Cβ ; la nouvelle liaison C=C est conjuguée à C=O.',
         'Deux partenaires énolisables mélangés sans contrôle donnent en général plusieurs aldols ; préformer un énolate puis ajouter l’accepteur peut contrôler la croisée.'],
        ['Bibliothèque acétophénone/propanone/benzaldéhyde et benzaldéhyde/éthanal ; sélectivité dirigée supposée avec conditions appropriées.',
         'L’état d’énolate du schéma est mésomère : aucune alternance temporelle entre formes de résonance n’est impliquée.',
         'Les niveaux du profil sont illustratifs, pas des valeurs cinétiques expérimentales ; Cannizzaro et autres voies du benzaldéhyde ne sont pas simulées.',
         'En mode crotonisation, l’énone est visée sous conditions de déshydratation favorables ; sa formation n’est pas universellement quantitative.'],blocked=blocked,selective=selective,frames=frames,donor_alpha_h=0 if blocked else 3 if donor=='acetophenone' else 6)


def michaelwittig(p):
    reaction=p['reaction'];reagent=p['reagent'];stage=p['stage'];valid=True
    if reaction=='michael':
        valid=reagent in ('enolate','grignard','cuprate');mode='1,2' if reagent=='grignard' else '1,4'
        acceptor=molecule('But-3-én-2-one : sites C=O et Cβ',[atom('m','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O'),atom('a','C',2,0,'CH'),atom('b','C',3,0,'CH₂')],[bond('m','c'),bond('c','o',2),bond('c','a'),bond('a','b',2)])
        malonate=reagent=='enolate';nucleophile='Carbanion stabilisé du malonate de diméthyle' if malonate else 'CH₃ apporté par CH₃MgBr' if reagent=='grignard' else 'CH₃ apporté par (CH₃)₂CuLi'
        attacked=molecule('Attaque nucléophile '+mode,acceptor['atoms']+[atom('nu','C',3,-1,'CH' if malonate else 'CH₃',-1,lone_pairs=1)],list(acceptor['bonds']))
        if malonate:
            attacked['atoms'] += [atom('ester1','C',2.2,-2,'CO₂Me'),atom('ester2','C',3.8,-2,'CO₂Me')]
            attacked['bonds'] += [bond('nu','ester1'),bond('nu','ester2')]
        if mode=='1,4':
            attacked['arrows']=[electron_arrow([3,-.8],[3,0],[3.5,-.5]),electron_arrow([2.5,0],[1.5,0],[2,.6]),electron_arrow([1,.5],[1,1],[.6,.8])]
            intermediate=molecule('Énolate après addition conjuguée',[atom('m','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O',-1,lone_pairs=3),atom('a','C',2,0,'CH'),atom('b','C',3,0,'CH₂'),atom('nu','C',4,0,'CH' if malonate else 'CH₃')],[bond('m','c'),bond('c','o'),bond('c','a',2),bond('a','b'),bond('b','nu')])
            if malonate:
                intermediate['atoms'] += [atom('ester1','C',4,1,'CO₂Me'),atom('ester2','C',5,0,'CO₂Me')];intermediate['bonds'] += [bond('nu','ester1'),bond('nu','ester2')]
            product=molecule('Carbonyle conservé : adduit malonate/MVK' if malonate else 'Carbonyle conservé : pentan-2-one',
               [dict(a,label='O',charge=0,lone_pairs=2) if a['id']=='o' else dict(a,label='CH₂') if a['id']=='a' else dict(a) for a in intermediate['atoms']],
               [dict(b,order=2) if (b['a'],b['b'])==('c','o') else dict(b,order=1) if (b['a'],b['b'])==('c','a') else dict(b) for b in intermediate['bonds']])
            caption='Un nucléophile stabilisé ou organocuprate favorise souvent 1,4 ; le carbonyle est restauré après protonation.'
        else:
            attacked['arrows']=[electron_arrow([3,-1],[1,0],[2,-1]),electron_arrow([1,.5],[1,1],[.6,.8])]
            intermediate=molecule('Alcoolate allylique',[atom('m','C',0,0,'CH₃'),atom('c','C',1,0,'C'),atom('o','O',1,1,'O',-1,lone_pairs=3),atom('nu','C',1,-1,'CH₃'),atom('a','C',2,0,'CH'),atom('b','C',3,0,'CH₂')],[bond('m','c'),bond('c','o'),bond('c','nu'),bond('c','a'),bond('a','b',2)])
            product=molecule('2-Méthylbut-3-én-2-ol après hydrolyse',[dict(a,label='OH',charge=0,lone_pairs=2) if a['id']=='o' else dict(a) for a in intermediate['atoms']],intermediate['bonds']);caption='Organomagnésien dur : tendance 1,2 dans ce cas ; conditions et substrat peuvent modifier la compétition.'
        frames=[acceptor,attacked,intermediate,product]
        atom_economy='Dépend du nucléophile et du travail réactionnel'
    else:
        valid=reagent in ('unstabilized','stabilized');mode='Z favorisé (cas usuel)' if reagent=='unstabilized' else 'E favorisé (cas usuel)'
        substituent='CH₃' if reagent=='unstabilized' else 'CO₂Et'
        acceptor=structure('benzaldehyde');ylure=molecule('Ylure non stabilisé' if reagent=='unstabilized' else 'Ylure stabilisé',[atom('p','P',0,0,'Ph₃P',1),atom('c','C',1,0,'CH',-1,lone_pairs=1),atom('r','C',2,0,substituent),atom('ac','C',4,0,'CH'),atom('ao','O',4,1,'O',lone_pairs=2),atom('ph','C',5,0,'Ph')],[bond('p','c'),bond('c','r'),bond('ac','ao',2),bond('ac','ph')],
          [electron_arrow([1,.2],[4,0],[2.5,1.2]),electron_arrow([4,.5],[4,1],[4.4,.75])])
        intermediate=molecule('Oxaphosphetane : cycle à 4 atomes',[atom('c','C',0,0,'CHPh'),atom('o','O',1,0,'O'),atom('p','P',1,1,'PPh₃'),atom('y','C',0,1,'CH'+substituent)],[bond('c','o'),bond('o','p'),bond('p','y'),bond('y','c')],
          [electron_arrow([.5,0],[0,.5],[-.1,0]),electron_arrow([.5,1],[1,.5],[1.1,1])])
        product=chain('Alcène Ph–CH=CH–'+substituent,['Ph','CH','CH',substituent],[1,2,1]);oxide=molecule('Oxyde de triphénylphosphine',[atom('p','P',0,0,'Ph₃P'),atom('o','O',1,0,'O')],[bond('p','o',2)])
        atoms=list(product['atoms'])+[dict(a,id='oxide_'+a['id'],x=a['x']+5) for a in oxide['atoms']]
        bonds=list(product['bonds'])+[dict(b,a='oxide_'+b['a'],b='oxide_'+b['b']) for b in oxide['bonds']]
        final=molecule('Alcène + oxyde de triphénylphosphine',atoms,bonds)
        frames=[acceptor,ylure,intermediate,final]
        caption='Le carbone carbonylé et le carbone de l’ylure donnent C=C ; l’oxygène quitte le produit carboné dans Ph₃P=O.'
        atom_economy='Sous-produit massif Ph₃P=O (278,29 g/mol)'
    if not valid: frames=[frames[0]]*4;caption='Le couple de réglages n’appartient pas à la bibliothèque : choisir un nucléophile pour Michael ou un ylure pour Wittig.';mode='Association de réglages non applicable'
    return result([metric('Famille', 'Addition conjuguée / directe' if reaction=='michael' else 'Oléfination de Wittig'),metric('Tendance conditionnelle',mode),metric('Réglages compatibles',valid),metric('Nucléophile nommé',('Association non applicable' if not valid else nucleophile if reaction=='michael' else 'Ph₃P⁺–C⁻H–CH₃' if reagent=='unstabilized' else 'Ph₃P⁺–C⁻H–CO₂Et')),metric('Liaison créée','C–C puis carbonyle conservé' if reaction=='michael' and reagent!='grignard' else 'C–C puis alcool' if reaction=='michael' else 'C=C'),metric('Économie d’atomes',atom_economy)],
        [chart('Comparer étapes et bilan : profil illustratif','Coordonnée de réaction','G / kJ·mol⁻¹',series('Modèle qualitatif',*energy_profile([0,5,-8,-18],[30,25,17])))],
        mechanism_scene('Michael / Wittig : destination des atomes',caption,frames,stage),
        ['Michael : compter 1 = O, 2 = C carbonylé, 3 = Cα, 4 = Cβ ; la notation 1,4 n’est pas une numérotation IUPAC de la molécule.',
         'Nu dur/doux et stabilisation guident une tendance ; vérifier substrat, contre-ion, solvant et conditions avant de conclure à une sélectivité.',
         'Wittig : distinguer ylure stabilisé par groupe attracteur et ylure non stabilisé. Les tendances E/Z usuelles ne prédisent pas tous les cas, notamment variantes Schlosser.',
         'La formation forte de P=O favorise l’oléfination, mais son sous-produit pénalise l’économie d’atomes. Ph = C₆H₅ ; Et = C₂H₅ ; Me = CH₃.'],
        ['Les substituants Ph, Et, Me et CO₂Me/Et sont des groupes abrégés ; les contre-ions MgBr⁺/Li⁺ et ligands cuivre ne sont pas dessinés. CH₃⁻ représente un équivalent carbanionique, pas une espèce libre isolable.',
         'Michael : pas de taux 1,2/1,4 numérique inventé ; les paramètres choisissent trois cas pédagogiques.',
         'Wittig : cycle oxaphosphetane représenté sans imposer une bétaïne libre dans toutes les conditions ; aucune proportion E/Z universelle simulée.'],valid=valid,mode=mode,frames=frames)


def dielsalder(p):
    T=p['temperature'];locked=p['diene']=='cyclopentadiene';accessible=locked or p['conformation']=='cis'
    cis=p['dienophile']=='maleate'
    endo_applicable=locked and cis
    if p['regime']=='kinetic':
        endo=1/(1+math.exp(-p['barrier_difference']*1000/(R*T)));selection='Rapport de vitesses initiales'
    else:
        endo=1/(1+math.exp(p['energy_difference']*1000/(R*T)));selection='Rapport d’équilibre sous réversibilité'
    diene=molecule('Diène s-cis' if accessible else 'Diène s-trans à convertir',[atom('1','C',0,1,'CH₂'),atom('2','C',1,1,'CH'),atom('3','C',1,0,'CH'),atom('4','C',0 if accessible else 2,0,'CH₂')],[bond('1','2',2),bond('2','3'),bond('3','4',2)])
    if locked:
        diene['name']='Cyclopentadiène s-cis'
        for a in diene['atoms']:a['label']='CH'
        diene['atoms'].append(atom('5','C',-.7,.5,'CH₂'));diene['bonds']+=[bond('1','5'),bond('4','5')]
    dienophile=molecule('Maléate de diéthyle (cis)' if cis else 'Fumarate de diéthyle (trans)',
      [atom('l','C',0,0,'C'),atom('r','C',1.4,0,'C'),atom('sl','C',-.5,.866,'CO₂Et'),atom('sr','C',1.9,.866 if cis else -.866,'CO₂Et'),atom('hl','H',-.5,-.866,'H'),atom('hr','H',1.9,-.866 if cis else .866,'H')],
      [bond('l','r',2),bond('l','sl'),bond('r','sr'),bond('l','hl'),bond('r','hr')])
    atoms=[atom(i,'C',math.cos(i*math.pi/3),math.sin(i*math.pi/3),label='') for i in range(6)]
    for a in atoms:a['label']=''
    bonds=[bond(i,(i+1)%6,2 if i==1 else 1) for i in range(6)]
    atoms.extend([atom('s4','C',-.9,-1.55,'CO₂Et'),atom('s5','C',.9,-1.55,'CO₂Et')]);bonds.extend([bond(4,'s4',style='wedge'),bond(5,'s5',style='wedge' if cis else 'dash')])
    if locked:
        atoms.append(atom('bridge','C',0,0,'CH₂'));bonds.extend([bond(0,'bridge'),bond(3,'bridge')])
    product=molecule('Adduit bicyclique' if locked else 'Cyclohexène substitué',atoms,bonds)
    temperatures=np.linspace(250,450,151)
    kinetic=1/(1+np.exp(-p['barrier_difference']*1000/(R*temperatures)))
    eq=1/(1+np.exp(p['energy_difference']*1000/(R*temperatures)))
    ratios_chart=chart('Cinétique et équilibre : paramètres indépendants','T / K','Endo / %',series('Barrières : cinétique',temperatures,100*kinetic),series('Énergies : équilibre',temperatures,100*eq))
    if not endo_applicable:
        endo=None
        selection='Pas de deux produits tout endo/tout exo pour le cas choisi'
        ratios_chart=chart('Comptage des liaisons dans la cycloaddition','0 : réactifs ; 1 : adduit','Nombre de liaisons',series('Liaisons π', [0,1],[3,1]),series('Liaisons σ nouvelles',[0,1],[0,2]))
    return result([metric('Diène accessible s-cis',accessible),metric('Diène bloqué s-cis',locked),metric('Relation conservée du diènophile','cis' if cis else 'trans'),metric('Endo dans le modèle',100*endo if endo is not None else 'Rapport non applicable','%' if endo is not None else ''),metric('Exo dans le modèle',100*(1-endo) if endo is not None else 'Rapport non applicable','%' if endo is not None else ''),metric('Nature du rapport',selection),metric('Liaisons σ C–C créées',2)],
        [ratios_chart],
        reaction_scene('Cycloaddition [4+2] : connectivité et stéréospécificité',
          'Le produit conserve cis/trans du diènophile. Les coins indiquent cette relation ; le ratio tout endo/tout exo n’est calculé que pour le diène cyclique + diènophile cis.',[diene,dienophile,product],[dict(a=0,b=2,label='Concertée, géométrie s-cis' if accessible else 'Rotation s-cis requise avant cycloaddition')]),
        ['Le diène doit présenter ses deux extrémités avec la géométrie s-cis ; un diène acyclique s-trans peut tourner, mais ne réagit pas depuis cette géométrie.',
         'Deux liaisons π du diène et une du diènophile deviennent deux liaisons σ et une liaison π : six électrons participent au cycle concerté.',
         'Stéréospécificité : substituants cis du diènophile restent cis ; trans restent trans. Endo/exo est une distinction supplémentaire pour les cas appropriés.',
         'La préférence endo cinétique est fréquente, notamment avec des diènophiles π-accepteurs, mais dépend du substrat et des conditions ; le curseur peut inverser les barrières. Et = C₂H₅.'],
        ['Régiosélectivité non calculée depuis des coefficients orbitaux ; systèmes symétriques choisis pour éviter une fausse généralité.',
         'Rapport cinétique : mêmes préfacteurs, deux voies irréversibles parallèles, ΔΔG‡ imposé. Rapport d’équilibre : réversibilité effective supposée, ΔG imposé.',
         'Diènophile trans symétrique avec cyclopentadiène : un ester endo et l’autre exo, pas deux produits tout endo/tout exo. Avec butadiène acyclique, endo décrit une approche, pas nécessairement deux produits isolables.',
         'Les contrôles ΔΔG‡ et ΔG n’ont d’effet sur les proportions que pour cyclopentadiène + maléate cis dans la bibliothèque.',
         'La température seule ne garantit pas l’équilibre : il faut aussi une rétro-Diels–Alder accessible et un temps suffisant.',
         'Les proportions sont conditionnelles à une géométrie réactive ; aucune vitesse absolue ou population s-cis ne sont prédites.'],accessible=accessible,endo=endo,exo=1-endo if endo is not None else None,endo_applicable=endo_applicable,cis=cis,product=product)


ROUTES={
 'aspirin':dict(name='Aspirine',short=['Acide salicylique','Acylation phénol par anhydride','Aspirine'],long=['Phénol','Carboxylation adaptée (Kolbe–Schmitt)','Acide salicylique','Acylation','Aspirine'],wrong=['Acide salicylique','Acide éthanoïque seul sans activation','Mélange, cible non garantie'],mass=180.16,atom_economy=180.16/(138.12+102.09),motif='Liaison O(phénol)–C(acyle), groupe COOH conservé'),
 'paracetamol':dict(name='Paracétamol',short=['p-Aminophénol','Acylation chimiosélective N','Paracétamol'],long=['p-Nitrophénol','Réduction NO₂ → NH₂','p-Aminophénol','Acylation adaptée','Paracétamol'],wrong=['p-Nitrophénol','Acylation O avant réduction','Produit autre que cible directe'],mass=151.16,atom_economy=151.16/(109.13+102.09),motif='Liaison N–C(acyle), OH phénolique conservé sous conditions adaptées'),
 'chalcone':dict(name='Chalcone',short=['Acétophénone + benzaldéhyde','Aldol croisée puis déshydratation','Chalcone'],long=['Benzène','Acylation de Friedel–Crafts','Acétophénone','Aldol/crotonisation','Chalcone'],wrong=['Benzaldéhyde comme donneur énolate','Absence de Hα','C–C non créée par cette voie'],mass=208.26,atom_economy=208.26/(120.15+106.12),motif='Disconnexion Cα–Cβ : Cα donneur acétophénone, Cβ ancien carbonyle benzaldéhyde'),
 'alcohol':dict(name='1-Phényléthanol',short=['Benzaldéhyde + CH₃MgBr','Addition puis hydrolyse','1-Phényléthanol racémique'],long=['Benzène','Acylation → acétophénone','Réduction NaBH₄','1-Phényléthanol racémique'],wrong=['Benzaldéhyde en eau','Ajouter CH₃MgBr : réactif détruit','Pas de bilan de synthèse viable'],mass=122.17,atom_economy=None,motif='Liaison C(carbinol)–CH₃ ; O du carbonyle devient OH après hydrolyse'),
 'aromatic':dict(name='3-Nitroacétophénone',short=['Benzène','Acylation de Friedel–Crafts','Acétophénone','Nitration dirigée méta','3-Nitroacétophénone majoritaire'],long=['Benzaldéhyde + CH₃MgBr','Addition puis hydrolyse','1-Phényléthanol','Oxydation benzylique MnO₂ activé','Acétophénone','Nitration méta','3-Nitroacétophénone'],wrong=['Benzène','Nitration','Nitrobenzène','Friedel–Crafts fortement défavorisée','Route non viable par cette méthode'],mass=165.15,atom_economy=None,motif='Introduire COCH₃ avant NO₂ ; NO₂ désactive trop pour la Friedel–Crafts choisie')
}


def target_structure(target):
    """Graphes atomisés des cinq cibles, avec H implicites usuels du squelette."""
    ring=benzene()
    atoms=[dict(a) for a in ring['atoms']];bonds=[dict(b) for b in ring['bonds']]
    if target=='aspirin':
        atoms += [atom('ophenol','O',1.8,0,'O'),atom('acetyl','C',2.7,0,'C'),atom('oacetyl','O',2.7,1,'O'),atom('methyl','C',3.6,0,'CH₃'),atom('carboxyl','C',.9,1.56,'C'),atom('ocarboxyl','O',.35,2.35,'O'),atom('ohacid','O',1.8,2.05,'OH')]
        bonds += [bond('0','ophenol'),bond('ophenol','acetyl'),bond('acetyl','oacetyl',2),bond('acetyl','methyl'),bond('1','carboxyl'),bond('carboxyl','ocarboxyl',2),bond('carboxyl','ohacid')]
    elif target=='paracetamol':
        atoms += [atom('n','N',1.8,0,'NH',lone_pairs=1),atom('acetyl','C',2.7,0,'C'),atom('oacetyl','O',2.7,1,'O'),atom('methyl','C',3.6,0,'CH₃'),atom('oh','O',-1.8,0,'OH')]
        bonds += [bond('0','n'),bond('n','acetyl'),bond('acetyl','oacetyl',2),bond('acetyl','methyl'),bond('3','oh')]
    elif target=='chalcone':
        right=benzene()
        atoms += [atom('carbonyl','C',2,0,'C'),atom('o','O',2,1,'O'),atom('alpha','C',3,0,'CH'),atom('beta','C',4,0,'CH')]
        atoms += [dict(a,id='right_'+a['id'],x=a['x']+6) for a in right['atoms']]
        bonds += [bond('0','carbonyl'),bond('carbonyl','o',2),bond('carbonyl','alpha'),bond('alpha','beta',2),bond('beta','right_3')]
        bonds += [dict(b,a='right_'+b['a'],b='right_'+b['b']) for b in right['bonds']]
    elif target=='alcohol':
        atoms += [atom('carbinol','C',1.9,0,'CH'),atom('oh','O',1.9,1,'OH'),atom('methyl','C',2.9,0,'CH₃')]
        bonds += [bond('0','carbinol'),bond('carbinol','oh'),bond('carbinol','methyl')]
    elif target=='aromatic':
        atoms += [atom('acetyl','C',1.9,0,'C'),atom('oacetyl','O',1.9,1,'O'),atom('methyl','C',2.9,0,'CH₃'),atom('n','N',-.9,1.56,'N',1),atom('osingle','O',-1.8,1.8,'O',-1),atom('odouble','O',-.6,2.5,'O')]
        bonds += [bond('0','acetyl'),bond('acetyl','oacetyl',2),bond('acetyl','methyl'),bond('2','n'),bond('n','osingle'),bond('n','odouble',2)]
    else:
        raise ValueError('Cible inconnue dans cette bibliothèque.')
    return molecule(ROUTES[target]['name']+(' (racémique)' if target=='alcohol' else ''),atoms,bonds)


def retrosynthese(p):
    data=ROUTES[p['target']];route=p['route'];labels=data[route];viable=route!='wrong';operations=(len(labels)-1)//2 if route=='short' else (len(labels)-1)//2+1
    # Explicit operation count, avoiding graph-node labels being mistaken for chemistry steps.
    operations={('aspirin','short'):1,('aspirin','long'):2,('paracetamol','short'):1,('paracetamol','long'):2,('chalcone','short'):1,('chalcone','long'):2,('alcohol','short'):1,('alcohol','long'):2,('aromatic','short'):2,('aromatic','long'):3}.get((p['target'],route),0)
    y=p['yield']**operations if viable else 0.;n=p['scale']*y;mass=n*data['mass']/1000
    nodes=[dict(id=str(i),label=label,x=i,y=.3*(i%2)) for i,label in enumerate(labels)]
    target_molecule=target_structure(p['target'])
    if viable:nodes[-1]['molecule']=target_molecule
    edges=[dict(a=str(i),b=str(i+1),label='Séquence explicite') for i in range(len(labels)-1)]
    eta=np.linspace(.5,.99,101)
    metrics=[metric('Cible',data['name']),metric('Route viable dans la bibliothèque',viable),metric('Opérations isolées comptées',operations),metric('Rendement global',100*y,'%'),metric('Quantité cible',n,'mmol'),metric('Masse cible',mass,'g'),metric('Économie d’atomes de l’étape clé','Bilan complet des réactifs requis' if data['atom_economy'] is None else 100*data['atom_economy'],'%' if data['atom_economy'] is not None else '')]
    return result(metrics,[chart('Chaque perte se multiplie','Rendement par opération','Rendement global / %',series('Une opération',eta,100*eta),series('Deux opérations',eta,100*eta**2),series('Trois opérations',eta,100*eta**3))],
        scene('network','Rétrosynthèse puis sens de synthèse',data['motif']+' Encart : structure de la cible visée'+(' ; elle n’est pas atteinte par la route incompatible.' if not viable else '.'),nodes=nodes,edges=edges,active=str(len(labels)-1) if viable else '2',molecule=target_molecule),
        [data['motif'],'Une flèche rétrosynthétique propose des précurseurs ; la flèche de synthèse doit préciser réactifs, compatibilités et travail réactionnel.',
         'Le rendement global d’une suite linéaire est le produit des rendements isolés. Un nœud de diagramme n’est pas nécessairement une opération isolée.',
         'L’économie d’atomes ne dépend pas du rendement. Pour aspirine/paracétamol/chalcone, le bilan affiché de l’étape clé inclut anhydride ou eau éliminée ; solvants et catalyseurs ne sont pas comptés.',
         'Nitrobenzène : NO₂ est méta-directeur et fortement désactivant ; placer une Friedel–Crafts après nitration ne valide pas une route.'],
        ['Bibliothèque de cinq cibles et routes nommées, pas d’optimisation automatique ni de synthèse universelle.',
         'Les rendements sont imposés égaux par opération ; la quantité de référence suppose l’autre partenaire disponible et aucun facteur de changement d’échelle.',
         'Une acylation chimiosélective de p-aminophénol demande conditions adaptées ; la nitration donne un produit majoritaire, pas un isomère unique.',
         'Une opération addition puis hydrolyse ou aldol puis crotonisation peut être groupée sans isolation intermédiaire ; les comptes d’opérations le précisent.'],viable=viable,operations=operations,global_yield=y,amount=n,mass=mass,atom_economy=data['atom_economy'])


def carothers(p,r): return (1+r)/(1+r-2*r*p)


def polymeres(p):
    conversion=p['conversion'];r=p['ratio'];step=p['mode']=='step';initial=p['monomers'];grid=np.linspace(.1,.999,451)
    if step:
        DP=carothers(conversion,r);chains=initial/DP
        # Total initial monomer entities = NA + NB, each bifunctional.
        na=initial/(1+r);nb=r*na;bonds=2*nb*conversion;remaining=initial-bonds
        mass_repeat=226.32 # ideal mean repeat pair nylon-6,6 after two waters.
        # DP counts monomer molecules AA and BB, not the AA+BB repeat pair.
        degree_repeat=DP/2
        labels=['Entités monomères initiales','Liaisons formées = eaux','Molécules restantes'];values=[initial,bonds,remaining]
        charts=[chart('Carothers : conversion et stœchiométrie','p des fonctions B limitantes','DPₙ (entités monomères)',series('r choisi',grid,carothers(grid,r)),series('r = 1',grid,carothers(grid,1))),chart('Déséquilibre à conversion fixée','r = N₀B/N₀A','DPₙ',series('Conversion imposée',np.linspace(.7,1,151),carothers(conversion,np.linspace(.7,1,151))))]
        desc='AA+BB bifonctionnels : DPₙ compte les entités AA et BB incorporées. Une répétition structurale du nylon-6,6 contient une unité de chaque, soit environ DPₙ/2 répétitions à grande chaîne.'
        economy=100*226.32/(146.14+116.20);name='Polycondensation type nylon-6,6'
    else:
        chains=p['chains'];DP=initial*conversion/chains;degree_repeat=DP;na=nb=0.;bonds=None;remaining=initial*(1-conversion)
        labels=['Monomère converti','Monomère restant','Chaînes imposées'];values=[initial*conversion,remaining,chains]
        charts=[chart('Croissance en chaîne : bilan, pas cinétique','Conversion des monomères','DPₙ',series('Nmonomères convertis/Nchaînes',grid,initial*grid/chains))]
        desc='Polymérisation d’addition de l’éthylène : un nombre de chaînes est imposé. Le modèle calcule un bilan de longueur moyenne, sans propagation/terminaison ou distribution.';economy=100.;name='Polyéthylène : addition'
    valid=step or DP>=1
    if not valid:desc+=' Le bilan imposé donne moins d’un monomère par chaîne : toutes les initiations ne peuvent donc pas être des chaînes polymères, domaine du modèle dépassé.'
    return result([metric('Modèle',name),metric('DPₙ' if valid else 'DPₙ formel, hors domaine',DP),metric('Hypothèses compatibles',valid),metric('Répétitions structurales moyennes approximées',degree_repeat),metric('Molécules/chaînes restantes',chains,'mmol'),metric('Conversion',100*conversion,'%'),metric('Économie d’atomes idéale',economy,'%'),metric('Stœchiométrie r',r if step else 'Non applicable au monomère éthylène')],charts,
        bars_scene('Compter fonctions, liaisons et chaînes',desc,labels,values,'mmol'),
        ['Croissance par étapes : chaque liaison intermoléculaire diminue de un le nombre de molécules ; N = N₀−2N₀B p, d’où DPₙ = (1+r)/(1+r−2rp).',
         'Pour r=1 : DPₙ=1/(1−p). Pour r<1 et p→1 : DPₙ→(1+r)/(1−r), même à conversion très élevée.',
         'Polyaddition en chaîne : un monomère entre dans une chaîne active ; DPₙ dépend aussi du nombre de chaînes, des transferts et terminaisons.',
         'Nylon-6,6 : hexane-1,6-diamine + acide adipique → motif C₁₂H₂₂N₂O₂ + 2 H₂O. Polyéthylène : les atomes de l’éthylène entrent idéalement tous dans le polymère.'],
        ['Carothers : uniquement bifonctionnels, réactivité égale, liaisons intermoléculaires sans cycles, pas de branchement, p conversion des fonctions B limitantes.',
         'r ≤ 1 par définition avec NA ≥ NB ; DPₙ compte toutes les molécules/oligomères dans cette moyenne en nombre.',
         'Conversion limitée à 0,999 pour garder un DP fini ; aucune prédiction de viscosité, polydispersité ou vitesse.',
         'En chaîne : nombre de chaînes imposé constant et assez de monomère converti pour que chacune comporte au moins une unité. Sinon seul un bilan formel, hors domaine, est affiché ; pas de masse d’initiateur ni de groupes terminaux dans l’économie d’atomes idéale.'],DP=DP,chains=chains,remaining=remaining,bonds=bonds,initial=initial,repeat_degree=degree_repeat,valid=valid,atom_economy=economy/100)


MODELS={name:globals()[name] for name in ('formule','stereo','conformeres','ir','rmn','ccm','extraction','esterification','acylation','protection','aldol','michaelwittig','dielsalder','retrosynthese','polymeres')}


def calculate(lab_id,params):
    if lab_id not in MODELS: raise ValueError('Laboratoire inconnu.')
    return MODELS[lab_id](params)
