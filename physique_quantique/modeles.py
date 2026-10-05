"""Neuf laboratoires de physique quantique, avec NumPy uniquement.

Les unités réduites et les conditions aux limites sont déclarées dans chaque
laboratoire. Les courbes sont des diagnostics ; les formules exactes sont aussi
exportées. Aucune évolution par différences finies n'est utilisée ici.
"""
from __future__ import annotations

import itertools
import math
import numpy as np

# SI exact (2019), puis valeurs recommandées CODATA 2022.
H = 6.62607015e-34
HBAR = H / (2 * math.pi)
E_CHARGE = 1.602176634e-19
C = 299792458
KB = 1.380649e-23
ME = 9.1093837139e-31
EPS0 = 8.8541878188e-12
GAMMA_PROTON = 2.6752218708e8  # rad s^-1 T^-1, proton libre
PHI0 = H / (2 * E_CHARGE)
BOHR_RADIUS = 4 * math.pi * EPS0 * HBAR**2 / (ME * E_CHARGE**2)
HARTREE_EV = ME * (E_CHARGE**2 / (4 * math.pi * EPS0))**2 / HBAR**2 / E_CHARGE

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
PAULI = [SX, SY, SZ]


def number(data, key, default, lo, hi, integer=False):
    v = data.get(key, default)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise ValueError(f"{key} doit être un nombre fini.")
    if not lo <= v <= hi or (integer and v != int(v)):
        raise ValueError(f"{key} doit être entre {lo} et {hi}" + (" et entier." if integer else "."))
    return int(v) if integer else float(v)


def choice(data, key, default, values):
    v = data.get(key, default)
    if not isinstance(v, str) or v not in values:
        raise ValueError(f"Choix inconnu pour {key}.")
    return v


def series(label, x, y, color="green", kind="line"):
    return dict(label=label, x=np.asarray(x).tolist(), y=np.asarray(y).tolist(), color=color, kind=kind)


def chart(title, xlabel, ylabel, data, logx=False, logy=False, equal=False, grid=None):
    result = dict(title=title, xlabel=xlabel, ylabel=ylabel, series=data,
                  logx=logx, logy=logy, equal=equal)
    if grid is not None:
        result["grid"] = {k: np.asarray(v).tolist() for k, v in grid.items()}
    return result


def metric(label, value, note=""):
    return dict(label=label, value=value if isinstance(value, str) else float(value), note=note)


def table(headers, rows):
    return dict(headers=headers, rows=rows)


def complex_text(z):
    z = complex(z)
    return f"{z.real:.5g}{z.imag:+.5g}i"


def matrix_text(A):
    return " ; ".join("[" + ", ".join(complex_text(v) for v in row) + "]" for row in np.asarray(A))


def positive(a):
    """Plancher réservé à l'affichage logarithmique, jamais aux résultats exacts."""
    return np.maximum(a, 1e-16)


def normal_density(x, mean, variance):
    return np.exp(-(np.asarray(x) - mean)**2 / (2 * variance)) / math.sqrt(2 * math.pi * variance)


def box_mode(n, x, boundary="parois"):
    """Fonction propre normalisée sur 0≤x≤1, sans dimension."""
    x = np.asarray(x)
    return math.sqrt(2) * np.sin(math.pi * n * x) if boundary == "parois" else np.exp(2j * math.pi * n * x)


def box_levels(boundary="parois", count=12):
    """Premières coquilles exactes ; le domaine énuméré couvre chaque coquille."""
    values = range(1, 9) if boundary == "parois" else range(-8, 9)
    shells = {}
    for state in itertools.product(values, repeat=3):
        s = sum(n*n for n in state)
        shells.setdefault(s, []).append(state)
    levels = sorted(shells)[:count]
    # Pour les coquilles demandées, tout composant est <9 en valeur absolue.
    if levels and levels[-1] >= 81:
        raise ValueError("Trop de niveaux demandés pour cette énumération exacte.")
    return [dict(level=s, degeneracy=len(shells[s]), states=shells[s]) for s in levels]


def box_degeneracy(level, boundary):
    bound = math.isqrt(level)
    values = range(1, bound+1) if boundary == "parois" else range(-bound, bound+1)
    return sum(sum(v*v for v in q) == level for q in itertools.product(values, repeat=3))


def boite(d):
    boundary = choice(d, "boundary", "parois", ["parois", "periodique"])
    L_nm = number(d, "L_nm", 1, .2, 5)
    lo, hi = (1, 6) if boundary == "parois" else (-4, 4)
    ns = [number(d, key, 1, lo, hi, True) for key in ["nx", "ny", "nz"]]
    mix = number(d, "mix", 0, 0, 1)
    phase = math.radians(number(d, "phase", 0, -180, 180))
    time = number(d, "time", 0, 0, 8)
    e1 = sum(n*n for n in ns)
    e2 = (ns[0]+1)**2 + ns[1]**2 + ns[2]**2
    scale = (math.pi if boundary == "parois" else 2*math.pi)**2 * HBAR**2 / (2*ME*(L_nm*1e-9)**2)
    x = np.linspace(0, 1, 321)
    u = box_mode(ns[0], x, boundary)
    v = box_mode(ns[0]+1, x, boundary)
    psi = math.sqrt(1-mix)*u*np.exp(-1j*e1*time) + math.sqrt(mix)*v*np.exp(1j*(phase-e2*time))
    density = abs(psi)**2
    mesh = np.linspace(0, 1, 61)
    p = math.sqrt(1-mix)*box_mode(ns[0],mesh,boundary)*np.exp(-1j*e1*time)
    p += math.sqrt(mix)*box_mode(ns[0]+1,mesh,boundary)*np.exp(1j*(phase-e2*time))
    joint = abs(box_mode(ns[1],mesh,boundary))[:,None]**2 * abs(p)[None,:]**2
    shells = box_levels(boundary)
    mean_energy = (1-mix)*e1+mix*e2
    variance_energy = mix*(1-mix)*(e2-e1)**2
    degeneracy = box_degeneracy(e1,boundary)
    rows = [[q["level"], q["level"]*scale/E_CHARGE, q["degeneracy"], ", ".join(str(v) for v in q["states"][:6]) + ("…" if q["degeneracy"]>6 else "")] for q in shells]
    return dict(
        metrics=[metric("Énergie moyenne · eV",mean_energy*scale/E_CHARGE,"Électron ; E₀ × moyenne des sommes nᵢ²"),
                 metric("Dégénérescence du premier mode",degeneracy,"Modes distincts d'une même énergie, sans spin"),
                 metric("Norme exacte",1,"Deux modes orthogonaux ; poids 1−mix et mix")],
        charts=[chart("Densité marginale le long de x","x/L","L × densité marginale",[series("État à l'instant choisi",x,density),series("Premier mode seul",x,abs(u)**2,"mint")]),
                chart("Présence dans le plan · z intégré","x/L","y/L",[],equal=True,grid=dict(x=mesh,y=mesh,z=joint)),
                chart("Premiers niveaux et dégénérescences","E/E₀","Nombre de modes",[series("Dégénérescence",[q["level"] for q in shells],[q["degeneracy"] for q in shells],"gold","stems")])],
        table=table(["E/E₀","Énergie · eV","Dégénérescence","Exemples (nₓ,nᵧ,n_z)"],rows),
        notes=["Parois infinies : ψ=0 sur chaque face, nᵢ≥1 et E₀=π²ℏ²/(2mL²). Périodicité : ψ et sa dérivée sont périodiques, nᵢ∈ℤ et E₀=(2π)²ℏ²/(2mL²). Ce sont deux problèmes distincts.",
               "La particule est libre à l'intérieur du cube. Aux parois infinies, sa dérivée n'est pas imposée périodique : la condition supplémentaire imprimée dans le TP est supprimée.",
               "Le second mode est (nₓ+1,nᵧ,n_z). L'état est √(1−mix)|n⟩+√mix e^{iφ}|n+(1,0,0)⟩, avec les phases d'évolution exactes. Le temps affiché vaut tE₀/ℏ.",
               "Le TP donne E₁₁₁=3E₀ ; le niveau suivant (2,1,1) et ses permutations vaut 6E₀, de dégénérescence 3. Les dégénérescences affichées couvrent les coquilles complètes et ne tiennent pas compte du spin."],
        theory=dict(boundary=boundary,mode=ns,second_mode=[ns[0]+1,ns[1],ns[2]],energy_scale_eV=scale/E_CHARGE,
                    energy_levels=[e1,e2],mean_energy=mean_energy,energy_variance=variance_energy,
                    degeneracy=degeneracy,normalization=1,levels=shells))


