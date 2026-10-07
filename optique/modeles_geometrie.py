"""Optique géométrique : calculs paraxiaux et tracés exacts explicitement séparés.

Toutes les coordonnées des scènes portent l'unité indiquée dans la scène.
Les distances objet des contrôles sont positives ; les relations de Descartes
emploient p=-distance et p'=distance_image, orientés vers la droite.
"""
from __future__ import annotations

import math
import numpy as np

from science import metric, series, chart, scene, clean
from catalogue_geometrie import LAB_BY_ID

C = 299792458.0
DEG = math.pi / 180
COLORS = ["#e87953", "#53b6b0", "#aa84d9", "#e0b34c", "#65a1d3"]


def ray(points, label="", color=None, dashed=False, opacity=1):
    return dict(points=points, label=label, color=color or COLORS[0], dashed=dashed, opacity=opacity)


def element(kind, **data):
    return dict(kind=kind, **data)


def rays_scene(title, description, bounds, paths, elements=(), annotations=(), unit="mm", **data):
    return scene("rays", title, description, bounds=bounds, paths=paths,
                 elements=list(elements), annotations=list(annotations), unit=unit, **data)


def translation(distance):
    """Matrice (y, theta) en milieu d'indice identique à l'entrée et à la sortie."""
    return np.array([[1., distance], [0., 1.]])


def lens(focal):
    return np.array([[1., 0.], [-1. / focal, 1.]])


def thin_image(distance, focal):
    """Retourne None pour l'image à l'infini, au lieu d'un nombre IEEE infini."""
    denominator = distance - focal
    if abs(denominator) <= 1e-11 * max(1., abs(distance), abs(focal)):
        return None
    return distance * focal / denominator


def fresnel_amplitudes(n1, n2, incidence):
    """Amplitudes TE/TM sur une interface transparente, avec racine passive."""
    ci = math.cos(incidence)
    st = n1 / n2 * math.sin(incidence)
    ct = complex(math.sqrt(max(0., 1. - st * st)), 0.) if st <= 1 else complex(0., math.sqrt(st * st - 1.))
    rs = (n1 * ci - n2 * ct) / (n1 * ci + n2 * ct)
    rp = (n2 * ci - n1 * ct) / (n2 * ci + n1 * ct)
    return rs, rp, ct


def fresnel_unpolarized(n1, n2, incidence):
    """Flux moyen d'une onde incidente non polarisée."""
    rs, rp, ct = fresnel_amplitudes(n1, n2, incidence)
    R = (abs(rs) ** 2 + abs(rp) ** 2) / 2
    return float(R), max(0., 1. - float(R)), ct


def compute_snell(p):
    n1, n2, i = p["n1"], p["n2"], p["angle"] * DEG
    st = n1 * math.sin(i) / n2
    total = st > 1 + 1e-12
    t = None if total else math.asin(min(1., st))
    R, T, _ = fresnel_unpolarized(n1, n2, i)
    rs, rp, _ = fresnel_amplitudes(n1, n2, i)
    length = 1.
    paths = [ray([[-length * math.cos(i), -length * math.sin(i)], [0, 0]], "Incident"),
             ray([[0, 0], [-length * math.cos(i), length * math.sin(i)]], "Réfléchi", COLORS[2], opacity=.3 + .7 * R)]
    if t is not None:
        paths.append(ray([[0, 0], [length * math.cos(t), length * math.sin(t)]], "Transmis", COLORS[1], opacity=.3 + .7 * T))
    angles = np.linspace(0, 89.5, 360)
    sine = n1 / n2 * np.sin(angles * DEG)
    valid = sine <= 1
    refraction = np.rad2deg(np.arcsin(np.minimum(1., sine[valid])))
    reflection = np.array([fresnel_unpolarized(n1, n2, a * DEG)[0] for a in angles])
    amplitudes = [fresnel_amplitudes(n1, n2, a * DEG) for a in angles]
    reflection_s = np.array([abs(a[0])**2 for a in amplitudes])
    reflection_p = np.array([abs(a[1])**2 for a in amplitudes])
    critical = math.degrees(math.asin(n2 / n1)) if n1 > n2 else None
    return dict(metrics=[metric("Angle transmis", "Pas de rayon propagatif" if t is None else math.degrees(t), "°"),
        metric("Angle critique", "Aucun pour ce sens de traversée" if critical is None else critical, "°"),
        metric("Réflectance moyenne TE/TM", R), metric("Réflectance TE : Rₛ", abs(rs)**2), metric("Réflectance TM : Rₚ", abs(rp)**2),
        metric("Transmittance de flux non polarisé", T), metric("Bilan R + T", R + T),
        metric("n₁ sin i − n₂ sin t", "Onde évanescente" if t is None else n1 * math.sin(i) - n2 * math.sin(t))],
        charts=[chart("La direction transmise s'écarte de la loi i = t", "Incidence i (°)", "Réfraction t (°)",
                      series("Descartes–Snell", angles[valid], refraction), series("Même indice : t=i", angles, angles)),
                chart("Fresnel : moyenne et polarisations séparées", "Incidence i (°)", "Fraction de puissance",
                      series("R non polarisé", angles, reflection), series("Rₛ : TE", angles, reflection_s),
                      series("Rₚ : TM", angles, reflection_p), series("T non polarisé=1−R", angles, 1-reflection))],
        scene=rays_scene("Un dioptre plan, une normale, deux milieux", "L'incidence et la réfraction se mesurent à la normale horizontale, jamais à la surface verticale. L'opacité des rayons indique qualitativement leur fraction de flux.",
             [-1.1, 1.1, -1.1, 1.1], paths,
             [element("line", points=[[0, -1.1], [0, 1.1]], label="Interface"), element("line", points=[[-1.1, 0], [1.1, 0]], dashed=True, label="Normale")],
             [dict(x=-.75, y=.95, text=f"n₁={n1:g}"), dict(x=.6, y=.95, text=f"n₂={n2:g}")], unit="échelle arbitraire", total_internal_reflection=total),
        steps=["À l'interface, la composante tangentielle du vecteur d'onde est conservée : n₁ sin i = n₂ sin t.",
               "Un rayon réfracté propagatif existe si |n₁ sin i/n₂| ≤ 1 ; sinon la composante normale de k est imaginaire.",
               "Pour une onde incidente non polarisée : R=(|rTE|²+|rTM|²)/2. Les milieux étant transparents, le flux transmis normal vérifie T=1−R.",
               "La réflexion totale conserve toute la puissance dans le milieu incident, tout en créant un champ évanescent de l'autre côté."],
        assumptions=["Deux milieux diélectriques transparents, isotropes et non magnétiques ; une seule interface plane, sans absorption ni rugosité.",
                     "La scène représente des directions. Un trait transmis très tangent ne signifie pas qu'une puissance normale non nulle traverse l'interface à l'angle critique.",
                     "TE et TM sont moyennés à puissance incidente égale ; un laser polarisé demanderait de choisir sa polarisation."])


