"""Dix-sept laboratoires d'algèbre : certificats et représentations graphiques.

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
           theory=None, matrices=None, steps=None, scenes=None, pedagogy=None):
    return dict(lab=lab, parameters=parameters, metrics=metrics,
                charts=charts or [], table=rows or table([], []), notes=notes or [],
                theory=theory or {}, matrices=matrices or [], steps=steps or [],
                scenes=scenes or [],pedagogy=pedagogy or {})


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
    A=parse_matrix(data.get("matrix","2 2 2 2;2 3 3 3;2 3 4 4;2 3 4 5"),square=True)
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
    nodes=[dict(id=str(k),label=str(k),x=math.cos(2*math.pi*k/modulus),y=math.sin(2*math.pi*k/modulus),color='green' if flags[k] else 'rose') for k in range(modulus)]
    detmod=int(det.p)*pow(int(det.q),-1,modulus)%modulus if math.gcd(int(det.q),modulus)==1 else None
    graph=[]
    if detmod is not None:
        graph=[dict(kind='graph',title=f'Multiplication par det(A) modulo {modulus}',description='La flèche k→det(A)k donne une permutation exactement lorsque le déterminant est une unité. Cette scène explore Z/mZ, même si le calcul principal est demandé sur Q ou Z.',nodes=nodes,
                    edges=[dict(**{'from':str(k),'to':str(detmod*k%modulus)},label=f'×{detmod}',color='green') for k in range(modulus)])]
    return output("anneaux",dict(ring=ring,matrix=serialize_matrix(A),modulus=modulus,prime=str(prime),dimension=n),
                  [metric("det(A)",str(det)),metric("Inversible dans l'anneau choisi","oui" if unit else "non"),
                   metric(f"|GL_{n}(F_{prime})|",str(gl_cardinality(n,prime)),"p premier ; choix successifs de colonnes indépendantes."),
                   metric(f"|GL₂(Z/{modulus}Z)|",str(gl2_mod_cardinality(modulus)))],charts,
                  table(["Anneau","Condition exacte"],values),
                  ["Un déterminant non nul n'est pas toujours une unité : diag(2,1) n'est inversible ni dans Z ni modulo 6.",
                   "Un anneau Z/mZ avec m composé n'est pas un corps. Sa cardinalité GL₂ se calcule par les puissances premières et le théorème chinois."],
                  dict(det=str(det),unit=bool(unit),inverse=serialize_matrix(inverse) if inverse is not None else None,
                       cardinal=str(gl_cardinality(n,prime)),gl2_mod=str(gl2_mod_cardinality(modulus))),blocks,scenes=graph)


def geometrie(data):
    raw=dict(data)
    if isinstance(raw.get('dimension'),int) and not isinstance(raw['dimension'],bool):raw['dimension']=str(raw['dimension'])
    dimension=int(choice(raw,'dimension','3',('2','3')))
    sx=rational(data,"sx",2,-3,3);sy=rational(data,"sy",1,-3,3)
    shear=rational(data,"shear",1,-3,3);lower=rational(data,"lower",1,-3,3)
    sz=rational(data,'sz',1.5,-3,3);shear_z=rational(data,'shear_z',.5,-3,3);lower_z=rational(data,'lower_z',.5,-3,3)
    if dimension==2:A=sp.Matrix([[sx,shear],[0,sy]]);B=sp.Matrix([[1,0],[lower,1]])
    else:
        A=sp.Matrix([[sx,shear,shear_z],[0,sy,shear_z/2],[0,0,sz]])
        B=sp.Matrix([[1,0,0],[lower,1,0],[0,lower_z,1]])
    theta=np.linspace(0,2*np.pi,241);circle=np.vstack([np.cos(theta),np.sin(theta)])
    square=np.array([[0,1,1,0,0],[0,0,1,1,0]],dtype=float)
    def transformed(M,points):
        if M.rows==3:points=np.vstack([points,np.zeros(points.shape[1])])
        return (np.array(M,dtype=float)@points)[:2]
    sets=[]
    for name,M,color in (("Cercle initial",sp.eye(dimension),"mint"),("A",A,"green"),("AB",A*B,"gold"),("BA",B*A,"rose")):
        points=transformed(M,circle);sets.append(series(name,*points,color))
    image=transformed(A,square)
    det=A.det();orientation="directe" if det>0 else "indirecte" if det<0 else "singulière"
    scenes=[]
    if dimension==3:
        from itertools import product
        vertices=list(product((0,1),repeat=3));edges=[(i,j) for i in range(8) for j in range(i+1,8) if sum(vertices[i][k]!=vertices[j][k] for k in range(3))==1]
        def cube_scene(title,transforms):
            points=[];links=[]
            for label,M,color in transforms:
                offset=len(points)
                for v in vertices:
                    w=M*sp.Matrix(v);points.append(dict(x=float(w[0]),y=float(w[1]),z=float(w[2]),label=label+str(v),color=color))
                links.extend(dict(**{'from':offset+i,'to':offset+j},color=color) for i,j in edges)
            return dict(kind='space3d',title=title,description='Chaque arête suit l’image d’un vecteur. Le cube devient un parallélépipède ; le déterminant donne son volume orienté.',axes=['x','y','z'],points=points,edges=links)
        scenes=[cube_scene('Du cube unité au parallélépipède',[('Cube',sp.eye(3),'mint'),('A',A,'green')]),
                cube_scene('Même volume, transformations AB et BA différentes',[('AB',A*B,'gold'),('BA',B*A,'rose')])]
    params={k:float(v) for k,v in dict(sx=sx,sy=sy,sz=sz,shear=shear,lower=lower,shear_z=shear_z,lower_z=lower_z).items()};params['dimension']=str(dimension)
    return output("geometrie",params,
        [metric("det(A)",str(det)),metric("Facteur de volume" if dimension==3 else "Facteur d'aire",str(abs(det))),metric("Orientation",orientation),
         metric("AB = BA","oui" if A*B==B*A else "non")],
        [chart("Composition : B agit d'abord dans AB — vue xy","x","y",sets,equal=True),
         chart("Image du carré unité","x","y",[series("Carré",*square,"mint"),series("A(carré)",*image)],equal=True)],
        table(["Objet","Interprétation"],[["det A","Volume orienté des images de e₁,e₂,e₃" if dimension==3 else "Aire orientée des images de e₁,e₂"],["AB","A après B"],["BA","B après A"]]),
        [f"GL{dimension}(R) a deux composantes : det>0 et det<0. SL{dimension}(R) est le sous-groupe det=1.",
         "Si une échelle est nulle, la transformation est singulière ; aire ou volume s’écrasent. En dimension 3, les courbes xy sont des projections et ne donnent pas à elles seules le volume."],
        dict(det=str(det),commutator=serialize_matrix(commutator(A,B))),
        [matrix_block(label,M) for label,M in (("A",A),("B",B),("AB",A*B),("BA",B*A),("[A,B]",commutator(A,B)))],scenes=scenes)


def lie_generators(family):
    try:from .structures import classical_generators
    except ImportError:from structures import classical_generators
    return classical_generators(family)


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
    family=choice(data,"family","so",("gl","sl","so","sp"))
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
    try:from .structures import jacobi_scene
    except ImportError:from structures import jacobi_scene
    scenes=[jacobi_scene(A,B,Z)]
    if family=='so':
        scenes.append(dict(kind='space3d',title='Orbite de rotation autour d’un axe oblique',description='Le vecteur exp(tX)v tourne en conservant sa longueur. La tangente en t=0 est Xv ; X est une matrice de so₃.',axes=['x','y','z'],
            points=[dict(x=float(v[0]),y=float(v[1]),z=float(v[2]),label='',color='green') for v in trajectory],
            edges=[dict(**{'from':i,'to':i+1},color='green') for i in range(len(trajectory)-1)]))
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
         dict(label=f"exp({time:g} X) — approximation numérique",entries=[[f"{v:.7g}" for v in row] for row in E],note=law)],scenes=scenes)


def gauss(data):
    A=parse_matrix(data.get("matrix","1 2 -1 3;2 1 1 -1;0 1 2 1;3 3 0 2"))
    b=parse_vector(data.get("vector","1;2;0;3"),A.rows)
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
    graph=dict(kind='graph',title='Quelles variables interviennent dans quelles équations ?',description='Chaque arête porte un coefficient de A ; les sommets de droite sont les équations avec leur second membre. Une dépendance d’équations se démontre par Gauss, pas seulement par la forme du graphe.',
        nodes=[dict(id=f'x{j}',label=f'x{j+1}',x=0.,y=float(j),color='green') for j in range(A.cols)]+[dict(id=f'e{i}',label=f'Éq.{i+1} = {b[i]}',x=2.,y=float(i),color='gold') for i in range(A.rows)],
        edges=[dict(**{'from':f'x{j}','to':f'e{i}'},label=str(A[i,j]),color='green' if A[i,j]>0 else 'rose') for i in range(A.rows) for j in range(A.cols) if A[i,j]!=0])
    return output("gauss",dict(matrix=serialize_matrix(A),vector=[str(v) for v in b]),
        [metric("Rang",rank),metric("Dimension du noyau",A.cols-rank),metric("Rang du système augmenté",len(pivots_aug)),
         metric("Compatibilité","oui" if compatible else "non"),metric("Certificat E[A|b]=R","exact" if E*augmented==R else "échec")],grids,
        table(["Colonne pivot dans A","Colonne originale conservée"],[[i+1,str(list(A[:,i]))] for i in pivots]),
        ["Les calculs s'effectuent dans Q, où tout pivot non nul est inversible. Ils ne sont pas transposables sans précaution à Z/mZ.",
         "Une ligne [0 … 0 | c] avec c≠0 démontre l'incompatibilité.",
         "Une réduction par opérations sur les lignes est une équivalence de matrices, pas une réduction d'endomorphisme par similitude."],
        dict(rank=rank,nullity=A.cols-rank,compatible=compatible,pivots=list(pivots),
             solution=[str(v) for v in particular] if compatible else None,
             kernel=[list(map(str,v)) for v in kernel],certificate=bool(E*augmented==R)),blocks,steps,scenes=[graph])


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
    A=sp.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            value=a*(j-i)+b*(i+j+1)+((i+1)*(j+1)%5-2)
            A[i,j]=value;A[j,i]=-value
    return A


def pfaffien(data):
    size_data=dict(data)
    if isinstance(size_data.get("size"),str):
        size_data["size"]=int(choice(size_data,"size","6",("4","6","8")))
    n=number(size_data,"size",6,4,8,True)
    if n not in (4,6,8):raise ValueError("size doit être 4, 6 ou 8.")
    a=rational(data,"a",1,-3,3,True);b=rational(data,"b",2,-3,3,True)
    shear=rational(data,"shear",1,-3,3,True);scale=rational(data,"scale",1,-2,2,True)
    A=pfaffian_family(n,a,b);P=sp.eye(n);P[0,0]=scale;P[0,1]=shear
    B=P.T*A*P;terms=pfaffian_terms(A);pf=pfaffian(A);pfB=pfaffian(B);odd=A[:n-1,:n-1]
    rows=[[" ".join(f"({i+1},{j+1})" for i,j in pairs),str(value)] for value,pairs in terms]
    vals=[float(value) for value,_ in terms]
    matchings=[]
    for value,pairs in terms:
        flattened=[i for pair in pairs for i in pair]
        sign=(-1)**sum(flattened[i]>flattened[j] for i in range(n) for j in range(i+1,n))
        product=sp.prod(A[i,j] for i,j in pairs)
        matchings.append(dict(pairs=[list(pair) for pair in pairs],sign=sign,product=str(product),term=str(value)))
    matching=dict(kind='matching',title=f'{len(terms)} appariements : sélectionner un terme du pfaffien',description='Chaque indice est utilisé exactement une fois. Le signe vient de la permutation des indices ; le produit vient des coefficients aᵢⱼ, avant leur somme signée.',
        nodes=[dict(id=i,label=str(i+1),x=math.cos(2*math.pi*i/n),y=math.sin(2*math.pi*i/n)) for i in range(n)],matchings=matchings,selected=0)
    scales=np.linspace(-2,2,81)
    return output("pfaffien",dict(size=n,a=int(a),b=int(b),shear=int(shear),scale=int(scale)),
        [metric("Pf(A)",str(pf)),metric("det(A)",str(A.det())),metric("Nombre d'appariements",len(terms)),
         metric("Pf(PᵀAP)",str(pfB)),metric("det(P) Pf(A)",str(P.det()*pf)),metric("Rang de A",A.rank()),metric("Rang après congruence",B.rank()),metric("Déterminant antisymétrique impair",str(odd.det()))],
        [chart("Contributions signées des appariements","appariement","terme exact",
               [series("Contributions",list(range(1,len(vals)+1)),vals,"green","bars")]),
         chart('Orientation et perte de rang quand scale traverse zéro','scale','Pf(PᵀAP)',[series('Pfaffien transformé',scales,float(pf)*scales),series('Valeur au scale choisi',[float(scale)],[float(pfB)],'rose','dots')])],
        table(["Appariement (indices à partir de 1)","Contribution signée"],rows),
        ["Convention Pf([[0,a],[-a,0]])=a ; en dimension 4 : a₁₂a₃₄−a₁₃a₂₄+a₁₄a₂₃.",
         "La loi Pf(PᵀAP)=det(P)Pf(A) vaut même pour P singulière. Ici scale=0 permet de le vérifier.",
         "Une matrice antisymétrique impaire a un déterminant nul en caractéristique différente de 2."],
        dict(pf=str(pf),det=str(A.det()),pf_transformed=str(pfB),congruence=bool(pfB==P.det()*pf),
             det_square=bool(A.det()==pf**2),odd_det=str(odd.det()),terms=len(terms)),
        [matrix_block("A",A),matrix_block("P",P),matrix_block("PᵀAP",B),matrix_block("Sous-matrice antisymétrique impaire",odd)],scenes=[matching])


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
    x=rational(data,"x",1,-3,3);y=rational(data,"y",1,-3,3);z=rational(data,'z',1,-3,3)
    parameters=dict(mode=mode,lambda1=int(l1),lambda2=int(l2),coupling=float(coupling),shear=float(shear),x=float(x),y=float(y),z=float(z))
    if mode=="oblique":
        P=sp.Matrix([[1,-shear],[0,0]]);Q=sp.eye(2)-P;v=sp.Matrix([x,y]);proj=P*v;ortho=sp.Matrix([x,0])
        ts=np.array([-3,3]);points=[series("Image : axe x",ts,np.zeros(2),"green"),series("Noyau : span(shear,1)",float(shear)*ts,ts,"gold"),
            series("Décomposition oblique",[0,float(proj[0]),float(v[0])],[0,float(proj[1]),float(v[1])],"rose"),
            series("Vecteur et projections",[float(v[0]),float(proj[0]),float(ortho[0])],[float(v[1]),float(proj[1]),float(ortho[1])],"mint","dots")]
        graph=dict(kind='graph',title='Deux chemins vers l’axe : oblique et perpendiculaire',description='La distance au point oblique n’est pas minimale en général. Le supplément impose la direction, tandis que la métrique choisit le point le plus proche.',
            nodes=[dict(id=label,label=label,x=float(w[0]),y=float(w[1]),color=color) for label,w,color in [('0',sp.zeros(2,1),'mint'),('v',v,'rose'),('Pv',proj,'green'),('P⊥v',ortho,'gold')]],
            edges=[dict(**{'from':'0','to':'v'},label='v',color='rose'),dict(**{'from':'Pv','to':'v'},label='distance oblique',color='green'),dict(**{'from':'P⊥v','to':'v'},label='distance minimale',color='gold')])
        return output("projecteurs",parameters,
            [metric("P²=P","exact"),metric("Pᵀ=P","oui" if P.T==P else "non"),metric("‖P‖₂",math.sqrt(1+float(shear)**2)),
             metric("Projection oblique",str(list(proj))),metric("Projection orthogonale",str(list(ortho)))],
            [chart("Image, noyau et décomposition du vecteur","x","y",points,equal=True)],
            table(["Sous-espace","Base"],[["Im P","(1,0)"],["Ker P",f"({shear},1)"]]),
            ["P projette sur l'axe x parallèlement à span(shear,1). P est orthogonal exactement lorsque shear=0.",
             "Un projecteur oblique reste idempotent ; sa norme peut dépasser 1. L'orthogonalité s'ajoute à l'idempotence."],
            dict(idempotent=bool(P*P==P),orthogonal=bool(P.T==P),image=serialize_matrix(sp.Matrix([1,0])),kernel=serialize_matrix(sp.Matrix([shear,1]))),
            [matrix_block("P",P),matrix_block("I−P",Q),matrix_block("v",v),matrix_block("Pv",proj)],scenes=[graph])
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
    from_vector=sp.Matrix([x,y,z]);projections=[item['P']*from_vector for item in items]
    u3=change[:,2]
    pts=[dict(x=0.,y=0.,z=0.,label='0',color='mint')]
    for w in [sp.Matrix([-2,-2,0]),sp.Matrix([2,-2,0]),sp.Matrix([2,2,0]),sp.Matrix([-2,2,0]),-2*u3,2*u3,from_vector]+projections:
        pts.append(dict(x=float(w[0]),y=float(w[1]),z=float(w[2]),label='',color='green'))
    pts[7].update(label='v',color='rose')
    for i,w in enumerate(projections):pts[8+i].update(label=f'P{i+1}v',color=('gold','green','rose')[i%3])
    graph=dict(kind='space3d',title='Décomposer un vecteur dans les composantes primaires',description='Pour deux valeurs distinctes, le plan z=0 et la droite S e₃ sont supplémentaires. En collision, une seule composante subsiste et le projecteur est I.',axes=['x','y','z'],points=pts,
        edges=[dict(**{'from':i,'to':j},color='mint') for i,j in [(1,2),(2,3),(3,4),(4,1),(5,6)]]+[dict(**{'from':0,'to':7},color='rose')]+[dict(**{'from':0,'to':8+i},color=('gold','green','rose')[i%3]) for i in range(len(projections))],faces=[[1,2,3,4]])
    return output("projecteurs",parameters,
        [metric("Polynôme minimal",str(minimal.as_expr())),metric("Nombre de composantes primaires",len(items)),
         metric("ΣPᵢ=I","exact" if total==sp.eye(3) else "échec"),metric("Pᵢ²=Pᵢ, PᵢPⱼ=0","exact" if checks and orthogonal_components else "échec")],
        [chart("Image des projecteurs — vue dans le plan xy","x","y",curves,equal=True)],
        table(["fᵢ","gᵢ=m/fᵢ","Certificat de Bézout","eᵢ modulo m"],rows),
        ["Le calcul utilise les puissances présentes dans le polynôme minimal : un bloc de Jordan exige un facteur multiple.",
         "Quand lambda1=lambda2, les facteurs fusionnent : il n'existe qu'une composante primaire et son projecteur est I.",
         "PᵢPⱼ=0 exprime une décomposition algébrique ; les sous-espaces ne sont pas nécessairement orthogonaux au sens euclidien."],
        dict(minimal=str(minimal.as_expr()),sum_identity=bool(total==sp.eye(3)),idempotent=bool(checks),
             pairwise_zero=bool(orthogonal_components),projectors=[serialize_matrix(item["P"]) for item in items]),blocks,scenes=[graph])


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
    small=np.linspace(-2,2,13);surface_points=[];surface_edges=[]
    for j,yv in enumerate(small):
        for i,xv in enumerate(small):
            height=float(S[0,0])*xv*xv+2*float(S[0,1])*xv*yv+float(S[1,1])*yv*yv
            surface_points.append(dict(x=float(xv),y=float(yv),z=float(height),label='',color='green'))
            if i:surface_edges.append(dict(**{'from':j*len(small)+i-1,'to':j*len(small)+i},color='green'))
            if j:surface_edges.append(dict(**{'from':(j-1)*len(small)+i,'to':j*len(small)+i},color='mint'))
    surface_points.append(dict(x=float(x),y=float(y),z=float(q),label=f'q(v)={q}',color='rose'))
    scene=dict(kind='space3d',title='Le graphe de q : vallée, selle ou direction plate',description='Il s’agit de la surface z=q(x,y) d’une forme sur R², et non d’une forme quadratique sur R³. Le relief relie inertie et Hessienne ; le point rose suit le vecteur choisi.',axes=['x','y','q(x,y)'],points=surface_points,edges=surface_edges)
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
         matrix_block("B⁻¹SB : similitude, pour comparaison",similar)],steps,scenes=[scene])


PEDAGOGY={
 'anneaux':dict(mission='Décider si une matrice dense possède un inverse dans l’anneau choisi et expliquer les changements de réponse.',
  objects=[dict(symbol='A',meaning='Matrice saisie, de taille d×d ; son défaut dense4 a un déterminant égal à 2.'),dict(symbol='R',meaning='Anneau Q, Z ou Z/mZ : l’inverse doit avoir ses coefficients dans R.'),dict(symbol='m',meaning='Module des congruences ; m composé peut contenir des éléments non nuls non inversibles.'),dict(symbol='p,n',meaning='p premier et dimension du comptage |GL_n(F_p)|, indépendant de la taille de A.')],
  reading=['Comparer la même matrice dans Q, Z puis modulo 6 et 5. Lire les coefficients de l’inverse, et non seulement son existence.', 'Le graphe multiplie les résidus par le déterminant : une permutation correspond à une unité ; plusieurs flèches vers le même sommet signalent une perte d’information.'],
  proof=['A adj(A)=det(A)I donne un inverse si det(A) est une unité. Réciproquement, AB=I impose det(A)det(B)=1.', 'Sur Z les seules unités sont ±1 ; modulo m, Bézout donne le critère gcd(det(A),m)=1. Aucun pivot non unité n’est divisé.'],
  questions=['Le nombre 2 est-il une unité dans Q, Z et Z/6Z ?', 'Un pivot non unité interdit-il forcément l’inversion d’une matrice modulo 6 ?', 'Pourquoi le comptage modulo p^α utilise-t-il quatre coordonnées libres pour GL₂ ?']),
 'geometrie':dict(mission='Voir comment une transformation linéaire mélange les axes, modifie le volume et dépend de l’ordre des compositions.',
  objects=[dict(symbol='A,B',meaning='Matrices agissant sur des vecteurs colonnes ; AB signifie B puis A.'),dict(symbol='sx,sy,sz',meaning='Échelles des axes de A ; elles déterminent det A.'),dict(symbol='shear,lower,shear_z,lower_z',meaning='Coefficients de cisaillement : mélanges linéaires de coordonnées.'),dict(symbol='det A',meaning='Volume orienté en dimension 3, aire orientée en dimension 2.')],
  reading=['Tourner la scène 3D et comparer les arêtes images des vecteurs de base. Le cube initial fournit une référence de volume 1.', 'Observer AB et BA : ils ont le même déterminant sans envoyer chaque vecteur au même point. Les vues xy sont des projections.'],
  proof=['La multilinéarité et l’alternance du déterminant mesurent le volume du parallélépipède formé par les colonnes de A.', 'det(AB)=det A det B donne les mêmes volumes pour AB et BA ; cette égalité scalaire n’impose pas AB=BA.'],
  questions=['Que devient le cube lorsque sz=0 ?', 'Peut-on conserver le volume tout en changeant l’orientation ?', 'Pourquoi un cisaillement peut-il modifier les angles sans modifier le déterminant ?']),
 'lie':dict(mission='Passer d’une contrainte de groupe à son espace tangent, puis observer un commutateur et Jacobi sans annulation artificielle.',
  objects=[dict(symbol='X,Y,Z',meaning='Générateurs contrôlés de l’algèbre choisie ; X=aX₀ et Y=bY₀, Z fixe.'),dict(symbol='[X,Y]=XY−YX',meaning='Crochet : mesure infinitésimale de la non-commutation.'),dict(symbol='t',meaning='Paramètre de la courbe exp(tX).'),dict(symbol='h',meaning='Petit pas employé pour comparer les quotients différentiels et le commutateur de groupe.'),dict(symbol='J',meaning='En sp₄, forme alternée [[0,I₂],[-I₂,0]], ordre q₁,q₂,p₁,p₂.')],
  reading=['Dans so₃, les axes obliques fournissent des doubles commutateurs non nuls ; lire leurs compensations dans la scène Jacobi.', 'Diminuer h, puis suivre le point de l’orbite avec t. Le résidu numérique illustre une limite ; les identités de fermeture sont vérifiées exactement.'],
  proof=['Dériver MᵀM=I donne Xᵀ+X=0. Dériver MᵀJM=J donne XᵀJ+JX=0. L’exponentielle conserve ces formes par dérivation.', 'Le développement du commutateur de groupe donne I+h²[X,Y]+O(h³). Jacobi résulte de douze produits qui se compensent en six paires.'],
  questions=['Quelle différence entre X et exp(tX) ?', 'Pourquoi tr([X,Y])=0 interdit-il [X,Y]=I en dimension finie sur R ?', 'Pourquoi trois paramètres linéaires ne décrivent-ils pas tout sp₄, qui est de dimension 10 ? Les crochets itérés peuvent-ils agrandir cet espace ?']),
 'gauss':dict(mission='Résoudre un système couplé et distinguer redondance d’équations, variables libres et incompatibilité.',
  objects=[dict(symbol='A,b,x',meaning='A est la matrice des coefficients, b le second membre, x le vecteur d’inconnues ; Ax=b.'),dict(symbol='E',meaning='Produit des opérations de lignes, inversible : R=E[A|b].'),dict(symbol='R,pivots',meaning='Forme réduite et positions des premiers coefficients non nuls.'),dict(symbol='Ker A, Im A',meaning='Solutions de Ax=0 et espace engendré par les colonnes initiales de A.')],
  reading=['Le défaut a 4 inconnues et 4 équations, mais rang 3 : la quatrième équation est la somme des deux premières.', 'Modifier seulement la quatrième composante de b permet de transformer cette redondance en contradiction. Suivre les étapes et le graphe des coefficients.'],
  proof=['Les opérations de lignes sont inversibles et conservent les solutions. Une ligne [0,…,0|c] avec c≠0 est impossible.', 'Si le système est compatible, x₀+Ker A décrit toutes les solutions. Le théorème du rang donne dim Ker A = nombre de colonnes − rang.'],
  questions=['Pourquoi une matrice carrée ne donne-t-elle pas toujours une solution unique ?', 'Pourquoi les colonnes de R ne sont-elles pas une base de Im A ?', 'Les opérations de lignes conservent-elles les valeurs propres ?']),
 'pfaffien':dict(mission='Construire un polynôme signé par appariements et comprendre ce que le déterminant carré ne dit plus.',
  objects=[dict(symbol='A=(aᵢⱼ)',meaning='Matrice antisymétrique dense, aⱼᵢ=−aᵢⱼ, taille paire 2r.'),dict(symbol='Appariement',meaning='Partition des 2r indices en r paires ; chaque indice apparaît une fois.'),dict(symbol='Pf(A)',meaning='Somme des produits de coefficients avec leurs signes de permutation.'),dict(symbol='P,scale,shear',meaning='P change les coordonnées : la première échelle fixe det P, le cisaillement conserve ce déterminant.')],
  reading=['Sélectionner plusieurs appariements : comparer leur signe, leur produit et leur contribution. Les 15 termes en dimension 6 ne sont pas tous de même signe.', 'Faire passer scale par zéro : le pfaffien change de signe et s’annule ; le rang antisymétrique baisse par un nombre pair.'],
  proof=['Les appariements donnent Pf([[0,a],[-a,0]])=a et la formule af−be+cd en dimension 4. Une réduction alternée par congruence établit det A=Pf(A)².', 'Le changement de base multiplie la forme extérieure de degré maximal par det P : Pf(PᵀAP)=det(P)Pf(A), même lorsque P est singulière par identité polynomiale.'],
  questions=['Pourquoi √det(A) perd-il le signe du pfaffien ?', 'Combien d’appariements y a-t-il en dimensions 4,6,8 ?', 'Comment cette loi prouve-t-elle det M=1 pour une transformation symplectique ?']),
 'projecteurs':dict(mission='Décomposer un vecteur selon des sous-espaces supplémentaires et séparer projection algébrique et approximation métrique.',
  objects=[dict(symbol='P²=P',meaning='Idempotence : P est l’identité sur son image et nul sur son noyau.'),dict(symbol='λ₁,λ₂,coupling',meaning='Valeurs propres et couplage de Jordan dans la famille de A.'),dict(symbol='shear,S',meaning='Inclinaison de la base : A=SJS⁻¹ ; elle peut rendre les projecteurs obliques.'),dict(symbol='fᵢ,gᵢ,eᵢ',meaning='Facteur primaire, complément du polynôme minimal et polynomial de Bézout évalué en A.'),dict(symbol='x,y,z',meaning='Coordonnées du vecteur dans la scène 3D ; le mode oblique est un exemple intrinsèquement plan.')],
  reading=['En mode Bézout, observer le plan et la droite, puis déplacer le vecteur et le cisaillement. En collision des λ, un seul projecteur primaire subsiste.', 'En mode oblique, comparer le point Pv au pied perpendiculaire et lire les distances : idempotent ne signifie pas minimisant.'],
  proof=['uᵢfᵢ+vᵢgᵢ=1 donne eᵢ=vᵢgᵢ modulo le minimal : Pᵢ=eᵢ(A), ΣPᵢ=I, Pᵢ²=Pᵢ et PᵢPⱼ=0.', 'P²=P implique V=Im P⊕Ker P. Dans une base orthonormée, Pᵀ=P ajoute l’orthogonalité, puis Pythagore prouve le minimum de distance.'],
  questions=['Pourquoi faut-il les puissances du polynôme minimal en présence de Jordan ?', 'PᵢPⱼ=0 signifie-t-il que leurs images sont perpendiculaires ?', 'Que se passe-t-il lorsque λ₁=λ₂ ?']),
 'quadratiques':dict(mission='Relier une forme bilinéaire à un relief, puis distinguer congruence, similitude, isotropie et dégénérescence.',
  objects=[dict(symbol='S,q(v)=vᵀSv',meaning='S réelle symétrique représente la forme ; x,y sont les coordonnées de v.'),dict(symbol='B,D=BᵀSB',meaning='Nouvelle base orthogonale pour la forme et coefficients diagonaux rationnels.'),dict(symbol='Inertie (n₊,n₋,n₀)',meaning='Nombres de coefficients positifs, négatifs et nuls après congruence.'),dict(symbol='shear',meaning='Cisaillement construisant S=PᵀS₀P ; il change les coordonnées sans changer l’inertie.')],
  reading=['Comparer le relief z=q(x,y), les lignes q=1 et les deux matrices BᵀSB/B⁻¹SB. Le relief représente une forme sur R², pas une forme sur R³.', 'Dans le cas isotrope, les deux premiers vecteurs de base ont q=0 ; leur somme fournit un pivot non nul. Un vecteur isotrope n’est pas forcément dans Ker S.'],
  proof=['Si q(eᵢ)=q(eⱼ)=0 mais b(eᵢ,eⱼ)≠0, q(eᵢ+eⱼ)=2b(eᵢ,eⱼ) fournit un pivot. Les soustractions de projections bilinéaires diagonalisent par congruence.', 'La loi de Sylvester conserve l’inertie sous congruence inversible. Une similitude conserve le spectre. Pour une matrice de base orthogonale euclidienne, Bᵀ=B⁻¹ : les deux calculs donnent la même matrice.'],
  questions=['Pourquoi le cône q(v)=0 n’est-il pas en général un sous-espace ?', 'Que révèle la Hessienne 2S dans le relief ?', 'Le critère des mineurs initiaux positifs peut-il être simplement rendu non strict pour tester toute semi-positivité ?'])}


LABS={"anneaux":anneaux,"geometrie":geometrie,"lie":lie,"gauss":gauss,"pfaffien":pfaffien,"projecteurs":projecteurs,"quadratiques":quadratiques}
REDUCTION_LABS=("spectre","dunford","cyclique","frobenius","cayley")


def reduction_wrapper(data):
    try:from .reductions import calculate_lab
    except ImportError:from reductions import calculate_lab
    result=calculate_lab(data);theory=result["theory"]
    params=dict(famille=theory.get("family"))
    if "field" in theory:params["corps"]=theory["field"]
    for key in ("power","shear","terms"):
        if key in theory:params[key]=theory[key]
    if "vector_mode" in theory:
        params["vecteur"]=theory["vector_mode"];params["v"]=theory["vector"]
    if theory.get("family")=="personnalisée":
        # « personnalisée » décrit le résultat, mais n'est pas un choix d'entrée.
        # _input valide d'abord la famille : conserver celle déjà validée ou son
        # défaut officiel permet de relancer l'export avec la matrice exacte.
        defaults={"spectre":"jordan42","dunford":"dense6","cyclique":"recurrence6","cayley":"dense6"}
        params["famille"]=data.get("famille",defaults[data.get("lab","spectre")])
        params["matrix"]=result["matrices"][0]["entries"]
    result["parameters"]=params
    return result


LABS.update({lab:reduction_wrapper for lab in REDUCTION_LABS})


def structures_wrapper(data):
    try:from .structures import calculate_lab
    except ImportError:from structures import calculate_lab
    return calculate_lab(data)


def applications_wrapper(data):
    try:from .applications import calculate_lab
    except ImportError:from applications import calculate_lab
    return calculate_lab(data)


LABS.update({lab:structures_wrapper for lab in ('jacobi','representations','symplectique')})
LABS.update({lab:applications_wrapper for lab in ('markov','reseaux')})


def calculate(data):
    if not isinstance(data,dict):raise ValueError("Un objet de paramètres est requis.")
    lab=choice(data,"lab","anneaux",tuple(LABS))
    result=LABS[lab](data)
    result.setdefault("lab",lab);result.setdefault("parameters",{})
    result.setdefault("matrices",[]);result.setdefault("steps",[])
    result.setdefault('scenes',[])
    if not result.get('pedagogy'):result['pedagogy']=PEDAGOGY.get(lab,{})
    # Dernière barrière : aucun objet SymPy, NaN ou Inf n'est exporté.
    json.dumps(result,ensure_ascii=False,allow_nan=False)
    return result
