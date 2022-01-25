import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType('./PyQt_workspace/PyQt/checkboxTest.ui')[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chkBox_A0.stateChanged.connect(self.chkFunction)
        self.chkBox_A1.stateChanged.connect(self.chkFunction)
        self.chkBox_B0.stateChanged.connect(self.groupchkFunction)
        self.chkBox_B1.stateChanged.connect(self.groupchkFunction)
        self.chkBox_B2.stateChanged.connect(self.groupchkFunction)
        
    def chkFunction(self):
        if self.chkBox_A0.isChecked() : 
            print(self.chkBox_A0.text())
        if self.chkBox_A1.isChecked() : 
            print(self.chkBox_A1.text())
        
    def groupchkFunction(self):
        if self.chkBox_B0.isChecked() : 
            print(self.chkBox_B0.text())
        if self.chkBox_B1.isChecked() : 
            print(self.chkBox_B1.text())
        if self.chkBox_B2.isChecked() : 
            print(self.chkBox_B2.text())

if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()