def gaussian_moments(sigma, chirp, time, p0=0):
    """ψ₀∝exp[−(1−iχ)x²/(4σ²)+ip₀x], ℏ=m=1 ; propagation libre."""
    varp = (1+chirp**2)/(4*sigma**2)
    cov = chirp/2+time*varp
    varx = sigma**2+chirp*time+time**2*varp
    return dict(mean_x=p0*time, mean_p=p0, variance_x=varx,
                variance_p=varp, covariance=cov, uncertainty=math.sqrt(varx*varp),
                covariance_determinant=varx*varp-cov**2)


def gaussian_wavefunction(x, sigma, chirp, time=0, p0=0):
    z = 1+1j*time*(1-1j*chirp)/(2*sigma*sigma)
    x = np.asarray(x)
    return (2*math.pi*sigma*sigma)**(-.25)/np.sqrt(z) * np.exp(
        -(1-1j*chirp)*(x-p0*time)**2/(4*sigma*sigma*z)+1j*p0*x-.5j*p0*p0*time)


def heisenberg(d):
    mode = choice(d,"mode","gaussienne",["gaussienne","fente","estimations"])
    sigma = number(d,"sigma",1,.2,2)
    chirp = number(d,"chirp",0,-3,3)
    time = number(d,"time",0,0,6)
    p0 = number(d,"p0",0,-3,3)
    width = number(d,"width",1,.2,4)
    wavelength = number(d,"wavelength_nm",550,380,780)
    omega = number(d,"omega",1,.2,3)
    if mode == "fente":
        ratio = wavelength/(1000*width)
        u = np.linspace(-6,6,700)
        angle = math.degrees(math.asin(ratio)) if ratio<=1 else None
        q = np.linspace(-width/2,width/2,120)
        return dict(metrics=[metric("Premier zéro · degrés",angle if angle is not None else "Hors du domaine propagatif","sin θ=λ/a ; a en µm, λ en nm"),metric("Écart type de position · µm",width/math.sqrt(12),"Amplitude uniforme idéale dans la fente"),metric("Écart type d'impulsion","Infini","Queues sinc² ; le second moment diverge")],
            charts=[chart("Diffraction d'une fente idéale","u=a sin θ/λ","I/I(0)",[series("sinc²(u)",u,np.sinc(u)**2)]),chart("Localisation initiale idéalisée","x · µm","Densité · µm⁻¹",[series("Densité uniforme",q,np.full_like(q,1/width)),series("Bords de la fente",[-width/2,-width/2,width/2,width/2],[0,1/width,1/width,0],"gold")])],
            table=table(["Grandeur","Valeur"],[["a · µm",width],["λ · nm",wavelength],["sin θ du premier zéro",ratio],["Échelle d'impulsion","ℏ/a ; ce n'est pas Δp RMS"],["Densité en impulsion","a/(2πℏ) × sinc²(ap/(2πℏ))"]]),
            notes=["La transformée de Fourier d'une amplitude rectangulaire est un sinus cardinal. Avec sinc(u)=sin(πu)/(πu), l'intensité relative est sinc²(a sin θ/λ).", "Le tracé couvre la transformée complète en u ; seuls |u|≤a/λ correspondent à des angles propagatifs. Le premier zéro est accessible si λ≤a.","Les bords abrupts produisent des queues ∝1/p² : la variance de p diverge. L'estimation angulaire λ/a est une largeur du lobe central, pas un produit exact d'écarts types. Une fente réelle aux bords lissés modifie ces queues."],
            theory=dict(first_zero_sine=ratio,first_zero_angle_degrees=angle,position_std_um=width/math.sqrt(12),momentum_variance_finite=False))
    if mode == "estimations":
        widths=np.geomspace(.12,3,250)
        bound=1/(8*widths**2)+omega**2*widths**2/2
        radii=np.linspace(.25,5,240)
        hydrogen=.5/radii**2-1/radii
        optimum=1/math.sqrt(2*omega)
        return dict(metrics=[metric("Énergie minimale de l'oscillateur",omega/2,"Borne rigoureuse, ℏ=m=1"),metric("Largeur minimisante Δx",optimum,"Gaussienne fondamentale : égalité"),metric("Estimation de l'hydrogène · eV",-HARTREE_EV/2,"Heuristique p≈ℏ/r ; noyau immobile")],
            charts=[chart("Une borne de l'énergie par Heisenberg","Δx","Énergie réduite",[series("1/(8Δx²)+ω²Δx²/2",widths,bound),series("ℏω/2",widths,np.full_like(widths,omega/2),"gold")],logx=True),chart("Échelle atomique par une estimation","r/a₀","Énergie / Hartree",[series("1/(2r²)−1/r",radii,hydrogen),series("Minimum estimé",[1],[-.5],"rose","dots")])],
            table=table(["Résultat","Statut"],[["Oscillateur : E≥ℏω/2","Borne exacte ; ⟨x⟩=⟨p⟩=0 au minimum"],["Puits infini 1D : E≥ℏ²/(2mL²)","Borne faible ; énergie exacte π²ℏ²/(2mL²)"],["Rayon de Bohr · pm",BOHR_RADIUS*1e12],["État 1s exact : ⟨r⟩=3a₀/2 · pm",1.5*BOHR_RADIUS*1e12],["Hydrogène : E₀≈−13,6 eV","Échelle heuristique, sans preuve à partir de ΔxΔp seule"]]),
            notes=["Pour l'oscillateur, E≥Δp²/2+ω²Δx²/2≥1/(8Δx²)+ω²Δx²/2. Minimiser cette fonction donne E≥ω/2. La gaussienne fondamentale atteint exactement cette borne.","Pour une variable confinée à [0,L], Δx≤L/2. Heisenberg impose Δp≥ℏ/L, donc une énergie de confinement non nulle ; cette borne ne fournit pas le facteur π² exact.","Pour l'hydrogène, on pose heuristiquement p≈ℏ/r, sans identifier r à un écart type. L'énergie obtenue est minimale à a₀ et vaut −13,6 eV. L'égalité numérique avec le niveau fondamental nécessite le problème coulombien ou un calcul variationnel adapté, et n'est pas une conséquence rigoureuse de la seule inégalité d'Heisenberg."],
            theory=dict(oscillator_bound=omega/2,oscillator_optimal_sigma=optimum,bohr_radius_m=BOHR_RADIUS,hydrogen_estimate_eV=-HARTREE_EV/2))
    g=gaussian_moments(sigma,chirp,time,p0)
    sx=math.sqrt(g["variance_x"]);sp=math.sqrt(g["variance_p"])
    x=np.linspace(min(-5*sigma,g["mean_x"]-5*sx),max(5*sigma,g["mean_x"]+5*sx),360)
    p=np.linspace(p0-5*sp,p0+5*sp,260)
    ts=np.linspace(0,6,240)
    moments=[gaussian_moments(sigma,chirp,t,p0) for t in ts]
    return dict(metrics=[metric("Δx Δp",g["uncertainty"],"ℏ=m=1 ; toujours ≥1/2"),metric("Covariance symétrisée",g["covariance"],"½⟨XP+PX⟩"),metric("Δx²Δp²−Cov²",g["covariance_determinant"],"Égal à 1/4 : borne de Robertson–Schrödinger saturée")],
        charts=[chart("Étalement et déplacement du paquet","x","|ψ|²",[series("Au temps choisi",x,normal_density(x,g["mean_x"],g["variance_x"])),series("Au départ",x,normal_density(x,0,sigma*sigma),"mint")]),chart("Impulsion : distribution conservée","p","Densité en p",[series("Impulsion",p,normal_density(p,p0,g["variance_p"]),"gold")]),chart("Incertitude et corrélation sous évolution libre","t","Produit ΔxΔp",[series("Paquet gaussien",ts,[v["uncertainty"] for v in moments]),series("Borne 1/2",ts,np.full_like(ts,.5),"rose")])],
        table=table(["Grandeur","Valeur"],[["⟨x⟩",g["mean_x"]],["⟨p⟩",p0],["Δx",sx],["Δp",sp],["Covariance initiale",chirp/2],["Chirp χ",chirp]]),
        notes=["État initial normalisé : ψ₀(x)=(2πσ²)⁻¹ᐟ⁴ exp[−(1−iχ)x²/(4σ²)+ip₀x]. Le chirp χ ajoute une phase quadratique et corrèle position et impulsion.","Avec ℏ=m=1, Δp²=(1+χ²)/(4σ²), Δx²(t)=σ²+χt+t²Δp² et Cov(t)=χ/2+tΔp². Un chirp négatif peut d'abord contracter le paquet.","La borne simple ΔxΔp≥1/2 n'est saturée que lorsque Cov=0. Cette gaussienne pure sature toujours la borne renforcée Δx²Δp²−Cov²≥1/4. Le déplacement du centre ⟨x⟩=p₀t suit Ehrenfest."],theory=g)


