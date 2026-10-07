"""Optique scalaire, Jones, ABCD et χ² : modèles explicites sans SciPy.

Les champs complexes restent internes. La convention temporelle des amplitudes
de Jones est exp(−iωt). np.sinc(x) signifie sin(πx)/(πx).
"""
from __future__ import annotations

import math
from numbers import Real
import numpy as np

try:
    from .catalogue_ondes import LAB_BY_ID
    from .science import metric, series, chart, scene, clean
except ImportError:
    from catalogue_ondes import LAB_BY_ID
    from science import metric, series, chart, scene, clean

C = 299792458.0
EPS0 = 8.8541878188e-12
H = 6.62607015e-34
ARCSEC = 180.0 * 3600.0 / np.pi
AIRY_ZERO = 3.8317059702075125
RAYLEIGH = AIRY_ZERO / np.pi


def validated(lab_id, supplied):
    if lab_id not in LAB_BY_ID:
        raise ValueError("Expérience d'ondes inconnue.")
    if supplied is None:
        supplied = {}
    if not isinstance(supplied, dict):
        raise ValueError("Les paramètres doivent former un objet.")
    controls = LAB_BY_ID[lab_id]["controls"]
    if set(supplied) - {c["key"] for c in controls}:
        raise ValueError("Un paramètre est inconnu.")
    result = {}
    for control in controls:
        key = control["key"]
        value = supplied.get(key, control["value"])
        if control["type"] == "select":
            if not isinstance(value, str) or value not in [o["value"] for o in control["options"]]:
                raise ValueError("Choix invalide : " + key)
        else:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValueError("Nombre attendu : " + key)
            try:
                value = float(value)
            except (OverflowError, ValueError):
                raise ValueError("Nombre fini attendu : " + key) from None
            if not math.isfinite(value) or not control["min"] <= value <= control["max"]:
                raise ValueError("Nombre hors domaine : " + key)
            if key in ("count", "order") and not value.is_integer():
                raise ValueError("Un entier est attendu : " + key)
        result[key] = value
    return result


def calculate(lab_id, params=None):
    p = validated(lab_id, params)
    return clean(dict(lab=lab_id, params=p, **COMPUTE[lab_id](p)))


def young_intensity(x, wavelength, separation, width, distance, ratio=1.0,
                    phase=0.0, visibility=1.0):
    """Intensité divisée par le maximum axial d'une fente : I₁(0)."""
    x = np.asarray(x)
    envelope = np.sinc(width * x / (wavelength * distance)) ** 2
    interference = 1 + ratio + 2 * math.sqrt(ratio) * visibility * np.cos(
        2 * np.pi * separation * x / (wavelength * distance) + phase)
    return envelope * interference


def young(p):
    lam, a, b, D = p["wavelength"] * 1e-9, p["separation"] * 1e-3, p["width"] * 1e-3, p["distance"]
    ratio = 0.0 if p["mode"] == "single" else p["ratio"]
    coherence = 0.0 if p["mode"] == "independent" else 1.0
    interfringe, halfwidth = lam * D / a, lam * D / b
    extent = min(2.2 * halfwidth, 30 * interfringe)
    x = np.linspace(-extent, extent, 2001)
    intensity = young_intensity(x, lam, a, b, D, ratio, np.deg2rad(p["phase"]), coherence)
    envelope = (1 + ratio + 2 * math.sqrt(ratio) * coherence) * np.sinc(b*x/(lam*D))**2
    contrast = 2*math.sqrt(ratio)*coherence/(1+ratio)
    return dict(
        metrics=[metric("Interfrange i = λD/a", interfringe*1e3, "mm"),
                 metric("Largeur entre les deux premiers zéros", 2*halfwidth*1e3, "mm"),
                 metric("Contraste intrinsèque", contrast),
                 metric("Maximum axial possible / I₁(0)", 1+ratio+2*math.sqrt(ratio)*coherence)],
        charts=[chart("Deux échelles : interférence et diffraction", "Position x (mm)", "I / I₁(0)",
                      series("Intensité", x*1e3, intensity), series("Enveloppe supérieure", x*1e3, envelope))],
        scene=scene("fringes", "Deux fentes, un écran", "L'éclairement est calculé ; l'exposition visuelle est commune au profil et à l'écran.",
                    x_mm=x*1e3, intensity=intensity, wavelength_nm=p["wavelength"],
                    slits_mm=[-a*500, a*500] if p["mode"] != "single" else [0],
                    slit_width_mm=p["width"], screen_distance_m=D, variant="young"),
        steps=["δ(x) ≃ ax/D et Δφ = 2πδ/λ + φ₀.",
               "Ajouter les amplitudes pour une source commune ; ajouter les intensités pour deux sources indépendantes.",
               "I/I₁(0) = sinc²(bx/(λD)) [1 + r + 2√r |γ| cos Δφ], où sinc(u) = sin(πu)/(πu).",
               "Les zéros de l'enveloppe sont à ±λD/b : sa largeur totale est 2λD/b."],
        assumptions=["Fraunhofer scalaire, fentes longues identiques, b < a, illumination uniforme.",
                     "L'observation est réalisée au plan focal d'une lentille de focale équivalente D, ou à distance suffisante pour Fraunhofer.",
                     "Les ordres de grandeur sont paraxiaux ; la phase ajoutée ne change pas la largeur de l'enveloppe."])


def grating_factor(q, count):
    """|Σ exp(2πipq)|²/N² ; valeurs exactes aux ordres entiers."""
    q = np.asarray(q, dtype=float)
    reduced = q - np.rint(q)
    return (np.sinc(count * reduced) / np.sinc(reduced))**2


def grating_intensity(theta, wavelength, pitch, count, fill, incidence=0.0):
    q = pitch * (np.sin(theta) - math.sin(incidence)) / wavelength
    return np.sinc(fill*q)**2 * grating_factor(q, count)


