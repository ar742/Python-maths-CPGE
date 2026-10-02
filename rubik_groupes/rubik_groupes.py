"""Lancer le cours illustré : python rubik_groupes.py (Python 3.10+).

Application locale, bibliothèque standard ; l'interface s'ouvre dans un
navigateur. Le moteur mathématique et les recherches sont en Python.
"""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import secrets
import socket
import threading
import traceback
from urllib.request import urlopen
import webbrowser

import cube
from cours import EXERCISES, LESSONS, PRESETS, SOURCES

ROOT = Path(__file__).resolve().parent


def execute(data):
    """API sans état partagé : chaque requête porte sa configuration."""
    action = data.get("action")
    if action == "scramble":
        length = data.get("length", 12)
        if type(length) is not int or not 1 <= length <= 100:
            raise ValueError("Le mélange doit contenir de 1 à 100 gestes.")
        tokens = cube.scramble(length)
        return {"sequence": " ".join(tokens), "moves": tokens}
    if action == "analyse":
        tokens = cube.parse(data.get("sequence", ""))
        state = cube.apply(cube.IDENTITY, tokens)
        result = cube.info(state)
        result.update(sequence=" ".join(tokens), inverse=" ".join(cube.invert(tokens)),
                      reduced=" ".join(cube.simplify(tokens)),
                      sticker_cycles=cube.cycle_text(cube.permutation(tokens),
                                                    [f"{cube.FACES[i//9]}{i%9+1}" for i in range(54)]))
        return result
    if action == "compare":
        a, b = cube.parse(data.get("a", "")), cube.parse(data.get("b", ""))
        ab = cube.apply(cube.IDENTITY, a+b)
        ba = cube.apply(cube.IDENTITY, b+a)
        c = a+b+cube.invert(a)+cube.invert(b)
        conjugate = a+b+cube.invert(a)
        return {"ab": cube.info(ab), "ba": cube.info(ba),
                "difference": [i for i in range(54) if ab[i] != ba[i]],
                "commute": ab == ba, "commutator": cube.info(cube.apply(cube.IDENTITY, c)),
                "commutator_sequence": " ".join(c),
                "conjugate": cube.info(cube.apply(cube.IDENTITY, conjugate)),
                "conjugate_sequence": " ".join(conjugate)}
    if action == "import":
        return cube.info(cube.validate_colors(data.get("facelets", "")))
    if action == "impossible":
        state = list(cube.IDENTITY)
        kind = data.get("kind")
        if kind == "twist":
            slots = cube.CORNER_SLOTS[0]
            for i, s in enumerate(slots):
                state[slots[(i+1) % 3]] = s
        elif kind == "flip":
            a, b = cube.EDGE_SLOTS[0]
            state[a], state[b] = state[b], state[a]
        elif kind == "parity":
            for a, b in zip(cube.EDGE_SLOTS[0], cube.EDGE_SLOTS[1]):
                state[a], state[b] = state[b], state[a]
        else:
            raise ValueError("Exemple inconnu.")
        try:
            cube.validate_colors(cube.facelets(state))
        except ValueError as exc:
            return {"legal": False, "reason": str(exc), "preview": cube.info(state)}
        raise ValueError("L'exemple devait être impossible.")
    state = cube.validate_state(data.get("state", list(cube.IDENTITY)))
    if action == "apply":
        return cube.info(cube.apply(state, cube.parse(data.get("sequence", ""))))
    if action == "timeline":
        tokens = cube.parse(data.get("sequence", ""))
        if len(tokens) > 300:
            raise ValueError("Pour une animation, limitez la séquence à 300 mouvements.")
        steps = []
        for token in tokens:
            state = cube.apply_move(state, token)
            steps.append({"token": token, "info": cube.info(state)})
        return {"steps": steps}
    if action == "solve":
        mode = data.get("mode")
        if mode == "history":
            history = cube.parse(data.get("history", ""))
            if cube.apply(cube.IDENTITY, history) != state:
                raise ValueError("L'historique ne décrit pas cet état. Utilisez la recherche courte ou le solveur complet.")
            solution = cube.simplify(cube.invert(history))
            result = {"moves": solution, "method": "Inverse de l'historique · réduction locale", "optimal": False}
        elif mode == "short":
            depth = data.get("depth", 6)
            if type(depth) is not int:
                raise ValueError("La profondeur doit être un entier.")
            result = cube.solve_short(state, depth)
            solution = result["moves"]
            result.update(method="Recherche en largeur bidirectionnelle · HTM", optimal=True)
        elif mode == "complete":
            solution = cube.solve_complete(state)
            result = {"moves": solution, "method": "Kociemba · deux phases (module optionnel)", "optimal": False}
        else:
            raise ValueError("Méthode inconnue.")
        if cube.apply(state, solution) != cube.IDENTITY:
            raise ValueError("La solution ne résout pas le cube : vérification refusée.")
        result["verified"] = True
        return result
    raise ValueError("Action inconnue.")


