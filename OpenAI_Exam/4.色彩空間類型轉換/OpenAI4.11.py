import cv2
img = cv2.imread("Cutie.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v[:,:] = 255
newHSV = cv2.merge([h,s,v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)
cv2.imshow("cutie", img)
cv2.imshow("art", art)
cv2.waitKey()
cv2.destroyAllWindows()