"""Champs, conducteurs et transducteurs : modèles déclarés et bilans contrôlables.

Convention harmonique commune : Re(X̂ exp(−iωt)). Bibliothèque standard + NumPy.
Le validateur central reçoit les entrées publiques ; ce module peut aussi être
appelé directement avec des paramètres partiels pour les tests scientifiques.
"""
import math
import numpy as np

from catalogue_conversion import LAB_BY_ID

C = 299792458.
MU0 = 1.25663706127e-6  # CODATA 2022 ; cohérent avec le moteur d'ondes.
EPS0 = 1/(MU0*C*C)
E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
TAU = 2*math.pi
G = 9.81
K_E = 1/(4*math.pi*EPS0)


def metric(label, value, unit=""):
    return dict(label=label, value=value, unit=unit)


def series(label, x, y):
    return dict(label=label, x=x, y=y)


def chart(title, x_label, y_label, *curves, **extra):
    return dict(title=title, x_label=x_label, y_label=y_label, series=list(curves), **extra)


def field(title, x, y, u, v, scalar, scalar_label, vector="B", **extra):
    return dict(title=title, x=x, y=y, u=u, v=v, scalar=scalar, scalar_label=scalar_label,
                vector_label=vector, vector_unit="T" if vector == "B" else "V·m⁻¹", x_unit="m", y_unit="m", **extra)


def clean(x):
    if isinstance(x, np.ndarray):
        return clean(x.tolist())
    if isinstance(x, np.generic):
        return clean(x.item())
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [clean(v) for v in x]
    if isinstance(x, float) and not math.isfinite(x):
        raise ArithmeticError("Valeur non finie produite par le modèle.")
    if isinstance(x, complex):
        raise ArithmeticError("Un nombre complexe doit être séparé en parties réelle et imaginaire.")
    return x


def calculate(lab, params=None):
    if lab not in LAB_BY_ID:
        raise ValueError("Laboratoire de conversion inconnu.")
    p = {c["key"]: c["value"] for c in LAB_BY_ID[lab]["controls"]}
    if params:
        p.update(params)
    r = globals()["compute_"+lab](p)
    return clean(dict(lab=lab, params=p, **r))


def electric_pair(x, y, q, a, angle=0):
    axis = np.array([math.cos(angle), math.sin(angle)])
    u, v, potential = np.zeros_like(x), np.zeros_like(y), np.zeros_like(x)
    for sign in (1, -1):
        cx, cy = sign*a/2*axis
        dx, dy = x-cx, y-cy
        distance = np.maximum(np.hypot(dx, dy), a*1e-6)
        u += K_E*sign*q*dx/distance**3
        v += K_E*sign*q*dy/distance**3
        potential += K_E*sign*q/distance
    return u, v, potential


def electric_dipole(x, y, moment_x, moment_y):
    r = np.maximum(np.hypot(x, y), 1e-30)
    product = moment_x*x+moment_y*y
    return (K_E*(3*product*x/r**5-moment_x/r**3),
            K_E*(3*product*y/r**5-moment_y/r**3), K_E*product/r**3)


def compute_dipoles(p):
    q, a, angle = p["q"]*1e-9, p["a"], math.radians(p["angle"])
    x = y = np.linspace(-2*a, 2*a, 41)
    X, Y = np.meshgrid(x, y)
    u, v, potential = electric_pair(X, Y, q, a, angle)
    charges = []
    for sign in (1, -1):
        cx, cy = sign*a*math.cos(angle)/2, sign*a*math.sin(angle)/2
        mask = np.hypot(X-cx, Y-cy) <= .09*a
        u[mask] = v[mask] = potential[mask] = 0
        charges.append(dict(x=cx, y=cy, q=sign*q, mask_radius=.09*a))
    ratio = np.geomspace(1, 30, 201)
    radius = a*ratio
    exact_axial = K_E*q*((radius-a/2)**-2-(radius+a/2)**-2)
    approx_axial = 2*K_E*q*a/radius**3
    exact_equator = K_E*q*a/(radius**2+a*a/4)**1.5
    approx_equator = K_E*q*a/radius**3
    rr = p["distance"]
    return dict(metrics=[metric("Moment dipolaire qa", q*a, "C·m"), metric("Erreur relative sur l’axe à r/a choisi", 1-(1-1/(4*rr*rr))**2),
                         metric("Erreur relative sur l’équateur à r/a choisi", (1+1/(4*rr*rr))**1.5-1),
                         metric("Charge totale", 0, "C")],
                charts=[chart("Champ exact et approximation sur l’axe du dipôle", "r/a", "E axial (V·m⁻¹)", series("Deux charges", ratio, exact_axial), series("Dipôle", ratio, approx_axial), x_scale="log", y_scale="log"),
                        chart("Deux directions, une erreur d’ordre (a/r)²", "r/a", "Erreur relative", series("Axe : |Eapprox/Eexact−1|", ratio, 1-approx_axial/exact_axial),
                              series("Équateur : |Eapprox/Eexact−1|", ratio, approx_equator/exact_equator-1), x_scale="log", y_scale="log")],
                field=field("Champ électrique exact et potentiel des deux charges", x, y, u, v, potential, "V (V)", vector="E", charges=charges),
                steps=["Les charges +q et −q sont placées en ±(a/2)ep : p=qa ep, orienté de −q vers +q.",
                       "E(M)=Σqᵢ(M−rᵢ)/(4πε₀|M−rᵢ|³) et V(M)=Σqᵢ/(4πε₀|M−rᵢ|).",
                       "Pour r≫a, Vdip=(p·er)/(4πε₀r²) et Edip=[3(p·er)er−p]/(4πε₀r³).",
                       "La symétrie ±q annule les corrections paires du potentiel : la première erreur relative du champ est d’ordre (a/r)²."],
                assumptions=["Charges ponctuelles fixes dans le vide ; zones proches des charges masquées, où le modèle serait singulier.",
                             "Les flèches représentent E et les lignes orientées un champ statique : aucune trajectoire de charge n’est simulée.",
                             "L’erreur est définie relativement au champ exact et varie avec la direction d’observation."])


def sphere_field(r, charge, radius):
    safe = np.maximum(r, radius)
    E = np.where(r <= radius, K_E*charge*r/radius**3, K_E*charge/safe**2)
    V = np.where(r <= radius, K_E*charge*(3-(r/radius)**2)/(2*radius), K_E*charge/safe)
    return E, V


