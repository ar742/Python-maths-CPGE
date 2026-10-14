"""Modèles multivariés : calculs exacts et géométrie réelle explicitement séparés."""
from __future__ import annotations
import cmath
import math
import numpy as np
import sympy as sp
from commun import metric, series, chart, table, result, plane_scene, field_scene, exact, formula

X,Y=sp.symbols('x y')
EPS=1e-10

def grid(d=3,n=121,centre=0):
    x=np.linspace(centre-d,centre+d,n); y=np.linspace(-d,d,n)
    xx,yy=np.meshgrid(x,y)
    return x,y,xx,yy

def path(label,x,y): return dict(label=label,x=np.asarray(x),y=np.asarray(y))
def pt(x,y,label,group=0): return dict(x=float(x),y=float(y),label=label,group=group)
def convex_hull(points):
    points=sorted(set(tuple(p) for p in points))
    if len(points)<=1: return points
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]; upper=[]
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def monomes_newton(p):
    m,n,q=int(p['m']),int(p['n']),int(p['q']); a,c=p['a'],p['c']
    terms={(m,0):1.,(0,n):1.}
    if a: terms[(2,q)]=a
    if c: terms[(0,0)]=c
    hull=convex_hull(terms); total=max(i+j for i,j in terms)
    dx=max(i for i,j in terms); dy=max(j for i,j in terms)
    vertices=hull+[hull[0]]
    ar=abs(sum(hull[k][0]*hull[(k+1)%len(hull)][1]-hull[k][1]*hull[(k+1)%len(hull)][0] for k in range(len(hull))))/2
    x=np.linspace(-1.5,1.5,301)
    rows=[[f'x^{i} y^{j}',v,i,j,i+j] for (i,j),v in sorted(terms.items())]
    return result([metric('Degré total',total),metric('Degré en x',dx),metric('Degré en y',dy),metric('Monômes non nuls',len(terms)),metric('Aire du polygone de Newton',ar)],
        [chart('Deux tranches du même polynôme','x','P(x,y)',series('y=0',x,x**m+c),series('y=1',x,x**m+a*x*x+1+c))],
        plane_scene('Le support vit dans le plan des exposants',points=[pt(i,j,f'coefficient {v:g} : degré {i+j}') for (i,j),v in terms.items()],polygons=[dict(label='Enveloppe convexe du support',x=[i for i,j in vertices],y=[j for i,j in vertices])],bounds=[-.5,max(6,dx)+.5,-.5,max(6,dy)+.5],xlabel='Exposant de x',ylabel='Exposant de y',description='Chaque point représente un monôme non nul, pas un point de la courbe P(x,y)=0. Retirer un coefficient peut modifier le support et le degré.'),
        [f'P(x,y)=x^{m}+({a:g})x²y^{q}+y^{n}+({c:g}). Le support ne contient que les coefficients non nuls.',f'Le degré total est le maximum i+j : {total}. Les degrés partiels sont les maximums de i et de j : {dx} et {dy}.','L’enveloppe convexe des exposants est le polygone de Newton. Elle décrit les monômes extrêmes ; elle ne constitue pas à elle seule une preuve du nombre de solutions.'],
        ['Deux indéterminées réelles ou complexes ; les tranches sont représentées pour x réel. Le dessin du support est un outil algébrique.'],table('Lire chaque terme avant de compter',['Monôme','Coefficient','Degré en x','Degré en y','Degré total'],rows))

def circle_parabola_roots(r,h):
    """Racines complexes en x, avec répétitions algébriques (quartique monique)."""
    rr,hh=exact(r),exact(h); D=1-4*hh+4*rr*rr
    d=cmath.sqrt(complex(float(D)))
    roots=[]
    for t in ((2*h-1+d)/2,(2*h-1-d)/2):
        z=cmath.sqrt(t); roots.extend([z,-z])
    return roots,D

def distinct_complex(roots,tol=1e-8):
    out=[]
    for z in roots:
        for item in out:
            if abs(item[0]-z)<tol: item[1]+=1; break
        else: out.append([z,1])
    return out

