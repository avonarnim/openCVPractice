import cv2 as cv

# Reading in an image
img = cv.imread('guy.jpeg')

# Rescales a given frame
def rescaleFrame(frame, scale=0.75):
    width = int (frame.shape[1] * scale)
    height = int (frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Creates a window with the image
resizedImage = rescaleFrame(img)
cv.imshow('Guy', resizedImage)

# Changing color spaces
grayVersion = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsvVersion = cv.cvtColor(img, cv.COLOR_BGR2HSV)
labVersion = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgbVersion = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('GuyInverted', rgbVersion)

# Splitting color channels. Displays pixel intensity in grayscale 
# (shape of structure passed to imshow determines how it's interpreted)
b,g,r = cv.split(img)
cv.imshow('Blue Only', b)

# Waits for 0 to be pressed, then closes image
cv.waitKey(0)

# capture = cv.VideoCapture('clapPushup.mov')
# while True:

#     # Displays video frame by frame
#     # Automatically stops playing video when there are no more frames
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     # Pressing 'd' breaks out of video displaying loop
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

