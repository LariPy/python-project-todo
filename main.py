
### ---------------------------- ### IMPORTS ### ------ ###
import sys
import json
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QLineEdit, QPushButton
)



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """### Load Tasks ###"""
        # load tasks here using load method from methods
        # tasks list

        """### Window Settings ###"""
        self.setWindowTitle("Todos")
        self.resize(560, 560)

        """### Contents/Layout ###"""

        ### Layout
        top = QHBoxLayout()
        mid = QHBoxLayout()
        footer = QHBoxLayout()

        ### Layout Content
        # top content
        task_input = QLineEdit(placeholderText="Input task")
        top.addWidget(task_input)
        btn_add_task = QPushButton("Add task")
        top.addWidget(btn_add_task)

        # mid content, list
        mid_list = QListWidget()
        mid.addWidget(mid_list)

        # TODO may need to use "self" for mid_list, somewhere
            # so that data can be passed
        # TODO list test content
        for i in range(10):
            mid_list.addItem(f'test item {i}')
        # TODO list items
            # object?
            # editable text
            # checkmark
            # delete button?

        # footer content
        footer_button = QPushButton("foot")
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
    # make sure methods are not inside __init__
    # load tasks
        # runs when app is opened
        # loads tasks.json into a list
        # check if file exists, returns read list
        # if file does not exist, returns empty list

    # save tasks
        # writes tasks list into tasks.json
        # is called when tasks list has changes

    # add task
        # runs when input field has text AND add task button is clicked
        # creates a dict, "text" = text from input field, "done" = False
        # adds created "task" to tasks list
        # runs "save tasks" to write updated list to tasks.json

    # edit task (???)
        # runs when ???
        # how to figure out which item in a list is "selected" ???
        # change "text" in the selected item from the list
        # run "save tasks"

    # delete
        # runs when "delete" button is clicked
        # removes selected task from the tasks list
        # runs "save tasks" to update tasks.json

    # clear completed
        # runs when "clear" button is clicked
        # removes all tasks with "done" = True from tasks list
        # runs "save tasks" to update tasks.json



### ---------------------------- ### MAIN ### ------ ###
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Basic GUI")
    # data_dir = Path()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



### ---------------------------- ### TEST ### ------ ###
if __name__=="__main__":
    main()



### ---------------------------- ### NOTES ### ------ ###
