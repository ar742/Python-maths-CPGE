"""Physique statistique CPGE : huit laboratoires, NumPy seul.

Les formules exactes, les sommes tronquées et les approximations classiques
sont identifiées séparément. Les constantes physiques sont CODATA 2022.
"""
from __future__ import annotations
import math
import numpy as np

H = 6.62607015e-34
HBAR = H / (2 * math.pi)
KB = 1.380649e-23
E_CHARGE = 1.602176634e-19
C_LIGHT = 299792458.0
M_E = 9.1093837139e-31
MU_B = 9.2740100657e-24
N_A = 6.02214076e23
M_U = 1.66053906892e-27
ZETA_3_2 = 2.612375348685488
SIGMA = 2 * math.pi**5 * KB**4 / (15 * H**3 * C_LIGHT**2)


def number(data, key, default, lo, hi, integer=False):
    value = data.get(key, default)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} doit être un nombre fini.")
    if not lo <= value <= hi or (integer and int(value) != value):
        raise ValueError(f"{key} doit être entre {lo} et {hi}" + (" et entier." if integer else "."))
    return int(value) if integer else float(value)


def choice(data, key, default, choices):
    value = data.get(key, default)
    if not isinstance(value, str) or value not in choices:
        raise ValueError(f"{key} doit être parmi : {', '.join(choices)}.")
    return value


def series(label, x, y, color="green", kind="line"):
    return dict(label=label, x=np.asarray(x).tolist(), y=np.asarray(y).tolist(), color=color, kind=kind)


def chart(title, xlabel, ylabel, data, logx=False, logy=False, equal=False):
    return dict(title=title, xlabel=xlabel, ylabel=ylabel, series=data, logx=logx, logy=logy, equal=equal)


def metric(label, value, note=""):
    return dict(label=label, value=value if isinstance(value, str) else float(value), note=note)


def table(headers, rows):
    return dict(headers=headers, rows=rows)


def canonical_levels(x, degeneracy=3):
    """Niveaux 0, ε, 2ε ; x=ε/(kBT)>0, dégénérescences 1,g,1."""
    if not math.isfinite(x) or x <= 0 or not isinstance(degeneracy, int) or degeneracy < 1:
        raise ValueError("x>0 et dégénérescence entière positive requis.")
    levels = np.array([0., 1., 2.])
    degeneracies = np.array([1., float(degeneracy), 1.])
    logs = np.log(degeneracies) - x * levels
    shift = float(logs.max())
    weights = np.exp(logs - shift)
    probabilities = weights / weights.sum()
    logz = shift + math.log(float(weights.sum()))
    mean = float(probabilities @ levels)
    variance = float(probabilities @ ((levels - mean)**2))
    entropy = sum(-p * math.log(p / g) for p, g in zip(probabilities, degeneracies) if p > 0)
    return dict(probabilities=probabilities, log_partition=logz, energy_ratio=mean,
                heat_capacity=x*x*variance, entropy=float(entropy), variance=variance)


def two_level_statistics(x):
    """Un site localisé, niveaux 0 et ε, x=ε/kBT>0 ; C et S en kB."""
    if not math.isfinite(x) or x <= 0:
        raise ValueError("x doit être positif.")
    z = math.exp(-x)
    p = z/(1+z)
    logz = math.log1p(z)
    return dict(probabilities=np.array([1-p, p]), energy_ratio=p,
                heat_capacity=x*x*z/(1+z)**2, entropy=logz+x*p,
                log_partition=logz, variance=p*(1-p))


def microcanonical_two_level(particles, excited):
    """Ω=C(N,k), N sites distinguables fixé ; aucune dérivée en N/μ."""
    if isinstance(particles, bool) or isinstance(excited, bool) or not isinstance(particles, int) or not isinstance(excited, int) or particles < 1 or not 0 <= excited <= particles:
        raise ValueError("N entier positif et 0≤k≤N entier requis.")
    n, k = particles, excited
    p = k/n
    exact = math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
    leading = -n*(p*math.log(p)+(1-p)*math.log1p(-p)) if 0 < k < n else 0.
    # Stirling raffiné est inapplicable à un bord : exporter None, pas ±∞.
    refined = leading-.5*math.log(2*math.pi*n*p*(1-p)) if 0 < k < n else None
    beta_epsilon = math.log((n-k)/k) if 0 < k < n else None
    return dict(particles=n, excited=k, fraction=p, entropy=exact,
                stirling_leading=leading, stirling_refined=refined,
                beta_epsilon_stirling=beta_epsilon)


def cube_statistics(x, cutoff):
    """Partition d'une particule : E/E_L=n₁²+n₂²+n₃², 1≤nᵢ≤cutoff.

    x=E_L/(kBT). Le décalage n²−1 protège la somme à basse température.
    L'entropie calculée est celle de cette distribution tronquée normalisée.
    """
    if not math.isfinite(x) or x <= 0 or not isinstance(cutoff, int) or cutoff < 1:
        raise ValueError("x>0 et coupure entière positive requis.")
    n = np.arange(1, cutoff + 1, dtype=float)
    squares = n*n
    weights = np.exp(-x*(squares-1))
    p = weights / weights.sum()
    mean = float(p @ squares)
    variance = float(p @ ((squares-mean)**2))
    logz1 = -x + math.log(float(weights.sum()))
    entropy1 = sum(-v*math.log(v) for v in p if v > 0)
    return dict(log_partition=3*logz1, energy_ratio=3*mean, heat_capacity=3*x*x*variance,
                entropy=3*entropy1, probabilities=p)


def oscillator_statistics(x):
    """x=hν/(kBT)>0 ; énergie exprimée en hν, C et S en kB."""
    if not math.isfinite(x) or x <= 0:
        raise ValueError("x doit être strictement positif.")
    z = math.exp(-x)
    one_minus_z = -math.expm1(-x)
    mean_n = z/one_minus_z
    capacity = (x/one_minus_z)**2*z
    entropy = x*mean_n-math.log(one_minus_z)
    return dict(mean_occupation=mean_n, energy_ratio=.5+mean_n, heat_capacity=capacity,
                entropy=entropy, log_partition=-x/2-math.log(one_minus_z))


def spin_statistics(x):
    """x=μB/(kBT), énergies −μB,+μB ; spins indépendants, spin 1/2."""
    if not math.isfinite(x):
        raise ValueError("x doit être fini.")
    a = abs(x)
    tail = math.exp(-2*a)
    polarization = math.tanh(x)
    sech2 = 4*tail/(1+tail)**2
    entropy = math.log1p(tail)+2*a*tail/(1+tail)
    return dict(polarization=polarization, probability_aligned=(1+polarization)/2,
                heat_capacity=x*x*sech2, entropy=entropy,
                log_partition=a+math.log1p(tail), susceptibility_ratio=sech2)


def occupation(energy_ratio, mu_ratio, statistics):
    """Occupation moyenne d'un seul état ; énergie et μ divisés par kBT."""
    x = np.asarray(energy_ratio, dtype=float)
    if not np.all(np.isfinite(x)) or not math.isfinite(mu_ratio):
        raise ValueError("Énergies et potentiel chimique finis requis.")
    y = x-mu_ratio
    if statistics == "BE":
        if np.any(y <= 0):
            raise ValueError("Bose–Einstein exige μ inférieur à chaque énergie considérée.")
        result = np.exp(-y)/(-np.expm1(-y))
    elif statistics == "FD":
        z = np.exp(-np.abs(y))
        result = np.where(y >= 0, z/(1+z), 1/(1+z))
    elif statistics == "MB":
        if np.any(-y > 700):
            raise ValueError("Occupation MB hors de la plage numérique finie.")
        result = np.exp(-y)
    else:
        raise ValueError("Statistique inconnue : BE, FD ou MB attendue.")
    return float(result) if result.ndim == 0 else result


