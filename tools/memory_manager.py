import json


MEMORY_FILE = "memory/memories.json"


def load_memories():
    with open(MEMORY_FILE, "r") as file:
        data = json.load(file)

    return data


def save_memories(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_memory():

    memory = input("Memory: ")

    data = load_memories()

    data["memories"].append(memory)

    save_memories(data)

    print("Memory saved")


def view_memories():

    data = load_memories()

    print("")
    print("====================================")
    print("          CYPHER MEMORY")
    print("====================================")

    if len(data["memories"]) == 0:
        print("No memories stored")

    else:
        for index, memory in enumerate(data["memories"], start=1):
            print(f"{index}. {memory}")

    print("====================================")


def memory_menu():

    while True:

        command = input("Cypher Memory > ")

        if command == "add":
            add_memory()

        elif command == "view":
            view_memories()

        elif command == "exit":
            break

        else:
            print("Unknown memory command")