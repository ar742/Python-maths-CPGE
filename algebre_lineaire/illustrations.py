"""Dix-neuf figures autonomes calculées par les laboratoires d'algèbre.

Matplotlib n'est requis que pour cet export. Les matrices et polynômes des
figures proviennent des certificats exacts ; les courbes l'indiquent lorsqu'elles
sont numériques. Le paramètre preview est réservé à la vérification visuelle.
"""
from pathlib import Path
import copy
import os
import tempfile
import textwrap

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir())/"python-maths-cpge-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import FancyArrowPatch
import numpy as np
import sympy as sp
try:
    from .modeles import calculate
except ImportError:
    from modeles import calculate

PALETTE = dict(green="#23745c", gold="#c79432", rose="#b66375", mint="#8dc9ac", ink="#17363d",
               blue="#487eac", purple="#8665a6")
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "text.color": PALETTE["ink"],
    "axes.labelcolor": PALETTE["ink"], "axes.titlecolor": PALETTE["ink"],
    "axes.edgecolor": "#9daaa3", "axes.facecolor": "#fcfbf7",
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#506b70", "ytick.color": "#506b70",
    "figure.facecolor": "white", "svg.fonttype": "none",
    "svg.hashsalt": "python-maths-cpge-algebre", "axes.formatter.use_mathtext": True,
})

