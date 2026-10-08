"""Calculs analytiques et quadratures contrôlées, convention Fourier en hertz.

TF(f)(ν)=∫ f(t) exp(−2iπνt) dt. La Laplace est unilatérale et causale.
Les signaux périodiques ont une amplitude normalisée explicitée dans chaque TP.
"""
from __future__ import annotations
import math
import numpy as np
from commun import chart, clean, integrate, metric, result, scene, series

PI = math.pi


def rc_response(t, tau, mode, amplitude=1., a=1., b=0., y0=0.):
    """Solution pour t≥0 de τ y′+y=u, avec état initial y0.

    Une impulsion d'aire A produit le saut A/τ ; y0 désigne alors l'état
    immédiatement AVANT l'impulsion. Dans les autres cas y(0+)=y0.
    """
    t = np.asarray(t, dtype=float)
    decay = np.exp(-t / tau)
    if mode == 'step': return amplitude + (y0 - amplitude) * decay
    if mode == 'impulse': return (amplitude / tau + y0) * decay
    if mode == 'ramp': return a * t + b - a * tau + (y0 - b + a * tau) * decay
    raise ValueError('Entrée RC inconnue.')


def rc_transfer(frequency, tau):
    return 1. / (1. + 2j * PI * np.asarray(frequency) * tau)


def rlc_response(t, omega0, zeta, mode):
    """Réponse causale au repos de H(p)=ω₀²/(p²+2ζω₀p+ω₀²)."""
    t = np.asarray(t, dtype=float)
    if abs(zeta - 1.) < 1e-12:
        decay = np.exp(-omega0 * t)
        return omega0 ** 2 * t * decay if mode == 'impulse' else 1. - decay * (1. + omega0 * t)
    if zeta < 1.:
        wd = omega0 * math.sqrt(1. - zeta ** 2)
        decay = np.exp(-zeta * omega0 * t)
        if mode == 'impulse': return omega0 ** 2 / wd * decay * np.sin(wd * t)
        return 1. - decay * (np.cos(wd * t) + zeta * omega0 / wd * np.sin(wd * t))
    delta = math.sqrt(zeta ** 2 - 1.)
    root1, root2 = -omega0 * (zeta - delta), -omega0 * (zeta + delta)
    exp1, exp2 = np.exp(root1 * t), np.exp(root2 * t)
    if mode == 'impulse': return omega0 ** 2 * (exp1 - exp2) / (root1 - root2)
    return 1. + (root2 * exp1 - root1 * exp2) / (root1 - root2)


def porte_convolution(t, width1, width2, shift=0.):
    """Longueur exacte de [−L₁/2,L₁/2]∩[t−d−L₂/2,t−d+L₂/2]."""
    t = np.asarray(t, dtype=float)
    return np.maximum(0., np.minimum(width1 / 2., t - shift + width2 / 2.)
                      - np.maximum(-width1 / 2., t - shift - width2 / 2.))


def fourier_coefficients(wave, N):
    """f(θ)=dc+Σ[a_n cos(nθ)+b_n sin(nθ)], θ=2πt/T."""
    n = np.arange(1, N + 1, dtype=float)
    a, b = np.zeros(N), np.zeros(N)
    odd = np.remainder(n, 2) == 1
    if wave == 'square':
        b[odd] = 4. / (PI * n[odd]); dc, energy = 0., 1.
    elif wave == 'triangle':
        a[odd] = -4. / (PI ** 2 * n[odd] ** 2); dc, energy = .5, 1. / 3.
    elif wave == 'sawtooth':
        b = 2. * (-1.) ** (n + 1.) / (PI * n); dc, energy = 0., 1. / 3.
    else: raise ValueError('Signal périodique inconnu.')
    return n, a, b, dc, energy


def periodic_wave(theta, wave):
    """Valeurs de demi-somme aux sauts, pour une comparaison à Dirichlet."""
    theta = np.asarray(theta, dtype=float)
    wrapped = np.remainder(theta + PI, 2. * PI) - PI
    if wave == 'triangle': return np.abs(wrapped) / PI
    if wave == 'square':
        out = np.sign(np.sin(theta))
        return np.where(np.abs(np.sin(theta)) < 1e-13, 0., out)
    if wave == 'sawtooth': return np.where(np.abs(np.abs(wrapped) - PI) < 1e-13, 0., wrapped / PI)
    raise ValueError('Signal périodique inconnu.')


def fourier_sum(theta, wave, N, fejer=False, abel=None):
    theta = np.asarray(theta, dtype=float)
    n, a, b, dc, _ = fourier_coefficients(wave, N)
    weights = 1. - n / (N + 1.) if fejer else np.ones(N)
    if abel is not None: weights *= float(abel) ** n
    angles = n[:, None] * theta.ravel()[None, :]
    out = dc + (a * weights) @ np.cos(angles) + (b * weights) @ np.sin(angles)
    return out.reshape(theta.shape)


