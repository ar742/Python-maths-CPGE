"""Calcul différentiel CPGE : huit laboratoires déterministes, sans SciPy.

Les résultats théoriques et les diagnostics numériques sont présentés séparément.
Les jacobiennes ont les composantes en lignes, les variables en colonnes.
"""
from __future__ import annotations
import math
import numpy as np


def number(data, key, default, lo, hi, integer=False):
    v = data.get(key, default)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise ValueError(f"{key} doit être un nombre fini.")
    if not lo <= v <= hi or (integer and v != int(v)):
        raise ValueError(f"{key} doit être entre {lo} et {hi}" + (" et entier." if integer else "."))
    return int(v) if integer else float(v)


def choice(d, key, default, values):
    v = d.get(key, default)
    if v not in values:
        raise ValueError(f"Choix inconnu pour {key}.")
    return v


def series(label, x, y, color="green", kind="line"):
    return dict(label=label, x=np.asarray(x).tolist(), y=np.asarray(y).tolist(), color=color, kind=kind)


def chart(title, xlabel, ylabel, data, logx=False, logy=False, equal=False):
    return dict(title=title, xlabel=xlabel, ylabel=ylabel, series=data, logx=logx, logy=logy, equal=equal)


def metric(label, value, note=""):
    return dict(label=label, value=value if isinstance(value, str) else float(value), note=note)


def table(headers, rows):
    return dict(headers=headers, rows=rows)


def matrix_text(A):
    return " ; ".join("[" + ", ".join(f"{x:.6g}" for x in row) + "]" for row in np.asarray(A))


def positive(values):
    """Plancher graphique, jamais utilisé dans les métriques ou les valeurs exportées."""
    return np.maximum(values, 1e-16)


def central_jacobian(f, x, h=1e-5):
    x = np.asarray(x, dtype=float)
    basis = np.eye(len(x))
    return np.column_stack([(f(x+h*u)-f(x-h*u))/(2*h) for u in basis])


def coordinates(q, mode):
    r, t = q[:2]
    if mode == "polaire":
        return np.array([r*math.cos(t), r*math.sin(t)])
    if mode == "cylindrique":
        return np.array([r*math.cos(t), r*math.sin(t), q[2]])
    p = q[2]
    return np.array([r*math.cos(t)*math.sin(p), r*math.sin(t)*math.sin(p), r*math.cos(p)])


def coordinate_jacobian(q, mode):
    r, t = q[:2]
    c, s = math.cos(t), math.sin(t)
    if mode == "polaire":
        return np.array([[c, -r*s], [s, r*c]])
    if mode == "cylindrique":
        return np.array([[c, -r*s, 0], [s, r*c, 0], [0, 0, 1]])
    p = q[2]
    u, v = math.sin(p), math.cos(p)
    return np.array([[c*u, -r*s*u, r*c*v], [s*u, r*c*u, r*s*v], [v, 0, -r*u]])


def project(points):
    p = np.asarray(points)
    return p if p.shape[-1] == 2 else p @ np.array([[1, 0], [.35, .25], [0, 1]])


