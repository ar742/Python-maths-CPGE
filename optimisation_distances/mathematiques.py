"""Optimisation euclidienne : projections, extrema et bornes primal-dual.

Python 3.10+, NumPy ; aucune dépendance à un optimiseur externe.
Les bornes sont évaluées en virgule flottante, sans arithmétique d'intervalles.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.polynomial import Polynomial, Legendre


def nombre(value, mini=-100, maxi=100):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Un nombre réel est attendu.")
    value = float(value)
    if not math.isfinite(value) or not mini <= value <= maxi:
        raise ValueError(f"Le nombre doit être fini, entre {mini:g} et {maxi:g}.")
    return value


def entier(value, mini, maxi):
    if type(value) is not int or not mini <= value <= maxi:
        raise ValueError(f"Un entier entre {mini} et {maxi} est attendu.")
    return value


def vecteur(value, mini=-20, maxi=20):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError("Trois coordonnées sont attendues.")
    return np.array([nombre(x, mini, maxi) for x in value])


def rotation(angles):
    """Angles en degrés ; R = Rz Ry Rx, vecteurs colonnes."""
    x, y, z = np.radians(angles)
    cx, sx, cy, sy, cz, sz = math.cos(x), math.sin(x), math.cos(y), math.sin(y), math.cos(z), math.sin(z)
    return np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1.]]) @ np.array([
        [cy, 0, sy], [0, 1., 0], [-sy, 0, cy]]) @ np.array([
        [1., 0, 0], [0, cx, -sx], [0, sx, cx]])


def ellipsoide(data):
    c = vecteur(data.get("centre", [0, 0, 0]))
    a = vecteur(data.get("axes", [2, 1.2, .8]), .15, 5)
    angles = vecteur(data.get("angles", [0, 0, 0]), -180, 180)
    r = rotation(angles)
    return c, a, r, r @ np.diag(a)


def quadrature(L, poids=0):
    x, w = np.polynomial.legendre.leggauss(96)
    t = (x+1)*L/2
    return t, w*L/2*(1+poids*t/L)


def affine_exact(L):
    a = 12/L**3*(L*math.sin(L)/2+math.cos(L)-1)
    return a, math.sin(L)/L-a*L/2


def affine_uniforme(L):
    a = (math.cos(L)-1)/L
    t = math.asin(-a)
    gap = math.cos(t)-1-a*t
    return {"a": a, "b": 1+gap/2, "erreur": gap/2, "contact": t}


def norme_uniforme_affine(a, b, L):
    points = [0., L]
    if -math.sin(L) <= a <= 0:
        points.append(math.asin(-a))
    return max(abs(math.cos(t)-a*t-b) for t in points)


def approximation(data):
    L = nombre(data.get("L", math.pi/2), .3, math.pi/2)
    deg = entier(data.get("degre", 1), 0, 6)
    k = nombre(data.get("poids", 0), -.8, 4)
    t, w = quadrature(L, k)
    design = np.polynomial.legendre.legvander(2*t/L-1, deg)
    design *= np.sqrt((2*np.arange(deg+1)+1)/L)
    q, r = np.linalg.qr(design*np.sqrt(w)[:, None], mode="reduced")
    coeff = np.linalg.solve(r, q.T @ (np.cos(t)*np.sqrt(w)))
    leg = Legendre(coeff*np.sqrt((2*np.arange(deg+1)+1)/L), domain=[0, L])
    poly = leg.convert(kind=Polynomial)
    residual = np.cos(t)-leg(t)
    I = float(np.dot(w, residual**2))
    orth = (design.T @ (w*residual)).tolist()
    gram = np.array([[L**(i+j+1)*(1/(i+j+1)+k/(i+j+2))
                      for j in range(deg+1)] for i in range(deg+1)])
    xs = np.linspace(0, L, 301)
    vals = leg(xs)
    uniforme = affine_uniforme(L)
    if deg <= 1:
        a = float(poly.coef[1]) if deg == 1 else 0.
        sup = norme_uniforme_affine(a, float(poly.coef[0]), L)
        sup_upper = sup
    else:
        sup = float(np.max(np.abs(np.cos(xs)-vals)))
        lip = 1+sum(i*abs(v)*L**(i-1) for i, v in enumerate(poly.coef) if i)
        sup_upper = sup+lip*L/600
    trial_a = nombre(data.get("a", -.1), -4, 4)
    trial_b = nombre(data.get("b", .6), -4, 4)
    H = 2*np.array([[gram[1, 1] if deg else L**3*(1/3+k/4), L**2*(1/2+k/3)],
                   [L**2*(1/2+k/3), L*(1+k/2)]])
    # Objectif affine pour le paysage, même si l'approximation a degré > 1.
    rhs = np.array([np.dot(w, t*np.cos(t)), np.dot(w, np.cos(t))])
    optimum = np.linalg.solve(H, 2*rhs)
    v = np.array([trial_a, trial_b])
    history = []
    step = .8/np.linalg.eigvalsh(H)[-1]
    for _ in range(140):
        history.append([*v.tolist(), float(np.dot(w, (np.cos(t)-v[0]*t-v[1])**2))])
        v -= step*(H @ v-2*rhs)
    return {"x": xs.tolist(), "cos": np.cos(xs).tolist(), "projection": vals.tolist(),
            "uniforme": (uniforme["a"]*xs+uniforme["b"]).tolist(), "minimax": uniforme,
            "coefficients": poly.coef.tolist(), "I": I, "distance": math.sqrt(I),
            "sup": sup, "sup_upper": sup_upper, "orthogonalite": orth,
            "gram": gram.tolist(), "condition_gram": float(np.linalg.cond(gram)),
            "condition_design": float(np.linalg.cond(r)), "hessienne": H.tolist(),
            "affine_optimum": optimum.tolist(), "descente": history,
            "trial": (trial_a*xs+trial_b).tolist(), "L": L, "degre": deg, "poids": k}


def decomposition(m):
    m = np.asarray(m)
    return (m+m.T)/2, (m-m.T)/2


def cellules(m):
    return [[[float(z.real), float(z.imag)] for z in row] for row in np.asarray(m, dtype=complex)]


def matrices(data):
    theta = math.radians(nombre(data.get("theta", 55), -180, 180))
    c, s = math.cos(theta), math.sin(theta)
    m = np.array([[1, 0, 0], [0, c, s], [0, -s, c]])
    sym, skew = decomposition(m)
    n = entier(data.get("n", 3), 2, 10)
    complex_mode = data.get("complexe", False)
    if type(complex_mode) is not bool:
        raise ValueError("Le choix réel/complexe doit être booléen.")
    eta = nombre(data.get("eta", 0), -2, 2)
    phase = math.radians(nombre(data.get("phase", 45), -180, 180)) if complex_mode else 0
    result = {"rotation": cellules(m), "symetrique": cellules(sym), "antisymetrique": cellules(skew),
              "distance_rotation": float(np.linalg.norm(skew)), "n": n,
              "dimension": n*(n+1)//2, "vide": n % 2 == 1}
    if n % 2:
        result.update(distance_ensemble=None, norme=None, matrice=None)
        return result
    a = np.zeros((n, n), dtype=complex)
    scales = np.ones(n//2, dtype=complex)
    if n >= 4:
        scales[0] = np.exp(eta+1j*phase)
        scales[1] = 1/scales[0]
    for j, z in enumerate(scales):
        a[2*j, 2*j+1], a[2*j+1, 2*j] = z, -z
    det = np.linalg.det(a)
    result.update(distance_ensemble=math.sqrt(n), norme=float(np.linalg.norm(a)),
                  matrice=cellules(a), determinant=[float(det.real), float(det.imag)],
                  valeurs_propres=np.linalg.eigvalsh(a.conj().T @ a).tolist(),
                  egalite=float(np.linalg.norm(a.conj().T @ a-np.eye(n))) < 1e-10)
    return result


def produit(data):
    axes = vecteur(data.get("axes", [2, 1.2, .8]), .15, 5)
    puissances = vecteur(data.get("puissances", [1, 1, 1]), .2, 5)
    longitude = math.radians(nombre(data.get("longitude", 25), -180, 180))
    latitude = math.radians(nombre(data.get("latitude", 20), -90, 90))
    u = np.array([math.cos(latitude)*math.cos(longitude),
                  math.cos(latitude)*math.sin(longitude), math.sin(latitude)])
    fractions = puissances/sum(puissances)
    extremal = axes*np.sqrt(fractions)
    maximum = float(np.prod(extremal**puissances))
    point = axes*u
    value = float(np.prod(abs(point)**puissances))
    points = [(extremal*np.array([i, j, k])).tolist()
              for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)]
    return {"axes": axes.tolist(), "maximum": maximum, "valeur": value,
            "point": point.tolist(), "maximiseurs": points, "fractions": fractions.tolist(),
            "volume_boite": float(8*np.prod(axes)/(3*math.sqrt(3))),
            "boite": (axes/math.sqrt(3)).tolist(), "puissances": puissances.tolist()}


def extremum_surface(p, c, axes, r, maximum=False):
    """Extremum global ; inclut les cas singuliers des multiplicateurs.

    Minimum : D+mu I >= 0. Maximum : lambda I-D >= 0.
    Ces conditions donnent une preuve globale par différence des objectifs.
    """
    p, c, axes, r = map(np.asarray, (p, c, axes, r))
    D = axes**2
    q = axes*(r.T @ (c-p))
    pole = float(max(D) if maximum else min(D))
    diff = pole-D if maximum else D-pole
    group = diff <= 1e-14*max(1., pole)
    diff[group] = 0
    sign = 1 if maximum else -1
    norm_q_group = float(np.linalg.norm(q[group]))
    base = np.zeros(3)
    base[~group] = sign*q[~group]/diff[~group]
    base_norm2 = float(base @ base)
    hard = bool(norm_q_group <= 1e-14*max(1., np.linalg.norm(q)) and base_norm2 <= 1)
    if hard:
        t = 0.
        u = base
        u[np.flatnonzero(group)[0]] = math.sqrt(max(0., 1-base_norm2))
    else:
        lo, hi = 0., max(1., np.linalg.norm(q), float(max(diff)))

        def norm2(t):
            return float(np.sum((q/(diff+t))**2))

        while norm2(hi) > 1:
            hi *= 2
        for _ in range(90):
            mid = (lo+hi)/2
            if norm2(mid) > 1:
                lo = mid
            else:
                hi = mid
        t = (lo+hi)/2
        u = sign*q/(diff+t)
    t = float(t)
    multiplier = float(pole+t if maximum else t-pole)
    point = c+r @ (axes*u)
    residual = (multiplier-D)*u-q if maximum else (D+multiplier)*u+q
    return {"point": point.tolist(), "u": u.tolist(), "distance": float(np.linalg.norm(point-p)),
            "multiplicateur": multiplier, "cas_singulier": hard,
            "stationnarite": float(np.linalg.norm(residual)),
            "contrainte": float(abs(u @ u-1)), "borne_spectrale": t}


def projection_solide(p, c, axes, r):
    u = (r.T @ (p-c))/axes
    if u @ u <= 1:
        return np.array(p, dtype=float)
    return np.array(extremum_surface(p, c, axes, r)["point"])


def point_ellipsoide(data):
    c, axes, r, b = ellipsoide(data)
    p = vecteur(data.get("point", [3, 2, 1]))
    u = (r.T @ (p-c))/axes
    inside = bool(u @ u <= 1)
    nearest = extremum_surface(p, c, axes, r)
    farthest = extremum_surface(p, c, axes, r, True)
    return {"centre": c.tolist(), "axes": axes.tolist(), "B": b.tolist(), "point": p.tolist(),
            "interieur": inside, "niveau": float(u @ u), "minimum": nearest,
            "maximum": farthest, "distance_solide": 0. if inside else nearest["distance"]}


def distance_ellipsoides(e1, e2, tolerance=1e-8, iterations=1200):
    """Distance des SOLIDES. Bornes via faisabilité et fonctions support.

    Les projections alternées ne prouvent pas seules l'optimalité. La borne
    duale g(n) contrôle l'écart à l'optimum, y compris à l'arrêt anticipé.
    """
    c1, a1, r1, b1 = ellipsoide(e1)
    c2, a2, r2, b2 = ellipsoide(e2)
    Q1, Q2 = b1 @ b1.T, b2 @ b2.T
    y = c2.copy()
    best_lower = 0.
    best_n = np.array([1., 0, 0])
    history = []
    converged = False
    scale = max(1., np.linalg.norm(c2-c1), max(a1), max(a2))
    for i in range(iterations):
        x = projection_solide(y, c1, a1, r1)
        y = projection_solide(x, c2, a2, r2)
        delta = y-x
        upper = float(np.linalg.norm(delta))
        if upper > 1e-14*scale:
            n = delta/upper
            lower = float(n @ (c2-c1)-math.sqrt(n @ Q1 @ n)-math.sqrt(n @ Q2 @ n))
            if lower > best_lower:
                best_lower, best_n = lower, n.copy()
        gap = upper-best_lower
        if i < 5 or i % 10 == 0:
            history.append([i+1, best_lower, upper])
        if gap <= tolerance*scale:
            converged = True
            break
    history.append([i+1, best_lower, upper])
    h1 = float(best_n @ c1+math.sqrt(best_n @ Q1 @ best_n))
    l2 = float(best_n @ c2-math.sqrt(best_n @ Q2 @ best_n))
    level = (h1+l2)/2
    signed_gap = l2-h1
    separated = bool(best_lower > tolerance*scale)
    return {"e1": {"centre": c1.tolist(), "B": b1.tolist(), "axes": a1.tolist()},
            "e2": {"centre": c2.tolist(), "B": b2.tolist(), "axes": a2.tolist()},
            "p1": x.tolist(), "p2": y.tolist(), "inferieure": best_lower, "superieure": upper,
            "ecart": gap, "iterations": i+1, "converge": converged, "separes": separated,
            "normal": best_n.tolist(), "niveau_plan": level, "marge": max(0., signed_gap/2),
            "w_svm": (2*best_n/signed_gap).tolist() if separated else None,
            "b_svm": -2*level/signed_gap if separated else None,
            "faisabilite": [float(np.linalg.norm((r1.T @ (x-c1))/a1)),
                             float(np.linalg.norm((r2.T @ (y-c2))/a2))], "historique": history}


def paire(data):
    if not isinstance(data.get("e1"), dict) or not isinstance(data.get("e2"), dict):
        raise ValueError("Deux ellipsoïdes sont attendus.")
    return distance_ellipsoides(data["e1"], data["e2"])


def execute(data):
    actions = {"approximation": approximation, "matrices": matrices, "produit": produit,
               "point": point_ellipsoide, "paire": paire}
    if data.get("action") not in actions:
        raise ValueError("Expérience inconnue.")
    return actions[data["action"]](data)