def reseau(p):
    lam, d, N = p["wavelength"]*1e-9, p["pitch"]*1e-6, int(p["count"])
    m, theta0 = int(p["order"]), np.deg2rad(p["incidence"])
    delta_lam = p["doublet"]*1e-9
    l1, l2 = lam-delta_lam/2, lam+delta_lam/2
    sincenter = math.sin(theta0)+m*lam/d
    present = abs(sincenter) < 1
    if present:
        center = math.asin(sincenter)
        qextent = max(7/N, 2*m*delta_lam/lam, .002)
        qmin = max(m-qextent, d*(-1-math.sin(theta0))/lam)
        qmax = min(m+qextent, d*(1-math.sin(theta0))/lam)
        q = np.linspace(qmin, qmax, 2001)
        theta = np.arcsin(np.clip(math.sin(theta0)+q*lam/d, -1, 1))
        peak1 = grating_intensity(theta, l1, d, N, p["fill"], theta0)
        peak2 = grating_intensity(theta, l2, d, N, p["fill"], theta0)
        total = (peak1+peak2)/2
        dispersion = m/(d*math.cos(center))
        center_deg = math.degrees(center)
        label = "Zoom autour de l'ordre m = " + str(m)
    else:
        theta = np.deg2rad(np.linspace(-89, 89, 2001))
        peak1 = grating_intensity(theta, l1, d, N, p["fill"], theta0)
        peak2 = grating_intensity(theta, l2, d, N, p["fill"], theta0)
        total = (peak1+peak2)/2
        dispersion, center_deg, label = 0.0, "Absent", "Champ angulaire : l'ordre demandé n'existe pas"
    maxorder = math.floor(d*(1-math.sin(theta0))/lam)
    minorder = math.ceil(d*(-1-math.sin(theta0))/lam)
    angles, orders = [], []
    for order in range(minorder, maxorder+1):
        argument = math.sin(theta0)+order*lam/d
        if abs(argument) <= 1:
            orders.append(order); angles.append(math.degrees(math.asin(argument)))
    resolving = m*N
    return dict(
        metrics=[metric("Ordre demandé propagatif", "Oui" if present else "Non"),
                 metric("Angle central", center_deg, "°" if present else ""),
                 metric("Pouvoir de résolution idéal mN", resolving),
                 metric("Écart Rayleigh Δλ = λ/(mN)", lam/resolving*1e9, "nm"),
                 metric("Dispersion angulaire", dispersion*1e-9*180/np.pi, "°·nm⁻¹")],
        charts=[chart(label, "Angle θ (°)", "I / maximum N² d'une fente", series("Raie courte, poids 1/2", np.rad2deg(theta), peak1/2),
                      series("Raie longue, poids 1/2", np.rad2deg(theta), peak2/2), series("Somme incohérente du doublet", np.rad2deg(theta), total))],
        scene=scene("fringes", "Réseau et raies spectrales", "Le profil détaillé porte sur l'ordre choisi ; deux fréquences distinctes donnent une somme d'intensités.",
                    variant="grating", x_mm=np.rad2deg(theta), x_label="Angle θ (°)", intensity=total,
                    wavelength_nm=p["wavelength"], count=N, pitch_um=p["pitch"],
                    angles_deg=angles, orders=orders, selected_order=m, order_present=present),
        steps=["d(sin θ − sin θ₀) = mλ : vérifier d'abord que |sin θ| ≤ 1.",
               "Une somme géométrique donne |Σₚ exp(2πipq)|² ; aux q entiers, sa limite est exactement N².",
               "La largeur de chaque fente multiplie cette somme par sinc²((b/d)q).",
               "Le premier zéro voisin d'un ordre est à Δq = 1/N ; le critère de Rayleigh donne λ/Δλ ≃ mN."],
        assumptions=["Réseau de transmission idéal, N fentes uniformes, Fraunhofer, pas de pertes chromatiques.",
                     "Les deux raies du doublet ont des intensités égales et sont mutuellement incohérentes.",
                     "L'échelle est normalisée par le maximum N² d'une fente non enveloppée ; un ordre peut être faible ou manquant à cause de l'enveloppe."])


def apodized_amplitude(q):
    """TF de cos(πx/a) sur |x|<a/2, normalisée à son amplitude axiale."""
    q = np.asarray(q)
    return np.pi/4 * (np.sinc(q+.5)+np.sinc(q-.5))


def diffraction(p):
    lam, a, b, f = p["wavelength"]*1e-9, p["width"]*1e-3, p["height"]*1e-3, p["focal"]*1e-3
    xa, yb = lam*f/a, lam*f/b
    x = np.linspace(-3.6*xa, 3.6*xa, 151)
    y = np.linspace(-3.6*yb, 3.6*yb, 121)
    qx, qy = x/xa, y/yb
    ax = apodized_amplitude(qx) if p["aperture"] == "apodized" else np.sinc(qx)
    ay = np.ones_like(y) if p["aperture"] == "slit" else np.sinc(qy)
    image = np.outer(ay**2, ax**2)
    q = np.linspace(-5, 5, 2001)
    uniform = np.sinc(q)**2
    apodized = apodized_amplitude(q)**2
    zero_factor = 1.5 if p["aperture"] == "apodized" else 1.0
    transmitted = .5 if p["aperture"] == "apodized" else 1.0
    return dict(
        metrics=[metric("Largeur centrale horizontale entre zéros", 2*zero_factor*xa*1e3, "mm"),
                 metric("Premier zéro uniforme", xa*1e3, "mm"),
                 metric("Puissance transmise / rectangle uniforme", transmitted),
                 metric("Maximum axial / rectangle uniforme", (2/np.pi)**2 if p["aperture"] == "apodized" else 1)],
        charts=[chart("Apodisation : largeur contre lobes secondaires", "q = ax/(λf)", "I / I(0) propre à chaque pupille",
                      series("Pupille uniforme", q, uniform), series("Pupille cosinus", q, apodized))],
        scene=scene("image", "La pupille dessine son spectre", "Intensité normalisée au maximum propre à la pupille ; le bilan de puissance est indiqué séparément.",
                    variant="diffraction", x=x*1e3, y=y*1e3, x_label="x (mm)", y_label="y (mm)", intensity=image,
                    wavelength_nm=p["wavelength"], aperture=p["aperture"], width_mm=p["width"], height_mm=p["height"]),
        steps=["Au foyer image : νx = x/(λf), νy = y/(λf).",
               "Le rectangle se sépare : E ∝ ab sinc(aνx) sinc(bνy).",
               "cos(πx/a) = [exp(iπx/a)+exp(−iπx/a)]/2 : la TF est la somme de deux sinc décalés.",
               "Après normalisation axiale, A(q) = (π/4)[sinc(q+1/2)+sinc(q−1/2)]. Les points q = ±1/2 ne sont pas des singularités.",
               "Le premier zéro apodisé est q = ±3/2 ; ∫ cos²(πx/a)dx = a/2 explique la perte de puissance."],
        assumptions=["Optique scalaire monochromatique et paraxiale, lentille idéale, observation dans son plan focal.",
                     "Le choix 'fente longue' néglige la diffraction verticale.",
                     "La comparaison des profils normalisés compare leur forme ; elle ne suppose pas des puissances transmises égales."])


def rotation(angle):
    co, si = math.cos(angle), math.sin(angle)
    return np.array([[co, -si], [si, co]])


