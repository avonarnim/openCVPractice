import cv2 as cv
import numpy as py

people = ['Person A', 'Person B']

features = []
labels = []
haarCascade = cv.CascadeClassifier('haarFace.xml')

def create_train():
    for person in people:
        # find group of images
        label = people.index(person)
        
        for each image:
            img_array = cv.imread(img_path):
            gray = cv.cvtCOlor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'same number of features as labels:{len(features) == len(labels)}')

features = np.array(features)
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml') # this is the trained model, which can be exported and reused anywhere

np.save('features.npy', features)
np.save('labels.npy', labels)

# Testing model
# Includes detecting face, then feeding detected face to model
img = cv.imread('img')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rect = haarCascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    printf('Label = {people[label]} with confidence {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)