"""Solutions analytiques P1 : la précision du tracé ne remplace pas les lois physiques."""
import math
import numpy as np
from commun import metric, series, chart, result

TAU = 2 * math.pi


def ellipse(a, e, mu, samples=601):
    """Positions et vitesses à temps uniforme ; mu=G(m1+m2), jamais masse réduite."""
    period = TAU * math.sqrt(a ** 3 / mu)
    t = np.linspace(0, period, samples)
    mean_anomaly = TAU * t / period
    eccentric_anomaly = mean_anomaly.copy()
    for _ in range(18):
        eccentric_anomaly -= ((eccentric_anomaly - e * np.sin(eccentric_anomaly) - mean_anomaly)
                              / (1 - e * np.cos(eccentric_anomaly)))
    x = a * (np.cos(eccentric_anomaly) - e)
    y = a * math.sqrt(1 - e * e) * np.sin(eccentric_anomaly)
    r = a * (1 - e * np.cos(eccentric_anomaly))
    edot = math.sqrt(mu / a ** 3) / (1 - e * np.cos(eccentric_anomaly))
    vx = -a * np.sin(eccentric_anomaly) * edot
    vy = a * math.sqrt(1 - e * e) * np.cos(eccentric_anomaly) * edot
    return t, x, y, vx, vy, r, eccentric_anomaly


def orbit_scene(title, paths, bodies, length, description, times=None):
    scene = dict(kind='orbits', title=title, paths=paths, bodies=bodies,
                 bounds=[-length, length, -length, length], description=description)
    if times is not None:
        scene['times'] = times
    return scene


def path(label, x, y, color=0):
    return dict(label=label, x=x, y=y, colorIndex=color)


def body(label, x, y, color=0, radius=5):
    return dict(label=label, x=x, y=y, colorIndex=color, radius=radius)


def orbite_kepler(p):
    a, e, mass = p['a'], p['e'], p['mass']
    mu = TAU ** 2 * mass
    t, x, y, vx, vy, r, eccentric_anomaly = ellipse(a, e, mu)
    speed2 = vx * vx + vy * vy
    h = x * vy - y * vx
    energy = speed2 / 2 - mu / r
    swept = a * a * math.sqrt(1 - e * e) / 2 * (eccentric_anomaly - e * np.sin(eccentric_anomaly))
    expected_h = math.sqrt(mu * a * (1 - e * e))
    expected_energy = -mu / (2 * a)
    intervals = np.linspace(0, len(t) - 1, 13, dtype=int)
    areas = np.diff(swept[intervals])
    area_times = (t[intervals[:-1]] + t[intervals[1:]]) / 2
    return result(
        [metric('Période orbitale T', t[-1], 'an'), metric('Péricentre a(1−e)', a * (1 - e), 'UA'),
         metric('Apocentre a(1+e)', a * (1 + e), 'UA'), metric('Énergie par unité de masse ε', expected_energy, 'UA²/an²'),
         metric('Moment cinétique par unité de masse h', expected_h, 'UA²/an'),
         metric('Écart relatif maximal du bilan d’énergie', np.max(np.abs(energy - expected_energy)) / abs(expected_energy)),
         metric('Écart relatif maximal du moment cinétique', np.max(np.abs(h - expected_h)) / expected_h),
         metric('Rapport vitesse au péricentre / à l’apocentre', (1 + e) / (1 - e))],
        [chart('Distance à l’étoile et vitesse au cours d’une période', 'Temps (an)', 'Valeur',
               series('Distance r (UA)', t, r), series('Vitesse (UA/an)', t, np.sqrt(speed2))),
         chart('Bilan mécanique : une énergie négative constante', 'Temps (an)', 'Énergie spécifique (UA²/an²)',
               series('Énergie cinétique', t, speed2 / 2), series('Énergie potentielle', t, -mu / r), series('Somme', t, energy)),
         chart('Douze durées égales : douze aires égales', 'Milieu de chaque intervalle (an)', 'Aire balayée (UA²)',
               series('Aire pendant T/12', area_times, areas)),
         chart('Loi des aires : A(t) est affine', 'Temps (an)', 'Aire balayée (UA²)', series('A(t)', t, swept))],
        orbit_scene('Une ellipse dont l’étoile occupe un foyer', [path('Orbite', x, y)],
                    [body('Étoile', np.zeros_like(t), np.zeros_like(t), 1, 8), body('Planète', x, y, 0, 5)],
                    a * (1 + e) * 1.12, 'Les points animés sont calculés à temps uniforme ; le centre géométrique de l’ellipse est différent du foyer.', t),
        ['La force gravitationnelle est centrale : son moment par rapport à l’étoile est nul. Donc h=r²θ̇ est constant et le mouvement reste plan.',
         'L’équation de Binet u″+u=μg/h², avec u=1/r et μg=GM, donne r=p/(1+e cosθ), p=h²/μg.',
         'L’énergie spécifique vaut ε=v²/2−μg/r=−μg/(2a). On en déduit la relation de vis-viva : v²=μg(2/r−1/a).',
         'Une aire élémentaire vaut dA=r²dθ/2=h dt/2. L’aire totale πa²√(1−e²) donne T²=4π²a³/μg.'],
        ['Planète de masse négligeable devant l’étoile ; astre ponctuel ou sphérique, sans atmosphère ni autre perturbation.',
         'Le modèle utilise UA, année et masse solaire avec G=4π² : la période d’une orbite de 1 UA autour d’une masse solaire vaut 1 an dans cette convention.',
         'Les bilans sont évalués sur la solution analytique ; les écarts affichés proviennent de l’arrondi numérique, pas d’une intégration du mouvement.'])


