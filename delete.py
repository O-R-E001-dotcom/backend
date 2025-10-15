from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "race": "caucasian",
        "race": "asian",
        "race": "african"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=202):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_DELETE(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)
        delete_data = json.loads(parsed_data.decode())

        # Extract the race to delete
        race_to_delete = delete_data.get("race")

        # Find and remove matching entry
        global data
        new_data = [item for item in data if item.get("race") != race_to_delete]
        
        # Check if anything was deleted
        if len(new_data) < len(data):
            data[:] = new_data  # update global list
            self.send_data({
                "Message": f"'{race_to_delete}' deleted successfully"
                }, status=200)
        else:
            self.send_data({
                "Error": f"No record found for '{race_to_delete}'"
                }, status=404)


def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is running")
run()
