import numpy as np
import cv2

imagem = cv2.imread('img/Lenna2.png')

# slicing
# img[30:50, :] = (255, 0, 0) # pega da linha 31 até a 50, pegando todas as colunas
# img[30:50, 3: 10] = (255, 0, 0) # pega da linha 31 até a 50, pegando as colunas 4 a 10


vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)

cv2.line(imagem, (0, 0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)

(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
for raio in range(0, 175, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)

