import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


def get_neighborhood(img, x, y, dx=1, dy=1):
    up = max(0, x - dx)
    bottom = min(img.shape[0] - 1, x + dx)

    left = max(0, y - dy)
    right = min(img.shape[1] - 1, y + dy)
    return img[up:bottom, left:right]


def average_picture(img, dx=1, dy=1):
    new_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            neighborhood = get_neighborhood(img, i, j, dx, dy)
            neighborhood_mean = neighborhood.mean()
            new_img[i, j] = neighborhood_mean
    return new_img


img = mpimg.imread('elon.jpg')
gray = rgb2gray(img)
avg_gray = average_picture(gray,10,10)

plt.imshow(avg_gray, cmap=plt.get_cmap('gray'))
plt.show()

# plt.imshow(gray / 255, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
