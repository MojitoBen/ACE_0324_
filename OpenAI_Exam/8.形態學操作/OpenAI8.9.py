#形態學梯度運算
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
kernel = np.ones((5,5),np.uint8)
r= cv2.morphologyEx(o, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("o", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()