def deux_corps(p):
    a, e, q, total = p['a'], p['e'], p['q'], p['total_mass']
    m1, m2 = total / (1 + q), total * q / (1 + q)
    reduced = m1 * m2 / total
    t, x, y, vx, vy, r, _ = ellipse(a, e, TAU ** 2 * total)
    x1, y1, x2, y2 = -m2 / total * x, -m2 / total * y, m1 / total * x, m1 / total * y
    speed2 = vx * vx + vy * vy
    k1, k2 = .5 * m1 * (m2 / total) ** 2 * speed2, .5 * m2 * (m1 / total) ** 2 * speed2
    potential = -TAU ** 2 * m1 * m2 / r
    total_energy = k1 + k2 + potential
    bary_error = np.max(np.hypot(m1 * x1 + m2 * x2, m1 * y1 + m2 * y2))
    return result(
        [metric('Masse de la première étoile m₁', m1, 'masses solaires'), metric('Masse de la deuxième étoile m₂', m2, 'masses solaires'),
         metric('Masse réduite μr', reduced, 'masses solaires'), metric('Période commune', t[-1], 'an'),
         metric('Demi-grand axe a₁ autour de G', a * m2 / total, 'UA'), metric('Demi-grand axe a₂ autour de G', a * m1 / total, 'UA'),
         metric('Erreur maximale sur m₁r₁+m₂r₂=0', bary_error, 'masse solaire·UA'),
         metric('Énergie totale dans le référentiel de G', -TAU ** 2 * m1 * m2 / (2 * a), 'masse solaire·UA²/an²')],
        [chart('Les deux distances au centre de masse', 'Temps (an)', 'Distance à G (UA)', series('Étoile 1', t, m2 / total * r), series('Étoile 2', t, m1 / total * r)),
         chart('Décomposer l’énergie cinétique', 'Temps (an)', 'Énergie (masse solaire·UA²/an²)',
               series('Ec₁', t, k1), series('Ec₂', t, k2), series('½μr vrelative²', t, .5 * reduced * speed2)),
         chart('Une énergie totale constante pour le système fermé', 'Temps (an)', 'Énergie (masse solaire·UA²/an²)',
               series('Ec₁+Ec₂', t, k1 + k2), series('Potentielle mutuelle', t, potential), series('Énergie totale', t, total_energy))],
        orbit_scene('Les deux étoiles autour du centre de masse', [path('Étoile 1', x1, y1, 0), path('Étoile 2', x2, y2, 1)],
                    [body('Étoile 1', x1, y1, 0, 7), body('Étoile 2', x2, y2, 1, 6), body('G', t * 0, t * 0, 2, 3)],
                    a * (1 + e) / (1 + q) * 1.12, 'G est fixe dans le référentiel du centre de masse ; la séparation r₂−r₁ décrit l’ellipse relative.', t),
        ['Choisir le système fermé formé des deux étoiles. Les forces internes sont opposées : la quantité de mouvement totale est constante.',
         'Poser r=r₂−r₁, M=m₁+m₂ et μr=m₁m₂/M. Les positions relatives à G sont r₁=−(m₂/M)r et r₂=(m₁/M)r.',
         'La soustraction des équations de Newton donne r̈=−GM r/r³. Le paramètre gravitationnel dépend de la masse totale, pas de la masse réduite.',
         'Dans le référentiel de G, Ec=½μr ṙ² et E=−Gm₁m₂/(2a). Dans un référentiel où G se déplace, ajouter ½M VG² à Ec.'],
        ['Deux masses ponctuelles isolées ; les forces de marée, collisions et effets relativistes sont négligés.',
         'Les unités astronomiques sont les mêmes que dans le laboratoire Kepler ; a est le demi-grand axe de la séparation, non celui d’une seule étoile.'])


