from core.commands import execute_command
from core.logger import log
from tools.config_manager import load_config


def create_banner():

    config = load_config()

    banner = f"""
====================================
          C Y P H E R // CORE
====================================

 User: {config["username"]}
 Version: {config["version"]}
 Status: Online
 Mode: Terminal Assistant

 Theme: {config["theme"]}

 Modules:
 [✓] Command Handler
 [✓] Logger
 [✓] Calculator
 [✓] System Monitor
 [✓] File Manager
 [✓] Config Manager

 Type "help" for available commands.
 Enter "exit" to shutdown Cypher

====================================
"""

    return banner


def main():
    banner = create_banner()

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