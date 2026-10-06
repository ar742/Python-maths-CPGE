"""Réductions exactes de matrices rationnelles, pour les ateliers de CPGE.

Les certificats portent sur QQ ; les graphiques du spectre sont seulement des
approximations pour l'affichage. Aucun texte utilisateur n'est évalué par SymPy.
"""
from itertools import product, chain
import math

import sympy as sp

try:
    from .calculs_exacts import (invariant_factors, parse_matrix, parse_vector,
                                polynomial_evaluate, serialize_matrix)
except ImportError:
    from calculs_exacts import (invariant_factors, parse_matrix, parse_vector,
                                polynomial_evaluate, serialize_matrix)

X = sp.Symbol("X")
REFERENCES = [
    {"title": "Patrick Brosnan, Rational Canonical and Jordan Forms",
     "url": "https://math.umd.edu/~pbrosnan/Teach/405-15-01/can.pdf"},
    {"title": "SymPy : formes normales sur un anneau principal",
     "url": "https://docs.sympy.org/latest/modules/matrices/normalforms.html"},
]


def _choice(d, name, default, allowed):
    value = d.get(name, default)
    if value not in allowed:
        raise ValueError(f"{name} : choisir parmi {', '.join(allowed)}.")
    return value


def _integer(d, name, default, low, high):
    value = d.get(name, default)
    if isinstance(value, bool):
        raise ValueError(f"{name} doit être un entier entre {low} et {high}.")
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(f"{name} doit être un entier entre {low} et {high}.") from None
    if not math.isfinite(number) or not number.is_integer() or not low <= number <= high:
        raise ValueError(f"{name} doit être un entier entre {low} et {high}.")
    return int(number)


def _poly(expression):
    if isinstance(expression, sp.Poly):
        expression = expression.as_expr().subs(expression.gen, X)
    return sp.Poly(expression, X, domain=sp.QQ)


def _text(expression, factor=True):
    if isinstance(expression, sp.Poly):
        expression = expression.as_expr()
    return str(sp.factor(expression) if factor else expression).replace("**", "^")


def _metric(label, value, note=""):
    return {"label": label, "value": value, "note": note}


def _series(label, x, y, color="green", kind="line"):
    return {"label": label, "x": list(x), "y": list(y), "color": color, "kind": kind}


def _chart(title, xlabel, ylabel, series, equal=False):
    return dict(title=title, xlabel=xlabel, ylabel=ylabel, series=series,
                logx=False, logy=False, equal=equal)


def _matrix(label, A, note=""):
    return {"label": label, "entries": serialize_matrix(A), "note": note}


def _step(title, A, text):
    return {"title": title, "matrix": serialize_matrix(A), "text": text}


def _zero(A):
    return all(sp.simplify(v) == 0 for v in A)


def jordan_block(n, eigenvalue=0):
    """Convention : 1 sur la surdiagonale, A=PJP⁻¹."""
    J = eigenvalue * sp.eye(n)
    for i in range(n-1):
        J[i, i+1] = 1
    return J


def companion(p):
    p = _poly(p).monic()
    n = p.degree()
    if n < 1:
        raise ValueError("Un compagnon exige un polynôme de degré au moins 1.")
    A = sp.zeros(n)
    for i in range(1, n):
        A[i, i-1] = 1
    for i in range(n):
        A[i, n-1] = -p.nth(i)
    return A


def _shear(n, value=1):
    P = sp.eye(n)
    for i in range(n-1):
        P[i, i+1] = value
    return P


def _tp_matrix():
    # Recueil p.137 : les colonnes sont u1=e1+2e2, u2=2e1+e2, u3=e1+e3.
    P = sp.Matrix([[1, 2, 1], [2, 1, 0], [0, 0, 1]])
    J = jordan_block(3, 1)
    return P*J*P.inv(), P, J


def _vandermonde_matrix():
    # Recueil p.145 : colonnes (1,a,a²,a³), a=1,2,3,5.
    A = sp.Matrix([[a**k for a in (1, 2, 3, 5)] for k in range(4)])
    return A, None, None


def _input(d, families, default):
    name = _choice(d, "famille", default, list(families))
    raw = d.get("matrix")
    if raw is not None and raw != "" and raw != []:
        return parse_matrix(raw, max_size=4, square=True), "personnalisée", None, None
    A, P, J = families[name]()
    return A, name, P, J


def _jordan_family(J):
    P = _shear(J.rows)
    return P*J*P.inv(), P, J


def dense_basis(n=6):
    """Réflexion de Householder rationnelle : P=Pᵀ=P⁻¹, sans décimales."""
    v = sp.Matrix(range(1, n+1))
    return sp.eye(n)-2*v*v.T/(v.T*v)[0]


def _dense_family(J):
    P = dense_basis(J.rows)
    return P*J*P.T, P, J


def _dense_multiple():
    return _dense_family(sp.diag(jordan_block(3, 1), jordan_block(2, -2), sp.Matrix([[3]])))


RECURRENCE6 = (X-1)**2*(X+1)*(X**2-X-1)*(X-2)


def _pedagogy(mission, objects, reading, proof, questions):
    return dict(mission=mission, objects=[dict(symbol=s, meaning=m) for s, m in objects],
                reading=reading, proof=proof, questions=questions)


