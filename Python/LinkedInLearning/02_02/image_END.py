import numpy as np
import cv2
img = cv2.imread('../images/devon.jpg')
#print(img.shape)

b = img[:,:,0]
print(b)
g = img[:,:,1]
r = img[:,:,2]

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
