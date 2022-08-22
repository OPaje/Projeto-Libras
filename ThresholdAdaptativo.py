import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.bilateralFilter(img, 7, 49, 49)

bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)

bin3 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
bin4 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin1, bin2]),
    np.hstack([bin3, bin4])
])

cv2.imshow('Threshold Adaptativo', resultado)
cv2.waitKey(0)
