"""Identités analytiques et quadratures indépendantes, sans SciPy."""
from __future__ import annotations
import functools
import math
import numpy as np
from commun import metric, series, chart, result, integrate


@functools.lru_cache(maxsize=8)
def gauss_unit(n=256):
    x, w = np.polynomial.legendre.leggauss(n)
    return (x + 1) / 2, w / 2


def gauss_integral(func, lo, hi, n=256):
    if hi == lo:
        return 0.0
    u, w = gauss_unit(n)
    return float((hi - lo) * np.dot(w, func(lo + (hi - lo) * u)))


def gamma_quadrature(x, cutoff=45, n=256):
    """t=v^q supprime la singularité en 0 lorsque 0<x<1."""
    q = max(1.0, 4 / x)
    return gauss_integral(lambda v: q * v ** (q * x - 1) * np.exp(-v ** q), 0, cutoff ** (1 / q), n)


def beta_value(a, b):
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def beta_quadrature(a, b, n=256):
    """Deux substitutions annulent séparément les singularités aux extrémités."""
    u, w = gauss_unit(n)
    qa, qb = max(1.0, 4 / a), max(1.0, 4 / b)
    left = (.5 ** a * qa) * np.dot(w, u ** (qa * a - 1) * (1 - .5 * u ** qa) ** (b - 1))
    right = (.5 ** b * qb) * np.dot(w, u ** (qb * b - 1) * (1 - .5 * u ** qb) ** (a - 1))
    return float(left + right)


def zeta_value(s):
    """Euler–Maclaurin sur une queue, valable ici pour 1<s≤6."""
    M = 40
    value = math.fsum(n ** (-s) for n in range(1, M + 1))
    value += M ** (1 - s) / (s - 1) - .5 * M ** (-s)
    bernoulli = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730]
    for k, B in enumerate(bernoulli, 1):
        rising = math.prod(s + j for j in range(2 * k - 1))
        value += B / math.factorial(2 * k) * rising * M ** (-s - 2 * k + 1)
    return value


def planck_quadrature(s, cutoff, n=256):
    q = max(1.0, 4 / (s - 1))
    def transformed(v):
        t = v ** q
        return q * v ** (q * (s - 1) - 1) * t / np.expm1(t)
    return gauss_integral(transformed, 0, cutoff ** (1 / q), n)


def curves_scene(title, x, curves, x_label, y_label, description):
    return dict(kind='curves', title=title, x=x, curves=[dict(label=label, y=y) for label, y in curves],
                xLabel=x_label, yLabel=y_label, description=description)


