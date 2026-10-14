"""Identités exactes et graphiques des six expériences classiques."""
import math
import numpy as np
import sympy as sp
from commun import exact,formula,metric,series,chart,result,table,curve_scene,plane_scene,point
X=sp.Symbol('X')

def sample(expr,lo=-4,hi=4,poles=(),count=1001):
    xs=np.linspace(lo,hi,count)
    f=sp.lambdify(X,expr,'numpy')
    with np.errstate(all='ignore'):
        ys=np.asarray(f(xs),dtype=float)
    if ys.ndim==0: ys=np.full(xs.shape,float(ys))
    valid=np.isfinite(ys)&(np.abs(ys)<40)
    for p in poles: valid &= np.abs(xs-float(p))>.035
    return xs,[float(y) if ok else None for y,ok in zip(ys,valid)]

def ordre(expr,a):
    _,den=sp.fraction(sp.cancel(expr))
    poly=sp.Poly(den,X)
    n=0
    while poly.degree()>0 and poly.eval(a)==0:
        poly=sp.div(poly,sp.Poly(X-a,X))[0]; n+=1
    return n

def rationnelle_recueil(p):
    A,B,C,D,s=[exact(p[k]) for k in ('A','B','C','D','shift')]
    z=X-s
    terms=[A/(z+1),B/(z-2),C/(z-2)**2,D/(z-2)**3]
    F=sp.cancel(1+sum(terms)); num,den=sp.fraction(F)
    q,r=sp.div(num,den,X)
    xs,ys=sample(F,poles=[a for a in (s-1,s+2) if ordre(F,a)>0])
    rows=[['Fraction réduite',formula(num),formula(den)],['Partie entière',formula(q),'1']]
    rows.extend([['Partie polaire '+str(i+1),formula(v),''] for i,v in enumerate(terms) if v!=0])
    return result([metric('Partie entière',formula(q)),metric('Ordre du pôle en s−1',ordre(F,s-1)),metric('Ordre du pôle en s+2',ordre(F,s+2)),metric('Recomposition exacte','vérifiée' if sp.cancel(F-1-sum(terms))==0 else 'échec')],
        [chart('Valeur de la fraction, sans relier les deux côtés des pôles','x','F(x)',series('F(x)',xs,ys))],
        curve_scene('Une partie entière et quatre parties polaires',xs,[('F',ys)],'x','F(x)','Les interruptions évitent de tracer une fausse liaison à travers un pôle. Les ordres sont calculés après simplification.'),
        ['Former le dénominateur commun et séparer le quotient de la division euclidienne.','Au pôle simple, multiplier par X−a puis évaluer en a.','Au pôle triple, multiplier par (X−a)³ puis utiliser les deux premières dérivées.','Recomposer les termes : le numérateur de la différence est exactement nul.'],
        ['Calcul symbolique sur ℚ ; les réglages décimaux sont convertis en fractions exactes.','Le graphique masque les voisinages des pôles et les valeurs de module supérieur à 40.','Les coefficients nuls peuvent supprimer un pôle ou abaisser son ordre.'],table('Décomposition exacte',['Élément','Expression','Dénominateur'],rows))