def thermal_wavelength(temperature, mass):
    if not math.isfinite(temperature) or not math.isfinite(mass) or temperature <= 0 or mass <= 0:
        raise ValueError("T et m doivent être positifs et finis.")
    return H/math.sqrt(2*math.pi*mass*KB*temperature)


def fermi_temperature(density, mass=M_E, degeneracy=2):
    """Gaz idéal homogène 3D : EF=ℏ²(6π²n/g)^(2/3)/(2m)."""
    if not math.isfinite(density) or density <= 0 or not math.isfinite(mass) or mass <= 0 or degeneracy <= 0:
        raise ValueError("Densité, masse et dégénérescence positives requises.")
    return HBAR**2/(2*mass*KB)*(6*math.pi**2*density/degeneracy)**(2/3)


def bose_temperature(density, mass):
    """Une seule composante bosonique, gaz idéal homogène 3D ; g=1."""
    if not math.isfinite(density) or density <= 0 or not math.isfinite(mass) or mass <= 0:
        raise ValueError("Densité et masse positives requises.")
    return 2*math.pi*HBAR**2/(mass*KB)*(density/ZETA_3_2)**(2/3)


_QUAD_X, _QUAD_W = np.polynomial.legendre.leggauss(64)


def _integrate_segments(function, points):
    """Gauss 64 points par intervalle ; pas de SciPy ni somme de niveaux."""
    result = 0.
    points = sorted(set(float(p) for p in points))
    for low, high in zip(points[:-1], points[1:]):
        if high > low:
            xx = (high-low)*(_QUAD_X+1)/2+low
            result += (high-low)/2*float(_QUAD_W @ function(xx))
    return result


def fermi_integrals(theta, mu_ef):
    """N/Nc et U/(Nc EF), Nc fixé par EF ; θ=kBT/EF>0.

    Variable q=p/pF ; scinder autour du bord de Fermi résout θ≪1.
    La queue E−μ>40kBT est omise (diagnostic numérique, pas exact).
    """
    if not math.isfinite(theta) or theta <= 0 or not math.isfinite(mu_ef):
        raise ValueError("θ>0 et μ/EF fini requis.")
    top = math.sqrt(max(0.,mu_ef)+40*theta)
    points = [0.,top]
    points += [math.sqrt(v) for v in [mu_ef+a*theta for a in (-20,-8,0,8,20)] if 0 < v < top*top]
    number_integral = _integrate_segments(lambda q:3*q*q*occupation(q*q/theta,mu_ef/theta,"FD"),points)
    energy_integral = _integrate_segments(lambda q:3*q**4*occupation(q*q/theta,mu_ef/theta,"FD"),points)
    return number_integral, energy_integral


def fermi_gas_state(theta):
    """Résoudre le nombre à n fixé ; μ et énergie en unités de EF."""
    if not math.isfinite(theta) or theta <= 0:
        raise ValueError("T/TF doit être positif.")
    low, high = -100*theta, max(2.,40*theta)
    for _ in range(72):
        middle = (low+high)/2
        density_ratio, _ = fermi_integrals(theta,middle)
        if density_ratio < 1:
            low = middle
        else:
            high = middle
    mu = (low+high)/2
    density_ratio, energy = fermi_integrals(theta,mu)
    return dict(mu_ef=mu, energy_ef=energy, density_ratio=density_ratio,
                number_residual=density_ratio-1)


def bose_number_function(mu_ratio):
    """g₃/₂(e^η), η=μ/kBT≤0 ; g(1)=ζ(3/2) explicitement.

    Variable q=√(E/kBT), avec sous-intervalles près de √(−η).
    Queue q²−η>40 omise ; intégrale numérique hors η=0.
    """
    if not math.isfinite(mu_ratio) or mu_ratio > 0:
        raise ValueError("Les bosons homogènes exigent μ≤0.")
    if mu_ratio == 0:
        return ZETA_3_2
    a = math.sqrt(-mu_ratio)
    top = math.sqrt(40.)
    points = [0.,top]+[v for v in [a,5*a,.02,.1,.5,1.,2.,4.] if 0 < v < top]
    # Relier l'échelle √(−η) à l'échelle thermique par pas géométriques.
    # Un unique intervalle [5√(−η),.02] manquerait le bord pour |η|≪1.
    bridge = a
    while 0 < bridge < .02:
        points.append(bridge)
        bridge *= 5
    return 4/math.sqrt(math.pi)*_integrate_segments(lambda q:q*q*occupation(q*q,mu_ratio,"BE"),points)


def bose_gas_state(theta):
    """Gaz homogène à nombre fixé, θ=T/Tc ; condensat séparé."""
    if not math.isfinite(theta) or theta <= 0:
        raise ValueError("T/Tc doit être positif.")
    if theta <= 1:
        return dict(mu_ratio=0.,condensate_fraction=1-theta**1.5,
                    thermal_fraction=theta**1.5,number_residual=0.)
    target = ZETA_3_2/theta**1.5
    # Bissection de α=√(−μ/kBT), mieux conditionnée près de Tc que η.
    low, high = 0.,10.
    for _ in range(76):
        middle = (low+high)/2
        if bose_number_function(-middle*middle) < target:
            high = middle
        else:
            low = middle
    mu = -((low+high)/2)**2
    residual = bose_number_function(mu)/target-1
    return dict(mu_ratio=mu,condensate_fraction=0.,thermal_fraction=1.,number_residual=residual)


def maxwell_statistics(temperature, mass, density):
    """Gaz classique dilué, isotrope, en équilibre ; masse par molécule."""
    if any(not math.isfinite(v) or v <= 0 for v in [temperature,mass,density]):
        raise ValueError("Température, masse et densité positives requises.")
    sigma = math.sqrt(KB*temperature/mass)
    return dict(sigma=sigma,most_probable=math.sqrt(2)*sigma,
                mean_speed=math.sqrt(8/math.pi)*sigma,rms_speed=math.sqrt(3)*sigma,
                pressure=density*KB*temperature,incident_flux=density*sigma/math.sqrt(2*math.pi))


def maxwell_speed_density(speed, temperature, mass, effusive=False):
    values = np.asarray(speed,dtype=float)
    if np.any(values < 0) or not np.all(np.isfinite(values)):
        raise ValueError("Les vitesses doivent être positives et finies.")
    sigma = maxwell_statistics(temperature,mass,1.)["sigma"]
    pdf = math.sqrt(2/math.pi)*values**2/sigma**3*np.exp(-values**2/(2*sigma**2))
    if effusive:
        pdf *= values/(math.sqrt(8/math.pi)*sigma)
    return float(pdf) if pdf.ndim == 0 else pdf


def porous_fractions(time, rate1, rate2, fraction_initial):
    """N₁/Ntotal avec T₁,T₂ fixes ; petits trous en régime moléculaire."""
    values = np.asarray(time,dtype=float)
    if np.any(values < 0) or not np.all(np.isfinite(values)) or any(not math.isfinite(v) or v <= 0 for v in [rate1,rate2]) or not 0 <= fraction_initial <= 1:
        raise ValueError("Temps ≥0, taux positifs, fraction entre 0 et 1 requis.")
    equilibrium = rate2/(rate1+rate2)
    first = equilibrium+(fraction_initial-equilibrium)*np.exp(-(rate1+rate2)*values)
    return first,1-first


