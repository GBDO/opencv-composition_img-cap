from threading import Thread, currentThread

class Messenger(Thread):
    def run(self):
        for i in range(5):
            print(currentThread().getName())

sender = Messenger(name='Sending out message')
receiver = Messenger(name='Receiving message')

sender.start()
receiver.start()