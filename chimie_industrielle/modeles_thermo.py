"""Bilans stœchiométriques, équilibres et diagrammes de phases.

Toutes les pressions logarithmiques sont réduites par p°=1 bar.
Les données arrondies et les limites du modèle sont affichées dans chaque TP.
"""
import math
import numpy as np
from commun import metric,chart,series,result,table,curve_scene,plane_scene,field_scene
R=8.31446261815324

def _curve(title,x,curves,xlabel,ylabel,description=''):
    return curve_scene(title,x,curves,xlabel,ylabel,description)

def hess_combustion(p):
    # Hf° at 298 K in kJ/mol; CH3OH is liquid, product water can condense.
    data={'methane':('CH₄',16.043,-74.87,1,2), 'hydrogen':('H₂',2.016,0,0,1),
          'methanol':('CH₃OH(l)',32.042,-238.7,1,2)}
    name,M,hf,co2,water=data[p['fuel']]
    hprod=co2*(-393.51)+water*(-241.826)
    dh=hprod-hf; latent=water*(285.830-241.826)
    pci=-dh/M; pcs=(-dh+latent)/M # kJ/g = MJ/kg.
    recover=p['recovery']*(pci+p['condensation']*(pcs-pci))
    f=np.linspace(0,1,101); released=pci+f*(pcs-pci)
    paths=[dict(label='Cycle de Hess',x=[0,1,2],y=[hf,0,hprod])]
    sc=plane_scene('Cycle de Hess : états et énergie',paths=paths,
        points=[dict(x=0,y=hf,label='Réactifs',group=0),dict(x=1,y=0,label='Éléments standard',group=1),dict(x=2,y=hprod,label='Produits, eau gazeuse',group=2)],
        xlabel='État du cycle',ylabel='H° relatif (kJ·mol⁻¹)',description='Le zéro est celui des éléments standard ; le bilan de combustion est la différence entre les deux extrémités.')
    sc['equalAspect']=False
    return result([metric('PCI',round(pci,3),'MJ·kg⁻¹'),metric('PCS',round(pcs,3),'MJ·kg⁻¹'),metric('Chaleur récupérée',round(recover,3),'MJ·kg⁻¹'),metric('CO₂ direct',round(co2*44.01/M,3),'kg·kg⁻¹')],
      [chart('Condensation et chaleur disponible','Fraction d’eau condensée','Énergie (MJ·kg⁻¹)',series('Chaleur de combustion',f,released),series('Chaleur récupérée',f,p['recovery']*released))],sc,
      [f'Pour 1 mol de {name}, ΔrH°=ΣνᵢΔfHᵢ°={dh:.3f} kJ·mol⁻¹ avec eau gazeuse.',
       f'La condensation ajoute {latent:.3f} kJ par mole de combustible. PCI et PCS diffèrent uniquement par cette eau dans le modèle.',
       'Multiplier la chaleur disponible par la fraction récupérée ; vérifier les unités avant de comparer un kilogramme et une mole.'],
      ['Enthalpies standard à 298 K arrondies ; aucune cinétique ni perte de combustion incomplète.',
       'CO₂ direct du combustible seulement : la production de H₂, le transport et les auxiliaires ne sont pas comptés.',
       'Récupération et condensation sont des réglages distincts, sans modèle de l’échangeur.'],
      table('Bilan pour une mole de combustible',['Grandeur','Valeur','Unité'],[['M',M,'g·mol⁻¹'],['ΔfH° combustible',hf,'kJ·mol⁻¹'],['n(CO₂)',co2,'mol'],['n(H₂O)',water,'mol'],['ΔrH° eau vapeur',round(dh,3),'kJ·mol⁻¹'],['ΔrH° eau liquide',round(dh-latent,3),'kJ·mol⁻¹']]))

