import cv2
import numpy as np

img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', gray)


# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', blur)
#
# # canny = cv2.Canny(img, 125, 175)
# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('Canny', canny)

#                               bellow 125 -> the pixel is set to 0 (black) , above 255 -> white
ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresh', thresh)

# contours, hiearchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# contours, hiearchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours, hiearchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(f'{len(contours)} contour(s) found.\n')

# draw contours on the blank img
#                 an img, a list, no.of contours (-1 -> all of them), bgr color, thickness
cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contours drawn', blank)


cv2.waitKey(0)