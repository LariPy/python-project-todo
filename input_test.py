
### ---------------------------- ### IMPORTS ### ------ ###
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
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

        # Layouts
        # top Layout
        top = QHBoxLayout()

        # bottom Layout
        bottom = QHBoxLayout()

        # Root, Container
        root = QVBoxLayout()
        root.addLayout(top)
        root.addLayout(bottom)
        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)

        # Contents
        # top content
        self.input = QLineEdit(placeholderText="Write something")
        self.input.returnPressed.connect(self.say_hello)
        button = QPushButton("Click me")
        button.clicked.connect(self.say_hello)
        top.addWidget(self.input)
        top.addWidget(button)

        # bottom content
        self.bottom_item = QLabel("Bottom Text")
        bottom.addWidget(self.bottom_item)



    ### Methods ###
    def say_hello(self):
        self.bottom_item.setText(self.input.text())

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