def potentiel_effectif(p):
    eta = p['eta']
    h, energy, ecc = eta, (eta * eta - 2) / 2, abs(eta * eta - 1)
    semilatus = h * h
    if ecc < 1:
        start = 0 if eta >= 1 else math.pi
        theta = np.linspace(start, start + TAU, 601)
        orbit_type = 'Cercle' if abs(ecc) < 1e-10 else 'Ellipse'
    else:
        limit = math.acos(-1 / ecc) if ecc > 1 else math.pi
        theta = np.linspace(0, limit * .975, 601)
        orbit_type = 'Parabole' if abs(ecc - 1) < 1e-10 else 'Hyperbole'
    r = semilatus / (1 + ecc * np.cos(theta))
    orientation = math.pi if eta < 1 else 0
    x, y = r * np.cos(theta - orientation), r * np.sin(theta - orientation)
    time = np.zeros_like(theta)
    time[1:] = np.cumsum(np.diff(theta) * (r[:-1] ** 2 + r[1:] ** 2) / (2 * h))
    grid = np.linspace(max(.05, semilatus / 8), max(4, min(12, float(np.max(r)) * 1.2)), 700)
    potential = h * h / (2 * grid * grid) - 1 / grid
    radial_velocity2 = 2 * (energy - (h * h / (2 * r * r) - 1 / r))
    peri = semilatus / (1 + ecc)
    apo = semilatus / (1 - ecc) if ecc < 1 else None
    circular_radius = h * h
    turn_description = f'rmin={peri:.4g} ; rmax={apo:.4g}' if apo is not None else f'rmin={peri:.4g} ; pas de borne supérieure'
    return result(
        [metric('Type de trajectoire', orbit_type), metric('Énergie spécifique ε', energy), metric('Excentricité e', ecc),
         metric('Points de rebroussement', turn_description), metric('Rayon du minimum de Ueff', circular_radius),
         metric('Énergie au minimum de Ueff', -1 / (2 * h * h)), metric('Vitesse d’échappement à r₀=1', math.sqrt(2))],
        [chart('Lire le domaine accessible : ε ≥ Ueff(r)', 'Distance r/r₀', 'Énergie spécifique réduite',
               series('Ueff', grid, potential), series('Énergie ε du lancement', grid, np.full_like(grid, energy)), yMin=-1.2 / (2 * h * h) - .1, yMax=max(1, energy + .3)),
         chart('Énergie radiale : ṙ²/2 = ε−Ueff(r)', 'Angle parcouru depuis le lancement (rad)', 'Énergie spécifique réduite',
               series('ṙ²/2', theta - theta[0], np.maximum(0, radial_velocity2 / 2)), series('Ueff le long de la trajectoire', theta - theta[0], energy - radial_velocity2 / 2))],
        orbit_scene('De la vitesse circulaire à l’échappement', [path('Trajectoire', x, y)],
                    [body('Astre', time * 0, time * 0, 1, 8), body('Objet lancé', x, y, 0, 5)],
                    min(12, max(1.2, float(np.max(r)) * 1.05)),
                    'Lancement tangent à r₀=1. Sur les trajectoires non bornées, seule une portion finie est tracée. L’animation utilise la grille angulaire, à temps non uniforme.', time),
        ['Les unités GM=r₀=1 donnent vcirc=1 et véchappement=√2. Le lancement tangent donne h=η et ε=(η²−2)/2.',
         'La conservation du moment cinétique donne θ̇=h/r². L’énergie se réécrit ε=ṙ²/2+Ueff(r), avec Ueff=h²/(2r²)−1/r.',
         'Un rayon est accessible si Ueff(r)≤ε. Les racines Ueff(r)=ε sont les rayons où ṙ=0 : les points de rebroussement radial.',
         'Le minimum est en rc=h², avec Ueff″(rc)=1/h⁶>0. On retrouve une orbite circulaire stable ; e=|η²−1| classe les coniques.'],
        ['Force gravitationnelle centrale newtonienne, masse du projectile négligeable, astre sans surface matérielle modélisée.',
         'Le tracé non borné est volontairement limité ; ce bord d’image ne représente pas une limite physique.',
         'Le potentiel effectif est une énergie par unité de masse. Son terme centrifuge résulte de l’élimination de θ̇, pas d’une nouvelle force physique dans le référentiel galiléen.'])


