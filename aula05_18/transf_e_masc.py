import cv2

captura = cv2.VideoCapture(0) # obter a captura da câmera do pc (0)

while (1): # loop para continuar aparecendo
    ret,imagem = captura.read() # atribuir a cap
    
    largura = imagem.shape[1]
    altura = imagem.shape[0]
    proporcao = float(altura/largura)

    largura_nova = 500
    altura_nova = int(largura_nova * proporcao)
    tamanho_novo = (largura_nova, altura_nova)
    
    imagem_nova = cv2.resize(imagem, tamanho_novo, interpolation=cv2.INTER_AREA)

    cv2.imshow('video', imagem_nova) # mostrar a imagem na tela
    flip_horizontal = imagem_nova[::-1,:] #comando equivalente abaixo
    #flip_horizontal = cv2.flip(imagem_nova, 1)
    cv2.imshow("Flip Horizontal", flip_horizontal)
    flip_vertical = imagem_nova[:,::-1] #comando equivalente abaixo
    #flip_vertical = cv2.flip(imagem_nova, 0)
    cv2.imshow("Flip Vertical", flip_vertical)
    flip_hv = imagem_nova[::-1,::-1] #comando equivalente abaixo
    #flip_hv = cv2.flip(imagem_nova, -1)
    cv2.imshow("Flip Horizontal e Vertical", flip_hv)
    
    # condição de saída
    k = cv2.waitKey(30)&0xff 
    if k==27: # apertar "ESC" para finalizar
        break

captura.release()
cv2.destroyAllWindows()