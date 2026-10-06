"""Modèles pédagogiques de fluides et d'ondes, NumPy et bibliothèque standard.

Les équations ont des domaines de validité indiqués dans chaque résultat.
Un tracé exact dans un modèle simplifié n'est pas une simulation universelle.
"""
from functools import lru_cache
import math

import numpy as np

from catalogue import LAB_BY_ID

G = 9.81
R_GAS = 8.31446261815324
MU0 = 4 * math.pi * 1e-7
TAU = 2 * math.pi


def parameters(data):
    if not isinstance(data, dict):
        raise ValueError("Le calcul attend un objet contenant lab et params.")
    lab_id = data.get("lab")
    if not isinstance(lab_id, str) or lab_id not in LAB_BY_ID:
        raise ValueError("Laboratoire inconnu.")
    supplied = data.get("params", {k: v for k, v in data.items() if k != "lab"})
    if not isinstance(supplied, dict):
        raise ValueError("Les paramètres doivent former un objet.")
    controls = LAB_BY_ID[lab_id]["controls"]
    if set(supplied) - {c["key"] for c in controls}:
        raise ValueError("Un paramètre n'appartient pas à ce laboratoire.")
    result = {}
    for control in controls:
        key = control["key"]
        value = supplied.get(key, control["value"])
        if control["type"] == "select":
            if not isinstance(value, str) or value not in {o["value"] for o in control["options"]}:
                raise ValueError(f"Choix invalide : {control['label']}.")
        else:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"Nombre attendu : {control['label']}.")
            try:
                value = float(value)
            except OverflowError as exc:
                raise ValueError(f"Nombre non fini : {control['label']}.") from exc
            if not math.isfinite(value) or not control["min"] <= value <= control["max"]:
                raise ValueError(f"{control['label']} doit rester entre {control['min']} et {control['max']} {control['unit']}.")
            if key in ("m", "n") and not value.is_integer():
                raise ValueError("Les indices de modes sont des entiers.")
        result[key] = value
    return lab_id, result


def metric(label, value, unit=""):
    return {"label": label, "value": value, "unit": unit}


def series(label, x, y):
    return {"label": label, "x": x, "y": y}


def chart(title, xlabel, ylabel, *curves, **scales):
    return {"title": title, "x_label": xlabel, "y_label": ylabel,
            "series": list(curves), **scales}


def field(title, x, y, u, v, scalar, scalar_label, **extra):
    return dict(title=title, x=x, y=y, u=u, v=v, scalar=scalar,
                scalar_label=scalar_label, x_unit="m", y_unit="m",
                velocity_unit="m·s⁻¹", **extra)


def profile(coordinate, velocity, geometry="plane", wall_speed=0):
    return {"kind": "profile", "coordinate": coordinate, "velocity": velocity,
            "geometry": geometry, "wall_speed": wall_speed}


def clean(value):
    """Ne laisse passer ni NaN/inf, ni scalaires NumPy dans le protocole JSON."""
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, np.generic):
        return clean(value.item())
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ArithmeticError("Un calcul a produit une valeur non finie.")
    return value


def calculate(data):
    lab_id, p = parameters(data)
    r = globals()["compute_" + lab_id](p)
    return clean({"lab": lab_id, "params": p, **r})


def compute_cinematique(p):
    a, w, U, L, duration = (p[k] for k in ("a", "omega", "U", "L", "time"))
    x = y = np.linspace(-L, L, 37)
    X, Y = np.meshgrid(x, y)
    u, v = U + a*X-w*Y, w*X-a*Y
    psi = U*Y+a*X*Y-w*(X*X+Y*Y)/2
    times = np.linspace(0, duration, 161)
    A = np.array([[a, -w], [w, -a]])
    d = a*a-w*w
    trajectories = []
    for initial in (np.array([L/3, 0.]), np.array([0., L/3]), np.array([-L/3, -L/3])):
        coords = []
        for t in times:
            if abs(d) < 1e-12:
                C, S, J = 1., t, t*t/2
            elif d > 0:
                q = math.sqrt(d)
                C, S, J = math.cosh(q*t), math.sinh(q*t)/q, (math.cosh(q*t)-1)/d
            else:
                q = math.sqrt(-d)
                C, S, J = math.cos(q*t), math.sin(q*t)/q, (math.cos(q*t)-1)/d
            coords.append((C*np.eye(2)+S*A)@initial + (S*np.eye(2)+J*A)@np.array([U, 0.]))
        coords = np.array(coords)
        trajectories.append(series(f"Départ ({initial[0]:.2g} ; {initial[1]:.2g}) m", coords[:, 0], coords[:, 1]))
    return dict(metrics=[metric("Divergence", 0, "s⁻¹"), metric("Vorticité ωz", 2*w, "s⁻¹"),
                          metric("Déformation principale", abs(a), "s⁻¹"), metric("Rotation locale", w, "rad·s⁻¹")],
                charts=[chart("Trajectoires exactes dans le champ stationnaire", "x (m)", "y (m)", *trajectories)],
                field=field("Champ v et fonction de courant ψ", x, y, u, v, psi, "ψ (m²·s⁻¹)"),
                steps=["v=(U+ax−Ωy, Ωx−ay), donc ∂xvx+∂yvy=a−a=0.",
                       "ψ=Uy+axy−Ω(x²+y²)/2 vérifie vx=∂yψ et vy=−∂xψ.",
                       "La trajectoire résout dr/dt=Ar+(U,0). Comme A²=(a²−Ω²)I, l’exponentielle se calcule par cos/cosh.",
                       "Le champ étant stationnaire, chaque trajectoire reste sur une ligne ψ constante."],
                assumptions=["Champ plan stationnaire, sans paroi ni modèle dynamique imposé.",
                             "Une trajectoire peut sortir de la fenêtre ; le champ linéaire reste défini au-delà."])


def compute_newtonien(p):
    eta, rho, s, a, w = p["eta"]*1e-3, p["rho"], p["shear"], p["a"], p["omega"]
    D = np.array([[a, s/2], [s/2, -a]])
    tau = 2*eta*D
    diss = 2*eta*np.sum(D*D)
    rates = np.linspace(-20, 20, 161)
    x = y = np.linspace(-.1, .1, 31)
    X, Y = np.meshgrid(x, y)
    u, v = a*X+(s-w)*Y, w*X-a*Y
    return dict(metrics=[metric("Viscosité cinématique ν=η/ρ", eta/rho, "m²·s⁻¹"),
                          metric("Contrainte τxy", tau[0, 1], "Pa"),
                          metric("Contrainte τxx", tau[0, 0], "Pa"),
                          metric("Dissipation τ:D", diss, "W·m⁻³"),
                          metric("Vorticité du champ", 2*w-s, "s⁻¹")],
                charts=[chart("Loi de cisaillement newtonienne", "γ̇ (s⁻¹)", "τxy (Pa)", series("τxy=ηγ̇", rates, eta*rates)),
                        chart("La rotation rigide ne dissipe pas", "Ω ajouté (rad·s⁻¹)", "Dissipation (W·m⁻³)",
                              series("τ:D indépendant de Ω", rates/2, np.full_like(rates, diss)))],
                field=field("Déformation et rotation superposées", x, y, u, v, np.hypot(u, v), "||v|| (m·s⁻¹)"),
                steps=["On choisit ∇v=[[a,γ̇−Ω],[Ω,−a]], de trace nulle.",
                       "Sa partie symétrique est D=[[a,γ̇/2],[γ̇/2,−a]] : la rotation ajoutée s’annule.",
                       "τ=2ηD ; η est la viscosité dynamique en Pa·s, ν=η/ρ est la viscosité cinématique.",
                       "τ:D=2ηD:D=η(4a²+γ̇²)≥0. La pression isotrope n’est pas incluse dans τ."],
                assumptions=["Fluide newtonien incompressible, η constante ; aucun modèle de seuil ni de rhéofluidification.",
                             "Pour un fluide compressible, la viscosité volumique et div(v) demandent un terme supplémentaire."])


