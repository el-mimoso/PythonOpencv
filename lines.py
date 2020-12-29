import cv2
import numpy as np

print("Package imported")

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (150, 150), (0, 254, 0), 2)
cv2.rectangle(img, (250, 10), (270, 50), (0, 0, 100), 2)
cv2.circle(img, (250, 250), 100, (150, 20, 0), cv2.FILLED)
cv2.putText(img, 'Figuras, linea y texto en openCV',(0,500),cv2.FONT_HERSHEY_SIMPLEX, 1,(254,254,254),2)
cv2.imshow("Linea en imagen", img)

cv2.waitKey(0)
