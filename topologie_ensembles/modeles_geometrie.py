"""Géométrie exacte des dix premiers laboratoires ; les maillages illustrent."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, scene, result, clean
from catalogue_geometrie import LABS


def _point(x, label, color=0):
    return dict(x=float(x[0]), y=float(x[1]), label=label, colorIndex=color)


def _path(points, label, color=0, closed=False, fill=False, **extra):
    return dict(points=np.asarray(points), label=label, colorIndex=color,
                closed=closed, fill=fill, **extra)


def _disc(c, r, label, color=0, closed=True, fill=False):
    return dict(x=float(c[0]), y=float(c[1]), r=float(r), label=label,
                colorIndex=color, closed=closed, fill=fill)


def _dots(label, x, y):
    s = series(label, x, y)
    s['style'] = 'dots'
    return s


def _unit(angle):
    u = np.array([math.cos(math.radians(angle)), math.sin(math.radians(angle))])
    u[np.abs(u) < 1e-14] = 0.0
    return u


def lp_norm(x, p):
    x = np.abs(np.asarray(x, dtype=float))
    return float(np.max(x)) if p == math.inf else float(np.sum(x ** p) ** (1 / p))


def ball_boundary(p, radius=1., count=241):
    theta = np.linspace(0, 2 * math.pi, count)
    uv = np.column_stack((np.cos(theta), np.sin(theta)))
    norm = np.max(np.abs(uv), axis=1) if p == math.inf else np.sum(np.abs(uv) ** p, axis=1) ** (1 / p)
    return radius * uv / norm[:, None]


def _geometry(title, description, paths=(), points=(), discs=(), bounds=(-2, 2, -2, 2), **data):
    return scene('geometry', title, description, paths=list(paths), points=list(points),
                 discs=list(discs), bounds=list(bounds), **data)


def boules_normes(p):
    q = math.inf if p['norm'] == 'inf' else (float(p['p']) if p['norm'] == 'p' else float(p['norm']))
    x = np.array([p['x'], p['y']], dtype=float)
    r = float(p['radius'])
    d = lp_norm(x, q)
    margin = r - d
    belongs = d <= r if p['closed'] == 'closed' else d < r
    paths = [_path(ball_boundary(k, r), name, i, True, False)
             for i, (k, name) in enumerate([(1, 'Norme 1'), (2, 'Norme 2'), (math.inf, 'Norme ∞')])]
    paths.append(_path(ball_boundary(q, r), 'Boule choisie', 3, True, True,
                       boundaryClosed=p['closed'] == 'closed'))
    theta = np.linspace(0, math.pi / 2, 181)
    curves = []
    for k, name in [(1, 'Norme 1'), (2, 'Norme 2'), (math.inf, 'Norme ∞'), (q, 'Choisie')]:
        uv = np.column_stack([np.cos(theta), np.sin(theta)])
        ns = np.max(np.abs(uv), axis=1) if k == math.inf else np.sum(np.abs(uv) ** k, axis=1) ** (1 / k)
        curves.append(series(name, theta * 180 / math.pi, r / ns))
    extent = max(2.25, r * 1.2, max(abs(x)) + .3)
    return result([metric('Norme choisie ‖x‖', d), metric('Marge exacte r−‖x‖', margin),
                   metric('Appartient à la boule', 'Oui' if belongs else 'Non'),
                   metric('Rayon de voisinage garanti', max(0., margin))],
                  [chart('Rayon euclidien du bord suivant la direction', 'Angle (°)', 'Rayon', *curves)],
                  _geometry('Une définition, plusieurs boules', 'Le point et les quatre contours proviennent des normes calculées.', paths,
                            [_point([0, 0], 'Centre', 4), _point(x, 'Point x', 3)],
                            bounds=(-extent, extent, -extent, extent), norm=q if q != math.inf else 'inf',
                            margin=margin, membership=bool(belongs)),
                  ['Dans la norme choisie, B(0,r) est définie par ‖x‖<r (ou ≤r).',
                   'Si la marge m=r−‖x‖ est positive, l’inégalité triangulaire donne B(x,m)⊂B(0,r).',
                   'Les normes sont équivalentes en dimension finie : elles définissent les mêmes ouverts, malgré les formes différentes.'],
                  ['Les boules sont centrées en 0 dans ℝ² ; le rayon de voisinage indiqué utilise la norme choisie.',
                   'Le contour polygonal est une illustration. L’appartenance et la marge utilisent la formule de la norme.'])


def classify_shape(shape, x, radius):
    rho = float(np.linalg.norm(x))
    if shape == 'annulus':
        inside = radius / 2 <= rho <= radius
        interior = radius / 2 < rho < radius
        adherent = inside
        boundary = rho == radius / 2 or rho == radius
        distance_boundary = min(abs(rho - radius / 2), abs(rho - radius))
    else:
        inside = rho <= radius if shape == 'closed' else (rho < radius and (shape != 'punctured' or rho > 0))
        interior = rho < radius and (shape != 'punctured' or rho > 0)
        adherent = rho <= radius
        boundary = rho == radius or (shape == 'punctured' and rho == 0)
        distance_boundary = min(rho, abs(rho - radius)) if shape == 'punctured' else abs(rho - radius)
    return dict(rho=rho, belongs=bool(inside), interior=bool(interior), adherent=bool(adherent),
                boundary=bool(boundary), boundary_distance=distance_boundary)


def interieur_frontiere(p):
    x = np.array([p['x'], p['y']], dtype=float)
    r = float(p['radius'])
    shape = p['shape']
    info = classify_shape(shape, x, r)
    paths = []
    if shape == 'annulus':
        paths = [_path(np.vstack([ball_boundary(2, r), ball_boundary(2, r / 2)[::-1]]), 'Anneau A', 0, True, True)]
    discs = [_disc([0, 0], r, 'Bord extérieur', 0, shape in ('annulus', 'closed'), shape != 'annulus')]
    if shape == 'annulus':
        discs.append(_disc([0, 0], r / 2, 'Bord intérieur', 1, True, False))
    if shape == 'punctured':
        discs.append(_disc([0, 0], .025, '0 est exclu', 1, False, False))
    discs.append(_disc(x, p['epsilon'], 'Voisinage B(x,ε)', 3, False, False))
    t = np.linspace(0, 1.25 * r, 251)
    flags = [classify_shape(shape, [z, 0], r) for z in t]
    curves = [series(label, t, [int(a[key]) + offset for a in flags])
              for key, label, offset in [('belongs', 'Dans A', 0), ('interior', 'Dans Int(A) + 1,5', 1.5),
                                         ('adherent', 'Dans adh(A) + 3', 3)]]
    title = 'Intérieur' if info['interior'] else ('Frontière' if info['boundary'] else 'Extérieur de l’adhérence')
    extent = max(2.5, r + .5, max(abs(x)) + p['epsilon'] + .3)
    return result([metric('Position topologique', title), metric('Appartient à A', 'Oui' if info['belongs'] else 'Non'),
                   metric('Point adhérent', 'Oui' if info['adherent'] else 'Non'), metric('Distance à la frontière', info['boundary_distance'])],
                  [chart('Test radial : 1 signifie oui, avec décalages verticaux', 'Rayon ρ', 'Indicateur décalé', *curves)],
                  _geometry('A, son bord et un voisinage', 'La classification est analytique, y compris aux points exclus.', paths,
                            [_point(x, 'Point x', 3)], discs, (-extent, extent, -extent, extent), classification=info),
                  ['x est intérieur lorsqu’un rayon ε>0 permet B(x,ε)⊂A.',
                   'x est adhérent lorsque chaque voisinage rencontre A ; il n’a pas besoin d’appartenir à A.',
                   'Fr(A)=adh(A) privé de Int(A). Pour le disque épointé, 0 est un point frontière supplémentaire.'],
                  ['Les ensembles sont définis par les inégalités radiales indiquées ; l’anneau inclut ses deux cercles.',
                   'Les indicateurs dessinés sur une grille ne servent pas à décider de l’appartenance exacte au bord.'])


def reciprocal_distance(x, include_zero=False):
    """Distance à l'ensemble infini {1/n}, avec infimum atteint ou non."""
    x = float(x)
    if x <= 0:
        return dict(distance=-x, nearest=0., attained=bool(include_zero), belongs=bool(include_zero and x == 0), index=None)
    if x >= 1:
        return dict(distance=x - 1, nearest=1., attained=True, belongs=x == 1, index=1)
    n = max(1, math.floor(1 / x))
    candidates = [(abs(x - 1 / k), k) for k in (n, n + 1)]
    d, k = min(candidates)
    return dict(distance=d, nearest=1 / k, attained=True, belongs=d == 0, index=k)


