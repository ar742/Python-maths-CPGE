"""Deux applications de l'algèbre : probabilités sur un graphe et diffusion.

M est stochastique par colonnes : M[i,j]=P(j→i), p_{k+1}=M p_k.
Les invariants, les stationnaires et les cofacteurs sont rationnels exacts ;
les trajectoires et plongements spectraux sont numériques et le disent.
"""
from itertools import combinations
import math
import numpy as np
import sympy as sp
try:
    from .calculs_exacts import (parse_vector, number, rational, choice,
        metric, series, chart, table, matrix_block, serialize_matrix)
except ImportError:
    from calculs_exacts import (parse_vector, number, rational, choice,
        metric, series, chart, table, matrix_block, serialize_matrix)

REFERENCES = [
    dict(title="Aldous et Fill : chaînes réversibles et équilibre détaillé",
         url="https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch3.S1.html"),
    dict(title="MIT : Laplacien, incidence et théorème de Kirchhoff",
         url="https://ocw.mit.edu/courses/18-212-algebraic-combinatorics-spring-2019/1c947fa02a84f4538bdd3caf95e67ee5_MIT18_212S19_lec26.pdf"),
]
COLORS = ["green", "gold", "rose", "mint", "blue", "purple", "green", "gold"]


def _positions(n):
    half=n//2
    points=[]
    for group in range(2):
        for i in range(half):
            angle=2*np.pi*i/half + (-2*np.pi*(half-1)/half if group==0 else np.pi)
            points.append(((-1.7 if group==0 else 1.7)+.85*np.cos(angle), .85*np.sin(angle)))
    return points


def markov_matrix(bridge=sp.Rational(1,4), bias=sp.Rational(3,5), teleport=sp.Rational(1,20)):
    """Deux triangles orientés, pont 2↔3 et maintien de probabilité 1/4."""
    bridge,bias,teleport=map(sp.Rational,(bridge,bias,teleport))
    if not 0<=bridge<=2 or not -sp.Rational(4,5)<=bias<=sp.Rational(4,5) or not 0<=teleport<=sp.Rational(3,10):
        raise ValueError("Paramètres de Markov hors domaine.")
    W=sp.zeros(6)
    for offset in (0,3):
        for i in range(3):
            j=(i+1)%3
            W[offset+i,offset+j]=1+bias
            W[offset+j,offset+i]=1-bias
    W[2,3]=W[3,2]=bridge
    Q=sp.eye(6)/4+sp.Rational(3,4)*sp.diag(*[1/sum(W[i,:]) for i in range(6)])*W
    M=(1-teleport)*Q.T+teleport*sp.ones(6)/6
    if any(v<0 for v in M) or any(sum(M[:,j])!=1 for j in range(6)):
        raise ArithmeticError("La matrice de transition n'est pas stochastique.")
    return M,W


def stationary_components(M):
    """Dans cette famille : une classe irréductible ou les deux triangles fermés."""
    vectors=(M-sp.eye(M.rows)).nullspace()
    laws=[]
    for vector in vectors:
        total=sum(vector)
        if total==0:raise ArithmeticError("Base stationnaire impropre.")
        law=vector/total
        if any(v<0 for v in law) or M*law!=law:
            raise ArithmeticError("Stationnaire non positive ou non invariante.")
        laws.append(law)
    return laws


