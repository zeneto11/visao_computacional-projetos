import cv2

imagem = cv2.imread('zebra.jpg') # obter a imagem

cv2.imshow('Zebra dos cria', imagem) # exibir imagem em uma nova janela
cv2.waitKey(0) # faz com que a imagem fique sendo mostrada


cv2.imwrite('zebra-flamenguista.jpg', imagem) # exportar arquivo da imagem