
### ---------------------------- ### IMPORTS ### ------ ###
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
)



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ### Window Settings ###
        self.setWindowTitle("Todos")
        self.resize(840, 560)

        ### Contents/Layout ###

        # Layout Content

        # Layout
        top = QHBoxLayout()
        mid = QHBoxLayout()
        footer = QHBoxLayout()

        # Add Content to Layout

        # Root, Container
        root = QVBoxLayout()
        root.addWidget(top)
        root.addWidget(mid)
        root.addWidget(footer)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        ### Methods ###
        # add
        # delete
        # update_count

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
