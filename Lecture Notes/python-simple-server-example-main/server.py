"""
Based on https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7

Very simple HTTP server in python for logging requests
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class SimpleServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """Processes HTTP GET requests"""
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        """Processes HTTP POST requests"""
        # Get the size of the data:
        content_length = int(self.headers['Content-Length'])
        # Get the content of the data:
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write(f"POST request for {self.path}".encode('utf-8'))

def run(port=8080):
    logging.basicConfig(level=logging.INFO)
    http_server = HTTPServer(('', port), SimpleServer)
    logging.info('Starting HTTP server...\n')
    try:
        logging.info('Server running on http://0.0.0.0:%d', port)
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    http_server.server_close()
    logging.info('Stopping HTTP server...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()