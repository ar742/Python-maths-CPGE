"""Ising CPGE : chaîne périodique exacte et carré Metropolis à champ nul.

J>0 et kB sont absorbés dans θ=kBT/J. L'énergie exportée est en unités J,
et l'aimantation m est la moyenne des spins ±1. La formule Onsager–Yang
concerne le réseau carré infini et une limite de champ explicitement indiquée.
"""
from __future__ import annotations

import math
import numpy as np

THETA_CRITICAL = 2 / math.log(1 + math.sqrt(2))


def number(data,key,default,lo,hi,integer=False):
    value=data.get(key,default)
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):
        raise ValueError(f"{key} doit être un nombre fini.")
    if not lo<=value<=hi or (integer and value!=int(value)):
        raise ValueError(f"{key} doit être entre {lo} et {hi}"+(" et entier." if integer else "."))
    return int(value) if integer else float(value)


def choice(data,key,default,values):
    value=data.get(key,default)
    if not isinstance(value,str) or value not in values:
        raise ValueError(f"Choix inconnu pour {key}.")
    return value


def series(label,x,y,color="green",kind="line"):
    return dict(label=label,x=np.asarray(x).tolist(),y=np.asarray(y).tolist(),color=color,kind=kind)


def chart(title,xlabel,ylabel,data,logx=False,logy=False,equal=False,grid=None):
    result=dict(title=title,xlabel=xlabel,ylabel=ylabel,series=data,logx=logx,logy=logy,equal=equal)
    if grid is not None:result["grid"]={k:np.asarray(v).tolist() for k,v in grid.items()}
    return result


def metric(label,value,note=""):
    return dict(label=label,value=value if isinstance(value,str) else float(value),note=note)


