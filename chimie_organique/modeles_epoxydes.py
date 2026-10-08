"""Époxydation et ouverture : charges, atomes et stéréochimie contrôlés."""
from __future__ import annotations
import copy
import numpy as np
from commun import (atom, bond, molecule, electron_arrow, metric,
                    mechanism_scene, clean)


def result(metrics, drawing, steps, assumptions, **extra):
    return dict(metrics=metrics, charts=[], scene=drawing, steps=steps,
                assumptions=assumptions, **extra)


def alkene(substrate):
    g = molecule({'ethylene': 'Éthylène', 'propene': 'Propène',
                  'butene_E': '(E)-but-2-ène', 'butene_Z': '(Z)-but-2-ène'}[substrate],
        [atom('c1', 'C', -.6, 0, label='CH₂' if substrate in ('ethylene', 'propene') else 'CH',
              implicit_h=2 if substrate in ('ethylene', 'propene') else 1),
         atom('c2', 'C', .6, 0, label='CH₂' if substrate == 'ethylene' else 'CH',
              implicit_h=2 if substrate == 'ethylene' else 1)], [bond('c1', 'c2', 2)])
    if substrate.startswith('butene'):
        g['atoms'].append(atom('m1', 'C', -1.4, .7, label='CH₃', implicit_h=3))
        g['bonds'].append(bond('c1', 'm1'))
    if substrate != 'ethylene':
        y = -.7 if substrate == 'butene_E' else .7
        g['atoms'].append(atom('m2', 'C', 1.4, y, label='CH₃', implicit_h=3))
        g['bonds'].append(bond('c2', 'm2'))
    return g


def epoxide(substrate, mirror=False):
    g = molecule({'ethylene': 'Oxyde d’éthylène', 'propene': 'Oxyde de propylène : un énantiomère',
                  'butene_E': 'trans-2,3-diméthyloxirane : un énantiomère',
                  'butene_Z': 'cis-2,3-diméthyloxirane : méso'}[substrate],
        [atom('c1', 'C', -.6, 0, label='CH₂' if substrate in ('ethylene', 'propene') else 'C',
              implicit_h=2 if substrate in ('ethylene', 'propene') else 0),
         atom('c2', 'C', .6, 0, label='CH₂' if substrate == 'ethylene' else 'C',
              implicit_h=2 if substrate == 'ethylene' else 0),
         atom('ox', 'O', 0, .95, lone_pairs=2)],
        [bond('c1', 'c2'), bond('c1', 'ox'), bond('c2', 'ox')])
    for i, side in [(1, -1), (2, 1)]:
        if (i == 1 and not substrate.startswith('butene')) or (i == 2 and substrate == 'ethylene'):
            continue
        style = 'dash' if i == 2 and substrate == 'butene_E' else 'wedge'
        if mirror:
            style = 'dash' if style == 'wedge' else 'wedge'
        g['atoms'].extend([atom(f'm{i}', 'C', side * 1.5, -.65, label='CH₃', implicit_h=3),
                           atom(f'h{i}', 'H', side * 1.45, .6)])
        g['bonds'].extend([bond(f'c{i}', f'm{i}', style=style),
                           bond(f'c{i}', f'h{i}', style='dash' if style == 'wedge' else 'wedge')])
    g['configuration_relation'] = 'cis' if substrate == 'butene_Z' else 'trans' if substrate == 'butene_E' else 'sans objet'
    g['configurations'] = stereocenters(g)
    return g


def center_configuration(graph, center, priorities):
    """CIP sur la perspective locale : deux liaisons planes, coin et hachures."""
    atoms = {a['id']: a for a in graph['atoms']}
    c = atoms[center]
    vectors = {}
    for group in priorities:
        a = atoms[group]
        b = next(b for b in graph['bonds'] if {b['a'], b['b']} == {center, group})
        style = b.get('style', '')
        z = 1. if style == 'wedge' else -1. if style in ('dash', 'hashed') else 0.
        vectors[group] = np.array([a['x'] - c['x'], a['y'] - c['y'], z])
    p1, p2, p3, p4 = [vectors[x] for x in priorities]
    signed = np.dot(p1 - p4, np.cross(p2 - p4, p3 - p4))
    if abs(signed) < 1e-10:
        raise ArithmeticError('Perspective stéréochimique dégénérée.')
    return 'R' if signed < 0 else 'S'