def _jordan_scene(blocks, title="Les chaînes de Jordan"):
    chains = []
    for b in blocks:
        for i, length in enumerate(b["sizes"]):
            chains.append(dict(**{"lambda": _text(b["eigenvalue"])}, length=length,
                               label="λ="+_text(b["eigenvalue"])+" : chaîne "+str(i+1)))
    return dict(kind="jordan", title=title,
                description="Pour une chaîne u₁,…,uₛ : (A−λI)u₁=0 et (A−λI)uⱼ=uⱼ₋₁. Une flèche est une action linéaire, pas une transition probabiliste.",
                chains=chains)


def _companion_scene(factors, title="La mécanique des blocs compagnons"):
    nodes, edges, start = [], [], 0
    for block, p in enumerate(factors):
        size = p.degree()
        for j in range(size):
            idx = start+j
            nodes.append(dict(id=str(idx), label=("v"+str(block+1) if j == 0 else "A^"+str(j)+"v"+str(block+1)),
                              x=1.6*j, y=-1.8*block, group=block))
            if j:
                edges.append(dict(source=str(idx-1), target=str(idx), weight=1, label="A", color="green"))
            coefficient = -p.nth(j)
            if coefficient:
                edges.append(dict(source=str(start+size-1), target=str(idx), weight=float(coefficient),
                                  label=_text(coefficient), color="rose", feedback=True))
        start += size
    return dict(kind="graph", title=title,
                description="A avance dans chaque base de Krylov. La dernière image revient vers la chaîne selon les coefficients opposés du polynôme monique.",
                nodes=nodes, edges=edges, directed=True)


def _rotation_jordan():
    R = sp.Matrix([[0, -1], [1, 0]])
    A = R.row_join(sp.eye(2)).col_join(sp.zeros(2).row_join(R))
    return A, None, None


SPECTRE_FAMILIES = {
    "jordan42": lambda: _dense_family(sp.diag(jordan_block(4, 1), jordan_block(2, 1))),
    "jordan321": lambda: _dense_family(sp.diag(jordan_block(3, 1), jordan_block(2, 1), sp.Matrix([[1]]))),
    "symetrique6": lambda: _dense_family(sp.diag(-2, -1, 0, 1, 2, 2)),
    "symetrique": lambda: (sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]]), None, None),
    "jordan": lambda: _jordan_family(jordan_block(3, 1)),
    "rotation": lambda: (sp.diag(sp.Matrix([[0, -1], [1, 0]]), sp.Matrix([[2]])), None, None),
    "double": lambda: _jordan_family(sp.diag(1, 1, 2)),
}
DUNFORD_FAMILIES = {
    "dense6": _dense_multiple,
    "nilpotent42": lambda: _dense_family(sp.diag(jordan_block(4), jordan_block(2))),
    "tp": _tp_matrix,
    "deux_blocs": lambda: _jordan_family(sp.diag(jordan_block(3, 1), sp.Matrix([[2]]))),
    "nilpotent": lambda: _jordan_family(jordan_block(4)),
    "rotation_jordan": _rotation_jordan,
}
CYCLIQUE_FAMILIES = {
    "recurrence6": lambda: _dense_family(companion(RECURRENCE6)),
    "deux_chaines6": lambda: _dense_family(sp.diag(jordan_block(4, 1), jordan_block(2, 1))),
    "compagnon": lambda: (companion((X-1)*(X-2)*(X-3)), None, None),
    "diagonale": lambda: (sp.diag(1, 2, 3), sp.eye(3), sp.diag(1, 2, 3)),
    "scalaire": lambda: (2*sp.eye(3), sp.eye(3), 2*sp.eye(3)),
    "jordan": lambda: (jordan_block(3, 1), sp.eye(3), jordan_block(3, 1)),
}
CAYLEY_FAMILIES = {
    "dense6": _dense_multiple,
    "tp": _vandermonde_matrix,
    "jordan": lambda: _jordan_family(jordan_block(4, 2)),
    "rotation": lambda: (sp.Matrix([[0, -1], [1, 0]]), None, None),
    "singuliere": lambda: _jordan_family(sp.diag(jordan_block(2), sp.Matrix([[1]]))),
}


def exact_invariants(A):
    """Smith indépendant des familles : χ=∏fᵢ et μ=fᵣ."""
    factors = [_poly(p).monic() for p in invariant_factors(A)]
    characteristic = _poly(A.charpoly(X).as_expr())
    if not factors or _poly(sp.prod(p.as_expr() for p in factors)) != characteristic:
        raise ArithmeticError("Échec du certificat de Smith : produit différent de χ.")
    if any(factors[i+1].rem(factors[i]).as_expr() != 0 for i in range(len(factors)-1)):
        raise ArithmeticError("Échec de la chaîne de divisibilité.")
    minimal = factors[-1]
    if not _zero(polynomial_evaluate(A, minimal)):
        raise ArithmeticError("Le polynôme minimal proposé n'annule pas A.")
    return characteristic, minimal, factors


def _valuation(p, f):
    exponent = 0
    while p.degree() >= f.degree() and p.rem(f).is_zero:
        p = p.exquo(f)
        exponent += 1
    return exponent


def spectral_structure(A):
    characteristic, minimal, factors = exact_invariants(A)
    blocks = []
    for f, multiplicity in characteristic.factor_list()[1]:
        sizes = sorted((_valuation(p, f) for p in factors), reverse=True)
        sizes = [s for s in sizes if s]
        roots = f.all_roots(radicals=f.degree() <= 2)
        for root in roots:
            # Dans une extension de caractéristique zéro les facteurs sont séparables.
            blocks.append(dict(eigenvalue=root, factor=f, algebraic=int(multiplicity),
                               geometric=len(sizes), sizes=sizes,
                               kernels=[sum(min(k, s) for s in sizes) for k in range(A.rows+1)]))
    squarefree = minimal.gcd(minimal.diff()).degree() == 0
    sf = minimal.sqf_part()
    split_q = all(f.degree() == 1 for f, _ in sf.factor_list()[1])
    split_r = sf.count_roots(-sp.oo, sp.oo) == sf.degree()
    return characteristic, minimal, factors, blocks, squarefree, bool(split_q), bool(split_r)


