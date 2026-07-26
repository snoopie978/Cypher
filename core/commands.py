from tools.calculator import calc
from tools.system import system
from tools.file_manager import file_manager
from tools.config_manager import show_config, set_config
#Command Functions

def help(): 
    commands = [


        "help",
        "about",
        "calculator",
        "system",
        "files",
        "config"
        


    ]

    print("available commands are: ")
    for cmd in commands:
        print("")
        
        print(cmd)


def  about():
    print("")
    print("Cypher is gregs personal AI assistant")

def config():

    while True:

        command = input("Cypher Config > ")

        if command == "exit":
            break


        elif command == "show":
            show_config()


        elif command.startswith("set "):

            parts = command.split()

            setting = parts[1]
            value = parts[2]

            set_config(setting, value)


        else:
            print("Unknown config command")







#Command-Function dictionary
func_dict = {
    "help": help,
    "about": about,
    "calculator": calc,
    "system": system,
    "files": file_manager,
    "config": config
    

}
#Function to execute command function
def execute_command(command):
    if command in func_dict:
        func_dict[command]()
    else:
        print("Unknown Command, enter 'help' to view commands")