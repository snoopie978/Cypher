import psutil
import platform
import sys


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
    percent = memory.percent

    return f"RAM: {used}GB / {total}GB ({percent}%)"


def get_storage():
    storage = psutil.disk_usage("/")

    total = round(storage.total / (1024 ** 3), 2)
    used = round(storage.used / (1024 ** 3), 2)
    percent = storage.percent

    return f"Storage: {used}GB / {total}GB ({percent}%)"


def get_python():
    version = sys.version.split()[0]

    return f"Python Version: {version}"


def system():
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