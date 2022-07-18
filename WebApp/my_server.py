import sys
import os.path as osp 
from pathlib import Path 
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST_NAME = "localhost"
PORT = 8080
DIRECTORY = osp.join(Path(__file__).parent, "templates") 

class PythonServer(SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == "__main__":
    server = HTTPServer((HOST_NAME, PORT), PythonServer)
    print(f"Server started http://{HOST_NAME}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)