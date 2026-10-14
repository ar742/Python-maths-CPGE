"""Bilans explicites et solutions vérifiables pour huit TP de cinétique."""
import math
import numpy as np
from commun import metric,series,chart,result,curve_scene,field_scene,table
R=8.314462618

def horloge_iode(p):
    t=np.array([50.,100.,170.,230.,315.,410.]);volume=np.arange(1.,7.);remaining=1-volume/p['vmax']
    fitted=[];rows=[];grid=np.linspace(0,500,251)
    for order in (0,1,2):
        target=1-remaining if order==0 else (-np.log(remaining) if order==1 else 1/remaining-1)
        k=float(np.dot(t,target)/np.dot(t,t))
        def fraction(times):
            return np.maximum(1-k*times,0) if order==0 else (np.exp(-k*times) if order==1 else 1/(1+k*times))
        predicted=p['vmax']*(1-fraction(t));error=float(np.mean((predicted-volume)**2))
        fitted.append((order,k,error,p['vmax']*(1-fraction(grid))))
        half=(.5/k if order==0 else math.log(2)/k if order==1 else 1/k)
        rows.append([order,k,half,error])
    chosen=min(fitted,key=lambda item:item[2]);order,k,error,_=chosen
    scene=curve_scene('Les seuils colorés du recueil et les modèles',grid,[(f'Ordre {o}',values) for o,_,_,values in fitted],'Temps (s)','Volume cumulé (mL)','Les six points proviennent du recueil. Les courbes sont ajustées en imposant V(0)=0 et l’asymptote V∞ choisie; aucune donnée mesurée n’est modifiée.')
    return result([metric('Modèle le mieux ajusté',f'ordre {order}'),metric('Coefficient normalisé κ',k,'s⁻¹'),metric('Erreur quadratique sur V',error,'mL²'),metric('Seuil de 5 mL du recueil',315,'s')],
        [chart('Comparer les mesures aux courbes','t (s)','V (mL)',series('Six mesures du recueil',t,volume),*[series(f'Ordre {o}',grid,values) for o,_,_,values in fitted])],scene,
        ['H₂O₂+2I⁻+2H⁺→I₂+2H₂O. I₂+2S₂O₃²⁻→2I⁻+S₄O₆²⁻ : l’iodure est régénéré.', 'On suppose c(t)/c(0)=1−V(t)/V∞. Les trois transformations sont 1−c/c₀, −ln(c/c₀) et c₀/c−1.', 'L’ajustement de chaque transformation est contraint à passer par l’origine. On compare ensuite les erreurs dans la même grandeur V, pas celles de trois axes différents.',f'Le meilleur ajustement sur ces six points est l’ordre {order}; sa comparaison dépend de V∞={p["vmax"]:g} mL.'],
        ['Six seuils du TP p.546, sans protocole physique reproduit. Le volume ajouté et la dilution ne sont pas modélisés séparément.', 'La conclusion concerne un ordre apparent dans les conditions du TP. Elle ne détermine pas les ordres partiels en iodure et en acidité.', 'κ est exprimé en s⁻¹ pour une concentration normalisée. Pour l’ordre 0, κ=k/c₀; pour l’ordre 2, κ=kc₀.'],table('Ajuster puis comparer dans la grandeur mesurée',['Ordre','κ (s⁻¹)','t½ ajusté (s)','Erreur moyenne (mL²)'],rows))

def arrhenius_k(T,ea):return .01*np.exp(ea*1000/R*(1/500-1/np.asarray(T)))

