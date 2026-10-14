"""Objectifs, notations et chemins de lecture de chaque TP."""
from contenu_classiques import GUIDES as G0
from contenu_arithmetique import GUIDES as G1
from contenu_complexes import GUIDES as G2
from contenu_multivaries import GUIDES as G3
from cours import LESSONS
LAB_GUIDES={**G0,**G1,**G2,**G3}
for key,guide in LAB_GUIDES.items():
    guide['lesson_numbers']=[i+1 for i,l in enumerate(LESSONS) if l['lab']==key]
