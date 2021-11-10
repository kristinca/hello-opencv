# import cv2


# img_from_vid = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/give_way_sign.jpg')
# template = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/give_way_template.png')
#
# # display the image and template image on screen
# cv2.imshow("Image", img_from_vid)
# cv2.imshow("Template", template)
#
# # convert both images to gray scale
# imageGray = cv2.cvtColor(img_from_vid, cv2.COLOR_BGR2GRAY)
# templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#
# # template matching
# print('Template matching...\n')
# print("[INFO] performing template matching...")
#
# # cv2.matchTemplate CAN NOT DETECT MULTIPLE OBJECTS!!!
#
# result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
#
# # define the starting and ending (x, y)-coordinates of the bounding box
# (startX, startY) = maxLoc
# endX = startX*2 + template.shape[0]//2
# endY = startY//2 + template.shape[0]
#
# # draw the bounding box on the image
# cv2.rectangle(img_from_vid, (startX, startY), (endX, endY), (0, 255, 0), 3)
# # show the output image
# cv2.imshow("Output", img_from_vid)
# cv2.waitKey(0)
#


import cv2
import numpy as np


img = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/traffic_signs.png')
# cv2.imshow('Traffic signs', img)

# # 1. create a masked image
#
# blank = np.zeros(img.shape[:2], dtype='uint8')
# # cv2.imshow('Blanks', blank)
#                                                              # radius , color
# # mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# # mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2+71), 100, 255, -1)
# mask = cv2.rectangle(blank, (img.shape[1]//2+200, img.shape[0]//2+220), (img.shape[1]//2+120, img.shape[0]//2+150),
#                      100, 255, -1)
# # cv2.imshow('Mask', mask)
#
# masked = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow('Masked', masked)
#
#
# # 2. convert masked image to gray
# blank = np.zeros(masked.shape, dtype='uint8')
#
# # cv2.imshow('Blank', blank)
#
# gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Gray', gray)
#
# #                               bellow 125 -> the pixel is set to 0 (black) , above 255 -> white
# ret, thresh = cv2.threshold(gray, 80, 275, cv2.THRESH_BINARY)
# cv2.imshow('Thresh', thresh)
#
#
# # 3. get contoours from thresh
#
# contours, hiearchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
#
# # 4. draw contours on the blank img
# #                 an img, a list, no.of contours (-1 -> all of them), bgr color, thickness
# cv2.drawContours(blank, contours, -1, (0,0,255), 1)
# cv2.imshow('Contours drawn', blank)
#
#
# # 5. convert both images to gray scale
#
# img1 = cv2.imread('C:/Users/User/Desktop/projectone/template_matching_imgs/stop_signs.jpg')
# imageGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# templateGray = cv2.cvtColor(blank, cv2.COLOR_BGR2GRAY)
#
#
#
# # template matching
# print('Template matching...\n')
# print("[INFO] performing template matching...")
#
# # cv2.matchTemplate CAN NOT DETECT MULTIPLE OBJECTS!!!
#
# result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
#
# # define the starting and ending (x, y)-coordinates of the bounding box
# (startX, startY) = maxLoc
# endX = startX + blank.shape[0]
# endY = startY + blank.shape[0]
#
# # draw the bounding box on the image
# cv2.rectangle(img1, (startX, startY), (endX, endY), (0, 255, 0), 3)
# # show the output image
# cv2.imshow("Output", img1)



cv2.waitKey(0)