def transfert_hohmann(p):
    central = p['central']
    scale, mu = (7000.0, 3.986e5) if central == 'earth' else (149597870.7, 1.3271244e11)
    r1, r2 = p['r1'] * scale, p['r2'] * scale
    a = (r1 + r2) / 2
    circular1, circular2 = math.sqrt(mu / r1), math.sqrt(mu / r2)
    transfer1 = math.sqrt(mu * (2 / r1 - 1 / a))
    transfer2 = math.sqrt(mu * (2 / r2 - 1 / a))
    dv1, dv2 = transfer1 - circular1, circular2 - transfer2
    transfer_time = math.pi * math.sqrt(a ** 3 / mu)
    theta = np.linspace(0, TAU, 601)
    c1x, c1y = r1 / scale * np.cos(theta), r1 / scale * np.sin(theta)
    c2x, c2y = r2 / scale * np.cos(theta), r2 / scale * np.sin(theta)
    e = abs(r2 - r1) / (r1 + r2)
    t, x, y, vx, vy, r, _ = ellipse(a, e, mu)
    if r2 >= r1:
        idx = slice(0, 301)
    else:
        idx = slice(300, 601)
    x, y, r, vx, vy = x[idx] / scale, y[idx] / scale, r[idx], vx[idx], vy[idx]
    if r2 < r1:
        x, y = -x, -y
    transfer_t = t[idx] - t[idx][0]
    ratio_grid = np.linspace(.95, 20, 251)
    target = ratio_grid * scale
    semimajor = (r1 + target) / 2
    cost = np.abs(np.sqrt(mu * (2 / r1 - 1 / semimajor)) - circular1) + np.abs(np.sqrt(mu / target) - np.sqrt(mu * (2 / target - 1 / semimajor)))
    return result(
        [metric('Première impulsion Δv₁ (signée)', dv1, 'km/s'), metric('Seconde impulsion Δv₂ (signée)', dv2, 'km/s'),
         metric('Coût total |Δv₁|+|Δv₂|', abs(dv1) + abs(dv2), 'km/s'), metric('Durée du transfert', transfer_time / 3600, 'h'),
         metric('Demi-grand axe de transfert a/L₀', a / scale), metric('Excentricité de transfert', e),
         metric('Vitesse circulaire de départ', circular1, 'km/s'), metric('Vitesse circulaire d’arrivée', circular2, 'km/s')],
        [chart('L’énergie sur l’ellipse fixe la vitesse', 'Temps depuis le départ (h)', 'Vitesse (km/s)', series('Vitesse de transfert', transfer_t / 3600, np.hypot(vx, vy))),
         chart('Coût de Hohmann selon l’orbite visée', 'Rayon cible r₂/L₀', 'Δv total (km/s)', series('Deux impulsions', ratio_grid, cost))],
        orbit_scene('Deux cercles tangents à l’ellipse de transfert', [path('Orbite de départ', c1x, c1y, 1), path('Orbite d’arrivée', c2x, c2y, 2), path('Demi-ellipse de transfert', x, y, 0)],
                    [body('Astre', transfer_t * 0, transfer_t * 0, 3, 8), body('Véhicule', x, y, 0, 5)],
                    max(r1, r2) / scale * 1.12, 'L’impulsion initiale a lieu sur l’axe positif ; l’impulsion finale sur l’axe négatif. La position de la planète d’arrivée n’est pas simulée.', transfer_t),
        ['L’ellipse de transfert est tangente aux deux orbites circulaires : ses extrémités ont rayons r₁ et r₂, donc a=(r₁+r₂)/2.',
         'Sur cette ellipse, la relation énergétique v²=GM(2/r−1/a) donne les vitesses vt₁ et vt₂.',
         'Comparer aux vitesses circulaires √(GM/r₁) et √(GM/r₂). Les différences signées indiquent accélération ou freinage ; le carburant dépend de la somme de leurs valeurs absolues.',
         'Le trajet représente une demi-période elliptique : τ=π√(a³/GM). Un transfert interplanétaire exige aussi de choisir la phase de la planète à l’arrivée.'],
        ['Orbites initiale et finale circulaires, coplanaires et de même sens ; impulsions instantanées ; gravitation d’un seul astre.',
         'Paramètres arrondis : GMterre=3,986×10⁵ km³/s², GMsoleil=1,3271244×10¹¹ km³/s². L’unité astronomique vaut 149 597 870,7 km.',
         'Ce modèle compare une famille de transferts à deux impulsions ; il ne démontre pas une optimalité parmi toutes les missions ou tous les transferts possibles.',
         'Sources de contexte : NASA, « Hohmann Transfer Orbit » ; NASA GSFC, « Flight to Mars: Calculations ».'])


