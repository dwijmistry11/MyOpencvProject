import cv2
import numpy as np

img = cv2.imread("Resources/baboon.png")

#findout size of image
print(img.shape)


cv2.imshow("Image",img)

cv2.waitKey(0)
