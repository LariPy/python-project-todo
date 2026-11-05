
"""
App architecture
- main.py
    - main_window.py
        - task_store.py
"""

### ---------------------------- ### IMPORTS ### ------ ###
import sys
from PySide6.QtWidgets import (
    QApplication
    )
from PySide6.QtCore import (
    Qt
    )
import main_window



### ---------------------------- ### MAIN ### ------ ###
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Todo App")
    app.styleHints().setColorScheme(Qt.ColorScheme.Dark)
    window = main_window.MainWindow()
    window.show()
    sys.exit(app.exec())



### ---------------------------- ### TEST ### ------ ###
if __name__=="__main__":
    main()