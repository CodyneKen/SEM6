import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import random as r



#trouver comment declarer img une seule fois et réassigner les valeurs
#trouver comment gerer les namespaces pour ne pas avoir a passer les params dans les fonction a chaque fois

height = 480
width = 640
delay = 300
img = np.zeros((height,width,3), np.uint8)

flag_rec = False 
windowName = 'EX2_COLOR'

img = np.zeros((height,width,3), np.uint8)

#DISPLAY
def displayRec(img, color_rgb, posx, posy):
    img = createRec(img, color_rgb, posx, posy)
    cv2.imshow(windowName, img)


def displayBlack(img):
    img = np.zeros_like(img)
    cv2.imshow(windowName, img)
    return img


#SLIDER_GENERATION
def createSliderRGB():
    cv2.createTrackbar("R", windowName, 100, 255, updateSliderR)
    cv2.createTrackbar("G", windowName, 100, 255, updateSliderG)
    cv2.createTrackbar("B", windowName, 100, 255, updateSliderB)

def createSliderHW():
    cv2.createTrackbar("Height", windowName, 50, height, updateSliderH) 
    cv2.createTrackbar("Width", windowName, 100, width, updateSliderW) 

def getSliderRGB():
    return np.array([slider_red, slider_green, slider_blue])

#UPDATE_CALLBACKS
def updateSliderR(newval):
    global slider_red
    slider_red = newval
def updateSliderG(newval):
    global slider_green
    slider_green = newval
def updateSliderB(newval):
    global slider_blue
    slider_blue = newval

def updateSliderH(newval):
    global slider_height
    slider_height = newval
def updateSliderW(newval):
    global slider_width
    slider_width = newval

def rectMouse(event, x, y , flags, data):
    sh2 = slider_height/2
    sw2 = slider_width/2

    if x >= width-sw2: x = width-sw2-1
    if x <= 0+sw2: x = sw2+1 
    if y >= height-sh2: y = height-sh2-1
    if y <= 0+sh2: y = sh2+1
    displayRec(img, color_rgb, x, y)


def createRec(img, color_rgb, posx, posy):

    west = int(posx-(slider_width/2))
    east = int(posx+(slider_width/2))
    north = int(posy-(slider_height/2))
    south = int(posy+(slider_height/2))

    img = np.zeros_like(img)
    #NOTE-> "," separates dimensions of shape, ":" is for slicing
    img[north, west : east] = color_rgb
    img[south, west : east] = color_rgb
    img[north:south, west] = color_rgb
    img[north:south, east] = color_rgb
    return img


def randPixel():
    return np.array([r.randrange(0,255), r.randrange(0,255), r.randrange(0,255)])

cv2.namedWindow(windowName)
createSliderRGB()
createSliderHW()
cv2.imshow(windowName, img)
color_rgb = getSliderRGB()
cv2.setMouseCallback(windowName, rectMouse)

while True:
    key = cv2.waitKey(delay) & 0x0FF
    if key == ord('q'):
        break

    elif key == ord('n'):
        flag_rec = False
        displayBlack(img)

    elif key == ord('s'):
        flag_rec = False
        color_rgb = getSliderRGB() 
        img = np.full_like(img, color_rgb)
        cv2.imshow(windowName, img)

    #On considere que vaut pas le coup/cout d'isoler la section utilisant color_rgb dans un elif key = c||r

    if key == ord('c'):
        flag_rec = False
        color_rgb = randPixel() 
        img = np.full_like(img, color_rgb)
        cv2.imshow(windowName, img)

    elif key == ord('r'):
        if flag_rec == False:
            displayRec(img, color_rgb, width/2, height/2)
            flag_rec = not flag_rec
        else:
            displayBlack(img)
            flag_rec = not flag_rec