def intersection_bezout(p):
    r,h=p['r'],p['h']; roots,D=circle_parabola_roots(r,h)
    distinct=distinct_complex(roots); reals=[(z.real,k) for z,k in distinct if abs(z.imag)<1e-8]
    d=max(3,h+1,r+1); x,y,xx,yy=grid(d)
    xp=np.linspace(-math.sqrt(d+h),math.sqrt(d+h),501) if d+h>0 else np.array([0.])
    points=[pt(a,a*a-h,f'Intersection réelle, multiplicité {k}',0 if k==1 else 1) for a,k in reals]
    scan=np.linspace(-max(2,r+1),max(2,r+1),501)
    quart=scan**4+(1-2*h)*scan**2+h*h-r*r
    rows=[]
    for z,k in distinct:
        zz=z*z-h
        rows.append([f'{z.real:.6g}{z.imag:+.6g}i',f'{zz.real:.6g}{zz.imag:+.6g}i',k,'réel' if abs(z.imag)<1e-8 else 'complexe non réel'])
    return result([metric('Points réels distincts',len(reals)),metric('Multiplicité réelle totale',sum(k for z,k in reals)),metric('Multiplicité complexe totale',4),metric('Discriminant en t=x²',float(D)),metric('Intersections à l’infini',0)],
        [chart('Éliminer y : un quartique en x','x','Q(x)',series('x⁴+(1-2h)x²+h²-r²',scan,quart))],
        field_scene('Cercle en contour, parabole en chemin',x,y,xx*xx+yy*yy-r*r,'Le champ représente x²+y²-r² ; son contour zéro est le cercle. Les points indiqués sont uniquement les intersections réelles.',points=points,paths=[path('Parabole y=x²-h',xp,xp*xp-h)],levels=[0]),
        ['Substituer y=x²-h dans x²+y²=r² : Q(x)=x⁴+(1-2h)x²+h²-r².',f'Poser t=x² : t²+(1-2h)t+h²-r²=0, de discriminant D={float(D):g}. Seuls les t réels positifs ou nuls fournissent des x réels.','Un t double ou t=0 crée des racines multiples en x. À r=h=1/2, Q=x⁴ : un seul point réel porte la multiplicité quatre.','Les deux courbes de degré deux n’ont pas de composante commune. Leurs équations homogénéisées n’ont aucun point commun à l’infini : les quatre intersections complexes, comptées avec multiplicité, sont affines.'],
        ['Les coordonnées complexes sont calculées par deux équations du second degré ; le dessin reste dans le plan réel. Bézout et la multiplicité d’intersection sont présentés comme prolongements.'],table('Solutions complexes : ne pas confondre nombre de points et multiplicité',['x','y=x²-h','Multiplicité','Nature'],rows))

def elimination_polynomials(a,b):
    aa,bb=exact(a),exact(b)
    F=(X-aa)*Y-1; G=(X-aa)*(Y-bb)
    return F,G,sp.factor(sp.resultant(F,G,Y))

def resultant_elimination(p):
    a,b=p['a'],p['b']; F,G,R=elimination_polynomials(a,b)
    d=max(3,(1/abs(b)+1) if b else 3)
    x,y,xx,yy=grid(d,centre=a)
    points=[]; rows=[[f'x={a:g}','F(a,y)=-1','Impossible : le degré en y chute']]
    if b:
        xi=a+1/b; points=[pt(xi,b,'Solution après substitution')]
        rows.append([f'x={xi:.6g}',f'y={b:g}','F=G=0 : solution conservée'])
    else: rows.append(['Aucun autre candidat','G=(x-a)y','Aucune solution affine'])
    scan=np.linspace(a-d,a+d,401)
    return result([metric('Points affines communs',int(bool(b))),metric('Candidats du résultant',2 if b else 1),metric('Candidats rejetés',1),metric('Résultant en x',formula(R))],
        [chart('Le zéro parasite apparaît dans le résultant','x','R(x)',series('R=(x-a)[1-b(x-a)]',scan,(scan-a)*(1-b*(scan-a))))],
        field_scene('Une hyperbole et une courbe réductible',x,y,(xx-a)*yy-1,'Le contour zéro est (x-a)y=1 ; les deux droites représentent (x-a)(y-b)=0. Le candidat x=a n’est jamais sur l’hyperbole.',points=points,paths=[path('Droite x=a',[a,a],[-d,d]),path('Droite y=b',[a-d,a+d],[b,b])],levels=[0]),
        ['Écrire F=(x-a)y-1 et G=(x-a)(y-b). Le déterminant de Sylvester en y est R=(x-a)[1-b(x-a)].','Tout point commun annule R. La réciproque exige de vérifier les équations initiales, notamment lorsque leurs coefficients dominants s’annulent.',f'Pour x=a={a:g}, F vaut -1 quel que soit y : ce candidat est rejeté.',f'Pour b={b:g}, '+(f'le second candidat donne x=a+1/b={a+1/b:.6g}, puis y=b.' if b else 'il ne reste aucun candidat valide. Le résultant possède pourtant un zéro.')],
        ['Calcul exact sur les valeurs rationnelles des réglages. Une projection ou une racine du résultant ne dispense jamais de la substitution dans F et G.'],table('Vérifier les fibres au-dessus des abscisses candidates',['Candidat','Substitution','Décision'],rows))

