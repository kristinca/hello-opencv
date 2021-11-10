import cv2
import numpy as np


img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cats', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Laplacian
#                        data depth
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian', lap)

# Sobel

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
combined_sobel = cv2.bitwise_or(sobelx, sobely)

cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Combined', combined_sobel)

canny = cv2.Canny(gray, 150, 175)
cv2.imshow('Canny', canny)


cv2.waitKey(0)