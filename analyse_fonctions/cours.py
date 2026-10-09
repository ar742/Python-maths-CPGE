"""Leçons, exercices et références, dans l’ordre des expériences."""
from contenu_speciales import LESSONS as LS, EXERCISES as ES, SOURCES as SS
from contenu_theoremes import LESSONS as LT, EXERCISES as ET
from contenu_edo import LESSONS as LE, EXERCISES as EE
from catalogue import LABS
order = {lab['id']:i for i,lab in enumerate(LABS)}
LESSONS = sorted(LS + LT + LE, key=lambda item:order[item['lab']])
EXERCISES = sorted(ES + ET + EE, key=lambda item:order[item['lab']])
SOURCES = [
    'Source principale : extrait du recueil de A. R., fonctions spéciales p.48, équations fonctionnelles p.52, dérivées et intégrales p.56–67, EDO p.68–72. Les numéros sont ceux des pages imprimées. Le PDF personnel n’est pas redistribué.',
    'Priorité : les trois théorèmes de la page 63, avec six applications, et les équations différentielles, avec dix laboratoires. Les domaines et les hypothèses de domination par une fonction intégrable sont explicités avant les échanges limite / intégrale et dérivation / intégrale.',
    '<a href="https://dlmf.nist.gov/5">NIST DLMF : fonctions gamma et bêta</a> ; <a href="https://dlmf.nist.gov/25">fonction zêta</a> ; <a href="https://dlmf.nist.gov/18">polynômes orthogonaux, dont Hermite</a>.',
    '<a href="https://prepas.org/ups.php?document=69">Programme MPSI</a> et <a href="https://prepas.org/ups.php?document=85">programme MP</a> : continuité, dérivation, intégration, équations différentielles linéaires et outils numériques. Les champs non linéaires, les fonctions spéciales et le calcul fractionnaire sont accompagnés comme prolongements.',
    'Convention : polynômes d’Hermite des physiciens, Hₙ(x)=(-1)ⁿ e^(x²) (dⁿ/dxⁿ)e^(-x²). Fractionnaires : borne inférieure 0 ; Riemann–Liouville et Caputo sont distinguées. Pour les équations fonctionnelles, la régularité fait partie des hypothèses de classification.',
    'Un calcul fini suggère et contrôle un résultat ; il ne démontre ni une identité sur un domaine infini, ni une convergence, ni l’existence d’une majorante intégrable.'
]
SOURCES += [f'<a href="{s["url"]}">{s["title"]}</a>.' for s in SS]
