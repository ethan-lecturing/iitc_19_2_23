from multiprocessing import Process,Queue

i = 0


def f():
    global i
    i = i + 1
    print(i)


if __name__ == '__main__':
    for j in range(50):
        p = Process(target=f)
        p.start()
