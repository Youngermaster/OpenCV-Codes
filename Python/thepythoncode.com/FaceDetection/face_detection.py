import cv2

# loading the test image
image = cv2.imread("kids.jpg")
# converting to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# initialize the face recognizer (default face haar cascade)
face_cascade = cv2.CascadeClassifier(
    "cascades/haarcascade_fontalface_default.xml")
# detect all the faces in the image
faces = face_cascade.detectMultiScale(image_gray)
# print the number of faces detected
print(f"{len(faces)} faces detected in the image.")
