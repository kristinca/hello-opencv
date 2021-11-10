import cv2
from cv2.cv2 import cvtColor
from matplotlib import pyplot as plt
# matplotlib plot -> doesn't work!!!!
# it inverts the color of the
# to do:
img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cats', img)


plt.imshow(img)
plt.show()


# BGR to gray scale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to L*a*b color space
lab = cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# BGR to RGB color

rgb = cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)
plt.show()

# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV --> BGR', hsv_bgr)

# Lab to BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB --> BGR', lab_bgr)


cv2.waitKey(0)
