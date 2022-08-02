import cv2
import numpy as np

img = cv2.imread('img/Lenna.png')

altura = img.shape[0]
largura = img.shape[1]

proporcao = float(altura/largura)

largura_nova = 380  # em pixels
altura_nova = int(largura_nova*proporcao)

tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img, tamanho_novo, interpolation=cv2.INTER_AREA)

(canalAzul, canalVerde, canalVermelho) = cv2.split(img_redimensionada)
zeros = np.zeros(img_redimensionada.shape[:2], dtype='uint8')

cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))

cv2.imshow('Original', img_redimensionada)
cv2.waitKey(0)