def _cos_sinc(q, distance):
    """cos(qd), sin(qd)/q, avec limite analytique exacte à q=0."""
    distance=np.asarray(distance)
    if abs(q)<1e-10:
        # Série locale évitant une perte de précision près du sommet.
        z=q*distance
        return 1-z*z/2+z**4/24, distance*(1-z*z/6+z**4/120)
    return np.cos(q*distance),np.sin(q*distance)/q


def scattering(energy,height,width=1,mode="barriere"):
    """Diffusion stationnaire, amplitude incidente 1, ℏ=m=1.

    La transmission est un RAPPORT DE FLUX. Pour la marche sous le seuil,
    la queue évanescente ne transporte aucun flux stationnaire transmis.
    """
    if energy<=0 or height<0 or width<=0:
        raise ValueError("E>0, V≥0 et a>0 requis.")
    k=math.sqrt(2*energy);q=np.sqrt(complex(2*(energy-height)))
    if mode=="marche":
        r=(k-q)/(k+q);t=2*k/(k+q)
        T=float(q.real/k*abs(t)**2)
        return dict(k=k,q=q,r=r,t=t,R=float(abs(r)**2),T=T,boundary_amplitude=t)
    if mode!="barriere":raise ValueError("Mode de diffusion inconnu.")
    cosine,sinc=_cos_sinc(q,width)
    denominator=cosine-.5j*(k*k+q*q)/k*sinc
    at_right=1/denominator
    psi0=at_right*(cosine-1j*k*sinc)
    r=psi0-1;t=at_right*np.exp(-1j*k*width)
    return dict(k=k,q=q,r=complex(r),t=complex(t),R=float(abs(r)**2),T=float(abs(t)**2),boundary_amplitude=complex(at_right))


def scattering_wave(x,solution,width=1,mode="barriere"):
    x=np.asarray(x,dtype=float);k=solution["k"];q=solution["q"];r=solution["r"];t=solution["t"]
    psi=np.empty(x.shape,dtype=complex);derivative=np.empty(x.shape,dtype=complex)
    left=x<0
    psi[left]=np.exp(1j*k*x[left])+r*np.exp(-1j*k*x[left])
    derivative[left]=1j*k*(np.exp(1j*k*x[left])-r*np.exp(-1j*k*x[left]))
    if mode=="marche":
        right=~left
        psi[right]=t*np.exp(1j*q*x[right]);derivative[right]=1j*q*psi[right]
    else:
        inner=(x>=0)&(x<=width);right=x>width
        cosine,sinc=_cos_sinc(q,width-x[inner]);at_right=solution["boundary_amplitude"]
        psi[inner]=at_right*(cosine-1j*k*sinc)
        derivative[inner]=at_right*(q*q*sinc+1j*k*cosine)
        psi[right]=t*np.exp(1j*k*x[right]);derivative[right]=1j*k*psi[right]
    return psi,derivative


def scattering_residuals(solution,width,mode):
    k=solution["k"];q=solution["q"];r=solution["r"];t=solution["t"]
    if mode=="marche":
        return [abs(1+r-t),abs(1j*k*(1-r)-1j*q*t)]
    cosine,sinc=_cos_sinc(q,width);end=solution["boundary_amplitude"]
    residuals=[abs(1+r-end*(cosine-1j*k*sinc)),abs(1j*k*(1-r)-end*(q*q*sinc+1j*k*cosine))]
    residuals += [abs(end-t*np.exp(1j*k*width)),abs(1j*k*end-1j*k*t*np.exp(1j*k*width))]
    return [float(v) for v in residuals]


