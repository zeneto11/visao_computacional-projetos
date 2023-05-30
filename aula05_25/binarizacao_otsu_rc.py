import numpy as np
import cv2

img = cv2.imread('aula05_25/vingadores.png') # obter a imagem
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # deixar preto e branco

suave = cv2.GaussianBlur(img, (7,7), 0) # aplica blur

# binarização
bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5) 
# bin. invert.
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5) 

resultado = np.vstack([ # junta duas imagens em uma janela
    np.hstack([img, suave]),
    np.hstack([bin1, bin2])
])

# mostrar imagem
cv2.imshow("Binarizacao da imagem", resultado)
cv2.waitKey(0)