H_NO_REF=-36*(400-298)/.07 # From the experimental heat-loss balance, not a high-T database.
def adiabatic_temperature(initial,inert,loss,extent=1.):
    x=np.asarray(extent)
    h=H_NO_REF-7.5*(initial-298)
    cp=43.5-7.5*x+29*inert
    return initial-(1-loss)*h*x/cp

def temperature_adiabatique(p):
    x=np.linspace(0,1,151); actual=adiabatic_temperature(p['initial'],p['inert'],p['loss'],x)
    ideal=adiabatic_temperature(p['initial'],p['inert'],0,x)
    dilution=np.linspace(0,12,101); tf=adiabatic_temperature(p['initial'],dilution,p['loss'])
    return result([metric('Température finale',round(float(actual[-1]),2),'K'),metric('Hausse adiabatique',round(float(ideal[-1])-p['initial'],2),'K'),metric('ΔrH°(298 K)',round(H_NO_REF/1000,3),'kJ·mol⁻¹'),metric('Chaleur cédée par mole',round(-p['loss']*(H_NO_REF-7.5*(p['initial']-298))/1000,3),'kJ')],
      [chart('Effet de la dilution','Inerte par mole initiale de NO (mol)','Température finale (K)',series('Bilan retenu',dilution,tf))],
      _curve('Bilan d’enthalpie au cours d’une conversion imposée',x,[('Avec les pertes',actual),('Adiabatique',ideal)],'Avancement ξ (mol)','Température (K)',description='Les courbes comparent la température pendant une conversion imposée de 0 à 1 mol, avec ou sans chaleur cédée. Les Cp sont constants ; l’équilibre de dissociation n’est pas calculé.'),
      ['Le mélange initial contient 1 mol de NO et 0,5 mol de O₂. Après ξ : n(NO)=1−ξ, n(O₂)=(1−ξ)/2, n(NO₂)=ξ.',
       'ΔrCp°=36−29−29/2=−7,5 J·mol⁻¹·K⁻¹. Kirchhoff donne ΔrH°(Tᵢ).',
       'À pression constante : Cp,total(ξ)(T−Tᵢ)=−(1−f)ξΔrH°(Tᵢ). Le bilan du recueil à 93 % de perte calibre ΔrH°(298 K).'],
      ['Chaleurs molaires constantes : 29 pour NO, O₂ et inerte ; 36 pour NO₂, en J·mol⁻¹·K⁻¹.',
       'Conversion totale imposée ; dissociation de NO₂ et dépendance réelle des Cp exclues. Les températures élevées sont des résultats du modèle, pas une prédiction de réacteur.',
       'La fraction de perte f est une donnée de bilan ; elle ne résout pas une loi de transfert thermique.'],
      table('Quantités et capacité thermique',['Espèce','Initial (mol)','Final (mol)','Cp (J·mol⁻¹·K⁻¹)'],[['NO',1,0,29],['O₂',.5,0,29],['NO₂',0,1,36],['Inerte',p['inert'],p['inert'],29]]))

def thermo_k(T,H,S,Cp=0):
    """ln K for H298,S298 and a constant reaction heat capacity (SI)."""
    T=np.asarray(T,dtype=float); ht=H+Cp*(T-298.15); st=S+Cp*np.log(T/298.15)
    return -(ht-T*st)/(R*T)

def ammonia_equilibrium(T,P,inert=0):
    T,P=np.broadcast_arrays(np.asarray(T,dtype=float),np.asarray(P,dtype=float))
    target=thermo_k(T,-92220,-198.1,-45)
    lo=np.full(T.shape,1e-13); hi=np.full(T.shape,1-1e-13)
    for _ in range(62):
        x=(lo+hi)/2; total=4-2*x+inert
        logq=2*np.log(2*x)-4*np.log(1-x)-3*np.log(3)+2*np.log(total)-2*np.log(P)
        smaller=logq<target; lo=np.where(smaller,x,lo); hi=np.where(smaller,hi,x)
    return (lo+hi)/2

