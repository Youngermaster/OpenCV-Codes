import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# read the image using OpenCV
# image = cv2.imread("test.png")
# image = cv2.imread("logo.png")
# or you can use Pillow
# image = Image.open("test.png")
image = Image.open("logo.png")

# get the string
string = pytesseract.image_to_string(image)
# print it
print(string)
