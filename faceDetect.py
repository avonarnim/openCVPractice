import cv2 as cv

img = cv.imread('guy.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Haar Cascade method to image/facial detection
haarCascade = cv.CascadeClassifier('haarFace.xml')

# increasing/decreasing MinNeighbors can decrease/increase number of faces identified
faces_rect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('found', img)

cv.waitKey(0)