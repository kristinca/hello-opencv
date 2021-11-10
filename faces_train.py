import os
import cv2
import numpy as np


# people = ["Zendaya", "Stellan Skarsgard", "Sharon Duncan-Brewster", "Rebecca Ferguson", "Golda Rosheuvel"]

p = []

for i in os.listdir(r'C:\Users\User\Pictures\Saved Pictures\faces_train'):
    p.append(i)

DIR = r'C:\Users\User\Pictures\Saved Pictures\faces_train'

haar_cascade = cv2.CascadeClassifier(r'C:\Users\User\Desktop\projectone\haar_face.xml')

features = []
labels = []


def create_train():
    # print(haar_cascade)
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done---------')

# print(f'length of the features = {len(features)}')
# print(f'length of the labels = {len(labels)}')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

features = np.array(features, dtype='object')
labels = np.array(labels)

# Train the recognizer on the features list and the labels list

face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
