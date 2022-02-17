import cv2

###########
# Display an image
###########

# # load in the image and save it
# img = cv2.imread("Assets/amongUsDad.png")

# # display the image in its own window
# cv2.imshow("Among Us", img)

# # delay the window from closing automatically (0 as the parameter means that it will delay
# # forever until you press a key on the window or exit out of it)
# cv2.waitKey(0)

# # close the image window
# cv2.destroyAllWindows() 


##########
# Showing a video
##########
# load the video
# capture = cv2.VideoCapture("Assets/labAsSuicideSquad.mp4")

# # loop through every frame of the video and show it (stops when you reach the end of the video)
# while capture.isOpened():
#     # read the next frame of the video. "isLoaded" is a boolean representing whether the frame was loaded or not
#     isLoaded, img = capture.read()

#     if isLoaded == True:
#         # show the current frame in a window titled "Lab vid"
#         cv2.imshow("Lab vid", img)
#         # if you press the q key or click on the exit button, then close the video window (& is bitwise "and")
#         # This also makes it wait 25ms between each frame
#         if cv2.waitKey(25) & 0xFF == ord('q') or cv2.getWindowProperty("Lab vid", 0) < 0:
#             break

#     # if an image is not loaded, leave the loop
#     else:
#         break

# # When everything done, release the video capture object
# capture.release()
   
# # Closes all the frames
# cv2.destroyAllWindows()

# load the video from the webcam
capture = cv2.VideoCapture(0)

#### setting parameters for the webcam capture
capture.set(3, 640) # the width of the window
capture.set(4, 480) # height of the window
#capture.set(10, 100)

# loop through every frame of the video and show it (stops when you reach the end of the video)
while capture.isOpened():
    # read the next frame of the video. "isLoaded" is a boolean representing whether the frame was loaded or not
    isLoaded, img = capture.read()

    if isLoaded == True:
        # show the current frame in a window titled "Lab vid"
        cv2.imshow("Lab vid", img)
        # if you press the q key or click on the exit button, then close the video window (& is bitwise "and")
        # This also makes it wait 25ms between each frame
        # Note: "getWindowProperty"
        if cv2.waitKey(25) & 0xFF == ord('q') or cv2.getWindowProperty("Lab vid", 0) < 0:
            break

    # if an image is not loaded, leave the loop
    else:
        break

# When everything done, release the video capture object
capture.release()
   
# Closes all the frames
cv2.destroyAllWindows()


