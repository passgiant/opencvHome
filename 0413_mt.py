import cv2
src = cv2.imread('./opencv_mycode/data/lena.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)

cv2.waitKey()
cv2.destroyAllWindows()