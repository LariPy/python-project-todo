
### ---------------------------- ### IMPORTS ### ------ ###
import sys
import json
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QLineEdit, QPushButton
    )

from PySide6.QtCore import (
    Qt, QStandardPaths, QUrl
    )

from PySide6.QtGui import QDesktopServices



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """### Init: File Location, Load Tasks ###"""
        data_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation))
        data_dir.mkdir(parents=True, exist_ok=True)
        self._FILE = data_dir / "tasks.json"
        self._tasks = self.load_tasks()

        """### Init: Window Settings ###"""
        self.setWindowTitle("Todos")
        self.resize(560, 560)

        """### Init: Menu Bar ###"""
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction("Open Data Folder", self.open_data_folder)

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
        self.task_list_view.setSelectionMode(QListWidget.ExtendedSelection)
        mid.addWidget(self.task_list_view)
        # refresh view on launch, item changed signal
        self.refresh_task_list_view()
        self.task_list_view.itemChanged.connect(self.on_item_changed)

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

    # refresh task list view
    def refresh_task_list_view(self):
        self.task_list_view.clear()
        for task in self._tasks:
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable)
            item.setCheckState(Qt.CheckState.Checked if task["done"] else Qt.CheckState.Unchecked)
            self.task_list_view.addItem(item)

    # add task
    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            return
        test_item = {"text": text, "done": False}
        self._tasks.append(test_item)
        self.save_tasks()
        self.refresh_task_list_view()
        self.task_input.clear()

    # delete item
    def delete_item(self):
        # get selected item index, do nothing of nothing is selected
        selected_row = self.task_list_view.currentRow()
        if selected_row == -1:
            return
        # pop selected item, save change and refresh
        self._tasks.pop(selected_row)
        self.save_tasks()
        self.refresh_task_list_view()

    # clear completed
    def clear_completed(self):
        new_list = []
        for task in self._tasks:
            if task["done"] == False:
                new_list.append(task)
        self._tasks = new_list
        self.save_tasks()
        self.refresh_task_list_view()

    # clear list
    def clear_list(self):
        self.task_list_view.clear()
        self._tasks = []
        self.save_tasks()
        self.refresh_task_list_view()

    # on item changed
        # when an item on the list is changed
        # handles text edit
        # handles checkmark
    def on_item_changed(self, item):
        selected_row = self.task_list_view.row(item)
        self._tasks[selected_row]["text"] = item.text()
        self._tasks[selected_row]["done"] = item.checkState() == Qt.CheckState.Checked
        self.save_tasks()

    # open data folder
    def open_data_folder(self):
        path = QUrl.fromLocalFile(str(self._FILE.resolve().parent))
        QDesktopServices.openUrl(path)



### ---------------------------- ### MAIN ### ------ ###
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Todo App")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



### ---------------------------- ### TEST ### ------ ###
if __name__=="__main__":
    main()