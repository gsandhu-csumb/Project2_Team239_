import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("MP900427683-1024x770.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (80, 90, 160), 5)
        roi_color = img[y:y+h, x:x+w]

cv2.imwrite('image.jpg', img)
cv2.waitKey()