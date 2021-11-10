import cv2


# Reading video

capture = cv2.VideoCapture('C:/Users/User/Desktop/projectone/Videos/1.mp4')

while True:
    """Get an image from a video, show that image,
    and make template matching from that image"""

    # # success, image = capture.read()
    # count = 0
    # success = True
    # while success:
    #     success,  image = capture.read()
    #     print('Read a new frame: ', success)
    #     cv2.imwrite( 'C:/Users/User/Desktop/projectone/template_matching_imgs' + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
    #     count += 1

    isTrue, frame = capture.read()
    isTrue = True
    cv2.imshow('Video', frame)
    if isTrue:
        success, image = capture.read()
        # this_img = str(input('Enter "h" to get image from the video...\t'))
        # if this_img.lower() == 'h':
        cv2.imwrite('C:/Users/User/Desktop/projectone/template_matching_imgs' + "\\image.jpg",frame)  # save frame as JPEG file
        cv2.imshow("This image", image)
        cv2.waitKey(0)
    if cv2.waitKey(100) & 0xFF == ord('d'):
        break

    capture.release()
    # cv2.destroyAllWindows()

