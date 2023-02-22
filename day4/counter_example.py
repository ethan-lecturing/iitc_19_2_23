import threading
import time


class Counter:
    def __init__(self, start=0):
        self.counter = start
        self.lock = threading.Lock()

    def incerment(self):
        self.lock.acquire()
        self.counter = self.counter + 1
        time.sleep(100)
        self.lock.release()


counter = Counter()
threading.Thread(target=counter.incerment).start()
counter.incerment()
