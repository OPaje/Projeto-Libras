import numpy as np
import cv2

imagem = cv2.imread('img/Lenna2.png')

fonte = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# parâmetros imagem, texto, posição, fonte, tamanho, cor, a espessura, tipo de linha
cv2.putText(imagem, 'Lenna', (5, 55), fonte, 1.5, (0, 0, 139), 1, cv2.LINE_AA)

cv2.imshow("Lenna", imagem)
cv2.waitKey()

cv2.imwrite('img/Lenna_Escrita.png', imagem)
