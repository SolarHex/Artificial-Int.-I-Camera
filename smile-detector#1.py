import cv2

cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cascade_1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



camera = cv2.VideoCapture(0)
img = cv2.imread('pool.jpg')
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
body = cascade.detectMultiScale(color,1.3, 5)
#In this step, we are going to build main function which would be performing the smile detection. 
def deter(frame,gray):
    determine = cascade_1.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in determine:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smile = cascade.detectMultiScale(frame, 1.9, 20)




cv2.imshow('oOoOo',img)
cv2.destroyAllWindows()
cv2.waitKey(0)