def jones_retarder(field, axis, retardance):
    basis = rotation(axis)
    return basis @ np.diag([1.0, np.exp(1j*retardance)]) @ basis.T @ field


def stokes(field):
    ex, ey = field
    total = abs(ex)**2+abs(ey)**2
    return np.array([total, abs(ex)**2-abs(ey)**2, 2*np.real(np.conj(ex)*ey), 2*np.imag(np.conj(ex)*ey)])


def polarisation(p):
    angle, axis, delay, analyzer = np.deg2rad([p["input_angle"], p["axis"], p["retardance"], p["analyzer"]])
    if p["input"] == "linear":
        field0 = np.array([1.0, 0.0], dtype=complex)
    elif p["input"] == "circular":
        field0 = np.array([1.0, 1j])/math.sqrt(2)
    else:
        field0 = np.array([1.0, .5j])/math.sqrt(1.25)
    field0 = rotation(angle) @ field0
    field = jones_retarder(field0, axis, delay)
    s = stokes(field)
    t = np.linspace(0, 2*np.pi, 241)
    ellipse = field.real[:, None]*np.cos(t)+field.imag[:, None]*np.sin(t)
    beta = np.deg2rad(np.linspace(-90, 90, 361))
    transmitted = np.abs(np.cos(beta)*field[0]+np.sin(beta)*field[1])**2
    selected = abs(math.cos(analyzer)*field[0]+math.sin(analyzer)*field[1])**2
    ellipticity = .5*math.asin(float(np.clip(s[3]/s[0], -1, 1)))
    return dict(
        metrics=[metric("Intensité après lame / incidente", s[0]),
                 metric("Transmission de l'analyseur", selected),
                 metric("Angle d'ellipticité χ", math.degrees(ellipticity), "°"),
                 metric("Norme du Stokes réduit", np.linalg.norm(s[1:])/s[0])],
        charts=[chart("Analyse de l'état sortant", "Angle β de l'analyseur (°)", "Iβ / Iincident",
                      series("Transmission", np.rad2deg(beta), transmitted))],
        scene=scene("polarisation", "De Jones à l'ellipse et à Poincaré", "Le champ réel est Re(E exp(−iωt)) ; S₃ = 2 Im(Ex* Ey). L'ellipse précède l'analyseur.",
                    ellipse_x=ellipse[0], ellipse_y=ellipse[1], jones_re=field.real, jones_im=field.imag,
                    stokes=s[1:]/s[0], stokes_full=s, analyzer_deg=p["analyzer"], transmission=selected,
                    axis_deg=p["axis"], retardance_deg=p["retardance"]),
        steps=["Le vecteur de Jones incident est normalisé : |Ex|²+|Ey|²=1.",
               "J = R(α) diag(1, exp(iδ)) R(−α), avec δ la phase de la seconde composante dans la base de la lame.",
               "Une lame idéale est unitaire : J†J = I ; elle change la polarisation sans absorber.",
               "Iβ = |Ex cos β + Ey sin β|². Une polarisation circulaire donne Iβ = 1/2 pour tout β.",
               "S₁=|Ex|²−|Ey|², S₂=2 Re(Ex*Ey), S₃=2 Im(Ex*Ey). Pour un état pur, S₁²+S₂²+S₃²=S₀²."],
        assumptions=["Onde plane monochromatique entièrement polarisée, lame sans dichroïsme, analyseur idéal.",
                     "Les noms droite/gauche dépendent du sens d'observation ; le signe de S₃ et la convention temporelle sont donnés explicitement.",
                     "La lumière naturelle exige une matrice de cohérence ou les paramètres de Stokes : un unique vecteur de Jones ne la représente pas."])


def michelson_opd(x, y, gap, focal, tilt, mode):
    x, y = np.asarray(x), np.asarray(y)
    if mode == "rings":
        return 2*gap/np.sqrt(1+(x*x+y*y)/(focal*focal))
    return 2*gap+2*tilt*x+np.zeros_like(y)


def michelson(p):
    lam, gap, f, tilt = p["wavelength"]*1e-9, p["gap"]*1e-6, p["focal"]*1e-3, p["tilt"]*1e-3
    extent = f*math.tan(math.radians(p["field"])) if p["mode"] == "rings" else .008
    if p["mode"] == "rings":
        # Quatre points par frange au bord : borne sur |∂δ/∂x| Δx/λ.
        count = max(181, int(math.ceil(16*gap*(extent/f)**2/lam))+1)
        count += (count+1) % 2
        nx, ny = count, count
    else:
        count = max(181, int(math.ceil(16*extent*abs(tilt)/lam))+1)
        count += (count+1) % 2
        nx, ny = count, 81
    x, y = np.linspace(-extent, extent, nx), np.linspace(-extent, extent, ny)
    X, Y = np.meshgrid(x, y)
    opd = michelson_opd(X, Y, gap, f, tilt, p["mode"])
    phase = math.radians(p["phase"])
    intensity = 1+np.cos(2*np.pi*opd/lam+phase)
    centeropd = michelson_opd(x, np.zeros_like(x), gap, f, tilt, p["mode"])
    central = 1+np.cos(2*np.pi*centeropd/lam+phase)
    fringe = lam/(2*tilt)*1e3 if tilt else "Uniforme"
    return dict(
        metrics=[metric("Ordre axial p = 2e/λ", 2*gap/lam),
                 metric("Translation d'un miroir pour une frange", lam*1e9/2, "nm"),
                 metric("Interfrange du coin", fringe, "mm" if tilt else ""),
                 metric("Étendue de δ dans le champ", np.ptp(opd)*1e6, "µm")],
        charts=[chart("Coupe de l'interférogramme", "x (mm)", "I / (I₁+I₂)", series("Franges", x*1e3, central))],
        scene=scene("image", "Michelson : deux trajets recombinés", "Lame d'air : δ=2e cos θ, avec tan θ=r/f. Coin d'air : δ≃2e+2αx dans le plan du coin imagé.",
                    variant="michelson", mode=p["mode"], x=x*1e3, y=y*1e3, x_label="x (mm)", y_label="y (mm)", intensity=intensity,
                    wavelength_nm=p["wavelength"], gap_um=p["gap"], tilt_mrad=p["tilt"], focal_mm=p["focal"]),
        steps=["La translation e modifie un aller-retour : la différence de marche axiale vaut 2e.",
               "En lame d'air, les deux rayons émergents parallèles ont δ = 2e cos θ : les franges sont d'égale inclinaison.",
               "Le plan focal associe r à θ par tan θ = r/f ; les points de même r donnent des anneaux.",
               "Dans un coin faiblement incliné, e(x)=e+αx et i=λ/(2α). Ces franges se localisent dans le plan du coin, observé par imagerie."],
        assumptions=["Séparatrice et compensatrice idéales, intensités des deux trajets égales, raie monochromatique.",
                     "Pour les anneaux, la source éclaire les différentes directions du champ ; chaque direction interfère avec sa réplique issue de la même source.",
                     "Les plans d'observation changent entre lame d'air et coin d'air ; les deux scènes ne représentent pas un même écran déplacé arbitrairement."])