def compute_couette(p):
    h, eta, U, V, gp = p["h"]*1e-3, p["eta"]*1e-3, p["U0"], p["U1"], p["G"]
    y = np.linspace(0, h, 201)
    u = U+(V-U)*y/h+gp*y*(h-y)/(2*eta)
    shear = eta*(V-U)/h+gp*(h/2-y)
    q = h*(U+V)/2+gp*h**3/(12*eta)
    wall = V*shear[-1]-U*shear[0]
    diss = eta*(V-U)**2/h+gp**2*h**3/(12*eta)
    return dict(metrics=[metric("Débit par unité de largeur", q, "m²·s⁻¹"),
                          metric("Vitesse moyenne", q/h, "m·s⁻¹"), metric("Cisaillement au mur bas", shear[0], "Pa"),
                          metric("Puissance de pression par aire", gp*q, "W·m⁻²"),
                          metric("Puissance des parois par aire", wall, "W·m⁻²"),
                          metric("Dissipation intégrée", diss, "W·m⁻²"),
                          metric("Résidu du bilan de puissance", gp*q+wall-diss, "W·m⁻²")],
                charts=[chart("Entraînement et pression se superposent", "y (mm)", "vx (m·s⁻¹)",
                              series("Profil total", y*1e3, u), series("Couette seul", y*1e3, U+(V-U)*y/h),
                              series("Pression seule", y*1e3, gp*y*(h-y)/(2*eta))),
                        chart("Contrainte tangentielle", "y (mm)", "τxy (Pa)", series("η du/dy", y*1e3, shear))],
                scene=profile(y, u, wall_speed=U),
                steps=["Navier–Stokes se réduit à ηu''=−G, avec G=−dp/dx ; le terme convectif est nul.",
                       "Les conditions d’adhérence u(0)=U₀ et u(h)=U₁ donnent une droite plus une parabole.",
                       "q=∫₀ʰu dy=h(U₀+U₁)/2+Gh³/(12η) ; q=0 peut coexister avec u non nul.",
                       "Gq+U₁τ(h)−U₀τ(0)=∫₀ʰη(u')²dy : le signe du travail de chaque paroi compte."],
                assumptions=["Écoulement plan, stationnaire, pleinement développé, fluide newtonien incompressible.",
                             "Puissances par aire de canal ; débit par unité de largeur. La stabilité de l’écoulement n’est pas calculée."])


def compute_poiseuille(p):
    rad, length, dp, eta, rho = p["R"]*1e-3, p["L"], p["dp"], p["eta"]*1e-3, p["rho"]
    r = np.linspace(0, rad, 201)
    umax = dp*rad**2/(4*eta*length)
    velocity = umax*(1-(r/rad)**2)
    q = math.pi*rad**4*dp/(8*eta*length)
    re = rho*(umax/2)*2*rad/eta
    xs = np.linspace(0, length, 101)
    assumptions = ["Tube droit circulaire horizontal, adhérence, régime stationnaire pleinement développé et laminaire.",
                   "Δp=pentrée−psortie>0. Pour un tube incliné, remplacer la pression par p+ρgz.",
                   "Re porte sur le diamètre et la vitesse moyenne. Le seuil de transition dépend des perturbations."]
    if re > 2300:
        assumptions.append("Ce réglage dépasse Re=2300 : le profil laminaire affiché est une solution formelle, sa réalisation stable n’est pas garantie.")
    return dict(metrics=[metric("Débit-volume Q", q, "m³·s⁻¹"), metric("Vitesse moyenne", umax/2, "m·s⁻¹"),
                          metric("Vitesse axiale maximale", umax, "m·s⁻¹"), metric("Nombre de Reynolds", re),
                          metric("Résistance hydraulique Δp/Q", dp/q, "Pa·s·m⁻³"),
                          metric("Puissance dissipée Δp Q", dp*q, "W"),
                          metric("Longueur d’entrée estimée 0,05 Re D", .05*re*2*rad, "m")],
                charts=[chart("Profil radial et moyenne", "r (mm)", "u (m·s⁻¹)", series("u(r)", r*1e3, velocity),
                              series("u moyenne", r*1e3, np.full_like(r, umax/2))),
                        chart("Pression relative à la sortie", "x (m)", "p(x)−psortie (Pa)", series("Chute linéaire", xs, dp*(1-xs/length)))],
                scene=profile(r, velocity, geometry="tube"),
                steps=["0=−dp/dx+η(r⁻¹∂r(r∂ru)) ; la régularité à r=0 élimine le terme logarithmique.",
                       "Avec u(R)=0 et dp/dx=−Δp/L : u(r)=Δp(R²−r²)/(4ηL).",
                       "Q=2π∫₀ᴿu(r)rdr=πΔpR⁴/(8ηL), puis ū=Q/(πR²)=umax/2.",
                       "L’intégrale de dissipation visqueuse vaut Δp Q. Doubler R multiplie Q par 16 à Δp fixé."],
                assumptions=assumptions)


def erfc_array(x):
    return np.array([math.erfc(float(item)) for item in np.ravel(x)]).reshape(np.shape(x))


def diffusion_profile(y, U, nu, t, h=None):
    d = 2*math.sqrt(nu*t)
    if h is None:
        return U*erfc_array(y/d)
    fo = nu*t/h**2
    if fo < .03:
        # Méthode des images : pas de troncature de Fourier oscillante au démarrage.
        answer = np.zeros_like(y)
        for n in range(8):
            answer += erfc_array((2*n*h+y)/d)-erfc_array((2*(n+1)*h-y)/d)
        return U*answer
    n = np.arange(1, 101)[:, None]
    transient = np.sum(2/(n*math.pi)*np.sin(n*math.pi*y[None, :]/h)*np.exp(-n*n*math.pi**2*fo), axis=0)
    answer = U*(1-y/h-transient)
    answer = np.where(y == 0, U, answer)
    answer = np.where(y == h, 0., answer)
    return answer


def compute_diffusion(p):
    U, nu, h, t = p["U"], p["nu"]*1e-6, p["h"]*1e-3, p["time"]
    finite = p["geometry"] == "finite"
    y = np.linspace(0, h, 241)
    velocity = diffusion_profile(y, U, nu, t, h if finite else None)
    d = 2*math.sqrt(nu*t)
    curves = [series(f"t={factor*t:.3g} s", y*1e3, diffusion_profile(y, U, nu, factor*t, h if finite else None))
              for factor in (.25, 1, 4)]
    if finite:
        curves.append(series("Couette final", y*1e3, U*(1-y/h)))
    return dict(metrics=[metric("Longueur diffusive δ=2√(νt)", d*1e3, "mm"),
                          metric("Temps diffusif h²/ν", h*h/nu, "s"),
                          metric("Nombre de Fourier νt/h²", nu*t/h**2),
                          metric("Vitesse au bord de fenêtre", velocity[-1], "m·s⁻¹")],
                charts=[chart("Diffusion de la quantité de mouvement", "y (mm)", "u (m·s⁻¹)", *curves)],
                scene=profile(y, velocity, wall_speed=U),
                steps=["Un champ v=u(y,t)ex a un terme convectif nul : ∂tu=ν∂²yu.",
                       "Dans le demi-espace, u(0,t)=U et u(y→∞,t)=0 donnent u/U=erfc(y/(2√νt)).",
                       "Deux parois imposent u(h,t)=0 : la solution est une série de modes sin(nπy/h) amortis.",
                       "Le régime final entre parois est Couette, u=U(1−y/h), alors que le demi-espace continue à s’épaissir."],
                assumptions=["Fluide initialement au repos, mise en mouvement instantanée de la paroi à t=0 ; ici t>0.",
                             "δ est une longueur caractéristique, pas une frontière nette. Le modèle fini et le demi-espace sont sélectionnés séparément.",
                             "Les solutions analytiques sont évaluées par images au début et série de Fourier ensuite dans le canal fini."])