CONFIGS = [
    dict(lab="anneaux", title="GL et anneaux · non nul ne signifie pas inversible",
         parameters=dict(ring="mod", modulus=6, prime="3", dimension=4),
         caption="Matrice entière dense 4×4, de déterminant 2 : elle est inversible sur Q, mais pas sur Z ni sur Z/6Z. La multiplication k→2k modulo 6 n'est pas une permutation."),
    dict(lab="geometrie", title="GL₃ · composer et mesurer le volume orienté", projections=["3d","3d"],
         parameters=dict(dimension="3",sx=2,sy=1,sz=1.5,shear=1,lower=1,shear_z=.5,lower_z=.5),
         caption="Images du cube unité dans R³. Dans AB, B agit d'abord. det(A)=3 multiplie les volumes et conserve l'orientation ; AB et BA ont même déterminant mais déforment différemment le cube."),
    dict(lab="lie", title="Algèbre de Lie · le crochet apparaît au deuxième ordre",
         parameters=dict(family="so", a=1, b=1, time=.5, h=.2),
         caption="Exemple so₃ : Xᵀ=−X et Yᵀ=−Y. Les identités de crochet et de Jacobi sont exactes ; les erreurs en norme de Frobenius ci-dessous proviennent d'exponentielles numériques."),
    dict(lab="gauss", title="Gauss · opérations sur les lignes et certificat exact",
         parameters=dict(matrix="1 2 -1 3;2 1 1 -1;0 1 2 1;3 3 0 2",vector="1;2;0;3"),
         caption="Quatre équations couplées de rang 3. La quatrième est la somme des deux premières : elle impose une condition sur b. Les entrées sont exactes ; E[A|b]=R est une équivalence, une similitude aurait la forme P⁻¹AP."),
    dict(lab="spectre", title="Jordan en 6D · même χ, chaînes différentes",
         parameters=dict(famille="jordan42",corps="Q"),
         caption="Deux matrices rationnelles denses 6×6 ont χ=(X−1)⁶. Les blocs 4+2 donnent μ=(X−1)⁴ ; les blocs 3+2+1 donnent μ=(X−1)³. Les incréments des noyaux retrouvent ces tailles."),
    dict(lab="dunford", title="Dunford en 6D · valeurs propres et mémoire nilpotente",
         parameters=dict(famille="dense6",corps="Q"),
         caption="Matrice rationnelle dense A=PJP⁻¹, J=diag(J₃(1),J₂(−2),3). D multiplie chaque chaîne par sa valeur propre ; N=A−D la descend. Newton polynomial sépare ces deux actions exactement."),
    dict(lab="cyclique", title="Krylov en 6D · un compagnon devient une récurrence", stack_right=True,
         parameters=dict(famille="recurrence6",vecteur="cyclique",terms=18),
         caption="Compagnon dense du polynôme p=(X−1)²(X+1)(X²−X−1)(X−2). Une base de Krylov donne une récurrence d'ordre 6. Le témoin choisi est cyclique, mais un vecteur propre n'observe qu'un mode."),
    dict(lab="frobenius", title="Frobenius en 6D · même χ, facteurs invariants différents",
         parameters=dict(famille="meme_chi_a",shear=1),
         caption="Deux matrices denses partagent χ=(X−1)⁴(X+2)². La première a deux facteurs invariants de degrés 2 et 4 ; la seconde un seul de degré 6. Elles ne sont pas semblables et seule la seconde est cyclique."),
    dict(lab="cayley", title="Cayley en 6D · traces, grandes puissances et quotient",
         parameters=dict(famille="dense6",power=12),
         caption="χ=μ=(X−1)³(X+2)²(X−3). Les traces valent 3+2(−2)ᵏ+3ᵏ ; Newton et Faddeev reconstruisent χ. Toute puissance de A se représente par seulement six coefficients, ceux du reste modulo μ."),
    dict(lab="pfaffien", title="Pfaffien en 6D · quinze appariements signés",
         parameters=dict(size="6",a=1,b=2,shear=1,scale=-1),
         caption="Chaque appariement utilise exactement une fois les six indices. Les quinze produits signés se somment pour donner Pf(A). Une congruence de déterminant −1 inverse ce signe, tandis que det(A)=Pf(A)²."),
    dict(lab="projecteurs", title="Projecteurs · Bézout et projection oblique",
         parameters=dict(mode="bezout", lambda1=1, lambda2=3, coupling=1, shear=1),
         caption="À droite : projecteurs primaires d'une matrice de polynôme minimal (X−1)²(X−3), construits par Bézout. À gauche : projection sur l'axe x parallèlement à (1,1), avec v=(1,2). Un projecteur oblique n'est pas nécessairement orthogonal."),
    dict(lab="quadratiques", title="Formes quadratiques · relief et directions isotropes", projections=["3d",None],
         parameters=dict(case="indefinie", shear=1, x=1, y=1),
         caption="q(x,y)=x²+2xy : forme indéfinie d'inertie (1,1,0). Les deux droites isotropes q=0 sont x=0 et x+2y=0. Le changement de base de la forme est BᵀSB, à distinguer de B⁻¹SB."),
    dict(lab="jacobi",title="Jacobi · trois vecteurs non nuls ferment un triangle",projections=["3d",None],
         parameters=dict(family="so",a=1,b=1,c=1),
         caption="Dans so₃, [x̂,ŷ]=(x×y)̂. Les trois doubles commutateurs se représentent par trois vecteurs qui se compensent. Les douze produits matriciels se réduisent à six paires opposées, indépendamment du dessin."),
    dict(lab="representations",title="Représentations · poids de sl₂ et polynômes homogènes",projections=[None,"polar"],
         parameters=dict(degree=4,generator="rotation",mix=-2,time=.5),
         caption="V₄ a dimension 5, de base x⁴,x³y,x²y²,xy³,y⁴. E=x∂y élève le poids et F=y∂x l'abaisse. À droite, le polynôme (x²−y²)² sur le cercle unité, avant et après la rotation exp(0,5(E−F))."),
    dict(lab="symplectique",title="Symplectique · oscillateurs couplés et énergie conservée",
         parameters=dict(modes="2",transform="cayley",omega1=1,omega2=1.5,coupling=.4,step=.15,steps=160),
         caption="Deux oscillateurs couplés, coordonnées (q₁,q₂,p₁,p₂), masses unitaires. Le schéma de Cayley conserve exactement J et l'énergie quadratique K avant arrondis ; Euler fait dériver l'énergie. Le portrait montre uniquement le premier mode."),
    dict(lab="markov",title="Markov · une loi stationnaire peut porter une circulation",stack_right=True,
         parameters=dict(bridge=.25,bias=.6,teleport=.05,steps=40,initial="etat0"),
         caption="Deux triangles orientés et un pont ; maintien 1/4 et mélange uniforme η=0,05. Mᵢⱼ=P(j→i), pₖ₊₁=Mpₖ. Les flèches portent les flux stationnaires πⱼMᵢⱼ sur les liens structuraux ; le mélange uniforme est ajouté à tous les états."),
    dict(lab="reseaux",title="Réseaux · un pont faible crée un mode lent",stack_right=True,
         parameters=dict(size="8",bridge=.2,time=2,signal="contraste"),
         caption="Deux K₄ aux arêtes internes de poids 1, liés par une conductance b=0,2. Le mode de Fiedler sépare les groupes ; λ₂≈0,0929. La diffusion x′=−Lx dissipe le contraste. Le cofacteur de Kirchhoff vaut exactement 256b=256/5."),
    dict(id="dunford_tp",lab="dunford",title="Dunford · le TP rationnel du recueil",
         parameters=dict(famille="tp",corps="C"),
         caption="Recueil p.137 : u₁=(1,2,0), u₂=(2,1,0), u₃=(1,0,1). Dans cette base, J=J₃(1). Newton dans Q[X]/((X−1)³) donne D=I₃ et N=A−I₃, avec N³=0 et N²≠0."),
    dict(id="cayley_tp",lab="cayley",title="Cayley–Hamilton · le TP de Vandermonde",
         parameters=dict(famille="tp",power=4),
         caption="Recueil p.145 : colonnes (1,a,a²,a³), a=1,2,3,5 ; tr(A)=137 et det(A)=48. Newton et Faddeev–LeVerrier reconstruisent χ exactement, puis χ(A)=0 réduit A⁴ à trois puissances et I."),
]


