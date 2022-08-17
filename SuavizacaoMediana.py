import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]

suave = np.vstack([
    np.hstack([img,
               cv2.medianBlur(img, 3)]),
    np.hstack([cv2.medianBlur(img, 5),
               cv2.medianBlur(img, 7)])
])

cv2.imshow('Suavizacao pela Mediana', suave)
cv2.waitKey(0)