def adherence_suite(p):
    N = int(p['N'])
    x, eps = float(p['x']), float(p['epsilon'])
    zero = p['include_zero'] == 'yes'
    info = reciprocal_distance(x, zero)
    seq = 1 / np.arange(1, N + 1)
    n_witness = math.floor(1 / eps) + 1
    while 1 / n_witness >= eps:
        n_witness += 1
    grid = np.linspace(-.3, 1.3, 401)
    exact = [reciprocal_distance(a, zero)['distance'] for a in grid]
    plotted = np.min(abs(grid[:, None] - seq), axis=1)
    if zero:
        plotted = np.minimum(plotted, abs(grid))
    pts = [_point([a, 0], f'1/{i + 1}' if i < 7 else '', 0) for i, a in enumerate(seq)]
    pts += [_point([x, .17], 'x', 3), _point([0, 0], '0 : limite', 1)]
    discs = [_disc([0, 0], .014, '0 inclus' if zero else '0 exclu', 1, zero, zero)]
    if info['attained']:
        pts.append(_point([info['nearest'], -.17], 'Point minimisant', 2))
    return result([metric('Distance exacte à A', info['distance']), metric('Infimum atteint', 'Oui' if info['attained'] else 'Non'),
                   metric('x appartient à A', 'Oui' if info['belongs'] else 'Non'),
                   metric('Témoin 1/n dans ]0,ε[ : n', n_witness), metric('A est compact', 'Oui' if zero else 'Non')],
                  [chart('Le nuage fini peut masquer une distance nulle', 'Point x', 'Distance', series('À A infini', grid, exact), series(f'Aux {N} points dessinés', grid, plotted)),
                   chart('Une suite converge vers le point adhérent 0', 'Indice n', '1/n', _dots('Éléments de A', np.arange(1, N + 1), seq))],
                  _geometry('Les points isolés s’accumulent en 0', 'Le nombre N commande le dessin, jamais la définition infinie de A.',
                            [_path([[x - eps, .17], [x + eps, .17]], 'Voisinage sur l’axe', 3)], pts, discs,
                            (-.35, 1.35, -.4, .45), infinite_set=True, include_zero=zero, distance=info,
                            witness=dict(n=n_witness, value=1 / n_witness, epsilon=eps)),
                  ['Pour x>0, les deux réciproques qui encadrent x donnent le minimum exact ; on n’énumère pas seulement N termes.',
                   'Pour x≤0, d(x,A)=−x ; sans 0, cette borne inférieure n’est pas atteinte.',
                   'Chaque voisinage de 0 contient un 1/n dès que n>1/ε. Ajouter 0 rend A fermé et borné, donc compact dans ℝ.'],
                  ['A désigne l’ensemble infini. Le nuage visible est uniquement une troncature.',
                   'L’adhérence vaut toujours {1/n : n≥1}∪{0}. Chaque 1/n est isolé.'])


