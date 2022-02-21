import cv2

#read image
img = cv2.imread("Resources/lena_color_256.tif")

#display image
cv2.imshow("Output", img)

#wait to see image
cv2.waitKey(0)