"""Bilans électroniques et lois électrochimiques explicitement bornées."""
import math
import numpy as np
from commun import metric,chart,series,result,table,curve_scene,plane_scene,field_scene,integrate
R=8.31446261815324
F=96485.33212
TREF=298.15

def _curve(title,x,curves,xlabel,ylabel,description=''):
    return curve_scene(title,x,curves,xlabel,ylabel,description)

def nernst_pile(p):
    T=p['temperature']; logq=p['logzn']-p['logcu']; slope=R*T*math.log(10)/(2*F)
    E0=.340-(-.763); E=E0-slope*logq; amount=p['amount']; charge=2*F*amount
    qq=np.linspace(-12,12,181); volts=E0-slope*qq; logk=2*F*E0/(R*T*math.log(10))
    copper=np.linspace(-5,0,61); zinc=np.linspace(-5,0,61)
    sc=field_scene('Tension Daniell : activités des deux ions',copper,zinc,E0-slope*(zinc[:,None]-copper[None,:]),levels=[],points=[dict(x=p['logcu'],y=p['logzn'],label=f'E={E:.3f} V',group=0)],description='Chaque point correspond à deux concentrations, pas à un temps de décharge.')
    sc.update(xLabel='log₁₀ aCu²⁺',yLabel='log₁₀ aZn²⁺',valueLabel='Tension E (V)')
    return result([metric('Tension réversible E',round(E,5),'V'),metric('ΔrG',round(-2*F*E/1000,3),'kJ·mol⁻¹'),metric('Charge transférée',round(charge,3),'C'),metric('log₁₀ K°',round(logk,3))],
      [chart('Nernst : pente et sens spontané','log₁₀ Q','E (V)',series('E°−RT ln Q/(2F)',qq,volts))],sc,
      ['Anode : Zn→Zn²⁺+2e⁻ ; cathode : Cu²⁺+2e⁻→Cu. Le bilan est Zn+Cu²⁺→Zn²⁺+Cu.',
       'Avec solides purs : Q=aZn²⁺/aCu²⁺. Pour deux électrons, E=1,103−(RT/2F)ln Q.',
       'Le bilan de charge q=2FnCu est exact pour cette réaction. Le travail électrique réversible par mole vaut 2FE ; une tension maintenue fixe est nécessaire pour multiplier E par q sur une décharge.'],
      ['Activités assimilées à c/c°, c°=1 mol·L⁻¹ ; potentiel de jonction, résistance et transfert de charge exclus.',
       'E° arrondi et considéré constant entre 278 et 348 K ; seule la pente de Nernst varie avec T.',
       'Le réglage de quantité donne une charge, pas une capacité disponible : volumes et quantités initiales ne sont pas imposés.'],
      table('Données et bilan',['Grandeur','Valeur','Unité'],[['E°Cu²⁺/Cu',.340,'V'],['E°Zn²⁺/Zn',-.763,'V'],['n électrons par réaction',2,''],['aCu²⁺',10**p['logcu'],''],['aZn²⁺',10**p['logzn'],''],['Cu déposé',round(amount*63.546,4),'g']]))