def haber_bosch(p):
    T=p['temperature']; P=p['pressure']; inert=p['inert']; x=float(ammonia_equilibrium(T,P,inert))
    tt=np.linspace(450,900,64); pp=np.linspace(1,250,55)
    xx=ammonia_equilibrium(tt[None,:],pp[:,None],inert)
    sc=field_scene('Carte de conversion d’équilibre',tt,pp,100*xx,levels=[],
        points=[dict(x=T,y=P,label=f'Conversion {100*x:.1f} %',group=0)],description='La carte montre l’équilibre des gaz parfaits. Elle ne donne ni vitesse, ni conversion industrielle par passage.')
    sc.update(xLabel='Température T (K)',yLabel='Pression P (bar)',valueLabel='Conversion de N₂ (%)')
    tempcurve=ammonia_equilibrium(tt,P,inert); pressurecurve=ammonia_equilibrium(T,pp,inert)
    return result([metric('Conversion de N₂',round(100*x,2),'%'),metric('NH₃ formé',round(2*x,4),'mol'),metric('ln K°',round(float(thermo_k(T,-92220,-198.1,-45)),3)),metric('Gaz en sortie',round(4-2*x+inert,4),'mol')],
      [chart('Température à pression fixée','T (K)','Conversion (%)',series(f'P={P:g} bar',tt,100*tempcurve)),chart('Pression à température fixée','P (bar)','Conversion (%)',series(f'T={T:g} K',pp,100*pressurecurve))],sc,
      ['État final : (1−ξ)N₂, 3(1−ξ)H₂ et 2ξ NH₃ ; le total est 4−2ξ+nᵢ.',
       'Pour chaque gaz aᵢ=yᵢP/p°. Former Q=aNH₃²/(aN₂aH₂³), puis résoudre ln Q=ln K°.',
       'La constante est calculée avec ΔrH°298=−92,22 kJ·mol⁻¹, ΔrS°298=−198,1 J·mol⁻¹·K⁻¹ et ΔrCp°=−45 J·mol⁻¹·K⁻¹ constants.'],
      ['Charge initiale stœchiométrique : 1 mol N₂, 3 mol H₂, nᵢ mol d’inerte ; pas de NH₃ initial.',
       'Approximation pédagogique des Cp et gaz parfaits ; fugacités nécessaires à une prévision quantitative sous forte pression.',
       'Le catalyseur change la vitesse, pas K°. Aucun temps de séjour n’est calculé.'],
      table('Bilan molaire exact du modèle',['Gaz','Initial (mol)','Équilibre (mol)'],[['N₂',1,round(1-x,7)],['H₂',3,round(3*(1-x),7)],['NH₃',0,round(2*x,7)],['Inerte',inert,inert]]))

def methanol_equilibrium(T,P,ratio):
    T,P=np.broadcast_arrays(np.asarray(T,dtype=float),np.asarray(P,dtype=float))
    target=thermo_k(T,-49500,-177,-28)
    xmax=min(1,ratio/3); lo=np.full(T.shape,1e-13); hi=np.full(T.shape,xmax*(1-1e-13))
    for _ in range(62):
        x=(lo+hi)/2; total=1+ratio-2*x
        logq=2*np.log(x)-np.log(1-x)-3*np.log(ratio-3*x)+2*np.log(total)-2*np.log(P)
        smaller=logq<target; lo=np.where(smaller,x,lo); hi=np.where(smaller,hi,x)
    return (lo+hi)/2

