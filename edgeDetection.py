import cv2 as cv
import numpy as np

img = cv.imread('guy.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian edge detection
# Finds maximum gradients
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel method
# Finds gradient in x and y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

# Combined sobel
sobelComb = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', sobelComb)

cv.waitKey(0)