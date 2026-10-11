"""Objectifs, notations et parcours avant la première manipulation."""
from contenu_commande import GUIDES as P1
from contenu_circuits import GUIDES as P2
from contenu_analogique import GUIDES as P3
from cours import LESSONS
LAB_GUIDES={**P1,**P2,**P3}
for lab,g in LAB_GUIDES.items():
    g['lesson_numbers']=[i+1 for i,l in enumerate(LESSONS) if l['lab']==lab]
