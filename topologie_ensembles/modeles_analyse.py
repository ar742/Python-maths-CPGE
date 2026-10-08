"""Compacité et continuité : formules exactes séparées des dessins finis."""
from __future__ import annotations
import math
from fractions import Fraction
import numpy as np
from commun import chart, metric, result, scene, series, integrate


def _dots(label,x,y):
    curve=series(label,x,y); curve['style']='dots'; return curve


def _path(label,points,closed=True,fill=False,color=0):
    return dict(label=label,points=np.asarray(points),closed=closed,fill=fill,colorIndex=color)


def _ellipse(a,b,count=361):
    t=np.linspace(0,2*math.pi,count)
    return np.column_stack((a*np.cos(t),b*np.sin(t)))


def _geometry(title,description,paths=(),points=(),discs=(),bounds=None,**extra):
    return scene('geometry',title,description,paths=list(paths),points=list(points),discs=list(discs),bounds=bounds or [-3,3,-2,2],**extra)


def bolzano_weierstrass(p):
    N=int(p['N']); eps=float(p['epsilon']); ns=np.arange(N+1)
    values=(-1.)**ns+1/(ns+1)
    even=ns[ns%2==0]; odd=ns[ns%2==1]
    rank_even=max(0,math.floor((1/eps-1)/2)+1)
    rank_odd=max(0,math.floor((1/eps-2)/2)+1)
    errors=1/(ns+1)
    points=[dict(x=int(n),y=float(values[n]),label=f'n={n}',colorIndex=int(n%2)) for n in ns[:min(N+1,81)]]
    return result(
        [metric('Borne exacte |uₙ|≤',2),metric('Valeur d’adhérence paire',1),metric('Valeur d’adhérence impaire',-1),metric('Rang k suffisant, sous-suite paire',rank_even),metric('Rang k suffisant, sous-suite impaire',rank_odd),metric('Convergence de la suite entière','Non')],
        [chart('Deux extractions explicites','Indice original n','uₙ',_dots('n pairs',even,values[even]),_dots('n impairs',odd,values[odd]),series('Limite paire',ns,np.ones_like(ns)),series('Limite impaire',ns,-np.ones_like(ns))),
         chart('Une erreur exacte, indépendante du maillage','Indice n','Distance à la limite de sa sous-suite',series('1/(n+1)',ns,errors),series('Tolérance ε',ns,np.full_like(ns,eps,dtype=float)))],
        _geometry('Une suite bornée à deux amas','Les couleurs isolent des indices strictement croissants. La séparation des limites exclut la convergence de la suite entière.',points=points,bounds=[-1,min(N+1,82),-1.4,2.3],subsequences=[dict(indices=even,values=values[even],limit=1),dict(indices=odd,values=values[odd],limit=-1)]),
        ['1. La formule donne −1<uₙ≤2, donc une suite bornée de ℝ.',
         '2. Pour φ(k)=2k et ψ(k)=2k+1, les applications d’indices sont strictement croissantes.',
         '3. u₂ₖ→1 et u₂ₖ₊₁→−1 avec les erreurs 1/(2k+1) et 1/(2k+2). Les deux limites diffèrent.',
         f'4. Pour obtenir une erreur strictement inférieure à ε={eps:g}, prendre k≥{rank_even} pour les pairs et k≥{rank_odd} pour les impairs.'],
        ['Le dessin montre seulement les N+1 premiers termes ; les limites reposent sur la formule exacte.','Bolzano–Weierstrass garantit une extraction convergente pour toute suite bornée de ℝᵈ, sans garantir une limite unique.'])


def record_indices(values,target=1.0):
    """Nouveaux records STRICTS ; la suite d'indices commence à zéro."""
    distances=np.abs(np.asarray(values,dtype=float)-target)
    if not len(distances):return np.array([],dtype=int)
    preceding=np.r_[np.inf,np.minimum.accumulate(distances)[:-1]]
    return np.flatnonzero(distances<preceding)


def nearest_survival(d,N):
    """P(min |X_j−1|>d), X_j indépendants uniformes sur [0,3]."""
    d=np.asarray(d,dtype=float)
    base=np.where(d<0,1.,np.where(d<=1,1-2*d/3,np.where(d<=2,(2-d)/3,0.)))
    return np.maximum(base,0.)**int(N)


def nearest_expectation(N):
    return (3+3.**(-int(N)))/(2*(int(N)+1))


