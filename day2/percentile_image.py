import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.round(np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140]))


img = mpimg.imread('elon.jpg')
gray = rgb2gray(img)
old_mat = gray.copy()
prec_25 = np.percentile(gray, 25)
prec_50 = np.percentile(gray, 50)
prec_75 = np.percentile(gray, 75)
gray[gray < prec_25] = 0
gray[(gray > prec_25) & (gray < prec_50)] = np.mean(gray[(gray > prec_25) & (gray < prec_50)])
gray[(gray > prec_50) & (gray < prec_75)] = np.mean(gray[(gray > prec_50) & (gray < prec_75)])
gray[gray > prec_75] = 255

# plt.imshow(np.hstack((old_mat, gray)), cmap=plt.get_cmap('gray'),vmin=0,vmax=255)
plt.imshow()
plt.show()
