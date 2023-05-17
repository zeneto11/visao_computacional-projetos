import cv2

imagem = cv2.imread('wallpaper_hypnotize_IA.jpg') # obter a imagem

cv2.imshow('Nome da janela', imagem) # exibir imagem em uma nova janela
cv2.waitKey(0) # faz com que a imagem fique sendo mostrada

print(imagem.shape[0]) # altura da imagem
print(imagem.shape[1]) # largura da imagem
print(imagem.shape[2]) # quantidade de canais da imagem

cv2.imwrite('novo_arquivo.jpg', imagem) # exportar arquivo da imagem