def compute_gauss(p):
    if p["mode"] == "coax":
        a, b, length, voltage = p["a"]*.01, p["a"]*.01*p["ratio"], p["length"], p["voltage"]
        cap_per_length = TAU*EPS0/math.log(b/a)
        r = np.linspace(a, b, 201)
        electric = voltage/(r*math.log(b/a))
        potential = voltage*np.log(b/r)/math.log(b/a)
        x = y = np.linspace(-1.2*b, 1.2*b, 41)
        X, Y = np.meshgrid(x, y)
        rr = np.hypot(X, Y)
        mask = (rr > a) & (rr < b)
        scale = np.divide(voltage, math.log(b/a)*rr*rr, out=np.zeros_like(rr), where=mask)
        V = np.where(rr <= a, voltage, np.where(rr < b, voltage*np.log(b/np.maximum(rr, a))/math.log(b/a), 0))
        return dict(metrics=[metric("Capacité linéique", cap_per_length, "F·m⁻¹"), metric("Capacité totale", cap_per_length*length, "F"),
                             metric("Charge du conducteur interne", cap_per_length*length*voltage, "C"),
                             metric("Énergie électrique stockée", .5*cap_per_length*length*voltage**2, "J"),
                             metric("Champ au bord interne", voltage/(a*math.log(b/a)), "V·m⁻¹")],
                    charts=[chart("Dans l’isolant du coaxial", "r (cm)", "Champ radial (V·m⁻¹)", series("E∝1/r", r*100, electric)),
                            chart("Le potentiel est logarithmique", "r (cm)", "V relatif au conducteur extérieur (V)", series("V(r)", r*100, potential))],
                    field=field("Coupe d’un condensateur coaxial", x, y, scale*X, scale*Y, V, "V (V)", vector="E", obstacle=dict(r=a, x=0, y=0)),
                    steps=["Un cylindre de Gauss coaxial donne E(r)2πrℓ=λℓ/ε₀, donc E=λ/(2πε₀r).",
                           "V(a)−V(b)=∫ₐᵇEdr=λ ln(b/a)/(2πε₀).",
                           "C/ℓ=2πε₀/ln(b/a), puis Q=CV et U=CV²/2.",
                           "Le champ est nul dans les conducteurs et à l’extérieur du conducteur externe portant la charge opposée."],
                    assumptions=["Conducteurs parfaits concentriques, isolant assimilé au vide, extrémités négligées (ℓ≫b).",
                                 "Le conducteur extérieur est pris comme référence de potentiel ; pas de claquage diélectrique calculé."])
    charge, radius = p["Q"]*1e-9, p["R"]
    r = np.linspace(0, 4*radius, 241)
    electric, potential = sphere_field(r, charge, radius)
    x = y = np.linspace(-2*radius, 2*radius, 41)
    X, Y = np.meshgrid(x, y)
    rr = np.hypot(X, Y)
    er, V = sphere_field(rr, charge, radius)
    scale = np.divide(er, rr, out=np.full_like(rr, K_E*charge/radius**3), where=rr != 0)
    return dict(metrics=[metric("Densité volumique uniforme", charge/(4*math.pi*radius**3/3), "C·m⁻³"),
                         metric("Champ à la surface", K_E*charge/radius**2, "V·m⁻¹"),
                         metric("Potentiel au centre", 1.5*K_E*charge/radius, "V"),
                         metric("Flux total à l’extérieur", charge/EPS0, "V·m"),
                         metric("Énergie électrostatique totale", 3*K_E*charge*charge/(5*radius), "J")],
                charts=[chart("Gauss donne un champ continu à la surface", "r/R", "Er (V·m⁻¹)", series("Sphère chargée en volume", r/radius, electric)),
                        chart("Potentiel référencé à l’infini", "r/R", "V (V)", series("V(r)", r/radius, potential))],
                field=field("Coupe de la sphère isolante chargée en volume", x, y, scale*X, scale*Y, V, "V (V)", vector="E"),
                steps=["La sphère est chargée dans son volume : Qint(r)=Q(r/R)³ pour r<R, Qint=Q pour r≥R.",
                       "4πr²Er=Qint/ε₀ : Er=Qr/(4πε₀R³) à l’intérieur et Q/(4πε₀r²) à l’extérieur.",
                       "En imposant V(∞)=0 et la continuité en R, Vint=Q[3−(r/R)²]/(8πε₀R).",
                       "U=∫ε₀E²/2 dV=3Q²/(20πε₀R) ; une sphère conductrice, chargée seulement en surface, aurait une autre énergie."],
                assumptions=["Distribution isolante uniforme immobile ; aucune réorganisation de charge conductrice n’est supposée.",
                             "Le champ et le potentiel changent de signe avec Q ; l’énergie reste positive."])


def loop_axis(z, radius, current, turns=1, center=0):
    return MU0*turns*current*radius**2/(2*(radius**2+(z-center)**2)**1.5)


def loop_field(x, z, radius, current, turns=1, center=0, segments=256):
    """Biot–Savart par points milieux ; coupe y=0 d'une boucle dans (x,y)."""
    shape = np.shape(x)
    xx, zz = np.ravel(x)[:, None], np.ravel(z)[:, None]-center
    angle = (np.arange(segments)+.5)*TAU/segments
    cosine, sine = np.cos(angle), np.sin(angle)
    dx, dy = xx-radius*cosine, -radius*sine
    distance2 = np.maximum(dx*dx+dy*dy+zz*zz, (radius*1e-8)**2)
    denominator = distance2**1.5
    dphi = TAU/segments
    factor = MU0*turns*current/(4*math.pi)
    bx = factor*np.sum(radius*cosine*zz/denominator, axis=1)*dphi
    bz = factor*np.sum((radius*radius-radius*cosine*xx)/denominator, axis=1)*dphi
    return bx.reshape(shape), bz.reshape(shape)


def mutual_inductance(r1, r2, distance, segments=1024):
    angle = (np.arange(segments)+.5)*TAU/segments
    separation = np.sqrt(r1*r1+r2*r2-2*r1*r2*np.cos(angle)+distance*distance)
    return MU0*r1*r2/2*np.sum(np.cos(angle)/separation)*TAU/segments


def solenoid_axis(z, radius, length, current, turns):
    return MU0*turns*current/(2*length)*((z+length/2)/np.sqrt(radius**2+(z+length/2)**2)
                                             -(z-length/2)/np.sqrt(radius**2+(z-length/2)**2))


def solenoid_field(x, z, radius, length, current, turns, segments=256):
    """Nappe de spires : intégration axiale exacte puis quadrature angulaire."""
    shape = np.shape(x)
    xx, zz = np.ravel(x)[:, None], np.ravel(z)[:, None]
    angle = (np.arange(segments)+.5)*TAU/segments
    cosine, sine = np.cos(angle), np.sin(angle)
    transverse2 = np.maximum((xx-radius*cosine)**2+(radius*sine)**2, (radius*1e-8)**2)
    lower, upper = zz-length/2, zz+length/2
    dlow, dup = np.sqrt(transverse2+lower*lower), np.sqrt(transverse2+upper*upper)
    factor = MU0*turns*current/(4*math.pi*length)*TAU/segments
    bx = factor*np.sum(radius*cosine*(1/dlow-1/dup), axis=1)
    bz = factor*np.sum((radius*radius-radius*cosine*xx)/transverse2*(upper/dup-lower/dlow), axis=1)
    return bx.reshape(shape), bz.reshape(shape)


