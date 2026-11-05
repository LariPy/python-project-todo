
"""
Task Store
- holds the task list
- handles operations
"""

### ---------------------------- ### IMPORTS ### ------ ###

import json
from pathlib import Path

### ---------------------------- ### CLASS ### ------ ###

class TaskStore:
    def __init__(self, file_path: Path):
        self._FILE = file_path
        self._tasks = self.load_tasks()

    ### Persistence ###

    # load tasks
    def load_tasks(self):
        if self._FILE.exists():
            return json.loads(self._FILE.read_text(encoding="utf-8"))
        return []

    # save tasks
        # writes tasks list into tasks.json
        # call when tasks list has changes
    def save_tasks(self):
        self._FILE.write_text(json.dumps(self._tasks, indent=2), encoding="utf-8")

    # add task
    # gets text
    # creates dict out of text, appends to tasks list
    # writes updated list to json database
    def add(self, text):
        self._tasks.append({"text": text, "done": False})
        self.save_tasks()