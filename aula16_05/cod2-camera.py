import cv2

captura = cv2.VideoCapture(0) # obter a captura da câmera do pc (0)

while (1): # loop para continuar aparecendo
    ret,imagem = captura.read() # atribuir a cap
    
    (b, g, r) = imagem[0,0] # selecionando 1° pixel da imagem
    print('| Vermelho', r, '| Verde', g, 'Azul', b) # descobrir qual valor do pixel especificado
    
    imagem[2,2] = (255, 0, 0) # deixando um pixel azul
    imagem[30:50,] = (255, 0, 0) # deixando uma faixa azul

    # escrever na imagem
    fonte = cv2.FONT_HERSHEY_TRIPLEX # definir fonte
    # definir onde e o que será escrito, posição, fonte e tamanho da fonte.
    cv2.putText(imagem, 'Zeneto', (15,65), fonte, 2, (255,255,255), 2, cv2.LINE_AA) 
    
    cv2.imshow('video', imagem) # mostrar a imagem na tela

    # condição de saída
    k = cv2.waitKey(30)&0xff 
    if k==27: # apertar "ESC" para finalizar
        break

captura.release()
cv2.destroyAllWindows()