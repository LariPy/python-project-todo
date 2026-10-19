
### ---------------------------- ### IMPORTS ### ------ ###
import sys
import json
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QLineEdit, QPushButton
    )

from PySide6.QtCore import (
    Qt
    )



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """### Init: File Location, Load Tasks ###"""
        self._FILE = Path("tasks.json")
        self._tasks = self.load_tasks()

        """### Init: Window Settings ###"""
        self.setWindowTitle("Todos")
        self.resize(560, 560)

        """### Init: Contents/Layout ###"""
        ### Layout
        top = QHBoxLayout()
        mid = QHBoxLayout()
        footer = QHBoxLayout()

        ### Layout Content
        # top content
        self.task_input = QLineEdit(placeholderText="Input task")
        self.task_input.returnPressed.connect(self.add_task)
        top.addWidget(self.task_input)
        btn_add_task = QPushButton("Add task")
        btn_add_task.clicked.connect(self.add_task)
        top.addWidget(btn_add_task)

        # mid content, task list view
        self.task_list_view = QListWidget()
        mid.addWidget(self.task_list_view)
        self.refresh_task_list_view()
        
        # TODO list items
            # object?
            # editable text
            # checkmark
            # delete button?

        # footer content
        footer_button = QPushButton("Clear List")
        footer_button.clicked.connect(self.clear_list)
        footer.addWidget(footer_button)
        # TODO
            # clear list
            # where is data?
            # need to refresh list when things are deleted?

        # Root, Container
        root = QVBoxLayout()
        root.addLayout(top)
        root.addLayout(mid)
        root.addLayout(footer)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

    """### Methods ###"""
    # load tasks
    def load_tasks(self):
        if self._FILE.exists():
            return json.loads(self._FILE.read_text(encoding="utf-8"))
        return []

    # TODO methods below
    # save tasks
        # writes tasks list into tasks.json
        # is called when tasks list has changes
    def save_tasks(self):
        self._FILE.write_text(json.dumps(self._tasks, indent=2), encoding="utf-8")

    # refresh task list view
        # any time a change is made to tasks, update tasks list (view)
        # for loop, add stuff to tasks list with tasks_list.addItem()
        # TODO: "done" status is not kept 
    def refresh_task_list_view(self):
        self.task_list_view.clear()
        for task in self._tasks:
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked if task["done"] else Qt.CheckState.Unchecked)
            self.task_list_view.addItem(item)

    # add task
    def add_task(self):
        test_item = {"text": self.task_input.text(), "done": False}
        self._tasks.append(test_item)
        self.save_tasks()
        self.refresh_task_list_view()
        self.task_input.clear()

    # edit task (???)
        # runs when ???
        # how to figure out which item in a list is "selected" ???
        # change "text" in the selected item from the list
        # run "save tasks"

    # delete
        # (not sure if this is necessary if clear completed is used instead)
        # runs when "delete" button is clicked
        # removes selected task from the tasks list
        # self.save_tasks()
        # self.refresh_task_list_view()

    # checkmark check
        # if checkmark is clicked, it does not show on tasks.json
        # it's not saved...
        # could it still work with clear completed method?

    # clear completed
        # for task in tasks
            # if done == false
                # tasks append new_task_list
        # save tasks
        # refresh view

    # clear list button method (change to clear completed later?)
    def clear_list(self):
        self.task_list_view.clear()
        self._tasks = []
        self.save_tasks()
        self.refresh_task_list_view()



### ---------------------------- ### MAIN ### ------ ###
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TODO")
    # data_dir = Path()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



### ---------------------------- ### TEST ### ------ ###
if __name__=="__main__":
    main()



### ---------------------------- ### NOTES ### ------ ###
