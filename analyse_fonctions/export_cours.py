"""Documents consultables sans lancer le serveur : cours et corrigés."""
from pathlib import Path
import html
import re
from cours import LESSONS,EXERCISES
from catalogue import LABS
from reperes import LAB_GUIDES
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
    text='# Fonctions & Équations — 56 leçons\n\nRecueil de A. R., Fonctions et fiches M5–M6. Chaque cours est relié à un laboratoire ; les approximations et les prolongements sont explicités.\n\n'
    for i,l in enumerate(LESSONS,1):text+=f'## {i:02d}. {l["title"]}\n\n{l["level"]} · Laboratoire `{l["lab"]}`\n\n'+markdown(l['html'])+'\n\n'
    (root/'COURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Fonctions & Équations — 84 exercices corrigés\n\n'
    for i,e in enumerate(EXERCISES,1):text+=f'## {i:02d}. {e["title"]}\n\n{e["level"]} · Laboratoire `{e["lab"]}`\n\n'+markdown(e['question'])+'\n\n**Correction guidée**\n\n'+markdown(e['answer'])+'\n\n'
    (root/'EXERCICES.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Quatorze séances d’analyse\n\nPour chaque TP : prévoir le résultat, effectuer les trois manipulations du guide puis justifier par le théorème adapté.\n\n'
    for j in range(0,len(LABS),2):
        text+=f'## Séance {j//2+1:02d} — {LABS[j]["category"]}\n\n'
        for l in LABS[j:j+2]:
            g=LAB_GUIDES[l['id']];text+='### '+l['title']+'\n\n'+g['purpose']+'\n\n'
            text+='\n'.join(f'{k+1}. {a}' for k,a in enumerate(g['first_steps']))+'\n\n**À justifier :** '+g['expected']+'\n\n'
    (root/'PARCOURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
if __name__=='__main__':export();print('Cours, exercices et parcours exportés.')