def diffusion(d):
    mode=choice(d,"mode","barriere",["barriere","marche"])
    E=number(d,"energy",1,.1,4);V=number(d,"height",2,0,4);a=number(d,"width",1,.05,4)
    s=scattering(E,V,a,mode);x=np.linspace(-4,a+4,720);psi,derivative=scattering_wave(x,s,a,mode)
    potential=np.where(x>=0,V,0) if mode=="marche" else np.where((x>=0)&(x<=a),V,0)
    energies=np.linspace(.05,4.5,210);coeff=[scattering(e,V,a,mode) for e in energies]
    residual=scattering_residuals(s,a,mode);current=np.imag(np.conj(psi)*derivative)
    flux_error=float(np.max(abs(current-s["k"]*s["T"])))
    return dict(metrics=[metric("Transmission T · flux",s["T"],"T=jtransmis/jincident"),metric("Réflexion R",s["R"],"R+T=1 pour ce potentiel réel"),metric("Écart maximal aux raccords",max(residual),"Continuité de ψ et de ψ′ ; diagnostic numérique")],
        charts=[chart("Potentiel et énergie incidente","x","Énergie réduite",[series("V(x)",x,potential,"gold"),series("E",x,np.full_like(x,E),"rose")]),chart("Fonction d'onde stationnaire","x","Amplitude / densité",[series("Re ψ",x,psi.real),series("Im ψ",x,psi.imag,"rose"),series("|ψ|²",x,abs(psi)**2,"gold")]),chart("Un spectre de transmission","E","Probabilité de flux",[series("T",energies,[q["T"] for q in coeff]),series("R",energies,[q["R"] for q in coeff],"rose"),series("Point choisi",[E],[s["T"]],"gold","dots")])],
        table=table(["Objet","Valeur"],[["k incident",s["k"]],["q dans le potentiel",complex_text(s["q"])],["Amplitude réfléchie r",complex_text(s["r"])],["Amplitude transmise t",complex_text(s["t"])],["R+T",s["R"]+s["T"]],["Variation observée du courant",flux_error]]),
        notes=["Unités réduites ℏ=m=1 ; potentiel réel, particule incidente de la gauche, aucune onde incidente de la droite. La fonction d'onde de diffusion n'est pas normalisable sur toute la droite : amplitude incidente fixée à 1.","La marche semi-infinie et la barrière de largeur finie sont distinctes. Si E<V, la marche possède une queue évanescente mais T=0 ; la barrière peut transmettre par effet tunnel.","T est un rapport de courants, pas toujours |t|² : à la marche au-dessus du seuil, T=(q/k)|t|². Pour la barrière, les potentiels extérieurs identiques donnent T=|t|².","La formule utilise sin(qa)/q avec sa limite a : le cas E=V est traité exactement, sans division par zéro. Au-dessus de la barrière, qa entier multiple de π donne une résonance T=1.","Pour E<V et une barrière épaisse, T décroît exponentiellement. La conservation du courant et les raccords sont calculés avec les amplitudes complexes complètes."],
        theory=dict(energy=E,height=V,width=a,R=s["R"],T=s["T"],r=[s["r"].real,s["r"].imag],t=[s["t"].real,s["t"].imag],raccord_residuals=residual,current_error=flux_error))


def hermite_wavefunction(n,x):
    """Fonction propre normalisée, x en √(ℏ/mω), récurrence stable."""
    x=np.asarray(x,dtype=float)
    first=math.pi**(-.25)*np.exp(-x*x/2)
    if n==0:return first
    second=math.sqrt(2)*x*first
    for j in range(1,n):
        first,second=second,math.sqrt(2/(j+1))*x*second-math.sqrt(j/(j+1))*first
    return second


def coherent_moments(alpha,phase,time):
    amplitude=alpha*np.exp(1j*(phase-time))
    return dict(mean_x=math.sqrt(2)*float(amplitude.real),mean_p=math.sqrt(2)*float(amplitude.imag),
                variance_x=.5,variance_p=.5,energy=alpha**2+.5)


def oscillateur(d):
    mode=choice(d,"mode","stationnaire",["stationnaire","coherent"])
    n=number(d,"n",0,0,10,True);alpha=number(d,"alpha",1.5,0,3)
    phase=math.radians(number(d,"phase",0,-180,180));time=number(d,"time",0,0,12)
    x=np.linspace(-8,8,650);potential=x*x/2
    if mode=="stationnaire":
        wave=hermite_wavefunction(n,x)*np.exp(-1j*(n+.5)*time)
        energy=n+.5;meanx=meanp=0;variance=n+.5;density=abs(wave)**2
        subtitle=f"État propre n={n}"
    else:
        g=coherent_moments(alpha,phase,time);meanx=g["mean_x"];meanp=g["mean_p"]
        energy=g["energy"];variance=.5;density=normal_density(x,meanx,.5)
        wave=np.sqrt(density)*np.exp(1j*meanp*x)
        subtitle="État cohérent · phase globale omise"
    levels=np.arange(7)
    spectrum=[series(f"n={j}",[-3.6,3.6],[j+.5,j+.5],"mint") for j in levels]
    spectrum += [series("V=x²/2",x,potential,"gold"),series("Énergie moyenne",[-4,4],[energy,energy],"rose")]
    ts=np.linspace(0,2*math.pi,220)
    position=np.full_like(ts,0) if mode=="stationnaire" else math.sqrt(2)*alpha*np.cos(phase-ts)
    momentum=np.full_like(ts,0) if mode=="stationnaire" else math.sqrt(2)*alpha*np.sin(phase-ts)
    return dict(metrics=[metric("Énergie moyenne",energy,"En unités ℏω"),metric("Δx Δp",variance,"Fondamental/cohérent : 1/2 ; état n : n+1/2"),metric("Position moyenne ⟨x⟩",meanx,"Longueur en √(ℏ/mω)")],
        charts=[chart(subtitle,"x","Densité / amplitude",[series("|ψ|²",x,density),series("Re ψ",x,wave.real,"mint")]),chart("Quantification de l'énergie","x","E/ℏω",spectrum),chart("Ehrenfest : trajectoire du centre","⟨x⟩","⟨p⟩",[series("Centre sur une période",position,momentum),series("Au temps choisi",[meanx],[meanp],"rose","dots")],equal=True)],
        table=table(["Grandeur","Valeur"],[["État",mode],["Δx²",variance],["Δp²",variance],["⟨p⟩",meanp],["Énergie du fondamental",.5],["Norme analytique",1]]),
        notes=["Unités ℏ=m=ω=1. Les états propres ont Eₙ=n+1/2 et ψₙ∝Hₙ(x)e^{−x²/2}. Les fonctions d'Hermite normalisées sont évaluées par récurrence, sans troncature spectrale.","La densité d'un état propre reste fixe ; seule sa phase globale évolue. Sa variance vaut n+1/2, et le fondamental sature Heisenberg.","Un état cohérent |α⟩ garde une densité gaussienne de variance 1/2. Son centre suit ⟨x⟩=√2 Re(αe^{−it}), ⟨p⟩=√2 Im(αe^{−it}) et l'énergie vaut |α|²+1/2.","Pour l'état cohérent, Re ψ est dessiné avec la phase spatiale correcte mais une phase globale conventionnelle omise. Elle ne change ni la densité ni les observables."],
        theory=dict(mode=mode,energy=energy,mean_x=meanx,mean_p=meanp,variance_x=variance,variance_p=variance,normalization=1))


