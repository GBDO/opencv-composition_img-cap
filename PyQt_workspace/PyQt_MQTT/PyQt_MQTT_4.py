#filename = PyQt_MQTT_0.py

import paho.mqtt.client as mqtt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType('./PyQt_workspace/PyQt/PyQt_MQTT1.ui')[0]

class Th_Client(QThread):
    def __init__(self):
        super().__init__()
        self.client = mqtt.Client()
        #self.client.username_pw_set(username='mqtt_GBD', password='1234')
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.topic = 'temp'
    def on_connect(self, client, userdata, flags, rc):
        print("Connect with result code " + str(rc) )
    def on_message(self, client, userdata, msg):
        print( msg.topic +" "+str(msg.payload))
    def publish_message(self, payload):
        self.client.publish(self.topic, payload)
    def send_message(self):
        text=self.client.textEdit.toPlainText()
        self.client.publish(self.topic, text)
        self.textEdit.clear()
    def run(self):
        self.client.connect('broker.emqx.io', 1883,60)
        self.client.subscribe(self.topic, qos=0)
        self.client.loop_forever()
        
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.th_client = Th_Client()
        self.btn_Sub.clicked.connect(self.slot_sub)
        self.btn_Pub.clicked.connect(self.slot_pub)
        self.btn_Send.clicked.connect(self.slot_send)
              
    def slot_sub(self):
        print('Subscribe btn clicked')
        self.th_client.start()
        self.textBrowser.append('subscrib start')
        
    def slot_pub(self):
        print('Publish btn clicked')
        self.th_client.publish_message('Feel so Good')

#엔터 누를 경우 메시지 보내기 버튼 작동 기능
    # def spacebar_event(self):
    #     if window.event.keyCode == 13 :
    #         self.slot_send(self)
    
    def slot_send(self):
        self.th_client.send_message()
        
if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

#가상 머신에서 Pub.
#   -$ mosquitto_pub -t phirippa -m hi~ -h broker.emqx.io