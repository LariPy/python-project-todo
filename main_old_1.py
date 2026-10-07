import os
import sys
from PySide6 import QtWidgets, QtCore, QtGui



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        ### Settings ###
        # settings of the application

        # window title, size
        self.setWindowTitle('TODO App')
        self.resize(800, 600)

        # icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/testicon.png"))
        self.setWindowIcon(icon) # window icon
        # TODO taskbar icon (complicated)



        ### Content ###
        # content that is added to the widgets later

        # test content cards
        self.card_1 = QtWidgets.QFrame()
        self.card_1.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.card_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.card_1.setStyleSheet("background-color: gray; border-radius: 4px;")
        self.card_1.setFixedSize(400, 200)

        self.card_2 = QtWidgets.QFrame()
        self.card_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.card_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.card_2.setStyleSheet("background-color: gray; border-radius: 4px;")
        self.card_2.setFixedSize(400, 200)

        self.card_3 = QtWidgets.QFrame()
        self.card_3.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.card_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.card_3.setStyleSheet("background-color: gray; border-radius: 4px;")
        self.card_3.setFixedSize(400, 200)

        # Sidebar List Widget (contains sidebar buttons/items)
        self.sidebar_list_widget = QtWidgets.QListWidget()
        self.sidebar_list_widget.addItem('test 1')
        self.sidebar_list_widget.addItem('test 2')
        self.sidebar_list_widget.addItem('test 3')



        ### Widgets, Layout ###
        # Central Widget, Main Layout
        self.main_layout = QtWidgets.QSplitter(self) # create main layout
        self.setCentralWidget(self.main_layout) # set main layout as central widget

        # Main Content Widget
        self.main_content_widget = QtWidgets.QWidget()
        self.main_content_layout = QtWidgets.QVBoxLayout(self.main_content_widget)

        # Sidebar Widget
        self.sidebar_widget = QtWidgets.QWidget()
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)

        # Scroll
        self.main_content_scroll = QtWidgets.QScrollArea()
        self.main_content_scroll.setWidget(self.main_content_widget)
        self.main_content_scroll.setWidgetResizable(True)



        ### Add Widgets/Content ###

        # add main content and sidebar
        self.main_layout.addWidget(self.sidebar_widget)
        self.main_layout.addWidget(self.main_content_scroll)
        # TODO right now main content is added through main_content_scroll, is this ok??
        # or is it??

        # add widgets to main content
        for card in [self.card_1, self.card_2, self.card_3]:
            self.main_content_layout.addWidget(card, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        # add widgets to sidebar
        self.sidebar_layout.addWidget(self.sidebar_list_widget)



        ### Main Layout settings ###

        self.main_content_layout.addStretch()

        # Sidebar and Main Content size
        self.main_layout.setSizes([200, 600])
        self.main_layout.setStretchFactor(0, 0)  # sidebar (index 0) doesn't grow
        self.main_layout.setStretchFactor(1, 1)  # main content (index 1) takes extra space



if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()

    sys.exit(app.exec())