def jacobiennes(d):
    mode = choice(d, "mode", "spherique", ["polaire", "cylindrique", "spherique"])
    r = number(d, "r", 2, 0, 3)
    t = math.radians(number(d, "theta", 35, -180, 180))
    p = math.radians(number(d, "phi", 65, 0, 180))
    z = number(d, "z", .5, -2, 2)
    h = number(d, "h", .2, .01, .4)
    q = np.array([r, t] if mode == "polaire" else [r, t, p if mode == "spherique" else z])
    F = lambda a: coordinates(a, mode)
    J = coordinate_jacobian(q, mode)
    det = -r*r*math.sin(p) if mode == "spherique" else r
    nonsingular = r > 0 and (mode != "spherique" or 0 < p < math.pi)
    mesh = []
    if mode == "spherique":
        for phi in np.linspace(.12, math.pi-.12, 8):
            a = project([coordinates([max(r,.5), theta, phi], mode) for theta in np.linspace(-math.pi,math.pi,120)])
            mesh.append(series("Grille sphérique", a[:,0], a[:,1], "mint"))
        for theta in np.linspace(-math.pi, math.pi, 9):
            a = project([coordinates([max(r,.5), theta, phi], mode) for phi in np.linspace(0,math.pi,100)])
            mesh.append(series("Grille sphérique", a[:,0], a[:,1], "mint"))
    else:
        for rad in np.linspace(.4,3,7):
            a = project([F(np.r_[rad, theta] if mode == "polaire" else np.r_[rad,theta,z]) for theta in np.linspace(-math.pi,math.pi,120)])
            mesh.append(series("Grille polaire", a[:,0], a[:,1], "mint"))
    # Une face paramétrique (ρ, θ) à troisième coordonnée fixée ; pas un volume 3D.
    perimeter = np.array([[0,0],[h,0],[h,h],[0,h],[0,0]])
    fine = np.vstack([np.linspace(a,b,25,endpoint=False) for a,b in zip(perimeter[:-1],perimeter[1:])])
    fine = np.vstack([fine,fine[0]])
    offsets = np.zeros((len(fine),len(q))); offsets[:,:2] = fine
    exact = project([F(q+u) for u in offsets])
    affine = project(F(q)+offsets @ J.T)
    mesh += [series("Face transformée", exact[:,0],exact[:,1]), series("Approximation affine",affine[:,0],affine[:,1],"rose")]
    u = np.ones(len(q)); u /= np.linalg.norm(u)
    steps = np.geomspace(1e-6,.4,80)
    errors = np.array([np.linalg.norm(F(q+s*u)-F(q)-s*J@u) for s in steps])
    return dict(metrics=[metric("Déterminant signé",det,"Ordre : (ρ, θ, φ) en sphérique"),
                         metric("Facteur de mesure",abs(det),"|det J|, dans le domaine d’une carte régulière"),
                         metric("Erreur de la jacobienne centrée",np.linalg.norm(central_jacobian(F,q)-J),"Pas 10⁻⁵ ; diagnostic numérique")],
        charts=[chart("Coordonnées et approximation locale"+(" · projection 3D" if len(q)==3 else ""),"x + 0,35y" if len(q)==3 else "x","z + 0,25y" if len(q)==3 else "y",mesh,equal=True),
                chart("Le reste après la différentielle", "Pas h", "‖F(q+hu)−F(q)−hJu‖",[series("Reste",steps,positive(errors)),series("Repère h²",steps,steps**2,"gold")],True,True)],
        table=table(["Objet","Valeur"],[["Point image",matrix_text([F(q)])],["Jacobienne J",matrix_text(J)],["Conditionnement 2",float(np.linalg.cond(J)) if nonsingular else "Singularité de coordonnées"]]),
        notes=["Les colonnes de J sont les images des directions de coordonnées. La face dessinée varie ρ et θ ; la troisième coordonnée reste fixe.",
               "En sphérique, le déterminant est −ρ² sin φ avec cet ordre des variables. L’intégration utilise sa valeur absolue.",
               "La carte est singulière à ρ=0 et aux pôles. Il faut aussi couper l’angle azimutal pour obtenir une carte injective. La formule F reste différentiable à ces paramètres."],
        theory=dict(point=F(q).tolist(),jacobian=J.tolist(),determinant=det,regular=nonsingular,remainder=errors.tolist(),steps=steps.tolist()))


def ellipse_integral(a, b, alpha=3, beta=1):
    return 2*alpha*a**4*b/15-beta*a*b**3*math.pi/16


def ellipse_quadrature(a,b,alpha,beta,order, jacobian=True):
    x,w=np.polynomial.legendre.leggauss(order)
    r=(x+1)/2; theta=(x+1)*math.pi/4
    R,T=np.meshgrid(r,theta,indexing="ij")
    values=alpha*(a*R*np.cos(T))**3-beta*(b*R*np.sin(T))**2
    if jacobian: values=values*a*b*R
    return float(np.sum(values*w[:,None]*w[None,:])*math.pi/8)


def elliptique(d):
    a=number(d,"a",3,.2,5);b=number(d,"b",2,.2,5)
    alpha=number(d,"alpha",3,0,5);beta=number(d,"beta",1,0,5)
    order=number(d,"order",12,2,64,True)
    exact=ellipse_integral(a,b,alpha,beta)
    numerical=ellipse_quadrature(a,b,alpha,beta,order)
    wrong=ellipse_quadrature(a,b,alpha,beta,order,False)
    data=[];theta=np.linspace(0,math.pi/2,120)
    for r in np.linspace(.1,1,10): data.append(series("Grille transformée",a*r*np.cos(theta),b*r*np.sin(theta),"mint"))
    for t in np.linspace(0,math.pi/2,10): data.append(series("Grille transformée",[0,a*math.cos(t)],[0,b*math.sin(t)],"mint"))
    data.append(series("Frontière de Ω",a*np.cos(theta),b*np.sin(theta)))
    orders=np.arange(2,25)
    err=[abs(ellipse_quadrature(a,b,alpha,beta,int(n))-exact) for n in orders]
    return dict(metrics=[metric("Intégrale exacte",exact,"2αa⁴b/15 − βab³π/16"),metric("Quadrature transformée",numerical,f"Gauss–Legendre : {order} × {order} nœuds"),metric("Sans la jacobienne",wrong,"Expérience volontairement incorrecte")],
        charts=[chart("Un quart de disque devient un quart d’ellipse","x","y",data,equal=True),chart("Convergence de la quadrature","Nœuds par variable","Erreur absolue",[series("Erreur",orders,positive(err))],logy=True)],
        table=table(["Calcul","Valeur"],[["Coefficient de r³ cos³ θ",alpha*a**3],["Coefficient de r² sin² θ",-beta*b**2],["Jacobian |det J|","ab r"],["Erreur absolue",abs(numerical-exact)]]),
        notes=["Ω = {(x,y) : x≥0, y≥0, x²/a²+y²/b²≤1}. On intègre αx³−βy² ; x=ar cos θ et y=br sin θ.",
               "TP du recueil : a=3, b=2, α=3, β=1. La substitution donne 81r³cos³θ−4r²sin²θ, puis le facteur 6r. Le résultat est 324/5−3π/2.",
               "Le recueil imprime 54 et −8 lors de la substitution : ces deux coefficients sont corrigés ici. La quadrature confirme une formule démontrée dans le cours ; elle ne constitue pas sa preuve."],
        theory=dict(exact=exact,numerical=numerical,without_jacobian=wrong,absolute_error=abs(numerical-exact)))