def arrhenius_catalyse(p):
    T=p['temperature'];ea=p['ea'];gain=p['gain'];temps=np.linspace(350,850,251)
    k=float(arrhenius_k(T,ea));cat=k*math.exp(gain*1000/(R*T));coordinate=np.linspace(0,1,201)
    def profile(barrier):return np.where(coordinate<=.5,barrier*np.sin(np.pi*coordinate)**2,-40+(barrier+40)*np.cos(np.pi*(coordinate-.5))**2)
    return result([metric('k sans catalyse',k,'s⁻¹'),metric('k de la voie catalysée',cat,'s⁻¹'),metric('Facteur d’accélération',cat/k),metric('Enthalpie de réaction conservée',-40,'kJ/mol')],
        [chart('Arrhénius : même préfacteur, deux barrières','T (K)','k (s⁻¹)',series('Sans catalyse',temps,arrhenius_k(temps,ea)),series('Voie catalysée',temps,arrhenius_k(temps,ea)*np.exp(gain*1000/(R*temps))),y_scale='log')],
        curve_scene('Une voie plus rapide conserve les états initial et final',coordinate,[('Sans catalyse',profile(ea)),('Voie catalysée',profile(ea-gain))],'Coordonnée de réaction (sans unité)','Énergie molaire relative (kJ/mol)','Profil schématique : les deux voies partagent les mêmes réactifs et produits. La hauteur est imposée; la forme du chemin n’est pas un mécanisme calculé.'),
        ['La référence sans catalyse est k(500 K)=0,01 s⁻¹. Le préfacteur est donc fixé après choix de Ea.', 'k(T)=kref exp[(Ea/R)(1/Tref−1/T)]. Pour comparer les deux voies, leur préfacteur est conservé et la barrière diminuée.',f'Le facteur à T={T:g} K vaut exp(ΔEa/RT)={cat/k:.6g}.', 'Un catalyseur accélère aussi le retour vers l’équilibre; il ne change pas la constante d’équilibre à température fixée.'],
        ['Paramètres cinétiques didactiques; ce facteur ne prédit pas le rendement d’un catalyseur industriel.', 'Ea est une énergie d’activation apparente, distincte de l’enthalpie de réaction. La barrière choisie pour la voie catalysée reste non négative.'])

def conversions(k,tau,n):
    da=k*np.asarray(tau)*60
    return da/(1+da),-np.expm1(-da),-np.expm1(-n*np.log1p(da/n))

def reacteurs_residence(p):
    k,tau,n=p['k'],p['tau'],p['n'];values=conversions(k,tau,n);times=np.linspace(0,30,301);curves=conversions(k,times,n)
    x=np.linspace(.1,30,100);y=np.arange(1.,9.);field=np.array([conversions(k,x,int(count))[2] for count in y])*100
    scene=field_scene('Conversion en fonction du séjour et du nombre de cuves',x,y,field,'Les huit lignes correspondent aux nombres entiers de cuves. Chaque cuve a un séjour τ/N; le séjour total reste τ.',points=[dict(x=tau,y=n,label='Choix courant',group=0)],levels=[25,50,75,90]);scene.update(xLabel='Temps total τ (min)',yLabel='Nombre de cuves N',valueLabel='Conversion (%)')
    return result([metric('Nombre de Damköhler kτ',k*tau*60),metric('Cuve agitée',100*values[0],'%'),metric('Réacteur piston',100*values[1],'%'),metric(f'{n} cuves en série',100*values[2],'%')],
        [chart('Même réaction, même temps total','τ (min)','Conversion (%)',*[series(label,times,100*c) for label,c in zip(['Une cuve','Piston',f'{n} cuves'],curves)])],scene,
        ['Pour une réaction isotherme A→B du premier ordre, Da=kτ est sans unité. Le temps en minutes est converti en secondes.', 'Cuve parfaitement mélangée : X=Da/(1+Da), obtenu en égalant débit net et consommation.', 'Piston : X=1−exp(−Da). N cuves identiques : X=1−(1+Da/N)⁻ᴺ.', 'À séjour total fixé, N=1 retrouve la cuve; augmenter N rapproche du piston. Il faut ensuite comparer coût, mélange et transferts.'],
        ['Débit volumique constant, densité constante, état stationnaire, absence de diffusion et de bilan thermique.', 'Les géométries et conversions sont des modèles idéalisés; le nombre de cuves est entier.'],table('Conversion et fraction restante',['Organisation','X','Fraction de A restante'],[[name,float(v),float(1-v)] for name,v in zip(['Cuve','Piston',f'{n} cuves'],values)]))