def nearest_trials(N,trials,seed):
    rng=np.random.default_rng(seed)
    values=[]
    for start in range(0,trials,25):
        count=min(25,trials-start)
        values.extend(np.min(np.abs(rng.uniform(0,3,(count,N))-1),axis=1))
    return np.asarray(values)


def extraction_aleatoire(p):
    N=int(p['N']); seed=int(p['seed']); trials=int(p['trials']); d=float(p['d'])
    rng=np.random.default_rng(seed); xs=rng.uniform(0,3,N)
    indices=record_indices(xs); distances=np.abs(xs[indices]-1)
    minima=nearest_trials(N,trials,seed+1000003)
    scaled=2*N*minima/3
    hist,edges=np.histogram(scaled,bins=np.linspace(0,6,25),density=False)
    density=hist/(trials*np.diff(edges)); centers=(edges[:-1]+edges[1:])/2
    w=np.linspace(0,6,401); exact=(1-w/N)**(N-1)
    show=np.unique(np.r_[np.linspace(0,N-1,max(1,min(N,600-len(indices))),dtype=int),indices])
    probability=float(nearest_survival(d,N))
    log_probability=N*math.log1p(-2*d/3)/math.log(10)
    probability_display=probability if probability>0 else f'10^({log_probability:.3f}) : sous la précision flottante'
    return result(
        [metric('Nouveaux records stricts',len(indices)),metric('Dernier indice retenu',int(indices[-1])),metric('Dernière distance à 1',float(distances[-1])),metric('Espérance exacte de D_N',nearest_expectation(N)),metric('Probabilité exacte D_N>d',probability_display),metric('Fréquence expérimentale D_N>d',float(np.mean(minima>d)))],
        [chart('Records de proximité : chaque indice avance','Indice original j','Distance |Xⱼ−1|',_dots('Tirages montrés',show,np.abs(xs[show]-1)),_dots('Records stricts',indices,distances)),
         chart('Le rapprochement de chaque nouveau record','Rang k de l’extraction','Xφ(k)',_dots('Valeurs extraites',np.arange(len(indices)),xs[indices]),series('Cible 1',[0,max(1,len(indices)-1)],[1,1])),
         chart('Loi du meilleur rapprochement, à l’échelle naturelle','w=2ND_N/3','Densité',_dots('Histogramme simulé',centers,density),series('Densité exacte sur cette fenêtre',w,exact),series('Limite exponentielle e⁻ʷ',w,np.exp(-w)))],
        _geometry('L’extraction du TP sans répétition','Un point correspond à un record strict, avec son indice original. Un échantillon fini ne constitue pas la preuve de convergence.',points=[dict(x=int(i),y=float(x),label=f'j={i}',colorIndex=0) for i,x in zip(indices,xs[indices])],bounds=[-N*.03,N*1.03,-.1,3.1],record_indices=indices,record_values=xs[indices],distances=distances,trial_minima=minima,log10_survival=log_probability),
        ['1. Tirer N valeurs indépendantes Xⱼ uniformes sur [0,3] ; la graine reproduit l’expérience.',
         '2. Retenir j seulement si |Xⱼ−1| est strictement inférieur à tous les rapprochements antérieurs. Les indices sont distincts et strictement croissants.',
         '3. Pour 0≤d≤1, P(D_N>d)=(1−2d/3)ᴺ, car un tirage évite ]1−d,1+d[ avec probabilité 1−2d/3.',
         '4. Pour chaque ε>0, P(D_N>ε)→0 et les D_N décroissent : leur limite est nulle presque sûrement. Une intersection dénombrable des événements pour ε=1/k suffit.',
         '5. Presque sûrement, aucun tirage ne vaut exactement 1 et il y a une infinité de records ; cette extraction converge vers 1.'],
        ['La propriété presque sûre suppose une suite infinie de tirages indépendants, absente de l’expérience finie.','L’histogramme utilise des expériences indépendantes de la trajectoire affichée. Les événements et la densité sont calculés analytiquement.','La fenêtre de densité 0≤w≤6 reste dans d≤1 car N≥100. La masse non représentée n’est pas renormalisée.'])


def heron_fractions(n):
    values=[Fraction(2)]
    for _ in range(int(n)):values.append(values[-1]/2+1/values[-1])
    return values


def heron_bounds(values):
    """u_n−√2=(u_n²−2)/(u_n+√2)<(u_n²−2)/u_n, exacte en Fraction."""
    return [(u*u-2)/u for u in values]