def methanol_co2(p):
    T=p['temperature']; P=p['pressure']; ratio=p['ratio']; recycle=p['recycle']
    x=float(methanol_equilibrium(T,P,ratio)); rr=np.linspace(0,.95,96)
    overall=x/(1-rr*(1-x)); total=x/(1-recycle*(1-x)); circulation=1/(1-recycle*(1-x))
    tt=np.linspace(450,650,64); pr=np.linspace(5,100,55); xx=methanol_equilibrium(tt[None,:],pr[:,None],ratio)
    sc=field_scene('Conversion par passage : CO₂ vers méthanol',tt,pr,100*xx,levels=[],points=[dict(x=T,y=P,label=f'Passage : {100*x:.1f} %',group=0)],description='Équilibre d’une seule réaction en phase gazeuse, avec le rapport H₂/CO₂ réglé.')
    sc.update(xLabel='T (K)',yLabel='P (bar)',valueLabel='Conversion par passage (%)')
    return result([metric('CO₂ converti par passage',round(100*x,2),'%'),metric('Conversion globale avec recyclage',round(100*total,2),'%'),metric('CO₂ circulant / CO₂ frais',round(circulation,3)),metric('CH₃OH par mole de CO₂ frais',round(total,4),'mol')],
      [chart('Recyclage idéal et conversion globale','Fraction recyclée r','Conversion (%)',series('x/[1−r(1−x)]',rr,100*overall)),chart('Besoin de circulation','Fraction recyclée r','Débit circulant / débit frais',series('Réactif circulant',rr,1/(1-rr*(1-x))))],sc,
      ['Pour 1 mol CO₂ initial : CO₂=1−ξ, H₂=h−3ξ, CH₃OH=ξ, H₂O=ξ ; 0<ξ<min(1,h/3).',
       'Les activités gazeuses sont yᵢP/p°. Résoudre ln Q=ln K° avec ΔH°298=−49,5 kJ·mol⁻¹, ΔS°298=−177 J·mol⁻¹·K⁻¹, ΔCp°=−28 J·mol⁻¹·K⁻¹.',
       'Pour le module de recyclage, x est la conversion d’un passage maintenue identique par réglage du rapport d’alimentation. Bilan stationnaire : Fcirculant=Ffrais+r(1−x)Fcirculant.'],
      ['Une réaction gazeuse, gaz parfaits et Cp constants ; équilibre CO/CO₂ et condensation exclus.',
       'Recyclage : séparation totale des produits, purge de la fraction 1−r et maintien du rapport H₂/CO₂ à l’entrée. Le bilan affiché concerne le carbone ; un appoint d’H₂ peut être nécessaire.',
       'Ni énergie de compression, ni origine de H₂, ni analyse de cycle de vie : la conversion seule ne prouve pas un bénéfice climatique.'],
      table('Un passage, pour une mole initiale de CO₂',['Espèce','Quantité finale (mol)'],[['CO₂',round(1-x,6)],['H₂',round(ratio-3*x,6)],['CH₃OH',round(x,6)],['H₂O',round(x,6)]]))

def zinc_gibbs(T):
    T=np.asarray(T,dtype=float)
    hz=np.where(T<=693,0,np.where(T<=1180,6.7,121.5))
    sz=.0416+np.where(T<=693,0,6.7/693)+np.where(T<=1180,0,114.8/1180)
    # Formation normalized to one mole of O2, as in the source TP.
    return 2*(-350.5-hz)-T*(2*.0436-.205-2*sz)