def successive(k1,k2,t):
    t=np.asarray(t);a=np.exp(-k1*t);delta=k2-k1
    b=k1*t*a if abs(delta)<1e-12*max(k1,k2) else k1*a*(-np.expm1(-delta*t))/delta
    c=np.maximum(0,1-a-b)
    return a,b,c

def selectivite_successive(p):
    k1,k2,t=p['k1'],p['k2'],p['time'];optimal=1/k1 if abs(k2-k1)<1e-12 else math.log(k2/k1)/(k2-k1)
    times=np.linspace(0,max(1.8*optimal,t),301);a,b,c=successive(k1,k2,times);point=successive(k1,k2,t);peak=float(successive(k1,k2,optimal)[1])
    return result([metric('Temps optimal pour B',optimal,'min'),metric('B maximal',peak,'mol/L'),metric('B à l’instant choisi',float(point[1]),'mol/L'),metric('Somme A+B+C',sum(float(v) for v in point),'mol/L')],
        [chart('Le maximum de B est une condition sur les vitesses','t (min)','Vitesse (mol·L⁻¹·min⁻¹)',series('Formation k₁[A]',times,k1*a),series('Consommation k₂[B]',times,k2*b))],
        curve_scene('Un intermédiaire formé puis consommé',times,[('A',a),('B',b),('C',c)],'Temps (min)','Concentration (mol/L)','A(0)=1 mol/L; B(0)=C(0)=0. Les deux étapes sont irréversibles et du premier ordre.'),
        ['A=A₀exp(−k₁t). B=A₀k₁[exp(−k₁t)−exp(−k₂t)]/(k₂−k₁) si k₁≠k₂.', 'Si k₁=k₂=k, B=A₀kt exp(−kt). La formule limite supprime la division par zéro.', 'C=A₀−A−B. Le maximum de B vérifie k₁A=k₂B.', 'Pour k₁≠k₂, topt=ln(k₂/k₁)/(k₂−k₁); pour k₁=k₂, topt=1/k.'],
        ['Modèle générique de sélectivité, sans données de procédé commercial; volume et température constants.', 'Le maximum de concentration de B n’est pas automatiquement le meilleur compromis économique ou énergétique.'],table('Bilan à l’instant choisi',['Espèce','Concentration (mol/L)'],[[name,float(value)] for name,value in zip(['A','B','C'],point)]))

def coverage(pa,pb,ka,kb):
    denominator=1+ka*np.asarray(pa)+kb*np.asarray(pb)
    return 1/denominator,ka*np.asarray(pa)/denominator,kb*np.asarray(pb)/denominator

def catalyse_surface(p):
    pa,pb,ka,kb=(p[k] for k in ('pa','pb','ka','kb'));free,a,b=coverage(pa,pb,ka,kb);pressures=np.linspace(0,10,251)
    x=np.linspace(0,10,91);y=np.linspace(0,10,81);xx,yy=np.meshgrid(x,y);field=coverage(xx,yy,ka,kb)[1]
    scene=field_scene('Occupation des sites par A',x,y,field,'Chaque valeur est la fraction θA des sites occupés par A. B occupe les mêmes sites sans produire dans ce modèle.',points=[dict(x=pa,y=pb,label='Réglages actuels',group=0)],levels=[.25,.5,.75]);scene.update(xLabel='pA (bar)',yLabel='pB (bar)',valueLabel='Fraction θA')
    return result([metric('Sites libres',float(free)*100,'%'),metric('Sites occupés par A',float(a)*100,'%'),metric('Sites occupés par B',float(b)*100,'%'),metric('Vitesse par site, kcat=1 s⁻¹',float(a),'s⁻¹')],
        [chart('Saturation et compétition','pA (bar)','Vitesse par site (s⁻¹)',series('Avec B',pressures,coverage(pressures,pb,ka,kb)[1]),series('Sans B',pressures,coverage(pressures,0,ka,kb)[1]))],scene,
        ['Un site est libre, occupé par A ou occupé par B. À l’équilibre d’adsorption, θA=KA pA/(1+KA pA+KB pB).', 'θB=KB pB/(1+KA pA+KB pB); θlibre complète la somme à 1.', 'Seul A adsorbé réagit ici : vsite=kcat θA, avec kcat=1 s⁻¹.', 'À faible pA, la vitesse est presque proportionnelle à pA. À forte pA, elle sature; augmenter pB bloque des sites.'],
        ['Adsorption de Langmuir compétitive, sites identiques, absence de transport limitant; paramètres didactiques.', 'Ce modèle ne décrit pas un mécanisme industriel précis de synthèse du méthanol ou d’oxydation du CO.'],table('Répartition de la surface',['État du site','Fraction'],[['Libre',float(free)],['A',float(a)],['B',float(b)],['Somme',float(free+a+b)]]))

