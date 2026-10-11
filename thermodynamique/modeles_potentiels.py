"""Modèles P22 : bilans signés, minima physiques et cycles explicitement calculés."""
from __future__ import annotations
import math
import numpy as np
from commun import metric, series, chart, result, integrate

R = 8.31446261815324
TM = 273.15
C_ICE = 2100.0
C_WATER = 4180.0
LATENT = 334000.0


def scene_curves(title, curves, xlabel, ylabel, description, apparatus=None, kind='curves'):
    scene = dict(kind=kind, title=title, description=description, xLabel=xlabel, yLabel=ylabel,
                 curves=[dict(label=name, x=x, y=y) for name, x, y in curves])
    if apparatus is not None:
        scene['apparatus'] = apparatus
    return scene


def cumulative_integral(y, x):
    return np.r_[0.0, np.cumsum((y[1:] + y[:-1]) / 2 * np.diff(x))]


def travail_chemins(p):
    Ti, ratio, k = p['T1'], p['ratio'], p['k']
    gamma = 1.4
    cv = R / (gamma - 1)
    Vi, Vf = R * Ti / 1e5, R * Ti / 1e5 * ratio
    Tf = Ti * ratio ** (1 - k)
    V = np.linspace(Vi, Vf, 501)
    T = Ti * (V / Vi) ** (1 - k)
    P = R * T / V
    Wp = -R * Ti * math.log(ratio) if abs(k - 1) < 1e-10 else -R * Ti * math.expm1((1 - k) * math.log(ratio)) / (1 - k)
    Wa, Wb = -R * Tf * math.log(ratio), -R * Ti * math.log(ratio)
    dU = cv * (Tf - Ti)
    dS = cv * math.log(Tf / Ti) + R * math.log(ratio)
    cumulative_W = cumulative_integral(-P, V)
    cumulative_U = cv * (T - Ti)
    paths = [('Polytrope', V * 1000, P / 1e5), ('Isochore puis isotherme finale', np.r_[Vi, V] * 1000, np.r_[R * Ti / Vi, R * Tf / V] / 1e5), ('Isotherme initiale puis isochore', np.r_[V, Vf] * 1000, np.r_[R * Ti / V, R * Tf / Vf] / 1e5)]
    out = result(
        [metric('Température finale commune T₂', Tf, 'K'), metric('ΔU commune aux trois chemins', dU, 'J'), metric('ΔS commune aux trois chemins', dS, 'J/K'),
         metric('Travail reçu : polytrope', Wp, 'J'), metric('Travail reçu : isochore puis isotherme finale', Wa, 'J'), metric('Travail reçu : isotherme initiale puis isochore', Wb, 'J'),
         metric('Chaleur reçue : polytrope', dU - Wp, 'J'), metric('Entropie créée sur les chemins réversibles', 0, 'J/K')],
        [chart('Trois chemins, les mêmes deux états', 'Volume (L)', 'Pression (bar)', *(series(name, x, y) for name, x, y in paths)),
         chart('Le bilan du chemin polytropique', 'Volume (L)', 'Énergie reçue (J)', series('W reçu, aire cumulée', V * 1000, cumulative_W), series('ΔU', V * 1000, cumulative_U), series('Q reçu = ΔU−W', V * 1000, cumulative_U - cumulative_W)),
         chart('La température dépend de la contrainte de chemin', 'Volume (L)', 'Température (K)', series('Polytrope', V * 1000, T), series('Isotherme initiale', V * 1000, np.full_like(V, Ti)), series('Isotherme finale', V * 1000, np.full_like(V, Tf)))],
        scene_curves('Le signe de W se lit avec le sens du déplacement', paths, 'V (L)', 'P (bar)', 'Les deux isochores sont les segments verticaux ; les trois courbes relient les mêmes états. W=−∫P dV est négatif pendant une détente.', dict(type='piston', initialVolume=Vi, finalVolume=Vf, initialTemperature=Ti, finalTemperature=Tf, work=Wp, heat=dU - Wp)),
        ['Pour une mole, fixer l’état initial avec P₁=1 bar et V₁=RT₁/P₁. La loi PVᵏ=constante impose T₂/T₁=(V₂/V₁)^(1−k).',
         'Calculer W=−∫P dV ; la limite k=1 donne −RT₁ ln(V₂/V₁). Pour k=γ=1,4, le bilan donne Q=0.',
         'Les deux chemins alternatifs ont les mêmes extrémités : une isochore ne fournit aucun travail, tandis que l’isotherme contribue −RT ln(V₂/V₁).',
         'Pour chaque chemin, utiliser ΔU=cV(T₂−T₁), puis Q=ΔU−W. L’entropie ΔS=cV ln(T₂/T₁)+R ln(V₂/V₁) est une fonction d’état.'],
        ['Une mole de gaz parfait, cV constant, γ=1,4 ; seuls les travaux de pression sont présents.', 'Chemins quasistatiques réversibles : les échanges thermiques sont avec des sources adaptées à chaque température, pas nécessairement avec un unique thermostat.', 'Le tracé cumulé utilise une quadrature ; les métriques de travail sont analytiques.'])
    out['table'] = dict(headers=['Chemin', 'W reçu (J)', 'Q reçu (J)', 'ΔU (J)'], rows=[['Polytrope', Wp, dU - Wp, dU], ['Isochore puis isotherme finale', Wa, dU - Wa, dU], ['Isotherme initiale puis isochore', Wb, dU - Wb, dU]])
    return out


