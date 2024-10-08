import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./opencv_mycode/data/lena.jpg')
histColor = ('b', 'g', 'r')
for i in range(3):
    hist = cv2.calcHist(images=[src], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color = histColor[i])
plt.show()