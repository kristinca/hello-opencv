import numpy as np
import cv2
import os

import people as people

haar_cascade = cv2.CascadeClassifier(r'C:\Users\User\Desktop\projectone\haar_face.xml')

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

p = []

for i in os.listdir(r'C:\Users\User\Pictures\Saved Pictures\faces_train'):
    p.append(i)

img = cv2.imread(r'C:\Users\User\Pictures\Saved Pictures\faces_train\Golda Rosheuvel\search1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Persons', gray)

# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {p[label]} with a confidence of {confidence}')

    cv2.putText(img, str(p[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv2.imshow('Detected face', img)

cv2.waitKey(0)