def travaux_generalises(p):
    device, si, sf, scale = p['device'], p['initial'], p['final'], p['scale']
    settings = {
        'surface': ('Surface liquide', 'Aire A', 'm²', .01, .072 * scale, 'Tension superficielle σ', 'N/m', 1e4, 'Aire (cm²)', 'Une seule interface ; σ=0,072κ N/m. A=0,01s m². Pour un film à deux faces, compter deux aires.'),
        'wire': ('Fil élastique', 'Allongement x', 'm', .02, 200 * scale, 'Force de traction F', 'N', 100, 'Allongement (cm)', 'Fil idéal : F=kx avec k=200κ N/m, x=0,02s m ; longueur de repos L₀=0,30 m.'),
        'capacitor': ('Condensateur', 'Charge q', 'C', 1e-5, scale / 2e-6, 'Tension u', 'V', 1e6, 'Charge (µC)', 'Condensateur C=2/κ µF ; q=10s µC, u=q/C. Travail électrique reçu : δW=u dq.'),
        'coil': ('Bobine idéale', 'Flux lié λ', 'Wb', .005, 1 / (.04 * scale), 'Intensité I', 'A', 1000, 'Flux lié (mWb)', 'Bobine sans pertes : inductance L=0,04κ H, flux lié λ=5s mWb, I=λ/L. Le flux lié inclut le nombre de spires.')
    }
    name, coord_name, coord_unit, factor, coupling, effort_name, effort_unit, display, xlabel, hypothesis = settings[device]
    qi, qf = factor * si, factor * sf
    q = np.linspace(qi, qf, 401)
    if device == 'surface':
        effort = np.full_like(q, coupling)
        energy = coupling * q
        initial_energy = coupling * qi
    else:
        effort, energy = coupling * q, .5 * coupling * q * q
        initial_energy = .5 * coupling * qi * qi
    W = energy[-1] - initial_energy
    return result(
        [metric('Dispositif', name), metric(coord_name + ' initiale', qi, coord_unit), metric(coord_name + ' finale', qf, coord_unit),
         metric(effort_name + ' finale', effort[-1], effort_unit), metric('Travail reçu W', W, 'J'), metric('Énergie stockée finale', energy[-1], 'J'), metric('Variation de l’énergie stockée', W, 'J')],
        [chart('L’effort est conjugué à la coordonnée', xlabel, effort_name + ' (' + effort_unit + ')', series(effort_name, q * display, effort)),
         chart('Énergie stockée et travail reçu', xlabel, 'Énergie (J)', series('Énergie stockée', q * display, energy), series('W reçu depuis l’état initial', q * display, energy - initial_energy)),
         chart('Une aire dans les unités SI', coord_name + ' (' + coord_unit + ')', 'Travail reçu cumulé (J)', series('∫ effort × dcoordonnée', q, cumulative_integral(effort, q)))],
        scene_curves('Un travail : aire orientée sous la courbe', [(effort_name, q * display, effort)], xlabel, effort_unit, hypothesis, dict(type='energy', device=device, initial=qi, final=qf, effort=effort[-1], work=W, storedEnergy=energy[-1])),
        ['Identifier le système, la coordonnée généralisée et l’effort extérieur associé. Utiliser des unités SI avant de calculer le travail.',
         hypothesis,
         'Pour un effort constant, W=effort×(coordonnée finale−initiale). Pour une loi linéaire effort=K×coordonnée, W=K(coordonnée finale²−initiale²)/2.',
         'Inverser les deux extrémités change le signe du travail. Sans dissipation, la variation d’énergie stockée est égale à ce travail ; aucune énergie ne disparaît.'],
        ['Dispositifs idéaux réversibles, sans frottement, résistance électrique ni hystérésis.', hypothesis, 'Pour un milieu magnétique matériel, les conventions et la géométrie doivent être précisées avant d’utiliser un travail en H dB ; ici la bobine et le flux lié fournissent un modèle sans ambiguïté.'])


def helmholtz_potential(y, T, fraction, stiffness, rest):
    K = stiffness * .2 ** 2
    y = np.asarray(y)
    return -R * T * (fraction * np.log(y) + (1 - fraction) * np.log(1 - y)) + .5 * K * (y - rest) ** 2


def helmholtz_gradient(y, T, fraction, stiffness, rest):
    return R * T * (-fraction / y + (1 - fraction) / (1 - y)) + stiffness * .2 ** 2 * (y - rest)


def helmholtz_equilibrium(T, fraction, stiffness, rest):
    lo, hi = 1e-9, 1 - 1e-9
    for _ in range(70):
        mid = (lo + hi) / 2
        if helmholtz_gradient(mid, T, fraction, stiffness, rest) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def potentiel_helmholtz(p):
    T, nL, stiffness, rest, yi = p['T'], p['fraction'], p['stiffness'], p['rest'], p['initial']
    nR, Vtot, length = 1 - nL, .02, .2
    yeq = helmholtz_equilibrium(T, nL, stiffness, rest)
    y = np.linspace(.04, .96, 601)
    Fmin = float(helmholtz_potential(yeq, T, nL, stiffness, rest))
    F = helmholtz_potential(y, T, nL, stiffness, rest) - Fmin
    gas = -R * T * (nL * np.log(y / yeq) + nR * np.log((1 - y) / (1 - yeq)))
    spring = .5 * stiffness * length ** 2 * ((y - rest) ** 2 - (yeq - rest) ** 2)
    force = -helmholtz_gradient(y, T, nL, stiffness, rest) / length
    PL, PR = nL * R * T / (Vtot * yeq), nR * R * T / (Vtot * (1 - yeq))
    path_u = np.linspace(0, 6, 301)
    path_y = yeq + (yi - yeq) * np.exp(-path_u)
    path_F = helmholtz_potential(path_y, T, nL, stiffness, rest) - Fmin
    available = float(helmholtz_potential(yi, T, nL, stiffness, rest)) - Fmin
    curvature = R * T * (nL / yeq ** 2 + nR / (1 - yeq) ** 2) + stiffness * length ** 2
    return result(
        [metric('Fraction de volume à gauche à l’équilibre yéq', yeq), metric('Volume gauche à l’équilibre', Vtot * yeq * 1000, 'L'),
         metric('Pression gauche à l’équilibre', PL / 1e5, 'bar'), metric('Pression droite à l’équilibre', PR / 1e5, 'bar'),
         metric('F(yi)−Fmin, énergie libre disponible', available, 'J'), metric('Force initiale sur la cloison', -helmholtz_gradient(yi, T, nL, stiffness, rest) / length, 'N'),
         metric('Courbure positive F″(yéq)', curvature, 'J'), metric('Résidu du bilan des forces à l’équilibre', (PL - PR) * Vtot / length - stiffness * length * (yeq - rest), 'N')],
        [chart('Le potentiel complet possède un minimum stable', 'Fraction de volume y', 'Énergie libre relative (J)', series('Ftotal−Fmin', y, F), series('Contribution des gaz', y, gas), series('Contribution du ressort', y, spring), xMarker=yeq, xMarkerLabel='Équilibre'),
         chart('La force est l’opposé de la pente du potentiel', 'y', 'Force sur la cloison (N)', series('−F′(y)/L', y, force)),
         chart('Une évolution dissipative vers le minimum', 'Paramètre de relaxation sans dimension', 'F−Fmin (J)', series('Potentiel le long du chemin', path_u, path_F))],
        scene_curves('Un volume total fixe, deux volumes internes variables', [('F(y)−Fmin', y, F)], 'y=VG/Vtotal', 'F−Fmin (J)', 'La cloison partage 20 L ; longueur de l’enceinte 0,20 m. Le ressort est inclus dans le système. À l’équilibre, la différence des pressions compense sa force.', dict(type='piston', fraction=yi, equilibriumFraction=yeq, leftMoles=nL, rightMoles=nR, totalVolume=Vtot, temperature=T, stiffness=stiffness, pressureLeft=PL, pressureRight=PR)),
        ['Choisir comme système les deux gaz, la cloison et le ressort. Le volume extérieur Vtotal=20 L est fixe ; les quantités de matière sont fixes et la température est imposée.',
         'L’énergie libre d’une mole idéale dépend de son volume par −RT lnV. Ajouter le ressort : F(y)=−RT[nG ln y+nD ln(1−y)]+kₛL²(y−yₛ)²/2, à une constante près.',
         'La condition F′(y)=0 est le bilan (PG−PD)A−kₛL(y−yₛ)=0, avec A=Vtotal/L. La dérivée seconde est strictement positive : le minimum est unique et stable.',
         'Une relaxation interne sans travail extérieur peut faire décroître F. Le troisième tracé utilise le chemin monotone y= yéq+(yi−yéq)e^(−u), pour illustrer la décroissance ; u n’est pas un temps mécanique prédit.'],
        ['Gaz parfaits, une mole au total, température constante et enceinte rigide ; aucun transfert de matière entre compartiments.', 'Le ressort est interne au système : minimiser F sous T,Vtotal fixés est donc le critère approprié.', 'La cloison et le ressort sont idéalisés ; les oscillations transitoires et la cinétique de dissipation ne sont pas calculées.'])


