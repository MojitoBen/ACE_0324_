#核函數
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_UNCHANGED)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (10,10))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
dst1 = cv2.dilate(o, kernel1)
dst2 = cv2.dilate(o, kernel2)
dst3 = cv2.dilate(o, kernel3)
cv2.imshow("o", o)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey()
cv2.destroyAllWindows()