def cauchy_rationnels(p):
    n=int(p['n']); epsilon=float(p['epsilon']); values=heron_fractions(n)
    bounds=heron_bounds(values); numerical=np.array([float(v) for v in values]); ns=np.arange(n+1)
    residuals=[u*u-2 for u in values]
    # Le dernier majorant reste représentable à n=8, même si u_n arrondit à √2.
    upper=np.array([float(b) for b in bounds]); tail=float(bounds[-1])
    fractions=[dict(index=k,numerator=str(u.numerator),denominator=str(u.denominator),value=float(u),error_upper=float(bounds[k]),square_residual=str(residuals[k])) for k,u in enumerate(values)]
    lines=[f'u{k}={u}' if k<=4 else f'u{k} : fraction exacte de {len(str(u.numerator))} chiffres au numérateur' for k,u in enumerate(values)]
    return result(
        [metric('Valeur approchée de uₙ',float(values[-1])),metric('Majorant exact converti de uₙ−√2',tail),metric('uₙ²−2 est strictement positif','Oui'),metric('Tous les termes appartiennent à ℚ','Oui'),metric('Limite dans ℚ','Non'),metric('Queue de Cauchy certifiée à ε','Oui' if bounds[-1]<Fraction(str(epsilon)) else 'Pas encore à ce rang')],
        [chart('Convergence monotone vers la complétion','Indice n','Valeur',_dots('Termes rationnels',ns,numerical),series('√2',[0,max(n,1)],[math.sqrt(2)]*2)),
         chart('Un majorant exact du reste','Indice n','Majorant de |uₙ−√2|',_dots('(uₙ²−2)/uₙ',ns,upper),series('ε',[0,max(n,1)],[epsilon]*2))],
        _geometry('Des rationnels de plus en plus précis','La représentation décimale finit par confondre uₙ et √2 ; les fractions exactes gardent uₙ²−2>0.',points=[dict(x=k,y=float(u),label=f'u{k}',colorIndex=0) for k,u in enumerate(values)],bounds=[-.5,max(1,n)+.5,1.35,2.1],fractions=fractions,fraction_labels=lines),
        ['1. Les opérations rationnelles préservent ℚ et uₙ>√2. La suite décroît car uₙ₊₁−uₙ=(2−uₙ²)/(2uₙ)<0.',
         '2. En posant eₙ=uₙ−√2, eₙ₊₁=eₙ²/(2uₙ) : l’erreur devient quadratique.',
         '3. Pour tout q≥p, 0≤u_p−u_q≤u_p−√2<(u_p²−2)/u_p. Ce majorant tend vers zéro et prouve Cauchy.',
         '4. Si √2=a/b avec a et b premiers entre eux, a²=2b² impose a puis b pairs, contradiction. ℚ n’est donc pas complet.',
         f'5. Fraction exacte au rang n={n} : {values[-1]}.'],
        ['√2 sert à identifier la limite dans ℝ ; son irrationalité se prouve par la parité, jamais par une décimale.','La comparaison de Cauchy est faite sur des fractions exactes. Les courbes et la métrique décimale peuvent atteindre la limite de précision des flottants.'])


def compact_cover(m,r):
    gap=1/(2*m); margin=r-gap
    covered=margin>0
    return covered,max(margin,0.),gap


