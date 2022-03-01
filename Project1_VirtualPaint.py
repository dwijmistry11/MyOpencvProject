import cv2
import numpy as np
#read video from webcam
cap = cv2.VideoCapture(0)   #0-> ID of the camera
cap.set(10,100)             #10-> Brighness
cap.set(3,640)              #3-> width
cap.set(4,480)              #4-> height

#defining color (h_min,s_min,v_min,h_max,s_max,v_max)
##### BY USING: COLOR_DETECTION.py
# yellow pensil             15,24,7,32,225,208
# orange mobile opener tool 5,34,236,14,255,255
# green Maped glue stick    64,52,66,88,255,255

myColors = [[15,24,7,32,225,208], [5,34,236,14,255,255], [64,52,66,88,255,255]] #[h_min,s_min,v_min,h_max,s_max,v_max]

MyColorValues = [[73,242,237], [5,168,255], [11,222,0]] #[B,G,R]

MyPoints = [] #[x,y,colorID]

def findColor(img,myColors,MyColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,MyColorValues[count],cv2.FILLED)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])

        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #minimum threshold for the area
        if area>500:
            # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return  x+w//2,y


def drawOnCanvas(MyPoints,MyColorValues):
    for point in MyPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,MyColorValues[point[2]],cv2.FILLED)

#displaying video frame by frame
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,MyColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            MyPoints.append(newP)
            
    if len(MyPoints)!=0:
        drawOnCanvas(MyPoints,MyColorValues)


    cv2.imshow("Result", imgResult)
    #stop when video ends OR when user press 'q'
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break





