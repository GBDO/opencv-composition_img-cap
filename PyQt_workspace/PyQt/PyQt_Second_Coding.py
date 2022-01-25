import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        #'원도우'의 타이틀 지정(set)
        self.setWindowTitle('Welcom to PyQt World!')
        #'윈도우'의 위치 및 크기 setGeometry(x,y,width,height)
        self.setGeometry(770,350,480,100)
        
        hello_label = QLabel(self)
        hello_label.setText('Hello World!')
        hello_label.move(200,40)
        
        button = QPushButton(self)
        button.setText('OK')
        button.move(200,60)
if __name__=='__main__':      
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()