def polarization_observable(angle):
    return math.cos(2*angle)*SZ+math.sin(2*angle)*SX


def pair_density(visibility,state="werner"):
    if not 0<=visibility<=1:raise ValueError("Visibilité comprise entre 0 et 1 requise.")
    if state=="werner":
        phi=np.array([1,0,0,1],dtype=complex)/math.sqrt(2)
        pure=np.outer(phi,phi.conj())
    elif state=="classique":pure=np.diag([.5,0,0,.5]).astype(complex)
    else:raise ValueError("État de la paire inconnu.")
    return visibility*pure+(1-visibility)*np.eye(4)/4


def pair_probabilities(rho,a,b):
    A=polarization_observable(a);B=polarization_observable(b)
    values=[]
    for sa,sb in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        PA=(I2+sa*A)/2;PB=(I2+sb*B)/2
        values.append(float(np.trace(rho@np.kron(PA,PB)).real))
    return np.array(values)


def pair_correlation(rho,a,b):
    return float(np.trace(rho@np.kron(polarization_observable(a),polarization_observable(b))).real)


def partial_trace_b(rho):
    return np.trace(np.asarray(rho).reshape(2,2,2,2),axis1=1,axis2=3)


def partial_transpose_b(rho):
    return np.asarray(rho).reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)


def intrication(d):
    state=choice(d,"state","werner",["werner","classique"])
    visibility=number(d,"visibility",1,0,1)
    angles=[math.radians(number(d,k,v,-180,180)) for k,v in [("a",0),("b",22.5),("a2",45),("b2",-22.5)]]
    a,b,a2,b2=angles;rho=pair_density(visibility,state)
    probabilities=pair_probabilities(rho,a,b)
    Es=[pair_correlation(rho,aa,bb) for aa,bb in [(a,b),(a,b2),(a2,b),(a2,b2)]]
    S=abs(Es[0]+Es[1]+Es[2]-Es[3])
    pteig=np.linalg.eigvalsh(partial_transpose_b(rho))
    entangled=state=="werner" and visibility>1/3+1e-14
    optimal=2*math.sqrt(2)*visibility if state=="werner" else 2*visibility
    scan=np.linspace(-90,90,260)
    curve=[pair_correlation(rho,a,math.radians(q)) for q in scan]
    vis=np.linspace(0,1,180)
    name="Werner autour de Φ⁺" if state=="werner" else "Mélange classique dépolarisé"
    return dict(metrics=[metric("CHSH avec ces quatre angles",S,"|E(a,b)+E(a,b′)+E(a′,b)−E(a′,b′)|"),metric("État intriqué ?","Oui" if entangled else "Non","Pour Werner : v>1/3 ; mélange classique : jamais"),metric("Probabilité locale A+",probabilities[0]+probabilities[1],"1/2, quel que soit le choix de B")],
        charts=[chart("Quatre issues jointes","Issue (++,+−,−+,−−)","Probabilité",[series("Issues",[0,1,2,3],probabilities,"green","bars")]),chart("Corrélation quand B tourne","Angle b · degrés","E(a,b)",[series(name,scan,curve),series("Mélange classique",scan,visibility*math.cos(2*a)*np.cos(2*np.radians(scan)),"gold")]),chart("Intrication et violation CHSH : deux seuils","Visibilité v","CHSH maximal",[series("Werner",vis,2*math.sqrt(2)*vis),series("Borne locale",vis,np.full_like(vis,2),"rose"),series("Seuil d'intrication",[1/3,1/3],[0,2.85],"mint")])],
        table=table(["Objet","Valeur"],[["ρ",matrix_text(rho)],["État local TrB ρ",matrix_text(partial_trace_b(rho))],["Corrélations (ab,ab′,a′b,a′b′)",str([round(e,6) for e in Es])],["Plus petite valeur propre de ρᵀᴮ",float(pteig[0])],["CHSH maximal de cet état",optimal],["Seuil Werner d'intrication",1/3],["Seuil Werner de violation CHSH",1/math.sqrt(2)]]),
        notes=["Werner : ρ=v|Φ⁺⟩⟨Φ⁺|+(1−v)I₄/4, avec |Φ⁺⟩=(|00⟩+|11⟩)/√2. Les analyseurs linéaires mesurent M(a)=cos(2a)σz+sin(2a)σx. On obtient E=v cos 2(a−b).", "Le mélange classique vaut v(|00⟩⟨00|+|11⟩⟨11|)/2+(1−v)I₄/4. Il possède des corrélations, mais reste séparable ; sa corrélation est v cos(2a)cos(2b).", "Pour Werner, l'intrication commence à v>1/3 tandis que la violation CHSH exige v>1/√2 avec des angles optimaux. L'absence de violation de cette inégalité ne prouve donc pas la séparabilité.","Les probabilités locales restent 1/2 et indépendantes de l'analyseur éloigné. Les corrélations sont accessibles en comparant les mesures ; elles ne transmettent pas une information contrôlable instantanément."],
        theory=dict(state=state,visibility=visibility,probabilities=probabilities.tolist(),correlations=Es,CHSH=S,CHSH_max=optimal,entangled=entangled,partial_transpose_eigenvalues=pteig.tolist(),local_A=partial_trace_b(rho).real.tolist()))


def squid_critical(I1,I2,flux):
    """I₁,I₂ dans la même unité ; flux en quanta h/(2e), inductance nulle."""
    return np.sqrt((I1-I2)**2+4*I1*I2*np.cos(math.pi*np.asarray(flux))**2)


