import time
import threading


class Queue:
    def __init__(self):
        self.lst = []
        self.lock = threading.Lock()
        self.b_lock = threading.Lock()
        self.b_lock.acquire()

    def push(self, x):
        self.lock.acquire()
        if self.b_lock.locked():
            self.b_lock.release()
        self.lst.append(x)
        self.lock.release()

    def b_pop(self):
        self.b_lock.acquire()

        x = self.pop()
        if len(self) > 0:
            self.b_lock.release()
        return x

    def pop(self):

        if len(self) == 0:
            raise ValueError('No items in queue')
        else:
            self.lock.acquire()
            x = self.lst[0]
            del self.lst[0]
            self.lock.release()
            return x

    def peek(self):
        if len(self) == 0:
            raise ValueError('No items in  queue')
        return self.lst[0]

    def __len__(self):
        return len(self.lst)


q = Queue()


def wait_and_insert():
    global q
    time.sleep(5)
    q.push('some value')


threading.Thread(target=wait_and_insert).start()
x = q.b_pop()
print('The popped item is:', x)
print('Trying to pop another one:')
x = q.b_pop()
print(x)
