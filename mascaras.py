import cv2
import numpy as np

img = cv2.imread('img/Lenna.png')
cv2.imshow('Original', img)

mascara = np.zeros(img.shape[:2], dtype="uint8")

(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)  # achando o centro
cv2.circle(mascara, (cX, cY), 250, 255, -1)

img_com_mascara = cv2.bitwise_and(img, img, mask=mascara)
cv2.imshow("Mascara", img_com_mascara)
cv2.waitKey(0)
