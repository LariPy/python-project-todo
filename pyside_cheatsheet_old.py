import sys
from PySide6 import QtWidgets, QtCore, QtGui



# Main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Size
        self.resize(800,600)
        # self.setMinimumSize(QtCore.QSize(600, 400))
        # self.setMaximumSize(QtCore.QSize(800, 600))

        # Window Title
        self.setWindowTitle('Application title')
        
        # Window Settings
        # self.setWindowOpacity(0.5)
        # self.setStyleSheet("background-color: lightgreen")

        # Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/testicon.png"))
        self.setWindowIcon(icon)

        # Label
        self.label = QtWidgets.QLabel("This is label", self)
        self.label.setVisible(False)
        # self.label.setObjectName("label name")
        # print(self.label.objectName())

        # Label Frame
        # self.label.setGeometry(400, 100, 600, 200)
        self.label.setGeometry(QtCore.QRect(400, 100, 300, 200))
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        # self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        # Label Style
        self.label.setStyleSheet("background-color: lightblue;" "color: green") # background, font
        self.label.setAlignment(QtCore.Qt.AlignCenter) # aligns text

        # Label Font
        font = QtGui.QFont() # first set a font variable
        font.setPointSize(36) # takes integer value
        # font.setPointSizeF(36.5) # takes float value
        # font.setBold(True)
        # font.setWeight(QtGui.QFont.Weight.DemiBold)
        # also works for weight: bold, demibold, light
        # font.setItalic(True)
        # font.setUnderline(True)
        # font.setOverline(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        # Label Icon
        self.label.setPixmap(QtGui.QPixmap("./icons/testicon.png"))
        self.label.setScaledContents(True)
        # makes icon fit the frame of the label, stretches icon if it's smaller than frame



        # Layouts

        # a widget should only have one main layout
        # main widget (parent self), main layout (parent main widget)
        self.main_widget = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)

        # Widgets
        self.label_1 = QtWidgets.QLabel("label_1", self.main_widget)
        self.label_2 = QtWidgets.QLabel("label_2", self.main_widget)
        self.label_3 = QtWidgets.QLabel("label_3", self.main_widget)
        self.label_4 = QtWidgets.QLabel("label_4", self.main_widget)

        # self.frame_1 = QtWidgets.QFrame(self.main_widget)

        # Widget styles
        # Label 1
        self.label_1.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_1.setStyleSheet("background-color: red")

        # Label 2
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_2.setStyleSheet("background-color: yellow")

        # Label 3
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_3.setStyleSheet("background-color: blue")

        # Label 4
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_4.setStyleSheet("background-color: green")

        # Horizontal layout, add widgets
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.label_1)
        self.horizontal_layout.addWidget(self.label_2)
        
        # Vertical layout, add widgets
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.addWidget(self.label_3)
        self.vertical_layout.addWidget(self.label_4)

        # add layouts to main layout
        self.main_layout.addLayout(self.horizontal_layout)
        self.main_layout.addLayout(self.vertical_layout)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("My App")
    app.setApplicationVersion("1.0")
    app.setApplicationDisplayName(f"{app.applicationName()} - {app.applicationVersion()}")
    ui = MainWindow()
    ui.show()
    
    sys.exit(app.exec())



# graveyard

    #     self.center()

    # TODO is this necessary?
    # def center(self):
    #     frame = self.frameGeometry()
    #     screen_center = self.screen().availableGeometry().center()
    #     frame.moveCenter(screen_center)
    #     self.move(frame.topLeft())