"""Nitrobenzène, dinitrobenzènes et élimination stéréospécifique du recueil.

Les séquences redox sont des bilans entre espèces, et non une prétention à
décrire chaque transfert à la surface d'un métal. Les dipôles appartiennent
à un modèle géométrique explicite. Aucun rendement n'est inventé.
"""
from __future__ import annotations
import math
import numpy as np
from commun import (atom, bond, molecule, benzene, electron_arrow,
                    metric, chart, series, scene, mechanism_scene,
                    reaction_scene, clean)


def result(metrics, charts, drawing, steps, assumptions, **extra):
    return dict(metrics=metrics, charts=charts, scene=drawing, steps=steps,
                assumptions=assumptions, **extra)


def aromatic_structure(name, groups, nitro_double='oxygen_a'):
    """Vrai squelette de cycle et fonctions N/O explicites ; H du cycle implicites."""
    g = benzene(name)
    g['substituents'] = {int(k): v for k, v in groups.items()}
    for site, group in groups.items():
        angle = site * math.pi / 3
        radial = np.array([math.cos(angle), math.sin(angle)])
        tangent = np.array([-radial[1], radial[0]])
        center = 1.8 * radial
        if group in ('NO2', 'NO', 'NHOH', 'NH2'):
            n_id = f'n{site}'
            n_charge = 1 if group == 'NO2' else 0
            g['atoms'].append(atom(n_id, 'N', *center, charge=n_charge,
                                   lone_pairs=0 if n_charge else 1))
            g['bonds'].append(bond(site, n_id))
            if group == 'NO2':
                for letter, sign in [('a', 1), ('b', -1)]:
                    pos = center + .58 * radial + sign * .7 * tangent
                    double = nitro_double == f'oxygen_{letter}'
                    o_id = f'o{letter}{site}'
                    g['atoms'].append(atom(o_id, 'O', *pos,
                                           charge=0 if double else -1,
                                           lone_pairs=2 if double else 3))
                    g['bonds'].append(bond(n_id, o_id, 2 if double else 1))
            elif group in ('NO', 'NHOH'):
                pos = center + .7 * radial + .55 * tangent
                o_id = f'o{site}'
                g['atoms'].append(atom(o_id, 'O', *pos, lone_pairs=2))
                g['bonds'].append(bond(n_id, o_id, 2 if group == 'NO' else 1))
                if group == 'NHOH':
                    h_o = pos + .6 * radial
                    h_n = center - .7 * tangent + .3 * radial
                    g['atoms'].extend([atom(f'ho{site}', 'H', *h_o),
                                       atom(f'hn{site}', 'H', *h_n)])
                    g['bonds'].extend([bond(o_id, f'ho{site}'),
                                       bond(n_id, f'hn{site}')])
            elif group == 'NH2':
                for letter, sign in [('a', 1), ('b', -1)]:
                    pos = center + .6 * radial + sign * .55 * tangent
                    h_id = f'h{letter}{site}'
                    g['atoms'].append(atom(h_id, 'H', *pos))
                    g['bonds'].append(bond(n_id, h_id))
        elif group == 'COCH3':
            c_id, o_id, m_id = f'ca{site}', f'oc{site}', f'me{site}'
            o_pos = center + .78 * tangent
            m_pos = center + .83 * radial - .25 * tangent
            g['atoms'].extend([atom(c_id, 'C', *center),
                               atom(o_id, 'O', *o_pos, lone_pairs=2),
                               atom(m_id, 'C', *m_pos, label='CH₃', implicit_h=3)])
            g['bonds'].extend([bond(site, c_id), bond(c_id, o_id, 2),
                               bond(c_id, m_id)])
        else:
            g['atoms'].append(atom(f's{site}', group, *center))
            g['bonds'].append(bond(site, f's{site}'))
    # Pour les vérifications, les H omis sur les six carbones sont explicites
    # dans les métadonnées, sans ajouter des lettres H sur tout le dessin.
    for a in g['atoms'][:6]:
        a['implicit_h'] = 0 if int(a['id']) in groups else 1
    return g


