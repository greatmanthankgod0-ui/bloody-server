from fastapi import BackgroundTasks

def log_registration(username: str):
    with open("logs/server.log", "a") as f:
        f.write(f"New user registered: {username}\n")
