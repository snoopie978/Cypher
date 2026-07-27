import os

tool_name = "files"
tool_description = "Browse and manage files"


def show_location():
    print("")
    print("Current Directory:")
    print(os.getcwd())


def list_files():

    print("")
    print("Files:")

    for item in os.listdir():

        if os.path.isdir(item):
            print("[DIR] ", item)

        else:
            print("[FILE]", item)


def change_directory(folder):

    if os.path.exists(folder):

        if os.path.isdir(folder):

            os.chdir(folder)
            print(f"Changed directory to: {folder}")

        else:
            print("That is not a folder")

    else:
        print("Folder does not exist")


def go_back():

    os.chdir("..")
    print("Went back")


def open_file(filename):

    if os.path.exists(filename):

        if os.path.isfile(filename):

            try:

                with open(filename, "r") as file:
                    print("")
                    print(file.read())

            except Exception as error:
                print("Could not open file:", error)

        else:
            print("That is a folder")

    else:
        print("File does not exist")


def search_files(term):

    found = []

    for root, folders, files in os.walk(os.getcwd()):

        for file in files:

            if term.lower() in file.lower():
                found.append(os.path.join(root, file))

    print("")

    if found:

        print("Found:")

        for item in found:
            print(item)

    else:
        print("No files found")


def run():

    print("")
    print("====================================")
    print("          FILE MANAGER")
    print("====================================")

    while True:

        command = input("\nCypher Files > ").strip().lower()

        if command == "exit":
            print("Closing File Manager")
            break

        elif command == "location":
            show_location()

        elif command == "list":
            list_files()

        elif command == "back":
            go_back()

        elif command.startswith("cd "):
            change_directory(command[3:])

        elif command.startswith("open "):
            open_file(command[5:])

        elif command.startswith("search "):
            search_files(command[7:])

        else:
            print("Unknown command")