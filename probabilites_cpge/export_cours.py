"""Exporter la version autonome du cours : python export_cours.py."""
from pathlib import Path
import html
import re
from cours import LESSONS, EXERCISES, SOURCES


def prose(value):
    value = re.sub(r'<br\s*/?>', '\n', value)
    value = re.sub(r'<(?:p|div)[^>]*>', '', value)
    value = re.sub(r'</(?:p|div)>', '\n\n', value)
    value = value.replace('<b>', '**').replace('</b>', '**')
    return html.unescape(re.sub(r'<[^>]*>', '', value)).strip()


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name('COURS.md')
    parts = ['# Probabilités & Expériences — cours et exercices\n',
             'Volet 03 de Python-maths-CPGE. Priorité aux exercices 6, 7 et 8 de la fiche M12.\n',
             'Les résultats théoriques et les observations simulées sont distingués. Les approfondissements sont signalés.\n']
    for lesson in LESSONS:
        parts.extend(['## '+lesson['title']+'\n', '*'+lesson['level']+'*\n', prose(lesson['html'])+'\n'])
    parts.append('## Exercices corrigés\n')
    for exercise in EXERCISES:
        parts.extend(['### '+exercise['title']+'\n', exercise['question']+'\n', '**Correction.** '+exercise['answer']+'\n'])
    parts.append('## Sources et conventions\n')
    parts.extend(source+'\n' for source in SOURCES)
    path.write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    return path


from reperes import LAB_GUIDES

LAB_TITLES = {'polarisation': 'La moyenne conservée et la polarisation', 'extremes': 'Maximum, minimum et rang', 'arcsinus': 'Cosinus et loi arcsinus', 'wigner': 'Matrices aléatoires et demi-cercle', 'urne': 'Urnes et dépendance', 'fluctuations': 'Marche, fréquences et fluctuations'}


def export_parcours(path=None):
    """Conserver le parcours initial et actualiser uniquement ses guides."""
    path = Path(path) if path else Path(__file__).with_name('PARCOURS.md')
    marker = '<!-- REPERES_EXPERIENCES -->'
    base = path.read_text(encoding='utf-8').split(marker)[0].rstrip() if path.exists() else '# Parcours : prévoir, expérimenter, démontrer'
    parts = [base, marker, '## Guides des expériences',
             'Les repères distinguent les outils de sup, ceux de spé et les prolongements. '
             'Ils s’appuient sur les programmes de mathématiques [MPSI](https://prepas.org/ups.php?document=69) '
             'et [MP](https://prepas.org/ups.php?document=85).']
    for ident, guide in LAB_GUIDES.items():
        parts.extend(['### '+LAB_TITLES[ident], guide['purpose'], '**Objets et notations**'])
        parts.extend('- '+value for value in guide['objects'])
        parts.append('**Hypothèses**')
        parts.extend('- '+value for value in guide['hypotheses'])
        parts.append('**Techniques à mobiliser**')
        parts.extend('- '+value for value in guide['techniques'])
        parts.append('**Trois premières manipulations**')
        parts.extend(str(i)+'. '+value for i,value in enumerate(guide['first_steps'],1))
        parts.append('**Repères CPGE**')
        parts.extend('**'+label+' :** '+guide['levels'][key] for key,label in [('sup','Sup'),('spe','Spé'),('beyond','Au-delà')])
        parts.append('**À retenir :** '+guide['expected'])
    path.write_text('\n\n'.join(parts)+'\n', encoding='utf-8', newline='\n')
    return path


if __name__ == '__main__':
    from export_progression import export as export_progression
    export_progression()
    print(export())
    print(export_parcours())
