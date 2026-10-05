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
    parts = ['# Physique statistique — cours et exercices\n',
             'Volet 06 de Python-maths-CPGE. Huit laboratoires pour relier les états microscopiques, les probabilités et les équilibres thermiques.\n',
             'Les résultats théoriques et les observations numériques sont distingués. Les approfondissements sont signalés.\n']
    for lesson in LESSONS:
        parts.extend(['## '+lesson['title']+'\n', '*'+lesson['level']+'*\n', prose(lesson['html'])+'\n'])
    parts.append('## Exercices corrigés\n')
    for exercise in EXERCISES:
        parts.extend(['### '+exercise['title']+'\n', exercise['question']+'\n', '**Correction.** '+exercise['answer']+'\n'])
    parts.append('## Sources et conventions\n')
    parts.extend(source+'\n' for source in SOURCES)
    path.write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    return path


if __name__ == '__main__':
    print(export())
