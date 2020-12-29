import cv2
import numpy as np
import myUtils
#preparar alto y ancho del video
frameWidth = 640
frameHeight = 480

#invocar a la webcam
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    kernel = np.ones((5, 5), np.uint8)
    print(kernel)
    # path = "Assets/chily.png"
    # img = cv2.imread(path)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

    # imgBlank = np.zeros((200, 200), np.uint8)

    StackedImages = myUtils.stackImages(([img, imgGray, imgBlur],
                                         [imgCanny, imgDilation, imgEroded]), 0.3)

    cv2.imshow("Staked Images", StackedImages)

    #mientras esto pasa obtenemos cada imagen si no solo toma cada que aprietas una tecla xD
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
