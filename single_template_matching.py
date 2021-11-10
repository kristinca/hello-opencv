import argparse
import cv2
import imutils


# construct the argument parser and parse the arguments
#
# ap = argparse.ArgumentParser()
# ap.add_argument('--image', '-i', required=True,
#                 help='C:/Users/User/Desktop/projectone/template_matching_imgs/coke_bottle.png')
#
#                 # help='C:/Users/User/Desktop/projectone/template_matching_imgs/image.jpg')
#
# ap.add_argument('--template', '-t', required=True,
#                 help='C:/Users/User/Desktop/projectone/template_matching_imgs/coke_logo.png')
#
#                 # help='C:/Users/User/Desktop/projectone/template_matching_imgs/fiat_logo.jpg')
#
# args = vars(ap.parse_args())
#
# # load the input image and the template image
# print('Loading images...\n')
# img_from_vid = cv2.imread(args["image"])
# template = cv2.imread(args["template"])

img_from_vid = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/image.jpg')
template = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/Fiat_Logo.png')

# display the image and template image on screen
cv2.imshow("Image", img_from_vid)
cv2.imshow("Template", template)



# convert both images to gray scale
imageGray = cv2.cvtColor(img_from_vid, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# template matching
print('Template matching...\n')
# print("[INFO] performing template matching...")

# cv2.matchTemplate CAN NOT DETECT MULTIPLE OBJECTS!!!

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

print(cv2.minMaxLoc(result))
# result_list = list(cv2.minMaxLoc(result))
# print(result_list)

# # center coordinates - manually
# maxLoc_tuple = (505, 465)
# maxLoc_tuple = cv2.minMaxLoc(result)[1]

maxLoc_tuple = (500, 425)

# define the starting and ending (x, y)-coordinates of the bounding box
(startX, startY) = maxLoc_tuple

print(maxLoc)


# endX = startX + template.shape[0]
# endY = startY + template.shape[0]
endX = startX + template.shape[0]//1000
endY = startY + template.shape[0]//1000

# draw the bounding box on the image
cv2.rectangle(img_from_vid, (startX, startY), (endX*2, endY*2), (0, 255, 0), 2)
# show the output image
cv2.imshow("Output", img_from_vid)
cv2.waitKey(0)