def planck_radiance(wavelength_m, temperature):
    """Luminance spectrale Bλ, par mètre de longueur d'onde, W m⁻³ sr⁻¹."""
    wavelength = np.asarray(wavelength_m, dtype=float)
    if not math.isfinite(temperature) or temperature <= 0 or np.any(wavelength <= 0) or not np.all(np.isfinite(wavelength)):
        raise ValueError("Température et longueurs d'onde strictement positives requises.")
    x = H*C_LIGHT/(wavelength*KB*temperature)
    factor = np.exp(-x)/(-np.expm1(-x))
    result = 2*H*C_LIGHT**2/wavelength**5*factor
    return float(result) if result.ndim == 0 else result


def wien_root():
    """Racine non nulle de 5(1−e⁻ˣ)=x par bissection, sans constante ajustée."""
    lo, hi = 4., 6.
    for _ in range(60):
        mid = (lo+hi)/2
        if 5*(-math.expm1(-mid))-mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


WIEN_X = wien_root()
WIEN_B = H*C_LIGHT/(KB*WIEN_X)


def canonique(d):
    mode = choice(d,"mode","deux",["deux","trois"])
    if mode == "trois":
        return canonique_trois(d)
    temp = number(d,"temperature",300,1,3000)
    epsilon_mev = number(d,"epsilon_mev",25,.1,250)
    particles = number(d,"particles",100,1,100000,True)
    fraction = number(d,"fraction",.25,0,1)
    epsilon = epsilon_mev*1e-3*E_CHARGE
    x = epsilon/(KB*temp)
    state = two_level_statistics(x)
    # Entier au plus proche ; la fraction effective est affichée explicitement.
    excited = int(math.floor(particles*fraction+.5))
    micro = microcanonical_two_level(particles,excited)
    theta = np.geomspace(.02,10,160)
    thermal = [two_level_statistics(1/t) for t in theta]
    counts = np.unique(np.rint(np.linspace(0,particles,min(particles+1,151))).astype(int))
    micros = [microcanonical_two_level(particles,int(k)) for k in counts]
    beta_label = "non défini au bord" if micro["beta_epsilon_stirling"] is None else f'{micro["beta_epsilon_stirling"]:.7g}'
    return dict(metrics=[metric("Fraction excitée canonique",state["probabilities"][1],"p=1/(1+exp(ε/kBT)) ; T positif"),
                         metric("Capacité C / (N kB)",state["heat_capacity"],"x²/[4 cosh²(x/2)] ; facteur 1/4"),
                         metric("Entropie microcanonique S / kB",micro["entropy"],"ln C(N,k), N fixé et k excités")],
        charts=[chart("Deux niveaux : populations et capacité","kBT / ε","Grandeurs par site",[series("Fraction excitée",theta,[s["energy_ratio"] for s in thermal]),series("C / (N kB)",theta,[s["heat_capacity"] for s in thermal],"rose"),series("S canonique / (N kB)",theta,[s["entropy"] for s in thermal],"gold")],logx=True),
                chart("Comptage exact et Stirling","Fraction excitée k / N","S / kB",[series("ln C(N,k), exact",counts/particles,[s["entropy"] for s in micros]),series("Stirling dominant N h(k/N)",counts/particles,[s["stirling_leading"] for s in micros],"gold")])],
        table=table(["Grandeur","Valeur","Portée"],[["N, sites distinguables",particles,"N fixé"],["k excités, arrondi de N×fraction",excited,f"k/N={excited/particles:g}"],["log Z_N",particles*state["log_partition"],"Z_N=(1+exp(−βε))^N, sans N!"],["U canonique",particles*epsilon*state["energy_ratio"],"J ; zéro choisi au niveau fondamental"],["S canonique / kB",particles*state["entropy"],"Fluctuations de k autorisées"],["S microcanonique / kB",micro["entropy"],"k fixé"],["Stirling raffiné",micro["stirling_refined"] if micro["stirling_refined"] is not None else "inapplicable au bord","k et N−k doivent être grands"],["βε microcanonique (Stirling)",beta_label,"ln[(N−k)/k] ; négatif si k>N/2"]]),
        notes=["Les N objets sont des sites localisés distinguables et indépendants à niveaux 0,ε. Le comptage microcanonique est Ω=C(N,k), tandis que le thermostat autorise k à fluctuer.",
               "Le laboratoire garde N fixé : il ne calcule pas de potentiel chimique à partir d'une dérivée en N. La dérivée microcanonique en énergie devient une approximation continue à grand N.",
               "L'entropie exacte vaut zéro aux bords k=0,N. Stirling raffiné diverge aux bords et n'y est pas employé ; la formule dominante reste une approximation, pas une identité.",
               "Le spectre borné admet une température microcanonique négative quand la population est inversée. Le curseur du thermostat représente seulement T>0, pour lequel p_exc<1/2.",
               "La capacité positive vaut C=NkB x²p(1−p), avec un facteur 1/4 devant cosh⁻²(x/2). Le pic Schottky n'est pas une transition de phase."],
        theory=dict(mode=mode,x=x,temperature=temp,epsilon_joule=epsilon,particles=particles,
                    probabilities=state["probabilities"].tolist(),log_partition=particles*state["log_partition"],
                    energy_joule=particles*epsilon*state["energy_ratio"],heat_capacity_kb=particles*state["heat_capacity"],
                    entropy_kb=particles*state["entropy"],microcanonical=micro))


def canonique_trois(d):
    temp = number(d,"temperature",300,1,3000)
    epsilon_mev = number(d,"epsilon_mev",25,.1,250)
    g = number(d,"degeneracy",4,1,30,True)
    epsilon = epsilon_mev*1e-3*E_CHARGE
    x = epsilon/(KB*temp)
    state = canonical_levels(x,g)
    theta = np.geomspace(.02,10,160)
    states = [canonical_levels(1/t,g) for t in theta]
    probs = np.array([s["probabilities"] for s in states])
    return dict(metrics=[metric("Énergie U / ε",state["energy_ratio"],"Moyenne des trois niveaux, dégénérescence incluse"),
                         metric("Capacité C / kB",state["heat_capacity"],"C/kB=Var(E)/(kBT)² ; spectre fixé"),
                         metric("Entropie S / kB",state["entropy"],"Entropie des microétats, pas des trois seuls niveaux")],
        charts=[chart("Population d'un niveau ≠ probabilité d'un microétat","kBT / ε","Probabilité du niveau",[series(f"E={j}ε ; g={v}",theta,probs[:,j],["green","gold","rose"][j]) for j,v in enumerate([1,g,1])],logx=True),
                chart("Stocker l'énergie : réponse thermique","kBT / ε","Grandeurs réduites",[series("U / ε",theta,[s["energy_ratio"] for s in states]),series("C / kB",theta,[s["heat_capacity"] for s in states],"rose")],logx=True)],
        table=table(["Niveau","Dégénérescence","Probabilité du niveau","Probabilité par microétat"],[[f"{j} ε",v,float(state["probabilities"][j]),float(state["probabilities"][j]/v)] for j,v in enumerate([1,g,1])]),
        notes=["Système en équilibre avec un thermostat à T>0 ; trois niveaux exactement spécifiés et dégénérescences 1,g,1.",
               "À haute température, les microétats sont équiprobables : les niveaux ne le sont pas si g≠1. Alors U→ε et S→kB ln(g+2).",
               "La capacité est positive et tend vers zéro aux deux extrêmes pour ce spectre borné. Le pic est un effet Schottky, sans transition de phase.",
               f"Paramètres SI : T={temp:g} K, ε={epsilon_mev:g} meV. La position actuelle sur les courbes est kBT/ε={1/x:.5g}."],
        theory=dict(x=x,temperature=temp,epsilon_joule=epsilon,degeneracy=g,probabilities=state["probabilities"].tolist(),log_partition=state["log_partition"],energy_joule=epsilon*state["energy_ratio"],heat_capacity_kb=state["heat_capacity"],entropy_kb=state["entropy"]))