def gibbs_equilibrium(T, dH, dS):
    dG = dH * 1000 - T * dS
    return 1 / (1 + math.exp(dG / (R * T)))


def gibbs_mixture(x, T, dH, dS):
    x = np.asarray(x)
    mixing = np.where(x > 0, x * np.log(np.maximum(x, 1e-300)), 0) + np.where(x < 1, (1 - x) * np.log(np.maximum(1 - x, 1e-300)), 0)
    return x * (dH * 1000 - T * dS) + R * T * mixing


def potentiel_gibbs(p):
    T, dH, dS, xi = p['T'], p['dH'], p['dS'], p['initial']
    dG0 = dH * 1000 - T * dS
    xe = gibbs_equilibrium(T, dH, dS)
    x = np.unique(np.r_[np.linspace(.0001, .9999, 601), xe])
    Gmin = float(gibbs_mixture(xe, T, dH, dS))
    G = gibbs_mixture(x, T, dH, dS) - Gmin
    slope = dG0 + R * T * np.log(x / (1 - x))
    initial_slope = dG0 + R * T * math.log(xi / (1 - xi))
    drop = float(gibbs_mixture(xi, T, dH, dS)) - Gmin
    temps = np.linspace(240, 700, 301)
    return result(
        [metric('ΔrG° à la température choisie', dG0 / 1000, 'kJ/mol'), metric('Constante K de A ⇌ B', math.exp(-dG0 / (R * T))),
         metric('Fraction de B à l’équilibre', xe), metric('ΔrG à la composition initiale', initial_slope / 1000, 'kJ/mol'),
         metric('G(initial)−Géquilibre', drop, 'J'), metric('Entropie créée si la réaction relaxe sans travail utile', drop / T, 'J/K'),
         metric('Courbure G″ au minimum', R * T * (1 / xe + 1 / (1 - xe)), 'J')],
        [chart('Énergie standard et entropie de mélange sélectionnent un minimum', 'Fraction molaire xB', 'G−Gmin (J)', series('G du mélange', x, G), xMarker=xe, xMarkerLabel='Équilibre'),
         chart('La pente indique le sens spontané de la réaction', 'xB', 'ΔrG (J/mol)', series('ΔrG°+RT ln(xB/xA)', x, slope)),
         chart('La composition d’équilibre change avec la température', 'Température (K)', 'Fraction de B', series('xB,équilibre', temps, [gibbs_equilibrium(t, dH, dS) for t in temps]))],
        scene_curves('Minimiser G sous température et pression imposées', [('G−Gmin', x, G)], 'xB', 'G−Gmin (J)', 'Mélange idéal d’une mole. La pression reste constante ; A et B ont la même stœchiométrie totale, ce qui rend le terme de pression commun aux deux espèces.', dict(type='energy', device='reaction', initialFraction=xi, equilibriumFraction=xe, temperature=T, releasedFreeEnergy=drop)),
        ['Pour A⇌B avec une mole au total, poser x=xB et xA=1−x. L’avancement vaut x mole ; G est défini à une constante indépendante de x près.',
         'Prendre ΔrG°=ΔrH°−TΔrS° et ajouter RT[(1−x)ln(1−x)+xlnx], l’énergie libre de mélange idéal.',
         'Dériver : ∂G/∂x=ΔrG°+RT ln[x/(1−x)]=ΔrG. L’équilibre vérifie x/(1−x)=K=exp(−ΔrG°/RT).',
         'La courbure RT(1/x+1/(1−x)) est positive. Si ΔrG<0, augmenter x diminue G ; si ΔrG>0, la réaction inverse est spontanée.'],
        ['T et P constants, mélange idéal, réaction A⇌B et une mole totale ; ΔrH° et ΔrS° sont supposés constants sur la gamme proposée.', 'Pas de cinétique : un minimum de G donne un équilibre, pas le temps nécessaire pour l’atteindre.', 'L’entropie créée ΔGperdue/T suppose une évolution sans travail utile autre que la pression, avec un thermostat à T.'])


def calorimetry_state(mode, warm, cold, m1, m2, Ccal):
    if mode == 'solids':
        C1, C2 = m1 * C_WATER + Ccal, m2 * C_ICE
        Tf = (C1 * warm + C2 * cold) / (C1 + C2)
        entropy = C1 * math.log(Tf / warm) + C2 * math.log(Tf / cold)
        return Tf, None, entropy, 'Capacités constantes, sans changement de phase', 0.0
    total = m1 + m2
    initial_energy = m1 * (LATENT + C_WATER * (warm - TM)) + m2 * C_ICE * (cold - TM) + Ccal * (warm - TM)
    initial_entropy = m1 * (LATENT / TM + C_WATER * math.log(warm / TM)) + m2 * C_ICE * math.log(cold / TM) + Ccal * math.log(warm / TM)
    if initial_energy < 0:
        Tf = TM + initial_energy / (total * C_ICE + Ccal)
        liquid = 0.0
        final_entropy = (total * C_ICE + Ccal) * math.log(Tf / TM)
        regime = 'Toute l’eau est gelée ; équilibre sous 0 °C'
    elif initial_energy <= total * LATENT:
        Tf, liquid = TM, initial_energy / LATENT
        final_entropy = liquid * LATENT / TM
        regime = 'Glace et eau coexistent à 0 °C'
    else:
        Tf = TM + (initial_energy - total * LATENT) / (total * C_WATER + Ccal)
        liquid = total
        final_entropy = total * (LATENT / TM + C_WATER * math.log(Tf / TM)) + Ccal * math.log(Tf / TM)
        regime = 'Toute la glace est fondue ; eau au-dessus de 0 °C'
    return Tf, liquid, final_entropy - initial_entropy, regime, initial_energy


