from PyQt6 import QtWidgets
import sys
from wrappers.mainWindowWrapper import MainWindowWrapper

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowWrapper()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
