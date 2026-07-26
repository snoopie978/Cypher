import json


CONFIG_FILE = "config/settings.json"


def load_config():
    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)

    return config


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