@lru_cache(maxsize=1)
def blasius_solution():
    """RK4 + tir bissecté : f'''+f f''/2=0, f'(12)=1."""
    xi = np.linspace(0, 12, 1201)
    step = xi[1]-xi[0]

    def integrate(slope, keep=False):
        state = np.array([0., 0., slope])
        states = [state.copy()] if keep else None
        def rhs(q):
            return np.array([q[1], q[2], -.5*q[0]*q[2]])
        for _ in xi[1:]:
            k1 = rhs(state)
            k2 = rhs(state+step*k1/2)
            k3 = rhs(state+step*k2/2)
            k4 = rhs(state+step*k3)
            state += step*(k1+2*k2+2*k3+k4)/6
            if keep:
                states.append(state.copy())
        return np.array(states) if keep else state[1]

    low, high = .3, .4
    for _ in range(34):
        mid = (low+high)/2
        if integrate(mid) < 1:
            low = mid
        else:
            high = mid
    return xi, integrate((low+high)/2, keep=True)


def compute_blasius(p):
    U, nu, x, rho = p["U"], p["nu"]*1e-6, p["x"], p["rho"]
    xi, f = blasius_solution()
    scale = math.sqrt(nu*x/U)
    re = U*x/nu
    slope = f[0, 2]
    d99 = np.interp(.99, f[:, 1], xi)*scale
    displacement = np.trapezoid(1-f[:, 1], xi) if hasattr(np, "trapezoid") else np.trapz(1-f[:, 1], xi)
    momentum = np.trapezoid(f[:, 1]*(1-f[:, 1]), xi) if hasattr(np, "trapezoid") else np.trapz(f[:, 1]*(1-f[:, 1]), xi)
    xs = np.linspace(max(.001, x/20), x*1.5, 100)
    curves = [series(f"x={xx:.3g} m", xi*math.sqrt(nu*xx/U)*1e3, U*f[:, 1]) for xx in (x/4, x, x*1.5)]
    assumptions = ["Plaque plane semi-infinie, gradient de pression extérieur nul, fluide newtonien incompressible, couche limite laminaire.",
                   "Similitude η=y√(U∞/(νx)) ; modèle hors du bord d’attaque, à Reₓ suffisamment grand et avant transition.",
                   "RK4 avec pas 0,01 et tir jusqu’à η=12 ; f''(0)≈0,332057336. L’amortissement numérique n’est pas un modèle turbulent."]
    if re > 500000:
        assumptions.append("Reₓ dépasse 5×10⁵ : une transition peut survenir selon les perturbations ; le profil laminaire est montré comme comparaison.")
    if re < 1000:
        assumptions.append("Reₓ est petit : la séparation d’échelles exigée par l’approximation de couche limite est faible.")
    plotted = slice(None, None, 6)
    curves = [series(f"x={xx:.3g} m", xi[plotted]*math.sqrt(nu*xx/U)*1e3, U*f[plotted, 1]) for xx in (x/4, x, x*1.5)]
    return dict(metrics=[metric("Reynolds local Reₓ", re), metric("Épaisseur à 99 %", d99*1e3, "mm"),
                          metric("Épaisseur de déplacement δ*", displacement*scale*1e3, "mm"),
                          metric("Épaisseur de quantité de mouvement θ", momentum*scale*1e3, "mm"),
                          metric("Coefficient de frottement local Cf", 2*slope/math.sqrt(re)),
                          metric("Contrainte à la paroi", rho*nu*U*slope/scale, "Pa")],
                charts=[chart("Un profil universel, trois distances", "y (mm)", "u (m·s⁻¹)", *curves),
                        chart("Épaississement en √x", "x (m)", "δ99 (mm)", series("Blasius", xs, d99*np.sqrt(xs/x)*1e3)),
                        chart("Le tir ajuste la pente initiale", "η de similitude", "f′ et f″", series("f′", xi[plotted], f[plotted, 1]), series("f″", xi[plotted], f[plotted, 2]))],
                scene=profile(xi[plotted]*scale, U*f[plotted, 1]),
                steps=["La continuité suggère ψ=√(νU∞x)f(η), η=y√(U∞/(νx)).",
                       "u=U∞f′, v=½√(νU∞/x)(ηf′−f) ; la couche limite conduit à f‴+½ff″=0.",
                       "On impose f(0)=f′(0)=0 et f′(∞)=1. Un tir numérique ajuste f″(0), sans imposer un polynôme arbitraire.",
                       "Cf=2f″(0)/√Reₓ ; δ*=∫(1−u/U∞)dy et θ=∫(u/U∞)(1−u/U∞)dy."],
                assumptions=assumptions)


def darcy_factor(re, relative_roughness):
    """Darcy (non Fanning). Interpolation illustrative de la zone de transition."""
    if re <= 2300:
        return 64/re, "laminaire"
    low, high = .003, .2
    for _ in range(60):
        f = (low+high)/2
        residual = 1/math.sqrt(f)+2*math.log10(relative_roughness/3.7+2.51/(re*math.sqrt(f)))
        if residual > 0:
            low = f
        else:
            high = f
    turbulent = (low+high)/2
    if re < 4000:
        fraction = (re-2300)/1700
        return (1-fraction)*64/re+fraction*turbulent, "transition : interpolation illustrative"
    return turbulent, "turbulent : Colebrook"


def compute_bernoulli(p):
    q, d1, d2 = p["Q"]*1e-3, p["D1"]*.01, p["D2"]*.01
    rho, eta, alpha = p["rho"], p["eta"]*1e-3, float(p["alpha"])
    u1, u2 = 4*q/(math.pi*d1*d1), 4*q/(math.pi*d2*d2)
    re = rho*u2*d2/eta
    friction, regime = darcy_factor(re, p["roughness"]*1e-3/d2)
    regular = friction*p["L"]/d2*u2*u2/(2*G)
    singular = p["K"]*u2*u2/(2*G)
    pump = p["efficiency"]*p["pump"]/(rho*G*q)
    kinetic = alpha*(u2*u2-u1*u1)/(2*G)
    dp = rho*G*(pump-regular-singular-p["dz"]-kinetic)
    positions = np.linspace(0, 1, 101)
    total = pump*positions-regular*positions-singular*(positions >= .5)
    assumptions = ["Bilan stationnaire incompressible entre sections, vitesses moyennes et correction α ; pas d’effet acoustique ni de cavitation.",
                   "La pompe reçoit une puissance électrique : puissance hydraulique=rendement×puissance électrique.",
                   "Le facteur de frottement est celui de Darcy ; Colebrook s’applique à la conduite pleinement développée turbulente.",
                   "Entre Re=2300 et 4000, l’interpolation sert à explorer une incertitude, pas à prédire la transition."]
    if (alpha == 2 and re > 2300) or (alpha == 1 and re <= 2300):
        assumptions.append("Le choix de α ne correspond pas au profil associé au régime estimé : comparez α=2 laminaire et α≈1 quasi uniforme.")
    return dict(metrics=[metric("Vitesse à l’entrée", u1, "m·s⁻¹"), metric("Vitesse dans la conduite", u2, "m·s⁻¹"),
                          metric("Reynolds de conduite", re), metric("Facteur de Darcy λ", friction),
                          metric("Régime de la loi de frottement", regime), metric("Charge fournie par pompe", pump, "m"),
                          metric("Pertes régulières + singulières", regular+singular, "m"),
                          metric("Écart de pression p₂−p₁", dp, "Pa")],
                charts=[chart("Bilan de charge relative", "Progression normalisée entre sections", "Charge (m)",
                              series("Apport de pompe distribué pour lecture", positions, pump*positions),
                              series("Pertes cumulées", positions, regular*positions+singular*(positions >= .5)),
                              series("Charge totale relative", positions, total))],
                steps=["Q=A₁ū₁=A₂ū₂, puis Re=ρū₂D₂/η : continuité et analyse dimensionnelle.",
                       "H=p/(ρg)+z+αū²/(2g). Le bilan est H₂−H₁=Hpompe−hpertes.",
                       "hpertes=(λL/D₂+ΣK)ū₂²/(2g), λ=64/Re en régime laminaire ; en turbulent, on résout Colebrook par dichotomie.",
                       "p₂−p₁=ρg[Hpompe−hpertes−(z₂−z₁)−α(ū₂²−ū₁²)/(2g)]."],
                assumptions=assumptions)