def smooth(x):
    a,b=x
    return math.sin(a)*math.cos(b)+.2*(a*a+b*b)


def smooth_derivatives(x):
    a,b=x
    return (np.array([math.cos(a)*math.cos(b)+.4*a,-math.sin(a)*math.sin(b)+.4*b]),
            np.array([[-math.sin(a)*math.cos(b)+.4,-math.cos(a)*math.sin(b)],[-math.cos(a)*math.sin(b),-math.sin(a)*math.cos(b)+.4]]))


def cubic(x):
    a,b=x
    return a**3+b**3-3*a*a*b-3*a*a


def cubic_derivatives(x):
    a,b=x
    return np.array([3*a*(a-2*b-2),3*(b*b-a*a)]),np.array([[6*(a-b-1),-6*a],[-6*a,6*b]])


def pathology(x):
    a,b=x
    den=a**6+b*b
    return a**3*b/den if den else 0.


def taylor(d):
    mode=choice(d,"mode","lisse",["lisse","cubique","pathologie"])
    x=np.array([number(d,"x",.5,-3,3),number(d,"y",.3,-3,3)])
    angle=math.radians(number(d,"angle",40,-180,180));u=np.array([math.cos(angle),math.sin(angle)])
    h=number(d,"h",.8,.05,1.5)
    if mode=="pathologie":
        ts=np.geomspace(1e-4,.5,100)
        line=np.array([pathology(t*u) for t in ts]);curve=np.array([pathology([t,t**3]) for t in ts])
        return dict(metrics=[metric("Dérivées directionnelles en 0","Toutes nulles","Toute direction fixe"),metric("Chemin y=x³",.5,"Pour x≠0 : f(x,x³)=1/2"),metric("Différentiabilité en 0","Impossible","La continuité est nécessaire")],
            charts=[chart("Une droite et un chemin courbe","t>0","f",[series("Droite tu",ts,line),series("Courbe (t,t³)",ts,curve,"rose")],logx=True),chart("Le test du reste linéaire sur le chemin courbe","t>0","|f(t,t³)| / ‖(t,t³)‖",[series("Quotient du reste",ts,.5/np.sqrt(ts**2+ts**6),"rose")],True,True)],
            table=table(["Chemin","Limite"],[["Direction fixe : f(tu)/t",0],["y=x³ : f(x,x³)",.5],["Valeur en (0,0)",0]]),
            notes=["f(x,y)=x³y/(x⁶+y²) hors de l’origine, f(0,0)=0. Le point de base est fixé à l’origine dans ce mode.","Les dérivées partielles et même toutes les dérivées directionnelles existent et sont nulles. Le chemin y=x³ montre pourtant que f n’est pas continue. Une dérivée directionnelle ne remplace pas une différentielle."],theory=dict(directional_derivatives=0,curved_limit=.5,continuous=False))
    f,df=(smooth,smooth_derivatives) if mode=="lisse" else (cubic,cubic_derivatives)
    g,H=df(x);eig=np.linalg.eigvalsh(H);s=np.linspace(-h,h,150);f0=f(x)
    actual=np.array([f(x+t*u) for t in s]);first=f0+s*(g@u);second=first+.5*s*s*(u@H@u)
    steps=np.geomspace(1e-5,.5,90)
    r1=np.array([abs(f(x+t*u)-f0-t*(g@u)) for t in steps])
    r2=np.array([abs(f(x+t*u)-f0-t*(g@u)-.5*t*t*(u@H@u)) for t in steps])
    critical=np.linalg.norm(g)<1e-10
    classification="Point non critique"
    if critical:
        classification="Selle" if eig[0]<-1e-10 and eig[-1]>1e-10 else "Test Hessien indécis"
        if np.all(eig>1e-10):classification="Minimum local strict"
        if np.all(eig<-1e-10):classification="Maximum local strict"
    return dict(metrics=[metric("Norme du gradient",np.linalg.norm(g)),metric("Valeur propre minimale",eig[0],"Hessienne symétrique"),metric("Diagnostic",classification,"Le test exige un point critique")],
        charts=[chart("Une coupe : fonction, tangente, Taylor 2","t dans x+tu","Valeur",[series("Fonction",s,actual),series("Taylor 1",s,first,"gold"),series("Taylor 2",s,second,"rose")]),chart("Restes de Taylor","Pas t>0","Erreur absolue",[series("Reste ordre 1",steps,positive(r1),"gold"),series("Reste ordre 2",steps,positive(r2),"rose")],True,True)],
        table=table(["Objet","Valeur"],[["Gradient",matrix_text([g])],["Hessienne",matrix_text(H)],["Spectre",matrix_text([eig])],["f(x)",f0]]),
        notes=["Les courbes suivent une direction unitaire fixe. Pour une fonction C³, les restes après Taylor 1 et 2 sont O(t²) et O(t³). En C² seulement, le second reste est o(t²).", "Correction de l’exercice 1 : (−2,−2) et (2/3,−2/3) sont des selles, avec det H=−72 et −24. À (0,0), H est dégénérée et f(0,y)=y³ exclut un extremum. Aucun des trois points n’est un extremum local.","Sous environ 10⁻⁵, les soustractions peuvent masquer l’ordre du reste. Le plancher 10⁻¹⁶ des graphiques est purement visuel ; les valeurs brutes sont exportées."],
        theory=dict(gradient=g.tolist(),hessian=H.tolist(),eigenvalues=eig.tolist(),classification=classification,steps=steps.tolist(),remainder1=r1.tolist(),remainder2=r2.tolist()))


