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
        [chart('Séparer les termes pairs et impairs','Indice n dans la suite initiale','uₙ',_dots('Termes pairs',even,values[even]),_dots('Termes impairs',odd,values[odd]),series('Limite des termes pairs : 1',ns,np.ones_like(ns)),series('Limite des termes impairs : −1',ns,-np.ones_like(ns))),
         chart('Garantir une erreur inférieure à ε','Indice n','Erreur de la suite extraite correspondante',series('Erreur exacte : 1/(n+1)',ns,errors),series('Erreur demandée ε',ns,np.full_like(ns,eps,dtype=float)))],
        _geometry('Deux suites extraites de la même suite','Les deux couleurs montrent les termes pairs et impairs. Chaque couleur se rapproche d’une limite différente : la suite entière ne peut pas converger.',points=points,bounds=[-1,min(N+1,82),-1.4,2.3],subsequences=[dict(indices=even,values=values[even],limit=1),dict(indices=odd,values=values[odd],limit=-1)]),
        ['1. Commencer par une borne valable pour tous les indices n≥0 : −1<uₙ≤2. La suite est donc bornée, comme dans une étude de suite en MPSI.',
         '2. Garder les indices 2k, puis les indices 2k+1. Dans les deux cas les indices augmentent strictement : on a bien deux suites extraites, et k est leur propre indice.',
         '3. Calculer u₂ₖ=1+1/(2k+1) et u₂ₖ₊₁=−1+1/(2k+2). Les limites 1 et −1 sont des valeurs d’adhérence, c’est-à-dire des limites de suites extraites. Leur différence exclut une limite de la suite entière.',
         f'4. Relier la définition de la limite au calcul d’un rang : pour une erreur <ε={eps:g}, k≥{rank_even} suffit pour les pairs et k≥{rank_odd} pour les impairs. Augmenter N permet de voir les termes correspondants.'],
        ['N règle uniquement le nombre de termes dessinés ; les limites sont établies pour tous les indices par leurs formules.','Lien MPSI : Bolzano–Weierstrass assure qu’une suite réelle bornée possède une suite extraite convergente. En MP, cette propriété sert à définir les parties compactes ; plusieurs valeurs d’adhérence restent possibles.'])


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
    probability_display=probability if probability>0 else f'10^({log_probability:.3f}) : trop petit pour l’écriture décimale de l’ordinateur'
    return result(
        [metric('Nouveaux records stricts',len(indices)),metric('Dernier indice retenu',int(indices[-1])),metric('Dernière distance à 1',float(distances[-1])),metric('Espérance exacte de D_N',nearest_expectation(N)),metric('Probabilité exacte D_N>d',probability_display),metric('Fréquence expérimentale D_N>d',float(np.mean(minima>d)))],
        [chart('Garder seulement les rapprochements strictement meilleurs','Indice j du tirage','Distance |Xⱼ−1|',_dots('Tirages représentés',show,np.abs(xs[show]-1)),_dots('Nouveaux records retenus',indices,distances)),
         chart('Les valeurs de la suite extraite','Rang k dans la suite extraite','Xφ(k)',_dots('Termes gardés',np.arange(len(indices)),xs[indices]),series('Valeur visée : 1',[0,max(1,len(indices)-1)],[1,1])),
         chart('Prolongement : comparer les meilleurs rapprochements','Distance ramenée à l’échelle w=2ND_N/3','Densité',_dots('Fréquences des expériences',centers,density),series('Densité calculée par la loi',w,exact),series('Densité limite lorsque N augmente : e⁻ʷ',w,np.exp(-w)))],
        _geometry('Lire les indices de la suite extraite','Un point indique un nouveau record de proximité à 1, avec l’indice du tirage initial. Les termes affichés permettent d’étudier l’algorithme ; ils ne prouvent pas à eux seuls une convergence.',points=[dict(x=int(i),y=float(x),label=f'j={i}',colorIndex=0) for i,x in zip(indices,xs[indices])],bounds=[-N*.03,N*1.03,-.1,3.1],record_indices=indices,record_values=xs[indices],distances=distances,trial_minima=minima,log10_survival=log_probability),
        ['1. Tirer N nombres Xⱼ indépendants entre 0 et 3. La graine fixe les mêmes tirages pour refaire une expérience ; d fixe le rayon du voisinage ]1−d,1+d[.',
         '2. Garder le tirage d’indice j seulement si |Xⱼ−1| améliore strictement tous les records précédents. Les indices augmentent : on construit une suite extraite au sens du cours MPSI.',
         '3. En prolongement probabiliste, D_N=min|Xⱼ−1| est le meilleur rapprochement parmi N tirages. Pour 0≤d≤1, un tirage évite le voisinage avec probabilité 1−2d/3 ; l’indépendance donne P(D_N>d)=(1−2d/3)ᴺ.',
         '4. La conclusion pour une suite infinie demande une preuve supplémentaire : D_N décroît et P(D_N>ε)→0. Pour les rayons ε=1/k, puis tous les rayons, cela établit D_N→0 avec probabilité 1, ce qu’on appelle presque sûrement.',
         '5. Avec probabilité 1, aucun tirage ne vaut exactement 1, mais les rapprochements deviennent arbitrairement petits : il existe alors une infinité de nouveaux records, et la suite extraite tend vers 1.'],
        ['Lien au TP : une suite bornée et des indices d’extraction. Les variables aléatoires à densité, la loi uniforme continue et la convergence presque sûre sont ici des prolongements, et non des connaissances exigibles en MPSI/MP.','N est fini dans le programme. La preuve avec probabilité 1 concerne une suite infinie de tirages indépendants ; l’histogramme ne remplace pas cette preuve.','Chaque expérience de l’histogramme a ses propres tirages. Sur 0≤w≤6, la densité correspond à d≤1 puisque N≥100 ; les fréquences hors de cette fenêtre restent hors du dessin.'])


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
    lines=[f'u{k}={u}' if k<=4 else f'u{k} : numérateur exact écrit avec {len(str(u.numerator))} chiffres' for k,u in enumerate(values)]
    return result(
        [metric('Valeur approchée de uₙ',float(values[-1])),metric('Erreur uₙ−√2 : majorant calculé exactement',tail),metric('uₙ²−2 est strictement positif','Oui'),metric('Tous les termes appartiennent à ℚ','Oui'),metric('Limite dans ℚ','Non'),metric('Tous les termes après n sont proches à ε','Oui' if bounds[-1]<Fraction(str(epsilon)) else 'Pas encore à ce rang')],
        [chart('Une suite récurrente décroissante vers √2','Rang n','Valeur de uₙ',_dots('Fractions rationnelles',ns,numerical),series('Limite réelle : √2',[0,max(n,1)],[math.sqrt(2)]*2)),
         chart('Garantir une précision par une majoration','Rang n','Borne de l’erreur |uₙ−√2|',_dots('Majorant : (uₙ²−2)/uₙ',ns,upper),series('Erreur demandée ε',[0,max(n,1)],[epsilon]*2))],
        _geometry('La limite peut sortir de l’ensemble des rationnels','Chaque terme est une fraction exacte. Les valeurs arrondies finissent par ressembler à √2, alors que le calcul fractionnaire garde toujours uₙ²−2>0.',points=[dict(x=k,y=float(u),label=f'u{k}',colorIndex=0) for k,u in enumerate(values)],bounds=[-.5,max(1,n)+.5,1.35,2.1],fractions=fractions,fraction_labels=lines),
        ['1. Étudier la récurrence comme en MPSI : les opérations gardent les termes dans ℚ et uₙ>√2. La différence uₙ₊₁−uₙ=(2−uₙ²)/(2uₙ)<0 prouve la décroissance ; une suite décroissante minorée converge.',
         '2. Poser eₙ=uₙ−√2. L’identité eₙ₊₁=eₙ²/(2uₙ) explique pourquoi l’erreur diminue très vite : elle est élevée au carré à chaque étape.',
         '3. Pour q≥p, 0≤u_p−u_q≤u_p−√2<(u_p²−2)/u_p. Ce majorant tend vers zéro : tous les termes assez tardifs sont proches deux à deux. C’est la condition de Cauchy, étudiée ici en prolongement.',
         '4. Une écriture √2=a/b en fraction irréductible imposerait a puis b pairs, car a²=2b². Cette contradiction prouve l’irrationalité de la limite. Les fractions restent dans ℚ, mais leur limite n’y est pas.',
         f'5. Comparer la fraction exacte au rang n={n} avec sa valeur arrondie : {values[-1]}.'],
        ['Lien MPSI : invariance d’un intervalle, monotonie, limite d’une suite récurrente et preuve de l’irrationalité de √2. Les suites de Cauchy, la complétude et les espaces de Banach sont explicitement hors programme MP.','Le prolongement dit que ℚ est incomplet : une suite de Cauchy de rationnels peut ne pas avoir de limite rationnelle. La preuve utilise les fractions exactes ; les décimales affichées peuvent être limitées par les arrondis de l’ordinateur.'])


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
        [metric('[0,1] couvert par les ouverts','Oui' if covered else 'Non'),metric('Seuil strict du rayon',threshold),metric('Marge de couverture δ garantie',margin),metric('Nombre d’intervalles ouverts placés',m+1),metric('Point hors de U₁∪…∪U_N',outside),metric('Borne droite exclue de l’union finie',float(ends[-1]))],
        [chart('Combien d’intervalles contiennent chaque point ?','x∈[0,1]','Nombre d’intervalles',series('Comptage aux points dessinés',x,counts),_dots('Milieux entre deux centres',witnesses,midpoint_counts)),
         chart('Pourquoi aucun nombre fini de Uₙ ne suffit','Indice n de l’ouvert Uₙ','Extrémité droite, exclue de Uₙ',_dots('1−1/n',ns,ends),series('Valeur limite : 1',[1,N],[1,1]))],
        _geometry('Les traces sur l’axe sont des intervalles ouverts','Chaque disque représente le voisinage de rayon r autour d’un point j/m. Sa trace sur l’axe est ]j/m−r,j/m+r[. Le bord pointillé est exclu : au seuil r=1/(2m), les milieux restent découverts.',paths=[_path('Segment fermé [0,1]',[[0,0],[1,0]],False,False,3)],discs=discs,points=[dict(x=float(c),y=0,label=f'{j}/{m}',colorIndex=3) for j,c in enumerate(centers)],bounds=[-r-.05,1+r+.05,-max(.2,r*1.3),max(.2,r*1.3)],uncovered_witnesses=[] if covered else witnesses),
        ['1. Placer les centres 0,1/m,…,1. Les milieux entre deux centres sont les points les plus éloignés du réseau : leur distance vaut 1/(2m). Cette formule permet de vérifier tous les points du segment.',
         '2. Un intervalle ouvert exclut ses extrémités. Avec r=1/(2m), les intervalles se touchent seulement à des points qui ne leur appartiennent pas ; il faut r>1/(2m) pour couvrir [0,1].',
         '3. Lorsque δ=r−1/(2m)>0, toute partie de [0,1] de diamètre <δ entre dans un des intervalles. C’est une marge commune de couverture, appelée ici marge de Lebesgue en prolongement.',
         '4. Comparer avec Uₙ=]−1,1−1/n[ : chaque x<1 finit par appartenir à Uₙ, donc cette famille couvre [0,1[. Comme les Uₙ grandissent, un choix fini est contenu dans le dernier U_N retenu.',
         f'5. Trouver un point qui échappe à ce choix fini : x_N=1−1/(2N)={outside:g} est dans [0,1[, mais hors de U_N. Aucun choix fini de ces ouverts ne couvre donc [0,1[.'],
        ['Lien MP : [0,1] est fermé et borné dans ℝ, donc compact ; [0,1[ n’est pas fermé. Le critère de compacité au programme est celui des suites extraites. La propriété par recouvrements de Borel–Lebesgue est hors programme MP et constitue ici un prolongement.','La formule r>1/(2m) décide la couverture de tout le segment. Un dessin qui paraît rempli, ou une vérification sur quelques points, ne suffit pas à prouver un recouvrement.'])


