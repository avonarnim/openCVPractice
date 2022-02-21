import cv2 as cv
import numpy as np

# Contours are curves joining continuous points along a boundary with a shared color/intensity
img = cv.imread('guy.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countrs found')

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,255,0), 2)
cv.imshow('Contours', blank)
cv.waitKey(0)