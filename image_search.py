"""ShapeDetector class"""

import cv2

# img = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/give_way_sign.jpg')
#
# cv2.imshow(img)


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        """Initialize the shape name and approximate the contour."""
        """      A contour consists of a list of vertices.       """

        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # if the shape is a triangle -> 3 vertices
        if len(approx) == 3:
            shape = "triangle"
        # if the shape has 4 vertices -> a square or a rectangle
        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "square" if 0.95 <= ar <= 1.05 else "rectangle"
        # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "pentagon"
        elif len(approx) == 6:
            shape = "hexagon"
        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"
        # return the name of the shape
        return shape


cv2.waitKey(0)