def compute_biotsavart(p):
    radius, current, length, turns = p["R"], p["I"], p["length"], p["turns"]
    if p["mode"] == "wire":
        r = np.linspace(.03*radius, 3*radius, 201)
        B = MU0*current/(TAU*r)*(length/2)/np.sqrt(r*r+(length/2)**2)
        infinite = MU0*current/(TAU*r)
        x = y = np.linspace(-2*radius, 2*radius, 41)
        X, Y = np.meshgrid(x, y)
        rr = np.hypot(X, Y)
        mask = rr > .08*radius
        scale = np.divide(MU0*current/(TAU)*(length/2), rr*rr*np.sqrt(rr*rr+(length/2)**2), out=np.zeros_like(rr), where=mask)
        magnitude = np.abs(scale)*rr
        return dict(metrics=[metric("Champ à r=R dans le plan médian", MU0*current/(TAU*radius)*(length/2)/math.sqrt(radius**2+(length/2)**2), "T"),
                             metric("Facteur fini / fil infini à r=R", (length/2)/math.sqrt(radius**2+(length/2)**2)),
                             metric("Sens du courant", "+z" if current > 0 else ("−z" if current < 0 else "Courant nul"))],
                    charts=[chart("Contribution d’un segment de fil", "r/R", "Bθ (µT)", series("Segment fini", r/radius, B*1e6), series("Fil infini", r/radius, infinite*1e6))],
                    field=field("Oersted : coupe transverse, fil suivant z", x, y, -scale*Y, scale*X, magnitude, "||B|| (T)", obstacle=dict(r=.08*radius, x=0, y=0)),
                    steps=["Biot–Savart : dB=μ₀I dl×(M−rsource)/(4π|M−rsource|³).",
                           "Au milieu d’un segment de longueur ℓ, Bθ=μ₀I/(2πr)×(ℓ/2)/√[r²+(ℓ/2)²].",
                           "Si r≪ℓ, le facteur tend vers 1 : on retrouve le fil infini et la règle de la main droite.",
                           "Le calcul représente la contribution de ce segment ; le retour du circuit, supposé éloigné, n’est pas représenté."],
                    assumptions=["Magnétostatique, fil fin ; voisinage de l’axe masqué.", "La fermeture du circuit est nécessaire physiquement ; le segment fini ne constitue pas seul un circuit stationnaire fermé."])
    axial_extent = max(length, 3*radius) if p["mode"] == "solenoid" else 6*radius
    field_extent = max(.75*length, 2*radius) if p["mode"] == "solenoid" else 2*radius
    z = np.linspace(-axial_extent, axial_extent, 241)
    xgrid = np.linspace(-1.5*radius, 1.5*radius, 31)
    zgrid = np.linspace(-field_extent, field_extent, 35)
    X, Z = np.meshgrid(xgrid, zgrid)
    mask = np.zeros_like(X, dtype=bool)
    if p["mode"] == "solenoid":
        B = solenoid_axis(z, radius, length, current, turns)
        bx, bz = solenoid_field(X, Z, radius, length, current, turns)
        mask = (np.abs(np.abs(X)-radius) < .08*radius) & (np.abs(Z) <= length/2+.08*radius)
        reference = MU0*turns*current/length
        curves = [series("Solénoïde fini", z/radius, B*1e3), series("Bobine infinie, intérieur seulement", [-length/(2*radius), length/(2*radius)], [reference*1e3]*2)]
        title = "Coupe (x,z) d’un solénoïde continu de longueur finie"
        explanation = "Une densité N/ℓ de spires donne Bz=μ₀NI/(2ℓ)[(z+ℓ/2)/√(R²+(z+ℓ/2)²)−(z−ℓ/2)/√(R²+(z−ℓ/2)²)]."
        field_extra = dict(winding=dict(radius=radius, length=length))
    else:
        B = loop_axis(z, radius, current)
        bx, bz = loop_field(X, Z, radius, current)
        mask = np.hypot(np.abs(X)-radius, Z) < .08*radius
        reference = MU0*current/(2*radius)
        curves = [series("Biot–Savart exact sur l’axe", z/radius, B*1e6)]
        title = "Coupe (x,z) du champ d’une spire"
        explanation = "Sur l’axe d’une spire : Bz(z)=μ₀IR²/[2(R²+z²)³ᐟ²]. Hors axe, la courbe source est intégrée par points milieux."
        field_extra = dict(wires=[dict(x=-radius, y=0, radius=.08*radius), dict(x=radius, y=0, radius=.08*radius)])
    bx[mask] = bz[mask] = 0
    magnetic = np.hypot(bx, bz)
    mutual = mutual_inductance(radius, radius/3, 2*radius)
    unit = "mT" if p["mode"] == "solenoid" else "µT"
    center_b = solenoid_axis(0., radius, length, current, turns) if p["mode"] == "solenoid" else reference
    return dict(metrics=[metric("Champ au centre", center_b, "T"),
                         metric("Inductance mutuelle, R₂=R/3 et d=2R", mutual, "H"),
                         metric("Moment magnétique total", (turns if p["mode"] == "solenoid" else 1)*current*math.pi*radius**2, "A·m²")],
                charts=[chart("Champ sur l’axe", "z/R", f"Bz ({unit})", *curves)],
                field=field(title, xgrid, zgrid, bx, bz, magnetic, "||B|| (T)", x_label="x", y_label="z", **field_extra),
                steps=["Le sens positif du courant est antihoraire vu depuis +z : le champ au centre est alors dirigé vers +z.", explanation,
                       "Le champ hors axe utilise une quadrature de Biot–Savart ; les fils sont exclus de la fenêtre de lecture singulière.",
                       "Deux spires coaxiales ont M=μ₀/(4π)∮∮dl₁·dl₂/r₁₂. Cette expression symétrique explique M₁₂=M₂₁ sans supposer les spires petites."],
                assumptions=["Filaments fins, vide, courants imposés, magnétostatique. Les fils et l’enroulement sont masqués.",
                             "Le solénoïde est une nappe continue de spires : intégration axiale analytique puis quadrature angulaire, sans approximation de bobine infinie.",
                             "La quadrature devient moins précise près des fils ; le voisinage exclu ne doit pas être interprété comme un champ nul physique."])


def compute_helmholtz(p):
    radius, spacing, current, turns = p["R"], p["spacing"]*p["R"], p["I"], p["turns"]
    z = np.linspace(-1.5*radius, 1.5*radius, 241)
    B = loop_axis(z, radius, current, turns, -spacing/2)+loop_axis(z, radius, current, turns, spacing/2)
    center = MU0*turns*current*radius**2/(radius**2+spacing**2/4)**1.5
    curvature = -3*(1-p["spacing"]**2)/(1+p["spacing"]**2/4)**2
    x = y = np.linspace(-.65*radius, .65*radius, 35)
    X, Z = np.meshgrid(x, y)
    bx1, bz1 = loop_field(X, Z, radius, current, turns, -spacing/2)
    bx2, bz2 = loop_field(X, Z, radius, current, turns, spacing/2)
    bx, bz = bx1+bx2, bz1+bz2
    selected = X*X+Z*Z <= (.2*radius)**2
    nonuniformity = np.max(np.hypot(bx[selected], bz[selected]-center))/abs(center) if center else None
    return dict(metrics=[metric("Champ au centre", center, "T"), metric("Courbure normalisée R²B″(0)/B(0)", curvature),
                         metric("Écart vectoriel maximal dans r≤R/5", nonuniformity if nonuniformity is not None else "Champ nul"),
                         metric("Écartement d/R", p["spacing"])],
                charts=[chart("Le réglage d=R annule la courbure centrale", "z/R", "Bz (mT)", series("Deux bobines", z/radius, B*1e3)),
                        chart("Uniformité axiale, référence centrale", "z/R", "Bz/Bcentre", series("Champ normalisé", z/radius, B/center if center else np.zeros_like(B)))],
                field=field("Champ hors axe dans la zone centrale, coupe (x,z)", x, y, bx, bz, bz, "Bz (T)", x_label="x", y_label="z"),
                steps=["Chaque bobine donne Bz=μ₀NIR²/[2(R²+(z∓d/2)²)³ᐟ²]. Les deux contributions s’ajoutent.",
                       "La symétrie annule B′(0). La courbure relative est R²B″(0)/B(0)=−3[1−(d/R)²]/[1+(d/2R)²]².",
                       "À d=R, B″(0)=0 : la première correction axiale est d’ordre (z/R)⁴ et Bcentre=(4/5)³ᐟ²μ₀NI/R.",
                       "Le calcul hors axe vérifie la qualité de la zone utile ; la seule valeur au centre ne mesure pas l’uniformité."],
                assumptions=["Deux bobines identiques coaxiales, fils fins, même courant et même sens d’enroulement.",
                             "La zone tracée est éloignée des conducteurs ; pas de matériau ferromagnétique ni de compensation de champs externes.",
                             "Le champ affiché est vectoriel et statique, sans mouvement de particules."])