def determinant_derivative(A,H):
    """Formule par cofacteurs, valable même si A est singulière, toute dimension."""
    A=np.asarray(A,dtype=float);H=np.asarray(H,dtype=float);n=len(A)
    return float(sum((-1)**(i+j)*np.linalg.det(np.delete(np.delete(A,i,0),j,1))*H[i,j] for i in range(n) for j in range(n)))


def inverse_derivative(A,H):
    inv=np.linalg.inv(A)
    return -inv@H@inv


def matrices(d):
    A=np.array([[number(d,"a",1,-3,3),number(d,"b",.6,-3,3)],[number(d,"c",-.2,-3,3),number(d,"d",1.5,-3,3)]])
    H=np.array([[.3,1],[-.7,.2]])
    det=float(np.linalg.det(A));dd=determinant_derivative(A,H);s=np.linspace(-.5,.5,160)
    steps=np.geomspace(1e-5,.2,80)
    deterrors=np.array([abs(np.linalg.det(A+t*H)-det-t*dd) for t in steps])
    curves=[series("Reste déterminant",steps,positive(deterrors),"gold")]
    rows=[["A",matrix_text(A)],["H (direction)",matrix_text(H)],["D det(A)[H]",dd]]
    invertible=abs(det)>1e-12
    invnorm="Non définie";der=None
    if invertible:
        inv=np.linalg.inv(A);der=inverse_derivative(A,H);invnorm=float(np.linalg.norm(der))
        valid=[t for t in steps if abs(np.linalg.det(A+t*H))>1e-12]
        err=[np.linalg.norm(np.linalg.inv(A+t*H)-inv-t*der) for t in valid]
        curves.append(series("Reste inverse",valid,positive(err),"rose"))
        rows += [["D inv(A)[H]",matrix_text(der)],["Conditionnement 2",float(np.linalg.cond(A))],["det A × Tr(A⁻¹H)",det*float(np.trace(inv@H))]]
    return dict(metrics=[metric("det A",det),metric("D det(A)[H]",dd,"Formule par cofacteurs"),metric("‖D inv(A)[H]‖F",invnorm,"−A⁻¹HA⁻¹ ; ordre des facteurs essentiel")],
        charts=[chart("Le déterminant le long d’une droite matricielle","t","det(A+tH)",[series("Déterminant",s,[np.linalg.det(A+t*H) for t in s]),series("Approximation affine",s,det+s*dd,"gold")]),chart("Restes des applications matricielles","Pas t","Norme du reste",curves,True,True)],
        table=table(["Objet","Valeur"],rows),
        notes=["Le déterminant est un polynôme, donc différentiable même aux matrices singulières. La différentielle de l’inverse n’est définie que sur GLₙ(R).", "Le calcul de l’inverse est suspendu lorsque |det A|≤10⁻¹², seuil numérique déclaré ; le déterminant reste étudié. Les pas rencontrant ce seuil sont omis de la courbe de l’inverse.","À I, D det(I)[H]=Tr H : c’est le passage du groupe SLₙ à son algèbre de Lie. Une matrice mal conditionnée amplifie le reste et les erreurs d’arrondi."],theory=dict(A=A.tolist(),H=H.tolist(),determinant=det,det_derivative=dd,inverse_derivative=None if der is None else der.tolist()))


def rotated_spd(a,b,angle):
    c,s=math.cos(angle),math.sin(angle);Q=np.array([[c,-s],[s,c]])
    return Q@np.diag([a,b])@Q.T


def rayleigh_value_gradient(A,x):
    S=(A+A.T)/2;den=float(x@x)
    if den==0:raise ValueError("Le quotient de Rayleigh est indéfini en zéro.")
    value=float(x@S@x/den)
    return value,2*(S@x-value*x)/den