def _spectrum_chart(blocks):
    values = [complex(sp.N(b["eigenvalue"], 16)) for b in blocks]
    return _chart("Spectre : positions dans le plan complexe", "Partie réelle", "Partie imaginaire",
                  [_series("Valeurs propres (affichage approché)", [v.real for v in values],
                           [v.imag for v in values], kind="dots")], equal=True)


def _kernel_chart(blocks, n):
    colors = ["green", "rose", "gold", "mint"]
    return _chart("Noyaux successifs : lire les tailles de Jordan", "k", "dim ker(A−λI)^k",
                  [_series("λ="+_text(b["eigenvalue"]), list(range(n+1)), b["kernels"], colors[i % 4])
                   for i, b in enumerate(blocks)])


def _display_jordan(A, characteristic, known_P=None, known_J=None):
    if known_P is not None:
        P, J = known_P, known_J
    elif all(f.degree() <= 2 for f, _ in characteristic.factor_list()[1]):
        P, J = A.jordan_form()
    else:
        # Des CRootOf représentent exactement les racines de degrés 3 et 4.
        # La structure reste certifiée par Smith, sans développer des radicaux illisibles.
        return None, None
    if P.det() == 0 or not _zero(A*P-P*J):
        raise ArithmeticError("Le changement de base de Jordan n'est pas certifié.")
    return P, J


def spectre(d):
    A, family, known_P, known_J = _input(d, SPECTRE_FAMILIES, "jordan42")
    field = _choice(d, "corps", "R", ["Q", "R", "C"])
    chi, mu, factors, blocks, squarefree, split_q, split_r = spectral_structure(A)
    split = {"Q": split_q, "R": split_r, "C": True}[field]
    diagonalizable = squarefree and split
    P, J = _display_jordan(A, chi, known_P, known_J)
    matrices = [_matrix("A", A, "Coefficients rationnels exacts ; colonnes = images des vecteurs de base.")]
    if P is not None:
        matrices += [_matrix("P : base de Jordan sur C", P, "A P = P J ; colonnes de P = vecteurs de la nouvelle base."),
                     _matrix("J = P⁻¹ A P", J, "Diagonale si et seulement si les blocs ont tous taille 1.")]
    notes = ["Diagonalisable sur le corps choisi ⇔ μ est scindé à racines simples sur ce corps.",
             "Trigonalisable sur le corps choisi ⇔ χ est scindé. Une valeur propre multiple peut avoir plusieurs blocs de taille 1.",
             "Le pivot de Gauss utilise des opérations sur les lignes : il donne une équivalence, pas en général une similitude P⁻¹AP.",
             "Les multiplicités et les dimensions des noyaux sont exactes ; seuls les points du plan complexe sont approchés."]
    if P is None:
        notes.append("Les racines CRootOf sont des nombres algébriques exacts. La structure de Jordan est certifiée par les facteurs invariants, sans développer des radicaux de degré 3 ou 4.")
    return dict(metrics=[_metric("Dimension", A.rows), _metric("χA(X)", _text(chi)),
                           _metric("μA(X)", _text(mu)), _metric("Diagonalisable sur "+field, "Oui" if diagonalizable else "Non"),
                           _metric("Trigonalisable sur "+field, "Oui" if split else "Non")],
                charts=[_spectrum_chart(blocks), _kernel_chart(blocks, A.rows)],
                table={"headers": ["λ exacte", "Multiplicité algébrique", "dim Eλ", "Tailles des blocs"],
                       "rows": [[_text(b["eigenvalue"]), b["algebraic"], b["geometric"], ", ".join(map(str, b["sizes"]))] for b in blocks]},
                matrices=matrices, notes=notes, scenes=[_jordan_scene(blocks)],
                pedagogy=_pedagogy("Reconstruire les chaînes de Jordan d'une matrice dense à partir des noyaux successifs.",
                    [("χ", "Multiplicités algébriques des valeurs propres"), ("μ", "Plus grande taille de chaîne pour chaque valeur propre"),
                     ("dₖ", "Dimension du noyau de (A−λI)^k")],
                    ["Suivre les flèches : chaque chaîne fournit un vecteur supplémentaire au noyau jusqu'à sa longueur.",
                     "Comparer Jordan 4+2 et 3+2+1 : même χ=(X−1)^6, mais μ et les pentes des noyaux diffèrent."],
                    ["Dans un bloc de taille s, dim ker(Jₛ(λ)−λI)^k=min(k,s).",
                     "dₖ−dₖ₋₁ compte les blocs de taille au moins k ; une nouvelle différence retrouve les blocs de taille exactement k."],
                    ["Pourquoi χ seul ne détermine-t-il pas les tailles de Jordan ?", "Quel plateau prouve que la valeur propre est semi-simple ?"]),
                theory=dict(family=family, field=field, characteristic=_text(chi), minimal=_text(mu),
                            invariant_factors=[_text(p) for p in factors], split=split,
                            semisimple=squarefree, diagonalizable=diagonalizable,
                            jordan_blocks=[dict(eigenvalue=_text(b["eigenvalue"]), sizes=b["sizes"], kernels=b["kernels"]) for b in blocks],
                            references=REFERENCES))


