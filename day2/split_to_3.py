import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


img = mpimg.imread('elon.jpg')
gray = rgb2gray(img)
old_mat = gray.copy()
gray[gray < 255 / 3] = 0
gray[(gray < 255 * 2 / 3) & (gray > 255 / 3)] = 128
gray[255 * 2 / 3 < gray] = 255

# only_black_and_white = (gray > 160) * 255
plt.imshow(np.hstack((old_mat, gray)), cmap=plt.get_cmap('gray'))

# plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()

# plt.imshow(gray / 255, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