def gamma_euler(p):
    x, T = p['x'], p['cutoff']
    reference = math.gamma(x)
    quadrature = gamma_quadrature(x, T)
    t = np.linspace(.004, max(12, T), 601)
    density = t ** (x - 1) * np.exp(-t)
    grid = np.linspace(.2, 8, 301)
    gamma_values = np.array([math.gamma(z) for z in grid])
    cutoffs = np.linspace(.02, max(35, T), 160)
    cumulative = np.array([gamma_quadrature(x, z) for z in cutoffs])
    return result(
        [metric('Γ(x), référence de la bibliothèque', reference), metric('Intégrale calculée de 0 à T', quadrature),
         metric('Part de l’intégrale retenue', quadrature / reference, 'fraction'), metric('Γ(x+1)/(xΓ(x))', math.gamma(x + 1) / (x * reference)),
         metric('Masse de la queue, référence moins quadrature', max(0, reference - quadrature)),
         metric('Position du maximum intérieur du noyau', x - 1 if x > 1 else 'Aucun : noyau décroissant sur ]0,+∞[', 't' if x > 1 else '')],
        [chart('Le noyau définit une intégrale, même quand il est singulier en 0', 't>0', 't^(x−1)e^(−t)', series('Noyau pour x choisi', t, density), xMarker=T, xMarkerLabel='Troncature T'),
         chart('Gamma prolonge la factorielle sur les réels positifs', 'Argument z>0', 'Γ(z)', series('Γ(z)', grid, gamma_values), y_scale='log'),
         chart('Une intégrale impropre : suivre la limite des intégrales tronquées', 'Borne supérieure', 'Intégrale de 0 à cette borne', series('Quadrature', cutoffs, cumulative), series('Γ(x)', cutoffs, np.full_like(cutoffs, reference)))],
        curves_scene('Où se trouve l’aire qui définit Γ(x) ?', t, [('t^(x−1)e^(−t)', density)], 't', 'Valeur du noyau', 'Le dessin commence à t=0,004. Une valeur infinie au point 0 pour x<1 n’interdit pas une aire finie. La quadrature traite le voisinage de 0 par changement de variable.'),
        ['Près de 0, le noyau est équivalent à t^(x−1) : son intégrale converge exactement lorsque x>0. À l’infini, l’exponentielle assure la convergence.',
         'Intégrer par parties sur [ε,T] puis faire tendre ε vers 0 et T vers l’infini : Γ(x+1)=xΓ(x). Les termes de bord tendent vers 0 pour x>0.',
         'Γ(1)=1 donne Γ(n)=(n−1)! ; le changement t=u² et l’intégrale gaussienne donnent Γ(1/2)=√π.',
         'La quadrature utilise t=v^q, q=max(1,4/x), pour rendre le noyau transformé régulier. Elle évalue une intégrale tronquée ; la valeur de math.gamma ne sert pas à fabriquer cette intégrale.'],
        ['Paramètres réels x>0 ; aucun prolongement complexe ni pôle négatif dans ce laboratoire.', 'L’erreur affichée entre l’intégrale tronquée et Γ(x) combine la queue négligée et l’arrondi de la quadrature ; elle n’est pas un certificat numérique de précision.'])


def beta_geometrie(p):
    a, b = p['a'], p['b']
    B = beta_value(a, b)
    numerical = beta_quadrature(a, b)
    t = np.linspace(.002, .998, 601)
    density = t ** (a - 1) * (1 - t) ** (b - 1) / B
    mirrored = t ** (b - 1) * (1 - t) ** (a - 1) / B
    grid = np.linspace(.35, 7, 301)
    vals = np.array([beta_value(z, b) for z in grid])
    r = np.linspace(.005, 20, 501)
    radial = r ** (a + b - 1) * np.exp(-r) / math.gamma(a + b)
    return result(
        [metric('B(a,b) par Γ(a)Γ(b)/Γ(a+b)', B), metric('B(a,b) par quadrature', numerical),
         metric('Écart relatif de la quadrature', abs(numerical - B) / B), metric('Moyenne de la densité', a / (a + b)),
         metric('Variance de la densité', a * b / ((a + b) ** 2 * (a + b + 1))), metric('B(a,b+1)/B(a,b)', beta_value(a, b + 1) / B)],
        [chart('Changer les paramètres déplace ou concentre la masse', 't∈]0,1[', 'Densité normalisée', series('Paramètres (a,b)', t, density), series('Paramètres (b,a)', t, mirrored)),
         chart('À b fixé, la fonction bêta varie avec a', 'a>0', 'B(a,b)', series('B(a,b choisi)', grid, vals), y_scale='log'),
         chart('Dans le changement (u,v)=(rt,r(1−t)), le facteur radial est gamma', 'r>0', 'r^(a+b−1)e^(−r)/Γ(a+b)', series('Facteur radial normalisé', r, radial))],
        curves_scene('La symétrie de B devient une réflexion du graphique', t, [('Densité (a,b)', density), ('Densité (b,a)', mirrored)], 't', 'Densité', 'Le remplacement t↦1−t échange a et b. Les extrémités singulières sont intégrables pour a,b>0 ; elles ne sont pas dessinées comme des valeurs finies.'),
        ['L’intégrabilité aux deux extrémités exige a>0 et b>0. Le changement t↦1−t démontre B(a,b)=B(b,a).',
         'Dans Γ(a)Γ(b), poser r=u+v et t=u/(u+v). Alors u=rt, v=r(1−t) et |∂(u,v)/∂(r,t)|=r.',
         'Le produit se factorise en Γ(a+b)B(a,b). Pour une densité normalisée, les moments se calculent en augmentant a : E(t)=B(a+1,b)/B(a,b).',
         'La relation Γ(z+1)=zΓ(z) donne B(a,b+1)=bB(a,b)/(a+b) et la variance ab/[(a+b)²(a+b+1)].'],
        ['a et b sont réels strictement positifs. La densité est un lien avec les probabilités ; la construction de B repose sur l’analyse des intégrales.', 'La quadrature découpe [0,1] en deux puis retire les singularités avec deux substitutions différentes. Le tracé seul ne permet pas de vérifier la normalisation.'])