def stereocenters(graph):
    atoms = {a['id'] for a in graph['atoms']}
    configurations = {}
    for i in [1, 2]:
        if f'h{i}' not in atoms:
            continue
        center = f'c{i}'
        neighbor = f'c{3-i}'
        oxygen = next((b['b'] if b['a'] == center else b['a']
                        for b in graph['bonds']
                        if center in (b['a'], b['b']) and
                        (b['b'] if b['a'] == center else b['a']) in ('ox', 'nu')), None)
        if oxygen:
            configurations[center] = center_configuration(graph, center,
                                                            [oxygen, neighbor, f'm{i}', f'h{i}'])
    return configurations


def carboxylic(peracid=True):
    g = molecule('Acide peréthanoïque' if peracid else 'Acide éthanoïque',
        [atom('ac', 'C', 0, 0), atom('m', 'C', -1, 0, label='CH₃', implicit_h=3),
         atom('carbonyl', 'O', 0, 1, lone_pairs=2), atom('ester_o', 'O', 1, 0, lone_pairs=2),
         atom('h', 'H', 2.5 if peracid else 1.8, 0)],
        [bond('ac', 'm'), bond('ac', 'carbonyl', 2)])
    if peracid:
        g['atoms'].append(atom('transfer_o', 'O', 1.8, 0, lone_pairs=2))
        g['bonds'].extend([bond('ac', 'ester_o'), bond('ester_o', 'transfer_o'), bond('transfer_o', 'h')])
    else:
        g['bonds'].extend([bond('ac', 'ester_o'), bond('ester_o', 'h')])
    return g


def combined(name, graphs, spacing=4.8):
    atoms, bonds, arrows = [], [], []
    n = len(graphs)
    components = []
    for i, graph in enumerate(graphs):
        offset = (i - (n - 1) / 2) * spacing
        prefix = f'g{i}_'
        components.append(dict(name=graph['name'], offset=offset))
        for a in graph['atoms']:
            a = copy.deepcopy(a)
            a['id'] = prefix + a['id']
            a['x'] += offset
            atoms.append(a)
        for b in graph['bonds']:
            b = copy.deepcopy(b)
            b['a'], b['b'] = prefix + b['a'], prefix + b['b']
            bonds.append(b)
        for arr in graph.get('arrows', []):
            arr = copy.deepcopy(arr)
            for key in ['start', 'end', 'control']:
                if key in arr:
                    arr[key][0] += offset
            arrows.append(arr)
    return molecule(name, atoms, bonds, arrows, components=components)


def mirror_graph(graph):
    g = copy.deepcopy(graph)
    for b in g['bonds']:
        if b.get('style') in ('wedge', 'dash'):
            b['style'] = 'dash' if b['style'] == 'wedge' else 'wedge'
    g['configurations'] = stereocenters(g)
    return g


def opening_nucleophile(methoxy, basic):
    atoms = [atom('nu', 'O', 3.4, 0, charge=-1 if basic else 0,
                  lone_pairs=3 if basic else 2)]
    bonds = []
    if methoxy:
        atoms.append(atom('nu_m', 'C', 4.3, 0, label='CH₃', implicit_h=3))
        bonds.append(bond('nu', 'nu_m'))
    for i in range(1 if (basic or methoxy) else 2):
        if methoxy and basic:
            break
        hid = f'nu_h{i}'
        atoms.append(atom(hid, 'H', 4.1, .55 if i == 0 else -.55))
        bonds.append(bond('nu', hid))
    return molecule('MeO⁻' if methoxy and basic else 'HO⁻' if basic else 'MeOH' if methoxy else 'H₂O', atoms, bonds)


def append_graph(destination, graph):
    destination['atoms'].extend(copy.deepcopy(graph['atoms']))
    destination['bonds'].extend(copy.deepcopy(graph['bonds']))