def ellingham_zinc(p):
    ts=np.unique(np.r_[np.linspace(400,1800,211),693,1180]); gz=zinc_gibbs(ts)
    gc=-221-ts*(2*.1976-2*.0057-.205)
    gco=-566-ts*(2*.2136-2*.1976-.205)
    dgC=(gc-gz)/2; dgCO=(gco-gz)/2; correction=R*ts*math.log(10)*p['logq']/1000
    T=p['temperature']; G=float(zinc_gibbs(T)); a=float(np.interp(T,ts,dgC+correction)); b=float(np.interp(T,ts,dgCO+correction))
    phase='solide' if T<=693 else ('liquide' if T<=1180 else 'gazeux')
    return result([metric('État stable du zinc',phase),metric('ΔrG avec C',round(a,2),'kJ·mol⁻¹ Zn'),metric('ΔrG avec CO',round(b,2),'kJ·mol⁻¹ Zn'),metric('Sens thermodynamique avec C','réduction favorisée' if a<0 else 'réduction défavorisée')],
      [chart('Deux réactions de réduction','T (K)','ΔrG (kJ·mol⁻¹ Zn)',series('ZnO+C→Zn+CO',ts,dgC+correction),series('ZnO+CO→Zn+CO₂',ts,dgCO+correction),series('Seuil ΔrG=0',ts,np.zeros_like(ts)))],
      _curve('Diagramme d’Ellingham : même normalisation',ts,[('2Zn+O₂→2ZnO',gz),('2C+O₂→2CO',gc),('2CO+O₂→2CO₂',gco)],'T (K)','ΔrG° (kJ·mol⁻¹ O₂)',description='Toutes les réactions de cette scène consomment une mole de O₂. Les ruptures du zinc sont continues aux températures de changement d’état.'),
      ['Construire G°Zn(T) avec H°Zn et S°Zn du tableau du TP. Ajouter ΔHfusion puis ΔHvaporisation à H, et ΔH/Ttransition à S.',
       'Soustraire la formation de ZnO de celle de CO ou de CO₂, puis diviser par deux : les réactions de réduction produisent une mole de zinc.',
       'Ajouter RT ln Q, où Q est le quotient des pressions partielles réduites : pour le zinc gazeux, aZn intervient aussi. ΔrG<0 favorise le sens écrit.'],
      ['Données du TP page 564 ; ZnO est le solide dans les réactions. ΔCp négligés, graphite et oxydes purs.',
       'Les changements d’état du zinc sont imposés à 693 K et 1180 K sous pression de référence ; log Q est un réglage thermodynamique indépendant.',
       'Ni cinétique, ni transport, ni dépression du point d’ébullition ; la favorabilité n’est pas une garantie de vitesse ou de rendement.'],
      table('Transitions du zinc',['Transition','T (K)','ΔH (kJ·mol⁻¹)','ΔS (J·mol⁻¹·K⁻¹)'],[['Fusion',693,6.7,round(6700/693,3)],['Vaporisation',1180,114.8,round(114800/1180,3)],['État retenu',T,phase,'']]))

def calcination_ciment(p):
    T=p['temperature']; pressure=p['pco2']; H=178300.; S=160.6
    ts=np.linspace(850,1400,181); pp=np.geomspace(.01,1,55)
    g=H-ts*S; corrected=g+R*ts*math.log(pressure)
    boundary=H/(S-R*math.log(pressure)); n=p['mass']/100.086 # kg / kg/kmol -> kmol.
    co2=n*44.01; energy=n*H/1000; captured=p['capture']*co2
    sc=field_scene('Calcination : signe de ΔrG',ts,pp,(H-ts[None,:]*S+R*ts[None,:]*np.log(pp[:,None]))/1000,levels=[0],points=[dict(x=T,y=pressure,label='Condition choisie',group=0)],description='ΔrG<0 favorise CaCO₃→CaO+CO₂ lorsque les deux solides purs sont présents.')
    sc.update(xLabel='T (K)',yLabel='pCO₂ (bar)',valueLabel='ΔrG (kJ/mol)')
    return result([metric('ΔrG aux conditions choisies',round((H-T*S+R*T*math.log(pressure))/1000,3),'kJ·mol⁻¹'),metric('Température d’équilibre du modèle',round(boundary,1),'K'),metric('CO₂ stœchiométrique',round(co2,2),'kg'),metric('Chaleur réactionnelle',round(energy,2),'MJ')],
      [chart('Effet du CO₂ sur la calcination','T (K)','ΔrG (kJ·mol⁻¹)',series('pCO₂=1 bar',ts,g/1000),series(f'pCO₂={pressure:g} bar',ts,corrected/1000))],sc,
      ['CaCO₃(s)→CaO(s)+CO₂(g). Les solides purs ont activité 1 ; Q=pCO₂/p°.',
       'Avec ΔH°=178,3 kJ·mol⁻¹ et ΔS°=160,6 J·mol⁻¹·K⁻¹ constants : ΔG=ΔH°−TΔS°+RT ln Q.',
       'Le bilan massique de conversion complète est une borne stœchiométrique indépendante du signe de ΔG affiché. Capturer CO₂ ne change pas le nombre de moles formées.'],
      ['Approximation d’Ellingham avec valeurs arrondies ; ce n’est pas une base de propriétés à haute température.',
       'Le bilan complet est affiché comme objectif théorique, même si la calcination n’est pas favorisée aux conditions retenues.',
       'Chauffage des matières, réactions du clinker, énergie du captage et émissions du combustible exclus.'],
      table('Bilan à conversion complète',['Flux','Masse (kg)'],[['CaCO₃ entrant',p['mass']],['CaO formé',round(n*56.076,3)],['CO₂ formé',round(co2,3)],['CO₂ capturé',round(captured,3)],['CO₂ résiduel',round(co2-captured,3)]]))

