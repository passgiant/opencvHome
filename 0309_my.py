import numpy as np
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
text = 'OpenCV Programming'
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text, org, font, 1, (255,0,0), 1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()