from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import pprint
import cv2
import smtplib
import getpass


print("These are all the images contained in the folder:  \n")
print("Images (rock.jpg), (Beyonce.jpg), (Jayz.jpg), (Rhianna.jpg)")
imgName = raw_input('Enter image name: ')
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
favoritecolor = int(raw_input('Enter the RGB values of your favorite color for the glasses! Enter value for R: '))
favoritecolor2 = int(raw_input('Enter value for G: '))
favoritecolor3 = int(raw_input('Enter value for B: '))
for (x,y,w,h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (favoritecolor, favoritecolor2, favoritecolor3), 10)
        print (x,y)
        print (x+w, y+h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

variable = int(raw_input('Enter the first of the four x coordiantes given: '))
variable2 = int(raw_input('Enter the first of the four y coordiantes given: '))
variable3 = int(raw_input('Enter the last of the four x coordiantes given: '))
variable4 = int(raw_input('Enter the last of the four y coordiantes given: '))
imsmart = (variable + 50)
imsmart2 = (variable2 + 25)
imsmart3 = (variable3 - 50)
imsmart4 = (variable4 - 25)
cv2.rectangle(img,(imsmart, imsmart2), (imsmart3, imsmart4),(favoritecolor, favoritecolor2, favoritecolor3),10)

favoritecolor4 = int(raw_input('Enter the RGB values of your favorite color for the dots in the middle of the glasses! Enter value for R: '))
favoritecolor5 = int(raw_input('Enter value for G: '))
favoritecolor6 = int(raw_input('Enter value for B: '))
morethings = (variable + 25)
morethings2 = (variable2 + 25)
cv2.line(img,(morethings, morethings2), (morethings, morethings2),(favoritecolor4,favoritecolor5,favoritecolor6),15)
more3 = (variable3 - 25)
more4 = (variable4 - 25)
cv2.line(img,(more3, more4), (more3, more4),(favoritecolor4,favoritecolor5,favoritecolor6),15)

cv2.imwrite('image.jpg', img)
cv2.waitKey()

print("These are all the fonts within the folder:  \n")
print("California, Surf, Thrust")
fontName = raw_input('Enter your font: ')
fontSize = int(raw_input('Enter a value for font size from 20 - 100: '))
favoritecolor7 = int(raw_input('Enter the RGB values of your favorite color for the font! Enter value for R: '))
favoritecolor8 = int(raw_input('Enter value for G: '))
favoritecolor9 = int(raw_input('Enter value for B: '))
finalFontName = fontName + ".ttf"
text = raw_input('Enter top meme text: ')
img = Image.open('image.jpg').convert('RGBA')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(finalFontName,fontSize)
sock = (middle_width - 100)
draw.text ((sock, 50),text,(favoritecolor7,favoritecolor8,favoritecolor9), font=font)
textBelow = raw_input('Enter below meme text only a few word: ')
img2 = Image.open(fileName).convert('RGBA')
draw2 = ImageDraw.Draw(img)
font = ImageFont.truetype(finalFontName,fontSize)
sock = (middle_width - 100)
muffin = (height - 150)
draw2.text ((sock, muffin),textBelow,(favoritecolor7,favoritecolor8,favoritecolor9), font=font)

outPutName = raw_input('Enter the final image name: ')
img.save(outPutName + ".png")