def compacts_recouvrements(p):
    m=int(p['m']); r=float(p['r']); N=int(p['N']); centers=np.linspace(0,1,m+1)
    covered,margin,threshold=compact_cover(m,r)
    witnesses=(np.arange(m)+.5)/m
    # La marge de Lebesgue affichée est certifiée (une minoration, pas le nombre optimal).
    x=np.unique(np.r_[np.linspace(0,1,451),centers,witnesses])
    # Une marge de quelques ulps préserve les exclusions de frontière du dessin.
    plot_radius=r-32*np.finfo(float).eps*max(1.,r)
    counts=np.sum(np.abs(x[:,None]-centers[None,:])<plot_radius,axis=1)
    midpoint_counts=np.sum(np.abs(witnesses[:,None]-centers[None,:])<plot_radius,axis=1)
    ns=np.arange(1,N+1); ends=1-1/ns
    outside=1-1/(2*N)
    discs=[dict(x=float(c),y=0.,r=r,fill=True,closed=False,colorIndex=int(j%4)) for j,c in enumerate(centers)]
    return result(
        [metric('[0,1] couvert par les ouverts','Oui' if covered else 'Non'),metric('Seuil strict du rayon',threshold),metric('Marge de Lebesgue certifiée',margin),metric('Nombre d’ouverts du réseau',m+1),metric('Point hors de U₁∪…∪U_N',outside),metric('Union finie jusqu’à',float(ends[-1]))],
        [chart('Compter les ouverts contenant chaque point','x∈[0,1]','Nombre d’ouverts',series('Comptage sur le dessin',x,counts),_dots('Milieux : témoins exacts',witnesses,midpoint_counts)),
         chart('La famille ouverte du contre-exemple','n','Borne droite de Uₙ',_dots('1−1/n',ns,ends),series('Bord absent 1',[1,N],[1,1]))],
        _geometry('Intervalles ouverts centrés sur le compact','Les disques schématisent les voisinages ouverts de centres j/m. Leurs traces sur l’axe couvrent [0,1] si et seulement si r>1/(2m).',paths=[_path('[0,1]',[[0,0],[1,0]],False,False,3)],discs=discs,points=[dict(x=float(c),y=0,label=f'{j}/{m}',colorIndex=3) for j,c in enumerate(centers)],bounds=[-r-.05,1+r+.05,-max(.2,r*1.3),max(.2,r*1.3)],uncovered_witnesses=[] if covered else witnesses),
        ['1. Le point le plus éloigné du réseau j/m est un milieu (j+1/2)/m : sa distance exacte vaut 1/(2m).',
         '2. Les boules sont ouvertes. L’égalité r=1/(2m) laisse précisément les milieux hors du recouvrement ; il faut une inégalité stricte.',
         '3. Si la marge δ=r−1/(2m)>0, toute partie de [0,1] de diamètre <δ est contenue dans un de ces ouverts : une marge de Lebesgue est ainsi certifiée.',
         '4. Les Uₙ=]−1,1−1/n[ recouvrent [0,1[, mais une sous-famille finie est incluse dans U_N pour son plus grand indice.',
         f'5. Le point x_N=1−1/(2N)={outside:g} appartient à [0,1[ mais pas à U_N. Il n’existe pas de sous-recouvrement fini.'],
        ['La couverture est décidée par la distance exacte au réseau, et non par le nombre de points colorés du maillage.','Le contre-exemple concerne [0,1[, qui n’est pas fermé dans ℝ ; il ne contredit pas Borel–Lebesgue sur [0,1].'])


def ellipse_support(a,b,theta):
    c=math.cos(theta); s=math.sin(theta); h=math.hypot(a*c,b*s)
    return h,np.array([a*a*c/h,b*b*s/h])


def valeurs_extremes(p):
    a=float(p['a']); b=float(p['b']); theta=math.radians(float(p['theta'])); N=int(p['N']); closed=p['domain']=='closed'
    h,vertex=ellipse_support(a,b,theta); approach=(1-1/N)*vertex
    t=np.linspace(-1,1,401); ks=np.arange(2,max(20,N)+1)
    description='Les points extrémaux appartiennent au domaine fermé.' if closed else 'Les points marqués sup/inf sont sur la frontière exclue ; le point d’approche appartient au domaine ouvert.'
    ellipse=_ellipse(a,b)
    outline=_path('Frontière de l’ellipse',ellipse,True,True,0)
    outline['boundaryClosed']=closed
    optimizer_markers=[dict(x=float(vertex[0]),y=float(vertex[1]),label='max',colorIndex=1),dict(x=float(-vertex[0]),y=float(-vertex[1]),label='min',colorIndex=1)] if closed else []
    excluded_markers=[] if closed else [dict(x=float(sign*vertex[0]),y=float(sign*vertex[1]),r=.025,fill=False,closed=False,label='Supremum exclu' if sign==1 else 'Infimum exclu',colorIndex=1) for sign in (1,-1)]
    return result(
        [metric('Supremum exact de ℓθ',h),metric('Infimum exact de ℓθ',-h),metric('Extrema atteints','Oui' if closed else 'Non'),metric('Valeur au point d’approche',(1-1/N)*h),metric('Écart exact au supremum',h/N),metric('Domaine compact','Oui' if closed else 'Non')],
        [chart('La forme linéaire sur un diamètre optimisant','Paramètre t du point tx_max','ℓθ(tx_max)',series('th',t,t*h)),
         chart('Une suite intérieure qui approche le supremum','N','Valeur',series('(1−1/N)h',ks,(1-1/ks)*h),series('Supremum h',ks,np.full_like(ks,h,dtype=float)))],
        _geometry('Les points de support de l’ellipse',description,paths=[outline,_path('Diamètre optimisant',[-vertex,vertex],False,False,2)],points=optimizer_markers+[dict(x=float(approach[0]),y=float(approach[1]),label='Point intérieur',colorIndex=2)],discs=excluded_markers,bounds=[-a*1.25,a*1.25,-b*1.25,b*1.25],support_point=vertex,approach_point=approach,boundary_included=closed),
        ['1. Écrire x=aX, y=bY ; la contrainte devient X²+Y²≤1 (ou <1).',
         '2. Cauchy–Schwarz donne ℓθ(x,y)≤√(a²cos²θ+b²sin²θ)=h.',
         '3. L’égalité a lieu au point (a²cosθ/h,b²sinθ/h), situé sur la frontière. Le minimum est le point opposé.',
         '4. Sur le domaine fermé, une fonction continue sur un compact atteint ses bornes.',
         '5. Sur l’intérieur, les points (1−1/N)x_max approchent h sans jamais l’atteindre : être borné ne suffit pas.'],
        ['La forme linéaire est non nulle puisque sa direction est un vecteur unitaire.','Le remplissage du dessin représente le domaine ; la frontière tracée est exclue dans le cas ouvert, comme le précise la légende.'])