def gaussian_coherence(opd, linewidth):
    """Module de γ pour un spectre gaussien de largeur en fréquence FWHM."""
    return np.exp(-(np.pi*linewidth*np.asarray(opd)/C)**2/(4*np.log(2)))


def doublet_coherence(opd, frequency_gap):
    return np.cos(np.pi*frequency_gap*np.asarray(opd)/C)


def coherence(p):
    lam, linewidth, delta_lam = p["wavelength"]*1e-9, p["linewidth"]*1e9, p["doublet"]*1e-9
    n1, n2 = C/(lam-delta_lam/2), C/(lam+delta_lam/2)
    difference, carrier = abs(n1-n2), (n1+n2)/2
    spatial = float(np.sinc(p["separation"]*1e-3*p["source_width"]*1e-3/(lam*p["source_distance"])))
    selected = p["opd"]*1e-3
    def gamma(delta):
        if p["spectrum"] == "independent":
            return np.zeros_like(np.asarray(delta), dtype=float)
        if p["spectrum"] == "doublet":
            return spatial*doublet_coherence(delta, difference)
        return spatial*gaussian_coherence(delta, linewidth)
    delta = np.linspace(0, .020, 1601)
    degree = gamma(delta)
    x = np.linspace(-.006, .006, 1601)
    localopd = selected+p["separation"]*1e-3*x
    localgamma = gamma(localopd)
    freq = carrier if p["spectrum"] == "doublet" else C/lam
    intensity = 1+localgamma*np.cos(2*np.pi*freq*localopd/C)
    centralgamma = float(gamma(selected))
    return dict(
        metrics=[metric("Visibilité au centre |γ|", abs(centralgamma)),
                 metric("Facteur de cohérence spatiale signé", spatial),
                 metric("Demi-largeur à mi-hauteur de |γtemp| gaussien", 2*np.log(2)/np.pi*C/linewidth*1e3, "mm"),
                 metric("Premier brouillage du doublet", C/(2*difference)*1e3, "mm")],
        charts=[chart("Enveloppe de visibilité : la phase fine est distincte", "Différence de marche δ (mm)", "Corrélation réduite",
                      series("γ réel signé", delta*1e3, degree), series("Visibilité |γ|", delta*1e3, abs(degree)))],
        scene=scene("fringes", "Le contraste dépend de la corrélation", "Le profil local résout les franges optiques ; la courbe globale résout leur enveloppe. Une corrélation négative décale les franges d'une demi-période.",
                    variant="coherence", x_mm=x*1e3, intensity=intensity, wavelength_nm=p["wavelength"],
                    slits_mm=[-p["separation"]/2, p["separation"]/2], screen_distance_m=1,
                    visibility=abs(centralgamma), spectrum=p["spectrum"], opd_mm=p["opd"]),
        steps=["γtemp(τ) est la transformée de Fourier du spectre d'intensité normalisé ; τ = δ/c.",
               "Pour un profil gaussien de largeur FWHM Δν : |γtemp| = exp[−(πΔνδ/c)²/(4 ln 2)].",
               "Pour deux raies fines égales : γtemp porte l'enveloppe cos(πΔνδ/c), avec une fréquence porteuse moyenne.",
               "Une source uniforme de largeur s à la distance Ds donne γspatial = sinc(as/(λDs)).",
               "Des sources indépendantes ont une corrélation mutuelle nulle : leurs intensités s'ajoutent, même si chacune est monochromatique."],
        assumptions=["Modèle stationnaire, spectre étroit autour de ν₀, largeur angulaire de source faible, deux fentes équilibrées.",
                     "Le spectre et la distribution angulaire sont séparables : γ = γtemp γspatial.",
                     "L'enveloppe globale est échantillonnée ; on ne prétend pas résoudre les oscillations optiques d'une longue différence de marche sur cette courbe."])


def airy_transmission(detuning, reflectivity):
    coefficient = 4*reflectivity/(1-reflectivity)**2
    return 1/(1+coefficient*np.sin(np.pi*np.asarray(detuning))**2)


def fabryperot(p):
    L, n, R, theta = p["length"]*1e-3, p["index"], p["reflectivity"], math.radians(p["angle"])
    fsr = C/(2*n*L*math.cos(theta))
    order = round((C/(p["wavelength"]*1e-9))/fsr)
    coefficient = 4*R/(1-R)**2
    halfargument = (1-R)/(2*math.sqrt(R)) if R else 2.0
    if halfargument <= 1:
        fractional_width = 2/np.pi*math.asin(halfargument)
        finesse, linewidth = 1/fractional_width, fsr*fractional_width/1e9
    else:
        finesse, linewidth = "Pas de largeur à mi-hauteur", "Non définie"
    detuning = np.linspace(-1.5, 1.5, 3001)
    T = airy_transmission(detuning, R)
    trans = float(airy_transmission(p["detuning"], R))
    return dict(
        metrics=[metric("Intervalle spectral libre", fsr/1e9, "GHz"),
                 metric("Coefficient d'Airy 4R/(1−R)²", coefficient),
                 metric("Finesse spectrale exacte ISL/FWHM", finesse),
                 metric("Largeur FWHM", linewidth, "GHz" if isinstance(linewidth, float) else ""),
                 metric("Transmission actuelle", trans)],
        charts=[chart("Trois résonances de la cavité", "Désaccord ν−νm (GHz)", "T = It/Iincident",
                      series("Transmission", detuning*fsr/1e9, T))],
        scene=scene("cavity", "Les allers-retours sélectionnent la fréquence", "Des miroirs identiques sans absorption peuvent transmettre 100 % sur résonance.",
                    variant="fabryperot", length_mm=p["length"], reflectivity=R, index=n,
                    orders=[order-1, order, order+1], freq_offset_GHz=detuning*fsr/1e9,
                    transmission=T, current_transmission=trans, detuning=p["detuning"], angle_deg=p["angle"]),
        steps=["La phase d'aller-retour est φ = 4πne cos θ/λ₀, avec θ l'angle interne.",
               "Sommer les amplitudes d'une suite géométrique de raison R exp(iφ).",
               "Miroirs symétriques sans pertes : T = [1 + (4R/(1−R)²) sin²(φ/2)]⁻¹.",
               "ISL = c/(2ne cos θ) si n et θ sont constants sur le balayage.",
               "La finesse exacte est π/[2 arcsin((1−R)/(2√R))] lorsque la transmission descend sous 1/2. À forte réflectivité elle tend vers π√R/(1−R)."],
        assumptions=["Cavité plane symétrique sans absorption ; R est une réflectivité en intensité, pas un coefficient d'amplitude.",
                     "Dispersion de l'indice négligée sur trois ISL ; angle interne maintenu constant.",
                     "Le coefficient d'Airy et la finesse spectrale sont deux quantités différentes."])