def electrolyse_h2(p):
    I=p['current']; time=p['hours']*3600; U=p['voltage']; eta=p['faraday']
    Erev=237130/(2*F); Etn=285830/(2*F)
    charge=I*time; n=eta*charge/(2*F); mass=n*.002016
    energy=charge*U/3.6e6; chemical=n*285830/3.6e6; heat=energy-chemical
    vv=np.linspace(1.3,2.4,111); specific=2*F*vv/(eta*.002016*3.6e6)
    hours=np.linspace(0,12,121); masses=eta*I*hours*3600/(2*F)*.002016
    return result([metric('H₂ produit',round(mass,5),'kg'),metric('Électricité consommée',round(energy,5),'kWh'),metric('Consommation spécifique',round(energy/mass,3),'kWh·kg⁻¹ H₂'),metric('Chaleur nette à évacuer',round(heat,5),'kWh')],
      [chart('Tension et consommation spécifique','U (V)','Électricité (kWh·kg⁻¹)',series('À ηF fixé',vv,specific)),chart('Production et durée','Durée (h)','H₂ (kg)',series('Faraday',hours,masses))],
      _curve('Énergie électrique et chaleur de l’électrolyse',vv,[('Électricité',2*F*vv/eta/1000),('Enthalpie du H₂ produit',np.full_like(vv,285.830)),('Chaleur nette',2*F*vv/eta/1000-285.830)],'U (V)','Énergie par mole de H₂ (kJ)',description='Pour une mole de H₂ à 298 K, comparer l’électricité fournie et l’enthalpie des produits. Une chaleur nette négative désigne de la chaleur à apporter ; les auxiliaires sont exclus.'),
      ['L’eau donne H₂+½O₂ ; deux électrons sont nécessaires par mol de H₂. nH₂=ηF IΔt/(2F).',
       'Énergie électrique WI=UIΔt. À 298 K, ΔG°=237,13 kJ·mol⁻¹ donne Erev≈1,229 V ; ΔH°=285,83 kJ·mol⁻¹ donne Etn≈1,481 V.',
       'Bilan thermique stationnaire ramené à la durée : chaleur évacuée=WI−nH₂ΔH°. Un résultat négatif signifie que le procédé doit recevoir de la chaleur.'],
      ['Une cellule à 298 K, eau liquide et gaz standard ; volumes de gaz, compression, alimentation et auxiliaires exclus.',
       'ηF est la fraction de charge qui produit H₂ ; les courants parasites sont traités comme pertes dissipatives.',
       'ηPCS=ηF Etn/U peut dépasser 1 lorsque de la chaleur est importée : ce quotient n’est pas le rendement total incluant toutes les entrées.'],
      table('Deux tensions et un rendement',['Grandeur','Valeur','Unité'],[['Charge q',round(charge,3),'C'],['n(H₂)',round(n,6),'mol'],['n(O₂)',round(n/2,6),'mol'],['Erev',round(Erev,5),'V'],['Etn',round(Etn,5),'V'],['ηPCS électrique',round(eta*Etn/U,5),'']]))

def fuel_voltage(j,resistance,exchange,limit):
    j=np.asarray(j,dtype=float)
    activation=.06*np.arcsinh(j/(2*exchange))
    transport=-R*TREF/(2*F)*np.log1p(-j/limit)
    ohmic=resistance*j
    raw=237130/(2*F)-activation-ohmic-transport
    return raw,activation,ohmic,transport

def pile_combustible(p):
    jj=np.linspace(0,.98*p['limit'],231); raw,act,ohm,trans=fuel_voltage(jj,p['resistance'],p['exchange'],p['limit'])
    volts=np.maximum(raw,0); power=jj*volts; imax=int(np.argmax(power)); chosen=float(p['density'])
    v,_,_,_=fuel_voltage(chosen,p['resistance'],p['exchange'],p['limit']); v=max(float(v),0)
    Etn=285830/(2*F); efficiency=v/Etn
    return result([metric('Tension utile',round(v,4),'V'),metric('Puissance surfacique choisie',round(chosen*v,4),'W·cm⁻²'),metric('Maximum sur la grille',round(float(power[imax]),4),'W·cm⁻²'),metric('Rendement électrique PCS',round(100*efficiency,2),'%')],
      [chart('Puissance et point de fonctionnement','j (A·cm⁻²)','P/S (W·cm⁻²)',series('jU(j)',jj,power)),chart('Décomposition des pertes','j (A·cm⁻²)','Surtension (V)',series('Activation',jj,act),series('Ohmique',jj,ohm),series('Transport',jj,trans))],
      _curve('Polarisation d’une pile H₂/O₂',jj,[('Tension positive',volts),('Réversible',np.full_like(jj,237130/(2*F)))],'j (A·cm⁻²)','U (V)',description='La tension diminue lorsque la densité de courant augmente, sous l’effet des pertes d’activation, ohmiques et de transport. La courbe didactique est arrêtée à zéro ; les points de tension négative ne produisent pas d’électricité en pile.'),
      ['Bilan : H₂+½O₂→H₂O(l). La tension réversible du modèle vaut ΔG°/(2F).',
       'U=Erev−b asinh[j/(2j₀)]−rj+(RT/2F)ln(1−j/jlim), avec b=0,060 V, r en Ω·cm² et tous les j en A·cm⁻².',
       'Puissance surfacique : jU. Le rendement sur PCS vaut U/Etn à rendement faradique 1 ; il diminue avec j, même si la puissance augmente d’abord.'],
      ['Courbe didactique isotherme à 298 K ; paramètres globaux, sans identification à une cellule commerciale.',
       'La loi n’est évaluée que pour j<jlim. Si U≤0, le point ne peut pas délivrer de puissance en pile : la courbe est arrêtée à zéro.',
       'Maximum évalué sur 231 points, pas une preuve de maximum continu ; auxiliaires et consommation d’air exclus.'],
      table('Point de puissance le plus élevé sur la grille',['Grandeur','Valeur','Unité'],[['j*',round(float(jj[imax]),5),'A·cm⁻²'],['U(j*)',round(float(volts[imax]),5),'V'],['ηPCS(j*)',round(float(volts[imax])/Etn,5),''],['H₂ consommé au point choisi',round(chosen/(2*F)*3600*1000,5),'mmol·h⁻¹·cm⁻²']]))

