"""Douze laboratoires d'algèbre : certificats rationnels et figures NumPy.

Les sept laboratoires de ce fichier ne déduisent jamais une identité exacte
d'une tolérance numérique. Les cinq laboratoires de réduction sont délégués
à reductions.py. Les seuls textes matriciels sont lus par Fraction.
"""
from __future__ import annotations
import json
import math
import numpy as np
import sympy as sp
try:
    from .calculs_exacts import (X, parse_matrix, parse_vector, serialize_matrix,
        number, rational, choice, metric, series, chart, table, matrix_block,
        step, polynomial_evaluate, invariant_factors, rref_steps, numeric_exp)
except ImportError:
    from calculs_exacts import (X, parse_matrix, parse_vector, serialize_matrix,
        number, rational, choice, metric, series, chart, table, matrix_block,
        step, polynomial_evaluate, invariant_factors, rref_steps, numeric_exp)


def output(lab, parameters, metrics, charts=None, rows=None, notes=None,
           theory=None, matrices=None, steps=None):
    return dict(lab=lab, parameters=parameters, metrics=metrics,
                charts=charts or [], table=rows or table([], []), notes=notes or [],
                theory=theory or {}, matrices=matrices or [], steps=steps or [])


def commutator(A, B):
    return A*B-B*A


def gl_cardinality(n, prime):
    """Cardinal de GL_n(F_p) ; p doit être premier, pas un module quelconque."""
    if not isinstance(n,int) or isinstance(n,bool) or not 1<=n<=6:
        raise ValueError("Dimension entière de 1 à 6 requise.")
    if not isinstance(prime,int) or isinstance(prime,bool) or not sp.isprime(prime):
        raise ValueError("p doit être premier pour désigner F_p.")
    return math.prod(prime**n-prime**k for k in range(n))


def gl2_mod_cardinality(modulus):
    return math.prod(p**(4*(alpha-1))*gl_cardinality(2,int(p))
                     for p,alpha in sp.factorint(modulus).items())


def modular_inverse(A, modulus):
    """A⁻¹ = det(A)⁻¹ adj(A) ; aucune division par un non-unité."""
    A=sp.Matrix(A)
    if A.rows!=A.cols or any(v.q!=1 for v in A):
        raise ValueError("Matrice carrée entière requise pour Z/mZ.")
    if isinstance(modulus,bool) or not isinstance(modulus,int) or modulus<2:
        raise ValueError("Module entier ≥2 requis.")
    det=int(A.det())
    if math.gcd(det,modulus)!=1:return None
    unit=pow(det,-1,modulus)
    return A.adjugate().applyfunc(lambda v:int(v)*unit % modulus)


def anneaux(data):
    ring=choice(data,"ring","Q",("Q","Z","mod"))
    A=parse_matrix(data.get("matrix","2 0;0 1"),square=True)
    modulus=number(data,"modulus",6,2,30,True)
    prime=int(choice(data,"prime","3",("2","3","5","7","11")))
    n=number(data,"dimension",2,1,5,True)
    if ring!="Q" and any(v.q!=1 for v in A):
        raise ValueError("Les coefficients doivent être entiers dans Z ou Z/mZ.")
    det=A.det()
    unit=det!=0 if ring=="Q" else abs(det)==1 if ring=="Z" else math.gcd(int(det),modulus)==1
    inverse=(modular_inverse(A,modulus) if ring=="mod" else A.inv()) if unit else None
    blocks=[matrix_block("A",A),matrix_block("adj(A)",A.adjugate(),"A adj(A)=det(A) I, y compris si A est singulière.")]
    if inverse is not None:blocks.append(matrix_block("A⁻¹"+(f" modulo {modulus}" if ring=="mod" else ""),inverse))
    residues=np.arange(modulus)
    flags=[int(math.gcd(int(k),modulus)==1) for k in residues]
    moduli=list(range(2,31))
    charts=[chart("Unités de Z/mZ","résidu","est inversible (0 ou 1)",
                  [series("gcd(k,m)=1",residues,flags,"green","bars")]),
            chart("Matrices inversibles modulo m, dimension 2","m","|GL₂(Z/mZ)|",
                  [series("Comptage par décomposition chinoise",moduli,[gl2_mod_cardinality(m) for m in moduli])])]
    values=[["Q","det(A) ≠ 0"],["Z","det(A) = ±1"],[f"Z/{modulus}Z","gcd(det(A),m) = 1"]]
    return output("anneaux",dict(ring=ring,matrix=serialize_matrix(A),modulus=modulus,prime=str(prime),dimension=n),
                  [metric("det(A)",str(det)),metric("Inversible dans l'anneau choisi","oui" if unit else "non"),
                   metric(f"|GL_{n}(F_{prime})|",str(gl_cardinality(n,prime)),"p premier ; choix successifs de colonnes indépendantes."),
                   metric(f"|GL₂(Z/{modulus}Z)|",str(gl2_mod_cardinality(modulus)))],charts,
                  table(["Anneau","Condition exacte"],values),
                  ["Un déterminant non nul n'est pas toujours une unité : diag(2,1) n'est inversible ni dans Z ni modulo 6.",
                   "Un anneau Z/mZ avec m composé n'est pas un corps. Sa cardinalité GL₂ se calcule par les puissances premières et le théorème chinois."],
                  dict(det=str(det),unit=bool(unit),inverse=serialize_matrix(inverse) if inverse is not None else None,
                       cardinal=str(gl_cardinality(n,prime)),gl2_mod=str(gl2_mod_cardinality(modulus))),blocks)