def zeta_series(p):
    s, N = p['s'], int(p['N'])
    n = np.arange(1, N + 1, dtype=float)
    partial = np.cumsum(n ** (-s))
    reference = zeta_value(s)
    lower = (n + 1) ** (1 - s) / (s - 1)
    upper = n ** (1 - s) / (s - 1)
    points = np.unique(np.linspace(0, N - 1, min(N, 601)).astype(int))
    values = np.linspace(1.1, 6, 240)
    return result(
        [metric('Somme des N premiers termes', partial[-1]), metric('ζ(s), référence Euler–Maclaurin', reference),
         metric('Borne inférieure du reste', lower[-1]), metric('Borne supérieure du reste', upper[-1]),
         metric('Largeur de l’encadrement de ζ(s)', upper[-1] - lower[-1]), metric('Part de ζ(s) déjà sommée', partial[-1] / reference, 'fraction')],
        [chart('Additionner des termes puis encadrer ce qui manque', 'N', 'Valeur', series('Somme partielle S_N', n[points], partial[points]), series('S_N + borne inférieure', n[points], (partial + lower)[points]), series('S_N + borne supérieure', n[points], (partial + upper)[points]), series('Référence ζ(s)', n[points], np.full(len(points), reference))),
         chart('Le reste : une convergence beaucoup plus lente près de s=1', 'N', 'Reste et majoration', series('ζ(s)−S_N', n[points], (reference - partial)[points]), series('Majorant N^(1−s)/(s−1)', n[points], upper[points]), y_scale='log'),
         chart('Le bord s=1 n’appartient pas au domaine de convergence', 's>1', 'ζ(s)', series('ζ(s)', values, [zeta_value(z) for z in values]), series('1/(s−1)', values, 1 / (values - 1)))],
        curves_scene('Le reste complète la somme partielle', n[points], [('S_N', partial[points]), ('S_N + reste minimal', (partial + lower)[points]), ('S_N + reste maximal', (partial + upper)[points])], 'N', 'Valeur', 'La vraie limite est comprise entre les deux courbes corrigées pour chaque N. Une somme qui varie peu peut encore être loin de sa limite.'),
        ['Pour s>1, t↦t^(−s) est positive et décroissante. Comparer chaque terme à l’aire d’un rectangle fournit ∫_(N+1)^∞t^(−s)dt≤R_N≤∫_N^∞t^(−s)dt.',
         'Ainsi (N+1)^(1−s)/(s−1)≤ζ(s)−S_N≤N^(1−s)/(s−1). L’encadrement reste valable même quand N est petit.',
         'Sur s≥1+δ, n^(−s)≤n^(−1−δ). La série majorante convergente donne la convergence normale et donc uniforme ; ζ y est continue.',
         'À s fixé, doubler N multiplie approximativement le reste par 2^(1−s). Pour s=1,1, ce facteur est proche de 0,933 : doubler le travail apporte peu.'],
        ['Domaine réel s>1. Le prolongement de ζ ailleurs et ses zéros complexes ne sont pas utilisés.', 'La référence Euler–Maclaurin est une approximation en double précision. L’encadrement par les intégrales est l’argument mathématique indépendant.'])


