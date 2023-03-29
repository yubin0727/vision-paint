import cv2 as cv
import numpy as np

while True:
    # Read the given image
    img = cv.imread('background.png')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    edge = cv.Laplacian(gray, cv.CV_8U, ksize = 5)
    ret, edge = cv.threshold(edge, 150, 255, cv.THRESH_BINARY_INV)
    color = cv.bilateralFilter(img, 7, 200, 400)
    cartoon = cv.bitwise_and(color, color, mask=edge)
    cv.imshow('Cartoonize', cartoon) 
    
    key = cv.waitKey()
    if key == 27: # ESC
        break

cv.destroyAllWindows()