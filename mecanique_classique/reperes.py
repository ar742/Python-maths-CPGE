"""Buts concrets, variables et trois premières manipulations de chaque TP."""
from contenu_p1 import GUIDES as P1
from contenu_p2 import GUIDES as P2
from contenu_p3 import GUIDES as P3
from cours import LESSONS
LAB_GUIDES={**P1,**P2,**P3}
for lab,g in LAB_GUIDES.items():
    g['lesson_numbers']=[i+1 for i,l in enumerate(LESSONS) if l['lab']==lab]
