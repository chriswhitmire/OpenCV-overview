import cv2

###########
# Display an image
###########

# load in the image and save it
img = cv2.imread("Assets/amongUsDad.png")

# display the image in its own window
cv2.imshow("Among Us", img)

# delay the window from closing automatically (0 as the parameter means that it will delay
# forever until you press a key on the window or exit out of it)
cv2.waitKey(0)

# close the image window
cv2.destroyAllWindows() 