def _rc(p):
    tau, A, a, b, y0 = (float(p[k]) for k in ('tau', 'amplitude', 'a', 'b', 'y0'))
    mode = p['mode']; t = np.linspace(0., 8. * tau, 501)
    output = rc_response(t, tau, mode, A, a, b, y0)
    if mode == 'step':
        input_ = np.full_like(t, A); asymptote = np.full_like(t, A)
        equation = 'y(t)=A+(y₀−A)e^(−t/τ).'; units = 'V'
    elif mode == 'ramp':
        input_ = a * t + b; asymptote = a * t + b - a * tau
        equation = 'y(t)=at+b−aτ+(y₀−b+aτ)e^(−t/τ).'; units = 'V'
    else:
        input_ = np.zeros_like(t); asymptote = np.zeros_like(t)
        equation = 'y(t)=(A/τ+y₀)e^(−t/τ) pour t>0 ; y(0+)−y(0−)=A/τ.'; units = 'V'
    initial = float(output[0]); residual = output - asymptote
    curves = [series('Sortie y(t)', t, output), series('Réponse asymptotique', t, asymptote)]
    if mode != 'impulse': curves.insert(0, series('Entrée u(t)', t, input_))
    return result([metric('Constante de temps', tau, 's'), metric('y(0+)', initial, units),
                   metric('Part transitoire à 5τ', (initial - float(asymptote[0])) * math.exp(-5.), 'V'),
                   metric('Pôle de H', -1. / tau, 's⁻¹')],
                  [chart('Entrée et sortie causales', 't (s)', 'Tension (V)', *curves),
                   chart('Transitoire isolé', 't/τ', 'y−y_asymptote (V)', series('Transitoire', t / tau, residual))],
                  scene('filter', 'Une équation, un pôle, trois entrées', 'τy′+y=u ; état initial précisé séparément de la fonction de transfert.', tau=tau, mode=mode, pole=-1. / tau, initial=y0, initial_after=initial, gain=1.),
                  ['Fixer u(t)=0 pour t<0. Le signal d’entrée est causal ; la tension initiale est un état du système.',
                   'L(y′)=pY−y₀ donne (1+τp)Y=U+τy₀. Le produit H(p)U(p) représente la seule réponse au repos.',
                   'Décomposer en éléments simples puis inverser : ' + equation,
                   'Vérifier directement τy′+y=u pour t>0, puis contrôler l’état initial. Pour une impulsion, intégrer l’équation autour de 0.',
                   'Le résidu transitoire est proportionnel à e^(−t/τ). Une rampe laisse un retard asymptotique aτ.'],
                  ['L est la transformée unilatérale ; l’entrée causale usuelle est transformée pour Re(p)>0. La transformée de la réponse impulsionnelle converge pour Re(p)>−1/τ ; son expression rationnelle se prolonge hors du pôle.',
                   'A est en V pour un pas, en V·s pour une impulsion de Dirac. a est en V/s, b et y₀ en V.',
                   'Pour l’impulsion, y₀=y(0−) ; la Dirac est une distribution, elle n’est pas dessinée comme une fonction de hauteur finie.'])


def _bode(p):
    tau, fundamental = float(p['tau']), float(p['frequency'])
    fc = 1. / (2. * PI * tau)
    frequencies = fc * np.logspace(-2., 2., 361); H = rc_transfer(frequencies, tau)
    t = np.linspace(0., 3. / fundamental, 601)
    harmonics = np.array([1., 2., 5.]); amplitudes = np.array([1., .6, .35]); phases = np.array([0., .3, -.5])
    harmonics_H = rc_transfer(harmonics * fundamental, tau)
    angles = 2. * PI * harmonics[:, None] * fundamental * t[None, :] + phases[:, None]
    input_ = np.sum(amplitudes[:, None] * np.sin(angles), axis=0)
    components = amplitudes[:, None] * np.abs(harmonics_H)[:, None] * np.sin(angles + np.angle(harmonics_H)[:, None])
    output = np.sum(components, axis=0)
    return result([metric('Coupure ν_c', fc, 'Hz'), metric('Gain à ν_c', -10. * math.log10(2.), 'dB'),
                   metric('Gain à ν₁', abs(harmonics_H[0])), metric('Phase à ν₁', math.degrees(float(np.angle(harmonics_H[0]))), '°')],
                  [chart('Diagramme de gain', 'ν (Hz)', '20 log₁₀|H| (dB)', series('Gain', frequencies, 20. * np.log10(np.abs(H))), x_scale='log'),
                   chart('Diagramme de phase', 'ν (Hz)', 'Arg H (°)', series('Phase', frequencies, np.degrees(np.angle(H))), x_scale='log'),
                   chart('Recomposition temporelle en régime établi', 't (s)', 'Amplitude', series('Entrée : 3 harmoniques', t, input_), series('Sortie recomposée', t, output)),
                   chart('Contributions à la sortie', 't (s)', 'Amplitude', *[series(f'Harmonique {int(k)}', t, y) for k, y in zip(harmonics, components)])],
                  scene('filter', 'Chaque harmonique porte son gain et sa phase', 'H(i2πν)=1/(1+i2πντ). La sortie garde les fréquences et transforme leurs amplitudes et phases.', tau=tau, cutoff=fc, frequencies=harmonics * fundamental, gains=np.abs(harmonics_H), phases=np.angle(harmonics_H)),
                  ['Transformer τy′+y=u au repos pour obtenir H(p)=1/(1+τp).',
                   'À la fréquence ν, H(i2πν) a pour module 1/√(1+(2πντ)²) et pour argument −arctan(2πντ).',
                   'L’entrée est sin(2πν₁t)+0,6 sin(4πν₁t+0,3)+0,35 sin(10πν₁t−0,5). Les phases sont en radians.',
                   'Multiplier chaque amplitude par |H| et ajouter Arg H à sa phase. La linéarité autorise la recomposition.',
                   'Les hautes fréquences sont davantage atténuées : une forme d’onde change même si chacune de ses fréquences est conservée.'],
                  ['Le graphe temporel montre le régime permanent, après disparition du transitoire.',
                   'À ν_c=1/(2πτ), le gain est 1/√2, soit −3,0103 dB ; la phase vaut −45°.', 'Fréquences en Hz, pulsations en rad/s.'])


