import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


img = mpimg.imread('majin.jpeg')
gray = rgb2gray(img)

values, counts = np.unique(gray, return_counts=True)
plt.bar(values, counts)
plt.show()

# plt.imshow(gray / 255, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
