
### ---------------------------- ### IMPORTS ### ------ ###
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow
)



### ---------------------------- ### MAIN WINDOW ### ------ ###
# main window class to be used as window in main()
# contains initial settings
# contains methods
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(420, 560)

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
"""
import sys, import pyside6 qtwidgets, QApplication, QMainwindow

make class MainWindow subclassing QMainwindow
MainWindow basically holds some initial data
for now resize to set size of window
holds other stuff later

main() declares app, declares window, shows window
has some sys stuff to handle sys stuff, such as exit
"""