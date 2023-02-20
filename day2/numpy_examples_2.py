import timeit
import numpy as np

mat_size = (1000, 1000,)
x = np.random.random(mat_size)


def get_min_by_for():
    global x
    min_value = 1
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i, j] < min_value:
                min_value = x[i, j]
    return min_value

np.min()
time = timeit.timeit(get_min_by_for, number=10) / 10
time2 = timeit.timeit(x.min, number=10) / 10
print('For loop time',time)
print('numpy time',time2)