def _rlc(p):
    w, zeta, mode = float(p['omega0']), float(p['zeta']), p['mode']
    if zeta < 1.:
        decay_rate = zeta * w; imag = w * math.sqrt(1. - zeta ** 2)
        poles = [[-zeta * w, imag], [-zeta * w, -imag]]; regime = 'Sous-amorti'
    elif zeta > 1.:
        d = math.sqrt(zeta ** 2 - 1.); decay_rate = w / (zeta + d)
        poles = [[-decay_rate, 0.], [-w * (zeta + d), 0.]]; regime = 'Suramorti'
    else:
        decay_rate = w; poles = [[-w, 0.], [-w, 0.]]; regime = 'Critique, pôle double'
    t = np.linspace(0., 8. / decay_rate, 601); y = rlc_response(t, w, zeta, mode)
    frequency = np.linspace(0., 2.5 * w / (2. * PI), 501)
    denominator = w ** 2 - (2. * PI * frequency) ** 2 + 2j * zeta * w * 2. * PI * frequency
    H = w ** 2 / denominator
    overshoot = math.exp(-PI * zeta / math.sqrt(1. - zeta ** 2)) if zeta < 1. else 0.
    return result([metric('Régime', regime), metric('Pulsation propre', w, 'rad/s'), metric('Dépassement du pas (exact)', 100. * overshoot, '%'), metric('Taux de décroissance lent', decay_rate, 's⁻¹')],
                  [chart('Réponse temporelle au repos', 't (s)', 'y(t)' if mode == 'step' else 'h(t) (s⁻¹)', series('Réponse', t, y), series('Limite', t, np.full_like(t, 1. if mode == 'step' else 0.))),
                   chart('Module fréquentiel', 'ν (Hz)', '|H(i2πν)|', series('Module', frequency, np.abs(H))),
                   chart('Plan des pôles', 'Re p (s⁻¹)', 'Im p (s⁻¹)', dict(series('Pôles (deux points ; multiplicité 2 au régime critique)', np.array(poles)[:, 0], np.array(poles)[:, 1]),style='dots'))],
                  scene('poles', 'Les racines de p²+2ζω₀p+ω₀²', 'Le régime dépend du discriminant ; tous les pôles restent dans le demi-plan Re p<0.', poles=poles, damping=zeta, omega0=w, regime=regime),
                  ['Poser y″+2ζω₀y′+ω₀²y=ω₀²u avec y(0−)=y′(0−)=0.',
                   'La transformée donne H(p)=ω₀²/(p²+2ζω₀p+ω₀²). Ses pôles sont −ζω₀±ω₀√(ζ²−1).',
                   'ζ<1 : exponentielle amortie et oscillation ; ζ=1 : le pôle double produit un facteur t ; ζ>1 : somme de deux exponentielles réelles.',
                   'La réponse au pas est l’intégrale de la réponse impulsionnelle. Son gain statique vaut H(0)=1.',
                   'Le dépassement du pas vaut exp(−πζ/√(1−ζ²)) dans le régime sous-amorti et zéro dans les deux autres régimes.'],
                  ['ζ>0 garantit la stabilité du modèle linéaire. La réponse causale converge dans le demi-plan à droite du pôle le plus à droite.',
                   'L’impulsion est d’aire 1 ; h(t) a l’unité s⁻¹. Le pas et sa réponse sont normalisés et sans dimension.', 'Au régime critique, les deux points du plan des pôles sont confondus : il s’agit d’un pôle de multiplicité 2.'])


