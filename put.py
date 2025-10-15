
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "race": "caucasian"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 202):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PUT(self):
        content_size = int(self.headers.get("Content-Length", 0))
        
        parsed_data = self.rfile.read(content_size)
        updated_data = json.loads(parsed_data.decode())
        
        data.append(updated_data) 
        self.send_data({
            "Message": "Data updated",
            "data": updated_data
        }, status= 203)

def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is running")
run()