def schiller_drag(U, rad, eta, rho):
    re = rho*2*rad*abs(U)/eta
    return 6*math.pi*eta*rad*abs(U)*(1+.15*re**.687)


def compute_sphere(p):
    rad, U, eta, rho, rho_s = p["R"]*1e-3, p["U"], p["eta"]*1e-3, p["rho"], p["rho_s"]
    re = rho*2*rad*U/eta
    stokes = 6*math.pi*eta*rad*U
    drag = schiller_drag(U, rad, eta, rho) if re <= 1000 else None
    weight = abs(rho_s-rho)*4*math.pi*rad**3*G/3
    terminal_stokes = 2*abs(rho_s-rho)*G*rad**2/(9*eta)
    max_u = 1000*eta/(rho*2*rad)
    if weight == 0:
        terminal, terminal_re = 0., 0.
    elif weight <= schiller_drag(max_u, rad, eta, rho):
        low, high = 0., max_u
        for _ in range(65):
            mid = (low+high)/2
            if schiller_drag(mid, rad, eta, rho) < weight:
                low = mid
            else:
                high = mid
        terminal = (low+high)/2
        terminal_re = rho*2*rad*terminal/eta
    else:
        terminal, terminal_re = None, None
    relaxation = 2*rho_s*rad**2/(9*eta)
    reynolds = np.geomspace(.001, 1000, 201)
    times = np.linspace(0, 5*relaxation, 121)
    assumptions = ["Sphère isolée, fluide newtonien au repos loin de la sphère ; pas d’effet de paroi, de masse ajoutée ni de mémoire hydrodynamique.",
                   "Stokes exige Re≪1. Schiller–Naumann Cd=24/Re(1+0,15Re^0,687) est une corrélation limitée ici à Re≤1000.",
                   "Aucune extrapolation vers la crise de traînée : un réglage hors domaine est signalé, sans valeur de traînée inventée.",
                   "La courbe exponentielle de chute utilise Stokes ; elle est une comparaison formelle si le Reynolds terminal n’est pas petit."]
    return dict(metrics=[metric("Reynolds imposé", re), metric("Traînée Stokes, comparaison", stokes, "N"),
                          metric("Traînée Schiller–Naumann", drag if drag is not None else "Hors domaine Re>1000", "N"),
                          metric("Poids corrigé d’Archimède", weight, "N"),
                          metric("Vitesse terminale corrélée, module", terminal if terminal is not None else "Hors domaine Re>1000", "m·s⁻¹"),
                          metric("Reynolds terminal corrélé", terminal_re if terminal_re is not None else "Hors domaine"),
                          metric("Temps de relaxation Stokes", relaxation, "s")],
                charts=[chart("Corrélation limitée à Re≤1000", "Reynolds", "Cd", series("Stokes", reynolds, 24/reynolds),
                              series("Schiller–Naumann", reynolds, 24/reynolds*(1+.15*reynolds**.687)), x_scale="log", y_scale="log"),
                        chart("Chute exponentielle : modèle Stokes", "t (s)", "Vitesse verticale descendante (m·s⁻¹)",
                              series("Poids−Archimède−Stokes", times, math.copysign(terminal_stokes, rho_s-rho)*(1-np.exp(-times/relaxation))))],
                steps=["Re=ρUD/η avec D=2R ; FStokes=6πηRU se déduit du régime rampant.",
                       "La poussée d’Archimède donne un poids effectif (ρs−ρ)Vg. On résout Ftraînée(v∞)=|poids effectif|.",
                       "Pour Stokes : v∞=2(ρs−ρ)gR²/(9η), τ=m/(6πηR)=2ρsR²/(9η).",
                       "v(t)=v∞(1−exp(−t/τ)) n’est valide qu’avec la loi de Stokes et les effets inertiels transitoires négligés."],
                assumptions=assumptions)


def rankine(r, rad, omega, rho):
    safe = np.maximum(r, rad)
    speed = np.where(r <= rad, omega*r, omega*rad*rad/safe)
    pressure = np.where(r <= rad, rho*omega**2*(r*r/2-rad*rad), -rho*omega**2*rad**4/(2*safe*safe))
    return speed, pressure


def compute_vortex(p):
    rad, w, rho = p["R"], p["omega"], p["rho"]
    r = np.linspace(0, 4*rad, 241)
    speed, pressure = rankine(r, rad, w, rho)
    circulation = TAU*r*speed
    x = y = np.linspace(-3*rad, 3*rad, 49)
    X, Y = np.meshgrid(x, y)
    rr = np.hypot(X, Y)
    vel, pr = rankine(rr, rad, w, rho)
    scale = np.divide(vel, rr, out=np.full_like(rr, w), where=rr != 0)
    return dict(metrics=[metric("Circulation à l’extérieur du cœur", TAU*w*rad**2, "m²·s⁻¹"),
                          metric("Vorticité dans le cœur", 2*w, "s⁻¹"),
                          metric("Vitesse au bord du cœur", w*rad, "m·s⁻¹"),
                          metric("Dépression au centre p∞−p(0)", rho*w*w*rad*rad, "Pa")],
                charts=[chart("Raccordement continu de la vitesse", "r/R", "vθ (m·s⁻¹)", series("Rankine", r/rad, speed)),
                        chart("Euler radial et pression", "r/R", "p−p∞ (Pa)", series("Dépression", r/rad, pressure)),
                        chart("Circulation sur un cercle", "r/R", "Γ(r) (m²·s⁻¹)", series("2πrvθ", r/rad, circulation))],
                field=field("Coupe horizontale du vortex de Rankine", x, y, -scale*Y, scale*X, pr, "p−p∞ (Pa)"),
                steps=["Dans le cœur, vθ=Ωr et rot(v)=2Ωez. À l’extérieur, Γ=2πΩR² est constant et vθ=ΩR²/r.",
                       "Euler radial donne dp/dr=ρvθ²/r : la pression augmente en s’éloignant de l’axe.",
                       "Avec p(∞)=p∞ : p−p∞=−ρΩ²R⁴/(2r²) à l’extérieur.",
                       "La continuité à r=R donne p−p∞=ρΩ²(r²/2−R²) dans le cœur."],
                assumptions=["Modèle de Rankine plan stationnaire, incompressible, sans vitesse verticale ni noyau visqueux évolutif.",
                             "Cette coupe illustre un aspect d’une tornade ; elle ne prédit ni sa naissance, ni sa structure atmosphérique tridimensionnelle.",
                             "p∞ est une référence à l’infini ; le bord de la fenêtre à 3R n’est pas l’infini."])