def _dirichlet(p):
    damping, cutoff = float(p['p']), float(p['cutoff'])
    grid = np.linspace(0., cutoff, max(2001, int(math.ceil(cutoff / .006)) + 1))
    integrand = np.sinc(grid / PI) * np.exp(-damping * grid)
    increments = .5 * (integrand[1:] + integrand[:-1]) * np.diff(grid)
    cumulative = np.concatenate(([0.], np.cumsum(increments)))
    numerical = float(cumulative[-1]); exact = math.atan2(1., damping)
    show = np.linspace(0., cutoff, 601)
    parameters = np.concatenate(([0.], np.geomspace(.001, 3., 400)))
    bound = 2. * math.exp(-damping * cutoff) / cutoff
    return result([metric('Valeur exacte I(p)', exact), metric('Quadrature sur [0,L]', numerical), metric('Borne du reste intégral après L', bound), metric('Limite d’Abel', PI / 2.)],
                  [chart('Intégrande régularisé', 't', 'e^(−pt) sin(t)/t', series('Intégrande', show, np.sinc(show / PI) * np.exp(-damping * show))),
                   chart('Intégrale cumulée tronquée', 'L′', '∫₀ᴸ′ e^(−pt) sin(t)/t dt', series('Quadrature cumulée', show, np.interp(show, grid, cumulative)), series('I(p), intégrale jusqu’à ∞', show, np.full_like(show, exact))),
                   chart('Approche de la limite d’Abel', 'p≥0', 'I(p)', series('arctan(1/p), prolongée en p=0', parameters, np.arctan2(np.ones_like(parameters), parameters)), series('π/2', parameters, np.full_like(parameters, PI / 2.)))],
                  scene('kernel', 'Amortir pour calculer, puis retirer l’amortissement', 'I′(p)=−1/(1+p²), I(+∞)=0 ; d’où I(p)=arctan(1/p).', parameter=damping, cutoff=cutoff, exact=exact, approximation=numerical, tail_bound=bound),
                  ['Pour p>0, e^(−pt) sin(t)/t est absolument intégrable. En t=0, sa valeur prolongée vaut 1.',
                   'Sur tout compact de ]0,+∞[, dériver sous l’intégrale : I′(p)=−∫₀∞ e^(−pt) sin(t) dt=−1/(1+p²).',
                   'La condition I(p)→0 quand p→+∞ fixe la constante : I(p)=π/2−arctan p=arctan(1/p).',
                   'Le contrôle uniforme du reste oscillant permet le passage p→0+ et donne ∫₀∞ sin(t)/t dt=π/2.',
                   'La borne 2e^(−pL)/L contrôle le reste analytique après L. Le graphe cumulé utilise une quadrature trapézoïdale de pas au plus 0,006 : son erreur numérique s’y ajoute.'],
                  ['La variable t et p sont ici adimensionnés. Le modèle exige p>0 ; la valeur en p=0 est le prolongement exact par limite.', 'L’intégrale de Dirichlet converge comme intégrale impropre, mais ∫₀∞ |sin(t)/t| dt diverge.', 'Un accord numérique sur une borne finie ne constitue pas une preuve de la valeur de l’intégrale impropre.'])


def _phase_segments(frequency, transform):
    """Découper aux zéros et aux sauts de branche, sans NaN dans le JSON."""
    phase = np.angle(transform); valid = np.abs(transform) > 1e-10 * max(1., float(np.max(np.abs(transform))))
    curves, start = [], None
    for k in range(len(frequency) + 1):
        stop = k == len(frequency) or not valid[k] or (k > 0 and valid[k - 1] and abs(phase[k] - phase[k - 1]) > PI)
        if stop and start is not None:
            if k - start >= 2: curves.append(series('Phase (branche principale, hors zéros)', frequency[start:k], phase[start:k]))
            start = None
        if k < len(frequency) and valid[k] and start is None: start = k
    return curves


def _porte(p):
    width, shift = float(p['width']), float(p['shift'])
    t = shift + np.linspace(-2. * width, 2. * width, 501)
    values = np.where(np.abs(t - shift) < width / 2., 1., 0.)
    frequency = np.linspace(-5., 5., 601) / width
    transform = width * np.sinc(width * frequency) * np.exp(-2j * PI * frequency * shift)
    return result([metric('Aire de la porte = TF(0)', width, 's'), metric('Premier zéro positif', 1. / width, 'Hz'), metric('Largeur du lobe central', 2. / width, 'Hz'), metric('Centre temporel', shift, 's')],
                  [chart('Porte temporelle', 't (s)', 'f(t)', series('Porte', t, values)),
                   chart('Transformée complexe', 'ν (Hz)', 'TF(f) (s)', series('Partie réelle', frequency, transform.real), series('Partie imaginaire', frequency, transform.imag)),
                   chart('Module spectral', 'ν (Hz)', '|TF(f)| (s)', series('Module', frequency, np.abs(transform))),
                   chart('Phase spectrale, zéros exclus', 'ν (Hz)', 'Arg TF(f) (rad)', *_phase_segments(frequency, transform),same_color=True)],
                  scene('spectrum', 'Une translation fait tourner le spectre', 'TF(f)(ν)=L sinc(Lν)e^(−2iπνt₀), avec sinc(x)=sin(πx)/(πx).', width=width, shift=shift, first_zero=1. / width, central_width=2. / width),
                  ['Définir f(t)=1 lorsque |t−t₀|<L/2, et 0 en dehors. Les valeurs aux deux bords ne changent pas la transformée.',
                   'Intégrer exp(−2iπνt) sur [t₀−L/2,t₀+L/2] : TF(f)=L sinc(Lν)e^(−2iπνt₀).',
                   'En ν=0, prolonger sinc par 1 : la transformée vaut l’aire L. Les autres zéros sont ν=k/L, k entier non nul.',
                   'Réduire L élargit le spectre ; déplacer t₀ conserve le module mais ajoute une phase −2πνt₀.',
                   'La phase est définie modulo 2π et n’est pas définie aux zéros. Les courbes sont coupées aux zéros et aux changements de branche.'],
                  ['Convention en Hz : sinc(x)=sin(πx)/(πx), conformément à numpy.sinc. La notation sin(x)/x correspond à sinc(x/π).', 'La porte a une amplitude 1 et une aire L ; la transformée a l’unité seconde.', 'Une porte temporelle n’est pas limitée en fréquence : ses lobes secondaires s’étendent à l’infini.'])