def battery_ocv(s):
    s=np.asarray(s,dtype=float)
    # Ideal-site regularization keeps each electrode occupancy away from 0 and 1.
    a=.05+.9*s; c=1-a
    return 3.4+R*TREF/F*(np.log(a/(1-a))-np.log(c/(1-c)))

def batterie_intercalation(p):
    ss=np.linspace(.05,.95,181); ocv=battery_ocv(ss); voltage=ocv-p['current']*p['resistance']
    s=p['soc']; voc=float(battery_ocv(s)); v=voc-p['current']*p['resistance']
    active=ss<=s; energy=p['capacity']*float(integrate(voltage[active],ss[active])) if sum(active)>1 else 0.
    # Integral restricted to displayed 5% stop and selected initial SOC.
    segment=np.linspace(.05,s,121) if s>.05 else np.array([.05,.05])
    energy=p['capacity']*float(integrate(battery_ocv(segment)-p['current']*p['resistance'],segment))
    occupied=.05+.9*ss
    return result([metric('Tension à vide',round(voc,5),'V'),metric('Tension sous décharge',round(v,5),'V'),metric('Charge jusqu’à s=5 %',round(p['capacity']*(s-.05),4),'Ah'),metric('Énergie jusqu’à s=5 %',round(energy,4),'Wh')],
      [chart('Charge et tension : modèle de sites idéaux','État de charge s','U (V)',series('À vide',ss,ocv),series('Sous décharge',ss,voltage)),chart('Répartition des sites','État de charge s','Fraction occupée',series('Électrode négative',ss,occupied),series('Électrode positive',ss,1-occupied))],
      _curve('Sites d’intercalation : transfert de lithium',ss,[('Électrode négative',occupied),('Électrode positive',1-occupied)],'État de charge s','Fraction occupée',description='Chaque fraction reste entre 0,05 et 0,95 ; la somme vaut 1 dans ce modèle symétrique.'),
      ['Occupation des sites : θ−=0,05+0,90s et θ+=1−θ−. La somme des occupations est conservée lors du transfert.',
       'Modèle idéal : µLi=µ°+RT ln[θ/(1−θ)]. La différence entre électrodes donne Uoc=3,4+(RT/F){ln[θ−/(1−θ−)]−ln[θ+/(1−θ+)]}.',
       'Sous décharge : U=Uoc−rI. Une baisse ds délivre la charge C ds en Ah ; énergie W=C∫U(s)ds en Wh, jusqu’au seuil choisi s=0,05.'],
      ['Deux électrodes symétriques de sites idéaux ; aucun plateau de coexistence de phases, hystérésis, vieillissement ou limite de puissance.',
       'C est la capacité associée à l’intervalle s∈[0,1] ; seul l’intervalle 5–95 % est utilisé ici.',
       'La tension de référence 3,4 V est illustrative. Les courbes ne décrivent pas une chimie de batterie commerciale.'],
      table('Bilan au point choisi',['Grandeur','Valeur','Unité'],[['θ−',round(.05+.9*s,6),''],['θ+',round(.95-.9*s,6),''],['Perte ohmique',round(p['current']*p['resistance'],5),'V'],['Puissance choisie',round(p['current']*v,4),'W'],['Chaleur Joule',round(p['current']**2*p['resistance'],4),'W']]))

