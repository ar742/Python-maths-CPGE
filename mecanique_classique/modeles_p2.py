"""Calculs P2. NumPy et bibliothèque standard ; unités précisées dans chaque labo."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, result, integrate

G = 9.81
U = 1.66053906660e-27
C = 299792458.0
EARTH_RATE = 2 * math.pi / 86164.0905
_GAUSS_X, _GAUSS_W = np.polynomial.legendre.leggauss(96)

def quadrature(f, lo, hi):
    x = (hi + lo) / 2 + (hi - lo) / 2 * _GAUSS_X
    return float((hi - lo) / 2 * np.dot(_GAUSS_W, f(x)))

def pendulum_period(angle, length=1.0):
    """Période exacte pour un lâcher sans vitesse, 0 <= angle < pi."""
    modulus = math.sin(angle / 2)
    return 4 * math.sqrt(length / G) * quadrature(lambda x: 1 / np.sqrt(1 - modulus**2 * np.sin(x)**2), 0, math.pi / 2)

def verlet(acceleration, x0, tmax, steps=3200):
    t = np.linspace(0, tmax, steps + 1)
    h = t[1] - t[0]
    x = np.empty(steps + 1); v = np.empty(steps + 1)
    x[0] = x0; v[0] = 0.0
    a = acceleration(x0)
    for i in range(steps):
        x[i + 1] = x[i] + h * v[i] + .5 * h * h * a
        anew = acceleration(x[i + 1])
        v[i + 1] = v[i] + .5 * h * (a + anew)
        a = anew
    return t, x, v

def energy_error(energy):
    reference = max(abs(float(energy[0])), 1e-300)
    return float(np.max(np.abs(energy - energy[0])) / reference)

def measured_period(t, x):
    """Deux passages par zéro dans le même sens, interpolation linéaire."""
    indices = np.where((x[:-1] >= 0) & (x[1:] < 0))[0]
    if len(indices) < 2:
        return None
    crossings = t[indices] + (t[indices + 1] - t[indices]) * x[indices] / (x[indices] - x[indices + 1])
    return float(np.mean(np.diff(crossings)))

def chaine_atomique(p):
    n = int(p['N']); q = int(p['q']) % n
    m, k, spacing, amplitude = (float(p[key]) for key in ('m', 'k', 'a', 'A'))
    modes = np.arange(n); wave_numbers = 2 * np.pi * modes / n
    omega = 2 * np.sqrt(k / m) * np.abs(np.sin(wave_numbers / 2))
    tscale = 2 * math.pi / (omega[q] if q else 2 * math.sqrt(k / m))
    t = np.linspace(0, 3 * tscale, 481)
    phase = wave_numbers[q] * np.arange(n)
    if p['excitation'] == 'traveling':
        u = amplitude * np.cos(phase[None, :] - omega[q] * t[:, None])
        v = amplitude * omega[q] * np.sin(phase[None, :] - omega[q] * t[:, None])
    elif p['excitation'] == 'local':
        initial = np.zeros(n); initial[0] = amplitude
        coefficients = np.fft.fft(initial)
        u = np.fft.ifft(coefficients[None, :] * np.cos(t[:, None] * omega), axis=1).real
        v = np.fft.ifft(-coefficients[None, :] * omega * np.sin(t[:, None] * omega), axis=1).real
    else:
        u = amplitude * np.cos(t[:, None] * omega[q]) * np.cos(phase)
        v = -amplitude * omega[q] * np.sin(t[:, None] * omega[q]) * np.cos(phase)
    energy = .5 * m * np.sum(v*v, axis=1) + .5 * k * np.sum((np.roll(u, -1, axis=1) - u)**2, axis=1)
    qa = np.linspace(-math.pi, math.pi, 401)
    chosen_qa = min(wave_numbers[q], 2 * math.pi - wave_numbers[q])
    linear = math.sqrt(k/m) * chosen_qa
    discrepancy = 0.0 if not linear else 100 * (linear - omega[q]) / linear
    return result(
        [metric('Indice effectif du mode', q), metric('Pulsation du mode choisi', float(omega[q]), 'rad/s'), metric('Vitesse des ondes de grande longueur d’onde', spacing*math.sqrt(k/m), 'm/s'),
         metric('Écart à la dispersion linéaire pour ce mode', discrepancy, '%'), metric('Variation relative maximale de l’énergie', energy_error(energy) if energy[0] else 0)],
        [chart('Déplacements de six masses au plus', 'Temps (s)', 'Déplacement (m)', *[series(f'Masse {j}', t, u[:, j]) for j in range(min(n, 6))]),
         chart('Profil initial et profil après une période de référence', 'Indice de la masse', 'Déplacement (m)', series('Au départ', np.arange(n), u[0]), series('À t ≈ T', np.arange(n), u[160])),
         chart('Dispersion : la chaîne devient-elle une corde ?', 'Nombre d’onde réduit κa (rad)', 'Pulsation (rad/s)', series('Chaîne exacte', qa, 2*math.sqrt(k/m)*np.abs(np.sin(qa/2))), series('Milieu continu : c |κ|', qa, math.sqrt(k/m)*np.abs(qa))),
         chart('Énergie totale', 'Temps (s)', 'Énergie (J)', series('Cinétique + élastique', t, energy))],
        dict(kind='chain', title='Une cellule périodique de N masses', description='La dernière masse est reliée à la première. Le déplacement est longitudinal ; le rail est une représentation de la cellule, sans dessiner sa fermeture.', positions=(spacing*np.arange(n)[None, :] + u)[::3], eq_positions=spacing*np.arange(n)),
        ['Noter uⱼ l’écart à la position au repos ja. Le bilan des deux forces donne m üⱼ = k(uⱼ₊₁ + uⱼ₋₁ − 2uⱼ), avec les indices pris modulo N.',
         'Chercher uⱼ = Re(U eⁱ⁽κja−ωt⁾). La périodicité impose κa = 2πq/N ; l’équation donne ω² = (4k/m) sin²(κa/2).',
         'Pour |κa| petit, sin(κa/2) ≈ κa/2 : ω ≈ c|κ|, avec c = a√(k/m). L’écart affiché compare ces deux pulsations pour le mode choisi.',
         'Une préparation locale n’est pas un mode propre : la transformée de Fourier discrète la décompose en N modes, dont les phases évoluent différemment. La somme de leurs solutions est ici calculée exactement.'],
        ['Ressorts linéaires et identiques, masses identiques, absence de dissipation ; seule la vibration longitudinale est modélisée.',
         'q est ramené modulo N ; q et N−q ont la même pulsation. Le mode q = 0 est une translation, sans force de rappel.',
         'Les valeurs en kg et N/m représentent une maquette. Le passage à un réseau atomique demande des masses, des raideurs et des espacements microscopiques.'])

def co2_modes(mo, mc, stiffness):
    masses = np.array([mo, mc, mo])
    matrix = stiffness * np.array([[1., -1., 0.], [-1., 2., -1.], [0., -1., 1.]])
    rootmass = np.sqrt(masses)
    dynamical = matrix / rootmass[:, None] / rootmass[None, :]
    eigenvalues, orthogonal = np.linalg.eigh(dynamical)
    eigenvalues = np.maximum(eigenvalues, 0)
    eigenvalues[0] = 0.0  # translation : noyau connu exactement
    return masses, matrix, np.sqrt(eigenvalues), orthogonal / rootmass[:, None]

def molecule_co2(p):
    masses, stiffness, omega, eigenvectors = co2_modes(float(p['mO'])*U, float(p['mC'])*U, float(p['k']))
    amplitude = float(p['A'])*1e-12
    vectors = eigenvectors / np.max(np.abs(eigenvectors), axis=0)
    factors = {'oxygen': [0, 1, 0], 'carbon': [0, 0, 1], 'mix': [0, .5, .5], 'translation': [1, 0, 0]}[p['mode']]
    t = np.linspace(0, 4*2*math.pi/omega[1], 721)
    coefficients = amplitude * np.array(factors)
    x = (np.cos(t[:, None]*omega) * coefficients) @ vectors.T
    v = (-np.sin(t[:, None]*omega) * coefficients * omega) @ vectors.T
    energy = .5*np.sum(masses*v*v, axis=1) + .5*np.einsum('ti,ij,tj->t', x, stiffness, x)
    shape = vectors[:, 1:]
    gram = eigenvectors.T @ (masses[:, None] * eigenvectors)
    residual = np.linalg.norm(stiffness @ eigenvectors - masses[:, None]*eigenvectors*omega**2) / max(np.linalg.norm(stiffness @ eigenvectors), 1e-300)
    wavenumber = omega / (2*math.pi*C*100)
    return result(
        [metric('Fréquence : oxygènes opposés', omega[1]/(2*math.pi*1e12), 'THz'), metric('Fréquence : carbone mobile', omega[2]/(2*math.pi*1e12), 'THz'),
         metric('Nombre d’onde spectroscopique du premier mode', wavenumber[1], 'cm⁻¹'), metric('Nombre d’onde spectroscopique du second mode', wavenumber[2], 'cm⁻¹'),
         metric('Résidu relatif des équations de modes', float(residual)), metric('Défaut maximal d’orthonormalité pondérée', float(np.max(np.abs(gram-np.eye(3)))))],
        [chart('Déplacements atomiques', 'Temps (fs)', 'Écart à l’équilibre (pm)', *[series(name, t*1e15, x[:, j]*1e12) for j, name in enumerate(['O gauche', 'C', 'O droit'])]),
         chart('Forme des deux modes vibratoires', 'Atome : 0 = O, 1 = C, 2 = O', 'Déplacement normalisé', series('Oxygènes opposés', np.arange(3), shape[:, 0]), series('Carbone opposé', np.arange(3), shape[:, 1])),
         chart('Énergie mécanique', 'Temps (fs)', 'Énergie (J)', series('Énergie totale', t*1e15, energy))],
        dict(kind='chain', title='Une molécule linéaire O–C–O', description='Les déplacements sont amplifiés pour distinguer les modes ; l’espacement dessiné est symbolique. Les coordonnées de la scène sont en pm.', positions=(np.array([0., 120., 240.])[None, :] + 4*x/1e-12)[::4], eq_positions=[0, 120, 240]),
        ['Écrire T = ½ Ẋᵀ M Ẋ et V = ½ Xᵀ K X, avec M = diag(mO,mC,mO) et K = k[[1,−1,0],[−1,2,−1],[0,−1,1]]. Les équations sont M Ẍ + K X = 0.',
         'Pour un mode X = a cos(ωt), résoudre K a = ω² M a. La matrice M⁻¹ᐟ² K M⁻¹ᐟ² est symétrique : sa diagonalisation fournit les trois pulsations et des modes orthogonaux pour le produit scalaire aᵀ M b.',
         'Le noyau est engendré par (1,1,1) : il décrit une translation longitudinale. Les deux vibrations ont ω₁² = k/mO et ω₂² = k/mO + 2k/mC ; leurs formes sont (1,0,−1) et (1,−2mO/mC,1), à un facteur près.',
         'Changer un isotope modifie M sans changer ici K. Les fréquences déplacées illustrent le lien avec un spectre ; le modèle ne calcule pas l’intensité des raies ni les règles de sélection infrarouge.'],
        ['Vibrations longitudinales de faible amplitude, deux liaisons harmoniques de même raideur ; ni flexion, ni rotation, ni interaction entre molécules.',
         'u = 1,66053906660 × 10⁻²⁷ kg ; 1 pm = 10⁻¹² m ; le nombre d’onde spectroscopique est ν/c, exprimé en cm⁻¹.',
         'Le facteur de normalisation des vecteurs propres est arbitraire. Leur orthogonalité physique se mesure avec M, et non avec le produit scalaire usuel des déplacements.'])

def foucault_solution(t, length, latitude, amplitude):
    rotation = EARTH_RATE * math.sin(math.radians(latitude))
    omega0 = math.sqrt(G/length)
    nu = math.sqrt(omega0**2 + rotation**2)
    z = amplitude*np.exp(-1j*rotation*t)*(np.cos(nu*t)+1j*rotation/nu*np.sin(nu*t))
    return z, rotation, omega0, nu

def foucault(p):
    length, latitude, amplitude, hours = (float(p[key]) for key in ('L', 'latitude', 'A', 'hours'))
    _, rotation, omega0, nu = foucault_solution(np.array([0.]), length, latitude, amplitude)
    slow = np.linspace(0, hours, 241)
    colors = [(0, 'Au début'), (.5, 'À mi-parcours'), (1, 'À la fin')]
    paths=[]; curves=[]
    for fraction, label in colors:
        t = fraction*hours*3600 + np.linspace(0, 12*2*math.pi/nu, 1201)
        z, *_ = foucault_solution(t, length, latitude, amplitude)
        paths.append(dict(label=label, x=z.real[::4], y=z.imag[::4]))
        curves.append(series(label, z.real, z.imag))
    tfast = np.linspace(0, 5*2*math.pi/nu, 601)
    zfast, *_ = foucault_solution(tfast, length, latitude, amplitude)
    return result(
        [metric('Période de l’oscillation rapide', 2*math.pi/nu, 's'), metric('Vitesse de précession Ω', rotation, 'rad/s'),
         metric('Rotation orientée de la direction pendant l’observation', -math.degrees(rotation*hours*3600), '°'),
         metric('Durée d’un tour complet de la direction', 2*math.pi/abs(rotation)/3600 if abs(rotation)>1e-16 else 'Aucune précession', 'h'),
         metric('Rapport |Ω|/ω₀', abs(rotation)/omega0), metric('Rapport A/L : validité du petit angle', amplitude/length)],
        [chart('Trois courts enregistrements dans le plan horizontal', 'x (m)', 'y (m)', *curves, equal=True),
         chart('Rotation lente de la direction de l’oscillation', 'Temps depuis le début (h)', 'Angle orienté (°)', series('Direction repérée en continu', slow, -rotation*slow*3600*180/math.pi)),
         chart('Les premières oscillations', 'Temps (s)', 'Déplacement (m)', series('x', tfast, zfast.real), series('y', tfast, zfast.imag))],
        dict(kind='trajectory', title='Le plan d’oscillation change de direction', description='Chaque trace ne dure qu’une douzaine d’oscillations. Comparer leur orientation ; les heures séparant les traces ne sont pas représentées par des oscillations sous-échantillonnées.', paths=paths, bodies=[]),
        ['Dans le référentiel terrestre, aux petits angles : ẍ + ω₀²x = 2Ωẏ et ÿ + ω₀²y = −2Ωẋ, où ω₀² = g/L et Ω = ΩTerre sin λ. La pesanteur effective inclut déjà l’effet centrifuge stationnaire.',
         'Poser z = x + iy : z̈ + 2iΩż + ω₀²z = 0. En écrivant z = e⁻ⁱΩᵗ w(t), on obtient ẅ + (ω₀² + Ω²)w = 0 : le facteur lent décrit la rotation de la direction, w l’oscillation rapide.',
         'Pour z(0) = A et ż(0) = 0, w(t) = A[cos(νt) + i(Ω/ν)sin(νt)], avec ν = √(ω₀²+Ω²). Au nord, la direction tourne dans le sens négatif de l’angle choisi ; au sud, le sens s’inverse.',
         'À l’équateur Ω = 0 : aucune précession dans ce modèle. Aux pôles la durée d’un tour est un jour sidéral ; ailleurs elle vaut un jour sidéral / |sin λ|. La direction d’une droite est équivalente modulo 180°, mais le graphe suit son angle en continu.'],
        ['Approximation linéaire des petits déplacements A/L ; amplitude assez faible pour négliger les effets d’un pendule sphérique à grande amplitude.',
         'Rotation uniforme de la Terre : jour sidéral de 86164,0905 s. Ni frottements, ni excitation d’entretien, ni variation de g avec la latitude.',
         'Les traces rapides sont calculées avec une solution analytique, et non avec un pas de temps de plusieurs minutes ; cela évite de faire apparaître un faux mouvement par sous-échantillonnage.'])

def pendule_exact(p):
    angle, length, cycles = math.radians(float(p['angle'])), float(p['L']), int(p['cycles'])
    period = pendulum_period(angle, length); linear_period = 2*math.pi*math.sqrt(length/G)
    t, theta, velocity = verlet(lambda x: -G/length*math.sin(x), angle, cycles*period, cycles*800)
    harmonic = angle*np.cos(math.sqrt(G/length)*t)
    e = .5*length**2*velocity**2 + G*length*(1-np.cos(theta))
    measured = measured_period(t, theta)
    angles = np.linspace(-math.pi, math.pi, 301)
    return result(
        [metric('Période obtenue par conservation de l’énergie', period, 's'), metric('Période du modèle linéaire', linear_period, 's'),
         metric('Allongement relatif de la période', 100*(period/linear_period-1), '%'), metric('Période mesurée sur la trajectoire', measured if measured is not None else 'Observation trop courte', 's'),
         metric('Variation relative maximale de l’énergie numérique', energy_error(e))],
        [chart('Le pendule suit-il encore une sinusoïde ?', 'Temps (s)', 'Angle (°)', series('Équation exacte', t[::3], np.degrees(theta[::3])), series('Petit angle', t[::3], np.degrees(harmonic[::3]))),
         chart('Portrait de phase', 'Angle θ (rad)', 'Vitesse angulaire θ̇ (rad/s)', series('Orbite', theta[::3], velocity[::3])),
         chart('Conservation de l’énergie, par unité de masse', 'Temps (s)', 'Énergie spécifique (J/kg)', series('Énergie totale', t[::3], e[::3])),
         chart('Le potentiel et le niveau d’énergie du lâcher', 'Angle θ (rad)', 'Énergie spécifique (J/kg)', series('gL(1−cos θ)', angles, G*length*(1-np.cos(angles))), series('Énergie initiale', angles, np.full_like(angles, e[0])))],
        dict(kind='pendulum', title='Pendule simple, angle compté depuis la verticale', description='La boule est lâchée sans vitesse. L’animation suit l’équation avec sin θ ; la liaison conserve sa longueur. Au-delà de 90°, elle représente une tige rigide, et non un fil.', theta=theta[::max(1, len(theta)//240)], length=length),
        ['Le moment du poids autour du point d’attache donne mL²θ̈ = −mgL sin θ, donc θ̈ + (g/L) sin θ = 0. La masse disparaît de cette équation.',
         'L’énergie par unité de masse vaut ½L²θ̇² + gL(1−cos θ). Au lâcher θ = θₘ et θ̇ = 0 ; la vitesse en chaque position se déduit de cette conservation.',
         'Le quart de période est une intégrale de dθ/|θ̇|. Le changement de variable sin(θ/2) = sin(θₘ/2) sin φ conduit à T = 4√(L/g) ∫₀^{π/2} [1−sin²(θₘ/2) sin²φ]⁻¹ᐟ² dφ.',
         'Une quadrature de Gauss à 96 points calcule cette intégrale. La trajectoire utilise Verlet à 800 pas par période ; la variation d’énergie affichée contrôle l’erreur de cette seconde méthode. Quand θₘ → π, le sommet est approché de plus en plus lentement et T diverge.'],
        ['Pendule ponctuel, liaison sans masse et de longueur constante, mouvement plan, pas de frottement ; g = 9,81 m/s². Une tige rigide est requise pour un lâcher au-delà de 90° ; un fil aurait une tension initiale négative.',
         'Le lâcher reste dans 0 < θₘ < π : on étudie des oscillations et non des rotations complètes.',
         'La période mesurée demande deux passages descendants par θ = 0 ; avec une seule période affichée, cette mesure n’est pas disponible.'])

def pendule_anharmonique(p):
    amplitude, length = math.radians(float(p['angle'])), float(p['L'])
    omega0 = math.sqrt(G/length); exact_period = pendulum_period(amplitude, length)
    t, exact, ve = verlet(lambda x: -omega0**2*math.sin(x), amplitude, 4*exact_period, 3200)
    _, cubic, vc = verlet(lambda x: -omega0**2*(x-x**3/6), amplitude, 4*exact_period, 3200)
    omega_approx = omega0*(1-amplitude**2/16)
    corrected = amplitude*((1+amplitude**2/192)*np.cos(omega_approx*t) - amplitude**2/192*np.cos(3*omega_approx*t))
    harmonics = np.arange(1, 10, 2)
    phase = 2*math.pi*t/exact_period
    basis = np.column_stack([np.ones_like(t), *[np.cos(j*phase) for j in harmonics], *[np.sin(j*phase) for j in harmonics]])
    coefficients = np.linalg.lstsq(basis, exact, rcond=None)[0]
    amplitudes = np.hypot(coefficients[1:6], coefficients[6:11])
    relative_amplitudes = amplitudes/amplitudes[0]
    visible_harmonics = relative_amplitudes >= 1e-5
    predicted = amplitude**2/192/(1+amplitude**2/192)
    sweep = np.linspace(0, 120, 81); exact_sweep = np.array([pendulum_period(math.radians(a), length) for a in sweep])
    linear_period = 2*math.pi/omega0
    cubic_period = measured_period(t, cubic)
    e = .5*length**2*ve**2 + G*length*(1-np.cos(exact))
    return result(
        [metric('Période exacte', exact_period, 's'), metric('Période à l’ordre θₘ²', linear_period*(1+amplitude**2/16), 's'),
         metric('Période du modèle avec rappel cubique', cubic_period, 's'), metric('Rapport mesuré troisième / première harmonique', float(amplitudes[1]/amplitudes[0])),
         metric('Rapport prévu au premier ordre utile', predicted), metric('Variation relative de l’énergie du calcul exact', energy_error(e))],
        [chart('Trois modèles, mêmes conditions initiales', 'Temps (s)', 'Angle θ (rad)', series('sin θ exact', t[::4], exact[::4]), series('θ−θ³/6', t[::4], cubic[::4]), series('Correction perturbative', t[::4], corrected[::4])),
         chart('Harmoniques impaires : amplitudes en échelle logarithmique', 'Rang de l’harmonique', 'Amplitude / amplitude fondamentale', series('Mesure : rapports ≥ 10⁻⁵', harmonics[visible_harmonics], relative_amplitudes[visible_harmonics]), series('Prévision avec rangs 1 et 3', [1, 3], [1, predicted]), y_scale='log'),
         chart('La correction de période résiste-t-elle à une grande amplitude ?', 'Amplitude maximale (°)', 'Période (s)', series('Exacte', sweep, exact_sweep), series('T₀(1+θₘ²/16)', sweep, linear_period*(1+np.radians(sweep)**2/16)), series('T₀', sweep, np.full_like(sweep, linear_period))),
         chart('Portrait de phase : exact et développement cubique', 'θ (rad)', 'θ̇ (rad/s)', series('Exact', exact[::4], ve[::4]), series('Rappel cubique', cubic[::4], vc[::4]))],
        dict(kind='pendulum', title='Le pendule réel de l’expérience', description='L’animation suit sin θ. Les développements sont comparés dans les graphiques, avec la même amplitude au point de rebroussement.', theta=exact[::14], length=length),
        ['Développer V = mgL(1−cos θ) = mgL(θ²/2 − θ⁴/24 + …). En dérivant V, le premier écart au rappel linéaire est θ̈ + ω₀²(θ−θ³/6) = 0.',
         'Pour éviter qu’une correction de phase croisse artificiellement avec le temps, corriger aussi la pulsation : Ω ≈ ω₀(1−θₘ²/16). Ainsi T ≈ T₀(1+θₘ²/16), à l’ordre θₘ².',
         'Avec θₘ défini comme l’angle maximal, la solution approchée s’écrit θ ≈ θₘ[(1+θₘ²/192)cos(Ωt) − (θₘ²/192)cos(3Ωt)]. Elle vérifie θ(0)=θₘ et θ̇(0)=0. La convention d’amplitude explique le coefficient de la fondamentale.',
         'Projeter le signal exact sur cos(jωt) et sin(jωt), sur quatre périodes exactes. Les amplitudes mesurées aux rangs 1,3,5,… rendent visible l’apparition de nouvelles harmoniques ; le rapport du rang 3 commence comme θₘ²/192.',
         'Le potentiel quartique tronqué est un modèle local. Il n’est pas borné inférieurement pour des angles arbitrairement grands : on l’utilise ici sous 80°, loin de cette extrapolation non physique.'],
        ['θₘ est l’amplitude au point de rebroussement, exprimée en radians dans les développements ; les valeurs en degrés ne doivent pas être substituées dans θₘ².',
         'Sans dissipation, les spectres sont ceux d’un mouvement périodique. Les coefficients sont obtenus par moindres carrés, et non par une FFT avec une fréquence fondamentale arrondie.',
         'L’échelle logarithmique rend la troisième harmonique visible malgré sa faible amplitude. Les rapports inférieurs à 10⁻⁵ ne sont pas tracés : à ces niveaux, l’erreur de discrétisation et l’ajustement peuvent dominer. Ce seuil de lecture n’est pas une borne rigoureuse de l’erreur ; les zéros de la prévision aux rangs supérieurs à 3 ne sont pas représentés sur une échelle logarithmique.',
         'Les méthodes perturbatives et l’analyse harmonique détaillée prolongent le cours CPGE. Le développement limité, la force −dV/dθ et la conservation de l’énergie sont les points d’appui.'])

def spring_potential(x, length, rest, stiffness):
    return stiffness*(np.hypot(x, length)-rest)**2

def spring_force(x, length, rest, stiffness):
    return -2*stiffness*(1-rest/math.hypot(x, length))*x

def ressorts_transverses(p):
    ratio, rest, stiffness, mass, offset = (float(p[key]) for key in ('rho','L0','k','m','A'))
    length = ratio*rest
    equilibrium = math.sqrt(max(0, rest**2-length**2)) if p['origin']=='well' else 0.0
    initial = equilibrium+offset*rest
    tscale = 2*math.pi*math.sqrt(mass/(2*stiffness))
    t, x, v = verlet(lambda u: spring_force(u, length, rest, stiffness)/mass, initial, 10*tscale, 6000)
    energy = .5*mass*v*v + spring_potential(x, length, rest, stiffness)
    barrier = spring_potential(0, length, rest, stiffness)
    axis = np.linspace(-1.8*rest, 1.8*rest, 501)
    quartic = stiffness*(length-rest)**2 + stiffness*(1-rest/length)*axis**2 + stiffness*rest/(4*length**3)*axis**4
    below = np.linspace(.4, 1, 161); above=np.linspace(1, 1.6, 101)
    root = np.sqrt(1-below**2)
    stable = math.sqrt(max(0, rest**2-length**2))
    curvature = 2*stiffness*(1-rest*length**2/(stable**2+length**2)**1.5)
    movement = 'Deux puits, passage possible par le centre' if ratio<1 and energy[0]>barrier else ('Deux puits, masse confinée dans un puits' if ratio<1 else 'Un puits central')
    return result(
        [metric('Équilibres stables : positions ±xₑ si L < L₀', stable, 'm'), metric('Courbure V″ à un minimum stable', curvature, 'N/m'),
         metric('Énergie du lâcher', float(energy[0]), 'J'), metric('Énergie au centre', float(barrier), 'J'), metric('Type de mouvement permis par l’énergie', movement), metric('Variation relative maximale de l’énergie', energy_error(energy))],
        [chart('Mouvement sur le rail', 'Temps (s)', 'Position x (m)', series('Masse', t[::6], x[::6])),
         chart('Potentiel exact, développement local et énergie du lâcher', 'x (m)', 'Énergie (J)', series('Exact', axis, spring_potential(axis,length,rest,stiffness)), series('Développement en x à l’ordre 4', axis, quartic), series('Énergie totale', axis, np.full_like(axis,energy[0]))),
         chart('Les équilibres quand on change L/L₀', 'Rapport L/L₀', 'Position d’équilibre / L₀', series('Stable : branche positive', below, root), series('Stable : branche négative', below, -root), series('Stable au centre', above, np.zeros_like(above)), series('Instable au centre', below, np.zeros_like(below))),
         chart('Portrait de phase', 'x (m)', 'Vitesse (m/s)', series('Orbite', x[::6], v[::6]))],
        dict(kind='oscillator', title='Masse sur un rail : déplacement transversal aux attaches', description=f'Les attaches sont à (0,+L) et (0,−L), avec L={length:.3g} m. Chaque ressort mesure √(x²+L²) ; le potentiel additionne leurs deux énergies.', x=x[::25]),
        ['La longueur de chaque ressort est ℓ(x)=√(x²+L²). Deux énergies ½k(ℓ−L₀)² donnent V(x)=k(√(x²+L²)−L₀)².',
         'Projeter la force sur le rail ou dériver V : m ẍ = −V′(x) = −2k[1−L₀/√(x²+L²)]x. La loi de Hooke reste linéaire en allongement ; la géométrie rend la force en x non linéaire.',
         'V′=0 donne x=0 et, si L<L₀, x=±√(L₀²−L²). Au centre V″(0)=2k(1−L₀/L) : positif pour L>L₀, négatif pour L<L₀. À L=L₀, le terme quadratique s’annule mais le terme quartique est positif.',
         'Comparer l’énergie du lâcher à V(0). En dessous de la barrière, une masse préparée à droite ne peut atteindre x=0. Au-dessus, elle peut traverser les deux puits ; au niveau exact de la barrière, l’approche du centre est asymptotique.',
         'Le portrait de phase et la conservation de l’énergie contrôlent l’intégration de Verlet. La courbe quartique sert à tester un développement autour de x=0 : elle peut s’éloigner nettement du potentiel exact quand |x|/L n’est plus petit.'],
        ['Les ressorts peuvent être comprimés ou allongés ; un fil élastique qui ne transmettrait aucune compression serait un autre modèle.',
         'Rail sans frottement, géométrie parfaitement symétrique ; le poids et la réaction du rail ne travaillent pas selon x.',
         'Le temps de référence utilisé pour la durée du calcul est 2π√(m/2k). Ce n’est pas la période physique, surtout près du seuil ou de la barrière.'])

def quartic_period(amplitude, mass, beta):
    integral = quadrature(lambda phi: 1/np.sqrt(1+np.sin(phi)**2), 0, math.pi/2)
    return 4*math.sqrt(2*mass/beta)*integral/amplitude

def threshold_spring_period(amplitude, mass, stiffness, rest):
    rA=math.hypot(amplitude,rest)
    def integrand(phi):
        x=amplitude*np.sin(phi); r=np.hypot(x,rest)
        increments=amplitude**2/(rA+rest)+x*x/(r+rest)
        return np.sqrt((rA+r)/(stiffness*increments))
    return 4*math.sqrt(mass/2)*quadrature(integrand,0,math.pi/2)

def oscillateur_quartique(p):
    rest, stiffness, mass = (float(p[key]) for key in ('L0','k','m'))
    amplitude = float(p['A'])*rest; beta=stiffness/rest**2
    period=quartic_period(amplitude,mass,beta); exact_period=threshold_spring_period(amplitude,mass,stiffness,rest)
    t,x,v=verlet(lambda u:-beta*u**3/mass,amplitude,3*period,3000)
    _,exact,_=verlet(lambda u:spring_force(u,rest,rest,stiffness)/mass,amplitude,3*period,3000)
    energy=.5*mass*v*v+beta*x**4/4
    sweep=np.linspace(.02,.9,101)*rest
    quarticT=np.array([quartic_period(a,mass,beta) for a in sweep]); springT=np.array([threshold_spring_period(a,mass,stiffness,rest) for a in sweep])
    axis=np.linspace(-1.2*amplitude,1.2*amplitude,301)
    return result(
        [metric('Coefficient du rappel cubique β=k/L₀²',beta,'N/m³'),metric('Période du potentiel quartique',period,'s'),metric('Période des ressorts exacts au seuil',exact_period,'s'),
         metric('Écart relatif des deux périodes',100*(exact_period/period-1),'%'),metric('Produit T×A du modèle quartique',period*amplitude,'m·s'),metric('Variation relative maximale de l’énergie quartique',energy_error(energy))],
        [chart('Deux modèles préparés à la même amplitude', 'Temps (s)', 'Position (m)',series('V=βx⁴/4',t[::4],x[::4]),series('Ressorts exacts avec L=L₀',t[::4],exact[::4])),
         chart('La période dépend fortement de l’amplitude', 'Amplitude A/L₀','Période (s)',series('Quartique : proportionnelle à 1/A',sweep/rest,quarticT),series('Ressorts exacts au seuil',sweep/rest,springT)),
         chart('Potentiel : le premier terme non nul est quartique', 'x (m)','Énergie (J)',series('βx⁴/4',axis,beta*axis**4/4),series('Ressorts exacts',axis,spring_potential(axis,rest,rest,stiffness))),
         chart('Portrait de phase du modèle quartique', 'x (m)', 'Vitesse (m/s)',series('Orbite',x[::4],v[::4]))],
        dict(kind='oscillator',title='Un centre stable sans pulsation linéaire non nulle',description='Le mouvement animé suit m ẍ=−βx³. Diminuer l’amplitude ralentit les oscillations ; le temps affiché couvre trois périodes de ce modèle.',x=x[::13]),
        ['Au seuil L=L₀, √(L₀²+x²)−L₀ = x²/(2L₀) + O(x⁴). Le potentiel exact des deux ressorts devient V(x)=kx⁴/(4L₀²)+O(x⁶), soit V≈βx⁴/4 avec β=k/L₀².',
         'L’équilibre x=0 est stable car V y possède un minimum strict, même si V″(0)=0. La linéarisation ẍ=0 ne permet donc pas de calculer une fréquence d’oscillation : il faut conserver le terme cubique de la force.',
         'Au lâcher x=A et ẋ=0, E=βA⁴/4. La conservation de l’énergie donne T=4√(2m/β) A⁻¹ ∫₀¹ du/√(1−u⁴). Le changement u=sin φ rend l’intégrale régulière : ∫₀^{π/2} dφ/√(1+sin²φ).',
         'La variable réduite u=x/A et le temps τ=A√(β/m)t ramènent tous les mouvements quartiques à u″+u³=0. La dépendance T∝1/A est une conséquence exacte de ce changement d’échelle.',
         'Une seconde quadrature calcule la période du potentiel exact des ressorts. Comparer ces périodes permet de mesurer l’erreur du développement local, au lieu de l’attribuer à l’intégration numérique.'],
        ['Le potentiel quartique pur définit un modèle valable en lui-même ; son interprétation comme approximation des ressorts demande |x|/L₀ petit.',
         'L’amplitude est strictement positive. À A=0 la masse reste au centre ; la limite des périodes quand A→0 est infinie.',
         'Gauss à 96 points pour les périodes, Verlet à 1000 pas par période quartique pour les trajectoires. La variation d’énergie affichée contrôle cette intégration.'])

def duffing_harmonic_roots(ratio,beta,damping,forcing):
    """Amplitudes positives de la balance harmonique, pas une preuve de stabilité."""
    delta=1-ratio*ratio; cubic=.75*beta; loss=2*damping*ratio
    if beta==0:
        return [forcing/math.hypot(delta,loss)]
    polynomial=[cubic*cubic,2*cubic*delta,delta*delta+loss*loss,-forcing*forcing]
    roots=np.roots(polynomial)
    return sorted(math.sqrt(float(z.real)) for z in roots if abs(z.imag)<1e-8*max(1,abs(z.real)) and z.real>0)

def duffing_trajectory(beta,damping,forcing,ratio,initial,cycles):
    steps=cycles*160
    t=np.linspace(0,cycles*2*math.pi/ratio,steps+1); h=t[1]-t[0]
    x=np.empty(steps+1);v=np.empty(steps+1);x[0]=initial;v[0]=0
    def accel(time,u,speed):
        return forcing*math.cos(ratio*time)-2*damping*speed-u-beta*u**3
    for i in range(steps):
        a1=accel(t[i],x[i],v[i]); k1=v[i]
        k2=v[i]+h*a1/2; a2=accel(t[i]+h/2,x[i]+h*k1/2,k2)
        k3=v[i]+h*a2/2; a3=accel(t[i]+h/2,x[i]+h*k2/2,k3)
        k4=v[i]+h*a3; a4=accel(t[i]+h,x[i]+h*k3,k4)
        x[i+1]=x[i]+h*(k1+2*k2+2*k3+k4)/6
        v[i+1]=v[i]+h*(a1+2*a2+2*a3+a4)/6
    return t,x,v

def fundamental(t,x,ratio):
    columns=np.column_stack((np.cos(ratio*t),np.sin(ratio*t),np.ones_like(t)))
    c=np.linalg.lstsq(columns,x,rcond=None)[0]
    return float(math.hypot(c[0],c[1]))

def duffing_force(p):
    beta,damping,forcing,ratio,initial=(float(p[key]) for key in ('beta','zeta','force','ratio','initial'))
    cycles=int(p['cycles']);t,x,v=duffing_trajectory(beta,damping,forcing,ratio,initial,cycles)
    last=slice(-1601,None); before=slice(-3201,-1600)
    amplitude=fundamental(t[last],x[last],ratio); previous=fundamental(t[before],x[before],ratio)
    energy=.5*v*v+.5*x*x+beta*x**4/4
    injected=forcing*np.cos(ratio*t)*v; dissipated=2*damping*v*v
    total_work=integrate(injected-dissipated,t)
    balance_error=abs(float(energy[-1]-energy[0]-total_work))/max(float(integrate(abs(injected)+dissipated,t)),1e-15)
    roots=duffing_harmonic_roots(ratio,beta,damping,forcing)
    sweep=np.linspace(.5,1.8,261)
    allroots=[duffing_harmonic_roots(r,beta,damping,forcing) for r in sweep]
    response=[]
    for index in range(3):
        segment_x=[]; segment_y=[]
        def flush():
            if segment_x:
                response.append(series(f'Racine positive n°{index+1}',list(segment_x),list(segment_y)))
                segment_x.clear();segment_y.clear()
        for r, values in zip(sweep,allroots):
            if index>=len(values):
                flush();continue
            value=values[index]
            if segment_y and abs(value-segment_y[-1])>.18:
                flush()
            segment_x.append(float(r));segment_y.append(value)
        flush()
    response.append(series('Amplitude fondamentale mesurée', [ratio], [amplitude]))
    periods=t*ratio/(2*math.pi)
    return result(
        [metric('Amplitude fondamentale mesurée, dix dernières périodes',amplitude),metric('Amplitude fondamentale, dix périodes précédentes',previous),metric('Écart relatif entre les deux fenêtres',abs(amplitude-previous)/max(amplitude,1e-15)),
         metric('Nombre d’amplitudes dans l’approximation sinusoïdale',len(roots)),metric('Amplitudes approchées à la fréquence choisie',', '.join(f'{a:.4g}' for a in roots)),
         metric('Puissance injectée moyenne sur la dernière fenêtre',float(integrate(injected[last],t[last])/(t[last][-1]-t[last][0]))),metric('Puissance dissipée moyenne sur la dernière fenêtre',float(integrate(dissipated[last],t[last])/(t[last][-1]-t[last][0]))),metric('Résidu relatif du bilan énergétique intégré',balance_error)],
        [chart('Installation du mouvement forcé', 'Temps / période du forçage', 'Position réduite u',series('Trajectoire',periods[::8],x[::8])),
         chart('Portrait de phase : dix dernières périodes', 'Position réduite u', 'Vitesse du/dτ',series('Mouvement calculé',x[last][::3],v[last][::3])),
         chart('Balance harmonique : plusieurs amplitudes possibles', 'Rapport de pulsations r', 'Amplitude fondamentale approchée',*response),
         chart('Bilan instantané : apport et perte d’énergie', 'Temps / période du forçage', 'Puissance réduite',series('Force extérieure × vitesse',periods[last][::4],injected[last][::4]),series('Dissipation 2ζu′²',periods[last][::4],dissipated[last][::4]))],
        dict(kind='oscillator',title='Un oscillateur entretenu par une force périodique',description='Position et temps sont réduits. L’animation montre les dix dernières périodes calculées ; vérifier l’écart des fenêtres avant de parler de régime établi.',x=x[last][::7]),
        ['Choisir une longueur de référence xréf et τ=ω₀t, u=x/xréf. On étudie u″+2ζu′+u+βu³=f cos(rτ). Les quatre coefficients sont sans unité ; β≥0 correspond ici à un rappel durcissant.',
         'Multiplier par u′ : dE/dτ=f cos(rτ)u′−2ζu′², avec E=½u′²+½u²+βu⁴/4. Le travail de la force alimente le mouvement et la dissipation prélève de l’énergie ; le résidu du bilan intégré contrôle le calcul.',
         'Chercher approximativement u=A cos(rτ−φ), et ne conserver que la fondamentale de u³ : cos³ψ=(3cosψ+cos3ψ)/4. Il vient A²[(1−r²+3βA²/4)²+(2ζr)²]=f².',
         'Résoudre le polynôme en A². Plusieurs racines positives indiquent plusieurs réponses candidates de cette approximation ; leur stabilité, les harmoniques négligées et la réponse retenue dépendent du mouvement réel. Le graphe ne constitue pas un balayage temporel de fréquence ni une démonstration d’hystérésis.',
         'La trajectoire utilise Runge–Kutta d’ordre 4, à 160 pas par période imposée. Les amplitudes sont mesurées par projection sinusoïdale sur deux fenêtres successives de dix périodes ; un écart sensible signale un transitoire persistant ou une réponse modulée.'],
        ['Prolongement non linéaire de l’oscillateur amorti forcé du programme ; le modèle est entièrement précisé, mais l’analyse de ses bifurcations dépasse les exigences CPGE.',
         'Les racines de balance harmonique sont une approximation à une harmonique. Aucune branche n’est déclarée stable à partir de cette seule équation.',
         'Le calcul part de u(0) choisi et u′(0)=0, à fréquence fixe. La dernière fenêtre n’est dite quasi stationnaire que si les observables ont cessé d’évoluer à l’échelle de l’expérience.',
         'Les unités physiques sont récupérées avec x=xréf u et t=τ/ω₀ ; les puissances physiques valent m xréf² ω₀³ fois les puissances réduites.'])

COMPUTE = {function.__name__: function for function in [chaine_atomique,molecule_co2,foucault,pendule_exact,pendule_anharmonique,ressorts_transverses,oscillateur_quartique,duffing_force]}