def diffusion_gravitationnelle(p):
    vinf, b, pv = p['vinf'], p['b'], p['planet_v']
    h = b * vinf
    e = math.sqrt(1 + b * b * vinf ** 4)
    limit = math.acos(-1 / e)
    theta = np.linspace(-limit * .98, limit * .98, 601)
    r = h * h / (1 + e * np.cos(theta))
    x, y = r * np.cos(theta), r * np.sin(theta)
    vx, vy = -np.sin(theta) / h, (e + np.cos(theta)) / h
    delta = 2 * math.asin(1 / e)
    incoming = np.array([math.sin(limit), e + math.cos(limit)]) / h
    outgoing = np.array([-math.sin(limit), e + math.cos(limit)]) / h
    planet_velocity = np.array([-pv if p['encounter'] == 'gain' else pv, 0.0])
    initial_speed = float(np.linalg.norm(incoming + planet_velocity))
    final_speed = float(np.linalg.norm(outgoing + planet_velocity))
    kinetic_ref = .5 * ((vx + planet_velocity[0]) ** 2 + vy ** 2)
    kinetic_body = .5 * (vx ** 2 + vy ** 2)
    impact_grid = np.linspace(.15, 6, 250)
    angles = 2 * np.arctan(1 / (impact_grid * vinf * vinf)) * 180 / math.pi
    return result(
        [metric('Excentricité hyperbolique e', e), metric('Angle de déviation δ', delta * 180 / math.pi, '°'),
         metric('Distance minimale au centre rp', h * h / (1 + e)), metric('Vitesse à l’entrée lointaine, second référentiel', initial_speed),
         metric('Vitesse à la sortie lointaine, second référentiel', final_speed),
         metric('Gain d’énergie cinétique spécifique à l’infini', .5 * (final_speed ** 2 - initial_speed ** 2)),
         metric('Énergie spécifique dans le référentiel de l’astre', .5 * vinf ** 2),
         metric('Erreur maximale sur ε=v²/2−1/r', np.max(np.abs(kinetic_body - 1 / r - vinf ** 2 / 2)))],
        [chart('Une déviation plus forte pour un survol plus proche', 'Paramètre d’impact b', 'Angle de déviation (°)', series('δ(b)', impact_grid, angles)),
         chart('L’énergie cinétique dépend du référentiel', 'Angle polaire θ (rad)', 'Énergie cinétique spécifique réduite',
               series('Référentiel de l’astre', theta, kinetic_body), series('Second référentiel : ajouter V à v', theta, kinetic_ref)),
         chart('Dans le référentiel de l’astre, l’énergie mécanique est constante', 'Angle polaire θ (rad)', 'Énergie spécifique réduite', series('v²/2−1/r', theta, kinetic_body - 1 / r))],
        orbit_scene('Une hyperbole autour de l’astre', [path('Sonde : référentiel de l’astre', x, y)], [body('Astre', theta * 0, theta * 0, 1, 8), body('Sonde', x, y, 0, 5)],
                    max(2, min(20, float(np.quantile(r, .9)) * 1.15)), 'Seule une portion finie de l’hyperbole est tracée ; les vitesses d’entrée et de sortie du bilan sont les limites à l’infini.'),
        ['À l’infini, ε=v∞²/2>0 et h=bv∞. On obtient e=√(1+b²v∞⁴/(GM)²), avec GM=1 dans les unités utilisées.',
         'La conique r=h²/[GM(1+e cosθ)] a des asymptotes aux angles θ∞=arccos(−1/e). La déviation vaut δ=2arcsin(1/e)=2arctan[GM/(bv∞²)].',
         'Dans le référentiel de l’astre, entrée et sortie lointaines ont la même norme v∞ : l’attraction modifie la direction de la vitesse.',
         'Dans un second référentiel, vin=vrel,in+V et vout=vrel,out+V. Le gain spécifique vaut V·(vrel,out−vrel,in). Il change de signe avec l’orientation du survol.'],
        ['Astre ponctuel ou sphérique, sans collision et sans atmosphère ; son rayon matériel n’est pas modélisé.',
         'La masse de la sonde est négligeable : l’astre conserve ici sa vitesse V. Un bilan exact à deux corps inclurait sa très faible variation de quantité de mouvement.',
         'Les courbes d’énergie cinétique restent calculées sur une portion finie ; les métriques entrée/sortie utilisent les valeurs asymptotiques exactes.',
         'Source de contexte : ESA, « What are gravity assists? » et documentation GODOT sur les survols hyperboliques.'])


