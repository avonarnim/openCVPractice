import cv2 as cv
import numpy as np

img = cv.imread('guy.jpeg')

# Convert to grayscale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grayImg)

# Blur image - good if the goodness of the image is doubted
# Size of kernel determines intensity of blur; must be odd-valued
blurImg = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blurImg)

# Edge cascade
# To reduce amount of edges found, apply blur
canny = cv.Canny(blurImg, 125, 175)
cv.imshow('Edges', canny)

# Dilating image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding image -- similar to inverse dilation
eroded = cv.dilate(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resizing image
# inter_area is fine for shrinking image
# cubic, linear are best for increasing size
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping image
cropped = img[200:300, 200:300]
cv.imshow('Cropped', cropped)

def translate(img, xShift, yShift):
    transMat = np.float32([[1, 0, xShift], [0, 1, yShift]])
    # width & height
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

shifted = translate(img, 100, 100)
cv.imshow('Translated', shifted)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Can also do resizing, flipping, etc. to an image

cv.waitKey(0)