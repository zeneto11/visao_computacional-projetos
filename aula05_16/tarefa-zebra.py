import cv2

imagem = cv2.imread('aula05_16/images/zebra.jpg') # obter a imagem

for y in range(imagem.shape[0]):
    for x in range(imagem.shape[1]):
        (b, g, r) = imagem[y, x]
        if (b > 200) and (g > 200) and (r > 200):
            imagem[y, x] = (0, 0, 255)

cv2.imshow('Zebra dos cria', imagem) # exibir imagem em uma nova janela
cv2.waitKey(0) # faz com que a imagem fique sendo mostrada

cv2.imwrite('aula05_16/images/zebra-flamenguista.jpg', imagem) # exportar arquivo da imagem