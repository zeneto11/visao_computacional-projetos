import cv2
import numpy as np
from matplotlib import pyplot as plt

def motionDetection():
    cap = cv2.VideoCapture(0) # obter a captura da câmera do pc (0)

    ret, frame1 = cap.read() # imagem 1
    ret, frame2 = cap.read() # imagem 2

    while cap.isOpened():
        # subtração das images que detecta o movimento
        diff = cv2.absdiff(frame1, frame2)
        # deixar preto e branco
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # binarização
        blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        # achar movimentos
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # desenhar onde estiver tendo movimento
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 500:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('te peguei'), (10, 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # mostrar webcam
        cv2.imshow("Detector de movimentos", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(50) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


motionDetection()