def zeta_integrale(p):
    s, T = p['s'], p['cutoff']
    reference = math.gamma(s) * zeta_value(s)
    numerical = planck_quadrature(s, T)
    t = np.linspace(.004, max(15, T), 601)
    kernel = t ** (s - 1) / np.expm1(t)
    cutoffs = np.linspace(.02, max(30, T), 160)
    cumulative = np.array([planck_quadrature(s, z) for z in cutoffs])
    powers = t ** (s - 2)
    return result(
        [metric('Γ(s)ζ(s), référence', reference), metric('Intégrale de 0 à T calculée', numerical),
         metric('ζ(s) retrouvée à partir de l’intégrale tronquée', numerical / math.gamma(s)),
         metric('Part de l’intégrale complète retenue', numerical / reference, 'fraction'),
         metric('Exposant du noyau au voisinage de 0 : s−2', s - 2), metric('Queue : référence moins quadrature', max(0, reference - numerical))],
        [chart('Noyau de l’intégrale et équivalent près de 0', 't>0', 'Valeur positive', series('t^(s−1)/(eᵗ−1)', t, kernel), series('t^(s−2)', t, powers), y_scale='log'),
         chart('L’intégrale tronquée approche Γ(s)ζ(s)', 'Borne supérieure', 'Intégrale', series('Quadrature de 0 à la borne', cutoffs, cumulative), series('Γ(s)ζ(s)', cutoffs, np.full_like(cutoffs, reference))),
         chart('Le développement géométrique au cœur de la preuve', 't>0', '1/(eᵗ−1)', series('Fonction exacte', t, 1 / np.expm1(t)), series('Somme de 20 exponentielles', t, sum(np.exp(-k * t) for k in range(1, 21))), y_scale='log')],
        curves_scene('L’aire du noyau vaut Γ(s)ζ(s)', t, [('t^(s−1)/(eᵗ−1)', kernel)], 't', 'Valeur du noyau', 'La condition s>1 vient du comportement au voisinage de 0. Pour s=4, cette intégrale est π⁴/15 et fournit une constante du rayonnement thermique.'),
        ['Pour t>0, la série géométrique donne 1/(eᵗ−1)=Σ_(n≥1)e^(−nt). Tous les termes sont positifs ; l’interversion série–intégrale est justifiée par convergence monotone.',
         'Le changement u=nt dans ∫₀^∞t^(s−1)e^(−nt)dt donne Γ(s)/n^s. La somme est Γ(s)ζ(s).',
         'Comme eᵗ−1∼t en 0, le noyau est équivalent à t^(s−2) et intégrable exactement pour s>1. À l’infini, la décroissance exponentielle suffit.',
         'Pour s=4, Γ(4)=6 et ζ(4)=π⁴/90 : l’intégrale vaut π⁴/15. Dans ∫ω³/(exp(ℏω/kT_phys)−1)dω, poser t=ℏω/(kT_phys) fait sortir (kT_phys/ℏ)⁴.'],
        ['La variable T du curseur est une borne sans dimension, distincte de la température physique T_phys.', 'L’application au rayonnement est un prolongement interdisciplinaire. La quadrature supprime la singularité de 0 ; le graphique commence à 0,004.'])


def power_integral(t, q, alpha):
    return math.exp(math.lgamma(q + 1) - math.lgamma(q + alpha + 1)) * np.asarray(t) ** (q + alpha)


def fractional_quadrature(func, t, alpha, n=256):
    """Substitution u=t(1−v^(1/α)), qui enlève le noyau singulier."""
    if t == 0:
        return 0.0
    v, w = gauss_unit(n)
    return float(t ** alpha / math.gamma(alpha + 1) * np.dot(w, func(t * (1 - v ** (1 / alpha)))))


def pulse_integral(t, alpha, a):
    t = np.asarray(t)
    return (t ** alpha - np.maximum(t - a, 0) ** alpha) / math.gamma(alpha + 1)