def josephson(d):
    mode=choice(d,"mode","squid",["squid","jonction"])
    I1=number(d,"I1",10,.1,30);I2v=number(d,"I2",10,.1,30)
    flux=number(d,"flux",0,-2,2);voltage=number(d,"voltage_uV",1,0,10)
    phase=math.radians(number(d,"phase",0,-180,180))
    f=2*E_CHARGE*voltage*1e-6/H
    phases=np.linspace(-math.pi,math.pi,250);phis=np.linspace(-2,2,350)
    critical=float(squid_critical(I1,I2v,flux))
    combined=I1*np.sin(phases+math.pi*flux)+I2v*np.sin(phases-math.pi*flux)
    ns=np.linspace(0,10 if f==0 else min(30,3/f*1e9),400)
    current=I1*np.sin(phase+2*math.pi*f*ns*1e-9)
    now=I1*math.sin(phase+math.pi*flux)+I2v*math.sin(phase-math.pi*flux)
    if mode=="squid":
        metrics=[metric("Courant critique SQUID · µA",critical,"Deux jonctions, inductance de boucle négligeable"),metric("Courant à la phase choisie · µA",now,"I₁sin(δ+πΦ/Φ₀)+I₂sin(δ−πΦ/Φ₀)"),metric("Quantum de flux · Wb",PHI0,"Φ₀=h/(2e), exact avec le SI")]
        charts=[chart("Interférence dans le SQUID","Φ/Φ₀","Icrit · µA",[series("Courant critique",phis,squid_critical(I1,I2v,phis),"gold"),series("Flux choisi",[flux],[critical],"rose","dots")]),chart("Addition de deux courants de phase","Phase moyenne δ · degrés","I · µA",[series("Jonction 1",np.degrees(phases),I1*np.sin(phases+math.pi*flux),"mint"),series("Jonction 2",np.degrees(phases),I2v*np.sin(phases-math.pi*flux),"rose"),series("Somme",np.degrees(phases),combined)])]
        rows=[["Quantum de flux · Wb",PHI0],["Courant à la phase choisie · µA",now],["Extinction parfaite à demi-flux ?","Oui si I₁=I₂"],["Minimum critique sur le flux · µA",abs(I1-I2v)]]
    else:
        metrics=[metric("Fréquence Josephson · MHz",f/1e6,"fJ=2eV/h ; zéro si V=0"),metric("Courant critique individuel · µA",I1,"I=I₁ sin δ"),metric("Charge d'une paire · C",2*E_CHARGE,"Deux électrons : q=2e")]
        charts=[chart("Courant d'une jonction sous tension constante","Temps · ns","I · µA",[series("I=I₁ sin δ(t)",ns,current)]),chart("Relation courant-phase d'une jonction","Phase δ · degrés","I · µA",[series("I=I₁ sin δ",np.degrees(phases),I1*np.sin(phases)),series("Phase initiale",[math.degrees(phase)],[I1*math.sin(phase)],"rose","dots")])]
        rows=[["Tension · µV",voltage],["Constante Josephson · Hz/V",2*E_CHARGE/H],["Courant initial · µA",I1*math.sin(phase)],["Fréquence · Hz",f],["Charge d'une paire de Cooper · C",2*E_CHARGE]]
    return dict(metrics=metrics,charts=charts,
        table=table(["Grandeur","Valeur"],rows),
        notes=["Relations idéales de Josephson : I=Icrit sin δ et δ̇=2eV/ℏ. Sous tension constante, la fréquence du courant est 2eV/h ; à V=0, la phase reste fixe et un courant continu peut circuler.","SQUID à deux jonctions : δ₁−δ₂=2πΦ/Φ₀ et I=I₁sin δ₁+I₂sin δ₂. Maximiser sur la phase moyenne donne Icrit(Φ)=√(I₁²+I₂²+2I₁I₂cos(2πΦ/Φ₀)).","Pour des jonctions égales, Icrit(Φ)=2I₁|cos(πΦ/Φ₀)|. Le facteur 2 correspond à deux courants critiques individuels. Une asymétrie laisse un minimum |I₁−I₂|.","Modèle à phases imposées, relation courant-phase sinusoïdale, inductance de boucle et dissipation négligées. Le courant sous tension tracé est celui d'une jonction seule ; le SQUID tracé est sa caractéristique critique en régime statique."],
        theory=dict(josephson_frequency_Hz=f,flux_quantum=PHI0,squid_critical_uA=critical,squid_current_uA=now,minimum_critical_uA=abs(I1-I2v)))


def rotation_unitary(axis,angle):
    axis=np.asarray(axis,dtype=float);norm=float(np.linalg.norm(axis))
    if norm==0:return I2.copy()
    axis=axis/norm
    generator=sum(v*p for v,p in zip(axis,PAULI))
    return math.cos(angle/2)*I2-1j*math.sin(angle/2)*generator


def bloch_vector(rho):
    return np.array([np.trace(np.asarray(rho)@p).real for p in PAULI])


def bloch_density(vector):
    vector=np.asarray(vector,dtype=float)
    if np.linalg.norm(vector)>1+1e-12:raise ValueError("Le vecteur de Bloch doit avoir une norme ≤1.")
    return (I2+sum(v*p for v,p in zip(vector,PAULI)))/2


def projection3(points):
    return np.asarray(points)@np.array([[1,0],[.32,.26],[0,1]])


def bloch_background():
    curves=[]
    t=np.linspace(0,2*math.pi,160)
    for z in [-.75,-.4,0,.4,.75]:
        r=math.sqrt(1-z*z);p=projection3(np.column_stack([r*np.cos(t),r*np.sin(t),np.full_like(t,z)]))
        curves.append(series("Sphère unité · projection",p[:,0],p[:,1],"mint"))
    for angle in np.linspace(0,math.pi,6,endpoint=False):
        p=projection3(np.column_stack([np.cos(angle)*np.sin(t),np.sin(angle)*np.sin(t),np.cos(t)]))
        curves.append(series("Sphère unité · projection",p[:,0],p[:,1],"mint"))
    return curves


def bloch_scene(paths=(), vectors=()):
    """Données tridimensionnelles pour une rotation interactive du dessin."""
    t=np.linspace(0,2*math.pi,100)
    sphere=[]
    for z in [-.75,-.4,0,.4,.75]:
        r=math.sqrt(1-z*z)
        sphere.append(dict(label="Sphère unité",points=np.column_stack([r*np.cos(t),r*np.sin(t),np.full_like(t,z)]).tolist(),color="mint"))
    for angle in np.linspace(0,math.pi,6,endpoint=False):
        sphere.append(dict(label="Sphère unité",points=np.column_stack([np.cos(angle)*np.sin(t),np.sin(angle)*np.sin(t),np.cos(t)]).tolist(),color="mint"))
    return dict(radius=1,paths=sphere+list(paths),vectors=list(vectors))


def rabi_unitary(omega,detuning,time):
    frequency=math.hypot(omega,detuning)
    return rotation_unitary([omega,0,detuning],frequency*time) if frequency else I2.copy()


def rabi_probability(omega,detuning,time):
    frequency=math.hypot(omega,detuning)
    return 0.0 if frequency==0 else (omega/frequency)**2*np.sin(frequency*np.asarray(time)/2)**2