def markov(data):
    bridge=rational(data,"bridge",.25,0,2)
    bias=rational(data,"bias",.6,-.8,.8)
    teleport=rational(data,"teleport",.05,0,.3)
    steps=number(data,"steps",40,1,100,True)
    initial=choice(data,"initial","etat0",("etat0","gauche","uniforme","stationnaire","manuel"))
    M,W=markov_matrix(bridge,bias,teleport)
    components=stationary_components(M)
    pi=sum(components,sp.zeros(6,1))/len(components)
    if initial=="manuel":
        p0=parse_vector(data.get("p0","1;0;0;0;0;0"),6)
        if any(v<0 for v in p0) or sum(p0)!=1:
            raise ValueError("La loi initiale contient six probabilités positives ou nulles, de somme exactement 1.")
    elif initial=="stationnaire":p0=pi
    elif initial=="uniforme":p0=sp.ones(6,1)/6
    elif initial=="gauche":p0=sp.Matrix([sp.Rational(1,3)]*3+[0]*3)
    else:p0=sp.eye(6)[:,0]
    if len(components)==1:
        target=pi
    else:
        target=sum((sum(p0[i] for i in range(6) if law[i]!=0)*law for law in components),sp.zeros(6,1))
    F=M*sp.diag(*pi)
    imbalance=F-F.T
    reversible=imbalance==sp.zeros(6)
    Mf=np.array(M,dtype=float);law=np.array(p0,dtype=float).ravel()
    histories=[law.copy()]
    for _ in range(steps):
        law=Mf@law;histories.append(law.copy())
    histories=np.asarray(histories)
    target_f=np.array(target,dtype=float).ravel()
    distances=.5*np.sum(np.abs(histories-target_f),axis=1)
    eig=np.linalg.eigvals(Mf)
    principal=int(np.argmin(np.abs(eig-1)))
    subleading=np.delete(eig,principal)
    radius=min(1.,float(np.max(np.abs(subleading))))
    gap=max(0.,1-radius)
    if len(components)>1:gap=0.
    points=_positions(6)
    nodes=[dict(id=i,label=chr(65+i),x=float(x),y=float(y),value=float(histories[-1,i]),
                stationary=float(pi[i]),group=i//3) for i,(x,y) in enumerate(points)]
    edges=[]
    for source in range(6):
        for target_id in range(6):
            if W[source,target_id]!=0:
                flow=F[target_id,source]
                edges.append(dict(source=source,target=target_id,weight=float(flow),transition=float(M[target_id,source]),
                                  label=f"{float(flow):.3f}",color="rose" if imbalance[target_id,source]!=0 else "green"))
    frame_ids=np.unique(np.linspace(0,steps,min(31,steps+1),dtype=int))
    scene=dict(kind="graph",title="Lois de probabilité et flux stationnaires",directed=True,
               description="La taille et la couleur des états représentent pₖ. Les flèches portent les flux stationnaires πⱼMᵢⱼ sur les triangles et le pont ; le mélange uniforme η agit en plus à chaque pas.",
               nodes=nodes,edges=edges,frames=[dict(step=int(k),values=histories[k].tolist()) for k in frame_ids],
               valueLabel="Probabilité de l'état",stationary=[float(v) for v in pi],
               protocol="Mᵢⱼ=P(j→i), somme de chaque colonne=1, pₖ₊₁=M pₖ")
    notes=["Les vecteurs de probabilités sont des colonnes : la colonne j de M décrit la loi du prochain état à partir de j.",
           "M, la loi stationnaire et les flux sont calculés dans Q. Les courbes temporelles et les valeurs propres affichées sont numériques.",
           "Une loi stationnaire vérifie Mπ=π ; la réversibilité exige en plus Mᵢⱼπⱼ=Mⱼᵢπᵢ. Une circulation persistante peut coexister avec une loi stationnaire.",
           "Le maintien 1/4 rend les classes apériodiques. Avec un pont positif ou η>0, la chaîne est irréductible et sa loi stationnaire est unique."]
    if len(components)>1:
        notes.append("Pont nul et η=0 : les deux triangles sont fermés. π affichée est leur mélange moitié/moitié ; la limite de pₖ conserve la masse initiale de chaque triangle et n'est pas forcément π.")
    return dict(parameters=dict(bridge=float(bridge),bias=float(bias),teleport=float(teleport),steps=steps,
                                initial=initial,p0=[str(v) for v in p0]),
                metrics=[metric("Dimension",6),metric("dim Ker(M−I)",len(components)),
                         metric("Stationnaire unique","Oui" if len(components)==1 else "Non"),
                         metric("Réversible","Oui" if reversible else "Non"),
                         metric("Plus grand courant net",str(max(abs(v) for v in imbalance))),
                         metric("Écart spectral 1−ρ",gap,"Approché ; vaut 0 s'il reste une deuxième valeur propre 1."),
                         metric("Distance TV à la limite",float(distances[-1]))],
                charts=[chart("Comment la loi se redistribue","Pas k","Probabilité",
                              [series(chr(65+i),range(steps+1),histories[:,i],COLORS[i]) for i in range(6)]),
                        chart("La distribution finale et sa limite","État (A=1,…,F=6)","Probabilité",
                              [series("p après les pas choisis",range(1,7),histories[-1],"green","bars"),
                               series("Limite pour cette loi initiale",range(1,7),target_f,"rose","dots")]),
                        chart("La convergence se mesure","Pas k","Distance en variation totale",
                              [series("½ Σ |pₖ−p∞|",range(steps+1),distances)])],
                matrices=[matrix_block("M : transitions par colonnes",M),matrix_block("π : stationnaire exacte",pi),
                          matrix_block("Fᵢⱼ=Mᵢⱼπⱼ : flux stationnaires",F),matrix_block("F−Fᵀ : courants nets",imbalance)],
                steps=[],table=table(["État","p₀ exact","π exacte","p∞ exact","p final approché"],
                    [[chr(65+i),str(p0[i]),str(pi[i]),str(target[i]),f"{histories[-1,i]:.6f}"] for i in range(6)]),
                notes=notes,scenes=[scene],
                pedagogy=dict(mission="Prédire la loi à long terme et repérer une circulation qui persiste à l'équilibre.",
                    objects=[dict(symbol="Mᵢⱼ",meaning="Probabilité de passer de l'état j à l'état i"),
                             dict(symbol="π",meaning="Vecteur fixe de la matrice stochastique"),
                             dict(symbol="πⱼMᵢⱼ",meaning="Flux stationnaire allant de j vers i")],
                    reading=["Commencer avec toute la masse en A et faire avancer l'animation.",
                             "Réduire le pont, puis le couper sans mélange uniforme : les deux groupes gardent leurs masses.",
                             "Mettre bias=0 et η=0 : les flux opposés sont égaux, même si M n'est pas symétrique."],
                    proof=["La somme des colonnes vaut 1, donc la somme des coordonnées de Mp égale celle de p.",
                           "Mπ=π implique que les flux entrants et sortants s'équilibrent en chaque sommet.",
                           "L'équilibre détaillé annule chaque courant Fᵢⱼ−Fⱼᵢ ; il est plus fort que le seul équilibre des sommes."],
                    questions=["Une stationnaire est-elle nécessairement uniforme ?", "Une loi stationnaire exclut-elle une circulation ?", "Pourquoi deux valeurs propres 1 empêchent-elles une limite indépendante de p₀ ?"]),
                theory=dict(transition=serialize_matrix(M),stationary=[str(v) for v in pi],initial=[str(v) for v in p0],
                            limiting_law=[str(v) for v in target],stationary_dimension=len(components),
                            reversible=bool(reversible),flux=serialize_matrix(F),max_net_current=str(max(abs(v) for v in imbalance)),
                            spectral_gap=gap,eigenvalues=[dict(real=float(v.real),imag=float(v.imag)) for v in eig],
                            final_law=histories[-1].tolist(),total_variation=float(distances[-1]),
                            exact_stationarity=bool(M*pi==pi),references=REFERENCES))


def clique_bridge(size=8, bridge=sp.Rational(1,5)):
    if size not in (6,8):raise ValueError("Le graphe possède 6 ou 8 sommets.")
    bridge=sp.Rational(bridge)
    if not 0<=bridge<=2:raise ValueError("Poids du pont entre 0 et 2 requis.")
    half=size//2
    edges=[(i,j,sp.S.One) for offset in (0,half) for i,j in combinations(range(offset,offset+half),2)]
    if bridge>0:edges.append((half-1,half,bridge))
    B=sp.zeros(size,len(edges))
    for k,(i,j,_) in enumerate(edges):B[i,k]=1;B[j,k]=-1
    W=sp.diag(*[w for _,_,w in edges])
    L=B*W*B.T
    return L,B,W,edges


def reseaux(data):
    raw=data.get("size","8")
    if isinstance(raw,int) and not isinstance(raw,bool):raw=str(raw)
    size=int(choice(dict(size=raw),"size","8",("6","8")))
    half=size//2
    bridge=rational(data,"bridge",.2,0,2)
    time=number(data,"time",2,0,8)
    signal=choice(data,"signal","contraste",("contraste","impulsion","manuel"))
    if signal=="manuel":x0=parse_vector(data.get("values",[1]*half+[-1]*half),size)
    elif signal=="impulsion":x0=sp.eye(size)[:,0]
    else:x0=sp.Matrix([1]*half+[-1]*half)
    L,B,W,edges=clique_bridge(size,bridge)
    components=size-L.rank()
    cofactor=L[:size-1,:size-1]
    trees=cofactor.det()
    energy0=(x0.T*L*x0)[0]
    edge_energy=sum(w*(x0[i]-x0[j])**2 for i,j,w in edges)
    if L*sp.ones(size,1)!=sp.zeros(size,1) or energy0!=edge_energy:
        raise ArithmeticError("Le certificat du Laplacien ou de l'énergie échoue.")
    a=half+2*bridge
    lambda_exact=(a-sp.sqrt(a*a-8*bridge))/2
    # Forme stable quand le pont est très faible.
    lambda2=float(4*bridge/(a+sp.sqrt(a*a-8*bridge))) if bridge else 0.
    fiedler=np.array([1.]*(half-1)+[1-lambda2]+[-(1-lambda2)]+[-1.]*(half-1))
    fiedler/=np.linalg.norm(fiedler)
    Lf=np.array(L,dtype=float)
    eigenvalues,U=np.linalg.eigh(Lf)
    eigenvalues[:components]=0.
    initial_f=np.array(x0,dtype=float).ravel()
    times=np.linspace(0,8,121)
    amplitudes=U.T@initial_f
    histories=(U@(np.exp(-np.outer(eigenvalues,times))*amplitudes[:,None])).T
    final=U@(np.exp(-eigenvalues*time)*amplitudes)
    energy=np.einsum("ij,jk,ik->i",histories,Lf,histories)
    stationary=U[:,:components]@(U[:,:components].T@initial_f)
    fiedler_residual=float(np.linalg.norm(Lf@fiedler-lambda2*fiedler))
    if fiedler_residual>1e-10:raise ArithmeticError("Le vecteur de Fiedler n'est pas certifié numériquement.")
    positions=_positions(size)
    def network_nodes(values):
        return [dict(id=i,label=chr(65+i),x=float(x),y=float(y),value=float(values[i]),group=i//half)
                for i,(x,y) in enumerate(positions)]
    graph_edges=[dict(source=i,target=j,weight=float(w),label=str(w),color="gold" if i//half!=j//half else "green") for i,j,w in edges]
    frame_ids=np.arange(0,len(times),4)
    spectral_nodes=[dict(id=i,label=chr(65+i),x=float(2*fiedler[i]),y=float(2*U[i,components+1]),value=float(fiedler[i])) for i in range(size)]
    scenes=[dict(kind="graph",title="Le pont et le mode lent de Fiedler",description="Les arêtes portent les conductances. Les valeurs aux sommets sont les coordonnées du vecteur de Fiedler normalisé ; son signe sépare les deux cliques.",
                 directed=False,nodes=network_nodes(fiedler),edges=graph_edges,valueLabel="Coordonnée de Fiedler"),
            dict(kind="graph",title="Diffuser un signal : x′=−Lx",description="La diffusion homogénéise les valeurs dans chaque composante. Le pont échange de la masse entre les deux groupes ; le signal limite conserve leur moyenne commune si le réseau est connecté.",
                 directed=False,nodes=network_nodes(final),edges=graph_edges,valueLabel="Valeur du signal",
                 frames=[dict(time=float(times[k]),values=histories[k].tolist()) for k in frame_ids]),
            dict(kind="graph",title="Plongement spectral du réseau",description="Coordonnées issues de modes propres du Laplacien. Une base dans un espace propre multiple n'est pas unique ; les invariants spectraux restent les mêmes.",
                 directed=False,nodes=spectral_nodes,edges=graph_edges,valueLabel="Coordonnée de Fiedler")]
    notes=["Chaque colonne de B oriente arbitrairement une arête : +1 à une extrémité, −1 à l'autre. L=BWBᵀ est indépendant de ces orientations.",
           "xᵀLx=Σ_arêtes wᵢⱼ(xᵢ−xⱼ)². Ainsi L est positif ; son noyau est constitué des fonctions constantes sur chaque composante.",
           "Le cofacteur exact est la somme des produits des poids des arbres couvrants. Pour des poids tous égaux à 1, cette somme est leur nombre ; pour un pont de poids b, elle vaut b·s^(2s−4).",
           "Fiedler, l'exponentielle et les courbes de diffusion sont numériques ; le noyau, l'énergie initiale et le cofacteur sont exacts.",
           "La valeur de Fiedler est ici connue explicitement : [(s+2b)−√((s+2b)²−8b)]/2. Le test constant ±1/√n donne la borne λ₂≤4b/n."]
    if bridge==0:notes.append("Pont coupé : dim Ker L=2 et λ₂=0. La diffusion conserve séparément la moyenne de chaque clique ; le réseau ne devient pas globalement uniforme.")
    return dict(parameters=dict(size=str(size),bridge=float(bridge),time=time,signal=signal,values=[str(v) for v in x0]),
                metrics=[metric("Nombre de sommets",size),metric("Composantes = dim Ker L",components),
                         metric("λ₂ : connectivité algébrique",lambda2,"Valeur affichée approchée ; formule exacte disponible."),
                         metric("Poids total des arbres couvrants",str(trees)),metric("Énergie initiale x₀ᵀLx₀",str(energy0)),
                         metric("Énergie au temps choisi",float(final@Lf@final)),metric("Masse Σx conservée",str(sum(x0)))],
                charts=[chart("Spectre du Laplacien","Indice propre","Valeur propre",
                              [series("Valeurs propres approchées",range(1,size+1),eigenvalues,"green","dots")]),
                        chart("La diffusion d'un contraste","Temps t","xᵢ(t)",
                              [series(chr(65+i),times,histories[:,i],COLORS[i]) for i in range(size)]),
                        chart("L'énergie de Dirichlet diminue","Temps t","x(t)ᵀLx(t)",
                              [series("Énergie",times,energy)])],
                matrices=[matrix_block("L : Laplacien pondéré",L),matrix_block("B : incidence orientée",B),
                          matrix_block("W : conductances",W),matrix_block("Cofacteur de Kirchhoff",cofactor)],
                steps=[],table=table(["Sommet","x₀ exact","Fiedler approché","x(t) approché","Limite du signal"],
                    [[chr(65+i),str(x0[i]),f"{fiedler[i]:.6f}",f"{final[i]:.6f}",f"{stationary[i]:.6f}"] for i in range(size)]),
                notes=notes,scenes=scenes,
                pedagogy=dict(mission="Relier un pont géométrique au noyau, à la valeur propre lente et à un déterminant exact.",
                    objects=[dict(symbol="B",meaning="Matrice d'incidence : une colonne par arête orientée"),
                             dict(symbol="L",meaning="Laplacien : il compare la valeur d'un sommet à celles de ses voisins"),
                             dict(symbol="λ₂",meaning="Coût minimal d'une variation de signal orthogonale aux constantes")],
                    reading=["Le signe du vecteur de Fiedler révèle les deux groupes fortement connectés.",
                             "Couper le pont : une deuxième valeur propre devient nulle.",
                             "Lancer la diffusion : les différences se dissipent plus lentement quand le pont est faible."],
                    proof=["Développer xᵀBWBᵀx donne la somme w(xᵢ−xⱼ)².",
                           "Cette énergie s'annule exactement sur les fonctions constantes de chaque composante.",
                           "Cauchy–Binet appliqué au cofacteur sélectionne les ensembles d'arêtes qui forment un arbre ; le déterminant d'incidence carré vaut ±1.",
                           "Pour x′=−Lx, la dérivée de xᵀLx vaut −2‖Lx‖²≤0."],
                    questions=["Pourquoi le choix d'orientation de B ne change-t-il pas L ?", "Pourquoi tout arbre couvrant doit-il emprunter le pont ?", "Que devient le signal si le pont est coupé ?"]),
                theory=dict(size=size,bridge=str(bridge),laplacian=serialize_matrix(L),incidence=serialize_matrix(B),
                            components=components,trees=str(trees),tree_polynomial=f"{half**(2*half-4)} b",
                            energy_initial=str(energy0),energy_edge_sum=str(edge_energy),lambda2=lambda2,lambda2_exact=str(lambda_exact),
                            fiedler=fiedler.tolist(),fiedler_residual=fiedler_residual,eigenvalues=eigenvalues.tolist(),
                            signal_initial=[str(v) for v in x0],signal_final=final.tolist(),signal_limit=stationary.tolist(),
                            mass_initial=str(sum(x0)),mass_final=float(final.sum()),references=REFERENCES))


APPLICATION_LABS={"markov":markov,"reseaux":reseaux}


def calculate_lab(data):
    lab=data.get("lab","markov")
    if lab not in APPLICATION_LABS:raise ValueError("Application d'algèbre inconnue.")
    return APPLICATION_LABS[lab](data)
