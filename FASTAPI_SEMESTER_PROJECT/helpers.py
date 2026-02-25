import json
import os
from datetime import datetime

FILE_PATH = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    tasks = []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks

def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")