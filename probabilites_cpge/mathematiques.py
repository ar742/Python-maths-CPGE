"""Six laboratoires de probabilités. Modèles exacts et expériences reproductibles.

Les simulations utilisent un générateur local : aucun état aléatoire global.
Les lois discrètes sont calculées sans SciPy ; les spectres utilisent NumPy.
"""
from __future__ import annotations

import math
import numpy as np


def number(data, key, default, lo, hi, integer=False):
    value = data.get(key, default)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} doit être un nombre.")
    if not math.isfinite(value) or not lo <= value <= hi:
        raise ValueError(f"{key} doit être entre {lo} et {hi}.")
    if integer and value != int(value):
        raise ValueError(f"{key} doit être entier.")
    return int(value) if integer else float(value)


def choice(data, key, default, values):
    value = data.get(key, default)
    if value not in values:
        raise ValueError(f"Choix inconnu pour {key}.")
    return value


def binomial(n, p):
    """Loi B(n,p), y compris les lois dégénérées. Logarithmes puis normalisation."""
    if p == 0 or p == 1:
        out = np.zeros(n + 1)
        out[0 if p == 0 else n] = 1
        return out
    logs = np.array([math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
                     + k*math.log(p)+(n-k)*math.log1p(-p) for k in range(n+1)])
    weights = np.exp(logs - logs.max())
    return weights / weights.sum()


def hypergeometric(red, blue, draws):
    den = math.comb(red+blue, draws)
    return np.array([math.comb(red, k)*math.comb(blue, draws-k)/den
                     if 0 <= k <= red and 0 <= draws-k <= blue else 0.
                     for k in range(draws+1)])


def wilson(successes, trials):
    """Intervalle de Wilson bilatéral, niveau nominal 95 %, approximation."""
    z = 1.959963984540054
    f = successes/trials
    den = 1+z*z/trials
    center = (f+z*z/(2*trials))/den
    radius = z*math.sqrt(f*(1-f)/trials+z*z/(4*trials*trials))/den
    return [max(0., center-radius), min(1., center+radius)]


def series(label, x, y, color="green", kind="line"):
    return dict(label=label, x=np.asarray(x).tolist(), y=np.asarray(y).tolist(),
                color=color, kind=kind)


def chart(title, xlabel, ylabel, series_list, xlim=None, ylim=None):
    return dict(title=title, xlabel=xlabel, ylabel=ylabel, series=series_list,
                xlim=xlim, ylim=ylim)


def histogram(values, bins, domain, label="Simulation", color="gold", density=False):
    counts, edges = np.histogram(values, bins=bins, range=domain)
    heights = counts/len(values)
    if density:
        heights /= np.diff(edges)
    return series(label, (edges[1:]+edges[:-1])/2, heights, color, "bars")


def empirical_cdf(values, grid):
    return np.searchsorted(np.sort(values), grid, side="right")/len(values)


def metric(label, value, note=""):
    return dict(label=label, value=float(value), note=note)


