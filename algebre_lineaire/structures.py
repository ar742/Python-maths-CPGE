"""Jacobi, représentations de sl₂ et dynamique symplectique.

Les identités sont rationnelles et exactes ; orbites et intégration affichée
utilisent NumPy. Le texte de l'utilisateur reste dans le parseur Fraction.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
try:
    from .calculs_exacts import (number,rational,choice,parse_vector,serialize_matrix,
        metric,series,chart,table,matrix_block,numeric_exp)
except ImportError:
    from calculs_exacts import (number,rational,choice,parse_vector,serialize_matrix,
        metric,series,chart,table,matrix_block,numeric_exp)


def out(lab,parameters,metrics,charts,rows,notes,theory,matrices,scenes,pedagogy,steps=None):
    return dict(lab=lab,parameters=parameters,metrics=metrics,charts=charts,table=rows,
                notes=notes,theory=theory,matrices=matrices,steps=steps or [],scenes=scenes,pedagogy=pedagogy)


def bracket(A,B):return A*B-B*A


def hat(v):
    x,y,z=v
    return sp.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])


def symplectic_form(modes):
    n=modes
    return sp.zeros(n).row_join(sp.eye(n)).col_join((-sp.eye(n)).row_join(sp.zeros(n)))


def classical_generators(family):
    if family=='gl':
        return sp.Matrix([[1,1],[0,0]]),sp.Matrix([[0,0],[1,0]]),sp.Matrix([[0,1],[1,0]])
    if family=='sl':
        return sp.Matrix([[1,2],[1,-1]]),sp.Matrix([[0,1],[2,0]]),sp.Matrix([[1,-1],[3,-1]])
    if family=='so':return tuple(hat(v) for v in ((1,2,-1),(-1,1,2),(2,-1,1)))
    if family=='sp':
        q=sp.Rational
        forms=[sp.Matrix([[2,1,1,q(1,2)],[1,3,q(1,2),1],[1,q(1,2),2,q(1,4)],[q(1,2),1,q(1,4),2]]),
               sp.Matrix([[3,q(-1,2),q(1,4),1],[q(-1,2),2,1,q(1,2)],[q(1,4),1,3,q(1,2)],[1,q(1,2),q(1,2),2]]),
               sp.Matrix([[2,q(1,4),q(1,2),q(-1,2)],[q(1,4),4,q(-1,4),1],[q(1,2),q(-1,4),2,1],[q(-1,2),1,1,3]])]
        J=symplectic_form(2)
        return tuple(J*K for K in forms)
    raise ValueError('Algèbre inconnue.')


def jacobi_parts(A,B,C):
    return [bracket(A,bracket(B,C)),bracket(B,bracket(C,A)),bracket(C,bracket(A,B))]


def adjoint_matrix(A):
    """Vectorisation par colonnes : vec(AX−XA)=(I⊗A−Aᵀ⊗I)vec X."""
    return sp.kronecker_product(sp.eye(A.rows),A)-sp.kronecker_product(A.T,sp.eye(A.rows))


def jacobi_scene(A,B,C):
    parts=jacobi_parts(A,B,C)
    labels=['[X,[Y,Z]]','[Y,[Z,X]]','[Z,[X,Y]]']
    expansion=[('XYZ',1),('XZY',-1),('YZX',-1),('ZYX',1),
               ('YZX',1),('YXZ',-1),('ZXY',-1),('XZY',1),
               ('ZXY',1),('ZYX',-1),('XYZ',-1),('YXZ',1)]
    return dict(kind='jacobi',title='Douze produits, six compensations',
        description='Les trois doubles commutateurs peuvent être non nuls. Chaque mot apparaît une fois avec + et une fois avec −.',
        contributions=[dict(label=label,matrix=serialize_matrix(M),norm=float(sp.sqrt(sp.trace(M.T*M))),norm_exact=str(sp.sqrt(sp.trace(M.T*M)))) for label,M in zip(labels,parts)],
        expansion=[dict(word=word,sign=sign,contribution=i//4) for i,(word,sign) in enumerate(expansion)])


def point3(v,label='',color='green'):
    return dict(x=float(v[0]),y=float(v[1]),z=float(v[2]),label=label,color=color)


def jacobi(data):
    family=choice(data,'family','so',('so','sl','sp'))
    a=rational(data,'a',1,-2,2);b=rational(data,'b',1,-2,2);c=rational(data,'c',1,-2,2)
    base=classical_generators(family);A=a*base[0];B=b*base[1];C=c*base[2]
    parts=jacobi_parts(A,B,C);total=sum(parts,sp.zeros(A.rows));adA=adjoint_matrix(A);adB=adjoint_matrix(B)
    ad_law=bracket(adA,adB)==adjoint_matrix(bracket(A,B))
    scenes=[jacobi_scene(A,B,C)]
    if family=='so':
        vectors=[sp.Matrix([M[2,1],M[0,2],M[1,0]]) for M in parts]
        vertices=[sp.zeros(3,1),vectors[0],vectors[0]+vectors[1],sum(vectors,sp.zeros(3,1))]
        scenes.append(dict(kind='space3d',title='Le triangle fermé des trois contributions vectorielles',axes=['x','y','z'],
            description='Le crochet de so₃ correspond au produit vectoriel : [x̂,ŷ]=(x×y)̂. Les vecteurs se placent bout à bout et reviennent à zéro.',
            points=[point3(v,label,('green','gold','rose','mint')[i]) for i,(v,label) in enumerate(zip(vertices,['0','C₁','C₁+C₂','0']))],
            edges=[dict(from_=i,to=i+1,color=('green','gold','rose')[i],label=f'C{i+1}') for i in range(3)]))
        # `from` est un mot réservé Python : le contrat JSON utilise ce nom.
        for edge in scenes[-1]['edges']:edge['from']=edge.pop('from_')
    norms=[float(sp.sqrt(sp.trace(M.T*M))) for M in parts]
    pedagogy=dict(mission='Expliquer pourquoi trois contributions non nulles peuvent donner une somme exactement nulle.',
        objects=[dict(symbol='X,Y,Z',meaning='Trois matrices de la même algèbre de Lie ; a,b,c les multiplient.'),
                 dict(symbol='[X,Y]',meaning='Le commutateur XY−YX, une matrice et non un nombre.'),
                 dict(symbol='ad_X',meaning='Ici, l’application linéaire T↦[X,T] agit sur tout M_n, de dimension n². On peut aussi la restreindre à T∈g pour obtenir la représentation adjointe de g.')],
        reading=['Lire séparément les trois doubles commutateurs, puis les douze mots matriciels. Les normes sont des amplitudes ; elles ne s’additionnent pas comme les matrices.',
                 'Dans so₃, le triangle représente les trois vecteurs associés. Mettre a=0 explique aussi un cas où les contributions deviennent triviales.'],
        proof=['Développer [X,[Y,Z]]=XYZ−XZY−YZX+ZYX, puis les deux permutations cycliques. Les douze termes se compensent mot à mot.',
               'Jacobi donne [X,[Y,T]]−[Y,[X,T]]=[[X,Y],T], donc [ad_X,ad_Y]=ad_[X,Y] : ad est une représentation.',
               'Sur M_n, ad_X=0 signifie que X commute avec toutes les matrices, donc X est scalaire. Si X parcourt g, le noyau est g∩{cI}. Lorsque l’action est restreinte à T∈g, son noyau est le centre Z(g)={X∈g : [X,T]=0 pour tout T∈g}.'],
        questions=['Pourquoi la norme de la somme est-elle nulle alors que la somme des normes ne l’est pas ?',
                   'La fermeture d’un crochet suffit-elle à prouver Jacobi ?',
                   'Comment le noyau change-t-il selon que T parcourt tout M_n ou seulement l’algèbre g ?'])
    return out('jacobi',dict(family=family,a=float(a),b=float(b),c=float(c)),
        [metric('Contributions non nulles',sum(M!=sp.zeros(A.rows) for M in parts)),metric('Somme de Jacobi','matrice nulle exacte' if total==sp.zeros(A.rows) else 'échec'),
         metric('Représentation ad','[ad_X,ad_Y]=ad_[X,Y], exactement' if ad_law else 'échec')],
        [chart('Amplitudes séparées et somme','contribution','norme de Frobenius',[series('Normes (elles ne se compensent pas)',[1,2,3,4],norms+[0],'green','bars')])],
        table(['Contribution','Norme exacte'],[[f'C{i+1}',str(sp.sqrt(sp.trace(M.T*M)))] for i,M in enumerate(parts)]+[['Somme','0']]),
        ['La preuve n’exige ni antisymétrie matricielle ni valeurs propres ; elle vient de l’associativité du produit matriciel.'],
        dict(jacobi=bool(total==sp.zeros(A.rows)),nonzero=sum(M!=sp.zeros(A.rows) for M in parts),ad_law=bool(ad_law),parts=[serialize_matrix(M) for M in parts]),
        [matrix_block('X',A),matrix_block('Y',B),matrix_block('Z',C)]+[matrix_block(f'C{i+1}',M) for i,M in enumerate(parts)]+[matrix_block('C₁+C₂+C₃',total)],scenes,pedagogy)


def sl2_polynomial_representation(degree):
    if isinstance(degree,bool) or not isinstance(degree,int) or not 1<=degree<=6:raise ValueError('Degré de 1 à 6 requis.')
    n=degree+1;E=sp.zeros(n);F=sp.zeros(n);H=sp.diag(*[degree-2*k for k in range(n)])
    for k in range(1,n):E[k-1,k]=k
    for k in range(n-1):F[k+1,k]=degree-k
    return E,F,H


def homogeneous_action(g,degree):
    """ρ(g)p(x,y)=p(gᵀ(x,y)) ; expansion interne, jamais de texte évalué."""
    x,y=sp.symbols('x y');g=sp.Matrix(g);columns=[]
    if g.shape!=(2,2):raise ValueError('Une matrice 2×2 est requise.')
    for k in range(degree+1):
        p=sp.Poly(sp.expand((g[0,0]*x+g[1,0]*y)**(degree-k)*(g[0,1]*x+g[1,1]*y)**k),x,y)
        columns.append(sp.Matrix([p.coeff_monomial(x**(degree-j)*y**j) for j in range(degree+1)]))
    return sp.Matrix.hstack(*columns)


def homogeneous_values(coefficients,degree,angles):
    xx=np.cos(angles);yy=np.sin(angles)
    return sum(float(coefficients[k])*xx**(degree-k)*yy**k for k in range(degree+1))


def representations(data):
    degree=number(data,'degree',4,2,6,True);generator=choice(data,'generator','rotation',('rotation','E','F','H'))
    mix=rational(data,'mix',-2,-3,3);time=rational(data,'time',.5,-1,1)
    E,F,H=sl2_polynomial_representation(degree);n=degree+1
    raw=data.get('coefficients')
    if raw is not None and raw!='':coefficients=parse_vector(raw,n)
    else:
        coefficients=sp.zeros(n,1);coefficients[0]=1;coefficients[-1]=1;coefficients[degree//2]=mix
    G=sp.diag(*[sp.Rational(1,math.comb(degree,k)) for k in range(n)])
    T={'E':E,'F':F,'H':H,'rotation':E-F}[generator]
    if generator in ('E','F'):
        S=sum((time**k*T**k/sp.factorial(k) for k in range(degree+1)),sp.zeros(n));selected=S*coefficients
    else:S=sp.Matrix(numeric_exp(time*T));selected=S*coefficients
    kernel_map=sp.Matrix.hstack(*[sp.Matrix(list(M)) for M in (E,F,H)])
    kernel_dim=3-kernel_map.rank();weights=[degree-2*k for k in range(n)]
    nodes=[dict(id=str(k),label=f'e{k}: poids {weights[k]}',x=float(weights[k]),y=0.,color='green',weight=weights[k],monomial=f'x^{degree-k} y^{k}') for k in range(n)]
    edges=[]
    for k in range(1,n):edges.append(dict(**{'from':str(k),'to':str(k-1)},label=f'E : ×{k}',color='green',operator='E',coefficient=k))
    for k in range(n-1):edges.append(dict(**{'from':str(k),'to':str(k+1)},label=f'F : ×{degree-k}',color='gold',operator='F',coefficient=degree-k))
    angles=np.linspace(0,2*np.pi,241);before=homogeneous_values(coefficients,degree,angles);after=homogeneous_values(selected,degree,angles)
    times=np.linspace(-1,1,101);orbit=np.array([numeric_exp(t*T)@np.array(coefficients,dtype=float).reshape(n) for t in times])
    x,y=sp.symbols('x y');p=sum(coefficients[k]*x**(degree-k)*y**k for k in range(n))
    weighted_before=(coefficients.T*G*coefficients)[0];weighted_after=float((selected.T*G*selected)[0])
    relations=[bracket(H,E)-2*E,bracket(H,F)+2*F,bracket(E,F)-H]
    scenes=[dict(kind='weights',title=f'Les {n} poids de V{degree}',description='E augmente le poids de 2 ; F le diminue de 2. Le coefficient de chaque flèche vient de la dérivation du monôme.',nodes=nodes,edges=edges),
            dict(kind='phase',title='Le polynôme sur le cercle unité',description='La même forme homogène est évaluée en (cos θ,sin θ), avant et après l’action choisie. Le graphe est une coupe ; le polynôme vit sur R².',xlabel='θ (rad)',ylabel='p(cos θ,sin θ)',curves=[dict(label='p initial',points=np.column_stack([angles,before]).tolist(),color='mint'),dict(label='ρ(exp tX)p',points=np.column_stack([angles,after]).tolist(),color='green')]),
            dict(kind='space3d',title='Une orbite dans l’espace des coefficients — trois coordonnées',description=f'Projection de l’orbite de dimension {n} sur (c₀,c₁,c₂), pour −1≤t≤1. Elle n’identifie pas tout l’espace V{degree}.',axes=['c₀','c₁','c₂'],
                 points=[point3(row[:3],str(round(float(t),2)) if i in (0,50,100) else '') for i,(row,t) in enumerate(zip(orbit,times))],edges=[dict(**{'from':i,'to':i+1},color='green') for i in range(100)])]
    pedagogy=dict(mission='Construire une représentation de sl₂ qui agit sur des polynômes plutôt que sur les vecteurs de R².',
        objects=[dict(symbol='m',meaning='Degré homogène ; la dimension de V_m est m+1.'),dict(symbol='e_k=x^(m−k)y^k',meaning='Base ordonnée, k=0,…,m ; les coefficients du polynôme sont les coordonnées dans cette base.'),
                 dict(symbol='E=x∂y, F=y∂x, H=x∂x−y∂y',meaning='Opérateurs différentiels linéaires préservant le degré.'),dict(symbol='ρ',meaning='Application linéaire respectant les crochets : ρ([X,Y])=[ρ(X),ρ(Y)].'),
                 dict(symbol='Ker ρ',meaning='Éléments de sl₂ agissant comme l’opérateur nul sur tous les polynômes, et non polynômes annulés par un seul E.')],
        reading=['Lire les poids sur les sommets et les coefficients sur les flèches. E e_k=k e_(k−1), F e_k=(m−k)e_(k+1), H e_k=(m−2k)e_k.',
                 'Le choix de t déplace le polynôme dans V_m. Pour E et F, l’exponentielle est une somme finie exacte ; rotation et H sont tracés numériquement.'],
        proof=['Appliquer les trois doubles compositions à chaque monôme prouve [H,E]=2E, [H,F]=−2F et [E,F]=H. Ce sont les relations des matrices de base de sl₂.',
               'Les trois matrices E,F,H sont linéairement indépendantes pour m≥1 : Ker ρ={0}. Pour le groupe SL₂, l’élément −I agit par (−1)^m : le noyau du groupe diffère de celui de l’algèbre quand m est pair.',
               'La rotation E−F préserve la forme G=diag(1/binomial(m,k)), car (E−F)ᵀG+G(E−F)=0. La norme euclidienne brute des coefficients n’a pas cette propriété.'],
        questions=['Pourquoi une représentation de dimension 5 peut-elle avoir une algèbre de départ de dimension 3 ?',
                   'Quelle différence entre Ker E et Ker ρ ?', 'Que deviennent les poids, les flèches et l’action de −I lorsque m passe de 4 à 5 ?'])
    return out('representations',dict(degree=degree,generator=generator,mix=float(mix),time=float(time),coefficients=[str(v) for v in coefficients]),
        [metric('Dimension de V_m',n),metric('Poids',str(weights)),metric('Relations de sl₂','trois identités exactes'),metric('Dimension de Ker ρ',kernel_dim),
         metric('Action de −I','+I : noyau de groupe {±I}' if degree%2==0 else '−I : noyau de groupe {I}'),
         metric('Norme pondérée au carré',str(weighted_before)),metric('Après le mouvement',weighted_after,'Conservée pour rotation, pas pour tout SL₂.')],
        [chart('Les coefficients se déplacent dans V_m','t','coefficient',[series(f'c{k}',times,orbit[:,k],('green','gold','rose','mint')[k%4]) for k in range(min(n,4))])],
        table(['k','Monôme','Poids','Coefficient initial','Coefficient final'],[[k,f'x^{degree-k} y^{k}',weights[k],str(coefficients[k]),str(selected[k]) if generator in ('E','F') else f'{float(selected[k]):.7g}'] for k in range(n)]),
        ['ρ(g)p(v)=p(gᵀv) fixe la convention d’action de groupe. Le diagramme des poids est exact ; les courbes des orbites sont des illustrations numériques.'],
        dict(degree=degree,dimension=n,relations_exact=all(M==sp.zeros(n) for M in relations),kernel_dimension=kernel_dim,weights=weights,center_sign=(-1)**degree,polynomial=str(p),coefficients=[str(v) for v in coefficients]),
        [matrix_block('ρ(E)',E),matrix_block('ρ(F)',F),matrix_block('ρ(H)',H),matrix_block('G : métrique adaptée aux rotations',G),matrix_block('ρ(exp tX)',S)],scenes,pedagogy)


def coupled_hamiltonian(modes,omegas,coupling):
    if modes not in (2,3):raise ValueError('Deux ou trois modes requis.')
    R=sp.eye(modes)
    for i in range(modes-1):R[i,i+1]=R[i+1,i]=coupling
    W=sp.diag(*omegas[:modes]);V=W*R*W;K=sp.diag(V,sp.eye(modes));J=symplectic_form(modes)
    return J,K,J*K


def cayley_step(A,h):
    I=sp.eye(A.rows)
    return (I-h*A/2).inv()*(I+h*A/2)


def symplectique(data):
    raw=dict(data)
    if isinstance(raw.get('modes'),int) and not isinstance(raw['modes'],bool):raw['modes']=str(raw['modes'])
    modes=int(choice(raw,'modes','2',('2','3')));transform=choice(data,'transform','cayley',('cayley','cisaillement','volume'))
    omegas=[rational(data,f'omega{i+1}',default,.5,3) for i,default in enumerate((1,1.5,2))]
    coupling=rational(data,'coupling',.4,-.6,.6);shear=rational(data,'shear',.7,-2,2);h=rational(data,'step',.15,.02,.5)
    count=number(data,'steps',160,20,400,True);J,K,A=coupled_hamiltonian(modes,omegas,coupling);n=2*modes
    C=cayley_step(A,h);Euler=sp.eye(n)+h*A
    B=shear*(sp.ones(modes)+sp.eye(modes));S=sp.eye(modes).row_join(B).col_join(sp.zeros(modes).row_join(sp.eye(modes)))
    volume=sp.eye(n);volume[0,0]=1+shear**2;volume[1,1]=1/(1+shear**2)
    chosen={'cayley':C,'cisaillement':S,'volume':volume}[transform];defect=chosen.T*J*chosen-J
    u0=sp.Matrix([1,sp.Rational(1,2)]+([sp.Rational(-1,3)] if modes==3 else [])+[0]*modes)
    cf=np.array(C,dtype=float);ef=np.array(Euler,dtype=float);kf=np.array(K,dtype=float)
    trajectories=[];energies=[]
    for M in (cf,ef):
        values=np.empty((count+1,n));values[0]=np.array(u0,dtype=float).reshape(n)
        for i in range(count):values[i+1]=M@values[i]
        trajectories.append(values);energies.append(.5*np.einsum('ij,ij->i',values,values@kf))
    times=float(h)*np.arange(count+1);energy0=float((u0.T*K*u0)[0]/2)
    indices=np.unique(np.rint(np.linspace(0,count,min(51,count+1))).astype(int))
    phase=[dict(kind='oscillators',title='Oscillateurs couplés : les coordonnées prennent vie',modes=modes,
        description='Les masses ont des positions de repos alignées ; qᵢ est un déplacement réduit ajouté à cette position. Les liaisons figurent le couplage bilinéaire V, pas nécessairement un ressort d’énergie (qᵢ−qⱼ)² : ici Vᵢⱼ=κωᵢωⱼ. La trajectoire provient de Cayley ; masses et unités de temps sont réduites.',
        frames=[dict(time=float(times[i]),values=trajectories[0][i,:modes].tolist(),momenta=trajectories[0][i,modes:].tolist()) for i in indices])]
    pindex=modes
    for i,(name,color) in enumerate((('Cayley : orbite bornée','green'),('Euler : énergie croissante','rose'))):
        values=trajectories[i]
        phase.append(dict(kind='phase',title=name,description='Même condition initiale et même pas ; coordonnées du premier mode. Les modes s’échangent de l’énergie, mais Cayley conserve exactement l’énergie quadratique totale avant arrondis.',xlabel='q₁',ylabel='p₁',curves=[dict(label=name,points=values[:,[0,pindex]].tolist(),color=color)]))
    angles=np.linspace(0,2*np.pi,81);plane=np.zeros((n,len(angles)));plane[0]=np.cos(angles);plane[pindex]=np.sin(angles)
    changed=np.array(chosen,dtype=float)@plane;projection=(0,pindex,1)
    points=[point3(plane[list(projection),i],color='mint') for i in range(len(angles))]+[point3(changed[list(projection),i]) for i in range(len(angles))]
    edges=[dict(**{'from':offset+i,'to':offset+i+1},color=color) for offset,color in ((0,'mint'),(len(angles),'green')) for i in range(len(angles)-1)]
    phase.append(dict(kind='space3d',title='Image d’un cercle de phase, avec mélange des modes',description='Vue (q₁,p₁,q₂) d’un sous-espace de l’espace des phases. Une déformation de la figure ne prouve pas à elle seule la symplecticité.',axes=['q₁','p₁','q₂'],points=points,edges=edges))
    frequencies=np.sqrt(np.linalg.eigvalsh(np.array(K[:modes,:modes],dtype=float)))
    pedagogy=dict(mission='Distinguer la conservation du volume de celle de la forme symplectique, puis comparer deux intégrateurs sur des oscillateurs couplés.',
        objects=[dict(symbol='u=(q₁,…,qᵣ,p₁,…,pᵣ)',meaning='Coordonnées de phase dans cet ordre ; r=2 ou 3, masses unitaires.'),dict(symbol='J=[[0,I],[-I,0]]',meaning='Matrice de la forme alternée ω(u,v)=uᵀJv.'),
                 dict(symbol='H(u)=½uᵀKu',meaning='Énergie quadratique ; K=diag(V,I), V=diag(ω)Rκdiag(ω).'),dict(symbol='A=JK',meaning='Équation de Hamilton u′=Au : q′=p, p′=−Vq.'),
                 dict(symbol='ωᵢ',meaning='Pulsations non couplées, en radians par unité de temps réduite ; une fréquence en cycles vaut ωᵢ/(2π).'),
                 dict(symbol='Rκ',meaning='Matrice de couplage relative : diagonale 1, coefficients κ entre voisins i et i+1, autres coefficients nuls.'),
                 dict(symbol='M',meaning='Transformation choisie : Cayley, cisaillement canonique ou exemple de déterminant 1 ; on teste MᵀJM=J.'),
                 dict(symbol='h, nombre de pas',meaning='Pas et durée numérique ; temps et pulsations réduits.'),dict(symbol='κ',meaning='Couplage relatif entre modes voisins ; |κ|≤0.6 assure V définie positive dans les familles proposées.')],
        reading=['Choisir « déterminant 1 » : la métrique det M vaut 1, mais MᵀJM−J peut être non nulle. Lire les couples qᵢ,pᵢ qui sont déformés.',
                 'Comparer séparément les portraits de phase et la courbe d’énergie. L’axe d’énergie est logarithmique pour ne pas masquer l’énergie constante par la dérive d’Euler.'],
        proof=['Kᵀ=K implique AᵀJ+JA=0 et AᵀK+KA=0. Par dérivation, exp(tA) conserve J et K.',
               'C=(I−hA/2)⁻¹(I+hA/2) vérifie CᵀJC=J et CᵀKC=K exactement. Euler I+hA possède au contraire un défaut h²AᵀJA.',
               'Pf(MᵀJM)=det(M)Pf(J). Si MᵀJM=J, Pf(J)≠0 impose det M=1 ; l’implication réciproque est fausse. Pf(J)=(-1)^(r(r−1)/2) pour notre ordre q puis p.'],
        questions=['Pourquoi le volume d’une région ne suffit-il pas à déterminer toutes ses aires symplectiques ?',
                   'Pourquoi l’énergie de chaque mode varie-t-elle malgré la conservation de l’énergie totale ?',
                   'Cayley conserve-t-il exactement l’énergie de tout Hamiltonien non quadratique ?'])
    params=dict(modes=str(modes),transform=transform,omega1=float(omegas[0]),omega2=float(omegas[1]),omega3=float(omegas[2]),coupling=float(coupling),shear=float(shear),step=float(h),steps=count)
    return out('symplectique',params,
        [metric('Dimension de phase',n),metric('det M',str(chosen.det())),metric('MᵀJM=J','oui, exactement' if defect==sp.zeros(n) else 'non'),
         metric('Pulsations normales (approchées)',', '.join(f'{v:.6g}' for v in frequencies),'Radians par unité de temps réduite ; diviser par 2π pour obtenir des cycles par unité de temps.'),metric('Énergie initiale',energy0),
         metric('Dérive relative Cayley',abs(energies[0][-1]/energy0-1),'Arrondis de simulation ; conservation exacte certifiée à part.'),metric('Dérive relative Euler',energies[1][-1]/energy0-1)],
        [chart('Énergie totale : invariant et dérive','t','H(u)',[series('Cayley',times,energies[0]),series('Euler',times,energies[1],'rose')],logy=True)],
        table(['Propriété','Cayley','Euler'],[['Forme symplectique','exacte',str(Euler.T*J*Euler-J)],['Énergie quadratique','exacte','croît pour ce Hamiltonien positif']]),
        ['Le modèle est un système linéaire stable d’oscillateurs couplés. La conservation exacte de K est spécifique au Cayley de ce système quadratique ; elle ne s’étend pas automatiquement aux Hamiltoniens non linéaires.',
         'Les portraits sont calculés en virgule flottante. Les cartes J et K et les certificats de Cayley sont rationnels exacts.'],
        dict(symplectic=bool(defect==sp.zeros(n)),det=str(chosen.det()),cayley_J=bool(C.T*J*C==J),cayley_K=bool(C.T*K*C==K),
             pf_J=str((-1)**(modes*(modes-1)//2)),euler_defect=serialize_matrix(Euler.T*J*Euler-J),K=serialize_matrix(K)),
        [matrix_block('J : forme symplectique',J),matrix_block('K : énergie',K),matrix_block('A=JK',A),matrix_block('M choisi',chosen),matrix_block('MᵀJM−J',defect),
         matrix_block('C : Cayley',C),matrix_block('Euler I+hA',Euler)],phase,pedagogy)


LABS={'jacobi':jacobi,'representations':representations,'symplectique':symplectique}


def calculate_lab(data):
    lab=choice(data,'lab','jacobi',tuple(LABS))
    return LABS[lab](data)