def _plot(ax, data):
    for s in data["series"]:
        color=PALETTE[s["color"]]
        if s["kind"]=="bars":
            ax.bar(s["x"],s["y"],width=.5,label=s["label"],color=color)
        elif s["kind"]=="dots":
            ax.scatter(s["x"],s["y"],s=32,label=s["label"],color=color,zorder=5)
        elif s["kind"]=="stems":
            ax.vlines(s["x"],0,s["y"],lw=1.5,label=s["label"],color=color)
            ax.scatter(s["x"],s["y"],s=24,color=color)
        elif s["kind"]=="step":
            ax.step(s["x"],s["y"],where="post",lw=1.9,label=s["label"],color=color)
        else:
            ax.plot(s["x"],s["y"],lw=1.1 if s["color"]=="mint" else 1.9,label=s["label"],color=color)
    ax.set(title=data["title"],xlabel=data["xlabel"],ylabel=data["ylabel"])
    ax.title.set_fontsize(11)
    if data.get("logx"): ax.set_xscale("log")
    if data.get("logy"): ax.set_yscale("log")
    if data.get("equal"): ax.set_aspect("equal",adjustable="box")
    ax.grid(alpha=.18,lw=.6)
    if data["series"]: ax.legend(loc="best",fontsize=8.5,framealpha=.92,edgecolor="#e4e6dc")


def _matrix(ax, entries, label, box=(.05,.18,.9,.66), fontsize=12):
    """Entrées exactes avec fractions mathématiques et crochets vectoriels."""
    ax.set_axis_off()
    left,bottom,width,height=box
    rows,cols=len(entries),len(entries[0])
    ax.text(left+width/2,bottom+height+.035,label,ha="center",va="bottom",fontsize=11,
            fontweight="bold",transform=ax.transAxes)
    padding=min(.06,width*.1)
    for i,row in enumerate(entries):
        for j,value in enumerate(row):
            expression=sp.sympify(value)
            ax.text(left+padding+(j+.5)*(width-2*padding)/cols,
                    bottom+(rows-i-.5)*height/rows,"$"+sp.latex(expression)+"$",
                    ha="center",va="center",fontsize=fontsize,transform=ax.transAxes)
    for x,orientation in [(left,1),(left+width,-1)]:
        ax.plot([x+orientation*.016,x,x,x+orientation*.016],
                [bottom+height,bottom+height,bottom,bottom],color=PALETTE["ink"],lw=1,
                transform=ax.transAxes,clip_on=False)


def _many_matrices(ax, blocks, vertical=False):
    ax.set_axis_off()
    count=len(blocks)
    for i,block in enumerate(blocks):
        if vertical:
            height=.70/count
            box=(.19,.05+(count-1-i)*.90/count,.62,height)
        else:
            width=.90/count
            box=(.04+i*.95/count,.27,width*.9,.48)
        _matrix(ax,block["entries"],block["label"],box=box,fontsize=11 if count<=2 else 10)


def _lookup(result, prefix):
    return next(block for block in result["matrices"] if block["label"].startswith(prefix))


def _formula(expression):
    # La chaîne vient du moteur exact, jamais directement d'une entrée personnelle.
    return sp.latex(sp.sympify(expression.replace("^","**")))


def _context(ax, text):
    ax.set_axis_off()
    ax.text(.5,.55,text,ha="center",va="center",fontsize=11,transform=ax.transAxes,
            linespacing=1.7,color=PALETTE["ink"])


def _grid(ax, data, exact_entries=None):
    grid=data["grid"];z=np.asarray(grid["z"],dtype=float)
    limit=max(float(np.max(np.abs(z))),1)
    picture=ax.pcolormesh(grid["x"],grid["y"],z,shading="nearest",cmap="RdYlGn",vmin=-limit,vmax=limit)
    ax.set(title=data["title"],xlabel=data["xlabel"],ylabel=data["ylabel"])
    ax.title.set_fontsize(11)
    if exact_entries is not None:
        for i,row in enumerate(exact_entries):
            for j,value in enumerate(row):
                ax.text(grid["x"][j],grid["y"][i],"$"+sp.latex(sp.sympify(value))+"$",
                        ha="center",va="center",fontsize=13,color=PALETTE["ink"],
                        bbox=dict(facecolor="white",alpha=.84,pad=3,edgecolor="none"))
        ax.set_xticks(grid["x"]);ax.set_yticks(grid["y"]);ax.invert_yaxis()
        ax.axvline(grid["x"][-1]-.5,color=PALETTE["ink"],lw=1.5)
    return picture


