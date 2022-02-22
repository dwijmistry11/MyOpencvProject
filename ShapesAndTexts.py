import cv2
import numpy as np

#creating an image using numpy lib
img = np.zeros((512,512)) # this will create the gray scale image
print(img)

img2 = np.zeros((512,512,3),np.uint8) # color image without colors
print(img2)

img3 = np.zeros((512,512,3),np.uint8) # coloring an image
print(img3)
img3[:] = 255,0,0 # coloring an whole image

img4 = np.zeros((512,512,3),np.uint8) # coloring an image
print(img4)
img4[200:300, 100:300] = 255,0,0 # coloring on a perticular region of an image

shapes = np.zeros((512,512,3),np.uint8) # coloring an image

cv2.line(shapes,(0,0),(shapes.shape[1],shapes.shape[0]),(0,255,0),3) #creating a line
cv2.rectangle(shapes,(0,0),(250,350),(0,0,255),2) #outlined rectangle
cv2.rectangle(shapes,(100,100),(250,350),(255,255,255),cv2.FILLED) #filled rectangle
cv2.circle(shapes, (400,50),100,(255,0,0),4) #Circle
cv2.putText(shapes, " OPENCV  ", (300,200), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)


cv2.imshow("gray image", img)
cv2.imshow("color image", img2)
cv2.imshow("Color image", img3)
cv2.imshow("Color image", img4)
cv2.imshow("My shapes", shapes)

cv2.waitKey(0)