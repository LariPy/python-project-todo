
### ---------------------------- ### IMPORTS ### ------ ###
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListView
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

        ### Components ###
        # model
        # filter

        ### Layout Contents ###
        # things like buttons, lists
        # input row, "add" button
        # tasks list
        # filter buttons
        # footer

        ### Layout ###
        # things used:
            # QWidget
            # QHBoxLayout
            # QVBoxLayout
        # content
        # layout
        # add content to layout

        # root layout
        # container widget
        # add root layout to container
        # set container as central widget

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