def optimisation(d):
    mode=choice(d,"mode","quadratique",["quadratique","rayleigh"])
    a=number(d,"lambda1",1,.2,5);b=number(d,"lambda2",4,.2,10)
    theta=math.radians(number(d,"rotation",30,-90,90));A=rotated_spd(a,b,theta)
    angle=math.radians(number(d,"angle",65,-180,180));x=np.array([math.cos(angle),math.sin(angle)])
    factor=number(d,"factor",.8,.1,2.5);count=number(d,"steps",25,0,50,True)
    if mode=="rayleigh":
        value,g=rayleigh_value_gradient(A,x);angles=np.linspace(-math.pi,math.pi,300)
        values=[rayleigh_value_gradient(A,np.array([math.cos(t),math.sin(t)]))[0] for t in angles]
        steps=np.geomspace(1e-5,.5,80);eigangle=theta if a<=b else theta+math.pi/2
        errors=[abs(rayleigh_value_gradient(A,np.array([math.cos(eigangle+t),math.sin(eigangle+t)]))[0]-min(a,b)) for t in steps]
        return dict(metrics=[metric("Quotient de Rayleigh",value),metric("‖∇R(x)‖",np.linalg.norm(g)),metric("Intervalle spectral",f"[{min(a,b):g} ; {max(a,b):g}]","Bornes exactes pour A symétrique")],charts=[chart("Quotient sur le cercle unité","Angle (degrés)","R(u)",[series("Quotient",np.degrees(angles),values),series("Direction choisie",[math.degrees(angle)],[value],"rose","dots")]),chart("Près d’un vecteur propre minimal","Écart angulaire t","R(u(t))−λmin",[series("Erreur",steps,positive(errors)),series("(λmax−λmin)t²",steps,positive(abs(b-a)*steps**2),"gold")],True,True)],table=table(["Objet","Valeur"],[["A",matrix_text(A)],["Gradient",matrix_text([g])]]),notes=["Pour A symétrique : ∇R(x)=2(Ax−R(x)x)/‖x‖². Les points stationnaires non nuls sont les vecteurs propres.","Si A n’est pas symétrique, le quotient ne dépend que de S=(A+Aᵀ)/2 ; il faut employer S dans le gradient.","L’erreur du quotient est quadratique près d’un vecteur propre. Si les deux valeurs propres coïncident, le quotient est constant."],theory=dict(A=A.tolist(),value=value,gradient=g.tolist(),eigenvalues=sorted([a,b])))
    B=np.array([1.,-.5]);star=np.linalg.solve(A,B)
    x0=np.array([number(d,"x",-1.5,-3,3),number(d,"y",2,-3,3)]);alpha=factor/max(a,b)
    path=[x0];cost=lambda v:float(.5*(v-star)@A@(v-star))
    for _ in range(count):path.append(path[-1]-alpha*(A@path[-1]-B))
    path=np.array(path);newton=x0-np.linalg.solve(A,A@x0-B)
    angles=np.linspace(0,2*math.pi,180);Q=np.linalg.eigh(A)[1];eigen=np.linalg.eigvalsh(A)
    contours=[]
    for level in [.2,.8,2,5]:
        p=star+np.column_stack([np.cos(angles),np.sin(angles)])@np.diag(np.sqrt(2*level/eigen))@Q.T
        contours.append(series("Niveaux de f−f*",p[:,0],p[:,1],"mint"))
    contours += [series("Descente",path[:,0],path[:,1]),series("Newton : un pas",[x0[0],newton[0]],[x0[1],newton[1]],"rose"),series("Minimum",[star[0]],[star[1]],"gold","dots")]
    costs=[cost(v) for v in path]
    return dict(metrics=[metric("Pas α",alpha,"α = facteur / λmax"),metric("Écart final f−f*",costs[-1]),metric("Erreur de Newton après un pas",np.linalg.norm(newton-star),"Quadratique à Hessienne inversible")],charts=[chart("Trajectoires sur une quadratique convexe","x","y",contours,equal=True),chart("Écart au minimum","Itération","f(xₖ)−f*",[series("Descente",np.arange(len(path)),positive(costs)),series("Newton",[0,1],positive([cost(x0),cost(newton)]),"rose")],logy=True)],table=table(["Objet","Valeur"],[["A",matrix_text(A)],["B",matrix_text([B])],["x*",matrix_text([star])],["Condition 0<α<2/λmax",factor<2],["Facteur spectral",float(max(abs(1-alpha*a),abs(1-alpha*b)))]]),notes=["Pour f(x)=½xᵀAx−Bᵀx avec A symétrique définie positive : ∇f=Ax−B, H=A et x*=A⁻¹B.","La descente converge pour tout départ si 0<α<2/λmax. Au facteur 2, une composante peut osciller ; au-delà, elle peut diverger. L’échelle du graphique s’adapte à la trajectoire.","La convexité C² exige une Hessienne positive semi-définie. Une Hessienne définie positive est une condition plus forte ; le recueil confond ces deux notions."],theory=dict(A=A.tolist(),B=B.tolist(),minimum=star.tolist(),alpha=alpha,path=path.tolist(),costs=costs,newton=newton.tolist()))


def matrix_exp(A):
    """Exponential par Taylor avec réduction de norme, puis carrés successifs.

    Algorithme pédagogique pour les petites matrices bornées de ces laboratoires.
    Ne prétend pas remplacer une bibliothèque de calcul scientifique généraliste.
    """
    A=np.asarray(A,dtype=float);norm=np.linalg.norm(A,ord=np.inf)
    scale=max(0,int(math.ceil(math.log2(norm/.5)))) if norm else 0
    C=A/(2**scale);out=np.eye(len(A));term=out.copy()
    for k in range(1,65):
        term=term@C/k;out+=term
        if np.linalg.norm(term,ord=np.inf)<1e-17:break
    for _ in range(scale):out=out@out
    return out