REDUCTION_SPECIES = ['PhNO2', 'PhNO', 'PhNHOH', 'PhNH2']
REDUCTION_EQUATIONS = [
    'PhNO₂ + 2 H⁺ + 2 e⁻ → PhNO + H₂O',
    'PhNO + 2 H⁺ + 2 e⁻ → PhNHOH',
    'PhNHOH + 2 H⁺ + 2 e⁻ → PhNH₂ + H₂O',
]
REDUCTION_BALANCES = [
    dict(reactants={'PhNO2': 1, 'H+': 2, 'e-': 2},
         products={'PhNO': 1, 'H2O': 1}),
    dict(reactants={'PhNO': 1, 'H+': 2, 'e-': 2},
         products={'PhNHOH': 1}),
    dict(reactants={'PhNHOH': 1, 'H+': 2, 'e-': 2},
         products={'PhNH2': 1, 'H2O': 1}),
]


def nitrobenzene(p):
    mode = p['mode']
    stage = int(p['stage'])
    if mode == 'lewis':
        graphs = []
        for double in ['oxygen_a', 'oxygen_b']:
            title = 'Ph–N⁺(=Oₐ)–Oᵦ⁻' if double == 'oxygen_a' else 'Ph–N⁺(–Oₐ⁻)=Oᵦ'
            g = aromatic_structure(title, {0: 'NO2'}, double)
            atoms = {a['id']: a for a in g['atoms']}
            origin = atoms['ob0' if double == 'oxygen_a' else 'oa0']
            other = atoms['oa0' if double == 'oxygen_a' else 'ob0']
            n = atoms['n0']
            g['arrows'] = [
                electron_arrow([origin['x'], origin['y']], [n['x'], n['y']],
                               [origin['x'] + .5, origin['y']]),
                electron_arrow([(n['x'] + other['x']) / 2,
                                (n['y'] + other['y']) / 2],
                               [other['x'], other['y']],
                               [other['x'] + .35, other['y'] + .35]),
            ]
            g['formula'] = 'C6H5NO2'
            graphs.append(g)
        index = 0 if p['contributor'] == 'oxygen_a' else 1
        return result(
            [metric('Formule brute', 'C₆H₅NO₂'),
             metric('Charge totale', 0, 'e'), metric('Charge de N', '+1'),
             metric('Électrons autour de N', 8), metric('Effet du groupe', '−M et −I'),
             metric('Orientation d’une SEA accessible', 'méta')], [],
            mechanism_scene('Deux contributeurs, une seule molécule',
                'Les atomes restent aux mêmes positions. Les charges N⁺/O⁻ et l’octet sont conservés pendant le déplacement des deux doublets.',
                graphs, index),
            ['Compter les électrons : N possède quatre unités de liaison, donc une charge formelle +1 et aucun doublet libre.',
             'L’oxygène simplement lié porte trois doublets et −1 ; l’oxygène doublement lié porte deux doublets et est neutre.',
             'Les deux formes décrivent la délocalisation des liaisons N–O ; elles ne sont pas deux isomères ou deux états successifs de la réaction.',
             'Dans le système conjugué du nitrobenzène, NO₂ retire de la densité électronique par mésomérie ; méta est une orientation, pas une garantie de faisabilité ou une proportion.'],
            ['Formules de Lewis usuelles respectant l’octet de C, N et O.',
             'Ces deux contributeurs localisent seulement la mésomérie N–O. L’effet −M sur le cycle se justifie en comparant les complexes σ d’une SEA.'],
            contributor=p['contributor'], charge_total=0, nitrogen_octet=8,
            formula='C6H5NO2', reference_pages=[532, 534])
    if mode == 'reduction':
        groups = ['NO2', 'NO', 'NHOH', 'NH2']
        names = ['Nitrobenzène : PhNO₂', 'Nitrosobenzène : PhNO',
                 'N-phénylhydroxylamine : PhNHOH', 'Aniline : PhNH₂']
        formulas = ['C6H5NO2', 'C6H5NO', 'C6H7NO', 'C6H7N']
        frames = [aromatic_structure(name, {0: group})
                  for name, group in zip(names, groups)]
        for g, formula in zip(frames, formulas):
            g['formula'] = formula
        consumed = 2 * stage
        waters = [0, 1, 1, 2][stage]
        return result(
            [metric('Espèce suivie', names[stage]),
             metric('Électrons consommés depuis le début', consumed, 'équiv.'),
             metric('Protons consommés dans le bilan neutre', consumed, 'équiv.'),
             metric('Eau produite cumulée', waters, 'équiv.'),
             metric('Nombre d’oxydation de N', [3, 1, -1, -3][stage]),
             metric('Aniline en milieu très acide', 'PhNH₃⁺ après protonation')],
            [chart('Trois réductions à deux électrons', 'État de la séquence',
                   'Nombre d’oxydation de N', series('N suivi', [0, 1, 2, 3], [3, 1, -1, -3])),
             chart('Bilan cumulé, sans cinétique imposée', 'État de la séquence',
                   'Équivalents par nitrobenzène',
                   series('Électrons', [0, 1, 2, 3], [0, 2, 4, 6]),
                   series('Eau', [0, 1, 2, 3], [0, 1, 1, 2]))],
            mechanism_scene('De NO₂ à NH₂ : suivre N et les deux O',
                'Les graphes montrent les espèces neutres de référence. Les trois transitions sont des bilans redox équilibrés ; les formes protonées et le métal réducteur dépendent des conditions.',
                frames, stage),
            REDUCTION_EQUATIONS + [
                'Somme : PhNO₂ + 6 H⁺ + 6 e⁻ → PhNH₂ + 2 H₂O.',
                'En milieu acide : PhNH₂ + H⁺ ⇌ PhNH₃⁺. Ajouter cette protonation si le produit écrit est l’anilinium ; neutraliser permet de récupérer l’aniline.'],
            ['Séquence nitro/nitroso/hydroxylamine/amine utilisée pour établir les bilans ; elle ne détaille pas les étapes élémentaires à une surface métallique.',
             'Les protons et électrons figurent dans les demi-équations. Le bilan complet exige aussi l’oxydation du métal réducteur.',
             'La progression affichée est un index d’espèce, pas un temps ni une conversion calculée.'],
            species=REDUCTION_SPECIES[stage], formula=formulas[stage],
            electron_equivalents=consumed, proton_equivalents=consumed,
            water_equivalents=waters, oxidation_number=[3, 1, -1, -3][stage],
            balances=REDUCTION_BALANCES, reference_pages=[532, 534])

    target = aromatic_structure('Cible : 4-bromo-3-chloro-5-nitroacétophénone',
                                {0: 'COCH3', 2: 'NO2', 3: 'Br', 4: 'Cl'})
    target['formula'] = 'C8H5BrClNO3'
    route = p['route']
    if route == 'bromobenzene':
        group_steps = [{3: 'Br'}, {0: 'COCH3', 3: 'Br'},
                       {0: 'COCH3', 2: 'NO2', 3: 'Br'},
                       {0: 'COCH3', 2: 'NO2', 3: 'Br', 4: 'Cl'}]
        names = ['Bromobenzène', 'Isoler la p-bromoacétophénone après acylation',
                 'Nitration : deux sites équivalents avant NO₂',
                 'Chloration : orientations concordantes à C₃']
        formulas = ['C6H5Br', 'C8H7BrO', 'C8H6BrNO3', 'C8H5BrClNO3']
        frames = [aromatic_structure(name, groups)
                  for name, groups in zip(names, group_steps)]
        for g, formula in zip(frames, formulas):
            g['formula'] = formula
        route_allowed = True
        status = 'Route de banque sous conditions ; séparation para nécessaire'
        statements = [
            'Acylation du bromobenzène par CH₃COCl / AlCl₃ : Br dirige ortho/para. La route choisit et isole le dérivé para, sans prétendre que lui seul se forme.',
            'Nitration de la p-bromoacétophénone : COCH₃ dirige méta et Br ortho ; les deux positions correspondantes sont équivalentes avant introduction de NO₂.',
            'Après nitration, la dernière position visée est méta à COCH₃, méta à NO₂ et ortho à Br. Les trois effets directeurs concordent pour la chloration de la banque.',
            'Une forte désactivation peut imposer des conditions plus exigeantes. L’accord des orientations ne calcule ni vitesse, ni rendement, ni pureté.']
    else:
        initial = aromatic_structure('Nitrobenzène : cycle fortement désactivé', {2: 'NO2'})
        blocked = aromatic_structure('Friedel–Crafts usuelle non retenue : le substrat est conservé', {2: 'NO2'})
        initial['formula'] = blocked['formula'] = 'C6H5NO2'
        frames = [initial, blocked]
        stage = min(stage, 1)
        route_allowed = False
        status = 'Étape incompatible : NO₂ puis acylation de Friedel–Crafts usuelle'
        statements = [
            'Une orientation méta de NO₂ ne rend pas une acylation de Friedel–Crafts accessible.',
            'NO₂ désactive fortement le cycle : la banque CH₃COCl / AlCl₃ ne fournit pas la nitroacétophénone attendue par cette séquence.',
            'La molécule cible existe, mais cette route ne suffit pas à la fabriquer. Chercher un autre ordre d’introduction ou une autre transformation explicitement fournie.',
            'Comparer avec le départ bromobenzène : introduire l’acyle avant les fonctions fortement désactivantes, puis réévaluer les orientations à chaque étape.']
    drawing = mechanism_scene('L’ordre des réactions fait partie de la synthèse',
        status + '. Numérotation finale : COCH₃ en C₁, Cl en C₃, Br en C₄, NO₂ en C₅.',
        frames, stage)
    drawing['target'] = target
    return result(
        [metric('Cible', '4-bromo-3-chloro-5-nitroacétophénone'),
         metric('Formule de la cible', 'C₈H₅BrClNO₃'),
         metric('État de la séquence', stage), metric('Évaluation', status),
         metric('Conclusion quantitative', 'Aucun rendement imposé')], [], drawing,
        statements,
        ['Route conceptuelle sous banque de réactions et conditions adaptées ; une séparation des isomères peut être indispensable.',
         'Le nombre des sites orientés décrit la constitution, pas une statistique de rendement.',
         'Les positions du dessin et la numérotation de la cible sont liées par le même cycle : C₁ à droite, puis numérotation horaire.'],
        allowed=route_allowed, route=route, stage=stage, target=target,
        target_formula='C8H5BrClNO3',
        target_positions={'COCH3': 1, 'Cl': 3, 'Br': 4, 'NO2': 5},
        reference_pages=[532, 534])