def groebner_data(c,order):
    cc=exact(c); F=X*Y-1; G=Y*Y-X-cc
    basis=sp.groebner([F,G],X,Y,order=order)
    certs=[]
    for i in range(len(basis.polys)):
        for j in range(i+1,len(basis.polys)):
            fi,fj=basis.polys[i],basis.polys[j]
            mi=fi.monoms(order=order)[0]; mj=fj.monoms(order=order)[0]
            ci=fi.coeffs(order=order)[0]; cj=fj.coeffs(order=order)[0]
            lcm=tuple(max(a,b) for a,b in zip(mi,mj))
            mult_i=X**(lcm[0]-mi[0])*Y**(lcm[1]-mi[1])/ci
            mult_j=X**(lcm[0]-mj[0])*Y**(lcm[1]-mj[1])/cj
            s=sp.expand(mult_i*fi.as_expr()-mult_j*fj.as_expr())
            remainder=basis.reduce(s)[1]
            certs.append((i+1,j+1,s,remainder))
    return F,G,basis,certs

def groebner_ordre(p):
    c=int(p['c']); order=p['order']; F,G,basis,certs=groebner_data(c,order)
    roots=np.roots([1,0,-c,-1]); real=[float(z.real) for z in roots if abs(z.imag)<1e-8]
    x,y,xx,yy=grid(4)
    xp=np.linspace(max(-4,-c),4,501); yp=np.sqrt(np.maximum(xp+c,0))
    rows=[[f'g{k+1}',formula(poly.as_expr()),formula(poly.LM(order=order).as_expr())] for k,poly in enumerate(basis.polys)]
    rows.extend([[f'S(g{i},g{j})',formula(s),f'reste : {formula(r)}'] for i,j,s,r in certs])
    scan=np.linspace(-3,3,401)
    return result([metric('Ordre choisi','lex' if order=='lex' else 'degré / lex inverse'),metric('Polynômes dans la base',len(basis.polys)),metric('Points réels',len(real)),metric('Dimension du quotient',3),metric('Restes des S-polynômes',max([abs(float(r)) for i,j,s,r in certs] or [0]))],
        [chart('L’éliminant lexicographique ne change pas','y','y³-cy-1',series('Éliminant en y',scan,scan**3-c*scan-1))],
        field_scene('Le même ensemble de solutions dans les deux ordres',x,y,xx*yy-1,'Le contour zéro est xy-1 ; les chemins sont y²-x-c=0. Changer l’ordre transforme la division et les termes dominants, pas les points communs.',points=[pt(t*t-c,t,'Solution réelle') for t in real],paths=[path('y=+√(x+c)',xp,yp),path('y=-√(x+c)',xp,-yp)],levels=[0]),
        ['L’idéal I est engendré par F=xy-1 et G=y²-x-c. Il regroupe toutes les combinaisons AF+BG avec A et B polynomiaux.', 'En ordre lexicographique x avant y, g₁=x-y²+c=-G et g₂=y³-cy-1=yG+F : la variable x est éliminée.', 'En ordre degré / lexicographique inverse, la base contient H=x²+cx-y=yF-xG, F et G. Ses monômes dominants sont x², xy et y².', 'Chaque S-polynôme compare deux termes dominants de même monôme. Son reste nul certifie ici la propriété de base de Gröbner (critère de Buchberger). Les monômes restants forment une base du quotient : {1,y,y²} en lex, {1,x,y} en degré / lex inverse.'],
        ['Les bases et les restes sont calculés exactement. Théorie des idéaux et bases de Gröbner : prolongement au-delà du programme ; les divisions et substitutions réinvestissent les méthodes CPGE.'],table('Base choisie et certificats de division',['Élément','Polynôme','Terme dominant ou reste'],rows))

