import numpy as np
import cv2

img = cv2.imread('aula05_25/vingadores.png') # obter a imagem
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # deixar preto e branco

suave = cv2.GaussianBlur(img, (7,7), 0) # aplica blur

# binarização
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY) 
# bin. invert.
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV) 

resultado = np.vstack([ # junta duas imagens em uma janela
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask=binI)])
])

# mostrar imagem
cv2.imshow("Binarizacao da imagem", resultado)
cv2.waitKey(0)
