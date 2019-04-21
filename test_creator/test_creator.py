#!/usr/bin/env python3

import Test
import Config
import templates
import http.server
from string import Template

config = Config.Config()

# TODO: write sequence of string.templates & handlers for paths
#       write client-js code to interact with question input & update 
#       think more about templates (may be add more urls) 

# Route class represents  
class Route():
    def __init__(self, rw, path, method):
        self.rw = rw 
        self.path = path 
        self.method = method 
        self.current_test = None 
    def index(self):
        tests = Test.getAllTests(config.test_path) 
        if method == "GET": 
            for test in tests:
                if test.endswith(".json"):
                    rw.write(bytes(templates.test_list.safe_substitute(test_name=test.rstrip(".json")), 
                        encoding="utf-8")) 
        elif method == "POST":
            pass 
    
    def test(self):
        pass      

    def question(self):
        pass

# / - index page - returns all links to tests
# /test_name/ - reutrns all questions and tests
# POST - create a new test 
#  
# /test_name/<int:question_index> - returns a form for updating and adding question
#                                   if the question exists - updates 
#                                   else adding new question
# POST - recieve question data and update or add 

class MainHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def do_GET(self):
        print(dir(self))  
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<p>You accessed path: %s</p>" % bytes(self.path, encoding="utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"thanks for your post data") 
        print(self.headers.items()) 

def main():
    httpd = http.server.HTTPServer(("", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
