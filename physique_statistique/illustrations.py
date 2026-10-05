"""Dix figures scientifiques autonomes, produites par les modèles de l'atelier.

Matplotlib est facultatif pour l'application interactive. Le fichier et le
laboratoire sont des identifiants distincts : Bose/Fermi et chaîne/carré partagent
une même entrée de calcul, tout en produisant des illustrations différentes.
"""
from pathlib import Path
import copy
import os
import tempfile
import textwrap

os.environ.setdefault("MPLCONFIGDIR",str(Path(tempfile.gettempdir())/"python-maths-cpge-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from modeles import calculate

PALETTE={"green":"#23745c","gold":"#c79432","rose":"#b66375","mint":"#8dc9ac","ink":"#17363d"}
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":10,"text.color":PALETTE["ink"],
    "axes.labelcolor":PALETTE["ink"],"axes.titlecolor":PALETTE["ink"],
    "axes.spines.top":False,"axes.spines.right":False,"axes.edgecolor":"#9daaa3",
    "xtick.color":"#506b70","ytick.color":"#506b70","axes.facecolor":"#fcfbf7",
    "figure.facecolor":"#ffffff","svg.fonttype":"none",
    "svg.hashsalt":"python-maths-cpge-statistique",
})

CONFIGS=[
    dict(file_id="maxwell",lab="maxwell",title="Maxwell · composantes, norme et effusion",
         parameters=dict(mode="vitesses",temperature=300,molar_mass=28,log_density=25),select=[0,1],
         heading="Maxwell : une composante et une norme ne suivent pas la même loi",
         caption="T=300 K ; masse molaire 28 g/mol. La loi des vitesses dans le gaz est normalisée ; l'effusion pondère les molécules par leur vitesse.",
         alt="Gaussienne d'une composante, distribution de Maxwell et sélection des molécules effusantes"),
    dict(file_id="canonique",lab="canonique",title="Boltzmann · populations et comptage exact",
         parameters=dict(mode="deux",temperature=300,epsilon_mev=25,particles=100,fraction=.25),select=[0,1],
         heading="Deux niveaux : réponse thermique et entropie de configuration",
         caption="N=100 sites distinguables, niveaux 0 et ε=25 meV. À gauche, moyennes canoniques ; à droite, entropie microcanonique à nombre k d'excitations fixé. Stirling est une approximation du comptage exact.",
         alt="Réponse canonique de deux niveaux et comparaison entre entropie exacte et formule dominante de Stirling"),
    dict(file_id="gaz",lab="gaz",title="Gaz libre · boîte quantique et limite classique",
         parameters=dict(temperature=300,side_nm=10,mass_ratio=1,cutoff=36,log_density=23),select=[0,1],
         heading="Boîte quantique : retrouver l'équipartition et contrôler la coupure",
         caption="Une particule de masse électronique, cube de côté 10 nm à parois infinies, T=300 K. Fenêtre thermique θ=kBT/E_L≥0,25 ; la divergence U/(kBT) à T→0 n'est pas tronquée dans le modèle.",
         alt="Passage de la boîte quantique à l'équipartition et convergence de la somme de niveaux"),
    dict(file_id="oscillateur",lab="oscillateur",title="Oscillateur · point zéro et gel thermique",
         parameters=dict(temperature=300,frequency_thz=5),select=[0,1],
         heading="Oscillateur : séparer l'énergie de point zéro et la capacité",
         caption="Oscillateur harmonique de fréquence ν=5 THz : E_n=hν(n+1/2). Les formules thermiques sont des sommes infinies exactes ; le point zéro contribue à U, mais pas à C.",
         alt="Énergie quantique et classique d'un oscillateur, capacité thermique et gel des excitations"),
    dict(file_id="spins",lab="spins",title="Spins indépendants · Curie et saturation",
         parameters=dict(temperature=5,field=2,magnetic_moment=1),select=[0,1],
         heading="Paramagnétisme : la loi de Curie cesse d'être une droite globale",
         caption="Moments indépendants ±μ, μ égal à un magnéton de Bohr, T=5 K. La droite de Curie est une approximation pour |μB|≪kBT ; ce modèle n'inclut aucune interaction ferromagnétique.",
         alt="Aimantation saturante comparée à Curie, capacité et entropie de deux niveaux magnétiques"),
    dict(file_id="planck",lab="planck",title="Corps noir · Planck, Wien et rendement visible",
         parameters=dict(temperature=2500,wavelength_um=.5),select=[0,2],
         heading="Corps noir : le spectre et la part énergétique visible",
         caption="T=2500 K ; bande visible 390–780 nm. Bλ est une luminance par μm et par stéradian. Le rendement est radiométrique : il ne représente pas l'efficacité lumineuse de l'œil ni le rendement électrique.",
         alt="Spectre de Planck et approximation Rayleigh–Jeans, bande visible et fraction énergétique visible"),
    dict(file_id="occupations",lab="occupations",title="Bose · un condensat séparé des excitations",
         parameters=dict(mode="bose",temperature=1e-7,log_density=20,mass_atom_u=87),select=[0,1],
         heading="Bose–Einstein : saturation du continuum et fraction condensée",
         caption="Gaz homogène idéal 3D, une composante bosonique, masse 87 u, n=10²⁰ m⁻³, T=100 nK. Le fondamental est compté séparément ; la courbe d'excitations n'est pas renormalisée sur sa fenêtre.",
         alt="Fraction condensée de Bose et distribution des excitations à densité fixée"),
    dict(file_id="fermi",lab="occupations",title="Fermi · le bord de remplissage électronique",
         parameters=dict(mode="fermi",temperature=300,log_density=28),select=[0,1],
         heading="Fermi–Dirac : le gaz d'électrons et sa densité d'états",
         caption="Gaz idéal d'électrons 3D, deux états de spin, n=10²⁸ m⁻³, T=300 K. Le potentiel chimique est résolu à densité fixée ; une occupation par état et une distribution en énergie sont deux objets différents.",
         alt="Bord de Fermi à faible température et distribution en énergie des électrons"),
    dict(file_id="ising",lab="ising",title="Ising 2D · un carré fini face à Onsager–Yang",
         parameters=dict(mode="carre",theta=2,size=16,burnin=200,sweeps=1200,stride=5,seed=742,initial="aleatoire"),select=[0,3],
         heading="Ising carré : un réseau fini et la référence infinie",
         caption="L=16, θ=kBT/J=2, champ nul, graine 742 ; 200 balayages de chauffe, puis 1200 balayages, mesure tous les 5. Le point fini est ⟨|m|⟩ : la référence m∞ suppose L→∞ puis h→0⁺.",
         alt="Configuration de spins sur un carré fini et comparaison avec l'aimantation spontanée de Yang"),
    dict(file_id="ising_chaine",lab="ising",title="Ising 1D · parois paires et entropie exacte",
         parameters=dict(mode="chaine",theta=1.2,N=20,level=2),select=[0,1],
         heading="Ising chaîne : les parois se ferment par paires",
         caption="Chaîne périodique N=20, θ=kBT/J=1,2 : E_n/J=−N+4n et g_n=2 C(N,2n). Probabilités canoniques et entropie d'un niveau microcanonique sont calculées par le comptage exact.",
         alt="Distribution canonique des parois de domaines et entropie des niveaux de la chaîne d'Ising"),
]


