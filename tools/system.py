import psutil
import platform
import sys

tool_name = "system"


def get_os():
    os_info = platform.system()
    version = platform.version()
    return f"OS: {os_info} {version}"


def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count()
    return f"CPU Usage: {cpu_usage}%\nCPU Cores: {cpu_cores}"


def get_memory():
    memory = psutil.virtual_memory()

    total = round(memory.total / (1024 ** 3), 2)
    used = round(memory.used / (1024 ** 3), 2)

    return f"RAM: {used}GB / {total}GB ({memory.percent}%)"


def get_storage():
    storage = psutil.disk_usage("/")

    total = round(storage.total / (1024 ** 3), 2)
    used = round(storage.used / (1024 ** 3), 2)

    return f"Storage: {used}GB / {total}GB ({storage.percent}%)"


def get_python():
    return f"Python Version: {sys.version.split()[0]}"


def run():

    print("")
    print("====================================")
    print("        SYSTEM INFORMATION")
    print("====================================")

    print("")
    print(get_os())

    print("")
    print(get_cpu())

    print("")
    print(get_memory())

    print("")
    print(get_storage())

    print("")
    print(get_python())

    print("")
    print("====================================")