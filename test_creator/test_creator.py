#!/usr/bin/env python3

import Test
import Config
import templates
import http.server
from string import Template

config = Config.Config()

# TODO: write sequence of string.templates & handlers for paths
#       write client-js code to interact with question input & update 

def index(rw):
    tests = Test.getAllTests(config.test_path)     
    for test in tests:
        if test.endswith(".json"):
            rw.write(bytes(templates.test_list.safe_substitute(test_name=test), encoding="utf-8")) 

def test(rw):
    pass

def question(rw):
    pass

class MainHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, encoding="utf-8"))
        if self.path == "" or self.path == "/":
            index(self.wfile)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

def main():
    httpd = http.server.HTTPServer(("", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
