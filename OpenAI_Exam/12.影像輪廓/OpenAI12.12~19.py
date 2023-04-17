#繪製矩形包圍框
import cv2
import numpy as np
o = cv2.imread('C:\\Users\\User\\Desktop\\Ben\\AI\\1.jpg')
cv2.imshow("o", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
'''
x, y, w, h = cv2.boundingRect(contours[0])
brcnt = np.array([[x,y], [x+w, y], [x+w,y+h], [x,y+h]])
o2 = cv2.drawContours(o, [brcnt], -1, (255,255,255), 2)
cv2.imshow("result12.12", o2)

o3 = cv2.rectangle(o, (x,y), (x+w,y+h),(255,255,255),2)
cv2.imshow("result12.13", o3)

rect = cv2.minAreaRect(contours[0])
points = cv2.boxPoints(rect)
points = np.int0(points)
o4 = cv2.drawContours(o, [points], 0, (0,0,255), 2)
cv2.imshow("result12.14", o4)


'''

cv2.waitKey()
cv2.destroyAllWindows()