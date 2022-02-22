import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('guy.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Creating a mask over the image; histogram can be set to only focus on masked area
blank = np.zeros(gray.shape[:2], dtype='int8')
mask = cv.bitwise_and(gray, gray, mask= cv.circle(blank, (gray.shape[1]//2+90, gray.shape[0]//2-50), 100, 255, -1))
cv.imshow('Masked', mask)
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Creating a plot of the frequencies of r,g,b intensities in a masked area
plt.figure()
plt.figure('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)