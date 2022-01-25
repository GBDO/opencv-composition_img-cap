import threading
import time
def periodic_work(hello, name, interval):
    print(hello, name)
    threading.Timer(interval,periodic_work,args=(hello,name,interval)).start()
    
periodic_work('Good morning!','phirippa',3)

count =0
while True:
    print('num : ', count)
    count+=1
    time.sleep(1)