#computer vision
import cv2

#kernal and metrix
import numpy as np

#Basic functionality of OpenCV

img = cv2.imread("Resources/lena_color_512.tif")

#defining kernel
kernel = np.ones((5,5),np.uint8)


#convering RGB image into Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edge detection
imgCanny = cv2.Canny(img, 150, 200)

#Dialation
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

#Errosan
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)
