import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import random as r



#trouver comment declarer img une seule fois et réassigner les valeurs

def main():
    global height 
    global width 
    height = 480
    width = 640
    delay = 300

    flag_rec = False 
    windowName = 'EX2_COLOR'

    img = np.zeros((height,width,3), np.uint8)

    cv2.namedWindow(windowName)
    createSliderRGB(windowName)
    createSliderHW(windowName)
    cv2.imshow(windowName, img)
    color_rgb = getSliderRGB() 

    while True:
        key = cv2.waitKey(delay) & 0x0FF
        if key == ord('q'):
                break

        elif key == ord('n'):
            flag_rec = False
            displayBlack(windowName, img)


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
                displayRec(windowName, img, color_rgb)
                flag_rec = not flag_rec
            else:
                displayBlack(windowName, img)
                flag_rec = not flag_rec

def displayRec(windowName, img, color_rgb):
    img = createRec(img, color_rgb)
    cv2.imshow(windowName, img)


def displayBlack(windowName, img):
    img = np.zeros_like(img)
    cv2.imshow(windowName, img)
    return img

def randPixel():
    return np.array([r.randrange(0,255), r.randrange(0,255), r.randrange(0,255)])

def createSliderRGB(windowName):
    cv2.createTrackbar("R", windowName, 100, 255, updateSliderR)
    cv2.createTrackbar("G", windowName, 100, 255, updateSliderG)
    cv2.createTrackbar("B", windowName, 100, 255, updateSliderB)

def getSliderRGB():
    return np.array([slider_red, slider_green, slider_blue])

def updateSliderR(newval):
    global slider_red
    slider_red = newval
def updateSliderG(newval):
    global slider_green
    slider_green = newval
def updateSliderB(newval):
    global slider_blue
    slider_blue = newval

def createSliderHW(windowName):
    cv2.createTrackbar("Height", windowName, 50, height, updateSliderH)
    cv2.createTrackbar("Width", windowName, 100, width, updateSliderW)

def updateSliderH(newval):
    global slider_height
    slider_height = newval
def updateSliderW(newval):
    global slider_width
    slider_width = newval

def createRec(img, color_rgb):

    height,width,x = img.shape

    west = int((width/2)-(slider_width/2))
    east = int((width/2)+(slider_width/2))
    north = int((height/2)-(slider_height/2))
    south = int((height/2)+(slider_height/2))

    img = np.zeros_like(img)
    #NOTE-> "," separates dimensions of shape, ":" is for slicing
    img[north, west : east] = color_rgb
    img[south, west : east] = color_rgb
    img[north:south, west] = color_rgb
    img[north:south, east] = color_rgb
    return img




main()
