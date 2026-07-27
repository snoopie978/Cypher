from tools.config_manager import show_config, set_config
from core.tool_loader import load_tools


# Load all tools automatically
tools = load_tools()


# ==========================
# Core Commands
# ==========================

def help():

    print("")
    print("====================================")
    print("          CYPHER COMMANDS")
    print("====================================")

    print("")
    print("Core Commands:")
    print("")

    print("help")
    print("about")
    print("config")
    print("exit")


    print("")
    print("Tools:")
    print("")

    for tool in tools:
        print(tool)


    print("")
    print("====================================")


def about():

    print("")
    print("Cypher is Greg's personal AI assistant")
    print("")


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


# ==========================
# Command Registry
# ==========================

func_dict = {

    # Core commands
    "help": help,
    "about": about,
    "config": config

}


# Add discovered tools
func_dict.update(tools)



# ==========================
# Command Executor
# ==========================

def execute_command(command):

    if command in func_dict:
        func_dict[command]()

    else:
        print("Unknown Command, enter 'help' to view commands")