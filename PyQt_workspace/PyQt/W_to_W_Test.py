import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('./PyQt_workspace/PyQt/pushbuttonTest2.ui')[0]
when_clicked_class = uic.loadUiType('./PyQt_workspace/PyQt/react_clicked.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.Button1.clicked.connect(self.button1Function)
        self.Button2.clicked.connect(self.button2Function)
        #
    def button1Function(self):
        print("button1 Clicked")
        react = ReactClass()
        react.show()
        
    def button2Function(self):
        print("button2 Clicked")

class ReactClass(QMainWindow,when_clicked_class):
    def __init__(self):
        super().__init__()
    
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()