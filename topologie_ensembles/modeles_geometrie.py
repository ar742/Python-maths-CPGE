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
    return result([metric('Distance du point à 0, dans la norme choisie', d), metric('Marge entre cette distance et le rayon r', margin),
                   metric('Le point est-il dans la boule ?', 'Oui' if belongs else 'Non'),
                   metric('Rayon d’une petite boule contenue dans la première', max(0., margin))],
                  [chart('Comparer les contours dans une direction donnée', 'Direction depuis 0 (°)', 'Distance euclidienne de 0 au bord', *curves)],
                  _geometry('Placer un point et regarder la place qui reste', 'Chaque contour est calculé avec sa norme. Comparer les formes, puis justifier l’appartenance par l’inégalité correspondante.', paths,
                            [_point([0, 0], 'Centre 0', 4), _point(x, 'Point testé', 3)],
                            bounds=(-extent, extent, -extent, extent), norm=q if q != math.inf else 'inf',
                            margin=margin, membership=bool(belongs)),
                  ['Calculer la norme du point (x,y), puis la comparer à r. L’inégalité stricte signifie que le bord est exclu ; l’inégalité large l’inclut. C’est la définition d’une boule au programme de MP.',
                   'Si m=r−‖(x,y)‖>0, tout point distant de moins de m du point testé reste dans B(0,r), par l’inégalité triangulaire. On a trouvé une petite boule contenue dans l’ensemble : elle constitue un voisinage intérieur.',
                   'Reprendre (0,7 ; 0,7) et r=1 : la norme 1 vaut 1,4, alors que la norme 2 est inférieure à 1. Les boules de même rayon diffèrent. En dimension finie, des rayons adaptés permettent néanmoins de retrouver les mêmes ouverts : c’est l’équivalence des normes en MP.'],
                  ['Les longueurs et le rayon intérieur sont mesurés dans la norme choisie. L’exposant p ne sert que lorsque la norme p est sélectionnée.',
                   'Un rayon affiché égal à 0 ne fournit aucun voisinage intérieur. Le contour suggère la forme ; la formule de la norme décide de l’appartenance.'])


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
    discs.append(_disc(x, p['epsilon'], 'Petit disque autour du point', 3, False, False))
    t = np.linspace(0, 1.25 * r, 251)
    flags = [classify_shape(shape, [z, 0], r) for z in t]
    curves = [series(label, t, [int(a[key]) + offset for a in flags])
              for key, label, offset in [('belongs', 'Appartenance : 0 ou 1', 0), ('interior', 'Intérieur : 1,5 ou 2,5', 1.5),
                                         ('adherent', 'Adhérence : 3 ou 4', 3)]]
    title = 'Intérieur' if info['interior'] else ('Frontière' if info['boundary'] else 'Extérieur de l’adhérence')
    extent = max(2.5, r + .5, max(abs(x)) + p['epsilon'] + .3)
    return result([metric('Position du point par rapport à A', title), metric('Le point appartient-il à A ?', 'Oui' if info['belongs'] else 'Non'),
                   metric('Peut-on approcher le point par des points de A ?', 'Oui' if info['adherent'] else 'Non'), metric('Distance du point au bord de A', info['boundary_distance'])],
                  [chart('Comparer appartenance, intérieur et adhérence sur un rayon', 'Distance ρ du point à 0', 'Courbes décalées : valeur haute = oui', *curves)],
                  _geometry('Réduire un disque autour du point testé', 'Un disque contenu dans A montre un point intérieur. Au bord, tous les petits disques rencontrent A et son complémentaire.', paths,
                            [_point(x, 'Point testé', 3)], discs, (-extent, extent, -extent, extent), classification=info),
                  ['Pour chercher un point intérieur, diminuer ε : peut-on obtenir un petit disque entier dans A ? Il suffit d’un rayon positif. Cette construction traduit x∈Int(A) et la définition d’un voisinage en MP.',
                   'Pour chercher un point adhérent, demander si tous les disques autour du point, aussi petits soient-ils, rencontrent A. Le centre retiré répond oui : on peut l’approcher par des points non nuls du disque, même s’il n’appartient pas à A.',
                   'À la frontière, chaque petit disque rencontre A et des points hors de A. Ainsi Fr(A)=adh(A) privé de Int(A). Pour le disque privé de son centre, la frontière comprend le cercle extérieur et le point 0 ; pour le disque fermé, son cercle appartient à A.'],
                  ['La distance est euclidienne. L’anneau contient ses deux cercles ; le disque épointé est un disque ouvert dont seul le centre a été retiré.',
                   'Le disque de rayon ε illustre un voisinage, mais les critères d’intérieur et d’adhérence portent sur des rayons quantifiés. Les inégalités radiales déterminent les réponses, y compris sur les bords.'])


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
        pts.append(_point([info['nearest'], -.17], 'Point de A le plus proche', 2))
    return result([metric('Distance de x à l’ensemble A', info['distance']), metric('Un point de A atteint-il cette distance ?', 'Oui' if info['attained'] else 'Non'),
                   metric('x est-il un élément de A ?', 'Oui' if info['belongs'] else 'Non'),
                   metric('Rang n donnant 0<1/n<ε', n_witness), metric('A est-il compact dans ℝ ?', 'Oui' if zero else 'Non')],
                  [chart('Comparer la distance à A et la distance au dessin fini', 'Point réel x', 'Distance minimale ou borne inférieure', series('Distance à l’ensemble infini A', grid, exact), series(f'Distance aux {N} points visibles', grid, plotted)),
                   chart('Approcher 0 par des éléments de A', 'Indice entier n', 'Valeur du terme 1/n', _dots('Termes de la suite', np.arange(1, N + 1), seq))],
                  _geometry('Chercher des éléments de A dans un intervalle autour de x', 'Les points 1/n appartiennent tous à A. Leur limite 0 s’ajoute à l’adhérence, qu’elle soit incluse dans A ou non.',
                            [_path([[x - eps, .17], [x + eps, .17]], 'Intervalle ouvert autour de x', 3)], pts, discs,
                            (-.35, 1.35, -.4, .45), infinite_set=True, include_zero=zero, distance=info,
                            witness=dict(n=n_witness, value=1 / n_witness, epsilon=eps)),
                  ['En MPSI, la suite 1/n converge vers 0. Pour un ε>0 donné, choisir n>1/ε place son terme dans ]0,ε[ : chaque voisinage de 0 rencontre A. On retrouve ainsi la caractérisation séquentielle de l’adhérence en MP.',
                   'Sans ajouter 0, d(0,A)=0 mais aucun élément de A ne réalise cette distance. Pour x≤0, d(x,A)=−x ; pour 0<x≤1, comparer les termes qui encadrent x, et pour x≥1 retenir le point 1. La borne inférieure et le minimum ne sont donc pas interchangeables.',
                   'Tester 1/4 : un petit intervalle l’isole des autres points de A. Tester ensuite 0 : aucun intervalle ne l’isole des termes 1/n. Ajouter cette limite rend A fermé ; comme il est aussi borné dans ℝ, le critère de MP le rend compact.'],
                  ['A contient les 1/n pour tous les entiers n≥1, même si seuls N termes sont visibles. La distance à A utilise cet ensemble infini.',
                   'Le rang affiché pour 0<1/n<ε sert à étudier le voisinage de 0. L’adhérence reste {1/n : n≥1}∪{0} ; ajouter 0 change l’appartenance et la fermeture, pas cette adhérence.'])