def chain_rates(c,k1,k5,k6):
    start=k1*np.asarray(c);propagation=k5*math.sqrt(k1/k6)*np.asarray(c)**1.5
    total=2*start+propagation
    return total,start,propagation

def ethanal_aeqs(p):
    k1,k5,k6=10.**p['logk1'],10.**p['logk5'],10.**p['logk6'];c=p['concentration'];v,init,chain=chain_rates(c,k1,k5,k6)
    radical=math.sqrt(k1*c/k6);order=(2*init+1.5*chain)/v;energy=(318*2*init+201*chain)/v;length=v/init
    concentrations=np.geomspace(.0001,1,251);total,starts,prop=chain_rates(concentrations,k1,k5,k6)
    return result([metric('Ordre apparent local',float(order)),metric('Énergie apparente locale',float(energy),'kJ/mol'),metric('Concentration de CH₃·',radical,'mol/L'),metric('Longueur de chaîne définie au recueil',float(length))],
        [chart('Du premier ordre au régime 3/2','[E] (mol/L)','Vitesse (mol·L⁻¹·s⁻¹)',series('Consommation totale',concentrations,total),series('Amorçage : 2k₁[E]',concentrations,2*starts),series('Propagation',concentrations,prop),x_scale='log',y_scale='log')],
        curve_scene('Les vitesses des produits suivent le bilan du mécanisme',concentrations,[('CO et disparition E',total),('CH₄',prop),('H₂ et C₂H₆, chacun',starts)],'[E] (mol/L)','Vitesse (mol·L⁻¹·s⁻¹)','Ces courbes représentent des lois de vitesse sous AEQS, pas l’évolution temporelle d’une même expérience.'),
        ['L’AEQS appliquée au mécanisme p.549–550 donne [CH₃·]=√(k₁[E]/k₆).', 'vE=2k₁[E]+k₅√(k₁/k₆)[E]³ᐟ². On garde les deux termes avant de discuter une approximation.', 'vCO=vE; vH₂=vC₂H₆=k₁[E]; vCH₄ est le terme de propagation.',f'L’ordre local est d ln(vE)/d ln([E])={order:.6g}. Il tend vers 3/2 seulement quand la propagation domine.', 'Pour la propagation, Ea=E₅+(E₁−E₆)/2=42+318/2=201 kJ/mol. L’énergie apparente totale est pondérée par les deux contributions.'],
        ['AEQS admise pour les quatre intermédiaires du mécanisme du recueil. Les constantes réglables sont illustratives, sans préfacteurs expérimentaux.', 'Le rapport [CH₃·]/[E] et la longueur de chaîne ne démontrent pas à eux seuls la validité dynamique de l’AEQS.', 'Le facteur 2 de l’amorçage est conservé; la longueur de chaîne n’est pas supposée supérieure à 100 pour tous les réglages.'],table('Bilans atomiques des vitesses',['Contrôle','Valeur (mol d’atomes·L⁻¹·s⁻¹)'],[['Carbone : 2vE−vCO−vCH₄−2vC₂H₆',float(2*v-v-chain-2*init)],['Hydrogène : 4vE−2vH₂−4vCH₄−6vC₂H₆',float(4*v-2*init-4*chain-6*init)],['Oxygène : vE−vCO',0.]]))

