#CST 205 Multimedia & Design 

#Glasses and Text Filter

#Gurjot Sandhu
#Alejandro Casillas
#Diego Garcia

#March 16, 2017

#Github:   https://github.com/gsandhu-csumb/Project2_Team239_


from PIL import Image           #Alejandro/Diego
from PIL import ImageFont       #Alejandro/Diego
from PIL import ImageDraw       #Alejandro/Diego
import numpy as np              #Gurjot
import pprint                   #Gurjot
import cv2                      #Gurjot
import smtplib
import getpass


print("These are all the images contained in the folder:  \n")          
print("Images (rock.jpg), (Beyonce.jpg), (Jayz.jpg), (Rhianna.jpg)")
imgName = raw_input('Enter image name: ')
fileName = imgName + ".jpg"                        #Adds jpg to the end of user input
im = Image.open(fileName)
width, height = im.size
print(im.size)
middle_width = (width/2)
middle_height = (height/2)
print(middle_width)
print(middle_height)
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")              #Detects eyes in the picture
img = cv2.imread(fileName)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)
favoritecolor = int(raw_input('Enter the RGB values of your favorite color for the glasses! Enter value for R: '))      #Lets user input color
favoritecolor2 = int(raw_input('Enter value for G: '))
favoritecolor3 = int(raw_input('Enter value for B: '))
for (x,y,w,h) in eyes:                                                  #For loop to draw the rectangles and print the x&y of rectangles
        cv2.rectangle(img, (x, y), (x+w, y+h), (favoritecolor, favoritecolor2, favoritecolor3), 10)
        print (x,y)
        print (x+w, y+h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

variable = int(raw_input('Enter the first of the four x coordiantes given: '))
variable2 = int(raw_input('Enter the first of the four y coordiantes given: '))
variable3 = int(raw_input('Enter the last of the four x coordiantes given: '))
variable4 = int(raw_input('Enter the last of the four y coordiantes given: '))
imsmart = (variable + 50)                                                               #Takes the x from the first rectangle drawn and adds 50 to bring it to middle of rectangle
imsmart2 = (variable2 + 25)                                                             #Takes the y from the first rectangle drawn and adds 25 to bring it to middle of rectangle
imsmart3 = (variable3 - 50)                                                             #Takes the x from the first rectangle drawn and subtracts 50 to bring it to middle of rectangle
imsmart4 = (variable4 - 25)                                                             #Takes the y from the first rectangle drawn and subtracts 25 to bring it to middle of rectangle
cv2.rectangle(img,(imsmart, imsmart2), (imsmart3, imsmart4),(favoritecolor, favoritecolor2, favoritecolor3),10) #draws the line which connects the square (Gurjot)

favoritecolor4 = int(raw_input('Enter the RGB values of your favorite color for the dots in the middle of the glasses! Enter value for R: '))
favoritecolor5 = int(raw_input('Enter value for G: '))
favoritecolor6 = int(raw_input('Enter value for B: '))
morethings = (variable + 25)                                                            #Calculates the coordinates directly in the middle of the rectangles
morethings2 = (variable2 + 25)                                                          #Calculates the coordinates directly in the middle of the rectangles
cv2.line(img,(morethings, morethings2), (morethings, morethings2),(favoritecolor4,favoritecolor5,favoritecolor6),15)    #Draws first dot for first rectangle (Gurjot)
more3 = (variable3 - 25)                                                                #Calculates the coordinates directly in the middle of the rectangles
more4 = (variable4 - 25)                                                                #Calculates the coordinates directly in the middle of the rectangles
cv2.line(img,(more3, more4), (more3, more4),(favoritecolor4,favoritecolor5,favoritecolor6),15)                          #Draws second dot for second recatngle (Gurjot)

cv2.imwrite('image.jpg', img)                                                           #Saves image as 'Image' to use in next line of code
cv2.waitKey()

print("These are all the fonts within the folder:  \n")
print("California, Surf, Thrust")
fontName = raw_input('Enter your font: ')
fontSize = int(raw_input('Enter a value for font size from 20 - 100: '))
favoritecolor7 = int(raw_input('Enter the RGB values of your favorite color for the font! Enter value for R: '))
favoritecolor8 = int(raw_input('Enter value for G: '))
favoritecolor9 = int(raw_input('Enter value for B: '))
finalFontName = fontName + ".ttf"                                                       #Adds .ttf to the end of user input to allow use within program 
text = raw_input('Enter top meme text: ')
img = Image.open('image.jpg').convert('RGBA')
draw = ImageDraw.Draw(img)                                                              #Enables the draw funciton which is used later (Alejandro)
font = ImageFont.truetype(finalFontName,fontSize)                                       #Gets the font to use and the size of the font (Diego)
sock = (middle_width - 100)                                                             #Makes code universal by drawing text 100 pixels to the left of the image (Diego)
draw.text ((sock, 50),text,(favoritecolor7,favoritecolor8,favoritecolor9), font=font)   #Draws text user inputed (Alejandro)
textBelow = raw_input('Enter below meme text only a few word: ')
img2 = Image.open(fileName).convert('RGBA')
draw2 = ImageDraw.Draw(img)
font = ImageFont.truetype(finalFontName,fontSize)
muffin = (height - 150)                                                                 #Makes code universal by drawing it 150 pixels before the bottom of the image (Gurjot)
draw2.text ((sock, muffin),textBelow,(favoritecolor7,favoritecolor8,favoritecolor9), font=font) #Draws text user inputed 

outPutName = raw_input('Enter the final image name: ')                                  #Allows user to save the pic as what they want to name it (Alejandro)
img.save(outPutName + ".png")                                                           #saves image as png (Alejandro)
