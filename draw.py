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

# Bitwise operations
blank = np.zeros((500, 500, 3), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (0,0), (250, 250), (0,255, 0), thickness=cv.FILLED)
circle = cv.circle(blank.copy(), (250, 250), 40, (0,255,0), thickness=cv.FILLED)
# cv.imshow('Bitwise AND', cv.bitwise_and(rectangle, circle))
# cv.imshow('Bitwise OR', cv.bitwise_or(rectangle, circle))
cv.imshow('Bitwise XOR', cv.bitwise_xor(rectangle, circle))
cv.imshow('Bitwise NOT', cv.bitwise_not(cv.bitwise_or(rectangle,circle)))

# Masking
img = cv.imread('guy.jpeg')
blank = np.zeros(img.shape[:2], dtype='int8')
mask = cv.circle(blank, (img.shape[1]//2+90, img.shape[0]//2-50), 100, 255, -1)
cv.imshow('Masked Image', cv.bitwise_and(img, img, mask=mask))

cv.waitKey(0)