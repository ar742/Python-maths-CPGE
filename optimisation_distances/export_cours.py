
"""Exporter le cours complet et les guides : python export_cours.py."""
from pathlib import Path
import html
import re
from cours import LESSONS, EXERCISES, SOURCES


def prose(value):
    value = re.sub(r'<br\s*/?>', '\n', value)
    value = re.sub(r'<(?:p|div)[^>]*>', '', value)
    value = re.sub(r'</(?:p|div)>', '\n\n', value)
    value = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m:'\n\n'+'#'*min(6,int(m[1])+2)+' '+m[2]+'\n\n', value, flags=re.S)
    value = re.sub(r'<li[^>]*>', '\n- ', value)
    value = re.sub(r'<sup[^>]*>(.*?)</sup>', r'^(\1)', value)
    value = re.sub(r'<sub[^>]*>(.*?)</sub>', r'_(\1)', value)
    for tag in ('b','strong'):
        value = value.replace('<'+tag+'>', '**').replace('</'+tag+'>', '**')
    value = value.replace('<code>',chr(96)).replace('</code>',chr(96))
    return html.unescape(re.sub(r'<[^>]*>', '', value)).strip()


def export(path=None):
    path = Path(path) if path else Path(__file__).with_name('COURS.md')
    parts = ['# Optimisation & Distances — cours et exercices\n',
             'Les démonstrations et corrections sont conservées. Les notations précèdent les formules ; '
             'les guides détaillés sont dans [PARCOURS.md](PARCOURS.md).\n']
    for lesson in LESSONS:
        parts.extend(['## '+lesson.get('title',lesson.get('titre'))+'\n',
                      '*'+lesson.get('level',lesson.get('niveau'))+'*\n'])
        if 'notations' in lesson:
            parts.extend([lesson['notations']+'\n', '**'+lesson['formula']+'**\n'])
        content=lesson.get('html',lesson.get('texte'))
        parts.append(content+'\n')
    parts.append('## Exercices corrigés\n')
    for i, exercise in enumerate(EXERCISES,1):
        if isinstance(exercise,dict):
            title,question,answer=exercise['title'],exercise['question'],exercise['answer']
        else:
            title,question,answer,_=exercise
        parts.extend(['### '+title+'\n', question+'\n', '**Correction.** '+answer+'\n'])
    parts.append('## Sources et conventions\n')
    for source in SOURCES:
        if isinstance(source,str): parts.append(source+'\n')
        else:
            title=source.get('title',source.get('titre'))
            if source.get('url'): title='['+title+']('+source['url']+')'
            parts.append('**'+title+'** — '+source.get('description',source.get('texte'))+'\n')
    path.write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    return path



from reperes import LAB_GUIDES

LAB_TITLES = {'approximation': 'Approcher cosinus', 'matrices': 'Projeter une matrice', 'produit': 'Ellipsoïde et boîte maximale', 'point': 'Distance d’un point', 'paire': 'Distance entre deux ellipsoïdes'}


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
    print(export())
    print(export_parcours())
