import cv2
import numpy as np

img = cv2.imread("Resources/baboon.png")

#print size of an image with color channel number
print(img.shape)

#Resize an image
imgResize = cv2.resize(img,(300,200)) #Width, Height
print(imgResize.shape)

#image cropped
imgCropped = img[0:200, 200:500] #Height, Width

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Croped image", imgCropped)

cv2.waitKey(0)