def dipolesnitro(p):
    isomer = p['isomer']
    theta = {'ortho': 60, 'meta': 120, 'para': 180}[isomer]
    mu0 = float(p['mu0'])
    rotation = float(p['rotation'])
    # Le bisecteur des deux moments fournit l'axe x avant la rotation rigide.
    half = math.radians(theta / 2)
    local = np.array([[mu0 * math.cos(half), -mu0 * math.sin(half)],
                      [mu0 * math.cos(half), mu0 * math.sin(half)]])
    phi = math.radians(rotation)
    rot = np.array([[math.cos(phi), -math.sin(phi)],
                    [math.sin(phi), math.cos(phi)]])
    # Moment physique : de la charge négative vers la charge positive.
    # NO₂ attire la densité électronique ; le vecteur de groupe choisi
    # pointe ici vers le cycle, à l'opposé de la flèche de polarisation
    # chimique à queue croisée. Ce choix de signe ne change pas les normes.
    moments = -local @ rot.T
    total = moments.sum(axis=0)
    # Annulation symétrique exacte plutôt qu'un artefact à 10^-16.
    if isomer == 'para':
        total[:] = 0
    magnitude = float(np.linalg.norm(total))
    angles = np.linspace(0, 180, 181)
    norms = 2 * mu0 * np.cos(np.radians(angles) / 2)
    norms[-1] = 0
    site = {'ortho': 1, 'meta': 2, 'para': 3}[isomer]
    g = aromatic_structure(f'{isomer.capitalize()}-dinitrobenzène', {0: 'NO2', site: 'NO2'})
    # Les positions initiales des deux groupes sont 0° et θ : tourner
    # aussi le vrai graphe pour aligner ses directions avec φ±θ/2.
    graph_angle = phi - half
    graph_rotation = np.array([[math.cos(graph_angle), -math.sin(graph_angle)],
                               [math.sin(graph_angle), math.cos(graph_angle)]])
    for a in g['atoms']:
        a['x'], a['y'] = (graph_rotation @ np.array([a['x'], a['y']])).tolist()
    vectors = [
        dict(label='μ₁', start=[0., 0.], end=moments[0].tolist(), role='group'),
        dict(label='μ₂', start=[0., 0.], end=moments[1].tolist(), role='group'),
        dict(label='μ₂ translaté', start=moments[0].tolist(), end=total.tolist(), role='construction'),
        dict(label='μ₁ + μ₂', start=[0., 0.], end=total.tolist(), role='resultant'),
    ]
    return result(
        [metric('Isomère', isomer), metric('Angle entre les deux moments', theta, '°'),
         metric('μ₀ dans le modèle', mu0, 'D'), metric('Norme du moment résultant', magnitude, 'D'),
         metric('Composante x après rotation', float(total[0]), 'D'),
         metric('Composante y après rotation', float(total[1]), 'D'),
         metric('Proportions issues de ce calcul', 'Non déterminées')],
        [chart('La somme dépend de l’angle, pas de l’orientation du dessin',
               'Angle entre μ₁ et μ₂ / °', 'Norme de μ₁ + μ₂ / D',
               series('2 μ₀ cos(θ/2)', angles, norms))],
        scene('dipoles', 'Deux moments identiques : construire un parallélogramme',
              'Convention physique : le moment pointe de la charge négative vers la positive, ici vers le cycle pour chaque contribution NO₂. Les deux vecteurs sont translatés à une origine commune. Leur somme est indépendante d’une rotation rigide ; les nombres ne sont pas des proportions de réaction.',
              molecule=g, vectors=vectors, moments=moments, resultant=total,
              magnitude=magnitude, mu0=mu0, unit='D', isomer=isomer,
              angle_deg=theta, rotation_deg=rotation),
        ['Dans ce modèle, chaque groupe apporte un même vecteur de norme μ₀ ; les axes du benzène donnent θ = 60°, 120° ou 180°.',
         'μ² = μ₀² + μ₀² + 2 μ₀² cos θ, donc μ = 2 μ₀ cos(θ/2) pour 0 ≤ θ ≤ 180°.',
         'Ortho : √3 μ₀ ; méta : μ₀ ; para : 0 par symétrie. Avec μ₀ = 4,03 D, cela donne environ 6,98 D, 4,03 D et 0 D.',
         'La rotation modifie μx et μy mais conserve √(μx²+μy²). Une somme de moments n’est pas un calcul de barrières ou de proportions ortho/méta/para.'],
        ['Modèle de deux contributions de groupe identiques et transférables, benzène hexagonal idéal.',
         'Les moments réels dépendent de la structure électronique, de la géométrie et du milieu ; les valeurs calculées sont celles du modèle donné.',
         'Aucune composition du mélange de nitration n’est déduite des dipôles.'],
        angle_deg=theta, magnitude=magnitude, moments=moments,
        resultant=total, mu0=mu0, formula='C6H4N2O4',
        reference_pages=[532, 534])


