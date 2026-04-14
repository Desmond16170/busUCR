#!/usr/bin/env python3
import http.server
import os
from urllib.parse import urlparse, unquote

PORT = 8080

REDIRECTS = {
    "/coronado": "/coronado.html",
    "/tibas": "/tibas.html",
    "/heredia": "/heredia.html",
    "/acosta": "/acosta.html",
    "/san_ramon": "/san_ramon.html",
    "/santa_ana_escazu": "/santa_ana_escazu.html",
    "/alajuela": "/alajuela.html",
    "/san_rafael": "/san_rafael.html",
    "/desamparados": "/desamparados.html",
    "/periferica": "/periferica.html",
    "/pavas": "/pavas.html",
    "/creditos": "/creditos.html",
    "/interlinea": "/interlinea.html",
    "/182930adminherrera": "/admin.html",
    "/servicios": "/servicios.html",
}

class BusUCRHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        raw_path = unquote(urlparse(self.path).path)
        path = raw_path.rstrip("/") or "/"

        print("RAW PATH:", raw_path)
        print("NORMALIZED PATH:", path)

        if path in REDIRECTS:
            self.path = REDIRECTS[path]
            print("REWRITTEN TO:", self.path)
        else:
            print("NO REDIRECT MATCH")

        super().do_GET()

    def log_message(self, format, *args):
        print(f"  {self.address_string()} → {format % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"\n🚌 BusUCR local server corriendo en http://localhost:{PORT}")
print("   Ctrl+C para detener\n")
http.server.HTTPServer(("", PORT), BusUCRHandler).serve_forever()