def compute_drude(p):
    n, tau, mass, omega, E = 10**p["logn"], p["tau"]*1e-15, p["mass"]*M_E, TAU*p["frequency"]*1e12, p["E"]
    q = -E_CHARGE if p["carrier"] == "electron" else E_CHARGE
    sigma0 = n*q*q*tau/mass
    sigma = sigma0/(1-1j*omega*tau)
    vhat = q*tau*E/(mass*(1-1j*omega*tau))
    relative_time = np.linspace(0, 6, 241)
    velocity = q*tau*E/mass*(-np.expm1(-relative_time))
    current = n*q*velocity
    heat = n*mass*velocity**2/tau
    power = current*E
    rate_kinetic = n*mass*velocity*(q*E/mass-velocity/tau)
    wt = np.geomspace(.001, 1000, 241)
    return dict(metrics=[metric("Conductivité continue σ₀", sigma0, "S·m⁻¹"), metric("Mobilité algébrique qτ/m*", q*tau/mass, "m²·V⁻¹·s⁻¹"),
                         metric("ωτ", omega*tau), metric("Partie réelle de σ(ω)", sigma.real, "S·m⁻¹"),
                         metric("Partie imaginaire de σ(ω), convention −iωt", sigma.imag, "S·m⁻¹"),
                         metric("Retard du courant par rapport à E", math.degrees(math.atan(omega*tau)), "°"),
                         metric("Chaleur moyenne harmonique", .5*sigma.real*E*E, "W·m⁻³"),
                         metric("Énergie cinétique moyenne des porteurs", .25*n*mass*abs(vhat)**2, "J·m⁻³")],
                charts=[chart("Une équation du premier ordre produit σ complexe", "ωτ", "σ/σ₀", series("Re σ", wt, 1/(1+wt*wt)), series("Im σ", wt, wt/(1+wt*wt)), x_scale="log"),
                        chart("Réponse à un échelon, vitesse de dérive signée", "t/τ", "v (m·s⁻¹)", series("Porteurs", relative_time, velocity)),
                        chart("Le courant ne chauffe pas instantanément comme à l’équilibre", "t/τ", "Puissance par volume (W·m⁻³)",
                              series("j·E reçu", relative_time, power), series("Chaleur transmise au réseau", relative_time, heat), series("Variation de l’énergie des porteurs", relative_time, rate_kinetic))],
                scene=dict(kind="drude", omega=omega, tau=tau, field_amplitude=E, sigma_real=sigma.real, sigma_imag=sigma.imag,
                           current_amplitude=abs(sigma*E), current_phase=np.angle(sigma), charge=q,
                           drift_amplitude=abs(vhat), drift_phase=np.angle(vhat)),
                steps=["m* dv/dt=qE−m*v/τ. Avec j=nqv, la conductivité continue σ₀=nq²τ/m* reste positive pour les deux signes de q.",
                       "Sous exp(−iωt), (1/τ−iω)v̂=qÊ/m* et σ(ω)=σ₀/(1−iωτ).",
                       "Après un échelon E, v=(qτE/m*)(1−exp(−t/τ)). Les électrons dérivent en sens opposé au courant.",
                       "j·E=d(nm*v²/2)/dt+nm*v²/τ ; en régime harmonique moyen, chaleur=Re(σ)|Ê|²/2."],
                assumptions=["Porteurs indépendants, masse parabolique isotrope, temps de relaxation constant, faible champ et réponse linéaire.",
                             "Pas de transitions interbandes, de localisation ni de quantification de Hall ; l’application à des fréquences optiques est une limite du modèle.",
                             "La convention complexe est exp(−iωt) ; un changement de convention change le signe de la partie imaginaire."])


def compute_hall(p):
    n, I, B, width, thickness = 10**p["logn"], p["I"], p["B"], p["width"]*1e-3, p["thickness"]*1e-3
    q = -E_CHARGE if p["carrier"] == "electron" else E_CHARGE
    j = I/(width*thickness)
    velocity = j/(n*q)
    ey = velocity*B
    hall_voltage = ey*width
    fields = np.linspace(-2, 2, 161)
    return dict(metrics=[metric("Coefficient de Hall RH=1/(nq)", 1/(n*q), "m³·C⁻¹"),
                         metric("Courant volumique jx", j, "A·m⁻²"), metric("Vitesse de dérive vx", velocity, "m·s⁻¹"),
                         metric("Champ de Hall Ey", ey, "V·m⁻¹"), metric("UH=Vbas−Vhaut suivant y", hall_voltage, "V"),
                         metric("Force électrique transverse par porteur", q*ey, "N"),
                         metric("Force magnétique transverse par porteur", -q*velocity*B, "N")],
                charts=[chart("Le signe de la tension dépend du porteur et des bornes", "Bz (T)", "UH (mV), V(−w/2)−V(+w/2)",
                              series("Électrons", fields, -I*fields/(n*E_CHARGE*thickness)*1e3),
                              series("Trous", fields, I*fields/(n*E_CHARGE*thickness)*1e3))],
                scene=dict(kind="hall", current=I, B=B, width=width, thickness=thickness, carrier=p["carrier"],
                           charge=q, drift=velocity, Ey=ey, UH=hall_voltage),
                steps=["Axes du montage : I suivant +x, largeur w suivant y, épaisseur t suivant z, B=Bz ez.",
                       "j=nqv : un courant positif correspond à vx<0 pour les électrons et vx>0 pour les trous.",
                       "À l’équilibre transverse, q(EH+v×B)=0 ; Ey=vxBz=jxBz/(nq).",
                       "UH est ici V(y=−w/2)−V(y=+w/2)=wEy=IBz/(nqt). Changer les bornes change son signe, pas la physique."],
                assumptions=["Un seul type de porteur, n uniforme, régime stationnaire, plaquette homogène et transverse sans courant jy.",
                             "Le modèle ne calcule pas le régime Hall quantique ni un mélange électrons-trous ; le signe de RH n’est simple que dans cette hypothèse."])


