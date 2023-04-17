#計算各輪廓面積並篩選 cv2.contourArea()
import cv2
import numpy as np
o = cv2.imread('C:\\Users\\User\\Desktop\\Ben\\AI\\contours.png')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("o", o)
n = len(contours)
contoursImg = []
for i in range(n):
    print("contours["+ str(i) +"]面積 = ", cv2.contourArea(contours[i]))
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(
        contoursImg[i], contours, i, (255, 255, 255), 3)
    if cv2.contourArea(contours[i]) > 8000:
        cv2.imshow("contours[" + str(i) +"]", contoursImg[i])
cv2.waitKey()
cv2.destroyAllWindows()