def _views(config,result):
    data=[copy.deepcopy(result["charts"][j]) for j in config["select"]]
    if config["file_id"]=="oscillateur":
        original=result["charts"][0]
        energy=copy.deepcopy(original)
        energy.update(title="Point zéro et limite classique",ylabel="U / hν",series=[original["series"][0],original["series"][2]])
        capacity=copy.deepcopy(original)
        temperatures=np.asarray(original["series"][1]["x"])
        capacity.update(title="Capacité : gel des excitations",ylabel="C / kB",series=[original["series"][1],dict(label="Limite classique : C=kB",x=temperatures.tolist(),y=np.ones_like(temperatures).tolist(),color="gold",kind="line")])
        data=[energy,capacity]
    if config["file_id"]=="planck":
        state=result["theory"]
        data[1]["series"].append(dict(label="T=2500 K",x=[state["temperature"]],y=[100*state["visible_fraction"]],color="rose",kind="dots"))
    if config["file_id"]=="occupations":
        state=result["theory"]
        data[0]["series"].append(dict(label="T choisi",x=[state["temperature_ratio"]],y=[state["condensate_fraction"]],color="rose",kind="dots"))
    return data


def _draw_axis(fig,ax,data):
    grid=data.get("grid")
    if grid is not None:
        cmap=ListedColormap(["#f1eee1",PALETTE["green"]],name="spins_ising")
        image=ax.pcolormesh(grid["x"],grid["y"],grid["z"],shading="nearest",cmap=cmap,
                            vmin=grid.get("vmin",-1),vmax=grid.get("vmax",1),rasterized=False)
        colorbar=fig.colorbar(image,ax=ax,ticks=[-1,1],fraction=.045,pad=.025)
        colorbar.set_label("Spin sᵢ (sans dimension)")
        colorbar.ax.set_yticklabels(["−1","+1"])
    seen=set()
    for s in data["series"]:
        label=s["label"] if s["label"] not in seen else "_nolegend_"
        seen.add(s["label"]);color=PALETTE[s["color"]]
        if s["kind"]=="dots":ax.scatter(s["x"],s["y"],s=32,color=color,label=label,zorder=5)
        elif s["kind"]=="bars":ax.bar(s["x"],s["y"],width=.5,color=color,label=label)
        elif s["kind"]=="stems":
            ax.vlines(s["x"],0,s["y"],color=color,lw=1.5,label=label);ax.scatter(s["x"],s["y"],s=20,color=color)
        elif s["kind"]=="step":ax.step(s["x"],s["y"],where="post",color=color,lw=1.8,label=label)
        else:ax.plot(s["x"],s["y"],color=color,lw=1 if s["color"]=="mint" else 1.9,label=label)
    ax.set(title=data["title"],xlabel=data["xlabel"],ylabel=data["ylabel"])
    ax.title.set_fontsize(11)
    if data["logx"]:ax.set_xscale("log")
    if data["logy"]:ax.set_yscale("log")
    if data["equal"]:ax.set_aspect("equal",adjustable="box")
    ax.grid(alpha=.18,linewidth=.6)
    if data["series"]:ax.legend(fontsize=8.5,loc="best",framealpha=.92,edgecolor="#e4e6dc")


