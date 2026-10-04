"""Huit figures scientifiques autonomes. Matplotlib n'est pas requis pour l'app."""
from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR",str(Path(tempfile.gettempdir())/"python-maths-cpge-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mathematiques import calculate

PALETTE={"green":"#23745c","gold":"#c79432","rose":"#b66375","mint":"#8dc9ac","ink":"#17363d"}
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"text.color":PALETTE["ink"],"axes.labelcolor":PALETTE["ink"],"axes.spines.top":False,"axes.spines.right":False,"svg.fonttype":"none","svg.hashsalt":"python-maths-cpge-differentiel"})


def export(folder=None,preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name("illustrations")
    folder.mkdir(parents=True,exist_ok=True)
    if preview:preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    configs=[("jacobiennes","TP · Coordonnées et approximation affine",{}),
             ("elliptique","TP · Changement de variables sur une ellipse",{}),
             ("taylor","Taylor · Une selle dans l’exercice du recueil",dict(mode="cubique",x=-2,y=-2)),
             ("matrices","TP · Déterminant et inverse : différentielles",{}),
             ("optimisation","TP · Descente et Newton sur une quadratique",{}),
             ("lie","Algèbres de Lie · Rotation, tangent et crochet",{}),
             ("gaussienne","Gaussienne étendue · Géométrie et dérivées",{}),
             ("green_fubini","Fubini · Des coupures aux limites différentes",dict(mode="fubini"))]
    files=[]
    for lab,title,params in configs:
        result=calculate(dict(lab=lab,**params))
        fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout="constrained")
        fig.suptitle(title,fontweight="bold",fontsize=16)
        for ax,data in zip(axes,result["charts"]):
            seen=set()
            for s in data["series"]:
                label=s["label"] if s["label"] not in seen else "_nolegend_";seen.add(s["label"])
                if s["kind"]=="dots":ax.scatter(s["x"],s["y"],s=22,color=PALETTE[s["color"]],label=label,zorder=5)
                else:ax.plot(s["x"],s["y"],color=PALETTE[s["color"]],lw=1 if s["color"]=="mint" else 1.8,label=label)
            ax.set(title=data["title"],xlabel=data["xlabel"],ylabel=data["ylabel"])
            if data["logx"]:ax.set_xscale("log")
            if data["logy"]:ax.set_yscale("log")
            if data["equal"]:ax.set_aspect("equal",adjustable="datalim")
            ax.grid(alpha=.18);ax.legend(fontsize=8,loc="best")
        path=folder/(lab+".svg");fig.savefig(path,metadata={"Date":None,"Creator":"Python-maths-CPGE — calcul différentiel"})
        text=path.read_text(encoding="utf-8")
        path.write_text("\n".join(line.rstrip() for line in text.splitlines())+"\n",encoding="utf-8",newline="\n")
        if preview:fig.savefig(preview/(lab+".png"),dpi=125)
        plt.close(fig);files.append(path.name)
    return files


if __name__=="__main__":print(export())
