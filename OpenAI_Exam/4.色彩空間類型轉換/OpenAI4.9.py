import cv2
import numpy as np 
cutie = cv2.imread("Cutie.png")
hsv = cv2.cvtColor(cutie, cv2.COLOR_BGR2HSV)
cv2.imshow("cutie", cutie)
#==========指定藍色值範圍==========
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
mask = cv2.inRange(hsv, minBlue, maxBlue)
blue = cv2.bitwise_and(cutie, cutie, mask=mask)
cv2.imshow("blue", blue)
#==========指定綠色值範圍==========
mingreen = np.array([50,50,50])
maxgreen = np.array([70,255,255])
mask = cv2.inRange(hsv, mingreen, maxgreen)
green = cv2.bitwise_and(cutie, cutie, mask=mask)
cv2.imshow("green", green)
#==========指定紅色值範圍==========
minred = np.array([0,50,50])
maxred = np.array([30,255,255])
mask = cv2.inRange(hsv, minred, maxred)
red = cv2.bitwise_and(cutie, cutie, mask=mask)
cv2.imshow("red", red)
cv2.waitKey()
cv2.destroyAllWindows()