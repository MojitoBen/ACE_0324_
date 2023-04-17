#分析影像特徵
import cv2
import numpy as np
o = cv2.imread('C:\\Users\\User\\Desktop\\Ben\\AI\\contours.png')
cv2.imshow("o", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
contoursImg = []
for i in range(n):
    temp = np.zeros(binary.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, 255, 3)
    cv2.imshow("contours["+ str(i) +"]", contoursImg[i])
print("觀察各個輪廓的矩")
for i in range(n):
    print("輪廓"+ str(i) + "的矩 : \n", cv2.moments(contours[i]))
print("觀察各個輪廓的面積")
for i in range(n):
    print("輪廓"+ str(i) + "的面積 : %d" %cv2.moments(contours[i])['m00'])
cv2.waitKey()
cv2.destroyAllWindows()