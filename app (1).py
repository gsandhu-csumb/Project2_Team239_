from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import pprint
import cv2
import smtplib
import getpass


print("These are all the images contained in the folder:  \n")
imageList = ['images']
imgName = raw_input('Enter an image name: ')
fileName = imgName + ".jpg"
im = Image.open(fileName)
width, height = im.size
print(im.size)
middle_width = (width/2)
middle_height = (height/2)
print(middle_width)
print(middle_height)
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
img = cv2.imread(fileName)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 10)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print (x,y)
        print (x+w, y+h)

variable = int(raw_input('Enter the first of the four x coordiantes given: '))
variable2 = int(raw_input('Enter the first of the four y coordiantes given: '))
variable3 = int(raw_input('Enter the last of the four x coordiantes given: '))
variable4 = int(raw_input('Enter the last of the four y coordiantes given: '))
imsmart = (variable + 50)
imsmart2 = (variable2 + 25)
imsmart3 = (variable3 - 50)
imsmart4 = (variable4 - 25)
cv2.rectangle(img,(imsmart, imsmart2), (imsmart3, imsmart4),(0,0,0),10)

morethings = (variable + 25)
morethings2 = (variable2 + 25)
cv2.line(img,(morethings, morethings2), (morethings, morethings2),(255,20,147),15)
more3 = (variable3 - 25)
more4 = (variable4 - 25)
cv2.line(img,(more3, more4), (more3, more4),(255,20,147),15)

cv2.imwrite('image.jpg', img)
cv2.waitKey()

print("These are all the fonts within the folder:  \n")
fontList = ['California']
print(fontList)
fontName = raw_input('Enter your font: ')
finalFontName = fontName + ".ttf"
text = raw_input('Enter meme text: ')
img = Image.open('image.jpg').convert('RGBA')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(finalFontName,50)
draw.text ((0, 50),text,(225,225,50), font=font)
outPutName = raw_input('Enter the final image name: ')
img.save(outPutName + ".png")