def marees(p):
    distance, q = p['distance'], p['mass_ratio']
    x = np.linspace(-1, 1, 301)
    exact = q * (1 / (distance - x) ** 2 - 1 / distance ** 2)
    linear = 2 * q / distance ** 3 * x
    transverse = -q * x / (distance ** 2 + x ** 2) ** 1.5
    transverse_linear = -q / distance ** 3 * x
    radial_strength = 2 * q / distance ** 3
    stretch = radial_strength / (1 + radial_strength)
    angle = np.linspace(0, TAU, 201)
    circlex, circley = np.cos(angle), np.sin(angle)
    # Le champ linéarisé est représenté par des segments, pas par une forme d’équilibre.
    field_paths = [path('Contour du corps (R=1)', circlex, circley, 2)]
    for j, angle0 in enumerate(np.linspace(0, TAU, 12, endpoint=False)):
        px, py = math.cos(angle0), math.sin(angle0)
        field_paths.append(path('Différence d’accélération' if j == 0 else '', [px, px + .6 * stretch * px], [py, py - .3 * stretch * py], 0))
    surface_relative_error = abs(exact[-1] - linear[-1]) / abs(exact[-1])
    return result(
        [metric('Accélération du centre vers l’astre', q / distance ** 2, 'Gm/R²'),
         metric('Coefficient d’étirement radial 2GM/D³', radial_strength, 'Gm/R³'),
         metric('Coefficient transverse −GM/D³', -q / distance ** 3, 'Gm/R³'),
         metric('Marée radiale linéaire / gravité propre en surface', radial_strength),
         metric('Erreur relative linéaire sur la face proche', surface_relative_error),
         metric('Somme des trois coefficients principaux', radial_strength - 2 * q / distance ** 3, 'Gm/R³')],
        [chart('Soustraire l’accélération du centre : composante radiale', 'Position x/R sur l’axe dirigé vers l’astre', 'Différence d’accélération (Gm/R²)', series('Champ exact', x, exact), series('Approximation du premier ordre', x, linear)),
         chart('Dans une direction perpendiculaire : compression', 'Position y/R', 'Composante transverse (Gm/R²)', series('Champ exact', x, transverse), series('Approximation du premier ordre', x, transverse_linear))],
        orbit_scene('Étirement radial et compression transverse', field_paths, [], 1.9,
                    'Segments du champ de marée linéarisé. L’astre est situé à droite. La longueur des segments est adaptée pour rester lisible ; ce dessin ne calcule pas une déformation matérielle.'),
        ['Se placer dans un repère dont l’origine suit le centre du corps. Soustraire son accélération gravitationnelle à celle d’un point voisin.',
         'Sur l’axe vers l’astre : Δax=GM[(D−x)⁻²−D⁻²]. Si |x|≪D, le développement limité donne Δax≈2GMx/D³.',
         'Dans une direction perpendiculaire : Δay≈−GMy/D³. La matrice du champ linéarisé est (GM/D³)diag(2,−1,−1), de trace nulle.',
         'La gravité propre à la surface vaut Gm/R². Le rapport 2(M/m)(R/D)³ indique si la différence d’attraction devient comparable à cette gravité ; il ne suffit pas à déterminer une limite exacte de dislocation.'],
        ['Corps sphérique et astre ponctuel ; le laboratoire représente le champ instantané, sans rotation orbitale, déformation ni réponse hydrodynamique.',
         'Unités R=m=G=1. L’approximation linéaire exige R/D≪1 ; le cas proche est affiché pour mesurer sa dégradation.',
         'Le rapport de marée n’est pas la limite de Roche d’un corps fluide : cette limite exige un modèle supplémentaire d’équilibre.'])