def gaz(d):
    temp = number(d,"temperature",300,1,3000)
    side_nm = number(d,"side_nm",3,.2,20)
    mass_ratio = number(d,"mass_ratio",1,.1,5)
    cutoff = number(d,"cutoff",36,4,100,True)
    log_density = number(d,"log_density",23,15,28)
    mass = M_E*mass_ratio
    side = side_nm*1e-9
    unit = math.pi**2*HBAR**2/(2*mass*side**2)
    x = unit/(KB*temp)
    state = cube_statistics(x,cutoff)
    reference = cube_statistics(x,2*cutoff)
    delta = reference["log_partition"]-state["log_partition"]
    # Masse absente relativement au calcul à 2N, pas une borne sur la queue infinie.
    omitted = -math.expm1(-max(0.,delta))
    energy = unit*state["energy_ratio"]
    wavelength = H/math.sqrt(2*math.pi*mass*KB*temp)
    degeneracy_parameter = 10**log_density*wavelength**3
    theta = np.geomspace(.04,200,170)
    curves = [cube_statistics(1/t,max(2*cutoff,math.ceil(8*math.sqrt(t)))) for t in theta]
    counts = sorted(set([4,8,12,20,cutoff,2*cutoff]))
    conv = [cube_statistics(x,n) for n in counts]
    log_mb = 3*math.log(side/wavelength)
    return dict(metrics=[metric("Énergie U / kBT",energy/(KB*temp),"Une particule ; limite classique 3/2"),
                         metric("Capacité C / kB",state["heat_capacity"],"Une particule ; limite classique 3/2"),
                         metric("Critère n λth³",degeneracy_parameter,"n : densité proposée ; critère MB si ≪1")],
        charts=[chart("De la boîte quantique à l'équipartition","kBT / E_L","Grandeurs par particule",[series("U / kBT",theta,[s["energy_ratio"]/t for s,t in zip(curves,theta)]),series("C / kB",theta,[s["heat_capacity"] for s in curves],"rose"),series("Limite classique 3/2",theta,np.full_like(theta,1.5),"gold")],logx=True),
                chart("Contrôler la coupure des nombres quantiques","Nombre maximal nᵢ","U / E_L",[series("Somme factorisée tronquée",counts,[s["energy_ratio"] for s in conv],kind="dots")])],
        table=table(["Grandeur","Valeur","Unité / portée"],[["E_L",unit/E_CHARGE,"eV"],["U",energy/E_CHARGE,"eV par particule"],["log Z₁, somme tronquée",state["log_partition"],"Sans dimension"],["log Z₁ classique",log_mb,"V/λth³ ; approximation continue"],["Écart de masse N→2N",omitted,"Diagnostic, pas borne absolue"],["λth",wavelength*1e9,"nm"],["Pression d'une particule",2*energy/(3*side**3),"Pa ; variation homothétique de la boîte"]]),
        notes=["Ce calcul canonique concerne une seule particule non relativiste, sans interaction, dans un cube à parois infinies. Les trois sommes se factorisent ; la coupure est nᵢ≤N dans chaque direction.",
               "À basse température U→3E_L et C→0. Le gaz classique U=3kBT/2 exige des niveaux suffisamment rapprochés et une statistique d'échange négligeable.",
               "Le rapport nλth³ teste cette seconde hypothèse pour une densité choisie. Il ne transforme pas la somme d'une particule en calcul exact de N bosons ou fermions.",
               f"L'écart N→2N vaut {omitted:.3g} pour la masse de partition. Il ne borne pas la queue au-delà de 2N. La courbe thermique élargit automatiquement sa somme à max(2N,⌈8√(kBT/E_L)⌉) ; les métriques et la comparaison des coupures gardent N choisi.",
               "P=2U/(3V) vient des niveaux en L⁻² pour une dilatation isotrope. PV=kBT est seulement la limite classique par particule."],
        theory=dict(x=x,temperature=temp,side_m=side,mass_kg=mass,cutoff=cutoff,energy_unit_joule=unit,energy_joule=energy,heat_capacity_kb=state["heat_capacity"],log_partition=state["log_partition"],entropy_kb=state["entropy"],thermal_wavelength_m=wavelength,degeneracy_parameter=degeneracy_parameter,truncation_diagnostic=omitted,reference_energy_joule=unit*reference["energy_ratio"]))


def oscillateur(d):
    temp = number(d,"temperature",300,.5,3000)
    frequency = number(d,"frequency_thz",5,.05,50)*1e12
    confinement = number(d,"confinement",1,0,6,True)
    quadratic_terms = 3+confinement
    quantum = H*frequency
    x = quantum/(KB*temp)
    state = oscillator_statistics(x)
    theta = np.geomspace(.015,20,180)
    states = [oscillator_statistics(1/t) for t in theta]
    n = np.arange(25)
    probabilities = -math.expm1(-x)*np.exp(-x*n)
    return dict(metrics=[metric("Énergie U / hν",state["energy_ratio"],"Point zéro inclus : E₀=hν/2"),
                         metric("Capacité C / kB",state["heat_capacity"],"Dérivée à fréquence fixe ; limite classique 1"),
                         metric("Occupation moyenne ⟨n⟩",state["mean_occupation"],"Nombre de quanta d'excitation")],
        charts=[chart("Le gel quantique des degrés de liberté","kBT / hν","Grandeurs réduites",[series("U / hν",theta,[s["energy_ratio"] for s in states]),series("C / kB",theta,[s["heat_capacity"] for s in states],"rose"),series("U classique / hν",theta,theta,"gold")],logx=True),
                chart("Distribution géométrique des excitations","Nombre quantique n","Probabilité pₙ",[series("pₙ, sans renormaliser la fenêtre",n,probabilities,kind="dots")])],
        table=table(["Grandeur","Valeur","Unité"],[["Température",temp,"K"],["Fréquence ν",frequency/1e12,"THz"],["Quantum hν",quantum/E_CHARGE*1000,"meV"],["log Z",state["log_partition"],"Sans dimension"],["S / kB",state["entropy"],"Sans dimension"],["Masse après n=24",math.exp(-25*x),"Queue exacte de la loi géométrique"],["Termes quadratiques classiques",quadratic_terms,f"3 de translation + {confinement} supplémentaires"],["U classique, modèle 3+r",quadratic_terms*KB*temp/2,"J ; autre modèle que l'OH 1D"],["C classique / kB, modèle 3+r",quadratic_terms/2,"Nombre de termes / 2"]]),
        notes=["L'oscillateur est en équilibre avec un thermostat ; son spectre Eₙ=hν(n+1/2) est celui du volet quantique.",
               "Z=e⁻ˣᐟ²/(1−e⁻ˣ) et pₙ=(1−e⁻ˣ)e⁻ⁿˣ. La somme infinie est calculée exactement ; le graphique de 25 états n'est pas renormalisé.",
               "À T→0, l'énergie de point zéro reste présente mais sa dérivée thermique est nulle : C→0. À haute température, C→kB et U≈kBT.",
               "Pour 3N oscillateurs indépendants de même fréquence, multiplier U et C par 3N : c'est le modèle d'Einstein d'un solide, idéalisation sans modes acoustiques.",
               f"L'exercice d'équipartition compte séparément 3 termes cinétiques de translation et r={confinement} termes quadratiques supplémentaires : U=(3+r)kBT/2. Pour r=1, le terme supplémentaire peut être le rappel selon x, tandis que y,z restent libres dans un volume fini. Un oscillateur harmonique 1D complet a deux termes au total et donne U=kBT.",
               "Pour une seule particule 3D, un rappel harmonique spatial ajoute au plus trois termes potentiels. r>3 est un comptage formel nécessitant des variables internes supplémentaires, dont les termes cinétiques doivent aussi être comptés ; ce ne sont pas six coordonnées spatiales de confinement. Par exemple trois vibrations 1D complètes ajoutent six termes à la translation."],
        theory=dict(x=x,temperature=temp,frequency_hz=frequency,energy_quantum_joule=quantum,energy_joule=quantum*state["energy_ratio"],mean_occupation=state["mean_occupation"],heat_capacity_kb=state["heat_capacity"],entropy_kb=state["entropy"],log_partition=state["log_partition"],probabilities=probabilities.tolist(),tail_probability=math.exp(-25*x),confinement_terms=confinement,classical_quadratic_terms=quadratic_terms,classical_energy_joule=quadratic_terms*KB*temp/2))


