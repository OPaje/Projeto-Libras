import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]

suave = np.vstack([
    np.hstack([img,
               cv2.bilateralFilter(img, 3, 21, 21)]),
    np.hstack([cv2.bilateralFilter(img, 5, 35, 35),
               cv2.bilateralFilter(img, 7, 49, 49)])
])

cv2.imshow('Suavizacao Filtro Bilateral', suave)
cv2.waitKey(0)
