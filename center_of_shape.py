""" OpenCV center of contour """


import argparse
import imutils
import cv2

# Compute the center of a contour/shape region.
# Recognize various shapes, such as circles, squares, rectangles, triangles and pentagons
# using only contour properties.
# Label the color of a shape.

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# image: load -> grayscale -> blur -> threshold
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("thresh", thresh)

# find contours of the thresh image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)

# loop over the center of the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 3)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)
    cv2.imshow("image", img)
    cv2.waitKey(0)
