import numpy as np

x = np.random.randint(0, 100, 100)
y = int(np.percentile(x,75))
print(y)
