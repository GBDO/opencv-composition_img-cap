from threading import Thread
import time

def task_A(value):
    for i in range(5):
        print('Thread - Task A:', i)
        time.sleep(2)

threadA = Thread(target = task_A, args=(1,))
threadA.start()

#main task
for i in range(5):
    print('Main Task:      ',i)
    time.sleep(1)
print('--- Main task end ---')
threadA.join()