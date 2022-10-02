import cv2

cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


camera = cv2.VideoCapture(0)
img = cv2.imread("faces.jpg")
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
body = cascade.detectMultiScale(color,1.3, 5)

for (x,y,h,w) in body:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cascade_1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_1 = cascade_1.detectMultiScale(color,1.3, 5)
def deter(frame,gray):
    for (x,y,w,h) in body_1:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smile = cascade.detectMultiScale(frame, 1.9, 20)


cv2.imshow('ромаш',img)
cv2.waitKey(0)
cv2.destroyAllWindows()