def _details(config,result,axes):
    if config["file_id"]=="gaz":
        axes[0].set(xlim=(.25,200),ylim=(0,13))
    elif config["file_id"]=="oscillateur":
        axes[1].set_ylim(0,1.08)
    elif config["file_id"]=="planck":
        axes[0].axvspan(.39,.78,color=PALETTE["mint"],alpha=.25,zorder=0)
        peak=result["theory"]["peak_wavelength_m"]*1e6
        axes[0].axvline(peak,color=PALETTE["rose"],ls=":",lw=1.3)
        axes[0].text(.98,.97,f"λmax={peak:.3f} μm",ha="right",va="top",transform=axes[0].transAxes,color=PALETTE["rose"])
        fraction=100*result["theory"]["visible_fraction"]
        axes[1].text(.98,.05,f"À 2500 K : {fraction:.3f} %",ha="right",va="bottom",transform=axes[1].transAxes,color=PALETTE["rose"])
    elif config["file_id"]=="occupations":
        state=result["theory"]
        axes[0].set_ylim(-.03,1.06)
        axes[0].text(.98,.52,f"Tc={state['critical_temperature']*1e9:.1f} nK\nN₀/N={state['condensate_fraction']:.3f}",ha="right",transform=axes[0].transAxes,color=PALETTE["rose"])
    elif config["file_id"]=="fermi":
        state=result["theory"]
        axes[0].set_ylim(-.03,1.07)
        axes[0].text(.98,.85,f"T/TF={state['temperature_ratio']:.4f}\nμ/EF={state['mu_ef']:.5f}",ha="right",transform=axes[0].transAxes,color=PALETTE["rose"])
    elif config["file_id"]=="ising":
        state=result["theory"]
        axes[1].set_ylim(-.03,1.08)
        axes[1].text(.98,.52,f"⟨|m|⟩ fini={state['mean_absolute_magnetization']:.3f}\n⟨m⟩ sur la trace={state['mean_magnetization']:.3f}",ha="right",transform=axes[1].transAxes,color=PALETTE["rose"])


def _gallery(folder):
    parts=["# Dix illustrations scientifiques — physique statistique", "",
           "Ces figures autonomes accompagnent le [parcours](../PARCOURS.md) et le [cours](../COURS.md). Elles sont produites par Matplotlib à partir des modèles Python de l'atelier ; les unités, les paramètres et les limites des comparaisons sont indiqués sous les graphiques.", ""]
    for config in CONFIGS:
        parts.extend([f"## {config['heading']}","",f"![{config['alt']}]({config['file_id']}.svg)","",config["caption"],""])
    parts.extend(["Les deux illustrations Ising distinguent le comptage exact de la chaîne finie, une simulation du carré fini et les résultats exacts d'Onsager–Yang pour le réseau infini. Les statistiques Bose et Fermi emploient leurs masses et dégénérescences propres ; un gaz bosonique atomique n'est pas un gaz électronique.","",
                  "Pour régénérer les SVG depuis le dossier `physique_statistique` :", "", "```sh",
                  "python -m pip install -r requirements-illustrations.txt", "python physique_statistique.py --export-illustrations", "```", ""])
    (folder/"README.md").write_text("\n".join(parts),encoding="utf-8",newline="\n")


def export(folder=None,preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name("illustrations")
    folder.mkdir(parents=True,exist_ok=True)
    if preview:preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    files=[]
    for config in CONFIGS:
        result=calculate(dict(lab=config["lab"],**config["parameters"]))
        fig,axes=plt.subplots(1,2,figsize=(13.8,6.05),layout="constrained")
        fig.suptitle(config["title"],fontweight="bold",fontsize=16)
        fig.supxlabel(textwrap.fill(config["caption"],width=145),fontsize=9,color="#506b70",fontweight="normal")
        for ax,data in zip(axes,_views(config,result)):_draw_axis(fig,ax,data)
        _details(config,result,axes)
        path=folder/(config["file_id"]+".svg")
        fig.savefig(path,metadata={"Date":None,"Creator":"Python-maths-CPGE · Physique statistique"})
        svg=path.read_text(encoding="utf-8")
        path.write_text("\n".join(line.rstrip() for line in svg.splitlines())+"\n",encoding="utf-8",newline="\n")
        if preview:fig.savefig(preview/(config["file_id"]+".png"),dpi=125)
        plt.close(fig);files.append(path.name)
    _gallery(folder)
    return files


if __name__=="__main__":print(export())