def urne(d, rng, reps):
    red = number(d, "red", 10, 1, 100, True)
    blue = number(d, "blue", 10, 1, 100, True)
    draws = number(d, "draws", 10, 1, red+blue, True)
    p = red/(red+blue)
    exact = hypergeometric(red, blue, draws)
    independent = binomial(draws, p)
    sample = rng.hypergeometric(red, blue, draws, reps)
    empirical = np.bincount(sample, minlength=draws+1)/reps
    k = np.arange(draws+1)
    mean = draws*p
    variance = draws*p*(1-p)*(red+blue-draws)/(red+blue-1)
    cov = -p*(1-p)/(red+blue-1)
    return dict(metrics=[metric("Espérance exacte", mean, "d × R/(R+B)"),
                         metric("Variance sans remise", variance, "Correction de population finie"),
                         metric("Covariance de deux tirages", cov, "Indicatrices rouges, positions distinctes")],
                charts=[chart("Sans remise : loi et fréquences", "Nombre de rouges", "Probabilité / fréquence",
                              [series("Hypergéométrique", k, exact), series("Simulation", k, empirical, "gold", "dots")]),
                        chart("L’effet de la remise", "Nombre de rouges", "Probabilité",
                              [series("Sans remise", k, exact), series("Avec remise : binomiale", k, independent, "rose")])],
                table=dict(headers=["k", "Sans remise", "Avec remise", "Simulation"],
                           rows=[[int(i), float(exact[i]), float(independent[i]), float(empirical[i])] for i in k]),
                notes=["Les boules sont tirées uniformément. Les échantillons répétés sont indépendants ; les tirages d’un même échantillon sans remise sont dépendants.",
                       "Exercice 4 : R = B = d = n donne E(X) = n/2. La variance plus petite n’autorise pas à remplacer la loi par une binomiale."],
                theory=dict(mean=mean, variance=variance, covariance=cov, pmf=exact.tolist()))


def fluctuations(d, rng, reps):
    n = number(d, "n", 100, 1, 1000, True)
    p = number(d, "p", .5, 0, 1)
    eps = number(d, "epsilon", .1, .001, 1)
    pmf = binomial(n, p)
    k = np.arange(n+1)
    bad = np.abs(k/n-p) >= eps-1e-14
    exact_tail = float(pmf[bad].sum())
    cheb = min(1., p*(1-p)/(n*eps*eps))
    counts = rng.binomial(n, p, reps)
    frequencies = np.bincount(counts, minlength=n+1)/reps
    path = rng.binomial(1, p, reps)
    t = np.unique(np.r_[1, np.geomspace(1, reps, 260).astype(int), reps])
    running = np.cumsum(path)[t-1]/t
    band = np.sqrt(p*(1-p)/(.05*t))
    # Bande point par point issue de BT, pas une garantie simultanée sur la trajectoire.
    normal = []
    if 0 < p < 1:
        sd = math.sqrt(n*p*(1-p))
        cdf = lambda x: .5*(1+math.erf(x/math.sqrt(2)))
        normal = [series("Normale, correction de continuité", k,
                         [cdf((i+.5-n*p)/sd)-cdf((i-.5-n*p)/sd) for i in k], "rose")]
    ci = wilson(int(path.sum()), reps)
    return dict(metrics=[metric("P(|K/n − p| ≥ ε)", exact_tail, "Somme binomiale, en virgule flottante"),
                         metric("Borne de Tchebychev", cheb, "p(1−p)/(nε²), plafonnée à 1"),
                         metric("Fréquence après N essais", path.mean(), "Un autre échantillon que les blocs de taille n")],
                charts=[chart("Loi binomiale : compter les succès", "K", "Probabilité / fréquence",
                              [series("Binomiale", k, pmf), series("Simulation", k, frequencies, "gold", "dots")]+normal),
                        chart("Loi des grands nombres : une trajectoire", "Nombre d’essais", "Fréquence",
                              [series("Fréquence", t, running), series("p", t, t*0+p, "rose"),
                               series("BT : borne haute ponctuelle à 95 %", t, np.minimum(1, p+band), "gold"),
                               series("BT : borne basse ponctuelle à 95 %", t, np.maximum(0, p-band), "gold")], ylim=[0, 1])],
                table=dict(headers=["Indicateur", "Valeur"], rows=[["E(K)", n*p], ["V(K)", n*p*(1-p)],
                    ["E(Sₙ), marche ±1", n*(2*p-1)], ["V(Sₙ)", 4*n*p*(1-p)],
                    ["Wilson 95 % : borne basse", ci[0]], ["Wilson 95 % : borne haute", ci[1]]]),
                notes=["Le TP correspond à Sₙ = 2K−n, avec p = 1/2. Une marche de longueur paire peut revenir en 0 ; de longueur impaire, non.",
                       "La bande BT vaut pour chaque instant fixé : elle n’est pas une bande de confiance simultanée. Wilson a un niveau nominal approximatif. La normale peut être mauvaise lorsque np ou n(1−p) est petit."],
                theory=dict(tail=exact_tail, chebyshev=cheb, pmf=pmf.tolist(), wilson=ci))


