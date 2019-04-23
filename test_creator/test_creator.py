#!/usr/bin/env python3

import cgi
import Test
import Config
import os.path
import templates
import http.server
from string import Template

config = Config.Config()
current_test = None # global variable for test 'caching' 
tests = Test.getAllTests(config.test_path)

# absolutely unreadable code using only string template
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
        #self.send_response(200)
        #self.send_header("Location", "/test/")
        #self.end_headers()
        self.route() 
   
    def get_post_data(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == "multipart/form-data":
            return cgi.parse_multipart(self.rfile, pdict)
        elif ctype == "application/x-www-form-urlencoded":
            length = int(self.headers.get('content-length'))
            return cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            return {} 

    def route(self):    
        self.path_list = [x for x in self.path.split("/") if x]  
        print("path: ", self.path_list)  
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
            self.send_response(302)
            postvars = self.get_post_data() 
            self.send_header("Location", "/"+postvars[b"test_name"][0].decode("utf-8")+"/")
            self.end_headers()
        
        elif self.method == "GET": 
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            global tests 
            tests = Test.getAllTests(config.test_path) 
            self.wfile.write(bytes(templates.nav.safe_substitute(page_name="your tests"), 
                encoding="utf-8")) 
            for test in tests:
                self.wfile.write(bytes(templates.test_list.safe_substitute(test_name=test), 
                        encoding="utf-8")) 
            self.wfile.write(bytes(templates.new_test_form, encoding="utf-8")) 
            
    def test(self):
        global current_test 
        print("test_files", tests) 
        self.wfile.write(bytes(templates.nav.safe_substitute(
            page_name="test name: "+self.path_list[0],
            static_path=config.static_path), encoding="utf-8"))   
        for test_name in tests:
            if test_name == self.path_list[0]:
                current_test = Test.Test.getTestFromFile(os.path.join(config.test_path,
                    test_name+".json"))
            else:
                current_test = Test.Test(self.path_list[0]) 
        if not current_test.questions:
            self.wfile.write(b"<h3>There is no questions</h3><br>") 
        else:  
            for index, question in enumerate(current_test.questions):
                self.wfile.write(bytes(templates.question_list.safe_substitute(
                    test_name=self.path_list[0], 
                    question_index=index, 
                    question_title=question["question_title"][:20]), 
                    encoding="utf-8"))
        self.wfile.write(bytes(templates.add_new_question_link.safe_substitute(
            test_name=current_test.name, 
            question_index=len(current_test.questions)), 
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
