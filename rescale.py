import cv2
import os
import time
import imutils
import numpy as np



img = cv2.imread('image.jpg')
cv2.imshow("Cat", img)


def rescaleFrame(frame1, scale=0.3):
    width = int(frame1.shape[1] * scale)
    height = int(frame1.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame1, dimensions, interpolation=cv2.INTER_AREA)


#
# resized_image = rescaleFrame(img)
# cv2.waitKey(0)
# cv2.imshow("Cat", resized_image)
# cv2.imwrite('C:/Users/User/Desktop/projectone' + "\\scaled_image.jpg", resized_image)  # save frame as JPEG file
# cv2.waitKey(0)


def changeRes(width, height):
    """"live videos"""

    capture.set(3, width)
    capture.set(4, height)


# Reading videos

capture = cv2.VideoCapture('C:/Users/User/Desktop/projectone/car1.avi')

# (h, w) = capture.shape[:2]
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# writer = cv2.VideoWriter('car1.mp4',
#                          fourcc, 1.0,
#                          (w, h), True)

# frame_width = int(capture.get(3))
# frame_height = int(capture.get(4))
# size = (frame_width//2, frame_height//2)
#
# result = cv2.VideoWriter('filename.avi',
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, size)

out = cv2.VideoWriter('car1.avi', -1, 20.0, (640,480))

while True:
    """existing videos"""

    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)

    out.write(frame_resized)


    # write the output frame to filed
    # result.write(frame)
    #
    # key = cv2.waitKey(1) & 0xFF
    # if key == ord("q"):
    #     break

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
out.release()
# result.release()
cv2.destroyAllWindows()