"""Exporter le parcours autonome à partir des mêmes données que la page locale."""
from pathlib import Path
from parcours_progressif import PROGRESSION, LAB_LINKS

def export():
    labels={'socle':'Techniques incontournables','approfondissement':'Approfondissement CPGE','prolongement':'Au-delà du programme'}
    p=PROGRESSION
    text='# '+p['title']+'\n\n'+p['intro']+'\n\n'+p['duration']+'\n\n'+p['scope']+'\n\n'
    text+='[Guide de lancement](LISEZ_MOI.md) · [Retour à l’atelier](README.md)\n\n'
    text+='## Avant de commencer\n\n'+'\n'.join('- '+s for s in p['prerequisites'])+'\n\n'
    text+='## Pour chaque séance\n\n'+'\n'.join(f'{i}. {s}' for i,s in enumerate(p['method'],1))+'\n\n'
    links={l['id']:l for l in LAB_LINKS}
    for stage in p['stages']:
        text+='## '+stage['title']+'\n\n'+stage['intro']+'\n\n'
        for s in stage['sessions']:
            text+='### '+s['title']+'\n\n**'+labels[s['status']]+'** · '+s['level']+'\n\n'+s['objective']+'\n\n'
            for title,key in [('À faire','task'),('Acquis attendu','success'),('Limites et compléments','limits')]:text+='**'+title+' :** '+s[key]+'\n\n'
            text+='**TP associés :** '+' ; '.join(links[i]['title'] for i in s['labs'])+'\n\n'
    text+='## Repères de programme\n\n'+'\n'.join(f'- [{s["label"]}]({s["url"]})' for s in p['sources'])+'\n'
    (Path(__file__).parent/'PARCOURS_PROGRESSIF.md').write_text(text,encoding='utf8')

if __name__=='__main__':export()