def opening_frames(substrate, methoxy, basic):
    g = epoxide(substrate)
    initial_configs = dict(g['configurations'])
    append_graph(g, opening_nucleophile(methoxy, basic))
    if basic:
        append_graph(g, molecule('H₂O réservée au traitement final',
            [atom('water_o', 'O', 5.4, 0, lone_pairs=2),
             atom('water_h0', 'H', 6.1, .45), atom('water_h1', 'H', 6.1, -.45)],
            [bond('water_o', 'water_h0'), bond('water_o', 'water_h1')]))
    else:
        g['atoms'].append(atom('acid_h', 'H', -2.5, 1.1, charge=1))
    target = 'c2' if not basic and substrate == 'propene' else 'c1'
    frames = []
    if not basic:
        g['name'] = 'Époxyde + H⁺ + nucléophile neutre'
        g['arrows'] = [electron_arrow([0, 1.1], [-2.5, 1.1], [-1.4, 1.9], label='O → H⁺')]
        frames.append(copy.deepcopy(g))
        for a in g['atoms']:
            if a['id'] == 'acid_h':
                a.update(x=0., y=1.65, charge=0)
            if a['id'] == 'ox':
                a.update(charge=1, lone_pairs=1)
        g['bonds'].append(bond('ox', 'acid_h'))
    g['name'] = 'Nu⁻ et époxyde ; eau réservée au traitement' if basic else 'Époxyde protoné : O possède trois liaisons et +1'
    tx = -.6 if target == 'c1' else .6
    g['arrows'] = [
        electron_arrow([3.4, .1], [tx, 0], [1.4, -1.6], label='Nu → C visé'),
        electron_arrow([tx / 2, .475], [0, .95], [tx - .45, 1.05], label='C–O → O'),
    ]
    frames.append(copy.deepcopy(g))
    g['bonds'] = [b for b in g['bonds'] if {b['a'], b['b']} != {target, 'ox'}]
    g['bonds'].append(bond(target, 'nu'))
    shift = np.array([tx - 3.4, -1.05])
    for a in g['atoms']:
        if a['id'].startswith('nu'):
            a['x'], a['y'] = (np.array([a['x'], a['y']]) + shift).tolist()
        if a['id'] == 'ox':
            a.update(charge=-1 if basic else 0, lone_pairs=3 if basic else 2)
        if a['id'] == 'nu':
            a.update(charge=0 if basic else 1, lone_pairs=2 if basic else 1)
    # Les coordonnées planes changent quand le cycle s'ouvre. Ajuster les
    # deux liaisons de perspective du C attaqué pour rendre sans ambiguïté
    # l'inversion physique ; le C non attaqué conserve sa configuration.
    if target in initial_configs:
        desired = 'S' if initial_configs[target] == 'R' else 'R'
        current = stereocenters(g)[target]
        if current != desired:
            for b in g['bonds']:
                if {b['a'], b['b']} in ({target, f'm{target[1]}'}, {target, f'h{target[1]}'}):
                    b['style'] = 'dash' if b.get('style') == 'wedge' else 'wedge'
    g['configurations'] = stereocenters(g)
    g['name'] = 'Cycle ouvert : alkoxide à protoner' if basic else 'Cycle ouvert : nucléophile oxonium à déprotoner'
    if basic:
        g['arrows'] = [electron_arrow([0, 1.05], [6.1, .45], [2.8, 2.3], label='O⁻ → H de l’eau'),
                       electron_arrow([5.75, .225], [5.4, 0], [5.6, 1.1], label='O–H → O')]
    else:
        # −H⁺ est une étape de bilan : le solvant est l'accepteur de proton.
        # Pas de flèche qui prétendrait détailler ce transfert sans sa base.
        g['arrows'] = []
    frames.append(copy.deepcopy(g))
    if basic:
        atoms = {a['id']: a for a in g['atoms']}
        atoms['ox'].update(charge=0, lone_pairs=2)
        atoms['water_o'].update(charge=-1, lone_pairs=3)
        atoms['water_h0'].update(x=.4, y=1.6)
        g['bonds'] = [b for b in g['bonds'] if {b['a'], b['b']} != {'water_o', 'water_h0'}]
        g['bonds'].append(bond('ox', 'water_h0'))
    else:
        atoms = {a['id']: a for a in g['atoms']}
        atoms['nu'].update(charge=0, lone_pairs=2)
        atoms['nu_h0'].update(x=-2.5, y=1.1, charge=1)
        g['bonds'] = [b for b in g['bonds'] if {b['a'], b['b']} != {'nu', 'nu_h0'}]
    g['name'] = 'Produit neutre + HO⁻ du traitement' if basic else 'Produit neutre + H⁺ restitué'
    g['arrows'] = []
    frames.append(copy.deepcopy(g))
    if not basic:
        product_atoms = [a for a in g['atoms'] if a['id'] != 'nu_h0']
    else:
        product_atoms = [a for a in g['atoms'] if a['id'] not in ('water_o', 'water_h1')]
    product_ids = {a['id'] for a in product_atoms}
    product = molecule('Méthoxyalcool' if methoxy else 'Diol vicinal',
        copy.deepcopy(product_atoms),
        [copy.deepcopy(b) for b in g['bonds'] if b['a'] in product_ids and b['b'] in product_ids],
        configurations=stereocenters(g))
    return frames, target, initial_configs, product