def symmetric_values(u,v,w):
    ss=[exact(u)+exact(v)+exact(w),exact(u)*exact(v)+exact(u)*exact(w)+exact(v)*exact(w),exact(u)*exact(v)*exact(w)]
    e1,e2,e3=ss
    powers=[sp.Integer(3),e1,e1**2-2*e2,e1**3-3*e1*e2+3*e3]
    for k in range(4,7): powers.append(sp.expand(e1*powers[-1]-e2*powers[-2]+e3*powers[-3]))
    discriminant=(exact(u)-exact(v))**2*(exact(u)-exact(w))**2*(exact(v)-exact(w))**2
    return ss,powers,discriminant

def symetriques(p):
    u,v,w=p['u'],p['v'],p['w']; ss,powers,D=symmetric_values(u,v,w); e1,e2,e3=map(float,ss)
    d2=max(4,abs(e2)*1.3); d3=max(4,abs(e3)*1.3)
    x=np.linspace(-d2,d2,121); y=np.linspace(-d3,d3,121); xx,yy=np.meshgrid(x,y)
    disc=e1*e1*xx*xx-4*xx**3-4*e1**3*yy-27*yy*yy+18*e1*xx*yy
    scene=field_scene('La frontière des racines multiples dans le plan des coefficients',x,y,disc,f'e₁={e1:g} est fixé ; le contour zéro est le discriminant. Le point choisi représente e₂ et e₃, pas les racines u,v,w.',points=[pt(e2,e3,'Coefficients des trois racines choisies')],levels=[0]); scene['xLabel']='e₂'; scene['yLabel']='e₃'
    t=np.linspace(min(u,v,w)-1,max(u,v,w)+1,401)
    return result([metric('e₁=u+v+w',e1),metric('e₂=uv+uw+vw',e2),metric('e₃=uvw',e3),metric('Discriminant',float(D)),metric('Racines distinctes',len(set((u,v,w))))],
        [chart('Retrouver les racines à partir des coefficients','T','P(T)',series('T³-e₁T²+e₂T-e₃',t,(t-u)*(t-v)*(t-w))),chart('Sommes de puissances par Newton','k','pₖ',series('uᵏ+vᵏ+wᵏ',list(range(1,7)),[float(z) for z in powers[1:]]),style='bars')],scene,
        ['Les fonctions symétriques élémentaires sont e₁=u+v+w, e₂=uv+uw+vw et e₃=uvw. Elles sont inchangées par permutation des trois variables.', 'Le polynôme monique dont les racines sont u,v,w est T³-e₁T²+e₂T-e₃.', 'Avec pₖ=uᵏ+vᵏ+wᵏ, Newton donne p₁=e₁, p₂=e₁p₁-2e₂, p₃=e₁p₂-e₂p₁+3e₃, puis pₖ=e₁pₖ₋₁-e₂pₖ₋₂+e₃pₖ₋₃ pour k≥4.', 'Le discriminant D=(u-v)²(u-w)²(v-w)² s’annule exactement lorsqu’au moins deux racines sont égales. Son expression en e₁,e₂,e₃ définit la frontière dessinée.'],
        ['Racines réelles imposées par les réglages ; calcul des identités en nombres rationnels exacts. Le plan des coefficients est une visualisation, pas une variation indépendante des racines.'],table('Comparer calcul direct et récurrence de Newton',['k','Valeur par Newton','Valeur directe'],[[k,formula(powers[k]),formula(exact(u)**k+exact(v)**k+exact(w)**k)] for k in range(1,7)]))