def integrale_fractionnaire(p):
    alpha, beta, q, a = p['alpha'], p['beta'], p['q'], p['a']
    t = np.linspace(0, 4, 601)
    if p['profile'] == 'pulse':
        f = (t <= a).astype(float)
        ja = pulse_integral(t, alpha, a)
        ordinary = np.minimum(t, a)
        combined = pulse_integral(t, alpha + beta, a)
        profile_label = 'Impulsion de durée a'
    else:
        f, ja = t ** q, power_integral(t, q, alpha)
        ordinary, combined = power_integral(t, q, 1), power_integral(t, q, alpha + beta)
        profile_label = 'Puissance t^q'
    probe = 2.0
    direct = float(power_integral(probe, q, alpha + beta))
    sequential = fractional_quadrature(lambda u: power_integral(u, q, beta), probe, alpha)
    orders = np.linspace(.1, 2, 181)
    at_two = np.array([float(power_integral(probe, q, order)) for order in orders])
    return result(
        [metric('Profil étudié', profile_label), metric('Ordre total α+β', alpha + beta),
         metric('J^α f(4)', ja[-1]), metric('J^1 f(4)', ordinary[-1]),
         metric('J^α[J^β(t^q)] à t=2, quadrature', sequential), metric('J^(α+β)(t^q) à t=2, formule', direct),
         metric('Écart relatif du contrôle de composition sur t^q', abs(sequential - direct) / max(abs(direct), 1e-30))],
        [chart('L’intégrale dépend de toute l’histoire entre 0 et t', 't≥0', 'Valeur', series('f(t)', t, f), series('J^α f(t)', t, ja), series('J^1 f(t)', t, ordinary)),
         chart('Changer l’ordre total transforme la réponse', 't≥0', 'Valeur', series('J^α f', t, ja), series('J^(α+β) f', t, combined)),
         chart('L’ordre devient un paramètre continu', 'Ordre α', 'J^α(t^q), évalué en t=2', series('Puissance : valeur en t=2', orders, at_two))],
        curves_scene('Une primitive pondérée par un noyau de mémoire', t, [('f', f), ('J^α f', ja), ('J^1 f', ordinary)], 't', 'Valeur', 'Pour une impulsion finie, la réponse continue après la fin du signal. Pour α=1, on retrouve la primitive choisie nulle en 0. Le contrôle de composition affiché porte toujours sur la puissance t^q.'),
        ['La formule de Cauchy pour n≥1 s’écrit Jⁿf(t)=1/(n−1)!∫₀ᵗ(t−u)^(n−1)f(u)du. Remplacer (n−1)! par Γ(α) définit J^α pour α>0.',
         'Pour f(u)=u^q, q>−1, poser u=tv. La fonction bêta donne J^α(t^q)=Γ(q+1)t^(q+α)/Γ(q+α+1).',
         'Les facteurs gamma se simplifient dans J^αJ^β(t^q). Pour des fonctions intégrables, Fubini et l’identité bêta permettent de prouver la même loi de composition.',
         'Pour une impulsion égale à 1 sur [0,a], intégrer seulement jusqu’à min(t,a) : J^αf(t)=[t^α−(t−a)_+^α]/Γ(α+1). Après a, le passé demeure dans le résultat.'],
        ['Borne initiale fixée à 0, ordres réels positifs. Les variables et fonctions sont sans dimension dans ce laboratoire.', 'La composition de deux intégrales fractionnaires se démontre sous des hypothèses d’intégrabilité ; il ne faut pas en déduire sans conditions une loi analogue pour toutes les dérivées fractionnaires.', 'Les réponses des profils sont analytiques ; le contrôle de composition utilise une quadrature indépendante sur une puissance.'])


def power_derivative(t, q, alpha):
    return math.exp(math.lgamma(q + 1) - math.lgamma(q + 1 - alpha)) * np.asarray(t) ** (q - alpha)