def ellipse_support(a,b,theta):
    c=math.cos(theta); s=math.sin(theta); h=math.hypot(a*c,b*s)
    return h,np.array([a*a*c/h,b*b*s/h])


def valeurs_extremes(p):
    a=float(p['a']); b=float(p['b']); theta=math.radians(float(p['theta'])); N=int(p['N']); closed=p['domain']=='closed'
    h,vertex=ellipse_support(a,b,theta); approach=(1-1/N)*vertex
    t=np.linspace(-1,1,401); ks=np.arange(2,max(20,N)+1)
    description='Le maximum et le minimum sont réalisés sur le bord, qui appartient au domaine fermé.' if closed else 'Les deux points creux du bord ne sont pas dans le domaine : les bornes supérieure et inférieure ne sont pas atteintes. Le point plein est intérieur et approche la borne supérieure.'
    ellipse=_ellipse(a,b)
    outline=_path('Frontière de l’ellipse',ellipse,True,True,0)
    outline['boundaryClosed']=closed
    optimizer_markers=[dict(x=float(vertex[0]),y=float(vertex[1]),label='max',colorIndex=1),dict(x=float(-vertex[0]),y=float(-vertex[1]),label='min',colorIndex=1)] if closed else []
    excluded_markers=[] if closed else [dict(x=float(sign*vertex[0]),y=float(sign*vertex[1]),r=.025,fill=False,closed=False,label='Point de la borne supérieure : exclu' if sign==1 else 'Point de la borne inférieure : exclu',colorIndex=1) for sign in (1,-1)]
    return result(
        [metric('Borne supérieure exacte de ℓθ',h),metric('Borne inférieure exacte de ℓθ',-h),metric('Maximum et minimum atteints','Oui' if closed else 'Non'),metric('Valeur au point d’approche',(1-1/N)*h),metric('Écart exact à la borne supérieure',h/N),metric('Domaine compact','Oui' if closed else 'Non')],
        [chart('Lire ℓθ sur le diamètre des points extrémaux','t : position du point tx_max','ℓθ(tx_max)',series('Valeur th',t,t*h)),
         chart('Approcher la borne supérieure depuis l’intérieur','Rang N de la suite','Valeur de ℓθ',series('Valeur intérieure : (1−1/N)h',ks,(1-1/ks)*h),series('Borne supérieure h',ks,np.full_like(ks,h,dtype=float)))],
        _geometry('Où les bornes de la forme linéaire sont-elles réalisées ?',description,paths=[outline,_path('Diamètre des points extrémaux',[-vertex,vertex],False,False,2)],points=optimizer_markers+[dict(x=float(approach[0]),y=float(approach[1]),label='Point intérieur',colorIndex=2)],discs=excluded_markers,bounds=[-a*1.25,a*1.25,-b*1.25,b*1.25],support_point=vertex,approach_point=approach,boundary_included=closed),
        ['1. Définir ℓθ(x,y)=x cosθ+y sinθ. L’ellipse pleine vérifie x²/a²+y²/b²≤1 ; pour son intérieur seul, remplacer ≤ par <. Poser x=aX et y=bY ramène le calcul au disque unité.',
         '2. Cauchy–Schwarz donne ℓθ(x,y)≤h=√(a²cos²θ+b²sin²θ). Cette valeur est le plus petit majorant possible : la borne supérieure. De même, −h est le plus grand minorant : la borne inférieure.',
         '3. Le point x_max=(a²cosθ/h,b²sinθ/h) du bord réalise h quand il appartient au domaine ; son opposé réalise −h. Une borne atteinte est respectivement un maximum ou un minimum.',
         '4. Sur l’ellipse pleine avec son bord, le domaine est fermé et borné dans ℝ², donc compact. Le théorème MP des bornes atteintes s’applique à la fonction continue ℓθ.',
         '5. Sans le bord, (1−1/N)x_max reste intérieur et sa valeur tend vers h, avec erreur h/N. La borne supérieure existe donc encore, mais aucun point du domaine ne la réalise : aucun maximum.'],
        ['Lien MPSI : majorant, minorant, borne supérieure et borne inférieure. Lien MP : Cauchy–Schwarz, continuité et bornes atteintes sur un compact. La forme linéaire n’est jamais nulle, puisque (cosθ,sinθ) est un vecteur unitaire.','Le choix avec ou sans bord change l’hypothèse de compacité : un ensemble borné ouvert n’est pas compact ici. Le bord pointillé et les points creux représentent des points exclus.'])


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
        graphs=[chart('Sur un segment, contrôler les variations de sin(x²)','x','sin(x²)',series('f(x)',x,y)),chart('Deux points proches dont les images restent éloignées','Rang n','Écart',series('Distance des points : |yₙ−xₙ|',ranks,gaps),series('Écart des images : |f(yₙ)−f(xₙ)|',ranks,np.ones_like(ranks)))]
        steps=['1. Sur le segment [−R,R], |f′(x)|=|2x cos(x²)|≤2R. L’inégalité des accroissements finis donne |f(x)−f(y)|≤2R|x−y| : c’est une technique MPSI de contrôle des variations.',
               '2. Pour une erreur ε>0, choisir δ=ε/(2R). Ce rayon convient pour tous les couples de points du segment. C’est la continuité uniforme, que le théorème MP de Heine garantit aussi parce que le segment est compact.',
               '3. Pour tester la même propriété sur tout ℝ, choisir xₙ=√(2πn) et yₙ=√(2πn+π/2). Leurs images valent exactement 0 et 1.',
               '4. La distance (π/2)/(xₙ+yₙ) tend vers zéro, tandis que l’écart des images reste 1. Aucun rayon δ ne convient partout sur ℝ pour une erreur ε<1 : la continuité uniforme y échoue.']
        description='Quand n augmente, les deux points xₙ et yₙ se rapprochent et sortent de tout segment fixé. Leurs images restent 0 et 1 : ce sont les témoins qui réfutent la continuité uniforme sur ℝ.'
        extra=dict(witness_x=xn,witness_y=yn,witness_values=[0,1],witness_gap=gap)
    else:
        x=np.linspace(0,1,501); y=np.sqrt(x); gap=1/n**2
        metrics=[metric('Module de continuité ω(δ)',f'√δ'),metric('Écart exact des arguments',gap),metric('Écart exact des images',1/n),metric('Quotient de Lipschitz sur la paire',n),metric('Uniformément continue sur [0,1]','Oui'),metric('Lipschitz sur [0,1]','Non')]
        graphs=[chart('√x près de zéro : variations contrôlées','x','√x',series('f(x)',x,y)),chart('Le quotient variation / distance devient non borné','Rang n','Quotient ou écart',series('Écart des images : |f(1/n²)−f(0)|',ranks,1/ranks),series('Quotient = n',ranks,ranks))]
        steps=['1. Pour x,y≥0, l’inégalité |√x−√y|≤√|x−y| donne une borne commune des variations. On note parfois ω(δ)=√δ ce module de continuité, c’est-à-dire la borne associée à une distance δ.',
               '2. Pour obtenir un écart des images <ε, la condition |x−y|<ε² suffit partout sur [0,1]. Un même δ=ε² convient donc pour tous les points : la fonction est uniformément continue.',
               '3. Une propriété lipschitzienne demanderait un L unique dans |f(x)−f(y)|≤L|x−y|. Pour xₙ=0 et yₙ=1/n², le quotient variation / distance vaut n.',
               '4. Comme n est arbitrairement grand, aucune constante L finie ne convient. Cet exemple distingue bien la continuité uniforme d’une majoration lipschitzienne.']
        description='Près de zéro, une distance δ entre les arguments donne un écart au plus √δ entre leurs racines. Cette borne assure la continuité uniforme, même si aucun multiple Lδ ne convient sur tout le segment.'
        extra=dict(witness_x=0,witness_y=gap,witness_values=[0,1/n],witness_gap=gap)
    return result(metrics,graphs,scene('functions','Un même rayon δ convient-il pour tous les points ?',description,**extra),steps,
                  ['Lien MPSI : continuité et inégalité des accroissements finis. Lien MP : définition de la continuité uniforme et théorème de Heine sur un compact. Le module √δ est une borne concrète ; sa lecture comme condition de Hölder est un prolongement de vocabulaire.','La fenêtre [−R,R] et les points comparés ne définissent pas le même domaine : l’échec pour sin(x²) concerne tout ℝ. Les suites de points qui le prouvent quittent chaque compact fixé ; cela respecte les hypothèses de Heine.'])


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
        [metric('Projection maximale dans la direction φ',h),metric('Aire exacte de A+B',area),metric('Produit A×B compact','Oui'),metric('Somme A+B compacte','Oui'),metric('Somme A+B convexe','Oui'),metric('Abscisse du point réalisant la projection',float(support_point[0]))],
        [chart('La plus grande projection de A+B est la somme de celles de A et B','Angle φ de la direction de projection (°)','Projection maximale h',series('Ellipse : h_A',np.degrees(aa),he),series('Segment : h_B',np.degrees(aa),hs),series('Somme : h_A+h_B',np.degrees(aa),he+hs))],
        _geometry('Chaque point de A+B est une somme de deux points','Le domaine bleu est A+B={P+Q : P∈A,Q∈B}. L’ellipse A et le segment B sont tracés comme repères. Le point marqué réalise la plus grande projection sur le vecteur de direction φ.',paths=[_path('Somme A+B',points,True,True,0),_path('Ellipse A',_ellipse(a,b),True,False,1),_path('Segment B',[-s*v,s*v],False,False,2)],points=[dict(x=float(support_point[0]),y=float(support_point[1]),label='Projection maximale, direction φ',colorIndex=3)],bounds=[-ex*1.2,ex*1.2,-ey*1.2,ey*1.2],support_point=support_point,area=area),
        ['1. A est l’ellipse pleine avec son bord. B={tv : |t|≤s} est le segment orienté par v=(cosθ,sinθ). Chacun est fermé et borné dans ℝ², donc compact par le théorème MP en dimension finie.',
         '2. Pour une suite de couples (Pₙ,Qₙ), extraire d’abord les Pₙ convergents. Dans cette même suite d’indices, extraire ensuite les Qₙ convergents. Les Pₙ restent convergents : les deux coordonnées convergent ensemble. C’est la technique des extractions successives.',
         '3. L’addition (P,Q)↦P+Q est continue. Elle envoie le produit compact A×B sur A+B, qui est donc compact. On utilise ici le théorème MP de l’image continue d’un compact.',
         '4. Pour un vecteur unitaire w, la fonction d’appui h_A(w)=max w·P est simplement la plus grande projection des points de A. Comme P et Q se choisissent indépendamment, h_A+B(w)=h_A(w)+h_B(w).',
         '5. En allongeant la figure dans la direction du segment, l’aire ajoutée est sa longueur 2s multipliée par la largeur perpendiculaire de l’ellipse, 2√(a²sin²θ+b²cos²θ). Le calcul de l’appui et de l’aire prolonge le résultat de compacité.'],
        ['Lien MP : produit fini de compacts, extractions successives et image par une application continue. La fonction d’appui est un outil géométrique complémentaire, défini comme une projection maximale ; elle n’est pas nécessaire à la preuve de compacité.','Le contour est dessiné avec un nombre fini de points ; les propriétés viennent des théorèmes et des formules. Perpendiculairement au segment, toute une portion droite du bord réalise le même maximum : le point maximisant n’est pas toujours unique.'])


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
        [metric('Dimension réelle du problème',n),metric('Norme d’opérateur 1',norm1),metric('Norme d’opérateur 2',norm2),metric('Norme d’opérateur ∞',norminf),metric('Conditionnement : gain maximal / minimal',float(s[0]/s[-1])),metric('Erreur numérique sur la direction de gain maximal',residual)],
        [chart('Valeurs singulières : les facteurs d’étirement de A','Indice j','Facteur σⱼ',_dots('Valeurs singulières calculées',np.arange(1,n+1),s)),
         chart('Comparer des directions à la plus grande amplification possible','Numéro du vecteur testé','‖Ax‖₂ avec ‖x‖₂=1',_dots('300 vecteurs unitaires',np.arange(1,301),ratios),series('Gain maximal : σ₁',[1,300],[norm2,norm2]))],
        _geometry('L’application x↦Ax transforme un cercle en ellipse','Le cercle se trouve dans le plan engendré par v₁,v₂, directions fournies par le calcul numérique. Son image est dessinée dans le plan engendré par u₁,u₂. Les longueurs sont multipliées par σ₁ et σ₂ ; les normes utilisent bien toutes les n coordonnées.',paths=[_path('Cercle avant application',np.column_stack((np.cos(t),np.sin(t))),True,False,1),_path('Ellipse image dans le plan choisi',np.column_stack((s[0]*np.cos(t),s[1]*np.sin(t))),True,True,0)],points=[dict(x=float(s[0]),y=0,label='σ₁u₁ : direction du gain maximal',colorIndex=2)],bounds=[-s[0]*1.15,s[0]*1.15,-max(1,s[1])*1.15,max(1,s[1])*1.15],matrix=A,singular_values=s,right_optimizer=x,image_optimizer=Ax),
        ['1. La matrice A=Q diag(σ₁,…,σₙ)Pᵀ applique successivement une transformation orthogonale, des étirements, puis une autre transformation orthogonale. Les facteurs σⱼ>0 sont ses valeurs singulières ; κ compare le plus grand au plus petit.',
         '2. La norme d’opérateur, aussi appelée norme subordonnée, est la plus petite constante C dans ‖Ax‖≤C‖x‖. Pour les normes vectorielles 1 et ∞, les formules sont ‖A‖₁=maxⱼ∑ᵢ|aᵢⱼ| et ‖A‖∞=maxᵢ∑ⱼ|aᵢⱼ|.',
         '3. En norme euclidienne, ‖A‖₂=σ₁=√λ_max(AᵀA). La direction unitaire v₁ réalise ce gain : ‖Av₁‖₂=σ₁. La décomposition en valeurs singulières, abrégée SVD, est ici un outil numérique de calcul et de visualisation en prolongement.',
         '4. Le critère MP de continuité linéaire s’applique : ‖Ax−Ay‖≤‖A‖‖x−y‖. Cette borne contrôle toutes les directions, pas seulement les vecteurs dessinés.',
         '5. La sphère unité est fermée et bornée en dimension finie, donc compacte. Le théorème des bornes atteintes garantit qu’une direction réalise la borne supérieure des gains : c’est un maximum.'],
        ['Lien MPSI : matrice d’une application linéaire et transformations orthogonales. Lien MP : norme subordonnée et critère de continuité linéaire. La SVD et les plans qu’elle fournit servent de prolongement numérique ; aucune maîtrise préalable de cet algorithme n’est demandée.','Le dessin montre deux directions d’un problème de dimension n. Les 300 vecteurs tests illustrent la borne ; ils ne la définissent pas. Les valeurs affichées sont calculées avec les arrondis de l’ordinateur à partir des formules matricielles.'])