def rail_state(times, mass, resistance, inductance, coupling, v0):
    """Solution exacte du système passif m v'=κi ; L i'=−Ri−κv."""
    A = np.array([[0., coupling/mass], [-coupling/inductance, -resistance/inductance]])
    q = np.trace(A)/2
    N = A-q*np.eye(2)
    determinant = coupling**2/(mass*inductance)
    d = np.lib.scimath.sqrt(q*q-determinant)
    t = np.asarray(times)
    # λ+ = q+d perd la racine lente lorsque κ→0 ; le produit des racines
    # vaut det(A), donc det(A)/λ− conserve cette petite valeur.
    pole_minus = q-d
    pole_plus = determinant/pole_minus if np.isrealobj(d) and pole_minus else q+d
    if abs(d) < 1e-10:
        C = np.exp(q*t)
        S = t*C
    else:
        eplus, eminus = np.exp(pole_plus*t), np.exp(pole_minus*t)
        C, S = (eplus+eminus)/2, (eplus-eminus)/(2*d)
        # Près du pôle double, une différence d'exponentielles perd ses chiffres.
        small = np.abs(d*t) < .1
        C[small] = np.exp(q*t[small])*np.cosh(d*t[small])
        S[small] = np.exp(q*t[small])*np.sinh(d*t[small])/d
    state0 = np.array([v0, 0.])
    states = np.real(C[:, None]*state0+S[:, None]*(N@state0))

    def phi(pole):
        return t if pole == 0 else np.expm1(pole*t)/pole

    if abs(d) < 1e-4*max(abs(q), 1e-10):
        # Intégrer e^(qt)[cosh(dt)−q sinh(dt)/d] en moments analytiques.
        # Le terme d^4 suffit ici : l'erreur est O((d/q)^6), sans annulation
        # de coefficients modaux qui divergeraient près du pôle double.
        moments = [phi(q)]
        small = np.abs(q*t) < 2
        for n in range(1, 6):
            moment = (t**n*np.exp(q*t)-n*moments[-1])/q if q else t**(n+1)/(n+1)
            z = q*t[small]
            term = np.ones_like(z)
            expansion = term/(n+1)
            for j in range(1, 28):
                term *= z/j
                expansion += term/(n+j+1)
            moment[small] = t[small]**(n+1)*expansion
            moments.append(moment)
        position = v0*(moments[0]-q*moments[1]
                       +d*d*(moments[2]/2-q*moments[3]/6)
                       +d**4*(moments[4]/24-q*moments[5]/120))
        position = np.real(position)
    else:
        position = np.real(v0*((1-q/d)*phi(pole_plus)+(1+q/d)*phi(pole_minus))/2)
    return states[:, 0], states[:, 1], position


def frame_entry(t, v0, tau):
    x = np.asarray(t)/tau
    one_minus_exp = -np.expm1(-x)
    remainder = np.where(x < 1e-4, x*x*(.5-x/6+x*x/24-x**3/120), x+np.expm1(-x))
    velocity = v0*np.exp(-x)+G*tau*one_minus_exp
    distance = v0*tau*one_minus_exp+G*tau*tau*remainder
    return distance, velocity


def compute_induction(p):
    B, length, height, R, L, mass, v0, end = p["B"], p["length"], p["height"], p["R"], p["L"]*1e-3, p["mass"]*1e-3, p["v0"], p["duration"]
    coupling = B*length
    times = np.unique(np.r_[np.linspace(0, end, 301), np.geomspace(max(1e-8, min(L/R, end)/100), end, 181)])
    if p["mode"] == "rail":
        velocity, current, position = rail_state(times, mass, R, L, coupling, v0)
        kinetic, magnetic = .5*mass*velocity**2, .5*L*current**2
        initial = .5*mass*v0*v0
        heat = np.maximum(0, initial-kinetic-magnetic)
        force, emf = coupling*current, -coupling*velocity
        return dict(metrics=[metric("Coefficient de conversion κ=Bℓ", coupling, "N·A⁻¹"),
                             metric("Constante électrique L/R", L/R, "s"), metric("Énergie mécanique initiale", initial, "J"),
                             metric("Énergie mécanique finale", kinetic[-1], "J"), metric("Énergie magnétique finale", magnetic[-1], "J"),
                             metric("Chaleur Joule accumulée", heat[-1], "J")],
                    charts=[chart("Le courant induit oppose la variation de flux", "t (s)", "Vitesse (m·s⁻¹)", series("Barreau", times, velocity)),
                            chart("Inductance et retard du courant", "t (s)", "Courant orienté i (A)", series("Courant induit", times, current)),
                            chart("Bilan d’une conversion passive", "t (s)", "Énergie (J)", series("Cinétique", times, kinetic), series("Magnétique LI²/2", times, magnetic),
                                  series("Chaleur accumulée", times, heat), series("Somme conservée", times, kinetic+magnetic+heat))],
                    scene=dict(kind="induction", mode="rail", time=times, position=position, velocity=velocity, current=current, B=B, length=length),
                    steps=["Axes : barreau mobile vers +x, courant positif dans le barreau vers +y, B suivant +z. Le flux positif croît avec x.",
                           "La fém de mouvement vaut e=−Bℓv=−κv et l’équation du circuit est Ldi/dt+Ri=−κv.",
                           "La force de Laplace suivant x est F=κi ; avec i(0)=0, m dv/dt=κi et le système linéaire est résolu exactement.",
                           "d(mv²/2+Li²/2)/dt=−Ri². Si l’inductance restitue de l’énergie, F n’est pas toujours opposée à v : le bilan global reste passif."],
                    assumptions=["Rails parfaits, barreau de masse m, résistance et inductance constantes, champ uniforme, aucune alimentation ni force externe.",
                                 "Le modèle RL peut être sous-amorti et échanger énergie mécanique et magnétique ; il ne faut pas supprimer l’inductance tout en conservant sa phase.",
                                 "La chaleur cumulée est obtenue du bilan exact ; les courbes montrent aussi chaque réservoir d’énergie."])
    if coupling == 0:
        exit_time = (-v0+math.sqrt(v0*v0+2*G*height))/G
        exit_velocity = v0+G*exit_time
        position = v0*times+.5*G*times**2
        velocity = v0+G*times
        current = np.zeros_like(times)
    else:
        tau = mass*R/coupling**2
        high = max(1., end)
        while frame_entry(high, v0, tau)[0] < height:
            high *= 2
        low = 0.
        for _ in range(60):
            mid = (low+high)/2
            if frame_entry(mid, v0, tau)[0] < height:
                low = mid
            else:
                high = mid
        exit_time = (low+high)/2
        exit_velocity = float(frame_entry(exit_time, v0, tau)[1])
        times = np.unique(np.r_[times, exit_time if exit_time <= end else end])
        entering = times < exit_time
        d_entry, v_entry = frame_entry(np.minimum(times, exit_time), v0, tau)
        after = np.maximum(times-exit_time, 0)
        position = np.where(entering, d_entry, height+exit_velocity*after+.5*G*after**2)
        velocity = np.where(entering, v_entry, exit_velocity+G*after)
        current = np.where(entering, -coupling*velocity/R, 0)
    entering = times < exit_time
    flux = coupling*np.minimum(position, height)
    current = np.where(entering, current, 0)
    force = coupling*current
    heat_power = R*current**2
    kinetic = .5*mass*velocity**2
    heat = np.maximum(0, mass*G*position+.5*mass*v0*v0-kinetic)
    return dict(metrics=[metric("Temps d’immersion complète", exit_time, "s"), metric("Vitesse à l’immersion complète", exit_velocity, "m·s⁻¹"),
                         metric("Flux après immersion complète", coupling*height, "Wb"),
                         metric("Chaleur accumulée à la fin", heat[-1], "J"),
                         metric("Régime final après immersion", "Chute libre ; aucune vitesse limite permanente")],
                charts=[chart("L’entrée est freinée ; l’immersion complète ne l’est plus", "t (s)", "Vitesse descendante (m·s⁻¹)", series("Cadre", times, velocity)),
                        chart("Le flux cesse de varier après immersion", "t (s)", "Flux (Wb)", series("B×aire immergée", times, flux)),
                        chart("La puissance gravitationnelle se partage", "t (s)", "Puissance (W)", series("Pesanteur mgv", times, mass*G*velocity),
                              series("Joule Ri²", times, heat_power), series("Variation d’énergie cinétique", times, (mass*G+force)*velocity))],
                scene=dict(kind="induction", mode="frame", time=times, position=position, velocity=velocity, current=current, B=B, length=length, height=height, exit_time=exit_time),
                steps=["Le cadre tombe vers le bas dans une zone semi-infinie de champ Bz. La longueur immergée d varie de 0 à h.",
                       "Pendant l’entrée : Φ=Bℓd, e=−Bℓv et i=e/R. Le freinage est Fvers le bas=−(Bℓ)²v/R.",
                       "m dv/dt=mg−(Bℓ)²v/R jusqu’à d=h. La solution exponentielle n’est valable que pendant cette entrée.",
                       "À d≥h, Φ=Bℓh est constant : e=i=0 dans le modèle résistif, donc dv/dt=g. Une vitesse limite calculée pendant l’entrée ne décrit pas t→∞."],
                assumptions=["Cadre rigide, champ uniforme à frontière nette, résistance constante ; inductance négligée dans ce mode uniquement.",
                             "Au passage de la frontière finale, le courant change brutalement dans cette approximation R seule ; un modèle RL donnerait un bref transitoire.",
                             "Le coefficient L du rail n’est pas utilisé dans ce mode ; un cadre entièrement plongé dans un champ uniforme ne reste pas freiné."])