def _space(ax, scene):
    points=scene["points"]
    coordinates=np.array([[p["x"],p["y"],p["z"]] for p in points])
    for edge in scene.get("edges",[]):
        source=edge.get("from",edge.get("source"));target=edge.get("to",edge.get("target"))
        pair=coordinates[[source,target]]
        ax.plot(*pair.T,color=PALETTE.get(edge.get("color","green"),PALETTE["green"]),lw=1.5)
    ax.scatter(*coordinates.T,s=18,color=[PALETTE.get(p.get("color","green"),PALETTE["green"]) for p in points])
    span=np.maximum(np.ptp(coordinates,axis=0),1)
    ax.set_box_aspect(span)
    ax.set(title=scene["title"],xlabel=scene.get("axes",["x","y","z"])[0],
           ylabel=scene.get("axes",["x","y","z"])[1],zlabel=scene.get("axes",["x","y","z"])[2])
    ax.title.set_fontsize(11);ax.view_init(elev=23,azim=-55)
    ax.grid(alpha=.2)


def _network(ax, scene, scalar=True, labels=True):
    """Une scène sémantique, sans déduire le sens des poids du dessin."""
    nodes=scene["nodes"];positions={n["id"]:np.array([n["x"],n["y"]],float) for n in nodes}
    values=np.array([n.get("value",0) for n in nodes],float)
    directed=scene.get("directed",False)
    has_feedback=any(e.get("feedback") for e in scene.get("edges",[]))
    for edge in scene.get("edges",[]):
        source=edge.get("source",edge.get("from"));target=edge.get("target",edge.get("to"))
        a,b=positions[source],positions[target]
        color=PALETTE.get(edge.get("color","green"),PALETTE["green"])
        width=1.2 if has_feedback else .7+min(2.8,8*abs(edge.get("weight",.15)))
        rad=.20 if directed and source!=target else 0.
        if edge.get("feedback"):
            rad=-.26-.025*abs(a[0]-b[0])
        if source==target:
            ax.annotate(edge.get("label",""),xy=a,xytext=a+np.array([.3,.5]),fontsize=9,ha="center",color=color,
                        arrowprops=dict(arrowstyle="-|>",color=color,connectionstyle="arc3,rad=.55",shrinkB=17))
            continue
        arrow=FancyArrowPatch(a,b,connectionstyle=f"arc3,rad={rad}",arrowstyle="-|>" if directed or has_feedback else "-",
                              mutation_scale=13,lw=width,color=color,shrinkA=19,shrinkB=19,alpha=.83)
        ax.add_patch(arrow)
        if labels and edge.get("label"):
            delta=b-a;perp=np.array([-delta[1],delta[0]])
            point=(a+b)/2 + (-rad*(.52 if has_feedback else .72))*perp
            if not rad:point+=np.array([0,.12])
            ax.text(*point,edge["label"],fontsize=8.5,color=color,ha="center",va="center",
                    bbox=dict(facecolor="white",alpha=.88,edgecolor="none",pad=1.2))
    if scalar:
        limit=max(np.max(np.abs(values)),.05)
        norm=TwoSlopeNorm(vmin=-limit,vcenter=0,vmax=limit) if np.min(values)<0 else None
        colors=ax.scatter([n["x"] for n in nodes],[n["y"] for n in nodes],c=values,s=720,cmap="RdYlGn" if norm else "YlGn",
                          norm=norm,vmin=None if norm else 0,vmax=None if norm else limit,edgecolors=PALETTE["ink"],lw=1,zorder=4)
        ax.figure.colorbar(colors,ax=ax,label=scene.get("valueLabel","Valeur"),fraction=.038,pad=.025,shrink=.8)
    else:
        ax.scatter([n["x"] for n in nodes],[n["y"] for n in nodes],s=780,c="#eef5ec",edgecolors=PALETTE["green"],lw=1,zorder=4)
    for n in nodes:
        ax.text(n["x"],n["y"],n["label"],ha="center",va="center",fontsize=9.5,zorder=5,
                color=PALETTE["ink"],bbox=dict(facecolor="white",alpha=.8,edgecolor="none",pad=.8))
    coords=np.array(list(positions.values()));xmin,ymin=coords.min(axis=0);xmax,ymax=coords.max(axis=0)
    ax.set(xlim=(xmin-.65,xmax+.65),ylim=(ymin-(2.8 if has_feedback else .9),ymax+.7),title=scene["title"])
    ax.title.set_fontsize(11);ax.set_aspect("equal",adjustable="box");ax.set_axis_off()


