import cv2

#read video from webcam
cap = cv2.VideoCapture(0)   #0-> ID of the camera
cap.set(10,100)             #10-> Brighness
# cap.set(3,640)              #3-> width
# cap.set(4,480)              #4-> height
#displaying video frame by frame
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    #stop when video ends OR when user press 'q'
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
