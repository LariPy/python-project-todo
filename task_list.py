# class task list
# init empty list
# way to add tasks to list
# show number of tasks
# show tasks
# clear tasks

import json
from pathlib import Path

FILE = Path("tasks.json")

# define function, load_tasks
# check if FILE exists()
    # if exists, return 

def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")

tasks = load_tasks()          # read once at startup

def add_task(text):
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)         # write after the change

add_task("Buy milk")
add_task("Write report")



### write data to json ###



### read data from json ###
# with open("tasks.json", "r", encoding="utf-8") as f:
#     tasks = json.load(f)

# for task in tasks:
#     print(task["text"])
#     print(task["done"])