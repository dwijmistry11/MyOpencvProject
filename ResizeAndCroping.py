import cv2
import numpy as np

img = cv2.imread("Resources/baboon.png")

#print size of an image with color channel number
print(img.shape)

#Resize an image
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)

cv2.waitKey(0)