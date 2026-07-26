import os


def show_location():
    location = os.getcwd()

    print("")
    print("Current Directory:")
    print(location)


def list_files():
    files = os.listdir()

    print("")
    print("Files:")

    for file in files:
        if os.path.isdir(file):
            print("[DIR]", file)
        else:
            print("[FILE]", file)


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

def open_file(filename):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            try:
                with open(filename, "r") as file:
                    content = file.read()

                print("")
                print(content)

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

    if found:
        print("")
        print("Found:")

        for item in found:
            print(item)

    else:
        print("No files found")



def file_manager():

    print("")
    print("====================================")
    print("          FILE MANAGER")
    print("====================================")

    while True:

        command = input("\nCypher Files > ")

        if command == "exit":
            print("Closing File Manager")
            break


        elif command == "location":
            show_location()


        elif command == "list":
            list_files()


        elif command.startswith("cd "):
            folder = command.replace("cd ", "")
            change_directory(folder)

        elif command == "back":
            go_back()
            print("Went back")

        elif command.startswith("open "):
            filename = command.replace("open ", "")
            open_file(filename)


        elif command.startswith("search "):
            term = command.replace("search ", "")
            search_files(term)


        else:
            print("Unknown command")