import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('../imgs/image-banane-dl23207.webp')
histo_grey = np.zeros((256,1), np.float32)

# cv2.imshow('TP1a_EX1', image)

# for i in range(0,256):
    # histo_grey[]

plt.figure()
plt.title("Histogramme")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histo_grey)
plt.xlim([0,255])
plt.show(block=False)

cv2.waitKey(0)
plt.close('all')
cv2.destroyAllWindows()

# cv2.calcHist(image, 0