def speaker_response(frequency, resistance, inductance, mass, stiffness, damping, coupling, voltage):
    omega = TAU*np.asarray(frequency)
    mechanical = damping-1j*(mass*omega-stiffness/omega)
    motional = coupling**2/mechanical
    impedance = resistance-1j*omega*inductance+motional
    current = voltage/impedance
    velocity = coupling*current/mechanical
    displacement = velocity/(-1j*omega)
    return impedance, motional, current, velocity, displacement


def compute_hautparleur(p):
    R, L, mass, stiffness, damping, coupling, f, voltage = p["R"], p["L"]*1e-3, p["mass"]*1e-3, p["stiffness"], p["damping"], p["coupling"], p["frequency"], p["voltage"]
    z, zmot, current, velocity, displacement = speaker_response(f, R, L, mass, stiffness, damping, coupling, voltage)
    power = .5*np.real(voltage*np.conj(current))
    joule, mechanical = .5*R*abs(current)**2, .5*damping*abs(velocity)**2
    resonance = math.sqrt(stiffness/mass)/TAU
    frequencies = np.geomspace(max(1., resonance/20), max(2000., resonance*20), 241)
    zs, zms, currents, vs, xs = speaker_response(frequencies, R, L, mass, stiffness, damping, coupling, voltage)
    return dict(metrics=[metric("Résonance mécanique libre f₀", resonance, "Hz"), metric("Module de l’impédance totale", abs(z), "Ω"),
                         metric("Courant, amplitude crête", abs(current), "A"), metric("Déplacement, amplitude crête", abs(displacement)*1e3, "mm"),
                         metric("Puissance électrique moyenne reçue", power, "W"), metric("Puissance Joule bobine", joule, "W"),
                         metric("Puissance mécanique dissipée", mechanical, "W"), metric("Résidu du bilan moyen", power-joule-mechanical, "W")],
                charts=[chart("La mécanique apparaît dans l’impédance électrique", "f (Hz)", "Impédance (Ω)", series("|Z total|", frequencies, np.abs(zs)),
                              series("Re Z motrice", frequencies, zms.real), x_scale="log"),
                        chart("Réponse mécanique couplée", "f (Hz)", "Déplacement crête (mm)", series("|x̂|", frequencies, np.abs(xs)*1e3), x_scale="log"),
                        chart("Lieu de l’impédance motrice, convention exp(−iωt)", "Re Zmot (Ω)", "Im Zmot (Ω)", series("κ²/Zm", zms.real, zms.imag))],
                scene=dict(kind="speaker", omega=TAU*f, displacement_amplitude=abs(displacement), velocity_amplitude=abs(velocity), current_amplitude=abs(current),
                           phase_x=np.angle(displacement), phase_i=np.angle(current), coupling=coupling),
                steps=["Le même coefficient κ=Bℓ relie force et courant (F=κi) et contre-fém et vitesse (econtre=κv).",
                       "u=Ri+Ldi/dt+κv ; m dv/dt+bv+kx=κi. Le produit κiv transféré entre les deux systèmes s’annule dans le bilan total.",
                       "Sous exp(−iωt), Zm=b−i(mω−k/ω), v̂=κî/Zm et Ztotal=R−iωL+κ²/Zm.",
                       "〈ui〉=R|î|²/2+b|v̂|²/2. La dissipation mécanique n’est pas automatiquement toute une puissance acoustique utile."],
                assumptions=["Transducteur linéaire à paramètres constants, petites excursions, sans non-linéarité de suspension ni échauffement.",
                             "L’amortissement b rassemble les pertes mécaniques et une éventuelle charge acoustique simplifiée ; aucune puissance sonore réelle n’est déduite sans modèle de rayonnement.",
                             "La fréquence de maximum de déplacement sous tension peut différer de √(k/m)/(2π) à cause du couplage électrique."])


def relay_hysteresis(H, coercivities, saturation, reversible_mu=1):
    state = -np.ones(len(coercivities))
    magnetic = []
    for value in H:
        state[value >= coercivities] = 1
        state[value <= -coercivities] = -1
        magnetic.append(MU0*reversible_mu*value+saturation*np.mean(state))
    return np.array(magnetic)


def compute_hysteresis(p):
    hc, amplitude, bs, mur, f, length, area, n1, n2 = p["Hc"], p["amplitude"]*p["Hc"], p["Bs"], p["mur"], p["frequency"], p["length"], p["area"]*1e-4, p["N1"], p["N2"]
    times = np.linspace(0, 1/f, 801)
    H = -amplitude*np.cos(TAU*f*times)
    thresholds = hc*np.linspace(.25, 1.75, 24)
    B = relay_hysteresis(H, thresholds, bs, mur)
    exact_loss = 4*bs*np.mean(np.where(thresholds <= amplitude, thresholds, 0))
    measured_loss = np.sum((H[:-1]+H[1:])/2*np.diff(B))
    dt = np.diff(times)
    secondary = -n2*area*np.diff(B)/dt
    reconstructed = np.r_[B[0], B[0]-np.cumsum(secondary*dt)/(n2*area)]
    primary = H*length/n1
    return dict(metrics=[metric("Nombre de relais magnétiques", len(thresholds)), metric("Énergie perdue par cycle et volume", exact_loss, "J·m⁻³"),
                         metric("Aire mesurée discrète ∮H dB", measured_loss, "J·m⁻³"),
                         metric("Puissance volumique hystérétique", f*exact_loss, "W·m⁻³"),
                         metric("Courant primaire, amplitude", amplitude*length/n1, "A"),
                         metric("Erreur de reconstruction de B", np.max(np.abs(B-reconstructed)), "T")],
                charts=[chart("Mémoire : même H, deux valeurs de B", "H (A·m⁻¹)", "B (T)", series("Banque de relais", H, B), series("Reconstruction depuis e₂", H, reconstructed)),
                        chart("Mesures du TP transformateur, secondaire ouvert", "t (ms)", "Courant primaire (A)", series("i₁=Hℓ/N₁", times*1e3, primary)),
                        chart("Signal secondaire : moyenne sur chaque intervalle", "t (ms)", "Fém e₂ (V)", series("−N₂S ΔB/Δt", (times[:-1]+times[1:])/2*1e3, secondary))],
                scene=dict(kind="hysteresis", H=H, B=B, time=times, Hmax=amplitude, Bs=bs),
                steps=["Le modèle comprend 24 domaines à seuils ±Hc,j, initialement préparés en saturation négative. Chaque domaine conserve son état entre ses deux seuils.",
                       "B=μ₀μrH+Bs〈état〉. La partie réversible ne crée aucune aire de cycle ; la mémoire vient des relais.",
                       "Chaque relais effectivement retourné perd 4Hc,j×son poids magnétique par cycle. La perte totale est ∮H dB≥0.",
                       "Pour un tore à secondaire ouvert : H=N₁i₁/ℓ et e₂=−N₂S dB/dt. Intégrer e₂ retrouve B à une constante d’intégration près."],
                assumptions=["Modèle de relais quasi statique déclaré, non ajusté à un matériau réel. Les cycles mineurs dépendent de la préparation antérieure.",
                             "Les sauts de relais idéaux donnent des impulsions ; la tension tracée est la moyenne sur chaque intervalle de mesure, pas une prédiction de bande passante instrumentale.",
                             "L’aire par cycle ne dépend pas de f dans ce modèle. Courants de Foucault, pertes dynamiques et saturation de la partie réversible ne sont pas calculés."])


