"""A small todo app built with PySide6 using Qt's Model/View architecture.

Run:  pip install PySide6 && python todo_app.py
"""
import json
import sys
from pathlib import Path

from PySide6.QtCore import (
    QAbstractListModel, QModelIndex, QSortFilterProxyModel,
    QStandardPaths, Qt,
)
from PySide6.QtGui import QFont, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication, QButtonGroup, QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QVBoxLayout, QWidget,
)


# ---------------------------------------------------------------- model ----
class TodoModel(QAbstractListModel):
    """Holds the todos and persists them to a JSON file."""

    def __init__(self, path: Path):
        super().__init__()
        self._path = path
        self._todos: list[dict] = []
        self.load()

    # --- required overrides
    def rowCount(self, parent=QModelIndex()):
        return 0 if parent.isValid() else len(self._todos)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        todo = self._todos[index.row()]
        if role in (Qt.DisplayRole, Qt.EditRole):
            return todo["text"]
        if role == Qt.CheckStateRole:
            return Qt.Checked if todo["done"] else Qt.Unchecked
        if role == Qt.FontRole and todo["done"]:
            font = QFont()
            font.setStrikeOut(True)
            return font
        if role == Qt.ForegroundRole and todo["done"]:
            return QApplication.palette().placeholderText()
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        todo = self._todos[index.row()]
        if role == Qt.CheckStateRole:
            todo["done"] = Qt.CheckState(value) == Qt.Checked
        elif role == Qt.EditRole:
            text = str(value).strip()
            if not text:
                return False
            todo["text"] = text
        else:
            return False
        self.dataChanged.emit(index, index)
        self.save()
        return True

    def flags(self, index):
        return (Qt.ItemIsEnabled | Qt.ItemIsSelectable
                | Qt.ItemIsUserCheckable | Qt.ItemIsEditable)

    # --- our own API
    def add(self, text: str):
        text = text.strip()
        if not text:
            return
        row = len(self._todos)
        self.beginInsertRows(QModelIndex(), row, row)
        self._todos.append({"text": text, "done": False})
        self.endInsertRows()
        self.save()

    def remove_rows(self, rows: list[int]):
        for row in sorted(set(rows), reverse=True):  # bottom-up keeps indices valid
            self.beginRemoveRows(QModelIndex(), row, row)
            del self._todos[row]
            self.endRemoveRows()
        self.save()

    def clear_completed(self):
        self.remove_rows([i for i, t in enumerate(self._todos) if t["done"]])

    def counts(self) -> tuple[int, int]:
        done = sum(t["done"] for t in self._todos)
        return len(self._todos) - done, done

    # --- persistence
    def load(self):
        try:
            self._todos = json.loads(self._path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            self._todos = []

    def save(self):
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._path.write_text(json.dumps(self._todos, indent=2), encoding="utf-8")


class FilterProxy(QSortFilterProxyModel):
    """Shows All / Active / Done without touching the underlying data."""

    def __init__(self):
        super().__init__()
        self._mode = "all"

    def set_mode(self, mode: str):
        self._mode = mode
        self.invalidateFilter()

    def filterAcceptsRow(self, row, parent):
        if self._mode == "all":
            return True
        done = self.sourceModel().index(row, 0, parent).data(Qt.CheckStateRole) == Qt.Checked
        return done == (self._mode == "done")


# ----------------------------------------------------------------- view ----
class MainWindow(QMainWindow):
    def __init__(self, model: TodoModel):
        super().__init__()
        self.setWindowTitle("Todos")
        self.resize(420, 560)

        self.model = model
        self.proxy = FilterProxy()
        self.proxy.setSourceModel(model)

        # input row
        self.input = QLineEdit(placeholderText="What needs doing?")
        self.input.returnPressed.connect(self.add_todo)
        add_btn = QPushButton("Add")
        add_btn.clicked.connect(self.add_todo)
        top = QHBoxLayout()
        top.addWidget(self.input)
        top.addWidget(add_btn)

        # list
        self.list = QListView()
        self.list.setModel(self.proxy)
        self.list.setSelectionMode(QListView.ExtendedSelection)
        self.list.setSpacing(2)
        QShortcut(QKeySequence.Delete, self.list, activated=self.delete_selected)

        # filter buttons
        filters = QHBoxLayout()
        self.group = QButtonGroup(self)
        for label, mode in [("All", "all"), ("Active", "active"), ("Done", "done")]:
            b = QPushButton(label, checkable=True, checked=(mode == "all"))
            b.clicked.connect(lambda _=False, m=mode: self.proxy.set_mode(m))
            self.group.addButton(b)
            filters.addWidget(b)

        # footer
        self.count = QLabel()
        clear_btn = QPushButton("Clear completed")
        clear_btn.clicked.connect(model.clear_completed)
        footer = QHBoxLayout()
        footer.addWidget(self.count, 1)
        footer.addWidget(clear_btn)

        root = QVBoxLayout()
        root.addLayout(top)
        root.addWidget(self.list)
        root.addLayout(filters)
        root.addLayout(footer)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        for sig in (model.rowsInserted, model.rowsRemoved,
                    model.dataChanged, model.modelReset):
            sig.connect(self.update_count)
        self.update_count()

    def add_todo(self):
        self.model.add(self.input.text())
        self.input.clear()

    def delete_selected(self):
        rows = [self.proxy.mapToSource(i).row() for i in self.list.selectedIndexes()]
        self.model.remove_rows(rows)

    def update_count(self, *_):
        active, done = self.model.counts()
        self.count.setText(f"{active} active, {done} done")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PySideTodo")
    data_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation))
    window = MainWindow(TodoModel(data_dir / "todos.json"))
    window.show()
    sys.exit(app.exec())    


if __name__ == "__main__":
    main()