def geometrie(data):
    sx=rational(data,"sx",2,-3,3);sy=rational(data,"sy",1,-3,3)
    shear=rational(data,"shear",1,-3,3);lower=rational(data,"lower",1,-3,3)
    A=sp.Matrix([[sx,shear],[0,sy]]);B=sp.Matrix([[1,0],[lower,1]])
    theta=np.linspace(0,2*np.pi,241);circle=np.vstack([np.cos(theta),np.sin(theta)])
    square=np.array([[0,1,1,0,0],[0,0,1,1,0]],dtype=float)
    def transformed(M,points):return np.array(M,dtype=float)@points
    sets=[]
    for name,M,color in (("Cercle initial",sp.eye(2),"mint"),("A",A,"green"),("AB",A*B,"gold"),("BA",B*A,"rose")):
        points=transformed(M,circle);sets.append(series(name,*points,color))
    image=transformed(A,square)
    det=A.det();orientation="directe" if det>0 else "indirecte" if det<0 else "singulière"
    return output("geometrie",{k:float(v) for k,v in dict(sx=sx,sy=sy,shear=shear,lower=lower).items()},
        [metric("det(A)",str(det)),metric("Facteur d'aire",str(abs(det))),metric("Orientation",orientation),
         metric("AB = BA","oui" if A*B==B*A else "non")],
        [chart("Composition : B agit d'abord dans AB","x","y",sets,equal=True),
         chart("Image du carré unité","x","y",[series("Carré",*square,"mint"),series("A(carré)",*image)],equal=True)],
        table(["Objet","Interprétation"],[["det A","Aire orientée des images de e₁,e₂"],["AB","A après B"],["BA","B après A"]]),
        ["GL₂(R) a deux composantes : det>0 et det<0. SL₂(R) est le sous-groupe det=1.",
         "Si sx ou sy est nul, la figure représente la frontière singulière de GL₂ ; les aires s'écrasent."],
        dict(det=str(det),commutator=serialize_matrix(commutator(A,B))),
        [matrix_block(label,M) for label,M in (("A",A),("B",B),("AB",A*B),("BA",B*A),("[A,B]",commutator(A,B)))])


def lie_generators(family):
    if family=="gl":
        return sp.Matrix([[1,1],[0,0]]),sp.Matrix([[0,0],[1,0]]),sp.Matrix([[0,1],[1,0]])
    if family=="sl":
        return sp.Matrix([[0,1],[0,0]]),sp.Matrix([[0,0],[1,0]]),sp.diag(1,-1)
    if family=="so":
        return (sp.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),
                sp.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),
                sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]]))
    if family=="sp":
        G=sp.zeros(4);H=sp.zeros(4);K=sp.diag(1,0,-1,0)
        G[0,2]=1;H[2,0]=1
        return G,H,K
    raise ValueError("Famille de Lie inconnue.")


def symplectic_J(n=2):
    return sp.zeros(n).row_join(sp.eye(n)).col_join((-sp.eye(n)).row_join(sp.zeros(n)))


