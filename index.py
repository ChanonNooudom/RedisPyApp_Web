from http.server import HTTPServer, BaseHTTPRequestHandler
import redis
from urllib.parse import urlparse, parse_qs
import cgi
import db_helper

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)

        except:
            file_to_open = "File not found"
            self.send_response(302)
            self.send_header('Location', "index.html")

        if self.path.find("isButtonPressed=true") != -1:
            
            parsed_url = urlparse(self.path)
            m = parse_qs(parsed_url.query)['myInput'][0]
            Publish(m)
            print("Button clicked")

        self.end_headers()
        
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        if (self.path == "/index.html"):
            result = db_helper.ReadDb()
            table = db_helper.GenerateTable(result)
            self.wfile.write(bytes(table, 'utf-8'))


def Publish(m):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True, health_check_interval=2)

    q = r.pubsub()
    q.subscribe('channel_a')

    m = '{"message": "' + m + '"}'

    r.publish("channel_a", m)

httpd = HTTPServer(('localhost', 8080), web_server)
httpd.serve_forever()