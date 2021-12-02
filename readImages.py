import cv2 as cv

img = cv.imread('images/elephant13.png')

cv.imshow('Elephant', img)

#resize images
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def rotateFrame(frame):
    return cv.rotate(frame, rotateCode = 0)


resizedImg = rescaleFrame(img)
cv.imshow('Elephant Resized', resizedImg)

rotatedImg = rotateFrame(img)
cv.imshow('Elephant Rotated', rotatedImg)

cv.waitKey(0)
cv.destroyAllWindows()