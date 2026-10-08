"""Rassembler les ressources de base et les TP centrés sur les pages du recueil."""
from copy import deepcopy
from cours import LESSONS as BASE_LESSONS, EXERCISES as BASE_EXERCISES, SOURCES as BASE_SOURCES
from reperes import LAB_GUIDES as BASE_GUIDES
from cours_recueil import LESSONS as RECUEIL_LESSONS, EXERCISES as RECUEIL_EXERCISES, LAB_GUIDES as RECUEIL_GUIDES

SOURCES=list(BASE_SOURCES)+[
    "<p><a href='https://www.chem.ucalgary.ca/courses/353/exams/3513/353w03/353mt03me.html'>Université de Calgary — addition de HCl aux alcynes et dihalogénure geminal</a>.</p>",
    "<p><a href='https://openstax.org/books/organic-chemistry/pages/16-2-other-aromatic-substitutions'>OpenStax, Organic Chemistry — sulfonation et autres substitutions aromatiques</a>.</p>",
]

LESSONS=deepcopy(BASE_LESSONS)+deepcopy(RECUEIL_LESSONS)
EXERCISES=deepcopy(BASE_EXERCISES)+deepcopy(RECUEIL_EXERCISES)
for collection in (LESSONS,EXERCISES):
    for i,item in enumerate(collection,1):
        title=item['title']
        if title.split('.',1)[0].isdigit():title=title.split('.',1)[1].strip()
        item['title']=f'{i}. {title}'
LAB_GUIDES=deepcopy(BASE_GUIDES)
for lab,guide in RECUEIL_GUIDES.items():
    guide=deepcopy(guide)
    guide['lesson_numbers']=[len(BASE_LESSONS)+number for number in guide['lesson_numbers']]
    LAB_GUIDES[lab]=guide
