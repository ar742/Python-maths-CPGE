"""Lancer : python chimie_organique.py ; modèles physiques NumPy et figures animées."""
from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import socket
import threading
import traceback
from http.client import HTTPConnection
import webbrowser

from modeles import calculate
from cours import LESSONS, EXERCISES, SOURCES
from reperes import LAB_GUIDES
from catalogue import LABS

ROOT = Path(__file__).resolve().parent


def figure_metadata():
    path = ROOT/"illustrations"/"catalogue.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf8"))
    return [dict(file=p.name, title=p.stem.replace("_", " "))
            for p in sorted((ROOT/"illustrations").glob("*.svg"))]



class Handler(BaseHTTPRequestHandler):
    server_version = "ChimieOrganique/1.0"

    def log_message(self, format, *args):
        pass

    def send(self, content, status=200, mime="application/json; charset=utf-8", download=None):
        if isinstance(content, (dict, list)):
            content = json.dumps(content, ensure_ascii=False, allow_nan=False).encode("utf-8")
        elif isinstance(content, str):
            content = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        if download:
            self.send_header("Content-Disposition", f'attachment; filename="{download}"')
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        # Envoyer les réponses volumineuses par blocs bornés.
        for start in range(0, len(content), 32_768):
            self.wfile.write(content[start:start+32_768])

    def allowed_host(self):
        p = self.server.server_port
        return self.headers.get("Host") in (f"127.0.0.1:{p}", f"localhost:{p}")

    def do_GET(self):
        if not self.allowed_host():
            self.send({"error": "Hôte refusé."}, 403)
            return
        path = self.path.split("?", 1)[0]
        if path.startswith("/api/export/"):
            with self.server.calcul_lock:
                result = self.server.exports.get(path.removeprefix("/api/export/"))
            if result is None:
                self.send({"error": "Export expiré. Recalculez l’expérience."}, 404)
            else:
                self.send(result, download=f"chimie_organique-{result['lab']}.json")
            return
        if path == "/api/bootstrap":
            self.send({"application": "chimie_organique", "token": self.server.api_token,
                       "lessons": LESSONS, "exercises": EXERCISES, "sources": SOURCES,
                       "lab_guides": LAB_GUIDES, "labs": LABS, "figures": figure_metadata()})
            return
        files = {"/": ("index.html", "text/html; charset=utf-8"),
                 "/index.html": ("index.html", "text/html; charset=utf-8"),
                 "/style.css": ("style.css", "text/css; charset=utf-8"),
                 "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                 "/visuals.js": ("visuals.js", "text/javascript; charset=utf-8"),
                 "/favicon.svg": ("favicon.svg", "image/svg+xml")}
        if path.startswith("/illustrations/"):
            filename = path.removeprefix("/illustrations/")
            allowed = {p.name for p in (ROOT/"illustrations").glob("*.svg")}
            if filename in allowed:
                self.send((ROOT/"illustrations"/filename).read_bytes(), mime="image/svg+xml")
                return
        if path not in files:
            self.send({"error": "Ressource inconnue."}, 404)
            return
        file, mime = files[path]
        self.send((ROOT/file).read_bytes(), mime=mime)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 20_000:
                raise ValueError("Requête trop grande ou vide.")
            self.connection.settimeout(10)
            payload = self.rfile.read(length)
        except (ValueError, OSError) as exc:
            self.send({"error": str(exc)}, 400)
            return
        p = self.server.server_port
        if self.path != "/api/calculate" or not self.allowed_host():
            self.send({"error": "Requête refusée."}, 403)
            return
        if self.headers.get("Origin") not in (None, f"http://127.0.0.1:{p}", f"http://localhost:{p}"):
            self.send({"error": "Origine refusée."}, 403)
            return
        if self.headers.get("X-CPGE-Token") != self.server.api_token:
            self.send({"error": "Session invalide. Rechargez la page."}, 403)
            return
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            self.send({"error": "Format JSON attendu."}, 400)
            return
        try:
            def invalid_constant(value):
                raise ValueError("Les nombres non finis sont refusés.")
            data = json.loads(payload, parse_constant=invalid_constant)
            if not isinstance(data, dict):
                raise ValueError("Objet JSON attendu.")
            with self.server.calcul_lock:
                result = calculate(data)
                export_id = secrets.token_urlsafe(18)
                result["export_id"] = export_id
                self.server.exports[export_id] = result
                if len(self.server.exports) > 4:
                    del self.server.exports[next(iter(self.server.exports))]
                self.send(result)
        except (ValueError, TypeError, KeyError) as exc:
            self.send({"error": str(exc)}, 400)
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception:
            traceback.print_exc()
            self.send({"error": "Erreur de calcul. Consultez le terminal."}, 500)


class LocalHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = False

    def server_bind(self):
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()


def make_server(port=8775):
    server = LocalHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    server.api_token = secrets.token_urlsafe(24)
    server.calcul_lock = threading.Lock()
    server.exports = {}
    return server


def main():
    parser = argparse.ArgumentParser(description="Chimie organique · CPGE sup / spé")
    parser.add_argument("--port", type=int, default=8775)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--export-illustrations", action="store_true")
    args = parser.parse_args()
    if args.export_illustrations:
        from illustrations import export
        print(export(ROOT/"illustrations"))
        return
    if not 0 <= args.port <= 65535:
        parser.error("Le port doit être entre 0 et 65535.")
    try:
        server = make_server(args.port)
    except OSError as exc:
        url = f"http://127.0.0.1:{args.port}"
        try:
            connection = HTTPConnection("127.0.0.1", args.port, timeout=2)
            try:
                connection.request("GET", "/api/bootstrap")
                existing = json.loads(connection.getresponse().read())
            finally:
                connection.close()
            if existing.get("application") == "chimie_organique":
                if not args.no_browser:
                    webbrowser.open(url)
                print(f"L'atelier fonctionne déjà : {url}")
                return
        except (OSError, ValueError):
            pass
        parser.exit(1, f"Port indisponible : {exc}\nEssayez --port 8780.\n")
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"Chimie organique · CPGE sup / spé\nOuvrez {url}\nFermer : Ctrl+C.\n")
    if not args.no_browser:
        threading.Timer(.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAtelier fermé.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
