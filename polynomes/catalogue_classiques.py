"""Fractions rationnelles, interpolation et bases orthogonales."""
from commun import lab,slider,select,preset
LABS=[
lab('rationnelle_recueil','Décomposer la fraction du recueil','Fractions & Interpolation',
    'Partir du quotient de degré quatre de l’exercice 4, page 170. Séparer partie entière, pôle simple et pôle triple. Modifier les coefficients des parties polaires : l’ordre effectif du pôle peut diminuer. Vérifier la recomposition exacte.',
    [slider('A','Coefficient A au pôle −1',-4,4,.5,2),slider('B','Coefficient B du terme 1/(X−2)',-3,3,.5,1),slider('C','Coefficient C du terme 1/(X−2)²',-3,3,.5,2),slider('D','Coefficient D du terme 1/(X−2)³',-5,5,.5,3),slider('shift','Translation s des deux pôles',-1,1,.25,0)],
    [preset('Retrouver la fraction page 170',A=2,B=1,C=2,D=3,shift=0),preset('Abaisser l’ordre du pôle en 2',D=0,C=2),preset('Conserver deux pôles simples',C=0,D=0)]),
lab('poles_multiples','Extraire une partie polaire par Taylor','Fractions & Interpolation',
    'Décomposer g(X)/(X−a)^m sans résoudre un grand système. Les dérivées de g au point a donnent les coefficients des puissances négatives. Distinguer l’ordre annoncé au dénominateur et l’ordre après simplification.',
    [slider('a','Point a',-1,1,.25,.5),slider('m','Puissance m du dénominateur',2,5,1,3,integer=True),slider('c','Coefficient c dans g(X)=X⁴+cX²+X+1',-3,3,.5,2)],
    [preset('Extraire trois coefficients',a=.5,m=3,c=2),preset('Faire disparaître le coefficient dominant',a=-1,m=4,c=-1),preset('Décomposer un pôle d’ordre cinq',a=0,m=5,c=2)]),
lab('reel_complexe','Regrouper des pôles complexes conjugués','Fractions & Interpolation',
    'Une même fraction admet une décomposition réelle ou complexe. Deux fractions à pôles conjugués se regroupent en un terme à dénominateur quadratique réel. Comparer les écritures et vérifier que leur valeur sur la droite réelle coïncide.',
    [slider('a','Partie réelle a des pôles complexes',-1,1,.25,0),slider('b','Partie imaginaire positive b',.25,2,.25,1),slider('u','Coefficient u du numérateur uX+v',-3,3,.5,2),slider('v','Coefficient v du numérateur',-3,3,.5,1),slider('w','Coefficient w au pôle réel 2',-2,2,.5,1)],
    [preset('Deux pôles imaginaires',a=0,b=1,u=2,v=1,w=1),preset('Éloigner les pôles de la droite réelle',b=2),preset('Supprimer le pôle réel',w=0)]),
lab('annulations','Reconnaître un trou et un pôle','Fractions & Interpolation',
    'Simplifier une fraction ne restaure pas les valeurs interdites de son expression initiale. Faire varier les multiplicités d’un facteur commun et rapprocher deux points interdits. Le calcul exact distingue prolongement possible et divergence.',
    [slider('a','Premier point interdit a',-1,1,.25,0),slider('b','Second point interdit b',-2,2,.25,1),slider('k','Multiplicité k au numérateur',1,3,1,2,integer=True),slider('m','Multiplicité m au dénominateur',1,4,1,2,integer=True)],
    [preset('Un trou et un pôle',a=0,b=1,k=2,m=2),preset('Conserver un pôle en a',k=1,m=3),preset('Confondre les deux points interdits',a=1,b=1,k=3,m=2)]),
lab('interpolation','Choisir les nœuds d’une interpolation','Fractions & Interpolation',
    'Interpoler la fonction de Runge par un polynôme. Augmenter le degré puis comparer des nœuds régulièrement espacés aux nœuds de Tchebychev. Une erreur faible aux nœuds ne garantit pas une bonne approximation entre eux.',
    [slider('n','Degré n du polynôme interpolateur',3,18,1,10,integer=True),select('nodes','Répartition des nœuds',[('equal','Équidistants'),('cheb','Tchebychev')],'equal'),slider('strength','Paramètre c de f(x)=1/(1+cx²)',1,40,1,25)],
    [preset('Voir les oscillations aux extrémités',n=14,nodes='equal',strength=25),preset('Conserver le degré, changer les nœuds',n=14,nodes='cheb',strength=25),preset('Commencer avec un degré modéré',n=5,nodes='equal')]),
lab('orthogonaux','Relier une base orthogonale à une quadrature','Fractions & Interpolation',
    'Explorer Legendre, Tchebychev et Hermite probabilistes. Les racines du polynôme donnent des nœuds de quadrature ; les poids sont positifs. Vérifier les moments jusqu’au degré 2n−1 puis observer un premier défaut au-delà.',
    [select('family','Famille et poids d’intégration',[('legendre','Legendre : poids 1 sur [−1,1]'),('chebyshev','Tchebychev : poids 1/√(1−x²)'),('hermite','Hermite : poids exp(−x²/2) sur ℝ')],'legendre'),slider('n','Degré n, donc nombre de nœuds',2,12,1,6,integer=True),slider('power','Puissance k du moment à calculer',0,24,1,10,integer=True)],
    [preset('Vérifier le dernier degré garanti',family='legendre',n=6,power=11),preset('Franchir ce degré',family='legendre',n=6,power=12),preset('Retrouver les moments gaussiens',family='hermite',n=6,power=10)])
]
