import time
from colorama import Fore, Style, init

init()

from core.commands import execute_command
from core.logger import log
from tools.config_manager import load_config


def create_banner():

    config = load_config()

    banner = f"""
{Fore.GREEN}====================================
          C Y P H E R // CORE
===================================={Style.RESET_ALL}

{Fore.CYAN} User:{Style.RESET_ALL} {config["username"]}
{Fore.CYAN} Version:{Style.RESET_ALL} {config["version"]}
{Fore.CYAN} Status:{Style.RESET_ALL} Online
{Fore.CYAN} Mode:{Style.RESET_ALL} Terminal Assistant

{Fore.YELLOW} Modules:{Style.RESET_ALL}

 {Fore.GREEN}[✓]{Style.RESET_ALL} Command Handler
 {Fore.GREEN}[✓]{Style.RESET_ALL} Logger
 {Fore.GREEN}[✓]{Style.RESET_ALL} Calculator
 {Fore.GREEN}[✓]{Style.RESET_ALL} System Monitor
 {Fore.GREEN}[✓]{Style.RESET_ALL} File Manager
 {Fore.GREEN}[✓]{Style.RESET_ALL} Config Manager

{Fore.CYAN} Type "help" for available commands.
 Enter "exit" to shutdown Cypher{Style.RESET_ALL}

{Fore.GREEN}===================================={Style.RESET_ALL}
"""

    return banner

def startup_sequence():

    messages = [
        "Loading Cypher Core...",
        "Loading Command Handler...",
        "Loading Logger...",
        "Loading Tools...",
        "Loading Configuration..."
    ]

    for message in messages:
        print(Fore.GREEN + "[✓] " + message + Style.RESET_ALL)
        time.sleep(0.3)

    print("")

def main():

    startup_sequence()

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