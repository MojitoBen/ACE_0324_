import cv2
img = cv2.imread("Cutie.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
#色調值在5到170之間
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)
#飽和度值在25到166之間
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("cutie", img)
cv2.imshow("ROI", roi)
cv2.waitKey()
cv2.destroyAllWindows()