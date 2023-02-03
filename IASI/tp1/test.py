import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

height = 800
width = 600

img = np.zeros((height,width,3), np.uint8)

img2 = np.zeros_like(img)

print("SHAPE:")
print(img.shape)

print("PIXEL VAL:")
#Visualiser img sous format rgb (0->255x3)
(b, g, r) = img[100,100]
print(b, g, r)
img[100,100]=[255,255,255]
(b, g, r) = img[100,100]
print(b, g, r)

#Visualiser img sous format greypixel (0->255)
gray = img[100,100]
img[100,100]=196

(B,G,R) = cv2.split(img)
print("BLUE :\n", B, b)
print("RED :\n", R, r)
print("GREEN :\n", G, g)

img = cv2.merge((B,G,R))
#print(img)

grey_converted = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(grey_converted)

#cv2.resize(s,size,fx,fy,interpolation)

cv2.namedWindow("IMG_BASE")
cv2.imshow("IMG_BASE",img)
delay = 3000
cv2.waitKey(delay)
