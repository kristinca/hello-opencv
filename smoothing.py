import cv2

img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cats', img)

# Averaging
average = cv2.blur(img, (7,7))
cv2.imshow('Average', average)

# Gaussian blur
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian blur', gauss)

# median blur
median = cv2.medianBlur(img, 3)
cv2.imshow('Median blur', median)

# Bilateral blur
bilateral = cv2.bilateralFilter(img, 10, 25, 25)
cv2.imshow('Bilateral blur', bilateral)

cv2.waitKey(0)