"""Le même contenu dans l’atelier et dans trois documents autonomes."""
from pathlib import Path
import html
import re
from cours import LESSONS,EXERCISES
from catalogue import LAB_BY_ID
from reperes import LAB_GUIDES

SESSIONS=[
('Sup · mesurer une vitesse',['horloge_iode','arrhenius_catalyse']),
('Sup → spé · établir un bilan thermique',['hess_combustion','temperature_adiabatique']),
('Sup · relier potentiel et composition',['nernst_pile','dosage_potentiometrique']),
('Spé · choisir une durée et un réacteur',['selectivite_successive','reacteurs_residence']),
('Spé · conversion, pression et recyclage',['haber_bosch','methanol_co2']),
('Spé · métaux, ciment et états physiques',['ellingham_zinc','calcination_ciment']),
('Spé · convertir l’énergie électrique et chimique',['electrolyse_h2','pile_combustible']),
('Spé · stocker et déposer la matière',['batterie_intercalation','electrodepot']),
('Spé · protéger et sélectionner les métaux',['corrosion_protection','cuivre_complexation']),
('Compléments · sites catalytiques et transport',['catalyse_surface','diffusion_grain']),
('Spé et complément thermique · mécanisme et stabilité',['ethanal_aeqs','emballement_thermique']),
('Spé · séparer et solidifier un mélange',['distillation_ideale','alliage_solidification'])]

def markdown(text):
    for tag in ('p','div','h3','h4','ul','ol','details','summary'):text=re.sub(r'</?'+tag+r'\b[^>]*>','\n\n',text)
    text=text.replace('<li>','\n- ').replace('</li>','').replace('<br>','\n')
    text=re.sub(r'<sup>(.*?)</sup>',r'^(\1)',text);text=re.sub(r'<sub>(.*?)</sub>',r'_(\1)',text)
    text=re.sub(r'</?(?:b|strong)>','**',text);text=re.sub(r'</?(?:i|em)>','*',text)
    return re.sub(r'\n{3,}','\n\n',html.unescape(re.sub(r'</?[A-Za-z][^>]*>','',text))).strip()

def export():
    root=Path(__file__).parent
    text='# Chimie pour l’industrie — 48 leçons\n\nRecueil de A. R., fiches C6–C8, pages 545–570. Les applications relient thermochimie, cinétique et électrochimie. Les paramètres didactiques et les limites sont annoncés dans chaque TP.\n\n'
    for i,l in enumerate(LESSONS,1):text+=f'## {i:02d}. {l["title"]}\n\n{l["level"]} · Laboratoire `{l["lab"]}`\n\n'+markdown(l['html'])+'\n\n'
    (root/'COURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Chimie pour l’industrie — 72 exercices corrigés\n\n'
    for i,e in enumerate(EXERCISES,1):text+=f'## {i:02d}. {e["title"]}\n\n{e["level"]} · Laboratoire `{e["lab"]}`\n\n'+markdown(e['question'])+'\n\n**Correction guidée**\n\n'+markdown(e['answer'])+'\n\n'
    (root/'EXERCICES.md').write_text(text.rstrip()+'\n',encoding='utf8')
    text='# Chimie pour l’industrie — douze séances guidées\n\nCommencer par les trois séances de sup. Les séances suivantes réinvestissent les outils de spé, selon la filière; les compléments de catalyse et de transport sont fournis. Pour chaque TP : lire les objets, prévoir un résultat, essayer les trois gestes et justifier un bilan.\n\n'
    for j,(title,ids) in enumerate(SESSIONS,1):
        text+=f'## Séance {j:02d} — {title}\n\n'
        for lab in ids:
            g=LAB_GUIDES[lab];text+='### '+LAB_BY_ID[lab]['title']+'\n\n'+g['purpose']+'\n\n'
            text+='**Objets et paramètres**\n\n'+'\n'.join('- '+item for item in g['objects'])+'\n\n'
            text+='**Repères** — '+' '.join(g['levels'][level] for level in ('sup','spe','beyond'))+'\n\n'
            text+='\n'.join(f'{k+1}. {a}' for k,a in enumerate(g['first_steps']))+'\n\n**À justifier :** '+g['expected']+'\n\n'
    (root/'PARCOURS.md').write_text(text.rstrip()+'\n',encoding='utf8')
    from export_progression import export as export_parcours
    export_parcours()

if __name__=='__main__':export();print('Cours, exercices et douze séances exportés.')