def compute_synchrone(p):
    moment, B, f, phase, load, J = p["moment"], p["B"], p["frequency"], math.radians(p["phase"]), p["load"], p["J"]
    tmax, omega = moment*B, TAU*f
    delta = np.linspace(-math.pi, math.pi, 361)
    torque = tmax*np.sin(delta)
    potential = -tmax*np.cos(delta)-load*tmax*delta
    if load < 1:
        stable = math.asin(load)
        unstable = math.pi-stable
        frequency = math.sqrt(tmax*math.cos(stable)/J)/TAU
        stable_value, unstable_value = math.degrees(stable), math.degrees(unstable)
    elif load == 1:
        stable_value = unstable_value = "Point critique : δ=90°, rappel nul"
        frequency = 0.
    else:
        stable_value = unstable_value = "Aucun équilibre verrouillé"
        frequency = "Décrochage statique"
    return dict(metrics=[metric("Couple maximal ℳB", tmax, "N·m"), metric("Couple à la phase choisie", tmax*math.sin(phase), "N·m"),
                         metric("Vitesse synchrone du champ", 60*f, "tr·min⁻¹"), metric("Phase stable d’équilibre", stable_value, "°"),
                         metric("Phase instable d’équilibre", unstable_value, "°"), metric("Fréquence des petites oscillations autour de l’équilibre", frequency, "Hz"),
                         metric("Raideur locale ℳB cosδ, à interpréter à l’équilibre", tmax*math.cos(phase), "N·m·rad⁻¹")],
                charts=[chart("L’angle de charge donne le couple", "Retard mécanique δ (°)", "Couple (N·m)", series("ℳB sinδ", np.degrees(delta), torque),
                              series("Couple résistant", np.degrees(delta), np.full_like(delta, load*tmax))),
                        chart("Potentiel effectif dans le repère tournant", "δ (°)", "Énergie effective (J)", series("−ℳB cosδ−Tchargeδ", np.degrees(delta), potential))],
                scene=dict(kind="motor", mode="synchrone", omega_field=omega, omega_rotor=omega, delta=phase, torque=tmax*math.sin(phase), poles=1),
                steps=["Modèle de dipôle à une paire de pôles : θchamp=Ωst, δ=θchamp−θrotor et Tz=ℳB sinδ.",
                       "Un verrouillage sous charge impose ℳB sinδ=Tcharge. Il existe si |Tcharge|≤ℳB.",
                       "Dans le repère tournant : Jδ″=Tcharge−ℳB sinδ ; près de δs, δ″+[ℳB cosδs/J](δ−δs)=0.",
                       "La branche cosδs>0 est stable ; la branche cosδs<0 est instable. Le schéma tourne à synchronisme imposé pour montrer la phase, sans simuler un lancement."],
                assumptions=["Dipôle dans un champ tournant uniforme, une paire de pôles, couple résistant constant ; pas de saturation ni de pertes.",
                             "La phase choisie n’est un état permanent que si le couple de charge y est équilibré ; la stabilité locale est celle d’un équilibre voisin.",
                             "À Tcharge=Tmax, le rappel linéaire s’annule ; le point critique à 90° n’est pas un équilibre stable de la dynamique non linéaire. Un couple de lancement moyen nul à vitesse imposée non synchrone ne constitue pas une preuve universelle d’impossibilité de démarrage."])


def induction_machine(s, voltage, frequency, poles, r1, r2, l1, l2, lm):
    """Circuit par phase, courant rotorique calculé par admittance sans 1/s."""
    s = np.asarray(s)
    omega = TAU*frequency
    z1 = r1-1j*omega*l1
    ym = 1j/(omega*lm)
    y2 = s/(r2-1j*s*omega*l2)
    gap_voltage = voltage/(1+z1*(ym+y2))
    rotor_current = gap_voltage*y2
    stator_current = gap_voltage*(ym+y2)
    pag = 3*np.abs(gap_voltage)**2*s*r2/(r2*r2+(s*omega*l2)**2)
    pj2 = 3*r2*np.abs(rotor_current)**2
    pj1 = 3*r1*np.abs(stator_current)**2
    mechanical = (1-s)*pag
    received = 3*np.real(voltage*np.conj(stator_current))
    synchronous = omega/poles
    return dict(I1=stator_current, I2=rotor_current, Vgap=gap_voltage, Pag=pag, Pj1=pj1, Pj2=pj2,
                Pm=mechanical, Pin=received, torque=pag/synchronous, omega_rotor=(1-s)*synchronous, omega_sync=synchronous)