def derivees_fractionnaires(p):
    alpha, q, c, A = p['alpha'], int(p['q']), p['c'], p['memory']
    t = np.linspace(.02, 3, 601)
    constant = (c + (1 if q == 0 else 0)) * t ** (-alpha) / math.gamma(1 - alpha)
    caputo = np.zeros_like(t) if q == 0 else power_derivative(t, q, alpha)
    rl = caputo + constant
    history_t = np.linspace(0, 1, 401)
    history_one = history_t
    history_two = history_t + A * history_t * (1 - history_t) ** 2
    h1 = history_t ** (1 - alpha) / math.gamma(2 - alpha)
    delta = A * (power_derivative(history_t, 1, alpha) - 2 * power_derivative(history_t, 2, alpha) + power_derivative(history_t, 3, alpha))
    h2 = h1 + delta
    return result(
        [metric('Ordre α', alpha), metric('Caputo de c+t^q à t=1', 0 if q == 0 else float(power_derivative(1, q, alpha))),
         metric('Riemann–Liouville à t=1', (c + (1 if q == 0 else 0)) / math.gamma(1 - alpha) + (0 if q == 0 else float(power_derivative(1, q, alpha)))),
         metric('Différence due à la valeur initiale f(0)', (c + (1 if q == 0 else 0)) / math.gamma(1 - alpha)),
         metric('Deux histoires : même valeur f(1)', 1), metric('Deux histoires : même pente f′(1)', 1),
         metric('Écart de Caputo entre les deux histoires à t=1', delta[-1])],
        [chart('Deux définitions appliquées à la même fonction c+t^q', 't>0', 'Dérivée d’ordre α', series('Riemann–Liouville', t, rl), series('Caputo', t, caputo)),
         chart('Deux fonctions se rejoignent avec la même pente en t=1', 't∈[0,1]', 'Fonction', series('f₁(t)=t', history_t, history_one), series('f₂(t)=t+A t(1−t)²', history_t, history_two)),
         chart('Leur dérivée fractionnaire garde une mémoire du passé', 't∈[0,1]', 'Dérivée de Caputo', series('Caputo de f₁', history_t, h1), series('Caputo de f₂', history_t, h2))],
        curves_scene('La constante initiale sépare les deux définitions', t, [('Riemann–Liouville', rl), ('Caputo', caputo)], 't>0', 'Dérivée d’ordre α', 'Pour Caputo, une constante a une dérivée nulle. Pour Riemann–Liouville, elle donne un terme en t^(−α), singulier près de l’origine. Les courbes commencent à t=0,02.'),
        ['Pour 0<α<1, définir D_RL^α f=d/dt[J^(1−α)f] et D_C^αf=J^(1−α)f′. L’ordre des opérations change.',
         'Pour une fonction absolument continue, D_RL^αf=D_C^αf+f(0)t^(−α)/Γ(1−α). Caputo annule une constante ; Riemann–Liouville ne l’annule généralement pas.',
         'Pour q≥1 entier, les deux définitions donnent Γ(q+1)t^(q−α)/Γ(q+1−α) sur t^q, car t^q s’annule à l’origine.',
         'Les fonctions t et t+A(t−2t²+t³) ont la même valeur et la même pente en t=1. La linéarité donne leur différence de Caputo en dérivant les trois puissances : elle reste généralement non nulle.'],
        ['Ordres strictement entre 0 et 1 et borne initiale 0. Le cas d’un ordre entier utilise la dérivée ordinaire, sans substitution directe dans une formule singulière.', 'q est entier non négatif ; pour q=0, c+t^q est la constante c+1.', 'Le second exemple est un prolongement pour comprendre la non-localité. Les valeurs initiales dans une équation fractionnaire dépendent de la définition choisie.'])


def bell_partial(derivatives, n):
    """B[n,k] par récurrence triangulaire ; entrées scalaires ou tableaux."""
    shape = np.asarray(derivatives[0]).shape
    B = [[np.zeros(shape) for _ in range(n + 1)] for _ in range(n + 1)]
    B[0][0] = np.ones(shape)
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            B[i][k] = sum(math.comb(i - 1, j - 1) * derivatives[j - 1] * B[i - j][k - 1] for j in range(1, i - k + 2))
    return B[n]


def outer_derivative(outer, z, k):
    if outer == 'exp':
        return np.exp(z)
    if k == 0:
        return 1 / z if outer == 'inverse' else np.log(z)
    if outer == 'inverse':
        return (-1) ** k * math.factorial(k) / z ** (k + 1)
    return (-1) ** (k - 1) * math.factorial(k - 1) / z ** k


def faa_value(x, a, b, n, outer):
    x = np.asarray(x)
    g = 1 + a * x + b * x * x
    derivatives = [a + 2 * b * x] + ([np.full_like(x, 2 * b)] if n >= 2 else []) + [np.zeros_like(x) for _ in range(max(0, n - 2))]
    bell = bell_partial(derivatives, n)
    return sum(outer_derivative(outer, g, k) * bell[k] for k in range(1, n + 1))