def lie_project(A,group):
    if group=="SL":return A-np.trace(A)/len(A)*np.eye(len(A))
    if group=="SO":return (A-A.T)/2
    return np.array(A,copy=True)


def bracket(A,B):
    return A@B-B@A


def lie(d):
    group=choice(d,"group","SO",["GL","SL","SO"]);n=number(d,"n",3,2,3,True)
    a=number(d,"a",.8,-2,2);b=number(d,"b",1,-2,2);c=number(d,"c",.6,-2,2)
    t=number(d,"t",1,-2,2)
    raw=np.array([[a,b],[-c,-.3]]) if n==2 else np.array([[a,b,.2],[-c,-.3,.8],[.1,-.4,.5]])
    other=np.array([[.2,-.3],[.9,-.1]]) if n==2 else np.array([[.2,-.3,.7],[.9,-.1,.1],[-.5,.4,.3]])
    X=lie_project(raw,group);Y=lie_project(other,group);C=bracket(X,Y);E=matrix_exp(t*X)
    s=np.geomspace(1e-4,.15,65)
    tangent=[np.linalg.norm((matrix_exp(h*X)-np.eye(n))/h-X) for h in s]
    comm=[np.linalg.norm((matrix_exp(h*X)@matrix_exp(h*Y)@matrix_exp(-h*X)@matrix_exp(-h*Y)-np.eye(n))/h**2-C) for h in s]
    angles=np.linspace(0,2*math.pi,180);circle=np.column_stack([np.cos(angles),np.sin(angles)])
    if n==3:circle=np.column_stack([circle,np.zeros(len(circle))])
    before=project(circle);after=project(circle@E.T)
    curves=[series("Cercle initial",before[:,0],before[:,1],"mint"),series("exp(tX) · cercle",after[:,0],after[:,1])]
    for i in range(n):
        p=project(np.vstack([np.zeros(n),E[:,i]]));curves.append(series("Images des axes",p[:,0],p[:,1],"gold"))
    det=float(np.linalg.det(E));expected=math.exp(t*float(np.trace(X)))
    return dict(metrics=[metric("Tr X",np.trace(X),"SL : trace nulle ; SO : Xᵀ=−X"),metric("det exp(tX)",det,"Valeur théorique : exp(t Tr X)"),metric("‖[X,Y]‖F",np.linalg.norm(C),"[X,Y]=XY−YX")],charts=[chart(f"{group}({n}) : transformation"+(" · projection 3D" if n==3 else ""),"x + 0,35y" if n==3 else "x","z + 0,25y" if n==3 else "y",curves,equal=True),chart("Retrouver le tangent et le crochet","Pas s","Norme de l’erreur",[series("(exp(sX)−I)/s → X",s,positive(tangent)),series("Commutateur / s² → [X,Y]",s,positive(comm),"rose")],True,True)],table=table(["Objet","Valeur"],[["X",matrix_text(X)],["Y",matrix_text(Y)],["[X,Y]",matrix_text(C)],["exp(tX)",matrix_text(E)],["Erreur sur det(exp)",abs(det-expected)],["‖EᵀE−I‖F",float(np.linalg.norm(E.T@E-np.eye(n)))]]),notes=["GLₙ : toute matrice est tangente. SLₙ : différencier det γ(t)=1 donne Tr X=0. SOₙ : différencier γ(t)ᵀγ(t)=I donne Xᵀ+X=0.","La réciproque se vérifie avec exp(tX). Le cercle est dessiné dans le plan des deux premiers axes ; en dimension 3, seule sa projection est visible.","Dans SO(2), l’algèbre est de dimension 1 et tous les crochets sont nuls. SO(3) permet d’observer la non-commutativité. Pour les petits pas, le quotient par s² amplifie l’arrondi.","L’exponentielle est calculée par réduction de norme, série de Taylor puis carrés successifs. Ce n’est pas une paramétrisation globale surjective de tous les groupes de matrices."],theory=dict(X=X.tolist(),Y=Y.tolist(),bracket=C.tolist(),exponential=E.tolist(),determinant=det,expected_determinant=expected,orthogonality_error=float(np.linalg.norm(E.T@E-np.eye(n)))))


def gaussian(A,B):
    A=np.asarray(A,dtype=float);B=np.asarray(B,dtype=float)
    if A.ndim!=2 or A.shape[0]!=A.shape[1] or B.shape!=(len(A),) or not np.isfinite(A).all() or not np.isfinite(B).all():
        raise ValueError("Dimensions ou valeurs incompatibles pour la gaussienne.")
    if not np.allclose(A,A.T,rtol=0,atol=1e-12):raise ValueError("A doit être symétrique.")
    try:L=np.linalg.cholesky(A)
    except np.linalg.LinAlgError as e:raise ValueError("A doit être définie positive.") from e
    mu=np.linalg.solve(A,B);cov=np.linalg.solve(A,np.eye(len(A)))
    logI=len(A)*math.log(2*math.pi)/2-np.log(np.diag(L)).sum()+float(B@mu)/2
    return dict(log_integral=float(logI),integral=math.exp(logI),mean=mu,covariance=cov,
                gradient_B=mu,hessian_B=cov,gradient_A=-.5*(cov+np.outer(mu,mu)))