def corrosion_currents(E,jlim,area,logfe):
    E=np.asarray(E,dtype=float)
    efe=-.440+R*TREF*math.log(10)/(2*F)*logfe
    ezn=-.763+R*TREF*math.log(10)/(2*F)*(-5)
    # Full anodic/cathodic BV contributions, in mA/cm² metal area.
    fe=.00005*2*np.sinh(np.clip((E-efe)/.052,-40,40))
    zn=.00010*2*np.sinh(np.clip((E-ezn)/.052,-40,40))
    # Cathodic oxygen current, activation + diffusion in series.
    oxygen_kin=.00002*np.exp(np.clip((.41-E)/.12,-40,40))
    oxygen=-jlim*oxygen_kin/(jlim+oxygen_kin)
    return fe,zn,oxygen,fe+area*zn+oxygen

def corrosion_mixed(jlim,area,logfe):
    lo=-1.1; hi=.4
    for _ in range(70):
        mid=(lo+hi)/2; total=float(corrosion_currents(mid,jlim,area,logfe)[3])
        if total<0: lo=mid
        else: hi=mid
    E=(lo+hi)/2
    fe,zn,oxygen,_=corrosion_currents(E,jlim,area,logfe)
    return E,float(fe),float(zn),float(oxygen)

def corrosion_protection(p):
    jlim=p['oxygen']; area=p['zinc']; logfe=p['logfe']; E,fe,zn,oxy=corrosion_mixed(jlim,area,logfe)
    E0,fe0,_,_=corrosion_mixed(jlim,0,logfe)
    ee=np.linspace(-1.05,.05,211); a,b,c,total=corrosion_currents(ee,jlim,area,logfe)
    # Show partial current near realistic corrosion window, not huge exponential tails.
    window=np.linspace(E-.18,E+.18,181); a,b,c,total=corrosion_currents(window,jlim,area,logfe)
    surface=np.linspace(0,5,101); states=[corrosion_mixed(jlim,float(s),logfe) for s in surface]
    potentials=[s[0] for s in states]; rates=[max(s[1],0) for s in states]
    # Fe metal loss at 2e per atom; 1 mA/cm² -> 10 A/m².
    penetration=max(fe,0)*10*55.845e-3/(2*F*7874)*3600*24*365*1000
    return result([metric('Potentiel mixte',round(E,5),'V'),metric('Dissolution nette du fer',round(max(fe,0),7),'mA·cm⁻²'),metric('Perte uniforme de fer',round(penetration,5),'mm·an⁻¹'),metric('Facteur de protection',round(fe0/max(fe,1e-12),2) if fe>0 else 'fer cathodique')],
      [chart('Courants : somme nulle au potentiel mixte','E (V)','j ramené à la surface du fer (mA·cm⁻²)',series('Fer',window,a),series('Zinc × surface relative',window,area*b),series('Oxygène',window,c),series('Somme',window,total)),chart('Effet de la surface de zinc','Surface Zn / surface Fe','E mixte (V)',series('Potentiel',surface,potentials))],
      _curve('Protection : diminuer la dissolution du fer',surface,[('Courant de dissolution du fer',rates)],'Surface Zn / surface Fe','jFe positif (mA·cm⁻²)',description='Augmenter la surface du zinc sacrificiel réduit le courant net de dissolution du fer dans ce modèle de potentiel mixte. Le courant limite d’oxygène est fixé ; la passivation et la durée de vie du revêtement sont exclues.'),
      ['Les potentiels d’équilibre de Fe et Zn viennent de Nernst. La réduction d’O₂ à pH 7 est représentée par une branche cathodique limitée par le transport.',
       'Chaque métal suit j=2j₀ sinh[(E−Eeq)/b] avec b=0,052 V. La contribution du zinc est multipliée par son rapport de surface.',
       'Au circuit ouvert du couple connecté : jFe+SZn/SFe·jZn+jO₂=0. Résoudre cette égalité ; seule la partie positive de jFe représente une perte de fer.'],
      ['Paramètres cinétiques illustratifs ; pas de passivation, piqûres, résistance d’électrolyte ou vieillissement du revêtement.',
       'Oxygène réduit sur la surface du fer ; la surface de zinc n’ajoute ici que son courant métallique. La limitation de transport est stationnaire.',
       'Perte uniforme avec Fe→Fe²⁺+2e⁻ et densité 7874 kg·m⁻³ ; la durée de vie du zinc exige un bilan séparé.'],
      table('Vérification de la conservation du courant',['Contribution au point mixte','Valeur','Unité'],[['jFe',round(fe,9),'mA·cm⁻² Fe'],['a·jZn',round(area*zn,9),'mA·cm⁻² Fe'],['jO₂',round(oxy,9),'mA·cm⁻² Fe'],['Somme',round(fe+area*zn+oxy,12),'mA·cm⁻² Fe'],['Fer seul : E',round(E0,6),'V']]))

