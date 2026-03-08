import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 9000
Handler = http.server.SimpleHTTPRequestHandler

def open_browser():
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}")

threading.Thread(target=open_browser).start()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()