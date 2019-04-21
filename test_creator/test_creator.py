#!/usr/bin/env python3

import Test
import Config
import templates
import http.server
from string import Template

config = Config.Config()
current_test = None # global variable for test 'caching' 
tests = None # list of test names in test_path

# TODO: write sequence of string.templates & handlers for paths
#       write client-js code to interact with question input & update 
#       think more about templates (may be add more urls) 
  

# This class is analyzes the path and calls 'views' as class's methods 
class Route():
    def __init__(self, rw, path, method):
        self.rw = rw 
        self.path = path 
        self.method = method 
        self.path_list = [x for x in self.path.split("/") if x] 
         
        #it's a root request handle with index 
        if not self.path_list:
            self.index()
        #path is with test_name check name & run with test  
        elif len(self.path_list) == 1:
            pass         
        #path is with test_name & question_index check & run question_form 
        elif len(self.path_list) == 2:
            pass
        #there is no anoter they to handle, return 404     
        else:
            self.rw.write(b"404 not found<br>Usage: /test_name/int:question_index") 
    
    # Below views methods
    def index(self):
        global tests 
        tests = Test.getAllTests(config.test_path) 
        self.rw.write(bytes(templates.nav.safe_substitute(page_name="your tests"), encoding="utf-8")) 
        if self.method == "GET": 
            for test in tests:
                self.rw.write(bytes(templates.test_list.safe_substitute(test_name=test), 
                        encoding="utf-8")) 
            self.rw.write(bytes(templates.new_test_form, encoding="utf-8")) 
            self.rw.write(bytes(templates.footer.sefe_substitute(static_path=config.static_path), encoding="utf-8")) 
        elif method == "POST":
            pass 
    
    def test(self):
        #check for tests
        pass 
    def question(self):
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
        Route(self.wfile, self.path, "GET")
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        Route(self.wfile, self.path, "POST")

def main():
    httpd = http.server.HTTPServer(("", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