def _gaussian(p):
    sigma, A = float(p['sigma']), float(p['amplitude'])
    t = np.linspace(-5. * sigma, 5. * sigma, 501)
    st, sf = sigma / math.sqrt(2.), 1. / (2. * math.sqrt(2.) * PI * sigma)
    frequency = np.linspace(-5. * sf, 5. * sf, 501)
    signal = A * np.exp(-t ** 2 / (2. * sigma ** 2))
    transform = A * sigma * math.sqrt(2. * PI) * np.exp(-2. * PI ** 2 * sigma ** 2 * frequency ** 2)
    energy = A ** 2 * sigma * math.sqrt(PI)
    return result([metric('Énergie E=∫|f|²', energy), metric('Écart type temporel énergétique σ_t', st, 's'), metric('Écart type fréquentiel énergétique σ_ν', sf, 'Hz'), metric('Produit σ_t σ_ν', st * sf)],
                  [chart('Amplitude temporelle', 't (s)', 'f(t)', series('Gaussienne', t, signal)),
                   chart('Amplitude de la transformée', 'ν (Hz)', 'TF(f)(ν)', series('Transformée gaussienne', frequency, transform)),
                   chart('Densités d’énergie réduites', 'Variable / écart type énergétique', 'Densité × écart type', series('Temps : σ_t |f|²/E', t / st, st * signal ** 2 / energy), series('Fréquence : σ_ν |TF(f)|²/E', frequency / sf, sf * transform ** 2 / energy))],
                  scene('spectrum', 'Plus bref en temps, plus large en fréquence', 'Les densités |f|²/E et |TF(f)|²/E ont la même énergie totale 1 ; leurs écarts types satisfont σ_tσ_ν=1/(4π).', sigma=sigma, amplitude=A, time_width=st, frequency_width=sf, product=st * sf),
                  ['Partir de f(t)=A exp(−t²/(2σ²)). Le paramètre σ décrit la largeur de l’amplitude, pas celle de la densité d’énergie.',
                   'Avec la convention Hz, TF(f)(ν)=Aσ√(2π) exp(−2π²σ²ν²).',
                   'Parseval donne E=∫|f|² dt=∫|TF(f)|² dν=A²σ√π. Normaliser séparément les deux densités par E.',
                   'Leurs variances sont σ_t²=σ²/2 et σ_ν²=1/(8π²σ²). Le produit exact est 1/(4π).',
                   'Pour des signaux suffisamment réguliers de variances finies, l’intégration par parties et Cauchy–Schwarz donnent σ_tσ_ν≥1/(4π). La gaussienne réalise l’égalité.'],
                  ['Les amplitudes sont positives et réelles dans ce TP ; A≠0 permet la normalisation énergétique.', 'La borne utilise les écarts types des densités d’énergie, et des fréquences en Hz. En pulsation elle devient σ_tσ_ω≥1/2.', 'Les courbes sont tronquées à cinq largeurs d’affichage ; les métriques sont analytiques sur toute la droite.'])