def compute_magnus(p):
    rad, U, gamma, rho = p["R"], p["U"], p["Gamma"], p["rho"]
    theta = np.linspace(0, TAU, 721)
    vt = -2*U*np.sin(theta)+gamma/(TAU*rad)
    dp = rho*(U*U-vt*vt)/2
    lift = -rho*U*gamma
    integ = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    fx = -rad*integ(dp*np.cos(theta), theta)
    fy = -rad*integ(dp*np.sin(theta), theta)
    x = y = np.linspace(-3*rad, 3*rad, 55)
    X, Y = np.meshgrid(x, y)
    rr = np.hypot(X, Y)
    mask = rr <= rad
    safe = np.maximum(rr, rad)
    co, si = X/safe, Y/safe
    vr = U*(1-rad*rad/safe**2)*co
    vtheta = -U*(1+rad*rad/safe**2)*si+gamma/(TAU*safe)
    vx, vy = vr*co-vtheta*si, vr*si+vtheta*co
    pr = rho*(U*U-vx*vx-vy*vy)/2
    vx[mask] = vy[mask] = pr[mask] = 0.
    return dict(metrics=[metric("Force Fx par longueur, intégrée", fx, "N·m⁻¹"),
                          metric("Force Fy par longueur, intégrée", fy, "N·m⁻¹"),
                          metric("Kutta–Joukowski Fy/L=−ρUΓ", lift, "N·m⁻¹"),
                          metric("Γ/(4πRU), seuil des points d’arrêt", gamma/(4*math.pi*rad*U)),
                          metric("Résidu de portance", fy-lift, "N·m⁻¹")],
                charts=[chart("Pression sur la surface du cylindre", "θ (degrés, antihoraire)", "p−p∞ (Pa)", series("Bernoulli", theta*180/math.pi, dp)),
                        chart("Vitesse tangentielle à la paroi", "θ (degrés)", "vθ (m·s⁻¹)", series("Circulation prescrite", theta*180/math.pi, vt))],
                field=field("Cylindre potentiel avec circulation", x, y, vx, vy, pr, "p−p∞ (Pa)", obstacle={"r": rad, "x": 0, "y": 0}),
                steps=["Superposition : φ=U(r+R²/r)cosθ+Γθ/(2π), localement hors du cylindre.",
                       "À r=R : vr=0 et vθ=−2U sinθ+Γ/(2πR). La circulation positive est antihoraire.",
                       "Bernoulli donne p−p∞=ρ(U²−vθ²)/2 ; on intègre −p n dS sur le cylindre.",
                       "Le terme croisé donne Fy/L=−ρUΓ, tandis que Fx/L=0 dans ce modèle parfait (paradoxe de d’Alembert)."],
                assumptions=["Écoulement potentiel extérieur, stationnaire et incompressible ; pas de couche limite, séparation ni traînée visqueuse.",
                             "Γ est prescrit : la seule vitesse de rotation d’un cylindre réel ne suffit pas à déterminer sa circulation.",
                             "Quand |Γ|>4πRU, les points d’arrêt quittent la surface ; le calcul de pression et de force reste celui du modèle potentiel."])


def dispersion(k, h, sigma, rho):
    kh = k*h
    th = np.tanh(kh)
    omega = np.sqrt((G*k+sigma*k**3/rho)*th)
    sech2 = 1-th*th
    group = ((G+3*sigma*k*k/rho)*th+(G*k+sigma*k**3/rho)*h*sech2)/(2*omega)
    return omega, group


def orbit_axes(k, h, z, amplitude):
    # Expressions exponentielles stables, même lorsque kh > 700.
    denominator = -np.expm1(-2*k*h)
    plus = np.exp(k*z)
    reflected = np.exp(-k*(z+2*h))
    return amplitude*(plus+reflected)/denominator, amplitude*(plus-reflected)/denominator


def compute_houle(p):
    wavelength, h, amp, sigma, rho = (p[k] for k in ("wavelength", "h", "amplitude", "sigma", "rho"))
    k = TAU/wavelength
    omega, group = dispersion(k, h, sigma, rho)
    phase = omega/k
    ks = np.geomspace(k/20, k*20, 241)
    om, cg = dispersion(ks, h, sigma, rho)
    angle = np.linspace(0, TAU, 161)
    orbits = []
    for z in (0, -h/4, -h/2, -h):
        horizontal, vertical = orbit_axes(k, h, z, amp)
        orbits.append(series(f"z/h={z/h:g}", horizontal*np.cos(angle), z+vertical*np.sin(angle)))
    return dict(metrics=[metric("Fréquence f", omega/TAU, "Hz"), metric("Vitesse de phase", phase, "m·s⁻¹"),
                          metric("Vitesse de groupe", group, "m·s⁻¹"), metric("Profondeur relative kh", k*h),
                          metric("Cambrure ka", k*amp), metric("Amplitude relative a/h", amp/h),
                          metric("Énergie moyenne par aire", .5*(rho*G+sigma*k*k)*amp*amp, "J·m⁻²")],
                charts=[chart("Gravité, capillarité et profondeur", "k (m⁻¹)", "Vitesse (m·s⁻¹)", series("Phase ω/k", ks, om/ks), series("Groupe dω/dk", ks, cg), x_scale="log"),
                        chart("Orbites linéaires autour des positions de repos", "Déplacement horizontal (m)", "z (m)", *orbits)],
                scene={"kind": "water", "k": k, "omega": omega, "h": h, "amplitude": amp, "group_velocity": group, "phase_velocity": phase},
                steps=["Incompressibilité et irrotationnalité donnent Δφ=0. Au fond, ∂zφ=0 ; la dépendance verticale est cosh(k(z+h)).",
                       "À la surface, la condition cinématique ∂tζ=∂zφ et la condition dynamique incluant la tension superficielle donnent ω²=(gk+γk³/ρ)tanh(kh).",
                       "cφ=ω/k et cg=dω/dk ; en eau profonde sans capillarité, cg=cφ/2, en eau peu profonde cg≈cφ≈√(gh).",
                       "Les particules ont des orbites elliptiques au premier ordre : amplitude horizontale a cosh(k(z+h))/sinh(kh), verticale a sinh(k(z+h))/sinh(kh)."],
                assumptions=["Théorie linéaire d’Airy, fluide parfait, profondeur constante, sans courant ni dissipation.",
                             "Elle exige ka≪1 et a/h≪1 ; les réglages plus grands servent à repérer la perte de validité, pas à calculer un déferlement.",
                             "Les orbites sont fermées au premier ordre. La dérive de Stokes est un effet d’ordre supérieur, absent de cette animation."])


def acoustic_coefficients(z1, z2):
    rp = (z2-z1)/(z1+z2)
    return {"rp": rp, "tp": 2*z2/(z1+z2), "rv": -rp,
            "tv": 2*z1/(z1+z2), "R": rp*rp, "T": 4*z1*z2/(z1+z2)**2}


