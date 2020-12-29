import cv2
import numpy as np

img = cv2.imread("Assets/baraja.png")
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
width, height = 250, 350

pts1 = np.float32([[242, 11], [372, 55], [165, 226], [305, 270]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
warp = cv2.warpPerspective(img, matrix, (width, height))

for x in range (0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, red, cv2.FILLED)

cv2.imshow("original image", img)
cv2.imshow("warp", warp)
cv2.waitKey(0)
