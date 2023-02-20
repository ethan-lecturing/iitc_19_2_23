import numpy as np

x = np.random.random((4, 5))
print(x.reshape(10,2))

x = np.arange(5)
y = np.arange(5) * 3
print(x)
print(y)
print(np.hstack((x,y)))