def _convolution(p):
    L1, L2, shift, probe = (float(p[k]) for k in ('width1', 'width2', 'shift', 'probe'))
    t = shift + np.linspace(-.7 * (L1 + L2), .7 * (L1 + L2), 601)
    out = porte_convolution(t, L1, L2, shift)
    lo, hi = min(-L1 / 2., probe - shift - L2 / 2.), max(L1 / 2., probe - shift + L2 / 2.)
    u = np.linspace(lo - .2, hi + .2, 501)
    f = np.where(np.abs(u) < L1 / 2., 1., 0.)
    reflected = np.where(np.abs(probe - u - shift) < L2 / 2., 1., 0.)
    frequency = np.linspace(-4. / min(L1, L2), 4. / min(L1, L2), 601)
    transform = L1 * L2 * np.sinc(L1 * frequency) * np.sinc(L2 * frequency) * np.exp(-2j * PI * frequency * shift)
    overlap = float(porte_convolution(probe, L1, L2, shift))
    return result([metric('Valeur (f*g)(t) à la position choisie', overlap, 's'), metric('Hauteur du plateau', min(L1, L2), 's'), metric('Largeur du support', L1 + L2, 's'), metric('Aire de la convolution', L1 * L2, 's²')],
                  [chart('Convolution exacte', 't (s)', '(f*g)(t) (s)', series('Convolution', t, out)),
                   chart('Recouvrement à t fixé', 'u (s)', 'Amplitude', series('f(u)', u, f), series('g(t−u)', u, reflected), series('Produit f(u)g(t−u)', u, f * reflected)),
                   chart('Produit des spectres', 'ν (Hz)', 'TF(f*g) (s²)', series('Module', frequency, np.abs(transform)), series('Partie réelle', frequency, transform.real), series('Partie imaginaire', frequency, transform.imag))],
                  scene('convolution', 'Retourner g, déplacer, intégrer le produit', 'Le résultat est la longueur de l’intersection des supports. Des largeurs différentes donnent un plateau de longueur |L₁−L₂|.', first=[-L1 / 2., L1 / 2.], second=[probe - shift - L2 / 2., probe - shift + L2 / 2.], probe=probe, width1=L1, width2=L2, shift=shift, overlap=overlap),
                  ['Définir f=1 sur [−L₁/2,L₁/2] et g=1 sur [d−L₂/2,d+L₂/2].',
                   'À t fixé, g(t−u)=1 sur [t−d−L₂/2,t−d+L₂/2]. La convolution est l’aire du recouvrement dans la variable u.',
                   'Donc (f*g)(t)=max(0,min(L₁/2,t−d+L₂/2)−max(−L₁/2,t−d−L₂/2)).',
                   'Le support va de d−(L₁+L₂)/2 à d+(L₁+L₂)/2. La hauteur maximale est min(L₁,L₂) ; la largeur du plateau est |L₁−L₂|.',
                   'TF(f*g)=L₁L₂ sinc(L₁ν)sinc(L₂ν)e^(−2iπνd). À ν=0, l’aire vaut L₁L₂, produit des aires initiales.'],
                  ['Convolution bilatérale sur ℝ, puisque les portes peuvent se trouver à des temps négatifs.', 'Le résultat utilise une formule géométrique exacte ; aucune convolution discrète sans facteur de pas n’est employée.', 'Les valeurs isolées aux bords ne changent aucune intégrale.'])


def _gibbs(p):
    wave, N, period = p['wave'], int(p['N']), float(p['period'])
    theta = np.linspace(-PI, PI, 601); t = theta * period / (2. * PI)
    original = periodic_wave(theta, wave); partial = fourier_sum(theta, wave, N); fejer = fourier_sum(theta, wave, N, True)
    n, a, b, dc, energy = fourier_coefficients(wave, N); powers = .5 * (a ** 2 + b ** 2)
    error2 = max(0., energy - dc ** 2 - float(np.sum(powers)))
    fejer_error2 = error2 + float(np.sum((n / (N + 1.)) ** 2 * powers))
    if wave == 'square':
        m = (N + 1) // 2; theta_peak = PI / (2. * m); jump = 2.
        peak = float(fourier_sum(np.array([theta_peak]), wave, N)[0]); norm_overshoot = max(0., peak - 1.) / jump
        near = np.linspace(-4. * PI / (N + 1), 4. * PI / (N + 1), 501); near_t = near * period / (2. * PI)
        note = 'Premier maximum près du saut en t=0 ; il est calculé en θ=π/(2m), m étant le nombre d’indices impairs ≤N.'
    elif wave == 'sawtooth':
        theta_peak = PI - PI / (N + 1.); jump = 2.
        peak = float(fourier_sum(np.array([theta_peak]), wave, N)[0]); norm_overshoot = max(0., peak - 1.) / jump
        near = PI + np.linspace(-4. * PI / (N + 1), 4. * PI / (N + 1), 501); near_t = near * period / (2. * PI)
        note = 'Premier maximum près du raccord θ=π ; il est calculé en θ=π−π/(N+1). Pour un petit N le signal peut rester sous 1.'
    else:
        peak, norm_overshoot, jump = 0., 0., 0.
        near = np.linspace(-.5, .5, 501); near_t = near * period / (2. * PI)
        note = 'Le triangle est continu : il n’a pas de saut de Gibbs. Sa série est normalement convergente, car les coefficients sont sommables.'
    return result([metric('Erreur quadratique moyenne de S_N (exacte)', error2), metric('Erreur quadratique moyenne de Fejér (exacte)', fejer_error2), metric('Dépassement / saut', 100. * norm_overshoot, '%' if jump else '% ; aucun saut'), metric('Harmoniques non nulles', int(np.count_nonzero(a ** 2 + b ** 2)))],
                  [chart('Une période : original, Dirichlet, Fejér', 't (s)', 'Amplitude', series('Signal, demi-somme aux sauts', t, original), series('Somme partielle S_N', t, partial), series('Moyenne de Fejér σ_N', t, fejer)),
                   chart('Loupe locale au raccord ou à la pointe', 't (s)', 'Amplitude', series('Signal', near_t, periodic_wave(near, wave)), series('S_N', near_t, fourier_sum(near, wave, N)), series('Fejér', near_t, fourier_sum(near, wave, N, True))),
                   chart('Amplitudes harmoniques', 'Indice n', '√(a_n²+b_n²)', series('Dirichlet', n, np.sqrt(a ** 2 + b ** 2)), series('Fejér : poids 1−n/(N+1)', n, (1. - n / (N + 1.)) * np.sqrt(a ** 2 + b ** 2)))],
                  scene('harmonics', 'Convergence ponctuelle, énergie et lissage', 'σ_N=(S₀+⋯+S_N)/(N+1) amortit chaque coefficient par 1−n/(N+1).', wave=wave, N=N, period=period, jump=jump, first_peak=peak, overshoot=norm_overshoot),
                  ['Poser θ=2πt/T. Créneau : sign(sin θ). Triangle : |θ|/π sur [−π,π]. Rampe : θ/π sur ]−π,π[, puis prolongement périodique.',
                   'Utiliser la parité avant d’intégrer les coefficients. Créneau : b_n=4/(πn) pour n impair. Triangle : a_n=−4/(π²n²) pour n impair et terme constant 1/2. Rampe : b_n=2(−1)^(n+1)/(πn).',
                   'La somme S_N conserve les indices 1 à N. Aux sauts, la valeur de convergence est la demi-somme des limites latérales.',
                   'La moyenne de Fejér multiplie a_n et b_n par 1−n/(N+1). Son noyau positif évite le dépassement des bornes du signal.',
                   note, 'Pour les signaux à saut et N→∞, le dépassement de Dirichlet tend à environ 8,949% de la hauteur du saut ; sa zone se rétrécit sans que son amplitude disparaisse.'],
                  ['Les métriques d’erreur sont des moyennes quadratiques sur une période, calculées avec Parseval ; elles ne sont pas des estimations visuelles sur la grille.', 'Pour le triangle, une majoration uniforme du reste est 4/(π²N).', 'Les valeurs dessinées aux sauts sont les demi-sommes ; aucun changement en un point ne modifie les coefficients ni l’énergie.'])


