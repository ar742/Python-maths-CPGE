"""Modèle exact du Rubik's Cube 3×3, sans bibliothèque externe.

Une permutation p envoie la position i vers p[i]. La multiplication est
chronologique : p * q signifie « p, puis q », donc (p * q)[i] = q[p[i]].
L'état contient, à chaque emplacement, l'identité de la facette présente.
Les mouvements sont construits par rotations entières dans l'espace.
"""
from __future__ import annotations

from collections import Counter, deque
from math import factorial, lcm
import random
import re
import time

FACES = "URFDLB"
IDENTITY = tuple(range(54))
COLORS = dict(U="#f6f3e9", R="#dc5555", F="#29a887", D="#f1c64c", L="#ed9744", B="#588cda")
CORNER_NAMES = ("URF", "UFL", "ULB", "UBR", "DFR", "DLF", "DBL", "DRB")
EDGE_NAMES = ("UR", "UF", "UL", "UB", "DR", "DF", "DL", "DB", "FR", "FL", "BL", "BR")
CORNER_SLOTS = ((8, 9, 20), (6, 18, 38), (0, 36, 47), (2, 45, 11),
                (29, 26, 15), (27, 44, 24), (33, 53, 42), (35, 17, 51))
EDGE_SLOTS = ((5, 10), (7, 19), (3, 37), (1, 46), (32, 16), (28, 25),
              (30, 43), (34, 52), (23, 12), (21, 41), (50, 39), (48, 14))
GROUP_SIZE = factorial(8) * factorial(12) * 3**7 * 2**10


def geometry():
    """Facettes URFDLB, chaque face regardée de l'extérieur, ligne par ligne."""
    result = []
    for face in FACES:
        for r in range(3):
            for c in range(3):
                positions = {"U": (c-1, 1, r-1), "R": (1, 1-r, 1-c),
                             "F": (c-1, 1-r, 1), "D": (c-1, -1, 1-r),
                             "L": (-1, 1-r, c-1), "B": (1-c, 1-r, -1)}
                normals = {"U": (0, 1, 0), "R": (1, 0, 0), "F": (0, 0, 1),
                           "D": (0, -1, 0), "L": (-1, 0, 0), "B": (0, 0, -1)}
                result.append((positions[face], normals[face]))
    return tuple(result)


GEOMETRY = geometry()


def rotate(v, axis, direction):
    """Quart de tour signé autour d'un axe positif (règle de la main droite)."""
    x, y, z = v
    for _ in range(direction % 4):
        if axis == 0:
            x, y, z = x, -z, y
        elif axis == 1:
            x, y, z = z, y, -x
        else:
            x, y, z = -y, x, z
    return x, y, z


def compose(p, q):
    """Appliquer p puis q ; convention d'action à droite."""
    return tuple(q[p[i]] for i in range(len(p)))


def inverse_permutation(p):
    result = [0] * len(p)
    for i, target in enumerate(p):
        result[target] = i
    return tuple(result)


def quarter_turn(face):
    axis, layer = {"U": (1, 1), "R": (0, 1), "F": (2, 1),
                   "D": (1, -1), "L": (0, -1), "B": (2, -1)}[face]
    lookup = {g: i for i, g in enumerate(GEOMETRY)}
    p = list(IDENTITY)
    for i, (pos, normal) in enumerate(GEOMETRY):
        if pos[axis] == layer:
            p[i] = lookup[(rotate(pos, axis, -layer), rotate(normal, axis, -layer))]
    return tuple(p)


MOVES = {}
for _face in FACES:
    _p = quarter_turn(_face)
    MOVES[_face] = _p
    MOVES[_face+"2"] = compose(_p, _p)
    MOVES[_face+"'"] = inverse_permutation(_p)
TOKENS = tuple(face+suffix for face in FACES for suffix in ("", "'", "2"))
PULLS = {token: inverse_permutation(p) for token, p in MOVES.items()}


def parse(text):
    """Notation stricte : U R F D L B, suffixes ' ou 2 ; pas de eval."""
    if not isinstance(text, str) or len(text) > 12000:
        raise ValueError("La séquence doit être un texte de moins de 12 000 caractères.")
    text = text.replace("’", "'").replace("′", "'").strip().upper()
    tokens, position = [], 0
    pattern = re.compile(r"([URFDLB])([2']?)")
    while position < len(text):
        if text[position].isspace():
            position += 1
            continue
        match = pattern.match(text, position)
        if not match:
            raise ValueError(f"Notation incorrecte près de « {text[position:position+12]} ». Utilisez R, U', F2…")
        tokens.append(match.group(0))
        position = match.end()
    if len(tokens) > 1000:
        raise ValueError("Limite : 1 000 mouvements par séquence.")
    return tokens


