"""Exporter le cours structuré, ses missions et les corrections : python export_cours.py."""
from pathlib import Path
import html
import re
from cours import LESSONS, EXERCISES, SOURCES


def prose(value):
    value = re.sub(r'<br\s*/?>', '\n', value)
    value = re.sub(r'<(?:p|div)[^>]*>', '', value)
    value = re.sub(r'</(?:p|div)>', '\n\n', value)
    value = re.sub(r'<h3[^>]*>', '\n### ', value)
    value = value.replace('</h3>', '\n\n')
    value = value.replace('<b>', '**').replace('</b>', '**')
    return html.unescape(re.sub(r'<[^>]*>', '', value)).strip()


def objects_block(items):
    if not items:
        return ''
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    rows = ['**Objets et variables**\n', '| Symbole | Signification |', '|---|---|']
    rows.extend('| '+cell(item['symbol'])+' | '+cell(item['meaning'])+' |' for item in items)
    return '\n'.join(rows)+'\n'


def list_block(title, items):
    if not items:
        return ''
    return '**'+title+'**\n\n'+'\n'.join('- '+str(item) for item in items)+'\n'


def worked_block(example):
    if not example:
        return ''
    parts = ['### Exemple guidé · '+example['title'], '', example['setup'], '']
    parts.extend(str(i)+'. '+step for i, step in enumerate(example['steps'], 1))
    parts.extend(['', '**Résultat à expliquer.** '+example['conclusion'], ''])
    return '\n'.join(parts)


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name('COURS.md')
    parts = ['# Algèbre & Réductions — cours et exercices\n',
             'Maths, volet 05 · Atelier 07 de Python-maths-CPGE. Dix-sept laboratoires : structures, réduction, représentations, oscillateurs, probabilités et réseaux.\n',
             'Vingt-cinq leçons et quarante exercices corrigés. Les objets, variables, hypothèses et contrôles sont déclarés ; les approfondissements se choisissent selon la filière. Le parcours propose dix missions.\n']
    for lesson in LESSONS:
        parts.extend(['## '+lesson['title']+'\n', '*'+lesson['level']+'*\n',
                      'Laboratoire : '+lesson['lab']+'\n',
                      objects_block(lesson.get('objects')),
                      list_block('Objectifs de la mission', lesson.get('objectives')),
                      prose(lesson['html'])+'\n',
                      worked_block(lesson.get('worked_example')),
                      list_block('Questions avant le corrigé', lesson.get('questions'))])
    parts.append('## Exercices corrigés\n')
    for exercise in EXERCISES:
        parts.extend(['### '+exercise['title']+'\n', '*'+exercise['level']+'*\n',
                      objects_block(exercise.get('objects')),
                      prose(exercise['question'])+'\n',
                      '**Correction.** '+prose(exercise['answer'])+'\n'])
    parts.append('## Sources et conventions\n')
    parts.extend(source+'\n' for source in SOURCES)
    path.write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    return path


if __name__ == '__main__':
    print(export())
