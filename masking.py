import cv2
import numpy as np


# img = cv2.imread('Photos/cats.jpg')
img = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/Fiat_Logo.png')
cv2.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('Blanks', blank)
                                                             # radius , color
# mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2+71), 100, 255, -1)
mask = cv2.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2, img.shape[0]//2), 100, 255, 1)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Masked', masked)

cv2.waitKey(0)
