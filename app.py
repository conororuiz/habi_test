from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from models import get_properties


class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests from the server.
        Responds to property queries
        """
        if self.path == '/properties':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                filters = json.loads(post_data.decode('utf-8'))
                properties = get_properties(filters)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(properties).encode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid JSON"}')
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler):
    """
    Starts the HTTP server.

    Args:
        server_class: Class of the HTTP server (by default, HTTPServer).
        handler_class: Class that handles requests (by default, RequestHandler).
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()