def spins(d):
    temp = number(d,"temperature",5,.1,500)
    field = number(d,"field",2,-10,10)
    moment_ratio = number(d,"magnetic_moment",1,.01,3)
    moment = moment_ratio*MU_B
    x = moment*field/(KB*temp)
    state = spin_statistics(x)
    fields = np.linspace(-10,10,180)
    magnet = np.tanh(moment*fields/(KB*temp))
    curie = moment*fields/(KB*temp)
    reduced = np.geomspace(.02,12,160)
    thermal = [spin_statistics(v) for v in reduced]
    return dict(metrics=[metric("Aimantation par spin / μ",state["polarization"],"Saturation entre −1 et +1"),
                         metric("Capacité C_B / kB",state["heat_capacity"],"Champ fixé ; pic Schottky à deux niveaux"),
                         metric("Entropie S / kB",state["entropy"],"À B=0 : ln 2 ; à fort |B|/T : 0")],
        charts=[chart("Loi de Curie et saturation","Champ B (T)","Moment moyen / μ",[series("tanh(μB/kBT)",fields,magnet),series("Curie : μB/kBT",fields,curie,"gold")]),
                chart("Une population à deux niveaux","|μB| / kBT","Grandeurs réduites",[series("C_B / kB",reduced,[s["heat_capacity"] for s in thermal],"rose"),series("S / kB",reduced,[s["entropy"] for s in thermal])],logx=True)],
        table=table(["Grandeur","Valeur","Unité"],[["μ",moment,"J/T"],["x=μB/kBT",x,"Sans dimension"],["Probabilité du moment +μ",state["probability_aligned"],"Pas forcément état fondamental si B<0"],["Énergie par spin",-moment*field*state["polarization"],"J"],["Susceptibilité par spin",moment**2/(KB*temp)*state["susceptibility_ratio"],"J/T² ; dérivée du moment par rapport à B"]]),
        notes=["Moments indépendants ±μ, sans interaction ni ferromagnétisme. Les deux énergies sont ∓μB ; la séparation vaut2μ|B|.",
               "Le moment μ est fourni en multiples du magnéton de Bohr. Un proton possède un autre moment : ne pas confondre ce modèle de paramagnétisme électronique avec les fréquences RMN du volet quantique.",
               "La loi de Curie est la linéarisation pour |μB|≪kBT. Elle n'est pas valable près de la saturation ; une droite dépassant ±1 n'est pas une probabilité.",
               "À B=0, les deux niveaux restent exactement dégénérés : S=kB ln 2 pour un spin isolé dans ce modèle. La limite T→0 à champ non nul donne S→0."],
        theory=dict(x=x,temperature=temp,field_tesla=field,magnetic_moment_joule_per_tesla=moment,polarization=state["polarization"],energy_joule=-moment*field*state["polarization"],heat_capacity_kb=state["heat_capacity"],entropy_kb=state["entropy"],probability_plus=state["probability_aligned"],susceptibility=moment**2/(KB*temp)*state["susceptibility_ratio"]))


def visible_fraction(temperature, lower_m=.39e-6, upper_m=.78e-6):
    """π∫visible Bλ dλ /(σT⁴), sans réponse photopique de l'œil."""
    if not math.isfinite(temperature) or temperature <= 0 or not 0 < lower_m < upper_m:
        raise ValueError("T positif et bande λmin<λmax positive requise.")
    low = H*C_LIGHT/(upper_m*KB*temperature)
    high = H*C_LIGHT/(lower_m*KB*temperature)
    integral = _integrate_segments(lambda v:v**3*occupation(v,0.,"BE"),[low,high])
    return integral/(math.pi**4/15)


def planck(d):
    temp = number(d,"temperature",5800,100,10000)
    wavelength_um = number(d,"wavelength_um",.5,.05,200)
    selected = wavelength_um*1e-6
    peak = WIEN_B/temp
    wavelength = np.geomspace(peak*.18,peak*10,200)
    exact = planck_radiance(wavelength,temp)*1e-6
    rj = 2*C_LIGHT*KB*temp/wavelength**4*1e-6
    temperatures = np.geomspace(100,10000,140)
    nodes,weights = np.polynomial.legendre.leggauss(96)
    u = (nodes+1)*20
    integral = float(20*np.sum(weights*u**3*occupation(u,0,"BE")))
    visible = visible_fraction(temp)
    return dict(metrics=[metric("Maximum de Bλ",peak*1e6,"μm ; λmax T=b de Wien"),
                         metric("Flux total σT⁴",SIGMA*temp**4,"W/m² ; émission dans un hémisphère"),
                         metric("Bλ à la longueur choisie",planck_radiance(selected,temp)*1e-6,"W m⁻² sr⁻¹ μm⁻¹"),
                         metric("Rendement visible",100*visible,"% du flux sur [390,780] nm ; rendement radiométrique")],
        charts=[chart("Le spectre d'un corps noir idéal","Longueur d'onde λ (μm)","Bλ (W m⁻² sr⁻¹ μm⁻¹)",[series("Planck",wavelength*1e6,exact),series("Rayleigh–Jeans",wavelength*1e6,rj,"gold")],logx=True,logy=True),
                chart("La loi en T⁴","Température T (K)","Flux (W/m²)",[series("σT⁴",temperatures,SIGMA*temperatures**4)],logx=True,logy=True),
                chart("Quelle part est visible ?","Température T (K)","Fraction du flux (%)",[series("Bande 390–780 nm",temperatures,[100*visible_fraction(t) for t in temperatures])],logx=True)],
        table=table(["Grandeur","Valeur","Portée"],[["b de Wien",WIEN_B,"m K, maximum par unité de λ"],["σ",SIGMA,"W m⁻² K⁻⁴"],["Racine de Wien",WIEN_X,"5(1−exp(−x))=x, x≠0"],["∫₀⁴⁰ x³/(exp(x)−1) dx",integral,"Quadrature 96 points, queue non incluse"],["Intégrale exacte sur [0,∞[",math.pi**4/15,"Sans dimension"],["h c / (λ kBT)",H*C_LIGHT/(selected*KB*temp),"Rayleigh–Jeans valide seulement si ≪1"]]),
        notes=["Bλ est une luminance spectrale par unité de longueur d'onde et par stéradian. Le graphique convertit du mètre vers le micromètre en multipliant par 10⁻⁶.",
               "Un corps noir isotrope donne un flux surfacique π∫Bλdλ=σT⁴. L'irradiance reçue à distance dépend ensuite de la géométrie.",
               "La loi de Rayleigh–Jeans est une approximation de basse fréquence, ou grande longueur d'onde. Son intégrale ultraviolette diverge.",
               "Le maximum de Bν n'est pas c/λmax de Bλ : le changement de variable comporte un jacobien. Les photons ont μ=0 ; leur nombre n'est pas imposé.",
               "Le rendement visible intègre la bande 390–780 nm de l'énoncé. À 2500 K il vaut environ 5,896 %. Le corrigé du recueil emploie ailleurs 760 nm : cette autre bande donne environ 5,187 %. Ce rendement énergétique ne mesure pas la sensibilité photopique ni le rendement électrique d'une lampe."],
        theory=dict(temperature=temp,wavelength_m=selected,radiance_per_m=planck_radiance(selected,temp),peak_wavelength_m=peak,wien_constant=WIEN_B,stefan_boltzmann=SIGMA,emitted_flux=SIGMA*temp**4,dimensionless_integral_numerical=integral,dimensionless_integral_exact=math.pi**4/15,visible_fraction=visible,visible_band_m=[.39e-6,.78e-6]))


