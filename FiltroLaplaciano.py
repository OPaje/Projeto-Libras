import numpy as np
import cv2

img = cv2.imread('img/Lenna.png')
img = img[::2, ::2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (3, 3), 0)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

lapBlur = cv2.Laplacian(suave, cv2.CV_64F)
lapBlur = np.uint8(np.absolute(lapBlur))


resultado = np.vstack([
    np.hstack([img, lap]),
    np.hstack([suave, lapBlur])
])

cv2.imshow('Filtro Laplaciano', resultado)
cv2.waitKey(0)