def calorimetrie_entropie(p):
    mode, warm, cold, m1, m2, Ccal = p['mode'], p['warm'], p['cold'], p['m1'], p['m2'], p['Ccal']
    Tf, liquid, Sprod, regime, E = calorimetry_state(mode, warm, cold, m1, m2, Ccal)
    masses = np.linspace(.02, .8, 301)
    states = [calorimetry_state(mode, warm, cold, m1, mass, Ccal) for mass in masses]
    temps, created = np.array([s[0] for s in states]), np.array([s[2] for s in states])
    if mode == 'ice':
        liquid_fraction = np.array([s[1] / (m1 + mass) for s, mass in zip(states, masses)])
        total = m1 + m2
        Tsolid, Tliquid = np.linspace(230, TM, 151), np.linspace(TM, 365, 151)
        xT = np.r_[Tsolid, np.full(151, TM), Tliquid]
        enthalpy = np.r_[(total * C_ICE + Ccal) * (Tsolid - TM), np.linspace(0, total * LATENT, 151), total * LATENT + (total * C_WATER + Ccal) * (Tliquid - TM)]
        mainchart = chart('L’énergie finale inclut un palier de fusion', 'Température (K)', 'Énergie relative à toute la glace à 0 °C (kJ)', series('Équilibre du mélange', xT, enthalpy / 1000), series('Énergie initiale conservée', xT, np.full_like(xT, E / 1000)))
        scene = scene_curves('Le bilan choisit la phase avant la température', [('Énergie à l’équilibre', xT, enthalpy / 1000)], 'T (K)', 'Énergie (kJ)', regime, dict(type='reservoir', device='calorimeter', initialHot=warm, initialCold=cold, finalTemperature=Tf, hotMass=m1, coldMass=m2, liquidMass=liquid, totalMass=total, entropyCreated=Sprod))
        extra = chart('La quantité de liquide finale n’est pas toujours la masse initiale d’eau', 'Masse de glace ajoutée (kg)', 'Fraction liquide finale', series('Fraction liquide', masses, liquid_fraction))
    else:
        trial = np.linspace(cold, warm, 301)
        net = (m1 * C_WATER + Ccal) * (trial - warm) + m2 * C_ICE * (trial - cold)
        mainchart = chart('Le bilan total s’annule à la température d’équilibre', 'Température finale supposée (K)', 'Variation totale d’énergie (kJ)', series('ΔUtotal', trial, net / 1000), xMarker=Tf, xMarkerLabel='Équilibre')
        scene = scene_curves('Deux capacités thermiques cherchent une température commune', [('ΔUtotal', trial, net / 1000)], 'Tfinale (K)', 'ΔUtotal (kJ)', regime, dict(type='reservoir', device='calorimeter', initialHot=warm, initialCold=cold, finalTemperature=Tf, hotMass=m1, coldMass=m2, entropyCreated=Sprod))
        extra = chart('Le calorimètre n’est pas une capacité nulle', 'Masse du corps froid (kg)', 'Température finale (K)', series('Avec calorimètre', masses, temps), series('Calorimètre négligé', masses, [calorimetry_state(mode, warm, cold, m1, mass, 0)[0] for mass in masses]))
    return result(
        [metric('Régime final', regime), metric('Température finale', Tf, 'K'), metric('Température finale en degrés Celsius', Tf - TM, '°C'),
         metric('Entropie totale créée', Sprod, 'J/K'), metric('Masse liquide finale', liquid if liquid is not None else 'Sans changement de phase', 'kg' if liquid is not None else ''),
         metric('Masse de glace finale', m1 + m2 - liquid if liquid is not None else 'Non applicable', 'kg' if liquid is not None else ''), metric('Chaleur latente massique utilisée pour la glace', LATENT / 1000, 'kJ/kg')],
        [mainchart, chart('La masse froide modifie la température finale', 'Masse froide (kg)', 'Température finale (K)', series('Tfinale', masses, temps)), extra,
         chart('Le second principe contrôle le résultat', 'Masse froide (kg)', 'Entropie créée (J/K)', series('ΔStotal', masses, created))], scene,
        ['Le système est le calorimètre et son contenu. Il est isolé : la somme des variations d’énergie est nulle ; les échanges internes se compensent.',
         'Sans changement de phase, associer une capacité à chaque corps et au calorimètre, puis résoudre ΣCj(Tf−Tj)=0.',
         'Avec glace, choisir comme référence la glace à Tm=273,15 K : hglace=cglace(T−Tm), heau=L+ceau(T−Tm). Le bilan d’enthalpie à pression ambiante choisit le régime final.',
         'Si l’énergie initiale relative est entre 0 et (m₁+m₂)L, Tf=Tm et la masse liquide vaut E/L. En dessous, tout gèle ; au-dessus, tout fond. Calculer ensuite S avec c ln(T/Tm) et le saut L/Tm.'],
        ['Capacités constantes : cglace=2100 et ceau=4180 J/(kg·K), L=334 kJ/kg. Pression atmosphérique, évaporation et travail de pression négligeables pour les phases condensées.', 'Le calorimètre est initialement à la température chaude et a une capacité Ccal ; le système complet est isolé.', 'Le mode sans changement de phase utilise deux corps idéaux à capacités constantes, même pour une température inférieure à 273,15 K.'])


def vdw_pressure(T, v, a, b):
    return R * np.asarray(T) / (np.asarray(v) - b) - a / np.asarray(v) ** 2


def vdw_enthalpy(T, v, a, b, cv):
    return cv * np.asarray(T) + R * np.asarray(T) * np.asarray(v) / (np.asarray(v) - b) - 2 * a / np.asarray(v)


def vdw_joule_thomson(T, v, a, b, cv):
    D = R * T / (v - b) ** 2 - 2 * a / v ** 3
    cp = cv + T * (R / (v - b)) ** 2 / D
    derivative = (R / (v - b)) / D
    mu = (T * derivative - v) / cp
    inversion = 2 * a / (R * b) * (1 - b / v) ** 2
    return mu, inversion, cp, D


