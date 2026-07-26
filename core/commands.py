from tools.calculator import calc
from tools.system import system
#Command Functions

def help(): 
    commands = [


        "help",
        "about",
        "calculator",
        "system"
        


    ]

    print("available commands are: ")
    for cmd in commands:
        print("")
        
        print(cmd)


def  about():
    print("")
    print("Cypher is gregs personal AI assistant")







#Command-Function dictionary
func_dict = {
    "help": help,
    "about": about,
    "calculator": calc,
    "system": system
    

}
#Function to execute command function
def execute_command(command):
    if command in func_dict:
        func_dict[command]()
    else:
        print("Unknown Command, enter 'help' to view commands")