def fourier_field(object_kind, filter_kind, cutoff, pixel_um, size=128):
    """Champ d'objet, TF unitaire, masque passif et champ image."""
    dx = pixel_um*1e-3  # mm
    coord = (np.arange(size)-size/2)*dx
    normalized = (np.arange(size)-size/2)/size
    X, Y = np.meshgrid(normalized, normalized)
    if object_kind == "grid":
        vertical = np.abs(np.sin(2*np.pi*8*X)) < .3
        horizontal = np.abs(np.sin(2*np.pi*5*Y)) < .3
        object_field = (.15+.85*(vertical | horizontal)).astype(complex)
    elif object_kind == "cells":
        disks = (((X+.19)**2+(Y-.08)**2 < .10**2) | ((X-.12)**2+(Y+.1)**2 < .14**2))
        bars = (abs(Y-.3)<.04)&(abs(X)<.3)&(np.cos(2*np.pi*20*X)>0)
        object_field = (.08+.92*(disks | bars)).astype(complex)
    else:
        phase = np.pi*.7*np.exp(-((X-.12)**2+(Y+.08)**2)/.035)
        phase += np.pi*.5*((abs(X+.2)<.05)&(abs(Y)<.25))
        object_field = np.exp(1j*phase)
    freq = np.fft.fftshift(np.fft.fftfreq(size, dx))
    FX, FY = np.meshgrid(freq, freq)
    if filter_kind == "identity":
        mask = np.ones_like(FX)
    elif filter_kind == "lowpass":
        mask = (FX*FX+FY*FY <= cutoff*cutoff).astype(float)
    elif filter_kind == "highpass":
        mask = (FX*FX+FY*FY >= cutoff*cutoff).astype(float)
    elif filter_kind == "vertical":
        mask = (abs(FX) <= cutoff).astype(float)
    else:
        mask = (abs(FY) <= cutoff).astype(float)
    transform = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(object_field), norm="ortho"))
    reconstructed = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(transform*mask), norm="ortho"))
    return coord, freq, object_field, transform, mask, reconstructed


def fourier(p):
    coord, freq, obj, transform, mask, out = fourier_field(p["object"], p["filter"], p["cutoff"], p["pixel"])
    input_image, output_image = abs(obj)**2, abs(out)**2
    energy_in, energy_freq, energy_out = np.sum(input_image), np.sum(abs(transform)**2), np.sum(output_image)
    spectrum_intensity = abs(transform)**2
    common_max = max(float(input_image.max()), float(output_image.max()))
    limit = p["wavelength"]*1e-9*(p["focal"]*1e-3)*p["cutoff"]*1e3
    middle = len(coord)//2
    panels = [dict(title="Objet : |Eobjet|²", values=input_image, x=coord, y=coord, x_label="x (mm)", y_label="y (mm)", intensity_scale="commune objet/image", max_value=common_max),
              dict(title="Spectre |TF|², affichage logarithmique", values=spectrum_intensity, x=freq, y=freq, x_label="νx (mm⁻¹)", y_label="νy (mm⁻¹)", display="log", intensity_scale="logarithmique annoncée"),
              dict(title="Masque d'amplitude H", values=mask, x=freq, y=freq, x_label="νx (mm⁻¹)", y_label="νy (mm⁻¹)", display="linear", intensity_scale="0 à 1", max_value=1),
              dict(title="Image : |Eimage|²", values=output_image, x=coord, y=coord, x_label="x (mm)", y_label="y (mm)", intensity_scale="commune objet/image", max_value=common_max)]
    return dict(
        metrics=[metric("Énergie image / énergie objet", energy_out/energy_in),
                 metric("Erreur relative de Parseval avant masque", abs(energy_freq/energy_in-1)),
                 metric("Fréquence de Nyquist", 500/p["pixel"], "mm⁻¹"),
                 metric("Dimension du masque au foyer : λfνc", limit*1e3, "mm"),
                 metric("Champ objet échantillonné", len(coord)*p["pixel"]*1e-3, "mm")],
        charts=[chart("Coupe dans l'objet et l'image", "x (mm)", "Intensité, même unité",
                      series("Objet", coord, input_image[middle]), series("Image filtrée", coord, output_image[middle]))],
        scene=scene("image", "Banc 4f : objet → spectre → masque → image", "Seule la vue du spectre utilise un affichage logarithmique. Objet et image conservent une unité d'intensité commune ; aucun flou artificiel n'est ajouté.",
                    variant="fourier", panels=panels, x=coord, y=coord, intensity=output_image,
                    x_label="x (mm)", y_label="y (mm)", wavelength_nm=p["wavelength"], focal_mm=p["focal"],
                    object_kind=p["object"], filter_kind=p["filter"], cutoff_per_mm=p["cutoff"]),
        steps=["Eobjet est une amplitude complexe ; un objet de phase peut avoir |Eobjet|² = 1 partout.",
               "Calculer la TF discrète 2D unitaire, multiplier par le masque H, puis effectuer la TF inverse.",
               "Le plan focal relie la position physique u à la fréquence spatiale ν par u = λfν.",
               "Parseval : Σ|Eobjet|² = Σ|TF(Eobjet)|². Si |H|≤1, l'énergie transmise ne peut augmenter.",
               "Le champ reconstruit du banc 4f est inversé géométriquement ; la scène le réoriente pour comparer les mêmes points.",
               "Le pas Δx impose |ν|≤1/(2Δx) ; un détail non échantillonné ne peut être récupéré par un filtre."],
        assumptions=["Imagerie cohérente scalaire, lentilles minces idéales, modèle discret périodique 128×128, pupille extérieure supposée assez grande.",
                     "La coupure peut dépasser Nyquist : la portion correspondante du masque n'a alors aucun effet supplémentaire.",
                     "Les contours numériques très fins sont bornés par l'échantillonnage ; l'atelier n'assimile pas l'intensité à une amplitude."])


