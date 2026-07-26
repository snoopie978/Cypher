from datetime import datetime


def log(message, event="INFO"):
    time_logged = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{time_logged}] [{event}] {message}\n"

    with open("logs/cypher.log", "a") as file:
        file.write(log_entry)