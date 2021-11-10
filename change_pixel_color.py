# import cv2
# from PIL import Image
#
#
# img = cv2.imread('C:/Users/User/Desktop/projectone/Photos/green_square.jpg')
# cv2.imshow("Green square", img)
#
# for x in range(img.size):
#     img.putpixel((x, x), (0, 0, 0, 255) )
#
#
# img.show()
# cv2.waitKey(0)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

imageArray = plt.imread('C:/Users/User/Desktop/projectone/Photos/green_square.jpg')

plt.imshow(imageArray)

fig, ax = plt.subplots(1)

plt.imshow(imageArray)

square = patches.Rectangle((100,100), 1,1, color='RED')
ax.add_patch(square)

plt.show()