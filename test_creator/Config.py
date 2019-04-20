import json 
import os

'''
    "test_path": "path" 
'''
class Config:
    def __init__(self):
        self.filename = "config.json"     
        self.test_path = "tests"        
        self.static_path = "static" 
        self.encodedConfig = None  
        self.check_config() 
        self.commit_config() 
    
    def parse_config(self):
        with open(self.filename, "r+") as fd:
            return json.loads(fd.read())

    def check_config(self):
        with open(self.filename, "r+") as fd:
            # Write the default configuration to config.json  
            context = fd.read() 
            if len(context) == 0:
                fd.write(json.dumps({"test_path": self.test_path, "static_path": self.static_path}))
                fd.close() 
                self.encodedConfig = parse_config() 
            else:
                self.encodedConfig = json.loads(context)
    # **kwards for update any type of field  
    def update_config(self, **kwards):
        with open(self.filename, "r+") as fd:
            fd.write(json.dumps(kwards))
            fd.close()
    
    def commit_config(self):
        self.test_path = self.encodedConfig["test_path"]
        os.makedirs(self.test_path, exist_ok=True) 