def occupations(d):
    mode = choice(d,"mode","fermi",["fermi","bose","comparaison"])
    if mode == "comparaison":
        return occupations_comparaison(d)
    temp = number(d,"temperature",300,1e-8,3000)
    log_density = number(d,"log_density",28,15,30)
    density = 10**log_density
    if mode == "fermi":
        mass = M_E
        scale = fermi_temperature(density)
        theta = temp/scale
        state = fermi_gas_state(theta)
        ef = KB*scale
        mu = state["mu_ef"]*ef
        energy = np.linspace(0,max(3.,12*theta),240)
        curve = occupation(energy/theta,state["mu_ef"]/theta,"FD")
        density_curve = 1.5*np.sqrt(energy)*curve
        zero_t = (energy<1).astype(float)
        return dict(metrics=[metric("Température de Fermi TF",scale,"K ; électrons, deux états de spin"),
                             metric("T / TF",theta,"Dégénérescence forte si ≪1"),
                             metric("Potentiel chimique μ / EF",state["mu_ef"],"Résolu à densité n et T fixées")],
            charts=[chart("Pauli et le bord de Fermi","Énergie E / EF","Occupation par état de spin",[series("FD à T choisi",energy,curve,"rose"),series("Limite T=0",energy,zero_t,"gold",kind="step")]),
                    chart("Occupation × densité d'états","Énergie E / EF","Distribution en énergie, par unité de E/EF",[series("(3/2) √(E/EF) fFD",energy,density_curve,"rose")])],
            table=table(["Grandeur","Valeur","Unité / portée"],[["Densité n",density,"m⁻³, deux états de spin inclus"],["Masse",mass,"kg ; électron"],["EF",ef/E_CHARGE,"eV"],["μ",mu/E_CHARGE,"eV ; origine au fond du continuum"],["Énergie moyenne U/N",state["energy_ef"]*ef/E_CHARGE,"eV"],["Pression",2*density*state["energy_ef"]*ef/3,"Pa ; gaz libre isotrope non relativiste"],["Résidu numérique du nombre",state["number_residual"],"N_calculé/N_imposé − 1"],["Limite T=0 : U/(N EF)",.6,"Remplissage d'une sphère de Fermi"]]),
            notes=["Gaz idéal électronique homogène 3D, non relativiste, sans interactions. Chaque état spatial dispose de deux états de spin ; la densité d'états totale inclut g=2.",
                   "EF=ℏ²(3π²n)^(2/3)/(2me), TF=EF/kB. À T=0 tous les états d'énergie E<EF sont occupés et U/N=3EF/5 : l'énergie ne tend pas vers zéro.",
                   "À T>0, μ est déterminé par l'intégrale du nombre, puis U par une seconde intégrale. L'occupation FD est une moyenne par état ; sa multiplication par la densité d'états produit une distribution en énergie dont l'intégrale complète vaut 1. La fenêtre graphique n'est pas renormalisée.",
                   "La quadrature de Gauss est divisée autour du bord de Fermi pour résoudre les températures faibles. La queue E−μ>40kBT est omise ; le résidu du nombre teste la résolution de la contrainte, sans constituer une borne absolue d'erreur de quadrature.",
                   "Les densités extrêmes servent d'exploration formelle : le modèle d'électrons libres sans interactions ne décrit pas tous les matériaux. La contrainte de Pauli s'applique à un état complet, spin compris."],
            theory=dict(mode=mode,temperature=temp,density_per_m3=density,mass_kg=mass,spin_degeneracy=2,fermi_temperature=scale,fermi_energy_joule=ef,temperature_ratio=theta,chemical_potential_joule=mu,mu_ef=state["mu_ef"],energy_per_particle_joule=state["energy_ef"]*ef,pressure_pa=2*density*state["energy_ef"]*ef/3,number_residual=state["number_residual"]))
    mass_atom_u = number(d,"mass_atom_u",87,1,250)
    mass = mass_atom_u*M_U
    scale = bose_temperature(density,mass)
    theta = temp/scale
    state = bose_gas_state(theta)
    wavelength = thermal_wavelength(temp,mass)
    energy = np.geomspace(.001,12,220)
    curve = occupation(energy,state["mu_ratio"],"BE")
    density_curve = 2/math.sqrt(math.pi)*np.sqrt(energy)*curve/(density*wavelength**3)
    temperatures = np.linspace(0,2.5,180)
    fraction = np.maximum(0,1-temperatures**1.5)
    mu = state["mu_ratio"]*KB*temp
    return dict(metrics=[metric("Température critique Tc",scale,"K ; gaz homogène idéal 3D, une composante"),
                         metric("T / Tc",theta,"Seuil de condensation à 1"),
                         metric("Fraction condensée N0 / N",state["condensate_fraction"],"Macroscopique ; état fondamental séparé du continuum")],
        charts=[chart("Le condensat apparaît quand le continuum sature","T / Tc","Fraction de particules",[series("N0/N",temperatures,fraction),series("Nexc/N",temperatures,1-fraction,"gold")]),
                chart("Excitations au-dessus du fondamental","Énergie E / kBT","Distribution par unité de E/kBT",[series("Densité d'états × occupation / n",energy,density_curve)],logx=True)],
        table=table(["Grandeur","Valeur","Unité / portée"],[["Densité n",density,"m⁻³"],["Masse",mass_atom_u,"u ; atomes bosoniques, pas électrons"],["λth",wavelength*1e9,"nm"],["n λth³",density*wavelength**3,"ζ(3/2) au seuil"],["ζ(3/2)",ZETA_3_2,"Une seule composante g=1"],["μ / kBT",state["mu_ratio"],"μ=0 sous Tc dans la limite thermodynamique"],["μ",mu,"J"],["Fraction thermique",state["thermal_fraction"],"Aire du continuum, fondamental exclu"],["Résidu numérique du nombre",state["number_residual"],"Part thermique + condensat"]]),
        notes=["Gaz idéal homogène 3D à une composante bosonique (g=1), énergie minimale 0 et densité fixée. Exemple : masse 87 u, n=10²⁰ m⁻³, T=100 nK ; Tc≈398 nK. Un nuage piégé dans un potentiel harmonique possède une autre loi de Tc.",
               "Tc=(2πℏ²/mkB)[n/ζ(3/2)]^(2/3). Le facteur ζ appartient lui aussi à la puissance 2/3. La longueur thermique vérifie nλth³=ζ(3/2) au seuil.",
               "Pour T≤Tc, le continuum ne peut accueillir que Nexc/N=(T/Tc)^(3/2) ; μ=0 et le reste est un condensat macroscopique. Toutes les particules ne sont au fondamental qu'à T→0 dans ce modèle.",
               "Le fondamental est traité séparément : sa fraction n'est pas obtenue en évaluant fBE(0,0), qui diverge. L'intégrale complète des excitations vaut la fraction thermique ; le graphique montre seulement 0,001≤E/kBT≤12 et n'est pas renormalisé.",
               "Pour T>Tc, μ<0 est résolu par bissection de l'intégrale du nombre. Une quadrature segmentée près de E≈−μ limite les difficultés proches de Tc ; la queue E/kBT>40 est omise. Le résidu du nombre ne borne pas à lui seul l'erreur de quadrature.",
               "L'idéalisation ignore les interactions, la taille finie et le piège expérimental. La masse est exprimée en u ; la statistique bosonique est supposée pour la composante atomique choisie."],
        theory=dict(mode=mode,temperature=temp,density_per_m3=density,mass_kg=mass,mass_atom_u=mass_atom_u,spin_degeneracy=1,critical_temperature=scale,temperature_ratio=theta,chemical_potential_joule=mu,mu_ratio=state["mu_ratio"],condensate_fraction=state["condensate_fraction"],thermal_fraction=state["thermal_fraction"],thermal_wavelength_m=wavelength,degeneracy_parameter=density*wavelength**3,number_residual=state["number_residual"]))


