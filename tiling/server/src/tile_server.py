#!/usr/bin/env python3

import os
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, HTTPServer

PACKAGE_PREFIX = "coding"
TILES_DIR = "tiles"
HOST = "localhost"
PORT = 8000


class TileRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(f"/{TILES_DIR}/"):
            filepath = Path(".") / self.path[1:]
            if filepath.exists() and filepath.is_file():
                with open(filepath, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "application/json") # Assuming GeoJSON for simplicity
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
            else:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Tile not found")
                return
        else:
            super().do_GET()

            
def coding_run_server(host: str = HOST, port: int = PORT, tiles_directory: str = TILES_DIR):
    os.chdir(tiles_directory)
    server_address = (host, port)
    httpd = HTTPServer(server_address, TileRequestHandler)
    print(f"Serving tiles from http://{host}:{port}/{tiles_directory}/")
    httpd.serve_forever()

    
if __name__ == "__main__":
    coding_run_server()
