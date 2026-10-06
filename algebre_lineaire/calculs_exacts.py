"""Outils rationnels et sorties JSON partagés par les laboratoires.

Le texte personnel n'est jamais confié à sympify, eval ou à un parseur de
polynômes. Fraction traite seulement des littéraux préalablement validés.
"""
from __future__ import annotations
from fractions import Fraction
import json
import math
import re
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

X = sp.Symbol("X")
_LITERAL = re.compile(r"[+-]?(?:\d{1,7}(?:/\d{1,7}|\.\d{1,6})?|\.\d{1,6})\Z")


def parse_scalar(value):
    if isinstance(value,bool) or not isinstance(value,(str,int,float)):
        raise ValueError("Une entrée doit être un entier, une fraction ou un décimal.")
    if isinstance(value,float):
        if not math.isfinite(value):raise ValueError("Les valeurs doivent être finies.")
        # Fraction(str(float)) est sûre ; aucun nom, opération ou fonction.
        fraction=Fraction(str(value))
    else:
        token=str(value).strip()
        if len(token)>32 or not _LITERAL.fullmatch(token):
            raise ValueError("Littéral attendu : entier, −a/b ou décimal (six décimales au plus).")
        try:fraction=Fraction(token)
        except (ValueError,ZeroDivisionError) as exc:raise ValueError("Fraction invalide ou dénominateur nul.") from exc
    if abs(fraction.numerator)>1000000 or fraction.denominator>1000000 or abs(fraction)>10000:
        raise ValueError("Entrée trop grande : |valeur|≤10000 et numérateur/dénominateur≤10⁶.")
    return sp.Rational(fraction.numerator,fraction.denominator)


def parse_matrix(value,max_size=4,square=False):
    """Texte `1 2;3 4`, lignes avec virgules, ou tableau JSON rectangulaire."""
    if isinstance(max_size,bool) or not isinstance(max_size,int) or not 1<=max_size<=6:
        raise ValueError("Limite de taille invalide.")
    if isinstance(value,str):
        if len(value)>4096:raise ValueError("Texte de matrice trop long.")
        text=value.strip()
        if text.startswith("["):
            try:value=json.loads(text)
            except (ValueError,RecursionError) as exc:raise ValueError("Tableau JSON invalide.") from exc
        else:
            value=[re.split(r"[\s,]+",line.strip()) for line in re.split(r"[;\n\r]+",text) if line.strip()]
    if not isinstance(value,list) or not 1<=len(value)<=max_size:
        raise ValueError(f"La matrice doit avoir de 1 à {max_size} lignes.")
    if any(not isinstance(row,list) or not 1<=len(row)<=max_size for row in value):
        raise ValueError(f"Chaque ligne doit avoir de 1 à {max_size} coefficients.")
    cols=len(value[0])
    if any(len(row)!=cols for row in value):raise ValueError("Toutes les lignes doivent avoir la même longueur.")
    if square and len(value)!=cols:raise ValueError("Une matrice carrée est requise.")
    return sp.Matrix([[parse_scalar(entry) for entry in row] for row in value])