def singularites(p):
    t=p['t']; d=max(3,abs(t)+1); x,y,xx,yy=grid(d)
    kind='nœud' if t>0 else ('pointe' if t==0 else 'point réel isolé')
    xp=np.linspace(max(-d,-t),d,501); yp=np.abs(xp)*np.sqrt(np.maximum(xp+t,0)); paths=[path('Branche supérieure',xp,yp),path('Branche inférieure',xp,-yp)]
    if t>0:
        z=np.linspace(-.8,.8,101); paths.extend([path('Tangente y=+√t x',z,math.sqrt(t)*z),path('Tangente y=-√t x',z,-math.sqrt(t)*z)])
    elif t==0: paths.append(path('Tangente double y=0',[-.8,.8],[0,0]))
    scan=np.linspace(-d,d,401)
    return result([metric('Nature réelle à l’origine',kind),metric('Points singuliers de la courbe',1),metric('Tangentes réelles distinctes',2 if t>0 else (1 if t==0 else 0)),metric('Déterminant de la hessienne à l’origine',-4*t)],
        [chart('Coupe suivant y=0','x','F(x,0)',series('-x²(x+t)',scan,-scan*scan*(scan+t)))],
        field_scene('Un même gradient nul, trois géométries',x,y,yy*yy-xx**3-t*xx*xx,'La courbe F=0 est suivie par ses branches exactes. À t<0, l’origine est isolée de l’autre branche réelle.',points=[pt(0,0,kind,1)],paths=paths,levels=[0]),
        ['F(x,y)=y²-x³-tx². Une singularité de la courbe vérifie simultanément F=0, ∂F/∂x=-3x²-2tx=0 et ∂F/∂y=2y=0.', 'L’origine est toujours singulière. Le candidat x=-2t/3,y=0 ne vérifie F=0 que si t=0 ; il ne fournit donc pas de second point singulier.', 'Le terme homogène de plus bas degré est y²-tx². Pour t>0, il se factorise en deux tangentes réelles ; pour t=0, il donne une tangente double y=0.', 'Pour t<0, y²+|t|x² est défini positif. Plus directement, y²=x²(x+t) est impossible pour 0<|x|<|t| : l’origine est un point réel isolé.'],
        ['Variables réelles pour le dessin ; singularités déterminées algébriquement et non détectées par pixels. La terminologie des singularités prolonge le calcul différentiel CPGE.'],table('Gradient et partie quadratique',['Objet','Expression'],[['F',f'y²-x³-({t:g})x²'],['∂F/∂x',f'-3x²-({2*t:g})x'],['∂F/∂y','2y'],['Partie de degré 2',f'y²-({t:g})x²'],['Hessienne à (0,0)',f'diag({-2*t:g}, 2)']]))

def homogenisation(p):
    c=p['c']; affine=p['chart']=='affine'; parabola=p['kind']=='parabola'
    x,y,xx,yy=grid(3)
    if affine:
        z=yy-xx*xx-c if parabola else xx*yy-c
        expression=f'y-x²-{c:g}' if parabola else f'xy-{c:g}'
        points=[]; xlabel='x=X/Z'; ylabel='y=Y/Z'
    else:
        z=yy-xx*xx-c*yy*yy if parabola else xx-c*yy*yy
        expression=f'v-u²-{c:g}v²' if parabola else f'u-{c:g}v²'
        points=[pt(0,0,'[0:1:0] : point à l’infini dans la carte affine',1)]; xlabel='u=X/Y'; ylabel='v=Z/Y'
    homogenized=f'YZ-X²-{c:g}Z²' if parabola else f'XY-{c:g}Z²'
    scene=field_scene('Une autre carte rend fini un point projectif',x,y,z,'Les coordonnées sont des rapports. Dans la carte Y≠0, la droite v=0 représente les points à l’infini de la carte Z≠0.',points=points,paths=[] if affine else [path('v=0 : droite à l’infini',[-3,3],[0,0])],levels=[0]); scene['xLabel']=xlabel; scene['yLabel']=ylabel
    scan=np.linspace(-2,2,401)
    rows=[['Équation homogène',homogenized],['Carte Z≠0 : X=xZ, Y=yZ',f'F(x,y)={expression}' if affine else ('y-x²-c' if parabola else 'xy-c')],['Carte Y≠0 : X=uY, Z=vY',('v-u²-cv²' if parabola else 'u-cv²')],['Points avec Z=0','[0:1:0]' if parabola else '[1:0:0] et [0:1:0]']]
    return result([metric('Degré homogène',2),metric('Points réels à l’infini',1 if parabola else 2),metric('Carte affichée','Z≠0' if affine else 'Y≠0'),metric('Équation dans cette carte',expression)],
        [chart('Coordonnées dans la carte Y≠0','v=Z/Y','u² (parabole) ou u (hyperbole)',series('v-cv²' if parabola else 'cv²',scan,scan-c*scan*scan if parabola else c*scan*scan))],scene,
        ['Un point projectif [X:Y:Z] est une classe de triplets non nuls, identifiés lorsqu’ils sont multipliés par un même scalaire non nul.', 'Une équation de degré d devient homogène en multipliant chaque monôme de degré k par Z^(d-k). Les termes ont alors tous le même degré.', 'La carte Z≠0 redonne le plan usuel : x=X/Z et y=Y/Z. Les points Z=0 n’appartiennent pas à cette carte.', 'Dans la carte Y≠0, poser u=X/Y et v=Z/Y. Le point [0:1:0] devient (u,v)=(0,0). Pour l’hyperbole, [1:0:0] n’est pas dans cette carte et exige la carte X≠0.'],
        ['Géométrie projective au-delà du programme ; le calcul consiste seulement à homogénéiser puis substituer. Un point à l’infini n’est pas un réel de grande valeur.'],table('Changer de carte sans changer de courbe',['Objet','Écriture'],rows))