def detentes_joule(p):
    experiment, Ti, vi, ratio, a, b, cv = p['experiment'], p['T'], p['vi'] / 1000, p['ratio'], p['a'], p['b'] * 1e-6, p['cvR'] * R
    v = np.linspace(vi, vi * ratio, 501)
    if experiment == 'free_ideal':
        a_effective, b_effective = 0.0, 0.0
        T = np.full_like(v, Ti)
        P = R * T / v
        U, H = cv * T, (cv + R) * T
        entropy = cv * np.log(T / Ti) + R * np.log(v / vi)
        mu, inversion, cp, D = 0.0, 0.0, cv + R, R * Ti / vi ** 2
        description = 'Détente dans le vide : U constante, pas de travail ni de chaleur échangés.'
    else:
        a_effective, b_effective = a, b
        if experiment == 'free_vdw':
            T = Ti + a / cv * (1 / v - 1 / vi)
            description = 'Détente dans le vide : U=cV T−a/v constante. L’énergie d’attraction augmente lors de la séparation ; T diminue.'
        else:
            Hi = float(vdw_enthalpy(Ti, vi, a, b, cv))
            T = (Hi + 2 * a / v) / (cv + R * v / (v - b))
            description = 'Étranglement adiabatique en régime permanent : h=cV T+Pv−a/v reste constant ; les travaux d’écoulement sont inclus dans h.'
        P = vdw_pressure(T, v, a, b)
        U, H = cv * T - a / v, vdw_enthalpy(T, v, a, b, cv)
        entropy = cv * np.log(T / Ti) + R * np.log((v - b) / (vi - b))
        mu, inversion, cp, D = vdw_joule_thomson(Ti, vi, a, b, cv)
    return result(
        [metric('Température finale Tf', T[-1], 'K'), metric('Variation Tf−Ti', T[-1] - Ti, 'K'),
         metric('Pression initiale', P[0] / 1e5, 'bar'), metric('Pression finale', P[-1] / 1e5, 'bar'),
         metric('Variation d’énergie interne molaire Δu', U[-1] - U[0], 'J/mol'), metric('Variation d’enthalpie molaire Δh', H[-1] - H[0], 'J/mol'),
         metric('Entropie créée par mole', entropy[-1], 'J/(mol·K)'), metric('µJT initial, pour un étranglement', mu * 1e5, 'K/bar'),
         metric('Température d’inversion au volume initial', inversion if experiment != 'free_ideal' else 'Gaz parfait : µJT=0', 'K' if experiment != 'free_ideal' else ''),
         metric('Stabilité mécanique initiale : −∂P/∂v', D, 'Pa·mol/m³')],
        [chart('Deux bilans différents peuvent donner des températures différentes', 'Volume molaire (L/mol)', 'Température (K)', series('Température du gaz', v * 1000, T), series('Température initiale', v * 1000, np.full_like(v, Ti))),
         chart('U ou H : repérer la grandeur conservée', 'Volume molaire (L/mol)', 'Variation molaire (J/mol)', series('Δu', v * 1000, U - U[0]), series('Δh', v * 1000, H - H[0])),
         chart('La pression baisse mais le signe de ΔT dépend du modèle', 'Volume molaire (L/mol)', 'Pression (bar)', series('P', v * 1000, P / 1e5)),
         chart('Une détente irréversible crée de l’entropie', 'Volume molaire (L/mol)', 'Variation d’entropie molaire (J/(mol·K))', series('s−si', v * 1000, entropy))],
        scene_curves('Détente : choisir le bon système et le bon invariant', [('T', v * 1000, T)], 'v (L/mol)', 'T (K)', description, dict(type='reservoir', device='throttle' if experiment == 'throttle_vdw' else 'free-expansion', initialTemperature=Ti, finalTemperature=T[-1], initialVolume=vi, finalVolume=v[-1], initialPressure=P[0], finalPressure=P[-1], invariant='h' if experiment == 'throttle_vdw' else 'U')),
        ['Détente dans le vide : système fermé isolé, Q=W=0, donc ΔU=0. Gaz parfait : u=cV T ; van der Waals : u=cV T−a/v.',
         'Étranglement : système ouvert en régime permanent, adiabatique, sans travail d’arbre et sans variation notable des énergies cinétique et potentielle. Le bilan impose hsortie=hentrée.',
         'Pour van der Waals, P=RT/(v−b)−a/v². Dans la branche d’étranglement, résoudre exactement h(T,v)=hi donne T(v)=[hi+2a/v]/[cV+Rv/(v−b)].',
         'µJT=(∂T/∂P)h=[T(∂v/∂T)P−v]/cP. L’inversion vérifie Tinv(v)=2a(1−b/v)²/(Rb). Comme ΔP<0, µJT>0 signifie refroidissement, µJT<0 réchauffement.'],
        ['Une mole, volumes molaires en m³/mol pour le calcul ; paramètres a,b du modèle de van der Waals, cV constant.', 'La gamme vérifie −(∂P/∂v)T>0 : stabilité mécanique. Le modèle est monophasé ; sous la température critique, une métastabilité peut subsister. La coexistence liquide–gaz est étudiée séparément dans les laboratoires de phases.', 'La courbe en v est une famille d’états finaux ou une ligne d’enthalpie constante, pas une transformation quasistatique du gaz dans la détente libre.'])


def carnot_reference(cold, hot, n=1, reverse=False):
    gamma = 1.4
    cv = R / (gamma - 1)
    V1, V2 = .001, .002
    scale = (hot / cold) ** (1 / (gamma - 1))
    V3, V4 = V2 * scale, V1 * scale
    V = np.r_[np.linspace(V1, V2, 161), np.linspace(V2, V3, 241), np.linspace(V3, V4, 161), np.linspace(V4, V1, 241)]
    T = np.r_[np.full(161, hot), hot * (V2 / np.linspace(V2, V3, 241)) ** (gamma - 1), np.full(161, cold), cold * (V4 / np.linspace(V4, V1, 241)) ** (gamma - 1)]
    P = n * R * T / V
    S = n * (cv * np.log(T / hot) + R * np.log(V / V1))
    if reverse:
        V, P, T, S = V[::-1], P[::-1], T[::-1], S[::-1]
    return V, P, T, S


def carnot_ditherme(p):
    mode, cold, hot, phi, q = p['mode'], p['cold'], p['hot'], p['quality'], p['energy'] * 1000
    eta_c, cop_c = 1 - cold / hot, cold / (hot - cold)
    if mode == 'engine':
        performance, limit = phi * eta_c, eta_c
        Qh, W = q, -q * performance
        Qc = -Qh - W
        name, unit = 'Rendement moteur', ''
        n = q / (R * hot * math.log(2))
    else:
        W = q
        Qc, Qh = phi * cop_c * W, -(1 + phi * cop_c) * W
        performance, limit = (phi * cop_c, cop_c) if mode == 'fridge' else (1 + phi * cop_c, 1 + cop_c)
        name, unit = 'COP frigorifique' if mode == 'fridge' else 'COP pompe à chaleur', ''
        n = q / (R * (hot - cold) * math.log(2))
    created = q * (1 - phi) * eta_c / cold if mode == 'engine' else q * (1 - phi) / hot
    V, P, T, S = carnot_reference(cold, hot, n, mode != 'engine')
    qualities = np.linspace(.3, 1, 141)
    if mode == 'engine':
        perf = qualities * eta_c
        entropy = q * (1 - qualities) * eta_c / cold
    else:
        perf = qualities * cop_c if mode == 'fridge' else 1 + qualities * cop_c
        entropy = q * (1 - qualities) / hot
    return result(
        [metric(name, performance, unit), metric('Limite de Carnot correspondante', limit), metric('Travail reçu W par cycle', W / 1000, 'kJ'),
         metric('Chaleur reçue depuis la source chaude Qc', Qh / 1000, 'kJ'), metric('Chaleur reçue depuis la source froide Qf', Qc / 1000, 'kJ'),
         metric('Entropie créée par cycle', created, 'J/K'), metric('Bilan W+Qc+Qf', W + Qh + Qc, 'J')],
        [chart('Cycle de Carnot : référence réversible dans P,V', 'Volume (L)', 'Pression (bar)', series('Cycle de référence', V * 1000, P / 1e5)),
         chart('Les isothermes et les isentropiques dans T,S', 'Entropie relative (J/K)', 'Température (K)', series('Référence réversible', S, T)),
         chart('Les pertes éloignent la performance de sa borne', 'Facteur φ', name, series('Performance', qualities, perf), series('Limite de Carnot', qualities, np.full_like(qualities, limit))),
         chart('Le second principe chiffre les irréversibilités', 'Facteur φ', 'Entropie créée (J/K)', series('Scréée', qualities, entropy))],
        scene_curves('Une machine cyclique échange avec deux sources', [('Cycle réversible de référence', V * 1000, P / 1e5)], 'V (L)', 'P (bar)', 'Les flèches énergétiques du dispositif utilisent les bilans du scénario choisi. Le cycle dessiné est la référence de Carnot et ne représente pas la géométrie d’un cycle irréversible inconnu.', dict(type='engine', mode=mode, hotTemperature=hot, coldTemperature=cold, Qhot=Qh, Qcold=Qc, work=W, entropyCreated=created, quality=phi), kind='phase'),
        ['Le fluide parcourt un cycle : ΔU=ΔS=0. Écrire W+Qc+Qf=0 puis Qc/Tc+Qf/Tf+Scréée=0, avec W et Q reçus positifs.',
         'Pour le moteur, Qc>0, Qf<0 et W<0. Le rendement −W/Qc est borné par 1−Tf/Tc ; ici il vaut φ fois cette limite.',
         'Pour le réfrigérateur, W>0, Qf>0 et Qc<0. Le COPf=Qf/W est borné par Tf/(Tc−Tf). La pompe à chaleur utilise COPc=−Qc/W=1+COPf.',
         'Le modèle prend COPf=φCOPf,Carnot ; le COP de la pompe suit le bilan, au lieu d’être réglé indépendamment. Calculer Scréée à partir des échanges vérifie leur cohérence.'],
        ['Sources thermostatiques à températures absolues fixes, Tc>Tf>0 ; aucune autre source ni échange d’énergie.', 'φ est un modèle de pertes globales. La chaleur chaude Qc et la chaleur froide Qf désignent des échanges reçus par la machine, avec signes différents selon l’usage.', 'Les courbes P,V et T,S montrent uniquement la référence réversible ; pour φ<1, le bilan énergétique et entropique est calculé sans inventer une trajectoire réelle.'])