def topologie_relative(p):
    b, x, eps = float(p['b']), float(p['x']), float(p['epsilon'])
    belongs = x < b
    ambient = 0 < x < min(1., b)
    contains = belongs and (b > 1 or x + eps <= b)
    right = min(1., b)
    paths = [_path([[0, 0], [1, 0]], 'Espace X=[0,1]', 0),
             _path([[0, .14], [right, .14]], 'A, ouvert relatif', 1),
             _path([[max(0., x - eps), -.14], [min(1., x + eps), -.14]], 'B(x,ε)∩X', 3)]
    discs = [_disc([0, .14], .012, '0 inclus dans A', 1, True, True),
             _disc([right, .14], .012, 'Bord droit', 1, b > 1, b > 1)]
    grid = np.linspace(0, 1, 401)
    return result([metric('x est intérieur dans X', 'Oui' if belongs else 'Non'),
                   metric('x est intérieur dans ℝ', 'Oui' if ambient else 'Non'),
                   metric('B(x,ε)∩X est contenu dans A', 'Oui' if contains else 'Non'),
                   metric('Rayon relatif garanti si x∈A', max(0., (b - x) / 2))],
                  [chart('Même ensemble, deux notions d’intérieur', 'x dans X', 'Indicateur',
                         series('Intérieur relatif', grid, (grid < b).astype(int)),
                         series('Intérieur ambiant, décalé de 1,5', grid, ((grid > 0) & (grid < min(1., b))).astype(int) + 1.5))],
                  _geometry('Le voisinage est coupé par X', 'Les trois lignes sont décalées pour comparer leurs extrémités.', paths,
                            [_point([x, -.14], 'x', 3)], discs, (-.25, 1.5, -.4, .45),
                            relative_interior=belongs, ambient_interior=ambient, neighborhood_inside=contains),
                  ['La topologie induite sur X utilise les traces U∩X des ouverts U de ℝ.',
                   'Ici U=]−1/2,b[, donc A est ouvert dans X pour toute valeur proposée de b.',
                   'Pour x<b, ε=(b−x)/2 garantit Bℝ(x,ε)∩X⊂A. En 0, aucun voisinage ambiant n’est contenu dans A.'],
                  ['x est contraint à X=[0,1]. Les lignes du dessin ont des décalages verticaux de présentation.',
                   'La borne droite b est exclue ; 1 appartient à A seulement si b>1.'])


