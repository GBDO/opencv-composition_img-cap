import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signalx = pyqtSignal()
    def run(self):
        self.signalx.emit()
    
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mysignal = MySignal()
        mysignal.signalx.connect(self.signalx_emitted)
        mysignal.run()
    
    @pyqtSlot()
    def signalx_emitted(self):
        print('signalx emitted')
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()