def quadratic_data(a,b,c):
    A=np.array([[1,a,0],[a,1,c],[0,c,b]],dtype=float)
    vals,vectors=np.linalg.eigh(A)
    minors=[1,1-a*a,b*(1-a*a)-c*c]
    signs=[sum(vals>1e-10),sum(vals<-1e-10),sum(abs(vals)<=1e-10)]
    return A,vals,vectors,minors,signs

def formes_quadratiques(p):
    a,b,c,z0=(p[k] for k in ('a','b','c','slice')); A,vals,vectors,minors,signs=quadratic_data(a,b,c)
    d=max(3,abs(z0)+1); x,y,xx,yy=grid(d)
    field=xx*xx+yy*yy+b*z0*z0+2*a*xx*yy+2*c*yy*z0
    t=np.linspace(-2,2,301)
    kind='définie positive' if signs==[3,0,0] else ('semi-définie positive' if signs[1]==0 else 'indéfinie')
    return result([metric('Nature de Q',kind),metric('Signature (+, -, 0)',f'({signs[0]}, {signs[1]}, {signs[2]})'),metric('Déterminant de A',minors[2]),metric('Critère de Sylvester', 'vérifié' if min(minors)>1e-10 else 'non vérifié'),metric('Tranche choisie z₀',z0)],
        [chart('Q le long des trois directions propres','t','Q(t eᵢ)',*[series(f'λ{i+1}={v:.5g}',t,v*t*t) for i,v in enumerate(vals)])],
        field_scene('Tranche z=z₀ d’une forme en trois variables',x,y,field,'Le champ représente Q(x,y,z₀). Les contours 0, 1 et 2 sont des niveaux ; la nature globale de Q est déduite des trois valeurs propres de A.',levels=[0,1,2]),
        ['Q=x²+y²+bz²+2axy+2cyz. Sa matrice symétrique A vérifie Q(v)=vᵀAv ; sa hessienne est 2A.',f'Les trois mineurs principaux successifs sont Δ₁=1, Δ₂=1-a²={minors[1]:g}, Δ₃=b(1-a²)-c²={minors[2]:g}.','Le critère de Sylvester donne A définie positive si et seulement si ces trois mineurs sont strictement positifs. Une égalité exige une analyse supplémentaire.',f'Les valeurs propres sont {vals[0]:.6g}, {vals[1]:.6g}, {vals[2]:.6g}. Dans une base orthonormée de vecteurs propres, Q=λ₁u₁²+λ₂u₂²+λ₃u₃² ; leur signe donne la signature.','La tranche z=z₀ ne représente pas toutes les directions de l’espace. Un niveau fermé dans une tranche ne suffit donc pas à conclure sur la forme entière.'],
        ['Matrice symétrique réelle de taille 3 ; valeurs propres calculées numériquement. La tolérance de classement vaut 10⁻¹⁰, adaptée à la plage des réglages.'],table('Mineurs et directions propres',['Objet','Valeur'],[['Δ₁',minors[0]],['Δ₂',minors[1]],['Δ₃',minors[2]]]+[[f'λ{i+1}',float(v)] for i,v in enumerate(vals)]))