def deposition_data(I,minutes,area,concentration,layer):
    # D=7e-10 m²/s ; area cm² -> m², c mol/L -> mol/m³, delta µm -> m.
    limiting=2*F*7e-10*(concentration*1000)/(layer*1e-6)*(area*1e-4)
    effective=min(I,limiting); n=effective*minutes*60/(2*F); mass=n*63.546
    thickness=mass/8.96/area*1e4 # g/(g/cm³)/cm² -> cm -> µm.
    return limiting,effective,n,mass,thickness

def electrodepot(p):
    vals=deposition_data(p['current'],p['minutes'],p['area'],p['concentration'],p['layer'])
    limit,effective,n,mass,thickness=vals
    currents=np.linspace(.05,20,181); deposited=np.minimum(currents,limit)*p['minutes']*60/(2*F)*63.546/8.96/p['area']*1e4
    times=np.linspace(0,120,121); growth=effective*times*60/(2*F)*63.546/8.96/p['area']*1e4
    delta=p['layer']; distances=np.linspace(0,delta,101); c=p['concentration']*(1-(effective/limit)*(1-distances/delta))
    return result([metric('Épaisseur déposée',round(thickness,4),'µm'),metric('Masse de cuivre',round(mass,5),'g'),metric('Courant limite',round(limit,4),'A'),metric('Rendement du dépôt',round(100*effective/p['current'],2),'%')],
      [chart('Charge utile et croissance','Durée (min)','Épaisseur (µm)',series('Cuivre déposé',times,growth)),chart('Saturation par transport','Courant demandé (A)','Épaisseur après la durée choisie (µm)',series('Dépôt utile',currents,deposited))],
      _curve('Profil de diffusion devant la cathode',distances,[('Cu²⁺ dissous',c)],'Distance à la cathode (µm)','Concentration (mol·L⁻¹)',description='À courant limite, la concentration s’annule à la surface, pas dans la solution éloignée.'),
      ['Cu²⁺+2e⁻→Cu. Faraday : nCu=Iutile Δt/(2F). Épaisseur e=m/(ρS), avec ρCu=8,96 g·cm⁻³.',
       'Fick, couche plane stationnaire : jlim=2FDc∞/δ. Convertir c de mol·L⁻¹ en mol·m⁻³, S en m² et δ en m.',
       'Le modèle impose Iutile=min(I,Ilim). Le reste du courant est attribué à des réactions parasites sans décrire leurs produits.'],
      ['Cuivre compact uniforme, diffusion D=7×10⁻¹⁰ m²·s⁻¹ constante ; solution bien alimentée de concentration de bulk fixe.',
       'Le plateau de courant utile est une idéalisation de contrôle : dendrites, rugosité, migration et bulles exclues.',
       'La solution n’est pas un réservoir fermé ; sinon sa concentration diminuerait au cours du dépôt.'],
      table('Conversions et bilan',['Grandeur','Valeur','Unité'],[['Surface',p['area']*1e-4,'m²'],['Concentration éloignée',p['concentration']*1000,'mol·m⁻³'],['δ',p['layer']*1e-6,'m'],['Iutile',round(effective,6),'A'],['nCu',round(n,7),'mol'],['Charge parasite',round((p['current']-effective)*p['minutes']*60,4),'C']]))

