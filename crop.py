import cv2

img = cv2.imread('img/Lenna.png')

#  crop serve para recortar a imagem

           #  linha     coluna
recorte = img[100:500, 100:500]
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey()

cv2.imshow('Lenna', img)
cv2.waitKey()

cv2.imwrite('img/Recorte_Lenna.png', recorte)
