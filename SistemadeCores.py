import cv2

img = cv2.imread('img/Lenna.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow('Original', img)
cv2.imshow('Gray', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('L*a*b', lab)
cv2.waitKey(0)