def copper_conditional(loglig,logb1,logb2):
    # Formation factors include free + complex species, valid even for weak ligand.
    l1=np.logaddexp(0,math.log(10)*(logb1+2*np.asarray(loglig)))
    l2=np.logaddexp(0,math.log(10)*(logb2+4*np.asarray(loglig)))
    e1=.521-R*TREF/F*l1
    e2=.340-R*TREF/(2*F)*l2
    return e1,e2,l1,l2

def cuivre_complexation(p):
    ligand=np.linspace(-5,0,151); e1,e2,_,_=copper_conditional(ligand,p['logbeta1'],p['logbeta2'])
    E1,E2,L1,L2=map(float,copper_conditional(p['lognh3'],p['logbeta1'],p['logbeta2']))
    E21=2*E2-E1; dismutation=2*F*(E2-E1)/1000
    c=10**p['logtotal']; free1=math.exp(math.log(c)-L1); free2=math.exp(math.log(c)-L2)
    x=[0,1,2]; y=[0,E1,2*E2]
    sc=plane_scene('Diagramme de Frost conditionnel',paths=[dict(label='États Cu(0), Cu(I), Cu(II)',x=x,y=y)],points=[dict(x=k,y=v,label=f'Cu({k})',group=k) for k,v in zip(x,y)],bounds=[-.15,2.15,min(y)-.12,max(y)+.12],xlabel='Nombre d’oxydation',ylabel='nE° conditionnel (V)',description='Les points dissous représentent les sommes espèce libre + complexe à activité fixée du ligand. Cu(I) sous la corde est stable vis-à-vis de sa dismutation.')
    sc['equalAspect']=False
    return result([metric('E° conditionnel Cu(I)/Cu',round(E1,5),'V'),metric('E° conditionnel Cu(II)/Cu',round(E2,5),'V'),metric('ΔG° dismutation Cu(I)',round(dismutation,3),'kJ·mol⁻¹ réaction'),metric('Dismutation standard','favorisée' if dismutation<0 else 'défavorisée')],
      [chart('Ligand et potentiel conditionnel','log₁₀ aNH₃','E° conditionnel (V)',series('Cu(I)/Cu',ligand,e1),series('Cu(II)/Cu',ligand,e2),series('Cu(II)/Cu(I)',ligand,2*e2-e1))],sc,
      ['Complexation : Cu⁺+2NH₃⇌[Cu(NH₃)₂]⁺, β₁ ; Cu²⁺+4NH₃⇌[Cu(NH₃)₄]²⁺, β₂.',
       'Pour chaque état : ctotal=clibre(1+βaNH₃^m). Substituer clibre dans Nernst donne E°cond=E°−(RT/nF)ln(1+βaNH₃^m).',
       'Frost : ordonnée Cu(I)=E1, Cu(II)=2E2. Pour 2Cu(I)→Cu(0)+Cu(II), ΔG°=2F(E2−E1). Une ordonnée Cu(I) sous la corde donne ΔG°>0.'],
      ['Activité de NH₃ libre imposée, β₁ et β₂ réglables ; protonation du ligand et autres complexes exclus.',
       'Potentiels libres choisis : E°Cu⁺/Cu=0,521 V et E°Cu²⁺/Cu=0,340 V à 298 K. Les valeurs conditionnelles sont relatives à la concentration totale de chaque état.',
       'Le signe affiché concerne la dismutation aux états standard conditionnels. Les concentrations réelles changent ΔG via RT ln Q.'],
      table('Fraction libre et potentiels à concentrations égales',['Grandeur','Valeur','Unité'],[['Cu(I) libre',float(free1),'mol·L⁻¹'],['Cu(II) libre',float(free2),'mol·L⁻¹'],['E Cu(I)/Cu à ctotal',round(E1+R*TREF/F*math.log(c),6),'V'],['E Cu(II)/Cu à ctotal',round(E2+R*TREF/(2*F)*math.log(c),6),'V'],['E°cond Cu(II)/Cu(I)',round(E21,6),'V']]))

