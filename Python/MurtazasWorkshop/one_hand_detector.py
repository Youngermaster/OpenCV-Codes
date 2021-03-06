# TODO: Test if the performance could be increased by executing the program with a GPU.
# from numba import jit, cuda

import cv2
from cvzone.HandTrackingModule import HandDetector


def execute():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)

    while True:
        success, img = cap.read()

        img = detector.findHands(img)
        lm_list, _ = detector.findPosition(img)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    execute()