def polarization_moments(c, lam, steps, order=4):
    """Propagation exacte des moments par l’opérateur de transition polynomial."""
    a = 1-lam
    values = np.zeros((steps+1, order+1))
    values[0] = [c**k for k in range(order+1)]
    for t in range(steps):
        values[t+1, 0] = 1
        for k in range(1, order+1):
            values[t+1, k] = a**k*values[t, k] + sum(
                math.comb(k, j)*lam**(k-j)*a**j*values[t, j+1] for j in range(k))
    return values


def polarisation(d, rng, reps):
    c = number(d, "c", .35, .01, .99)
    lam = number(d, "lambda", .25, .01, .99)
    n = number(d, "steps", 100, 0, 500, True)
    eps = number(d, "epsilon", .1, .01, .49)
    x = np.full(reps, c)
    tracked = np.empty((min(12, reps), n+1))
    tracked[:, 0] = c
    for t in range(n):
        x = (1-lam)*x + lam*(rng.random(reps) < x)
        tracked[:, t+1] = x[:len(tracked)]
    moments = polarization_moments(c, lam, n)
    defect = c*(1-c)*(1-lam*lam)**n
    bound = min(1., defect/(eps*(1-eps)))
    interior = float(np.mean((x >= eps) & (x <= 1-eps)))
    grid = np.arange(n+1)
    hist = histogram(x, 32, (0, 1), "État à l’étape n")
    return dict(metrics=[metric("E(Xₙ), exacte", c, "La moyenne reste constante"),
                         metric("E[Xₙ(1−Xₙ)], exacte", defect, "c(1−c)(1−λ²)ⁿ"),
                         metric("Masse observée dans [ε,1−ε]", interior, f"Borne théorique : {bound:.6g}")],
                charts=[chart("Douze trajectoires, une moyenne conservée", "Étape", "Xₙ",
                              [series(f"Trajectoire {i+1}", grid, row, "mint") for i, row in enumerate(tracked)]
                              +[series("E(Xₙ) = c", grid, grid*0+c, "rose")], ylim=[0, 1]),
                        chart("Concentration aux extrémités", "État Xₙ", "Masse par classe / masse limite",
                              [hist, series("Limite Bernoulli : masses 1−c et c", [0, 1], [1-c, c], "green", "stems")], xlim=[-.04, 1.04])],
                table=dict(headers=["Moment", "Exact à l’étape n", "Simulation", "Limite"],
                           rows=[[f"E(Xₙ^{k})", float(moments[-1, k]), float(np.mean(x**k)), c] for k in range(1, 5)]),
                notes=["Xₙ₊₁ = (1−λ)Xₙ + λBₙ₊₁, où conditionnellement à Xₙ=x, Bₙ₊₁ suit Bernoulli(x). Ces B ne sont pas des tirages indépendants de paramètre c.",
                       "Les barres dorées sont des fréquences par classe ; les deux tiges vertes sont les masses de la loi limite, pas une densité. Une trajectoire seule ne révèle pas la moyenne de la population."],
                theory=dict(mean=c, variance=c*(1-c)-defect, defect=defect, interior_bound=bound,
                            moments=moments[-1].tolist()), paths=tracked.tolist(), terminal=x[:100].tolist())


def order_cdf(n, k, grid):
    # P(U_(k) ≤ x) = P(B(n,x) ≥ k).
    return np.array([float(binomial(n, float(x))[k:].sum()) for x in grid])


