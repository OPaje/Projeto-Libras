import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (3, 3), 0)

#  valores menores que o limiar 1 não são considerados bordas
#  valores maiores que o limiar 2 são considerados bordas
#  valores entre os limiares dependem de como eles estão conectados para serem considerados bordas ou não
canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 200)

resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([canny1, canny2])
])

cv2.imshow('Canny', resultado)
cv2.waitKey(0)
