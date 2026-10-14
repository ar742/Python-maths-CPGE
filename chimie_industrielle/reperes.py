"""Buts, notations et acquis avant les manipulations."""
from contenu_thermo import GUIDES as THERMO
from contenu_cinetique import GUIDES as CINETIQUE
from contenu_redox import GUIDES as REDOX
from cours import LESSONS
LAB_GUIDES={**THERMO,**CINETIQUE,**REDOX}
for id_,guide in LAB_GUIDES.items():
    guide['lesson_numbers']=[i+1 for i,lesson in enumerate(LESSONS) if lesson['lab']==id_]