def cycle_data(cycle, ratio, z, gamma, T1, regen=1, samples=241):
    cv, cp = R / (gamma - 1), R * gamma / (gamma - 1)
    V1 = R * T1 / 1e5
    if cycle == 'otto':
        T2, V2 = T1 * ratio ** (gamma - 1), V1 / ratio
        T3, V3, T4, V4 = z * T2, V2, z * T1, V1
        branches = ['adiabatique', 'isochore', 'adiabatique', 'isochore']
        Qh, Qc = cv * (T3 - T2), cv * (T1 - T4)
    elif cycle == 'diesel':
        T2, V2 = T1 * ratio ** (gamma - 1), V1 / ratio
        T3, V3 = z * T2, z * V2
        T4, V4 = T1 * z ** gamma, V1
        branches = ['adiabatique', 'isobare', 'adiabatique', 'isochore']
        Qh, Qc = cp * (T3 - T2), cv * (T1 - T4)
    elif cycle == 'brayton':
        T2, V2 = T1 * ratio ** ((gamma - 1) / gamma), V1 / ratio ** (1 / gamma)
        T3, V3, T4, V4 = z * T2, z * V2, z * T1, z * V1
        branches = ['adiabatique', 'isobare', 'adiabatique', 'isobare']
        Qh, Qc = cp * (T3 - T2), cp * (T1 - T4)
    else:
        T2, V2, T3, V3, T4, V4 = T1, V1 / ratio, z * T1, V1 / ratio, z * T1, V1
        branches = ['isotherme', 'isochore', 'isotherme', 'isochore']
        Qh = R * T3 * math.log(ratio) + (1 - regen) * cv * (T3 - T1)
        Qc = -R * T1 * math.log(ratio) - (1 - regen) * cv * (T3 - T1)
    states = [(T1, V1), (T2, V2), (T3, V3), (T4, V4)]
    volumes, temperatures, labels, branch_work, branch_heat = [], [], [], [], []
    for i, kind in enumerate(branches):
        Ta, Va = states[i]
        Tb, Vb = states[(i + 1) % 4]
        if kind == 'isochore':
            V, T, work = np.full(samples, Va), np.linspace(Ta, Tb, samples), 0.0
        else:
            V = np.linspace(Va, Vb, samples)
            if kind == 'adiabatique':
                T = Ta * (Va / V) ** (gamma - 1)
                work = cv * (Tb - Ta)
            elif kind == 'isotherme':
                T = np.full(samples, Ta)
                work = -R * Ta * math.log(Vb / Va)
            else:
                T = Ta * V / Va
                work = -R * (Tb - Ta)
        volumes.append(V)
        temperatures.append(T)
        labels.append(f'{i+1}→{(i+1)%4+1} : {kind}')
        branch_work.append(work)
        branch_heat.append(cv * (Tb - Ta) - work)
    V, T = np.concatenate(volumes), np.concatenate(temperatures)
    P = R * T / V
    S = cv * np.log(T / T1) + R * np.log(V / V1)
    W = -Qh - Qc
    return dict(V=V, P=P, T=T, S=S, states=states, labels=labels, work=branch_work, heat=branch_heat, Qhot=Qh, Qcold=Qc, W=W, efficiency=-W / Qh, cv=cv, cp=cp)