def _parseval(p):
    wave, N = p['wave'], int(p['N'])
    n, a, b, dc, energy = fourier_coefficients(wave, N); powers = .5 * (a ** 2 + b ** 2)
    cumulative = dc ** 2 + np.cumsum(powers); residual = np.maximum(energy - cumulative, 1e-16)
    all_n = np.concatenate(([0.], n)); all_powers = np.concatenate(([dc ** 2], powers))
    theta = np.linspace(-PI, PI, 601)
    s2 = float(np.sum(1. / n ** 2)); s4 = float(np.sum(1. / n ** 4)); odd = n[np.remainder(n, 2) == 1]
    if wave == 'square': identity = '1=(8/π²)Σ_{n impair≥1}1/n² ; donc Σ_{n impair≥1}1/n²=π²/8 et Σ_{n≥1}1/n²=π²/6.'
    elif wave == 'triangle': identity = '1/3=1/4+(8/π⁴)Σ_{n impair≥1}1/n⁴ ; donc Σ_{n impair≥1}1/n⁴=π⁴/96 et Σ_{n≥1}1/n⁴=π⁴/90.'
    else: identity = '1/3=(2/π²)Σ_{n≥1}1/n² ; donc Σ_{n≥1}1/n²=π²/6.'
    return result([metric('Énergie moyenne totale', energy), metric('Énergie moyenne captée jusqu’à N', float(cumulative[-1])), metric('Fraction captée', 100. * float(cumulative[-1]) / energy, '%'), metric('Reste quadratique moyen', float(residual[-1])), metric('Σ₁ᴺ 1/n²', s2), metric('Σ₁ᴺ 1/n⁴', s4)],
                  [chart('Puissance de chaque harmonique et du continu', 'Indice n (0 : continu)', 'Puissance moyenne', series('Puissances', all_n, all_powers)),
                   chart('Bilan cumulatif', 'Dernier indice N′', 'Énergie moyenne', series('Captée', n, cumulative), series('Totale exacte', n, np.full_like(n, energy))),
                   chart('Énergie du reste', 'Dernier indice N′', 'Reste quadratique moyen', series('Reste', n, residual), y_scale='log'),
                   chart('Signal et projection orthogonale', 'θ=2πt/T (rad)', 'Amplitude', series('Signal', theta, periodic_wave(theta, wave)), series('Projection S_N', theta, fourier_sum(theta, wave, N)))],
                  scene('harmonics', 'Pythagore dans l’espace des signaux', 'Moyenne |f|²=dc²+½Σ(a_n²+b_n²). Les puissances s’ajoutent grâce à l’orthogonalité.', wave=wave, N=N, total=energy, captured=float(cumulative[-1]), residual=float(residual[-1]), odd_sum2=float(np.sum(1. / odd ** 2)), odd_sum4=float(np.sum(1. / odd ** 4))),
                  ['Munir les signaux T-périodiques du produit scalaire (1/T)∫₀ᵀ f(t)ḡ(t) dt. Les exponentielles e^(2iπnt/T) sont orthonormales.',
                   'Pour une série réelle, les cosinus et sinus ont une norme carrée 1/2. Le terme constant dc=a₀/2 contribue dc².',
                   'Calculer directement la moyenne du carré : 1 pour le créneau, 1/3 pour le triangle normalisé et la rampe normalisée.',
                   'Parseval : moyenne |f|²=dc²+(1/2)Σ(a_n²+b_n²). La projection S_N minimise l’erreur quadratique parmi les polynômes trigonométriques de degré N.',
                   identity, 'Séparer les indices pairs et impairs : Σ_{pair}1/n^q=2^(−q)Σ_{n≥1}1/n^q. Le reste d’énergie est exact, y compris pour un petit nombre d’harmoniques.'],
                  ['Il s’agit de puissance moyenne périodique, et non de l’énergie ∫ℝ |f|², qui diverge pour ces signaux non nuls.', 'Pour les signaux normalisés du TP, le terme constant vaut 1/2 pour le triangle et 0 pour les deux autres.', 'Un coefficient absent, par exemple un indice pair du créneau, contribue zéro ; N désigne le degré, pas le nombre de termes non nuls.'])


