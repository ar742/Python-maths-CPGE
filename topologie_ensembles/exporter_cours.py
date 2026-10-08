"""Régénérer les cours et exercices Markdown depuis les contenus de l'application."""
from html.parser import HTMLParser
from pathlib import Path
import re
from cours import LESSONS, EXERCISES, SOURCES

class Markdown(HTMLParser):
    def __init__(self):
        super().__init__();self.output=[];self.links=[];self.formula=False
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='div' and attrs.get('class')=='formula':self.output.append('\n\n```text\n');self.formula=True
        elif tag in ('p','h3','h4','ul','ol'):self.output.append('\n\n'+('### ' if tag=='h3' else '#### ' if tag=='h4' else ''))
        elif tag=='li':self.output.append('\n- ')
        elif tag in ('b','strong'):self.output.append('**')
        elif tag=='br':self.output.append('\n')
        elif tag=='a':self.output.append('[');self.links.append(attrs.get('href',''))
        elif tag=='code':self.output.append('`')
    def handle_endtag(self,tag):
        if tag=='div' and self.formula:self.output.append('\n```\n');self.formula=False
        elif tag in ('p','li','h3','h4','ul','ol'):self.output.append('\n')
        elif tag in ('b','strong'):self.output.append('**')
        elif tag=='a':self.output.append(']('+self.links.pop()+')')
        elif tag=='code':self.output.append('`')
    def handle_data(self,data):self.output.append(data)

def markdown(html):
    parser=Markdown();parser.feed(html)
    return re.sub(r'\n{3,}','\n\n',''.join(parser.output)).strip()

def export(destination):
    destination=Path(destination)
    text='# Topologie & Ensembles · Cours et démonstrations\n\n60 leçons originales, avec variables, hypothèses, preuves et applications. [Laboratoires et lancement](README.md).\n\n'
    text+='\n\n'.join(f"## {l['title']}\n\n**{l['level']} · TP : {l['lab']}**\n\n{markdown(l['html'])}" for l in LESSONS)
    text+='\n\n## Sources\n\n'+'\n\n'.join(markdown(s) for s in SOURCES)+'\n'
    (destination/'COURS.md').write_text(text,encoding='utf8')
    text='# Topologie & Ensembles · Exercices corrigés\n\n60 exercices originaux. Chercher la solution avant de lire la correction et réinvestir le laboratoire associé.\n\n'
    text+='\n\n'.join(f"## {e['title']}\n\n**{e['level']} · TP : {e['lab']}**\n\n{markdown(e['question'])}\n\n### Correction guidée\n\n{markdown(e['answer'])}" for e in EXERCISES)+'\n'
    (destination/'EXERCICES.md').write_text(text,encoding='utf8')
    return len(LESSONS),len(EXERCISES)

if __name__=='__main__':print(export(Path(__file__).resolve().parent))
