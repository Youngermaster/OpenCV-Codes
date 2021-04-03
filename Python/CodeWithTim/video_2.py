import cv2
from os import path
import random
img = cv2.imread(path.abspath('Python/CodeWithTim/Assets/cam.jpg'), 1)

# Prints the array
#print(img)

# Prints out the type of the img object
print(type(img))

"""
Prints: 

Height
Width
Channels
"""
print(img.shape)

# Gives Random color values to the first 300 rows
for i in range(300):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


tag = img[500:700, 600:900]
img[800:1000, 650:950] = tag

img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2) # Scales by a 0.2x factor.

cv2.imwrite('video_2new_image_stored.jpg', img) # Stores the image previously modified (rotated in this context).

cv2.imshow('Image', img) # Shows the image.
cv2.waitKey(0) # Wait infinitely.
cv2.destroyAllWindows() # At the end destroys all the windows generated.
