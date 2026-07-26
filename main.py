from core.commands import execute_command
from core.logger import log


banner = """
====================================
            C Y P H E R
====================================

 Version: 0.1.0
 Status: Online
 Mode: Terminal Assistant

 Type "help" for available commands.
 Enter 'exit' to quit Cypher
====================================
"""


def main():
    print(banner)

    log("Cypher started")

    while True:
        command = input("Cypher > ")

        log(f"Command entered: {command}")

        if command == "exit":
            log("Cypher closed")
            print("Closing Cypher")
            break

        execute_command(command)


main()