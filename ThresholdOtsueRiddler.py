import cv2
import numpy as np
import mahotas

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.bilateralFilter(img, 7, 49,  49)

# por Otsu
T = mahotas.thresholding.otsu(suave)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)

# por Riddler-Calvard
T = mahotas.thresholding.rc(suave)
temp2 = img.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp = cv2.bitwise_not(temp2)

resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([temp, temp2])
])

cv2.imshow('Threshold Otsu e Riddler-Clavard', resultado)
cv2.waitKey(0)
