import cv2
import numpy as np

from pyzbar.pyzbar import decode

# img = cv2.imread('Qr/img.png')
cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 480)

while True:
    succes, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 0), 5)
        pts2 = barcode.rect
        #Cambiamos el color del cuadro si es una pag autorizada
        if myData == 'http://combizona.com':
            colorTxt = (255, 50, 50)
        else:
            colorTxt = (0, 0, 255)
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                    0.9, colorTxt, 2)
    cv2.imshow("Result", img)
    cv2.waitKey(1)
