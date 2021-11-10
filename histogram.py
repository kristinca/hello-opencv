import cv2
import matplotlib.pyplot as plt
import numpy as np

# plot with matplotlib does not work !!!

img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

circle = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, -1)
mask = cv2.bitwise_and(gray, gray, mask=circle)
cv2.imshow('Mask', mask)

# grayscale histogram
#                                        number of pixels, range
gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color histogram
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv2.waitKey(0)