def heat_terms(T,ambient,qref,ea,h):
    T=np.asarray(T)
    return qref*np.exp(ea*1000/R*(1/300-1/T)),h*(T-ambient)

def heat_equilibria(ambient,qref,ea,h):
    ts=np.linspace(ambient,ambient+90,1801);gen,out=heat_terms(ts,ambient,qref,ea,h);diff=gen-out;roots=[]
    candidates=[float(ts[i]) for i in range(len(ts)) if abs(diff[i])<=1e-12*max(1.,abs(gen[i]),abs(out[i]))]
    for i in range(len(ts)-1):
        if diff[i]*diff[i+1]<0:
            lo,hi=ts[i],ts[i+1]
            for _ in range(55):
                mid=(lo+hi)/2;gm,om=heat_terms(mid,ambient,qref,ea,h)
                if (float(gm-om)>0)==(diff[i]>0):lo=mid
                else:hi=mid
            candidates.append((lo+hi)/2)
    for root in sorted(candidates):
        if roots and abs(root-roots[-1][0])<1e-7:continue
        g,_=heat_terms(root,ambient,qref,ea,h);slope=float(g)*ea*1000/(R*root*root)-h
        roots.append((root,slope))
    return roots

def emballement_thermique(p):
    ta,qref,ea,h,t0=(p[k] for k in ('ambient','qref','ea','h','initial'));roots=heat_equilibria(ta,qref,ea,h)
    # Intégration RK4 indépendante de l’échantillonnage exporté.
    times=[0.];temps=[t0];current=t0;step=.25;last=0.;limit=ta+90
    def rhs(temp):
        g,o=heat_terms(temp,ta,qref,ea,h);return float(g-o)/100
    for i in range(7200):
        a=rhs(current)
        if not 250<=current+step*a<=limit:break
        b=rhs(current+step*a/2);c=rhs(current+step*b/2);d=rhs(current+step*c)
        nxt=current+step*(a+2*b+2*c+d)/6
        if not 250<=nxt<=limit:break
        current=nxt;last=(i+1)*step
        if i%8==7:times.append(last);temps.append(current)
    if times[-1]!=last:times.append(last);temps.append(current)
    axis=np.linspace(ta,ta+90,361);gen,out=heat_terms(axis,ta,qref,ea,h)
    display=np.linspace(ta,ta+min(90,max(35,max((r-ta for r,_ in roots),default=0)+10)),251);gd,od=heat_terms(display,ta,qref,ea,h)
    return result([metric('Équilibres dans le domaine étudié',len(roots)),metric('Température finale calculée',current,'K'),metric('Durée calculée',last,'s'),metric('État du calcul','1800 s atteintes' if last>=1800 else 'Arrêt à la limite du domaine')],
        [chart('Une trajectoire de température','t (s)','T (K)',series('Intégration RK4',times,temps)),chart('Bilans sur tout le domaine','T (K)','Puissance volumique (W/L)',series('Production',axis,gen),series('Évacuation',axis,out),y_scale='log')],
        curve_scene('Les intersections sont des équilibres thermiques',display,[('Production de chaleur',gd),('Évacuation de chaleur',od)],'T (K)','Puissance (W/L)','La dérivée du bilan production−évacuation distingue stabilité et instabilité. Les intersections sont recherchées entre Ta et Ta+90 K.'),
        ['Production : q(T)=qref exp[(Ea/R)(1/300−1/T)]. Évacuation : h(T−Ta).', 'La capacité volumique Cth=100 J/(L·K) donne Cth dT/dt=q(T)−h(T−Ta).', 'Un équilibre vérifie production=évacuation. Il est localement stable si q′(T)−h<0, instable si ce nombre est positif.', 'La concentration de réactif est maintenue constante dans ce modèle de bilan thermique. La chaleur n’est donc pas limitée par un stock de réactif.', 'RK4 utilise un pas 0,25 s; l’intégration est interrompue si elle quitte le domaine T≤Ta+90 K. Une trajectoire arrêtée n’est pas une température finale de procédé.'],
        ['Modèle pédagogique de production/évacuation, inspiré du raisonnement de Semenov; paramètres et capacité didactiques.', 'Les zéros du maillage et les changements de signe sont détectés. Une racine tangente située entre deux points peut demander une étude analytique supplémentaire; une dérivée nulle ne suffit pas à conclure.', 'Absence de consommation des réactifs, changement de phase et variation de volume; aucune extrapolation hors du domaine étudié.'],table('Équilibres localisés par dichotomie',['T (K)','Dérivée du bilan (W/(L·K))','Conclusion locale'],[[float(t),float(s),'Stable' if s<-1e-9 else ('Instable' if s>1e-9 else 'Indécis au premier ordre')] for t,s in roots]))

