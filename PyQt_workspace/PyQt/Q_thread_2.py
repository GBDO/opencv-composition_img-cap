import time 
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
# QThread 클래스를 사용하려면 QtCore 모듈을 import 해야함
class Thread_A_Task(QThread):
    def __init__(self, parent): # parent는 WindowClass에서 잔달하는 self이다.(WindowClass의 인스턴스)
        super().__init__(parent) # parent를 사용하여 WindowClass 위젯을 제어할 수 있음
    def run(self):
        print('A 업무를 시작합니다')
        for i in range(0, 101, 10): 
            print('A 업무 진행률 {}%'.format(i)) 
            time.sleep(2)
        print('A 업무 종료')
              
class Thread_B_Task(QThread):
    def __init__(self, parent): # parent는 WindowClass에서 잔달하는 self이다.(WindowClass의 인스턴스)
        super().__init__(parent) # parent를 사용하여 WindowClass 위젯을 제어할 수 있음
    def run(self):
        print('B 업무를 시작합니다')
        for i in range(0, 101, 10): 
            print('B 업무 진행률 {}%'.format(i)) 
            time.sleep(2)
        print('B 업무 종료')
        
form_class = uic.loadUiType("./PyQt_workspace/PyQt/QThreadTest.ui")[0] 

class WindowClass(QMainWindow, form_class):
    def __init__(self) : 
        super().__init__() 
        self.setupUi(self) 
        self.btn_A_start.clicked.connect(self.slot_A_task)
        self.btn_B_start.clicked.connect(self.slot_B_task)
    def slot_A_task(self): 
        A_task = Thread_A_Task(self)
        A_task.start()
    def slot_B_task(self): 
        B_task = Thread_B_Task(self)
        B_task.start()
if __name__ == "__main__" : 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()