def compute_acoustique(p):
    z1, z2 = p["rho1"]*p["c1"], p["rho2"]*p["c2"]
    co = acoustic_coefficients(z1, z2)
    omega, amp = TAU*p["frequency"], p["pressure"]
    k1, k2 = omega/p["c1"], omega/p["c2"]
    x1, x2 = np.linspace(-2*TAU/k1, 0, 201), np.linspace(0, 2*TAU/k2, 201)
    pi, pr, pt = amp*np.cos(k1*x1), amp*co["rp"]*np.cos(k1*x1), amp*co["tp"]*np.cos(k2*x2)
    vi, vr, vt = pi/z1, -pr/z1, pt/z2
    intensity = amp*amp/(2*z1)
    return dict(metrics=[metric("Impédance Z₁", z1, "Pa·s·m⁻¹"), metric("Impédance Z₂", z2, "Pa·s·m⁻¹"),
                          metric("Réflexion de pression rp", co["rp"]), metric("Réflexion de vitesse rv", co["rv"]),
                          metric("Transmission de pression tp", co["tp"]), metric("Transmission de vitesse tv", co["tv"]),
                          metric("Fraction énergétique réfléchie R", co["R"]), metric("Fraction énergétique transmise T", co["T"]),
                          metric("Intensité incidente moyenne", intensity, "W·m⁻²"),
                          metric("Niveau incident, référence 10⁻¹² W/m²", 10*math.log10(intensity/1e-12), "dB")],
                charts=[chart("Instantané à t=0 : pression continue", "x (m), interface à 0", "Surpression (Pa)",
                              series("Incidente", x1, pi), series("Réfléchie", x1, pr), series("Totale milieu 1", x1, pi+pr), series("Transmise milieu 2", x2, pt)),
                        chart("Vitesse normale continue : signe de l’onde réfléchie", "x (m)", "v₁ (m·s⁻¹)",
                              series("Totale milieu 1", x1, vi+vr), series("Transmise milieu 2", x2, vt))],
                scene={"kind": "sound", "k": k1, "k2": k2, "omega": omega, "r_pressure": co["rp"],
                       "t_pressure": co["tp"], "c": p["c1"], "amplitude": amp, "Z1": z1, "Z2": z2},
                steps=["Linéariser Euler et la continuité ; avec χS, c²=1/(ρ₀χS) et Z=ρ₀c.",
                       "Une onde allant vers +x vérifie p₁=Zv₁ ; l’onde réfléchie allant vers −x vérifie p₁=−Zv₁.",
                       "Continuité de p₁ et de la vitesse normale : rp=(Z₂−Z₁)/(Z₁+Z₂), tp=1+rp, rv=−rp et tv=1−rp.",
                       "Iinc=p̂²/(2Z₁), R=rp² et T=(Z₁/Z₂)tp²=1−R ; tp peut dépasser 1 sans créer d’énergie."],
                assumptions=["Incidence normale, interface plane entre deux milieux parfaits homogènes, approximation acoustique linéaire.",
                             "Pas d’absorption, de tension de surface ni de mode transverse ; les amplitudes de pression sont des valeurs crête.",
                             "Le niveau affiché emploie une référence d’intensité : il ne faut pas confondre cette convention avec les références de pression propres à l’air et à l’eau."])


def compute_conduit(p):
    a, b, m, n, freq, c = (p[k] for k in ("width", "height", "m", "n", "frequency", "c"))
    kx, ky, omega = m*math.pi/a, n*math.pi/b, TAU*freq
    kc2 = kx*kx+ky*ky
    fc = c*math.sqrt(kc2)/TAU
    difference = (omega/c)**2-kc2
    propagating = difference > 1e-10
    kz = math.sqrt(difference) if propagating else 0.
    decay = math.sqrt(-difference) if difference < 0 else 0.
    vg = c*c*kz/omega
    vp = omega/kz if propagating else None
    freq_axis = np.linspace(max(fc*1.0001, 1), max(fc*3, freq*1.5, 100), 201)
    kzs = np.sqrt(np.maximum((TAU*freq_axis/c)**2-kc2, 0))
    z = np.linspace(0, max(a*3, c/freq), 161)
    longitudinal = np.cos(kz*z) if propagating else np.exp(-decay*z)
    return dict(metrics=[metric("Fréquence de coupure fc", fc, "Hz"), metric("f/fc", freq/fc if fc else "Mode plan, fc=0"),
                          metric("Régime axial", "Propagatif" if propagating else ("À la coupure" if decay == 0 else "Évanescent")),
                          metric("Nombre d’onde axial réel kz", kz, "m⁻¹"), metric("Constante d’atténuation sous coupure", decay, "m⁻¹"),
                          metric("Vitesse de phase axiale", vp if vp is not None else "Indéfinie sous/à coupure", "m·s⁻¹"),
                          metric("Vitesse de groupe axiale", vg if propagating or decay == 0 else "Pas de propagation", "m·s⁻¹")],
                charts=[chart("Dispersion des modes propagatifs", "f (Hz)", "Vitesse axiale (m·s⁻¹)",
                              series("Groupe", freq_axis, c*c*kzs/(TAU*freq_axis)),
                              series("Phase", freq_axis, TAU*freq_axis/kzs)),
                        chart("Amplitude à t=0, mode normalisé", "z axial (m)", "Pression relative", series("Mode choisi", z, longitudinal))],
                scene={"kind": "duct", "kx": kx, "ky": ky, "kz": kz, "evanescent": not propagating,
                       "width": a, "height": b, "omega": omega, "decay": decay},
                steps=["Parois rigides : vitesse normale nulle, donc ∂np₁=0. Les modes sont cos(mπx/a)cos(nπy/b).",
                       "La séparation donne kz²=(ω/c)²−(mπ/a)²−(nπ/b)² ; fc=(c/2)√[(m/a)²+(n/b)²].",
                       "Au-dessus de fc, vφ=ω/kz≥c et vg=c²kz/ω≤c : vφvg=c².",
                       "Sous la coupure, kz=iκ et l’amplitude décroît comme exp(−κz). Cette décroissance géométrique n’est pas une dissipation visqueuse."],
                assumptions=["Conduit rectangulaire uniforme à parois rigides, fluide parfait, mode unique séparé.",
                             "Un mode évanescent isolé ne transporte pas de flux énergétique moyen axial ; un conduit fini peut coupler ses deux extrémités.",
                             "Le mode (0,0) a fc=0 et vφ=vg=c. Les vitesses de groupe sous la coupure ne décrivent aucun paquet propagatif."])


def compute_diffraction(p):
    wavelength, a = p["c"]/p["frequency"], p["a"]*.01
    angle = np.linspace(-math.pi/2, math.pi/2, 501)
    intensity = np.sinc(a*np.sin(angle)/wavelength)**2
    ratio = wavelength/a
    zero = math.asin(ratio) if ratio <= 1 else None
    return dict(metrics=[metric("Longueur d’onde λ", wavelength*1e3, "mm"), metric("Rapport λ/a", ratio),
                          metric("Premier zéro, angle exact", zero*180/math.pi if zero is not None else "Aucun dans −90° à +90°", "°"),
                          metric("Approximation θ≈λ/a", ratio if ratio < .2 else "Petit angle non justifié", "rad")],
                charts=[chart("Directivité d’une fente uniforme", "θ (degrés)", "Intensité relative I/I(0)", series("sinc²(πa sinθ/λ)", angle*180/math.pi, intensity))],
                steps=["Une fente de largeur a porte une distribution uniforme de sources cohérentes dans le modèle.",
                       "En champ lointain, la différence de marche donne I(θ)/I(0)=[sin(πa sinθ/λ)/(πa sinθ/λ)]².",
                       "Le premier zéro satisfait sinθ=λ/a. Il n’existe dans l’hémisphère propagatif que si λ≤a.",
                       "θ≈λ/a exige λ/a≪1 ; pour les données du TP λ≈13,6 mm>a=10 mm, il faut lire un large lobe sans premier zéro."],
                assumptions=["Diffraction scalaire de Fraunhofer, fente uniformément excitée, observation lointaine ; pas de résonance du diaphragme.",
                             "La loi illustre un laboratoire ultrasonore ; les bords réels et le montage peuvent modifier la directivité."])


