import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

# here we are searching the points visually
l1 = cv2.line(img,(243,115),(405,215),(0,0,255),3)
l2 = cv2.line(img,(405,215),(267,437),(0,255,0),3)
l3 = cv2.line(img,(267,437),(100,330),(255,0,0),3)
l4 = cv2.line(img,(100,330),(243,115),(255,255,0),3)
# p1 = (243,115)
# p2 = (405,215)
# p3 = (267,437)
# p4 = (100,330)

#defining width and height of the output card image
width, height = 250, 350

#defining points
pts1 = np.float32([[243,115],[405,215],[100,330],[267,437]])
#defining the locations(corners) of the points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#transfermation matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#generating output image
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image", img)
cv2.imshow("output image", imgOutput)

cv2.waitKey(0)