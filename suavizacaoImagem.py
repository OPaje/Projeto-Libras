import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]  # diminuindo a imagem usando slicing

# juntando as imagens em uma só
# suavização por cálculo da média(blur)
suave = np.vstack([
    np.hstack([img,                   cv2.blur(img, (3, 3))]),
    np.hstack([cv2.blur(img, (5, 5)), cv2.blur(img, (7, 7))]),
    np.hstack([cv2.blur(img, (9, 9)), cv2.blur(img, (11, 11))]),
])

cv2.imshow('Blur', suave)
cv2.waitKey(0)

