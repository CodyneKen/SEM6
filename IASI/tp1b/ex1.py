import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('../imgs/image-banane-dl23207.webp')
grey_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histo_grey = np.zeros((256,1), np.float32)

wait_time = 3000

cv2.imshow('TP1a_EX1', grey_converted)

# for i in range(0,256):
    # histo_grey[grey_converted[i]]+=1

plt.figure()
plt.title("Histogramme")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
# plt.plot(histo_grey)
plt.plot(cv2.calcHist([grey_converted],[0],None,[256], [0,256]))
plt.xlim([0,255])
plt.show(block=True)

cv2.waitKey(wait_time)

plt.close('all')
cv2.destroyAllWindows()

# cv2.calcHist(image, 0