def motzkin_value(x,y,lam): return x**4*y*y+x*x*y**4-lam*x*x*y*y+1
def motzkin_minimum(lam): return 1-lam**3/27

def positivite_motzkin(p):
    lam=p['lam']; x,y,xx,yy=grid(2); field=motzkin_value(xx,yy,lam)
    s=math.sqrt(lam/3) if lam else 0
    points=[pt(sx*s,sy*s,'Minimum global',0 if lam<=3 else 1) for sx in (-1,1) for sy in (-1,1)] if lam else []
    t=np.linspace(-2,2,401); minimum=motzkin_minimum(lam)
    return result([metric('Minimum global exact',minimum),metric('Valeur en (1,1)',3-lam),metric('Non négatif sur ℝ²','oui' if lam<=3 else 'non'),metric('Somme de carrés de polynômes réels','oui' if lam==0 else 'non'),metric('Zéros réels pour λ choisi',4 if lam==3 else ('aucun' if lam<3 else 'courbes de zéros'))],
        [chart('Une diagonale atteint le minimum global','t','Mλ(t,t)',series('2t⁶-λt⁴+1',t,2*t**6-lam*t**4+1),series('Référence λ=0 : somme de carrés',t,2*t**6+1))],
        field_scene('Le polynôme de Motzkin et ses minima',x,y,field,'Les quatre points sont les minima globaux pour λ>0. Le contour zéro apparaît à λ=3, puis borde des régions négatives pour λ>3.',points=points,levels=[0]),
        ['Mλ=x⁴y²+x²y⁴-λx²y²+1. Poser t=|xy|. L’inégalité arithmético-géométrique donne x⁴y²+x²y⁴≥2t³, avec égalité lorsque |x|=|y| (ou xy=0).',f'La fonction 2t³-λt²+1 sur t≥0 est minimale en t=λ/3 : min Mλ=1-λ³/27={minimum:.6g}. Pour λ>0, ce minimum est atteint en x,y=±√(λ/3).','Mλ est donc non négatif exactement pour 0≤λ≤3. À λ=3, une autre application de l’inégalité arithmético-géométrique à x⁴y², x²y⁴ et 1 donne M₃≥0.', 'À λ=0, M₀=(x²y)²+(xy²)²+1². Pour λ>0, supposer Mλ=∑qᵢ² force deg qᵢ≤3. Les coefficients absents de x⁶,y⁶,x⁴,y⁴,x²,y² imposent successivement qᵢ=Aᵢ+Bᵢxy+Cᵢx²y+Dᵢxy². Le coefficient de x²y² serait alors ∑Bᵢ²≥0, alors qu’il vaut -λ : contradiction.'],
        ['Preuve algébrique globale : le maillage sert uniquement à illustrer les signes. Une somme de carrés désigne ici des carrés de polynômes à coefficients réels, sans dénominateurs.'],table('Trois valeurs qui changent le problème',['λ','Minimum','Conclusion'],[[0,1,'Somme de carrés explicite'],[3,0,'Non négatif, sans somme de carrés polynomiaux'],[4,1-64/27,'Prend des valeurs négatives']]))