def compute_lentille(p):
    focal = p["focal"] * (1 if p["type"] == "convergente" else -1)
    distance, height, aperture = p["distance"], p["height"], p["aperture"]
    image = thin_image(distance, focal)
    magnification = None if image is None else -image / distance
    image_height = None if image is None else magnification * height
    right = max(2.2 * abs(focal), 80., 1.15 * image if image is not None and 0 < image < 1500 else 0)
    left = min(-1.1 * distance, -1.1 * abs(focal), 1.15 * image if image is not None and -1500 < image < 0 else 0)
    lim_y = max(1.4 * aperture, 1.4 * height, 1.3 * abs(image_height) if image_height is not None and abs(image_height) < 300 else 0)
    paths = []
    intercepts = [-.75 * aperture, 0., min(.8 * aperture, height)]
    for index, intercept in enumerate(intercepts):
        slope_in = (intercept - height) / distance
        slope_out = slope_in - intercept / focal
        paths.append(ray([[-distance, height], [0, intercept], [right, intercept + right * slope_out]], f"Rayon {index+1}", COLORS[index]))
        if image is not None and image < 0:
            paths.append(ray([[0, intercept], [left, intercept + left * slope_out]], "Prolongement virtuel", COLORS[index], dashed=True, opacity=.55))
    elements = [element("lens", x=0, y=0, height=2*aperture, divergent=focal<0, label="Lentille"),
                element("object", x=-distance, y=0, height=height, label="Objet AB")]
    if image is not None and left <= image <= right and abs(image_height) <= lim_y:
        elements.append(element("object", x=image, y=0, height=image_height, label="Image A′B′", virtual=image<0))
    annotation = [dict(x=-focal, y=0, text="F"), dict(x=focal, y=0, text="F′")]
    if image is not None and not left <= image <= right:
        annotation.append(dict(x=right*.7, y=lim_y*.8, text="Image hors du champ affiché"))
    ds = np.linspace(20, 500, 321)
    valid = np.abs(ds-focal) > .2
    qs = ds[valid]*focal/(ds[valid]-focal)
    q_curve = np.abs(qs) < 2000
    before = (ds[valid] < focal) & q_curve
    after = (ds[valid] > focal) & q_curve
    inv_d = 1/ds
    kind = "à l'infini" if image is None else "réelle" if image>0 else "virtuelle"
    return dict(metrics=[metric("Nature de l'image", kind), metric("p = OA", -distance, "mm"), metric("p′ = OA′", "∞" if image is None else image, "mm"),
                         metric("Grandissement γ=p′/p", "Non défini à l'infini" if magnification is None else magnification),
                         metric("Vergence signée", 1000/focal, "δ"), metric("Écart de conjugaison", 0 if image is None else 1/image+1/distance-1/focal, "mm⁻¹")],
        charts=[chart("Une hyperbole de conjugaison", "Distance objet positive (mm)", "Distance image orientée (mm)",
                      series("p′ : avant la focale", ds[valid][before], qs[before]), series("p′ : au-delà de la focale", ds[valid][after], qs[after])),
                chart("Le même calcul devient affine en vergences", "1/distance objet (mm⁻¹)", "1/p′ (mm⁻¹)", series("1/p′=1/f′−1/d", inv_d, 1/focal-inv_d))],
        scene=rays_scene("Construire une image avec trois rayons", "Les traits pleins suivent la propagation ; les pointillés prolongent les rayons qui donnent une image virtuelle. L'axe est orienté vers la droite.",
                         [left, right, -lim_y, lim_y], paths, elements, annotation,
                         image_distance=image, focal=focal, image_type=kind),
        steps=["Choisir l'orientation vers la droite : pour cet objet réel, p=−d et f′ est positif pour une convergente, négatif pour une divergente.",
               "La conjugaison 1/p′−1/p=1/f′ donne p′=df′/(d−f′), avec une image à l'infini lorsque d=f′.",
               "Un rayon arrivant à la hauteur y avec pente θ ressort avec θ′=θ−y/f′. Dans l'approximation paraxiale, tous les rayons issus de B se recoupent en B′.",
               "Le grandissement transversal est γ=p′/p. Une image réelle inversée a donc γ négatif pour un objet réel devant une convergente."],
        assumptions=["Lentille mince idéale dans l'air, approximation de Gauss. Les hauteurs et distances sont exactes dans ce modèle linéaire, pas dans une lentille épaisse réelle.",
                     "Les pentes sont des angles paraxiaux ; un grand rapport ouverture/focale sort des conditions physiques de cette approximation.",
                     "La scène et la première courbe limitent leur champ d'affichage près de l'asymptote ; la valeur de p′ conserve sa valeur calculée."])


def bessel_positions(D, focal):
    discriminant = D*D-4*D*focal
    if discriminant < -1e-10*D*D:
        return None
    gap = math.sqrt(max(0., discriminant))
    return (D-gap)/2, (D+gap)/2, gap


def bessel_uncertainty(D, gap, sigma_D, sigma_gap):
    dD = .25*(1+(gap/D)**2)
    dd = -gap/(2*D)
    return math.hypot(dD*sigma_D, dd*sigma_gap)


def compute_bessel(p):
    D, focal = p["distance"], p["focal"]
    s = p["position"]*D
    positions = bessel_positions(D, focal)
    aperture = 12.
    slope_factor = 1/s - 1/focal
    blur = 2*aperture*abs(1+(D-s)*slope_factor)
    grid = np.linspace(.05*D, .95*D, 401)
    diameters = 2*aperture*np.abs(1+(D-grid)*(1/grid-1/focal))
    paths = [ray([[0, 0], [s, y], [D, y*(1+(D-s)*slope_factor)]], "Faisceau axial", COLORS[k]) for k, y in enumerate([-aperture, 0, aperture])]
    metric_list = [metric("Diamètre du flou sur l'écran", blur, "mm"), metric("Position actuelle depuis l'objet", s, "mm"), metric("D − 4f′", D-4*focal, "mm")]
    annotations = []
    if positions is None:
        metric_list += [metric("Positions de mise au point", "Aucune : D < 4f′"), metric("Focale déduite de Bessel", "Non mesurable dans ce montage")]
    else:
        s1, s2, gap = positions
        sigma = bessel_uncertainty(D, gap, p["sigma_D"], p["sigma_d"])
        g1, g2 = -(D-s1)/s1, -(D-s2)/s2
        metric_list += [metric("Première position s₁", s1, "mm"), metric("Seconde position s₂", s2, "mm"), metric("Écart d=s₂−s₁", gap, "mm"),
                       metric("f′=(D²−d²)/(4D)", (D*D-gap*gap)/(4*D), "mm"), metric("Incertitude type u(f′)", sigma, "mm"),
                       metric("Produit γ₁γ₂", g1*g2), metric("Écart / incertitude sur d", gap/p["sigma_d"])]
        annotations += [dict(x=s1, y=18, text="O₁"), dict(x=s2, y=18, text="O₂")]
    return dict(metrics=metric_list,
        charts=[chart("Repérer les deux zéros du flou", "Position de la lentille s (mm)", "Diamètre géométrique de la tache (mm)", series("Écran à la distance D", grid, diameters)),
                chart("L'écart des positions est réel seulement au-delà de 4f′", "D/f′", "d/f′", series("√[(D/f′)²−4D/f′]", np.linspace(4,12,241), np.sqrt(np.linspace(4,12,241)**2-4*np.linspace(4,12,241))))],
        scene=rays_scene("Objet fixe, écran fixe, lentille mobile", "Le faisceau issu du point axial doit converger sur l'écran. Les deux positions échangent les tailles objet et image ; à D=4f′ elles se confondent.",
            [-.03*D, 1.03*D, -max(25., blur*.6), max(25., blur*.6)], paths,
            [element("object", x=0, y=0, height=12, label="Objet"), element("lens", x=s, y=0, height=30, label="Lentille"), element("screen", x=D, y=0, height=max(40, 1.2*blur), label="Écran")], annotations,
            optical_bench=True, focus_positions=None if positions is None else list(positions[:2])),
        steps=["Noter s=AO>0 et v=OA′=D−s>0 à la mise au point. La lentille vérifie 1/s+1/v=1/f′.",
               "Le polynôme s²−Ds+Df′=0 a deux racines réelles si D≥4f′. L'écart est d=√(D²−4Df′).",
               "En inversant la relation : f′=D/4−d²/(4D). Les deux grandissements sont −(D−s₁)/s₁ et −(D−s₂)/s₂, de produit 1.",
               "Pour D et d mesurés indépendamment : u(f′)²=[(1+d²/D²)u(D)/4]²+[d u(d)/(2D)]².",
               "Près de D=4f′, les positions sont difficilement distinguables : le rapport d/u(d) mesure cette séparabilité. La formule de propagation linéaire reste un repère, pas une preuve que l'incertitude augmente systématiquement."],
        assumptions=["Lentille convergente mince ; point objet axial, écran perpendiculaire à l'axe, ouverture de rayon 12 mm.",
                     "Le flou est géométrique : ni diffraction, ni aberrations, ni profondeur de perception de la mise au point.",
                     "u(D) et u(d) sont des incertitudes types indépendantes. Au cas limite d≈0, une loi gaussienne pour un écart positif et l'approximation linéaire demandent de la prudence."])


def afocal_matrix(f1, f2, spacing):
    return lens(f2) @ translation(spacing) @ lens(f1)


