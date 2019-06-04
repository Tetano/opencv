import cv2
import numpy as np

rosto_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
olho_cascade = cv2.CascadeClassifier('haarcascade_frontalface_eye.xml')

frame = cv2.VideoCapture(1)

while True:
    ret, img = frame.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = rosto_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w), (y+h), (255,0,0),2 )
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        olhos = olho_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in olhos:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    frame.release()
    cv2.destroyAllWindows()



