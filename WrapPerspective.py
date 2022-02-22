import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

l1 = cv2.line(img,(243,115),(380,230),(0,0,255),3)

cv2.imshow("image", img)

cv2.waitKey(0)