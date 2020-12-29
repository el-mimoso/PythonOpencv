import cv2
import numpy as np

print("Package imported")

img = cv2.imread("Assets/io.jpg")
print(img.shape)
chica = cv2.resize(img, (254, 254))

imgcrop = img[0:200, 20:500]
cv2.imshow('Images', imgcrop)
cv2.waitKey(0)
