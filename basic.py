import cv2


img = cv2.imread('Photos/cat.jpg')

cv2.imshow('Cat', img)


# Converting to gray scale
#                           color_blue green red to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cat', gray)

# Blur
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('Cat', blur)

# Edge cascade

# canny = cv2.Canny(img, 125, 175)
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny edges', canny)

# Dilating the image

# dilated = cv2.dilate(canny, (3,3), iterations=1)
# number of iterations goes up -> thicker
dilated = cv2.dilate(canny, (3,3), iterations=3)
cv2.imshow('Dilating', dilated)

# Eroding

eroded = cv2.erode(dilated, (3, 3), iterations=1)
cv2.imshow('Eroding', eroded)

# Resize

resize = cv2.resize(img, (500,500))
# if shrinking the image to smaller dimensions -> interpolation=cv2.INTER_AREA
resize = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
# img -> to larger dimensions -> interpolation=cv2.INTER_LINEAR
# CUBUC is the slowest of them all but the resulting image is of a higher quality
resize = cv2.resize(img, (500,500), interpolation=cv2.INTER_LINEAR)

# Cropping
cropped = img[50:200, 200:400]
cv2.imshow('Cropping', cropped)

cv2.imshow('Resizing', resize)

cv2.waitKey(0)