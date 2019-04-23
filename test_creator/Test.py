import json
import os

def getAllTests(path):
    tests = [] 
    for f in os.listdir(path):  
        if f.endswith(".json"):
            tests.append(f.replace(".json", ""))    
    return tests

class Test():
    def __init__(self, name, time=20): 
        self.name = name  
        self.time = time 
        self.questions = [] 
    
    def getTestFromFile(self, path):
        with open(path, "r+") as fd:  
            parsedTest = json.loads(fd.read())
            self.name = parsedTest["name"]  
            self.time = parsedTest["time"]
            self.questions = parsedTest["questions"] 
            print("PARSED JSON: ", parsedTest)  
            fd.close()
        return self 
    
    def update_time(time):
        self.time = time
    
    def update_name(name):
        self.name = name
    
    # **kwards presents all question fields  
    def add_question(self, **kwards):
        self.questions.append({"question_title": kwards["question_title"], "answers": kwards["answers"], 
            "true_answers": kwards["true_answers"]})
        print("after append: ", self.questions) 
    
    # **kwards presents all question fields  
    def update_question(self, question_index, **kwards):
        self.questions[question_index] = {"question_title": kwards["question_title"], "answers": kwards["answers"], 
                "true_answers": kwards["true_answers"]}
 
    def get_question(self, question_index): 
        return self.questions[question_index]         
    
    def delete_question(self, question_index):
        del(self.questions[question_index])
    
    # **kwards have attribute/s to update in a specific question    
    def update_question(self, question_index, **kwards):
        for key in kwards.keys():
            self.questions[int(question_index)][key] = kwards[key] 
    
    def save(self, test_path):
        with open(os.path.join(test_path,self.name+".json"), "w+") as fd:
            fd.write(json.dumps({"name": self.name, "time": self.time, 
                "questions": self.questions}))
            fd.close() 
