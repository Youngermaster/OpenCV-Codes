import numpy as np
import cv2
img = cv2.imread('../images/typewriter.jpg')
#print(img.shape)

all_rows = open('../model/synset_words.txt').read().strip().split("\n")

classes = [r[r.find(' ') + 1:] for r in all_rows]

for (i,c) in enumerate(classes):
    if i==4:
        break
    print(i,c)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
