"""Douze figures autonomes calculées par les laboratoires d'algèbre.

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
import numpy as np
import sympy as sp
try:
    from .modeles import calculate
except ImportError:
    from modeles import calculate

PALETTE = dict(green="#23745c", gold="#c79432", rose="#b66375", mint="#8dc9ac", ink="#17363d")
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
         parameters=dict(ring="mod", matrix="2 0;0 1", modulus=6, prime="3", dimension=2),
         caption="A=diag(2,1) est inversible sur Q, mais pas sur Z ni sur Z/6Z. Sur un anneau commutatif, A est inversible exactement lorsque det(A) est une unité."),
    dict(lab="geometrie", title="GL₂ · composer, orienter et mesurer l'aire",
         parameters=dict(sx=2, sy=1, shear=1, lower=1),
         caption="A=[[2,1],[0,1]], B=[[1,0],[1,1]]. Dans AB, B agit d'abord. Le déterminant det(A)=2 multiplie les aires et conserve l'orientation ; AB et BA sont différents."),
    dict(lab="lie", title="Algèbre de Lie · le crochet apparaît au deuxième ordre",
         parameters=dict(family="so", a=1, b=1, time=.5, h=.2),
         caption="Exemple so₃ : Xᵀ=−X et Yᵀ=−Y. Les identités de crochet et de Jacobi sont exactes ; les erreurs en norme de Frobenius ci-dessous proviennent d'exponentielles numériques."),
    dict(lab="gauss", title="Gauss · opérations sur les lignes et certificat exact",
         parameters=dict(matrix="1 2 1;2 4 0;1 1 1", vector="1;2;0"),
         caption="Réduction du système Ax=b sur Q. Les valeurs inscrites dans les cases sont exactes. R=E[A|b] est une équivalence par opérations sur les lignes ; une similitude aurait la forme P⁻¹AP."),
    dict(lab="spectre", title="Spectre · multiplicités, noyaux et choix du corps",
         parameters=dict(famille="symetrique", corps="R"),
         caption="A est symétrique réelle : ses valeurs propres 2 et 2±√2 sont simples. Elle est diagonalisable sur R et C, mais pas sur Q. Les positions du spectre sont approchées ; les dimensions sont exactes."),
    dict(lab="dunford", title="Dunford · le TP du recueil en calcul rationnel exact",
         parameters=dict(famille="tp", corps="C"),
         caption="Recueil p.137 : u₁=(1,2,0), u₂=(2,1,0), u₃=(1,0,1). Dans cette base, J=J₃(1). Newton dans Q[X]/((X−1)³) donne D=I₃ et N=A−I₃, avec N³=0 et N²≠0."),
    dict(lab="cyclique", title="Vecteurs cycliques · le quantificateur est « il existe »",
         parameters=dict(famille="compagnon", vecteur="cyclique"),
         caption="Compagnon de μ=(X−1)(X−2)(X−3). v=(1,0,0) est cyclique, mais un vecteur propre ne l'est pas. L'endomorphisme est cyclique parce qu'il existe un témoin, pas parce que tous les vecteurs conviennent."),
    dict(lab="frobenius", title="Frobenius · deux facteurs invariants et une base reconstruite",
         parameters=dict(famille="deux_facteurs", shear=1),
         caption="Famille de dimension 6 : f₁=X²−1 et f₂=(X²−1)(X−2)², avec f₁|f₂. P=I+surdiagonale, A=PFP⁻¹ ; les facteurs sont recalculés indépendamment par Smith de XI−A sur Q[X]."),
    dict(lab="cayley", title="Cayley–Hamilton · les traces du TP de Vandermonde",
         parameters=dict(famille="tp", power=4),
         caption="Recueil p.145 : colonnes (1,a,a²,a³), a=1,2,3,5 ; tr(A)=137 et det(A)=48. Newton et Faddeev–LeVerrier reconstruisent χ exactement, puis χ(A)=0 réduit A⁴ à trois puissances et I."),
    dict(lab="pfaffien", title="Pfaffien · trois appariements et un changement d'orientation",
         parameters=dict(size="4", a=1, b=2, shear=1, scale=-1),
         caption="Convention Pf([[0,a],[−a,0]])=a. En dimension 4, Pf(A)=a₁₂a₃₄−a₁₃a₂₄+a₁₄a₂₃. Ici Pf(A)=1, det(A)=1 ; det(P)=−1 inverse le signe du pfaffien, avec Pf(PᵀAP)=−1."),
    dict(lab="projecteurs", title="Projecteurs · Bézout et projection oblique",
         parameters=dict(mode="bezout", lambda1=1, lambda2=3, coupling=1, shear=1),
         caption="À droite : projecteurs primaires d'une matrice de polynôme minimal (X−1)²(X−3), construits par Bézout. À gauche : projection sur l'axe x parallèlement à (1,1), avec v=(1,2). Un projecteur oblique n'est pas nécessairement orthogonal."),
    dict(lab="quadratiques", title="Formes quadratiques · la congruence conserve l'inertie",
         parameters=dict(case="indefinie", shear=1, x=1, y=1),
         caption="q(x,y)=x²+2xy : forme indéfinie d'inertie (1,1,0). Les deux droites isotropes q=0 sont x=0 et x+2y=0. Le changement de base de la forme est BᵀSB, à distinguer de B⁻¹SB."),
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


def _render(config,result,axes,context):
    lab=config["lab"];left,right=axes
    state=result["theory"]
    if lab=="anneaux":
        _plot(left,result["charts"][0]);_plot(right,result["charts"][1])
        left.set_xticks(range(6));left.set_ylim(-.05,1.2)
        _context(context,"A=diag(2,1), det(A)=2.\nQ : A⁻¹=diag(1/2,1) ; Z et Z/6Z : pas d'inverse.  |GL₂(F₃)|=48.")
    elif lab=="geometrie":
        for ax,data in zip(axes,result["charts"]): _plot(ax,data)
        _context(context,"A=[[2,1],[0,1]] ; B=[[1,0],[1,1]]\nAB=[[3,1],[1,1]] ; BA=[[2,1],[2,2]] ; det(AB)=det(BA)=2.")
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
        _context(context,"rang A=3 ; Ker A={0} ; solution x₀=(−1,1,0).\nLes colonnes pivots de la matrice initiale donnent une base de Im A ; le certificat est E[A|b]=R.")
    elif lab=="spectre":
        for ax,data in zip(axes,result["charts"]): _plot(ax,data)
        left.set(xlim=(0,4),ylim=(-2,2))
        left.axhline(0,color="#9daaa3",lw=.8)
        left.legend(loc="upper left",fontsize=8.5,framealpha=.92,edgecolor="#e4e6dc")
        right.set_xticks(range(4));right.set_ylim(-.1,1.3)
        _context(context,"$\\chi_A(X)="+_formula(state["characteristic"])+"=\\mu_A(X)$\nA=[[2,1,0],[1,2,1],[0,1,2]] ; chaque espace propre est de dimension 1.")
    elif lab=="dunford":
        _plot(left,result["charts"][0]);left.set_xticks(range(4));left.set_ylim(-.1,3.4)
        _many_matrices(right,[_lookup(result,prefix) for prefix in ("A","D =","N =")],vertical=True)
        _context(context,"$\\mu_A=(X-1)^3,\\quad q=X-1,\\quad h_0=X,\\quad h_1=1.$\nA=D+N ; DN=ND ; N²≠0 et N³=0, exactement.")
    elif lab=="cyclique":
        data=copy.deepcopy(result["charts"][0])
        noncyclic=calculate(dict(lab="cyclique",famille="compagnon",vecteur="propre"))
        data["series"].insert(1,dict(label="Vecteur propre",x=list(range(4)),y=[0,1,1,1],color="rose",kind="line"))
        _plot(left,data);left.set_xticks(range(4));left.set_ylim(-.1,3.4)
        _many_matrices(right,[_lookup(result,"A"),_lookup(result,"K(v)")])
        v=", ".join(row[0] for row in noncyclic["theory"]["vector"])
        _context(context,"$\\mu_A=\\chi_A=(X-1)(X-2)(X-3).$\nVecteur propre non cyclique : ("+v+") ; dim C(A)=dim Q[A]=3.")
    elif lab=="frobenius":
        _plot(left,result["charts"][0]);left.set_xticks([1,2]);left.set_ylim(0,4.8)
        _matrix(right,state["F"],"F = diag(C(f₁), C(f₂))",fontsize=12)
        _context(context,"$f_1=X^2-1,\\quad f_2=(X^2-1)(X-2)^2,\\quad f_1\\mid f_2.$\n$\\chi_A=f_1f_2,\\quad\\mu_A=f_2,\\quad AP=PF.$")
    elif lab=="cayley":
        _plot(left,result["charts"][0]);left.set_xticks(range(7));left.set_ylim(-.1,4.5)
        _matrix(right,_lookup(result,"A")["entries"],"Vandermonde du TP",box=(.15,.52,.7,.38),fontsize=12)
        table=right.table(cellText=result["table"]["rows"],colLabels=["k","tr(Aᵏ)","cₖ Newton","cₖ Faddeev"],
                          cellLoc="center",bbox=[.02,.02,.96,.36])
        table.auto_set_font_size(False);table.set_fontsize(10)
        for (row,col),cell in table.get_celld().items():
            cell.set_edgecolor("#d8dfd4");cell.set_facecolor("#e6efe8" if row==0 else "#fcfbf7")
        _context(context,"$\\chi_A(X)="+_formula(state["characteristic"])+".$\n$A^4="+_formula(state["power_remainder"]).replace("X","A")+"I\\quad(\\chi_A(A)=0).$")
    elif lab=="pfaffien":
        _plot(left,result["charts"][0]);left.set_xticks([1,2,3]);left.axhline(0,color="#9daaa3",lw=.8)
        for i,row in enumerate(result["table"]["rows"]):
            left.text(i+1,float(row[1])+.10,row[0],ha="center",fontsize=9)
        left.set_ylim(-1.5,2.7)
        _many_matrices(right,[_lookup(result,"A"),_lookup(result,"PᵀAP")])
        _context(context,"Pf(A)=2−1+0=1 ; det(A)=Pf(A)²=1.\nPf(PᵀAP)=det(P)Pf(A)=−1 ; det(PᵀAP)=1.")
    elif lab=="projecteurs":
        oblique=calculate(dict(lab="projecteurs",mode="oblique",shear=1,x=1,y=2))
        _plot(left,oblique["charts"][0])
        projectors=[block for block in result["matrices"] if block["label"].startswith("Projecteur primaire")]
        _many_matrices(right,projectors)
        _context(context,"$\\mu_A=(X-1)^2(X-3).$\nP₁+P₂=I ; Pᵢ²=Pᵢ ; P₁P₂=P₂P₁=0 ; A Pᵢ=Pᵢ A, exactement.")
    elif lab=="quadratiques":
        grid=result["charts"][0]["grid"];z=np.asarray(grid["z"])
        norm=TwoSlopeNorm(vmin=float(z.min()),vcenter=0,vmax=float(z.max()))
        image=left.contourf(grid["x"],grid["y"],z,levels=25,cmap="RdYlGn",norm=norm)
        lines=left.contour(grid["x"],grid["y"],z,levels=[0],colors=PALETTE["ink"],linewidths=1.4)
        left.clabel(lines,fmt={0:"q=0"},fontsize=9)
        left.set(title="Lignes de niveau et directions isotropes",xlabel="x",ylabel="y",aspect="equal")
        left.figure.colorbar(image,ax=left,label="q(x,y)",fraction=.045,pad=.025)
        _many_matrices(right,[_lookup(result,"S ("),_lookup(result,"D=B")])
        _context(context,"$q(x,y)=x^2+2xy,\\quad B^T S B=\\operatorname{diag}(1,-1).$\nL'inertie (1,1,0) est conservée par congruence ; les valeurs propres ne le sont pas en général.")


def export(folder=None,preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name("illustrations")
    folder.mkdir(parents=True,exist_ok=True)
    if preview:
        preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    files=[]
    for config in CONFIGS:
        result=calculate(dict(lab=config["lab"],**config["parameters"]))
        fig=plt.figure(figsize=(13.8,7.6),layout="constrained")
        gridspec=fig.add_gridspec(2,2,height_ratios=[5,1.15])
        axes=[fig.add_subplot(gridspec[0,i]) for i in range(2)]
        context=fig.add_subplot(gridspec[1,:])
        fig.suptitle(config["title"],fontsize=16,fontweight="bold")
        fig.supxlabel(textwrap.fill(config["caption"],width=150),fontsize=9,color="#506b70")
        _render(config,result,axes,context)
        path=folder/(config["lab"]+".svg")
        fig.savefig(path,metadata={"Date":None,"Creator":"Python-maths-CPGE · Algèbre"})
        svg=path.read_text(encoding="utf-8")
        path.write_text("\n".join(line.rstrip() for line in svg.splitlines())+"\n",encoding="utf-8",newline="\n")
        if preview: fig.savefig(preview/(config["lab"]+".png"),dpi=125)
        plt.close(fig);files.append(path.name)
    return files


if __name__=="__main__":
    print(export())