def extremes(d, rng, reps):
    n = number(d, "n", 20, 1, 300, True)
    mode = choice(d, "mode", "max", ["max", "min", "ordre", "ecart"])
    k = number(d, "k", min(5, n), 1, n, True)
    theta = number(d, "theta", 1, .1, 10)
    if mode == "ecart":
        maximum = rng.beta(n, 1, reps)
        sample = n*(1-maximum)
        xmax = min(n, 7.)
        grid = np.linspace(0, xmax, 241)
        cdf = 1-np.maximum(0, 1-grid/n)**n
        pdf = np.maximum(0, 1-grid/n)**(n-1)
        # n=1 : densité 1 sur [0,1], valeurs aux bords sans effet sur la loi.
        limit_cdf = 1-np.exp(-grid)
        label = "Zₙ = n(1−Mₙ/θ)"
        mean, variance = n/(n+1), n**3/((n+1)**2*(n+2))
        models = [series("Densité exacte", grid, pdf), series("Limite Exp(1)", grid, np.exp(-grid), "rose")]
        cdfs = [series("Répartition exacte", grid, cdf), series("Limite Exp(1)", grid, limit_cdf, "rose")]
        domain = (0, xmax)
    else:
        rank = n if mode == "max" else 1 if mode == "min" else k
        sample = theta*rng.beta(rank, n+1-rank, reps)
        u = np.linspace(0, 1, 241)
        grid = theta*u
        cdf = u**n if rank == n else 1-(1-u)**n if rank == 1 else order_cdf(n, rank, u)
        coefficient = rank*math.comb(n, rank)/theta
        pdf = coefficient*u**(rank-1)*(1-u)**(n-rank)
        mean = theta*rank/(n+1)
        variance = theta*theta*rank*(n+1-rank)/((n+1)**2*(n+2))
        label = "Mₙ" if mode == "max" else "mₙ" if mode == "min" else f"U_({rank})"
        models, cdfs = [series("Densité exacte", grid, pdf)], [series("Répartition exacte", grid, cdf)]
        domain = (0, theta)
    hist = histogram(sample, 32, domain, density=True)
    example_max = float(sample[0]) if mode == "max" else None
    example_rows = [] if example_max is None else [
        ["Premier maximum simulé", example_max],
        ["Estimation corrigée de θ", (n+1)*example_max/n],
        ["IC exact 95 % : borne basse", example_max],
        ["IC exact 95 % : borne haute", example_max/(.05**(1/n))]]
    return dict(metrics=[metric("Espérance exacte", mean, label), metric("Variance exacte", variance, label),
                         metric("Moyenne simulée", sample.mean(), f"{reps} échantillons indépendants")],
                charts=[chart("Statistique d’ordre : densité", label, "Densité", [hist]+models, xlim=list(domain)),
                        chart("Statistique d’ordre : répartition", label, "P(X ≤ x)", cdfs+
                              [series("Répartition empirique", grid, empirical_cdf(sample, grid), "gold", "step")], ylim=[0, 1])],
                table=dict(headers=["Propriété du maximum sur [0,θ]", "Valeur"], rows=[
                    ["E(Mₙ)", theta*n/(n+1)], ["Biais de Mₙ pour θ", -theta/(n+1)],
                    ["Facteur de correction sans biais", (n+1)/n],
                    ["P(Mₙ ≤ 0,9θ)", .9**n]]+example_rows),
                notes=["Le tirage Beta est une simulation directe de la loi de la statistique d’ordre ; les n valeurs uniformes sont intégrées analytiquement.",
                       "Les densités peuvent dépasser 1. En mode écart, seules les classes visibles [0,min(n,7)] sont tracées ; leur intégrale peut être inférieure à 1, sans renormalisation artificielle."],
                theory=dict(mean=mean, variance=variance, cdf=cdf.tolist()))


def arcsine_cdf(x):
    a = np.clip(np.asarray(x, dtype=float), -2, 2)
    return .5+np.arcsin(a/2)/np.pi


