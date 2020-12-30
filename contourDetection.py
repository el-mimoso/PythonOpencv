import cv2
import numpy as np
import myUtils

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("Parametros")
cv2.resizeWindow("Parametros", 640, 240)
cv2.createTrackbar("Threshold1", "Parametros", 150, 255, empty)
cv2.createTrackbar("Threshold2", "Parametros", 255, 255, empty)
cv2.createTrackbar("Area", "Parametros", 500, 3000, empty)


# cap.set(10, 150)

def getContours(img, imgCountour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area","Parametros")
        if area > areaMin:
            cv2.drawContours(imgCountour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgCountour, (x, y), (x + w, y + h), (0, 255, 0), 5)

            cv2.putText(imgCountour, "Points" + str(len(approx)), (x + w + 20, y + h + 20),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(imgCountour, "Area" + str(int(area)), (x + w + 20, y + h + 40),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


while True:
    success, img = cap.read()
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parametros")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parametros")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgContour)

    imgStack = myUtils.stackImages(0.5, ([img, imgCanny, imgDil, imgContour]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
