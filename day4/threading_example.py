import threading

import time


def worker(i):
    time.sleep(0.1)
    print(f'worker {i}')


lst = []
for i in range(1000):
    t = threading.Thread(target=worker, args=[i], daemon=True)
    t.start()
    lst.append(t)

# for t in lst:
#     t.join()
print('Finished running threads')
