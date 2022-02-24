import cv2

#read video file
cap = cv2.VideoCapture("Resources/earth.mp4")

#displaying video frame by frame
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    #stop when video ends OR when user press 'q'
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

