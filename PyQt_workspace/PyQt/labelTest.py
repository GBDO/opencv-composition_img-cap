import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./PyQt_workspace/PyQt/labelTest.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btnChangeText.clicked.connect(self.changeTextFunction)
        self.btnPrintText.clicked.connect(self.printTextFunction)
    def changeTextFunction(self):
        self.label.setText("This is Label - Change Text")
    def printTextFunction(self):
        print(self.label.text())
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()