def effectiveness(phi):
    phi=np.asarray(phi);small=phi<.01;safe=np.where(small,1.,phi)
    return np.where(small,1-phi**2/15+2*phi**4/315,3*(safe/np.tanh(safe)-1)/safe**2)

def grain_profile(rho,phi):
    rho=np.asarray(rho);safe=np.where(rho==0,1.,rho)
    if phi<1e-5:return np.ones_like(rho)
    return np.where(rho==0,phi/math.sinh(phi),np.sinh(phi*safe)/(safe*math.sinh(phi)))

def diffusion_grain(p):
    radius=p['radius']*1e-6;diffusion=10.**p['logd'];k=p['k'];phi=radius*math.sqrt(k/diffusion);eta=float(effectiveness(phi));rho=np.linspace(0,1,251);profile=grain_profile(rho,phi)
    sizes=np.linspace(50,1500,251);etas=effectiveness(sizes*1e-6*math.sqrt(k/diffusion));x=np.linspace(-1.15,1.15,91);y=x.copy();xx,yy=np.meshgrid(x,y);rr=np.sqrt(xx*xx+yy*yy);field=np.where(rr<=1,grain_profile(np.minimum(rr,1),phi),1)
    angle=np.linspace(0,2*np.pi,201);scene=field_scene('Une coupe du grain poreux et sa concentration',x,y,field,'La couleur donne C/Csurface. Le cercle est la frontière du grain; à l’extérieur, le bain est imposé à C/Csurface=1.',paths=[dict(label='Frontière du grain',x=np.cos(angle),y=np.sin(angle))],levels=[.2,.5,.8]);scene.update(xLabel='x/R (sans unité)',yLabel='y/R (sans unité)',equalAspect=True,valueLabel='C/Csurface')
    return result([metric('Module de Thiele φ',phi),metric('Efficacité interne η',eta),metric('Concentration au centre / surface',float(profile[0])),metric('Temps diffusif R²/Deff',radius*radius/diffusion,'s')],
        [chart('Le profil ne reste pas uniforme','r/R','C/Csurface',series('Profil stationnaire',rho,profile)),chart('Même matériau, rayon différent','Rayon (µm)','Efficacité interne',series('η',sizes,etas))],scene,
        ['Le grain sphérique consomme A au premier ordre : Deff ΔC−kC=0, à l’état stationnaire.', 'φ=R√(k/Deff). La surface est maintenue à Csurface; la solution est C/Csurface=sinh(φr/R)/[(r/R)sinhφ].', 'Au centre, la limite vaut φ/sinhφ. Le facteur d’efficacité est η=3(φ cothφ−1)/φ².', 'Quand φ→0, η=1−φ²/15+… : presque tout le grain est alimenté. Pour φ grand, η≈3/φ.'],
        ['Complément de génie chimique : grain isotherme, diffusivité constante, cinétique du premier ordre, absence de résistance externe.', 'La taille change l’utilisation des sites, sans modifier ici la constante cinétique intrinsèque; le coût et la perte de charge ne sont pas calculés.'])

CALCULATORS={name:globals()[name] for name in ('horloge_iode','arrhenius_catalyse','reacteurs_residence','selectivite_successive','catalyse_surface','ethanal_aeqs','emballement_thermique','diffusion_grain')}
