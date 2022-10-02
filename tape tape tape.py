import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:  
    _, frame = cam.read()
    
    cv2.circle(frame,(225,150),5,(0,225,0),-1)
    cv2.circle(frame,(475,150),5,(0,225,0),-1)
    cv2.circle(frame,(225,450),5,(0,225,0),-1)
    cv2.circle(frame,(475,450),5,(0,225,0),-1)
    
    pts1 = np.float32([[225,150],[475,150],[225,450],[475,450]])
    pts2 = np.float32([[0,0],[400,0],[0,600],[400,600]])
    
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(frame,matrix,(400,600))
    
    cv2.imshow('Camera',frame)
    cv2.imshow('Tra',result)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    

cam.release()
cv2.destroyAllWindows()