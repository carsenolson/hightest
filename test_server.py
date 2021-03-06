#!/usr/bin/env python3

import os
import cgi
import http.server
import templates
import Test
import Config
import Result 

config = Config.Config()
current_test = None # global variable for test 'caching' 
tests = Test.getAllTests(config.test_path)
result = None
results = []

class MainHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def do_GET(self):
        self.method = "GET" 
        self.route() 
    
    def do_POST(self):
        self.method = "POST" 
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

    def send_ok(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.end_headers()
    
    def route(self):    
        self.path_list = [x for x in self.path.split("/") if x]  
        print("path: ", self.path_list)  
        #it's a root request handle with index 
        if not self.path_list:
            self.index()
        elif len(self.path_list) == 1:
            if self.path_list[0] == "favicon.ico":
                self.send_ok() 
            elif self.path_list[0] == "testing": 
                self.testing()         
            elif self.path_list[0] == "save":
                self.save() 
        else:
            self.redirect("testing")  
    
    def show_student_form(self):
        self.wfile.write(bytes(templates.students_name_form, encoding="utf-8"))
        for test_name in tests:
            self.wfile.write(bytes(templates.test_option.safe_substitute(test_name=test_name), encoding="utf-8")) 
        self.wfile.write(bytes(templates.end_students_name_form, encoding="utf-8")) 
   
    def show_non_empty_student_form(self, student_name, student_group, test_name_selected):
        self.wfile.write(bytes(templates.non_empty_students_name_form.safe_substitute(
            student_name=student_name, student_group=student_group, test_name=test_name_selected), encoding="utf-8"))
        self.wfile.write(bytes(templates.end_students_name_form, encoding="utf-8"))  
    
    def show_nav1(self):
        self.wfile.write(bytes(templates.nav1, encoding="utf-8"))
    
    def index(self):
        if self.method == "POST":
            global current_test, result 
            postvars = self.get_post_data()
            print(postvars)
            name = postvars[b"student_name"][0].decode("utf-8")
            group = postvars[b"student_group"][0].decode("utf-8")
            test_name =  postvars[b"test_name"][0].decode("utf-8")
            current_test = Test.Test("").getTestFromFile(os.path.join(config.test_path, test_name)+".json")
            self.send_ok() 
            self.show_nav1() 
            self.show_non_empty_student_form(name, group, test_name)   
            self.show_test() 
        elif self.method == "GET": 
            self.send_ok()   
            self.show_nav1() 
            self.show_student_form() 
    
    def show_test(self):
        self.wfile.write(bytes(templates.start_form, encoding="utf-8"))
        for question in current_test.questions:
            self.wfile.write(bytes(templates.question_title_h3.safe_substitute(
                question_title=question["question_title"]), encoding="utf-8"))
            for answer in question["answers"]:
                self.wfile.write(bytes(templates.question_answer.safe_substitute(
                    question_answer=answer), encoding="utf-8"))
            self.wfile.write(bytes(templates.input_answer, encoding="utf-8"))
        self.wfile.write(bytes(templates.end_form, encoding="utf-8"))
    
    def testing(self):
        if self.method == "POST":
            global result 
            postvars = self.get_post_data()  
            name = postvars[b"student_name"][0].decode("utf-8")
            group = postvars[b"student_group"][0].decode("utf-8")
            test_name =  postvars[b"test_name"][0].decode("utf-8")
            result = Result.Result(name=name, student_group=group, test_name=test_name) 
            for answer in postvars[b"answers"]:
                result.answers.append(self.answers_to_list(answer.decode("utf-8")))
            result.save(config.results_path) 
            result = None 
            self.redirect("save") 
    
    def save(self):
        self.send_ok() 
        self.show_nav1() 
        self.wfile.write(b"Wow! You have completed the test!")  
    
    def answers_to_list(self, answers):
        return answers.split(";")

    
def main():
    httpd = http.server.HTTPServer(("0.0.0.0", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