def cycles_moteurs(p):
    cycle, ratio, z, gamma, T1, regen = p['cycle'], p['ratio'], p['z'], p['gamma'], p['T1'], p['regen']
    d = cycle_data(cycle, ratio, z, gamma, T1, regen)
    V, P, T, S = d['V'], d['P'], d['T'], d['S']
    grid = np.linspace(2, 18, 161)
    efficiencies = [cycle_data(cycle, r, z, gamma, T1, regen, samples=9)['efficiency'] for r in grid]
    Tmax = float(np.max(T))
    created = (1 - regen) * d['cv'] * (Tmax - T1) * (1 / T1 - 1 / Tmax) if cycle == 'stirling' else -d['Qhot'] / Tmax - d['Qcold'] / T1
    out = result(
        [metric('Cycle', cycle.capitalize()), metric('Rendement du cycle', d['efficiency']), metric('Borne de Carnot entre les températures extrêmes', 1 - T1 / Tmax),
         metric('Travail reçu W par mole et par cycle', d['W'] / 1000, 'kJ/mol'), metric('Chaleur externe reçue positive Qchaud', d['Qhot'] / 1000, 'kJ/mol'),
         metric('Chaleur externe reçue négative Qfroid', d['Qcold'] / 1000, 'kJ/mol'), metric('Température maximale du gaz', Tmax, 'K'),
         metric('Entropie créée si les deux sources restent à Tmax et Tmin', created, 'J/(mol·K)'), metric('Bilan W+Qchaud+Qfroid', d['W'] + d['Qhot'] + d['Qcold'], 'J/mol')],
        [chart('Diagramme P,V : identifier les quatre branches', 'Volume molaire (L/mol)', 'Pression (bar)', series(cycle.capitalize(), V * 1000, P / 1e5)),
         chart('Diagramme T,S : les isentropiques sont verticales', 'Entropie molaire relative (J/(mol·K))', 'Température (K)', series(cycle.capitalize(), S, T)),
         chart('Le rendement dépend du type de contrainte', 'Taux r', 'Rendement', series('Cycle sélectionné', grid, efficiencies)),
         chart('Vérifier le signe de l’aire et du travail', 'Fraction d’un tour de cycle', 'Travail reçu cumulé (kJ/mol)', series('−∫P dV le long du cycle', np.linspace(0, 1, len(V)), cumulative_integral(-P, V) / 1000))],
        scene_curves('Un cycle n’est pas seulement quatre points', [('Cycle ' + cycle.capitalize(), V * 1000, P / 1e5)], 'v (L/mol)', 'P (bar)', 'Les branches sont calculées avec leurs contraintes. Pour Stirling, le régénérateur échange une chaleur interne pendant les isochores ; seules ses pertes comptent dans Qchaud et Qfroid externes.', dict(type='engine', mode='engine', cycle=cycle, hotTemperature=Tmax, coldTemperature=T1, Qhot=d['Qhot'], Qcold=d['Qcold'], work=d['W'], regenerator=regen if cycle == 'stirling' else None), kind='phase'),
        ['Une mole de gaz parfait : cV=R/(γ−1), cP=γR/(γ−1). Les deux compressions ou détentes adiabatiques sont réversibles, donc TV^(γ−1) reste constant.',
         'Otto chauffe à volume constant ; Diesel chauffe à pression constante ; Brayton chauffe et refroidit à pression constante ; Stirling combine deux isothermes et deux isochores.',
         'Sur chaque branche, calculer W=−∫P dV et Q=cVΔT−W. Sur le cycle, ΔU=0 et W=−Qchaud−Qfroid. Le rendement est −W/Qchaud.',
         'Pour Stirling, les chaleurs des isochores sont en partie récupérées par le régénérateur. À ε=1, elles sont internes et le rendement devient 1−Tf/Tc ; sinon les pertes augmentent les échanges externes.'],
        ['Gaz parfait à capacités constantes ; cycles idéalisés, sans combustion réelle, frottement ni variation de composition.', 'r est un rapport de volumes pour Otto, Diesel, Stirling ; un rapport de pressions pour Brayton. z règle le chauffage : rapport T₃/T₂ pour Otto et Brayton, V₃/V₂ pour Diesel, Tc/Tf pour Stirling. Les grandeurs sont définies dans le guide.', 'Le calcul d’entropie des deux sources suppose celles-ci maintenues à Tmax et Tmin. Les branches de chauffage à température variable créent alors de l’entropie ; une trajectoire quasistatique n’est pas automatiquement réversible.', 'Pour Diesel, z<r pour conserver l’ordre des volumes ; les bornes des curseurs assurent cette condition.'])
    out['table'] = dict(headers=['Branche', 'Tinitiale (K)', 'Tfinale (K)', 'W reçu (J/mol)', 'Q reçu par le gaz (J/mol)'], rows=[[d['labels'][i], d['states'][i][0], d['states'][(i + 1) % 4][0], d['work'][i], d['heat'][i]] for i in range(4)])
    return out


def compressor_work(T, ratio, stages, fraction, efficiency):
    r_air, gamma = 287.0, 1.4
    cp = r_air * gamma / (gamma - 1)
    exponent = (gamma - 1) / gamma
    first = ratio ** fraction
    other = (ratio / first) ** (1 / (stages - 1))
    return cp * T / efficiency * (first ** exponent - 1 + (stages - 1) * (other ** exponent - 1))


def compresseur_etages(p):
    Ti, ratio, N, f, eta = p['T1'], p['ratio'], int(p['stages']), p['fraction'], p['efficiency']
    r_air, gamma = 287.0, 1.4
    cp, exponent = r_air * gamma / (gamma - 1), (gamma - 1) / gamma
    first = ratio ** f
    other = (ratio / first) ** (1 / (N - 1))
    ratios = np.r_[first, np.full(N - 1, other)]
    pressures = 1e5 * np.r_[1.0, np.cumprod(ratios)]
    output_temps = Ti * (1 + (ratios ** exponent - 1) / eta)
    W = cp * np.sum(output_temps - Ti)
    Q = -cp * np.sum(output_temps[:-1] - Ti)
    delta_h = cp * (output_temps[-1] - Ti)
    delta_s = cp * math.log(output_temps[-1] / Ti) - r_air * math.log(ratio)
    created = delta_s - Q / Ti
    minimum = compressor_work(Ti, ratio, N, 1 / N, eta)
    one = cp * Ti * (ratio ** exponent - 1) / eta
    reversible_isothermal = r_air * Ti * math.log(ratio)
    fractions = np.linspace(.01, .99, 241)
    work_curve = [compressor_work(Ti, ratio, N, x, eta) / 1000 for x in fractions]
    n_values = np.arange(1, 17)
    equal_works = n_values * cp * Ti / eta * (ratio ** (exponent / n_values) - 1)
    point_index, point_T, point_P = [0.0], [Ti], [pressures[0]]
    for j in range(N):
        point_index += [j + .8]
        point_T += [output_temps[j]]
        point_P += [pressures[j + 1]]
        if j < N - 1:
            point_index += [j + 1.0]
            point_T += [Ti]
            point_P += [pressures[j + 1]]
    point_index, point_T, point_P = np.array(point_index), np.array(point_T), np.array(point_P)
    point_S = cp * np.log(point_T / Ti) - r_air * np.log(point_P / pressures[0])
    out = result(
        [metric('Travail d’arbre reçu', W / 1000, 'kJ/kg'), metric('Travail minimal avec ces N étages et ηs', minimum / 1000, 'kJ/kg'),
         metric('Première pression optimale Pentrée·r^(1/N)', ratio ** (1 / N), 'bar'), metric('Première pression choisie', first, 'bar'),
         metric('Travail d’un seul étage avec ηs identique', one / 1000, 'kJ/kg'), metric('Borne réversible isotherme', reversible_isothermal / 1000, 'kJ/kg'),
         metric('Chaleur reçue dans les refroidisseurs', Q / 1000, 'kJ/kg'), metric('Variation d’enthalpie entrée–sortie', delta_h / 1000, 'kJ/kg'),
         metric('Entropie créée, refroidisseurs au thermostat T₁', created, 'J/(kg·K)'), metric('Résidu W+Q−Δh', W + Q - delta_h, 'J/kg')],
        [chart('Le minimum répartit également les logarithmes des pressions', 'f=ln(Pintermédiaire/Pentrée)/ln(r)', 'Travail (kJ/kg)', series('Travail total', fractions, work_curve), xMarker=1 / N, xMarkerLabel='foptimal=1/N'),
         chart('Multiplier les étages approche la compression isotherme', 'Nombre d’étages', 'Travail optimal (kJ/kg)', series('Rapports égaux et ηs choisi', n_values, equal_works / 1000), series('Isotherme réversible', n_values, np.full(len(n_values), reversible_isothermal / 1000)), series('Limite du modèle avec ηs<1', n_values, np.full(len(n_values), reversible_isothermal / eta / 1000))),
         chart('Comprimer réchauffe, le refroidisseur abaisse T à pression constante', 'Étape du dispositif', 'Température (K)', series('Température', point_index, point_T)),
         chart('Bilan d’un écoulement ouvert dans T,S', 'Entropie massique relative (J/(kg·K))', 'Température (K)', series('États entrée / sortie des dispositifs', point_S, point_T))],
        scene_curves('Le refroidissement intermédiaire réduit le travail suivant', [('Température dans les étages', point_index, point_T)], 'Étape', 'T (K)', 'Les segments relient les états d’entrée et de sortie ; aucune loi temporelle n’est attribuée aux machines. Chaque refroidisseur ramène l’air à T₁.', dict(type='engine', mode='compressor', stages=N, pressures=pressures, temperatures=output_temps, inletTemperature=Ti, work=W, heat=Q, efficiency=eta)),
        ['En régime permanent, négliger les variations d’énergie cinétique et potentielle : Δh=w_arbre+q. Les travaux de pression sont inclus dans h=u+Pv.',
         'Pour un étage adiabatique, Ts,sortie=T₁(Psortie/Pentrée)^((γ−1)/γ) et ηs=(Ts,sortie−T₁)/(Tsortie−T₁). Donc w=cP(Tsortie−T₁).',
         'Chaque refroidisseur isobare fournit un travail d’arbre nul et rejette cP(Tsortie−T₁). Les étages suivants recommencent à T₁.',
         'Le travail est une somme de fonctions exponentielles des logarithmes de rapports, dont la somme est ln r. La convexité impose les rapports égaux r^(1/N), soit des pressions en progression géométrique.'],
        ['Air parfait : r=287 J/(kg·K), γ=1,4, cP=1004,5 J/(kg·K). Toutes les grandeurs énergétiques sont rapportées à 1 kg.', 'Refroidissement complet entre étages, sans perte de pression ; rendement isentropique identique pour les étages.', 'Le thermostat des refroidisseurs est à T₁ : leur échange à différence de température finie crée de l’entropie. Un refroidissement complet ne signifie pas un refroidissement réversible.'])
    out['table'] = dict(headers=['Étage', 'Pentrée (bar)', 'Psortie (bar)', 'Tsortie (K)', 'Travail reçu (kJ/kg)'], rows=[[j + 1, pressures[j] / 1e5, pressures[j + 1] / 1e5, output_temps[j], cp * (output_temps[j] - Ti) / 1000] for j in range(N)])
    return out