def normes_dimension_infinie(p):
    N=int(p['N'])
    x=np.unique(np.r_[np.linspace(0,1,351),1-np.geomspace(1e-8,1,181)])
    selected=np.unique([1,2,5,max(1,N//3),N]); curves=[series(f'x^{j}',x,x**j) for j in selected]
    ns=np.unique(np.r_[np.arange(1,min(N,70)+1),np.linspace(1,N,min(300,N),dtype=int)])
    return result(
        [metric('Norme ∞ : plus grande erreur',1),metric('Norme 1 : erreur absolue moyenne',1/(N+1)),metric('Norme 2 : erreur moyenne quadratique',1/math.sqrt(2*N+1)),metric('Rapport ‖f_N‖∞ / ‖f_N‖₁',N+1),metric('Rapport ‖f_N‖∞ / ‖f_N‖₂',math.sqrt(2*N+1)),metric('Normes équivalentes sur C([0,1])','Non')],
        [chart('L’erreur se concentre près de x=1','x∈[0,1]','fₙ(x), écart à la fonction nulle',*curves),
         chart('Comparer convergence en moyenne et convergence uniforme','Exposant n','Mesure de l’erreur',series('Norme ∞ : 1',ns,np.ones_like(ns)),series('Norme 1 : 1/(n+1)',ns,1/(ns+1)),series('Norme 2 : 1/√(2n+1)',ns,1/np.sqrt(2*ns+1)))],
        scene('functions','Des erreurs moyennes petites, mais une erreur maximale égale à 1','Les normes 1 et 2 mesurent une erreur répartie sur le segment. La norme ∞ cherche la plus grande erreur en un point. Les formules intégrales donnent leurs valeurs indépendamment du nombre de points dessinés.',exact_norms=dict(sup=1,L1=1/(N+1),L2=1/math.sqrt(2*N+1))),
        ['1. Comparer fₙ(x)=xⁿ à la fonction nulle sur [0,1]. La plus grande erreur, appelée norme ∞ ou norme uniforme, vaut 1 car fₙ(1)=1.',
         '2. La norme 1 mesure l’erreur absolue moyenne : ∫₀¹xⁿdx=1/(n+1). La norme 2 mesure l’erreur moyenne quadratique : (∫₀¹x²ⁿdx)¹ᐟ²=1/√(2n+1). Les deux tendent vers zéro.',
         '3. Des normes équivalentes se compareraient avec des constantes indépendantes de la fonction. Une inégalité ‖f‖∞≤C‖f‖₁ imposerait ici n+1≤C pour tout n, impossible ; de même, ‖fₙ‖∞/‖fₙ‖₂=√(2n+1) est non borné.',
         '4. Les fonctions convergent donc vers zéro en moyenne et en moyenne quadratique, mais pas uniformément. Cela relie une convergence à la norme choisie, plutôt qu’à la seule apparence du graphe.',
         '5. Le théorème MP d’équivalence des normes exige une dimension finie fixée. Ici les degrés n augmentent sans limite dans C([0,1]), espace de toutes les fonctions continues : le programme MP demande justement de savoir utiliser une suite pour prouver que deux normes ne sont pas équivalentes.'],
        ['Sur le segment [0,1], de longueur 1, les intégrales correspondent directement aux moyennes. Sur les fonctions continues, elles définissent bien des normes : une intégrale d’une fonction continue positive ne peut être nulle que si cette fonction est identiquement nulle.','Lien MP : normes de convergence uniforme, en moyenne et en moyenne quadratique ; non-équivalence démontrée par une suite ; équivalence en dimension finie. La limite simple vaut 0 pour x<1 et 1 en x=1 : elle est discontinue, donc ne peut pas être une limite uniforme des fonctions continues fₙ.'])


def boule_non_compacte(p):
    M=int(p['M']); n=int(p['probe']); x=np.linspace(0,2*math.pi,601)
    amplitude=1/math.sqrt(2*math.pi)
    gram=np.eye(M)
    difference=np.abs(amplitude*np.exp(1j*n*x)-amplitude*np.exp(1j*(n+1)*x))
    return result(
        [metric('Norme 2 exacte de chaque vₙ',1),metric('Distance en norme 2 entre fonctions distinctes',math.sqrt(2)),metric('Nombre de fonctions comparées dans Gram',M),metric('Rang exact de Gram',M),metric('Boule unité fermée compacte','Non'),metric('Suite extraite convergente de (vₙ)','Aucune')],
        [chart('Lire la fonction complexe à travers son cosinus et son sinus','x∈[0,2π]','vₙ(x)',series('Partie réelle',x,amplitude*np.cos(n*x)),series('Partie imaginaire',x,amplitude*np.sin(n*x))),
         chart('L’écart entre deux fonctions oscillantes voisines','x∈[0,2π]','|vₙ(x)−vₙ₊₁(x)|',series('Écart en chaque point x',x,difference))],
        scene('matrix','Gram : le tableau des produits scalaires','La case (n,m) contient ⟨vₙ,vₘ⟩. Les fonctions sont de norme 1 et orthogonales deux à deux : la diagonale vaut 1, les autres cases 0. Les M fonctions affichées illustrent la même formule pour tous les indices.',matrix=gram,labels=[str(j) for j in range(M)],mode=n),
        ['1. Les fonctions vₙ(x)=eⁱⁿˣ/√(2π) sont continues sur [0,2π]. On les considère comme des vecteurs, avec norme ‖f‖₂=(∫₀²π|f(x)|²dx)¹ᐟ². Le cosinus et le sinus donnent leurs parties réelle et imaginaire.',
         '2. Le produit scalaire intégral donne ⟨vₙ,vₘ⟩=(1/2π)∫₀²πeⁱ⁽ⁿ⁻ᵐ⁾ˣdx : il vaut 1 si n=m et 0 sinon. Le tableau de ces produits s’appelle la matrice de Gram.',
         '3. Pour n≠m, développer la norme carrée de la différence donne ‖vₙ−vₘ‖₂²=1+1−0=2. Les fonctions sont toutes dans la boule unité fermée, mais restent à distance √2 deux à deux.',
         '4. Une suite extraite garde des indices distincts et donc cette même distance. Les termes d’une suite convergente doivent au contraire devenir proches deux à deux : aucune suite extraite ne converge ici.',
         '5. Le critère MP par suites extraites exclut alors la compacité de la boule. Ce prolongement précise pourquoi « fermé et borné ⇒ compact » exige une dimension finie.'],
        ['M fixe seulement la taille du tableau ; la preuve porte sur une infinité de fonctions. Lien MP : norme en moyenne quadratique des fonctions continues et critère de compacité par suites extraites. L’interprétation des produits intégrés comme produit scalaire hermitien est un prolongement hors programme MP.','La norme 2 utilise ici l’intégrale sur un intervalle de longueur 2π, sans division par cette longueur. Les notions de suite de Cauchy, de complétude, d’espace de Banach et de complétion L² sont hors programme MP ; elles ne sont pas nécessaires pour constater l’absence de suite extraite convergente.'])


MODELS={name:globals()[name] for name in ('bolzano_weierstrass','extraction_aleatoire','cauchy_rationnels','compacts_recouvrements','valeurs_extremes','heine_continuite','image_compacte','applications_lineaires','normes_dimension_infinie','boule_non_compacte')}


def calculate(lab_id,p):
    return MODELS[lab_id](p)
