import json
import os 

def getAllResults(results_path):
    results = []
    for r in os.listdir(results_path):
        if r.endswith(".json"):
            results.append(r.replace(".json", ""))
    return results

class Result:
    def __init__(self, name="", student_group="", test_name=""):
        self.student_name = name
        self.student_group = student_group 
        self.test_name = test_name
        self.answers = []
     
    def save(self, result_path):
        with open(os.path.join(result_path, self.test_name+"_"+self.student_name+".json"), "w+") as fd:
            fd.write(json.dumps({"student_name": self.student_name, "student_group": self.student_group, 
                "test_name": self.test_name, "answers": self.answers}))
            fd.close()
    
