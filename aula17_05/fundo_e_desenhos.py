import cv2
import numpy as np

canvas = np.ones((300, 400, 3)) * 255 # faz um fundo branco

# desenhar linha azul diagonal
azul = (255, 0, 0)
cv2.line(canvas, (0,0), (400,300), azul)

# desenhar linha verde vertical
verde = (0, 255, 0)
cv2.line(canvas, (200,0), (200,300), verde, 3)

# desenhar retângulo com borda verde
cv2.rectangle(canvas, (10,70), (90,190), verde)

# desenhar retângulo todo vermelho
vermelho = (0, 0, 255)
cv2.rectangle(canvas, (250,50), (300,125), vermelho, -1)

# desenhar círculo
preto = (0, 0, 0)
cv2.circle(canvas, (130,230), 50, preto)

cv2.imshow('Canvas', canvas) # exibe a imagem
cv2.waitKey(0)