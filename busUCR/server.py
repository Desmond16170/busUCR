#!/usr/bin/env python3
"""
Servidor local para probar BusUCR unificado.
Simula los redirects de Netlify (rutas sin .html).

Uso: python3 server.py
Luego abrí: http://localhost:8080
"""

import http.server
import os

PORT = 8080

REDIRECTS = {
    "/coronado":         "/coronado.html",
    "/tibas":            "/tibas.html",
    "/heredia":          "/heredia.html",
    "/acosta":           "/acosta.html",
    "/san_ramon":        "/san_ramon.html",
    "/santa_ana_escazu": "/santa_ana_escazu.html",
    "/alajuela":         "/alajuela.html",
    "/san_rafael":       "/san_rafael.html",
    "/desamparados":     "/desamparados.html",
    "/periferica":       "/periferica.html",
    "/pavas":            "/pavas.html",
    "/creditos":         "/creditos.html",
    "/182930adminherrera": "/admin.html",
    "/servicios": "/servicios.html",
}

class BusUCRHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path in REDIRECTS:
            self.path = REDIRECTS[path]
        super().do_GET()

    def log_message(self, format, *args):
        print(f"  {self.address_string()} → {format % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"\n🚌 BusUCR local server corriendo en http://localhost:{PORT}")
print(f"   Ctrl+C para detener\n")
http.server.HTTPServer(("", PORT), BusUCRHandler).serve_forever()