def silver_titration(ratio,concentration,pks):
    ratio=np.asarray(ratio,dtype=float)
    ct_ag=concentration*ratio/(1+ratio); ct_br=concentration/(1+ratio)
    difference=ct_ag-ct_br; ks=10**(-pks)
    precipitates=ct_ag*ct_br>ks
    disc=np.hypot(difference,2*math.sqrt(ks))
    # Stable evaluation of positive root for both signs of difference.
    silver=np.where(difference>=0,(difference+disc)/2,2*ks/(disc-difference))
    bromide=np.where(difference<=0,(-difference+disc)/2,2*ks/(disc+difference))
    silver=np.where(precipitates,silver,ct_ag); bromide=np.where(precipitates,bromide,ct_br)
    solid=np.maximum(ct_ag-silver,0)
    return silver,bromide,solid,precipitates

def dosage_potentiometrique(p):
    rr=np.linspace(0,2,401); ag,br,solid,prec=silver_titration(rr,p['concentration'],p['pks'])
    ratio=p['ratio']; aa,bb,ss,has=silver_titration(ratio,p['concentration'],p['pks']); aa=float(aa); bb=float(bb); ss=float(ss)
    potential=.800+R*TREF/F*np.log(np.maximum(ag,1e-30))
    # No defined Ag+/Ag equilibrium potential at exactly zero Ag+.
    y=[None if a==0 else float(v) for a,v in zip(ag,potential)]
    chosen='non défini : aucune activité Ag⁺' if aa==0 else round(.800+R*TREF/F*math.log(aa),6)
    curve=_curve('Précipitation et conservation de la matière',rr,[('Ag⁺ libre',ag),('Br⁻ libre',br),('AgBr solide par volume de mélange',solid)],'V/Véquiv','Quantité par volume (mol·L⁻¹)',description='Le volume titrant réduit fait passer d’un excès de bromure à un excès d’argent. Les deux ions restent à concentration finie à l’équivalence ; AgBr solide est compté en moles par litre de mélange, avec dilution et produit de solubilité conservés.')
    return result([metric('Potentiel Ag⁺/Ag',chosen,'V' if aa else ''),metric('Ag⁺ libre',float(aa),'mol·L⁻¹'),metric('Br⁻ libre',float(bb),'mol·L⁻¹'),metric('AgBr précipité',float(ss),'mol·L⁻¹ mélange')],
      [chart('Saut potentiométrique fini à l’équivalence','V/Véquiv','E (V)',series('E°+(RT/F)ln aAg⁺',rr,y))],curve,
      ['Avec c identique pour la solution initiale et le titrant, Véquiv=Vinitial et r=V/Véquiv. Les concentrations totales diluées sont cAg=c r/(1+r) et cBr=c/(1+r).',
       'Si AgBr(s) existe : [Ag⁺][Br⁻]=Ks et [Ag⁺]−[Br⁻]=cAg−cBr. Résoudre le quadratique par une formule stable, y compris à r=1.',
       'À l’équivalence, les deux ions valent √Ks. Si le produit des concentrations totales est inférieur à Ks, il n’y a pas de solide et les concentrations libres sont les totales.'],
      ['Solution idéale, électrode Ag/Ag⁺ à 298 K, produit de solubilité constant ; complexation et potentiel de référence exclus.',
       'Le solide est quantifié en moles par litre de mélange, pas en concentration d’une espèce dissoute.',
       'À r=0, aucune activité Ag⁺ n’est imposée : Nernst ne définit pas ce potentiel ; le point est laissé vide, sans coupure arbitraire.'],
      table('Contrôle des deux bilans',['Grandeur','Valeur','Unité'],[['Ag total',p['concentration']*ratio/(1+ratio),'mol·L⁻¹'],['Ag libre + AgBr',aa+ss,'mol·L⁻¹'],['Br total',p['concentration']/(1+ratio),'mol·L⁻¹'],['Br libre + AgBr',bb+ss,'mol·L⁻¹'],['[Ag⁺][Br⁻]',aa*bb,'(mol·L⁻¹)²'],['Ks',10**(-p['pks']),'']]))

CALCULATORS={name:globals()[name] for name in ('nernst_pile','electrolyse_h2','pile_combustible','batterie_intercalation','corrosion_protection','electrodepot','cuivre_complexation','dosage_potentiometrique')}