def parse_vector(value,n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=6:raise ValueError("Dimension de vecteur invalide.")
    if isinstance(value,str):
        if len(value)>1024:raise ValueError("Vecteur trop long.")
        text=value.strip()
        if text.startswith("["):
            try:value=json.loads(text)
            except (ValueError,RecursionError) as exc:raise ValueError("Vecteur JSON invalide.") from exc
        else:value=re.split(r"[\s,;]+",text)
    if isinstance(value,list) and all(isinstance(v,list) and len(v)==1 for v in value):value=[v[0] for v in value]
    if not isinstance(value,list) or len(value)!=n:raise ValueError(f"Le second membre doit contenir {n} valeurs.")
    return sp.Matrix([parse_scalar(v) for v in value])


def serialize_matrix(matrix):
    matrix=sp.Matrix(matrix)
    return [[str(matrix[i,j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def number(data,key,default,lo,hi,integer=False):
    value=data.get(key,default)
    if isinstance(value,bool) or not isinstance(value,(int,float)) or isinstance(value,float) and not math.isfinite(value):raise ValueError(f"{key} doit être un nombre fini.")
    if not lo<=value<=hi or integer and int(value)!=value:raise ValueError(f"{key} doit être entre {lo} et {hi}"+(" et entier." if integer else "."))
    return int(value) if integer else float(value)


def rational(data,key,default,lo,hi,integer=False):
    value=number(data,key,default,lo,hi,integer)
    return sp.Rational(str(round(value,6)))


def choice(data,key,default,values):
    value=data.get(key,default)
    if not isinstance(value,str) or value not in values:raise ValueError(f"{key} doit être parmi : {', '.join(values)}.")
    return value


def metric(label,value,note=""):
    return dict(label=label,value=value if isinstance(value,str) else float(value),note=note)


def series(label,x,y,color="green",kind="line"):
    return dict(label=label,x=np.asarray(x,dtype=float).tolist(),y=np.asarray(y,dtype=float).tolist(),color=color,kind=kind)


def chart(title,xlabel,ylabel,data,logx=False,logy=False,equal=False,grid=None):
    result=dict(title=title,xlabel=xlabel,ylabel=ylabel,series=data,logx=logx,logy=logy,equal=equal)
    if grid is not None:result["grid"]={k:np.asarray(v,dtype=float).tolist() for k,v in grid.items()}
    return result


def table(headers,rows):return dict(headers=headers,rows=rows)


def matrix_block(label,matrix,note=""):
    return dict(label=label,entries=serialize_matrix(matrix),note=note)


def step(title,matrix,text=""):
    return dict(title=title,matrix=serialize_matrix(matrix),text=text)


def polynomial_evaluate(matrix,polynomial):
    """Horner exact ; le polynôme est construit en interne, jamais un texte."""
    A=sp.Matrix(matrix)
    if A.rows!=A.cols:raise ValueError("Une matrice carrée est requise.")
    if isinstance(polynomial,str):raise ValueError("Un objet polynôme est requis, pas du texte.")
    if not isinstance(polynomial,sp.Poly):
        if not isinstance(polynomial,sp.Expr):raise ValueError("Expression SymPy requise.")
        variables=polynomial.free_symbols
        if len(variables)>1:raise ValueError("Un seul indéterminé est autorisé.")
        polynomial=sp.Poly(polynomial,next(iter(variables),X),domain=sp.QQ)
    if len(polynomial.gens)!=1:raise ValueError("Polynôme univarié requis.")
    out=sp.zeros(A.rows);identity=sp.eye(A.rows)
    for coefficient in polynomial.all_coeffs():out=out*A+coefficient*identity
    return out


def invariant_factors(matrix):
    """Facteurs invariants moniques de XI−A sur QQ[X], unités retirées."""
    A=sp.Matrix(matrix)
    if A.rows!=A.cols or A.rows>6 or any(not v.is_Rational for v in A):raise ValueError("Matrice rationnelle carrée de taille ≤6 requise.")
    smith=smith_normal_form(X*sp.eye(A.rows)-A,domain=sp.QQ.poly_ring(X))
    return [sp.Poly(smith[i,i],X,domain=sp.QQ).monic() for i in range(A.rows) if sp.Poly(smith[i,i],X).degree()>0]


def rref_steps(matrix):
    """Élimination de Gauss–Jordan exacte : R=EA, avec toutes les étapes."""
    A=sp.Matrix(matrix);R=A.copy();E=sp.eye(A.rows);row=0;pivots=[];steps=[]
    for column in range(A.cols):
        pivot=next((i for i in range(row,A.rows) if R[i,column]!=0),None)
        if pivot is None:continue
        if pivot!=row:
            R.row_swap(row,pivot);E.row_swap(row,pivot)
            steps.append(step(f"Échanger L{row+1} et L{pivot+1}",R,"Opération inversible sur les équations ; permutation de lignes."))
        value=R[row,column]
        if value!=1:
            R.row_op(row,lambda v,j:v/value);E.row_op(row,lambda v,j:v/value)
            steps.append(step(f"L{row+1} ← L{row+1} / ({value})",R,"La division est faite dans Q ; un pivot non nul y est inversible."))
        for i in range(A.rows):
            if i==row or R[i,column]==0:continue
            coefficient=R[i,column]
            R.row_op(i,lambda v,j:v-coefficient*R[row,j]);E.row_op(i,lambda v,j:v-coefficient*E[row,j])
            steps.append(step(f"L{i+1} ← L{i+1} − ({coefficient}) L{row+1}",R,"Ajouter un multiple d'une autre ligne préserve la compatibilité du système."))
        pivots.append(column);row+=1
        if row==A.rows:break
    return R,tuple(pivots),E,steps


def numeric_exp(matrix):
    """Exponentielle NumPy par Taylor, réduction d'échelle puis carrés.

    Utilisée seulement pour des figures de familles bornées ; les identités
    algébriques affichées sont vérifiées séparément en calcul exact.
    """
    A=np.array(sp.Matrix(matrix),dtype=float)
    norm=float(np.linalg.norm(A,ord=np.inf))
    scale=max(0,math.ceil(math.log2(norm/.5))) if norm>.5 else 0
    B=A/2**scale;result=np.eye(len(A));term=result.copy()
    for k in range(1,45):
        term=term@B/k;result+=term
        if np.linalg.norm(term,ord=np.inf)<2e-16:break
    for _ in range(scale):result=result@result
    return result