def _jordan(ax, scene):
    chains=scene["chains"];colors=["green","gold","rose","blue"]
    for row,entry in enumerate(chains):
        length=entry["length"];y=-row;color=PALETTE[colors[row%4]]
        ax.text(-.68,y,"λ="+entry["lambda"],ha="right",va="center",fontsize=12,color=color)
        for j in range(length):
            ax.scatter(j,y,s=800,color="#eef5ec",edgecolors=color,lw=1.5,zorder=4)
            ax.text(j,y,"u"+str(j+1),ha="center",va="center",fontsize=12,zorder=5)
            if j:
                ax.add_patch(FancyArrowPatch((j,y),(j-1,y),arrowstyle="-|>",mutation_scale=15,color=color,lw=2,shrinkA=20,shrinkB=20))
        ax.text(-.22,y-.31,"(A−λI)u₁=0",ha="left",fontsize=9,color=color)
    ax.set(xlim=(-1.65,max(e["length"] for e in chains)-.45),ylim=(-len(chains)+.25,.7),title=scene["title"])
    ax.title.set_fontsize(11);ax.set_aspect("equal");ax.set_axis_off()


def _weights(ax, scene):
    nodes=scene["nodes"];coords={n["id"]:np.array([n["x"],n["y"]]) for n in nodes}
    for edge in scene["edges"]:
        a,b=coords[edge["from"]],coords[edge["to"]]
        color=PALETTE[edge["color"]];rad=.28
        ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f"arc3,rad={rad}",arrowstyle="-|>",
                                    mutation_scale=15,color=color,lw=2,shrinkA=25,shrinkB=25))
        offset=-.65 if edge["operator"]=="E" else .65
        ax.text((a[0]+b[0])/2,offset,edge["label"],color=color,ha="center",fontsize=10)
    for k,n in enumerate(nodes):
        ax.scatter(n["x"],0,s=1700,color="#eef5ec",edgecolors=PALETTE["green"],lw=1.5,zorder=4)
        ax.text(n["x"],0,str(n["weight"]),ha="center",va="center",fontsize=16,fontweight="bold",zorder=5)
        ax.text(n["x"],-1.13,"$x^{"+str(len(nodes)-1-k)+"}y^{"+str(k)+"}$",ha="center",fontsize=11)
    ax.set(xlim=(-len(nodes),len(nodes)),ylim=(-1.6,1.45),title=scene["title"])
    ax.title.set_fontsize(11);ax.set_axis_off()