def rabi(d):
    omega=number(d,"omega",1,.1,4);detuning=number(d,"detuning",0,-4,4);time=number(d,"time",math.pi,0,15)
    B0=number(d,"B0",1,.1,7);B1=number(d,"B1_uT",10,1,100)
    eff=math.hypot(omega,detuning)
    ts=np.linspace(0,15,400);vectors=[]
    for t in ts:
        psi=rabi_unitary(omega,detuning,t)@np.array([1,0],dtype=complex)
        vectors.append(bloch_vector(np.outer(psi,psi.conj())))
    vectors=np.array(vectors);psi=rabi_unitary(omega,detuning,time)@np.array([1,0],dtype=complex)
    vec=bloch_vector(np.outer(psi,psi.conj()));p=projection3(vectors);point=projection3([vec])[0]
    graphics=bloch_background()+[series("Précession dans le repère tournant",p[:,0],p[:,1]),series("Au temps choisi",[0,point[0]],[0,point[1]],"rose")]
    sphere_chart=chart("Sphère de Bloch · projection 3D","rₓ+0,32rᵧ","r_z+0,26rᵧ",graphics,equal=True)
    sphere_chart["sceneBloch"]=bloch_scene(
        paths=[dict(label="Précession",points=vectors.tolist(),color="green")],
        vectors=[dict(label="État initial",point=[0,0,1],color="gold"),dict(label="Au temps choisi",point=vec.tolist(),color="rose"),dict(label="Axe effectif",point=[omega/eff,0,detuning/eff],color="green")])
    proton_larmor=GAMMA_PROTON*B0/(2*math.pi)
    proton_rabi=GAMMA_PROTON*B1*1e-6
    return dict(metrics=[metric("Probabilité |−⟩",rabi_probability(omega,detuning,time),"État initial |+⟩ ; repère tournant"),metric("Pulsation effective Ωeff",eff,"√(Ω²+Δ²)"),metric("Période de retournement résonant",math.pi/omega,"Durée d'une impulsion π lorsque Δ=0")],
        charts=[chart("Oscillations de Rabi","Temps réduit","P(|−⟩)",[series("Avec désaccord Δ",ts,rabi_probability(omega,detuning,ts)),series("Résonance Δ=0",ts,rabi_probability(omega,0,ts),"gold"),series("Point choisi",[time],[rabi_probability(omega,detuning,time)],"rose","dots")]),sphere_chart,chart("Composantes de Bloch dans le repère tournant","Temps réduit","Composante",[series("rₓ",ts,vectors[:,0]),series("rᵧ",ts,vectors[:,1],"rose"),series("r_z",ts,vectors[:,2],"gold")])],
        table=table(["Grandeur","Valeur"],[["Hrot/ℏ",matrix_text((detuning*SZ+omega*SX)/2)],["Vecteur de Bloch",str(vec.tolist())],["Amplitude maximale de transition",(omega/eff)**2],["RMN proton libre : fL · MHz",proton_larmor/1e6],["Champ B₁ circulaire : Ω/2π · kHz",proton_rabi/(2*math.pi*1e3)],["RMN : durée π · µs",math.pi/proton_rabi*1e6],["RMN : durée π/2 · µs",math.pi/(2*proton_rabi)*1e6]]),
        notes=["Hamiltonien dans le repère tournant : Hrot=(ℏ/2)(Δσz+Ωσx), avec Δ défini ici comme le coefficient de σz. U(t)=cos(Ωeff t/2)I−i sin(Ωeff t/2)(Δσz+Ωσx)/Ωeff.","P(|−⟩)=Ω²/(Ω²+Δ²) sin²(√(Ω²+Δ²)t/2). À résonance, une impulsion π retourne le spin et une impulsion π/2 crée une superposition équiprobable. Le désaccord diminue le transfert maximal.","Les courbes emploient Ω, Δ et t dans un même système d'unités réduites. Les valeurs RMN du tableau sont un exemple SI distinct : proton libre, fL=γpB₀/(2π), Ω=γpB₁ pour un champ transverse circulaire.","Pour un champ transverse linéaire d'amplitude B₁, sa composante corotative a une amplitude B₁/2 : sous approximation de l'onde tournante, Ω=γpB₁/2. Relaxation, inhomogénéité et couplages entre spins sont absents ici.","Le Hamiltonien initial de l'exercice doit avoir deux énergies distinctes : un terme proportionnel à l'identité seul n'engendre aucun désaccord. Le modèle utilise les matrices de Pauli et un coefficient 1/2 explicites."],
        theory=dict(probability=float(rabi_probability(omega,detuning,time)),effective_frequency=eff,maximum_probability=(omega/eff)**2,bloch=vec.tolist(),pi_time=math.pi/omega,pi_half_time=math.pi/(2*omega),RMN_larmor_Hz=proton_larmor,RMN_rabi_rad_s=proton_rabi,RMN_pi_s=math.pi/proton_rabi))


def spherical_unit(theta,phi):
    return np.array([math.sin(theta)*math.cos(phi),math.sin(theta)*math.sin(phi),math.cos(theta)])


def bloch(d):
    theta=math.radians(number(d,"theta",60,0,180));phi=math.radians(number(d,"phi",30,-180,180))
    length=number(d,"purity",1,0,1)
    gate=choice(d,"gate","identite",["identite","H","X","Rx","Ry","Rz"])
    angle=math.radians(number(d,"angle",90,-360,360))
    at=math.radians(number(d,"axis_theta",0,0,180));ap=math.radians(number(d,"axis_phi",0,-180,180))
    initial=length*spherical_unit(theta,phi);rho=bloch_density(initial)
    if gate=="identite":U=I2
    elif gate=="H":U=HADAMARD
    elif gate=="X":U=SX
    else:U=rotation_unitary({"Rx":[1,0,0],"Ry":[0,1,0],"Rz":[0,0,1]}[gate],angle)
    finalrho=U@rho@U.conj().T;final=bloch_vector(finalrho)
    measurement=spherical_unit(at,ap);prob=(1+float(final@measurement))/2
    purity=(1+length*length)/2
    graphics=bloch_background();start=projection3([initial])[0];end=projection3([final])[0]
    graphics += [series("État initial",[0,start[0]],[0,start[1]],"gold"),series("Après la porte",[0,end[0]],[0,end[1]],"rose")]
    path3=[]
    if gate in ["Rx","Ry","Rz"]:
        axis={"Rx":[1,0,0],"Ry":[0,1,0],"Rz":[0,0,1]}[gate]
        path=[bloch_vector((v:=rotation_unitary(axis,s))@rho@v.conj().T) for s in np.linspace(0,angle,120)]
        p=projection3(path);graphics.append(series("Rotation unitaire",p[:,0],p[:,1]))
        path3=[dict(label="Rotation unitaire",points=np.asarray(path).tolist(),color="green")]
    sphere_chart=chart("Sphère de Bloch · projection 3D","rₓ+0,32rᵧ","r_z+0,26rᵧ",graphics,equal=True)
    sphere_chart["sceneBloch"]=bloch_scene(paths=path3,vectors=[dict(label="État initial",point=initial.tolist(),color="gold"),dict(label="Après la porte",point=final.tolist(),color="rose"),dict(label="Axe de mesure",point=measurement.tolist(),color="green")])
    azimuth=np.linspace(-180,180,240)
    probabilities=[(1+final@spherical_unit(at,math.radians(q)))/2 for q in azimuth]
    return dict(metrics=[metric("Pureté Tr(ρ²)",purity,"(1+r²)/2 ; r est la longueur de Bloch"),metric("P(+ selon l'axe choisi)",prob,"(1+r⃗·n⃗)/2 après la porte"),metric("Longueur du vecteur de Bloch",float(np.linalg.norm(final)),"Conservée par toute porte unitaire")],
        charts=[sphere_chart,chart("Probabilités dans la base |0⟩, |1⟩","Issue (0,1)","Probabilité",[series("Mesure Z",[0,1],[(1+final[2])/2,(1-final[2])/2],"green","bars")]),chart("Tourner l'axe de mesure à polarité fixée","Azimut de l'axe · degrés","P(+)",[series("Mesure d'un même état",azimuth,probabilities)])],
        table=table(["Objet","Valeur"],[["ρ initial",matrix_text(rho)],["Porte U",matrix_text(U)],["ρ final",matrix_text(finalrho)],["Vecteur initial",str(initial.tolist())],["Vecteur final",str(final.tolist())],["Valeurs propres de ρ",str(np.linalg.eigvalsh(finalrho).tolist())]]),
        notes=["Pour un état pur, |ψ⟩=cos(θ/2)|0⟩+e^{iφ}sin(θ/2)|1⟩. Sa direction de Bloch est (sinθ cosφ, sinθ sinφ, cosθ). Une phase globale ne change pas cette direction.","Le curseur de longueur r construit ρ=(I+r⃗·σ⃗)/2. Les états purs sont sur la sphère (r=1), les mélanges à l'intérieur. La pureté physique vaut Trρ²=(1+r²)/2, pas r.","Rx, Ry et Rz sont définies par exp(−i angle σ/2). Hadamard échange x et z et change le signe de y ; X retourne y et z. Les portes unitaires conservent la pureté.","Mesurer σ⃗·n⃗ donne les probabilités (1±r⃗·n⃗)/2. Une mesure produit une issue classique ; le tracé compare des ensembles de préparations identiques. La sphère est dessinée en projection, ses coordonnées exportées restent tridimensionnelles."],
        theory=dict(initial=initial.tolist(),final=final.tolist(),length=length,purity=purity,measurement_axis=measurement.tolist(),probability_plus=prob,probability_zero=(1+final[2])/2))