def flash_ideal(z,P,relative):
    pa=.5; pb=pa*relative; bubble=pa+(pb-pa)*z; dew=1/((1-z)/pa+z/pb)
    if P>=bubble: return z,None,0.,'liquide'
    if P<=dew: return None,z,1.,'vapeur'
    xl=(P-pa)/(pb-pa); yv=pb*xl/P; beta=(z-xl)/(yv-xl)
    return xl,yv,beta,'liquide + vapeur'

def distillation_ideale(p):
    z=p['z']; P=p['pressure']; relative=p['relative']; xl,yv,beta,phase=flash_ideal(z,P,relative)
    x=np.linspace(0,1,151); pa=.5; pb=pa*relative
    bubble=pa+(pb-pa)*x; dew=1/((1-x)/pa+x/pb)
    paths=[dict(label='Ébullition : xL',x=x,y=bubble),dict(label='Rosée : yV',x=x,y=dew)]
    if xl is not None and yv is not None: paths.append(dict(label='Ligne d’équilibre',x=[xl,yv],y=[P,P]))
    sc=plane_scene('Fuseau isotherme et règle du levier',paths=paths,points=[dict(x=z,y=P,label=f'Composition globale : {phase}',group=0)],bounds=[0,1,.15,max(2.2,pb+.2)],xlabel='Fraction molaire de B',ylabel='P (bar)',description='Les deux courbes sont issues de Raoult et du bilan de vapeur idéale. Le segment horizontal relie les compositions coexistantes.')
    sc['equalAspect']=False
    m=metric
    return result([m('Phase',phase),m('Fraction vapeur',round(beta,5)),m('Composition liquide xL','—' if xl is None else round(xl,5)),m('Composition vapeur yV','—' if yv is None else round(yv,5))],
      [chart('Enrichissement de la vapeur en B','xL','yV',series('yV=αxL/[1+(α−1)xL]',x,relative*x/(1+(relative-1)*x)),series('yV=xL',x,x))],sc,
      ['Pressions de vapeur imposées à la température fixée : p*A=0,5 bar et p*B=αp*A ; α>1.',
       'Ébullition : P=(1−xL)p*A+xLp*B ; équilibre : yV=xLp*B/P. Rosée : 1/P=(1−yV)/p*A+yV/p*B.',
       'Si deux phases coexistent, z=(1−β)xL+βyV, d’où β=(z−xL)/(yV−xL). En phase unique, sa composition vaut z.'],
      ['Solution liquide idéale, gaz parfaits, température fixée et pressions de vapeur constantes.',
       'Aucun azéotrope ; A et B sont des constituants didactiques, pas un mélange réel identifié.',
       'La figure illustre un étage d’équilibre ; une colonne réelle exige des bilans d’énergie et de débit.'],
      table('Bilan pour une mole globale',['Phase','Quantité (mol)','Fraction de B'],[['Liquide',round(1-beta,6),'—' if xl is None else round(xl,6)],['Vapeur',round(beta,6),'—' if yv is None else round(yv,6)],['Global',1,z]]))