def invert(tokens):
    return [t if t.endswith("2") else t[0] if t.endswith("'") else t+"'" for t in reversed(tokens)]


def simplify(tokens):
    """Réduction locale uniquement ; ne prétend pas produire un mot minimal."""
    stack = []
    for token in tokens:
        amount = 2 if token.endswith("2") else 3 if token.endswith("'") else 1
        if stack and stack[-1][0] == token[0]:
            amount = (amount + stack.pop()[1]) % 4
        if amount:
            stack.append((token[0], amount))
    return [face + {1: "", 2: "2", 3: "'"}[amount] for face, amount in stack]


def apply_move(state, token):
    return tuple(state[i] for i in PULLS[token])


def apply(state, tokens):
    for token in tokens:
        state = apply_move(state, token)
    return tuple(state)


def permutation(tokens):
    return inverse_permutation(apply(IDENTITY, tokens))


def cycles(p):
    seen, result = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        cycle, j = [], i
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = p[j]
        if len(cycle) > 1:
            result.append(cycle)
    return result


def order(p):
    return lcm(*(len(c) for c in cycles(p))) if cycles(p) else 1


def parity(p):
    return sum(len(c)-1 for c in cycles(p)) % 2


def cycle_text(p, labels):
    return " ".join("("+" → ".join(labels[i] for i in c)+")" for c in cycles(p)) or "e (identité)"


