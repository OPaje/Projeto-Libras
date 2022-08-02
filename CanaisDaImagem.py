import cv2

img = cv2.imread('img/Lenna.png')

altura = img.shape[0]
largura = img.shape[1]

proporcao = float(altura/largura)

largura_nova = 380  # em pixels
altura_nova = int(largura_nova*proporcao)

tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img, tamanho_novo, interpolation=cv2.INTER_AREA)

# Uma imagem possui no padrão RGB possui 3 canais, um para cada cor
# Use a função split para separar os canais
(canalAzul, canalVerde, canalVermelho) = cv2.split(img_redimensionada)

# Juntando os canais
juntando = cv2.merge([canalAzul, canalVerde, canalVermelho])

cv2.imshow('Original', img_redimensionada)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.imshow("Canais Juntados", juntando)
cv2.waitKey(0)

