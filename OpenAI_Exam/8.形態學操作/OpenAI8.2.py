#腐蝕
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_UNCHANGED)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(o, kernel)
cv2.imshow("o", o)
cv2.imshow("erosion", erosion)
cv2.waitKey()
cv2.destroyAllWindows()