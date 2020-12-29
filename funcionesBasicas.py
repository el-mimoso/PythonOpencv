import cv2
import numpy as np
print("Package imported")

img = cv2.imread("Assets/io.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 200, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)

# cv2.imshow("simagen en escala de gris", imgGray)
# cv2.imshow("imagen en desenfocada", imgBlur)
cv2.imshow("imagen en borde", imgCanny)
cv2.imshow("imagen en dilatada", imgDilation)
cv2.waitKey(0)
