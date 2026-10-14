"""Documents consultables sans lancer le serveur : cours et corrigés."""
from pathlib import Path
import html
import re
from cours import LESSONS,EXERCISES
from catalogue import LABS
from reperes import LAB_GUIDES
from parcours_progressif import PROGRESSION


def heading_anchor(number, title):
    return re.sub(r'[^\w\s-]', '', f'{number:02d}. {title}'.lower()).replace(' ', '-')


def export_progression(root):
    labels = {'socle': 'Techniques incontournables',
              'approfondissement': 'Approfondissement accessible CPGE',
              'prolongement': 'Au-delà du programme'}
    text = '# Parcours progressif sup / spé — Polynômes & Géométrie\n\n'
    text += PROGRESSION['intro'] + '\n\n'
    text += '**5 séances de sup · 3 séances de spé · 2 approfondissements · 4 pistes au-delà.**\n\n'
    text += PROGRESSION['duration'] + '\n\n' + PROGRESSION['scope'] + '\n\n'
    text += '[Ouvrir le parcours dans l’atelier local](http://127.0.0.1:8784/#parcours) · [Guide de lancement](LISEZ_MOI.md) · [18 séances pour les 36 TP](PARCOURS.md)\n\n'
    text += '## Trois catégories\n\n'
    text += '- **Techniques incontournables :** priorité aux outils du programme. Les limites indiquent les parties facultatives du TP.\n'
    text += '- **Approfondissement accessible CPGE :** exercice guidé utilisant ces outils ; les définitions et formules nouvelles sont fournies.\n'
    text += '- **Au-delà du programme :** théorèmes ou méthodes nouveaux, à choisir après le socle.\n\n'
    text += '## Avant de commencer\n\n' + '\n'.join('- ' + item for item in PROGRESSION['prerequisites']) + '\n\n'
    text += '## Pour chaque séance\n\n' + '\n'.join(f'{i}. {item}' for i, item in enumerate(PROGRESSION['method'], 1)) + '\n\n'
    labs = {lab['id']: lab for lab in LABS}
    for stage in PROGRESSION['stages']:
        text += '## ' + stage['title'] + '\n\n' + stage['intro'] + '\n\n'
        for session in stage['sessions']:
            text += '### ' + session['title'] + '\n\n'
            text += '**' + labels[session['status']] + '** · ' + session['level'] + '\n\n'
            text += session['objective'] + '\n\n'
            for label, key in [('À faire', 'task'), ('Acquis attendu', 'success'), ('Limites et compléments', 'limits')]:
                text += '**' + label + ' :** ' + session[key] + '\n\n'
            text += '**TP et cours associés**\n\n'
            for lab_id in session['labs']:
                links = [f'[{number:02d}. {lesson["title"]}](COURS.md#{heading_anchor(number, lesson["title"])})'
                         for number, lesson in enumerate(LESSONS, 1) if lesson['lab'] == lab_id]
                text += '- **' + labs[lab_id]['title'] + '** — ' + ' · '.join(links) + '\n'
            text += '\n'
    text += '## Repères de programme\n\n'
    text += '\n'.join(f'- [{source["label"]}]({source["url"]})' for source in PROGRESSION['sources']) + '\n'
    (root / 'PARCOURS_PROGRESSIF.md').write_text(text, encoding='utf8')
def markdown(text):
    text=re.sub(r'<img[^>]*>','',text)
    text=re.sub(r'<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>',r'[\2](\1)',text,flags=re.S)
    for tag in ('p','div','h3','h4','ul','ol','details','summary'):text=re.sub(r'</?'+tag+r'\b[^>]*>','\n\n',text)
    text=text.replace('<li>','\n- ').replace('</li>','').replace('<br>','\n').replace('<br/>','\n')
    text=re.sub(r'<sup>(.*?)</sup>',r'^(\1)',text);text=re.sub(r'<sub>(.*?)</sub>',r'_(\1)',text)
    text=re.sub(r'</?(?:b|strong)>','**',text);text=re.sub(r'</?(?:i|em)>','*',text)
    return re.sub(r'\n{3,}','\n\n',html.unescape(re.sub(r'</?[A-Za-z][^>]*>','',text))).strip()
def export():
    root=Path(__file__).parent
    text='# Polynômes & Géométrie — 72 leçons\n\nRecueil de A. R., fiche M17, pages 165–172, et exercices des pages 31 et 39. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.\n\n'
    for i,l in enumerate(LESSONS,1):text+=f'## {i:02d}. {l["title"]}\n\n{l["level"]} · Laboratoire `{l["lab"]}`\n\n'+markdown(l['html'])+'\n\n'
    (root/'COURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Polynômes & Géométrie — 108 exercices corrigés\n\n'
    for i,e in enumerate(EXERCISES,1):text+=f'## {i:02d}. {e["title"]}\n\n{e["level"]} · Laboratoire `{e["lab"]}`\n\n'+markdown(e['question'])+'\n\n**Correction guidée**\n\n'+markdown(e['answer'])+'\n\n'
    (root/'EXERCICES.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Dix-huit séances de polynômes et géométrie\n\nPour les complexes et les polynômes à plusieurs variables, commencer par le [parcours progressif sup / spé](PARCOURS_PROGRESSIF.md) : huit séances prioritaires, puis des approfondissements et des prolongements facultatifs. Le présent document rassemble les guides des 36 TP.\n\nPour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par une identité exacte, un certificat ou une démonstration.\n\n'
    for j in range(0,len(LABS),2):
        text+=f'## Séance {j//2+1:02d} — {LABS[j]["category"]}\n\n'
        for l in LABS[j:j+2]:
            g=LAB_GUIDES[l['id']];text+='### '+l['title']+'\n\n'+g['purpose']+'\n\n'
            text+='**Objets et paramètres**\n\n'+'\n'.join('- '+item for item in g['objects'])+'\n\n'
            text+='**Repères** — Sup : '+g['levels']['sup']+' Spé : '+g['levels']['spe']+' Au-delà : '+g['levels']['beyond']+'\n\n'
            text+='\n'.join(f'{k+1}. {a}' for k,a in enumerate(g['first_steps']))+'\n\n**À justifier :** '+g['expected']+'\n\n'
    (root/'PARCOURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
    export_progression(root)
if __name__=='__main__':export();print('Cours, exercices et parcours exportés.')
