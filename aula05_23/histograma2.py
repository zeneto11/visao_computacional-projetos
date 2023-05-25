from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('aula05_23/ademir-comunista.jpeg')
cv2.imshow("Imagem Colorida", img)

#Separa os canais
canais = cv2.split(img)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cor)
    plt.xlim([0, 256])
plt.show()