def body_exergy(T, T0, C):
    z = (np.asarray(T) - T0) / T0
    return C * T0 * (z - np.log1p(z))


def exergie_corps(p):
    Ti, T0, C, phi = p['initial'], p['ambient'], p['capacity'], p['quality']
    maximum = float(body_exergy(Ti, T0, C))
    Wout = phi * maximum
    dU, dS = C * (T0 - Ti), C * math.log(T0 / Ti)
    Qenv = dU + Wout
    created = (1 - phi) * maximum / T0
    T = np.linspace(Ti, T0, 401)
    remaining = body_exergy(T, T0, C)
    extracted = phi * (maximum - remaining)
    delta_U = C * (T - Ti)
    Q_received = delta_U + extracted
    created_path = (1 - phi) * (maximum - remaining) / T0
    grid = np.linspace(180, 1000, 401)
    return result(
        [metric('Travail maximal disponible', maximum / 1000, 'kJ'), metric('Travail fourni au milieu extérieur', Wout / 1000, 'kJ'),
         metric('Travail reçu par corps + machine', -Wout / 1000, 'kJ'), metric('Variation d’énergie interne du corps', dU / 1000, 'kJ'),
         metric('Chaleur reçue de l’environnement par corps + machine', Qenv / 1000, 'kJ'), metric('Variation d’entropie du corps', dS, 'J/K'),
         metric('Entropie créée', created, 'J/K'), metric('Exergie détruite T₀Scréée', T0 * created / 1000, 'kJ')],
        [chart('L’exergie disparaît à l’équilibre avec l’environnement', 'Température du corps (K)', 'Énergie (kJ)', series('Exergie restante', T, remaining / 1000), series('Travail déjà fourni', T, extracted / 1000)),
         chart('Le premier principe sépare chaleur et travail', 'Température du corps (K)', 'Énergie reçue (kJ)', series('ΔU du corps', T, delta_U / 1000), series('Q reçu de l’environnement', T, Q_received / 1000), series('W reçu = −travail fourni', T, -extracted / 1000)),
         chart('Un corps chaud ou froid peut servir de ressource', 'Température initiale possible (K)', 'Exergie initiale (kJ)', series('C[(Ti−T₀)−T₀ln(Ti/T₀)]', grid, body_exergy(grid, T0, C) / 1000), xMarker=T0, xMarkerLabel='Équilibre'),
         chart('La destruction d’exergie mesure l’irréversibilité', 'Température du corps (K)', 'Entropie créée (J/K)', series('Scréée cumulée', T, created_path))],
        scene_curves('Une énergie thermique n’est pas entièrement convertible en travail', [('Travail fourni', T, extracted / 1000), ('Exergie restante', T, remaining / 1000)], 'T du corps (K)', 'Énergie (kJ)', 'Le système étudié inclut le corps et une machine cyclique. Le milieu reste à T₀. Pour φ=1, l’évolution globale est réversible ; pour φ=0, le contact direct fournit zéro travail.', dict(type='energy', device='exergy', initialTemperature=Ti, ambientTemperature=T0, currentTemperature=T0, capacity=C, work=-Wout, heat=Qenv, maximumWork=maximum, entropyCreated=created)),
        ['Le système est un corps de capacité constante C et une machine cyclique. L’environnement reste à T₀ ; le corps finit à T₀. ΔU=C(T₀−Ti) et ΔS=C ln(T₀/Ti).',
         'Pour une évolution réversible, Qreçu=T₀ΔS. Le premier principe donne le travail fourni maximal −W=−ΔU+T₀ΔS=C[(Ti−T₀)−T₀ ln(Ti/T₀)].',
         'Avec un travail fourni φ fois ce maximum, le bilan impose Qreçu=ΔU+φWmax. L’entropie créée vaut (1−φ)Wmax/T₀ : elle ne se choisit pas indépendamment.',
         'La fonction z−ln(1+z), z=(Ti−T₀)/T₀, est non négative et s’annule seulement à Ti=T₀. Un corps froid possède donc également de l’exergie ; son réchauffement peut produire du travail.'],
        ['Corps à capacité C constante, sans changement de phase, volume et travaux mécaniques propres négligeables.', 'Environnement thermostaté à T₀ et machine cyclique ; les conventions W,Q reçus concernent le système corps + machine.', 'Le facteur φ représente une récupération globale ; les courbes suivent les bilans sans prédire la vitesse d’une réalisation technique.'])


COMPUTE = {f.__name__: f for f in [travail_chemins, travaux_generalises, potentiel_helmholtz, potentiel_gibbs, calorimetrie_entropie, detentes_joule, carnot_ditherme, cycles_moteurs, compresseur_etages, exergie_corps]}
