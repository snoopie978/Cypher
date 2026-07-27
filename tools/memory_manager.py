import json
from datetime import datetime

tool_name = "memory"
tool_description = "Store and manage memories"

MEMORY_FILE = "memory/memories.json"


def load_memories():
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memories(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_memory():

    memory_text = input("Memory: ")
    category = input("Category: ")

    data = load_memories()

    memory = {
        "id": len(data["memories"]) + 1,
        "memory": memory_text,
        "category": category,
        "date": str(datetime.now().date())
    }

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
        for memory in data["memories"]:

            print("")
            print(f"ID: {memory['id']}")
            print(f"Memory: {memory['memory']}")
            print(f"Category: {memory['category']}")
            print(f"Date: {memory['date']}")

    print("")
    print("====================================")


def search_memory():

    search_term = input("Search: ").lower()

    data = load_memories()

    found = False

    print("")
    print("====================================")
    print("          MEMORY SEARCH")
    print("====================================")

    for memory in data["memories"]:

        if (search_term in memory["memory"].lower()
                or search_term in memory["category"].lower()):

            print("")
            print(f"ID: {memory['id']}")
            print(f"Memory: {memory['memory']}")
            print(f"Category: {memory['category']}")
            print(f"Date: {memory['date']}")

            found = True

    if not found:
        print("No matching memories found")

    print("")
    print("====================================")


def delete_memory():

    data = load_memories()

    view_memories()

    try:
        memory_id = int(input("Delete ID: "))

    except ValueError:
        print("Invalid ID")
        return

    for memory in data["memories"]:

        if memory["id"] == memory_id:

            data["memories"].remove(memory)

            save_memories(data)

            print("")
            print("Memory deleted:")
            print(memory["memory"])

            return

    print("Memory not found")


def update_memory():

    data = load_memories()

    view_memories()

    try:
        memory_id = int(input("Update ID: "))

    except ValueError:
        print("Invalid ID")
        return

    for memory in data["memories"]:

        if memory["id"] == memory_id:

            print("")
            print("Current memory:")
            print(memory["memory"])

            new_memory = input("New memory: ")
            new_category = input("New category: ")

            memory["memory"] = new_memory
            memory["category"] = new_category

            save_memories(data)

            print("")
            print("Memory updated")

            return

    print("Memory not found")


def run():

    while True:

        command = input("Cypher Memory > ").lower()

        if command == "add":
            add_memory()

        elif command == "view":
            view_memories()

        elif command == "search":
            search_memory()

        elif command == "delete":
            delete_memory()

        elif command == "update":
            update_memory()

        elif command == "exit":
            break

        else:
            print("Unknown memory command")