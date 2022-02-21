import cv2

print('Hello world')

#####################################################

# #read image
# img = cv2.imread("Resources/lena_color_256.tif")
#
# #display image
# cv2.imshow("Output", img)
#
# #wait to see image
# cv2.waitKey(0)

#####################################################
#
# #read video file
# cap = cv2.VideoCapture("Resources/earth.mp4")
#
# #displaying video frame by frame
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     #stop when video ends OR when user press 'q'
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

########################################################

# #read video from webcam
# cap = cv2.VideoCapture(0)   #0-> ID of the camera
# cap.set(10,100)             #10-> Brighness
# # cap.set(3,640)              #3-> width
# # cap.set(4,480)              #4-> height
# #displaying video frame by frame
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     #stop when video ends OR when user press 'q'
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

############################################################

#Basic functionality of OpenCV

img = cv2.imread("Resources/lena_color_512.tif")

#convering RGB image into Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)

cv2.waitKey(0)