def lagrange_data(a,r):
    angles=[math.pi/4+k*math.pi/2 for k in range(4)]; ratio=a/(2*r*r)
    if abs(ratio)<=1+EPS:
        s=math.asin(max(-1,min(1,ratio)))
        for k in (0,1): angles.extend([(s/2+k*math.pi)%(2*math.pi),((math.pi-s)/2+k*math.pi)%(2*math.pi)])
    angles=sorted(angles); distinct=[]
    for t in angles:
        if not distinct or abs(t-distinct[-1])>1e-8: distinct.append(t)
    if len(distinct)>1 and 2*math.pi-distinct[-1]+distinct[0]<1e-8: distinct.pop()
    fmin=r**4/2-abs(a)*r*r/2
    fmax=r**4+a*a/8 if abs(a)<=2*r*r else r**4/2+abs(a)*r*r/2
    rows=[]
    for t in distinct:
        x,y=r*math.cos(t),r*math.sin(t); val=x**4+y**4+a*x*y
        second=-2*r*r*math.sin(2*t)*(a-2*r*r*math.sin(2*t))-4*r**4*math.cos(2*t)**2
        classification='minimum' if second>EPS else ('maximum' if second<-EPS else 'maximum dégénéré')
        mult=(4*(x**4+y**4)+2*a*x*y)/(2*r*r)
        rows.append(dict(theta=t,x=x,y=y,value=val,second=second,classification=classification,multiplier=mult))
    return rows,fmin,fmax

def lagrange_contrainte(p):
    a,r=p['a'],p['r']; rows,fmin,fmax=lagrange_data(a,r)
    theta=np.linspace(0,2*math.pi,721); xc=r*np.cos(theta); yc=r*np.sin(theta)
    vals=xc**4+yc**4+a*xc*yc; deriv=r*r*np.cos(2*theta)*(a-2*r*r*np.sin(2*theta))
    x,y,xx,yy=grid(max(2.5,1.4*r))
    return result([metric('Minimum sur le cercle',fmin),metric('Maximum sur le cercle',fmax),metric('Points stationnaires',len(rows)),metric('Valeur critique |a|',2*r*r),metric('Points dégénérés',sum(abs(z['second'])<=EPS for z in rows))],
        [chart('La fonction restreinte au cercle','θ (rad)','f(r cos θ,r sin θ)',series('Valeur sur le cercle',theta,vals),series('Minimum global',theta,np.full_like(theta,fmin)),series('Maximum global',theta,np.full_like(theta,fmax))),chart('Retrouver tous les points stationnaires','θ (rad)','d f / dθ',series('r²cos(2θ)[a-2r²sin(2θ)]',theta,deriv))],
        field_scene('Le cercle contraint et les niveaux du quartique',x,y,xx**4+yy**4+a*xx*yy,'Le champ représente f dans le plan ; le chemin indique la contrainte x²+y²=r². Seuls les points stationnaires sur ce cercle sont marqués.',points=[pt(z['x'],z['y'],z['classification'],0 if 'maximum' in z['classification'] else 1) for z in rows],paths=[path('Cercle de rayon r',xc,yc)],levels=[fmin,fmax]),
        ['La contrainte g=x²+y²-r²=0 est régulière puisque ∇g=2(x,y) ne s’annule pas sur le cercle (r>0). Lagrange donne ∇f=μ∇g.', 'Avec x=r cosθ et y=r sinθ, la dérivée est r²cos(2θ)[a-2r²sin(2θ)]. Les solutions sont cos(2θ)=0 ou sin(2θ)=a/(2r²).','La seconde famille existe pour |a|≤2r². À l’égalité, deux paires de points se rejoignent : huit points stationnaires deviennent quatre.', 'Poser s=sin(2θ)∈[-1,1] : f=r⁴(1-s²/2)+(ar²/2)s est une fonction concave de s. Son minimum est atteint à une extrémité ; son maximum est au sommet lorsque celui-ci est dans [-1,1].', f'On obtient min f=r⁴/2-|a|r²/2={fmin:.6g}. Max f=r⁴+a²/8 si |a|≤2r², sinon r⁴/2+|a|r²/2={fmax:.6g}.'],
        ['Cercle compact et rayon strictement positif : minimum et maximum existent. Les points stationnaires sont obtenus par factorisation exacte de la dérivée ; la figure n’est pas un algorithme de recherche.'],table('Stationnaires et multiplicateur ∇f=μ∇g',['θ (rad)','x','y','f','μ','Nature'],[[z['theta'],z['x'],z['y'],z['value'],z['multiplier'],z['classification']] for z in rows]))

COMPUTE={name:globals()[name] for name in ('monomes_newton','intersection_bezout','resultant_elimination','groebner_ordre','symetriques','singularites','homogenisation','formes_quadratiques','positivite_motzkin','lagrange_contrainte')}
