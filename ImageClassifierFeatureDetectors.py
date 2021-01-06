import cv2
import numpy as np
import os

path = 'ImgQuery'
images = []
classname = []
orb = cv2.ORB_create(nfeatures=1000)

mylist = os.listdir(path)
print('total classes detected', len(mylist))

for cl in mylist:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classname.append(os.path.splitext(cl)[0])
print(classname)


def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList


def findID(img, desList, thres=15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    if len(matchList)!=0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal


desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture(0)
while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    id=findID(img2,desList)
    if id != -1:
        cv2.putText(imgOriginal, classname[id],(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

    cv2.imshow('img2', imgOriginal)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# # cv2.imshow("GTA", img1)
# # cv2.imshow("CS", img2)

# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)


# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# cv2.imshow("img2", img1)
# cv2.imshow("img1 ", img2)
# cv2.imshow("img3 ", img3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