def chain_levels(N):
    """Exactement 2n parois sur un anneau : E/J=−N+4n et g=2 C(N,2n)."""
    if isinstance(N,bool) or not isinstance(N,int) or N<3:
        raise ValueError("Un nombre entier de spins N≥3 est requis.")
    return [dict(n=n,walls=2*n,energy=-N+4*n,degeneracy=2*math.comb(N,2*n),
                 log_degeneracy=math.log(2*math.comb(N,2*n))) for n in range(N//2+1)]


def chain_statistics(N,theta):
    """Somme canonique exacte, normalisée après décalage de l'énergie."""
    if isinstance(theta,bool) or not isinstance(theta,(int,float)) or not math.isfinite(theta) or theta<=0:
        raise ValueError("θ=kBT/J doit être strictement positif et fini.")
    levels=chain_levels(N)
    energies=np.array([v["energy"] for v in levels],dtype=float)
    logg=np.array([v["log_degeneracy"] for v in levels])
    # E−E0=4n≥0 : jamais d'exponentielle de +N/θ.
    logs=logg-(energies+N)/theta
    maximum=float(np.max(logs));weights=np.exp(logs-maximum);probabilities=weights/np.sum(weights)
    mean=float(probabilities@energies)
    variance=float(probabilities@((energies-mean)**2))
    nonzero=probabilities>0
    entropy=float(np.sum(probabilities[nonzero]*(logg[nonzero]-np.log(probabilities[nonzero]))))
    return dict(levels=levels,probabilities=probabilities,energy=mean,energy_per_spin=mean/N,
                energy_variance=variance,heat_capacity=variance/theta**2,
                entropy=entropy,log_partition=N/theta+maximum+math.log(float(weights.sum())),
                mean_wall_pairs=float(probabilities@np.arange(len(levels))),
                magnetization=0.0)


def chain_stirling_pair_mean(N,theta):
    """Approximation thermodynamique, avec le facteur 2 corrigé du recueil."""
    if theta<=0 or not math.isfinite(theta):raise ValueError("θ>0 fini requis.")
    small=math.exp(-2/theta)
    return N*small/(2*(1+small))


def onsager_magnetization(theta):
    """m∞ à h→0+ après L→∞, à couplages isotropes J et θ=kBT/J.

    L'évaluation de 1/sinh(2/θ) par exponentielles négatives protège le calcul
    à basse température. Pour θ≥θc, m∞=0. Une taille finie à h=0 n'a pas
    cette aimantation signée d'équilibre : sa symétrie impose ⟨m⟩=0.
    """
    values=np.asarray(theta,dtype=float)
    if not np.all(np.isfinite(values)) or np.any(values<=0):
        raise ValueError("Température réduite strictement positive et finie requise.")
    safe=np.minimum(np.maximum(values,1e-300),THETA_CRITICAL)
    z=2/safe
    inverse_sinh=2*np.exp(-z)/(-np.expm1(-2*z))
    result=np.where(values<THETA_CRITICAL,np.maximum(0.,1-inverse_sinh**4)**.125,0.)
    return float(result) if result.ndim==0 else result


def _spins(spins):
    a=np.asarray(spins)
    if a.ndim!=2 or a.shape[0]!=a.shape[1] or a.shape[0]<2 or a.dtype.kind not in ["i","f"] or not np.all((a==1)|(a==-1)):
        raise ValueError("Un réseau carré de côtés ≥2 et de spins ±1 est requis.")
    return a


def energy_square(spins):
    """Chaque liaison droite/bas est comptée une fois, limites périodiques.

    Pour L=2, le tore possède des liaisons parallèles : gauche=droite et
    haut=bas, mais ce sont les quatre liaisons de la définition périodique.
    La même convention est utilisée dans delta_flip et dans les tests.
    """
    a=_spins(spins)
    return -int(np.sum(a*(np.roll(a,-1,axis=0)+np.roll(a,-1,axis=1)),dtype=np.int64))


def delta_flip(spins,i,j):
    a=_spins(spins);L=len(a)
    if not 0<=i<L or not 0<=j<L:raise ValueError("Indice de spin hors du réseau.")
    neighbors=int(a[(i-1)%L,j])+int(a[(i+1)%L,j])+int(a[i,(j-1)%L])+int(a[i,(j+1)%L])
    return 2*int(a[i,j])*neighbors


def checkerboard_sweep(spins,theta,rng,masks=None,return_stats=False):
    """Un essai par spin, en deux couleurs non voisines sur un tore de L pair.

    Chaque site propose un retournement avec probabilité 1/2, sinon identité.
    Cette proposition paresseuse évite les cycles fermés à ΔE=0 du damier
    systématique. Chaque sous-balayage conserve la loi de Boltzmann. Les voisins sont
    recalculés après le premier : une mise à jour simultanée de tout le carré
    avec les anciens voisins ne serait pas ce noyau de Metropolis.
    """
    a=_spins(spins);L=len(a)
    if L%2:raise ValueError("La mise à jour en damier exige un côté L pair.")
    if not math.isfinite(theta) or theta<=0:raise ValueError("θ>0 fini requis.")
    if masks is None:
        row,column=np.indices(a.shape);red=(row+column)%2==0;masks=(red,~red)
    accepted=0;attempted=0
    for mask in masks:
        neighbors=np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1)
        change=2*a*neighbors
        probability=np.exp(-np.maximum(change,0)/theta)
        proposed=mask&(rng.random(a.shape)<.5)
        attempted+=int(np.count_nonzero(proposed))
        flip=proposed&(rng.random(a.shape)<probability)
        accepted+=int(np.count_nonzero(flip));a[flip]*=-1
    return (accepted,attempted) if return_stats else accepted


def autocorrelation_diagnostic(values,stride=1):
    """Fenêtre au premier terme non positif ; diagnostic, pas certification."""
    a=np.asarray(values,dtype=float);N=len(a)
    if N<4 or not np.all(np.isfinite(a)):raise ValueError("Au moins quatre mesures finies requises.")
    centered=a-np.mean(a);variance=float(np.mean(centered**2))
    lagmax=min(80,N//4)
    if variance<1e-28:
        return dict(lags=list(range(lagmax+1)),acf=[1.]+[0.]*lagmax,
                    varying=False,tau_measurements=None,tau_sweeps=None,effective_samples=None,
                    standard_error_naive=None,standard_error_blocks=None,block_length=None,blocks=0)
    acf=[1.]+[float(centered[:-lag]@centered[lag:]/((N-lag)*variance)) for lag in range(1,lagmax+1)]
    positive=[]
    for value in acf[1:]:
        if value<=0:break
        positive.append(value)
    tau=.5+sum(positive)
    blocks=min(16,max(4,math.isqrt(N)));length=N//blocks
    block_means=np.mean(a[:blocks*length].reshape(blocks,length),axis=1)
    return dict(lags=list(range(lagmax+1)),acf=acf,varying=True,tau_measurements=tau,
                tau_sweeps=tau*stride,effective_samples=min(float(N),N/(2*tau)),
                standard_error_naive=float(np.std(a,ddof=1)/math.sqrt(N)),
                standard_error_blocks=float(np.std(block_means,ddof=1)/math.sqrt(blocks)),
                block_length=length,blocks=blocks)


def metropolis_square(size,theta,burnin=200,sweeps=1200,stride=5,seed=742,initial="aleatoire"):
    """Simulation déterministe pour une graine donnée, sans champ extérieur."""
    if not isinstance(size,int) or isinstance(size,bool) or size<2 or size%2:
        raise ValueError("Côté entier pair ≥2 requis.")
    if not math.isfinite(theta) or theta<=0:raise ValueError("θ>0 fini requis.")
    for value in [burnin,sweeps,stride,seed]:
        if isinstance(value,bool) or not isinstance(value,int):raise ValueError("Comptages et graine entiers requis.")
    if burnin<0 or stride<1 or sweeps<4*stride or seed<0:
        raise ValueError("Chauffe ≥0, au moins quatre mesures et graine ≥0 requises.")
    if initial not in ["aleatoire","plus"]:raise ValueError("État initial inconnu.")
    rng=np.random.default_rng(seed)
    spins=rng.choice(np.array([-1,1],dtype=np.int8),size=(size,size)) if initial=="aleatoire" else np.ones((size,size),dtype=np.int8)
    row,column=np.indices(spins.shape);red=(row+column)%2==0;masks=(red,~red)
    energies=[];magnetizations=[];steps=[];accepted=0;attempted=0
    for sweep in range(burnin+sweeps):
        count,proposed=checkerboard_sweep(spins,theta,rng,masks,return_stats=True)
        if sweep<burnin:continue
        accepted+=count;attempted+=proposed
        measured=sweep-burnin+1
        if measured%stride==0:
            steps.append(measured);energies.append(energy_square(spins)/(size*size));magnetizations.append(float(np.mean(spins)))
    energies=np.array(energies);magnetizations=np.array(magnetizations);absolute=abs(magnetizations)
    count=size*size
    return dict(spins=spins,steps=np.array(steps),energy_trace=energies,magnetization_trace=magnetizations,
                absolute_magnetization_trace=absolute,mean_energy_per_spin=float(np.mean(energies)),
                mean_magnetization=float(np.mean(magnetizations)),mean_absolute_magnetization=float(np.mean(absolute)),
                heat_capacity_per_spin=count*float(np.var(energies))/theta**2,
                acceptance_rate=accepted/attempted if attempted else 0,
                proposed_flips=attempted,accepted_flips=accepted,flip_fraction=accepted/(sweeps*count),
                absolute_diagnostic=autocorrelation_diagnostic(absolute,stride),
                energy_diagnostic=autocorrelation_diagnostic(energies,stride),
                final_magnetization=float(np.mean(spins)),final_energy_per_spin=energy_square(spins)/count,
                samples=len(energies),seed=seed)


def _diagnostic_value(value):
    return "Non estimable sur une trace constante" if value is None else value


def calculate_lab(d):
    mode=choice(d,"mode","chaine",["chaine","carre"])
    theta=number(d,"theta",2.3,.2,8)
    if mode=="chaine":
        N=number(d,"N",20,3,100,True)
        selected=number(d,"level",1,0,N//2,True)
        state=chain_statistics(N,theta);levels=state["levels"];chosen=levels[selected]
        temperatures=np.geomspace(.2,8,160);states=[chain_statistics(N,float(t)) for t in temperatures]
        energies=[v["energy"]/N for v in levels];entropies=[v["log_degeneracy"] for v in levels]
        approximate=chain_stirling_pair_mean(N,theta)
        beta_discrete=(entropies[selected+1]-entropies[selected-1])/8 if 0<selected<len(levels)-1 else None
        rows=[[v["n"],v["walls"],v["energy"],str(v["degeneracy"]),float(p)] for v,p in zip(levels,state["probabilities"])]
        return dict(metrics=[metric("Énergie exacte U/(NJ)",state["energy_per_spin"],"Chaîne périodique de N spins, champ nul"),metric("Capacité exacte C/(NkB)",state["heat_capacity"]/N,"Variance de l'énergie, sans simulation"),metric("Entropie du niveau choisi / kB",chosen["log_degeneracy"],"ln[2 C(N,2n)] ; niveau microcanonique")],
            charts=[chart("Les parois doivent se fermer par paires","Nombre de parois 2n","Probabilité canonique",[series("Probabilité exacte du niveau",[v["walls"] for v in levels],state["probabilities"],kind="stems"),series("Niveau choisi",[chosen["walls"]],[state["probabilities"][selected]],"rose","dots")]),chart("Entropie microcanonique exacte","E/(NJ)","S/kB",[series("Comptage exact",energies,entropies),series("Niveau choisi",[chosen["energy"]/N],[chosen["log_degeneracy"]],"rose","dots")]),chart("Une chaîne 1D n'a pas de transition à T>0","θ=kBT/J","U/(NJ) et C/(NkB)",[series("Énergie, chaîne finie",temperatures,[s["energy_per_spin"] for s in states]),series("Capacité, chaîne finie",temperatures,[s["heat_capacity"]/N for s in states],"rose"),series("Énergie, N→∞",temperatures,-np.tanh(1/temperatures),"gold")],logx=True)],
            table=dict(headers=["n","Parois 2n","E/J","Dégénérescence exacte","Probabilité"],rows=rows),
            notes=["L'anneau vérifie s_{N+1}=s₁. Le nombre de liaisons opposées est pair : choisir 2n liaisons puis le premier spin détermine toute la configuration. Ainsi gₙ=2 C(N,2n) et Eₙ/J=−N+4n, pour 0≤n≤⌊N/2⌋.","Le fondamental a deux configurations et E₀=−NJ. Pour N impair, toutes les liaisons ne peuvent pas être opposées. Le comptage total vaut Σgₙ=2ᴺ ; les grands entiers sont exportés en texte pour conserver leurs chiffres.","Les probabilités canoniques sont calculées par la somme complète des niveaux, après décalage de l'énergie : aucune exponentielle croissante n'est évaluée. L'aimantation signée exacte reste nulle par symétrie à champ nul.","Stirling donne βJ≈½ln[(N−2n)/(2n)], puis n≈N/[2(1+exp(2βJ))]. L'exponentielle exp(βJ) du recueil omet un facteur 2. Cette approximation thermodynamique ne remplace pas le calcul exact de petite chaîne.",f"À θ={theta:g}, la moyenne exacte de n vaut {state['mean_wall_pairs']:.6g} ; l'estimation Stirling vaut {approximate:.6g}. Un niveau microcanonique isolé est discret : sa température n'est pas définie par une dérivée exacte pour petit N."],
            theory=dict(mode=mode,N=N,theta=theta,levels=[dict(v,degeneracy=str(v["degeneracy"])) for v in levels],total_states=str(1<<N),probabilities=state["probabilities"].tolist(),energy_over_J=state["energy"],energy_per_spin=state["energy_per_spin"],heat_capacity_kb=state["heat_capacity"],entropy_kb=state["entropy"],log_partition=state["log_partition"],selected_level=selected,selected_entropy_kb=chosen["log_degeneracy"],microcanonical_betaJ_discrete=beta_discrete,mean_wall_pairs=state["mean_wall_pairs"],stirling_mean_wall_pairs=approximate,magnetization_exact=0))
    size=number(d,"size",16,8,24,True)
    if size%2:raise ValueError("Le côté du carré doit être pair : 8, 10, …, 24.")
    burnin=number(d,"burnin",200,50,1000,True);sweeps=number(d,"sweeps",1200,300,5000,True)
    stride=number(d,"stride",5,1,20,True);seed=number(d,"seed",742,0,9999999,True)
    initial=choice(d,"initial","aleatoire",["aleatoire","plus"])
    simulation=metropolis_square(size,theta,burnin,sweeps,stride,seed,initial)
    absdiag=simulation["absolute_diagnostic"];ediag=simulation["energy_diagnostic"]
    index=np.unique(np.r_[np.arange(0,simulation["samples"],max(1,math.ceil(simulation["samples"]/600))),simulation["samples"]-1]).astype(int)
    steps=simulation["steps"][index];temperatures=np.linspace(.2,8,300)
    theory_m=onsager_magnetization(theta)
    varying=absdiag["varying"] and ediag["varying"]
    observations=["Carré fini à limites périodiques, spins ±1, J>0 et champ strictement nul. E/J=−Σ⟨ij⟩sᵢsⱼ, chaque liaison comptée une fois ; le fondamental vaut E/(L²J)=−2.",f"Chauffe : {burnin} balayages ; mesure ensuite pendant {sweeps} balayages, une observation tous les {stride}. Un balayage visite chaque spin une fois en deux couleurs ; les voisins sont recalculés entre les couleurs. Graine : {seed}.","À chaque visite, un retournement est proposé avec probabilité 1/2, sinon le spin est laissé inchangé. Les retournements proposés sont acceptés avec min(1,exp(−ΔE/(Jθ))). Cette version Metropolis paresseuse évite les cycles fermés de bandes à champs locaux nuls. Le taux d'acceptation compte uniquement les retournements réellement proposés après chauffe.","La référence Onsager–Yang représente un carré infini : θc=2/ln(1+√2), m∞=[1−sinh(2/θ)⁻⁴]¹ᐟ⁸ sous θc et 0 au-dessus, après L→∞ puis h→0+. Elle ne donne pas l'aimantation exacte d'un réseau fini à champ nul.","Pour une taille finie à h=0, l'équilibre symétrique impose ⟨m⟩=0 ; une trajectoire courte peut garder un signe choisi par sa graine ou son état initial. ⟨|m|⟩ reste positif même au-dessus de θc. Son rapprochement avec m∞ doit tenir compte de la taille et de l'équilibration.","Le temps d'autocorrélation est estimé en coupant au premier terme non positif. L'erreur par blocs et l'effectif estimé sont des diagnostics de cette seule trace, sans garantie d'équilibre. Près de θc, le ralentissement critique exige des trajectoires plus longues et des comparaisons de graines ou d'états initiaux."]
    if not varying:observations.append("Au moins une trace est constante : sa corrélation et son erreur ne sont pas estimables. Une trace bloquée ne prouve pas une erreur Monte Carlo nulle ni l'exploration des deux signes d'aimantation.")
    return dict(metrics=[metric("Monte Carlo ⟨|m|⟩",simulation["mean_absolute_magnetization"],"Carré fini ; comparaison indicative avec m∞"),metric("⟨m⟩ sur cette trajectoire",simulation["mean_magnetization"],"Le signe dépend de la trajectoire, pas d'un champ appliqué"),metric("Température critique θc",THETA_CRITICAL,"Référence exacte du carré infini")],
        charts=[chart("Dernier carré fini · spins ±1","Colonne","Ligne",[],equal=True,grid=dict(x=np.arange(size),y=np.arange(size),z=simulation["spins"],vmin=-1,vmax=1)),chart("Une aimantation fluctue pendant la mesure","Balayages après chauffe","Aimantation par spin",[series("m signé",steps,simulation["magnetization_trace"][index]),series("|m|",steps,simulation["absolute_magnetization_trace"][index],"gold")]),chart("Énergie : surveiller la trace","Balayages après chauffe","E/(L²J)",[series("Énergie par spin",steps,simulation["energy_trace"][index],"rose")]),chart("Référence infinie et un point sur un carré fini","θ=kBT/J","Aimantation",[series("Onsager–Yang : m∞",temperatures,onsager_magnetization(temperatures)),series("θc",[THETA_CRITICAL,THETA_CRITICAL],[0,1],"mint"),series("Monte Carlo : ⟨|m|⟩ fini",[theta],[simulation["mean_absolute_magnetization"]],"rose","dots")]),chart("Mesures successives : autocorrélation estimée","Écart en balayages","Autocorrélation",[series("|m|",np.array(absdiag["lags"])*stride,absdiag["acf"]),series("Énergie",np.array(ediag["lags"])*stride,ediag["acf"],"rose")])],
        table=dict(headers=["Objet","Valeur","Portée"],rows=[["Taille",f"{size} × {size}","Limites périodiques"],["Nombre de mesures",simulation["samples"],"Après chauffe"],["Référence m∞",theory_m,"Carré infini, h→0+ après L→∞"],["Énergie moyenne / spin",simulation["mean_energy_per_spin"],"Unités J, estimation Monte Carlo"],["Capacité / spin",simulation["heat_capacity_per_spin"],"Unités kB, variance empirique"],["Taux d'acceptation",simulation["acceptance_rate"],"Parmi les flips proposés post-chauffe"],["Flips proposés / acceptés",f"{simulation['proposed_flips']} / {simulation['accepted_flips']}","Proposition de retournement : probabilité 1/2"],["τ intégré pour |m|",_diagnostic_value(absdiag["tau_sweeps"]),"En balayages ; fenêtre empirique"],["Effectif estimé pour |m|",_diagnostic_value(absdiag["effective_samples"]),"Pas une garantie d'équilibration"],["Erreur de ⟨|m|⟩ par blocs",_diagnostic_value(absdiag["standard_error_blocks"]),f"{absdiag['blocks']} blocs ; longueur {absdiag['block_length']} mesures"],["τ intégré pour énergie",_diagnostic_value(ediag["tau_sweeps"]),"En balayages"]]),
        notes=observations,
        theory=dict(mode=mode,theta=theta,size=size,burnin=burnin,sweeps=sweeps,stride=stride,seed=seed,initial=initial,critical_temperature=THETA_CRITICAL,infinite_spontaneous_magnetization=theory_m,finite_signed_equilibrium_magnetization=0,mean_absolute_magnetization=simulation["mean_absolute_magnetization"],mean_magnetization=simulation["mean_magnetization"],mean_energy_per_spin=simulation["mean_energy_per_spin"],heat_capacity_per_spin=simulation["heat_capacity_per_spin"],acceptance_rate=simulation["acceptance_rate"],proposed_flips=simulation["proposed_flips"],accepted_flips=simulation["accepted_flips"],proposal_flip_probability=.5,samples=simulation["samples"],measurements=dict(steps=simulation["steps"].tolist(),magnetization=simulation["magnetization_trace"].tolist(),absolute_magnetization=simulation["absolute_magnetization_trace"].tolist(),energy_per_spin=simulation["energy_trace"].tolist()),absolute_diagnostic=absdiag,energy_diagnostic=ediag,final_spins=simulation["spins"].tolist(),final_magnetization=simulation["final_magnetization"]))