def faa_di_bruno(p):
    n, outer, a, b, point = int(p['n']), p['outer'], p['a'], p['b'], p['point']
    x = np.linspace(-1.2, 1.2, 601)
    g = 1 + a * x + b * x * x
    composed = outer_derivative(outer, g, 0)
    derivative = faa_value(x, a, b, n, outer)
    g0, g1, g2 = 1 + a * point + b * point * point, a + 2 * b * point, 2 * b
    rows, term_curves = [], []
    for j in range(n // 2 + 1):
        m1, m2, k = n - 2 * j, j, n - j
        coefficient = math.factorial(n) // (math.factorial(m1) * math.factorial(m2) * 2 ** m2)
        value = coefficient * float(outer_derivative(outer, g0, k)) * g1 ** m1 * g2 ** m2
        rows.append([m1, m2, k, coefficient, value])
        term_curves.append(series(f'm₁={m1}, m₂={m2}', x, coefficient * outer_derivative(outer, g, k) * (a + 2 * b * x) ** m1 * (2 * b) ** m2))
    output = result(
        [metric('Ordre n', n), metric('Nombre de contributions structurelles', len(rows)), metric('g(x₀)', g0),
         metric('Dérivée n-ième en x₀, polynômes de Bell', float(faa_value(point, a, b, n, outer))),
         metric('Somme du tableau en x₀', math.fsum(row[-1] for row in rows)), metric('Minimum global de g', 1 - a * a / (4 * b))],
        [chart('La fonction composée', 'x', 'f(g(x))', series('f∘g', x, composed)),
         chart(f'La dérivée d’ordre {n}', 'x', f'(f∘g)^({n})(x)', series('Dérivée par Bell', x, derivative)),
         chart('Les termes du tableau : des compensations peuvent être importantes', 'x', 'Contribution', *term_curves)],
        curves_scene('Dériver une composition à un ordre élevé', x, [('Dérivée n-ième', derivative)], 'x', f'(f∘g)^({n})', 'Le tableau donne les multiplicités m₁,m₂, le nombre k=m₁+m₂ de dérivées de f et le coefficient combinatoire. Une contribution nulle à x₀ peut ne pas être identiquement nulle.'),
        ['Une dérivation agit soit sur f^(k)(g), ce qui introduit g′, soit sur un facteur g^(j), ce qui le remplace par g^(j+1). Faà di Bruno organise toutes ces possibilités.',
         'Le polynôme de Bell partiel B_(n,k) rassemble les produits de dérivées de g. La formule est (f∘g)^(n)=Σ_(k=1)^n f^(k)(g)B_(n,k)(g′,…,g^(n−k+1)).',
         'Ici g est quadratique : seuls m₁ et m₂ peuvent intervenir, avec m₁+2m₂=n. Le coefficient d’un terme vaut n!/[m₁!m₂!(2!)^m₂], et k=m₁+m₂.',
         'Pour f(z)=1/z, f^(k)(z)=(−1)^k k!/z^(k+1). Une autre méthode vient de g·h=1 : dériver n fois et isoler h^(n). Elle fournit un contrôle indépendant et efficace.'],
        ['g(x)=1+ax+bx². Avec les bornes des curseurs, g≥1−a²/(4b)≥0,375 : inverse et logarithme sont bien définis.', 'Les ordres élevés amplifient les valeurs et les compensations ; les graphes utilisent leurs unités propres. L’algorithme calcule les coefficients de Bell sans différences finies.'])
    output['table'] = dict(headers=['m₁', 'm₂', 'k=m₁+m₂', 'Coefficient', 'Contribution en x₀'], rows=rows)
    return output


def hermite(n, x):
    x = np.asarray(x)
    if n == 0:
        return np.ones_like(x)
    h0, h1 = np.ones_like(x), 2 * x
    for k in range(1, n):
        h0, h1 = h1, 2 * x * h1 - 2 * k * h0
    return h1


def hermite_function(n, x):
    return hermite(n, x) * np.exp(-np.asarray(x) ** 2 / 2) / (math.pi ** .25 * math.sqrt(2 ** n * math.factorial(n)))


def hermite_gauss(p):
    n, m = int(p['n']), int(p['m'])
    x = np.linspace(-5.5, 5.5, 801)
    H = hermite(n, x)
    gaussian_derivative = (-1) ** n * H * np.exp(-x * x)
    psi_n, psi_m = hermite_function(n, x), hermite_function(m, x)
    norm = gauss_integral(lambda t: hermite_function(n, t) ** 2, -11, 11, 384)
    product = gauss_integral(lambda t: hermite_function(n, t) * hermite_function(m, t), -11, 11, 384)
    roots = np.polynomial.hermite.hermroots([0] * n + [1]) if n else np.array([])
    output = result(
        [metric('Degré n de Hₙ', n), metric('Nombre de zéros réels simples', len(roots)),
         metric('Coefficient du terme de plus haut degré', 2 ** n), metric('Norme ∫ψₙ² sur [−11,11]', norm),
         metric('Produit scalaire ∫ψₙψₘ sur [−11,11]', product), metric('Valeur théorique du produit scalaire', 1 if n == m else 0),
         metric('Valeur Hₙ(0)', float(hermite(n, 0)))],
        [chart('La gaussienne et sa dérivée n-ième', 'x', 'Valeur', series('e^(−x²)', x, np.exp(-x * x)), series(f'Dérivée d’ordre {n}', x, gaussian_derivative)),
         chart('Enveloppe gaussienne : comparer des fonctions normalisées', 'x', 'ψ', series(f'ψ_{n}', x, psi_n), series(f'ψ_{m}', x, psi_m)),
         chart('Le produit scalaire se construit par une intégrale', 'x', 'Fonction intégrée', series('ψₙ², norme', x, psi_n ** 2), series('ψₙψₘ, orthogonalité', x, psi_n * psi_m)),
         chart('Le polynôme avant multiplication par la gaussienne', 'x', f'H_{n}(x)', series(f'H_{n}', x, H))],
        curves_scene('Une famille de modes sous une enveloppe gaussienne', x, [(f'ψ_{n}', psi_n), (f'ψ_{m}', psi_m)], 'x', 'Fonction normalisée', 'Convention des physiciens : H₁=2x et poids e^(−x²). Les fonctions ψ utilisent l’enveloppe e^(−x²/2). Les zéros et les alternances de signe rendent visible le degré.'),
        ['La formule de Rodrigues est Hₙ(x)=(−1)^n e^(x²)(dⁿ/dxⁿ)e^(−x²). Pour g=−x², Faà di Bruno ne conserve que g′=−2x et g″=−2.',
         'On obtient Hₙ=n!Σ_(j=0)^⌊n/2⌋(−1)^j(2x)^(n−2j)/[j!(n−2j)!]. Donc Hₙ a degré n, coefficient dominant 2ⁿ et parité celle de n.',
         'Les récurrences Hₙ′=2nH_(n−1) et H_(n+1)=2xHₙ−2nH_(n−1) donnent Hₙ″−2xHₙ′+2nHₙ=0.',
         'Par intégrations par parties, ∫ℝHₙHₘe^(−x²)dx=√π2ⁿn!δ_(n,m). La normalisation de ψ transforme ce résultat en ∫ψₙψₘ=δ_(n,m), puis −ψₙ″+x²ψₙ=(2n+1)ψₙ.'],
        ['Convention des physiciens explicitement fixée ; les polynômes dits probabilistes utilisent une autre échelle et un autre poids.', 'Les intégrales numériques sont calculées sur [−11,11], avec une queue gaussienne négligeable pour les degrés proposés. L’orthogonalité est un théorème, pas une conséquence du seul tracé.', 'L’oscillateur quantique est un prolongement ; la récurrence, les dérivées, la parité et les intégrations par parties sont des techniques CPGE.'])
    output['table'] = dict(headers=['Rang du zéro', 'Abscisse'], rows=[[i + 1, float(z)] for i, z in enumerate(roots)])
    return output


COMPUTE = {f.__name__: f for f in [gamma_euler, beta_geometrie, zeta_series, zeta_integrale, integrale_fractionnaire, derivees_fractionnaires, faa_di_bruno, hermite_gauss]}
