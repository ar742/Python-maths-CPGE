"""Exporter la version autonome du cours : python export_cours.py."""
from pathlib import Path
import html
import re
from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES


def prose(value):
    value = re.sub(r'<br\s*/?>', '\n', value)
    value = re.sub(r'<(?:p|div)[^>]*>', '', value)
    value = re.sub(r'</(?:p|div)>', '\n\n', value)
    value = value.replace('<b>', '**').replace('</b>', '**')
    return html.unescape(re.sub(r'<[^>]*>', '', value)).strip()


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name('COURS.md')
    parts = ['# Physique statistique — cours et exercices\n',
             'Volet 06 de Python-maths-CPGE. Huit laboratoires pour relier les états microscopiques, les probabilités et les équilibres thermiques.\n',
             'Les résultats théoriques et les observations numériques sont distingués. Les approfondissements sont signalés.\n']
    for lesson in LESSONS:
        parts.extend(['## '+lesson['title']+'\n', '*'+lesson['level']+'*\n', prose(lesson['html'])+'\n'])
    parts.append('## Préparer les laboratoires\n')
    for lab, guide in LAB_GUIDES.items():
        parts.extend(['### '+lab+'\n', guide['purpose']+'\n', '**Objets et unités.**\n'])
        parts.extend('- '+item for item in guide['objects'])
        parts.append('\n**Hypothèses.**\n')
        parts.extend('- '+item for item in guide['assumptions'])
        parts.append('\n**Techniques.** '+ '; '.join(guide['techniques'])+'\n')
        parts.append('**Première expérience.**\n')
        parts.extend(str(i)+'. '+item for i,item in enumerate(guide['first_steps'],1))
        parts.extend(['\n**Sup.** '+guide['levels']['sup'], '**Spé et filières.** '+guide['levels']['spe'], '**Prolongements.** '+guide['levels']['beyond'], '**Résultat attendu.** '+guide['expected']+'\n'])
    parts.append('## Exercices corrigés\n')
    for exercise in EXERCISES:
        parts.extend(['### '+exercise['title']+'\n', exercise['question']+'\n', '**Correction.** '+exercise['answer']+'\n'])
    parts.append('## Sources et conventions\n')
    parts.extend(source+'\n' for source in SOURCES)
    path.write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    if path.resolve().parent == Path(__file__).resolve().parent:
        parcours = Path(__file__).with_name('PARCOURS.md')
        original = parcours.read_text(encoding='utf-8')
        marker = '<!-- reperes-laboratoires -->'
        original = original.split(marker, 1)[0].rstrip()
        overview = [marker, '## Préparer chaque expérience', '', 'Les repères Sup et Spé indiquent les techniques utilisées. Les indications MP/PC et les prolongements précisent la place de chaque sujet.', '']
        for lab, guide in LAB_GUIDES.items():
            overview.extend(['### '+lab, '', guide['purpose'], '', '**Spé et filières.** '+guide['levels']['spe'], '', '**Prolongements.** '+guide['levels']['beyond'], ''])
        parcours.write_text(original+'\n\n'+'\n'.join(overview), encoding='utf-8', newline='\n')
    return path


if __name__ == '__main__':
    from export_progression import export as export_progression
    export_progression()
    print(export())