def bell_circuit_states():
    """Ordre de base |q₀q₁⟩ ; CNOT contrôle q₀, cible q₁."""
    initial=np.array([1,0,0,0],dtype=complex)
    after_h=np.kron(HADAMARD,I2)@initial
    cnot=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=complex)
    return [initial,after_h,cnot@after_h]


def grover_states(marked,iterations):
    if marked not in range(4) or iterations not in range(5):raise ValueError("Indice marqué 0..3 et itérations 0..4 requis.")
    uniform=np.ones(4,dtype=complex)/2
    oracle=np.eye(4,dtype=complex);oracle[marked,marked]=-1
    diffusion_op=2*np.outer(uniform,uniform.conj())-np.eye(4)
    states=[uniform]
    for _ in range(iterations):states.append(diffusion_op@oracle@states[-1])
    return states


def circuits(d):
    mode=choice(d,"mode","bell",["bell","grover"])
    marked=number(d,"marked",3,0,3,True);iterations=number(d,"iterations",1,0,4,True)
    states=bell_circuit_states() if mode=="bell" else grover_states(marked,iterations)
    final=states[-1];prob=abs(final)**2;rho=np.outer(final,final.conj())
    local=partial_trace_b(rho);local_purity=float(np.trace(local@local).real)
    steps=list(range(len(states)))
    curves=[series(f"|{j:02b}⟩",steps,[float(abs(s[j])**2) for s in states],color,"step") for j,color in enumerate(["green","mint","rose","gold"])]
    if mode=="grover":
        analytic=[math.sin((2*k+1)*math.pi/6)**2 for k in steps]
        note="Grover sur quatre éléments : une itération donne une réussite certaine dans ce modèle idéal. Répéter aveuglément peut la réduire."
        target=float(prob[marked]);target_label=f"P de l'état marqué |{marked:02b}⟩"
    else:
        analytic=[];target=float(prob[0]+prob[3]);target_label="P d'issues identiques"
        note="Le circuit H sur q₀, puis CNOT(q₀→q₁), transforme |00⟩ en (|00⟩+|11⟩)/√2. Les états locaux sont mélangés, tandis que l'état de la paire est pur."
    return dict(metrics=[metric(target_label,target,"Calcul des amplitudes, puis règle de Born"),metric("Norme de l'état final",float(np.vdot(final,final).real),"Portes unitaires, aucune renormalisation ajoutée"),metric("Pureté locale de q₀",local_purity,"Un état global pur peut avoir un état local mélangé")],
        charts=[chart("Probabilités de mesure finales","Issue |00⟩,|01⟩,|10⟩,|11⟩","Probabilité",[series("Règle de Born",range(4),prob,"green","bars")]),chart("Suivre chaque étape du circuit","Étape" if mode=="bell" else "Itération de Grover","Probabilité",curves),chart("Les amplitudes gardent leur phase","Indice de base","Amplitude",[series("Partie réelle",range(4),final.real,"green","stems"),series("Partie imaginaire",range(4),final.imag,"rose","dots")])],
        table=table(["Étape","Amplitude |00⟩","Amplitude |01⟩","Amplitude |10⟩","Amplitude |11⟩"],[[str(k)]+[complex_text(v) for v in state] for k,state in enumerate(states)]),
        notes=[note,"L'ordre de la base est |q₀q₁⟩. L'état est un vecteur de quatre amplitudes complexes ; une porte à deux qubits est une matrice 4×4. On ne calcule les probabilités qu'après les additions d'amplitudes.","L'oracle de Grover change le signe de l'amplitude de la cible sans la mesurer. La diffusion 2|s⟩⟨s|−I réalise une réflexion autour de l'état uniforme ; les deux réflexions amplifient par interférence.","L'oracle suppose une fonction de recherche donnée. La simulation de quatre éléments illustre le mécanisme ; elle n'établit aucun avantage pratique sur un calcul classique de cette taille. Les dispositifs physiques, le bruit et la correction d'erreurs demandent des modèles supplémentaires."],
        theory=dict(mode=mode,marked=marked,probabilities=prob.tolist(),amplitudes=[[float(v.real),float(v.imag)] for v in final],normalization=float(np.vdot(final,final).real),local_purity=local_purity,grover_analytic_probabilities=analytic,stages=[[[float(v.real),float(v.imag)] for v in s] for s in states]))


LABS={"boite":boite,"heisenberg":heisenberg,"diffusion":diffusion,"oscillateur":oscillateur,
      "intrication":intrication,"josephson":josephson,"rabi":rabi,"bloch":bloch,"circuits":circuits}


def calculate(data):
    if not isinstance(data,dict):raise ValueError("Un objet de paramètres est attendu.")
    lab=choice(data,"lab","boite",LABS)
    result=LABS[lab](data)
    result["lab"]=lab
    result["parameters"]={k:v for k,v in data.items() if k!="lab"}
    return result