def dunford_newton(A):
    """Newton dans QQ[X]/(μ) : correction exacte, sans résolution approchée."""
    chi, mu, factors = exact_invariants(A)
    q = mu.sqf_part().monic()
    h = _poly(X).rem(mu)
    history = [dict(index=0, polynomial=h, residual=q.compose(h).rem(mu))]
    for index in range(1, A.rows+2):
        residual = q.compose(h).rem(mu)
        if residual.is_zero:
            break
        derivative = q.diff().compose(h).rem(mu)
        inverse = _poly(sp.invert(derivative, mu))
        h = (h-residual*inverse).rem(mu)
        history.append(dict(index=index, polynomial=h, residual=q.compose(h).rem(mu)))
    if not q.compose(h).rem(mu).is_zero:
        raise ArithmeticError("Newton n'a pas terminé dans l'algèbre quotient.")
    D = polynomial_evaluate(A, h)
    N = A-D
    index = max(exponent for _, exponent in mu.factor_list()[1])
    if not (_zero(A-D-N) and _zero(D*N-N*D) and _zero(N**index)
            and _zero(polynomial_evaluate(D, q))):
        raise ArithmeticError("Le certificat de Dunford est invalide.")
    return dict(A=A, D=D, N=N, characteristic=chi, minimal=mu, q=q,
                polynomial=h, history=history, nilpotence_index=int(index), factors=factors)


def dunford(d):
    A, family, known_P, known_J = _input(d, DUNFORD_FAMILIES, "dense6")
    field = _choice(d, "corps", "C", ["Q", "R", "C"])
    result = dunford_newton(A)
    chi, mu, factors, blocks, _, split_q, split_r = spectral_structure(A)
    split = {"Q": split_q, "R": split_r, "C": True}[field]
    P, J = _display_jordan(A, chi, known_P, known_J)
    matrices = [_matrix("A", A), _matrix("D = h(A)", result["D"], "q(D)=0 : partie semi-simple, diagonalisable sur un corps de décomposition."),
                _matrix("N = A−D", result["N"], "[D,N]=0 ; N est nilpotente.")]
    if P is not None:
        matrices += [_matrix("P", P, "Colonnes = base de Jordan ; A=PJP⁻¹."), _matrix("J", J)]
    history = result["history"]
    steps = [_step("Newton exact : étape "+str(item["index"]), polynomial_evaluate(A, item["polynomial"]),
                   "h"+str(item["index"])+"(X)="+_text(item["polynomial"])+" ; q(h) modulo μ = "+_text(item["residual"])) for item in history]
    ranks = [(result["N"]**k).rank() for k in range(A.rows+1)]
    notes = ["Calcul dans QQ[X]/(μ) : h₀=X, puis hₖ₊₁=hₖ−q(hₖ)/q′(hₖ), toujours modulo μ. L'inverse de q′(hₖ) est un inverse polynomial de Bézout.",
             "q est la partie sans facteur carré de μ ; en caractéristique zéro, q et q′ sont premiers entre eux. Les corrections de Newton terminent exactement, sans seuil numérique.",
             "A=D+N, [D,N]=0 et N^ν=0 sont vérifiés exactement. L'indice de la matrice nulle est ici 1.",
             "Sur Q ou R non scindé, D reste semi-simple et rationnelle, mais elle peut ne pas être diagonalisable sur ce corps. Sur C elle est diagonalisable."]
    return dict(metrics=[_metric("q(X)", _text(result["q"])), _metric("D=h(A)", _text(result["polynomial"])),
                           _metric("Indice de nilpotence ν", result["nilpotence_index"]),
                           _metric("Corrections de Newton", len(history)-1),
                           _metric("D diagonalisable sur "+field, "Oui" if split else "Non"),
                           _metric("Certificats A=D+N et [D,N]=0", "Exacts")],
                charts=[_chart("Nilpotence : rang de N^k", "k", "rang", [_series("rang N^k", range(A.rows+1), ranks)]),
                        _kernel_chart(blocks, A.rows)],
                table={"headers": ["Étape", "hₖ modulo μ", "q(hₖ) modulo μ"],
                       "rows": [[item["index"], _text(item["polynomial"]), _text(item["residual"])] for item in history]},
                matrices=matrices, steps=steps, notes=notes, scenes=[_jordan_scene(blocks, "D agit par λ ; N descend les chaînes")],
                pedagogy=_pedagogy("Séparer la croissance due aux valeurs propres de la mémoire nilpotente d'un endomorphisme dense.",
                    [("D", "Partie semi-simple h(A)"), ("N", "A−D, déplacement le long des chaînes"), ("q", "Radical sans carré du polynôme minimal")],
                    ["Sur une chaîne associée à λ, D multiplie par λ et N envoie chaque vecteur vers le précédent.",
                     "Le graphe de rang N^k révèle l'indice nilpotent ; les corrections de Newton construisent D sans changer de base."],
                    ["Dans Q[X]/(μ), q′(hₖ) est inversible par Bézout et le défaut q(hₖ₊₁) est multiple du carré du défaut précédent.",
                     "La nilpotence du radical assure la terminaison ; q(D)=0, N=A−D et [D,N]=0 sont certifiés exactement."],
                    ["Que devient N lorsque μ est sans carré ?", "Pourquoi une D rationnelle semi-simple peut-elle ne pas être diagonalisable sur R ?"]),
                theory=dict(family=family, field=field, characteristic=_text(chi), minimal=_text(mu),
                            squarefree=_text(result["q"]), dunford_polynomial=_text(result["polynomial"]),
                            nilpotence_index=result["nilpotence_index"], newton_iterations=len(history)-1,
                            D=serialize_matrix(result["D"]), N=serialize_matrix(result["N"]),
                            diagonalizable_over_field=split, references=REFERENCES))


