#filename = PyQt_MQTT_0.py
from email import message
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import paho.mqtt.client as mqtt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect('broker.emqx.io',1883, 60)
        self.client.loop_start()
        self.client.subscribe('phirippa') #구독할 Topic명: phirippa

    def on_connect(self,client, userdata, flags, rc):
        print('Connected with result code : ' + str(rc))
        
        
    def on_message(self,client, userdata, msg):
        message = str(msg.payload, 'utf-8')
        print('Topic : '+msg.topic +', Message : '+message)

if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

#가상 머신에서 Pub.
#   -$ mosquitto_pub -t phirippa -m hi~ -h broker.emqx.io