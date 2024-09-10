import cv2
src = cv2.imread('./opencv_mycode/data/lena.jpg')

dst = cv2.split(src)
print(type(dst))
print(type(dst[0]))
#print(type(dst[1]))
#print(type(dst[2]))

cv2.imshow('blue', dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red', dst[2])
cv2.waitKey()
cv2.destroyAllWindows()