def occupations_comparaison(d):
    temp = number(d,"temperature",300,1e-8,3000)
    mu = number(d,"mu_ratio",-2,-8,-.01)
    selected = number(d,"energy_ratio",1,0,12)
    energy = np.linspace(0,12,180)
    values = {name:occupation(energy,mu,name) for name in ["BE","FD","MB"]}
    point = {name:occupation(selected,mu,name) for name in values}
    variances = dict(BE=point["BE"]*(1+point["BE"]),FD=point["FD"]*(1-point["FD"]),MB=point["MB"])
    return dict(metrics=[metric("Bosons : ⟨n⟩",point["BE"],"Un état peut accueillir plusieurs particules"),
                         metric("Fermions : ⟨n⟩",point["FD"],"Un état, spin fixé : 0≤⟨n⟩≤1"),
                         metric("Limite Maxwell–Boltzmann",point["MB"],"e^{(μ−ε)/kBT} ; approximation si ⟨n⟩≪1")],
        charts=[chart("Occupation moyenne : trois statistiques","Énergie ε / kBT","⟨n⟩ par état",[series(name,energy,values[name],color) for name,color in [("BE","green"),("FD","rose"),("MB","gold")]]),
                chart("Comparer les fluctuations d'un état","Énergie ε / kBT","Var(n)",[series("BE : n(1+n)",energy,values["BE"]*(1+values["BE"])),series("FD : n(1−n)",energy,values["FD"]*(1-values["FD"]),"rose"),series("MB : n",energy,values["MB"],"gold")])],
        table=table(["Statistique","Occupation moyenne","Variance","Type de loi d'un état"],[[name,point[name],variances[name],kind] for name,kind in [("BE","Géométrique"),("FD","Bernoulli"),("MB","Poisson en régime dilué")]]),
        notes=["L'énergie minimale est choisie égale à 0 ; μ/kBT est strictement négatif pour que toutes les occupations bosoniques soient définies. Ce laboratoire compare les trois lois au même μ.",
               "Les courbes sont des occupations moyennes par état, pas une densité de probabilité normalisée sur l'énergie. Pour obtenir un nombre total, sommer sur les états et leurs dégénérescences.",
               "Dans un gaz à nombre fixé, μ doit être déterminé par la contrainte sur N ; les curseurs représentent ici un réservoir grand canonique.",
               "Pour ε−μ≫kBT, BE et FD tendent vers MB. Pauli contraint un état fermionique complet, spin compris. L'approche μ→0⁻ n'est pas, à elle seule, un calcul de condensation de Bose–Einstein.",
               "La fonction Python occupation permet aussi μ>0 pour FD ; le mode Fermi résout μ à densité fixée. La comparaison au même réservoir garde μ<0 pour inclure BE."],
        theory=dict(temperature=temp,mu_ratio=mu,chemical_potential_joule=mu*KB*temp,energy_ratio=selected,energy_joule=selected*KB*temp,occupations=point,variances=variances))