def compute_telescope(p):
    f1, f2, diameter = p["objective"], p["eyepiece"], p["diameter"]
    spacing = f1+f2+p["defocus"]
    theta = p["angle"]*DEG/60
    matrix = afocal_matrix(f1, f2, spacing)
    output_slopes, paths = [], []
    for index, y in enumerate(np.linspace(-diameter/2, diameter/2, 5)):
        u1 = theta-y/f1
        y2 = y+spacing*u1
        u2 = u1-y2/f2
        output_slopes.append(u2)
        paths.append(ray([[-.15*f1, y-.15*f1*theta], [0,y], [spacing,y2], [spacing+4*f2,y2+4*f2*u2]], "Rayon stellaire", COLORS[index]))
    focal_height = f1*theta
    limit_y = max(.7*diameter, max(abs(point[1]) for item in paths for point in item["points"])*1.1)
    wavelength = p["wavelength"]*1e-6
    resolution = 1.22*wavelength/diameter
    pupil_image = f2*spacing/(spacing-f2)
    pupil_diameter = diameter*f2/(spacing-f2)
    Ds = np.linspace(30,300,181)
    fs = np.linspace(10,80,181)
    return dict(metrics=[metric("Grossissement afocal nominal", -f1/f2), metric("Hauteur au foyer de l'objectif", focal_height, "mm"),
        metric("Diamètre de la pupille de sortie", pupil_diameter, "mm"), metric("Pupille de sortie après l'oculaire", pupil_image, "mm"),
        metric("Rayleigh : séparation angulaire", resolution/DEG*3600, "secondes d'arc"), metric("Matrice ABCD : déterminant", float(np.linalg.det(matrix))),
        metric("C : défaut de collimation", float(matrix[1,0]), "mm⁻¹"), metric("Écart angulaire des rayons sortants", max(output_slopes)-min(output_slopes), "rad")],
        charts=[chart("Grossir ne change pas l'ouverture", "Focale de l'oculaire (mm)", "|Grossissement|", series("fobjectif / foculaire", fs, f1/fs)),
                chart("Résoudre impose une ouverture", "Diamètre objectif (mm)", "Rayleigh (secondes d'arc)", series("1,22 λ/D", Ds, 1.22*wavelength/Ds/DEG*3600)),
                chart("Tester le caractère afocal", "Hauteur sur l'objectif (mm)", "Angle de sortie (rad)", series("θ′=Cy+Dθ", np.linspace(-diameter/2,diameter/2,101), matrix[1,0]*np.linspace(-diameter/2,diameter/2,101)+matrix[1,1]*theta))],
        scene=rays_scene("De l'astre à l'oculaire : la lunette de Kepler", "Un faisceau parallèle incliné forme une image intermédiaire au foyer de l'objectif. À la séparation f₁+f₂, l'oculaire restitue un faisceau parallèle, de direction inversée.",
            [-.18*f1, spacing+4.5*f2, -limit_y, limit_y], paths,
            [element("lens", x=0, y=0, height=diameter, label="Objectif"), element("lens", x=spacing, y=0, height=max(diameter*.1, 20), label="Oculaire")],
            [dict(x=f1,y=focal_height,text="Image intermédiaire"),dict(x=-.1*f1,y=.85*limit_y,text="Astre à l'infini")],
            matrix=matrix, angular_resolution_rad=resolution, aspect_note="Les hauteurs et longueurs sont exprimées dans la même unité ; les axes peuvent être étirés pour lire le banc."),
        steps=["En air, un rayon se décrit par (y,θ). Translation : T(d)=[[1,d],[0,1]] ; lentille : L(f)=[[1,0],[−1/f,1]].",
               "La lunette a pour matrice M=L(f₂)T(d)L(f₁). Elle est afocale lorsque C=M₂₁=0, soit d=f₁+f₂.",
               "Alors θ′=−(f₁/f₂)θ et G=−f₁/f₂. Le signe traduit le renversement de l'image.",
               "La pupille de sortie est l'image de l'objectif par l'oculaire : sa distance vaut f₂d/(d−f₂) et son diamètre Dobjectif f₂/(d−f₂). Au réglage afocal, Dsortie=Dobjectif/|G|.",
               "Pour un objectif circulaire, le repère de Rayleigh est 1,22 λ/D. Changer l'oculaire modifie G mais ne sépare pas deux détails en dessous de la résolution de l'objectif."],
        assumptions=["Lunette réfractive de Kepler à deux lentilles minces, approximation paraxiale. Le télescope réflecteur utilise d'autres éléments mais la même distinction grossissement/résolution.",
                     "La limite de Rayleigh suppose une ouverture circulaire idéale, deux points incohérents d'intensités comparables et aucune turbulence atmosphérique.",
                     "Le diamètre de l'oculaire dessiné n'introduit pas de vignettage supplémentaire. L'expérience ne modélise ni pupille de l'observateur, ni aberrations chromatiques."])


def microscope_setup(f1, f2, interval):
    spacing = f1+interval+f2
    intermediate = f1+interval
    object_distance = f1*intermediate/(intermediate-f1)
    return spacing, intermediate, object_distance


def compute_microscope(p):
    f1, f2, interval = p["objective"], p["eyepiece"], p["interval"]
    spacing, intermediate, s_nominal = microscope_setup(f1,f2,interval)
    distance = s_nominal+p["defocus"]*.001
    image = thin_image(distance,f1)
    gamma = -image/distance
    h = p["height"]
    nominal_gamma = -interval/f1
    commercial = nominal_gamma*250/f2
    aperture = f1*p["NA"]
    paths = []
    outputs = []
    for index, y in enumerate([-aperture, 0., aperture]):
        u0=(y-h)/distance
        u1=u0-y/f1
        y2=y+spacing*u1
        u2=u1-y2/f2
        paths.append(ray([[-distance,h],[0,y],[spacing,y2],[spacing+3*f2,y2+3*f2*u2]], "Point B", COLORS[index]))
        outputs.append(u2)
    limit_y = max(3., max(abs(pt[1]) for item in paths for pt in item["points"])*1.12)
    wavelengths = p["wavelength"]*.001
    nas = np.linspace(.05,.35,121)
    offsets = np.linspace(-50,50,201)
    distances=s_nominal+offsets*.001
    images=distances*f1/(distances-f1)
    return dict(metrics=[metric("Distance objet actuelle", distance, "mm"), metric("Image intermédiaire après l'objectif", image, "mm"),
                         metric("Grandissement de l'objectif", gamma), metric("Grossissement commercial nominal, d₀=25 cm", commercial),
                         metric("Rayleigh objet : 0,61λ/NA", .61*wavelengths/p["NA"], "µm"),
                         metric("Écart angulaire en sortie", max(outputs)-min(outputs), "rad")],
        charts=[chart("L'ouverture fixe une résolution", "Ouverture numérique NA", "Séparation objet (µm)", series("0,61λ/NA", nas, .61*wavelengths/nas)),
                chart("Un petit déplacement de l'objet déplace fortement l'image", "Déplacement objet (µm)", "Écart au plan focal de l'oculaire (mm)", series("p′−(f₁+Δ)", offsets, images-intermediate))],
        scene=rays_scene("L'objectif agrandit ; l'oculaire observe l'image", "Le microscope est réglé pour une observation sans accommodation lorsque l'image intermédiaire est dans le plan focal objet de l'oculaire. Les axes sont étirés pour rendre visibles les petites hauteurs.",
            [-1.3*distance,spacing+3.2*f2,-limit_y,limit_y],paths,
            [element("lens",x=0,y=0,height=2.3*aperture,label="Objectif"),element("lens",x=spacing,y=0,height=2*limit_y*.7,label="Oculaire"),
             element("object",x=-distance,y=0,height=h,label="Objet"),element("object",x=image,y=0,height=gamma*h,label="Image intermédiaire")],
            [dict(x=intermediate,y=-.8*limit_y,text="F₂ : plan attendu")],
            magnification=gamma, resolution_um=.61*wavelengths/p["NA"], aspect_note="Échelles horizontale et verticale différentes."),
        steps=["Avec Δ=F′₁F₂, l'image intermédiaire visée est à v=f₁+Δ après l'objectif. La conjugaison impose s=f₁v/(v−f₁).",
               "Au réglage nominal : γobjectif=−Δ/f₁. L'oculaire a pour grossissement commercial d₀/f₂, avec d₀=250 mm.",
               "Le produit vaut G=−Δd₀/(f₁f₂). Ce grossissement dépend du réglage nominal : une image sortant à distance finie réclame une autre comparaison angulaire.",
               "NA=n sin u décrit le cône reçu par l'objectif. Le repère de Rayleigh 0,61λ/NA concerne deux points incohérents ; il ne constitue pas un calcul de contraste pour tout échantillon."],
        assumptions=["Objectif et oculaire minces dans l'air, approximation paraxiale ; l'ouverture de tracé est a≈f₁ NA. Ce modèle ne simule pas un objectif à immersion de grande NA.",
                     "Le déplacement positif éloigne l'objet de l'objectif. Le réglage de tube est maintenu fixe, ce qui révèle la sensibilité axiale.",
                     "La séparation de Rayleigh est un repère pour l'imagerie incohérente. L'éclairage, le contraste de phase et l'échantillon ne sont pas modélisés."])