def facelets(state):
    return "".join(FACES[i//9] for i in state)


def decode_colors(text):
    """Identifier pièces et orientations ; rejeter pièces répétées et coins miroirs."""
    if not isinstance(text, str):
        raise ValueError("L'état doit être une chaîne de 54 lettres.")
    text = "".join(text.upper().split())
    if len(text) != 54 or Counter(text) != Counter({f: 9 for f in FACES}):
        raise ValueError("Il faut 54 lettres URFDLB, exactement 9 de chaque.")
    if any(text[9*i+4] != f for i, f in enumerate(FACES)):
        raise ValueError("Les centres doivent être U, R, F, D, L, B dans cet ordre.")
    result = list(IDENTITY)
    cp, co, ep, eo = [], [], [], []
    for slots, primary in ((CORNER_SLOTS, True), (EDGE_SLOTS, False)):
        piece_ids, orientations = [], []
        for target_slots in slots:
            found = None
            actual = tuple(text[i] for i in target_slots)
            for piece, source_slots in enumerate(slots):
                original = tuple(FACES[i//9] for i in source_slots)
                for orientation in range(len(slots[0])):
                    if all(actual[(n+orientation) % len(actual)] == original[n] for n in range(len(actual))):
                        found = piece, orientation, source_slots
                        break
                if found:
                    break
            if found is None:
                raise ValueError("Pièce inconnue ou coin miroir : les couleurs ne décrivent pas un cube standard.")
            piece, orientation, source_slots = found
            piece_ids.append(piece)
            orientations.append(orientation)
            for n, source in enumerate(source_slots):
                result[target_slots[(n+orientation) % len(target_slots)]] = source
        if len(set(piece_ids)) != len(slots):
            raise ValueError("Une pièce apparaît plusieurs fois ; vérifiez les couleurs.")
        if primary:
            cp, co = piece_ids, orientations
        else:
            ep, eo = piece_ids, orientations
    return tuple(result), (cp, co, ep, eo)


def cubies(state):
    return decode_colors(facelets(state))[1]


def validate_colors(text):
    state, (cp, co, ep, eo) = decode_colors(text)
    problems = []
    if sum(co) % 3:
        problems.append("Somme des orientations des coins non nulle modulo 3.")
    if sum(eo) % 2:
        problems.append("Somme des orientations des arêtes non nulle modulo 2.")
    if parity(cp) != parity(ep):
        problems.append("Les permutations des coins et des arêtes ont des parités différentes.")
    if problems:
        raise ValueError("Configuration physiquement impossible : " + " ".join(problems))
    return state


def validate_state(data):
    if not isinstance(data, list) or len(data) != 54 or any(type(i) is not int for i in data) or sorted(data) != list(IDENTITY):
        raise ValueError("État interne incorrect.")
    state = tuple(data)
    # Les identités des stickers d'une pièce doivent rester solidaires.
    canonical = validate_colors(facelets(state))
    if canonical != state:
        raise ValueError("Les facettes ne restent pas solidaires de leurs pièces.")
    return state


def info(state):
    cp, co, ep, eo = cubies(state)
    corner_map, edge_map = inverse_permutation(cp), inverse_permutation(ep)
    corner_changed = [i for i in range(8) if cp[i] != i or co[i] != 0]
    edge_changed = [i for i in range(12) if ep[i] != i or eo[i] != 0]
    return {"state": list(state), "facelets": facelets(state), "solved": state == IDENTITY,
            "stickers_changed": sum(i != s for i, s in enumerate(state)),
            "corners_changed": len(corner_changed), "edges_changed": len(edge_changed),
            "corner_names_changed": [CORNER_NAMES[i] for i in corner_changed],
            "edge_names_changed": [EDGE_NAMES[i] for i in edge_changed],
            "corner_cycles": cycles(corner_map), "edge_cycles": cycles(edge_map),
            "corner_cycle_text": cycle_text(corner_map, CORNER_NAMES),
            "edge_cycle_text": cycle_text(edge_map, EDGE_NAMES),
            "cp": cp, "co": co, "ep": ep, "eo": eo,
            "corner_parity": parity(cp), "edge_parity": parity(ep),
            "corner_sum": sum(co) % 3, "edge_sum": sum(eo) % 2,
            "order": order(state), "in_h": not any(co) and not any(eo) and set(ep[8:]) == set(range(8, 12))}


def scramble(length=12, seed=None):
    rng, result = random.Random(seed), []
    for _ in range(length):
        options = [t for t in TOKENS if not result or t[0] != result[-1][0]]
        result.append(rng.choice(options))
    return result


class SearchLimit(Exception):
    pass


def solve_short(state, max_depth=6, seconds=20):
    """BFS bidirectionnelle en métrique HTM, sans accès à l'historique.

    Un quart, un demi-tour et un quart inverse coûtent chacun 1. On construit
    des boules du graphe de Cayley. Le premier croisement donne un mot minimal
    dans la borne demandée. Aucun mouvement consécutif d'une même face n'est
    nécessaire dans un mot minimal, ce qui réduit la recherche sans perte.
    """
    if max_depth not in range(0, 7):
        raise ValueError("La recherche pédagogique est limitée à 6 mouvements.")
    started = time.monotonic()
    if state == IDENTITY:
        return {"moves": [], "visited": 1, "seconds": 0.0, "depth": 0}
    goal_depth, start_depth = (max_depth+1)//2, max_depth//2
    goal = bytes(IDENTITY)
    target = bytes(state)
    pulls = {t: PULLS[t] for t in TOKENS}

    def moved(s, token):
        return bytes(s[i] for i in pulls[token])

    def check_time():
        if time.monotonic()-started > seconds:
            raise SearchLimit("Temps de recherche dépassé. Essayez une borne plus petite.")

    backward = {goal: ()}
    queue = deque([(goal, ())])
    while queue:
        current, path = queue.popleft()
        if len(path) == goal_depth:
            continue
        for token in TOKENS:
            if path and path[-1][0] == token[0]:
                continue
            nxt = moved(current, token)
            if nxt not in backward:
                nxt_path = path+(token,)
                backward[nxt] = nxt_path
                queue.append((nxt, nxt_path))
        check_time()
    forward, queue = {target}, deque([(target, ())])
    while queue:
        current, path = queue.popleft()
        if current in backward:
            solution = list(path)+invert(backward[current])
            assert apply(state, solution) == IDENTITY
            return {"moves": solution, "visited": len(forward)+len(backward),
                    "seconds": round(time.monotonic()-started, 3), "depth": len(solution)}
        if len(path) == start_depth:
            continue
        for token in TOKENS:
            if path and path[-1][0] == token[0]:
                continue
            nxt = moved(current, token)
            if nxt not in forward:
                forward.add(nxt)
                queue.append((nxt, path+(token,)))
        check_time()
    raise SearchLimit(f"Aucune solution de longueur ≤ {max_depth} HTM. Cela ne signifie pas que le cube est insoluble.")


def solve_complete(state):
    """Adaptateur optionnel : le solveur Kociemba reste une dépendance séparée."""
    try:
        import kociemba
    except ImportError as exc:
        raise ValueError("Le solveur complet optionnel n'est pas installé. Consultez LISEZ_MOI.md.") from exc
    if state == IDENTITY:
        return []
    result = parse(kociemba.solve(facelets(state)))
    if apply(state, result) != IDENTITY:
        raise ValueError("La solution proposée par le module externe n'a pas passé la vérification.")
    return result
