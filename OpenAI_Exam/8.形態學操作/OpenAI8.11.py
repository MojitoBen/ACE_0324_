#黑帽運算
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_UNCHANGED)
o2 = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\BG.png", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(o, cv2.MORPH_BLACKHAT, kernel)
r2 = cv2.morphologyEx(o2, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("o", o)
cv2.imshow("or", r1)
cv2.imshow("o2", o2)
cv2.imshow("o2r", r2)
cv2.waitKey()
cv2.destroyAllWindows()