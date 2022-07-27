import numpy as np
import cv2

# ler uma imagem
img = cv2.imread("img/Lenna.png")

print('Largura em pixels: ', end='')
print(img.shape[1])  # mostra a largura da imagem
print('Altura em pixels: ', end='')
print(img.shape[0])  # mostra a altura da imagem
print('Quantidade de canais: ', end='')
print(img.shape[2])  # mostra a quantidade de canais

# mostrar uma imagem
cv2.imshow("Lenna", img)
cv2.waitKey(0)  # espera pressionar qualquer tecla para fechar a janela da imagem

# O comando imwrite serve para salvar uma imagem
cv2.imwrite("Lenna2.png", img)