def _render(config,result,axes,context):
    lab=config["lab"];left,right=axes[:2]
    state=result["theory"]
    if lab=="anneaux":
        scene=copy.deepcopy(result["scenes"][0]);scene["directed"]=True
        _network(left,scene,scalar=False,labels=False);_plot(right,result["charts"][0])
        right.set_xticks(range(6));right.set_ylim(-.05,1.2)
        _context(context,"det A=2 ; multiplication modulo 6 : 0 et 3 ont la même image, de même 1 et 4.\nQ : det A≠0 ; Z : det A≠±1 ; Z/6Z : pgcd(2,6)=2≠1.")
    elif lab=="geometrie":
        for ax,scene in zip(axes,result["scenes"]):_space(ax,scene)
        _context(context,"$\\det A=2\\times1\\times\\frac{3}{2}=3,\\quad\\det B=1,\\quad\\det(AB)=\\det(BA)=3.$\nVert : A ; pâle : cube initial ; or : AB ; rose : BA. Le même volume ne détermine pas la transformation.")
    elif lab=="lie":
        _plot(left,result["charts"][0])
        _many_matrices(right,[_lookup(result,prefix) for prefix in ("X","Y","[X,Y]")])
        _context(context,"exp(hX)exp(hY)exp(−hX)exp(−hY) = I + h²[X,Y] + O(h³).\n[X,Y]ᵀ=−[X,Y] ; tr([X,Y])=0 ; Jacobi=0, exactement.")
    elif lab=="gauss":
        A=np.asarray(_lookup(result,"A")["entries"],dtype=object)
        b=np.asarray(_lookup(result,"b")["entries"],dtype=object)
        augmented=np.hstack([A,b]).tolist()
        _grid(left,result["charts"][0],augmented)
        _grid(right,result["charts"][1],_lookup(result,"[A|b] réduit")["entries"])
        kernel=state["kernel"][0];solution=state["solution"]
        _context(context,"rang A=3 ; dim Ker A=1 ; x₀=("+", ".join(solution)+") ; Ker A=Vect("+", ".join(kernel)+").\nLa dernière ligne devient nulle : b₄=b₁+b₂. Les solutions sont x₀+t v ; le certificat exact est E[A|b]=R.")
    elif lab=="spectre":
        _jordan(left,result["scenes"][0])
        alternate=calculate(dict(lab="spectre",famille="jordan321",corps="Q"))
        data=copy.deepcopy(result["charts"][1]);data["series"][0]["label"]="Blocs 4+2"
        other=copy.deepcopy(alternate["charts"][1]["series"][0]);other.update(label="Blocs 3+2+1",color="rose")
        data["series"].append(other);_plot(right,data);right.set_xticks(range(7));right.set_ylim(-.15,6.5)
        _context(context,"$\\chi_A=(X-1)^6,\\quad\\mu_{4+2}=(X-1)^4,\\quad\\mu_{3+2+1}=(X-1)^3.$\nIncréments des noyaux : 2,2,1,1 pour 4+2 ; 3,2,1 pour 3+2+1. Ils comptent les chaînes de longueur ≥k.")
    elif lab=="dunford":
        if config.get("id")=="dunford_tp":
            _plot(left,result["charts"][0]);left.set_xticks(range(4));left.set_ylim(-.1,3.4)
            _many_matrices(right,[_lookup(result,prefix) for prefix in ("A","D =","N =")],vertical=True)
            _context(context,"$\\mu_A=(X-1)^3,\\quad q=X-1,\\quad h_0=X,\\quad h_1=1.$\nA=D+N ; DN=ND ; N²≠0 et N³=0, exactement.")
        else:
            _jordan(left,result["scenes"][0]);_plot(right,result["charts"][0]);right.set_xticks(range(7))
            _context(context,"$D=H\\,\\operatorname{diag}(1,1,1,-2,-2,3)H,\\quad N=A-D,\\quad H^T H=I.$\nA=D+N ; DN=ND ; N²≠0, N³=0. D multiplie par λ, N suit les flèches vers la gauche.")
    elif lab=="cyclique":
        _network(left,result["scenes"][0],scalar=False)
        _plot(right,result["charts"][1]);right.set_yscale("symlog",linthresh=10)
        data=copy.deepcopy(result["charts"][0]);data["series"].insert(1,dict(label="Un vecteur propre",x=list(range(7)),y=[0]+[1]*6,color="rose",kind="line"))
        _plot(axes[2],data);axes[2].set_xticks(range(7))
        _context(context,"$p(X)="+_formula(state["minimal"])+".$\nLa dernière coordonnée du compagnon donne y₀,…,y₅=(0,0,0,0,0,1), puis la récurrence. L'échelle verticale est symétrique logarithmique au-delà de 10.")
    elif lab=="frobenius":
        _network(left,result["scenes"][0],scalar=False)
        xpos=np.array([0,1]);right.bar(xpos-.19,[6,6],width=.35,color=PALETTE["gold"],label="deg χ")
        right.bar(xpos+.19,[4,6],width=.35,color=PALETTE["green"],label="deg μ")
        right.set(title="Même χ n'implique pas la similitude",xticks=xpos,xticklabels=["Deux facteurs\n2+4","Un facteur\n6"],ylabel="Degré",ylim=(0,7));right.legend()
        right.text(0,6.45,"Non cyclique",ha="center");right.text(1,6.45,"Cyclique",ha="center")
        _context(context,"$f_1=(X-1)^2,\\quad f_2=(X-1)^2(X+2)^2,\\quad f_1\\mid f_2.$\n$\\chi=f_1f_2=(X-1)^4(X+2)^2,\\quad\\mu=f_2;\\qquad\\mu_{\\mathrm{autre}}=\\chi.$")
    elif lab=="cayley":
        if config.get("id")=="cayley_tp":
            _plot(left,result["charts"][0]);left.set_xticks(range(7));left.set_ylim(-.1,4.5)
            _matrix(right,_lookup(result,"A")["entries"],"Vandermonde du TP",box=(.15,.52,.7,.38),fontsize=12)
            box=[.02,.02,.96,.36]
            _context(context,"$\\chi_A(X)="+_formula(state["characteristic"])+".$\n$A^4="+_formula(state["power_remainder"]).replace("X","A")+"I\\quad(\\chi_A(A)=0).$")
        else:
            _plot(left,result["charts"][1]);left.set_yscale("symlog",linthresh=10)
            right.set_axis_off();right.set_title("Les traces reconstruisent χ exactement",fontsize=11)
            box=[.02,.18,.96,.64]
            _context(context,"$\\chi_A(X)="+_formula(state["characteristic"])+",\\quad\\det A=12,\\quad\\operatorname{tr}A=2.$\n$A^{12}=r_{12}(A),\\quad\\deg r_{12}<6$ ; chaque couleur est un coefficient du reste, avec échelle symétrique logarithmique.")
        table=right.table(cellText=result["table"]["rows"],colLabels=["k","tr(Aᵏ)","cₖ Newton","cₖ Faddeev"],
                          cellLoc="center",bbox=box)
        table.auto_set_font_size(False);table.set_fontsize(10)
        for (row,col),cell in table.get_celld().items():
            cell.set_edgecolor("#d8dfd4");cell.set_facecolor("#e6efe8" if row==0 else "#fcfbf7")
    elif lab=="pfaffien":
        selected=result["scenes"][0];example=next(m for m in selected["matchings"] if sp.Rational(m["term"])!=0)
        scene=dict(kind="graph",title="Un appariement parmi les quinze",nodes=selected["nodes"],
                   edges=[dict(source=i,target=j,color="green",label=f"a{i+1}{j+1}") for i,j in example["pairs"]])
        _network(left,scene,scalar=False);_plot(right,result["charts"][0]);right.axhline(0,color="#9daaa3",lw=.8);right.set_xticks(range(1,16))
        _context(context,"Appariement dessiné : signe="+str(example["sign"])+", produit="+example["product"]+", terme="+example["term"]+".\nPf(A)="+state["pf"]+", det(A)="+state["det"]+" ; Pf(PᵀAP)="+state["pf_transformed"]+" lorsque det(P)=−1.")
    elif lab=="projecteurs":
        oblique=calculate(dict(lab="projecteurs",mode="oblique",shear=1,x=1,y=2))
        _plot(left,oblique["charts"][0])
        projectors=[block for block in result["matrices"] if block["label"].startswith("Projecteur primaire")]
        _many_matrices(right,projectors)
        _context(context,"$\\mu_A=(X-1)^2(X-3).$\nP₁+P₂=I ; Pᵢ²=Pᵢ ; P₁P₂=P₂P₁=0 ; A Pᵢ=Pᵢ A, exactement.")
    elif lab=="quadratiques":
        grid=result["charts"][0]["grid"];z=np.asarray(grid["z"])
        norm=TwoSlopeNorm(vmin=float(z.min()),vcenter=0,vmax=float(z.max()))
        xx,yy=np.meshgrid(grid["x"],grid["y"]);left.plot_surface(xx,yy,z,cmap="RdYlGn",norm=norm,alpha=.85,rstride=3,cstride=3,lw=0)
        left.set(title="Le relief z=q(x,y)",xlabel="x",ylabel="y",zlabel="q");left.view_init(elev=26,azim=-60)
        image=right.contourf(grid["x"],grid["y"],z,levels=25,cmap="RdYlGn",norm=norm)
        lines=right.contour(grid["x"],grid["y"],z,levels=[0],colors=PALETTE["ink"],linewidths=1.4)
        right.clabel(lines,fmt={0:"q=0"},fontsize=9)
        right.set(title="Directions isotropes et lignes de niveau",xlabel="x",ylabel="y",aspect="equal")
        right.figure.colorbar(image,ax=right,label="q(x,y)",fraction=.045,pad=.025)
        _context(context,"$q(x,y)=x^2+2xy,\\quad B^T S B=\\operatorname{diag}(1,-1).$\nL'inertie (1,1,0) est conservée par congruence ; les valeurs propres ne le sont pas en général.")
    elif lab=="jacobi":
        _space(left,result["scenes"][1]);_plot(right,result["charts"][0]);right.set_xticks([1,2,3,4],labels=["C₁","C₂","C₃","Somme"])
        _context(context,"$C_1=[X,[Y,Z]],\\quad C_2=[Y,[Z,X]],\\quad C_3=[Z,[X,Y]],\\quad C_1+C_2+C_3=0.$\nLes normes ne se compensent pas : le triangle additionne les vecteurs associés, pas leurs longueurs.")
    elif lab=="representations":
        _weights(left,result["scenes"][0])
        for curve in result["scenes"][1]["curves"]:
            points=np.asarray(curve["points"]);right.plot(points[:,0],points[:,1],label=curve["label"],color=PALETTE[curve["color"]],lw=2)
        right.set_title("La rotation déplace les lobes du polynôme",fontsize=11,pad=18)
        right.legend(loc="upper center",bbox_to_anchor=(.5,-.08),fontsize=9,ncol=2);right.set_ylim(0,1.1)
        _context(context,"$[H,E]=2E,\\quad[H,F]=-2F,\\quad[E,F]=H,\\quad\\dim V_4=5,\\quad\\ker\\rho=\\{0\\}.$\nLa rotation préserve la norme pondérée cᵀGc=8/3 ; l'action de −I est +I en degré pair, et son noyau de groupe est {±I}.")
    elif lab=="symplectique":
        curve=next(s for s in result["scenes"] if s["kind"]=="phase" and "Cayley" in s["title"])["curves"][0];points=np.asarray(curve["points"])
        left.plot(*points.T,color=PALETTE["green"],lw=1.7,label="Cayley : premier mode")
        left.scatter(*points[0],s=45,color=PALETTE["rose"],label="État initial",zorder=5)
        left.set(title="Échange d'énergie entre modes : portrait (q₁,p₁)",xlabel="q₁",ylabel="p₁",aspect="equal");left.legend(fontsize=9);left.grid(alpha=.2)
        _plot(right,result["charts"][0])
        _context(context,"$u'=JKu,\\quad C=(I-hJK/2)^{-1}(I+hJK/2),\\quad C^TJC=J,\\quad C^TKC=K.$\nL'énergie totale reste constante, celle d'un seul mode varie. Conserver le volume (det M=1) n'impose pas MᵀJM=J.")
    elif lab=="markov":
        _network(left,result["scenes"][0]);_plot(right,result["charts"][0]);_plot(axes[2],result["charts"][2])
        right.legend(loc="upper right",fontsize=8,ncol=3)
        _context(context,"$M\\pi=\\pi,\\quad F_{ij}=M_{ij}\\pi_j,\\quad F-F^T\\ne0.$\nLa couleur des états représente p après 40 pas ; les flèches portent F stationnaire. Biais 0,6 : état stationnaire et équilibre détaillé sont distincts.")
    elif lab=="reseaux":
        scene=copy.deepcopy(result["scenes"][0])
        for edge in scene["edges"]:
            if edge["weight"]==1:edge["label"]=""
        _network(left,scene);_plot(right,result["charts"][1]);_plot(axes[2],result["charts"][2]);right.legend(fontsize=8,ncol=4)
        _context(context,"$L=BWB^T,\\quad x^TLx=\\sum_{\\{i,j\\}}w_{ij}(x_i-x_j)^2,\\quad\\tau=256b=\\frac{256}{5}.$\n$\\lambda_2="+f"{state['lambda2']:.6f}"+"\\leq b/2=0.1.$ Couper le pont augmente dim Ker L de 1 à 2 ; le contraste cesse alors de se dissiper entre les groupes.")


