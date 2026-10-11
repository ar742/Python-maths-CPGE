"""Cours, méthodes et exercices associés aux laboratoires P15–P19."""
from contenu_commande import LESSONS as L1, EXERCISES as E1
from contenu_circuits import LESSONS as L2, EXERCISES as E2
from contenu_analogique import LESSONS as L3, EXERCISES as E3
LESSONS=L1+L2+L3
EXERCISES=E1+E2+E3
SOURCES=[
"Recueil personnel de A. R., extrait Électricité : P15 (pages 386–397, exercices 2 et 4), P16 (398–403, exercices 1 à 4), P17 (404–414, priorité au TP Moteur X, à la rétroaction, à la fonction de z et aux exercices 4 et 5), P18 (415–422, ALI et exercice 6), P19 (423–433, analyse fréquentielle et exercices 3 et 4). Le PDF n’est pas redistribué.",
"<a href='https://www.lyceedecachan.fr/wp-content/uploads/2023/07/Programme-PC-PTSI.pdf'>Programme officiel de physique-chimie PTSI</a> ; <a href='https://prepas.org/ups.php?document=94'>programme officiel de physique-chimie PSI</a> ; <a href='https://prepas.org/ups.php?document=96'>programme officiel de physique-chimie PT</a>. Mesures, acquisition numérique, ALI réels et conversion de puissance complètent le recueil.",
"<a href='https://www.education.gouv.fr/bo/21/Special1/ESRS2035781A.htm'>Programme de sciences industrielles PTSI–PT (annexe 3)</a> ; <a href='https://www.education.gouv.fr/bo/21/Special1/ESRS2035780A.htm'>programme de sciences industrielles PCSI–PSI (annexe 4)</a>. Les fonctions de transfert, diagrammes de Bode, performances et correcteurs sont reliés aux compétences de SI. Les inversions générales de Laplace sont des prolongements mathématiques accompagnés.",
"Les valeurs temporelles sont instantanées ; une amplitude sinusoïdale et une valeur efficace sont distinguées. Le nombre j vérifie j²=−1 ; ω=2πf est la pulsation en rad/s. La variable p décrit le modèle continu, z le modèle discret ; leurs conventions et les conditions initiales sont précisées dans les leçons concernées.",
"Chaque TP définit ses grandeurs, ses unités, ses hypothèses et trois premières manipulations. Les repères sup / spé / au-delà distinguent physique, sciences industrielles et ouvertures. Le schéma de principe aide à lire le modèle ; les courbes et les tableaux proviennent des calculs Python."
]
