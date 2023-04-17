#抓取個別輪廓
import cv2
import numpy as np
o = cv2.imread('C:\\Users\\User\\Desktop\\Ben\\AI\\contours.png')
cv2.imshow("o", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)
contoursImg = []
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, (0, 0, 255), 5)
    cv2.imshow("contours[" + str(i) +"]", contoursImg[i])
cv2.waitKey()
cv2.destroyAllWindows()