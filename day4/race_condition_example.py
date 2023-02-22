import threading
import time

i = 0


def bla():
    global i
    print(i)
    i = i+ 1
    time.sleep(0.1)
    i = i- 1
    print(i)

for j in range(100):
    threading.Thread(target=bla).start()