def group_vector(angle, z):
    angle = math.radians(angle)
    return np.array([math.cos(angle), math.sin(angle), z], dtype=float)


def cip_configuration(vectors, priority):
    """Orientation d'un tétraèdre : z positif est dirigé vers l'observateur."""
    p1, p2, p3, p4 = [np.asarray(vectors[group], dtype=float) for group in priority]
    orientation = np.linalg.det(np.array([p1 - p4, p2 - p4, p3 - p4]))
    return 'R' if orientation < 0 else 'S'


def newman_geometry(configuration, dihedral):
    # Br avant et H arrière occupent l'index 0. Leur séparation azimutale
    # est le dièdre réglable. Le repère géométrique y est orienté vers le haut.
    front = ['Br', 'Et', 'Me'] if configuration[0] == 'R' else ['Br', 'Me', 'Et']
    back = ['H', 'Et', 'Me'] if configuration[1] == 'R' else ['H', 'Me', 'Et']
    base_angles = [90, -30, 210]
    front_vectors = {group: group_vector(angle, 1 / 3)
                     for group, angle in zip(front, base_angles)}
    front_vectors['C4'] = np.array([0., 0., -1.])
    back_vectors = {group: group_vector(angle - dihedral, -1 / 3)
                    for group, angle in zip(back, base_angles)}
    back_vectors['C3'] = np.array([0., 0., 1.])
    # L'affichage Canvas y vers le bas utilise une rotation positive :
    # angle géométrique = angle initial − dièdre, d'où les mêmes rayons.
    return front, back, front_vectors, back_vectors