def compute_thermo(p):
    T, M, gamma, pressure, freq, diffusivity = p["T"], p["M"]*1e-3, p["gamma"], p["p"]*1e3, p["frequency"], p["diffusivity"]*1e-6
    rho = pressure*M/(R_GAS*T)
    ct, cs = math.sqrt(R_GAS*T/M), math.sqrt(gamma*R_GAS*T/M)
    wavelength, omega = cs/freq, TAU*freq
    thermal = math.sqrt(2*diffusivity/omega)
    diffusion_time = (wavelength/TAU)**2/diffusivity
    temperatures = np.linspace(200, 600, 161)
    frequencies = np.geomspace(1, 100000, 201)
    return dict(metrics=[metric("Masse volumique idéale", rho, "kg·m⁻³"), metric("Compressibilité isotherme χT", 1/pressure, "Pa⁻¹"),
                          metric("Compressibilité isentropique χS", 1/(gamma*pressure), "Pa⁻¹"),
                          metric("Célérité isotherme cT", ct, "m·s⁻¹"), metric("Célérité isentropique cS", cs, "m·s⁻¹"),
                          metric("Longueur thermique √(2Dth/ω)", thermal*1e3, "mm"),
                          metric("Rapport δth/(λ/2π)", thermal/(wavelength/TAU)),
                          metric("ω×temps diffusif sur λ/2π", omega*diffusion_time)],
                charts=[chart("L’équation d’état fixe les deux limites", "T (K)", "Célérité (m·s⁻¹)",
                              series("Isotherme", temperatures, np.sqrt(R_GAS*temperatures/M)),
                              series("Isentropique", temperatures, np.sqrt(gamma*R_GAS*temperatures/M))),
                        chart("Comparer longueur thermique et longueur de variation", "f (Hz)", "Longueur (m)",
                              series("δth", frequencies, np.sqrt(diffusivity/(math.pi*frequencies))),
                              series("λ/(2π)", frequencies, cs/(TAU*frequencies)), x_scale="log", y_scale="log")],
                steps=["Gaz parfait : p=ρRT/M. À T fixé, χT=1/p ; sur une isentrope pρ^−γ=constante, χS=1/(γp).",
                       "c²=(∂p/∂ρ) dans l’évolution considérée : cT²=RT/M et cS²=γRT/M.",
                       "Une oscillation thermique diffuse sur δth=√(2Dth/ω). Comparer ce rayon à la longueur de variation 1/k=λ/(2π).",
                       "Si la chaleur diffuse peu durant une oscillation dans le volume, l’hypothèse isentropique est pertinente ; près d’une paroi, les couches thermiques doivent être étudiées séparément."],
                assumptions=["Gaz parfait, γ constant et évolution linéarisée. Les deux courbes sont des limites thermodynamiques.",
                             "Ce laboratoire ne fabrique pas une célérité intermédiaire à partir d’un temps de relaxation arbitraire.",
                             "Dans un conduit étroit, échanges aux parois et pertes thermo-visqueuses demandent un modèle géométrique supplémentaire."])


def hartmann_profile(y, h, gp, eta, sigma, B):
    ha = abs(B)*h*math.sqrt(sigma/eta)
    if ha < 1e-3:
        # Expansion d'ordre B², évitant la soustraction de cosh presque égaux.
        q = y/h
        u = gp*h*h/(2*eta)*(1-q*q)*(1-ha*ha*(5-q*q)/12)
        du = -gp*y/eta + gp*h/eta*ha*ha*(3*q-q**3)/6
        return u, du, ha
    q = y/h
    ratio = (np.exp(ha*(q-1))+np.exp(-ha*(q+1)))/(1+math.exp(-2*ha))
    sinh_ratio = (np.exp(ha*(q-1))-np.exp(-ha*(q+1)))/(1+math.exp(-2*ha))
    scale = gp/(sigma*B*B)
    return scale*(1-ratio), -scale*ha/h*sinh_ratio, ha


def compute_mhd(p):
    B, sigma, eta, rho, h, gp = p["B"], p["sigma"], p["eta"]*1e-3, p["rho"], p["h"]*1e-3, p["G"]
    if p["mode"] == "alfven":
        k, amp = TAU/p["wavelength"], p["amplitude"]
        speed = B/math.sqrt(MU0*rho)
        omega = k*speed
        x = np.linspace(0, 2*p["wavelength"], 201)
        velocity_amp = omega*amp
        magnetic_amp = math.sqrt(MU0*rho)*velocity_amp
        return dict(metrics=[metric("Vitesse d’Alfvén vA", speed, "m·s⁻¹"), metric("Fréquence", omega/TAU, "Hz"),
                              metric("Amplitude de vitesse transverse", velocity_amp, "m·s⁻¹"),
                              metric("Amplitude de perturbation magnétique", magnetic_amp, "T"),
                              metric("Rapport b̂/B₀", k*amp if B else "Champ nul : pas d’onde Alfvén"),
                              metric("Énergie cinétique moyenne", rho*velocity_amp**2/4, "J·m⁻³"),
                              metric("Énergie magnétique moyenne", magnetic_amp**2/(4*MU0), "J·m⁻³")],
                    charts=[chart("Onde transverse : tension des lignes de champ", "x parallèle à B₀ (m)", "Déplacement transverse (m)", series("À t=0", x, amp*np.cos(k*x)))],
                    scene={"kind": "alfven", "k": k, "omega": omega, "amplitude": amp},
                    steps=["En MHD idéale, l’induction et la force de Lorentz couplent vitesse transverse et perturbation magnétique.",
                           "Pour une onde parallèle à B₀ : ∂²tξ=vA²∂²xξ, vA=B₀/√(μ₀ρ).",
                           "Une onde progressive vérifie |b̂|=√(μ₀ρ)|v̂|, donc égalité des énergies cinétique et magnétique moyennes.",
                           "La fréquence est ω=kvA. Le champ nul annule la force de rappel : l’animation reste alors immobile."],
                    assumptions=["MHD idéale linéaire, densité uniforme, champ de fond uniforme, sans résistivité ni viscosité.",
                                 "ka≪1 ; la conductivité et la viscosité des contrôles Hartmann ne sont pas employées dans ce modèle idéal.",
                                 "Ce modèle d’onde et le canal quasi statique de Hartmann sont deux limites distinctes."])
    # Nœuds rapprochés des parois : les couches de Hartmann restent visibles.
    y = h*np.sin(np.linspace(-math.pi/2, math.pi/2, 301))
    u, du, ha = hartmann_profile(y, h, gp, eta, sigma, B)
    if ha == 0:
        mean = gp*h*h/(3*eta)
    elif ha < 1e-3:
        mean = gp*h*h/(3*eta)*(1-2*ha*ha/5)
    else:
        mean = gp/(sigma*B*B)*(1-math.tanh(ha)/ha)
    q = 2*h*mean
    if ha < .1:
        nodes, weights = np.polynomial.legendre.leggauss(64)
        qv, qd, _ = hartmann_profile(nodes*h, h, gp, eta, sigma, B)
        visc = h*np.dot(weights, eta*qd*qd)
        joule = h*np.dot(weights, sigma*B*B*qv*qv)
    else:
        # Intégrales fermées : pas de quadrature sous-résolue lorsque Ha est grand.
        tail = math.exp(-2*ha)
        sech2 = 4*tail/(1+tail)**2
        common = gp*gp*h/(sigma*B*B)
        visc = common*(math.tanh(ha)/ha-sech2)
        joule = common*(2-3*math.tanh(ha)/ha+sech2)
    rm = MU0*sigma*abs(mean)*h
    delta = h/ha if ha > 0 else None
    return dict(metrics=[metric("Nombre de Hartmann Ha", ha), metric("Vitesse moyenne", mean, "m·s⁻¹"),
                          metric("Reynolds magnétique Rm", rm), metric("Épaisseur h/Ha", delta*1e3 if delta else "Champ nul", "mm"),
                          metric("Puissance de pression par aire", gp*q, "W·m⁻²"),
                          metric("Dissipation visqueuse intégrée", visc, "W·m⁻²"),
                          metric("Dissipation Joule intégrée", joule, "W·m⁻²"),
                          metric("Résidu du bilan intégré", gp*q-visc-joule, "W·m⁻²")],
                charts=[chart("Le champ aplatit et freine le profil", "y (mm)", "u (m·s⁻¹)",
                              series("Hartmann à G fixé", y*1e3, u), series("Sans champ", y*1e3, gp*(h*h-y*y)/(2*eta))),
                        chart("Deux canaux de dissipation", "y (mm)", "Dissipation volumique (W·m⁻³)",
                              series("Visqueuse η(u′)²", y*1e3, eta*du*du), series("Joule σB²u²", y*1e3, sigma*B*B*u*u))],
                scene=profile(y, u),
                steps=["Axes : u suivant +x, B₀ suivant +y. Le circuit transverse court-circuité impose Ez=0, donc jz=σuB₀.",
                       "j×B=−σB₀²u ex ; le bilan devient ηu″−σB₀²u=−G, u(±h)=0.",
                       "Ha=B₀h√(σ/η) et u=G/(σB₀²)[1−cosh(Ha y/h)/cosh(Ha)]. À B₀→0, on retrouve G(h²−y²)/(2η).",
                       "Multiplier par u et intégrer : GQ=∫η(u′)²dy+∫j²/σ dy, les parois étant au repos."],
                assumptions=["Canal plan infini, stationnaire, incompressible, adhérence ; approximation quasi statique supposant Rm≪1.",
                             "Circuit transverse court-circuité (Ez=0), courant pouvant se fermer ; des parois isolantes et un circuit ouvert imposeraient une autre condition électrique.",
                             "Si Rm n’est pas petit, le champ induit ne peut plus être négligé : le profil affiché devient une comparaison hors hypothèse.",
                             "Les puissances sont intégrées sur y, par aire axiale et largeur transverse ; leurs intégrales fermées évitent de sous-résoudre les couches fines."])


