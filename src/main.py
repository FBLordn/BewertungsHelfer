import sys
from wrappers.mainWindowWrapper import MainWindowWrapper
from PyQt5 import QtWidgets 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowWrapper()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
