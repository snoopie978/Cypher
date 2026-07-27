import json

tool_name = "config"
tool_description = "Manage Cypher settings"

CONFIG_FILE = "config/settings.json"


def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)


def show_config():

    config = load_config()

    print("")
    print("====================================")
    print("        CYPHER CONFIGURATION")
    print("====================================")

    for setting, value in config.items():
        print(f"{setting}: {value}")

    print("====================================")


def set_config(setting, value):

    config = load_config()

    if setting in config:

        config[setting] = value
        save_config(config)

        print(f"Changed {setting} to {value}")

    else:
        print("Unknown setting")


def run():

    while True:

        command = input("Cypher Config > ").strip()

        if command == "exit":
            break

        elif command == "show":
            show_config()

        elif command.startswith("set "):

            parts = command.split(maxsplit=2)

            if len(parts) != 3:
                print("Usage: set <setting> <value>")
                continue

            setting = parts[1]
            value = parts[2]

            set_config(setting, value)

        else:
            print("Unknown config command")