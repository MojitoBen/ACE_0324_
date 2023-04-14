#2D旋積濾波
import numpy as np
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
kernel = np.ones((9,9), np.float32)/81
r = cv2.filter2D(o, -1, kernel)
cv2.imshow("img", o)
cv2.imshow("filter2D", r)
cv2.waitKey()
cv2.destroyAllWindows()