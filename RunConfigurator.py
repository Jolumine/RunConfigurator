import subprocess
import json 
import os
import sys


class RunConfigurator:
    def __init__(self, arguments) -> None:
        self.config_file = "./configs.json"
        if len(arguments) > 1: 
            self.script = arguments[1].split("-")[1]
            self.execute()
        else: 
            print("Error, no configuration specified.")
        
    # Main Method 
    def execute(self):
        if self.script == "init" and not os.path.exists(self.config_file): # inits the whole application 
            print("Initilization")
            with open(self.config_file, "w") as f: 
                f.write("{}")
        
        elif self.script == "add" and os.path.exists(self.config_file): # creates new script / configuration
            print("Add configuration: ")
            name = input("Name: ")
            path = input("Script Path (Enter absolute path): ")
            args = input("Script parameters (default: []): ")

            with open(self.config_file, "r") as f: 
                parsed = json.load(f)
                parsed[name] = {"file": path, "args": args}
            
            with open(self.config_file, "w") as f: 
                json.dump(parsed, f, indent=4, sort_keys=False)
        
        else: # Executes the script
            if os.path.exists(self.config_file):
                with open(self.config_file, "r") as f: 
                    parsed = json.load(f)
                if self.script in parsed:
                    file = parsed[self.script]["file"]
                    folder = "".join(os.listdir("."))

                    if "env" in folder:
                        if parsed[self.script]["args"] != "":
                            args = parsed[self.script]["args"].split(" ")
                            subprocess.call(["python", file] + args)
                        else: 
                            pass  
                        for element in os.listdir("."):
                            if "env" in element: 
                                python = f"./{element}/Scripts/python.exe"
                                subprocess.call([python, file])

                    else: 
                        if parsed[self.script]["args"] != "":
                            args = parsed[self.script]["args"].split(" ")
                            subprocess.call(["python", file] + args)
                        else: 
                            subprocess.call(["python", file])
                else: 
                    print("Error, command not defined.")
            else: 
                print("Error, -init first.")

    

def main():
    RunConfigurator(sys.argv)



if __name__ == "__main__":
    main()