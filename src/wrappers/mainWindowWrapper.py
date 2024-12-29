from generated.mainWindow import Ui_MainWindow
from configParser import parse
from PyQt5 import QtWidgets

class ConfigLine:
    def __init__(self, dropDownOptions:QtWidgets.QComboBox, label: QtWidgets.QHBoxLayout):
        self.options = dropDownOptions
        self.label = label

class MainWindowWrapper (Ui_MainWindow):

    def set_name(self, name: str):
        for i in range(0, len(self.config_lines)):
            self.config_lines[i].label.setText(format_assessment(self.config.lines[i], self.config_lines[i].options.currentText(), name)) 

    def save(self, button):
        file = self.config.file.replace("$N", self.nameInputBox.text().replace(" ", "_"))
        #TODO

    def setupUi(self, main_window):
        super().setupUi(main_window)
        self.config = parse()
        self.config_lines: list[ConfigLine] = []
        for i in range(0,len(self.config.lines)):
            self.add_line(i)
        self.nameInputBox.textChanged.connect(self.set_name)
        self.saveBox.clicked.connect(self.save)

    def add_line(self, counter):
        config_label = QtWidgets.QLabel(self.centralwidget)
 
        def set_assessment(text: str):
            config_label.setText(format_assessment(self.config.lines[counter], text, self.nameInputBox.text())) 

        config_line = QtWidgets.QHBoxLayout()
        config_line.setObjectName("configLine"+str(counter))
        config_label.setWordWrap(True)
        config_label.setObjectName("configLabel"+str(counter))
        config_label.setText(self.config.lines[counter])
        config_line.addWidget(config_label)
        vertical_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        config_line.addItem(vertical_spacer)
        horizontal_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        config_line.addItem(horizontal_spacer)
        config_dropdown = QtWidgets.QComboBox(self.centralwidget)
        config_dropdown.addItems(self.config.options)
        config_dropdown.setObjectName("configDropdown"+str(counter))
        config_dropdown.currentTextChanged.connect(set_assessment)
        config_line.addWidget(config_dropdown)
        self.config_lines.append(ConfigLine(config_dropdown, config_label))
        self.configContainer.addLayout(config_line)
        self.configContainer.setStretch(counter, 1)

def format_assessment(text:str, input:str, name:str)-> str:
    return text.replace("$B", input).replace("$N", name)

    
        