def heine_continuite(p):
    family=p['family']; R=float(p['R']); n=int(p['n'])
    ranks=np.unique(np.geomspace(1,n,max(2,min(180,n))).astype(int))
    if family=='chirp':
        x=np.linspace(-R,R,601); y=np.sin(x*x)
        xs=np.sqrt(2*math.pi*ranks); ys=np.sqrt(2*math.pi*ranks+math.pi/2)
        gaps=(math.pi/2)/(xs+ys)
        xn=math.sqrt(2*math.pi*n); yn=math.sqrt(2*math.pi*n+math.pi/2)
        gap=(math.pi/2)/(xn+yn)
        metrics=[metric('Constante Lipschitz certifiée sur [−R,R]',2*R),metric('Écart xₙ−yₙ en valeur absolue',gap),metric('Écart exact des images',1),metric('Continuité uniforme sur ℝ','Non'),metric('xₙ',xn),metric('yₙ',yn)]
        graphs=[chart('Un compact protège la continuité uniforme','x','sin(x²)',series('f(x)',x,y)),chart('Les arguments se rapprochent, les images restent séparées','n','Écart',series('|yₙ−xₙ|',ranks,gaps),series('|f(yₙ)−f(xₙ)|',ranks,np.ones_like(ranks)))]
        steps=['1. Sur [−R,R], |f′(x)|=|2x cos(x²)|≤2R : |f(x)−f(y)|≤2R|x−y|.',
               '2. La compacité et la continuité suffisent aussi par le théorème de Heine ; la dérivée fournit ici un module explicite.',
               '3. Sur ℝ, choisir xₙ=√(2πn), yₙ=√(2πn+π/2). Alors f(xₙ)=0 et f(yₙ)=1 exactement.',
               '4. La différence des arguments vaut (π/2)/(xₙ+yₙ)→0 ; celle des images reste 1. Cela exclut la continuité uniforme sur ℝ.']
        description='Deux points témoins très éloignés du compact dessiné peuvent se rapprocher sans que leurs images se rapprochent.'
        extra=dict(witness_x=xn,witness_y=yn,witness_values=[0,1],witness_gap=gap)
    else:
        x=np.linspace(0,1,501); y=np.sqrt(x); gap=1/n**2
        metrics=[metric('Module de continuité ω(δ)',f'√δ'),metric('Écart exact des arguments',gap),metric('Écart exact des images',1/n),metric('Quotient de Lipschitz sur la paire',n),metric('Uniformément continue sur [0,1]','Oui'),metric('Lipschitz sur [0,1]','Non')]
        graphs=[chart('Un module de Hölder à l’origine','x','√x',series('f(x)',x,y)),chart('Un quotient qui exclut une constante Lipschitz','n','Quotient / écart',series('|f(1/n²)−f(0)|',ranks,1/ranks),series('Quotient = n',ranks,ranks))]
        steps=['1. Pour x,y≥0, |√x−√y|≤√|x−y| : un module de continuité indépendant du point vaut ω(δ)=√δ.',
               '2. Choisir δ=ε² prouve la continuité uniforme sur [0,1].',
               '3. Avec xₙ=0 et yₙ=1/n², le quotient |√yₙ−√xₙ|/|yₙ−xₙ| vaut n.',
               '4. Aucune constante Lipschitz finie ne convient. La continuité uniforme est donc strictement plus faible.']
        description='Le voisinage de zéro admet le module √δ, mais aucun module linéaire Cδ sur l’intervalle entier.'
        extra=dict(witness_x=0,witness_y=gap,witness_values=[0,1/n],witness_gap=gap)
    return result(metrics,graphs,scene('functions','Des témoins et un module explicite',description,**extra),steps,
                  ['Les écarts entre témoins sont calculés analytiquement, sans soustraire deux racines très proches.','Un contre-exemple sur ℝ ne contredit pas Heine : les témoins de sin(x²) sortent de tout compact fixé.'])