def operations_ouverts(p):
    N, x = int(p['N']), float(p['x'])
    intersection = p['operation'] == 'intersection'
    finite = abs(x) < 1 / N if intersection else 1 / N <= x <= 1
    infinite = x == 0 if intersection else 0 < x <= 1
    ns = np.unique(np.round(np.geomspace(1, N, min(7, N))).astype(int))
    paths, discs = [], []
    for j, n in enumerate(ns):
        a, b = (-1 / n, 1 / n) if intersection else (1 / n, 1.)
        y = .2 * j
        paths.append(_path([[a, y], [b, y]], f'n={n}', j % 4))
        discs.extend([_disc([a, y], .014, 'Bord', j % 4, not intersection, not intersection),
                      _disc([b, y], .014, '', j % 4, not intersection, not intersection)])
    ngrid = np.arange(1, N + 1)
    fflags = np.abs(x) < 1 / ngrid if intersection else ((1 / ngrid <= x) & (x <= 1))
    return result([metric('Appartient au résultat fini', 'Oui' if finite else 'Non'),
                   metric('Appartient au résultat infini', 'Oui' if infinite else 'Non'),
                   metric('Résultat fini', f']−1/{N},1/{N}[' if intersection else f'[1/{N},1]'),
                   metric('Résultat infini', '{0}, non ouvert' if intersection else ']0,1], non fermé')],
                  [chart('La borne mobile tend vers zéro', 'n', 'Borne 1/n', series('1/n', ngrid, 1 / ngrid)),
                   chart('Appartenance de x aux opérations finies', 'Dernier indice n', 'Indicateur', series('Résultat fini', ngrid, fflags.astype(int)))],
                  _geometry('Une famille infinie, quelques membres visibles', 'Chaque ligne représente un membre exact de la famille.', paths,
                            [_point([x, -.2], 'Point x', 3), _point([0, -.2], '0', 1)], discs,
                            (-1.3, 1.3, -.4, .2 * len(ns) + .2), finite_membership=bool(finite),
                            infinite_membership=bool(infinite), finite_limit_radius=1 / N),
                  ['Une intersection finie d’ouverts est ouverte ; une union quelconque d’ouverts est ouverte.',
                   'Une union finie de fermés est fermée ; une intersection quelconque de fermés est fermée.',
                   'Les opérations inversées ne conservent pas ces propriétés en général : ces deux familles sont des contre-exemples exacts.'],
                  ['Le résultat infini est calculé par les quantificateurs sur tous les n≥1, pas par un très grand N.',
                   'Dans le cas intersection, les deux extrémités sont exclues ; dans le cas union, elles sont incluses.'])


def project_disk(x, center, radius):
    x, c = np.asarray(x, float), np.asarray(center, float)
    v = x - c
    rho = float(np.linalg.norm(v))
    return x.copy() if rho <= radius else c + radius * v / rho


def disk_union_distance(x, separation, radius):
    x = np.asarray(x, float)
    centers = [np.array([-separation / 2, 0.]), np.array([separation / 2, 0.])]
    distances = [max(0., float(np.linalg.norm(x - c)) - radius) for c in centers]
    best = min(distances)
    projections = [project_disk(x, c, radius) for c, d in zip(centers, distances) if d == best]
    if len(projections) == 2 and np.array_equal(projections[0], projections[1]):
        projections.pop()
    return best, projections, distances


def distance_ensemble(p):
    sep, r = float(p['separation']), float(p['radius'])
    x = np.array([p['x'], p['y']], float)
    d, projections, ds = disk_union_distance(x, sep, r)
    centers = [np.array([-sep / 2, 0.]), np.array([sep / 2, 0.])]
    grid = np.linspace(-3.5, 3.5, 501)
    dist = np.array([disk_union_distance([a, x[1]], sep, r)[0] for a in grid])
    paths = [_path([x, q], f'Projection {i + 1}', i + 1) for i, q in enumerate(projections)]
    points = [_point(x, 'x', 3)] + [_point(q, f'p{i + 1}', i + 1) for i, q in enumerate(projections)]
    return result([metric('Distance exacte d(x,A)', d), metric('Nombre de projections', len(projections)),
                   metric('A est connexe', 'Oui' if sep <= 2 * r else 'Non'),
                   metric('A est convexe', 'Oui' if sep == 0 else 'Non')],
                  [chart('Coupe horizontale de la fonction distance', 'Abscisse u à ordonnée y fixée', 'Distance', series('d((u,y),A)', grid, dist)),
                   chart('Lipschitz : pentes des sécantes, bornées par 1', 'Abscisse u', 'Pente en valeur absolue',
                         series('Pente calculée', (grid[1:] + grid[:-1]) / 2, abs(np.diff(dist) / np.diff(grid))),
                         series('Borne théorique 1', grid, np.ones_like(grid)))],
                  _geometry('La projection peut avoir deux valeurs', 'La distance est le minimum des deux distances exactes aux disques.', paths, points,
                            [_disc(c, r, f'Disque {i + 1}', i, True, True) for i, c in enumerate(centers)],
                            (-3.6, 3.6, -2.8, 2.8), projections=projections, distance=d, distance_to_disks=ds),
                  ['Pour un disque fermé D(c,r), d(x,D)=max(‖x−c‖−r,0).',
                   'Pour leur union A, prendre le minimum des deux distances et garder tous les points minimisants.',
                   'Pour tout ensemble non vide, |d(x,A)−d(y,A)|≤‖x−y‖. L’unicité de la projection exige un cadre supplémentaire, notamment la convexité.'],
                  ['La distance est euclidienne. Les deux disques ont le même rayon et des centres sur l’axe horizontal.',
                   'Le tracé des sécantes illustre la borne ; sa preuve vient de l’inégalité triangulaire, pour tous les points.'])