def fusee(p):
    m0, ratio, u, burn, g = p['m0'] * 1000, p['ratio'], p['u'], p['burn'], p['g']
    final_mass = m0 / ratio
    flow = (m0 - final_mass) / burn
    t = np.linspace(0, burn, 401)
    mass = m0 - flow * t
    ideal_velocity = u * np.log(m0 / mass)
    velocity = ideal_velocity - g * t
    position = u * (t + mass / flow * np.log(mass / m0)) - g * t * t / 2
    acceleration = u * flow / mass - g
    return result(
        [metric('Masse finale mf', final_mass / 1000, 't'), metric('Débit de masse q', flow, 'kg/s'), metric('Poussée constante uq', u * flow / 1000, 'kN'),
         metric('Gain idéal de vitesse u ln(m₀/mf)', u * math.log(ratio), 'm/s'), metric('Perte de vitesse gτ', g * burn, 'm/s'),
         metric('Vitesse finale', velocity[-1], 'm/s'), metric('Déplacement vertical final', position[-1] / 1000, 'km'),
         metric('Accélération initiale', acceleration[0], 'm/s²')],
        [chart('Une masse qui diminue à débit constant', 'Temps (s)', 'Masse (t)', series('m(t)', t, mass / 1000)),
         chart('Le bilan de quantité de mouvement donne la vitesse', 'Temps (s)', 'Vitesse (m/s)', series('Sans pesanteur', t, ideal_velocity), series('Avec pesanteur', t, velocity)),
         chart('La même poussée accélère davantage une masse plus faible', 'Temps (s)', 'Accélération (m/s²)', series('a(t)', t, acceleration)),
         chart('Déplacement vertical pendant la poussée', 'Temps (s)', 'Déplacement (km)', series('z(t)−z(0)', t, position / 1000))],
        dict(kind='trajectory', title='Une montée calculée par bilan de quantité de mouvement',
             paths=[path('Trajectoire verticale (km)', t * 0, position / 1000)],
             bodies=[body('Fusée', t * 0, position / 1000, 0, 6)], times=t,
             bounds=[-max(1, np.ptp(position) / 10000), max(1, np.ptp(position) / 10000), min(0, float(np.min(position)) / 1000) - 1, max(1, float(np.max(position)) / 1000) + 1],
             description='Le gaz n’est pas dessiné. Aucune réaction du sol n’est incluse ; le point peut commencer par descendre si la poussée ne compense pas son poids.'),
        ['Considérer pendant dt le système fermé constitué de la fusée et de la masse −dm qui vient d’être éjectée. Dans le référentiel galiléen, le gaz a vitesse v−u.',
         'Le bilan donne m dv=−u dm−mg dt. Le terme propulsif provient de la vitesse relative du gaz ; écrire seulement d(mv)/dt=−mg serait incorrect pour la fusée seule.',
         'À débit constant q=−dm/dt>0, m(t)=m₀−qt et dv/dt=uq/m(t)−g. Intégrer : v(t)=u ln[m₀/m(t)]−gt.',
         'Intégrer encore la vitesse : z(t)−z₀=u{t+[m(t)/q]ln[m(t)/m₀]}−gt²/2. À la fin, Δv=u ln(m₀/mf)−gτ.'],
        ['Éjection colinéaire à vitesse relative constante ; débit constant ; poussée verticale ; masse finale strictement positive.',
         'Pesanteur uniforme et absence de traînée. Ce modèle de bilan n’est pas une simulation complète d’un lancement réel.',
         'La vitesse initiale est nulle et la position initiale sert d’origine. Le référentiel galiléen et la vitesse relative d’éjection doivent être distingués.'])


