import cv2
import numpy as np


img = cv2.imread('Photos/cat.jpg')

cv2.imshow('Cat', img)

# Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    #              width -> 1,   height-> 0
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

#  -x -> Left
#  -y -> Up
#  x -> Right
#  y -> Down

# translated down 100 pixels and right 100 pixels
# translated = translate(img, 100, 100)
translated = translate(img, -100, -100)
cv2.imshow('Translated', translated)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    #                     (rotation point, angle, scaling)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
rotated = rotate(img, -45)

cv2.imshow('Rotated', rotated)

rotated_rotaded = rotate(rotated, 60)
cv2.imshow('Rotated rotated', rotated_rotaded)
#  rotating on a black background by default


# Resizing

resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Flip
#                   0 -> around the x axis, 1 -> y, -1 -> flip vertically and horizontally
# flip = cv2.flip(img, 0)
flip = cv2.flip(img, 1)
cv2.imshow('Flipped', flip)

# Cropping

cropped = img[100:200, 100:200]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)