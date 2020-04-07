from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl  
import json

data = {'result': 'this is a test'}
host = ('localhost', 8888)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':

    httpd = HTTPServer(host, SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./cert/server.pem', server_side=True)
    print("Starting server, listen at: %s:%s" % host)
    httpd.serve_forever()