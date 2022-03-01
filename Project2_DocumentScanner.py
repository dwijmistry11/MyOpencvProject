import cv2
import numpy as np

#################################################
widthImg = 480
heightImg = 640

###################################################
#read video from webcam
cap = cv2.VideoCapture(0)   #0-> ID of the camera
cap.set(10,150)             #10-> Brighness
# cap.set(3,widthImg)              #3-> width
# cap.set(4,heightImg)              #4-> height

###################################################

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDilate = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThreshold = cv2.erode(imgDilate,kernel,iterations=1)

    return imgThreshold
    

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #minimum threshold for the area
        if area>5000:
            # cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) ==4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
    return biggest


def reorder(myPoints):
    # we have to reshape the points
    # because when we print bigest it shows (4,1,2) 
    # in which 4 is the points 2 is the x and y cordinets  and we have to get rid of 1
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)

    # now we have to reorder the cordinets 
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


def getWarp(img,biggest):
    
    # biggest = reorder(biggest)
    
    #defining points
    pts1 = np.float32(biggest)
    #defining the locations(corners) of the points
    pts2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    #transfermation matrix
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    #generating output image
    imgOutput = cv2.warpPerspective(img,matrix,(widthImg,heightImg))

    return imgOutput



#############################################################

while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgContour = img.copy()


    imgTherhold = preProcessing(img)
    biggest = getContours(imgTherhold)
    imgWarped = getWarp(img,biggest)

    cv2.imshow("Video", imgWarped)
    #stop when video ends OR when user press 'q'
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
