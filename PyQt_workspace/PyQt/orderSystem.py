import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType('./PyQt_workspace/PyQt/menu1.ui')[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.order)
        
    def order(self):
        Alst = []
        Blst = []
        if self.chkBox_A0.isChecked() : 
            Alst.append(self.chkBox_A0.text())
        if self.chkBox_A1.isChecked() : 
            Alst.append(self.chkBox_A1.text())
        if self.chkBox_B0.isChecked() : 
            Blst.append(self.chkBox_B0.text())
        if self.chkBox_B1.isChecked() : 
            Blst.append(self.chkBox_B1.text())
        if self.chkBox_B2.isChecked() : 
            Blst.append(self.chkBox_B2.text())

        print('식사 :',Alst,'\n요리:',Blst,'\n를 주문합니다.')
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()