import cv2

# img = cv2.imread('Photos/megan_fox.jpeg')
# cv2.imshow('MeganFox', img)

img = cv2.imread('Photos/ABBA.jpg')
cv2.imshow('ABBA', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

# this is a list:
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f'The number of faces found is {len(faces_rect)}.')
for (x,y,w,h) in faces_rect:



    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)

