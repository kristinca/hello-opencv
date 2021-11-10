import cv2

img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cats', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cats 2', gray)

# Simple thrasholding

threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold', thresh)

threshold, thresh_inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold inverse', thresh_inv)

# Adaptive thrashold
#                                            max value                                      kernel = 11x11
# adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
# adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 13, 9)
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 13, 9)
cv2.imshow('adaptive Threshold', adaptive_thresh)




cv2.waitKey(0)