def topologie_relative(p):
    b, x, eps = float(p['b']), float(p['x']), float(p['epsilon'])
    belongs = x < b
    ambient = 0 < x < min(1., b)
    contains = belongs and (b > 1 or x + eps <= b)
    right = min(1., b)
    paths = [_path([[0, 0], [1, 0]], 'Espace de travail X=[0,1]', 0),
             _path([[0, .14], [right, .14]], 'Points de l’intervalle qui restent dans X', 1),
             _path([[max(0., x - eps), -.14], [min(1., x + eps), -.14]], 'Voisinage limité à X', 3)]
    discs = [_disc([0, .14], .012, '0 inclus dans A', 1, True, True),
             _disc([right, .14], .012, 'Bord droit', 1, b > 1, b > 1)]
    grid = np.linspace(0, 1, 401)
    return result([metric('x est-il intérieur à A dans X ?', 'Oui' if belongs else 'Non'),
                   metric('x est-il intérieur à A dans ℝ ?', 'Oui' if ambient else 'Non'),
                   metric('Le voisinage choisi reste-t-il dans A ?', 'Oui' if contains else 'Non'),
                   metric('Rayon sûr d’un voisinage relatif, si x∈A', max(0., (b - x) / 2))],
                  [chart('Comparer l’intérieur de A dans X et dans ℝ', 'Point x de [0,1]', 'Courbes décalées : valeur haute = oui',
                         series('Intérieur dans X : 0 ou 1', grid, (grid < b).astype(int)),
                         series('Intérieur dans ℝ : 1,5 ou 2,5', grid, ((grid > 0) & (grid < min(1., b))).astype(int) + 1.5))],
                  _geometry('Ne garder du voisinage que ses points dans X', 'Comparer les trois lignes : l’espace X, l’ensemble A et le voisinage autour de x. Le décalage vertical facilite la lecture des bords.', paths,
                            [_point([x, -.14], 'x', 3)], discs, (-.25, 1.5, -.4, .45),
                            relative_interior=belongs, ambient_interior=ambient, neighborhood_inside=contains),
                  ['Commencer par annoncer l’espace : dans X=[0,1], un voisinage de x ne contient que les points de X proches de x. On prend donc l’intervalle ]x−ε,x+ε[, puis son intersection avec X. C’est la notion de voisinage relatif en MP.',
                   'A est obtenu de la même façon : A=X∩]−1/2,b[. L’intervalle est ouvert dans ℝ, donc sa restriction est un ouvert relatif de X. Autour de 0, il suffit que ε<b pour que [0,ε[ reste dans A.',
                   'Pour un point x<b, ε=(b−x)/2 fournit un voisinage relatif contenu dans A. Dans ℝ, chaque intervalle autour de 0 contient des réels négatifs, hors de A : 0 n’y est pas intérieur. Si b>1, A devient tout X, ouvert et fermé dans lui-même.'],
                  ['Le point testé est toujours dans X=[0,1]. Les lignes représentent des parties de la droite réelle et sont seulement décalées pour les comparer.',
                   'La borne b n’appartient jamais à ]−1/2,b[. Le point 1 appartient à A uniquement pour b>1 ; préciser l’espace est indispensable pour les conclusions sur l’intérieur.'])


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
    return result([metric('x reste-t-il après les N premiers intervalles ?', 'Oui' if finite else 'Non'),
                   metric('x reste-t-il pour la famille entière ?', 'Oui' if infinite else 'Non'),
                   metric('Ensemble obtenu avec N intervalles', f']−1/{N},1/{N}[' if intersection else f'[1/{N},1]'),
                   metric('Ensemble obtenu avec tous les intervalles', '{0}, non ouvert' if intersection else ']0,1], non fermé')],
                  [chart('Suivre la borne 1/n qui se rapproche de 0', 'Indice entier n', 'Position de la borne', series('Borne 1/n', ngrid, 1 / ngrid)),
                   chart('Tester x après chaque opération finie', 'Nombre n d’intervalles retenus', '1 : x appartient ; 0 : x est absent', series('Appartenance au résultat fini', ngrid, fflags.astype(int)))],
                  _geometry('Comparer quelques intervalles de la famille', 'Les petits cercles signalent les extrémités : vides pour les ouverts, pleins pour les fermés. Chercher les points communs ou réunir les segments selon le cas choisi.', paths,
                            [_point([x, -.2], 'Point x', 3), _point([0, -.2], '0', 1)], discs,
                            (-1.3, 1.3, -.4, .2 * len(ns) + .2), finite_membership=bool(finite),
                            infinite_membership=bool(infinite), finite_limit_radius=1 / N),
                  ['Pour l’intersection, garder les points qui satisfont toutes les contraintes retenues. Après N étapes, il reste ]−1/N,1/N[. On peut encore entourer 0 d’un intervalle ouvert contenu dans cet ensemble ; pour tous les n à la fois, seul 0 reste et aucun rayon positif ne convient.',
                   'Pour la réunion, il suffit d’appartenir à un des segments [1/n,1]. Chaque x>0 jusqu’à 1 finit par y figurer, mais 0 ne figure jamais. La suite 1/n converge pourtant vers 0 : la caractérisation séquentielle de MP montre que la réunion ]0,1] n’est pas fermée.',
                   'Retenir les quatre propriétés de MP : réunion quelconque d’ouverts et intersection finie d’ouverts ; intersection quelconque de fermés et réunion finie de fermés. Dans une intersection finie d’ouverts, le minimum des rayons autour d’un point reste positif ; l’exemple infini explique pourquoi le mot « finie » compte.'],
                  ['N fixe une opération finie. L’opération sur tous les n≥1 est déterminée séparément par le raisonnement, même pour un grand N.',
                   'Les intervalles ]−1/n,1/n[ excluent leurs extrémités ; les segments [1/n,1] les incluent. Tous les mots ouvert et fermé se rapportent ici à ℝ.'])


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
    return result([metric('Distance du point à A', d), metric('Points de A réalisant cette distance', len(projections)),
                   metric('Peut-on relier tous les points dans A ?', 'Oui' if sep <= 2 * r else 'Non'),
                   metric('Tous les segments entre points de A restent-ils dans A ?', 'Oui' if sep == 0 else 'Non')],
                  [chart('Déplacer le point horizontalement et suivre sa distance à A', 'Abscisse u, avec la même ordonnée y', 'Distance d((u,y),A)', series('Distance à la réunion des disques', grid, dist)),
                   chart('Comparer variation de distance et déplacement', 'Abscisse u', 'Variation de distance / déplacement',
                         series('Quotient pour deux points voisins du dessin', (grid[1:] + grid[:-1]) / 2, abs(np.diff(dist) / np.diff(grid))),
                         series('Limite garantie : 1', grid, np.ones_like(grid)))],
                  _geometry('Chercher le ou les trajets les plus courts vers A', 'Les segments relient le point testé à tous ses points les plus proches dans A. La distance est unique, même quand ces points sont deux.', paths, points,
                            [_disc(c, r, f'Disque {i + 1}', i, True, True) for i, c in enumerate(centers)],
                            (-3.6, 3.6, -2.8, 2.8), projections=projections, distance=d, distance_to_disks=ds),
                  ['Pour atteindre un disque D(c,r) depuis l’extérieur, aller vers son centre puis s’arrêter sur le cercle. Il reste la longueur ‖x−c‖−r ; si x est déjà dans le disque, la distance vaut 0. Ainsi d(x,D)=max(‖x−c‖−r,0).',
                   'Pour atteindre la réunion A, comparer les deux trajets et choisir la plus petite longueur. Sur la médiatrice de disques séparés, les deux trajets sont aussi courts : deux points réalisent le minimum. Ce cas aide à distinguer distance et point projeté.',
                   'Déplacer le point d’une longueur δ ne peut faire varier sa distance à A de plus de δ, par l’inégalité triangulaire : |d(P,A)−d(Q,A)|≤‖P−Q‖. C’est la propriété 1-lipschitzienne de MP. L’unicité de la projection sur un ensemble général demande des hypothèses supplémentaires, contrairement à la projection orthogonale sur un sous-espace étudiée en MPSI.'],
                  ['A est la réunion de deux disques fermés non vides de même rayon ; les distances sont euclidiennes. Leur fermeture en dimension finie garantit que le minimum est atteint.',
                   'Les quotients sur la courbe illustrent la borne 1. Sa justification vaut pour tous les points et vient de l’inégalité triangulaire, indépendamment du tracé.'])


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
        criterion = 'Parcourir le segment par z(t)=(1−t)a+tb. Pour chaque disque, résoudre ‖z(t)−c‖²≤r² donne les valeurs de t admises. Le segment entier reste dans la réunion si ces deux intervalles couvrent [0,1], sans laisser de passage hors des disques.'
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
        criterion = 'Parcourir le segment par z(t)=(1−t)a+tb. La norme ne dépasse pas la plus grande des normes des extrémités. Pour l’anneau, il faut aussi éviter le trou : minimiser la fonction quadratique ‖z(t)‖² et vérifier que son minimum correspond à un rayon au moins égal à 1/2.'
    minimum, t_min = segment_min_norm(a, b)
    t = np.linspace(0, 1, 301)
    z = (1 - t[:, None]) * a + t[:, None] * b
    paths += [_path([a, b], 'Segment [a,b]', 3)]
    points = [_point(a, 'a', 3), _point(b, 'b', 3), _point((1 - t_min) * a + t_min * b, 'Point le plus proche de 0', 2)]
    if not global_convex:
        mid = (witness_a + witness_b) / 2
        paths.append(_path([witness_a, witness_b], 'Un segment qui sort de A', 1))
        points += [_point(witness_a, 'u', 1), _point(witness_b, 'v', 1), _point(mid, 'Milieu hors de A', 1)]
    else:
        mid = (a + b) / 2
    return result([metric('Le segment choisi reste-t-il entièrement dans A ?', 'Oui' if valid else 'Non'),
                   metric('A est-il convexe ?', 'Oui' if global_convex else 'Non'), metric('Plus petite distance du segment à 0', minimum),
                   metric('Distance à A du milieu du segment témoin', float(distance(mid)))],
                  [chart('Repérer les endroits où le segment sort de A', 'Paramètre t : de a en 0 à b en 1', 'Distance du point z(t) à A', series('Distance : positive hors de A', t, [distance(q) for q in z]))],
                  _geometry('Relier deux points, puis chercher un contre-exemple', 'Le premier segment dépend des points choisis. Quand A n’est pas convexe, un autre segment fournit un milieu hors de A et démontre cette non-convexité.', paths, points, discs,
                            (-3, 3, -1.7, 1.7), segment_contained=bool(valid), global_convex=global_convex,
                            endpoints=[a, b], witness_endpoints=[witness_a, witness_b], witness_midpoint=mid),
                  [criterion, 'La définition de MP demande que tout segment entre deux points de A reste dans A. Le disque la vérifie pour toutes les paires, grâce à l’inégalité triangulaire. Réussir avec la seule paire choisie ne suffit donc pas à conclure pour l’ensemble.',
                   'Pour réfuter la convexité, une seule paire suffit. Dans l’anneau, prendre deux points opposés : leur milieu 0 manque A. Pour deux disques distincts de même rayon, prendre leurs points supérieurs : le milieu est au-dessus du passage entre les disques et hors de chacun.'],
                  ['Les angles a et b placent les points autour de leur centre. ρ règle la fraction du rayon extérieur utilisée ; les points choisis sont toujours dans A.',
                   'Les calculs de minima et d’intervalles décident pour tout le segment. Le graphe aide à repérer la sortie, mais ses points dessinés ne remplacent pas le raisonnement.'])


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
    return result([metric('Sommets nécessaires pour tracer le bord', len(hull)), metric('Aire du polygone convexe', area),
                   metric('Somme des poids du barycentre', float(weights.sum())), metric('Distance intérieure minimale du barycentre aux côtés', float(margins.min()))],
                  [chart('Vérifier les poids du barycentre', 'Numéro i du point', 'Poids λᵢ, non négatif', stems),
                   chart('Vérifier que le barycentre est du bon côté de chaque bord', 'Numéro du côté du polygone', 'Distance signée : positive vers l’intérieur',
                         _dots('Distance vers l’intérieur', np.arange(1, len(hull) + 1), margins))],
                  _geometry('Entourer le nuage et déplacer son barycentre', 'Le bord utilise les sommets extérieurs du nuage. Le point barycentre utilise tous les poids, que l’on modifie avec α.',
                            [_path(hull, 'Enveloppe convexe', 0, True, True)],
                            [_point(q, str(i + 1) if i < 6 else '', 1) for i, q in enumerate(pts)] + [_point(bary, 'Barycentre', 3)],
                            bounds=(-1.6, 2, -1.4, 1.4), hull=hull, cloud=pts, barycenter=bary, weights=weights,
                            margins=margins, area=area),
                  ['Partir du point le plus à gauche et chercher les bords inférieurs, puis supérieurs. Le signe d’un déterminant de deux directions indique dans quel sens on tourne ; l’algorithme écarte les points qui ne sont pas nécessaires au bord. C’est une application géométrique du déterminant.',
                   'Former un barycentre Σλᵢxᵢ avec des poids λᵢ≥0 et de somme 1. Il reste dans tout convexe contenant les points. L’ensemble de ces barycentres est donc le plus petit convexe qui les contient : l’enveloppe convexe, étudiée ici comme prolongement du calcul vectoriel de MPSI et de la convexité en MP.',
                   'Le point 1 est le sommet le plus à droite. Le réglage réserve une part α à ce point et partage 1−α également entre tous les points. À α=0, on obtient leur moyenne ; à α=1, le barycentre est le point 1. Comparer les poids et la position pour justifier qu’il ne sort pas du polygone.'],
                  ['Le numéro du nuage reproduit les mêmes coordonnées. L’enveloppe est celle des N points présents, et non celle de tous les nuages possibles.',
                   'La distance signée à un côté est positive vers l’intérieur, nulle sur ce côté. Un résidu d’environ 10⁻¹⁵ au bord vient de l’arrondi ; les poids non négatifs et de somme 1 donnent la justification mathématique.'])


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
    return result([metric('Distance du point à C', float(np.linalg.norm(x - q))), metric('Abscisse du point le plus proche p', float(q[0])),
                   metric('Ordonnée du point le plus proche p', float(q[1])), metric('Plus grand produit scalaire aux sommets', float(variation.max())),
                   metric('Différence ‖x−z‖²−‖x−p‖²−‖z−p‖²', pythagorean)],
                  [chart('Vérifier l’angle entre x−p et les directions de C', 'Fraction du tour du bord parcourue par z', 'Produit scalaire ⟨x−p,z−p⟩',
                         series('Produit scalaire le long du bord', s, inner), series('Il doit rester inférieur ou égal à 0', s, np.zeros_like(s)))],
                  _geometry('Trouver le point de C qui réalise la distance', 'Le point p minimise la distance. Le point z permet de vérifier qu’aucune direction de p vers C ne rapproche de x au premier ordre.',
                            [_path(v, 'Ensemble convexe C', 0, True, True), _path([x, q], 'Trajet le plus court', 3), _path([q, z], 'Direction de p vers z', 1)],
                            [_point(x, 'Point x', 3), _point(q, 'Point le plus proche p', 2), _point(z, 'Point z sur le bord', 1)],
                            bounds=(-2.8, 2.8, -2.8, 2.8), projection=q, vertices=v,
                            vertex_variations=variation, test_point=z, pythagorean_gap=pythagorean),
                  ['Si le point x est déjà dans C, la distance est nulle et p=x. Sinon, chercher le point le plus proche sur chaque côté. La projection sur la droite portant ce côté se calcule avec le produit scalaire, comme en MPSI ; si elle dépasse le segment, retenir une de ses extrémités.',
                   'Depuis le point candidat p, prendre une direction vers un point z de C. La condition ⟨x−p,z−p⟩≤0 signifie que cette direction ne rapproche pas de x au premier ordre. Pour un polygone, il suffit de la vérifier aux sommets : tout point de C est une combinaison convexe de ces sommets.',
                   'Développer le carré de la distance donne ‖x−z‖²≥‖x−p‖²+‖z−p‖². Le point p réalise donc le minimum, et tout autre point donne une distance plus grande. Cette projection sur un convexe fermé est un prolongement distinct de la projection orthogonale sur un sous-espace au programme de MPSI.'],
                  ['Le résultat utilise le produit scalaire euclidien et un convexe fermé non vide. Ces hypothèses garantissent l’existence et l’unicité du point le plus proche.',
                   'ζ repère la fraction du tour du bord parcourue par z ; ζ=0 et ζ=1 donnent le même sommet de départ. Un produit scalaire positif d’environ 10⁻¹⁵ peut venir de l’arrondi : la caractérisation mathématique porte sur la valeur non positive.'])


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
        detail = 'Partir du premier point en suivant son rayon jusqu’au cercle de rayon max(r₁,r₂), parcourir ce cercle, puis rejoindre le second point sur son rayon. La distance à 0 reste entre min(r₁,r₂) et max(r₁,r₂) : le chemin évite 0 et reste aussi dans l’anneau lorsque ce cas est choisi.'
        metric_radius = min(r1, r2)
    elif space == 'disks':
        radius, sep = .65, 1.3 + float(p['gap'])
        a, b = np.array([-sep / 2, 0.]), np.array([sep / 2, 0.])
        discs = [_disc(a, radius, 'Composante gauche', 0, True, True), _disc(b, radius, 'Composante droite', 1, True, True)]
        paths = [_path([a, b], 'Segment qui quitte les disques', 3)]
        segment = (1 - t[:, None]) * a + t[:, None] * b
        values = np.array([disk_union_distance(q, sep, radius)[0] for q in segment])
        direct_min, existence, components, metric_radius = 0., False, 2, 0.
        detail = 'Les points a et b sont ici les centres des deux disques. Pour passer d’un disque à l’autre, l’abscisse d’un chemin continu devrait prendre une valeur dans l’écart vide entre eux, par le TVI de MPSI. Aucun point de X n’a cette abscisse : ce chemin est impossible.'
        data['gap'] = float(p['gap'])
    else:
        a, b = np.array([r1, 0.]), np.array([-r2, 0.])
        paths = [_path([[-2, 0], [0, 0]], 'Composante négative', 0),
                 _path([[0, 0], [2, 0]], 'Composante positive', 1), _path([a, b], 'Passage obligé par 0', 3)]
        discs = [_disc([0, 0], .025, '0 exclu', 2, False, False)]
        values = (1 - t) * r1 - t * r2
        direct_min, existence, components, metric_radius = 0., False, 2, 0.
        detail = 'Les points choisis sont d’un côté et de l’autre de 0 sur la droite. Tout chemin continu entre eux devrait prendre la valeur 0, par le TVI de MPSI. Comme 0 a été retiré, le chemin ne pourrait pas rester dans X.'
    points = [_point(a, 'a', 3), _point(b, 'b', 3)]
    axis_label = 'Distance à 0 le long du chemin construit' if existence else ('Distance à X le long du segment essayé' if space == 'disks' else 'Abscisse le long du segment essayé')
    grid = np.linspace(0, 1, len(values))
    return result([metric('Peut-on relier a et b sans quitter X ?', 'Construit' if existence else 'Impossible'),
                   metric('Nombre de composantes connexes par arcs', components), metric('Plus petite distance du chemin construit à 0', metric_radius),
                   metric('Plus petite distance du segment direct à 0', direct_min)],
                  [chart(axis_label, 'Fraction du parcours effectuée', axis_label, series(axis_label, grid, values))],
                  _geometry('Essayer un segment, puis construire un détour', 'Le détour est un chemin dans X quand il existe. Dans les deux cas séparés, le segment dessiné sert à expliquer pourquoi aucun chemin dans X ne peut relier a à b.', paths, points, discs,
                            (-2.5, 2.5, -2, 2), path_exists=existence, components=components,
                            endpoints=[a, b], path_minimum_radius=metric_radius, **data),
                  [detail, 'En MP, X est connexe par arcs si toute paire de points peut être reliée par un chemin continu qui reste dans X. Un convexe a cette propriété grâce aux segments. L’anneau montre que la réciproque est fausse : des détours existent alors que certains segments passent dans le trou.',
                   'Les points que l’on peut relier entre eux constituent une composante connexe par arcs. La droite privée de 0 en a deux, ses deux demi-droites ; le plan privé de 0 n’en a qu’une. La construction par deux segments dans le plan reprend aussi l’exercice 7 du recueil.'],
                  ['Dans le plan et l’anneau, l’angle donne la direction du second point ; r₁ et r₂ sont les distances des deux points à 0. Dans la droite, ces distances placent les points de signes opposés. Dans le cas des disques, seul l’écart gap change leur séparation.',
                   'Les rayons du chemin construit sont strictement positifs et restent dans [1/2,3/2] pour l’anneau. Quand le chemin est impossible, le rayon minimal affiché comme 0 ne décrit aucun chemin construit : le segment essayé montre l’obstacle.'])


MODELS = {f.__name__: f for f in (boules_normes, interieur_frontiere, adherence_suite,
          topologie_relative, operations_ouverts, distance_ensemble, convexite,
          enveloppe_convexe, projection_convexe, connexite_chemins)}


def calculate(lab_id, p):
    if lab_id not in MODELS:
        raise ValueError('Laboratoire géométrique inconnu.')
    defaults = {c['key']: c['value'] for item in LABS if item['id'] == lab_id for c in item['controls']}
    defaults.update(p)
    return clean(MODELS[lab_id](defaults))