def krylov(A, v, count=None):
    count = A.rows if count is None else count
    columns = []
    current = v
    for _ in range(count):
        columns.append(current)
        current = A*current
    return sp.Matrix.hstack(*columns) if columns else sp.zeros(A.rows, 0)


def vector_minimal(A, v):
    if _zero(v):
        return _poly(1)
    for k in range(1, A.rows+1):
        K = krylov(A, v, k)
        target = A**k*v
        if K.row_join(target).rank() == k:
            coefficients = K.gauss_jordan_solve(-target)[0]
            p = _poly(X**k+sum(coefficients[i]*X**i for i in range(k)))
            if not _zero(polynomial_evaluate(A, p)*v):
                raise ArithmeticError("Le polynôme du vecteur n'est pas un annulateur.")
            return p
    raise ArithmeticError("Aucune relation de Krylov trouvée.")


def cyclic_vector(A, minimal=None):
    """Une recherche finie exacte, seulement si deg μ=n.

    Le déterminant de Krylov est de degré n en les coordonnées de v ; la grille
    {0,...,n}^n garantit donc un témoin pour un endomorphisme cyclique.
    """
    minimal = exact_invariants(A)[1] if minimal is None else minimal
    n = A.rows
    if minimal.degree() < n:
        return sp.ones(n, 1)
    candidates = chain([sp.eye(n)[:, i] for i in range(n)], [sp.ones(n, 1)],
                       (sp.Matrix(entries) for entries in product(range(n+1), repeat=n)))
    for v in candidates:
        if krylov(A, v).det() != 0:
            return v
    raise ArithmeticError("La recherche de vecteur cyclique a échoué.")


def commutant_dimension(A):
    # Le rang d'un système dense n²×n² est inutile : le module fournit un
    # certificat exact de même dimension, via Hom(Q[X]/fᵢ,Q[X]/fⱼ).
    factors = exact_invariants(A)[2]
    return sum(a.gcd(b).degree() for a in factors for b in factors)