def compute_oeil(p):
    distance=p["distance"]*1000
    retina=p["retina"]
    power=1000/retina+p["error"]+p["correction"]+p["accommodation"]
    required=1000/retina+1000/distance
    image=thin_image(distance,1000/power)
    pupil_radius=p["pupil"]/2
    factor=1+retina*(1/distance-power/1000)
    blur=2*pupil_radius*abs(factor)
    diffraction=2.44*.00055*retina/p["pupil"]
    paths=[]
    for k,y in enumerate(np.linspace(-pupil_radius,pupil_radius,5)):
        slope=y/distance
        out=slope-power*y/1000
        paths.append(ray([[-12,y-12*slope],[0,y],[retina,y+retina*out]],"Faisceau axial",COLORS[k]))
    ds=np.geomspace(.1,10,201)
    pupils=np.linspace(2,8,121)
    return dict(metrics=[metric("Vergence de l'œil avec correction",power,"δ"),metric("Vergence nécessaire pour cet objet",required,"δ"),
        metric("Correction supplémentaire nécessaire",required-power,"δ"),metric("Position du foyer image","∞" if image is None else image,"mm"),
        metric("Diamètre du flou géométrique",blur*1000,"µm"),metric("Diamètre jusqu'au premier zéro d'Airy, λ=550 nm",diffraction*1000,"µm")],
        charts=[chart("Le besoin d'accommodation suit 1/d", "Distance de l'objet (m)", "Accommodation requise (δ)",series("Après la correction sélectionnée",ds,1/ds-p["error"]-p["correction"]),x_scale="log"),
                chart("Fermer la pupille : deux effets opposés", "Diamètre pupillaire (mm)","Diamètre de tache (µm)",series("Flou géométrique",pupils,pupils*abs(factor)*1000),series("Premier zéro d'Airy",pupils,2.44*.00055*retina/pupils*1000))],
        scene=rays_scene("Former une image sur une rétine fixe", "L'œil réduit remplace les dioptres oculaires par une lentille mince dans l'air. Le faisceau montré provient d'un point axial à la distance indiquée ; le point objet peut être hors du dessin.",
            [-13,retina+3,-12,12],paths,
            [element("lens",x=0,y=0,height=p["pupil"],label="Œil + correction"),element("screen",x=retina,y=0,height=12,label="Rétine"),
             element("circle",x=retina*.45,y=0,radius=retina*.58,label="Contour schématique")],
            [dict(x=-10,y=6.5,text=f"Objet à {p['distance']:g} m"),dict(x=retina,y=-6.8,text=f"Flou : {blur*1000:.3g} µm")],
            retinal_blur_um=blur*1000, image_distance=image),
        steps=["La rétine est fixée à r. Un œil emmétrope au repos est ici défini par C₀=1/r pour un objet à l'infini.",
               "L'excès de vergence e est positif pour une myopie dans ce modèle, négatif pour une hypermétropie. La correction c et l'accommodation A s'ajoutent : C=C₀+e+c+A.",
               "Pour un objet à distance d, la mise au point exige Cnécessaire=1/r+1/d. Le défaut résiduel est Cnécessaire−C.",
               "Un rayon interceptant la lentille à y atteint la rétine à y[1+r(1/d−C)]. Le diamètre géométrique vaut Dpupille fois la valeur absolue du crochet.",
               "Le diamètre d'Airy est 2,44λr/Dpupille. C'est une échelle de diffraction, pas une quantité à additionner directement au diamètre géométrique."],
        assumptions=["Modèle pédagogique d'œil réduit en air, sans séparation cornée/cristallin ni indice intraoculaire ; les vergences ne constituent pas une prescription médicale.",
                     "Correction au même plan que l'œil : des lunettes à distance finie exigeraient une translation et une composition de vergences.",
                     "Pas d'astigmatisme ni d'aberrations. La tache géométrique et Airy sont comparées comme deux mécanismes, sans convolution du point image."])


def fiber_parameters(core, cladding, radius_m, wavelength_m, length_m):
    """Fibre à saut d'indice, rayons méridiens ; extension V en faible guidage."""
    if core <= cladding:
        return dict(NA=0., internal_max=0., delay_min=length_m*core/C,
                    delay_max=None, V=0., guiding=False)
    NA=math.sqrt(core*core-cladding*cladding)
    return dict(NA=NA, internal_max=math.acos(cladding/core), delay_min=length_m*core/C,
                delay_max=length_m*core*core/(C*cladding),
                V=2*math.pi*radius_m*NA/wavelength_m, guiding=True)


def folded_fiber_y(x, radius, angle):
    """Dépliage exact d'un guide plan méridien aux faces y=±a."""
    unfolded=np.mod(np.asarray(x)*math.tan(angle)+radius, 4*radius)
    return np.where(unfolded <= 2*radius, unfolded-radius, 3*radius-unfolded)


def compute_fibre(p):
    n1,n2=p["core"],p["cladding"]
    angle_air=p["angle"]*DEG
    angle=math.asin(math.sin(angle_air)/n1)
    radius=p["radius"]
    data=fiber_parameters(n1,n2,radius*1e-6,p["wavelength"]*1e-9,p["length"])
    acceptance=math.asin(min(1.,data["NA"])) if data["guiding"] else 0.
    guided=data["guiding"] and angle <= data["internal_max"]+1e-12
    display_length=20*radius
    paths=[ray([[-3*radius,-3*radius*math.tan(angle_air)],[0,0]],"Entrée dans l'air",COLORS[2])]
    if guided:
        if angle == 0:
            vertices=[[0,0],[display_length,0]]
        else:
            hits=np.arange(radius/math.tan(angle),display_length,2*radius/math.tan(angle))
            xs=np.concatenate(([0.],hits,[display_length]))
            vertices=np.column_stack((xs,folded_fiber_y(xs,radius,angle)))
        paths.append(ray(vertices,"Rayon méridien guidé",COLORS[0]))
    else:
        hit=radius/math.tan(angle) if angle else None
        if hit is None or hit >= display_length:
            paths.append(ray([[0,0],[display_length,display_length*math.tan(angle)]],"Aucun confinement démontré",COLORS[0]))
        else:
            st=n1*math.cos(angle)/n2
            exit_t=math.asin(min(1.,st))
            exit_dir=np.array([math.sin(exit_t),math.cos(exit_t)])
            paths.append(ray([[0,0],[hit,radius],np.array([hit,radius])+exit_dir*5*radius],"Transmission dans la gaine",COLORS[0]))
    angles=np.linspace(0,35,181)
    internal=np.arcsin(np.sin(angles*DEG)/n1)
    valid=(internal <= data["internal_max"]+1e-12) if data["guiding"] else np.zeros_like(angles,dtype=bool)
    selected_delay=p["length"]*n1/(C*math.cos(angle)) if guided else None
    spread=None if data["delay_max"] is None else data["delay_max"]-data["delay_min"]
    if data["V"] == 0:
        mode_note="Pas de guidage par saut d'indice"
    elif data["V"] < 2.405:
        mode_note="Repère monomode du guide circulaire en faible guidage"
    else:
        mode_note="Plusieurs modes possibles ; estimation V²/2 seulement si V≫1"
    lengths=np.linspace(100,10000,101)
    charts=[chart("Temps de trajet des rayons acceptés", "Angle d'entrée dans l'air (°)", "Excès de retard sur le rayon axial (ns)",
                  series("n₁L/[c cos θ]−n₁L/c",angles[valid],(p["length"]*n1/(C*np.cos(internal[valid]))-data["delay_min"])*1e9))]
    if spread is not None:
        charts.append(chart("Un saut d'indice étale une impulsion multimodale", "Longueur de fibre (m)", "Écart des temps extrêmes (ns)",
                            series("L n₁(n₁/n₂−1)/c",lengths,lengths*n1*(n1/n2-1)/C*1e9)))
    return dict(metrics=[metric("Rayon sélectionné", "Guidé par réflexion totale" if guided else "Hors du domaine de guidage"),metric("Angle intérieur à l'axe",angle/DEG,"°"),
        metric("Ouverture numérique √(n₁²−n₂²)",data["NA"]),metric("Demi-angle d'acceptance dans l'air",acceptance/DEG,"°"),
        metric("Retard axial",data["delay_min"]*1e6,"µs"),metric("Retard du rayon sélectionné","Non guidé" if selected_delay is None else selected_delay*1e6,"µs"),
        metric("Étalement modal géométrique maximal","Non applicable" if spread is None else spread*1e9,"ns"),metric("Fréquence normalisée V",data["V"]),metric("Repère ondulatoire",mode_note)],
        charts=charts,
        scene=rays_scene("Observer une courte portion de fibre", "La scène affiche seulement une section de longueur 20a, pas les kilomètres du contrôle L. Le retard est calculé sur L. Un rayon méridien reste dans un plan contenant l'axe.",
            [-3.5*radius,display_length+radius,-4*radius,4*radius],paths,
            [element("line",points=[[0,radius],[display_length,radius]],label="Cœur / gaine"),
             element("line",points=[[0,-radius],[display_length,-radius]])],
            [dict(x=display_length*.4,y=radius*.4,text=f"n₁={n1:g}"),dict(x=display_length*.4,y=2.5*radius,text=f"n₂={n2:g}")],unit="µm",guided=guided,NA=data["NA"],V=data["V"],fiber=True),
        steps=["À l'entrée plane, sin α=n₁ sin θ dans l'air. Au cœur/gaine, l'incidence à la normale vaut i=π/2−θ.",
               "La réflexion totale exige cos θ≥n₂/n₁, avec n₁>n₂. En combinant : sin α≤√(n₁²−n₂²)=NA, tant que NA≤1 pour l'entrée dans l'air.",
               "Le trajet dans une longueur axiale L vaut L/cos θ ; le retard est donc t(θ)=n₁L/(c cos θ).",
               "Entre le rayon axial et la limite critique : Δt=Ln₁(n₁/n₂−1)/c. Ce résultat suppose des indices indépendants de la fréquence.",
               "Extension ondulatoire : V=2πa NA/λvide. La valeur 2,405 est le seuil d'apparition du mode LP₁₁ d'une fibre circulaire en faible guidage ; elle ne découle pas du seul tracé de rayons."],
        assumptions=["Fibre droite à saut d'indice, cœur circulaire, rayons méridiens et indices réels constants. La scène en coupe ignore les rayons gauches et les pertes aux réflexions.",
                     "Pas de dispersion chromatique, courbure, absorption ni couplage entre modes. Δt est un écart géométrique de temps, pas la largeur FWHM d'une impulsion simulée.",
                     "Si n₂≥n₁, l'expérience reste définie mais aucun confinement par réflexion totale n'est possible. Un rayon axial peut traverser la portion représentée sans rencontrer la gaine.",
                     "Le repère V s'applique à une fibre circulaire en faible contraste d'indice ; la géométrie de rayons devient insuffisante lorsque a est comparable à λ."])