def lie_membership(A,family):
    if family=="gl":return True
    if family=="sl":return sp.trace(A)==0
    if family=="so":return A.T+A==sp.zeros(A.rows)
    if family=="sp":
        J=symplectic_J(A.rows//2)
        return A.T*J+J*A==sp.zeros(A.rows)
    return False


def lie(data):
    family=choice(data,"family","sl",("gl","sl","so","sp"))
    a=rational(data,"a",1,-2,2);b=rational(data,"b",1,-2,2)
    time=number(data,"time",.5,-2,2);h=number(data,"h",.2,.02,.5)
    X0,Y0,Z=lie_generators(family);A=a*X0;B=b*Y0;C=commutator(A,B)
    jacobi=commutator(A,commutator(B,Z))+commutator(B,commutator(Z,A))+commutator(Z,C)
    dim=A.rows;I=np.eye(dim);Af=np.array(A,dtype=float);Cf=np.array(C,dtype=float)
    def errors(t):
        EA=numeric_exp(t*A);EB=numeric_exp(t*B)
        tangent=np.linalg.norm((EA-I)/t-Af,ord="fro")
        group=EA@EB@numeric_exp(-t*A)@numeric_exp(-t*B)
        return float(tangent),float(np.linalg.norm((group-I)/t**2-Cf,ord="fro"))
    hs=np.geomspace(.02,.5,80);err=np.array([errors(t) for t in hs]);point=errors(h)
    E=numeric_exp(time*A)
    if family=="so":preservation=np.linalg.norm(E.T@E-I,ord="fro");law="EᵀE=I"
    elif family=="sp":
        Jf=np.array(symplectic_J(),dtype=float);preservation=np.linalg.norm(E.T@Jf@E-Jf,ord="fro");law="EᵀJE=J"
    elif family=="sl":preservation=abs(np.linalg.det(E)-1);law="det E=1"
    else:preservation=abs(np.linalg.det(E)-math.exp(time*float(sp.trace(A))));law="det(exp tX)=exp(t tr X)"
    if family=="so":seed=np.array([0.,1.,0.]);axes=(1,2);labels=("y","z")
    elif family=="sp":seed=np.array([1.,0.,1.,0.]);axes=(0,2);labels=("q₁","p₁")
    else:seed=np.array([1.,1.]);axes=(0,1);labels=("x","y")
    times=np.linspace(-2,2,101)
    trajectory=np.array([numeric_exp(t*A)@seed for t in times])
    tangent=np.array([(I+t*Af)@seed for t in times]);selected=E@seed
    trajectory_chart=chart("Une orbite exp(tX)v et sa tangente en t=0",*labels,
        [series("exp(tX)v, −2≤t≤2",trajectory[:,axes[0]],trajectory[:,axes[1]],"green"),
         series("(I+tX)v",tangent[:,axes[0]],tangent[:,axes[1]],"gold"),
         series("Position au temps choisi",[selected[axes[0]]],[selected[axes[1]]],"rose","dots")],equal=True)
    return output("lie",dict(family=family,a=float(a),b=float(b),time=time,h=h),
        [metric("[X,Y] appartient à l'algèbre","oui" if lie_membership(C,family) else "non"),
         metric("Identité de Jacobi","exactement nulle" if jacobi==sp.zeros(dim) else "échec"),
         metric("tr([X,Y])",str(sp.trace(C))),metric("Erreur de tangence",point[0],"Norme de Frobenius ; figure numérique."),
         metric("Erreur du commutateur de groupe",point[1],"Commutateur/h² − [X,Y]."),metric("Résidu de conservation",preservation,law)],
        [chart("Deux passages du groupe à l'algèbre","h","norme de Frobenius",
              [series("(exp(hX)−I)/h − X",hs,err[:,0]),series("Commutateur/h² − [X,Y]",hs,err[:,1],"gold")],logx=True),trajectory_chart],
        table(["Algèbre","Condition"],[["glₙ","toutes les matrices"],["slₙ","tr X=0"],["soₙ","Xᵀ+X=0"],["sp₂ₙ","XᵀJ+JX=0"]]),
        ["Le crochet est XY−YX. La fermeture et Jacobi sont des égalités exactes ; les exponentielles affichées sont numériques.",
         "En dimension finie et caractéristique zéro, [X,Y]=I est impossible : sa trace serait à la fois 0 et n.",
         "Le commutateur de groupe choisi est exp(hX) exp(hY) exp(−hX) exp(−hY), donc le terme de degré 2 a le signe +[X,Y].",
         "Les générateurs contrôlés illustrent des éléments des algèbres indiquées ; ils ne paramètrent pas toute l'algèbre sp₄. L'orbite utilise X et un vecteur initial fixe, avec une vue sur deux coordonnées."],
        dict(closure=bool(lie_membership(C,family)),jacobi=serialize_matrix(jacobi),trace=str(sp.trace(C)),preservation=law),
        [matrix_block("X",A),matrix_block("Y",B),matrix_block("Z",Z),matrix_block("[X,Y]",C),
         dict(label=f"exp({time:g} X) — approximation numérique",entries=[[f"{v:.7g}" for v in row] for row in E],note=law)])


def gauss(data):
    A=parse_matrix(data.get("matrix","1 2 1;2 4 0;1 1 1"))
    b=parse_vector(data.get("vector","1;2;0"),A.rows)
    augmented=A.row_join(b);R,pivots_aug,E,steps=rref_steps(augmented)
    RA,pivots=A.rref();rank=len(pivots);compatible=len(pivots_aug)==rank
    kernel=A.nullspace();image=[A[:,i] for i in pivots]
    particular=sp.zeros(A.cols,1)
    if compatible:
        for row,col in enumerate(pivots):particular[col]=R[row,A.cols]
    blocks=[matrix_block("A",A),matrix_block("b",b),matrix_block("[A|b] réduit",R),
            matrix_block("E (R=E[A|b])",E,"Opérations sur les lignes : elles changent la base du but, sans constituer en général une similitude.")]
    if kernel:blocks.append(matrix_block("Base du noyau",sp.Matrix.hstack(*kernel),"Chaque colonne est un vecteur de Ker A."))
    if image:blocks.append(matrix_block("Base de l'image",sp.Matrix.hstack(*image),"Colonnes pivots de la matrice initiale A, et non de la matrice réduite."))
    if compatible:blocks.append(matrix_block("Solution particulière x₀",particular,"Les variables libres sont fixées à zéro ; toutes les solutions sont x₀+Ker A."))
    grids=[]
    for title,M in (("Système augmenté initial",augmented),("Échelonnement réduit",R)):
        grids.append(chart(title,"colonne","ligne",[],grid=dict(x=list(range(1,M.cols+1)),y=list(range(1,M.rows+1)),z=np.array(M,dtype=float))))
    return output("gauss",dict(matrix=serialize_matrix(A),vector=[str(v) for v in b]),
        [metric("Rang",rank),metric("Dimension du noyau",A.cols-rank),metric("Rang du système augmenté",len(pivots_aug)),
         metric("Compatibilité","oui" if compatible else "non"),metric("Certificat E[A|b]=R","exact" if E*augmented==R else "échec")],grids,
        table(["Colonne pivot dans A","Colonne originale conservée"],[[i+1,str(list(A[:,i]))] for i in pivots]),
        ["Les calculs s'effectuent dans Q, où tout pivot non nul est inversible. Ils ne sont pas transposables sans précaution à Z/mZ.",
         "Une ligne [0 … 0 | c] avec c≠0 démontre l'incompatibilité.",
         "Une réduction par opérations sur les lignes est une équivalence de matrices, pas une réduction d'endomorphisme par similitude."],
        dict(rank=rank,nullity=A.cols-rank,compatible=compatible,pivots=list(pivots),
             solution=[str(v) for v in particular] if compatible else None,
             kernel=[list(map(str,v)) for v in kernel],certificate=bool(E*augmented==R)),blocks,steps)


def pfaffian_terms(A):
    """Développement signé par appariements : (n−1)!! termes en dimension paire."""
    A=sp.Matrix(A)
    if A.rows!=A.cols or A.T!=-A:raise ValueError("Matrice antisymétrique requise.")
    def pairings(indices):
        if not indices:return [(sp.Integer(1),[])]
        i=indices[0];out=[]
        for position in range(1,len(indices)):
            j=indices[position];sign=(-1)**(position+1)
            remaining=indices[1:position]+indices[position+1:]
            for value,pairs in pairings(remaining):out.append((sign*A[i,j]*value,[(i,j)]+pairs))
        return out
    if A.rows%2:return []
    return pairings(list(range(A.rows)))


def pfaffian(A):
    return sp.expand(sum((value for value,_ in pfaffian_terms(A)),sp.Integer(0)))


def pfaffian_family(n,a,b):
    A=sp.zeros(n);coefficients=[a,b,a+b,a-b]
    for k in range(n//2):A[2*k,2*k+1]=coefficients[k];A[2*k+1,2*k]=-coefficients[k]
    for i in range(n-2):A[i,i+2]=1;A[i+2,i]=-1
    return A


def pfaffien(data):
    size_data=dict(data)
    if isinstance(size_data.get("size"),str):
        size_data["size"]=int(choice(size_data,"size","4",("4","6","8")))
    n=number(size_data,"size",4,4,8,True)
    if n not in (4,6,8):raise ValueError("size doit être 4, 6 ou 8.")
    a=rational(data,"a",1,-3,3,True);b=rational(data,"b",2,-3,3,True)
    shear=rational(data,"shear",1,-3,3,True);scale=rational(data,"scale",1,-2,2,True)
    A=pfaffian_family(n,a,b);P=sp.eye(n);P[0,0]=scale;P[0,1]=shear
    B=P.T*A*P;terms=pfaffian_terms(A);pf=pfaffian(A);pfB=pfaffian(B);odd=A[:n-1,:n-1]
    rows=[[" ".join(f"({i+1},{j+1})" for i,j in pairs),str(value)] for value,pairs in terms]
    vals=[float(value) for value,_ in terms]
    return output("pfaffien",dict(size=n,a=int(a),b=int(b),shear=int(shear),scale=int(scale)),
        [metric("Pf(A)",str(pf)),metric("det(A)",str(A.det())),metric("Nombre d'appariements",len(terms)),
         metric("Pf(PᵀAP)",str(pfB)),metric("det(P) Pf(A)",str(P.det()*pf)),metric("Déterminant antisymétrique impair",str(odd.det()))],
        [chart("Contributions signées des appariements","appariement","terme exact",
               [series("Contributions",list(range(1,len(vals)+1)),vals,"green","bars")])],
        table(["Appariement (indices à partir de 1)","Contribution signée"],rows),
        ["Convention Pf([[0,a],[-a,0]])=a ; en dimension 4 : a₁₂a₃₄−a₁₃a₂₄+a₁₄a₂₃.",
         "La loi Pf(PᵀAP)=det(P)Pf(A) vaut même pour P singulière. Ici scale=0 permet de le vérifier.",
         "Une matrice antisymétrique impaire a un déterminant nul en caractéristique différente de 2."],
        dict(pf=str(pf),det=str(A.det()),pf_transformed=str(pfB),congruence=bool(pfB==P.det()*pf),
             det_square=bool(A.det()==pf**2),odd_det=str(odd.det()),terms=len(terms)),
        [matrix_block("A",A),matrix_block("P",P),matrix_block("PᵀAP",B),matrix_block("Sous-matrice antisymétrique impaire",odd)])


def primary_projectors(A):
    """Projecteurs primaires par Bézout ; collisions automatiquement fusionnées.

    Le polynôme minimal est le dernier facteur invariant, et non le produit
    des valeurs propres distinctes quand un bloc de Jordan est présent.
    """
    factors=invariant_factors(A)
    minimal=factors[-1]
    primary=[sp.Poly(f**power,X,domain=sp.QQ).monic() for f,power in sp.factor_list(minimal.as_expr(),X)[1]]
    result=[]
    for f in primary:
        g=minimal.exquo(f);u,v,h=sp.gcdex(f,g)
        if h!=sp.Poly(1,X,domain=sp.QQ):raise ArithmeticError("Facteurs primaires non premiers entre eux.")
        e=(v*g).rem(minimal);P=polynomial_evaluate(A,e)
        result.append(dict(f=f,g=g,u=u,v=v,e=e,P=P))
    return minimal,result


def projecteurs(data):
    mode=choice(data,"mode","bezout",("bezout","oblique"))
    l1=rational(data,"lambda1",1,-3,3,True);l2=rational(data,"lambda2",3,-3,3,True)
    coupling=rational(data,"coupling",1,-2,2);shear=rational(data,"shear",1,-3,3)
    x=rational(data,"x",1,-3,3);y=rational(data,"y",1,-3,3)
    parameters=dict(mode=mode,lambda1=int(l1),lambda2=int(l2),coupling=float(coupling),shear=float(shear),x=float(x),y=float(y))
    if mode=="oblique":
        P=sp.Matrix([[1,-shear],[0,0]]);Q=sp.eye(2)-P;v=sp.Matrix([x,y]);proj=P*v;ortho=sp.Matrix([x,0])
        ts=np.array([-3,3]);points=[series("Image : axe x",ts,np.zeros(2),"green"),series("Noyau : span(shear,1)",float(shear)*ts,ts,"gold"),
            series("Décomposition oblique",[0,float(proj[0]),float(v[0])],[0,float(proj[1]),float(v[1])],"rose"),
            series("Vecteur et projections",[float(v[0]),float(proj[0]),float(ortho[0])],[float(v[1]),float(proj[1]),float(ortho[1])],"mint","dots")]
        return output("projecteurs",parameters,
            [metric("P²=P","exact"),metric("Pᵀ=P","oui" if P.T==P else "non"),metric("‖P‖₂",math.sqrt(1+float(shear)**2)),
             metric("Projection oblique",str(list(proj))),metric("Projection orthogonale",str(list(ortho)))],
            [chart("Image, noyau et décomposition du vecteur","x","y",points,equal=True)],
            table(["Sous-espace","Base"],[["Im P","(1,0)"],["Ker P",f"({shear},1)"]]),
            ["P projette sur l'axe x parallèlement à span(shear,1). P est orthogonal exactement lorsque shear=0.",
             "Un projecteur oblique reste idempotent ; sa norme peut dépasser 1. L'orthogonalité s'ajoute à l'idempotence."],
            dict(idempotent=bool(P*P==P),orthogonal=bool(P.T==P),image=serialize_matrix(sp.Matrix([1,0])),kernel=serialize_matrix(sp.Matrix([shear,1]))),
            [matrix_block("P",P),matrix_block("I−P",Q),matrix_block("v",v),matrix_block("Pv",proj)])
    J=sp.Matrix([[l1,coupling,0],[0,l1,0],[0,0,l2]])
    change=sp.Matrix([[1,shear,0],[0,1,shear],[0,0,1]]);A=change*J*change.inv()
    minimal,items=primary_projectors(A);total=sum((item["P"] for item in items),sp.zeros(3))
    rows=[];blocks=[matrix_block("A",A),matrix_block("J (famille construite)",J),matrix_block("S (A=SJS⁻¹)",change)]
    for i,item in enumerate(items,1):
        f,g,u,v,e,P=(item[k] for k in ("f","g","u","v","e","P"))
        rows.append([str(f.as_expr()),str(g.as_expr()),f"({u.as_expr()})f + ({v.as_expr()})g = 1",str(e.as_expr())])
        blocks.append(matrix_block(f"Projecteur primaire P{i}",P,f"Im P{i}=Ker({f.as_expr()})(A)."))
    checks=all(item["P"]**2==item["P"] and A*item["P"]==item["P"]*A for item in items)
    orthogonal_components=all(items[i]["P"]*items[j]["P"]==sp.zeros(3) for i in range(len(items)) for j in range(len(items)) if i!=j)
    theta=np.linspace(0,2*np.pi,161);vectors=np.vstack([np.cos(theta),np.sin(theta),np.zeros_like(theta)])
    curves=[series("Cercle dans le plan z=0",vectors[0],vectors[1],"mint")]
    for i,item in enumerate(items):
        proj=np.array(item["P"],dtype=float)@vectors
        curves.append(series(f"P{i+1}(cercle), projection xy",proj[0],proj[1],("green","gold","rose")[i%3]))
    return output("projecteurs",parameters,
        [metric("Polynôme minimal",str(minimal.as_expr())),metric("Nombre de composantes primaires",len(items)),
         metric("ΣPᵢ=I","exact" if total==sp.eye(3) else "échec"),metric("Pᵢ²=Pᵢ, PᵢPⱼ=0","exact" if checks and orthogonal_components else "échec")],
        [chart("Image des projecteurs — vue dans le plan xy","x","y",curves,equal=True)],
        table(["fᵢ","gᵢ=m/fᵢ","Certificat de Bézout","eᵢ modulo m"],rows),
        ["Le calcul utilise les puissances présentes dans le polynôme minimal : un bloc de Jordan exige un facteur multiple.",
         "Quand lambda1=lambda2, les facteurs fusionnent : il n'existe qu'une composante primaire et son projecteur est I.",
         "PᵢPⱼ=0 exprime une décomposition algébrique ; les sous-espaces ne sont pas nécessairement orthogonaux au sens euclidien."],
        dict(minimal=str(minimal.as_expr()),sum_identity=bool(total==sp.eye(3)),idempotent=bool(checks),
             pairwise_zero=bool(orthogonal_components),projectors=[serialize_matrix(item["P"]) for item in items]),blocks)


def quadratic_congruence(S):
    """Orthogonalisation rationnelle BᵀSB=D, y compris les pivots isotropes.

    Quand toutes les diagonales restantes sont nulles, mais s_ij≠0,
    e_i+e_j fournit un pivot 2s_ij. Pas de division par un vecteur isotrope.
    """
    S=sp.Matrix(S)
    if S.rows!=S.cols or S.T!=S:raise ValueError("Matrice symétrique requise.")
    n=S.rows;B=sp.eye(n);D=S.copy();steps=[]
    def transform(T,title,text):
        nonlocal B,D
        B=B*T;D=T.T*D*T;steps.append(step(title,D,text))
    for k in range(n):
        if D[k,k]==0:
            pivot=next((i for i in range(k,n) if D[i,i]!=0),None)
            if pivot is not None and pivot!=k:
                T=sp.eye(n);T.col_swap(k,pivot)
                transform(T,f"Permuter les vecteurs {k+1} et {pivot+1}","Permutation simultanée des lignes et colonnes : congruence.")
            elif pivot is None:
                pair=next(((i,j) for i in range(k,n) for j in range(i+1,n) if D[i,j]!=0),None)
                if pair is None:break
                i,j=pair
                if i!=k:
                    T=sp.eye(n);T.col_swap(k,i);transform(T,f"Amener le vecteur {i+1} en position {k+1}","Recherche d'un couplage bilinéaire non nul.")
                T=sp.eye(n);T[j,k]=1
                transform(T,f"Remplacer e{k+1} par e{k+1}+e{j+1}","Le nouveau pivot vaut 2sᵢⱼ et n'est pas nul, malgré les deux diagonales isotropes.")
        if D[k,k]==0:raise ArithmeticError("Pivot de congruence introuvable.")
        T=sp.eye(n)
        for j in range(k+1,n):T[k,j]=-D[k,j]/D[k,k]
        if T!=sp.eye(n):transform(T,f"Orthogonaliser les vecteurs suivants au pivot {k+1}","Soustraire b(eₖ,eⱼ)/q(eₖ) fois le vecteur pivot ; les coefficients restent rationnels.")
    return B,D,steps


def quadratic_family(case,shear):
    P=sp.Matrix([[1,shear],[0,1]])
    base={"definie":sp.diag(2,1),"indefinie":sp.diag(1,-1),"degenerate":sp.diag(1,0),"isotrope":sp.Matrix([[0,1],[1,0]])}[case]
    return P.T*base*P,P,base


def quadratiques(data):
    case=choice(data,"case","indefinie",("definie","indefinie","degenerate","isotrope"))
    shear=rational(data,"shear",1,-3,3);x=rational(data,"x",1,-3,3);y=rational(data,"y",1,-3,3)
    S,P,base=quadratic_family(case,shear);B,D,steps=quadratic_congruence(S)
    diagonal=[D[i,i] for i in range(D.rows)];inertia=[sum(bool(v>0) for v in diagonal),sum(bool(v<0) for v in diagonal),sum(v==0 for v in diagonal)]
    vector=sp.Matrix([x,y]);q=(vector.T*S*vector)[0]
    coordinates=np.linspace(-2,2,101);xx,yy=np.meshgrid(coordinates,coordinates)
    z=float(S[0,0])*xx**2+2*float(S[0,1])*xx*yy+float(S[1,1])*yy**2
    eigenvalues,eigenvectors=np.linalg.eigh(np.array(S,dtype=float))
    curves=[]
    if case=="definie":
        t=np.linspace(0,2*np.pi,241)
        points=eigenvectors@np.vstack([np.cos(t)/np.sqrt(eigenvalues[0]),np.sin(t)/np.sqrt(eigenvalues[1])])
        curves.append(series("q=1 : ellipse",*points,"green"))
    elif case=="degenerate":
        positive=int(np.argmax(eigenvalues));zero=1-positive;t=np.linspace(-3,3,121)
        for sign,color in ((1,"green"),(-1,"gold")):
            points=sign*eigenvectors[:,positive,None]/math.sqrt(eigenvalues[positive])+eigenvectors[:,zero,None]*t
            curves.append(series("q=1 : droite"+str(sign),*points,color))
    else:
        positive=int(np.argmax(eigenvalues));negative=1-positive;t=np.linspace(-1.5,1.5,161)
        for sign,color in ((1,"green"),(-1,"gold")):
            points=(sign*eigenvectors[:,positive,None]*np.cosh(t)/math.sqrt(eigenvalues[positive])
                    +eigenvectors[:,negative,None]*np.sinh(t)/math.sqrt(-eigenvalues[negative]))
            curves.append(series("q=1 : branche"+str(sign),*points,color))
    curves.extend([series("Vecteur choisi",[0,float(x)],[0,float(y)],"rose"),
                   series(f"q(v)={q}",[float(x)],[float(y)],"rose","dots")])
    minors=[S[:k,:k].det() for k in range(1,S.rows+1)]
    similar=B.inv()*S*B
    return output("quadratiques",dict(case=case,shear=float(shear),x=float(x),y=float(y)),
        [metric("q(x,y)",str(q)),metric("Inertie (positive, négative, nulle)",str(tuple(inertia))),metric("Rang",S.rank()),
         metric("Congruence BᵀSB=D","exact" if B.T*S*B==D else "échec"),metric("Définie positive","oui" if all(v>0 for v in minors) else "non")],
        [chart("Valeurs de la forme q(x,y)","x","y",[],equal=True,grid=dict(x=coordinates,y=coordinates,z=z)),
         chart("Niveau q=1 et vecteur choisi","x","y",curves,equal=True)],
        table(["Mineur principal initial","Déterminant"],[[k+1,str(v)] for k,v in enumerate(minors)]),
        ["L'inertie est donnée dans l'ordre (n₊,n₋,n₀). Elle est conservée par congruence inversible (loi de Sylvester).",
         "BᵀSB diagonalise la forme bilinéaire ; B⁻¹SB représente un endomorphisme par similitude et conserve son spectre.",
         "Dans le cas isotrope, un pivot diagonal nul ne signifie pas que la forme est nulle : e₁+e₂ révèle un pivot non nul.",
         "Le critère des mineurs principaux initiaux tous strictement positifs caractérise les formes définies positives ; il ne classe pas à lui seul tous les cas indéfinis.",
         "Les contours q=1 sont tracés dans une base propre approchée ; le certificat d'inertie et l'orthogonalisation BᵀSB sont calculés exactement sur Q."],
        dict(q=str(q),inertia=inertia,rank=int(S.rank()),congruence=bool(B.T*S*B==D),minors=list(map(str,minors))),
        [matrix_block("S (q(v)=vᵀSv)",S),matrix_block("B : nouvelle base orthogonale pour la forme",B),matrix_block("D=BᵀSB",D),
         matrix_block("B⁻¹SB : similitude, pour comparaison",similar)],steps)


LABS={"anneaux":anneaux,"geometrie":geometrie,"lie":lie,"gauss":gauss,"pfaffien":pfaffien,"projecteurs":projecteurs,"quadratiques":quadratiques}
REDUCTION_LABS=("spectre","dunford","cyclique","frobenius","cayley")


def reduction_wrapper(data):
    try:from .reductions import calculate_lab
    except ImportError:from reductions import calculate_lab
    result=calculate_lab(data);theory=result["theory"]
    params=dict(famille=theory.get("family"))
    if "field" in theory:params["corps"]=theory["field"]
    for key in ("power","shear"):
        if key in theory:params[key]=theory[key]
    if "vector_mode" in theory:
        params["vecteur"]=theory["vector_mode"];params["v"]=theory["vector"]
    if theory.get("family")=="personnalisée":params["matrix"]=result["matrices"][0]["entries"]
    result["parameters"]=params
    return result


LABS.update({lab:reduction_wrapper for lab in REDUCTION_LABS})


def calculate(data):
    if not isinstance(data,dict):raise ValueError("Un objet de paramètres est requis.")
    lab=choice(data,"lab","anneaux",tuple(LABS))
    result=LABS[lab](data)
    result.setdefault("lab",lab);result.setdefault("parameters",{})
    result.setdefault("matrices",[]);result.setdefault("steps",[])
    # Dernière barrière : aucun objet SymPy, NaN ou Inf n'est exporté.
    json.dumps(result,ensure_ascii=False,allow_nan=False)
    return result