def central_alkene(configuration):
    right_up = configuration == 'Z'
    sy = 1 if right_up else -1
    return molecule(f'({configuration})-3,4-diméthylhex-3-ène',
        [atom('c3', 'C', -.6, 0), atom('c4', 'C', .6, 0),
         atom('c2', 'C', -1.5, .8, label='CH₂', implicit_h=2),
         atom('c1', 'C', -2.4, .8, label='CH₃', implicit_h=3),
         atom('m3', 'C', -1.5, -.8, label='CH₃', implicit_h=3),
         atom('c5', 'C', 1.5, .8 * sy, label='CH₂', implicit_h=2),
         atom('c6', 'C', 2.4, .8 * sy, label='CH₃', implicit_h=3),
         atom('m4', 'C', 1.5, -.8 * sy, label='CH₃', implicit_h=3)],
        [bond('c3', 'c4', 2), bond('c3', 'c2'), bond('c2', 'c1'),
         bond('c3', 'm3'), bond('c4', 'c5'), bond('c5', 'c6'), bond('c4', 'm4')],
        formula='C8H16', configuration=configuration,
        priority_groups={'c3': 'c2', 'c4': 'c5'})


def substrate_structure(configuration):
    # Squelette semi-développé ; la configuration est rendue par Newman.
    return molecule(f'({configuration[0]}₃,{configuration[1]}₄)-3-bromo-3,4-diméthylhexane',
        [atom('c1', 'C', -2.1, .2, label='CH₃', implicit_h=3),
         atom('c2', 'C', -1.2, 0, label='CH₂', implicit_h=2),
         atom('c3', 'C', -.3, .2), atom('c4', 'C', .7, 0, label='CH', implicit_h=1),
         atom('c5', 'C', 1.6, .2, label='CH₂', implicit_h=2),
         atom('c6', 'C', 2.5, 0, label='CH₃', implicit_h=3),
         atom('br', 'Br', -.3, 1.2),
         atom('m3', 'C', -.3, -.8, label='CH₃', implicit_h=3),
         atom('m4', 'C', .7, -1, label='CH₃', implicit_h=3)],
        [bond('c1', 'c2'), bond('c2', 'c3'), bond('c3', 'c4'),
         bond('c4', 'c5'), bond('c5', 'c6'), bond('c3', 'br'),
         bond('c3', 'm3'), bond('c4', 'm4')], formula='C8H17Br')