def minkowski_support(a,b,s,theta,phi):
    h,point=ellipse_support(a,b,phi)
    v=np.array([math.cos(theta),math.sin(theta)])
    scalar=math.cos(phi-theta)
    offset=s*(1 if scalar>=0 else -1)*v
    return h+s*abs(scalar),point+offset


def image_compacte(p):
    a=float(p['a']); b=float(p['b']); s=float(p['length']); theta=math.radians(float(p['theta'])); phi=math.radians(float(p['direction']))
    v=np.array([math.cos(theta),math.sin(theta)])
    angles=np.sort(np.r_[np.linspace(0,2*math.pi,361),np.mod(theta+math.pi/2,2*math.pi),np.mod(theta+3*math.pi/2,2*math.pi)])
    points=[]
    for angle in angles:
        _,u=ellipse_support(a,b,float(angle)); c=math.cos(angle-theta)
        if abs(c)<1e-12:
            # Doubler le point normal : l'arête du segment apparaît exactement.
            derivative=-math.sin(angle-theta)
            points.extend([u+s*(-1 if derivative>0 else 1)*v,u+s*(1 if derivative>0 else -1)*v])
        else:points.append(u+s*np.sign(c)*v)
    h,support_point=minkowski_support(a,b,s,theta,phi)
    aa=np.linspace(0,2*math.pi,501)
    he=np.sqrt((a*np.cos(aa))**2+(b*np.sin(aa))**2); hs=s*np.abs(np.cos(aa-theta))
    area=math.pi*a*b+4*s*math.hypot(a*math.sin(theta),b*math.cos(theta))
    ex=a+s*abs(v[0]); ey=b+s*abs(v[1])
    return result(
        [metric('Appui exact dans la direction φ',h),metric('Aire exacte de A+B',area),metric('Produit A×B compact','Oui'),metric('Somme A+B compacte','Oui'),metric('Somme A+B convexe','Oui'),metric('Abscisse du point de support',float(support_point[0]))],
        [chart('La fonction d’appui transforme la somme en addition','Angle de la normale (°)','Appui h',series('Ellipse h_A',np.degrees(aa),he),series('Segment h_B',np.degrees(aa),hs),series('Somme h_A+h_B',np.degrees(aa),he+hs))],
        _geometry('Image continue d’un produit de compacts','Le stade elliptique est A+B={a+b : a∈A,b∈B}. Les deux côtés plats sont les images des segments de support.',paths=[_path('A+B',points,True,True,0),_path('Ellipse A',_ellipse(a,b),True,False,1),_path('Segment B',[-s*v,s*v],False,False,2)],points=[dict(x=float(support_point[0]),y=float(support_point[1]),label='Support φ',colorIndex=3)],bounds=[-ex*1.2,ex*1.2,-ey*1.2,ey*1.2],support_point=support_point,area=area),
        ['1. A est l’ellipse pleine fermée ; B={tv : |t|≤s} est un segment. Ils sont fermés et bornés en dimension finie, donc compacts.',
         '2. Pour toute suite (aₙ,bₙ) du produit, extraire d’abord aφ(n), puis extraire bφ(ψ(n)) de cette sous-suite ; les deux composantes convergent avec les mêmes indices.',
         '3. L’application continue (a,b)↦a+b envoie ce produit compact sur A+B : la somme est compacte.',
         '4. L’appui h_A+B(u)=max u·(a+b)=h_A(u)+h_B(u), car les deux maximisations sont indépendantes.',
         '5. L’aire de l’ellipse augmente de la longueur 2s du segment multipliée par la largeur perpendiculaire 2√(a²sin²θ+b²cos²θ).'],
        ['La courbe de l’ellipse est échantillonnée pour le dessin ; les fonctions d’appui, la convexité et la compacité sont établies exactement.','Aux normales perpendiculaires au segment, le point de support n’est pas unique ; tout un segment réalise le même maximum.'])


def dense_matrix(n,kappa,seed):
    rng=np.random.default_rng(int(seed))
    Q,_=np.linalg.qr(rng.normal(size=(n,n))); P,_=np.linalg.qr(rng.normal(size=(n,n)))
    sigmas=np.geomspace(float(kappa),1.,n)
    return (Q*sigmas)@P.T


