#filename = PyQt_MQTT_0.py
from email import message
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import paho.mqtt.client as mqtt
from PyQt5 import uic

form_class = uic.loadUiType('./PyQt_workspace/PyQt/PyQt_MQTT1.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn_Connect.clicked.connect(self.slot_connect)
        self.btn_Sub.clicked.connect(self.slot_sub)
        self.btn_Pub.clicked.connect(self.slot_pub)
        self.btn_Disconnect.clicked.connect(self.slot_disconnect)
        self.btn_Send.clicked.connect(self.slot_send)
        
        self.client = mqtt.Client()
        #self.client.username_pw_set(username='mqtt_GBD', password='1234')
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
    
    def on_connect(self,client, userdata, flags, rc):
        self.textBrowser.append('Connected with result code : ' + str(rc))
           
    def on_message(self,client, userdata, msg):
        message = str(msg.payload, 'utf-8')
        self.textBrowser.append('Topic : '+msg.topic +', Message : '+message)

    def slot_connect(self):
        self.client.connect('broker.emqx.io',1883, 60)
        self.textBrowser.append('Connected')
        
    def slot_sub(self):
        self.client.subscribe('phirippa') #구독할 Topic명: phirippa
        self.client.loop_start()
        
    def slot_pub(self):
        self.client.publish('phirippa', payload='good')
        
    def slot_disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.textBrowser.append('Disconnected')
#엔터 누를 경우 메시지 보내기 버튼 작동 기능   
    # def spacebar_event(self):
    #     if window.event.keyCode == 13 :
    #         self.slot_send(self)
    
    def slot_send(self):
        text=self.textEdit.toPlainText()
        self.client.publish('phirippa',text)
        self.textEdit.clear()
        
if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

#가상 머신에서 Pub.
#   -$ mosquitto_pub -t phirippa -m hi~ -h broker.emqx.io