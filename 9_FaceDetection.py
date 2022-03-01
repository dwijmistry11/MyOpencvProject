import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lena_color_512.tif')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detecting face
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#creteing bounding box around face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("Result",img)
cv2.waitKey(0)

