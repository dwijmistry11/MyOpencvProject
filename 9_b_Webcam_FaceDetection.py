import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")


#read video from webcam
cap = cv2.VideoCapture(0)   #0-> ID of the camera
cap.set(10,100)             #10-> Brighness
# cap.set(3,640)              #3-> width
# cap.set(4,480)              #4-> height
#displaying video frame by frame
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detecting face
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    #creteing bounding box around face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow("Video", img)
    #stop when video ends OR when user press 'q'
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