def cyclique(d):
    A, family, known_P, _ = _input(d, CYCLIQUE_FAMILIES, "recurrence6")
    terms = _integer(d, "terms", 18, 8, 40)
    mode = _choice(d, "vecteur", "cyclique", ["cyclique", "propre", "manuel"])
    chi, mu, factors = exact_invariants(A)
    if mode == "manuel":
        if d.get("v") is None or d.get("v") == "":
            raise ValueError("Indiquer les coordonnées rationnelles du vecteur v.")
        v = parse_vector(d["v"], A.rows)
    elif mode == "propre":
        rational_eigenvalues = [f for f, _ in chi.factor_list()[1] if f.degree() == 1]
        if not rational_eigenvalues:
            raise ValueError("A ne possède pas de valeur propre rationnelle : choisir un vecteur manuel ou une recherche cyclique.")
        eigenvalue = -rational_eigenvalues[0].nth(0)/rational_eigenvalues[0].nth(1)
        v = (A-eigenvalue*sp.eye(A.rows)).nullspace()[0]
    else:
        seed = known_P[:, 0] if known_P is not None else None
        v = seed if seed is not None and krylov(A, seed).rank() == A.rows else cyclic_vector(A, mu)
    K = krylov(A, v)
    p_v = vector_minimal(A, v)
    rank = K.rank()
    cyclic_A = mu.degree() == A.rows
    cyclic_v = rank == A.rows
    # Hom(Q[X]/fᵢ,Q[X]/fⱼ) a dimension deg pgcd(fᵢ,fⱼ).
    commutant = sum(a.gcd(b).degree() for a in factors for b in factors)
    matrices = [_matrix("A", A), _matrix("v", v), _matrix("K(v)=(v,Av,…,Aⁿ⁻¹v)", K, "Le rang décide si ce vecteur engendre tout l'espace.")]
    steps = [_step("Construire la famille de Krylov", K,
                   "dim Vect(v,Av,…) = deg pᵥ = "+str(p_v.degree())+" ; pᵥ(X)="+_text(p_v))]
    if cyclic_v:
        C = companion(mu)
        if not _zero(A*K-K*C):
            raise ArithmeticError("La relation A K = K C(μ) est invalide.")
        matrices.append(_matrix("K⁻¹ A K = C(μ)", C, "Compagnon : 1 sous la diagonale, coefficients opposés dans la dernière colonne."))
    elif rank:
        C = companion(p_v)
        matrices.append(_matrix("Restriction à Vect(v,Av,…)", C, "Compagnon de pᵥ dans la base de Krylov de ce sous-espace stable."))
    ranks = [krylov(A, v, k).rank() for k in range(A.rows+1)]
    observable = (known_P.inv() if known_P is not None else sp.eye(A.rows))[-1, :]
    sequence, current = [], v
    for _ in range(terms):
        sequence.append((observable*current)[0])
        current = A*current
    if any(sum(p_v.nth(j)*sequence[k+j] for j in range(p_v.degree()+1)) != 0
           for k in range(max(0, terms-p_v.degree()))):
        raise ArithmeticError("La suite observée ne respecte pas la récurrence de pᵥ.")
    scenes = [_companion_scene([p_v], "Le sous-espace engendré par v") ] if rank else []
    notes = ["Le bon quantificateur est ∃v : A est cyclique si un vecteur engendre une base de Krylov. Ce n'est pas une propriété de tous les vecteurs non nuls.",
             "A est cyclique ⇔ deg μ=n ⇔ μ=χ ⇔ il n'y a qu'un facteur invariant non unité.",
             "pᵥ divise μ et son degré est la dimension du sous-espace stable engendré par v. Un vecteur propre peut être non cyclique pour une matrice cyclique.",
             "Pour A cyclique, tout B qui commute avec A s'écrit comme un polynôme en A, et dim C(A)=dim Q[A]=n. Hors du cas cyclique, ces dimensions peuvent être différentes."]
    return dict(metrics=[_metric("A cyclique", "Oui" if cyclic_A else "Non"),
                           _metric("v cyclique", "Oui" if cyclic_v else "Non"), _metric("rang K(v)", rank),
                           _metric("pᵥ(X)", _text(p_v)), _metric("μA(X)", _text(mu)),
                           _metric("dim commutant C(A)", commutant), _metric("dim Q[A]", mu.degree())],
                charts=[_chart("Croissance du sous-espace de Krylov", "Nombre de colonnes k", "rang de Kₖ(v)",
                               [_series("Vecteur choisi", range(A.rows+1), ranks),
                                _series("Maximum possible", range(A.rows+1), range(A.rows+1), "gold")]),
                        _chart("Une suite linéaire observe les itérés A^k v", "k", "yₖ = ℓ(A^k v)",
                               [_series("Suite exacte, affichage approché", range(terms), [float(s) for s in sequence], "rose")])],
                table={"headers": ["k", "rang (v,…,Aᵏ⁻¹v)", "Gain de dimension"],
                       "rows": [[k, ranks[k], ranks[k]-ranks[k-1] if k else 0] for k in range(A.rows+1)]},
                matrices=matrices, steps=steps, notes=notes, scenes=scenes,
                pedagogy=_pedagogy("Transformer un problème matriciel en une récurrence scalaire, puis mesurer ce qu'un vecteur permet d'observer.",
                    [("K(v)", "Colonnes v, Av,…,Aⁿ⁻¹v"), ("pᵥ", "Première relation linéaire monique entre les itérés"),
                     ("yₖ", "Une observation linéaire ℓ(A^k v), dernière coordonnée dans la base construite quand elle est connue")],
                    ["La dernière colonne du compagnon revient vers les colonnes précédentes : ses poids donnent la récurrence.",
                     "Passer au vecteur propre réduit le rang à 1, même si A est cyclique ; la suite perd alors des modes."],
                    ["Si pᵥ(X)=ΣcⱼXʲ, alors ΣcⱼA^(k+j)v=0 ; appliquer ℓ donne Σcⱼyₖ₊ⱼ=0.",
                     "Une base de Krylov impose A K=K C(pᵥ) ; deg pᵥ=dim Vect(v,Av,…)."],
                    ["La récurrence d'une seule observation est-elle toujours minimale ?", "Pourquoi le commutant est-il de dimension n lorsque A est cyclique ?"]),
                theory=dict(family=family, vector_mode=mode, characteristic=_text(chi), minimal=_text(mu),
                            vector_minimal=_text(p_v), vector=serialize_matrix(v), rank=rank,
                            cyclic_matrix=cyclic_A, cyclic_vector=cyclic_v, commutant_dimension=commutant,
                            polynomial_algebra_dimension=mu.degree(), terms=terms,
                            observable=serialize_matrix(observable), sequence=[str(s) for s in sequence],
                            recurrence_coefficients=[str(p_v.nth(j)) for j in range(p_v.degree()+1)], references=REFERENCES))


def frobenius_family(name, shear=1):
    polynomials = {
        "irreductible": [X**2+1, X**2+1],
        "deux_facteurs": [X**2-1, (X**2-1)*(X-2)**2],
        "puissances": [X-1, (X-1)**3],
        "cyclique": [(X**2+1)**2],
        "meme_chi_a": [(X-1)**2, (X-1)**2*(X+2)**2],
        "meme_chi_b": [(X-1)**4*(X+2)**2],
    }
    factors = [_poly(p) for p in polynomials[name]]
    F = sp.diag(*[companion(p) for p in factors])
    P = _shear(F.rows, shear)
    if name in ("meme_chi_a", "meme_chi_b"):
        P = dense_basis(F.rows)*P
    A = P*F*P.inv()
    return A, P, F, factors


