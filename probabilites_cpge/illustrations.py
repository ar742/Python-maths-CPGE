"""Six figures scientifiques autonomes : python illustrations.py.

Matplotlib sert seulement à régénérer les SVG ; l'application utilise le canvas.
"""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'python-maths-cpge-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mathematiques import (binomial, hypergeometric, polarization_moments,
                          arcsine_cdf, semicircle_cdf, wigner_matrix)

GREEN, GOLD, ROSE, INK = '#23745c','#c79432','#b66375','#17363d'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'text.color':INK,
                    'axes.labelcolor':INK,'axes.edgecolor':'#dedfd4',
                    'xtick.color':INK,'ytick.color':INK,'axes.spines.top':False,
                    'axes.spines.right':False,'svg.fonttype':'none',
                    'svg.hashsalt':'python-maths-cpge-probabilites'})


def export(folder=None, preview=None):
    folder=Path(folder) if folder else Path(__file__).with_name('illustrations')
    folder.mkdir(parents=True,exist_ok=True)
    if preview:
        preview=Path(preview);preview.mkdir(parents=True,exist_ok=True)
    files=[]

    def make(title):
        fig, axes=plt.subplots(1,2,figsize=(11.5,4.5),layout='constrained')
        fig.suptitle(title,fontsize=16,fontweight='bold')
        for ax in axes:
            ax.grid(alpha=.18)
        return fig,axes

    def save(fig,name):
        path=folder/(name+'.svg')
        fig.savefig(path,metadata={'Date':None,'Creator':'Python-maths-CPGE — probabilités'})
        text=path.read_text(encoding='utf-8')
        path.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8',newline='\n')
        if preview:
            fig.savefig(preview/(name+'.png'),dpi=130)
        plt.close(fig);files.append(path.name)

    fig,(a,b)=make('Exercice 6 · Une moyenne conservée, une loi qui se polarise')
    rng=np.random.default_rng(742);c=.35;lam=.25;n=120;x=np.full(12,c)
    paths=[x.copy()]
    for _ in range(n):
        x=(1-lam)*x+lam*(rng.random(12)<x);paths.append(x.copy())
    a.plot(np.arange(n+1),paths,color=GREEN,alpha=.4,lw=1)
    a.axhline(c,color=ROSE,lw=2,label='E(Xₙ) = 0,35');a.legend(loc='center right')
    a.set(xlabel='Étape n',ylabel='Xₙ',ylim=(-.03,1.03),title='Douze trajectoires')
    m=polarization_moments(c,lam,n)
    b.plot(m[:,2],label='E(Xₙ²)',color=GREEN)
    b.plot(m[:,3],label='E(Xₙ³)',color=GOLD)
    b.plot(m[:,4],label='E(Xₙ⁴)',color=ROSE)
    b.axhline(c,color=INK,ls='--',label='Limite c')
    b.set(xlabel='Étape n',ylabel='Moment',title='Moments calculés par récurrence');b.legend()
    save(fig,'polarisation')

    fig,(a,b)=make('Exercice 7 · Le maximum uniforme et sa vitesse de convergence')
    u=np.linspace(0,1,400)
    for n,col in [(1,INK),(5,GOLD),(20,GREEN)]:
        a.plot(u,u**n,color=col,label=f'n = {n}')
    a.set(xlabel='x',ylabel='P(Mₙ ≤ x)',title='Le maximum se rapproche de 1');a.legend()
    z=np.linspace(0,6,400)
    for n,col in [(10,GOLD),(100,GREEN)]:
        b.plot(z,1-(1-z/n)**n,color=col,label=f'n = {n}')
    b.plot(z,1-np.exp(-z),color=ROSE,ls='--',label='Limite Exp(1)')
    b.set(xlabel='z',ylabel='P(n(1−Mₙ) ≤ z)',title='L’écart renormalisé reste aléatoire');b.legend()
    save(fig,'maximum_uniforme')

    fig,(a,b)=make('Exercice 8 · Le spectre d’un chemin converge vers arcsinus')
    n=80;eig=np.sort(2*np.cos(np.arange(1,n+1)*np.pi/(n+1)))
    edges=np.linspace(-2,2,25);centers=(edges[:-1]+edges[1:])/2
    mass=np.diff(arcsine_cdf(edges));counts,_=np.histogram(eig,bins=edges)
    a.bar(centers,counts/n,width=.13,color=GREEN,alpha=.65,label='Spectre T₈₀')
    a.plot(centers,mass,color=ROSE,marker='o',ms=3,label='Masses limites par intervalle')
    a.set(xlabel='Valeur propre',ylabel='Masse par intervalle',title='Davantage de masse près des bords');a.legend()
    j=np.arange(1,21)
    for k,col in [(1,GREEN),(3,GOLD)]:
        b.plot(j,np.sqrt(2/21)*np.sin(j*k*np.pi/21),'-o',ms=3,color=col,label=f'Mode k = {k}')
    b.set(xlabel='Sommet j du chemin',ylabel='Composante du vecteur propre',title='Vecteurs propres de T₂₀');b.legend()
    save(fig,'arcsinus_chemin')

    fig,(a,b)=make('Exercice 8 · Arcsinus et demi-cercle : deux limites différentes')
    edges=np.linspace(-2.6,2.6,35);centers=(edges[1:]+edges[:-1])/2
    values=np.concatenate([np.linalg.eigvalsh(wigner_matrix(120,'signes',rng)) for _ in range(5)])
    count,_=np.histogram(values,bins=edges)
    a.bar(centers,count/len(values),width=.13,color=GREEN,alpha=.7,label='W₁₂₀/√120, 5 matrices')
    a.plot(centers,np.diff(semicircle_cdf(edges)),color=ROSE,label='Demi-cercle')
    a.plot(centers,np.diff(arcsine_cdf(edges)),color=GOLD,label='Arcsinus')
    a.set(xlabel='Valeur propre',ylabel='Masse par intervalle',title='La normalisation fixe l’échelle');a.legend()
    power=np.arange(1,5);arc=np.array([2,6,20,70]);sc=np.array([1,2,5,14])
    b.bar(power-.18,arc,width=.36,color=GOLD,label='Arcsinus : C(2r,r)')
    b.bar(power+.18,sc,width=.36,color=GREEN,label='Demi-cercle : Catalan')
    b.set(xlabel='r (moment d’ordre 2r)',ylabel='Moment limite',title='Les moments distinguent les lois',xticks=power);b.legend()
    save(fig,'wigner_demi_cercle')

    fig,(a,b)=make('Exercice 4 · Sans remise, la dépendance réduit la variance')
    k=np.arange(11);hg=hypergeometric(10,10,10);bi=binomial(10,.5)
    a.plot(k,hg,'o-',color=GREEN,label='Sans remise : hypergéométrique')
    a.plot(k,bi,'o-',color=ROSE,label='Avec remise : binomiale')
    a.set(xlabel='Nombre de rouges',ylabel='Probabilité',title='Urne : 10 rouges, 10 bleues, 10 tirages');a.legend(fontsize=9)
    draws=np.arange(1,21)
    b.plot(draws,draws/4,color=ROSE,label='Avec remise')
    b.plot(draws,draws/4*(20-draws)/19,color=GREEN,label='Sans remise')
    b.set(xlabel='Nombre de tirages d',ylabel='Variance',title='Tirer toute l’urne devient déterministe');b.legend()
    save(fig,'urnes_dependance')

    fig,(a,b)=make('TP et grands nombres · Fréquences, fluctuations et preuve')
    p=.5;N=4000;trials=rng.binomial(1,p,N);t=np.arange(1,N+1)
    a.plot(t,np.cumsum(trials)/t,color=GREEN,lw=1,label='Fréquence observée')
    a.axhline(p,color=ROSE,label='p = 1/2');a.set(xlabel='Nombre d’essais',ylabel='Fréquence',ylim=(.35,.65),title='Une trajectoire n’est pas monotone');a.legend()
    sizes=np.arange(20,1001,20);epsilon=.1
    exact=[sum(v for k,v in enumerate(binomial(int(n),p)) if abs(k/n-p)>=epsilon-1e-14) for n in sizes]
    b.semilogy(sizes,exact,color=GREEN,label='Probabilité binomiale')
    b.semilogy(sizes,np.minimum(1,.25/(sizes*epsilon**2)),color=GOLD,label='Borne de Tchebychev')
    b.set(xlabel='Taille du bloc n',ylabel='P(|K/n−p| ≥ 0,1)',title='Une borne conservatrice, valable pour tout n');b.legend()
    save(fig,'grands_nombres')
    return files


if __name__=='__main__':
    print('\n'.join(export()))
