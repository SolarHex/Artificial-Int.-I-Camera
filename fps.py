import cv2
import numpy as np
import dlib

cam = cv2.VideoCapture(0)

while True: 
    _, frame = cam.read()
    cv2.imshow('Camera',frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()