def frobenius(d):
    family = _choice(d, "famille", "meme_chi_a", ["meme_chi_a", "meme_chi_b", "irreductible", "deux_facteurs", "puissances", "cyclique"])
    shear = _integer(d, "shear", 1, 0, 3)
    A, P, F, expected = frobenius_family(family, shear)
    chi, mu, factors = exact_invariants(A)
    if factors != expected or not _zero(A*P-P*F):
        raise ArithmeticError("La reconstruction de Frobenius ne satisfait pas les certificats.")
    rows, chain_columns, start = [], [], 0
    for i, p in enumerate(factors):
        v = P[:, start]
        K = krylov(A, v, p.degree())
        if K != P[:, start:start+p.degree()] or not _zero(polynomial_evaluate(A, p)*v):
            raise ArithmeticError("Une chaîne cyclique de Frobenius n'est pas certifiée.")
        chain_columns.append(K)
        rows.append([i+1, _text(p), p.degree(), "f"+str(i+1)+" | f"+str(i+2) if i+1 < len(factors) else "μ = f"+str(i+1)])
        start += p.degree()
    notes = ["La forme rationnelle de Frobenius est diag(C(f₁),…,C(fᵣ)), avec f₁|…|fᵣ. Elle n'exige pas que χ soit scindé.",
             "Les facteurs invariants sont recalculés par la forme de Smith de XI−A dans QQ[X], indépendamment de la construction de la famille.",
             "χ=∏fᵢ et μ=fᵣ. P rassemble les bases de Krylov des sous-espaces cycliques : A P = P F.",
             "Le bloc C(X²+1) n'est ni diagonalisable ni trigonalisable sur Q ou R ; sur C il est diagonalisable, avec valeurs propres ±i. Une puissance (X²+1)² crée au contraire des blocs de Jordan de taille 2 sur C."]
    return dict(metrics=[_metric("Dimension", A.rows), _metric("Nombre de blocs compagnons", len(factors)),
                           _metric("χA(X)", _text(chi)), _metric("μA(X)", _text(mu)),
                           _metric("A cyclique", "Oui" if len(factors) == 1 else "Non"),
                           _metric("Certificats Smith et A P=P F", "Exacts")],
                charts=[_chart("Dimensions des sous-espaces cycliques", "Indice du facteur invariant", "deg fᵢ",
                               [_series("Dimension du bloc compagnon", range(1, len(factors)+1), [p.degree() for p in factors], kind="bars")])],
                table={"headers": ["i", "Facteur invariant fᵢ", "Degré", "Divisibilité"], "rows": rows},
                matrices=[_matrix("A = P F P⁻¹", A), _matrix("P : bases cycliques réunies", P),
                          _matrix("F : forme de Frobenius sur Q", F)],
                steps=[_step("Sous-espace cyclique "+str(i+1), K, "Colonnes : vᵢ,Avᵢ,… ; annulateur minimal fᵢ="+_text(factors[i])) for i, K in enumerate(chain_columns)],
                notes=notes, scenes=[_companion_scene(factors)],
                pedagogy=_pedagogy("Lire la décomposition rationnelle en sous-espaces cycliques et expliquer pourquoi un même χ peut cacher plusieurs similitudes.",
                    [("f₁|…|fᵣ", "Facteurs invariants de XI−A sur Q[X]"), ("F", "Somme de blocs compagnons"), ("P", "Réunion des bases de Krylov")],
                    ["Chaque ligne du réseau est un sous-espace cyclique stable ; les retours pondérés réalisent C(fᵢ).",
                     "Comparer les deux familles 6×6 : χ=(X−1)^4(X+2)^2 dans les deux cas, mais deg μ vaut 4 ou 6."],
                    ["La forme de Smith sur Q[X] certifie indépendamment les facteurs, leur divisibilité et leur produit χ.",
                     "Le module Qⁿ est la somme des Q[X]/(fᵢ) ; son annulateur minimal est le dernier facteur μ."],
                    ["Quel changement rend la matrice cyclique sans modifier χ ?", "Que devient C(X²+1) après extension à C ?"]),
                theory=dict(family=family, shear=shear, characteristic=_text(chi), minimal=_text(mu),
                            invariant_factors=[_text(p) for p in factors],
                            A=serialize_matrix(A), P=serialize_matrix(P), F=serialize_matrix(F), references=REFERENCES))


def newton_coefficients(A):
    """c₀=1, k cₖ + Σⱼ₌₁ᵏ cₖ₋ⱼ tr(Aʲ)=0, caractéristique zéro."""
    traces = [sp.trace(A**j) for j in range(1, A.rows+1)]
    coefficients = [sp.S.One]
    for k in range(1, A.rows+1):
        coefficients.append(-sum(coefficients[k-j]*traces[j-1] for j in range(1, k+1))/k)
    polynomial = _poly(sum(c*X**(A.rows-k) for k, c in enumerate(coefficients)))
    return polynomial, coefficients, traces


def faddeev_leverrier(A):
    B = sp.eye(A.rows)
    states, coefficients = [], [sp.S.One]
    for k in range(1, A.rows+1):
        c = -sp.trace(A*B)/k
        B = A*B+c*sp.eye(A.rows)
        coefficients.append(c)
        states.append(dict(index=k, coefficient=c, matrix=B))
    if not _zero(B):
        raise ArithmeticError("Faddeev–LeVerrier n'a pas produit Bₙ=0.")
    polynomial = _poly(sum(c*X**(A.rows-k) for k, c in enumerate(coefficients)))
    return polynomial, states


