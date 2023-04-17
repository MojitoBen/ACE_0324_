#計算輪廓長度 cv2.arcLength()
import cv2
import numpy as np
o = cv2.imread('C:\\Users\\User\\Desktop\\Ben\\AI\\contours.png')
cv2.imshow("o", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
cntLen = []
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print("第"+str(i)+"個輪廓的長度:%d" %cntLen[i])
cntLenSum = np.sum(cntLen)
cntLenAvr = cntLenSum/n
print("輪廓的總長度為:%d"%cntLenSum)
print("輪廓的平均長度為:%d"%cntLenAvr)
contoursImg = []
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255,255,255), 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        cv2.imshow("contours[" + str(i) +"]", contoursImg[i])
cv2.waitKey()
cv2.destroyAllWindows()