class Handler(BaseHTTPRequestHandler):
    server_version = "RubikGroupes/1.0"

    def log_message(self, format, *args):
        # Garder le terminal lisible : les erreurs Python restent visibles.
        pass

    def send(self, content, status=200, mime="application/json; charset=utf-8"):
        if isinstance(content, (dict, list)):
            content = json.dumps(content, ensure_ascii=False).encode("utf-8")
        elif isinstance(content, str):
            content = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(content)

    def allowed_host(self):
        port = self.server.server_port
        return self.headers.get("Host") in (f"127.0.0.1:{port}", f"localhost:{port}")

    def do_GET(self):
        if not self.allowed_host():
            self.send({"error": "Hôte refusé."}, 403)
            return
        path = self.path.split("?", 1)[0]
        if path == "/api/bootstrap":
            self.send({"token": self.server.api_token, "lessons": LESSONS, "exercises": EXERCISES,
                       "presets": PRESETS, "sources": SOURCES, "identity": cube.info(cube.IDENTITY),
                       "geometry": cube.GEOMETRY, "faces": cube.FACES, "colors": cube.COLORS,
                       "corners": cube.CORNER_NAMES, "edges": cube.EDGE_NAMES,
                       "group_size": str(cube.GROUP_SIZE),
                       "complete_solver": importlib.util.find_spec("kociemba") is not None})
            return
        resources = {"/": ("index.html", "text/html; charset=utf-8"),
                     "/index.html": ("index.html", "text/html; charset=utf-8"),
                     "/style.css": ("style.css", "text/css; charset=utf-8"),
                     "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                     "/favicon.svg": ("favicon.svg", "image/svg+xml")}
        if path not in resources:
            self.send({"error": "Ressource inconnue."}, 404)
            return
        filename, mime = resources[path]
        self.send((ROOT/filename).read_bytes(), mime=mime)

    def do_POST(self):
        # Consommer un petit corps avant tout refus : sous Windows, fermer une
        # socket avec un corps non lu peut masquer la réponse par un reset TCP.
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 100_000:
                raise ValueError("Requête trop grande ou vide.")
            self.connection.settimeout(10)
            payload = self.rfile.read(length)
        except (ValueError, OSError) as exc:
            self.send({"error": str(exc)}, 400)
            return
        if self.path != "/api" or not self.allowed_host():
            self.send({"error": "Requête refusée."}, 403)
            return
        origin = self.headers.get("Origin")
        allowed = {f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}"}
        if origin and origin not in allowed:
            self.send({"error": "Origine refusée."}, 403)
            return
        if self.headers.get("X-Rubik-Token") != self.server.api_token:
            self.send({"error": "Session invalide. Rechargez la page."}, 403)
            return
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            self.send({"error": "Format JSON attendu."}, 400)
            return
        try:
            data = json.loads(payload)
            if not isinstance(data, dict):
                raise ValueError("Objet JSON attendu.")
            self.send(execute(data))
        except (ValueError, KeyError, TypeError, cube.SearchLimit) as exc:
            self.send({"error": str(exc)}, 400)
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception:
            traceback.print_exc()
            self.send({"error": "Erreur du moteur. Consultez le terminal puis relancez l'application."}, 500)


class LocalHTTPServer(ThreadingHTTPServer):
    # Sur Windows, SO_REUSEADDR peut autoriser plusieurs serveurs à écouter le
    # même port. Ils auraient des jetons distincts et des réponses imprévisibles.
    allow_reuse_address = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def make_server(port=8765):
    server = LocalHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    server.api_token = secrets.token_urlsafe(24)
    return server


def main():
    parser = argparse.ArgumentParser(description="Théorie des groupes et Rubik's Cube · cours CPGE illustré")
    parser.add_argument("--port", type=int, default=8765, help="port local (défaut : 8765)")
    parser.add_argument("--no-browser", action="store_true", help="ne pas ouvrir automatiquement le navigateur")
    parser.add_argument("--export-illustrations", action="store_true", help="exporter les schémas SVG puis quitter")
    args = parser.parse_args()
    if args.export_illustrations:
        from illustrations import export
        print(f"Illustrations : {export(ROOT / 'illustrations')}")
        return
    if not 0 <= args.port <= 65535:
        parser.error("Le port doit être compris entre 0 et 65535.")
    try:
        server = make_server(args.port)
    except OSError as exc:
        # Un double clic répété réouvre une application déjà lancée.
        existing_url = f"http://127.0.0.1:{args.port}"
        try:
            with urlopen(existing_url+"/api/bootstrap", timeout=2) as response:
                existing = json.load(response)
            if existing.get("group_size") == str(cube.GROUP_SIZE) and len(existing.get("lessons", [])) == 10:
                print(f"Rubik & Groupes fonctionne déjà : {existing_url}")
                if not args.no_browser:
                    webbrowser.open(existing_url)
                return
        except (OSError, ValueError):
            pass
        parser.exit(1, f"Impossible d'ouvrir le port {args.port} : {exc}\nEssayez --port 8766.\n")
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Rubik & Groupes — niveau maths sup / maths spé\nOuvrez {url}\nFermer : Ctrl+C dans cette fenêtre.\n")
    if not args.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nApplication fermée.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