def taylor_green(x, y, time, U, k, nu, rho):
    A = U*np.exp(-2*nu*k*k*time)
    u, v = A*np.sin(k*x)*np.cos(k*y), -A*np.cos(k*x)*np.sin(k*y)
    pressure = rho*A*A/4*(np.cos(2*k*x)+np.cos(2*k*y))
    vorticity = 2*A*k*np.sin(k*x)*np.sin(k*y)
    return u, v, pressure, vorticity


def compute_navier(p):
    U, L, nu, t, rho = (p[k] for k in ("U", "L", "nu", "time", "rho"))
    k = TAU/L
    A = U*math.exp(-2*nu*k*k*t)
    x = y = np.linspace(0, L, 49)
    X, Y = np.meshgrid(x, y)
    u, v, pressure, vort = taylor_green(X, Y, t, U, k, nu, rho)
    ts = np.linspace(0, max(10, t*1.5), 201)
    energies = rho*U*U/4*np.exp(-4*nu*k*k*ts)
    dissipation = 4*nu*k*k*energies
    return dict(metrics=[metric("Amplitude de vitesse à t", A, "m·s⁻¹"), metric("Énergie cinétique moyenne", rho*A*A/4, "J·m⁻³"),
                          metric("Dissipation moyenne", rho*nu*k*k*A*A, "W·m⁻³"), metric("Vorticité maximale en module", 2*A*k, "s⁻¹"),
                          metric("Divergence analytique", 0, "s⁻¹"),
                          metric("Reynolds U₀/(νk)", U/(nu*k) if nu else "Euler, ν=0"),
                          metric("Résidu analytique dE/dt+dissipation", 0, "W·m⁻³")],
                charts=[chart("La viscosité enlève de l’énergie", "t (s)", "Énergie moyenne (J·m⁻³)", series("Taylor–Green exact", ts, energies)),
                        chart("Le taux de décroissance égale la dissipation", "t (s)", "Puissance volumique (W·m⁻³)",
                              series("−dE/dt", ts, dissipation), series("ρν〈|∇v|²〉", ts, dissipation))],
                field=field("Vorticité de Taylor–Green, instantané", x, y, u, v, vort, "ωz (s⁻¹)"),
                steps=["Sur le tore carré : vx=A sin(kx)cos(ky), vy=−A cos(kx)sin(ky), k=2π/L. La divergence s’annule exactement.",
                       "(v·∇)v=(A²k/2)(sin(2kx),sin(2ky)) est équilibré par −∇p/ρ, avec p−p₀=ρA²[cos(2kx)+cos(2ky)]/4.",
                       "Comme Δv=−2k²v, ∂tv=νΔv donne A=U₀ exp(−2νk²t). À ν=0, c’est une solution d’Euler.",
                       "L’énergie moyenne est E=ρA²/4 et −dE/dt=ρνk²A²=ρν〈|∇v|²〉."],
                assumptions=["Solution exacte bidimensionnelle, périodique, incompressible, sans forçage ; aucune intégration numérique instable n’est mise en scène.",
                             "Les particules dessinées sur le champ instantané illustrent la direction locale ; les lignes de courant ne sont pas des trajectoires générales instationnaires.",
                             "Le bilan 2D et cet exemple particulier ne démontrent aucun résultat général de régularité 3D et ne résolvent pas le problème du millénaire."])


def compute_hydrostatique(p):
    height, rho, p0, T = p["height"], p["rho"], p["p0"]*1e3, p["T"]
    z = np.linspace(0, max(height, 1), 201)
    if p["mode"] == "gas":
        scale = 287.05*T/G
        pressure = p0*np.exp(-z/scale)
        at = p0*math.exp(-height/scale)
        density = pressure/(287.05*T)
        return dict(metrics=[metric("Pression à l’altitude choisie", at, "Pa"), metric("Masse volumique locale", at/(287.05*T), "kg·m⁻³"),
                              metric("Hauteur d’échelle RT/(Mg)", scale, "m"), metric("Rapport p/p₀", at/p0)],
                    charts=[chart("Atmosphère idéale isotherme", "Altitude z (m)", "Pression (kPa)", series("p₀ exp(−z/H)", z, pressure/1e3)),
                            chart("La densité diminue aussi", "Altitude z (m)", "ρ (kg·m⁻³)", series("Gaz parfait", z, density))],
                    steps=["Au repos, Euler devient dp/dz=−ρg, avec z dirigé vers le haut.",
                           "Pour un gaz parfait isotherme, ρ=p/(RspecT) et dp/p=−g dz/(RspecT).",
                           "p(z)=p₀exp(−z/H), H=RspecT/g et Rspec=287,05 J·kg⁻¹·K⁻¹ pour l’air.",
                           "La baisse de pression est exponentielle parce que la densité varie, pas parce que la pesanteur varierait ici."],
                    assumptions=["Atmosphère idéale isotherme d’air sec, g constant ; comparaison pédagogique, pas modèle météorologique réel.",
                                 "Le contrôle ρ liquide ne s’applique pas à l’atmosphère ; sa densité se déduit de l’équation d’état."])
    pressure = p0+rho*G*z
    return dict(metrics=[metric("Pression à la profondeur choisie", p0+rho*G*height, "Pa"),
                          metric("Surpression hydrostatique", rho*G*height, "Pa"), metric("Gradient en profondeur", rho*G, "Pa·m⁻¹")],
                charts=[chart("Liquide incompressible au repos", "Profondeur d=−z (m)", "Pression (kPa)", series("p₀+ρgd", z, pressure/1e3))],
                steps=["Au repos, ∇p=ρg ; en prenant z vers le haut, dp/dz=−ρg.",
                       "Dans un liquide de densité constante, p+ρgz est constant.",
                       "À la profondeur d=−z sous la surface, p=p₀+ρgd ; il faut distinguer pression absolue et surpression.",
                       "Le même bilan appliqué sur la surface d’un corps immergé conduit à la poussée d’Archimède."],
                assumptions=["Liquide incompressible homogène au repos, g constant ; pas de capillarité ni de variation de densité thermique.",
                             "La température est utilisée seulement dans le mode atmosphère idéale."])
