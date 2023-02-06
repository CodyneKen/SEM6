import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import random as r



#trouver comment declarer img une seule fois et réassigner les valeurs

def main():
    height = 480
    width = 640
    delay = 1000

    cv2.namedWindow('EX1_COLOR')
    createSliderRGB('EX1_COLOR')
    img = np.zeros((height,width,3), np.uint8)

    while True:
        key = cv2.waitKey(delay) & 0x0FF
        if key == ord('q'):
            break

        if key == ord('n'):
            img = np.zeros_like(img)
            cv2.imshow('EX1_COLOR', img)


        if key == ord('s'):
            img = np.full_like(img, [slider_red, slider_green, slider_blue])
            cv2.imshow('EX1_COLOR', img)

        #delay d'1 sec potentiellement, donc on considere que vaut pas le coup/cout d'isoler la section utilisant color_rgb dans un elif key = c||r
        color_rgb = np.array([r.randrange(0,255),r.randrange(0,255),r.randrange(0,255)])

        if key == ord('c'):
            img = np.full_like(img, color_rgb )
            cv2.imshow('EX1_COLOR', img)

        if key == ord('r'):
            img = disp_rect(img, color_rgb)
            cv2.imshow('EX1_COLOR', img)

def createSliderRGB(windowName):
    cv2.createTrackbar("R", windowName, 100, 255, updateSliderR)
    cv2.createTrackbar("G", windowName, 100, 255, updateSliderG)
    cv2.createTrackbar("B", windowName, 100, 255, updateSliderB)

def updateSliderR(newval):
    global slider_red
    slider_red = newval
def updateSliderG(newval):
    global slider_green
    slider_green = newval
def updateSliderB(newval):
    global slider_blue
    slider_blue = newval


def disp_rect(img, color_rgb):

    height,width,x = img.shape

    west = int((width/2)-50)
    east = int((width/2)+50)
    north = int((height/2)-25)
    south = int((height/2)+25)

    img = np.zeros_like(img)
    #NOTE-> "," separates dimensions of shape, ":" is for slicing
    img[north, west : east] = color_rgb
    img[south, west : east] = color_rgb
    img[north:south, west] = color_rgb
    img[north:south, east] = color_rgb
    return img




main()