def coriolis(p):
    omega, vx, x0, y0, duration = p['omega'], p['vx'], p['x0'], p['y0'], p['duration']
    t = np.linspace(0, duration, 501)
    cosine, sine = np.cos(omega * t), np.sin(omega * t)
    xi, yi = x0 + vx * t, np.full_like(t, y0)
    x, y = cosine * xi + sine * yi, -sine * xi + cosine * yi
    # R(-Ωt)vgaliléenne − Ω×r fournit les vitesses relatives.
    vrx, vry = cosine * vx + omega * y, -sine * vx - omega * x
    centrifugalx, centrifugaly = omega * omega * x, omega * omega * y
    corx, cory = 2 * omega * vry, -2 * omega * vrx
    ax, ay = centrifugalx + corx, centrifugaly + cory
    explicit_ax = -omega * omega * x - 2 * omega * sine * vx
    explicit_ay = -omega * omega * y - 2 * omega * cosine * vx
    balance_error = np.max(np.hypot(ax - explicit_ax, ay - explicit_ay))
    bound = max(1, float(np.max(np.hypot(x, y))) * 1.1)
    return result(
        [metric('Norme de la vitesse galiléenne constante', vx, 'm/s'), metric('Vitesse relative finale', math.hypot(vrx[-1], vry[-1]), 'm/s'),
         metric('Accélération de Coriolis finale (norme)', math.hypot(corx[-1], cory[-1]), 'm/s²'),
         metric('Accélération centrifuge finale (norme)', math.hypot(centrifugalx[-1], centrifugaly[-1]), 'm/s²'),
         metric('Erreur sur la somme des accélérations d’inertie', balance_error, 'm/s²')],
        [chart('Une vitesse relative différente de la vitesse galiléenne', 'Temps (s)', 'Vitesse (m/s)',
               series('vx dans les axes tournants', t, vrx), series('vy dans les axes tournants', t, vry), series('Norme de la vitesse galiléenne', t, t * 0 + vx)),
         chart('Bilan suivant x dans le référentiel tournant', 'Temps (s)', 'Accélération (m/s²)',
               series('Coriolis', t, corx), series('Centrifuge', t, centrifugalx), series('Somme = accélération relative', t, ax)),
         chart('La distance au centre est indépendante du choix des axes', 'Temps (s)', 'Distance (m)', series('Dans les axes tournants', t, np.hypot(x, y)), series('Dans les axes galiléens', t, np.hypot(xi, yi)))],
        orbit_scene('La trajectoire vue par l’observateur tournant', [path('Coordonnées tournantes', x, y)],
                    [body('Point libre', x, y, 0, 5), body('Origine commune', t * 0, t * 0, 1, 4)], bound,
                    'Dans les axes galiléens, le mouvement est la droite (x₀+v₀t,y₀). Le dessin utilise uniquement les axes tournants.', t),
        ['Partir de la solution galiléenne rI(t)=(x₀+v₀t,y₀), qui satisfait r̈I=0. Faire tourner ses coordonnées d’un angle −Ωt : rR=R(−Ωt)rI.',
         'Dériver : vR=R(−Ωt)vI−Ω×rR. Une nouvelle dérivation donne aR=−2Ω×vR−Ω×(Ω×rR).',
         'Le premier terme est l’accélération associée à la force de Coriolis ; le second est centrifuge. Pour Ω suivant z : acor=(2Ωvy,−2Ωvx) et acent=Ω²(x,y).',
         'Coriolis ne travaille pas dans le référentiel tournant car (Ω×vR)·vR=0. Pour Ω constant, la force centrifuge dérive du potentiel −mΩ²r²/2.'],
        ['Point libre, sans force réelle ; deux référentiels de même origine ; rotation uniforme autour d’un axe fixe.',
         'Les forces d’inertie permettent d’écrire la dynamique dans les axes tournants ; elles ne modifient pas le mouvement rectiligne dans le référentiel galiléen.',
         'Ω peut être négatif : les termes de Coriolis changent de sens, alors que le terme centrifuge dépend de Ω².'])


COMPUTE = {name: globals()[name] for name in ['orbite_kepler', 'deux_corps', 'potentiel_effectif', 'transfert_hohmann', 'diffusion_gravitationnelle', 'marees', 'fusee', 'coriolis']}
