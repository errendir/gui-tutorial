import sys
from PyQt4 import QtGui

from mainwindow import MyWindow

def main():

    app = QtGui.QApplication(sys.argv)

    w = MyWindow()
    w.show()

    scene = QtGui.QGraphicsScene(w)
    path = QtGui.QGraphicsPathItem(None, scene)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