def export(folder=None,preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name("illustrations")
    folder.mkdir(parents=True,exist_ok=True)
    if preview:
        preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    files=[]
    for config in CONFIGS:
        result=calculate(dict(lab=config["lab"],**config["parameters"]))
        fig=plt.figure(figsize=(13.8,7.6),layout="constrained")
        gridspec=fig.add_gridspec(3,2,height_ratios=[3,2,1.15],width_ratios=[1,1.05])
        projections=config.get("projections",[None,None])
        axes=[fig.add_subplot(gridspec[:2,0],projection=projections[0])]
        if config.get("stack_right"):
            axes += [fig.add_subplot(gridspec[0,1]),fig.add_subplot(gridspec[1,1])]
        else:axes += [fig.add_subplot(gridspec[:2,1],projection=projections[1])]
        context=fig.add_subplot(gridspec[2,:])
        fig.suptitle(config["title"],fontsize=16,fontweight="bold")
        fig.supxlabel(textwrap.fill(config["caption"],width=150),fontsize=9,color="#506b70")
        _render(config,result,axes,context)
        identifier=config.get("id",config["lab"])
        path=folder/(identifier+".svg")
        fig.savefig(path,metadata={"Date":None,"Creator":"Python-maths-CPGE · Algèbre"})
        svg=path.read_text(encoding="utf-8")
        path.write_text("\n".join(line.rstrip() for line in svg.splitlines())+"\n",encoding="utf-8",newline="\n")
        if preview: fig.savefig(preview/(identifier+".png"),dpi=125)
        plt.close(fig);files.append(path.name)
    return files


if __name__=="__main__":
    print(export())
