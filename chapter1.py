from cv2 import cv2
print("Package imported")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img= cap.read()
    cv2.imshow('salida de video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break