import cv2
from os import path

img = cv2.imread(path.abspath('Python/CodeWithTim/Assets/cam.jpg'), 1)
#img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2) # Scales by a 0.2x factor.
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) # Rotates.

cv2.imwrite('video_1_new_image_stored.jpg', img) # Stores the image previously modified (rotated in this context).

cv2.imshow('Image', img) # Shows the image.
cv2.waitKey(0) # Wait infinitely.
cv2.destroyAllWindows() # At the end destroys all the windows generated.