def alloy_compositions(T):
    T=np.asarray(T,dtype=float)
    ka=np.exp(-13050*(1-T/1358)/(R*T)); kb=np.exp(-17480*(1-T/1728)/(R*T))
    xs=(1-ka)/(kb-ka); xl=kb*xs
    return xl,xs

def alloy_state(T,z):
    if T<=1358: return None,z,1.,'solide'
    if T>=1728: return z,None,0.,'liquide'
    xl,xs=map(float,alloy_compositions(T))
    if z<=xl: return z,None,0.,'liquide'
    if z>=xs: return None,z,1.,'solide'
    fs=(z-xl)/(xs-xl)
    return xl,xs,fs,'liquide + solide'

def alliage_solidification(p):
    T=p['temperature']; z=p['z']; xl,xs,fs,phase=alloy_state(T,z)
    tt=np.linspace(1358,1728,161); liquid,solid=alloy_compositions(tt)
    path=[dict(label='Liquidus',x=liquid,y=tt),dict(label='Solidus',x=solid,y=tt)]
    if phase=='liquide + solide': path.append(dict(label='Équilibre à T',x=[xl,xs],y=[T,T]))
    sc=plane_scene('Diagramme idéal : liquidus et solidus',paths=path,points=[dict(x=z,y=T,label=f'Alliage : {phase}',group=0)],bounds=[0,1,1300,1800],xlabel='Fraction molaire de B',ylabel='T (K)',description='Les courbes sont calculées par égalité des potentiels chimiques de chaque constituant dans le liquide et le solide.')
    sc['equalAspect']=False
    temps=np.linspace(1300,1800,151); fractions=[alloy_state(float(t),z)[2] for t in temps]
    return result([metric('Phase',phase),metric('Fraction solide',round(fs,5)),metric('Composition liquide','—' if xl is None else round(xl,5)),metric('Composition solide','—' if xs is None else round(xs,5))],
      [chart('Refroidissement à composition globale fixée','T (K)','Fraction solide',series('Règle du levier',temps,fractions))],sc,
      ['Données du modèle : Tf,A=1358 K, Tf,B=1728 K, ΔHfus,A=13,05 kJ·mol⁻¹ et ΔHfus,B=17,48 kJ·mol⁻¹.',
       'Égalité µi,L=µi,S : xi,L/xi,S=exp[−ΔHfus,i(1−T/Tf,i)/(RT)]. Combiner les deux égalités avec la somme des fractions égale à 1.',
       'Dans le fuseau : z=(1−fS)xL+fSxS. La fraction solide est (z−xL)/(xS−xL), comprise entre 0 et 1.'],
      ['Modèle de solution idéale dans les deux phases, Cp négligés et pression fixée ; paramètres proches de Cu–Ni, sans ajustement à un diagramme expérimental.',
       'Aucun composé défini, eutectique, diffusion limitée ou surfusion. Le Mg–Ni du recueil comporte des domaines supplémentaires.',
       'La fraction solide est une fraction molaire, pas une fraction massique.'],
      table('Bilan pour une mole d’alliage',['Phase','Quantité (mol)','Fraction de B'],[['Liquide',round(1-fs,6),'—' if xl is None else round(xl,6)],['Solide',round(fs,6),'—' if xs is None else round(xs,6)],['Global',1,z]]))

CALCULATORS={name:globals()[name] for name in ('hess_combustion','temperature_adiabatique','haber_bosch','methanol_co2','ellingham_zinc','calcination_ciment','distillation_ideale','alliage_solidification')}
