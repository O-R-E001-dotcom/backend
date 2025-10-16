from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the requested path (e.g. "/", "/users", "/items")
        path = self.path

        if path == "/":
            data = {"message": "Welcome to my simple API!"}

        elif path == "/users":
            data = {"users": ["Alice", "Bob", "Charlie"]}

        elif path == "/items":
            data = {"items": ["apple", "banana", "mango"]}

        else:
            # For unknown paths
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())
            return  # Stop execution here

        # If route matched, send a normal 200 response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


# Run the server
server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
