import json
import os

def getAllTests(path):
    tests = [] 
    for f in os.listdir(path):  
        if f.endswith(".json"):
            tests.append(f.rstrip(".json"))    
    return tests

class Test():
    def __init__(self, name, time=20): 
        self.name = name  
        self.time = time 
        self.questions = [] 
    
    @classmethod
    def newTest(self, name, time=20):
        self.name = name
        self.time = time
        return self 
    
    @classmethod 
    def getTestFromFile(self, path):
        with open(path, "r+") as fd:  
            parsedTest = json.loads(fd.read())
            self.name = parsedTest["test_name"]  
            self.time = parsedTest["time"]
            self.questions = parsedTest["questions"] 
            fd.close()
        return self
    
    def update_time(time):
        self.time = time
    
    def update_name(name):
        self.name = name
    
    # **kwards presents all question fields  
    def add_question(self, **kwards):
        if question_type == "selection":  
            self.questions.append({"question_type": question_type, 
                "question_title": question_title, "answers": kwards.answers, 
                "true_answers": kwards.true_answers, "images": images})
        else:
            self.questions.append({"question_type": question_type, 
                "question_title": question_title, "question_answer": kwards.answer, 
                "images": images})
     
    # **kwards presents all question fields  
    def update_question(self, question_index, **kwards):
        if question_type == "selection":  
            self.questions[question_index] = {"question_type": question_type, 
                "question_title": question_title, "answers": kwards.answers, 
                "true_answers": kwards.true_answers, "images": images}
        else:
            self.questions[question_index] = {"question_type": question_type, 
                "question_title": question_title, "question_answer": kwards.answer, 
                "images": images}
 
    def get_question(self, question_index): 
        return self.questions[question_index]         
    
    def delete_question(self, question_index):
        del(self.questions[question_index])
    
    # **kwards have attribute/s to update in a specific question    
    def update_question(self, question_index, **kwards):
        for key in kwards.keys():
            self.questions[question_index][key] = kwards[key] 
    
    def saveTest(self, test_path):
        with open(os.path.join(test_path,self.name+".json"), "r+") as fd:
            fd.write(json.dumps({"test_name": self.name, "time": self.time, 
                "questions": self.questions}))
            fd.close() 
