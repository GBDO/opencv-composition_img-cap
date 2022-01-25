import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signaly = pyqtSignal(int, int)
    def run(self):
        print('보낼 숫자를 공백없이 입력하세요')
        self.signaly.emit(int(input()),int(input()))
    
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mysignal = MySignal()
        mysignal.signaly.connect(self.signaly_emitted)
        mysignal.run()
    
    @pyqtSlot(int,int)
    def signaly_emitted(self,arg1,arg2):
        print('signaly emitted {}, {}'.format(arg1,arg2))
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()