def gaussian_mass_quadrature(A,B,order,width=6):
    """Masse normalisée de la marginale 2D sur μ±width écarts types.

    Dans le labo, les autres dimensions sont indépendantes et intégrées exactement.
    """
    g=gaussian(A,B);mu=g["mean"];cov=g["covariance"]
    nodes,weights=np.polynomial.legendre.leggauss(order)
    scales=width*np.sqrt(np.diag(cov))
    x=mu[0]+scales[0]*nodes;y=mu[1]+scales[1]*nodes
    X,Y=np.meshgrid(x,y,indexing="ij");delta=np.stack([X-mu[0],Y-mu[1]],axis=-1)
    exponent=np.einsum("...i,ij,...j->...",delta,A,delta)
    return float(np.sum(np.exp(-.5*exponent)*weights[:,None]*weights[None,:])*np.prod(scales)*math.sqrt(np.linalg.det(A))/(2*math.pi))


def gaussienne(d):
    n=number(d,"n",3,2,8,True);a=number(d,"lambda1",.7,.2,5);b=number(d,"lambda2",2,.2,5)
    gamma=number(d,"gamma",1,.2,5);angle=math.radians(number(d,"rotation",35,-90,90))
    B=np.zeros(n);B[:2]=[number(d,"b1",1,-3,3),number(d,"b2",-.5,-3,3)]
    A=np.eye(n)*gamma;A[:2,:2]=rotated_spd(a,b,angle);g=gaussian(A,B)
    order=number(d,"order",32,4,80,True);mass=gaussian_mass_quadrature(A[:2,:2],B[:2],order)
    mu=g["mean"][:2];cov=g["covariance"][:2,:2];eig,Q=np.linalg.eigh(cov)
    ts=np.linspace(0,2*math.pi,180);contours=[]
    for radius in [1,2,3]:
        p=mu+radius*np.column_stack([np.cos(ts),np.sin(ts)])@np.diag(np.sqrt(eig))@Q.T
        contours.append(series(f"Mahalanobis : rayon {radius}",p[:,0],p[:,1],["green","gold","mint"][radius-1]))
    contours.append(series("Centre μ=A⁻¹B",[mu[0]],[mu[1]],"rose","dots"))
    v=np.linspace(-3,3,140);logvalues=[]
    for q in v:
        rhs=B.copy();rhs[0]=q;logvalues.append(gaussian(A,rhs)["log_integral"])
    tangent=g["log_integral"]+(v-B[0])*mu[0]
    orders=[4,8,12,20,32,48,64,80];masses=[gaussian_mass_quadrature(A[:2,:2],B[:2],q) for q in orders]
    return dict(metrics=[metric("Intégrale I(A,B)",g["integral"],"(2π)ⁿᐟ² det(A)⁻¹ᐟ² exp(½BᵀA⁻¹B)"),metric("log I(A,B)",g["log_integral"],"Forme stable pour les calculs"),metric("I numérique / I exact",mass,f"Quadrature {order}² ; troncature à ±6σ")],charts=[chart("Gaussienne décentrée : marginale 2D","x₁","x₂",contours,equal=True),chart("Dériver log I par rapport à B₁","B₁","log I",[series("log I",v,logvalues),series("Tangente au B₁ choisi",v,tangent,"rose")]),chart("Quadrature et troncature","Nœuds par variable","|I numérique / I exact − 1|",[series("Erreur observée",orders,positive(np.abs(np.array(masses)-1)))],logy=True)],table=table(["Objet","Valeur"],[["A",matrix_text(A)],["B",matrix_text([B])],["μ = ∇B log I",matrix_text([g["mean"]])],["Σ = HessB log I",matrix_text(g["covariance"])],["Gradient matriciel en A",matrix_text(g["gradient_A"])],["Borne de masse omise (troncature seule)",2*math.erfc(6/math.sqrt(2))]]),notes=["A est construite symétrique définie positive. Les deux premiers axes peuvent tourner ; les autres coordonnées sont indépendantes, de précision γ et de centre 0.","Compléter le carré donne μ=A⁻¹B et Σ=A⁻¹. La densité normalisée a ces moyenne et covariance. Les ellipses représentent des niveaux de densité, et non des intervalles de confiance.","∇B log I=μ ; HessB log I=Σ. Pour H symétrique, D_A log I[H]=−½Tr((Σ+μμᵀ)H). Le cours justifie les dérivations sous l’intégrale.","La quadrature porte sur le rectangle μ±6σ des deux premières coordonnées ; les autres intégrales sont exactes. La masse omise est ≤4Φ(−6). Cette borne ne couvre pas l’erreur de quadrature. Un déterminant positif ne suffit pas à garantir l’intégrabilité."],theory=dict(A=A.tolist(),B=B.tolist(),integral=g["integral"],log_integral=g["log_integral"],mean=g["mean"].tolist(),covariance=g["covariance"].tolist(),gradient_A=g["gradient_A"].tolist(),numerical_ratio=mass,omitted_mass_bound=2*math.erfc(6/math.sqrt(2))))