def mirage_analytic(x, scale, altitude, theta):
    x=np.asarray(x,dtype=float)
    acceleration=1/(2*(scale+altitude)*math.cos(theta)**2)
    return altitude+math.tan(theta)*x+.5*acceleration*x*x


def mirage_ground_intersection(scale, altitude, theta):
    quadratic=1/(4*(scale+altitude)*math.cos(theta)**2)
    linear=math.tan(theta)
    discriminant=linear*linear-4*quadratic*altitude
    if discriminant < 0 or linear >= 0:
        return None
    # Forme stable de la petite racine lorsque le gradient est presque nul.
    return 2*altitude/(-linear+math.sqrt(max(0.,discriminant)))


def mirage_integrate(scale, altitude, theta, length, count=801):
    """RK4 de z'=w, w'=(1+w²)n'/n, avec n'/n=1/[2(a+z)]."""
    ground=mirage_ground_intersection(scale,altitude,theta)
    end=min(length,ground) if ground is not None else length
    xs=np.linspace(0,end,count)
    states=np.empty((count,2))
    states[0]=[altitude,math.tan(theta)]
    def derivative(state):
        z,w=state
        return np.array([w,(1+w*w)/(2*(scale+z))])
    for k,step in enumerate(np.diff(xs)):
        state=states[k]
        k1=derivative(state)
        k2=derivative(state+.5*step*k1)
        k3=derivative(state+.5*step*k2)
        k4=derivative(state+step*k3)
        states[k+1]=state+step*(k1+2*k2+2*k3+k4)/6
    return xs,states,ground


def compute_mirage(p):
    a,z0,theta,L=p["scale"],p["altitude"],p["angle"]*DEG,p["length"]
    xs,states,ground=mirage_integrate(a,z0,theta,L)
    exact=mirage_analytic(xs,a,z0,theta)
    n=p["n0"]*np.sqrt(1+states[:,0]/a)
    invariant=n/np.sqrt(1+states[:,1]**2)
    original=p["n0"]*math.sqrt(1+z0/a)*math.cos(theta)
    turning=-2*(a+z0)*math.cos(theta)**2*math.tan(theta)
    reached_turn=0 <= turning <= xs[-1]
    paths=[ray(np.column_stack([xs,states[:,0]]),"RK4 : loi du rayon",COLORS[0])]
    for k,offset in enumerate([-.2,.2]):
        other=theta+offset*DEG
        crossing=mirage_ground_intersection(a,z0,other)
        stop=min(L,crossing) if crossing is not None else L
        x=np.linspace(0,stop,401)
        paths.append(ray(np.column_stack([x,mirage_analytic(x,a,z0,other)]),f"Incidence {p['angle']+offset:g}°",COLORS[k+1],opacity=.55))
    apparent_altitude=float(states[-1,0]-xs[-1]*states[-1,1])
    paths.append(ray([[float(xs[-1]),float(states[-1,0])],[0,apparent_altitude]],
                     "Prolongement apparent",COLORS[3],dashed=True,opacity=.7))
    max_z=max(max(point[1] for point in item["points"]) for item in paths)
    max_z=max(1.4*z0,1.08*max_z)
    min_z=min(0.,apparent_altitude)*1.08
    zs=np.linspace(0,max_z,181)
    return dict(metrics=[metric("n cos θ initial",original),metric("Erreur relative maximale de l'invariant",float(np.max(np.abs(invariant/original-1)))),
        metric("Écart maximal numérique / parabole",float(np.max(np.abs(states[:,0]-exact))),"m"),
        metric("Abscisse du retournement",turning if reached_turn else "Non atteint avant le sol ou la limite","m"),
        metric("Altitude minimale atteinte",float(states[:,0].min()),"m"),metric("Rencontre du sol","Non sur le trajet affiché" if ground is None or ground>L else ground,"m"),
        metric("Altitude apparente de la source à x=0",apparent_altitude,"m")],
        charts=[chart("La loi du rayon retrouve une parabole", "Distance horizontale x (m)","Altitude z (m)",series("Intégration de la loi du rayon",xs,states[:,0]),series("Parabole analytique",xs,exact)),
                chart("Un indice qui augmente avec l'altitude", "Altitude z (m)","n(z)−n₀",series("n₀[√(1+z/a)−1]",zs,p["n0"]*(np.sqrt(1+zs/a)-1))),
                chart("Contrôle d'une quantité conservée", "Distance horizontale x (m)","Erreur relative n cosθ / constante − 1",series("Invariant de translation horizontale",xs,invariant/original-1))],
        scene=rays_scene("Un gradient courbe les rayons sans miroir", "Le profil n(z)=n₀√(1+z/a) produit une parabole. Les rayons physiques s'arrêtent au sol ; les pointillés prolongent seulement la tangente reçue par un observateur placé à l'arrivée. Ils indiquent l'altitude apparente de la source à x=0. Les échelles des axes sont différentes.",
            [0,L,min_z,max_z],paths,[element("line",points=[[0,0],[L,0]],label="Sol"),
             element("point",x=float(xs[-1]),y=float(states[-1,0]),label="Observateur"),element("point",x=0,y=apparent_altitude,label="Image apparente")],
            [dict(x=.1*L,y=.88*max_z,text="L'indice augmente vers le haut")],unit="m",profile_z=zs,profile_n=p["n0"]*np.sqrt(1+zs/a),gradient=True,aspect_note="Échelles horizontale et verticale différentes.",ground_intersection=ground,apparent_altitude=apparent_altitude),
        steps=["L'invariance du milieu par translation selon x impose n(z) cos θ=K, puisque θ est mesuré à l'horizontale.",
               "Avec z′=tan θ, K²=n²/(1+z′²). Le profil n²=n₀²(1+z/a) donne z″=1/[2(a+z₀)cos²θ₀].",
               "En intégrant deux fois : z(x)=z₀+x tan θ₀+x²/[4(a+z₀)cos²θ₀]. Le facteur 1/2 de la seconde intégration est nécessaire.",
               "Le calcul numérique intègre directement z′=w et w′=(1+w²)n′/n ; il contrôle ensuite K et l'écart à la solution analytique.",
               "Le retournement z′=0, s'il précède le sol, change une trajectoire descendante en trajectoire ascendante et permet l'interprétation en mirage inférieur.",
               "L'observateur, placé au point d'arrivée (xe,ze), prolonge la direction locale comme une droite : à x=0, zapp=ze−xe z′e. Ce prolongement peut passer sous le sol sans représenter un trajet de lumière."],
        assumptions=["Profil atmosphérique pédagogique prescrit, stratification horizontale et propagation dans un plan vertical. Il ne constitue pas une loi universelle de l'atmosphère chaude.",
                     "La lumière se courbe en continu ; il n'y a pas de surface réfléchissante au retournement. Un mirage complet nécessite de relier source, observateur et prolongement apparent.",
                     "La valeur n₀ multiplie le chemin optique mais ne change pas la forme du rayon pour ce profil ; le contrôle de n₀ illustre cette invariance.",
                     "Les traits correspondent à des trajectoires calculées. L'étirement vertical est explicitement annoncé, les coordonnées et courbes restent en mètres."])


