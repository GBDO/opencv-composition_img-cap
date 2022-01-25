import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./PyQt_workspace/PyQt/radiobuttonTest.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_1.clicked.connect(self.groupboxRadFunction)
        self.radioButton_2.clicked.connect(self.groupboxRadFunction)
        self.radioButton_3.clicked.connect(self.groupboxRadFunction)
        self.radioButton_4.clicked.connect(self.groupboxRadFunction)
        
    def groupboxRadFunction(self):
        if self.radioButton_1.isChecked():
            print(self.radioButton_1.text()+' Checked')
            QMessageBox.information(self,'notice', self.radioButton_1.text()+' 선택')
        elif self.radioButton_2.isChecked():
            print(self.radioButton_2.text()+' Checked')         
            QMessageBox.information(self,'notice', self.radioButton_2.text()+' 선택')
        elif self.radioButton_3.isChecked():
            print(self.radioButton_3.text()+' Checked')
            QMessageBox.information(self,'notice', self.radioButton_3.text()+' 선택')      
        elif self.radioButton_4.isChecked():
            print(self.radioButton_4.text()+' Checked')
            QMessageBox.information(self,'notice', self.radioButton_4.text()+' 선택')
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()        