def maxwell(d):
    mode = choice(d,"mode","vitesses",["vitesses","pression","effusion","paroi"])
    temperature = number(d,"temperature",300,1,3000)
    molar_mass = number(d,"molar_mass",28,1,200)
    log_density = number(d,"log_density",25,15,28)
    mass = molar_mass*1e-3/N_A
    density = 10**log_density
    state = maxwell_statistics(temperature,mass,density)
    sigma = state["sigma"]
    speeds = np.linspace(0,6*sigma,220)
    vx = np.linspace(-5*sigma,5*sigma,220)
    speed_pdf = maxwell_speed_density(speeds,temperature,mass)
    gaussian = np.exp(-vx**2/(2*sigma**2))/(math.sqrt(2*math.pi)*sigma)
    wavelength = thermal_wavelength(temperature,mass)
    common_notes = ["Gaz parfait classique monatomique, isotrope et dilué, molécules non relativistes. La masse moléculaire vaut M/N_A avec M convertie de g/mol en kg/mol. Les vitesses sont en m/s ; une densité de probabilité de vitesse a pour unité s/m.",
                    "Les composantes cartésiennes sont gaussiennes indépendantes, de variance kBT/m. La norme v≥0 suit une loi de Maxwell ; v_probable, ⟨v⟩ et √⟨v²⟩ sont différents.",
                    f"Le critère proposé vaut nλth³={density*wavelength**3:.4g} ; l'emploi de Maxwell–Boltzmann exige nλth³≪1 et des interactions négligeables. Les valeurs extrêmes du curseur peuvent sortir de cette idéalisation."]
    result = dict(metrics=[metric("Vitesse la plus probable",state["most_probable"],"m/s ; √(2kBT/m)"),
                           metric("Vitesse moyenne",state["mean_speed"],"m/s ; √(8kBT/πm)"),
                           metric("Vitesse quadratique moyenne",state["rms_speed"],"m/s ; √(3kBT/m)")],
        charts=[chart("Composante et norme : deux distributions","Vitesse (m/s)","Densité de probabilité (s/m)",[series("Composante vx",vx,gaussian,"gold"),series("Norme v",speeds,speed_pdf)]),
                chart("Les molécules rapides traversent davantage","Norme v (m/s)","Densité de probabilité (s/m)",[series("Gaz dans le volume",speeds,speed_pdf),series("Gaz effusant : v f(v)/⟨v⟩",speeds,maxwell_speed_density(speeds,temperature,mass,True),"rose")])],
        table=table(["Grandeur","Valeur","Unité"],[["Masse moléculaire",mass,"kg"],["Pression",state["pressure"],"Pa"],["Flux incident n⟨v⟩/4",state["incident_flux"],"molécules m⁻² s⁻¹"],["⟨vx²⟩",sigma**2,"m²/s²"],["Énergie moyenne dans le gaz",1.5*KB*temperature,"J"],["Énergie moyenne des molécules effusantes",2*KB*temperature,"J ; sélection par le flux"],["nλth³",density*wavelength**3,"Critère classique"]]),
        notes=common_notes,
        theory=dict(mode=mode,temperature=temperature,mass_kg=mass,molar_mass_g_per_mol=molar_mass,density_per_m3=density,thermal_wavelength_m=wavelength,degeneracy_parameter=density*wavelength**3,**state))
    if mode == "pression":
        angles = np.linspace(0,math.pi/2,180)
        temperatures = np.linspace(1,3000,180)
        result["metrics"] = [metric("Pression P",state["pressure"],"Pa ; nkBT=nm⟨vx²⟩"),metric("Flux sur une face",state["incident_flux"],"molécules m⁻² s⁻¹ ; seules les vitesses entrantes"),metric("Énergie U par molécule",1.5*KB*temperature,"J ; 3 termes quadratiques")]
        result["charts"] = [chart("Pression : transfert de quantité de mouvement","Température T (K)","Pression P (Pa)",[series("nkBT",temperatures,density*KB*temperatures)]),chart("Une face ne reçoit qu'un hémisphère","Angle avec la normale θ (degrés)","Poids angulaire normalisé par degré",[series("3 sinθ cos²θ × π/180",angles*180/math.pi,3*np.sin(angles)*np.cos(angles)**2*math.pi/180)])]
        result["notes"] += ["Chaque collision élastique transfère 2m|vx| à la paroi ; le nombre de collisions comporte encore un facteur |vx|. Intégrer seulement vx>0 donne P=nm⟨vx²⟩, sans facteur 2 supplémentaire.","Le poids 3 sinθ cos²θ s'intègre à 1 sur [0,π/2] en radians. Le graphique convertit à la fois l'angle et sa densité vers le degré, avec le jacobien π/180."]
    if mode in ["effusion","paroi"]:
        volume = number(d,"volume_litre",1,.001,100)*1e-3
        area = number(d,"hole_mm2",.01,1e-6,10)*1e-6
        reduced_time = number(d,"time_ratio",1,0,8)
        rate1 = area/volume*sigma/math.sqrt(2*math.pi)
        tau = 1/rate1
        tt = np.linspace(0,8,180)
        remaining = math.exp(-reduced_time)
        result["metrics"] = [metric("Temps d'effusion τ",tau,"s ; V/S √(2πm/kBT)"),metric("Fraction restante N(t)/N(0)",remaining,"Température maintenue constante"),metric("Temps choisi t",reduced_time*tau,"s ; curseur t/τ")]
        result["charts"] = [chart("Vidange isotherme vers le vide","t / τ","Fraction",[series("N(t)/N(0)=exp(−t/τ)",tt,np.exp(-tt)),series("Fraction sortie",tt,1-np.exp(-tt),"gold")]),chart("Filtrage cinétique à travers un petit trou","Vitesse v (m/s)","Densité de probabilité (s/m)",[series("Volume",speeds,speed_pdf),series("Flux effusant",speeds,maxwell_speed_density(speeds,temperature,mass,True),"rose")])]
        result["table"]["rows"] += [["Volume",volume,"m³"],["Surface totale des trous",area,"m²"],["N initial",density*volume,"molécules"],["Débit sortant initial",state["incident_flux"]*area,"molécules/s"],["Débit sortant à t",rate1*density*volume*remaining,"molécules/s"]]
        result["notes"] += ["Effusion de Knudsen : dimensions des trous petites devant le libre parcours moyen, gaz interne rééquilibré rapidement, extérieur assimilé au vide. Le modèle n'est pas l'écoulement hydrodynamique par un grand orifice.","Le thermostat maintient T : dN/dt=−(S/V)√(kBT/2πm) N. Les molécules sortantes ont une énergie moyenne 2kBT, supérieure à 3kBT/2 ; sans thermostat le gaz refroidit et cette exponentielle à T constant cesse d'être le modèle adapté."]
        result["theory"].update(volume_m3=volume,hole_area_m2=area,rate_per_second=rate1,tau_seconds=tau,time_seconds=reduced_time*tau,remaining_fraction=remaining)
        if mode == "paroi":
            temperature2 = number(d,"temperature2",600,1,3000)
            volume2 = number(d,"volume2_litre",1,.001,100)*1e-3
            initial = number(d,"fraction_initial",.5,0,1)
            rate2 = area/volume2*math.sqrt(KB*temperature2/(2*math.pi*mass))
            tau_exchange = 1/(rate1+rate2)
            p1,p2 = porous_fractions(tt*tau_exchange,rate1,rate2,initial)
            chosen1,chosen2 = porous_fractions(reduced_time*tau_exchange,rate1,rate2,initial)
            total = density*(volume+volume2)
            pressure1 = total*float(chosen1)*KB*temperature/volume
            pressure2 = total*float(chosen2)*KB*temperature2/volume2
            equilibrium = rate2/(rate1+rate2)
            result["metrics"] = [metric("Fraction N1 / Ntotal",float(chosen1),"Deux thermostats, nombre total conservé"),metric("Fraction N1 stationnaire",equilibrium,"Débits opposés égaux"),metric("Temps de relaxation τ",tau_exchange,"s ; 1/(a1+a2), avec ai=S√(kBTi/2πm)/Vi")]
            result["charts"] = [chart("Relaxation entre deux volumes thermostatés","t / τ_relaxation","Fraction de molécules",[series("N1/Ntotal",tt,p1),series("N2/Ntotal",tt,p2,"gold"),series("N1 stationnaire",tt,np.full_like(tt,equilibrium),"rose")]),chart("Les pressions réduites deviennent égales","t / τ_relaxation","P / √T (Pa K⁻¹/²)",[series("P1/√T1",tt,total*p1*KB*math.sqrt(temperature)/volume),series("P2/√T2",tt,total*p2*KB*math.sqrt(temperature2)/volume2,"gold")])]
            result["table"] = table(["Grandeur","Valeur","Unité / portée"],[["T1, T2",f"{temperature:g}, {temperature2:g}","K, thermostats imposés"],["V1, V2",f"{volume:g}, {volume2:g}","m³"],["N total",total,"molécules conservées"],["N1 initial / Ntotal",initial,"Fraction"],["P1 à t choisi",pressure1,"Pa"],["P2 à t choisi",pressure2,"Pa"],["Débit net 1→2 à t choisi",total*(rate1*float(chosen1)-rate2*float(chosen2)),"molécules/s ; peut être négatif"],["P1/P2 stationnaire",math.sqrt(temperature/temperature2),"Racine du rapport des températures"]])
            result["notes"] = common_notes+["Les trous fonctionnent en régime moléculaire (Knudsen), petits devant le libre parcours moyen ; chaque compartiment se rééquilibre rapidement. La surface représente la somme des aires des petits pores.","La paroi laisse passer le même gaz dans les deux sens. Les températures sont maintenues par des thermostats ; ce montage est un état stationnaire entretenu, pas un équilibre thermique si T1≠T2.","Pendant la relaxation, dN1/dt=−a1N1+a2N2 et N1+N2 est constant. La relation N1√T1/V1=N2√T2/V2, équivalente à P1/√T1=P2/√T2, n'est vraie qu'au débit net nul."]
            # Retirer les valeurs du scénario de vidange, qui ne s'appliquent pas ici.
            for key in ["remaining_fraction","rate_per_second"]:
                result["theory"].pop(key,None)
            result["theory"].update(temperature2=temperature2,volume2_m3=volume2,rate1=rate1,rate2=rate2,total_particles=total,fraction_initial=initial,fraction1=float(chosen1),fraction2=float(chosen2),equilibrium_fraction1=equilibrium,pressure1_pa=pressure1,pressure2_pa=pressure2,tau_seconds=tau_exchange,time_seconds=reduced_time*tau_exchange)
    return result


from ising import calculate_lab as ising_lab


LABS = {"canonique":canonique,"gaz":gaz,"oscillateur":oscillateur,"spins":spins,"planck":planck,"occupations":occupations,"maxwell":maxwell,"ising":ising_lab}


def calculate(data):
    if not isinstance(data,dict):
        raise ValueError("Un objet de paramètres est attendu.")
    lab = choice(data,"lab","canonique",list(LABS))
    result = LABS[lab](data)
    result["lab"] = lab
    result["parameters"] = {key:value for key,value in data.items() if key != "lab"}
    return result
