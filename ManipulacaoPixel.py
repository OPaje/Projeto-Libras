import cv2

img = cv2.imread('img/Lenna2.png')

# colocando em uma tupla os valores do pixel da posição (0,0)
(b, g, r) = img[0, 0]  # o método retorna o padrão BGR

print('O pixel (0,0) tem as seguintes cores: ')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# Muda todos os pixel para azul
# for y in range(0, img.shape[0]):  # percorre as linhas
#     for x in range(0, img.shape[1]):  # percorre as colunas
#         img[y, x] = (255, 0, 0) # padrão BGR

# for y in range(0, img.shape[0]):
#     for x in range(0, img.shape[1]):
#         img[y, x] = (x % 256, y % 256, x % 256) # usa % 256 para manter os valores entre 0 e 255

# for y in range(0, img.shape[0], 1):
#     for x in range(0, img.shape[1], 1):
#         img[y, x] = ((x*y) % 256, 0, 0) # forma um determinado padrão na cor azul

# criando um pixel amarelo de 5x5 na imagem a cada salto
for y in range(0, img.shape[0], 10):  # percorre as linhas saltando de 10 em 10
    for x in range(0, img.shape[1], 10):  # percorre as colunas saltando de 10 em 10
        img[y: y+5, x: x+5] = (0, 255, 255) # criando o pixel amarelo de 5x5


cv2.imshow("Imagem modificada", img)
cv2.waitKey(0)
