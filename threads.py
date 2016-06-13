import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(20):
            print(threading.currentThread().getName())

m1 =Messenger(name="Sends  messages")
r1 =Messenger(name="Recieves messages")

m1.start()
r1.start()
