import argparse
import cv2

ap = argparse.ArgumentParser()
print('test1')
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input image where we'll apply template matching")
args = vars(ap.parse_args())
print('test')
image = cv2.imread('Photos/cat1.jpg')

cv2.imshow("image", image)
cv2.waitKey(0)
