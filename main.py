import cv2


img = cv2.imread('Photos/cat1.jpg')
cv2.imshow("Cat", img)

cv2.waitKey(0)

# Reading videos
#
# capture = cv2.VideoCapture('Videos/1.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()
#
# # cv2.waitKey(0)