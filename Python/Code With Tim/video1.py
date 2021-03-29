import cv2

img = cv2.imread('C:\\Users\\juanm\\Documents\\GitHub\\Youngermaster\\OpenCV-Codes\\Python\\Code With Tim\\Assets\\cam.jpg', 1)
img = cv2.resize(img, (400, 400))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()