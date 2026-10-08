"""Formation et ouverture des époxydes : banque ciblée du recueil."""
from commun import lab, select, slider, preset


LABS = [lab('epoxydes', 'Époxydes : transférer O puis ouvrir le cycle',
    'Transformations du recueil · 524–528',
    'Comparer époxydation par peracide et procédé à l’argent sur l’éthylène ; suivre une ouverture anti et distinguer les sites d’attaque en milieu basique ou acide.',
    [select('substrate', 'Alcène de référence et époxyde correspondant', [
        ('ethylene', 'Éthylène : oxyde d’éthylène'),
        ('propene', 'Propène : oxyde de propylène'),
        ('butene_E', '(E)-but-2-ène : époxyde trans'),
        ('butene_Z', '(Z)-but-2-ène : époxyde cis')], 'propene'),
     select('mode', 'Transformation et conditions', [
        ('peracid', 'Peracide : transfert concerté d’un O'),
        ('silver', 'O₂ / Ag : cas industriel de l’éthylène'),
        ('basic', 'Ouverture par HO⁻ ou MeO⁻, puis traitement'),
        ('acid', 'Ouverture acido-catalysée par H₂O ou MeOH')], 'peracid'),
     select('nucleophile', 'Famille du nucléophile pour l’ouverture', [
         ('water', 'H₂O / HO⁻ : obtenir un diol'),
         ('methoxide', 'MeOH / MeO⁻ : obtenir un méthoxyalcool')], 'water'),
     slider('stage', 'État de la transformation ou du mécanisme', 0, 3, 1, 0, integer=True)],
    [preset('Propène + peracide : deux énantiomères', mode='peracid', substrate='propene', stage=1),
     preset('E devient époxyde trans', mode='peracid', substrate='butene_E', stage=1),
     preset('Z devient époxyde cis', mode='peracid', substrate='butene_Z', stage=1),
     preset('Éthylène et dioxygène sur argent', mode='silver', substrate='ethylene', stage=1),
     preset('Argent et propène : hors de cette banque', mode='silver', substrate='propene'),
     preset('MeO⁻ attaque le carbone le moins substitué', mode='basic', substrate='propene', nucleophile='methoxide', stage=1),
     preset('MeOH en milieu acide : site plus substitué', mode='acid', substrate='propene', nucleophile='methoxide', stage=2),
     preset('Diol après ouverture anti', mode='basic', substrate='butene_Z', nucleophile='water', stage=2)])]
