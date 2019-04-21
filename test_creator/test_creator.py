#!/usr/bin/env python3

import Test
import Config
import os.path
import templates
import http.server
from string import Template

config = Config.Config()
current_test = None # global variable for test 'caching' 
tests = Test.getAllTests(config.test_path)

class MainHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def do_GET(self):
        self.method = "GET" 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.route() 
    
    def do_POST(self):
        self.method = "POST" 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.route() 
    def route(self):    
        self.path_list = [x for x in self.path.split("/") if x]  
        #it's a root request handle with index 
        if not self.path_list:
            self.index()
        #path is with test_name check name & run with test  
        elif len(self.path_list) == 1:
            self.test()         
        #path is with test_name & question_index check & run question_form 
        elif len(self.path_list) == 2:
            pass
        #there is no anoter they to handle, return 404     
        else:
            self.wfile.write(b"404 not found<br>Usage: /test_name/int:question_index")  
    
    def index(self):
        if self.method == "POST":
            print(self.rfile.read()) 
        elif self.method == "GET": 
            global tests 
            tests = Test.getAllTests(config.test_path) 
            self.wfile.write(bytes(templates.nav.safe_substitute(static_path=config.static_path, 
            page_name="your tests"), encoding="utf-8")) 
            for test in tests:
                self.wfile.write(bytes(templates.test_list.safe_substitute(test_name=test), 
                        encoding="utf-8")) 
            self.wfile.write(bytes(templates.new_test_form, encoding="utf-8")) 
            self.wfile.write(bytes(templates.footer.safe_substitute(static_path=config.static_path), 
                encoding="utf-8")) 
            
    def test(self):
        global current_test 
        print(tests) 
        self.wfile.write(bytes(templates.nav.safe_substitute(
            page_name="test name: "+self.path_list[0],
            static_path=config.static_path), encoding="utf-8"))   
        for test in tests:
                self.wfile.write(bytes(templates.test_list.safe_substitute(test_name=test), 
                        encoding="utf-8"))  
        self.wfile.write(b"<br><br>") 
        for test_name in tests:
            if test_name == self.path_list[0]:
                current_test = Test.Test.getTestFromFile(os.path.join(config.test_path ,test_name+".json"))
            else:
                current_test = Test.Test(self.path_list[0]) 
        if not current_test.questions:
            self.wfile.write(b"<h3>There is no questions</h3>") 
        else:  
            for index, question in enumerate(current_test.questions):
                self.wfile.write(bytes(templates.question_list.safe_substitute(
                    test_name=self.path_list[0], 
                    question_index=index, 
                    question_title=question["question_title"][:20]), 
                    encoding="utf-8"))
             
    def question(self):
        pass


def main():
    httpd = http.server.HTTPServer(("", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