def side_alkene_c2(geometry, retained_configuration):
    sy = 1 if geometry == 'Z' else -1
    return molecule(f'({geometry})-3,4-diméthylhex-2-ène ; C₄ de configuration {retained_configuration}',
        [atom('c2', 'C', -.6, 0, label='CH', implicit_h=1),
         atom('c3', 'C', .6, 0), atom('c1', 'C', -1.5, .8, label='CH₃', implicit_h=3),
         atom('m3', 'C', 1.5, -.8 * sy, label='CH₃', implicit_h=3),
         atom('c4', 'C', 1.5, .8 * sy, label='CH', implicit_h=1),
         atom('m4', 'C', 1.5, 1.8 * sy, label='CH₃', implicit_h=3),
         atom('c5', 'C', 2.4, .8 * sy, label='CH₂', implicit_h=2),
         atom('c6', 'C', 3.3, .5 * sy, label='CH₃', implicit_h=3)],
        [bond('c2', 'c3', 2), bond('c2', 'c1'), bond('c3', 'm3'),
         bond('c3', 'c4'), bond('c4', 'm4'), bond('c4', 'c5'), bond('c5', 'c6')],
        formula='C8H16', configuration=geometry,
        priority_groups={'c2': 'c1', 'c3': 'c4'})


def terminal_alkene():
    return molecule('2-éthyl-3-méthylpent-1-ène : pas de configuration E/Z',
        [atom('m3', 'C', -1.1, 0, label='CH₂', implicit_h=2),
         atom('c3', 'C', 0, 0), atom('c2', 'C', 0, 1, label='CH₂', implicit_h=2),
         atom('c1', 'C', -.8, 1.5, label='CH₃', implicit_h=3),
         atom('c4', 'C', 1.1, 0, label='CH', implicit_h=1),
         atom('m4', 'C', 1.1, -.9, label='CH₃', implicit_h=3),
         atom('c5', 'C', 2.1, .3, label='CH₂', implicit_h=2),
         atom('c6', 'C', 3.1, 0, label='CH₃', implicit_h=3)],
        [bond('m3', 'c3', 2), bond('c3', 'c2'), bond('c2', 'c1'),
         bond('c3', 'c4'), bond('c4', 'm4'), bond('c4', 'c5'), bond('c5', 'c6')], formula='C8H16')


