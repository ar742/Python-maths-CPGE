"""Expériences centrées sur les deux exercices du recueil, pages 531–534."""
from commun import lab, select, slider, preset


LABS = [
    lab('nitrobenzene', 'Nitrobenzène : Lewis, réduction et ordre des substitutions',
        'Exercices du recueil · 531–534',
        'Suivre le groupe nitro sans perdre ses charges, équilibrer sa réduction en aniline et vérifier une séquence de substitutions sur une cible aromatique à quatre substituants.',
        [select('mode', 'Question de l’exercice', [
            ('lewis', 'Lewis et mésomérie du groupe nitro'),
            ('reduction', 'Nitro → nitroso → hydroxylamine → aniline'),
            ('strategy', 'Cible aromatique : ordonner les réactions')], 'lewis'),
         select('contributor', 'Contributeur de Lewis', [
             ('oxygen_a', 'Liaison double vers Oₐ'),
             ('oxygen_b', 'Liaison double vers Oᵦ')], 'oxygen_a'),
         select('route', 'Séquence à examiner', [
             ('bromobenzene', 'Bromobenzène : acyler, nitrer, chlorer'),
             ('nitro_first', 'Nitrobenzène : tenter ensuite Friedel–Crafts')], 'bromobenzene'),
         slider('stage', 'État de la réduction ou de la stratégie', 0, 3, 1, 0, integer=True)],
        [preset('Deux N–O, un seul nitrobenzène', mode='lewis', contributor='oxygen_a'),
         preset('Déplacer les électrons, garder les noyaux', mode='lewis', contributor='oxygen_b'),
         preset('Nitrosobenzène : première étape de 2 électrons', mode='reduction', stage=1),
         preset('Aniline : bilan complet à 6 électrons', mode='reduction', stage=3),
         preset('Cible à quatre substituants', mode='strategy', route='bromobenzene', stage=3),
         preset('Friedel–Crafts après nitration : étape incompatible', mode='strategy', route='nitro_first', stage=1)]),
    lab('dipolesnitro', 'Dinitrobenzènes : addition vectorielle des moments dipolaires',
        'Exercices du recueil · 531–534',
        'Construire géométriquement les dipôles ortho, méta et para avec deux groupes identiques ; distinguer propriété d’une molécule et composition d’un mélange réactionnel.',
        [select('isomer', 'Position du second groupe NO₂', [
            ('ortho', 'Ortho : 1,2'), ('meta', 'Méta : 1,3'), ('para', 'Para : 1,4')], 'ortho'),
         slider('mu0', 'Moment de chaque groupe dans le modèle', 0, 8, .01, 4.03, 'D'),
         slider('rotation', 'Rotation rigide de la molécule', 0, 360, 5, 0, '°')],
        [preset('Ortho : √3 μ₀', isomer='ortho', mu0=4.03, rotation=0),
         preset('Méta : μ₀', isomer='meta', mu0=4.03, rotation=0),
         preset('Para : annulation par symétrie', isomer='para', mu0=4.03, rotation=0),
         preset('Tourner sans changer la norme', isomer='ortho', mu0=4.03, rotation=90)]),
    lab('e2stereo', 'E2 du recueil : des configurations R/S à l’alcène E/Z',
        'Exercices du recueil · 531–534',
        'Projeter le 3-bromo-3,4-diméthylhexane suivant C₃–C₄ ; placer Hβ et Br en anti, puis comparer stéréospécificité du produit et choix du carbone β.',
        [select('configuration', 'Configuration du substrat (C₃, C₄)', [
            ('SS', '(3S,4S)'), ('RR', '(3R,4R)'),
            ('SR', '(3S,4R)'), ('RS', '(3R,4S)')], 'SS'),
         slider('dihedral', 'Dièdre Br–C₃–C₄–Hβ', 0, 360, 5, 180, '°'),
         select('beta', 'Carbone β où l’on retire H', [
             ('c4', 'C₄ : alcène C₃=C₄ de l’exercice'),
             ('c2', 'C₂ : autre position dans la chaîne'),
             ('methyl', 'Méthyle porté par C₃ : alcène terminal')], 'c4')],
        [preset('SS en anti → E', configuration='SS', dihedral=180, beta='c4'),
         preset('RR en anti → E', configuration='RR', dihedral=180, beta='c4'),
         preset('SR en anti → Z', configuration='SR', dihedral=180, beta='c4'),
         preset('RS en anti → Z', configuration='RS', dihedral=180, beta='c4'),
         preset('Tourner : le substrat reste SS', configuration='SS', dihedral=60, beta='c4'),
         preset('Éliminer vers un autre carbone β', configuration='SS', beta='c2')])
]
