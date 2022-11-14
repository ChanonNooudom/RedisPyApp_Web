from http.server import HTTPServer, BaseHTTPRequestHandler
import redis
from urllib.parse import urlparse, parse_qs
import cgi
import db_helper
from jinja2 import Template
from random import randrange
import time

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        try:
            if ".html" in self.path:
                url = self.path[1:]
                self.send_response(200)
                self.end_headers()
                if  url == 'index.html':
                    RenderTemplate(self, url, ds = ['1','2', '3'], dd = "st")
                elif url == 'EventLog.html':
                    CreateEventLogTable()
                    RenderTemplate(self, url, items = SelectEventLog())
                else:
                    RenderTemplate(self, url)
            else:
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write((file_to_open))
        except Exception as e:
            print(e) 
            file_to_open = "Not found"
            self.send_response(404)
            # self.send_header('Location', "index.html")
            self.end_headers()
        

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        config_string = self.rfile.read(content_length).decode("UTF-8")
        url = self.path[1:]
        try:
                parms = config_string.split("&")
                for key in parms:
                    data = key.split("=")
                    key = data[0]
                    value = data[1]
                    if url == "Config.html":
                        # print("key: {}".format(key))
                        # print("value: {}".format(value))
                        Publish(key, value)
                        SetVariable(key, value)
                    elif url == "EventLog.html":
                        if key == "mode" and value == "delete":
                            DeleteEventLog()
                        elif key == "mode" and value == "create":
                            GenerateEventLog()
        except Exception as e:
            print(e)
        
        self.send_response(301)
        self.send_header('Location',url)
        self.end_headers()
        # self.wfile.write( bytes( "<h1>sss</h1>", "utf-8"))


def CreateEventLogTable():
    db_helper.CreateTable("CREATE TABLE IF NOT EXISTS event_log (" + 
        "  id INTEGER PRIMARY KEY " +
        ", item INTEGER " + 
        ", unit_1 INTEGER " + 
        ", unit_2 INTEGER " +
        ", psu_1 INTEGER " +
        ", psu_2 INTEGER " + 
        ", wg_sw INTEGER " + 
        ", timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")

def SelectEventLog():
    result = db_helper.Select("SELECT id, unit_1, unit_2, psu_1, psu_2, wg_sw, timestamp FROM event_log order by timestamp desc")
    return result

def DeleteEventLog():
    db_helper.Delete("DELETE FROM event_log")

def GenerateEventLog():
    for i in range(5):
        db_helper.Insert("INSERT INTO event_log (item, unit_1, unit_2, psu_1, psu_2, wg_sw) values ({}, {}, {}, {}, {}, {})".format(randrange(3),randrange(3),randrange(3),randrange(3),randrange(3),randrange(3)))
        time.sleep(1)


def RenderTemplate(self, url, **data):
    with open(url, 'r') as f:
            template = Template(f.read())
            rendered_url = 'rendered_' + url
    with open(rendered_url, 'w') as f:
        f.write(template.render(data))
    f = open(rendered_url).read()
    self.wfile.write(bytes(f, 'utf-8'))

def Publish(channel, msg):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)#, health_check_interval=2)

    q = r.pubsub()
    q.subscribe(channel)

    msg = '{"message": "' + msg + '"}'

    r.publish(channel, msg)


def SetVariable(key, value):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)#, health_check_interval=2)
    r.set(key, value)

httpd = HTTPServer(('localhost', 8080), web_server)
httpd.serve_forever()