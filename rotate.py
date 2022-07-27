import cv2

img = cv2.imread('img/Lenna.png')

(altura, largura) = img.shape[:2]  # captura a altura e a largura
centro = (largura // 2, altura // 2)

graus = cv2.getRotationMatrix2D(centro, 45, 1.0)  # 45 graus

img_rotacionada = cv2.warpAffine(img, graus, (largura, altura))

cv2.imshow('Imagem Rotacionada em 45 Graus', img_rotacionada)

cv2.waitKey()