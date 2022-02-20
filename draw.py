import cv2 as cv
import numpy as np

# Height, width, num color channels
blankImg = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blankImg)

# # Painting image entirely/partially green
# # blankImg[:] = 0, 255, 0
# blankImg[200:300, 200:300] = 0, 255, 0
# cv.imshow('Green', blankImg)

# Drawing a rectangle (border vs filled)
cv.rectangle(blankImg, (0,0), (250, 250), (0,255, 0), thickness=2)
cv.rectangle(blankImg, (0,0), (250, 250), (0,255, 0), thickness=cv.FILLED)

# Drawing a circle, specifying center as image midpoint, radius as 40
cv.circle(blankImg, (250, 250), 40, (0,255,0), thickness=2)

# Drawing a line
cv.line(blankImg, (100,100), (350, 350), (255, 255, 255), thickness=2)

# Writing text on an image
cv.putText(blankImg, 'Hello world', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)

cv.imshow('Green', blankImg)

cv.waitKey(0)