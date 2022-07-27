import numpy as np
import imutils
import cv2

#  O resize serve para redimensionar a imagem

img = cv2.imread('img/Lenna.png')

# altura = img.shape[0]
# largura = img.shape[1]
# print(altura, largura)
#
# # é preciso calcular a proporção para que a imagem não fique distorcida
# proporcao = float(altura/largura)
# print(proporcao)
#
# largura_nova = 350  # em pixels
# altura_nova = int(largura_nova*proporcao)
# print(altura_nova)
#
# tamanho_novo = (largura_nova, altura_nova)
# print(tamanho_novo)
#
# #  cv2.INTER_AREA é a especificação do cálculo matemático para redimensionar a imagem
# img_redimensionada = cv2.resize(img, tamanho_novo, interpolation=cv2.INTER_AREA)
# cv2.imshow('Resultado', img_redimensionada)
# cv2.waitKey(0)
#
# cv2.imshow('Lenna', img)
# cv2.waitKey()

# usando slicing para redimensionar


cv2.imshow("Original", img)
cv2.waitKey()

img_redimensionada = img[::2, ::2]  # pulando pega uma linha/coluna e ignora a outra
# a imagem vai ficar com a metada da altura e da largura da original
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)