def applications_lineaires(p):
    n=int(p['dimension']); kappa=float(p['condition']); seed=int(p['seed']); A=dense_matrix(n,kappa,seed)
    U,s,Vt=np.linalg.svd(A); norm1=float(np.max(np.sum(np.abs(A),axis=0))); norminf=float(np.max(np.sum(np.abs(A),axis=1))); norm2=float(s[0])
    x=Vt[0]; Ax=A@x; residual=float(np.linalg.norm(Ax-s[0]*U[:,0]))
    rng=np.random.default_rng(seed+333); samples=rng.normal(size=(n,300)); samples/=np.linalg.norm(samples,axis=0)
    ratios=np.linalg.norm(A@samples,axis=0)
    t=np.linspace(0,2*math.pi,401)
    return result(
        [metric('Dimension réelle du problème',n),metric('Norme d’opérateur 1',norm1),metric('Norme d’opérateur 2',norm2),metric('Norme d’opérateur ∞',norminf),metric('Conditionnement euclidien',float(s[0]/s[-1])),metric('Résidu du vecteur optimisant',residual)],
        [chart('Spectre singulier d’une matrice dense','Indice j','σⱼ',_dots('Valeurs singulières',np.arange(1,n+1),s)),
         chart('Tous les vecteurs tests restent sous la norme','Vecteur test','‖Ax‖₂ pour ‖x‖₂=1',_dots('300 directions',np.arange(1,301),ratios),series('Norme atteinte σ₁',[1,300],[norm2,norm2]))],
        _geometry('Image d’un cercle dans le plan singulier dominant','Le cercle est dans span(v₁,v₂) de ℝⁿ et son image est représentée dans span(u₁,u₂). Les calculs de normes utilisent la matrice complète.',paths=[_path('Cercle source',np.column_stack((np.cos(t),np.sin(t))),True,False,1),_path('Image dans le plan singulier',np.column_stack((s[0]*np.cos(t),s[1]*np.sin(t))),True,True,0)],points=[dict(x=float(s[0]),y=0,label='σ₁u₁',colorIndex=2)],bounds=[-s[0]*1.15,s[0]*1.15,-max(1,s[1])*1.15,max(1,s[1])*1.15],matrix=A,singular_values=s,right_optimizer=x,image_optimizer=Ax),
        ['1. Générer A=Q diag(σ₁,…,σₙ)Pᵀ avec Q et P orthogonales et σ₁/σₙ=κ ; la matrice est dense et inversible.',
         '2. Les formules exactes sont ‖A‖₁=maxⱼ∑ᵢ|aᵢⱼ| et ‖A‖∞=maxᵢ∑ⱼ|aᵢⱼ|.',
         '3. La norme euclidienne vaut σ₁=√λ_max(AᵀA). Le vecteur singulier droit v₁ la réalise : ‖Av₁‖₂=σ₁.',
         '4. Pour toute norme choisie, ‖Ax−Ay‖≤‖A‖‖x−y‖ prouve la continuité et même le caractère lipschitzien.',
         '5. Sur la sphère unité compacte de dimension finie, une fonction continue atteint son maximum ; cette étape explique le supremum réalisé.'],
        ['La SVD, les vecteurs tests et les normes portent sur la dimension n affichée. Le dessin dans deux plans singuliers est une coupe représentative.','Les 300 vecteurs tests ne définissent pas la norme : sa valeur provient de la SVD et des formules de sommes.'])