def cavity_matrix(length, curvature1, curvature2):
    propagation = np.array([[1.0, length], [0.0, 1.0]])
    mirror1 = np.array([[1.0, 0.0], [-2*curvature1, 1.0]])
    mirror2 = np.array([[1.0, 0.0], [-2*curvature2, 1.0]])
    return mirror1 @ propagation @ mirror2 @ propagation


def cavity_mode(length, curvature1, curvature2, wavelength):
    """q juste après le miroir 1 ; None pour cavité instable ou marginale."""
    product = (1-length*curvature1)*(1-length*curvature2)
    if not 0 < product < 1:
        return None
    A, B, C_, D = cavity_matrix(length, curvature1, curvature2).ravel()
    roots = np.roots([C_, D-A, -B]).astype(complex)
    q = next((root for root in roots if root.imag > 0), None)
    if q is None:
        return None
    return q


def laser(p):
    L, lam, k1, k2 = p["length"]*1e-3, p["wavelength"]*1e-9, p["curvature1"], p["curvature2"]
    g1, g2 = 1-L*k1, 1-L*k2
    matrix = cavity_matrix(L, k1, k2)
    q = cavity_mode(L, k1, k2, lam)
    stable = q is not None
    threshold = p["loss"]-math.log(p["reflectivity1"]*p["reflectivity2"])/(2*L)
    steady = p["saturation"]*max(p["gain"]/threshold-1, 0) if stable else 0.0
    output = (1-p["reflectivity2"])*steady
    power = np.linspace(0, max(2*p["saturation"], 1.5*steady), 601)
    saturated = p["gain"]/(1+power/p["saturation"])
    zz = np.linspace(0, L, 151)
    if stable:
        qz = q+zz
        width = np.sqrt(-lam/(np.pi*np.imag(1/qz)))
        width1, width2 = width[0]*1e3, width[-1]*1e3
    else:
        width = np.zeros_like(zz)
        width1, width2 = "Mode non fixé", "Mode non fixé"
    if not stable:
        state = "Géométrie instable ou marginale"
    elif p["gain"] > threshold:
        state = "Mode stable, gain au-dessus du seuil"
    else:
        state = "Mode stable, gain au-dessous du seuil"
    return dict(
        metrics=[metric("État", state), metric("Produit de stabilité g₁g₂", g1*g2),
                 metric("Gain seuil en intensité", threshold, "m⁻¹"),
                 metric("Puissance intracavité stationnaire", steady, "W"),
                 metric("Puissance du coupleur", output, "W"),
                 metric("Rayon du mode au miroir 1", width1, "mm" if stable else "")],
        charts=[chart("Saturation : l'équilibre impose gain = pertes", "Puissance intracavité P (W)", "Coefficient en intensité (m⁻¹)",
                      series("Gain g₀/(1+P/Ps)", power, saturated), series("Pertes de seuil", power, np.full_like(power, threshold)))],
        scene=scene("cavity", "Deux conditions pour un laser", "La géométrie confine le mode ; le bilan d'énergie impose un gain supérieur aux pertes. Une géométrie marginale exige une analyse particulière.",
                    variant="laser", length_mm=p["length"], curvature1_per_m=k1, curvature2_per_m=k2,
                    reflectivity1=p["reflectivity1"], reflectivity2=p["reflectivity2"], stable=stable,
                    g1=g1, g2=g2, roundtrip_matrix=matrix, z_mm=zz*1e3, w_mm=width*1e3,
                    wavelength_nm=p["wavelength"], intracavity_W=steady, output_W=output),
        steps=["Dans la base (hauteur, angle), P(L)=[[1,L],[0,1]] et un miroir concave de courbure 1/R donne M=[[1,0],[−2/R,1]].",
               "La matrice d'aller-retour a det M = 1 et Tr M/2 = 2g₁g₂−1, gᵢ=1−L/Rᵢ.",
               "Stabilité stricte : 0 < g₁g₂ < 1. Le paramètre q vérifie q = (Aq+B)/(Cq+D), Im q > 0.",
               "Le gain et les pertes sont définis ici en intensité : R₁R₂ exp[2(g−α)L] = 1 au seuil.",
               "gseuil = α − ln(R₁R₂)/(2L). Avec g(P)=g₀/(1+P/Ps), P=Ps(g₀/gseuil−1) lorsqu'un mode stable existe et g₀>gseuil."],
        assumptions=["Cavité de deux miroirs sphériques, approximation paraxiale ; aucun rayon de courbure nul n'est introduit.",
                     "Le cas confocal g₁g₂=0 est marginal dans le critère strict ; il possède des modes mais demande de traiter la dégénérescence séparément.",
                     "Modèle modal stationnaire à gain homogène saturable, sans compétition de modes ni dynamique de population ; les pertes de diffraction sont négligées pour le mode stable.",
                     "Dans une géométrie instable ou marginale, la puissance stationnaire de ce modèle de mode confiné n'est pas extrapolée."])


def gaussian_width(z, waist, wavelength, index=1.0):
    rayleigh = np.pi*index*waist*waist/wavelength
    return waist*np.sqrt(1+(np.asarray(z)/rayleigh)**2)


def gaussian_intensity(r, z, waist, wavelength, power, index=1.0):
    w = gaussian_width(z, waist, wavelength, index)
    return 2*power/(np.pi*w*w)*np.exp(-2*np.asarray(r)**2/(w*w))