def cauchy_index(wavelength_nm, a, b_um2):
    return a+b_um2/(np.asarray(wavelength_nm,dtype=float)*.001)**2


def refract_vector(direction, normal_to_next, n_from, n_to):
    """Normale orientée vers le milieu suivant ; None indique une réflexion totale."""
    direction=np.asarray(direction,dtype=float)
    normal=np.asarray(normal_to_next,dtype=float)
    direction=direction/np.linalg.norm(direction)
    normal=normal/np.linalg.norm(normal)
    tangent=(direction-np.dot(direction,normal)*normal)*n_from/n_to
    squared=float(tangent@tangent)
    if squared > 1+1e-12:
        return None
    return tangent+math.sqrt(max(0.,1-squared))*normal


def reflect_vector(direction, normal):
    direction=np.asarray(direction,dtype=float)
    normal=np.asarray(normal,dtype=float)
    normal=normal/np.linalg.norm(normal)
    return direction-2*np.dot(direction,normal)*normal


def rainbow_deviation(incidence, index, reflections):
    refraction=np.arcsin(np.sin(incidence)/index)
    return reflections*math.pi+2*incidence-2*(reflections+1)*refraction


def rainbow_stationary(index, reflections):
    q=reflections+1
    sine_squared=(q*q-index*index)/(q*q-1)
    if not 0 <= sine_squared <= 1:
        return None
    incidence=math.asin(math.sqrt(sine_squared))
    deviation=float(rainbow_deviation(incidence,index,reflections))
    radius=math.pi-deviation if reflections==1 else deviation-math.pi
    return incidence,deviation,radius


def rainbow_path(incidence,index,reflections):
    """Réfractions et réflexions exactes dans une sphère unité, coupe méridienne."""
    entry=np.array([-math.cos(incidence),math.sin(incidence)])
    direction=refract_vector([1,0],-entry,1,index)
    vertices=[entry+np.array([-2.,0.]),entry]
    point=entry
    for bounce in range(reflections+1):
        step=-2*float(point@direction)
        point=point+step*direction
        point=point/np.linalg.norm(point)
        vertices.append(point)
        if bounce < reflections:
            direction=reflect_vector(direction,point)
        else:
            direction=refract_vector(direction,point,index,1)
    vertices.append(point+2.5*direction)
    return np.array(vertices),direction


def compute_arcenciel(p):
    m=int(p["reflections"])
    n=float(cauchy_index(p["wavelength"],p["cauchy_a"],p["cauchy_b"]))
    incidence=p["angle"]*DEG
    r=math.asin(math.sin(incidence)/n)
    stationary=rainbow_stationary(n,m)
    rays=[]
    for wavelength,color,label in [(420,COLORS[2],"Violet"),(p["wavelength"],COLORS[1],"λ sélectionnée"),(700,COLORS[0],"Rouge")]:
        index=float(cauchy_index(wavelength,p["cauchy_a"],p["cauchy_b"]))
        path,direction=rainbow_path(incidence,index,m)
        rays.append(ray(path,label,color))
    angles=np.linspace(20,89,361)*DEG
    ds=rainbow_deviation(angles,n,m)
    derivative=2-2*(m+1)*np.cos(angles)/np.sqrt(n*n-np.sin(angles)**2)
    wavelengths=np.linspace(400,750,176)
    indices=cauchy_index(wavelengths,p["cauchy_a"],p["cauchy_b"])
    radii=np.array([rainbow_stationary(float(index),m)[2]/DEG for index in indices])
    minimum_angle,minimum_deviation,angular_radius=stationary
    selected_deviation=float(rainbow_deviation(incidence,n,m))
    path,out=rainbow_path(incidence,n,m)
    scattering=math.acos(float(np.clip(out[0],-1,1)))
    measured_radius=math.pi-scattering
    lims=np.array([point for item in rays for point in item["points"]])
    return dict(metrics=[metric("Indice à λ sélectionnée",n),metric("Incidence stationnaire",minimum_angle/DEG,"°"),
        metric("Rayon angulaire de l'arc à cette λ",angular_radius/DEG,"°"),metric("Déviation du rayon sélectionné",selected_deviation/DEG,"°"),
        metric("Angle à l'axe antisolaire du rayon tracé",measured_radius/DEG,"°"),
        metric("dD/di pour le rayon sélectionné",2-2*(m+1)*math.cos(incidence)/math.sqrt(n*n-math.sin(incidence)**2))],
        charts=[chart("La concentration apparaît à une déviation stationnaire", "Incidence i (°)","Déviation déroulée D (°)",series(f"{m} réflexion(s)",angles/DEG,ds/DEG)),
                chart("Annuler la dérivée pour trouver l'arc", "Incidence i (°)","dD/di",series("2−2(m+1) cos i/[n cos r]",angles/DEG,derivative)),
                chart("Les couleurs ont des rayons angulaires différents", "Longueur d'onde (nm)","Angle à l'axe antisolaire (°)",series("Stationnarité + Cauchy",wavelengths,radii))],
        scene=rays_scene("Une goutte, trois longueurs d'onde", "Le tracé calcule Snell à l'entrée et à la sortie, puis les réflexions spéculaires internes. Le nombre de réflexions distingue l'arc primaire et le secondaire ; seuls les trajets demandés sont montrés.",
            [min(-3.1,lims[:,0].min()-.15),max(2.2,lims[:,0].max()+.15),min(-2.,lims[:,1].min()-.15),max(2.,lims[:,1].max()+.15)],rays,
            [element("circle",x=0,y=0,radius=1,label="Goutte sphérique")],
            [dict(x=-2.8,y=-1.5,text=f"{m} réflexion(s) interne(s)")],unit="rayons de goutte",reflections=m,rainbow=True),
        steps=["Snell donne r=arcsin(sin i/n). Pour m réflexions internes : Dm=mπ+2i−2(m+1)r.",
               "À n fixé, dr/di=cos i/(n cos r), donc dDm/di=2−2(m+1)cos i/(n cos r).",
               "La condition stationnaire impose sin² i=[(m+1)²−n²]/[(m+1)²−1]. Le primaire a m=1 ; le secondaire a m=2.",
               "Le rayon angulaire observé autour de l'axe antisolaire est π−D₁ pour le primaire, D₂−π pour le secondaire au voisinage de la stationnarité.",
               "Cauchy n(λ)=a+b/λ² sépare les angles. Le rouge est à l'extérieur du primaire et à l'intérieur du secondaire, ce que contrôle la courbe spectrale."],
        assumptions=["Goutte sphérique, eau remplacée par une loi de Cauchy pédagogique dans le visible ; aucun indice mesuré n'est revendiqué par ces coefficients.",
                     "La stationnarité concentre géométriquement des rayons, mais l'intensité finie nécessite Fresnel, taille du Soleil, diffraction et distribution des gouttes.",
                     "Les réflexions internes de l'arc ne sont généralement pas totales : le dessin ne calcule pas leur fraction de puissance.",
                     "La déviation D est déroulée et peut dépasser 180°. L'angle observé à l'axe antisolaire est une autre grandeur, calculée séparément."])


def cross2(a,b):
    return a[0]*b[1]-a[1]*b[0]