def poles_multiples(p):
    a,c=exact(p['a']),exact(p['c']); m=p['m']; g=X**4+c*X**2+X+1
    F=sp.cancel(g/(X-a)**m)
    q,_=sp.div(g,(X-a)**m,X)
    coeff=[sp.diff(g,X,m-k).subs(X,a)/sp.factorial(m-k) for k in range(1,m+1)]
    polar=sum(coeff[k-1]/(X-a)**k for k in range(1,m+1))
    xs,ys=sample(F,poles=[a]); tx=np.linspace(float(a)-1,float(a)+1,401)
    gv=np.asarray(sp.lambdify(X,g,'numpy')(tx),float)
    T=sp.expand(sum(sp.diff(g,X,j).subs(X,a)/sp.factorial(j)*(X-a)**j for j in range(m)))
    tv=np.asarray(sp.lambdify(X,T,'numpy')(tx),float); tv=np.full(tx.shape,float(tv)) if tv.ndim==0 else tv
    return result([metric('Ordre après réduction',ordre(F,a)),metric('Partie entière',formula(q)),metric('Coefficient du terme (X−a)⁻¹',formula(coeff[0])),metric('Certificat de décomposition','vérifié' if sp.cancel(F-q-polar)==0 else 'échec')],
        [chart('La fraction près du point a','x','F(x)',series('F',xs,ys)),chart('Taylor de g au point a','x','Valeur',series('g',tx,gv),series('Taylor, degré m−1',tx,tv))],
        curve_scene('Les dérivées de g déterminent la partie polaire',xs,[('F',ys)],'x','F(x)','Le tableau donne les coefficients exacts ; le graphique montre la fonction hors du point interdit.'),
        ['Écrire g(X) en puissances de X−a.','Diviser par (X−a)^m : les puissances négatives constituent la partie polaire.','Pour k de 1 à m, le coefficient A_k est g^(m−k)(a)/(m−k)!.','Les termes restants forment la partie entière ; vérifier la différence exacte.'],
        ['Le numérateur est un polynôme de degré quatre.','Une dérivée d’ordre supérieur à quatre est nulle.','L’ordre effectif peut être plus petit que m si g(a)=0.'],table('Coefficients de Taylor et termes polaires',['Puissance','Coefficient exact'],[[f'(X−a)^−{k}',formula(coeff[k-1])] for k in range(1,m+1)]+[['Partie entière',formula(q)]]))

def reel_complexe(p):
    a,b,u,v,w=[exact(p[k]) for k in ('a','b','u','v','w')]
    alpha=a+sp.I*b; beta=sp.conjugate(alpha)
    cp=sp.simplify((u*alpha+v)/(alpha-beta)); cm=sp.conjugate(cp)
    F=sp.cancel((u*X+v)/((X-a)**2+b*b)+w/(X-2))
    reconstructed=cp/(X-alpha)+cm/(X-beta)+w/(X-2)
    xs,ys=sample(F,poles=[2] if w!=0 else [])
    residue_points=[point(complex(cp.evalf()),'Résidu en a+ib',0),point(complex(cm.evalf()),'Résidu en a−ib',1)]
    roots=[point(complex(alpha),'Pôle a+ib',0),point(complex(beta),'Pôle a−ib',1)] if (u!=0 or v!=0) else []
    if w!=0: roots.append(point(2,'Pôle réel 2',2))
    return result([metric('Identité réelle/complexe','vérifiée' if sp.cancel(F-reconstructed)==0 else 'échec'),metric('Résidu au pôle supérieur',formula(cp)),metric('Résidu conjugué',formula(cm)),metric('Nombre de pôles effectifs',len(roots))],
        [chart('La fraction sur la droite réelle','x','F(x)',series('Écriture réelle = écriture complexe',xs,ys)),chart('Parties réelle et imaginaire des résidus','Pôle : −1 inférieur, +1 supérieur','Coefficient',series('Partie réelle',[-1,1],[float(sp.re(cm)),float(sp.re(cp))]),series('Partie imaginaire',[-1,1],[float(sp.im(cm)),float(sp.im(cp))]),style='bars')],
        plane_scene('Les pôles et leurs résidus se conjuguent',points=roots,bounds=[-3,3,-2.5,2.5],description='Les points représentent les pôles du transfert réduit, pas les valeurs de F. Le tableau donne les coefficients des éléments simples.'),
        ['Factoriser (X−a)²+b² en (X−a−ib)(X−a+ib).','Au pôle α=a+ib, calculer le coefficient (uα+v)/(α−conj(α)).','Le coefficient du pôle conjugué est son conjugué.','Additionner les deux fractions complexes : on retrouve (uX+v)/((X−a)²+b²).'],
        ['b>0 : les deux pôles complexes sont distincts et non réels.','Les coefficients u,v,w,a,b sont réels.','Le pôle réel disparaît si w=0 ; les deux autres disparaissent si u=v=0.'],table('Deux écritures d’une même fraction',['Pôle','Coefficient exact'],[['a+ib',formula(cp)],['a−ib',formula(cm)],['2',formula(w)]]))