def fubini_rectangle(epsx,epsy):
    if not 0<epsx<=1 or not 0<epsy<=1:raise ValueError("Coupures strictement positives et ≤1 requises.")
    return math.pi/4-math.atan(epsx)-math.atan(1/epsy)+math.atan(epsx/epsy)


def green_boundary(order=24):
    nodes,w=np.polynomial.legendre.leggauss(order);x=(nodes+1)/2
    return float(np.sum((x**4+x**3-2*x*x)*w)/2)


def green_fubini(d):
    mode=choice(d,"mode","green",["green","fubini"])
    sign=number(d,"orientation",1,-1,1,True)
    if sign not in [-1,1]:raise ValueError("Orientation : −1 ou +1.")
    ex=10**number(d,"logx",-2,-6,0);ey=10**number(d,"logy",-2,-6,0)
    if mode=="green":
        x=np.linspace(0,1,160)
        mesh=[series("Parabole : aller",x,x*x),series("Droite : retour",x,x,"rose")]
        for q in np.linspace(.1,.9,9):mesh.append(series("Domaine",[q,q],[q*q,q],"mint"))
        return dict(metrics=[metric("Intégrale curviligne",-sign*13/60,"∮ y(y+x) dx"),metric("Quadrature de la frontière",sign*green_boundary()),metric("Aire de Ω",1/6,"Entre y=x² et y=x")],charts=[chart("La frontière et son orientation positive","x","y",mesh,equal=True),chart("Comparer les intégrandes après paramétrage","x","Intégrande",[series("Parabole",x,sign*(x**4+x**3)),series("Droite, sens retour",x,-sign*2*x*x,"rose")])],table=table(["Terme","Valeur"],[["Orientation choisie","Positive" if sign==1 else "Négative"],["Parabole",sign*(1/5+1/4)],["Droite",-sign*2/3],["Green : −∬(2y+x) dxdy",-sign*13/60]]),notes=["L’orientation positive suit la parabole de (0,0) à (1,1), puis la droite en retour : le domaine reste à gauche. Le premier dessin indique ce sens positif ; le choix négatif inverse les signes des intégrales.","Green–Riemann avec P=y(y+x), Q=0 donne ∮P dx=−∬(2y+x) dxdy=−13/60. Inverser l’orientation change le signe."],theory=dict(exact=-sign*13/60,numerical=sign*green_boundary(),area=1/6))
    cutoff=np.geomspace(1e-6,.2,130)
    curves=[]
    for power,color in [(.5,"green"),(1,"gold"),(2,"rose")]:
        curves.append(series(f"εx=εy^{power:g}",cutoff,[fubini_rectangle(q**power,q) for q in cutoff],color))
    value=fubini_rectangle(ex,ey)
    return dict(metrics=[metric("Intégrale sur le rectangle tronqué",value,"[εx,1] × [εy,1]"),metric("y intégré d’abord, puis x",math.pi/4,"Intégrales itérées ; point exceptionnel exclu"),metric("x intégré d’abord, puis y",-math.pi/4,"Deux valeurs différentes")],charts=[chart("Le chemin des coupures change la limite","εy>0","Intégrale tronquée",curves,logx=True),chart("Rectangle tronqué","x","y",[series("Frontière",[ex,1,1,ex,ex],[ey,ey,1,1,ey])],equal=True)],table=table(["Objet","Valeur"],[["εx",ex],["εy",ey],["Rapport εx/εy",ex/ey],["Limite si rapport → q","−π/4 + arctan q"],["Intégrabilité absolue","Non : divergence logarithmique"]]),notes=["f(x,y)=(x²−y²)/(x²+y²)². Chaque rectangle tronqué évite la singularité et possède une intégrale ordinaire.","En coordonnées polaires, |f| dxdy=|cos(2θ)| dr dθ/r : l’intégrale absolue diverge près de 0. On ne peut donc pas permuter les intégrales par Fubini.","Les intégrales intérieures divergent au point extérieur 0 ; les valeurs affichées désignent les intégrales itérées des fonctions définies presque partout. Elles ne définissent pas une intégrale double de Lebesgue sur le carré.","Pour εx=εy, l’intégrale tronquée vaut exactement 0 par antisymétrie. Faire tendre le rapport vers 0 ou +∞ produit les deux limites −π/4 et +π/4."],theory=dict(truncated=value,epsilon_x=ex,epsilon_y=ey,y_first=math.pi/4,x_first=-math.pi/4,absolutely_integrable=False))


LABS={"jacobiennes":jacobiennes,"elliptique":elliptique,"taylor":taylor,"matrices":matrices,"optimisation":optimisation,"lie":lie,"gaussienne":gaussienne,"green_fubini":green_fubini}


def calculate(data):
    if not isinstance(data,dict):raise ValueError("Un objet de paramètres est attendu.")
    lab=choice(data,"lab","jacobiennes",LABS)
    result=LABS[lab](data)
    result["lab"]=lab
    result["parameters"]={k:v for k,v in data.items() if k!="lab"}
    return result
