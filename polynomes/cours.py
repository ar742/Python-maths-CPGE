"""Cours, corrigés et sources des expériences polynomiales."""
from contenu_classiques import LESSONS as L0, EXERCISES as E0
from contenu_arithmetique import LESSONS as L1, EXERCISES as E1
from contenu_complexes import LESSONS as L2, EXERCISES as E2
from contenu_multivaries import LESSONS as L3, EXERCISES as E3
LESSONS=L0+L1+L2+L3
EXERCISES=E0+E1+E2+E3
SOURCES=[
    'Recueil de A. R., extrait Polynômes : fiche M17, pages imprimées 165–172 ; page 31, exercice 5 (complexes et racines de l’unité) ; page 39, exercice 8 (inversion de Möbius et polynômes irréductibles sur un corps fini). Le PDF personnel n’est pas redistribué.',
    "<a href='https://prepas.org/ups.php?document=69'>Programme de mathématiques sup</a> et <a href='https://prepas.org/ups.php?document=85'>programme de mathématiques spé</a> : polynômes, fractions rationnelles, arithmétique, algèbre linéaire, espaces préhilbertiens et calcul différentiel. Les repères sup / spé indiquent les techniques à mobiliser ; les prolongements sont accompagnés.",
    'Les identités de polynômes, divisions et certificats algébriques sont calculés exactement avec SymPy. Les coordonnées des racines, les interpolations, quadratures et grilles de tracé sont numériques. Une figure suggère un résultat ; une identité ou une démonstration le justifie.',
    'Pour un polynôme complexe, X est l’indéterminée et z une valeur complexe. Les coordonnées sont Re(z), Im(z). Pour plusieurs variables, le degré total diffère des degrés en chaque indéterminée. Chaque TP précise ses symboles, son corps de coefficients et ses hypothèses.',
    'Les corps finis, le théorème de Rouché, Gauss–Lucas, les bases de Gröbner, les intersections projectives et l’exemple de Motzkin sont présentés comme des prolongements. Leur cours est fourni avant les manipulations.',
    "<a href='https://github.com/ar742/Python-maths-CPGE/blob/main/polynomes/errata.md'>Errata des formules</a> : corrections limitées aux erreurs de formules vérifiées dans le contexte du recueil."
]