def annulations(p):
    a,b=exact(p['a']),exact(p['b']); k,m=p['k'],p['m']
    num=(X-a)**k*(X**2+1); den=(X-a)**m*(X-b)*(X**2+1)
    F=sp.cancel(num/den); rn,rd=sp.fraction(F)
    poles=[]; holes=[]; rows=[]
    for c in sorted({a,b},key=float):
        order=ordre(F,c)
        if order: poles.append(c); rows.append([formula(c),'Pôle',str(order),'Pas de limite finie'])
        else:
            limit=sp.limit(F,X,c); holes.append(dict(x=float(c),y=float(limit),label='Trou, limite '+formula(limit),group=1,hollow=True)); rows.append([formula(c),'Trou','0',formula(limit)])
    xs,ys=sample(F,poles=poles)
    scene=curve_scene('La fonction réduite et les points exclus',xs,[('Expression réduite',ys)],'x','Valeur','Un cercle vide indique un point exclu où un prolongement continu est possible. Les pôles restent des interruptions.')
    scene['points']=holes
    return result([metric('Fraction réduite',formula(F)),metric('Points interdits réels distincts',len({a,b})),metric('Trous',len(holes)),metric('Pôles réels',len(poles))],
        [chart('Simplifier sans oublier le domaine initial','x','F(x)',series('Expression réduite',xs,ys))],scene,
        ['Le domaine initial exclut les zéros du dénominateur, même si un facteur se simplifie.','Le facteur X²+1 n’ajoute aucun point interdit réel.','Après réduction, compter la multiplicité restante de chaque facteur réel.','Une limite finie donne un trou ; une puissance négative donne un pôle. Si a=b, additionner les multiplicités.'],
        ['Les multiplicités k et m sont des entiers positifs.','Les limites sont calculées exactement sur ℚ.','Le tracé représente la formule réduite et marque les exclusions de l’expression initiale.'],table('Domaine et comportement local',['Point','Nature','Ordre','Limite'],rows))

def barycentric(nodes,values,xx):
    nodes=np.asarray(nodes,float); values=np.asarray(values,float); xx=np.asarray(xx,float)
    dif=nodes[:,None]-nodes[None,:]; np.fill_diagonal(dif,1)
    weights=1/np.prod(dif,axis=1); weights/=max(abs(weights))
    dist=xx[:,None]-nodes[None,:]; close=np.abs(dist)<1e-13
    safe=np.where(close,1,dist); coeff=weights[None,:]/safe
    result=np.sum(coeff*values,axis=1)/np.sum(coeff,axis=1)
    for i in np.where(np.any(close,axis=1))[0]: result[i]=values[np.argmax(close[i])]
    return result

def interpolation(p):
    n=p['n']; c=p['strength']; xx=np.linspace(-1,1,1001); f=lambda t:1/(1+c*t*t)
    equal=np.linspace(-1,1,n+1); cheb=np.sort(np.cos((2*np.arange(n+1)+1)*np.pi/(2*(n+1))))
    nodes=equal if p['nodes']=='equal' else cheb
    pe=barycentric(equal,f(equal),xx); pc=barycentric(cheb,f(cheb),xx); selected=pe if p['nodes']=='equal' else pc
    scene=curve_scene('Les mêmes valeurs, deux répartitions de nœuds',xx,[('f',f(xx)),('Nœuds équidistants',pe),('Nœuds de Tchebychev',pc)],'x','Valeur','Les points indiquent les nœuds actuellement choisis. Les erreurs affichées sont mesurées sur 1001 points.')
    scene['points']=[dict(x=float(x),y=float(y),group=3,label='Nœud '+str(i)) for i,(x,y) in enumerate(zip(nodes,f(nodes)))]
    return result([metric('Erreur maximale équidistante, grille',float(max(abs(pe-f(xx))))),metric('Erreur maximale Tchebychev, grille',float(max(abs(pc-f(xx))))),metric('Conditionnement de Vandermonde',float(np.linalg.cond(np.vander(nodes)))),metric('Nombre de contraintes',n+1)],
        [chart('Erreur entre les nœuds','x','P_n(x)−f(x)',series('Équidistants',xx,pe-f(xx)),series('Tchebychev',xx,pc-f(xx))),chart('Interpolateur sélectionné','x','Valeur',series('Fonction',xx,f(xx)),series('Polynôme',xx,selected))],scene,
        ['Il existe un unique polynôme de degré au plus n prenant les n+1 valeurs prescrites.','Évaluer la formule barycentrique de Lagrange sans développer les coefficients.','Comparer l’erreur entre les nœuds, particulièrement près de −1 et 1.','Le conditionnement de Vandermonde concerne l’écriture dans la base des monômes ; il ne prouve pas à lui seul la taille de l’erreur d’approximation.'],
        ['Fonction de Runge f(x)=1/(1+cx²), c>0.','Nœuds distincts ; calculs flottants en double précision.','L’erreur maximale affichée est un maximum discret, pas une preuve du maximum sur tout l’intervalle.'],table('Données d’interpolation',['i','Nœud x_i','Valeur f(x_i)'],[[i,float(x),float(y)] for i,(x,y) in enumerate(zip(nodes,f(nodes)))]))

