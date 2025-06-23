from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = 'localhost'
server_port = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><head><title>Python Web Server</title></head>', 'utf-8'))
        self.wfile.write(bytes('<body><p>Este es un ejemplo de servidor con Python.</p></body></html>', 'utf-8'))

if __name__ == '__main__':
    webServer = HTTPServer((hostname, server_port), MyServer)
    print(f'Servidor iniciando en http://{hostname}:{server_port}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Servidor detenido')