def e2stereo(p):
    configuration = p['configuration']
    phi = float(p['dihedral'])
    beta = p['beta']
    front, back, front_vectors, back_vectors = newman_geometry(configuration, phi)
    anti = abs((phi - 180 + 180) % 360 - 180) < 1e-9
    # Dans le Newman anti, projeter les deux groupes prioritaires Et de
    # part et d'autre du plan d'élimination Br–C3–C4–H fournit E ou Z.
    _, _, f_anti, b_anti = newman_geometry(configuration, 180)
    product_configuration = 'E' if f_anti['Et'][0] * b_anti['Et'][0] < 0 else 'Z'
    central = central_alkene(product_configuration)
    substrate = substrate_structure(configuration)
    if beta == 'c4':
        product = central if anti else None
        drawing = scene('newman', 'Regarder C₃ → C₄ et placer Br/H en anti',
            'Point avant C₃ ; cercle arrière C₄. Et = CH₂CH₃ et Me = CH₃. Le produit dessiné appartient à la seule voie C₃=C₄, quand la conformation affichée est anti.',
            variant='e2', angle=phi, front=front, back=back,
            front_center='C₃', back_center='C₄', configuration=configuration,
            product=product, product_configuration=product_configuration,
            reactive=anti, molecule=substrate,
            caption='Élimination concertée anti : Br reçoit le doublet C–Br ; le doublet C–H crée C=C ; la base capte H.')
        actual = central['name'] if anti else 'Tourner vers 180° avant l’E2 anti représentée'
        availability = 'Anti disponible pour H sur C₄' if anti else 'Conformation instantanée non anti'
        beta_note = 'Une rotation autour C₃–C₄ change le dièdre et la conformation ; elle conserve les configurations R/S du substrat.'
        possible_products = [central]
    elif beta == 'c2':
        possible_products = [side_alkene_c2(g, configuration[1]) for g in ['E', 'Z']]
        drawing = reaction_scene('Régiosélectivité : choisir un autre carbone β',
            'C₂ porte deux Hβ. Des conformations anti suivant C₂–C₃ peuvent conduire à E ou Z pour la double liaison C₂=C₃ ; le curseur C₃–C₄ ne teste pas cette anti-périplanarité.',
            [substrate] + possible_products)
        actual = '3,4-diméthylhex-2-ène : E et Z possibles'
        availability = 'Vérifier l’anti autour C₂–C₃, autre axe'
        beta_note = 'C₄ reste stéréogène ; les deux H de C₂ ouvrent des conformations d’élimination distinctes. Ne pas réutiliser automatiquement le produit E/Z de la voie C₄.'
        product = None
    else:
        terminal = terminal_alkene()
        possible_products = [terminal]
        drawing = reaction_scene('Un troisième site β : le méthyle porté par C₃',
            'Retirer H du méthyle branché sur C₃ donne un alcène terminal CH₂=C ; ce carbone porte deux H identiques, donc aucune configuration E/Z.',
            [substrate, terminal])
        actual = terminal['name']
        availability = 'Vérifier l’anti autour C₃–C(méthyle), autre axe'
        beta_note = 'Le produit est CH₂=C(CH₂CH₃)–CH(CH₃)–CH₂CH₃. Compter huit carbones et ne pas attribuer E/Z à CH₂=C.'
        product = None
    return result(
        [metric('Substrat', f'(3{configuration[0]},4{configuration[1]})'),
         metric('Sites β portant H', 'C₂, C₄, méthyle sur C₃'),
         metric('Dièdre Br–C₃–C₄–H', phi, '°'), metric('Géométrie', availability),
         metric('Voie C₃=C₄ à l’anti', product_configuration),
         metric('Produit de la voie sélectionnée', actual),
         metric('Proportion de cette voie', 'Non calculée')], [], drawing,
        ['Priorités sur C₃ : Br > branche C₄ > Et > Me. Sur C₄ : branche C₃ > Et > Me > H.',
         'Pour la voie C₄, placer Br et H à 180°. L’élimination concertée relie une configuration du réactif à une géométrie E/Z du produit.',
         '(3S,4S) et (3R,4R) donnent E ; (3S,4R) et (3R,4S) donnent Z pour cette voie anti.',
         beta_note,
         'Stéréospécificité : quelle géométrie pour une voie donnée ? Régiosélectivité : quelle double liaison parmi les positions possibles ? Zaïtsev seul ne calcule pas leurs proportions.'],
        ['Substrat exact du recueil : 3-bromo-3,4-diméthylhexane. Les choix R/S sont construits par un repère tétraédrique de Newman, vérifiable par CIP.',
         'À dièdre non anti, on décrit une conformation figée ; en solution, la molécule peut tourner pour rejoindre une conformation réactive.',
         'L’illustration de la voie principale conserve l’inventaire C₈H₁₇Br → C₈H₁₆ + HBr au bilan moléculaire. Avec une base B⁻, écrire plutôt BH + Br⁻.',
         'Les autres sites β sont comparés sans constantes de vitesse ni rendements imposés.'],
        configuration=configuration, front_vectors=front_vectors, back_vectors=back_vectors,
        front_priority=['Br', 'C4', 'Et', 'Me'], back_priority=['C3', 'Et', 'Me', 'H'],
        anti=anti, beta=beta, product_configuration=product_configuration,
        product=product, possible_products=possible_products,
        substrate_formula='C8H17Br', product_formula='C8H16',
        reference_pages=[531, 533])


CALCULATIONS = {'nitrobenzene': nitrobenzene, 'dipolesnitro': dipolesnitro,
                'e2stereo': e2stereo}


def calculate(lab_id, params):
    if lab_id not in CALCULATIONS:
        raise ValueError('Exercice du recueil inconnu.')
    return clean(CALCULATIONS[lab_id](params))
