#閉運算
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
o2 = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\BG.png")
kernel = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(o, cv2.MORPH_OPEN, kernel)
r2 = cv2.morphologyEx(o2, cv2.MORPH_OPEN, kernel)
cv2.imshow("o", o)
cv2.imshow("or", r1)
cv2.imshow("o2", o2)
cv2.imshow("o2r", r2)
cv2.waitKey()
cv2.destroyAllWindows()