def segment_min_norm(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    v = b - a
    vv = float(v @ v)
    t = min(1., max(0., -float(a @ v) / vv)) if vv else 0.
    return float(np.linalg.norm(a + t * v)), t


def segment_disk_interval(a, b, center, radius):
    a, b, c = np.asarray(a, float), np.asarray(b, float), np.asarray(center, float)
    v, u = b - a, a - c
    A, B, C = float(v @ v), 2 * float(u @ v), float(u @ u) - radius ** 2
    if A == 0:
        return (0., 1.) if C <= 0 else None
    delta = B * B - 4 * A * C
    if delta < 0:
        return None
    lo = max(0., (-B - math.sqrt(max(0., delta))) / (2 * A))
    hi = min(1., (-B + math.sqrt(max(0., delta))) / (2 * A))
    return (lo, hi) if lo <= hi else None


def intervals_cover_unit(intervals):
    intervals = sorted(q for q in intervals if q is not None)
    end = 0.
    for lo, hi in intervals:
        if lo > end + 2e-14:
            return False
        end = max(end, hi)
    return end >= 1 - 2e-14


def convexite(p):
    shape, rho, sep = p['shape'], float(p['rho']), float(p['separation'])
    a, b = rho * _unit(p['a']), rho * _unit(p['b'])
    discs, paths = [], []
    if shape == 'union':
        r = .65
        centers = [np.array([-sep / 2, 0.]), np.array([sep / 2, 0.])]
        a, b = centers[0] + r * a, centers[1] + r * b
        intervals = [segment_disk_interval(a, b, c, r) for c in centers]
        valid = intervals_cover_unit(intervals)
        witness_a, witness_b = centers[0] + [0, r], centers[1] + [0, r]
        discs = [_disc(c, r, f'Disque {i + 1}', i, True, True) for i, c in enumerate(centers)]
        global_convex = sep == 0
        distance = lambda z: disk_union_distance(z, sep, r)[0]
        criterion = 'Le paramètre t doit appartenir à la réunion des deux intervalles quadratiques, qui doit couvrir [0,1].'
    else:
        minimum, _ = segment_min_norm(a, b)
        valid = shape == 'disk' or minimum >= .5
        global_convex = shape == 'disk'
        witness_a, witness_b = np.array([.75, 0]), np.array([-.75, 0])
        if shape == 'annulus':
            paths = [_path(np.vstack([ball_boundary(2), ball_boundary(2, .5)[::-1]]), 'Anneau A', 0, True, True)]
            discs = [_disc([0, 0], 1, 'Bord extérieur', 0), _disc([0, 0], .5, 'Bord intérieur', 1)]
            distance = lambda z: max(.5 - np.linalg.norm(z), np.linalg.norm(z) - 1, 0.)
        else:
            discs = [_disc([0, 0], 1, 'Disque convexe', 0, True, True)]
            distance = lambda z: max(np.linalg.norm(z) - 1, 0.)
        criterion = 'La norme maximale est aux extrémités. Dans l’anneau, minimiser la norme au carré sur le segment et vérifier min‖z(t)‖≥1/2.'
    minimum, t_min = segment_min_norm(a, b)
    t = np.linspace(0, 1, 301)
    z = (1 - t[:, None]) * a + t[:, None] * b
    paths += [_path([a, b], 'Segment [a,b]', 3)]
    points = [_point(a, 'a', 3), _point(b, 'b', 3), _point((1 - t_min) * a + t_min * b, 'Point le plus proche de 0', 2)]
    if not global_convex:
        mid = (witness_a + witness_b) / 2
        paths.append(_path([witness_a, witness_b], 'Témoin de non-convexité', 1))
        points += [_point(witness_a, 'u', 1), _point(witness_b, 'v', 1), _point(mid, '(u+v)/2 hors de A', 1)]
    else:
        mid = (a + b) / 2
    return result([metric('Tout le segment choisi est dans A', 'Oui' if valid else 'Non'),
                   metric('A est convexe', 'Oui' if global_convex else 'Non'), metric('Minimum de ‖z(t)‖ sur le segment', minimum),
                   metric('Distance du milieu témoin à A', float(distance(mid)))],
                  [chart('La distance positive repère la sortie du segment', 'Paramètre t de [a,b]', 'd(z(t),A)', series('Distance exacte', t, [distance(q) for q in z]))],
                  _geometry('La convexité porte sur tous les segments', 'Le segment choisi et un témoin indépendant sont distingués.', paths, points, discs,
                            (-3, 3, -1.7, 1.7), segment_contained=bool(valid), global_convex=global_convex,
                            endpoints=[a, b], witness_endpoints=[witness_a, witness_b], witness_midpoint=mid),
                  [criterion, 'Un segment réussi ne prouve pas que A est convexe : la définition quantifie sur toutes les paires (a,b)∈A².',
                   'Un seul segment qui sort suffit à réfuter la convexité. Pour deux disques distincts de même rayon, les deux points supérieurs fournissent toujours ce témoin.'],
                  ['Les points choisis appartiennent à A pour tous les paramètres proposés.',
                   'L’acceptation du segment repose sur un minimum quadratique ou des intervalles exacts ; le graphe est une illustration.'])


def convex_hull(points):
    """Chaînes monotones, sommets dans le sens trigonométrique, sans doublons."""
    pts = sorted(set(tuple(map(float, p)) for p in points))
    if len(pts) <= 1:
        return np.array(pts, dtype=float).reshape(-1, 2)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    chains = []
    for values in (pts, list(reversed(pts))):
        chain = []
        for q in values:
            while len(chain) >= 2 and cross(chain[-2], chain[-1], q) <= 0:
                chain.pop()
            chain.append(q)
        chains.append(chain[:-1])
    return np.array(chains[0] + chains[1], dtype=float)


def polygon_signed_area(vertices):
    v = np.asarray(vertices, float)
    return float(np.sum(v[:, 0] * np.roll(v[:, 1], -1) - v[:, 1] * np.roll(v[:, 0], -1)) / 2)


def halfplane_margins(vertices, point):
    v, x = np.asarray(vertices, float), np.asarray(point, float)
    edges = np.roll(v, -1, axis=0) - v
    cross = edges[:, 0] * (x[1] - v[:, 1]) - edges[:, 1] * (x[0] - v[:, 0])
    return cross / np.linalg.norm(edges, axis=1)


def enveloppe_convexe(p):
    N, seed, alpha = int(p['N']), int(p['seed']), float(p['alpha'])
    rng = np.random.default_rng(seed)
    angles = rng.uniform(0, 2 * math.pi, N)
    radii = np.sqrt(rng.uniform(.02, 1, N))
    pts = np.column_stack([1.25 * radii * np.cos(angles), radii * np.sin(angles)])
    pts[0] = [1.6, 0]
    hull = convex_hull(pts)
    weights = np.full(N, (1 - alpha) / N)
    weights[0] += alpha
    bary = weights @ pts
    margins = halfplane_margins(hull, bary)
    area = polygon_signed_area(hull)
    stems = series('Poids λᵢ', np.arange(1, N + 1), weights)
    stems['style'] = 'stems'
    return result([metric('Nombre de sommets extrêmes', len(hull)), metric('Aire de l’enveloppe', area),
                   metric('Somme des poids', float(weights.sum())), metric('Marge minimale du barycentre aux côtés', float(margins.min()))],
                  [chart('Une combinaison convexe : poids positifs de somme 1', 'Indice i', 'Poids λᵢ', stems),
                   chart('Tests des demi-plans intérieurs du barycentre', 'Côté de l’enveloppe', 'Distance signée',
                         _dots('Marge intérieure', np.arange(1, len(hull) + 1), margins))],
                  _geometry('L’enveloppe se construit à partir des points', 'Les sommets du polygone sont calculés, le barycentre dépend de α.',
                            [_path(hull, 'Enveloppe convexe', 0, True, True)],
                            [_point(q, str(i + 1) if i < 6 else '', 1) for i, q in enumerate(pts)] + [_point(bary, 'Barycentre', 3)],
                            bounds=(-1.6, 2, -1.4, 1.4), hull=hull, cloud=pts, barycenter=bary, weights=weights,
                            margins=margins, area=area),
                  ['Le déterminant de deux directions donne l’orientation ; les chaînes monotones suppriment les tournants vers l’intérieur.',
                   'L’enveloppe convexe est l’ensemble des combinaisons Σλᵢxᵢ, avec λᵢ≥0 et Σλᵢ=1.',
                   'Le point 1 est imposé comme sommet extrême droit. α=1 y concentre tous les poids ; α=0 donne la moyenne uniforme.'],
                  ['La graine rend le nuage reproductible. Les arêtes calculées forment un polygone convexe dans ℝ².',
                   'Les marges peuvent présenter un résidu d’arrondi d’environ 10⁻¹⁵ lorsque le barycentre est exactement sur le bord.'])


def project_polygon(x, vertices):
    x, v = np.asarray(x, float), np.asarray(vertices, float)
    if np.min(halfplane_margins(v, x)) >= 0:
        return x.copy()
    candidates = []
    for a, b in zip(v, np.roll(v, -1, axis=0)):
        edge = b - a
        t = min(1., max(0., float((x - a) @ edge) / float(edge @ edge)))
        candidates.append(a + t * edge)
    return min(candidates, key=lambda q: float(np.sum((x - q) ** 2)))


def boundary_point(vertices, s):
    v = np.asarray(vertices, float)
    edges = np.roll(v, -1, axis=0) - v
    lengths = np.linalg.norm(edges, axis=1)
    position = (float(s) % 1.) * float(lengths.sum())
    for a, edge, length in zip(v, edges, lengths):
        if position <= length:
            return a + position / length * edge
        position -= length
    return v[0].copy()


def projection_convexe(p):
    v = np.array([[-1, -.65], [1, -.65], [1, .65], [-1, .65]]) if p['shape'] == 'rectangle' else np.array([[-1, -.75], [1, -.75], [.1, 1.1]])
    x = np.array([p['x'], p['y']], float)
    q = project_polygon(x, v)
    z = boundary_point(v, p['zeta'])
    variation = (v - q) @ (x - q)
    s = np.linspace(0, 1, 401)
    boundary = np.array([boundary_point(v, a) for a in s])
    inner = (boundary - q) @ (x - q)
    pythagorean = float(np.sum((x - z) ** 2) - np.sum((x - q) ** 2) - np.sum((z - q) ** 2))
    return result([metric('Distance à C', float(np.linalg.norm(x - q))), metric('Abscisse de la projection', float(q[0])),
                   metric('Ordonnée de la projection', float(q[1])), metric('Maximum variationnel sur les sommets', float(variation.max())),
                   metric('Écart dans l’inégalité de Pythagore', pythagorean)],
                  [chart('Le produit scalaire est affine en z', 'Position normalisée sur le bord', '⟨x−p,z−p⟩',
                         series('Produit scalaire calculé', s, inner), series('Borne théorique 0', s, np.zeros_like(s)))],
                  _geometry('Le segment orthogonal atteint le convexe', 'L’unicité vient de la convexité, la projection est calculée sur chaque arête.',
                            [_path(v, 'Convexe C', 0, True, True), _path([x, q], 'Distance minimale', 3), _path([q, z], 'Vecteur z−p', 1)],
                            [_point(x, 'x', 3), _point(q, 'p=projC(x)', 2), _point(z, 'z∈C', 1)],
                            bounds=(-2.8, 2.8, -2.8, 2.8), projection=q, vertices=v,
                            vertex_variations=variation, test_point=z, pythagorean_gap=pythagorean),
                  ['Si x est dans C, sa projection est x. Sinon, minimiser sur chacune des arêtes par un paramètre t tronqué à [0,1].',
                   'p est la projection si et seulement si ⟨x−p,z−p⟩≤0 pour tout z∈C.',
                   'Cette expression est affine en z : sur le polygone, la vérifier aux sommets suffit pour tous les points. Elle donne ‖x−z‖²≥‖x−p‖²+‖z−p‖².'],
                  ['Le théorème concerne ici un convexe fermé non vide d’un espace euclidien ; la métrique est issue du produit scalaire.',
                   'Un maximum variationnel de l’ordre de 10⁻¹⁵ représente un arrondi numérique, pas une violation du théorème.'])


def connexite_chemins(p):
    space = p['space']
    r1, r2, angle = float(p['r1']), float(p['r2']), float(p['angle'])
    a, b = np.array([r1, 0.]), r2 * _unit(angle)
    t = np.linspace(0, 1, 301)
    discs, paths = [], []
    data = {}
    if space in ('punctured', 'annulus'):
        R = max(r1, r2)
        radii = np.concatenate([np.linspace(r1, R, 51), np.full(151, R), np.linspace(R, r2, 51)])
        angles = np.concatenate([np.zeros(51), np.linspace(0, math.radians(angle), 151), np.full(51, math.radians(angle))])
        route = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
        route[0], route[-1] = a, b
        paths = [_path(route, 'Chemin radial et angulaire', 3), _path([a, b], 'Segment direct', 1)]
        if space == 'annulus':
            paths.insert(0, _path(np.vstack([ball_boundary(2, 1.5), ball_boundary(2, .5)[::-1]]), 'Anneau', 0, True, True))
            discs = [_disc([0, 0], 1.5, 'Bord extérieur', 0), _disc([0, 0], .5, 'Bord intérieur', 1)]
        else:
            discs = [_disc([0, 0], .025, '0 exclu', 1, False, False)]
            q = R * _unit(angle / 2)
            two_segments_min = min(segment_min_norm(a, q)[0], segment_min_norm(q, b)[0])
            paths.append(_path([a, q, b], 'Deux segments (exercice 7)', 2))
            data['two_segments'] = dict(vertex=q, minimum_radius=two_segments_min)
        direct_min, _ = segment_min_norm(a, b)
        values = radii
        existence, components = True, 1
        detail = 'La norme sur le chemin reste entre min(r₁,r₂) et max(r₁,r₂). Le trou est donc évité exactement.'
        metric_radius = min(r1, r2)
    elif space == 'disks':
        radius, sep = .65, 1.3 + float(p['gap'])
        a, b = np.array([-sep / 2, 0.]), np.array([sep / 2, 0.])
        discs = [_disc(a, radius, 'Composante gauche', 0, True, True), _disc(b, radius, 'Composante droite', 1, True, True)]
        paths = [_path([a, b], 'Segment interdit dans le vide', 3)]
        segment = (1 - t[:, None]) * a + t[:, None] * b
        values = np.array([disk_union_distance(q, sep, radius)[0] for q in segment])
        direct_min, existence, components, metric_radius = 0., False, 2, 0.
        detail = 'Les deux disques sont séparés par un écart strictement positif. Un chemin continu entre eux produirait des abscisses dans cet écart, par le TVI.'
        data['gap'] = float(p['gap'])
    else:
        a, b = np.array([r1, 0.]), np.array([-r2, 0.])
        paths = [_path([[-2, 0], [0, 0]], 'Composante négative', 0),
                 _path([[0, 0], [2, 0]], 'Composante positive', 1), _path([a, b], 'Passage obligé par 0', 3)]
        discs = [_disc([0, 0], .025, '0 exclu', 2, False, False)]
        values = (1 - t) * r1 - t * r2
        direct_min, existence, components, metric_radius = 0., False, 2, 0.
        detail = 'Un chemin de la demi-droite positive à la demi-droite négative devrait prendre la valeur 0 par le TVI. Ce point a été exclu.'
    points = [_point(a, 'a', 3), _point(b, 'b', 3)]
    axis_label = 'Norme sur le chemin construit' if existence else ('Distance du segment à X' if space == 'disks' else 'Abscisse sur le segment')
    grid = np.linspace(0, 1, len(values))
    return result([metric('Chemin dans X entre a et b', 'Construit' if existence else 'Impossible'),
                   metric('Nombre de composantes de X', components), metric('Rayon minimal du chemin construit', metric_radius),
                   metric('Rayon minimal du segment direct', direct_min)],
                  [chart(axis_label, 'Paramètre de parcours', axis_label, series(axis_label, grid, values))],
                  _geometry('Un trou ne sépare pas toujours l’espace', 'La construction ou l’obstruction est reliée à une preuve explicite.', paths, points, discs,
                            (-2.5, 2.5, -2, 2), path_exists=existence, components=components,
                            endpoints=[a, b], path_minimum_radius=metric_radius, **data),
                  [detail, 'Un ensemble convexe est connexe par arcs ; la réciproque échoue pour l’anneau ou le plan épointé.',
                   'Dans ℝ, les connexes sont les intervalles. Dans ℝ², un obstacle ponctuel peut être contourné.'],
                  ['Les rayons proposés sont strictement positifs et restent dans [1/2,3/2] pour le cas anneau.',
                   'Pour les espaces non connexes, le segment dessiné montre l’obstruction et n’est pas présenté comme un chemin dans X.'])


MODELS = {f.__name__: f for f in (boules_normes, interieur_frontiere, adherence_suite,
          topologie_relative, operations_ouverts, distance_ensemble, convexite,
          enveloppe_convexe, projection_convexe, connexite_chemins)}


def calculate(lab_id, p):
    if lab_id not in MODELS:
        raise ValueError('Laboratoire géométrique inconnu.')
    defaults = {c['key']: c['value'] for item in LABS if item['id'] == lab_id for c in item['controls']}
    defaults.update(p)
    return clean(MODELS[lab_id](defaults))
