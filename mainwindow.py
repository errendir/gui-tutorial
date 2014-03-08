from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow, QIcon, QPushButton, QGridLayout, QWidget, QSizePolicy

from PyQt4.QtCore import qDebug, QSize

class MyWindow(QMainWindow):

    def __init__(self):
        # Initialize the super-class
        QMainWindow.__init__(self)

        # Set the icon
        self.setWindowIcon(QIcon("logo3.svg"))

        desktop = QtGui.QDesktopWidget()
        geom = desktop.availableGeometry()

        windowWidth = int(geom.width()/1.5)
        windowHeight = int(geom.height()/1.5)
        self.wh = QSize(windowWidth, windowHeight)

        # Restrict the resizing
        self.setMinimumSize(self.wh * 0.7)
        self.setSizeIncrement(QSize(30,30))

        # Resize and move to the middle of the screen
        self.resize(self.wh)
        self.move(int((geom.width()-windowWidth)/2.0), int((geom.height()-windowHeight)/2.0))
        self.setWindowTitle('The windowed application!')

        # Create the main widget of the window
        self.center = QWidget()
        self.layout().addWidget(self.center)

        # Create a grid layout to fit elements into
        self.center.setLayout(QGridLayout())

        # Add a button
        self.button = QPushButton(self)
        self.button.setText("This is a magic button!");
        self.button.resize(self.button.sizeHint());
        self.button.setFixedSize(self.button.sizeHint());

        self.center.layout().addWidget(self.button, 0, 1)

        self.button.clicked.connect(self.reaction)

        qDebug(str(self.sizeHint()))

    def sizeHint(self):
        return self.wh

    def reaction(self):
        qDebug("Button was clicked!")

    def closeEvent(self, event):
        # Call the method of the parent as well
        QMainWindow.closeEvent(self, event)

    def resizeEvent(self, event):
        # Resize the main widget
        self.center.resize(event.size())

        QMainWindow.resizeEvent(self, event)

    def moveEvent(self, event):
        #qDebug("Window moved!")
        print (event.pos().x(), event.pos().y())
        QMainWindow.moveEvent(self, event)