def prism_path(incidence,index,apex,height=100):
    """Triangle à face d'entrée verticale ; TIR suivie jusqu'à quatre réflexions."""
    width=height*math.tan(apex)
    polygon=np.array([[0.,0.],[width,0.],[0.,height]])
    edges=[(polygon[k],polygon[(k+1)%3]) for k in range(3)]
    point=np.array([0.,height*.25])
    incoming=np.array([math.cos(incidence),math.sin(incidence)])
    direction=refract_vector(incoming,[1,0],1,index)
    vertices=[point-incoming*height,point.copy()]
    previous=2
    exited=False
    first_face=None
    for bounce in range(5):
        intersections=[]
        for edge,(start,end) in enumerate(edges):
            if edge==previous:
                continue
            tangent=end-start
            denominator=cross2(direction,tangent)
            if abs(denominator)<1e-12:
                continue
            delta=start-point
            travel=cross2(delta,tangent)/denominator
            fraction=cross2(delta,direction)/denominator
            if travel>1e-8 and -1e-9 <= fraction <= 1+1e-9:
                intersections.append((travel,edge))
        if not intersections:
            break
        travel,edge=min(intersections)
        point=point+travel*direction
        vertices.append(point.copy())
        if first_face is None:
            first_face=edge
        start,end=edges[edge]
        tangent=end-start
        normal=np.array([tangent[1],-tangent[0]])
        transmitted=refract_vector(direction,normal,index,1)
        if transmitted is not None:
            vertices.append(point+height*transmitted)
            exited=True
            break
        direction=reflect_vector(direction,normal)
        previous=edge
    return np.array(vertices),polygon,exited,first_face


def prism_deviation(incidence,index,apex):
    r=np.arcsin(np.sin(incidence)/index)
    argument=index*np.sin(apex-r)
    valid=np.abs(argument)<=1
    angles=np.arcsin(np.clip(argument,-1,1))
    return incidence+angles-apex,valid


def compute_prisme(p):
    A,i=p["apex"]*DEG,p["angle"]*DEG
    n=float(cauchy_index(p["wavelength"],p["cauchy_a"],p["cauchy_b"]))
    r=math.asin(math.sin(i)/n)
    argument=n*math.sin(A-r)
    emerges=abs(argument)<=1+1e-12
    selected_D=i+math.asin(float(np.clip(argument,-1,1)))-A if emerges else None
    minimum_argument=n*math.sin(A/2)
    exists=minimum_argument<=1
    minimum_i=math.asin(min(1.,minimum_argument)) if exists else None
    minimum_D=2*minimum_i-A if exists else None
    inferred=math.sin((A+minimum_D)/2)/math.sin(A/2) if exists else None
    paths=[]
    polygon=None
    for wavelength,color,label in [(420,COLORS[2],"Violet"),(p["wavelength"],COLORS[1],"λ sélectionnée"),(700,COLORS[0],"Rouge")]:
        index=float(cauchy_index(wavelength,p["cauchy_a"],p["cauchy_b"]))
        vertices,polygon,exited,_=prism_path(i,index,A)
        paths.append(ray(vertices,label,color))
    angles=np.linspace(0,89,441)*DEG
    deviations,valid=prism_deviation(angles,n,A)
    wavelengths=np.linspace(400,750,176)
    indices=cauchy_index(wavelengths,p["cauchy_a"],p["cauchy_b"])
    args=indices*math.sin(A/2)
    valid_spectral=args<=1
    spectral_D=2*np.arcsin(np.clip(args[valid_spectral],-1,1))-A
    bounds_points=np.concatenate([np.array(item["points"]) for item in paths]+[polygon])
    lo=bounds_points.min(axis=0)-15
    hi=bounds_points.max(axis=0)+15
    return dict(metrics=[metric("Indice à λ sélectionnée",n),metric("Angle r dans le prisme",r/DEG,"°"),
        metric("Émergence à la seconde face","Oui" if emerges else "Réflexion totale à cette face"),
        metric("Déviation à la seconde face","Pas de rayon transmis" if selected_D is None else selected_D/DEG,"°"),
        metric("Incidence du minimum","Aucun minimum transmissif" if minimum_i is None else minimum_i/DEG,"°"),
        metric("Déviation minimale","Non accessible" if minimum_D is None else minimum_D/DEG,"°"),
        metric("Indice déduit du minimum","Non applicable" if inferred is None else inferred)],
        charts=[chart("Le mouvement apparent s'inverse au minimum", "Incidence i (°)","Déviation D (°)",series("Émergence à la seconde face",angles[valid]/DEG,deviations[valid]/DEG)),
                chart("Un minimum différent pour chaque couleur", "Longueur d'onde (nm)","Déviation minimale (°)",series("n=a+b/λ²",wavelengths[valid_spectral],spectral_D/DEG))],
        scene=rays_scene("Le prisme disperse ou réfléchit le faisceau", "L'entrée est sur la face verticale et les incidences se mesurent aux normales locales. Le tracé suit aussi des réflexions totales jusqu'à une autre face, avec au plus quatre réflexions représentées.",
            [lo[0],hi[0],lo[1],hi[1]],paths,
            [element("line",points=np.vstack([polygon,polygon[0]]),label="Prisme")],
            [dict(x=polygon[1,0]*.2,y=20,text=f"A={p['apex']:g}°")],unit="mm",prism_vertices=polygon,prism=True),
        steps=["Le rayon intérieur vérifie r=arcsin(sin i/n), r+r′=A et D=i+i′−A, avec sin i′=n sin r′.",
               "L'émergence à la seconde face exige |n sin(A−r)|≤1 ; une réflexion totale peut conduire ensuite le rayon à une autre face.",
               "Au minimum transmissif, le trajet est symétrique : r=r′=A/2 et i=i′. Donc Dmin=2 arcsin[n sin(A/2)]−A.",
               "Le goniomètre mesure A et Dmin. La formule n=sin[(A+Dmin)/2]/sin(A/2) transforme cette mesure en indice.",
               "Cauchy est ici utilisé avec λ exprimée en micromètres et b en µm². Les longueurs d'onde sont celles du vide."],
        assumptions=["Prisme homogène isotrope dans l'air ; réfractions exactes sur des faces planes et loi de Cauchy limitée au visible.",
                     "Aucun minimum transmissif n'existe si n sin(A/2)>1. Le programme signale ce régime plutôt que de produire un arcsinus non réel.",
                     "Les couleurs tracées sont un repère graphique, sans calcul de perception visuelle ni de réflectance de Fresnel. Les faces inférieures ne représentent pas le montage complet d'un goniomètre."])


def mirror_surface(height,radius,kind):
    heights=np.asarray(height,dtype=float)
    if kind=="parabole":
        x=-heights*heights/(2*radius)
        normals=np.column_stack([np.ones_like(heights),heights/radius])
    else:
        x=-radius+np.sqrt(radius*radius-heights*heights)
        normals=np.column_stack([(x+radius)/radius,heights/radius])
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    directions=np.array([reflect_vector([1,0],normal) for normal in normals])
    return x,directions


def mirror_axis_intercept(height,radius,kind):
    heights=np.asarray(height,dtype=float)
    if kind=="parabole":
        return np.full_like(heights,-radius/2)
    return -radius+radius/(2*np.sqrt(1-(heights/radius)**2))