def _poisson(p):
    r, N, period = float(p['r']), int(p['N']), float(p['period'])
    span = min(PI / 2., max(.05, 4. * (1. - r)))
    theta = np.unique(np.concatenate((np.linspace(-PI, -span, 180), np.linspace(-span, span, 251), np.linspace(span, PI, 180))))
    t = theta * period / (2. * PI)
    exact = (1. - r ** 2) / ((1. - r) ** 2 + 4. * r * np.sin(theta / 2.) ** 2)
    n = np.arange(1, N + 1, dtype=float)
    partial = 1. + (2. * r ** n) @ np.cos(n[:, None] * theta[None, :])
    bound = 2. * r ** (N + 1) / (1. - r)
    smoothed = 2. / PI * np.arctan2(2. * r * np.sin(theta), np.full_like(theta, 1. - r ** 2))
    return result([metric('Masse sur une période (exacte)', period, 's'), metric('Maximum P_r(0)', (1. + r) / (1. - r)), metric('Minimum P_r(T/2)', (1. - r) / (1. + r)), metric('Norme uniforme exacte du reste après N', bound)],
                  [chart('Noyau géométrique bilatéral', 't (s)', 'P_r(t)', series('Somme exacte', t, exact), series('Somme partielle |n|≤N', t, partial)),
                   chart('Reste et contrôle uniforme', 't (s)', 'P_r−P_{r,N}', series('Reste', t, exact - partial), series('Borne +', t, np.full_like(t, bound)), series('Borne −', t, np.full_like(t, -bound))),
                   chart('Poisson appliqué à un créneau', 't (s)', 'Amplitude', series('Créneau', t, periodic_wave(theta, 'square')), series('Lissage exact par Poisson', t, smoothed), series('Harmoniques amorties jusqu’à N', t, fourier_sum(theta, 'square', N, abel=r)))],
                  scene('kernel', 'Une masse fixe qui se concentre', 'P_r≥0 et ∫sur une période P_r=T. La convolution périodique avec P_r/T amortit l’harmonique n par r^|n|.', parameter=r, N=N, period=period, maximum=(1. + r) / (1. - r), tail_bound=bound),
                  ['Regrouper les indices k et −k : P_r(t)=1+2Σ_{k≥1}r^k cos(2πkt/T).',
                   'La série converge normalement pour r<1, car Σ2r^k converge. Sommer les deux séries géométriques complexes donne (1−r²)/(1−2r cos θ+r²).',
                   'L’intégration terme à terme conserve uniquement le terme constant : ∫_{−T/2}^{T/2}P_r(t) dt=T.',
                   'Le reste est majoré par 2r^(N+1)/(1−r). Cette borne est atteinte en t=0 : c’est ici la norme uniforme exacte.',
                   'La convolution périodique normalisée transforme chaque coefficient c_n en r^|n|c_n. Pour le créneau, la somme exacte vaut (2/π)arctan(2r sin θ/(1−r²)).',
                   'Quand r→1−, le noyau se concentre et restitue le signal aux points continus, et la demi-somme aux sauts. La convergence n’est pas uniforme pour un créneau discontinu.'],
                  ['0≤r<1 dans ce laboratoire ; T est en secondes et θ=2πt/T.', 'P_r est sans dimension ; le noyau de convolution périodique P_r/T a l’unité s⁻¹ et la masse 1.', 'Les métriques de masse et de reste sont analytiques : une grille ne suffit pas à contrôler un noyau qui devient très étroit.'])


CALCULATORS = {'rc_reponses': _rc, 'rc_bode': _bode, 'rlc_poles': _rlc, 'dirichlet_abel': _dirichlet,
               'porte_sinc': _porte, 'gaussienne': _gaussian, 'convolution_portes': _convolution,
               'gibbs_fourier': _gibbs, 'parseval_spectre': _parseval, 'poisson_noyau': _poisson}


def calculate(lab_id, params):
    try: calculator = CALCULATORS[lab_id]
    except KeyError as exc: raise ValueError('Laboratoire de transformées inconnu.') from exc
    return clean(calculator(params))
