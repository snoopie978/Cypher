from core.commands import execute_command
from core.logger import log


banner = """
====================================
          C Y P H E R // CORE
====================================

 Version: 0.1.0
 Status: Online
 Mode: Terminal Assistant

 Modules:
 [✓] Command Handler
 [✓] Logger
 [✓] Calculator
 [✓] System Monitor
 [✓] File Manager

 Type "help" for available commands.
 Enter "exit" to shutdown Cypher

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