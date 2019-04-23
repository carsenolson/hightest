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

# something wrond with writer and reader tests 
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
        #path is with test_name check name & run with test  
        elif len(self.path_list) == 1:
            if self.path_list[0] == "favicon.ico":
                self.send_ok() 
            else: 
                self.test()         
        #path is with test_name & question_index check & run question_form 
        elif len(self.path_list) == 2:
            self.question() 
        #there is no anoter they to handle, return 404     
        elif len(self.path_list) == 3 and self.path_list == "delete":
            self.delete_question() 
        else:
            self.wfile.write(b"404 not found<br>Usage: /test_name/int:question_index")  
    
    def index(self):
        if self.method == "POST":
            postvars = self.get_post_data() 
            self.redirect("/"+postvars[b"test_name"][0].decode("utf-8")+"/") 
        elif self.method == "GET": 
            self.send_ok() 
            global tests 
            tests = Test.getAllTests(config.test_path) 
            self.wfile.write(bytes(templates.nav.safe_substitute(page_name="your tests"), 
                encoding="utf-8")) 
            for test in tests:
                self.wfile.write(bytes(templates.test_list.safe_substitute(test_name=test), 
                        encoding="utf-8")) 
            self.wfile.write(bytes(templates.new_test_form, encoding="utf-8")) 
           
    def test_lookup(self):
        global current_test
        for test_name in tests:
            print("test name: ", test_name) 
            if test_name == self.path_list[0]:
                current_test = Test.Test.getTestFromFile(os.path.join(config.test_path, test_name)+".json")
        current_test = Test.Test(self.path_list[0])
    
    def delete_question(self):
        if current_test == None or current_test.name != self.path_list[0]:
            self.test_lookup()
        current_test.delete_question(int(self.path_list[1]))
        current_test.saveTest(config.test_path)
        self.redirect("/"+current_test.name+"/") 

    def test(self):
        self.send_ok() 
        print("test_files", tests) 
        self.wfile.write(bytes(templates.nav.safe_substitute(page_name="test name: "+self.path_list[0], 
            static_path=config.static_path), encoding="utf-8"))   
        if current_test == None or current_test.name != self.path_list[0]:
            self.test_lookup()
        print("test from test view: ", current_test) 
        print("questions from test view: ", current_test.questions) 
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
    
    def question_in_questions(self):
        return int(self.path_list[1]) < len(current_test.questions)     
     
    def answers_to_text(self, question_field, question_index): 
        answers = "" 
        if len(current_test.questions[question_index][question_field]) <= 1:
            answers = current_test.questions[question_index][question_field][0] 
        else:
            for index, a in enumerate(current_test.questions[question_index][question_field]):
                if index < len(current_test.questions[question_index][question_field])-1: 
                    answers += str(a) 
                    answers += ";" 
                else:
                    answers += str(a) 
        return answers
    def answers_to_list(self, answers):
        return answers.split(";")
    def question(self):
        if self.method == "POST":
            if current_test == None or current_test.name != self.path_list[0]: 
                self.test_lookup() 
            postvars = self.get_post_data() 
            answers = self.answers_to_list(postvars[b"answers"][0].decode("utf-8")) 
            true_answers = self.answers_to_list(postvars[b"true_answers"][0].decode("utf-8")) 
            print("test name: ", current_test.name) 
            print("post data from question: ", postvars) 
            if self.question_in_questions():
                current_test.update_question(self.path_list[1], 
                        question_title=postvars[b"question_title"][0].decode("utf-8"), 
                        answers=answers, true_answers=true_answers)
            else: 
                current_test.add_question(question_title=postvars[b"question_title"][0].decode("utf-8"), 
                        answers=answers, true_answers=true_answers)
            current_test.save(config.test_path) 
            print(current_test.questions) 
            self.redirect("/"+current_test.name+"/") 
        if self.method == "GET":
            self.send_ok() 
            # handle when user get question from url without visiting test page 
            if current_test == None or current_test.name != self.path_list[0]:
                self.test_lookup()
            self.wfile.write(bytes(templates.nav.substitute(page_name="you are editing question of test: "+current_test.name), encoding="utf-8"))   
            print("questions: ", current_test.questions) 
            cq = int(self.path_list[1]) 
            if self.question_in_questions():  
                answers = self.answers_to_text("answers", cq) 
                true_answers = self.answers_to_text("true_answers", cq) 
                self.wfile.write(bytes(templates.question_form.substitute(
                    question_title=current_test.questions[cq]["question_title"],
                    answers=answers, 
                    true_answers=true_answers  
                    ),encoding="utf-8")) 
                   
            else:
                self.wfile.write(bytes(templates.empty_question_form, encoding="utf-8")) 
def main():
    httpd = http.server.HTTPServer(("", 8080), MainHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    main()