def gaussien(p):
    w0, lam, power, n = p["waist"]*1e-6, p["wavelength"]*1e-9, p["power"]*1e-3, p["index"]
    rayleigh = np.pi*n*w0*w0/lam
    position = p["position"]*rayleigh
    width = float(gaussian_width(position, w0, lam, n))
    zz = np.linspace(-5*rayleigh, 5*rayleigh, 181)
    ww = gaussian_width(zz, w0, lam, n)
    rr = np.linspace(-3*width, 3*width, 801)
    observed = gaussian_intensity(rr, position, w0, lam, power, n)
    waistprofile = gaussian_intensity(rr, 0, w0, lam, power, n)
    radial = np.linspace(0, 5*width, 2001)
    integral_rule = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    integral = float(integral_rule(2*np.pi*radial*gaussian_intensity(radial, position, w0, lam, power, n), radial))
    curvature = position*(1+(rayleigh/position)**2) if position else "Front plan"
    yy = np.linspace(-3*ww.max(), 3*ww.max(), 91)
    intensity = gaussian_intensity(yy[:, None], zz[None, :], w0, lam, power, n)
    return dict(
        metrics=[metric("Longueur de Rayleigh zR", rayleigh*1e3, "mm"),
                 metric("Rayon du faisceau dans le plan observé", width*1e6, "µm"),
                 metric("Demi-divergence λ₀/(πnw₀)", lam/(np.pi*n*w0)*1e3, "mrad"),
                 metric("Phase de Gouy", math.degrees(math.atan(p["position"])), "°"),
                 metric("Puissance intégrée numériquement", integral*1e3, "mW"),
                 metric("Rayon de courbure du front", curvature*1e3 if isinstance(curvature, float) else curvature, "mm" if isinstance(curvature, float) else "")],
        charts=[chart("Profil transverse : aire conservée en 2D", "Coordonnée transverse r (µm)", "I (W·m⁻²)",
                      series("Au waist", rr*1e6, waistprofile), series("Plan observé", rr*1e6, observed)),
                chart("Étendue et phase lente", "z/zR", "w/w₀", series("Rayon à 1/e²", zz/rayleigh, ww/w0))],
        scene=scene("beam", "Une solution paraxiale qui diffracte", "w est le rayon à 1/e² d'intensité, pas un diamètre. Le profil 2D longitudinal est calculé depuis la même puissance.",
                    z_mm=zz*1e3, w_mm=ww*1e3, waist_mm=w0*1e3, rayleigh_mm=rayleigh*1e3,
                    observation_mm=position*1e3, lambda_nm=p["wavelength"], index=n, power_mW=p["power"],
                    x=zz*1e3, y=yy*1e3, intensity=intensity, profiles=[dict(title="Plan observé", x_um=rr*1e6, intensity=observed)]),
        steps=["zR = πnw₀²/λ₀ et w(z) = w₀√(1+(z/zR)²).",
               "I(r,z) = [2P/(πw²)] exp(−2r²/w²). Le rayon w correspond à I(w)/I(0)=exp(−2).",
               "L'intégrale 2π∫₀∞ I(r,z)rdr vaut P pour tout z ; une simple aire sous une coupe 1D n'est pas la puissance totale.",
               "R(z)=z[1+(zR/z)²], avec front plan au waist ; ψG(z)=arctan(z/zR).",
               "La phase paraxiale s'écrit kz+kr²/(2R)−ψG dans la convention exp(−iωt)."],
        assumptions=["Mode TEM₀₀ scalaire monochromatique, milieu homogène d'indice n, solution de l'équation paraxiale.",
                     "λ₀≪πnw₀ : les demi-divergences des réglages restent petites.",
                     "La couleur représente une intensité ; elle ne représente pas directement la phase du front d'onde."])


# Quadrature de l'intégrale de Bessel : adaptée aux arguments ≤ 50 des scènes.
_LEGENDRE_X, _LEGENDRE_W = np.polynomial.legendre.leggauss(72)
_BESSEL_THETA = np.pi*(_LEGENDRE_X+1)/2
_BESSEL_WEIGHT = _LEGENDRE_W/2


def bessel_j1(argument):
    value = np.asarray(argument, dtype=float)
    flat = value.ravel()
    result = np.empty_like(flat)
    # Éviter un immense tableau temporaire pour une image complète.
    for start in range(0, flat.size, 2048):
        block = flat[start:start+2048]
        result[start:start+2048] = np.cos(block[:, None]*np.sin(_BESSEL_THETA)-_BESSEL_THETA) @ _BESSEL_WEIGHT
    return result.reshape(value.shape)


def airy_amplitude(argument, obstruction=0.0):
    u = np.asarray(argument, dtype=float)
    result = np.ones_like(u)
    nonzero = abs(u) > 1e-5
    v = u[nonzero]
    if v.size:
        result[nonzero] = 2*(bessel_j1(v)-obstruction*bessel_j1(obstruction*v))/(v*(1-obstruction*obstruction))
    # Développement régulier au centre, y compris pour la pupille annulaire.
    result[~nonzero] = 1-(1+obstruction*obstruction)*u[~nonzero]**2/8
    return result


def first_airy_zero(obstruction):
    if obstruction == 0:
        return AIRY_ZERO
    low, high = 2.0, AIRY_ZERO
    for _ in range(45):
        middle = (low+high)/2
        if float(airy_amplitude(middle, obstruction)) > 0:
            low = middle
        else:
            high = middle
    return (low+high)/2


def airy(p):
    lam, D, eps = p["wavelength"]*1e-9, p["diameter"]*1e-3, p["obstruction"]
    scale = lam/D
    separation = p["separation"]*RAYLEIGH*scale
    extent = max(4.3*scale, separation/2+3.4*scale)
    x = np.linspace(-extent, extent, 151)
    y = np.linspace(-3.8*scale, 3.8*scale, 131)
    X, Y = np.meshgrid(x, y)
    first = airy_amplitude(np.pi/scale*np.hypot(X+separation/2, Y), eps)**2
    second = p["ratio"]*airy_amplitude(np.pi/scale*np.hypot(X-separation/2, Y), eps)**2
    total = first+second
    xx = np.linspace(-extent, extent, 1201)
    profile1 = airy_amplitude(np.pi/scale*abs(xx+separation/2), eps)**2
    profile2 = p["ratio"]*airy_amplitude(np.pi/scale*abs(xx-separation/2), eps)**2
    zero = first_airy_zero(eps)*scale/np.pi
    return dict(
        metrics=[metric("Repère Rayleigh sans obstruction", RAYLEIGH*scale*ARCSEC, "″"),
                 metric("Séparation réelle des étoiles", separation*ARCSEC, "″"),
                 metric("Premier minimum de la pupille choisie", zero*ARCSEC, "″"),
                 metric("Surface transmise / disque plein", 1-eps*eps)],
        charts=[chart("Deux PSF s'ajoutent en intensité", "Angle θx (secondes d'arc)", "Intensité, premier pic isolé = 1",
                      series("Étoile 1", xx*ARCSEC, profile1), series("Étoile 2", xx*ARCSEC, profile2), series("Image totale", xx*ARCSEC, profile1+profile2))],
        scene=scene("image", "Deux étoiles derrière une pupille circulaire", "Les étoiles sont incohérentes : I=I₁+I₂. L'obstruction centrale redistribue l'énergie vers les anneaux et change le premier minimum.",
                    variant="airy", x=x*ARCSEC, y=y*ARCSEC, x_label="θx (″)", y_label="θy (″)", intensity=total,
                    wavelength_nm=p["wavelength"], diameter_mm=p["diameter"], obstruction=eps,
                    separation_arcsec=separation*ARCSEC, flux_ratio=p["ratio"]),
        steps=["Pour un disque plein : A(u)=2J₁(u)/u, u=πDθ/λ, et A(0)=1.",
               "Le premier zéro est u₁=3,83170597 : θ₁=(u₁/π)λ/D ≃1,22λ/D.",
               "Deux étoiles indépendantes produisent la somme des PSF d'intensité translatées, sans terme d'interférence mutuelle.",
               "Une pupille annulaire de rapport ε donne A(u)=2[J₁(u)−εJ₁(εu)]/[u(1−ε²)].",
               "Le repère de Rayleigh est un critère de résolution de deux sources comparables, pas une frontière absolue indépendante du bruit et du flux relatif."],
        assumptions=["Diffraction de Fraunhofer d'une pupille circulaire idéale, petites directions angulaires, lumière monochromatique.",
                     "Atmosphère, aberrations, pixels du détecteur et bruit ne sont pas inclus : il s'agit de la limite de diffraction.",
                     "Les profils sont normalisés à leur intensité axiale propre. La surface transmise indique séparément la perte de lumière due à l'obstruction."])


