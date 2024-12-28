from generated.mainWindow import Ui_MainWindow
from configParser import parse

class MainWindowWrapper (Ui_MainWindow):

    def setupUi(self, main_window):
        super().setupUi(main_window)
        lines = parse()
        