def epoxydes(p):
    substrate, mode = p['substrate'], p['mode']
    stage = int(p['stage'])
    if mode == 'silver':
        allowed = substrate == 'ethylene'
        if allowed:
            dioxygen = molecule('Dioxygène', [atom('o1', 'O', -.5, 0, lone_pairs=2),
                                              atom('o2', 'O', .5, 0, lone_pairs=2)], [bond('o1', 'o2', 2)])
            frames = [combined('Bilan : deux éthylènes et un dioxygène', [alkene('ethylene'), dioxygen, alkene('ethylene')]),
                      combined('Deux oxydes d’éthylène au bilan', [epoxide('ethylene'), epoxide('ethylene')])]
            steps = ['2 C₂H₄ + O₂ → 2 C₂H₄O, catalyse par Ag.',
                     'Un O est incorporé dans chaque molécule d’oxyde d’éthylène ; l’équation équilibre C, H et O.',
                     'La combustion complète est une voie concurrente : C₂H₄ + 3 O₂ → 2 CO₂ + 2 H₂O. La présence d’Ag ne signifie donc pas une sélectivité de 100 %.']
            conclusion = 'Éthylène : transformation de la banque industrielle'
        else:
            frames = [alkene(substrate)]
            steps = ['La banque O₂ / Ag présentée ici concerne l’éthylène.',
                     'Pour le substrat choisi, aucune structure de produit ni sélectivité n’est prédite par cette banque.',
                     'Comparer avec la voie peracide, documentée pour les alcènes proposés.']
            conclusion = 'Cas non couvert par le procédé éthylène / Ag'
        stage = min(stage, len(frames) - 1)
        return result([metric('Applicabilité', conclusion),
                       metric('Bilan pour l’éthylène', '2 C₂H₄ + O₂ → 2 C₂H₄O'),
                       metric('Catalyseur', 'Ag'), metric('Sélectivité', 'Non fixée à 100 %')],
            mechanism_scene('Le domaine d’une réaction compte autant que son nom',
                conclusion + '. Les dessins sont des bilans, pas un mécanisme de surface.', frames, stage),
            steps, ['Comparaison de principes de synthèse, sans protocole opératoire.',
                    'Le mécanisme de catalyse hétérogène et les rendements nécessitent des données supplémentaires.'],
            allowed=allowed, stage=stage, equation='2 C2H4 + O2 -> 2 C2H4O',
            reference_pages=[528])
    if mode == 'peracid':
        first = combined('Alcène + acide peréthanoïque', [alkene(substrate), carboxylic(True)])
        epox = epoxide(substrate)
        final = combined('Époxyde + acide éthanoïque', [epox, carboxylic(False)])
        frames = [first, final]
        stage = min(stage, 1)
        stereo = {'ethylene': 'Achiral', 'propene': 'Racémique : deux faces équivalentes',
                  'butene_E': 'Époxyde trans, racémique',
                  'butene_Z': 'Époxyde cis, méso'}[substrate]
        products = [epox] if substrate in ('ethylene', 'butene_Z') else [epox, mirror_graph(epox)]
        return result([metric('Réactif', 'Peracide R–C(=O)–O–OH'),
                       metric('O transféré par alcène', 1), metric('Coproduit', 'Acide carboxylique'),
                       metric('Stéréochimie', stereo), metric('Carbocation libre', 'Absent de ce mécanisme concerté')],
            mechanism_scene('Époxydation : un transfert concerté d’oxygène',
                'Le bilan avant/après montre l’incorporation d’un O et l’acide coproduct. La relation cis/trans des substituants est conservée ; un seul représentant est dessiné si deux énantiomères se forment.',
                frames, stage),
            ['Alcène + RCO₃H → époxyde + RCO₂H. L’oxygène transféré est celui du groupe peroxyde terminal.',
             'La formation des deux liaisons C–O est concertée : aucun carbocation libre n’autorise ici une rotation effaçant la relation E/Z.',
             '(E)-but-2-ène → époxyde trans racémique ; (Z)-but-2-ène → époxyde cis méso, dans un milieu achiral.',
             'Le propène peut réagir par ses deux faces énantiotopiques : l’oxyde de propylène est racémique sans réactif ou catalyseur chiral.'],
            ['Acide peréthanoïque choisi comme exemple de peracide ; bilan structural concerté avant/après.',
             'Les dessins ne prétendent pas décrire des intermédiaires isolables ou imposer un rendement.',
             'Les coins/hachures de l’époxyde rendent la relation des substituants explicite.'],
            allowed=True, stage=stage, product=epox, products=products,
            stereo_summary=stereo,
            atom_transfer={'source': 'g1_transfer_o', 'destination': 'g0_ox'},
            reference_pages=[526, 528])
    basic = mode == 'basic'
    methoxy = p['nucleophile'] == 'methoxide'
    frames, target, initial_configurations, product = opening_frames(substrate, methoxy, basic)
    stage = min(stage, len(frames) - 1)
    site = 'moins substitué' if substrate == 'propene' and basic else 'plus substitué' if substrate == 'propene' else 'sites de constitution équivalente'
    formula = {'ethylene': 'C2H6O2' if not methoxy else 'C3H8O2',
               'propene': 'C3H8O2' if not methoxy else 'C4H10O2',
               'butene_E': 'C4H10O2' if not methoxy else 'C5H12O2',
               'butene_Z': 'C4H10O2' if not methoxy else 'C5H12O2'}[substrate]
    product['formula'] = formula
    if substrate == 'ethylene':
        stereo = 'Produit achiral'
    elif substrate == 'butene_E' and not methoxy:
        stereo = 'Diol méso après ouverture anti du trans-époxyde'
    else:
        stereo = 'Mélange racémique ; un énantiomère représenté'
    if substrate == 'propene' and methoxy:
        product['name'] = '1-méthoxypropan-2-ol' if basic else '2-méthoxypropan-1-ol'
    statements = [
        'En base, Nu⁻ attaque par l’arrière ; le cycle se rompt au C le moins encombré. Le O initial devient alkoxide puis reçoit un proton au traitement.' if basic else
        'En acide, protoner d’abord O active l’époxyde. H₂O ou MeOH attaque par l’arrière ; pour l’oxyde de propylène, le C plus substitué est retenu dans cette banque.',
        'La liaison entre le C attaqué et le O initial cède son doublet à O ; le nucléophile forme simultanément sa liaison C–O.',
        'Le C attaqué s’inverse s’il est stéréogène ; la géométrie du C non attaqué est conservée. L’ouverture est anti, sans carbocation libre autorisant une rotation arbitraire.',
        'HO⁻ donne un diol après protonation ; MeO⁻ donne un méthoxyalcool. Sous catalyse acide, employer les espèces neutres H₂O ou MeOH, puis déprotoner l’oxonium.',
        'La région attaquée et la stéréochimie répondent à deux questions distinctes. Les proportions exactes restent dépendantes des conditions et ne sont pas inventées.']
    return result([metric('Milieu', 'Basique' if basic else 'Acido-catalysé'),
                   metric('Nucléophile attaquant', 'MeO⁻' if basic and methoxy else 'HO⁻' if basic else 'MeOH' if methoxy else 'H₂O'),
                   metric('Carbone attaqué', target.upper() + ' : ' + site),
                   metric('Produit', product['name']), metric('Formule du produit', formula),
                   metric('Stéréochimie', stereo),
                   metric('Charge du système figuré', -1 if basic else 1, 'e')],
        mechanism_scene('Ouvrir un époxyde : conserver atomes, charges et géométrie',
            'Chaque état inclut les espèces nécessaires au bilan. En base, H₂O est réservée au traitement final ; en acide, le proton est restitué à la dernière étape. Les produits sont dessinés en perspective.',
            frames, stage), statements,
        ['Comparaison d’une banque de réactions sur quatre squelettes simples ; la préférence de site en acide est donnée pour le cas propylène étudié.',
         'Le curseur parcourt des états du mécanisme, pas un temps ou un rendement.',
         'Les espèces HO⁻ ou H⁺ finales permettent de comparer des systèmes de même inventaire. L’eau de traitement basique n’est pas un ajout conseillé dès le début de la réaction.',
         'La déprotonation acide finale est un bilan −H⁺ ; l’accepteur de proton est le solvant et sa molécule n’est pas détaillée dans cette dernière transition.',
         'Époxyde issu d’un alcène en milieu achiral : une perspective représentative ne signifie pas un produit énantiopur.'],
        allowed=True, stage=stage, attack_carbon=target, product=product,
        initial_configurations=initial_configurations,
        final_configurations=product['configurations'], stereo_summary=stereo,
        product_formula=formula, system_charge=-1 if basic else 1,
        reference_pages=[526, 528])


def calculate(lab_id, params):
    if lab_id != 'epoxydes':
        raise ValueError('Laboratoire époxyde inconnu.')
    return clean(epoxydes(params))
