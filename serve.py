#!/usr/bin/env python3
"""Static server with COOP + COEP (credentialless) for @imgly/background-removal / ONNX."""

import http.server
import os
import socketserver

PORT = 8765
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        # credentialless is less likely to block fonts/CDN assets than require-corp
        self.send_header("Cross-Origin-Embedder-Policy", "credentialless")
        super().end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"http://127.0.0.1:{PORT}/")
        httpd.serve_forever()