def compute_aberrations(p):
    R,opening,kind=p["radius"],p["opening"],p["surface"]
    aperture=R*opening
    heights=np.linspace(-aperture,aperture,13)
    xs,directions=mirror_surface(heights,R,kind)
    xscreen=-p["screen"]*R
    travel=(xscreen-xs)/directions[:,0]
    yscreen=heights+travel*directions[:,1]
    paths=[]
    for k,(x,y,direction) in enumerate(zip(xs,heights,directions)):
        endpoint=np.array([x,y])+direction*R*.9
        paths.append(ray([[-1.05*R,y],[x,y],endpoint],"Réflexion exacte",COLORS[k%len(COLORS)],opacity=.8))
    cap_y=np.linspace(-aperture*1.04,aperture*1.04,161)
    cap_x,_=mirror_surface(cap_y,R,kind)
    radial=np.linspace(0,aperture,401)
    rx,rd=mirror_surface(radial,R,kind)
    slopes=rd[:,1]/rd[:,0]
    intercept=radial-slopes*rx
    weights=radial
    best_x=-float(np.sum(weights*intercept*slopes)/np.sum(weights*slopes*slopes))
    rms=math.sqrt(float(np.sum(weights*(intercept+slopes*xscreen)**2)/np.sum(weights)))
    best_rms=math.sqrt(float(np.sum(weights*(intercept+slopes*best_x)**2)/np.sum(weights)))
    norms=np.linspace(0,opening,181)
    positions=np.linspace(.3,.7,201)
    rms_by_position=np.sqrt(np.sum(weights[:,None]*(intercept[:,None]-slopes[:,None]*positions[None,:]*R)**2,axis=0)/np.sum(weights))
    marginal_focus=float(mirror_axis_intercept([aperture],R,kind)[0])
    return dict(metrics=[metric("Foyer paraxial, coordonnée x",-R/2,"mm"),metric("Intersection axiale du rayon marginal",marginal_focus,"mm"),
        metric("Aberration longitudinale marginale",marginal_focus+R/2,"mm"),metric("Rayon RMS sur l'écran",rms,"mm"),
        metric("Écran optimal RMS, coordonnée x",best_x,"mm"),metric("Rayon RMS minimal",best_rms,"mm")],
        charts=[chart("Chaque hauteur donne-t-elle le même foyer ?", "Hauteur incidente |y|/R", "Coordonnée du croisement axial / R",series("Sphère exacte",norms,mirror_axis_intercept(norms*R,R,"sphere")/R),series("Paraboloïde",norms,-np.ones_like(norms)/2)),
                chart("Choisir l'écran de moindre tache", "Position de l'écran −x/R", "Rayon RMS (mm)",series("Ouverture circulaire uniformément éclairée",positions,rms_by_position))],
        scene=rays_scene("Une même courbure au sommet ne donne pas le même stigmatisme", "Les normales sont calculées sur la surface ; la réflexion utilise u′=u−2(u·N)N. Le paraboloïde est exactement stigmatique pour le faisceau axial, la sphère l'est seulement dans la limite paraxiale.",
            [-1.1*R,.08*R,-1.2*aperture,1.2*aperture],paths,
            [element("mirror",points=np.column_stack([cap_x,cap_y]),label="Paraboloïde" if kind=="parabole" else "Sphère"),element("screen",x=xscreen,y=0,height=2.2*aperture,label="Écran")],
            [dict(x=-R/2,y=0,text="F paraxial")],unit="mm",mirror=kind,spot_screen=np.column_stack([np.full_like(yscreen,xscreen),yscreen])),
        steps=["Le sommet est en x=0 ; les rayons incidents viennent de la gauche. Le miroir concave sphérique a pour centre (−R,0), donc x(y)=−R+√(R²−y²).",
               "Le paraboloïde de même courbure au sommet a x(y)=−y²/(2R). Calculer les normales puis appliquer la réflexion vectorielle exacte.",
               "Pour la sphère, le croisement axial vaut xF(y)=−R+R/[2√(1−y²/R²)], qui tend vers −R/2 lorsque y/R→0.",
               "Pour le paraboloïde, tous les rayons axiaux arrivent au foyer (−R/2,0). Cet avantage ne garantit pas l'absence de coma pour un objet hors axe.",
               "Le rayon RMS est calculé avec le poids radial r dr d'une ouverture circulaire uniformément éclairée. Son minimum détermine l'écran optimal dans ce critère."],
        assumptions=["Réflexions exactes d'un faisceau axial parallèle sur des surfaces de révolution idéales ; le dessin est une coupe méridienne.",
                     "Pas de diffraction, obstruction, rugosité, inclinaison du faisceau ni chromatisme. La tache géométrique peut être nulle alors qu'un instrument réel conserve une tache de diffraction.",
                     "Le RMS mesure une distribution radiale de rayons, sans convolution de l'image d'un objet étendu. L'écran est un plan d'observation abstrait qui ne bloque pas les rayons incidents dans ce calcul."])


def fermat_path(x,n1,n2,distance,h1,h2):
    x=np.asarray(x,dtype=float)
    return n1*np.hypot(x,h1)+n2*np.hypot(distance-x,h2)


def fermat_derivative(x,n1,n2,distance,h1,h2):
    x=np.asarray(x,dtype=float)
    return n1*x/np.hypot(x,h1)-n2*(distance-x)/np.hypot(distance-x,h2)


def fermat_crossing(n1,n2,distance,h1,h2):
    lo,hi=0.,distance
    for _ in range(80):
        mid=.5*(lo+hi)
        if fermat_derivative(mid,n1,n2,distance,h1,h2)>0:
            hi=mid
        else:
            lo=mid
    return .5*(lo+hi)


def compute_fermat(p):
    n1,n2,D,h1,h2=p["n1"],p["n2"],p["distance"],p["h1"],p["h2"]
    optimum=fermat_crossing(n1,n2,D,h1,h2)
    selected=p["crossing"]*D
    shortest=D*h1/(h1+h2)
    args=(n1,n2,D,h1,h2)
    optical=float(fermat_path(optimum,*args))
    selected_optical=float(fermat_path(selected,*args))
    geometric=float(math.hypot(optimum,h1)+math.hypot(D-optimum,h2))
    i=math.atan2(optimum,h1)
    t=math.atan2(D-optimum,h2)
    xs=np.linspace(-.1*D,1.1*D,301)
    return dict(metrics=[metric("Passage du chemin le plus rapide",optimum,"cm"),metric("Passage du segment le plus court",shortest,"cm"),
        metric("Chemin optique minimal",optical,"cm"),metric("Longueur géométrique au minimum optique",geometric,"cm"),
        metric("Excès de temps du passage sélectionné",(selected_optical-optical)*.01/C*1e12,"ps"),
        metric("n₁sin i − n₂sin t au minimum",n1*math.sin(i)-n2*math.sin(t)),metric("L″ au minimum",n1*h1*h1/(optimum*optimum+h1*h1)**1.5+n2*h2*h2/((D-optimum)**2+h2*h2)**1.5,"cm⁻¹")],
        charts=[chart("Fermat compare les temps de parcours", "Point de passage x (cm)", "Chemin optique L (cm)",series("n₁√(x²+h₁²)+n₂√[(D−x)²+h₂²]",xs,fermat_path(xs,*args))),
                chart("La dérivée s'annule exactement à Snell", "Point de passage x (cm)","dL/dx",series("n₁ sin i−n₂ sin t",xs,fermat_derivative(xs,*args)))],
        scene=rays_scene("Même départ, même arrivée : comparer deux passages", "Le trait turquoise suit le minimum du temps de trajet ; le trait orangé suit le passage choisi. Dans ce montage à deux segments, L est strictement convexe et le minimum est unique.",
            [-.12*D,1.12*D,-1.2*h2,1.2*h1],
            [ray([[0,h1],[selected,0],[D,-h2]],"Passage choisi",COLORS[0]),ray([[0,h1],[optimum,0],[D,-h2]],"Minimum de Fermat",COLORS[1]),
             ray([[0,h1],[D,-h2]],"Segment le plus court",COLORS[2],dashed=True,opacity=.6)],
            [element("line",points=[[-.12*D,0],[1.12*D,0]],label="Interface")],
            [dict(x=0,y=h1,text="A"),dict(x=D,y=-h2,text="B"),dict(x=.1*D,y=.75*h1,text=f"n₁={n1:g}"),dict(x=.75*D,y=-.7*h2,text=f"n₂={n2:g}")],unit="cm",stationary_crossing=optimum),
        steps=["Un point de passage P=(x,0) définit deux segments entre A=(0,h₁) et B=(D,−h₂). Le temps est L(x)/c.",
               "L(x)=n₁√(x²+h₁²)+n₂√[(D−x)²+h₂²]. La dérivée est n₁x/√(x²+h₁²)−n₂(D−x)/√[(D−x)²+h₂²].",
               "Ces rapports sont les sinus des angles à la normale : L′=0 redonne n₁ sin i=n₂ sin t.",
               "L″=n₁h₁²/(x²+h₁²)³ᐟ²+n₂h₂²/[(D−x)²+h₂²]³ᐟ²>0. Le point stationnaire est donc ici un minimum strict unique.",
               "Si n₁=n₂, on retrouve le segment droit. Pour des systèmes optiques plus généraux, Fermat affirme une stationnarité du chemin optique, qui peut être un minimum, un maximum ou un point selle."],
        assumptions=["Deux milieux homogènes transparents et une interface plane ; les points A et B sont situés de part et d'autre.",
                     "Le passage est libre sur la droite entière ; le minimum se trouve entre les projections des extrémités. La courbe montre aussi des chemins en dehors de cet intervalle.",
                     "La comparaison traite uniquement les trajets transmis à deux segments ; elle n'intègre ni diffraction ni amplitude de transmission."])


COMPUTE={"snell":compute_snell,"lentille":compute_lentille,"bessel":compute_bessel,"telescope":compute_telescope,
         "microscope":compute_microscope,"oeil":compute_oeil,"fibre":compute_fibre,"mirage":compute_mirage,
         "arcenciel":compute_arcenciel,"prisme":compute_prisme,"aberrations":compute_aberrations,"fermat":compute_fermat}


def calculate(lab_id,parameters):
    defaults={control["key"]:control["value"] for control in LAB_BY_ID[lab_id]["controls"]}
    defaults.update(parameters)
    return clean(COMPUTE[lab_id](defaults))
