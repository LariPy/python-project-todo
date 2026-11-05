
"""
Main Window
- handles UI
- needs task_store for handling operations between UI and data
"""

### ---------------------------- ### IMPORTS ### ------ ###

from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QLineEdit, QPushButton
    )

from PySide6.QtCore import (
    Qt, QStandardPaths, QUrl
    )

from PySide6.QtGui import QDesktopServices

from task_store import TaskStore



### ---------------------------- ### CLASS ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """### Init: File Location, Load Tasks ###"""
        data_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation))
        data_dir.mkdir(parents=True, exist_ok=True)
        self.store = TaskStore(data_dir / "tasks.json")

        """### Init: Window Settings ###"""
        self.setWindowTitle("Todos")
        self.resize(560, 560)

        """### Init: Menu Bar ###"""
        # Menu Bar - Help Menu
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction("Open Data Folder", self.open_data_folder)
        help_menu.addAction("Toggle Light/Dark Mode", self.toggle_theme)
        # Menu Bar - Sort Menu
        sort_menu = self.menuBar().addMenu("Sort")
        sort_menu.addAction("By Completion (Ascending)", self.sort_completion_ascending)
        sort_menu.addAction("By Completion (Descending)", self.sort_completion_descending)

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

        # mid content
        # task list view
        self.task_list_view = QListWidget()
        self.task_list_view.setSelectionMode(QListWidget.ExtendedSelection) # allow selection of items
        self.task_list_view.setDragDropMode(QListWidget.InternalMove) # allow dragging of items
        mid.addWidget(self.task_list_view)
        # refresh view on launch, item changed signal
        self.refresh_task_list_view()
        self.task_list_view.itemChanged.connect(self.on_item_changed)
        self.task_list_view.model().rowsMoved.connect(self.sync_tasks_from_list) # emit signal for handler

        # footer content
        delete_item_btn = QPushButton("Delete Item")
        delete_item_btn.clicked.connect(self.delete_item)
        clear_list_btn = QPushButton("Clear List")
        clear_list_btn.clicked.connect(self.clear_list)
        clear_completed_btn = QPushButton("Clear Completed")
        clear_completed_btn.clicked.connect(self.clear_completed)
        footer.addWidget(delete_item_btn)
        footer.addWidget(clear_list_btn)
        footer.addWidget(clear_completed_btn)

        # Root, Container
        root = QVBoxLayout()
        root.addLayout(top)
        root.addLayout(mid)
        root.addLayout(footer)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

    """### Methods ###"""

    # refresh task list view
    # creates widget items for the task list using data from tasks.json
    def refresh_task_list_view(self):
        self.task_list_view.clear()
        for task in self.store._tasks:
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable)
            item.setCheckState(Qt.CheckState.Checked if task["done"] else Qt.CheckState.Unchecked)
            self.task_list_view.addItem(item)

    ### Buttons ###

    # add task
    def add_task(self):
        text = self.task_input.text().strip()   # gets text from UI: Input
        if not text:
            return
        self.store.add(text)                    # hands text to task_store (data packaged, database updated)
        self.refresh_task_list_view()           # refresh UI
        self.task_input.clear()                 # clear input UI

    # delete item
    def delete_item(self):
        # get selected item index, do nothing of nothing is selected
        selected_row = self.task_list_view.currentRow()
        if selected_row == -1:
            return
        # pop selected item, save change and refresh
        self.store._tasks.pop(selected_row)
        self.store.save_tasks()
        self.refresh_task_list_view()

    # clear completed
    def clear_completed(self):
        new_list = []
        for task in self.store._tasks:
            if task["done"] == False:
                new_list.append(task)
        self.store._tasks = new_list
        self.store.save_tasks()
        self.refresh_task_list_view()

    # clear list
    def clear_list(self):
        self.task_list_view.clear()
        self.store._tasks = []
        self.store.save_tasks()
        self.refresh_task_list_view()

    ### Menu Bar Methods ###

    ### Help menu

    # open data folder
    def open_data_folder(self):
        path = QUrl.fromLocalFile(str(self._FILE.resolve().parent))
        QDesktopServices.openUrl(path)

    # light/dark mode
    def toggle_theme(self):
        hints = QApplication.styleHints()
        if hints.colorScheme() == Qt.ColorScheme.Dark:
            hints.setColorScheme(Qt.ColorScheme.Light)
        else:
            hints.setColorScheme(Qt.ColorScheme.Dark)

    ### Sort menu

    # sort by completion ascending
    def sort_completion_ascending(self):
        new_list = []
        tasks_copy = self.store._tasks.copy()
        
        # first add completed to new list
        for item in tasks_copy:
            if item['done']:
                new_list.append(item)
        # then add not completed to new list
        for item in tasks_copy:
            if item['done'] == False:
                new_list.append(item)

        # save changes
        self.store._tasks = new_list
        self.store.save_tasks()
        self.refresh_task_list_view()

    # sort by completion descending
    def sort_completion_descending(self):
        new_list = []
        tasks_copy = self.store._tasks.copy()
        
        # first add not completed to new list
        for item in tasks_copy:
            if item['done'] == False:
                new_list.append(item)
        # then add completed to new list
        for item in tasks_copy:
            if item['done']:
                new_list.append(item)
        
        # save changes
        self.store._tasks = new_list
        self.store.save_tasks()
        self.refresh_task_list_view()

    ### Event Handling: Handler methods ###

    # on item changed
        # when an item on the list is changed
        # handles text edit
        # handles checkmark
    def on_item_changed(self, item):
        selected_row = self.task_list_view.row(item)
        self.store._tasks[selected_row]["text"] = item.text()
        self.store._tasks[selected_row]["done"] = item.checkState() == Qt.CheckState.Checked
        self.store.save_tasks()

    # drag and drop sync handler
    def sync_tasks_from_list(self):
        new_list = []
        for index in range(self.task_list_view.count()):
            item = self.task_list_view.item(index)
            text = item.text()
            done = item.checkState() == Qt.CheckState.Checked
            new_list.append({"text": text, "done": done})
        self.store._tasks = new_list
        self.store.save_tasks()