def normes_dimension_infinie(p):
    N=int(p['N'])
    x=np.unique(np.r_[np.linspace(0,1,351),1-np.geomspace(1e-8,1,181)])
    selected=np.unique([1,2,5,max(1,N//3),N]); curves=[series(f'x^{j}',x,x**j) for j in selected]
    ns=np.unique(np.r_[np.arange(1,min(N,70)+1),np.linspace(1,N,min(300,N),dtype=int)])
    return result(
        [metric('Norme uniforme exacte',1),metric('Norme L¹ exacte',1/(N+1)),metric('Norme L² exacte',1/math.sqrt(2*N+1)),metric('Rapport ‖f_N‖∞ / ‖f_N‖₁',N+1),metric('Rapport ‖f_N‖∞ / ‖f_N‖₂',math.sqrt(2*N+1)),metric('Équivalence sur C([0,1])','Non')],
        [chart('Une masse concentrée près du bord','x∈[0,1]','fₙ(x)',*curves),
         chart('Trois normes, trois comportements','Exposant n','Norme',series('Uniforme : 1',ns,np.ones_like(ns)),series('L¹ : 1/(n+1)',ns,1/(ns+1)),series('L² : 1/√(2n+1)',ns,1/np.sqrt(2*ns+1)))],
        scene('functions','Un contre-exemple en dimension infinie','Les normes sont calculées par intégration exacte ; le maillage sert uniquement à voir la concentration près de x=1.',exact_norms=dict(sup=1,L1=1/(N+1),L2=1/math.sqrt(2*N+1))),
        ['1. Chaque fₙ(x)=xⁿ est continue et vaut 1 en x=1, donc ‖fₙ‖∞=1.',
         '2. L’intégration exacte donne ‖fₙ‖₁=∫₀¹xⁿdx=1/(n+1) et ‖fₙ‖₂=(∫₀¹x²ⁿdx)¹ᐟ²=1/√(2n+1).',
         '3. Si ‖f‖∞≤C‖f‖₁ pour tout f∈C([0,1]), alors n+1≤C pour tout n, impossible. Le même raisonnement vaut pour L².',
         '4. Les normes intégrales tendent vers zéro mais la norme uniforme reste 1 : les topologies ne sont pas identiques.',
         '5. Cela ne contredit pas l’équivalence des normes sur un sous-espace de dimension finie fixé : les degrés n ne sont pas bornés ici.'],
        ['Sur les fonctions continues, les normes L¹ et L² sont bien des normes : une fonction continue nulle presque partout est identiquement nulle.','La limite simple vaut 0 sur [0,1[ et 1 en x=1 ; elle est discontinue, donc la convergence ne peut pas être uniforme.'])


def boule_non_compacte(p):
    M=int(p['M']); n=int(p['probe']); x=np.linspace(0,2*math.pi,601)
    amplitude=1/math.sqrt(2*math.pi)
    gram=np.eye(M)
    difference=np.abs(amplitude*np.exp(1j*n*x)-amplitude*np.exp(1j*(n+1)*x))
    return result(
        [metric('Norme L² exacte de chaque vₙ',1),metric('Distance L² exacte entre modes distincts',math.sqrt(2)),metric('Nombre de modes de Gram affichés',M),metric('Rang exact de Gram',M),metric('Boule unité compacte','Non'),metric('Sous-suite de Cauchy de (vₙ)','Aucune')],
        [chart('Un mode complexe est formé de deux fonctions réelles','x∈[0,2π]','vₙ(x)',series('Partie réelle',x,amplitude*np.cos(n*x)),series('Partie imaginaire',x,amplitude*np.sin(n*x))),
         chart('Deux modes voisins restent séparés en norme','x∈[0,2π]','|vₙ(x)−vₙ₊₁(x)|',series('Écart ponctuel',x,difference))],
        scene('matrix','La matrice de Gram des modes','La diagonale vaut 1 et les termes hors diagonale valent 0 par intégration exacte. Une matrice finie illustre la formule valable pour tous les indices.',matrix=gram,labels=[str(j) for j in range(M)],mode=n),
        ['1. Définir vₙ(x)=eⁱⁿˣ/√(2π) dans l’espace des fonctions continues muni de la norme L² sur [0,2π].',
         '2. ⟨vₙ,vₘ⟩=(1/2π)∫₀²πeⁱ⁽ⁿ⁻ᵐ⁾ˣdx vaut 1 si n=m et 0 sinon.',
         '3. Pour n≠m, ‖vₙ−vₘ‖₂²=1+1−0=2. Tous les termes sont pourtant dans la boule unité fermée.',
         '4. Une extraction conserve des indices distincts, donc la distance √2 : aucune sous-suite n’est de Cauchy, aucune ne converge.',
         '5. La boule unité n’est pas compacte. Le théorème « fermé et borné ⇒ compact » exige la dimension finie.'],
        ['La preuve concerne une infinité de modes et ne dépend pas du nombre M affiché.','L’espace de fonctions continues muni de L² est un espace normé ; sa complétion usuelle est L². Le contre-exemple s’applique aux deux espaces.'])


MODELS={name:globals()[name] for name in ('bolzano_weierstrass','extraction_aleatoire','cauchy_rationnels','compacts_recouvrements','valeurs_extremes','heine_continuite','image_compacte','applications_lineaires','normes_dimension_infinie','boule_non_compacte')}


def calculate(lab_id,p):
    return MODELS[lab_id](p)
