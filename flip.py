import cv2

#  O flip é usado para espelhar uma imagem

img = cv2.imread('img/Lenna.png')
img_redimensionada = img[::2, ::2]
cv2.imshow('Original', img_redimensionada)


# flip_horizontal = img_redimensionada[:, ::-1]  # invertendo direto nas matrizes
flip_horizontal = cv2.flip(img_redimensionada, 1)  # invertendo usando a função flip
cv2.imshow('Flip Horizontal', flip_horizontal)

# flip_vertical = img_redimensionada[::-1, :]
flip_vertical = cv2.flip(img_redimensionada, 0)
cv2.imshow('Flip Vertical', flip_vertical)

# flip_vertical_horizontal = img_redimensionada[::-1, ::-1]
flip_vertical_horizontal = cv2.flip(img_redimensionada, -1)
cv2.imshow('Vertical e Horizontal', flip_vertical_horizontal)

cv2.waitKey()