def shg_coupling(wavelength, intensity, coefficient, index1, index2):
    omega = 2*np.pi*C/wavelength
    return math.sqrt(2*omega*omega*coefficient*coefficient*intensity/(index1*index1*index2*EPS0*C**3))


def coupled_shg(length, coupling, mismatch, count=1201):
    """u fondamental et v harmonique normalisés en énergie ; RK4 complexe."""
    steps = max(count-1, int(80*(coupling+abs(mismatch))*length)+1)
    z = np.linspace(0, length, steps+1)
    u, v = np.empty(steps+1, complex), np.empty(steps+1, complex)
    u[0], v[0] = 1, 0
    h = length/steps
    def derivative(position, state):
        a, b = state
        phase = np.exp(1j*mismatch*position)
        return np.array([-coupling*np.conj(a)*b/phase, coupling*a*a*phase])
    state = np.array([1+0j, 0j])
    for j in range(steps):
        k1 = derivative(z[j], state)
        k2 = derivative(z[j]+h/2, state+h*k1/2)
        k3 = derivative(z[j]+h/2, state+h*k2/2)
        k4 = derivative(z[j]+h, state+h*k3)
        state += h*(k1+2*k2+2*k3+k4)/6
        u[j+1], v[j+1] = state
    return z, u, v


def nonlineaire(p):
    lam, intensity, d = p["wavelength"]*1e-9, p["intensity"]*1e13, p["coefficient"]*1e-12
    L, mismatch = p["length"]*1e-3, p["mismatch"]*1e3
    coupling = shg_coupling(lam, intensity, d, p["index1"], p["index2"])
    if p["model"] == "coupled":
        z, u, v = coupled_shg(L, coupling, mismatch)
        fundamental, harmonic = abs(u)**2, abs(v)**2
        conservation = float(np.max(abs(fundamental+harmonic-1)))
    else:
        z = np.linspace(0, L, 1201)
        harmonic = (coupling*z)**2*np.sinc(mismatch*z/(2*np.pi))**2
        fundamental = np.ones_like(harmonic)
        conservation = "Pompe fixée : bilan tronqué"
    small = (coupling*z)**2*np.sinc(mismatch*z/(2*np.pi))**2
    eta = float(harmonic[-1])
    input_photon_flux = intensity/(H*C/lam)
    return dict(
        metrics=[metric("Conversion à la sortie I₂ω/Iω(0)", eta),
                 metric("Conversion prédite sans déplétion", float(small[-1])),
                 metric("Erreur max du bilan énergétique", conservation),
                 metric("Longueur d'interaction 1/g", 1/coupling*1e3, "mm"),
                 metric("Longueur d'onde doublée", p["wavelength"]/2, "nm"),
                 metric("Flux photonique harmonique / flux incident", eta/2)],
        charts=[chart("Conversion et reconversion dans le cristal", "z (mm)", "Intensité / Iω(0)",
                      series("Fondamental", z*1e3, fundamental), series("Harmonique 2ω", z*1e3, harmonic),
                      series("Pompe constante : prédiction", z*1e3, small)),
                chart("Conservation photonique pondérée", "z (mm)", "Flux / Nω(0)",
                      series("Nω", z*1e3, fundamental), series("2 N₂ω", z*1e3, harmonic),
                      series("Nω + 2N₂ω", z*1e3, fundamental+harmonic))],
        scene=scene("nonlinear", "Deux photons fondamentaux → un photon harmonique", "Les intensités normalisées sont des fractions d'énergie. À accord parfait, la pompe décroît en sech²(gz), l'harmonique croît en tanh²(gz).",
                    z_mm=z*1e3, pump1=fundamental, pump2=np.zeros_like(fundamental), harmonic=harmonic,
                    mismatch_per_mm=p["mismatch"], model=p["model"], wavelength_nm=p["wavelength"],
                    coupling_per_mm=coupling*1e-3, input_photon_flux_per_m2_s=input_photon_flux),
        steps=["Ce TP traite le doublage dégénéré d'une seule pompe : deux photons ω créent un photon 2ω.",
               "Avec Ephys = Re(E exp(−iωt)) et d = χeff/2, g² = 2ω²d²Iω(0)/(nω²n₂ω ε₀c³).",
               "Pompe non déplétée : η(z) = (gz)² sinc²(Δkz/(2π)), pour sinc(u)=sin(πu)/(πu).",
               "Ondes couplées normalisées : u′=−g u* v exp(−iΔkz), v′=g u² exp(iΔkz), avec u(0)=1, v(0)=0.",
               "Les équations donnent d(|u|²+|v|²)/dz=0. À Δk=0 : u=sech(gz), v=tanh(gz).",
               "Manley–Rowe : Nω+2N₂ω=Nω(0). La conservation du nombre brut Nω+N₂ω ne s'applique pas au doublage dégénéré."],
        assumptions=["Ondes planes monochromatiques colinéaires, cristal sans absorption, approximation d'enveloppe lentement variable.",
                     "Δk est un désaccord effectif indépendant réglé par orientation et biréfringence ; les deux indices fournis fixent seulement la normalisation des intensités.",
                     "L'approximation de pompe constante est quantitative pour η≪1. Une prédiction supérieure à 1 signale sa sortie de validité et n'est pas tronquée artificiellement.",
                     "Le cas à deux pompes distinctes du PDF a deux invariants N₁+N₃ et N₂+N₃ ; il est distinct du cas dégénéré simulé ici."])


COMPUTE = dict(young=young, reseau=reseau, diffraction=diffraction,
               polarisation=polarisation, michelson=michelson,
               coherence=coherence, fabryperot=fabryperot, fourier=fourier,
               laser=laser, gaussien=gaussien, airy=airy, nonlineaire=nonlineaire)
