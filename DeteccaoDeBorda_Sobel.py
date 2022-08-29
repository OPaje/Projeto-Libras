import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3, 3), 0)

# trabalhando com a imagem com ponto flutuante de 64 bits
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# convertendo para uint8

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

resultado = np.vstack([
    np.hstack([img, sobelX]),
    np.hstack([sobelY, sobel])
])

cv2.imshow('Sobel', resultado)
cv2.waitKey(0)