def cayley(d):
    A, family, _, _ = _input(d, CAYLEY_FAMILIES, "dense6")
    power = _integer(d, "power", 12, 0, 40)
    chi, mu, _ = exact_invariants(A)
    from_traces, coefficients, traces = newton_coefficients(A)
    from_faddeev, states = faddeev_leverrier(A)
    if chi != from_traces or chi != from_faddeev:
        raise ArithmeticError("Les coefficients de χ ne coïncident pas avec ceux du déterminant.")
    residual = polynomial_evaluate(A, chi)
    quotient, remainder = _poly(X**power).div(mu)
    power_matrix = polynomial_evaluate(A, remainder)
    if not _zero(residual) or power_matrix != A**power:
        raise ArithmeticError("L'identité de Cayley–Hamilton ou la réduction de puissance a échoué.")
    inverse_polynomial, inverse_matrix = None, None
    if chi.nth(0) != 0:
        inverse_polynomial = _poly(-(chi.as_expr()-chi.nth(0))/X/chi.nth(0)).rem(mu)
        inverse_matrix = polynomial_evaluate(A, inverse_polynomial)
        if not _zero(A*inverse_matrix-sp.eye(A.rows)):
            raise ArithmeticError("Le polynôme proposé pour l'inverse est invalide.")
    matrices = [_matrix("A", A), _matrix("χA(A) = 0", residual, "Vérification matricielle exacte, pas substitution d'un nombre dans un déterminant."),
                _matrix("A^"+str(power)+" = r(A)", power_matrix, "X^p=q(X)μ(X)+r(X), deg r < deg μ.")]
    if inverse_matrix is not None:
        matrices.append(_matrix("A⁻¹ = s(A)", inverse_matrix, "s(X)="+_text(inverse_polynomial)))
    xs = list(range(A.rows+3))
    span_dimensions = [min(k+1, mu.degree()) for k in xs]
    reduced_powers = [_poly(X**k).rem(mu) for k in range(max(13, min(power+1, 21)))]
    coefficient_series = [_series("Coefficient de X^"+str(j), range(len(reduced_powers)),
                                  [float(p.nth(j)) for p in reduced_powers], ["green", "rose", "gold", "mint", "blue", "purple"][j % 6])
                          for j in range(mu.degree())]
    notes = ["χA(X)=det(XI−A). Cayley–Hamilton affirme χA(A)=0, une identité entre matrices.",
             "Newton : c₀=1 et cₖ=−(1/k)Σⱼ₌₁ᵏ cₖ₋ⱼ tr(Aʲ). Faddeev–LeVerrier : B₀=I, cₖ=−tr(ABₖ₋₁)/k, Bₖ=ABₖ₋₁+cₖI.",
             "Ces algorithmes divisent par k : ce laboratoire travaille en caractéristique zéro. On ne les applique pas tels quels modulo un nombre premier.",
             "La division euclidienne par μ réduit toute puissance en une combinaison de I,A,…,Aᵈ⁻¹. Le reste modulo μ est unique ; on pourrait aussi employer χ, avec un degré parfois plus grand.",
             "A est inversible si et seulement si χ(0)≠0. Si χ(0)=0, aucun polynôme en A ne peut être son inverse."]
    return dict(metrics=[_metric("χA(X)", _text(chi)), _metric("μA(X)", _text(mu)),
                           _metric("χA(A)", "Matrice nulle, exactement"), _metric("Reste de X^"+str(power)+" modulo μ", _text(remainder)),
                           _metric("det A", _text(A.det())),
                           _metric("Polynôme de l'inverse", _text(inverse_polynomial) if inverse_polynomial is not None else "A singulière")],
                charts=[_chart("L'algèbre Q[A] finit par se stabiliser", "Plus grande puissance k", "dim Vect(I,A,…,A^k)",
                               [_series("Dimension exacte", xs, span_dimensions)]),
                        _chart("Calculer A^k avec seulement deg μ coefficients", "k", "Coefficient dans le reste de X^k modulo μ", coefficient_series)],
                table={"headers": ["k", "tr(A^k)", "cₖ par Newton", "cₖ par Faddeev"],
                       "rows": [[k, _text(traces[k-1]), _text(coefficients[k]), _text(states[k-1]["coefficient"])] for k in range(1, A.rows+1)]},
                matrices=matrices,
                steps=[_step("Faddeev–LeVerrier : B"+str(s["index"]), s["matrix"], "c"+str(s["index"])+"="+_text(s["coefficient"])+" ; Bₖ=ABₖ₋₁+cₖI") for s in states],
                notes=notes, scenes=[_companion_scene([mu], "Multiplier par X dans Q[X]/(μ)")],
                pedagogy=_pedagogy("Calculer exactement une grande puissance de A à partir des traces et d'une division euclidienne.",
                    [("tr(Aʲ)", "Sommes de puissances des valeurs propres, avec multiplicités"), ("rₖ", "Reste de X^k modulo μ"),
                     ("Q[A]", "Algèbre de dimension deg μ")],
                    ["Les courbes suivent les coefficients de rₖ : seuls deg μ nombres sont nécessaires pour représenter A^k.",
                     "Le réseau est celui de la multiplication par X dans l'algèbre quotient ; le dernier retour porte la relation μ=0."],
                    ["Les identités de Newton reconstruisent les coefficients de χ à partir des traces ; Faddeev–LeVerrier fournit Bₙ=0.",
                     "X^k=qμ+rₖ et μ(A)=0 donnent A^k=rₖ(A). Si χ(0)≠0, la même identité exprime A⁻¹ comme polynôme en A."],
                    ["Pourquoi réduire modulo μ plutôt que χ ?", "Quelles divisions empêchent d'appliquer Newton sans précaution en caractéristique positive ?"]),
                theory=dict(family=family, power=power, characteristic=_text(chi), minimal=_text(mu),
                            coefficients=[str(c) for c in coefficients], traces=[str(t) for t in traces],
                            power_quotient=_text(quotient), power_remainder=_text(remainder),
                            inverse_polynomial=_text(inverse_polynomial) if inverse_polynomial is not None else None,
                            power_matrix=serialize_matrix(power_matrix), references=REFERENCES))


REDUCTION_LABS = {"spectre": spectre, "dunford": dunford, "cyclique": cyclique,
                  "frobenius": frobenius, "cayley": cayley}


def calculate_lab(d):
    lab = d.get("lab", "spectre")
    if lab not in REDUCTION_LABS:
        raise ValueError("Laboratoire de réduction inconnu.")
    return REDUCTION_LABS[lab](d)