def semicircle_cdf(x):
    a = np.clip(np.asarray(x, dtype=float), -2, 2)
    return .5+(a*np.sqrt(np.maximum(0, 4-a*a))/4+np.arcsin(a/2))/np.pi


def path_matrix(n):
    return np.diag(np.ones(n-1), 1)+np.diag(np.ones(n-1), -1)


def arcsinus(d, rng, reps):
    n = number(d, "n", 60, 2, 300, True)
    mode = number(d, "mode", min(3, n), 1, n, True)
    power = number(d, "power", 4, 1, 10, True)
    eigenvalues = np.sort(2*np.cos(np.arange(1, n+1)*np.pi/(n+1)))
    sample = rng.choice(eigenvalues, reps)
    edges = np.linspace(-2, 2, 33)
    centers = (edges[1:]+edges[:-1])/2
    masses = np.diff(arcsine_cdf(edges))
    finite, _ = np.histogram(eigenvalues, bins=edges)
    grid = np.linspace(-2, 2, 501)
    vector = np.sqrt(2/(n+1))*np.sin(np.arange(1, n+1)*mode*np.pi/(n+1))
    lam = 2*math.cos(mode*math.pi/(n+1))
    residual = float(np.linalg.norm(path_matrix(n)@vector-lam*vector))
    limit = 0 if power % 2 else math.comb(power, power//2)
    return dict(metrics=[metric("Valeur propre du mode choisi", lam, "2 cos(kπ/(n+1))"),
                         metric("Moment spectral choisi", np.mean(eigenvalues**power), f"Limite arcsinus : {limit}"),
                         metric("Résidu du vecteur propre", residual, "‖Tₙv − λv‖₂, arrondi numérique")],
                charts=[chart("Loi arcsinus : masses par intervalle", "Valeur propre / Xₙ", "Masse par classe",
                              [series("Spectre exact de Tₙ", centers, finite/n), series("Loi limite arcsinus", centers, masses, "rose"),
                               histogram(sample, 32, (-2, 2), "Simulation", "gold")], xlim=[-2, 2]),
                        chart("De la loi discrète à la loi continue", "x", "P(X ≤ x)",
                              [series("Arcsinus", grid, arcsine_cdf(grid), "rose"),
                               series("Spectre fini, répartition exacte", grid, empirical_cdf(eigenvalues, grid), "green", "step")], ylim=[0, 1]),
                        chart("Un mode propre du chemin", "Sommet j", "Composante vⱼ",
                              [series(f"Mode k = {mode}, vecteur normé", np.arange(1, n+1), vector)])],
                table=dict(headers=["Puissance r", "(1/n) Tr(Tₙʳ)", "Moment arcsinus"], rows=[
                    [r, float(np.mean(eigenvalues**r)), 0 if r%2 else math.comb(r, r//2)] for r in range(1, 9)]),
                notes=["Uₙ est uniforme DISCRÈTE sur {1,…,n}. Xₙ = 2cos(πUₙ/(n+1)). Tₙ est la matrice d’adjacence d’un chemin, sans facteur 1/√n.",
                       "On compare des masses intégrées par classe : la densité arcsinus est non bornée aux bords ±2. Les valeurs propres sont comptées avec leur multiplicité."],
                theory=dict(eigenvalues=eigenvalues.tolist(), limit_moment=limit, vector=vector.tolist(),
                            mode_eigenvalue=lam, residual=residual, bin_masses=masses.tolist()))


def wigner_matrix(n, law, rng):
    indices = np.triu_indices(n)
    size = len(indices[0])
    if law == "gauss":
        values = rng.normal(size=size)
    elif law == "signes":
        values = 2*rng.integers(0, 2, size)-1
    else:
        values = rng.uniform(-math.sqrt(3), math.sqrt(3), size)
    matrix = np.zeros((n, n))
    matrix[indices] = values
    matrix += np.triu(matrix, 1).T
    return matrix/math.sqrt(n)


def wigner(d, rng, reps):
    n = number(d, "n", 80, 8, 180, True)
    matrices = number(d, "matrices", 3, 1, 8, True)
    law = choice(d, "law", "gauss", ["gauss", "signes", "uniforme"])
    spectra = [np.linalg.eigvalsh(wigner_matrix(n, law, rng)) for _ in range(matrices)]
    all_values = np.concatenate(spectra)
    domain = (min(-2.6, float(all_values.min())-.1), max(2.6, float(all_values.max())+.1))
    grid = np.linspace(*domain, 401)
    edges = np.linspace(*domain, 33)
    centers = (edges[1:]+edges[:-1])/2
    masses = np.diff(semicircle_cdf(edges))
    arc_masses = np.diff(arcsine_cdf(edges))
    counts, _ = np.histogram(all_values, bins=edges)
    # Erreur de répartition calculée aux sauts, à gauche ET à droite.
    ordered = np.sort(all_values)
    F = semicircle_cdf(ordered)
    distance = float(max(np.max(np.abs(np.arange(1, len(F)+1)/len(F)-F)),
                         np.max(np.abs(np.arange(len(F))/len(F)-F))))
    rows = []
    for power in range(1, 9):
        values = np.array([np.mean(s**power) for s in spectra])
        target = 0 if power%2 else math.comb(power, power//2)//(power//2+1)
        se = float(values.std(ddof=1)/math.sqrt(matrices)) if matrices > 1 else None
        rows.append([power, float(values.mean()), target, se])
    return dict(metrics=[metric("Moment spectral d’ordre 2", np.mean(all_values**2), "Limite demi-cercle : 1 ; arcsinus : 2"),
                         metric("Écart de répartition", distance, "Demi-cercle, spectres regroupés"),
                         metric("Plus grande |valeur propre|", np.max(np.abs(all_values)), "±2 est un bord limite, pas une borne finie")],
                charts=[chart("Deux lois, deux modèles", "Valeur propre", "Masse par classe",
                              [series("Matrices simulées", centers, counts/len(all_values), "green", "bars"),
                               series("Demi-cercle", centers, masses, "rose"), series("Arcsinus, pour comparaison", centers, arc_masses, "gold")]),
                        chart("Répartition spectrale empirique", "x", "Part des valeurs propres ≤ x",
                              [series("Spectres regroupés", grid, empirical_cdf(all_values, grid), "green", "step"),
                               series("Demi-cercle", grid, semicircle_cdf(grid), "rose")], ylim=[0, 1])],
                table=dict(headers=["r", "Moyenne de Tr(Aʳ)/n", "Moment demi-cercle", "Erreur-type entre matrices"], rows=rows),
                notes=["Les entrées du triangle supérieur, diagonale comprise, sont indépendantes, centrées, de variance 1, puis la matrice est symétrisée et divisée par √n. Ce modèle gaussien n’est pas le GOE standard (variance diagonale différente).",
                       "L’indépendance porte sur les matrices répétées et leurs entrées supérieures. Les valeurs propres d’une matrice sont dépendantes : aucune erreur-type fondée sur n valeurs propres indépendantes n’est utilisée.",
                       "Le théorème de Wigner est admis en approfondissement. Pour passer des moments moyens à une convergence en probabilité, un contrôle des fluctuations est nécessaire."],
                theory=dict(spectra=[s.tolist() for s in spectra], moment_rows=rows, distance=distance))


LABS = {"urne": urne, "fluctuations": fluctuations, "polarisation": polarisation,
        "extremes": extremes, "arcsinus": arcsinus, "wigner": wigner}


def execute(data):
    lab = choice(data, "lab", "polarisation", LABS)
    seed = number(data, "seed", 742, 0, 2**32-1, True)
    reps = number(data, "reps", 4000, 100, 10000, True)
    result = LABS[lab](data, np.random.default_rng(seed), reps)
    result.update(lab=lab, seed=seed, reps=reps, parameters=data)
    return result
