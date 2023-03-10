import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


img = mpimg.imread('elon.jpg')
gray = rgb2gray(img)
only_black_and_white = (gray > 160) * 255
plt.imshow(only_black_and_white, cmap=plt.get_cmap('gray'))
plt.show()

# plt.imshow(gray / 255, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
