import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# read the image using OpenCV
# image = cv2.imread("test.png")
image = cv2.imread("test_2.png")

# ! If you try to use text that doesn't look like a text, the program won't work
# image = cv2.imread("logo.png")
# image = cv2.imread("stop.jpg")

# or you can use Pillow
# image = Image.open("test.png")

# get the string
string = pytesseract.image_to_string(image)
# print it
print(string)