def compute_asynchrone(p):
    args = (p["voltage"], p["frequency"], p["poles"], p["R1"], p["R2"], p["L1"]*1e-3, p["L2"]*1e-3, p["Lm"]*1e-3)
    a = induction_machine(p["slip"], *args)
    slips = np.linspace(-.5, 1.5, 401)
    curve = induction_machine(slips, *args)
    return dict(metrics=[metric("Vitesse synchrone", a["omega_sync"]*60/TAU, "tr·min⁻¹"), metric("Vitesse du rotor", a["omega_rotor"]*60/TAU, "tr·min⁻¹"),
                         metric("Courant rotorique référé, efficace", abs(a["I2"]), "A"), metric("Couple électromagnétique", a["torque"], "N·m"),
                         metric("Puissance d’entrefer Pag", a["Pag"], "W"), metric("Pertes Joule au rotor sPag", a["Pj2"], "W"),
                         metric("Puissance mécanique convertie (1−s)Pag", a["Pm"], "W"), metric("Résidu Pin−Pjstator−Pag", a["Pin"]-a["Pj1"]-a["Pag"], "W")],
                charts=[chart("Le couple change de signe au synchronisme", "Glissement s", "Couple (N·m)", series("Circuit triphasé", slips, curve["torque"])),
                        chart("Le flux d’entrefer se partage", "Glissement s", "Puissance (W)", series("Entrefer Pag", slips, curve["Pag"]),
                              series("Joule rotor", slips, curve["Pj2"]), series("Conversion mécanique", slips, curve["Pm"]))],
                scene=dict(kind="motor", mode="asynchrone", omega_field=a["omega_sync"], omega_rotor=a["omega_rotor"], delta=0, torque=a["torque"], slip=p["slip"], poles=p["poles"]),
                steps=["Alimentation triphasée équilibrée, valeurs efficaces par phase. Ωs=2πf/p et s=(Ωs−Ωr)/Ωs.",
                       "Circuit référé : Z₁=R₁−iωL₁, Ym=i/(ωLm), Y₂=s/(R₂−isωL₂). Cette forme traite exactement s=0.",
                       "Vg=V/[1+Z₁(Ym+Y₂)], I₂=VgY₂. Pag=3|Vg|²sR₂/[R₂²+(sωL₂)²] et Tem=Pag/Ωs.",
                       "Pjr=sPag≥0 et Pm=(1−s)Pag=TemΩr ; Pin=Pjstator+Pag. Le couple moyen ne dépend pas d’une phase initiale arbitraire."],
                assumptions=["Circuit équivalent linéaire sinusoïdal permanent, vitesse imposée, triphasé équilibré ; paramètres référés au stator.",
                             "Pas de pertes fer, frottement, ventilation ni saturation. Lm représente une branche magnétisante purement réactive.",
                             "0<s<1 : moteur ; s<0 : génératrice ; s>1 : freinage avec rotor inversé. À s=0, le courant rotorique et le couple s’annulent mais le stator magnétise toujours."])


def erfc_array(x):
    return np.array([math.erfc(float(y)) for y in np.ravel(x)]).reshape(np.shape(x))


def compute_peau(p):
    sigma, mu, B0, f, t = p["sigma"]*1e6, MU0*p["mur"], p["B"]*1e-3, 10**p["logf"], p["time"]*1e-3
    D, omega = 1/(mu*sigma), TAU*f
    delta = math.sqrt(2*D/omega)
    if p["mode"] == "step":
        depth = np.linspace(0, 6*math.sqrt(D*t), 241)
        values = B0*erfc_array(depth/(2*math.sqrt(D*t)))
        current = -B0/(mu*math.sqrt(math.pi*D*t))*np.exp(-depth**2/(4*D*t))
        received = B0*B0/(mu*mu*sigma*math.sqrt(math.pi*D*t))
        heat = received/math.sqrt(2)
        stored = B0*B0/mu*math.sqrt(D*t)*(2-math.sqrt(2))/math.sqrt(math.pi)
        curves = [series(f"t={factor*t*1e3:g} ms", depth*1e3, B0*erfc_array(depth/(2*math.sqrt(D*t*factor)))*1e3) for factor in (.25, 1, 4)]
        return dict(metrics=[metric("Diffusivité magnétique D=1/(μσ)", D, "m²·s⁻¹"), metric("Longueur de pénétration 2√(Dt)", 2*math.sqrt(D*t)*1e3, "mm"),
                             metric("Puissance reçue à la surface", received, "W·m⁻²"), metric("Puissance Joule intégrée", heat, "W·m⁻²"),
                             metric("Croissance de l’énergie magnétique", received-heat, "W·m⁻²"), metric("Énergie magnétique par aire à t", stored, "J·m⁻²")],
                    charts=[chart("Un champ continu pénètre de plus en plus loin", "Profondeur x (mm)", "By (mT)", *curves),
                            chart("Courant de diffusion", "Profondeur x (mm)", "jz (A·m⁻²)", series("∂xBy/μ", depth*1e3, current))],
                    scene=dict(kind="skin", mode="step", diffusivity=D, omega=0, B0=B0, x=depth, field=values, physical_time=t),
                    steps=["Dans le métal normal, sans courant de déplacement, ∂tB=DΔB avec D=1/(μσ).",
                           "Un échelon By(0,t)=B₀, avec B initialement nul dans x>0, donne By=B₀erfc[x/(2√Dt)].",
                           "jz=∂xBy/μ=−B₀exp[−x²/(4Dt)]/(μ√πDt). L’énergie reçue se partage entre chaleur et champ magnétique croissant.",
                           "La longueur 2√Dt augmente sans borne : cette diffusion d’un métal normal ne décrit pas l’expulsion statique de Meissner."],
                    assumptions=["Demi-espace homogène, μ et σ réels constants, approximation magnétique quasi statique ; t>0.",
                                 "L’échelon instantané est idéalisé ; la singularité du courant à t=0 est évitée par le temps strictement positif.",
                                 "La fréquence f n’est pas utilisée dans le mode échelon ; la longueur de London appartient à un autre modèle."])
    depth = np.linspace(0, 6*delta, 241)
    magnetic = B0*np.exp((-1+1j)*depth/delta)
    current = (-1+1j)*magnetic/(mu*delta)
    rs = 1/(sigma*delta)
    received = .5*rs*(B0/mu)**2
    return dict(metrics=[metric("Épaisseur de peau δ", delta*1e3, "mm"), metric("Diffusivité magnétique", D, "m²·s⁻¹"),
                         metric("Résistance de surface", rs, "Ω"), metric("Réactance de surface, convention −iωt", -rs, "Ω"),
                         metric("Courant volumique à la surface, amplitude", abs(current[0]), "A·m⁻²"),
                         metric("Flux énergétique entrant moyen", received, "W·m⁻²"), metric("Puissance Joule totale moyenne", received, "W·m⁻²"),
                         metric("Rapport courant de déplacement / conduction", EPS0*omega/sigma)],
                charts=[chart("Atténuation et retard spatial du champ harmonique", "x/δ", "By (mT)", series("À t=0", depth/delta, magnetic.real*1e3),
                              series("Enveloppe", depth/delta, np.abs(magnetic)*1e3), series("Enveloppe négative", depth/delta, -np.abs(magnetic)*1e3)),
                        chart("Le courant et la chaleur sont localisés", "Profondeur x (mm)", "Chaleur moyenne (W·m⁻³)", series("|ĵ|²/(2σ)", depth*1e3, np.abs(current)**2/(2*sigma)))],
                scene=dict(kind="skin", mode="harmonic", delta=delta, diffusivity=D, omega=omega, B0=B0, x=depth, field=magnetic.real, envelope=np.abs(magnetic)),
                steps=["Pour By suivant y dans x>0 : ∂tBy=D∂²xBy. Sous exp(−iωt), le nombre d’onde passif est k=(1+i)/δ.",
                       "δ=√[2/(μσω)] et B̂y=B₀exp[(−1+i)x/δ]. L’amplitude décroît et la phase varie dans le métal.",
                       "ĵz=∂xB̂y/μ ; avec E suivant z, le flux entrant est −Re(ÊzĤy*)/2. L’impédance orientée est Zs=−Êz/Ĥy=(1−i)/(σδ).",
                       "∫₀∞|ĵ|²/(2σ)dx=Re(Zs)|Ĥ(0)|²/2 : tout le flux entrant est dissipé dans le demi-espace établi."],
                assumptions=["Bon conducteur homogène semi-infini, μ et σ constants, courant de déplacement négligeable ; champ tangentiel imposé à la surface.",
                             "μr est un paramètre linéaire idéal ; dispersion de la perméabilité, saturation et hystérésis ne sont pas ajoutées arbitrairement.",
                             "δ∝f⁻¹ᐟ² diverge quand f→0 ; une longueur de London statique finie est un effet supraconducteur distinct."])
