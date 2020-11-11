import sys
from PyQt5 import uic, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("xxxxxxx.ui",self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