def orthogonal_data(family,n):
    if family=='legendre':
        P=sp.legendre(n,X); nodes,weights=np.polynomial.legendre.leggauss(n); norm=2/(2*n+1); extent=1.1
    elif family=='chebyshev':
        P=sp.chebyshevt(n,X); nodes,weights=np.polynomial.chebyshev.chebgauss(n); norm=math.pi/2; extent=1.05
    else:
        P=sp.hermite_prob(n,X); nodes,weights=np.polynomial.hermite_e.hermegauss(n); norm=math.sqrt(2*math.pi)*math.factorial(n); extent=1.05*math.sqrt(4*n+2)
    return P,nodes,weights,norm,extent

def moment(family,k):
    if k%2: return 0.0
    if family=='legendre': return 2/(k+1)
    if family=='chebyshev': return math.pi*math.comb(k,k//2)/4**(k//2)
    return math.sqrt(2*math.pi)*math.prod(range(1,k,2))

def orthogonaux(p):
    n,k,family=p['n'],p['power'],p['family']; P,nodes,weights,norm,extent=orthogonal_data(family,n)
    xx=np.linspace(-extent,extent,1001); yy=np.asarray(sp.lambdify(X,P/sp.sqrt(norm),'numpy')(xx),float)
    lower=orthogonal_data(family,n-1)[0]; yp=np.asarray(sp.lambdify(X,lower,'numpy')(xx),float)
    yp/=max(1,np.max(np.abs(yp))); shown=yy/max(1,np.max(abs(yy)))
    q=math.fsum(float(w*x**k) for x,w in zip(nodes,weights)); ref=moment(family,k)
    scene=curve_scene('Les racines organisent les nœuds de quadrature',xx,[('Degré n, échelle graphique',shown),('Degré n−1, échelle graphique',yp)],'x','Polynômes mis à l’échelle','Chaque courbe est divisée par son maximum sur la fenêtre. Les racines et leur entrelacement ne changent pas.')
    scene['points']=[dict(x=float(x),y=0,group=0,label='Nœud '+str(i+1)) for i,x in enumerate(nodes)]
    return result([metric('Moment exact',ref),metric('Quadrature',q),metric('Erreur relative ou absolue si moment nul',abs(q-ref)/abs(ref) if ref else abs(q)),metric('Degré d’exactitude garanti',2*n-1)],
        [chart('Polynôme orthonormal','x','P_n(x)/√‖P_n‖²',series('P_n normalisé',xx,yy)),chart('Poids positifs de quadrature','Nœud x_i','Poids w_i',series('Poids',nodes,weights),style='bars')],scene,
        ['Choisir le poids : uniforme, arcsinus ou gaussien.','Les n racines du polynôme orthogonal sont les nœuds de la quadrature de Gauss correspondante.','Une quadrature à n nœuds est exacte pour tous les polynômes de degré au plus 2n−1.','Calculer le moment d’ordre k puis comparer à la somme des w_i x_i^k. Au-delà de 2n−1, l’exactitude n’est plus garantie.'],
        ['Hermite désigne ici la convention probabiliste du recueil : H₁(X)=X.','Les moments impairs exacts sont nuls par symétrie.','Les nœuds et poids sont numériques ; les moments de référence proviennent des formules analytiques.','La quadrature de Gauss est un prolongement accompagné du cours d’espaces préhilbertiens.'],table('Polynôme, nœuds et poids',['Élément','Valeur','Poids'],[['P_n',formula(P),'']]+[[i+1,float(x),float(w)] for i,(x,w) in enumerate(zip(nodes,weights))]))

COMPUTE={name:globals()[name] for name in ['rationnelle_recueil','poles_multiples','reel_complexe','annulations','interpolation','orthogonaux']}
